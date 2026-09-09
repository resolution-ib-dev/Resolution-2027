# -*- coding: utf-8 -*-
"""Contrôle de `REF_norme` — huit codes, et un seul est aveugle au fond.

Un vecteur relevé par recherche ne se prouve pas en le recherchant une seconde
fois : on retrouverait la même erreur. **Le contrôle est donc structurel** — il
vérifie ce qui se vérifie sans réseau, et il déclare ce qu'il ne peut pas voir.

    N1  rattachement et vecteur ne se confondent pas          échec
    N2  la référence d'article a une forme reconnue           échec
    N3  un relevé Légifrance porte son identifiant et sa date échec
    N4  les vecteurs dérivés de l'annexe s'y retrouvent       échec
    N5  l'état déclaré concorde avec ce que l'entrée porte    échec
    N6  deux mesures ne visent pas le même article            signalement
    N7  un vecteur réglementaire n'est pas amendable          signalement
    N8  la couverture par population se dit                   compte

**N4 est le seul contrôle total.** Il rejoue la dérivation depuis le socle et
compare à l'octet : si l'annexe change au millésime suivant, les vecteurs
dérivés changent avec elle et l'écart sort. Les autres sont des contrôles de
forme et de cohérence — ils attrapent une faute de saisie, pas une erreur de
droit.

**Ce que le contrôle ne peut pas voir, et qui se dit** : si l'article existe
encore, s'il a été recodifié, s'il porte bien ce qu'on croit. Cela se vérifie
sur pièce, et la date du relevé est là pour dire quand cela a été fait.

Usage : python3 controle_norme.py ../referentiels/REF_norme.json \\
            ../referentiels/socle_budgetaire.json
"""
import collections
import json
import re
import sys

import ref_norme
import vecteurs

# Une référence d'article français : une lettre de partie facultative, un
# numéro, des subdivisions en chiffres romains, lettres, bis/ter/quater, et des
# fourchettes. Volontairement large : le but est d'attraper une saisie qui n'a
# pas la forme d'un article, pas de valider le droit.
FORME_ARTICLE = re.compile(
    r'^\*?(?:[LRDA]\.?\s*)?'
    r'\d+(?:[-–]\d+)*'
    r'(?:\s*(?:' + '|'.join(vecteurs.ORDINAUX) + r'|[A-H]|O|'
    r'[IVX]+|°|-|\d+|[a-z]\b|\.)\s*)*$',
    re.I)

FORME_IDENTIFIANT = re.compile(r'^(?:LEGIARTI|LEGISCTA|LEGITEXT|JORFTEXT)\d{12}$')

# Un vecteur dont le rôle est codifié doit nommer un texte de droit, pas un
# véhicule. C'est le contrôle qui refuse de confondre les deux colonnes.
VEHICULES = ('loi de finances', 'projet de loi de finances', 'plf', 'plfss',
             'loi de financement de la sécurité sociale')
ROLES_CODIFIES = ('creation', 'financement', 'competence', 'derogation')


def n1_confusion(entrees):
    ech = []
    for e in entrees:
        for v in e['vecteurs']:
            t = (v.get('texte') or '').lower()
            if v['role'] in ROLES_CODIFIES and any(w in t for w in VEHICULES):
                ech.append((e['population'], e['cle'], v['role'],
                            v.get('texte')))
    return ech


def n2_forme(entrees):
    """Le numéro d'article a-t-il une forme reconnue ?

    Depuis que l'adresse est décomposée, le contrôle porte sur le champ
    `article` seul — la subdivision est du texte libre par nature et ne se
    contraint pas.
    """
    ech = []
    for e in entrees:
        for v in e['vecteurs']:
            if v['role'] == 'montant':
                continue
            a = v.get('article')
            if a is None:
                # Vecteur écrit à la main : l'adresse est encore d'un bloc.
                arts = (v.get('articles') or '').split('—')[0]
                if not arts.strip() or arts.strip() == 'texte entier':
                    continue
                for art, _ in ref_norme.decouper_articles(arts):
                    art = art.split(' à ')[0].strip()
                    if art and not FORME_ARTICLE.match(art):
                        ech.append((e['population'], e['cle'], art))
                continue
            if ref_norme.TEXTE_NOMME.match(a) or a.startswith('BOI'):
                continue
            if not FORME_ARTICLE.match(a.split(' à ')[0].strip()):
                ech.append((e['population'], e['cle'], a))
    return ech


def n9_code(entrees):
    """Le code est-il déterminé, et par quelle règle ?

    **Aucun code ne s'affirme.** La première version posait « code général des
    impôts » sur les 465 dépenses fiscales : c'était un faux sur 55 d'entre
    elles — accises et taxes sur les véhicules vivent au code des impositions
    sur les biens et services. Le code se déduit désormais par une règle
    écrite, datée, et déclarée sur chaque vecteur ; ce qu'aucune règle ne
    couvre sort en `indéterminé` et se compte ici.
    """
    ind, sans_regle = [], []
    for e in entrees:
        for v in e['vecteurs']:
            if v['role'] == 'montant' or 'article' not in v:
                continue
            if v.get('texte') == vecteurs.CODE_INDETERMINE:
                ind.append((e['population'], e['cle'], v.get('articles')))
            elif not v.get('regle_code'):
                sans_regle.append((e['population'], e['cle'], v.get('texte')))
    return ind, sans_regle


def n3_identifiant(entrees):
    ech = []
    for e in entrees:
        for v in e['vecteurs']:
            if v['provenance'] != 'legifrance':
                continue
            ident = v.get('identifiant')
            if not ident or not FORME_IDENTIFIANT.match(ident):
                ech.append((e['population'], e['cle'], ident, 'identifiant'))
            elif not e.get('releve_le'):
                ech.append((e['population'], e['cle'], ident, 'date de relevé'))
    return ech


def n4_annexe(entrees, socle):
    """Rejoue la dérivation et compare. Contrôle total."""
    rejoue = {x['cle']: x for x in ref_norme.des_depenses_fiscales(socle)}
    ech = []
    for e in entrees:
        if e['population'] != 'depense_fiscale':
            continue
        r = rejoue.get(e['cle'])
        if r is None:
            ech.append((e['cle'], 'absente de la dérivation rejouée'))
            continue
        a = [(v['role'], v['texte'], v['articles']) for v in e['vecteurs']]
        b = [(v['role'], v['texte'], v['articles']) for v in r['vecteurs']]
        if a != b:
            ech.append((e['cle'], 'vecteur dérivé divergent'))
    return ech, len(rejoue)


def n5_etat(entrees):
    ech = []
    for e in entrees:
        if e['etat_vecteur'] not in ref_norme.ETATS:
            ech.append((e['population'], e['cle'], f"état inconnu "
                                                   f"« {e['etat_vecteur']} »"))
        elif bool(e['vecteurs']) != (e['etat_vecteur'] == 'trouve'):
            ech.append((e['population'], e['cle'],
                        f"état « {e['etat_vecteur']} » avec "
                        f"{len(e['vecteurs'])} vecteur(s)"))
        for v in e['vecteurs']:
            if v['provenance'] not in vecteurs.PROVENANCES:
                ech.append((e['population'], e['cle'],
                            f"provenance inconnue « {v['provenance']} »"))
            if v['role'] not in vecteurs.ROLES:
                ech.append((e['population'], e['cle'],
                            f"rôle inconnu « {v['role']} »"))
    return ech


def n6_collision(entrees):
    """Deux mesures visent-elles la même adresse ?

    La collision se juge sur **l'adresse complète** — code et article. Deux
    dépenses fiscales qui dérogent au même article, chacune par une subdivision
    différente, ne se neutralisent pas ; deux qui visent l'article entier, si.
    La subdivision est donc portée au détail et non à la clé.
    """
    par_adresse = collections.defaultdict(list)
    for e in entrees:
        for v in e['vecteurs']:
            if v['role'] == 'montant':
                continue
            art = v.get('article')
            if art is None:
                for a, _ in ref_norme.decouper_articles(
                        (v.get('articles') or '').split('—')[0]):
                    if a and a != 'texte entier':
                        par_adresse[(v.get('texte'), a)].append(
                            (e['population'], e['cle'], None))
            elif art and art != 'texte entier':
                par_adresse[(v.get('texte'), art)].append(
                    (e['population'], e['cle'], v.get('subdivision')))
    out = []
    for k, lot in par_adresse.items():
        cles = {(p, c) for p, c, _ in lot}
        if len(cles) > 1:
            entier = {(p, c) for p, c, sub in lot if not sub}
            out.append((k, sorted(cles), len(entier)))
    return out


def n7_reglementaire(entrees):
    sig = []
    for e in entrees:
        codif = [v for v in e['vecteurs'] if v['role'] in ROLES_CODIFIES]
        if codif and all(v.get('strate') == 'reglementaire' for v in codif):
            sig.append((e['population'], e['cle']))
    return sig


def main(src_norme, src_socle):
    r = json.load(open(src_norme, encoding='utf-8'))
    socle = json.load(open(src_socle, encoding='utf-8'))
    entrees = r['entrees']
    echecs = 0

    print('--- REF_norme : rattachement, vecteur, provenance ---\n')

    e1 = n1_confusion(entrees)
    print(f'N1 — {len(e1)} confusion(s) rattachement / vecteur')
    for x in e1[:10]:
        print(f'    {x}')
    echecs += len(e1)

    e2 = n2_forme(entrees)
    print(f'N2 — {len(e2)} référence(s) d\'article de forme non reconnue')
    for pop, cle, a in e2[:10]:
        print(f'    {pop} {cle} : « {a} »')
    echecs += len(e2)

    e3 = n3_identifiant(entrees)
    print(f'N3 — {len(e3)} relevé(s) Légifrance sans identifiant ou sans date')
    for x in e3[:10]:
        print(f'    {x}')
    echecs += len(e3)

    e4, n = n4_annexe(entrees, socle)
    print(f'N4 — {len(e4)} divergence(s) sur {n} dérivation(s) rejouée(s) '
          'depuis l\'annexe')
    for x in e4[:10]:
        print(f'    {x}')
    echecs += len(e4)

    e5 = n5_etat(entrees)
    print(f'N5 — {len(e5)} incohérence(s) d\'état, de provenance ou de rôle')
    for x in e5[:10]:
        print(f'    {x}')
    echecs += len(e5)

    e6 = n6_collision(entrees)
    durs = [x for x in e6 if x[2] > 1]
    print(f'N6 — {len(e6)} adresse(s) visée(s) par plus d\'une mesure, '
          f'dont {len(durs)} visée(s) en entier par plusieurs [signalement]')
    for (texte, art), qui, entier in sorted(e6, key=lambda x: -x[2])[:8]:
        print(f'    {texte} art. {art} — {len(qui)} mesure(s), '
              f'{entier} sur l\'article entier')

    e7 = n7_reglementaire(entrees)
    print(f'N7 — {len(e7)} mesure(s) dont le seul vecteur est réglementaire, '
          'donc hors de portée d\'un amendement [signalement]')
    for x in e7[:10]:
        print(f'    {x}')

    ind, sans_regle = n9_code(entrees)
    print(f'N9 — {len(ind)} adresse(s) de code indéterminé, '
          f'{len(sans_regle)} sans règle de déduction déclarée')
    for x in ind[:8]:
        print(f'    {x}')
    for x in sans_regle[:5]:
        print(f'    SANS RÈGLE {x}')
    echecs += len(sans_regle)

    print('\nN8 — couverture par population')
    ppe = r['comptes']['par_population_et_etat']
    for pop, e in sorted(ppe.items()):
        tot = sum(e.values())
        tr = e.get('trouve', 0)
        print(f'    {pop:16} {tot:5} — trouvé {tr:5} ({100 * tr // tot:3} %) '
              f'· à trouver {tot - tr}')
    a_trouver = sum(sum(e.values()) - e.get('trouve', 0) for e in ppe.values())
    print(f'    {"TOTAL":16} {len(entrees):5} — à trouver {a_trouver}')

    print(f'\n{echecs} échec(s), {len(e6)} collision(s), '
          f'{len(e7)} vecteur(s) réglementaire(s)')
    return 1 if echecs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
