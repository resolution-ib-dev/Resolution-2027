import json,csv,re,sys,collections
sys.path.insert(0,'.'); sys.path.insert(0,'/home/user/Resolution-2027')
import droit
from matcher import sieges, VIS, VIS_NC
n=droit.norm_num
S=list(csv.DictReader(open('/home/user/Resolution-2027/chantier/referentiels/sort_prelevements_20261015.tsv'),delimiter='\t'))
m={o['i']:o for o in json.load(open('match.json'))}
A=[int(x) for x in open('annexeA.txt').read().split()]
U=[i for i,x in enumerate(S,1) if x['sort'] in ('fondu par rattachement','fondu dans l’équilibre') and not (x['nature']=='cotisation sociale' and x['sort']=='fondu dans l’équilibre')]
res=[]
for i in U:
    if i in A: continue
    best=None
    for c,a in sieges(i):
        cands=VIS.get((c,a),[]) or [v for v in VIS_NC.get(a,[]) if re.search(r'[a-z]',a.lstrip('lrdo')) or '-' in a]
        for v in cands:
            ab=bool(v.get('chapeau')) or bool(re.search(r'abrog|n’est pas due|ne sont pas dus|supprim',v['alinea'],re.I))
            k=(0 if ab else 1, v['liasse'], v['n'])
            if best is None or k<best[0]: best=(k,v,a)
    if best:
        k,v,a=best
        res.append(dict(i=i,libelle=S[i-1]['libelle'],verdict='A' if k[0]==0 else 'à relire',porteur=f"{v['liasse']} n° {v['n']}",article=v['article'],alinea=v['alinea'][:160]))
    else:
        res.append(dict(i=i,libelle=S[i-1]['libelle'],verdict='non relié',porteur='',article='',alinea='',l42=m[i]['l42_24']))
c=collections.Counter(r['verdict'] for r in res); print(len(res),c)
for r in res:
    if r['verdict']!='A': print(r['i'],r['libelle'][:60],'|',r['verdict'],r['porteur'],r['article'],'|',r['alinea'][:110], r.get('l42',''))
json.dump(res,open('hors120.json','w'),ensure_ascii=False,indent=0)
