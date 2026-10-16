#!/usr/bin/env python3
"""Génère les pièces de crédits de la liasse P2 depuis la chaîne.

Une mission, un amendement. Les montants viennent de `chaine_credits.py` ;
rien n'est écrit à la main. L'exposé se construit des seuls faits mesurés :
crédits ouverts au texte déposé, catégories touchées, date d'effet.
"""
import sys, csv
sys.path.insert(0, 'appareil')
import pandas as pd
from chaine_credits import DATE_CAT, FRACTION, residuel, norm, INDEMNITE
from collections import defaultdict

NB = ' '
def eur(n): return f'{int(round(n)):,}'.replace(',', NB)

CAT_NOM = {21: 'rémunérations', 22: 'cotisations sociales', 23: 'avantages salariaux',
           31: 'fonctionnement courant', 32: 'subventions pour charges de service public',
           51: 'investissement de l’État', 52: 'investissement de l’État',
           53: 'investissement de l’État', 61: 'transferts aux ménages',
           62: 'transferts aux entreprises', 63: 'transferts aux collectivités',
           64: 'transferts aux autres collectivités'}

def charger(X):
    eb, t2, cur = {}, {}, None
    for r in csv.DictReader(open('referentiels/etatB_2027_bg.tsv'), delimiter='\t'):
        if r['rang'] == 'programme':
            cur = norm(r['libelle']); eb[cur] = (int(r['ae']), int(r['cp']))
        elif r['rang'] == 'titre2' and cur:
            t2[cur] = int(r['ae'])
    d = pd.read_excel(X, 'A — Crédits', header=0)
    d.columns = [str(c).strip() for c in d.columns]
    d = d[(d['Statut doctrine'] == 'arrêté') & (d['AE arrêtées (M€)'].astype(float) > 0)]
    par = defaultdict(lambda: defaultdict(lambda: [0.0, 0.0, set(), set()]))
    for _, r in d.iterrows():
        t, c = int(r['Titre']), int(r['Catégorie'])
        p, m = str(r['Libellé programme']), str(r['Mission'])
        dt = DATE_CAT.get(c)
        if dt is None or norm(p) not in eb: continue
        fr = FRACTION[dt]; res = residuel(t, c)
        a = 0.90 if t == 2 else 1.0
        net = (1 - INDEMNITE) if t == 2 else 1.0
        par[m][p][0] += float(r['AE arrêtées (M€)']) * 1e6 * a * fr * net
        par[m][p][1] += min(float(r['CP arrêtés (M€)']), float(r['AE arrêtées (M€)'])) * 1e6 * a * fr * (1 - res) * net
        par[m][p][2].add(c); par[m][p][3].add(dt)
    return eb, t2, par

def piece(n, mission, lignes, eb, t2):
    sae = sum(l[1] for l in lignes); scp = sum(l[2] for l in lignes)
    cats = sorted({c for l in lignes for c in l[3]})
    dates = sorted({d for l in lignes for d in l[4]})
    o = []
    o.append(f'## Amendement n° {n} — mission «{NB}{mission}{NB}»\n')
    o.append('ARTICLE 58\n')
    o.append(f'Modifier ainsi les crédits de la mission «{NB}{mission}{NB}» :\n')
    o.append('| Programmes | AE + | AE − | CP + | CP − |')
    o.append('|---|---:|---:|---:|---:|')
    for p, ae, cp, _, _, t2m in lignes:
        o.append(f'| {p} | 0 | {eur(ae)} | 0 | {eur(cp)} |')
        if t2m: o.append(f'| *dont titre 2* | 0 | {eur(t2m)} | 0 | {eur(t2m)} |')
    o.append(f'| **TOTAUX** | 0 | **{eur(sae)}** | 0 | **{eur(scp)}** |')
    o.append(f'| **SOLDE** | **−{eur(sae)}** | | **−{eur(scp)}** | |\n')
    o.append('La présente mesure concourt à la réduction des prélèvements pesant sur les '
             'revenus d’activité.\n')
    o.append('EXPOSÉ SOMMAIRE\n')
    nat = ', '.join(dict.fromkeys(CAT_NOM.get(c, f'catégorie {c}') for c in cats))
    plu = 's' if len(lignes) > 1 else ''
    o.append(f'Cet amendement retire de la mission «{NB}{mission}{NB}» les crédits des '
             f'dispositifs que la présente loi interrompt. Il porte sur {len(lignes)} '
             f'programme{plu} et sur les crédits de {nat}.\n')
    tot_ouvert = sum(eb[norm(l[0])][0] for l in lignes)
    o.append(f'Les programmes visés reçoivent {eur(tot_ouvert)} euros d’autorisations '
             f'd’engagement dans le texte déposé (état B)¹. L’amendement en retire '
             f'{eur(sae)} euros en autorisations d’engagement et {eur(scp)} euros en '
             f'crédits de paiement. L’écart entre les deux règle les engagements déjà '
             f'contractés, que la mesure ne remet pas en cause.\n')
    if dates == ['1er juil.']:
        o.append('La mesure prend effet au 1er juillet 2027 : elle atteint des personnes '
                 'physiques, et la moitié de l’exercice leur est laissée.\n')
    elif dates == ['1er janv.']:
        o.append('La mesure prend effet au 1er janvier 2027 : elle n’atteint que des '
                 'personnes morales, et l’exercice est plein.\n')
    else:
        o.append('La mesure prend effet au 1er janvier 2027 pour les personnes morales et '
                 'au 1er juillet 2027 pour les personnes physiques.\n')
    o.append('Dit simplement : le Parlement cesse d’autoriser une dépense dont il ne '
             'vote ni le barème, ni les bénéficiaires.\n')
    o.append(f'¹ Projet de loi de finances pour 2027, n° 3210, état B annexé à '
             f'l’article 58, mission «{NB}{mission}{NB}».\n')
    return '\n'.join(o), sae, scp

def main(X, sortie):
    eb, t2, par = charger(X)
    blocs, tae, tcp, n = [], 0, 0, 0
    for mis in sorted(par, key=lambda k: -sum(v[0] for v in par[k].values())):
        lignes = []
        for p, (ae, cp, cats, dates) in sorted(par[mis].items(), key=lambda x: -x[1][0]):
            o = eb[norm(p)]
            aep = min(ae, o[0]); cpp = min(cp, o[1], aep)
            if aep < 1: continue
            t2m = aep if cats <= {21, 22, 23} else 0
            lignes.append((p, aep, cpp, cats, dates, t2m))
        if not lignes: continue
        n += 1
        b, sae, scp = piece(n, mis, lignes, eb, t2)
        blocs.append(b); tae += sae; tcp += scp
    tete = [f'# Liasse PLF 2027 — seconde partie, crédits\n',
            f'**{n} amendements**, un par mission. Montants tirés de la chaîne du § 1 du '
            f'registre sur la table A, plafonnés à l’état B 2027.\n',
            f'**Total : {eur(tae)} euros d’autorisations d’engagement et '
            f'{eur(tcp)} euros de crédits de paiement.**\n', '---\n']
    open(sortie, 'w').write('\n'.join(tete) + '\n'.join(blocs))
    print(f'{n} amendements écrits · AE {eur(tae)} · CP {eur(tcp)} → {sortie}')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
