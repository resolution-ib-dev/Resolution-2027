# Tri des impôts — le tri unique du 16 novembre

*Fil d’exécution du chantier n° 4, 20261116, branche `claude/tri-impots-unique`, sans pull
request. Chaque chiffre porte sa provenance : **[R]** relevé sur le fichier au moment de
l’écrire, **[H]** hérité et non rejoué, **[D]** déduit. Tout se rejoue depuis `chantier/` :*

```
python3 appareil/tri_porte/tri_unique.py            # la table, les rangs déplacés, le passage
python3 appareil/tri_porte/classeur_tri_unique.py   # le classeur, relu après écriture
python3 appareil/controle_sieges_prelevements.py    # lit le tri unique par défaut
```

## 1. Rendu

| pièce | adresse |
|---|---|
| la table | `referentiels/sort_prelevements_20261116.tsv` — 434 rangs, 33 colonnes [R] |
| le classeur | `livrables/tri_prelevements/Tri des impôts.xlsx` — Lisez-moi, Le tri, Par devenir, Par poste du tableau, Passage |
| les rangs déplacés | `livrables/tri_prelevements/rangs_deplaces_20261116.tsv` — 24 rangs, motif et statut |
| le passage | `livrables/tri_prelevements/passage_tableau_20261116.tsv` — 24 postes et 4 lignes hors tableau |
| les outils | `appareil/tri_porte/tri_unique.py`, `classeur_tri_unique.py` (nouveaux) ; `appareil/controle_sieges_prelevements.py` (tri par défaut) ; `Makefile` (cible `controle`, deux lignes) ; `appareil/tri_porte/LISEZ-MOI.md` |

Cinq colonnes ajoutées à la table : `mention`, `poste_tableau`, `regle_20261116`,
`statut_20261116`, `motif_20261116`. Les 28 colonnes du 3 novembre sont gardées, dans leur ordre.
Le tri du 3 novembre et ses classeurs ne sont pas modifiés.

## 2. Comptes par devenir, avant et après [R]

Rendement : `rendement_2026_M`, en M€. « Vides » : rangs sans rendement publié.

| devenir | 3 novembre : rangs | rendement | vides | 16 novembre : rangs | rendement | vides |
|---|---|---|---|---|---|---|
| grand impôt conservé | 7 | 463 638,5 | 2 | 7 | 463 638,5 | 2 |
| remplacé par un grand impôt | 265 | 304 743,5 | 89 | 258 | 302 767,8 | 83 |
| fondu dans l’équilibre des quatre grands impôts | 32 | 41 840,1 | 6 | 34 | 42 735,1 | 7 |
| conservé en complément | 42 | 64 050,8 | 12 | 45 | 65 990,4 | 15 |
| à fusionner | 82 | 2 212,8 | 77 | 80 | 1 317,8 | 76 |
| recette non fiscale | 6 | 1 743,7 | 1 | 10 | 1 779,8 | 4 |
| **total** | **434** | **878 229,4** | **187** | **434** | **878 229,4** | **187** |

Aucun rendement n’a changé (invariant contrôlé par l’outil) [R]. Les six blocs du devenir
« conservé en complément » : accise 15, simili TVA 8, fonds de garantie 6, fiscalité outre-mer 6,
taxe de séjour unique 6, Union européenne 4 [R].

## 3. Rangs déplacés, avec leur motif

24 rangs touchés [R] : **15 changent de devenir** (13 177,3 M€), **3 changent d’impôt cible ou
de bloc** (2 630,0 M€), **6 sont confirmés à leur place** par une qualification tranchée. Statut :
*pilotage* = tranché par le pilotage, révocable ; *fil* = tranché par ce fil sur les règles déjà
écrites, révocable.

| rang | prélèvement | M€ | avant | après | règle | statut | motif |
|---|---|---|---|---|---|---|---|
| 6 | indemnités de rupture conventionnelle | — | à fusionner | fondu dans l’équilibre | 1 | pilotage | taxe sur la main-d’œuvre, n’ouvre aucun droit (reclassement validé le 20261020) ; nature « contribution sociale », assiette « les revenus » |
| 12 | indemnités de mise à la retraite | 895,0 | à fusionner | fondu dans l’équilibre | 1 | pilotage | même motif |
| 135 | taxe sur les transactions financières | 2 630,0 | remplacé, impôt sur le revenu | remplacé, TVA | 1 | pilotage | rattachée au poste « autres taxes sur les produits », qui porte ses euros (troisième échange du 20261020) ; assiette « propriété et droits d’usage » |
| 137 | ordres annulés à haute fréquence | — | remplacé, impôt sur le revenu | remplacé, TVA | 1 | pilotage | suit la précédente |
| 211 | taxe sur l’électricité | 3 249,5 | conservé, accise | remplacé, TVA | 3 | pilotage | le tableau supprime 8 Md€ sur l’énergie : électricité fondue, carburants et gaz gardés |
| 214 | électricité, part des communes | 1 084,1 | conservé, accise | remplacé, TVA | 3 | pilotage | même motif |
| 215 | électricité, part des départements | 819,7 | conservé, accise | remplacé, TVA | 3 | pilotage | même motif |
| 194 | taxe de solidarité additionnelle | 6 654,8 | remplacé, TVA | conservé, simili TVA | 3 | pilotage | le tableau garde les 19,2 Md€ d’assurances |
| 277 | protection juridique | — | remplacé, TVA | conservé, simili TVA | 3 | pilotage | majoration de la taxe sur les conventions d’assurance, gardée avec elle |
| N7 | contribution des complémentaires santé (L. 862-4-1 CSS) | 434,0 | remplacé, TVA | conservé, simili TVA | 3 | **fil** | mêmes redevables et même assiette que la taxe de solidarité additionnelle [R au dépôt de droit] : la garder seule supprimée contredirait « rien de supprimé » |
| 136 | quota d’investissement des fonds de capital-risque | — | remplacé, impôt sur le revenu | recette non fiscale | 4 | fil | amende (art. 1763 C CGI : « redevable d’une amende ») [R] |
| 171 | emballages (REP) | — | remplacé, impôt sur les sociétés | recette non fiscale | 4 | fil | versée à un éco-organisme privé, aucune recette publique |
| 172 | équarrissage | — | remplacé, impôt sur les sociétés | recette non fiscale | 4 | fil | cotisation interprofessionnelle étendue, perçue par une interprofession privée |
| 187 | accidents du travail des exploitants agricoles | 4,1 | remplacé, impôt sur les sociétés | conservé, fonds de garantie | 4 | fil | fonds adossé à une assurance obligatoire, « à restituer dans la réforme des régimes, comme l’agriculture » (règle des six devenirs) |
| 188 | fonds de garantie des dommages de soins | — | remplacé, impôt sur les sociétés | conservé, fonds de garantie | 4 | fil | L. 426-1 C. assur. [R] : fonds adossé à une assurance obligatoire, le bloc s’étend à lui |
| 189 | contribution UNOCAM | — | remplacé, impôt sur les sociétés | conservé, simili TVA | 4 | fil | même objet que N7, la suit ; sans rendement propre |
| 326 | assurance-vie en déshérence | 36,1 | remplacé, taxe foncière | recette non fiscale | 4 | fil | sommes acquises à l’État |
| 300 | droits de place | — | conservé, bloc « à qualifier » | conservé, fiscalité outre-mer | 5 | fil | le bloc suit le poste du tableau (« outre-mer ») où la version du 20 octobre le range |
| 128 | médecine du travail | — | fondu dans l’équilibre | *confirmé* | 4 | fil | cotisation des employeurs par salarié (L. 4622-6 C. trav.) [R] : taxe sur la main-d’œuvre |
| 339 | droits d’enregistrement (ligne générique) | — | remplacé, taxe foncière | *confirmé* | 4 | fil | suit les droits de mutation |
| 363 | droits de plaidoirie | 123,5 | remplacé, impôt sur le revenu | *confirmé* | 4 | fil | la règle des six devenirs nomme la plaidoirie : un particulier, pour un acte |
| 382 | redevance hydraulique | 37,7 | remplacé, impôt sur les sociétés | *confirmé* | 4 | fil | une entreprise, pour le domaine public ; les redevances restent au tri |
| 388 | redevance des concessions hydroélectriques | — | remplacé, impôt sur les sociétés | *confirmé* | 4 | fil | même règle |
| 417 | garantie de l’or et de l’argent | — | remplacé, impôt sur les sociétés | *confirmé* | 4 | fil | la règle des six devenirs la nomme |

Les 13 qualifications en attente (201,4 M€ [R]) sont les rangs 128, 136, 171, 172, 187, 188,
189, 326, 339, 363, 382, 388, 417 : 7 déplacées, 6 confirmées.

**Trois choix de ce fil que le mandat ne dictait pas, à révoquer s’il y a lieu.**
- **N7 gardé avec la taxe de solidarité additionnelle** (434,0 M€) : le mandat ne nomme que la
  taxe et la protection juridique.
- **Droits de place en « fiscalité outre-mer »** : choix mécanique, par le poste. Sur le fond, c’est
  un droit communal de marché (L. 2224-18 CGCT [R]) ; l’autre lecture est « recette non fiscale ».
  Rang sans rendement, aucun effet chiffré.
- **171 et 172 en « recette non fiscale »** : le libellé du devenir dit « ce n’est pas un
  prélèvement obligatoire », ce qui est leur cas, mais ce ne sont pas des recettes publiques. La
  qualification des cotisations interprofessionnelles hors des impositions de toute nature est
  citée de mémoire (Conseil constitutionnel, 2012), **non relevée sur pièce**.

**Sans déplacement.** Règle 2 : les dix rangs de jeux étaient déjà « remplacé par la TVA » au
3 novembre ; ils portent désormais le statut « réponse de l’auteure » [R]. Règle 4 : les onze
redevances « en R » restent remplacées, mention « supprimé par voie réglementaire » (11 rangs,
942,0 M€, 4 vides [R]). Règle 5 : le libellé « droit ramené à 1 % et 3 % » est une mention en
colonne (9 rangs, part gardée 11 050,1 M€ [R]) ; la colonne `question` ne porte plus « False »
(106 cellules vidées ; il reste 3 cellules, les qualifications proposées des rangs N10, N15, N16) [R].

**Report de la version du 20 octobre.** La colonne `poste_tableau` reprend `ligne_schema` de la
table archivée pour les 418 rangs communs, libellé contrôlé rang par rang [R] : 279 rangs ont un
poste, 139 sont hors tableau. Les 16 rangs ajoutés le 3 novembre n’y étaient pas : 9 reçoivent un
poste par analogie [D] (N1, N2, N8 taxe foncière ; N3 transports ; N4 autres taxes sur les ménages ;
N5 autres taxes sur les entreprises ; N6 jeux ; N7 assurances ; N9 chiffre d’affaires et bénéfices),
7 restent hors tableau. Au total 288 rangs à un poste, 146 hors tableau [R]. Les redevances de
l’eau étaient déjà en « consommation » au 3 novembre [R].

**Millésime.** Prévision 2026 du budget 2026 pour les 418 rangs de base, sans changement [R].
**Exception déclarée** : 13 des 16 rangs ajoutés portent la prévision 2026 révisée du budget 2027
(1 665,5 M€ [R]), seule publiée pour eux ; l’annexe du budget 2026 n’est pas au dépôt. La colonne
d’attente `rendement_2026_revise_plf2027_M` est gardée, non employée.

## 4. Rapprochement avec le tableau « Refonte fiscalité »

Le classeur du site a été téléchargé ce jour (sha256 `ac56012f…`) et l’onglet comparé à
`referentiels/schema_refonte_fiscalite_2024.tsv` : 25 lignes, colonnes Montant 2024, Taxes à
supprimer et Hausses d’équilibre **identiques** [R]. Le classeur n’est pas modifié.

En M€. Tableau : montants 2024 des comptes nationaux. Tri : prévision 2026, somme des rangs
rattachés au poste [R]. « Supprimé » : rangs remplacés ou fondus, hors part gardée des droits de
mutation. Écart = tri moins tableau [D].

| poste du tableau | montant 2024 | à supprimer | rangs (vides) | tri 2026 | dont supprimé | dont gardé | écart de montant | écart sur le supprimé |
|---|---|---|---|---|---|---|---|---|
| TVA | 206 300 | — | 1 (0) | 242 838 | 0 | 242 838 | +36 538 | 0 |
| énergie | 43 700 | 8 000 | 10 (2) | 20 553 | 5 153 | 15 399 | −23 147 | −2 847 |
| alcool, tabac, jeux | 25 600 | 300 | 23 (5) | 23 072 | 6 867 | 16 205 | −2 528 | +6 567 |
| assurances | 19 200 | — | 9 (3) | 20 637 | 0 | 20 637 | +1 437 | 0 |
| redevances sur l’eau | 2 200 | 2 200 | 3 (0) | 2 675 | 2 675 | 0 | +475 | +475 |
| services de transports | 1 900 | 1 900 | 13 (1) | 3 624 | 3 624 | 0 | +1 724 | +1 724 |
| véhicules | 3 100 | 6 400 | 9 (3) | 3 862 | 3 862 | 0 | +762 | −2 538 |
| numérique, spectacles | 1 800 | 1 800 | 17 (1) | 2 216 | 2 216 | 0 | +416 | +416 |
| autres taxes sur les produits | 4 500 | 4 500 | 19 (1) | 6 486 | 6 086 | 400 | +1 986 | +1 586 |
| taxe de séjour | 1 100 | — | 8 (3) | 1 346 | 90 | 1 257 | +246 | +90 |
| taxe pollution | 1 000 | 1 000 | 2 (0) | 1 382 | 1 382 | 0 | +382 | +382 |
| outre-mer | 1 600 | — | 3 (2) | 1 744 | 0 | 1 744 | +144 | 0 |
| taxes sur la main-d’œuvre | 58 000 | 48 000 | 32 (7) | 42 646 | 42 646 | 0 | −15 354 | −5 354 |
| dont forfaits de cotisation | 8 800 | — | 2 (0) | 9 253 | 0 | 9 253 | +453 | 0 |
| impôt sur le revenu net | 87 300 | — | 10 (4) | 139 187 | 3 081 | 136 106 | +51 887 | +3 081 |
| impôt sur les sociétés net | 57 400 | — | 1 (0) | 84 694 | 0 | 84 694 | +27 294 | 0 |
| chiffre d’affaires et bénéfices | 10 300 | 10 300 | 16 (5) | 16 916 | 16 416 | 500 | +6 616 | +6 116 |
| taxe foncière | 42 900 | — | 22 (10) | 11 679 | 11 679 | 0 | −31 221 | +11 679 |
| autres taxes sur les ménages | 6 500 | 6 700 | 28 (9) | 4 172 | 4 136 | 0 | −2 328 | −2 564 |
| autres taxes sur les entreprises | 13 200 | 13 500 | 46 (19) | 8 636 | 8 632 | 4 | −4 564 | −4 868 |
| droits de mutation (ligne de total) | 37 900 | 32 450 | 5 (4) | 478 | 478 | 0 | *voir les deux lignes* | |
| à titre onéreux | 17 100 | 12 050 | 7 (0) | 19 280 | 14 230 | 5 050 | +2 180 | +2 180 |
| à titre gratuit | 20 800 | 20 400 | 2 (0) | 21 418 | 15 418 | 6 000 | +618 | −4 982 |
| *hors tableau* | | | 146 (108) | 189 435 | 185 783 | 591 | | |

Hors tableau [R] : 59 rangs remplacés (185 782,9, dont CSG 155 467,8, prélèvements de solidarité
15 634,9, CRDS 9 350,4) ; 80 cotisations à fusionner (1 317,8) ; 6 recettes non fiscales (1 743,7) ;
1 conservé (stocks pétroliers, 591,0).

**Les écarts, un par un** (texte complet à l’onglet « Passage »).

1. **Énergie, −2 847 sur le supprimé.** Le tableau supprime 8 000 ; le tri ne trouve que les trois
   rangs d’électricité, 5 153 [R]. Reste 2 847 que le tableau supprime et qu’aucun rang ne porte
   [D]. Le tableau est « corrigé du bouclier tarifaire » (note de l’onglet [R]) ; le montant de
   l’électricité avant bouclier n’a pas été relevé.
2. **Alcool, tabac, jeux, +6 567 sur le supprimé.** Voir § 5 : 6 392 pour les dix rangs de la
   règle 2, 175 pour N6, créé en 2025 et rattaché au poste par ce fil.
3. **Assurances, outre-mer, forfaits de cotisation : concordants** (rien de supprimé des deux côtés).
4. **Eau, transports, numérique, pollution, autres taxes sur les produits** : supprimés en entier
   des deux côtés ; l’écart est de montant (2024 contre 2026). Transports : 3 624 contre 1 900,
   dont billets d’avion 1 447, taxe d’aéroport 1 192, autoroutes 776 [R]. Autres produits : le tri
   garde la taxe « petit colis » (400), réponse de l’auteure du 3 novembre [H].
5. **Véhicules, −2 538.** Les 6 400 du tableau comprennent 3 300 de niches [R], hors du tri.
6. **Taxe de séjour, +90.** Remontées mécaniques et ski de fond fondus dans l’équilibre (règle de
   l’auteure du 3 novembre), quand le tableau garde le poste entier.
7. **Main-d’œuvre, −5 354.** Le tableau supprime 48 000 ; les 32 rangs du poste, tous fondus,
   pèsent 42 646, dont 7 sans rendement publié [R]. Cause non établie au-delà du millésime et des
   rangs vides.
8. **Impôt sur le revenu, +3 081 supprimés** : petites impositions du poste remplacées par l’impôt
   sur le revenu (rôles 2 414, CDHR 650, cessions de terrains 17) — elles s’y fondent, le tableau
   ne compte aucune suppression nette.
9. **Chiffre d’affaires et bénéfices, +6 116.** Contribution exceptionnelle des grandes
   entreprises, 7 300, créée en 2025, absente des 10 300 de 2024 [D] ; pilier 2 gardé (500).
10. **Taxe foncière.** La taxe foncière sur les propriétés bâties (rang 304) **n’a aucun rendement
    publié** : c’est le défaut déclaré du tri, et il explique l’écart de montant. Les 11 679
    « supprimés » sont 21 taxes locales remplacées par la taxe foncière (ordures ménagères 5 859,
    IFI 3 095) : fondues dans le poste que le tableau garde, aucune suppression nette [D].
11. **Autres taxes sur les ménages (−2 564) et sur les entreprises (−4 868).** Supprimés en entier
    des deux côtés ; 9 et 19 rangs sans rendement publié [R]. Le rang « autres taxes » a été ramené
    de 5 024 à 983 le 3 novembre [H].
12. **Droits de mutation.** Part gardée égale à celle du tableau : 5 050 et 6 000 [R]. À titre
    gratuit, les 20 400 du tableau comprennent 5 600 de niches et de gisement, hors du tri.

## 5. Effet de la règle 2 : les jeux supprimés en entier

- Le tri : 10 rangs (280 à 287, 289, 290), **6 692,2 M€** en prévision 2026 [R].
- Le tableau du site, ligne « dont alcool, tabac, jeux » : 25,6 Md€, **−0,3** à supprimer [R,
  cellules C18 et H18].
- **Écart : 6,39 Md€** [D : 6,69 − 0,30]. Avec N6 (publicité des jeux, 175,0 M€) : 6,57.

Mécanique du tableau [R sur les formules] : `K13 = K15 + K34 + K37 + K40` ; `K15` (TVA) est vide ;
`K34 = 7/20 × (C34 + E34 + G34)`, indépendant des suppressions ; **`K37`, taxe foncière, est le
solde** : `−J13 − K15 − K34 − K40`.

| cellule | aujourd’hui [R] | jeux supprimés en entier [D] | variation |
|---|---|---|---|
| H18, à supprimer sur alcool, tabac, jeux | −0,30 | −6,69 | −6,39 |
| H16, taxes sur la consommation | −26,10 | −32,49 | −6,39 |
| H13, total à supprimer | −137,05 | −143,44 | −6,39 |
| K13, hausses d’équilibre | 67,75 | 74,14 | +6,39, soit +9,4 % |
| K34, impôt sur les sociétés | 25,69 | 25,69 | 0 |
| K37, taxe foncière | 42,06 | 48,45 | +6,39, soit +15,2 % |

**Trois réserves.** Le tableau est en montants 2024, les 6,69 sont une prévision 2026 : le montant
2024 des jeux dans les 25,6 n’est pas isolé au tableau et n’a pas été relevé. Le tri donne la TVA
pour impôt de remplacement des jeux, mais les formules du tableau font porter tout l’écart à la
taxe foncière, la colonne K de la TVA étant vide. Les amendements n° 22 (I, 4° et 6°) et n° 29 (III bis, 2°) de la première partie et le PLFSS n° 9
portent déjà la suppression : c’est le tableau, non la liasse, qui est en retard sur la réponse de l’auteure.

## 6. Contrôles

| contrôle | résultat [R] |
|---|---|
| `tri_unique.py` | 0 échec : 434 rangs, six devenirs exactement, un bloc par rang conservé en complément, aucun « False », un impôt cible par rang remplacé, aucun rendement modifié |
| `classeur_tri_unique.py` | 0 écart à la relecture : cinq onglets, 434 lignes, six devenirs, aucune mention interne, aucun montant décimal, comptes rebouclés. Total 878 229 ; somme des cases arrondies 878 236, écart d’arrondi dit au Lisez-moi |
| `controle_sieges_prelevements.py` (défaut : tri unique) | **0 échec, 10 signaux.** 84 sièges sous contrôle ; S6 410/419 ; rapprochement 420/420 ; millésime LEGI 20261105 |
| même contrôle sur le tri du 3 novembre | 0 échec, 10 signaux ; S6 414/423 |

S6 passe de 423 à 419 rangs d’imposition : les quatre rangs requalifiés en recette non fiscale. Les
10 signaux sont les mêmes des deux côtés : 3 appariements par variante, 5 n.d., 2 sièges
réglementaires non relevés.

**Non rejoués** : `make controle` en entier, `make index`, `controle_liasses.py` (sa règle L6 lit
encore les porteurs du tri du 3 novembre, cohérents avec les liasses tant qu’elles ne sont pas
reprises). `make publier` et `make coffre` : non lancés.

## 7. Amendements que le tri unique oblige à reprendre

Listés, non touchés. Porteur relevé à la table du 3 novembre [R].

| pièce | reprise | rangs |
|---|---|---|
| **PLF P1 n° 36**, intégré le 9 novembre au **n° 22** | retirer le I, 5° (5° ter de l’article 1001 CGI, protection juridique) ; les jeux y restent (I, 4° et 6°) | 277 |
| **PLF P1 n° 22** | la taxe sur les transactions financières et les ordres annulés y restent abrogés ; l’exposé les rattache à la TVA et non plus à l’impôt sur le revenu | 135, 137 |
| **PLF P1 n° 22** ou pièce nouvelle | porter la fin de la taxe sur l’électricité (accise, CIBS L. 312-1 s.), part de l’État et parts locales : aucun dispositif ne la porte | 211, 214, 215 (5 153,3 M€) |
| **PLFSS n° 9** | retirer de son I, 1° et de son III, 3° la taxe de solidarité additionnelle (L. 862-4) et la contribution L. 862-4-1 ; l’intitulé « dix-huit impositions » est à recompter | 194, N7 (7 088,8 M€) |
| **PLFSS**, pièce à désigner | porter les contributions sur les indemnités de rupture et de mise à la retraite, désormais fondues dans l’équilibre | 6, 12 (895,0 M€) |
| jeux | quatre rangs supprimés sans porteur : fractions affectées aux communes et au patrimoine, « orphelins » | 285, 286, 287, 290 (228,2 M€) |

Rangs supprimés sans porteur : **34, 11 419,5 M€** [R] (36 et 5 411,4 M€ au 3 novembre [H]) ;
l’électricité et les indemnités de rupture font la hausse.

## 8. Restes, dits en clair

- **187 rangs sans rendement publié** : défaut déclaré, inchangé, dit au Lisez-moi et à chaque
  onglet de synthèse. Il comprend la taxe foncière sur les propriétés bâties.
- **« À fusionner » compte 80 rangs** et non plus 82 : l’entrée du registre « les 82 cotisations
  sociales » est à relire à l’insertion.
- **`chantier/CLAUDE.md`** désigne encore `prelevements_forces_20260930.tsv` pour « le sort des
  prélèvements » et dit que le classeur ne se publie pas : à mettre à jour par le pilotage.
- **Index** : les sept fichiers nouveaux ne sont pas déclarés (`generer_index.py` hors mandat).
- **`generer_tri_public.py` et `passage_schema_tri.py`** lisent toujours le tri du 15 octobre : ils
  sont remplacés par les deux outils nouveaux et peuvent être retirés.
- Le tableau du site reste à aligner sur la règle 2 (§ 5) : décision de l’auteure.

## 9. Entrées de registre rendues au pilotage

*Titrées, datées, sans numéro (A-282).*

### Tri des impôts : le tri unique du 16 novembre — 20261116

**Tranché par le pilotage, révocable**, sauf les jeux. Base : le tri du 3 novembre, six devenirs,
434 rangs. Reportés de la version du 20 octobre : le poste du tableau « Refonte fiscalité » (288
rangs à un poste, 146 hors tableau) et le passage ; les indemnités de rupture et de mise à la
retraite (6, 12) fondues dans l’équilibre comme taxes sur la main-d’œuvre ; la taxe sur les
transactions financières et les ordres annulés (135, 137) remplacés par la TVA. Le tableau fait
foi sur l’énergie et les assurances : électricité (211, 214, 215 ; 5 153,3 M€) fondue dans la TVA ;
taxe de solidarité additionnelle et protection juridique (194, 277) conservées en complément, bloc
simili TVA. Montants : prévision 2026 du budget 2026 ; 13 rangs ajoutés portent la prévision
révisée du budget 2027, seule publiée. Redevances « en R » : supprimées par voie réglementaire,
gardées au tri (11 rangs). *Relevé* : 7 / 258 / 34 / 45 / 80 / 10 rangs par devenir, 878 229,4 M€,
187 sans rendement. Pièces : `referentiels/sort_prelevements_20261116.tsv`,
`livrables/tri_prelevements/Tri des impôts.xlsx`, `methode/etats/TRI_unique_20261116.md`.
**Caduc** : « les 82 cotisations sociales » — elles sont 80.

### Jeux : supprimés — 20261116

**Validé.** *Réponse de l’auteure du 20261116* : « oui on supprime, cf synthèse refonte ». Les dix
rangs de jeux (6 692,2 M€) restent remplacés par la TVA. **Constaté** : le tableau « Refonte
fiscalité » du site n’en supprime que 0,3 Md€ ; l’écart de 6,39 Md€ porterait les hausses
d’équilibre de 67,75 à 74,14, en entier sur la taxe foncière (42,06 → 48,45), par la formule de
solde de la colonne K. Le classeur du site n’est pas modifié.

### Tri des impôts : les treize qualifications tranchées — 20261116

**Tranché** (par le fil du tri, sur les règles écrites, révocable). Recette non fiscale : amende des
fonds de capital-risque (136), emballages (171), équarrissage (172), assurance-vie en déshérence
(326). Conservé en complément, fonds de garantie : accidents du travail des exploitants agricoles
(187), dommages de soins (188). Conservé, simili TVA : contribution UNOCAM (189), avec la
contribution L. 862-4-1 (N7), qui suit la taxe de solidarité additionnelle. Confirmés : médecine du
travail (128, fondu), droits d’enregistrement génériques (339), plaidoirie (363), redevances
hydroélectriques (382, 388), garantie de l’or (417). Droits de place (300) : bloc fiscalité
outre-mer, par le poste. **Non relevé sur pièce** : la qualification des cotisations
interprofessionnelles (172).

### Tri des impôts : export ramené à six devenirs, contrôle des sièges promu — 20261116

**Tranché** (tambouille, révocable). « Droit ramené à 1 % et 3 % » et « supprimé par voie
réglementaire » sont des mentions en colonne, non des devenirs. La colonne `question` ne porte
plus « False ». `controle_sieges_prelevements.py` et la cible `controle` du `Makefile` lisent le
tri unique par défaut. *Relevé* : 0 échec, 10 signaux, S6 410/419.

### Les quatre échanges de l’auteure du 20 octobre : ce que le tri unique en porte — 20261116

**Constaté.** Portés : redevances de l’eau en consommation ; les deux reclassements d’assiette
(transactions financières, indemnités de rupture) ; la taxe sur les transactions financières au
poste « autres taxes sur les produits ». Sans effet sur le tri : cotisations imputées ignorées,
crédits d’impôt non retranchés, flux physiques privés, comparaison sur la notion INSEE, comptes
distribués écartés. **Caduc** : « cotisations sociales à unifier ». Le fragment archivé
`archive/tri_20261020/methode/fragments/arbitrages/20261020-flux-prives-et-classements.md` fait
foi et reste à verser au registre à sa date.

### Amendements à reprendre après le tri unique — 20261116

**Constaté, à traiter.** PLF P1 n° 22 (ex-n° 36) : retirer la protection juridique (I, 5°), porter
la fin de la taxe sur l’électricité. PLFSS n° 9 : retirer la taxe de solidarité additionnelle et la
contribution L. 862-4-1. Indemnités de rupture (6, 12) et quatre fractions de jeux (285, 286, 287,
290) sans porteur. *Relevé* : 34 rangs supprimés sans porteur, 11 419,5 M€.
