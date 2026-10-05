# Ordre de baisse des concours aux collectivités sous contrainte de part déterminante — 20261004

**Mandat** : trancher la question suspendue au § 2 de `methode/fragments/arbitrages/20261004-depot-domicile-dgf-et-gabarit.md`.
L'arbitrage du 20261002 — « toutes les économies en taxe sur la valeur ajoutée » — était suspendu sur ce point.
**Aucune disposition n'est rédigée ici.**

---

## 1. Mesure d'entrée

**Définition en vigueur des ressources propres.** Article LO 1114-2 du code général des collectivités
territoriales : le produit des impositions de toutes natures **dont la loi autorise la collectivité à fixer
l'assiette, le taux ou le tarif, ou dont elle détermine, par collectivité, le taux ou une part locale
d'assiette**, les redevances pour services rendus, les produits du domaine, les participations d'urbanisme,
les produits financiers et les dons et legs.

**Ratio imposé.** Article LO 1114-3 : le ratio rapporte les ressources propres à l'ensemble des ressources
de la catégorie, **emprunts exclus**, ainsi que les ressources correspondant à des compétences transférées
à titre expérimental ou déléguées. « **Pour chaque catégorie, la part des ressources propres ne peut être
inférieure au niveau constaté au titre de l'année 2003.** » La loi organique **ne fixe aucun pourcentage en
dur** : le plancher est un niveau historique, constaté par catégorie.

| catégorie | plancher 2003 | dernier ratio constaté (2021) |
|---|---|---|
| communes et établissements publics de coopération intercommunale | **60,8 %** | 70,9 % |
| départements | **58,6 %** | 74,7 % |
| régions | **41,7 %** | 73,9 % |

**Les deux faits qui commandent toute la suite.**

1. **La dotation globale n'est pas une ressource propre** — dotations et participations sont au dénominateur
   seul.
2. **La fraction de taxe sur la valeur ajoutée en est une** — non parce que la collectivité en voterait le
   taux, mais par la seconde branche de LO 1114-2 : la loi en détermine, par collectivité, une part locale
   d'assiette. C'est la conjonction « ou » qui la fait entrer, et elle est contestée en doctrine sans avoir
   été censurée.

**Base mesurée** (rapport du Gouvernement sur l'autonomie financière, exercice 2021, en M€) :

| catégorie | ressources propres `P` | ressources totales `T` | autres ressources `A = T − P` | dont dotations et participations |
|---|---|---|---|---|
| communes et EPCI | 94 313 | 133 038 | 38 725 | 32 181 |
| départements | 50 543 | 67 639 | 17 096 | 14 909 |
| régions | 24 556 | 33 214 | 8 658 | 4 402 |

**Rang de source : 2 — source déclarée.** Le dépôt de droit n'est pas disponible dans ce fil et Légifrance
refuse la lecture directe ; les verbatim de LO 1114-2 et LO 1114-3 sont tenus de sources secondaires
concordantes. **Le verbatim est à reprendre au dépôt de droit avant tout emploi en pièce.**

---

## 2. Le mécanisme, qui tranche la question

Soit `R = P / (P + A)`.

- **Baisser une dotation**, c'est retrancher `d` de `A` seul : `R' = P / (P + A − d)`. **Le ratio monte,
  toujours, quel que soit le montant.** Il ne peut pas rompre.
- **Baisser une fraction de taxe sur la valeur ajoutée**, c'est retrancher `t` de `P` et de `T` à la fois :
  `R' = (P − t) / (P + A − t)`. **Le ratio baisse, toujours**, puisque `P < T`.

**L'auteure a raison, et l'effet est plus fort que l'intuition ne le dit.** Il ne s'agit pas seulement
d'éviter de dégrader le ratio : **chaque euro de dotation retranché achète de la marge sur la jambe de
taxe.** Avec `k = r₂₀₀₃ / (1 − r₂₀₀₃)`, la coupe admissible en ressources propres vaut `t_max = P − k·A`.
La dérivée est `dt_max/dd = + k`.

| catégorie | `k` | marge gagnée par euro de dotation coupé |
|---|---|---|
| communes et EPCI | 1,551 | **1,55 €** |
| départements | 1,415 | **1,42 €** |
| régions | 0,715 | **0,72 €** |

**Conclusion : la baisse porte d'abord sur la dotation globale, intégralement, avant toute coupe en fraction
de taxe sur la valeur ajoutée. L'arbitrage du 20261002 est inversé sur l'ordre ; il n'est pas défait sur le
reste.**

---

## 3. Ordre de baisse et ratio atteint à chaque étape

### Bloc communal — plancher 60,8 %

| étape | opération | ressources propres | ressources totales | ratio |
|---|---|---|---|---|
| 0 | état constaté | 94 313 | 133 038 | 70,9 % |
| 1 | − 10 000 de dotations | 94 313 | 123 038 | 76,7 % |
| 2 | − 20 000 cumulés | 94 313 | 113 038 | 83,4 % |
| 3 | − 32 181 — **toutes dotations et participations** | 94 313 | 100 857 | **93,5 %** |
| 4 | puis − `t` en fraction de taxe | 94 313 − `t` | 100 857 − `t` | décroissant |
| **rupture** | `t` = **84 163** | 10 150 | 16 694 | **60,8 %** |

**Ordre inverse, pour mesurer ce qu'il coûte** : dotations intactes, la rupture arrive à
**`t` = 34 251**. **L'inversion de l'ordre fait passer la coupe admissible de 34,3 Md€ à 84,2 Md€ — un
facteur 2,5.**

### Départements — plancher 58,6 %

| ordre | coupe admissible en fraction de taxe avant rupture |
|---|---|
| taxe d'abord, dotations intactes | 26 343 |
| **dotations d'abord** (− 14 909), puis taxe | **47 447** |

### Régions — plancher 41,7 %

| ordre | coupe admissible en fraction de taxe avant rupture |
|---|---|
| taxe d'abord, dotations intactes | 18 363 |
| **dotations d'abord** (− 4 402), puis taxe | **21 512** |

**Ce que ce dernier tableau dit, et il est structurant** : la réserve de dotation est presque épuisée pour
les régions — 4,4 Md€ — parce que l'État a déjà converti leur dotation globale en fraction de taxe sur la
valeur ajoutée en 2018, et une part de celle des départements en 2021. **Là où la conversion a déjà eu lieu,
la règle « la dotation d'abord » n'a plus de matière.** Elle garde toute sa force sur le bloc communal, où
la dotation globale de fonctionnement reste le concours principal.

---

## 4. Point de rupture constitutionnel — quatre, dans l'ordre où ils se présentent

**1. Le ratio n'est pas le point de rupture, et la suppression des échelons le fait disparaître.**
L'article 72 de la Constitution nomme les départements et les régions. M-010 — échelon local unique, bloc
B-03 — **ne passe pas à Constitution inchangée** : il relève de la proposition de loi constitutionnelle.
Une fois la révision acquise, **la catégorie disparaît et son ratio avec elle** : LO 1114-3 ne s'applique
plus qu'à la commune. La contrainte analysée ici ne survit, au terme du schéma, que pour le bloc communal.

**2. À Constitution inchangée, LO 1114-3 est injoignable par la voie des dotations.** Aucune coupe de
concours non propre, si massive soit-elle, ne peut rompre le ratio — elle l'améliore. **La rupture est un
événement de la jambe fiscale, et d'elle seule.**

**3. La contrainte qui mord avant LO 1114-3 est l'alinéa 4 de l'article 72-2** — compensation des
compétences transférées — **et la libre administration**. Le juge constitutionnel censure la ressource
retirée qui prive la collectivité des moyens de ses compétences, non le ratio arithmétique. **Le schéma y
répond par construction** : M-010 et M-015 retirent les compétences avant les ressources ; la baisse suit le
transfert au lieu de le précéder. **C'est la défense principale, et elle ne passe pas par le ratio.**

**4. Le risque propre à la jambe fiscale n'est pas le montant, c'est la qualification.** La fraction de taxe
n'est ressource propre que par la part locale d'assiette déterminée par collectivité. **Une refonte qui
supprimerait la clé de répartition par collectivité ferait sortir la fraction du numérateur sans qu'un seul
euro soit coupé** — et la rupture arriverait par la définition, non par le montant. Articulation à tenir
avec M-029, taux unique de taxe sur la valeur ajoutée.

**Nature de la sanction, à ne pas surévaluer.** L'article LO 1114-4 fait constater le ratio par un rapport
transmis deux ans après l'exercice, et impose la correction **par la deuxième loi de finances suivant le
constat**. La rupture n'est pas une censure immédiate : c'est une obligation de correction différée, doublée
d'un contrôle du juge sur l'effet de la mesure au moment du vote.

---

## 5. Ce que l'analyse emporte sur le corpus

**Sur l'arbitrage du 20261002, § 1** — « toutes les économies en taxe sur la valeur ajoutée » : **inversé
quant à l'ordre**. La remontée se fait **d'abord en dotation, jusqu'à épuisement, ensuite seulement en
fraction de taxe**. Ce qui reste acquis du 20261002 : la taxe foncière unique est une fusion de principe,
sans calcul de rendement.

**Sur la pièce 4.4** — aucune reprise due. La taxe foncière unique est une imposition à taux voté localement :
elle est ressource propre pleine et entière, et elle **remplace des impositions qui l'étaient déjà**.
À produit constant pour chaque commune, elle laisse le ratio inchangé ; en absorbant l'impôt sur la fortune
immobilière et la taxe annuelle sur les logements vacants, qui étaient des recettes d'État, **elle le fait
monter**. Combinée à l'épuisement de la dotation globale, elle rend LO 1114-3 **pratiquement inopérant pour
le bloc communal**.

**Reste ouvert, et ce n'est pas tranché ici** : la ventilation de la baisse entre dotation globale de
fonctionnement et autres concours du prélèvement sur recettes — le ratio ne les distingue pas, la lisibilité
politique peut-être.
