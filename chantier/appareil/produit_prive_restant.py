#!/usr/bin/env python3
"""Produit privé et produit privé restant, à la manière de Rothbard.

Inscrit le 20261020. Rejoue le classeur de l'auteur `T_1101_1103_PIBtoPPR.xlsx`
(SHA-256 f77645d2…4745b), puis le corrige.

Pièces lues :
  referentiels/insee_comptes_pib_apu_menages_1949_2025.tsv  INSEE 1.101, 7.301,
      3.201, 7.401 et le déflateur du 1.103, tels que le classeur les porte ;
      la colonne `ligne` est la ligne du classeur
  referentiels/produit_prive_formules_auteur.tsv  ses formules et valeurs 2024-2025
  referentiels/eurostat_heures_travaillees.tsv    heures travaillées

Les notions, au sens de Rothbard (Power and Market, ch. 5) :
  PP   produit privé = PIB − valeur ajoutée des administrations publiques
  DG   dépenses publiques tournées vers le privé, hors flux internes au circuit
  RG   recettes publiques, hors flux internes au circuit
  PPR  produit privé restant = PP − max(DG, RG)

Variantes :
  auteur      le classeur, à l'identique
  rothbard    toute la dépense et toute la recette, hors flux internes au circuit
              (cotisations et impôts sur la masse salariale publique) et hors
              production immobilisée pour compte propre, qui n'est pas un flux :
              le déficit retombe sur celui des comptes (B9). Crédits d'impôt
              retirés des deux côtés, comme le fait l'auteur
  credits     rothbard, crédits d'impôt gardés en dépense et en recette
              (arbitrage du 20261020)
  flux        rothbard, et les seuls flux réels de crédits d'impôt : la part
              imputée sur l'impôt dû n'est versée par personne et sort des deux
              côtés ; la part restituée est un décaissement du Trésor et reste en
              dépense (tableau 3.217, ligne « au-delà de l'impôt dû »)
  neutralise  le choix de l'auteur gardé : excédent brut d'exploitation public
              et autres acquisitions retirés de la dépense comme de la recette,
              erreurs de formule levées (maximum, production pour compte propre)
"""
import csv
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
REF = RACINE / "referentiels"
ANNEES = list(range(1959, 2026))

# Lignes du classeur
PIB, VAPUB, EBE, D12, D11_APU = 34, 64, 75, 68, 67
DEP, CI_DEP, P12_DEP, AUTRES_ACQ = 105, 108, 107, 103
REC, CI_REC, P12_REC = 136, 139, 138
D11_MEN, D613CE, D51_MEN, B2A3G, D4_MEN = 197, 237, 231, 195, 201
DEFL = 7


def charger():
    t = {}
    for r in csv.DictReader((REF / "insee_comptes_pib_apu_menages_1949_2025.tsv").open(encoding="utf-8"),
                            delimiter="\t"):
        cle = DEFL if r["tableau"].startswith("1.103") else int(r["ligne"])
        t[cle] = {int(k[1:]): float(v) for k, v in r.items() if k.startswith("y") and v}
    return t


def restitues():
    for r in csv.DictReader((REF / "insee_3217_payeur.tsv").open(encoding="utf-8"), delimiter="\t"):
        if r["ligne"] == "109":
            return {int(k[1:]): -float(v) for k, v in r.items() if k.startswith("y") and v not in ("", "n.d.")}
    return {}


def serie(t, variante="auteur"):
    s = {}
    rest = restitues() if variante == "flux" else {}
    for a in ANNEES:
        g = lambda l: t[l].get(a, 0.0)
        cot_pub = g(D11_APU) * g(D613CE) / g(D11_MEN)                       # ligne 300
        imp_pub = g(D11_APU) * g(D51_MEN) / (g(D11_MEN) + g(B2A3G) + g(D4_MEN))  # ligne 301
        circuit = g(D12) + cot_pub + imp_pub
        pp = g(PIB) - g(VAPUB)
        if variante == "auteur":
            dg = g(DEP) - g(CI_DEP) - g(EBE) - g(D12) - g(AUTRES_ACQ) - cot_pub - imp_pub
            rg = g(REC) - g(CI_DEP) - g(EBE) - g(D12) - g(AUTRES_ACQ) - cot_pub - imp_pub
            ppr = pp - dg                       # le classeur retranche DG, non le maximum
        else:
            dg = g(DEP) - circuit - g(P12_DEP)
            rg = g(REC) - circuit - g(P12_REC)
            if variante != "credits":
                dg -= g(CI_DEP)
                rg -= g(CI_REC)
            dg += rest.get(a, 0.0)
            if variante == "neutralise":
                dg -= g(EBE) + g(AUTRES_ACQ)
                rg -= g(EBE) + g(AUTRES_ACQ)
            ppr = pp - max(dg, rg)
        s[a] = dict(pib=g(PIB), vapub=g(VAPUB), pp=pp, dg=dg, rg=rg, mg=max(dg, rg), ppr=ppr,
                    ppb=pp - rg, deficit=dg - rg, cot_pub=cot_pub, imp_pub=imp_pub, defl=g(DEFL))
    return s


def croissance(s, cle, a):
    if a - 1 not in s:
        return None
    return (s[a][cle] / s[a]["defl"]) / (s[a - 1][cle] / s[a - 1]["defl"]) - 1


def heures():
    h = {}
    for r in csv.DictReader((REF / "eurostat_heures_travaillees.tsv").open(encoding="utf-8"), delimiter="\t"):
        if r["nace_r2"] == "TOTAL":
            h[int(r["annee"])] = float(r["milliers_heures"]) / 1e6        # milliards d'heures
    return h


def verifier(t):
    """Le rejeu de l'auteur doit redonner ses valeurs 2024 et 2025."""
    s = serie(t, "auteur")
    ecarts = []
    for r in csv.DictReader((REF / "produit_prive_formules_auteur.tsv").open(encoding="utf-8"), delimiter="\t"):
        cle = {"12": "pp", "16": "dg", "18": "rg", "21": "ppr", "25": "ppb", "300": "cot_pub",
               "301": "imp_pub"}.get(r["ligne"])
        if cle:
            for a, col in ((2024, "valeur_2024"), (2025, "valeur_2025")):
                if abs(s[a][cle] - float(r[col])) > 1e-4:
                    ecarts.append((r["ligne"], a, s[a][cle], r[col]))
    return ecarts


def main():
    t = charger()
    ecarts = verifier(t)
    print("Rejeu du classeur de l'auteur, 2024-2025 :", "concorde" if not ecarts else ecarts)
    h = heures()
    for v in ("auteur", "neutralise", "rothbard", "flux", "credits"):
        s = serie(t, v)
        x = s[2024]
        print(f"\n{v:10} 2024  PP {x['pp']:7.1f}  DG {x['dg']:7.1f}  RG {x['rg']:7.1f}  "
              f"PPR {x['ppr']:7.1f} = {x['ppr'] / x['pp'] * 100:4.1f} % du PP, "
              f"{x['ppr'] / x['pib'] * 100:4.1f} % du PIB ; RG/PP {x['rg'] / x['pp'] * 100:4.1f} %")
        hh = h[2024]
        print(f"         par heure : PIB {x['pib'] / hh:5.1f}  public {x['vapub'] / hh:5.1f}  "
              f"pris {x['rg'] / hh:5.1f}  à crédit {x['deficit'] / hh:5.1f}  restant {x['ppr'] / hh:5.1f}")
    s = serie(t, "auteur")
    print("\nAnnées d'excédent (RG > DG), où le classeur retranche DG au lieu du maximum :",
          [a for a in ANNEES if s[a]["rg"] > s[a]["dg"]])
    return 0 if not ecarts else 1


if __name__ == "__main__":
    sys.exit(main())
