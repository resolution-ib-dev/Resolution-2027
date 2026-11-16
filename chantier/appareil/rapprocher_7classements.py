#!/usr/bin/env python3
"""Rapprochement du tri des prélèvements avec la table « sept classements ».

Inscrit le 20261020. La table est une pièce tierce (un fiscaliste) : 142
lignes de prélèvements bruts 1995-2024, tirées du tableau 3.217 de l'INSEE,
chacune rangée selon sept classements — qualification juridique, INSEE,
SEC 2010, FMI, OCDE, ONU (UNU-WIDER), TAXUD. Elle est versée telle
qu'extraite de la page publiée, sans retouche :

  referentiels/prelevements_7classements_1995_2024.tsv
  referentiels/prelevements_7classements_passage.tsv

Le script ne croit ni la page ni notre livrable : il recompte.

  R1 — le passage du brut aux prélèvements obligatoires 2024 se rejoue sur
       la table et doit redonner 1 250,76 Md€ (INSEE, Informations rapides
       n° 81) à l'arrondi près.
  R2 — le bouclage écrit au compte rendu du 20260930 (huit assiettes,
       solde non ventilé, retraits) se rejoue tel qu'écrit, et se confronte
       au même total.
  R3 — les masses par assiette que le compte rendu publie se reconstituent
       ligne à ligne sur la table quand la ventilation est nommée.
  R4 — les répartitions de la table par classement, 2024, sont rendues.

Sortie : texte, sur la sortie standard. Code retour 1 si R1 échoue.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TABLE = RACINE / "referentiels/prelevements_7classements_1995_2024.tsv"
PASSAGE = RACINE / "referentiels/prelevements_7classements_passage.tsv"
PO_2024_INSEE = 1250.76
CLASSEMENTS = ["qj", "ins", "sec", "fmi", "ocde", "grd", "tx"]


def md(v):
    return v / 1000


def lire():
    lignes = list(csv.DictReader(TABLE.open(encoding="utf-8"), delimiter="\t"))
    passage = {r["annee"]: r for r in csv.DictReader(PASSAGE.open(encoding="utf-8"), delimiter="\t")}
    return lignes, passage


def somme(lignes, filtre):
    return md(sum(int(r["y2024"]) for r in lignes if filtre(r)))


def main():
    lignes, passage = lire()
    p = {k: md(int(v)) for k, v in passage["2024"].items() if k != "annee"}
    brut = somme(lignes, lambda r: True)
    po = brut - p["teom"] - p["cotisations_imputees"] + p["non_recouvre"] + p["credits_impot"]
    print("R1 — passage du brut aux prélèvements obligatoires, 2024")
    print(f"  brut {brut:.2f} − TEOM {p['teom']:.2f} − imputées {p['cotisations_imputees']:.2f}"
          f" − non recouvré {-p['non_recouvre']:.2f} − crédits {-p['credits_impot']:.2f} = {po:.2f}")
    r1 = abs(po - PO_2024_INSEE) < 0.02
    print(f"  INSEE {PO_2024_INSEE} : {'concorde' if r1 else 'ÉCART'}")
    hors = brut - p["teom"] - p["cotisations_imputees"]
    print(f"  brut hors TEOM et hors imputées : {hors:.2f}")

    print("\nR2 — bouclage écrit au compte rendu du 20260930")
    ecrit = 1248.09 + 26.77 - 51.22 - 4.62 - 19.49
    print(f"  1 248,09 + 26,77 − 51,22 − 4,62 − 19,49 = {ecrit:.2f} (écrit : 1 250,76)")
    sans_imputees = 1248.09 + 26.77 - 4.62 - 19.49
    print(f"  sans retrancher les imputées : {sans_imputees:.2f}")
    print(f"  1 248,09 + 26,77 = {1248.09 + 26.77:.2f} ; table, brut hors TEOM et imputées = {hors:.2f}")

    print("\nR3 — masses par assiette reconstituées sur la table, 2024")
    nom = lambda *m: (lambda r: any(x in r["libelle"] for x in m))
    fam = lambda *f: (lambda r: r["fam"] in f)
    cot = somme(lignes, lambda r: r["ins"] == "Cotisations effectives")
    csg = somme(lignes, fam("CSG, CRDS, prélèvements sociaux"))
    dep = somme(lignes, nom("Forfait social", "Contribution solidarité autonomie", "stock-options"))
    d291 = somme(lignes, lambda r: r["ins"] == "D291 Impôts sur les salaires")
    autres_sal = somme(lignes, nom("Autres taxes sur les salaires"))
    ir = somme(lignes, nom("Impôt sur le revenu (avant crédits d'impôt)"))
    d51 = somme(lignes, lambda r: r["ins"] == "D51 Impôts sur le revenu")
    print(f"  cotisations effectives {cot:.2f} (écrit 431,06)")
    print(f"  CSG + CRDS + prélèvements sociaux {csg:.2f} ; + forfait social, CSA, stock-options"
          f" {dep:.2f} = {csg + dep:.2f} (écrit 186,66)")
    print(f"  D291 {d291:.2f} − {dep:.2f} = {d291 - dep:.2f} (écrit 46,82) ;"
          f" « autres taxes sur les salaires » {autres_sal:.2f}")
    print(f"  IR avant crédits {ir:.2f} (écrit 96,16)")
    print(f"  D51 {d51:.2f} (écrit 359,03)")
    print("  D51 par famille :")
    for f, v in sorted(_par(lignes, "fam", lambda r: r["ins"] == "D51 Impôts sur le revenu").items(), key=lambda x: -x[1]):
        print(f"    {v:8.2f}  {f}")

    print("\nR4 — répartition 2024 par classement (Md€)")
    for k in CLASSEMENTS:
        print(f"  {k}")
        for c, v in sorted(_par(lignes, k).items(), key=lambda x: -x[1]):
            print(f"    {v:8.2f}  {c}")
    return 0 if r1 else 1


def _par(lignes, cle, filtre=lambda r: True):
    a = defaultdict(float)
    for r in lignes:
        if filtre(r):
            a[r[cle]] += md(int(r["y2024"]))
    return a


if __name__ == "__main__":
    sys.exit(main())
