# -*- coding: utf-8 -*-
"""Contrôle de la restauration — R1 à R4.

Se joue en ouverture de session, juste après le dépliage, avant toute lecture et
toute génération. Il répond à une seule question : **ce qui vient d'être remis au
dépôt est-il bien ce que le coffre porte ?**

R1  divergence — un fichier présent dont l'empreinte ne concorde pas. C'est un
    faux. Il ne se corrige pas au dépôt : il se redemande au coffre, et si le
    coffre ne sait pas le rendre en octets, il ne s'emploie pas du tout.
R2  absence — un artefact du coffre qui n'a pas été restauré. Ce n'est pas une
    faute en soi : un fil n'a pas besoin de tout. Mais il se dit, et rien ne le
    cite.
R3  hors empreinte — un artefact du coffre restaurable qu'aucune empreinte ne
    couvre. Le versement l'a manqué, ou il est né depuis.
R4  sans empreinte — le relevé ne l'a jamais vu : rien à quoi comparer.
R5  dérivé divergent — un dérivé n'est pas un faux : il se régénère. Certains
    horodatent leur pied de page, et divergeraient à chaque session. Ils sortent
    de R1 pour ne pas noyer ce qui compte, et `make` les remet d'aplomb.

Sortie non nulle dès qu'un R1 existe. Une session qui continue sur un R1 travaille
sur un faux.

Usage : python3 controle_restauration.py ../methode/index.json ../methode/empreintes.json ..
"""
import json
import os
import sys

import empreintes


def main(argv):
    index = json.load(open(argv[1], encoding='utf-8'))
    racine = argv[3] if len(argv) > 3 else '.'
    try:
        ref = json.load(open(argv[2], encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        print(f'R0 — le fichier d\'empreintes ne se lit pas : {exc}')
        print('    Aucune restauration ne peut être contrôlée. Arrêt.')
        return 1
    table = ref.get('empreintes', {})
    declares_absents = set(ref.get('sans_empreinte', []))

    attendus = [a for a in index['artefacts'] if a['coffre'] and a['restaurable']]
    attendus += [{'chemin': arch['chemin_coffre'], 'restaurable': True,
                  'coffre': True, 'rang': 'appareil'}
                 for arch in index['archives']]
    derives = {a['chemin'] for a in index['artefacts'] if a['rang'] == 'derive'}

    diverge, rejouables, absents, hors, presents = [], [], [], [], 0
    for a in attendus:
        c = a['chemin']
        chemin = os.path.join(racine, c)
        if c in table and c.startswith('technique/'):
            chemin = os.path.join(racine, 'coffre', os.path.basename(c))
        e = empreintes.relever(chemin)
        if e is None:
            if c not in declares_absents:
                absents.append(c)
            continue
        presents += 1
        if c not in table:
            if c != 'methode/empreintes.json':
                hors.append(c)
        elif e['sha256'] != table[c]['sha256']:
            (rejouables if c in derives else diverge).append((c, table[c], e))

    print(f'{len(attendus)} artefact(s) attendu(s), {presents} présent(s) au '
          f'dépôt, {len(table)} empreinte(s) de référence\n')

    print(f'R1 — {len(diverge)} divergence(s)')
    for c, att, obt in diverge:
        print(f'    {c}')
        print(f'        attendu {att["octets"]} o, {att["lignes"]} l, '
              f'{att["sha256"][:16]}')
        print(f'        obtenu  {obt["octets"]} o, {obt["lignes"]} l, '
              f'{obt["sha256"][:16]}')
    print()

    print(f'R2 — {len(absents)} artefact(s) du coffre non restauré(s)')
    for c in sorted(absents):
        print(f'    {c}')
    print()

    print(f'R3 — {len(hors)} artefact(s) restauré(s) hors empreinte')
    for c in sorted(hors):
        print(f'    {c}')
    print()

    print(f'R4 — {len(declares_absents)} artefact(s) sans empreinte de référence')
    for c in sorted(declares_absents):
        print(f'    {c}')
    print()

    print(f'R5 — {len(rejouables)} dérivé(s) divergent(s), à régénérer par `make`')
    for c, att, obt in rejouables:
        print(f'    {c} — {att["octets"]} o attendus, {obt["octets"]} o obtenus')
    print()

    if diverge:
        print(f'{len(diverge)} faux au dépôt. Ils ne s\'emploient pas, ils se '
              f'redemandent au coffre.')
        return 1
    print('Aucune divergence. Ce qui est au dépôt est ce que le coffre porte.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
