#!/usr/bin/env python3
"""Table close des pièces nommées — reconnaissance par liste, jamais devinée.

Une pièce ne se devine pas à l'expression régulière : trois reprises
successives ont tronqué les noms longs (« code des impositions sur les biens »)
et en ont inventé (« code propriétés non bâties »). La liste se relève une fois,
elle est close, et la reconnaissance se fait au plus long libellé.

Les codes sont relevés du millésime 2026 et du relevé PLF 2027 qui fait foi.
Les lois, ordonnances et décrets gardent leur forme régulière : ils portent leur
numéro et leur date, qui les identifient sans ambiguïté.
"""
import re

CODES = [
    "code des impositions sur les biens et services",
    "code général des impôts",
    "code général des collectivités territoriales",
    "code général de la fonction publique",
    "code des pensions civiles et militaires de retraite",
    "code des pensions civiles et militaires",
    "code des pensions militaires d’invalidité et des victimes de guerre",
    "code de la construction et de l’habitation",
    "code de l’action sociale et des familles",
    "code rural et de la pêche maritime",
    "code des procédures civiles d’exécution",
    "code de la propriété intellectuelle",
    "code des juridictions financières",
    "code de la commande publique",
    "code monétaire et financier",
    "code de la sécurité sociale",
    "code de la santé publique",
    "code de la sécurité intérieure",
    "code de l’environnement",
    "code de l’organisation judiciaire",
    "code de procédure pénale",
    "code de procédure civile",
    "code de l’aviation civile",
    "code de la mutualité",
    "code de la recherche",
    "code de l’éducation",
    "code des assurances",
    "code des transports",
    "code de l’énergie",
    "code de la défense",
    "code des douanes",
    "code du tourisme",
    "code du travail",
    "code électoral",
    "code forestier",
    "code du cinéma et de l’image animée",
    "code du patrimoine",
    "code du sport",
    "code de la route",
    "code civil",
    "code de commerce",
    "code pénal",
    "code minier",
    "code de l’urbanisme",
    "code de la consommation",
    "code des relations entre le public et l’administration",
    "code de l’entrée et du séjour des étrangers et du droit d’asile",
    "livre des procédures fiscales",
]
# plus long d'abord : « code des pensions civiles et militaires de retraite »
# doit l'emporter sur « code des pensions civiles et militaires ».
CODES.sort(key=len, reverse=True)


def _souple(nom):
    """Apostrophe droite ou courbe, espaces multiples : même pièce."""
    return re.escape(nom).replace("’", "['’’]").replace("\\ ", r"\s+")


MOTIF = re.compile(
    "(?P<nom>"
    + "|".join(_souple(c) for c in CODES)
    + r"|loi organique n[°o]\s*[\d‑\-]+\s+du\s+\d{1,2}\w*\s+\w+\s+\d{4}"
    + r"|loi n[°o]\s*[\d‑\-]+\s+du\s+\d{1,2}\w*\s+\w+\s+\d{4}"
    + r"|ordonnance n[°o]\s*[\d‑\-]+\s+du\s+\d{1,2}\w*\s+\w+\s+\d{4}"
    + r"|décret n[°o]\s*[\d‑\-]+\s+du\s+\d{1,2}\w*\s+\w+\s+\d{4}"
    + r"|loi de finances pour \d{4}"
    + r"|loi de financement de la sécurité sociale pour \d{4}"
    + ")", re.I)

INCONNU = re.compile(r"\bcode\s+[a-zà-ÿ’'\- ]{3,60}", re.I)


def trouver(texte):
    """Rend les pièces reconnues : (début, fin, libellé normalisé)."""
    out = []
    for m in MOTIF.finditer(texte):
        nom = " ".join(m.group("nom").split()).lower().replace("'", "’")
        out.append((m.start(), m.end(), nom))
    return out


def non_reconnues(texte):
    """Les « code … » qu'aucune entrée de la table ne couvre — à verser à la
    table, jamais à deviner au vol."""
    couvert = [(a, b) for a, b, _ in trouver(texte)]
    manques = []
    for m in INCONNU.finditer(texte):
        if not any(a <= m.start() < b for a, b in couvert):
            manques.append(" ".join(m.group(0).split()).lower())
    return manques
