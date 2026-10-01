# Grille de lecture budgétaire

**Les classeurs de l'auteur sont la source officielle.** Ils ne se réécrivent
pas, ils ne viennent pas au dépôt, et rien de ce document ne prétend les
remplacer. Ce que la grille formalise, c'est **comment on les lit** — et elle
n'a de valeur que parce que le contrôle prouve qu'elle les lit juste.

Les deux dispositifs coexistent. Le classeur reste l'outil de travail ; la
grille est ce qui permet de le rejouer, de le contrôler, et un jour de le
varianter sur un PLF neuf.

---

## Ce que la grille sépare, et pourquoi

Dans les classeurs, deux choses vivent côte à côte dans les mêmes lignes.

**Le socle** est ce que le document budgétaire publie : un bénéficiaire, un
montant, une référence juridique, un effectif. Il ne se discute pas. Il change
à chaque exercice, et il change tout seul.

**L'interprétation** est ce que l'auteur a ajouté en colonnes : le régime
retenu — supprimer, fusionner, internaliser, laisser au flux outre-mer — et les
montants qui en découlent. Elle se discute, elle se varie, et c'est elle qu'un
PLF neuf oblige à réexaminer.

**Les mélanger, c'est perdre la capacité de rejouer.** Un montant qui change
d'un exercice à l'autre ne dit rien de la décision qu'on avait prise ; une
décision qu'on a prise ne dépend pas du montant. Séparées, les deux se
recomposent : socle × interprétation = chiffrage.

C'est la seule chose que la grille impose. Tout le reste en découle.

---

## Le vocabulaire en vigueur est celui du 20260917

*Tranché par l'auteur le 20260921 — question 26.* Les classeurs mis au propre du
20260917 ont requalifié six termes sur quatre classeurs sur six, **à valeurs
identiques à l'octet**. La grille passe au nouveau vocabulaire, et l'ancien
disparaît d'ici.

| ce que la grille dit désormais | ce qu'elle disait jusqu'au 20260917 |
|---|---|
| économie à horizon 1 an | gage CSG, gage net CSG |
| économie supplémentaire | économie pérenne en sus, solde |
| solde PO | effet macroéconomique, effet macro |
| champ non indispensable | suppression immédiate |
| aide fondamentale universelle | crédit d'impôt unique |
| niches restituées | niches supprimées |

**Ce n'est pas un renommage, et c'est pourquoi il fallait le trancher** :
« effet macro » et « solde PO » ne disent pas la même chose du même nombre. La
grille tient désormais la seconde lecture.

**Ce que la bascule ne touche pas : les adresses.** Un onglet qui a changé de
nom, une en-tête qui a changé de ligne, une plage qui a bougé restent notées
avec leur état antérieur — ce sont des faits vérifiables sur où la matière vit,
et `appareil/socle_0910.py` en dépend. Seul le vocabulaire bascule.

---

## Les identifiants

Les nomenclatures budgétaires sont stables d'un exercice à l'autre. Les
identifiants se gardent donc tels quels, sans table de correspondance.

| objet | clé | où elle vit |
|---|---|---|
| dépense fiscale | numéro à six chiffres — `100112`, `40101` | annexe 3 du tome II des Voies et moyens |
| organisme affectataire | numéro SIREN | annexe 2 du tome I |
| taxe affectée | code de la taxe, sous son affectataire | annexe 2 du tome I |
| programme budgétaire | numéro à trois chiffres | annexe État, missions et programmes |
| opérateur | intitulé, tel que le PLF l'écrit | jaune des opérateurs |

**Une seule fragilité, et elle est nommée** : l'opérateur n'a pas de clé
numérique, et les agrégats du classeur le filtrent sur son intitulé exact. Un
libellé qui changerait au PLF suivant casserait un total sans bruit. C'est
pourquoi les intitulés filtrants sont écrits en clair dans
`appareil/controle_socle.py` — un changement les fait sortir en échec.

**Ce que cette fragilité a coûté, mesuré le 20260917.** La ligne du chiffrage
« CNC et subventions culturelles » agrège **trois affectataires** — le CNC, le
Centre national de la musique et l'association pour le soutien du théâtre privé,
douze lignes de taxe. Le rattachement du corpus n'en comptait **qu'un**, neuf
lignes : 705,3350200 M€ au lieu de 749,8160514. **Quarante-quatre millions
d'euros de taxe affectée manquaient depuis l'origine, et rien ne regardait** —
`S6` ne bouclait que trois affectataires isolés là où la tête en nomme huit, et
la tolérance posée du bouclage aval, 0,09 Md€, absorbait le reste. Les deux
contre-mesures sont prises : **`S6` boucle les huit lignes de l'onglet
`Synthèse TA` et le total, et il les lit au classeur au lieu de les recopier.**
La tolérance posée, elle, reste ouverte — question 15 de
`methode/a_trancher.md`.

---

## Les trois sources sectorielles, colonne par colonne

### Les dépenses fiscales — annexe 3 du tome II

Onglet `Chiffrages Résolution`, en-têtes sur les lignes 5 et 6, données à partir
de la ligne 7. *Jusqu'au 20260917 : onglet `Chiffrages IB`, en-têtes 19 et 20,
données à partir de 21.* Quatre cent soixante-cinq dépenses fiscales.

| colonne | couche | ce qu'elle porte |
|---|---|---|
| A à C | socle | catégorie, sous-catégorie, sous-sous-catégorie |
| D | socle | **le numéro de la dépense fiscale** |
| E | socle | libellé législatif |
| F, G | socle | création, fin du fait générateur |
| H | socle | nombre de bénéficiaires |
| I | socle | réalisation 2024, en M€, telle que le PLF la publie |
| J | interprétation | la même, augmentée de la TVA des administrations publiques |
| K | interprétation | **part d'effet net** — 1 pour une base inerte, 0,5 pour une base active |
| L | interprétation | part de solde brut |
| M | interprétation | **le régime** — `Oui`, `En 3 ans`, `Fusion CI IR`, `Flux OM` |
| N | interprétation | **économie à horizon 1 an**, en M€ |
| O | interprétation | **solde PO**, en M€ |
| P, Q | interprétation | entreprise, nature de la niche — `Exo`, `Aba`, `Déd`, `CI`, `RI` |

**Les huit autres feuilles de l'annexe portent la même clé et enrichissent la
même entrée**, et elles ne se lisent donc pas séparément : `Chiffrages` donne la
réalisation et les prévisions 2025 et 2026 ; `Echéances` la création, la
dernière modification, la fin du fait générateur et de l'incidence budgétaire ;
`Bénéficiaires` leur nature et leur nombre ; `Méthodologie` **la fiabilité que
l'administration déclare de son propre chiffrage** et la méthode retenue ;
`Références juridiques` la norme de référence, le code et l'article ;
`Programme de rattachement` le programme porteur — 519 rattachements pour 465
dépenses, certaines en ayant plusieurs.

**La fiabilité qualifie chaque chiffre qu'on reprend.** Un gage bâti sur un
ordre de grandeur ne vaut pas un gage bâti sur une simulation, et le classeur de
synthèse le compte par ligne.

Les mentions `ε`, `nc` et `-` du PLF ne sont pas des nombres : elles se gardent
telles quelles et **ne se lisent jamais comme zéro**.

Les agrégats de tête se font par `SUMIFS` croisant l'impôt (colonne B) et le
régime ou la nature. La règle du croisement `IR et IS` est de compter la moitié
de chaque côté.

### Les taxes affectées — annexe 2 du tome I

Deux feuilles depuis le 20260917 : `Synthèse TA` porte la tête, `taxes affectées`
porte les lignes — en-têtes sur les lignes 2 et 3, données à partir de la ligne 4.
Deux cent soixante-dix-huit lignes. *Jusqu'au 20260917 : une feuille, en-têtes 15
et 16, données à partir de 17.*

| colonne | couche | ce qu'elle porte |
|---|---|---|
| A à C | socle | secteur, catégorie d'opérateur, nature juridique |
| D | socle | **SIREN de l'affectataire** |
| E à G | socle | programme et mission de rattachement |
| H, I | socle | **code de la taxe et libellé de l'affectataire** |
| Y | socle | référence juridique |
| O | socle | affectation nette, en euros |
| J | interprétation | **le régime** — `Oui`, `Flux OM`, `Fusion CI`, `Bourse` |
| K | interprétation | **économie à horizon 1 an** |
| L | interprétation | **économie supplémentaire** |

**En budgétaire — et seulement en budgétaire — les deux colonnes sont deux temps
d'une même restitution**, non deux natures différentes. L'économie à horizon
1 an est ce qui est restituable dès l'année 1 ; l'économie supplémentaire est ce
qui est restitué ensuite. **La vraie économie valorisable restituée est leur
total**, et c'est ce total qui remonte au tableau de référence.

La règle ne vaut pas pour les dépenses fiscales : là, l'économie à horizon 1 an
et le solde PO sont deux grandeurs distinctes, et elles ne s'additionnent pas.

### Les opérateurs et les agences — classeur ETP et agences

Onglet `Opérateurs R`, données à partir de la ligne 5. Cent quatre-vingts lignes
pour quatre cent trente-quatre entités : une ligne peut regrouper une catégorie,
et c'est la colonne F qui porte le compte.

| colonne | couche | ce qu'elle porte |
|---|---|---|
| A à D | socle | mission et programme de rattachement |
| E | socle | **intitulé de l'opérateur** |
| F | socle | nombre d'entités que la ligne regroupe |
| G à I | socle | emplois LFI 2025 — total, sous plafond, hors plafond |
| J à L | socle | emplois PLF 2026 — total, sous plafond, hors plafond |
| N à R | interprétation | **le régime, marqué d'une croix dans une seule colonne** |

Les cinq régimes : `vente`, `suppression`, `epic_musee`, `epic_enseignement`,
`internalisation`. **Un opérateur porte au plus un régime** — deux croix le
compteraient deux fois dans les agrégats, et le contrôle le refuse.

L'onglet `Synthèse agences R` récapitule quatre familles — opérateurs du PLF,
organismes hors PLF, autorités indépendantes, commissions — qui font ensemble
les mille cent quatre agences d'État, et une cinquième ligne pour les agences
locales.

---

## Comment un agrégat de la doctrine se recompose

L'exemple qui prouve la grille, et qu'il faut avoir en tête pour lire tous les
autres.

**France Compétences, 10,6 Md€ au sous-item `D2-2-1-s2`.**

1. À l'annexe 2 du tome I, onze lignes de taxe affectée portent le libellé
   « France Compétences ». Elles restituent 3 374,90 M€ dès l'année 1 et
   6 749,80 M€ ensuite.
2. L'économie restituée totale est la somme : **10 124,69 M€**.
3. S'y ajoute la subvention budgétaire, 434,07 M€, qui ne vient pas des taxes
   affectées.
4. Total : **10 558,8 M€**, soit les 10,6 Md€ du référentiel.

Le même chemin vaut pour les autres affectataires isolés : Agences de l'eau
2 085,36 M€ pour 2,1 ; Action Logement 1 910 M€ pour 1,9 ; AFITF 715,69 M€ pour
0,7 ; chambres de commerce 549,60 M€ pour 0,5 ; établissements publics fonciers
264,23 M€ pour 0,3 ; Anah 409,5 M€ pour 0,4. Pour le CNC et les subventions
culturelles, il faut cumuler **trois affectataires** — douze lignes, 749,82 M€ ;
la part budgétaire qui complétait la ligne n'est plus sourcée (`A-422`).

**La leçon de lecture** : un agrégat de la doctrine n'est presque jamais une
colonne du PLF. C'est une somme de lignes filtrées, plus ce qui vient d'ailleurs.
Chercher le chiffre tel quel dans le document budgétaire ne le trouve pas.

---

## Ce que le bouclage prouve

`appareil/controle_socle.py` recompose depuis les lignes et compare aux totaux
que le classeur affiche. Dix-sept bouclages, et **tant qu'ils ne sont pas verts,
la grille est une hypothèse**.

**Un bouclage prouve qu'un total affiché se retrouve depuis ses lignes, et rien
d'autre.** Il ne dit pas qu'une hypothèse est bonne : `S9` retrouve une
dérivation et laisse deux écarts de concept ouverts sous les yeux, et c'est la
forme juste.

**Un contrôle neuf porte son jeu de fautes et son jeu de justes.** Un contrôle
qui n'a jamais rien attrapé ne prouve pas qu'il regarde, et un contrôle qui
hurle sur tout ne prouve pas qu'il discrimine.
`appareil/epreuve_controle_socle.py` blesse le socle de treize façons, une à la
fois, et vérifie que chaque blessure lève son code ; puis il le modifie de six
façons légitimes — un arrondi dans la tolérance, un libellé réécrit, un
sous-ensemble ajouté, une ligne hors compte déplacée — et vérifie qu'aucune ne
lève rien. `make controle` joue les deux jeux.

**La tolérance n'est pas un réglage.** Le classeur arrondit chaque colonne au
dixième de milliard à l'affichage : une somme de `n` lignes peut donc dériver de
`n × 0,05`, et la tolérance se calcule depuis ce nombre. Elle ne se remonte
jamais pour faire tomber un compte.

| bouclage | ce qu'il retrouve |
|---|---|
| S1 | 434 entités, un régime chacune, réparties 15 · 123 · 36 · 226 · 34 |
| S2 | 479 514 emplois LFI 2025 répartis entre les cinq régimes |
| S3 | chaque ligne de la synthèse des agences égale son détail |
| S4 | les quatre familles font les 1 104 agences d'État |
| S5 | 8 119,67 M€ restitués en année 1, 9 802,72 ensuite, 17 922,39 au total |
| S6 | **les huit affectataires** que l'onglet `Synthèse TA` isole retrouvent leurs lignes, et le total de la tête se recompose depuis les 278 lignes |
| S7 | 465 dépenses fiscales, 89,406 Md€ de réalisation, 101,321 y compris TVA, 43,126 d'économie à horizon 1 an, 29,141 de solde PO |
| S8 | l'arbre des économies se somme de bas en haut — 27 bouclages, du détail à la rubrique, de la rubrique à la tête, de l'incidence aux trois totaux — et chaque ligne rattachée retrouve ses taxes |
| S9 | la chaîne des emplois et des charges se rejoue depuis la synthèse du budget général — 5 dérivations sur 7, 2 écarts de concept, **0 ouvert** |
| S10 | les 128 programmes font les 35 missions, les missions font la grille des dix catégories, et **la part supprimable se retrouve depuis les traitements écrits** — 4 catégories sur 4 |
| S11 | la tête de l'onglet `Flux` se recompose depuis ses quatre blocs, chaque bloc depuis son détail, et **chaque tête retrouve la ligne correspondante de l'arbre des économies** — c'est la confrontation des deux vues du même chiffrage |
| S12 | `Fusion taxes` : les cinq colonnes se somment à leur total, le solde à compenser se retrouve depuis elles, et **chacune des quatre compensations se recompose depuis les lignes qui portent un point d'assiette** |
| S13 | `CI unique` — l'aide fondamentale universelle : l'économie à horizon 1 an se retrouve depuis ses trois blocs, le coût brut depuis la population et le montant mensuel, la hausse d'impôt sur le revenu depuis le coût brut moins cette économie, et la partition de l'effet somme à un |
| S14 | `CSG` : les effets nets se retrouvent depuis leurs trois composantes, actifs et retraités font les ménages sur chaque effet ventilé, les gains par niveau de salaire se retrouvent depuis le taux et l'assiette, et l'effet par adulte depuis l'effet et la population de l'aide fondamentale universelle |
| S15 | `Perdants` : chaque **partition** se somme à sa tête, et chaque population se convertit — un libellé qui cesserait de se lire sortirait en absence et non en zéro. *L'onglet n'a pas de successeur au 20260917 ; sa source est désormais `livrables/extrait_classeurs_anterieurs_20260917.md` — voir plus bas.* |
| S16 | la dépense intérieure d'éducation : à l'année de référence des prix, les euros courants et les euros constants sont la même série. *Le classeur DEPP est le seul des sept antérieurs sans successeur au 20260917 ; **le millésime reste valable et on le garde** — tranché le 20260921 (`A-423`).* |
| S17 | la restitution salariale : année 1 / total = **0,30 exactement**, sur les départs de fonctionnaires d'État, les départs locaux et la part salariale de France Travail |

### La restitution salariale — 30 % en année 1, 70 % au solde

**Une économie de masse salariale se restitue en totalité, mais pas d'un coup.**
Le classeur en porte 30 % en année 1 et 70 % au solde. Il ne l'écrit nulle part
en toutes lettres : il l'applique, et le rapport est la seule preuve. `S17` le
vérifie donc **exactement, sans tolérance** — un rapport qui cesserait d'être
exact dirait que l'hypothèse a changé sans le dire.

| ligne | année 1 | total | rapport |
|---|---|---|---|
| Départs fonctionnaires d'État | 0,9 Md€ | 3 Md€ | 0,300000 |
| Départs fonctionnaires locaux | 6 Md€ | 20 Md€ | 0,300000 |
| France Travail, part salariale | 1 051,92 M€ | 3 506,40 M€ | 0,300000 |

*Arrêté par l'auteur le 20260917.* **Avant ce dépôt, seuls les 30 % d'année 1
étaient comptés** : les départs de fonctionnaires portaient 0,9 et 6 Md€ sans
solde, et la part salariale de France Travail ne portait pas ses 2 454,48 M€
de solde. C'est de là que viennent les +4,8 Md€ d'économie d'État et les
+13,9 Md€ de collectivités locales entre les deux états du classeur.

**Ce que le jeu de justes a appris.** Le niveau des montants a le droit de
bouger — doubler les trois lignes ne lève rien tant que le rapport tient —, le
libellé et l'hypothèse en toutes lettres aussi. Ce qui n'a pas le droit de
bouger est le rapport. `appareil/epreuve_s17_salaire.py` blesse le socle de huit
façons et le modifie de six façons légitimes : huit codes levés, six silences.

### L'écart de détail qui s'est déplacé

Le détail des rubriques d'État collait à 77,9 contre 77,7 en tête avant le
20260917 ; il colle désormais exactement à 82,5. Les collectivités, elles, sont
passées de l'exactitude à **53,5 de détail contre 53,4 en tête**. Les deux
restent sous la tolérance calculée — quatre lignes × 0,05 = 0,20 — donc `S8` ne
sonne pas. **L'écart est neuf et il se dit** : une tolérance qui absorbe n'est
pas une tolérance qui approuve.

**Une divergence ne se corrige pas au socle.** Elle dit que la grille est
fausse, et c'est la grille qu'on reprend.

---

## La réconciliation des opérateurs

Un opérateur reçoit son argent par trois canaux et porte des emplois, et les
quatre vivent dans trois fichiers sans identifiant commun.

| ce qu'on réconcilie | maille | d'où ça vient |
|---|---|---|
| statut juridique | opérateur | annexe 2 du tome I, colonne C |
| emplois | opérateur | onglet Opérateurs, sous et hors plafond |
| taxes affectées | opérateur | annexe 2, agrégée puis appariée par libellé |
| subvention pour charges de service public | **programme** | PAP, catégorie 32 |
| transferts de titre 6 | **programme** | PAP, catégories 61 à 65 |

**Les mailles ne sont pas les mêmes, et c'est la limite à tenir.** Le projet
annuel de performance ne nomme jamais l'opérateur : il donne, par programme, ce
qui part en subvention et en transferts. Trente programmes sur cinquante-quatre
portent plus d'un opérateur — pour ceux-là le montant n'est **pas** imputable à
l'opérateur, et la ligne le dit. Les additionner produirait un tableau qui
paraît complet et qui compte plusieurs fois la même subvention.

Deux constats à assumer : **le statut n'est connu que pour vingt-trois
opérateurs**, parce qu'il ne se lit que dans l'annexe des taxes affectées et
qu'un opérateur qui n'en perçoit aucune n'a pas de statut déclaré ; et **la
subvention n'est à la maille de l'opérateur que dans vingt-quatre cas**.

Les libellés de mission et de programme de l'onglet Opérateurs sont des formules
que la conversion rend illisibles : ils se réparent par la nomenclature de
l'annexe État, qui les porte en clair indexés par numéro de programme. Cent
quatre-vingts sur cent quatre-vingts.

## L'arbre des économies, et l'assiette de chaque ligne

Le chiffrage vit dans l'onglet `Détail Economies` du classeur de calculs. Il a
trois étages : deux totaux de tête — l'État pour **82,5 Md€**, les collectivités
locales pour **53,4** —, dix rubriques, et vingt-deux lignes de détail sous quatre
rubriques d'État. Chaque ligne porte deux temps de restitution, un code de
destination, une hypothèse en toutes lettres, et parfois l'incidence par
population.

| colonne | ce qu'elle porte |
|---|---|
| A | le code de destination — **où l'économie retombe une fois reclassée** |
| C | l'intitulé, et le niveau : « dont » marque le détail |
| D | l'**économie à horizon 1 an** |
| E | l'**économie supplémentaire** |
| F | le total supprimé — c'est lui l'économie valorisable |
| G | l'hypothèse de chiffrage |
| I | une note de dérivation : base d'ETP, économie d'année 1 |
| S:W | l'incidence par population, quand elle est allouée. *En `L:P` jusqu'au 20260917.* |

**Le code de la colonne A n'est pas la rubrique.** Une économie logée sous
« chèques aux ménages » peut porter le code AE et rejoindre les aides à l'emploi
— c'est le cas de l'aide médicale de l'État et des exonérations d'emploi à
domicile. Perdre cette colonne, c'est ne plus savoir qui supporte quoi.

### Les trois mailles d'une ligne d'opérateur

| maille | exemples | combien |
|---|---|---|
| opérateur du PLF | France Compétences, France Travail, ADEME, CNC, AFITF, ANAH (deux lignes), agences de l'eau | 8 |
| ODAC-ODAL, hors opérateurs | Action Logement Services, chambres consulaires, établissements publics fonciers | 3 |
| résidu non détaillé | « autres » | 1 |

**Le périmètre des opérateurs ne couvre pas le chiffrage.** Trois lignes se
prennent sur la liste ODAC-ODAL, où elles portent un régime :

| ligne | ODAC | entités | régime | taxes à l'annexe |
|---|---|---|---|---|
| Action Logement | ODAC-223 | 1 | vente | 1 affectataire |
| CCI et chambres d'agriculture | ODAC-730 | 273 | vente | 2 affectataires, 3 lignes |
| Établissements publics fonciers | ODAC-731 | 40 | vente | 34 affectataires |

**Deux mailles subsistent dans chaque ligne, et elles se déclarent.** L'annexe
des taxes nomme des affectataires, l'ODAC compte des structures : ce ne sont pas
les mêmes objets. Six établissements fonciers n'ont pas de taxe affectée au
PLF 2026, et cela se lit (A-114).

**MaPrimeRénov' est un dispositif, mais l'ANAH le distribue** : la ligne rejoint
son opérateur porteur, qui porte donc deux économies — 0,4 Md€ de restitution de
taxe et 1,3 Md€ de crédits, soit 1,7 Md€ (A-112). Un opérateur peut porter plus
d'une ligne, et la réconciliation en tient la liste.

### Les deux canaux, et l'écart qui ne s'absorbe pas

Une économie de **taxe affectée** se recompose exactement depuis l'annexe 2 du
tome I : restitué en année 1 plus solde restitué ensuite, agrégés sur les
bénéficiaires nommés. Six lignes bouclent ainsi.

Une économie **budgétaire** est prise sur des crédits. Le projet annuel de
performance donne l'enveloppe du programme ; il ne dit pas la part qu'on y
taille. L'assiette se nomme, le montant ne s'en déduit pas.

L'écart entre ce que la ligne affiche et ce que les taxes recomposent relève de
trois cas et de trois seulement : il tient dans l'arrondi d'affichage du
classeur — 0,055 Md€, puisque chaque colonne est arrondie au dixième — et il se
nomme arrondi ; il est positif au-delà, et c'est une **part budgétaire** ; il est
négatif au-delà, et c'est un défaut de lecture.

| ligne | classeur | recomposé par les taxes | reste |
|---|---|---|---|
| France Compétences | 10,6 | 10,125 (11 taxes) | 0,475 budgétaire, **non sourcé** (A-422) |
| France Travail | 2,7 | — | 2,700 budgétaire, programme 102 |
| CNC et subventions culturelles | 1,3 | 0,750 (12 taxes) | 0,550 budgétaire, **non sourcé** (A-422) |
| Agences de l'eau | 2,1 | 2,085 (1 taxe) | arrondi |
| AFITF | 0,7 | 0,716 (4 taxes) | arrondi |
| Action Logement | 1,9 | 1,910 (1 taxe) | arrondi |
| CCI et chambres d'agriculture | 0,5 | 0,550 (3 taxes) | arrondi |
| ADEME | 0,9 | — | 0,900 budgétaire, programme 181 |
| Établissements publics fonciers | 0,3 | 0,264 (34 taxes) | arrondi |
| ANAH | 0,4 | 0,409 (1 taxe) | arrondi |
| MaPrimeRénov' (ANAH) | 1,3 | — | 1,300 budgétaire, programmes 174 et 135 |
| autres | 2,8 | — | résidu, non détaillé |

Un rattachement écrit par règle — les trente-quatre établissements fonciers —
**déclare le nombre de lignes de taxe qu'il attend**. Si un affectataire apparaît
ou disparaît au PLF suivant, le compte ne tient plus et le contrôle le sort.

### La chaîne des emplois et des charges

Trois rubriques d'État ne passent ni par une taxe ni par un programme. Elles se
rejouent depuis la synthèse du budget général, et le classeur écrit le résultat
sans écrire la formule.

| ce qu'on rejoue | formule | calculé | écrit |
|---|---|---|---|
| charges courantes et achats | (fonctionnement + investissement non régaliens) × 80 % | 3,784 Md€ | 3,8 |
| départs de fonctionnaires d'État | masse salariale non régalienne × 90 % × 30 % | 0,866 Md€ | 0,9 |
| ETP d'État supprimés | masse salariale non régalienne ÷ salaire moyen × 90 % | 61 392 | 61 400 |
| ETP État et opérateurs | 61 400 + 41 800 + 47 880 | 151 080 | 151 000 |
| ETP toutes administrations | les précédents + 428 500 locaux | 579 580 | 580 000 |

Deux dérivations **restent ouvertes** et ne se corrigent d'aucun côté : la base
d'ETP des opérateurs hors France Travail — 46 440 écrit contre 46 833 au PLF
2026 — et celle de France Travail — 53 200 contre 53 052. La base de l'auteur
vient d'ailleurs, et l'écart reste affiché jusqu'à arbitrage.

### Ce que la source citée apporte, et ce qu'elle coûte

L'onglet `Flux` — `Gages` jusqu'au 20260917, même gabarit à la cellule près — est
la seule pièce du corpus qui écrive une source à côté de chaque montant. Elle est reprise telle quelle. Elle révèle du même coup que
**trois lignes reposent sur une pièce qui n'est pas au corpus** : le budget
initial 2025 de France Compétences, de France Travail et de l'ADEME, soit
14,2 Md€ de chiffrage.

L'auteur les a sourcés ailleurs et valide le chiffrage (A-113). Le signalement
reste sur les trois lignes — il dit d'où vient le montant — mais il ne vaut plus
réserve. **Distinction à tenir** : une pièce absente qu'on n'a pas cherchée est
un trou ; une pièce absente du corpus mais sourcée ailleurs est un renvoi.

## La couche budgétaire — titres, traitements, qualifications

Depuis le 20260917 cet onglet est **éclaté en deux** : `SynthèseR` porte la
synthèse de restitution et les postes nommés, `Economies R` porte la grille, les
missions, les programmes et la couche de décision. Ensemble ils tiennent les
quatre blocs et la couche de décision qu'aucune autre pièce ne détient.

| bloc | lignes | ce qu'il porte |
|---|---|---|
| grille | 1 à 4 | dix catégories LOLF, crédits de paiement, part supprimable en année 1 |
| paramètres | 5 à 19, colonnes D:I | salaire moyen, assiettes non régaliennes, ETP supprimés, fusion du crédit d'impôt, bourse |
| postes | 5 à 23, colonnes K:T | 41 postes nommés, en paires libellé / valeur |
| missions et programmes | 25 à 226 | 35 missions, 128 programmes, **et le traitement retenu** |

### Les qualifications, et pourquoi elles décident de tout

**Un montant sans qualification n'est pas un chiffre, c'est une apparence.** Les
mêmes cellules du même onglet portent des enveloppes, des parts supprimables et
des économies déjà restituées.

| qualification | unité | se somme avec |
|---|---|---|
| crédit porté au PLF | M€ | les autres crédits |
| part supprimable dès l'année 1 | M€ | les autres parts supprimables |
| assiette d'un poste nommé | M€ | **rien** |
| économie à horizon 1 an | M€ | les autres économies à horizon 1 an |
| économie supplémentaire | M€ | les autres économies supplémentaires |
| effectif | ETP | les autres effectifs |
| paramètre de calcul | € | **rien** |

La règle de lecture d'un poste porte sur le libellé écrit dans la cellule :
« dont X » et « T2/T6 X » sont des assiettes ; « Economie à horizon 1 an » est
l'économie d'année 1 ; « Economie supplémentaire » est ce qui est restitué
ensuite ; **« sur X » est une économie, pas une assiette** — quatre postes le
prouvent, et ils sont écrits à la main plutôt que déduits d'un préfixe (A-116).
*Les libellés antérieurs — « gage CSG », « pérenne » — ne sont plus lus ici : ils
vivent à `appareil/socle_0910.py`, avec les adresses de la même génération.*

Le patron se lit alors sans effort. L'APL : assiette 16 116,74 M€, économie
à horizon 1 an 5 372,25, supplémentaire 10 744,49 — un tiers puis deux tiers. Les
exonérations d'emploi à domicile : assiette 1 180,12, 354,04 puis 708,07 —
**30 % puis 60 %, le socle de 10 % restant**, ce qui est la forme exacte d'une
« sortie en 3 ans ». L'AME : assiette 1 216,30, économie 1 094,67 — 90 %, ce qui
est le « hors 10 % pour soins urgents » de l'hypothèse.

### Les traitements, la couche de décision

Chaque programme porte, pour chacune des cinq catégories de transfert, un mot.
Sept valeurs, pas une de plus : un mot inconnu sort en échec.

| mot | ce que c'est | retire le crédit ? |
|---|---|---|
| Oui | champ non indispensable | oui, année 1 |
| En 3 ans | extinction en trois ans | oui, trois ans |
| Fusion CI | absorbé par l'aide fondamentale universelle | **non** — change de véhicule |
| Bourse | basculé en bourse | **non** — change de forme |
| Sécu | transféré à la sécurité sociale | **non** — quitte l'État, pas la dépense publique |
| Flux OM | laissé au flux outre-mer | non |
| X (colonne J) | mission régalienne | non — sort des assiettes « hors régalien » |

Compter Fusion CI, Bourse ou Sécu en économie gonflerait le chiffrage de ce qui
n'a fait que bouger.

**La lecture se prouve.** La part supprimable affichée en tête se retrouve
exactement en sommant les crédits des programmes marqués « Oui » : 6 728,42 en
catégorie 32, 21 827,40 en 61, 7 761,51 en 63, 13 543,42 en 64. Les catégories 62 et 64
sortent en `#VALUE!` après conversion ; elles se recomposent à 15 282,13 et
13 543,42 M€ et s'affichent en le disant — **recomposer n'est pas corriger**
(A-120). **Le `#VALUE!` n'est pas au classeur** : le `.xls` d'origine porte les
deux valeurs en cache, et c'est le recalcul de `soffice` à la conversion qui les
casse — une cellule sur l'état antérieur, deux sur les pièces du 20260917.
L'attribution au classeur était fausse ; elle est corrigée ici.

### La part budgétaire d'une économie, écrite pour trois lignes sur cinq

Elle se déduisait par soustraction. Un résidu n'est pas une source.

**Deux des cinq postes qui l'écrivaient ont disparu au dépôt du 20260917**, et
**ils se retirent.** *Tranché par l'auteur le 20260921 — question 28, « on peut
retirer, on reconstruira au besoin » (`A-422`).* Le bloc des postes nommés de
l'ancien onglet « Synthèse » portait « sur FrComp. » pour 434,071252 M€ et
« sur culture » pour 516,998084 M€ ; la synthèse de restitution ne détaille ni
France Compétences ni le CNC, qu'elle range en « Autres ».

**Les deux bouclages de `S8` qui les visaient sont retirés, non laissés en
échec** : un bouclage qui porte sur une grandeur que le corpus ne revendique
plus n'a pas d'objet. `S8` sort **30 bouclages sur 30**.

**Ce qui subsiste et ce qui disparaît.** L'écart arithmétique reste un fait —
10,6 au classeur contre 10,125 recomposés, 1,3 contre 0,750 — et il se qualifie
toujours en part budgétaire au sens de la règle des trois cas. **Ce qui
disparaît, c'est la prétention à le sourcer** : plus aucune pièce ne l'écrit, et
la remettre par soustraction serait revenir au résidu. Si le besoin revient, les
voies sont nommées — le budget initial 2025 de France Compétences (A-113) pour
le premier, l'auteur pour le périmètre de « sur culture ».

Les trois autres se relisent à leur nouvelle adresse : France Travail en
`C20`, `C21`, `D20` et `D21` de `SynthèseR`, l'ADEME en `G20` et `G21`,
MaPrimeRénov' en `F20` — cette dernière ayant changé de bloc, des transferts aux
ménages au détail des opérateurs, sans que son montant bouge.

| ligne du chiffrage | taxes | poste budgétaire | total | classeur |
|---|---|---|---|---|
| France Compétences | 10,125 | **retiré** — n'est plus écrit nulle part | — | 10,6 |
| France Travail | — | 2,734 · cat. 32, T2 et T6 | 2,734 | 2,7 |
| CNC et subventions culturelles | 0,750 | **retiré** — n'est plus écrit nulle part | — | 1,3 |
| ADEME | — | 0,921 · cat. 32, horizon 1 an + supplémentaire | 0,921 | 0,9 |
| MaPrimeRénov' | — | 1,333 · cat. 61 « MPR (Anah) » | 1,333 | 1,3 |

### Ce que la couche de décision ne couvre pas

128 programmes portent un traitement ; le PLF en compte 162. Ce qui échappe se
nomme plutôt que de se supposer :

- **141 Md€ de remboursements et dégrèvements** (programmes 200 et 201), crédits
  évaluatifs — hors périmètre par nature, ce n'est pas une dépense de politique
  publique ;
- **1,15 Md€ de comptes d'affectation spéciale** (pensions) ;
- **273 M€ sur deux programmes ordinaires** — fonds de soutien aux emprunts
  toxiques (178,6) et Épargne (94,8) ;
- le **programme 368**, absent du bloc de détail alors que sa ligne de mission le
  compte : 52,9 M€ de titre 2 dans l'agrégat, pas dans le détail.

## Ce qui n'est pas encore lu

- **La jonction avec le tableau de référence.** Le classeur `Synthèse Calculs`
  porte 1 336 formules et **aucune référence externe** : ses entrées sont
  saisies à la main depuis les sectoriels. Le socle permet de vérifier ces
  saisies ; il ne les remplace pas. Sont désormais importés **et bouclés**
  l'arbre des économies, la grande synthèse, `Fusion taxes`, `CI unique`,
  `CSG` et `Perdants` ; restent lus sans être importés les onglets `Manuscrit`,
  `Manifeste` et `Détail Niches`, et les douze feuilles de graphiques, qui sont
  des vues et non des sources.
- **`Capitalisation` est à importer, avec son bouclage.** *Tranché par l'auteur
  le 20260921 — question 24 (`A-421`).* Il porte l'horizon de sept ans de la
  sortie des fonctionnaires, dernier onglet du classeur de calculs que le second
  cercle n'avait pas repris. Lot d'appareil sur le modèle des sept bouclages
  neufs, jeu de fautes et jeu de justes compris. **Jusqu'à ce lot, l'horizon de
  sept ans reste `estimé`.**
- **`Manifeste` et `Perdants` n'ont pas de successeur au 20260917, et leur
  contenu est gardé.** *Tranché par l'auteur le 20260921 — question 29 : les
  deux onglets ont été retirés pour la présentation, non parce qu'ils étaient
  caducs.* Le porteur durable est
  `livrables/extrait_classeurs_anterieurs_20260917.md`, qui en porte la recopie
  cellule à cellule — `Manifeste` 35×13, la ventilation des baisses de dépense
  par catégorie de perdant, 183,954667 Md€ au total ; `Perdants` 16×8, le
  dénombrement des populations et des perdants à 1 an et à 3 ans. **C'est à ce
  document que `S15` et les deux entrées de `REF_chiffres` — 236 Md€/an et
  30 Md€/an — se sourcent désormais**, et non plus à un onglet de classeur.
- **Les économies des ODAC-ODAL**, comptées et jamais valorisées : 749
  organismes portent un régime, aucun ne porte un montant — sauf les trois
  qu'une ligne du chiffrage nomme.
- **Les 145 affectataires de taxe qui ne sont pas opérateurs du PLF.** Ils sont
  rattachables aux ODAC-ODAL comme les trois qui le sont déjà : c'est le travail
  des 269 appariements, dont la cible est **la liste des opérateurs ou celle des
  ODAC-ODAL**, et non la première seule (A-114).
- **Le résidu « autres »** de la rubrique des opérateurs, 2,8 Md€, que le
  classeur ne détaille pas.
- **Les comptes des administrations locales** — deux classeurs Insee, non
  ouverts. **La dépense d'éducation est ouverte depuis le 20260917** : classeur
  DEPP « L'état de l'École 2025 », onglet `Figure 9.1`, série 2019-2024 en euros
  courants, en euros constants aux prix du PIB 2024 et en part du PIB. Les onze
  autres figures du classeur ne sont pas importées.
- **Les douze feuilles de graphiques** du classeur de synthèse, qui sont des
  vues et non des sources.
- **Ce qui n'existe qu'en PDF** — jaunes budgétaires. Un extracteur par gabarit, plus fragile qu'un import de classeur.
  **Règle à tenir dès maintenant : un chiffre tiré d'un PDF porte sa page.**

---

## Comment on bascule sur un PLF neuf

La grille est écrite pour que la bascule soit un rapport et non une reprise.

1. Convertir les nouveaux classeurs et rejouer `socle_budgetaire.py` : on obtient
   un socle millésimé de plus.
2. Comparer les deux socles par leurs identifiants. Quatre listes sortent : les
   objets **disparus**, dont l'économie tombe ; les **nouveaux**, sans régime, à
   instruire ; ceux dont le **montant a bougé** au-delà d'un seuil, dont
   l'économie change mécaniquement ; ceux dont le **libellé ou le périmètre a
   changé**, dont le régime est peut-être caduc.
3. Ne traiter que ces quatre listes. Le reste se rejoue seul.
4. Rejouer les bouclages contre les nouveaux totaux du classeur.

**Le variantage suit la même mécanique** : un second jeu de régimes sur le même
socle, nommé, avec son écart au scénario de référence.

---

## Les hypothèses, qui ne sont ni des faits ni des paramètres

Un chiffre ne vaut que sous ce qui le fonde. Le livre pose ses hypothèses en
littéraire — un multiplicateur de 0,5, un socle conservé de 15 %, une durée de
retraite de 24 ans, un chiffrage déclaré prudent — et **elles n'étaient portées
par aucun référentiel**.

Elles vivent désormais dans `appareil/hypotheses_doctrine.py` : seize entrées,
avec leur nature, leur sens — minorant, majorant, neutre —, leur domaine, la
note ou le passage qui les porte, et les nœuds qu'elles commandent.

**Une hypothèse ne recopie pas le verbatim du livre.** Elle porte un repère
court, dont `controle_hypotheses.py` vérifie la présence littérale au manuscrit.
Un repère qui ne se retrouve plus est une alerte : soit le manuscrit a changé,
soit la recopie a dérivé.

C'est la couche qui manquait pour varianter : quand un PLF neuf arrive, ce sont
les hypothèses qu'on réexamine, et les faits se recalculent.

**Les deux écarts relevés entre l'hypothèse annoncée et celle appliquée sont
clos.** *Tranché par l'auteur le 20260921 — question 27.* La doctrine et le
classeur disent la même chose : **3 % de rendement du patrimoine**, et
**600 Md€ à restituer** — les 20 000 € par foyer — sur **606,972666 Md€
valorisés**, après une coupe de 10 % sur les logements publics et le parc social
et de 6,365 Md€ sur les participations financières.

**La marge de 6,97 Md€ n'est pas un écart : c'est la prudence assumée.** On
valorise un peu plus qu'on ne promet, et la promesse tient donc même si la
valorisation se révèle haute. La grille ne relève plus ces deux points.
