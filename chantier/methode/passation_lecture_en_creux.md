# Passation — divisions du PLF, lecture en creux, fourchettes, domaine de la loi Sécu

**Sas ouvert le 20260902.** Fil de production. Il n'a pas touché `methode/`
hors ce document et la ligne d'inscription à `methode/sas.md`, il n'a pas joué
`make coffre`, et il n'a rien versé au corpus. Ce qu'il a fabriqué attend son
absorption.

Les sept fichiers sont à `technique/depot_lecture_en_creux.txt`, au format
d'archive de `appareil/coffre.py`. **Portés en entier et non en correctif** :
cinq ancres, dont une de quarante lignes, recopiées à la main sont un risque de
transcription que le dépliage prouvé écarte à coût nul — A-283 lu avec le point 1
de `methode/sas.md`.

---

## 1. Preuve de dépliage

Dépôt déplié dans un répertoire temporaire vierge, SHA-256 de chaque fichier
comparé à l'original. **Sept sur sept identiques.**

```
python3 appareil/coffre.py deplier technique/depot_lecture_en_creux.txt /tmp/preuve
7 fichier(s) dépliés
OK    appareil/socle_plf_texte.py
OK    appareil/plages_articles.py
OK    appareil/lecture_en_creux.py
OK    appareil/portes_domaine_lfss.py
OK    appareil/controle_index.py
OK    Makefile
OK    .gitignore
```

Dépôt : `d642585fdd1dc0d1f8d3bdbf0a3ab346709f2da44ca86853e2f49f70bbeb2cce`,
142 479 o, 3 081 lignes.

---

## 2. Entrées de registre — titrées et datées, sans numéro

Le fil de réconciliation numérote à l'insertion (A-282). Les renvois entre ces
entrées sont relatifs et se signalent par leur titre ; les renvois vers le
registre existant portent leur numéro.

### Les parties et titres du PLF se relevaient, et la cause n'était pas celle qu'on présumait — 20260902

**Relevé.** `divisions_attendues` était épinglé à 0 au profil `plf`, et A-294
avait requalifié l'explication en défaut de repère présumé faute de la pièce.
La pièce est entrée. Le balayage de la zone d'extraction, pages 30 à 256, pour
**toute ligne contenant « PARTIE » ou « TITRE »** rend **six lignes, et six
seulement**.

Des deux causes candidates d'A-294, **la première est écartée** : le PLF n'écrit
jamais « TITRE Ier ». Il écrit `TITRE PREMIER` et `TITRE II`, en capitales, que
`DIVISION_TITRE` acceptait déjà — c'est le PLFSS qui écrit « TITRE IER », et son
profil marchait. **La seconde est confirmée, et seule** : les deux expressions
se terminent par `$` et exigent la ligne pleine, quand le PLF compose la tête
**et son intitulé sur la même ligne**, séparés par un deux-points.

Le relevé ajoute un troisième fait que la cause 2 ne couvrait pas : page 210,
`TITRE II:` **sans espace avant le deux-points**. Un motif écrit `\s+:` aurait
manqué une division sur six.

La correction est une queue d'intitulé optionnelle exigeant le deux-points, et
une fonction `tete_division` qui rend le couple tête / intitulé. Le deux-points
est celui de la pièce, jamais une ponctuation de notre cru : `partie` porte
« PREMIÈRE PARTIE », `partie_intitule` porte « CONDITIONS GÉNÉRALES DE
L'ÉQUILIBRE FINANCIER ». `divisions_attendues` passe de 0 à **6**.

**Après correction, 81 des 82 articles du PLF portent leur partie et leur
titre.** Les deux tables plates des articles ouverts restent identiques à
l'octet, et les dix contrôles passent sur les deux pièces, zéro échec.

### Le critère « chaque article porte sa division » ne tient pas, et l'article liminaire dit pourquoi — 20260902

**Relevé.** Le prompt du fil demandait de vérifier que *chaque* article du PLF
porte désormais sa partie et son titre, un article sans division valant échec.
Ce critère n'est pas atteignable, et pas seulement au PLF.

L'article liminaire du PLF est page 31 ; `PREMIÈRE PARTIE` ouvre page 34. **Le
liminaire précède la première partie** — il n'en porte aucune, et c'est juste en
droit. Le même critère échoue déjà sur le PLFSS, **où le mécanisme fonctionne**
depuis le 20260901 : un article sans partie, le liminaire, et **quatre sans
titre de division** — liminaire, 1er, 2 et 3 —, parce que la `PREMIÈRE PARTIE`
du PLFSS ne porte pas de titre.

**Critère retenu, et il est mécanique** : le seul article du PLF sans division
est le liminaire, nommément. Un article non liminaire sans partie est un échec.
Le compte au socle : 82 articles, 1 sans partie, 1 sans titre de division, tous
deux le liminaire.

### Les cinq fourchettes se déplient au dépôt de droit, et douze adresses passaient pour fermées à tort — 20260902

**Relevé.** Cinq lignes de la table du PLF visent une plage et non un article, et
la table les comptait sur leur borne basse seule. Les articles réellement
présents dans les intervalles se relèvent sur le code, à sa source : le dépôt de
droit porte `cibs` et `cgct`, les deux codes concernés.

**22 articles relevés sur les cinq plages, dont 12 intérieurs** — douze adresses
qu'une mesure pouvait viser et que la jointure comptait fermées. Aucun manque :
les cinq plages se déplient, bornes retrouvées.

L'ordre des numéros d'article ne se déduit ni d'une chaîne ni d'un entier :
« L. 421-79-1 » suit « L. 421-79 » et la plage `L. 421-77 à L. 421-79-1`
s'arrête sur un article suffixé. La clé est le découpage du numéro en suites de
chiffres et de lettres, un tuple plus court valant préfixe donc moins. **La
convention est déclarée au module**, elle n'est pas une propriété du code.

**Le module ne réécrit pas la table des articles ouverts** et ne remonte rien au
socle. Il rend le relevé ; la jointure est ailleurs.

### Trois articles de fourchette sur vingt-deux portent une abrogation déjà votée, et une plage entière est dans ce cas — 20260902

**Relevé au dépôt de droit, millésime LEGI 20260901.** Sur les 22 articles des
cinq plages, **8 sont à l'état `ABROGE_DIFF`** — abrogation votée, pas encore
entrée en vigueur — et 14 en `VIGUEUR`. Ils ne se répartissent pas au hasard :

- `L. 314-13 à L. 314-18` du code des impositions sur les biens et services —
  5 des 8 articles, les cinq premiers de la plage ;
- `L. 421-120 à L. 421-122` du même code — **les trois articles, soit la plage
  entière**.

Un amendement qui viserait un de ces huit articles viserait un texte dont la
disparition est déjà décidée. **Ce n'est pas une faute du relevé, c'est une
information à porter au choix du siège**, et `vecteur-mesure` ne la voit pas
aujourd'hui.

### La lecture en creux rend cinq relevés, et la troisième colonne du trois colonnes n'en est pas un — 20260902

**Relevé.** A-230 nomme six dispositifs. Cinq se calculent sur le socle sans
rouvrir le PDF ; le sixième — les amendements déposés — demande une pièce hors
corpus et n'est pas fait.

Ce que les cinq rendent, recompté sur les deux socles au moment de l'écrire :

| | PLF 2026 n° 1906 | PLFSS 2026 n° 1907 |
|---|---|---|
| mots de portée, liste fermée de 6 | 264 occurrences | 271 |
| dates, 3 familles | 71 | 47 |
| absences attendues, 4 tests | 63 signaux | 29 |
| montants annoncés à l'exposé sans contrepartie à la rédaction | 45, sur 17 articles | 48, sur 20 articles |
| texte en vigueur relevé en regard de la disposition | 277 adresses sur 406 | 109 sur 216 |

**La troisième colonne du dispositif trois colonnes n'est pas rendue, et c'est
une limite déclarée.** Texte en vigueur et disposition se relèvent à l'octet —
l'un au dépôt de droit, l'autre au socle. Le **texte résultant** suppose
d'appliquer la modification : c'est un acte de légistique, le travail de
`redaction-legistique`, et `Constitution_3col` comme `LOLF_3col` ont été
composés à la main. Le fabriquer par script serait inventer du droit.

Les deux listes fermées sont celles d'A-230 et rien de plus — six mots de portée,
quatre tests d'absence. **Elles s'étendent par arbitrage, jamais par
intuition** : un mot ajouté de notre cru ferait passer un choix de lecture pour
un relevé.

### La grille du domaine de la loi de financement rend trente et une portes, et l'axe de transparence en a trois — 20260902

**Relevé en verbatim au dépôt de droit**, millésime LEGI 20260901, chaque porte
avec son identifiant `LEGIARTI` et sa date de version. Même règle que
`portes_domaine.py` : le module ne porte que des repères, le texte est découpé à
l'octet, un repère qui ne mord pas fait sortir la porte en échec déclaré. **31
portes, 0 échec.**

Construite sur la série, jamais sur `LO 111-3` : `LO 111-3-6` à `-3-8` pour les
portes utiles, `-3-14` à `-3-16` pour les monopoles, plus le cadre — `LO 111-3`
pour la définition, `-3-1` et `-3-2` pour la structure, `-3-3` à `-3-5` pour
l'obligatoire, `-3-18` pour la reprise. Répartition : 15 facultatives,
9 obligatoires, 4 monopoles, 1 définition, 1 structure, 1 reprise.

Cinq choses que le relevé apprend et que le corpus ne portait pas :

- **Trois parties, et trois portes de transparence** — une par partie, aucune
  avec condition d'équilibre. L'axe de transparence a **trois entrées au PLFSS
  contre deux au PLF**, et le choix de la partie suit l'objet.
- **La porte de dépenses change de largeur selon la partie** : sans réserve en
  première partie, mais l'effet doit affecter **directement** l'équilibre en
  troisième. Une même mesure n'a pas le même coût de plaidoirie selon
  l'exercice qu'elle vise.
- **`LO 111-3-8` 2° est la porte des mesures de structure sur les caisses** —
  organisation et gestion interne, sous condition d'objet ou d'effet sur
  l'équilibre général, et elle est en **troisième** partie. C'est la porte à
  citer pour les organismes de sécurité sociale du chiffrage.
- **Le monopole de `LO 111-3-16` est une arme, pas une porte.** Il ne fait
  entrer aucun amendement : il établit qu'un allègement de cotisations porté par
  un autre véhicule est attaquable. Il relève de la contestabilité.
- **`LO 111-3-18` est un argument de rattachement écrit dans le texte** : toute
  mesure prise ailleurs qui pèse sur les comptes sociaux doit être reprise à la
  loi de financement suivante. Il ne se plaide pas, il se cite.

**Deux manques déclarés et non comblés.** `LO 111-4` et `LO 111-4-1` — les
annexes obligatoires, pendant de l'article 51 de la LOLF et **siège de toute
obligation documentaire nouvelle au PLFSS** — ne sont pas relevés : le choix
entre une annexe opposable et un rapport appartient à l'auteur, comme au PLF. Et
`LO 111-3-9` à `-3-13`, qui traitent des lois rectificatives et de la loi
d'approbation des comptes, sont hors du PLFSS de l'année.

**Le croisement des deux grilles n'est pas fait.** Trois portes de la grille Sécu
renvoient au III de l'article 2 de la LOLF : une mesure d'affectation entre
l'État et la sécurité sociale se qualifie sur **deux** grilles à la fois.

### Cloner le dépôt de droit dans l'atelier faisait sortir I2, et le corpus prescrivait ce geste — 20260902

**Relevé.** `reference/depot_droit.md` écrit `git clone … droit`, dans
l'atelier. Le faire fait sortir **`I2` à 15** : `droit/` n'était ni au
`.gitignore` ni aux `IGNORES` de `controle_index.py`. **La procédure que le
corpus prescrit cassait un contrôle que le corpus tient.**

Corrigé aux deux endroits. Le fil a par ailleurs travaillé avec le dépôt cloné
hors atelier, et la variable `DROIT` du `Makefile` accepte les deux formes.

### `I1` n'est pas un invariant du corpus, et son épinglage à 28 ne se reproduit pas — 20260902

**Relevé.** L'état d'ouverture annoncé au prompt de ce fil donnait « I1 = 28,
régime établi ». Mesuré à l'atelier nu : **31**. Mesuré une fois les deux socles
du texte régénérés : **25**.

`I1` compte les chemins que l'index déclare et que le dépôt ne porte pas ; les
31, puis 25, sont **tous** des dérivés et des référentiels qui se régénèrent.
`I1` mesure donc ce qu'un fil a régénéré, pas ce que le corpus porte. **Sa
valeur ne se compare qu'à périmètre identique**, et l'annoncer comme un compte
d'ouverture invite à chercher un faux qui n'existe pas. `I2` à `I5` sont, eux,
des invariants.

---

## 3. Bloc de journal

```markdown
## 20260902 — Les divisions du PLF, la lecture en creux, les fourchettes et le domaine de la loi Sécu

**Le défaut des divisions du PLF est corrigé, et le relevé a écarté la cause
qu'on présumait.** Le balayage de la zone d'extraction pour toute ligne portant
« PARTIE » ou « TITRE » rend six lignes, et six seulement. Le PLF n'écrit pas
« TITRE Ier » : il écrit `TITRE PREMIER` et `TITRE II`, en capitales, que le
motif acceptait déjà. Ce qui bloquait est la seule exigence de ligne pleine, la
pièce composant la tête et son intitulé sur la même ligne, séparés par un
deux-points — et une fois « TITRE II: » sans espace. `divisions_attendues` passe
de 0 à 6 au profil `plf`. **81 des 82 articles portent désormais leur partie et
leur titre** ; le seul sans division est l'article liminaire, qui précède la
première partie. Les deux tables plates des articles ouverts sortent identiques
à l'octet et les dix contrôles passent sur les deux pièces.

**Les cinq fourchettes du PLF sont dépliées, et douze adresses passaient pour
fermées à tort.** 22 articles relevés au code à sa source, aucun manque. Huit
des 22 portent une abrogation déjà votée, dont une plage entière — trois
articles sur trois. Un amendement qui viserait ces huit viserait un texte dont
la disparition est décidée.

**Les cinq relevés de lecture en creux d'A-230 existent**, sur les deux socles :
mots de portée, dates, absences attendues, montants confrontés entre rédaction
et exposé des motifs, texte en vigueur en regard de la disposition. La troisième
colonne du dispositif trois colonnes — le texte résultant — n'est pas rendue et
se déclare pour ce qu'elle est : un acte de légistique, non un relevé.

**La grille du domaine de la loi de financement est écrite**, sur la série
`LO 111-3-6` à `-3-8` et `-3-14` à `-3-16`, jamais sur `LO 111-3`. 31 portes en
verbatim, 0 échec de relevé. L'axe de transparence y a trois entrées, une par
partie, contre deux au PLF ; la porte des mesures de structure sur les caisses
est en troisième partie ; le monopole sur les exonérations de cotisations est
une arme de contestabilité et non une porte d'entrée. Les annexes obligatoires
— `LO 111-4-1`, pendant de l'article 51 — sont déclarées non relevées : le choix
entre annexe opposable et rapport appartient à l'auteur.

**Deux corrections d'appareil.** `droit/` entre au `.gitignore` et aux
`IGNORES` de `controle_index.py` : suivre la procédure écrite à
`reference/depot_droit.md` faisait sortir `I2` à 15. Et `I1` cesse d'être
annoncé comme un compte d'ouverture — il vaut 31 à l'atelier nu, 25 les socles
régénérés, et il mesure le périmètre d'un fil, pas l'état du corpus.

**Aucun versement au corpus.** Sept fichiers au sas
`technique/depot_lecture_en_creux.txt`, dépliage prouvé sept sur sept.
```

---

## 4. Entrées d'index

Dix artefacts, à porter à la table de `appareil/generer_index.py`. Les sept
fichiers du dépôt qui existent déjà à l'index n'y changent que leur empreinte.

| role | chemin | rang | coffre | chemin_coffre | produit_par | consomme_par | famille |
|---|---|---|---|---|---|---|---|
| `plages_articles_gen` | `appareil/plages_articles.py` | appareil | true | `technique/coffre.txt` | — | `make`, préparation des amendements | outillage |
| `lecture_en_creux_gen` | `appareil/lecture_en_creux.py` | appareil | true | `technique/coffre.txt` | — | `make`, lecture en creux (A-230) | outillage |
| `portes_domaine_lfss_gen` | `appareil/portes_domaine_lfss.py` | appareil | true | `technique/coffre.txt` | — | `make`, test de rattachement, pack public | grilles |
| `plages_articles` | `referentiels/plages_articles.json` | referentiel | false | `technique/coffre.txt` | `appareil/plages_articles.py` | `portes_ouvertes.py`, `vecteur-mesure` | grilles |
| `plages_articles_releve` | `livrables/plages_articles.txt` | derive | false | `livrables/plages_articles.txt` | `appareil/plages_articles.py` | lecture de l'auteur | bac à sable |
| `lecture_en_creux_plf` | `referentiels/lecture_en_creux_plf.json` | referentiel | false | `technique/coffre.txt` | `appareil/lecture_en_creux.py` | lecture en creux, contestabilite | grilles |
| `lecture_en_creux_plf_releve` | `livrables/lecture_en_creux_plf.txt` | derive | false | `livrables/lecture_en_creux_plf.txt` | `appareil/lecture_en_creux.py` | lecture de l'auteur | bac à sable |
| `lecture_en_creux_plfss` | `referentiels/lecture_en_creux_plfss.json` | referentiel | false | `technique/coffre.txt` | `appareil/lecture_en_creux.py` | lecture en creux, contestabilite | grilles |
| `lecture_en_creux_plfss_releve` | `livrables/lecture_en_creux_plfss.txt` | derive | false | `livrables/lecture_en_creux_plfss.txt` | `appareil/lecture_en_creux.py` | lecture de l'auteur | bac à sable |
| `portes_domaine_lfss_md` | `livrables/portes_domaine_lfss.md` | derive | false | `livrables/portes_domaine_lfss.md` | `appareil/portes_domaine_lfss.py` | test de rattachement, pack public, qualification des articles | bac à sable |

**Ces dix sont exactement ce qu'`I2` sort aujourd'hui au dépôt**, ni plus ni
moins. Vérifié après correction de l'exclusion de `droit/` : `I2` = 10, et les
dix sont ces dix.

---

## 5. Règles de `Makefile`

Le `Makefile` est porté **en entier** au dépôt du sas ; les règles n'ont donc pas
à se recopier. Ce qu'elles ajoutent, pour la relecture :

- **variables** — `DROIT` (chemin du dépôt de droit *tel que vu depuis
  `appareil/`*, défaut `../droit`), `DROIT_PRESENT`, `PLAGES`, `PLAGES_TXT`,
  `CREUX_PLF`, `CREUX_PLF_TXT`, `CREUX_PLFSS`, `CREUX_PLFSS_TXT`,
  `PORTES_LFSS` ;
- **deux règles inconditionnelles** — la lecture en creux du PLF et celle du
  PLFSS, qui dépendent du socle seul. Sans dépôt de droit, leur cinquième relevé
  se déclare non joué et la cible tourne quand même ;
- **deux règles sous `ifneq ($(DROIT_PRESENT),)`** — le dépliage des fourchettes
  et la grille du domaine Sécu, qui n'ont aucun sens sans le texte en vigueur ;
- **quatre extensions de `tout`**, chacune conditionnelle à la pièce ou au dépôt
  dont elle dépend, comme les règles des socles (A-234).

`DROIT_PRESENT` teste les deux formes, `$(APP)/$(DROIT)/droit.py` et
`$(DROIT)/droit.py`, pour qu'un chemin absolu marche autant qu'un relatif.

---

## 6. Empreintes

Relevées sur les fichiers au moment d'écrire ce document, jamais reprises d'un
récit (A-283).

| fichier | SHA-256 | octets | lignes | avant |
|---|---|---|---|---|
| `appareil/socle_plf_texte.py` | `f8e7c95ac4619e8a4d587520db88adade0b74f5f98d7f0d0809d549995dc8813` | 52 914 | 1 185 | `3b9b6a444116…` · 49 948 o · 1 129 l. |
| `appareil/plages_articles.py` | `6e17998d570980524d03b391574eb1ca286db1130f7f50974ae5cdd53c644632` | 9 998 | 227 | neuf |
| `appareil/lecture_en_creux.py` | `387e623507f856d4a8a531a01ef39fbe2cd046892265a5d7aca953cb3b98df19` | 16 163 | 357 | neuf |
| `appareil/portes_domaine_lfss.py` | `b5e7722b24f65c65fd793a2f973637293a778601528873391403f875b3192e69` | 28 979 | 557 | neuf |
| `appareil/controle_index.py` | `ceafc949d6688234abe114dbb78b45c2dc71791c91e91615261fbf17d8ece0d6` | 9 461 | 210 | `b41babbce5f8…` · 9 176 o · 206 l. |
| `Makefile` | `03ce8cf7886c6a54aaa267186c4dc28fc07f9cf0a033f4dbcdb20133b2cfb855` | 22 907 | 479 | `b2ea4bedd10c…` · 20 170 o · 419 l. |
| `.gitignore` | `7500d5537907ab0aec9124b55364e2f28f88f41b626cb4d56fa189e49bc08f70` | 691 | 22 | `04a45a5cc3fa…` · 520 o · 18 l. |
| `technique/depot_lecture_en_creux.txt` | `d642585fdd1dc0d1f8d3bdbf0a3ab346709f2da44ca86853e2f49f70bbeb2cce` | 142 479 | 3 081 | neuf |

Les deux socles du texte et les deux tables plates, pour mémoire — les socles ne
se versent pas, les tables si :

| | empreinte du socle | table plate |
|---|---|---|
| PLF 2026 n° 1906 | `20eebda5a1004df8d770305b236bc319e625b158e3d574786afa2c1e8548a33c` — **changée**, les six lignes de division sortant des motifs du liminaire | `2863d12f…f2c9e9ec`, 23 061 o, 396 l. — **identique à l'octet** |
| PLFSS 2026 n° 1907 | `44eeb4b9630335d215f021702e9fe3809d704452e217885efa29265fa81f89f1` — inchangée | `8aa17c75…074f15c8b`, 11 634 o, 218 l. — **identique à l'octet** |

---

## 7. La jauge, lue à `project_info`

Jamais une prévision par somme d'octets, qui s'est révélée fausse d'un facteur
trois (A-128, A-281).

| | `knowledge_size` | marge sur 2 000 000 |
|---|---|---|
| avant écriture | **1 747 208** | 252 792 |
| après écriture | **1 804 462** | **195 538** |

Le sas a consommé **57 254** à la jauge, pour 165 556 octets de fichiers —
dépôt de 142 479 o et passation de 23 077 o. **Le rapport est de 0,35 pour un**,
et il confirme qu'une prévision par somme d'octets se trompe : elle aurait
annoncé près du triple. Le projet passe de 61 à **63 documents**.

**La marge restante est de 195 538, et le sas en rendra la totalité de sa part
à l'absorption**, puisqu'un sas absorbé se supprime.

---

## 8. Les phrases du corpus que les relevés démentent

Trois, et elles sont toutes relevées, aucune héritée.

1. **`appareil/socle_plf_texte.py`, profil `plf`** — le commentaire d'épinglage
   présumait deux causes candidates au défaut des divisions. **La première est
   fausse** : « TITRE Ier » en bas de casse n'existe pas dans le PLF. Corrigé au
   module par le présent sas.
2. **`reference/depot_droit.md`** — « `git clone … droit` », dans l'atelier.
   Le geste faisait sortir `I2` à 15. Corrigé au `.gitignore` et à
   `controle_index.py` ; **le document, lui, reste à amender** pour dire que le
   dépôt est exclu du suivi et de l'index.
3. **Le prompt de ce fil, et l'état d'ouverture qu'il annonce** — « I1 = 28,
   régime établi ». `I1` vaut 31 à l'atelier nu et 25 les socles régénérés : ce
   n'est pas un invariant, et il ne devrait pas figurer parmi les comptes
   d'ouverture à confronter.

---

## 9. Ce que ce fil n'a pas fait, et qui reste dû

- **La table des articles ouverts n'est pas réécrite.** Les cinq fourchettes y
  restent comptées sur leur borne basse, avec leur colonne `fourchette` à 1. Le
  dépliage vit à côté ; **c'est à la jointure de `portes_ouvertes.py` de le
  consommer**, et elle ne le fait pas encore. Tant qu'elle ne le fait pas, les
  douze adresses intérieures restent comptées fermées.
- **Le croisement des deux grilles de domaine** — LOLF et loi de financement —
  n'est pas fait.
- **La troisième colonne du trois colonnes** n'est pas rendue, et ne le sera pas
  par un script.
- **L'état `ABROGE_DIFF` n'est pas remonté à `vecteur-mesure`** : la skill ne
  voit pas qu'un siège porte une abrogation déjà votée.
- **Les amendements déposés**, sixième dispositif d'A-230 et « meilleur
  correcteur disponible » selon lui, demandent une pièce hors corpus.
- **`methode/prompt_fil_courant.md`, `methode/procedure_contre_plf.md` et
  `CLAUDE.md` ne sont pas touchés.** Les points 2, 4 et 5 de la liste « ce qui
  reste dû » du bloc du 20260902 au fil courant sont faits par ce sas, et c'est
  au fil de réconciliation de le dire là-bas.
