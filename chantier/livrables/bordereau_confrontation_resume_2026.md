# Bordereau — le résumé attendu du texte financier 2026, confronté à la pièce

**Livrable confronté** : `livrables/resume_attendu_texte_financier_2026.md`, gelé
le 20260916.
**Pièces rouvertes** : `referentiels/redaction_plf.json` (82 articles, liminaire
compris), `referentiels/redaction_plfss.json` (55 articles),
`referentiels/articles_ouverts_plf.tsv` et `articles_ouverts_plfss.tsv`, et les
trois classeurs du projet — annexe 2 du tome I, annexe 3 du tome II, Synthèse ETP
et agences.
**Appareil versé** : `appareil/confronter_lecture.py` et son jeu de fautes
`appareil/faux_lecture.py`. **Les cinq fautes mordent**, dont le verdict
retourné.
**Ce bordereau ne bloque rien.**

---

## 1. Ce que ce fil a établi d'abord

**Le résumé porte des repères, et ils sont confrontables.** Leur forme est
constante : la pièce nommée, l'article, l'emplacement — hors-alinéa, alinéa
numéroté, tableau —, la page, et le libellé exact de la ligne. La question posée
en tête du fil est donc tranchée dans le bon sens : **le taux de concordance se
calcule**, et il n'y a pas lieu de reconstituer une table de repères.

La table de repères est extraite du résumé **mécaniquement** : tableaux markdown
sous leur ligne de source, en-têtes de colonne portant leur propre repère,
valeurs de prose portant un repère d'article et de page. Rien n'est transcrit à
la main. Elle est versée à `referentiels/reperes_resume_2026.tsv`, et le relevé
de confrontation à `livrables/confrontation_resume_2026.tsv`.

---

## 2. Le compte

| | |
|---|---|
| valeurs relevées avec repère | **308** |
| concordent | **291** |
| divergent | **1** |
| introuvables | **15** |
| non sourcées | **1** |
| **taux de concordance sur les confrontables** | **99,7 % sur 292** |
| grandeurs affirmées sans aucun repère | **0** |

| bloc | concorde | diverge | introuvable | non sourcé | taux |
|---|---|---|---|---|---|
| en-tête | 2 | 0 | 0 | 1 | 100 % |
| L1.a solde, côté finances | 96 | 0 | 0 | 0 | 100 % |
| L1.b effets de périmètre | 5 | 0 | 0 | 0 | 100 % |
| L1.d équilibre par branche | 61 | 0 | 0 | 0 | 100 % |
| L1.e objectif de dépenses | 14 | 0 | 3 | 0 | 100 % |
| L2 portes ouvertes | 33 | 1 | 0 | 0 | 97,1 % |
| L3.a impositions affectées | 20 | 0 | 4 | 0 | 100 % |
| L3.b dépenses fiscales | 24 | 0 | 7 | 0 | 100 % |
| L3.c opérateurs | 36 | 0 | 1 | 0 | 100 % |

**Deux opérations, et le relevé dit laquelle.** 189 valeurs sont rouvertes par
**lecture** au repère ; 119 agrégats sont rejoués par **réapplication** sur la
structure, chaque réapplication portant sa recette, nommée et motivée dans le
module.

**Une réserve sur la précision, et elle est de fond.** Sur les 185 concordances
de lecture, 64 se prononcent **à la ligne** — le libellé du résumé est l'étiquette
de la ligne de la pièce —, 15 **à la section** d'un tableau, et **106 au seul
périmètre de l'article** : la valeur est bien dans l'article visé, à la page
visée, mais rien ne prouve mécaniquement qu'elle y est à la ligne que le résumé
nomme. C'est le plafond de ce que la pièce aplatie permet, et c'est exactement
la difficulté 2 que le résumé décrit lui-même.

---

## 3. La divergence — une seule, affichée des deux côtés

| repère | ce que le livrable dit | ce que la pièce porte |
|---|---|---|
| L2, « 594 adresses ouvertes, sur **81 textes**, par 92 articles des deux véhicules » | **81 textes** | **73 textes distincts** |

Les deux comptes sont justes et ne disent pas la même chose. 81 est la somme des
deux comptes par véhicule — 49 au PLF, 32 au PLFSS, que la confrontation valide
l'un et l'autre. 73 est le compte des textes **distincts** : huit textes sont
ouverts par les deux véhicules et comptés deux fois — code de commerce, code de
la santé publique, code de la sécurité sociale, code de procédure pénale, code
des transports, code du travail, code général des impôts, code rural et de la
pêche maritime.

**Cette divergence ne s'arbitre pas ici.** Elle remonte : « sur 81 textes » se
lit naturellement comme un compte de textes, et c'est un compte d'occurrences.

---

## 4. Les introuvables — quinze, par famille

**a. Une réapplication que la pièce ne permet pas — 1**

- **L3.a, somme des plafonds d'affectation 2026 de l'article 36, 21 374 967 575 €.**
  La colonne des plafonds ne se sépare pas de celle du rendement prévisionnel :
  la géométrie de colonne n'est stable ni d'une page à l'autre ni à l'intérieur
  d'une page. Le résumé le déclare lui-même — difficulté 2, emplacement non
  relevé 8, où deux passes de lecture avaient donné deux valeurs. **La
  confrontation ne tranche pas et n'invente pas de recette.**
  Conséquence directe : l'écart de **354 040 674 €** entre le tableau de
  l'article 36 et le classeur ne se rejoue pas davantage.

**b. Une recette que le livrable n'a pas déclarée — 5**

- **L3.b, le relevé des formules modificatives** : 154 alinéas d'abrogation ou
  de suppression au PLF sur 38 articles, 63 au PLFSS sur 19 ; 129 alinéas de
  création au PLF sur 37 articles, 60 au PLFSS sur 26. Le livrable annonce un
  « relevé mécanique » sans nommer les formules relevées. Sans la liste des
  formules, l'opération ne se rejoue pas.
- **L3.c, « Fusionnés — 0 »** : le balayage des formules de dissolution, de
  fusion et de transfert à l'État n'est pas déclaré non plus. **Une absence ne
  se rejoue pas sans la règle qui l'a produite** — et c'est la rubrique où une
  absence pèse le plus.

**c. Une grandeur calculée par le livrable, sans repère propre — 3**

- **L1.e**, l'écart des totaux **+4,5 Md€** et **+1,69 %**, et la remarque sur le
  sous-objectif « personnes handicapées » écrit **« 16 »** sans décimale. Les
  valeurs dont ces grandeurs dérivent concordent toutes ; la dérivation, elle,
  n'a pas d'adresse dans la pièce.

**d. Un agrégat de classeur sans recette déclarée — 6**

- **L3.a**, la réaffectation DEFI / Institut Français du Textile et de
  l'Habillement : **70 %** et **30 %**, relevés à la rédaction et non au tableau ;
  l'écart de 354 040 674 € (voir a).
- **L3.b**, trois comptes d'articles adossés au même relevé de formules que b.

---

## 5. Le non sourcé — un seul

- **En-tête**, « PLFSS 2026 n° 1907 […] **162 pages** ». La pièce est un PDF
  absent de l'atelier ; son empreinte est déclarée, son compte de pages ne se
  rouvre pas d'ici. Les deux autres grandeurs de l'en-tête — 82 articles au PLF,
  55 au PLFSS — concordent avec les deux référentiels de rédaction.

---

## 6. Ce qui relève du jugement, et qui n'entre dans aucun taux

Nommé, non compté, une ligne par point, avec la question posée.

| point | question qui revient à l'auteur |
|---|---|
| **L4 — l'écart à nos positions**, 56 propositions, 5 / 22 / 29 | La règle de verdict — exiger un acte du texte sur le siège même que la mesure vise — a été posée dans le fil du lot A faute d'arbitrage antérieur. La valide-t-on, ou la resserre-t-on ? |
| **L4, deux *va contre* sur vingt-deux tiennent à l'article des plafonds d'emplois** | Un article que la loi organique impose chaque année doit-il produire un *va contre* ? |
| **Le compte par bloc, 76 rubriques, 68 remplies** | Décompte que le livrable fait de lui-même : il ne se confronte à aucune pièce. |
| **Les douze emplacements de page non relevés** | Lesquels ouvre-t-on au lot suivant — l'état A et l'état B d'abord ? |
| **Les neuf difficultés de lecture** | C'est le produit principal du lot A, et la spécification du module à venir. Rien à y confronter. |
| **L2, « 81 textes »** | Voir la divergence au point 3 : compte d'occurrences ou compte de textes distincts ? |

---

## 7. Ce que la confrontation a démenti au passage

**Le trou annoncé sur le PLFSS n'est pas là où on le croyait.** Les sept articles
du PLFSS marqués comme portant un tableau — liminaire, 1er, 2, 14, 15, 16, 49 —
ont bien **zéro ligne hors-alinéa**. Mais leurs tableaux vivent dans les
**alinéas**, en prose aplatie, et ils s'y rouvrent : les 61 valeurs du bloc L1.d
et les 14 du bloc L1.e concordent toutes, tableaux d'équilibre par branche et
objectif national de dépenses compris. **Aucune valeur n'est sortie `introuvable`
pour cause de pièce manquante côté financement.** Il n'y avait rien à combler.

---

## 8. Deux arbitrages pris dans ce fil, et inscrits

- **Un agrégat ne se lit pas, il se rejoue.** Toute valeur dont la pièce est un
  classeur ou une table sort par réapplication, avec une recette déclarée dans le
  module ; sans recette, elle sort `introuvable` avec son motif. Aucune recette
  n'a été écrite en cours d'exécution pour laisser passer ce qu'on venait de
  trouver.
- **Un séparateur de milliers est une seule espace suivie de trois chiffres.**
  La pièce sort de `pdftotext -layout`, où les colonnes sont séparées par
  plusieurs espaces : traiter toute suite d'espaces comme un séparateur collait
  « 1 652   1 696 » en un seul nombre et faisait diverger trente lignes justes.
  C'est la faute d'un contrôle qui invente sa propre lecture au lieu de lire la
  pièce ; elle est corrigée et le jeu de fautes la garde.
