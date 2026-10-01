# Doctrine Résolution — corpus pour lecteur assisté

**Ce paquet sert à s'approprier un point du projet en détail.** Il n'est pas
fait pour être lu d'un bout à l'autre : il est fait pour qu'on lui pose une
question et qu'il y réponde avec ses pièces.

**Deux choses à faire avant tout le reste.**

1. Lire `00_REGLES_DE_LECTURE.md`. Il dit ce qu'un chiffre vaut, ce qu'un contrôle
   prouve, et ce qu'on a le droit d'en tirer. **Sans lui, le corpus se lit de
   travers** — un lecteur qui l'ignore comblera les trous tout seul.
2. Ne pas tout charger. `2_chiffres_socle_budgetaire.json` pèse à lui seul
   3,9 Mo. On l'ouvre sur une question précise, pas par principe.

---

## Par où entrer, selon la question posée

| la question | où aller |
|---|---|
| « qu'est-ce que le projet propose sur X ? » | `1_enonce_M-nnn` — 71 énoncés, un par mesure, verbe, objet, paramètres |
| « pourquoi, et sur quel argument ? » | `1_doctrine_REF_doctrine.json`, puis le passage du manuscrit qu'il désigne |
| « qu'est-ce que le texte dit exactement ? » | `1_doctrine_manuscrit.html` — **c'est la Vérité du projet**, tout le reste en dérive |
| « d'où sort ce montant ? » | `2_chiffres_REF_chiffres.json` d'abord — source et niveau de confiance ; puis `2_chiffres_socle_budgetaire.json` pour remonter à la ligne du document budgétaire |
| « par quelle norme ça passe ? » | les fichiers `3_juridique_` — transposabilité, texte de révision, présentation |
| « qu'est-ce qui n'est pas tranché ? » | les entrées du référentiel des chiffres à confiance nulle, et les écarts déclarés au fil des pièces |

---

## Ce qu'il y a dedans

### Bloc 1 — le manuscrit et sa lecture

| pièce | ce qu'elle est |
|---|---|
| `1_doctrine_manuscrit.html` | le texte du projet. **Point de vérité.** |
| `1_doctrine_texte_livre.json` | le même texte, découpé pour citation exacte |
| `1_doctrine_REF_doctrine.json` | la doctrine formalisée : chaque proposition, son effet, ses paramètres, ses ancrages au manuscrit |
| `1_doctrine_notes_manuscrit.json` | les 141 notes de fin, dont 37 portent un chiffre |
| `1_doctrine_positions.json` | les positions dérivées de la doctrine, 56 catégories, 294 lignes |
| `1_enonce_M-001` à `M-071` | les 71 mesures en langage naturel — **M-001 à M-071, sans trou** |

*Un énoncé marqué `direction` donne une direction sans dispositif. Il ne se
complète pas : le compléter reviendrait à inventer la mesure.*

### Bloc 2 — la traçabilité des montants

| pièce | ce qu'elle est |
|---|---|
| `2_chiffres_REF_chiffres.json` | 257 chiffres du corpus, chacun avec sa valeur, son unité, son millésime, sa source et son **niveau de confiance de 0 à 3**. 93 sont déclarés sans source : ils ne sortent dans aucun livrable diffusable. |
| `2_chiffres_socle_budgetaire.json` | la lecture formalisée des cinq classeurs budgétaires en un seul objet — 278 taxes affectées, 465 dépenses fiscales et leurs 8 feuilles d'enrichissement, 180 opérateurs, 749 ODAC-ODAL, 128 programmes, 2 351 lignes de projet annuel de performance, 1 405 de rapport annuel, et l'arbre des économies |
| `2_chiffres_reconciliation_operateurs.json` | le rapprochement des opérateurs entre leurs quatre canaux de financement |

**Le socle sépare deux couches dans chaque entrée**, et elles ne se mélangent
pas : `socle` est ce que le document budgétaire publie — un bénéficiaire, un
montant, une référence juridique ; `interpretation` est ce que l'auteur a
ajouté — le régime retenu et les montants qui en découlent. La première ne se
discute pas, la seconde se discute.

**Deux limites déclarées, à ne pas franchir.** La subvention aux opérateurs
n'est connue qu'à la maille du programme, et trente programmes sur cinquante-
quatre portent plus d'un opérateur : pour ceux-là le montant n'est pas
imputable à l'opérateur. Et la part budgétaire de deux économies — France
Compétences et le CNC — n'est écrite nulle part : elle ne se déduit pas par
soustraction.

### Bloc 3 — par quelle norme ça passe

Texte de révision constitutionnelle consolidé, en version modificative et en
version de substitution ; récapitulatif de transposabilité ; recensement des
innovations ; présentation ; Constitution en trois colonnes.

---

## Ce qui n'est pas dedans, et pourquoi

L'outillage, les grilles de lecture des classeurs, la méthode de travail et
l'appareil de contrôle. Ils servent à produire le corpus, pas à s'en servir.

Les classeurs sources eux-mêmes : ils sont lus dans `socle_budgetaire.json`, et
la lecture est contrôlée — dix-sept bouclages recomposent leurs totaux depuis
leurs lignes.

---

---

## Les noms des fichiers portent leur bloc, et c'est voulu

**Ce paquet se lit aussi bien à plat qu'en arborescence.** Si tu déposes les
fichiers dans une conversation, les dossiers disparaissent et il ne reste que
les noms : ils sont donc préfixés par leur bloc, et **aucun n'est en double**.
L'ordre alphabétique remet le paquet dans son ordre de lecture.

| préfixe | bloc |
|---|---|
| `00_` | à lire en premier — cet index et les règles de lecture |
| `1_doctrine_` | le manuscrit et sa lecture formalisée |
| `1_enonce_M-nnn` | les 71 mesures, une par fichier |
| `1_enonces_00_` | la règle de lecture des énoncés |
| `2_chiffres_` | la traçabilité des montants |
| `3_juridique_` | par quelle norme ça passe |

---

## Manifeste des fichiers

| fichier | octets | sha256 (16) |
|---|---|---|
| `00_REGLES_DE_LECTURE.md` | 6 108 | `b0c4a4cf9f399ffc` |
| `1_doctrine_REF_doctrine.json` | 348 132 | `8beb2e0fd63ba268` |
| `1_doctrine_manuscrit.html` | 224 422 | `5ec342cb49dd0157` |
| `1_doctrine_notes_manuscrit.json` | 59 142 | `a6a07a73468b939e` |
| `1_doctrine_positions.json` | 242 572 | `b159cb9ee7462691` |
| `1_doctrine_texte_livre.json` | 311 829 | `2d3854998e6b01d3` |
| `1_enonce_M-001.md` | 639 | `c1a2e479640b7f61` |
| `1_enonces_00_regle_de_lecture.md` | 1 890 | `9f1ffc300f578a9d` |
| `2_chiffres_REF_chiffres.json` | 284 536 | `493c467cdc51e4f8` |
| `2_chiffres_reconciliation_operateurs.json` | 190 967 | `91fa3adf50192628` |
| `2_chiffres_socle_budgetaire.json` | 3 920 086 | `fefef4386e9190a8` |
| `3_juridique_Constitution_3colonnes_v46.html` | 104 362 | `80de491474511d12` |
| `3_juridique_PPLC_modificative_v7.md` | 35 863 | `fcdb19bd0ba23b0a` |
| `3_juridique_PPLC_substitution_v7.md` | 46 402 | `1370a27f3e41de80` |
| `3_juridique_innovations_v3.md` | 22 950 | `3743cdd59bb64082` |
| `3_juridique_presentation_v47.md` | 60 528 | `d486b7dcf14b2050` |
| `3_juridique_transposabilite_v8.md` | 41 770 | `2e44b435acd7b7b6` |
| `1_enonce_M-002.md` … `1_enonce_M-071.md` | 70 fichiers | — |

*Corpus arrêté au 20260917. Le manuscrit restauré est prouvé à l'octet : le
relevé de ses notes rejoué sur ce fichier redonne `notes_manuscrit.json`
identique, empreinte `a6a07a73468b939e`.*
