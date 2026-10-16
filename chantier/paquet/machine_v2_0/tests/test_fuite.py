#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test 6 — aucune marque de l'atelier d'origine ne part avec le paquet.

Ce que le test prouve : aucune pièce du paquet ne nomme le projet qui l'a
fabriqué, ses adresses internes, ses personnes, ni ses chemins de travail.

Il se joue contre une **liste de motifs qui ne fait pas partie du paquet** —
elle nomme ce qu'il ne faut pas laisser sortir, donc la livrer reviendrait à
livrer ce qu'elle protège. La liste vit chez l'atelier, et le test sort en
`ABSENT` quand elle n'est pas fournie : chez un tiers, il n'a rien à mesurer et
le dit.

**Deux exceptions, déclarées et non devinées.** L'adresse du dépôt public de
droit est nécessaire — un tiers doit pouvoir le cloner — et le nom du dépôt
apparaît forcément dans la procédure qui l'installe. Elles sont nommées à
`EXCEPTIONS` ci-dessous, et toute autre occurrence est une fuite.

Usage :
    MOTIFS=/chemin/motifs_locaux_atelier.txt python3 tests/test_fuite.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from socle import RACINE, Journal  # noqa: E402

# Pièces où une occurrence est attendue, avec la raison. Une exception se
# déclare par pièce ET par motif : elle ne vaut jamais pour tout le paquet.
EXCEPTIONS = {
    ("appareil/installer_droit.py", "resolution-ib-dev"):
        "adresse du dépôt public de droit, que le tiers doit cloner",
    ("appareil/installer_droit.py", "Resolution"):
        "nom du dépôt public de droit",
    ("procedures/depot_droit.md", "resolution-ib-dev"):
        "adresse du dépôt public de droit",
    ("procedures/depot_droit.md", "Resolution"):
        "nom du dépôt public de droit",
    ("procedures/passation_droit_renvois.md", "resolution-ib-dev"):
        "adresse du dépôt public de droit",
    ("procedures/passation_droit_renvois.md", "Resolution"):
        "nom du dépôt public de droit",
}

LISIBLES = (".py", ".md", ".txt", ".tsv", ".json", ".csv", ".sha256")

# Le module ne se lit pas lui-même : sa table d'exceptions cite forcément les
# chaînes qu'elle autorise, et il se signalerait comme sa propre fuite.
HORS_LECTURE = {"tests/test_fuite.py"}


def _motifs():
    for c in (os.environ.get("MOTIFS"),
              os.path.join(os.path.dirname(RACINE), "motifs_locaux_atelier.txt"),
              os.path.join(os.path.dirname(RACINE),
                           "appareil", "motifs_locaux_atelier.txt")):
        if c and os.path.exists(c):
            lignes = [l.strip() for l in open(c, encoding="utf-8")]
            return c, [l for l in lignes if l and not l.startswith("#")]
    return None, []


def main():
    j = Journal("Test 6 — fuites de l'atelier d'origine")
    chemin, motifs = _motifs()
    if not motifs:
        j.absent("liste de motifs fournie",
                 "ni $MOTIFS ni ../motifs_locaux_atelier.txt — "
                 "elle ne fait pas partie du paquet")
        return j.rendre()
    j.passe("liste de motifs lue",
            f"{os.path.basename(chemin)}, {len(motifs)} motifs")

    mauvais = [m for m in motifs if _invalide(m)]
    if mauvais:
        j.echoue("tous les motifs compilent", " · ".join(mauvais[:3]))
        return j.rendre()

    fuites, tolerees, lus = {}, 0, 0
    for r, dirs, files in os.walk(RACINE):
        dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git")]
        for f in sorted(files):
            p = os.path.join(r, f)
            rel = os.path.relpath(p, RACINE)
            if not rel.endswith(LISIBLES) or rel in HORS_LECTURE:
                continue
            try:
                t = open(p, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            lus += 1
            for m in motifs:
                for h in re.finditer(m, t):
                    if (rel, h.group(0)) in EXCEPTIONS:
                        tolerees += 1
                        continue
                    fuites.setdefault(rel, []).append(h.group(0))
    j.passe("pièces lues", lus)

    if tolerees:
        j.passe("occurrences tolérées, chacune déclarée", tolerees)

    if fuites:
        for rel, v in sorted(fuites.items()):
            j.echoue(f"aucune marque : {rel}",
                     f"{len(v)} — " + " · ".join(sorted(set(v))[:5]))
    else:
        j.passe("aucune marque de l'atelier dans le paquet",
                f"0 sur {lus} pièces, {len(motifs)} motifs")

    return j.rendre()


def _invalide(motif):
    try:
        re.compile(motif)
        return False
    except re.error:
        return True


if __name__ == "__main__":
    sys.exit(main())
