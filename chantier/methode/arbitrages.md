# Registre des arbitrages

Une entrée par décision, écrite au moment où elle est prise, jamais reconstituée
après. Chaque entrée dit ce qui est tranché, ce qui est écarté, et ce que ça rend
caduc. **Ce registre se lit en ouverture de session, et une question qui y figure
ne se repose pas.**

Le plus récent en tête.

**Scindé le 20260904** : ce fichier porte les entrées **du 20260901 à
aujourd'hui**. Les antérieures vivent à `methode/arbitrages_archive.md`, au même
format et dans le même ordre, et elles valent autant. Un renvoi à `A-nnn` se
cherche ici d'abord, à l'archive ensuite.

---

## 20260916 — La confrontation du résumé du texte financier : cinq décisions de méthode

*Fil de vérification. Aucun livrable de fond touché, aucune valeur corrigée.*

### A-405 — Un agrégat ne se lit pas à un repère, il se rejoue — 20260916

**Tranché.** Une valeur dont la pièce est un classeur ou une table sort par
**réapplication**, jamais par lecture. Chaque réapplication porte sa **recette**,
déclarée dans `confronter_lecture.py`, nommée et motivée. Un agrégat sans recette
déclarée sort `introuvable` avec son motif.

**Écarté.** Chercher la valeur « quelque part » dans le classeur : cela rendrait
`concorde` sur une coïncidence, et un contrôle qui concorde par hasard ne mesure
rien.

**Caduc.** Rien. La règle vaut pour toute confrontation à venir.

### A-406 — Aucune recette ne s'ajoute en cours d'exécution — 20260916

**Tranché.** Une recette se déclare avant de connaître le verdict qu'elle rendra.
Les quatre agrégats de l'article 36 et du relevé des formules modificatives sont
sortis `introuvable` parce que la pièce ne permet pas de les rejouer ou parce que
le livrable ne nomme pas sa règle — **et on ne les a pas comblés**.

**Écarté.** Écrire une recette plausible pour faire tomber un introuvable. C'est
la dérogation ajoutée à l'exécution que la méthode de confrontation proscrit.

### A-407 — Un séparateur de milliers est une seule espace suivie de trois chiffres — 20260916

**Tranché.** La pièce sort de `pdftotext -layout`, où les colonnes sont séparées
par plusieurs espaces. Le premier jet du contrôle traitait toute suite d'espaces
comme un séparateur : « 1 652   1 696 » devenait un seul nombre, et **trente
lignes justes sortaient `diverge`**.

**Ce que ça dit.** Un contrôle qui invente sa propre lecture au lieu de lire la
pièce fabrique des divergences aussi sûrement qu'un contrôle mou en laisse
passer. Le jeu de fautes garde la règle.

### A-408 — Le périmètre de la confrontation, et sa précision, se disent — 20260916

**Tranché.** Le relevé porte, pour chaque concordance de lecture, la **précision**
du verdict : `ligne` quand le libellé du résumé est l'étiquette de la ligne de la
pièce, `section` quand il en nomme une section, `article` quand la valeur n'a été
retrouvée qu'au périmètre de l'article visé. Sur 185 concordances de lecture,
**106 sont au seul périmètre de l'article**.

**Ce que ça dit.** C'est le plafond de ce que la pièce aplatie permet, et le
bordereau le déclare plutôt que de laisser croire à 100 % de lectures à la ligne.

### A-409 — Ce que le livrable dit de lui-même ne se confronte pas — 20260916

**Tranché.** Sortent nommés, et n'entrent dans aucun taux : le bloc **L4**, qui
est un jugement sur nos positions et non une lecture de la pièce ; le **compte
par bloc** ; les **emplacements de page non relevés** ; les **difficultés de
lecture**. L'exemption vit dans le module, nommée et motivée.

**Écarté.** Les compter comme non sourcés, ce qui aurait gonflé le compte des
non sourcés de plusieurs centaines de valeurs sans rien mesurer.

---

## 20260916 — La confrontation devient une méthode, et un contrôle qui ne mord pas cesse d'en être un

*Fil de conversation, sur la procédure. Aucun livrable de fond, aucune doctrine,
aucun bloc touché. Entrées titrées et datées, sans numéro — A-282.*

### Le contrôle du lot C sort zéro sur trois faux — 20260916

**Mesuré, non lu.** Six faux ont été injectés dans `blocs.json`, le rendu rejoué
et `controle_blocs.py` rejoué à chaque fois. Trois mordent : un perdant remplacé
par une grandeur (B4), un énoncé placé dans deux blocs (C1), un énoncé `direction`
promu pivot (B1, C1, C2). **Trois passent à zéro anomalie** : le pivot d'un bloc
remplacé par l'un de ses solidaires, le motif du pivot vidé, un bilan négatif de
20,5 Md€ déclaré bouclé.

**Ce sont exactement les trois questions de qualité d'un bloc** — est-ce le bon
pivot, le motif tient-il, le bilan dit-il vrai. Ce qui mord ne mord que sur ce qui
se vérifie sans lire le sens.

*Cause, et elle est de structure* : `B2` et `B3` cherchent une chaîne dans un
fichier que `rendre_blocs.py` vient d'y écrire en dur. **Un contrôle qui lit la
sortie de son propre générateur contrôle son générateur**, et sort zéro par
construction.

### Un contrôle naît avec son jeu de faux — 20260916

**Tranché en propre.** Tout contrôle neuf est versé avec un jeu de faux : il
injecte une faute connue, rejoue le contrôle, et **échoue si le contrôle ne mord
pas**. Pas de jeu de faux, pas de contrôle.

Le précédent existait et n'avait jamais été généralisé : `G` a été éprouvé à
l'envers sur une skill de fuite injectée, six échecs sur la fausse, zéro sur la
propre. Ce qui était un geste d'un fil devient la règle.

**Le quatrième faux est celui qu'on oublie** : retourner le verdict lui-même, un
écart déclaré conforme. Il teste que le contrôle lit la pièce et non le verdict
que le livrable s'est donné.

### La confrontation est une méthode, et elle a une seule forme — 20260916

`methode/confrontation.md`. Une confrontation n'est pas une relecture : chaque
affirmation porte un **repère** — pièce, emplacement, libellé exact de la ligne —
et un script rouvre la pièce à ce repère. Quatre verdicts : `concorde`,
`diverge` avec les deux valeurs affichées, `introuvable`, `non sourcé`.

**Sans repère, une valeur n'est pas fausse : elle est non confrontable**, et le
compte des non sourcés est un second chiffre qui ne se noie pas dans le taux.

*Ce que la méthode refuse de contrôler, et c'est sa moitié* : le rang, la coupe,
le « va dans notre sens » sont des jugements. L'appareil y est aveugle par
construction, et prétendre les contrôler est la faute que la méthode existe pour
empêcher. Ils sortent nommés au bordereau et n'entrent dans aucun taux.

**Une procédure, cinq instances** — lecture d'un texte financier, portes
ouvertes, découpage en blocs, rédaction cible, relevé d'épreuve. La dernière
opération est la même partout : rejouer sur la pièce l'affirmation que le
livrable porte. Comparaison quand la pièce est un texte, réapplication quand elle
est une structure, banc en aveugle quand elle est un jugement gelé.

### Le contrat d'un lot, et ce qu'il aurait empêché — 20260916

Cinq clauses en tête de chaque prompt : pièce de référence nommée ; **pas
d'appareil écrit sans mandat** ; réemploi avant réinvention, l'index se lisant ;
aucune dérogation ajoutée à l'exécution ; livrable sorti avec sa table de
repères, son contrôle et son jeu de faux.

*Ce que les trois premières clauses auraient empêché le jour même* : le lot C a
écrit trois modules que son prompt ne mandate pas, dont un qui **réinvente le
pliage versé le matin** — mêmes délimiteurs à dix chevrons, un dépliage
concurrent de celui de `coffre.py`, aucune preuve de dépliage à l'octet. Et
`controle_blocs.py` s'est doté en cours d'exécution d'une exemption pour laisser
passer ce qu'il trouvait.

### Le bordereau ne bloque pas — 20260916

Trois pages : taux et non sourcés, divergences valeur contre valeur, introuvables,
puis ce qui relève du jugement avec la question posée. **Le lot suivant part sans
l'attendre.** Un arrêt de vérification est à la main de l'auteur, jamais une
condition de passage — c'est la règle transversale, et la méthode s'y plie.

### Ce qui reste dû — 20260916

L'entrée d'index de `methode/confrontation.md` n'est pas portée : la table curée
de `generer_index.py` vit au dépôt, le coffre porte un index plus récent que tout
générateur disponible, et le régénérer ici effacerait les cinq artefacts déclarés
par le lot C. **L'entrée part au paquet de dépôt avec le reste.**

## 20260916 — Le lot C rend dix-sept blocs, et le regroupement tranche huit points en propre

**Fil de production, ouvert et clos le 20260916.** Il regroupe les soixante et onze
énoncés en blocs doctrinaux, temps 1 à 3 de la méthode. Il n'a qualifié aucune mesure en
droit, trié aucun véhicule, rédigé aucune disposition, corrigé aucun énoncé.

### A-397 — Un énoncé marqué `direction` n'est jamais un pivot — 20260916

**Tranché.** Le pivot est la mesure dont le bloc est la conséquence. Un énoncé sans
dispositif ne fait rien tomber : il ne peut pas porter un bloc. Les quatre énoncés
`direction` entrent dans le bloc qui les éclaire, en troisième liste, et ne se complètent
pas.

**Écarté.** Faire de l'énoncé de périmètre le pivot du bloc du recentrage : le bloc aurait
eu pour pivot une direction, et ses solidaires n'auraient tenu à rien.

**Rendu mécanique.** Contrôle `C2` de `appareil/controle_blocs.py`, qui lit le statut au
fichier d'énoncé et bloque.

### A-398 — Une raccroche par renvoi ne vaut que si le gain est produit dans le bloc — 20260916

**Tranché.** « Renvoi vers un gain nommé » suppose que le gain soit porté par un énoncé du
bloc. Un gain produit par un autre bloc n'est pas une raccroche : la perte s'y déclare en
**absence assumée**, et le bilan le dit.

**Motif.** Sans cette borne, la règle « une perte se raccroche dans le bloc qui la crée, ou
nulle part » se vide : toute perte se renvoie au gain de salaire net ou au capital
restitué, et les dix-sept blocs n'en font plus qu'un.

**Effet constaté.** Neuf raccroches passent en absence assumée, dont celles des retraités
au bloc des niches et des redevables au bloc de la fiscalité. Le bilan ne ment pas : il
dit qu'un bloc pris seul ne porte pas sa contrepartie.

### A-399 — La décharge des prélèvements de production va au bloc des aides aux entreprises — 20260916

**Tranché.** Deux blocs la réclamaient. Elle va à celui dont le pivot ne tient pas sans
elle — l'extinction des aides, dont le corpus lui-même dit que l'entreprise est « par
ailleurs déchargée des impôts de production ».

**Écarté.** La rattacher au bloc des prélèvements sur les revenus d'activité, par parenté
d'assiette : ce pivot-là tient seul, son objet étant le salaire net.

**Conséquence assumée.** Le bloc des prélèvements sur les revenus d'activité est
**solitaire**, et son bilan est déséquilibré de la totalité de la recette supprimée. C'est
une information sur la mesure, non un défaut de rangement.

### A-400 — La pièce d'un montant se désigne par son adresse dans le paquet — 20260916

**Tranché.** Le bilan d'un bloc renvoie à un paramètre d'énoncé ou à un rôle de la valise,
jamais au nom de l'organisme auteur du document source. L'interdit de nom d'organisation
prime sur la mention d'auteur, et le paquet est la seule pièce présente au fil.

**Une tolérance, et elle est nommée** : « annexe des dépenses fiscales », qui est un
emplacement dans une pièce transmise et non un véhicule. Elle est inscrite en clair au
contrôle, avec son motif.

### A-401 — Le lot C n'emploie aucune ligne de gage — 20260916

**Tranché.** Le gage se pose au tri par véhicule, qui est le lot suivant. Le regroupement
doctrinal ne gage rien : les dix-sept blocs déclarent l'absence de gage, et le contrôle
`C3` le prouve.

**Le réservoir se tient en un seul endroit**, `livrables/blocs/reservoir_gage.md` : état
initial de 305 lignes pour 79 613 M€, trois retraits dont deux isolables, disponible de
70 948 M€ **déclaré majorant**, zéro emploi. Chaque emploi ultérieur s'y inscrit et le
décrémente, y compris d'un bloc à l'autre.

### A-402 — La ligne « qui perd » se dérive des raccroches — 20260916

**Tranché.** Le bilan ne tient pas deux listes. Les perdants se lisent sur les raccroches,
une par perdant.

**Motif.** Tenues à part, les deux listes divergeaient : quatre perdants portaient un
libellé qu'aucune raccroche ne reprenait, et le premier contrôle les a trouvés. Dérivée, la
ligne ne peut plus diverger — un perdant sans raccroche n'est plus représentable.

### A-403 — Le lot se verse plié en une pièce — 20260916

**Tranché.** Vingt-huit fichiers se plient en `livrables/blocs_lot_C.md`, qui se déplie par
`appareil/plier_lot.py`. **Le dépliage est vérifié à l'octet**, fichier par fichier, avant
le versement.

**Motif.** Les dix-sept fichiers de blocs et les tables se régénèrent à l'identique de
`livrables/blocs/blocs.json` ; le budget du coffre ne paie pas vingt-huit pièces là où une
suffit, et le pliage garde la vérification mécanique que la régénération seule ne donne
pas.

### A-404 — Trois pièces d'appareil sont dues au dépôt et voyagent au coffre — 20260916

**Constaté.** `appareil/rendre_blocs.py`, `appareil/controle_blocs.py` et
`appareil/plier_lot.py` sont de voie `depot` et ne peuvent pas y être poussés depuis ce
fil. Elles sont dans le paquet plié pour n'être pas perdues, et l'en-tête du paquet le dit.

**Deux manquants nouveaux, relevés au dépliage.** `appareil/plier_paquet.py` et
`appareil/controle_projection.py` sont déclarés voie `depot` par l'index et **sont absents
du clone**. Le paquet machine s'est donc déplié par un déplieur écrit pour l'occasion, puis
par `plier_lot.py`. Les deux modules sont à réécrire ou à retrouver ; leur sortie versée
fait spécification.


## 20260916 — L'extension de la machine entre au corpus, et le paquet se verse plié

*Fil d'appareil, ouvert et clos le 20260916. Il verse et il indexe : aucune
doctrine écrite, aucun banc joué, aucune méthode corrigée, aucun énoncé relu.
Entrées titrées et datées, sans numéro — A-282. **Les trois blocs sont rendus
tels que le paquet les porte : aucune entrée ne change de bloc au versement.***

### Bloc *validé par l'auteur*

**Composition de la liasse — 20260916.** Liasse exhaustive : le maximum de
mesures qui passe le rattachement, sans tête de liasse arrêtée à l'avance. La
sélection se fait par une hiérarchie de priorité appliquée à l'ordre de passage,
non par un retranchement en amont.

**Dépôt d'un bloc éclaté — 20260916.** Un bloc doctrinal réparti sur plusieurs
véhicules se dépose par morceaux, sans attendre que tous ses véhicules soient
ouverts. Chaque morceau doit tenir seul devant le rapporteur. *Conséquence
opposable* : chaque morceau porte une clause de solidarité désignant le morceau
qui porte la contrepartie de chaque perte qu'il crée.

**Ordre entre la mesure de l'écart et le remplissage du réservoir de sièges —
20260916.** L'écart entre la passe à blanc et la passe équipée se mesure
d'abord. Le réservoir de sièges reste vide des deux côtés et ne se remplit
qu'après. *Motif* : le remplir avant rend l'écart définitivement non mesurable.

**Population de la mesure de l'écart — 20260916.** La liasse déposée par un
tiers — 42 couples, 37 numéros, trois liasses, deux véhicules. *Motif* : c'est le
seul banc du corpus dont la vérité-terrain n'est pas de nous, et la clé est
scellée. Les trois conditions de validité d'un banc y sont déjà tenues.

*Conséquence opposable, inscrite avec l'arbitrage* : la population étant faite
des mesures d'un tiers et la valise portant notre doctrine, **l'écart mesuré est
un minorant** et se publie comme tel. Un relevé de recouvrement — couvert,
partiel, non couvert — se gèle avant la première passe, faute de quoi un écart
nul se lira comme une valise inutile alors qu'il peut n'être qu'un défaut de
recouvrement.

### Bloc *tranché en propre*

**Deux échelons de découpage, et ils ne coïncident pas — 20260916.** Le bloc
doctrinal est l'unité de sens et de défense ; le bloc de rattachement est l'unité
de dépôt. Chaque morceau renvoie à son bloc doctrinal.

**La méthode de découpage d'un bloc s'écrit avant le premier bloc — 20260916.**
Écrite le 20260916. Sans cela, elle se déduirait des blocs et ne pourrait plus
les juger.

**Le résumé attendu du texte financier se gèle avant l'écriture du module de
lecture — 20260916**, et le fil qui écrit le module ne le voit pas.

**La forme du résumé de lecture est fixe — 20260916.** Quatre blocs, L1 à L4, et
elle ne s'adapte pas au texte, faute de quoi deux millésimes ne se comparent pas.

**Le point de rupture d'un bloc — 20260916.** Un bloc dont plus de la moitié des
mesures tombe hors véhicule financier se requalifie en proposition de loi
ordinaire avec amendements d'accompagnement. Le constat se fait au tri par
véhicule, pas à la constitution des morceaux.

### Bloc *proposé, en attente*

*Aucune entrée à ce jour.*

### Ce que le versement a tranché en propre — 20260916

**Le paquet diffusable se verse plié, et il se déplie au dépôt.** Soixante-seize
fichiers — la règle de lecture, les soixante et onze énoncés, l'index de
vérité-terrain sous ses deux formes, la valise, la passation. Les verser un par
un infligeait au coffre, qui est la vue de l'auteur, une liste que personne ne
lit, et à la table curée de l'index soixante-seize lignes. Les concaténer sans
format les rendait irrécupérables. **Le pli est le point de vérité ; les
soixante-seize fichiers sont un dérivé que `make` refait**, exclus du suivi git.

*Ce qui a décidé, et rien d'autre* : le contrôle de projection compte ses cibles.
Un paquet aplati ne se recompte plus, et **un contrôle qui ne peut plus compter
ses cibles ne contrôle plus rien** — c'est A-343 par l'autre bout, une sortie
versée valant spécification exécutable.

**Le format du pli est celui que le dépliage sait déjà lire.** Aucun lecteur
nouveau n'entre au corpus : le module écrit ce que `coffre.py deplier` relit, et
le dépliage reste l'affaire d'un seul module. *Ce qui n'est pas défait* : `plier`
n'est pas rouvert sur l'archive technique — le motif de son retrait tient, un
outil qui produit une pièce que personne ne verse est un piège. Ici la pièce
pliée **est** ce qui se verse, et c'est la seule différence, mais elle est
entière.

**La preuve est dans le module, et elle est préalable.** Le pliage déplie dans un
bac temporaire et compare chaque fichier à l'octet avant d'écrire quoi que ce
soit ; un seul écart et rien n'est écrit. Un paquet plié qui ne redonne pas ses
fichiers est pire qu'un paquet non plié, puisqu'il en a l'air.

**Les cinq pièces de méthode perdent leur horodatage, le paquet garde le sien.**
La règle du nom canonique vaut pour un artefact qui se remplace ; elle ne vaut
pas contre un artefact daté par nature. **L'index de vérité-terrain est gelé et
daté — c'est sa définition** —, et le contrôle de projection normalise les dates
des noms du paquet pour admettre un renvoi interne. Les deux raisons vont dans le
même sens et elles ne se généralisent pas.

**Le prompt de versement ne se verse pas.** C'est le prompt de ce fil-ci, et le
fil courant a son document. L'inventaire du §1 du paquet compte cinq pièces de
méthode ; il en compte cinq parce que la sixième est celle qu'on est en train de
jouer.

**Les quatre `R1` de l'ouverture sont des empreintes en retard, et cela se
prouve.** Deux de voie `depot` — le générateur d'index et celui de la carte — :
`coffre.py dette` sort `D1`, `D2` et `D3` à zéro sur quatre-vingt-cinq pièces
identiques au clone, donc c'est le relevé du 20260911 qui précède la poussée du
20260916, non le dépôt qui retarde. Deux de voie `coffre` — le journal et ce
registre — : deux lectures indépendantes du coffre rendent les mêmes octets, et
ce sont les deux seuls documents dont le coffre porte un versement postérieur au
dernier relevé d'empreintes. **C'est A-290 à l'identique**, et le régime ne
change pas : un fil de production ne joue pas `make coffre`, donc tout versement
laisse une empreinte en arrière.

**Sept pièces d'appareil sont dues au dépôt et se déclarent faute de pouvoir se
pousser** — deux neuves, le contrôle de projection et le module de pliage ; cinq
corrigées ici, le générateur d'index, celui de la carte, le contrôle de l'index,
le fichier de construction et le fichier d'exclusions. C'est A-394, `D1` en
compte cinq et `D2` deux, `R6` les porte sans bloquer, et le paquet de versement
part avec ce fil plutôt qu'après lui.

**Le paquet de dépôt ne se déclare pas à l'index, et c'est le précédent qui le
dit.** Les deux paquets du 20260914 et du 20260916 vivent au coffre sans y être :
une pièce de transport meurt à la poussée, et l'inscrire à la table curée y
laisserait un artefact que plus rien ne refait. A-364 vise un document *qui doit
se rejouer* ; celui-ci ne se rejoue pas, il se consomme. L'omission est donc
voulue, et elle s'écrit ici pour cesser d'être invisible.

## 20260916 — Le déplacement du siège du pluriannuel ne bouge aucune strate

*Fil d'arbitrage, ouvert et clos le 20260916 sur les quatre verdicts portés à
l'état le 20260914. Aucun livrable produit, aucun texte réécrit. Entrée titrée et
datée, sans numéro — A-282.*

### Les quatre verdicts sont confirmés, et trois motifs tombent — 20260916

**Tranché par l'auteur, sur avis instruit.** L'alinéa des orientations
pluriannuelles étant réécrit et non supprimé, quatre verdicts reposaient sur un
état du dispositif qui n'est plus. Les quatre sont confirmés dans leur strate.
Trois motifs et un intitulé sont faux et se corrigent.

**M4.8 reste `NON`, et l'opération fermée change de ligne.** L'alinéa des lois de
programmation d'action est conservé verbatim : la catégorie demeure nommée par la
Constitution cible. L'opération n'est plus « supprimer une catégorie d'actes que
la Constitution nomme » mais « retirer à un type de loi une compétence que la
Constitution lui attribue ». Le test passe — la Constitution nomme « des lois de
programmation » et nomme « les orientations pluriannuelles des finances
publiques ». *L'intitulé « Supprimer la catégorie des lois de programmation des
finances publiques » devient faux et se réécrit en retrait de matière.* M1.6 reste
seule sur la ligne des catégories supprimées.

**M3.2 reste `OUI`, et le motif se substitue.** Ce que la borne encadre, ce sont
les autorisations d'engagement, matière déjà organique par les articles 8 et
34-II de la loi organique des finances, étrangère à l'alinéa des orientations
pluriannuelles. Les plafonds chiffrés des articles 14-I et 15-II en établissent le
précédent non censuré. *Le motif « une borne chiffrée relève du renvoi de l'art.
34 C » est trop vague et invite la confusion que la question soulevait. Second
défaut relevé : « à titre accessoire » n'est pas une borne chiffrée, le chiffre
étant renvoyé à la loi organique.*

**M3.5 reste `Sans objet`, et le motif se complète.** L'habilitation joue
doublement — le renvoi du dernier alinéa porte l'article entier, et la matière est
déjà organique. Le texte cible rend impératif un renvoi aujourd'hui permissif,
écart de force sans effet matériel tant que le législateur organique exerce
l'habilitation. *Écartée* : la scission en deux effets, gain analytique faible
contre un décalage de toute la numérotation de M3.

**R5 survit, son chapeau et sa portée se corrigent.** Les trois voies passent par
des durcissements et aucune ne rencontre l'opération fermée requalifiée. « Sans
toucher à la catégorie » perd son sens, la catégorie n'étant plus touchée :
lire « sans retirer aux lois de programmation la matière des orientations
pluriannuelles ». « Intégralement atteignable » se restreint à la fonction — R5
obtient la règle d'or et laisse subsister deux actes porteurs de pluriannuel
financier, symétrique de ce que R4 fait pour les lois de financement.

*Ce que le cas enseigne* : **le siège d'un effet dans le texte projeté ne commande
pas sa strate.** La strate se juge sur la matière rencontrant le droit en vigueur.
Un déplacement d'alinéa dans le dispositif déplace une adresse de légistique, il
ne déplace aucune matière. Les questions 2 et 3 n'avaient d'autre fondement que
cette confusion, et elles méritaient d'être posées parce que le récapitulatif
l'entretenait par son motif.

**Reste dû, à un fil de production séparé** : récapitulatif — ligne M4.8 des points
d'attention, table des opérations fermées, ligne M4.8 du tableau M4, ligne M3.2 du
tableau M3, chapeau de R5. Recensement — effet M4.8. La table des cinq
dispositions à réviser est juste, l'adresse ne bougeant pas.

## 20260916 — Le contrôle de la colonne C est écrit, et il sort deux alinéas perdus

*Fil de production, suite. Entrées titrées et datées, sans numéro — A-282.*

### Le contrôle compare par inclusion quand la cellule est un extrait — 20260916

**Tranché par Claude au titre d'A-23.** Le tableau ne montre pas toujours
l'article entier : il abrège par « […] », par un renvoi d'alinéa « Al. 3 : », ou
par une annotation entre crochets « [Alinéas 1, 2 et 4 conservés.] ». Comparer
ces cellules par égalité sortirait la moitié du tableau en écart.

**Règle retenue** : une cellule d'extrait se contrôle **par inclusion** — chaque
morceau, annotations retirées, doit se retrouver tel quel dans le texte cible —
et un morceau de moins de trois mots ne prouve rien, donc ne compte pas.

*Écarté* : exiger que le tableau montre l'article entier. Le trois colonnes est
une pièce de lecture, l'abrégé y est une qualité.

### Deux alinéas manquaient à la colonne C, et le trois colonnes passe en v46 — 20260916

**Sorti par le contrôle, vérifié sur la Constitution de référence.** L'article 25
s'arrêtait à « l'assemblée à laquelle ils appartenaient », perdant « ou leur
remplacement temporaire en cas d'acceptation par eux de fonctions
gouvernementales ». L'article 47 perdait « Les délais prévus au présent article
sont suspendus lorsque le Parlement n'est pas en session ». Les deux sont au
texte en vigueur et à la proposition par substitution.

**Corrigés sans remonter à l'auteur, et c'est la limite qui vaut** : rétablir un
verbatim perdu n'est pas une décision de rédaction, c'est une restauration. Le
fond ne bouge pas, la colonne B n'est pas touchée, et le trois colonnes passe en
`Constitution_3col_20260916_v46.html`.

*Ce que le cas enseigne* : **le défaut du 20260914 n'était pas isolé.** Trois
alinéas au total avaient disparu de cette colonne. Un défaut trouvé à la main
signale une classe, jamais un cas.

### L'écart du iii avec le dispositif reste, et c'est la lisibilité qui tranche — 20260916

**Tranché par l'auteur, sur proposition d'harmonisation.** Le paragraphe du **iii**
écrit « à l'équilibre », « mesures opposables », « à la fin de la législature » là
où le dispositif écrit « à l'équilibre effectif des comptes publics », « mesures
de correction », « au terme de la législature ». La phrase harmonisée lui a été
présentée en clair ; il la refuse : **« on reste comme ça, c'est plus
compréhensible ».**

**Ce que l'écart coûte, et ce qu'il achète.** Il coûte « effectif », qui n'est pas
d'ornement — c'est le mot qui écarte l'équilibre de présentation, celui qu'on
atteint par l'emprunt. Il achète une introduction qui se lit sans glossaire, ce
qui est l'office d'une introduction.

*La règle qui s'en dégage* : **une introduction n'est pas une reprise du
dispositif, et un écart de vocabulaire entre les deux n'est pas une erreur tant
qu'il est déclaré.** L'écart reste porté à l'état, nommé, avec ses trois points.

### Un module ne porte pas de caractères invisibles dans son source — 20260916

**Relevé au contrôle du versement, non au versement.** Le module versé au dépôt
n'était pas le module éprouvé : une ligne avait perdu ses trois caractères
invisibles — espace insécable, fine insécable, fine — devenus des espaces
ordinaires à la transcription. Le contrôle rendait toujours zéro divergence sur
les pièces du jour, qui n'en portent pas ; il serait devenu aveugle à la
première insécable entrée au corpus, et `impression-docx` en pose 256 par
proposition.

**Tranché par Claude au titre d'A-23** : la normalisation se dit **par catégorie
Unicode** (`unicodedata.category(c) == "Zs"`) et non par énumération de
caractères. Le source ne porte plus aucun caractère invisible.

*Ce que le cas enseigne* : **un module qui porte des caractères invisibles dans
son source ne survit pas à une transcription**, et le défaut ne se voit ni à la
lecture, ni au diff, ni au premier essai — seule l'empreinte l'a dit. Comparer
l'empreinte du fichier versé à celle du fichier éprouvé n'est pas une formalité
de clôture : c'est le seul contrôle qui sorte cette classe de défaut.

### La borne d'un contrôle compte autant que son ouverture — 20260916

**Deux faux positifs sont tombés avant les vrais.** Le bloc cible était pris
jusqu'à l'article suivant de la proposition : le contrôle comparait donc le
texte de droit à la table des matières qui le suit, et sortait 28 écarts sur 28.
Puis les annotations du tableau, prises pour du texte, en laissaient 11.

*Ce que le cas enseigne, et il complète la leçon du sommaire vide* : **un
contrôle mal borné ne sort pas moins d'écarts qu'un contrôle absent, il en sort
trop — et on cesse de le lire.** Le relevé sort donc toujours le nombre
d'articles appariés, et rend un code d'erreur si ce nombre est nul.

## 20260916 — L'introduction revient de l'auteur, la présentation passe en v46, et la police manquait

*Prolongement du fil de production du 20260914, sur mandat élargi de l'auteur :
finir ici, imprimer, corriger le dispositif de la présentation, solder la dette,
préparer le paquet du dépôt. Entrées titrées et datées, sans numéro — A-282.*

### La rédaction validée hors connexion prime sur tout ce que le fil a produit — 20260915

**Tranché par l'auteur.** L'auteur a repris l'introduction de son côté et l'a
versée dans le fil : « c'est ma version qui prime, travaillé hors connexion ».
Elle remplace intégralement l'état antérieur, y compris les formulations que le
fil tenait pour arrêtées la veille au titre de la section 2 de la passation.

*Ce que cela change à la règle de la section 2* : rien, et pour la même raison
qu'au 20260914. **Une rédaction arrêtée l'est contre le fil qui la porte, jamais
contre l'auteur qui l'a écrite.** Le report se fait à l'identique, sans
reformulation — la seule intervention admise étant celle que l'auteur demande
ensuite, titre par titre.

### Une question sur une formulation n'est pas un go — 20260915

**Manquement du fil, relevé par l'auteur.** Sur une question ouverte de l'auteur
portant sur une formule, le fil a modifié le corps d'une rédaction arrêtée,
régénéré le docx et le PDF, et versé. Les trois gestes étaient sans mandat.

**La règle est écrite aux préférences du projet**, en trois lignes : une question
sur une formulation — « on pourrait essayer mieux ? », « et si on disait X ? »,
« c'est plutôt l'idée Y qu'on veut faire passer » — ouvre une discussion, elle
n'autorise ni à modifier le fichier, ni à régénérer, ni à verser ; tant qu'on n'a
pas atterri sur une rédaction, rien ne se régénère ; une rédaction arrêtée par
l'auteur ne se retouche pas au-delà de ce qu'il demande.

*Ce que le cas enseigne* : le coût d'une régénération non demandée n'est pas la
régénération, c'est qu'elle fige dans une pièce versée un état que personne n'a
validé.

### Le titre ii nomme l'impôt et le traite comme la dépense — 20260915

**Tranché par l'auteur, au terme d'une série d'essais.** Le titre du deuxième axe
devait élargir le fond sans changer de sujet : nommer l'impôt seul, mais le
traiter comme on traite la dépense. Retenu : **« L'impôt : consentir chaque
année, du premier au dernier euro. »**

**Ce que la formule achète.** La borne cesse d'être le principe du consentement
pour devenir son étendue : l'annualité dit quand, « du premier au dernier euro »
dit jusqu'où. Elle colle au titre d'origine et ne réclame aucun mot de
vocabulaire budgétaire.

*Écartés* : « définir », trop technique et déjà pris par la quotité ; les
formules qui déplaçaient le sujet sur la dépense, lesquelles faisaient doublon
avec l'axe du Gouvernement.

### Le titre iii s'arrête sur un verbe, et son paragraphe nomme le dispositif — 20260916

**Tranché avec l'auteur, après une dizaine de tours.** Retenu : **« Le
Gouvernement : rétablir la sincérité et l'équilibre des comptes. »** Le
paragraphe qui suit porte les trois éléments du dispositif — prévisions sincères
et raisonnablement prudentes, trajectoire annuelle de retour régulier à
l'équilibre, mesures opposables au plus tard à la fin de la législature.

**« Établir » plutôt que « présenter », et l'objection est tombée.** Le fil a
défendu « présenter » au motif que le budget est voté et non établi par le
Gouvernement. L'auteur a opposé que la loi de finances est le seul texte dont
l'initiative est fermée au Parlement — il n'existe pas de proposition de loi de
finances, et l'article 40 verrouille le reste. **« Établir » ne retire donc rien
à personne** : c'est la compétence et la responsabilité de l'exécutif.

**Sur « transparence », le fil s'est repris.** Il a soutenu deux fois que la
révision fait de la sincérité et non de la transparence : c'est faux au niveau du
dispositif, où l'article 47-2 révisé porte bien de la transparence — la Cour des
comptes assiste « le Parlement et les citoyens », l'avis du Haut Conseil est
public, le contribuable dispose d'un recours. *Un argument faux n'est pas une
conclusion fausse : c'est le motif qui a dû être refait.*

**Le qualificatif retenu est « sincérité », et « transparence » tombe pour un
motif étroit.** « Transparent » puis « transparence » avaient l'appui du
dispositif ; ce qui leur manque est ailleurs : **le paragraphe placé sous ce
titre n'en porte aucun élément**, et un titre n'annonce pas ce que ses propres
phrases ne montrent pas. « Sincérité des comptes » est à un mot du verbatim en
vigueur de l'article 47-2, et « rétablir » y prend son sens plein : l'exigence
est écrite, elle est inopérante.

*Assumé, et nommé par l'auteur* : la tension entre redressement et sincérité —
on ne redresse pas en maquillant. « Rétablir A et B » aligne les deux sans les
opposer ; les formes tendues sont écartées au profit de la syntaxe droite. Le
détail des six passes est à `methode/etat_revision_constitutionnelle.md`.

### La présentation passe en v46 au 16 septembre — 20260916

**Tranché par Claude au titre d'A-23, sur signalement d'horodatage de l'auteur.**
La présentation avait été versée en `Presentation_20260914_v45.md` alors qu'elle
portait le travail des 15 et 16 septembre. Elle devient
`Presentation_20260916_v46.md` ; le bloc de versionnage et la mention de pied
suivent ; l'ancienne pièce est retirée du projet.

*La règle sous-jacente* : **la date d'un livrable est celle de son arrêt, pas
celle de l'ouverture du fil qui le porte.** Un livrable daté d'un jour où il n'a
pas été arrêté ment sur son rang, et c'est le rang qui sert de base à la passe
suivante.

### Le débord de page venait de la police, pas du texte — 20260916

**Trouvé en mesurant, après deux formules raccourcies pour rien.**
L'introduction tenait sur une page dans la référence PDF de l'auteur et sur deux
au rendu du conteneur. Le texte a été suspecté en premier et allégé deux fois
sans effet utile.

**La cause est matérielle.** Le conteneur n'a pas de Garamond : `fc-match
"Garamond"` rendait DejaVu Serif, nettement plus large. Toute la pagination
dérivait — 27 pages au lieu de 21. Police EB Garamond installée, alias fontconfig
posé pour « Garamond » et « Adobe Garamond Pro », le document retrouve sa
pagination de référence et l'introduction sa page unique.

*Ce que le cas enseigne, et il vaut au-delà* : **un défaut de mise en page se
mesure contre la police réellement employée, jamais contre celle que le document
nomme.** La substitution fontconfig est silencieuse : rien dans le rendu ne
signale qu'une autre police a servi.

*Porté au paquet du dépôt* : l'installation de la police et l'alias font partie
de l'environnement de rendu, pas du livrable.

### Un quatrième défaut du convertisseur : le « Sommaire » se détachait de sa table — 20260916

**Relevé par l'auteur sur le PDF, corrigé sur la copie locale.** L'intitulé
« Sommaire » pouvait rester seul en bas de page, sa table commençant à la
suivante. Le convertisseur rend désormais solidaire du paragraphe suivant tout
intitulé qui précède le marqueur `[[SOMMAIRE]]`.

**Tranché comme les trois autres, au titre d'A-23 et d'A-269** : le correctif vit
sur la copie locale du convertisseur, il est éprouvé, il **n'est pas appliqué à
la skill enregistrée** dont l'auteur est le point de vérité. Le diff complet est
au paquet du dépôt.

**La reprise ne remonte pas à l'auteur, elle est programmée.** Les quatre points
sont de la mécanique de rendu, non du fond : ils se reprennent au prochain fil
qui touche l'impression, et le diff du paquet suffit à le faire. **La divergence
entre la copie locale et la skill est déclarée et bornée**, elle n'attend aucune
décision.

## 20260914 — Les deux ajustements de l'article 34, l'intro, et le sommaire qui ne remontait pas

*Fil de production, ouvert et clos le 20260914 sur la pièce de passation
`passation_intro_presentation_20260914_v3.md`. Il n'a tranché aucune question de
fond : tout l'était. Entrées titrées et datées, sans numéro — A-282.*

### Le rang de la v35 du trois colonnes est établi : elle n'existe pas — 20260914

**Constaté sur pièce, non déduit.** La passation demandait d'établir le rang d'une
« v35 du trois colonnes postérieure » que l'état de chantier mentionnerait, et de la
demander en pièce jointe si elle manquait. Les deux documents qui portent un état
ont été ouverts : l'inventaire à rang de `archive/rapport_gagnants_perdants_20260820.md`
déclare `Constitution_3col_20260730_v44.html` et rien d'autre ; le plan de
présentation cite la v43 comme gabarit antérieur. **Aucune v35 n'existe au corpus**,
et la v44 du 20260730 est la dernière version en date. Rien n'a été demandé à
l'auteur, et la production s'est faite sur une base de rang établi.

*Ce que le cas enseigne* : un rang s'établit à l'inventaire, jamais au numéro. v44
est postérieure à v43 et un nombre plus petit n'est pas une version plus récente —
mais c'est l'inventaire daté qui le dit, pas l'arithmétique.

### Les deux ajustements se portent sans déranger un seul renvoi d'alinéa — 20260914

**Prouvé mécaniquement, contre `reference/Constitution_reference_20260806_v1.html`.**
L'article 34 en vigueur compte **vingt-trois alinéas**. La crainte portée par la
passation — un renvoi d'alinéa non recalé est un défaut bloquant — ne se matérialise
pas, et le motif est de structure : **les douze items de l'article 1er adressent les
alinéas du texte en vigueur, que la révision ne déplace pas.** Changer le 9° de
« supprimé » en « ainsi rédigé » ne bouge aucune cible.

Ce qui bouge est le compte de l'article **résultant** : 23 − 1 + 1 + 1 = **vingt-quatre
alinéas**, contre vingt-trois avant l'ajustement, l'alinéa des orientations
pluriannuelles cessant de disparaître. Aucun article de la proposition, ni ses
dispositions transitoires, ne renvoie à un alinéa de l'article 34 révisé : les
trente-trois articles ont été balayés, le renvoi de l'article 8 vise l'article 34
entier et l'article 33 ne connaît que des numéros d'articles de la proposition.
**Zéro renvoi à recaler**, et c'est un résultat, pas une omission.

*Contrôlé aussi* : l'ordre des items structurels tient et il est nécessaire. 9° (22ᵉ)
précède 10° (qui insère au rang 20 et décalerait le 22ᵉ), qui précède 11° (18ᵉ), qui
précède 12° (insertion en tête, qui décale tout). Toute permutation casse la
numérotation.

### La réapplication est prouvée, et sur le texte en vigueur, pas sur le récit — 20260914

**Jouée par script, alinéa par alinéa.** Les douze items de la version modificative,
appliqués dans leur ordre d'écriture aux vingt-trois alinéas du texte en vigueur,
redonnent les vingt-quatre alinéas du texte de substitution, **24 sur 24**. Les seuls
écarts relevés sont d'encodage — tiret d'énumération et apostrophe du fichier de
référence HTML — et non de texte.

Chaque item a été vérifié contre le contenu de l'alinéa qu'il vise : 19ᵉ les lois de
finances, 20ᵉ les lois de financement, 22ᵉ les orientations pluriannuelles, 18ᵉ
l'interruption volontaire de grossesse, 5ᵉ l'émission de la monnaie, 9ᵉ les
fonctionnaires, 10ᵉ les nationalisations, 17ᵉ le droit du travail. **Aucun renvoi
faux.**

*Les trente-deux autres articles ne se reprouvent pas* : ils sont identiques à
l'octet à la v6, que ce fil n'a pas touchée.

### Le trois colonnes avait perdu un alinéa en colonne C, et cela ne se voyait pas — 20260914

**Relevé en portant le siège du pluriannuel.** La colonne C de l'article 34 de la
v44 passait des impositions au renvoi organique final : **l'alinéa des lois de
programmation ordinaires — « Des lois de programmation déterminent les objectifs de
l'action de l'État. » — n'y figurait pas**, alors que la colonne B le déclarait
conservé et que la version par substitution le porte. La colonne C disait donc un
article plus court que celui que la proposition écrit.

Rétabli en v45, avec l'alinéa des orientations pluriannuelles réécrit à sa suite.
**C'est un défaut qu'aucun contrôle du corpus n'aurait sorti** : rien ne rapproche
mécaniquement la colonne C du trois colonnes du texte de substitution de la
proposition, et les deux sont deux écritures du même droit. *Le rapprochement des
deux est un contrôle à écrire, et il est porté aux points ouverts.*

### Le complément sur le mandat unique ne remontait pas parce qu'il ne déclarait aucun niveau — 20260914

**Cause trouvée dans le module, non supposée.** `md2docx.js` ne pose un niveau de
titre que sur trois motifs — `**Partie <chiffre>.`, `**<Lettre><chiffre>. ` (niveau
2, rang des axes), `**<Lettre><chiffre>.<chiffre> ` (niveau 3) — et le champ de
sommaire ne remonte que les niveaux 1 à 3. `**Complément : le mandat unique**` ne
répond à aucun des trois, non plus que `**C.1 …**` et `**C.2 …**`, dont l'identifiant
n'a pas de chiffre entre la lettre et le point. **Le bloc entier était hors du
sommaire, et c'était bien une erreur et non un choix.**

**Tranché par Claude au titre d'A-23** : la correction se porte au document et non au
module. Le complément devient `**C1. Le mandat unique**`, ses deux sous-sections
`**C1.1 …**` et `**C1.2 …**`. Il remonte au rang des axes, son rendu reste celui d'un
axe — gras aligné à gauche —, aucun axe n'est renuméroté, et l'index croisé est
recalé sur les deux nouveaux identifiants.

*Écarté* : élargir le motif du convertisseur. Le point de vérité d'une skill est la
skill enregistrée (A-269), un fil de production n'en corrige aucune, et le document
pouvait déclarer son niveau lui-même. *Écarté aussi* : renuméroter le complément en
A9, qui l'aurait fait passer pour un axe et aurait déplacé la frontière des parties.

*Relevé au passage, non corrigé* : « Annexes techniques » et les sections 3.1 à 3.4
ne répondent à aucun des trois motifs — leur identifiant commence par un chiffre. Le
sommaire du docx ne les portera pas davantage. Porté à la dette.

### Les noms datés l'emportent sur le nom canonique, pour cette famille de livrables — 20260914

**Tranché par Claude au titre d'A-23.** La règle du corpus veut un nom canonique par
artefact, sans horodatage. La passation prescrit `NOM_AAAAMMJJ_vN.ext`, et les quatre
bases ouvertes portent toutes cette forme. **La prescription de l'auteur l'emporte
pour cette famille** — proposition de loi consolidée, présentation, trois colonnes —,
dont l'historique de version est ce que l'auteur suit et arbitre, pièce par pièce.

Conséquence à tenir : ces artefacts ne se déclarent pas à l'index sous un nom
canonique avec alias, mais un par version. *La règle générale n'est pas amendée : elle
vaut pour l'appareil et les dérivés, qui se régénèrent.*

### Ce que l'audit sort, et que ce fil ne corrige pas — 20260914

**`audit-conformite` joué sur la présentation et sur les deux propositions.** Les
deux propositions sortent à deux anomalies, toutes deux corrigées dans la passe :
« droits » réduit là où le corpus impose « droits et libertés de 1789 », et la
formule de la règle d'or paraphrasée sans « annuelle », « régulier » ni « effectif ».

**La présentation sort onze anomalies, dont neuf sont antérieures à ce fil et portent
sur le dispositif hors les deux ajustements** — donc hors périmètre déclaré. Six
verbatim de texte en vigueur faux ou amputés (articles 25, 50-1, 1er, 24), et trois
versions cibles qui ne disent pas ce que la proposition écrit (articles 61, 72-1, 65,
72-2). **Elles ne se corrigent pas ici** : corriger le dispositif sous couvert d'une
passe d'intro serait le rouvrir sans mandat. Elles vont à la dette, nommées.

**La onzième est dans la rédaction arrêtée, et elle ne se corrige pas non plus.** La
ligne **iii** de l'intro écrit « une trajectoire annuelle de retour régulier à
l'équilibre effectif et des mesures opposables, au plus tard à la fin de la
législature », quand le dispositif écrit « des comptes publics au plus tard au terme
de la législature » et « mesures de correction ». La section 2 de la passation pose
que cette rédaction se reporte à l'identique : **l'écart se déclare, il ne se
harmonise pas.** Il revient à l'auteur.

*Les dix-sept chapeaux de plus de trois phrases de la présentation sont eux aussi
antérieurs — A2.2 en portait onze avant la phrase de raccord. Signalés sans couper,
comme la passation le demande.*

### La règle de redevabilité passe après le constat, et l'intro s'ouvre sur le piège — 20260914

**Tranché par l'auteur, en amendement de sa propre rédaction arrêtée.** La phrase
« Rendre compte au citoyen doit être la règle de toute institution de la
République » ouvrait l'introduction ; elle passe après le constat du piège.

**Ce que le déplacement achète.** Le document s'ouvre désormais sur « Le
législateur d'hier a piégé celui d'aujourd'hui », et la règle arrive comme la
réponse au constat au lieu de le précéder. L'enchaînement devient constat →
règle → exigence → remède → borne, du fait vers la norme, chaque paragraphe
appelant le suivant. En tête, la règle demandait au lecteur d'accepter une
maxime avant de savoir contre quoi elle est écrite.

*Ce que cela change à la règle de la section 2 de la passation* : rien. Une
rédaction arrêtée l'est contre le fil qui la porte, jamais contre l'auteur qui
l'a écrite. **L'ordre des paragraphes n'est pas de la reformulation** : pas un
mot ne bouge.

### Le sommaire ne manquait pas d'un champ, il manquait d'un niveau de plan — 20260914

**Trouvé en mesurant, après deux hypothèses fausses.** Le PDF sortait sans table
des matières. La première explication — le champ `TableOfContents` n'est pas
calculé hors de Word — était vraisemblable et fausse : l'index existe bien à
l'import, `CreateFromOutline` est vrai, `Level` vaut 3. La seconde — poser
`updateFields` dans les réglages du document — n'a rien changé, et le drapeau y
était déjà.

**La cause est ailleurs, et elle est nette.** Les paragraphes d'intitulé portent
le style « Heading 1-3 » et un **niveau de plan à zéro**. Word construit son
champ `TOC \\o "1-3"` sur les styles ; LibreOffice construit le sien sur les
niveaux de plan. Le même fichier rend donc un sommaire juste dans Word et une
page blanche partout ailleurs — **et c'est le PDF, seul lieu où la skill prescrit
de contrôler le rendu, qui était aveugle.**

`appareil/refresh_toc_pdf.py` pose le niveau de plan d'après le style **au rendu
seulement**, met l'index à jour en deux passes — la première pose la table, la
seconde recale les numéros de page que son insertion vient de décaler — et
exporte. Quarante-six entrées.

*Écarté* : figer un sommaire statique dans le markdown. Il aurait fallu le
recalculer à chaque passe, et le .docx aurait perdu son champ vivant. *Écarté
aussi* : corriger le niveau de plan dans le .docx. La correction appartient au
convertisseur ; en attendant, elle vit au rendu et ne touche pas le livrable.

*Ce que le cas enseigne, et il vaut au-delà* : **un contrôle qui ne sort rien
n'est pas un contrôle qui passe.** Le sommaire vide a été rapporté deux fois
comme « non contrôlable », ce qui était vrai de l'outil et faux du document.

### Trois défauts de rendu, tous du module, et le correctif n'est pas appliqué à la skill — 20260914

**Relevés sur le PDF, réparés, et le correctif attend l'auteur.** Aucune espace
insécable n'était posée devant les deux-points, les points-virgules et à
l'intérieur des guillemets français, quand l'étape 4 de la skill en fait un point
de contrôle. L'intitulé d'article et l'intitulé de chapitre n'étaient pas
solidaires du paragraphe suivant — deux titres orphelins en bas de page. La
césure automatique coupait les mots composés, « lui-/même », « dix-/sept ».

**Tranché par Claude au titre d'A-23** : le correctif se joue sur la copie locale
du convertisseur, il est éprouvé, et il **ne s'applique pas à la skill
enregistrée**, dont l'auteur est le point de vérité (A-269). Il est écrit en
entier à `methode/paquet_depot_20260914.md`, diff compris, avec les deux modules
neufs. **La divergence entre la copie locale et la skill est déclarée**, et elle
dure jusqu'à l'arbitrage.

*Mesuré après correction* : zéro coupure de mot sur les trois PDF, 256 espaces
insécables et 32 fines pour la seule proposition modificative, plus aucun titre
orphelin.

### Le paquet dû au dépôt porte son code, et non sa description — 20260914

**Tranché par Claude au titre d'A-23, contre la pratique du 20260910.** Ce jour-là
quatre modules ont été écrits depuis Cowork, déclarés au registre, et perdus avec
le conteneur : le registre survit, le code non. La leçon avait été inscrite ; elle
s'applique ici pour la première fois.

`methode/paquet_depot_20260914.md` porte **le code entier** des deux modules
neufs, le correctif du convertisseur en diff, les sept entrées d'index avec leur
rang, leur voie et leur famille, et le prompt du fil qui poussera. Rien n'est à
reconstituer. *Une dette déclarée sans son code n'est pas une dette, c'est une
perte annoncée.*

### Les neuf écarts de dispositif sont corrigés, et deux n'étaient pas où l'audit les situait — 20260914

**Repris sur mandat de l'auteur, après que la passe les eut mis à la dette.** Les
neuf écarts que l'audit sortait sur la présentation sont recalés, chacun sur sa
référence — le texte en vigueur sur la Constitution de référence, la version
cible sur la proposition par substitution.

**Deux ne se trouvaient pas à l'adresse annoncée, et c'est la référence qui a
tranché.** L'article 72-2 était juste en colonne cible : la formule fautive
vivait au chapeau d'A4.3. L'article 1er n'était pas en A4.4, qui ne cite que
« Son organisation est décentralisée », mais en A5.3. *Un relevé d'audit nomme
un écart, il ne garantit pas son adresse : l'adresse se rétablit sur pièce.*

*Signalé et non corrigé, hors des neuf* : la version cible de l'article 65 abrège
« La formation compétente à l'égard des magistrats du siège » en « La formation
du siège ». Le fond ne change pas, la citation n'est plus un verbatim.

### Quatre verdicts de transposabilité sont mis en question, et aucun n'est tranché — 20260914

**Relevé en soldant la dette, non provoqué.** Le siège du pluriannuel ayant changé
d'alinéa, quatre verdicts du récapitulatif et du recensement reposent sur un état
du dispositif qui n'est plus.

M4.8 qualifiait l'opération « supprimer une catégorie d'actes que la Constitution
nomme » ; l'alinéa étant réécrit et non supprimé, c'est désormais « lui retirer la
matière ». M3.2 et M3.5 tiennent la borne du pluriannuel pour atteignable par la
seule loi organique des finances ; le pluriannuel siège maintenant dans l'alinéa
dont l'homologue en vigueur attribue la matière aux lois de programmation. Le
repli R5 pose que la fonction de la règle d'or est atteignable sans toucher à
cette catégorie.

**Le fil ne les tranche pas** : ce sont des jugements de strate normative, ils
relèvent de l'auteur, et un fil qui solde une dette de formule n'a pas mandat
pour reclasser une innovation. Les quatre sont portés à l'état, nommés.

## 20260911 — Le livre validé entre au corpus, et la strate 1 se dédouble

*Fil de production, ouvert et clos le 20260911 sur la validation des épreuves
finales par l'auteur. Il n'a corrigé aucun texte, tranché aucun écart de fond,
et n'a touché ni doctrine, ni skill, ni livrable. Entrées titrées et datées,
sans numéro — A-282.*

### La strate 1 se dédouble, et ce n'est pas deux points de vérité — 20260911

**Tranché par Claude au titre d'A-23, et c'est la décision qui tient tout le
fil.** L'auteur valide la troisième épreuve et demande de mettre à jour les
sources. La question que cela pose n'est pas de rangement : elle est de savoir
ce qu'un fil cite quand il cite le livre.

**Le manuscrit ne peut plus l'être.** 858 écarts le séparent de la seconde
épreuve, relevés le 20260908 ; 12 de plus entre la seconde et la troisième. Une
skill qui citerait `manuscrit/manuscrit.html` citerait désormais un texte que
personne ne lira, et le ferait sans qu'aucun contrôle le voie.

**Le manuscrit ne se déclasse pas pour autant, et le retirer aurait été une
faute.** Il ancre le référentiel de doctrine, les 141 notes, les chiffres et
leur confiance `strate1` ; il est le troisième terme de tout relevé d'épreuve —
celui qui dit de quel côté un écart déplace le texte. Le sortir de la strate 1
aurait fait tomber la chaîne de `notes_manuscrit.json`, que neuf consommateurs
lisent dont quatre skills, pour un gain nul.

**Deux artefacts portent donc la strate 1, et chacun répond à une question
différente** — c'est un point de vérité par question, jamais deux pour un même
fait :

| artefact | ce dont il est la strate 1 |
|---|---|
| `manuscrit/manuscrit.html` | la **doctrine** — ancrage du REF_doctrine, des notes, des chiffres ; troisième terme des relevés |
| `livre/texte_livre.json` | le **verbatim citable** — ce qui se cite du livre se cite de lui |

**Le départage se lit à `consomme_par`, et nulle part ailleurs.** Le manuscrit
perd « toute skill qui cite un verbatim » et garde « toute skill qui cite un
verbatim de la doctrine » ; le livre prend l'autre moitié. *Un index qui déclare
deux strates 1 sans dire laquelle sert à quoi est pire qu'un index qui n'en
déclare qu'une.*

### Le texte du livre se verse en lignes de composition, et aucune césure n'y est recollée — 20260911

**Tranché par Claude au titre d'A-23.** `livre/texte_livre.json`, 311 829
octets, 180 pages, produit par `appareil/texte_livre.py` depuis l'épreuve
validée — `sha256 1ea86386…f199948b`, 2 759 475 octets, composée le 10/09/2026.

**Ce qui se verse est le verbatim, et lui seul** : une entrée par page, les
lignes de composition dans leur ordre. Le pied d'atelier tombe — le nom du
document InDesign, le folio et l'horodatage de composition ne sont pas du livre.
Le folio de tête tombe et devient un champ.

**Aucune césure n'est recollée dans le versé, et c'est le point.** Recoller,
c'est décider si le trait d'union appartient au mot ou à la composition, et un
jugement ne se plie pas dans du verbatim. Les 284 coupes de fin de ligne se
relèvent à part, chacune avec son verdict et son motif ; le texte coulant se
dérive par `couler()` et ne se verse pas — A-71.

**La règle de coupe se recompte et elle reproduit les deux verdicts rendus sur
pièce le 20260910.** Un composé garde son trait d'union si le même composé
s'écrit entier ailleurs dans le livre — c'est « titres-restaurant », deux fois ;
à défaut, si **ses deux éléments sont capitalisés** et qu'un composé de même
élément de gauche s'écrit entier — c'est « Cross-Sectional », tranché par
« Cross-Country » sur la même ligne du même titre. Trois traits d'union gardés,
281 césures.

*La capitalisation n'est pas un ornement de la règle, elle en est la borne, et
elle a été trouvée en jouant.* Sans elle, le repli sur le seul élément de gauche
gardait quatre traits d'union qui étaient des césures — « main-tenir »,
« entre-prises », « sur-monté », « de-France ». **Un verbatim faux est pire
qu'un verbatim coupé**, et c'est A-303 par un autre chemin : une règle plus
large rassure et corrompt.

### Six contrôles, dont un qui prouve qu'aucune ligne n'est perdue — 20260911

**Joués, non affirmés.** `T1` 180 pages. `T2` le folio de tête concorde avec le
folio du pied, sur les 109 pages qui en portent un. `T3` aucun pied de
composition ne subsiste. `T4` 19 pages sans ligne, déclaratif. `T5` les cinq
verbatim que le relevé du 20260910 publie se retrouvent, p. 105, p. 142, p. 88,
p. 40 et p. 147. `T6` **aucune ligne du livre n'est perdue à l'extraction** —
les lignes non vides rendues par `pdftotext`, moins les pieds et les 109 folios,
se retrouvent une à une dans le versé, au compte.

*`T2` a mordu au premier passage, et le défaut était instructif* : la première
ligne non vide d'une ouverture de chapitre n'est pas le folio, c'est le numéro
du chapitre. La retirer sans départage effaçait une ligne du livre, quatorze
fois. **Le folio du pied fait autorité**, et la règle ne retire la tête que
lorsque les deux concordent.

### Le livre imprimé contredit sa propre note, et l'écart part à l'impression — 20260911

**Relevé sur le texte versé, et c'est ce qui remonte à l'auteur.** La p. 105
écrit : « un socle contributif par répartition égale à 1 100 euros par mois pour
tous les travailleurs ». La note 124, p. 157, écrit : « le socle contributif
forme avec l'aide fondamentale une pension de retraite de base ». Le corps fait
donc valoir la pension de base 1 650 quand le corpus la déclare à 1 100, et
**l'écart vaut 550 euros par mois et par retraité**.

Le 20260908 l'avait relevé, le 20260910 avait constaté que la troisième épreuve
ne le répare pas et qu'**aucune correction n'avait été demandée à cet endroit**.
L'épreuve est validée : l'écart entre au livre imprimé. **Ce fil ne corrige
rien** — un livre validé ne se corrige pas depuis l'aval, et le texte se verse
tel qu'il part. *Ce qui reste à trancher n'est plus une correction d'épreuve,
c'est de savoir lequel des deux, du livre ou du corpus, dit la pension de base.*
Porté aux questions ouvertes.

### La note 124 est fautive, le chiffre ne l'est pas — 20260911

**Tranché par l'auteur le jour même, et cela ferme la question ouverte quelques
heures après son ouverture.** *« C'est 1 100, la note est grammaticalement
fautive. »*

**Ce qui est juste, et ce qui ne l'est pas.** Le corps de la p. 105 dit juste :
1 100 euros est la pension de base. C'est **la note 124 qui est fautive** —
« le socle contributif forme avec l'aide fondamentale une pension de retraite de
base » se lit comme une addition, quand l'aide fondamentale est **une composante
du 1 100** et non un terme qui s'y ajoute. Aucun chiffre du corpus ne bouge, et
aucun livrable n'a à se reprendre.

**Le contrôle mesurait la grammaire d'une note et le publiait comme un écart de
chiffre.** Il tirait 1 650 de la lecture additive et sortait « faux de 550 euros
par mois et par retraité » sur les deux épreuves, les 20260908 et 20260910. Le
verdict était un faux positif ; il a été publié deux jours de suite et porté au
relevé versé comme le seul point arithmétique qui bloquait.

*Ce que la faute enseigne, et elle est d'un genre neuf.* A-379 disait qu'une clé
fausse note faux. Ici la clé était juste et **c'est l'énoncé de référence qui
l'était grammaticalement**. Un contrôle qui lit le référent d'un nombre — règle
posée le 20260908, et elle est bonne — lit une phrase, et une phrase peut être
mal écrite sans que le chiffre le soit. **Le référent lu n'est pas le référent
voulu, et rien de mécanique ne les départage.** La règle tient donc avec sa
borne : quand le référent lu fait sortir un écart de fond, le verdict revient à
l'auteur avant de se publier, au lieu de se publier avant de lui revenir.

**Corrigé au module, jamais au document contrôlé** — A-303.
`rendre_releve_epreuve.py` pose désormais la même identité dans les deux
branches, 1 100 = 550 + 550, et quand la page ne nomme plus son référent il
**signale que la note imprimée ne se cite pas pour dériver la pension de base**
au lieu de sortir un faux. La pièce rejoint la dette au dépôt.

*Ce qui reste vrai et qui ne se corrige pas* : la note part à l'impression telle
quelle. Ce n'est plus un écart de chiffrage, c'est une phrase du livre imprimé
dont on sait qu'elle induit en erreur qui la lit seule.

### Quatre modules du 20260910 sont perdus, et c'est A-394 réalisée — 20260911

**Constaté au clone, non déduit.** `flux_epreuve.py`,
`relever_mandat_epreuve.py`, `valeurs_epreuve_relachees.py` et
`rendre_releve_mandat.py` sont déclarés voie `depot` par l'index du coffre. Le
clone du 20260911 — `HEAD` à `9bf6744` — ne les porte pas, et le conteneur qui
les portait est mort avec la session. **Ils n'existent plus nulle part.**

A-394 posait que corriger l'appareil depuis Cowork crée une dette qu'un autre
fil doit solder. Ce n'était pas une gêne de procédure : **une dette non soldée
avant la fin de la session est une perte sèche.** Le fil du 20260910 a écrit
quatre modules, relevé leurs empreintes, déclaré leur voie, et n'a rien poussé.

**Ce qui les sauve est l'asymétrie d'A-343** : leur sortie est au coffre.
`livrables/releve_epreuve_EP3.tsv` et son `.md` sont versés, lisibles, et font
spécification exécutable — c'est exactement ce qui avait rendu sûre la
réécriture d'`articles_ouverts_plf.py`. Ils passent aux manquants avec ce motif,
et non comme une perte muette.

*Règle qui en sort, et elle durcit A-394* : **un fil Cowork qui écrit une pièce
d'appareil livre son paquet de versement avant de clore**, ou il a écrit pour
rien. La déclarer au registre ne suffit pas : le registre survit, le code non.

### Deux documents du 20260910 seraient morts au prochain rejeu — 20260911

**Sorti en portant les entrées à la table curée.** Le fil du 20260910 avait
écrit, et il l'avait bien fait : *« les deux documents se portent à la table
dans le fil qui les produit »*. **Son édition de `generer_index.py` est morte
avec son conteneur.** Seul l'index du coffre portait encore
`livrables/releve_epreuve_EP3.tsv` et son `.md` ; le premier `make reindex` les
aurait dé-déclarés en silence.

C'est A-386 par un troisième chemin. Les deux entrées sont reportées à
`generer_index.py` et leur famille à `generer_carte.py`.

*Ce que le cas ajoute, et qui n'était pas dit* : **porter à la table curée ne
met à l'abri que si la table est poussée.** Un artefact déclaré dans une table
qui vit dans un conteneur est exactement aussi fragile qu'un artefact déclaré
nulle part.

### L'épreuve validée est une pièce jointe, pas un manquant — 20260911

**Tranché par Claude au titre d'A-23, après un faux départ.** Le PDF de
l'épreuve — 2 759 475 octets — a d'abord été porté aux manquants. `I2` l'a
sorti : présent au dépôt, déclaré nulle part parmi les artefacts. Le contrôle
avait raison. Ce n'est pas une pièce perdue, c'est **un input que l'auteur
détient** : même régime que les classeurs et que les deux épreuves précédentes
— le texte va au coffre, le binaire non, et la pièce rentre par pièce jointe du
fil qui rejoue l'extraction.

Elle rejoint `SOURCES_JOINTES`, voie `piece_jointe`, `restaurable: false`, avec
son SHA écrit. **Rien n'est dû à l'auteur pour autant**, et le fil qui a d'abord
écrit l'inverse se corrige ici : le texte versé fait foi seul, il est prouvé et
il se restaure par copie d'octets. Le PDF ne sert qu'à **rejouer** l'extraction
si `texte_livre.py` change — ce qui, le livre étant fini, ne se produira pas de
soi-même. Il rentre donc par pièce jointe du fil qui en aurait besoin, comme les
classeurs, et comme les deux épreuves précédentes, qui n'ont jamais été jointes.

*Ce que la faute enseigne* : déclarer une source pour qu'un renvoi résolve est
juste ; en tirer une demande à l'auteur ne l'est pas. **Une pièce déclarée
`piece_jointe` n'est pas une pièce attendue** — c'est une pièce dont on sait où
elle est le jour où quelqu'un en a besoin.

### Trois contrôles cassaient `make controle` au lieu de se déclarer absents — 20260911

**Constaté en jouant la chaîne, et c'est A-348 par l'autre bout.** A-348 disait
qu'un manquant qui ne casse rien ne se déclare pas tout seul. Ici l'inverse :
`controle_chiffres`, `controle_hypotheses` et `controle_apports` étaient appelés
sans garde. Un fil qui ne déplie pas le proto Données ou le manuscrit — c'est
le cas de tous les fils d'appareil — recevait une trace d'exception et
`make controle` en erreur, alors que neuf autres contrôles étaient passés.

Les trois reçoivent la garde que les six autres avaient déjà, et disent
l'absence au lieu de rompre. **`make controle` sort désormais à zéro sur un
périmètre partiel** — 0 anomalie bloquante, 0 échec, 13 skills contrôlées.
Un quatrième est ajouté, qui rejoue les six contrôles du texte du livre quand
l'épreuve est jointe.

*Écarté* : jouer les trois sans garde et lire la sortie à l'œil. Un contrôle qui
casse la chaîne est un contrôle qu'on finit par ne plus jouer.

### Quatre pièces sont dues au dépôt, et le paquet est prêt — 20260911

**Relevé à `coffre.py dette`, contre le clone.**

```
D1  appareil/generer_index.py          strate 1 dédoublée, EP3 et texte du livre portés
D1  appareil/generer_carte.py          familles du livre, de l'épreuve et des relevés EP3
D1  appareil/rendre_releve_epreuve.py  la note 124 est fautive, le chiffre ne l'est pas
D1  Makefile                           règle du texte du livre, gardes des trois contrôles
D2  appareil/texte_livre.py            pièce neuve
```

`D3` à zéro. C'est le régime permanent d'A-394 — et, cette fois, le paquet est
parti avec le fil plutôt que de mourir avec lui.

### Le push est fait, et il est contrôlé sur pièce — 20260911

**Relevé sur un clone frais, non hérité du récit.** Branche
`chantier-livre-20260911`, commit `1e9a387`, fusionné dans `main` au commit
`788a38d063842eb7b6414545132567c352bf61de`.

Le clone dit quatre choses, et les quatre se recomptent :

- **`HEAD` est bien `788a38d0`** ;
- **cinq chemins touchés sous `chantier/`** — quatre modifiés, un créé, zéro
  supprimé, exactement ce que le manifeste prescrivait ;
- **le diff hors `chantier/` est vide** — la garde qu'A-395 avait posée en
  arbitrant la sous-racine tient une fois de plus ;
- **les cinq empreintes du clone concordent avec le manifeste livré**, à
  l'octet.

`coffre.py dette` sort alors **`D1`, `D2` et `D3` à zéro**, 85 pièces identiques
au clone, et `make restauration` sort **`R1` à `R6` à zéro**. `R6` à zéro dit que
plus aucune pièce d'appareil ne vit dans le seul conteneur.

*Ce que la journée aura prouvé par ses deux bouts* : le fil du 20260910 a écrit
quatre modules et ne les a pas poussés — ils sont perdus ; celui-ci a livré son
paquet avant de clore — sa dette est soldée en une heure. **La différence n'est
pas la qualité du code, c'est l'ordre des gestes.**


## Questions ouvertes, non tranchées

- **La table d'équivalence légistique** (A-362) — trois familles où
  l'administration et la skill écrivent le même droit avec deux verbes :
  grouper ou séparer, supprimer ou abroger une subdivision, compléter ou insérer
  après le dernier alinéa. La neutraliser fait passer le taux d'opération de
  32 % à 71 %. C'est un jugement de fond, il revient à l'auteur, et les deux
  taux se publient tant qu'il n'est pas rendu.
- **La saturation du coffre** — ~~ouverte~~ **fermée le 20260910** : l'appareil
  entier est au dépôt, les douze pièces dues sont poussées (fusion `31896bb5`),
  et la jauge relevée à `project_info` est de **1 023 183 sur 2 000 000, marge
  976 817**. Deux libérations, 623 934 puis 367 490 jetons, sans perte de
  contenu. ~~La dette d'appareil d'A-396~~ **est comblée et prouvée sur le clone
  seul**, `R1` à `R5` à zéro sur 162 artefacts. **Ce qui reste ouvert est la
  rotation** des fichiers qui croissent — `arbitrages.md`, `journal.md`,
  `empreintes.json` —, qui se fait entièrement au coffre et n'a pas de voie vers
  le dépôt. Historique conservé : desserrée le 20260904, revenue depuis. Relevée à
  `project_info` le 20260907 à l'ouverture du fil de maintenance : **la marge est
  de 62 541 jetons**, contre 169 525 trois jours plus tôt. Deux candidats
  d'A-346 restent, `notes_manuscrit.json` et les quatre dérivés HTML ; l'identité
  au rejeu du premier **est désormais prouvée** — `extraire_notes.py` rejoué sur
  le manuscrit restauré redonne le référentiel à l'octet, `a6a07a73…` — et A-392
  ajoute un motif aux quatre dérivés : trois d'entre eux étaient en retard au
  coffre sans que rien ne le dise. Rappel de la contrainte qui commande l'ordre
  des opérations : un remplacement n'est pas crédité de la place que l'ancienne
  version libère, donc une grosse pièce se supprime avant de se réécrire.
- **Trois emplois de mots proscrits dans les livrables diffusables** (A-390),
  qui sont de fond et non de mécanique. « La gratuité » en vedette de perte, où
  la charge tient à la position et non à la phrase — galerie et site.
  « L'instruction gratuite des jeunes Français » au manifeste, emploi
  affirmatif. « Les fonctionnaires » dans l'énumération des boucs émissaires, où
  le substitut inverserait le sens. Le contrôle les sort ; il ne les corrige pas.
- **La présentation des sept compétences internes.** Leurs 223 renvois au corpus
  sont légitimes — elles sont internes par arbitrage —, et elles n'ont jamais été
  relues comme des documents. Aucun contrôle ne mesure cela, et le point de
  vérité d'une skill est la skill enregistrée (A-269) : la reprise passe par
  l'auteur.
- **La structure de production** — porter sur chaque brique du chantier : fait,
  à faire, réemployable, découpable. En cours avec l'auteur.
- **`Releve_affecte`** — reconstructible depuis le manuscrit et les `membres` du
  `REF_doctrine`, ou à retirer des trois skills qui l'appellent. Non établi.
- **La pension de base du livre imprimé** (20260911) — ~~ouverte~~ **fermée le
  jour même, tranchée par l'auteur** : *« c'est 1 100, la note est
  grammaticalement fautive. »* Le corps de la p. 105 dit juste ; c'est la note
  124 qui se lit comme une addition — « le socle contributif forme avec l'aide
  fondamentale une pension de retraite de base » — quand l'aide fondamentale est
  une composante du 1 100 et non un terme qui s'y ajoute. **Aucun chiffre du
  corpus ne bouge.** Le contrôle qui sortait « faux de 550 €/mois » mesurait la
  grammaire de la note et non un écart de chiffre : corrigé au module. La note
  part à l'impression telle quelle, et elle ne se cite pas pour dériver la
  pension de base.
- **La date du bon à tirer de l'essai**, qui borne le contrôle arithmétique du
  livre. ~~ouverte~~ **L'épreuve validée est celle du 10/09/2026**, validée par
  l'auteur le 20260911 ; son SHA est à l'index et le texte au coffre.
- **Le manifeste et le document de présentation au public** — deux livrables, ou
  un seul dont le manifeste est la version courte.
- **Les instructions permanentes du projet.** Elles portent encore l'ancienne
  feuille de route. `methode/feuille_de_route.md` est écrit pour les remplacer ;
  Claude n'a pas la main dessus.

---

## 20260910 — La relecture d'une épreuve contre l'épreuve relue

*Fil de production, ouvert et clos le 20260910. Il n'a rien corrigé, rien
réécrit, et n'a tranché aucun écart de fond. Entrées titrées et datées, sans
numéro — A-282.*

### La référence s'établit par inspection de ce qui est joint, et c'est l'épreuve annotée — 20260910

**Tranché par Claude au titre d'A-23.** Le fil pose trois formes possibles pour
« la seconde épreuve relue » et interdit de la demander : elle s'établit sur
pièce. L'inspection tranche. `livrables/releve_epreuve_EP2.tsv` ne porte
**aucune colonne de décision** — page, flux, classe, motif, ancienneté, ancre,
les deux versions, et rien d'autre : ce n'est pas un relevé arbitré. Le PDF de
l'EP2, lui, porte **261 surlignages annotés**, tous de la même main, chacun
avec un commentaire non vide.

**C'est donc l'épreuve annotée qui fait foi**, et la colonne de mandat se
remplit. Le relevé du 20260908 reste au dossier comme antériorité, non comme
demande.

*Ce que l'extraction a coûté, et qui vaut pour la prochaine* : un surlignage
couvre rarement un mot entier. Sur les 261, la plupart couvrent deux ou trois
caractères au point d'insertion — « s, », « e ou », « é t ». Le passage visé se
relève donc à deux échelles, les caractères couverts et **la ou les lignes de
composition qui les portent**, et la seconde échelle n'est pas un confort : six
surlignages n'auraient eu aucun passage visé sans elle.

### Le mandat se prouve, et la preuve se déclare avec le verdict — 20260910

**Tranché par Claude au titre d'A-23, et c'est la décision qui tient tout le
relevé.** Le fil interdit de rien supposer sur l'intention : un écart n'est
`porté` que contre une correction écrite. Mais toutes les demandes ne se
vérifient pas de la même façon, et un taux qui mélangerait les niveaux de
preuve mentirait sans qu'on le voie.

Quatre preuves, et le relevé donne la sienne à chaque verdict :

| preuve | ce qu'elle établit |
|---|---|
| `texte` | l'épreuve nouvelle porte, jeton pour jeton, le texte demandé |
| `suppression` | le jeton visé est du côté relu et n'est plus du côté neuf |
| `alinéa` | la coupe de paragraphe demandée est là où elle n'était pas |
| `place` | quelque chose a bougé à l'endroit visé, sans que la conformité se tranche mécaniquement |

**`place` n'est pas une preuve au même titre que les trois autres**, et le
document le dit avant de donner ses taux. Elle couvre les déplacements — « je
mettrais cette phrase en fin de paragraphe » — et les questions ouvertes, où
la demande n'énonce pas de texte à comparer. Sur 215 corrections portées, 132
le sont par `texte`, 46 par `suppression`, 37 par `place`.

*Écarté* : compter `place` comme un porté plein et n'en rien dire. Un relevé
qui ne distingue pas ses preuves rassure à tort, et c'est la faute du 20260908
par un autre chemin.

### Une demande d'alinéa ne se juge que sur l'alinéa — 20260910

**Tranché par Claude au titre d'A-23.** Dix-sept demandes portent sur une coupe
de paragraphe. Jugées une par une, cinq sortaient `porté de travers` — parce
qu'un texte voisin avait bougé sur la même ligne, pour une autre demande. C'est
un verdict faux : le voisinage n'est pas la demande.

Elles se jugent donc **sur la suite des ouvertures d'alinéa, comparée d'un
bloc**. 365 ouvertures à l'épreuve relue, 365 à la nouvelle, et les deux suites
se superposent mot pour mot — la seule divergence est un mot changé *à
l'intérieur* d'une ouverture, non une coupe déplacée. **Pas une coupe de
paragraphe n'a bougé dans tout l'ouvrage**, et les dix-sept demandes sont non
portées, toutes.

*Ce que la détection a coûté* : la première ligne d'une page n'est pas un
alinéa. Comptée comme telle, elle ajoutait 130 fausses ouvertures de chaque
côté et fabriquait vingt-neuf divergences qui n'étaient que des reprises de
ligne.

### Le déplacement prime sur l'alinéa, et sa portée est la page — 20260910

**Tranché par Claude au titre d'A-23.** Un même commentaire demande parfois les
deux — « remonter avant "Face aux peurs" puis faire un nouvel alinéa ». Le
mouvement est l'acte principal et l'alinéa sa conséquence : la demande se range
en `déplacement`.

Et une demande de déplacement **porte sur la page entière de l'épreuve relue**,
non sur les trois mots de tolérance qui suffisent partout ailleurs : elle
ordonne un mouvement dont l'autre bout tombe où il veut. Sans cette portée, la
moitié arrivante de chaque déplacement passait pour un changement que personne
n'avait demandé.

### Un passage retiré ici et rendu là-bas est un seul écart — 20260910

**Tranché par Claude au titre d'A-23.** Le diff rend un déplacement en deux
temps : un retrait, un ajout. Comptés séparément, ils font une perte et un
ajout de fond, et l'ajout — loin de la demande qui l'a ordonné — passe pour
gratuit. Les deux se recollent quand leurs textes se ressemblent à plus de
0,86, et le recollement porte les deux pages. Au-delà de 0,97 la pièce est
déplacée sans retouche : elle se compte en `forme`.

*Mesuré* : huit écarts de moins, dont sept qui auraient grossi la colonne des
non demandés.

### `autojunk` de difflib fausse silencieusement toute comparaison de textes longs — 20260910

**Constaté au débogage, et c'est un piège d'outil, pas une décision.** Au-delà
de deux cents caractères, `SequenceMatcher` déclare « junk » les caractères
fréquents et rend une ressemblance **quasi nulle entre deux textes
identiques** : 0,013 sur deux notes de fin qui ne diffèrent que par la place
d'un numéro. Rien ne l'annonce, et le résultat a l'air d'un vrai écart.

**Toute comparaison de chaînes de ce corpus se fait `autojunk=False`.** Les
modules du 20260908 le faisaient sur les suites de mots et l'omettaient sur les
chaînes dépouillées.

### Un contrôle qui ne joue pas rassure autant qu'un contrôle qui passe — 20260910

**Tranché par Claude au titre d'A-23, et c'est la suite directe de la règle du
référent.** Trois des vingt et une grandeurs du corpus sortaient
« introuvables » de l'épreuve nouvelle. Aucune n'avait bougé : une césure de
composition — « 77 cen-times » — et une virgule que l'auteur avait lui-même
demandé de déplacer suffisaient à faire échouer le libellé.

Un contrôle non joué ne sort ni `juste` ni `faux` : il disparaît, et le compte
final a l'air sain. **Le relevé des valeurs se fait donc sur un texte dont les
césures sont recollées, et chaque libellé se cherche une seconde fois sur le
même texte privé de ses virgules.** Le relâchement se déclare valeur par
valeur. Vingt et une grandeurs sur vingt et une se relèvent ainsi à l'épreuve
relue, vingt sur vingt et une à la nouvelle — la vingt et unième a perdu un mot
de son libellé, pas sa valeur.

*Ce qui n'a pas été fait, et pourquoi* : les libellés de
`rendre_releve_epreuve.py` ne sont pas touchés. Ils sont justes ; c'est le
texte qui leur résistait.

### La table d'un nombre en lettres se refait, faute d'avoir été versée — 20260910

**Constaté.** L'arbitrage du 20260908 pose qu'un nombre écrit en lettres porte
la même valeur qu'en chiffres, et que le passage de l'un à l'autre est une
coquille. La table qui servait cette règle **n'est ni dans
`relever_ecarts_epreuve.py` ni dans `rendre_releve_epreuve.py`** : elle vivait
dans la part non versée du fil. Sans elle, « deux pourcents » devenu « 2 % »
sortait en écart de fond.

Elle est refaite dans le module neuf, avec les bornes du 20260908 — « un »,
« une », « cent » et « mille » ne comptent pour un nombre que dans un composé.

### L'appareil ne se réécrit pas : quatre modules neufs, aucune retouche des deux prouvés — 20260910

**Tranché par Claude au titre d'A-23.** Les deux modules du relevé d'épreuve
comparent une épreuve au manuscrit et le font bien ; ce fil compare une épreuve
à une épreuve, sur une référence qui n'existait pas. Les retoucher pour deux
usages aurait mis en risque celui qui est prouvé.

Quatre pièces naissent — `flux_epreuve.py`, `relever_mandat_epreuve.py`,
`valeurs_epreuve_relachees.py`, `rendre_releve_mandat.py` — et elles
**réemploient** les fonctions des deux anciennes : normalisation, classement,
groupement, appariement des notes, libellés des grandeurs, identités du
contrôle. Deux pièces existantes changent, et seulement pour déclarer les
nouvelles : `generer_index.py` et `generer_carte.py`.

**Six pièces sont dues au dépôt** — `D1` deux, `D2` quatre. C'est A-394, et
`R6` les compte sans bloquer : un fil Cowork ne pousse pas.

### Les deux documents se portent à la table dans le fil qui les produit — 20260910

**Prescrit par le fil, et exécuté.** `livrables/releve_epreuve_EP3.tsv` et son
`.md` sont à `generer_index.py` et à `generer_carte.py` **avant** d'être
versés, en `derive`, `coffre: true`, famille `grilles`. Le fil du 20260908 les
avait versés sans les déclarer et l'avait constaté le lendemain ; ici la
déclaration précède le versement.

La table des matières se compte en `forme` et ne se compare pas : elle n'a pas
de vis-à-vis, elle suit les intitulés du corps. Un intitulé de chapitre qui
gagne « par an » à la page 83 le gagne à la page 179, et c'est une conséquence,
pas un écart.

### Les trois points dus au bon à tirer sont soldés — 20260910

**Rendu sur pièce, et le détail est au document.**

- **La page 105 n'est pas réparée.** L'épreuve nouvelle imprime mot pour mot ce
  que la précédente imprimait ; la note 124 ne bouge pas non plus ; le corps
  contredit toujours sa note et **l'écart vaut 550 euros par mois et par
  retraité**. Ce que ce fil ajoute au constat du 20260908 : **aucune correction
  n'avait été demandée à cet endroit**. Ce n'est donc ni un `non porté` ni un
  `non demandé` — rien n'a bougé et rien n'avait été écrit. Le contrôle
  arithmétique le relève seul, et il sort `faux` sur les deux épreuves.
- **Les deux césures sont tranchées.** P. 40, la nouvelle épreuve porte
  « sous-directeur » entier sur une ligne, trait d'union compris : la coupe
  était une césure de composition. P. 147, les deux épreuves coupent au même
  endroit et la coupe ne dit rien — mais « Cross-Country Heterogeneity » tient
  d'un seul tenant sur la même ligne du même titre, trait d'union compris. La
  référence écrit ses composés anglais avec le trait d'union, et
  « Cross-Sectional » le porte comme « Cross-Country ».
- **La page 142 est réparée, et comme l'auteur l'a demandée.** « la moitié des
  236 milliards d'euros par an d'économie sera déjà réalisée et restituée » :
  le sens du manuscrit est rétabli, la grandeur reste explicite, et « la
  seconde moitié des économies », deux paragraphes plus loin, ne la contredit
  plus.

### La phrase du bon à tirer ne peut pas s'écrire, et ce qui peut s'écrire à sa place — 20260910

**Rendu, et c'est la sortie du fil.** *« La troisième épreuve porte les
corrections demandées et n'en porte pas d'autres »* échoue sur ses deux
moitiés.

Sur la première : 43 des 261 corrections ne sont pas portées et 3 le sont
autrement que demandé. **Les non portées ne sont pas dispersées, elles font
deux blocs homogènes** — les dix-sept demandes de coupe de paragraphe, toutes ;
et vingt virgules à retirer, dont seize sous la même question, « abusif ? ».
Ce ne sont pas des oublis épars : ce sont deux consignes entières qui ne sont
pas arrivées jusqu'à la composition.

Sur la seconde : 12 écarts sont apparus sans demande écrite, dont **trois
seulement touchent la rédaction ou un renvoi** — « des établissements » devenu
« les » p. 125, « le citoyen » ajouté p. 129, et le renvoi interne de la note
133 passé de la note 135 à la note 137. Ce dernier **répare** : la note 135 est
un rapport de la Cour des comptes quand la phrase annonce « d'après les données
de l'OCDE », et la note 137 est l'OCDE. Personne ne l'avait demandé.

*Ce qui s'écrit à la place* : **la composition ne réécrit plus.** 572 écarts
étaient apparus hors du manuscrit entre la première et la deuxième épreuve ; il
y en a 12 entre la deuxième et la troisième. Ce qui reste ouvert au bon à tirer
n'est plus une dérive de la composition, c'est une liste d'arbitrages, et elle
revient à l'auteur.

## 20260910 — Le dépôt porte l'appareil entier, et l'empreinte cesse de mentir

*Suite du fil de production sur l'appareil, sur le push des douze pièces. Il n'a
touché ni doctrine, ni skill, ni livrable. Entrées titrées et datées, sans
numéro — A-282.*

### La dette est refermée, et l'appareil du dépôt est celui du corpus — 20260910

**Second push, contrôlé sur pièce.** Les quatre pièces corrigées le matin sont
au dépôt : commit `167c53e`, fusionné dans `main` au commit
`9bf67442edaff3b3b00f80666dd90b0eecd870c3`. **Diff hors `chantier/` vide**,
quatre chemins touchés, quatre modifiés, zéro créé, zéro supprimé.

`coffre.py dette` : **`D1`, `D2` et `D3` à zéro**, 84 pièces identiques au clone.
*« Rien n'est dû au dépôt : le clone porte l'appareil à l'octet. »*

`make restauration` : **`R1` à `R6` à zéro**, 162 artefacts attendus, 162
présents. **`R6` à zéro est le chiffre neuf** : plus aucune pièce d'appareil ne
vit dans le seul conteneur, et l'empreinte du coffre décrit exactement ce que le
clone porte.

**La restauration à blanc finale, sur le clone seul** : 84 fichiers du clone,
index amorcé du transcript, 78 documents du coffre, **`R1` à `R6` à zéro**. La
preuve externe du verbatim tient — `extraire_notes.py` rejoué redonne le
référentiel des notes à l'octet, 59 142 o. `make index` à zéro anomalie,
`make controle` code de retour nul, `make generateurs` zéro échec bloquant.

*Ce que le cycle complet a coûté, et il vaut d'être écrit* : **deux allers-retours
Cowork ↔ claude.ai/code** pour une seule correction d'appareil. Le premier porte
le fond, le second porte ce que le premier a rendu nécessaire — vider
`COFFRE_DOCUMENT`, relever l'empreinte au clone, distinguer `R6`. **C'est le prix
d'A-394, et il est structurel** : le fil qui corrige ne peut pas pousser, et
corriger crée une dette que seul un autre fil solde. *Un fil d'appareil se pense
donc en un seul aller-retour : ce qui se corrige, se corrige d'un bloc.*

*Relevé au passage, et c'est un défaut du tuyau* : deux fois sur douze, un fil
auxiliaire chargé de lire a rendu un résumé au lieu de sa ligne de compte. **Cela
n'a rien coûté** — le transcript porte les lectures, pas la réponse —, et c'est
justement ce qui rend la voie robuste. *Un tuyau se juge à ce qu'il a lu, jamais
à ce qu'il dit.*

### Le push est fait, et il est contrôlé sur pièce — 20260910

**Relevé sur le clone, non hérité du récit.** Le fil claude.ai/code a poussé les
douze pièces : commit `6cc1b99`, fusionné dans `main` au commit
`31896bb5f1896057aafc8e3e2c8335df04f1a6fb`.

Le clone frais dit trois choses, et les trois se recomptent :

- **`HEAD` est bien `31896bb5`** ;
- **le diff hors `chantier/` est vide** — aucun fichier du dépôt de droit n'a
  bougé, ce qui est la garde qu'A-395 avait posée en arbitrant la sous-racine ;
- **douze chemins touchés sous `chantier/`, huit modifiés et quatre créés, zéro
  supprimé** — exactement ce que le manifeste prescrivait.

`coffre.py dette` sort alors **`D1` à zéro et `D2` à zéro**, 80 pièces
identiques au clone. **La dette d'A-396 est fermée sur pièce**, et non sur
l'affirmation du fil qui l'a comblée.

### Les quatre pièces quittent le coffre, prouvées d'abord — 20260910

**Exécuté dans l'ordre d'A-357 : prouver, puis supprimer.** Les quatre pièces de
`D3` ont été comparées au clone **et** à leur empreinte avant tout retrait :

| pièce | octets | verdict |
|---|---|---|
| `referentiels/redaction_plf.json` | 848 687 | identique, clone et empreinte |
| `referentiels/redaction_plfss.json` | 351 968 | identique, clone et empreinte |
| `appareil/reappliquer.py` | 3 587 | identique, clone et empreinte |
| `appareil/cas_disposition.py` | 5 965 | identique, clone et empreinte |

Puis `COFFRE_DOCUMENT` a été vidée, l'index rejoué — **84 artefacts de voie
`depot` au lieu de 80** —, et les quatre documents supprimés du coffre.

**Mesuré à `project_info`, avant et après, dans son unité** : la jauge passe de
**1 390 673 à 1 023 183** sur 2 000 000. **367 490 jetons rendus**, pour une
marge qui passe de 609 327 à **976 817**. Le coffre passe de 87 à **83
documents**. C'est la seconde plus grosse libération du corpus, après les
623 934 d'A-395, et elle ne perd aucun contenu.

### `COFFRE_DOCUMENT` est vidée et elle reste — 20260910

**Tranché par Claude au titre d'A-23.** La table n'a plus d'entrée : les deux
motifs qui la peuplaient sont morts. Les deux référentiels de rédaction y
étaient depuis A-349 parce qu'une pièce plus grosse que l'archive ne s'y
repliait pas sans rendre sa réécriture impossible ; **il n'y a plus d'archive**.
Les deux modules de la réapplication y étaient parce que le fil qui les a écrits
n'avait pas replié le coffre ; ils sont au dépôt.

**Elle reste vide plutôt que d'être retirée, et le motif est structurel** : le
cas revient à chaque fois qu'un fil Cowork écrit une pièce d'appareil, puisqu'il
ne peut pas la pousser (A-393). Elle vit alors au coffre comme document, se
déclare ici, et `coffre.py dette` la réclame en `D3` jusqu'à ce qu'un fil
claude.ai/code la porte. *Retirer la table obligerait à la réinventer au premier
cas, et c'est exactement ce qu'A-349 dit d'une table d'exception.*

### L'empreinte d'une pièce de voie `depot` se relève au clone, jamais au dépôt courant — 20260910

**Tranché par Claude au titre d'A-23, et c'est la correction qui compte le plus
de cette journée.** Elle a été trouvée en jouant la procédure, non en la
relisant.

**Le défaut.** `empreintes.py` relevait toute empreinte au dépôt courant. Un fil
Cowork qui corrige une pièce de l'appareil **ne peut pas la pousser** ; relever
son empreinte ici écrivait donc au coffre **la référence d'un fichier qui ne vit
que dans un conteneur éphémère**. La session suivante clone, reçoit l'autre
version, et sort un `R1` qui n'est pas un faux. **C'est A-392 par l'autre bout** :
là, un dérivé versé qu'aucun fil ne reversait faisait mentir le coffre ; ici,
c'est l'empreinte qui décrit un état qu'aucune surface ne porte.

**La règle, et elle est générale** : *une empreinte ne décrit jamais un état
qu'aucune surface permanente ne porte.* D'où, pour la voie `depot`, le relevé
**au clone**, qui est ce que la session suivante recevra. Sans clone, l'empreinte
**ne se touche pas** — l'ancienne vaut, et le module le dit au lieu de deviner.
Pour la voie `coffre`, elle se relève au dépôt courant, qui est ce que le fil
verse : les deux voies ne sont pas symétriques, et le motif est que l'une se
pousse depuis ici et l'autre non.

*Ce que la correction a coûté et ce qu'elle achète* : le clone devient un
argument de `make coffre`, et sans lui la cible le dit et continue, comme toute
règle qui dépend d'une pièce absente. En échange, **une restauration à blanc sur
le clone seul sort à zéro**, ce qu'elle ne pouvait pas faire avant.

### `R6` — une dette d'appareil n'est pas un faux, et elle sort de `R1` — 20260910

**Tranché par Claude au titre d'A-23, dans le même geste.** Une fois les
empreintes relevées au clone, la pièce corrigée ici et non poussée diverge de son
empreinte **par construction**. La compter en `R1` faisait échouer
`make restauration` à tout fil qui corrige l'appareil — c'est-à-dire à sa propre
clôture.

Le départage est mécanique et il demande le clone :

- la pièce diverge de l'empreinte **et du clone** → elle a été éditée ici et non
  poussée. **`R6`**, non bloquant, avec renvoi à `coffre.py dette`.
- la pièce diverge de l'empreinte **et concorde avec le clone** → c'est le clone
  qui diverge, donc le dépôt est en retard ou l'empreinte a été relevée sur autre
  chose. **`R1`**, bloquant, et c'est le cas qui compte.
- **sans clone, toute divergence de voie `depot` reste en `R1`.** Le
  comportement prudent est celui qui bloque.

*Écarté* : sortir la voie `depot` de `R1` en bloc. Cela aurait rendu invisible un
dépôt en retard, qui est précisément l'accident qu'A-392 a payé.

### La restauration à blanc passe sur le clone seul, sans aucune pièce portée à la main — 20260910

**Éprouvé, dans un répertoire vierge et hors du dépôt, avec l'appareil du clone
et lui seul.** C'est le test que la passe 2 du 20260909 ne pouvait pas faire,
faute du push.

```
git clone … droit && cp -r droit/chantier/. .      84 fichiers
python3 appareil/restaurer.py amorce .             index, 98 330 o
python3 restaurer.py ../methode/index.json ..      78 documents du coffre
make restauration
```

| verdict | compte |
|---|---|
| artefacts attendus | **162** — 78 par le coffre, 84 par le dépôt |
| présents au dépôt | **162** |
| `R1` · `R2` · `R3` · `R4` · `R5` | **0 · 0 · 0 · 0 · 0** |

**Aucune pièce n'a été portée à la main, et les deux gros référentiels ne
demandent plus de `cp`** : ils viennent du clone. **La voie 1 n'est plus sur le
chemin critique de l'ouverture.**

**La preuve externe du verbatim tient** : `extraire_notes.py` rejoué sur le
manuscrit restauré redonne `referentiels/notes_manuscrit.json` **identique à
l'octet** — `a6a07a73…`, 59 142 o. Et `make index` dans ce dépôt vierge sort
**zéro anomalie bloquante**, `I2` à `I5` à zéro.

*Un `R1` s'est présenté au premier essai, et il n'était pas un faux* : trois
documents de `methode/` — journal, registre, prompt de fil — sortaient à leur
version d'avant le versement du jour. **C'est A-313 mot pour mot** : le
transcript porte l'état d'avant, pas l'état d'après, et il faut relire le coffre
après avoir versé. Relus par un fil auxiliaire, les trois concordent et le relevé
retombe à zéro.

### Quatre pièces sont dues au dépôt, et c'est le régime permanent — 20260910

**Relevé à `coffre.py dette`, contre le clone.** Corriger l'appareil depuis
Cowork crée mécaniquement une dette, puisque le même geste ne peut pas la
pousser. Les quatre de ce jour :

```
appareil/generer_index.py           COFFRE_DOCUMENT vidée
appareil/empreintes.py              relevé au clone pour la voie `depot`
appareil/controle_restauration.py   verdict R6
Makefile                            le clone passé aux deux contrôles
```

**Ce n'est pas un défaut du fil, c'est la forme que prend A-394** : aucune
surface ne voit les deux bouts. Le corpus le porte désormais sans mentir — `R6`
le compte sans bloquer, `D1` le réclame, et l'empreinte reste celle du clone.
*Le seul régime à éviter est celui d'hier : une empreinte relevée sur une pièce
que rien ne porte.*

### `V2` et `V5` ne se mesurent pas sur le même dépôt — 20260910

**Relevé sur deux passages du même balayage, mêmes entrées.** `make generateurs`
a sorti `V5` à **6** au premier passage et à **0** au second. `V2` avait fait
l'inverse la veille — 0 quand le fichier existait, 1 sur un dépôt vierge.

**Les deux verdicts ne se lisent donc pas au même endroit**, et c'est mécanique :
`V2` demande qu'une cible n'ait pas de règle, ce que `make` ne dit que si le
fichier est absent ; `V5` compare le rejeu au fichier présent, ce qui n'a de sens
que si le fichier était à jour. *La cause de l'écart de 6 est déduite et non
relevée — les dérivés que le premier passage venait de régénérer —, et elle
s'inscrit comme telle.*

**Règle qui en sort** : `V2` se mesure sur un dépôt vierge ou après `make
propre` ; `V5` sur un dépôt déjà régénéré. Un balayage joué une seule fois ne
peut pas dire les deux.

---

## 20260909 — La dette d'A-396 est comblée, et la voie de restauration devient un champ

*Fil de production sur l'appareil, ouvert et clos le 20260909 après le fil de
conversation qui a versé l'archive au dépôt. Il n'a touché ni doctrine, ni skill,
ni livrable. Entrées titrées et datées, sans numéro — A-282.*

### La voie de restauration est un champ de l'index, et elle cesse d'être déductible du rang — 20260909

**Tranché par Claude au titre d'A-23.** Jusqu'au 20260909, l'appartenance d'un
artefact à l'archive technique se déduisait de son rang : `appareil` ou
`referentiel` valait « replié dans `technique/coffre.txt` ». Le rang ne dit plus
où la pièce vit, puisque le même rang couvre désormais trois cas — au dépôt sous
`chantier/`, au coffre comme document, ou nulle part.

**L'index porte donc un champ `voie`**, à quatre valeurs et aucune cinquième :

| voie | ce qui la rend | comment |
|---|---|---|
| `depot` | le clone du dépôt | `git clone` puis `cp -r droit/chantier/. .` |
| `coffre` | le coffre | texte au transcript, ou fichier local par `cp` |
| `piece_jointe` | personne — l'auteur la rejoint | aucune |
| `hors_coffre` | rien de l'extérieur | `make` la refait |

Et **`chemin_coffre` donne où la pièce se lit sur sa voie** : son chemin au
coffre, un chemin préfixé de racine, ou son chemin dans le dépôt sous
`chantier/`. Les deux formes qu'A-396 proposait sont donc prises ensemble, et
c'est le seul choix qui laisse `restaurer.py` garder une clé unique par pièce.

*Écarté* : mettre `chemin_coffre` à `null` pour la voie `depot`. Le module de
restauration en fait une clé de dictionnaire, et deux `null` se seraient
écrasés. *Écarté aussi* : passer `coffre: false` sur les quatre-vingts. Le champ
`coffre` ne dit pas le lieu, il dit la durabilité — qu'une pièce survive aux
sessions par une surface permanente —, et le basculer aurait fait sortir
l'appareil entier des empreintes et des attendus de restauration.

**Le bloc `archives` de l'index disparaît avec l'archive.** Le bloc **`depot`**
le remplace, et il porte plus que ce que l'ancien portait : le nom du dépôt, la
branche, la sous-racine, **la commande de clone en clair**, l'état de l'écriture,
les quatre-vingts chemins rendus, et ceux des pièces de l'appareil qui sont
encore au coffre comme documents. *Un fil qui ouvre demain y lit tout ce qu'il
lui faut sans avoir à connaître A-395.*

### `coffre.py` cesse de plier, et `plier` est retiré plutôt que gardé — 20260909

**Tranché par Claude au titre d'A-23.** Le module pliait la couche technique en
une archive unique que `make coffre` versait au coffre. Cette archive n'existe
plus. **Garder `plier` aurait été pire qu'inutile** : un fil l'aurait joué,
aurait vu une archive apparaître dans `coffre/`, et aurait cru avoir versé
quelque chose. C'est A-364 par un autre chemin — un dérivé produit que personne
ne pense à porter.

`deplier` **reste**, et le motif se dit : c'est le seul lecteur du format, et le
retirer rendrait illisible une archive qui resurgirait d'un transcript ou d'une
sauvegarde. Il ne sert plus à l'ouverture de session.

**Un mode naît, `dette`.** Il compare chaque artefact de voie `depot` au clone,
octet par octet, et sort trois verdicts : `D1` les pièces modifiées ici et non
poussées, `D2` celles que le clone ne porte pas, `D3` celles de l'appareil encore
versées au coffre comme documents. **Il ne pousse rien** — l'écriture au dépôt
est fermée depuis Cowork (A-393) — et son code de retour reste nul : une dette
est déclarative, et `make coffre` ne doit pas s'arrêter dessus.

**`make coffre` ne plie donc plus.** Il relève les empreintes, puis il dit ce qui
est dû au dépôt. Sans clone en `../droit`, il le dit et continue, comme les
règles qui dépendent d'une pièce jointe.

### `restaurer.py` rend la main sur la voie `depot`, et il gagne une amorce — 20260909

**Tranché par Claude au titre d'A-23.** Le module ne retenait que les pièces dont
le `chemin_coffre` n'était pas une archive : les quatre-vingts en sortaient parce
qu'elles étaient repliées. Sur le champ `voie`, elles en sortent pour la bonne
raison — **le clone les rend déjà, et un clone est une copie d'octets par
construction**.

**Mais il ne les tait pas.** Il les compte à part, dit combien sont présentes au
dépôt courant, et **imprime la commande de clone** quand il en manque. Les taire
aurait laissé croire que le corpus tient sur le seul transcript, ce qui est faux
depuis A-395 ; les chercher au transcript aurait sorti quatre-vingts absences et
noyé les vraies.

**Et il refuse un index d'avant.** Un index sans champ `voie` décrit une archive
qui n'existe plus : le module le dit et s'arrête, plutôt que de chercher au
transcript des chemins que le coffre ne porte plus.

**L'amorce est la pièce qui manquait à la procédure, et elle manquait depuis le
début.** `methode/index.json` est la table qui dit quoi restaurer, et il est
lui-même un document du coffre : dans un dépôt vierge, `restaurer.py` n'avait
rien pour savoir quoi restaurer, et c'est le dépliage de l'archive qui masquait
le trou. Le mode `amorce` restaure l'index seul, sans index. **C'est la seule
pièce du corpus dont la voie soit connue sans consulter l'index** — elle se lit
au coffre à son propre chemin, et cela ne changera pas.

*Écarté* : régénérer l'index par `make reindex` à l'ouverture. L'index serait
alors celui de la table curée et non celui du coffre, et `make restauration` ne
pourrait plus prouver que les deux concordent — c'est exactement le contrôle
qu'on veut garder.

### Un `R1` ne se lit pas de la même façon selon la voie, et le contrôle le dit — 20260909

**Tranché par Claude au titre d'A-23.** Sur la voie `coffre`, un fichier
divergent est un faux : il a repassé par une chaîne où une recopie peut
normaliser, et il se redemande au coffre. Sur la voie `depot`, **l'octet vient
d'un clone, donc il n'est pas douteux** : ce qui diverge est le clone contre
l'empreinte, et cela veut dire que le dépôt est en retard, ou qu'un fil a versé
des empreintes sans pousser.

Le verdict reste bloquant dans les deux cas — on s'arrête sur un `R1` —, mais le
relevé nomme la voie de chaque divergence et renvoie à `coffre.py dette` pour
départager. *Un contrôle qui bloque sans dire où chercher fait perdre un fil
entier*, et le corpus a déjà payé ce prix trois fois sur des empreintes en
retard.

### Le contrôle de l'index ignore le répertoire personnel du conteneur — 20260909

**Tranché par Claude au titre d'A-23, et c'est A-337 à l'identique.** La racine du
dépôt de cette session **est** le répertoire personnel du conteneur. `I2`
sortait donc à **29 297**, dont 29 295 fichiers de cache d'outils — `.cache`,
`.npm`, `.config`, `.ssh` — et **deux du corpus, invisibles dedans**. A-337 dit
la règle : la procédure que le corpus prescrit ne doit pas casser un contrôle que
le corpus tient. Un contrôle qui crie 29 297 fois ne sert plus à rien.

Les répertoires du conteneur rejoignent les ignorés, avec `epreuve` — l'atelier
d'une restauration à blanc, même régime qu'`eval/` et `machine/` (A-363).
**`I2` retombe à zéro, et le compte du dépôt passe de 29 459 à 162 fichiers.**

### La cible du site nommait une sortie sur deux, et le balayage l'a dit — 20260909

**Sorti de `make generateurs`, verdict `V2`.** `appareil/generer_site.py` écrit
vingt et une pages d'un coup et l'index en déclare deux : l'entrée, qui vaut pour
le dossier, et le manifeste, qui est un livrable diffusable à part. **La règle
n'en nommait qu'une.** `make site/manifeste.html` sortait « no rule » dans un
dépôt vierge, et le manifeste ne se rejouait jamais par `make`.

C'est le défaut exact qu'A-385 a relevé six fois le 20260907, et qu'elle a manqué
ici. La cible nomme désormais ses deux sorties déclarées. **`V2` retombe à zéro,
et le balayage sort à zéro échec bloquant sur ses cinq verdicts.**

*Ce que l'incident enseigne, et qui vaut au-delà* : le balayage ne voyait pas le
défaut sur un dépôt où le fichier existait déjà — `make` répond « rien à faire »
au lieu de « pas de règle ». **Un `V2` ne se mesure que sur un dépôt vierge, ou
après `make propre`.**

### La restauration à blanc est jouée deux fois, et la seconde passe — 20260909

**Éprouvé, non supposé, dans un répertoire vierge et hors du dépôt.**

**Passe 1 — le clone tel que le dépôt le porte aujourd'hui.** Les deux voies
d'ouverture échouent, et c'est la dette d'A-396 en acte : `coffre.py deplier
coffre/coffre.txt` lève `FileNotFoundError`, l'archive n'existant plus ; et
`restaurer.py amorce` n'existe pas dans la version que le clone porte. **Un fil
qui ouvrirait sur le clone seul ne pourrait pas ouvrir.**

**Passe 2 — le clone plus les huit pièces dues, portées à la main comme le push
le fera.** 80 fichiers rendus par le clone, l'index amorcé du transcript
(98 300 o), 82 documents du coffre restaurés — dont les deux référentiels de
rédaction par `cp` du fichier local, voie 1 —, puis `make restauration` :

| verdict | compte |
|---|---|
| artefacts attendus | **162** — 82 par le coffre, 80 par le dépôt |
| présents au dépôt | **162** |
| `R1` divergence | **0** |
| `R2` non restauré | **0** |
| `R3` hors empreinte | **0** |
| `R4` sans empreinte | **0** |
| `R5` dérivé divergent | **0** |

**Le corpus entier remonte du coffre plus le clone, et rien ne diverge.** `R2` à
zéro est le chiffre qui compte : aucune pièce du corpus ne tombe entre les deux
surfaces.

**La preuve externe du verbatim tient, et elle ne passe par aucune empreinte** :
`extraire_notes.py` rejoué sur le manuscrit restauré redonne
`referentiels/notes_manuscrit.json` **identique à l'octet** — `a6a07a73…`,
59 142 o, 141 notes. Et `make index` dans le dépôt vierge sort **zéro anomalie
bloquante**.

*Ce que la passe 2 simule, et il faut l'écrire* : les huit pièces ont été portées
par `cp` depuis le dépôt courant, parce que **l'écriture au dépôt est fermée
depuis Cowork** (A-393). **Tant qu'elles ne sont pas poussées, la passe 1 est
l'état réel** : un fil qui cloner demain reçoit l'appareil d'avant, et la dette se
rouvre entière.

### Douze pièces sont dues au dépôt, et elles se déclarent faute de pouvoir se pousser — 20260909

**Relevé par `coffre.py dette`, mesuré contre le clone et non estimé.**

**Huit pièces modifiées ici et non poussées** — `D1` :

```
appareil/generer_index.py            appareil/empreintes.py
appareil/generer_carte.py            appareil/restaurer.py
appareil/coffre.py                   appareil/controle_restauration.py
appareil/controle_index.py           Makefile
```

**Quatre pièces de l'appareil encore versées au coffre comme documents** — `D3`.
Elles n'étaient pas dans l'archive au moment du versement, donc elles ne sont pas
parties avec elle :

```
referentiels/redaction_plf.json      848 687 o
referentiels/redaction_plfss.json    351 968 o
appareil/reappliquer.py                3 587 o
appareil/cas_disposition.py            5 965 o
```

**Les y porter rendrait de l'ordre de 360 000 jetons de jauge**, au rapport
mesuré d'A-395 — 0,3 jeton par octet. C'est la plus grosse libération encore
disponible, et le motif qui les gardait au coffre est caduc : A-349 les tenait
hors de l'archive parce qu'une pièce plus grosse que la marge ne s'y replie pas,
et **il n'y a plus d'archive à réécrire**.

*Ce que le fil ne fait pas* : pousser. Il déclare, et il s'arrête là.

### Les douze pièces sont livrées en un paquet prouvé, et c'est la seule voie — 20260909

**Fait le 20260909, sur go de l'auteur.** A-394 pose que le transfert passe par un
fichier livré à l'auteur, qui le dépose dans le fil qui écrit : aucune surface ne
voit les deux bouts. Le paquet est livré — `versement_depot_chantier_20260909.zip`,
**259 933 octets**, seize entrées.

Il porte les douze pièces **rangées sous `chantier/`**, de sorte qu'elles se
déposent par-dessus la sous-racine sans qu'aucun chemin ne se décide au
versement, et un `EMPREINTES.txt` qui donne pour chacune son SHA-256, ses octets
et ses lignes. **Les douze concordent avec `methode/empreintes.json`**, et le
dézippage a été comparé au dépôt courant : **12 sur 12 identiques à l'octet.**

*Ce que le manifeste prescrit, et qui n'est pas de commodité* : comparer avant de
fusionner, vérifier que le diff hors `chantier/` est vide, et ne retirer les
quatre pièces de `D3` de `COFFRE_DOCUMENT` **qu'après** leur présence au dépôt —
prouver, puis supprimer du coffre, dans l'ordre d'A-357. Le contrôle d'après est
mécanique : `coffre.py dette` doit sortir `D1`, `D2` et `D3` à zéro.

*Écarté* : livrer les huit et garder les quatre pour plus tard. Le fil
claude.ai/code ne voit pas le coffre, donc un second aller-retour aurait été
nécessaire pour des pièces déjà prêtes.

### Deux référentiels ne reviennent pas du transcript, et la voie 1 n'est pas outillée — 20260909

**Relevé au premier essai.** `restaurer.py` ne moissonne au transcript que ce que
le coffre rend **en texte**. Les deux référentiels de rédaction — 848 ko et
352 ko — reviennent comme **fichiers locaux**, et le module les compte en absents
plutôt que de les taire, ce qui est le bon comportement. Leur restauration s'est
faite par `cp`, et les deux sont **identiques à l'octet** à leur empreinte —
`eec65f01…` et `71119c0f…`.

**C'est la voie 1 de `CLAUDE.md`, et elle reste manuelle.** A-313 la déclarait
déjà « prévue, et manuelle », à reprendre quand un deuxième document franchirait
le seuil. **Ils sont deux depuis le 20260904.** Ce fil ne l'outille pas : le
transcript porte le chemin local que l'appel a rendu, et un module qui le
moissonnerait est un travail d'appareil que la dette du dépôt précède — inutile
d'écrire une pièce de plus qu'on ne peut pas pousser.

### Quatre documents sont au coffre sans être à l'index, et ce fil ne les qualifie pas — 20260909

**Relevé à `project_info`, non déduit.** Le coffre porte 87 documents ; l'index en
déclare 82 par la voie `coffre`, plus une pièce jointe. **Quatre ne sont
déclarés nulle part** :

```
appareil/trois_colonnes_regle_dor.py     20260908
livrables/PPLC_regle_dor_modificative.md 20260908
livrables/Presentation_regle_dor.md      20260908
methode/sas_pplc_regle_dor.md            20260908
```

Ils viennent d'un fil de la règle d'or, versés le 20260908, et **le quatrième est
un sas** — donc il se lit avant d'être absorbé. C'est exactement le cas qu'`I6`
compte, et `I6` ne l'a pas vu : l'inventaire du coffre n'est pas au dépôt de ce
fil, et le contrôle le dit plutôt que de bloquer.

**Ce fil ne les ouvre pas et ne les classe pas** — A-24 l'interdit, et son objet
est A-396 et rien d'autre. Le constat s'inscrit, la table ne bouge pas. *Le
premier fil qui les ouvrira les portera, et le sas dira ce qu'il reste à
absorber.*

---

## 20260909 — L'appareil quitte le coffre, et les deux surfaces ne se rejoignent pas

*Fil de conversation, ouvert le 20260909 sur la passation du 20260908. Il n'a
déplié aucune source, joué aucun `make` et corrigé aucune skill. Numérotation à
la suite d'A-392.*

### A-393 — L'écriture au dépôt était fermée par le proxy de session, non par les droits GitHub

**Mesuré de trois façons, et la passation du 20260908 se trompait de cause.** Elle
écrivait « l'atelier n'a aucun outil GitHub authentifié chargé ». Il en a un : le
jeton de l'atelier s'authentifie comme `resolution-ib-dev`, propriétaire du dépôt.

| test | résultat |
|---|---|
| `git ls-remote` anonyme | passe |
| `git push` avec le jeton | refusé — *« not in this session's authorized repository set »* |
| API GitHub `/repos/…` | 403, même motif |

**Le refus vient du proxy de la session**, qui n'injecte de credential que pour les
dépôts déclarés comme sources de la session. **La synchronisation GitHub d'un
projet Claude est en lecture seule par conception** et ne servira jamais à écrire,
quel que soit son filtre. **Et Cowork n'a aucun sélecteur de dépôt** : la voie que
ce fil a d'abord fait chercher à l'auteur n'existe pas, et l'avoir posée en
question avant de la vérifier est la faute du fil.

### A-394 — Aucune surface ne voit les deux bouts, et c'est la contrainte permanente de l'architecture

**Constaté, et cela commande tout versement futur du coffre vers le dépôt.**

- Une session **Cowork** voit le coffre et **ne peut pas pousser**.
- Une session **claude.ai/code** pousse et **ne voit pas le coffre** — une session
  ne voit qu'un projet, et les surfaces ne partagent pas la base de connaissance.

**Le transfert passe donc par un fichier livré à l'auteur**, qui le dépose dans le
fil qui écrit. C'est acceptable pour l'appareil, qui bouge rarement. **Ce n'est
pas une voie de rotation** : `arbitrages.md`, `journal.md` et `empreintes.json`
grossissent à chaque session et leur rotation se fait entièrement au coffre, sans
dépôt.

### A-395 — L'appareil est au dépôt, prouvé 80 sur 80 à l'octet, et le coffre a lâché son archive

**Exécuté le 20260909, dans l'ordre d'A-357 — prouver, puis supprimer.**

`technique/coffre.txt` a été rendu par le coffre **comme fichier**, donc par copie
d'octets et non par le modèle — 1 766 639 octets, 80 blocs. Il a été déplié par
**`appareil/coffre.py` extrait de l'archive elle-même**, jamais par un déplieur
écrit pour l'occasion : la restauration ne se délègue pas au jugement d'un modèle.

Le versement s'est fait par un fil claude.ai/code sur `resolution-ib-dev/Resolution-2027`,
branche `appareil`, commit `6752e77`, fusionnée dans `main` au commit
`eb0e0981e808a03178e8d255084bed542dc39388`.

**Contrôle avant suppression, mécanique et fait deux fois** — contre la branche
puis contre `main`, fichier par fichier : **80 identiques, 0 divergent, 0 absent**.
Le diff hors `chantier/` est vide : aucun fichier du dépôt de droit n'a bougé.

*Ce que le fil qui a versé a bien arbitré, et qui n'était pas dans sa consigne* :
le `.gitignore` du corpus ignore `droit/`, `eval/`, `publication/`, `machine/`,
`coffre/`. **Posé à la racine du dépôt de droit, il en aurait masqué le contenu**,
et le fusionner l'aurait fait en silence. L'appareil est donc sous `chantier/`,
avec son `.gitignore` local, qui ne porte que sur son sous-arbre. **Deux corpus
dans un dépôt, deux racines distinctes** — la consigne « à la racine » venait de
ce fil et elle était fausse.

*Mesuré à `project_info`, avant et après* : la jauge passe de **1 997 265 à
1 373 331** sur 2 000 000. **623 934 jetons rendus**, pour une marge qui passe de
**2 735 à 626 669**. C'est la plus grosse libération du corpus à ce jour, et elle
ne perd aucun contenu.

### A-396 — La restauration ne passe plus par le coffre pour ce que l'archive portait, et l'appareil ne le sait pas encore

**Dette déclarée, non comblée, et elle est la contrepartie d'A-395.** Quatre-vingts
artefacts portent `chemin_coffre: technique/coffre.txt` à l'index. **Ce chemin
n'existe plus au coffre.** `coffre.py deplier` n'a plus d'archive à lire, et
`restaurer.py` ne trouvera rien pour eux.

Leur voie de restauration est désormais **le clone du dépôt** :
`git clone https://github.com/resolution-ib-dev/Resolution-2027` puis
`chantier/`. C'est une voie de copie d'octets, donc conforme à l'exigence — mais
**elle n'est écrite nulle part dans l'appareil**, et un fil qui ouvrirait demain
en suivant la procédure trouverait quatre-vingts artefacts manquants sans savoir
où les prendre.

Ce qui reste dû, au premier fil de production qui clone le dépôt :

- `generer_index.py` — un `chemin_coffre` qui dit le dépôt, ou un champ qui le dit ;
- `coffre.py` et `make coffre` — ils replient une archive qui ne se verse plus ;
- `restaurer.py` — il doit rendre la main sur ces chemins au lieu de les chercher ;
- la procédure d'ouverture, qui prescrit un dépliage d'archive qui n'a plus lieu.

**Rien de cela ne se fait de ce fil** : il ne déplie rien et ne joue aucun `make`.

*Et une pièce du relevé du 20260908 tombe d'elle-même* :
`referentiels/notes_manuscrit.json`, seul candidat prouvé, n'était pas un document
du coffre — il était **plié dans l'archive**. Il est parti avec elle. Le retrait
qu'A-346 réservait à l'auteur est sans objet.

### Un dérivé ne sort du coffre que sur un rejeu prouvé à l'octet, jamais sur une identité affirmée — 20260908

**Tranché par l'auteur, exécuté par Claude.** La jauge était à 1 027 jetons de sa
borne, et l'auteur a autorisé le retrait des dérivés graphiques — « si tu sais
regénérer, en effet supprime » —, **la condition portant sur la preuve et non sur
l'intention**. A-346 le dit déjà : aucun retrait ne se fait sur une identité
affirmée. La preuve s'est donc faite pièce par pièce, en rejouant le générateur
et en comparant à l'empreinte versée.

| dérivé | rejeu | verdict |
| --- | --- | --- |
| `livrables/galerie_fiches.html` | `30e64637…`, 35 539 o | identique à l'octet |
| `livrables/carte_du_projet.html` | `bd2280f2…`, 23 863 o | identique à l'octet |
| `livrables/etat_machine.html` | `e595ed53…`, 12 208 o | identique à l'octet |
| `livrables/extrait_gagnants_perdants.html` | `7a9994e3…`, 90 277 o | identique **à date égale** |
| `livrables/etat_vecteurs.html` | non rejoué | **reste au coffre** |

*La réserve de l'extrait se nomme* : la page horodate son propre pied, donc elle
ne se compare qu'à date égale. Rejouée le 20260908 elle rend `7a9994e3…` ; la
même privée de son horodatage rend exactement l'empreinte versée `557c74fe…`, au
même compte de 90 277 octets. Ce n'est pas une identité affirmée, c'est une
identité prouvée modulo une variable nommée — et c'est aussi un défaut du
générateur, qui rend un dérivé non reproductible d'un jour à l'autre.

*Ce qui a failli fausser toute la preuve* : le dépôt était **d'une version en
retard** — archive à 1 685 571 o contre 1 721 690 au coffre, index à 87 637 o
contre 89 851. La carte rejouée sortait 23 237 o là où le coffre en portait
23 863, et `etat_machine.py` levait un `KeyError`. **Une divergence de rejeu se
lit d'abord contre l'état du dépôt, jamais contre le générateur** : les deux
« échecs » étaient des faux, et la preuve n'a tenu qu'une fois l'archive et
l'index redéployés depuis le coffre par copie d'octets.

**`etat_vecteurs.html` reste, et c'est A-342 qui le retient.** Il descend de
`REF_norme`, donc du socle budgétaire, donc des cinq classeurs, **qui sont des
pièces jointes et non des documents du coffre**. « Régénérable » se lit depuis le
coffre seul : un dérivé dont la source n'est pas au coffre ne s'y régénère pas,
il s'y verse. C'est la seule des cinq pièces graphiques dont la chaîne sorte du
coffre, et c'est pour cela qu'elle seule y reste.

### L'appareil du relevé d'épreuve se retrouve au transcript, par rejeu de ses écritures

**Tranché par Claude au titre d'A-23.** Le fil du 20260907 avait déclaré comme un
manque que `relever_ecarts_epreuve.py` et `rendre_releve_epreuve.py` n'étaient pas
versés ; le 20260908 ils n'étaient plus au dépôt non plus, le redéploiement de
l'archive les ayant recouverts. Ils n'étaient perdus qu'en apparence.

**Le transcript porte les écritures, pas seulement les lectures.** `restaurer.py`
n'y moissonne que les rendus du coffre — les `project_read`. Les appels `Write` et
`Edit` y sont pourtant écrits verbatim eux aussi, avec leurs chaînes exactes. La
restauration s'est donc faite par **rejeu** : partir du dernier `Write`, rappliquer
dans l'ordre les `Edit` qui le suivent, en exigeant que chaque `old_string`
apparaisse **exactement une fois**. Quatorze retouches rejouées, **zéro échec
d'appariement** : le rejeu est mécanique, rien n'est passé par le modèle.

*Preuve, et elle est externe au rejeu* : les deux modules rejoués sur les mêmes
entrées rendent `releve_bat.tsv`, `releve_bat.md` et
`controle_chiffres_epreuve.json` **identiques à l'octet** à ceux du 20260907. Un
rejeu d'écritures qui redonne les sorties n'est pas une reconstitution, c'est une
copie.

*Portée* : la voie vaut pour tout ce qu'une session a écrit et perdu, tant que son
transcript vit. Elle ne vaut pas pour ce qu'aucune session n'a écrit.

### Le référent d'un nombre se contrôle avec le nombre, et le module le fait maintenant

**Tranché par Claude au titre d'A-23, en application de la règle qu'A-379 par un
autre chemin avait déjà posée.** Les deux modules retrouvés portaient encore le
contrôle arithmétique tel qu'il était avant la reprise de l'auteur : deux
identités inventées qui sortaient des `faux` inexistants, et l'aveuglement sur le
seul endroit où l'épreuve bloque. **Verser le module tel quel aurait planté au
coffre un contrôle dont l'auteur avait déjà dit qu'il était faux** — exactement ce
qu'A-364 nomme : un dérivé versé que personne ne pense à reverser.

Trois corrections, dans le module et non dans le document contrôlé — A-303 :

- **Le compte éducation est retiré du contrôle**, et le retrait est motivé sur
  place : la p. 123 cumule les 6 600 avec les 275, la note 133 les estime sur le
  coût public réel de l'éducation. Ce que l'identité prétendait contrôler relève
  du chiffrage du corpus, pas du bon à tirer.
- **La montée mensuelle se rejoue sur la fenêtre que le texte donne** — latence de
  six mois p. 141, puis six à sept mois à deux points —, et non sur douze mois.
  Elle tombe juste.
- **Le référent décide, plus la valeur.** Le motif de la pension rendait
  optionnel « avec une pension de base » et capturait 1 100 des deux côtés : le
  contrôle sortait `juste` sur une page cassée. Il lit désormais le voisinage —
  celui de l'épreuve et celui du manuscrit, tous deux relevés — et pose
  l'identité que la page nomme. Quand la page ne nomme plus la pension de base,
  1 100 est le socle seul, la note 124 en fait 1 650, et le contrôle sort **faux
  de 550 euros par mois**, avec les deux voisinages cités.

*Mesuré* : le contrôle passe de « 5 justes, 2 faux » — deux faux imaginaires et
la vraie casse invisible — à **« 5 justes, 1 faux »**, le faux étant la p. 105.
Le relevé détaillé ne bouge pas : 858 écarts, 134 comptés en forme.

*Écart déclaré entre le document et son générateur* : `releve_epreuve_EP2.md`
tient neuf lignes de contrôle, le module en pose six — les trois autres ont été
calculées à la main lors de la reprise. **Le document dit plus que son
générateur**, et c'est un manque, pas une divergence de fond : les six que le
module pose s'y retrouvent à l'identique.

### Deux documents étaient au coffre sans être à l'index, et rien ne l'aurait dit

**Constaté et corrigé le 20260908.** `livrables/releve_epreuve_EP2.tsv` et son
`.md` avaient été versés le 20260907 sans être portés à la table de
`generer_index.py`. **Un document au coffre qu'aucune grille ne déclare est un
document que nul rejeu ne refait et que nul contrôle ne relève** : c'est le cas
qu'A-364 décrit, et il s'est produit dans le fil même qui l'a écrit. Les deux
sont désormais à l'index, en `derive`, `coffre: true` — ils descendent des
épreuves, binaires de 3 Mo qui ne se versent pas —, produits par
`rendre_releve_epreuve.py`, et classés en `grilles` à la carte.

*Ce que le contrôle de l'index dit encore, et qui n'est pas une anomalie du
coffre* : 22 fichiers du dépôt ne sont pas déclarés. Ce sont les épreuves, leurs
rendus texte, les relevés intermédiaires et les blocs de rédaction de ce fil —
de l'atelier, pas du coffre. Ils n'ont pas vocation à y aller.

## 20260908 — La relecture comparée des épreuves

*Fil de production, ouvert et clos le 20260908. Il n'a rien corrigé, rien
réécrit, et n'a tranché aucun écart de fond. Entrées titrées et datées, sans
numéro — A-282.*

### Le contrôle des chiffres était faux deux fois, et la cause est une définition inventée — 20260908

**Relevé par l'auteur le jour même, et il avait raison sur les deux.** Le contrôle
arithmétique du relevé d'épreuve sortait deux verdicts `faux`. Aucun des deux ne
portait sur l'épreuve : tous deux venaient d'identités que j'avais posées et que
le corpus n'écrit nulle part.

- **« Le compte éducation devrait valoir douze fois l'aide de l'enfant. »**
  L'épreuve écrit p. 123 « **en plus de** l'aide fondamentale universelle de 275
  euros par mois, versons à chaque enfant 6 600 euros par an » : les deux se
  cumulent. Le `550 × 12` que `controle_arithmetique.py` porte à `D10-2-1-p1` se
  rapporte à **l'aide fondamentale de l'adulte**, et le 6 600 est estimé sur le
  coût public réel de l'éducation. J'ai lu une coïncidence arithmétique consignée
  comme une définition, puis j'y ai substitué le mauvais terme.
- **« +2 % par mois pendant douze mois font 24 points. »** L'épreuve pose p. 141
  une latence — « **au bout de six mois**, les premières économies seront
  constatées et rendues » — avant que la montée commence. Six à sept mois à deux
  points encadrent les 13 % annoncés au bout d'un an.

**Et le contrôle manquait le seul endroit où l'arithmétique bloque vraiment.**
P. 105, l'épreuve retire « avec une pension de base » : 1 100 euros cesse d'être
la **pension de base** — dont le socle est une moitié et l'aide fondamentale
l'autre — pour devenir le **socle seul**. La note 124 de l'épreuve, inchangée,
pose pourtant que « le socle contributif forme avec l'aide fondamentale une
pension de retraite de base ». **Le corps contredit sa propre note, et l'écart
vaut 550 euros par mois et par retraité.** Le contrôle l'a déclaré `juste` parce
qu'il comparait 1 100 au bon nombre.

**Règle, et c'est la sortie utile de la faute** : *un chiffre inchangé dont la
définition bouge est un écart de chiffre.* Un contrôle qui compare des valeurs
sans comparer leurs référents ne le voit pas, et il rassure à tort — c'est A-379
par un autre chemin, où une clé fausse notait faux. **Le référent d'un nombre se
relève avec lui**. Le relevé d'épreuve ne le faisait pas : il comparait des
chaînes autour du nombre, pas la définition que la phrase lui donne. **Il le
fait depuis le même jour** — le module retrouvé au transcript porte le référent
dans le contrôle lui-même, et l'entrée du 20260908 sur le nettoyage du coffre
dit comment.

*Corrigé au coffre le 20260908* : la section de contrôle de
`livrables/releve_epreuve_EP2.md` est reprise — huit contrôles justes, un faux
nommé —, et le bloc de journal du jour avec elle. **Le relevé détaillé ne bouge
pas** : l'écart de la p. 105 y est, en classe `fond` et motif `rédaction`. Le
reclasser en motif `chiffre` demanderait de reverser 95 ko, et la jauge ne le
porte pas.

### La comparaison se fait contre l'épreuve courante, et l'épreuve antérieure ne sert qu'à dater

**Tranché par Claude au titre d'A-23.** Deux épreuves sont jointes au fil, et le
relevé se fait **contre la seconde**, qui est celle d'un bon à tirer. La
première ne se compare pas au manuscrit pour elle-même : elle sert à marquer
chaque écart de son ancienneté — déjà porté par la première, ou apparu entre les
deux.

*Ce que ce marquage rend, et qui est la sortie la plus lourde du fil* : la
première épreuve ne divergeait du manuscrit que par **374 écarts**, la seconde
par **858**, dont **572 apparus entre les deux**. Sans le marquage, un relevé de
858 lignes aurait laissé croire à une composition qui dérive depuis le début.

### La classe se pose par critère mécanique, et `fond` ne juge pas du sens

**Tranché par Claude au titre d'A-23.** Les quatre classes du fil se posent sans
lire : un chiffre qui bouge, un côté vide, une différence qui disparaît quand on
retire casse, accents, ponctuation et appels de note. **`fond` veut dire que la
rédaction change au-delà de la typographie** — le sens *peut* changer, et
l'interdit du fil dit que c'est à l'auteur de trancher.

**Chaque écart porte en plus un `motif`**, à l'intérieur de sa classe : chiffre,
nom propre, rédaction, texte absent, note ajoutée, note retirée, orthographe ou
casse, ponctuation, appel de note. La classe reste l'une des quatre ; le motif
est ce qui permet de lire un relevé de 858 lignes sans que les 47 écarts de
chiffre s'y noient.

*Écarté* : juger du sens pour trier. C'est l'interdit du fil, et un tri qui
juge est un arbitrage rendu en silence.

### Un nombre écrit en lettres porte la même valeur, et ce n'est pas un écart de chiffre

**Tranché par Claude au titre d'A-23.** « vingt-quatre » et « 24 » disent la même
chose : passer de l'un à l'autre est une convention de composition. Les valeurs
se normalisent donc avant comparaison, et le passage se relève en coquille.

*Sans cette normalisation, mesuré* : 73 écarts de chiffre au lieu de 47, dont
« 0 euro » devenu « zéro euro » et « m2 » devenu « mètre carré ». **Les 26 faux
positifs auraient noyé les vrais**, qui sont en tête du relevé.

*Bornes* : « un », « une », « cent », « mille » et « demi » ne comptent pour un
nombre que dans un composé — seuls, ce sont des articles.

### Les notes s'apparient par alignement de leurs textes, jamais par leur numéro

**Tranché par Claude au titre d'A-23, et c'est la décision qui a le plus d'effet
sur le relevé.** Les deux côtés portent 141 notes, et un appariement par numéro
aurait été juste jusqu'à la trente-neuvième et faux ensuite : deux notes entrent,
deux sortent, six changent de rang, et **78 se renumérotent par contrecoup**.

L'appariement se fait par alignement global des textes dépouillés, sans jamais
inverser l'ordre, avec un seuil de ressemblance qui sépare nettement une note
retouchée d'une note étrangère. **La renumérotation se compte en `forme` et ne
se détaille pas** : elle est la conséquence mécanique des quatre notes entrées et
sorties, qui, elles, se relèvent une par une.

*Ce qu'un appariement par numéro aurait produit* : tout le cahier de notes en
écart à partir de la page 149, et les quatre vraies entrées et sorties noyées
dedans.

### Un appel de note se relève à la suite croissante, en deux passages

**Tranché par Claude au titre d'A-23.** L'extraction colle l'appel au mot qui le
précède — « côte1 », et parfois au chiffre qui le précède, « CAC 40 » suivi de
l'appel 116 sortant « 40116 ». Un motif seul confondrait « m2 » et « xixe » avec
des appels.

Le relevé se fait donc **par la suite croissante** : un candidat n'est retenu que
s'il continue la suite. Un numéro que le premier passage ne trouve pas se cherche
au second, **seul entre les deux appels qui l'encadrent** — la composition l'a
détaché de son mot —, et un nombre qui suit un autre nombre n'est jamais un
appel : « 1 104 » ne se lit pas comme un appel 104.

### Une césure de composition ne se décide pas sur le texte extrait

**Tranché par Claude au titre d'A-23.** L'extraction recolle un mot coupé en fin
de ligne **en retirant son tiret** : « Alsace-Lorraine » revient
« AlsaceLorraine ». Ce n'est pas un écart de l'épreuve, c'est une perte de
l'outil.

Les coupes se relèvent au rendu qui garde les lignes, et un écart n'est écarté du
compte **que si le recollement l'explique entièrement** — le manuscrit privé de
ses tirets et de ses espaces doit rendre l'épreuve caractère pour caractère.
Deux écarts sortent ainsi, p. 40 et p. 147 ; ils se disent à part, **à vérifier à
l'œil sur l'épreuve et nulle part ailleurs**.

*Ce que la borne protège* : une première version de la règle, plus lâche,
écartait treize écarts dont onze étaient de vrais changements d'apostrophe et
d'accent.

### Le paratexte se compte en `forme` et ne se compare pas

**Tranché par Claude au titre d'A-23.** La table des matières, les annexes, les
pages liminaires, les faux titres, les intitulés de rang que l'épreuve ajoute —
« PARTIE I », le numéro de chapitre en tête de page — n'ont pas de vis-à-vis au
manuscrit. Les comparer sortirait 134 écarts qui ne disent rien. Ils se comptent,
et le fil l'a écrit : c'est exactement ce que la classe `forme` prescrit.

*Relevé au passage et non tranché* : le manuscrit intitule sa dernière partie
« Alors peut-être… » et l'épreuve la nomme « POSTFACE ». C'est un écart de
structure, il est au relevé, et il revient à l'auteur.

### Le relevé se verse, les épreuves ne se versent pas

**Prescrit par le fil, et exécuté tel quel.** `livrables/releve_epreuve_EP2.tsv`
porte un écart par ligne — page, flux, classe, motif, ancienneté, ancre au
manuscrit, les deux versions —, et `livrables/releve_epreuve_EP2.md` porte le
compte et le contrôle des chiffres. Les deux épreuves sont des binaires de 3 Mo
et ne vont pas au coffre.

*Ce qui ne s'est pas versé non plus, et c'est un manque déclaré* : les deux
modules du relevé, `relever_ecarts_epreuve.py` et `rendre_releve_epreuve.py`. Ce
fil n'a pas déplié l'archive technique, et **une archive ne se réécrit pas depuis
un dépôt qui n'en porte que deux fichiers**. Ils se verseront au premier fil qui
la déplie ; d'ici là, le relevé se refait mais l'outil qui l'a fait n'est pas au
coffre.

## 20260907 — Le corpus contrôle enfin qu'il sait encore se refaire

*Fil de maintenance, ouvert et clos le 20260907. Il n'a produit aucun livrable de
fond, n'a tranché aucune question de doctrine, et n'a écrit aucune skill.
Numérotation à la suite d'A-384.*

### A-385 — Le balayage des générateurs devient un contrôle, et il a mordu trois fois

**A-364 posait le trou en toutes lettres** : *rien ne contrôle qu'un générateur
du coffre tourne encore*, et *le fil qui voudra fermer ce trou jouera tous les
générateurs à vide et comptera ceux qui lèvent*. Deux avaient été trouvés par
hasard — la carte, qui levait depuis deux jours sur un chemin renommé, et l'état
de la machine. **Une page qui ne se régénère plus vieillit en silence**, et rien
ne la distingue d'un dérivé sain tant qu'on ne la rejoue pas.

`appareil/controle_generateurs.py`, joué par `make generateurs`. Il prend les
producteurs que l'index déclare, joue chacun **par la règle du fichier de
construction** — A-343 pour la reproductibilité, A-382 pour l'écrasement — et
sort cinq verdicts, dont trois bloquent.

**Il ne va pas dans `make controle`, et le motif est de définition** : le
balayage **écrit au dépôt**, il régénère pour de vrai, faute de quoi il ne prouve
rien ; `controle` ne produit rien. Il se demande, et il se demande à la clôture.

**Ce qu'il a trouvé au premier passage, mesuré et non estimé.**

- **Une cible pour deux artefacts.** `PORTES` désignait
  `livrables/portes_domaine.md` en tête de fichier et
  `referentiels/portes_ouvertes.tsv` trois cents lignes plus bas. Les deux
  règles vivaient parce que `:=` s'expanse à la lecture ; **le premier
  déplacement de ligne en aurait tué une**, sans bruit. `LOTS` était affectée
  deux fois à la même valeur — inoffensif, et c'est le même défaut.
- **Six sorties qu'aucune cible ne nommait.** `articles_ouverts_plf.py` écrit
  trois fichiers et une seule cible le déclarait ; `tracer_economies.py` et
  `reconcilier_operateurs.py` en écrivent deux chacun, et leur JSON n'était nulle
  part. **Une sortie qu'aucune cible ne nomme ne se rejoue jamais par `make`.**
- **`make tout` s'arrêtait sur le premier consommateur du socle budgétaire**, et
  donc ne refaisait rien de ce qui vient après. Le socle vient des cinq
  classeurs, qui sont des pièces jointes. La garde porte désormais sur l'entrée
  dans `tout`, jamais sur les règles elles-mêmes : le balayage doit pouvoir les
  jouer une par une pour dire quel intrant leur manque.

*Après correction* : **zéro échec bloquant**, vingt-six générateurs en attente
d'une pièce jointe, nommée pour chacun.

*Ce que le contrôle a dû apprendre à distinguer, et c'est ce qui le rend
utilisable* : `make` rend le même message quand la cible demandée n'a pas de
règle et quand c'est **un de ses prérequis** qui n'en a pas. Le premier est un
défaut, le second est une pièce jointe absente. Le départage se fait sur le
chemin que `make` nomme, et sur les cibles que le fichier déclare **y compris
sous une garde inactive**.

### A-386 — `make reindex` n'existait pas, et c'est ce qui faisait disparaître les artefacts

**Constaté en portant deux entrées, et c'est la cause commune d'A-364 et
d'A-381.** L'index est un dérivé : l'index le déclare lui-même produit par
`generer_index.py`. **Aucune règle du fichier de construction ne le rejouait.**

D'où le mécanisme qui a mordu deux fois : un fil verse une pièce, l'écrit dans
l'index dérivé, et ne la porte pas à la table curée. Rien ne le voit, parce que
rien ne rejoue. **Le prochain rejeu la dé-déclare en silence.**

La règle est écrite, et elle est explicite plutôt qu'attachée à `tout` : l'index
est une entrée de presque tout le reste, et le refaire au milieu d'une chaîne
ferait tourner la chaîne sur deux états.

### A-387 — Deux pièces du second banc étaient au coffre et invisibles à l'index

**Sorties par `I6`, une fois l'inventaire du coffre relevé.**
`methode/banc_gl.md` et `methode/prompt_fil_joueur_banc_gl.md` ont été versés le
20260907 par le fil du second banc, portés au dérivé et **pas à la table curée** —
exactement ce qu'A-381 venait de constater sur le premier banc, dans le fil qui
l'écrivait. La faute s'est répétée dans le même geste.

Elles sont portées, et leur famille avec. `I6` retombe à zéro.

*Relevé au même passage, et c'est un défaut de l'inventaire lui-même* :
l'inventaire du coffre ne porte que les **documents**. Y verser aussi les pièces
jointes faisait sortir les huit classeurs en `I6` à perpétuité, leur nom réel ne
pouvant pas coïncider avec le chemin normalisé que l'index leur donne. La
confrontation des pièces jointes à l'index reste ce qu'elle était : un geste de
l'ouverture, qu'aucun script ne sait faire.

### A-388 — La stratégie réseaux est sortie du projet, et A-366 disait le contraire

**Constaté à la confrontation des pièces jointes.** A-366 écrivait le 20260906 :
*« La stratégie réseaux, elle, reste au projet — l'auteur la croyait retirée,
elle y est encore. »* Elle n'y est plus. La même entrée nommait le prix : *« sa
sortie ne coûte rien au corpus si elle intervient après une digestion courte, et
perd le reste sinon. »*

**Ce qui est digéré tient** : le lexique (A-53), la date de parution du livre et
son identification au manuscrit par recoupement verbatim (A-55), trois angles
morts (A-54). **Ce qui sort avec elle et n'est digéré nulle part** :
l'architecture des comptes, le plan de lancement, les cinq postures, les scripts.

Elle va au bloc des manquants avec ce motif. **Son entrée d'artefact reste**, et
c'est A-354 : une source sortie reste la source que sa digestion cite, et c'est
son entrée qui fait résoudre le renvoi. Dix manquants déclarés.

### A-389 — `I1` sortait en échec depuis A-338, qui disait le contraire

**A-338 pose le 20260902 qu'`I1` n'est pas un invariant** : il compte ce qu'un
fil a régénéré, pas ce que le corpus porte, et sa valeur ne se compare qu'à
périmètre identique. **Le code le comptait quand même parmi les échecs.**

Conséquence tenue pendant cinq jours : `controle_index` rendait `1` à tout fil
qui ne déplie qu'une partie du coffre — c'est-à-dire tous —, et `make controle`
sortait en erreur. Les fils ont écrit « zéro échec sur tous les contrôles joués »
en lisant les compteurs, sans que le code de retour le confirme.

**C'est A-349, mot pour mot** : une règle qui n'est pas dans le code n'est pas
une règle. `I1` se compte à part et se dit ; il ne bloque plus.

### A-390 — Le contrôle du lexique balayait des documents qui ne sont pas des livrables

**Éprouvé pour la première fois sur des livrables régénérés**, ce qu'A-365
déclarait n'avoir jamais eu lieu : le seul livrable au dépôt du fil qui l'a écrit
sortait à zéro. Sur trente-sept, il en sortait douze.

**La plupart n'étaient pas des fautes, et le périmètre en était la cause.** Le
lexique est une règle de **livrable diffusable** — l'index l'écrit à
`consomme_par`. Balayer `livrables/` en entier y faisait entrer les vues
internes, qui portent la nomenclature interne par construction, et les relevés de
notes, qui portent du verbatim du manuscrit. **Ni les unes ni les autres ne se
réécrivent.** Le périmètre se lit désormais à la carte : les familles
`graphique`, `rédactionnel` et `juridique`, et rien d'autre.

**Deux corrections de mécanique, aucune de règle.** « en apparence » rejoint les
marqueurs de dénonciation — le motif écrit `apparent` ne mordait pas sur
`apparence`, et « des études gratuites en apparence » est une dénonciation
exemplaire. Et « à titre gratuit », locution du code civil qui qualifie une
transmission, reçoit une exemption nommée **dans le module de contrôle et jamais
dans le document contrôlé** (A-303).

**Ce qui reste après bornage est de fond, et cela remonte à l'auteur** : trois
emplois, dans quatre livrables. « La gratuité » en vedette de perte, où la charge
tient à la position et non à la phrase. « L'instruction gratuite des jeunes
Français » au manifeste, qui est un emploi affirmatif. Et « les fonctionnaires »
dans l'énumération des boucs émissaires, où le substitut inverserait le sens de
la phrase. **Le fil ne les corrige pas** : ce sont des livrables diffusables.

### A-391 — Les deux modules manquants ne se réécrivent pas à l'aveugle, et le motif se dit

**A-343 a réécrit `articles_ouverts_plf.py` et l'a prouvé à l'octet.** Ce qui
rendait la réécriture sûre était une asymétrie nommée : le module manquait, **sa
sortie était versée**, et une sortie versée est une spécification exécutable.

Cette asymétrie n'existe pour aucun des deux modules restants.
`referentiels/portes_ouvertes.tsv` n'est pas au coffre — c'est un dérivé, et la
règle qui le produit le dit. `controle_socle_plf.py` ne rend rien qu'on puisse
comparer : il rouvre la pièce jointe et sort des verdicts. **Les réécrire
maintenant, ce serait les croire au lieu de les prouver.** Ils restent aux
manquants, avec ce motif.

### A-392 — Trois dérivés du coffre étaient en retard, et personne ne pouvait le savoir

**Sorti du balayage, verdict `V5`.** La carte du projet, la galerie des fiches et
l'extrait gagnants-perdants ont bougé au rejeu : le coffre en portait des
versions antérieures à ce que leur source produit aujourd'hui.

**L'extrait est le cas qui instruit.** Le coffre en portait 78 663 octets ; son
empreinte de référence en attendait 90 222 ; le rejeu en rend 90 277. **Les trois
chiffres diffèrent**, ce qui veut dire qu'un fil l'a régénéré, a relevé son
empreinte, et ne l'a pas reversé. C'est le cas exact qu'A-364 décrivait pour la
carte, sur un artefact que rien ne signalait.

Les trois sont reversés. *Et c'est l'argument qui manquait à A-346* : les quatre
dérivés HTML restent candidats à la sortie du coffre, et **leur retard est un
motif de plus** — un dérivé versé qu'aucun fil ne pense à reverser est pire
qu'un dérivé absent.

## 20260907 — Le second banc est construit, et l'appareil de mesure sortait faux de trois manières

*Fil de production, ouvert et clos le 20260907. Il n'a joué aucune étape du banc
qu'il construit, et il n'a écrit aucune réponse. Numérotation à la suite d'A-376, qu'un autre fil a prise le même jour sur la valise de matériel.*

### A-377 — Le second banc est versé, et sa clé ne l'est pas

**42 couples pour 37 numéros d'amendement**, sur les trois liasses déposées d'un
tiers, entrées par pièce jointe. `methode/banc_gl.md`.

**Ce que ce banc a et que le premier n'a pas** : sa vérité-terrain n'est pas la
nôtre. Elle existait avant qu'on la regarde et personne chez nous n'a choisi ce
qu'elle dirait. C'est le seul banc du corpus dans ce cas, et c'est tout son
intérêt — le premier banc mesure si la machine fait ce qu'on veut, celui-ci
mesure si elle fait ce qu'un praticien fait.

**Deux choses ne se versent pas, et pour deux raisons différentes.** La clé —
`appareil/scinde/cles_eval.json` — parce qu'elle est la vérité-terrain et qu'elle
se régénère des pièces jointes en une commande. Les liasses converties et les
couples scindés, parce que c'est l'atelier d'une éval : il va dans `scinde/`,
ignoré comme `eval/`, `coffre/`, `droit/` et `plf/` (A-363).

**La forme diverge du premier banc sur un point, et c'est nécessaire.** Au
premier banc, les seize énoncés aveugles sont écrits à la main et vivent dans le
document. Ici l'énoncé **est** l'exposé sommaire du déposant : il ne se réécrit
pas, il s'extrait, et le document ne le recopie pas. Le banc décrit donc ses cas
**par famille** — ce que le couple apporte — et non par mesure.

*Le prompt du fil qui jouera est écrit et il ne porte aucune réponse* :
`methode/prompt_fil_joueur_banc_gl.md`.

### A-378 — La clé était fausse sur neuf couples, et c'est un contrôle qui l'a dit

**A-261 posait la règle : une clé fausse note faux, et seul un contrôle mécanique
l'attrape.** Elle n'était pas outillée. `appareil/controle_cles_gl.py` sort `K1` à
`K6`, il est joué à `make controle`, et **il a mordu au premier passage.**

**Le défaut est le troisième de la même famille que les deux d'A-261, un cran
plus bas.** L'extracteur ne relevait que **le premier fragment d'une
énumération** : une phrase qui abroge n articles n'en portait qu'un à la clé, et
sur le cas le plus lourd huit tombaient. Et le motif du numéro coupait tout
suffixe qu'il n'avait pas prévu — ceux plus loin dans l'alphabet que sa borne
écrite, et **les suffixes doublés**, dont le radical sortait nu.

**La correction ne réécrit aucune grammaire, et c'est le point.** Le corpus en
portait déjà deux, et les deux sont désormais **appelées** : la suite de numéros
d'articles du socle du texte déposé — dont il est écrit noir sur blanc qu'elle
est *plus large que celle de `ref_norme`* et dont l'écart est *compté et déclaré
plutôt qu'absorbé* — et le découpage en fragments d'énumération de la table des
articles ouverts (A-343 : la virgule, le point-virgule et « et » séparent, « à »
ne sépare pas). L'adresse retenue est **le libellé exact du fragment**, comme à
cette table.

*Une correction plus large a été écrite, mesurée, puis retirée.* Élargir le
suffixe dans `ref_norme` lui-même réparait 39 divergences déclarées au PLF — mais
`ref_norme` alimente `REF_norme`, les deux tables plates versées et deux skills,
et **son écart est une position déclarée du corpus, pas un défaut**. Le fichier
est reposé **identique à l'octet** à ce que le coffre porte, vérifié.

**Ce que la correction change, mesuré et non estimé.** Neuf couples sur
quarante-deux portaient une clé fausse, dont **huit des vingt-quatre couples de
norme du lot de finances** — un tiers de la population qui a été mesurée. 42
adresses entrent à la clé, 10 en sortent.

### A-379 — Deux défauts de plus dans l'appareil de mesure, et un démenti

**Le premier ne pouvait pas se voir avant.** La clé ne portait qu'un véhicule ;
elle porte les trois liasses depuis ce fil. Le noteur filtrait sa population sur
la **seule nature du couple**, ce qui faisait entrer les six couples de
financement dans le dénominateur du lot de finances — six cas sans réponse, et un
taux faux par le bas. **La population d'un lot est celle de son véhicule**, et le
véhicule se dérive de la partie de la liasse, jamais ne se suppose (G1).

**Le second était écrit dans le module et pas dans le code.** Le noteur annonçait
dans son propre docstring qu'« un article cité dans la fourchette relevée » vaut
concordance, et `verdict` ne le faisait pas : une skill qui rendait la **borne
basse** d'une fourchette sortait en voisinage. C'est A-349 par un autre chemin —
*une règle qui n'est pas dans le code n'est pas une règle.* Corrigée sur la borne
basse seule ; l'intérieur de la fourchette attend son dépliage, et cela se dit.

**Le troisième défaut était dans le contrôle neuf, et il s'est fait prendre sur
la première pièce qu'il avait à contrôler.** `K5` cherchait une fuite d'adresse
derrière « article » au singulier seulement. La première rédaction du banc citait
en verbatim une énumération de la clé — neuf adresses —, et `K5` ne la voyait
pas. Élargi, il l'a sortie ; le banc ne la cite plus. **Un contrôle trop étroit
rassure sans rien garantir.**

**Et la correction dément une phrase publiée.** A-259 concluait : *« Aucune
adresse n'a envoyé l'amendement au mauvais endroit. C'est le résultat qui compte
le plus. »* **C'était un effet de la clé fausse.** Sur la clé corrigée, un cas
sort en discordance — celui-là même qu'A-259 décrivait deux paragraphes plus loin
comme un vrai manque, un crédit d'impôt déclaré sans siège alors qu'il en a un.
**Les deux affirmations se contredisaient dans la même entrée**, et rien ne
l'avait vu parce que le verdict venait d'une clé vide.

**Les taux se relisent sans rejouer la skill**, les réponses étant au coffre.

| lot de finances, 22 notés | clé fausse | clé corrigée |
|---|---|---|
| concordance | 14 — 63,6 % | 20 — 90,9 % |
| voisinage | 8 — 36,4 % | 1 — 4,5 % |
| discordance | 0 — 0 % | **1 — 4,5 %** |
| précision | non publiée | 27 justes sur 42 rendues — 64,3 % |

Au lot de financement, le rappel ne bouge pas — 6 sur 6 — et la précision est
neuve : **6 justes sur 13 rendues, 46,2 %.** Elle n'avait jamais été publiée sur
ces deux lots : la dimension a été ajoutée au noteur après leur mesure, et aucun
fil ne l'avait relue depuis. **Elle est basse, et c'est la sortie neuve du
relevé** — la skill trouve l'adresse, et elle en ramasse d'autres avec.

*Les deux lectures ne se comparent pas comme deux mesures de la skill : c'est la
même sortie, notée deux fois. Ce qui se compare, ce sont les deux clés.*

### A-380 — L'écart de compte des liasses est fermé par explication, non par comblement

**Le banc portait « deux manquent, et l'écart se relève plutôt qu'il ne se
comble ».** Il est relevé, et les deux causes n'en font pas une.

Le contre-budget est annoncé à 39 amendements. Les trois liasses portent **38
en-têtes**, et **37 numéros portent un couple**.

- **le n° 37 est absent des trois pièces.** Aucun en-tête ne le porte : il n'est
  ni perdu par l'extracteur ni mal découpé, il n'y est pas.
- **le n° 8 porte un dispositif et aucun exposé sommaire.** Son en-tête est là ;
  le couple ne se forme pas, et un couple sans exposé n'est pas un cas.

**La liasse de financement porte 6 numéros**, et non les 8 que la soustraction
laissait attendre. Le banc annonçait 8 « restants » : c'était une déduction, pas
un relevé.

*Fait relevé au passage et qui fait un cas d'épreuve* : un couple de la liasse de
financement porte une ligne de rattachement qui dit littéralement « Après
l'article X ». **Le déposant n'a pas résolu son propre véhicule.** C'est `G1` par
l'absurde : le véhicule est une donnée, et la donnée manque.

### A-381 — L'archive se remplace, et l'ordre des gestes est ce qui le permet

**Mesuré, non estimé.** Cinq pièces de l'appareil ont changé au fil du banc, et
elles vivent dans l'archive technique. La sortir de l'archive par la table
d'exception d'A-349 a été écrite, puis **retirée avant d'être versée** : elle
ouvrait un trou de restauration. L'archive du coffre aurait continué de porter
les anciennes versions, `coffre.py deplier` les aurait écrites au dépôt, et
`restaurer.py` — qui **n'écrase jamais un fichier présent** — n'aurait pas posé
les neuves par-dessus. **Le coffre aurait rendu l'ancien appareil sans rien
dire.**

L'archive se remplace donc en entier. Elle passe de 1 685 571 à 1 704 181 octets,
77 fichiers, et **son dépliage est prouvé 77 sur 77 à l'octet avant tout
versement**. Ce qui rend le remplacement possible est l'ordre des gestes d'A-357,
et lui seul : **supprimer, puis verser**. La pièce neuve n'est pas créditée de la
place que l'ancienne libère (A-312), et une archive de cette taille ne se réécrit
pas par-dessus elle-même.

*Ce que la table d'exception reste* : bonne pour une pièce qui n'a jamais été
dans l'archive — c'est le cas des deux référentiels de rédaction et des deux
modules de la réapplication. Elle est mauvaise pour une pièce qui y est déjà,
tant que l'archive n'est pas réécrite au même geste. **La règle manquait, et elle
s'écrit ici.**

*Relevé au même geste, et c'est A-364 qui se répète* : le premier banc était au
coffre, l'index du coffre le déclarait, et **la table curée de
`generer_index.py` ne le portait pas.** Le fil qui l'a versé a écrit l'index sans
porter son entrée là où elle vit. Régénérer l'index l'aurait dé-déclaré en
silence ; c'est `I2` qui l'a vu, et l'entrée est portée. **Un artefact déclaré
dans le dérivé et absent de la table curée est un artefact qui disparaît au
prochain rejeu.**

### A-382 — Un générateur joué à la main a écrasé le référentiel de doctrine, et c'est ma faute

**Faute de Claude, constatée et réparée dans le même geste.**
`construire_positions.py` prend **un seul argument, sa sortie**. Je l'ai appelé
avec deux, source puis destination, et il a écrit les positions **par-dessus
`referentiels/REF_doctrine.json`**. Le référentiel de doctrine a été corrompu au
dépôt pendant deux commandes.

**La réparation est mécanique et prouvée.** Le fichier a été repris de l'archive
dépliée et comparé à son empreinte : `348132` octets,
`8beb2e0fd63ba268a8bc8f6e8d9038800c1582d13600408a9cf6a8ec0eae149f`, **identique**.
Puis `positions.json` a été régénéré **par la règle du `Makefile`**, et il
ressort à `242572` octets, `b159cb9e…8cdbe4e` — exactement ce qu'A-356 avait
prouvé le 20260904.

*Ce que la faute enseigne, et c'était déjà écrit* : A-343 dit que le rejeu passe
par la règle du `Makefile`, jamais par un appel à la main. La règle y était pour
la reproductibilité ; **elle protège aussi de l'écrasement**, parce qu'elle porte
l'ordre des arguments. Un générateur ne se joue pas à la main sans avoir lu sa
ligne d'usage — et la mienne était à trois lignes du haut du fichier.

### A-383 — Le banc est une pièce de la machine, donc dû au déménagement d'A-375

**Constaté à la clôture, et cela revient à l'auteur.** A-375 décide que le point
de vérité de chaque pièce de la machine est au projet machine, et que le coffre
actuel n'en garde aucune copie vivante. **Le banc construit ici est une pièce de
la machine**, et il est versé au coffre actuel parce que c'est le seul que ce fil
puisse atteindre : une session ne voit qu'un projet.

Ce qui est dû au transfert, et l'inventaire se tient maintenant plutôt qu'après :

```
methode/banc_gl.md
methode/prompt_fil_joueur_banc_gl.md
referentiels/lots_epreuve.json
appareil/scinder_liasses.py
appareil/cles_eval_gl.py
appareil/noter_eval_gl.py
appareil/controle_cles_gl.py
les trois liasses PDF, qui rentrent par pièce jointe
```

**La clé ne se transfère pas** : elle se régénère des pièces jointes de l'autre
côté, en une commande, et c'est ce qui rend le banc transportable.

*Et le déménagement change la mesure, ce qui est l'argument d'A-375 lui-même* :
éprouvée dans le projet qui la porte, la chaîne est éprouvée **sans la doctrine
sous la main** — ce qu'A-267 exige de toute étape de la machine. Les taux relus
ici l'ont été avec le coffre à portée ; ils sont donc des plafonds pour ce que la
version diffusée sait faire, et non des planchers.

### A-384 — Un second fil versait au coffre pendant celui-ci, et cela se constate

**Relevé mécaniquement, à `make restauration`.** Le registre restauré en
ouverture faisait 120 969 octets ; l'empreinte de référence en attendait 130 865 ;
une seconde lecture, en fin de fil, en a rendu 132 721. **Le coffre a bougé trois
fois pendant ce fil**, et l'index qu'il porte n'était plus celui que les
empreintes décrivaient.

**Ce que la procédure a bien fait.** `restaurer.py` a vu les deux états du
registre, a retenu le plus récent et **a nommé celui qu'il écartait, avec son
horodatage** — c'est exactement ce que sa garde promet. Le bloc de ce fil est
porté sur le corps le plus récent, par découpe et non par recopie.

**Ce qui reste ouvert, et ce n'est pas de la tambouille.** Rien n'empêche deux
fils de verser la même pièce, et le second efface le premier sans le dire. Ce fil
n'a pas de quoi le régler : il l'a constaté, il a relu avant d'écrire, et il
l'inscrit. *La règle « une seule tranche active à la fois » suppose un seul fil
actif ; elle n'est pas outillée.*

## 20260907 — Le matériel entre par une valise, et l'à-blanc devient la moitié d'une mesure

### A-376 — Le matériel voyage dans une valise séparable, et une étape nomme un rôle plutôt qu'un fichier

**Tranché par l'auteur le 20260907**, contre une lecture trop courte d'`A-368` que Claude avait tenue pour un interdit de principe. *La question n'est pas « la doctrine dedans ou dehors », c'est **dépendance ou commodité**.* Le motif existait déjà, isolé sur un cas : la source de niches est une commodité, non une dépendance, et sans elle la skill retombe sur le gage standard qu'elle écrit. Il devient général.

**Trois règles, et elles se tiennent ensemble.**

1. **Aucune étape ne dépend du matériel.** Elle déclare ce qu'elle rend quand il manque, et le contrôle de généralisation le signale quand elle ne le dit pas. **Le mode à blanc n'est pas un mode de test, c'est le mode de base.**
2. **Une étape nomme un rôle, jamais un fichier.** « Un réservoir d'arguments sourcés », « une source de niches », « les annexes du texte déposé ». C'est le dossier qui dit quel fichier tient le rôle. Un tiers y branche les siens, et rien de ce qui identifie n'apparaît dans une skill.
3. **Le matériel vit dans une valise séparable et optionnelle.** On la retire pour diffuser, on la garde pour l'usage propre. C'est ce qui autorise la doctrine à y entrer sans que la machine en dépende.

**L'à-blanc ne disparaît pas, il devient la moitié d'une mesure.** Le banc se joue **deux fois sur la même population aveugle** — à blanc, puis équipé. **L'écart entre les deux taux est la valeur du matériel**, un chiffre et non une impression. Les deux passes se comparent au sens d'`A-308`, seul l'équipement changeant.

**La doctrine entre projetée en clair, jamais brute.** Arguments et chiffres sourcés, écrits pour être lus, sans aucune nomenclature interne. *La projection n'est pas un coût de production : c'est elle qui sépare la machine de la source.* Le brut emporterait la nomenclature, et toute sortie qui s'y appuie serait à nettoyer avant de sortir.

**Ce que la valise porte au premier tour** : les annexes enrichies du texte déposé — taxes affectées, dépenses fiscales —, qui sont la matière de la troisième branche du gage, et un réservoir d'arguments sourcés pour l'exposé.

*Amende `A-368`* : son exclusion vaut pour le socle du projet machine, non pour la valise. *Restent interdits* : qu'une étape nomme une pièce de la valise, et qu'elle échoue en son absence. *Écarté* : la doctrine comme dépendance ; le référentiel brut dans la valise ; deux points de vérité pour une même pièce.

**Ce que l'amendement oblige à reprendre avant la bascule** : le contrat de la chaîne, pour y écrire la règle du rôle ; les skills diffusables, dont le vocabulaire traite encore la base documentaire absente comme un cas dégradé ; la troisième branche du gage, qui cite les annexes par leur nom au lieu de leur rôle ; la procédure de contrôle, pour que les deux configurations soient deux passes d'une même population et non deux bancs.

## 20260907 — Le déploiement s'accélère : le projet machine se crée et reçoit le banc

### A-375 — Le projet machine se crée maintenant, et le banc s'y joue plutôt qu'au projet actuel

**Tranché par l'auteur le 20260907**, en accélération assumée du calendrier. Le projet dédié à la machine **se crée immédiatement** et reçoit son sous-ensemble sans attendre. **Le banc bout en bout — les chouchous d'abord, les cas déposés ensuite — s'y joue**, et non au projet actuel.

*Amende `A-368` sur son calendrier et sur le lieu de l'épreuve.* Tombent : « le montage et les tests restent au projet actuel jusqu'au dixième chouchou validé » et « copie en fin de deuxième jour ». **Tiennent, et sans changement** : le périmètre du sous-ensemble, et l'interdit d'écrire à deux endroits.

**L'interdit devient plus exigeant, pas moins.** Dès la copie, **le point de vérité de chaque pièce de la machine est au projet machine** ; le projet actuel n'en garde aucune copie vivante. Une pièce qui vivrait aux deux endroits est un second point de vérité, et c'est ce que la maison refuse depuis toujours.

**Ce que l'accélération achète, et c'est l'argument de fond.** Éprouver la machine dans le projet qui la porte, c'est l'éprouver **sans la doctrine sous la main** — exactement la condition qu'`A-267` pose à toute étape de la machine. Le banc joué au projet actuel aurait mesuré une capacité que la version diffusée n'a pas.

**Le transfert passe par pièces jointes.** Une session ne voit qu'un projet : le fil ouvert sur le projet machine ne peut rien aller chercher au coffre actuel. Les pièces s'exportent d'un côté, se téléversent de l'autre, et l'inventaire de ce qui est parti se tient.

*Écarté* : attendre le dixième chouchou pour basculer. *Caduc* : le calendrier de `A-368`, et lui seul.

## 20260907 — La stratégie de la machine est arrêtée, et la v1 est bornée à deux jours

*Arbitrages rendus par le fil « stratégie de la machine », tenu hors de l'atelier les 20260906 et 20260907, et portés ici par le fil d'inscription. Numérotation à la suite d'A-366. Les relevés postérieurs sont du fil d'inscription, datés, et ne modifient aucune décision.*

### A-367 — L'interface de la v1 est un projet dédié et un zip, et trois arrêts la tiennent en conversation

**Tranché par l'auteur le 20260907.** La machine s'utilise dans un projet Claude public portant ses instructions et ses skills ; en version dégradée, un zip de skills installable. **Trois arrêts « je vérifie et j'ajuste »** dans la conversation : dispositif, exposé, modificatif.

*Écarté* : toute interface externe appelant l'API. Elle n'aurait sous la main ni le dépôt de droit ni les skills, et elle n'est pas atteignable dans le délai d'un à deux jours.

*Relevé postérieur, 20260907, par le fil d'inscription* : **la création d'un projet public est fermée par les contrôles de l'organisation.** La décision tient, son support change — un second projet **privé** porte le sous-ensemble, et la diffusion à un tiers passe par les skills enregistrées et par le zip, jamais par un projet. Publier reste une décision distincte, à reprendre le jour où un tiers demande le code.

### A-368 — Le projet actuel ne se découpe pas, le projet dédié en reçoit un sous-ensemble

**Tranché par l'auteur le 20260907.** Le projet Résolution n'est pas découpé. Le projet dédié reçoit **un sous-ensemble** : les skills de la chaîne, le contrat, le gabarit d'exposé, les grilles de portes et de recevabilité, la règle de gage, et plus tard la digestion du texte déposé. Il n'emporte ni manuscrit, ni doctrine, ni positions, ni référentiel de normes, ni Constitution, ni loi organique. Le dépôt de droit est partagé et hors jauge.

**Le montage et les tests restent au projet actuel jusqu'au dixième chouchou validé**, la copie se fait en fin de deuxième jour, et **rien ne s'écrit à deux endroits avant**.

*Écarté* : découper le projet actuel avant de basculer. *Caduc* : l'hypothèse de découpage posée à l'ouverture du fil de stratégie.

### A-369 — La recevabilité se joue en liste de contrôle, et l'étape n'est pas outillée en v1

**Tranché par l'auteur le 20260906.** Le rattachement n'est pas outillé pour la v1. La recevabilité se joue par le test de rattachement, par la grille des portes de la loi organique relative aux lois de finances en verbatim, et par les portes de la loi de financement — `LO 111-3-6` à `LO 111-3-8` —, tenues en liste de contrôle dans la chaîne. Les bases existantes, règles de gage et dépense à valoriser, suffisent à cette phase.

*Écarté* : outiller le rattachement avant le premier bout en bout. *Caduc* : le fil « recevabilité légère » prévu au schéma du 20260906.

### A-370 — Le gage s'écrit au lieu de se laisser à trancher, et sa formule est relevée

**Tranché par l'auteur le 20260907.** La skill de rédaction cible **écrit le gage**, en dernier paragraphe du dispositif. Quatre branches, dans l'ordre.

1. **La mesure produit-elle une perte de recettes ?** Sinon, pas de gage : une charge nouvelle ne se gage pas.
2. **La consigne du dossier** — « sans gage », « gage fourni », « gager sur telle niche ».
3. **Sans consigne, une niche en rapport** — même impôt ou même secteur —, cherchée au référentiel de normes puis à l'annexe des dépenses fiscales. **Une niche ne se gage qu'une fois par lot.**
4. **À défaut, le gage standard**, formule entière, État seulement.

**Le gage est un paragraphe de l'amendement, jamais un fragment du texte cible.** L'explication du gage postiche reste à l'exposé sommaire (A-224).

**La formule standard, relevée sur pièce** — source : amendements à l'Assemblée nationale au projet de loi de finances pour 2026, texte n° 2247, janvier 2026, commission des finances et séance, formule constante :

> La perte de recettes pour l'État est compensée à due concurrence par la création d'une taxe additionnelle à l'accise sur les tabacs prévue au chapitre IV du titre Ier du livre III du code des impositions sur les biens et services.

*Non tranché, et cela ne se comble pas de mémoire* : les formules pour une perte supportée par les collectivités et pour une perte supportée par les organismes de sécurité sociale. **Elles se relèveront sur pièce au premier cas concerné.**

*Écarté* : un fil « gage » distinct ; refuser de gager en cas de difficulté. *Caduc* : la mention « gage » à la ligne des non-tranchés de la fiche de rédaction cible.

*Relevé postérieur, 20260907* : le § 10 est à la skill enregistrée et il a passé le contrôle de généralisation à zéro échec. **Il ne se verse pas au coffre** : le point de vérité d'une skill est la skill enregistrée, jamais une copie (A-269).

### A-371 — Un article manquant se résout au dépôt de droit, et une recherche ne vaut jamais verbatim

**Tranché par l'auteur le 20260907.** Un article absent du dépôt de droit — codifié ou non, siège en loi de finances antérieure compris — s'obtient en **ajoutant l'identifiant du texte au fichier des codes** ; l'action du dépôt rafraîchit, le fil suivant clone. La recherche publique reste possible **en dernier recours et en repérage seulement** (A-234) : elle ne fournit jamais un verbatim. Les sites de l'Assemblée et du Sénat servent au texte déposé, au texte adopté, aux amendements et à leur sort, et aux formules de gage — **jamais au droit consolidé**.

*Écarté* : traiter le droit non codifié comme une borne définitive de la matière. *Caduc* : le constat de borne du prompt de stratégie, pour ce qui concerne la voie de résorption.

*Relevé postérieur, 20260907* : le dépôt est **ancré au projet en lecture**, et la lecture est vérifiée depuis l'atelier — révision `553a723` atteinte. **L'écriture n'est pas ouverte pour autant** : aucun jeton et aucun client n'est disponible à l'atelier. Pousser le module de coordination demande un jeton posé, ou la machine de l'auteur.

### A-372 — L'ordre de la liasse suit le texte en discussion, la doctrine ordonne à l'intérieur

**Tranché par l'auteur le 20260907.** Les amendements d'une liasse se rangent **dans l'ordre des articles du texte en discussion**, en indicatif global ; à l'intérieur d'un même rang, l'ordre des blocs de doctrine. Sauf consigne contraire de l'utilisateur.

*Écarté* : l'ordre de doctrine comme ordre principal. *Précise A-310*, qui laissait l'ordre de dépôt entier à l'auteur : l'indicatif est désormais écrit, la chute et l'ordre final restent à lui.

### A-373 — Le socle reste le texte initial, et l'année est un paramètre du dossier

**Tranché par l'auteur le 20260907.** Le socle est le **texte initial déposé par le gouvernement**, n° 1906, octobre 2025. On y reste.

**Année, numéro de texte et fichier de socle sont trois paramètres du dossier** — jamais inscrits dans une skill, jamais dans le contrat de la chaîne. Architecture pour l'exercice suivant : socle remplacé par le même extracteur, digestion régénérée, appariement doctrine contre texte rejoué ; **les blocs de doctrine, eux, ne bougent pas**.

*Fait relevé* : le projet de loi de finances pour 2026 a porté **deux numéros** à l'Assemblée, n° 1906 au dépôt et n° 2247 en janvier 2026. *Écarté* : reprendre le socle sur le second.

### A-374 — Le banc bout en bout part de dix mesures choisies, les cas déposés viennent en troisième lot

**Tranché par l'auteur le 20260907.** Le premier banc bout en bout porte **dix mesures choisies par l'auteur**, couvrant une niche, un opérateur, une taxe, une dépense, une refonte complexe et d'autres types, **en deux lots — trois puis sept**. Les cas déposés par un tiers forment le **troisième lot**, et c'est le seul qui porte une vérité-terrain.

**Le protocole.** Énoncés donnés comme un tiers les donnerait, sans adresse d'article ni identifiant interne. **Un fil vierge par lot.** Trois arrêts par mesure. Verdict `déposable` · `à corriger` · `hors capacité`, avec l'étape fautive nommée. **Chaque correction devient un cas au banc.** Clôture de lot avec le taux par étape, et les corrections remontées aux skills **en une seule opération**.

**L'ordre d'assemblage qui en découle**, tiré des dépendances et non d'un calendrier : inscription et versements d'abord ; puis les dix énoncés ; puis le bout en bout sur trois mesures simples ; puis l'exposé sommaire éprouvé et la liasse assemblée sur ces trois sorties ; puis le bout en bout sur les sept restantes ; puis la copie au projet dédié et le zip ; puis le lot des cas déposés. **Ensuite seulement**, d'ici à l'exercice suivant : digestion article par article, appariement doctrine contre texte, lieu d'arrivée dans le texte en discussion, extracteur rejouable. *La dépendance qui commande : le lieu d'arrivée et l'ingestion de l'exercice suivant dépendent de la digestion, qui dépend du socle, qui existe.*

**La priorité est nommée** : que la machine tienne, en un à deux jours, l'item individuel — une mesure, un amendement. La découpe complète du corpus en mesures portables vient après.

*Écarté* : commencer par les cas déposés ; commencer par la découpe complète du corpus.

*Relevé postérieur, 20260907* : **le fil des chouchous a déjà tourné** et son banc est au coffre — `methode/banc_chouchous.md`, **quinze mesures et seize énoncés**, en quatre lots. L'écart au dix en deux lots ne se tranche pas ici : soit le banc arrête la composition et A-374 se lit sur elle, soit les dix se prélèvent dans les quinze. **Il remonte à l'auteur.**

## 20260906 — « Gratuit » devient un contrôle, et quatre pièces sortent du projet

### A-365 — « Gratuit » ne se dit que pour être nié, et c'est mécanique

**Arbitré par l'auteur le 20260906**, relevé sur le site : *rien n'est gratuit,
tout est payé par quelqu'un, et c'est la base de la doctrine.* Le mot ne
s'emploie donc qu'à charge.

**En cherchant où l'inscrire, un manquement de treize jours est apparu.** A-53
posait le 20260824 que le lexique n'est pas une préférence de style mais une
règle vérifiable, et qu'il était « porté à `controle_sortie.py` ». **Il ne l'a
jamais été** — aucun des six termes n'y figure. Une règle qu'on déclare portée
sans la porter est pire qu'une règle non écrite : on la croit tenue.

**`appareil/controle_lexique.py`**, joué à `make controle`, sort `L1`. Deux
familles de termes. Les **proscrits simples** ont un substitut — baisse d'impôt,
prélèvements obligatoires, fonctionnaires, les actifs, il est évident que. Les
**proscrits de doctrine** n'en ont pas : leur emploi affirmatif contredit ce que
le corpus démontre, et « gratuit » est le premier.

**La dénonciation se reconnaît, elle ne se devine pas.** Un marqueur de fausseté
ou de négation dans la **même phrase** — « gratuité apparente », « faussement
gratuites », « rien n'est gratuit » — et l'emploi passe. La fenêtre est la
phrase : un démenti trois phrases plus loin ne rattrape pas une affirmation.
Éprouvé dans les deux sens avant d'être admis.

*Relevé au passage, et c'est rassurant* : les deux emplois du mot au
`REF_doctrine` sont déjà à charge — « études faussement gratuites », « la
gratuité enferme l'étudiant ». La doctrine tenait la règle avant qu'elle soit
écrite.

*Ce que le module ne fait pas* : il ne lit ni la méthode, ni l'appareil, ni les
références — ces documents parlent **du** mot. Et le reste du lexique d'A-53 y
est désormais, mais il n'a jamais été éprouvé sur un livrable réel : le seul
livrable au dépôt de ce fil sort à zéro.

### A-366 — Quatre pièces sorties se déclarent aux manquants, elles ne s'effacent pas

**Sorties par l'auteur, deux constatées et deux annoncées.**
`input/guide-public-du-budgetaire-2023.pdf` et `input/NL_cba-guidance.pdf` ont
disparu du coffre entre le 20260903 et le 20260904, constatés à l'ouverture du
fil d'éval. `Comparaison_internationale.pdf` — l'annexe des régimes de retraite
comparés — et `ResolutionD1a.png` sont retirés le 20260906, la première avec
l'intention déclarée de la refaire.

**Aucune n'a de digestion, et aucune ne se recompose** : un binaire ne se refait
pas par le modèle. Les effacer de la table les ferait disparaître des renvois
sans bruit. Elles vont donc au bloc `manquants`, avec leur motif et ce qui les
attend — c'est exactement ce à quoi ce bloc sert. Neuf manquants déclarés.

**La stratégie réseaux, elle, reste au projet** — l'auteur la croyait retirée,
elle y est encore. Sa part utile est digérée depuis le 20260824 : le lexique
(A-53, désormais joué), la date de parution du livre et son identification au
manuscrit par recoupement verbatim (A-55), trois angles morts (A-54). Ce qui
n'est digéré nulle part : l'architecture des comptes, le plan de lancement, les
cinq postures, les scripts. **Sa sortie ne coûte rien au corpus si elle
intervient après une digestion courte**, et perd le reste sinon.

## 20260904 — L'éval de la rédaction cible a tourné

*Fil de production, ouvert et clos le 20260904. Il n'a pas écrit la skill, il ne
l'a pas corrigée, et il n'a rédigé aucune colonne C de son cru. Numérotation à la
suite d'A-357.*

### A-358 — L'unité de la notation est le bloc de disposition, pas le couple

**Relevé en construisant l'échantillon, et c'est la trouvaille du fil.** Le
couple (alinéa, adresse) est la bonne unité pour le partage calibrage / épreuve —
il compte des occasions de modifier. **Il n'est pas l'unité de ce qu'on note.**

Le texte déposé écrit en arbre : « 6° Au I de l'article 1418 : » porte l'adresse,
et ce sont les `a)`, `b)`, `c)` qui suivent qui portent les opérations. Le couple
ne retient que le chapeau, parce que lui seul nomme l'article. **Noter la skill
sur le chapeau seul, c'est la noter sur une phrase qui ne prescrit rien** ; et
**écarter les chapeaux ferait un banc plus facile que le texte réel**, puisque ce
sont eux qui portent le cas dur du contrat — plusieurs opérations sur un même
article, rendues en une seule colonne C.

Le bloc est donc l'alinéa du couple plus, s'il ouvre par un deux-points, tous
ceux qui le suivent jusqu'au premier de niveau égal ou supérieur. Le niveau se
lit au marqueur de tête, jamais à une indentation que l'extracteur ne rend pas.
`appareil/blocs_disposition.py`. **Sur 42 cas tirés, 24 blocs font plus d'un
alinéa**, et le plus gros en fait quatorze.

### A-359 — Le banc s'échantillonne, et la règle s'écrit avant le tirage

**380 couples au lot d'épreuve ; les jouer tous demande un fil par poignée de cas
et plusieurs heures.** Une éval qu'on ne peut jouer qu'une fois ne mesure pas une
correction, et c'est tout l'objet du banc. On échantillonne donc, et la règle est
du code écrit avant que le premier couple soit regardé — même exigence qu'A-330
sur le partage lui-même : `appareil/echantillon_epreuve.py`.

**Stratifié proportionnel, pas régulier, aucune graine.** Une graine
pseudo-aléatoire est un choix caché que personne ne peut recompter ; un pas
régulier se recompte et couvre tout le texte, là où « les n premiers de chaque
strate » tasserait l'échantillon sur les premiers articles. Les couples **hors
strate** — ceux dont l'opération n'est pas à la liste fermée — sont dans
l'échantillon à leur poids : les écarter ferait, là encore, un banc plus facile
que le texte.

**42 cas tirés pour 40 voulus** — l'arrondi par strate se dit, il ne se rattrape
pas en piochant dans la plus grosse.

### A-360 — L'aveuglement se tient par des fils séparés, et il se contrôle sur les transcripts

**Trois rôles, trois fils, et aucun ne voit ce que voit l'autre.** Six fils ont
rédigé les énoncés d'entrée en lisant la disposition de l'administration ; sept
fils ont joué la skill en ne voyant que l'énoncé, l'adresse d'article et le
dépôt de droit ; la notation est mécanique. **Un fil qui a vu la disposition ne
peut plus juger ce qu'une skill en rend**, et la consigne ne suffit pas à le
garantir.

**Elle a donc été vérifiée, et non tenue pour acquise.** Les transcripts des sept
fils joueurs ont été relevés sur disque : **chacun ne porte les trois chemins
interdits qu'une fois, celle de son propre prompt.** Aucun n'a ouvert le terrain.

**La règle des énoncés est écrite** — `methode/regle_enonces_eval.md` —, elle
l'a été avant qu'un seul énoncé existe, et elle se joue :
`appareil/controle_enonces.py` refuse tout verbe de la grammaire modificative,
tout marqueur de subdivision, tout énoncé qui ne nomme pas son article. **Les 42
énoncés passent à zéro anomalie.** Trois cas sont déclarés `indicible` — l'effet
ne se dit pas sans nommer une subdivision : c'est une limite du banc, pas une
note, et ils sortent du compte.

### A-361 — Ce que l'éval mesure, avec ses réserves, et ce qu'elle ne mesure pas

**Population.** 42 tirés, 3 indicibles, **8 hors capacité** — le siège est hors
de l'extrait de droit, la skill le déclare et c'est le comportement attendu —,
**31 notés**. Dégradation `partiel` : les joueurs ont eu l'énoncé et le dépôt de
droit, pas la recherche publique que le proxy refuse, pas la doctrine non
dépliée. **Un taux mesuré ainsi est un plancher.**

| critère | strict | en équivalence |
|---|---|---|
| article visé | 94 % exact | **100 %** cité dans la disposition |
| opération | 32 % | **71 %** en nature |
| portée | 39 % | **non mesurable** |
| couverture des effets | — | 87 % complète, 95 % en moyenne |
| les trois ensemble | 26 % | **68 %** |

**Réapplication : 41 colonnes sur 41, à l'octet.** Elle a été **rejouée par le
noteur**, jamais crue sur la parole du fil qui a rendu la disposition.

**Trois réserves, et elles font partie du résultat.**

**Les deux écarts d'adresse ne sont pas des erreurs.** Sur une insertion
d'article, le socle relève l'article d'ancrage — « après l'article L. 314-12 » —
et la skill nomme l'article créé — « L. 314-12-1 ». Les deux sont justes, et la
disposition écrite porte les deux. Le critère qui lit ce que la skill a **écrit**
plutôt que ce qu'elle a **déclaré** sort à 100 %.

**La portée n'est pas mesurable en l'état, et le taux de 39 % note le
détecteur.** `partage_calibrage.cible` lit la cible en tête de phrase — « Le
second alinéa … est supprimé » — et non en complément circonstanciel — « Au
deuxième alinéa, les mots : « X » sont remplacés par … », qui est la forme la
plus courante du texte réel. **71 % des portées relevées sortent `indéterminé`,
des deux côtés.** Le rendre mesurable est un travail d'appareil ; il précède
toute conclusion sur la portée, et il est porté au fil suivant.

**La réapplication à 100 % ne dit rien de la justesse d'un C.** Elle dit que
chaque disposition écrit bien le C que son auteur a voulu. Sur l'article
L. 314-24 du code des impositions sur les biens et services, l'administration
réécrit l'article entier ; la skill retranche des alinéas, et sa réapplication
passe. **La porte est cohérente et elle est aveugle**, exactement comme le
contrat l'annonçait — et c'est maintenant démontré, chiffres en main, plutôt
qu'affirmé.

*Ce que l'éval dit à corriger, et rien d'autre* : la couverture d'un article
travaillé en plusieurs endroits — quatre cas sous-couvrent, l'un massivement,
trois opérations rendues sur huit —, et le choix entre réécrire et retrancher.
Les 135 doutes déclarés sur 31 cas, aucun cas n'en étant dépourvu, sont la sortie
la plus solide de l'étape et il ne faut rien y casser.

### A-362 — La table d'équivalence légistique est proposée, et elle revient à l'auteur

**L'écart entre 32 % et 71 % n'est presque pas un écart d'effet.** Trois familles,
mesurées : l'administration groupe — « les articles X et Y sont abrogés » — là où
la skill écrit deux phrases ; elle *supprime* une subdivision là où la skill
l'*abroge* ; elle *complète* un article là où la skill *insère* après le dernier
alinéa. Dans les trois cas, le droit écrit est le même.

**Neutraliser ces familles est un jugement de légistique, donc un jugement de
fond.** Ce fil ne le rend pas. La table vit dans
`appareil/noter_eval_disposition.py`, déclarée `proposée et non validée`, et
**les deux taux se publient** — le strict, qui ne l'emploie pas, et celui en
équivalence, qui l'emploie. Aucun ne remplace l'autre tant que l'auteur n'a pas
tranché.

### A-364 — La carte levait depuis deux jours, et personne ne pouvait le voir

**Constaté à la clôture, en la régénérant.** `appareil/generer_carte.py` pointait
encore `methode/ETAT_DU_CHANTIER.md` et `sources/gabarit_expose_sommaire.md` —
deux chemins renommés les 20260902 et 20260901. Le générateur lève un `KeyError`
sur le premier des deux, donc **la carte n'a pas pu être refaite depuis ce
renommage**, et celle que le coffre portait était en retard sur l'index sans que
rien ne le dise.

**Ce que l'incident enseigne, et qui vaut au-delà de la carte.** Un renvoi mort
dans un générateur ne se voit qu'au rejeu. `controle_index` compte les chemins
de l'index ; il ne joue pas les générateurs, donc il ne voit pas leurs renvois.
Un artefact du coffre qu'aucun fil ne régénère peut vieillir indéfiniment.
**A-19 fait de la carte la première chose que lit un fil neuf** : elle mentait
depuis deux jours.

*Réparé, et la carte est reversée* — 11 familles, 211 artefacts classés, 5
renvois morts déclarés. *Non réparé, et inscrit* : rien ne contrôle qu'un
générateur du coffre tourne encore. Le fil qui voudra fermer ce trou jouera tous
les générateurs à vide et comptera ceux qui lèvent.

### A-363 — L'atelier d'une éval n'a pas de place au coffre, et il se range à part

**Quinze pièces sortaient à `I2` : le terrain, l'échantillon, les six lots
d'énoncés et les sept lots de réponses.** Les déclarer une à une aurait chargé
l'index de quinze entrées volatiles ; ne pas les déclarer aurait laissé une
anomalie permanente.

**Elles vont dans `eval/`, ignoré comme `coffre/`, `droit/` et `plf/`.** Ce qui
se verse tient en trois pièces à `livrables/eval_disposition/` : les énoncés,
qui ne se régénèrent pas — des fils les ont écrits —, le **relevé condensé** de
ce que la skill a rendu, et la notation.

**Les colonnes A et C ne se versent pas.** Elles pèsent un demi-mégaoctet ; A est
du verbatim régénérable depuis le dépôt de droit, C se refait en rejouant l'éval.
Le relevé garde ce qui ne se refait pas : l'adresse visée, la forme littérale et
les doutes.

## 20260904 — Le registre ne repassait plus au coffre, et la première libération est faite

### A-357 — `positions.json` sort du coffre, l'auteur l'a tranché, et la place est mesurée

**Décision de l'auteur, prise le 20260904 sur la preuve d'A-356.** Le
référentiel des positions ne se verse plus. Il reste un artefact du dépôt,
produit par `construire_positions.py`, et l'index le porte à `coffre: false`.

**La sortie a demandé un ordre précis, parce que l'archive ne pouvait pas se
remplacer.** Replier l'archive sans les positions donne 1 631 154 o, mais son
versement est contrôlé sur le total **avant** retrait de l'ancienne (A-355) :
il aurait été refusé. L'ordre tenu est donc **déplier, replier, vérifier,
supprimer, verser** — la nouvelle archive a été dépliée dans un répertoire
témoin et ses 70 fichiers comparés **à l'octet** à ceux du dépôt, zéro
divergence, avant que `technique/coffre.txt` ne soit supprimé du projet.

**Ce que l'opération a rendu, mesuré à `project_info` avant et après** : la
jauge passe de **1 919 586 à 1 830 475** sur 2 000 000. **89 111 jetons
rendus**, pour une marge qui passe de 80 414 à **169 525**. Le gain dépasse le
poids du seul référentiel : l'archive s'écrit plus courte à plusieurs endroits.

**Les empreintes sont relevées au même geste** — 144 empreintes, celle de
`positions.json` retirée comme périmée et plus déclarée à l'index. Deux
artefacts restent sans empreinte, `methode/passation_site.md` et
`methode/prompt_eval_disposition_cible.md` : ils ne sont pas au dépôt de ce fil,
et leur empreinte se relèvera au premier fil qui les déplie.

*Ce que la sortie ne règle pas* : `notes_manuscrit.json` et les quatre dérivés
HTML restent des candidats non prouvés, donc non proposés. Et le retour de
`positions.json` au coffre est désormais interdit sans arbitrage : c'est une
décision de l'auteur, pas un effet de bord d'un `make coffre`.

### A-356 — `positions.json` est prouvé redondant au coffre, et la preuve est à l'octet

**A-346 exigeait la preuve avant le retrait, et la voici pour un des trois
candidats.** `referentiels/positions.json`, 242 572 o dans l'archive technique,
a été régénéré par la règle du `Makefile` — `construire_positions.py` sur le
seul `REF_doctrine`, avec `justifications.py` et `apports.py`, tous au coffre —
et le fichier obtenu est **identique à l'octet** à celui que le coffre porte :
`b159cb9ee7462691915b2656d4bf147c25775abb4130f8b88a73087da8cdbe4e`, 242 572 o,
sur les deux.

**Ce que le retrait rendrait, mesuré au rapport du versement** : de l'ordre de
60 000 jetons, à comparer aux ~80 000 de marge. C'est la seule des trois pistes
d'A-346 dont la preuve est faite ce jour.

*Les deux autres restent non prouvées, et ne se proposent donc pas.*
`notes_manuscrit.json` demande le manuscrit, que ce fil n'a pas déplié ; les
quatre dérivés HTML demandent leurs sources, non dépliées elles non plus.
**Aucun retrait ne se fait sur une identité affirmée.**

**Le retrait lui-même n'est pas tranché ici** : il touche ce que le corpus
porte, et A-346 le réserve à l'auteur.

### A-355 — La scission du registre est de la tambouille, et elle se mesure avant de se faire

**Le refus est la mesure.** `methode/arbitrages.md`, 344 903 o, a été refusé au
versement : ~86 226 jetons demandés, ~80 414 de marge. Le registre du chantier
ne pouvait donc plus revenir au coffre — et la procédure de clôture, qui exige
une entrée par décision, était mécaniquement infaisable.

**Ce que le refus prouve en plus.** A-312 posait qu'un versement n'est pas
crédité de la place que l'ancienne pièce libère ; on ne l'avait vu que sur un
versement neuf. Ici la pièce **remplace la sienne, à l'identique de rôle**, et
le contrôle se fait quand même sur le total avant retrait. La règle vaut donc
aussi pour les remplacements, ce qui est le cas qui compte : tout document du
coffre qui grossit finit par ne plus pouvoir se réécrire.

**La coupe est au 20260901**, et elle est de forme, pas de fond.
`methode/arbitrages.md` porte le courant — du 20260901 à aujourd'hui, 101 341 o
— et `methode/arbitrages_archive.md` l'antérieur, 244 311 o. Les corps
recomposés sont **identiques à l'octet** à ce que le registre portait avant la
coupe, vérifié avant versement. Le bloc des questions ouvertes reste au registre
courant : une question ouverte qui part à l'archive est une question perdue.

*Ce que la scission ne fait pas, et il faut l'écrire* : **elle ne rend pas un
jeton.** Les deux moitiés pèsent ce que pesait l'entier. Elle rétablit la
faisabilité de l'écriture, pas la marge. La saturation reste entière, et elle
est portée aux questions ouvertes.

## 20260904 — Ouverture du fil d'éval : la dette d'index se solde, et l'empreinte du prompt de fil est périmée

*Fil de production, ouvert le 20260904 après le fil du site. Numérotation à la suite d'A-351.*

### A-352 — Le R1 de `prompt_fil_courant.md` vient de l'empreinte, pas du fichier, et il se dit ainsi

**Mesuré à `make restauration`, non estimé.** `methode/prompt_fil_courant.md`
restauré fait 12 408 o, 246 lignes, `32d284ff08a4566c` ; l'empreinte de
référence attend 27 900 o, 522 lignes, `b7fdbc5f23b36eec`. C'est le seul R1 du
relevé ; R3, R4 et R5 sont à zéro.

**Le fichier n'est pas un faux, et la preuve est mécanique.** Les octets viennent
du transcript de la lecture du coffre, par `restaurer.py`, et le relevé ne voit
qu'**une seule version distincte** de ce chemin — `0 document(s) lu(s) en
plusieurs états`. Le coffre porte donc bien ces 12 408 octets. Ce qui a vieilli,
c'est `methode/empreintes.json` : le fil du 20260904 a versé un prompt de fil
neuf et **n'a pas joué `make coffre`**, qui est ce qui relève les empreintes.

**La règle « on s'arrête sur un R1 » n'est pas suspendue pour autant : elle est
appliquée à ce qu'elle vise.** Elle interdit d'employer une pièce divergente.
Ici la pièce est conforme au coffre et la divergence est au registre. Ce fil
continue, et il l'écrit plutôt que de le laisser passer en silence.

*Ce que cela coûte, et qui le paiera* : l'empreinte reste fausse tant que le
coffre n'est pas replié. **Le premier fil qui joue `make coffre` la remet
d'aplomb**, et il n'y a rien à corriger avant. Trois autres pièces versées le
20260904 sont dans le même cas — `methode/prompt_eval_disposition_cible.md`,
`appareil/reappliquer.py`, `appareil/cas_disposition.py` — et elles n'ont, elles,
aucune empreinte du tout.

### A-353 — Les entrées d'index dues sont portées, et il y en avait une quatrième

**Le prompt du fil en déclarait trois** (§7) : le prompt d'éval et les deux
modules de la réapplication. **Le relevé en trouve une quatrième**, née du fil du
site le même jour et que personne n'avait déclarée : `methode/passation_site.md`.
Elle était au coffre et invisible à l'index, exactement le cas qu'`I6` compte.

Les quatre sont portées à `appareil/generer_index.py` — la table curée, jamais
l'arborescence — et leur famille à `appareil/generer_carte.py`. `I2` et `I5`
retombent à zéro. Les deux modules sont déclarés **hors archive**, à leur propre
chemin : c'est où ils se lisent aujourd'hui, et le premier fil qui replie le
coffre les y ramène en retirant leur entrée de `COFFRE_HORS_ARCHIVE`.

*Ce que le relevé ne règle pas* : `exporter_site.py` et
`referentiels/donnees_site.json`, que la passation du site décrit comme la
nouvelle couture du rendu, **ne sont ni au coffre ni au dépôt**. Le
`generer_site.py` que porte l'archive est celui d'avant la refonte. Ce n'est pas
une entrée d'index qui manque, c'est du code, et cela s'inscrit sans se combler
ici.

### A-354 — Cinq pièces jointes digérées sont sorties, deux documents du coffre ont disparu, et l'index ne le disait pas

**Confrontation mécanique de l'index aux pièces jointes et aux documents du
projet, faite à l'ouverture parce qu'aucun script ne sait la faire.**

**Cinq sources que l'index déclare pièces jointes n'y sont plus** :
`Expose_des_motifs_redaction_GL.docx`, la note n° 1 de Fondapol sur la justice
fiscale, `dgfip_stat_32_2025.pdf`, l'étude IFRAP sur la liste des impôts et
taxes, et l'étude Fondapol sur la taxe Zucman. **Leur sortie est régulière** :
chacune a sa digestion au coffre — `reference/gabarit_expose_sommaire.md`,
`justice_fiscale_1789_fondapol.md`, `sourcage_ir_dgfip.md`,
`nomenclature_prelevements_ifrap.md`, `imposition_du_capital_fondapol.md` — et
R5 veut qu'une digestion chasse son original. Ce qui n'était pas régulier, c'est
que l'index les porte encore comme disponibles.

**Deux documents que l'index déclare au coffre n'y sont plus** :
`input/NL_cba-guidance.pdf` et `input/guide-public-du-budgetaire-2023.pdf`. Tous
deux sont `restaurable: false` — un binaire ne se recompose pas par le modèle.
**Ils sont perdus pour l'atelier tant que l'auteur ne les rejoint pas**, et cela
lui revient : c'est de l'input.

*Ce que ce fil ne fait pas.* Il n'invente pas de champ « sortie » à l'index pour
les cinq, et il ne retire aucune ligne : une source sortie après digestion reste
la source que la digestion cite, et son entrée est ce qui fait résoudre le
renvoi. Le constat s'inscrit, la table ne bouge pas.

## 20260903 — Deux rapports tiers sortent du projet, et la dette de la loi de financement se ferme

### A-350 — Le retrait des deux rapports tiers finance le socle de la loi de financement, et A-346 se ferme le jour de son écriture

**Décision de l'auteur, prise à la clôture du fil de la digestion.** Les deux
rapports tiers ont quitté les pièces jointes du projet :
`RAPPORTLemodelesocialfrancaisGenerationLibreFevrier2025.pdf` — en réalité le
rapport **AIRE**, « Le modèle social français contre les couples », février 2025
— et `201701LIBERunepropositionrealiste_generationlibre.pdf`, **Génération
Libre, LIBER volume II**, janvier 2017.

**Mesuré à `project_info`, dans son unité** : la jauge passe de **1 971 239 à
1 799 049** sur 2 000 000. **172 190 jetons rendus**, pour une marge de 200 951.
La part irréproductible du socle de la loi de financement demandait environ
104 000 : elle rentrait, et elle est versée —
`referentiels/redaction_plfss.json`, 351 968 octets, 55 articles, 1 070 alinéas,
340 adresses.

**A-346 est donc close le jour où elle a été écrite**, et les trois candidats à
la libération qu'elle nommait — les dérivés HTML régénérables, `positions.json`,
`notes_manuscrit.json` — **ne sont pas touchés**. Ils restent des candidats,
instruits et non tranchés, pour la prochaine fois que la jauge mordra.

**A-223 est tenue de bout en bout** : la loi de finances est passée d'abord, la
loi de financement ensuite, et l'ordre ne s'est pas rediscuté sous la contrainte.

*Ce que ce versement ne règle pas, et qui appartient au fil suivant* : le banc de
la rédaction reste celui de la loi de finances seule (A-347). La part versée du
socle de financement le rend désormais **partageable**, mais un second banc est
une décision de fil, pas une conséquence du versement.

### A-351 — Une pièce sortie n'est pas une pièce digérée, et le registre le dit dans les deux sens

**Relevé au même geste.** Le retrait libère la jauge ; il ne fait pas entrer la
matière. Les deux rapports gardent leur verdict du 20260902 — **digestion due**,
inchangé —, et ils ne sont plus au projet : ils **rentreront par pièce jointe du
fil qui les digérera** (A-234), comme le guide néerlandais et les classeurs.

**R5 se lit désormais par ses deux bouts.** Le registre des digestions posait
qu'« une digestion chasse son original » : l'original sort quand la digestion
entre. Ici l'ordre est inverse — l'original sort d'abord, et la digestion lui
doit son retour. **La règle tient dans les deux sens, à une condition : que la
référence exacte de la pièce sortie soit écrite avant qu'elle sorte, et qu'elle
ne s'invente pas.** Les deux références sont portées à
`reference/digestions_attendues.md`, avec l'erreur de nom du premier fichier,
relevée sur pièce le 20260902 et qui aurait fait chercher un rapport de
Génération Libre là où il y a un rapport AIRE.

*Ce que le retrait ne casse pas, vérifié* : aucune phrase du corpus ne s'appuie
aujourd'hui sur l'une ou l'autre. Les deux étaient aux verdicts « après
vendredi » et « plus tard ». Sur LIBER, la seule citation du corpus passe par la
note 122 du manuscrit — les travaux de Marc de Basquiat —, pas par le rapport ;
et ses chiffres, de base 2016, se réactualisent avant tout emploi.

## 20260903 — La digestion du texte déposé, le socle versé, le banc partagé

*Fil de production, ouvert et clos le 20260903 après le fil de structuration. Il n'a écrit aucune skill, n'a rédigé aucune colonne C, et n'a pas pris connaissance du lot d'épreuve. Numérotation à la suite d'A-342.*

### A-343 — Le générateur perdu se réécrit sur sa propre sortie, et la preuve est à l'octet

**Fait, non affirmé.** `appareil/articles_ouverts_plf.py` était déclaré aux
manquants depuis le 20260902 : invoqué par le `Makefile`, absent du dépôt, du
coffre et de l'archive du sas. Les deux tables plates, elles, étaient versées.

**C'est cette asymétrie qui rendait la réécriture sûre.** Une sortie versée est
une spécification exécutable : on écrit le module, on le joue, on compare à
l'octet. Il n'y a rien à croire.

Les deux tables ressortent **identiques à l'octet** —
`2863d12f…f2c9e9ec`, 23 061 o, 396 lignes pour la loi de finances ;
`8aa17c75…074f15c8b`, 11 634 o, 218 lignes pour la loi de financement — et le
rejeu passe par la règle du `Makefile`, non par un appel à la main.

**Trois choses que la réécriture a dû retrouver et que rien ne documentait.**
L'unité de la table n'est pas la référence du socle mais **le fragment
d'énumération** : le socle relève « L. 314-2, L. 314-3 et L. 314-4 » comme un
seul brut, la table en fait trois adresses. La virgule, le point-virgule et
« et » séparent ; **« à » ne sépare pas** — une fourchette reste une adresse et
se marque. Et `texte` à `None` au socle — la pièce modifie une adresse sans
nommer son texte — s'écrit `aucun texte nommé`, qui n'est pas l'`indéterminé` de
`vecteurs.py` : l'un dit que la pièce ne nomme rien, l'autre qu'on ne sait pas
rattacher ce qu'elle nomme.

*Ce que la réécriture ne fait pas* : la grammaire d'adresse n'est pas dupliquée.
`ref_norme.decouper_articles` est **appelé**, et la colonne
`article_selon_ref_norme` déclare l'écart au lieu de le corriger — 39
divergences au PLF, 0 au PLFSS, exactement ce que les tables versées portaient.

### A-344 — Le socle de la loi de finances ne tient pas à la jauge, et la clause de repli d'A-342 s'applique

**Mesuré au refus du versement, jamais estimé.** Le socle du texte déposé de la
loi de finances pèse **494 461 jetons** pour 1 977 841 octets — le rapport de
0,25 jeton par octet qu'A-312 avait relevé sur l'archive. La marge à
`project_info` était de **310 550**. L'écart n'est pas un ajustement : il
manquait 183 911 jetons, soit 59 % de la marge entière.

**Ni la sérialisation compacte, ni le retrait de l'exposé des motifs ne
suffisent** — 410 000 jetons pour la première, 355 000 pour les deux ensemble.
Aucune forme qui porte la rédaction complète des 82 articles ne tient.

**A-342 prévoit exactement ce cas, et il ne se subit pas** : *c'est sa part
irréproductible qui se verse, et jamais la part qu'une autre source sait
rendre.* `appareil/redaction_deposee.py` découpe cette part, et
`referentiels/redaction_plf.json` est versé — 848 687 octets, **251 270 jetons
mesurés**, 82 articles, 2 164 alinéas, 552 adresses.

*Ce qui reste un dérivé d'atelier* : le socle complet, régénérable depuis la
pièce jointe, et son empreinte est portée au document versé pour que le rejeu se
vérifie.

### A-345 — Le socle porte le même verbatim dans deux rendus, et on n'en verse qu'un

**Relevé en mesurant le socle champ par champ**, et c'est ce qui a rendu la coupe
possible. `redaction.lignes` porte 602 852 octets de sortie brute de
`pdftotext -layout` ; `redaction.alineas` porte 484 816 octets **du même
verbatim**, reflué par l'extracteur, une entrée par alinéa avec sa page. Verser
les deux coûte un demi-mégaoctet pour aucune information de plus.

**On garde `alineas`, et le choix se dit.** C'est la forme qu'une disposition
modificative adresse, et celle que la colonne A du trois colonnes consomme.
`hors_alinea` — états législatifs, plafonds d'emplois, tableau d'équilibre,
224 875 octets — est gardé à part : rien d'autre ne le porte.

**Ce que la coupe coûte, et il faut l'écrire.** La mise en page brute ne se
relit plus au coffre. Et `expose_des_motifs`, retiré comme étant de l'indice et
non de la norme (A-229), emporte avec lui le rejeu depuis le coffre du quatrième
relevé de la lecture en creux — montants annoncés à l'exposé sans contrepartie à
la rédaction. Il se rejoue depuis la pièce jointe, comme aujourd'hui.

*La liste des champs retirés est fermée et portée au document versé.* Une coupe
nouvelle est un arbitrage, pas une optimisation.

### A-346 — La loi de financement n'est pas versée, et la dette est chiffrée

**A-223 tient : la loi de finances passe d'abord, et elle est passée.** La jauge
après son versement est de **1 940 720 sur 2 000 000**, soit **59 280 jetons de
marge**. La part irréproductible de la loi de financement fait 351 968 octets,
soit **environ 104 000 jetons** au rapport mesuré du versement précédent — 0,296
jeton par octet. **Elle ne rentre pas, et rien de ce qui porte sa rédaction ne
rentrerait** : ses alinéas seuls pèsent 268 624 octets, déjà plus que la marge.

**Le coffre est à saturation, et ce n'est plus une contrainte de fil mais un
arbitrage à rendre.** Trois candidats se mesurent, aucun ne se tranche ici parce
que tous touchent ce que le corpus porte :

- **les dérivés HTML régénérables depuis le coffre seul** — `galerie_fiches`,
  `extrait_gagnants_perdants`, `carte_du_projet`, `etat_machine` : par A-71 ils
  n'ont rien à y faire, mais leur identité au rejeu se prouve, elle ne
  s'affirme pas, et ce fil n'a pas déplié leurs sources ;
- **`referentiels/positions.json`**, 242 572 octets dans l'archive, qui se
  régénère de `REF_doctrine` — même exigence de preuve ;
- **`referentiels/notes_manuscrit.json`**, 59 142 octets, dont l'identité au
  rejeu est déjà la preuve externe que le corpus tient sur le manuscrit.

*Ce que la dette n'est pas* : un oubli. Le socle de la loi de financement se
régénère de sa pièce jointe, comme avant ce fil — c'est la situation qu'A-342
condamne, et elle survit pour ce seul véhicule, avec son chiffre.

### A-347 — Le partage calibrage / épreuve est du code, et il est écrit avant le tirage

**A-330 exige que le partage se fixe avant que le fil de la skill s'ouvre, et par
un autre fil.** Une règle écrite en prose se contourne sans qu'on le voie ; la
règle est donc `appareil/partage_calibrage.py`, elle se rejoue, et elle a été
écrite **avant** qu'un seul couple soit regardé.

**La population** est celle de `referentiels/redaction_plf.json` — la part versée,
et non le socle : un banc qu'on ne peut pas rejouer depuis le coffre n'est pas un
banc. **384 couples (alinéa, adresse ouverte)**, ce qui n'est pas les 386
adresses de la table plate : l'unité n'est pas la même, et les deux comptes se
lisent avec leur unité.

**La règle, et ses quatre clauses.** Éligibilité : une opération et une seule,
une adresse et une seule — un alinéa composite est un cas d'épreuve. Strates :
`abrogation_article`, `abrogation_subdivision`,
`remplacement_membre_de_phrase` par A-329, puis **la plus peuplée des opérations
restantes, mesurée**. Tirage : le premier couple de chaque strate dans l'ordre
du texte — **aucune graine pseudo-aléatoire**, une graine étant un choix caché
quand le premier de l'ordre du texte se recompte par quiconque. Strate vide :
elle sort vide et ne se remplace pas.

**Ce que la mesure a donné.** 239 couples éligibles sur 384 ; par strate,
100 remplacements, 49 insertions, 38 complètements, 29 abrogations d'article,
19 abrogations de subdivision, 6 rétablissements, 3 rédactions nouvelles, 1
création ; 139 couples hors strate, dont l'opération n'est pas à la liste fermée
et qui **se comptent sans se qualifier**. La quatrième strate est donc
`insertion`, mesurée et non choisie.

**Le lot de calibrage fait quatre couples** — art. 5 al. 2, art. 5 al. 9,
art. 2 al. 1, art. 3 al. 2 — **et le lot d'épreuve les 380 autres, scellés.** Ce
fil n'en a pas lu le contenu, et le banc ne les énumère pas : ils se recalculent.

### A-348 — Deux modules de plus que le corpus invoque n'existent nulle part, et le relevé est mécanique

**Trouvé en cherchant le premier.** Le relevé croise ce que le `Makefile` appelle
et ce que le dépôt porte — une commande, pas une lecture. Il sort trois modules,
dont un seul était déclaré.

- **`appareil/controle_socle_plf.py`**, appelé par `make controle` sur chacun des
  deux socles. Sa règle est gardée par un test de présence du socle : **`make
  controle` ne casse pas, il ne contrôle simplement rien sur les deux socles, et
  cela ne se voyait pas.** Les dix contrôles internes de `socle_plf_texte.py`
  tournent, eux, à chaque génération.
- **`appareil/portes_ouvertes.py`**, la jointure qui dit quelle mesure du corpus
  tombe sur un article que le texte déposé ouvre déjà (A-293). C'est le plus
  coûteux des trois, et le dépliage des cinq fourchettes attend d'elle sa
  consommation (A-333) : tant qu'il manque, **les douze adresses intérieures des
  plages restent comptées fermées**.

*Ce que le relevé enseigne, au-delà des deux cas* : **un manquant qui ne casse
rien ne se déclare pas tout seul.** `articles_ouverts_plf.py` s'était déclaré
parce que sans lui une sortie manquait ; ces deux-là se taisaient parce que leur
règle est gardée. Le croisement du `Makefile` avec le dépôt est désormais le
geste qui les trouve, et il tient en une commande.

### A-349 — Un référentiel plus gros que l'archive ne s'y replie pas, et `coffre.py` lisait le rang au lieu de l'index

**Sorti au premier `make coffre` du fil, et l'écart était visible : l'archive
passait de 1 825 441 à 2 719 630 octets.** `referentiels/redaction_plf.json` est
de rang `referentiel`, donc `COFFRE_ARCHIVES` l'adressait à l'archive — alors
qu'il venait d'être versé comme document.

**Deux corrections, et la seconde est la vraie.** L'index reçoit une table
d'exception, `COFFRE_HORS_ARCHIVE`, qui n'est pas de commodité : une pièce de
848 687 octets repliée dans l'archive en ferait une pièce d'un million et demi de
jetons, et A-312 interdit alors de la réécrire — on ne fait pas dépendre
l'appareil entier d'une suppression réussie. Et **`coffre.py` cesse de déduire
du rang ce que l'index déclare** : il plie ce dont le `chemin_coffre` est
l'archive, le rang ne bornant plus que le groupe.

*A-286 avait déjà posé cette règle le 20260902* — « `coffre.py` plie ce que
l'index adresse à l'archive plutôt que ce que le rang y adresserait ». Elle
était écrite au journal et **pas dans le code** : la sélection se faisait toujours
sur le seul rang, et cela n'avait pas mordu parce qu'aucun artefact ne
contredisait encore le rang. **Une règle qui n'est pas dans le code n'est pas une
règle**, elle est une intention qui attend son contre-exemple.

L'archive revient à 1 871 374 octets, 71 fichiers, dépliage prouvé 71 sur 71.

## 20260903 — Absorption du sas de la lecture en creux

*Absorbé le 20260903. Les entrées sont celles du fil de la lecture en creux, écrites le 20260902 et datées comme telles dans leur titre ; elles sont portées ici par découpe de sa passation, numérotées à l'insertion. Le texte n'est pas recopié : il est découpé du document que le coffre porte.*

### A-331 — Les parties et titres du PLF se relevaient, et la cause n'était pas celle qu'on présumait — 20260902

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

### A-332 — Le critère « chaque article porte sa division » ne tient pas, et l'article liminaire dit pourquoi — 20260902

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

### A-333 — Les cinq fourchettes se déplient au dépôt de droit, et douze adresses passaient pour fermées à tort — 20260902

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

### A-334 — Trois articles de fourchette sur vingt-deux portent une abrogation déjà votée, et une plage entière est dans ce cas — 20260902

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

### A-335 — La lecture en creux rend cinq relevés, et la troisième colonne du trois colonnes n'en est pas un — 20260902

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

### A-336 — La grille du domaine de la loi de financement rend trente et une portes, et l'axe de transparence en a trois — 20260902

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

### A-337 — Cloner le dépôt de droit dans l'atelier faisait sortir I2, et le corpus prescrivait ce geste — 20260902

**Relevé.** `reference/depot_droit.md` écrit `git clone … droit`, dans
l'atelier. Le faire fait sortir **`I2` à 15** : `droit/` n'était ni au
`.gitignore` ni aux `IGNORES` de `controle_index.py`. **La procédure que le
corpus prescrit cassait un contrôle que le corpus tient.**

Corrigé aux deux endroits. Le fil a par ailleurs travaillé avec le dépôt cloné
hors atelier, et la variable `DROIT` du `Makefile` accepte les deux formes.

### A-338 — `I1` n'est pas un invariant du corpus, et son épinglage à 28 ne se reproduit pas — 20260902

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

## 20260903 — La rédaction cible, l'épreuve sur pièce, la dette purgée

*Le fil de structuration ouvert la veille s'est poursuivi. La date d'une entrée est celle où la décision est prise, jamais celle où le fil s'est ouvert : ce qui suit est du 20260903, et le bloc du 20260902 reprend plus bas à `A-313`.*

### A-328 — Les colonnes A et « disposition » existent déjà, sur 386 couples — je réclamais une pièce déjà digérée

**Relevé par l'auteur, et c'est une faute de ma part.** J'ai demandé le texte du
projet de loi de finances en pièce jointe « pour tester le contrôle de
réapplication ». **Il est digéré, deux fois**, et le sas de la lecture en creux
le dit noir sur blanc.

Ce que le socle du texte porte, mesuré par le fil qui l'a écrit :

| | adresses | texte en vigueur relevé **en regard de la disposition** |
|---|---|---|
| projet de loi de finances | 406 | **277** |
| projet de loi de financement | 216 | **109** |

**C'est la colonne A et la colonne « disposition » du trois colonnes, déjà
produites à l'octet** — l'une au dépôt de droit, l'autre au socle. Et le même
document déclare le trou avec exactitude : *« La troisième colonne n'est pas
rendue, et c'est une limite déclarée. Le texte résultant suppose d'appliquer la
modification : c'est un acte de légistique. Le fabriquer par script serait
inventer du droit. »*

**Le trou déclaré là est exactement l'étape de rédaction.** Et les 386 couples
sont le banc d'épreuve du contrôle de réapplication : des dispositions
modificatives écrites par l'administration, avec leur texte de départ. **Rien
n'est à charger.**

*Ce que la faute enseigne, et elle est déjà écrite au garde-fou* : ne pas
qualifier un document non ouvert. J'avais listé quatorze documents du coffre
« non déclarés à l'index » et refusé de les qualifier — ce qui était juste — puis
j'ai conclu sur ce que le corpus portait **sans les ouvrir**, ce qui ne l'était
pas. **Un document qu'on ne classe pas, on peut toujours l'ouvrir avant de dire
qu'il manque.**

### A-329 — Le lot d'un tiers n'est pas notre profil d'usage — nous supprimons, il ajoute

**Relevé par l'auteur** : *nous, on aura moins de créations d'articles nouveaux ;
notre esprit est de simplifier, pas d'ajouter. Tout ce qui peut être supprimé est
très valorisable pour nous.*

*Corrige A-324 sur sa portée, pas sur son compte.* Les 40 % de mesures sans
siège codifié sont **le profil du contre-budget d'un tiers**, mesuré sur son lot.
Ce n'est pas le nôtre. **Le lot mesure la forme, il ne prédit pas la
fréquence** — et un taux relevé sur lui ne se transpose pas à notre usage.

**Notre opération dominante est l'abrogation**, et c'est une bonne nouvelle pour
la machine : c'est l'opération où **tous les contrôles mordent**. A existe et se
relève à l'octet ; le balayage segment par segment a quelque chose à balayer ; la
forme modificative se dérive et se prouve par réapplication. **La création est
exactement l'inverse** — A est vide, le balayage n'a rien à vérifier, et le seul
contrôle disponible est l'écart au modèle.

*Conséquence sur les trois exemples travaillés* : deux abrogations — l'article
entier, puis une subdivision — et un remplacement de membre de phrase. **La
création descend au quatrième rang** : elle reste dans la skill, elle ne
commande plus le calibrage.

*Ce qui reste vrai d'A-324* : quand A est vide, l'analogie est le seul mode
disponible, et l'écart au modèle est le seul contrôle. Ce n'est plus le second
mode par fréquence, cela reste le second mode par nature.

### A-340 — La rédaction est d'abord un exercice de rigueur, et trois pièces la règlent

**Relevé par l'auteur le 20260903** : *les modèles sont intéressants pour se
jauger, mais c'est vraiment un exercice de réflexion et de rigueur avant tout ;
le guide du SGG est intéressant pour ça, ainsi que la Constitution, qui dit le
domaine de la loi, et les précédents.*

*Cela déclasse les modèles et classe trois pièces.* Un lot de référence dit où
l'on en est ; il ne dit pas comment écrire. Ce qui règle la rédaction :

- **le guide de légistique**, par sa digestion au corpus — la méthode, les
  formules, les refus ;
- **la Constitution**, qui dit **le domaine de la loi** : ce qui relève du
  législateur et ce qui relève du pouvoir réglementaire ;
- **les précédents**, qui donnent le squelette quand il n'y a pas d'article de
  départ.

**Ce que la Constitution ajoute à l'étape, et qui manquait au contrat.** La
colonne C ne doit rien écrire qui relève du décret. Un paramètre d'application,
un seuil de gestion, une modalité de contrôle **se renvoient au pouvoir
réglementaire** au lieu de s'écrire dans l'article. **C'est un refus, pas un
conseil** : une disposition de niveau réglementaire glissée dans un article de
loi est un vice, et il se voit.

*Conséquence sur la sortie* : la skill déclare, pour chaque fragment neuf de C,
qu'il est de niveau législatif — et renvoie au décret ce qui ne l'est pas.
### A-342 — Un dérivé dont la source n'est pas au coffre n'est pas un dérivé : il se verse

**Relevé par l'auteur le 20260903, et c'est une faute de règle, pas d'exécution.**
Le texte financier a été digéré **deux fois** — la seconde parce que la première
n'avait pas gardé ce qu'il fallait —, et son contenu n'est toujours pas au
coffre. Un troisième passage était sur le point d'être demandé.

**La cause est une règle appliquée hors de son domaine.** A-71 dit qu'un dérivé
qui se régénère à l'identique ne se verse pas ; A-235 ajoute que le texte déposé
lui-même ne se verse pas, étant public et retéléchargeable. Les deux sont justes
**et supposent que la source du dérivé soit atteignable depuis le coffre**. Ici
elle ne l'est pas : le socle du texte se régénère depuis un fichier qui n'est ni
au coffre, ni au dépôt, et qui rentre par pièce jointe. **La chaîne de
régénération sort du coffre, donc elle est rompue.**

**Règle, et elle vaut au-delà du cas** : *un dérivé dont la source n'est pas au
coffre se verse.* « Régénérable » se lit **depuis le coffre seul** — c'est ce que
prouve la restauration à blanc, et rien d'autre ne compte. Un dérivé dont la
reconstruction demande un geste de l'auteur est, pour le coffre, une pièce que
personne ne sait refaire.

**Ce qui en découle immédiatement.** Le socle du texte déposé — la rédaction
exacte des articles, leurs adresses, et le texte en vigueur relevé en regard de
la disposition — **se verse dès qu'il est produit**, et les deux tables plates
restent versées à côté de lui. S'il ne tient pas dans la jauge en entier, c'est
sa part irréproductible qui se verse — la rédaction exacte —, jamais la part que
le dépôt de droit sait rendre.

*Ce que la faute a coûté, mesuré* : deux digestions du même document, et une
troisième évitée de justesse. *Ce qu'elle enseigne* : **une règle d'économie
n'est valable que dans le périmètre où elle a été écrite**, et celle-ci avait
été écrite pour des dérivés dont la source est au coffre.

### A-341 — Les douze invisibles sont ouvertes et déclarées, `I6` tombe à zéro

**Ouvertes une par une avant d'être classées** — A-24, et cette fois dans le bon
ordre. Douze pièces que le coffre portait et que l'index ne déclarait pas.

| pièce | ce que c'est | rang · famille |
|---|---|---|
| `methode/sas.md` | procédure du sas et registre vivant de ce qui attend absorption | méthode |
| `reference/digestions_attendues.md` | registre des références externes non encore digérées | méthode |
| `reference/imposition_du_capital_fondapol.md` | digestion d'une note externe, R5 | références externes |
| `reference/justice_fiscale_1789_fondapol.md` | digestion d'une note externe, R5 | références externes |
| `reference/nomenclature_prelevements_ifrap.md` | digestion, volet narratif, table séparée | références externes |
| `reference/sourcage_ir_dgfip.md` | sourçage d'une note statistique, tableau par page | références externes |
| `referentiels/prelevements_ifrap.tsv` | la table primitive de la digestion précédente | source · références externes |
| `referentiels/articles_ouverts_plf.tsv` | table plate du texte déposé, 386 adresses | dérivé · grilles |
| `referentiels/articles_ouverts_plfss.tsv` | idem, 208 adresses | dérivé · grilles |
| `livrables/eval_gl/reponses_*.json` | les deux jeux de réponses d'éval versés | dérivé · bac à sable |
| `input/accroche…20260901.md` | note de l'auteur | source · références internes |

**Deux points de rangement tranchés au passage.** Les deux **tables plates du
texte déposé** se versent comme documents et non dans l'archive : elles portent
l'empreinte de leur pièce source, donc leur rejeu se vérifie, quand le socle qui
les produit ne se verse pas. Et les **sorties d'éval** se versent bien qu'elles
soient des dérivés : un rejeu ne redonnerait pas les mêmes réponses, un fil les a
écrites en aveugle — **ce n'est pas un dérivé au sens d'A-71**.

*Restauration vérifiée à l'octet sur les deux tables* : `2863d12f…`, 23 061 o, et
`8aa17c75…`, 11 634 o — exactement ce que la passation du sas déclarait.

**`I6` passe de treize à zéro.** Le contrôle a servi le jour où il est né.

### A-339 — L'invisibilité se compte : le contrôle `I6`

**Tranché par Claude au titre d'A-23**, sur relevé de l'auteur — *tu as bien fixé
ton erreur interne ? il y en a tout le temps.* Il a raison : une entrée de
registre qui dit « ouvrir avant de conclure » est une règle qu'on tient à l'œil,
et **une règle qu'on tient à l'œil se perd** (A-268).

**La cause n'était pas l'inattention, c'était un trou de l'appareil.** Quatorze
documents étaient au coffre et hors index ; `controle_index.py` ne pouvait pas
les voir, puisqu'il ne connaît que ce que l'index déclare. **Le corpus n'avait
aucun contrôle sur ce qu'il porte et qu'il ne déclare pas.**

`I6` le comble. `methode/inventaire_coffre.tsv` porte la liste des documents du
coffre, **relevée au transcript et jamais retapée** — même copie d'octets que la
restauration, appliquée à la liste au lieu du contenu. Le contrôle sort toute
pièce du coffre qu'aucun `chemin_coffre` ne réclame, et la compte en anomalie.

**Treize à la première exécution**, nommées. Ce sont exactement celles qui
m'avaient rendu aveugle.

*L'inventaire ne se verse pas* : c'est une photo de session, et le verser
figerait un état. Sans lui, `I6` le dit et ne bloque pas.

*Ce que la faute enseigne, au-delà du cas* : **un garde-fou qui dépend de la
mémoire n'est pas un garde-fou.** A-24 interdit de qualifier un document non
ouvert ; il ne disait rien de celui qu'on ne voit même pas. C'est désormais
compté.

### A-330 — On ne calibre pas sur ce dont on sera mesuré, et le partage se fixe avant

**Question de l'auteur** : *comment tu vas générer et calibrer la skill en la
générant ?* La réponse est une règle, et elle manquait.

**Calibrer n'est pas juger.** Regarder un modèle pour apprendre la **forme**
d'une disposition est nécessaire — on n'écrit pas la skill à l'aveugle. Mesurer
la skill sur ce même modèle ne prouve rien.

**Trois règles, et la troisième est celle qui tient.**

- Le fil qui écrit la skill **voit un lot de calibrage**, déclaré et petit.
- Le lot de calibrage **sort de la population d'épreuve**, comme un cas
  contaminé.
- **Le partage se fixe avant que le fil s'ouvre, et par un autre fil.** Celui qui
  choisit son lot de calibrage choisit ses cas faciles — c'est la même faute que
  d'écrire sa propre clé d'éval, et elle ne se voit pas après coup.

*Conséquence sur l'ordre des fils, et elle remplace le découpage annoncé* : le
banc d'épreuve de la rédaction n'est pas le lot d'un tiers, **c'est le texte
financier lui-même**, dont 386 couples portent déjà une disposition écrite par
l'administration en regard de son texte de départ. Le lot du tiers reste le
modèle de la **mesure** et de l'**exposé**, pas de la rédaction modificative.

### A-323 — La note logement social est une borne haute, pas la norme — et l'écart se mesure

**Relevé par l'auteur le 20260903** : *la note HLM est un modèle de rédaction
cible et de complication, pas la vérité et pas la norme ; on ne devra sans doute
pas aller aussi loin la plupart du temps.* **Il a raison, et l'écart est d'un
facteur huit.**

Mesuré sur le lot d'un contre-budget réel, dix-huit mesures qui portent une
adresse, contre les huit cibles de la note :

| | médiane par mesure | note logement social |
|---|---|---|
| articles visés | 2 | 8 |
| alinéas à lire | 36 | 171 |
| renvois internes | 8 | 126 |
| renvois entrants sûrs | 12 | — |

**Conséquence de conception, et elle allège le fil** : la grille des huit verbes
et des six fonctions est ce que la machine doit **pouvoir** atteindre, pas ce
qu'elle déroule à chaque mesure. Une mesure courante tient sur deux articles.
*Écarté* : faire de la note le gabarit de sortie — ce serait imposer un plan de
démantèlement à un amendement de taux.

### A-324 — Deux mesures sur cinq n'ont aucun siège codifié — la création n'est pas un repli

**Constaté sur le lot, et cela déplace le centre de gravité de l'étape.** Sur les
trente couples du contre-budget, **douze n'ont pas d'article à modifier** : huit
sièges non codifiés, un sans objet, un à trouver, deux au lot de financement.
**Quarante pour cent.**

Le « = » ne s'applique donc qu'à trois mesures sur cinq. Pour les autres, **A est
vide** : la mesure insère un article qui n'existe pas — clause de caducité,
obligation de rapport, dispositif neuf.

*Ce que cela corrige au 20260902* : j'avais rangé l'analogie en dernier, « et
seulement là où A est vide », comme un repli. **C'est le second mode de l'étape,
pas son exception**, et l'opération « créer un article » cesse d'être la sixième
par ordre de difficulté pour devenir la seconde par fréquence.

*Ce que cela ne change pas* : l'analogie transpose un **squelette** et jamais des
mots, et l'écart au modèle reste le contrôle. Sans article de départ, c'est le
seul contrôle disponible — raison de plus pour qu'il soit tenu.

### A-325 — Le régime des renvois tient, à condition que la règle de déduction le précède

**Mesuré, et c'est ce qui valide A-299.** La médiane des renvois entrants sûrs —
ceux dont le code est nommé, ou dont le citant est dans le même code — est de
**douze par mesure**. Douze lignes en fin d'exposé sommaire est un signalement.
Les 393 de la note logement social étaient un annuaire : c'est le cas extrême qui
donnait le faux ordre de grandeur.

**Mais le compte brut est faux d'un facteur cinq à trente**, et il l'est
d'autant plus que le numéro d'article est court. Mesuré, sur le corpus entier :

| cible | relevé brut | introduit par « article » | dont sûrs |
|---|---|---|---|
| `14` CGI | 1 216 | 186 | 36 |
| `L. 411-1` CCH | 124 | 114 | 13 |
| `279` CGI | 25 | 15 | 8 |
| `L. 302-5` CCH | 51 | 51 | 47 |

**La règle de déduction n'est pas un raffinement du relevé : sans elle, le relevé
est du bruit.** Une citation ne compte que si elle est introduite par « article »
ou « art. », et elle n'est sûre que si le code est nommé ou si le citant est dans
le même code. **Les `ambigu` se comptent et ne se listent pas.**

### A-326 — `coordination.py` a bien tourné ; c'est le versement qui manque

*Précise A-321, qui constatait son absence sans pouvoir dire si le travail avait
eu lieu.*

Un compte indépendant, écrit ici et sans voir l'outil, retrouve **neuf articles
applicables citant `L. 3262-1` du code du travail** — exactement le chiffre
publié par la passation, dont cinq hors du code du travail. **L'outil a existé et
il a compté juste.** Il a été écrit dans un atelier et jamais poussé au dépôt
public.

*Un écart reste ouvert, et il ne se tranche pas ici* : sur l'article `279` du code
général des impôts, la passation annonce **quatre** articles touchés ; le compte
indépendant en trouve **huit** sûrs. Soit la règle de l'outil est plus stricte,
soit la mienne est plus large. **À instruire quand l'outil sera au dépôt**, et non
à arbitrer de mémoire.

*Fait neuf trouvé au passage* : une **quatrième** cible du lot porte une
abrogation programmée — `1613 ter` du code général des impôts, au lot de
financement — que la liste des trois ne mentionnait pas. *Et deux adresses d'un
même amendement sont absentes du dépôt* : `1` et `1649-0 A` du code général des
impôts.

### A-327 — Coordination et transitoire : isolés et jugés sur pièce, développables au besoin

**Précisé par l'auteur le 20260903** : *les coordinations, c'est typiquement à
isoler et juger sur pièce, pareil pour le transitoire, mais on voudra pouvoir
développer au besoin — propositions de loi complètes.*

*Amende A-318*, qui posait « signalé, non rédigé » comme un régime unique. Il
devient le **régime par défaut**, et non le seul :

- **par défaut, l'amendement** : la coordination et le transitoire sont
  **isolés** — nommés, avec ce qu'ils doivent régler et le précédent qui les
  modèle — et jugés sur pièce. Ils ne se rédigent pas.
- **sur demande, la proposition de loi complète** : ils se développent. La skill
  doit en être capable, et le mode se demande explicitement.

**Ce que le régime par défaut protège reste vrai dans les deux cas** : le délai,
le prix de transfert et qui paie sont des décisions politiques. En mode
développé, la skill **rend une rédaction et nomme ces trois-là comme non
tranchés**, elle ne les choisit pas.

*Portée sur les mesures d'un texte financier* : elles sont souvent complexes,
additives et maximalistes. C'est ce qui rend la découpe en segments obligatoire
avant toute rédaction — non pour la beauté du découpage, mais parce qu'un
amendement qui ajoute trois dispositifs à un article ne se lit pas d'un bloc.

### A-321 — L'épreuve sur pièce a trouvé quatre choses, et elle a corrigé sa propre clé

**Non, l'architecture n'était pas prête.** Question de l'auteur — *tu penses
sérieusement que tu es prêt ?* — et la réponse se mesure au lieu de s'affirmer.
Le dépôt de droit a été cloné et les neuf cibles du plan juridique de la note sur
le logement social ont été passées au compteur. **88 334 articles applicables,
vingt codes.**

*Et la première mesure était fausse* : elle cherchait « L302-5 » quand le droit
écrit « L. 302-5 », et rendait zéro citation sur tous les articles en L. C'est
A-261 refaite — une clé fausse note faux — attrapée avant publication parce que
zéro sur un article aussi cité que le plancher SRU ne pouvait pas être vrai.
**Les chiffres ci-dessous sont ceux de la version corrigée.**

| cible | alinéas | renvois internes | renvois sortants | articles qui la citent | dont hors de son code |
|---|---|---|---|---|---|
| plancher SRU · `L. 302-5` CCH | 30 | 30 | 24 | 51 | 13 |
| plus-values terrains · `150 VE` CGI | 17 | 23 | 13 | 2 | 0 |
| plus-values immeubles · `150 U` CGI | 35 | 34 | 28 | 27 | 2 |
| taxe foncière · `1384 A` CGI | 14 | 7 | 15 | 13 | 7 |
| centralisation du livret A · `L. 221-5` CMF | 7 | 2 | 4 | 40 | 30 |
| statut des bailleurs · `L. 411-1` CCH | 8 | 1 | 2 | 124 | 114 |
| OPH · `L. 421-1` CCH | 41 | 15 | 40 | 124 | 105 |
| SA HLM · `L. 422-2-1` CCH | 19 | 14 | 3 | 12 | 2 |
| **total, huit cibles** | **171** | **126** | **129** | **393** | **273** |

**Premier constat — « on signale » n'est pas un régime tant qu'il n'y a pas de
tri.** Une seule mesure traîne **393 articles applicables qui citent ses cibles**.
Les lister en fin d'exposé sommaire ne produit pas un signalement, cela produit
un annuaire. *A-299 tient sur le principe et se précise* : le service minimum
porte sur les renvois de certitude `nomme` et `interne` ; les `ambigu` se
comptent et ne se listent pas.

**Deuxième constat — et il explique le premier.** Les 273 « hors de son code »
sont un **majorant grossier** : `L. 411-1` existe dans plusieurs codes, et un
compte nu ne sait pas si l'article citant vise le nôtre. **La règle de certitude
n'est pas un raffinement du relevé, c'est ce qui le rend interprétable.**

**Troisième constat, et c'est un défaut du corpus : `coordination.py` n'est pas
au dépôt de droit.** `reference/depot_droit.md` et
`reference/passation_droit_renvois.md` le décrivent, donnent sa ligne de commande
et publient ses mesures — quatre articles touchés par l'abrogation du `279` du
code général des impôts, neuf par celle du `L. 3262-1` du code du travail. **Le
dépôt public ne le porte pas**, à la révision `b6753f4`, millésime LEGI 20260901,
et son manifeste ne le mentionne pas. Il a été écrit dans un atelier et jamais
poussé. **L'étape du droit applicable n'a donc qu'une moitié en service**, et
l'état de la machine la déclarait entière.

**Quatrième constat — l'axe temporel est une opération, pas un avertissement.**
`1384 A` du code général des impôts est applicable **et** son abrogation est votée
au 1er janvier 2027 — et **une version nouvelle entre en vigueur le même jour**.
L'abroger aujourd'hui ne mord que trois mois : il faut traiter les deux versions,
ou la mesure s'éteint d'elle-même. Le même code porte une version
`MODIFIE_MORT_NE`, supprimée avant d'avoir pris effet.

*Ce que la machine a vu et que la lecture à la main n'avait pas vu* : la note
signale l'échéance sur les plus-values et pas sur la taxe foncière. Ce n'est pas
un reproche à la note — **c'est la démonstration que ce contrôle-là ne se tient
pas à l'œil**.

*Un point resté ouvert, et il ne se comble pas* : la note situe la TVA du
logement social aux articles `L. 221-56` à `L. 221-82` du code des impositions
sur les biens et services, ex-`278 sexies` du code général des impôts. **Le dépôt
ne porte aucune version de `L. 221-56`**, ni applicable ni future, quand il porte
bien l'ancien `278 sexies` en abrogation programmée. Soit l'extraction manque un
bloc, soit la référence n'est pas celle-là. **À vérifier sur pièce, et non à
trancher ici.**

### A-322 — Une septième opération : la version future déjà votée

**Tirée du constat précédent.** Les six opérations sur le texte n'en portaient
aucune sur le temps. Il en faut une septième, et elle se pose avant les autres :
**la cible porte-t-elle une version future déjà votée ?**

Trois cas, trois traitements, et aucun ne se devine :

- **abrogation programmée seule** — la cible disparaît d'elle-même à la date ; la
  mesure doit dire si elle avance la date ou si elle devient sans objet ;
- **version future qui remplace** — abroger la version applicable ne suffit pas,
  la suivante prend le relais. **Les deux se traitent, ou la mesure s'éteint** ;
- **version morte-née** — elle ne prendra jamais effet et ne se vise pas.

*Conséquence de rédaction* : **rédiger dans l'absolu reste juste ; c'est la
portée dans le temps qui ne l'est plus.** La colonne C se double, sur ces cibles,
d'une ligne qui dit sur quelle version elle porte et à partir de quand.

### A-316 — La rédaction se fait en deux niveaux, et le mur est au premier

**Structuré avec l'auteur le 20260903**, sur sa demande expresse : *réfléchissons
ensemble à comment construire cette grosse skill juridique clef, pour ne pas
aller dans le mur.*

**Le vrai enseignement vient d'une pièce du corpus, pas d'une idée.** La partie
« leviers juridiques » de la note sur le logement social fait déjà le travail, à
la main, et elle le fait bien. Ce qu'elle montre est que **la mesure éclate en
lots avant de se rédiger** : six codes, deux lois non codifiées, et pour chaque
bloc un verbe. La rédaction article par article vient après, et elle est la
partie facile.

**Niveau 1 — le plan de mesure.** Un siège, un verbe, une raison par lot. Huit
verbes relevés sur pièce : abroger · abroger sauf · supprimer une subdivision ·
maintenir avec adaptation · coordonner · transitionner · ponctionner · **rien à
faire**.

**`rien à faire` est le verbe qui compte.** La note le porte expressément — les
coopératives restent des coopératives, sans besoin de précision. Un lot muet ne
se distingue pas d'un lot oublié : le déclarer est ce qui sépare un plan complet
d'un plan qu'on croit complet.

**La grille de complétude, six fonctions**, cinq relevées sur la note et une
ajoutée par déduction : la norme, les privilèges, le statut, les contrats et
situations en cours, le patrimoine, et — *proposé, non validé* — le contrôle et
le reporting devenus sans objet. Le plan est complet quand les six sont
répondues, « sans objet » compris.

**Niveau 2 — la rédaction**, lot par lot, en trois colonnes. C'est là seulement
que le « = » s'applique.

**Le plan est dans la skill, en premier temps** — arbitré par l'auteur le 20260903. Une seule
chose à lancer ; l'utilisateur voit le plan dans la sortie, il peut le corriger
et rejouer.

### A-317 — Les trois procédures s'enchaînent, elles ne se choisissent pas

**Structuré avec l'auteur**, qui en proposait trois comme des options. Ce sont
trois objets différents, et les mettre en concurrence était la question mal
posée.

**Le levier et ses dépendants — elle décide.** On nomme le segment qui porte la
norme attaquée, un seul, avec sa raison ; C s'écrit là d'abord ; puis on suit la
cascade interne — définitions employées, dérogations qui le visent, renvois
numérotés, renumérotation, sanction, entrée en vigueur. **La cascade est en
grande partie mécanique** : un renvoi interne est un motif, pas un jugement.
C'est la coordination du dépôt de droit un cran plus bas — celle-là voit qui cite
l'article, celle-ci voit ce qui, dans l'article, dépend du segment. *C'est aussi
là que la question des coordinations se pose quantitativement, et elle se compte
avant de se juger.*

**Le balayage de couverture — il contrôle, et il ne rédige pas.** Segment par
segment, une seule question fermée : *ce segment reste-t-il vrai sous la
mesure ?* Trois verdicts — `inchangé`, `touché, traité`, `touché, non traité`.
**Le troisième est la sortie utile.** Un segment sans verdict est une rédaction
incomplète, et cela se compte.

**L'analogie — elle génère, et seulement là où A est vide.** Elle transpose un
**squelette** — assiette, bénéficiaire, taux, plafond, fait générateur, sanction,
entrée en vigueur, renvoi au règlement — **jamais les mots**, faute de quoi on
importe le régime du modèle sans le savoir. **L'écart au modèle est le
contrôle** : délibéré et déclaré, ou c'est un oubli. Le corpus en porte déjà un
usage — la transition des sociétés anonymes de crédit immobilier de 2006 sert de
précédent à la bascule statutaire et à la ponction.

**L'ordre n'est pas indifférent, et c'est la vraie réponse.** Lire du haut et
corriger au fil — la première voie proposée — fait rédiger dans l'ordre de
lecture : la portée dérive et les boucles d'harmonisation ne convergent pas.
**Une passe de jugement, une passe de vérification, aucune oscillation.**

### A-318 — Le transitoire se signale, il ne se rédige pas ; les crédits restent dans la skill

**Deux arbitrages de l'auteur, le 20260903.**

**Le transitoire et la coordination sont signalés.** La skill dit qu'il faut un
article, ce qu'il doit régler, et sur quel précédent le modeler. **Elle ne
l'écrit pas** : le délai, le prix de transfert et qui paie sont des décisions
politiques.

*La ligne est nette et elle se tient* : un article **créé qui porte la mesure**
se rédige, par squelette et analogie ; un article **de coordination** se signale.
Le premier est la mesure, le second est la machinerie. *Ce que cela protège* : la
skill ne fabrique jamais un texte sans A dont le contenu serait une décision
qu'on ne lui a pas donnée.

**Les crédits restent dans la skill, en branche à part** — « le cas facile à
part, mais ce serait bien que la skill ait cet add-in ». Ils ne modifient aucun
texte et n'ont ni A ni C ; la branche se prend au découpage, court-circuite les
trois procédures et applique un gabarit fixe — mission, programme, action au
besoin, sens, autorisations d'engagement et crédits de paiement, **jamais un
montant en dur**. *Motif retenu : l'utilisateur ne doit pas avoir à savoir qu'il
change d'outil.*

### A-319 — Les deux murs de l'étape, et ce qui les tient

**Tranché par Claude au titre d'A-23**, et c'est la part du risque que le
découpage ne suffit pas à couvrir.

**Le choix du levier**, sur un article long qui porte plusieurs régimes : jugement
irréductible. **La skill rend deux leviers candidats avec leur conséquence
plutôt que d'en choisir un en silence.**

**La réécriture d'article entier.** Le balayage n'y vérifie plus rien : tout a
changé, il n'y a plus de segment inchangé à opposer. **Réécrire est un refus par
défaut** — on décompose en abroger, remplacer, compléter, ou on déclare que le
contrôle sur ce lot est seulement humain. *C'est exactement là que vit la
disposition plausible et fausse, et c'est la sortie facile qu'il faut fermer.*

### A-320 — Ce qui existe ailleurs, et ce qui ne s'y trouve pas

Relevé par recherche, non supposé, sur question de l'auteur — *je ne connais
personne qui l'a fait, je crois qu'on est les premiers.*

**La plomberie existe et ne se rebâtit pas.** Le format d'échange des textes
législatifs est normalisé — Akoma Ntoso, employé par le Sénat pour sa base
d'amendements, et par plusieurs parlements ; la Commission européenne édite ses
textes dans un éditeur ouvert bâti dessus.

**La dérivation de la formule modificative à partir d'une comparaison de versions
est un problème résolu depuis longtemps** : la génération automatique de
législation modificative est publiée en conférence dès 1997. *Cela confirme le
choix du 20260902 : la forme modificative se dérive, elle ne se rédige pas.*

**Ce qui ne se trouve nulle part**, c'est le « = » : partir d'un énoncé de mesure
en langue naturelle et rendre le texte révisé. Le seul cas d'usage public voisin
est celui déposé par le Sénat italien en juin 2024 à l'Union interparlementaire —
et il est décrit comme un scénario, non comme une implémentation.

**Conséquence de conception** : on reprend la plomberie, on ne la refait pas ; ce
qui est neuf et à nous est **le plan et le jugement**, pas le formatage.

### A-315 — L'étape de rédaction est le signe « = » du trois colonnes, pas la disposition modificative

**Corrigé par l'auteur le 20260903**, contre une confusion que j'avais installée
au contrat et au prompt : *tu parles de code et d'additionnel, il y a une
confusion qui trempe déjà dans la légistique modificative contextuelle au
véhicule.*

**Ce que j'avais écrit.** Quatre « formes » de disposition — modificative sur un
article de code, sur les alinéas du texte déposé, article additionnel non
codifié, crédits sur la ligne. C'est une taxonomie de **l'emballage modificatif**,
et l'emballage dépend du véhicule et du texte en discussion. J'avais donc fait de
l'étape la plus véhicule-agnostique de la chaîne la plus dépendante d'entre
elles, dans un contrat dont c'est justement l'objet de l'empêcher.

**Ce que l'étape est.** Entrée : une mesure globale — supprimer, conditionner,
réduire — plus la localisation et le contenu des articles en vigueur. Sortie :
**la ou les nouvelles versions des articles**, du plus simple « X est abrogé » au
plus lourd « ceci à la place de cela, et cela en plus ».

**C'est le trois colonnes, et le corpus l'a déjà fait deux fois** — sur la
Constitution, sur la loi organique relative aux lois de finances. A le texte
actuel, B la réforme visée, C la rédaction révisée. **La skill est le signe
« = ».** Le descriptif de la colonne B s'allège et se ventile, comme il l'a été
sur la révision ; il ne devient pas la sortie.

**Trois conséquences, et elles bornent le fil mieux que ce que j'avais écrit.**

**La forme modificative est une dérivation, pas une rédaction.** « L'article X
est abrogé », « au deuxième alinéa, les mots … sont remplacés par … », « il est
inséré un article ainsi rédigé » se déduisent de la comparaison entre A et C.
*Et elle se prouve* : **réappliquée à A, elle doit redonner C à l'octet.** C'est
le seul endroit de la chaîne où une sortie rédigée se contrôle mécaniquement, et
c'est ce qui remplace les quatre « formes » comme colonne vertébrale de l'étape.

**L'échelle de difficulté n'est pas le véhicule, c'est l'opération sur le texte.**
Six, du plus simple au plus lourd : abroger l'article, abroger une subdivision,
remplacer un fragment, compléter, réécrire, créer. Le cas dur est leur
combinaison sur un même article, et il se rend en **une seule colonne C**.

**Les crédits sortent de l'étape.** Un amendement de crédits ne modifie aucun
texte : il porte un tableau sur une ligne de l'état, mission, programme,
catégorie, jamais un montant en dur. Il n'a ni A ni C. Le faire passer par le
« = » plierait un objet dans une forme qui n'est pas la sienne. **Gabarit propre,
écrit une fois, et pas dans ce fil.**

*Ce que la correction achète aussi, et qui n'était pas visible* : la colonne A du
trois colonnes n'était un verbatim que pour **26 blocs sur 37** à la Constitution
et **21 sur 29** à la loi organique — le reste était un résumé ou un constat de
vacance. Elle l'est désormais toujours : le texte en vigueur vient du dépôt de
droit avec son identifiant et sa date. **C'est le gain net de l'étape, et il se
gaspille dès qu'on résume A.**

*Portée générale, et c'est la leçon* : **une étape se définit par son objet, pas
par la forme que prend sa sortie en aval.** J'avais décrit E4 par ce qu'un
amendement donne à lire, non par ce que l'étape produit — et le contrat, qui
existe précisément pour séparer les deux, ne m'en a pas protégé parce que je
l'avais écrit avec la même confusion.

*Amende A-314 sur ses bornes B1 et B2*, et le contrat sur son E4. Les deux sont
réécrits.

### A-314 — Le fil de la disposition est borné avant d'être ouvert

**Tranché par Claude au titre d'A-23**, sur relevé de l'auteur : *ça peut être
dantesque.*

C'est juste, et c'est propre à cette étape. La rédaction légistique n'a pas de
fond : on peut y écrire un manuel et n'avoir toujours pas une skill. Les quatre
autres étapes de la chaîne ont un objet fini — une adresse, un verdict, un
exposé de 250 mots ; celle-ci n'en a pas. **Elle se borne donc au prompt, pas en
cours de route.**

**Cinq bornes.**

- **Deux véhicules, pas cinq.** Loi de finances et loi de financement ; les trois
  autres sortent en `hors_capacite` déclaré. *Motif : ce sont les deux seuls qui
  portent un lot au banc d'épreuve, et une capacité qu'on ne peut pas mesurer ne
  s'annonce pas.*
- **Quatre formes, dans un ordre, et on s'arrête où on en est.** Crédits sur la
  ligne, puis modificative sur article de code, puis article additionnel non
  codifié, puis alinéas du texte déposé. **Une skill qui tient les deux premières
  vaut mieux qu'une skill qui prétend les quatre.**
- **Trois exemples travaillés, pas trente-six.** Rédiger le lot entier serait
  jouer l'éval, et un fil ne juge pas sa propre skill.
- **La skill ne porte pas la légistique, elle y renvoie.** Elle ajoute l'arbre de
  décision et la liste des refus ; le répertoire de formules existe.
  *Signal d'arrêt mécanique : une skill plus longue que `vecteur-mesure` a
  commencé à écrire un manuel.*
- **Elle ne compense pas l'étape amont.** Le rattachement n'est pas outillé ;
  elle le déclare absent et rédige quand même. Une disposition juste sur une
  mesure irrecevable reste une disposition juste.

**Et le débordement a une issue écrite** : le fil verse ce qu'il a et écrit le
prompt de la suite, plutôt que de tout tenir. C'est A-8 — borner l'effort — vu
depuis le prompt au lieu de la conduite.



## 20260902 — Clôture du fil de structuration

### A-310 — L'ordre de dépôt et les chutes ne s'inscrivent nulle part par avance

**Arbitré par l'auteur le 20260902** : *je le dirai au moment venu.*

L'étape de liasse **assemble, numérote, et signale les concurrences qu'elle
voit** — deux pièces qui visent le même article, deux pièces qui visent la même
ligne de crédits. Elle ne propose ni ordre, ni chute.

**Aucune règle d'ordre ne s'écrit au corpus**, et c'est un résultat, pas un
manque : ni l'ordre du texte, ni le montant d'abord, ni les blocs à repli. Une
règle inscrite serait une décision de stratégie parlementaire prise par
l'appareil, et elle survivrait à celui qui ne l'a pas prise.

*Ce que cela ferme* : la dernière colonne de l'étape de liasse reste vide par
construction, et une liasse sans ordre déclaré n'est pas une liasse en défaut.
*Ce que cela laisse ouvert* : rien. La question ne se repose pas ; elle se pose
à l'auteur, liasse par liasse.

### A-311 — Le calendrier d'examen reste déclaré inconnu

**Arbitré par l'auteur le 20260902** : *on s'en passe pour l'instant.*

Seule la date de dépôt du projet de loi de finances est certaine — la loi
organique la borne au premier mardi d'octobre. **Elle borne la passe ; elle ne
dimensionne pas la machine.**

Le calendrier d'examen — commission, séance, et surtout la date limite de dépôt
des amendements, qui est celle qui commanderait — **n'entre pas au corpus tant
qu'il n'est pas publié**. Il ne se cherche pas, il ne se suppose pas, et rien ne
se dimensionne dessus.

*Ce que cela protège* : un calendrier relevé sur un site et vieilli de trois
semaines a l'apparence d'un fait et n'en est pas. C'est la règle du vecteur
périmé, appliquée à une date.

### A-312 — La jauge du coffre se compte en jetons, pas en octets

**Constaté au versement, et cela corrige une lecture tenue depuis A-128.**

A-128 posait que « la jauge ne compte pas des octets bruts » et s'arrêtait là.
Elle compte des **jetons** : le champ `knowledge` du projet portait 1 631 440
pour un maximum de 2 000 000, et l'archive technique seule pèse **425 062
jetons** pour 1 700 246 octets — un rapport d'environ quatre octets par jeton.

**Deux conséquences qui changent un geste.**

Le versement d'une pièce **n'est pas crédité de la place que l'ancienne
libère** : réécrire l'archive par-dessus elle-même a été refusé, la somme de la
jauge et de la pièce neuve dépassant le maximum. **Une grosse pièce se supprime
avant d'être réécrite**, et l'ordre des deux gestes n'est pas indifférent — entre
les deux, le coffre ne la porte plus, et seul le dépôt et le transcript la
tiennent.

**Un chiffre de marge annoncé en octets est faux d'un facteur quatre.** Le prompt
du fil annonçait 113 519 ; le champ portait 1 631 440 / 2 000 000, soit 368 560
de marge en jetons, ce qui n'est pas une quantité d'octets. *La jauge se lit à
`project_info`, dans son unité, et jamais convertie.*

### A-313 — La restauration à blanc a tourné, et le tuyau était nécessaire

**Éprouvé, non affirmé.** Après versement, l'ensemble a été remonté dans un
**dépôt vierge** : archive dépliée, documents lisibles restaurés par copie
d'octets, comparaison aux empreintes. **80 artefacts présents, R1 à 0, R3 à 0,
R4 à 0, R5 à 0.** Les 40 absents sont ceux que ce fil n'a jamais dépliés.

Deux choses que le test apprend, et qu'aucun contrôle sur le dépôt courant ne
dit.

**Le transcript porte l'état d'avant, pas l'état d'après.** Un fil qui verse puis
restaure à blanc dans la foulée récupérerait les octets qu'il a lus en ouverture,
et non ceux qu'il vient de verser. Il faut **relire le coffre après le
versement** — par un fil auxiliaire qui sert de tuyau, qui lit et n'écrit rien.
`restaurer.py` a bien retenu les lectures les plus récentes et nommé les quatre
versions écartées avec leur horodatage.

**Un document rendu comme fichier échappe au tuyau.** `restaurer.py` ne relève au
transcript que ce que le coffre rend **en texte** ; le registre, désormais à
274 099 octets, revient comme fichier et se restaure par `cp`. C'est la voie 1,
elle est prévue, et elle est manuelle. *À reprendre à l'appareil quand un
deuxième document franchira le seuil.*

## 20260902 — La structuration de la machine à amendements

*Numérotation : les fils du dépôt de droit et de l'éval ont consommé les numéros
`A-270` à `A-298` sans porter leurs entrées au registre — `A-271`, `A-272`,
`A-273`, `A-297` et `A-298` sont cités par `reference/passation_droit_renvois.md`
et par `reference/domaine_lfss_LO111-3.md`, dont les textes ne sont pas au
coffre. Ils restent à porter par le fil qui les détient. Ce fil reprend à
`A-299` plutôt que de réattribuer des numéros déjà cités.*

### A-299 — Les renvois entrants : on signale en amendement, on coordonne en proposition de loi

**Arbitré par l'auteur le 20260902**, au fil du dépôt de droit, et porté ici
parce qu'aucun fil ne l'avait inscrit.

Modifier un article laisse derrière lui les articles qui le **citent**. Rien ne
les cherchait : `N1` refuse de confondre vecteur et véhicule, `N6` voit deux
mesures qui visent la même adresse, **aucun ne voit qui cite la nôtre**.

**Amendement — service minimum.** On ne coordonne pas, on **signale** : les
renvois relevés se listent en fin d'exposé sommaire. *Le maquis des renvois ne
doit pas bloquer la production.*

**Proposition de loi — la boucle va jusqu'au bout.** Chaque renvoi se traite ou
se déclare sans objet avant dépôt. Travail lourd, assumé comme tel.

Chaque renvoi porte sa **certitude**, fixée par une règle de déduction et jamais
par une impression : `nomme`, `interne`, `ambigu`. *Mesuré : abroger l'article
279 du code général des impôts touche quatre articles applicables ; abroger
`L. 3262-1` du code du travail en touche neuf, dont cinq au code de l'éducation,
invisibles depuis le code du travail seul.*

*Conséquence portée au contrat* : c'est le **seul** endroit de la chaîne où le
véhicule change le régime d'une étape, et non seulement sa porte.

### A-300 — La dépense locale se prend par les trois leviers, dans l'ordre

**Arbitré par l'auteur le 20260902**, sur question fermée : *les trois, dans cet
ordre.*

| ordre | levier | siège | véhicule |
|---|---|---|---|
| 1 | la **recette** — dotations et fiscalité affectée | code général des collectivités territoriales ; code général des impôts et fiscalité affectée | loi de finances |
| 2 | la **dotation** — prélèvement sur recettes et concours | code général des collectivités territoriales | loi de finances |
| 3 | la **norme** — la compétence ou l'obligation qui produit la dépense | code sectoriel | loi ordinaire |

L'étape de qualification **rend les trois adresses quand elles existent** et dit,
pour chacune, si elle est portable dans le véhicule visé. Elle ne choisit pas.

*Ce que cela coûte, et il faut le dire* : trois recherches par mesure au lieu
d'une. *Ce que cela achète* : la mesure ne tombe plus faute d'avoir cherché du
mauvais côté — c'est le manque de l'éval sur la participation des employeurs à
l'effort de construction, où l'article qui porte la cotisation avait été rendu
pour celui qui porte l'obligation.

*Ce qui se dit dans l'exposé et ne se découvre pas en séance* : réduire la
ressource ne commande pas l'emploi. La collectivité arbitre, et elle peut
arbitrer contre la mesure.

### A-301 — Le registre de l'amendement est celui de la séance

**Arbitré par l'auteur le 20260902** : quand le français parlementaire et notre
vocabulaire divergent, **le parlementaire l'emporte**, sauf une courte liste de
mots tenus.

L'exposé sommaire s'écrit donc dans la langue de la séance — prélèvements
obligatoires, administration, dépense publique. C'est la condition pour que
l'outil serve n'importe qui : un amendement qui se repère comme militant à sa
langue n'est pas déposable par un tiers.

*Proposé, non validé* : trois mots tenus, **restitution**, **bureaucratie**,
**intermédiaires**. Ils portent le fond et non le style. La liste se révoque d'un
mot, et le contrôle vérifiera alors deux jeux — les interdits de séance d'un
côté, les mots tenus de l'autre.

*Ferme, sur ce point, la divergence signalée au gabarit de l'exposé sommaire.*
Reste ouverte l'autre : la proportion du constat, un cinquième chez nous, un
tiers au gold standard.

### A-302 — La forme du passage : un objet unique, à lecture bornée

**Arbitré par l'auteur le 20260902**, dans ses termes : *il faut que les étapes
soient découpables pour être décomposables et recomposables, mais que
l'utilisateur, dans le contexte, ne voie pas cette complexité et voie la boucle
complète.*

Une seule forme tient les deux exigences, et c'est la dérivation qu'en tire
Claude.

**Un objet unique voyage** — le dossier de mesure. Chaque étape y ajoute son bloc
et n'efface rien. L'utilisateur donne un énoncé et reçoit un amendement : il ne
compose pas des étapes et ne recopie rien de l'une à l'autre.

**Chaque étape déclare ce qu'elle lit.** Un bloc `lit`, un bloc `ecrit`, vérifiés
mécaniquement. Une étape se rejoue seule en ne lui donnant que ce qu'elle
déclare lire, et son taux se mesure sans que le reste du dossier lui souffle la
réponse. C'est ce qui garde le découpage réel au lieu d'affiché.

**Invariant** : chaque étape déclare ce qu'elle a reçu et si elle en a douté.
`recu` et `doutes` ne se laissent jamais vides ; une étape qui n'a douté de rien
écrit `aucun`.

*Écarté* : le relevé par étape, qui s'éprouve aussi bien mais fait recopier le
contexte à la main entre deux étapes — donc par l'utilisateur, et c'est
exactement la complexité que l'auteur refuse de lui montrer. Écarté aussi le
relevé doublé d'un socle recopié : le même énoncé en plusieurs exemplaires est
un second point de vérité.

`methode/contrat_chaine_amendement.md`.

### A-303 — Le contrôle `G` bloque sur l'identité, signale le reste — et une question de tambouille ne se pose pas

**Tranché par Claude au titre d'A-23**, après un rappel de l'auteur qui vaut
au-delà du cas : *pas clair, orienté utilisateur — je connais bien la procédure,
pas la tambouille.*

**J'avais posé en questions deux points qui n'en sont pas.** Bloquer ou signaler,
et la liste des termes interdits, sont de la mécanique de contrôle. A-23 le dit
depuis le 20260821 : demander un feu vert pour de la tambouille est une faute au
même titre que trancher seul une question de fond. **La règle se précise ici : une
question se pose dans les termes de ce que l'auteur décide — un input, un output,
un objectif —, jamais dans ceux de l'outil qui l'exécute.** Deux tours ont été
perdus.

**Le contrôle, tranché.** Deux rangs.

- **`G1` à `G6` — échec.** Ce qui identifie : un déposant nommé, le nom du
  projet, le manuscrit et la doctrine, le coffre et l'appareil de session, un
  référentiel interne, la nomenclature interne. Une skill qui en porte un n'est
  pas publiable, et le savoir après diffusion ne sert à rien.
- **`G7` à `G8` — signalement.** Ce qui est seulement suspect : rien ne dit ce
  que la skill rend quand la base documentaire manque ; un chemin de dépôt est
  cité. Cela se juge, cela ne se prouve pas.

**Le frontmatter est dans le périmètre** : c'est là que la fuite a survécu le
plus longtemps, dans la description enregistrée, visible dans toute liste de
skills sans que le fichier soit ouvert.

**Une seule exemption, et elle vit dans le module de contrôle, jamais dans la
skill contrôlée** : l'adresse d'un dépôt public. Une skill qui lit le texte en
vigueur doit nommer ce qu'elle clone ; une ressource publique n'est pas un
référentiel interne. Une exemption qui vivrait dans la skill serait une porte que
la skill s'ouvre elle-même.

**Éprouvé à l'envers avant d'être admis** : une skill de fuite injectée sort six
échecs et un signalement, une skill propre sort à zéro. `make controle` le joue,
`make G` le joue seul, et sans fichier de skill au dépôt il le dit et la chaîne
continue.

### A-304 — Ce que la dette portait réellement, et ce qui était déjà purgé

Vérifié au dépôt, contre le prompt du fil, qui était périmé sur trois points.

**Déjà purgé** : `cles_eval_expose.py` et `noter_eval_expose.py` sont déclarés à
l'index et pliés dans l'archive ; les `SKILL.md` ne sont plus au dépôt.

**A-194 est clos, et il n'a jamais été un défaut de code.** L'archive au dépôt
vit à `coffre/coffre.txt`, là où `make coffre` l'écrit, et le contrôle l'y
trouve. Elle sortait en R2 parce qu'elle avait été posée ailleurs.

**Le chemin du gabarit n'était pas périmé, il était mal rangé.** La digestion de
l'exposé sommaire est **notre écrit**, vérifiable contre une source externe :
c'est une référence de rang `methode`, pas une pièce de l'auteur. Elle passe de
`sources/gabarit_expose_sommaire.md` à `reference/gabarit_expose_sommaire.md`,
avec l'ancien chemin en alias, et rejoint les trois documents de `reference/`
versés par le fil du dépôt de droit — dépôt de droit, domaine des lois de
financement, passation — qui n'étaient déclarés nulle part.

**La dette réelle est ailleurs, et elle se dit** : **quatorze documents sont au
coffre et non déclarés à l'index**, venus des fils du sourçage et de la lecture
en creux. Ils ne sont pas perdus — le coffre les porte — mais aucun script ne
sait les remettre au dépôt, et aucune empreinte ne les couvre. **Ce fil ne les
déclare pas** : classer un document qu'on n'a pas ouvert est la faute qu'A-24
interdit. Ils reviennent au fil qui les a écrits, ou à un fil qui les ouvrira.

### A-305 — Cumulatif ne veut pas dire éternel

**Tranché par Claude au titre d'A-23.** Le relevé des empreintes est cumulatif —
un fil qui ne déplie qu'une partie du coffre n'efface pas le reste. Il ne l'était
pas seulement : il ne retirait **jamais** rien. `appareil/proto_fiches.py`,
renommé depuis, y portait encore son empreinte, et chaque renommage en ajoutait
une.

**Le retrait se fait sur ce que l'index déclare, jamais sur ce qui est présent au
dépôt.** Un fil qui n'a pas restauré un document ne l'efface pas ; un artefact
que l'index ne déclare plus est renommé ou mort, et son empreinte ment. Trois
empreintes périmées retirées à la première exécution, et le retrait se dit ligne
à ligne.

### A-306 — L'appareil de mesure fuyait et ne mesurait qu'une moitié

Deux défauts inscrits au 20260902 et corrigés le 20260903, par un fil qui ne les subit
pas — aucun fil ne peut corriger son propre appareil de mesure pendant qu'il
s'en sert.

**La clé fuyait par son propre résumé.** Elle nommait en clair les cas sans
adresse relevable et comptait ceux qui portent un article, **avant que le fil
joue**. C'était donner la moitié de la vérité-terrain : deux cas du lot de
financement ont été joués en connaissance de cause. Le résumé ne rend plus que ce
que la liasse dit déjà — combien de couples, leur ventilation par nature et par
variante. *La vérité-terrain est scellée ou elle n'est pas.*

**La notation mesurait le rappel et ignorait la précision.** Un cas concordait
dès qu'une adresse sur N intersectait la clé : une skill qui rend neuf adresses
dont une juste obtenait le même verdict qu'une skill qui en rend une, juste. Les
deux dimensions se publient désormais ensemble, avec le détail des concordances
obtenues sur plus d'une adresse rendue. *Un rappel seul dit qu'on trouve ; il ne
dit pas ce qu'on ramasse avec.*

**Deux corrections de plomberie avec elles.** Le chemin des réponses se déduit du
lot et non d'un fichier posé à côté du script. **Les contaminés se vérifient
contre la population** au lieu de s'annoncer en compte fixe : un contaminé déclaré
et absent fait sortir un dénominateur faux, et le contrôle le dit maintenant.

### A-307 — Ce qui se compte descend dans un dérivé, ce qui se décide reste à la carte

**Trois gestes, un seul principe** : un état tenu à la main raconte au lieu de
compter.

**Le rapport de clôture se renomme.** `methode/ETAT_DU_CHANTIER.md` était le
rapport du fil gagnants-perdants du 20260820 : il ne parle ni de la machine, ni
du projet de loi de finances, et son inventaire de montage décrit un dispositif
remplacé. Son nom faisait croire à un point de situation courant, et un fil
neuf l'ouvrait pour cela. Il devient
`archive/rapport_gagnants_perdants_20260820.md`, **contenu inchangé à l'octet** —
`71c1c607…`, 30 453 octets — et l'ancien nom résout par alias.

**La carte des chantiers perd ses comptes.** Son §3 portait les 128 programmes,
les 41 lignes, les 465 dépenses fiscales, les 278 taxes et des états d'étape qui
dérivaient à chaque passe. Il se réduit au **périmètre et aux dépendances**.

*Constaté et non corrigé* : son §2 porte les mêmes comptes qui dérivent — « 12
apports rédigés sur 194 ». Il relève du chantier gagnants-perdants et non de
celui-ci ; il se signale plutôt que de se toucher au passage.

**Les comptes descendent dans `livrables/etat_machine.html`**, généré, zéro
chiffre saisi à la main. Deux grilles — les étapes et leur état, les étapes
contre les véhicules et les contextes — et un troisième tableau qui rend le banc
d'épreuve tel qu'il est. Tout ce qui s'y compte sort de
`referentiels/lots_epreuve.json` ; ce qu'aucun lot ne porte reste vide, **et une
case vide est un résultat**.

*Il va au coffre*, comme l'état des vecteurs et pour la même raison : c'est le
point de situation que l'auteur ouvre entre deux sessions. La marge le permet
largement — le prompt du fil annonçait 113 519 octets, la jauge en portait
368 560.

### A-308 — Le banc d'épreuve est un référentiel, pas un compte-rendu

**Tranché par Claude au titre d'A-23.** `referentiels/lots_epreuve.json` porte un
lot par véhicule, et pour chaque lot la population, les contaminés, et **la suite
des mesures jouées sur chaque étape** — pas la dernière seule.

Cinq règles de lecture y sont écrites, et la quatrième est celle qui manquait :
**deux taux ne se comparent que si la population aveugle est la même.** Le rejeu
du 20260902 rend 90,9 % contre 63,6 %, et les deux ne se comparent pas — le
prompt du rejeu nommait huit des vingt-deux cas. Le référentiel porte le second
taux avec `comparable: false` plutôt que de le taire ou de l'afficher comme un
progrès.

**Trois lots existent, cinq véhicules sont visés.** Les trois véhicules sans lot
se déclarent sans lot, avec la raison : sur une proposition de loi, l'unité n'est
pas le couple, et la vérité-terrain d'une révision serait la nôtre.

*Ce que le lot de financement ne sait pas encore de lui-même* : ses deux cas
contaminés ne sont pas nommés, faute d'avoir été relevés au moment où ils l'ont
été. Ils sont portés en `a_relever`, et la notation majore son taux d'autant en
le disant. **Les nommer de mémoire fabriquerait une clé fausse.**

### A-309 — Ce que ce fil n'a pas fait, et pourquoi

**L'entrée au journal du 20260902 n'est pas écrite.** Le fil avait consigne de ne
pas déplier le journal ; il ne peut donc ni le lire, ni y insérer un bloc par
`porter_bloc.py`, qui travaille sur le fichier au dépôt. La consigne et A-65 —
le journal se tient en dynamique — se contredisent sur ce point, et la
contradiction se dit plutôt qu'elle ne se tranche seule. *Le premier fil qui
déplie le journal y porte le bloc du 20260902.*

**Aucune skill n'est écrite et aucune éval n'est jouée.** Un fil ne juge jamais
une skill qu'il a écrite, et celui-ci a touché l'appareil de mesure.

### A-267 — L'objet du chantier est une machine, pas un lot d'amendements

Corrigé par l'auteur le 20260902, après une erreur de cadrage tenue sur deux
réponses. J'avais fait de la population des amendements le dénominateur du
chantier et proposé de la construire en référentiel, avec le dépôt du PLF pour
échéance dimensionnante.

**Ce qu'on construit est une procédure outillée** qui prend l'énoncé d'une mesure
en langage naturel et rend un amendement déposable, et qui doit tourner **pour
n'importe qui, n'importe quand, sur n'importe quel véhicule** — PLF, PLFSS, PPL,
PPLO, PPLC. L'amendement est l'output roi immédiat. **L'analyse du PLF contre le
manuscrit est une passe** — majeure, un point d'orgue — pas la fin du jeu.

Trois conséquences, et elles commandent tout ce qui suit.

- **L'avancée ne se mesure pas en amendements produits.** C'est le compte d'une
  passe. Elle se mesure à l'état de la capacité : quelles étapes existent, sont
  éprouvées, généralisent, et dégradent proprement. Une étape a un état, pas un
  pourcentage.
- **Aucune étape ne peut dépendre du corpus interne pour fonctionner.** Celle qui
  exige le socle, le manuscrit ou la doctrine pour rendre un résultat n'est pas
  une étape de la machine : c'est une étape de la passe (A-232).
- **Le référentiel des mesures n'est pas le dénominateur, c'est le banc
  d'épreuve.** Un lot de référence par véhicule, sur lequel on rejoue le taux de
  chaque étape — ce qui rend la maturité mesurée au lieu d'affirmée, et ce qui
  détecte qu'une correction de skill a cassé autre chose.

Le dépôt du PLF est borné par la loi organique au premier mardi d'octobre, soit
le 6 octobre 2026. **Cette date borne la passe ; elle ne dimensionne pas la
machine.**

### A-268 — La généralisation devient un contrôle, elle cesse d'être une intention

Quatorze mentions d'un déposant nommé ont été rattrapées à la main par l'auteur,
en deux fois : treize dans `expose-sommaire`, une dans `vecteur-mesure` — plus,
et c'était la plus exposée, **la description de la skill enregistrée**, visible
dans toute liste de skills sans que le fichier soit ouvert.

Une règle qu'on tient à l'œil se perd. Elle devient donc mécanique : un contrôle
`G` refuse dans un fichier de skill toute mention d'un déposant nommé, du nom du
projet, du manuscrit, du coffre, d'un référentiel interne, de la nomenclature D ;
et toute étape qui ne rend rien socle absent. **Le frontmatter est dans le
périmètre du contrôle** — c'est là que la fuite a survécu le plus longtemps.

### A-269 — Ce que la clôture a corrigé, et ce que le point de situation ne peut pas faire

**Deux fichiers étaient au dépôt sans être déclarés** — `cles_eval_expose.py` et
`noter_eval_expose.py` — donc absents du coffre et perdus à la réinitialisation
suivante. Déclarés, pliés, versés. Le coffre passe de 59 à 61 pièces.

**Cinq fichiers n'avaient rien à faire au dépôt** et sortent à l'atelier : les
trois json de travail de l'éval, qui se régénèrent depuis les pièces jointes
(A-71), et les deux `SKILL.md`, dont le point de vérité est la skill enregistrée
au compte et non une copie de travail. Un fil n'est pas un lieu de stockage, et
un dépôt non plus quand le durable est ailleurs.

**Sur le point de situation, trois documents portent le nom et aucun ne le fait.**
`methode/ETAT_DU_CHANTIER.md` est le rapport de clôture du fil gagnants-perdants
du 20260820 et ne parle pas du PLF : son nom induit en erreur.
`methode/carte_des_chantiers.md` §3 est le seul cadrage du contre-PLF, et il
porte des comptes qui dérivent. `livrables/etat_vecteurs.html` est généré, donc
juste par construction, mais il ne couvre qu'une étape.

**La règle qui en sort** : un état tenu à la main raconte au lieu de compter. Les
comptes descendent dans un dérivé régénéré, la carte garde le périmètre et les
dépendances. Et un point de situation ne se construit pas avant que les cases
existent : une grille aux trois quarts vide n'apprend rien qu'on ne sache déjà.

## 20260901 — L'éval du vecteur a tourné, et elle a corrigé la skill

### A-256 — Le statut de la dépense décide de la famille de siège, et il se qualifie avant de chercher

**Énoncé par l'auteur** : « toutes les dépenses n'auront pas le même statut :
dépenses sociales cadre particulier du PLFSS, dépenses locales pilotées via
dotations et recettes et règles, dépenses d'opérateurs via taxes affectées et
cadre budgétaire. Tu dois bien chercher pour localiser le bon siège à chaque
fois. »

**C'est la cause des trois manques de l'éval, et non une remarque de plus.**

| statut | véhicule | siège |
|---|---|---|
| crédits d'État | PLF, état B | interne au PLF, aucun siège de droit |
| dépense fiscale | PLF 1re partie | l'article dérogatoire, porté par l'annexe |
| dépense sociale | PLFSS | code de la sécurité sociale, porte à l'article LO 111-3 |
| dépense locale | PLF pour la ressource, loi ordinaire pour la norme | **trois sièges** : dotations au CGCT, recettes au CGI et à la fiscalité affectée, compétence au code sectoriel |
| dépense d'opérateur | PLF 1re ou 2de partie | **deux sièges** plus le cadre budgétaire, qui vit dans des lois de finances antérieures et non dans un code |

**Le choix du levier précède la recherche.** Réduire une dépense locale par la
dotation, par la recette ou par la norme mène à trois codes différents. La skill
ne tranche pas le levier, mais elle ne cherche pas avant qu'il soit dit.

*Ce que le défaut a coûté, mesuré* : sur la participation des employeurs à
l'effort de construction, la skill a rendu l'article du code général des impôts
qui porte la cotisation quand l'amendement visait celui du code de la
construction qui porte l'obligation. Adresse plausible, mauvais levier — c'est
A-245 sur la création contre le financement, ratée là où elle mordait.

`vecteur-mesure` prend donc une **étape 0** : qualifier le statut. Elle est
enregistrée.

### A-257 — L'unité de la liasse est le couple dispositif / exposé, pas le numéro d'amendement

Constaté sur pièce. `GL-II-7` porte **un numéro et six déclinaisons**, chacune
avec son tableau de crédits et son propre exposé sommaire. Découper sur le numéro
perdait cinq exposés sur six, et le premier jet les a perdus.

**36 couples pour 31 numéros**, zéro dispositif vide, zéro exposé vide. Un
amendement peut courir sur plusieurs pages : une page sans en-tête est une
continuation et se recolle. Un glyphe de police symbole précède parfois l'en-tête
— le repérage se fait par recherche, non par ancrage en début de ligne.

*Compte* : 31 numéros au PLF, les 8 restants des 39 sont à la liasse PLFSS.
`GL-II-8` n'a pas d'exposé sommaire dans la pièce et sort de l'éval faute
d'entrée.

### A-258 — L'éval des crédits ne mesure rien, et la population se juge autrement

**Onze exposés de crédits sur douze nomment eux-mêmes le programme.** L'adresse
est dans l'entrée : l'éval telle qu'A-249 la spécifie mesurerait la lecture, pas
la recherche de vecteur.

*Précise A-249* : **le taux de rappel porte sur les seuls cas de norme.** Les cas
de crédits reçoivent un exercice de conformité — l'adresse étant donnée, la skill
construit-elle le bon vecteur d'état B, mission puis programme, et refuse-t-elle
un montant en dur (A-244). Deux exercices, deux résultats, jamais un taux unique.

*Confirmé par l'auteur* : « pour les crédits, ce sera interne au PLF donc un non
sujet. »

*Point d'appareil ouvert* : la clé des 12 cas de crédits n'est pas extractible,
les programmes vivant dans les tableaux. Cette population demande son propre
extracteur de tableau.

### A-259 — Le taux : 14 concordances sur 22, zéro discordance

Éval jouée en aveugle sur l'exposé sommaire seul, en mode socle non disponible —
`REF_norme` n'était pas au dépôt, faute des classeurs. C'est donc un **plancher**,
dans les conditions de la version publique.

| verdict | n | part |
|---|---|---|
| concordance | 14 | 63,6 % |
| voisinage | 8 | 36,4 % |
| **discordance** | **0** | **0 %** |

**Aucune adresse n'a envoyé l'amendement au mauvais endroit.** C'est le résultat
qui compte le plus : le risque nommé par A-245 ne s'est pas matérialisé une fois.

**Les huit voisinages ne se valent pas.** Cinq ne sont pas des manques — sur
`GL-I-22`, `GL-II-9`, `GL-II-10`, `GL-II-11` et `GL-II-12`, le dispositif de GL ne
cite aucun article de code : il insère un article non codifié, ou travaille sur
les alinéas de l'article du PLF qu'il rouvre. La skill a rendu une adresse là où
GL n'en visait pas. **Trois sont de vrais manques** : `GL-II-2` (siège dans une
loi de finances antérieure), `GL-I-29` (crédit d'impôt déclaré sans siège alors
qu'il en a un), `GL-I-33` (levier confondu).

### A-260 — La variante commande le type d'adresse, pas seulement le point d'accroche

Tiré des cinq voisinages ci-dessus. **Sur un article ouvert, le dispositif porte
sur les alinéas du texte déposé, pas sur un article de code** — en produire un est
une surqualification. Sur un article additionnel, la mesure vise soit un article
existant, soit un article nouveau non codifié : une clause de caducité, une
obligation de rapport, une règle de suppression automatique n'ont pas de siège
préexistant.

D'où une valeur d'état de plus, **`siege_non_codifie`** : la mesure est
rédigeable, elle n'a pas d'article à modifier. Ce n'est ni `trouve` ni
`a_trouver`.

### A-261 — Le premier tour a donné 36 %, et c'était ma clé qui était fausse

Deux défauts, tous deux dans mon extracteur de vérité-terrain, aucun dans la
skill. **Ils valent d'être écrits parce qu'ils sont des rechutes.**

**La ligne de rattachement était relevée comme une adresse.** « Après l'article
65 » nomme le **véhicule**. J'ai refait l'erreur que `N1` refuse, dans l'outil
qui devait la mesurer. Cinq cas sortaient en discordance contre un article du PLF
pris pour un article de code.

**Le suffixe en lettre était coupé** : « 200 A » → « 200 », « 790 G » → « 790 »,
« 1594 D » → « 1594 », « 244 quater B » → « 244 quater ». C'est A-251 refaite un
cran plus bas, dans la clé au lieu du référentiel. Quatre voisinages étaient des
concordances.

*Ce que cela enseigne, et c'est la règle* : **une clé fausse note faux, et seul un
contrôle mécanique l'attrape.** Une relecture à l'œil aurait validé les 36 %.

### A-262 — Une correction de skill se rééprouve par un fil qui ne l'a pas écrite

Tranché par Claude au titre d'A-23. Le fil qui a joué l'éval connaît les 22
réponses : rejouer chez lui mesurerait sa mémoire. **Le rejeu passe par un fil
vierge**, qui reçoit les exposés, joue la skill enregistrée, écrit ses réponses,
et laisse `noter_eval_gl.py` noter. Les clés ne bougent pas, les taux se comparent
terme à terme.

*Corollaire* : le fil de mesure ne lit ni le registre ni la procédure des
vecteurs. C'est la skill qui est sous test, pas le corpus.

### A-263 — Le gabarit de l'exposé sommaire cale sur le docx, pas sur la pratique GL

**La règle de 200 à 300 mots est tenue par 19 exposés sur 36 — 53 %.** Médiane
216 mots, 14 sous la borne basse, 3 au-dessus de la haute, le plus long à 672.
**L'exemple du document GL fait 249 mots** : la norme est cohérente avec
elle-même, c'est la pratique déposée qui dérive.

**Conséquence de conception, et elle inverse ce qu'on attendait** :
`expose-sommaire` cale sur le gold standard, jamais sur les liasses. Calibrer sur
la pratique aurait appris une médiane de 216 et une fourchette molle. **Les
liasses mesurent l'écart, elles ne fixent pas la cible.**

*Deux choses que la digestion avait perdues et que le gabarit reprend* : le
critère central — « un exercice pédagogique d'exposition d'un dispositif
technique, mis en rapport avec un objectif politique clairement identifiable » —
et le caractère **souple** des trois temps, que GL écrit « tant que peut se
faire ». Une skill qui refuserait un exposé à deux temps serait plus stricte que
le gold standard : signalement, pas échec.

### A-264 — Le document GL sort du coffre, son grain reste

**Autorisé par l'auteur**, qui en a copie : `Exposé des motifs - rédaction GL.docx`
se supprime du coffre. Son grain est levé et porté à
`reference/gabarit_expose_sommaire.md` avant la suppression, et l'index le
déclare désormais pièce jointe de l'auteur, hors coffre, `restaurable: false` —
même régime que les classeurs.

*Ce qui rendait la suppression admissible, et rien d'autre* : l'auteur a le
fichier. A-6 tient — une pièce que rien ne sait refaire ne se supprime pas ; ici
elle se refait par pièce jointe.

*Où la place se trouve vraiment* : A-128 la nommait déjà — les trois protos gelés
les plus lourds, 208 ko sur trois documents, contre 125 ko de marge. Décision de
l'auteur, après vérification d'index : `Donnees` et `1pager` sont porteurs.

### A-265 — Les liasses confirment le 12 000, et A-129 se ferme sur la source

L'exposé de `GL-II-1` porte « 103 agences, 434 opérateurs, 317 organismes
consultatifs, 12000 organismes publics nationaux », et **ses notes nomment la
source** : Vie Publique, « Agences et opérateurs de l'État : quelles possibilités
de réorganisation de l'action publique ? », 9 juillet 2025 ; et pour le coût du
rapport du CESE, Le Figaro du 14 mars 2025.

A-129 laissait ce 12 000 « à vérifier sur la pièce Vie Publique ». **Il est bien
de GL, sourcé chez eux, daté.** L'écart à nos 1 104 et aux 1 153 du Sénat reste
entier — il porte désormais sur une pièce identifiable, et le chiffre à citer
reste celui d'A-130 : notre décompte.

### A-266 — Ce que l'éval a versé, et ce qui reste au fil

Trois modules entrent à l'archive technique : `scinder_liasses.py` — extraction
des liasses en couples, dispositif scellé —, `cles_eval_gl.py` — la
vérité-terrain, écrite et jamais affichée — et `noter_eval_gl.py` — les trois
verdicts et le taux. **Le taux se rejoue à l'identique**, les PDF rentrant par
pièce jointe.

Ne se versent pas : les exposés extraits et les clés, qui se refont en une
commande depuis les pièces jointes (A-71).

## Sections sans fragment, reprises à l'historique le 20261001

*Les fragments qui avaient produit les onze sections ci-dessous ne sont plus
au coffre : un assemblage les aurait effacées. Elles sont reprises ici,
verbatim et à l'octet, au-dessus de la ligne de marque, où rien ne les
réécrit. Deux d'entre elles n'ont jamais eu de fragment — elles avaient été
écrites à la main sous la marque, ce que la règle interdit.*

## 20260917 — ecart-classeurs

**Les classeurs mis au propre du 20260917 sont la source officielle, seuls.**
*Tranché par l'auteur.* Les six classeurs antérieurs sortent du rôle de source ;
ils restent aux pièces jointes comme état daté. L'appareil est rebranché dessus,
et les sources de `appareil/sources_chiffres.py` qui nomment les millésimes 0819
et 0804 deviennent historiques — elles restent vraies de l'état qu'elles citent.
*Ancienne question 25, retirée de `methode/a_trancher.md`.*

**Une économie de masse salariale se restitue en totalité : 30 % en année 1,
70 % au solde.** *Tranché par l'auteur.* Le classeur ne l'écrit nulle part en
toutes lettres, il l'applique — le rapport est la seule preuve, et il est exact
sur les trois lignes qui le portent : départs de fonctionnaires d'État
(0,9 / 3), départs locaux (6 / 20), part salariale de France Travail
(1 051,92 / 3 506,40). Avant ce dépôt, seuls les 30 % d'année 1 étaient comptés :
c'est de là que viennent les +4,8 Md€ d'économie d'État et les +13,9 Md€ de
collectivités. La règle est portée à `methode/grille_lecture_budgetaire.md` et
tenue par le bouclage **`S17`, vérifié exactement, sans tolérance** — un rapport
qui cesserait d'être exact dirait que l'hypothèse a changé sans le dire.

**L'ordre des lots sort de `methode/a_trancher.md` : ce fil l'y a reformulé deux
fois, et les deux fois il l'a déformé.** Ce qui reste inscrit est le seul énoncé
de l'auteur — la sortie des fonctionnaires est un **bloc juridique**, elle se
résout **après** les parties faciles de la liasse. **C'est une position relative,
et elle ne se convertit pas en plan** : ce fil en a tiré « les parties faciles de
la liasse » comme lot suivant, ce qui n'était dit nulle part. *L'ordre des lots
revient au fil chef de file. Un fil rend son état et s'arrête.*

**Le socle se relit par déplacement d'adresses, prouvé avant d'être écrit.**
Chaque adresse déplacée — trois onglets en ` R`, deux renommés, un éclaté en
deux, les taxes de la ligne 17 à la 4, les dépenses fiscales de 21 à 7,
l'incidence de `L:P` à `S:W` — l'a été après confrontation cellule à cellule des
deux états : 0 divergence sur 278 lignes de taxe, 465 dépenses fiscales, 184
opérateurs, 777 ODAC-ODAL, 202 lignes de mission et de programme. **Aucun calcul
n'est touché.** *Tranché par Claude au titre d'A-23.*

**La clé d'un poste nommé devient une adresse de cellule.** L'ancien onglet
`Synthèse` portait les postes en paires libellé / valeur en colonne, d'où une clé
en numéro de ligne ; `SynthèseR` les porte en matrice. La clé devient `C20`,
`G21`, `F20` — **elle se vérifie à l'œil dans le classeur**, ce qu'un numéro de
ligne ne permettait pas. `tracer_economies.RATTACHEMENTS` est re-clé.
MaPrimeRénov' change de bloc au passage — des transferts aux ménages au détail
des opérateurs — sans que son montant bouge.

**Deux bouclages de S8 restent rouges et ne se corrigent pas.** La part
budgétaire de France Compétences (« sur FrComp. », 434,071252 M€) et celle du CNC
(« sur culture », 516,998084 M€) disparaissent avec le bloc des postes de
l'ancien onglet `Synthèse` ; la synthèse de restitution les range en « Autres ».
Les remettre par soustraction serait revenir au résidu que la grille refuse.
`S8` passe de 32/32 à **30/32**, et les deux échecs disent pourquoi.

**Une garde qui neutralise une règle dit désormais ce qu'elle a neutralisé.**
Les motifs `*Depenses_BG*` et `Synthese_Calculs*` du Makefile ne trouvaient plus
leur classeur, et `make` sortait vert sans la couche budgétaire ni l'arbre des
économies. Deux causes, pas une : les noms déposés changent à chaque millésime,
et `make` ne sait pas porter un chemin qui contient une espace. Les classeurs se
convertissent désormais sous cinq noms canoniques, et ce qui manque se dit.
*Question 21 traitée sur ce cas, non close en général.*

**Le `#VALUE!` de la catégorie 62 n'est pas au classeur, il est à la
conversion.** Les deux états portent la valeur en cache dans le `.xls`
d'origine — 15 282,129296 et 13 543,417778. Le recalcul `soffice` les casse :
une cellule sur l'état antérieur, deux sur les pièces du 20260917.
`methode/grille_lecture_budgetaire.md` l'attribuait au classeur ; l'attribution
est corrigée.

**Un écart de détail s'est déplacé sous la tolérance.** Les rubriques d'État
collaient à 77,9 contre 77,7 en tête ; elles collent maintenant exactement à
82,5. Les collectivités passent de l'exactitude à 53,5 contre 53,4. Les deux
restent sous la tolérance calculée (4 × 0,05 = 0,20), donc `S8` ne sonne pas.
**Une tolérance qui absorbe n'est pas une tolérance qui approuve** : l'écart est
inscrit à la grille.

**Trois lignes de taxe affectée manquaient au corpus depuis l'origine, et aucun
contrôle ne regardait.** La ligne « CNC et subventions culturelles » agrège trois
affectataires — le CNC, le Centre national de la musique, l'association pour le
soutien du théâtre privé, douze lignes, 749,8160514 M€. Le rattachement n'en
comptait qu'un, neuf lignes, 705,3350200 M€. **44,4810514 M€ hors compte.** Deux
aveuglements superposés : `S6` ne bouclait que trois affectataires isolés là où
la tête en nomme huit, et la tolérance **posée** du bouclage aval — 0,09 Md€ —
absorbait l'écart de 0,077667 qui en résultait. *Une tolérance posée n'a pas
seulement laissé du jeu : elle a laissé passer une omission de source.*

**`S6` se cale désormais sur l'onglet `Synthèse TA`, et il lit au lieu de
recopier.** Huit affectataires isolés, plus le total de la tête, tous bouclés
contre ce que le classeur affiche — les montants ne sont plus relevés à la main
dans le contrôle. Les libellés filtrants, eux, restent écrits en clair : c'est
eux qui doivent sortir en échec si un intitulé change. *Tranché par Claude au
titre d'A-23 ; la tolérance posée, elle, reste ouverte — question 15.*

### Dette d'appareil ouverte par ce fil

Quatre pièces de voie `depot`, au paquet
`methode/paquet_depot_ecart_20260917.md`, avec leurs diffs et une épreuve de
rejeu : `socle_budgetaire.py`, `controle_socle.py`, `tracer_economies.py`, le
`Makefile`, et `epreuve_s17_salaire.py` qui est neuf.

**Le paquet est un fork d'une base périmée et il le dit.** Le clone ne porte pas
le second cercle du socle : les diffs sont calculés contre la version à dix
bouclages, et les écraser détruirait `S11` à `S16`. L'ordre est écrit au paquet —
le second cercle d'abord, les diffs ensuite. *Le rejeu est éprouvé en salle
blanche : clone vierge, diffs appliqués, `make`, contrôle et épreuve rendent
exactement ce que le paquet annonce.*
## 20260917 — fil-application

**Le bouclage d'ensemble n'est pas un objet du corpus.** Le programme assume de
ne boucler qu'au total, jamais bloc par bloc. `B-05` et `B-07` restent
déséquilibrés et le disent ; aucune pièce ne dira ce qui finance quoi. Le relevé
des bilans déséquilibrés est donc un état définitif, non une liste de travaux.
*Tranché par l'auteur. Ancienne question 18 du registre.*

**Le nœud de mise en œuvre existe comme objet, et on en écrit un seul d'abord.**
Le gabarit se rédige, puis se remplit sur la sortie des fonctionnaires. Les six
autres attendent ce que ce premier aura coûté. Sept reste une proposition, pas un
décompte. *Tranché par l'auteur. Ancienne question 19.*

**Un terme qu'aucune pièce du corpus ne porte est à produire, non absent
définitivement.** Le verdict `absent` ouvre un travail, il ne clôt rien. Le seul
terme dans ce cas — la reprise par l'État des missions de solidarité
départementales — est un nœud de mise en œuvre. *Tranché par l'auteur. Ancienne
question 20.*

**Les fichiers cumulatifs du coffre s'écrivent par fragments datés.** Un fil
dépose `methode/fragments/<cible>/<AAAAMMJJ>-<fil>.md` ; `appareil/fragments.py`
assemble. L'historique, avant la ligne de marque, est repris verbatim et ne se
réécrit jamais ; la queue se régénère depuis les fragments, triés par date puis
par fil. L'assemblage est idempotent : deux fils qui l'exécutent en même temps
produisent le même octet. C'est ce qui rend le travail en parallèle possible.
Éprouvé sur six cas, dont l'ordre de dépôt et le double dépôt refusé. *Tranché
par l'auteur. Ancienne question 17.*

**Ordre des lots arrêté le 20260917** : second cercle du socle, puis le gabarit
du nœud et la sortie des fonctionnaires, puis le tri par véhicule.
## 20260917 — socle

**Un contrôle neuf porte son jeu de fautes et son jeu de justes.** Les sept
bouclages du second cercle du socle sont livrés avec
`appareil/epreuve_controle_socle.py` : quatorze socles blessés d'une seule façon,
qui doivent chacun lever leur code, et sept socles modifiés légitimement, qui ne
doivent rien lever. Un contrôle qui n'a jamais rien attrapé ne prouve pas qu'il
regarde ; un contrôle qui hurle sur tout ne prouve pas qu'il discrimine. *Pris
faute de réponse à la question 11 du registre, et inscrit à la grille de lecture
budgétaire.*

**La tolérance d'un bouclage se calcule, elle ne se règle pas.** Le classeur
arrondit chaque colonne au dixième de milliard à l'affichage : une somme de `n`
lignes peut dériver de `n × 0,05`, et c'est ce produit qui fait la tolérance. Une
tolérance posée à la main se remonte pour faire tomber un compte ; une tolérance
calculée ne le peut pas.

**Un document du coffre que personne n'a classé se classe par son adresse.**
`generer_carte.py` porte désormais une règle de dossier, essayée après la ligne
de carte et après la règle de rang : `methode/` et `reference/` sont de la
méthode, `referentiels/` des grilles, `livrables/` du bac à sable, `archive/` et
`input/` des références internes. **C'est une règle d'adresse, pas un jugement de
contenu** — une ligne de carte la contredit toujours, et c'est ce que fait un fil
qui a ouvert le document. Motif : un fil Cowork verse au coffre et ne peut pas
pousser le générateur (A-393) ; sans cette règle, `controle_index.py` refusait
l'artefact faute de famille, ce qui interdisait de l'y porter sans l'avoir
ouvert — et il disparaissait au premier `make reindex`.

**La table curée avait quarante-cinq artefacts de retard sur le coffre**, relevé
mécaniquement le 20260917 en confrontant la sortie de `generer_index.py` à
l'index restauré et à la liste des documents du projet : seize étaient à l'index
sans être à la table, vingt-neuf n'étaient nulle part. Les quarante-cinq sont
portés en un passage. **Le registre n'en réclamait que quatre** — c'est la mesure
qui a dit les quarante et un autres, et c'est le troisième constat du même genre
après A-364 et A-381.

**Une règle gardée qui ne trouve plus son fichier est du même genre qu'un
contrôle aveugle.** Deux motifs du fichier de construction ne trouvaient plus
leur classeur — `Depenses_BG` contre `Depenses_2026_du_BG`, `Synthese_Calculs`
sans accent contre un nom qui en porte deux. Rien ne cassait : la règle était
gardée, et le socle se refaisait sans la couche budgétaire ni l'arbre des
économies. Les deux motifs sont élargis. **Une garde qui empêche de casser
empêche aussi de voir**, et cela vaut inscription.

**L'onglet `Perdants` porte deux natures de lien, et une seule se somme.** Toutes
ses lignes écrivent « Dont » et aucune ne dit de quoi. Une **partition** épuise sa
tête et se rejoue ; un **sous-ensemble** — les agents publics dans les
travailleurs, les résidents en logement social à travers toutes les têtes — n'en
épuise aucune et ne se somme à rien. Les confondre aurait fait sortir en échec un
dénombrement croisé. La distinction est déclarée au socle, et le jeu de justes la
vérifie.

**Une feuille de vue s'importe quand elle porte la seule écriture d'un
paramètre.** `GraphAFU` est une feuille de graphique, et la grille dit qu'une vue
n'est pas une source. Elle est importée quand même : c'est le seul endroit du
corpus où la dotation par enfant est écrite. Le bouclage `S17` en rejoue les deux
lignes qui **dérivent** de l'onglet `CI unique`, et **nomme comme posés** les
paramètres qu'aucune dérivation ne produit, plutôt que de faire croire qu'il les
prouve. Le jeu de justes vérifie qu'en déplacer un ne lève rien.

**`appareil/trois_colonnes_regle_dor.py` est déclaré à `COFFRE_DOCUMENT`.** Écrit
par un fil Cowork le 20260908 et versé au coffre faute de pouvoir être poussé,
c'est exactement le cas que la table prévoyait depuis qu'elle a été vidée le
20260909. `coffre.py dette` le réclame désormais en `D3`.

**Un fil de travail ne se donne pas son successeur.** Ce fil a écrit le prompt du
lot suivant et y a tranché deux questions de fond — un nœud de mise en œuvre
est-il un artefact à part, l'onglet `Capitalisation` s'importe-t-il. **C'était une
faute**, relevée par l'auteur le jour même : l'ordre des lots est de l'auteur, et
c'est au fil chef de file de dicter la suite — quel fil s'ouvre, sous quelle
forme, avec quel mandat. `methode/prompt_fil_noeud_mise_en_oeuvre.md` est ramené
à *proposé, non validé*, et les deux arbitrages sont ressortis en questions 23
et 24 de `methode/a_trancher.md`. *La frontière : la tambouille se tranche —
appareil, index, nommage, ordre d'exécution ; le mandat du fil suivant, non.*
## 20260921 — digestion-archives

### A-410 — Une unité qui porte plusieurs éléments se classe sur celui qui manque

*Tranché par Claude au titre d'A-23.* Le prompt du fil pose trois cases —
`digérée`, `reformulée`, `absente` — et laisse leur frontière ouverte sur une
unité qui porte plusieurs éléments. La frontière décide du verdict, donc elle se
tranche avant de compter.

**`digérée`** : l'énoncé se retrouve tel quel, ou à la valeur près, dans une
pièce vivante nommée. **`reformulée`** : le fond s'y retrouve sous une autre
forme, ou sous une autre valeur qui l'a remplacé — `R-ARG066` porte 100 Md€
d'économie sur 1 700 quand le manuscrit porte 236 sur 1 714, et c'est le même
énoncé à une génération de chiffrage près. **`absente`** : l'unité est classée
sur l'élément qui manque, non sur ceux qui se retrouvent.

Un fait, un chiffre, un exemple nommé, une affirmation sont des éléments ; une
image ou une tournure n'en sont pas. Sans quoi `R-ARG020` — « trop d'État a tué
l'État », titre de section au manuscrit — sortirait absente pour un coq sur un
tas de boue.

*Ce que la règle sert* : celle de l'auteur, *on garde une archive tant que son
contenu n'est pas digéré ailleurs*. Le contenu d'une réserve d'arguments, ce sont
ses exemples nommés — `R-OBJ043` récite Saint Louis, Philippe le Bel, le système
de Law et les 45 centimes de 1848 là où le manuscrit résume « une quinzaine de
dévaluations depuis Clovis ». Le résumé n'est pas la digestion de la liste.

### A-411 — Un référentiel qui n'est ni au coffre ni au dépôt se lit par ses générateurs

*Tranché par Claude au titre d'A-23.* `referentiels/positions.json` porte la
matière contre laquelle l'input gagnants-perdants devait se confronter, et il
n'est nulle part : `coffre: false` à l'index (A-16), absent du dépôt puisqu'il se
régénère. Le lire supposerait de rejouer la chaîne, ce qu'un fil de vérification
n'a pas à faire.

**Ce qui se lit à sa place est ce qui l'écrit** : `construire_positions.py` pour
les catégories, les groupes et l'éventail, `justifications.py` pour les
justifications et les relais, `apports.py` pour les apports et les
contreparties, `structure_fiches.py` pour la sélection. Ces quatre modules sont
au dépôt, ils portent la matière écrite à la main, et le reste du référentiel se
dérive du `REF_doctrine`, qui y est aussi.

*Corollaire tenu* : les livrables `extrait_gagnants_perdants.html`,
`inventaire_gagnants_perdants.html` et `galerie_fiches.html` n'ont pas été
interrogés. Ce sont des dérivés des mêmes pièces ; les interroger serait les
interroger deux fois et gonfler le compte des digestions d'autant.

### A-412 — Une vérification de digestion est mécanique, et elle déclare ses passes

*Tranché par Claude au titre d'A-23.* « Un contrôle annoncé est un contrôle
mécanique » vaut ici comme ailleurs, et une recherche de digestion faite à l'œil
sur 219 unités serait une inspection présentée comme une preuve.

**Trois passes, et il en fallait trois.** Les 5-grammes littéraux sur le texte
normalisé attrapent la reprise verbatim. Les trigrammes de mots pleins attrapent
la reprise à mots outils près. La co-occurrence des deux termes les plus rares
d'une unité dans une fenêtre de 500 caractères attrape ce que les deux premières
manquent.

*Et la première version a manqué une digestion évidente*, ce qui vaut d'être
écrit : la passe par trigrammes de mots pleins retirait « fait » et « peut » de
son vocabulaire, et ne voyait donc pas que « Ce que la démocratie a fait, elle
peut le défaire » est au prologue du manuscrit, mot pour mot. **Une liste de mots
vides taillée pour la pertinence coupe aussi la preuve.** C'est la passe sur le
texte entier, sans retrait, qui l'a trouvée.

Ce que les passes sortent n'est jamais un verdict : c'est une liste de
candidats, lue une à une. A-35 tient — deux textes qui partagent des mots ne
parlent pas forcément de la même chose.
## 20260921 — purge-a-trancher

### A-413 — La doctrine reprend 82,5 et 53,4, en une passe dédiée

*Tranché par l'auteur le 20260921 — question 30 de `methode/a_trancher.md`.*
L'origine des +4,8 Md€ d'État et des +13,9 Md€ de collectivités est mesurée : la
masse salariale compte en totalité, 30 % en année 1 et 70 % au solde, et `S17`
le vérifie sans tolérance. Restait la conséquence éditoriale — le manuscrit, les
fiches et le site portent encore 77,7 et 39,5.

**Une passe dédiée, tout de suite. Les trois avals basculent d'un coup**, non au
fil des régénérations. Le total général ne bouge pas — 236,054667 Md€ — ; ce sont
les deux totaux de tête qui bougent sans lui, et deux totaux de tête qui ne
concordent pas entre le classeur et le livre sont une faute visible par le
lecteur.

*Ce que la décision ouvre* : un lot, dont le mandat est de l'auteur. Un fil ne
se donne pas son successeur.

### A-414 — Les deux écarts de valorisation du patrimoine sont clos

*Tranché par l'auteur le 20260921 — question 27.* La doctrine et le classeur
disent la même chose : **3 % de rendement**, et **600 Md€ à restituer** — les
20 000 € par foyer — sur **606,972666 Md€ valorisés**.

**La marge de 6,97 Md€ n'est pas un écart résiduel : c'est la prudence
assumée.** On valorise un peu plus qu'on ne promet, donc la promesse tient même
si la valorisation se révèle haute. Le premier écart — 3 % annoncés contre 2,9 %
appliqués — était réel et il est refermé par les classeurs du 20260917 ; le
second n'en était pas un.

*Porté* : `methode/grille_lecture_budgetaire.md` ne relève plus ces deux points.

### A-415 — Le corpus passe au vocabulaire du 20260917, et l'ancien disparaît

*Tranché par l'auteur le 20260921 — question 26.* Six termes ont été requalifiés
dans quatre classeurs sur six, **à valeurs identiques à l'octet** : « gage CSG »
devient « économie à horizon 1 an », « économie pérenne en sus » devient
« économie supplémentaire », « effet macro » devient « solde PO », « suppression
immédiate » devient « champ non indispensable », « CI unique » devient « aide
fondamentale universelle », « niches supprimées » devient « niches restituées ».

**Pas de table de concordance vivante : la grille passe au nouveau.** C'était le
point qui demandait un arbitrage et non un renommage — « effet macro » et
« solde PO » ne disent pas la même chose du même nombre, et choisir le second
est un jugement de fond.

**Partage tenu à l'écriture, et il est de la tambouille** *(A-23)* : **la
bascule porte sur le vocabulaire, pas sur les adresses.** Un onglet qui a changé
de nom, une en-tête qui a changé de ligne, une plage qui a bougé restent notées
avec leur état antérieur — ce sont des faits vérifiables sur où la matière vit,
et `appareil/socle_0910.py` en dépend. Les libellés antérieurs quittent la
grille et vivent là, avec les adresses de la même génération.

*Porté* : `methode/grille_lecture_budgetaire.md` réécrit le 20260921 — vingt et
un remplacements, un tableau de concordance en tête qui dit d'où l'on vient, et
plus aucun ancien terme dans le corps.

### A-416 — Le contenu de `Manifeste` et `Perdants` est gardé, et son porteur est nommé

*Tranché par l'auteur le 20260921 — question 29.* Les deux onglets disparaissent
des classeurs du 20260917 **parce qu'ils ont été retirés pour la présentation,
non parce qu'ils étaient caducs**. La consigne est de garder le contenu.

**Mesure avant travail, et elle change la réponse : le contenu est déjà gardé,
intégralement.** `livrables/extrait_classeurs_anterieurs_20260917.md` en porte
la recopie mécanique cellule à cellule — `Manifeste` 35×13, la ventilation des
baisses de dépense par catégorie de perdant, 183,954667 Md€ au total ;
`Perdants` 16×8, le dénombrement des populations et des perdants à 1 an et à
3 ans, 68 M résidents, 17 M retraités dont 4,3 M perdants, 5,8 M agents publics
dont 0,54 M, 10,4 M HLM dont 3,5 M. Le document dit lui-même sa raison d'être :
*« il existe pour qu'ils puissent sortir des pièces jointes sans perte »*.

**Ce qui restait à faire n'était donc pas une extraction mais une
déclaration** : ce document est le porteur durable, et **`S15` et les deux
entrées de `REF_chiffres` qui citaient `Manifeste` — 236 Md€/an et 30 Md€/an —
se sourcent désormais à lui**, non plus à un onglet de classeur.

*Règle qui se dégage, et qui vaut au-delà du cas* : **avant d'exécuter une
consigne de conservation, on mesure ce qui est déjà conservé.** Rejouer une
extraction déjà faite aurait produit une seconde copie, donc deux vérités pour
un même chiffre — exactement ce que le principe du point de vérité unique
interdit.

### A-417 — Le bouclage d'ensemble n'est pas un objet du corpus

*Tranché par l'auteur le 20260917 ; porté au registre le 20260921, la question
17 ayant donné sa règle de concurrence.* Le programme assume de ne boucler qu'au
total, jamais bloc par bloc. `B-05` et `B-07` restent déséquilibrés et le
disent ; aucune pièce ne sera écrite pour dire ce qui finance quoi.

*Conséquence tenue* : les deux bilans du lot C sont clos en l'état, et le relevé
des bilans déséquilibrés est un état définitif, non une liste de travaux.
*(ancienne question 18 de `methode/a_trancher.md`)*

### A-418 — Le nœud de mise en œuvre existe comme objet, et on en écrit un seul d'abord

*Tranché par l'auteur le 20260917 ; porté au registre le 20260921.* Le gabarit
se rédige, puis se remplit sur la sortie des fonctionnaires — le seul nœud du
premier lot. Les six autres attendent ce que ce premier aura coûté. **Sept reste
une proposition, pas un décompte.** *(ancienne question 19)*

### A-419 — Un terme qu'aucune pièce du corpus ne porte est à produire, non absent définitivement

*Tranché par l'auteur le 20260917 ; porté au registre le 20260921.* Le verdict
`absent` du relevé de comblement ouvre un travail ; il ne clôt rien. Le seul
terme dans ce cas au 20260917 — la reprise par l'État des missions de solidarité
départementales, que `B-03` suppose — est un nœud de mise en œuvre, et il
rejoint la file derrière la sortie des fonctionnaires. *(ancienne question 20)*

### A-420 — Les « nœuds de mise en œuvre » sont des blocs de travail juridique préidentifiés, et rien de plus

*Tranché par l'auteur le 20260921 — question 23, et elle se dissout.* Interrogé
sur la forme de l'objet, l'auteur ne reconnaît pas le terme : *« si c'était les
nœuds juridiques, alors c'est juste des blocs de travail juridique à venir
préidentifiés »*.

**C'est la réponse, et elle annule la question.** Il n'y a ni famille
d'artefacts à créer, ni gabarit à rédiger, ni contrôle de gabarit à écrire. Ce
sont des chantiers, ils vivent à `methode/carte_des_chantiers.md` et au plan de
bataille, et ils produiront ce que produit un chantier — pas un objet de corpus
d'un type nouveau.

*Conséquences tenues* : `methode/prompt_fil_noeud_mise_en_oeuvre.md` est
**caduc** ; la question 24 se repose sur ses propres mérites et non comme une
dépendance du gabarit ; `A-419` reste vrai — un terme qu'aucune pièce ne porte
est à produire — mais il rejoint la file des chantiers juridiques, sans
qualification d'objet.

**Signalement, au titre du garde-fou qui interdit de porter en validé ce que
l'auteur n'a pas dit.** `A-418`, porté au registre le 20260921, énonçait que *le
nœud de mise en œuvre existe comme objet* et l'attribuait à l'auteur au
20260917. **Cette attribution est douteuse** : le terme est né le même jour dans
un prompt de Claude marqué *proposé, non validé*, et l'auteur ne le reconnaît
pas quatre jours plus tard. `A-418` est donc **réduit à ce qui tient** : on
traite un chantier à la fois, la sortie des fonctionnaires d'abord, et « sept »
reste une estimation jamais énumérée — le corpus n'en nomme que deux.

*Ce que la faute enseigne* : un concept forgé par un fil pour son propre usage
se lit comme du vocabulaire acquis dès le lendemain, et une question de forme
posée dessus n'a pas de réponse parce qu'elle n'a pas d'objet. **On ne demande
pas à l'auteur d'arbitrer la forme d'une chose qu'il n'a pas demandée.**

### A-421 — L'onglet `Capitalisation` s'importe au socle, avec son bouclage

*Tranché par l'auteur le 20260921 — question 24.* Il porte l'horizon de sept ans
de la sortie des fonctionnaires, et il était le dernier onglet du classeur de
calculs que le second cercle n'avait pas importé.

**Il s'importe, et avec bouclage** — un lot d'appareil sur le modèle des sept
bouclages neufs, avec son jeu de fautes et son jeu de justes. Le terme cesse
d'être `estimé`. *L'argument qui portait : un chantier bâti sur un chiffre sans
garde-fou est un chantier qu'il faudra refaire.*

### A-422 — La part budgétaire de France Compétences et du CNC se retire

*Tranché par l'auteur le 20260921 — question 28 : « on peut retirer, on
reconstruira au besoin ».* Le bloc des postes nommés qui portait « sur
FrComp. » — 434,071252 M€ — et « sur culture » — 516,998084 M€ — a disparu au
dépôt du 20260917, et rien ne les remplace. Mesuré : aucune combinaison à un ou
deux termes des 2 810 valeurs du socle ne les atteint, et le projet annuel de
performance ne peut pas les rendre — la subvention y est à la maille du
programme, et les deux programmes sont partagés.

**Elles se retirent, elles ne se reconstruisent pas.** Les deux bouclages de
`S8` qui les visaient sont **retirés**, non laissés en échec : un bouclage qui
porte sur une grandeur que le corpus ne revendique plus n'a pas d'objet. Les
deux lignes du chiffrage restent ce que le classeur les donne — 10,6 et
1,3 Md€ —, et leur décomposition s'arrête aux taxes affectées.

**Ce qui n'est pas fait, et qui se dit** : la remettre par soustraction serait
revenir au résidu, et *un résidu n'est pas une source*. Si le besoin revient, la
voie est nommée — le budget initial 2025 de France Compétences (A-113) pour le
premier, et l'auteur pour le périmètre de « sur culture ».

### A-423 — `S16` reste sur le millésime du classeur DEPP en vigueur

*Tranché par l'auteur le 20260921 — question 31.* Le classeur de la dépense
d'éducation est le seul des sept antérieurs à n'avoir pas eu de successeur au
20260917. **Ce n'est pas un retard : le millésime reste valable et on le
garde.** `S16` continue de boucler dessus, et son absence du dépôt du 20260917
cesse d'être un signalement.
## 20260921 — rapprochement-proto

**Le livre et ses annexes prévalent.** *Tranché par l'auteur le 20260921, en
réponse aux questions 34, 35 et 36.* Le proto vient de
`Données_Résolution_0112.docx`, antérieur aux classeurs `0819` comme à ceux du
`0910` : **là où il diverge du livre, c'est lui qui est périmé**, et cela sans
réexamen au cas par cas. La règle ferme les trois questions d'un coup et elle
vaut au-delà d'elles — c'est une règle de préséance entre strates, non une
décision sur trois chiffres.

*Conséquences opposables, écrites et jouées le jour même.* **Une** : le groupe
`postes publics facultatifs supprimés` porte désormais `P-D-102` et un bloc
`arbitrage` retenant `R-D6-2-1-p1` ; joué, `F7` reste vert, la discordance se
range en décision et **l'écart reste visible au contrôle** au lieu d'être effacé.
On retient 580 000 postes et −10 % des effectifs. **Deux** : le taux de
couverture des retraites du corpus est 69,3 % et son déficit spontané 125 Md€ ;
les 73 % et les 106 Md€ du proto sont périmés. **Trois** : le corpus retient son
décompte des 1 104, dont 434 agences nationales ; les 431 opérateurs de la liste
du PLF 2026 restent du contexte de sous-jacent.

**Une contradiction close au fond peut rester inécrivable, et il faut le dire.**
`P-D-067` oppose 106 Md€ aux 125 Md€ du corps du livre. La règle la tranche, mais
**les 125 Md€ ne sont entrés dans aucune entrée du référentiel** — le relevé de
reconfirmation les classe `absent` — et un groupe `MEME_QUE` apparie des entrées.
*Elle s'écrira quand le corps du livre entrera au référentiel, ce que la question
33 a déjà décidé et qui reste un travail. D'ici là, la décision vit au registre et
pas à la table, et c'est un endroit de moins où le contrôle la voit.*

**Un dénombrement ne se force pas en groupe pour avoir l'air arbitré.**
`P-D-035` — 431 opérateurs du PLF — et `R-D2-2-1-p1` — 750 agences sur 1 104, dont
434 nationales — ne portent pas le même objet en tête. Les apparier pour poser un
bloc `arbitrage` aurait donné un contrôle rassurant sur un rapprochement faux.
*La règle de l'auteur tranche au fond ; la table ne porte que ce qui s'apparie.*

**Le fait se nomme depuis l'énoncé du candidat, jamais depuis sa valeur de
tête.** Le relevé mécanique de `generer_ref_chiffres.py` met en tête le premier
nombre lisible de la ligne, qui est souvent un millésime ou un ordinal :
`P-D-026` porte « 1 », qui est le « 1er » de « 1er janvier », et `P-D-099` porte
« 2024 ». Classer sur la tête aurait rangé ces candidats en non-grandeurs et
perdu deux rapprochements réels. **La tête décalée se relève en remarque**, elle
ne commande pas la case. *Tambouille — ne remonte pas à l'auteur.*

**Un candidat dont l'énoncé ne porte aucune grandeur sort en `sans vis-à-vis` et
se déclare « non-grandeur ».** Fragment d'adresse web, millésime d'une décision,
en-tête de colonnes, ordinal de décile, note de lecture d'un tableau, numéro de
rapport. Ils ne se requalifient pas ici : c'est la question 32, ouverte côté
notes le 20260921 et désormais ouverte côté proto. *Les distinguer dans la
remarque évite qu'on relise 78 `sans vis-à-vis` comme 78 faits que le corpus
ignore, alors qu'une part d'entre eux n'est pas un fait.*

**La table `MEME_QUE` ne porte que des groupes concordants.** Un groupe
contradictoire sans bloc `arbitrage` fait sortir `F7` en échec, et rendrait
`make controle` rouge pour une question de fond que l'auteur n'a pas tranchée.
Le groupe de `P-D-102` est donc rédigé, motif compris, et **laissé hors de la
table tant que l'arbitrage n'est pas pris**. *Un fil de travail n'échange pas un
contrôle vert contre une décision qu'il n'a pas le droit de prendre, et il ne
prend pas non plus la décision pour garder le contrôle vert.*

**Un rapprochement qui ne tient que par une tolérance posée n'est pas un
rapprochement.** Le groupe « population de la France » — `R-D7-2-1-p1` et
`P-D-026` — a été écrit, appliqué et joué : il sort en `DISCORDANCE`, « aucune
valeur commune », et ne passe qu'avec une tolérance posée à 0,6 M, l'écart entre
l'arrondi du corpus et le millésime 2025 du proto. **Retiré**, et `P-D-026`
reclassé en divergence d'hypothèse. *La question 15 a déjà mesuré ce que coûte
une tolérance posée : 0,09 Md€ avaient masqué trois lignes de taxe affectée. Une
tolérance qui existe pour faire passer un groupe est la faute que tout ce
dispositif cherche à empêcher — et l'écrire au motif ne la rend pas moins
fausse.* **La leçon générale, et elle est neuve : un groupe se joue avant d'être
proposé.** Deux des trois rapprochements de ce fil ont tenu, le troisième non, et
seule l'exécution le disait.

**Une correction à `SOURCES` qui ne corrige qu'à moitié ne s'écrit pas.** La tête
de `P-D-026` est fausse — le relevé a pris le « 1 » de « 1er janvier ». Une
entrée `SOURCES` a été écrite sur le modèle de `P-D-020` : elle change `valeur`
et `unite`, **jamais `valeur_num`**, que le contrôle est seul à lire. Elle
rendait donc la fiche lisible et le contrôle inchangé. *Retirée. Le défaut est
relevé au livrable et rejoint la famille de la question 32.*

**Un calcul qui retombe juste n'est pas un rapprochement.** `P-D-005` porte le
rendement d'un point de CSG à 11,8 Md€, et `R-D3-2-1-p4` divisé par
`R-D3-2-1-p5` rend 11,75. Aucune entrée du corpus ne porte le fait « rendement
d'un point » : le candidat sort donc en `sans vis-à-vis`, avec le calcul en
remarque. Même règle pour les sommes qui bouclent — `P-D-061` + `P-D-062` = les
30 Md€ de `R-D8-3-1-e2`. *C'est la règle du corpus appliquée au sens inverse :
une opération rejouée dit que le compte est juste, non qu'il y a rapprochement.*

**Une déclinaison qui a un vis-à-vis ne fait pas basculer la case du candidat.**
`P-D-104` porte en tête 1,5 million de ménages, que le corpus ne dénombre pas,
et en déclinaison les 180 €/mois d'avantage de loyer et l'écart de taux d'effort
de 10 points, tous deux au manuscrit. La case suit le fait de tête ; **les
déclinaisons rapprochées se disent en remarque** plutôt que de se perdre.

**Le proto se relève contre lui-même, et rien de plus.** Quatre divergences
internes sont inscrites au livrable — mutuelles, revenus déclarés, CSG hors
activité, et une valeur portée deux fois sous deux identifiants. Ce fil n'était
pas mandaté pour auditer le proto ; **mais une pièce qu'on cite comme source de
source doit être cohérente**, et taire ces quatre écarts aurait laissé croire
qu'elle l'est. *Relevé, non tranché, et le proto n'est pas réécrit : c'est une
archive.*

**Un cumulatif volumineux se restaure par un fil auxiliaire qui sert de tuyau, et
la voie est éprouvée.** `methode/journal.md` et `methode/arbitrages.md` font
ensemble 597 ko : les lire au fil principal aurait mangé son contexte pour rien.
Un fil auxiliaire les a lus sans rien écrire, et le coffre les a rendus **comme
fichiers locaux** — donc par `cp`, la première des trois voies, sans passer par
le modèle. Les treize fragments, eux, sont revenus en texte au transcript.
*Conséquence opposable : la restauration d'un cumulatif ne coûte plus le
contexte du fil qui assemble.*

**Neuf fragments sur quinze ne sont pas à l'index, et `restaurer.py` ne sait donc
pas les placer.** Ils ont été écrits par `moisson()` à leur propre chemin, le
chemin au coffre et le chemin au dépôt étant identiques pour un fragment. *C'est
une copie d'octets, pas une reconstitution ; mais c'est un contournement, et il
mesure ce que la dette de table curée coûte déjà.* **Un fil qui assemble sans le
savoir perdrait neuf fragments en silence** — c'est exactement ce qui est arrivé
au fil de purge, qui a assemblé sans les deux fragments de ce fil.

**L'index n'est pas régénéré**, pour le motif déjà inscrit : `generer_index.py`
au clone est antérieur aux quarante-cinq artefacts portés le 20260917, et un
`make reindex` d'ici les perdrait. Les trois pièces nées de ce fil sont dues à la
table curée.
## 20260921 — reconfirmation-chiffres

**Le relevé est mécanique, et son outil reste à l'atelier.** Le prompt du fil
interdit toute pièce qu'il ne nomme pas. Les trois scripts qui relèvent,
confrontent et rendent ont donc été écrits hors du corpus et n'y entrent pas.
**Conséquence assumée : le relevé n'est pas rejouable en l'état.** Ce qui le rend
reproductible est écrit au livrable — les règles d'exclusion, la règle de
comparaison, la tolérance — et suffit à le réécrire à l'identique.
*Tranché par Claude au titre d'A-23.*

**Ce qui n'est pas un chiffre du manuscrit, et que le relevé écarte.** Une année
seule sans unité — c'est une date ; un numéro d'article, d'alinéa, de page, de
décret, de loi ou de rapport ; un quantième de date ; un ordinal ; le nombre d'un
nom propre (`CAC 40`). Sans ces quatre règles, le relevé comptait 374 entrées
dont un quart de renvois. *Tambouille — ne remonte pas à l'auteur.*

**Une somme d'argent ne se compare qu'à une somme d'argent.** L'échelle — €, M€,
Md€ — ne se devine pas : un `7` nu du manuscrit ne vaut pas `7 Md€/an` au
référentiel. Sans cette règle, le rapprochement produisait des appariements faux
et silencieux. Les autres unités restent permissives, le proto n'en déclarant
souvent aucune.

**L'égalité de deux valeurs est relative, à 0,5 %.** Le manuscrit arrondit là où
le classeur porte la décimale — 236 contre 236,054667. Une égalité stricte
aurait mis en `absent` des chiffres que le référentiel porte. *La tolérance est
de lecture, non de calcul : elle ne referme aucun écart, elle évite un faux
écart de notation.* Question 15 non touchée.

**Une divergence se relève dans le sens où elle est lisible.** La table du
manuscrit va du manuscrit vers le référentiel, comme le prompt le demande ; mais
une entrée du référentiel peut porter une valeur qu'aucun chiffre de son ancrage
ne porte, et cela ne se voit d'aucun chiffre du manuscrit. Le relevé fait donc
une **passe inverse par ancrage** — code de note, code de preuve — et non par
ressemblance de texte, qui appariait faux sur les énoncés courts.

**L'appariement hors ancrage se fait sur le libellé entier de l'entrée**, et non
sur son seul énoncé : `intitulé`, `fait partagé`, `rubrique` et énoncé
ensemble. Les énoncés de `ref_doctrine` sont des formules — « 236 Md€/an »,
« 750 agences » — sur lesquelles aucun recouvrement de mots ne se calcule.

**Un ordinal se reconnaît au suffixe collé au nombre, pas au mot suivant.** Le
premier jet du relevé testait les deux caractères suivants après suppression des
espaces : tout nombre suivi d'un mot commençant par `re` ou `er` — « 25 m2
renseignée » — tombait en ordinal et disparaissait sans bruit. **Deux chiffres
perdus sur 311, dont `25 m²` à la note e114.** Corrigé : le suffixe doit coller
au nombre. *Le défaut ne se voyait d'aucun compte : c'est un relevé qui
disparaît, non un relevé qui échoue.*

**Les onglets `Manifeste` et `Perdants` ne sont pas rouverts.** La question 29 de
`methode/a_trancher.md` les porte déjà ; ce fil ne fait que relever les neuf
sources concernées, sans en réécrire aucune.

**Le référentiel des faits couvre tout chiffre du livre.** *Tranché par l'auteur
le 20260921.* Tout nombre imprimé au manuscrit — corps et notes de fin — a
vocation à être un fait du corpus, traçable à sa source, et non plus seulement
les chiffres du plan. Le relevé du 20260921 en mesure la portée : **225 chiffres
sur 311 n'ont aujourd'hui aucune entrée**, et six grandeurs de notes de fin
échappent au détecteur d'`extraire_notes.py`. *Conséquence opposable, inscrite
avec l'arbitrage : le périmètre du référentiel n'est plus celui du détecteur de
notes, et `generer_ref_chiffres.py` ne peut plus le produire seul — le corps du
livre n'est source d'aucune de ses trois provenances.* **Question 33 close.**

**Le proto Données n'est pas un rebut : c'est un sous-jacent, et il vaut source
de source.** *Tranché par l'auteur le 20260921.*
`sources/Donnees_20260806_v1_proto.html` a servi d'appui à des chiffres du
corpus ; peu ont évolué depuis. Ses candidats se conservent dès lors qu'ils ne
**contredisent pas** la doctrine, et ils se citent là où le contexte manque.
**C'est une catégorie à part, du même genre que les classeurs annexes** — une
pièce nommée et datée, non un candidat en attente de source.

*Conséquence opposable, mesurée le jour même.* « Non contradictoire » suppose un
rapprochement, et le corpus a déjà tranché qu'un rapprochement **ne se devine
pas** : il s'écrit à la main, par `meme_que`, et `F7` ne contrôle que ce qui a
été rapproché. **Six des 93 candidats sont rapprochés aujourd'hui.** Trois
confirment exactement le corpus — `P-D-059` (6 mois d'indemnisation),
`P-D-060` (30 Md€ de chômage basculés), `P-D-078` (16,9 Md€ de frais de gestion).
Deux — `P-D-006` et `P-D-012` — portent « 2024 » comme valeur : c'est le défaut
de relevé des onze entrées de la question 32, pas une contradiction. Un —
`P-D-100` — oppose un pourcentage à des Md€/an, ce que `controle_chiffres`
signale déjà en unités divergentes. **Zéro contradiction de valeur.** Les 87
autres n'ont aucun vis-à-vis : ils ne contredisent rien, et la règle les
conserve tous.

*Une tentative d'appariement automatique a été jouée et elle est écartée* : au
seuil de recouvrement de 0,30, elle sort 38 « contradictions » dont l'examen
montre qu'elles opposent un millésime à un pourcentage. **Elle confirme
l'arbitrage du corpus plutôt qu'elle ne l'entame** — le rapprochement ne se
devine pas.

*Proposé, non validé — le statut technique du sous-jacent.* Un champ `role`
valant `sous-jacent`, la confiance laissée à 0 et `a_sourcer` mis à faux : ces
chiffres ne sont pas en attente de source, ils ont la leur, qui est le proto.
**Ce point touche la règle de diffusion** — « un chiffre de confiance nulle ne
sort dans aucun livrable diffusable » — et il faut l'écrire : un sous-jacent se
cite comme source de source dans une note de méthode, jamais comme grandeur dans
un livrable diffusable. *La règle de diffusion est de l'auteur ; elle n'est pas
tranchée ici.*

---
## 20260923 — manifeste

**Tranché par l'auteur le 20260923, sur le fil de révision du manifeste.**

**Politique des chiffres en livrable de diffusion.** Un chiffre **compatible avec
la doctrine** passe ; il n'a pas à être cité au corpus pour être écrit. Ce qui
bloque est l'incompatibilité, pas l'absence de citation. *Conséquence
immédiate : 303 agences, division par dix du volume de réglementation, 50 fois,
2 000 CERFA sont maintenus au manifeste.*

**Le dénominateur par défaut d'un ratio de dépense est le grand État** —
l'ensemble des dépenses publiques —, non le budget de l'État seul. Les 6 % du
régalien s'écrivent donc « 6 % des dépenses publiques », là où le livre écrit
« 6 % de ses dépenses ».

**Le texte du manifeste est une source, non un proto corrigé.** Le texte arrêté
du 20260923 rend caduques les onze corrections et la non-correction déclarée
d'`appareil/manifeste.py`. L'entorse signalée par `methode/passation_site.md` le
20260904 — un module qui porte à la fois le rendu et le fond — se ferme à cette
occasion.

**Le vocabulaire « suppression » est banni du registre de diffusion**, sauf là où
il désigne l'acte sur un impôt nommé — la suppression de la CSG et de la CRDS.
Une soustraction se dit par ce qu'elle rend.

**Le mot « euros » s'écrit en toutes lettres**, le symbole € ne se substitue
jamais au mot. Alignement sur le livre.

**Les sept missions s'amènent en trois axes** — sécurité, solidarité, éducation —
et non en énumération des sept. Le chiffre de tête est « 7 ministères au lieu de
35 », en chiffres.

---

**Faute de méthode relevée le même jour, et portée en mémoire projet.**
`livre/texte_livre.json` est le **corps** du livre — 180 folios, EP3 —, **pas le
livre entier** : les annexes n'y sont pas. Un chiffre absent d'EP3 n'est donc pas
un chiffre absent du livre. La division par dix et les 303 agences sont aux
annexes. Le verdict juste est « absent d'EP3 », suivi d'une recherche aux
annexes, jamais « non sourcé ».

---
## 20260923 — passe-825-534

**Tambouille tranchée par le fil de la passe 82,5 / 53,4, et inscrite.**

**Un relevé porte la date de sa production, pas celle de son mandat.** Le mandat
est du 20260921, le relevé du 20260923 : c'est ce dernier qui vaut, parce que
c'est l'état qu'il mesure.

**Un motif de relevé numérique porte ses deux gardes.** Rien avant un chiffre,
une virgule ou un point ; rien après un chiffre. Sans elles, `177,93 €` de
`REF_doctrine`, `rgba(177,57,15)` de `generer_interface.py` et `1977.37164` de
l'extrait des classeurs sortent en occurrences de 77,9 et de 77,5. **Trois faux
ont été rencontrés dans ce fil et écartés mécaniquement.** Un relevé qui les
compte fait basculer des chiffres justes.

**Un relevé de grandeur relève aussi ses arrondis de présentation.** `77,9` et
`39,49` ont été relevés à côté de `77,7` et `39,5` : c'est le même chiffrage
écrit à un autre onglet. Les omettre laisse passer la moitié de la matière.

**Le coffre se restaure aux adresses canoniques de l'index, jamais aux adresses
de coffre.** Restauré à `archive/…`, `reference/…`, `input/…`, il fait rendre à
`controle_index.py` **39 fausses anomalies bloquantes sur 79**. La règle
`chemin` / `chemin_coffre` de l'index est la table de conversion, et elle se
joue avant tout contrôle. *Constaté et corrigé dans ce fil ; 40 anomalies
réelles subsistent après correction.*

**Un contrôle se joue sur la pièce qui fait foi quand l'intermédiaire manque.**
Le contrôle 2 a été joué en lisant `Synthèse Calculs Résolution_0910.xlsx`
cellule par cellule, le socle budgétaire ne se régénérant pas. **Le socle n'est
pas la source : c'est un dérivé de la pièce.** Renoncer au contrôle parce que le
dérivé manque aurait été une faute.

---

**Deux constats de fait, qui ne sont pas de la tambouille et qui corrigent des
énoncés du corpus.**

**L'énoncé « S17 est perdu » est faux.** `appareil/controle_socle.py` du clone
porte S1 à S10 et **S17** ; `appareil/epreuve_s17_salaire.py` est au dépôt. La
pièce perdue est `appareil/epreuve_controle_socle.py`, déclarée voie `depot` par
l'index et absente du clone. Et ce qui empêche S17 de se jouer n'est pas sa
disparition mais **l'absence d'intrant** : sans `appareil/socle_0910.py`, le
socle ne se régénère pas sur les classeurs du 20260917, et **aucun des dix-sept
bouclages ne se joue**.

**L'énoncé « 82,5 + 53,4 + le reste = 236,054667 » ne se recompose pas tel
quel.** Le total général vit sous la nomenclature de l'`Annexe Manuscrit`, les
deux totaux de tête sous celle de `Détail Economies`. Le joint entre les deux
vaut **135,954667** — structures facultatives 67,006667 + subventions 68,948 —
et non 135,9. **L'écart, 0,054667, est exactement l'arrondi de la ligne
« autres » des opérateurs.** Recomposé ainsi, le contrôle sort à
**236,054667 = 236,054667, écart nul**.

---
## 20260924 — EP3 est le livre entier, et l'énoncé contraire a fait tourner en rond

**Constat de fait, mesuré, qui corrige le corpus.**

**`livre/texte_livre.json` est le livre complet.** Mesuré sur la pièce : 180
folios, **192 143 caractères** de texte utile, extraits de
`ETAT_PARTOUT_JUSTICE_NULLE_PART_EP3.pdf` (2 759 475 octets, sha256
`1ea86386…`). Il porte le corps, la postface (folio 131), **les notes
(folios 145-159)**, **les annexes (folios 163-171** — Déclaration de 1789,
lettre de Turgot, et le tableau du détail des 236 Md€ au folio 170**)**, les
trois bios (173-177) et la table des matières (179-180).

**L'énoncé « EP3 est le corps du livre, pas le livre entier ; les annexes n'y
sont pas » est faux.** Il était inscrit en mémoire projet et repris par les CR du
20260923, où il figurait même comme « faute de méthode relevée ». Il a produit
l'inverse de ce qu'il visait : il a fait conclure « absent d'EP3, donc à chercher
aux annexes » sur des chiffres qui étaient dans la pièce, ou qui n'existaient
nulle part. **Il a coûté deux tours au fil du manifeste et a orienté à faux la
passe du 20260923.**

*Ce que la faute enseigne, et c'est le vrai sujet* : **un énoncé sur le périmètre
d'une pièce se mesure sur la pièce, une fois, et s'inscrit.** Celui-ci n'avait
jamais été mesuré — il avait été déduit d'une absence constatée sur un seul
chiffre. Une déduction sur un cas est devenue une règle de périmètre, et la règle
a survécu à toutes les relectures parce que personne ne l'a rejouée.

**Deux énoncés tombent avec lui.**

**La division par dix du volume de réglementation n'est pas aux annexes.**
*Tranché par l'auteur le 20260924* : elle figurait dans une version antérieure du
texte et **a été retirée du livre**, jugée trop indicative. L'ordre de grandeur
reste utilisable en livrable de diffusion au titre de la règle des chiffres
compatibles avec la doctrine ; le livre ne le porte plus.

**Les « annexes chiffrées » ne sont pas une pièce manquante.** *Rappelé par
l'auteur* : ce sont **les classeurs Excel joints au projet**, déjà digérés au
corpus de chiffres. Il n'y a pas d'autre pièce à chercher, et le tableau du détail
des 236 Md€ est en outre au folio 170 du livre.

**Pièce produite** : `livre/index_livre_EP3.md`, qui donne le folio de chaque
section. On ouvre l'index, puis le folio — jamais les 180 pages.

**Reste redondant, et c'est un arbitrage ouvert.** `manuscrit/manuscrit.html`
porte l'état du **21 juillet 2026**, deux épreuves en arrière, pour 224 Ko. Son
seul avantage sur EP3 est son balisage : les 141 notes y sont structurées et
ancrées à leurs appels. **Il est cité par `controle_hypotheses`, qui y cherche ses
repères en littéral** — il ne se supprime pas sans reporter ces repères sur EP3.

---
## 20260924 — La navigation du site : deux rangs, et les actions cessent de se valoir

**Arbitré par l'auteur**, sur maquette des trois options.

**Deux rangs.** Un bandeau de service porte la marque, la date de parution et les
trois actions ; **le rang principal est aux seuls onglets de contenu**, en gros.
*Motif : dans une barre à un seul rang, ce sont les onglets qui sautent quand la
place manque — ils y sont structurellement les plus faibles. Un rang à eux le rend
impossible, et la barre encaissera la carto et les graphiques.*

**Les trois actions ne se valent plus, et la forme le dit.** *Précommander le
livre* en or plein — seule action qui a une échéance et la seule qui vend ;
*J'adhère* en lien de service ; *Je m'exprime* en lien de service atténué.
*Elles étaient à égalité sur la page de garde ; elles ne le sont plus.*

**Ordre des onglets, les fiches déclassées** : Le livre · Le manifeste · Les
propositions · Les auteurs · Vidéos. Les dix-huit fiches passent en troisième
position — **déclassées sans être cachées**, conformément à la consigne de
l'auteur.

**Les mentions légales vont au pied**, avec le contact et l'adhésion. Une mention
légale ne se cherche pas dans une barre principale.

**Ce qui ne s'inverse pas, et qui a été écarté** : échanger la place des onglets
et des actions. Marque à gauche, actions à droite est la lecture attendue sur tout
site ; l'inverser désoriente sans rien gagner. **Ce qui se déplace est le poids —
par la place, la taille et la couleur — jamais l'ordre de lecture.**

*Option C écartée pour l'instant, et le motif vaut d'être gardé* : barre crème et
onglets en encre, plus sobre, mais elle retire l'aplat brique du haut de page.
**C'est une décision de charte, pas de navigation**, et elle ne se prend pas dans
un fil de navigation.

*Tambouille tranchée par Claude, au titre d'A-23.* **La barre se pose en deux
temps, et le premier ne porte que les onglets dont la page existe** — Le manifeste,
Les propositions, Vidéos. « Le livre » et « Les auteurs » n'entrent qu'avec leurs
pages. **A-59 l'impose : un onglet qui promet et ne délivre pas est plus dangereux
qu'un onglet absent.**

<!-- fragments : tout ce qui suit est régénéré par appareil/fragments.py -->

## 20260930 — arbitrages-phase1

Trois arbitrages de phase 1, tranchés par l'auteure. Ils ferment trois bornes de
`livrables/arborescence_mesures_20260928.md` — M-002, M-016, M-026.

## Critère des structures visées — M-002

**Tranché : la liste close, organisée par les critères.** Le texte porte la liste des
structures supprimées, ordonnée par les critères qui la fondent, et non le seul critère.

**Portée générale, et elle corrige une règle du corpus.** L'interdiction de nommer un
bénéficiaire est un principe de **présentation** — exposé des motifs, exposé sommaire — et
non une contrainte juridique. La règle « pas de cas nommés » de
`livrables/arborescence_mesures_20260928.md` est corrigée en ce sens : elle vaut pour la
présentation, elle ne borne pas le dispositif. *La correction est à porter à l'arborescence
par le fil qui la reprendra ; ce fil ne l'écrit pas.*

**Ce que la décision emporte.** 746 lignes à établir et à ordonner par critère — 750 est un
arrondi de communication, décomposé en 78 cessions d'actif et 668 suppressions. Le périmètre
devient opposable et le chiffre de 8,632 Md€ tenu. Les exceptions déjà nommées en extension
ne bougent pas : environ 300 établissements à patrimoine et revenus propres restent hors
champ (M-004), environ 50 agences régaliennes sont réinternalisées et non fermées (M-003).

**Reste ouvert, et c'est de la tambouille du fil qui établira la liste** : l'ordre des
critères d'organisation.

## Champ du mot « association » — M-016

**Tranché : le tiers non public et non lucratif**, quelle que soit sa forme juridique et
quel que soit le payeur.

**Motif de l'auteure.** Ces financements n'avaient pas à exister ; ils sont entrés par un
trou budgétaire. Le projet redéfinit positivement et de manière circonscrite le principe et
les moyens de l'action de l'État ; tout le reste sort.

**Ce que la décision emporte.** La forme juridique cesse d'être le critère : fondations,
fonds de dotation et coopératives d'intérêt collectif entrent au champ, et le contournement
par changement de statut est fermé. Le versant social — fonds d'action sociale des caisses,
agences régionales de santé — entre au champ ; la frontière entre textes financiers impose
alors la scission, soit deux amendements, PLF et PLFSS. Le montant du versant social n'est
pas ventilé à ce jour : le classeur isole 3,2 Md€ pour le seul versant État, sur 12,6 Md€ à
terme portés par M-016.

**Exclusion.** Les personnes publiques ne sont pas dans ce champ. Le renforcement de leur
définition et de leur gestion est un chantier distinct, à ouvrir.

**Déjà tranché, rappelé ici** : volet local inclus et plus strictement interdit ; transition
en deux ans ; composante recette portée par la suppression de toutes les niches.

## Secteurs écartés de la suppression des niches — M-026

**Tranché : différés, non sortis du champ.** Transition progressive, et restitution au sein
de la fusion fiscale.

**Ce que la décision confirme.** La lecture de la note du manuscrit est la bonne : le champ
est écarté *de la restitution immédiate*, non de l'abrogation. L'arborescence portait
« liste des secteurs écartés », qui suggérait une exception de champ ; c'est une exception de
calendrier.

**Ce que la décision emporte.** Aucune niche n'est conservée : la promesse d'intégralité
tient et la cible de 143,2 Md€ reste atteignable à terme. M-026 reste une mesure, et sa
composante TRANSITION porte deux vitesses — suppression immédiate d'un côté, extinction
progressive avec restitution renvoyée à la refonte de l'autre. Les 52 Md€ restitués ne
bougent pas : ils sont déjà nets de ce champ.

**La liste.** La seule qui existe est celle du classeur, écrite en hypothèse : hors
outre-mer sauf crédits et réductions d'impôt, hors agriculture, hors emploi à domicile et
garde d'enfant. Elle sert au chiffrage et à l'exposé ; une part lui revient au dispositif si
la progressivité s'écrit secteur par secteur.

**Reste ouvert** : la durée de la progressivité, et si elle s'inscrit par secteur ou en bloc.

## 20260930 — cle-de-passage

## 20260930 — Clé de passage du schéma aux prélèvements

**A — Trois étapes, une affectation.** L'appariement se joue dans l'ordre libellé,
puis ligne d'agrégat, puis non atteint ; un prélèvement rejoint au plus une ligne
du schéma. Le contrôle est mécanique : 420 lignes à la table, 420 libellés
distincts.

**B — Les treize sous-lignes sont des lignes d'agrégat à part entière.** Un
prélèvement rejoint la sous-ligne, jamais la ligne mère, quand une sous-ligne le
reçoit. L'absence de valeur à la colonne de suppression vaut maintien, et cette
lecture se déclare au relevé sans être appliquée.

**C — Un motif de contrepartie invoquée n'a pas de réceptacle.** Redevance pour
service rendu, redevance domaniale, redevance de contrôle, rémunération pour
service rendu, redevance sur produits de santé : le schéma ne porte aucune ligne
pour ces prélèvements. Ils sortent en « non atteint » avec leur cause, et ne se
rattachent pas de force à « Autres taxes sur les ménages ».

**D — Une seule variante de code de siège est résolue.** `cgct` vaut
`code général des collectivités territoriales`, trois lignes. Aucune autre
normalisation n'est nécessaire : 17 codes bruts, 16 après résolution.

**E — La clé vit dans la table, pas dans un générateur.** Le mandat nomme deux
pièces ; l'affectation de chaque prélèvement est portée en colonne de la table de
passage, qui se relit seule. Aucun script n'est versé.

## 20260930 — correction-cle-de-passage

## 20260930 — Correction de la clé de passage

**F — Une affectation peut traverser la frontière d'assiette, sur déclaration.**
Le forfait social et les contributions sur attributions d'actions gratuites et
stock-options rejoignent « dont forfaits de cotisation » alors que le référentiel
les classe en assiette 2, hors périmètre du schéma. Le motif est écrit au relevé :
le schéma lit par la fonction, le référentiel classe par l'assiette juridique. La
règle ne vaut pas précédent et ne s'étend à aucun autre prélèvement des assiettes
1 et 2.

**G — Le test de périmètre cède devant un rattachement de libellé déclaré.**
L'ordre d'exécution place la règle de libellé avant le retrait d'assiette, et le
retrait du temps 1 se calcule sur l'étape effective, non sur l'assiette.

**H — Les 41 non atteints se qualifient en catégorie sans réceptacle.** Ils ne
sont plus présentés comme un reste d'appariement. Le relevé nomme les trois voies
possibles pour leur sort et n'en ouvre aucune : l'arbitrage appartient à l'étape
suivante.

## 20260930 — csa-forfaits-de-cotisation

# Arbitrage — 20260930 — La ligne « dont forfaits de cotisation »

**Décidé par l'auteur, contre son propre rattachement antérieur.**

La ligne « dont forfaits de cotisation » du schéma « Refonte fiscalité »,
8,8 Md€ base 2024, reçoit **le forfait social et la contribution solidarité
autonomie**. Les contributions patronales et salariales sur les attributions
d'options et sur les attributions gratuites d'actions **restent hors du
périmètre du schéma**, comme le reste de l'assiette 2.

**Les deux motifs, tenus ensemble.**

1. Arithmétique : forfait social + CSA font 8,77 contre 8,8 au schéma, à
   l'arrondi près ; forfait social + stock-options font 7,33.
2. Assiette : la CSA est assise sur la masse salariale et appartient
   naturellement à la ligne mère « taxes sur la main d'œuvre », ce qui n'est
   pas le cas des stock-options.

Le rattachement par la fonction — des forfaits qui remplacent des cotisations
sur des rémunérations qui y échappent — est écarté au profit de ces deux-là.

**Enjeu : 1,67 Md€, faible.**

**Conséquence déclarée.** Le résidu réel entre le périmètre de recensement et
le périmètre de doctrine passe de 5,5 à 12,8 Md€. Il est déclaré ; on ne le
chasse pas.

**Pièce à reprendre.** `referentiels/table_passage_schema_prelevements_20260930.tsv`
porte encore l'ancien rattachement. Contradiction C-1 de
`livrables/reconciliation_sources_fiscales_20260930.md`.

---

# Arbitrage — 20260930 — Les 41 prélèvements à contrepartie invoquée

**Rappelé comme déjà tranché, sans être rouvert.** Par défaut **supprimer et
fondre** ; **sortie du périmètre en repli** ; **au cas par cas, sans paresse**.
C'est la troisième voie du relevé, avec un défaut orienté. Part telle quelle
au fil du sort.

## 20260930 — defauts-reconciliation

# Défauts appliqués aux contradictions du relevé de réconciliation — 20260930

Tranchés par Cowork, sur défaut existant au corpus. Révocables par l'auteure.
Pièce d'origine : `livrables/reconciliation_sources_fiscales_20260930.md`.

## D-1 — Le schéma prime sur la rédaction de l'expert

**Règle générale posée.** Quand le CGI réécrit par l'expert et le schéma
« Refonte fiscalité » tranchent différemment le sort d'un prélèvement, **le
corpus prime, et l'écart à la rédaction de l'expert se déclare en exposé
sommaire.** C'est le défaut déjà écrit au § 5 de
`reference/cgi_expert_regles_de_lecture.md` pour le taux réduit de TVA ; il
est étendu ici aux trois autres contradictions de même forme.

Conséquences, sans autre instruction :

- **C-3, taxe foncière.** Une taxe foncière unique en euros par mètre carré
  (M-035). Les deux taxes du texte — 1380 et 1393 — et l'assiette en valeur
  locative tombent. Écart déclaré.
- **C-4, taux de TVA.** Un taux unique à 20 % (M-029). L'article 278-0 bis
  tombe avec les autres taux réduits. Écart déclaré.
- **C-5, droits de mutation à titre gratuit.** Supprimés et remplacés par la
  franchise de 3 % (M-033). L'article 777 laissé sans taux et l'article
  750 ter maintenu ne valent pas maintien. Écart déclaré.

## D-2 — Un article-siège touché ne vaut maintien ni suppression par lui-même

**C-6, droit de licence sur la rémunération des débitants de tabacs.** Le rang
`maintenue` prime : l'exception nommée de M-030 porte sur les produits à
effets négatifs et à dépendance forte, et le tabac en est. L'allègement de
l'article 568 est un fait de rédaction, pas un sort. **Maintenu.**

**C-7, les huit que le texte touche parmi les 41.** L'abrogation d'un article
du CGI ne qualifie pas le prélèvement : les sept redevances sanitaires
abrogées et la contribution de sécurité immobilière allégée **restent dans le
lot des 41 à contrepartie invoquée** et suivent son arbitrage — par défaut
supprimer et fondre, sortie du périmètre en repli, au cas par cas. Le fait que
le texte les touche déjà est un appui de rédaction, pas une décision.

## D-3 — Les cotisations sociales restent hors mandat

**C-2.** Deux sources se contredisent sur 81 prélèvements de l'assiette 1 :
M-031 les atteint par le motif « main-d'œuvre », la décision de l'auteure
portée sous M-028 dit que « les cotisations restantes [sont] laissées de côté,
traitées plus tard par convergence et lissage progressifs ».

**Défaut appliqué : la décision sous M-028 prime, comme la plus explicite et
la plus récente. M-031 est lu comme ne portant, dans le périmètre du chantier,
que les impôts de production — 36 prélèvements de l'assiette 5 — et les
30 prélèvements de l'assiette 3, déjà dans le périmètre du schéma.**

**Conséquence : les 83 cotisations sociales restent au solde et ne reçoivent
aucun sort.** Le solde du fil d'attribution reste à 129.

*Ce défaut est celui qui pèse le plus lourd en nombre. Il est posé pour que la
chaîne déroule sans arrêt ; il se révoque en une ligne.*

## D-4 — La table de passage se corrige avant d'être relue

`referentiels/table_passage_schema_prelevements_20260930.tsv` porte encore
l'ancien rattachement de la ligne « dont forfaits de cotisation »
(contradiction C-1). **Le fil qui l'ouvre ensuite la corrige d'abord** :
la contribution solidarité autonomie entre à la ligne, les contributions sur
les attributions d'options et d'actions gratuites en sortent vers
« 0 — hors périmètre du schéma ». Les compteurs de
`livrables/couverture_table_de_passage_20260930.md` se rejouent dans le même
mouvement.

## 20260930 — perimetre-fiscal

# Arbitrages — périmètre fiscal, 20260930

## Prélèvements sociaux sur le capital

Les prélèvements sociaux sur les revenus du capital et assimilés ne sont pas touchés. Cela couvre les prélèvements de solidarité, 15,6 Md€, et les prélèvements sociaux sur les revenus du patrimoine et des placements.

Motif : la restitution salariale porte sur les revenus d'activité. M-025 supprime la CSG et la CRDS sur l'activité, non sur le capital. La question restait ouverte au relevé de réconciliation du 20260930 ; elle est close par cette décision.

Conséquence pour l'attribution du sort : ces prélèvements prennent le sort « non touché », et ne comptent ni au gage ni à la restitution.

## Flat tax

La rédaction de l'expert fusionne le prélèvement forfaitaire unique dans un impôt sur le revenu des personnes physiques traité à part.

C'est une opération technique de rédaction. Elle ne change ni le schéma macroéconomique, ni la situation des redevables ordinaires. Elle ne se raconte pas en exposé sommaire et n'appelle aucun arbitrage de doctrine.

## Redevances et rémunérations pour service rendu

Les 33 prélèvements à contrepartie invoquée restés sans sort — redevances, rémunérations pour service rendu, frais de contrôle — s'auditent **un par un** contre les principes de la doctrine.

Règle : par défaut, supprimer et fondre. Sortie du périmètre des prélèvements obligatoires en repli, lorsque la suppression ne vole pas. Le repli ne se prend jamais par défaut ni par commodité : chaque ligne s'éprouve.

Sous le milliard d'euros, le principe prime et le montant est secondaire.

Le fil d'attribution rend une solution justifiée pour chacune et ne remonte à l'auteure que les points saillants.

## Frontière de projet — rappel opposable

Le découpage des mesures, les énoncés, les paramètres, les arguments et leur vérification se font au projet doctrine. La qualification, le rattachement, le vecteur, la rédaction cible, l'exposé sommaire et la liasse se font au projet machine, valise branchée.

Une ligne de lancement du projet doctrine n'active donc jamais `disposition-cible`, `redaction-legistique` ni `expose-sommaire`. Elle peut activer `compatibilite-doctrine` et `vecteur-mesure`.

Cette règle a été enfreinte deux fois le 20260930, dans les deux cas par une ligne de lancement de phase 1 écrite au projet doctrine. Elle se vérifie à chaque lancement.

## Mesure de siège — chantier à inscrire

105 prélèvements du référentiel ne portent aucun siège renseigné, dont les prélèvements de solidarité, 15,6 Md€.

Un sort s'attribue sans adresse ; un amendement ne s'écrit pas sans elle. Le trou ne mord pas à l'attribution du sort ; il mord à la rédaction de la phase 3.

Un relevé de siège est donc dû avant la phase 3, sur les prélèvements sans siège qui reçoivent un sort autre que « non touché » ou « hors mandat ». Il n'est inscrit à aucun plan à ce jour.

## Conduite de la première écriture

La phase 1 sera la première écriture réelle de la chaîne : aucun dossier de mesure n'a jamais été versé, et l'étape de rattachement n'est pas outillée.

Elle se lance sur un petit nombre de mesures d'abord, non sur le mouvement entier.

## 20260930 — sort-prelevements

Six points de tambouille tranchés par le fil du sort des prélèvements, et
inscrits. Révocables par l'auteure.

**Le vocabulaire de sort est clos à neuf termes.** `conservé`, `fondu`,
`supprimé`, `maintenu à part`, `non touché`, `sortie du périmètre des PO`,
`en attente`, plus `hors mandat` et `hors champ`, qui ne sont pas des sorts mais
des états. Le mandat en nommait cinq ; `conservé` manquait pour les quatre impôts
eux-mêmes, `sortie du périmètre des PO` est le repli que l'arbitrage du périmètre
fiscal ouvre pour les prélèvements à contrepartie invoquée, `en attente` est ce
que le prompt réserve à ce que ni la règle ni l'agrégat n'atteignent.

**L'ordre d'application : le schéma au niveau de la ligne, la doctrine pour la
destination de l'assiette.** Colonne « Taxes à supprimer » vide vaut maintien,
colonne servie vaut suppression ; la règle de doctrine départage ensuite
`supprimé` de `fondu` selon que l'assiette revient ou non à un impôt conservé.
**Le sort ne rouvre jamais l'arithmétique du schéma** : les −137,05 Md€ restent
ce que le schéma écrit, qu'un prélèvement soit supprimé ou fondu.

**Le critère du repli, pour les 41 prélèvements à contrepartie invoquée : le fait
générateur est un acte demandé par le redevable à son seul bénéfice, et le tarif
rémunère cet acte.** À défaut — police administrative, bien public, ou assiette
proportionnelle à la valeur et non au coût du service — la suppression ne vole
pas et le prélèvement est supprimé. Appliqué ligne à ligne : 25 replis, 16
suppressions. Le repli porte 0,470 Md€ sur 2,338, soit 20 % du lot : il n'a pas
été pris par commodité.

**La ligne « dont énergie » se partage par la nature du produit, non par le
montant.** M-030 conserve les énergies fossiles ; l'électricité n'en est pas.
Sept accises maintenues à part, trois supprimées, 5,153 Md€ en base 2026 contre
8 Md€ au schéma en base 2024. **L'écart de 2,85 Md€ est déclaré non comblé** :
millésime, correction du bouclier tarifaire que le schéma porte lui-même en note,
et assiette mixte électricité-combustibles d'une des trois lignes, ne se séparent
sur aucune pièce du corpus.

**La ligne « Taxes sur chiffre d'affaires et bénéfices » se partage par
sous-assiette.** Les 7 prélèvements assis sur le bénéfice sont `fondu — impôt sur
les sociétés` ; les 8 assis sur le chiffre d'affaires ou les dépenses sont
`supprimé` au titre de M-031. La compensation passe par le taux de l'impôt sur
les sociétés, que le schéma porte en hausse d'équilibre de 25,69 Md€, non par un
report d'assiette.

**La table de passage n'a pas été réécrite au coffre, et c'est délibéré.** La
clé corrigée par le lot 0 est appliquée à toute l'attribution et les compteurs
sont rejoués sur elle, mais la copie de travail du fil ne porte que six des huit
colonnes du fichier : `siege_code_normalise` n'est pas reconstituable ligne à
ligne, et réécrire le fichier la perdrait. Ce serait une reconstruction, pas une
correction. Le patch de deux lignes — la contribution solidarité autonomie entre
à « dont forfaits de cotisation », les contributions sur les attributions
d'options et d'actions gratuites en sortent vers « 0 — hors périmètre du
schéma » — est rendu au livrable et dû au dépôt.

## 20260930 — sort-prelevements-decisions

Trois décisions de l'auteure, prises sur questions du fil du sort des
prélèvements et appliquées le jour même.

**Les 14 prélèvements « Locaux d'activité » de la ligne « Autres taxes sur les
entreprises » sont supprimés et leur rendement repris par la taxe foncière
unique.** CFE, taxes additionnelles pour frais de chambres de commerce et de
métiers, taxe sur les bureaux d'Île-de-France, TASCOM, surfaces de stationnement,
friches commerciales — 1,915 Md€ en base 2026. Le schéma et M-035 sont tenus
ensemble et non l'un contre l'autre : le sort porté est `fondu — taxe foncière`,
qui dit la disparition du prélèvement et le report de son assiette sur un impôt
conservé. **L'arithmétique du schéma n'est pas rouverte** : les −13,5 Md€ de la
ligne restent ce que le schéma écrit.

**Les prélèvements obligatoires 2024 valent 1 251,8 Md€, chiffre Insee.**
`Synthèse Calculs Résolution_0910.xlsx`, onglet `Refonte fiscalité`, `F3` —
2 919,9 Md€ de PIB à 42,871 %, source Insee citée en `B8`. Les 1 250,76 Md€ qui
circulaient par ailleurs sont écartés. L'écart de 1,04 Md€ est clos. La ligne 1
du bouclage devient : 1 251,8 − 626,9 = 624,9.

**Les quatre sous-lignes sans valeur en colonne « Taxes à supprimer » sont
maintenues à dessein.** Assurances 19,2, forfaits de cotisation 8,8, outre-mer
1,6, taxe de séjour 1,1 — 21 prélèvements, 25,891 Md€ en base 2026. La lecture
« colonne vide vaut maintien », déclarée au relevé de couverture du 20260930, est
confirmée par l'auteure. La contradiction apparente avec M-030 est close et ne se
rouvre pas.

---

**Ce que la mesure a rendu sur les stock-options, et qui ne donne pas le sort.**
Question posée par l'auteure, mesurée, non tranchée.

- Le CGI réécrit par l'expert **supprime `80 bis` et `80 quaterdecies`**, les deux
  articles qui portent l'imposition de l'avantage — options de souscription et
  d'achat, attributions gratuites — tous deux à zéro caractère à
  `referentiels/cgi_expert_articles.tsv`, et retire le taux dérogatoire de
  l'avantage salarial à `200 A` ainsi que le renvoi à `80 bis` dans le prix
  d'acquisition de `150-0 D`. L'avantage retombe au droit commun du revenu, au
  taux unique de M-036.
- **L'expert ne dit rien des contributions elles-mêmes** : siège aux articles
  `L. 137-13` et `L. 137-14` du code de la sécurité sociale, hors de ses cinq
  pièces. Cas général du § 8 du relevé de couverture du 20260929.
- **L'onglet `Annexe Manuscrit` ne dit rien non plus** : c'est le tableau des
  économies, 236,05 Md€, et aucune de ses 26 lignes ne porte l'épargne salariale,
  les stock-options ni les attributions gratuites.
- **L'arbitrage du 20260930 sur « dont forfaits de cotisation » a déjà tranché le
  rattachement**, contre le rattachement par la fonction : les stock-options
  restent hors du périmètre du schéma, sur un motif arithmétique — 8,77 contre
  7,33 — et un motif d'assiette. Les laisser avec le forfait social rouvrirait cet
  arbitrage. **Le fil ne le rouvre pas** ; le prélèvement reste `en attente`.

## 20261001 — courroies

**Un fragment déposé depuis Cowork n'est pas au clone que la session de code lit.**
Mesuré, et c'était la question à fermer avant toute autre. Le dépôt
`resolution-ib-dev/Resolution-2027`, `main` à `4e6e1a4`, porte
`chantier/Makefile`, `chantier/.gitignore`, `chantier/appareil/` — 92 modules —
`chantier/referentiels/` — 5 JSON —, plus `data/`, `codes.json`, `droit.py`,
`essai.py`, `extraire_legi.py`, `README.md`. **Il n'y a ni `methode/`, ni
`livrables/`, ni `reference/`, ni `methode/fragments/`.** Un paquet de dépôt qui
renvoie à un chemin du coffre ne renvoie donc à rien : il porte verbatim, ou il
ne porte pas.

**Tranché en propre — la déclaration d'un document à la table curée se fait par
son adresse.** Les 46 documents du rattrapage sont déclarés sans être ouverts :
rang et famille tirés du dossier où le document vit, consommateur générique
— `appareil/fragments.py` pour un fragment, `ouverture de session` pour une
pièce de `methode/` ou de `reference/`, `lecture de l'auteur` pour un livrable ou
une grille. C'est l'arbitrage du 20260917 sur le classement par adresse, appliqué
à la déclaration elle-même : un fait vérifiable sur où le document vit, non un
jugement de contenu, et que toute ligne de carte contredit. Le premier garde-fou
— ne pas classer un document non ouvert — est tenu : rien n'est qualifié.

**Tranché en propre — les deux grilles du sort des prélèvements entrent à
`COFFRE_DOCUMENT`.** `referentiels/sort_prelevements_20260930.tsv` et
`referentiels/table_passage_schema_prelevements_20260930.tsv` sont de rang
`referentiel` et vivent au coffre à leur propre chemin. Sans cette entrée, la
règle de voie les enverrait en `depot`, où `restaurer.py` les chercherait en
vain. Même régime que les six grilles du rattrapage du 20260930.

**Un paquet de dépôt se contrôle en le rejouant.** Les blocs verbatim du paquet
ont été réextraits de leur propre texte et appliqués à une copie neuve du clone :
les deux générateurs rendent les nombres annoncés. Un paquet dont on n'a pas
rejoué le texte est un paquet non mesuré.

**Deux énoncés du registre sont périmés, et la mesure les corrige.**
`appareil/plier_paquet.py` et `appareil/controle_projection.py`, déclarés perdus
et absents du clone, **y sont**. Le générateur de l'index, dit décroché à 253
artefacts contre 310 au coffre, rend **315** — exactement ce que l'index du
coffre porte. Les deux constats du 20260930 sont des traces datées rattrapées par
le commit `4e6e1a4` du même jour, et ils ne valent plus état.

## 20261001 — entame-liste

*Seconde reprise de la liste du PLFSS 2027, sur consigne de l'auteure : le chapeau
passait trop de temps sur des agrégats techniques, et les lignes d'article étaient
trop techniques dès leur entame. Deux règles portées au gabarit — étage 0, elles
priment sur ce que le gabarit disait.*

**A — L'ordre du chapeau est renversé : les gens d'abord, les agrégats après.**
L'ordre antérieur ouvrait sur le solde, le besoin d'emprunt et les crédits. Le
nouveau ouvre sur **`## Ce que ce texte change, et pour qui`** : trois à cinq lignes
sans un seul agrégat, puis **un tableau `qui` · `ce qui change pour lui` · `où`**,
treize lignes rangées par poids et non par ordre du texte. Les grandeurs suivent,
sous **`## Les grandeurs, pour mémoire`** — le titre dit leur statut.

*Gain mesuré sur la pièce : un lecteur qui n'ouvre que la première page sait
désormais qui paie, sans avoir traversé un mur de nombres.*

**B — L'entame d'une ligne d'article dit ce que l'article fait à quelqu'un.**
Registre pris à `expose-sommaire` — § 5.1, « le constat s'ouvre sur ce que le
dispositif fait à quelqu'un, le défaut de genre vient ensuite » ; § 5.3 bis, la
phrase de sens « qui nomme quelqu'un » ; § 5.0 bis, le verbe direct sans périphrase.
Appliqué aux quarante-neuf lignes :

| avant | après |
|---|---|
| Intègre les compléments de salaire dans l'assiette de calcul des allègements généraux | **Fait entrer les primes dans le calcul des allègements de cotisations : les employeurs verseront 3,7 Md€ de plus** |
| Remplace la clause de sauvegarde des dispositifs médicaux, qui ne couvrait que 21 % de la dépense remboursée | **Taxe plus largement les fabricants de matériel médical : la contribution portait sur 21 % de la dépense remboursée, elle portera sur tout** |
| Crée un statut des groupements d'officines et une contribution sur les rémunérations qu'ils perçoivent des laboratoires | **Encadre les centrales d'achat des pharmacies et taxe ce qu'elles perçoivent des laboratoires** |
| Prolonge d'un an l'expérimentation de fusion des sections soins et dépendance des EHPAD | **Prolonge d'un an l'expérience qui fusionne les deux budgets des EHPAD, soins et dépendance** |
| Déroge pour 2027 à la revalorisation automatique des pensions | **Suspend pour 2027 la règle qui indexe les pensions sur l'inflation** |

**Le terme technique n'est pas banni : il est déplacé.** Il vient après le fait,
quand il apporte quelque chose. *Le test retenu : lue seule, la ligne apprend
quelque chose à quelqu'un qui n'a pas le texte sous les yeux.*

**C — Ce qui ne bouge pas.** Aucun chiffre n'a changé, aucune source, aucun des sept
écarts relevés. La reprise porte sur l'ordre et sur la langue, jamais sur le fond.
Le contrôle de rendu est rejoué : **49 articles sur 49, zéro ligne nue.**

**D — Un défaut de rendu trouvé au passage.** La colonne `où` du tableau d'entrée
coupait « art. 35 » sur deux lignes. Corrigé par une espace insécable dans la
cellule, non par une règle de largeur : une largeur fixée sur la troisième colonne
aurait déréglé les tableaux à deux colonnes, qui partagent la même feuille de style.

**E — Coût : deux pages.** De 5 à 7. Inscrit au gabarit pour que personne ne le
reprenne comme une dérive.

## 20261001 — epargne-salariale-et-affectataires

Trois décisions de l'auteure, prises le 20261001 sur le fil du sort des
prélèvements.

## Les affectataires ne se suivent pas

**Un flux entre administrations publiques est neutre au solde.** Traiter la perte
de recette d'une caisse comme un coût du programme ferait apparaître un coût là
où il n'en existe pas : c'est un piège, et il se nomme.

**Règle.** Aucun livrable de la chaîne ne suit l'affectataire d'un prélèvement
supprimé, fondu ou restitué. Les affectataires se reprennent **facialement, en
aval**, une fois les sorts arrêtés. Aucune colonne d'affectataire n'entre au
relevé de sort ni au classeur de réforme.

## L'épargne salariale — défaut orienté, à confirmer

Les contributions patronales et salariales sur les attributions d'options et
d'actions gratuites, 1 669,1 M€. **Les deux jambes se séparent, et elles ne vont
pas au même flux.**

**Jambe du code général des impôts — supprimée avec les niches.** Le CGI réécrit
par l'expert supprime `80 bis` et `80 quaterdecies` ; l'avantage retourne à
l'assiette de l'impôt sur le revenu, au taux unique de M-036. Son flux est celui
des niches d'impôt sur le revenu — ligne « IR net » du schéma, 27 Md€ de niches
restituées. *La ligne exacte de l'annexe 3 qui la porte n'est pas mesurée.*

**Jambe du code de la sécurité sociale — restituée en capitalisation, et
ultérieurement seulement.** Siège aux articles `L. 137-13` et `L. 137-14`. Elle
rejoint le **circuit A à la colonne « au-delà », jamais l'année 1** — parallèle
exact avec l'assurance chômage transformée en épargne, que
`livrables/mecanique_gages_restitutions_20260929.md` porte déjà à 30 Md€ en
« au-delà » et à zéro en année 1.

**Le motif qui décide, et il est de mécanique.** Portée en `supprimé`, la jambe
sociale relèverait du circuit B, dont la contrepartie — 67,75 Md€ de hausses
d'équilibre, 25,69 par 27 points d'impôt sur les sociétés et 42,06 par la taxe
foncière — est déjà écrite, close à l'euro, et **ne se rouvre pas mesure par
mesure**. Portée en restitution, elle relève du circuit A, dont la restitution au
salarié est l'objet même, et **le circuit B n'est pas touché**.

**Sort porté au relevé : `restitué en capitalisation`.** Le vocabulaire de sort
passe de neuf à dix termes ; plus aucun prélèvement des 420 n'est `en attente`.
Le défaut est révocable en une ligne.

## L'ordre de la restitution en capitalisation

**Les forfaits sont de second ordre, et la séquence est arrêtée.** La restitution
en capitalisation se fait **d'abord par les cotisations salariales**. Les forfaits
— forfait social 6 690,2 M€, contributions sur les attributions d'options et
d'actions gratuites 1 669,1 M€ — sont embarqués ensuite ou pas, et cela se décide
à ce moment-là.

**Conséquence tenue :** le forfait social reste `maintenu à part`, les
contributions sur les attributions restent au défaut `restitué en capitalisation`
en colonne « au-delà », et **ni l'un ni l'autre ne se rejoue avant le chantier de
capitalisation**.

*Fait relevé, et rien de plus* : les cotisations salariales par lesquelles la
restitution commence sont les 83 prélèvements de l'assiette 1, que D-3 tient hors
mandat et sans sort.

## 20261001 — lecture-plf2027

*Tambouille tranchée par le fil de lecture du PLF 2027, en l'absence de
`appareil/index_mesures.py` au clone. Chaque règle vient d'une divergence mesurée,
non d'un principe : la grille a été reprise à chaque fois, jamais le résultat.*

**1. Le repère de page est le folio imprimé, mesuré, jamais le renvoi du
sommaire.** Le folio a été extrait des 391 pages qui en portent un et confronté à
l'index de page du PDF : écart constant de 0. Le sommaire, lui, diverge du folio à
partir de l'article 8 et jusqu'à +21. *Une divergence ne se corrige pas en
déplaçant le repère : elle dit laquelle des deux sources est la pièce. C'est le
folio.*

**2. La profondeur de découpage d'une mesure est bornée à deux niveaux.** Le
gabarit 2026 ne porte aucune référence plus profonde que `<romain>-<second
niveau>`. La règle est donc : le bloc de premier niveau fait une mesure s'il ne
modifie qu'un siège ; sinon il se découpe à son second niveau et pas au-delà, le
chapeau du bloc restant attaché à son premier enfant. *Reprise du gabarit, non
réinvention.*

**3. Garde d'ordre sur les marqueurs de subdivision.** Un marqueur n'est retenu
que si sa valeur excède celle du marqueur retenu précédemment au même niveau.
*Mesure qui l'a imposée : sans elle, l'article 42 se découpait sur un « 9° » lu à
l'intérieur du tableau d'affectation à des tiers, et rendait deux blocs de dix
pages là où il y en a un.*

**4. Garde de rang 1 sur le sous-découpage.** Un bloc ne se découpe que si son
premier sous-marqueur est de rang 1 — `I`, `A`, `1°` ou `a`. *Même mesure que la
précédente : un tableau produit des marqueurs plausibles mais jamais une série
qui commence à son premier rang.*

**5. Les lettres `I`, `V` et `X` ne sont pas des marqueurs de second niveau.**
Elles sont ambiguës avec les chiffres romains du premier niveau, et la légistique
française saute `I` dans les séries en lettres. *Mesure qui l'a imposée : sans
elle, l'article 2 rendait une seule mesure de quatre pages au lieu de douze — le
marqueur `I.` du premier niveau était lu comme une lettre et bloquait, par la
garde d'ordre, les subdivisions `A` à `H` qui le suivaient.*

**6. Les passages entre guillemets sont blanchis avant toute détection de siège,
et le blanchiment traverse les lignes.** Le texte cité est le droit à venir, pas
le siège modifié. Un blanchiment ligne à ligne ne suffit pas : une citation ouverte
en fin de ligne continue sur les suivantes. *Mesure qui l'a imposée : 41 sièges
faux relevés sur l'ensemble du texte — 516 mesures avant, 475 après —, dont des
articles du code général de la fonction publique attribués au code général des
impôts.* **Les offsets sont préservés** — les caractères cités sont remplacés par
des espaces, non supprimés —, faute de quoi le siège ne se rattache plus à sa
ligne ni à sa page.

**7. Le contexte de pièce se porte le long de l'article et ne se met à jour que
sur une formule de modification.** Un siège sans pièce explicite hérite de la
dernière pièce déclarée « est ainsi modifié », « est ainsi rédigé », « est
complété », « est rétabli », « est abrogé ». Une pièce nommée en simple
qualificatif d'un renvoi ne change pas le contexte. *Mesure qui l'a imposée : la
règle inverse faisait basculer tout l'article 2 sur le code de la sécurité sociale
dès la première mention de ce code dans un renvoi.*

**8. La fiche de mesure principale se rend à la maille de l'article, non de la
mesure.** Le critère « article parmi les plus chargés en adresses ouvertes » est,
par construction, un critère d'article : appliqué à la mesure, il retenait
**206 mesures** et rendait les fiches illisibles. À la maille de l'article, il en
retient **54 sur 90**, chacune portant les mesures principales de son article.
*Le prompt dit « fiche courte, lisible par un tiers » : 206 fiches ne le sont pas.*

**9. La sélection des mesures principales est elle-même un relevé, et elle se
verse avec sa liste de non-retenus.** Les 36 articles écartés sont nommés au
livrable, avec quatre cas signalés d'office dont la non-retenue tient à la lettre
du critère et non à leur poids. *Un critère mécanique qui écarte l'article 74 ne
se corrige pas en ajoutant l'article 74 à la main : c'est le critère qui se
reprend, et l'auteure seule le fait.*

**10. Un montant écrit dans le texte cité du dispositif est un chiffre du texte,
pas un chiffre de l'exposé.** La règle de chiffre interdit l'exposé des motifs,
pas la rédaction nouvelle que le dispositif édicte. Les paramètres — taux,
plafonds, seuils — sont donc rendus, sous le nom de « chiffre porté par le
dispositif », distinct du « chiffre pris à l'état ». *Sans cette distinction, les
fiches ne portaient plus aucun paramètre et devenaient vides.*

**11. Les relevés mécaniques intégraux ne sont pas versés.** Mots de portée,
absences attendues, formules d'entrée en vigueur : le balayage porte sur les
90 articles, la restitution sur les seuls articles où elle discrimine. Le prompt
l'ordonne — « ne pas truffer le livrable ». Le relevé intégral reste à l'atelier et
ne constitue pas une pièce.

## 20261001 — lecture-plfss-2027

*Tambouille tranchée par le fil, et inscrite. Rien ici n'est de fond ; ce qui l'est
est allé à `methode/a_trancher.md`.*

**A — Grammaire de relevé locale, faute de `appareil/index_mesures.py` au clone.**
Le module est de voie `depot` et absent ; le paquet de dépôt des courroies du
20261001 le nomme déjà comme trou de déclaration. Le fil n'a pas renoncé à son
livrable : il a écrit sa propre grammaire, déclarée ici avant exécution.

1. Texte sorti par `pdftotext -layout`, 121 pages, découpé en articles sur la ligne
   de titre d'article isolée, puis en dispositif et exposé des motifs sur la ligne
   « Exposé des motifs ».
2. Subdivisions reconnues, du moins profond au plus profond : `I. –`, `A. –`, `1°`,
   `a)`. Descente récursive : un bloc qui porte **plus d'un siège** est redécoupé au
   niveau suivant ; un bloc qui en porte zéro ou un est une mesure. C'est la
   définition du mandat — la subdivision la moins profonde sous laquelle un seul
   siège de droit est modifié.
3. Siège = couple (code ou loi, article). Le code est pris au plus proche à droite
   dans les 120 caractères, sinon au plus proche à gauche, sinon **hérité du chapeau
   du bloc parent** — c'est ce qui permet à « 2° L'article L. 16 est complété » de
   porter le code de la sécurité sociale annoncé au I.
4. Un numéro d'article immédiatement suivi de « de la loi », « de l'ordonnance »,
   « du règlement » ou « du traité » n'est pas compté comme siège de code : la loi
   ou l'ordonnance est relevée séparément.
5. **Les chapeaux portent leur propre mesure**, comme dans le gabarit 2026 — où
   l'article 32 du PLF porte une mesure `32` sans subdivision, suivie de `32.2 (I)`.
   Le relevé passe ainsi de 256 à 314 mesures ; le compte retenu est 314.
6. Titre d'article : première ligne non-marqueur, plus les lignes suivantes dont
   l'indentation dépasse 15 colonnes — c'est la signature d'un titre centré sur deux
   lignes. L'article liminaire n'en porte pas et sort à `—`.

**Ce que cette grammaire ne fait pas**, et qui se déclare plutôt que de se deviner :
elle relève les **adresses citées** dans la subdivision, pas seulement celles que la
subdivision modifie. Un article visé comme simple référence — « les employeurs
mentionnés au II de l'article L. 241-13 » — est compté comme siège. Les 95 mesures à
siège vide ne sont donc pas des mesures sans objet, et les 219 autres ne sont pas
toutes des portes ouvertes : **le tri des portes est l'affaire du bloc L2**, pas de
l'index.

**B — Nommage.** `livrables/index_mesures_plfss_2027.md` et
`livrables/fiches_mesures_plfss_2027.md`, sur le modèle de
`livrables/index_mesures_plf.md` augmenté du véhicule et du millésime, le gabarit
2026 n'ayant pas eu à les distinguer.

**C — Pas de TSV compagnon.** Le millésime 2026 porte
`referentiels/index_mesures_plf.tsv` à côté de son index. Le mandat de ce fil nomme
l'index au gabarit, pas sa grille. Un fil ne produit que les pièces que son mandat
nomme : le TSV ne s'écrit pas ici. Il s'écrira si un fil aval en a besoin.

**D — Périmètre des fiches.** Le critère de mesure principale est celui du prompt,
appliqué tel quel. Il donne 33 fiches couvrant 36 articles. Les trois conditions se
répartissent ainsi : montant propre — liminaire, 1er, 2, 3, 11, 15 à 19, 40 à 48 ;
nos objets — 5 à 14, 33 ; articles les plus chargés en adresses ouvertes — 20, 27,
28, 32, 34. L'article 35 entre par son montant d'exposé, l'article 37 par son objet.
Les articles 45 à 48, qui ne portent qu'une phrase chacun, sont regroupés en une
fiche : quatre fiches d'une ligne auraient alourdi sans rien rendre.

**E — Les relevés mécaniques ne truffent pas le livrable.** Mots de portée, absences
attendues, montées en charge et entrées en vigueur différées ont été relevés sur les
49 articles. Ils ne sont restitués que dans les fiches, et seulement là où ils
changent la lecture : neuf « peut » à l'article 28, le XIII de l'article 41, les
entrées différées des articles 20, 32, 33, 34, 36 et 37, la rétroactivité au 1er
janvier 2026 du c du 2° du I de l'article 14.

**F — Les montants d'exposé sont nommés comme tels.** Aucun n'est inscrit comme
chiffre de la mesure. Les 3,7 Md€ de l'article 7, les 0,3 Md€ des articles 6 et 8,
les 1,1 Md€ de l'article 12, les 5,6 Md€ de l'article 14 et les 4,0 Md€ de l'article
35 ne figurent au texte d'aucun de ces articles : trois d'entre eux ne figurent que
dans l'exposé **d'un autre article**, le 16. Les fiches le disent à chaque fois.

**G — Empreintes.** L'empreinte du PDF, le compte de pages et le compte d'articles
sont inscrits en tête de l'index et au fragment de journal. Rien n'est porté à
`methode/empreintes.json` : les livrables en `.md` de `livrables/` y figurent en
`sans_empreinte` par convention du fichier, et la pièce jointe n'est pas un document
du coffre.

## 20261001 — lisibilite-liste

*Reprise de lisibilité demandée par l'auteure sur la liste du PLFSS 2027. Jugée sur
le rendu regardé, pas sur le markdown : le PDF a été converti en image et lu.
Quatre défauts constatés, quatre règles portées au gabarit et au script — nulle part
ailleurs.*

**1. La clé de lecture était l'endroit le plus illisible de la page.** La légende
des poids courait en paragraphe justifié, pastilles de 3,2 px collées les unes aux
autres au milieu du texte. **Elle devient un tableau de quatre lignes**, au même
traitement que le tableau « annoncé / écrit ».

**2. Le fait et le commentaire avaient le même poids.** Tout sortait en 10 pt noir,
y compris les remarques en italique, qui font souvent la moitié d'une ligne
d'article. **L'italique passe en 9,2 pt gris `#3a3a3a`.** C'est le gain le plus
fort : le lecteur pressé lit les faits en noir et saute le reste, l'autre lit tout.
*Les titres de section et le sous-titre sont exemptés, sans quoi ils rétrécissaient
avec.*

**3. Les pastilles n'étaient pas décodables, et `●` seul était invisible.**
Disques portés de 3,2 à 4,2 px, espacés de 1,8 px, gris foncés de `#b4b4b4` à
`#8c8c8c` pour le poids simple, cercle vide bordé `#555`. Colonne élargie de 4,6 à
6 mm.

**4. Le texte entre accents graves sortait en chasse fixe.** `au texte` et
`annexe A` tombaient en police à chasse fixe au milieu d'un Times, par simple défaut
de la feuille de style. `code, tt, kbd, samp { font-family: inherit; font-style:
italic }`.

**Plus deux réglages de confort** : articles séparés de 2,8 mm au lieu de 1,4, et
`hyphenate-limit-chars: 6 3 3` pour interdire les coupes à deux lettres. Et deux
intertitres dans le chapeau — `## Les grandeurs`, `## Comment lire cette liste` —
sans quoi six paragraphes de même gris se lisent comme un mur.

**Coût : une page.** De 5 à 6 pages. L'air est le prix de la lisibilité, et il est
payé une fois pour tous les millésimes.

**Un faux défaut, inscrit pour ne pas être « corrigé » plus tard.** Au rendu en
image, `Md€` paraît collé au mot suivant. L'espace est bien présente : vérifiée en
extrayant le texte du PDF. Le contrôle d'une espace se fait sur le texte extrait,
jamais à l'œil sur une capture.

**Rien n'a été porté dans un troisième endroit.** Le gabarit `reference/gabarit_liste_articles.md`
et `livrables/rendre_liste_pdf.py` ont bougé ensemble, comme le gabarit l'exige. Le
script étant partagé, **les quatre règles valent aussi pour la liste du PLF 2027 à
son prochain rendu** — sans qu'il faille y toucher.

## 20261001 — plan-vehicule

Deux cadrages de l'auteure, une correction de mandat, et trois décisions de tambouille
prises par le fil.

## La règle de l'entonnoir — arbitrage de l'auteure du 20261001

**Tranché : le véhicule commande l'entrée dans une phase ; la phase commande la suite.**

On entre par la jambe que la fenêtre parlementaire oblige — la jambe fiscale d'abord
quand la première partie du PLF est en discussion. Une fois entré, on enchaîne le reste
de la phase en cohérence, et **on le publie tout de suite**, sans attendre la fenêtre de
dépôt de chaque jambe.

**Mots de l'auteure** : « il faut commencer par la partie fiscale de manière obligatoire,
mais on a probablement envie d'enchaîner en cohérence sur le reste de la phase et la
publier tout de suite. c'est juste une histoire d'entonnoir ».

**Ce que la décision emporte.** La publication se fait par phase, en bloc, et non par
véhicule : une phase ne sort pas en morceaux au rythme des fenêtres. Le dépôt de chaque
jambe, lui, suit la fenêtre de son véhicule — publication et dépôt sont deux horloges, et
la publication n'attend pas la seconde. L'éclatement d'une phase entre véhicules est donc
une contrainte de dépôt et non une contrainte d'écriture.

**Ce que la décision ferme.** Les deux questions que le mandat posait — ce qui commande
l'ordre quand phase et véhicule divergent, et ce qui se publie par véhicule plutôt que par
phase — sont closes par ce seul énoncé. Elles ne se reposent pas.

## Durée de la progressivité de M-026 — cadrage de l'auteure du 20261001

**Cadré, non arrêté : un à trois ans selon les cas.**

Le découpage — quelle durée pour quel secteur, et si la progressivité s'inscrit secteur par
secteur ou en bloc — **se propose par le fil qui rédige M-026 et se confirme par l'auteure**.
La fourchette est un cadre de travail ; elle ne s'écrit pas en l'état comme paramètre de
dispositif.

Porté à `livrables/arborescence_mesures_20260928.md`, M-026, en ligne `CADRAGE 20261001`
sous la ligne `TRANCHÉ 20260930`. La question sort de « ce qui reste ouvert sans cadre » et
devient une proposition due par le fil de rédaction.

## La règle de rattachement n'est pas périmée — correction du mandat

Le mandat du fil demandait de reprendre la règle « le rattachement au PLF 2026 est fabriqué
et déclaré comme tel » au motif que le dépôt du PLF 2027 la périmerait. **Le fil
commanditaire a retiré ce point du mandat le 20261001** : un texte financier en discussion
n'est pas du droit en vigueur, donc la base de travail ne bouge pas et le rattachement reste
fabriqué. Le point est porté par le fil de lecture des textes financiers 2027 ; il ne se
rejoue pas ailleurs.

La règle est laissée inchangée au plan et à `livrables/arborescence_mesures_20260928.md`.
Seule une note de renvoi est ajoutée au plan, pour que la question ne se repose pas à chaque
dépôt d'un texte financier.

## Tambouille tranchée par le fil

**La dimension véhicule est une section du plan, non un document neuf.** Elle croise les
phases sans les remplacer : un document séparé doublerait le plan et ferait diverger les
deux. Inscrite à `methode/plan_sept_phases_20260930.md`, section « La seconde dimension — le
véhicule », entre les phases et les quatre temps par mesure.

**Les trois colonnes sont nommées et rien de plus.** PLF première partie, PLF seconde
partie, PLFSS. Aucune ventilation des 66 mesures en jambes n'est écrite : la qualification
et le rattachement se font au projet machine. Le plan porte la grille, non ses cases. Les
seuls rattachements cités sont ceux qu'un arbitrage a déjà fermés — la jambe PLFSS de M-016.

**Une borne fermée devient une ligne `TRANCHÉ`, au même rang que la borne qu'elle
remplace ; un cadrage non arrêté devient une ligne `CADRAGE`.** À l'arborescence, une borne
close ne se supprime pas en silence : elle est remplacée en place par une ligne
`*TRANCHÉ AAAAMMJJ — …*` qui porte la décision et ce qu'elle laisse ouvert. Une orientation
donnée sans être arrêtée s'écrit en `*CADRAGE AAAAMMJJ — …*`, qui dit la fourchette et à qui
revient la proposition. La mesure garde ainsi la trace de ce qui a été fermé, et le fil
suivant lit la décision là où il lisait la question.

## 20261001 — reprise-grille-lecture

*Tambouille tranchée après coup, sur mesure. Le fil PLFSS a relevé son index avec
une grille plus faible que celle que le fil PLF avait arrêtée le même jour. Les
deux index n'étaient pas au même gabarit. **Une divergence ne se corrige pas au
résultat : c'est la grille qu'on reprend.***

**A — La grille du fil PLF est reprise telle quelle pour le PLFSS.** Les sept
règles de `methode/fragments/arbitrages/20261001-lecture-plf2027.md` — repère au
folio, profondeur bornée à deux niveaux, garde d'ordre, garde de rang 1, `I`/`V`/`X`
écartés du second niveau, blanchiment des passages cités à offsets préservés,
contexte de pièce mis à jour sur la seule formule de modification — sont portées à
la grammaire du PLFSS. Elles n'avaient pas été cherchées : le fil PLFSS a écrit la
sienne sans lire ce que le fil PLF avait versé deux heures plus tôt. **C'est la
faute, et elle est de réutilisation, pas de méthode.**

**B — Delta mesuré de la reprise.**

| | grille faible | grille reprise |
|---|---|---|
| mesures | 314 | **251** |
| sièges vides | 95 | **68** |
| mesures à siège relevé | 219 | **183** |
| profondeur maximale de référence | 4 niveaux (`I-C-1-a`) | **2 niveaux** (`I-C`) |

Le blanchiment des citations est ce qui pèse le plus : l'article 9 passait de
**20 à 6 adresses** une fois le droit à venir écarté du relevé des sièges. La borne
de profondeur explique le reste : l'article 7 passe de 19 à 11 mesures, l'article 34
de 34 à 24.

**C — Le classement des articles les plus chargés change, et la sélection des
fiches avec lui.** Sous la grille reprise, les cinq plus chargés sont l'article 27
(21 adresses), le **4** (20), le 34 (19), le 33 (14) et le 41 (13). **L'article 4 —
cotisants sinistrés et sapeurs-pompiers volontaires — entre au critère et reçoit sa
fiche** ; elle relève que le VI écarte expressément la compensation par l'État des
exonérations qu'il crée.

**D — Les fiches 20, 28 et 32 sont conservées, et déclarées.** Elles avaient été
retenues au titre des articles les plus chargés sous la grille faible ; elles n'y
sont plus. *La règle du fil PLF est que le critère se reprend et que l'auteure seule
le fait : les retirer serait trancher du fond. Elles restent, marquées en tête du
livrable.* Question portée à `methode/a_trancher.md`.

**E — Propagation du jour même.** Les quatre pièces du PLFSS portent les comptes
corrigés : index régénéré, fiches recomptées et augmentées de l'article 4, liste par
article et note lisible mises à jour. Rien n'a été laissé à un fil suivant.

**F — Le prompt de fil est corrigé là où la règle est lue**, et non doublé par un
document neuf. `methode/prompt_fil_lecture_textes_2027.md` porte désormais : les
**quatre** pièces de lecture au lieu de deux, la grille de relevé en sept règles, le
critère de mesure principale à la maille de l'article, la consigne d'entrées
différées bornée au relevé interne, la règle des intitulés d'article non acquis d'un
millésime à l'autre, et la consigne de lire ce que le fil du premier véhicule a
versé avant d'écrire quoi que ce soit.

## 20261001 — tenue-apres-poussee

### Un assemblage se compte en sections, pas en octets

Assembler `arbitrages.md` en l'état perdait onze sections pour un rétrécissement
de 9 863 o seulement. Aucun contrôle de taille n'aurait vu la faute.

Tranché en propre : **un assemblage se joue d'abord sur une copie jetable, et
la mesure porte sur le compte des sections avant et après.** Un assemblage qui
en perd une ne se verse pas.

### Une section sans fragment se reprend au-dessus de la marque

Plutôt que d'inventer des fragments pour onze sections dont les originaux
n'existent plus — ce qui aurait fait passer du verbatim par le modèle et aurait
donné un nom de fil à deux sections qui n'en ont jamais eu —, les onze sections
ont été découpées à l'octet de la queue et replacées dans la tête, sous un
avertissement daté.

Tranché en propre : **la tête d'un cumulatif est le lieu de ce qu'aucun
fragment ne reproduit.** Un assemblage ne la touche pas, donc elle ne se reperd
pas. Résultat mesuré : 79 sections, 0 perdue, rejeu inchangé.

### Un journal perdu se rebâtit avec son constat de perte en tête

`methode/journal.md` est introuvable. Repartir d'un fichier vide aurait effacé
la perte elle-même : dans six mois, rien n'aurait dit que 4 875 lignes
manquaient.

Tranché en propre : **la tête du journal rebâti porte le constat, l'empreinte du
document disparu et la consigne de remise.** Une copie retrouvée se reconnaît à
son sha256 et se remet au-dessus de la marque sans rien réécrire de ce qui suit.

### La restauration hors table curée ne sert qu'à mesurer

Trois fragments d'arbitrages du 20261001 sortent `hors index` de
`appareil/restaurer.py`. Ils ont été restaurés par copie d'octets en appelant
`restaurer.moisson()` directement, sans écrire de module neuf.

Tranché en propre : cette voie mesure, elle ne verse pas. La dette de
déclaration qu'elle révèle s'inscrit plutôt que de se contourner.

### L'archive d'un coffre se prouve par relecture, pas par écriture

L'archive remise porte son propre manifeste — sha256, taille et chemin des 172
documents — et elle a été décompressée ailleurs puis recomparée ligne à ligne
avant d'être rendue.

Tranché en propre : **une archive n'est archivée qu'une fois relue.** 172
conformes, 0 divergent, 0 absent.

### Un délestage s'inscrit avant d'être joué

Le registre des sorties a été écrit, avec les quinze empreintes, **avant** la
première suppression.

Tranché en propre : l'ordre n'est pas cosmétique. Si la session meurt au milieu,
le registre dit déjà ce qui devait partir et où le retrouver.

### Le scratch d'atelier n'est pas de l'appareil

La moisson du transcript a eu besoin d'une variante qui relève aussi les
documents rendus comme fichier, ce que `restaurer.py` ne fait pas. Elle a été
écrite au scratchpad de session, pas sous `appareil/`.

Tranché en propre : un outil d'une seule session vit au scratchpad, ne se verse
pas, ne se pousse pas, et ne crée donc aucune dette de paquet.
