# Audit du coffre « Résolution » — mesure, classement, plan de nettoyage

**Mandat** : audit. Aucun document n'a été supprimé, ni au coffre ni au dépôt ; aucun `project_delete`, aucun `project_write` n'a été joué.
**Date** : 20261014. **Clone rafraîchi** : `/home/claude/chk2`, `origin/main` au commit `a7ed0a0` du 2026-10-14 16:23 UTC (« droit : millésime LEGI 20261013 »).

---

## 1. Mesure

| grandeur | valeur |
|---|---:|
| documents au coffre | **242** |
| taille déclarée du coffre (`knowledge_size`) | **1 827 387 o** sur 2 000 000 |
| documents trouvés au dépôt au même chemin sous `chantier/` | **240** |
| documents absents du dépôt | **2** |
| poids au dépôt des 240 pièces retrouvées | **5 016 842 o** (≈ 4 899 ko) |

### 1.1 Un écart de mesure à inscrire, et il commande la façon de lire les gains

Les 240 pièces retrouvées pèsent **5 016 842 o au dépôt**, quand le coffre entier en déclare **1 827 387**. L'écart n'est pas une différence de contenu : la pièce la plus lourde, `methode/arbitrages.md`, pèse **470 385 o au coffre** et **471 258 o au dépôt** — mesure prise des deux côtés. Sept pièces suffisent déjà à dépasser 1,4 Mo au dépôt ; les 233 autres ne tiendraient pas dans les 380 ko restants.

**Conséquence** : `knowledge_size` n'est pas la somme des octets des documents, et **l'API du projet n'expose pas le poids d'un document pris isolément**. Le seul poids mesurable pièce par pièce est celui du dépôt, et c'est celui que le mandat demande. **Les gains du plan ci-dessous sont donc donnés en kilooctets au dépôt — grandeur mesurée — accompagnés d'une estimation proportionnelle du gain au coffre, explicitement marquée comme estimation.** Aucun poids de coffre n'est inventé.

### 1.2 Comment la divergence a été mesurée

Peser 242 pièces au coffre supposait de les ouvrir une à une, au prix d'une lecture intégrale du corpus. La mesure retenue est une **datation croisée** : pour chaque pièce, la date du dernier commit du fichier au dépôt est comparée à la date de création de la pièce au coffre.

- **239 pièces sur 240** ont au dépôt un commit **daté à la date de création au coffre ou après**. Le dépôt porte donc au moins la version du coffre.
- **1 pièce** fait exception à la date : `methode/adressage.md`, créée au coffre le 20261014 et commitée au dépôt le 20261013. **Vérification faite au contenu** : la version du dépôt porte le même en-tête (« Inscrit le 20261013 »), la même règle de prévalence et le même § 5. L'écart d'un jour est un simple reversement au coffre, non une divergence.

**Limite de la méthode, inscrite** : la date de création d'un document du coffre ne dit pas s'il a été réécrit depuis. La datation est donc un indice fort de non-perte, non une identité à l'octet.

**Pièces lues au verbatim : 10.** `methode/arbitrages.md` · `methode/index.json` · `livrables/depot_2027/clause_generale_niches_20261005.md` · `methode/etats/NUIT_3A_exposes_20261008.md` · `methode/etats/CALENDRIER_20261007.md` · `methode/etats/L1.md` · `livrables/depot_2027/P1/4_4_taxe_fonciere_unique.md` · `appareil/versement.py` · `methode/etats/APP_fiscal.md` · `methode/adressage.md`.

**Un seul diff joué octet à octet**, sur `methode/arbitrages.md` : **le dépôt est en avance de 15 lignes sur le coffre** — une ligne corrigée au § du millésime de l'annexe 3, et l'arbitrage « 20261009 — site-publier-desactive » que le coffre ne porte pas. **La divergence est en faveur du dépôt : il n'y a rien à verser, et la suppression au coffre ne perd rien.**

---

## 2. Classement par famille

| famille | pièces | poids au dépôt |
|---|---:|---:|
| **au dépôt, identique** | **233** | 4 346 ko |
| **au dépôt, divergent** | **1** | 460 ko |
| **au coffre seul** | **2** | — |
| **à garder au coffre quoi qu'il arrive** | **6** | 93 ko |
| **total** | **242** | |

La table nominative des 242 pièces, avec leur poids, leur présence au dépôt et leur motif, est à `/home/claude/menage/coffre.tsv`.

### 2.1 Au dépôt, divergent — une seule pièce

`methode/arbitrages.md` — 471 258 o au dépôt, 470 385 o au coffre. **Le dépôt est en avance.** Le coffre fait foi sur les pièces de méthode, mais la règle n'a pas d'objet ici : la version du coffre est strictement contenue dans celle du dépôt, à la ligne corrigée près. **Aucun versement dû.**

### 2.2 Au coffre seul — deux pièces, à verser avant toute suppression

| pièce | pourquoi elle n'est pas au dépôt |
|---|---|
| `methode/registre_a_reconcilier_20261014.md` | créée au coffre le 20261014, postérieure au dernier commit utile ; jamais versée |
| `methode/fragments/arbitrages/20261009-tirage-p1-support-revue.md` | fragment d'arbitrage du 20261009 oublié au versement du lot ; ses dix-neuf frères du même jour sont au dépôt |

**Périmètre de l'absence, nommé** : absentes **du dépôt `resolution-ib-dev/Resolution-2027`, branche `main`, au chemin `chantier/<chemin de coffre>`**, au commit `a7ed0a0`. Elles sont au coffre, et elles n'ont été cherchées nulle part ailleurs.

### 2.3 À garder au coffre quoi qu'il arrive — six pièces, 93 ko au dépôt

Le critère est celui du mandat, et il se déduit de `methode/adressage.md` elle-même : le geste d'ouverture d'un fil est un **clone du dépôt**. Tout ce qui vit au dépôt est donc atteignable sans le coffre — **sauf ce qu'un fil doit lire pour savoir qu'il faut cloner, et pour savoir ce qu'il doit faire une fois cloné.** C'est exactement ce noyau.

| pièce | poids au dépôt | pourquoi elle reste |
|---|---:|---|
| `CLAUDE.md` | 25 487 o | instructions d'ouverture de session ; lues avant tout geste, donc avant tout clone |
| `methode/adressage.md` | 3 703 o | porte le geste d'ouverture en trois lignes, la règle de prévalence coffre/dépôt et la règle d'absence ; sans elle, aucun fil ne sait qu'il doit cloner |
| `methode/appui_des_passes.md` | 20 498 o | règles R-G, R-H, R-I et R8, citées en appui par la quasi-totalité des mandats du corpus |
| `methode/a_trancher.md` | 32 692 o | arbitrages ouverts en attente de l'auteure ; se lit à l'ouverture de tout fil de méthode |
| `methode/etats/SUIVI_chantier_20261009.md` | 6 370 o | état d'avancement du chantier ; répond à « où en est-on » sans rien déplier |
| `methode/passation_20261009.md` | 6 239 o | dernière passation ; les quatre précédentes sont caduques (§ 3) |

**Ce noyau est aussi au dépôt** : il n'est pas gardé parce qu'il serait irrécupérable, mais parce qu'il doit être lisible **avant** le clone.

---

## 3. Redondances internes au coffre

C'est le plus gros gisement, et il ne se voit pas en comparant au dépôt : ces pièces sont toutes au dépôt, mais elles sont surtout **redondantes entre elles**.

| # | gisement | pièces | poids au dépôt | ce qui fait redondance |
|---|---|---:|---:|---|
| 1 | **`methode/etats/` — les états journaliers** | **78** | **1 513 996 o** (1 478 ko, **30 % du corpus mesuré**) | une série d'états dont seul le dernier sert. Détail ci-dessous |
| 1a | — dont `etats/NUIT_*` | 14 | 550 728 o | **quatorze états pour une seule nuit, celle du 20261008** : `NUIT_1A`, `1B`, `1C`, `2`, `2bis`, `3A`, `3B`, `3ter`, `4`, `5_6`, `7`, `8`, `9`, `10`. Chacun rend la mesure de sortie de la phase précédente ; `NUIT_10` les résout toutes |
| 1b | — dont les états de lots à lettres | 31 | 270 886 o | `L1` à `L19`, `N1` à `N7b`, `S1` à `S3`, `T1` à `T3`, `U1` à `U7`, `V1`, `V2` : états de lots clos, dont les arbitrages sont inscrits à `arbitrages.md` et dont les renvois sont périmés par deux renumérotations successives du III (20261007, puis 20261009) |
| 1c | — dont `etats/APP_*` | 11 | 194 050 o | onze états d'application d'une même vague de corrections du 20261007, tous résolus par `application_corrections_20261007.md` et par les pièces elles-mêmes |
| 2 | **`livrables/depot_2027/` — les pièces de liasse** | **63** | **1 340 888 o** (1 309 ko, **27 %**) | ce n'est pas une redondance interne mais un **doublon pur du dépôt** : le livrable y vit en entier, au même chemin. Le coffre en porte une copie de travail |
| 3 | **Les passations et les procédures empilées** | **10** | **136 842 o** | cinq passations — `20261005`, `20261007`, `20261008`, `relecture_export_20261008`, `20261009` — dont **seule la dernière fait foi**, chacune rendant la précédente caduque ; cinq procédures — `liasse_P1`, `nuit`, `revue_fond`, `fin_de_chantier`, `contre_plf` — dont trois portent sur des phases closes |

**Une redondance déclarée par le corpus lui-même, et c'est la plus propre à traiter.** `methode/adressage.md`, inscrite le 20261013, dit en tête qu'elle **remplace** les règles d'adresse de `methode/carte_des_domiciles_20261012.md` (3 755 o), du bloc « Ouverture de session » de `CLAUDE.md` et de `methode/gestion_depot_projet.md` (3 529 o), « qui disaient la même chose en trois endroits et en trois grammaires ». Les deux pièces remplacées sont toujours au coffre.

**Quatre comptes rendus** (`cr_fil1`, `cr_couverture_cgi_expert`, `cr_consolidation`, `cr_fil_de_tete`, 49 411 o) et **vingt et un fragments** d'arbitrage et de journal (73 649 o) relèvent du même régime : le fragment est un intermédiaire, son contenu est fondu dans `arbitrages.md` ou `journal.md` par `appareil/fragments.py`.

---

## 4. Plan de nettoyage en trois paliers

### Palier 1 — se supprime tout de suite, sans rien verser

**234 pièces · 4 921 853 o au dépôt (4 806 ko) · 98,1 % du corpus mesuré · gain estimé au coffre ≈ 1 750 ko**

Toutes les pièces du coffre **sauf** le noyau de six (palier 3) et les deux pièces non versées (palier 2). Chacune est au dépôt au même chemin sous `chantier/`, dans une version datée à la création au coffre ou après. **`methode/arbitrages.md` est dans ce palier** : son unique divergence est en faveur du dépôt.

**Risque : faible, et il est nommé.** Le risque n'est pas la perte — un clone les restitue toutes — mais **la friction** : chaque pièce supprimée devient inatteignable sans clone, et un fil qui n'a pas joué le geste d'ouverture ne la trouve plus. `methode/adressage.md`, conservée, est ce qui ramène ce risque à son minimum : elle porte le geste et la règle d'absence.

**Risque résiduel mesuré** : la datation est un indice, pas une identité à l'octet. **Levée proposée, non jouée** : rejouer `appareil/versement.py verifier` — il est écrit pour cela et rend, empreinte SHA-256 à l'appui, la liste des documents du projet dont la copie au dépôt est **identique**. Ce contrôle convertirait les 233 « identiques par datation » en identiques prouvées, avant toute suppression.

La liste nominative des 234 pièces est à `/home/claude/menage/coffre.tsv`, familles `au depot, identique` et `au depot, divergent`.

### Palier 2 — se supprime après versement au dépôt

**2 pièces · poids au dépôt : sans objet, elles n'y sont pas**

À verser, nommément :

1. `methode/registre_a_reconcilier_20261014.md` → `chantier/methode/registre_a_reconcilier_20261014.md`
2. `methode/fragments/arbitrages/20261009-tirage-p1-support-revue.md` → `chantier/methode/fragments/arbitrages/20261009-tirage-p1-support-revue.md`

**Le versement se joue d'une session claude.ai/code**, pas d'ici : `methode/adressage.md`, § 6, un fil Cowork lit le dépôt et ne pousse pas. **Risque : réel tant que le versement n'est pas fait** — ce sont les deux seules pièces du coffre dont la suppression perdrait le contenu. Une fois versées et l'empreinte contrôlée, elles rejoignent le palier 1.

### Palier 3 — ne se supprime pas

**6 pièces · 94 989 o au dépôt (93 ko) · gain nul, et c'est voulu · ≈ 34 ko estimés au coffre**

`CLAUDE.md` · `methode/adressage.md` · `methode/appui_des_passes.md` · `methode/a_trancher.md` · `methode/etats/SUIVI_chantier_20261009.md` · `methode/passation_20261009.md`.

**Pourquoi** : ce sont les six pièces qu'un fil doit lire **avant** d'avoir cloné quoi que ce soit — ce qui lui dit de cloner, comment adresser ce qu'il trouve, quelles règles de passe tenir, ce qui est en attente d'arbitrage, où en est le chantier et d'où il reprend. Les supprimer ne gagnerait que 2 % du coffre et coûterait l'ouverture de session.

### Récapitulation

| palier | pièces | gain mesuré au dépôt | gain estimé au coffre | risque |
|---|---:|---:|---:|---|
| 1 — suppression immédiate | 234 | 4 806 ko | ≈ 1 750 ko | faible — friction, non perte ; levée par `versement.py verifier` |
| 2 — versement puis suppression | 2 | — | marginal | réel avant versement : seules pièces non récupérables |
| 3 — conservation | 6 | 0 | 0 (≈ 34 ko conservés) | — |

**Après exécution des paliers 1 et 2, le coffre retomberait à l'ordre de 40 à 80 ko pour 6 à 8 documents**, contre 1 824 ko pour 242 — ordre de grandeur estimé à partir de la part du noyau dans le corpus mesuré, non une mesure.

---

## 5. Ce que cet audit n'a pas fait

- **Aucune suppression**, aucun `project_delete`, aucun `project_write`.
- **Aucun versement** : les deux pièces du palier 2 restent au coffre seul.
- **232 pièces sur 242 n'ont pas été ouvertes** : leur classement repose sur la datation croisée, dont la limite est inscrite au § 1.2.
- **Aucun poids de coffre n'a été mesuré pièce par pièce** : l'API ne l'expose pas, et aucun n'a été inventé.
- **Le contrôle d'empreinte de `appareil/versement.py verifier` n'a pas été joué** : il suppose un manifeste de versement que le mandat ne nomme pas.
