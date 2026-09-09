# -*- coding: utf-8 -*-
"""Contrôle du chaînage des notes de fin.

Deux contrôles, dans les deux sens.

N1 — toute note citée par un référentiel existe au relevé. Une citation d'une
note disparue signale un référentiel en retard sur le manuscrit.

N2 — toute note portant un chiffre est citée quelque part. C'est le contrôle
utile : il signale les raisonnements chiffrés du manuscrit que les référentiels
n'ont pas repris. Sans lui, une note comme celle qui chiffre le coût d'une
rupture d'accès au crédit souverain reste invisible jusqu'à ce que quelqu'un
la lise par hasard.

Usage : python3 controle_notes.py Notes.json REF.json [Positions.json ...]
"""
import json, re, sys

CITATION = re.compile(r'\be(\d{1,3})(?:\.\d+)?\b')


def citees(chemin):
    """Identifiants de notes cités dans un fichier JSON, où qu'ils soient."""
    s = open(chemin, encoding='utf-8').read()
    return {'e' + m.group(1) for m in CITATION.finditer(s)}


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    releve = json.load(open(argv[1], encoding='utf-8'))
    if isinstance(releve, dict) and 'notes' in releve:
        releve = releve['notes']
    notes = {n['id']: n for n in releve}

    cite = {}
    for chemin in argv[2:]:
        for i in citees(chemin):
            cite.setdefault(i, []).append(chemin.split('/')[-1])

    # N1
    fantomes = sorted(set(cite) - set(notes),
                      key=lambda x: int(x[1:]))
    # N2
    muettes = sorted((i for i, n in notes.items()
                      if n['porte_un_chiffre'] and i not in cite),
                     key=lambda x: int(x[1:]))

    print(f"{len(notes)} notes au relevé, {len(cite)} citées par "
          f"{len(argv) - 2} référentiel(s)")
    print(f"N1 — {len(fantomes)} citation(s) sans note correspondante")
    for i in fantomes:
        print(f"    {i} cité par {', '.join(cite[i])}")
    print(f"N2 — {len(muettes)} note(s) chiffrée(s) qu'aucun référentiel ne cite")
    for i in muettes:
        print(f"    {i} [{notes[i]['section'][:40]}] {notes[i]['texte'][:110]}")
    return 1 if fantomes else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
