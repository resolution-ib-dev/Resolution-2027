#!/usr/bin/env python3
"""Images du graphique « 434 prélèvements » : PNG paysage (1600 × 1230), PDF, PNG portrait (1200 × 1500).

Rendu par Chromium avec les polices du graphique (feuille de style de la page). Le paysage est le SVG
de la page. Le portrait reprend sa mise en page : cinq colonnes de cinq carrés, titre sur deux lignes
(calibré le 20261125 sur l'image portrait existante).

    NODE_PATH=/opt/node-tools/node_modules python3 appareil/tri_porte/graphique_fusion_images.py [dossier]
"""
import re, subprocess, sys, json, tempfile
from pathlib import Path

PAGE = Path('/home/user/Site-ETNP/site/graphiques/fusion-des-impots.html')
SORTIE = Path(sys.argv[1]) if len(sys.argv) > 1 else PAGE.parent
X0P = [70, 302, 534, 766, 998]


def morceaux():
    s = PAGE.read_text(encoding='utf-8')
    a = s.index('<style'); style = s[a:s.index('</style>', a) + 8]
    k = s.index('<svg viewBox="0 0 1600 1230"'); svg = s[k:s.index('</svg>', k) + 6]
    return style, svg


def portrait(svg):
    t = lambda pat: re.search(pat, svg, re.S)
    vals = re.findall(r'<text class="val" x="(\d+)" y="336">(\d+)</text>', svg)
    subs = re.findall(r'<text class="sub" style="font-style:italic" x="(\d+)" y="378">([^<]*)</text>', svg)
    labs = re.findall(r'<text class="lab" x="(\d+)" y="(\d+)">([^<]*)</text>', svg)
    X = [120, 408, 696, 984, 1272]
    col = {x: i for i, x in enumerate(X)}
    out = ['<svg viewBox="0 0 1200 1500" xmlns="http://www.w3.org/2000/svg" style="max-width:1200px"><rect x="0" y="0" width="1200" height="1500" fill="#fffdf2"/>',
           '<text class="marque" style="font-size:46px;letter-spacing:.20em" x="70" y="88">RÉSOLUTION</text>',
           '<rect x="70" y="112" width="353.3" height="5" fill="#000091"/>',
           '<rect x="423.3" y="112" width="353.3" height="5" fill="#ffffff" stroke="#d9cfbe" stroke-width="1"/>',
           '<rect x="776.7" y="112" width="353.3" height="5" fill="#e1000f"/>',
           '<text class="titre" x="70" y="196">434 prélèvements aujourd’hui,</text>',
           '<text class="titre" x="70" y="258">4 grands impôts demain</text>',
           '<text class="chapeau" x="70" y="314">Un carré, un prélèvement, rangé sous l’impôt qui le reprend.</text>']
    for x, v in vals:
        out.append(f'<text class="val" x="{X0P[col[int(x)]]}" y="398">{v}</text>')
    for x, v in subs:
        out.append(f'<text class="sub" style="font-style:italic" x="{X0P[col[int(x)]]}" y="440">{v}</text>')
    for x, y, v in labs:
        out.append(f'<text class="lab" x="{X0P[col[int(x)]]}" y="{482 if y == "420" else 520}">{v}</text>')
    # carrés : relus dans l'ordre de la page, colonne par colonne
    tu = re.findall(r'(<g class="tuile".*?<rect x=")([\d.]+)(" y=")([\d.]+)(" width="20" height="20" fill="[^"]+"/></g>)', svg, re.S)
    n = {i: 0 for i in range(5)}; h = 0
    for a, x, b, y, c in tu:
        x, y = float(x), float(y)
        if y == 915:
            out.append(f'{a}{70 + 26 * h}{b}1186{c}'); h += 1
            continue
        i = min(4, int((x - 120) // 288)); k = n[i]; n[i] += 1
        out.append(f'{a}{X0P[i] + 26 * (k % 5)}{b}{550 + 26 * (k // 5)}{c}')
    rec = t(r'<text class="sub" style="fill:#3a2a1c" x="\d+" y="936">([^<]*)</text>').group(1)
    out.append(f'<text class="sub" style="fill:#3a2a1c" x="{70 + 26 * h + 8}" y="1206">{rec}</text>')
    leg = re.findall(r'<rect x="(120|800)" y="(977|1021)" width="20" height="20" fill="([^"]+)"/><text class="sub" style="fill:#3a2a1c" x="\d+" y="\d+">([^<]*)</text>', svg)
    out.append('<rect x="70" y="1228" width="1060" height="1" fill="#d9cfbe"/>')
    for x, y, f, lib in leg:
        X1 = 70 if x == '120' else 600
        Y1 = 1247 if y == '977' else 1291
        out.append(f'<rect x="{X1}" y="{Y1}" width="20" height="20" fill="{f}"/><text class="sub" style="fill:#3a2a1c" x="{X1 + 34}" y="{Y1 + 21}">{lib}</text>')
    out.append('<rect x="70" y="1342" width="1060" height="1" fill="#d9cfbe"/>')
    src = t(r'<text class="source" x="120" y="1104">([^<]*)</text>').group(1)
    out.append(f'<text class="source" x="70" y="1374">{src}</text></svg>')
    return '\n'.join(out)


def rendre(style, svg_p, svg_l, dossier):
    d = Path(tempfile.mkdtemp())
    for nom, svg, w, h in (('l', svg_l, 1600, 1230), ('p', svg_p, 1200, 1500)):
        (d / f'{nom}.html').write_text(f'<!doctype html><meta charset=utf-8>{style}<style>html,body{{margin:0;background:#fffdf2}}'
                                       f'.s-piece svg{{display:block;width:{w}px;height:{h}px;max-width:none}}</style>'
                                       f'<div class=s-piece>{svg}</div>', encoding='utf-8')
    js = f'''const {{chromium}} = require('playwright');
(async () => {{ const b = await chromium.launch(); 
for (const [n, w, h, png] of [['l',1600,1230,'fusion-des-impots.png'],['p',1200,1500,'fusion-des-impots-portrait.png']]) {{
  const p = await b.newPage({{viewport: {{width: w, height: h}}, deviceScaleFactor: 1}});
  await p.goto('file://{d}/' + n + '.html'); await p.evaluate(() => document.fonts.ready);
  const ok = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family));
  if (!ok.some(f => f.includes('Archivo')) || !ok.some(f => f.includes('Source Serif'))) throw new Error('polices de repli : ' + ok);
  await p.screenshot({{path: '{dossier}/' + png, clip: {{x:0, y:0, width:w, height:h}}}});
  if (n === 'l') await p.pdf({{path: '{dossier}/fusion-des-impots.pdf', width: '1600px', height: '1230px', printBackground: true, pageRanges: '1'}});
}}
await b.close(); }})().catch(e => {{ console.error(e); process.exit(1); }});'''
    (d / 'r.js').write_text(js)
    r = subprocess.run(['node', str(d / 'r.js')], capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr)


if __name__ == '__main__':
    style, svg = morceaux()
    SORTIE.mkdir(parents=True, exist_ok=True)
    rendre(style, portrait(svg), svg, SORTIE.resolve())
    print('  écrit :', ', '.join(p.name for p in sorted(SORTIE.glob('fusion-des-impots*.p*'))))
