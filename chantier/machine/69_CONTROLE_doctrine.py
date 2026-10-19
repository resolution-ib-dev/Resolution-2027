#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle de doctrine — aucun prélèvement nouveau, aucune hausse.

**C'est le réflexe par défaut de la maison, et il ne se demande pas.** Un
amendement de cette chaîne ne crée aucun prélèvement et n'en majore aucun, y
compris pour gager une perte. Un gage qui institue une taxe au profit d'un
opérateur, ou qui relève un taux pour combler un trou, est une mesure fiscale
déguisée en clause de forme.

**Une seule exception, et elle est exacte au mot près** : la formule standard de
recevabilité, État seulement, relevée sur pièce. Elle est une convention
parlementaire, non une mesure, et son caractère postiche s'explique à l'exposé.

**Deux formules n'existent pas et ne s'inventent pas** : le gage d'une perte
supportée par les collectivités territoriales, et celui d'une perte supportée par
les organismes de sécurité sociale. Elles se relèvent sur une pièce réelle. Trois
formules ont été écrites de mémoire sur ce point, et les trois étaient fausses.

L'utilisateur peut lever le réflexe, en clair et au dossier, par la ligne
`gage par création de recette autorisée`. Ce contrôle la cherche dans la pièce.

Usage :
    python3 69_CONTROLE_doctrine.py <pièce.md> [<pièce.md> ...]
    python3 69_CONTROLE_doctrine.py --test
"""
import os
import re
import sys

import importlib.util as _iu


def _charger(nom_fichier, nom_module):
    """Un module Python ne peut pas commencer par un chiffre, et les pièces sont
    numérotées pour porter l'ordre de lecture."""
    c = os.path.join(os.path.dirname(os.path.abspath(__file__)), nom_fichier)
    s = _iu.spec_from_file_location(nom_module, c)
    m = _iu.module_from_spec(s)
    s.loader.exec_module(m)
    return m


Journal = _charger("60_CONTROLE_socle.py", "socle_controle").Journal

# La formule arbitrée, au mot près. Tout écart est un gage inventé.
STANDARD = ("la perte de recettes pour l'état est compensée à due concurrence "
            "par la création d'une taxe additionnelle à l'accise sur les tabacs "
            "prévue au chapitre iv du titre ier du livre iii du code des "
            "impositions sur les biens et services")

LICENCE = "gage par création de recette autorisée"

# Ce qui crée ou majore un prélèvement. Chaque motif a été écrit par un fil.
INTERDITS = {
    "création d'une taxe additionnelle, hors formule standard":
        r"cr[ée]ation d[’']une taxe additionnelle",
    "majoration d'un prélèvement pour gager":
        r"(?:major(?:ation|é\w*)|rel[èe]v\w+|port\w+)\s+(?:de\s+|du\s+|des\s+|le\s+|la\s+)?"
        r"(?:taux|droits?|accise|tarif|contribution|taxe)",
    "institution d'un prélèvement nouveau":
        r"il est institu[ée]\s+(?:une|un)\s+(?:taxe|contribution|pr[ée]l[èe]vement|accise)",
    "création d'un prélèvement au profit d'un tiers":
        r"cr[ée]ation d[’']un(?:e)? (?:taxe|contribution|pr[ée]l[èe]vement)[^.]{0,80}"
        r"au profit",
}


def _norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'").replace(" ", " ")
                  .replace(" ", " ")).strip().lower()


def _dispositif(texte):
    """La part de la pièce qui fait droit. Un exposé sommaire peut nommer une
    création de taxe pour la critiquer, et ce n'est pas une faute."""
    return re.split(r"(?mi)^#*\s*EXPOS[ÉE] SOMMAIRE\s*$", texte)[0]


def examiner(texte):
    """Rend la liste des écarts d'une pièce, chacun avec son extrait."""
    if LICENCE in _norm(texte):
        return [], True
    d = _norm(_dispositif(texte))
    # La formule standard est retirée avant la recherche : elle est permise.
    reste = d.replace(STANDARD, " ")
    ecarts = []
    for libelle, motif in INTERDITS.items():
        for m in re.finditer(motif, reste):
            ecarts.append((libelle, reste[max(0, m.start() - 40):m.end() + 60]))
    return ecarts, False


def main(argv):
    if "--test" in argv:
        return test()
    pieces = [a for a in argv[1:] if not a.startswith("--")]
    j = Journal("Contrôle de doctrine — aucun prélèvement nouveau")
    if not pieces:
        # Sans pièce nommée, le contrôle s'exerce sur les sorties de référence :
        # ce sont elles que la chaîne recopie, et c'est là que la faute est née.
        ici = os.path.dirname(os.path.abspath(__file__))
        pieces = [os.path.join(ici, f) for f in
                  ("51_RECETTE_sortie_attendue.md",
                   "54_RECETTE_lot2_sorties_attendues.md")
                  if os.path.exists(os.path.join(ici, f))]
    if not pieces:
        j.absent("pièce fournie", "passer un ou plusieurs <pièce.md>")
        return j.rendre()
    for p in pieces:
        if not os.path.exists(p):
            j.echoue(f"pièce lue : {os.path.basename(p)}", "introuvable")
            continue
        ecarts, licence = examiner(open(p, encoding="utf-8").read())
        nom = os.path.basename(p)
        if licence:
            j.passe(f"doctrine : {nom}", "levée explicite au dossier")
        elif ecarts:
            for libelle, extrait in ecarts[:4]:
                j.echoue(f"doctrine : {nom}", f"{libelle} — « …{extrait.strip()}… »")
        else:
            j.passe(f"doctrine : {nom}", "aucun prélèvement créé ni majoré")
    return j.rendre()


def test():
    ok = True
    cas = [
        ("formule standard seule",
         "**V.** – La perte de recettes pour l'État est compensée à due "
         "concurrence par la création d'une taxe additionnelle à l'accise sur "
         "les tabacs prévue au chapitre IV du titre Ier du livre III du code "
         "des impositions sur les biens et services.", 0),
        ("taxe additionnelle au profit d'un opérateur",
         "La perte de recettes pour le Centre national du cinéma est compensée "
         "par la création d'une taxe additionnelle aux droits mentionnés aux "
         "articles 575 et 575 A du code général des impôts.", 1),
        ("majoration pour gager",
         "La perte est compensée par la majoration des droits mentionnés aux "
         "articles 575 et 575 A du code général des impôts.", 1),
        ("création nommée dans l'exposé seulement",
         "**I.** – L'article 1 est abrogé.\n\nEXPOSÉ SOMMAIRE\n\nLe Gouvernement "
         "a proposé la création d'une taxe additionnelle, que cet amendement "
         "écarte.", 0),
        ("levée explicite",
         "gage par création de recette autorisée\n\nLa perte est compensée par "
         "la majoration des droits sur les tabacs.", 0),
    ]
    print("\nJeu d'essai — contrôle de doctrine")
    print("-" * 52)
    for libelle, texte, attendu in cas:
        ecarts, licence = examiner(texte)
        n = 0 if licence else min(len(ecarts), 1)
        bon = n == attendu
        ok = ok and bon
        print(f"  {'OK   ' if bon else 'ÉCHEC'}  {libelle} : "
              f"attendu {attendu}, obtenu {n}")
    print("\nJEU D'ESSAI :", "PASSE" if ok else "ÉCHOUE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
