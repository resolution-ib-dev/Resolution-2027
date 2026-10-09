# -*- coding: utf-8 -*-
"""Contrôle B — reprise du CGI réécrit par l'expert.

Le standard existe (`reference/cgi_expert_regles_de_lecture.md`), le contrôle
n'existait pas. Il est écrit ici, avec son jeu de fautes.

**Ce qu'il passe.** Toute pièce dont le dispositif touche un siège du code
général des impôts doit porter sa section « ce que la pièce reprend de
l'expert », qui cite les lignes des quatre tables — `ART` pour
`cgi_expert_articles.tsv`, `INS` pour les insertions, `SUP` pour les
suppressions, `PAR` pour les paramètres — et **tout écart au corpus se déclare
à l'exposé sommaire**.

**La règle de fond est acquise et ne se rouvre pas** : *le corpus prime sur la
rédaction de l'expert, et l'écart se déclare en exposé sommaire.* Le contrôle ne
juge donc jamais qui a raison. Il passe quatre choses, et quatre seulement :

| test | ce qu'il dit |
|---|---|
| **B1 — section due** | la pièce touche un siège du CGI et ne porte pas la section |
| **B2 — siège non repris** | un article du CGI touché au dispositif que la section ne cite pas |
| **B3 — ligne non résolue** | la section cite un article que les quatre tables ne portent pas |
| **B4 — écart non déclaré** | la pièce traite un article autrement que l'expert, sans le dire à l'exposé |

**B5**, à part et sans verdict d'écart : un article de
`cgi_expert_articles_bouges.tsv` employé au dispositif. La rédaction de l'expert
y part d'un état qui n'est plus le droit — le signalement est dû, la correction
ne l'est pas.

Le contrôle **ne lit aucun fichier qu'il aurait écrit** : les quatre tables
viennent du dépôt de droit, les pièces du coffre.
"""
import csv
import os
import re

from liasse import RANGS, lire, normaliser, segments
import c3_adresses as adr

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REF = os.path.join(RACINE, 'referentiels')
CGI = 'code général des impôts'

SECTION = re.compile(r'^#{1,6}\s*Ce que la pièce reprend de l[’\']expert', re.M | re.I)
FIN_SECTION = re.compile(r'^#{1,6}\s+', re.M)


RE_LIGNE = re.compile(r'\b(INS|SUP|ART|PAR)\s+(\d+)(?:\s*(?:à|et|,)\s*(\d+))*', re.I)
FICHIER = {'ART': 'cgi_expert_articles.tsv', 'INS': 'cgi_expert_insertions.tsv',
           'SUP': 'cgi_expert_suppressions.tsv', 'PAR': 'cgi_expert_parametres.tsv'}


def _tsv(nom, colonne='article'):
    chemin = os.path.join(REF, nom)
    with open(chemin, encoding='utf-8') as f:
        # QUOTE_NONE : les tables sont du TSV nu. Un seul guillemet égaré dans
        # `cgi_expert_suppressions.tsv` faisait avaler 2 690 lignes dans un
        # champ cité, et la table passait de 3 250 lignes à 560 — toute ligne
        # citée au-delà sortait alors en écart.
        return list(csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE))


def tables():
    art = _tsv('cgi_expert_articles.tsv')
    ins = _tsv('cgi_expert_insertions.tsv')
    sup = _tsv('cgi_expert_suppressions.tsv')
    par = _tsv('cgi_expert_parametres.tsv')
    bouges = _tsv('cgi_expert_articles_bouges.tsv')
    return {
        'ART': {r['article'].strip(): r for r in art if r.get('article')},
        'INS': {r['article'].strip() for r in ins if r.get('article')},
        'SUP': {r['article'].strip() for r in sup if r.get('article')},
        'PAR': {r['article'].strip(): r for r in par if r.get('article')},
        'BOUGES': {r['article'].strip(): r for r in bouges if r.get('article')},
    }


T = tables()

# Numéro de ligne -> article, pour résoudre une ligne citée. L'en-tête est la
# ligne 1 : la convention est celle que les sections emploient déjà.
LIGNE_ARTICLE, NB_LIGNES = {}, {}
for _t, _f in FICHIER.items():
    # Les sections citent le **numéro de ligne physique du fichier**, en-tête
    # compris. Un enregistrement TSV peut courir sur plusieurs lignes : compter
    # les enregistrements donnerait une table six fois trop courte et ferait
    # sortir en écart des lignes parfaitement valides.
    with open(os.path.join(REF, _f), encoding='utf-8') as _fh:
        NB_LIGNES[_t] = sum(1 for _ in _fh)
    with open(os.path.join(REF, _f), encoding='utf-8') as _fh:
        _r = csv.reader(_fh, delimiter='\t', quoting=csv.QUOTE_NONE)
        _entete = next(_r)
        _i = _entete.index('article')
        _carte, _debut = {}, 2
        for _ligne in _r:
            _fin = _r.line_num
            _art = (_ligne[_i] if len(_ligne) > _i else '').strip()
            for _n in range(_debut, _fin + 1):
                _carte[_n] = _art
            _debut = _fin + 1
        LIGNE_ARTICLE[_t] = _carte

RE_ART = re.compile(r'\b(?:articles?|art\.)\s+((?:L\.?\s?|R\.?\s?|D\.?\s?)?\d+(?:-\d+)*'
                    r'(?:\s+(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|'
                    r'undecies|duodecies|terdecies|quaterdecies|quindecies|sexdecies|septdecies|'
                    r'octodecies|novodecies|vicies|unvicies|duovicies|tervicies|quatervicies|'
                    r'quinvicies|sexvicies|septvicies|octovicies|novovicies|tricies)(?:-0)?){0,2}'
                    r'(?:\s+[A-Z]{1,2}\b)?)', re.I)

# L'abrogation en bloc d'un article dont l'expert déclare `supprimé` est la
# reprise même de l'expert : le § 3 des règles de lecture pose que C est vide et
# que la disposition modificative est « L'article N est abrogé. » La clause
# générale abroge 396 rangs à ce titre. Exemption nommée et motivée, versée avec
# le contrôle et jamais ajoutée à l'exécution.
EXEMPTION_ABROGATION_SECHE = 'abrogation sèche d’un article que l’expert déclare supprimé'


def section_expert(texte):
    m = SECTION.search(texte)
    if not m:
        return None
    f = FIN_SECTION.search(texte, m.end())
    return texte[m.start(): f.start() if f else len(texte)]


def sieges_cgi(rang, occurrences):
    """Les articles du CGI que le dispositif du rang touche."""
    return sorted({o['num'] for o in occurrences
                   if o['rang'] == rang and o['code'] == CGI
                   and o['segment'] == 'dispositif'})


def abroge_sec(disp, num):
    """Le dispositif abroge-t-il l'article num en bloc, sans toucher ses divisions ?"""
    for m in re.finditer(re.escape(num) + r'\b', disp):
        fen = disp[m.start(): m.start() + 160]
        if re.search(r'\best abrogé', fen):
            avant = disp[max(0, m.start() - 90): m.start()]
            if not re.search(r'(alinéa|phrase|mots?|membre|[IVX]+\s*(?:bis|ter)?\s*$)', avant):
                return True
    return False


def controler(rang, occurrences):
    texte = normaliser(lire(rang))
    seg = segments(texte, rang)
    disp, expose = seg['dispositif'], seg['expose']
    sieges = sieges_cgi(rang, occurrences)
    ecarts = []

    def ec(test, libelle, detail, exemption=None):
        ecarts.append({'rang': rang, 'test': test, 'libelle': libelle,
                       'detail': detail, 'exemption': exemption})

    if not sieges:
        return ecarts

    sect = section_expert(texte)
    connus = {a for a in sieges if a in T['ART'] or a in T['INS']
              or a in T['SUP'] or a in T['PAR']}

    if sect is None:
        if connus:
            secs = [a for a in sorted(connus) if not abroge_sec(disp, a)]
            if secs:
                ec('B1', 'section « ce que la pièce reprend de l’expert » absente',
                   f'{len(sieges)} siège(s) du CGI au dispositif, dont {len(connus)} '
                   f'portés par les tables ; {len(secs)} hors abrogation sèche : '
                   + ', '.join(secs[:12]) + ('…' if len(secs) > 12 else ''))
            else:
                ec('B1', 'section absente — exemption retenue',
                   f'{len(connus)} siège(s) portés par les tables, tous abrogés en bloc',
                   EXEMPTION_ABROGATION_SECHE)
        return ecarts

    # Les articles cités à la section, sous toutes les formes que la section
    # emploie : « article N », « (117 quater, alinéa 6) », « 163 quinquies D »
    # employé nu, et l'article porté par chaque ligne de table citée.
    cites = set()
    for m in RE_ART.finditer(sect):
        cites.add(re.sub(r'\s+(?:et|ou|à)$', '', m.group(1).strip()))
    cites |= {m.group(0).strip() for m in re.finditer(
        r'\b\d+(?:-\d+)?(?:\s+(?:bis|ter|quater|quinquies|sexies|septies|octies|'
        r'nonies|decies|undecies|duodecies|terdecies|quaterdecies|quindecies|'
        r'sexdecies|septdecies|octodecies|novodecies|vicies|unvicies|duovicies|'
        r'tervicies|quatervicies|quinvicies|sexvicies|tricies)(?:-0)?){1,2}'
        r'(?:\s+[A-Z]{1,2})?\b', sect)}
    cites |= {m.group(0).strip() for m in re.finditer(
        r'\((\d+(?:-\d+)?(?:\s+[a-z]+)?(?:\s+[A-Z]{1,2})?),\s*alinéa', sect)}

    # B3 — toute ligne citée doit résoudre dans sa table.
    lignes_citees = []
    for m in RE_LIGNE.finditer(sect):
        table = m.group(1).upper()
        for g in m.groups()[1:]:
            if g:
                lignes_citees.append((table, int(g)))
    for table, n in lignes_citees:
        bornes = NB_LIGNES[table]
        if n < 2 or n > bornes:
            ec('B3', 'ligne citée hors de sa table',
               f'{table} {n} — la table porte {bornes} lignes, en-tête compris')
        else:
            a = LIGNE_ARTICLE[table].get(n)
            if a:
                cites.add(a)

    for a in sieges:
        if a in cites:
            continue
        if a not in T['ART'] and a not in T['INS'] and a not in T['SUP'] and a not in T['PAR']:
            continue                       # l'expert ne dit rien de cet article
        if abroge_sec(disp, a):
            continue                       # exemption nommée
        ec('B2', 'siège du CGI touché au dispositif et non repris à la section', a)

    # B6 — la ligne citée et l'article que la section nomme à côté d'elle
    # doivent désigner le même article. Une ligne qui résout justement sous un
    # libellé faux est la première faute du jeu : le repère mord, la valeur est
    # fausse, et rien ne le dit si l'on ne confronte pas les deux.
    for m in RE_LIGNE.finditer(sect):
        table = m.group(1).upper()
        nums = [int(g) for g in m.groups()[1:] if g]
        if not nums:
            continue
        reels = {LIGNE_ARTICLE[table].get(n) for n in nums
                 if 2 <= n <= NB_LIGNES[table]}
        reels.discard(None)
        reels.discard('')
        if not reels:
            continue
        apres = sect[m.end():m.end() + 70]
        mp = re.match(r"\s*\((\d+(?:-\d+)?(?:\s+[a-zé]+)?(?:\s+[A-Z]{1,2})?)\s*[,)]", apres)
        if mp:
            nomme = mp.group(1).strip()
            if nomme not in reels:
                ec('B6', 'la ligne citée et l’article nommé à côté d’elle divergent',
                   f'{table} {"-".join(str(n) for n in nums)} porte '
                   f'{" / ".join(sorted(reels))} ; la section écrit {nomme}')

    # B4 — l'écart au corpus se déclare à l'exposé. Une déclaration générale
    # — « aucun écart à la rédaction de l'expert » — ne vaut pas déclaration :
    # **l'exposé doit nommer l'article**. Sans cette exigence, une phrase de
    # conformité suffirait à éteindre le contrôle, ce qui est précisément la
    # quatrième faute du jeu.
    divergents = []
    for a in sieges:
        r = T['ART'].get(a)
        if not r:
            continue
        op = (r.get('operation') or '').strip()
        motif = None
        if op == 'supprimé' and not abroge_sec(disp, a):
            motif = f'{a} (expert : supprimé ; la pièce ne l’abroge pas en bloc)'
        if op in ('réécrit', 'complété', 'allégé') and abroge_sec(disp, a):
            motif = f'{a} (expert : {op} ; la pièce l’abroge)'
        if motif and not re.search(re.escape(a) + r'\b', expose):
            divergents.append(motif)
    for motif in divergents:
        ec('B4', 'écart à la rédaction de l’expert non déclaré à l’exposé sommaire',
           motif)

    # B5 — article à contrôler avant emploi, signalé sans verdict d'écart.
    for a in sieges:
        if a in T['BOUGES']:
            ec('B5', 'article porté par `cgi_expert_articles_bouges.tsv` — '
               'la rédaction de l’expert part d’un état qui n’est plus le droit',
               f'{a} : {T["BOUGES"][a].get("etat", "")}', 'signalement, non écart')
    return ecarts


def jouer(occurrences=None):
    if occurrences is None:
        occurrences, _ = adr.jouer()
    tout = []
    for rang in sorted(RANGS):
        tout.extend(controler(rang, occurrences))
    return tout


if __name__ == '__main__':
    import collections
    e = jouer()
    c = collections.Counter(x['test'] for x in e)
    for k in ('B1', 'B2', 'B3', 'B4', 'B5'):
        print(f'{k} {c.get(k, 0)}')
    print('total', len(e))
    for x in e[:25]:
        print(' ', x['rang'], x['test'], x['libelle'][:60], '|', str(x['detail'])[:90])
