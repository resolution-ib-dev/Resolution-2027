"""Construit le tri du 20261103, la table de vérification, la relecture des annexes,
les sorts contre le schéma et la table des niches. Tout se recompte ici."""
import csv, json, re, sys, collections
W = '/home/user/Resolution-2027/chantier/appareil/tri_porte/'
sys.path.insert(0, W); sys.path.insert(0, '/home/user/Resolution-2027')
import droit
from verdicts import V
from amendements import AM
from matcher import sieges, VIS, VIS_NC

R = '/home/user/Resolution-2027/chantier/referentiels/'
OUT = '/home/user/Resolution-2027/chantier/livrables/tri_prelevements/'
S = list(csv.DictReader(open(R + 'sort_prelevements_20261015.tsv'), delimiter='\t'))
F = list(csv.DictReader(open(R + 'prelevements_forces_20260930.tsv'), delimiter='\t'))
REL = {d['n']: d for d in json.load(open(W + 'relecture.json'))}
H120 = {d['i']: d for d in json.load(open(W + 'hors120.json'))}
VD = {v[0]: v for v in V}
n_ = droit.norm_num

# ---------------------------------------------------------------- devenirs
A_CIBLE = {}  # impôt cible de l'annexe A (règle de ventilation déjà appliquée par l'auteur)
_a = """329 TF;86 IR;194 TVA;407 TF;134 IR;144 IS;131 IR;195 TVA;129 EQ;369 TF;183 IS;133 IR;282 TVA;95 IR;151 IS;380 IS;343 IR;146 IS;196 TVA;335 TF;284 TVA;147 IS;302 TF;288 TVA;152 IS;311 IS;312 IS;381 IS;285 TVA;178 IS;363 IR;125 EQ;379 TF;241 TVA;163 IS;293 EQ;410 IS;286 TVA;246 TVA;382 IS;326 TF;233 TVA;384 IS;319 IS;199 TVA;185 IS;201 TVA;385 IS;411 IS;119 EQ;365 IR;412 TF;390 IS;187 IS;295 EQ;391 IS;413 IR;168 IS;392 IS;414 IR;374 TF;415 IR;386 IS;70 IR;126 EQ;127 EQ;128 EQ;136 IR;140 IR;141 IR;154 IS;155 IS;156 IS;171 IS;172 IS;173 IS;174 IS;176 IS;188 IS;189 IS;190 IS;192 IS;270 TVA;289 TVA;290 TVA;303 TF;307 TF;317 IS;318 IS;320 IS;321 IS;322 IS;339 TF;350 IR;351 IR;354 IR;356 IR;358 IS;359 IR;360 IR;366 IR;367 IS;368 IR;375 TF;377 TF;387 IS;388 IS;393 IS;394 IS;395 IS;396 IS;397 IS;398 IS;399 IS;400 IS;401 IS;402 IS;403 IS;406 IS;417 IS"""
for t in _a.split(';'):
    k, v = t.split(); A_CIBLE[int(k)] = v
# ventilation « propriété et droits d'usage » pour les rangs hors annexe A (déduit de la règle)
VENT = {**{i: 'IS' for i in (309, 310, 313, 314, 315, 316, 323, 328, 349, 362, 371, 383, 389, 404, 405, 416)},
        **{i: 'IR' for i in (344, 345, 346, 347, 348, 352, 353, 355, 357, 361, 364, 409)}}
NOM = {'IR': 'Impôt sur le revenu', 'IS': 'Impôt sur les sociétés', 'TVA': 'Taxe sur la valeur ajoutée', 'TF': 'Taxe foncière'}
ABS = {'Impôt sur le revenu': 'IR', 'Impôt sur les sociétés': 'IS', 'Taxe sur la valeur ajoutée': 'TVA', 'Taxe foncière': 'TF'}

BLOC = {**{i: 'Accise (sur-TVA)' for i in (209, 210, 211, 212, 213, 214, 215, 217, 218, 219, 220, 221, 223, 224, 225, 226, 227, 230)},
        **{i: 'Fiscalité outre-mer' for i in (216, 222, 228, 229, 298)},
        **{i: 'Simili TVA' for i in (94, 98, 272, 278)},
        **{i: 'Fonds de garantie' for i in (273, 274, 275, 276)},
        **{i: 'Taxe de séjour unique' for i in (291, 292, 294, 252, 296, 297)},
        299: 'Union européenne', 300: 'à qualifier'}
GRANDS = {130: 'IR', 142: 'IS', 193: 'TVA', 304: 'TF', 133: 'IR', 134: 'IR', 140: 'IR'}
CONSERVE_BLOC = {146: 'Union européenne', 196: 'Union européenne', 380: 'Union européenne'}
REGL = {391, 392, 401, 403, 413, 414, 354, 367}
RETIRES = {270: 'retiré : aucune imposition de ce nom au droit en vigueur (CGI et CIBS, LEGI 20261031)',
           279: 'fusionné avec le rang 272 : même impôt, art. 991 CGI'}

NATURE = {'impôt ou taxe': 'impôt', 'taxe sur la masse salariale': 'impôt', 'cotisation sociale': 'cotisation sociale',
          'contribution sociale': 'contribution sociale', 'hors champ': 'recette non fiscale'}
ASS = {'1': 'le travail', '2': 'les revenus', '3': 'le travail', '4': 'les revenus', '5': 'l’activité des entreprises',
       '6': 'la consommation', '7': 'la propriété et les droits d’usage', '8': ''}

SIEGE_CORR = {129: ('L. 3253-18 du code du travail', 'travail', 'L. 3253-18'),
              363: ('L. 652-7 du code de la sécurité sociale', 'css', 'L. 652-7'),
              365: ('L. 652-6 du code de la sécurité sociale', 'css', 'L. 652-6'),
              70: ('L. 380-2 du code de la sécurité sociale', 'css', 'L. 380-2'),
              233: ('L. 213-14-1 et L. 213-14-2 du code de l’environnement', 'environnement', 'L. 213-14-1'),
              155: ('L. 138-19-8 à L. 138-19-13 du code de la sécurité sociale', 'css', 'L. 138-19-8'),
              369: ('Art. 1635 quater A du code général des impôts ; L. 331-1 s. du code de l’urbanisme', 'cgi', '1635 quater A'),
              182: ('Art. 299 à 299 septies du code général des impôts', 'cgi', '299'),
              239: ('L. 422-13 à L. 422-57 du code des impositions sur les biens et services (tarif de sûreté et de sécurité)', 'cibs', 'L. 422-20'),
              124: ('L. 2135-15-1 du code du travail', 'travail', 'L. 2135-15-1'),
              126: ('L. 4031-4 du code de la santé publique', 'sante', 'L. 4031-4')}

# porteurs des amendements nouveaux
NOUV = {}
for a in AM:
    for r in a['rangs']:
        NOUV[r] = f"{'PLF P1' if a['liasse']=='P1' else 'PLFSS'} n° {a['n']}"
ALIN_NOUV = {35: '« Supprimer cet article »'}
AL = {}
for i in (139,231,232,280,281,283,358,410,375,393,394,395,396,397,398,399,400,402): AL[i]='I, 1°'
AL[277]='I, 2°'
for i in (86,306,309,319,318): AL[i]='II, 1°'
for i in (183,184,192,386): AL[i]='II, 2°'
for i in (302,303,311,314,320,321,322,370,372,'n-321'): AL[i]='I, 1°'
for i in (282,289,293,295,379): AL[i]='I, 2°'
AL[371]='I, 4°'; AL[374]='I, 5°'; AL[312]='I, 6°'
AL.update({129:'I, 1°',125:'I, 2°',126:'I, 3°',389:'I, 3°',390:'I, 3°',201:'I, 4°',381:'I, 5°',415:'I, 6°',373:'I, 7°',385:'I, 8°',207:'I, 9°',411:'I, 9°',170:'I, 9°'})
for i in (70,95,99,127,143,151,152,153,154,155,156,178,194,284,365): AL[i]='I, 1°'
AL[195]='I, 2°'

def alinea_label(v):
    ch = v.get('chapeau', '') or ''
    m = re.match(r'\**([IVX]+)\.\**\s*[–-]\s*(?:([A-Z])\.\s*[–-])?', ch)
    lab = ''
    if m:
        lab = m.group(1) + (', ' + m.group(2) if m.group(2) else '')
    m2 = re.match(r'\**([IVX]+)\.', v['alinea'].strip())
    m3 = re.match(r'(\d+°)', v['alinea'].strip())
    if m3:
        lab = (lab + ', ' if lab else '') + m3.group(1)
    elif m2 and not lab:
        lab = m2.group(1)
    return lab


def legiarti(code, art):
    try:
        x = droit.article(code, art, jour='2027-07-01')
        return x['id']
    except Exception:
        return ''


def lien(lid, code):
    if not lid:
        return ''
    kind = 'loda' if str(code).startswith('loi') else 'codes'
    return f'https://www.legifrance.gouv.fr/{kind}/article_lc/{lid}'


# ---------------------------------------------------------------- lignes de l'article 42 (numéros distinctifs seulement)
A42 = json.load(open(W + 'art42.json'))
def lignes42(i):
    ss = [a for c, a in sieges(i) if a and (re.search(r'[a-z]', a.lstrip('lrdo')) or '-' in a or len(a) >= 4)]
    out = []
    for k, bl in A42.items():
        arts = set(n_(t) for b in bl for t in re.findall(r'(?:L\.\s?|R\.\s?)?\d+(?:-\d+)*(?: (?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|[A-Z]{1,3}))*', b['brut']))
        if any(a in arts for a in ss):
            out.append(int(k))
    return sorted(out)

# ---------------------------------------------------------------- niches rattachées (par impôt)
NICH = json.load(open(W + 'niches.json'))
nmap = collections.defaultdict(list)
CATR = {'Impôt sur le revenu': [130], 'Impôt sur les sociétés': [142], 'Impôt sur le revenu et impôt sur les sociétés': [130, 142],
        'Taxe sur la valeur ajoutée': [193], 'Accise sur les énergies': [211]}
for x in NICH:
    for r in CATR.get(x['cat'], []):
        nmap[r].append(x['numero'])

# ---------------------------------------------------------------- rangs
rows = []
for i, (s, f) in enumerate(zip(S, F), 1):
    if i in RETIRES:
        continue
    nat = NATURE[s['nature']]
    ass = ASS[s['assiette'][0]] if s['assiette'] else ''
    rel = REL[i]
    # rendement au millésime en vigueur (prévision 2026 initiale) ; cinq écarts de source corrigés à l'état A LFI 2026
    rdt = s['rendement_2026_M']; src = 'tri du 20261015 (prévision 2026 du PLF 2026 ou liste IFRAP)'
    if i in (132, 144, 158, 196, 407):
        rdt = str(rel['etatA_lfi26']); src = 'état A, évaluation initiale 2026 (LFI 2026) — écart de source corrigé'
    elif rel['source'] == 'ressources affectées' and rel['plf26'] is not None:
        src = 'PLF 2026, annexe des taxes affectées, prévision 2026'
    elif rel['source'] == 'état A':
        src = 'état A, évaluation initiale 2026' if rel['verdict'].startswith('concordant') else src
    elif rel['source'] == 'aucune annexe':
        src = 'liste IFRAP (aucune ligne d’annexe ni d’état A)' if F[i-1]['origine'].startswith('ifrap') or F[i-1]['origine'] == '' else src
    alt = rel['plf27_rev26'] if rel['plf27_rev26'] is not None else rel['etatA_rev26']
    # devenir
    sort = s['sort']; bloc = ''; cible = ''
    if i in GRANDS:
        dev = 'grand impôt conservé'; cible = NOM[GRANDS[i]]
    elif i in CONSERVE_BLOC:
        dev = 'conservé en complément'; bloc = CONSERVE_BLOC[i]
    elif sort == 'hors champ':
        dev = 'recette non fiscale'
    elif i in (293, 295) or (sort == 'fondu dans l’équilibre' and s['nature'] != 'cotisation sociale'):
        dev = 'fondu dans l’équilibre des quatre grands impôts'
    elif sort == 'fondu dans l’équilibre' and s['nature'] == 'cotisation sociale':
        dev = 'à fusionner'
    elif sort == 'fondu par rattachement':
        dev = 'remplacé par un grand impôt'
        c = A_CIBLE.get(i) or VENT.get(i) or ABS.get(s['impot_absorbant'], '')
        if c == 'EQ':
            dev = 'fondu dans l’équilibre des quatre grands impôts'; c = ''
        cible = NOM.get(c, '')
    elif sort == 'maintenu à part':
        dev = 'conservé en complément'; bloc = BLOC.get(i, 'à qualifier')
    else:
        dev = sort
    # siège
    sg = s['siege_article']; code = F[i-1]['siege_code']; lid = F[i-1]['legiarti']
    if i in SIEGE_CORR:
        sg, c2, a2 = SIEGE_CORR[i]; lid = legiarti(c2, a2) or lid; code = c2
    # porteur
    vd = VD.get(i); h = H120.get(i)
    porteur = alin = verdict = prov = ''
    if dev in ('à fusionner', 'grand impôt conservé', 'conservé en complément', 'recette non fiscale'):
        verdict = 'sans objet (devenir sans abrogation)'
    elif vd:
        verdict, porteur, alin, prov = vd[1], vd[2], vd[3], vd[5]
    elif h and h['verdict'] == 'A':
        verdict, porteur, prov = 'A', h['porteur'], 'relevé (mécanique)'
        vv = [v for v in VIS_NC.get(n_(h['article']), []) if f"{v['liasse']} n° {v['n']}" == h['porteur']]
        alin = alinea_label(vv[0]) if vv else ''
    elif h:
        verdict, prov = 'C', 'relevé'
    # corrections de la passe hors liste (lecture sur pièce)
    FIX = {84: ('A', 'PLFSS n° 1', 'V, 1°', 'relevé'), 85: ('A', 'PLFSS n° 1', 'VI', 'relevé'),
           99: ('C', '', '', 'relevé'), 102: ('A', 'PLF P1 n° 25', 'I, 8°', 'relevé'), 111: ('A', 'PLF P1 n° 25', 'I, 2°', 'relevé'),
           124: ('A', 'PLF P1 n° 25', 'I, 8°', 'relevé'), 158: ('A', 'PLF P1 n° 1', 'III, 266°', 'relevé'),
           181: ('A', 'PLF P1 n° 25', 'II, B, 1°', 'relevé'), 182: ('A', 'PLF P1 n° 22', 'II, 1°', 'relevé'),
           239: ('A', 'PLF P1 n° 25', 'I, 1°', 'relevé'), 280: ('C', '', '', 'relevé'), 325: ('A', 'PLF P1 n° 20', 'I, 9°', 'relevé'),
           331: ('A', 'PLF P1 n° 19', 'I, 9°', 'relevé'), 334: ('A', 'PLF P1 n° 1', 'III, 232°', 'relevé'),
           336: ('A', 'PLF P1 n° 19', 'I, 8°', 'relevé'), 344: ('A', 'PLF P1 n° 22', 'I, 1°', 'relevé'),
           306: ('C', '', '', 'relevé'), 362: ('C', '', '', 'relevé'), 370: ('C', '', '', 'relevé'), 383: ('C', '', '', 'relevé')}
    if i in FIX and verdict not in ('sans objet (devenir sans abrogation)',):
        verdict, porteur, alin, prov = FIX[i]
    for k in (87, 88, 89, 90, 91, 92, 93):
        if i == k: verdict, porteur, alin, prov = 'B', 'PLF P1 n° 20', 'I, 11° et 12°', 'relevé'
    nouveau = NOUV.get(i, '')
    if verdict == 'C' and nouveau:
        porteur_final = nouveau; alin_final = ALIN_NOUV.get(int(nouveau.split('n° ')[1])) or AL.get(i, 'I'); etat = 'C → porté par un amendement nouveau (projet)'
    else:
        porteur_final, alin_final = porteur, alin
        etat = {'A': 'porté', 'B': 'porté par une clause', 'S': 'sans objet : déjà abrogé', 'C': 'non porté'}.get(verdict, verdict)
    if verdict == 'C' and i in REGL:
        porteur_final, alin_final, etat = 'voie réglementaire (décret)', '', 'porté par la voie réglementaire (hors liasse)'
    rows.append(dict(n=i, libelle=s['libelle'], nature=nat, assiette=ass, rendement_2026_M=rdt, source_rendement=src,
                     rendement_2026_revise_plf2027_M='' if alt is None else alt, devenir=dev, impot_cible=cible, bloc=bloc,
                     siege=sg, legiarti=lid, lien_legifrance=lien(lid, code), niches_rattachees=len(nmap.get(i, [])) or '',
                     amendement_porteur=porteur_final, alinea=alin_final, verdict=verdict, etat_porteur=etat, provenance=prov,
                     ligne_art42=', '.join(str(x) for x in lignes42(i)), carte='—',
                     question=(vd[6] == 'Q' and vd[7]) if vd else '', observation=(vd[7] if vd else '') or s['observation'],
                     nature_ligne=s['nature_ligne'], siege_article=s['siege_article'], statut_siege=s['statut_siege'], fondement=s['fondement']))

# rangs ajoutés (annexe C et contrôle inverse) — relevés au dépôt de droit ou à l'annexe 2027
NEW = [
 ('Taxe forfaitaire sur la cession à titre onéreux de terrains devenus constructibles', 'impôt', 'la propriété et les droits d’usage', '15.0', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'remplacé par un grand impôt', 'Taxe foncière', '', 'Art. 1529 du code général des impôts', ('cgi', '1529'), 'PLF P1 n° 29', 'III', 'A', 'relevé'),
 ('Taxe sur la vacance des locaux d’habitation', 'impôt', 'la propriété et les droits d’usage', '', 'rendement non publié aux annexes', 'remplacé par un grand impôt', 'Taxe foncière', '', 'Art. 1406 bis du code général des impôts', ('cgi', '1406 bis'), 'PLF P1 n° 29', 'III', 'A', 'relevé'),
 ('Contribution spéciale CDG Express, majoration de la taxe sur le transport aérien de passagers', 'impôt', 'la consommation', '0.0', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'remplacé par un grand impôt', 'Taxe sur la valeur ajoutée', '', 'L. 422-26-1 du code des impositions sur les biens et services', ('cibs', 'L. 422-26-1'), 'PLF P1 n° 26', 'V, 2', 'A', 'relevé'),
 ('Contribution pour l’aide juridique en appel', 'impôt', 'la propriété et les droits d’usage', '', 'création du PLF 2027 (art. 27) ; 17,2 M€ prévus en 2027 à l’art. 42, ligne 140', 'remplacé par un grand impôt', 'Impôt sur le revenu', '', 'Art. 1635 bis P du code général des impôts, rédaction de l’art. 27 du PLF 2027', ('cgi', '1635 bis P'), 'PLF P1 n° 25', 'I, 2°', 'A', 'déduit'),
 ('Contribution pour la justice économique', 'impôt', 'la propriété et les droits d’usage', '', 'création du PLF 2027 (art. 27)', 'remplacé par un grand impôt', 'Impôt sur les sociétés', '', 'Art. 27 du PLF 2027 (création)', None, '', '', 'C', 'relevé'),
 ('Contribution sur les publicités et actions promotionnelles des opérateurs de jeux et paris', 'contribution sociale', 'la consommation', '175.0', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'remplacé par un grand impôt', 'Taxe sur la valeur ajoutée', '', 'L. 137-27 du code de la sécurité sociale', ('css', 'L. 137-27'), 'PLFSS n° 9', 'I, 1°', 'C', 'relevé'),
 ('Contribution à la prise en charge des modes de rémunération des médecins (13° de l’art. L. 162-5 CSS)', 'contribution sociale', 'la consommation', '434.0', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'remplacé par un grand impôt', 'Taxe sur la valeur ajoutée', '', 'L. 862-4-1 du code de la sécurité sociale', ('css', 'L. 862-4-1'), 'PLFSS n° 9', 'I, 1°', 'C', 'relevé'),
 ('Taxe spéciale complémentaire au profit de la Société du Grand Projet du Sud-Ouest', 'impôt', 'la propriété et les droits d’usage', '22.2', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'remplacé par un grand impôt', 'Taxe foncière', '', 'Art. 1609 I du code général des impôts', ('cgi', '1609 I'), 'PLF P1 n° 37', 'I, 1°', 'C', 'relevé'),
 ('Contribution exceptionnelle sur le résultat d’exploitation des grandes entreprises de transport maritime', 'impôt', 'l’activité des entreprises', '0.0', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'remplacé par un grand impôt', 'Impôt sur les sociétés', '', 'Art. 50 de la loi n° 2025-127 du 14 février 2025', ('loi n° 2025-127 du 14 février 2025', '50'), '', '', 'S', 'relevé'),
 ('Majoration de prélèvement au titre de la loi Solidarité et renouvellement urbains', 'recette non fiscale', '', '50.0', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'recette non fiscale', '', '', 'L. 302-9-1 du code de la construction et de l’habitation', ('cch', 'L. 302-9-1'), '', '', 'sans objet (devenir sans abrogation)', 'déduit'),
 ('Droits de port (redevances d’équipement, de stationnement, sur les navires, les marchandises et les passagers)', 'impôt', 'la propriété et les droits d’usage', '495.2', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'remplacé par un grand impôt', 'Impôt sur les sociétés', '', 'L. 5321-1 à L. 5321-4 du code des transports', ('transports', 'L. 5321-1'), 'voie réglementaire (décret)', '', 'C', 'déduit'),
 ('Redevance domaniale due par les sociétés concessionnaires d’autoroutes', 'impôt', 'la propriété et les droits d’usage', '440.8', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'remplacé par un grand impôt', 'Impôt sur les sociétés', '', 'R. 122-48 du code de la voirie routière', None, 'voie réglementaire (décret)', '', 'C', 'déduit'),
 ('Redevance d’exploitation de substances non énergétiques sur le plateau continental ou dans la zone économique exclusive', 'impôt', 'la propriété et les droits d’usage', '0.3', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'remplacé par un grand impôt', 'Impôt sur les sociétés', '', 'L. 132-15-1 du code minier', None, 'voie réglementaire (décret)', '', 'C', 'déduit'),
 ('Taxe de protection des obtentions végétales', 'impôt', 'la propriété et les droits d’usage', '0.0', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'remplacé par un grand impôt', 'Impôt sur les sociétés', '', 'L. 623-16 du code de la propriété intellectuelle', None, '', '', 'C', 'relevé'),
 ('Contribution aux frais de garderie et d’administration des bois et forêts des collectivités', 'recette non fiscale', '', '28.0', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'recette non fiscale', '', '', 'L. 224-3 du code forestier', None, '', '', 'sans objet (devenir sans abrogation)', 'déduit'),
 ('Contribution additionnelle des collectivités propriétaires de bois et forêts relevant du régime forestier', 'recette non fiscale', '', '5.0', 'PLF 2027, annexe des ressources affectées, prévision 2026 révisée', 'recette non fiscale', '', '', 'L. 224-4 du code forestier', None, '', '', 'sans objet (devenir sans abrogation)', 'déduit'),
]
for k, t in enumerate(NEW, 1):
    lib, nat, ass, rdt, src, dev, cible, bloc, sg, ref, por, ali, ver, prov = t
    lid = legiarti(*ref) if ref else ''
    etat = {'A': 'porté', 'C': ('porté par la voie réglementaire (hors liasse)' if por.startswith('voie') else 'C → porté par un amendement nouveau (projet)') if por else 'non porté', 'S': 'sans objet : déjà abrogé'}.get(ver, ver)
    rows.append(dict(n=f'N{k}', libelle=lib, nature=nat, assiette=ass, rendement_2026_M=rdt, source_rendement=src,
                     rendement_2026_revise_plf2027_M=rdt if 'révisée' in src else '', devenir=dev, impot_cible=cible, bloc=bloc,
                     siege=sg, legiarti=lid, lien_legifrance=lien(lid, ref[0] if ref else ''), niches_rattachees='',
                     amendement_porteur=por, alinea=ali, verdict=ver, etat_porteur=etat, provenance=prov, ligne_art42='', carte='—',
                     question='qualification proposée : recette non fiscale' if nat == 'recette non fiscale' else '',
                     observation='rang ajouté le 20261103 (annexe des ressources affectées 2027 ou contrôle inverse)', nature_ligne='imposition' if nat != 'recette non fiscale' else 'recette non fiscale',
                     siege_article=sg, statut_siege=('confirmé' if lid else ('création du PLF' if 'PLF 2027' in sg else 'siège déclaré, texte hors dépôt')), fondement='annexe des ressources affectées 2027'))

COLS = list(rows[0].keys())
import os
os.makedirs(OUT, exist_ok=True)
with open(R + 'sort_prelevements_20261103.tsv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=COLS, delimiter='\t'); w.writeheader(); w.writerows(rows)
json.dump(rows, open(W + 'tri_20261103.json', 'w'), ensure_ascii=False, indent=0)
c = collections.Counter(r['devenir'] for r in rows); print(len(rows), c)
print(collections.Counter(r['etat_porteur'] for r in rows))
print(collections.Counter(r['nature'] for r in rows)); print(collections.Counter(r['assiette'] for r in rows))
print('à qualifier', [r['n'] for r in rows if r['bloc'] == 'à qualifier' or (r['devenir'] == 'remplacé par un grand impôt' and not r['impot_cible'])])
