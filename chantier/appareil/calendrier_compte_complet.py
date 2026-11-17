#!/usr/bin/env python3
"""Le compte complet du calendrier des flux, 2027 à 2030 — construit le 20261117.

Règles de l'auteure (20261116) : les agents sont tous privés ; « le solde public
est l'inverse de la somme des privés » ; « tout doit se compenser ».

Le croisé `referentiels/calendrier_mesures_mois_20261116.tsv` ne porte que les
27 lignes de dépenses du § 4 du registre de calcul. Ce module y ajoute tout le
reste, relevé sur pièces :

  circuit A, la restitution (les 236,4 Md€ du classeur) :
    - les 27 coupes (croisé du 20261116, inchangé) ;
    - les 8 lignes « de première partie et sociale » (8,30 Md€, § 4) ;
    - les niches fiscales et sociales, part gagée sur la baisse de CSG
      (43,126 + 9 = 52,1 Md€ par an), niche par niche, à la date que lui
      donne le IV de l'amendement n° 1 de la liasse P1 ou le IV de
      l'amendement n° 1 de la liasse PLFSS ;
    - la baisse de CSG (§ 2) ;
    - l'assurance chômage transformée, le rendement du patrimoine rendu ;
    - l'épargne rendue, calculée : le surplus cumulé qui ne sera plus repris.
  circuit B, la refonte « à rendement constant » — seules lignes que le
  registre date et chiffre (§ 17 et § 18) : solde des niches, taux réduits de
  TVA, taxe sur les salaires, suppressions d'impôts du tri. Ses contreparties
  (taux unique de l'impôt sur les sociétés, taxe foncière unique) ne sont
  datées et chiffrées par aucune pièce : le circuit B ne se ferme pas ici, et
  le module le dit.

Signe : montant positif = le solde public s'améliore = un agent privé paie ou
perd. En mesure, en Md€, hors règle de CP résiduel.

  construire   écrit les deux TSV de `referentiels/`
  controler    rejoue les TSV contre les pièces ; code 1 au premier échec
  etat         imprime les tableaux de l'état (par agent, par an, par mois)
  leviers      rejoue les leviers de date du § 17 sur le compte complet
"""
import csv, re, sys
from collections import OrderedDict, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import calendrier_mesures_mois as cm

RACINE = cm.RACINE
PARAM = RACINE / 'referentiels/compte_complet_parametres_20261117.tsv'
TSV = RACINE / 'referentiels/calendrier_compte_complet_20261117.tsv'
TSV_NICHES = RACINE / 'referentiels/calendrier_compte_complet_niches_20261117.tsv'
NICHES_XLS = RACINE / 'sources/projet_20261116/14_PLF2026_VM_tome_II_Annexe_3_Depenses_fiscales_0910.xls'
LIASSE_P1 = RACINE / 'livrables/depot_2027/LIASSE_PLF_P1.md'
LIASSE_SS = RACINE / 'livrables/depot_2027/LIASSE_PLFSS.md'
COLS = cm.COLS_MOIS
ANNEES = cm.ANNEES

MAT = 'Ménages actifs — transferts monétaires'
MSN = cm.MSN
MAE = 'Ménages actifs — épargne'
MSR = "Ménages sans revenus d'activité"
MNR = 'Ménages, non répartis'
AGP, ENT = cm.AGP, cm.ENT
ASS = 'Associations'
AGENTS = [MAT, MSN, MAE, MSR, MNR, AGP, ENT, ASS]


def params():
    return {d['cle']: float(d['valeur']) for d in csv.DictReader(open(PARAM, encoding='utf-8'), delimiter='\t')}


# ---------------------------------------------------------------- calendriers
def paliers(*marches):
    """marches : (indice de mois, rythme annuel). Un douzième du rythme par mois
    entre deux marches (règle du § 16 du registre)."""
    v, rythme = [0.0] * 48, 0.0
    m = dict(marches)
    for i in range(48):
        rythme = m.get(i, rythme)
        v[i] = rythme / 12
    return v


def annee(a):
    return (a - 2027) * 12


def rentree(a, part=1.0):
    """Un montant annuel perçu de septembre à décembre de l'année a (solde de
    l'impôt sur le revenu, rôles d'automne), puis par douzièmes."""
    v = [0.0] * 48
    for i in range(annee(a) + 8, annee(a) + 12):
        v[i] = part / 4
    return v


def suite(v, a, part=1.0):
    for i in range(annee(a), 48):
        v[i] = part / 12
    return v


# Fractions du montant annuel, mois par mois, selon l'impôt et la division du IV
# de l'amendement n° 1 (liasse P1). La date d'application est relevée ; le mois
# d'incidence est déduit du mode de perception (voir la note de lecture).
def fractions(impot, div, retenue):
    if impot == 'IR':
        if div == 'A':       # impôt dû au titre de 2026 : soldé à l'automne 2027
            return suite(rentree(2027), 2028), '2027-09', 'IV, A : impôt sur le revenu dû au titre de 2026'
        if div == 'B':       # dépenses et investissements de 2027 : impôt liquidé en 2028
            return suite(rentree(2028), 2029), '2028-09', 'IV, B : dépenses, investissements et versements à compter du 1er janvier 2027'
        if div == 'C' and retenue:   # salaires et produits d'épargne : retenus à la source dès 2028
            return suite([0.0] * 48, 2028), '2028-01', 'IV, C : revenus et opérations à compter du 1er janvier 2028, retenus à la source'
        if div == 'C':       # barème, parts, décote : impôt dû au titre de 2028, soldé en 2029
            return suite(rentree(2029), 2030), '2029-09', 'IV, C : impôt sur le revenu dû au titre de 2028'
        if div == 'C82':     # cessions à compter du 1er janvier 2027
            return suite([0.0] * 48, 2027), '2027-01', 'IV, C, dernière phrase : cessions à compter du 1er janvier 2027'
        if div == 'E':       # un tiers au titre de 2027, deux tiers au titre de 2028, tout au titre de 2029
            v = rentree(2028, 1 / 3)
            for i in range(annee(2029), annee(2030)):
                v[i] = 2 / 3 / 12
            return suite(v, 2030), '2028-09', 'IV, E : un tiers au titre de 2027, deux tiers au titre de 2028, en totalité au titre de 2029'
        if div == 'F':       # dons : moitié à compter du 1er juillet 2027, tout au 1er janvier 2028
            return suite(rentree(2028, 1 / 4), 2029), '2028-09', 'IV, F : moitié pour les dons à compter du 1er juillet 2027, en totalité au 1er janvier 2028'
    if impot == 'IS':
        if div in ('A', 'B'):
            return suite([0.0] * 48, 2027), '2027-01', ('IV, A : exercices clos à compter du 1er janvier 2027' if div == 'A' else
                                                        'IV, B : dépenses et investissements à compter du 1er janvier 2027')
        if div == 'C':
            return suite([0.0] * 48, 2028), '2028-01', 'IV, C : opérations à compter du 1er janvier 2028'
        if div == 'E':
            return paliers((0, 1 / 3), (12, 2 / 3), (24, 1.0)), '2027-01', 'IV, E : un tiers au titre de 2027, deux tiers au titre de 2028, en totalité en 2029'
        if div == 'F':
            return paliers((6, 0.5), (12, 1.0)), '2027-07', 'IV, F : moitié pour les dons à compter du 1er juillet 2027, en totalité au 1er janvier 2028'
    if impot == 'INDIRECT':
        if div == 'E':
            return paliers((0, 1 / 3), (12, 2 / 3), (24, 1.0)), '2027-01', 'IV, E : un tiers au titre de 2027, deux tiers au titre de 2028, en totalité en 2029'
        return paliers((6, 1.0)), '2027-07', 'IV, D : fait générateur à compter du 1er juillet 2027'
    if impot == 'ENREG':
        return paliers((0, 1.0)), '2027-01', 'IV, A et C bis : actes, mutations, successions et donations à compter du 1er janvier 2027'
    if impot == 'LOCAL':
        return suite(rentree(2027), 2028), '2027-09', 'IV, A : impôt sur la fortune immobilière et impositions directes locales dus au titre de 2027'
    raise ValueError((impot, div))


# ------------------------------------------------- le III et le IV de la pièce
ORD = ('bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies|terdecies|quaterdecies|'
       'quindecies|sexdecies|septdecies|octodecies|novodecies|vicies')
ART = r'\d{1,4}(?:-0)?(?: (?:%s))?(?:-0)?(?: [A-Z]{1,3}(?![a-zé]))?(?: (?:%s))?(?: [A-Z](?![a-zé]))?' % (ORD, ORD)
SUB = r'(?:\d+°?|[a-z]|[IVX]+)(?: (?:%s))?' % ORD


def _plage(s):
    out = set()
    for a in re.split(r',| et ', s):
        a = a.replace('°', '').strip()
        m = re.match(r'(\d+) à (\d+)$', a)
        if m:
            out |= set(range(int(m[1]), int(m[2]) + 1))
        elif a:
            out.add(int(a))
    return out


def lire_amendement_1():
    """Rend les items du III (n° → texte) et les listes d'items que le IV range
    à ses B, C, C bis, E et F — lues au texte, non recopiées."""
    L = open(LIASSE_P1, encoding='utf-8').read().split('\n')
    a = next(i for i, l in enumerate(L) if l.startswith('**III.** – Sont abrogés'))
    b = next(i for i, l in enumerate(L) if l.startswith('**III bis.**'))
    items = OrderedDict()
    for l in L[a:b]:
        m = re.match(r'(\d+)° (.*)', l)
        if m:
            items[int(m[1])] = m[2]
    div = {}
    for lettre in ('B', 'C', 'C bis', 'E', 'F'):
        l = next(x for x in L[b:] if x.startswith(f'**{lettre}.**'))
        m = re.search(r'celles que le III abroge à ses (.*?), (?:le I s’applique|l’avantage est réduit)', l)
        div[lettre] = _plage(m[1])
    c82 = _plage(re.search(r'pour les dispositions que le III abroge à ses (.*?), le I s’applique aux cessions',
                           next(x for x in L[b:] if x.startswith('**C.**')))[1])
    div['C82'] = c82
    div['C'] -= c82
    dates = {k: next(x for x in L[b:] if x.startswith(f'**{k}.**') or x.startswith(f'**IV. – {k}.**'))
             for k in ('A', 'B', 'C', 'C bis', 'D', 'E', 'F')}
    return items, div, dates


def _norm(t):
    return t.replace('°', '').strip()


def clauses(texte):
    """« Le a du 5 de l’article 158 » → [('158', [{'5'}, {'a'}])] ; « L’article 81 ter » → [('81 ter', [])]."""
    out = []
    t = texte.replace('\xa0', ' ').replace("'", '’')
    t = re.sub(r'loi n° [\d-]+ du \d+\w* \w+ \d+', '', t)
    # sous-parties suivies de « de l’article X »
    for m in re.finditer(r'((?:%s)(?:(?:, | et | à )(?:%s))*(?: du (?:%s))*) de l’article (%s)' % (SUB, SUB, SUB, ART), t):
        niveaux = [set(_norm(x) for x in re.split(r', | et | à ', n)) for n in m[1].split(' du ')]
        out.append((m[2].strip(), list(reversed(niveaux))))
    # articles entiers
    for m in re.finditer(r'(?:^|[,;] | et |[Ll]’|[Ll]es )articles? ((?:%s)(?:(?:, | et | à )(?:%s))*)' % (ART, ART), t):
        avant = t[max(0, m.start() - 4):m.start() + 3]
        if ' de l’' in t[max(0, m.start() - 6):m.start() + 4] or avant.strip().startswith('de'):
            continue
        for x in re.split(r', | et | à ', m[1]):
            out.append((x.strip(), []))
    return out


def reference(ref):
    """« 81-18°-a, 157-16° bis » → [('81', ['18', 'a']), ('157', ['16 bis'])]."""
    out = []
    for tok in re.split(r',| et |;', ref.replace('\xa0', ' ')):
        tok = tok.strip().lstrip('# ')
        m = re.match(r'(%s)(.*)' % ART, tok)
        if m and m[1]:
            out.append((m[1].strip(), [_norm(x) for x in m[2].split('-') if _norm(x)]))
    return out


def division_par_article(ref, items, div):
    """Les items du III qui abrogent la référence, du plus précis au moins précis."""
    precis, entier = set(), set()
    R = reference(ref)
    for n, texte in items.items():
        for art, niveaux in clauses(texte):
            for a, chemin in R:
                if a != art:
                    continue
                if not niveaux:
                    entier.add(n)
                elif chemin and all(chemin[i] in niveaux[i] for i in range(min(len(chemin), len(niveaux)))):
                    precis.add(n)
    cand = precis or entier

    def d(n):
        return next((k for k, s in div.items() if n in s), 'A')
    return sorted(cand), sorted(set(d(n) for n in cand))


MOTS = (('F', ('dons', 'mécénat')),
        ('E', ('agricol', 'exploitant', 'à domicile', 'garde des enfants', 'jeunes enfants', 'services à la personne', 'forêt', 'forestier')),
        ('C', ('livret', 'épargne', 'plus-value', 'assurance-vie', 'capitalisation', 'demi-part', 'quotient', 'décote')))


def division_par_nature(lib, P, Q):
    l = lib.lower()
    for d, mots in MOTS:
        if any(m in l for m in mots):
            return d
    if P == 'E':
        return 'C'
    if Q in ('RI', 'CI', 'Déd'):
        return 'B'
    return 'A'


IMPOT = {'Impôt sur le revenu': 'IR', 'Autres impôts directs': 'LOCAL', 'Impôts locaux': 'LOCAL',
         'Impôt sur le revenu et impôt sur les sociétés': 'IS', 'Impôt sur les sociétés': 'IS',
         'Taxe sur la valeur ajoutée': 'INDIRECT', 'Accise sur les énergies': 'INDIRECT', 'Autres droits': 'INDIRECT',
         "Droits d'enregistrement et de timbre": 'ENREG'}
FAMILLE = {'Impôt sur le revenu': 'revenus', 'Autres impôts directs': 'revenus',
           'Impôt sur le revenu et impôt sur les sociétés': 'sociétés', 'Impôt sur les sociétés': 'sociétés',
           'Taxe sur la valeur ajoutée': 'TVA', 'Accise sur les énergies': 'énergie et autres',
           'Autres droits': 'énergie et autres', 'Impôts locaux': 'énergie et autres',
           "Droits d'enregistrement et de timbre": 'énergie et autres'}
# Agent qui paie, d'après l'onglet « Bénéficiaires ». « Véhicules » : ménages
# (`Détail Niches`!L21, malus) ; « Locaux » et « Parcelles » : moitié ménages, moitié entreprises.
PAYEUR = {'Entreprises': [(ENT, 1.0)], 'Ménages': [(MNR, 1.0)], 'Entreprises et ménages': [(ENT, 0.5), (MNR, 0.5)],
          'Véhicules': [(MNR, 1.0)], 'Locaux': [(MNR, 0.5), (ENT, 0.5)], 'Parcelles': [(MNR, 0.5), (ENT, 0.5)]}


def lire_niches():
    import xlrd
    w = xlrd.open_workbook(NICHES_XLS)
    s, bs, rj = (w.sheet_by_name(n) for n in ('Chiffrages Résolution', 'Bénéficiaires', 'Références juridiques'))

    def table(sh, col):
        t = {}
        for r in range(2, sh.nrows):
            try:
                t[int(sh.cell_value(r, 3))] = tuple(str(sh.cell_value(r, c)).replace('\xa0', ' ') for c in col)
            except ValueError:
                pass
        return t
    ben, ref = table(bs, (5,)), table(rj, (6, 7))
    items, div, _ = lire_amendement_1()
    out = []
    for r in range(6, s.nrows):
        v = [s.cell_value(r, c) for c in range(s.ncols)]
        try:
            n = int(v[3])
        except ValueError:
            continue
        gage = v[13] / 1000 if isinstance(v[13], float) else 0.0
        solde = v[14] / 1000 if isinstance(v[14], float) else 0.0
        if not gage and not solde:
            continue
        cat, lib, P, Q = v[0], v[4].replace('\xa0', ' '), v[15], v[16]
        code, rf = ref.get(n, ('', ''))
        impot = IMPOT[cat]
        cand, divs, mode = [], [], ''
        if impot in ('IR', 'IS') and 'général des impôts' in code:
            cand, divs = division_par_article(rf, items, div)
        if len(divs) == 1:
            d, mode = divs[0], 'III, ' + ', '.join(f'{x}°' for x in cand)
        elif impot in ('IR', 'IS'):
            d = division_par_nature(lib, P, Q)
            mode = 'nature de l’avantage' + (f" (III ambigu : {', '.join(f'{x}°' for x in cand)})" if cand else '')
        elif impot == 'INDIRECT':
            d = 'E' if (cat != 'Taxe sur la valeur ajoutée' and any(m in lib.lower() for m in ('agricol', 'forest'))
                        and 'autres que' not in lib.lower()) else 'D'
            mode = 'impôt (IV, D)' if d == 'D' else 'nature de l’avantage'
        else:
            d, mode = 'A', 'impôt (IV, A)'
        if d == 'C bis':
            d = 'A'
        if d in ('C82',) and impot != 'IR':
            d = 'A'
        retenue = P in ('S', 'E')
        fr, premier, regle = fractions(impot, d, retenue)
        b = ben.get(n, ('',))[0]
        payeur = PAYEUR[b]
        if n == 120401:      # abattement de 10 % sur les pensions : `Détail Niches`!N10, retraités
            payeur = [(MSR, 1.0)]
        elif P == 'S':       # exonérations salariales : `Détail Niches`!M9, actifs
            payeur = [(MAT, 1.0)]
        out.append(dict(numero=n, categorie=cat, famille=FAMILLE[cat], libelle=lib, reference=rf, beneficiaire=b,
                        payeur=payeur, gage=gage, solde=solde, division=d, mode=mode, premier=premier, regle=regle,
                        fr=fr, type=Q, marque=P))
    return out


# ----------------------------------------------------------------- le registre
def lire_s17_s18():
    t17 = cm.lire_tableau('## 17. TVA', '**Leviers chiffrés')
    t18 = {}
    for i, l in cm.section('## 18. Refonte', '## 13.'):
        if l.startswith('| 2027, en mesure'):     # le second tableau, mensuel, ne se relit pas ici
            break
        if l.startswith('| P1 n°') or l.startswith('| ajouts') or l.startswith('| PLFSS'):
            c = cm._c(l)
            t18[c[0]] = [cm._n(x) for x in c[2:5]]
    return t17, t18


# ------------------------------------------------------------------- les lignes
def ligne(id_, circuit, nature, famille, mesure, agents, v, date, regle, piece, statut):
    return dict(id=id_, circuit=circuit, nature=nature, famille=famille, mesure=mesure, agents=agents, v=v,
                date=date, regle=regle, piece=piece, statut=statut)


def lignes_hors_epargne():
    P = params()
    L = []
    # 1. les 27 coupes, du croisé du 20261116
    _, cle = cm.lire_flux()
    for d in cm.lire():
        cel = d['cellule']
        parts = cm.CLE_PRIVEE.get(cel, cle[cel])
        parts = [(MAT if 'transferts' in a else a, p) for a, p in parts]
        L.append(ligne(cel, 'A', 'dépense', d['pan'], d['ligne_doctrinale'], parts, [float(d[c]) for c in COLS],
                       d['date_effet_2027'], f"rythme {d['rythme']}, marche au {d['marche_annuelle']}",
                       'referentiels/calendrier_mesures_mois_20261116.tsv ; ' + d['adresse_registre'],
                       'relevé (montants, dates) ; mensualisation déduite ; agent : clé posée'))
    # 2. les 8 lignes de première partie et sociale (§ 4 : 8,30 Md€ en régime plein)
    tiers = lambda F: paliers((0, F / 3), (12, 2 * F / 3), (24, F))
    plein = lambda F: paliers((0, F))
    huit = [
        ('D7', 'CNC et subventions culturelles', plein, [(ENT, 1.0)], 'rythme 1'),
        ('D8', 'Agences de l’eau', tiers, [(MSN, 0.5), (ENT, 0.5)], 'rythme ⅓ (G8 : sortie en 3 ans)'),
        ('D9', 'AFITF', plein, [(ENT, 1.0)], 'rythme 1'),
        ('D10', 'Action Logement', tiers, [(MSN, 1.0)], 'rythme ⅓ (G10 : sortie en 3 ans)'),
        ('D11', 'CCI et chambres d’agriculture', plein, [(ENT, 1.0)], 'rythme 1'),
        ('D13', 'Établissements publics fonciers', plein, [(MSN, 0.5), (ENT, 0.5)], 'rythme 1'),
        ('D14', 'Agence nationale de l’habitat', lambda F: paliers((0, F / 2), (12, F)), [(MSN, 1.0)],
         'moitié la première année (D14 = 0,2 sur F14 = 0,4)'),
    ]
    for cel, nom, f, parts, r in huit:
        L.append(ligne(cel, 'A', 'dépense, première partie', 'Opérateurs', nom, parts, f(P[cel + '_F']), '1er janv. 2027',
                       r + ', un douzième par mois', f'Synthèse des chiffrages.xlsx, Détail Economies, ligne {cel[1:]} ; registre § 4',
                       'montant et rythme relevés ; date tranchée en propre (R-P : personne morale, 1er janvier) — le registre ne date pas la ligne ; agent : clé posée'))
    F = P['D21_F']
    L.append(ligne('D21', 'A', 'dépense, jambe sociale', 'Chèques', 'Exonérations emploi à domicile', [(MAT, 1.0)],
                   paliers((6, F / 3), (12, 2 * F / 3), (24, F)), '1er juil. 2027',
                   'un tiers au 1er juillet 2027, deux tiers au 1er janvier 2028, en totalité au 1er janvier 2029',
                   'LIASSE_PLFSS.md, amendement n° 1, IV, second alinéa (L. 241-10 CSS) ; Détail Economies, ligne 21',
                   'montant et dates relevés ; agent relevé (R21, tous ménages)'))
    # 3. la baisse de CSG (§ 2)
    rest = cm.restitution()
    L.append(ligne('CSG', 'A', 'restitution', 'salaire net', 'Baisse de CSG et de CRDS sur les revenus d’activité',
                   [(MAT, 0.9), (AGP, 0.1)], [-x for x in rest], '1er juil. 2027, six marches',
                   '§ 2 : six marches de juillet à décembre 2027, puis 9,54 par mois',
                   'registre § 2 ; LIASSE_PLFSS.md, amendement n° 1, VII à IX',
                   'relevé ; partage 90 % / 10 % : clé posée (§ 6)'))
    # 4. les niches fiscales, gage (A) et solde (B)
    for circuit, champ, nat in (('A', 'gage', 'recette, niche fiscale — part gagée sur la CSG'),
                                ('B', 'solde', 'recette, niche fiscale — solde rendu en taxes (refonte)')):
        g = OrderedDict()
        for n in lire_niches():
            if not n[champ]:
                continue
            for agent, part in n['payeur']:
                k = (n['famille'], n['regle'], n['premier'], agent)
                e = g.setdefault(k, dict(v=[0.0] * 48, n=0, plein=0.0))
                e['n'] += 1
                e['plein'] += n[champ] * part
                for i in range(48):
                    e['v'][i] += n[champ] * part * n['fr'][i]
        for j, ((fam, regle, premier, agent), e) in enumerate(sorted(g.items(), key=lambda x: (x[0][0], x[0][2], x[0][1], x[0][3])), 1):
            L.append(ligne(f"N{circuit}{j:02d}", circuit, nat, 'niches — ' + fam,
                           f"Niches fiscales, {fam} : {e['n']} dépenses fiscales, {e['plein']:.3f} Md€ par an en régime plein",
                           [(agent, 1.0)], e['v'], 'première incidence ' + premier, regle,
                           'LIASSE_PLF_P1.md, amendement n° 1, III et IV ; Niches fiscales.xls, « Chiffrages Résolution » N et O, « Bénéficiaires »',
                           'montant et date d’application relevés ; mois d’incidence déduit du mode de perception ; détail : calendrier_compte_complet_niches_20261117.tsv'))
    # 5. les niches sociales
    pa, pe = P['niches_sociales_part_actifs'], P['niches_sociales_part_entreprises']
    for circuit, cle_, nat in (('A', 'niches_sociales_gage', 'recette, niche sociale — part gagée sur la CSG'),
                               ('B', 'niches_sociales_solde', 'recette, niche sociale — solde affecté à l’aide fondamentale')):
        L.append(ligne('NS' + circuit, circuit, nat, 'niches — sociales', 'Niches sociales : exemptions et exonérations de cotisations sur les revenus d’activité',
                       [(MAT, pa), (ENT, pe)], paliers((6, P[cle_])), '1er juil. 2027',
                       'périodes d’activité courant à compter du 1er juillet 2027, un douzième par mois',
                       'LIASSE_PLFSS.md, amendement n° 1, I et IV ; Flux!C13 et E13 ; Détail Niches!M24 et O24',
                       'relevé'))
    # 6. circuit B : ce que le registre date et chiffre (§ 17, § 18)
    t17, t18 = lire_s17_s18()
    G, alim = P['tva_gisement'], P['tva_part_alimentation']
    r1 = G * (1 - alim) + G * alim * 4.5 / 14.5
    r2 = G * (1 - alim) + G * alim * 9.5 / 14.5
    L.append(ligne('TVA21', 'B', 'recette, refonte', 'TVA', 'Taux réduits de TVA de droit commun alignés sur le taux normal',
                   [(MNR, 0.5), (ENT, 0.5)], paliers((18, r1), (30, r2), (42, G)), '1er juil. 2028',
                   'trois marches : 1er juillet 2028, 2029 et 2030 (§ 17, règle statique)',
                   'LIASSE_PLF_P1.md, amendement n° 21, IV ; registre § 17', 'relevé ; agent : moitié ménages, moitié entreprises, clé posée (Détail Niches!L4 et O4)'))
    TS = P['taxe_salaires']
    L.append(ligne('TS', 'B', 'perte de recette, refonte', 'taxe sur les salaires', 'Taxe sur les salaires éteinte par tiers',
                   [(ENT, 1.0)], paliers((12, -TS / 3), (24, -2 * TS / 3), (36, -TS)), '1er janv. 2028',
                   'un tiers sur les rémunérations de 2028, deux tiers en 2029, abrogation au 1er janvier 2030',
                   'LIASSE_PLFSS.md, amendement n° 3, IV ; registre § 17', 'relevé ; agent : employeurs non assujettis à la TVA, part des employeurs publics non isolée'))
    ajouts = [k for k in t18 if not k.startswith('P1 n° 35')]
    a27, a28 = sum(t18[k][0] for k in ajouts), sum(t18[k][1] for k in ajouts)
    L.append(ligne('TRI', 'B', 'perte de recette, refonte', 'impôts supprimés', 'Suppressions d’impôts du tri (ajouts aux P1 n° 22, 23, 25 et 29, PLFSS n° 9)',
                   [(ENT, 1.0)], paliers((6, 2 * a27), (12, a28)), '1er juil. 2027',
                   'moitié de l’année en 2027, de juillet à décembre ; plein en 2028 (§ 18)',
                   'registre § 18 ; livrables/tri_prelevements/calendrier_suppressions_nouvelles.md', 'relevé ; total minorant (26 rangs non chiffrés) ; agent non réparti, porté aux entreprises'))
    c35 = t18[next(k for k in t18 if k.startswith('P1 n° 35'))]
    L.append(ligne('P1-35', 'B', 'perte de recette, refonte', 'impôts supprimés', 'Contribution exceptionnelle : pas de troisième exercice',
                   [(ENT, 1.0)], paliers((0, c35[0]), (12, 0.0)), 'exercice 2027',
                   '5,2 Md€ sur 2027, par douzièmes faute de pièce (« non mensualisé » au § 18)',
                   'registre § 18 ; LIASSE_PLF_P1.md, amendement n° 35', 'montant relevé ; mensualisation posée'))
    # 7. assurance chômage et patrimoine : dates du compte d'épargne (P1 n° 27, VIII)
    ch = P['chomage_epargne']
    L.append(ligne('CHO-', 'A', 'dépense, assurance chômage', 'chômage', 'Allocations de chômage transformées (ce que perdent les allocataires)',
                   [(MSR, 1.0)], paliers((12, ch)), '1er janv. 2028 (posée)', 'régime plein dès le premier mois, un douzième par mois',
                   'Annexe Manuscrit!F27 ; aucune disposition de la liasse', 'montant relevé ; DATE MANQUANTE : aucune pièce ne porte la transformation ; posée au jour du compte d’épargne'))
    L.append(ligne('CHO+', 'A', 'épargne', 'chômage', 'Cotisation chômage rendue en épargne',
                   [(MAE, 1.0)], paliers((12, -ch)), '1er janv. 2028 (posée)', 'régime plein dès le premier mois, un douzième par mois',
                   'Annexe Manuscrit!F27 ; LIASSE_PLF_P1.md, amendement n° 27, VIII', 'montant relevé ; date posée'))
    L.append(ligne('PAT', 'A', 'épargne', 'patrimoine', 'Rendement du patrimoine public rendu (versement de patrimoine)',
                   [(MNR, 1.0)], paliers((12, -P['patrimoine_rendement'])), '1er janv. 2028',
                   'versement dû au titre de 2028, égal par titulaire ; un douzième par mois',
                   'LIASSE_PLF_P1.md, amendement n° 27, III, C et VIII ; Annexe Manuscrit!F28',
                   'date relevée ; montant relevé au classeur (17,6 ; 18,2 au simulateur) ; contrepartie publique non établie par pièce'))
    return L


def par_agent(L):
    A = OrderedDict((a, [0.0] * 48) for a in AGENTS)
    for l in L:
        for agent, part in l['agents']:
            for i in range(48):
                A[agent][i] -= l['v'][i] * part
    return A


def solde_public(L, filtre=lambda l: True):
    return [sum(l['v'][i] * sum(p for _, p in l['agents']) for l in L if filtre(l)) for i in range(48)]


def epargne_rendue(L):
    """Règle du classeur : tout ce qui dépasse la baisse de CSG va à l'épargne.
    Surplus = circuit A hors chômage, hors patrimoine. L'épargne rendue est le
    surplus cumulé qui ne sera plus repris : le plus bas des cumuls à venir,
    jamais avant le 1er janvier 2028 (P1 n° 27, VIII)."""
    s = solde_public(L, lambda l: l['circuit'] == 'A' and l['famille'] not in ('chômage', 'patrimoine'))
    cumul, c = [], 0.0
    for x in s:
        c += x
        cumul.append(c)
    plancher = [max(0.0, min(cumul[i:])) for i in range(48)]
    rendu, deja = [0.0] * 48, 0.0
    for i in range(12, 48):
        rendu[i] = max(0.0, plancher[i] - deja)
        deja += rendu[i]
    return s, cumul, rendu


def lignes():
    L = lignes_hors_epargne()
    s, cumul, rendu = epargne_rendue(L)
    L.append(ligne('EPA', 'A', 'épargne', 'épargne rendue', 'Épargne rendue : surplus du circuit de restitution (versement de restitution)',
                   [(MAE, 1.0)], [-x for x in rendu], '1er janv. 2028',
                   'surplus cumulé qui ne sera plus repris, jamais avant le 1er janvier 2028',
                   'LIASSE_PLF_P1.md, amendement n° 27, III, B et VIII ; Input Capitalisation!E2 à E8', 'calculé'))
    return L


# ------------------------------------------------------------------- les sorties
def an(v):
    return [sum(v[12 * i:12 * i + 12]) for i in range(4)]


def construire():
    L = lignes()
    with open(TSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['id', 'circuit', 'nature', 'famille', 'mesure', 'agent', 'part', 'date_effet', 'regle_de_calendrier', 'piece', 'statut']
                   + COLS + [f'total_{a}' for a in ANNEES])
        n = 0
        for l in L:
            for agent, part in l['agents']:
                v = [x * part for x in l['v']]
                w.writerow([l['id'], l['circuit'], l['nature'], l['famille'], l['mesure'], agent, f'{part:g}'.replace('.', ','),
                            l['date'], l['regle'], l['piece'], l['statut']] + [f'{x:.6f}' for x in v] + [f'{x:.4f}' for x in an(v)])
                n += 1
    with open(TSV_NICHES, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['numero', 'categorie', 'famille', 'libelle', 'reference_juridique', 'beneficiaire', 'agent_qui_paie', 'type', 'marque',
                    'gage_csg_Md', 'solde_refonte_Md', 'division_du_IV', 'rattachement', 'premiere_incidence', 'regle']
                   + [f'gage_{a}' for a in ANNEES])
        N = lire_niches()
        for x in N:
            w.writerow([x['numero'], x['categorie'], x['famille'], x['libelle'], x['reference'], x['beneficiaire'],
                        ' + '.join(f'{p * 100:g} % {a}' for a, p in x['payeur']), x['type'], x['marque'],
                        f"{x['gage']:.6f}", f"{x['solde']:.6f}", x['division'], x['mode'], x['premier'], x['regle']]
                       + [f"{sum(x['fr'][12 * i:12 * i + 12]) * x['gage']:.6f}" for i in range(4)])
    print(f"{TSV.relative_to(RACINE)} : {len(L)} mesures, {n} lignes mesure × agent, 48 mois")
    print(f"{TSV_NICHES.relative_to(RACINE)} : {len(N)} dépenses fiscales")
    return 0


def lire_tsv():
    return list(csv.DictReader(open(TSV, encoding='utf-8'), delimiter='\t'))


def controler():
    P = params()
    T = lire_tsv()
    ech, out = 0, []

    def verdict(nom, ecart, tol, detail=''):
        nonlocal ech
        ok = abs(ecart) <= tol
        ech += not ok
        out.append(f"{'tenu ' if ok else 'ÉCHEC'} {nom} : écart {ecart:+.4f} Md€ (tolérance {tol:.4f}){detail}")

    M = lambda d: [float(d[c]) for c in COLS]
    # 1. les 27 coupes = le croisé du 20261116, mois par mois
    croise = {d['cellule']: [float(d[c]) for c in COLS] for d in cm.lire()}
    e = 0
    for cel, v in croise.items():
        s = [sum(M(d)[i] for d in T if d['id'] == cel) for i in range(48)]
        e = max(e, max(abs(a - b) for a, b in zip(s, v)))
    verdict('27 coupes = croisé du 20261116, 27 × 48 valeurs', e, 1e-5)
    s5 = cm.lire_s5()
    coupes = an([sum(M(d)[i] for d in T if d['id'] in croise) for i in range(48)])
    for i, a in enumerate(ANNEES):
        verdict(f'coupes {a} = § 5', coupes[i] - s5['Coupes, 27 lignes'][i], 0.03)
    # 2. la restitution = § 5
    csg = an([sum(M(d)[i] for d in T if d['id'] == 'CSG') for i in range(48)])
    for i, a in enumerate(ANNEES):
        verdict(f'restitution {a} = § 5', -csg[i] - s5['Restitution'][i], 0.03)
    # 3. solde des seules coupes et de la CSG = solde du § 5
    for i, a in enumerate(ANNEES):
        verdict(f'coupes − restitution {a} = solde du § 5', coupes[i] + csg[i] - s5['Solde du budget'][i], 0.03)
    # 4. les 8 lignes de première partie : régime plein = 8,30 (§ 4)
    huit = ('D7', 'D8', 'D9', 'D10', 'D11', 'D13', 'D14', 'D21')
    v = [sum(M(d)[i] for d in T if d['id'] in huit) for i in range(48)]
    verdict('8 lignes de première partie et sociale, rythme de décembre 2030 = 8,30 (§ 4)', v[47] * 12 - 8.30, 0.005)
    # 5. niches : régime plein = classeur
    N = lire_niches()
    verdict('niches fiscales, gage, dépense par dépense = Synthèse!C20', sum(x['gage'] for x in N) - P['niches_fiscales_gage'], 0.001)
    verdict('niches fiscales, solde = Synthèse!D20', sum(x['solde'] for x in N) - P['niches_fiscales_solde'], 0.001)
    verdict('niches, gage fiscal + social = 52,1 (Annexe Manuscrit!C24)',
            P['niches_fiscales_gage'] + P['niches_sociales_gage'] - P['niches_an1'], 0.05)
    g = [sum(M(d)[i] for d in T if d['id'].startswith('NA')) for i in range(48)]
    verdict('niches fiscales au TSV, rythme de décembre 2030 = gage du classeur', g[47] * 12 - P['niches_fiscales_gage'], 0.001)
    e = max(abs(sum(sum(x['fr'][12 * i:12 * i + 12]) * x['gage'] for x in N) - an(g)[i]) for i in range(4))
    verdict('niches fiscales au TSV, par exercice = détail par dépense fiscale', e, 1e-4)
    # 6. le IV relu au texte : les numéros d'items rangés à une division existent au III, aucun n'est à deux divisions
    items, div, _ = lire_amendement_1()
    tous = [n for k, s in div.items() for n in s]
    verdict('IV de l’amendement n° 1 : items hors du III', float(sum(n not in items for n in tous)), 0)
    verdict('IV de l’amendement n° 1 : items rangés à deux divisions', float(len(tous) - len(set(tous))), 0)
    # 7. identités du classeur
    verdict('129,459 = 114,46 + 14,999 (Flux!C6, Input Capitalisation!E8)', P['gain_an1'] - P['csg_plein'] - P['epargne_reliquat_an1'], 0.001)
    verdict('236,402 = 114,46 + 121,94 (Annexe Manuscrit!C3, Input Capitalisation!E2)',
            P['total_regime_plein'] - P['csg_plein'] - P['epargne_regime_plein'], 0.05)
    verdict('137,145 + 52,1 + 29,6 + 17,6 = 236,4',
            P['economies_etat_plein'] + P['economies_collectivites_plein'] + P['niches_an1'] + P['chomage_epargne']
            + P['patrimoine_rendement'] - P['total_regime_plein'], 0.05)
    # 8. § 17 et § 18
    t17, t18 = lire_s17_s18()
    tva = an([sum(M(d)[i] for d in T if d['id'] == 'TVA21') for i in range(48)])
    ts = an([sum(M(d)[i] for d in T if d['id'] == 'TS') for i in range(48)])
    for i, a in enumerate(ANNEES):
        verdict(f'TVA {a} = § 17', tva[i] - t17['TVA, en mesure'][i], 0.0051)
        verdict(f'taxe sur les salaires {a} = § 17', ts[i] - t17['taxe sur les salaires'][i], 0.0051)
    tri = an([sum(M(d)[i] for d in T if d['id'] in ('TRI', 'P1-35')) for i in range(48)])
    verdict('suppressions du tri 2027 = § 18 (somme des lignes du tableau)', tri[0] - sum(x[0] for x in t18.values()), 0.001)
    verdict('suppressions du tri 2028 = § 18 (somme des lignes du tableau)', tri[1] - sum(x[1] for x in t18.values()), 0.001)
    # 9. le compte : privés + public = 0 chaque mois ; le TSV se régénère à l'identique
    L = lignes()
    A = par_agent(L)
    pub = solde_public(L)
    verdict('somme des agents privés + solde public, 48 mois', max(abs(sum(A[a][i] for a in A) + pub[i]) for i in range(48)), 1e-9)
    e = 0
    for l in L:
        for agent, part in l['agents']:
            d = next(x for x in T if x['id'] == l['id'] and x['agent'] == agent)
            e = max(e, max(abs(a * part - b) for a, b in zip(l['v'], M(d))))
    verdict('TSV = reconstruction', e, 1e-6)
    verdict('lignes du TSV = lignes reconstruites', float(len(T) - sum(len(l['agents']) for l in L)), 0)
    # 10. l'épargne rendue ne rend jamais le cumul du circuit de restitution négatif
    s, cumul, rendu = epargne_rendue(lignes_hors_epargne())
    c, pire = 0.0, 0.0
    for i in range(48):
        c += s[i] - rendu[i]
        pire = min(pire, c) if i >= 12 else pire
    verdict('cumul du surplus après épargne rendue, plus bas à compter de 2028', min(0.0, pire), 1e-9)
    verdict('épargne rendue avant le 1er janvier 2028', sum(rendu[:12]), 0)
    out.append(f"{ech} contrôle(s) en échec.")
    print('\n'.join(out))
    return 1 if ech else 0


def _f(x):
    return f'{x:+.2f}'.replace('.', ',').replace('-', '−')


def etat():
    L = lignes()
    A = par_agent(L)
    pub = solde_public(L)

    def tableau(titre, lignes_, cols, idx):
        print(f'\n{titre}\n')
        print('| | ' + ' | '.join(cols) + ' |')
        print('|---|' + '---:|' * len(cols))
        for nom, v in lignes_:
            print(f'| {nom} | ' + ' | '.join(_f(sum(v[i] for i in ix)) for ix in idx) + ' |')

    ans = [range(12 * i, 12 * i + 12) for i in range(4)]
    cum = []
    c = 0.0
    for x in pub:
        c += x
        cum.append(c)
    priv = [sum(A[a][i] for a in A) for i in range(48)]
    hors = lambda l: l['circuit'] == 'A' and l['famille'] != 'patrimoine'
    rows = [(a, A[a]) for a in AGENTS] + [('**Agents privés**', priv), ('**Solde public**', pub),
            ('dont circuit de restitution, hors patrimoine', solde_public(L, hors)),
            ('dont rendement du patrimoine rendu', solde_public(L, lambda l: l['famille'] == 'patrimoine')),
            ('dont refonte, lignes datées au registre', solde_public(L, lambda l: l['circuit'] == 'B'))]
    tableau('### Par agent et par an, tous circuits', rows, [str(a) for a in ANNEES], ans)
    print('| **Solde public cumulé, fin d’exercice** | ' + ' | '.join(_f(cum[12 * i + 11]) for i in range(4)) + ' |')
    for a in (2027, 2028, 2029, 2030):
        k = annee(a)
        tableau(f'### Par agent et par mois, {a}', rows, list(cm.MOIS), [[k + m] for m in range(12)])
        print('| **Solde public cumulé** | ' + ' | '.join(_f(cum[k + m]) for m in range(12)) + ' |')
    # par circuit
    for nom, filtre in (('circuit A — restitution', lambda l: l['circuit'] == 'A'), ('circuit B — refonte, lignes du registre', lambda l: l['circuit'] == 'B')):
        print(f'\n### Solde public, {nom}, par an : ' + ' · '.join(_f(x) for x in an(solde_public(L, filtre))))
    # par famille
    fam = OrderedDict()
    for l in L:
        k = (l['circuit'], l['nature'].split(' — ')[0].split(',')[0], l['famille'])
        fam.setdefault(k, [0.0] * 48)
        for i in range(48):
            fam[k][i] += l['v'][i]
    tableau('### Par famille de mesures et par an (signe : effet sur le solde public)',
            [(' · '.join(k), v) for k, v in fam.items()], [str(a) for a in ANNEES], ans)
    # par mesure
    tableau('### Par mesure et par an (signe : effet sur le solde public)',
            [(f"{l['id']} · {l['mesure'][:70]}", l['v']) for l in L], [str(a) for a in ANNEES], ans)
    # épargne
    s, cumul, rendu = epargne_rendue(lignes_hors_epargne())
    print('\n### Surplus du circuit de restitution (hors chômage et patrimoine), cumul, épargne rendue — par mois\n')
    print('| mois | surplus | cumul | épargne rendue | cumul après épargne |')
    print('|---|---:|---:|---:|---:|')
    c = 0.0
    for i in range(48):
        c += s[i] - rendu[i]
        print(f'| {COLS[i]} | {_f(s[i])} | {_f(cumul[i])} | {_f(rendu[i])} | {_f(c)} |')
    print('\npar an — surplus : ' + ' · '.join(_f(x) for x in an(s)) + ' ; épargne rendue : ' + ' · '.join(_f(x) for x in an(rendu)))
    # niches : rattachement
    N = lire_niches()
    mode = defaultdict(float)
    for x in N:
        mode[('III' if x['mode'].startswith('III') else x['mode'].split(' (')[0])] += x['gage']
    print('\n### Niches fiscales, gage : mode de rattachement à une date (Md€) : ' + ' ; '.join(f'{k} {v:.2f}' for k, v in mode.items()))
    d = defaultdict(lambda: [0.0] * 5)
    for x in N:
        for i in range(4):
            d[x['famille']][i] += sum(x['fr'][12 * i:12 * i + 12]) * x['gage']
        d[x['famille']][4] += x['gage']
    print('\n| famille | 2027 | 2028 | 2029 | 2030 | régime plein |\n|---|---:|---:|---:|---:|---:|')
    for k, v in d.items():
        print(f'| {k} | ' + ' | '.join(f'{x:.2f}'.replace('.', ',') for x in v) + ' |')
    return 0


def leviers():
    """Les leviers de date du § 17, rejoués sur le compte complet."""
    L = lignes_hors_epargne()
    base = an(solde_public(L, lambda l: l['circuit'] == 'A' and l['famille'] not in ('chômage', 'patrimoine')))
    baseB = an(solde_public(L, lambda l: l['circuit'] == 'B'))
    print('surplus du circuit de restitution, par an : ' + ' · '.join(_f(x) for x in base))
    print('circuit B, lignes du registre, par an : ' + ' · '.join(_f(x) for x in baseB))
    s4, s5 = cm.lire_s4(), cm.lire_s5()

    def deux_ans(cels):
        eff = [0.0] * 4
        for cel in cels:
            p = s4[cel]
            F = s5[p['libelle']][3] if cel not in ('D12', 'D30', 'D33') else cm._n(p['F'].split()[0])
            juil = cm.mois_debut(p['date']) == 6
            neuf = [F / 4, 3 * F / 4, F, F] if juil else [F / 2, F, F, F]
            for i in range(4):
                eff[i] += neuf[i] - s5[p['libelle']][i]
        return eff
    P = params()
    G, alim = P['tva_gisement'], P['tva_part_alimentation']
    r1 = G * (1 - alim) + G * alim * 4.5 / 14.5
    lev = [('première marche de TVA au 1er janvier 2028 (circuit B)', [0, r1 / 2, 0, 0]),
           ('taxe sur les salaires décalée d’un an (circuit B)', [0, P['taxe_salaires'] / 3, P['taxe_salaires'] / 3, P['taxe_salaires'] / 3]),
           ('sorties en trois ans ramenées à deux, État hors aide au logement (circuit A)', deux_ans(('D5', 'D6', 'D12', 'D26', 'D30', 'D32', 'D33'))),
           ('sorties en trois ans ramenées à deux, collectivités (circuit A)', deux_ans(('D41', 'D42')))]
    for nom, e in lev:
        print(f'{nom} : ' + ' · '.join(_f(x) for x in e))
    return 0


if __name__ == '__main__':
    a = (sys.argv[1:] or ['controler'])[0]
    sys.exit({'construire': construire, 'controler': controler, 'etat': etat, 'leviers': leviers}[a]())
