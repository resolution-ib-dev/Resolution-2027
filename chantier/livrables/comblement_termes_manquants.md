# Relevé de comblement des termes manquants du lot C — 20260917

*Sept bilans de blocs portent « non chiffré au paquet ». C'est exact au regard du
paquet machine, pauvre par construction, et cela ne dit rien du corpus : les
annexes du projet portent les indications de chiffrage, et
`methode/grille_lecture_budgetaire.md` formalise comment on les lit. Ce relevé va
du terme manquant à la ligne qui le porte.*

**Ce relevé ne chiffre rien.** Il dit où le chiffre est, sous quelle
qualification il se lit, et quel bouclage le rejoue. Reporter une valeur au bilan
d'un bloc est un autre travail, et il rouvre le bloc.

> **Deuxième passe, 20260917 — le second cercle du socle.** La première passe
> concluait que cinq termes sur six étaient `estimé` **pour la même raison
> mécanique** : l'onglet qui les portait n'était pas importé au socle, donc aucun
> bouclage ne le rejouait. Les six onglets ont été importés et sept bouclages
> neufs — `S11` à `S17` — les rejouent. **Aucune valeur n'a été produite** : cinq
> termes passent de `estimé` à `porté`, un sixième passe de « porté en
> composantes » à « porté en total », et un seul reste `estimé` pour une raison
> qui n'est plus l'import.

---

## La règle du verdict, écrite avant d'être appliquée

Le verdict se rend en trois valeurs et pas une quatrième.

| verdict | condition, mécanique | effet sur le bilan |
|---|---|---|
| **porté** | chaque composante du terme a sa ligne dans un onglet nommé, **et** un bouclage `S1` à `S17` rejoue cette ligne | il entre au bilan avec sa ligne, son onglet et son bouclage |
| **estimé** | la ligne existe, **aucun bouclage ne la rejoue** | il entre au bilan déclaré estimé |
| **à produire** | aucune pièce du projet ne porte le terme | c'est un travail ouvert, non un défaut de lecture |

**Ce qui sépare `porté` de `estimé` est mécanique et se vérifie.** Un onglet est
rejoué ou il ne l'est pas.

**`porté` ne veut pas dire « le bloc boucle ».** Les deux sont indépendants, et
l'arbitrage du 20260917 tranche le second : *le bouclage d'ensemble n'est pas un
objet du corpus* — `B-05` et `B-07` restent déséquilibrés et le disent. Un terme
porté est un terme dont la ligne est rejouée par un garde-fou ; il ne promet rien
sur l'équilibre du bloc qui l'accueille.

**Un bouclage prouve qu'un total affiché se retrouve depuis ses lignes, et rien
d'autre.** Il ne dit pas qu'une hypothèse est bonne. `S9` retrouve une dérivation
et laisse deux écarts de concept ouverts sous les yeux ; `S17` nomme
explicitement les paramètres qu'il ne prouve pas. C'est la forme juste.

**Les annexes vont être remplacées par des versions à jour.** Tout ce qui suit se
rejoue après remplacement : c'est la règle de propagation, et c'est précisément
ce pour quoi les bouclages ont été écrits.

**Deux pièges que la grille nomme, et qui s'appliquent ici.** Un agrégat de la
doctrine n'est presque jamais une colonne de l'annexe : c'est une somme de lignes
filtrées, plus ce qui vient d'ailleurs. Et un résidu n'est pas une source : une
part déduite par soustraction ne vaut pas une part écrite.

---

## Ce qui a changé, et par quoi

| onglet | classeur | état au matin | état au soir |
|---|---|---|---|
| `Gages` | calculs | importé, comparé à rien | importé, **bouclé par `S11`** et confronté à l'arbre des économies |
| `Fusion taxes` | calculs | non importé | importé, **bouclé par `S12`** |
| `CI unique` | calculs | non importé | importé, **bouclé par `S13`** |
| `CSG` | calculs | non importé | importé, **bouclé par `S14`** |
| `Perdants` | calculs | non importé | importé, **bouclé par `S15`** |
| `Figure 9.1` | DEPP, état de l'École | classeur non ouvert | ouvert, importé, **bouclé par `S16`** |
| `GraphAFU` | calculs | non importé | importé, **bouclé par `S17`** pour ce qui en dérive |

**Dix-sept bouclages, zéro en échec.** Et, parce qu'un contrôle qui n'a jamais
rien attrapé ne prouve pas qu'il regarde, les sept neufs portent leur épreuve —
`appareil/epreuve_controle_socle.py` : **quatorze fautes**, une par blessure, qui
lèvent toutes leur code, et **sept justes** — un arrondi dans la tolérance
déclarée, un libellé réécrit, un sous-ensemble ajouté, une ligne hors compte
déplacée, un point d'assiette réécrit, un paramètre posé déplacé — qui ne lèvent
rien.

**Deux choses valent plus que les taux.** La première : la confrontation de la
grande synthèse et de l'arbre des économies, deux vues du même chiffrage écrites
à deux endroits, qui se retrouvent **à l'octet sur cinq colonnes sur six** —
seule la ligne des collectivités locales diverge de 0,01 Md€, qui est son arrondi
d'affichage. La seconde : deux motifs du fichier de construction ne trouvaient
plus leur classeur — celui du budget général et celui des calculs —, et **rien ne
cassait**, la règle étant gardée. Le socle se refaisait sans la couche budgétaire
ni l'arbre des économies, et cela ne se voyait pas. C'est le même défaut qu'un
contrôle qui n'attrape jamais rien.

---

## Le relevé

Dix termes pour sept blocs : **8 portés, 1 estimé, 1 à produire.**

### B-02 — Effectifs et statut des agents publics · **porté** *(inchangé)*

**Terme.** Le coût de l'indemnité de `M-008` — 70 % du traitement jusqu'à sept
ans après le départ.

**Qualification** : *paramètre de calcul*. La grille dit qu'un paramètre « se
somme avec rien » : ce n'est pas un montant, c'est ce qui produit les montants.

**Où il se lit.** Classeur de calculs, onglet `Détail Economies`, colonne
« Hypothèses » : ligne « Départs fonctionnaires Etat » — *hors régalien et
éducation, 90 % de départs, **70 % salaire maintenu*** —, et même paramètre à la
ligne « Opérateurs (y. c. salaires) ». L'horizon de sept ans se lit à l'onglet
`Capitalisation`, ligne « Année 7 fonctionnaires ».

**Bouclage.** `S9` — la chaîne des emplois et des charges rejoue la dérivation
« masse salariale non régalienne × 90 % × **30 %** » et retrouve 0,866 Md€ contre
0,9 écrit. Le 30 % est le complément du 70 % maintenu : **le paramètre est dans
la formule que le bouclage rejoue.**

**Conséquence de lecture, qui vaut plus que le chiffre** : l'économie de masse
salariale du corpus est **déjà nette de l'indemnité**. Le bilan du bloc n'a donc
pas un terme à ajouter mais une mention à porter.

### B-03 — Échelon local unique, premier terme · **porté** *(inchangé)*

**Terme.** Le montant supprimé par la fermeture des échelons intermédiaires, hors
masse salariale.

**Où il se lit.** Onglet `Détail Economies`, bloc « Economies Collectivités
locales », ligne « Charges courantes et achats » — 6,1 restitué en année 1,
3,5 de solde, **9,6 Md€ de total supprimé**, hypothèse « **hors communes**,
sortie logement en 3 ans ». C'est l'hypothèse qui qualifie la ligne.

**Bouclage.** `S8` — l'arbre des économies se somme de bas en haut, 32 bouclages
sur 32. **Et désormais `S11`** : la même ligne se retrouve à l'onglet `Gages`,
« Charges courantes et achats » des collectivités, 6,1 et 3,5 pour 9,6.

### B-03 — Échelon local unique, second terme · **à produire** *(était `absent`)*

**Terme.** Le coût de la reprise par l'État des missions de solidarité
départementales.

**Où il se cherche.** Aucune ligne ne le porte. La grandeur voisine — « Aides
sociales locales, 36,1 Md€ », onglet `CI unique`, désormais importée et bouclée
comme composante du bloc *Social* du gage net — est une **assiette de gisement**
pour l'aide fondamentale, et la grille dit qu'une assiette « se somme avec rien ».
La prendre pour un coût de reprise serait exactement le résidu que la grille
interdit. *L'import de l'onglet ne change donc rien à ce terme, et c'est la bonne
issue : il rend la confusion impossible plutôt que de la combler.*

**Verdict.** L'arbitrage du 20260917 le requalifie : *un terme qu'aucune pièce du
corpus ne porte est à produire, non absent définitivement*. C'est un **nœud de
mise en œuvre**, et il rejoint la file derrière la sortie des fonctionnaires.

### B-05 — Extinction des aides aux entreprises · **estimé → porté**

**Terme.** La contrepartie du solde négatif de 20,5 Md€ — 27,5 Md€ d'économie
contre 48 Md€ de recette supprimée. Aucun énoncé du bloc ne couvre l'écart.

**Où il se lit.** Onglet `Fusion taxes` : « Taxes sur la main d'œuvre, −48 » ;
« Total à supprimer, −148 » ; « Solde à compenser, **78,7** » ; et les colonnes
de hausse — cible 78,70, option 1 77,03, option 2 77,26, option 3 77,51 — avec
leurs équivalents en points d'impôt sur les sociétés et en taxe foncière.

**Bouclage.** `S12`, et il prouve trois choses :

- les cinq colonnes se somment à leur total — montant 2024 **624,90**, niches
  supprimées **72,40**, solde net post CSG **29,20**, niches à supprimer
  **40,10**, taxes à supprimer **−148,00**, toutes exactes ;
- le **solde à compenser** se retrouve depuis elles : `−148 + 40,1 + 29,2 =
  −78,7`, à l'octet ;
- **chacune des quatre compensations se recompose depuis les lignes qui portent
  un point d'assiette** — cible 78,70 depuis 27 points d'IS, la taxe foncière et
  les droits de mutation ; option 1 77,03 depuis 29 points d'IS et une taxe
  foncière doublée ; option 2 77,26 depuis 2 points de TVA, 22 points d'IS et la
  taxe foncière ; option 3 77,51 depuis 4 points de TVA, 21 points d'IS et une
  taxe foncière portée à 22.

S'y ajoute le cadrage de tête : `PO = PIB × taux de prélèvements`, retrouvé pour
l'existant comme pour la cible, et la variation totale des taxes sur les produits
retrouvée depuis ses quatre composantes.

**Ce que le verdict ne dit pas.** Le bloc **reste déséquilibré**, et c'est
l'arbitrage du 20260917 : le programme assume de ne boucler qu'au total. Ce qui a
changé n'est pas l'équilibre du bloc, c'est que la pièce qui porte le solde a
désormais rang de preuve.

### B-06 — Solidarité universelle · **estimé → porté**

**Terme.** Le coût brut de l'aide fondamentale et de l'aide par enfant.

**Où il se lit.** Onglet `CI unique` : « Coût brut annuel **max 417,285 Md€** »,
« **min 386,727 Md€** », « Gages nets pour aide sociale unique **135,34564 Md€** »,
avec la population qui les produit — 68,6 M d'habitants, 54,5 M d'adultes,
14,1 M d'enfants, pondération enfant 0,5 — et la population fiscale qui produit
le minorant — 63,4 M, 50,4 M d'adultes, 13,04 M d'enfants.

**Bouclage.** `S13`, et ce qu'il retrouve est exact au millième :

- le **gage net** `135,34564` depuis ses trois blocs — Fiscal 21,6, Budgétaire
  31,8, Social 81,94564 — et chaque bloc depuis son détail ;
- le **coût brut max** `417,285` depuis la population : `(54,5 + 14,1 × 0,5) ×
  550 € × 12`, plus le supplément de handicap `(1,24 + 0,435) × (1 100 − 550) ×
  12` ;
- le **coût brut min** `386,727` par le même chemin sur la population fiscale ;
- la **hausse d'impôt sur le revenu** qui en découle, `281,93936` et `251,38136`,
  retrouvée comme coût brut moins gage net, et son **multiple** `3,46666` et
  `3,19931` comme `1 + hausse / 114,3` ;
- la **partition de l'effet** entre retraités et actifs, qui somme à un.

**Trois lignes ne participent à rien, et cela se déclare** : « Economies Etat en
année pleine », « Economies locales en année pleine » et « Reliquat économies
CSG » vivent en colonne D et n'entrent dans aucun total de la colonne C. Le socle
les porte `hors_compte`, et le jeu de justes de l'épreuve vérifie que les
déplacer ne fait rien bouger.

**Une grandeur reste non écrite, et le contrôle le dit** : les deux taux
implicites d'impôt sur le revenu — 0,25383 et 0,23425 — reposent sur une assiette
de **1 561 Md€** qui n'apparaît nulle part à l'onglet. Le bouclage vérifie que
les deux reposent bien sur la même, et il s'arrête là.

**Et le bloc reste déséquilibré.** L'auteur a tranché le 20260917 : la synthèse
ne porte que ces éléments d'estimation macro, il n'y a pas plus, et ce n'est pas
un défaut à corriger.

### B-07 — Prélèvements uniformes, premier terme · **porté en composantes → porté en total**

**Terme.** La ressource qui remplace les 114,46 Md€ supprimés.

**Où elle se lit, et par composantes.** Onglet `Détail Niches`, ligne « Niches
fiscales » — 43,1 restitué en CSG. Onglet `Détail Economies`, lignes de tête
« Economies Etat » — 44 / 33,7 / **77,7** — et « Economies Collectivités
locales » — 33,3 / 6,1 / **39,5**.

**Bouclages.** `S7` pour la première — 465 dépenses fiscales, 43,126 Md€ de gage
net retrouvés. `S8` pour les secondes.

**Ce qui change.** Les **129,4 Md€ de gain direct restitué** ne s'écrivaient qu'à
l'onglet `Gages`, que le socle importait en dix-huit lignes et qu'aucun bouclage
ne comparait. `S11` les recompose désormais depuis les quatre blocs de l'onglet —
niches fiscales 43,1, niches sociales 9, économies de l'État 44, économies des
collectivités 33,3 — et retrouve `129,4` exactement ; de même le gain indirect
`77,9`, le total supprimé à terme `207,49` et le gisement en sus `95,8`.

**Et surtout, la confrontation des deux vues.** Les deux têtes de l'onglet
`Gages` retrouvent les deux têtes de l'arbre des économies, colonne par
colonne — 44,0 / 33,7 / 77,7 pour l'État, 33,3 / 6,1 / 39,49 contre 39,5 pour les
collectivités. **C'est ce qui vaut, et non la somme** : le même chiffrage est
écrit à deux endroits par deux chemins, et les deux disent la même chose.

**Une divergence interne, nommée plutôt que corrigée.** La tête « Economies
Etat » de l'onglet `Gages` porte 33,7 en gain indirect quand ses six lignes de
détail font 33,9. L'écart tient dans les arrondis d'affichage — six lignes au
dixième, soit 0,30 de dérive possible — et la tête vient de l'arbre, non de son
propre détail. La tolérance du bouclage est calculée depuis le nombre de lignes
sommées, jamais réglée à la main.

### B-07 — Prélèvements uniformes, second terme · **estimé → porté**

**Terme.** Le perdant n'est pas nommé, alors que le corpus tient qu'un gain a
toujours un perdant nommé.

**Où il se lit.** Onglet `Perdants` : les populations et leur compte — 17 M de
retraités dont **4,3 M** perdants à un an, 5,8 M d'agents publics dont **0,54 M**,
3,3 M de sans-emploi, 10,4 M en logement social dont **3,5 M**. Onglet `CSG`,
colonnes « Effets nets à horizon 1 an » : **dont retraités, −15,182 Md€** contre
+71,617 pour les actifs.

**Bouclages.** `S14` et `S15`.

`S14` retrouve les effets nets depuis leurs trois composantes — suppression de la
CSG-CRDS, suppression des niches fiscales, économies budgétaires — pour les
quatre populations, et vérifie sur **chaque** effet ventilé que actifs plus
retraités font les ménages. Il retrouve aussi les gains par niveau de salaire
depuis le taux et l'assiette : un point de CSG porte sur 98,25 % du brut, la CSG
vaut 9,2 points et la CRDS 0,5, l'annuel est le mensuel douze fois, et la part du
net est le gain sur le net. Neuf niveaux de salaire, du SMIC au brut moyen.
Enfin, il retrouve l'effet **par adulte** — +952,73 € pour les ménages,
+1 695,68 € pour les actifs, **−893,06 € pour les retraités** — depuis l'effet et
la population de l'onglet `CI unique` : c'est une jonction entre deux onglets, et
elle tient.

`S15` retrouve chaque partition de population : les travailleurs et les chômeurs
au sens du Bureau international du travail font les actifs ; les sans-emploi et
l'activité réduite font les demandeurs d'emploi ; les boursiers et les
non-boursiers font les étudiants. Il vérifie en outre que **chaque population se
convertit** — tout y est écrit en toutes lettres, et un libellé qui cesserait de
se lire vaudrait zéro dans une somme au lieu d'échouer.

**Un écart de périmètre, dit et non comblé.** Les quatre têtes écrites font
65,4 M contre 68 M de résidents : **2,6 M ne relèvent d'aucune tête écrite**.
L'onglet ne prétend pas partitionner la population, et l'écart reste sous les
yeux. Il ne se corrige pas au socle.

**Une distinction que l'import a imposée, et qui n'était pas écrite** : toutes
les lignes de l'onglet commencent par « Dont » et aucune ne dit de quoi. Deux
natures s'y cachent, et elles ne se somment pas pareil — une **partition** épuise
sa tête, un **sous-ensemble** non. Les agents publics sont pris dans les
travailleurs, les résidents en logement social traversent toutes les têtes. Les
confondre aurait fait sortir en échec un simple dénombrement croisé.

**Et l'anomalie du bilan que ce relevé ferme.** Le contrôle `D2` de
`controle_blocs.py` sortait, sur ce bloc, « 108,56 Md€ ni aux paramètres du bloc,
ni ailleurs au paquet, ni d'origine déclarée ». Son origine est désormais **au
socle** : `csg.produit_2024_md_eur.csg`, onglet `CSG`, ligne « Données 2024 » —
108,56 pour la CSG seule contre 114,46 pour CSG + CRDS activité. **La correction
n'est pas de retirer le montant mais de déclarer son origine**, et elle appartient
au fil qui rouvre les blocs.

### B-09 — Fiscalité à quatre impôts · **estimé → porté**

**Terme.** Le rendement du taux unique de 23 % sur le revenu net, celui du taux
unique de taxe sur la valeur ajoutée, et l'ampleur de la hausse de l'impôt sur
les bénéfices.

**Où ils se lisent.** Onglet `Fusion taxes` : l'existant — « IR net 87,3 »,
« IS net 57,4 », « TVA 206,3 », « Taxe foncière 42,9 » — et les cibles, colonnes
« Hausse cible / option 1 / option 2 / option 3 » : **78,70 / 77,03 / 77,26 /
77,51** au total, avec « 27pt IS / 29pt / 22pt / 21pt » et la taxe foncière portée
de 41,96 à 44,0. Onglet `CI unique` : « IR total brut **114,3 Md€** — DGFiP,
IR 2023 », et les taux moyens et revenus d'équilibre qui en dérivent.

**Bouclages.** `S12` pour les quatre colonnes de compensation, recomposées depuis
les lignes qui portent un point d'assiette. `S13` pour la hausse d'impôt sur le
revenu et son multiple.

**Ce que le bouclage ne prouve pas, et il faut le dire** : que 27 points d'impôt
sur les sociétés rendent 25,69 Md€ est une **hypothèse de rendement**, pas une
somme. Le bouclage vérifie que les montants écrits s'additionnent à leur total et
que chaque montant porte son point d'assiette ; il ne vérifie aucune élasticité.

### B-15 — Éducation choisie, premier terme · **estimé** *(motif changé)*

**Terme.** Le coût brut de la dotation de 6 600 € par enfant et par an.

**Qualification** : *paramètre de calcul*. Aucun total n'est écrit.

**Où il se lit.** Onglet `GraphAFU`, ligne « Compte éducation » : 6 600 € par an
de la naissance à dix-huit ans, année par année, constant sur les dix-huit âges.

**Ce qui a changé.** L'onglet est désormais importé et `S17` le rejoue. Il y
trouve deux lignes qui **dérivent** du corpus et se retrouvent exactement :
l'aide fondamentale à 3 300 € par an, soit `550 € × 0,5 × 12` — le montant
mensuel par la pondération de l'enfant —, et la part d'aide handicap à 6 600 €,
soit `1 100 € × 0,5 × 12`. Ces deux-là prouvent que la feuille est lue de la même
manière que l'onglet `CI unique`.

**Le compte éducation n'est pas de ceux-là.** Aucune dérivation du corpus ne le
produit, et aucun total ne le somme : c'est un paramètre posé. `S17` le **nomme
comme tel** plutôt que de faire croire qu'il le prouve, et le jeu de justes de
l'épreuve vérifie que le déplacer ne lève rien — ce qui est la forme honnête d'un
contrôle qui connaît sa portée.

**Verdict : estimé**, et le motif n'est plus le même. Ce n'était pas un défaut
d'import : c'est une absence de dérivation. **Le combler n'est pas un travail
d'appareil**, c'est un travail de chiffrage — combien d'enfants, quelle assiette,
quel coût brut —, et il rouvre le bloc.

### B-15 — Éducation choisie, second terme · **estimé → porté**

**Terme.** La dépense que la dotation remplace.

**Où elle se lit.** Classeur DEPP « L'état de l'École 2025 », onglet
`Figure 9.1` : dépense intérieure d'éducation **197,0994 Md€ en 2024**,
provisoire, 6,8 % du PIB, et la série 2019-2024 en euros courants et constants.

**Bouclage.** `S16`. Le classeur est ouvert, l'onglet importé, et le bouclage
vérifie l'identité qui fait la série : **à l'année de référence des prix, les
euros courants et les euros constants sont la même valeur** — 197,0994 des deux
côtés, à la quatrième décimale. Le déflateur implicite d'un millésime au suivant
est rendu en clair, et celui de 2023 à 2024 vaut 1,02088 contre les « + 2,1 % »
que la note du classeur déclare.

**Ce que le bouclage ne prouve pas** : les déflateurs des millésimes antérieurs
sont chaînés et ne s'écrivent pas à la feuille. Ils sont affichés, non vérifiés.

---

## Ce que le relevé laisse

**Un seul terme estimé sur dix**, et il ne l'est plus faute de garde-fou : il
l'est faute de dérivation. La dotation par enfant est un paramètre posé, et le
chiffrer est un travail de doctrine, pas d'appareil.

**Un seul terme à produire** : la reprise par l'État des missions de solidarité
départementales. Il rejoint la file des nœuds de mise en œuvre derrière la sortie
des fonctionnaires.

**Huit termes portés**, dont cinq qui ne l'étaient pas ce matin, **sans qu'aucune
valeur ait été produite**. C'était le pari du lot, et il tient : ce qui séparait
`estimé` de `porté` n'était pas une incertitude sur les chiffres mais une absence
de garde-fou.

**Ce que le lot a trouvé en chemin, et qui ne se cherchait pas** : deux motifs du
fichier de construction ne trouvaient plus leur classeur, sans que rien ne casse.
La leçon est celle du jeu de fautes, appliquée ailleurs — **un mécanisme qui ne
trouve jamais rien ne se distingue pas d'un mécanisme qui fonctionne**, et seule
une épreuve les sépare.
