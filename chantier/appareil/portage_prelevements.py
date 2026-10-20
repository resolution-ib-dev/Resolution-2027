#!/usr/bin/env python3
"""Le portage des prélèvements : qui les remet au fisc, qui les supporte.

Inscrit le 20261020. Rejoue le calcul de l'auteur, puis le corrige sur pièces.

Pièces lues :
  referentiels/insee_3217_payeur.tsv              tableau 3.217 de l'INSEE,
      édition du classeur de l'auteur `T_3217_Impots_0902.xlsx` (SHA-256
      b66f4e45…8a8e), 1995-2025, avec sa colonne « Payeur »
  referentiels/insee_3217_payeur_corrections.tsv  ses cinq corrections, 2025,
      formule comprise
  referentiels/eurostat_prelevements_apu.tsv      Eurostat, gov_10a_main,
      gov_10a_taxag, nasa_10_nf_tr
  referentiels/prelevements_7classements_1995_2024.tsv  la table du fiscaliste

  P1 — le calcul de l'auteur, rejoué à l'identique. Doit redonner 1 153,214
       et 88,2 % (y compris prélèvement à la source) ; code retour 1 sinon.
  P2 — le même calcul, corrigé. Chaque correction est nommée, avec son
       origine : relevée (pièce publique), auteur (sans source), déduite.
  P3 — la fonction économique (TAXUD) de ce qui est prélevé, 2024.
"""
import csv
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
REF = RACINE / "referentiels"
AN = "y2025"
CREDITS = {76, 77, 79, 80}          # crédits d'impôt sur l'IRPP et l'IS


def tsv(nom):
    return list(csv.DictReader((REF / nom).open(encoding="utf-8"), delimiter="\t"))


def v(ligne, an=AN):
    x = ligne[an]
    return float(x) if x not in ("", "n.d.") else 0.0


def eurostat(item, annee, jeu="gov_10a_main"):
    for r in tsv("eurostat_prelevements_apu.tsv"):
        if r["na_item"] == item and r["annee"] == annee and r["jeu"].startswith(jeu):
            return float(r["valeur_M"]) / 1000
    raise KeyError((item, annee, jeu))


def part_csg_transferts_2024():
    """Part des revenus de remplacement dans CSG + CRDS, table du fiscaliste."""
    t = [r for r in tsv("prelevements_7classements_1995_2024.tsv")
         if r["libelle"].startswith(("Contribution sociale généralisée", "Contribution au remboursement"))]
    tot = sum(int(r["y2024"]) for r in t)
    trans = sum(int(r["y2024"]) for r in t if "Transferts" in r["libelle"])
    return trans / tot


def rendre(titre, base, postes):
    print(titre)
    print(f"  base privée {base:9.3f}")
    for nom, m in postes:
        print(f"  {nom:<12}{m:9.3f}   {m / base * 100:5.1f} %")


def main():
    L = {int(r["ligne"]): r for r in tsv("insee_3217_payeur.tsv")}
    C = {int(r["ligne"]): r for r in tsv("insee_3217_payeur_corrections.tsv")}
    tag = lambda n: L[n]["payeur_auteur"]
    corr = lambda n: float(C[n]["valeur_2025"])

    # --- P1 : le calcul de l'auteur, tel qu'écrit.
    po = v(L[110])
    base = po + corr(116) + corr(117)
    def somme(payeur, avec_pas, exclues=()):
        s = sum(v(L[n]) for n in L if tag(n) == payeur and n not in exclues)
        s += sum(corr(n) for n in (115, 116, 117) if C[n]["payeur_auteur"] == payeur)
        if avec_pas:
            s += sum(corr(n) for n in (118, 119) if C[n]["payeur_auteur"] == payeur)
        return s
    m, e = somme("Ménages", True), somme("Entreprises", True)
    rendre("P1 — calcul de l'auteur, 2025, y compris prélèvement à la source", base,
           [("ménages", m), ("entreprises", e), ("non affecté", base - m - e)])
    m0, e0 = somme("Ménages", False), somme("Entreprises", False)
    rendre("      hors prélèvement à la source", base,
           [("ménages", m0), ("entreprises", e0), ("non affecté", base - m0 - e0)])
    ok = abs(base - 1153.214) < 1e-3 and abs(e / base - 0.8819) < 1e-3

    # --- P2 : corrigé.
    print("\nP2 — corrections")
    brut = v(L[104]) + v(L[105]) + v(L[106])
    print(f"  base brute : (I) {v(L[104]):.3f} − non recouvré {-v(L[105]):.3f} − imputées {-v(L[106]):.3f}"
          f" = {brut:.3f} ; les crédits d'impôt ne sont pas retranchés  [auteur ; Eurostat de même]")
    ci_m = sum(v(L[n]) for n in CREDITS if tag(n) == "Ménages")
    ci_e = sum(v(L[n]) for n in CREDITS if tag(n) == "Entreprises")
    print(f"  crédits d'impôt retirés du compte : ménages {ci_m:.3f}, entreprises {ci_e:.3f}")
    print(f"  ligne {L[74]['libelle'].strip()!r} : {v(L[74]):.3f} passe aux entreprises, "
          "comme la ligne 73 — retenue par l'établissement payeur  [déduit]")
    part = part_csg_transferts_2024()
    csg_transf = part * (v(L[71]) + v(L[72]))
    print(f"  CSG-CRDS sur revenus de remplacement : {part * 100:.1f} % (fiscaliste, 2024) × "
          f"{v(L[71]) + v(L[72]):.3f} = {csg_transf:.3f}, au lieu de {-corr(116):.3f}  [déduit]")
    print(f"    la correction de l'auteur retirait aussi la CSG du capital, payée par des privés,"
          f" et mêlait 114 (2024, PLACSS) à des montants 2025")
    empl = eurostat("D12PAY", "2025") - (-v(L[106]))
    print(f"  cotisations employeurs publics : D12 APU {eurostat('D12PAY', '2025'):.3f} − imputées "
          f"{-v(L[106]):.3f} = {empl:.3f} (l'auteur : 70)  [relevé Eurostat, soustraction déduite]")
    print("  cotisations salariés publics : 30  [auteur, sans source]")
    d29 = eurostat("D29PAY", "2025")
    print(f"  impôts sur la production payés par les APU : {d29:.3f}  [relevé Eurostat]")

    base2 = brut - csg_transf - empl - 30 - d29
    pas_e, pas_m = corr(118), corr(119)
    m2 = sum(v(L[n]) for n in L if tag(n) == "Ménages" and n not in CREDITS | {74})
    e2 = (sum(v(L[n]) for n in L if tag(n) == "Entreprises" and n not in CREDITS) + v(L[74])
          + corr(115) - csg_transf - empl - 30 - d29)
    print()
    rendre("P2 — corrigé, 2025, hors prélèvement à la source", base2,
           [("ménages", m2), ("entreprises", e2), ("non affecté", base2 - m2 - e2)])
    rendre("      y compris prélèvement à la source (ratio de l'auteur, sans source)", base2,
           [("ménages", m2 + pas_m), ("entreprises", e2 + pas_e), ("non affecté", base2 - m2 - e2)])
    sal = eurostat("D11", "2024", "nasa_10_nf_tr")
    csg_pub = 0.097 * 0.9825 * sal
    print(f"\n  variante : sans la CSG-CRDS sur les traitements publics (9,7 % × 98,25 % × {sal:.1f},"
          f" salaires APU 2024, déduit des taux légaux) = {csg_pub:.1f} ; part des entreprises"
          f" {(e2 + pas_e - csg_pub) / (base2 - csg_pub) * 100:.1f} %")
    print("  non mesuré : prélèvement à la source sur traitements et pensions publics,"
          " TVA sur les achats publics")

    # --- P3 : fonction économique.
    print("\nP3 — fonction économique TAXUD, 2024, table du fiscaliste")
    t = tsv("prelevements_7classements_1995_2024.tsv")
    fonc = {}
    for r in t:
        fonc[r["tx"]] = fonc.get(r["tx"], 0) + int(r["y2024"]) / 1000
    tot = sum(x for k, x in fonc.items() if not k.startswith("Hors"))
    for k in ("Travail", "Consommation", "Capital"):
        print(f"  {k:<13}{fonc[k]:9.2f}   {fonc[k] / tot * 100:5.1f} %")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
