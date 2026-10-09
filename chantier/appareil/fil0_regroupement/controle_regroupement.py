# -*- coding: utf-8 -*-
"""Contrôle du regroupement par bloc de la clause générale (fil 0, 20261009).
Pièce qui fait foi : la clause AVANT passe (version du coffre) et le dépôt de droit.
Lit la clause APRÈS passe telle qu'écrite sur disque ; ne reçoit rien du générateur.
C1 numérotation continue du III · C2 couverture des listes du IV (dispositif) et du § 10.1
C3 conservation exacte de l'ensemble abrogé (articles entiers + subdivisions), désignations
   de division résolues sur le droit · C4 cohérence lettres : un rang nouveau = lettres anciennes."""
import sys, re, clause as C, designer as D
from collections import defaultdict
AV, AP = sys.argv[1], sys.argv[2]
err=[]
def E(m): err.append(m)
# ---- index des divisions du droit : désignation (tuple normalisé) -> articles vivants
KINDS={'section','sous-section','chapitre','paragraphe','sous-paragraphe','titre','livre','partie'}
def norm_el(t):
    w=t.split(' ')
    if w[0] in KINDS: return (w[0],' '.join(w[1:]))
    if len(w)>1 and w[1] in KINDS: return (w[1],w[0])
    return ('nu',t)
IDX={}
for code in ('cgi','cibs'):
    V=C.versions(code); nodes=defaultdict(set)
    for k,vs in V.items():
        for v in vs:
            if not C.vivant_apres(v): continue
            parts=v['section'].split(' > ')
            for d in range(1,len(parts)+1): nodes[' > '.join(parts[:d])].add(vs[0]['num'])
    for nd,arts in nodes.items():
        try: els=[e for e in (D.element(x) for x in nd.split(' > ')) if e]
        except D.NonDesignable: continue
        key=(code,tuple(norm_el(t) for g,t in els[::-1]))
        IDX.setdefault(key,set()).update(arts)
SING={'sections':'section','sous-sections':'sous-section','chapitres':'chapitre','paragraphes':'paragraphe','sous-paragraphes':'sous-paragraphe'}
def resoudre(phrase, code):
    """« les 1°, 3° et 4° du 5 du VII de la ... livre premier » -> ensemble d'articles"""
    p=re.sub(r'^(?:[Ll]es?|[Ll]a|[Ll]’)\s?','',phrase.strip())
    chaine=re.split(r' du | de la ',p)
    tete,parent=chaine[0],chaine[1:]
    k=None; w=tete.split(' ',1)
    if w[0] in SING: k=SING[w[0]]; tete=w[1]
    elif w[0] in KINDS: k=w[0]; tete=w[1]
    labs=re.split(r', | et ',tete)
    par=tuple(norm_el(t) for t in parent)
    out=set()
    for l in labs:
        el=(k,l) if k else norm_el(l)
        key=(code,(el,)+par)
        if key not in IDX: E('désignation non résolue : %s'%phrase[:120]); continue
        out|=IDX[key]
    return out
BLOC=re.compile(r"(?:(?<=^)|(?<=, )|(?<= et )|(?<=ainsi que ))((?:[Ll]es?|[Ll]a) (?:(?!l’article|les articles).)*?livre (?:premier|II))")
def ensemble_rang(t, code):
    """articles entiers (code,num) + subdivisions (code,num,sd) d'un texte de rang"""
    whole=set(); subs=set()
    for mm in BLOC.finditer(t):
        for a in resoudre(mm.group(1),code): whole.add((code,a))
    t2=BLOC.sub('', t)
    refs,_=C.analyser_rang(t2 if t2.strip()[-1]=='.' else t, code)
    for c,k,num,sd in refs:
        if k=='a': whole.add((c,num))
        elif k=='plage': whole|={(c,x) for x in C.deplier(c,*num.split('|'))}
        else:
            sd=re.sub(r'^(?:Le|Les|La|L’) ',lambda x:x.group(0).lower(),sd)
            m2=re.fullmatch(r'les ((?:[a-z]+(?: bis| ter| quater| quinquies| sexies)?|\d+(?: bis| ter| quater| quinquies| sexies)?°?)(?:(?:, | et )(?:[a-z]+(?: bis| ter| quater| quinquies| sexies)?|\d+(?: bis| ter| quater| quinquies| sexies)?°?))+) (du .*)',sd)
            if m2:
                for x in re.split(r', | et ',m2.group(1)): subs.add((c,num,'le '+x+' '+m2.group(2)))
            else: subs.add((c,num,sd))
    return whole,subs
def charger(path):
    T=C.lire(path); R=C.rangs_III(T); code='cgi'; out={}
    for n,l,t in R:
        m_=re.search(r' du (code [^.]*?|même code)\.$',t)
        if m_ and m_.group(1)!='même code': code=C.CODES[m_.group(1)]
        out[n]=(t,code)
    return T,out
TA,RA=charger(AV); TB,RB=charger(AP)
# C1
if sorted(RB)!=list(range(1,len(RB)+1)): E('C1 numérotation du III discontinue')
# C3 III
def tot(R):
    W=set(); S=set()
    for n,(t,c) in R.items():
        w,s=ensemble_rang(t,c); W|=w; S|=s
    return W,S
WA,SA=tot(RA); WB,SB=tot(RB)
if WA!=WB: E('C3 III articles entiers : %d perdus %s, %d ajoutés %s'%(len(WA-WB),sorted(WA-WB)[:5],len(WB-WA),sorted(WB-WA)[:5]))
if SA!=SB: E('C3 III subdivisions : %d perdues %s, %d ajoutées %s'%(len(SA-SB),sorted(SA-SB)[:3],len(SB-SA),sorted(SB-SA)[:3]))
# C3 quater / quinquies
def q(T,tag):
    i=T.index('> **III %s.**'%tag); l=T[i:T.index('\n',i)]
    corps=re.sub(r'^.*?Sont également abrogés(?:, à compter du 1er janvier 2028,)? ','',l)
    corps=re.sub(r' du (?:code général des impôts|même code)\.$','',corps)
    W=set()
    if ', ainsi que les articles ' in corps:
        blocs,arts=corps.split(', ainsi que les articles ')
        for mm in BLOC.finditer(blocs): W|=resoudre(mm.group(1),'cgi')
    else: arts=corps[len('les articles '):]
    for e in C.liste_articles(arts):
        W|= {e[1]} if e[0]=='a' else set(C.deplier('cgi',e[1],e[2]))
    return W
for tag in ('quater','quinquies'):
    a,b=q(TA,tag),q(TB,tag)
    if a!=b: E('C3 III %s : %d perdus %s, %d ajoutés %s'%(tag,len(a-b),sorted(a-b)[:5],len(b-a),sorted(b-a)[:5]))
# C2 / C4
def listes(T, region):
    def pl(s):
        out=[]
        for p in re.split(r', | et ',s.replace(' · III bis','').replace(' · III ter','')):
            p=p.strip()
            m_=re.fullmatch(r'(\d+)° à (\d+)°',p)
            if m_: out+=list(range(int(m_.group(1)),int(m_.group(2))+1)); continue
            m_=re.fullmatch(r'(\d+)°',p)
            if m_: out.append(int(m_.group(1))); continue
            E('liste illisible : %r'%p)
        return out
    res={}
    if region=='IV':
        i=T.index('> **IV. – A.**'); blk=T[i:T.index('> **V.**',i)]
        for lt,deb in (('B','> **B.**'),('C','> **C.**'),('C bis','> **C bis.**'),('E','> **E.**'),('F','> **F.**')):
            k=blk.index(deb); l=blk[k:blk.index('\n',k)]
            m_=re.search(r'celles que le III abroge à ses (.*?), (?:le I s’applique|l’avantage est)',l); res[lt]=pl(m_.group(1))
    else:
        i=T.index('### 10.1'); blk=T[i:T.index('| **total**',i)]
        for row in blk.split('\n'):
            m_=re.match(r'\| (A|B|C|C bis|D|E|F) — .*? \| .*? \| (.*?) \| (\d+) \|$',row)
            if m_:
                L=pl(m_.group(2)); res[m_.group(1)]=L
                if len(L)!=int(m_.group(3)): E('C2 § 10.1 lettre %s : compte annoncé %s, énuméré %d'%(m_.group(1),m_.group(3),len(L)))
    return res
LB=listes(TB,'§'); IVB=listes(TB,'IV')
tous=[x for v in LB.values() for x in v]
if sorted(tous)!=list(range(1,len(RB)+1)): E('C2 § 10.1 : couverture fausse (%d entrées, %d distinctes, %d rangs)'%(len(tous),len(set(tous)),len(RB)))
for lt,v in IVB.items():
    if sorted(v)!=sorted(LB.get(lt,[])): E('C2 IV %s ≠ § 10.1 %s'%(lt,lt))
# C4 : lettre de chaque rang nouveau = lettre des articles qu'il porte dans l'ancien
LA=listes(TA,'§'); lettreA={n:lt for lt,v in LA.items() for n in v}; lettreB={n:lt for lt,v in LB.items() for n in v}
art2A={}
for n,(t,c) in RA.items():
    w,s=ensemble_rang(t,c)
    for a in w: art2A[a]=lettreA.get(n)
    for x in s: art2A[x]=lettreA.get(n)
for n,(t,c) in RB.items():
    w,s=ensemble_rang(t,c)
    ls={art2A.get(a) for a in w|s}
    if ls!={lettreB.get(n)}: E('C4 rang %d : lettre %s, lettres d’origine %s'%(n,lettreB.get(n),ls))
print('ANOMALIES',len(err))
for e in err[:30]: print(' -',e)
sys.exit(1 if err else 0)
