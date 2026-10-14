# Carte des domiciles — où la matière vit, 20261012

**À quoi sert cette pièce** : répondre en trente secondes à « où est-ce que je cherche ».
Elle s’ouvre avant toute recherche de matière, au titre de R-X.

## Les trois surfaces

| surface | ce que c’est | ce qu’elle peut faire |
|---|---|---|
| **coffre** | le projet Claude « Résolution », outil `Projects` | lecture et écriture depuis un fil Cowork ou un fil de conversation ; **un fil claude.ai/code n’y accède pas**. Porte aussi les classeurs sources en pièces jointes |
| **dépôt** | `resolution-ib-dev/Resolution-2027`, branche `main`, **public** | lecture par clone sans jeton, depuis Cowork comme depuis code ; **le push exige claude.ai/code** |
| **atelier** | le shell d’un fil Cowork | porte un clone du dépôt, joue les scripts et les `make`, calcule ; **rien n’y persiste d’un fil à l’autre** |

Clone : `git clone --depth 1 https://github.com/resolution-ib-dev/Resolution-2027 depot`

## La table

| matière | adresse | surface | qui fait foi |
|---|---|---|---|
| **le livre EP3 et son index** | `chantier/livre/` — 2 pièces, 316 Ko ; `texte_livre.json` porte les 180 folios et 192 143 caractères | **dépôt seul** | dépôt |
| **les notes du manuscrit** | `chantier/referentiels/notes_manuscrit.json` | **dépôt seul** | dépôt |
| **la doctrine et les référentiels** | `chantier/referentiels/` — 31 pièces, 6,2 Mo : `REF_doctrine.json`, socles 2027, `redaction_*.json`, niches et sièges, `cgi_expert_*` | **dépôt seul** | dépôt |
| **le droit en vigueur** | `data/` — 75 fichiers, 41 Mo, millésime LEGI 20261007 ; lu par `droit.py` à la racine du dépôt | **dépôt seul** | dépôt |
| **les sources PDF** | `chantier/sources/` — 4 pièces, 14 Mo : guide de légistique, guide budgétaire, deux projets de loi | **dépôt seul** | dépôt |
| **les pièces de référence et les guides** | `chantier/reference/` — 19 pièces, 688 Ko | dépôt ; **2 au coffre** (`reference/guide_legistique.md`, `reference/regles_credits.md`) | **coffre** pour ces deux, **dépôt** pour les 17 autres |
| **la méthode, les états, les fragments** | `chantier/methode/` — 268 pièces au dépôt, dont 77 états et 91 fragments | coffre **et** dépôt | **coffre** — le dépôt est en retard, dernier versement 20261011 |
| **les livrables et les registres** | `chantier/livrables/` — 208 pièces au dépôt | coffre **et** dépôt | **coffre** — même retard |
| **l’appareil, scripts et `make`** | `chantier/appareil/` — 120 pièces au dépôt ; `Makefile` et `MANIFESTE.md` à la racine du chantier | coffre **et** dépôt | **dépôt** pour la chaîne complète et les `make` ; **coffre** pour les scripts de fil versés depuis le 20261009 |
| **les paquets de machine** | `chantier/paquet/` — 22 pièces au dépôt | coffre **et** dépôt | **coffre** |
| **les classeurs sources** | pièces jointes du projet — 9 classeurs `.xls` et `.xlsx` | **coffre seul** — le `.gitignore` du chantier les exclut | coffre |
| **le dossier de démarrage** | `chantier/racine/DEMARRAGE.md`, `chantier/input/`, `chantier/archive/` | **dépôt seul** | dépôt |
| **la table des codes** | `codes.json`, racine du dépôt | dépôt, **synchronisé au coffre** | dépôt |

## Les trois réflexes

1. **On cherche aux deux surfaces.** Le livre, les notes du manuscrit, les référentiels et le
droit vivent au dépôt et nulle part ailleurs — R-X.
2. **Une absence se dit avec son périmètre.** « Absent du coffre » n’est pas « absent du
projet » — R-Y.
3. **Sur une pièce qui existe aux deux, le clone peut être en retard.** Méthode, livrables et
paquets se relisent au coffre avant d’être contrôlés — R-Z.
