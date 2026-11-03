import csv, json, re, sys, collections, xlrd
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter
W = '/home/user/Resolution-2027/chantier/appareil/tri_porte/'
sys.path.insert(0, W)
from amendements import AM
OUT = '/home/user/Resolution-2027/chantier/livrables/tri_prelevements/'
T = json.load(open(W + 'tri_20261103.json'))
N = json.load(open(W + 'niches.json'))
DEVN = {'Oui': 'supprimée, gain restitué', 'En 3 ans': 'supprimée en trois ans, gain restitué', 'Fusion CI IR': 'fondue dans l’aide fondamentale', 'Flux OM': 'fiscalité outre-mer', '': 'déjà éteinte'}
for x in N: x['devenir'] = DEVN[x['sort']]
sh = xlrd.open_workbook('/home/user/Site-ETNP/site/donnees/PLF 2026_V&M tome II - Annexe 3 - Depenses fiscales - 0910.xls').sheet_by_name('Chiffrages Résolution')
LIB, MT = {}, {}
for r in range(6, sh.nrows):
    num = str(sh.cell_value(r, 3)).replace('.0', '')
    if num.strip():
        LIB[num] = str(sh.cell_value(r, 4)).strip()
        v = sh.cell_value(r, 9)
        MT[num] = v if isinstance(v, float) else None
H = Font(bold=True); WRAP = Alignment(wrap_text=True, vertical='top'); FILL = PatternFill('solid', fgColor='DDDDDD')


def sheet(wb, title, cols, rows, widths=None):
    ws = wb.create_sheet(title)
    ws.append(cols)
    for c in ws[1]:
        c.font = H; c.fill = FILL; c.alignment = WRAP
    for r in rows:
        ws.append(r)
    for i, c in enumerate(cols, 1):
        ws.column_dimensions[get_column_letter(i)].width = (widths or {}).get(c, 18)
    ws.freeze_panes = 'A2'
    return ws


def tsv(name):
    return list(csv.DictReader(open(OUT + name), delimiter='\t'))


# ------------------------------------------------------------ classeur de travail
wb = Workbook(); wb.remove(wb.active)
cols = list(T[0].keys())
sheet(wb, 'Tri', cols, [[r[c] for c in cols] for r in T], {'libelle': 50, 'siege': 40, 'observation': 50, 'question': 40, 'lien_legifrance': 30})
for name, t in [('Vérification', 'verification_porteurs_20261103.tsv'), ('Relecture des annexes', 'relecture_annexes_20261103.tsv'),
                ('Sorts contre le schéma', 'sorts_contre_schema_20261103.tsv'), ('Niches', 'niches_clause_generale_20261103.tsv')]:
    rr = tsv(t); c = list(rr[0].keys())
    sheet(wb, name, c, [[x[k] for k in c] for x in rr], {'prelevement': 50, 'citation': 60, 'observation': 50, 'explication': 70, 'decision': 50})
sheet(wb, 'Amendements nouveaux', ['liasse', 'n°', 'objet', 'article visé', 'rangs portés', 'gage', 'rattachement', 'fichier'],
      [[a['liasse'], a['n'], a['objet'], a['vise'], ', '.join(map(str, a['rangs'])), a['gage'], a['lolf'], a['fichier']] for a in AM],
      {'objet': 60, 'rangs portés': 40, 'gage': 40, 'rattachement': 50})
wb.save(OUT + 'Tri_prelevements_travail_20261103.xlsx')

# ------------------------------------------------------------ version exportable
INTERDIT = re.compile(r'\b(?:A|M|D)-\d+|\d{8}|à confirmer|à vérifier|probable|n\.d\.|relevé par le fil|\.tsv|\.md|\.xlsx|\.py|tri du|IFRAP', re.I)


def m(v):
    if v in ('', None):
        return ''
    v = float(v)
    return round(v) if abs(v) >= 10 else round(v, 1)


def propre(s):
    s = '' if s is None else str(s)
    return '' if INTERDIT.search(s) else s


LIASSE = {'PLF P1': 'PLF 2027, 1re partie', 'PLF P2': 'PLF 2027, 2de partie', 'PLFSS': 'PLFSS 2027'}


def porteur(r):
    p = r['amendement_porteur']
    if not p:
        return 'abrogé par le droit en vigueur' if r['verdict'] == 'S' else ''
    k, n = p.split(' n° ')
    return f"{LIASSE[k]}, amendement n° {n}" + (f", {r['alinea']}" if r['alinea'] else '')


wb = Workbook(); ws = wb.active; ws.title = 'Présentation'
PRES = [
 ('Le tri des prélèvements obligatoires', ''),
 ('', ''),
 ('Objet', 'Chaque prélèvement obligatoire recensé reçoit un devenir dans la réforme : il est conservé, remplacé par l’un des quatre grands impôts, fondu dans leur équilibre ou conservé en complément. Les montants sont en millions d’euros, prévision 2026.'),
 ('', ''),
 ('Les devenirs', ''),
 ('Grand impôt conservé', 'Impôt sur le revenu, impôt sur les sociétés, taxe sur la valeur ajoutée, taxe foncière.'),
 ('Remplacé par un grand impôt', 'Le prélèvement disparaît ; un impôt précis en reprend le produit.'),
 ('Fondu dans l’équilibre des quatre grands impôts', 'Le prélèvement disparaît ; son produit est repris par les hausses d’équilibre de la refonte : taxes sur la masse salariale, taxe sur les remontées mécaniques, redevance de ski de fond.'),
 ('Conservé en complément', 'Le prélèvement demeure à côté du grand impôt qu’il prolonge : accises sur l’énergie, le tabac et l’alcool ; impositions des activités sans TVA (taxe sur les conventions d’assurance, forfait social, contribution de solidarité pour l’autonomie, prélèvement du fonds de prévention des risques naturels) ; taxe de séjour unique ; fonds de garantie ; fiscalité outre-mer ; ressources de l’Union européenne.'),
 ('À fusionner', 'Les cotisations sociales, dont le schéma de fusion sera présenté séparément.'),
 ('Recette non fiscale', 'Ressource qui n’est pas un prélèvement obligatoire : redevance pour service rendu, redevance domaniale, produit de cession.'),
 ('', ''),
 ('Les niches', ''),
 ('Supprimée, gain restitué', 'L’avantage disparaît ; son produit est rendu par la baisse des prélèvements sur le travail.'),
 ('Supprimée en trois ans, gain restitué', 'L’avantage est réduit d’un tiers par an.'),
 ('Fondue dans l’aide fondamentale', 'L’avantage disparaît dans l’aide fondamentale versée à chacun.'),
 ('Fiscalité outre-mer', 'Régime propre aux collectivités d’outre-mer, conservé.'),
 ('Déjà éteinte', 'Avantage dont le fait générateur a pris fin.'),
 ('', ''),
 ('Perspectives', 'La CSG et la CRDS sont remplacées par l’impôt sur le revenu, dont le taux unique de 23 % se calcule sur une assiette qui intègre la leur. Deux perspectives accompagnent la réforme : la restitution lisible sur la fiche de paie et le compte épargne personnel. Elles ne constituent le devenir d’aucun prélèvement.'),
 ('', ''),
 ('Sources', 'Projets de loi de finances pour 2026 et 2027, évaluation des voies et moyens (tome I, annexes 1 et 2 ; tome II, dépenses fiscales) ; code général des impôts, code des impositions sur les biens et services, code de la sécurité sociale et autres textes, dans leur version en vigueur.'),
]
for a, b in PRES:
    ws.append([a, b])
ws['A1'].font = Font(bold=True, size=14)
for c in ('A5', 'A13', 'A20', 'A22'):
    ws[c].font = H
ws.column_dimensions['A'].width = 42; ws.column_dimensions['B'].width = 110
for row in ws.iter_rows():
    for c in row:
        c.alignment = WRAP

cols = ['Prélèvement', 'Nature', 'Assiette', 'Rendement 2026 (M€)', 'Devenir', 'Impôt cible', 'Bloc', 'Siège', 'Lien Légifrance', 'Niches rattachées', 'Amendement porteur', 'Ligne de l’article 42 du PLF 2027']
rows = []
for r in T:
    rows.append([r['libelle'], r['nature'], r['assiette'], m(r['rendement_2026_M']), r['devenir'], r['impot_cible'],
                 '' if r['bloc'] == 'à qualifier' else r['bloc'], propre(r['siege']).replace('—', ''), r['lien_legifrance'],
                 r['niches_rattachees'], propre(porteur(r)), r['ligne_art42']])
sheet(wb, 'Prélèvements', cols, rows, {'Prélèvement': 55, 'Siège': 40, 'Lien Légifrance': 32, 'Amendement porteur': 40, 'Devenir': 30})

# synthèse
syn = collections.defaultdict(lambda: [0, 0.0])
for r in T:
    k = (r['devenir'], r['impot_cible'] or r['bloc'] or '')
    syn[k][0] += 1; syn[k][1] += float(r['rendement_2026_M'] or 0)
ORD = ['grand impôt conservé', 'remplacé par un grand impôt', 'fondu dans l’équilibre des quatre grands impôts', 'conservé en complément', 'à fusionner', 'recette non fiscale']
srows = [[k[0], '' if k[1] == 'à qualifier' else k[1], v[0], m(v[1])] for k, v in sorted(syn.items(), key=lambda kv: (ORD.index(kv[0][0]), kv[0][1]))]
tot = sum(v[1] for v in syn.values())
srows.append(['Total', '', len(T), m(tot)])
sheet(wb, 'Synthèse', ['Devenir', 'Impôt cible ou bloc', 'Nombre de prélèvements', 'Rendement 2026 (M€)'], srows, {'Devenir': 45, 'Impôt cible ou bloc': 35})

# niches
nrows = []
for x in N:
    nrows.append([x['numero'], x['cat'], LIB.get(x['numero'], ''), m(MT.get(x['numero'])), x['devenir']])
sheet(wb, 'Niches', ['Numéro', 'Impôt', 'Libellé', 'Coût 2024 (M€)', 'Devenir'], nrows, {'Libellé': 80, 'Impôt': 35, 'Devenir': 35})
agg = collections.defaultdict(lambda: [0, 0.0])
for x in N:
    k = (x['cat'], x['devenir']); agg[k][0] += 1; agg[k][1] += MT.get(x['numero']) or 0
sheet(wb, 'Niches par impôt', ['Impôt', 'Devenir', 'Nombre de niches', 'Coût 2024 (M€)'],
      [[k[0], k[1], v[0], m(v[1])] for k, v in sorted(agg.items())], {'Impôt': 40, 'Devenir': 40})

# amendements
OBJ = {}
for liasse, fic in [('PLF 2027, 1re partie', 'LIASSE_PLF_P1.md'), ('PLF 2027, 2de partie', 'LIASSE_PLF_P2.md'), ('PLFSS 2027', 'LIASSE_PLFSS.md')]:
    t = open('/home/user/Resolution-2027/chantier/livrables/depot_2027/' + fic, encoding='utf-8').read()
    for n, o in re.findall(r'\n## Amendement n° (\d+) \[(.*?)\]\n', t):
        OBJ[f'{liasse}, amendement n° {n}'] = o
am = collections.defaultdict(int)
for r in T:
    p = porteur(r)
    if r['amendement_porteur']:
        am[re.match(r'(.*?amendement n° \d+)', p).group(1)] += 1
sheet(wb, 'Amendements', ['Amendement', 'Objet', 'Prélèvements portés'],
      [[k, OBJ.get(k, ''), v] for k, v in sorted(am.items(), key=lambda kv: (kv[0].split(',')[0], int(kv[0].rsplit('n° ', 1)[1])))],
      {'Amendement': 40, 'Objet': 90})
wb.save(OUT + 'Tri_prelevements_export.xlsx')

# contrôle mécanique de la version exportable : aucune mention interne
from openpyxl import load_workbook
bad = []
for wsx in load_workbook(OUT + 'Tri_prelevements_export.xlsx').worksheets:
    for row in wsx.iter_rows(values_only=True):
        for v in row:
            if isinstance(v, str) and not v.startswith('https://') and INTERDIT.search(v):
                bad.append((wsx.title, v[:80]))
            if isinstance(v, float) and abs(v) >= 10 and v != round(v):
                bad.append((wsx.title, v))
print('mentions interdites ou décimales :', len(bad), bad[:10])
print('lignes export', len(rows), 'synthèse total', m(tot))
