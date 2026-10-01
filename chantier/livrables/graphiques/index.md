# Graphiques du classeur de synthèse, rendus dans la charte du site

*Arrêté le 20260925. Douze onglets mesurés, dix-sept graphiques d'origine,
**quinze pièces retenues**. Chacune en HTML autonome + PNG haute définition,
lisible sur mobile, source en pied, chaque chiffre traçable à sa cellule.
Charte : `fiche.css` du site — Archivo aux titres, chiffres et capitales,
Source Serif 4 au texte, papier crème, filet tricolore.*

---

## La palette

**L'orange de la couverture est la couleur du mouvement.** Le vert est écarté.

| rôle | valeurs |
|---|---|
| orange, du clair au foncé | `#f2c4ac` · `#e1865c` · `#d2490a` · `#b03c07` |
| bleu, du clair au foncé | `#a8c4d8` · `#6d96b5` · `#2f5d87` |
| violet | `#8a6f93` |
| gris neutre | `#6d6a64` |

**Grammaire.** L'orange marque ce qui est discuté, cessible, restituable ou hors
du périmètre essentiel ; son intensité monte avec la portée de la mesure. Le bleu
marque ce qui est conservé. Le violet est réservé à ce qui n'est ni l'un ni
l'autre — la sécurité sociale et la santé : les mettre en orange laissait croire
qu'elles étaient facultatives. Le gris ne sert qu'à la charge de la dette, qui
n'est pas une politique publique.

## Les règles de rendu

- **Chiffres** : deux significatifs, trois au besoin ; une décimale seulement
  sous 10. 392, 231, 49, 13 — mais 8,9 et 3,5.
- **Écritures** : quatre corps fixes, jamais calculés sur la largeur d'écran ;
  l'agrégat ne dépasse jamais son libellé de plus du double ; pas de capitales
  dans les tuiles ; aucun mot coupé.
- **Filets** : trait plein de 3 px autour d'un groupe, tirets de 20 px espacés de
  12 à l'intérieur, même blanc. C'est l'épaisseur qui dit le niveau, pas le style.
  Aucun titre ne chevauche un filet.
- **Marges** : réduites au minimum, pour que les graphiques soient hauts et les
  écarts vertigineux.
- **Échelles** : jamais tronquées, toujours ancrées à zéro.
- **Hachures** : 7 % d'opacité, 2 px tous les 15 — visibles seulement en les
  cherchant.

---

## Les quinze pièces

| fichier | onglet | forme |
|---|---|---|
| `Graph236_orange` | Graph236 | treemap à deux niveaux, palette chaude |
| `Graph1672Md_depense_publique` | Graph1672Md | treemap, tri de couleur, sécu en violet |
| `GraphETP_emplois_publics` | GraphETP | treemap, dégradé sur le hors-périmètre |
| `GraphPatrimoine_patrimoine_public` | GraphPatrimoine | treemap, dégradé sur le restituable |
| `GraphAgences_agences_grille_unite` | GraphAgences | grille, un carré = une agence |
| `GraphGov_depenses` | GraphGov | colonnes, France en vedette orange |
| `GraphGov_deficit` | GraphGov | colonnes, axe zéro respecté |
| `GraphRDB_revenu_median` | GraphRDB | colonnes, écart % et montant mensuel |
| `GraphRDB_revenu_ppa` | GraphRDB | idem, en pouvoir d'achat |
| `GraphVA_valeur_ajoutee` | GraphVA | colonne empilée, 63 € en vedette |
| `Graph51pc_representation` | Graph51pc | pyramide centrée, flèches de vote |
| `GraphCodes_volume_normes` | GraphCodes | aires empilées, dégradé de progression |
| `GraphIR_profil` | GraphIR | aires + ligne, bascule annotée |
| `GraphAFU_solidarite` | GraphAFU | strates empilées par âge |

## Ce qui est écarté, et pourquoi

- **`GraphIR_cinq_cas` — À REFAIRE.** Le rendu ne montre pas la mécanique de la
  mesure. Retiré du lot.
- **Devenir des 35 ministères — À VISUALISER.** Le graphique en barres n'apporte
  rien sur trois valeurs. Le sujet reste à traiter, la forme est à trouver.
- Le schéma de tri des agences en barres et la grille au carré de cinq sont
  abandonnés au profit de la grille à l'unité.
- Les variantes brique et bleue sont abandonnées : la palette orange est arrêtée.

## Les écarts assumés au classeur

- **GraphCodes** : le classeur porte le Code de l'environnement sur un axe
  secondaire. Un double axe fausse la comparaison ; il est retiré du graphique,
  qui ne montre plus que les deux agrégats. Aucune valeur ne change.
- **GraphRDB** : le second graphique est remis dans l'ordre croissant du premier.
  Ses écarts en pourcentage et les montants mensuels sont calculés — le classeur
  ne porte les écarts que sur le premier. C'est dit en pied de pièce.
- **GraphETP et GraphPatrimoine** : la couleur porte une **lecture doctrinale**
  (ce qui sort du périmètre essentiel, ce qui est restituable) qui ne figure dans
  aucune colonne du classeur. **À valider sur pièce.**
- **GraphETP** : départements et régions partagent une bande, chacun gardant son
  libellé et son chiffre — à 99 milliers d'agents, les régions ne tenaient
  aucune surface lisible dans le pavage.

## Le contrôle de cohérence sur l'impôt

Confronté à `Synthèse Calculs Résolution_0910.xlsx`, onglet Refonte fiscalité :

- aide fondamentale 550 €/mois = 6 600 €/an — **concorde** (G50) ;
- pondération enfant 0,5 → 3 300 €, part handicap 1 → 6 600 € — **concordent** ;
- revenu d'entrée dans l'impôt net 28 695,65 € — **concorde** (J53) ;
- **écart** : les graphiques appliquent un taux de **23 %**, la synthèse estime le
  taux unique à **22,74 %** (K50). Le seuil de 28 696 € découle du 23 %. À
  22,74 %, la bascule serait à 29 024 €. **Arbitrage non rendu.**

## Ce qui reste ouvert

1. **Le taux d'impôt** : 23 % ou 22,74 %. Décision de fond.
2. **La lecture doctrinale** portée par la couleur sur les emplois publics et le
   patrimoine, à valider.
3. **Les liens du bloc « les valeurs, cellule par cellule »** doivent pointer vers
   **l'onglet sous-jacent** du bon classeur, pas seulement vers le fichier.
   L'ancre est aujourd'hui `../donnees.html#synthese-graphiques`, à brancher par
   le fil code quand la page Données existera.
4. **Le placement sur le site** — « pour approfondir » dans les fiches et le
   manifeste, page Données qui rassemble — relève du fil code, après validation.
5. **Pousser la créativité** sur les formes, dans un fil suivant.
