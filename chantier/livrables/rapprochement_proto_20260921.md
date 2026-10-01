# Rapprochement du proto Données à la doctrine — 20260921

*Lecture. Aucun classeur ouvert, aucun sourçage, aucune valeur neuve, aucun recalcul.
Aucune valeur du proto corrigée, aucune valeur du corpus remise en cause. Le manuscrit
et la doctrine font foi ; le proto est antérieur — il vient de `Données_Résolution_0112.docx` —
et là où les deux divergent, c'est lui qui est périmé.*

> **Règle énoncée par l'auteur le 20260921, et elle commande tout ce document :**
> **le livre et ses annexes prévalent.** Les deux contradictions relevées ci-dessous sont
> closes par elle. L'une est écrite au référentiel sous forme d'arbitrage ; l'autre ne peut
> pas encore l'être, et on dit pourquoi.

## Le compte

**93 candidats instruits — concordant 8 · contradictoire 2 · divergence d'hypothèse 5 · sans vis-à-vis 78.**
Six candidats avaient déjà un rapprochement écrit ; les 87 autres étaient non instruits, et le sont.

## L'état reçu, et il est mesuré

`referentiels/REF_chiffres.json` est hors coffre. Il a été régénéré par
`appareil/generer_ref_chiffres.py` sur le manuscrit restauré du coffre, le `REF_doctrine` du
dépôt et le proto restauré : **257 entrées, dont 93 sans source, `0 échec` au contrôle**, 57
calculs rejoués justes, 25 faits rapprochés sur 53 entrées. C'est le compte que ce fil attendait.

Le manuscrit est prouvé de l'extérieur : `extraire_notes.py` rejoué dessus rend
`referentiels/notes_manuscrit.json` **identique à l'octet**.

**État après le rapprochement, mesuré** : la table `MEME_QUE` passe de 25 à 26 groupes et de
53 à 57 entrées rapprochées, **`0 échec`** au contrôle, 2 discordances arbitrées et aucune
discordance de valeur. Le patch est éprouvé, il est au paquet de dépôt
`methode/paquet_depot_rapprochement_20260921.md`, et **il n'est pas poussé d'ici**.

## Les cases

| case | ce qu'elle veut dire | compte |
|---|---|---|
| `concordant` | le corpus porte le même fait, même valeur | 8 |
| `contradictoire` | le corpus porte le même fait, autre valeur | 2 |
| `divergence d'hypothèse` | même fait, valeurs compatibles, hypothèses qui s'excluent | 5 |
| `sans vis-à-vis` | le corpus ne porte pas ce fait — c'est du contexte, et il se conserve | 78 |

**Une part des `sans vis-à-vis` ne porte aucune grandeur** : un millésime, un ordinal de
décile, un fragment d'adresse web, un en-tête de tableau, une note de lecture. Ce sont les faux
positifs du relevé mécanique de `generer_ref_chiffres.py`, déclarés comme tels et non
requalifiés ici — c'est la question 32, déjà ouverte, transposée du côté du proto.

## La table

Une ligne par candidat : identifiant, valeur, rubrique, fait nommé, case, entrée du corpus en vis-à-vis, remarque.

| entrée | valeur | rubrique | fait | case | vis-à-vis | remarque |
|---|---|---|---|---|---|---|
| `P-D-100` | +1,4 % | Perdants | effet inflationniste subi par un consommateur adulte, à un an | `concordant` | R-D3-2-1-e4 | Rapprochement déjà écrit. Tête décalée : le proto porte +1,4 %, le REF −21 Md€/an. La concordance se lit sur la déclinaison commune, 30 €/mois. Le proto annualise à 360 €/an quand le REF porte 357 €/an — arrondi du mois à l'année, relevé et non tranché. |
| `P-D-101` | environ 20 | Perdants | complément de retraite annuel tiré du patrimoine restitué | `divergence d'hypothèse` | N-e119-1 · R-D7-2-2-p1 · R-D7-2-2-e1 | Reprise telle quelle du relevé du 20260921. Le proto calcule 950 €/an par retraité sur douze ans — demi-espérance de vie à la retraite — sur 160 Md€ affectés aux retraités ; la note e119 pose 3 % de rendement net sur vingt-quatre ans pour « au moins 500 € par an ». Les deux hypothèses de durée s'excluent. |
| `P-D-102` | 9 % | Perdants | postes publics facultatifs supprimés la première année | `contradictoire` | R-D6-2-1-p1 · R-D6-2-1-e1 | Reprise telle quelle. Le proto porte 540 000 agents et 9 % des effectifs ; le manuscrit porte « environ 580 000 postes » et « une baisse de 10 % des effectifs publics totaux », repris en R-D6-2-1-p1 et R-D6-2-1-e1. **Arbitrée par l'auteur le 20260921** — le livre et ses annexes prévalent, le proto est périmé — et écrite au groupe `postes publics facultatifs supprimés` : la discordance se range en décision et reste visible. La perte sèche de 30 % concorde, elle, avec les 70 % de traitement maintenus de la note e93 et de R-D6-2-2-p1. |
| `P-D-103` | 3,3 millions | Perdants | nombre de chômeurs de catégorie A | `sans vis-à-vis` | — | Le corpus ne dénombre pas les chômeurs. La déclinaison +13 % est celle de la restitution, portée ailleurs ; elle n'est pas le fait de cette entrée. |
| `P-D-104` | 1,5 | Perdants | ménages du parc social dont le bail s'éteint la première année | `sans vis-à-vis` | — | Le tiers le plus aisé, 1,5 million de ménages, n'est pas un ensemble que le corpus dénombre. Le manuscrit compte « un locataire du parc social sur dix » au-dessus des plafonds, soit environ un demi-million : autre critère, autre population, et ce n'est pas une contradiction. Les déclinaisons, elles, ont un vis-à-vis : 180 €/mois d'avantage de loyer et l'écart de taux d'effort de 10 points (25 % contre 15 %) sont au manuscrit, P1-C5. |
| `P-D-105` | 3,8 % | Perdants | part des subsides et marchés publics avantageux dans la valeur ajoutée des entreprises non financières | `sans vis-à-vis` | — | Le corpus porte 68,9 Md€/an d'aides éteintes dont 41,4 aux entreprises (R-D2-4-1-e2) ; le proto compte 56 Md€ en ajoutant les marchés publics. Périmètres distincts, non comparables en l'état. |
| `P-D-106` | 2,3 millions | Perdants | nombre d'étudiants non boursiers | `sans vis-à-vis` | — | Le manuscrit porte le rapport et non l'effectif : « les étudiants non boursiers sont moitié plus nombreux que les étudiants boursiers », 40 % contre 60 % à la note e83 (N-e83-1). |
| `P-D-107` | 3 | Perdants | seuil de trois enfants au-delà duquel les parents sont perdants | `sans vis-à-vis` | — | Le corpus ne porte pas ce seuil. La déclinaison « 0 € » de soutien socio-fiscal au couple modeste avec un enfant est au manuscrit, P1-C5, et concorde. |
| `P-D-108` | +13 % | Perdants | hausse des salaires nets à l'horizon d'un an | `concordant` | R-D3-2-1-p1 · R-D3-2-1-e1 · R-lexique-restitution-b1 | Le manuscrit porte la même hausse pour les enseignants en P3-C4 — « maintenu et augmenté de +13 % grâce à la restitution ». Le candidat rejoint le groupe existant « hausse des salaires nets à l'horizon d'un an ». |
| `P-D-109` | environ +50 % | Perdants | hausse de la fiscalité foncière à la détention | `sans vis-à-vis` | — | Le corpus porte la taxe foncière unifiée en euros par mètre carré au taux fixé localement, et la suppression des droits de mutation, sans aucun taux ni aucune variation chiffrée. |
| `P-D-001` | 1270 | 3 axes de simplification | prélèvements obligatoires augmentés des crédits d'impôt | `sans vis-à-vis` | — | Agrégat propre au proto. Le corpus ne porte ni PO+CI ni les 1 270 Md€. |
| `P-D-002` | 1270 | 3 axes de simplification | poids de la dépense publique dans la richesse produite | `divergence d'hypothèse` | manuscrit P1-C1 et P1-C3 | Même fait, deux assiettes qui s'excluent : le proto additionne PO + CI + bouclier + déficit pour 1 445 Md€, soit 50 % du PIB ; le manuscrit porte 1 714 Md€ dépensés en 2025 et des dépenses publiques à 57 % de la richesse produite. Aucun des deux nombres n'est au référentiel. |
| `P-D-003` | 1990 | 3 axes de simplification | aucun — millésime d'une décision du Conseil constitutionnel cité en adresse web | `sans vis-à-vis` | — | Non-grandeur. Faux positif du relevé. |
| `P-D-004` | 922276 | 3 axes de simplification | aucun — fragment d'adresse web | `sans vis-à-vis` | — | Non-grandeur. Faux positif du relevé. |
| `P-D-005` | 2024 | 3 axes de simplification | rendement d'un point de CSG d'activité | `sans vis-à-vis` | — | Aucune entrée du corpus ne porte le rendement d'un point. Il se retrouve par division de R-D3-2-1-p4 (114 Md€) par R-D3-2-1-p5 (9,7 points), soit 11,75 Md€ — proche des 11,8 du proto. Un calcul n'est pas un vis-à-vis : relevé, non conclu. |
| `P-D-006` | 2024 | 3 axes de simplification | assiette de la CSG rapportée au salaire brut | `concordant` | R-D3-2-1-p6 | Rapprochement déjà écrit, sur 98,25 %. Tête décalée : le relevé a pris le millésime 2024. Le taux de 9,2 % de l'énoncé est celui de la CSG seule, quand R-D3-2-1-p5 porte 9,7 points CSG + CRDS — cohérent, pas contradictoire. |
| `P-D-007` | 2024 | 3 axes de simplification | rendement annuel de la CSG d'activité | `sans vis-à-vis` | — | R-D3-2-1-p4 porte 114 Md€ pour 9,7 points, CSG et CRDS d'activité ; le proto porte 108,6 Md€ pour les 9,2 points de CSG seule. Périmètres différents et cohérents entre eux. |
| `P-D-008` | 2024 | 3 axes de simplification | rendement annuel total de la CSG | `sans vis-à-vis` | — | Le corpus ne porte que la part d'activité. |
| `P-D-009` | 8657156 | 3 axes de simplification | aucun — fragment d'adresse web | `sans vis-à-vis` | — | Non-grandeur. Faux positif du relevé. |
| `P-D-010` | 2024 | 3 axes de simplification | salaire brut moyen mensuel du secteur privé, 2024 | `sans vis-à-vis` | — | Le corpus porte le net médian, jamais le brut moyen. |
| `P-D-011` | 2024 | 3 axes de simplification | salaire net moyen mensuel du secteur privé, 2024 | `sans vis-à-vis` | — | Le corpus porte le net médian, jamais le net moyen. L'élasticité de 1,317 n'est portée nulle part. |
| `P-D-012` | 2024 | 3 axes de simplification | salaire médian net mensuel, 2024 | `concordant` | N-e4-1 · N-e99-2 | Rapprochement déjà écrit, sur 2 190 €. Tête décalée : le relevé a pris le millésime 2024. |
| `P-D-013` | 1801,80 € | 3 axes de simplification | SMIC brut mensuel | `sans vis-à-vis` | — | Aucune entrée ne le porte. La valeur sert au motif du groupe « assiette de la CSG rapportée au salaire brut » de `sources_chiffres.py`, qui n'est pas une entrée du référentiel. |
| `P-D-014` | 2026 | Prestations sociales | gel des prestations sociales indexées prévu par le PLFSS 2026 | `sans vis-à-vis` | — | Contexte réglementaire, sans grandeur. Le corpus ne porte pas ce gel. |
| `P-D-015` | 2025 | Prestations sociales | aucun — fragment d'adresse web | `sans vis-à-vis` | — | Non-grandeur. Faux positif du relevé. |
| `P-D-016` | 2024 | Prestations sociales | prestations familiales, montant annuel | `sans vis-à-vis` | — | Le corpus porte le montant de l'aide par enfant (275 €/mois, R-D9-4-1-p1) et non la masse des prestations familiales. |
| `P-D-017` | 7 075 M€ | Prestations sociales | autres subventions à la famille, montant annuel | `sans vis-à-vis` | — | Même motif que P-D-016. |
| `P-D-018` | 3 132 M€ | Prestations sociales | dépenses de fonctionnement de la CNAF | `sans vis-à-vis` | — | Le corpus ne porte pas les frais de gestion par branche. |
| `P-D-019` | 7 391 M€ | Prestations sociales | dépenses de fonctionnement de la branche maladie | `sans vis-à-vis` | — | Même motif que P-D-018. |
| `P-D-020` | 14 261 M€ | Prestations sociales | dépenses de fonctionnement du régime général et du FSV | `sans vis-à-vis` | — | Périmètre distinct des 16,9 Md€ de N-e129-1, qui cumulent mutuelles, administrations de sécurité sociale et ministère de la santé sur le seul champ de la santé. L'erreur d'unité du proto — « 14 261 Md€ » pour des M€ — est déjà relevée et corrigée à `sources_chiffres.py`, non au proto. |
| `P-D-021` | 3817 M€ | Prestations sociales | minimum vieillesse, ASPA et ASV, montant annuel | `sans vis-à-vis` | — | Le corpus ne porte pas le minimum vieillesse. |
| `P-D-022` | 2023 | Prestations sociales | évolution annuelle des dépenses d'ASV et d'ASPA | `sans vis-à-vis` | — | Même motif que P-D-021. |
| `P-D-023` | 5014911 | Prestations sociales | aucun — fragment d'adresse web | `sans vis-à-vis` | — | Non-grandeur. Faux positif du relevé. |
| `P-D-024` | 14,1 M | Prestations sociales | nombre d'enfants et pondération retenue pour l'aide unique | `sans vis-à-vis` | — | Le corpus porte le montant par enfant, pas l'assiette démographique. |
| `P-D-025` | 54,5 M | Prestations sociales | nombre d'adultes et pondération retenue pour l'aide unique | `sans vis-à-vis` | — | Même motif que P-D-024. |
| `P-D-026` | 1 | Prestations sociales | population de la France | `divergence d'hypothèse` | manuscrit, Prologue · R-D7-2-1-p1 (déclinaison « 68 M ») | Tête relevée fausse : le « 1 » est celui de « 1er janvier ». Le fait est la population — 67,7 M au 1er janvier 2021, 68,6 M au 1er janvier 2025. Le manuscrit porte « les 68 millions de Français » sans millésime, et R-D7-2-1-p1 retient 68 M comme diviseur du capital restitué. **Le corpus ne date pas sa population, le proto la date** : 68 contre 68,6, et les deux millésimes s'excluent. Éprouvé : le groupe ne passe `F7` qu'avec une tolérance posée à 0,6, et la question 15 dit ce que vaut une tolérance posée. Non écrit. |
| `P-D-027` | 2021 | Prestations sociales | population en ménages fiscaux | `sans vis-à-vis` | — | Le corpus porte 30 M de foyers, déduits de 600 Md€ / 20 000 € (R-D7-2-1-p1), et non la population des ménages fiscaux. |
| `P-D-028` | 2025 | Prestations sociales | projection 2025 des enfants et des adultes en ménages fiscaux | `sans vis-à-vis` | — | Même motif que P-D-027. |
| `P-D-029` | 2021 | Prestations sociales | nombre moyen de personnes par foyer fiscal | `sans vis-à-vis` | — | Même motif que P-D-027. |
| `P-D-030` | 1 | Prestations sociales | échelle des unités de consommation | `sans vis-à-vis` | — | Convention statistique de l'Insee. Le corpus ne l'emploie nulle part. |
| `P-D-031` | 2021 | Prestations sociales | ménages bénéficiaires de prestations sociales et poids dans leur niveau de vie | `sans vis-à-vis` | — | Le corpus ne porte pas le taux de recours agrégé. La note e69 ne porte que le non-recours au RSA. |
| `P-D-032` | 2023 | Prestations sociales | taux d'imposition implicite des revenus déclarés | `sans vis-à-vis` | — | Le corpus porte le taux unique cible de 23 % (R-D9-3-1-p1) et, en déclinaison, l'IR total brut 2023 à 114,3 Md€ — autre grandeur que les 96,9 Md€ hors crédits d'impôt du proto. Ni le taux implicite actuel ni son assiette ne sont au corpus. |
| `P-D-033` | 1176 Md€ | Prestations sociales | revenu net imposable total | `sans vis-à-vis` | — | Même motif que P-D-032. |
| `P-D-034` | 350 | Prestations sociales | coût annuel de l'aide fondamentale universelle | `sans vis-à-vis` | — | Le corpus porte les montants — 550 €/mois par adulte, 275 €/mois par enfant — et jamais le coût agrégé. C'est un manque du corpus, non une divergence. |
| `P-D-035` | 431 | Prestations sociales | dénombrement des opérateurs de l'État | `divergence d'hypothèse` | R-D2-2-1-p1 (déclinaison « 1 104 = 434 + 328 + 24 + 318 ») | 431 opérateurs au sens de la liste du PLF 2026 contre 434 agences nationales au sens du décompte arrêté des 1 104. Valeurs voisines, nomenclatures qui s'excluent : ce ne sont pas les mêmes ensembles. **Réglé au fond par la règle de l'auteur du 20260921** — le livre fait foi, donc le corpus retient son décompte ; les 431 du PLF restent du contexte de sous-jacent. Aucun groupe n'est écrit : les deux têtes ne portent pas le même objet, et une discordance arbitrée y serait un artifice. |
| `P-D-036` | 2024 | Prestations sociales | aucun — millésime d'un jeu de comptes | `sans vis-à-vis` | — | Non-grandeur. Faux positif du relevé. |
| `P-D-038` | 2025 | Prestations sociales | aucun — fragment d'adresse web | `sans vis-à-vis` | — | Non-grandeur. Faux positif du relevé. |
| `P-D-046` | 2022 | Prestations sociales | aucun — en-tête de colonnes d'un tableau | `sans vis-à-vis` | — | Non-grandeur. Faux positif du relevé. |
| `P-D-050` | 28,0 | Prestations sociales | nombre de jours indemnisés par mois au titre de l'assurance chômage | `sans vis-à-vis` | — | Le corpus ne descend pas à la maille du jour indemnisé. |
| `P-D-052` | 1 | Prestations sociales | premier décile de l'allocation mensuelle brute | `sans vis-à-vis` | — | Tête relevée fausse : le « 1 » est l'ordinal du décile. Le corpus ne porte pas la distribution des allocations. |
| `P-D-053` | 1 | Prestations sociales | premier quartile de l'allocation mensuelle brute | `sans vis-à-vis` | — | Même motif que P-D-052. |
| `P-D-055` | 3 | Prestations sociales | troisième quartile de l'allocation mensuelle brute | `sans vis-à-vis` | — | Même motif que P-D-052. |
| `P-D-056` | 9 | Prestations sociales | neuvième décile de l'allocation mensuelle brute | `sans vis-à-vis` | — | Même motif que P-D-052. |
| `P-D-057` | 99 | Prestations sociales | quatre-vingt-dix-neuvième centile de l'allocation mensuelle brute | `sans vis-à-vis` | — | Même motif que P-D-052. |
| `P-D-058` | 5 | Prestations sociales | aucun — note de lecture d'un tableau | `sans vis-à-vis` | — | Tête relevée fausse : le « 5 » est celui de « arrondis au multiple de 5 ». Non-grandeur. |
| `P-D-059` | 6 mois | Prestations sociales | durée d'indemnisation collective du chômage | `concordant` | R-D8-3-1-p1 | Rapprochement déjà écrit, sur six mois. |
| `P-D-060` | 30,0 Md€ | Prestations sociales | assurance chômage transformée en épargne, par an | `concordant` | R-D8-3-1-e2 | Rapprochement déjà écrit, sur 30 Md€/an. Le proto en porte la dérivation, que le corpus n'a pas ; il vaut source de source. |
| `P-D-061` | 17,8 Md€ | Prestations sociales | part de l'allocation chômage absorbée par l'aide fondamentale | `sans vis-à-vis` | — | Décomposition interne au proto. 17,8 + 12,2 = 30,0, le total que porte R-D8-3-1-e2 : le proto est la dérivation de cet effet, que le corpus n'écrit pas. |
| `P-D-062` | 12,2 Md€ | Prestations sociales | économie nette après aide fondamentale sur l'assurance chômage | `sans vis-à-vis` | — | Même motif que P-D-061. |
| `P-D-063` | 7767061 | Prestations sociales | aucun — fragment d'adresse web | `sans vis-à-vis` | — | Non-grandeur. Faux positif du relevé. |
| `P-D-066` | 73 % | Prestations sociales | part des dépenses de retraite couverte par les recettes | `divergence d'hypothèse` | N-e74-1 | Le proto porte 73 %, soit 282,4 / 388. La note e74 donne 282 / 407, soit 69,3 %. L'écart tient au périmètre de dépense, arbitré le 20260825 en faveur du manuscrit sur P-D-065 et confirmé par la règle du 20260921. **Le taux du manuscrit est 69,3 %** ; celui du proto est périmé. |
| `P-D-067` | 106 Md€ | Prestations sociales | déficit spontané annuel du système de retraites | `contradictoire` | manuscrit P1-C5 | Le proto porte 106 Md€, le corps du manuscrit « environ 125 milliards d'euros par an », soit 407 − 282. Même fait, deux valeurs. Le motif de l'arbitrage du 20260825 écarte déjà les 106 Md€ en toutes lettres. **La règle de l'auteur du 20260921 la referme au fond** — le livre prévaut, donc 125 Md€ —, mais aucune entrée du référentiel ne porte encore les 125 Md€ : la contradiction ne peut toujours pas s'écrire à `MEME_QUE`, et elle attend que le corps du livre entre au référentiel (question 33, déjà tranchée). |
| `P-D-068` | 2024 | Prestations sociales | aucun — millésime d'un intertitre | `sans vis-à-vis` | — | Non-grandeur. Faux positif du relevé. |
| `P-D-069` | 253 Md€/an | Prestations sociales | dépenses totales de santé | `sans vis-à-vis` | — | Le manuscrit qualifie sans chiffrer : « nos dépenses en santé dépassent d'un tiers la moyenne de l'OCDE ». Aucun montant au corpus. |
| `P-D-070` | 200,5 Md€/an | Prestations sociales | dépenses publiques de santé | `sans vis-à-vis` | — | Même motif que P-D-069. |
| `P-D-072` | 32,5 Md€/an | Prestations sociales | dépenses de santé prises en charge par les mutuelles | `sans vis-à-vis` | — | Aucun montant au corpus. À rapprocher du 41 Md€ de P-D-093, qui n'est pas la même valeur — divergence interne au proto, relevée et non tranchée. |
| `P-D-073` | 20 Md€/an | Prestations sociales | reste à charge médical des ménages | `sans vis-à-vis` | — | Le corpus porte la règle du bouclier — 10 % par acte, plafond 5 % du revenu (R-D8-4-1-p1) — et non la masse actuelle du reste à charge. |
| `P-D-074` | 52,2 Md€/an | Prestations sociales | dépenses de soins de longue durée hors médical | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-075` | 15,3 Md€/an | Prestations sociales | ventilation des soins de longue durée entre handicap, autonomie et addictions | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-076` | 38,3 Md€/an | Prestations sociales | part publique et part des ménages dans les soins de longue durée | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-077` | 8,7 Md€/an | Prestations sociales | dépenses de prévention | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-078` | 16,9 Md€/an | Prestations sociales | frais de gestion cumulés de la santé, par an | `concordant` | N-e129-1 | Rapprochement déjà écrit, sur 16,9 Md€. La note source le candidat, qui n'a pas de source propre. |
| `P-D-079` | 7 Md€/an | Prestations sociales | ventilation des frais de gestion de la santé entre sécurité sociale, État et mutuelles | `sans vis-à-vis` | — | La note e129 nomme les trois postes sans les chiffrer ; le proto les chiffre, et 7 + 1,2 + 8,7 = 16,9 redonne N-e129-1. C'est précisément le cas où le proto se cite comme source de source. |
| `P-D-080` | 16,3 Md€/an | Prestations sociales | dépenses publiques d'accidents du travail et maladies professionnelles | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-081` | 242 Md€ | Prestations sociales | dépenses publiques de santé à couvrir hors gestion | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-082` | 1457 Md€ | Prestations sociales | revenus déclarés hors agricoles | `sans vis-à-vis` | — | Aucun montant au corpus. Le proto porte 1 457 Md€ ici et 1 466 Md€ déclarés à P-D-032 : divergence interne, relevée et non tranchée. |
| `P-D-083` | 304,2 | Prestations sociales | cotisations sociales hors équilibre du CAS Pensions | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-084` | 11 Md€ | Prestations sociales | part du CAS Pensions équivalente au privé | `sans vis-à-vis` | — | Le corpus porte la surcontribution d'équilibre de l'enseignement scolaire, 17 Md€ à N-e135-2 ; autre grandeur, autre champ. La valeur de 11 Md€ est reprise par P-D-064, qui est sourcée. |
| `P-D-085` | 21 Md€ | Prestations sociales | contributions et taxes sociales | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-086` | 14 Md€ | Prestations sociales | CSG hors activité | `sans vis-à-vis` | — | Aucun montant au corpus. Le proto porte 14 Md€ ici quand P-D-008 et P-D-007 laissent 45,2 Md€ par différence : divergence interne, relevée et non tranchée. |
| `P-D-087` | 10,5 Md€ | Prestations sociales | remises conventionnelles | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-088` | 368 Md€ | Prestations sociales | total des recettes sociales du socle | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-089` | 200 Md€ | Prestations sociales | socle de répartition cible des retraites | `sans vis-à-vis` | — | Le corpus porte la pension de base, 1 100 €/mois (R-D8-2-1-p1), et non la masse du socle. |
| `P-D-090` | 242 Md€ | Prestations sociales | dépenses publiques de santé à répartir | `sans vis-à-vis` | — | Aucun montant au corpus. Le proto porte deux fois la même valeur, ici et à P-D-081. |
| `P-D-091` | 142 | Prestations sociales | socle public de santé, cible | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-092` | 100 Md€ | Prestations sociales | dépenses de santé à flécher sur le compte santé | `sans vis-à-vis` | — | Aucun montant au corpus. |
| `P-D-093` | 41 Md€ | Prestations sociales | dotation du compte santé | `sans vis-à-vis` | — | Aucun montant au corpus. Les 41 Md€ de mutuelles ne sont pas les 32,5 Md€ de P-D-072 : divergence interne, relevée et non tranchée. |
| `P-D-094` | 10 pt | Prestations sociales | ventilation en points d'impôt du financement de la santé | `sans vis-à-vis` | — | Hypothèse de travail propre au proto. Le taux unique de 23 % du corpus (R-D9-3-1-p1) est un taux d'imposition du revenu, non une somme de points affectés. |
| `P-D-095` | 30 % | Prestations sociales | taux de taxation des revenus du capital | `concordant` | N-e15-2 | Même fait, même valeur : 30 % au prélèvement forfaitaire unique, que la note e15 porte comme taux de taxation du capital. La décomposition 23 + 7 du proto rejoint par ailleurs le taux unique de 23 % de R-D9-3-1-p1. |
| `P-D-096` | 5 pt | Prestations sociales | points d'impôt sur le revenu affectés à la retraite | `sans vis-à-vis` | — | Même motif que P-D-094. |
| `P-D-097` | 368 Md€ | Prestations sociales | ventilation des charges sociales entre santé et retraite | `sans vis-à-vis` | — | Ventilation interne du total de P-D-088. Aucun montant au corpus. |
| `P-D-098` | 1457 Md€ | Prestations sociales | revenus déclarés hors agricoles et hors pensions | `sans vis-à-vis` | — | Aucun montant au corpus. Reprise de P-D-082 avec une déclinaison de plus. |
| `P-D-099` | 2024 | Prestations sociales | flux annuel du marché du logement et volume remis sur le marché | `sans vis-à-vis` | — | Tête relevée fausse : le « 2024 » est le millésime. Deux relevés, et aucun ne se tranche ici. Un : les 1,77 M de logements remis sur le marché rapportés aux 7,2 M du parc locatif privé font 24,6 %, soit les +25 % d'offre locative privée de R-D7-3-1-e1 — le proto est la dérivation de cet effet, que le corpus n'écrit pas. Deux : le proto compte 5,9 M de logements sociaux quand la note e118 compte 4,8 millions de logements d'organismes HLM — périmètres à distinguer avant toute conclusion. |

## Les contradictions, closes par la règle de l'auteur

**Deux.** Toutes deux opposent le proto au livre, et la règle du 20260921 — *le livre et
ses annexes prévalent* — les tranche dans le même sens. Elles ne se referment pas de la
même façon pour autant.

| entrée | valeur du proto | valeur du corpus | où le corpus la porte |
|---|---|---|---|
| `P-D-102` | 540 000 agents publics · 9 % des effectifs | 580 000 postes · −10 % des effectifs | manuscrit P2-C3, repris en `R-D6-2-1-p1` et `R-D6-2-1-e1` |
| `P-D-067` | 106 Md€ de déficit implicite brut | « environ 125 milliards d'euros par an » | manuscrit P1-C5, corps — **aucune entrée du référentiel ne le porte** |

**`P-D-102` est close et écrite.** Le groupe `postes publics facultatifs supprimés`
porte désormais le candidat et un bloc `arbitrage` — retenu `R-D6-2-1-p1`, par l'auteur,
le 20260921. Joué : la discordance se range en décision, `F7` reste vert, et **l'écart
reste visible au contrôle** plutôt que d'être effacé. Le proto n'est pas réécrit : c'est
une archive. La perte sèche de 30 % du candidat concorde, elle, avec les 70 % de
traitement maintenus de la note e93 et de `R-D6-2-2-p1`.

**`P-D-067` est close au fond et ne peut pas être écrite.** Les 125 Md€ du livre ne sont
entrés nulle part — le relevé de reconfirmation les classe `absent` —, et un groupe
`MEME_QUE` apparie des entrées. **Elle s'écrira quand le corps du livre entrera au
référentiel**, ce que l'arbitrage du 20260921 sur la question 33 a déjà décidé et qui
reste un travail. `P-D-066`, le taux de couverture à 73 %, vient du même écart de
périmètre : le taux du livre est 69,3 %, celui du proto est périmé.

**Le dénombrement des opérateurs se règle au registre, pas à la table.** `P-D-035` porte
431 opérateurs au sens de la liste du PLF 2026, le décompte arrêté des 1 104 en porte
434. Le livre fait foi, donc le corpus retient son décompte ; les 431 restent du
contexte de sous-jacent. **Aucun groupe n'est écrit** : les deux têtes ne portent pas le
même objet, et une discordance arbitrée y serait un artifice.

## Ce que le sous-jacent rapporte

Trois cas où le proto porte la dérivation d'un chiffre que le corpus affirme sans
l'établir. C'est ce que l'arbitrage du 20260921 appelle « source de source », et c'est
le rendement net de la conservation du proto.

- **`P-D-079`** — la note e129 nomme les trois postes des frais de gestion de la santé
  sans les chiffrer ; le proto les chiffre, et 7 + 1,2 + 8,7 = 16,9 redonne `N-e129-1`.
- **`P-D-061` et `P-D-062`** — 17,8 + 12,2 = 30,0, qui est exactement `R-D8-3-1-e2`.
  Le corpus porte le total, le proto porte sa décomposition.
- **`P-D-099`** — 1,77 M de logements remis sur le marché rapportés aux 7,2 M du parc
  locatif privé font 24,6 %, soit les « +25 % d'offre locative privée » de
  `R-D7-3-1-e1`. Le corpus porte l'effet, le proto porte son calcul.

## Quatre divergences internes au proto, relevées et non tranchées

Elles ne sont pas des rapprochements : elles opposent le proto à lui-même. Elles se
relèvent parce qu'un sous-jacent cité comme source de source doit être cohérent.

| entrées | ce qui diverge |
|---|---|
| `P-D-072` contre `P-D-093` | les mutuelles à 32,5 Md€/an, puis à 41 Md€ |
| `P-D-082` contre `P-D-032` | les revenus déclarés à 1 457 Md€, puis à 1 466 Md€ |
| `P-D-086` contre `P-D-007` et `P-D-008` | la CSG hors activité à 14 Md€, quand 153,8 − 108,6 en laisse 45,2 |
| `P-D-081` contre `P-D-090` | la même valeur, 242 Md€, portée deux fois sous deux identifiants |

## La table `MEME_QUE` — écrite, éprouvée, due au dépôt

**Elle est due au dépôt.** Un fil Cowork ne pousse pas (A-393) : le patch est écrit et
joué ici, il se pousse d'une session claude.ai/code. Contenu verbatim au paquet
`methode/paquet_depot_rapprochement_20260921.md`.

**Trois modifications.** `P-D-108` rejoint le groupe « hausse des salaires nets à
l'horizon d'un an » ; un groupe neuf apparie `N-e15-2` et `P-D-095` sur le prélèvement
forfaitaire unique à 30 % ; et le groupe « postes publics facultatifs supprimés »
accueille `P-D-102` avec l'arbitrage de l'auteur. **Aucune tolérance.** Mesuré après
application : la table passe de 25 à 26 groupes, de 53 à 57 entrées rapprochées,
**`0 échec`** au contrôle, 2 discordances arbitrées.

### Un troisième groupe a été écrit, joué, et retiré

« Population de la France » — `R-D7-2-1-p1` et `P-D-026` — semblait concordant : le
corpus divise le capital restitué par 68 M de personnes, le manuscrit écrit « les
68 millions de Français » au Prologue, le proto porte 67,7 M au 1er janvier 2021 et
68,6 M au 1er janvier 2025.

**Joué, le groupe sort en `DISCORDANCE`** — « aucune valeur commune » — et il ne passe
qu'avec une **tolérance posée à 0,6 M**, l'écart entre l'arrondi du corpus et le
millésime du proto. C'est exactement ce que la question 15 tient pour dangereux : une
tolérance posée se remonte pour faire tomber un compte, et le 20260917 elle avait déjà
masqué trois lignes de taxe affectée. **Le groupe est donc retiré, et `P-D-026` est
reclassé en `divergence d'hypothèse`** : le corpus ne date pas sa population, le proto
la date, et les deux millésimes s'excluent.

*La tête de `P-D-026` est fausse par ailleurs — le relevé a pris le « 1 » de
« 1er janvier ». Une correction à `SOURCES` a été écrite puis retirée avec le groupe :
elle changeait la valeur affichée sans changer `valeur_num`, donc elle corrigeait à
moitié. Le défaut est relevé, non corrigé — famille de la question 32.*

## Une limite connue d'avance, non levée

Les 56 entrées de `ref_doctrine` dont les codes de preuve sont en `M-nnnn` renvoient à
`referentiels/releve_affecte.json`, que l'index déclare introuvable. Leur rattachement
au manuscrit reste invérifiable, et le rapprochement s'est fait sur le libellé seul pour
celles-là. **Ce fil n'a pas reconstruit `releve_affecte`.**

## Ce qui n'est pas de ce fil

- Le statut technique du sous-jacent — `role`, `a_sourcer`, et la règle de diffusion qui
  va avec — est proposé au registre du 20260921 et revient à l'auteur.
- Les 87 candidats désormais instruits restent **sans source**. Instruire n'est pas
  sourcer : un candidat `sans vis-à-vis` se conserve, il ne monte pas en confiance.
- La requalification des faux positifs du relevé — millésimes, ordinaux, fragments
  d'adresse — est la question 32, ouverte côté notes et désormais ouverte côté proto.
