# Restes à payer — la coupe en dépense finale, 2027-2030 — état du 20261118

**Porteur** : fil d'exécution du 20261118, sur mandat du pilotage. **Objet** : passer de la coupe
« en mesure » (le croisé `referentiels/calendrier_mesures_mois_20261116.tsv`, hors règle de CP
résiduel) à la coupe **en dépense finale** — l'argent que les agents privés cessent effectivement
de recevoir —, mois par mois, et en tirer l'effet sur le solde du circuit de restitution.
**Calcul** : `appareil/restes_a_payer.py` (`construire`, `controler`). **Table** :
`referentiels/restes_a_payer_20261118.tsv` (27 lignes × trois séries, plus 20 agrégats, 48 mois).
**Rien n'est modifié** au registre, au croisé ni au compte complet. Proposition, non validée.

Md€, signe positif = économie. Chaque chiffre porte son statut : **relevé** (lu à la pièce),
**déduit** (calculé sur des relevés), **posé** (hypothèse du fil, avec ses bornes), **hérité**
(lu dans une pièce de méthode, non rejoué).

---

## 1. L'existant, sur pièce

**Les pièces.**

| pièce | contenu | statut |
|---|---|---|
| registre § 1, R-R | « Les engagements en cours se règlent par le CP résiduel, jamais par la date » ; CP minorés = min (CP ; AE) × (1 − résiduel) | relevé |
| registre § 3 | huit régimes : titre 2, titres 1 et 4, cat. 21-23, 32, 61, 64 à 0 % ; plancher 15 % ; cat. 62 20 % ; cat. 63 25 % ; titre 5 80 % ; France Travail un sixième conservé | relevé, et relu par le script |
| registre § 3 bis | l'égalité AE = CP se relève par catégorie (ratio ≥ 1,000 à 0,005 près) ; recalage 1,01288 | relevé |
| registre § 15 | mesure contre caisse, **part État, 2027 seulement** : écart 11,11 Md€, dont 2,49 de résiduel et CP ≤ AE, 1,33 de France 2030 (AE 2027 nulles), 0,86 sans véhicule ; marge de prudence 4,7 | relevé ; **antérieur à la mise à niveau du 20261116, non rejoué** (le § 5 le dit) |
| `referentiels/parametres_credits_20261116.tsv` | 296 lignes programme × catégorie : brut AE/CP, règle de résiduel (0, 0,15, 0,20, 0,25, 0,80), cibles AE et CP du projet. Lignes retenues : AE 24,50, CP 21,04, **écart AE − CP 3,46 Md€** | relevé (somme calculée) |
| `sources/projet_20261116/10_Suivi_depenses…xlsx`, onglet `Règle proxy AE-CP` | rapports AE/CP du PLF 2026 par titre et catégorie : titre 5 AE = 1,729 × CP, cat. 51 1,772, cat. 31 1,113, cat. 63 0,958 ; « Titre 5 et catégorie 51 : l'écart est un engagement pluriannuel » | relevé |
| `referentiels/ratios_cp_ae_pap2026.tsv` | 643 ratios CP/AE programme × titre × catégorie | relevé (non relu ici) |
| liasse P2, amendements n° 1 à 22 | « L'écart entre les deux règle les engagements déjà contractés, que la mesure ne remet pas en cause » | relevé |
| `P2/etatB_02` | associations : AE éteintes dès le premier jour ; restes à payer en CP **sur 2027 et 2028**, terme au 1er janvier 2029 ; « ventilation entre 2027 et 2028 non portée par une cellule : à chiffrer » | relevé |
| `P2/etatB_01` | MaPrimeRénov' : « Les dossiers déjà engagés sont payés » ; Ademe minorée de 300 M€, AE = CP (cat. 32) | relevé |
| `P2/2_6_*` | aide au logement et chèque énergie : « aucune marge de reste à payer » ; hébergement d'urgence : « marge de reste à payer de dix pour cent », **non reprise** par `etatB_03` | relevé |
| `P2/coll_P2_04` | IV : « Les engagements juridiques souscrits avant cette date sont exécutés jusqu'à leur terme » ; III D : baisse des concours de l'État dès 2027, par douzièmes | relevé |
| `methode/arbitrages.md`, 20261118 | « En trois ans » mêlait **clé de décaissement (CP)** et **clause du grand-père (AE)** ; distinguer droits en cours et engagements déjà pris honorés | relevé |
| `methode/etats/SUIVI_chantier_20261009.md` § 4 | « le pilotage du calendrier se fait sur les rythmes de CP, les pentes de montée en charge » ; la restitution principale ne s'étale pas | relevé |
| guide du budgétaire 2023 (`sources/`) | AE = engagement juridique, CP = paiement (p. 115 du PDF) ; CP « consommés au moment du décaissement » (p. 146) ; boîte à outils « restes à payer sur 4 ans, échéancier de CP sur 5 ans » (p. 91) ; ODAC et APUL sont des sous-secteurs distincts de l'État (p. 31) ; ODAC financés pour moitié par des transferts publics et interdits d'emprunter auprès d'un établissement de crédit au-delà de douze mois (p. 32) ; transferts de l'État ≈ moitié des recettes locales (p. 34) | relevé ; **aucune clé de décaissement chiffrée** |

**Les manques.** Aucune pièce du dépôt ne porte : une clé de décaissement **pluriannuelle** (le
§ 3 ne donne que la première année) ; un résiduel au-delà de 2027 ; une couche « agence » ou
« collectivité » entre le crédit coupé et la dépense finale ; la trésorerie des collectivités ; la
ventilation 2027/2028 des restes à payer associatifs ; un profil mensuel en dépense finale. La
recherche a porté sur `methode/`, `livrables/`, `sources/projet_20261116/` et le registre
(clé de CP, clé de décaissement, restes à payer, profil de montée en charge, trésorerie) ; aucun
fichier de méthode dédié aux clés de CP n'a été trouvé hors de ceux listés ci-dessus.

---

## 2. Méthode

**Une ligne, une couche.** Le solde public est l'opposé de la somme des privés (règle de
l'auteur, 20261116) : un transfert entre l'État et une agence ou une collectivité ne compte pas ;
seule compte la dépense versée à un privé.

| couche | lignes | mécanisme |
|---|---|---|
| **État** | D18-D38 sauf opérateurs | l'État paie le privé ; le CP résiduel du § 3 règle les engagements en cours |
| **Agence** | D5, D6, D12, D15 (Anah), D16, D24 | l'État coupe la subvention à la date ; l'agence baisse sa propre dépense plus lentement et puise dans sa trésorerie |
| **Collectivité** | D40, D41, D42 | la collectivité baisse sa dépense ; ses contrats, conventions et marchés en cours courent |
| **sans reste à payer** | D18, D19, D20, D22 (cat. 61, guichet ou chèque), D38, D43 (titre 2) | effet immédiat |

**La clé de décaissement.** Chaque marche de la mesure ouvre une tranche. Pendant sa k-ième année,
la tranche garde une part **r^k** de la dépense antérieure (restes à payer) ; la dépense finale vaut
mesure × (1 − r^k). *Forme posée* : profil géométrique stationnaire — chaque génération d'AE se
paie pour (1 − r) l'année de l'engagement, puis r^j (1 − r) la j-ième année. *Déduit* de cette
forme : la première année redonne exactement la chaîne du § 1 (contrôle tenu sur D27 : 1,30 ×
0,80 = 1,04), et le stock de restes à payer vaut r / (1 − r) années de paiement. Pour un taux de
80 % (titre 5), la clé laisse 80 %, 64 %, 51 %, 41 % — horizon cohérent avec les « restes à payer
sur 4 ans » du guide (relevé, p. 91), sans que le guide donne de profil.

**Restitution** : § 2 du registre, relu (33,39 en 2027, 114,46 par an ensuite). **Surplus du
circuit de restitution** : compte complet, circuit A, hors épargne, chômage et patrimoine
(57,23 · 30,84 · 55,05 · 58,66 en mesure, relevé au registre § 5) ; en dépense finale, on en
retranche l'écart calculé ici.

---

## 3. Hypothèses, ligne par ligne

r = part gardée la première année. Bornes [bas ; haut] : bas = moins de restes à payer.

| ligne | couche | r central | bornes | statut | appui |
|---|---|---:|---|---|---|
| D18, D19, D20, D22 | État | 0 | — | relevé | § 3, cat. 61 ; pièces 2.6 « aucune marge » ; D20 : restes de la campagne 2026 déjà dans la mesure |
| D38, D43 | État | 0 | — | relevé | § 3, titre 2 ; indemnité déjà à 30 % dans la mesure |
| D25, D27 | État | 0,20 | [0 ; 0,20] | relevé | § 3, cat. 62. Borne basse : rythme déjà net du stock (D25 : contrats en cours maintenus, § 9) |
| D32 | État | 0,20 sur 43 %, 0 sur 57 % | — | relevé (taux), déduit (poids des AE cibles) | § 3, cat. 62 et 64 |
| D37 | État | 0,15 sur 65 %, 0,80 sur 35 % | titre 5 [0,60 ; 0,80] | relevé (taux), déduit (poids) ; borne basse posée | § 3, plancher et titre 5 |
| D26, D33 | État | **rien en 2027**, puis 0,20 | [0 ; 0,20] après 2027 | relevé | § 15 : AE 2027 nulles aux programmes 421 à 425, un amendement de crédits n'y retire rien |
| D29 | État | 0,10 | [0 ; 0,10] | relevé à la pièce, non repris par la liasse | `P2/2_6_socle_hebergement_urgence` |
| D30 | État | 0,335 | [0 ; 0,335] | déduit | 1 − CP/AE des cibles, `parametres_credits` ; terme au 1er janvier 2029 |
| D31, D34, D35, D36 | État | 0,25 | [0 ; 0,50] | **posé** (taux transposé du § 3, cat. 63) ; relevé (terme 1er janvier 2029) | `P2/etatB_02` |
| D12 Ademe | Agence | 0,695 | [0,45 ; 0,695] | **déduit** | Jaune « Opérateurs » PLF 2026, p. 74 du PDF : restes à payer 3,22 Md€ au 31/12/2024 ; financement de l'État 2026 1,42 Md€ (`operateurs_jaune2026`) ; r = 3,22 / (3,22 + 1,42). Borne basse posée : l'Ademe paie aussi sur d'autres ressources |
| D5, D6, D16 | Agence | 0,15 | [0,05 ; 0,30] | **posé** | personnel, marchés, financements au service fait |
| D24 audiovisuel | Agence | 0,30 | [0,15 ; 0,50] | **posé** | contrats de production pluriannuels ; classement des sociétés en entité publique posé |
| D15 MaPrimeRénov' | Agence (Anah) | 0,50 | [0,25 ; 0,75] | **posé** | « les dossiers déjà engagés sont payés » (relevé), prime versée à la fin des travaux |
| D40 culture locale | Collectivité | 0,15 | [0,05 ; 0,30] | **posé** | transposé du plancher § 3 |
| D41 aides aux entreprises | Collectivité | 0,25 | [0,15 ; 0,50] | **posé** (taux transposé, cat. 63) | `coll_P2_04`, IV, relevé : engagements exécutés jusqu'à leur terme |
| D42 charges courantes | Collectivité | 0,15 | [0,10 ; 0,30] | **posé** (taux transposé, cat. 31) | marchés en cours |

Une transposition d'un taux de l'État à une agence ou une collectivité est une **hypothèse**, non un
constat : aucune pièce ne mesure la durée des engagements des agences (hors l'Ademe) ni des
collectivités.

---

## 4. Résultats

### Par exercice

| | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|
| coupes en mesure (croisé, relevé) | 57,47 | 89,49 | 109,11 | 112,71 |
| restes à payer — État | 4,08 | 3,11 | 1,78 | 0,81 |
| restes à payer — agences | 2,32 | 2,62 | 1,76 | 0,67 |
| restes à payer — collectivités | 5,08 | 1,58 | 0,90 | 0,19 |
| **coupes en dépense finale, central** | **46,00** | **82,18** | **104,66** | **111,04** |
| fourchette (bas ; haut) | 51,33 ; 38,79 | 87,32 ; 75,22 | 107,81 ; 99,94 | 112,29 ; 108,62 |
| restitution (§ 2) | 33,39 | 114,46 | 114,46 | 114,46 |
| solde en mesure (§ 5) | +24,08 | −24,97 | −5,35 | −1,75 |
| **solde en dépense finale, central** | **+12,61** | **−32,28** | **−9,80** | **−3,42** |
| fourchette (bas ; haut) | +17,94 ; +5,40 | −27,14 ; −39,24 | −6,65 ; −14,52 | −2,17 ; −5,84 |
| surplus du circuit, compte complet, en mesure | +57,23 | +30,84 | +55,05 | +58,66 |
| surplus du circuit, en dépense finale | +45,76 | +23,53 | +50,60 | +56,98 |

Le croisé donne 57,47 en 2027 contre 57,46 au § 5 : arrondi des lignes, relevé.

**Lecture.** Les restes à payer ne font rien perdre : ils décalent. 24,90 Md€ glissent de 2027-2030
vers les exercices suivants de la fenêtre, et 3,02 Md€ sortent de la fenêtre (queue après 2030,
surtout D37 titre 5, D12 et D41). L'excédent de 2027 est divisé par deux (+24,08 → +12,61) ; le
déficit de 2028 se creuse de 7,31 (−24,97 → −32,28).

### Par mois, et la bascule

| mois | coupes, mesure | coupes, dépense finale | restitution | solde, mesure | solde, dépense finale |
|---|---:|---:|---:|---:|---:|
| juillet 2027 | 6,07 | 4,94 | 1,59 | +4,48 | +3,35 |
| septembre 2027 | 6,07 | 4,94 | 4,77 | +1,30 | +0,17 |
| octobre 2027 | 6,07 | 4,94 | 6,36 | **−0,29** | **−1,42** |
| décembre 2027 | 6,07 | 4,94 | 9,54 | −3,47 | −4,60 |
| janvier 2028 | 6,97 | 6,30 | 9,54 | −2,57 | −3,24 |
| juillet 2028 | 7,95 | 7,39 | 9,54 | −1,59 | −2,15 |
| janvier 2029 | 8,79 | 8,38 | 9,54 | −0,75 | −1,16 |

- **Le solde mensuel bascule en octobre 2027**, en mesure comme en dépense finale (septembre 2027
  en borne haute). Le creux est décembre 2027 : −3,47 en mesure, **−4,60** en dépense finale.
- **Le solde cumulé depuis janvier 2027 devient négatif en avril 2028** en dépense finale (février
  en borne haute, juillet en borne basse), contre **décembre 2028** en mesure. C'est la vraie
  bascule 2027 → 2028 : le coussin de 2027 tient trois mois de 2028 au lieu de douze.
- **Au compte complet**, le surplus du circuit de restitution reste positif chaque mois des 48 :
  au plus bas **+0,69** en décembre 2027 en dépense finale (+1,80 en janvier 2028 en mesure), et
  +1,13 à +1,15 par mois au premier semestre 2028 (+1,80 en mesure). La condition du compte complet
  reste celle qu'il pose : que les niches rapportent à leur date.

### Trésorerie des agences — contrôle de vraisemblance

Trésorerie au 31/12/2024, relevée au Jaune « Opérateurs » PLF 2026 (p. 160 du PDF ; somme
calculée de 175 lignes : 39,44 · 37,96 · **31,75** Md€ en 2022 · 2023 · 2024). Écart cumulé maximal
des agences, central : **7,37 Md€**, couvert en masse. Ligne à ligne, il ne l'est pas toujours :

| agence | trésorerie 2024 | écart cumulé max, central |
|---|---:|---:|
| Ademe (D12) | 2,82 | 1,17 |
| France Travail (D6) | 0,56 | 0,92 |
| Anah (D15) | 0,57 | 1,10 |
| France Compétences (D5) | 0,23 | 1,85 |

Pour France Compétences et l'Anah, l'écart dépasse la trésorerie, et un ODAC n'emprunte pas auprès
d'un établissement de crédit au-delà de douze mois (guide, p. 32, relevé). Deux issues : l'État dote l'agence (la coupe en
crédits n'est pas tenue), ou l'agence coupe ses engagements non juridiques plus vite (r baisse). Si
les engagements sont juridiques, la dépense finale ne change pas, seul le payeur change.

Collectivités : écart cumulé maximal 7,76 Md€, dont 5,08 en 2027. **Aucune pièce du dépôt ne
porte leur trésorerie** (les comptes Insee de `comptes_strates_locales` sont non financiers).

---

## 5. Les hypothèses qui pèsent le plus

Écart sur les coupes en dépense finale, une famille à la fois, borne basse puis haute (Md€) :

| famille | statut | 2027 | 2028 |
|---|---|---|---|
| **collectivités, D40-D42** | posé | +2,43 ; −5,08 | +0,91 ; −3,59 |
| **agences sous subvention, D5, D6, D16, D24** | posé | +0,99 ; −1,44 | +1,32 ; −2,31 |
| **associations, D29-D36** | posé (taux), relevé (terme) | +0,76 ; −0,40 | +0,97 ; −0,70 |
| État, cat. 62 et France 2030 après 2027 (bas = rythme déjà net du stock) | relevé ; borne posée | +0,56 ; 0 | +1,24 ; 0 |
| Anah, D15 | posé | +0,29 ; −0,29 | +0,22 ; −0,37 |
| D37, titre 5 | relevé ; borne posée | +0,26 ; 0 | +0,37 ; 0 |
| Ademe, D12 | déduit | +0,04 ; 0 | +0,12 ; 0 |

France 2030 ne figure pas comme hypothèse : rien en 2027 est un **relevé** (§ 15), qui pèse 1,34
Md€ sur 2027.

---

## 6. Pistes de modulation — à soumettre, non appliquées

**a) Caler la marche de restitution de 2028 sur la dépense finale.** Baisser la restitution de 2028
de l'écart de l'exercice, **7,31 Md€**, soit **0,62 point** sur les 9,70 de CSG et de CRDS (0,61 Md€
par mois), plein taux en janvier 2029. Solde : +12,61 · **−24,97** · −9,80 · −3,42 ; 2028 revient à
son niveau en mesure. **Contraire à l'arbitrage du 20261009** (« la restitution principale ne
s'étale pas ») : à trancher par l'auteure.

**b) Solder en 2027 les restes à payer de 2028 sur dossiers et conventions de l'État**
(D25, D27, D29 à D32, D34 à D36), dans l'excédent de 2027 : versement anticipé du solde des
conventions, *posé*. **1,84 Md€** passent de 2028 à 2027. Solde : **+10,77 · −30,44** · −9,80 ·
−3,42. Le cumul ne change pas ; le creux de 2028 se réduit d'autant.

**c) Éteindre les AE au 1er janvier 2027 sur les lignes datées du 1er juillet qui portent un reste à
payer** (D12, D16, D24, D25, D30, D31, D33, D34 à D36), la coupe en CP gardant sa date. La règle
existe déjà pour les associations (`etatB_02`, « AE éteintes dès le premier jour ») ; la piste
l'étend aux agences. L'horloge des restes à payer avance de six mois. Solde : +12,61 · **−30,95** ·
−9,13 · −3,18, soit **+1,33** en 2028 ; le cumul passe sous zéro en mai 2028 au lieu d'avril.

Les trois pistes ne se cumulent pas sans rejeu. Le levier du § 15, l'article qui éteint les
engagements de France 2030, rendrait 1,34 Md€ en 2027 en dépense finale ; il est déjà inscrit.

---

## 7. Limites

1. **La forme de la clé est posée** (géométrique, marches annuelles). Une clé linéaire à terme fixe
   viderait les restes à payer plus tôt ; aucune pièce ne permet de trancher.
2. **Double compte possible avec les rythmes en trois ans.** L'arbitrage du 20261118 dit que « En
   trois ans » mêlait clé de décaissement et grand-père. Le central suit R-R (résiduel en sus de la
   date) ; la borne basse retire le résiduel des lignes dont le rythme porte déjà le stock.
3. **Agences et collectivités : hypothèses grossières.** Une seule clé par famille, transposée de
   l'État, sauf l'Ademe (déduite). La trésorerie des collectivités n'est dans aucune pièce.
4. **D5 relève surtout de la première partie** (taxes affectées) ; la couche agence s'y applique de
   même, la dépense finale de France Compétences ne dépendant pas du véhicule.
5. **Le § 15 du registre n'est pas rejoué** ; le calcul part du croisé à jour, non de la caisse de
   2027. **L'épargne rendue du compte complet n'est pas rejouée** : seul le surplus du circuit est
   corrigé de l'écart.
6. **Associations et entreprises sont des privés** : le paiement de l'État est leur dépense finale ;
   aucune couche n'est ajoutée derrière elles.

---

## 8. Contrôles

`python3 appareil/restes_a_payer.py controler` : **0 échec** — croisé contre § 5 ; restitution
contre § 2 et § 5 ; résidus de `parametres_credits` contenus dans ceux du § 3 ; identité mesure =
dépense finale + reste à payer ; reste à payer ≥ 0 ; chaîne du § 1 sur D27 ; lignes D du compte
complet égales au croisé ; TSV égal au calcul ; aucun reste à payer en titre 2 et cat. 61 ; rien
après le 1er janvier 2029 sur les associations. `calendrier_mesures_mois.py controler` et
`calendrier_compte_complet.py controler` : **0 échec**, rejoués après écriture.

---

## 9. Entrées de registre — titrées, datées, sans numéro

### Restes à payer : la coupe en dépense finale, 2027-2030 — 20261118

*Calculé, proposé, non appliqué.* En dépense finale, les coupes valent 46,00 · 82,18 · 104,66 ·
111,04 Md€ contre 57,47 · 89,49 · 109,11 · 112,71 en mesure ; le solde du § 5 passe à +12,61 ·
−32,28 · −9,80 · −3,42. Le solde mensuel bascule toujours en octobre 2027 ; le cumul passe sous
zéro en avril 2028 au lieu de décembre 2028. Hypothèses : registre § 3 (relevé), Jaune
« Opérateurs » pour l'Ademe (déduit), agences et collectivités (posé, bornes au § 3 de la note).

### Pistes de lissage de 2028 — 20261118

*À soumettre.* a) restitution de 2028 réduite de 7,31 Md€ (0,62 point), contraire à l'arbitrage du
20261009 ; b) 1,84 Md€ de restes à payer de 2028 soldés en 2027 ; c) AE éteintes au 1er janvier
2027 sur les lignes de juillet à reste à payer, +1,33 en 2028.
