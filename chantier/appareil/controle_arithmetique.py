#!/usr/bin/env python3
"""Contrôle arithmétique des chiffres du corpus Résolution.

Rejoué à chaque versement du REF_doctrine. Chaque contrôle porte un identifiant
de nœud, l'opération déclarée dans la propriété `operation`, et la tolérance
admise. Un contrôle qui échoue nomme l'écart chiffré.

Tranches couvertes : D2 à D11. D1 et D12 ne portent aucune valeur numérique.
"""

import sys

ECHECS = []
CONSIGNES = []


def ctrl(nid, libelle, calcule, attendu, tol=0.005, unite=''):
    ecart = calcule - attendu
    ok = abs(ecart) <= tol
    if not ok:
        ECHECS.append((nid, libelle, calcule, attendu, ecart, unite))
    print(f"{'OK ' if ok else 'ECH'} {nid:<14} {libelle:<46} "
          f"{calcule:>12.4f} / {attendu:>12.4f} {unite}")
    return ok


def consigne(nid, libelle, valeur, unite=''):
    CONSIGNES.append((nid, libelle, valeur, unite))
    print(f"CSG {nid:<14} {libelle:<46} {valeur:>12.4f} {unite}")


# ------------------------------------------------------------------ données
# Relevés du classeur Synthèse Calculs Résolution 0819.
PT_CSG = 11.8          # Md€ par point, PLACSS 2024 Annexe 1
PTS = 9.2 + 0.5        # points de CSG et CRDS d'activité
ABATT = 0.9825         # assiette de la CSG rapportée au brut
SMIC_NET_2025 = 1426.30
SMIC_BRUT_2025 = 1801.80
MEDIAN_NET = 2190.0
MEDIAN_BRUT = 2886.26      # brut implicite, reconstitué du point de CSG mensuel
MOYEN_NET = 2733.0
MOYEN_BRUT = 3602.0
POP_RETRAITES = 17.0e6
POP_ACTIFS = 42.235e6
POP_FISCALE = 63.4e6
POP_PERSONNES = 68.0e6
CONSO = 1528.0         # Md€


def gain_mensuel(brut):
    """Gain mensuel de la suppression, à partir du brut.

    Le rapport net / brut n'est pas uniforme : 75,88 % au médian et au moyen,
    79,17 % au SMIC. Le gain se calcule donc sur le brut, jamais par application
    d'un rapport unique au net.
    """
    return brut * ABATT * 0.01 * PTS


# -------------------------------------------------------- croisement 1 et 3
print('\n--- D3-2-1-p4 : coût budgétaire ---')
ctrl('D3-2-1-p4', 'CSG + CRDS activité = 11,8 × 9,7', PT_CSG * PTS, 114.46, 0.01, 'Md€')
ctrl('D3-2-1-p4', 'CSG seule = 11,8 × 9,2', PT_CSG * 9.2, 108.56, 0.01, 'Md€')

print('\n--- D3-2-1-p1 et p7 : hausse du net ---')
ctrl('D3-2-1-p1', 'gain au médian', gain_mensuel(MEDIAN_BRUT), 275.0759, 0.05, '€/mois')
ctrl('D3-2-1-p1', 'taux au médian', gain_mensuel(MEDIAN_BRUT) / MEDIAN_NET * 100, 12.56, 0.01, '%')
ctrl('D3-2-1-p1', 'taux rapporté au brut', ABATT * PTS, 9.5303, 0.001, '%')
ctrl('D3-2-1-p1', 'rapport net / brut au médian', MEDIAN_NET / MEDIAN_BRUT * 100, 75.88, 0.01, '%')
ctrl('D3-2-1-p7', 'rapport net / brut au SMIC', SMIC_NET_2025 / SMIC_BRUT_2025 * 100, 79.16, 0.01, '%')
ctrl('D3-2-1-p7', 'gain au SMIC', gain_mensuel(SMIC_BRUT_2025), 171.716, 0.05, '€/mois')
ctrl('D3-2-1-p7', 'taux au SMIC', gain_mensuel(SMIC_BRUT_2025) / SMIC_NET_2025 * 100, 12.04, 0.01, '%')
ctrl('D3-2-1-e1', 'gain au net moyen', gain_mensuel(MOYEN_BRUT), 343.2796, 0.05, '€/mois')
consigne('D3-2-1-p1', 'écart ancre 13 % contre exact', 13 - 12.56, 'pt')

print('\n--- D3-2-1-e2 : solde entreprises ---')
ctrl('D3-2-1-e2', 'agrégat = somme des composants', -20.425 - 17.75, -38.175, 0.001, 'Md€')

print('\n--- D3-2-1-e3 : perte des retraités ---')
ctrl('D3-2-1-e3', 'agrégat = somme des composants', 0 - 9.7578 - 5.4242, -15.182, 0.001, 'Md€')
ctrl('D3-2-1-e3', 'unitaire = agrégat / 17,0 M', -15.182e9 / POP_RETRAITES, -893.06, 0.01, '€/an')

print('\n--- D3-2-1-e4 : effet inflation ---')
inflation = -18.9 - 4.95 - 2.725 + 5.4
ctrl('D3-2-1-e4', 'agrégat = somme des composants', inflation, -21.175, 0.001, 'Md€')
ctrl('D3-2-1-e4', 'unitaire = agrégat / 59,235 M',
     -21.175e9 / (POP_ACTIFS + POP_RETRAITES), -357.4745, 0.01, '€/an')
ctrl('D3-2-1-e4', 'mensuel = annuel / 12', -357.4745 / 12, -29.7895, 0.001, '€/mois')
ctrl('D3-2-1-e4', 'taux implicite sur la consommation', 21.175 / CONSO * 100, 1.39, 0.01, '%')
consigne('D3-2-1-e4', 'résidu de population non alloué',
         (POP_FISCALE - POP_ACTIFS - POP_RETRAITES) / 1e6, 'M')

print('\n--- croisement 1 : bouclage des effets généraux ---')
menages = 114.46 - 29.875 - 28.15
actifs = 114.46 - 20.1172 - 22.7258
retraites = 0 - 9.7578 - 5.4242
ctrl('D3-2-1', 'ménages = actifs + retraités', actifs + retraites, menages, 0.001, 'Md€')

print('\n--- D3-2-2-e1 : restitution de 600 € ---')
ECO = 183.9547 + 52.1
ctrl('D2-1-1-p1', 'économies restituables', ECO, 236.0547, 0.001, 'Md€')
mult = ECO / (PT_CSG * PTS)
ctrl('D3-2-2-e1', 'multiplicateur', mult, 2.0623, 0.001, '')
ctrl('D3-2-2-e1', 'restitution au médian', 275.0759 * mult, 567.2983, 0.01, '€/mois')
ctrl('D3-2-2-e1', 'part hors CSG-CRDS', 567.2983 - 275.0759, 292.2224, 0.01, '€/mois')
ctrl('D3-2-2-e1', 'restitution au SMIC', 171.716 * mult, 354.1357, 0.01, '€/mois')
ctrl('D3-2-2-e1', 'restitution au net moyen', 343.2796 * mult, 707.957, 0.01, '€/mois')
consigne('D3-2-2-e1', 'écart ancre 600 contre exact', 600 - 567.2983, '€/mois')

print('\n--- bouclage année 1 : écart de nomenclature ---')
gages = 43.1 + 9 + 44 + 33.3
manif = 75.2522 + 52.1
ctrl('D11', 'agrégat Gages', gages, 129.4, 0.001, 'Md€')
ctrl('D11', 'somme du détail Manifeste', manif, 127.3522, 0.001, 'Md€')
ctrl('D11', 'écart État', 44 - 41.8522, 2.1478, 0.001, 'Md€')
ctrl('D11', 'écart collectivités', 33.3 - 33.4, -0.1, 0.001, 'Md€')
ctrl('D11', 'écart total attribué', (44 - 41.8522) + (33.3 - 33.4), gages - manif, 0.001, 'Md€')
consigne('Gages C22', 'écart contre son propre détail', 33.4 - 33.3, 'Md€')

print('\n--- D7-2-2-e1 : rente viagère ---')
PAT = 8800.0            # arrondi d'aval de 8 823,53 €, base des rentes déjà instruites
EXACT_PAT = 600.0e9 / 68.0e6
for n, att in ((12, 884.07), (17, 668.38), (22, 552.18), (24, 519.62)):
    ctrl('D7-2-2-e1', f'rente sur {n} ans, base arrondie',
         PAT * 0.03 / (1 - 1.03 ** -n), att, 0.01, '€/an')
for n, att in ((12, 886.43), (17, 670.16), (22, 553.65), (24, 521.01)):
    ctrl('D7-2-2-e1', f'rente sur {n} ans, base exacte',
         EXACT_PAT * 0.03 / (1 - 1.03 ** -n), att, 0.01, '€/an')
consigne('D7-2-2-e1', 'marge du plancher de 500 € sur 24 ans',
         EXACT_PAT * 0.03 / (1 - 1.03 ** -24) - 500, '€/an')

# ============================================================ D2, D5, D6
print('\n--- D2-1-1-e1 : économies restituables ---')
ctrl('D2-1-1-e1', 'agrégat = somme des cinq composants',
     67.007 + 68.948 + 52.1 + 30.0 + 18.0, 236.055, 0.001, 'Md€')
ctrl('D2-1-1-e1', 'structures facultatives = ses composants',
     3.8 + 9.6 + 8.632 + 11.6 + 3.8 + 9.575 + 20.0, 67.007, 0.001, 'Md€')
ctrl('D2-1-1-e1', 'dépenses hors niches', 236.055 - 52.1, 183.955, 0.001, 'Md€')
consigne('D2-1-1-e1', 'part non issue de baisses de dépense', 30.0 + 18.0, 'Md€')

print('\n--- D2-2-1 et D2-3 : recensement des agences ---')
ctrl('D2-2-1-p1', 'fermetures = cession + suppression', 78 + 668, 746, 0.001, 'agences')
ctrl('D2-3-2-p1', 'conservées = EPIC musée + EPIC recherche + AI', 40 + 258 + 5, 303, 0.001, 'agences')
ctrl('D2-2-1-p1', 'total arrêté', 434 + 328 + 24 + 318, 1104, 0.001, 'agences')
ctrl('D2-2-1-p1', 'bouclage sur le total du classeur', 746 + 55 + 303, 1104, 0.001, 'agences')
consigne('D2-2-1-p1', 'écart des ancres arrondies au manuscrit', 750 + 300 + 50 - 1104, 'agences')

print('\n--- D2-2-1-e2 et D5-2-1-e2 : fonctionnement ---')
ctrl('D2-2-1-e2', 'agences + administrations d’État', 8.632 + 3.8, 12.432, 0.001, 'Md€')
consigne('D2-2-1-e2', 'écart ancre 12,4 contre exact', 12.432 - 12.4, 'Md€')
ctrl('D5-2-1-e2', 'échelons locaux non indispensables', 9.6, 9.6, 0.001, 'Md€')

print('\n--- D2-4-1-e2 : subventions et aides ---')
ctrl('D2-4-1-e2', 'entreprises', 22.548 + 6.6 + 12.3, 41.448, 0.001, 'Md€')
ctrl('D2-4-1-e2', 'particuliers et associations', 17.7 + 3.6 + 3.2 + 3.0, 27.5, 0.001, 'Md€')
ctrl('D2-4-1-e2', 'total', 41.448 + 27.5, 68.948, 0.001, 'Md€')

print('\n--- D2-4-1-e1 : solde du bénéficiaire d’aides ---')
FOYERS = 30.0e6
ctrl('D2-4-1-e1', 'perte par foyer', 27.5e9 / FOYERS / 12, 76.389, 0.01, '€/mois')
consigne('D2-4-1-e1', 'solde de deux bases distinctes', 275.0759 - 27.5e9 / FOYERS / 12, '€/mois')
consigne('D2-4-1-e1', 'écart ancre 220 contre solde arithmétique',
         220 - (275.0759 - 27.5e9 / FOYERS / 12), '€/mois')

print('\n--- statut_ancre : cohérence manuscrit contre classeur ---')
# Une valeur de statut classeur ne prévaut jamais sur une ancre du manuscrit.
# Les écarts ci-dessous sont consignés, jamais corrigés au détriment du manuscrit.
consigne('D4-3-2-e1', 'ancre manuscrit 16 contre classeur 16,6', 16.6 - 16.0, 'Md€')
consigne('D4-3-2-e1', 'ancre manuscrit 16 contre détail des taxes 26,1', 26.1 - 16.0, 'Md€')
consigne('D2-5-1-p2', 'ancre manuscrit 52 contre classeur 52,1', 52.1 - 52.0, 'Md€')
consigne('D2-1-1-e1', 'ancre manuscrit 236 contre classeur 236,055', 236.055 - 236.0, 'Md€')

print('\n--- D11-4-1 et D11-4-2 : séquence calendaire ---')
# La montée court depuis l'ouverture de la restitution au mois 6, non depuis
# l'entrée en vigueur. La séquence du manuscrit boucle sur douze mois et demi.
ctrl('D11-4-1-p1', 'six mois avant restitution', 3 + 3, 6, 0.01, 'mois')
ctrl('D11-4-2-p1', 'durée de montée à +2 % par mois', 13 / 2, 6.5, 0.01, 'mois')
ctrl('D11-4-2-p1', 'cible atteinte, compté depuis l’entrée en vigueur',
     6 + 13 / 2, 12.5, 0.01, 'mois')
ctrl('D11-4-2-p1', 'part restituée à la fin de la première année',
     129.4 / 236.055 * 100, 54.82, 0.01, '%')
consigne('D11-4-2-p1', 'écart de l’ancre « la moitié » à la part calculée',
         129.4 / 236.055 * 100 - 50, 'pt')

print('\n--- D2-5-1 : niches ---')
ctrl('D2-5-1-p1', 'cible = immédiat + restantes + sociales', 72.2 + 53.0 + 18.0, 143.2, 0.001, 'Md€')
ctrl('D2-5-1-p2', 'restitué = fiscales + sociales', 43.1 + 9.0, 52.1, 0.001, 'Md€')
ctrl('D2-5-1-p3', 'compensé = immédiat + restantes + sociales', 29.1 + 53.0 + 9.0, 91.1, 0.001, 'Md€')
ctrl('D2-5-1-e2', 'bouclage', 52.1 + 91.1, 143.2, 0.001, 'Md€')

print('\n--- D6 : effectifs et masse salariale ---')
AGENTS = 5803862
ctrl('D6-2-1-p1', 'postes = 10 % des effectifs', AGENTS * 0.10, 580386.2, 1.0, 'postes')
ctrl('D6-2-1-e1', 'taux = 580 386 / effectifs', 580386.2 / AGENTS * 100, 10.0, 0.01, '%')
consigne('D6-2-1-p1', 'écart ancre 580 000 contre exact', 580386.2 - 580000, 'postes')
ctrl('D6-2-2-e2', 'État et agences + locales', 9.575 + 20.0, 29.575, 0.001, 'Md€')
consigne('D6-2-2-e2', 'écart ancre 29,6 contre exact', 29.6 - 29.575, 'Md€')

# ============================================================ D7
print('\n--- D7 : patrimoine, ancres du manuscrit ---')
CESSIBLE = 600.0        # Md€, plancher, ancre manuscrit M-0966
PAR_FOYER = 20000.0     # €, ancre manuscrit M-0965
ctrl('D7-2-1-p1', 'foyers impliqués par les deux ancres',
     CESSIBLE * 1e9 / PAR_FOYER, FOYERS, 1.0, 'foyers')
ctrl('D7-2-1-p1', 'équivalent par personne',
     CESSIBLE * 1e9 / POP_PERSONNES, 8823.53, 0.01, '€')
consigne('D7-2-1-p1', 'écart arrondi 8 800 contre exact par personne',
         CESSIBLE * 1e9 / POP_PERSONNES - 8800, '€')
ctrl('D7-2-1-e1', 'patrimoine net implicite du foyer type', PAR_FOYER / 0.16, 125000.0, 1.0, '€')
ctrl('D7-2-2-e2', 'rendement total', CESSIBLE * 0.03, 18.0, 0.001, 'Md€')
ctrl('D7-2-2-e2', 'rendement par personne', 18.0e9 / POP_PERSONNES, 264.71, 0.01, '€/an')
ctrl('D7-2-2-e2', 'rendement par foyer', 18.0e9 / FOYERS, 600.0, 0.01, '€/an')
ctrl('D7-2-2-e2', 'équivalence des deux bases',
     18.0e9 / POP_PERSONNES * POP_PERSONNES, 18.0e9 / FOYERS * FOYERS, 1.0, '€')

# ============================================================ D8, D9, D10
print('\n--- D8-4-2-e1 : frais de gestion santé ---')
ctrl('D8-4-2-e1', 'frais par foyer', 16.9e9 / FOYERS, 563.33, 0.01, '€/an')
consigne('D8-4-2-e1', 'part du total retenue au plafond de 300 €', 300 / (16.9e9 / FOYERS) * 100, '%')

print('\n--- D9 : aide fondamentale et impôt ---')
CI = 550.0
ctrl('D9-2-1-p1', 'annualisation', CI * 12, 6600.0, 0.01, '€/an')
ctrl('D9-2-1-p1', 'coût brut, population totale',
     (54.5 + 1.24 + 14.1 * 0.5 + 0.435) * CI * 12 / 1000, 417.285, 0.01, 'Md€')
ctrl('D9-2-1-p1', 'coût brut, population fiscale',
     (50.4 + 1.24 + 13.04 * 0.5 + 0.435) * CI * 12 / 1000, 386.727, 0.01, 'Md€')
consigne('D9-2-1-p1', 'écart entre les deux bornes de population', 417.285 - 386.727, 'Md€')
ctrl('D9-2-3-p2', 'total handicap = aide + part', CI + CI, 1100.0, 0.01, '€/mois')
ctrl('D9-4-1-p1', 'aide par enfant = 550 × 0,5', CI * 0.5, 275.0, 0.01, '€/mois')
ctrl('D9-3-1-e1', 'net par euro gagné = 1 − 23 %', 1 - 0.23, 0.77, 0.001, '€')
consigne('D9-3-1-p1', 'largeur de l’encadrement du taux unique', 23.6 - 21.8, 'pt')
ctrl('D10-2-1-p1', 'compte éducation = 550 × 12', CI * 12, 6600.0, 0.01, '€/an')

# ============================================================ D11
print('\n--- D11 : taux de prélèvements et rythme ---')
PIB = 2919.9
ctrl('D11-e1', 'taux 2024', 1251.8 / PIB * 100, 42.87, 0.01, '%')
ctrl('D11-e1', 'taux cible', 1060.754 / PIB * 100, 36.33, 0.01, '%')
ctrl('D11-e1', 'baisse de prélèvements', 1251.8 - 1060.754, 191.046, 0.001, 'Md€')
consigne('D11-e1', 'écart économies contre baisse de prélèvements', 236.055 - 191.046, 'Md€')
consigne('D11-e1', 'solde non attribué après chômage et patrimoine',
         236.055 - 191.046 - 48.0, 'Md€')

# ------------------------------------------------------------------ synthèse
print(f"\n{len(ECHECS)} échec(s), {len(CONSIGNES)} écart(s) consigné(s)")
for nid, lib, cal, att, ec, un in ECHECS:
    print(f"  ECHEC {nid} — {lib} : {cal:.4f} contre {att:.4f}, écart {ec:+.4f} {un}")
sys.exit(1 if ECHECS else 0)
