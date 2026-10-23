#!/usr/bin/env python3
"""Dossier de synthèse de la réécriture complète (passe 2), source de l'export Word.

Lit referentiels/code_cible_penal_bilan.json et referentiels/trois_colonnes_penal.tsv
(écrits par code_cible_penal.py), referentiels/bareme_delits.tsv et
revision/arbitrages_passe2.md. Écrit livrables/synthese_revision_penale.md.
Tout chiffre est compté sur ces fichiers au moment de l'écrire.
"""
import collections
import csv
import json
import pathlib
import re
import sys

CHANTIER = pathlib.Path(__file__).resolve().parents[1]
REF = CHANTIER / "referentiels"
csv.field_size_limit(sys.maxsize)
CODES = {"cpp": "Code de procédure pénale (2029)", "cp": "Code pénal", "penitentiaire": "Code pénitentiaire"}
VERBES = [("G", "gardés"), ("S", "simplifiés"), ("R", "réécrits"), ("F", "fusionnés"), ("A", "abrogés"),
          ("D", "déclassés"), ("M", "remontés à la loi"), ("C", "créés")]
DELITS = ["garder", "relever", "amende délictuelle", "contravention C5", "sanction administrative", "abroger"]


def n(x):
    """Séparateur de milliers : une espace insécable fine."""
    return f"{x:,}".replace(",", " ")


def typo(t):
    t = t.replace("'", "’")
    t = re.sub(r" ([:;?!»])", " \\1", t)
    t = re.sub(r"« ", "« ", t)
    return t


def main():
    bilan = json.loads((REF / "code_cible_penal_bilan.json").read_text(encoding="utf-8"))
    lignes = list(csv.DictReader((REF / "trois_colonnes_penal.tsv").open(encoding="utf-8"), delimiter="\t"))
    bar = list(csv.DictReader((REF / "bareme_delits.tsv").open(encoding="utf-8"), delimiter="\t"))
    arb = (CHANTIER / "revision" / "arbitrages_passe2.md").read_text(encoding="utf-8")
    params = collections.Counter()
    for l in lignes:
        for p in re.findall(r"\[[^\]]+\]", l["texte_cible"]):
            if p not in l["texte_2029"]:   # un crochet de la base n'est pas un paramètre
                params[p] += 1
    lots = {l["lot"] for l in lignes}
    tot = bilan["total"]
    out = ["**RÉÉCRITURE DE LA CHAÎNE PÉNALE**", "",
           "Dossier de synthèse de la passe 2", "",
           "Code de procédure pénale de 2029, code pénal, code pénitentiaire", "",
           "23 octobre 2026", "", "---", "",
           "# Synthèse", "",
           "## Objet", "",
           f"Chacun des {n(sum(b['articles_avant'] for k, b in bilan.items() if k != 'total') + tot['par_verbe'].get('C', 0))} articles "
           "de la chaîne pénale a été lu et jugé contre la grille des vingt-sept principes. Chaque décision porte un verbe, "
           "le principe qui la fonde, un motif et la ligne rouge examinée. Les textes cibles sont dérivés des opérations "
           "appliquées au texte en vigueur au 1er janvier 2029 : aucun ne s’écrit à la main.", "",
           f"Le travail s’est fait en {len(lots)} lots, un par titre, chacun contrôlé (couverture, forme, opérations, renvois, "
           "lignes rouges) puis relu en adversaire sur ses abrogations et ses réécritures avant d’être versé.", "",
           "## Bilan par code", "",
           "| code | articles avant | articles après | mots avant | mots après |",
           "|---|---|---|---|---|"]
    for k, nom in CODES.items():
        b = bilan[k]
        out.append(f"| {nom} | {n(b['articles_avant'])} | {n(b['articles_apres'])} | {n(b['mots_avant'])} | {n(b['mots_apres'])} |")
    out.append(f"| **Total** | **{n(tot['articles_avant'])}** | **{n(tot['articles_apres'])}** | **{n(tot['mots_avant'])}** | **{n(tot['mots_apres'])}** |")
    out += ["", "Les mots sont comptés comme suites de lettres et de chiffres. Un article fusionné ou abrogé sort du compte "
            "après réécriture.", "",
            "## Décisions par verbe", "",
            "| verbe | " + " | ".join(CODES.values()) + " | total |",
            "|---|---|---|---|---|"]
    for v, lib in VERBES:
        cs = [bilan[k]["par_verbe"].get(v, 0) for k in CODES]
        if sum(cs):
            out.append(f"| {lib} | " + " | ".join(n(c) for c in cs) + f" | {n(sum(cs))} |")
    cnt = collections.Counter(r["decision"] for r in bar)
    out += ["", "## Barème des délits", "",
            f"Les {n(len(bar))} délits du barème ont été jugés, par famille de code, en commençant par les délits formels.", "",
            "| décision | délits |", "|---|---|"]
    for d in DELITS:
        out.append(f"| {d} | {n(cnt.get(d, 0))} |")
    out += ["", "## Paramètres à arbitrer", "",
            f"Les textes cibles portent {n(len(params))} paramètres distincts entre crochets, "
            f"en {n(sum(params.values()))} occurrences. Les plus fréquents :", ""]
    for p, c in params.most_common(15):
        out.append(f"- {p} : {n(c)}")
    out += ["", "## Produits", "",
            "- Code cible complet : livrables/code_cible_penal.md.",
            "- Trois colonnes complet (texte actuel, texte 2029, texte cible, avec verbe, principe, motif et ligne rouge) : "
            "referentiels/trois_colonnes_penal.tsv.",
            "- Table de concordance (numéro actuel, numéro 2029, numéro cible) : referentiels/concordance_penale.tsv.",
            "- Décisions article par article : revision/decisions/, une pièce par lot.", "", "---", ""]
    corps = arb.split("\n", 1)[1]
    out += ["# Arbitrages", ""] + [l for l in corps.split("\n")]
    (CHANTIER / "livrables" / "synthese_revision_penale.md").write_text(typo("\n".join(out)) + "\n", encoding="utf-8")
    print(f"synthèse écrite : {len(lots)} lots, {len(params)} paramètres")


if __name__ == "__main__":
    main()
