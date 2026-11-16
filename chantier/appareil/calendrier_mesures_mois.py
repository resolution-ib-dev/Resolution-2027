#!/usr/bin/env python3
"""Le croisé mesure × mois, 2027 à 2030 — reconstruit le 20261116.

`livrables/flux_par_agent_20261015.md` déclare perdu le croisé mesure × agent
× mois d'un fil antérieur. Ce module le reconstruit des seules pièces qui font
foi, sans paramètre neuf :

  - § 4 de `livrables/registre_calcul_etatB.md` : les 27 lignes, leur socle,
    leur rythme, leur date d'effet et leur montant 2027 (relevé) ;
  - § 5 de la même pièce : la trajectoire annuelle 2027-2030 (relevé) ;
  - onglet « La clé d'incidence » de `referentiels/Flux_par_agent_20261015.xlsx`
    : l'agent de chaque ligne (relevé).

La mensualisation est déduite, par la règle écrite au § 16 du registre : « un
douzième par mois entre deux marches », les marches étant au 1er juillet pour
les lignes à sortie en trois ans entrées en juillet, au 1er janvier pour les
autres.

Un écart est déclaré, et un seul : la ligne D25 en 2028. Le § 16 du registre
la fait marcher au 1er juillet (2,38 puis 3,53 Md€ par trimestre au pan
« Entreprises ») ; le classeur de flux l'étale par douzièmes sur l'exercice.
Les deux donnent 4,60 Md€ sur l'année. Le registre fait foi : le croisé suit
le § 16, et l'agent « Entreprises » (donc le total) s'écarte du classeur de
flux de 0,19 Md€ par mois en 2028, en plus au premier semestre, en moins au
second.

  construire   écrit `referentiels/calendrier_mesures_mois_20261116.tsv`
  controler    rejoue le TSV contre le § 4, le § 5, le § 6, le § 16 et les
               quatre onglets du classeur de flux ; code 1 au premier écart
               au-delà de la tolérance.

En mesure, en Md€, signe positif = économie. Hors règle de CP résiduel.
"""
import csv, re, sys
from collections import OrderedDict, defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
REGISTRE = RACINE / 'livrables/registre_calcul_etatB.md'
FLUX = RACINE / 'referentiels/Flux_par_agent_20261015.xlsx'
TSV = RACINE / 'referentiels/calendrier_mesures_mois_20261116.tsv'
ANNEES = (2027, 2028, 2029, 2030)
MOIS = ('janv', 'févr', 'mars', 'avril', 'mai', 'juin', 'juil', 'août', 'sept', 'oct', 'nov', 'déc')
COLS_MOIS = [f'{a}-{m:02d}' for a in ANNEES for m in range(1, 13)]
TOL_AN = 0.0051      # le registre arrondit au centième
TOL_MOIS = 0.0051    # tolérance déjà retenue par `flux_par_agent_20261015.md`
TOL_AN_AGENT = 0.02  # la restitution du § 2, 9,54 par mois, fait 114,48 sur douze mois contre 114,46
# Écart déclaré contre le classeur de flux : D25 en 2028 (voir l'en-tête).
DECLARE = {('Entreprises', 2028), ('TOTAL', 2028)}


def _c(l):
    return [x.strip().replace('*', '').replace('⚑', '').strip() for x in l.strip().strip('|').split('|')]


def _n(s):
    s = s.replace(' ', '').replace('\xa0', '').replace(' ', '').replace(',', '.').replace('−', '-').replace('+', '')
    try:
        return float(s)
    except ValueError:
        return None


def section(debut, fin):
    out, dedans = [], False
    for i, l in enumerate(open(REGISTRE, encoding='utf-8'), 1):
        if l.startswith(debut):
            dedans = True
            continue
        if dedans and l.startswith(fin):
            break
        if dedans:
            out.append((i, l))
    return out


def lire_s4():
    s4 = OrderedDict()
    for i, l in section('## 4. Le tableau', '## 5.'):
        if l.startswith('|') and re.search(r'\| D\d+ \|', l):
            c = _c(l)
            s4[c[1]] = dict(libelle=c[0], F=c[2], socle=c[3], F_net=c[4], rythme=c[5], acteur=c[6],
                            date=c[7], fraction=c[8], an2027=_n(c[9]), programme=c[11], ligne=i)
    return s4


def lire_s5():
    s5 = OrderedDict()
    for i, l in section('## 5. Trajectoire', '## 6.'):
        if l.startswith('|'):
            c = _c(l)
            v = [_n(x) for x in c[1:5]]
            if len(c) >= 5 and all(x is not None for x in v):
                s5[c[0]] = v
    return s5


def lire_tableau(debut, fin):
    t = OrderedDict()
    for i, l in section(debut, fin):
        if l.startswith('|') and not l.startswith('|---'):
            c = _c(l)
            v = [_n(x) for x in c[1:]]
            if v and v[0] is not None:
                t[c[0].replace('’', "'")] = v
    return t


def lire_flux():
    import openpyxl
    w = openpyxl.load_workbook(FLUX, data_only=True)
    f = {}
    for nom in ('Mensuel par agent', 'Trimestriel par agent', 'Annuel par agent'):
        t = OrderedDict()
        for row in w[nom].iter_rows(values_only=True):
            if row[0] and isinstance(row[1], (int, float)):
                t[row[0].replace('’', "'")] = [x or 0 for x in row[1:]]
        f[nom] = t
    cle = defaultdict(list)
    onglet = [n for n in w.sheetnames if n.startswith('La clé')][0]
    for row in w[onglet].iter_rows(min_row=4, values_only=True):
        if row[0] and row[1] and re.search(r'D\d+', row[1]):
            moitie = set(re.findall(r'D\d+', (row[2] or '').split('moitié')[1])) if 'moitié' in (row[2] or '') else set()
            for d in re.findall(r'D\d+', row[1]):
                cle[d].append((row[0].replace('’', "'"), 0.5 if d in moitie else 1.0))
    return f, cle


def mois_debut(date):
    return 3 if 'avril' in date else 6 if 'juil' in date else 0


def mensualiser(p, traj):
    """48 valeurs. 2027 : le montant du § 4, par parts égales du mois d'effet à
    décembre. Ensuite : un douzième de l'exercice, sauf pour une sortie en
    trois ans entrée en juillet, dont la marche tombe au 1er juillet."""
    deb = mois_debut(p['date'])
    v = [0.0] * deb + [traj[0] / (12 - deb)] * (12 - deb)
    marche_juillet = p['rythme'].startswith(('⅓', '1/6')) and deb == 6
    for a in traj[1:]:
        if marche_juillet:
            h1 = v[-1]
            v += [h1] * 6 + [(a - 6 * h1) / 6] * 6
        else:
            v += [a / 12] * 12
    return v, ('1er juillet' if marche_juillet else '1er janvier')


PAN = (('Opérateurs', 5, 16), ('Chèques', 18, 22), ('Entreprises', 24, 27), ('Associations', 29, 36),
       ('Charges', 37, 37), ('Départs État', 38, 38), ('Collectivités', 40, 43))


def pan(cel):
    n = int(cel[1:])
    return next(nom for nom, a, b in PAN if a <= n <= b)


def construire():
    s4, s5 = lire_s4(), lire_s5()
    _, cle = lire_flux()
    assert len(s4) == 27, len(s4)
    with open(TSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['cellule', 'ligne_doctrinale', 'pan', 'agent', 'perimetre', 'F_regime_plein', 'socle',
                    'F_net_du_socle', 'rythme', 'date_effet_2027', 'fraction_2027', 'marche_annuelle',
                    'programme_porteur', 'adresse_registre'] + COLS_MOIS + [f'total_{a}' for a in ANNEES]
                   + [f'registre_s5_{a}' for a in ANNEES])
        for cel, p in s4.items():
            traj = s5[p['libelle']]
            assert abs(traj[0] - p['an2027']) < 1e-9, (cel, traj[0], p['an2027'])
            v, marche = mensualiser(p, traj)
            agent = ' + '.join(f"{int(part * 100)} % {a}" if part != 1 else a for a, part in cle[cel])
            perim = 'hors état B de l’État' if 'hors état B' in p['programme'] else 'État'
            w.writerow([cel, p['libelle'], pan(cel), agent, perim, p['F'], p['socle'], p['F_net'], p['rythme'],
                        p['date'], p['fraction'], marche, p['programme'],
                        f"livrables/registre_calcul_etatB.md § 4, ligne {p['ligne']}"]
                       + [f'{x:.6f}' for x in v]
                       + [f'{sum(v[12 * i:12 * i + 12]):.4f}' for i in range(4)] + [f'{x:.2f}' for x in traj])
    print(f"{TSV.relative_to(RACINE)} : 27 lignes, 48 mois")
    return 0


def lire():
    return list(csv.DictReader(open(TSV, encoding='utf-8'), delimiter='\t'))


RESTITUTION_2027 = None


def restitution():
    """§ 2 du registre : 48 valeurs mensuelles."""
    r = []
    for i, l in section('## 2. La restitution', '## 3.'):
        if l.startswith('|'):
            c = _c(l)
            x = _n(c[-1])
            if x is not None:
                r += [x] * (6 if 'juin' in c[0] else 1)
    assert len(r) == 12, r
    return r + [r[-1]] * 36


def controler():
    L = lire()
    s4, s5 = lire_s4(), lire_s5()
    flux, cle = lire_flux()
    ech, out = 0, []

    def verdict(nom, n, emax, tol, detail=''):
        nonlocal ech
        ok = emax <= tol
        ech += not ok
        out.append(f"{'tenu ' if ok else 'ÉCHEC'} {nom} : {n} valeurs, écart maximal {emax:.4f} Md€"
                   f" (tolérance {tol:.4f}){detail}")

    M = {d['cellule']: [float(d[c]) for c in COLS_MOIS] for d in L}
    # 1. somme annuelle par ligne = colonne « 2027 » du § 4 et trajectoire du § 5
    e4 = max(abs(sum(M[c][:12]) - s4[c]['an2027']) for c in s4)
    verdict('somme 2027 par ligne = § 4', 27, e4, TOL_AN)
    e5, pire = 0, ''
    for c in s4:
        for i in range(4):
            e = abs(sum(M[c][12 * i:12 * i + 12]) - s5[s4[c]['libelle']][i])
            if e > e5:
                e5, pire = e, f" ; pire : {c} {ANNEES[i]}"
    verdict('somme annuelle par ligne = § 5', 108, e5, TOL_AN, pire)
    tot5 = s5['Coupes, 27 lignes']
    et = max(abs(sum(sum(M[c][12 * i:12 * i + 12]) for c in M) - tot5[i]) for i in range(4))
    verdict('total des coupes par exercice = § 5', 4, et, 0.03)
    # 2. par agent et par mois = classeur de flux ; § 6 pour 2027
    rest = restitution()
    agents = defaultdict(lambda: [0.0] * 48)
    for c, parts in cle.items():
        for a, part in parts:
            for m in range(48):
                agents[a][m] -= M[c][m] * part
    for a in list(agents):
        k = 0.9 if 'transferts' in a else 0.1 if a.startswith('Agents') else 0
        for m in range(48):
            agents[a][m] += rest[m] * k
    fm = flux['Mensuel par agent']
    em, pire, ed, nd = 0, '', 0, 0
    for a, v in fm.items():
        tot = a.upper().startswith('TOTAL')
        calc = [sum(agents[x][m] for x in agents) for m in range(48)] if tot else agents[a]
        for m in range(48):
            e = abs(calc[m] - v[m])
            if ('TOTAL' if tot else a, ANNEES[m // 12]) in DECLARE:
                ed, nd = max(ed, e), nd + 1
            elif e > em:
                em, pire = e, f" ; pire : {a}, {COLS_MOIS[m]}"
    verdict('par agent et par mois = classeur de flux, mensuel', 9 * 48 - nd, em, TOL_MOIS, pire)
    out.append(f"      écart déclaré, D25 en 2028 : {nd} valeurs mensuelles (Entreprises et total), "
               f"écart maximal {ed:.4f} Md€, nul sur l'année")
    ft = flux['Trimestriel par agent']
    eq = max(abs(sum(agents[a][3 * q:3 * q + 3]) - v[q]) for a, v in ft.items()
             if not a.upper().startswith('TOTAL') for q in range(16) if (a, ANNEES[q // 4]) not in DECLARE)
    verdict('par agent et par trimestre = classeur de flux', 8 * 16 - 4, eq, 0.011)
    fa = flux['Annuel par agent']
    ea, pire = 0, ''
    for a, v in fa.items():
        if not a.upper().startswith('TOTAL'):
            for i in range(4):
                e = abs(sum(agents[a][12 * i:12 * i + 12]) - v[i])
                if e > ea:
                    ea, pire = e, f" ; pire : {a}, {ANNEES[i]}"
    verdict('par agent et par exercice = classeur de flux', 8 * 4, ea, TOL_AN_AGENT, pire)
    s6 = lire_tableau('## 6. Projection', '## 7.')
    e6, pire = 0, ''
    for a, v in s6.items():
        calc = [sum(agents[x][m] for x in agents) for m in range(12)] if a.upper().startswith('TOTAL') \
            else agents.get(a)
        if calc is None:
            continue
        for m in range(12):
            e = abs(abs(calc[m]) - abs(v[m]))
            if e > e6:
                e6, pire = e, f" ; pire : {a}, {MOIS[m]}"
    verdict('par agent et par mois de 2027 = § 6', 9 * 12, e6, 0.0101, pire)
    # 3. par pan et par trimestre = § 16
    s16 = lire_tableau('## 16. Tableau trimestriel', '**Par exercice**')
    noms = [n for n, _, _ in PAN]
    e16, pire = 0, ''
    for q, (tri, v) in enumerate(s16.items()):
        for j, n in enumerate(noms):
            calc = sum(sum(M[d['cellule']][3 * q:3 * q + 3]) for d in L if d['pan'] == n)
            e = abs(calc - v[j])
            if e > e16:
                e16, pire = e, f" ; pire : {n}, {tri}"
    verdict('par pan et par trimestre = § 16', 7 * 16, e16, 0.0151, pire)
    etat = sum(sum(M[d['cellule']][:12]) for d in L if d['perimetre'] == 'État')
    out.append(f"part État, somme des douze mois de 2027, en mesure : {etat:.2f} Md€")
    out.append(f"{ech} contrôle(s) en échec.")
    print('\n'.join(out))
    return 1 if ech else 0


if __name__ == '__main__':
    a = sys.argv[1:] or ['controler']
    sys.exit(construire() if a[0] == 'construire' else controler())
