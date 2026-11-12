# Opérateurs de l’État — relevé du Jaune PLF 2026, 20261112

**Objet.** Trois tableaux portent, opérateur par opérateur, ce que l’annexe au
projet de loi de finances pour 2026 « Opérateurs de l’État » dit de chacun : qui il
est, ce que l’État lui verse en 2025 et en 2026, et combien d’emplois il porte.

| fichier | une ligne par | lignes |
|---|---|---:|
| `operateurs_jaune2026_20261112.tsv` | opérateur ou catégorie d’opérateurs | **180** |
| `operateurs_jaune2026_categories_20261112.tsv` | entité d’une catégorie | **268** |
| `operateurs_jaune2026_entites_20261112.tsv` | entité (nature juridique, classement ODAC) | **431** |

**La pièce lue** est le PDF du jaune (663 pages), rangé au dépôt du site :
`Site-ETNP/site/donnees/PLF 2026_Jaune - Operateurs.pdf`. **Le lecteur** est
`Site-ETNP/outils/jaune.py`. Tout ce qui suit est *relevé* : chaque grandeur a été
recomptée sur les trois fichiers le jour de l’écriture.

---

## 1. Ce que porte le relevé

Cinq tableaux du jaune sont lus.

| tableau du jaune | pages | ce qui en est tiré |
|---|---|---|
| Liste des opérateurs de l’État | 30 à 47 | statut, comptabilité budgétaire, mission et programme chefs de file, nombre d’entités ; entités de chaque catégorie |
| Financement 2025/2026 par le budget de l’État | 48 à 65 | crédits de paiement par nature, programmes financeurs |
| Financement 2025/2026 par les taxes affectées | 66 | montant versé à chaque opérateur |
| Emplois 2025/2026 | 67 à 73 | ETPT, six colonnes par année |
| Liste des opérateurs / ODAC | 207 à 218 | nature juridique et classement ODAC de chaque entité |

**Ne sont pas lus** : les tableaux d’exécution 2022-2024 (financements, ressources
propres, emplois, masse salariale, trésorerie), les dettes et engagements hors
bilan, les données immobilières, les dix plus fortes rémunérations et les budgets
initiaux 2025 opérateur par opérateur (pages 219 à 663).

### Colonnes de `operateurs_jaune2026_20261112.tsv`

- `operateur`, `statut`, `comptabilite_budgetaire` (O ou N), `mission`,
  `programme_chef_de_file`, `nombre_entites`. Une catégorie rattachée à plusieurs
  programmes a plusieurs lignes à la liste du jaune ; elles sont réunies ici, les
  missions et les programmes séparés par ` | `, le nombre d’entités additionné.
- `programmes_financeurs` : ceux de la ligne grise du tableau de financement.
- `scsp_`, `investissement_`, `transferts_`, `dotations_` suivis de `2025` (LFI) et
  `2026` (PLF) : **crédits de paiement, en milliers d’euros**. Dans l’ordre :
  subvention pour charges de service public (catégorie 32), subvention pour charges
  d’investissement (catégorie 53), transferts (titre 6), dotations en fonds propres
  (catégorie 72). Les autorisations d’engagement ne sont pas reprises.
- `taxes_affectees_2025`, `taxes_affectees_2026` : **en euros**, comme au jaune.
- `etpt_…_2025` et `etpt_…_2026` : ETPT rémunérés par d’autres programmes
  (`autres_programmes`), par le programme (`ce_programme`), par l’opérateur sous
  plafond (`sous_plafond`) et hors plafond (`hors_plafond`), dont contrats aidés et
  dont apprentis.

## 2. Les grandeurs, et leur contrôle sur le jaune lui-même

Le lecteur s’arrête si une somme ne retrouve pas le total que le jaune publie.

| grandeur | relevé | publié par le jaune | écart |
|---|---:|---:|---|
| opérateurs (somme de `nombre_entites`) | **431** | 431 (p. 30) | aucun |
| entités classées (fichier `entites`) | **431**, dont **356** ODAC | — | — |
| subvention pour charges de service public, PLF 2026 | **33 893 819 k€** | 33 893 823 323 € (p. 24) | 4 k€, arrondis de ligne |
| subvention d’investissement, PLF 2026 | **1 022 878 k€** | 1 022 879 338 € | 1 k€ |
| transferts, PLF 2026 | **16 696 523 k€** | 16 696 522 245 € | 1 k€ |
| dotations en fonds propres, PLF 2026 | **0** | 0 | aucun |
| taxes affectées 2026 | **21 675 050 802 €**, 24 bénéficiaires | 21 675 050 802 € (p. 66) | aucun |
| taxes affectées 2025 | **20 551 454 414 €** | 20 551 454 414 € | aucun |
| emplois sous plafond, PLF 2026 | **401 310 ETPT** | 401 310 (total du tableau, p. 73) | aucun |
| emplois, les onze autres colonnes | sommes égales au total du tableau | — | aucun |

**Deux écarts sur la colonne LFI 2025, constatés et non expliqués par la pièce** :
la subvention pour charges de service public relevée est de 33 488 265 k€ pour
33 491 513 097 € publiés (3,2 M€ de moins), les transferts de 19 797 176 k€ pour
19 833 126 204 € publiés (36,0 M€ de moins). Les mêmes lignes donnent la colonne
PLF 2026 à l’arrondi près : la lecture n’est donc pas en cause. *Déduit, non
relevé* : le tableau de financement ne porte que les opérateurs du périmètre 2026
et un sorti du périmètre, quand le total publié pour 2025 porte tout le périmètre
2025.

## 3. Ce que le relevé fait voir

- **Douze lignes n’ont aucun financement par le budget en 2026**, dont six vivent de
  taxes affectées (AFITF, agences de l’eau, ANCOLS, CGLLS, CNC, SGP ; l’INPI aussi)
  et trois sont à la liste sans figurer au tableau de financement : Cinémathèque
  française, ENSMIS, Fonds national des aides à la pierre.
- **Centre Inffo** figure aux tableaux de financement et d’emplois pour 2025
  (72 ETPT sous plafond) et non à la liste : le jaune le dit sorti du périmètre.
  Sa ligne est gardée, sans statut.
- **Pass Culture** est à la liste sans statut ; le tableau des entités le donne SAS.
- **Seize catégories** regroupent 268 entités ; le compte de chacune au fichier
  `categories` égale son `nombre_entites` au fichier principal.

## 4. Rapprochement avec le classeur ETP

Les 180 lignes de l’onglet `Opérateurs R` de `Synthèse ETP et agences
Résolution_0910.xlsx` se retrouvent toutes dans le relevé, une seule par un nom
différent (« Centre inffo » au classeur, « Centre info » au jaune). **Le classeur
compte 434 opérateurs, le jaune 431** : l’écart tient au nombre d’entités de
certaines catégories, non aux lignes ; il n’a pas été réparti catégorie par
catégorie.

Le même lecteur porte au classeur, colonnes U à Y de cet onglet, les financements
2026 de chaque ligne en milliers d’euros (subvention, investissement, transferts,
taxes affectées, total). Le total général y est de 73 288 271 k€, pour
73 288 275 708 € de financement public publiés par le jaune.

Il y porte aussi, colonnes Z à AB, l’économie de taxes affectées que le classeur
des taxes affectées (`PLF 2026_V&M tome I - Annexe 2`) chiffre pour chaque
bénéficiaire : à horizon d’un an, supplémentaire, totale. *Relevé au classeur le
20261112* : 14 365 847 k€ portés à l’onglet, dont 6 015 559 à un an ; neuf lignes
ont une économie non nulle. Le reste de l’économie de taxes affectées du classeur,
3,56 Md€, va à 39 bénéficiaires qui ne sont pas des opérateurs de l’onglet —
Action Logement, les chambres consulaires, les établissements publics fonciers
entre autres — et n’y est donc pas porté.

## 5. Comment le relevé se rejoue

Depuis le dépôt du site, avec `pdftotext` (paquet poppler) et le module Python
`pdfplumber` :

```bash
python3 outils/jaune.py --tsv <dossier>
```

écrit les trois fichiers dans `<dossier>` ;

```bash
python3 outils/jaune.py --classeur
```

réécrit les colonnes U à AB du classeur, sans toucher au reste du fichier ;

```bash
python3 outils/jaune.py
```

lit et contrôle sans rien écrire.

**Ce qui est fragile dans la lecture, et comment c’est tenu.** Les noms longs
débordent sur plusieurs lignes : un morceau est rattaché au nom qu’il prolonge par
confrontation aux noms des autres tableaux. Le tableau des emplois a des cases
vides : chaque nombre est rangé dans sa colonne par sa position sur la page, sur
les douze bords que donne la ligne de total. Les deux mécanismes sont éprouvés par
les totaux du § 2, non par une relecture à l’œil.
