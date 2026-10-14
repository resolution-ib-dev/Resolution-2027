# -*- coding: utf-8 -*-
"""Tirage de la colonne de première partie, au gabarit du 20261008.

**Support de revue, et rien d'autre.** Il ne remplace aucune pièce du corpus et
ne se verse pas : les pièces font foi, le tirage les montre dans l'ordre de la
colonne à un état donné.

Le gabarit est pris sur le tirage du 20261008 — titres de rang et accroches lus
sur lui, jamais réécrits. Le corps vient des pièces à leur état courant : clause
renumérotée à 389 rangs, 31 rangs à la liasse, P1-29 hors colonne.

Deux fichiers portent deux amendements : la pièce de solde (P1-30) et la pièce
des dotations (P1-32). Le gabarit les rend en deux blocs « a » et « b », et le
tirage les suit.
"""
import os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RACINE, 'appareil', 'fil1_verification'))
import liasse                                                   # noqa

GABARIT = os.path.join(RACINE, 'livrables', 'depot_2027', 'LIASSE_P1_20261008.md')
SORTIE = os.path.join(RACINE, 'livrables', 'tirage_P1_20261009.md')
FIN_DEPOSABLE = re.compile(r'^\s*(?:#{1,6}\s*)?(?:\*\*)?\[interne\]|^\s*#{1,6}\s*ANNEXE\b', re.M)
# Après l'exposé sommaire, le déposable s'arrête au premier titre de section non
# cité : les pièces portent ensuite leurs fiches de liasse et de vecteur, qui
# sont de l'appareil. Sans cette coupe, la pièce 4.3 faisait entrer deux fiches
# et leurs tableaux dans le tirage.
TITRE_HORS_CITATION = re.compile(r'^#{1,6}\s+\S', re.M)
MARQUE_EXPOSE = re.compile(r'^\s*>?\s*(?:#{1,6}\s*)?(?:\*\*)?EXPOS[EÉ] SOMMAIRE', re.M)
JOUR = '9 octobre 2026'


def tetes():
    """rang (ou « rang a » / « rang b ») -> (intitulé, accroche), pris au gabarit."""
    out = {}
    for b in open(GABARIT, encoding='utf-8').read().split('\\newpage'):
        m = re.match(r'\s*## (P1-\d\d(?: [ab])?) — (.+?)\n\n\*(.+?)\*\n', b)
        if m:
            out[m.group(1)] = (m.group(2), m.group(3))
    return out


def _deciter(t):
    """Retire la citation markdown : le dispositif se lit au fil du texte."""
    lignes = []
    for l in t.split('\n'):
        lignes.append(re.sub(r'^>\s?', '', l))
    return '\n'.join(lignes)


def corps(rang):
    """Les blocs déposables du rang : dispositif et exposé, sans bloc interne."""
    t = liasse.normaliser(liasse.lire(rang))
    blocs = liasse.dispositifs(t, rang)
    if rang in liasse.DECOUPE:
        a = re.compile(liasse.DECOUPE[rang][0], re.M).search(t)
        b = re.compile(liasse.DECOUPE[rang][1], re.M).search(t, a.end()) if a else None
        fin_div = b.start() if b else len(t)
    else:
        fin_div = len(t)
    out = []
    for i, (deb, _f) in enumerate(blocs):
        suite = blocs[i + 1][0] if i + 1 < len(blocs) else fin_div
        span = t[deb:suite]
        m = FIN_DEPOSABLE.search(span)
        if m:
            span = span[:m.start()]
        me = MARQUE_EXPOSE.search(span)
        if me:
            mt = TITRE_HORS_CITATION.search(span, me.end())
            if mt:
                span = span[:mt.start()]
        out.append(_deciter(span).strip())
    return out


def construire():
    T = tetes()
    rangs = sorted(liasse.RANGS)
    pages = ["""**LIASSE DÉPOSABLE — PLF 2027, PREMIÈRE PARTIE**

**Véhicule** — Projet de loi de finances pour 2027, **n° 3210**, déposé le 1er octobre 2026 \
(Assemblée nationale, 17e législature) — **première partie**.

**Texte visé** — PLF 2027 — première partie.

**Amendements de la liasse** : **31 rangs, 33 amendements**.

**Tirage du %s.** Il porte la clause générale renumérotée à **389 rangs** au III, \
et **P1-29 reste hors colonne**.

**Support de revue.** Il ne remplace aucune pièce du corpus : les pièces font foi, \
le tirage les montre dans l’ordre de la colonne.

Droit en vigueur lu sur l’extrait LEGI, millésime **20261007**.
""" % JOUR]
    # L'encart de réserves est du contenu propre à la colonne, non un dérivé des
    # pièces : il se reprend du gabarit par copie d'octets, jamais réécrit.
    for b in open(GABARIT, encoding='utf-8').read().split('\\newpage'):
        if b.lstrip().startswith('# Encart de réserves'):
            # Repris du tirage du 20261008 par copie d'octets. Une de ses
            # réserves est tombée depuis : le regroupement par bloc est joué, et
            # le III ne porte plus 396 rangs mais 389. Le constat se dit, la
            # réserve ne se réécrit pas.
            note = ('*Encart repris du tirage du 8 octobre 2026. Sa réserve sur le '
                    'regroupement des abrogations est levée : le regroupement est joué '
                    'depuis le 9 octobre 2026, et le III porte 389 rangs.*\n\n')
            pages.append(b.strip().replace('\n', '\x00', 1).replace('\x00', '\n\n' + note, 1))
            break
    manquants = []
    for rang in rangs:
        blocs = corps(rang)
        cles = [rang] if len(blocs) == 1 else [f'{rang} a', f'{rang} b']
        for cle, b in zip(cles, blocs):
            titre, accroche = T.get(cle, (liasse.RANGS[rang][1], ''))
            if cle not in T:
                manquants.append(cle)
            pages.append(f'## {cle} — {titre}\n\n*{accroche}*\n\n{b}\n')
    return '\n\\newpage\n\n'.join(pages) + '\n', manquants


if __name__ == '__main__':
    txt, manquants = construire()
    open(SORTIE, 'w', encoding='utf-8').write(txt)
    n = txt.count('\\newpage')
    print(f'{SORTIE} · {len(txt.encode())} octets · {n} sauts de page · '
          f'{txt.count(chr(10) + "## P1-")} blocs d\'amendement')
    if manquants:
        print('titres absents du gabarit :', manquants)
