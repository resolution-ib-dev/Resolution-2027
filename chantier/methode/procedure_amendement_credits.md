# Procédure complète d'un amendement de crédits — 20261016

Elle consolide ce qui était épars : la chaîne du § 1 du registre, les huit règles
de lecture, les huit régimes de résiduel du § 3, la formule de titre 2 du § 10, et
les règles arrêtées entre le 15 et le 16 octobre — l'état B lu avant tout calcul,
AE ≥ CP avec égalité relevée, le resize, et la table A comme seule assiette d'un
amendement.

**Elle fait foi. Une pièce de crédits qui ne la suit pas ne se verse pas.**

L'appareil qui l'exécute est `appareil/chaine_credits.py`, et le contrôle qui la
vérifie `appareil/controle_credits_liasse.py`.

---

## 0. Ce qui fait foi, et dans quel ordre on l'ouvre

| rang | pièce | ce qu'on y lit |
|---|---|---|
| 1 | `Suivi dépenses — crédits et vecteurs_20261007.xlsx`, onglet **`A — Crédits`** | **l'assiette** — AE arrêtées et CP arrêtés, au grain mission × programme × titre × catégorie |
| 2 | même classeur, onglet **`Mesure`** | ce que la table A a déjà appliqué, et ses contrôles |
| 3 | `referentiels/etatB_2027_bg.tsv` | **les crédits ouverts de 2027**, par programme, et le titre 2 qui s'y rattache |
| 4 | `referentiels/ratios_cp_ae_pap2026.tsv` | les ratios CP/AE mesurés, par programme × titre × catégorie |
| 5 | `livrables/registre_calcul_etatB.md` | § 1 la chaîne · § 3 et § 3 bis le CP · § 4 les dates · § 10 le titre 2 |
| 6 | `reference/regles_credits.md` | la LOLF, les six invariants de forme, les quatre contrôles |

**On ouvre la division qui nomme la matière. On ne cherche pas le mot.**

---

## 1. L'assiette — table A, et rien d'autre

> **Pour un amendement, l'assiette est la table A.** La colonne F de
> `Détail Economies` sert à une **projection**, jamais à un amendement. Le § 1 du
> registre le dit depuis le début ; quatre pièces sur cinq l'avaient ignoré, et
> c'est la faute qui a tout fait reprendre le 16 octobre.

La table A porte **718 lignes**, dont **247 arrêtées**, sur **76 programmes** et
**28 missions** : **67 494,2 M€ d'AE** et **73 160,9 M€ de CP**.

**Le socle, le rythme et le drapeau d'arrêt y sont déjà appliqués.** L'onglet
`Mesure` l'écrit, et son contrôle le prouve : « CP arrêtés = Economies R, somme des
neuf colonnes *arrêter*, écart nul ». **Les réappliquer est la faute R-V à
l'envers** — le socle ne se retire pas deux fois, le rythme ne se proratise pas
deux fois.

Ce que la table A a déjà tranché, et qu'on ne rouvre pas :

- titres 2, 3 et 5 : arrêté si le programme n'est pas essentiel ;
- catégorie 32 et titre 6 : drapeau propre par programme × catégorie, et seul
  « Oui » vaut arrêt immédiat ;
- catégorie 22 : elle suit le sort de la catégorie 21, jamais arrêtée seule ;
- **34 programmes hors périmètre** — remboursements, avances, pensions, dette,
  prêts, pouvoirs publics — jamais arrêtés.

---

## 2. La date d'effet, donc la fraction d'exercice

La date se lit à la **catégorie**, qui porte l'acteur, par **R-P** et **R-S**.

| catégories | acteur | date | fraction |
|---|---|---|---:|
| 21, 22, 23 salaires et cotisations | agents publics, personnes physiques | 1er juillet | 6/12 |
| 31 fonctionnement | va avec les personnels, arbitrage du 20261016 | 1er juillet | 6/12 |
| 61 subvention aux ménages | personnes physiques | 1er juillet | 6/12 |
| 32 subvention aux opérateurs | personnes morales | 1er janvier | 12/12 |
| 62 subvention aux entreprises | personnes morales économiques | 1er janvier | 12/12 |
| 63 subvention aux collectivités | personnes morales | 1er janvier | 12/12 |
| 64 subvention aux autres | personnes morales | 1er janvier | 12/12 |
| 51, 52, 53 investissement | personnes morales économiques | 1er janvier | 12/12 |

**R-S prime R-P** : une aide captée par un intermédiaire se coupe immédiatement,
même si elle finit chez une personne physique. **R-Q** : un acteur ne subit qu'une
date dans l'exercice. **R-R** : les engagements en cours se règlent par le CP
résiduel, jamais par la date. **R-U** : un aménagement de transition ne repousse
jamais le terme.

---

## 3. Les autorisations d'engagement

> **AE minorées = AE arrêtées × fraction d'exercice.**

Rien d'autre. Pas de socle, pas de rythme : ils sont dans l'assiette.

**L'exposé sommaire porte l'AE.** C'est l'autorisation qui s'éteint, et c'est elle
que le vote retire. Le CP est une conclusion technique, qui se dit au tableau et
non au texte.

---

## 4. Les crédits de paiement

> **CP minorés = min (CP arrêtés ; AE arrêtées) × fraction × (1 − résiduel).**

Les huit régimes de résiduel, § 3 du registre :

| régime | périmètre | résiduel |
|---|---|---:|
| AE = CP par texte | titre 2, LOLF art. 8 | **0 %** |
| AE = CP mesuré | titres 1 et 4 · catégories 21, 22, 23, 32 | **0 %** |
| AE = CP à l'arrondi | catégories 61 et 64 | **0 %** |
| plancher commun | tout le reste | **15 %** |
| stock de dossiers | catégorie 62 | **20 %** |
| stock de conventions | catégorie 63 | **25 %** |
| opérations engagées | titre 5 | **80 %** |
| devis et prestations signés | France Travail, D6 | 1/6 conservé en 2027 |

**AE ≥ CP, toujours.** L'égalité est admise sur le titre 2, où l'article 8
l'impose, et **hors titre 2 lorsqu'elle est relevée** : le ratio CP/AE de la
catégorie visée vaut au moins 1,000 au PAP, à 0,005 près. Un ratio inférieur la
refuse, et le CP suit son régime.

**Le resize.** Quand l'estimation se construit sur la ventilation du PAP, millésime
2026, et que les crédits ouverts sont de 2027, le recalage se fait par le rapport
des agrégats du budget général : 0,97199 ÷ 0,95962 = **1,01288**.

**La catégorie visée se déclare**, au bloc `[interne]` de la pièce, en une ligne :

```
Catégories visées : Service public de l'énergie → 62
```

Sans déclaration, l'égalité hors titre 2 est refusée.

---

## 5. Le titre 2, qui ne se ferme pas encore

> **Minoration = M × a × d − I**, en AE comme en CP.
> **M** masse salariale · **a** = 0,90 · **d** fraction · **I** indemnités versées
> dans l'exercice.

**`I` vaut 70 % de l'économie de titre 2**, arbitrage de l'auteur du 20261016 :
l'indemnité est de 70 % du traitement indiciaire brut, et c'est la borne haute.
Il reste donc **30 % net**.

> **Titre 2 = arrêtée × 0,90 × fraction × 0,30**, en AE comme en CP.

Le socle **a = 0,90** s'applique bien à l'arrêtée, qui est brute : 3 287,5 × 0,90 =
2 958,8, soit F38 = 3,0 Md€ à 1,4 % près, et le § 5 du registre porte 1,48 Md€ pour
2027 — la chaîne redonne **1 479 367 851 €** avant indemnité. **Après indemnité :
443 810 355 €.**

---

## 6. Les quatre contrôles

| | ce qu'il vérifie | bloquant |
|---|---|---|
| **C1** | minoration AE ≤ AE du programme à l'état B 2027 | oui |
| **C2** | minoration CP ≤ CP du même programme | oui |
| **C3** | AE ≥ CP, l'égalité relevée sur la catégorie déclarée | oui |
| **C4** | minoration AE ≤ AE de la catégorie visée, recalée | **signal** |

C4 ne tranche pas : la ventilation par catégorie est au millésime 2026.

**Le plafond se lit avant le calcul, jamais après.** Comparer une minoration aux
crédits d'un exercice antérieur a fabriqué, le 15 octobre, un risque bloquant qui
n'existait pas.

---

## 7. Les six invariants de forme

1. **Une seule mission** par amendement, nommée ; la compensation lui est interne.
2. **Un tableau à quatre colonnes** : AE +, AE −, CP +, CP −.
3. **Somme des majorations = somme des minorations**, à l'euro, séparément en AE et
   en CP. Sans objet pour une minoration sèche, qui est licite.
4. **Chaque ligne nomme un programme**, jamais une action seule.
5. **Aucune majoration du titre 2 par prélèvement sur un autre titre**, et si le
   titre 2 est touché, AE = CP.
6. **L'amendement est motivé** et porte ses développements.

**Et un interdit** : un amendement de crédits ne se gage pas.

---

## 8. Ce que la chaîne rend aujourd'hui

Mesuré le 20261016 par `appareil/chaine_credits.py` sur les 247 lignes arrêtées :

| titre | AE minorées | CP minorés | CP/AE | programmes |
|---|---:|---:|---:|---:|
| 2 personnel, net d'indemnité | 443 810 355 | 443 810 355 | 1,000 | 13 |
| 3 fonctionnement | 8 025 487 709 | 7 826 451 221 | 0,975 | 53 |
| 5 investissement | 1 297 077 314 | 215 625 145 | 0,166 | 27 |
| 6 intervention | 42 678 397 631 | 36 863 777 899 | 0,864 | 64 |
| **total** | **52 444 773 009** | **45 349 664 621** | **0,865** | **76** |

**Dont état B du budget général** — le seul périmètre de la seconde partie :
**43 855 438 935 € d'AE** et **39 905 020 175 € de CP**, sur 58 programmes et
**23 missions, donc 23 amendements**, dix lignes plafonnées aux crédits de 2027.

**6 241,4 M€ sortent de l'état B** : dix-huit programmes relèvent de comptes
spéciaux — avances à l'audiovisuel public, contrôle de la circulation,
électrification rurale, patrimoine immobilier de l'État. Ils appellent un article
distinct, et `appareil/tablette_p2.py` les écarte.

**Dix programmes dépassent leur crédit ouvert de 2027**, parce que la table A est
bâtie sur les crédits de 2026 et le plafond sur ceux de 2027. Ils se plafonnent aux
crédits 2027, à ratio CP/AE conservé, et l'exposé dit en une phrase que le solde de
la mesure est porté ailleurs.

**Quatre programmes de la table A ne se retrouvent pas à l'état B 2027** sous le nom
qu'elle porte — Transformation publique, Affaires maritimes pêche et aquaculture,
Électrification rurale, Recherche appliquée et innovation en agriculture. À
rapprocher avant emploi.

---

## 9. Le compte par agent et par trimestre

L'agent qui perd se lit à la catégorie, dont `Economies R` donne le libellé.

| agent | T1 | T2 | T3 | T4 | année |
|---|---:|---:|---:|---:|---:|
| associations | 2 728,1 | 2 728,1 | 2 728,1 | 2 728,1 | **10 912,4** |
| ménages | 0,0 | 0,0 | 5 453,4 | 5 453,4 | **10 906,9** |
| entreprises | 2 150,8 | 2 150,8 | 2 613,3 | 2 613,3 | **9 528,3** |
| opérateurs | 1 666,1 | 1 666,1 | 1 666,1 | 1 666,1 | **6 664,4** |
| collectivités | 1 350,0 | 1 350,0 | 1 350,0 | 1 350,0 | **5 399,9** |
| agents publics | 0,0 | 0,0 | 221,8 | 221,8 | **443,6** |
| **total** | **7 895,0** | **7 895,0** | **14 032,7** | **14 032,7** | **43 855,4** |

Périmètre état B, après plafonnement et après indemnité.

En M€, en AE, sur l'état B.

**Ce tableau ne se confond pas avec celui du § 6 du registre.** Celui-ci est en
**caisse**, sur les seules autorisations d'engagement de l'état B de l'État ; celui
du registre est en **mesure**, toutes administrations publiques. Les deux couches ne
s'additionnent jamais, et tout chiffre se dit avec la sienne.

**Ce que la forme du tableau dit.** Rien ne bouge aux deux premiers trimestres pour
les ménages et les agents publics : leur coupe entre au 1er juillet, par R-P. Le
second semestre porte **62,9 %** de l'année. Entreprises, associations, opérateurs
et collectivités portent leur part dès le premier trimestre, par la même règle.

---

## 10. L'ordre d'exécution, en une ligne par étape

1. Ouvrir la table A, filtrer sur `Statut doctrine` = arrêté.
2. Lire la catégorie, en tirer la date, donc la fraction.
3. AE = AE arrêtées × fraction.
4. CP = min(CP arrêtés ; AE arrêtées) × fraction × (1 − résiduel).
5. Lire l'état B 2027, plafonner, déclarer la catégorie visée.
6. Jouer les quatre contrôles.
7. Écrire la pièce : une mission, un tableau, l'exposé sur l'AE.
8. **S'arrêter sur un bloquant.** Produire du neuf ne répare rien.
