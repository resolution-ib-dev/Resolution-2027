#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle 0 — de quoi dispose cet atelier.

**Il se joue avant tous les autres**, et il est le seul qui ne mesure pas la
machine : il mesure l'endroit où elle va tourner. Sans lui, un assistant
découvre les manques un par un, à l'étape où chacun bloque — et l'utilisateur
croit la machine cassée quand c'est son atelier qui est nu.

Il rend une **voie** :

    A  terminal complet   git + python3 + python-docx → la chaîne entière
    B  terminal nu        python3 sans git ou sans python-docx → chaîne partielle
    C  pas de terminal    ce contrôle ne s'est pas joué du tout

**La voie C ne se détecte pas d'ici.** Si vous lisez ce fichier sans pouvoir
l'exécuter, vous êtes en C : allez au § « Voie B » de `01_DEMARRER.md`, qui
couvre les deux.

Usage : python3 68_CONTROLE_atelier.py
"""
import os
import shutil
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))

V, R, J, G, N = "\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[0m"
if not sys.stdout.isatty():
    V = R = J = G = N = ""


def _dire(code, quoi, mesure=""):
    c = {"OK": V, "MANQUE": R, "—": J}[code]
    print(f"  {c}{code:7}{N} {quoi:44} {G}{mesure}{N}")


def main():
    print("\nContrôle 0 — de quoi dispose cet atelier")
    print("-" * 56)

    acquis = {}

    # python, et sa version : la chaîne demande 3.9
    v = sys.version_info
    if (v.major, v.minor) >= (3, 9):
        _dire("OK", "python", f"{v.major}.{v.minor}.{v.micro}")
        acquis["python"] = True
    else:
        _dire("MANQUE", "python 3.9 ou plus", f"{v.major}.{v.minor}")
        acquis["python"] = False

    # git : sans lui, pas de clone, donc pas de sources par la voie A
    g = shutil.which("git")
    if g:
        r = subprocess.run([g, "--version"], capture_output=True, text=True)
        _dire("OK", "git", r.stdout.strip()[:40])
        acquis["git"] = True
    else:
        _dire("MANQUE", "git", "pas de clone possible — voie B")
        acquis["git"] = False

    # python-docx : sans lui, pas de .docx, donc pas de livrable déposable
    try:
        import docx  # noqa: F401
        _dire("OK", "python-docx", "l'export .docx est possible")
        acquis["docx"] = True
    except Exception:                                      # noqa: BLE001
        _dire("MANQUE", "python-docx", "pip install python-docx")
        acquis["docx"] = False

    # le réseau : mesuré sur le dépôt lui-même, pas sur une adresse quelconque
    try:
        import urllib.request
        urllib.request.urlopen(
            "https://raw.githubusercontent.com/resolution-ib-dev/"
            "Resolution-2027/main/codes.json", timeout=12).read(64)
        _dire("OK", "accès au dépôt public", "en lecture, sans clé")
        acquis["reseau"] = True
    except Exception as e:                                 # noqa: BLE001
        _dire("MANQUE", "accès au dépôt public", str(e)[:44])
        acquis["reseau"] = False

    # le clone, s'il est déjà là
    clone = os.environ.get("DROIT") or os.path.join(ICI, "depot")
    if os.path.isdir(clone):
        _dire("OK", "sources déjà clonées", clone)
        acquis["clone"] = True
    else:
        _dire("—", "sources pas encore clonées", "c'est le geste 1")
        acquis["clone"] = False

    # ---- la voie, et ce qu'elle permet
    print()
    if acquis["python"] and acquis["git"] and acquis["reseau"]:
        voie = "A"
        quoi = ("la chaîne entière : clone des sources, verbatim du droit, "
                "contrôles, export .docx")
        if not acquis["docx"]:
            quoi = ("tout sauf l'export .docx — `pip install python-docx` et "
                    "rejouez ce contrôle")
    elif acquis["python"] and acquis["reseau"]:
        voie = "B"
        quoi = ("les sources en texte par le web, sans la base de droit : "
                "le verbatim se relève sur le site public du droit, à la main")
    elif acquis["python"]:
        voie = "B"
        quoi = ("rien ne peut se télécharger : il faut que l'utilisateur "
                "joigne lui-même les sources")
    else:
        voie = "B"
        quoi = "ni python ni réseau : la machine ne peut pas tourner ici"

    print(f"  VOIE {voie} — {quoi}")
    print(f"\n  Allez au § « Voie {voie} » de 01_DEMARRER.md.")
    if voie == "A" and acquis["docx"]:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
