#!/usr/bin/env python3
"""Régénère les amendements « Retirer les crédits » de la liasse P2.

Réécrit le 20261116. Une mission, un amendement ; les numéros sont ceux de la
liasse en place. Les montants viennent de `chaine_credits.py`, qui lit
`referentiels/parametres_credits_20261116.tsv` : rien n'est écrit à la main,
aucun paramètre ne vit ici. L'exposé se construit des seuls faits de la table :
crédits ouverts au texte déposé, natures de crédits touchées, date d'effet de
chaque ligne.

Le générateur remplace, dans la liasse, les seuls blocs des amendements de
mission et leurs lignes de sommaire. Les autres amendements ne sont pas lus.

Usage : python3 appareil/generer_liasse_p2.py [liasse.md] [--a-blanc]
"""
import re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chaine_credits import RACINE, lire_table, missions, montant

LIASSE = RACINE / 'livrables/depot_2027/LIASSE_PLF_P2.md'
NB = ' '
OBJET_TITRE = 'Retirer les crédits que la présente loi interrompt'


def eur(n):
    return f'{int(round(n)):,}'.replace(',', NB)


def rond(n):
    """Règle du 20261019 : entier au-dessus de 10, une décimale en dessous,
    dans l'unité qui convient."""
    def f(x):
        return f'{x:.0f}' if x >= 9.95 else f'{x:.1f}'.replace('.', ',')
    if n >= 999_500_000:
        return f'{f(n / 1e9)}{NB}milliard{"s" if n / 1e9 >= 1.95 else ""} d’euros'
    if n >= 999_500:
        return f'{f(n / 1e6)}{NB}million{"s" if n / 1e6 >= 1.95 else ""} d’euros'
    return f'{eur(round(n, -3))}{NB}euros'


CAT_NOM = {21: 'rémunérations', 22: 'cotisations sociales', 23: 'avantages salariaux',
           31: 'fonctionnement courant', 32: 'subventions pour charges de service public',
           51: 'investissement de l’État', 52: 'investissement de l’État',
           53: 'investissement de l’État', 61: 'transferts aux ménages',
           62: 'transferts aux entreprises', 63: 'transferts aux collectivités',
           64: 'transferts aux autres collectivités'}
DATE_LONGUE = {'1er janv.': '1er janvier 2027', '1er avril': '1er avril 2027', '1er juil.': '1er juillet 2027'}


def enumerer(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ', '.join(xs[:-1]) + ' et ' + xs[-1]


def piece(n, mission, progs, table):
    sae = sum(p['ae'] for _, p in progs)
    scp = sum(p['cp'] for _, p in progs)
    lignes = [d for _, p in progs for d in p['lignes'] if montant(d)[0] >= 0.5]
    o = [f'## Amendement n° {n} [{OBJET_TITRE}, mission «{NB}{mission}{NB}»]\n',
         'AMENDEMENT\n', 'présenté par\n', '----------\n', 'ARTICLE 58\n',
         f'Modifier ainsi les crédits de la mission «{NB}{mission}{NB}» :\n',
         '| Programmes | AE + | AE − | CP + | CP − |', '|---|---:|---:|---:|---:|']
    for lib, p in progs:
        o.append(f'| {lib} | 0 | {eur(p["ae"])} | 0 | {eur(p["cp"])} |')
        if p['t2'] >= 1:
            o.append(f'| *dont titre 2* | 0 | {eur(p["t2"])} | 0 | {eur(p["t2"])} |')
    o.append(f'| **TOTAUX** | 0 | **{eur(sae)}** | 0 | **{eur(scp)}** |')
    o.append(f'| **SOLDE** | **−{eur(sae)}** | | **−{eur(scp)}** | |\n')
    o.append('La présente mesure concourt à la réduction des prélèvements pesant sur les '
             'revenus d’activité.\n')
    o.append('EXPOSÉ SOMMAIRE\n')
    cats = sorted({int(d['categorie']) for d in lignes})
    nat = ', '.join(dict.fromkeys(CAT_NOM.get(c, f'catégorie {c}') for c in cats))
    plu = 's' if len(progs) > 1 else ''
    p1 = (f'Cet amendement retire de la mission «{NB}{mission}{NB}» les crédits des '
          f'dispositifs que la présente loi interrompt. Il porte sur {len(progs)} '
          f'programme{plu} et sur les crédits de {nat}.')
    if any('entretien des routes' in d['motif_hors_liasse'] for d in table
           if d['etatB_2027_mission'] == mission):
        p1 += ' Les crédits d’entretien du réseau routier national sont maintenus.'
    o.append(p1 + '\n')
    ouvert = sum(p['ouvert_ae'] for _, p in progs)
    p2 = (f'Les programmes visés reçoivent {eur(ouvert)} euros d’autorisations '
          f'd’engagement dans le texte déposé (état B)¹. L’amendement en retire '
          f'{rond(sae)} en autorisations d’engagement et {rond(scp)} en crédits de paiement.')
    if scp < sae:
        p2 += (' L’écart entre les deux règle les engagements déjà contractés, que la '
               'mesure ne remet pas en cause.')
    if any(float(d['regle_rythme']) < 0.99 for d in lignes):
        p2 += (' Un dispositif qui s’éteint en trois ans est retiré pour sa première année.')
    o.append(p2 + '\n')
    par_date = {}
    for d in lignes:
        par_date.setdefault(d['regle_date'], []).append(d['objet_expose'])
    ordre = [k for k in DATE_LONGUE if k in par_date]
    # La règle de date et sa raison (registre de calcul, § 1, R-P et R-S, § 7) : une
    # coupe qui atteint des personnes physiques tombe le mois où le salaire net monte.
    JUILLET = ('le mois où commence la baisse des prélèvements pesant sur les revenus '
               'd’activité')
    if len(ordre) == 1 and 'juil' in ordre[0]:
        o.append(f'La mesure prend effet au {DATE_LONGUE[ordre[0]]}, {JUILLET}{NB}: '
                 'elle atteint des personnes physiques.\n')
    elif len(ordre) == 1:
        o.append(f'La mesure prend effet au {DATE_LONGUE[ordre[0]]}{NB}: elle n’atteint '
                 'que des personnes morales.\n')
    else:
        ph = ['Une dépense versée à des personnes physiques, ou à des organismes dont elle '
              f'paie les salariés, s’arrête au 1er juillet 2027, {JUILLET}. Une dépense '
              'versée à des entreprises ou à des collectivités s’arrête au 1er janvier 2027.']
        for i, k in enumerate(ordre):
            sujet = 'La mesure' if i == 0 else 'Elle'
            ph.append(f'{sujet} prend effet au {DATE_LONGUE[k]} pour '
                      f'{enumerer(dict.fromkeys(par_date[k]))}.')
        o.append(' '.join(ph) + '\n')
    if any(d['ligne_registre'] == 'D20' for d in lignes):
        o.append('Le chèque énergie s’éteint au 1er janvier 2027{NB}: aucun titre n’est émis '
                 'au titre de 2027. L’exercice règle encore les titres de la campagne '
                 'précédente, et la moitié des crédits est retirée.\n'.replace('{NB}', NB))
    o.append(f'Dit simplement{NB}: le Parlement cesse d’autoriser une dépense dont il ne '
             'vote ni le barème ni les bénéficiaires.\n')
    o.append(f'¹ Projet de loi de finances pour 2027, n° 3210, état B annexé à '
             f'l’article 58, mission «{NB}{mission}{NB}».\n')
    return '\n'.join(o).replace("'", '’'), sae, scp


def main(argv):
    chemin = Path(next((a for a in argv if not a.startswith('--')), LIASSE))
    texte = chemin.read_text(encoding='utf-8')
    table = lire_table()
    ms = missions(table)
    tae = tcp = 0
    for n, (mission, progs) in ms.items():
        bloc, sae, scp = piece(n, mission, progs, table)
        tae += sae
        tcp += scp
        m = re.search(rf'^## Amendement n° {n} \[{OBJET_TITRE}, mission «.*?»\]\n', texte, re.M)
        if not m:
            sys.exit(f'amendement n° {n} introuvable dans {chemin.name}')
        fin = re.compile(r'^---\n+(?:---\n+)?## Amendement n° ', re.M).search(texte, m.end())
        texte = texte[:m.start()] + bloc + '\n' + texte[fin.start():]
        texte, k = re.subn(rf'^\| {n} \| ARTICLE 58, état B \| .* \|$',
                           f'| {n} | ARTICLE 58, état B | {OBJET_TITRE}, mission «{NB}{mission}{NB}» |',
                           texte, flags=re.M)
        if k != 1:
            sys.exit(f'ligne de sommaire du n° {n} : {k} occurrence(s)')
        print(f'n° {n:>2}  AE {eur(sae):>15}  CP {eur(scp):>15}  {mission}')
    print(f'{len(ms)} amendements · AE {eur(tae)} · CP {eur(tcp)}')
    if '--a-blanc' not in argv:
        chemin.write_text(texte, encoding='utf-8')
        print(f'→ {chemin}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
