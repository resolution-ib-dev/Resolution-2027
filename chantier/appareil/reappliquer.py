# -*- coding: utf-8 -*-
"""Contrôle de réapplication — la forme modificative, rejouée sur A, redonne C.

C'est le seul endroit de la chaîne où une sortie rédigée se prouve. On n'y juge
rien : soit la réapplication redonne le texte révisé à l'octet, soit la forme
modificative est fausse.

La forme modificative s'écrit en opérations typées, une par ligne de la
disposition. Chaque opération porte le fragment EXACT du texte de départ sur
lequel elle mord — pas une paraphrase, pas un numéro d'alinéa seul. Un fragment
qui n'apparaît pas une fois et une seule dans A fait lever : c'est une adresse
ambiguë, et une adresse ambiguë en séance se lit de deux façons.

Opérations :

  {"op": "abroger"}                                       C est vide
  {"op": "supprimer",  "fragment": "..."}                 retire le fragment
  {"op": "remplacer",  "fragment": "...", "par": "..."}    échange le fragment
  {"op": "inserer_apres", "fragment": "...", "texte": "..."}
  {"op": "completer",  "texte": "..."}                    ajoute en fin de texte

Usage : python3 reappliquer.py cas.json
        {"a": "<texte en vigueur>", "c": "<texte révisé>", "forme": [ ... ]}
        sortie non nulle dès qu'un cas échoue.
"""
import json
import sys


class Ambigu(Exception):
    pass


def _unique(texte, fragment):
    n = texte.count(fragment)
    if n == 0:
        raise Ambigu(f'fragment absent du texte de départ : {fragment[:60]!r}')
    if n > 1:
        raise Ambigu(f'fragment présent {n} fois — adresse ambiguë : '
                     f'{fragment[:60]!r}')
    return texte.index(fragment)


def appliquer(a, forme):
    """Rejoue la forme modificative sur le texte de départ."""
    c = a
    for o in forme:
        op = o['op']
        if op == 'abroger':
            c = ''
        elif op == 'supprimer':
            i = _unique(c, o['fragment'])
            c = c[:i] + c[i + len(o['fragment']):]
        elif op == 'remplacer':
            i = _unique(c, o['fragment'])
            c = c[:i] + o['par'] + c[i + len(o['fragment']):]
        elif op == 'inserer_apres':
            i = _unique(c, o['fragment'])
            j = i + len(o['fragment'])
            c = c[:j] + o['texte'] + c[j:]
        elif op == 'completer':
            c = c + o['texte']
        else:
            raise Ambigu(f'opération inconnue : {op}')
    return c


def controler(cas):
    """Rend (verdict, détail). Le verdict est le seul résultat qui compte."""
    try:
        obtenu = appliquer(cas['a'], cas['forme'])
    except Ambigu as exc:
        return 'AMBIGU', str(exc)
    if obtenu == cas['c']:
        return 'PROUVE', f'{len(obtenu)} o à l\'octet'
    # Où ça décroche, pour que la correction ne se cherche pas à l'œil.
    n = next((k for k in range(min(len(obtenu), len(cas['c'])))
              if obtenu[k] != cas['c'][k]), min(len(obtenu), len(cas['c'])))
    return 'ECHEC', (f'divergence au caractère {n} — obtenu '
                     f'{obtenu[n:n + 50]!r}, attendu {cas["c"][n:n + 50]!r}')


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    echecs = 0
    for chemin in argv[1:]:
        charge = json.load(open(chemin, encoding='utf-8'))
        cas = charge if isinstance(charge, list) else [charge]
        for c in cas:
            verdict, detail = controler(c)
            print(f'{verdict:7} {c.get("intitule", chemin)} — {detail}')
            if verdict != 'PROUVE':
                echecs += 1
    return 1 if echecs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
