#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test 2 — l'impression docx ne perd ni ne substitue aucun caractère.

Ce que le test prouve, sur une liasse réelle :

1. **l'invariant de caractères** — le texte extrait du docx est celui du source,
   à l'ajout près des intitulés de colonne `page` que le gabarit prescrit ;
2. **les caractères sensibles sont intacts** — insécables, apostrophes
   typographiques, guillemets français, tirets cadratin et demi-cadratin,
   comptés un à un de chaque côté ;
3. **les comptes de structure** — un saut de page par amendement, un signet par
   amendement, un renvoi `PAGEREF` par ligne de sommaire, et aucun amendement
   qui partage sa page.

Le contrôle est joué sur le flux de texte du docx, **jamais sur un PDF** : une
substitution de police ne peut pas le fausser. C'est la règle du § 5 de
`NUIT_8_impression_20261008`, et c'est elle qui a prouvé en octobre que la
conversion ne cassait ni les insécables ni les apostrophes.

Usage : python3 63_CONTROLE_docx.py [liasse.md …]
"""
import os
import re
import sys
import tempfile

sys.path.insert(0, os.path.join(RACINE_ := os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))),
    "skills", "expose-sommaire", "scripts"))
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


def _generateur():
    """Le générateur d'impression, chargé par chemin : son nom est numéroté."""
    return _charger("40_SCRIPT_imprimer_liasse.py", "imprimer_liasse")


# La pièce de contrôle par défaut est un amendement réel au gabarit de liasse,
# et non l'énoncé du mini-lot : l'énoncé est un texte de mandat, il ne porte pas
# le gabarit et son balisage fausse l'invariant. Défaut relevé par le lanceur le
# 20261016 — écart −4 sur une pièce qui n'avait rien à mesurer.
LIASSES_PAR_DEFAUT = ["51_RECETTE_sortie_attendue.md"]


def main(argv):
    j = Journal("Test 2 — invariant de caractères de l'impression docx")
    try:
        g = _generateur()
    except Exception as e:                      # noqa: BLE001
        j.absent("générateur importable", str(e)[:60])
        return j.rendre()

    sources = argv[1:] or [os.path.join(RACINE, p) for p in LIASSES_PAR_DEFAUT]
    sources = [s for s in sources if os.path.exists(s)]
    if not sources:
        j.absent("liasse de contrôle présente",
                 " / ".join(argv[1:] or LIASSES_PAR_DEFAUT))
        return j.rendre()
    j.passe("liasse de contrôle lue",
            f"{len(sources)} pièce(s), {sum(octets(s) for s in sources)} o")

    with tempfile.TemporaryDirectory() as tmp:
        sortie = os.path.join(tmp, "controle.docx")
        rendu = g.imprimer(sources, sortie)
        j.passe("docx produit", f"{octets(sortie)} o")

        src = g.texte_du_source(sources)
        out = g.texte_du_docx(sortie)
        nsrc = len(re.sub(r"\s+", "", src))
        nout = len(re.sub(r"\s+", "", out))

        # Les seuls caractères que le gabarit ajoute : un intitulé `page` par
        # tableau de sommaire, soit 4 caractères chacun.
        attendu = nsrc + 4 * rendu.sommaires
        ecart = nout - nsrc
        if nout == attendu:
            j.passe("invariant de caractères",
                    f"source {nsrc}, docx {nout}, écart +{ecart} "
                    f"= {rendu.sommaires} × 4 (intitulés « page »)")
        else:
            j.echoue("invariant de caractères",
                     f"source {nsrc}, docx {nout}, écart {ecart:+d}, "
                     f"attendu {attendu - nsrc:+d}")

        # caractères sensibles, un à un
        cs, co = g.comptes_sensibles(src), g.comptes_sensibles(out)
        intacts = 0
        for nom in cs:
            if cs[nom] == co[nom]:
                intacts += 1
            else:
                j.echoue(f"intact : {nom}",
                         f"source {cs[nom]}, docx {co[nom]}")
        if intacts == len(cs):
            j.passe("caractères sensibles intacts",
                    " · ".join(f"{n.split()[-1]} {v}" for n, v in cs.items()))

        # comptes de structure
        amdts = sum(len(re.findall(r"^##\s+Amendement\s+n°",
                                   open(s, encoding="utf-8").read(), re.M))
                    for s in sources)
        j.egal("un amendement rendu par amendement du source",
               rendu.amendements, amdts)
        j.egal("un signet posé par amendement rendu",
               len(rendu.poses), rendu.amendements)
        j.egal("tout rang de sommaire trouve son signet",
               rendu.pagerefs_morts, 0)
        if rendu.sauts >= rendu.amendements:
            j.passe("un saut de page au moins par amendement",
                    f"{rendu.sauts} sauts pour {rendu.amendements} amendements")
        else:
            j.echoue("un saut de page au moins par amendement",
                     f"{rendu.sauts} sauts pour {rendu.amendements} amendements")

        # aucun paragraphe de saut propre : le saut est porté par le paragraphe
        # suivant, sans quoi une page blanche naît en bas de page.
        from docx import Document
        doc = Document(sortie)
        vides_avec_saut = sum(
            1 for p in doc.paragraphs
            if not p.text.strip()
            and p._p.find(
                "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
                "pPr") is not None
            and p._p.findall(".//{http://schemas.openxmlformats.org/"
                             "wordprocessingml/2006/main}pageBreakBefore"))
        j.egal("aucun paragraphe de saut vide (source de pages blanches)",
               vides_avec_saut, 0)

    return j.rendre()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
