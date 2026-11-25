import json, re, csv, sys, gzip, unicodedata
sys.path.insert(0,'/home/user/Resolution-2027'); sys.path.insert(0,'.')
import droit
from extraire_visas import dispositifs, LIASSES, D
from matcher import S, F, sieges, VIS, A42, L24
n=droit.norm_num
DISP=[]
for liasse,fic in LIASSES.items():
    for num,titre,disp in dispositifs(open(D+fic,encoding='utf-8').read()):
        DISP.append((liasse,num,titre,disp))
def sa(s): return ''.join(c for c in unicodedata.normalize('NFKD',s.lower()) if not unicodedata.combining(c)).replace('’',"'")
DS=[(l,k,t,sa(d),d) for l,k,t,d in DISP]
STOP=set("de la le les des du d l a au aux et en sur pour par un une dans ou certaines certains taxe taxes contribution contributions redevance redevances droit droits prelevement prelevements annuelle due perçue percue fraction".split())
def cles(lib):
    out=[]
    for sig in re.findall(r'\(([A-Z][A-Z0-9\- ]{1,15})\)', lib): out.append(sig.strip())
    for sig in re.findall(r'\b([A-Z]{3,}[A-Z0-9-]*)\b', lib): out.append(sig)
    w=[x for x in re.findall(r"[a-zà-ÿ0-9]+", sa(lib)) if x not in STOP and len(x)>3]
    if len(w)>=2: out.append(' '.join(w[:2]))
    return list(dict.fromkeys(out))
def hits_nom(lib):
    res=[]
    for k in cles(lib):
        ks=sa(k)
        for l,num,t,d,raw in DS:
            if ' ' in ks:
                a,b=ks.split(' ',1)
                if re.search(re.escape(a)+r"\W+(?:\w+\W+){0,3}"+re.escape(b), d): res.append(f'{l} n°{num} [{k}]')
            elif re.search(r'\b'+re.escape(ks)+r'\b', d): res.append(f'{l} n°{num} [{k}]')
    return sorted(set(res))
_idx={}
def legi_index(code):
    if code not in _idx:
        try: c=droit.resoudre_code(code)
        except Exception: _idx[code]=None; return None
        d={}
        with gzip.open(droit.DATA/f"{c['court']}.jsonl.gz",'rt') as f:
            for l in f:
                a=json.loads(l)
                if droit.applicable(a): d.setdefault(n(a['num']),a)
        _idx[code]=d
    return _idx[code]
def section(code,art):
    ix=legi_index(code)
    if not ix or art not in ix: return None,[]
    sec=ix[art]['section']
    sib=[a['num'] for a in ix.values() if a['section']==sec]
    return sec,sib
if __name__=='__main__':
    A=[int(x) for x in open('annexeA.txt').read().split()]
    out=[]
    for i in A:
        s,f=S[i-1],F[i-1]
        ss=sieges(i)
        secs=[]; sibhits=[]
        for c,a in ss:
            sec,sib=section(c,a)
            if sec:
                secs.append(f'{c} {a} ⊂ {sec[-140:]} ({len(sib)} art.)')
                from matcher import VIS_NC
                for x in sib:
                    for v in VIS.get((c,n(x)),[]) or [w for w in VIS_NC.get(n(x),[]) if re.search(r'[a-z]', n(x).lstrip('lrdo')) or '-' in x]: sibhits.append(f"{v['liasse']} n°{v['n']} {x}")
            else: secs.append(f'{c} {a} : absent LEGI ou code non porté')
        l42=[int(k) for k,bl in A42.items() if any(n(t) in [a for _,a in ss] for b in bl for t in re.findall(r'(?:L\.\s?|R\.\s?)?\d+(?:-\d+)*(?: (?:bis|ter|quater|quinquies|[A-Z]{1,3}))*', b['brut']))]
        out.append(dict(i=i,libelle=s['libelle'],sort=s['sort'],absorbant=s['impot_absorbant'],rdt=s['rendement_2026_M'],siege_tri=s['siege_article'],statut=s['statut_siege'],siege_declare=f['siege_declare'],code_annexe=f['code_annexe'],etatA=f['ligne_etat_A'],sieges=ss,sections=secs,visas_section=sorted(set(sibhits)),noms=hits_nom(s['libelle']), visas=[],l42=sorted(set(l42)),l42_dans_24=sorted(set(x for x in l42 if x in L24)), obs=s['observation']))
    json.dump(out,open('dossier.json','w'),ensure_ascii=False,indent=1)
    print(len(out), sum(1 for o in out if o['visas_section']), sum(1 for o in out if o['noms']), sum(1 for o in out if o['l42_dans_24']))
