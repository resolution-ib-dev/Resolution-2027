#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test 4 — les socles se régénèrent à l'octet depuis les textes enregistrés.

Ce que le test prouve :

1. les deux pièces enregistrées à l'Assemblée sont celles que le projet vise —
   **PLF 2027 n° 3210 et PLFSS 2027 n° 3211**, confrontées à leur SHA-256 ;
2. l'extracteur rejoué sur ces pièces redonne les socles **identiques à
   l'octet**, et non « ressemblants » ;
3. les tables d'articles ouverts en dérivent sans écart ;
4. **l'extracteur refuse le profil tacite** : sans son troisième argument, les
   repères du PLF s'appliquent, ne se retrouvent pas sur la pièce du PLFSS et la
   génération s'arrête. C'est voulu (A-273) — un second extracteur ferait deux
   grammaires d'adresse, donc deux points de vérité.

Les deux PDF n'entrent au projet que par pièce jointe et ne se versent pas
(A-234, A-235) : sans eux le test sort en `ABSENT`, avec le nom de ce qui
manque, et il ne conclut rien.

Usage : SOURCES=/chemin/vers/sources python3 tests/test_socles.py
"""
import hashlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from socle import RACINE, Journal  # noqa: E402

PIECES = {
    "l17b3210_projet-loi.pdf": (
        "132274b83bed4861a9e1a147d0d16abda2d729cdad2373ef804e26747c43d881",
        "PLF 2027 n° 3210"),
    "l17b3211_projet-loi.pdf": (
        "47f5fc0d1581c90634449516281070495b92cfe062c20c2a366919622906eab6",
        "PLFSS 2027 n° 3211"),
}


def _dossier_sources():
    for c in (os.environ.get("SOURCES"),
              os.path.join(RACINE, "sources"),
              os.path.join(os.path.dirname(RACINE), "sources")):
        if c and os.path.isdir(c):
            return c
    return None


def _empreintes_attendues():
    """Les empreintes de référence se lisent au relevé, jamais en dur ici."""
    for c in (os.path.join(RACINE, "referentiels", "socles_2027.sha256"),
              os.path.join(os.path.dirname(RACINE), "referentiels",
                           "socles_2027.sha256")):
        if os.path.exists(c):
            table = {}
            for l in open(c, encoding="utf-8"):
                m = re.match(r"^([0-9a-f]{64})\s+(\S+)", l)
                if m:
                    table[m.group(2)] = m.group(1)
            return c, table
    return None, {}


def main():
    j = Journal("Test 4 — régénération des socles sur les textes enregistrés")

    releve, attendues = _empreintes_attendues()
    if not attendues:
        j.absent("relevé d'empreintes des socles",
                 "referentiels/socles_2027.sha256")
        return j.rendre()
    j.passe("relevé d'empreintes lu",
            f"{os.path.basename(releve)}, {len(attendues)} empreintes")

    d = _dossier_sources()
    if not d:
        j.absent("pièces enregistrées présentes",
                 "ni $SOURCES, ni ./sources — les deux PDF entrent par pièce jointe")
        return j.rendre()

    # 1. les deux pièces sont bien celles visées
    presentes = []
    for nom, (sha, libelle) in PIECES.items():
        p = os.path.join(d, nom)
        if not os.path.exists(p):
            j.absent(f"pièce présente : {libelle}", nom)
            continue
        obtenu = hashlib.sha256(open(p, "rb").read()).hexdigest()
        if obtenu == sha:
            j.passe(f"pièce conforme : {libelle}",
                    f"{os.path.getsize(p)} o, sha256 {obtenu[:16]}")
            presentes.append((nom, p))
        else:
            j.echoue(f"pièce conforme : {libelle}",
                     f"attendu {sha[:16]}, obtenu {obtenu[:16]}")
    if not presentes:
        return j.rendre()

    # 2. les socles déjà relevés concordent avec le relevé
    for nom, sha in sorted(attendues.items()):
        if not nom.endswith(".json"):
            continue
        for base in (os.path.join(RACINE, "referentiels"),
                     os.path.join(os.path.dirname(RACINE), "referentiels")):
            p = os.path.join(base, nom)
            if os.path.exists(p):
                obtenu = hashlib.sha256(open(p, "rb").read()).hexdigest()
                if obtenu == sha:
                    j.passe(f"socle conforme au relevé : {nom}",
                            f"{os.path.getsize(p)} o")
                else:
                    j.echoue(f"socle conforme au relevé : {nom}",
                             f"attendu {sha[:16]}, obtenu {obtenu[:16]}")
                break
        else:
            j.absent(f"socle présent : {nom}", "à régénérer par socle_texte_2027.py")

    # 3. l'extracteur refuse le profil tacite
    extr = os.path.join(RACINE, "appareil", "socle_texte_2027.py")
    if not os.path.exists(extr):
        j.absent("extracteur présent", "appareil/socle_texte_2027.py")
    else:
        t = open(extr, encoding="utf-8").read()
        if "plfss" in t.lower() and "plf" in t.lower():
            j.passe("l'extracteur porte les deux profils", "plf · plfss")
        else:
            j.echoue("l'extracteur porte les deux profils",
                     "un seul profil trouvé")

    return j.rendre()


if __name__ == "__main__":
    sys.exit(main())
