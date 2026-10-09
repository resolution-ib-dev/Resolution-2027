import re
ORD_PARTIE={'première':'première','deuxième':'deuxième','troisième':'troisième','quatrième':'quatrième'}
class NonDesignable(Exception): pass
def element(lab):
    """rend (genre, texte) pour un élément de chemin ; None si à sauter"""
    head=lab.split(' : ')[0].strip()
    head=re.sub(r'\s*:$','',head)
    h=head
    if h.upper()=='PARTIE LÉGISLATIVE': return None
    m=re.match(r'Livre (premier|[IVXL]+(?: bis| ter)?)$',h)
    if m: return ('m','livre '+m.group(1))
    m=re.match(r'(Première|Deuxième|Troisième|Quatrième) [Pp]artie$',h)
    if m: return ('f',m.group(1).lower()+' partie')
    m=re.match(r'Titre (premier|Ier|[IVXL0-]+(?: bis| ter| quater)?)$',h)
    if m: return ('m','titre '+m.group(1))
    m=re.match(r'Chapitre (premier|Ier|[0IVXL-]+(?: bis| ter| quater)?)$',h)
    if m: return ('m','chapitre '+m.group(1))
    m=re.match(r'Section ([0-9]+|[0IVXL]+(?: bis| ter| quater)?)$',h)
    if m: return ('f','section '+m.group(1))
    m=re.match(r'Sous-section ([0-9]+)$',h)
    if m: return ('f','sous-section '+m.group(1))
    m=re.match(r'(1re|2e|3e|4e) Sous-section$',h)
    if m: return ('f',m.group(1)+' sous-section')
    m=re.match(r'Paragraphe ([0-9]+)$',h)
    if m: return ('m','paragraphe '+m.group(1))
    m=re.match(r'Sous-[Pp]aragraphe ([0-9]+)$',h)
    if m: return ('m','sous-paragraphe '+m.group(1))
    # subdivisions nues du CGI
    LAT=r'(?: (?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies|terdecies))?'
    m=re.match(r'((?:0?[IVXL]+)%s)$'%LAT,h)
    if m: return ('m',m.group(1))
    m=re.match(r'([0-9]+) ?°(-0)?(%s)(?: [A-Z][^:]*)?$'%LAT,h)
    if m: return ('m',m.group(1)+'°'+(m.group(2) or '')+(m.group(3) or ''))
    m=re.match(r'([0-9]+)\.? ?((?: (?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies))?(?: [A-Z])?)(?:\. .*)?$',h)
    if m and not h.endswith('°'): return ('m',(m.group(1)+(m.group(2) or '')).strip())
    m=re.match(r'([A-Za-z])((?: bis| ter| quater)?)$',h)
    if m: return ('m',m.group(1)+m.group(2))
    raise NonDesignable(lab)
def art(g,t,debut):
    if g=='f': return ('la ' if not debut else 'La ')+t if not t[0] in 'aeiouéè' else ("l’" if not debut else "L’")+t
    return ('le ' if not debut else 'Le ')+t
def designer(chemin):
    els=[e for e in (element(x) for x in chemin.split(' > ')) if e]
    els=els[::-1]
    out=[]
    for i,(g,t) in enumerate(els):
        if i==0: out.append(art(g,t,False))
        else:
            out.append(('du ' if g=='m' else 'de la ')+t)
    return ' '.join(out)

PLUR={'section':'sections','sous-section':'sous-sections','chapitre':'chapitres','paragraphe':'paragraphes','sous-paragraphe':'sous-paragraphes','titre':'titres','livre':'livres'}
def _parent_suffix(parent_els):
    out=[]
    for (g,t) in parent_els:
        out.append(('du ' if g=='m' else 'de la ')+t)
    return ' '.join(out)
def designer_groupe(chemins, majuscule=False):
    """chemins frères (même parent) -> désignation groupée"""
    E=[[e for e in (element(x) for x in c.split(' > ')) if e] for c in chemins]
    parents={tuple(e[:-1]) for e in E}
    assert len(parents)==1, chemins
    parent=list(E[0][:-1])[::-1]
    feuilles=[e[-1] for e in E]
    suf=_parent_suffix(parent)
    if len(feuilles)==1:
        g,t=feuilles[0]
        d=art(g,t,majuscule)
    else:
        kinds={t.split(' ')[0] if t.split(' ')[0] in PLUR else None for g,t in feuilles}
        assert len(kinds)==1, feuilles
        k=kinds.pop()
        if k:
            labs=[t[len(k)+1:] for g,t in feuilles]
            tete=PLUR[k]+' '
        else:
            labs=[t for g,t in feuilles]; tete=''
        lst=', '.join(labs[:-1])+' et '+labs[-1]
        d=('Les ' if majuscule else 'les ')+tete+lst
    return d+(' '+suf if suf else '')
