#!/usr/bin/env python3
"""Le passage complet du schéma « Refonte fiscalité » au tri des prélèvements.

Inscrit le 20261020. Pour chaque poste du schéma de l'auteur, il met côte à côte
ce que le schéma porte (montant 2024, taxes à supprimer) et ce que le tri y range
(prélèvements, rendement 2026 publié, sorts), et il juge la cohérence :

  poste maintenu   « taxes à supprimer » vide        → aucun rang fondu
  poste supprimé   « taxes à supprimer » = montant   → aucun rang maintenu
  poste partiel    entre les deux                    → les deux, déclaré
  impôt conservé   TVA, IR net, IS net, taxe foncière

Pièces : referentiels/schema_refonte_fiscalite_2024.tsv (onglet « Refonte
fiscalité » de Synthèse Chiffres Résolution_0910.xlsx, valeurs, SHA-256
3264cd06…), referentiels/sort_prelevements_20261015.tsv.

Sortie : livrables/tri_public/passage_schema_tri.tsv ; code retour 1 sur une
incohérence non déclarée.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
REF = RACINE / "referentiels"
SORTIE = RACINE / "livrables/tri_public/passage_schema_tri.tsv"
CONSERVES = {"TVA", "IR net", "IS net", "Taxe foncière"}
FONDUS = {"fondu par rattachement", "fondu dans l’équilibre"}
# Écarts connus et expliqués : poste → explication.
DECLARES = {
    "dont énergie*": "partiel : l'électricité fondue (le schéma supprime 8 Md€), les carburants maintenus",
    "dont alcool, tabac, jeux": "0,3 Md€ supprimés au schéma, sans prélèvement identifié au tri",
    "Taxes sur la main d'œuvre": "partiel : les forfaits de cotisation (8,8) maintenus, les stock-options "
                                 "fondues dans l'impôt sur le revenu (1,0), le reste dans l'équilibre (48)",
    "à titre onéreux": "partiel : remplacés par une franchise ; le solde est repris par la taxe foncière",
    "à titre gratuit": "partiel : remplacés par une franchise ; le solde est repris par la taxe foncière",
    "Taxes sur la consommation*": "agrégat des lignes « dont » qui suivent",
    "Droits de mutation": "agrégat des deux lignes « à titre onéreux » et « à titre gratuit »",
}


def tsv(chemin):
    return list(csv.DictReader(chemin.open(encoding="utf-8"), delimiter="\t"))


def f(x):
    return float(x) if x not in ("", None) else None


def table():
    schema = {r["poste"]: r for r in tsv(REF / "schema_refonte_fiscalite_2024.tsv")}
    rangs = defaultdict(list)
    for r in tsv(REF / "sort_prelevements_20261015.tsv"):
        rangs[r["ligne_schema"]].append(r)
    out = []
    for poste, s in schema.items():
        if poste.startswith("Total"):
            continue
        rs = rangs.get(poste, [])
        c, h = f(s["montant_2024"]), f(s["taxes_a_supprimer"])
        n_f = sum(1 for r in rs if r["sort"] in FONDUS)
        n_m = sum(1 for r in rs if r["sort"] == "maintenu à part")
        rend = sum(float(r["rendement_2026_M"]) for r in rs if r["rendement_2026_M"]) / 1000
        rend_f = sum(float(r["rendement_2026_M"]) for r in rs if r["rendement_2026_M"] and r["sort"] in FONDUS) / 1000
        if poste in CONSERVES:
            nature, ok = "impôt conservé", True
        elif h is None:
            nature, ok = "maintenu", n_f == 0
        elif c is not None and -h >= c - 0.05:
            nature, ok = "supprimé", n_m == 0
        else:
            nature, ok = "partiel", False
        verdict = "cohérent" if ok else ("déclaré : " + DECLARES[poste] if poste in DECLARES else "INCOHÉRENT")
        if ok and c is not None and nature != "impôt conservé" and rend > 1.5 * c + 0.5:
            verdict = f"cohérent ; montant à vérifier : {rend:.1f} Md€ rangés en 2026 pour {c:.1f} au schéma en 2024"
        if not rs and poste not in CONSERVES:
            verdict = "aucun prélèvement rangé à ce poste" + (" ; " + DECLARES[poste] if poste in DECLARES else "")
        out.append(dict(poste=poste.replace("*", ""), montant_2024=c, taxes_a_supprimer=h, nature=nature,
                        prelevements=len(rs), fondus=n_f, maintenus=n_m, rendement_2026=round(rend, 3),
                        rendement_fondu_2026=round(rend_f, 3), verdict=verdict))
    hors = rangs.get("—", [])
    par_sort = defaultdict(lambda: [0, 0.0])
    for r in hors:
        par_sort[r["sort"]][0] += 1
        par_sort[r["sort"]][1] += float(r["rendement_2026_M"] or 0) / 1000
    for srt, (n, m) in sorted(par_sort.items()):
        out.append(dict(poste=f"hors schéma — {srt}", montant_2024=None, taxes_a_supprimer=None, nature="hors schéma",
                        prelevements=n, fondus=n if srt in FONDUS else 0,
                        maintenus=n if srt == "maintenu à part" else 0, rendement_2026=round(m, 3),
                        rendement_fondu_2026=round(m, 3) if srt in FONDUS else 0.0, verdict="—"))
    return out


def main():
    t = table()
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    cles = list(t[0])
    with SORTIE.open("w", encoding="utf-8") as o:
        o.write("\t".join(cles) + "\n")
        for l in t:
            o.write("\t".join("" if l[k] is None else str(l[k]) for k in cles) + "\n")
    for l in t:
        print(f"{l['poste'][:38]:<38} {str(l['montant_2024'] or ''):>6} {str(l['taxes_a_supprimer'] or ''):>7} "
              f"{l['prelevements']:>4} {l['rendement_2026']:>8.2f}  {l['verdict']}")
    return 1 if any(l["verdict"] == "INCOHÉRENT" for l in t) else 0


if __name__ == "__main__":
    sys.exit(main())
