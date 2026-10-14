#!/usr/bin/env python3
"""Contrôle : le rejeu de `referentiels/niches_sieges_20261004.tsv` sur l'annexe
des dépenses fiscales du PLF 2027.

Le référentiel portait 465 montants lus à l'annexe 3 au tome II du PLF 2026.
Le 20261012, l'auteure a fait rejouer ces montants sur l'annexe 1 au tome II du
PLF 2027, puis arbitré quatre cas (`methode/etats/REJEU_annexes_2027_20261012.md`).
Ce module relit l'annexe 2027, dans sa table digérée et versée
`referentiels/annexe_depenses_fiscales_2027.tsv` (`appareil/digerer_annexes_vm2027.py`),
ainsi que l'état d'avant rejeu. Il vérifie ensuite chaque ligne du référentiel écrit.
**Il ne lit aucune table produite par le rejeu.** Il refuse une table digérée dont
l'empreinte de pièce n'est pas celle du classeur sur lequel le rejeu a été joué
(`EMPREINTE_DF27`). La concordance de la table avec son classeur se prouve à part, par
`digerer_annexes_vm2027.py verifier`.

Une ligne du référentiel est dans un seul des cinq cas suivants, et le contrôle
vérifie ce que ce cas impose :

- **rejouée** : millésime « 2027 (prévision) », et le montant est celui de la
  colonne H de l'annexe 2027, au numéro de la ligne ;
- **sans effet budgétaire 2027** : l'annexe 2027 porte « - » en colonne H. Le
  millésime est 2027, le montant est 0 et l'observation porte la marque ;
- **rattachée** : le numéro de 2026 est absent de l'annexe 2027. La ligne porte
  un nouveau numéro de 2027, et son libellé à l'annexe 2027 est identique au
  libellé de l'ancien numéro. Celui-ci se lit à la colonne `objet_en_clair` de
  l'état d'avant rejeu, qui a gardé le libellé de l'annexe 2026 mais y a rendu
  l'espace insécable simple. La comparaison se fait donc après cette seule
  normalisation, U+00A0 → espace (`NORMALISATION_2026`). Le verbatim strict des
  deux classeurs a été prouvé au rejeu, état REJEU, § 1.2. L'ancien
  numéro est dit à l'observation, et la ligne suit ensuite l'un des deux cas
  qui précèdent ;
- **objet changé** : numéro inscrit à `OBJET_CHANGE` ci-dessous. Montant et
  millésime sont ceux d'avant rejeu, et l'observation porte le signalement ;
- **restée 2026** : aucun numéro de 2027 ne lui correspond. Elle est identique à
  l'état d'avant rejeu.

Hors de `montant_M_EUR`, `millesime_montant`, `observation` (où seul un ajout
est admis) et `numero` (pour une ligne rattachée), aucune colonne ne bouge.

Usage :
    python3 appareil/controle_rejeu_annexes_2027.py \\
        referentiels/niches_sieges_20261004.tsv \\
        referentiels/annexe_depenses_fiscales_2027.tsv
    ... --fautes   rejoue en plus le jeu de fautes

Aucun classeur n'est lu : tout est au dépôt. L'état d'avant rejeu se lit au
commit `BASE` par `git show`.
Code de retour non nul s'il reste une anomalie, ou si une faute injectée ne
mord pas.
"""

import csv
import io
import os
import subprocess
import sys

from digerer_annexes_vm2027 import lire as lire_digeree

BASE = '7c2ed1d'
EMPREINTE_DF27 = 'f0f0eac440ebe18be9a2d21fe5514f06451e7a1572712cbbbb694459cf891e89'
NORMALISATION_2026 = {'\u00a0': ' '}
CHEMIN = 'chantier/referentiels/niches_sieges_20261004.tsv'
MILLESIME = '2027 (prévision)'
MARQUE_SANS_EFFET = 'sans effet budgétaire 2027'
MARQUE_OBJET = "objet changé à l'annexe 2027 sous le même numéro"
MARQUE_RATTACHE = 'rattachée : ancien numéro '

# Exemption nommée et motivée : arbitrage de l'auteure du 20261012, point 4.
# Pour ces lignes, le libellé de l'annexe 2027 ajoute ou retire une catégorie
# de bénéficiaires, d'opérations, de produits ou de territoires, ou bien change
# de mécanisme. Elles restent sur leur montant 2026. La qualification relève du
# jugement : elle est motivée ligne à ligne à l'état REJEU, § 4.
OBJET_CHANGE = {
    '110249': 'territoires retirés : quartiers anciens dégradés et NPNRU',
    '110271': 'bénéficiaires : JEI à 30 % de R&D → JEI de rupture et JEI à impact',
    '120138': 'opérations : rupture conventionnelle → toute rupture du contrat',
    '230604': 'bénéficiaires : JEI et JEU → JEI à impact',
    '320121': 'produits : œuvres audiovisuelles ajoutées, production déléguée',
    '320147': 'bénéficiaires : investisseurs institutionnels → logement intermédiaire',
    '710101': 'opérations : transport aérien ajouté',
    '740107': 'mécanisme : remboursement forfaitaire → exonération dérogatoire',
    '800228': 'produits : gaz de pétrole liquéfiés ajoutés',
    '820204': 'opérations : ferroviaire → transports guidés, marchandises ajoutées',
    '90109': 'bénéficiaires et périodes : établissements commerciaux, artisanaux, de santé',
    '940204': 'produits : micro-hybrides exclus',
    '940205': 'produits : véhicules électriques → hybrides rechargeables',
}

COLONNES_LIBRES = ('montant_M_EUR', 'millesime_montant', 'observation', 'numero')


def normaliser_2026(s):
    for a, b in NORMALISATION_2026.items():
        s = s.replace(a, b)
    return s


def lire_annexe_2027(chemin):
    """numéro → (libellé verbatim, prévision 2027), depuis la table digérée versée."""
    sha, lignes = lire_digeree(chemin)
    if sha != EMPREINTE_DF27:
        raise SystemExit(f'table digérée sur une autre pièce : sha256 {sha}, attendu {EMPREINTE_DF27}')
    return {x['numero']: (x['libelle'], x['prevision_2027']) for x in lignes}


def libelles_2026(base_texte):
    """numéro 2026 → libellé de l'annexe 2026, tel que l'état d'avant rejeu le garde."""
    return {x['numero']: (x['objet_en_clair'], None) for x in lire_tsv(base_texte)}


def lire_tsv(texte):
    return list(csv.DictReader(io.StringIO(texte), delimiter='\t'))


def controle(texte, base_texte, a27, a26):
    anomalies = []
    base = {x['numero']: x for x in lire_tsv(base_texte)}
    lignes = lire_tsv(texte)
    if len(lignes) != len(base):
        anomalies.append(('compte', len(lignes), len(base)))
    vus = set()
    for x in lignes:
        n = x['numero']
        if not n:
            anomalies.append(('non sourcé', x['objet_en_clair'][:40]))
            continue
        obs = x['observation']
        ancien = n
        if MARQUE_RATTACHE in obs:
            ancien = obs.split(MARQUE_RATTACHE, 1)[1].split(' ', 1)[0]
            if ancien not in base or ancien in a27:
                anomalies.append(('rattachement sans objet', n, ancien))
                continue
            if n in base or n not in a27:
                anomalies.append(('rattachement introuvable', n, ancien))
                continue
            if normaliser_2026(a27[n][0]) != normaliser_2026(a26[ancien][0]):
                anomalies.append(('rattachement sur libellé non identique', n, ancien))
        b = base.get(ancien)
        if b is None:
            anomalies.append(('introuvable', n))
            continue
        if ancien in vus:
            anomalies.append(('doublon', ancien))
        vus.add(ancien)
        for k in x:
            if k not in COLONNES_LIBRES and x[k] != b[k]:
                anomalies.append(('colonne bougée', n, k))
        if not obs.startswith(b['observation']):
            anomalies.append(('observation réécrite', n))
        etat = (x['montant_M_EUR'], x['millesime_montant'])
        if ancien in OBJET_CHANGE:
            if etat != (b['montant_M_EUR'], b['millesime_montant']) or MARQUE_OBJET not in obs or n != ancien:
                anomalies.append(('objet changé non tenu', n))
            continue
        if n not in a27:
            if etat != (b['montant_M_EUR'], b['millesime_montant']) or obs != b['observation']:
                anomalies.append(('restée 2026 mais modifiée', n))
            rattachable = [k for k, v in a27.items() if k not in base
                           and normaliser_2026(v[0]) == normaliser_2026(a26[n][0])]
            if len(rattachable) == 1:
                anomalies.append(('rattachable non rattachée', n, rattachable[0]))
            continue
        h = a27[n][1]
        if x['millesime_montant'] != MILLESIME:
            anomalies.append(('rejouable non rejouée', n))
        elif h in ('-', ''):
            if x['montant_M_EUR'] != '0' or MARQUE_SANS_EFFET not in obs:
                anomalies.append(('sans effet mal porté', n, x['montant_M_EUR']))
        else:
            if x['montant_M_EUR'] != h:
                anomalies.append(('diverge', n, x['montant_M_EUR'], h))
            if MARQUE_SANS_EFFET in obs:
                anomalies.append(('marque sans effet sur ligne chiffrée', n))
    return anomalies, len(lignes)


def fautes(texte):
    """Les quatre fautes minimales, déclinées sur le référentiel."""
    L = texte.split('\n')
    h = L[0].split('\t')
    iN, iM, iY = h.index('numero'), h.index('montant_M_EUR'), h.index('millesime_montant')
    def ligne(pred):
        return next(i for i, l in enumerate(L[1:], 1) if l and pred(l.split('\t')))
    i_rej = ligne(lambda f: f[iY] == MILLESIME and f[iM].isdigit() and f[iM] != '0')
    i_obj = ligne(lambda f: f[iN] == '940205')
    def mut(i, col, val):
        M = [l.split('\t') for l in L]
        M[i][col] = val(M[i][col])
        return '\n'.join('\t'.join(m) for m in M)
    return {
        '1 valeur fausse au même repère': mut(i_rej, iM, lambda v: str(int(v) + 1)),
        '2 repère qui ne résout pas': mut(i_rej, iN, lambda v: '999999'),
        '3 repère retiré': mut(i_rej, iN, lambda v: ''),
        '4 verdict retourné : objet changé déclaré rejoué': mut(i_obj, iY, lambda v: MILLESIME),
    }


def main(argv):
    tsv, x27 = argv[1:3]
    racine = subprocess.run(['git', '-C', os.path.dirname(os.path.abspath(tsv)), 'rev-parse', '--show-toplevel'],
                            capture_output=True, text=True, check=True).stdout.strip()
    base = subprocess.run(['git', '-C', racine, 'show', f'{BASE}:{CHEMIN}'],
                          capture_output=True, text=True, check=True).stdout
    a27, a26 = lire_annexe_2027(x27), libelles_2026(base)
    texte = open(tsv, encoding='utf-8').read()
    anomalies, n = controle(texte, base, a27, a26)
    print(f'{n} lignes contrôlées, {len(anomalies)} anomalie(s)')
    for a in anomalies:
        print('  ', *a)
    ok = not anomalies
    if '--fautes' in argv:
        for nom, t in fautes(texte).items():
            r, _ = controle(t, base, a27, a26)
            print(f"faute {nom} : {'mord' if r else 'NE MORD PAS'}", r[:1])
            ok &= bool(r)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
