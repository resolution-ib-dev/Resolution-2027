"""Chaîne A — montants et dates, dépôt 2027. Calcul rejouable.
Pièces lues (jamais un fichier écrit par ce script) :
  w/A.pkl   <- Suivi dépenses…xlsx, feuille « A — Crédits » (xl_row = ligne Excel)
  w/pap.pkl <- PLF26 - Depenses 2026…xls, feuille « Données PAP 2026 » (xl = ligne Excel)
  w/etatB2027.json <- socle_texte_plf2027.json, annexe etat_B (crédits ouverts 2027)
Sortie : w/resultats.json
"""
import json, pandas as pd
from fractions import Fraction as Fr

A = pd.read_pickle('w/A.pkl'); P = pd.read_pickle('w/pap.pkl')
EB = json.load(open('w/etatB2027.json'))

def a_row(r):
    x = A[A.xl_row == r]
    assert len(x) == 1, f'A!{r} introuvable'
    x = x.iloc[0]
    return dict(src=f"`A — Crédits`!K{r}/L{r}", pg=str(x.Programme), cat=str(x.Catégorie),
                titre=str(x.Titre), ae=round(x['AE arrêtées (M€)'] * 1e6), cp=round(x['CP arrêtés (M€)'] * 1e6),
                statut=x['Statut doctrine'])

def p_row(r):
    x = P[P.xl == r]
    assert len(x) == 1, f'PAP!{r} introuvable'
    x = x.iloc[0]
    return dict(src=f"`Données PAP 2026`!L{r}/M{r}", pg=str(x.pg), cat=str(x.ctg), titre=str(x.titre),
                ae=int(x.ae), cp=int(x.cp), statut='PAP')

def residuel(cat, titre):
    """Registre § 3 — point de vérité. Aucun paramètre neuf."""
    if titre == '2' or cat in ('21', '22', '23'): return Fr(0)
    if titre in ('1', '4'): return Fr(0)
    if cat in ('32', '61', '64'): return Fr(0)
    if cat == '62': return Fr(20, 100)
    if cat == '63': return Fr(25, 100)
    if titre == '5' or cat in ('51', '52', '53'): return Fr(80, 100)
    return Fr(15, 100)

# ---------- 1. Table de passage des huit lignes ----------
ALL32 = A[(A['Statut doctrine'] == 'arrêté') & (A.Catégorie.astype(str) == '32')].xl_row.tolist()
ALL61 = A[(A['Statut doctrine'] == 'arrêté') & (A.Catégorie.astype(str) == '61')].xl_row.tolist()
ALL62 = A[(A['Statut doctrine'] == 'arrêté') & (A.Catégorie.astype(str) == '62')].xl_row.tolist()

def rows_ex(base, excl):
    return [r for r in base if r not in excl]

PASSAGE = {
 # code: (composantes état B, motif, reste hors état B)
 'D5': ([p_row(2303)], "103, cat. 32, action 4 « Financement des structures de la formation professionnelle et de l'emploi » — attribution nominative à France Compétences non portée par la ligne",
        "taxes affectées à France Compétences, `B1 — Vecteur taxes affectées` lignes 218 à 228 (première partie)"),
 'D6': ([p_row(2267)], "102, cat. 32, action 2 « Financement du service public de l'emploi »",
        "contribution de l'assurance chômage — aucune ligne d'annexe tenue"),
 'D16': ([a_row(r) for r in rows_ex(ALL32, [66, 76, 103, 223, 117])] + [p_row(2270), p_row(2283), p_row(2287), p_row(2292), p_row(2295)],
         "catégorie 32 arrêtée, résidu après les lignes nommées (D6, D12, D5, D14) et hors vie étudiante (G4 « hors éducation »)", None),
 'D19': ([p_row(2029)], "183, cat. 61, action 2 « Aide médicale de l'État »", None),
 'D22': ([p_row(955), p_row(958)] + [a_row(r) for r in [166, 260, 332, 382, 385, 396, 496, 585, 623, 646, 682, 705, 715]] + [p_row(2030)],
         "catégorie 61 arrêtée, résidu après D15, D18, D19, D20 et D21, hors enseignement scolaire (G38 « hors éducation »)", None),
 'D25': ([p_row(r) for r in [2291, 2293, 2294, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2304]],
         "103, cat. 62, hors « particuliers employeurs » (D21)", "aucune ligne d'annexe d'état B — l'apprentissage est aussi financé par France Compétences (D5) : déduit, non mesuré"),
 'D27': ([a_row(r) for r in rows_ex(ALL62, [23, 41, 43, 95, 110, 111, 161, 163, 251, 277, 302, 357, 442, 547])],
         "catégorie 62 arrêtée, résidu après D24, D25, D26, D30, D32", None),
 'D32': ([a_row(95)] + [p_row(r) for r in [2278, 2279, 2280, 2281, 2282]],
         "102, action 3 « Accompagnement des personnes les plus éloignées du marché du travail », cat. 62 et 64", None),
}
# Pas de second décompte : une ligne d'annexe ne sert qu'une fois
seen = {}
for k, (comps, _, _) in PASSAGE.items():
    for c in comps:
        assert c['src'] not in seen, f"double emploi {c['src']} ({k}, {seen.get(c['src'])})"
        seen[c['src']] = k

# ---------- 2. Paramètres du registre (§ 4), et la correction du double socle ----------
# F, socle, F déjà net du socle (preuve), calendrier, catégories pour le résiduel des lignes non nommées ci-dessus
REG = {
 # code: F, socle, net, sched, M_registre_2027, véhicule
 'D5': (10.6, .10, True, 'J3', 3.18), 'D6': (5.255, .10, True, 'J3FT', 1.31), 'D12': (0.9, .10, True, 'L3', 0.14),
 'D15': (1.3, .10, False, 'J1', 1.17), 'D16': (2.745, .10, True, 'L1', 1.24), 'D18': (16.1, 0, False, 'L3', 2.68),
 'D19': (1.1, .10, True, 'L1', 0.50), 'D20': (0.6, 0, False, 'L1', 0.30), 'D22': (1.0, 0, False, 'L1', 0.50),
 'D24': (3.8, 0, False, 'L1', 1.90), 'D25': (6.9, 0, False, 'APP', 1.15), 'D26': (3.2, 0, False, 'J3', 1.07),
 'D27': (1.3, 0, False, 'J1', 1.30), 'D29': (2.5, .20, True, 'A1', 1.50), 'D30': (3.0, 0, False, 'L3', 0.50),
 'D31': (0.9, 0, False, 'L1', 0.45), 'D32': (2.3, 0, False, 'J3', 0.77), 'D33': (1.6, 0, False, 'L3', 0.27),
 'D34': (0.5, 0, False, 'L1', 0.25), 'D35': (0.4, 0, False, 'L1', 0.20), 'D36': (1.4, 0, False, 'L1', 0.70),
 'D37': (3.8, .20, True, 'J1', 3.04), 'D38': (3.0, .10, True, 'L1', 1.35),
 'D40': (11.6, .10, True, 'J1', 10.44), 'D41': (12.3, 0, False, 'J3', 4.10), 'D42': (9.6, 0, False, 'J3', 3.20),
 'D43': (20.0, .15, True, 'L1', 8.50),
}
REG_TRAJ = {  # registre § 5, pour le contrôle de reproduction
 'D5': (3.18, 6.36, 9.54, 9.54), 'D6': (1.31, 3.15, 4.73, 4.73), 'D12': (0.14, 0.41, 0.67, 0.81), 'D15': (1.17,) * 4,
 'D16': (1.24, 2.47, 2.47, 2.47), 'D18': (2.68, 8.05, 13.42, 16.10), 'D19': (0.50, 0.99, 0.99, 0.99),
 'D20': (0.30, 0.60, 0.60, 0.60), 'D22': (0.50, 1.00, 1.00, 1.00), 'D24': (1.90, 3.80, 3.80, 3.80),
 'D25': (1.15, 4.60, 6.90, 6.90), 'D26': (1.07, 2.13, 3.20, 3.20), 'D27': (1.30,) * 4, 'D29': (1.50, 2.00, 2.00, 2.00),
 'D30': (0.50, 1.50, 2.50, 3.00), 'D31': (0.45, 0.90, 0.90, 0.90), 'D32': (0.77, 1.53, 2.30, 2.30),
 'D33': (0.27, 0.80, 1.33, 1.60), 'D34': (0.25, 0.50, 0.50, 0.50), 'D35': (0.20, 0.40, 0.40, 0.40),
 'D36': (0.70, 1.40, 1.40, 1.40), 'D37': (3.04,) * 4, 'D38': (1.35, 2.70, 2.70, 2.70), 'D40': (10.44,) * 4,
 'D41': (4.10, 8.20, 12.30, 12.30), 'D42': (3.20, 6.40, 9.60, 9.60), 'D43': (8.50, 17.00, 17.00, 17.00),
}
PANS = {'Opérateurs': ['D5', 'D6', 'D12', 'D15', 'D16'], 'Chèques aux ménages': ['D18', 'D19', 'D20', 'D22'],
        'Aides aux entreprises': ['D24', 'D25', 'D26', 'D27'], 'Associations': ['D29', 'D30', 'D31', 'D32', 'D33', 'D34', 'D35', 'D36'],
        'Charges courantes': ['D37'], 'Départs État': ['D38'], 'Collectivités': ['D40', 'D41', 'D42', 'D43']}

def step(sched, y, m):  # m = 1..12 ; marches lues au registre § 5, aucune autre
    if sched == 'J1': return Fr(1)
    if sched == 'L1': return Fr(0) if (y == 2027 and m < 7) else Fr(1)
    if sched == 'A1': return Fr(0) if (y == 2027 and m < 4) else Fr(1)
    if sched == 'J3': return min(Fr(1), Fr(y - 2026, 3))
    if sched == 'J3FT': return Fr(1, 3) * Fr(5, 6) if y == 2027 else min(Fr(1), Fr(y - 2026, 3))
    if sched == 'L3':
        k = (y - 2027) * 2 + (1 if m >= 7 else 0)  # semestres depuis 2027S1
        return Fr(0) if k == 0 else min(Fr(1), Fr((k + 1) // 2, 3))
    if sched == 'APP':
        if y == 2027: return Fr(0) if m < 7 else Fr(1, 3)
        if y == 2028 and m < 7: return Fr(1, 3)
        return Fr(1)
    raise ValueError(sched)

def regime(code, corrige):
    F, s, net, _, _ = REG[code]
    if corrige and net: return Fr(str(F))
    return Fr(str(F)) * (1 - Fr(str(s)))

def mensuel(code, corrige):
    R = regime(code, corrige); sched = REG[code][3]
    return {(y, m): R * step(sched, y, m) / 12 for y in range(2027, 2031) for m in range(1, 13)}

res = {'controles': [], 'passage': {}}
def ctl(nom, ok, detail):
    res['controles'].append(dict(nom=nom, ok=bool(ok), detail=detail))

# Contrôle 1 — la projection reproduit le registre § 5, au centième
ecarts = []
for code in REG:
    mm = mensuel(code, corrige=False)
    for i, y in enumerate(range(2027, 2031)):
        v = float(sum(mm[(y, m)] for m in range(1, 13)))
        if abs(v - REG_TRAJ[code][i]) > 0.0051 + 1e-9: ecarts.append((code, y, round(v, 4), REG_TRAJ[code][i]))
ctl('projection = registre § 5', not ecarts, f'{len(REG)*4} valeurs, écarts : {ecarts}')
tot = [round(sum(float(sum(mensuel(c, False)[(y, m)] for m in range(1, 13))) for c in REG), 2) for y in range(2027, 2031)]
ctl('totaux § 5', tot == [51.69, 92.85, 116.20, 119.79], f'{tot}')

# Contrôle 2 — preuve du double socle, ligne par ligne, sur l'annexe
PREUVE_NET = {
 'D16': sum(c['cp'] for c in PASSAGE['D16'][0]),
 'D19': p_row(2029)['cp'],
 'D29': a_row(36)['cp'],
 'D37': sum(a_row(r)['cp'] for r in A[(A['Statut doctrine'] == 'arrêté') & (A.Titre.astype(str).isin(['3', '5'])) & (A.Catégorie.astype(str) != '32')].xl_row),
 'D38': sum(a_row(r)['cp'] for r in A[(A['Statut doctrine'] == 'arrêté') & (A.Titre.astype(str) == '2')].xl_row),
 'D15': a_row(62)['cp'],
}
preuves = {}
for code, base in PREUVE_NET.items():
    F, s, net, _, _ = REG[code]
    brut = base / 1e9; netv = brut * (1 - s)
    verdict = 'net' if abs(netv - F) < abs(brut - F) else 'brut'
    preuves[code] = dict(annexe=round(brut, 3), annexe_nette=round(netv, 3), F=F, verdict=verdict, declare_net=net)
    ctl(f'socle {code}', verdict == ('net' if net else 'brut'), f'annexe {brut:.3f} · nette {netv:.3f} · F {F}')
res['preuves_socle'] = preuves

# ---------- 3. Les huit lignes : portage, montant d'amendement, CP en caisse ----------
P8 = {'D5': (Fr(1, 3), Fr(1)), 'D6': (Fr(1, 3) * Fr(5, 6), Fr(1)), 'D16': (Fr(1), Fr(1, 2)), 'D19': (Fr(1), Fr(1, 2)),
      'D22': (Fr(1), Fr(1, 2)), 'D25': (Fr(1, 6), Fr(1)), 'D27': (Fr(1), Fr(1)), 'D32': (Fr(1, 3), Fr(1))}
huit = {}
for code, (comps, motif, reste) in PASSAGE.items():
    F, s, net, _, M = REG[code]
    rythme, frac = P8[code]
    k = (1 - Fr(str(s))) * rythme * frac
    ae = sum(c['ae'] for c in comps); cp = sum(c['cp'] for c in comps)
    ae_min = sum(Fr(c['ae']) * k for c in comps)
    cp_min = sum(Fr(min(c['ae'], c['cp'])) * k * (1 - residuel(c['cat'], c['titre'])) for c in comps)
    par_pg = {}
    for c in comps:
        d = par_pg.setdefault(c['pg'], [Fr(0), Fr(0)])
        d[0] += Fr(c['ae']) * k
        d[1] += Fr(min(c['ae'], c['cp'])) * k * (1 - residuel(c['cat'], c['titre']))
    plaf = []
    for pg, (a_, c_) in par_pg.items():
        e = EB.get(pg)
        ok = e is not None and a_ <= e['ae'] and c_ <= e['cp'] and c_ <= a_
        plaf.append(dict(pg=pg, ae=round(float(a_)), cp=round(float(c_)), ae27=e and e['ae'], cp27=e and e['cp'], ok=ok))
        ctl(f'plafond {code} pg {pg}', ok or e is None and a_ == 0, f'AE {float(a_)/1e6:.1f} / CP {float(c_)/1e6:.1f} M€ sous ' + (f'{e["ae"]/1e6:.1f} / {e["cp"]/1e6:.1f}' if e else 'programme absent de l état B 2027'))
    huit[code] = dict(motif=motif, reste=reste, n_comp=len(comps), ae=ae, cp=cp, portage=round(cp / 1e9 * ((1 - s) if net else 1) / F, 3),
                      ae_min=round(float(ae_min)), cp_min=round(float(cp_min)), M_registre=M, plafonds=plaf,
                      composantes=[(c['src'], c['pg'], c['cat'], c['ae'], c['cp']) for c in comps])
res['huit'] = huit
for code, v in huit.items():
    ctl(f'sourcée {code}', v['n_comp'] >= 1 and all(c[0].startswith('`') for c in v['composantes']), f"{v['n_comp']} lignes d'annexe")

# ---------- 4. Mesure / caisse 2027, part État ----------
VEH = {  # véhicule et part portable en état B, pour les lignes nommées hors des huit (registre § 4)
 'D12': ('état B', [a_row(76)]), 'D15': ('état B', [a_row(62)]), 'D18': ('état B', [a_row(11)]), 'D20': ('état B', [p_row(953)]),
 'D24': ('état D — compte de concours financiers', []), 'D26': ('état B, AE 2027 nulles', [a_row(r) for r in [41, 111, 98, 112, 204, 433, 442, 547]]),
 'D29': ('état B', [a_row(36)]), 'D30': ('état B', [a_row(r) for r in [58, 99, 104, 251, 357, 477, 517, 577, 535, 624]]),
 'D31': ('état B', [a_row(83)]), 'D33': ('état B, AE 2027 nulles', []), 'D34': ('état B', [a_row(150)]), 'D35': ('état B', [a_row(136)]),
 'D36': ('état B — prorata, catégorie 64', None),
 'D37': ('état B', [a_row(r) for r in A[(A['Statut doctrine'] == 'arrêté') & (A.Titre.astype(str).isin(['3', '5'])) & (A.Catégorie.astype(str) != '32')].xl_row]),
 'D38': ('état B', [a_row(r) for r in A[(A['Statut doctrine'] == 'arrêté') & (A.Titre.astype(str) == '2')].xl_row]),
}
AE_NULLES_2027 = {'D26', 'D33'}  # état B 2027 : programmes 421 à 425 à 0 € d'AE
lignes = {}
for code in [c for c in REG if c not in ('D40', 'D41', 'D42', 'D43')]:
    F, s, net, sched, M = REG[code]
    Mc = float(sum(mensuel(code, True)[(2027, m)] for m in range(1, 13)))
    if code in PASSAGE: veh, comps = 'état B', PASSAGE[code][0]
    else: veh, comps = VEH[code]
    if comps is None:
        kp, kc = 1.0, 1.0
    elif code in AE_NULLES_2027 or not comps:
        kp, kc = 0.0, 0.0
    else:
        cp = sum(c['cp'] for c in comps)
        kp = min(1.0, (cp / 1e9 * ((1 - s) if net else 1)) / F)
        kc = float(sum(Fr(min(c['ae'], c['cp'])) * (1 - residuel(c['cat'], c['titre'])) for c in comps) / sum(Fr(c['cp']) for c in comps))
    lignes[code] = dict(veh=veh, M_reg=M, M_corr=round(Mc, 3), kp=round(kp, 3), kc=round(kc, 3),
                        porte=round(Mc * kp, 3), caisse=round(Mc * kp * kc, 3))
res['lignes2027'] = lignes
S = lambda k: round(sum(v[k] for v in lignes.values()), 2)
res['etat2027'] = dict(M_reg=S('M_reg'), M_corr=S('M_corr'), porte=S('porte'), caisse=S('caisse'))

# ---------- 5. Trajectoire corrigée et tableau trimestriel ----------
REST = {(2027, m): Fr(0) for m in range(1, 7)}
REST.update({(2027, 7): Fr('1.59'), (2027, 8): Fr('3.18'), (2027, 9): Fr('4.77'), (2027, 10): Fr('6.36'), (2027, 11): Fr('7.95'), (2027, 12): Fr('9.54')})
for y in (2028, 2029, 2030):
    for m in range(1, 13): REST[(y, m)] = Fr('114.46') / 12
TVA_G15 = Fr(33)                 # `Refonte fiscalité`!G15
ALIM = Fr(20, 30)                # CPO 2023 p. 32 : 20 sur 30 Md€ « eau et alimentation » (annexe3 `Synthèse` A12-A13)
def tva(y, m):
    h2 = m >= 7
    hors = Fr(0) if (y < 2028 or (y == 2028 and not h2)) else Fr(1)
    if y < 2028 or (y == 2028 and not h2): al = Fr(0)
    elif y == 2028 or (y == 2029 and not h2): al = Fr('4.5') / Fr('14.5')
    elif y == 2029 or (y == 2030 and not h2): al = Fr('9.5') / Fr('14.5')
    else: al = Fr(1)
    return TVA_G15 * ((1 - ALIM) * hors + ALIM * al) / 12
TS = Fr('17.877')                # annexe2!V96, exécution 2026
def ts(y, m):
    f = {2027: Fr(0), 2028: Fr(1, 3), 2029: Fr(2, 3), 2030: Fr(1)}[y]
    return -TS * f / 12

def trim(fn):
    return {(y, q): sum(fn(y, m) for m in range(3 * q - 2, 3 * q + 1)) for y in range(2027, 2031) for q in range(1, 5)}
pans = {}
for pan, codes in PANS.items():
    mm = [mensuel(c, True) for c in codes]
    pans[pan] = trim(lambda y, m, mm=mm: sum(x[(y, m)] for x in mm))
pans_reg = {pan: trim(lambda y, m, mm=[mensuel(c, False) for c in codes]: sum(x[(y, m)] for x in mm)) for pan, codes in PANS.items()}
rest_t = trim(lambda y, m: REST[(y, m)]); tva_t = trim(tva); ts_t = trim(ts)
an = lambda t, y: float(sum(t[(y, q)] for q in range(1, 5)))
traj = {}
for y in range(2027, 2031):
    coupes = sum(an(t, y) for t in pans.values()); coupes_reg = sum(an(t, y) for t in pans_reg.values())
    traj[y] = dict(coupes_reg=round(coupes_reg, 2), coupes=round(coupes, 2), restitution=round(an(rest_t, y), 2),
                   solde_reg=round(coupes_reg - an(rest_t, y), 2), solde=round(coupes - an(rest_t, y), 2),
                   tva=round(an(tva_t, y), 2), ts=round(an(ts_t, y), 2),
                   solde_tva_ts=round(coupes - an(rest_t, y) + an(tva_t, y) + an(ts_t, y), 2))
res['trajectoire'] = traj
ctl('restitution 2027 = 33,39', abs(traj[2027]['restitution'] - 33.39) < 0.005, traj[2027]['restitution'])
ctl('restitution 2028 = 114,46', abs(traj[2028]['restitution'] - 114.46) < 0.005, traj[2028]['restitution'])
ctl('solde registre 2028 = −21,61', abs(traj[2028]['solde_reg'] + 21.61) < 0.006, traj[2028]['solde_reg'])
ctl('trimestres = années', all(abs(sum(float(t[(y, q)]) for q in range(1, 5)) - an(t, y)) < 1e-9 for t in list(pans.values()) + [rest_t, tva_t, ts_t] for y in range(2027, 2031)), 'somme des quatre trimestres')
res['trimestres'] = {f'{y}T{q}': {**{pan: round(float(t[(y, q)]), 2) for pan, t in pans.items()},
                                  'Restitution': round(float(rest_t[(y, q)]), 2), 'TVA': round(float(tva_t[(y, q)]), 2), 'TS': round(float(ts_t[(y, q)]), 2)}
                     for y in range(2027, 2031) for q in range(1, 5)}
res['perimetre'] = dict(regime_plein_corrige=round(sum(float(regime(c, True)) for c in REG), 2),
                        regime_plein_registre=round(sum(float(regime(c, False)) for c in REG), 2))

# ---------- 6. Pièces P2 ----------
def chain(comps, k=Fr(1)):
    ae = sum(Fr(c['ae']) * k for c in comps)
    cp = sum(Fr(min(c['ae'], c['cp'])) * k * (1 - residuel(c['cat'], c['titre'])) for c in comps)
    return int(ae), int(cp)  # troncature à l'euro : on ne minore jamais au-delà
coll = {
 'A_119': dict(comps=[p_row(1992), p_row(1994), p_row(1998)], pg='119'),
 'A_122': dict(comps=[p_row(1999)], pg='122'),
 'B_380': dict(comps=[p_row(r) for r in (1112, 1113, 1114, 1115)], pg='380'),
 'C_112': dict(comps=[p_row(r) for r in (219, 222, 226)], pg='112'),
}
for k_, v in coll.items():
    ae, cp = chain(v['comps'])
    if k_ == 'B_380': ae = EB['380']['ae']  # programme entier fermé : AE ouvertes 2027 en entier
    e = EB[v['pg']]
    v.update(ae=ae, cp=cp, ae27=e['ae'], cp27=e['cp'])
    ctl(f'coll_P2_02 {k_}', cp <= ae <= e['ae'] and cp <= e['cp'], f'AE {ae} CP {cp} sous {e["ae"]} / {e["cp"]}')
    v['comps'] = [(c['src'], c['cat'], c['ae'], c['cp']) for c in v['comps']]
res['coll'] = coll
# etatB_01 — deux lignes dues
pat = [p_row(408), p_row(419)]
ae, cp = chain(pat, Fr(1, 6))
e = EB['175']; ctl('etatB_01 patrimoine', cp <= ae <= e['ae'] and cp <= e['cp'], f'{ae} {cp}')
anr = [p_row(1916)]
ae2, cp2 = chain(anr)
e2 = EB['172']; e3 = EB['150']
ctl('etatB_01 recherche', cp2 <= ae2 <= e2['ae'] and cp2 <= e2['cp'], f'{ae2} {cp2}')
res['etatB01'] = dict(patrimoine=dict(ae=ae, cp=cp, base=[(c['src'], c['ae']) for c in pat], ae27=e['ae'], cp27=e['cp']),
                      recherche=dict(ae=ae2, cp=cp2, base=[(c['src'], c['ae'], c['cp']) for c in anr], p172=e2, p150=e3))
json.dump(res, open('w/resultats.json', 'w'), ensure_ascii=False, indent=1, default=str)
print('contrôles', sum(c['ok'] for c in res['controles']), '/', len(res['controles']))
for c in res['controles']:
    if not c['ok']: print('ÉCHEC', c)
import sys
sys.exit(0 if all(c['ok'] for c in res['controles']) else 1)
