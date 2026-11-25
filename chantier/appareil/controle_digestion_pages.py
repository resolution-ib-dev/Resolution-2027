#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle d'une digestion paginée contre le texte par page de sa source.

Usage : python3 controle_digestion_pages.py <digestion.md> <texte_par_page.txt> [marge]
Le texte par page porte un marqueur `=== p. N ===` en tête de chaque page.
Le contrôle s'arrête au titre `## 10.` : les divisions de méthode ne se rejouent pas.

Chaque ligne (ou citation) qui porte un renvoi (p. N) ou (p. N-M) : tout nombre
qu'elle écrit doit se retrouver dans le texte de ces pages (± 1 page de marge
optionnelle), et toute citation en retrait doit s'y retrouver à l'identique."""
import re,sys
md,pages,marge=sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 0
def norm(s):
    s=s.replace(' ',' ').replace(' ',' ').replace(' ',' ')
    s=s.replace('’',"'").replace('−','-').replace('–','-').replace('—','-')
    return re.sub(r'\s+',' ',s).strip()
P={}
parts=re.split(r'(?m)^=== p\. (\d+) ===$',open(pages,encoding='utf8').read())
for i in range(1,len(parts),2): P[int(parts[i])]=norm(parts[i+1])
def texte(a,b): return ' '.join(P.get(n,'') for n in range(a-marge,b+marge+1))
REF=re.compile(r'p\. (\d+)(?:(?:-| à )(\d+))?(?: et (\d+))?')
NUM=re.compile(r'(?<![\w,])\d{1,3}(?: \d{3})+(?:,\d+)?|(?<![\w,])\d+(?:,\d+)?')
def nums(s):
    s=REF.sub(' ',s)
    s=re.sub(r'`[^`]*`',' ',s)
    out=[]
    for m in NUM.finditer(norm(s)):
        out.append(m.group(0))
    return out
def present(n,t):
    return re.search(r'(?<![\d,])'+re.escape(n)+r'(?![\d])(?!,\d)',t) is not None

def pages_de(refs):
    ps=set()
    for r in refs:
        x=int(r.group(1)); y=int(r.group(2) or x)
        for n in range(x-marge,y+marge+1): ps.add(n)
        if r.group(3): ps.add(int(r.group(3)))
    return ps
lignes=open(md,encoding='utf8').read().split('\n')
# blocs : citation ; item de liste ou ligne de tableau avec ses suites ; paragraphe
blocs=[];cur=None
def clos():
    global cur
    if cur: blocs.append(cur); cur=None
for l in lignes:
    if not l.strip(): clos(); continue
    if l.startswith('>'):
        if cur and cur[0]=='q': cur[1].append(l[1:].strip())
        else: clos(); cur=['q',[l[1:].strip()]]
    elif l.lstrip().startswith(('- ','|','#')) or re.match(r'\s*\d+\. ',l):
        clos(); cur=['t',[l]]
    else:
        if cur and cur[0]=='t': cur[1].append(l)
        else: clos(); cur=['t',[l]]
clos()
tot=ko=cit=citko=sansref=0; rapport=[]
corps=False; dernier=[]
for k,(typ,ls) in enumerate(blocs):
    if ls[0].startswith('##'): corps=True
    if ls[0].startswith('## 10.'): break
    if not corps: continue
    txt=norm(' '.join(ls))
    if typ=='q':
        cit+=1
        refs=list(REF.finditer(txt))
        if not refs and k+1<len(blocs): refs=list(REF.finditer(norm(' '.join(blocs[k+1][1]))))[:1]
        q=norm(REF.sub('',txt)).strip(' *_')
        if not refs: citko+=1; rapport.append(('CITATION SANS PAGE',q[:90])); continue
        t=' '.join(P.get(n,'') for n in sorted(pages_de(refs)))
        if q not in t: citko+=1; rapport.append(('CITATION ABSENTE '+refs[0].group(0),q[:110]))
        continue
    if txt.startswith('#') or set(txt)<=set('|-: '): continue
    refs=list(REF.finditer(txt)); ns=nums(' '.join(ls))
    if refs and not txt.startswith('|'): dernier=refs
    if not refs and txt.startswith('|'): refs=dernier
    if not ns: continue
    if not refs:
        sansref+=1; rapport.append(('BLOC CHIFFRÉ SANS PAGE',txt[:110])); continue
    t=' '.join(P.get(n,'') for n in sorted(pages_de(refs)))
    for n in ns:
        tot+=1
        if not present(n,t): ko+=1; rapport.append((f'NOMBRE ABSENT {",".join(r.group(0) for r in refs)[:40]} : {n}',txt[:110]))
print(f'{tot} nombres contrôlés, {tot-ko} retrouvés ; {cit} citations, {cit-citko} retrouvées ; {sansref} bloc(s) chiffré(s) sans page')
for r in rapport: print(' ',r[0],'|',r[1])
sys.exit(1 if (citko or sansref) else 0)
