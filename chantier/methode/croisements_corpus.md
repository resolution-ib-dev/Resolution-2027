# CROISEMENTS — Corpus complet, D1 à D12

Versé au `REF_doctrine_20260819_v10.json`. Contrôle rejouable :
`controle_arithmetique.py`, 71 contrôles, 0 échec, 25 écarts consignés.

Sources : `Synthèse_Calculs_Résolution_0819.xlsx` — onglets `Manuscrit`
(tableau de référence), `CSG`, `Gages`, `Manifeste`, `CI unique`,
`Détail Economies`, `Détail Niches`, `Fusion taxes`, `Perdants`.
`Synthèse_ETP_et_agences_Résolution_0819.xls` — onglets `Synthèse ETP`,
`Synthèse agences`. Manuscrit pour les ancres et les notes.

## État du peuplement

63 entrées porteuses de valeur numérique, huit propriétés chacune. D1 et D12 ne
portent aucune valeur numérique et sortent de la grille.

| verdict | nombre |
|---|---|
| POSÉ | 35 |
| APPROCHÉ | 15 |
| RECONSTITUÉ | 4 |
| POSÉ pour l'agrégat, RECONSTITUÉ pour l'unitaire | 2 |
| POSÉ pour le paramètre, RECONSTITUÉ pour le coût | 1 |
| POSÉ pour l'ancre, opération ou dimensionnement non instruit | 4 |
| NON INSTRUIT | 1 |

Aucun IRRÉDUCTIBLE. Le seul écart qui portait ce statut, le bouclage de l'année
1, est attribué.

## Défauts structurels relevés

### Valeur corrompue au REF v5 : 236 Md€ de niches

Le champ `bornes` de `D2-5-1-p1` portait « sur 236 Md€ de niches et taux réduits
recensés ». Aucun montant de cette nature n'existe. Le manuscrit dénombre 486
niches fiscales sans montant ; le classeur les valorise à 134,703 Md€. La valeur
était une contamination des 236 Md€ d'économies restituables. Bornes remplacées
par le recensement réel.

### Trois corrections de la version v7

La v7 avait porté la présomption sur le manuscrit au lieu du calcul, contre le
principe fondateur. Corrigé en v8.

| nœud | erreur v7 | rétabli en v8 |
|---|---|---|
| `D2-5-1-p1` | 236 Md€ de niches traités comme entrée homonyme | corruption corrigée, entrée supprimée |
| `D2-2-1-p1` | total ramené de 1 105 à 1 104 | ancre manuscrit de 1 105, écart de 1 consigné |
| `D7-2-1-p1` | 8 800 € traité comme ancre, 600 Md€ comme arrondi de 598,4 | 600 Md€ et 20 000 € par foyer sont les ancres, 8 823,53 € en découle |

Les 8 800 € ne figurent pas au manuscrit. Les ancres du patrimoine y sont : au
moins 600 Md€ d'actifs cessibles, 20 000 € par foyer, 16 % du patrimoine net du
foyer type, au moins 500 € par an et par personne de complément viager. Les deux
premières impliquent 30 M foyers exactement.

### Doublons d'identifiants au REF v5

Deux effets portaient `D2-2-1-e2` et deux portaient `D6-2-2-e2` : dans chaque
paire, un effet chiffré et un effet qualitatif. La règle d'identité était donc
violée dans le référentiel lui-même. Les effets qualitatifs sont renumérotés en
`D2-2-1-e3` et `D6-2-2-e7` ; les effets chiffrés conservent leur identifiant.
L'effet déplacé depuis `D8-2-3` prend `D9-3-1-e7`, `D9-3-1-e2` étant occupé.

### Rapport net sur brut non uniforme

79,16 % au SMIC contre 75,88 % au médian. Reconstituer un gain au SMIC depuis le
net avec le rapport du médian produit 179,16 € au lieu de 171,72 €, et 12,56 %
au lieu de 12,04 %. Tout gain se calcule sur le brut.

### Soustraction de deux bases dans un même chiffre

`D2-4-1-e1` affiche +220 €/mois comme différence de 300 € de gain salarial et
80 € d'aides perdues. Le gain est par personne au salaire médian, la perte est
par foyer sur 30 M foyers. Sur les valeurs exactes, 275,08 − 76,39 = 198,69 €,
mais la soustraction n'est pas licite en l'état : le solde réel dépend du nombre
de salaires du foyer.

## Croisement 7 — statut d'ancre

Croisement ajouté en cours de session, par balayage des 154 énoncés quantifiés du
manuscrit. Il décide seul du sens de la présomption en cas d'écart, et corrige la
cause des trois erreurs relevées ci-dessus.

| statut | nombre | règle |
|---|---|---|
| manuscrit | 42 | prévaut toujours ; l'écart du classeur est consigné, jamais corrigé au détriment de l'ancre |
| classeur | 19 | valeur de travail ; à déclarer comme telle dans tout emploi externe |
| absent des deux | 2 | non diffusable en l'état |

Cinq écarts de statut relevés, tous consignés au profit du manuscrit.

| ancre manuscrit | valeur classeur | écart |
|---|---|---|
| 236 Md€ d'économies | 236,055 | 0,055 |
| 52 Md€ restitués | 52,1 | 0,1 |
| 16 Md€ de taxes spécifiques | 16,6 nette, 26,1 en détail | 0,6 et 10,1 |
| 1 105 agences | 1 104 | 1 |
| 500 €/an de viager | 519,62 sur base arrondie, 521,01 sur base exacte | plancher tenu |

Quatre entrées sont des ancres du manuscrit dont l'opération manque : `D4-3-3-e1`,
`D7-3-1-e1`, `D8-2-1-p1`, `D9-3-1-e7`. Elles sortent de NON INSTRUIT — le défaut
est d'instruction, non de statut.

Le balayage ne voit que les grandeurs écrites en chiffres. `D11-4-1-p1`, classé
d'abord « absent des deux », est en réalité une ancre du manuscrit : les deux
phases de trois mois y sont écrites en lettres. Toute entrée classée « absent des
deux » se revérifie donc sur ses formes en lettres.

Six chiffres du manuscrit n'ont aucune entrée au REF : 48 Md€ de taxes sur la
main d'œuvre, environ 200 Md€ de cessions sur le parc social, 4,8 Md€
d'abattement « Papon », 438 impôts et 1,7 milliard de combinaisons de charges,
10 000 € par foyer de gain de qualité de vie, 5 points de croissance.

## Croisement 1 — agrégat contre composants

Onze bouclages testés, tous exacts.

| agrégat | composants | résultat |
|---|---|---|
| 236,055 Md€ économies | 67,007 + 68,948 + 52,1 + 30,0 + 18,0 | 0 |
| 67,007 structures facultatives | 3,8 + 9,6 + 8,632 + 11,6 + 3,8 + 9,575 + 20,0 | 0 |
| 68,948 subventions | 41,448 entreprises + 27,5 particuliers | 0 |
| 41,448 entreprises | 22,548 + 6,6 + 12,3 | 0 |
| 27,5 particuliers | 17,7 + 3,6 + 3,2 + 3,0 | 0 |
| 12,432 fonctionnement | 8,632 + 3,8 | 0 |
| 29,575 masse salariale | 9,575 + 20,0 | 0 |
| 143,2 niches cible | 72,2 + 53,0 + 18,0 | 0 |
| 52,1 restitué | 43,1 + 9,0 | 0 |
| 91,1 compensé | 29,1 + 53,0 + 9,0 | 0 |
| 1 104 agences | 746 fermées + 55 réinternalisées + 303 conservées | 0 |
| 56,435 ménages | 71,617 actifs − 15,182 retraités | 0 |

Passe.

## Croisement 2 — unitaire contre agrégat

| unitaire | agrégat | population | résultat |
|---|---|---|---|
| −893,06 €/an | −15,182 Md€ | 17,0 M retraités | tombe |
| −357,47 €/an | −21,175 Md€ | 59,235 M actifs et retraités | tombe |
| 20 000 €/foyer | 600 Md€ | 30 M foyers | tombe |
| 8 823,53 €/personne | 600 Md€ | 68 M personnes | tombe |
| 264,71 €/an | 18,0 Md€ | 68 M personnes | tombe |
| 600 €/an | 18,0 Md€ | 30 M foyers | tombe |
| 563,33 €/foyer | 16,9 Md€ | 30 M foyers | tombe |
| 76,39 €/mois/foyer | 27,5 Md€ | 30 M foyers | tombe |
| 580 386 postes | 5 803 862 agents | 10 % | tombe |
| 3 815,33 €/actif | 114,46 Md€ | **30 M en dur** | **ne tombe pas** |

Échoue une fois, sur `CSG!O12`, ligne sortie du périmètre diffusable.

Sept populations coexistent au corpus, toutes distinctes et toutes désormais
déclarées.

| effectif | libellé | emploi |
|---|---|---|
| 68 M | personnes résidentes | patrimoine, rendement, viager |
| 68,6 M | population totale 2025 | borne haute du coût de l'aide fondamentale |
| 63,4 M | population fiscale 2025 | borne basse du coût, référence, non diviseur |
| 59,2 M | actifs et retraités | effets ménages agrégés |
| 42,235 M | actifs dont demi-part enfant | effets par actif |
| 30 M | foyers | patrimoine par foyer, aides, frais de gestion |
| 29 M | travailleurs | colonnes « en moyenne » du tableau de référence |
| 17,0 M | retraités | effets par retraité |
| 5,80 M | agents publics | effectifs supprimés |

## Croisement 3 — conversion de base

| conversion | contrôle | résultat |
|---|---|---|
| annuel vers mensuel, inflation | −357,4745 / 12 | tombe |
| annuel vers mensuel, rendement | 264 / 12 = 22 | tombe |
| mensuel vers annuel, aide fondamentale | 550 × 12 = 6 600 | tombe |
| brut vers net, médian | 75,88 % | tombe |
| brut vers net, SMIC | 79,16 % | tombe |
| taux sur assiette, inflation | 21,175 / 1 528 = 1,39 % | tombe |
| taux sur assiette, prélèvements 2024 | 1 251,8 / 2 919,9 = 42,87 % | tombe |
| taux sur assiette, prélèvements cible | 1 060,754 / 2 919,9 = 36,33 % | tombe |
| foyer contre personne, D2-4-1-e1 | 76,39 €/foyer et 275,08 €/personne | **ne tombe pas** |

Échoue une fois, sur la soustraction de bases de `D2-4-1-e1`.

## Croisement 4 — rente contre rendement

| chiffre | qualification | valeur |
|---|---|---|
| 18,0 Md€ par an | rendement permanent, n'épuise pas le capital | exact, 600 × 3 % |
| 264,71 €/an par personne · 600 €/an par foyer | rendement permanent, deux bases équivalentes | exacts |
| 500 €/an viager | rente sur 24 ans à 3 % | 521,01 sur base exacte, 519,62 sur base arrondie |
| 886 / 670 / 554 €/an | rentes sur 12 / 17 / 22 ans | sur 8 823,53 € |

Rendement et rente ne se cumulent jamais sur le même capital. `D7-2-2-e2` porte
le rendement, `D7-2-2-e1` la rente. La double lecture des 18 Md€ est levée : la
ligne figure au tableau des économies comme ressource finançant la restitution,
non comme gain distinct s'ajoutant à celle-ci. Elle s'exprime indifféremment par
personne ou par foyer, l'équivalence étant écrite.

## Croisement 5 — homonymes

Sept paires relevées, toutes nommées au REF.

| valeur | origine 1 | origine 2 | qualification |
|---|---|---|---|
| 1 100 €/mois | pension de base, `D8-2-1-p1` | total handicap, `D9-2-3-p2` | deux entrées ; la seconde se construit en 550 + 550, la première n'a pas d'opération déclarée |
| 6 600 €/an | compte éducation, `D10-2-1-p1` | aide fondamentale annualisée, 550 × 12 | deux entrées de même valeur, non cumulables sans être nommées |
| 16 Md€ | taxes spécifiques supprimées, `D4-3-2-e1` | niches sur l'impôt sur les sociétés | deux entrées |
| 3 % | franchise à la transmission, `D4-4-2-p1` | rendement net du patrimoine, `D7-2-2-p1` | deux entrées |
| 300 € | gain CSG au médian, exact 275,08 | part épargne de la restitution, exact 292,22 | deux entrées, à ne jamais fusionner |
| 8 823,53 € et 9 463,72 € | 600 / 68 M | 600 / 63,4 M | même chiffre sur deux populations, tranché en faveur de 68 M |
| 9,6 Md€ | fonctionnement des échelons locaux, `D5-2-1-e2` | plan de départ État et agences arrondi de 9,575, `D6-2-2-e2` | deux entrées, la seconde arrondie |
| 30 Md€ | cotisations chômage, `D8-3-1-e2` | secteurs sensibles écartés, `D2-5-1-p5` | deux entrées, la seconde non instruite |

## Croisement 6 — renvois

Ce croisement a rattrapé une erreur de lecture. Le rythme de restitution de
`D11-4-2-p1` avait été porté en ANCRE CONTRADICTOIRE, faute d'avoir traversé son
renvoi vers `D11-4-1`. La séquence du manuscrit boucle sans contradiction :

| mois | étape |
|---|---|
| 0 à 3 | phase juridique |
| 3 à 6 | phase opérationnelle préparatoire |
| 6 | ouverture de la restitution |
| 6 à 12,5 | montée de +2 % de net par mois, 13 / 2 = 6,5 mois |
| 12,5 | cible de +13 % atteinte, « au bout d'un an » |

La part restituée à la fin de la première année, énoncée « la moitié », vaut
129,4 / 236,055 = 54,8 %.



Six entrées sont des renvois purs, sans production propre : `D2-5-1-e2`,
`D6-2-1-e1`, `D8-4-1-e1`, `D9-2-3-e1`, et le +13 % de `D3-2-1-e1`. Chacune
hérite de la base et de la portée de son origine sans rien redéfinir.

Un déplacement effectué : `D8-2-3-e1` devient `D9-3-1-e7`. La baisse d'environ
6 % au-delà de 1 600 € relève de la refonte fiscale (M-1502, M-1503), non de la
transition des retraites. `D8-2-3` ne porte plus que la garantie de pension au
moins équivalente.

Aucun chiffre modifié en valeur affichée, à trois exceptions près, qui
propagent :

| entrée | avant | après | propagation |
|---|---|---|---|
| `D7-2-2-e2` | 18 Md€, bénéficiaire foyers | 18 Md€, 264,71 €/an par personne et 600 €/an par foyer | fiches D7, Q&A patrimoine |
| `D8-2-3-e1` | sous D8 | `D9-3-1-e7` sous D9 | fiches D8 et D9, Q&A retraites |

## Écarts consignés

| écart | valeur | statut |
|---|---|---|
| ancre 13 % contre exact 12,56 % | 0,44 pt | arrondi assumé |
| ancre 600 € contre exact 567,30 € | 32,70 € | arrondi assumé |
| ancre 236,1 contre exact 236,055 | 0,045 Md€ | arrondi assumé |
| ancre 12,4 contre exact 12,432 | 0,032 Md€ | arrondi assumé |
| ancre 29,6 contre exact 29,575 | 0,025 Md€ | arrondi assumé |
| arrondi 8 800 € contre exact 8 823,53 € par personne | 23,53 € | arrondi d'aval, non une ancre |
| ancre 580 000 contre exact 580 386 | 386 postes | arrondi assumé |
| ancres agences 750 + 300 + 50 contre 1 105 | 5 agences | arrondi assumé |
| total manuscrit 1 105 contre classeur 1 104 | 1 agence | organismes centraux, 329 contre 328 |
| composants non issus de baisses de dépense dans les 236 Md€ | 48 Md€ | portée à déclarer |
| solde de `D2-4-1-e1` sur bases distinctes | 198,69 contre 220 affichés | base à reconstruire |
| bornes de population du coût de l'aide fondamentale | 30,558 Md€ | population à arrêter |
| encadrement du taux unique d'impôt | 1,8 pt | estimation assumée |
| plafond de frais de gestion santé | 53,25 % du total | part retenue à déclarer |
| économies contre baisse de prélèvements | 45,009 Md€ | dont 48 Md€ expliqués, solde de −2,991 Md€ à attribuer |
| résidu de population non alloué | 4,165 M personnes | portée à déclarer |
| `Gages!C22` contre son propre détail | 0,1 Md€ | valeur conservatrice conservée |
| 18,0 contre 18,447 Md€ au tableau de référence | 0,447 Md€ | 18,0 est exact, la divergence est au classeur |
| marge du plancher viager de 500 € | 21,01 €/an | plancher tenu |

## Cinq entrées NON INSTRUIT

Aucune opération traçable. À établir ou à retirer avant tout emploi externe.

| entrée | chiffre | manque |
|---|---|---|
| `D2-5-1-p5` | 30 Md€ de secteurs sensibles écartés | aucune cellule du classeur ne le porte |
| `D4-3-3-e1` | 81 % de la consommation en produits français | aucune source citée |
| `D7-3-1-e1` | +25 % d'offre locative privée, flux doublé | ni parc de référence, ni flux actuel |
| `D8-2-1-p1` | pension de base de 1 100 €/mois | aucun dimensionnement écrit |
| `D9-3-1-e7` | −6 % au-delà de 1 600 € | ni barème de départ, ni profil de l'effet |

## Vingt-six lacunes au registre

Portées au REF sur le nœud concerné, propriété `lacunes`. Elles se répartissent
en quatre familles : chaîne incomplète (7), base non déclarée (6), source
absente (6), décomposition non bouclée (5).

## Corrections classeur, à porter par les auteurs

Sans effet sur les ancres.

1. `CSG!P15` — clé de répartition moyennant une cellule vide avec 63,4.
2. `CSG!O12` — diviseur de 30 en dur, incohérent avec `CI unique!G29`.
3. `CSG!P20:P22` — rentes à recalculer sur 8 800 € par personne.
4. `Gages!C22` — 33,3 contre un détail qui somme à 33,4.
5. `Manuscrit!F` — colonne libellée « en € par an par personne » alors qu'elle
   arrondit la colonne H, exprimée par travailleur sur 29 M. Libellé à corriger.
6. `Manuscrit!N28` — 18,447 Md€ contre 18,0 en colonne C, qui explique à lui
   seul la non-additivité de la colonne des gains en année pleine.

## État du chantier

Douze tranches traitées. Entrées peuplées, six croisements passés sur chacune,
écarts consignés, REF versé en v7. Aucun IRRÉDUCTIBLE.

Reste à instruire, hors de ce fil : les cinq entrées NON INSTRUIT, les six
corrections classeur, et la propagation des trois valeurs modifiées vers les
fiches mesures et la Q&A.
