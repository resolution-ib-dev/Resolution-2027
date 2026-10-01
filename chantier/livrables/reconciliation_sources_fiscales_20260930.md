# Réconciliation des trois sources fiscales — 20260930

Mandat : constater, prélèvement par prélèvement, les sorts que les sources
existantes tranchent déjà. La table de passage est l'entrée. **Aucune
attribution de sort, aucun arbitrage.** Le solde rendu ici est l'objet du fil
suivant.

Entrée : `referentiels/table_passage_schema_prelevements_20260930.tsv` et
`referentiels/prelevements_forces_20260930.tsv`, 420 prélèvements.
Sources confrontées : le CGI réécrit par l'expert, les énoncés M-028 à M-036,
la mécanique des gages et restitutions.

**Mesure d'ouverture.** 420 lignes au référentiel, 420 libellés distincts,
somme des assiettes 83 + 16 + 30 + 12 + 51 + 108 + 117 + 3 = 420. Le fil procède.

---

## Relevé 1 — La dispersion des sièges

Recompté sur la pièce, code par code. Le taux global retombe à l'unité sur
celui de `livrables/couverture_table_de_passage_20260930.md` : **315 sur 420,
75,0 %**.

| code de siège | prélèvements | part des 420 |
|---|---|---|
| code de la sécurité sociale | 108 | 25,7 % |
| **code général des impôts** | **96** | **22,9 %** |
| **code des impositions sur les biens et services** | **46** | **11,0 %** |
| code général des collectivités territoriales | 17 | 4,0 % |
| code du travail | 15 | 3,6 % |
| code de l'environnement | 7 | 1,7 % |
| code de la construction et de l'habitation | 5 | 1,2 % |
| code de la santé publique | 5 | 1,2 % |
| code général de la fonction publique | 3 | 0,7 % |
| code rural et de la pêche maritime | 3 | 0,7 % |
| code des douanes | 2 | 0,5 % |
| code de commerce | 2 | 0,5 % |
| code monétaire et financier | 2 | 0,5 % |
| code de l'énergie | 2 | 0,5 % |
| code de l'éducation | 1 | 0,2 % |
| code des transports | 1 | 0,2 % |
| **total avec siège** | **315** | **75,0 %** |
| **sans siège renseigné** | **105** | **25,0 %** |

**Normalisation appliquée.** 17 libellés bruts, 16 codes après normalisation :
le sigle `cgct` désigne le code général des collectivités territoriales et
porte 3 lignes — taxe d'ouverture de caveau, taxe de réduction et réunion de
corps, taxe de superposition des corps. Aucune autre variante n'a été trouvée.

**Le fait de structure.** Le premier siège du recensement n'est pas le code
général des impôts mais le code de la sécurité sociale, avec 108 prélèvements
— dont 97 hors du périmètre du schéma. Le CGI et le CIBS, les deux codes que
la refonte touche, portent ensemble **142 prélèvements sur 420, soit 33,8 %**.

---

## Relevé 2 — Ce que le CGI réécrit tranche déjà

**Part mesurée, non supposée : le CGI réécrit ne peut atteindre que les 96
prélèvements dont il est le siège, soit 22,9 % du recensement.** Sur ces 96,
l'article-siège a été apparié à `referentiels/cgi_expert_articles.tsv`.

| ce que le texte fait de l'article-siège | prélèvements |
|---|---|
| **abrogé** — le sort est tranché, c'est une suppression | **71** |
| réécrit — l'article vit, sa rédaction change | 7 |
| allégé — l'article vit, un segment est retiré | 7 |
| **article absent des cinq pièces** — le texte ne dit rien | **11** |
| total | 96 |

**85 prélèvements sur 420, soit 20,2 %, ont leur article-siège touché ; 71,
soit 16,9 %, l'ont abrogé.** Le reste du recensement — 324 prélèvements — est
hors de portée du CGI réécrit, dont 46 au CIBS, que les cinq pièces ne
touchent pas.

**Les 11 articles absents, nommés.** Impôt sur les sociétés (art. 205) · TVA
nette (art. 256) · taxe d'aéroport (art. 1609 quatervicies) · impôt sur les
spectacles, jeux et divertissements (art. 124) · droits de mutation à titre
gratuit par décès (art. 750 ter) · fraction des droits de timbre relative aux
titres de séjour (art. 953) · taxe sur les permis de conduire
(art. 1599 terdecies) · droit de timbre sur les demandes de naturalisation
(art. 958) · droit de timbre sur les visas de passeports étrangers (art. 954) ·
droits sur les conventions et actes civils (art. 680) · redevance pour le
contrôle vétérinaire à l'importation (art. 302 bis X).

**Les 7 réécrits, nommés, avec ce que la réécriture laisse.** Impôt net sur le
revenu (1 A) · retenues à la source sur certains BNC (182 B) · retenues à la
source sur les revenus de capitaux mobiliers (119 bis) · droits
d'enregistrement (635) · droits de mutation à titre gratuit entre vifs (777,
**réduit à une phrase sans taux**) · taxe départementale de publicité foncière
et droits départementaux d'enregistrement sur les mutations à titre onéreux,
qui partagent l'article 1594 A.

**Les 7 allégés, nommés.** Taxe foncière sur les propriétés bâties (1380) ·
taxe foncière sur les propriétés non bâties (1393) · taxes d'enlèvement des
ordures ménagères (1520) · droits de mutation à titre onéreux de créances,
rentes et prix d'offices (724) · contribution de sécurité immobilière (879) ·
taxe sur l'exploration d'hydrocarbures (1590) · droit de licence sur la
rémunération des débitants de tabacs (568).

**Trois articles portent chacun deux prélèvements** — 1635 bis A, 1594 A et
1601 : 96 prélèvements pour 93 articles-sièges distincts.

**Une anomalie de saisie, relevée non corrigée.** Le référentiel écrit
`L568` pour le droit de licence des débitants de tabacs ; l'article du CGI est
568, sans préfixe. L'appariement est fait sur 568.

---

## Relevé 3 — Ce que les règles M-028 à M-036 tranchent

Le sort se lit dans la règle. Le référentiel porte trois colonnes qui
suffisent à l'appariement : `rang`, `motif`, `assiette`.

### La portée de chaque règle, mesurée

| énoncé | ce qu'il vise | prélèvements atteints |
|---|---|---|
| **M-028** — nombre d'impôts | les impositions hors des quatre conservées | **253** visés en suppression, **4** conservés |
| M-029 — taux de la TVA | le taux, non l'existence | 1 — TVA nette |
| **M-030** — taxes spécifiques | les taxes sur produits et services particuliers, sauf l'exception nommée | 85 en assiette 6, **22 exceptés** |
| M-031 — main-d'œuvre et production | les prélèvements assis sur la main-d'œuvre et les impôts de production | 149 par le motif, dont 81 en cotisations sociales — **voir la contradiction C-2** |
| M-032 — taux de l'IS | le taux, non l'existence | 1 — impôt sur les sociétés |
| **M-033** — droits de mutation | les droits à titre onéreux et gratuit | **14** |
| M-034 — plus-values | les prélèvements portant le motif « plus-value » | 4 |
| M-035 — contributions locales | les contributions locales, remplacées par une taxe foncière unique | 19 à la ligne « Taxe foncière » du schéma |
| M-036 — taux de l'IR | le taux, non l'existence | 1 — impôt net sur le revenu |

### Le compte d'ensemble, sans double affectation

Sur les **320** prélèvements du périmètre du schéma :

| | prélèvements |
|---|---|
| conservés par M-028 — les quatre `grand` | 4 |
| conservés par l'exception nommée de M-030 — énergies, tabacs, alcools | 22 |
| visés en suppression par M-028 | 253 |
| **sort tranché par les règles** | **279** |
| qualification d'imposition ouverte — les 41 à contrepartie invoquée | 41 |

**279 est exactement ce que la clé du schéma atteint.** Les deux mesures
tombent l'une sur l'autre : la règle tranche le sort de tout ce que la clé
rattache, et de rien d'autre.

**Les 22 exceptées, comptées.** 10 énergies, 5 tabacs, 7 alcools — les seules
lignes du référentiel portant le rang `maintenue`. Leur siège est au CIBS pour
17 d'entre elles, hors du périmètre des cinq pièces du CGI.

**Ce que le montant ne dit pas.** Le sort se lit dans la règle, jamais dans le
montant de la ligne d'agrégat. Deux exemples mesurés : la ligne « dont
assurances », 19,2 Md€ au schéma, ne porte aucune valeur en colonne « Taxes à
supprimer » — ses 8 prélèvements sont maintenus, alors que la ligne est
lourde ; à l'inverse la ligne « dont taxe pollution », 1,0 Md€, porte 2
prélèvements visés en suppression pour 1,4 Md€ de rendement 2026.

---

## Relevé 4 — Ce que la mécanique des gages rattache à un circuit

La mécanique rattache par **affectataire** et par **agrégat**, jamais
prélèvement par prélèvement. Ce qui se rattache nominativement :

### Circuit A — la restitution, 236,055 Md€/an

**Par la chaîne A, taxe affectée : 34 prélèvements nommés**, recomposés depuis
les huit affectataires isolés à l'onglet `Synthèse TA`.

| affectataire, libellé exact du classeur | prélèvements du référentiel | lignes d'annexe 2 |
|---|---|---|
| France Compétences | 11 | 11 |
| CNC + CNM + Association pour le soutien du théâtre privé | 12 | 12 |
| AFITF | 4 | 4 |
| CCI France + Chambres départementales d'agriculture | 3 | 3 |
| Agences de l'eau | 1 | 1 |
| Action Logement Services | 1 | 1 |
| Établissements publics fonciers | 1 | 34 |
| ANAH | 1 | 1 |
| **total** | **34** | **67** |

**Emploi principal du circuit A : 2 prélèvements nommés** — contribution
sociale généralisée 155 467,8 M€ et contribution pour le remboursement de la
dette sociale 9 350,4 M€, dont la part sur les revenus d'activité, 114,46 Md€,
est ce que le circuit A couvre.

**L'écart de granularité, nommé.** Une ligne d'annexe 2 n'est pas un
prélèvement : les établissements publics fonciers portent 34 lignes pour un
seul prélèvement du référentiel, les taxes spéciales d'équipement. Le compte
ne se fait donc pas ligne à ligne, et c'est mesuré ici, non supposé.

### Circuit B — la compensation fiscale, 67,75 Md€

**2 prélèvements nommés, et eux seuls** : l'impôt sur les sociétés, qui porte
25,69 Md€ par 27 points de taux, et la taxe foncière, qui porte 42,06 Md€.
Les 137,05 Md€ de taxes supprimées sont un agrégat de lignes du schéma ; la
mécanique ne les ventile pas au prélèvement, et le fil ne les ventile pas
davantage.

### Circuit C — l'aide fondamentale

**1 prélèvement nommé** : l'impôt net sur le revenu, dont le taux unique
d'entrée estimé à 22,737 % referme le compte. Le circuit s'auto-finance et ne
rattache aucun autre prélèvement.

**Total rattaché à un circuit : 39 prélèvements sur 420, soit 9,3 %.**

---

## Relevé 5 — Les contradictions, et le solde

### Les contradictions, nommées, non résolues

**C-1 — Le rattachement de l'épargne salariale n'est plus celui de
l'arbitrage.** La table de passage rattache à « dont forfaits de cotisation »
le forfait social et les contributions sur les attributions d'options et
d'actions gratuites. L'arbitrage de l'auteure du 20260930 retient **forfait
social + contribution solidarité autonomie**, les contributions sur actions
gratuites restant hors périmètre. La table porte encore l'ancien
rattachement. Enjeu : 1 669,1 M€.

**C-2 — Les 81 cotisations sociales, visées et exclues à la fois.** M-031
vise « les autres prélèvements assis sur la main-d'œuvre » ; 81 prélèvements
de l'assiette 1 portent le motif « main-d'oeuvre » au référentiel. La décision
de l'auteure portée sous M-028 dit à l'inverse que les « cotisations restantes
[sont] laissées de côté, traitées plus tard par convergence et lissage
progressifs ». Deux sources traitent différemment 81 prélèvements. C'est la
contradiction la plus lourde en nombre du relevé.

**C-3 — Une taxe foncière au schéma, deux au texte.** M-035 supprime les
contributions locales et crée une taxe foncière unique en euros par mètre
carré. Le CGI réécrit maintient deux taxes — propriétés bâties (1380, allégé)
et propriétés non bâties (1393, allégé) — et conserve l'assiette en valeur
locative. Concerne 2 prélèvements et la ligne du schéma qui porte 42,9 Md€.

**C-4 — Un taux de TVA au schéma, deux au texte.** M-029 pose le taux unique
à 20 %. Le CGI réécrit maintient l'article 278-0 bis et porte son taux de
5,5 % à 7 %. Concerne 1 prélèvement et 33,4 Md€ de taux réduits.

**C-5 — Les droits de mutation à titre gratuit, supprimés d'un côté,
subsistants sans taux de l'autre.** M-033 supprime les droits et institue la
franchise de 3 %. Le CGI réécrit maintient l'assiette (750 ter, non touché) et
réduit l'article 777 à « Les droits de mutation à titre gratuit sont fixés au
taux » — phrase inachevée, sans taux. Concerne 2 prélèvements pour 21,4 Md€.

**C-6 — Une accise maintenue dont le siège est touché.** Le droit de licence
sur la rémunération des débitants de tabacs porte le rang `maintenue` —
l'exception nommée de M-030 — et son article-siège au CGI, l'article 568, est
allégé par le texte. 330,5 M€.

**C-7 — Le texte tranche 8 des 41 que le schéma laisse ouverts.** Les 41
prélèvements à contrepartie invoquée n'ont aucun réceptacle au schéma et leur
qualification est ouverte. Huit d'entre eux ont pourtant leur article-siège
touché par le CGI réécrit : **sept abrogés** — droits perçus au profit de la
CNAMTS en matière de produits de santé (1635 bis AE), redevance pour
l'agrément des établissements du secteur de l'alimentation animale
(302 bis WD), redevance sanitaire d'abattage (302 bis N), redevance sanitaire
de découpage (302 bis S), redevance sanitaire de première mise sur le marché
des produits de la pêche (302 bis WA), redevance sanitaire de transformation
des produits de la pêche (302 bis WB), redevance sanitaire pour le contrôle de
certaines substances et de leurs résidus (302 bis WC) — et **un allégé**, la
contribution de sécurité immobilière (879), qui pèse à elle seule 814,6 M€.

**Un signalement qui n'est pas une contradiction.** Les 46 prélèvements dont le
siège est au CIBS sont hors du périmètre des cinq pièces. Leur silence n'est
pas un maintien — c'est la règle de lecture § 2.3 de
`reference/cgi_expert_regles_de_lecture.md`. 17 des 22 accises maintenues sont
dans ce cas.

### Le solde — ce qu'aucune des quatre sources n'atteint

**129 prélèvements sur 420, soit 30,7 %.**

| ensemble | prélèvements | sans siège renseigné | avec un siège, et rien qui les traite |
|---|---|---|---|
| cotisations sociales — assiette 1 | 83 | 3 | 80 |
| contributions sociales sur les revenus — assiette 2 | 11 | 1 | 10 |
| contrepartie invoquée — les 41, moins les 8 que le CGI touche | 33 | 17 | 16 |
| hors champ — assiette 8 | 2 | 1 | 1 |
| **total** | **129** | **22** | **107** |

**Ce que le solde n'est pas.** Ce n'est pas un défaut d'appariement. Les 83
cotisations sociales et les 11 contributions sociales sur les revenus sont
hors du périmètre du schéma par construction ; les 33 forment une catégorie
entière sans réceptacle. Aucune règle d'appariement ne les rattacherait.

**Les 107 qui portent un siège** sont ceux sur lesquels un fil d'attribution
peut travailler sans mesure préalable : 80 au code de la sécurité sociale pour
les cotisations, 10 au même code pour les contributions sur les revenus, et
16 dispersés — code de l'environnement, code de la santé publique, code
monétaire et financier, code de l'énergie, code des transports, code rural,
code général des collectivités territoriales, code des impositions sur les
biens et services, code de commerce.

**Les 22 sans siège** appellent d'abord une mesure de siège, pas une
attribution de sort. Trois d'entre eux sont les contributions des employeurs
de main-d'œuvre étrangère, permanente, saisonnière et temporaire ; un est les
prélèvements de solidarité, 15 634,9 M€ — le plus lourd prélèvement du
recensement dépourvu de siège établi.

### Ce que le fil ne fait pas

Aucun sort attribué, aucune contradiction résolue, aucune rédaction, aucun
arbitrage. Les sept contradictions et les 129 prélèvements du solde sont
l'objet du fil suivant.

---

## Sources

`referentiels/table_passage_schema_prelevements_20260930.tsv` ·
`referentiels/prelevements_forces_20260930.tsv` ·
`livrables/couverture_table_de_passage_20260930.md` ·
`referentiels/cgi_expert_articles.tsv` ·
`livrables/cgi_expert_couverture_20260929.md` ·
`reference/cgi_expert_regles_de_lecture.md` ·
`livrables/mecanique_gages_restitutions_20260929.md` ·
`livrables/paquet_machine.md`, énoncés M-028 à M-036 ·
`livrables/arborescence_mesures_20260928.md`, mouvement 5
