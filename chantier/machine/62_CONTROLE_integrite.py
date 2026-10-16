#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test 1 — intégrité du paquet contre son manifeste.

Ce que le test prouve : chaque pièce du paquet est à l'octet celle que le
manifeste déclare, et le paquet ne porte aucune pièce que le manifeste ignore.

Pourquoi il existe. La version 1.4 a été livrée en zip avec un manifeste exact,
et cinq de ses pièces n'existaient plus nulle part ailleurs : le manifeste est
resté, les pièces non. Ce test fait du manifeste la pièce qui commande — ce qui
en diverge se dit, et rien ne se livre sans lui.

Usage : python3 62_CONTROLE_integrite.py
"""
import os
import sys

import importlib.util as _iu


def _charger(nom_fichier, nom_module):
    """Charge un module dont le nom de fichier commence par un chiffre.

    Les pièces sont numérotées pour porter l'ordre de lecture ; un module Python
    ne peut pas commencer par un chiffre. On charge donc par chemin.
    """
    c = os.path.join(os.path.dirname(os.path.abspath(__file__)), nom_fichier)
    sp = _iu.spec_from_file_location(nom_module, c)
    m = _iu.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


_socle = _charger("60_CONTROLE_socle.py", "socle_tests")
RACINE, Journal = _socle.RACINE, _socle.Journal
empreinte, octets, lire_manifeste = (_socle.empreinte, _socle.octets,
                                     _socle.lire_manifeste)

# Le manifeste ne figure pas à sa propre table.
HORS_COMPTE = {"99_MANIFESTE.md"}

# Les outils de la tranche 10–20 appartiennent à l'utilisateur : il les lit, il
# les modifie, et c'est l'usage prévu. Une divergence s'y NOTE ; elle n'échoue
# pas. Partout ailleurs — procédures, scripts, contrôles, références — une
# divergence est un échec : c'est la méthode, et elle ne se modifie pas sans le
# savoir. Défaut relevé le 20261016 : la chaîne déclarait « ne se livre pas »
# pour une modification légitime d'un outil.
def _a_lui(nom):
    t = nom[:2]
    return t.isdigit() and 10 <= int(t) <= 20


def main():
    j = Journal("Test 1 — intégrité du paquet contre son manifeste")
    chemin = os.path.join(RACINE, "99_MANIFESTE.md")
    if not os.path.exists(chemin):
        j.absent("manifeste lisible", "99_MANIFESTE.md")
        return j.rendre()
    table = lire_manifeste(chemin)
    if not table:
        j.echoue("le manifeste porte un tableau de pièces", "0 ligne lue")
        return j.rendre()
    j.passe("manifeste lu", f"{len(table)} pièces déclarées")

    # 1. chaque pièce déclarée est présente et conforme
    manquantes = divergentes = a_lui = 0
    for rel, (h, n) in sorted(table.items()):
        p = os.path.join(RACINE, rel)
        if not os.path.exists(p):
            j.echoue(f"présente : {rel}", "absente du paquet")
            manquantes += 1
            continue
        o, e = octets(p), empreinte(p)
        if o != n or e != h:
            if _a_lui(rel):
                j.passe(f"outil modifié par vous : {rel}",
                        f"{n} → {o} o — gardé tel quel")
                a_lui += 1
            else:
                j.echoue(f"conforme : {rel}",
                         f"manifeste {n} o / {h} — jeu {o} o / {e}")
                divergentes += 1
    if not manquantes and not divergentes:
        j.passe("la méthode est conforme à l'octet",
                f"{len(table) - a_lui} sur {len(table)}"
                + (f", {a_lui} outil(s) à vous" if a_lui else ""))

    # 2. aucune pièce du paquet n'échappe au manifeste
    sur_disque = {f for f in os.listdir(RACINE)
                  if os.path.isfile(os.path.join(RACINE, f))
                  and f not in HORS_COMPTE}
    non_declarees = sorted(sur_disque - set(table))
    if non_declarees:
        for rel in non_declarees:
            j.echoue(f"déclarée au manifeste : {rel}", "présente, non déclarée")
    else:
        j.passe("aucune pièce non déclarée", f"{len(sur_disque)} fichiers")

    return j.rendre()


if __name__ == "__main__":
    sys.exit(main())
