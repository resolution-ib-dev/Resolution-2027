# Digestion des archives — vérification du 20260921

*Fil de vérification. Il n'a digéré, réécrit ni retiré quoi que ce soit. Le
retrait est une action d'interface, à la main de l'auteur.*

---

## Les trois verdicts

| pièce | verdict |
|---|---|
| `archive/Reserve_arguments_20260806_v1.html` | **à garder** — 163 unités `absente` sur 167 |
| `archive/Input_gagnants_perdants_20260820_v1_brouillon.html` | **à garder** — 12 unités `absente` sur 51 |
| `methode/arbitrages_archive.md` | **copie unique** — ne se retire pas |

---

## Ce que « digérée » a voulu dire ici

Le prompt pose les trois cases et laisse leur frontière ouverte sur une unité
qui porte plusieurs éléments. *Tranché par Claude au titre d'A-23* :

- `digérée` — l'énoncé se retrouve tel quel, ou à la valeur près, dans une
  pièce vivante nommée ;
- `reformulée` — le fond se retrouve sous une autre forme, ou sous une autre
  valeur qui l'a remplacé ;
- `absente` — **une unité qui porte plusieurs éléments est classée sur celui qui
  manque.** Un fait, un chiffre, un exemple nommé, une affirmation sont des
  éléments ; une image ou une tournure n'en sont pas.

C'est la lecture qui sert la règle de l'auteur — *on garde une archive tant que
son contenu n'est pas digéré ailleurs* — puisque le contenu d'une réserve
d'arguments, ce sont précisément ses exemples nommés. La table dit, pour chaque
`absente`, ce qui d'elle est par ailleurs digéré.

## Le corpus vivant interrogé

`manuscrit/manuscrit.html` · `referentiels/REF_doctrine.json` ·
`referentiels/notes_manuscrit.json` · les 89 modules d'`appareil/` du dépôt,
dont `construire_positions.py`, `justifications.py`, `apports.py` et
`structure_fiches.py`, qui portent la matière écrite à la main du référentiel
des positions · le `Makefile`.

`referentiels/positions.json` n'est ni au coffre ni au dépôt : il se régénère
depuis `REF_doctrine` et les trois modules ci-dessus, qui ont donc été lus à sa
place. Les livrables `extrait_gagnants_perdants.html`,
`inventaire_gagnants_perdants.html` et `galerie_fiches.html` sont des dérivés de
ces mêmes pièces : les interroger serait les interroger deux fois.

**Trois passes mécaniques, et la recherche n'a pas été faite à l'œil** :
5-grammes littéraux sur le texte normalisé ; trigrammes de mots pleins ;
co-occurrence des deux termes les plus rares de chaque unité dans une fenêtre de
500 caractères. Ce que ces passes ont sorti a ensuite été lu une à une.

---

## Pièce 1 — `archive/Reserve_arguments_20260806_v1.html`

### Verdict : à garder

167 unités. **3 `digérée`, 1 `reformulée`, 163 `absente`.**

Ce résultat est cohérent avec ce que la pièce déclare d'elle-même : son critère
de sélection était la **nouveauté** — au moins trois dixièmes du vocabulaire
distinctif absent du corpus doctrinal au 20260806. Les unités y sont entrées
parce qu'elles n'étaient pas au corpus, et rien ne les y a fait entrer depuis :
le travail des cinq dernières semaines a porté sur le budgétaire, la norme et la
légistique, pas sur l'argumentaire.

### Les quatre unités retrouvées

| unité | case | où elle se retrouve |
|---|---|---|
| `R-ARG007` — refontes historiques de l'État, plans de 1926, 1938, 1958 | `digérée` | manuscrit, prologue « Pourquoi nous croire ? » : « les trois plans de redressement que la France a connus en 1926, 1938, et 1958 » ; note e3, qui les nomme un par un |
| `R-ARG008` — « Ce que la démocratie a fait, elle peut le défaire » ; 1793, 1940 | `digérée` | manuscrit, prologue « Comment faire ? », littéralement ; et « Pourquoi ne pas se résigner ? » pour la Terreur de 1793 et 1940 |
| `R-ARG020` — trop d'État a tué l'État, partout donc nulle part | `digérée` | manuscrit, titre de section P1-C4 « Trop d'État tue l'État » ; P2-C1 « en s'occupant du superflu, l'État a failli sur l'essentiel » |
| `R-ARG066` — 100 Md€/an d'économie sur 1 700, reversés ~300 €/mois au salaire médian | `reformulée` | manuscrit P2-C4 : 236 Md€ sur 1 714 Md€, et « 300 euros nets par mois » au salarié type. Même fond, valeur remplacée |

### Ce que les `absente` portent quand même, en partie

Quatre cas où une part de l'unité se retrouve et où c'est l'exemple nommé qui
manque — ils sont dits parce qu'ils sont les plus proches de la digestion, et
qu'ils restent `absente` :

- `R-ARG006` — l'image des épaules de géants est au manuscrit (épigraphe P3-C4,
  Newton), La Boétie et Voltaire y sont ; **Kant et l'hommage aux inventeurs de
  l'imprimerie, nulle part**.
- `R-ARG011` — la figure « et nous ne pourrions pas… » est à l'épilogue ; **Nancy
  Wake, Madeleine Riffaud, Geneviève de Gaulle et Lucie Aubrac, nulle part**.
- `R-OBJ014` — 1926, 1938, 1958 sont au manuscrit ; **la Suède 1990, la
  Nouvelle-Zélande 1984, le Canada 1994 et les pays de l'Est, nulle part**.
- `R-OBJ043` — la faillite des deux tiers de 1797 et « une quinzaine de
  dévaluations depuis Clovis » sont au prologue ; **Saint Louis, Philippe le Bel,
  François Ier, le système de Law, les assignats et les 45 centimes de 1848,
  nulle part**.

### Un fait qui n'est pas une case, et qui pèse sur le retrait

`appareil/relever_protos.py`, module vivant joué à la chaîne, **prend cette pièce
en entrée** : il découpe les protos rédigés en phrases chiffrées et les confronte
au référentiel des faits, pour sortir les collisions, la veille et les chiffres
hors référentiel. Son en-tête nomme « une réserve d'arguments » dans sa liste
d'entrées, et son usage lit `../sources/*.html`. La retirer retire une entrée à
un contrôle en service.

A-128 avait déjà posé la question du retrait de cette pièce — 92 ko, la plus
lourde des gelées — et A-6 y répondait : *une gelée que rien ne sait refaire ne
se supprime pas.*

---

## Pièce 2 — `archive/Input_gagnants_perdants_20260820_v1_brouillon.html`

### Verdict : à garder

52 unités, dont une sans contenu. **39 `digérée`, 12 `absente`.**

La dérivation systématique du 20260820 a bien digéré la matière : les catégories
de l'input se retrouvent nommées au bloc `CATEGORIES` de `construire_positions.py`,
avec leur définition, leur effectif et leur source. Deux unités y sont même
citées comme venant de l'input : `C-38` porte « input brouillon : environ 12 %
des élus, non instruit », et la ligne de l'agent public porte « Fin de l'emploi à
vie. Perte nommée à l'input brouillon, absente du référentiel. »

### Table des unités

| unité | case | où elle se retrouve |
|---|---|---|
| G-01 État concentré, 7 missions | `digérée` | manuscrit P2-C1 ; REF_doctrine `D2-1` |
| G-02 travail mieux rémunéré, y compris pour les inactifs | `digérée` | manuscrit P1-C2 « actif ou inactif » ; REF_doctrine `D3-2` |
| G-03 à une génération, État plus riche, recettes plus élevées en euros et plus faibles en proportion | **`absente`** | le manuscrit ne porte que la baisse de l'IS quand les recettes remontent ; l'énoncé et son horizon, nulle part |
| G-04 forte réduction du risque de crise | `digérée` | manuscrit épilogue ; REF_doctrine `D11-ed7` ; `justifications.py` |
| G-05 compte épargne régulièrement alimenté | `digérée` | manuscrit P2-C4 et P3-C1 ; `C-22` épargnant |
| G-06 disparition des aides, subventions et régimes particuliers | `digérée` | manuscrit P2-C4 ; REF_doctrine `D9-2-1` ; `C-32` |
| G-07 interruption des missions facultatives, regret et reprise associative | `digérée` | manuscrit P2-C1 et P2-C3 ; REF_doctrine `D6-3-2-e4` ; `C-31` |
| G-08 nature et égalité femmes-hommes hors contrainte fiscale ou réglementaire de l'État | **`absente`** | le manuscrit ne porte la biodiversité que comme compétence communale ; l'énoncé, nulle part |
| G-09 population donatrice plus riche, reste à vivre accru | `digérée` | `justifications.py` : « une population donatrice dont le reste à vivre a augmenté de 600 euros par mois » |
| G-10 missions libérées au bénéfice des associations | `digérée` | manuscrit P2-C3 « la sphère privée, qu'elle soit associative ou marchande » ; REF_doctrine `D6-3-2-e4` |
| G-11 fin des subventions et des réductions fiscales | `digérée` | `C-34` association subventionnée ; `C-35` bénéficiaire de niche |
| G-12 mandat plus important, moins d'élus, Parlement renforcé | `digérée` | `justifications.py` : « moins d'élus, mais dont le mandat pèse : c'est le vote qui y gagne » |
| G-13 communes renforcées, échelons intermédiaires supprimés | `digérée` | manuscrit P2-C2 « l'échelon politique local unique » ; `C-20`, `C-37` |
| G-14 environ 12 % des élus, mandat interrompu | `digérée` | `construire_positions.py`, `C-38`, qui porte la valeur en clair et la déclare non instruite |
| G-15 +13 % en un an, doublement du salaire moyen en 20 ans | **`absente`** | le +13 % est partout ; **le doublement en vingt ans, nulle part** |
| G-16 arrêt de l'avantage sur les chèques conditionnés, au choix du salarié | **`absente`** | l'arrêt est au manuscrit P1-C3 et P2-C4 et en `C-52` ; **l'option laissée au salarié, nulle part** |
| G-17 agent public, +13 % | `digérée` | manuscrit P2-C3 ; REF_doctrine `D6-3-2-e2` |
| G-18 fin de l'emploi à vie, disparition du statut | `digérée` | manuscrit P2-C3 ; `construire_positions.py`, qui l'attribue à l'input |
| G-19 10 % des agents, 70 % du traitement pendant 7 ans | `digérée` | manuscrit P2-C3, notes e93 et e94 ; `C-30` ; A-210 pour « jusqu'à sept ans » |
| G-20 principe de neutralité fiscale de l'entreprise | `digérée` | `construire_positions.py` et `justifications.py` : « les prélèvements nets de subventions et d'aides sont stables » |
| G-21 disparition des impôts de production | `digérée` | manuscrit P2-C5 ; REF_doctrine `D4-3-3-e2` |
| G-22 clientèle plus prospère | `digérée` | `apports.py` et `justifications.py` : « des clients plus riches » |
| G-23 baisse du risque de crise et de renchérissement du crédit | `digérée` | manuscrit épilogue ; REF_doctrine `D11-ed7` |
| G-24 réécriture des codes : simplicité, lisibilité, prévisibilité | `digérée` | manuscrit P2-C5 « code essentiel », « une réglementation stable et sans piège » |
| G-25 arrêt des subventions | `digérée` | manuscrit P2-C4 ; `C-33` |
| G-26 hausse de l'IS en compensation de près de deux cents impôts | **`absente`** | la hausse de l'IS est au manuscrit P2-C5 ; **les « près de deux cents impôts », nulle part — le corpus compte 438 impôts fusionnés en 4** |
| G-27 moindre recours à l'État, robustesse, fonds propres | **`absente`** | nulle part |
| G-28 indépendants et professions libérales, +13 % | `digérée` | manuscrit P2-C4 ; REF_doctrine, portée « salariés, indépendants, temps partiel et temps plein » |
| G-29 personne sans emploi, salaire futur +13 % | `digérée` | `C-10` personne sans emploi ; REF_doctrine `D3-2` |
| G-30 transition de 18 mois, puis indemnisation à 6 mois | **`absente`** | les six mois sont au manuscrit P3-C1 et à `hypotheses_doctrine.py` ; **la transition de dix-huit mois, nulle part** |
| G-31 étudiant majeur — catégorie ouverte, sans contenu | *sans contenu* | le corpus porte `C-16` jeune adulte et `C-42` étudiant de la gratuité |
| G-32 parents mieux rémunérés | `digérée` | `C-17` parent ; manuscrit P3-C4 |
| G-33 compte éducation | `digérée` | manuscrit P3-C4, 6 600 € par an ; REF_doctrine `D10-2-1` |
| G-34 choix libre de l'école | `digérée` | manuscrit P3-C4 ; REF_doctrine `D10-2` « l'argent suit l'enfant » |
| G-35 soignants mieux rémunérés | `digérée` | manuscrit P3-C3 ; `C-18` |
| G-36 lisibilité du remboursement | `digérée` | manuscrit P3-C3 ; REF_doctrine `D8-4-1-e1` « reste à charge prévisible et soutenable » |
| G-37 reste à charge de 10 %, plafonné à 5 % du revenu | `digérée` | manuscrit P3-C3, note e127 ; REF_doctrine `D8-4-1-p1` |
| G-38 sécurisation des pensions actuelles | `digérée` | manuscrit épilogue « une pension au moins équivalente au régime actuel » ; `hypotheses_doctrine.py` |
| G-39 rente viagère d'environ 500 € par an | `digérée` | manuscrit P3-C1, note e119 ; REF_doctrine ; `justifications.py` |
| G-40 fin des droits de donation et succession, DMTO 3 % au-delà de 100 000 € | `digérée` | manuscrit P2-C5, note e108 ; REF_doctrine : « un maximum entre 3 % de la valeur au-delà de 100 000 € et l'imposition de la plus-value » |
| G-41 travailler après l'âge minimal sans cotisation retraite | **`absente`** | le libre choix de l'âge de départ est au manuscrit P3-C1 ; **l'exonération de cotisation, nulle part** |
| G-42 suppression de l'abattement de 10 % sur les pensions | `digérée` | manuscrit note e120 « abattement dit Papon » ; `justifications.py` ; `C-39` |
| G-43 étranger en situation régulière, salaire plus élevé | **`absente`** | aucune catégorie de résident étranger régulier au référentiel des positions ; l'énoncé, nulle part |
| G-44 traitement plus rapide des demandes par la réécriture des codes | **`absente`** | le manuscrit porte « un traitement plus rapide des dossiers criminels », pas des demandes de titre |
| G-45 meilleur fonctionnement justice-police, fin des situations indécises | **`absente`** | nulle part |
| G-46 baisse des candidats, des passeurs, des accidents graves | **`absente`** | nulle part |
| G-47 disparition de l'AME hors urgence vitale | `digérée` | manuscrit P3-C3, note e125 ; `C-44`, défini comme « bénéficiaire de l'aide médicale d'État hors pronostic vital » |
| G-48 aucun capteur de rente n'est nommé | `digérée` | le manque est comblé : `construire_positions.py`, bloc capteurs `C-50` à `C-61`, douze catégories |
| G-49 aucune échelle | `digérée` | champ `echelle` du référentiel des positions — macro, méso, micro |
| G-50 aucune voie de raccroche | `digérée` | champ `raccroche` ; règle `RT-2` au REF_doctrine ; `justifications.py` |
| G-51 aucun rattachement à un nœud | `digérée` | clé `ancrage\|position\|categorie` du référentiel des positions |
| G-52 le parent seul manque, `D9-4-1` et `D9-4-2` | `digérée` | `C-43` parent seul ; REF_doctrine `D9-4-1` |

---

## Pièce 3 — `methode/arbitrages_archive.md`

### Verdict : copie unique

**Elle n'existe nulle part ailleurs.** Le dépôt `resolution-ib-dev/Resolution-2027`
a été cloné et inspecté : sa sous-racine `chantier/` ne porte que `appareil/`,
`referentiels/`, le `Makefile` et le `.gitignore`. Aucun `.md` de méthode, aucune
trace de ce fichier dans son historique. L'index le déclare `voie: coffre`, et
c'est exact : le coffre est son seul porteur.

**Et elle n'est pas dormante.** 255 entrées titrées, `A-1` à `A-255`. Les renvois
`A-nnn` cités dans les modules vivants du dépôt ont été relevés puis confrontés
au registre courant `methode/arbitrages.md` :

| relevé | compte |
|---|---|
| renvois `A-nnn` distincts cités au dépôt | 99 |
| qui résolvent dans `methode/arbitrages.md` | 48 |
| **qui ne résolvent que dans l'archive** | **51** |

*Deux occurrences ont été écartées du relevé et ne sont pas des renvois : `A-01`
et `A-0` sont le code d'une porte du domaine dans `portes_domaine.py`.*

Parmi eux, `A-35` et `A-57` sont cités dans l'en-tête même de
`relever_protos.py` comme la raison d'être de son dispositif, et `A-23` fonde la
répartition du travail que toute la méthode applique. Retirer l'archive rendrait
cinquante et un renvois muets.

*Une copie unique ne se retire pas.*

---

## Les unités `absente`, isolées

C'est la seule liste qui appelle une suite.

### Pièce 2 — 12 unités

`G-03` · `G-08` · `G-15` · `G-16` · `G-26` · `G-27` · `G-30` · `G-41` · `G-43` ·
`G-44` · `G-45` · `G-46`

Quatre d'entre elles forment un bloc : **les résidents étrangers**, réguliers et
irréguliers, n'ont aucune catégorie au référentiel des positions du côté gain —
`C-44` n'existe que comme perdant de l'AME. C'est le seul manque de la pièce qui
soit structurel et non ponctuel.

### Pièce 1 — 163 unités

- **Distinction facultatif / indispensable** — 10 unités, 8 `absente` :
  R-ARG001, R-ARG002, R-ARG003, R-ARG004, R-ARG005, R-ARG006, R-ARG009, R-ARG010
- **Idées diverses** — 58 unités, 56 `absente` :
  R-ARG011, R-ARG012, R-ARG013, R-ARG014, R-ARG015, R-ARG016, R-ARG017, R-ARG018,
  R-ARG019, R-ARG021, R-ARG022, R-ARG023, R-ARG024, R-ARG025, R-ARG026, R-ARG027,
  R-ARG028, R-ARG029, R-ARG030, R-ARG031, R-ARG032, R-ARG033, R-ARG034, R-ARG035,
  R-ARG036, R-ARG037, R-ARG038, R-ARG039, R-ARG040, R-ARG041, R-ARG042, R-ARG043,
  R-ARG044, R-ARG045, R-ARG046, R-ARG047, R-ARG048, R-ARG049, R-ARG050, R-ARG051,
  R-ARG052, R-ARG053, R-ARG054, R-ARG055, R-ARG056, R-ARG057, R-ARG058, R-ARG059,
  R-ARG060, R-ARG061, R-ARG062, R-ARG063, R-ARG064, R-ARG065, R-ARG067, R-ARG068
- **Innovation** — 2 unités, 2 `absente` : R-ARG069, R-ARG070
- **Le commerce international** — 1 unité, 1 `absente` : R-ARG071
- **Objections** — 45 unités, 45 `absente` :
  R-OBJ001 à R-OBJ045, sans exception
- **Hors périmètre — à trancher** — 51 unités, 51 `absente` :
  R-ARG072 à R-ARG122, sans exception

La dernière section est celle que la pièce elle-même signale comme relevant d'un
autre périmètre que le projet — climat, immigration, audiovisuel —, portant des
affirmations sans source et non mobilisables en cet état. **Elle représente
51 des 163 `absente`**, soit près d'un tiers : le retrait de la pièce se
discuterait autrement si elle en était détachée, mais ce fil ne détache rien.

---

*Aucune unité `absente` n'a été digérée par ce fil. Aucune pièce n'a été
retirée, réécrite ni complétée. Les trois pièces restent en l'état.*
