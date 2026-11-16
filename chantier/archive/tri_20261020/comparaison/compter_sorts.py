import csv,collections,sys
def lire(p):
    with open(p,encoding='utf-8',newline='') as f: return list(csv.DictReader(f,delimiter='\t'))
o=lire('archive/tri_20261020/versions_branche/referentiels/sort_prelevements_20261015.tsv')
m=lire('referentiels/sort_prelevements_20261015.tsv')
n=lire('referentiels/sort_prelevements_20261103.tsv')
def f(x):
    try: return float(x)
    except: return None
for nom,t,cs,cr in (('oct20',o,'sort','rendement_2026_M'),('main1015',m,'sort','rendement_2026_M'),('nov3',n,'devenir','rendement_2026_M')):
    print('==',nom,len(t),'rangs; cols',len(t[0]))
    c=collections.Counter(r[cs] for r in t); s=collections.defaultdict(float); v=collections.Counter()
    for r in t:
        x=f(r[cr])
        if x is None: v[r[cs]]+=1
        else: s[r[cs]]+=x
    for k,nb in c.most_common(): print(f'  {nb:4d}  {s[k]:12.1f}  vides={v[k]:3d}  {k}')
    print('  total',round(sum(s.values()),1),'vides',sum(v.values()))
print(sorted(set(o[0])-set(n[0])));print(sorted(set(n[0])-set(o[0])))
print(collections.Counter(r['impot_absorbant'] for r in o).most_common())
print(collections.Counter(r['impot_cible'] for r in n).most_common())
print(collections.Counter(r['bloc'] for r in n).most_common())
print(collections.Counter(r['complement_de'] for r in o).most_common())
