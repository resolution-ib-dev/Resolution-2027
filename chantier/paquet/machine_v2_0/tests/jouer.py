#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Joue les cinq modules de test de la machine et rend un bilan unique.

    python3 tests/jouer.py              tous les modules
    python3 tests/jouer.py docx droit   ceux-là seulement

**Lecture du bilan, et c'est la règle qui compte** :

- `ÉCHEC` — une mesure a eu lieu et elle contredit l'attendu. **La machine ne se
  livre pas.**
- `ABSENT` — la mesure n'a pas eu lieu, faute d'une pièce. Ce n'est pas un
  succès. Le bilan nomme ce qui manque, et c'est à l'auteure de dire si
  l'absence est irréductible — auquel cas elle se **déclare** au manifeste et
  n'empêche pas de livrer — ou si la pièce doit être jointe.
- `PASSE` — la mesure a eu lieu et elle concorde.

Le code de sortie est 1 dès qu'un module porte un échec, 0 sinon. Un `ABSENT`
seul ne fait pas échouer la chaîne : il la rend incomplète, et le bilan le dit
en toutes lettres.
"""
import importlib
import os
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)

MODULES = [
    ("integrite", "intégrité du paquet contre son manifeste"),
    ("docx", "invariant de caractères de l'impression"),
    ("droit", "base de droit et péremption des relevés"),
    ("socles", "régénération des socles sur les textes enregistrés"),
    ("recette", "recette de bout en bout sur le mini-lot"),
]


def main(argv):
    choisis = [a for a in argv[1:] if not a.startswith("-")]
    a_jouer = [m for m in MODULES if not choisis or m[0] in choisis]
    if choisis and not a_jouer:
        print(f"modules connus : {', '.join(m for m, _ in MODULES)}")
        return 2

    print("=" * 72)
    print("MACHINE À AMENDEMENTS 2027 — chaîne de test")
    print("=" * 72)

    bilan = []
    for nom, libelle in a_jouer:
        chemin = os.path.join(ICI, f"test_{nom}.py")
        if not os.path.exists(chemin):
            print(f"\n  module absent : test_{nom}.py")
            bilan.append((nom, None, None, None))
            continue
        r = subprocess.run([sys.executable, chemin], capture_output=True,
                           text=True, cwd=RACINE)
        print(r.stdout, end="")
        if r.stderr.strip():
            print(r.stderr, end="")
        derniere = [l for l in r.stdout.splitlines() if l.strip().startswith("→")]
        p = e = ab = 0
        if derniere:
            import re
            m = re.search(r"(\d+) passés, (\d+) échecs, (\d+) non joués",
                          derniere[-1])
            if m:
                p, e, ab = (int(x) for x in m.groups())
        bilan.append((nom, p, e, ab))

    print("\n" + "=" * 72)
    print("BILAN")
    print("=" * 72)
    tp = te = ta = 0
    for nom, p, e, ab in bilan:
        if p is None:
            print(f"  {nom:12} module absent")
            continue
        tp, te, ta = tp + p, te + e, ta + ab
        etat = "ÉCHEC" if e else ("incomplet" if ab else "vert")
        print(f"  {nom:12} {p:3} passés  {e:3} échecs  {ab:3} non joués   {etat}")
    print(f"  {'TOTAL':12} {tp:3} passés  {te:3} échecs  {ta:3} non joués")

    if te:
        print("\n  La machine ne se livre pas : un échec est une mesure qui "
              "contredit l'attendu.")
    elif ta:
        print("\n  Aucun échec. Des mesures n'ont pas eu lieu : les déclarer au "
              "manifeste avant de livrer.")
    else:
        print("\n  Chaîne verte de bout en bout.")
    return 1 if te else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
