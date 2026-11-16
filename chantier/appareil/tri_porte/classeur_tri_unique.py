#!/usr/bin/env python3
"""Le classeur publiable du tri unique : livrables/tri_prelevements/Tri des impôts.xlsx.

Lit referentiels/sort_prelevements_20261116.tsv et
livrables/tri_prelevements/passage_tableau_20261116.tsv (écrits par tri_unique.py).
Cinq onglets : Lisez-moi, Le tri, Par devenir, Par poste du tableau, Passage.
Montants en M€ entiers. Le classeur se relit après écriture : aucune mention
interne, aucun identifiant, aucun montant décimal, six devenirs exactement,
434 lignes, totaux rebouclés. Code retour 1 sur un seul écart.
"""
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

RACINE = Path(__file__).resolve().parent.parent.parent
TRI = RACINE / 'referentiels/sort_prelevements_20261116.tsv'
PASSAGE = RACINE / 'livrables/tri_prelevements/passage_tableau_20261116.tsv'
SORTIE = RACINE / 'livrables/tri_prelevements/Tri des impôts.xlsx'

DEVENIRS = ['grand impôt conservé', 'remplacé par un grand impôt', 'fondu dans l’équilibre des quatre grands impôts',
            'conservé en complément', 'à fusionner', 'recette non fiscale']
DEF = {
    'grand impôt conservé': 'Impôt sur le revenu, impôt sur les sociétés, TVA, taxe foncière.',
    'remplacé par un grand impôt': 'Le prélèvement disparaît. Un des quatre grands impôts, nommé à la colonne « Impôt de remplacement », en reprend le produit.',
    'fondu dans l’équilibre des quatre grands impôts': 'Le prélèvement disparaît. Son produit est repris par les hausses d’équilibre de la refonte : taxes sur la main-d’œuvre, remontées mécaniques, ski de fond.',
    'conservé en complément': 'Le prélèvement demeure à côté du grand impôt qu’il prolonge. Six blocs : accises sur les carburants, le gaz, le tabac et l’alcool ; taxes des activités sans TVA (assurances, forfait social, contribution de solidarité pour l’autonomie) ; taxe de séjour unique ; fonds de garantie ; fiscalité outre-mer ; Union européenne.',
    'à fusionner': 'Les cotisations sociales. Leur fusion est présentée séparément.',
    'recette non fiscale': 'Redevance, amende, somme acquise à l’État ou contribution versée à un organisme privé : la ligne figure dans les recensements, elle n’est pas un impôt.',
}
POSTE = {
    'TVA': 'TVA', 'Taxes sur la consommation*': 'Taxes sur la consommation (total)',
    'dont énergie*': 'Consommation : énergie', 'dont alcool, tabac, jeux': 'Consommation : alcool, tabac, jeux',
    'dont assurances': 'Consommation : assurances', "dont redevances sur l'eau": 'Consommation : redevances sur l’eau',
    'dont services de transports': 'Consommation : services de transports', 'dont véhicules': 'Consommation : véhicules',
    'dont numérique, spectacles': 'Consommation : numérique, spectacles',
    'dont autres taxes sur les produits': 'Consommation : autres taxes sur les produits',
    'dont taxe de séjour': 'Consommation : taxe de séjour', 'dont taxe pollution': 'Consommation : taxe pollution',
    'dont outre-mer': 'Consommation : outre-mer', "Taxes sur la main d'œuvre": 'Taxes sur la main-d’œuvre',
    'dont forfaits de cotisation': 'Taxes sur la main-d’œuvre : forfaits de cotisation',
    'IR net': 'Impôt sur le revenu', 'IS net': 'Impôt sur les sociétés',
    "Taxes sur chiffre d'affaires et bénéfices": 'Taxes sur le chiffre d’affaires et les bénéfices',
    'Taxe foncière': 'Taxe foncière', 'Autres taxes sur les ménages': 'Autres taxes sur les ménages',
    'Autres taxes sur les entreprises': 'Autres taxes sur les entreprises',
    'Droits de mutation': 'Droits de mutation (ligne générale)', 'à titre onéreux': 'Droits de mutation à titre onéreux',
    'à titre gratuit': 'Droits de mutation à titre gratuit', '—': 'Hors tableau',
}
INTERDIT = re.compile(r'\b(?:A|M|D)-\d+\b|\d{8}|à confirmer|à vérifier|probable|n\.d\.|\.tsv|\.md|\.xlsx|\.py|tri du|IFRAP|'
                      r'\bauteure?\b|pilotage|\bfil\b|\bregistre\b|\brangs?\b|nœud|référentiel|manuscrit|schéma|\bN\d{1,2}\b', re.I)
SOURCE = re.compile(r'\b(?:A|M|D)-\d+\b|\d{8}|\.tsv|\.md|\.xlsx|\.py|tri du|IFRAP', re.I)   # pour un libellé repris de sa source
SIEGE_SALE = re.compile(r'\d{8}|à confirmer|à vérifier|probable|n\.d\.|relevé par|tri du|IFRAP', re.I)
GRAS = Font(bold=True)
HAUT = Alignment(wrap_text=True, vertical='top')
GRIS = PatternFill('solid', fgColor='DDDDDD')
NB = '# ##0'


def f(x):
    return float(x) if x not in ('', None) else 0.0


def m(x):
    """Montant en M€ entier ; une case vide reste vide."""
    if x in ('', None):
        return None
    x = float(x)
    return int(x + 0.5) if x >= 0 else -int(-x + 0.5)


def esp(n):
    return f'{n:,}'.replace(',', '\u00a0')


def som(rs):
    """Somme des rendements publiés ; vide si aucun ne l'est."""
    rs = [r for r in rs if r['rendement_2026_M'] != '']
    return m(sum(f(r['rendement_2026_M']) for r in rs)) if rs else None


def lire(p):
    with open(p, encoding='utf-8') as fh:
        return list(csv.DictReader(fh, delimiter='\t'))


def feuille(wb, titre, cols, lignes, larg, filtre=True):
    ws = wb.create_sheet(titre)
    ws.append(cols)
    for c in ws[1]:
        c.font, c.fill, c.alignment = GRAS, GRIS, HAUT
    for l in lignes:
        ws.append(l)
    for i, c in enumerate(cols, 1):
        ws.column_dimensions[get_column_letter(i)].width = larg.get(c, 16)
    for row in ws.iter_rows(min_row=2):
        for c in row:
            if isinstance(c.value, int) and cols[c.column - 1] != 'N°':
                c.number_format = NB
            if isinstance(c.value, str) and len(c.value) > 40:
                c.alignment = HAUT
    ws.freeze_panes = 'A2'
    if filtre:
        ws.auto_filter.ref = ws.dimensions
    return ws


def construire():
    T = lire(TRI)
    P = lire(PASSAGE)
    n_tot = len(T)
    vides = [r for r in T if r['rendement_2026_M'] == '']
    chiffres = n_tot - len(vides)
    cot = sum(1 for r in vides if r['devenir'] == 'à fusionner')
    rev = sum(1 for r in T if 'révisée' in r['source_rendement'] and r['rendement_2026_M'] != '')
    par_dev = {d: [r for r in T if r['devenir'] == d] for d in DEVENIRS}
    tot_exact = sum(f(r['rendement_2026_M']) for r in T)

    wb = Workbook()
    ws = wb.active
    ws.title = 'Lisez-moi'
    L = [('Le tri des impôts', ''), ('', ''),
         ('Objet', f'{n_tot} prélèvements obligatoires recensés : impôts, taxes, contributions et cotisations. Chacun reçoit un devenir dans la réforme, parmi six.'),
         ('Montants', 'Millions d’euros, arrondis à l’unité. Prévision pour 2026 du budget 2026. Les totaux sont calculés sur les montants exacts, puis arrondis.'),
         ('', ''), ('Les six devenirs', 'Nombre de prélèvements, rendement 2026 en millions d’euros')]
    for d in DEVENIRS:
        rs = par_dev[d]
        L.append((d[0].upper() + d[1:], f'{len(rs)} prélèvements, {esp(m(sum(f(r["rendement_2026_M"]) for r in rs)))} M€. ' + DEF[d]))
    L += [('', ''),
          ('Prélèvements sans rendement publié',
           f'{len(vides)} prélèvements sur {n_tot} n’ont aucun rendement publié aux annexes du budget : leur case est vide, et les totaux portent sur les {chiffres} autres. '
           f'Il s’agit de {cot} cotisations sociales, de taxes affectées à des organismes et d’impôts locaux, dont la taxe foncière sur les propriétés bâties. '
           f'{rev} prélèvements, ajoutés d’après le budget 2027, portent sa prévision révisée pour 2026.'),
          ('', ''), ('Les onglets', ''),
          ('Le tri', 'Une ligne par prélèvement : nature, assiette, rendement, devenir, impôt de remplacement ou bloc, poste du tableau de la refonte, siège juridique et lien vers Légifrance.'),
          ('Par devenir', 'Nombre et rendement par devenir, par impôt de remplacement et par bloc.'),
          ('Par poste du tableau', 'Nombre et rendement par poste du tableau « Refonte fiscalité » et par devenir.'),
          ('Passage', 'Chaque poste du tableau « Refonte fiscalité » (montant 2024, taxes à supprimer) face aux prélèvements du tri qui s’y rattachent, avec la lecture de chaque écart.'),
          ('', ''), ('Lecture des colonnes', ''),
          ('Impôt de remplacement', 'Renseigné pour un prélèvement remplacé : impôt sur le revenu quand un particulier paie, impôt sur les sociétés quand une entreprise paie pour son activité, TVA pour une taxe sur la consommation, taxe foncière pour le patrimoine et l’action locale.'),
          ('Mention', '« Droit ramené à 1 % et 3 %, part gardée » : les droits de mutation sont ramenés à 1 % et 3 %, acompte de l’impôt sur le revenu ou sur les sociétés ; la part gardée figure en colonne. « Supprimé par voie réglementaire » : redevance supprimée par décret.'),
          ('Poste du tableau', 'Ligne du tableau « Refonte fiscalité » de la synthèse des chiffrages. « Hors tableau » : cotisations sociales, CSG, CRDS et autres prélèvements que ce tableau ne détaille pas.'),
          ('Tableau en 2024, tri en 2026', 'Le tableau « Refonte fiscalité » est en montants de 2024 des comptes nationaux ; le tri est en prévision 2026 du budget. Un écart de montant entre les deux tient d’abord à ces deux années et à ces deux sources.'),
          ('', ''),
          ('CSG et CRDS', 'Elles sont remplacées par l’impôt sur le revenu, dont le taux unique de 23 % se calcule sur une assiette qui intègre la leur.'),
          ('', ''),
          ('Sources', 'Projets de loi de finances pour 2026 et pour 2027, évaluation des voies et moyens ; code général des impôts, code des impositions sur les biens et services, code de la sécurité sociale et autres textes en vigueur ; comptes nationaux de l’Insee, tableau 3.217, pour le tableau « Refonte fiscalité ».')]
    for a, b in L:
        ws.append([a, b])
    ws['A1'].font = Font(bold=True, size=14)
    for row in ws.iter_rows():
        row[0].alignment = row[1].alignment = HAUT
        if row[0].value in ('Les six devenirs', 'Les onglets', 'Lecture des colonnes', 'Prélèvements sans rendement publié'):
            row[0].font = GRAS
    ws.column_dimensions['A'].width = 44
    ws.column_dimensions['B'].width = 120

    # ---- Le tri
    cols = ['N°', 'Prélèvement', 'Nature', 'Assiette', 'Rendement 2026 (M€)', 'Devenir', 'Impôt de remplacement', 'Bloc',
            'Mention', 'Dont part gardée (M€)', 'Poste du tableau', 'Siège', 'Lien Légifrance']
    lignes = []
    for k, r in enumerate(T, 1):
        sg = r['siege'].replace('—', '').strip()
        lignes.append([k, r['libelle'], r['nature'], r['assiette'] or None, m(r['rendement_2026_M']), r['devenir'],
                       r['impot_cible'] or None, r['bloc'] or None,
                       (r['mention'][0].upper() + r['mention'][1:]) if r['mention'] else None,
                       m(r['part_conservee_2026_M']), POSTE[r['poste_tableau']],
                       None if (not sg or SIEGE_SALE.search(sg)) else sg, r['lien_legifrance'] or None])
    ws = feuille(wb, 'Le tri', cols, lignes, {'N°': 6, 'Prélèvement': 60, 'Devenir': 34, 'Impôt de remplacement': 24, 'Bloc': 20,
                                              'Mention': 30, 'Poste du tableau': 36, 'Siège': 40, 'Lien Légifrance': 34,
                                              'Assiette': 26, 'Nature': 18})
    for row in ws.iter_rows(min_row=2, min_col=13, max_col=13):
        c = row[0]
        if c.value:
            c.hyperlink = c.value
            c.font = Font(color='0563C1', underline='single')

    # ---- Par devenir
    syn = defaultdict(lambda: [0, 0, 0.0, 0.0, []])
    for r in T:
        x = syn[(r['devenir'], r['impot_cible'] or r['bloc'] or '')]
        x[0] += 1
        x[1] += r['rendement_2026_M'] == ''
        x[2] += f(r['rendement_2026_M'])
        x[3] += f(r['part_conservee_2026_M'])
        x[4].append(r)
    lignes = []
    for d in DEVENIRS:
        rs = par_dev[d]
        lignes.append([d[0].upper() + d[1:], 'Ensemble', len(rs), sum(1 for r in rs if r['rendement_2026_M'] == ''),
                       m(sum(f(r['rendement_2026_M']) for r in rs)), m(sum(f(r['part_conservee_2026_M']) for r in rs)) or None])
        sous = sorted((k for k in syn if k[0] == d and k[1]), key=lambda k: -syn[k][2])
        for k in sous:
            v = syn[k]
            lignes.append([None, k[1], v[0], v[1], som(v[4]), m(v[3]) or None])
    lignes.append(['Total', None, n_tot, len(vides), m(tot_exact), m(sum(f(r['part_conservee_2026_M']) for r in T))])
    ws = feuille(wb, 'Par devenir', ['Devenir', 'Impôt de remplacement ou bloc', 'Prélèvements', 'Dont sans rendement publié',
                                     'Rendement 2026 (M€)', 'Dont part gardée (M€)'], lignes,
                 {'Devenir': 46, 'Impôt de remplacement ou bloc': 32}, filtre=False)
    for row in ws.iter_rows(min_row=2):
        if row[0].value:
            for c in row:
                c.font = GRAS

    # ---- Par poste du tableau
    ordre = list(POSTE)
    pp = defaultdict(lambda: [0, 0, 0.0, []])
    for r in T:
        x = pp[(r['poste_tableau'], r['devenir'])]
        x[0] += 1
        x[1] += r['rendement_2026_M'] == ''
        x[2] += f(r['rendement_2026_M'])
        x[3].append(r)
    lignes = []
    for p in ordre:
        ks = [(p, d) for d in DEVENIRS if (p, d) in pp]
        if not ks:
            continue
        lignes.append([POSTE[p], 'Ensemble', sum(pp[k][0] for k in ks), sum(pp[k][1] for k in ks), m(sum(pp[k][2] for k in ks))])
        for k in ks:
            lignes.append([None, k[1][0].upper() + k[1][1:], pp[k][0], pp[k][1], som(pp[k][3])])
    lignes.append(['Total', None, n_tot, len(vides), m(tot_exact)])
    ws = feuille(wb, 'Par poste du tableau', ['Poste du tableau', 'Devenir', 'Prélèvements', 'Dont sans rendement publié',
                                              'Rendement 2026 (M€)'], lignes, {'Poste du tableau': 46, 'Devenir': 46}, filtre=False)
    for row in ws.iter_rows(min_row=2):
        if row[0].value:
            for c in row:
                c.font = GRAS

    # ---- Passage
    cols = ['Poste du tableau', 'Montant 2024 au tableau (M€)', 'Taxes à supprimer au tableau (M€)', 'Prélèvements du tri',
            'Dont sans rendement publié', 'Rendement 2026 au tri (M€)', 'Dont supprimé au tri (M€)', 'Dont gardé au tri (M€)',
            'Écart de montant, tri moins tableau (M€)', 'Écart sur le supprimé, tri moins tableau (M€)', 'Lecture']
    lignes = []
    for r in P:
        p = r['poste']
        nom = POSTE[p] if p in POSTE else 'Hors tableau : ' + p.split(' — ')[1]
        iv = lambda k: int(r[k]) if r[k] != '' else None
        lignes.append([nom, m(r['montant_2024_M']), m(r['a_supprimer_2024_M']), iv('rangs'), iv('sans_rendement'),
                       m(r['rendement_2026_M']), m(r['supprime_2026_M']), m(r['garde_2026_M']), m(r['ecart_montant_M']),
                       m(r['ecart_supprime_M']), r['lecture']])
    feuille(wb, 'Passage', cols, lignes, {'Poste du tableau': 46, 'Lecture': 110}, filtre=False)
    wb.save(SORTIE)
    return T, n_tot, len(vides), m(tot_exact)


def relire(T, n_tot, n_vides, total):
    ko = []
    wb = load_workbook(SORTIE)
    if wb.sheetnames != ['Lisez-moi', 'Le tri', 'Par devenir', 'Par poste du tableau', 'Passage']:
        ko.append(f'onglets : {wb.sheetnames}')
    for ws in wb.worksheets:
        for row in ws.iter_rows(values_only=True):
            for j, v in enumerate(row):
                motif = SOURCE if (ws.title == 'Le tri' and j in (1, 11)) else INTERDIT
                if isinstance(v, str) and not v.startswith('https://') and motif.search(v):
                    ko.append(f'{ws.title} : mention interne « {motif.search(v).group()} » dans « {v[:60]} »')
                if isinstance(v, float):
                    ko.append(f'{ws.title} : montant décimal {v}')
    tri = list(wb['Le tri'].iter_rows(min_row=2, values_only=True))
    if len(tri) != n_tot:
        ko.append(f'Le tri : {len(tri)} lignes')
    if set(l[5] for l in tri) != set(DEVENIRS):
        ko.append('Le tri : les devenirs ne sont pas les six')
    if sum(1 for l in tri if l[4] is None) != n_vides:
        ko.append('Le tri : compte des cases vides')
    for nom in ('Par devenir', 'Par poste du tableau'):
        ll = list(wb[nom].iter_rows(min_row=2, values_only=True))
        ens = [l for l in ll if l[1] == 'Ensemble']
        tot = ll[-1]
        if sum(l[2] for l in ens) != tot[2] or sum(l[3] for l in ens) != tot[3]:
            ko.append(f'{nom} : les comptes ne rebouclent pas')
        if abs(sum(l[4] for l in ens) - tot[4]) > len(ens) / 2:
            ko.append(f'{nom} : les montants ne rebouclent pas ({sum(l[4] for l in ens)} contre {tot[4]})')
        print(f'  {nom} : {len(ens)} ensembles, {tot[2]} prélèvements, somme des ensembles {sum(l[4] for l in ens)}, total {tot[4]}')
    print(f'  Le tri : {len(tri)} lignes, {n_vides} sans rendement, somme des cases {sum(l[4] or 0 for l in tri)}, total exact arrondi {total}')
    return ko


def main():
    T, n_tot, n_vides, total = construire()
    ko = relire(T, n_tot, n_vides, total)
    if ko:
        print(f'\nÉCHEC — {len(ko)} écart(s) :')
        for k in ko[:30]:
            print('  ', k)
        return 1
    print('  0 écart : aucune mention interne, aucun montant décimal, six devenirs, totaux rebouclés.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
