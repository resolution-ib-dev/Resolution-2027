# -*- coding: utf-8 -*-
"""Contrôle D — recevabilité : les accroches contre le socle du texte déposé.

Le rattachement est joué et ne se refait pas (39 acquis, 15 plaidables,
7 fragiles, 0 non rattachable). Ce contrôle est autre chose : il passe les
**accroches** et les **citations du texte en discussion** contre le socle du
projet de loi de finances pour 2027, n° 3210, relevé à
`referentiels/socle_texte_plf2027.json` — 90 articles, 8 annexes.

Les 538 citations du texte en discussion de la liasse n'avaient jamais été
passées au socle : le contrôle 1 du 20261008 les mettait hors contrôle, à bon
droit, parce qu'elles ne sont pas au droit en vigueur et ne peuvent pas être
cherchées à LEGI. Elles se cherchent ici.

| test | ce qu'il dit |
|---|---|
| **D1 — accroche introuvable** | l'article d'accroche n'est pas au socle |
| **D2 — accroche hors partie** | une pièce de première partie s'accroche à un article de la seconde |
| **D3 — citation introuvable** | une citation du texte en discussion ne résout pas au socle |
| **D4 — accroche divergente** | la pièce écrit une accroche autre que celle du registre |

Le socle est la **pièce qui fait foi**, et le contrôle le rouvre à chaque
verdict : il ne lit aucun fichier qu'il aurait écrit.
"""
import json
import os
import re

from liasse import ACCROCHES, RANGS, lire, normaliser, segments

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SOCLE = os.path.join(RACINE, 'referentiels', 'socle_texte_plf2027.json')

PREMIERE = 'PREMIÈRE PARTIE'


def socle():
    s = json.load(open(SOCLE, encoding='utf-8'))
    arts = {a['numero']: a for a in s['articles']}
    annexes = {(a.get('lettre') or a.get('id')): a for a in s['annexes']}
    return arts, annexes


ARTS, ANNEXES = socle()

# Les accroches écrites par la pièce, dans sa forme de cartouche d'amendement.
RE_ACCROCHE_ART = re.compile(r'^\s*>?\s*(?:\*\*)?`?ARTICLE\s+(\d+)\b|`ARTICLE\s+(\d+)`', re.M)
RE_ACCROCHE_ADD = re.compile(
    r"(?:APRÈS|APRES)\s+L[’']ARTICLE\s+(\d+)|art(?:icle)?\.?\s+add(?:itionnel)?\.?\s+"
    r"après\s+l[’']art(?:icle)?\.?\s+(\d+)", re.I)
RE_CITATION = re.compile(
    r"(?:l[’']|des\s+|aux\s+|à\s+l[’']|les\s+)?articles?\s+(\d+)(?:\s+(?:et|à)\s+(\d+))?"
    r"[^.;]{0,40}?(?:du\s+texte\s+déposé|du\s+projet\s+de\s+loi\s+de\s+finances\s+pour\s+2027"
    r"|du\s+présent\s+projet\s+de\s+loi)", re.I)


def controler(rang):
    texte = normaliser(lire(rang))
    seg = segments(texte, rang)
    ecarts = []

    def ec(test, libelle, detail):
        ecarts.append({'rang': rang, 'test': test, 'libelle': libelle, 'detail': detail})

    attendues = ACCROCHES[rang]

    # D1 et D2 — l'accroche du registre, passée au socle.
    for genre, num in attendues:
        a = ARTS.get(str(num))
        if a is None:
            ec('D1', 'accroche introuvable au socle du texte déposé n° 3210',
               f'{"ARTICLE" if genre == "article" else "art. add. après l’art."} {num}')
            continue
        partie = a.get('partie') or ''
        if not partie.startswith(PREMIERE):
            ec('D2', 'accroche hors de la première partie du texte déposé',
               f'article {num} — « {partie[:60]} »')

    # D4 — l'accroche que la pièce écrit, mesurée sur la pièce (R-H).
    # Elle se mesure **au dispositif**, qui est ce qui se dépose. Le cartouche
    # se confronte ensuite au dispositif : les deux ont déjà divergé, et un
    # contrôle qui réunit les deux textes ne voit jamais la divergence.
    def _ecrites(t):
        e = set()
        for m in RE_ACCROCHE_ART.finditer(t):
            e.add(('article', int(m.group(1) or m.group(2))))
        for m in RE_ACCROCHE_ADD.finditer(t):
            e.add(('additionnel', int(m.group(1) or m.group(2))))
        return e

    au_disp = _ecrites(seg['dispositif'])
    au_cart = _ecrites(seg['cartouche'])
    if not au_disp:
        ec('D4', 'le dispositif n’écrit aucune accroche',
           'registre : ' + ' · '.join(f'{g} {n}' for g, n in attendues))
    elif not (set(attendues) & au_disp):
        ec('D4', 'le dispositif écrit une accroche autre que celle du registre',
           'registre : ' + ' · '.join(f'{g} {n}' for g, n in attendues)
           + ' | dispositif : ' + ' · '.join(f'{g} {n}' for g, n in sorted(au_disp)))
    if au_cart and au_disp and not (au_cart & au_disp):
        ec('D4', 'le cartouche et le dispositif portent deux accroches différentes',
           'cartouche : ' + ' · '.join(f'{g} {n}' for g, n in sorted(au_cart))
           + ' | dispositif : ' + ' · '.join(f'{g} {n}' for g, n in sorted(au_disp)))

    # D3 — les citations du texte en discussion, cherchées au socle. Deux
    # formes : la citation en prose (« l'article 11 du texte déposé ») et la
    # forme d'accroche (« ARTICLE 42 », « APRÈS L'ARTICLE 33 »), qui est celle
    # que la liasse emploie le plus.
    controlees = 0
    for nom_seg in ('cartouche', 'dispositif', 'expose', 'interne'):
        t = seg[nom_seg]
        vus = []
        for m in RE_CITATION.finditer(t):
            for g in m.groups():
                if g:
                    vus.append((g, m.group(0)[:80], 'prose'))
        for m in RE_ACCROCHE_ART.finditer(t):
            vus.append((m.group(1) or m.group(2), m.group(0).strip(), 'accroche'))
        for m in RE_ACCROCHE_ADD.finditer(t):
            vus.append((m.group(1) or m.group(2), m.group(0).strip(), 'accroche'))
        for num, extrait, forme in vus:
            controlees += 1
            if str(num) not in ARTS:
                ec('D3', 'citation du texte en discussion introuvable au socle',
                   f'[{nom_seg}, {forme}] article {num} — « {extrait} »')
    return ecarts, controlees


def jouer():
    tout, n = [], 0
    for rang in sorted(RANGS):
        e, c = controler(rang)
        tout.extend(e)
        n += c
    return tout, n


if __name__ == '__main__':
    import collections
    e, n = jouer()
    print('citations du texte en discussion contrôlées au socle :', n)
    print('socle :', len(ARTS), 'articles ·', len(ANNEXES), 'annexes')
    c = collections.Counter(x['test'] for x in e)
    for k in ('D1', 'D2', 'D3', 'D4'):
        print(f'{k} {c.get(k, 0)}')
    for x in e:
        print(' ', x['rang'], x['test'], '|', x['libelle'][:55], '|', str(x['detail'])[:100])
