#!/usr/bin/env python3
"""Recale le graphique « 434 prélèvements aujourd'hui, 4 grands impôts demain » sur le tri (20261125).

Le graphique n'avait pas de générateur : celui-ci garde sa grille (cinq colonnes de huit carrés de
20 px au pas de 26, première ligne à y = 488 ; recettes non fiscales sur une ligne à y = 915), ses
couleurs, sa légende et ses textes, et recompose les carrés et les effectifs depuis le tri. Chaque
prélèvement va dans la colonne que lui donne le classeur du tri (fonction demain), dans l'ordre de
l'onglet « Le tri ». Écrit le SVG dans les deux pages qui le portent.

    python3 appareil/tri_porte/graphique_fusion.py [--ecrire]
"""
import html, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import classeur_tri_unique as C

SITE = Path('/home/user/Site-ETNP/site')
PAGES = [SITE / 'graphiques/fusion-des-impots.html', SITE / 'graphiques.html']
COLS = ['Impôt sur le revenu', 'Impôt sur les sociétés', 'TVA', 'Taxe foncière', 'Cotisation unique']
X0 = [120, 408, 696, 984, 1272]
DANS = {'Impôt sur le revenu': 'dans l’impôt sur le revenu', 'Impôt sur les sociétés': 'dans l’impôt sur les sociétés',
        'TVA': 'dans la TVA', 'Taxe foncière': 'dans la taxe foncière'}


def sorte(r, col):
    d = r['devenir']
    if d == 'grand impôt conservé':
        return '#000091', 'grand impôt conservé'
    if d == 'remplacé par un grand impôt':
        return '#b23a10', 'supprimé et fusionné ' + DANS[col]
    if d.startswith('fondu'):
        return '#b23a10', 'supprimé et fusionné dans l’équilibre des quatre grands impôts'
    if d == 'conservé en complément':
        b = (r['bloc'] or '').strip()
        return '#6d96b5', 'complément sectoriel' + (' : ' + b[0].lower() + b[1:] if b else '')
    if d == 'à fusionner':
        return '#c5b4ca', 'convergé en cotisation unique'
    return '#9b9188', 'recette non fiscale'


def tuile(lib, val, x, y, fill):
    a, v = html.escape(lib, quote=True), html.escape(val, quote=True)
    return (f'<g class="tuile" data-lib="{a}" data-val="{v}"><title>{html.escape(lib)} · {html.escape(val)}</title>'
            f'<rect x="{x}" y="{y}" width="20" height="20" fill="{fill}"/></g>')


def composer():
    T = C.lire(C.TRI)
    col_g = C.colonne_du_graphique()
    ordre = sorted(T, key=lambda r: C.rang_graphique(r, col_g))
    par = {c: [] for c in COLS + ['Hors impôts']}
    for r in ordre:
        par[C.demain(r, col_g)].append(r)
    assert sum(map(len, par.values())) == len(T) == 434
    tuiles = []
    for k, c in enumerate(COLS):
        assert len(par[c]) <= 8 * 15, c
        for i, r in enumerate(par[c]):
            fill, val = sorte(r, c)
            tuiles.append(tuile(' '.join(r['libelle'].split()), val, X0[k] + 26 * (i % 8), 488 + 26 * (i // 8), fill))
    for i, r in enumerate(par['Hors impôts']):
        fill, val = sorte(r, None)
        tuiles.append(tuile(' '.join(r['libelle'].split()), val, 120 + 26 * i, 915, fill))
    return par, tuiles


def recaler(svg, par, tuiles):
    svg = re.sub(r'\s*<g class="tuile".*?</g>', '', svg, flags=re.S)
    for k, c in enumerate(COLS):
        svg, n = re.subn(rf'(<text class="val" x="{X0[k]}" y="336">)\d+(</text>)', rf'\g<1>{len(par[c])}\g<2>', svg)
        assert n == 1, c
    nh = len(par['Hors impôts'])
    svg, n = re.subn(r'<text class="sub" style="fill:#3a2a1c" x="\d+" y="936">\d+ recettes non fiscales',
                     f'<text class="sub" style="fill:#3a2a1c" x="{120 + 26 * nh + 8}" y="936">{nh} recettes non fiscales', svg)
    assert n == 1
    i = svg.index('<text class="sub" style="fill:#3a2a1c"')
    return svg[:i] + ''.join(tuiles) + svg[i:]


def main():
    par, tuiles = composer()
    print('  ' + ' · '.join(f'{c} {len(v)}' for c, v in par.items()))
    for p in PAGES:
        s = p.read_text(encoding='utf-8')
        a = s.index('<text class="titre" x="120" y="196">434 prélèvements')
        a = s.rindex('<svg', 0, a)
        b = s.index('</svg>', a) + 6
        nouveau = recaler(s[a:b], par, tuiles)
        if '--ecrire' in sys.argv:
            p.write_text(s[:a] + nouveau + s[b:], encoding='utf-8')
        print(f'  {p.name} : {s[a:b].count("class=\"tuile\"")} carrés → {nouveau.count("class=\"tuile\"")}')


if __name__ == '__main__':
    main()
