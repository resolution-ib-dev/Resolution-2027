# Suivi des dépenses — crédits et vecteurs juridiques, 20261007

**Porteur** : fil Cowork d'audit d'architecture sur les dépenses, 20261007.
**Mandat** : l'auteure — « audite ton architecture de bout en bout sur les dépenses pour la
doctrine et la production d'amendements », puis « fais tout », puis « prépare tout pour un fil
de réconciliation et de reprise des travaux ».
**Domicile** : `methode/suivi_depenses_20261007.md`.
**Appui** : `methode/appui_des_passes.md` · `methode/passation_20261007.md` § 3 et § 4.1 ·
`reference/regles_credits.md` (LOLF art. 5, 7, 8, 43, 47 ; Guide du budgétaire 2023).
**Mesure** : 2 blocages levés, 2 erreurs de formule localisées, 2 tables construites,
3 règles nouvelles, 2 fautes propres corrigées.
**Livrable** : `Suivi dépenses — crédits et vecteurs_20261007.xlsx`, 8 feuilles, 4 422 formules,
recalcul sans erreur.

---

## 1. Deux blocages levés

**1.1 — `SynthèseR` est trouvée.** Feuille du classeur
`PLF26 - Depenses 2026 du BG et des BA selon nomenclatures destination et nature_0910.xls`.
Le blocage § 4.1 de `methode/passation_20261007.md` est levé. Les quatre cellules du mandat
d'origine résolvent toutes.

**1.2 — Les `#VALUE!` n'existent pas.** `'Economies R'!U4` = 15 282,1 et `Y4` = 13 543,4, lus
en cache dans le `.xls`. Les dix cellules de `SynthèseR` signalées mortes portent toutes une
valeur. L'artefact venait d'une conversion LibreOffice (`SUMIFS` sur plages entières,
`_xlfn.XLOOKUP` non résolu). **Aucun bloc du chiffrage n'est sans source.**

---

## 2. Les deux erreurs de formule, localisées et chiffrées

| cellule | formule en place | défaut | effet |
|---|---|---|---|
| `SynthèseR!H8` | `=G21+D21+C20*7/3` | omet `E21` (Anah, 53,52) et `H21` (Autres, 1 317,61) | **+1 371,1 M€** sur la jambe au-delà d'1 an des subventions aux opérateurs |
| `SynthèseR!F32` | `=('Economies R'!S4−C31−D31−F20−E31−197,995)*0,9` | retranche `D31` (AME) et `E31` (emploi service), **déjà nets de leur 0,9**, d'une base brute, puis multiplie le tout par 0,9 | **−215,7 M€** sur le résidu « Autres » des chèques aux ménages |

Vérification du second : bruts sous-jacents `'Economies R'!R155` = 1 216,30 et `R177` = 1 180,12 ;
base amputée de 239,64 ; × 0,9 → −215,68.

**Ni l'une ni l'autre n'est corrigée.** Les deux sont à poser dans `SynthèseR`, pas ailleurs.

**Point de périmètre, non une erreur** : les 934,1 sont le résidu non nommé de la jambe taxes
affectées à 1 an — `Synthèse TA!F7` moins la somme des lignes nommées `F8:F15`. Ils se rangent du
côté taxes affectées, où `Flux` ligne 15 les porte déjà sous « Dont taxes affectées ».

---

## 3. La règle de classement, restituée

Le classement des dépenses n'est pas un drapeau binaire. Il obéit à **deux régimes distincts**,
lus dans `'Economies R'` :

| périmètre | règle d'arrêt | où elle se lit |
|---|---|---|
| **titres 2, 3 et 5** (cat. 21, 23, 31, titre 5) | arrêté si le **programme** est non essentiel | `'Economies R'` colonne E vide |
| **cat. 32 et titre 6** (32, 61, 62, 63, 64) | **drapeau propre par programme × catégorie** | `'Economies R'` colonnes Q, S, U, W, Y |
| **cat. 22** | aucune colonne d'arrêt — suit le sort de la cat. 21 | — |

**Les six valeurs du drapeau**, et leur portée :

| valeur | portée | porteur |
|---|---|---|
| `Oui` | arrêt immédiat | amendement d'état B, sur la mission |
| `En 3 ans` | extinction échelonnée | état B échelonné |
| `Fusion CI` | fondu dans l'aide fondamentale | première partie |
| `Bourse` | bascule vers les bourses | première partie |
| `Flux OM` | outre-mer — hors champ | — |
| `Sécu` | bascule sociale | PLFSS |
| *(vide)* | maintenu | — |

**Seul `Oui` vaut arrêt immédiat.** Le reste du classement était jusqu'ici invisible dans les
pièces du corpus.

**Contrôle de restitution** : CP arrêtés recalculés depuis `Données PAP 2026` sur cette règle =
**73 160,9 M€**, écart nul avec la somme des neuf colonnes « arrêter » d'`Economies R`,
catégorie par catégorie (21 : 3 206,9 · 23 : 80,6 · 31 : 3 414,3 · titre 5 : 1 316,2 ·
32 : 6 728,4 · 61 : 21 827,4 · 62 : 15 282,1 · 63 : 7 761,5 · 64 : 13 543,4).

---

## 4. Les deux tables construites

### Table A — crédits, grain amendable

718 lignes **mission × programme × titre × catégorie**, 45 missions, 162 programmes.

| | AE | CP |
|---|---:|---:|
| PLF 2026 | 842 785,5 | 818 506,8 |
| **arrêté** | **67 494,2** | **73 160,9** |

Répartition des CP par statut : essentiel 149 932,6 · **arrêté 73 160,9** · suit le titre 2
67 453,9 · maintenu 49 465,5 · fondu aide fondamentale 31 335,1 · sortie en 3 ans 12 454,4 ·
bourses 2 548,7 · outre-mer 2 544,8 · bascule sociale 449,0 · hors périmètre 428 520,2.

**Feuille `A — Contrôle mission`** : AE et CP séparés par mission, part arrêtée, verdict art. 47.
**Cinq missions sont arrêtées à 100 % des CP** — Cohésion des territoires (22 221), Relations
avec les collectivités territoriales (3 932), Avances à l'audiovisuel public (3 878), Santé
(1 672), et Investir pour la France de 2030 à 99,8 % (5 484). Ce sont des **suppressions de
mission** : elles relèvent du vote (« les parlementaires peuvent décider de ne voter aucun crédit
sur une mission donnée », Guide du budgétaire 2023, p. 74), non de l'amendement.

### Table B — vecteurs juridiques

**B1 — taxes affectées** : 278 lignes, **référence juridique sur 278/278**, plafond et
reversement 2026, début du plafonnement, geste qualifié. 76 suppressions d'affectation,
8 119,7 M€ à 1 an et 9 802,7 M€ au-delà.

**B2 — dépenses fiscales** : 465 lignes, **référence juridique sur 465/465, programme de
rattachement sur 465/465**. Dépense fiscale 2024 : 89 406,0 ; économie an 1 (gage CSG) :
43 126,4 ; supplémentaire (solde PO) : 29 140,8. Création, fin du fait générateur et fin
d'incidence budgétaire par ligne.

Les totaux fiscaux recoupent `Flux!C8` (43,1 Md€), `Flux!E8` (29,1) et `Détail Niches!D4`
(89,406) : la jambe fiscale est désormais traçable à la ligne.

### Jointure — porteur par programme

162 programmes, trois jambes face à face. **12 programmes portent les trois jambes**, 49 n'ont
que des crédits arrêtés, 71 n'ont aucune jambe.

Cinq premiers par effort total (M€) : **103** Accompagnement des mutations économiques 21 058 ·
**109** Aide à l'accès au logement 16 186 · **135** Urbanisme et habitat 11 395 · **134**
Développement des entreprises 6 490 · **157** Handicap et dépendance 5 704.

**Trois programmes lourds n'ont aucun vecteur juridique** et reposent entièrement sur l'état B :
109 (16 126), 424 Financement des investissements stratégiques (3 754), 177 Hébergement (3 071).

---

## 5. Trois règles nouvelles, à tenir

### 5.1 — Règle de proxy AE/CP

**Un amendement d'état B lit AE et CP sur la ligne de la table A.** Le proxy ne sert que si la
coupe est définie par un montant cible et non par une ligne. Ratios mesurés sur le PLF 2026 :

| niveau | AE/CP | régime |
|---|---:|---|
| **titre 2** | 1,0000 | **identité par construction** — LOLF art. 8, dernier alinéa. Aucune vérification due. |
| titres 1 et 4 | 1,0000 | identité |
| cat. 21, 22, 23, 32 | 1,0000 | identité |
| cat. 61, 64 | 1,0003 / 1,0006 | identité à l'arrondi |
| titre 6 global | 0,9952 | proxy acceptable |
| cat. 62 | 0,9947 | proxy acceptable |
| titre 7 | 0,9962 | proxy acceptable |
| **cat. 31** | 1,1133 | **écart structurel — lire la ligne** |
| **cat. 63** | 0,9580 | **écart structurel — lire la ligne** |
| **cat. 52** | 1,1924 | **écart structurel — lire la ligne** |
| **cat. 51 / titre 5** | 1,7722 / 1,7287 | **engagement pluriannuel — proxy interdit** |

Seuils retenus : écart < 0,2 % → identité ; < 2 % → proxy acceptable ; ≥ 2 % → lire la ligne.

### 5.2 — Les 34 programmes non classés sont un périmètre, non un oubli

`Economies R` couvre 128 programmes sur 162. Les **34 absents** portent 428 520,2 M€ de CP et
relèvent tous de natures non discrétionnaires :

remboursements et dégrèvements (200 : 140 845,4 ; 201 : 4 618,0) · avances aux collectivités
(833 : 135 395,4 ; 832 : 206,0) · pensions (741 : 66 073,0 ; 742 : 2 083,7 ; 743 : 1 170,4) ·
dette et engagements financiers (117 : 58 615,0 ; 114 : 790,4 ; 355 : 661,0 ; 344 : 178,7 ;
145 : 96,2 ; 336 : 37,5) · prêts et avances (821 : 9 000,0 ; 851 : 828,6 ; 852 : 211,8 ;
823 : 210,0 ; 869 : 150,0 ; 853 : 100,0 ; 862 : 75,0 ; 830 : 40,0 ; 824 : 30,0 ; 825 : 15,0 ;
861 : 0,1) · participations financières (731 : 5 421,2) · pouvoirs publics (511 : 607,6 ;
521 : 353,5 ; 501 : 122,6 ; 541 : 35,6 ; 531 : 20,0 ; 533 : 0,9) · crédits non répartis
(551 : 350,0 ; 552 : 125,0) · transformation publique (368 : 52,9).

**Aucun ne reste à instruire.** Le classement est complet ; c'est le classeur qui ne le disait pas.

### 5.3 — Soupçonner l'instrument avant le texte

Rappel de `appui_des_passes.md`, reprise 1 du 20261007, et faute commise ici : dix `#VALUE!` et
deux totaux morts auraient dû déclencher un contrôle de la conversion avant toute conclusion.
**Un classeur `.xls` se lit en valeurs de cache, jamais après recalcul par un moteur tiers**,
quand la question porte sur l'existence d'une valeur.

---

## 6. Deux fautes propres, inscrites

**6.1 — Le −215,7 a été posé au mauvais endroit.** Réparti au prorata sur `Détail Economies!D19`
(AME) et `D21` (emploi à domicile), alors que `SynthèseR!F32` est le **résidu « Autres »** du bloc
ménages. Le classeur `Synthèse Calculs Résolution_corrige_20261007.xlsx` produit ce jour porte
cette erreur : **ne pas le verser en l'état.**

**6.2 — Un recouvrement inexistant a été signalé.** Taxes affectées et crédits budgétaires se
somment par nomenclature : la subvention pour charges de service public est une catégorie du
titre 3 (LOLF art. 5, II), la taxe affectée est une ressource propre hors budget général, seule
sa fraction reversée revenant au budget. **Il n'y a pas de double compte entre les deux jambes.**
La colonne « exposition au double compte » du classeur
`Réconciliation budgétaire-taxes affectées_20261007.xlsx` est fausse d'intitulé : elle mesure
l'**effort joint par programme**. Ce classeur est remplacé par le présent livrable.

---

## 7. Reste dû au fil suivant

1. **Poser `H8` et `F32` dans `SynthèseR`** — les deux formules sont rendues au § 2.
2. **Relier `Détail Economies` et `Flux` à `SynthèseR`** et passer `Flux!C15`, `E15` et les
   totaux de bloc en sommes. Aujourd'hui `C15` est en dur à 44 000 et ne bouge pas quand ses
   composantes bougent.
3. **Mesurer les résidus au lieu de les caler.** Quatre lignes « autres » de `Détail Economies`
   (`D16`, `D22`, `D27`, `D36`) sont des soldes : le total y est une entrée, pas une sortie.
   C'est ce qui a laissé 14 500 survivre.
4. **`Détail Economies!A16` n'a pas de code** : le résidu « autres » du bloc opérateurs n'entre
   dans aucun `SUMIFS` d'`Annexe Manuscrit`. Antérieur à cette passe.
5. **Descendre la jointure au bénéficiaire** via `Opérateurs R` (184 lignes, couple opérateur ×
   programme) — le grain programme ne suffit pas pour nommer un opérateur dans un exposé.
6. **Qualifier les 12 programmes à trois jambes** : un même programme coupé en crédits, en taxe
   affectée et en dépense fiscale demande trois pièces et un ordre entre elles.

---

## 8. Ligne de lancement du fil suivant

Fil **Cowork** — il lui faut le coffre, le droit et le classeur.

> Réconciliation et reprise des travaux sur les dépenses — ouvrir `methode/appui_des_passes.md`
> et `methode/suivi_depenses_20261007.md` ; appui `reference/regles_credits.md` ;
> skills `confrontation`, `vecteur-mesure`, `disposition-cible`, `resolution-chantier` ;
> pièce de travail `Suivi dépenses — crédits et vecteurs_20261007.xlsx` (tables A et B, jointure,
> règle de proxy AE/CP, programmes non classés) ; mesurer d'abord les deux formules `SynthèseR!H8`
> et `SynthèseR!F32` et rendre le compte avant toute écriture ; puis traiter le reste dû § 7 dans
> l'ordre ; ne rédiger aucun amendement ; la mesure de sortie reprend ce mandat point par point
> avec un verdict par point, « non joué » compris.
