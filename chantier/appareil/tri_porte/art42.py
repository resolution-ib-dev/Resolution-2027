import json,re,sys
d=json.load(open('/home/user/Resolution-2027/chantier/referentiels/socle_texte_plf2027.json'))
a=[x for x in d['articles'] if str(x['numero'])=='42'][0]
t=a['dispositif']
# isoler le tableau du I : jusqu'à "II. –"
i=t.index('I. –'); j=t.index('\n(', t.index('II. –') - 10) if 'II. –' in t else len(t)
tab=t[:t.index('II. –')]
blocs=re.split(r'\n\s*\n', tab)
rows={}
for b in blocs:
    ls=b.split('\n')
    num=None
    for l in ls:
        m=re.match(r'^\s{0,10}(\d{1,3})\s{2,}\S', l)
        if m: num=int(m.group(1)); break
    if num is None: continue
    # colonnes : A <38, B 38-70, C 70-104, reste
    A=' '.join(l[:38].strip() for l in ls); B=' '.join(l[38:70].strip() for l in ls)
    C=' '.join(l[70:104].strip() for l in ls); R=' '.join(l[104:].strip() for l in ls)
    A=re.sub(r'^\s*\d{1,3}\s','',re.sub(r'\s+',' ',A)).strip()
    nums=re.findall(r'\d{1,3}(?: \d{3})+|Non plafonnée|-', re.sub(r'\s+',' ',R))
    rows.setdefault(num,[]).append(dict(A=A,B=re.sub(r'\s+',' ',B).strip(),C=re.sub(r'\s+',' ',C).strip(),R=re.sub(r'\s+',' ',R).strip(),brut=b))
print(len(rows), sorted(rows)[:5], sorted(rows)[-5:])
missing=[k for k in range(1,max(rows)+1) if k not in rows]; print('manquent',missing)
json.dump({k:v for k,v in rows.items()},open('art42.json','w'),ensure_ascii=False,indent=0)
for k in (2,3,13,102,130): print(k, rows[k][0]['A'][:80],'|',rows[k][0]['B'][:80],'|',rows[k][0]['R'][:60])
