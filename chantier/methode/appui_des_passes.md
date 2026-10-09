# Appui des passes — quelle pièce s'ouvre avant quoi

**Porteur** : fil de digestion du guide de légistique, 20261007 ; **reprise du 20261007 par le fil
de consolidation (règle R-G)** ; **reprise du 20261007 par le fil de tête (règle R-H)**.
**Mandat** : l'auteure — « qu'est-ce qui permet d'assurer que l'info sera systématiquement vue
au bon moment par le bon fil ».
**Domicile** : `methode/appui_des_passes.md`.
**Mesure** : 2 pièces de référence, 7 types de passe, **2 règles transversales d'appui (R-G, R-H)**.

---

## Pourquoi ce document existe

La faute du 20261006 n'était pas une pièce manquante : la checklist était sur disque et n'a pas
été ouverte. Le verrou posé alors est l'invariant d'en-tête **Appui** — les références ouvertes
avant la passe, nommées et datées —, et une passe dont la ligne `Appui` est vide n'est pas une
passe valide.

Cet invariant dit qu'il faut nommer ce qu'on a ouvert. Il ne dit pas **ce qu'il fallait ouvrir**.
Ce document le dit. Il tient en une table, il se lit en entier, et une ligne de lancement de fil
peut le nommer seul : **le fil l'ouvre, et il sait quoi ouvrir ensuite.**

## Les deux pièces de référence, et le partage entre elles

| pièce | ce qu'elle porte | ce qu'elle ne porte pas |
|---|---|---|
| `reference/guide_legistique.md` | digestion intégrale du guide de légistique du SGG : structure d'une PPL, frontière loi/règlement, renvoi au décret, langue, formules modificatives, renvois au droit positif, entrée en vigueur, abrogations, domaine des lois financières, institution d'un prélèvement | le verbatim des textes en vigueur |
| `reference/regles_credits.md` | verbatim de onze articles de la LOLF relevé au dépôt de droit, règles d'amendement des crédits, nomenclature, gabarit d'un amendement de crédits | tout ce qui relève du guide |

Les deux ne fusionnent pas : la seconde vaut par son verbatim, et la règle R8 du classement
interdit de recopier un document qui vaut par son verbatim.

**Renvois qui résolvent sur `guide_legistique.md`** : `guide_legistique`, `structure_ppl`,
`guide_redaction`, `guide_domaine_financier`.
**Renvoi qui résout sur `regles_credits.md`** : `guide_budgetaire`.

## La table

Chaque passe ouvre ce que sa ligne nomme, et l'inscrit à son invariant `Appui`. Une passe dont
l'appui est incomplet se marque et se rejoue ; elle ne se verse pas.

| type de passe | appui dû |
|---|---|
| **toute passe, quel que soit son type** | **les états des fils qui ont tourné sur la même matière le même jour — règle R-G ci-dessous** ; **et l'objet lui-même, mesuré avant correction — règle R-H**. Ces deux lignes s'ajoutent à celle du type de passe, elles ne la remplacent pas |
| **rédaction d'une disposition normative** (cible, modificative, clause) | `guide_legistique` parties I à IV + `redaction-legistique/references/regles_redactionnelles.md` + le texte en vigueur relevé à l'extrait |
| **amendement de crédits, état B** | `regles_credits` + `guide_legistique` partie V |
| **test de rattachement d'une mesure à un véhicule financier** | `guide_legistique` partie V + `paquet/…/procedures/domaine_lfss_LO111-3.md` + `paquet/…/procedures/test_rattachement.md` |
| **recherche d'un vecteur, adresse de droit** | le dépôt de droit + `paquet/…/procedures/procedure_vecteurs.md` |
| **exposé sommaire d'amendement** | `paquet/…/procedures/gabarit_expose_sommaire.md` |
| **exposé des motifs d'une proposition de loi** | `guide_legistique` partie I |
| **contrôle de sortie avant dépôt** | `methode/controle_avant_transmission.md` + `guide_legistique` partie IV + `regles_redactionnelles.md`, ligne à ligne |

## R-G — Les fils frères du même jour

> **R-G — Un fil ouvre les états des fils qui ont tourné sur la même matière le même jour, avant
> sa passe, et les nomme à son `Appui`.** La table « type de passe → appui dû » ne les connaît
> pas : le parallélisme les crée après qu'elle a été écrite. Un fil qui déclare une pièce non
> jouée sans avoir ouvert ces états rend un constat faux.

**Les deux fautes qui la fondent, toutes deux du 20261007.**

1. **Le fil fiscal a déclaré dix pièces bloquées.** Cinq avaient leurs divisions corrigées rendues
   en clair dans un état écrit deux heures plus tôt, qu'il n'a pas ouvert. La seconde passe du même
   fil, cet état ouvert, a écrit cinq pièces.
2. **Le fil de croisement a rendu vingt-trois anomalies sans ouvrir le CR de consolidation ni
   l'état d'application des corrections.** Quatre de ses constats en sortent faux ou incomplets,
   dont un sur les dates d'abrogation de deux articles, où l'anomalie réelle est plus lourde que
   celle qu'il décrit.

**Comment un fil sait quels sont ses frères.** Il relève, avant sa passe, les états du jour qui
portent sa matière — par leur domicile sous `methode/etats/`, et par le dernier état de passation
en vigueur, qui les nomme tous. **Un état postérieur à sa propre ligne de lancement compte aussi :
la ligne est écrite avant que le fil frère ait fini.**

**Ce que R-G n'impose pas.** Elle n'oblige pas à ouvrir tout ce qui a été écrit dans la journée :
le critère est **la matière**, non la date seule. Un fil qui ouvre un état de matière étrangère
perd son temps ; un fil qui n'ouvre pas celui de sa matière rend un constat faux.

## R-H — L'objet se mesure, l'état se lit

> **R-H — Une correction se mesure sur l'objet à corriger, jamais sur l'état qui le décrit.**
> Un état dit ce qu'une passe a trouvé au moment où elle l'a écrit. Il ne dit pas ce que l'objet
> porte maintenant. Avant d'appliquer une correction, le fil ouvre la pièce, le registre ou la
> cellule et vérifie que l'écart y est encore. **Un écart déjà corrigé se constate et se raye ;
> il ne se corrige pas deux fois.**

**La faute qui la fonde, et elle est du 20261007 au soir.** Trois fils lancés en parallèle sur des
périmètres disjoints ont trouvé, chacun, qu'une part de leur mandat était déjà faite : trois
anomalies sur cinq pour le fil des pièces — dont quatorze renvois sur vingt déjà appliqués —, trois
sur neuf pour le fil des registres, l'ensemble du registre des sources de gage étant déjà juste. Le
mandat venait d'un état exact à l'heure où il a été écrit, et périmé à l'heure où il a été exécuté.

**R-G et R-H ne disent pas la même chose, et aucune ne remplace l'autre.** R-G protège du fil
frère qu'on n'a pas lu ; R-H protège de l'état qu'on a lu et qui a vieilli. Le parallélisme crée
les deux risques, et il ne se corrige que par les deux ensemble.

**Conséquence sur la mesure d'ouverture.** La mesure d'entrée d'un fil de correction porte sur les
objets de son mandat, un par un, et rend trois comptes : ce qui est à corriger, ce qui l'est déjà,
ce qui ne se mesure pas. Les trois vont à la mesure de sortie, « non joué » et « déjà fait » étant
des verdicts au même titre que « joué ».

## R-I — La partition est déclarée dans la ligne de lancement

> **R-I — Deux fils ne tournent en parallèle que si leurs mandats nomment des objets disjoints,
> et chacune des deux lignes de lancement dit ce que l'autre fil tient.** Le critère de partition
> est le fichier, non la matière : deux matières voisines peuvent s'écrire dans la même pièce.

Trois fils sur objets disjoints — pièces, registres, classeur — ont tourné ensemble sans se
contredire le 20261007 au soir. Les six fils d'application du même après-midi, partitionnés par
matière et non par fichier, se sont contredits. **La partition par fichier tient ; la partition
par matière ne tient pas.**

Un fil de conversation ne compte dans aucune partition : il n'écrit rien. Il se parallélise avec
n'importe quoi. **Ce qui ne se parallélise jamais** : la régénération des exposés, qui est en
bloc, et les contrôles de sortie, qui portent sur la liasse entière.

## Quel fil pour quelle passe

Une passe ne se confie pas au même fil selon ce qu'elle touche, et la frontière n'est pas une
préférence : elle est technique.

| passe | fil | pourquoi |
|---|---|---|
| lire, écrire ou restaurer une pièce du coffre | **Cowork** | un fil Claude Code n'a aucun accès au projet, et `restaurer.py` travaille sur le transcript d'une session qui l'a lu |
| **relever le droit en vigueur pour une passe qui touche une pièce** | **Cowork** | le dépôt de droit se clone depuis l'atelier Cowork, en public et sans jeton — vérifié le 20261007, millésime LEGI 20261001. Un fil Cowork a donc le coffre **et** le droit ; c'est la seule place où les deux se rencontrent, et une passe sur pièce ne se renvoie pas ailleurs faute de droit |
| éditer l'appareil, jouer les `make`, relever les empreintes, pousser | **code** | il a le dépôt du chantier sous la main, et les empreintes exigent un clone du dépôt de droit en `droit/` |
| arbitrer, trancher une question de fond | **conversation** | il ne déplie rien et ne joue aucun `make` |

**Un fil code à qui l'on demande de restaurer une pièce du projet s'arrête**, et il a raison de
s'arrêter : le constat est exact, et la faute est dans la ligne de lancement.

**Correction locale d'une pièce qui porte du verbatim.** La question n'est pas l'accès, elle est
la recopie. Une pièce dont la correction porte sur des divisions identifiées se réécrit
entièrement, avec report verbatim du reste. **Une pièce qui porte de longues énumérations — listes
nominatives d'articles, tableaux de verdicts — ne se réécrit pas pour une correction locale** :
ses divisions corrigées se rendent en clair et s'appliquent par copie d'octets, R8. Le critère est
le risque de déformation, et il se juge pièce par pièce.

## Les trois mécanismes qui portent cette table, et aucun ne suffit seul

1. **La ligne de lancement de fil** nomme la documentation à activer. C'est le mécanisme
   principal, et le seul qui agit avant que le fil ait lu quoi que ce soit. Une ligne de
   lancement qui ne nomme rien produit un fil qui n'ouvre rien.
2. **L'invariant `Appui`** de l'en-tête enregistre ce qui a été ouvert. Il ne garantit rien par
   lui-même : il rend la faute visible après coup, ce qui est déjà ce qui manquait le 20261006.
3. **`methode/index.json`** résout les renvois. Un renvoi qui ne résout pas se déclare au bloc
   `manquants` et ne meurt pas en silence.

**La conséquence pratique, et elle est la vraie réponse** : le nombre de pièces ne décide de
rien ; ce qui décide, c'est qu'une ligne de lancement nomme ce document-ci. Un fil qui ouvre
`methode/appui_des_passes.md` trouve, en une table, tout ce qu'il devait ouvrir — quel que soit
le nombre de pièces derrière. **Depuis R-G, il y trouve aussi ce que la table ne pouvait pas
connaître : les fils qui tournent à côté de lui. Depuis R-H, il sait que ce qu'il y lit a pu
vieillir entre l'écriture et l'exécution.**

---

## Reprises inscrites le 20261007 (fil d'intégration de `methode/reprise_20261007.md`, § 3)

**1 — Un contrôle dit ce qu'il n'a pas vu.** Complément à la règle de mesure : une mesure qui rend
un grand nombre d'absences suspecte l'instrument avant le texte. **Tout contrôle d'adresses rend,
à côté de son compte d'absences, le compte des références laissées hors contrôle et la raison de
chacune.** Un contrôle qui ne rend que ses absences est incomplet et se rejoue.

**2 — L'appui se nomme par la pièce qui l'indexe, non par des chemins.** La ligne de lancement
d'un fil de contrôle nomme `methode/appui_des_passes.md` et les skills, **jamais des chemins de
projet, qui bougent**. Constat du 20261007 : deux pièces nommées par chemin au mandat ne
résolvaient plus.

**3 — `impression-docx` se contredit sur le nommage.** Son § 5 prescrit un nom daté, sa règle de
résolution des renvois l'interdit. **Écart signalé, non corrigé** : la skill n'est pas éditable
depuis le coffre. Correction due au § 5, hors de ce fil.

**4 — Les reprises de légistique du même document (§ 3, points 4 à 7) sont inscrites à
`methode/regles_redactionnelles.md`**, section du 20261007 : formule de réécriture, partage
abroger/supprimer, quatre dates communes d'entrée en vigueur, règle de virgule et son symétrique.

**5 — Le dépôt de droit se clone depuis Cowork**, et le partage des fils ci-dessus est recalé en
conséquence. Les trois gestes, à inscrire à l'`Appui` d'une passe qui relève du droit :

```bash
git clone --depth 1 https://github.com/resolution-ib-dev/Resolution-2027 droit
python3 droit/droit.py etat
python3 droit/droit.py article <court> <numéro>
```

**6 — R-G, les fils frères du même jour.** Inscrite ci-dessus, à la table et à sa propre section.

**7 — R-H et R-I, inscrites le 20261007 au soir par le fil de tête.** R-H : l'objet se mesure,
l'état se lit. R-I : la partition se déclare, et elle se fait par fichier et non par matière.
Les trois règles R-G, R-H et R-I se tiennent et répondent au même défaut — le parallélisme — par
trois côtés différents : ce qu'on n'a pas lu, ce qu'on a lu trop tard, ce qu'un autre écrit en
même temps.

**8 — Écart de mesure levé.** Deux états du 20261007 lisaient « 43 textes » et « 62 textes » à la
même sortie de `droit.py etat`. Rejoué : **62 textes**, millésime LEGI 20261001.

---

## Reprises inscrites le 20261008 (fil de reprise, sur `methode/passation_relecture_export_20261008.md`, § 4)

**Mesure d'entrée, R-H.** Les quatre reprises dues ont été mesurées sur le présent document avant
écriture : **deux y étaient déjà inscrites et se rayent**, deux manquaient et sont écrites ici.

- **Déjà inscrite** — « un contrôle d'adresses rend, à côté de son compte d'absences, le compte des
  références laissées hors contrôle et la raison de chacune » : c'est la reprise 1 du 20261007
  ci-dessus. Le complément mesuré du 20261007 — 409, 327, 31, 20 puis 2 absences, toutes des
  défauts d'extracteur — la confirme et ne la change pas.
- **Déjà inscrite** — la contradiction de nommage de la skill `impression-docx`, § 5 : c'est la
  reprise 3 du 20261007 ci-dessus. **Toujours non corrigée**, la skill n'étant éditable ni depuis
  le coffre ni depuis un fil Cowork.

**9 — La virgule de coordination : la règle ne se restreint pas, c'est la passe qui est
incomplète.** Le contrôle de sortie de la skill `impression-docx` refuse les 213 occurrences de
virgule devant une conjonction relevées aux trois liasses, dont la typographie a été déclarée
validée en phase 3 ter. **Le contrôle a raison** : la règle du corpus
(`methode/regles_redactionnelles.md`, et sa confirmation par la fiche 3.3.1 du guide de légistique)
interdit la virgule devant **et, ou, mais, ni, car, or, donc**, sans restriction à « ni ». La
phase 3.B n'a traité que « ni », et sept occurrences seulement. **Ce qui est dû est une passe de
lecture, non une modification de la règle** : chaque occurrence se lit avant correction, la clôture
d'incise étant l'exception inscrite, et son symétrique — la virgule due lorsqu'elle clôt une incise
ouverte avant la conjonction — se contrôle dans la même passe. **La question Q3 est close à tort et
se rouvre à ce titre.**

**Mesure du 20261008, les trois liasses** : **213 occurrences** — 12 devant « ni », 195 devant
« et », 5 devant « ou », 1 devant « donc » ; 0 devant « mais », « car » et « or ». Les douze
« ni » survivent aux sept retirées en phase 3.B.

**10 — Un contrôle d'impression dit ce qu'il ne cherche pas, et un compte de sauts n'est pas un
compte de pages.** Deux défauts mesurés à l'export du 20261008 :

- **Le motif `*Forme*` s'ajoute aux onze motifs de fuite de bloc interne.** Le contrôle déclarait
  0 fuite sur onze motifs ; une note de forme a été imprimée au texte déposable de SS-01, entre le
  dispositif et l'exposé sommaire. **Un contrôle de fuite nomme ses motifs, et un motif absent de
  la liste n'est pas une absence de fuite.**
- **Le compte des blocs `\newpage` et le compte des pages imprimées sont deux mesures
  distinctes**, et une pièce ne porte jamais l'un pour l'autre. Mesure du 20261008 : **90 blocs
  `\newpage`** pour **190 pages imprimées** sur cinq documents, dont **174 pour les trois liasses**.

---

## Reprises inscrites le 20261009 (fil de reprise, après le fil 0 de regroupement)

**La faute qui les fonde, et elle est du fil de tête, non du fil d'exécution.** La ligne de
lancement du fil 0 nommait « les dix-neuf rangs ultramarins relevés le 20261007 ». Mesure faite sur
la clause : **douze de ces rangs n'existaient plus**, supprimés le jour même avec les rangs « (Sans
objet) », et **les sept restants avaient été rétablis par l'auteure le 20261005**, au motif que ces
niches profitent à des contribuables qui ne résident pas outre-mer. L'exclusion que le mandat
demandait d'écrire au II **y était déjà**, avec la réserve de domicile qui maintient ces sept rangs
dans le champ du I.

**Trois défaillances empilées, et seule l'auteure a arrêté la chaîne.**

**R-V — Un compte repris d'un état se date, et se remesure sur l'objet avant d'être inscrit à un
mandat.**

> Un mandat qui porte un chiffre — un compte de rangs, de pièces, d'occurrences — **nomme l'état
> d'où il vient et sa date**, et le fil qui l'exécute **le remesure sur l'objet avant d'écrire**.
> Une divergence entre le compte annoncé et le compte mesuré **arrête le fil**.

C'est R-H appliquée à celui qui écrit le mandat, et non plus seulement à celui qui l'exécute. Le
compte de dix-neuf venait d'un état exact à l'heure où il a été écrit et périmé une heure plus tard
par une renumérotation. **Il a traversé l'arbitrage, la procédure et le suivi sans que la clause
soit ouverte une seule fois.** R-H protège le fil d'exécution ; R-V protège la ligne de lancement.

**R-W — L'extension d'une décision de l'auteure se pose en question, elle ne s'inscrit pas.**

> Une décision de l'auteure vaut **pour les objets qu'elle nomme**. L'étendre à d'autres est une
> proposition, et une proposition **se pose en une question fermée** ; elle ne s'inscrit jamais au
> nom de l'auteure.

« On sort l'outre-mer » répondait à une question sur deux pièces. Inscrit comme valant « pour tout
le dépôt », l'arbitrage abolissait sept rangs que l'auteure avait elle-même rétablis quatre jours
plus tôt. **C'est le garde-fou du registre : ce que l'auteure a dit va au bloc validé, ce que le
fil propose va au bloc proposé.** Il ne souffre pas d'exception, et surtout pas quand l'extension
paraît évidente.

**Rappel, et il n'appelle pas de règle neuve.** La règle de mesure du corpus est déjà catégorique :
*si la mesure ne trouve pas l'objet annoncé, le fil rend le nombre mesuré et s'arrête
immédiatement.* Le fil 0 a bien mesuré, bien rendu la contradiction — réserve de domicile au II
d'un côté, retrait des rangs au III de l'autre — **et a annoncé qu'il continuait**. Il devait
s'arrêter. **Une contradiction rendue n'est pas une contradiction traitée**, et rendre en continuant
n'est pas rendre.

**11 — Un contrôle lit le registre qui enregistre ce qu'il relève, et la clôture de la question
qu'il rouvre.** Deux signalements du fil 1 du 20261009 sont tombés à la mesure, et les deux défauts
proposés auraient introduit une faute :

- **deux dates déclarées hors registre y étaient inscrites** depuis le 20261008 ter — le contrôle
  de conformité ne lit pas `livrables/registre_exceptions_dates.md`. Le défaut « les inscrire »
  aurait créé deux lignes en double ;
- **une adresse déclarée à retirer était juste** — l'article 721 du code général des impôts est
  absent du droit en vigueur **parce que le texte déposé le rétablit**, et c'est l'article rétabli
  que la pièce supprime. La question était close sur ce motif le 20261008. Le défaut « retirer
  l'adresse » aurait cassé la lecture de la pièce.

> **Un contrôle qui relève une exception lit d'abord le registre qui l'enregistre. Un contrôle qui
> rouvre une question lit d'abord sa clôture.** Un signalement qui ignore l'un ou l'autre n'est pas
> un écart : c'est un défaut du contrôle, et il se corrige au contrôle.

C'est R-H vue du côté de l'instrument : l'objet se mesure, et **le registre fait partie de
l'objet**.
