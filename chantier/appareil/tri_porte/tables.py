"""Tables de livraison : vérification, relecture des annexes, sorts contre le schéma, niches."""
import csv, json, sys, collections, re
W = '/home/user/Resolution-2027/chantier/appareil/tri_porte/'
sys.path.insert(0, W)
from verdicts import V
OUT = '/home/user/Resolution-2027/chantier/livrables/tri_prelevements/'
T = json.load(open(W + 'tri_20261103.json'))
REL = json.load(open(W + 'relecture.json'))
A120 = [int(x) for x in open(W + 'annexeA.txt').read().split()]
VD = {v[0]: v for v in V}

def w(name, rows, cols):
    with open(OUT + name, 'w', newline='') as fh:
        x = csv.DictWriter(fh, fieldnames=cols, delimiter='\t', extrasaction='ignore'); x.writeheader(); x.writerows(rows)

# 1. vérification : les 120 de l'annexe A, puis tous les autres rangs remplacés ou fondus
ver = []
for r in T:
    if r['devenir'] not in ('remplacé par un grand impôt', 'fondu dans l’équilibre des quatre grands impôts'):
        continue
    v = VD.get(r['n'])
    ver.append(dict(rang=r['n'], liste='annexe A (120)' if r['n'] in A120 else ('rang ajouté' if str(r['n']).startswith('N') else 'hors annexe A'),
                    prelevement=r['libelle'], devenir=r['devenir'], impot_cible=r['impot_cible'], verdict=r['verdict'],
                    amendement=(v[2] if v else r['amendement_porteur']) if r['verdict'] in ('A', 'B') else '',
                    alinea=(v[3] if v else r['alinea']) if r['verdict'] in ('A', 'B') else '',
                    citation=(v[4] if v else ''), provenance=r['provenance'],
                    famille_redaction=(v[6] if v else ''), porteur_propose=r['amendement_porteur'] if r['verdict'] == 'C' else '',
                    observation=(v[7] if v else '')))
for n in A120:
    if not any(x['rang'] == n for x in ver):
        v = VD[n]
        ver.append(dict(rang=n, liste='annexe A (120)', prelevement='Taxe sur les papiers graphiques', devenir='rang retiré du tri', impot_cible='',
                        verdict=v[1], amendement='', alinea='', citation=v[4], provenance=v[5], famille_redaction=v[6], porteur_propose='',
                        observation='rang retiré : aucune imposition de ce nom au droit en vigueur'))
w('verification_porteurs_20261103.tsv', ver, list(ver[0].keys()))

# 2. relecture des annexes, achevée
BIG = {151: 'révision de rendement (même bénéficiaire, CNAM)', 337: 'révision de rendement (même bénéficiaire)',
       382: 'révision de rendement (mêmes deux bénéficiaires)', 185: 'changement de périmètre : part des communes concernées, 18,0, ajoutée en 2027',
       180: 'révision de rendement (même bénéficiaire, CGLLS)', 385: 'révision de rendement (part des régions ramenée à 0)'}
rel = []
for d in REL:
    n = d['n']
    if n in (270, 279):
        dec = 'retiré' if n == 270 else 'fusionné avec le rang 272'
    elif n in (132, 144, 158, 196, 407):
        dec = 'corrigé au montant de l’état A, LFI 2026' + (' ; agrégat à éclater' if n == 407 else '')
    elif d['verdict'] == 'écart' and d['source'] == 'ressources affectées':
        dec = 'conforme à sa source (PLF 2026) ; actualisation suspendue au millésime'
    elif d['verdict'] == 'écart':
        dec = 'écart de source mineur (liste IFRAP contre état A) ; alignement suspendu au millésime'
    elif d['verdict'].startswith('concordant'):
        dec = 'aucune'
    elif d['source'] == 'aucune annexe':
        dec = 'source IFRAP seule ; pièce publique non versée au dépôt (LFSS annexe 4, rapport sur les prélèvements obligatoires, comptes DGCL)'
    elif 'absent' in d['verdict']:
        dec = 'ressource absente de l’annexe 2027 : extinction ou renommage, à lire au PLF 2027'
    else:
        dec = d['verdict']
    rel.append(dict(rang=n, prelevement=d['libelle'], source=d['source'], millesime_tri='prévision 2026 initiale (PLF 2026 / LFI 2026)',
                    montant_tri=d['tri'], part_affectee_tri=d['tri_affecte'], plf2026_prev2026=d['plf26'], plf2027_prev2026_revisee=d['plf27_rev26'],
                    etatA_lfi2026=d['etatA_lfi26'], etatA_revise_plf2027=d['etatA_rev26'], etatA_2027=d['etatA_2027'],
                    ecart_pct=d.get('ecart_pct', ''), verdict=d['verdict'], perimetre=BIG.get(n, ''), decision=dec))
w('relecture_annexes_20261103.tsv', rel, list(rel[0].keys()))
print('relecture', collections.Counter((x['source'], x['verdict']) for x in rel))

# 3. sorts contre le schéma
H = {'dont énergie*': -8.0, 'dont alcool, tabac, jeux': -0.3, 'dont assurances': None, 'dont redevances sur l\'eau': -2.2,
     'dont services de transports': -1.9, 'dont véhicules': -6.4, 'dont numérique, spectacles': -1.8,
     'dont autres taxes sur les produits': -4.5, 'dont taxe de séjour': None, 'dont taxe pollution': -1.0, 'dont outre-mer': None,
     'Taxes sur la main d\'œuvre': -48.0, 'IR net': None, 'IS net': None, 'Taxes sur chiffre d\'affaires et bénéfices': -10.3,
     'Taxe foncière': None, 'Autres taxes sur les ménages': -6.7, 'Autres taxes sur les entreprises': -13.5,
     'à titre onéreux': -12.05, 'à titre gratuit': -20.4, 'TVA': None, 'dont forfaits de cotisation': None, 'Droits de mutation': None}
EXPL = {'dont énergie*': 'H17 porte la suppression des certificats d’économies d’énergie (6 à 8 Md€, note E6), qui ne sont pas un rang du tri ; aucune accise n’est supprimée (bloc accise)',
        'dont alcool, tabac, jeux': 'le tri supprime les prélèvements sur les jeux (6,7 Md€) ; le schéma n’en retient que 0,3 : divergence à trancher',
        'dont véhicules': 'le schéma retient 6,4 contre 3,9 au tri, dont 3 rangs sans rendement : écart non expliqué à ce stade',
        'dont autres taxes sur les produits': 'la TSA (6,7 Md€) est rangée ici au tri ; sans elle le tri donne 3,9 contre 4,5',
        'Taxes sur la main d\'œuvre': 'C29 = 58 dont 8,8 de forfaits conservés ; tri 41,8 au millésime 2026 contre 48 au schéma (2024) ; 6 rangs sans rendement',
        'IR net': 'H vide (conservation) mais 11 rangs rattachés à la ligne sont « remplacés » au tri (12,6 Md€, dont retenues à la source 5,9) : question 4',
        'Taxe foncière': 'H vide : les composantes fondues dans la taxe foncière unique gardent leur produit (C37), ce qui vaut conservation du produit',
        'Taxes sur chiffre d\'affaires et bénéfices': 'tri 13,6 contre 10,3 ; avec la CVAE corrigée à l’état A (+1,3) l’écart passe à 4,6 : millésime 2026 contre 2024',
        'Autres taxes sur les entreprises': 'tri 7,3 contre 13,5 : 18 rangs sans rendement',
        'à titre onéreux': 'net de la part conservée au tarif de 1 % et 3 % (P1 n° 19, 5,05 Md€ selon le schéma) ; écart de millésime : 19,3 Md€ en 2026 contre 17,1 en 2024',
        'à titre gratuit': 'net de la part conservée au tarif de 1 % et 3 % (P1 n° 19, 6 Md€ selon le schéma) ; H42 retire aussi 5,6 Md€ de niches et de gisement (colonnes E à G) : droits seuls, 14,8 au schéma contre 15,4 au tri',
        'Autres taxes sur les ménages': 'concordant à l’écart de millésime près',
        'dont redevances sur l\'eau': 'concordant à l’écart de millésime près', 'dont numérique, spectacles': 'concordant à l’écart de millésime près',
        'dont taxe pollution': 'concordant à l’écart de millésime près', 'dont services de transports': 'tri 3,6 contre 1,9 : écart de millésime et de périmètre non expliqué à ce stade'}
g = collections.defaultdict(lambda: [0, 0.0, 0])
S15 = list(csv.DictReader(open('/home/user/Resolution-2027/chantier/referentiels/sort_prelevements_20261015.tsv'), delimiter='\t'))
lig = {i: s['ligne_schema'] for i, s in enumerate(S15, 1)}
for r in T:
    if isinstance(r['n'], int) and r['devenir'] in ('remplacé par un grand impôt', 'fondu dans l’équilibre des quatre grands impôts'):
        k = lig[r['n']]; g[k][0] += 1; g[k][2] += 0 if r['rendement_2026_M'] else 1
        g[k][1] += float(r['rendement_2026_M'] or 0) - float(r.get('part_conservee_2026_M') or 0)   # part conservée : P1 n° 19
sch = []
for k, (nr, som, sans) in sorted(g.items()):
    h = H.get(k)
    sch.append(dict(ligne_schema=k, rangs_supprimes=nr, somme_tri_2026_Md=round(som / 1000, 1), sans_rendement=sans,
                    H_taxes_a_supprimer_2024_Md='' if h is None else -h, ecart_Md='' if h is None else round(som / 1000 + h, 1),
                    explication=EXPL.get(k, 'ligne hors schéma (cotisations, contributions sociales)' if k == '—' else '')))
w('sorts_contre_schema_20261103.tsv', sch, list(sch[0].keys()))

# 4. niches : clause générale
N = json.load(open(W + 'niches.json'))
for x in N:
    x['devenir'] = {'Oui': 'supprimée, gain restitué', 'En 3 ans': 'supprimée en trois ans, gain restitué',
                    'Fusion CI IR': 'fondue dans l’aide fondamentale', 'Flux OM': 'fiscalité outre-mer', '': 'déjà éteinte ou non chiffrée'}[x['sort']]
w('niches_clause_generale_20261103.tsv', N, ['numero', 'cat', 'siege', 'devenir', 'verdict_clause', 'nominatif', 'bilan', 'bornee', 'etat'])
print('niches', collections.Counter((x['devenir'], x.get('verdict_clause')) for x in N))
