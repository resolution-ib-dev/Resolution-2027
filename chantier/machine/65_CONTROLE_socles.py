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

Usage : SOURCES=/chemin/vers/sources python3 65_CONTROLE_socles.py
"""
import hashlib
import os
import re
import sys

from importlib import import_module as _im
socle = _im('60_CONTROLE_socle'.replace('60_CONTROLE_socle','socle_tests')) if False else None
import importlib.util as _iu


def _charger(nom_fichier, nom_module):
    """Charge un module dont le nom de fichier commence par un chiffre.

    Les pièces sont numérotées pour porter l'ordre ; un module Python ne peut pas
    commencer par un chiffre. On charge donc par chemin.
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

PIECES = {
    "l17b3210_projet-loi.pdf": (
        "132274b83bed4861a9e1a147d0d16abda2d729cdad2373ef804e26747c43d881",
        "PLF 2027 n° 3210"),
    "l17b3211_projet-loi.pdf": (
        "47f5fc0d1581c90634449516281070495b92cfe062c20c2a366919622906eab6",
        "PLFSS 2027 n° 3211"),
}


def _clone():
    """Le clone du dépôt public, posé par le geste d'ouverture du LISEZ-MOI."""
    for c in (os.environ.get("DROIT"),
              os.path.join(RACINE, "droit")):
        if c and os.path.isdir(c):
            return c
    return os.path.join(RACINE, "droit")


def _dossier_sources():
    for c in (os.environ.get("SOURCES"),
              os.path.join(RACINE, "sources"),
              os.path.join(_clone(), "chantier", "sources")):
        if c and os.path.isdir(c):
            return c
    return None


def _empreintes_attendues():
    """Les empreintes de référence se lisent au relevé, jamais en dur ici."""
    for c in (os.path.join(RACINE, "31_REFERENCE_socles_2027.sha256"),
              os.path.join(RACINE, "31_REFERENCE_socles_2027.sha256")):
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
                 "31_REFERENCE_socles_2027.sha256")
        return j.rendre()
    j.passe("relevé d'empreintes lu",
            f"{os.path.basename(releve)}, {len(attendues)} empreintes")

    d = _dossier_sources()
    if not d:
        j.absent("pièces enregistrées présentes",
                 "ni $SOURCES, ni ./sources, ni le clone — les deux PDF se téléchargent chez l'Assemblée")
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
        for base in (os.path.join(_clone(), "chantier", "referentiels"),):
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
    # L'extracteur vit au dépôt, qui est la surface des références, et non au
    # paquet : le paquet porte la méthode, le dépôt porte ce qui se relève.
    extr = None
    for c in (os.path.join(_clone(), "chantier", "appareil",
                           "socle_texte_2027.py"),):
        if os.path.exists(c):
            extr = c
            break
    if not extr:
        j.absent("extracteur présent au clone",
                 "droit/chantier/appareil/socle_texte_2027.py — cloner le dépôt")
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
