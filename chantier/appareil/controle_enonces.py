# -*- coding: utf-8 -*-
"""Contrôle des énoncés d'entrée de l'éval — la règle, jouée et non tenue à l'œil.

`methode/regle_enonces_eval.md` dit ce qu'un énoncé ne porte jamais. Une règle
qu'on vérifie en relisant se perd au dixième cas ; celle-ci se joue.

Quatre contrôles, et le premier est le seul qui compte vraiment :

  E1  aucun verbe de la grammaire modificative
  E2  aucun marqueur de subdivision
  E3  l'article visé nommé au moins une fois
  E4  longueur — de 15 à 120 mots

Un énoncé qui sort se réécrit avant que la skill soit jouée. Après, il est trop
tard : on ne réécrit pas une entrée en sachant ce qu'elle a produit.

Usage : python3 controle_enonces.py ../livrables/eval_disposition/enonces.json
"""
import json
import re
import sys

VERBES = [
    'abrog', 'supprim', 'remplac', 'insér', 'inser', 'complèt', 'complet',
    'rétabli', 'retabli', 'réécri', 'reecri', 'récriv', 'ainsi rédigé',
    'ainsi modifié', 'est ainsi', 'sont ainsi', 'substitu', 'ajout',
]

SUBDIVISIONS = [
    re.compile(r'\b\d+°'),
    re.compile(r'\b[a-z]\s?\)\s'),
    re.compile(r'\b(premier|deuxième|troisième|quatrième|cinquième|sixième|'
               r'septième|huitième|neuvième|dixième|dernier|avant-dernier)\s+'
               r'alinéa', re.I),
    re.compile(r'\balinéas?\b', re.I),
    re.compile(r'\b(première|deuxième|dernière)\s+phrase', re.I),
    re.compile(r'\ble\s+[IVX]+\b'),
    re.compile(r'\bdu\s+[IVX]+\s+de\b'),
]

MOTS_MIN, MOTS_MAX = 15, 120


def controler(cas):
    """Rend la liste des anomalies d'un cas. Vide si l'énoncé tient."""
    e = cas.get('enonce')
    if cas.get('indicible'):
        return []
    if not e:
        return [('E0', 'énoncé absent')]
    bas = e.lower()
    a = []
    for v in VERBES:
        if v in bas:
            a.append(('E1', f'verbe de la grammaire modificative : {v!r}'))
    for rx in SUBDIVISIONS:
        m = rx.search(e)
        if m:
            a.append(('E2', f'marqueur de subdivision : {m.group(0)!r}'))
    for ad in cas.get('adresse_donnee', []):
        num = ad.get('article', '')
        premier = num.split(' et ')[0].split(',')[0].strip()
        if premier and premier not in e:
            a.append(('E3', f'article non nommé : {premier!r}'))
    n = len(e.split())
    if not MOTS_MIN <= n <= MOTS_MAX:
        a.append(('E4', f'{n} mots, hors des bornes {MOTS_MIN}–{MOTS_MAX}'))
    return a


def main(chemin):
    d = json.load(open(chemin, encoding='utf-8'))
    total, fautifs, indicibles = 0, 0, 0
    par_code = {}
    for c in d['cas']:
        total += 1
        if c.get('indicible'):
            indicibles += 1
            continue
        an = controler(c)
        if an:
            fautifs += 1
            print(f"  {c['cle']}")
            for code, msg in an:
                print(f'      {code} — {msg}')
                par_code[code] = par_code.get(code, 0) + 1
    print(f'{total} énoncé(s), {indicibles} déclaré(s) indicible(s), '
          f'{fautifs} en anomalie')
    for code in sorted(par_code):
        print(f'    {code} — {par_code[code]}')
    return 1 if fautifs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
