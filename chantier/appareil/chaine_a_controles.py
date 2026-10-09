# -*- coding: utf-8 -*-
"""Jeu de fautes de chaineA.py : chaque faute injectée doit faire échouer le contrôle."""
import subprocess, sys
src = open('appareil/chaine_a.py').read()
FAUTES = {
 '1 valeur fausse au même repère (registre § 5, D19 2028)': ("'D19': (0.50, 0.99, 0.99, 0.99)", "'D19': (0.50, 1.09, 0.99, 0.99)"),
 '2 repère qui ne résout pas (ligne PAP inexistante)': ("p_row(2029)], \"183", "p_row(99999)], \"183"),
 '3 repère retiré, valeur restant (composante sans ligne d annexe : D19 vidée)': ("'D19': ([p_row(2029)]", "'D19': (["),
 '4 verdict retourné (D19 déclarée brute)': ("'D19': (1.1, .10, True,", "'D19': (1.1, .10, False,"),
 '5 CP au-delà des AE (résiduel de la catégorie 63 annulé et AE 380 sous les CP)': ("if k_ == 'B_380': ae = EB['380']['ae']", "if k_ == 'B_380': ae = 1"),
 '6 double emploi d une ligne d annexe (577 rendue à D22 et à D30 via D22)': ("[166, 260, 332, 382, 385, 396, 496, 585,", "[166, 260, 332, 382, 385, 396, 496, 585, 166,"),
}
ok = True
for nom, (a, b) in FAUTES.items():
    assert src.count(a) == 1, f'faute non injectable : {nom}'
    open('w/_faute.py', 'w').write(src.replace(a, b))
    r = subprocess.run([sys.executable, 'w/_faute.py'], capture_output=True, text=True)
    mord = r.returncode != 0
    print(('MORD   ' if mord else 'NE MORD PAS ') + nom)
    ok &= mord
subprocess.run([sys.executable, 'appareil/chaine_a.py'], capture_output=True)  # résultats propres rétablis
if not ok: sys.exit(1)

# ---- confrontation : chaque repère se rouvre dans la pièce brute ----
import json, re, xlrd, openpyxl, sys
R = json.load(open('w/resultats.json'))
wbA = openpyxl.load_workbook('w/suivi.xlsx', data_only=True)['A — Crédits']
shP = xlrd.open_workbook('w/plf26.xls').sheet_by_name('Données PAP 2026')
def lire(src):
    m = re.match(r"`(.+?)`!L?K?(\d+)", src)
    feuille, r = m.group(1), int(m.group(2))
    if feuille == 'A — Crédits':
        return round(wbA[f'K{r}'].value * 1e6), round(wbA[f'L{r}'].value * 1e6)
    return int(shP.cell_value(r - 1, 11)), int(shP.cell_value(r - 1, 12))
n = ok = 0; div = []
items = [(c[0], c[3], c[4]) for v in R['huit'].values() for c in v['composantes']]
items += [(c[0], c[2], c[3]) for v in R['coll'].values() for c in v['comps']]
items += [(c[0], c[1], None) for c in R['etatB01']['patrimoine']['base']] + [(c[0], c[1], c[2]) for c in R['etatB01']['recherche']['base']]
for src, ae, cp in items:
    n += 1; a, c = lire(src)
    if a == ae and (cp is None or c == cp): ok += 1
    else: div.append((src, ae, cp, a, c))
print(f'concordance {ok}/{n} · non sourcés 0 · divergences {div}')
sys.exit(0 if ok == n else 1)
