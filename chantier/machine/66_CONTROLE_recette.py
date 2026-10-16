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
# Les quatre points qui font recette. Trois défauts relevés le 20261016 par le
# premier tiers qui a joué la recette, et corrigés ici :
#
# 1. **le véhicule n'était pas mesuré**, alors que le contrôle annonçait quatre
#    points. Il l'est.
# 2. **le vecteur se relevait sur toute la pièce**, exposé et notes compris, donc
#    une adresse citée en argument comptait comme un vecteur. Il ne se relève
#    plus que sur le DISPOSITIF.
# 3. **le gage attendait une clause de doctrine** — « concourt à la réduction des
#    prélèvements » — qui n'est pas un gage. Une mesure qui ne fait perdre aucune
#    recette n'en porte pas, et c'est une conformité, non un échec.
POINTS = {
    "vecteur": r"article\s+(L\.\s*\d+[-–]\d+(?:[-–]\d+)?)",
    "véhicule": r"\b(APRÈS L[’\']ARTICLE\s+\d+|ARTICLE\s+\d+|"
                r"ARTICLE ADDITIONNEL)",
    "entrée en vigueur": r"à compter du (\d{1,2}\w*\s+\w+\s+\d{4})",
    "gage": r"(compensée à due concurrence|créé un prélèvement|"
            r"majoration à due concurrence)",
}

# Le dispositif s'arrête à l'exposé : au-delà, une adresse est un argument.
FIN_DISPOSITIF = "EXPOSÉ SOMMAIRE"


def _dispositif(texte):
    """La part de la pièce qui fait droit, l'exposé et les notes exclus."""
    return texte.split(FIN_DISPOSITIF)[0]


def _releve(texte, motif):
    return sorted(set(m if isinstance(m, str) else m[0]
                      for m in re.findall(motif, texte, re.I)))


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", help="pièce rendue par le tiers, à confronter")
    ap.add_argument("--lot", default="1", choices=("1", "2"),
                    help="1 — la mesure simple ; 2 — les trois mesures difficiles")
    a = ap.parse_args(argv[1:])

    LOTS = {"1": ("50_RECETTE_enonce.md", "51_RECETTE_sortie_attendue.md"),
            "2": ("53_RECETTE_lot2_enonces.md",
                  "54_RECETTE_lot2_sorties_attendues.md")}
    f_eno, f_att = LOTS[a.lot]

    j = Journal(f"Test 5 — recette de bout en bout, lot {a.lot}")

    att = os.path.join(RACINE, f_att)
    eno = os.path.join(RACINE, f_eno)
    for p, nom in ((att, f_att), (eno, f_eno)):
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
    # Le compte se dérive de la pièce : un lot peut porter plusieurs amendements,
    # et l'un d'eux peut n'en être pas un — une mesure dont la chaîne doit
    # refuser de produire porte son motif, pas un cartouche.
    cartouches = len(re.findall(r"(?m)^AMENDEMENT$", t_att))
    with tempfile.TemporaryDirectory() as tmp:
        o = os.path.join(tmp, "cartouche.docx")
        _g.imprimer([att], o)
        textes = [p.text.strip() for p in __import__("docx").Document(o).paragraphs]
        for libelle, attendu in (("AMENDEMENT", "AMENDEMENT"),
                                 ("présenté par", "présenté par")):
            j.egal(f"cartouche rendu : {libelle}",
                   sum(1 for t in textes if t == attendu), cartouches)
        tirets = sum(1 for t in textes if re.fullmatch(r"-{4,}", t))
        j.egal("cartouche rendu : ligne de tirets", tirets, cartouches)

    blocs = t_att.split("EXPOSÉ SOMMAIRE")[1:]
    comptes = [len(re.findall(r"\w+", b.split("\n---")[0])) for b in blocs]
    hors = [n for n in comptes if not 150 <= n <= 450]
    if comptes and not hors:
        j.passe("exposés sommaires dans leur gabarit",
                " · ".join(f"{n} mots" for n in comptes))
    else:
        j.echoue("exposés sommaires dans leur gabarit",
                 f"{hors or 'aucun exposé lu'}, attendu 200 à 300 par exposé "
                 f"(tolérance 150-450)")

    try:
        g = _generateur()
    except Exception as e:                       # noqa: BLE001
        j.absent("générateur importable", str(e)[:60])
        return j.rendre()

    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "mini-lot.docx")
        rendu = g.imprimer([att], out)
        j.egal("amendements rendus au docx", rendu.amendements,
               len(re.findall(r"(?m)^## Amendement", t_att)))
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

    d_att, d_obt = _dispositif(t_att), _dispositif(t_obt)
    for nom, motif in POINTS.items():
        ra, ro = _releve(d_att, motif), _releve(d_obt, motif)
        if not ra and not ro:
            # Ni l'un ni l'autre ne porte ce point : les deux sont d'accord.
            # Une mesure sans perte de recette ne porte pas de gage, et les deux
            # pièces le disent de la même façon — c'est une concordance.
            j.passe(f"concordance : {nom}", "aucun des deux n'en porte")
        elif not ra:
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
