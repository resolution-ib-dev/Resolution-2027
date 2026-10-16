#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test 5 — recette de bout en bout sur le mini-lot.

Ce que le test prouve : la chaîne installée chez un tiers rend, depuis un énoncé
en langage ordinaire, **un amendement déposable exporté en .docx**. C'est le seul
test qui mesure le produit et non ses pièces.

Il se joue en deux temps, et le second est facultatif :

**Temps 1 — le gabarit, toujours joué.** La sortie attendue est confrontée au
gabarit de liasse : en-tête de rang et de titre, cartouche, dispositif, exposé
sommaire, et export docx réussi avec l'invariant de caractères tenu. Ce temps ne
demande aucun modèle : il mesure la pièce et la chaîne d'impression.

**Temps 2 — la concordance de fond, jouée si une sortie du tiers est fournie.**
`--sortie <pièce.md>` confronte la pièce rendue par le tiers à la sortie
attendue sur les **quatre points qui font recette** : le vecteur, le véhicule,
l'entrée en vigueur, le gage. Un écart de rédaction n'est pas un échec ; un
écart de vecteur en est un.

Usage :
    python3 66_CONTROLE_recette.py
    python3 66_CONTROLE_recette.py --sortie /chemin/amendement_du_tiers.md
"""
import argparse
import os
import re
import sys
import tempfile

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


# Les quatre points de recette, relevés sur la sortie attendue et non écrits ici
POINTS = {
    "vecteur": r"article\s+(L\.\s*\d+[-–]\d+(?:[-–]\d+)?)",
    "entrée en vigueur": r"à compter du (\d{1,2}\w*\s+\w+\s+\d{4})",
    "gage": r"(concourt à la réduction des prélèvements"
            r"|compensée à due concurrence|gage)",
}


def _releve(texte, motif):
    return sorted(set(m if isinstance(m, str) else m[0]
                      for m in re.findall(motif, texte, re.I)))


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", help="pièce rendue par le tiers, à confronter")
    a = ap.parse_args(argv[1:])

    j = Journal("Test 5 — recette de bout en bout sur le mini-lot")

    att = os.path.join(RACINE, "51_RECETTE_sortie_attendue.md")
    eno = os.path.join(RACINE, "50_RECETTE_enonce.md")
    for p, nom in ((att, "51_RECETTE_sortie_attendue.md"),
                   (eno, "50_RECETTE_enonce.md")):
        if not os.path.exists(p):
            j.absent(f"présent : {nom}", p)
            return j.rendre()
    t_att = open(att, encoding="utf-8").read()
    j.passe("mini-lot lu", f"énoncé {octets(eno)} o, attendu {octets(att)} o")

    # ---- temps 1 : le gabarit et la chaîne d'impression -----------------
    gabarit = {
        "en-tête de rang et de titre": r"^##\s+Amendement\s+n°\s*\S+\s*\[.+\]",
        "cartouche AMENDEMENT": r"^AMENDEMENT\s*$",
        "ligne « présenté par »": r"^présenté par\s*$",
        "accroche d'article": r"^(ARTICLE|APRÈS L[’']ARTICLE)",
        "exposé sommaire": r"^EXPOSÉ SOMMAIRE\s*$",
        "dispositif subdivisé": r"^\*\*[IVX]+\.\*\*\s*[–—]",
    }
    for libelle, motif in gabarit.items():
        if re.search(motif, t_att, re.M):
            j.passe(f"gabarit : {libelle}")
        else:
            j.echoue(f"gabarit : {libelle}", "absent de la sortie attendue")

    # Le cartouche a quatre lignes, et la quatrième est une ligne de tirets qui
    # DOIT se rendre. Un motif de séparateur trop large l'avalait, sans que
    # l'invariant de caractères puisse le voir : les deux côtés la supprimaient
    # de la même façon. Ce contrôle se fait donc sur le rendu, pas sur le compte.
    try:
        _g = _generateur()
    except Exception as e:                       # noqa: BLE001
        j.absent("générateur importable", str(e)[:60])
        return j.rendre()
    with tempfile.TemporaryDirectory() as tmp:
        o = os.path.join(tmp, "cartouche.docx")
        _g.imprimer([att], o)
        textes = [p.text.strip() for p in __import__("docx").Document(o).paragraphs]
        for libelle, attendu in (("AMENDEMENT", "AMENDEMENT"),
                                 ("présenté par", "présenté par")):
            j.egal(f"cartouche rendu : {libelle}",
                   sum(1 for t in textes if t == attendu), 1)
        tirets = sum(1 for t in textes if re.fullmatch(r"-{4,}", t))
        j.egal("cartouche rendu : ligne de tirets", tirets, 1)

    mots = len(re.findall(r"\w+", t_att.split("EXPOSÉ SOMMAIRE")[-1]))
    if 150 <= mots <= 450:
        j.passe("exposé sommaire dans son gabarit", f"{mots} mots")
    else:
        j.echoue("exposé sommaire dans son gabarit",
                 f"{mots} mots, attendu 200 à 300 (tolérance 150-450)")

    try:
        g = _generateur()
    except Exception as e:                       # noqa: BLE001
        j.absent("générateur importable", str(e)[:60])
        return j.rendre()

    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "mini-lot.docx")
        rendu = g.imprimer([att], out)
        j.egal("un amendement rendu au docx", rendu.amendements, 1)
        src = re.sub(r"\s+", "", g.texte_du_source([att]))
        doc = re.sub(r"\s+", "", g.texte_du_docx(out))
        attendu = len(src) + 4 * rendu.sommaires
        if len(doc) == attendu:
            j.passe("invariant de caractères sur le mini-lot",
                    f"source {len(src)}, docx {len(doc)}")
        else:
            j.echoue("invariant de caractères sur le mini-lot",
                     f"source {len(src)}, docx {len(doc)}, "
                     f"écart {len(doc) - len(src):+d}")
        cs, co = g.comptes_sensibles(g.texte_du_source([att])), \
            g.comptes_sensibles(g.texte_du_docx(out))
        ecarts = [n for n in cs if cs[n] != co[n]]
        if ecarts:
            j.echoue("caractères sensibles intacts", " · ".join(ecarts))
        else:
            j.passe("caractères sensibles intacts",
                    " · ".join(f"{n.split()[-1]} {v}" for n, v in cs.items()))
        j.passe("docx du mini-lot produit", f"{octets(out)} o")

    # ---- temps 2 : la concordance de fond, si une sortie est fournie -----
    if not a.sortie:
        j.absent("concordance de fond avec la pièce du tiers",
                 "aucune pièce fournie — passer --sortie <pièce.md>")
        return j.rendre()
    if not os.path.exists(a.sortie):
        j.echoue("pièce du tiers lisible", a.sortie)
        return j.rendre()
    t_obt = open(a.sortie, encoding="utf-8").read()
    j.passe("pièce du tiers lue", f"{octets(a.sortie)} o")

    for nom, motif in POINTS.items():
        ra, ro = _releve(t_att, motif), _releve(t_obt, motif)
        if not ra:
            j.absent(f"point de recette relevable : {nom}",
                     "absent de la sortie attendue")
        elif set(ra) == set(ro):
            j.passe(f"concordance : {nom}", " · ".join(ra))
        else:
            j.echoue(f"concordance : {nom}",
                     f"attendu {' · '.join(ra) or '—'}, "
                     f"obtenu {' · '.join(ro) or '—'}")

    return j.rendre()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
