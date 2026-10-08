# Croisements — passe unique sur la liasse entière, dépôt 2027 — 20261007

**Porteur** : fil Cowork de croisement, dépôt 2027, 20261007. Matière unique : l'étape 4 de la
procédure de fin de chantier, jouée en une fois. **Aucune pièce n'est réécrite.**

**Mandat** : l'auteure, 20261007 — jouer les sept contrôles de l'étape 4 sur la liasse entière,
rendre les corrections en clair, porter en réserve les cinq paramètres non arrêtés sans qu'ils
arrêtent les autres contrôles.

**Domicile** : `methode/etats/CROISEMENTS_20261007.md`.

**Appui** : `methode/appui_des_passes.md` · `methode/procedure_fin_de_chantier_depot_2027.md`,
§ 4 · `methode/COMMUN.md` · `reference/regles_credits.md` · `reference/guide_legistique.md` ·
`livrables/registre_colonnes_depot_2027.md` · `livrables/registre_sources_gage.md` ·
`methode/etats/APP_collectivites.md` · `APP_etatB.md` · `APP_arrets_immediats.md` ·
`APP_social.md` · `APP_fiscal.md` · `APP_compte_epargne.md` ·
`RECONCILIATION_impositions_maintenues.md` — tous ouverts le 20261007 avant la passe. Droit en
vigueur : dépôt local `/home/claude/droit/`, base LEGI millésime **20261001**, `droit.py etat`
joué (63 lignes, 43 textes).

**Mesure** : **32 pièces mesurées présentes au projet et lues intégralement** — le mandat en
annonce 31, la liste qu'il porte en compte 32 ; aucune absente, aucune tronquée · 7 contrôles
joués, **6 rendent au moins une anomalie, 1 compte zéro faute d'objet à la liasse** ·
**23 anomalies** au total, chacune avec sa correction en clair · **7 catégories d'objets laissés
hors contrôle**, raison donnée pour chacune · 5 réserves · 3 questions fermées.

---

## 0. Mesure d'entrée — ce qui a été compté, et comment

| compte | valeur | instrument |
|---|---:|---|
| pièces annoncées au mandat | 31 | énoncé du mandat |
| pièces effectivement nommées par le mandat | **32** | dénombrement de la liste, lieu par lieu : clause 1 · `P1/` 12 · `P2/` 11 · `SS/` 5 · `sans_colonne/` 3 |
| pièces lues intégralement au projet | **32** | `project_read`, une par pièce, contenu entier |
| pièces absentes | **0** | — |
| rangs du III de la clause, en sortie | **396** | réunion des sept listes du IV recalculée ligne à ligne |
| amendements de crédits à la liasse | **23** | 20 à `etatB_01` à `04`, 3 à `coll_P2_02` |
| amendements de plafond d'emplois | **1** | `etatB_04`, pièce T2-0 |

**Écart de mesure n° 1, inscrit.** Le mandat annonce 31 pièces et en nomme 32. Le compte qui fait
foi est 32 ; aucune pièce n'a été écartée pour tenir le nombre annoncé.

---

## 1. Contrôle des dates

**Compte** : 32 pièces examinées · dates d'entrée en vigueur ou de champ d'application relevées
aux dispositifs : **26 pièces en portent, 6 n'en portent aucune** (les 4 fichiers d'état B et
`coll_P2_02`, un amendement de crédits n'en portant pas, et `4_7`, périmée) · **0 date au
31 décembre** · **0 date hors 1er janvier ou 1er juillet** · **5 pièces de troisième partie de loi
de financement, 5 portent leur propre date** · **2 exceptions de date non inscrites**.

**Pièces de loi de financement — la règle de date propre est tenue sur les cinq.**

| pièce | division porteuse | date |
|---|---|---|
| `SS/n5_cadre_bouclier_sanitaire` | II | 1er janvier 2028 |
| `SS/n5_extinction_aides_fondues` | II | 1er janvier 2028, sous condition d'entrée en vigueur de l'aide fondamentale ; second terme 1er janvier 2030 |
| `SS/n5_amorce_extinction_repartition` | premier alinéa du I | 1er janvier 2028 |
| `SS/n7b_m037a_gel_indexations_lfss` | II | revalorisations prenant effet à compter du 1er janvier 2027 |
| `SS/n7b_ss03_liste_niches_sociales` | IV de l'article 2 | 1er juillet 2027, par tiers pour les rangs 10° et 24° |

**Corrélation des pièces liées — vérifiée, aucune discordance.** 1er juillet 2027 : clause
(IV, D), `4_2_A` (I), `4_2_B` (I), `4_5` (exercices ouverts), `n7b_m022`, `n7b_ss03`. 1er janvier
2028 : `4_2_C`, `4_2_D`, `4_4`, clause (IV, C et C bis, III quinquies), `coll_P1_02` (palier des
deux tiers), `n5_compte_epargne_personnel` (VIII), `SS/n5_amorce_extinction_repartition` (I).
1er janvier 2027 : `n6_typologies`, `n6_defaisance`, `n6_logement_social_flux`, `n7b_m037b`,
`coll_P2_01` (C du XI), `coll_P2_04` (V), `coll_P1_01` (III).

### Anomalie 1.1 — deux exceptions de date arrêtées, jamais inscrites, et le registre qui doit les porter n'existe pas

`etatB_03` arrête, au bloc interne de ses pièces 2.6-A et 2.6-C, deux dates qui ne sont ni un
1er janvier ni un 1er juillet : **1er juin 2027** (dépôt de la demande d'aide au logement) et
**1er avril 2027** (entrée progressive de l'hébergement d'urgence). `APP_etatB` et `L13` les
déclarent « à inscrire au registre des exceptions ». **Mesure : recherche nominative du registre
des exceptions au projet — 0 document.** Il n'existe pas.

Troisième exception déjà arrêtée ailleurs et dans le même cas : le **1er décembre 2027** du terme
de la restitution de CSG et de CRDS (`methode/etats/L2.md`), porté par SS-05, hors liasse.

**Correction proposée, en clair.** Ouvrir `livrables/registre_exceptions_dates.md`, trois lignes,
une par exception, chacune avec son motif et la pièce qui la porte :

> | date | pièce porteuse | motif de l'exception |
> |---|---|---|
> | 1er avril 2027 | P2-08, socle d'hébergement (jambe de crédits : `P2/etatB_03`, pièce 2.6-C) | entrée progressive du recentrage, arbitrage du lot 13 |
> | 1er juin 2027 | P2-07, extinction de l'aide au logement (jambe de crédits : `P2/etatB_03`, pièce 2.6-A) | ancrage au dépôt de la demande, acte de la caisse, non antidatable — arbitrage du lot 13 |
> | 1er décembre 2027 | SS-05, restitution salariale | terme mensualisé de la baisse de CSG et de CRDS, arbitrage de l'auteure du 20261005 |

**Les deux pièces normatives qui portent ces dates — P2-07 et P2-08 — ne sont pas à la liasse.**
Compté, dit, non élargi.

### Anomalie 1.2 — trois marches de `4_6` hors des quatre dates communes, déclarées mais non inscrites

`4_6` porte 1er juillet **2028**, **2029** et **2030**. Ce sont bien des 1er juillet, donc
conformes à la règle du jour ; elles ne sont **aucune des quatre dates communes** (1er janvier
2027, 1er juillet 2027, 1er janvier 2028, 1er janvier 2029) que le IV de la clause fixe pour la
liasse. La pièce le déclare et renvoie à un registre d'exceptions qui n'existe pas.

**Correction proposée** : trois lignes de plus au registre ouvert à l'anomalie 1.1, motif commun
« sortie progressive de l'alimentation, calendrier arrêté par l'auteure le 20261005 ; les marches
de 2029 et 2030 sont déduites et restent à confirmer ».

---

## 2. Contrôle des gages

**Compte** : 32 pièces examinées · **6 pièces perdent une recette, 6 portent leur clause** (aucun
manquant) · **0 gage porté par un amendement de crédits** sur les 23 · **1 niche nommée gage
encore une pièce du circuit B au registre** · **2 écarts de circuit** · **1 contradiction de gage
entre deux pièces**.

| pièce | circuit | perte de recette | clause portée |
|---|---|---|---|
| `4_2_A` | B | oui | VI — majoration de l'IS (CGI, 219) |
| `4_2_B` | B | oui | VI — DGF puis IS |
| `4_2_C` | B | oui | V — DGF puis IS |
| `4_2_D` | B | oui | IV — IS |
| `4_4` | B | oui | IX — DGF puis IS |
| `n7b_m022` | B | oui | VI — IS |
| `4_5`, `4_6`, clause, `n7b_ss03` | B puis A | non, recette en hausse | aucune, et aucune due |
| 13 pièces de dépense (coll, n6, etatB, SS, m037a/b, m070, compte d'épargne) | A ou C | non, diminution de charge | phrase de restitution, jamais un gage |

**Aucune des six clauses de gage ne nomme une niche** : toutes visent la majoration du taux de
l'article 219 et, pour la part locale, la majoration de la dotation globale de fonctionnement.
Sur les pièces, la règle « aucune niche nommée ne gage une pièce du circuit B » est **tenue**.

### Anomalie 2.1 — le registre des sources de gage gage encore une pièce du circuit B sur une niche nommée

`livrables/registre_sources_gage.md`, § I, quatrième ligne : les **certificats d'économies
d'énergie** y sont gagés, sous condition, sur **A-7 — CGI, article 208, 3° nonies, clause générale,
article 1er, III, 182°**, pour 556 M€. La pièce `n7b_m022` a abandonné cette prétention le
20261005 et porte depuis un gage `GR` sur la majoration de l'IS ; elle le dit à son bloc interne
(« la ligne quitte sa source antérieure », « A-7 est libérée »). **Le registre n'a pas été repris.**
Tant qu'il porte cette ligne, une niche nommée gage une pièce du circuit B.

**Correction proposée, en clair**, au § I du registre, quatrième ligne : remplacer la ligne « — ⚑ |
certificats d'économies d'énergie » par :

> | — ⚑ | certificats d'économies d'énergie | 2.5 | suppression du versement libératoire de l'article L. 221-4 du code de l'énergie — **circuit B** | **majoration du taux de l'impôt sur les sociétés**, variable de solde de la refonte | CGI, art. 219 | solde de la refonte arrêté par la pièce 4.5 | `figé` le 20261005 — forme `GR`. **La prétention conditionnelle sur CGI, art. 208, 3° nonies est abandonnée ; A-7 est libérée.** |

Et, au § V, ligne A-7 : état « **disponible** — libérée le 20261005, la pièce des certificats
d'énergie étant passée au gage `GR` » (le rang du III devient **179°**, voir le contrôle 5).

### Anomalie 2.2 — `4_6` est au circuit A sur la pièce, au circuit B au registre

L'arbitrage du 20261007 reclasse `4_6` (taux réduits de TVA de droit commun) au **circuit A**. La
pièce le porte à son cartouche et à son V. Sa propre section « Correspondance avec la refonte » et
le registre des sources de gage lisent encore son gisement au **circuit B**. Un euro appartient à
un circuit : l'écart est ouvert.

**Correction proposée** : porter au registre des sources de gage une ligne au § II (emplois à
`nul`) — « `4_6`, taux réduits de TVA de droit commun, lot 4.6, recette en hausse, **circuit A**,
phrase de restitution, aucun gage dû » — et retirer le gisement G15 (33 Md€) du décompte du
circuit B. **La section « Correspondance avec la refonte » de la pièce porte l'écart et le
déclare ; elle ne se corrige pas ici.**

### Anomalie 2.3 — le gage de `4_2_C` promet aux collectivités une compensation que `coll_P1_01` leur refuse

Le V de `4_2_C` écrit : « La perte de recettes pour les collectivités territoriales est compensée,
à due concurrence, par la majoration de la dotation globale de fonctionnement. » Le **III bis** du
nouvel article L. 1614-1-2, créé par `coll_P1_01`, écrit l'inverse : la perte des droits de
mutation « constitue une réduction des ressources de la collectivité » qui **s'impute** sur la
réduction due au titre des retraits de compétences, et « la part de cette perte qui excède la
réduction prévue au I **n'est compensée que dans les conditions prévues à l'article LO 1114-4** ».
`coll_P1_01` relève lui-même la tension et la renvoie « au porteur de 4.2 C ».

Les deux formules ne sont pas conciliables au même rang : l'une est une formule de recevabilité de
`COMMUN.md`, l'autre une règle de fond. **Le fil ne tranche pas** (R-F) : question fermée n° 3.

### Hors contrôle, et la raison

Les lignes du registre des sources de gage attachées à **P1-01** (aide fondamentale) et à
**SS-05** (restitution salariale) ne sont pas contrôlées : **les deux pièces ne sont pas à la
liasse**. Leur gage reste donc non vérifié sur pièce. Compté : 2 lignes.

---

## 3. Contrôle des crédits — les six invariants

**Compte** : **23 amendements de crédits** mesurés à la liasse · **20 tiennent les six
invariants**, aucun ne porte de gage · **3 ne les tiennent pas** · **1 amendement de plafond
d'emplois**, hors des six invariants, motivé · **1 jeu de corrections rendu en clair et non
appliqué**.

**Les vingt amendements conformes** — `etatB_01` (2.1-A, 2.1-B), `etatB_02` (2.3-A, 2.3-B, 2.3-C),
`etatB_03` (2.6-A, 2.6-B, 2.6-C), `etatB_04` (T2-1 à T2-12). Une mission par pièce, nommée ·
tableau à quatre colonnes AE et CP · invariant n° 3 **sans objet**, ce sont des minorations sèches
(geste licite de l'article 47 de la loi organique) · une ligne par programme, jamais une action ·
aucun abondement du titre 2 depuis un autre titre, et AE = CP partout où le titre 2 est touché ·
motivation portée.

**Deux contrôles arithmétiques rejoués ici, et ils tombent juste à l'euro et à l'unité.**

- Somme des douze minorations de titre 2 (T2-1 à T2-12) : **900 000 000 €** exactement, égale à
  `Détail Economies`!D38.
- Somme des dix écarts ministériels du tableau de T2-0 : **61 400** exactement, égale à
  `Détail Economies`!J38 ; la base du prorata somme à 224 037 ETPT, comme la pièce l'annonce.

**Recoupement de programme, rejoué** : « Politique de la ville » est touché deux fois —
`etatB_02` 2.3-C hors titre 2 pour 484 848 485 €, `etatB_04` T2-9 au titre 2 pour 1 048 400 €.
Pas de recoupement ; le plafond hors titre 2 (599 923 640 €) tient. « Cohésion des territoires »
porte cinq minorations sur quatre programmes distincts, aucune ne franchit les crédits ouverts de
son programme.

### Anomalie 3.1 — les trois amendements de `coll_P2_02` ne sont pas des amendements de crédits recevables

Les trois amendements A, B et C de `P2/coll_P2_02_credits_etat_B.md` :

1. **ne portent aucun montant** — chaque cellule du tableau lit « à reporter » ; l'invariant n° 2
   (tableau AE et CP) et l'invariant n° 3 ne sont pas vérifiables, et un amendement sans montant
   ne se vote pas ;
2. **portent un tableau à deux colonnes** (« + », « − ») qui mêle AE et CP dans la même cellule,
   là où l'article 43 de la loi organique impose un vote sur les deux et où les vingt autres
   pièces portent quatre colonnes ;
3. **portent une phrase normative au dispositif** — « La présente mesure concourt à la réduction
   des prélèvements pesant sur les revenus d'activité. » — là où un amendement de crédits ne porte
   aucun texte. Les vingt autres pièces la logent à l'exposé, et c'est la forme correcte.

La pièce déclare elle-même les montants « bloquants avant dépôt ». **L'écart de forme, lui, n'est
pas déclaré.**

**Correction proposée, en clair** : reprendre les trois tableaux au gabarit des vingt autres —
`| Programmes | AE + | AE − | CP + | CP − |`, lignes TOTAUX et SOLDE —, porter la phrase de
restitution au dernier paragraphe de chaque exposé sommaire, et **laisser les montants à relever
au projet annuel de performances 2027**, qui reste le bloquant de fond.

### Anomalie 3.2 — les trois divisions rendues en clair pour `etatB_04` ne sont pas appliquées

`APP_etatB`, § 4, rend trois divisions « à appliquer telles quelles » à `etatB_04` par copie
d'octets (R8) : (a) la ligne `Mesure` de l'en-tête, (b) quatre paragraphes après « Petites pièces »
— qualification des 61 400 postes en fermetures, universités, croisement budgétaire, rappel des six
invariants —, (c) deux puces au bloc interne de T2-0.

**Mesure prise sur le texte entier de la pièce, non sur un affichage** : la ligne `Mesure` est
restée dans sa rédaction antérieure (elle s'arrête à « aucun article de code au dispositif » et ne
porte pas « 2 adresses au droit contrôlées, millésime LEGI 20261001 ») · **0 occurrence** de
« fermetures de postes », de « Recoupement avec la pièce 2.3-C » et de « Six invariants » dans
`etatB_04`. **Les trois divisions ne sont pas appliquées.**

**Correction proposée** : rejouer la copie d'octets des trois divisions, telles qu'elles sont
écrites au § 4 de `APP_etatB`. Aucune autre ligne de la pièce ne bouge, aucun montant.

---

## 4. Contrôle de l'autonomie des jambes

**Compte** : 32 pièces examinées · **29 se suffisent et le déclarent** · **2 dépendent d'une
division d'une autre pièce qui n'est pas écrite** · **1 règle du mandat contredite par un
arbitrage antérieur**.

### Anomalie 4.1 — l'exclusion que la clause est censée porter n'est pas à son dispositif

**C'est l'anomalie la plus lourde de la passe.**

Trois pièces déclarent que la clause générale porte une exclusion expresse à son II :

- `P1/n5_compte_epargne_personnel`, bloc interne : « Exclusion expresse du compte dans la clause
  générale (5° du A) — **non joué** : la pièce de la clause générale la porte, non celle-ci » et,
  plus bas, « **sans elle, la clause abroge le compte le jour de son entrée en vigueur** » ;
- `P1/4_2_D`, § Collisions : l'imposition au retrait « serait neutralisée par la clause. Parade :
  exclusion expresse au II de la clause » ;
- `P1/4_2_C`, § Collisions : le seuil de 10 000 € et la tranche à 1 % appellent une « exclusion
  expresse due au II de la clause ».

La clause elle-même l'annonce **deux fois à son propre cartouche** : reprise du lot U1 — « un 5°
exclut les dispositions instituées par la présente loi pour l'aide fondamentale, **le compte
d'épargne et le tarif des droits de mutation** » ; reprise du lot V1 — « II, 5° : le seuil de
perception et la fraction taxée à 1 % du tarif des droits de mutation (III de l'article 683,
articles 719 et 777, pièce 4.2 C) sont exclus **en toutes lettres** du champ du I ».

**Mesure prise sur le dispositif, non sur le cartouche.** Le 5° du II de l'article 1er est écrit :

> « 5° Qui s'appliquent dans les mêmes conditions à toute personne, sans considération de la
> nature ou de l'emploi des biens, revenus ou opérations, le montant qu'elles prévoient pouvant
> être modulé à raison de l'âge ou du handicap. »

**Il ne nomme ni le compte d'épargne personnel, ni le tarif des droits de mutation.** Les quatre
autres rangs du II ne les couvrent pas davantage (1° droit commun, 2° double imposition, 3° droit
de l'Union, 4° taux de TVA). Le cartouche décrit une rédaction que le dispositif ne porte pas.

**Conséquence, et elle est de fond.** Le 5° du A du I de la clause range « un report, un sursis ou
un étalement d'imposition » au nombre des avantages fiscaux que le I fait tomber. L'imposition au
retrait du compte d'épargne (II de l'article 163 quinquies D réécrit par `4_2_D`) et le sursis
d'apport de titres (V de `n5_compte_epargne_personnel`) en sont deux. **En l'état, la clause
abroge le compte d'épargne personnel le jour de son entrée en vigueur**, et la pièce `n5` ne se
suffit pas à elle-même. Le seuil de 10 000 € et la tranche à 1 % de `4_2_C` sont dans le même cas
au titre du 4° du A du I (taux réduit) et du 1° (exonération).

**Correction proposée, en clair — à appliquer au II de l'article 1er de la clause, et nulle part
ailleurs.** Après le 5° existant, insérer un 6° :

> « 6° Qui sont instituées par la présente loi, au nombre desquelles le compte d'épargne personnel
> et le régime d'imposition de ses retraits, ainsi que le seuil et les fractions de la base
> imposable prévus au III de l'article 683 du code général des impôts et les dispositions qui s'y
> réfèrent. »

Le 5° garde son rang et son texte : aucun renvoi n'est touché. **Le fil ne réécrit pas la pièce ;
la division est rendue en clair et s'applique par copie d'octets.**

### Anomalie 4.2 — la règle d'autonomie et l'arbitrage du lot U3 se contredisent sur les taxes affectées

Le mandat du croisement pose : « une taxe affectée va à zéro quand bien même la taxe est supprimée
ailleurs ». `4_2_B`, § « Coordination avec l'article 42 du texte déposé », pose l'inverse : pour
les taxes qu'elle supprime, « le plafond à zéro de la pièce P1-23 **se retire sur ces lignes**,
sinon un même euro est compté au circuit A et au circuit B », et la pièce énumère une
cinquantaine de lignes du tableau de l'article 42 à retirer de P1-23.

Les deux règles sont inconciliables au même rang et du même jour. **Le fil ne tranche pas** (R-F) :
question fermée n° 2. **P1-23 n'est pas à la liasse** : la correction, quelle qu'elle soit,
s'appliquera hors de ce périmètre.

### Ce que le contrôle n'a pas vu, et la raison

Quatre pièces de la liasse déclarent des **jambes corrélées qui ne sont pas à la liasse** et dont
l'autonomie ne se vérifie donc que sur la déclaration : `etatB_01` et `etatB_02` renvoient à P2-03
et à SS-02 ; `etatB_03` à P2-07, P2-08 et P2-09 ; `n7b_ss03` à SS-05 ; `SS/n5_extinction_aides_fondues`
à P1-01. Compté : **7 pièces corrélées hors liasse**.

---

## 5. Contrôle des renvois

**Compte** : **25 renvois entrants au III de la clause relevés par `APP_fiscal`**, dont 5
appliqués et 20 rendus en clair · **9 renvois entrants de plus relevés par la présente passe et
non comptés par `APP_fiscal`** · **396 rangs du III classés par le IV, couverture entière
recalculée ici** · **1 renvoi mort hors clause**.

### 5.1 Couverture du III par le IV — recalculée, et elle tient

Les sept listes du IV (A, B, C, C bis, D, E, F) ont été reprises rang par rang et leur réunion
recalculée : **91 + 109 + 45 + 20 + 92 + 32 + 7 = 396**, **aucun doublon, aucun orphelin, aucun
rang hors de 1° à 396°**. Les listes du dispositif et celles du § 10.1 du bloc interne sont
identiques, lettre par lettre. **Contrôle tenu.**

Écart de forme, sans conséquence : le A n'est pas énuméré au dispositif — il y joue en reliquat
(« Sous réserve des B à F »), ce qui est correct en légistique. Le cartouche du 20261007 écrit
que « le A n'est plus un reliquat implicite : il est énuméré » ; cela ne vaut que du § 10.1,
interne. Pas de correction due au dispositif.

### 5.2 Les vingt renvois rendus en clair par `APP_fiscal` ne sont pas appliqués

Mesure prise sur les pièces : `SS/n7b_ss03` porte encore 47°, 50°, 51°, 65°, 67° ·
`P1/4_2_C` porte encore 237°, 242°, 243°, 252°, 259°, 266° · `P1/4_2_D` porte encore 47°, 51°,
52°, 87°, 88°, 90°, 94°, 99° à 108°. **Les vingt sont dans un bloc `[interne]`, aucun dans un
dispositif** : aucun amendement déposable n'est atteint. La table de passage d'`APP_fiscal` a été
recalculée ici et elle est exacte.

**Correction proposée** : appliquer la table de passage d'`APP_fiscal`, § 3.2, par copie d'octets,
sans toucher une autre ligne de ces trois pièces.

### Anomalie 5.3 — trois renvois entrants morts, non comptés par `APP_fiscal`, dont un qui résout sur un autre article

`APP_fiscal` déclare que `4_2_A` « ne porte aucun renvoi au III de la clause » et que les renvois
entrants sont au nombre de 25. **Mesure rejouée sur les 32 pièces, par recherche du caractère de
rang : trois renvois de plus.**

| pièce | rang écrit | ce que le rang désigne aujourd'hui au III | rang dû |
|---|---|---|---|
| `P1/4_2_A`, § Exclus du dispositif | **298°** | « L'article L. 213-107 du code des impositions sur les biens et services » | **285°** (CGI, art. 1586 ter, cotisation sur la valeur ajoutée) |
| `sans_colonne/n7b_m022`, § Circuit et gage | **182°** | « Le VIII de l'article 209 » | **179°** (CGI, art. 208, 3° nonies) |
| `sans_colonne/n7b_m022`, § Collision | **177°** | « Les 3° quater et 3° quinquies de l'article 208 » | **174°** (CGI, art. 207, 4° du 1) |
| `sans_colonne/n7b_m022`, § Collision | **410°** | **hors de la numérotation** — le III s'arrête à 396° | **394°** (loi n° 2020-1721, art. 27) |

**Deux de ces renvois ne sont pas seulement périmés : ils résolvent sur un autre objet** (298° et
177°), ce qui est pire qu'un renvoi mort — il se lit sans erreur apparente. Le 410° est un renvoi
mort franc.

`APP_arrets_immediats`, § 3, range ces trois rangs de `m022` parmi les « renvois à des pièces du
chantier, non au droit » laissés hors contrôle. **La raison est fausse** : ce sont des renvois à
une division renumérotée, c'est-à-dire exactement l'objet du contrôle 5.

**Correction proposée, en clair**, sur les deux pièces, blocs `[interne]` seulement :
`4_2_A` — « clause générale (III, **285°**) » · `n7b_m022` — « clause générale, art. 1er, III,
**179°** », « Le rang **174°** du III de l'article 1er abroge le 4° du 1 de l'article 207 »,
« Le rang **394°** abroge l'article 27 de la loi n° 2020-1721 ».

### Anomalie 5.4 — les deux registres portent la numérotation périmée

`livrables/registre_colonnes_depot_2027.md`, ligne P1-21 : « `clause_generale_niches_20261004.md`,
**III à 412 rangs** contrôlés au droit le 20261005 ». Le domicile a changé
(`livrables/depot_2027/clause_generale_niches_20261005.md`) et le III compte **396 rangs**.

`livrables/registre_sources_gage.md`, § V, porte onze rangs de l'ancienne numérotation :
A-1 81° · A-2 217° · A-3 146° · A-4 124° · A-5 186° · A-6 88° · A-7 182° · A-8 80° · A-9 212° ·
A-10 130° · C-1 (129°, 54°, 62°, 56°, 137°, 139°, 167°) ; le § VIII en porte quatre de plus
(130°, 165°, 207°, 265°, 312° à 356°) et le § I en porte sept au titre de P1-01.

**Correction proposée** : appliquer aux deux registres la table de passage d'`APP_fiscal`, § 3.2 —
« un rang garde son numéro diminué du nombre de rangs “(Sans objet)” qui le précèdent, augmenté
de 1 au-delà de l'ancien 312° et de 1 encore au-delà de l'ancien 355° » —, et porter au registre
des colonnes « III à **396** rangs » et le domicile `livrables/depot_2027/clause_generale_niches_20261005.md`.

### Anomalie 5.5 — un constat d'absence faux, répété par cinq pièces et un état : la loi organique est au dépôt de droit

Cinq pièces écrivent, à leur bloc interne, que « la loi organique n° 2001-692 n'est pas versée au
dépôt de droit au millésime LEGI 20261001 » et laissent en conséquence l'article 34 de la LOLF
hors contrôle : `sans_colonne/n7b_m022`, `sans_colonne/n7b_m037b`, `sans_colonne/n7b_m070`,
`P2/n6_typologies_de_depenses`, `P2/n6_defaisance_participations`,
`P2/n6_logement_social_flux`. `methode/etats/APP_arrets_immediats`, § 3, en fait sa première
raison de mise hors contrôle, pour **8 références**.

**Mesure rejouée sur un compte, non sur un affichage.** `droit.py etat` rend **63 lignes** et
**43 textes** ; la ligne « loi organique n° 2001-692 du 1er août 2001 — 73 appl. » y figure, au-delà
de la quarantième. Interrogation nominative :

| adresse | verdict | identifiant |
|---|---|---|
| LOLF, art. 19 | `VIGUEUR` | LEGIARTI000006321039 |
| LOLF, art. 21 | `VIGUEUR` | LEGIARTI000044611922 |
| LOLF, art. 34 | `VIGUEUR` | LEGIARTI000044611799 |
| LOLF, art. 47 | `VIGUEUR` | LEGIARTI000006321072 |

**Les huit références déclarées hors contrôle sont toutes contrôlables et toutes en vigueur.** Le
constat vient d'une lecture tronquée de la sortie d'`etat` — la faute que la règle R-B nomme. Trois
autres pièces de la même liasse (`P2/coll_P2_04`, `P2/etatB_01` à `04`, `reference/regles_credits.md`)
contrôlent au contraire la loi organique au dépôt et rendent les mêmes verdicts : la contradiction
était lisible à l'intérieur du corpus.

**Correction proposée, en clair**, sur les six pièces et sur `APP_arrets_immediats` : remplacer la
mention « hors contrôle — la loi organique n'est pas versée au dépôt de droit au millésime
20261001 » par « `EXISTE` (VIGUEUR, LEGIARTI000044611799, base LEGI 20261001) », et retirer la
première ligne du tableau des références hors contrôle d'`APP_arrets_immediats`, dont le compte
passe de 25 à **17**.

### Références laissées hors contrôle par la présente passe, et la raison de chacune

| ensemble | nombre | raison |
|---|---:|---|
| renvois **entrants** vers les 396 rangs du III et vers les 366 articles des III quater et III quinquies, depuis le droit en vigueur | **non dénombrés** | relevé déclaré dû depuis le 20261004 et jamais fait ; à ce volume il appelle son propre fil et un relevé mécanique sur l'extrait. **Le présent contrôle n'a relevé que les renvois entrants depuis les pièces de la liasse et depuis les deux registres** |
| les 433 références du dispositif de l'article 1er de la clause, les 698 articles de `4_2_B`, les 116 de `4_2_A` | 1 247 | contrôlées à leurs passes respectives, non rejouées : la présente passe ne touche aucun dispositif |
| articles du texte déposé (PLF 2027 n° 3210, PLFSS 2027 n° 3211) cités en accroche ou en collision | **46 relevés** | texte en discussion, non droit en vigueur : ils se lisent au socle `socle_texte_plf2027.json` / `socle_texte_plfss2027.json`, que ce fil n'a pas ouvert |
| décisions du Conseil constitutionnel et du Conseil d'État citées (19 relevées) | 19 | le dépôt de droit porte le texte en vigueur, non la jurisprudence |
| cellules de classeur citées par les pièces | **non dénombrées** | aucun classeur n'est monté sur ce fil ; seul `/home/claude/droit/` l'est. Une passe de relevé des cellules reste due avant dépôt |
| textes hors `codes.json` (loi n° 2004-809 art. 199-1, loi n° 86-897 art. 1-1, loi n° 2021-1104 art. 107, loi de finances 2014 art. 92, loi n° 2009-594 art. 31, règlement (UE) 2017/625) | 6 | hors de la liste close des textes couverts par le dépôt |
| articles réglementaires (CGCT R. et D., annexe III au CGI) | 16 | hors de la portée d'un amendement législatif |

---

## 6. Contrôle du registre des colonnes, et du porteur unique de chaque abrogation

### 6.1 Registre des colonnes — un rang par pièce

**Compte** : 32 pièces · **5 fichiers portent un rang au registre**, pour 6 rangs (clause :
P1-21, SS-03, P1-25 ; `n7b_ss03` : SS-03 ; `etatB_01` : P2-01 ; `etatB_04` : P2-02 ; `4_7` :
P1-24, périmé) · **27 fichiers ne portent aucun rang** · **0 rang orphelin au sens strict** (tous
les rangs du registre renvoient à une pièce) · **le registre n'a pas été repris depuis le
20261005**.

| anomalie | constat | correction proposée |
|---|---|---|
| **6.1.a** | 27 des 32 pièces sont rangées à la partie V ter, « écrites la nuit du 20261005, **en attente de rang** ». Le versement du paquet est intervenu le 20261007 ; elles ne sont plus en attente de versement, seulement de rang | ouvrir une entrée unique au registre, qui attribue leurs rangs aux 27 pièces en une fois, dans l'ordre des articles du texte en discussion. **Une entrée recalcule les rangs** (§ V du registre) : les rangs P1-04 à P1-25 et P2-01 à P2-09 se recalculent |
| **6.1.b** | la partie IV du registre range trois pièces en « colonne non écrite ». **Les trois l'ont désormais écrite** : `n7b_m022` « PLF 2027, première partie, article additionnel après l'article 24 » · `n7b_m037b` « PLF 2027, seconde partie, article additionnel après l'article 74 » · `n7b_m070` « PLF 2027, seconde partie, article additionnel après l'article 67 » | vider la partie IV et porter les trois pièces à leur colonne. **Conséquence sur le gage** : la réserve ⚑ du registre des sources (« la ligne des certificats d'énergie ne vaut qu'en première partie ») est levée, la colonne arrêtée étant la première partie |
| **6.1.c** | `P2/coll_P2_04_facultes_et_obligations_de_baisse.md` déclare à son cartouche « colonne : PLF 2027, **première partie** » et vit dans `P2/`. La pièce le dit : « nom de fichier conservé pour les renvois des autres pièces ; la pièce passe en première partie » | inscrire la colonne au registre (première partie, après l'article 34) et **laisser le fichier à son domicile**, les quatre pièces collectivités s'y renvoyant par chemin |
| **6.1.d** | le rang **P1-24** est périmé par la fonte de `4_7` (20261007) et le registre porte encore « structures facultatives, jambe recette » à ce rang | barrer P1-24, mention « périmé le 20261007 par la fonte de la pièce 4.7 dans la clause générale ; rang vacant, non réattribué » (§ V du registre) |
| **6.1.e** | deux fichiers de clause coexistent au projet : `livrables/clause_generale_niches_20261004.md` et `livrables/depot_2027/clause_generale_niches_20261005.md`. Le second fait foi et le dit | marquer le premier « copie de travail périmée le 20261005 ; ne pas lire » ; son retrait relève du fil de rangement |

### 6.2 Porteur unique de chaque article abrogé

**Compte** : la table des porteurs d'`APP_fiscal`, § 2, est reprise et **son verdict est contrôlé
par sondage croisé sur les articles que deux pièces pourraient atteindre** : 4.4 contre la clause
(964 à 983, 1388, 1393, 1407, 1447, 1520, 1529, 1530, 1635 quater A) — **disjoints** ; 4.2 B
contre la clause (1519 à 1519 HB, 1586 ter, 1600, 1635-0 quinquies, L. 421-65 à L. 421-81-1) —
**disjoints, la plage d'immatriculation étant découpée autour des rangs 374° à 386°** ; 4.2 A
contre la clause (990 J, 224, 234 nonies à quindecies, 235 ter) — **disjoints** ; 4.2 D contre la
clause (150 VI, 150 VK, 150 VL, 1609 nonies G) — **disjoints**.

**Deux articles ont trois porteurs, et le contrôle d'`APP_fiscal` ne les voit pas.**

| article | porteur 1 | porteur 2 | porteur 3 | date |
|---|---|---|---|---|
| CGI, **150 VJ** | clause, III, 91° (1°, 2° et 3°) et 92° (5°) | **`4_2_D`, I, 9° (le 4°)** | clause, **III quinquies** (l'article entier) | 1er janvier 2028 pour les trois |
| CGI, **788** | clause, III, 240° (le III) | **`4_2_C`, I, 7° (le IV)** | clause, **III quinquies** (l'article entier) | 1er janvier 2028 pour les trois |

`APP_fiscal` range ces deux articles parmi les « six adresses à double visa **interne** » à la
clause, et écrit que « les 366 articles des III quater et III quinquies sont ceux qu'aucune autre
pièce n'abroge ». **C'est faux pour ces deux-là** : une pièce extérieure en abroge déjà une
subdivision, à la même date.

Le risque est faible — les subdivisions visées sont disjointes et les dates identiques — mais la
forme est fautive : un même article disparaît deux fois le même jour, et le service de la séance
le relève.

**Correction proposée, en clair** : retirer `150 VJ` et `788` de l'énumération du **III quinquies**
de la clause, les deux articles étant déjà vidés par la conjonction de la clause (III), de `4_2_D`
et de `4_2_C`, et porter au § 7 de la clause la mention : « **Deux articles ont été retirés du
III quinquies le 20261007 bis** — 150 VJ et 788 —, une autre pièce de la liasse en abrogeant déjà
une subdivision à la même date ; le compte du III quinquies passe de 185 à **183** articles, celui
de la fonte de 366 à **364**. » Les tables du lot U7 se recalent en conséquence.

**Zéro article à zéro porteur** relevé sur le périmètre mesuré ; les 301 articles retenus pour
coordination ne sont pas abrogés, et c'est voulu.

---

## 7. Contrôle du suivi mensuel

**Compte : zéro, et le motif est l'absence d'objet à la liasse.**

Le suivi par flux et par agent vit en deux fichiers nommés par `methode/etats/L2.md` :
`etats/suivi_calendrier_flux.tsv` et `etats/suivi_mensuel_2027_restitution.tsv`. **Mesure prise par
recherche nominative au projet** : `project_read` sur le second rend « No doc or file » ; la liste
des documents voisins que l'erreur renvoie n'en porte aucun ; une recherche sur « suivi mensuel
par agent, bouclage » ne rend que la procédure, l'état L2 et des pièces sans rapport. **Les deux
fichiers ne sont pas au projet.**

L'objet du contrôle — la pièce SS-05 (restitution salariale) et son suivi — **n'est pas à la
liasse** : SS-05 ne figure pas parmi les 32 pièces.

**Verdict : 0 ligne de suivi contrôlée, 0 bouclage vérifié, 0 anomalie.** Le fil le dit et ne
cherche pas ailleurs. Le contrôle se rejouera quand SS-05 et son suivi seront versés.

---

## 8. Mesure de sortie — le mandat point par point, verdict par point

| n° | point du mandat | verdict | compte |
|---|---|---|---|
| 0 | mesurer les 31 pièces annoncées, toutes présentes au projet | **joué, avec un écart** | 32 nommées, 32 lues, 0 absente ; l'écart de nombre est inscrit au § 0 |
| 0 bis | traiter `4_7` comme périmée, après contrôle | **joué** | la pièce est une notice de péremption ; aucun dispositif n'y subsiste ; son rang P1-24 est périmé et le registre ne le dit pas (anomalie 6.1.d) |
| 1 | **dates** — 1er janvier ou 1er juillet, sauf exception inscrite | **joué** | 0 date au 31 décembre, 0 date hors règle, **2 exceptions arrêtées et non inscrites, le registre qui doit les porter n'existe pas** (anomalie 1.1) ; 3 marches de `4_6` hors des quatre dates communes (1.2) |
| 1 bis | deux pièces liées portent la même date | **joué — aucune discordance** | trois grappes de dates vérifiées pièce par pièce, § 1 |
| 1 ter | une pièce LFSS de dépense qui vise le 1er janvier porte sa propre date | **joué — tenu sur les cinq** | tableau du § 1 |
| 2 | **gages** — un euro, un circuit ; aucune niche nommée sur une pièce B ; chaque perte porte sa clause ; aucun gage sur un amendement de crédits | **joué** | 6 pertes, 6 clauses, 0 manquant · 0 gage sur les 23 amendements de crédits · **1 niche nommée gage encore une pièce B au registre** (2.1) · **1 écart de circuit sur `4_6`** (2.2) · **1 contradiction de gage entre `4_2_C` et `coll_P1_01`** (2.3) |
| 3 | **crédits** — les six invariants sur chaque amendement | **joué** | 20 amendements conformes, sommes recalculées exactes (900 000 000 € et 61 400) · **3 amendements non conformes à `coll_P2_02`** (3.1) · **3 divisions rendues en clair pour `etatB_04` non appliquées** (3.2) |
| 4 | **autonomie des jambes** | **joué** | 29 pièces se suffisent · **la clause ne porte pas l'exclusion que trois pièces supposent, et le compte d'épargne tombe sous la clause** (4.1) · **la règle du mandat et l'arbitrage du lot U3 se contredisent sur les taxes affectées** (4.2) · 7 pièces corrélées hors liasse, nommées |
| 5 | **renvois** — aucun renvoi mort, aucun renvoi à une division renumérotée | **joué** | couverture des 396 rangs recalculée, entière et sans doublon · **20 renvois rendus en clair non appliqués** (5.2) · **3 renvois morts ou dérivants non comptés** (5.3) · **2 registres à l'ancienne numérotation** (5.4) · **1 constat d'absence faux sur la loi organique, 8 références rendues au contrôle** (5.5) |
| 5 bis | revérifier nommément les renvois de `SS/n7b_ss03`, `4_2_C` et `4_2_D` | **joué** | les 20 rangs vérifiés un à un contre la table de passage recalculée ; la table d'`APP_fiscal` est exacte, et elle est incomplète de trois renvois |
| 6 | **registre des colonnes** — un rang par pièce, aucun doublon, aucun rang orphelin | **joué** | **27 pièces sans rang**, 3 colonnes arrêtées non portées, 1 pièce de première partie classée en seconde, 1 rang périmé non barré, 2 fichiers de clause (6.1.a à e) |
| 6 bis | **chaque article abrogé a exactement un porteur** | **joué** | 0 article à zéro porteur · **2 articles à trois porteurs, non vus par `APP_fiscal`** : CGI 150 VJ et 788 (§ 6.2) |
| 7 | **suivi mensuel** — lignes datées, bouclage nul | **non joué — objet absent de la liasse** | compte **zéro**, mesuré par recherche nominative : les deux fichiers de suivi ne sont pas au projet et SS-05 n'est pas à la liasse |
| 8 | porter en réserve les cinq paramètres non arrêtés sans qu'ils arrêtent les six autres contrôles | **tenu** | § 9 ; aucun contrôle n'a été suspendu de leur fait |
| 9 | ne réécrire aucune pièce | **tenu** | 0 pièce écrite, 0 pièce touchée ; 23 corrections rendues en clair |
| 10 | n'inventer aucune adresse ni aucun montant | **tenu** | les 4 verdicts de droit rendus au § 5.5 sont relevés au dépôt, identifiants portés ; aucun montant nouveau n'est écrit |

### Récapitulation des 23 anomalies, par ordre de gravité

| rang | anomalie | ce qu'elle casse |
|---|---|---|
| 1 | **4.1** — l'exclusion du compte d'épargne et du tarif des droits de mutation manque au II de la clause | la clause abroge le compte d'épargne personnel le jour de son entrée en vigueur |
| 2 | **5.5** — constat d'absence faux sur la loi organique, 6 pièces et 1 état | 8 références laissées hors contrôle sans raison ; la porte de rattachement de 6 pièces n'est pas vérifiée |
| 3 | **6.2** — CGI 150 VJ et 788 ont trois porteurs | double abrogation du même article à la même date |
| 4 | **3.1** — les 3 amendements de `coll_P2_02` n'ont ni montant, ni tableau AE/CP, et portent un texte au dispositif | trois amendements non déposables |
| 5 | **5.3** — 3 renvois morts ou dérivants à `4_2_A` et `n7b_m022` | deux renvois résolvent sur un autre article que celui visé |
| 6 | **2.1** — le registre gage les certificats d'énergie sur une niche nommée, circuit B | règle de circuit violée au registre |
| 7 | **3.2** — les 3 divisions rendues en clair pour `etatB_04` ne sont pas appliquées | une passe annoncée n'a pas été jouée |
| 8 | **5.2** — 20 renvois rendus en clair non appliqués | tous en bloc interne, aucun amendement atteint |
| 9 | **5.4** — les deux registres à l'ancienne numérotation | 22 rangs périmés au registre des sources, 1 au registre des colonnes |
| 10 | **6.1.a à e** — 5 anomalies du registre des colonnes | 27 pièces sans rang de dépôt |
| 11 | **1.1 et 1.2** — 5 exceptions de date non inscrites, registre inexistant | la règle des dates n'a pas de dérogation tracée |
| 12 | **2.2** — `4_6` au circuit A sur pièce, au circuit B au registre | un euro dans deux circuits |
| 13 | **2.3** et **4.2** — deux contradictions d'arbitrage, non tranchées (R-F) | questions fermées n° 2 et n° 3 |

---

## 9. Réserves — les cinq paramètres non arrêtés, portés et non tranchés

Aucun n'a arrêté un contrôle ; chacun est porté tel quel, à l'auteure.

1. **Taxe spéciale sur les conventions d'assurance** — sort non arrêté ; 12 646,4 M€ mesurés
   (`annexe2!V73` + `annexe2!V165`), siège CGI art. 991, six articles satellites. Aucune pièce de
   la liasse ne la vise. `RECONCILIATION`, § 1.7 et question 1.
2. **Taxe sur les salaires** — montant mesuré 17 877,0 M€ (`annexe2!V96`) contre 16 Md€ arbitrés ;
   la pièce qui la supprime **n'est pas écrite** et son vecteur est la loi de financement. Aucune
   pièce de la liasse ne la porte. `RECONCILIATION`, § 1.1 et question 2 ; `APP_fiscal`, point 12.
3. **Prélèvements sur les jeux** — vecteur partagé entre loi de finances et loi de financement,
   non arbitré ; 11 articles relevés à `etats/U7.md`, aucun visé par une pièce de la liasse.
   `APP_fiscal`, point 7 a et question 3.
4. **Redevances sanitaires** — l'alignement « au minimum autorisé » exige l'annexe IV du règlement
   (UE) 2017/625, hors du dépôt de droit ; aucun tarif ne s'invente. 14 articles relevés.
   `APP_fiscal`, point 7 b et question 2.
5. **Péréquation de la taxe foncière** — le dispositif de `4_4` écrit **2 % + 2 %** au II du nouvel
   article L. 2336-1 ; l'arbitrage du 20261005 dit **3 points + 3 %**. Écart d'environ 5 Md€ de
   masse du fonds. `APP_fiscal`, question 1 ; `4_4`, premier point à vérifier.

**Réserves ajoutées par la présente passe, et qui ne sont pas des paramètres** : la ventilation des
lignes « autres » opérateurs (2,6 Md€), chèques (0,9 Md€) et entreprises (1,2 Md€) reste non jouée
faute de base de prorata · le relevé des cellules du classeur, treize au moins, reste dû sur tous
les fils · le relevé mécanique des renvois entrants sur les 396 rangs et sur les 364 articles des
III quater et III quinquies reste dû et appelle son propre fil.

---

## 10. Questions fermées pour l'auteure

1. **Clause générale et compte d'épargne.** Le II de la clause ne porte pas l'exclusion que son
   propre cartouche annonce et que trois pièces supposent : en l'état, la clause abroge le compte
   d'épargne personnel et le seuil de 10 000 € des droits de mutation le jour où elle entre en
   vigueur. **Écrit-on le 6° proposé au § 4.1 maintenant, par dérogation à la règle qui réserve
   les corrections de la clause à une passe dédiée — oui ou non ?**

2. **Taxes affectées, plafond à zéro.** La règle du croisement veut qu'« une taxe affectée aille à
   zéro quand bien même la taxe est supprimée ailleurs » ; l'arbitrage du lot U3 veut que le
   plafond à zéro de P1-23 se retire sur les cinquante lignes que `4_2_B` supprime, pour qu'un même
   euro ne soit pas compté au circuit A et au circuit B. **Lequel des deux l'emporte — la règle
   d'autonomie, ou le retrait des lignes de P1-23 ?**

3. **Droits de mutation, compensation des collectivités.** Le V de `4_2_C` promet aux collectivités
   une compensation « à due concurrence, par la majoration de la dotation globale de
   fonctionnement » ; le III bis du nouvel article L. 1614-1-2, créé par `coll_P1_01`, ne compense
   l'excédent que dans les conditions de l'article LO 1114-4. **Garde-t-on la formule de gage de
   `4_2_C` telle quelle — formule de recevabilité, sans portée — ou l'aligne-t-on sur le III bis ?**
