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
    MOTIFS=/chemin/motifs_locaux_atelier.txt python3 67_CONTROLE_fuite.py
"""
import os
import re
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

# Pièces où une occurrence est attendue, avec la raison. Une exception se
# déclare par pièce ET par motif : elle ne vaut jamais pour tout le paquet.
EXCEPTIONS = {
    ("11_OUTIL_disposition_cible.md", "resolution-ib-dev"):
        "adresse du dépôt public de droit, que le tiers doit cloner",
    ("11_OUTIL_disposition_cible.md", "Resolution"):
        "nom du dépôt public de droit",
    ("LISEZ-MOI.md", "resolution-ib-dev"):
        "adresse du dépôt public de droit",
    ("LISEZ-MOI.md", "Resolution"):
        "nom du dépôt public de droit",
    ("LISEZ-MOI.md", "resolution-ib-dev"):
        "adresse du dépôt public de droit, au geste d'ouverture",
    ("LISEZ-MOI.md", "Resolution"):
        "nom du dépôt public de droit",
    # Une source publique CITÉE n'est pas une fuite : la nommer est du sourçage,
    # et le taire serait prendre son travail sans le dire.
    ("04_PROCEDURE_vecteurs.md", "Génération Libre"):
        "source publique citée — contre-budget 2026, document publié",
}

LISIBLES = (".py", ".md", ".txt", ".tsv", ".json", ".csv", ".sha256")

# Le module ne se lit pas lui-même : sa table d'exceptions cite forcément les
# chaînes qu'elle autorise, et il se signalerait comme sa propre fuite.
HORS_LECTURE = {"67_CONTROLE_fuite.py"}


# La liste de motifs ne vit JAMAIS dans un dépôt. Le dépôt du projet est public :
# y verser la liste de ce qu'on ne veut pas publier revient à publier la carte de
# ce qu'il faut y chercher. Elle vit au coffre — les documents du projet, qui sont
# privés — et un fil d'atelier la passe par $MOTIFS le temps du contrôle.
# Versée au dépôt le 20261016, retirée le même jour.
HORS_DEPOT = "motifs_locaux_atelier.txt"


def _motifs():
    for c in (os.environ.get("MOTIFS"),
              os.path.join(os.path.dirname(RACINE), HORS_DEPOT)):
        if c and os.path.exists(c):
            lignes = [l.strip() for l in open(c, encoding="utf-8")]
            return c, [l for l in lignes if l and not l.startswith("#")]
    return None, []


def main():
    j = Journal("Test 6 — fuites de l'atelier d'origine")
    chemin, motifs = _motifs()
    if not motifs:
        j.absent("liste de motifs fournie",
                 "sans objet chez un tiers : la liste reste à l'atelier d'origine — "
                 "elle ne se livre pas")
        return j.rendre()
    j.passe("liste de motifs lue",
            f"{os.path.basename(chemin)}, {len(motifs)} motifs")

    # Garde-fou : la liste ne se livre pas avec le paquet.
    porte = [f for f in os.listdir(RACINE) if f == HORS_DEPOT]
    if porte:
        j.echoue("la liste de motifs n'est pas dans le paquet",
                 " · ".join(porte) + " — à retirer, elle ne se publie pas")
    else:
        j.passe("la liste de motifs n'est pas dans le paquet")

    mauvais = [m for m in motifs if _invalide(m)]
    if mauvais:
        j.echoue("tous les motifs compilent", " · ".join(mauvais[:3]))
        return j.rendre()

    fuites, tolerees, lus = {}, 0, 0
    for rel in sorted(os.listdir(RACINE)):
        p = os.path.join(RACINE, rel)
        if os.path.isfile(p):
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
