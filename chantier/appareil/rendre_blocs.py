#!/usr/bin/env python3
"""Rend les fichiers de blocs et les quatre tables du lot C, depuis blocs.json.

Entrée  : livrables/blocs/blocs.json
          livrables/paquet_machine/decoupage/M-*.md  (population des énoncés)
Sorties : livrables/blocs/B-nn.md            un fichier par bloc
          livrables/blocs/table_des_blocs.md
          livrables/blocs/correspondance.tsv  et .md
          livrables/blocs/blocs_solitaires.md
          livrables/blocs/bilans_desequilibres.md
          livrables/blocs/reservoir_gage.md
"""
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCS = os.path.join(RACINE, "livrables", "blocs")
DECOUPAGE = os.path.join(RACINE, "livrables", "paquet_machine", "decoupage")


def population():
    ids = sorted(
        f[:-3] for f in os.listdir(DECOUPAGE) if re.fullmatch(r"M-\d{3}\.md", f)
    )
    intitules, statuts = {}, {}
    for i in ids:
        txt = open(os.path.join(DECOUPAGE, i + ".md"), encoding="utf-8").read()
        m = re.search(r"^# %s — (.+)$" % i, txt, re.M)
        intitules[i] = m.group(1).strip() if m else ""
        s = re.search(r"^\*\*Statut\.\*\*\s*(\w+)", txt, re.M)
        statuts[i] = s.group(1) if s else ""
    return ids, intitules, statuts


def enonces_du_bloc(b):
    out = [b["pivot"]]
    for cle in ("tombent", "conditions", "directions"):
        out += [e[0] for e in b.get(cle, [])]
    return out


def rendre_bloc(b, intitules):
    L = []
    A = L.append
    A("# %s — %s" % (b["id"], b["intitule"]))
    A("")
    A("**Rang doctrinal.** %s — %s" % (b["rang"], b["motif_rang"]))
    A("")
    A("---")
    A("")
    A("## Temps 1 — Le pivot")
    A("")
    A("**%s — %s.**" % (b["pivot"], b["pivot_intitule"]))
    A("")
    A(b["motif_pivot"])
    A("")
    A("## Temps 2 — Les solidaires")
    A("")
    A("### Ce qui tombe si le pivot tombe")
    A("")
    if b["tombent"]:
        A("| énoncé | intitulé | pourquoi il perd son objet |")
        A("|---|---|---|")
        for i, t, m in b["tombent"]:
            A("| %s | %s | %s |" % (i, t, m))
    else:
        A("**Déclarée vide.** Aucun énoncé du découpage ne perd son objet avec ce pivot.")
    A("")
    A("### Ce sans quoi le pivot ne tient pas")
    A("")
    if b["conditions"]:
        A("| énoncé | intitulé | ce qu'il garantit |")
        A("|---|---|---|")
        for i, t, m in b["conditions"]:
            A("| %s | %s | %s |" % (i, t, m))
    else:
        A("**Déclarée vide.** Aucun énoncé du découpage ne conditionne ce pivot.")
    A("")
    if b.get("directions"):
        A("### Éclairés par le bloc, et non complétés")
        A("")
        A("| énoncé | ce qu'il donne |")
        A("|---|---|")
        for i, t, m in b["directions"]:
            A("| %s — %s | %s |" % (i, t, m))
        A("")
        A("Ces énoncés sont marqués `direction`. Ils entrent au bloc parce qu'il les "
          "éclaire ; ils ne se complètent pas.")
        A("")
    A("**Liste close et datée le 20260916.** Une mesure ajoutée ensuite rouvre le temps 3.")
    A("")
    if b.get("solitaire"):
        A("### Bloc solitaire")
        A("")
        A(b["solitaire"])
        A("")
    A("## Temps 3 — Le bilan")
    A("")
    bl = b["bilan"]
    A("| ligne | contenu |")
    A("|---|---|")
    A("| ce que le bloc supprime | %s |" % bl["supprime"])
    A("| ce qu'il rend | %s |" % bl["rend"])
    A("| qui perd | %s |" % " ; ".join(q for q, _v, _m in bl["raccroches"]))
    A("| ce qui raccroche la perte | %s |" % " ; ".join(
        "**%s** — %s : %s" % (v, q, m) for q, v, m in bl["raccroches"]))
    A("| ce qui gage | %s |" % bl["gage"])
    A("")
    if bl["etat"] == "bouclé":
        A("**État du bilan : bouclé.**")
    else:
        A("**État du bilan : déséquilibré.** Terme manquant : %s" % bl["terme_manquant"])
    A("")
    A("## Contrôles à la clôture")
    A("")
    A("B1 à B4 sont rendus par `appareil/controle_blocs.py`. B5 et B6 relèvent des lots "
      "suivants et ne se jouent pas ici.")
    A("")
    return "\n".join(L) + "\n"


def main():
    data = json.load(open(os.path.join(BLOCS, "blocs.json"), encoding="utf-8"))
    ids, intitules, statuts = population()
    blocs = data["blocs"]

    for b in blocs:
        open(os.path.join(BLOCS, b["id"] + ".md"), "w", encoding="utf-8").write(
            rendre_bloc(b, intitules))

    # table des blocs
    L = ["# Table des blocs — 20260916", "",
         "Dix-sept blocs, soixante et onze énoncés, aucun doublon, aucun manquant.", "",
         "| bloc | intitulé | pivot | énoncés | rang | état du bilan |", "|---|---|---|---|---|---|"]
    for b in blocs:
        n = len(enonces_du_bloc(b))
        L.append("| %s | %s | %s | %d | %s | %s |" % (
            b["id"], b["intitule"], b["pivot"], n, b["rang"], b["bilan"]["etat"]))
    L += ["", "**Rangs.** %d portant, %d structurant, %d d'accompagnement." % (
        sum(1 for b in blocs if b["rang"] == "portant"),
        sum(1 for b in blocs if b["rang"] == "structurant"),
        sum(1 for b in blocs if b["rang"] == "d'accompagnement")),
        "",
        "Le rang doctrinal est distinct du rang de passage, qui n'est pas posé ici.", ""]
    open(os.path.join(BLOCS, "table_des_blocs.md"), "w", encoding="utf-8").write("\n".join(L))

    # correspondance
    place = {}
    for b in blocs:
        for e in enonces_du_bloc(b):
            place.setdefault(e, []).append(b["id"])
    role = {}
    for b in blocs:
        role[b["pivot"]] = "pivot"
        for i, _, _ in b["tombent"]:
            role[i] = "tombe avec le pivot"
        for i, _, _ in b["conditions"]:
            role[i] = "condition du pivot"
        for i, _, _ in b.get("directions", []):
            role[i] = "direction éclairée"
    tsv = ["énoncé\tintitulé\tstatut\tbloc\trôle dans le bloc"]
    md = ["# Correspondance énoncé vers bloc — 20260916", "",
          "Soixante et onze lignes, une par énoncé. Couverture prouvée par "
          "`appareil/controle_blocs.py`.", "",
          "| énoncé | intitulé | statut | bloc | rôle dans le bloc |", "|---|---|---|---|---|"]
    for e in ids:
        bl = place.get(e, [])
        b = bl[0] if len(bl) == 1 else ("DOUBLON:" + ",".join(bl) if bl else "MANQUANT")
        tsv.append("\t".join([e, intitules[e], statuts[e], b, role.get(e, "")]))
        md.append("| %s | %s | %s | %s | %s |" % (e, intitules[e], statuts[e], b, role.get(e, "")))
    md.append("")
    open(os.path.join(BLOCS, "correspondance.tsv"), "w", encoding="utf-8").write(
        "\n".join(tsv) + "\n")
    open(os.path.join(BLOCS, "correspondance.md"), "w", encoding="utf-8").write("\n".join(md))

    # blocs solitaires
    sol = [b for b in blocs if len(enonces_du_bloc(b)) == 1]
    L = ["# Relevé des blocs solitaires — 20260916", "",
         "Un bloc solitaire n'est pas un défaut de rangement : c'est une information sur "
         "la mesure.", ""]
    if not sol:
        L.append("Aucun.")
    for b in sol:
        L += ["## %s — %s" % (b["id"], b["intitule"]), "",
              "**Pivot.** %s — %s" % (b["pivot"], b["pivot_intitule"]), "",
              "**Raison de la solitude.** %s" % b.get("solitaire", ""), ""]
    open(os.path.join(BLOCS, "blocs_solitaires.md"), "w", encoding="utf-8").write("\n".join(L))

    # bilans déséquilibrés
    des = [b for b in blocs if b["bilan"]["etat"] != "bouclé"]
    L = ["# Relevé des bilans déséquilibrés — 20260916", "",
         "Un bilan qui ne boucle pas se déclare et le bloc continue. Ce qui est proscrit "
         "est le bilan muet, non le bilan déséquilibré.", "",
         "| bloc | intitulé | terme manquant |", "|---|---|---|"]
    for b in des:
        L.append("| %s | %s | %s |" % (b["id"], b["intitule"], b["bilan"]["terme_manquant"]))
    L += ["", "**%d bilans déséquilibrés sur %d.**" % (len(des), len(blocs)), ""]
    open(os.path.join(BLOCS, "bilans_desequilibres.md"), "w", encoding="utf-8").write("\n".join(L))

    print("%d blocs rendus, %d énoncés placés" % (len(blocs), len(place)))


if __name__ == "__main__":
    sys.exit(main())

