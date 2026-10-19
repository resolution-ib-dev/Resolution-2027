#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Joue les cinq modules de test de la machine et rend un bilan unique.

    python3 61_CONTROLE_jouer.py              tous les modules
    python3 61_CONTROLE_jouer.py docx droit   ceux-là seulement

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
RACINE = ICI

# Les pièces sont numérotées : le numéro porte l'ordre, le nom porte le sujet.
MODULES = [
    ("68_CONTROLE_atelier.py", "de quoi dispose cet atelier"),
    ("62_CONTROLE_integrite.py", "intégrité du paquet contre son manifeste"),
    ("63_CONTROLE_docx.py", "invariant de caractères de l'impression"),
    ("64_CONTROLE_droit.py", "base de droit et péremption des relevés"),
    ("65_CONTROLE_socles.py", "régénération des socles sur les textes déposés"),
    ("66_CONTROLE_recette.py", "recette de bout en bout sur le mini-lot"),
    ("67_CONTROLE_fuite.py", "aucune marque de l'atelier d'origine"),
    ("69_CONTROLE_doctrine.py", "aucun prélèvement nouveau ni majoré"),
]


def main(argv):
    choisis = [a for a in argv[1:] if not a.startswith("-")]
    a_jouer = [m for m in MODULES
               if not choisis or any(c in m[0] for c in choisis)]
    if choisis and not a_jouer:
        print("modules connus : " + " ".join(m for m, _ in MODULES))
        return 2

    print("=" * 72)
    print("MACHINE À AMENDEMENTS 2027 — chaîne de test")
    print("=" * 72)

    bilan = []
    for nom, libelle in a_jouer:
        chemin = os.path.join(ICI, nom)
        if not os.path.exists(chemin):
            # Les six modules sont nommés à MODULES : il en manque un, donc le
            # paquet est incomplet. Un module absent n'est pas une absence de
            # mesure, c'est un contrôle qu'on a perdu. Défaut relevé le
            # 20261016 : la chaîne le tolérait en silence et sortait verte.
            print(f"\n  ÉCHEC  module absent du paquet : {nom}")
            bilan.append((nom, 0, 1, 0))
            continue
        r = subprocess.run([sys.executable, chemin], capture_output=True,
                           text=True, cwd=RACINE)
        print(r.stdout, end="")
        if r.stderr.strip():
            print(r.stderr, end="")
        derniere = [l for l in r.stdout.splitlines() if l.strip().startswith("→")]
        p = e = ab = 0
        rendu = False
        if derniere:
            import re
            m = re.search(r"(\d+) passés, (\d+) échecs, (\d+) non joués",
                          derniere[-1])
            if m:
                p, e, ab = (int(x) for x in m.groups())
                rendu = True
        if nom == "68_CONTROLE_atelier.py":
            # Le contrôle 0 ne mesure pas la machine mais l'atelier : il rend une
            # voie, pas un compte. Son code de sortie dit si la voie est complète.
            print(f"  {'voie complète' if r.returncode == 0 else 'voie partielle — voir ci-dessus'}")
            bilan.append((nom, 1 if r.returncode == 0 else 0,
                          0, 0 if r.returncode == 0 else 1))
            continue
        if not rendu or (p == 0 and e == 0 and ab == 0):
            # Le module n'a rendu aucun verdict : il a planté avant de mesurer.
            # Ce n'est pas un succès, c'est un échec, et le code de sortie le dit.
            print(f"  ÉCHEC  le module n'a rendu aucun verdict — il a planté "
                  f"avant de mesurer (code {r.returncode})")
            e = max(e, 1)
        bilan.append((nom, p, e, ab))

    print("\n" + "=" * 72)
    print("BILAN")
    print("=" * 72)
    tp = te = ta = 0
    for nom, p, e, ab in bilan:
        tp, te, ta = tp + p, te + e, ta + ab
        etat = "ÉCHEC" if e else ("incomplet" if ab else "vert")
        print(f"  {nom[:26]:28} {p:3} passés  {e:3} échecs  {ab:3} non joués   {etat}")
    print(f"  {'TOTAL':28} {tp:3} passés  {te:3} échecs  {ta:3} non joués")

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
