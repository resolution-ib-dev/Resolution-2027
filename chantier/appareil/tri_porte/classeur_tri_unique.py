#!/usr/bin/env python3
"""Le classeur publiable du tri unique : livrables/tri_prelevements/Tri des impôts.xlsx.

Lit referentiels/sort_prelevements_20261116.tsv et
livrables/tri_prelevements/passage_tableau_20261116.tsv (écrits par tri_unique.py).
Six onglets : Avant, après (par grand impôt, puis comptes nationaux → tableau de la refonte → tri ; dans l'ordre du graphique « 434 prélèvements aujourd'hui,
4 grands impôts demain »), Le tri (une ligne par prélèvement, dans l'ordre du graphique, cotisations à
fusionner isolées en bas), Par devenir, Par poste du tableau, Passage, Lisez-moi. Montants en M€ entiers,
indicatifs : en gris, en dernière colonne, car 186 prélèvements n'ont pas de rendement publié (règle de
l'auteure, 20261123). Le classeur se relit après écriture : aucune mention
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
# Du brut Insee aux prélèvements du projet : tablette T4, relevée au tableau 3.217 de l'Insee (archivée le 20261020).
TABLETTES = RACINE / 'archive/tri_20261020/livrables/tablettes/Tablettes_prelevements.xlsx'

DEVENIRS = ['grand impôt conservé', 'remplacé par un grand impôt', 'fondu dans l’équilibre des quatre grands impôts',
            'conservé en complément', 'à fusionner', 'recette non fiscale']
# Libellé publié d'un devenir (auteure, 20261123 : « complément sectoriel harmonisé »).
NOM_DEV = {d: d for d in DEVENIRS}
NOM_DEV['conservé en complément'] = 'complément sectoriel harmonisé'
GRAPHIQUE = Path('/home/user/Site-ETNP/site/graphiques/fusion-des-impots.html')
COLONNES = ['Impôt sur le revenu', 'Impôt sur les sociétés', 'Taxe sur la valeur ajoutée', 'Taxe foncière', 'Cotisation unique']
NOM_COL = {'Taxe sur la valeur ajoutée': 'TVA'}
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
TETE = PatternFill('solid', fgColor='B23A10')
BLANC = Font(bold=True, color='FFFFFF')
SABLE = PatternFill('solid', fgColor='F7F3E8')
INDIC = Font(italic=True, color='8C8C8C')
UNE = Alignment(wrap_text=False, vertical='center')
from openpyxl.styles import Border, Side
FIL = Border(bottom=Side(style='thin', color='DDD7CD'))
NB = '# ##0'
MD = '# ##0.0'


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
            if isinstance(c.value, float):
                c.number_format = MD
            if isinstance(c.value, str) and len(c.value) > 40:
                c.alignment = HAUT
    ws.freeze_panes = 'A2'
    if filtre:
        ws.auto_filter.ref = ws.dimensions
    return ws


def colonne_du_graphique():
    """{libellé: rang de colonne 0..4} relevé sur le graphique publié (abscisse de chaque carré)."""
    s = GRAPHIQUE.read_text(encoding='utf-8')
    svg = s[s.index('<svg'):s.index('</svg>')]
    out = {}
    for lib, x in re.findall(r'<g class="tuile" data-lib="([^"]*)"[^>]*>.*?<rect x="([\d.]+)"', svg):
        import html as _h
        out[' '.join(_h.unescape(lib).split())] = min(4, int((float(x) - 120) // 288))
    return out


def rang_graphique(r, col_g):
    """Clé d'ordre : colonne du graphique, puis devenir, puis rendement décroissant ; les cotisations
    à fusionner en tout dernier (auteure, 20261123)."""
    d = r['devenir']
    if d == 'à fusionner':
        return (9, 0, -f(r['rendement_2026_M']))
    if d == 'recette non fiscale':
        return (8, 0, -f(r['rendement_2026_M']))
    c = col_g.get(' '.join(r['libelle'].split()))
    if c is None:
        c = COLONNES.index(r['impot_cible']) if r['impot_cible'] in COLONNES else (4 if d.startswith('fondu') else 2)
    return (c, DEVENIRS.index(d), -f(r['rendement_2026_M']))


def demain(r, col_g):
    d = r['devenir']
    if d == 'à fusionner':
        return 'Cotisation unique'
    if d == 'recette non fiscale':
        return 'Hors impôts'
    return NOM_COL.get(COLONNES[rang_graphique(r, col_g)[0]], COLONNES[rang_graphique(r, col_g)[0]])


def entete(ws, ligne, cols, indic=()):
    for j, c in enumerate(cols, 1):
        x = ws.cell(row=ligne, column=j, value=c)
        x.font, x.fill, x.alignment = BLANC, TETE, Alignment(wrap_text=True, vertical='center')
    ws.row_dimensions[ligne].height = 62
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True


def construire():
    T = lire(TRI)
    P = lire(PASSAGE)
    col_g = colonne_du_graphique()
    n_tot = len(T)
    vides = [r for r in T if r['rendement_2026_M'] == '']
    chiffres = n_tot - len(vides)
    par_dev = {d: [r for r in T if r['devenir'] == d] for d in DEVENIRS}
    tot_exact = sum(f(r['rendement_2026_M']) for r in T)
    ordre = sorted(T, key=lambda r: rang_graphique(r, col_g))
    wb = Workbook()
    vue_ensemble(wb.active, T, P, ordre, col_g, par_dev, vides, tot_exact)

    # ---- Le tri : une ligne par prélèvement, ordre du graphique, cotisations en bas
    ws = wb.create_sheet('Le tri')
    cols = ['N°', 'Prélèvement', 'Demain', 'Devenir', 'Nature', 'Assiette', 'Bloc', 'Mention', 'Siège', 'Lien Légifrance',
            'Rendement 2026, indicatif (M€)']
    entete(ws, 1, cols)
    lig, k, coupe = 2, 0, False
    for r in ordre:
        if r['devenir'] == 'à fusionner' and not coupe:
            lig += 1
            c = ws.cell(row=lig, column=1, value='Cotisations à fusionner en une cotisation unique')
            c.font = Font(bold=True, color='B23A10')
            lig += 1
            coupe = True
        k += 1
        sg = r['siege'].replace('—', '').strip()
        v = [k, r['libelle'], demain(r, col_g), NOM_DEV[r['devenir']][0].upper() + NOM_DEV[r['devenir']][1:], r['nature'],
             r['assiette'] or None, r['bloc'] or None, (r['mention'][0].upper() + r['mention'][1:]) if r['mention'] else None,
             None if (not sg or SIEGE_SALE.search(sg)) else sg, r['lien_legifrance'] or None, m(r['rendement_2026_M'])]
        for j, x in enumerate(v, 1):
            c = ws.cell(row=lig, column=j, value=x)
            c.alignment = UNE
            if j == 11:
                c.font, c.number_format = INDIC, NB
            if j == 10 and x:
                c.hyperlink, c.font = x, Font(color='0563C1', underline='single')
        lig += 1
    for j, w in enumerate([6, 70, 26, 34, 18, 22, 22, 30, 34, 30, 16], 1):
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.freeze_panes = 'C2'
    ws.auto_filter.ref = f'A1:K{lig - 1}'

    # ---- Par devenir
    syn = defaultdict(lambda: [0, 0, []])
    for r in T:
        x = syn[(r['devenir'], r['impot_cible'] or r['bloc'] or '')]
        x[0] += 1
        x[1] += r['rendement_2026_M'] == ''
        x[2].append(r)
    lignes = []
    for d in DEVENIRS:
        rs = par_dev[d]
        lignes.append([NOM_DEV[d][0].upper() + NOM_DEV[d][1:], 'Ensemble', len(rs), sum(1 for r in rs if r['rendement_2026_M'] == ''),
                       md(sum(f(r['rendement_2026_M']) for r in rs))])
        for kk in sorted((kk for kk in syn if kk[0] == d and kk[1]), key=lambda kk: -sum(f(r['rendement_2026_M']) for r in syn[kk][2])):
            v = syn[kk]
            lignes.append([None, kk[1], v[0], v[1], md(som(v[2]))])
    lignes.append(['Total', None, n_tot, len(vides), md(tot_exact)])
    ws = feuille(wb, 'Par devenir', ['Devenir', 'Impôt de remplacement ou bloc', 'Prélèvements', 'Dont sans rendement publié',
                                     'Rendement 2026, indicatif (Md€)'], lignes, {'Devenir': 46, 'Impôt de remplacement ou bloc': 32}, filtre=False)
    habiller(ws)

    # ---- Par poste du tableau
    pp = defaultdict(lambda: [0, 0, []])
    for r in T:
        x = pp[(r['poste_tableau'], r['devenir'])]
        x[0] += 1
        x[1] += r['rendement_2026_M'] == ''
        x[2].append(r)
    lignes = []
    for p in POSTE:
        ks = [(p, d) for d in DEVENIRS if (p, d) in pp]
        if not ks:
            continue
        lignes.append([POSTE[p], 'Ensemble', sum(pp[kk][0] for kk in ks), sum(pp[kk][1] for kk in ks),
                       md(sum(sum(f(r['rendement_2026_M']) for r in pp[kk][2]) for kk in ks))])
        for kk in ks:
            lignes.append([None, NOM_DEV[kk[1]][0].upper() + NOM_DEV[kk[1]][1:], pp[kk][0], pp[kk][1], md(som(pp[kk][2]))])
    lignes.append(['Total', None, n_tot, len(vides), md(tot_exact)])
    ws = feuille(wb, 'Par poste du tableau', ['Poste du tableau', 'Devenir', 'Prélèvements', 'Dont sans rendement publié',
                                              'Rendement 2026, indicatif (Md€)'], lignes, {'Poste du tableau': 46, 'Devenir': 46}, filtre=False)
    habiller(ws)

    # ---- Passage
    cols = ['Poste du tableau', 'Montant 2024 au tableau (Md€)', 'Taxes à supprimer au tableau (Md€)', 'Prélèvements du tri',
            'Dont sans rendement publié', 'Rendement 2026 au tri, indicatif (Md€)', 'Dont supprimé au tri (Md€)', 'Dont gardé au tri (Md€)',
            'Écart de montant, tri moins tableau (Md€)', 'Écart sur le supprimé, tri moins tableau (Md€)', 'Lecture']
    lignes = []
    for r in P:
        p = r['poste']
        nom = POSTE[p] if p in POSTE else 'Hors tableau : ' + p.split(' — ')[1]
        iv = lambda kk: int(r[kk]) if r[kk] != '' else None
        lignes.append([nom, md(r['montant_2024_M']), md(r['a_supprimer_2024_M']), iv('rangs'), iv('sans_rendement'),
                       md(r['rendement_2026_M']), md(r['supprime_2026_M']), md(r['garde_2026_M']), md(r['ecart_montant_M']),
                       md(r['ecart_supprime_M']), r['lecture'].replace('conservé en complément', 'complément sectoriel harmonisé')
                       .replace('Conservé en complément', 'Complément sectoriel harmonisé')])
    ws = feuille(wb, 'Passage', cols, lignes, {'Poste du tableau': 46, 'Lecture': 110}, filtre=False)
    for c in ws[1]:
        c.font, c.fill = BLANC, TETE

    # ---- Lisez-moi
    ws = wb.create_sheet('Lisez-moi')
    L = [('Le tri des impôts', ''), ('', ''),
         ('Objet', f'{n_tot} prélèvements obligatoires recensés : impôts, taxes, contributions et cotisations. Chacun reçoit un devenir dans la réforme, parmi six.'),
         ('Montants', f'Indicatifs, en gris : {len(vides)} prélèvements sur {n_tot} n’ont pas de rendement publié aux annexes du budget, et les totaux portent sur les {chiffres} autres. '
                      'Prévision 2026 du budget 2026 : milliards d’euros à une décimale, sauf l’onglet « Le tri », en millions d’euros.'),
         ('', ''), ('Les six devenirs', '')]
    for d in DEVENIRS:
        L.append((NOM_DEV[d][0].upper() + NOM_DEV[d][1:], f'{len(par_dev[d])} prélèvements. ' + DEF[d]))
    L += [('', ''), ('Les onglets', ''),
          ('Avant, après', 'Ce que chaque grand impôt reprend, dans l’ordre du graphique « 434 prélèvements aujourd’hui, 4 grands impôts demain » ; puis le passage des comptes nationaux au tableau de la refonte fiscale, et aux prélèvements du tri.'),
          ('Le tri', 'Une ligne par prélèvement, dans l’ordre du graphique ; les cotisations à fusionner sont regroupées en bas.'),
          ('Par devenir', 'Nombre et rendement par devenir, par impôt de remplacement et par bloc.'),
          ('Par poste du tableau', 'Nombre et rendement par poste du tableau « Refonte fiscalité » et par devenir.'),
          ('Passage', 'Chaque poste du tableau « Refonte fiscalité » face aux prélèvements du tri qui s’y rattachent.'),
          ('', ''),
          ('CSG et CRDS', 'Elles sont remplacées par l’impôt sur le revenu, dont le taux unique de 23 % se calcule sur une assiette qui intègre la leur.'),
          ('Sources', 'Projets de loi de finances pour 2026 et pour 2027, évaluation des voies et moyens ; code général des impôts, code des impositions sur les biens et services, code de la sécurité sociale et autres textes en vigueur ; comptes nationaux de l’Insee, tableau 3.217.')]
    for a, b in L:
        ws.append([a, b])
    ws['A1'].font = Font(bold=True, size=14, color='B23A10')
    for row in ws.iter_rows():
        row[0].alignment = row[1].alignment = HAUT
        if row[0].value in ('Les six devenirs', 'Les onglets', 'Montants'):
            row[0].font = GRAS
    ws.column_dimensions['A'].width = 40
    ws.column_dimensions['B'].width = 120
    wb.save(SORTIE)
    return T, n_tot, len(vides), m(tot_exact)


def md(x):
    """Montant en Md€, une décimale ; une case vide reste vide."""
    if x in ('', None):
        return None
    return round(float(x) / 1000, 1)


def titre_bloc(ws, lig, texte, sous=None):
    ws.cell(row=lig, column=1, value=texte).font = Font(bold=True, size=13, color='B23A10')
    if sous:
        ws.cell(row=lig + 1, column=1, value=sous).font = Font(italic=True, color='6D6A64')
        return lig + 2
    return lig + 1


def ecrire(ws, lig, v, gras=False, fond=None, indic=(), largeur_texte=()):
    for j, x in enumerate(v, 1):
        c = ws.cell(row=lig, column=j, value=x)
        c.border = FIL
        c.alignment = Alignment(vertical='center', wrap_text=(j in largeur_texte))
        if isinstance(x, float):
            c.number_format = MD
        elif isinstance(x, int):
            c.number_format = NB
        if gras:
            c.font = GRAS
        if fond:
            c.fill = fond
        if j in indic:
            c.font = Font(bold=gras, italic=True, color='8C8C8C')


def vue_ensemble(ws, T, P, ordre, col_g, par_dev, vides, tot_exact):
    """Onglet de tête (auteure, 20261124) : l'avant / après par grand impôt, puis la réconciliation
    du macro au micro — comptes nationaux (Insee, tableau 3.217) → tableau « Refonte fiscalité » → tri.
    Md€ à une décimale ; le rendement du tri, incomplet, en gris et en dernière colonne."""
    n_tot = len(T)
    ws.title = 'Avant, après'
    ws.sheet_view.showGridLines = False
    ws['A1'] = f'{n_tot} prélèvements aujourd’hui, 4 grands impôts demain'
    ws['A1'].font = Font(bold=True, size=16, color='B23A10')
    ws['A2'] = ('En haut, chaque prélèvement rangé sous l’impôt qui le reprend. Dessous, le passage des comptes nationaux '
                'au tableau de la refonte, puis aux prélèvements du tri.')
    ws['A2'].font = Font(italic=True, color='6D6A64')
    G = 7  # colonne du rendement indicatif

    # 1. Avant / après
    lig = titre_bloc(ws, 4, '1. Aujourd’hui, demain : par grand impôt', 'Dans l’ordre du graphique « 434 prélèvements aujourd’hui, 4 grands impôts demain ».')
    entete(ws, lig, ['Demain', 'Aujourd’hui : prélèvements', 'dont grand impôt conservé', 'dont remplacés par le grand impôt',
                     'dont compléments sectoriels harmonisés', 'dont fondus dans l’équilibre', 'Rendement 2026, indicatif (Md€)', 'Les plus lourds'])
    lig += 1
    haut = lig
    for g in ['Impôt sur le revenu', 'Impôt sur les sociétés', 'TVA', 'Taxe foncière', 'Cotisation unique', 'Hors impôts']:
        rs = [r for r in ordre if demain(r, col_g) == g]
        if not rs:
            continue
        n = lambda d: sum(1 for r in rs if r['devenir'] == d) or None
        lourds = ' ; '.join(r['libelle'] for r in sorted(rs, key=lambda r: -f(r['rendement_2026_M']))[:3] if r['rendement_2026_M'] != '')
        if g == 'Cotisation unique':
            lourds = f'{n("à fusionner") or 0} cotisations à fusionner' + (f' ; {lourds}' if lourds else '')
        nom = {'Cotisation unique': 'Cotisation unique (travail)', 'Hors impôts': 'Recettes non fiscales'}.get(g, g)
        s = som(rs)
        ecrire(ws, lig, [nom, len(rs), n('grand impôt conservé'), n('remplacé par un grand impôt'), n('conservé en complément'),
                         n('fondu dans l’équilibre des quatre grands impôts'), None if s is None else round(s / 1000, 1), lourds],
               indic=(G,), largeur_texte=(8,))
        ws.cell(row=lig, column=1).font = GRAS
        ws.row_dimensions[lig].height = 30
        lig += 1
    ecrire(ws, lig, ['Total', n_tot] + [len(par_dev[d]) or None for d in ('grand impôt conservé', 'remplacé par un grand impôt',
            'conservé en complément', 'fondu dans l’équilibre des quatre grands impôts')] + [round(tot_exact / 1000, 1), None],
           gras=True, fond=SABLE, indic=(G,))
    lig += 3

    # 2. Des comptes nationaux au tableau de la refonte
    t4 = {}
    for r in load_workbook(TABLETTES, read_only=True, data_only=True)['T4'].iter_rows(values_only=True):
        if r and len(r) > 2 and isinstance(r[2], (int, float)):
            t4.setdefault(r[0] or '=', []).append(r[2])
    val = lambda debut: next(v[0] for k, v in t4.items() if k.startswith(debut))
    pib = val('PIB')
    brut, nr, ci, cr = val('Ensemble'), val('− non recouvrés'), val('− cotisations imputées'), val('− crédits')
    projet = brut + nr + ci
    tab = sum(float(r['montant_2024_M']) for r in P if r['poste'] in POSTE and not r['poste'].startswith(('dont', 'à titre'))
              and r['montant_2024_M'] != '') / 1000
    lig = titre_bloc(ws, lig, '2. Des comptes nationaux au tableau de la refonte, 2024', 'Source : Insee, comptes nationaux, tableau 3.217.')
    entete(ws, lig, ['', 'Md€', 'En % du PIB'])
    lig += 1
    for nom, v, gras in [
            ('Impôts et cotisations sociales, total des comptes nationaux', brut, False),
            ('− impôts et cotisations dus et jamais encaissés (non recouvrés)', nr, False),
            ('− cotisations imputées : prestations versées directement par l’employeur, sans cotisation effective', ci, False),
            ('Base du projet : impôts et cotisations recouvrables, crédits d’impôt compris', projet, True),
            ('− crédits d’impôt, déduits par l’Insee', cr, False),
            ('Prélèvements obligatoires publiés par l’Insee', projet + cr, True)]:
        ecrire(ws, lig, [nom, round(v, 1), round(v / pib, 3)], gras=gras, fond=SABLE if gras else None, largeur_texte=(1,))
        ws.cell(row=lig, column=3).number_format = '0.0 %'
        lig += 1
    lig += 1
    for nom, v, gras in [('Base du projet, répartie en deux :', None, True),
                         ('dont postes du tableau de la refonte (bloc 3)', tab, False),
                         ('dont hors tableau : cotisations sociales, CSG, CRDS, prélèvements sociaux (bloc 4)', projet - tab, False)]:
        ecrire(ws, lig, [nom, None if v is None else round(v, 1), None if v is None else round(v / pib, 3)], gras=gras, largeur_texte=(1,))
        ws.cell(row=lig, column=3).number_format = '0.0 %'
        lig += 1
    lig += 2

    # 3. Le tableau de la refonte, poste par poste
    lig = titre_bloc(ws, lig, '3. Le tableau de la refonte, poste par poste, face aux prélèvements du tri',
                     'Montants du tableau : comptes nationaux 2024. Rendement : prévision 2026 du budget, pour les seuls prélèvements dont il est publié.')
    entete(ws, lig, ['Poste du tableau', 'Montant 2024 (Md€)', 'dont taxes à supprimer (Md€)', 'Prélèvements rattachés',
                     'dont supprimés', 'dont gardés', 'Rendement 2026, indicatif (Md€)'])
    lig += 1
    garde = ('grand impôt conservé', 'conservé en complément')
    supprime = ('remplacé par un grand impôt', 'fondu dans l’équilibre des quatre grands impôts')
    par_poste = defaultdict(list)
    for r in T:
        par_poste[r['poste_tableau']].append(r)
    lignes, parent = [], None
    for r in P:
        p = r['poste']
        if p.startswith('hors tableau'):
            continue
        sous = p.startswith(('dont', 'à titre'))
        if not sous:
            parent = {'p': p, 'r': r, 'enfants': []}
            lignes.append(parent)
        else:
            parent['enfants'].append(r)
    nomme = {'Taxes sur la consommation*': 'Taxes sur la consommation, hors TVA', 'Droits de mutation': 'Droits de mutation',
             "Taxes sur la main d'œuvre": 'Taxes sur la main-d’œuvre', 'IR net': 'Impôt sur le revenu (net)', 'IS net': 'Impôt sur les sociétés (net)'}
    sousnom = lambda p: 'dont ' + POSTE[p].split(' : ')[-1].replace('Droits de mutation à titre', 'à titre').replace('Consommation : ', '')

    def compte(rs):
        if not rs:
            return [None, None, None, None]
        s = som(rs)
        return [len(rs), sum(1 for r in rs if r['devenir'] in supprime) or None, sum(1 for r in rs if r['devenir'] in garde) or None,
                None if s is None else round(s / 1000, 1)]

    for L in lignes:
        r, p = L['r'], L['p']
        propres = par_poste.get(p, [])
        tous = propres + [x for e in L['enfants'] for x in par_poste.get(e['poste'], [])]
        n = compte(tous)
        ecrire(ws, lig, [nomme.get(p, POSTE[p]), md(r['montant_2024_M']), md(r['a_supprimer_2024_M']) or None] + n[:3] + [n[3]],
               gras=True, indic=(G,))
        lig += 1
        for e in L['enfants']:
            n = compte(par_poste.get(e['poste'], []))
            ecrire(ws, lig, ['    ' + sousnom(e['poste']), md(e['montant_2024_M']), md(e['a_supprimer_2024_M']) or None] + n[:3] + [n[3]], indic=(G,))
            lig += 1
        if L['enfants'] and propres:
            n = compte(propres)
            ecrire(ws, lig, ['    dont autres ' + nomme.get(p, POSTE[p])[0].lower() + nomme.get(p, POSTE[p])[1:], None, None] + n[:3] + [n[3]], indic=(G,))
            lig += 1
    n = compte([r for r in T if r['poste_tableau'] != '—'])
    ecrire(ws, lig, ['Total du tableau de la refonte', round(tab, 1), None] + n[:3] + [n[3]], gras=True, fond=SABLE, indic=(G,))
    lig += 1
    ws.cell(row=lig, column=1, value='Supprimés : remplacés par un grand impôt ou fondus dans l’équilibre. Gardés : grands impôts '
                                     'et compléments sectoriels harmonisés. Les autres sont des recettes non fiscales.').font = INDIC
    lig += 3

    # 4. Hors du tableau
    lig = titre_bloc(ws, lig, '4. Hors du tableau de la refonte')
    entete(ws, lig, ['Devenir', '', '', 'Prélèvements du tri', '', '', 'Rendement 2026, indicatif (Md€)'])
    lig += 1
    libelles = {'remplacé par un grand impôt': 'Remplacés par un grand impôt : CSG, CRDS, prélèvements sociaux…',
                'conservé en complément': 'Compléments sectoriels harmonisés',
                'à fusionner': 'Cotisations sociales, à fusionner en une cotisation unique',
                'recette non fiscale': 'Recettes non fiscales'}
    hors = [r for r in T if r['poste_tableau'] == '—']
    for d in DEVENIRS:
        rs = [r for r in hors if r['devenir'] == d]
        if rs:
            n = compte(rs)
            ecrire(ws, lig, [libelles.get(d, NOM_DEV[d][0].upper() + NOM_DEV[d][1:]), None, None, n[0], None, None, n[3]], indic=(G,))
            lig += 1
    n = compte(hors)
    ecrire(ws, lig, ['Total hors tableau', None, None, n[0], None, None, n[3]], gras=True, fond=SABLE, indic=(G,))
    lig += 1
    n = compte(T)
    ecrire(ws, lig, ['Total des prélèvements du tri (blocs 3 et 4)', None, None, n[0], None, None, n[3]], gras=True, fond=SABLE, indic=(G,))
    lig += 2
    ws.cell(row=lig, column=1, value=f'Rendement indicatif : {len(vides)} prélèvements sur {n_tot} n’ont pas de rendement publié '
                                     '(cotisations sociales, taxes affectées à des organismes, impôts locaux). '
                                     'Le rendement des cotisations sociales n’y figure donc presque pas.').font = INDIC
    for j, w in enumerate([62, 16, 16, 17, 17, 16, 17, 95], 1):
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.freeze_panes = 'A3'


def habiller(ws):
    for c in ws[1]:
        c.font, c.fill = BLANC, TETE
    for row in ws.iter_rows(min_row=2):
        row[-1].font = INDIC
        if row[0].value:
            for c in row[:-1]:
                c.font = GRAS
            row[-1].font = Font(bold=True, italic=True, color='8C8C8C')


def relire(T, n_tot, n_vides, total):
    ko = []
    wb = load_workbook(SORTIE)
    if wb.sheetnames != ['Avant, après', 'Le tri', 'Par devenir', 'Par poste du tableau', 'Passage', 'Lisez-moi']:
        ko.append(f'onglets : {wb.sheetnames}')
    for ws in wb.worksheets:
        for row in ws.iter_rows(values_only=True):
            for j, v in enumerate(row):
                motif = SOURCE if (ws.title == 'Le tri' and j in (1, 8)) else INTERDIT
                if ws.title == 'Avant, après' and j == 7:
                    motif = SOURCE
                if isinstance(v, str) and not v.startswith('https://') and motif.search(v):
                    ko.append(f'{ws.title} : mention interne « {motif.search(v).group()} » dans « {v[:60]} »')
                if isinstance(v, float) and (ws.title == 'Le tri' or round(v, 3) != v):
                    ko.append(f'{ws.title} : montant décimal {v}')
                if isinstance(v, str) and v.lower().startswith('dont part gardée'):
                    ko.append(f'{ws.title} : « part gardée » encore présent')
    tri = [l for l in wb['Le tri'].iter_rows(min_row=2, values_only=True) if isinstance(l[0], int)]
    if len(tri) != n_tot:
        ko.append(f'Le tri : {len(tri)} lignes')
    devs = {NOM_DEV[d][0].upper() + NOM_DEV[d][1:] for d in DEVENIRS}
    if set(l[3] for l in tri) != devs:
        ko.append('Le tri : les devenirs ne sont pas les six')
    if sum(1 for l in tri if l[10] is None) != n_vides:
        ko.append('Le tri : compte des cases vides')
    fus = [i for i, l in enumerate(tri) if l[3] == 'À fusionner']
    if fus and fus[0] != len(tri) - len(fus):
        ko.append('Le tri : les cotisations à fusionner ne sont pas toutes en bas')
    for nom in ('Par devenir', 'Par poste du tableau'):
        ll = list(wb[nom].iter_rows(min_row=2, values_only=True))
        ens = [l for l in ll if l[1] == 'Ensemble']
        tot = ll[-1]
        if sum(l[2] for l in ens) != tot[2] or sum(l[3] for l in ens) != tot[3]:
            ko.append(f'{nom} : les comptes ne rebouclent pas')
        if abs(sum(l[4] or 0 for l in ens) - tot[4]) > len(ens) * 0.05 + 0.05:
            ko.append(f'{nom} : les montants ne rebouclent pas ({sum(l[4] for l in ens)} contre {tot[4]})')
        print(f'  {nom} : {len(ens)} ensembles, {tot[2]} prélèvements, total {tot[4]}')
    sy = list(wb['Avant, après'].iter_rows(min_row=7, values_only=True))
    k = next(i for i, l in enumerate(sy) if l[0] == 'Total')
    tl = sy[k]
    if sum(l[1] for l in sy[:k] if isinstance(l[1], int)) != tl[1] or tl[1] != n_tot:
        ko.append('Avant, après : les comptes ne rebouclent pas')
    t3 = next(l for l in sy if l[0] == 'Total du tableau de la refonte')
    t4 = next(l for l in sy if l[0] == 'Total hors tableau')
    if t3[3] + t4[3] != n_tot:
        ko.append('Avant, après : tableau et hors tableau ne rebouclent pas sur le total')
    print(f'  Le tri : {len(tri)} lignes, {n_vides} sans rendement ; synthèse : {tl[1]} prélèvements')
    return ko


def main():
    T, n_tot, n_vides, total = construire()
    ko = relire(T, n_tot, n_vides, total)
    if ko:
        print(f'\nÉCHEC — {len(ko)} écart(s) :')
        for k in ko[:30]:
            print('  ', k)
        return 1
    print('  0 écart : aucune mention interne, aucun montant décimal, six devenirs, cotisations en bas, totaux rebouclés.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
