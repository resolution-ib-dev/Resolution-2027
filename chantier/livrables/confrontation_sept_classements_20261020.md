# Confrontation du tri des prélèvements avec la table « sept classements » — 20261020

Pièce confrontée : page « Prélèvements FR, sept classements » remise par
l'auteur, travail d'un fiscaliste. Ouverte en entier (HTML publié, SHA-256
`d51923e7…6ee2`). Ses données sont versées telles qu'extraites, sans retouche :

| fichier | contenu |
|---|---|
| `referentiels/prelevements_7classements_1995_2024.tsv` | 142 lignes, 121 non nulles en 2024 ; montants bruts annuels 1995-2024 en M€ ; huit colonnes de rangement |
| `referentiels/prelevements_7classements_passage.tsv` | par année : TEOM, non recouvré, cotisations imputées, crédits d'impôt, PIB |
| `appareil/rapprocher_7classements.py` | le rapprochement, rejouable ; tous les chiffres ci-dessous en sortent |

Les deux travaux partent de la **même source**, le tableau 3.217 de l'INSEE,
exercice 2024. Ils ne répondent pas à la même question : le sien range un même
euro sous sept nomenclatures publiques ; le nôtre range 420 prélèvements par
matière taxée et les adresse en droit.

## 1. Ce qui concorde — relevé

| grandeur 2024 | sa table | notre compte rendu du 20260930 |
|---|---|---|
| passage aux prélèvements obligatoires | 1 335,51 − 9,43 TEOM − 51,22 imputées − 4,62 non recouvré − 19,49 crédits = **1 250,76** | 1 250,76 |
| cotisations sociales effectives | 431,06 | 431,06 |
| CSG + CRDS + prélèvements sociaux du capital | 176,86 | 153,13 + 9,08 + 14,65 = 176,86 |
| contributions sociales au sens de notre assiette 2 | 176,86 + forfait social 6,30 + CSA 2,47 + stock-options 1,03 = 186,66 | 186,66 |
| impôt sur le revenu avant crédits | 96,16 | 96,16 |
| D51 | 359,03 | 359,03 |

Le passage de sa table retombe à l'unité sur le chiffre INSEE : la pièce est
tenue.

## 2. Une erreur chez nous — relevée

Le bouclage écrit au compte rendu du 20260930 (§ « Le cadrage, et le
bouclage ») ne tombe pas juste :

> 1 248,09 + 26,77 − 51,22 − 4,62 − 19,49 = **1 199,53**, et non 1 250,76.

Les cotisations imputées n'ont jamais été dans les huit assiettes : l'assiette 1
vaut 431,06, les cotisations **effectives**. Les retrancher les retire deux fois.
Sans ce retrait, 1 248,09 + 26,77 − 4,62 − 19,49 = 1 250,75. Et 1 248,09 + 26,77
= 1 274,86, soit exactement le brut de sa table hors TEOM et hors imputées
(1 274,87).

**Seconde fragilité, déduite.** Notre assiette 4 nette déjà 8,88 de crédits
d'impôt (96,16 − 8,88 + 3,88), puis le bouclage retranche les 19,49 de crédits.
Le compte ne tombe juste que si les 8,88 reviennent par le « solde non ventilé »
de 26,77. Sa table le permet de voir : le résidu D51 que nos assiettes laissent
hors ventilation vaut 359,03 − 176,86 − 91,28 − 68,25 = 22,64, soit les
remises pharmaceutiques (9,68), le reste de l'impôt sur les sociétés au-delà de
nos 68,25 (5,83), le retour des 8,88 de crédits, moins 1,75 que notre assiette 4
compte au-delà de sa famille « impôt sur le revenu » (98,41 − 91,28 − 8,88).
Le résidu D291 vaut 1,35 (« autres taxes sur les salaires »,
1,36 chez lui). Restent 2,78 qu'on ne localise pas sans le classeur
`tri_impositions_20260930.xlsx`, non versé.

**Correction proposée** (non appliquée : le compte rendu est une pièce datée) :
« les huit assiettes somment à 1 248,09 ; s'y ajoutent 26,77 de solde non
ventilé, dont 8,88 de crédits d'impôt sur le revenu réintégrés, ce qui donne le
brut hors cotisations imputées et hors TEOM, 1 274,86 ; s'en retranchent 4,62
de non recouvré et 19,49 de crédits d'impôt : 1 250,75. »

## 3. Ce que sa table dit et que notre thèse doit absorber — déduit

**« Les contributions sociales valent deux fois l'impôt sur le revenu »** (notre
compte rendu) tient sur notre périmètre : 186,66 contre 91,28 net, rapport 2,04.
Sur le périmètre CSG-CRDS seul et l'impôt brut, le rapport tombe à 1,80
(176,86 / 98,41). L'argument reste juste, mais il se dit avec son périmètre ; à
défaut, l'objection « vous avez gonflé l'un et dégonflé l'autre » porte.

Sa série donne la dynamique que nous n'avons pas, et elle renforce la thèse :

| | 1995 | 2007 | 2019 | 2024 |
|---|---|---|---|---|
| prélèvements obligatoires, % du PIB | 42,7 | 42,3 | 44,0 | 42,6 |
| CSG-CRDS-prélèvements sociaux, % du PIB | 1,2 | 4,6 | 5,9 | 6,0 |
| cotisations effectives, % du PIB | 18,2 | 15,8 | 14,9 | 14,7 |
| impôt sur le revenu brut, % du PIB | 3,5 | 2,9 | 3,5 | 3,3 |

En trente ans, près de cinq points de PIB ont glissé de la cotisation, qui ouvre
des droits, à la contribution, qui n'en ouvre pas. L'impôt progressif n'a pas
bougé.

**Fonction économique (TAXUD), 2024**, sur 1 274,9 : travail 51,7 %, capital
23,7 %, consommation 24,6 %. Stable depuis 1995 (51,0 / 21,1 / 27,9). C'est la
seule nomenclature publique qui dise qui porte le prélèvement ; notre tri par
assiette ne la donne pas.

## 4. Où nos rangements divergent des siens — relevé

| prélèvement | chez nous | chez lui, et les sept classements | lecture |
|---|---|---|---|
| taxe sur les transactions financières | assiette 4, revenu des personnes, « revenus du capital » | droits d'enregistrement ; D214, OCDE 4400, FMI 114 | **contraire à notre propre règle** (« les droits de transaction sont soldés sur la propriété ») ; à reclasser en assiette 7 |
| redevances pour pollution de l'eau, modernisation des réseaux (2 485,7 M€) | assiette 6, sous-catégorie « Transport, véhicules et déplacements » | D214, « autres taxes sur services » | **sous-catégorie fautive chez nous** ; « Eau, déchets et boissons sucrées » existe |
| contributions sur les indemnités de rupture conventionnelle et de mise à la retraite | assiette 1, cotisations sociales | D291, taxes sur les salaires | n'ouvrent aucun droit : relèvent de l'assiette 2 ou 3 par notre propre critère |
| forfait social, CSA, stock-options | assiette 2, contributions | D291, taxes sur les salaires | arbitrage tenu par nous, documenté ; à garder |
| contribution sur les revenus locatifs | assiette 4, revenus fonciers | D214, services | notre rangement suit la matière ; le sien suit l'INSEE |
| taxe sur les surfaces commerciales | assiette 7, propriété | D292 ; OCDE 5000 | le tarif dépend du chiffre d'affaires au m² : défendable des deux côtés |
| CSG, CRDS | famille « prélèvement social » | qualification juridique « fiscal » | les deux sont vrais : la CSG est une imposition de toute nature (Conseil constitutionnel, 90-285 DC). Notre colonne « famille » n'est pas une qualification juridique et ne doit pas se lire comme telle |
| TEOM | assiette 7, fondue dans la taxe foncière | hors total INSEE, OCDE 4000 | 9,43 Md€ hors des prélèvements obligatoires : tout chiffre de masse de l'assiette 7 se dit hors ou avec la TEOM |

Absents de notre tri et présents chez lui, montant 2024 : contribution sur les
rentes inframarginales de l'électricité (0,13, éteinte), taxe de risque
systémique (0,03), contribution au fonds de résolution unique (non fiscale).
Rien de significatif.

## 5. Ce que chaque pièce a que l'autre n'a pas

**Sa table** : trente ans de série ; sept nomenclatures publiques, dont l'OCDE,
qui rend toute comparaison internationale immédiate ; la fonction TAXUD ; un
passage brut → prélèvements obligatoires explicite par année ; la ventilation
complète du D51 et du D291.

**Notre tri** : 420 prélèvements contre 121 lignes (il agrège « autres
taxes… ») ; un siège juridique pour 402 des 412 rangs d'imposition (hérité
de `CLAUDE.md`, mesure du 20261019, non rejouée ici) ; le rendement 2026
par prélèvement et son affectataire ; le sort de chaque prélèvement dans la
refonte ; une qualification à trois états (imposition, redevance, hors champ)
plus fine que son « fiscal / non fiscal ».

## 6. Réserves sur sa pièce — relevé

- Le titre annonce 1 335,5 Md€ de « prélèvements » ; 51,22 sont des cotisations
  imputées, qui ne sont prélevées sur personne. Le chiffre qui se cite est
  1 250,8.
- Sa ligne « remises pharmaceutiques (clause de sauvegarde) » mêle les remises
  conventionnelles, contractuelles, et la contribution de l'article L. 138-10 du
  code de la sécurité sociale, que nous qualifions d'imposition. Il la classe en
  bloc « non fiscal ». À trancher ligne à ligne avant toute citation.
- Les codes de classement d'aujourd'hui sont appliqués à toutes les années, ce
  qu'il déclare.
- Les PIB sont ceux d'Eurostat d'octobre 2026 : ses taux peuvent s'écarter de
  quelques dixièmes des taux publiés, ce qu'il déclare.

## 7. Suites proposées

1. Corriger le bouclage dans le prochain état du tri (§ 2).
2. Reclasser la TTF en assiette 7, les redevances eau dans leur sous-catégorie,
   les deux contributions sur indemnités hors de l'assiette 1 (§ 4). Effet sur
   les masses : à recompter au classeur.
3. Ajouter au tri trois colonnes de passage — code INSEE, code OCDE, fonction
   TAXUD — par appariement aux 121 lignes de sa table. Cela donne à chacun des
   420 rangs sa place dans les nomenclatures publiques sans rien changer à la
   nôtre.
4. Citer la glissade cotisation → contribution (§ 3) dans l'argumentaire : elle
   est sourcée INSEE, sur trente ans.

[interne] Rapprochement rejoué par `appareil/rapprocher_7classements.py` le
20261020 : R1 concorde, R2 écart relevé. Pièce tierce, non validée par l'auteur ;
reste au bac à sable.
