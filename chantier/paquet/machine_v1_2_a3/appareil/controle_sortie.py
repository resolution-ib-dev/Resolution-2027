#!/usr/bin/env python3
"""Contrôle G — aucune pièce diffusée ne nomme un déposant, un projet, un
référentiel interne.

Il vaut pour toute pièce qui sort : document de méthode versé au paquet,
amendement, exposé sommaire, liasse, mode d'emploi. Il bloque — une règle qu'on
tient à l'œil se perd.

Usage :
    python3 controle_sortie.py FICHIER [FICHIER...]       rapport lisible
    python3 controle_sortie.py --json FICHIER [...]        rapport JSON
    python3 controle_sortie.py --epreuve                   jeu de fautes et jeu de justes

Sortie : code 0 si aucune pièce ne porte de fuite, 1 sinon.
"""
import json
import re
import sys

# --------------------------------------------------------------------- motifs
#
# Chaque motif porte sa famille et ce qu'il attrape. Un motif se lit seul :
# celui qui le relit doit comprendre pourquoi il est là sans ouvrir autre chose.

MOTIFS = [
    # -- une organisation, un déposant, une personne : vos propres noms se
    # déclarent dans `motifs_locaux.txt`, à côté de ce module, une expression
    # régulière par ligne. Le paquet n'en livre aucun : il ne nomme personne.
    # -- un référentiel interne
    ("referentiel", r"\bREF_\w+", "référentiel interne"),
    ("referentiel", r"\bvalises?\b", "objet interne"),
    ("referentiel", r"\bcoffre\b", "objet interne"),

    # -- un identifiant de registre
    ("identifiant", r"\bA-\d{1,4}\b", "arbitrage interne"),
    ("identifiant", r"\bM-\d{3}\b", "mesure interne"),
    ("identifiant", r"\bB-\d{2}\b", "bloc interne"),
    ("identifiant", r"\bP-D-\d+\b", "nœud de doctrine interne"),
    ("identifiant", r"\bD\d-\d[\w-]*\b", "nœud de doctrine interne"),
    ("identifiant", r"\bS\d{2}\b", "repère interne"),

    # -- une pièce ou un lieu interne
    ("piece", r"\ble\s+manuscrit\b", "pièce interne"),
    # Garde étroite et motivée : « le livre III du code des impositions sur les
    # biens et services » est dans la formule canonique du gage. Un faux positif
    # y bloquerait toute liasse gagée. Seul le livre non suivi d'un rang est pris.
    ("piece", r"\ble\s+livre\b(?!\s+(?:[IVXLCDM]+\b|premier\b|\d))", "pièce interne"),
    ("piece", r"\bcorpus\b", "pièce interne"),
    ("piece", r"\ble\s+classeur\b|\bles\s+classeurs\b", "pièce interne"),
    ("piece", r"\ble\s+d[ée]coupage\b", "pièce interne"),
    ("piece", r"\bnotre\s+doctrine\b|\bla\s+doctrine\b", "pièce interne"),

    # -- un chemin, une commande, une mécanique de notre atelier
    ("chemin", r"(?<![\w/])(?:methode|livrables|referentiels|appareil|reference|sources|paquet)/[\w./-]+",
     "chemin du corpus"),

    # -- la figure de l'auteur
    ("auteur", r"\bl['’]auteure?\b", "renvoi à l'auteur du projet"),
]

# ----------------------------------------------------------------- exceptions
#
# Déclarées, et elles le restent. Une exception non écrite est une fuite.

EXCEPTIONS = [
    # Le dépôt de droit est cloné par la machine du destinataire : son adresse
    # est fonctionnellement nécessaire et voyage donc avec le paquet.
    (r"resolution-ib-dev/Resolution-2027", "dépôt de droit, cloné par la machine"),
    (r"github\.com/resolution-ib-dev[\w/-]*", "dépôt de droit, cloné par la machine"),

    # Le paquet livré porte lui-même des dossiers `appareil/` et `referentiels/`.
    # Son mode d'emploi doit pouvoir les nommer : ce sont les dossiers que le
    # destinataire a sous les yeux. L'exception est close — elle énumère les
    # pièces livrées, et ne couvre ni `methode/`, ni `livrables/`, ni
    # `reference/`, qui n'existent que dans l'atelier.
    (r"appareil/(?:controle_sortie|generateur_liasse_docx|socle_texte_2027"
     r"|portes_ouvertes|index_mesures_2027|redaction_2027|pieces_nommees"
     r"|installer_droit)\.py",
     "pièce livrée du paquet"),
    # `plfss?` ne couvrait pas `plf` : il se lit « plfs » plus un « s »
    # facultatif. Le mode d'emploi de la version 1.0 ne pouvait donc pas nommer
    # `referentiels/articles_ouverts_plf2027.tsv`, pourtant livré, sans être
    # déclaré en fuite. Corrigé au 20261002 : `plf(?:ss)?`.
    (r"referentiels/(?:articles_ouverts|portes_ouvertes|releves_transversaux"
     r"|index_mesures)_plf(?:ss)?\d{4}\.(?:tsv|md)",
     "référentiel livré du paquet"),
    (r"referentiels/redaction_plf(?:ss)?\.json", "référentiel livré du paquet"),
]

import os as _os
_LOCAUX = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "motifs_locaux.txt")
if _os.path.exists(_LOCAUX):
    with open(_LOCAUX, encoding="utf-8") as _fh:
        for _l in _fh:
            _l = _l.strip()
            if _l and not _l.startswith("#"):
                MOTIFS.append(("organisation", _l, "nom déclaré localement"))

MOTIFS_COMPILES = [(f, re.compile(m, re.IGNORECASE), q) for f, m, q in MOTIFS]
EXCEPTIONS_COMPILEES = [(re.compile(m, re.IGNORECASE), r) for m, r in EXCEPTIONS]


def _couvert(ligne, debut, fin):
    """Vrai si l'occurrence tombe dans une exception déclarée."""
    for rx, _ in EXCEPTIONS_COMPILEES:
        for e in rx.finditer(ligne):
            if e.start() <= debut and fin <= e.end():
                return True
    return False


def controler(texte, nom="<texte>"):
    """Rend la liste des fuites. Une fuite par occurrence, jamais dédoublonnée :
    le nombre est ce qui se corrige, pas la variété."""
    fuites = []
    for n, ligne in enumerate(texte.split("\n"), 1):
        for famille, rx, quoi in MOTIFS_COMPILES:
            for m in rx.finditer(ligne):
                if _couvert(ligne, m.start(), m.end()):
                    continue
                fuites.append({
                    "piece": nom,
                    "ligne": n,
                    "famille": famille,
                    "quoi": quoi,
                    "texte": m.group(0),
                    "contexte": ligne.strip()[:120],
                })
    return fuites


def rapport(fuites, nom):
    par_famille = {}
    for f in fuites:
        par_famille[f["famille"]] = par_famille.get(f["famille"], 0) + 1
    if not fuites:
        return f"{nom} : PROPRE"
    detail = ", ".join(f"{k} {v}" for k, v in sorted(par_famille.items()))
    return f"{nom} : {len(fuites)} fuites — {detail}"


# -------------------------------------------------------------------- épreuve
#
# Un contrôle neuf porte son jeu de fautes et son jeu de justes. Le jeu de
# justes est le plus utile : il répond à « qu'est-ce qui a le droit de passer ».

JEU_DE_FAUTES = [
    ("referentiel", "La valeur se lit dans REF_exemple."),
    ("referentiel", "Le chiffre se prend à REF_table avec son niveau de confiance."),
    ("referentiel", "Le matériel vit dans la valise, séparable."),
    ("referentiel", "Le coffre rend ses documents en texte."),
    ("referentiel", "Le document a été retiré du coffre."),
    ("piece", "Deux règles du corpus s'y ajoutent."),
    ("chemin", "Il complète sources/structure_ppl.md."),
    ("identifiant", "Méthode arrêtée par A-999."),
    ("identifiant", "La mesure M-999 porte la clause."),
    ("identifiant", "Le bloc B-99 reste ouvert."),
    ("identifiant", "Le nœud D9-9 écrit un montant."),
    ("piece", "Le manuscrit prime sur le classeur."),
    ("piece", "Croiser avec le découpage interne."),
    ("chemin", "La règle vit dans methode/exemple.md."),
    ("chemin", "Voir livrables/exemple.md."),
    ("chemin", "Voir reference/exemple.md."),
    ("auteur", "L'arbitrage revient à l'auteure."),
    ("auteur", "L'auteur tranche."),
]

JEU_DE_JUSTES = [
    "L'article 200 du code général des impôts est abrogé.",
    "Le présent amendement supprime la réduction d'impôt au titre des dons.",
    "Au deuxième alinéa, les mots : « et 18 % » sont supprimés.",
    "Le projet de loi de finances pour 2027 ouvre l'article 39 decies A.",
    "Source : Cour des comptes, rapport public annuel 2025, page 112.",
    "Le droit en vigueur se lit sur github.com/resolution-ib-dev/Resolution-2027.",
    "git clone https://github.com/resolution-ib-dev/Resolution-2027 droit",
    "La recevabilité financière s'apprécie au regard de l'article 40 de la Constitution.",
    "Le gage est pris sur une dépense fiscale désignée par son numéro.",
    "Cette disposition entre en vigueur le 1er juillet 2027.",
    "Le taux réduit prévu à l'article 278-0 bis est supprimé.",
    "Un tableau d'état B porte la mission, le programme et la catégorie.",
    "La perte de recettes résultant pour l'État du I est compensée à due "
    "concurrence par la création d'une taxe additionnelle à l'accise sur les "
    "tabacs prévue au chapitre IV du titre Ier du livre III du code des "
    "impositions sur les biens et services.",
    "Les accises régies par le livre III du code des impositions sur les biens "
    "et services.",
]


def epreuve():
    echecs = []
    for famille, phrase in JEU_DE_FAUTES:
        f = controler(phrase, "faute")
        if not f:
            echecs.append(f"FAUTE NON VUE [{famille}] : {phrase}")
        elif not any(x["famille"] == famille for x in f):
            vues = sorted({x["famille"] for x in f})
            echecs.append(f"FAUTE MAL CLASSÉE [{famille} attendu, {vues} vu] : {phrase}")
    for phrase in JEU_DE_JUSTES:
        f = controler(phrase, "juste")
        if f:
            quoi = ", ".join(f"{x['famille']}:{x['texte']}" for x in f)
            echecs.append(f"JUSTE REFUSÉ [{quoi}] : {phrase}")
    print(f"jeu de fautes : {len(JEU_DE_FAUTES)} | jeu de justes : {len(JEU_DE_JUSTES)}")
    for e in echecs:
        print("  " + e)
    print("ÉPREUVE : " + ("verte" if not echecs else f"{len(echecs)} échecs"))
    return 0 if not echecs else 1


def main(argv):
    if "--epreuve" in argv:
        return epreuve()
    en_json = "--json" in argv
    fichiers = [a for a in argv if not a.startswith("--")]
    if not fichiers:
        print(__doc__)
        return 2
    toutes, sortie = [], []
    for nom in fichiers:
        with open(nom, encoding="utf-8") as fh:
            fuites = controler(fh.read(), nom)
        toutes += fuites
        sortie.append(rapport(fuites, nom))
    if en_json:
        print(json.dumps(toutes, ensure_ascii=False, indent=1))
    else:
        print("\n".join(sortie))
        print(f"\nTOTAL : {len(toutes)} fuites sur {len(fichiers)} pièces")
    return 0 if not toutes else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
