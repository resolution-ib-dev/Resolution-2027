#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test 1 — intégrité du paquet contre son manifeste.

Ce que le test prouve : chaque pièce du paquet est à l'octet celle que le
manifeste déclare, et le paquet ne porte aucune pièce que le manifeste ignore.

Pourquoi il existe. La version 1.4 a été livrée en zip avec un manifeste exact,
et cinq de ses pièces n'existaient plus nulle part ailleurs : le manifeste est
resté, les pièces non. Ce test fait du manifeste la pièce qui commande — ce qui
en diverge se dit, et rien ne se livre sans lui.

Usage : python3 tests/test_integrite.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from socle import (RACINE, Journal, empreinte, lire_manifeste, octets)

HORS_COMPTE = {"MANIFESTE.md"}


def main():
    j = Journal("Test 1 — intégrité du paquet contre son manifeste")
    chemin = os.path.join(RACINE, "MANIFESTE.md")
    if not os.path.exists(chemin):
        j.absent("manifeste lisible", "MANIFESTE.md")
        return j.rendre()
    table = lire_manifeste(chemin)
    if not table:
        j.echoue("le manifeste porte un tableau de pièces", "0 ligne lue")
        return j.rendre()
    j.passe("manifeste lu", f"{len(table)} pièces déclarées")

    # 1. chaque pièce déclarée est présente et conforme
    manquantes = divergentes = 0
    for rel, (h, n) in sorted(table.items()):
        p = os.path.join(RACINE, rel)
        if not os.path.exists(p):
            j.echoue(f"présente : {rel}", "absente du paquet")
            manquantes += 1
            continue
        o, e = octets(p), empreinte(p)
        if o != n or e != h:
            j.echoue(f"conforme : {rel}",
                     f"manifeste {n} o / {h} — paquet {o} o / {e}")
            divergentes += 1
    if not manquantes and not divergentes:
        j.passe("toutes les pièces déclarées sont conformes à l'octet",
                f"{len(table)} sur {len(table)}")

    # 2. aucune pièce du paquet n'échappe au manifeste
    sur_disque = set()
    for r, dirs, files in os.walk(RACINE):
        dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git")]
        for f in files:
            rel = os.path.relpath(os.path.join(r, f), RACINE)
            if rel not in HORS_COMPTE:
                sur_disque.add(rel)
    non_declarees = sorted(sur_disque - set(table))
    if non_declarees:
        for rel in non_declarees:
            j.echoue(f"déclarée au manifeste : {rel}", "présente, non déclarée")
    else:
        j.passe("aucune pièce non déclarée", f"{len(sur_disque)} fichiers")

    return j.rendre()


if __name__ == "__main__":
    sys.exit(main())
