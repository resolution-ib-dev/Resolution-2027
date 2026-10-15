# Commissions et instances consultatives — relevé du Jaune PLF 2026, 20261014

**Objet.** Le référentiel `commissions_jaune2026_20261014.tsv` porte, instance par
instance, la liste annexée au projet de loi de finances pour 2026 des commissions
et instances consultatives ou délibératives placées directement auprès du Premier
ministre, des ministres ou de la Banque de France.

**Deux valeurs corrigées le 20261015**, par recompte sur le référentiel lui-même :
le nombre d'instances supprimées et le nombre de rattachements. Le détail est au
§ 5. Rien d'autre n'a bougé : les 317 instances en vigueur, les 32,5 M€, les
10 884 membres et les 3 417 réunions sont confirmés à l'unité.

---

## 1. Ce que porte le relevé

| grandeur | valeur |
|---|---:|
| instances en vigueur relevées | **317** |
| instances supprimées depuis 2024 | **6** |
| rattachements | **14 ministères** + Banque de France |
| coût de fonctionnement 2024 | **32,5 M€** |
| membres | **10 884** |
| réunions tenues en 2024 | **3 417** |

Colonnes : `ministere`, `instance`, `texte_institutif`, `membres`, `cout_2022` à
`cout_2024` en milliers d'euros, `reunions_2022` à `reunions_2024`, `statut`,
`page` du Jaune, `observations` reprises du Jaune.

**Répartition par rattachement** — Travail, santé, solidarités et familles 43 ·
Économie et finances 39 · Éducation nationale et recherche 36 · Culture 35 ·
Transition écologique 34 · Premier ministre 33 · Aménagement du territoire 31 ·
Agriculture 19 · Intérieur 15 · Armées 10 · Justice 9 · Europe et affaires
étrangères 6 · Action publique 5 · Outre-mer 1 · Banque de France 1. **Somme : 317.**

## 2. L'écart au nombre annoncé — à arbitrer

**Le Jaune annonce 318 instances ; le relevé en trouve 317.** Les tableaux ont été
lus page à page sur les 113 pages, et aucune ligne d'instance n'a été écartée.
L'écart d'une unité n'est pas expliqué : il se tranche sur pièce, il ne se comble
pas. Il est porté à l'onglet de synthèse du classeur livré.

## 3. Le contrôle des doubles comptes

Les 317 libellés ont été rapprochés un à un des **750 entités de l'onglet
`ODAC-ODAL R`** et des **180 lignes de l'onglet `Opérateurs R`** du classeur
`Synthèse ETP et agences Résolution_0910.xls`, hors mots vides.

**Aucun double compte.** Six rapprochements ont été examinés puis écartés, l'organe
consultatif et l'organisme gestionnaire étant deux personnes morales distinctes :
CNESER / HCERES · Conférence nationale des services d'incendie et de secours / les
SDIS · Conseil national de pilotage des ARS / les ARS · Conseil supérieur de la
fonction publique hospitalière / CNG · Haut conseil de la santé publique / Santé
publique France · Conseil supérieur de la fonction publique territoriale / centres
de gestion.

**Conséquence.** Les commissions forment bien un bloc distinct dans le compte des
1 104 agences d'État, qui se décompose en 434 opérateurs + 328 organismes hors PLF
+ 24 autorités indépendantes + 318 commissions.

## 4. Deux réserves de lecture

- **Le coût de fonctionnement n'est pas le coût complet.** Le Jaune chiffre le
  fonctionnement de l'instance, non le temps de ses membres ni celui des
  administrations qui l'instruisent.
- **Un coût à zéro ne vaut pas inactivité.** Plusieurs instances portent 0 € et 0
  réunion parce que leurs dépenses sont absorbées par une autre structure, ce que
  les observations du Jaune disent au cas par cas.

## 5. Les deux corrections du 20261015

**Instances supprimées : 6 et non 7.** Le référentiel porte 324 rangs de données,
dont 317 au statut « en vigueur » et 7 au statut « supprimée depuis 2024 ». Le
septième n'est pas une instance : c'est la ligne d'en-tête du tableau des
suppressions du Jaune, dont la cellule `instance` porte le mot « Ministère » et
dont toutes les cellules de coût, de membres et de réunions sont vides. Elle a été
relevée comme un rang faute d'être distinguée à l'extraction. **Les six instances
supprimées** relèvent de trois rattachements : Travail, santé, solidarités et
familles 3 · Économie, finances, souveraineté industrielle et numérique 2 ·
Culture 1. Le rang d'en-tête reste au référentiel, où il est reconnaissable à sa
cellule `instance` ; il ne se compte pas.

**Rattachements : 14 ministères et la Banque de France, non 15 et la Banque de
France.** Le référentiel porte quinze valeurs distinctes en colonne `ministere`,
Banque de France comprise. La Banque de France n'est pas un ministère : le
dénombrement l'ajoutait au compte des ministères au lieu de l'en distraire.

---

**Source** : liste des commissions et instances consultatives ou délibératives
placées directement auprès du Premier ministre ou des ministres, annexe au projet
de loi de finances pour 2026, 113 pages. Relevé du 20261014, recompte du 20261015
sur le référentiel, tableaux extraits page
à page. **Livrable** : `Commissions_R_20261014.xlsx`, onglets `Commissions R` et
`Commissions — synthèse`, à verser au classeur `Synthèse ETP et agences`.
