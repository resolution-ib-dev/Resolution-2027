# Passation — 20261015

Elle remplace `methode/passation_20261009.md`, qui ne fait plus foi. Elle est
écrite pour qu'un fil de tête reprenne le chantier **sans relire aucune
conversation** : tout ce qui est utile est ici ou à l'adresse que cette pièce
nomme.

**Relevé sur `main` à `6384cff`, base de droit au millésime LEGI 20261013.**

---

## 1. Lire d'abord, dans cet ordre

1. `CLAUDE.md` — les instructions permanentes, **et sa table de ce qui fait foi
   par matière**, inscrite le 20261015 comme septième garde-fou. Elle se lit
   avant de produire quoi que ce soit.
2. `methode/carte_du_depot.md` — le geste d'ouverture en trois lignes, ce que
   porte chaque dossier, et les six questions courantes avec leur adresse.
3. La présente pièce.
4. `methode/registre_a_reconcilier_20261014.md` — ce qui reste à appliquer.

**Le geste d'ouverture, sans lequel rien n'est disponible :**

```
git clone --depth 1 https://github.com/resolution-ib-dev/Resolution-2027 depot
cp -r depot/chantier/. .
python3 depot/droit.py etat
```

**Un fil claude.ai/code n'accède pas au coffre.** Les pièces qu'il doit verser lui
sont jointes en fichier ou en zip. C'est la seule surface qui pousse ; un fil
Cowork lit le dépôt et ne pousse pas.

---

## 2. L'état des trois liasses

| liasse | amendements | numérotation |
|---|---:|---|
| `livrables/depot_2027/LIASSE_PLF_P1.md` | **34** | 1 à 34, continue |
| `livrables/depot_2027/LIASSE_PLF_P2.md` | **41** | 1 à 41, continue |
| `livrables/depot_2027/LIASSE_PLFSS.md` | **8** | 1 à 8, continue |

Deux états contrôlés et stables : la clause générale des niches du P1 n° 1, III
porte **350 rangs continus**, la liste des dissolutions du P2 n° 27, III en porte
**337**. Comptes vérifiés par un fil indépendant au versement du 15 octobre.

Elles ont traversé, depuis le 12 octobre : une passe qui a retiré les
proclamations et écrit une règle de défaut derrière chaque renvoi au décret, un
audit complet par un fil indépendant, la correction de ses quarante-neuf
constats, et les treize arbitrages de l'auteure.

**Quatre points restent ouverts sur les liasses**, et aucun ne se corrige sans
arbitrage :

- **Deux articles du code des impositions sur les biens et services, et non
  trois, sont abrogés en différé au 1er janvier 2027**, date même d'entrée en
  vigueur retenue. Le V du P1 n° 26 vise `L. 452-27`, `L. 422-26-1` et
  `L. 422-40` ; `L. 452-27` et `L. 422-40` sont à l'état `ABROGE_DIFF`,
  `L. 422-26-1` est en vigueur sans terme. **C'est le risque le plus sérieux.**
- Le critère de financement de **SNCF Réseau**, réservé à l'arbitrage 6 du
  20261014.
- La **seconde « Maison des adolescents »** : la source porte deux dénominations
  nues identiques et ne les distingue pas. Un seul rang est gardé.
- La **ligne ministérielle qui porte l'écart de deux emplois**, à vérifier contre
  l'article 63 du texte déposé. Les totaux corrigés — 1 990 894 et 2 002 052 —
  sont gardés.

**Deux points sont levés le 20261015** : l'accroche du P1 n° 26 est juste —
l'article 42 du texte n° 3210 s'intitule « Dispositions relatives à l'affectation
de ressources à des tiers » — et l'écart d'adresse `L. 422-15-1` contre
`L. 422-26-1` n'existait pas dans la liasse, mais dans le registre.

---

## 3. L'état de la trajectoire

**Recalculée intégralement le 20261015**, 27 lignes reconstruites depuis F, le
socle, le rythme et la fraction d'exercice. **Zéro écart ligne à ligne au-delà du
centième.** Les trois contrôles de somme passent.

| exercice | coupes | restitution | solde **en mesure** |
|---|---:|---:|---:|
| 2027 | 56,34 | 33,39 | **+22,95** |
| 2028 | 100,05 | 114,46 | **−14,41** |
| 2029 | 123,97 | 114,46 | **+9,51** |
| 2030 | 127,57 | 114,46 | **+13,11** |

Régime plein 127,57 + 8,30 hors périmètre = **135,87**, contre 135,9 au classeur.
Cumul 2027-2028 : **+8,55**.

**Mesure et caisse ne se confondent jamais.** Le solde ci-dessus est en mesure :
il ignore le CP résiduel, qui ne vit qu'au § 15 du registre et sur la seule part
État de 2027. Trois lectures du même exercice 2027 :

| lecture | 2027 |
|---|---:|
| en mesure, telle qu'affichée | **+22,95** |
| marge de prudence déduite (4,7) | **+18,25** |
| part État en caisse (16,34 au lieu de 27,45), le reste en mesure | **+11,84** |

**Le point dur est 2028, et il est de calendrier.** La restitution passe en régime
plein dès janvier quand les coupes sont à 100,05. Besoin de l'exercice : 11,45
une fois la TVA et la taxe sur les salaires comptées. **Deux leviers de date
suffisent** — TVA au 1er janvier 2028 et taxe sur les salaires décalée d'un an
donnent +14,87. La restitution ne s'étale pas, arbitrage du 20261009.

---

## 4. L'état des flux — ce qui existe, et le trou

Les trois axes — mesure, agent, temps — existent, **mais jamais ensemble**.

| pièce | mesure | agent | temps | portée |
|---|---|---|---|---|
| onglet `Flux` de `Synthèse Calculs` | oui | oui, nommé par transfert | non | année 1 et terme |
| onglet `CSG-CRDS` | non | niveau de salaire | mensuel | restitution seule |
| registre § 6 | non | oui, 8 agents | mensuel | **2027 seulement** |
| registre § 16 | par pan | non | trimestriel | 2027-2030 |
| `Suivi dépenses — crédits et vecteurs` | oui | non | dates d'échéance | crédits et vecteurs |
| `referentiels/table_passage_schema_prelevements_20260930.tsv` | 420 rangs | non | non | 24 lignes, 141 non rattachées |

**Le croisé mesure × agent × mois n'existe nulle part.** Cherché par nom et par
contenu dans tout le dépôt et dans les trois classeurs du projet. Il a été
fabriqué dans un fil et jamais versé : il est perdu. **C'est la pièce à refaire**,
et c'est l'étape 2 du plan.

**Le trimestriel par agent 2027 est acquis** — agrégation des douze mois du § 6,
sans paramètre neuf. Il se referme sur le trimestriel par pan à 0,06 près, et les
coupes portées par agent somment à 56,40 contre 56,34 au § 4.

| agent | T1 | T2 | T3 | T4 | 2027 |
|---|---:|---:|---:|---:|---:|
| Ménages actifs — transferts monétaires | −0,30 | −0,30 | +6,54 | +19,44 | **+25,38** |
| Ménages actifs — services en nature | −3,72 | −3,72 | −3,72 | −3,72 | **−14,88** |
| Ménages sans revenus d'activité | 0,00 | −0,63 | −0,90 | −0,90 | **−2,43** |
| Agents publics | 0,00 | 0,00 | −4,80 | −3,36 | **−8,16** |
| Entreprises | −3,18 | −3,18 | −3,78 | −3,78 | **−13,92** |
| Associations | 0,00 | 0,00 | −1,17 | −1,17 | **−2,34** |
| Opérateurs | 0,00 | 0,00 | −1,71 | −1,71 | **−3,42** |
| Collectivités | −0,81 | −0,81 | −0,81 | −0,81 | **−3,24** |
| **TOTAL** | **−8,01** | **−8,64** | **−10,35** | **+3,99** | **−23,01** |

**Les deux trous à ne jamais lisser dans une synthèse** : l'indemnité de départ
des agents publics, contrepartie de −8,16 et **non chiffrée** ; les ménages sans
revenus d'activité, **−2,43 sans aucune contrepartie**, que seul le socle protège.

---

## 5. L'état du tri des prélèvements

**Ce qui fait foi est `referentiels/prelevements_forces_20260930.tsv`, colonne
`rang`** — et non `sort_prelevements_20260930.tsv`, qui le contredit sur 179
rangs. Le vocabulaire des sorts est celui de l'onglet `Refonte fiscalité` de
`Synthèse Calculs Résolution`, qui est la doctrine de l'auteure.

**« Supprimé » n'est pas un sort.** Un prélèvement qui disparaît ne fait pas
disparaître son produit : il est repris, soit par l'impôt qui l'absorbe, soit par
les hausses d'équilibre des quatre impôts conservés.

| sort | rangs | rendement 2026 (M€) |
|---|---:|---:|
| conservé et absorbe | 4 | 457 710,6 |
| fondu par rattachement | 258 | 310 765,1 |
| fondu dans l'équilibre | 112 | 43 963,4 |
| maintenu à part | 43 | 62 649,3 |
| hors champ | 3 | 1 660,7 |
| **total** | **420** | **876 749,1** |

Les cotisations et contributions sociales sont suivies à part par une colonne
`nature` : impôt ou taxe 288 · cotisation sociale 83 · taxe sur la masse salariale
30 · contribution sociale 16 · hors champ 3.

**Deux défauts levés le 20261015** : 65 rangs classés « non rattachable » alors
qu'ils portaient un impôt principal, reclassés ; 21 rangs appartenant à quatre
lignes du schéma sans valeur en colonne « Taxes à supprimer » — assurances, taxe
de séjour, outre-mer, forfaits de cotisation — passés en maintenus.

**Trois défauts tiennent, et ils interdisent toute publication** : 188 rangs sur
420 sans rendement 2026 · 105 sièges juridiques non établis · 420 rangs relevés
contre 438 affichés au manifeste, écart non expliqué. S'y ajoute qu'aucune colonne
ne relie un rang à l'amendement qui le porte.

---

## 6. Les commissions du Jaune 2026

317 instances en vigueur · **6** supprimées depuis 2024 · **14 ministères** et la
Banque de France · 32,5 M€ de fonctionnement 2024 · 10 884 membres · 3 417
réunions. Le Jaune en annonce 318 : **l'écart d'une unité se tranche sur pièce et
ne se comble pas.**

Les deux valeurs corrigées le 20261015 — six supprimées et non sept, quatorze
rattachements et non quinze — sont portées au lisez-moi du référentiel, à la vue
consolidée et au registre des reprises sous C11. **L'onglet `Commissions —
synthèse` du classeur `Commissions_R_20261014.xlsx` porte encore les deux valeurs
fausses** et reste à reprendre.

Aucun double compte avec les opérateurs ni les ODAC-ODAL : les 317 libellés ont
été rapprochés un à un. Les commissions sont un bloc distinct des 1 104 agences
d'État = 434 opérateurs + 328 organismes hors PLF + 24 autorités indépendantes +
318 commissions.

---

## 7. Les dettes de versement

- **L'index n'est pas régénéré.** `make index` sort en échec avec trente-deux
  anomalies, dont vingt-trois sont exactement les pièces du versement du 15
  octobre, non déclarées. `make reindex` les lève.
- **Les cinq liasses du 12 octobre sont restées au dépôt** à côté des nouvelles :
  `LIASSE_P1.md`, `LIASSE_P1_20261008.md`, `LIASSE_P2_20261008.md`,
  `LIASSE_PLFSS_20261008.md`, `LIASSE_20261008.md`. Tant qu'elles y sont, le
  dépôt porte deux vérités.
- `methode/carte_des_domiciles_20261012.md` est périmée et se supprime du coffre
  et du dépôt.
- Le registre `livrables/registre_calcul_etatB.md` vit au dépôt : **Cowork n'y
  pousse pas**. Toute correction de valeur y passe d'abord, par un fil
  claude.ai/code, avant d'être portée à la vue consolidée.

---

## 8. Le plan, dans l'ordre

**1. Verser ce qui est en dette.** *Fil claude.ai/code.* Supprimer les cinq
liasses périmées et la carte des domiciles, verser les pièces corrigées du 15
octobre, puis `make reindex` et `make index`. Rien d'autre ne commence proprement
tant que le dépôt porte deux vérités.

**2. Construire l'axe agent 2027-2030.** *Fil Cowork.* C'est la pièce perdue, et
elle se refait sans paramètre neuf : la clé d'incidence du § 6 du registre
appliquée aux marches des §§ 5 et 16. Trois onglets — mesure × agent × trimestre,
le cumulé par agent, la contemporanéité étendue aux quatre exercices. Contrôles :
chaque trimestre se referme sur le trimestriel par pan, chaque année sur la
trajectoire. **Dire ce qui est posé et non mesuré** : la clé 90 / 10 entre ménages
actifs et agents publics.

**3. Lever les trois défauts du tri.** *Fil Cowork, parallélisable avec le 2* —
fichiers différents, aucun conflit. 188 rendements, 105 sièges, l'écart de 18 au
manifeste. Tant qu'ils tiennent, rien ne part au site.

**4. Le Sankey des flux.** *Après le 3.* Les 141 rangs non rattachés à une ligne
de schéma sont exactement ce qui l'empêche aujourd'hui.

**5. Le compteur par agent économique, en vue publiable.** *Après le 2.* C'est la
pièce qui répond à « qui paie, qui reçoit, quand », et la seule qui tienne debout
devant un contradicteur.

---

## 9. Ce qui est posé et non mesuré

À ne jamais présenter comme établi : la clé de restitution 90 / 10 entre ménages
actifs et agents publics · le socle à 15 % de la ligne D43, borne « 10 à 20 % » au
classeur et non arrêtée · la ventilation de la TVA par marche, règle statique sans
effet de comportement qui sous-estime 2028 · l'écart d'une unité au nombre de
commissions · les quatre sièges d'audiovisuel, de confiance moyenne tant que la
loi n° 86-1067 du 30 septembre 1986 n'est pas dans la base de droit.
