# -*- coding: utf-8 -*-
"""Socle commun des modules de test de la machine.

Trois règles, et elles valent pour chaque module :

- **un test qui ne peut pas s'exercer ne passe pas** : il sort en `ABSENT` avec
  le nom de la pièce qui lui manque. Un `ABSENT` n'est pas un succès, et il
  n'est pas non plus un échec : il dit que la mesure n'a pas eu lieu.
- **aucun nombre attendu n'est écrit en dur sans sa source** : il vient du
  manifeste, d'un fichier d'empreintes ou d'un relevé nommé.
- **un test rend le nombre mesuré**, même quand il échoue, et surtout quand il
  échoue.
"""
import hashlib
import os
import sys
import time

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VERT, ROUGE, JAUNE, GRIS, NEUTRE = (
    "\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[0m")
if not sys.stdout.isatty():
    VERT = ROUGE = JAUNE = GRIS = NEUTRE = ""


class Journal:
    """Recueille les verdicts d'un module et rend son bilan."""

    def __init__(self, titre):
        self.titre = titre
        self.lignes = []
        self.t0 = time.time()

    def _poser(self, code, libelle, mesure=""):
        self.lignes.append((code, libelle, str(mesure)))

    def passe(self, libelle, mesure=""):
        self._poser("PASSE", libelle, mesure)

    def echoue(self, libelle, mesure=""):
        self._poser("ÉCHEC", libelle, mesure)

    def absent(self, libelle, mesure=""):
        self._poser("ABSENT", libelle, mesure)

    def egal(self, libelle, obtenu, attendu):
        if obtenu == attendu:
            self.passe(libelle, obtenu)
        else:
            self.echoue(libelle, f"attendu {attendu}, obtenu {obtenu}")
        return obtenu == attendu

    @property
    def echecs(self):
        return sum(1 for c, _, _ in self.lignes if c == "ÉCHEC")

    @property
    def absents(self):
        return sum(1 for c, _, _ in self.lignes if c == "ABSENT")

    @property
    def passes(self):
        return sum(1 for c, _, _ in self.lignes if c == "PASSE")

    def rendre(self):
        couleur = {"PASSE": VERT, "ÉCHEC": ROUGE, "ABSENT": JAUNE}
        print(f"\n{self.titre}")
        print("-" * len(self.titre))
        for c, libelle, mesure in self.lignes:
            print(f"  {couleur[c]}{c:6}{NEUTRE} {libelle:52} {GRIS}{mesure}{NEUTRE}")
        d = time.time() - self.t0
        print(f"  → {self.passes} passés, {self.echecs} échecs, "
              f"{self.absents} non joués — {d:.1f} s")
        return 1 if self.echecs else 0


def empreinte(chemin, n=16):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()[:n]


def octets(chemin):
    return os.path.getsize(chemin)


def lire_manifeste(chemin):
    """Rend {chemin: (empreinte, octets)} depuis le tableau du manifeste."""
    import re
    table = {}
    for l in open(chemin, encoding="utf-8"):
        m = re.match(r"^\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*`([0-9a-f]+)`\s*\|", l)
        if m:
            table[m.group(1)] = (m.group(3), int(m.group(2)))
    return table
