# Arbitrage — quelle correction de `lire_structure` fait foi, 20261008, **clos le 20261009**

**Décision prise en propre par le fil de reprise**, la question étant d'appareil et non de fond.

## La situation

Deux corrections concurrentes du même défaut — la chaîne hiérarchique absente des articles extraits
de LEGI :

| branche | méthode | état |
|---|---|---|
| **fusionnée le 20261008** (`claude/inspiring-turing-2d9ovs`, dans `main` par `05d77d1`) | lit la chaîne au **`CONTEXTE` du fichier de section**, sur la version de titre en vigueur, et fait taire les fichiers d'article | fondée sur la forme réelle d'une livraison DILA relevée pour l'occasion, mesurée à l'essai |
| `claude/eager-euler-qpqxy9` (20261007) | reconstruit la chaîne en remontant l'arborescence LEGI | hors de `main`, aucune mesure de couverture rendue |

## La décision, et elle est désormais close

**La correction fusionnée fait foi, et la question ne se rouvre pas.** Elle n'est plus seulement
mesurée à l'essai : **elle est en production et mesurée sur la livraison réelle.**

**Mesure du 20261009, sur `data/` au millésime LEGI 20261007** — extraction déclenchée par la fusion,
commit `2e0758c` :

| ensemble | articles portant leur chaîne | couverture |
|---|---:|---:|
| **code général des impôts** | 3 484 / 3 484 | **100 %** |
| **code des impositions sur les biens et services** | toutes | **100 %** |
| **tous codes et textes confondus** | 160 952 / 165 098 | **97,5 %** |
| codes complets à 100 % | 23 sur 74 ensembles | — |

**Les deux codes que le regroupement des abrogations vise sont servis en entier.** La confrontation
des deux méthodes, prévue comme un fil, **n'a plus d'objet** : une méthode qui rend 100 % sur les
deux codes utiles ne se départage pas d'une autre par une mesure. **Le fil de confrontation ne
s'ouvre pas** ; la branche concurrente reste comme trace et ne se fusionne pas.

## Ce que la mesure fait apparaître, et qui n'était pas demandé

**Les 2,5 % sans chaîne sont, pour l'essentiel, des textes non codifiés** — lois de finances
anciennes, LOLF, ordonnances : ils n'ont pas de structure de sections à lire, et le défaut n'en est
pas un.

**Trois ensembles font exception et sont des codes** : code du tourisme (711 articles), code des
postes et communications électroniques (789) et le recueil `tva2025` (1 066), tous **à 0 %**.
**Sans effet sur le dépôt 2027** — aucune pièce ne les vise —, **mais à vérifier** avant de
s'appuyer sur la chaîne hors du champ fiscal.

## Une conséquence qui n'est pas d'appareil

Le dépôt de droit est passé du **millésime LEGI 20261001 au 20261007**. Les **2 844 adresses** de la
liasse ont été contrôlées sur l'ancien. **Le recontrôle d'adresses au nouveau millésime est dû avant
tout dépôt réel** ; il est mécanique et se rejoue d'un geste.
