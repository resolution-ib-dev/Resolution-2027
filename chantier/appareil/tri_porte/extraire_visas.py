"""Extrait des trois liasses les articles visés par chaque dispositif.
Sortie : visas.json  [{liasse, n, titre, code, article, partiel, contexte, alinea}]"""
import re, json, sys, gzip
sys.path.insert(0, '/home/user/Resolution-2027')
import droit

D = '/home/user/Resolution-2027/chantier/livrables/depot_2027/'
LIASSES = {'PLF P1': 'LIASSE_PLF_P1.md', 'PLF P2': 'LIASSE_PLF_P2.md', 'PLFSS': 'LIASSE_PLFSS.md'}

CODES = {c['cle'].lower(): c['court'] for c in droit._cfg()}
# noms de codes tels qu'écrits dans les dispositifs
NOMS = sorted([k for k in CODES if k.startswith('code') or k.startswith('livre')], key=len, reverse=True)

SUFF = r'(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies|terdecies|quaterdecies|quindecies|sexdecies|septdecies|octodecies|novodecies|vicies|unvicies|duovicies|tervicies|quatervicies|quinvicies|sexvicies|septvicies|octovicies|novovicies|tricies|untricies|duotricies|tertricies|quatertricies|[A-Z]{1,3}|-0|-00|-0 [A-Z])'
ART = r'(?:(?:L\.|R\.|D\.|LO|L|R|D)\s?)?\d+(?:-\d+)*(?:-?\s' + SUFF + r'(?![a-zé]))*'
ART_RE = re.compile(ART)


def dispositifs(texte):
    blocs = re.split(r'\n## Amendement n° (\d+) \[(.*?)\]\n', texte)
    for i in range(1, len(blocs), 3):
        n, titre, corps = int(blocs[i]), blocs[i + 1], blocs[i + 2]
        disp = corps.split('EXPOSÉ SOMMAIRE')[0]
        yield n, titre, disp


def code_de(fragment, courant):
    f = fragment.lower().replace('’', "'")
    if f.split('code')[0].strip().endswith(('du même','de ce')) or 'même code' in f[:20]:
        return courant
    for nom in NOMS:
        if re.match(r"\s*(?:du|de la|de l'|des|le|au)\s+" + re.escape(nom.replace('’', "'")), f):
            return CODES[nom]
    m = re.search(r"(loi|ordonnance) n° ?[\d-]+", f)
    if m:
        return m.group(0)
    return None


def ordre(code):
    """numéros d'article dans l'ordre du fichier LEGI (ordre du code)"""
    try:
        c = droit.resoudre_code(code)
    except KeyError:
        return []
    seen, out = set(), []
    with gzip.open(droit.DATA / f"{c['court']}.jsonl.gz", 'rt') as f:
        for l in f:
            a = json.loads(l)
            k = droit.norm_num(a['num'])
            if k not in seen:
                seen.add(k); out.append(a['num'])
    return out


_ordres = {}


ORD = ['bis','ter','quater','quinquies','sexies','septies','octies','nonies','decies','undecies','duodecies','terdecies','quaterdecies','quindecies','sexdecies','septdecies','octodecies','novodecies','vicies','unvicies','duovicies','tervicies','quatervicies','quinvicies','sexvicies','septvicies']


def cle(num):
    s = num.replace('.', ' ').replace('\u00a0', ' ').strip()
    m = re.match(r'^(LO|L|R|D)?\s*([\d-]+)\s*(.*)$', s)
    if not m:
        return None
    pre, nums, rest = m.group(1) or '', m.group(2), m.group(3)
    k = [pre] + [(0, int(x)) for x in nums.strip('-').split('-') if x != '']
    for t in rest.replace('-', ' ').split():
        if t in ORD:
            k.append((1, ORD.index(t)))
        elif re.fullmatch(r'[A-Z]{1,3}', t):
            k.append((2, t))
        elif t.isdigit():
            k.append((0, int(t)))
        else:
            k.append((3, t))
    return k


def _lt(a, b):
    try:
        return a < b
    except TypeError:
        return str(a) < str(b)


def deplier(code, a, b):
    if code not in _ordres:
        _ordres[code] = ordre(code)
    ka, kb = cle(a), cle(b)
    if ka is None or kb is None:
        return [a, b], 'bornes seules'
    res = []
    for x in _ordres[code]:
        k = cle(x)
        if k is None or k[0] != ka[0]:
            continue
        if not _lt(k, ka) and not _lt(kb + [(9, 'zzz')], k):
            # borne haute inclusive, avec ses suffixes (881 N inclut 881 N bis ? non) :
            if _lt(kb, k) and k[:len(kb)] != kb:
                continue
            if _lt(kb, k):
                continue
            res.append(x)
    if not res:
        return [a, b], 'bornes seules (absentes de LEGI)'
    return res, 'ordre naturel LEGI'


CODEPAT = re.compile(r"\b(?:du|de la|de l[’']|des|Le|le|au)\s+(même code|code [a-zéèêàôç' ’]+?|livre des procédures fiscales|loi n° ?[\d-]+[^,.;]*?|ordonnance n° ?[\d-]+)(?=[\s,.;:»)]|$)", re.I)


CHAP=['']

def _refs(out, liasse, n, titre, frag, c, courant, al):
    # références d'article dans le fragment
    for am in re.finditer(r"\barticles?\s+(.*?)(?=(?:\s(?:du|de la|de l[’']|des)\s+(?:même code|code|livre|loi|ordonnance))|$)", frag):
        liste = am.group(1)
        partiel = bool(re.search(r"\b(?:Le|La|Les|Au|À|du|de la)\s+(?:[IVX]+|\d+°|\d+ ?(?:bis|ter)?|[a-z])\b[^.]*?de l[’']article", frag[:am.start() + 8]))
        toks = ART_RE.findall(liste)
        # fourchettes
        spans = [(mm.group(0), mm.start(), mm.end()) for mm in ART_RE.finditer(liste)]
        k = 0
        while k < len(spans):
            a = spans[k][0].strip()
            if k + 1 < len(spans) and re.match(r'\s*à\s*$', liste[spans[k][2]:spans[k + 1][1]]):
                b = spans[k + 1][0].strip()
                arts, how = deplier(c or courant, a, b) if (c or courant) and not str(c or courant).startswith(('loi', 'ordonnance')) else ([a, b], 'bornes seules')
                for x in arts:
                    out.append(dict(liasse=liasse, n=n, titre=titre, code=c, article=x, partiel=partiel, fourchette=f'{a} à {b} ({how})', alinea=al[:220], chapeau=CHAP[0]))
                k += 2
            else:
                out.append(dict(liasse=liasse, n=n, titre=titre, code=c, article=a, partiel=partiel, fourchette='', alinea=al[:220], chapeau=CHAP[0]))
                k += 1



def visas():
    out = []
    for liasse, fic in LIASSES.items():
        t = open(D + fic, encoding='utf-8').read()
        for n, titre, disp in dispositifs(t):
            courant = None
            for al_no, al in enumerate([x for x in disp.split('\n') if x.strip()]):
                st = al.strip().lstrip('*')
                if re.match(r'^(?:[IVX]+\.|[A-Z]\.|\d+\.)\s*[–-]', st) or not re.match(r'^\d+°', st):
                    # nouvel en-tête : il fixe le chapeau pour les 1°, 2°… qui suivent
                    CHAP[0] = st[:120] if re.search(r'(?:Sont|sont|est) abrogée?s?\s*:', st) else ''
                    if re.search(r'abrogée?s?|n’est pas due|ne sont pas dus', st) and not re.search(r':\s*$', st):
                        CHAP[0] = 'ALINEA:' + st[:120]
                # coupe l'alinéa sur chaque mention de code
                pos = 0
                for m in CODEPAT.finditer(al):
                    frag = al[pos:m.end()]
                    c = code_de(al[m.start():m.start()+110], courant)
                    if c:
                        courant = c
                    _refs(out, liasse, n, titre, frag, c, courant, al)
                    pos = m.end()
                if courant and not str(courant).startswith(('loi','ordonnance')):
                    _refs(out, liasse, n, titre, al[pos:], courant, courant, al)
    return out


if __name__ == '__main__':
    v = visas()
    json.dump(v, open(sys.argv[1], 'w'), ensure_ascii=False, indent=0)
    import collections
    print(len(v), collections.Counter((x['liasse']) for x in v))
    print(collections.Counter(x['code'] for x in v).most_common(40))
