#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Relève le tableau des pièces du manifeste, sans toucher à son texte.

Le manifeste porte deux parties : un texte, écrit à la main, qui dit ce que la
version change et ce qu'elle déclare ; et un tableau des pièces, qui se relève.
Ce script **ne réécrit que le tableau** — tout ce qui précède la ligne de tête
est recopié tel quel.

Pourquoi il existe : `62_CONTROLE_integrite.py` fait du manifeste la pièce qui
commande. Un manifeste qu'on ne peut pas recaler mécaniquement après une
correction devient faux à la première passe, et un manifeste faux vaut moins que
pas de manifeste.

    python3 90_SCRIPT_relever_manifeste.py          recale le tableau
    python3 90_SCRIPT_relever_manifeste.py --juger  dit l'écart sans rien écrire
"""
import hashlib
import os
import re
import sys

RACINE = os.path.dirname(os.path.abspath(__file__))
MANIFESTE = os.path.join(RACINE, "99_MANIFESTE.md")
TETE = "| fichier | octets | sha256 |"
HORS_COMPTE = {"99_MANIFESTE.md"}


def relever():
    # Le paquet est plat : un sous-dossier est étranger au paquet.
    lignes = []
    for f in sorted(os.listdir(RACINE)):
        p = os.path.join(RACINE, f)
        if not os.path.isfile(p) or f in HORS_COMPTE:
            continue
        b = open(p, "rb").read()
        lignes.append((f, len(b), hashlib.sha256(b).hexdigest()[:16]))
    return sorted(lignes)


def main(argv):
    if not os.path.exists(MANIFESTE):
        print("99_MANIFESTE.md absent — il s'écrit à la main, ce script le recale",
              file=sys.stderr)
        return 2
    pieces = relever()
    total = sum(p[1] for p in pieces)
    texte = open(MANIFESTE, encoding="utf-8").read()

    anciennes = dict(
        (m.group(1), (int(m.group(2)), m.group(3)))
        for m in re.finditer(r"^\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*`([0-9a-f]+)`",
                             texte, re.M))
    nouvelles = {p[0]: (p[1], p[2]) for p in pieces}
    ajoutees = sorted(set(nouvelles) - set(anciennes))
    retirees = sorted(set(anciennes) - set(nouvelles))
    changees = sorted(k for k in set(anciennes) & set(nouvelles)
                      if anciennes[k] != nouvelles[k])

    if "--juger" in argv:
        for k in ajoutees:
            print(f"  AJOUTÉE  {k}  {nouvelles[k][0]} o")
        for k in retirees:
            print(f"  RETIRÉE  {k}")
        for k in changees:
            print(f"  CHANGÉE  {k}  {anciennes[k][0]} → {nouvelles[k][0]} o")
        print(f"\n{len(pieces)} pièces, {total} octets — "
              f"{len(ajoutees)} ajoutées, {len(retirees)} retirées, "
              f"{len(changees)} changées")
        return 1 if (ajoutees or retirees or changees) else 0

    avant = texte.split(TETE)[0].rstrip()
    # Le séparateur de milliers est une espace insécable : une seule espace
    # suivie de trois chiffres, jamais une virgule.
    avant, n = re.subn(
        r"\*\*Jeu\*\* : [\d\s\u00a0]+ pièces, [\d\s\u00a0]+ octets\.",
        "**Jeu** : {} pièces, {} octets.".format(
            len(pieces), f"{total:,}".replace(",", "\u00a0")),
        avant)
    if n != 1:
        print("la ligne « Jeu » du manifeste n'a pas ete recalee — "
              "elle s'ecrit « **Jeu** : N pièces, N octets. »",
              file=sys.stderr)
        return 2
    corps = [avant, "", TETE, "|---|---:|---|"]
    corps += [f"| `{rel}` | {n} | `{h}` |" for rel, n, h in pieces]
    open(MANIFESTE, "w", encoding="utf-8").write("\n".join(corps) + "\n")
    print(f"tableau recalé — {len(pieces)} pièces, {total} octets "
          f"({len(ajoutees)} ajoutées, {len(retirees)} retirées, "
          f"{len(changees)} changées)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
