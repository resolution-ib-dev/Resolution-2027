# -*- coding: utf-8 -*-
"""Chaîne A, dépôt 2027 — extraction des pièces brutes. Partie 1 de 3 : `chaine_a_extraire.py` → `chaine_a.py` → `chaine_a_controles.py`."""
"""Pièces brutes → w/A.pkl, w/pap.pkl, w/etatB2027.json. Attendus : w/suivi.xlsx (Suivi dépenses…_20261007.xlsx),
w/plf26.xls (PLF26 - Depenses 2026…_0910.xls), w/synth.xlsx (Synthèse Calculs Résolution_0910.xlsx), et le clone droit/."""
import os, json, re, unicodedata, openpyxl, pandas as pd
ws = openpyxl.load_workbook('w/suivi.xlsx', data_only=True)['A — Crédits']
rows = list(ws.iter_rows(values_only=True)); df = pd.DataFrame(rows[1:], columns=rows[0]); df['xl_row'] = range(2, len(df) + 2)
df.to_pickle('w/A.pkl')
d = pd.read_excel('w/plf26.xls', sheet_name='Données PAP 2026', header=0)
d.columns = ['type', 'mission', 'cm', 'pg', 'lpg', 'act', 'lact', 'sact', 'lsact', 'ctg', 'titre', 'ae', 'cp', 'aef', 'cpf', 'cmin', 'mn']
d['xl'] = d.index + 2; d.to_pickle('w/pap.pkl')
j = json.load(open('droit/chantier/referentiels/socle_texte_plf2027.json'))
open('w/etatB2027.txt', 'w').write([x for x in j['annexes'] if x['id'] == 'etat_B'][0]['texte'])
import re,json,unicodedata,pandas as pd
def norm(s):
    s=unicodedata.normalize('NFKD',str(s).replace('’',"'").replace(' ',' ')).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+',' ',s).strip()
t=open('w/etatB2027.txt').read()
lines=[]
for i,l in enumerate(t.split('\n')):
    m=re.match(r'^\s*(\S.*?\S)\s{2,}([\d ]+?\d)\s{2,}([\d ]+?\d)\s*$',l)
    if m:
        lines.append(dict(lib=m.group(1).strip(),ae=int(m.group(2).replace(' ','')),cp=int(m.group(3).replace(' ','')),ligne=i+1))
df=pd.read_pickle('w/A.pkl')
progs=df.groupby('Programme')['Libellé programme'].first()
mp={}
for p,l in progs.items(): mp.setdefault(norm(l),[]).append(p)
out={}
for x in lines:
    n=norm(x['lib'])
    if n.startswith('dont titre'): continue
    if n in mp:
        for p in mp[n]: out[str(p)]=x
json.dump(out,open('w/etatB2027.json','w'),ensure_ascii=False,indent=0)
print(len(lines),len(out))
miss=[p for p in progs.index if str(p) not in out]
print('programmes table A sans ligne 2027:',len(miss),miss[:80])
# Correspondances de libellé relevées à l'œil sur l'état B 2027 et inscrites ici (renommages 2026 → 2027)
ALIAS = {'205': 'mer peche et aquaculture', '149': "competitivite et durabilite de l agriculture et de l agroalimentaire"}
for p, n in ALIAS.items():
    for x in lines:
        if norm(x['lib']) == n: out[p] = x
json.dump(out, open('w/etatB2027.json', 'w'), ensure_ascii=False, indent=0)
print('après alias', len(out))
