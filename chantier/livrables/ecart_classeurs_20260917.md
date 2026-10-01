# Écart entre les classeurs du 20260819-0423 et les classeurs mis au propre du 20260917

*Fil d'écart. Ce document part de la différence entre deux états, jamais d'un
inventaire réécrit. Aucune valeur n'y est produite, aucun classeur corrigé,
aucun trou comblé. Les onglets et les colonnes sont comparés cellule à cellule
par `appareil/socle_budgetaire.py` et par une confrontation mécanique des deux
états ; ce qui est déclaré identique l'a été prouvé, ce qui ne l'a pas été se
dit.*

**Périmètre mesuré** : 7 classeurs neufs, 6 antérieurs correspondants,
1 classeur antérieur sans successeur. 47 onglets d'un côté, 47 de l'autre.

---

## 1. La correspondance, classeur par classeur

| classeur du 20260917 | classeur antérieur | onglets |
|---|---|---|
| `PLF 2026_VM tome I - Annexe 2 - Taxes affectees_0910.xls` | `…Taxes affectees_IB_1113.xls` | 1 → 2 |
| `T_3305_APUL_Résolution_0910.xlsx` | `T_3305_APUL_IB_1118.xlsx` | 2 → 2 |
| `Synthèse ETP et agences Résolution_0910.xls` | `…_0819.xls` | 9 → 9 |
| `Synthèse Calculs Résolution_0910.xlsx` | `…_0819.xlsx` | 22 → 7 |
| `Synthèse Graphiques Résolution_0910.xlsx` | **aucun — classeur neuf** | 0 → 12 |
| `PLF 2026_VM tome II - Annexe 3 - Depenses fiscales - 0910.xls` | `…Depenses fiscales  IB  1126.xls` | 9 → 10 |
| `PLF26 - Depenses 2026 du BG et des BA…_0910.xls` | `…IB_1127.xls` | 4 → 5 |
| **aucun** | `deppee2025donneesfiche09ladepensepourleducation25 12 19IB.xlsx` | **sans successeur** |

**Les deux états coexistent aux pièces jointes du projet.** Les six classeurs
antérieurs n'ont pas été retirés ; rien ne dit lequel des deux fait foi, et rien
au corpus ne le déclare.

**Le classeur de la dépense d'éducation n'a pas de successeur au 20260917.** Le
bouclage `S16` porte sur lui ; il porte donc, depuis ce dépôt, sur une pièce
d'un autre millésime que les six autres.

### Onglet par onglet

**Taxes affectées** — 1 onglet → 2.

| ancien | neuf | ce qui change |
|---|---|---|
| — | `Synthèse TA` | **apparaît** — reprend la tête de l'onglet unique (L4:L15 de l'ancien) |
| `taxes affectées` | `taxes affectées` | en-têtes de L15:L16 à L2:L3, données de L17 à L4 ; 278 lignes de part et d'autre |

**T_3305 APUL** — 2 onglets → 2, aucun renommage.

| ancien | neuf | ce qui change |
|---|---|---|
| `Métadonnées` | `Métadonnées` | **0 divergence** sur 117 lignes |
| `T_3305` | `T_3305` | une colonne insérée en `AK` ; en-têtes d'interprétation réécrits |

**ETP et agences** — 9 onglets → 9, trois renommages.

| ancien | neuf | ce qui change |
|---|---|---|
| `Opérateurs` | `Opérateurs R` | **renommé — 0 divergence** sur 184 lignes × 19 colonnes |
| `Synthèse agences` | `Synthèse agences R` | **renommé — 1 divergence** : `C4` reçoit « Synthèse Résolution » |
| `ODAC-ODAL` | `ODAC-ODAL R` | **renommé — 0 divergence** sur 777 lignes |
| `Synthèse ETP`, `FPT`, `FPH`, `FPE`, `Emplois Etat RAP 2024`, `Annexe Etat` | idem | **0 divergence** sur chacun |

**Dépenses fiscales** — 9 onglets → 10.

| ancien | neuf | ce qui change |
|---|---|---|
| — | `Synthèse` | **apparaît** — reprend la tête de `Chiffrages IB` (L3:L13) |
| `Chiffrages IB` | `Chiffrages Résolution` | **renommé** ; en-têtes de L19:L20 à L5:L6, données de L21 à L7 ; 465 lignes de part et d'autre |
| les huit autres feuilles | idem | **0 divergence** sur chacune |

**Dépenses du budget général** — 4 onglets → 5, et l'onglet porteur est éclaté.

| ancien | neuf | ce qui change |
|---|---|---|
| `Synthèse` (226 l. × 20 c.) | `SynthèseR` (41 × 11) **+** `Economies R` (206 × 25) | **éclaté en deux** |
| — | `SynthèseR` | **apparaît** — synthèse de restitution, structure sans précédent |
| — | `Economies R` | **apparaît** — reçoit la grille, les 35 missions et les 128 programmes, décalés de 20 lignes |
| `Données PAP 2026`, `Crédits RAP 2024`, `Emplois RAP 2024` | idem | **0 divergence** sur chacun |

**Synthèse Calculs** — 22 onglets → 7. C'est le classeur le plus remanié.

| ancien | neuf | ce qui change |
|---|---|---|
| `Détail Economies` | `Détail Economies` | conservé ; 16 → 22 colonnes |
| `Détail Niches` | `Détail Niches` | **0 divergence** |
| `Manuscrit` | `Annexe Manuscrit` | renommé, 42 → 29 lignes, 9 colonnes de déclinaison retirées |
| `Gages` | `Flux` | renommé, **même gabarit** — L8:L26, colonnes B:J inchangées de place |
| `CSG` | `CSG-CRDS` | renommé ; le bloc « Effets généraux » (L:P) est retiré |
| `Capitalisation` | `Input Capitalisation` | renommé, restructuré |
| `Fusion taxes` + `CI unique` | `Refonte fiscalité` | **deux onglets fusionnés en un** |
| `Manifeste` | — | **disparaît sans équivalent** |
| `Perdants` | — | **disparaît sans équivalent** |
| les 12 onglets `Graph…` | → classeur des graphiques | **sortis du classeur** |

**Graphiques** — classeur neuf, 12 onglets, tous repris du classeur de calculs.

---

## 2. Les quatre listes, classeur par classeur

### Taxes affectées

**Disparu** — la tête de l'onglet unique (13 lignes), qui portait les totaux et
les sept affectataires isolés ; elle est reversée à `Synthèse TA`, valeurs
identiques.

**Nouveau** — l'onglet `Synthèse TA`.

**Montants qui bougent** — **aucun.** La comparaison cellule à cellule du bloc
de données rend **3 divergences, toutes de libellé** :

| cellule | ancien | neuf |
|---|---|---|
| K (2 lignes d'en-tête) | « Gage CSG net » | « Economie à horizon 1 an » |
| L | « économie pérenne en sus » | « Economie supplémentaire » |

**Périmètres qui changent** — le vocabulaire de l'interprétation, et lui seul.
`methode/grille_lecture_budgetaire.md` écrit « gage CSG » et « solde » en toutes
lettres pour ces deux colonnes.

### T_3305 APUL

**Disparu** — rien.

**Nouveau** — une colonne vide insérée en `AK`, qui décale d'un rang la colonne
de fusion et les deux lignes de total de tête.

**Montants qui bougent** — **aucun.** Les 71 lignes divergentes s'expliquent
toutes par l'insertion de colonne ; sous décalage, les valeurs sont identiques.

**Périmètres qui changent** — cinq en-têtes d'interprétation :

| ancien | neuf |
|---|---|
| Suppression immédiate | **Champ non indispensable** |
| Gage CSG | **Economie année 1** |
| gage CSG hors MS | **économie hors MS** |
| économie à terme | **économie en plus** |
| Fusion CI · 10 % fdg/social | **Fusion aide fondamentale** · 10 % fdg/social |

### ETP et agences

**Disparu** — rien. **Nouveau** — rien, hors le libellé « Synthèse Résolution ».

**Montants qui bougent** — **aucun**, sur les 9 onglets.

**Périmètres qui changent** — trois onglets prennent le suffixe ` R`. Le socle
les nomme en dur : `des_operateurs`, `des_agences` et `des_odac` cherchent
`Opérateurs`, `Synthèse agences` et `ODAC-ODAL`.

### Dépenses fiscales

**Disparu** — le bloc d'agrégats `R:T` des deux lignes d'en-tête, qui portait la
ventilation `S` / `E` :

| | S/E | gage | solde |
|---|---|---|---|
| S | 8 163 | 4 797,29 | 3 365,71 |
| E | 3 301 | 2 749,50 | 551,50 |

Ces six valeurs ne se retrouvent nulle part dans les pièces du 20260917.

**Nouveau** — l'onglet `Synthèse`.

**Montants qui bougent** — **aucun.** Le bloc des 465 dépenses fiscales rend
**0 divergence** de valeur ; les 15 divergences sont d'en-tête.

**Périmètres qui changent** — quatre en-têtes de colonne :

| colonne | ancien | neuf |
|---|---|---|
| K | % économie nette | **% effet net** |
| L | % effet macro | **% solde brut** |
| N | gage net CSG (M€) | **gage CSG (M€)** |
| O | effet macro | **solde PO** |

Les valeurs sont à l'octet les mêmes : c'est une requalification de ce que le
nombre est, non un nouveau nombre.

### Dépenses du budget général

**Disparu** — le bloc des **postes nommés** de la tête de `Synthèse`
(L5:L23, paires libellé / valeur). Sur ses 22 postes, **18 n'ont d'équivalent
nulle part** dans les sept classeurs du 20260917 :

| poste | valeur (M€) |
|---|---|
| Gage budgétaire CSG | 43 968,658369 |
| Économie pérenne en sus | 33 741,523730 |
| Taxes affectées (opérateurs) | 23 519 |
| Gage CSG — opérateurs | 14 499,952451 |
| Gage CSG — ménages | 8 425,583202 |
| hors FrTravail | 5 453,559710 |
| dont autre — opérateurs | 4 352,778457 |
| T2 FR Travail | 3 896 |
| dont autre — autres | 3 605,187552 |
| gage CSG — dont autre opérateurs | 2 546,375397 |
| T6 FR Travail | 1 869 |
| dont autre (hors après-mine) — ménages | 1 782,925138 |
| gage CSG — dont autre ménages | 1 604,632624 |
| dont autre — entreprises | 1 277,551162 |
| Gage CSG — salaires | 865,871586 |
| sur culture | 516,998084 |
| sur FrComp. | 434,071252 |
| poste sans libellé, catégorie 62 | 129,277098 |

Quatre autres — `dont HU` 3 068,234369, `dont AME` 1 216,3, `dont exo emploi à
dom` 1 180,117879, `dont Ademe` 1 100,781253 — ne se retrouvent que comme
**crédit de programme** dans `Economies R`, c'est-à-dire comme assiette et non
comme poste.

Disparaissent avec eux les **paramètres** de la même tête : « Non régalien »,
« Gage CSG », « Fusion CI (budgétaire + fiscal) », « Bourse (CB et TA) » — sauf
le salaire moyen et le nombre d'ETP supprimés, qui passent à `SynthèseR`.

**Nouveau** — 31 valeurs à `SynthèseR` sans antécédent dans la tête ancienne,
dont les trois lignes de restitution par destinataire et les quatre blocs de
détail (opérateurs, entreprises, ménages, associations) ; et, à `Economies R`,
**quatre colonnes « à arrêter »** par mission là où l'ancien ne portait le
chiffre qu'au total. Leur détail somme exactement au total connu :

| colonne | somme des 202 lignes | total écrit |
|---|---|---|
| salaires à arrêter | 3 206,931799 | 3 206,931799 |
| avantages salariaux à arrêter | 80,552315 | 80,552315 |
| fonctionnement à arrêter | 3 414,341134 | 3 414,341134 |
| investissement à arrêter | 1 316,240739 | 1 316,240739 |

**Montants qui bougent** — sur le bloc des 35 missions et 128 programmes,
**0 divergence** sur 202 lignes. Un seul montant bouge, et sa correspondance
est **par la place et par le libellé voisin, non prouvée** :

| poste | ancien | neuf | écart |
|---|---|---|---|
| gage CSG sur les salaires → « Economie à horizon 1 an · Salaires » | 865,871586 | 887,620711 | **+21,749125** |

**Périmètres qui changent** — la grille des dix catégories et la couche de
décision passent de `Synthèse` à `Economies R`, décalées de 20 lignes, avec dix
colonnes de montant renumérotées et la colonne « Mission régalienne » devenue
« Périmètre essentiel ».

### Synthèse Calculs

**Disparu** — huit onglets : `Manuscrit`, `Manifeste`, `CSG`, `Gages`,
`Fusion taxes`, `CI unique`, `Capitalisation`, `Perdants`, plus les douze
onglets `Graph…`. De ces huit, **deux disparaissent sans équivalent** :

- **`Manifeste`** — la ventilation des baisses de dépense par catégorie de
  perdant (entreprises, ménages, actifs, retraités, autres) ;
- **`Perdants`** — le dénombrement des populations (68 M de résidents,
  17 M de retraités, 5,8 M d'agents publics, 10,4 M en HLM…) et des perdants à
  1 an et à 3 ans.

Disparaissent aussi, à l'intérieur d'onglets conservés : le bloc
« Effets généraux » de `CSG` (13 valeurs, dont les effets nets à horizon 1 an
par catégorie) ; le bloc « Rationalisation des niches fiscales » de `Manuscrit`
(L30:L40) ; les trois variantes d'équilibre de `Fusion taxes` (options 1 à 3,
`L:N`) ; le tableau de break-even par demi-part de `Capitalisation` (K2:AJ2) ;
les postes « Effet retour du CI sur les retraites actuelles » (56,1) et
« Année 7 fonctionnaires » (20,7025).

**Nouveau** — `Refonte fiscalité` reprend le tableau des prélèvements
obligatoires de `Fusion taxes` et le schéma d'aide de `CI unique`, sous un
gabarit neuf : « Schéma PO Résolution », puis « Schéma de l'aide fondamentale
universelle couplée à l'impôt sur le revenu uniformisé ». `Flux` reprend
`Gages` au même gabarit. `Annexe Manuscrit` reprend `Manuscrit` sur quatre
colonnes.

**Montants qui bougent** —

`Détail Economies`, 13 cellules sur 7 lignes :

| ligne | grandeur | ancien | neuf | écart |
|---|---|---|---|---|
| Economies Etat | solde à restituer | 33,7 | 38,5 | **+4,8** |
| Economies Etat | total supprimé | 77,7 | 82,5 | **+4,8** |
| Opérateurs (y. c. salaires) | solde | 11 | 13,454667 | **+2,454667** |
| Opérateurs (y. c. salaires) | total | 25,5 | 28 | **+2,5** |
| dont France Travail | solde | 0,6 | 3,054667 | **+2,454667** |
| dont France Travail | total | 2,7 | 5,254667 | **+2,554667** |
| autres (opérateurs) | total | 2,8 | 2,745333 | **−0,054667** |
| Départs fonctionnaires Etat | solde | *vide* | 2,1 | **+2,1** |
| Départs fonctionnaires Etat | total | 0,9 | 3 | **+2,1** |
| Economies Collectivités locales | solde | 6,1 | 20,1 | **+14** |
| Economies Collectivités locales | total | 39,5 | 53,4 | **+13,9** |
| Départs fonctionnaires locaux | solde | *vide* | 14 | **+14** |
| Départs fonctionnaires locaux | total | 6 | 20 | **+14** |

`Gages` → `Flux`, 17 montants, cohérents avec les précédents :

| ligne | grandeur | ancien | neuf | écart |
|---|---|---|---|---|
| tête | gain à terme | 77,9 | 96,7 | **+18,8** |
| tête | total supprimé à terme | 207,49 | 226,2 | **+18,71** |
| tête | autre gisement | 95,8 | 97 | **+1,2** |
| Economies Etat | gain à terme | 33,7 | 38,5 | **+4,8** |
| Economies Etat | total | 77,7 | 82,5 | **+4,8** |
| Economies Etat | gisement | 42,8 | 44 | **+1,2** |
| Opérateurs | gain à terme | 11 | 13,454667 | **+2,454667** |
| Opérateurs | total | 25,5 | 28 | **+2,5** |
| Opérateurs | gisement | *vide* | 0,9 | **+0,9** |
| Aides aux entreprises | gisement | 11 | 11,3 | **+0,3** |
| Subventions aux associations | gisement | *vide* | 0,4 | **+0,4** |
| Départs fonctionnaires Etat | gain à terme | *vide* | 2,1 | **+2,1** |
| Départs fonctionnaires Etat | total | 0,9 | 3 | **+2,1** |
| Economies Collectivités | gain à terme | 6,1 | 20,1 | **+14** |
| Economies Collectivités | total | 39,49 | 53,4 | **+13,91** |
| Départs fonctionnaires locaux | gain à terme | *vide* | 14 | **+14** |
| Départs fonctionnaires locaux | total | 6 | 20 | **+14** |

`Capitalisation` → `Input Capitalisation`, 11 montants :

| poste | ancien | neuf | écart |
|---|---|---|---|
| Total des actifs à restituer | 636,100143 | 606,972666 | **−29,127477** |
| Participations financières | 208,28 | 201,915 | **−6,365** |
| Patrimoine foncier public | 200,195372 | 200,195372 | *inchangé* |
| Logements publics | 57,733333 | 51,96 | **−5,773333** |
| Parc social | 169,891438 | 152,902294 | **−16,989144** |
| taux de rendement appliqué | 0,029 | **0,03** | +0,001 |
| rendement net annuel | 18,446904 | 18,209180 | **−0,237724** |
| flux annuels à affecter | 123,889404 | 121,749180 | **−2,140224** |
| flux économisé | 84,74 | 103,54 | **+18,8** |
| économie budgétaire en année pleine | 33,7 | 38,5 | **+4,8** |
| économie locale en année pleine | 6,1 | 20,1 | **+14** |

`Manuscrit` → `Annexe Manuscrit`, sur les quatre colonnes conservées :

| ligne | grandeur | ancien | neuf | écart |
|---|---|---|---|---|
| Total des économies | gain supp. en année pleine | 109,149404 | 108,911680 | **−0,237724** |
| Patrimoine public valorisé et restitué | gain supp. | 18,446904 | 18,209180 | **−0,237724** |
| Extinction des niches sur la TVA et les sociétés | gain supp. | 2 | « - » | **−2** |
| Economies sur les structures facultatives | gain supp. | *vide* | 27,9025 | *cellule renseignée* |
| Economies sur les subventions | gain supp. | *vide* | 32,8 | *cellule renseignée* |

Les colonnes `Md€ par an`, `€ par an par foyer` et `Gain en année 1` sont
identiques ligne à ligne : **236,054667 Md€ et 127,352167 Md€ ne bougent pas.**

`Fusion taxes` → `Refonte fiscalité`, 6 montants :

| poste | ancien | neuf | écart |
|---|---|---|---|
| Total — taxes à supprimer | −148 | −137,05 | **+10,95** |
| Total — solde à compenser | −78,7 | −67,75 | **+10,95** |
| Total — hausses d'équilibre | 78,7 | 67,75 | **−10,95** |
| Total — somme niches | *vide* | 97 | **+97** |
| Droits de mutation — taxes à supprimer | −43,4 | −32,45 | **+10,95** |
| Taxe foncière — hausse | 41,96 | 42,06 | **+0,10** |

`CSG` → `CSG-CRDS` : le tableau des salaires est identique cellule à cellule.
Aucun montant ne bouge ; 13 valeurs disparaissent avec le bloc
« Effets généraux ».

**Périmètres qui changent** — `CI unique` devient « aide fondamentale
universelle » ; « Niches supprimées » devient « Niches restituées » ; « Solde
net post CSG » devient « Solde brut à restituer » ; « Niches à supprimer »
devient « Gisement à supprimer » ; « Gain direct restitué » devient « Gain
année 1 » ; « Gain indirect à allouer » devient « Gain supp. à terme » ;
« Gisement en sus » devient « Autre gisement ». Trois commentaires de `Flux`
changent de sens : « Affectés à l'aide unique » devient
« Fléché sur la capitalisation » sur les économies d'État et de collectivités,
et « Compense refonte fiscalité » sur les niches sociales.

Le bloc des ETP de `Détail Economies`, tenu en note de texte libre
(« ETP tt APU : 580 000 », « ETP hors FrTr : 90 % * 46440 = 41800 »), devient
six cases nommées et chiffrées : `Toutes APU` 580 000, `APUC` 151 000,
`France Travail` 47 880, `hors FrTravail` **41 799,6**, `Etat` 61 400,
`APUL` 428 500. Les colonnes d'incidence par population passent de `L:P` à
`S:W`.

### Graphiques

Traité au § 5.

---

## 3. Le rejeu des bouclages

**Passe 1 — l'appareil joué tel quel.** `socle_budgetaire.py` s'arrête à la
première lecture, sur `KeyError: 'Worksheet Opérateurs does not exist.'`. Il
échoue bruyamment et non en silence : c'est le seul point favorable de la
mesure. Aucun bouclage n'est joué.

**Passe 2 — après déplacement des seules adresses.** Un adaptateur
`appareil/socle_0910.py` déplace ce que la comparaison cellule à cellule a
prouvé identique : nom d'onglet, ligne de début, lettre de colonne. **Il ne
change aucun calcul.** Ce dont l'adresse n'a pas d'équivalent reste vide et se
déclare vide.

Le socle se régénère avec exactement les mêmes comptes qu'à l'état
antérieur — 278 taxes, 465 dépenses fiscales, 180 opérateurs, 749 ODAC-ODAL,
128 programmes, 2 351 lignes de PAP, 41 lignes d'économie — à une exception :
**`grande_synthese` passe de 18 à 0**, l'onglet `Gages` n'existant plus sous ce
nom.

### Verdict, bouclage par bouclage

| bouclage | état antérieur | pièces du 20260917 |
|---|---|---|
| S1 opérateurs, un régime chacun | OK | **OK** |
| S2 emplois par régime | OK | **OK** |
| S3 synthèse des agences | OK | **OK** |
| S4 les quatre familles font 1 104 | OK | **OK** |
| S5 taxes affectées — 8 119,670 / 9 802,722 / 17 922,392 M€ | OK | **OK** |
| S6 bénéficiaires isolés en tête | OK (3/3) | **OK (3/3)** |
| S7 dépenses fiscales — 465, 89,406, 101,321, 43,126, 29,141 | OK | **OK** |
| S8 arbre des économies | **32/32** | **27/32 — 5 en échec** |
| S9 chaîne des emplois et des charges | 7 dérivations, 2 écarts de concept, 0 ouvert | **identique** |
| S10 grille, missions, programmes, traitements | OK | **OK** |
| S11 à S16 | — | **injouables** |

**Les cinq échecs de S8 sont les cinq mêmes bouclages, et ils ont une seule
cause.**

| bouclage | recomposé | affiché au classeur |
|---|---|---|
| dont France Compétences · taxes + crédits → ligne | 10,125 | 10,6 |
| dont France Travail · taxes + crédits → ligne | 0,0 | 5,254667 |
| dont CNC et subventions culturelles · taxes + crédits → ligne | 0,705 | 1,3 |
| dont Ademe · taxes + crédits → ligne | 0,0 | 0,9 |
| dont MaPrimeRénov' · taxes + crédits → ligne | 0,0 | 1,3 |

Ce sont exactement les cinq lignes dont la **part budgétaire était écrite** au
bloc des postes nommés de l'onglet `Synthèse` des dépenses — le bloc que le
§ 2 déclare disparu. Sans lui, la part budgétaire redevient un résidu, et
`tracer_economies` la rend introuvable. **Ces bouclages s'arrêtent et se
rapportent ; rien n'est corrigé.**

Les 27 autres bouclages de S8 passent : l'arbre continue de se sommer de bas en
haut malgré les sept lignes dont le montant bouge.

**S11 à S16 ne se jouent pas, et pour deux raisons indépendantes.** Le module
qui les porte — la version de `controle_socle.py` écrite au second cercle du
socle — **n'est pas au dépôt** : il est en dette, au paquet
`methode/paquet_depot_socle_20260917.md`, et le clone rend la version à dix
bouclages. Et leurs onglets sources ont disparu : `Gages` pour S11,
`Fusion taxes` pour S12, `CI unique` pour S13, `CSG` pour S14, `Perdants` pour
S15. S16 porte sur le classeur de l'éducation, qui n'a pas de successeur.

### Une observation d'appareil, sur les cellules en erreur

`methode/grille_lecture_budgetaire.md` écrit que « la catégorie 62 est un
`#VALUE!` au classeur ». **Ce n'est pas une propriété du classeur.** Les deux
états portent, dans le `.xls` d'origine, la valeur en cache : 15 282,129296
pour la catégorie 62, 13 543,417778 pour la 64. Le `#VALUE!` est produit par le
recalcul de la conversion `soffice`. Sur l'état antérieur il frappait une
cellule, sur les pièces du 20260917 il en frappe **deux** — la 62 et la 64.
C'est ce qui explique la seule autre ligne de différence entre les deux sorties
de contrôle.

---

## 4. La reprise du référentiel des chiffres

`REF_chiffres` se régénère : **257 entrées** — 59 de note, 109 de proto,
89 de `REF_doctrine`.

| confiance | compte |
|---|---|
| 3 · strate 1 | 59 |
| 2 · source déclarée | 105 |
| 1 · ancrage ou opération | 0 |
| **0 · sans source** | **93** |

**Quatre-vingt-treize entrées restent sans source**, 65 sans unité. Les 57
calculs déclarés se rejouent justes. `controle_chiffres` sort **0 échec** et
22 signalements — 1 discordance arbitrée, 7 têtes décalées, 14 unités
divergentes.

**Aucune source n'a été inventée et aucun trou comblé.**

Le référentiel ne lit pas les classeurs : il ne bouge donc pas d'une valeur.
Le lien aux classeurs passe par les **45 sources écrites à la main** dans
`appareil/sources_chiffres.py`, et c'est là que le dépôt du 20260917 mord.
Dix-huit entrées nomment le classeur ou un de ses onglets. **Neuf citent une
adresse qui n'existe plus** :

| entrée | valeur | onglet cité | état |
|---|---|---|---|
| `R-D2-1-1-e1` | 236 Md€/an | `Manifeste`, L3 et L24 | **onglet disparu** |
| `R-D8-3-1-e2` | 30 Md€/an | `Manifeste` L20 ; `Capitalisation` | **deux onglets disparus** |
| `R-D3-2-1-p4` | 114 | `Gages` | **renommé `Flux`** |
| `R-D3-2-1-p5` | 9,7 | `CSG` H3 et I3 | **renommé `CSG-CRDS`, bloc retiré** |
| `R-D3-2-1-p6` | 98,25 | `CSG` | **renommé** |
| `R-D3-2-1-p7` | +12 | `CSG` G8 | **renommé** |
| `R-D3-2-1-e3` | −15,18 Md€/an | `CSG`, bloc Effets généraux | **bloc disparu** |
| `R-D3-2-1-e4` | −21 Md€/an | `CSG`, ligne Effet inflation | **bloc disparu** |
| `R-D7-2-2-e2` | 18 Md€/an | `Capitalisation` L2:L7 | **renommé `Input Capitalisation`** |

Cinq autres citent une adresse qui tient : `Détail Economies` L18 (APL, 16,1) et
L19 (AME, 1,1) sont inchangées, `Synthèse agences` est renommé mais identique.
Quatre citent une source hors classeur ou déclarent explicitement n'en avoir
aucune.

**Toutes ces sources nomment par ailleurs le millésime `0819` ou `0804`.** Elles
restent vraies de l'état qu'elles citent ; elles ne décrivent plus l'état déposé
le 20260917. Aucune n'a été réécrite : réécrire une source sur une pièce qu'on
vient de recevoir serait produire une valeur neuve.

---

## 5. Le classeur des graphiques

**Ce qu'il contient.** Douze onglets : `GraphGov`, `GraphRDB`, `GraphVA`,
`GraphCodes`, `Graph51pc`, `Graph1672Md`, `GraphETP`, `Graph236`,
`GraphAgences`, `GraphPatrimoine`, `GraphIR`, `GraphAFU`.

**Ce qui y est repris de l'ancienne synthèse.** Les douze portent le nom des
douze onglets `Graph…` du classeur `Synthèse Calculs 0819`, et leur matière en
vient. Chaque onglet est décalé vers le bas — de 20 à 39 lignes selon les
cas — pour loger le graphique au-dessus des données. La confrontation des
valeurs, onglet par onglet :

| onglet | valeurs anciennes | valeurs neuves | reprises | inédites | absentes du neuf |
|---|---|---|---|---|---|
| GraphGov | 224 | 226 | 224 | 2 | 0 |
| GraphRDB | 157 | 159 | 157 | 2 | 0 |
| GraphVA | 11 | 11 | 11 | 0 | 0 |
| GraphCodes | 257 | 258 | 256 | 2 | 1 |
| Graph51pc | 12 | 12 | 12 | 0 | 0 |
| Graph1672Md | 200 | 202 | 200 | 2 | 0 |
| GraphETP | 112 | 113 | 112 | 1 | 0 |
| Graph236 | 38 | 25 | 25 | 0 | **13** |
| GraphAgences | 112 | 112 | 112 | 0 | 0 |
| GraphPatrimoine | 148 | 150 | 148 | 2 | 0 |
| GraphIR | 479 | 479 | 479 | 0 | 0 |
| GraphAFU | 415 | 415 | 415 | 0 | 0 |
| **total** | **2 165** | **2 162** | **2 151** | **11** | **14** |

**Ce qui y est inédit** — onze valeurs, et pas une de plus :

- **sept adresses de source**, ajoutées en tête d'onglet : Eurostat pour
  `GraphGov` (deux) et `GraphRDB`, Légifrance pour `GraphCodes`, Insee pour
  `Graph1672Md` et `GraphPatrimoine`, le rapport annuel de la fonction publique
  pour `GraphETP` ;
- **un libellé corrigé** : « Nombre mots » devient « Nombre de mots »
  (`GraphCodes`) ;
- **deux nombres** : `3,301` à `Graph1672Md` et `8,204` à `GraphPatrimoine`,
  tous deux dans un bloc voisin de la source ajoutée ;
- **un libellé de série** : « Rendement des actifs publics » à `Graph236`.

**Ce qui y manque** — `Graph236` perd treize valeurs : les trois totaux de
regroupement en colonne A (67,006667 · 68,948 · 52,1) et le bloc entier
« Économies sur les aides aux ménages et aux associations » (27,5 · 17,7 · 3,6 ·
3,2 · 3, avec leurs cinq libellés).

**Le classeur des graphiques est donc une extraction, non une production.** Il
ne porte aucune valeur nouvelle hors sept sources et deux nombres de contexte.
`methode/grille_lecture_budgetaire.md` déclare déjà les douze feuilles de
graphiques « des vues et non des sources » : le dépôt du 20260917 confirme ce
statut et le rend matériel.

---

## Ce que ce fil n'a pas fait

Il n'a produit aucune valeur, corrigé aucun classeur, comblé aucun trou, touché
aucun texte de fond. Il n'a pas réécrit les sources de `sources_chiffres.py` sur
les nouveaux onglets. Il n'a pas remis les cinq bouclages de S8 en accord. Il
n'a pas déclaré lequel des deux états des pièces jointes fait foi.
