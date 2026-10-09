# -*- coding: utf-8 -*-
"""Ce que la clause fait à chaque article du CGI — rangs, III quater, III quinquies.

**Réemploi, non réinvention.** La résolution d'une désignation de division en
articles est celle que le fil 0 a versée avec son contrôle
(`appareil/fil0_regroupement/`) : même index de divisions, même grammaire de
rang, mêmes modules `clause.py` et `designer.py`. Un second résolveur ferait deux
grammaires de désignation, donc deux points de vérité — et c'est exactement la
faute que le corpus a déjà payée une fois.

Sans cette résolution, les **220 articles** que le regroupement du 20261009 a
remplacés par 171 désignations de division sortiraient « absents de nos pièces ».
"""
import os, re, sys
from collections import defaultdict

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RACINE, 'appareil', 'fil0_regroupement'))
import clause as C                                              # noqa
import designer as D                                            # noqa

CLAUSE = os.path.join(RACINE, 'livrables', 'depot_2027',
                      'clause_generale_niches_20261005.md')
KINDS = {'section', 'sous-section', 'chapitre', 'paragraphe', 'sous-paragraphe',
         'titre', 'livre', 'partie'}
SING = {'sections': 'section', 'sous-sections': 'sous-section', 'chapitres': 'chapitre',
        'paragraphes': 'paragraphe', 'sous-paragraphes': 'sous-paragraphe'}
BLOC = re.compile(r"(?:(?<=^)|(?<=, )|(?<= et )|(?<=ainsi que ))"
                  r"((?:[Ll]es?|[Ll]a) (?:(?!l’article|les articles).)*?livre (?:premier|II))")
_IDX = {}
NON_RESOLUES = []


def norm_el(t):
    w = t.split(' ')
    if w[0] in KINDS:
        return (w[0], ' '.join(w[1:]))
    if len(w) > 1 and w[1] in KINDS:
        return (w[1], w[0])
    return ('nu', t)


def index():
    if _IDX:
        return _IDX
    for code in ('cgi', 'cibs'):
        V = C.versions(code)
        nodes = defaultdict(set)
        for k, vs in V.items():
            for v in vs:
                if not C.vivant_apres(v):
                    continue
                parts = v['section'].split(' > ')
                for d in range(1, len(parts) + 1):
                    nodes[' > '.join(parts[:d])].add(vs[0]['num'])
        for nd, arts in nodes.items():
            try:
                els = [e for e in (D.element(x) for x in nd.split(' > ')) if e]
            except D.NonDesignable:
                continue
            key = (code, tuple(norm_el(t) for g, t in els[::-1]))
            _IDX.setdefault(key, set()).update(arts)
    return _IDX


def resoudre(phrase, code):
    IDX = index()
    p = re.sub(r'^(?:[Ll]es?|[Ll]a|[Ll]’)\s?', '', phrase.strip())
    chaine = re.split(r' du | de la ', p)
    tete, parent = chaine[0], chaine[1:]
    k = None
    w = tete.split(' ', 1)
    if w[0] in SING:
        k = SING[w[0]]; tete = w[1]
    elif w[0] in KINDS:
        k = w[0]; tete = w[1]
    labs = re.split(r', | et ', tete)
    par = tuple(norm_el(t) for t in parent)
    out = set()
    for l in labs:
        el = (k, l) if k else norm_el(l)
        key = (code, (el,) + par)
        if key not in IDX:
            NON_RESOLUES.append(phrase[:120])
            continue
        out |= IDX[key]
    return out


def ensemble_rang(t, code):
    """(articles entiers, subdivisions) d'un texte de rang."""
    whole, subs = set(), set()
    for mm in BLOC.finditer(t):
        for a in resoudre(mm.group(1), code):
            whole.add((code, a))
    t2 = BLOC.sub('', t)
    refs, _ = C.analyser_rang(t2 if t2.strip()[-1:] == '.' else t, code)
    for c, k, num, sd in refs:
        if k == 'a':
            whole.add((c, num))
        elif k == 'plage':
            whole |= {(c, x) for x in C.deplier(c, *num.split('|'))}
        else:
            subs.add((c, num, sd))
    return whole, subs


def _qq(T, tag):
    i = T.index('> **III %s.**' % tag)
    l = T[i:T.index('\n', i)]
    corps = re.sub(r'^.*?Sont également abrogés(?:, à compter du 1er janvier 2028,)? ', '', l)
    corps = re.sub(r' du (?:code général des impôts|même code)\.$', '', corps)
    W = set()
    if ', ainsi que les articles ' in corps:
        blocs, arts = corps.split(', ainsi que les articles ')
        for mm in BLOC.finditer(blocs):
            W |= resoudre(mm.group(1), 'cgi')
    else:
        arts = corps[len('les articles '):]
    for e in C.liste_articles(arts):
        W |= {e[1]} if e[0] == 'a' else set(C.deplier('cgi', e[1], e[2]))
    return W


def clause_sur_cgi():
    """article du CGI -> (opération, rang, division ou subdivision)."""
    T = C.lire(CLAUSE)
    lettres = C.lettres_IV(T)
    out = {}
    code = 'cgi'
    for n, l, t in C.rangs_III(T):
        m_ = re.search(r' du (code [^.]*?|même code)\.$', t)
        if m_ and m_.group(1) != 'même code':
            code = C.CODES[m_.group(1)]
        w, s = ensemble_rang(t, code)
        for c, num in w:
            if c == 'cgi':
                out.setdefault(num, ('abrogation entière', f'P1-31, III, {n}°',
                                     lettres.get(n, 'A')))
        for c, num, sd in s:
            if c == 'cgi':
                out.setdefault(num, ('abrogation partielle', f'P1-31, III, {n}°',
                                     lettres.get(n, 'A')))
    for tag, lib in (('quater', 'III quater'), ('quinquies', 'III quinquies')):
        for num in _qq(T, tag):
            out.setdefault(num, ('abrogation entière', f'P1-31, {lib}', lib))
    return out
