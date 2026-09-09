# -*- coding: utf-8 -*-
"""Contrôle de la restauration — R1 à R4.

Se joue en ouverture de session, juste après le dépliage, avant toute lecture et
toute génération. Il répond à une seule question : **ce qui vient d'être remis au
dépôt est-il bien ce que le coffre porte ?**

R1  divergence — un fichier présent dont l'empreinte ne concorde pas. C'est un
    faux. Il ne se corrige pas au dépôt : il se redemande au coffre, et si le
    coffre ne sait pas le rendre en octets, il ne s'emploie pas du tout.
R2  absence — un artefact qui n'a pas été restauré. Ce n'est pas une faute en
    soi : un fil n'a pas besoin de tout. Mais il se dit, et rien ne le cite.

Chaque artefact porte sa **voie** de restauration, et le relevé la nomme : le
coffre rend ses documents en texte au transcript, le dépôt rend l'appareil par
clone sous `chantier/` (A-395). Une divergence ne se lit pas de la même façon
sur les deux, et le contrôle le dit plutôt que de laisser chercher.
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

    # Les deux voies de restauration se contrôlent ensemble et se comptent à
    # part. Le coffre rend ses documents en texte ; le dépôt rend l'appareil par
    # clone. **Il n'y a plus d'archive** : jusqu'au 20260909 le bloc `archives`
    # ajoutait un attendu de plus, `technique/coffre.txt`, relevé à
    # `coffre/coffre.txt`. Il n'existe plus (A-395), et les quatre-vingts
    # fichiers qu'il portait se contrôlent désormais un par un, à leur chemin de
    # dépôt, contre leur propre empreinte.
    attendus = [a for a in index['artefacts'] if a['coffre'] and a['restaurable']]
    derives = {a['chemin'] for a in index['artefacts'] if a['rang'] == 'derive'}
    voies = {a['chemin']: a.get('voie', 'coffre') for a in index['artefacts']}

    diverge, rejouables, absents, hors, presents = [], [], [], [], 0
    for a in attendus:
        c = a['chemin']
        e = empreintes.relever(os.path.join(racine, c))
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

    par_voie = {}
    for a in attendus:
        par_voie.setdefault(voies.get(a['chemin'], 'coffre'), 0)
        par_voie[voies.get(a['chemin'], 'coffre')] += 1
    detail = ', '.join(f'{n} par le {v}' for v, n in sorted(par_voie.items()))
    print(f'{len(attendus)} artefact(s) attendu(s) — {detail} —, {presents} '
          f'présent(s) au dépôt, {len(table)} empreinte(s) de référence\n')

    print(f'R1 — {len(diverge)} divergence(s)')
    for c, att, obt in diverge:
        print(f'    {c}  [voie {voies.get(c, "coffre")}]')
        print(f'        attendu {att["octets"]} o, {att["lignes"]} l, '
              f'{att["sha256"][:16]}')
        print(f'        obtenu  {obt["octets"]} o, {obt["lignes"]} l, '
              f'{obt["sha256"][:16]}')
    # Une divergence ne se lit pas de la même façon sur les deux voies, et le
    # dire évite de chercher un faux là où il n'y en a pas. Sur la voie
    # `coffre`, le fichier restauré est un faux : il se redemande au coffre. Sur
    # la voie `depot`, l'octet vient d'un clone, donc il n'est pas douteux : ce
    # qui diverge, c'est le clone contre l'empreinte — le dépôt est en retard,
    # ou un fil a versé des empreintes sans pousser au dépôt. C'est A-346 vu
    # depuis l'autre bout, et c'est ce que `coffre.py dette` mesure.
    if any(voies.get(c) == 'depot' for c, _a, _o in diverge):
        print('    Une divergence de voie `depot` n\'est pas un faux du coffre : '
              'l\'octet vient\n    d\'un clone. Le dépôt est en retard, ou une '
              'empreinte a été versée sans\n    pousser. `appareil/coffre.py '
              'dette` dit lequel des deux.')
    print()

    print(f'R2 — {len(absents)} artefact(s) non restauré(s)')
    for c in sorted(absents):
        print(f'    {c}  [voie {voies.get(c, "coffre")}]')
    if any(voies.get(c) == 'depot' for c in absents):
        print('    Ce qui manque en voie `depot` ne se restaure pas du '
              'transcript : il se clone.')
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
