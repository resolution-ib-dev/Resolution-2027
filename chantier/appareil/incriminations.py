#!/usr/bin/env python3
"""Inventaire des articles d'incrimination par strate — étapes 2 et 3 de
methode/procedure_revision_penale.md.

Lit le droit applicable aujourd'hui par `droit.py`, dans tous les codes de la
base, et écrit referentiels/incriminations.tsv : une ligne par article qui
punit, avec sa strate (L ou R/D), sa nature (crime, délit, contravention de
classe 1 à 5) et la peine relevée.

C'est un relevé lexical d'ARTICLES, pas de natures d'infraction : un article
peut porter plusieurs NATINF. Le rapprochement avec la nomenclature NATINF
(17 168 natures en 2026) se fait quand la nomenclature est au dépôt.

Emploi :
    python3 chantier/appareil/incriminations.py
"""
import csv
import gzip
import hashlib
import json
import pathlib
import re
import sys
from collections import Counter
from datetime import date

CHANTIER = pathlib.Path(__file__).resolve().parents[1]
RACINE = CHANTIER.parent
sys.path.insert(0, str(RACINE))
import droit  # noqa: E402

TSV = CHANTIER / "referentiels" / "incriminations.tsv"
MOTS = {"première": 1, "deuxième": 2, "troisième": 3, "quatrième": 4, "cinquième": 5}
RE_CONTRA = re.compile(
    r"contraventions? de (?:la )?(première|deuxième|troisième|quatrième|cinquième|[1-5]e|[1-5]ème) classe", re.I)
RE_PUNIT = re.compile(r"\bpuni|amende prévue", re.I)
RE_DELIT = re.compile(r"puni(?:e|s|es)? (?:de |d')((?:[\w\-]+ ){0,4}(?:ans?|mois)) d'emprisonnement", re.I)
RE_CRIME = re.compile(r"puni(?:e|s|es)? (?:de |d')((?:[\w\-]+ ){0,4})réclusion criminelle", re.I)


def classe(m):
    m = m.lower()
    return MOTS.get(m) or int(m[0])


def main():
    jour = str(date.today())
    mil, _, _ = droit.fraicheur()
    lignes, bilan = [], Counter()
    for c in droit._cfg():
        court = c["court"]
        try:
            index = droit.charger(court)
        except FileNotFoundError:
            continue
        for versions in index.values():
            appl = [v for v in versions if droit.applicable(v, jour)]
            if not appl:
                continue
            a = sorted(appl, key=lambda v: v.get("date_debut") or "")[-1]
            num, texte = a.get("num") or "", a.get("texte") or ""
            reglementaire = bool(re.match(r"^[RD]\*?\d", num))
            if reglementaire:
                classes = sorted({classe(m) for m in RE_CONTRA.findall(texte)}) if RE_PUNIT.search(texte) else []
                for k in classes:
                    lignes.append([court, num, a["id"], "R/D", f"contravention C{k}", ""])
                    bilan[("R/D", f"C{k}")] += 1
            else:
                m = RE_CRIME.search(texte)
                if m:
                    lignes.append([court, num, a["id"], "L", "crime", m.group(0)[:80]])
                    bilan[("L", "crime")] += 1
                m = RE_DELIT.search(texte)
                if m:
                    lignes.append([court, num, a["id"], "L", "délit", m.group(1).strip()])
                    bilan[("L", "délit")] += 1
    TSV.parent.mkdir(parents=True, exist_ok=True)
    with TSV.open("w", encoding="utf-8", newline="") as t:
        w = csv.writer(t, delimiter="\t", lineterminator="\n")
        w.writerow(["code", "num", "id", "strate", "nature", "peine_relevee"])
        w.writerows(sorted(lignes, key=lambda l: (l[0], droit.norm_num(l[1]), l[4])))
    print(f"base LEGI {mil}")
    for (s, n), v in sorted(bilan.items()):
        print(f"{s:4} {n:18} {v:6}")
    h = hashlib.sha256(TSV.read_bytes()).hexdigest()[:12]
    print(f"{TSV.relative_to(RACINE)} : {len(lignes)} lignes, sha256 {h}")


if __name__ == "__main__":
    main()
