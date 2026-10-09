# -*- coding: utf-8 -*-
"""Lecture de la clause générale : rangs du III, listes des III quater et quinquies,
listes de rangs du IV. Analyse en références atomiques (article entier / subdivision)."""
import re, json, gzip, sys
sys.path.insert(0,'/home/claude/droit')
import droit

LATIN = ['bis','ter','quater','quinquies','sexies','septies','octies','nonies','decies',
 'undecies','duodecies','terdecies','quaterdecies','quindecies','sexdecies','septdecies',
 'octodecies','novodecies','vicies','unvicies','duovicies','tervicies','quatervicies',
 'quinvicies','sexvicies','septvicies','octovicies','novovicies','tricies']
LAT = '|'.join(sorted(LATIN,key=len,reverse=True))
# numéro d'article : CGI « 199 ter-0 B », « 125-00 A », CIBS « L. 213-186 », loi « 140 »
NUM = r"(?:L\.\s?\d+(?:-\d+)+|\d+(?:-0+)?(?:(?:\s|-)(?:0+\s)?(?:%s|[A-Z]{1,3}\b))*)" % LAT
NUMRE = re.compile(NUM)

def cle(num):
    n=num.replace('L. ','L').replace('L.','L')
    if n.startswith('L'):
        return tuple((0,int(x),'') for x in n[1:].split('-'))
    out=[]
    toks=re.findall(r'-\d+|\d+|%s|[A-Z]+'%LAT, n)
    first=True
    for t in toks:
        if first: out.append((0,int(t),'')); first=False; continue
        if t.startswith('-'): out.append((1,len(t),''))
        elif t in LATIN: out.append((3,LATIN.index(t),''))
        else: out.append((2,0,t))
    return tuple(out)

CODES={'code général des impôts':'cgi','code des impositions sur les biens et services':'cibs',
       'code des douanes':'douanes','code général des collectivités territoriales':'cgct'}

def lire(path):
    T=open(path,encoding='utf-8').read()
    return T

def rangs_III(T):
    """rend [(n, ligne_complete, texte)] du III de l'article 1er"""
    i=T.index('> **III.** – Sont abrogés'); j=T.index('> **III bis.**')
    out=[]
    for l in T[i:j].split('\n'):
        m=re.match(r'> (\d+)° (.*)$',l)
        if m: out.append((int(m.group(1)),l,m.group(2)))
    return out

def liste_articles(s):
    """« 39 bis, 39 bis A et 39 bis B » / « X à Y » -> [('a',num)|('plage',a,b)]"""
    parts=re.split(r',\s|\set\s',s)
    out=[]
    for p in parts:
        p=p.strip()
        if not p: continue
        m=re.fullmatch(r'(%s)\sà\s(%s)'%(NUM,NUM),p)
        if m: out.append(('plage',m.group(1),m.group(2))); continue
        m=re.fullmatch(NUM,p)
        if m: out.append(('a',p)); continue
        raise ValueError('élément non lu: %r dans %r'%(p,s))
    return out

def analyser_rang(txt, code_prec):
    """rend (refs, code) ; refs = [(code, kind, num, subdiv_or_None)] kind in a/plage/sub"""
    code=code_prec
    m=re.search(r' du (code [^.]*?|même code)\.$',txt)
    loi=None
    if m:
        if m.group(1)!='même code': code=CODES[m.group(1)]
        corps=txt[:m.start()]
    else:
        m2=re.match(r"L’article (\d+) de la (loi n° .*)\.$",txt)
        if not m2: raise ValueError(txt)
        return [( 'loi:'+m2.group(2), 'a', m2.group(1), None)], code
    refs=[]
    s=corps
    W=re.compile(r"(?<!de )(?:L’|l’)article\s(?P<wn>%s)|(?:Les|les) articles\s(?P<wls>%s(?:(?:,\s|\set\s|\sà\s)%s)*)"%(NUM,NUM,NUM))
    S=re.compile(r"de l’article\s(?P<sn>%s)"%NUM)
    ev=[]
    for m in W.finditer(s): ev.append((m.start(),m.end(),'w',m))
    for m in S.finditer(s): ev.append((m.start(),m.end(),'s',m))
    ev.sort(key=lambda e:e[0])
    prev=0
    for st,en,k,m in ev:
        if k=='w':
            if m.group('wn'): refs.append((code,'a',m.group('wn'),None))
            else:
                for e in liste_articles(m.group('wls')):
                    if e[0]=='a': refs.append((code,'a',e[1],None))
                    else: refs.append((code,'plage',e[1]+'|'+e[2],None))
        else:
            sd=s[prev:st].strip()
            sd=re.sub(r'^(?:,\s|et\s|ainsi que\s)','',sd).strip()
            refs.append((code,'sub',m.group('sn'),sd))
        prev=en
    # contrôle de consommation : le reste ne doit être que séparateurs
    return refs, code

def quater_quinquies(T):
    i=T.index('> **III quater.** – Sont également abrogés les articles ')
    l=T[i:T.index('\n',i)]
    q4=l[len('> **III quater.** – Sont également abrogés les articles '):l.rindex(' du code général des impôts.')]
    i=T.index('> **III quinquies.** – Sont également abrogés, à compter du 1er janvier 2028, les articles ')
    l=T[i:T.index('\n',i)]
    q5=l[len('> **III quinquies.** – Sont également abrogés, à compter du 1er janvier 2028, les articles '):l.rindex(' du même code.')]
    return liste_articles(q4), liste_articles(q5)

# ---- droit
_V={}
def versions(code):
    if code in _V: return _V[code]
    d={}
    with gzip.open('/home/claude/droit/data/%s.jsonl.gz'%code,'rt',encoding='utf-8') as f:
        for l in f:
            a=json.loads(l); d.setdefault(droit.norm_num(a['num']),[]).append(a)
    _V[code]=d; return d

def vivant_apres(a, jour='2027-01-01'):
    f=a.get('date_fin') or ''
    return f in droit.FIN_OUVERTE or f>jour

def deplier(code, a, b):
    V=versions(code); ka,kb=cle(a),cle(b)
    nums=set()
    for k,vs in V.items():
        n=vs[0]['num']
        try: kk=cle(n)
        except Exception: continue
        if ka<=kk<=kb and any(vivant_apres(v) for v in vs): nums.add(n)
    return sorted(nums,key=cle)

def lettres_IV(T):
    """rend {rang: lettre} depuis les énumérations du IV (B, C, C bis, E, F) ; D = 296-355,359-390 selon §10.1 ; A = reste"""
    import re
    i=T.index('> **IV. – A.**'); j=T.index('> **V.**',i)
    IV=T[i:j]
    def plage(s):
        out=set()
        s=s.replace(' et ',', ')
        for p in s.split(', '):
            p=p.strip().rstrip('°')
            m=re.fullmatch(r'(\d+)° à (\d+)',p)
            if m: out.update(range(int(m.group(1)),int(m.group(2))+1)); continue
            m=re.fullmatch(r'(\d+)',p)
            if m: out.add(int(p)); continue
            raise ValueError(p)
        return out
    res={}
    for lettre,deb in (('B','> **B.**'),('C','> **C.**'),('C bis','> **C bis.**'),('E','> **E.**'),('F','> **F.**')):
        k=IV.index(deb); l=IV[k:IV.index('\n',k)]
        m=re.search(r'celles que le III abroge à ses (.*?), (?:le I s’applique|l’avantage est)',l)
        for n in plage(m.group(1)): res[n]=lettre
    return res
