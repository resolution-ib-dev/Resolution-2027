import json,re,sys,collections
sys.path.insert(0,'.'); sys.path.insert(0,'/home/user/Resolution-2027')
import droit
from matcher import S, sieges
from dossier import section, legi_index
n=droit.norm_num
V=json.load(open('visas.json'))
CIBLES={('PLF P1',19),('PLF P1',20),('PLF P1',22),('PLF P1',25),('PLF P1',29),('PLFSS',3),('PLFSS',1)}
ab=[v for v in V if (v['liasse'],v['n']) in CIBLES and re.search(r'abrog', v['alinea'], re.I) and v['code'] and not str(v['code']).startswith(('loi','ordonnance'))]
# index tri : (code, article) et (code, section)
idx_art=collections.defaultdict(set); idx_sec=collections.defaultdict(set)
for i in range(1,len(S)+1):
    for c,a in sieges(i):
        if not c: continue
        idx_art[(c,a)].add(i)
        sec,_=section(c,a)
        if sec: idx_sec[(c,sec)].add(i)
res=collections.OrderedDict()
for v in ab:
    c=v['code']; a=n(v['article'])
    key=(v['liasse'],v['n'],c,v['article'])
    if key in res: continue
    rows=idx_art.get((c,a),set())
    how='article'
    if not rows:
        ix=legi_index(c)
        sec=ix[a]['section'] if ix and a in ix else None
        rows=idx_sec.get((c,sec),set()) if sec else set()
        how='section' if rows else ('absent LEGI' if not sec else 'aucun rang')
    res[key]=(how,sorted(rows),(legi_index(c) or {}).get(a,{}).get('section','')[-90:])
out=[]
for k,(how,rows,sec) in res.items():
    out.append(dict(liasse=k[0],n=k[1],code=k[2],article=k[3],rattachement=how,rangs=rows,section=sec))
json.dump(out,open('inverse.json','w'),ensure_ascii=False,indent=0)
c=collections.Counter(o['rattachement'] for o in out); print(len(out),c)
# regroupe les « aucun rang » par section
g=collections.defaultdict(list)
for o in out:
    if o['rattachement'] in ('aucun rang',): g[(o['liasse'],o['n'],o['code'],o['section'])].append(o['article'])
for k,v in g.items(): print(k, v[:6], len(v))
