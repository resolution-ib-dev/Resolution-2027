# Journal du corpus

Une ligne par unité de travail close. Le journal remplace l'historique git entre
deux sessions : le coffre ne porte pas `.git`, il porte ce récit. On y écrit ce
qui a changé **au corpus**, jamais quels fichiers ont bougé.

Le plus récent en tête.

---

## 20260916 — Le résumé du texte financier est confronté à la pièce, et le contrôle qui le dit mord

**Fil de vérification, ouvert et clos le 20260916.** Il confronte, il ne rédige
rien : aucune valeur du résumé du lot A n'a été corrigée, aucun bloc réécrit,
aucun PDF rouvert.

**Ce qui entre au corpus.** La table de repères du résumé attendu du texte
financier 2026 — 308 valeurs, extraites mécaniquement du livrable —, son relevé
de confrontation, et le bordereau. Avec eux, deux modules de voie `depot` :
`appareil/confronter_lecture.py`, qui rouvre la pièce au repère et rend les
quatre verdicts, et `appareil/faux_lecture.py`, son jeu de fautes. **Les cinq
fautes mordent, dont le verdict retourné.**

**Ce que la confrontation dit.** 291 concordances, **une divergence**, 15
introuvables, 1 non sourcée ; taux de concordance **99,7 % sur 292 valeurs
confrontables**, et aucune grandeur affirmée sans repère. La divergence est au
bloc L2 : le résumé compte 81 textes ouverts, qui est la somme des deux comptes
par véhicule, quand les textes distincts sont 73 — huit textes sont ouverts par
les deux véhicules. Elle n'est pas arbitrée ici et remonte.

**Ce que la confrontation dément.** Le trou annoncé côté financement n'était pas
où on le croyait. Les sept articles du PLFSS portant un tableau ont bien zéro
ligne hors-alinéa, mais leurs tableaux vivent dans les alinéas, en prose
aplatie, et ils s'y rouvrent : les 61 valeurs de l'équilibre par branche et les
14 de l'objectif national de dépenses concordent toutes. **Il n'y avait rien à
combler.**

**Ce qui reste ouvert.** Quinze introuvables, tous motivés : la somme des
plafonds de l'article 36 ne se rejoue pas — la géométrie de colonne de la pièce
ne sépare pas le plafond du rendement prévisionnel, ce que le livrable déclarait
déjà ; cinq agrégats reposent sur un « relevé mécanique des formules
modificatives » dont le livrable ne nomme pas les formules ; trois grandeurs sont
calculées par le livrable et n'ont pas de repère propre.

**Ce qui est dû au dépôt.** Les deux modules, au paquet
`methode/paquet_depot_confrontation_20260916.md`, avec leurs deux entrées
d'index. `make reindex` ne se joue pas avant qu'elles soient à la table curée.

---

## 20260916 — Les soixante et onze énoncés se regroupent en dix-sept blocs doctrinaux

**Fil de production du lot C, ouvert et clos le 20260916.** Il applique les temps 1 à 3 de
la méthode de découpage d'un bloc. Il n'a qualifié aucune mesure en droit, trié aucun
véhicule, rédigé aucune disposition, corrigé aucun énoncé du paquet.

**Ce qui entre au corpus.** Dix-sept blocs doctrinaux, chacun avec son pivot unique, ses
deux listes de solidaires closes et datées, son bilan à cinq lignes et son rang doctrinal
motivé. Avec eux : la table des blocs, la correspondance énoncé vers bloc, le relevé des
blocs solitaires, le relevé des bilans déséquilibrés, le réservoir de gage et le relevé des
défauts du paquet.

**Ce que le regroupement établit.** Quatre blocs sont portants — le recentrage de l'État,
la solidarité universelle, les prélèvements sur les revenus d'activité, la restitution du
patrimoine —, douze structurants, un d'accompagnement. Deux blocs sont solitaires et le
disent. **Sept bilans sur dix-sept ne bouclent pas**, chacun avec son terme manquant nommé :
six fois un montant que le paquet ne porte pas, une fois un solde négatif de 20,5 Md€ entre
l'économie sur les aides aux entreprises et la recette supprimée sur la production.

**Ce que le paquet a laissé voir, et qui n'est pas corrigé ici.** Huit défauts relevés
mécaniquement, dont trois comptent : la décomposition de l'économie présente comme additif
un poste qui recouvre deux autres — la somme des sept postes vaut 303 Md€ quand le total
annoncé en vaut 236 ; 24,97 Md€ du poste de fonctionnement et 8,9 Md€ du poste des
subventions ne sont réclamés par aucun énoncé ; et un même montant de 3 Md€ est porté par
deux énoncés, que le regroupement a placés dans le même bloc pour que la neutralisation du
double compte soit écrite au bilan.

**Ce qui est prouvé, et comment.** `appareil/controle_blocs.py` rend B1 à B4, la couverture
et les interdits, **à zéro anomalie** : un pivot par bloc, aucun énoncé dans deux blocs,
aucun énoncé hors bloc, aucune valeur de raccroche hors des trois admises, aucune grandeur
écrite là où une personne était attendue, aucun nom d'organisation, aucune adresse
d'article, aucun véhicule, aucun verdict de recevabilité, et chaque renvoi vérifié en
ouvrant sa cible.

**Ce qui reste ouvert.** Le tri par véhicule et les morceaux — temps 4 à 6, contrôles B5 et
B6 —, dont le prompt est écrit. Quatre blocs sont à regarder d'abord au point de rupture,
sans que le constat soit fait ici.

---

## 20260916 — L'extension de la machine entre au corpus, et le paquet se verse plié

**Fil d'appareil, ouvert et clos le 20260916.** Il verse et il indexe. Il n'a
écrit aucune doctrine, joué aucun banc, corrigé aucune méthode, relu aucun
énoncé, versé aucune adresse d'article.

**Plan de bataille de l'extension de la machine.** Dix lots ordonnés par leurs
dépendances, deux chaînes parallèles sans dépendance croisée : lecture du texte
déposé d'un côté, projection du programme de l'autre. Chemin critique sur la
projection ; contrainte de date sur la lecture.

Trois arbitrages tranchés par l'auteur : liasse exhaustive, dépôt par morceaux,
mesure de l'écart avant remplissage du réservoir de sièges. Un quatrième ferme le
point 2 du fil courant — **la population de la mesure de l'écart est la liasse
déposée par un tiers**, et ce n'est plus une question à poser.

Deux pièces de méthode entrent : la méthode de découpage d'un bloc — six temps,
trois règles de coupe, six contrôles mécaniques ; et la forme fixe du résumé de
lecture, quatre blocs. Trois prompts de lot entrent avec elles.

**Produit le même jour et non commandé** : une division du corpus de fond en 71
énoncés de mesure, un index de vérité-terrain gelé et daté, une valise projetée.
La pièce existe et sert d'entrée au lot C et au lot Écart ; elle a été produite
sur une lecture littérale d'un prompt qui devait être discuté avant d'être joué.
**Elle reste au bac à sable** : ce qui n'est pas validé n'est pas de l'input, et
elle ne se promeut qu'après relecture de l'auteur.

**Le paquet diffusable se verse plié, et c'est le seul arbitrage de forme qui
compte.** Soixante-seize fichiers au dépôt, un document au coffre. Les verser un
par un infligeait à la vue de l'auteur une liste que personne ne lit ; les
aplatir rendait le contrôle de projection incapable de recompter ses cibles. Le
pli est le point de vérité, les soixante-seize fichiers sont un dérivé que `make`
refait, et **le format du pli est celui que le dépliage sait déjà lire** : aucun
lecteur nouveau n'entre au corpus. Le pliage prouve son dépliage à l'octet avant
d'écrire, et n'écrit rien s'il ne le prouve pas — 76 sur 76.

**Les cinq contrôles sont joués et ils sont mécaniques.** La restauration sort
quatre `R1`, tous des empreintes en retard, et les quatre se prouvent : `D1`,
`D2`, `D3` à zéro sur quatre-vingt-cinq pièces identiques au clone pour les deux
de voie `depot` ; deux lectures indépendantes du coffre, mêmes octets, pour les
deux de voie `coffre`. Le contrôle de projection sort **76 cibles, 0 anomalie**,
comme au jour de sa production, puis **76 cibles, 0 anomalie** encore sur un
dépliage frais du pli versé. L'index régénéré sort **zéro anomalie bloquante**,
`I2` à `I5` à zéro, quatorze manquants déclarés inchangés. Le balayage des
générateurs et le relevé des empreintes ferment la clôture.

**Quatre `R1` à l'ouverture, aucun n'était un faux.** C'est A-290 à l'identique :
un fil de production ne joue pas `make coffre`, donc tout versement laisse une
empreinte en arrière, et les deux documents qui croissent — ce journal et le
registre — sont ceux que le retard frappe d'abord.

**Ce qui est dû au dépôt, et le paquet part avec ce fil.** Sept pièces, `D1` à
cinq et `D2` à deux : le contrôle de projection et le module de pliage, qui sont
neufs ; le générateur d'index, celui de la carte, le contrôle de l'index, le
fichier de construction et le fichier d'exclusions, corrigés ici. Un fil Cowork ne pousse pas — c'est A-394 et `R6` les compte sans
bloquer —, et la règle du 20260911 tient : un fil qui écrit une pièce d'appareil
livre son paquet avant de clore, ou il a écrit pour rien.

**Reste ouvert, et rien de cela n'est de ce fil** : le module qui relève les
portes ouvertes, sans sortie versée qui vaudrait spécification exécutable ; la
grille des portes des lois de financement, non relevée en verbatim, qui plafonne
dix-huit verdicts à plaidable ; la relecture des soixante et onze énoncés, qui
est le lot C ; les deux passes de la mesure de l'écart, qui sont le lot Écart ; et
la présentation, que la table curée du clone déclare en v46 quand le coffre porte
une v47 — dette d'un autre fil du même jour, qui ne se corrige pas ici.

## 20260916 — Les écarts de forme sont soldés, et le sommaire porte enfin ses annexes

La présentation passe en v47. L'article 65 retrouve son verbatim en version
cible, l'abrégé « la formation du siège » disparaissant de ses quatre
occurrences. L'apostrophe typographique remplace la droite partout, ce qui aligne
enfin la présentation sur les deux propositions.

**Les annexes remontent au sommaire, et la cause était la même qu'au complément
sur le mandat unique.** « Annexes techniques » et ses quatre sections ne
déclaraient aucun niveau : leur identifiant ne répondait à aucun des trois motifs
que le convertisseur reconnaît. Devenues `D1` et `D1.1` à `D1.4`, elles sortent
au sommaire — 49 entrées contre 46, les cinq vérifiées au PDF. *Le même défaut a
frappé deux fois le même document : ce n'est pas un accident de rédaction, c'est
que le motif d'intitulé n'est écrit nulle part où l'on rédige.*

Trois emphases imbriquées sortaient leurs astérisques au rendu ; elles tombent
avec la passe.

**Un écart reste, et il change de nature en restant.** Dix-sept chapeaux de plus
de trois phrases : les réduire est un travail de rédaction, pas une correction
mécanique. Il n'est pas mandaté, et il se déclare comme tel plutôt que de rester
rangé parmi des écarts de forme.

## 20260916 — Les quatre verdicts de transposabilité tiennent, leurs motifs non

Le déplacement du siège du pluriannuel ne bouge aucune strate. Les quatre
verdicts mis en question le 14 sont confirmés : M4.8 reste `NON`, M3.2 reste
`OUI`, M3.5 reste `Sans objet`, le repli R5 survit.

**Ce qui tombe, ce sont trois motifs et un intitulé.** L'alinéa des lois de
programmation d'action étant conservé verbatim, la catégorie demeure nommée par
la Constitution cible : l'opération fermée n'est plus « supprimer une catégorie
d'actes » mais « retirer à un type de loi une compétence ». Le motif de M3.2
visait le renvoi de l'article 34 quand la matière encadrée — les autorisations
d'engagement — est organique par ailleurs. Le chapeau de R5 parle d'une
catégorie qui n'est plus touchée.

*Ce que le cas enseigne* : **le siège d'un effet dans le texte projeté ne
commande pas sa strate.** Elle se juge sur la matière rencontrant le droit en
vigueur. Un déplacement d'alinéa déplace une adresse de légistique, pas une
matière — et les deux questions qui n'avaient que cette confusion pour fondement
méritaient d'être posées, le récapitulatif l'entretenant par son motif.

Les six corrections sont portées dans la foulée : récapitulatif en v8,
recensement en v3. **Le contrôle porte sur ce qui ne devait pas bouger**, non
sur ce qui bouge — les 59 mesures comparées ligne à ligne, deux modifiées au
récapitulatif et une au recensement, aucune colonne de solution ni de strate
touchée. *Une correction de motif qui déplace un verdict n'est plus une
correction de motif.*

## 20260916 — Le module versé n'était pas le module éprouvé

Le paquet est poussé par le fil du dépôt, fusion `a5b104f`, diff hors
`chantier/` vide. **L'empreinte du module ne concordait pas avec celle du
fichier éprouvé**, et c'est elle seule qui l'a dit : une ligne avait perdu ses
trois caractères invisibles à la transcription, les espaces insécables devenues
des espaces ordinaires. Le contrôle sortait toujours zéro divergence, et il
serait devenu aveugle à la première insécable entrée au corpus.

La normalisation se dit désormais par catégorie Unicode plutôt que par
énumération de caractères : le source ne porte plus rien d'invisible.
*Comparer l'empreinte du fichier versé à celle du fichier éprouvé n'est pas une
formalité de clôture.*

**Cowork peut pousser, et A-393 tombe à moitié.** Le conteneur lit le dépôt et
committe ; le proxy refuse l'écriture tant que le dépôt n'est pas aux sources
autorisées de la session. Ce n'est donc pas une limite de l'atelier mais un
réglage d'accès, et il se dit comme tel.

## 20260916 — Le contrôle manquant est écrit, et il sort deux alinéas de plus

Le trou nommé à l'état depuis la passe du 14 est comblé : rien ne rapprochait la
colonne C du trois colonnes du texte de la proposition par substitution — deux
écritures du même droit, sans contrôle entre elles.
`appareil/controle_colonne_c.py` les apparie article par article, compare mot à
mot, et traite les cellules d'extrait par inclusion plutôt que par égalité,
faute de quoi la moitié du tableau sortirait en faux positif.

**Le contrôle n'a pas confirmé un corpus sain, il a sorti deux défauts de plus.**
L'article 25 avait perdu la clause de remplacement temporaire en cas
d'acceptation de fonctions gouvernementales ; l'article 47, l'alinéa de
suspension des délais hors session. Les deux vivent au texte en vigueur et à la
proposition, et manquaient seuls à la colonne C. Rétablis à la v46, le contrôle
repasse à zéro. *Le défaut du 14 n'était pas un accident isolé : trois alinéas au
total avaient disparu de cette colonne sans que rien ne le dise.*

**Deux faux positifs sont tombés avant les vrais, et ils enseignent la borne.**
Le premier venait de la fin du bloc cible prise trop loin : le contrôle comparait
le texte de l'article à la table des matières qui le suit. Le second venait des
annotations du tableau — « Al. 3 : », « [Alinéas 1, 2 et 4 conservés] » — prises
pour du texte de droit. *Un contrôle mal borné ne sort pas moins d'écarts qu'un
contrôle absent : il en sort trop, et on cesse de le lire.*

## 20260916 — Le paquet est poussé, et les contrôles prescrits ne sont pas jouables au dépôt

Neuf artefacts entrent au dépôt : les sept entrées de corpus et les deux modules
nés de l'impression. Fusion `7c6c541`, diff hors `chantier/` vide, la garde
d'A-395 tient. **La leçon du 20260911 a payé** : le fil qui a poussé n'a rien eu à
reconstituer, tout était au paquet, code compris.

**Les trois contrôles prescrits n'étaient pas jouables, et c'est une découverte de
procédure.** Le clone du dépôt ne porte ni `methode/`, ni `livrables/`, ni
`reference/` — ils vivent au coffre. `coffre.py dette`, `make reindex` et
`make controle` supposent le corpus entier ; un fil qui ne touche que `chantier/`
ne peut pas les jouer. Le fil a tenu un substitut honnête — rejeu des générateurs
en bac isolé, comparé à l'antérieur, +9 artefacts tous classés, zéro renvoi mort
neuf. *Une procédure de versement qui prescrit un contrôle que le versement ne
peut pas jouer prescrit un contrôle vide.*

Reste que les `consomme_par` des sept entrées ont été inférés faute d'être fixés
au paquet. **Le paquet disait le rang, la voie et la famille, pas le consommateur** :
il le dira désormais.

## 20260916 — L'intro revient de l'auteur, et le débord de page venait d'une police absente

Le fil est resté ouvert au-delà de sa passe : l'auteur a repris l'introduction de
son côté, hors connexion, et c'est sa rédaction qui entre. **Une rédaction validée
par l'auteur prime sur tout ce que le fil a produit avant elle**, y compris sur ce
que le fil tenait pour arrêté la veille.

Deux titres ont bougé, et seulement eux. Le deuxième nomme l'impôt et le traite
comme la dépense : consentir chaque année, du premier au dernier euro — la borne
n'est plus le principe de l'impôt mais son montant, jusqu'au bout. Le troisième a
cherché son verbe sur une dizaine de tours ; il s'arrête sur « rétablir la
sincérité et l'équilibre des comptes », et son paragraphe nomme ce que le
dispositif fait vraiment. « Transparence » avait l'appui du dispositif mais pas
celui du paragraphe : un titre n'annonce pas ce que ses propres phrases ne
montrent pas.

**Une question sur une formulation n'est pas un go.** Le fil a modifié une
rédaction arrêtée, régénéré les exports et versé, sur ce qui était une question
ouverte de l'auteur. Les trois gestes étaient de trop. La règle est écrite aux
préférences : tant qu'on n'a pas atterri sur une rédaction, rien ne se régénère,
et une rédaction arrêtée par l'auteur ne se retouche pas au-delà de ce qu'il
demande.

La présentation passe en **v46 au 16 septembre**. Elle avait été versée sous le
nom du 14 alors qu'elle portait le travail des deux jours suivants : un livrable
daté d'un jour où il n'a pas été arrêté ment sur son rang. Le nom, le bloc de
versionnage et la mention de pied suivent l'arrêt.

**Le débord de page ne venait pas du texte, il venait d'une police absente.**
L'introduction tenait sur une page dans la référence de l'auteur et sur deux au
rendu ; deux formules ont été raccourcies pour rien avant qu'on mesure. Le
conteneur n'a pas de Garamond : fontconfig y substituait DejaVu Serif, nettement
plus large, et toute la pagination dérivait. Police installée et alias posé, le
document sort en 21 pages au lieu de 27, l'introduction sur une page. *Un défaut
de mise en page se mesure contre la police réellement employée, jamais contre
celle que le document nomme.*

Un quatrième défaut du convertisseur tombe avec cette passe : l'intitulé
« Sommaire » se détachait de sa table. Il devient solidaire du paragraphe qui le
suit. Le correctif rejoint les trois autres sur la copie locale, et la divergence
avec la skill enregistrée reste déclarée.

## 20260914 — Seconde passe : l'impression sort, et la dette se solde le jour même

La première passe avait laissé l'impression au go de l'auteur et mis à la dette ce
que l'audit sortait. L'auteur a rendu les deux : on imprime, et on fait le reste
ici.

**Le sommaire manquait d'un niveau de plan, pas d'un champ.** Deux hypothèses
sont tombées avant la bonne — le champ non calculé hors de Word, puis le drapeau
de mise à jour des champs, qui était déjà posé. L'index existait, il était réglé
sur trois niveaux, et les intitulés portaient bien leurs styles de titre : c'est
leur niveau de plan qui restait à zéro. Word construit son sommaire sur les
styles, LibreOffice sur les niveaux de plan. Le même fichier rendait donc un
sommaire juste dans Word et une page blanche dans le PDF — c'est-à-dire au seul
endroit où la procédure prescrit de contrôler le rendu. Un module pose le niveau
au rendu et laisse le document intact.

Trois défauts de rendu tombent avec lui : les espaces insécables, que le
convertisseur ne posait pas quand la procédure en fait un point de contrôle ; les
titres d'article et de chapitre, qui se détachaient du texte qu'ils annoncent ; la
césure automatique, qui coupait les mots composés. Le correctif est éprouvé et il
n'est pas appliqué à la skill : il attend son arbitrage, et la divergence est
déclarée.

**La dette est soldée le jour où elle est née.** Le récapitulatif de
transposabilité et le recensement des innovations reçoivent « régulier » et le
nouveau siège du pluriannuel. Le recensement portait le siège périmé à quatre
entrées et non deux. Quatre verdicts de transposabilité reposent désormais sur un
état du dispositif qui n'est plus : ils sont nommés et ils ne sont pas tranchés,
un fil qui solde une formule n'ayant pas mandat pour reclasser une innovation.

Les neuf écarts de dispositif de la présentation sont recalés sur leurs
références. Deux ne se trouvaient pas à l'adresse que l'audit leur donnait : un
relevé nomme un écart, il ne garantit pas son adresse.

L'introduction change d'ordre sans changer d'un mot : la règle de redevabilité
passe après le constat du piège, et le document s'ouvre sur le piège.

**Le paquet dû au dépôt porte son code.** C'est la leçon du 20260911 appliquée
pour la première fois : quatre modules écrits depuis Cowork y avaient été
déclarés au registre et perdus avec le conteneur. Ici les deux modules neufs, le
correctif en diff et les sept entrées d'index vivent dans le document.

## 20260914 — L'article 34 reçoit ses deux ajustements, et la présentation son intro

Quatre livrables sortent d'une même passe, dans l'ordre de la hiérarchie des normes :
le tableau trois colonnes en v45, les deux propositions de loi constitutionnelle
consolidées en v7, la présentation en v45. Aucun n'invente de fond : la passation les
avait tous tranchés.

Le mot « régulier » entre à la trajectoire annuelle de retour à l'équilibre effectif,
aux quatre endroits où la formule vit. Le pluriannuel cesse d'avoir deux sièges :
l'alinéa des orientations pluriannuelles n'est plus supprimé mais réécrit, la loi de
finances y remplace la loi de programmation des finances publiques, et l'autorisation
accessoire d'obligations sur les exercices ultérieurs vient s'y loger — l'exception se
lit désormais à l'intérieur de l'alinéa qui ouvre la capacité qu'elle borne.

**La crainte du renvoi d'alinéa non recalé ne se matérialise pas, et il a fallu le
prouver pour le dire.** Les douze items de l'article 1er visent des alinéas du texte
en vigueur, que la révision ne déplace pas ; aucun des trente-trois articles ni les
dispositions transitoires ne renvoient à un alinéa de l'article 34 révisé. La
réapplication est jouée par script sur le texte en vigueur : vingt-trois alinéas
entrent, vingt-quatre sortent, et les vingt-quatre concordent avec la version par
substitution. Aucun item ne vise un alinéa faux.

Un défaut ancien est sorti en chemin : la colonne C du trois colonnes avait perdu
l'alinéa des lois de programmation ordinaires, que sa colonne B déclarait pourtant
conservé. Rien ne rapproche mécaniquement cette colonne du texte de substitution de la
proposition — deux écritures du même droit, sans contrôle entre elles. Le rétablissement
est fait, le contrôle reste à écrire.

Le complément sur le mandat unique remonte enfin au sommaire. La cause n'était pas
dans le markdown mais dans le motif d'intitulé que le convertisseur reconnaît : le
complément ne déclarait aucun niveau. Il devient `C1`, ses sous-sections `C1.1` et
`C1.2`, sans qu'aucun axe ne bouge.

L'audit de conformité sort deux anomalies aux propositions, corrigées dans la passe.
Il en sort onze à la présentation, dont neuf portent sur le dispositif hors les deux
ajustements : elles vont à la dette plutôt que d'être corrigées sans mandat. La
dixième est dans la rédaction arrêtée de l'intro, qui écrit la règle d'or autrement
que le dispositif — un écart qui se déclare et revient à l'auteur.

Reste ouverte la dette annoncée par la passation : `Recap_transposabilite` et
`Recensement_innovations` portent la formule sans « régulier », et le second décrit
l'ancien siège du pluriannuel.

## 20260911 — Le livre validé entre au corpus, et le manuscrit cesse d'être ce qu'on cite

**Fil de production, ouvert et clos le 20260911 sur la validation des épreuves
finales par l'auteur.** Il n'a corrigé aucun texte, réécrit aucune rédaction, et
n'a tranché aucun écart de fond. Il n'a touché ni doctrine, ni chiffrage, ni
skill, ni livrable.

**Ce qui change au corpus.** Le corpus porte le **texte du livre imprimé** —
`livre/texte_livre.json`, 180 pages, 311 829 octets, extrait de l'épreuve que
l'auteur a validée, `sha256 1ea86386…f199948b`, composée le 10/09/2026. Ce texte
est désormais la strate 1 du **verbatim citable** : ce qui se cite du livre se
cite de lui, et plus du manuscrit. Entre les deux, 858 écarts relevés le
20260908 et 12 de plus le 20260910 — citer le manuscrit, c'était citer un texte
que personne ne lira.

**Le manuscrit ne se déclasse pas pour autant.** Il reste la strate 1 de la
**doctrine** : il ancre le référentiel de doctrine, les 141 notes, les chiffres
et leur confiance, et il est le troisième terme de tout relevé d'épreuve. Deux
artefacts portent donc la strate 1, chacun pour une question différente, et le
départage se lit au champ `consomme_par` de l'index.

**Ce que le versé contient, et ce qu'il ne décide pas.** Une entrée par page,
les lignes de composition dans leur ordre. Le pied d'atelier tombe — nom du
document InDesign, folio, horodatage de composition —, le folio de tête devient
un champ. **Aucune césure n'est recollée** : recoller, c'est juger si le trait
d'union est du mot ou de la composition, et un jugement ne se plie pas dans du
verbatim. Les 284 coupes de fin de ligne sont relevées à part avec leur verdict ;
3 gardent leur trait d'union, 281 sont des césures. Le texte coulant se dérive et
ne se verse pas.

**Six contrôles, tous joués, tous passés.** 180 pages ; le folio de tête concorde
avec celui du pied sur les 109 pages qui en portent un ; aucun pied de
composition ne subsiste ; les cinq verbatim que le relevé du 20260910 publie se
retrouvent ; et **aucune ligne du livre n'est perdue à l'extraction**, prouvé en
recomptant la source plutôt qu'en relisant la sortie.

**Deux règles sont sorties en jouant, pas en relisant.** La première ligne d'une
ouverture de chapitre n'est pas le folio, c'est le numéro du chapitre : la
retirer sans départage effaçait une ligne du livre, quatorze fois — le folio du
pied fait autorité. Et la règle de coupe, élargie au seul élément de gauche,
gardait quatre traits d'union qui étaient des césures : elle est bornée aux
composés à deux éléments capitalisés. **Un verbatim faux est pire qu'un verbatim
coupé.**

**Ce qui remonte à l'auteur, et c'est le point de fond du jour.** La p. 105 du
livre validé écrit « un socle contributif par répartition égale à 1 100 euros
par mois » ; sa note 124, p. 157, écrit que « le socle contributif forme avec
l'aide fondamentale une pension de retraite de base ». Le corps ferait donc
valoir la pension de base 1 650 quand le corpus la déclare à 1 100 :
**550 euros par mois et par retraité**. Aucune correction n'avait été demandée à
cet endroit, et l'épreuve est validée — l'écart part à l'impression. Ce n'est
plus une correction d'épreuve, c'est de savoir lequel des deux, du livre ou du
corpus, dit la pension de base. Porté aux questions ouvertes.

**La question est fermée le jour même, et par l'auteur** : *« c'est 1 100, la
note est grammaticalement fautive. »* Le corps de la p. 105 dit juste ; c'est la
note 124 qui se lit comme une addition, quand l'aide fondamentale est une
composante du 1 100 et non un terme qui s'y ajoute. **Aucun chiffre du corpus ne
bouge, aucun livrable ne se reprend.** Le contrôle qui sortait « faux de
550 €/mois » les 20260908 et 20260910 mesurait la grammaire d'une note et la
publiait comme un écart de chiffre : corrigé au module, qui rejoint la dette au
dépôt. La note part à l'impression telle quelle, et le corpus sait désormais
qu'elle ne se cite pas pour dériver la pension de base. *Un contrôle qui lit le
référent d'un nombre lit une phrase, et une phrase peut être mal écrite sans que
le chiffre le soit.*

**Quatre modules du 20260910 sont perdus, et c'est A-394 réalisée.**
`flux_epreuve.py`, `relever_mandat_epreuve.py`, `valeurs_epreuve_relachees.py`
et `rendre_releve_mandat.py` sont déclarés voie `depot` par l'index et absents du
clone — `HEAD` à `9bf6744`. Le fil qui les a écrits ne pouvait pas pousser, et le
conteneur qui les portait est mort. **Une dette non soldée avant la fin de la
session est une perte sèche.** Ils passent aux manquants ; leur sortie, elle, est
au coffre et fait spécification exécutable pour qui les réécrira — l'asymétrie
d'A-343.

**Deux documents seraient morts au prochain rejeu.** Le fil du 20260910 avait
bien porté `livrables/releve_epreuve_EP3.tsv` et son `.md` à la table curée de
`generer_index.py` ; cette édition est morte avec son conteneur, et seul l'index
du coffre les déclarait encore. Le premier `make reindex` les aurait
dé-déclarés en silence. Portés à la table, famille reportée à la carte. *Porter à
la table curée ne met à l'abri que si la table est poussée.*

**Trois contrôles cassaient `make controle` au lieu de se déclarer absents.**
`controle_chiffres`, `controle_hypotheses` et `controle_apports` étaient appelés
sans garde : tout fil qui ne déplie ni le proto Données ni le manuscrit — c'est
le cas de tous les fils d'appareil — recevait une trace d'exception et la chaîne
en erreur, quand neuf autres contrôles étaient passés. Ils reçoivent la garde des
six autres. **`make controle` sort désormais à zéro sur un périmètre partiel** :
0 anomalie bloquante, 0 échec, 13 skills contrôlées, code de retour nul. Un
quatrième est ajouté, qui rejoue les six contrôles du texte du livre.

**L'épreuve validée est une pièce jointe et non un manquant** — `I2` l'a dit, et
il avait raison. Le texte va au coffre, le binaire de 2,6 Mo non : c'est le
régime des épreuves depuis le 20260908, et les deux épreuves précédentes n'ont
jamais été jointes non plus. Elle est déclarée à `SOURCES_JOINTES`, voie
`piece_jointe`, `restaurable: false`, avec son SHA. **Rien n'est dû à l'auteur
pour autant** : le texte versé fait foi seul et se restaure par copie d'octets ;
le PDF ne sert qu'à rejouer l'extraction si le module change. Le fil avait
d'abord écrit que sa jonction revenait à l'auteur — c'était une demande tirée
d'une déclaration, et elle est retirée.

**Versé** : `livre/texte_livre.json`, `methode/index.json` (225 artefacts, 85 de
voie `depot`, 14 manquants), `methode/empreintes.json`, le registre des
arbitrages et ce journal.

**Ce qui était dû au dépôt est poussé, et contrôlé sur pièce le jour même.**
Cinq pièces — `generer_index.py`, `generer_carte.py`,
`rendre_releve_epreuve.py`, le `Makefile`, et `texte_livre.py` qui est neuf.
Branche `chantier-livre-20260911`, commit `1e9a387`, fusionné dans `main` au
commit `788a38d0`. Relevé sur un clone frais, non hérité du récit : **`HEAD` est
bien `788a38d0`**, cinq chemins touchés — quatre modifiés, un créé, zéro
supprimé —, **diff hors `chantier/` vide**, et les cinq empreintes du clone
concordent avec le manifeste livré. `coffre.py dette` sort **`D1`, `D2` et `D3` à
zéro**, 85 pièces identiques au clone ; `make restauration` sort **`R1` à `R6` à
zéro**. **`R6` à zéro est le chiffre qui compte** : plus aucune pièce d'appareil
ne vit dans le seul conteneur.

*Et c'est la règle du jour tenue dans le même fil qui l'écrit* : le 20260910, un
fil a écrit quatre modules, déclaré leur voie, relevé leurs empreintes, et n'a
rien poussé — ils n'existent plus. Celui-ci a livré son paquet avant de clore, et
la dette est soldée avant que le conteneur meure. **Un fil Cowork qui écrit une
pièce d'appareil livre son paquet de versement avant de clore, ou il a écrit pour
rien.**

**Reste ouvert, et rien de cela n'est de ce fil** : les 43 corrections non portées et les 3 portées
de travers du relevé EP3, qui sont des arbitrages de l'auteur ; la réécriture des
quatre modules perdus ; et le bout en bout de la machine, qui reste l'objet du
fil courant.

## 20260910 — La troisième épreuve est relevée contre la seconde relue, et la phrase du bon à tirer ne s'écrit pas

**Fil de production, ouvert et clos le 20260910.** Il n'a rien corrigé, rien
réécrit, et n'a tranché aucun écart de fond. Il n'a touché ni doctrine, ni
chiffrage, ni skill.

**Ce qui change au corpus.** Le corpus porte un second relevé d'épreuve, et il
ne mesure pas la même chose que le premier. Celui du 20260908 comparait une
épreuve au manuscrit et disait *ce qui diffère*. Celui-ci compare une épreuve à
l'épreuve précédente **relue** et dit *ce qui a été fait de la demande*. Sa
référence n'est pas le manuscrit mais **la demande écrite de l'auteur** — les
261 surlignages annotés de la seconde épreuve, établis par inspection de ce qui
était joint et non demandés. Le manuscrit reste le troisième terme : il sert à
dire de quel côté un écart non demandé déplace le texte.

**Le compte.** Sur 261 corrections demandées : **215 portées, 3 portées de
travers, 43 non portées**. Et **12 écarts sans demande écrite**. Le relevé
donne sa preuve à chaque verdict, et il distingue les quatre : 132 corrections
sont attestées par le texte demandé, 46 par la disparition de ce qui devait
sauter, 37 seulement par un mouvement à l'endroit visé.

**Ce que le relevé refuse d'écrire.** *« La troisième épreuve porte les
corrections demandées et n'en porte pas d'autres »* ne s'écrit pas. Les non
portées font deux blocs homogènes — les dix-sept demandes de coupe de
paragraphe, toutes, et vingt virgules à retirer dont seize sous la même
question. Deux consignes entières ne sont pas arrivées jusqu'à la composition.

**Ce qu'il permet d'écrire.** La composition ne réécrit plus : 572 écarts
étaient apparus hors du manuscrit entre la première et la deuxième épreuve, il
y en a 12 entre la deuxième et la troisième, dont trois seulement touchent la
rédaction ou un renvoi.

**Les trois points dus au bon à tirer sont soldés.** La page 105 n'est pas
réparée, et le contrôle arithmétique la relève seul — l'écart vaut toujours
550 euros par mois et par retraité, et aucune correction n'avait été demandée à
cet endroit. Les deux césures sont tranchées : « sous-directeur » porte son
trait d'union, « Cross-Sectional » aussi. La page 142 est réparée, et comme
l'auteur l'a demandée.

**Ce qui reste ouvert.** Les 43 corrections non portées, les 3 portées de
travers et les 12 écarts non demandés sont des arbitrages, et ils reviennent à
l'auteur. Deux d'entre eux introduisent une faute que l'épreuve relue n'avait
pas : « resterons » pour « resteront » p. 86, et « à la seconde moitié
économies » p. 90, où le « des » demandé manque.

**Ce qui est dû au dépôt.** Six pièces — quatre modules neufs de la relecture
d'épreuve contre épreuve, et les deux générateurs qui les déclarent. Un fil
Cowork ne pousse pas ; `coffre.py dette` les réclame en `D1` et `D2`, et
`make restauration` les compte en `R6`, qui ne bloque pas.

**Ce qui n'a pas pu se jouer.** `make controle` ne tourne pas entier : ce fil
n'a délibérément déplié ni la doctrine, ni les positions, ni les référentiels
de chiffres, et deux contrôles s'arrêtent faute de leur entrée. Ce n'est pas
une anomalie du corpus, c'est le périmètre du fil.

## 20260910 — L'appareil est entier au dépôt, la jauge se rouvre de 367 490 jetons

**Suite du fil de production sur l'appareil, sur le push des douze pièces.** Il
n'a touché ni doctrine, ni skill, ni livrable.

**Clôture, après le second push.** Les quatre pièces corrigées le matin sont au
dépôt — commit `167c53e`, fusion `9bf67442`, diff hors `chantier/` vide.
`coffre.py dette` sort **`D1`, `D2` et `D3` à zéro**, 84 pièces identiques au
clone : *rien n'est dû au dépôt*. `make restauration` sort **`R1` à `R6` à
zéro**, et la restauration à blanc finale sur le clone seul aussi — 162 attendus,
162 présents, verbatim du manuscrit prouvé à l'octet. **`R6` à zéro est le
chiffre neuf** : plus aucune pièce d'appareil ne vit dans le seul conteneur.

*Ce que le cycle a coûté* : **deux allers-retours Cowork ↔ claude.ai/code** pour
une correction d'appareil, le second portant ce que le premier a rendu
nécessaire. C'est le prix d'A-394 et il est structurel — d'où la règle : un fil
d'appareil se pense en un seul aller-retour.

**Le push est contrôlé sur pièce, non hérité du récit.** Commit `6cc1b99`,
fusionné dans `main` au commit `31896bb5`. Le clone frais dit les trois choses
qui comptent : `HEAD` est bien `31896bb5`, **le diff hors `chantier/` est vide**
— aucun fichier du dépôt de droit n'a bougé —, et douze chemins touchés sous
`chantier/`, huit modifiés et quatre créés, zéro supprimé. `coffre.py dette`
sort **`D1` et `D2` à zéro**, 80 pièces identiques au clone.

**Les quatre pièces quittent le coffre, prouvées d'abord.** Comparées au clone
**et** à leur empreinte avant tout retrait : quatre identiques sur quatre. Puis
`COFFRE_DOCUMENT` vidée, index rejoué — **84 artefacts de voie `depot` au lieu
de 80** —, et les quatre documents supprimés. Ordre d'A-357 tenu de bout en
bout.

**Jauge relevée à `project_info`, avant et après, dans son unité** : de
**1 390 673 à 1 023 183** sur 2 000 000. **367 490 jetons rendus**, marge portée
de 609 327 à **976 817**. Le coffre passe de 87 à **83 documents**. Deuxième plus
grosse libération du corpus, après les 623 934 de la veille.

**Une correction de fond est sortie en jouant la procédure, et c'est la plus
importante du jour.** `empreintes.py` relevait toute empreinte au dépôt courant.
Un fil Cowork qui corrige une pièce de l'appareil ne peut pas la pousser :
relever son empreinte ici écrivait au coffre **la référence d'un fichier qui ne
vit que dans un conteneur éphémère**, et la session suivante sortait un `R1` qui
n'était pas un faux. **C'est A-392 par l'autre bout.** La règle est désormais
générale — *une empreinte ne décrit jamais un état qu'aucune surface permanente
ne porte* — et pour la voie `depot` le relevé se fait **au clone**. Sans clone,
elle ne se touche pas.

**Un verdict naît, `R6`.** Une pièce de voie `depot` qui diverge de son empreinte
**et du clone** a été corrigée ici et non poussée : ce n'est pas un faux, et la
compter en `R1` faisait échouer `make restauration` à tout fil qui corrige
l'appareil. Elle sort de `R1`, non bloquante, avec renvoi à `coffre.py dette`.
**Celle qui diverge de l'empreinte et concorde avec le clone reste en `R1`** :
là, c'est le dépôt qui est en retard. Sans clone, tout reste en `R1`, ce qui est
le comportement prudent.

**La restauration à blanc passe sur le clone seul, sans aucune pièce portée à la
main.** C'est le test que la veille ne pouvait pas faire, faute du push :
**162 artefacts attendus — 78 par le coffre, 84 par le dépôt —, 162 présents,
`R1` à `R5` à zéro.** Les deux gros référentiels ne demandent plus de `cp` : ils
viennent du clone, et **la voie 1 n'est plus sur le chemin critique de
l'ouverture**. La preuve externe du verbatim tient — `extraire_notes.py` rejoué
sur le manuscrit restauré redonne le référentiel des notes à l'octet,
`a6a07a73…` — et `make index` sort à zéro anomalie dans ce dépôt vierge.

*Un `R1` s'est présenté au premier essai et il n'était pas un faux* : trois
documents de `methode/` sortaient à leur version d'avant le versement du jour.
**A-313 mot pour mot** — le transcript porte l'état d'avant, et il faut relire le
coffre après avoir versé. Relus par un fil auxiliaire, les trois concordent.

**`make controle` sort à zéro échec**, code de retour nul. **`make generateurs`**
sort à zéro échec bloquant, 23 générateurs en attente d'une pièce jointe.
*Relevé au passage* : `V5` a donné **6 au premier passage et 0 au second**, sur
les mêmes entrées, quand `V2` avait fait l'inverse la veille. Les deux verdicts
ne se mesurent pas sur le même dépôt — `V2` sur un dépôt vierge, `V5` sur un
dépôt déjà régénéré —, et un balayage joué une seule fois ne peut pas dire les
deux.

**Versé** : `methode/index.json` (220 artefacts, 84 de voie `depot`),
`methode/empreintes.json` (161 empreintes, la voie `depot` relevée au clone),
`methode/arbitrages.md`, ce journal, et le prompt du fil suivant. **Supprimé du
coffre** : les quatre pièces devenues des pièces du dépôt. L'insertion au
registre se prouve de l'extérieur : privé de son bloc neuf, il redonne l'état
d'avant à l'octet.

**Reste ouvert, et rien de cela n'est de ce fil** : quatre pièces d'appareil
corrigées aujourd'hui et non poussées — `generer_index.py`, `empreintes.py`,
`controle_restauration.py`, le `Makefile` —, qui sont le régime permanent
d'A-394 et que `R6` compte sans bloquer ; quatre documents au coffre non déclarés
à l'index, venus d'un fil de la règle d'or le 20260908, dont un sas ; la rotation
des fichiers qui croissent, sans voie vers le dépôt ; et le bout en bout de la
machine, qui est l'objet du fil suivant.

## 20260909 — L'appareil sait qu'il est au dépôt, et la restauration à blanc le prouve

**Fil de production sur l'appareil, ouvert et clos le 20260909, sur A-396 et rien
d'autre.** Il n'a touché ni doctrine, ni skill, ni livrable, et n'a rien poussé
au dépôt. Il a déplié l'index, le prompt de fil, le registre, puis cloné le
dépôt.

**La dette était réelle et elle se mesure en acte.** Dans un répertoire vierge,
le clone tel que le dépôt le porte aujourd'hui **ne permet pas d'ouvrir** :
`coffre.py deplier coffre/coffre.txt` lève, l'archive n'existant plus, et rien
d'autre ne sait par où prendre les quatre-vingts artefacts. C'est exactement ce
qu'A-396 annonçait la veille.

**La voie de restauration devient un champ de l'index.** Le rang ne dit plus où
une pièce vit — le même rang couvre le dépôt, le coffre et rien. `voie` prend
quatre valeurs, `depot` · `coffre` · `piece_jointe` · `hors_coffre`, et
`chemin_coffre` donne où la pièce se lit **sur sa voie** : au coffre, préfixée de
racine, ou dans le dépôt sous `chantier/`. Le bloc `archives` disparaît avec
l'archive ; le bloc **`depot`** le remplace et porte le nom du dépôt, la branche,
la sous-racine, **la commande de clone en clair**, les quatre-vingts chemins, et
ceux des pièces de l'appareil encore au coffre. **220 artefacts, 163 durables
dont 80 rendus par le dépôt.**

**`coffre.py` ne plie plus, et `plier` est retiré plutôt que gardé** : un outil
qui produit une pièce que personne ne verse est un piège, et un fil l'aurait joué
en croyant verser. `deplier` reste, seul lecteur du format, pour une archive qui
resurgirait. Un mode naît, **`dette`**, qui compare l'appareil au clone octet par
octet et sort trois verdicts. Il ne pousse rien : l'écriture au dépôt est fermée
depuis Cowork. **`make coffre` relève les empreintes, puis dit ce qui est dû.**

**`restaurer.py` rend la main sur la voie `depot`** — il ne cherche plus au
transcript ce que le clone rend déjà, il compte les quatre-vingts à part, et
**imprime la commande de clone** quand il en manque. Il refuse un index d'avant,
qui décrit une archive disparue. Et il gagne une **amorce** : l'index est
lui-même un document du coffre, donc un dépôt vierge n'avait rien pour savoir
quoi restaurer — le dépliage de l'archive masquait ce trou depuis le début.

**Un `R1` se lit désormais avec sa voie.** Sur le coffre, c'est un faux, il se
redemande. Sur le dépôt, l'octet vient d'un clone : ce qui diverge est le clone
contre l'empreinte, donc le dépôt est en retard, ou une empreinte a été versée
sans pousser. Le verdict reste bloquant, et il dit où chercher.

**La procédure d'ouverture est réécrite** à `methode/localisation.md` et à
`CLAUDE.md` : lire les trois documents, amorcer l'index, **cloner le dépôt**,
restaurer les documents du coffre, `make restauration`. Les trois voies de la
restauration deviennent `cp` du fichier local, `git clone`, et le transcript.
`technique/` ne figure plus au rangement du coffre.

**La restauration à blanc passe, et c'est le seul test qui vaille.** Dans un
répertoire vierge et hors du dépôt, clone plus les huit pièces dues portées à la
main comme le push le fera : **162 artefacts attendus — 82 par le coffre, 80 par
le dépôt —, 162 présents, `R1` à `R5` à zéro.** `R2` à zéro est le chiffre qui
compte : aucune pièce du corpus ne tombe entre les deux surfaces. **La preuve
externe du verbatim tient** — `extraire_notes.py` rejoué sur le manuscrit
restauré redonne le référentiel des notes identique à l'octet, `a6a07a73…` — et
`make index` sort à zéro anomalie dans ce dépôt vierge.

**Deux défauts de plus sortent des contrôles, et ils ne sont pas de ce fil par
nature.** `I2` sortait à **29 297** parce que la racine du dépôt de cette session
est le répertoire personnel du conteneur : 29 295 caches d'outils, et deux
fichiers du corpus invisibles dedans. C'est A-337 à l'identique, et les
répertoires du conteneur rejoignent les ignorés — `I2` retombe à zéro, le compte
du dépôt passe à 162. Et `make generateurs` sort **`V2`** : la cible du site ne
nommait qu'une de ses deux sorties déclarées, donc `site/manifeste.html` ne se
rejouait jamais par `make`. C'est le défaut qu'A-385 a relevé six fois et manqué
là. Corrigé, le balayage sort à **zéro échec bloquant, 23 générateurs en attente
d'une pièce jointe**.

**`make controle` sort à zéro échec**, code de retour nul, sur tous les contrôles
joués : lexique **27 livrables lus, 4 alertes** — les trois emplois de fond
qu'A-390 renvoie à l'auteur —, structurel zéro échec, arithmétique 23 écarts
consignés, chiffres 93 entrées à sourcer et 22 signalements, hypothèses zéro
échec, apports 20 signalements, `G` 13 skills diffusables et 5 signalements. Les
contrôles de socle se déclarent non joués, faute de pièce jointe. `I1` sort à
23 : les dérivés que ce fil n'a pas régénérés, et A-338 pose que ce n'est pas un
invariant.

**Douze pièces sont dues au dépôt et se déclarent faute de pouvoir se pousser** :
les huit modules corrigés ici, et quatre pièces de l'appareil encore versées au
coffre comme documents — les deux référentiels de rédaction, 848 ko et 352 ko, et
les deux modules de la réapplication. **Les y porter rendrait de l'ordre de
360 000 jetons de jauge**, et le motif qui les gardait au coffre est caduc : il
n'y a plus d'archive à réécrire.

**Un trou de l'appareil est nommé et non comblé** : les deux gros référentiels ne
reviennent pas du transcript, le coffre les rendant comme fichiers. Ils se
restaurent par `cp`, prouvés identiques à l'octet, et le module les compte en
absents plutôt que de les taire. A-313 réservait la reprise au jour où un
deuxième document franchirait le seuil ; ils sont deux, et une pièce d'appareil de
plus qu'on ne peut pas pousser n'aide personne.

**Versé** : `methode/index.json` (220 artefacts, bloc `depot`),
`methode/empreintes.json` (161 empreintes, celle de l'archive retirée comme
périmée), `methode/localisation.md`, `CLAUDE.md`, `methode/arbitrages.md`,
ce journal, et le prompt du fil suivant. Les deux insertions se prouvent de
l'extérieur : registre et journal privés de leur bloc neuf redonnent l'état
d'avant à l'octet.

**Les douze pièces sont livrées en un paquet prouvé**, sur go de l'auteur, et
c'est la seule voie qu'A-394 laisse : aucune surface ne voit les deux bouts.
`versement_depot_chantier_20260909.zip`, 259 933 o, les douze rangées sous
`chantier/` avec un manifeste d'empreintes. **Les douze concordent avec le
registre des empreintes, et le dézippage est identique à l'octet au dépôt
courant, 12 sur 12.** Le push lui-même se fait d'une session claude.ai/code, et
`coffre.py dette` le contrôlera à zéro.

**Reste ouvert, et rien de cela n'est de ce fil** : le push lui-même, sans lequel
un fil qui clone demain reçoit l'appareil d'avant ; quatre documents au
coffre non déclarés à l'index, venus d'un fil de la règle d'or le 20260908, dont
un sas — ce fil ne les ouvre pas, A-24 l'interdit ; la rotation des fichiers qui
croissent ; et le bout en bout de la machine, qui est l'objet du fil suivant.

## 20260909 — L'appareil quitte le coffre pour le dépôt, et la jauge se rouvre

**Fil de conversation, sur la passation du nettoyage écrite la veille.** Il n'a
déplié aucune source, joué aucun `make`, corrigé aucune skill. Il a mesuré,
transféré et prouvé.

**Le coffre était à 2 735 jetons de sa borne** — 1 997 265 sur 2 000 000, plus
serré encore que les 4 884 du relevé de la veille. Rien ne pouvait plus être
versé, l'arbitrage du relevé compris.

**Le verrou n'était pas celui que la passation nommait.** Elle écrivait que
l'atelier n'avait aucun outil GitHub authentifié. Il en a un, qui s'authentifie
comme le propriétaire du dépôt. Ce qui refuse est **le proxy de la session**, qui
n'injecte de credential que pour les dépôts déclarés comme sources de la session :
`git ls-remote` anonyme passe, `git push` et l'API sortent en refus nommé. Et la
synchronisation GitHub d'un projet Claude est **en lecture seule par conception** —
elle ne servira jamais à écrire, quel que soit son filtre.

**Aucune surface ne voit les deux bouts, et c'est la contrainte permanente.** Une
session Cowork voit le coffre et ne pousse pas ; une session claude.ai/code pousse
et ne voit pas le coffre. Le transfert passe donc par un fichier livré à l'auteur,
qui le dépose dans le fil qui écrit. Acceptable pour l'appareil, qui bouge
rarement ; **pas une voie de rotation** pour les fichiers qui grossissent à chaque
session.

**L'appareil est au dépôt et la preuve est faite deux fois.** L'archive a été
rendue comme fichier — copie d'octets, jamais le modèle — puis dépliée par
`appareil/coffre.py` extrait de l'archive elle-même, 80 blocs. Versée par un fil
claude.ai/code sous `chantier/`, branche `appareil`, commit `6752e77`, fusionnée
dans `main` au commit `eb0e0981…`. Comparaison fichier par fichier contre la
branche **puis** contre `main` : **80 identiques, 0 divergent, 0 absent**, et le
diff hors `chantier/` est vide.

**Le fil qui a versé a arbitré une chose que sa consigne ne prévoyait pas, et il
a eu raison contre elle.** Le `.gitignore` du corpus ignore `droit/`, `eval/`,
`publication/`, `machine/`, `coffre/` ; posé à la racine du dépôt de droit il en
aurait masqué le contenu, et le fusionner l'aurait fait en silence. D'où le
sous-répertoire, avec son `.gitignore` local : **deux corpus dans un dépôt, deux
racines distinctes.** La consigne « à la racine » venait de ce fil et elle était
fausse.

**`technique/coffre.txt` est supprimé du coffre après la preuve, dans l'ordre
d'A-357.** La jauge passe de **1 997 265 à 1 373 331** : **623 934 jetons rendus**,
marge portée de 2 735 à **626 669**. Plus grosse libération du corpus à ce jour, et
aucun contenu perdu.

**Ce que le transfert crée comme dette, et elle est nommée.** Quatre-vingts
artefacts portent `chemin_coffre: technique/coffre.txt`, un chemin qui n'existe
plus. Leur voie de restauration est désormais le clone du dépôt — copie d'octets,
donc conforme —, mais **l'appareil ne le sait pas** : l'index, `coffre.py`,
`restaurer.py` et la procédure d'ouverture décrivent encore une archive au coffre.
Un fil qui ouvrirait demain trouverait quatre-vingts artefacts manquants sans
savoir où les prendre. Rien de cela n'est de ce fil, qui ne déplie rien.

*Et une pièce du relevé de la veille tombe d'elle-même* :
`referentiels/notes_manuscrit.json`, seul candidat prouvé, n'était pas un document
du coffre mais un fichier plié dans l'archive. Il est parti avec elle, et le
retrait qu'A-346 réservait à l'auteur est sans objet.

**Reste ouvert, et rien de cela n'est de ce fil** : la dette d'appareil ci-dessus ;
la rotation des fichiers qui croissent, qui se fait entièrement au coffre ; la
scission thématique des projets, que l'auteur n'a pas tranchée ; et le kit CSS,
non mesuré.

## 20260908 — Le coffre allégé de quatre dérivés, l'appareil du relevé retrouvé

**Fil de nettoyage, ouvert sur une jauge à 1 027 jetons de sa borne.** Il ne
produit rien : il retire ce qui se refait, verse ce qui ne se refaisait pas, et
met les grilles d'accord avec l'état réel du coffre.

**Quatre dérivés graphiques sortent du coffre, chacun sur un rejeu prouvé à
l'octet** — `galerie_fiches.html` (`30e64637…`), `carte_du_projet.html`
(`bd2280f2…`), `etat_machine.html` (`e595ed53…`), et
`extrait_gagnants_perdants.html` (`7a9994e3…`, identique à date égale : la page
horodate son propre pied, et privée de son horodatage elle rend exactement
l'empreinte versée). **`etat_vecteurs.html` reste** : il descend du socle
budgétaire, donc des cinq classeurs, qui sont des pièces jointes — A-342 ne lit
« régénérable » que depuis le coffre seul.

**Le dépôt était d'une version en retard, et c'est ce qui a failli faire conclure
à des générateurs cassés.** Archive à 1 685 571 o contre 1 721 690 au coffre,
index à 87 637 o contre 89 851. La carte rejouée sortait 626 octets de moins et
`etat_machine.py` levait un `KeyError` : deux faux, l'un et l'autre disparus une
fois l'archive et l'index redéployés par copie d'octets. **Une divergence de
rejeu se lit d'abord contre l'état du dépôt.**

**L'appareil du relevé d'épreuve est retrouvé au transcript et versé.** Déclaré
comme un manque la veille, puis recouvert au dépôt par le redéploiement de
l'archive, `relever_ecarts_epreuve.py` et `rendre_releve_epreuve.py` ont été
reconstitués par **rejeu de leurs écritures** — dernier `Write`, puis les
quatorze `Edit` qui le suivent, chacun exigé unique, **zéro échec**. Preuve
externe : rejoués sur les mêmes entrées ils rendent `releve_bat.tsv`,
`releve_bat.md` et le contrôle des chiffres **identiques à l'octet**. Le
transcript ne porte pas que les lectures du coffre ; il porte aussi ce que la
session a écrit.

**Le contrôle des chiffres est corrigé dans le module, pas seulement dans le
document.** Les deux identités inventées que l'auteur avait relevées la veille
sont retirées ou reposées sur la fenêtre que le texte donne, et le contrôle lit
désormais **le référent du nombre** des deux côtés : quand la p. 105 cesse de
nommer la pension de base, 1 100 devient le socle seul, la note 124 en fait
1 650, et le contrôle sort faux de 550 euros par mois. Il passe de « 5 justes,
2 faux » — deux faux imaginaires, la vraie casse invisible — à **« 5 justes,
1 faux »**, celui de la p. 105. Le relevé détaillé ne bouge pas : 858 écarts,
134 comptés en forme.

**Deux documents étaient au coffre sans être à l'index** — le relevé d'écarts et
son compte, versés la veille. Un document que nulle grille ne déclare est un
document que nul rejeu ne refait : c'est A-364, survenu dans le fil qui l'a
écrit. Les deux sont portés à la table, en `derive`, `coffre: true`, classés en
`grilles`.

**Versé** : `technique/coffre.txt` (1 766 639 o, 80 fichiers, dépliage vérifié
80 sur 80 identiques), `methode/index.json` (220 artefacts, 163 au coffre),
`methode/empreintes.json` (157 empreintes, 4 périmées retirées),
`methode/arbitrages.md` et `methode/journal.md`. **Retiré** : les quatre
dérivés. Chaque remplacement s'est fait retrait d'abord, écriture ensuite —
A-357.

**Reste ouvert, et rien de cela n'est de ce fil** : les 297 écarts de fond du bon
à tirer, qui sont des arbitrages de l'auteur ; les deux césures des p. 40 et 147,
à vérifier à l'œil sur l'épreuve ; le générateur de l'extrait, qui horodate sa
propre sortie et rend donc un dérivé non reproductible d'un jour à l'autre ; les
trois lignes de contrôle que `releve_epreuve_EP2.md` porte et que le module ne
pose pas, calculées à la main lors de la reprise.

## 20260908 — Les épreuves relues contre le manuscrit, et la refonte se voit

**Fil long de relecture comparée.** Il n'a rien corrigé, rien réécrit, et n'a
tranché aucun écart de fond. Il rend un relevé et le contrôle des chiffres qui
s'y lisent.

**Le manuscrit est prouvé deux fois avant tout emploi.** Restauré du coffre par
copie d'octets depuis le transcript, il redonne son empreinte à l'octet —
`5ec342cb…`, 224 422 o, 868 lignes — et la preuve externe tient :
`extraire_notes.py` rejoué dessus rend `referentiels/notes_manuscrit.json`
identique, `a6a07a73…`. **Un seul `R1` à l'ouverture, sur `methode/index.json`**,
et ce n'est pas un faux : le coffre en porte dix-neuf lignes de plus que
l'empreinte relevée le 20260907 à 10 h 42, un versement d'index ayant suivi le
dernier `make coffre`. Le journal, redemandé plus tard, montre le même retard —
185 545 o au coffre contre 172 491 à l'empreinte.

**La seconde épreuve n'est pas une correction de la première, c'est une
refonte.** Contre le manuscrit, la première épreuve du 31 juillet ne diverge que
par **374 écarts** ; celle du 4 septembre en porte **858**, dont **572 sont
apparus entre les deux**. La réécriture est venue de la composition, pas du
manuscrit.

**Le compte, par classe** : 297 de fond, 171 de perte, 390 de coquille, 134
comptés en forme. Le fond se répartit en 47 écarts de chiffre, 70 de nom propre
et 180 de rédaction ; la perte, en 161 passages de texte, 5 notes ajoutées et 5
notes retirées.

**Un seul chiffre du corpus diffère entre le manuscrit et l'épreuve**, et il se
contredit sur sa propre page. Page 142, « la moitié des économies sera déjà
réalisée et restituée » devient « 236 milliards d'euros d'économie seront déjà
réalisées et restituées », deux paragraphes avant « la seconde moitié des
économies ». Les vingt autres grandeurs relevées — 236 Md€, 600 €, +13 %, 550 €,
275 €, 6 600 €, 1 100 €, 23 %, 77 centimes, 20 000 €, 600 Md€, 4 500 Md€, 36 %,
580 000 postes — sont identiques des deux côtés.

**Le contrôle arithmétique se joue sur les valeurs relevées, et sa première
version était fausse deux fois — relevé par l'auteur, repris le jour même.** Elle
posait deux identités qui n'existent pas au corpus : que le compte éducation
vaudrait douze fois l'aide de l'enfant, quand l'épreuve écrit « **en plus de**
l'aide fondamentale de 275 euros, 6 600 euros par an » et que le `550 × 12` du
corpus se rapporte à l'aide de l'adulte ; et que la montée de +2 % par mois
courrait sur douze mois, quand l'épreuve pose une **latence de six mois** avant
qu'elle commence — six à sept mois à deux points encadrent les 13 % annoncés.
**Les deux comptes tombent.** Huit contrôles sont justes après reprise.

**Le seul endroit où l'arithmétique bloque est p. 105, et le contrôle ne le
voyait pas.** Le manuscrit écrit « un socle contributif par répartition **avec
une pension de base** égale à 1 100 euros » ; l'épreuve retire le membre de
phrase, et 1 100 cesse d'être la pension de base pour devenir le socle seul. **La
note 124 de l'épreuve est inchangée** et pose que « le socle contributif forme
avec l'aide fondamentale une pension de retraite de base » : le corps et sa
propre note ne disent plus la même chose, et l'écart vaut **550 euros par mois et
par retraité**. L'accord au féminin — « un socle contributif … égale » — est la
trace de la coupe. *Leçon portée au registre : un chiffre inchangé dont la
définition bouge est un écart de chiffre, et un contrôle qui compare des valeurs
sans comparer leurs référents ne le voit pas.* `make controle` du corpus passe
par ailleurs à zéro échec sur ses 23 consignes.

**Les notes ne s'apparient pas par numéro, et personne ne pouvait le voir à
l'œil.** 141 des deux côtés, mais deux notes entrent, deux sortent, six changent
de rang, et **78 sont renumérotées** à partir de la quarantième. L'appariement
se fait par alignement global des textes ; un relevé fait sur les numéros aurait
déclaré faux tout le cahier de notes à partir de la page 149.

**Trois passages entiers ont changé de place** — les 521 pages du code de la
route, de la partie I chapitre 4 à la partie II chapitre 5 ; le palais d'Iéna ;
les 77 centimes nets. **Quatre phrases entrent que le manuscrit ne porte pas**,
dont la réduction du gouvernement à 7 ministères « au lieu des 35 ministres que
compte l'actuel », et deux emplois de « pourcents ». **Les taxis de 2025 sortent**
de la liste des mouvements sociaux.

**Deux écarts se déclarent non décidables sur le texte extrait** — une césure de
composition que l'extraction recolle sans son tiret, p. 40 et p. 147. Ils se
vérifient à l'œil sur l'épreuve, et nulle part ailleurs.

**Versé, et cela seul** : `livrables/releve_epreuve_EP2.tsv`, un écart par ligne,
et `livrables/releve_epreuve_EP2.md`, le compte et le contrôle. Les épreuves
elles-mêmes ne se versent pas : binaires, et la jauge ne les porterait pas.

**Reste ouvert, et rien de cela n'est de ce fil** : les 297 écarts de fond, qui
sont des arbitrages de l'auteur ; les deux comptes faux du corpus, qui ne
relèvent pas du bon à tirer mais du chiffrage ; l'empreinte de l'index et celle
du journal, à relever au prochain `make coffre` ; et l'appareil du relevé —
`relever_ecarts_epreuve.py` et `rendre_releve_epreuve.py` — qui n'est pas versé
à l'archive technique, ce fil ne l'ayant pas dépliée.

## 20260907 — Le corpus contrôle enfin qu'il sait encore se refaire

**Fil de maintenance.** Il n'a produit aucun livrable de fond et n'a tranché
aucune question de doctrine. Il a réparé, déclaré et versé.

**Le balayage des générateurs existe** — `make generateurs`, cinq verdicts, dont
trois bloquent. A-364 avait nommé le trou le 20260904 sans le fermer : *rien ne
contrôle qu'un générateur du coffre tourne encore*. Il joue chaque producteur
que l'index déclare, **par la règle du fichier de construction et jamais à la
main**, et compte ceux qui ne tournent plus. Il n'entre pas dans `make controle` :
il écrit au dépôt, et `controle` ne produit rien.

**Il a mordu trois fois au premier passage.** Une variable du fichier de
construction désignait deux artefacts différents selon l'endroit où on la lisait,
et le premier déplacement de ligne aurait tué une règle sans bruit. Six sorties
n'étaient nommées par aucune cible, donc ne se rejouaient jamais par `make`. Et
`make tout` s'arrêtait sur le premier consommateur du socle budgétaire, qui vient
de pièces jointes absentes de l'atelier — il ne refaisait donc rien de ce qui
vient après. Après correction : **zéro échec bloquant**, vingt-six générateurs en
attente d'une pièce jointe, nommée pour chacun.

**La cause commune de deux incidents est trouvée, et elle tenait en une règle
absente.** L'index est un dérivé, et aucune règle ne le rejouait. Un fil qui
versait une pièce, l'écrivait à l'index et oubliait la table curée passait
inaperçu — jusqu'au rejeu suivant, qui la dé-déclarait en silence. C'est ce
qu'A-364 puis A-381 ont constaté à deux jours d'écart. `make reindex` existe.

**Deux pièces du second banc étaient au coffre et invisibles à l'index** — le
banc des liasses déposées et le prompt de son fil joueur, versés la veille. La
faute d'A-381 s'est répétée dans le fil qui l'écrivait. Portées, `I6` à zéro.

**Trois dérivés du coffre étaient en retard.** La carte du projet, la galerie des
fiches et l'extrait gagnants-perdants ont bougé au rejeu. Sur l'extrait, le
coffre, l'empreinte et le rejeu donnent **trois tailles différentes** : un fil
l'a régénéré, a relevé son empreinte, et ne l'a pas reversé. Les trois sont
reversés.

**Deux contrôles disaient faux, chacun dans un sens.** `controle_index` comptait
`I1` parmi les échecs alors qu'A-338 pose depuis cinq jours que ce n'est pas un
invariant : tout fil qui ne déplie qu'une partie du coffre sortait en erreur, et
les fils écrivaient « zéro échec » en lisant les compteurs plutôt que le code de
retour. Et `controle_lexique`, éprouvé pour la première fois sur des livrables
régénérés, sortait douze anomalies sur trente-sept — parce qu'il balayait les
vues internes et les relevés de notes, qui ne sont pas des livrables diffusables
et ne se réécrivent pas. Le périmètre se lit désormais à la carte.

**Ce que le lexique laisse après bornage est de fond, et cela remonte** : trois
emplois dans quatre livrables, dont « l'instruction gratuite des jeunes
Français » au manifeste, qui est un emploi affirmatif d'un mot que la doctrine
n'admet qu'à charge.

**La stratégie réseaux est sortie du projet**, et A-366 affirmait la veille
qu'elle y était encore. Sa part digérée tient ; l'architecture des comptes, le
plan de lancement, les cinq postures et les scripts sortent avec elle et ne sont
digérés nulle part. Déclarée aux manquants, qui passent à dix.

**Le prompt de fil courant est réécrit sur l'état réel.** Il portait la
correction de `disposition-cible` depuis le 20260904 et deux fils l'avaient
laissé en place pour ne pas l'écraser. Le fil suivant transfère la machine à son
projet dédié, puis joue le bout en bout.

**La restauration.** Périmètre déplié : l'archive technique — 77 fichiers —, les
documents lisibles par copie d'octets, les deux référentiels de rédaction rendus
comme fichiers. **Cinq `R1` à l'ouverture, aucun n'était un faux** : deux
lectures indépendantes du coffre rendent les mêmes octets sur les quatre
documents concernés, et le relevé ne voit qu'une seule version distincte de
chacun. Ce sont les empreintes qui retardaient, faute d'un `make coffre` depuis
plusieurs versements. **La preuve externe du verbatim tient** :
`extraire_notes.py` rejoué sur le manuscrit redonne le référentiel des notes
identique à l'octet, `a6a07a73…`.

**Ce que ce fil n'a pas fait, et pourquoi.** Il n'a pas réécrit les deux modules
manquants : la réécriture d'`articles_ouverts_plf.py` était sûre parce que sa
sortie était versée et valait spécification exécutable, et cette asymétrie
n'existe pour aucun des deux. Il n'a pas transféré le banc au projet machine —
une session ne voit qu'un projet, et le transfert passe par pièces jointes. Il
n'a pas repris la présentation des sept compétences internes : le point de vérité
d'une skill est la skill enregistrée.

## 20260907 — Le second banc est construit, et l'appareil qui le mesure sortait faux

**Le banc des liasses déposées existe** — `methode/banc_gl.md`, 42 couples pour 37
numéros, deux véhicules, trois liasses entrées par pièce jointe. C'est le premier
banc du corpus dont la vérité-terrain n'est pas la nôtre. Sa clé ne se verse pas :
elle est la vérité-terrain, et elle se régénère des pièces jointes en une
commande. Le prompt du fil qui le jouera est écrit et ne porte aucune réponse.

**La clé était fausse sur neuf couples des quarante-deux**, dont huit des
vingt-quatre couples de norme du lot de finances. Un contrôle neuf l'a dit — `K1`
à `K6`, joué à `make controle` —, pas une relecture. L'extracteur ne relevait que
le premier fragment d'une énumération d'articles, et coupait tout suffixe en
lettre qu'il n'avait pas prévu. La grammaire n'a pas été réécrite : les deux que
le corpus porte déjà sont désormais appelées.

**Trois défauts de l'appareil de mesure sortent du même geste.** La population
d'un lot était filtrée sur la nature du couple et non sur son véhicule. La borne
basse d'une fourchette ne s'appariait pas, alors que le module l'annonçait dans
son propre docstring. Et le contrôle neuf lui-même cherchait trop étroit : il
avait laissé passer, dans la première rédaction du banc, une énumération de la
clé citée en verbatim.

**Un taux publié est démenti.** « Aucune adresse n'a envoyé l'amendement au
mauvais endroit » était un effet de la clé fausse. Sur clé corrigée, un cas sort
en discordance. Les taux ont été relus sans rejouer la skill : au lot de
finances, 90,9 % de concordance contre 63,6 %, une discordance contre zéro, et
une précision de 64,3 % qui n'avait jamais été publiée. Au lot de financement, le
rappel ne bouge pas et la précision est de 46,2 %.

**L'écart de compte des liasses est fermé, par explication et non par
comblement** : sur 39 amendements annoncés, 38 en-têtes sont aux pièces et 37
numéros portent un couple — un numéro absent des trois pièces, un numéro sans
exposé sommaire.

**Ce que le banc dit de la machine, et c'est sa sortie la plus utile** : seize
couples sur quarante-deux ne peuvent être pris par aucune étape outillée, et deux
étapes manquent sur tout le banc — le rattachement, non outillé, et la liasse,
qui n'existe pas.

**Jauge, relevée à `project_info` dans son unité, avant et après.** De
**1 908 374 à 1 935 724** sur 2 000 000 : la marge passe de 91 626 à **64 276**.
**27 350 jetons consommés** pour un demi-mégaoctet de pièces versées — l'archive
technique en entier, le registre, le journal, l'index, les empreintes et les deux
pièces neuves du banc. Le rapport ne tient qu'à l'ordre des gestes : chaque
remplacement a été **supprimé avant d'être versé**, sans quoi rien de tout cela
ne rentrait.

**Reste ouvert.** Le banc est une pièce de la machine, donc dû au déménagement
décidé le même jour ; son inventaire de transfert est au registre. Le référentiel
de doctrine a été écrasé au dépôt par un générateur joué à la main, puis repris
de l'archive et prouvé identique à son empreinte. Un second fil versait au coffre
pendant celui-ci, et rien n'outille ce cas.

## 20260907 — La valise entre au contrat, et l'à-blanc cesse d'être un mode dégradé

**`A-376` corrige une lecture trop courte.** L'exclusion posée par `A-368` valait pour le socle du projet machine, non pour le matériel. La bonne coupe n'est pas « la doctrine dedans ou dehors » mais **dépendance ou commodité** — le motif existait déjà, isolé sur la source de niches du gage, et il devient général.

**Le contrat de la chaîne est repris en trois endroits.** La règle transversale qui interdisait la dépendance au corpus interne dit désormais comment le matériel entre : **une étape nomme un rôle, jamais un fichier**, et c'est le dossier qui fait le branchement ; le matériel vit dans une **valise séparable**, retirée pour diffuser ; ce qui y entre y entre **projeté en clair**, sans nomenclature interne. Le champ de dégradation passe de `socle_absent` à **`a_blanc`** : ce n'est plus un accident, c'est le mode de base, et l'équipé est l'environnement cible.

**Une faute de plus se compte** : une étape qui nomme un fichier de la valise au lieu de son rôle, que le contrôle de généralisation voit déjà.

**Le banc se joue désormais deux fois** — à blanc, puis équipé, sur la même population aveugle. L'écart entre les deux taux est la valeur du matériel, et il se compare au sens d'`A-308` puisque seul l'équipement change.

*Reste à reprendre avant la bascule* : le vocabulaire des skills diffusables, qui traite encore la base documentaire absente comme un cas dégradé, et la troisième branche du gage, qui cite les annexes par leur nom au lieu de leur rôle.

## 20260907 — Le projet machine est décidé, et le banc y déménage

**`A-375` amende le calendrier d'`A-368`.** Le projet dédié à la machine se crée sans attendre le dixième chouchou, et le banc bout en bout s'y joue. Le périmètre du sous-ensemble ne bouge pas ; l'interdit d'écrire à deux endroits se durcit — dès la copie, le point de vérité de chaque pièce de la machine est au projet machine, et le coffre actuel n'en garde aucune copie vivante.

**Ce que le déménagement du banc change à la mesure.** Éprouver la chaîne dans le projet qui la porte, c'est l'éprouver sans la doctrine sous la main. C'est la condition qu'`A-267` pose à toute étape de la machine, et un banc joué au coffre actuel aurait mesuré une capacité que la version diffusée n'a pas.

**Le transfert n'a qu'une route** : une session ne voit qu'un projet, donc les pièces s'exportent d'un côté et se téléversent de l'autre. L'inventaire de ce qui part se tient au moment où il part.

## 20260907 — Les arbitrages de la stratégie entrent au registre, et trois faits les corrigent

**Le registre reçoit les huit arbitrages du fil « stratégie de la machine », `A-367` à `A-374`**, portés par script et non par réécriture. Ils bornent une v1 à deux jours : interface en conversation avec trois arrêts, recevabilité en liste de contrôle plutôt qu'outillée, gage écrit au lieu d'être laissé à trancher, ordre de liasse calé sur le texte en discussion, socle figé au texte initial, banc bout en bout en trois lots.

**Le gage a enfin sa formule et sa source** — texte n° 2247, janvier 2026. La demande du fil d'inscription de la veille, restée sans bloc où se relever, est servie. Les formules pour les collectivités et pour les organismes de sécurité sociale restent non relevées, et elles ne se reconstitueront pas de mémoire.

**Trois relevés postérieurs sont portés dans les entrées, sans modifier aucune décision.** La création d'un projet public est fermée par les contrôles de l'organisation : le sous-ensemble se portera à un second projet privé, la diffusion à un tiers passant par les skills enregistrées et le zip. Le dépôt de droit est ancré **en lecture**, vérifié depuis l'atelier à la révision `553a723` ; **l'écriture n'est pas ouverte**, faute de jeton, et le module de coordination reste à pousser. Le § 10 du gage vit à la skill enregistrée et ne se verse pas au coffre.

**Un écart de composition remonte à l'auteur** : l'arbitrage arrête dix mesures en deux lots, le banc versé le matin même en porte quinze en quatre lots. Le fil d'inscription ne le tranche pas.

**Ce qui ne s'inscrit pas, et pourquoi.** La carte des briques et la table des configurations rendues par le fil de stratégie sont un état, et un état tenu à la main raconte au lieu de compter (A-307) : elles descendront à `livrables/etat_machine.html`, qui est généré, au premier fil qui le régénère. L'ordre d'assemblage, lui, est une décision et il est porté à `A-374`. Le prompt du fil des chouchous n'est pas versé : il a déjà été joué, et son produit est au coffre.

## 20260907 — Le contrôle de généralisation ouvert sur les skills enregistrées, et les externalisables recadrées

**Le contrôle `G` ne contrôlait rien, et le disait comme un succès.** Sa liste de
fichiers ne balayait que le dépôt, où il n'y a de skill que le temps d'un fil qui
en écrit une. Il annonçait « non contrôlé » et la chaîne continuait. La règle
`A-268` avait été rendue mécanique après quatorze fuites relevées à l'œil ; le
mécanisme, lui, était resté tenu à l'œil. Ouvert sur les deux racines où vivent
les skills enregistrées, `G` sort **282 échecs sur onze skills** — 59 noms nus,
73 chemins de dépôt, 150 renvois à la doctrine.

**Les skills se partagent en deux familles, et l'arbitrage est de l'auteur.**
Cinq sont **externalisables** : elles disent une compétence de droit ou de
légistique qui ne suppose aucun corpus. Elles peuvent nommer une source de niche
à condition que la référence soit **contournable et que la dégradation soit
écrite**. Sept sont **internes** : la famille de projection a la doctrine pour
entrée, la disjonction déjà faite ne couvrait que la chaîne de l'amendement.
Une exemption nommée est portée au module de contrôle, jamais à la skill
contrôlée — `A-303`.

**Les quatre externalisables non conformes sont recadrées** : `disposition-cible`,
`analyse-transposabilite`, `vecteur-mesure`, `expose-sommaire` passent à zéro
échec ; `redaction-legistique` y était déjà. **`G` ne bloque désormais que sur les
diffusables** : les internes sortent au dénombrement, avec leur motif de régime,
et leurs 223 renvois au corpus sont attendus, non des écarts. Leur présentation,
elle, n'est mesurée par aucun contrôle.

**`vecteur-mesure` reçoit un lot d'un autre fil, et une règle neuve.** La porte
du domaine des lois de financement est corrigée aux articles `LO 111-3-6` à
`LO 111-3-8`, `LO 111-3` ne définissant plus que les trois espèces ; l'état
`inexistant` reçoit sa cascade de contournement, dont le dernier cran ne se prend
qu'en dernier ; une intention que nul véhicule unique ne porte se rend en deux
jambes. S'y ajoute, sur arbitrage de l'auteur, la **décomposition d'un énoncé qui
vise une entité** : quatre leviers — ressource, affectation, crédits, emploi — et
la structure de financement qui décide lesquels sont ouverts. Elle est écrite
comme première rédaction, sur des cas encore peu nombreux.

**Coût payé.** Le module de contrôle et le fichier de règles ayant changé,
l'archive technique est reversée au coffre.

## 20260907 — Fil d'inscription : deux écritures sur quatre, et le gage sort deux échecs

**Fil de travail, ouvert sur l'atelier nu.** Il n'écrit aucune skill, ne tranche
aucune question de fond, et ne rédige rien. Quatre écritures étaient demandées ;
deux sont sans objet, une est bloquée, une est faite.

**Le registre ne reçoit rien, et la cause est au prompt.** Les huit arbitrages du
fil « stratégie de la machine » y étaient appelés par un renvoi non résolu — le
prompt porte la consigne de les coller et ne les porte pas. Leur texte n'est ni au
coffre ni au fil, et le fil de stratégie prévoyait lui-même de rendre ses
décisions en clair pour que le suivant les inscrive. **Rien n'est écrit au
registre** : un fil de travail n'invente pas ce qu'il doit inscrire. Le gage qui
demandait la formule tabac avec sa source — texte n° 2247 de janvier 2026 — n'a
donc pas de bloc où se relever.

**La skill de rédaction cible est déjà à la version attendue.** L'assert
d'antériorité ne passe pas : la chaîne « À trancher · branchement, gage » n'est
plus au fichier — la ligne des non-tranchés porte désormais « branchement, entrée
en vigueur, fait générateur » — et « ## 10. Le gage » y est. **Rien à copier.**
Le § 10 porte la formule de la taxe additionnelle sur les tabacs, relevée « sur
les amendements au projet de loi de finances pour 2026, commission et séance,
sans variante » ; il ne nomme pas le numéro de texte, et l'écart se dit.

**Et le gage de cette écriture mord contre elle.** `make G` au dépôt sort
« aucun fichier de skill au dépôt, non contrôlé » : le contrôle de généralisation
est aveugle tant que la skill n'est pas posée à l'atelier, et c'est ainsi qu'une
version neuve peut s'enregistrer sans jamais passer devant lui. Joué sur la skill
enregistrée, il sort **deux échecs, tous deux au § 10** : `G5` référentiel
interne, ligne 236, « REF_norme » ; `G6` nomenclature interne, ligne 259,
« A-224 ». Par A-303 une skill qui porte l'un des deux n'est pas publiable. **La
correction est une écriture de skill** : elle n'est pas de ce fil, et elle
remonte.

**`coordination.py` est absent et se déclare tel.** Ni à l'atelier, ouvert vide,
ni au dépôt de droit à la révision `553a723` du 20260904. Rien à pousser ; il
reste au bloc des attendus, avec `portes_ouvertes.py` et `controle_socle_plf.py`.

**Le contrôle a tourné, périmètre déclaré.** Déplié : l'archive technique — 76
fichiers, dépliage comparé à l'octet à celui de `coffre.py`, zéro divergence —,
l'index, les empreintes, le manuscrit, le proto Données, le journal.
`make restauration` : **`R1` à zéro**, `R3` et `R5` à zéro, `R4` à deux, les deux
pièces déjà déclarées sans empreinte. `make controle` : **zéro échec sur tous les
contrôles joués** — lexique `L1` à zéro, structurel zéro échec et quatre alertes
connues, arithmétique zéro échec et 23 écarts consignés, chiffres zéro échec et
93 entrées à sourcer, hypothèses zéro échec, apports zéro échec et 20
signalements. `I2` à `I5` à zéro ; `I6` non contrôlé, l'inventaire du coffre
n'étant pas au dépôt. **`I1` sort à 39** : ce sont les dérivés et référentiels que
ce fil n'a pas régénérés, et A-338 pose que `I1` n'est pas un invariant.

**La preuve externe du verbatim tient.** `extraire_notes.py` rejoué sur le
manuscrit restauré redonne `referentiels/notes_manuscrit.json` **identique à
l'octet** — `a6a07a73…`, 141 notes, 37 portant un chiffre.

**Jauge** : 1 889 290 sur 2 000 000 avant, marge 110 710 ; **1 890 685**
après le versement du journal et des empreintes, marge **109 315**. Le bloc
porté coûte 3 965 octets et 1 395 jetons ; l'archive technique se replie
identique à l'octet et ne se reverse pas.

**Reste ouvert, et rien de cela n'est de ce fil** : les huit arbitrages du fil de
stratégie, à fournir avant qu'un fil les porte ; les deux échecs `G` du § 10 de
la rédaction cible ; le numéro de texte de la formule de gage ; `A-309` pour les
numéros `A-270` à `A-298` — ce fil a déplié le journal et ne détient pas le bloc
à porter.

## 20260904 — L'éval de la rédaction cible, et un coffre qui se desserre

**Trois fils se sont succédé ce jour-là et deux n'avaient pas la main sur la
méthode** : celui du site, celui qui a écrit `disposition-cible`, puis celui-ci.
Ce qu'ils ont versé sans pouvoir le déclarer est déclaré maintenant — la
passation du site, le prompt d'éval, les deux modules de la réapplication et les
trois cas travaillés. **Quatre entrées d'index dues, dont une que personne
n'avait vue.**

**Le registre ne repassait plus au coffre, et c'est mesuré au refus du
versement** : 344 903 octets, ~86 226 jetons, pour ~80 414 de marge. Un
remplacement n'est pas crédité de la place que l'ancienne version libère, et la
règle vaut donc aussi pour un document qui se réécrit — tout ce qui grossit finit
par ne plus pouvoir revenir. Le registre est scindé au 20260901, corps recomposé
**identique à l'octet** avant versement, questions ouvertes gardées au courant.

**`positions.json` sort du coffre, sur arbitrage de l'auteur et après preuve.**
Régénéré depuis le seul référentiel de doctrine, il revient identique à l'octet.
L'archive a dû être **supprimée avant d'être réécrite**, faute de quoi son
versement se refusait. **89 111 jetons rendus**, marge portée à 169 525. Les deux
autres candidats d'A-346 restent non prouvés, donc non proposés.

### L'éval de la rédaction cible

**380 couples au lot d'épreuve, 42 tirés**, par une règle écrite en code avant
que le premier couple soit regardé : stratifié proportionnel, pas régulier dans
chaque strate, aucune graine. Les couples hors strate y sont à leur poids — les
écarter ferait un banc plus facile que le texte.

**L'unité de notation n'est pas le couple, c'est le bloc de disposition.** Le
texte déposé écrit en arbre : le chapeau porte l'adresse, les subordonnés portent
les opérations. Noter sur le chapeau seul, c'est noter sur une phrase qui ne
prescrit rien. **24 des 42 blocs font plus d'un alinéa**, le plus gros en fait
quatorze.

**L'aveuglement se tient par des fils séparés, et il a été vérifié.** Six fils
ont écrit les énoncés en voyant la disposition de l'administration ; sept fils
ont joué la skill sans la voir. Les transcripts des sept ont été relevés :
**chacun ne porte les chemins interdits qu'une fois, celle de son prompt.** La
règle des énoncés est écrite, antérieure au premier énoncé, et elle se joue —
zéro anomalie sur 42.

**Population notée 31** : 42 tirés, 3 indicibles — l'effet ne se dit pas sans
nommer une subdivision —, 8 hors capacité — le siège est hors de l'extrait de
droit, et la skill le déclare, ce qui est le comportement attendu. Dégradation
`partiel` : l'énoncé et le dépôt de droit, pas la recherche publique que le proxy
refuse, pas la doctrine.

**Ce que ça donne.** L'article visé est tenu : **100 % des articles attendus
figurent dans la disposition écrite**, les deux écarts du taux strict étant une
différence de convention sur l'insertion d'article, où le socle relève l'ancrage
et la skill nomme l'article créé. L'opération sort à **32 % en strict et 71 % en
nature** — l'écart est presque entièrement du découpage et du verbe, non de
l'effet, et la table d'équivalence qui le neutralise est proposée, non validée.
La couverture des effets est **complète dans 87 % des cas**. **Réapplication :
41 colonnes sur 41 à l'octet.**

**Trois choses que l'éval apprend et qu'aucune lecture n'aurait données.**

La **portée n'est pas mesurable** : le détecteur lit la cible en tête de phrase
et non en complément circonstanciel, qui est la forme courante du texte réel.
71 % des portées sortent indéterminé, **des deux côtés**. Le taux de 39 % note le
détecteur, pas la skill.

**La réapplication à 100 % ne dit rien de la justesse d'un C.** Sur l'article
L. 314-24 du code des impositions sur les biens et services, l'administration
réécrit l'article entier, la skill retranche des alinéas, et sa réapplication
passe. La porte est cohérente et elle est aveugle — le contrat l'annonçait, le
banc le démontre.

**Ce qui est à corriger tient en deux points** : la couverture d'un article
travaillé en plusieurs endroits — quatre cas sous-couvrent, l'un rendant trois
opérations sur huit — et le choix entre réécrire et retrancher. Les **135 doutes
déclarés sur 31 cas**, aucun cas n'en étant dépourvu, sont la sortie la plus
solide de l'étape.

### Deux constats d'appareil

**La carte du projet levait depuis deux jours, et rien ne pouvait le dire.** Son
générateur pointait deux chemins renommés les 20260901 et 20260902 ; il échouait
donc à chaque rejeu, et la carte au coffre était en retard sur l'index. A-19 en
fait la première chose que lit un fil neuf : elle mentait. Réparée et reversée.
**Rien ne contrôle qu'un générateur du coffre tourne encore.**

**Deux binaires que l'index déclare au coffre n'y sont plus** — le guide
néerlandais coût-bénéfice et le guide public du budgétaire 2023 —, et ils ne se
recomposent pas. C'est de l'input, et cela revient à l'auteur. Cinq pièces
jointes déclarées à l'index sont sorties après digestion : régulier au titre de
R5, mais l'index ne le disait pas.

**Versé** : l'archive technique à 75 fichiers, le registre scindé en deux, le
prompt du fil de correction, la règle des énoncés, les trois pièces de l'éval qui
ne se régénèrent pas, la carte réparée, l'index à 213 artefacts, les empreintes.
`R1` à zéro, `I2` à `I5` à zéro. Les colonnes A et C rendues par les joueurs ne
sont pas versées : un demi-mégaoctet dont A est régénérable et C se refait en
rejouant l'éval.

**Reste ouvert, et rien de cela n'est de ce fil** : la table d'équivalence
légistique, qui revient à l'auteur ; la portée, à rendre mesurable avant toute
conclusion sur elle ; les deux candidats à la libération, non prouvés ; les trois
modules que le corpus invoque et qui n'existent nulle part ; et `make controle`,
qui s'arrête sur `REF_chiffres` absent — le fil n'avait pas déplié le manuscrit,
et un dérivé absent se constate, il ne se régénère pas à l'ouverture.

*Relevé au passage* : **la dette du journal du 20260902 est close** — les quatre
entrées de ce jour y sont, portées depuis. A-309 ne vaut plus que pour les
numéros `A-270` à `A-298`, consommés sans être au registre.

---

## 20260903 — Deux rapports tiers sortent, et le socle de la loi de financement entre

**Décision de l'auteur, à la clôture du fil de la digestion.** Les deux rapports
tiers ont quitté les pièces jointes du projet — le rapport **AIRE** « Le modèle
social français contre les couples » de février 2025, dont le nom de fichier
annonçait à tort Génération Libre, et **LIBER volume II** de Génération Libre,
janvier 2017.

**Le retrait a rendu 172 190 jetons** : la jauge passe de 1 971 239 à 1 799 049
sur 2 000 000. Les 104 000 que demandait la part irréproductible du socle de la
loi de financement rentraient. **`referentiels/redaction_plfss.json` est
versé** — 351 968 o, 55 articles, 1 070 alinéas, 340 adresses. **La dette
d'A-346 est close le jour où elle a été écrite**, et les trois candidats à la
libération qu'elle nommait ne sont pas touchés : ils restent instruits et non
tranchés pour la prochaine fois que la jauge mordra.

**Les deux pièces ne sont pas digérées pour autant, et leur verdict tient
inchangé** : digestion due, avec leur référence exacte écrite avant leur sortie —
elle ne s'invente pas, et le nom du premier fichier aurait fait chercher un
rapport qui n'existe pas. Elles rentreront par pièce jointe du fil qui les
digérera. **R5 se lit donc par ses deux bouts** : une digestion chasse son
original, et un original sorti d'avance doit son retour à sa digestion. Aucune
phrase du corpus ne s'appuie aujourd'hui sur l'une ou l'autre.

**Versé** : la part irréproductible des deux socles du texte déposé, l'archive
technique, l'index à 199 artefacts et 44 sources, les empreintes, le registre des
digestions, le registre des arbitrages et ce journal. Dépliage prouvé 71 sur 71,
`R1` à zéro, `I2` à `I5` à zéro.

## 20260903 — Le texte déposé entre au corpus, et le banc de la rédaction est partagé

**Fil de production court. Il n'a écrit aucune skill, rédigé aucune colonne C, et
n'a pas pris connaissance du lot d'épreuve.** Son objet était de mettre fin à une
dette : le texte financier avait été digéré deux fois et son contenu n'était
toujours pas au coffre.

**Les deux textes sont digérés et les deux tables plates ressortent identiques à
l'octet** — `2863d12f…`, 23 061 o, 396 lignes pour la loi de finances ;
`8aa17c75…`, 11 634 o, 218 lignes pour la loi de financement. Les deux socles
retrouvent l'empreinte que la passation du sas déclarait, `20eebda5…` et
`44eeb4b9…` : même pièce, même script, même JSON. **82 articles et 2 164 alinéas
au PLF, 55 articles et 1 070 alinéas au PLFSS.**

**`articles_ouverts_plf.py` est réécrit.** Il était invoqué par le `Makefile`,
déclaré aux manquants, et absent du dépôt comme du coffre. Les deux tables
versées donnaient sa sortie attendue à l'octet : la réécriture ne s'est pas crue,
elle s'est prouvée. Ce que la spécification cachait et qu'il a fallu retrouver :
l'unité de la table est le fragment d'énumération et non la référence du socle —
« L. 314-2, L. 314-3 et L. 314-4 » fait trois adresses —, « à » ne sépare pas une
fourchette, et une adresse dont la pièce ne nomme pas le texte s'écrit « aucun
texte nommé », qui n'est pas l'« indéterminé » de la grammaire.

**Le socle de la loi de finances ne tient pas à la jauge, et c'est mesuré au
refus du versement : 494 461 jetons pour 310 550 de marge.** Ni la sérialisation
compacte ni le retrait de l'exposé des motifs n'y changent rien. La clause de
repli d'A-342 s'applique donc, et **c'est la part irréproductible qui se
verse** : `referentiels/redaction_plf.json`, 848 687 octets, 251 270 jetons
mesurés, structure des articles, alinéas exacts, hors-alinéa des tableaux et
adresses relevées à la disposition.

**Le socle portait le même verbatim dans deux rendus, et c'est ce qui a rendu la
coupe possible** : la sortie brute de mise en page et son reflux par alinéa
disent la même chose pour un demi-mégaoctet de plus. On garde le reflux, qui est
la forme qu'une disposition modificative adresse. L'exposé des motifs sort comme
étant de l'indice et non de la norme — et cela coûte le rejeu depuis le coffre du
quatrième relevé de la lecture en creux, qui se dit.

**La loi de financement n'est pas versée, faute de jauge, et la dette est
chiffrée** : 104 000 jetons requis, 59 280 disponibles. Trois candidats à la
libération sont mesurés et aucun n'est tranché — ils touchent ce que le corpus
porte, et leur identité au rejeu se prouve au lieu de s'affirmer. **Le coffre est
à saturation ; ce n'est plus une contrainte de fil, c'est un arbitrage à rendre.**

**Le partage calibrage / épreuve du banc de la rédaction est fixé, et c'est du
code.** A-330 exige qu'il se fixe avant que le fil de la skill s'ouvre : la règle
de sélection est un module, elle se rejoue, et elle a été écrite avant qu'un seul
couple soit regardé. **384 couples (alinéa, adresse ouverte), 239 éligibles,
quatre couples de calibrage — un par opération, la quatrième strate mesurée et
non choisie — et 380 couples d'épreuve scellés**, que le banc ne liste pas et qui
se recalculent. Le tirage est le premier couple de chaque strate dans l'ordre du
texte : aucune graine pseudo-aléatoire, une graine étant un choix caché.

**Deux modules de plus que le corpus invoque n'existent nulle part**, trouvés par
croisement mécanique du `Makefile` avec le dépôt. `controle_socle_plf.py`, appelé
par `make controle` sur les deux socles : sa règle est gardée par un test de
présence, donc rien ne cassait — **il ne contrôlait simplement rien, et cela ne
se voyait pas**. Et `portes_ouvertes.py`, la jointure des portes ouvertes, dont
l'absence laisse les douze adresses intérieures des cinq fourchettes comptées
fermées. *Un manquant qui ne casse rien ne se déclare pas tout seul.*

**Une règle du corpus n'était pas dans le code.** A-286 posait le 20260902 que
`coffre.py` plie ce que l'index adresse à l'archive et non ce que le rang y
adresserait. C'était au journal et pas au module : la sélection se faisait
toujours sur le seul rang, et l'archive a doublé de taille au premier
`make coffre` du fil. Corrigé, avec une table d'exception à l'index — un
référentiel plus gros que l'archive entière ne s'y replie pas, sous peine de
rendre sa réécriture impossible.

**Versé** : la part irréproductible du socle de la loi de finances, l'archive
technique à 71 fichiers, l'index à 201 artefacts et 5 manquants déclarés, les
empreintes, le banc d'épreuve avec son lot neuf, le registre et ce journal.
Dépliage prouvé 71 sur 71, `R1` à zéro, `I2` à `I5` à zéro. Les deux tables
plates ne sont pas reversées : elles sont identiques à l'octet, et rien de
recopié ne se reverse.

**Reste ouvert, et rien de cela n'est de ce fil** : la part irréproductible du
socle de la loi de financement, et l'arbitrage sur ce qui sort du coffre pour lui
faire place ; les deux modules manquants ; et le bloc de journal du 20260902, que
le fil de structuration n'avait pas la main pour écrire.

## 20260903 — La rédaction cible recadrée, le sas absorbé, l'invisibilité comptée

**Le fil de structuration, ouvert la veille, s'est poursuivi et a été recadré
deux fois par l'auteur.**

**L'étape de rédaction n'est pas la disposition modificative, c'est le signe
« = » du trois colonnes.** Le contrat la décrivait par quatre « formes »
— article de code, alinéas du texte déposé, article additionnel, crédits — qui
sont une taxonomie de l'emballage, laquelle dépend du véhicule. L'étape la plus
véhicule-agnostique de la chaîne était donc décrite comme la plus dépendante.
Elle rend désormais A le texte en vigueur, B la réforme visée, C le texte
révisé ; **la forme modificative se dérive de A vers C et se prouve** —
réappliquée à A, elle doit redonner C à l'octet. Sept opérations sur le texte,
dont une, posée avant les six autres, sur la version future déjà votée.

**L'étape a deux niveaux, et le mur est au premier.** Une mesure éclate en lots
avant de se rédiger — huit verbes, dont `rien à faire`, qui est un résultat et se
déclare. La grille de complétude a six fonctions. Le modèle est la partie
juridique de la note sur le logement social, **et c'est une borne haute, pas la
norme** : mesuré, une mesure courante pèse huit fois moins.

**Deux épreuves sur pièce, et elles ont corrigé le cadrage.** Le dépôt de droit
cloné, les neuf cibles de la note passées au compteur : 393 articles citent
leurs cibles. Puis le lot d'un contre-budget de tiers, dix-huit mesures : médiane
de 2 articles, 36 alinéas, 8 renvois internes, 12 renvois entrants sûrs. **Le
relevé brut des renvois est faux d'un facteur cinq à trente** — l'article 14 du
code général des impôts sort à 1 216 en brut et 36 en sûrs — et la règle de
déduction n'est pas un raffinement : sans elle le relevé est du bruit. Une
première mesure a été refaite : elle cherchait « L302-5 » quand le droit écrit
« L. 302-5 ».

**Deux modules que le corpus invoque n'existent nulle part.**
`coordination.py` au dépôt de droit — un compte indépendant retrouve pourtant
exactement les neuf articles qu'il avait publiés, donc c'est le versement qui
manque, pas le travail. Et `articles_ouverts_plf.py`, que le `Makefile` appelle
pour bâtir les deux tables plates du texte déposé : les tables sont versées et
ne se régénèrent pas. Déclaré aux manquants.

**Le sas de la lecture en creux est absorbé**, dépliage conforme à son empreinte,
sept fichiers sur sept. Fusion du `Makefile` par union contrôlée, aucune variable
ni cible perdue des deux côtés. Quatre modules neufs entrent, dont l'extracteur
du socle du texte déposé. Quatorze artefacts déclarés, huit entrées de registre
portées par découpe et numérotées à l'insertion. Le sas est supprimé du coffre.

**Le contrôle `I6` naît, et il compte l'invisibilité.** Quatorze documents
étaient au coffre et hors index : aucun contrôle ne pouvait les voir, et un fil a
réclamé en pièce jointe un travail que deux d'entre eux portaient. L'inventaire
du coffre se relève au transcript, jamais retapé ; `I6` sort toute pièce que
l'index ne réclame pas. **Treize à la première exécution, zéro après
déclaration.**

**Deux corrections de fond de l'auteur.** Le lot d'un tiers n'est pas notre
profil d'usage : deux de ses mesures sur cinq créent un article, quand notre
esprit est de simplifier — **l'abrogation est notre opération dominante**, et
c'est celle où tous les contrôles mordent. Et la rédaction est d'abord un
exercice de rigueur : ce qui la règle est le guide de légistique, la Constitution
qui dit **le domaine de la loi**, et les précédents. La colonne C n'écrit rien
qui relève du décret, et c'est un refus.

**Versé** : le contrat de la chaîne réécrit, le prompt du fil suivant, le banc
d'épreuve, l'état de la machine régénéré, l'index à 189 artefacts, l'archive
technique à 68 fichiers. `I6` à zéro, `R1` à zéro, restauration à blanc vérifiée.

---

## 20260902 — Le contrat de la chaîne, le contrôle de généralisation, le banc d'épreuve

**Fil de structuration de la machine à amendements.** Il n'a écrit aucune skill
et n'a joué aucune éval : un fil ne juge pas une skill qu'il a écrite, et
celui-ci a touché l'appareil de mesure.

**`methode/contrat_chaine_amendement.md` est versé.** Huit étapes, ce que chacune
reçoit, rend et déclare avoir douté. **Un objet unique voyage** — le dossier de
mesure — et **chaque étape déclare ce qu'elle lit** : l'utilisateur voit la
boucle complète, et le découpage reste réel puisqu'une étape se rejoue seule avec
ses seuls blocs. Le véhicule est une donnée du dossier, jamais l'hypothèse d'une
étape.

**Le contrôle `G` est au `Makefile`.** Il refuse dans un fichier de skill toute
mention d'un déposant nommé, du projet, du manuscrit, du coffre, d'un référentiel
interne, de la nomenclature interne — **frontmatter compris**, où la fuite avait
survécu le plus longtemps. Il bloque sur ce qui identifie, signale le reste, et
porte une seule exemption écrite dans le module de contrôle : l'adresse d'un
dépôt public. Éprouvé à l'envers : six échecs sur une skill de fuite injectée,
zéro sur une skill propre.

**`referentiels/lots_epreuve.json` est le banc d'épreuve** — un lot par véhicule,
la population, les contaminés, et la suite des mesures jouées. Il porte la règle
qui manquait : **deux taux ne se comparent que si la population aveugle est la
même**, et le rejeu à 90,9 % y est inscrit `comparable: false`.

**`livrables/etat_machine.html` remplace l'état tenu à la main.** Deux grilles,
zéro chiffre saisi : tout ce qui s'y compte sort du banc, et ce qu'aucun lot ne
porte reste vide.

**Deux défauts de l'appareil de mesure corrigés.** La clé de l'éval fuyait par
son propre résumé — elle nommait les cas sans adresse relevable avant que le fil
joue. Et la notation mesurait le rappel en ignorant la précision : les deux
dimensions se publient désormais ensemble, le chemin des réponses se déduit du
lot, et les contaminés se vérifient contre la population au lieu de s'annoncer.

**Deux corrections de nommage.** Le rapport de clôture du fil gagnants-perdants
quitte `methode/ETAT_DU_CHANTIER.md` pour son vrai nom, contenu inchangé à
l'octet. Et le §3 de la carte des chantiers se réduit au périmètre et aux
dépendances : ses comptes descendent dans le dérivé régénéré.

**Trois faits d'appareil.** Les empreintes cessent d'être éternelles : une
empreinte que l'index ne déclare plus est retirée. La jauge du coffre se compte
en **jetons**, pas en octets, et un versement n'est pas crédité de la place que
l'ancienne pièce libère. Et la restauration à blanc a tourné dans un dépôt
vierge — 80 artefacts, `R1` à zéro — après relecture du coffre par fil auxiliaire,
le transcript portant l'état d'avant et non celui d'après.

**Six questions à l'auteur, quatre tranchées** : les trois leviers de la dépense
locale dans l'ordre, le registre parlementaire avec trois mots tenus, l'objet
unique à lecture bornée, l'ordre de dépôt qui ne s'inscrit nulle part par
avance, le calendrier d'examen déclaré inconnu. **Deux étaient de la tambouille
et n'auraient pas dû être posées** — une question se pose dans les termes de ce
que l'auteur décide, jamais dans ceux de l'outil.

## 20260902 — Le domaine du PLFSS corrigé, et l'audit du fil porté au registre

**Un fil frère a relevé que le corpus se trompait d'article**, et il avait raison
sur le fond. Vérification faite sur le texte au coffre : `LO 111-3` ne définit
plus que les trois espèces de lois de financement depuis la loi organique
n° 2022-354 du 14 mars 2022. La porte d'un amendement au PLFSS est aux
`LO 111-3-6` à `-3-8` ; les monopoles, dont celui sur les exonérations de
cotisations, aux `-3-14` à `-3-16` (A-297).

Le relevé des dix-huit articles est déclaré et restauré au dépôt —
`sources/domaine_lfss_LO111-3.md`, adresse de coffre `reference/`, au régime de
`LOLF_reference` : un texte normatif de référence, pas un document de méthode.
Restauré par copie d'octets, 5 230 o.

**Trois documents corrigés** : `appareil/portes_domaine.py`, dont l'entrée
nommait LO 111-3 comme le domaine et le déclarait non relevable ;
`methode/procedure_contre_plf.md` ; `methode/prompt_fil_courant.md`, deux
endroits. Le registre et le journal ne se réécrivent pas.

**Deux choses du fil frère ne tenaient pas, et se corrigent aussi** (A-298). Il
affirmait que `reference/gabarit_expose_sommaire.md` porte la mention fautive :
lecture faite du document entier, aucune occurrence. La phrase est corrigée dans
le relevé lui-même. Et il numérotait son entrée A-282, déjà pris — par la règle
qui interdit à un fil de production de numéroter.

**L'audit du fil de réconciliation est porté au registre** sur arbitrage de
l'auteur (A-299). Quatre manquements, une cause commune : tous les contrôles
joués portaient sur le transport des octets, aucun sur la véracité d'une phrase.
Une affirmation sur une pièce jamais ouverte versée comme vraie ; sept chiffres
recopiés d'un récit au lieu d'être comptés ; une pièce redemandée à l'auteur
alors qu'elle était au projet ; une chaîne entière jouée sans annonce de coût,
juste après le relevé d'une erreur. Les quatre règles qui en sortent sont à
l'entrée, et la cinquième est la seule qui ne se mécanise pas : dire d'où vient
chaque phrase versée — relevée, héritée, ou déduite.

## 20260902 — Les portes ouvertes du texte déposé

**La chaîne s'est jouée entière sans rien demander à l'auteur.** Les cinq
classeurs sont des pièces jointes permanentes du projet : ils se lisent par
`project_read`, qui rend leurs octets, et se convertissent en `.xlsx` par
`soffice --headless`. Le fil courant les rangeait derrière « les pièces
jointes », ce qui laissait croire à un dépôt à refaire chaque fois (A-296).

Ce que la chaîne a produit, dans l'ordre : `socle_budgetaire.json` — 465 dépenses
fiscales, 278 taxes affectées, 180 opérateurs, 749 ODAC-ODAL, 128 programmes,
2 351 lignes de PAP, 41 économies, 18 lignes de grande synthèse ; puis
`REF_norme.json` — **1 856 entrées, 880 vecteurs déclarés**, 614 trouvés et
1 242 à trouver ; puis, par un module neuf, la jointure avec les deux tables
d'articles ouverts.

**Le résultat, et c'est lui qui sert à préparer les amendements.** Sur les
880 vecteurs, **100 adresses tombent sur un article que le texte déposé ouvre
déjà** — 99 au PLF, 1 au PLFSS. Elles portent **90 mesures, toutes des dépenses
fiscales, pour 25,3 Md€, soit 28 % du montant des 465**. Aucune proposition du
corpus, aucune taxe affectée, aucun opérateur, aucun ODAC-ODAL, aucun programme
ne tombe sur une porte ouverte : les portes que le PLF 2026 ouvre sont des portes
de dépense fiscale.

Les articles du véhicule les plus chargés : l'article 5 et l'article 18 avec
24 adresses chacun, l'article 23 avec 22, l'article 21 avec 20, l'article 12
avec 13.

**Deux défauts relevés en chemin, et mesurés.** La colonne
`article_selon_ref_norme` des tables tronque les suffixes de rang — joindre
dessus aurait fait passer 77 vecteurs pour ouverts à tort (A-293). Et
l'affirmation « le PLF ne rend aucune tête de division », que le corpus portait
au profil `plf` et que l'auteur a contestée, est requalifiée : ce qui était
établi est qu'un repère ne mord pas, non que la pièce ne porte rien (A-294).
Le départage demande le PDF.

**Ce que le fil a versé** : `appareil/portes_ouvertes.py`, la règle de `make` qui
l'appelle, quatre entrées de registre, et la correction des chiffres que le fil
courant portait faux — 39 divergences de grammaire au PLF et non 34, huit
colonnes aux tables et non seize.

## 20260902 — Les quatre sas sont absorbés, le corpus les porte

**Le fil de réconciliation a tourné. Rien de ce que les deux fils du socle ont
produit ne vit plus dans un sas.** Il n'a produit aucun fond : il a inséré,
déclaré, plié, supprimé.

**Les trois modules du socle sont à l'archive technique** —
`socle_plf_texte.py`, `articles_ouverts_plf.py`, `controle_socle_plf.py`. Le
dépôt s'est déplié à l'octet sur les trois empreintes annoncées, puis le
correctif a épinglé `divisions_attendues` à 0 au profil `plf` : ancre trouvée
une fois, sortie `fe7c6422…`. **Deux passations annonçaient deux empreintes du
même module** ; c'est celle que le script imprime qui fait foi, et le correctif
la portait juste (A-283).

**Le registre porte quinze entrées de plus, et il n'a pas été renuméroté.** Il
allait jusqu'à A-266 ; le bloc du PLF court de A-267 à A-272, celui du PLFSS de
A-273 à A-281, et les deux enchaînaient déjà. **Un renvoi du bloc PLFSS était
resté à l'ancienne numérotation** — A-259 au lieu d'A-270 — et il est corrigé
(A-284). Le journal porte deux blocs de plus.

**Les deux insertions se prouvent de l'extérieur, et la preuve a tenu.** Le
registre privé de ses blocs neufs redonne `db8de1dc…`, 254 432 octets, 4 881
lignes — l'empreinte que le coffre portait. Le journal redonne `46363d9d…`,
128 068 octets. Rien du texte ancien n'est passé par le modèle (A-285).

**Onze artefacts entrent à l'index** : les trois modules, les deux socles de
texte, les deux JSON d'ouverts, les deux tables plates, et les deux relevés.
**Les deux tables plates vont au coffre comme documents et non dans l'archive**
— ce sont les seules formes de cette matière qui se lisent sans outil (A-16), et
`coffre.py` plie désormais ce que l'index adresse à l'archive plutôt que ce que
le rang y adresserait (A-286). Elles sont au dépôt et concordent à l'octet avec
les empreintes que les deux passations annonçaient : `2863d12f…` pour les 386
adresses du PLF, `8aa17c75…` pour les 208 du PLFSS.

**Quatre déclarations manquaient au corpus, et aucune n'était inscrite comme
sas.** Le registre des sas lui-même, qui était au coffre sans être déclaré ; le
registre des digestions attendues ; la note du dépôt de droit, qui portait en
dernière ligne « entrée d'index due » ; et le prompt de versement écrit par le
fil PLF pour le fil PLFSS (A-287, A-289). **Ce dernier a été supprimé le même
jour sur arbitrage de l'auteur** — son fil est clos, et ce qu'il portait d'utile
est porté à `methode/sas.md` (A-292). `I2` à `I5` sortent à zéro.

**Le `Makefile` porte les deux chaînes du socle du texte**, conditionnelles à la
présence des pièces sous `sources/plf/` et `sources/plfss/`, qui entrent par
pièce jointe (A-234). Le profil se passe en troisième argument ; sans lui, les
repères du PLF ne se retrouvent pas sur la pièce du PLFSS et la génération
s'arrête, ce qui est le comportement voulu. `make controle` joue les deux
contrôles de socle quand la pièce est là, et le dit quand elle ne l'est pas.

**Un `R1` s'est présenté à l'ouverture et il ne cachait pas un faux.**
`methode/localisation.md` fait 11 287 octets au dépôt contre 10 077 à son
empreinte : il a été versé le matin même par le fil PLFSS, après le dernier
relevé. Deux lectures indépendantes du coffre rendent les mêmes octets. C'est
l'empreinte qui retardait, et **c'est désormais le régime et non une dérive** :
un fil de production ne joue pas `make coffre`, donc tout sas laisse une
empreinte en arrière, et c'est au fil de réconciliation de la relever (A-290).

**Trois règles de l'auteur passent à `CLAUDE.md`** : un fil de production rend
ses entrées de registre titrées et datées, sans numéro ; un fil qui touche
`methode/` ou un module partagé d'`appareil/` est seul ; tout sas s'inscrit
d'une ligne à `methode/sas.md` en fin de fil (A-282).

**L'appareil à la clôture.** `make restauration` : `R1` fermé, `R3`, `R4` et
`R5` à zéro. `make index` : `I2` à `I5` à zéro, les 30 anomalies `I1` étant des
dérivés et des référentiels dont les sources — le manuscrit, les classeurs, les
deux PDF — sont hors du périmètre déplié. Contrôle structurel : zéro échec,
quatre alertes connues. Contrôle arithmétique : zéro échec, 23 écarts consignés.
Notes : `N1` à zéro, `N2` à onze, connues. `controle_chiffres.py` ne se joue pas,
faute de `REF_chiffres.json`, qui demande le manuscrit.

**Les quatre sas sont supprimés du coffre** et leurs lignes ont quitté
`methode/sas.md`, qui ne porte plus aucun sas ouvert.

**Reste ouvert, et rien de cela n'est de ce fil.** Le socle du PLF et celui du
PLFSS ne se régénèrent que si les deux PDF sont joints. La jointure des 386 et
des 208 adresses dans la colonne `variante` de `REF_norme` demande les
classeurs. `referentiels/articles_ouverts_plf_compact.json` du 20260901 n'existe
plus au coffre et ne sort pas de ces trois modules : il ne se laisse pas vieillir
en silence, il se régénère ou il n'existe pas. La ventilation par partie au PLF
n'existe pas — `divisions_attendues` est épinglé à 0, et c'est un manque déclaré.
La troncature de la grammaire de `ref_norme` sur les 465 dépenses fiscales n'est
toujours pas mesurée. Et `R2` compte toujours l'archive technique parmi les
non-restaurés alors qu'elle concorde à l'octet (A-194).

## 20260902 — Le socle du texte du PLFSS, et ce que la pièce impose

**Le socle du PLFSS est fait.** Une pièce demandée à l'auteur — le PDF n° 1907 —
et trois produits : le socle, la liste des articles ouverts, le contrôle qui les
prouve.

**Ce n'est pas un second extracteur.** L'auteur l'a tranché en cours de fil : le
PLFSS est un **profil de pièce** déclaré dans l'extracteur du PLF. Cinq repères
sur cinq diffèrent d'une pièce à l'autre, et aucun n'appartient à la famille
« projet de loi ». Le découpage, la grammaire d'adresse, la liste des codes et
les dix contrôles restent uniques.

**55 articles, pages 4 à 150, 1 070 alinéas**, la rédaction exacte et l'exposé
des motifs rattaché à chacun dans deux champs qui ne se mêlent jamais. Aucune
page lue en image ; les huit tableaux gardent leurs lignes brutes et se
déclarent. **208 adresses ouvertes sur 32 textes**, dont 110 au code de la
sécurité sociale : c'est ce qui alimente la colonne `variante` pour le second
véhicule. **Zéro divergence de grammaire du numéro sur 208**, contre 34 sur 386
au PLF — les adresses du PLFSS sont toutes de forme `L. nnn-n`.

**Trois choses que la pièce a imposées, et qu'on n'a pas forcées.** L'hypothèse
« toute tête d'article ouvre une page » est tombée — six pages en portent deux,
une en porte trois, et cinq articles sortaient vides : le découpage a été repris.
La pièce ne numérote pas ses alinéas en clair, elle les **pastille** : 1 060
glyphes de police symbole, décodés en 55 suites strictement continues, sans trou
ni doublon. Et elle porte **trois parties dont deux nommées « DEUXIÈME
PARTIE »**, sans aucune partie pour l'exercice clos — le relevé du 20260831
venait d'une page web, celui-ci du texte.

**Le dispositif a mordu deux fois contre nous, et c'est ce qui compte le plus.**
La pièce écrit p. 117 « Le code **la** sécurité sociale est ainsi modifié : »,
sans le « de » : le chapeau ne nommait rien, l'héritage restait en place, et
**treize articles du code de la sécurité sociale sortaient sous « code rural et
de la pêche maritime »**. Et la branche « de l' » de l'expression qui lit le
texte nommé après une référence **n'avait jamais pu s'apparier**, faute d'une
espace après l'apostrophe : cinq adresses de plus, fausses ou perdues. Les deux
sont corrigées, la seconde vérifiée par diff des 340 références, zéro
régression.

**Dix contrôles, aucun échec**, et l'un se déclare non jouable plutôt que de se
replier : le PLFSS n'a pas de sommaire, donc `S3` n'a qu'une source et le dit.
Déterminisme prouvé dans un dépôt vierge, à l'octet.

**Conséquence pour le PLF** : le script a changé, donc le JSON change, donc
l'empreinte `4413b7df…` du socle PLF est périmée. Le socle du PLF se régénère
avec la version à deux profils, ses dix contrôles se rejouent, et son compte
d'articles ouverts se confronte au 386 publié.

**Reste ouvert** : les cinq relevés mécaniques d'A-230 — mots de portée, dates,
absences attendues, chiffre pris à l'état, trois colonnes —, qui se calculent sur
le socle sans rouvrir la pièce et sans lesquels la base ne sert pas la lecture en
creux ; la jointure des 208 adresses dans `REF_norme`, qui demande les
classeurs ; la grille des portes du domaine du PLFSS, sur l'article LO 111-3 du
code de la sécurité sociale, qui entre par pièce jointe.

## 20260901 — Le socle du texte déposé, et ce que le PLF rouvre déjà

**Le fil 2 est fait.** Il demandait une seule chose à l'auteur — le PDF du PLF —
et il rend trois pièces plus leur contrôle.

**`referentiels/socle_plf_texte.json`** : 82 articles, le liminaire et 1 à 81,
2 164 alinéas, la rédaction exacte, la page dans la pièce, et l'exposé des
motifs rattaché à chacun. 48 articles en première partie, 33 en seconde, le
liminaire hors partie. **L'exposé des motifs est indexé avec l'article et
jamais confondu avec lui** : deux champs, et aucune adresse d'article ouvert
n'est relevée depuis l'exposé.

**Aucune page n'a été lue en image.** Les 23 articles qui portent un tableau
gardent leurs lignes brutes, avec leur mise en page et leur page, dans un champ
distinct des alinéas — et le socle le déclare.

**L'extracteur est déterministe, et son empreinte tient à trois choses** :
l'empreinte de la pièce, la commande `pdftotext` figée, la version de poppler.
Les trois sont au JSON. Rejeu vérifié identique à l'octet.

**386 adresses ouvertes par le texte déposé**, sur 48 textes — 126 au code
général des impôts, 81 au code des impositions sur les biens et services, 54 au
code général des collectivités territoriales. C'est ce qui alimente la colonne
`variante` de `REF_norme`, et c'est la moitié du travail de la skill
`vecteur-mesure` que le fil des skills attendait.

**Ouvert veut dire modifié, jamais cité** : sur 552 références relevées à la
disposition, 406 seulement modifient. Trois règles mécaniques les séparent — la
coupe à la formule modificative, le masquage des guillemets, et le chapeau sans
verbe, qui vaut 77 fois dans la pièce.

**24 des 82 articles n'ouvrent aucune adresse.** Ce sont exactement les articles
de crédits, d'équilibre, de plafonds et de garanties — le lot qu'A-243 range en
`non codifié`, et qui n'a pas besoin de vecteur.

**Le dispositif a mordu contre nous, comme il faut.** La grammaire du numéro de
`REF_norme` **tronque 34 adresses sur 386** : les ordinaux ne sont pas rangés du
plus long au plus court, et le suffixe est borné à une lettre de A à H.
« 199 terdecies-0 A » devient « 199 ter », « 235 ter ZD » devient « 235 ter »,
« 223 VU » devient « 223 » — trois articles qui existent, et qui ne sont pas les
bons. Le fil ne corrige pas `vecteurs.py`, qui appartient au fil des vecteurs :
il porte deux colonnes et compte l'écart. **La même grammaire a servi aux 465
dépenses fiscales, et ce qu'elle y tronque n'est pas mesuré.**

**Dix contrôles, zéro échec.** 8 790 lignes sur 8 790 retrouvées littéralement
dans la pièce ; 82 articles sur 82 retrouvés dans l'ordre à l'intérieur de leurs
pages ; **le sommaire de la pièce confronté au corps, 82 sur 82, zéro écart de
titre et zéro écart de page** ; 552 références sur 552 retrouvées dans leur
alinéa ; zéro code affirmé hors de la liste fermée, six indéterminés déclarés et
aucun sur une référence modificative ; rejeu déterministe.

**Reste ouvert** : le PLFSS, qui attend son tour (A-223) ; la colonne `variante`
elle-même, qui demande de régénérer `REF_norme` depuis le socle budgétaire ; et
la troncature de la grammaire sur les dépenses fiscales, à mesurer avant qu'un
amendement se rédige sur l'une d'elles.

## 20260901 — L'éval des vecteurs, et la première skill de la chaîne

**`vecteur-mesure` est écrite, éprouvée, corrigée et enregistrée.** C'est la
première des trois skills de la chaîne de l'amendement, et la seule qui soit
mesurée.

**Les liasses du contre-budget 2026 de Génération Libre sont entrées par pièce
jointe** — parties I et II du PLF, la liasse PLFSS restant à joindre.
L'extraction rend **36 couples dispositif / exposé sommaire pour 31 numéros
d'amendement**, zéro dispositif vide, zéro exposé vide. Les 8 amendements qui
manquent aux 39 sont à la liasse PLFSS.

**L'éval s'est jouée en aveugle**, sur l'exposé sommaire seul, le dispositif
scellé sur disque et jamais affiché : **14 concordances sur 22, 63,6 %, zéro
discordance.** En mode socle non disponible, donc un plancher.

**Le premier tour donnait 36 %, et c'était la clé de vérité-terrain qui était
fausse** : elle relevait la ligne de rattachement comme une adresse, et coupait
le suffixe en lettre des numéros d'article. Deux rechutes, corrigées, et
personne ne les aurait vues à l'œil.

**Trois enseignements ont été portés à la skill.** Le statut de la dépense —
sociale, locale, opérateur — décide de la famille de siège et se qualifie avant
toute recherche. La variante commande le type d'adresse : sur un article ouvert,
le dispositif porte sur les alinéas du texte déposé et non sur un code. Et un
état neuf, `siege_non_codifie`, pour une mesure qui crée une règle sans modifier
d'article.

**Le gabarit de l'exposé sommaire est enrichi du grain du document GL**, dont le
docx sort du coffre : l'auteur en a copie. La mesure qui commande la conception
de `expose-sommaire` : GL ne tient sa propre règle de longueur que dans 19
exposés sur 36, quand son exemple de référence la tient. Le gabarit cale sur le
gold standard, jamais sur la pratique.

**Périmètre déplié et prouvé** : R1 à zéro divergence, 63 artefacts au dépôt
conformes à l'octet.

**Ce qui reste ouvert** : le rejeu par un fil vierge, sur les 22 cas puis sur les
8 du PLFSS ; les deux skills aval, `disposition-cible` et `expose-sommaire` ; et
l'extracteur de tableau pour la clé des cas de crédits.

## 20260831 — L'adresse devient précise, et un faux de 55 entrées est corrigé

**Deux remarques de l'auteur sur l'état des vecteurs, et la première a sorti un
faux.**

### Le code n'était pas dit, et il était faux sur 55 dépenses fiscales

`ref_norme.py` posait « code général des impôts » sur les 465, avec une note qui
avouait le procédé. **C'était une affirmation, pas une déduction.** Vérifié sur
pièce : les articles `L. 312-xx` et `L. 421-xx` sont au **code des impositions
sur les biens et services** — accises sur les énergies, taxes sur les véhicules
— et `L. 2333-55-3` au code général des collectivités territoriales. Un
amendement rédigé sur cette base aurait visé un article du CGI qui n'existe pas.

C'est exactement ce qu'A-245 interdit, et je l'avais écrit le matin même.

**Le code se déduit désormais par une table de règles**, chacune avec son motif,
son identifiant Légifrance, son siège, sa date de vérification et la requête qui
l'a établie ; chaque vecteur déclare la règle qui l'a produit. Après correction :
617 CGI, 94 code des impositions sur les biens et services, 8 textes non
codifiés où la loi de finances est elle-même le vecteur, 1 code général des
collectivités territoriales, **4 indéterminés** — des renvois à la doctrine
administrative, et un vrai résultat. **`N9` refuse un code posé sans règle**
(A-250).

### L'adresse se décompose du macro au micro

Quatre niveaux, quatre colonnes : **code · siège · article · subdivision**.
`158-5-a` n'est pas une adresse, c'est trois niveaux collés — et une disposition
modificative ne vise pas le même objet selon qu'on abroge l'article, le 5 ou
le a.

**Aucune épissure de chaîne** : la version d'avant recollait un fragment
orphelin sur un radical tronqué et fabriquait `L. al.3` à partir de
`L. 312-35, al.3`. Trois corrections de découpage, chacune un faux possible : la
lettre de partie bornée à L, R, D — `A 2°` est une subdivision, pas un article
de partie A ; un nombre nu suivi du signe ordinal est une subdivision ; et le
numéro admet un suffixe après l'ordinal, faute de quoi `278 sexies-0 A` se
coupait en deux.

`278 sexies – II. A 1°, A 2°, B 1° et B 2°, III, 278 sexies-0 A et 278 sexies A
– I 1°, 2°, 3° a, 4°, 5°, 6° et II` se décompose maintenant en **treize adresses
justes**. `N2` sort zéro référence de forme non reconnue (A-251).

### La table est plate et s'exporte

`livrables/etat_vecteurs.csv` — **880 lignes, seize colonnes atomiques**, rien
d'imbriqué et rien de collé. La page HTML rend la même table ; les deux sortent
de la même fonction et ne peuvent pas diverger (A-252).

**La colonne `variante` existe dès maintenant** — « dans l'absolu » contre
« article ouvert par le texte déposé ». Elle vaut `à déterminer` partout, et
c'est honnête : sans le socle du texte on ne sait pas lesquels sont ouverts. Ce
qui compte est qu'elle soit là et qu'elle se compte plutôt que d'être ajoutée
après coup sur 1 856 entrées (A-253).

*Source partielle et gratuite, relevée par l'auteur* : les liasses de Génération
Libre appellent elles-mêmes des articles du PLF 2026. Elles portent donc, en
creux, **une première liste d'articles ouverts** — avant le fil 2, pour le coût
d'une lecture.

### Ce que N6 voit maintenant, et qui change de sens

La collision se juge sur l'adresse complète, code compris, et la subdivision est
portée au détail : deux dépenses fiscales qui dérogent au même article par deux
subdivisions différentes ne se neutralisent pas.

**82 adresses visées par plus d'une mesure, dont 30 en entier par plusieurs.**
Le cas le plus net : **`L. 312-48` du code des impositions sur les biens et
services porte onze dépenses fiscales.** Un seul amendement les supprimerait
toutes d'un coup — efficace ou piège selon l'intention, et cela ne se voit nulle
part ailleurs qu'ici.

### Deux précisions de méthode

**L'éval du vecteur et celle de la rédaction ne se jugent pas pareil** (A-254).
L'article est l'article : correspondance dure, taux de rappel. Une disposition,
non — deux rédacteurs écrivent deux textes différents qui produisent le même
effet de droit. Ce qui se compare est la correspondance : même article, même
opération, même portée. **La rédaction de GL est un modèle dont on s'inspire,
pas un corrigé**, et cela reste un travail juridique lourd que la skill outille
sans l'automatiser.

**Et aucune skill n'est écrite** (A-255). Ce qui existe est ce qu'une skill
envelopperait : la procédure, l'appareil, le référentiel, et un lot pilote de
onze cibles. C'est la matière, pas l'outil.

## 20260831 — L'état des vecteurs s'ouvre, et la chaîne de l'amendement est spécifiée

**Clôture du fil. Une page, trois arbitrages, un passage de témoin.**

### L'état des vecteurs se lit sans ouvrir un JSON

`livrables/etat_vecteurs.html` — la couverture par lot, les onze cibles
relevées avec leur identifiant Légifrance cliquable et leur date, les 31
dépenses fiscales dont l'annexe ne donne pas d'adresse exploitable, les 55
articles visés par plus d'une mesure, et les quatre étapes restantes. **Aucun
texte de loi : uniquement des adresses**, ce qui est la règle du vecteur.

Elle est au coffre — l'auteur l'ouvre, donc elle y va (A-16) — et elle se
régénère par `make`. Une correction se porte à `vecteurs.py` ou à l'annexe.

### La chaîne de l'amendement : trois skills, et je m'étais trompé de découpage

**L'auteur tranche contre ma proposition, et il a raison.** J'avais recommandé
deux skills neuves plus la reprise de `redaction-legistique` pour le
dispositif. **Je sous-estimais la différence entre une proposition de loi et un
amendement** — ce ne sont ni le même objet, ni la même longueur, ni la même
contrainte de recevabilité.

Trois skills, chacune s'arrêtant à un produit qui se contrôle seul :
`vecteur-mesure` rend les adresses, `disposition-cible` rend le dispositif en
style SGG, `expose-sommaire` rend les 200 à 300 mots.
`redaction-legistique` garde son objet, le texte déposable complet (A-247).

**Ce que la séparation achète** : chaque étape s'exporte et s'éprouve seule. Une
chaîne d'un seul tenant ne se mesure pas, et l'éval exige d'isoler la première
étape.

**Deux contraintes portées à l'écriture.** `vecteur-mesure` joint au socle avant
de chercher, et **chaque recherche neuve enrichit `vecteurs.py`** : la skill
capitalise. Et **la version exportable ne lit pas `vecteurs.py`** — nos régimes
de suppression sont la doctrine sous forme de tableau, qu'A-232 exclut du pack.

### Le contre-budget GL, et l'éval qu'il rend possible

39 mesures, **trois liasses PDF** — rien sur la page, qui est un portail.
**Elles entrent par pièce jointe** (A-248). Elles apportent le gabarit réel du
dispositif et de l'exposé sommaire, l'ordre de grandeur des baisses de crédits,
et la vérité-terrain de l'éval.

**L'éval se joue sur les exposés des motifs seuls** (A-249) : on donne à
`vecteur-mesure` l'exposé qui décrit la mesure sans nommer l'article, et on
compare à l'article que le dispositif cite. Trois verdicts — concordance,
voisinage, discordance — et **un taux de rappel sur 39 cas**. C'est A-95
transposé : un dispositif qui ne sait pas se mesurer est un dispositif qu'on
croit sur parole.

**Deux gardes.** L'extraction sépare dispositif et exposé **avant** de rien
montrer, sinon l'éval se donne la réponse. Et elle se joue **avant** que les
cibles GL entrent à `vecteurs.py`.

### L'appareil à la clôture

`make coffre` plie 56 pièces ; le dépliage rejoué les redonne **identiques à
l'octet**, 56 sur 56. `make restauration` : `R1`, `R3`, `R5` à zéro. `make
index` : `I2` à `I5` à zéro, les 14 de `I1` étant des dérivés dont les sources
sont hors du périmètre déplié. Le contrôle de `REF_norme` : `N1`, `N3`, `N4`,
`N5` à zéro échec, `N4` rejouant 465 dérivations sans divergence.

**Reste ouvert** : les trois liasses GL à verser ; le PDF du PLF, qui commande
le fil 2 et la moitié de `vecteur-mesure` ; combien d'abrogations pour 424
organismes ; et, sur les collocs, le choix entre couper la ressource et couper
la compétence.

## 20260831 — `REF_norme` existe, et la procédure des vecteurs est éprouvée

**Deux corrections de l'auteur, et un dispositif monté et joué dans la foulée.**

### Les crédits sont des mesures de plein exercice

A-241 rangeait les 128 programmes en « aucun vecteur ». La formule était juste
techniquement et **fausse de portée** : elle laissait entendre qu'une mesure de
crédits serait de rang inférieur parce qu'elle ne touche pas d'article de code.
Elle est de rang législatif — l'état B est voté, les crédits qu'il ouvre sont
limitatifs — et **c'est le lot le plus simple et le plus mordant, pas le moins
sérieux**. Le vecteur devient `non codifié`, pas `aucun`, et `REF_norme` le
porte en `trouvé` pour les 128 (A-243).

**Et notre chiffrage n'est pas une condition de la mesure** (A-244). Il est fait
sur le PLF 2026 ; le texte qu'on amendera portera d'autres chiffres. Une mesure
se paramètre donc sur **la ligne** — mission, programme, catégorie — et sur **la
règle de baisse**, jamais sur un montant en dur. L'écart avec le PLF de l'année
ne bloque rien ; il se relève. Le financement, lui, boucle et ne bouge pas.

### La procédure des vecteurs, et ce qu'elle a coûté à l'épreuve

`methode/procedure_vecteurs.md` (A-245). **Le vecteur est un identifiant, jamais
du verbatim** — c'est ce qui rend la recherche légitime : A-234 dit que l'outil
de récupération repère et ne copie pas. Le texte de l'article entrera par pièce
jointe le jour où le trois colonnes le demandera.

**Vérifié, et cela borne l'appareil** : le shell de l'atelier n'atteint ni
Légifrance ni un moteur de recherche. **Un script ne trouvera jamais un
vecteur** ; il dérive, il joint, il contrôle.

Quatre provenances sur le dispositif de `REF_chiffres` — `annexe`,
`legifrance`, `corpus`, `a_trouver`. Cinq rôles, parce qu'**un organisme a
souvent deux vecteurs et que l'économie porte sur le second** : les agences de
l'eau sont créées par une section du code de l'environnement et financées par
une autre.

**Coût mesuré, non estimé** : onze cibles, onze recherches, onze réponses au
premier essai, dix-huit vecteurs. Le titre de section de Légifrance nomme
lui-même la cible — « Section 3 : France compétences », « Chapitre V :
Impositions affectées au Centre national du cinéma et de l'image animée et
perçues par lui » — et quand il la nomme, la fourchette d'articles qui suit est
le vecteur, sans interprétation.

### `REF_norme` est construit et contrôlé

**1 856 entrées, 621 vecteurs déclarés.** Les 465 dépenses fiscales et les 128
programmes sont couverts à 100 %. Les onze organismes relevés couvrent **les
onze lignes d'économie d'opérateur qui nomment une cible, 22,7 Md€** — la
douzième est le résidu « autres », qui n'a pas d'assiette nommée et ne peut donc
pas avoir de vecteur.

**Huit contrôles**, `N1` à `N8`. `N4` est le seul total : il rejoue la
dérivation depuis l'annexe et compare, 465 sur 465 sans divergence. `N1` est
celui qu'A-227 demande — il refuse qu'un vecteur codifié nomme un véhicule.

**Le dispositif a mordu dès la première exécution, et deux fois contre
moi** (A-246). La jointure a refusé deux clés que j'avais recopiées d'un
arbitrage au lieu du socle — A-94 tient, et sans elle deux vecteurs justes
auraient été rattachés à rien. Et `N2` a trouvé que mon découpage fragmentait
« art. 199 undecies B, C, D » en un article et deux lettres orphelines.

**Ce qui reste après correction est un vrai résultat** : **31 dépenses fiscales
sur 465 portent à l'annexe autre chose qu'une adresse d'article** — renvoi à la
doctrine administrative, mention d'alinéa, texte libre — dont **20 avec un
régime de suppression, pour 4,25 Md€**. Le lot des niches est donc à 100 % de
références et **93 % d'adresses exploitables** ; c'est la seconde grandeur qui
compte.

**Et `N6` a sorti ce qu'aucune lecture par mesure n'aurait montré** : **55
articles du code général des impôts sont visés par plus d'une dépense
fiscale**. Deux amendements qui abrogeraient le même article se neutralisent.

### Le plan par étapes

Étape 0 close. **Étape 1** : les 20 dépenses fiscales dont la référence n'est
pas exploitable, 4,25 Md€ — vingt recherches, et le lot passe à 100 %. **Étape
2** : les 87 taxes du régime `Oui` et `Flux OM`, le compte de recherches étant
très inférieur au compte de taxes puisqu'une section couvre souvent plusieurs
taxes. **Étape 3** : les organismes, **par montant et non par ordre
alphabétique**, en lots de 25 à 30, soit une dizaine de fils. **Étape 4** : les
44 propositions arrêtées, les 12 esquissées attendant leur norme cible.

**Reste ouvert** : combien d'abrogations on dépose pour 424 organismes ; le
contre-budget 2026 de Génération Libre, à verser et à mobiliser ; la révision du
code général des impôts, dont la question change puisque les vecteurs des niches
sont connus ; et, quand un organisme porte les deux, abroger la loi fondatrice
ou les articles du code.

## 20260831 — Les collocs rentrent par la ressource, et le vecteur cesse d'être une estimation

**Deux reprises, sur la même session, l'une sur reproche de l'auteur et l'autre
sur mesure.**

### La ventilation par véhicule était fausse sur les collocs

**Reproche de l'auteur, et il est fondé.** La ventilation du matin rangeait les
39,5 Md€ du périmètre local en « hors véhicule financier de l'État ». C'était
juste sur la dépense et faux sur le levier : beaucoup de la dépense locale
intersecte le budgétaire et le fiscal d'État par le millefeuille, les
cofinancements et le cadrage.

**L'erreur de raisonnement se nomme** : j'ai cherché le véhicule de la dépense
au lieu de chercher le véhicule de ce qui la produit — c'est-à-dire que je n'ai
pas appliqué à ma propre ventilation le test de rattachement par l'implicite
budgétaire que j'avais écrit deux heures plus tôt.

**Le fait qui emporte la correction était sous les yeux, deux fois.** L'auteur a
lui-même classé **86 taxes affectées en régime `Collocs`**, pour **58,25 Md€**,
dans le classeur de calculs. Et le 3° bis du I de l'article 34, relevé en
verbatim le matin même, vise « les impositions de toutes natures affectées à une
personne morale autre que l'État » — les collectivités en sont. J'avais lu
l'exclusion du 5° bis, qui ne porte que sur la **reprise du produit par
l'État**, comme si elle fermait tout le domaine.

**Huit leviers d'État sont relevés, chiffrés au socle, et six ont une porte au
domaine** : la fiscalité affectée aux collocs (58,25 Md€), les niches sur impôts
locaux (1,44 Md€, **article de code renseigné pour 42 sur 42**), les
dégrèvements d'impôts locaux (4,62 Md€, dépense d'État en totalité), les
concours budgétaires (5,74 Md€), les transferts au budget général (11,09 Md€),
et les prélèvements sur recettes — premier levier en montant, dont **la porte
est établie et le montant absent du corpus**, l'annexe n'y étant pas.

Deux ne l'ont pas : **la norme**, qui est le seul levier atteignant la dépense
elle-même et qui est en loi ordinaire ; et **le cadrage**, dont la porte est
perdue avec l'abrogation de la loi de programmation et non retrouvée.

**Ce que la correction ne change pas, et qui doit se dire dans l'exposé
sommaire** : réduire la ressource ne commande pas l'emploi. La colloc arbitre,
et elle peut arbitrer contre nous.

**Sept points tangents sont signalés à part**, sur demande de l'auteur, sans
être qualifiés. Le plus dangereux est celui des exonérations compensées par
l'État : supprimer la niche sans la compensation ne rend rien à l'État,
supprimer la compensation sans la niche transfère la charge à la commune — et
le chiffrage doit dire lequel des deux il compte.

### Le chantier des vecteurs est mesuré, et il n'est pas où on le croyait

A-227 posait que le vecteur est le gros du travail. **Il l'est, et le compter
déplace entièrement le problème.**

L'intuition disait 56 propositions, donc 56 vecteurs. C'est faux dans les deux
sens : une proposition peut toucher des centaines d'articles ou aucun. **Le
vecteur se compte en articles touchés, et la distribution est très inégale.**

| lot | population | volume | vecteur connu |
|---|---|---|---|
| V1 | programmes du budget général | 128 | *aucun vecteur* |
| V2 | dépenses fiscales à supprimer | 383 | **100 %** |
| V3 | taxes affectées portant un régime | 232 | 20 % |
| V4 | organismes à supprimer, internaliser ou vendre | 424 | **0 %** |
| V5 | propositions du REF_doctrine | 56 | norme cible d'abord |

**Trois faits que l'estimation ne donnait pas.** Une mesure de crédits n'a
**aucun vecteur** — elle se dépose en amendement sur l'état B, et le lot qui
porte le plus de montant est celui qui coûte le moins en légistique. **Le
vecteur des niches est déjà écrit à 100 %** : l'annexe porte, pour chacune des
465, l'article du code et la norme de référence à laquelle elle déroge — ce lot
ne se cherche pas, il se convertit par script. Et **le chantier réel est de 608
vecteurs à trouver, dont 424 organismes**, soit 69 % dans une seule population
qu'aucune de nos pièces ne documente.

*Conséquence d'appareil* : `REF_norme` porte **quatre** valeurs d'état du
vecteur et non trois — la quatrième, `sans objet`, pour les mesures de crédits,
sans quoi les 128 programmes sortiraient en manque à chaque contrôle.

*Conséquence sur la révision du code général des impôts* : la question qu'on lui
pose change. Les vecteurs des niches sont connus ; elle est précieuse ailleurs,
sur les articles que la fiscalité à quatre impôts réécrit et qui ne sont pas des
dépenses fiscales.

**Et le récapitulatif de transposabilité fait déjà ce travail — sur un axe.** 59
mesures du seul axe du consentement à l'impôt, 44 compatibles à Constitution
inchangée, 7 incompatibles, 8 sans objet. Son tableau VII est exactement le
format cible de `REF_norme` vu par vecteur. **Ce qui s'en reprend et que
`REF_norme` ne prévoit pas : la notion de repli avec son écart déclaré.** Un
vecteur inexistant appelle un repli, pas un abandon.

### L'appareil

Le socle est rejoué entier — cinq classeurs reconvertis, **32 bouclages sur
32**, zéro échec au contrôle du socle. `positions.json` régénéré revient
**identique à l'octet** à ce que le coffre porte. `make index` sort zéro
anomalie sur I2 à I5 ; les 14 de I1 sont des dérivés dont les sources sont hors
du périmètre déplié.

**Reste ouvert** : le montant des prélèvements sur recettes, premier levier et
seule grandeur manquante ; le choix entre couper la ressource et couper la
compétence, qui est de doctrine et non de technique ; le sort des exonérations
compensées ; la porte du cadrage ; et, sur les vecteurs, **combien d'abrogations
on dépose pour 424 organismes** — trois voies, qui ne coûtent pas la même chose
et qui ne se déduisent d'aucune donnée.

## 20260831 — Le contre-PLF s'ouvre : les portes relevées, l'axe de transparence vide

**Premier fil de production du contre-PLF.** Il ne demandait rien à l'auteur, et
il rend cinq choses.

**Les treize arbitrages du fil de conversation sont au registre**, A-223 à
A-235, portés **par script** : le bloc neuf est inséré après la préface, et les
196 533 octets d'avant sont recollés sans jamais repasser par le modèle. Preuve
mécanique et non à l'œil — le registre privé du bloc redonne le SHA-256 que le
coffre porte, `a1b7ede2…`, à l'octet, à la ligne près.

**La grille des portes est relevée en verbatim, et elle apprend quatre choses.**
Vingt-huit portes sur la loi organique relative aux lois de finances, zéro échec
de relevé, et un contrôle indépendant qui retrouve les vingt-huit citations
littéralement à la pièce. Le module ne porte que des repères : une phrase de loi
ne s'y écrit jamais, et un repère qui ne se retrouve pas arrête la génération —
c'est A-91 appliqué aux portes.

Ce que le relevé donne et qu'aucune lecture de mémoire n'aurait donné.
**Trois portes nomment les opérateurs**, de trois rangs et en deux parties
différentes : les taxes affectées au 3° bis du I, facultatif ; la reprise du
produit au 5° bis du I, obligatoire ; les plafonds d'emplois au 3° du II,
obligatoire. **Le 5° bis exclut nommément les collectivités, leurs
établissements et les organismes de sécurité sociale** — c'est la borne qui
décide, taxe par taxe, si la porte est ouverte ou s'il faut plaider. **La
condition de lien de l'article 2-II est une prise qui ne demande aucune
plaidoirie** : une imposition ne reste affectée que si elle est en lien avec les
missions de service public confiées. Et **le 8° du II est la seule porte du II
qui écrit sa propre réserve de lien direct** ; les autres n'en portent pas, ce
qui ne veut pas dire qu'elles en sont dispensées.

Sept portes se déclarent non relevables sur cette pièce, qui abrège certains
articles — dont les articles 35 à 37, et le domaine de la loi de financement de
la sécurité sociale, qui n'est pas dans la loi organique relative aux lois de
finances et se relèvera sur sa propre pièce.

**Le test de rattachement est écrit**, `methode/test_rattachement.md` : quatre
canaux d'effet budgétaire à parcourir tous les quatre, trois qualifications dont
une seule est forte, quatre contrefactuels à interroger, la partie, et quatre
verdicts dont un seul est un feu vert sans réserve. **L'argument le plus fort du
test est écrit dans le texte** et il n'avait jamais été nommé : l'article 33
oblige la loi de finances à évaluer et autoriser les conséquences de ce qui se
décide ailleurs. Une mesure dont l'adoption force la loi de finances à réagir a
avec elle un lien qui ne s'invente pas — et l'invoquer, c'est admettre qu'elle
pourrait être adoptée ailleurs.

**L'axe de transparence existe comme intention et n'existe pas comme doctrine.**
C'est le résultat le plus lourd du fil. Le levier `D1-1` porte le nom exact que
A-226 lui donne — « droit de savoir : transparence et audit » — et une
proposition, `D1-1-1`, « État en audit permanent ». Elle est déclarée
*esquissée*, et le relevé mécanique de ses dix champs en sort **huit vides** :
ni paramètre, ni effet, ni sous-item, ni source, ni droit existant, ni périmètre.
Sa seule matière est un renvoi à deux membres `M-nnnn`, dont la couche de preuve
est au bloc `manquants` de l'index depuis des semaines.

**Et son périmètre n'est pas celui d'A-226.** Le balayage littéral du
référentiel entier sort 49 occurrences du vocabulaire des opérateurs, 35 de
celui des associations, 21 de celui des caisses — et **zéro à l'intérieur de
`D1-1`**. Elles vivent toutes ailleurs, à la fermeture des structures, à
l'extinction des subventions, aux assurances sociales, où ces populations sont
des **objets de suppression, non des débiteurs d'information**. Ce n'est pas le
même geste.

Conséquence directe, et le fil l'inscrit sans la trancher : A-226 réserve la
porte du 7° du II à un axe dont le corpus ne porte que le titre. Tant qu'il
n'est pas écrit — débiteur, assiette, support, périodicité, sanction — cette
porte n'a rien à faire passer, et un amendement qui l'emprunterait retomberait
dans la demande de rapport qu'A-226 écarte précisément. *Deux issues, et deux
seulement : l'axe se dote d'un contenu, ou A-226 se corrige.*

**La ventilation des 41 lignes d'économie sort un fait qui n'était pas
attendu.** Vingt-trois lignes et 50,5 Md€ relèvent du projet de loi de finances ;
huit lignes et 27,4 Md€ appellent un partage entre les deux textes, dont quatre
sont des résidus « autres » que le classeur ne détaille pas ; **39,5 Md€
n'entrent dans aucun des deux textes** — le périmètre des collectivités locales
entier, qu'une loi de finances ne vote pas et où l'État n'agit que par le
prélèvement sur recettes ou par la norme.

**Et aucune ligne ne relève du PLFSS.** Les 41 lignes sont le bras « dépenses
d'État et dépenses locales » du chiffrage ; le chômage, les retraites et la santé
vivent ailleurs et ne sont pas tracés. **La phase PLFSS ne se prépare donc pas
depuis `economies.json`** : il lui faudra sa propre couche tracée, sur les mêmes
règles. La seule ligne lourde et vraiment mixte est celle des aides à l'emploi et
à l'apprentissage, 6,9 Md€ — crédits d'un côté, exonérations de cotisations de
l'autre.

**Un écart de 0,2 Md€ sort du contrôle de recomposition et il n'est pas
absorbé.** Il est dans l'arbre du classeur lui-même, entre la tête du périmètre
État et la somme de ses six rubriques, et six arrondis d'affichage au dixième le
bornent à trois dixièmes. Il reste écrit au livrable, et la ventilation somme les
lignes, jamais la tête.

**La couche des chiffres est rejouée entière et elle tient.** Les cinq classeurs
sont reconvertis, le socle refait — 465 dépenses fiscales, 278 taxes affectées,
180 lignes d'opérateur, 749 ODAC-ODAL, 2 351 lignes de PAP, 128 programmes — et
le traçage sort **32 bouclages sur 32**, zéro échec au contrôle du socle.

**Ce que la restauration a donné.** Périmètre borné et annoncé avant : l'archive
technique, les deux pièces LOLF, le registre, l'index, les empreintes, la
procédure et le journal. `make restauration` sort **`R1` à zéro divergence** sur
52 artefacts présents et 93 empreintes ; `R3`, `R4` et `R5` à zéro. L'archive
elle-même concorde à l'octet, `5193beba…`. Les 41 pièces que `R2` compte sont
celles que le fil n'a pas demandées, et les 14 anomalies `I1` sont des dérivés
dont les sources — le manuscrit, les protos — sont hors périmètre.

**Reste ouvert, et le fil s'y arrête.** Le contenu de l'axe de transparence, ou
la correction d'A-226. Le partage des huit lignes mixtes entre les deux textes,
dont quatre supposent d'ouvrir le classeur sur ses résidus. La référence du
contrefactuel — droit constant ou évolution tendancielle —, qu'A-225 pose
expressément comme à instruire. Le choix, pour la transparence, entre le rapport
du 7° du II et l'annexe de l'article 51 : les deux portes sont ouvertes, la
seconde est opposable.

## 20260828 — Le site est en ligne

**Publié depuis l'atelier**, sans Vercel et sans geste de l'auteur :
`site/resolution_une_page.html`, la même matière et le même rendu en un fichier,
avec **une adresse par fiche** en fragment (A-199). Routage vérifié : sans
fragment le sommaire, sur `#retraite` la fiche du retraité et elle seule ; sans
JavaScript, tout se lit à la suite.

**Les deux formes sortent du même générateur** et ne peuvent pas diverger.
`site/` reste la cible — vraies adresses, domaine propre — et attend que le
dépôt de publication soit autorisé pour la session.

**Le dépôt porte désormais sa configuration** : `make publier` pose un
`vercel.json` à la racine, qui désigne `site/` et interdit toute construction.
Plus aucun champ à remplir sur Vercel (A-198) — le réglage *Root Directory* ne
s'édite de toute façon pas avant que le dossier existe au dépôt, ce qui rendait
la consigne précédente inexécutable.

---

## 20260828 — Le site existe, et il attend un réseau

**Le squelette est arbitré** : l'index et les dix-huit, une fiche par adresse
(A-195). L'auteur a tranché contre le mur d'une page.

**`appareil/generer_site.py` est réécrit** et sort `site/` — 21 fichiers,
68 719 o, 18 fiches à leur adresse, zéro fuite de nomenclature interne. Il
importe le rendu de fiche de `generer_fiches.py` au lieu de le redessiner :
l'entrée liste les dix-huit axes, chaque page porte sa carte, sa voisine
précédente, sa suivante, et les autres fiches de son groupe. Ni manifeste, ni
note, ni vidéo : le site ne porte que ce qui existe.

**La chaîne suit.** `Makefile` : la règle du site lit le référentiel des
positions et la structure, plus l'interface de travail ; `make propre` efface le
dossier. L'index déclare le site à `site/index.html`, et
`livrables/site_prototype.html` résout sur lui par alias.

**La mise en ligne ne se fait pas d'ici.** L'atelier sort par un proxy à liste
blanche qui n'admet que les registres de paquets : Vercel est injoignable, le
CLI échoue au premier appel. La voie du jeton tombe ; le dépôt Git devient la
voie durable, `github.com` étant joignable en git (A-196).

**Reste ouvert** : la ligne de copie de l'entrée, à valider ; le périmètre
public ; les onze catégories de rente pure hors galerie ; « jusqu'à sept ans »
ou « sept ans » (A-140) ; la charte graphique.

---

## 20260828 — Le fil du site s'ouvre, et la galerie se prouve d'elle-même

**Le périmètre du fil est déplié et rien de plus.** L'archive technique, les
documents de `methode/`, `CLAUDE.md`, la galerie et la carte du projet. Le
manuscrit, le socle budgétaire, les sources et les archives restent au coffre :
la galerie porte ses chiffres, et aucun classeur n'est converti. `make
restauration` sort **`R1` à zéro divergence** sur 65 artefacts présents et 91
empreintes de référence ; `R3`, `R4` et `R5` à zéro. Les 26 pièces que `R2`
compte sont celles que le fil n'a pas demandées.

**La galerie se prouve de l'extérieur, et c'est plus fort qu'une empreinte.**
Elle n'en portait pas — l'index la déclarait hors coffre (A-191). Rejouée par
`generer_fiches.py` depuis le référentiel des positions, elle revient
**identique à l'octet** : 35 546 o, 18 fiches.

**Ce que le fil courant ne savait pas : la galerie est complète.** 83 gains
d'attache sur 83 portent leur apport, 20 pertes retenues sur 20 portent leur
libellé. La surface publiable des dix-huit fiches est entière, et le « seize
gains » que le fil courant annonçait est un état périmé de plusieurs passes
(A-194).

**Le générateur du prototype de site ne se reprend pas.** Il intègre l'interface
de travail au lieu de la galerie, porte une autre typographie que l'esthétique
arrêtée, sort une page unique là où A-190 demande un dossier `site/`, et déclare
des sections vides que A-59 interdit. Il est remplacé ; ce qui se reprend est la
factorisation par fiche de `generer_fiches.py`, que le site importera (A-192).

**Reste ouvert, et le fil s'y arrête** : le squelette du site — pages, entrée,
navigation entre dix-huit fiches. Deux structures sont portées à l'auteur
(A-193). Avec elles, ce qui l'attendait déjà : les onze catégories de rente pure
hors galerie, « jusqu'à sept ans » ou « sept ans » (A-140), et la charte
graphique, fil dédié après le site.

---

## 20260828 — La galerie passe les corrections de fond, et une fiche mince se lit

**La galerie sort du bac à sable.** Elle était déclarée comme prototype :
`proto_fiches.py`, `proto_fiche.html`, famille « bac à sable », régénérée à la
main hors du `Makefile`. Elle devient un output. `appareil/generer_fiches.py`
écrit `livrables/galerie_fiches.html`, famille **graphique**, avec sa règle
`make` et celle de la carte d'attribution ; les anciens noms résolvent par
alias. `make index` sort 0 anomalie sur I2 à I5.

**Les procédures suivent.** `methode/procedure_controle.md` porte la table des
huit contrôles d'apport `A1`–`A8`, avec le rang de chacun — trois échecs, cinq
signalements. `CLAUDE.md` porte la chaîne propre de la galerie, la vedette au
rang de champ rédigé, la règle d'attache et de rappel, et perd la lacune sur le
recouvrement `C-01`/`C-02`/`C-03`, tranché de fait, au profit de la vraie : les
onze catégories de rente pure hors galerie.

**Le fil courant bascule sur le site.**

**Dix-huit fiches, 124 apports rédigés sur 204, zéro échec aux huit contrôles.**
La galerie de présentation générale tient : elle balaie les grands persona, elle
adresse en propre les catégories de perdants, et chaque gain majeur a une
catégorie d'attache et une seule.

**Les corrections de fond de l'auteur sont passées à la source** (A-189). Trois
d'entre elles touchaient le référentiel et non le rendu : la dette par foyer
sort des pertes — c'était une image —, l'APL se maintient jusqu'au terme des
baux en cours, et l'indemnisation se dit du point de vue de la personne, « au-
delà de six mois », non en moyenne. Le reste est de la rédaction : la vérité des
prix contre le mot « inflation », les policiers renforcés et non plus nombreux,
les 300 € de frais de gestion rendus au patient, le seuil rendu au foyer, le
libre emploi de son argent rendu au bénéficiaire d'un chèque.

**Une fiche mince ne relègue plus sa matière en pied** (A-188). Le rappel nu
suppose une fiche qui tient debout ; sous trois gains d'attache elle ne tient
pas, et la bande verte se vidait — l'entreprise subventionnée ne montrait rien
de ce qu'elle gagne. Les rappels dotés d'un apport écrit pour la catégorie
remontent désormais en ligne pleine. L'attache reste unique et le rappel nu
reste la règle partout ailleurs : A-178 n'est pas révoquée.

**Ce qui reste ouvert** : les onze catégories de rente pure, hors galerie, et la
fiche « ce qui s'arrête » qui les porterait. A-141 sur le recouvrement
contribuable-citoyen-foyer est tranché de fait — trois persona distincts, trois
axes distincts — sans être écrit comme tel.

---

## 20260828 — Le format des gagnants-perdants s'éprouve sur deux fiches

**Le prototype prévu par A-135 est fait, et il rend trois choses.**

**Quatre apports écrits, et pas un de plus.** `C-30`, l'agent d'une structure
fermée, passe de zéro à quatre apports sur quatre. Avec les douze de `C-04`, le
corpus en porte seize. `make etat` : 16 gains rédigés sur 194.

**Le contrôle qui refuse un apport recopié existe** — `controle_apports.py`,
quatre codes, joué à `make controle`. Il était porté au fil courant comme l'un
des trois actes préalables à l'écriture des cinquante-trois apports du groupe
« Tout le monde » ; il ne reste que deux. Éprouvé à l'envers sur deux faux
apports avant d'être admis.

**Trois traitements de la même matière**, produits par `proto_fiches.py` depuis
le seul référentiel — rien n'y est écrit à la main. La balance, le montant, le
parcours. Chacun dit en tête ce qu'il rend impossible. Le choix revient à
l'auteur ; le PNG et le PDF ne se font qu'après.

**Ce que le prototype a trouvé, et qu'aucune lecture n'aurait donné.** Le côté
perte, réputé complet, n'a pas de libellé court : `justification` fait trente
mots de médiane, `relais` vingt-quatre, et un format visuel en demande six. Sept
apports sur seize seulement portent une quantité en tête. Et trois pertes de
`C-30` se raccrochent au même gain, ce qui imprimait trois fois la même phrase.

**Deux questions de fond partent à l'auteur et arrêtent le fil.** La durée du
plan de départ — plafond ou borne, « jusqu'à sept ans » contre « sept ans », les
apports et les relais divergeant déjà dans la même fiche. Et le recouvrement de
`C-01`, `C-02` et `C-03`, instruit et posé côte à côte, avec ses trois voies.

Le socle budgétaire n'a pas été déplié et les classeurs n'ont pas été convertis :
les 194 gains portent leur grandeur dérivée, le fil n'en avait pas besoin.
`make controle` sort zéro échec sur tous les contrôles joués.

**Deuxième passe, après relecture de l'auteur.** Le parcours est retiré : il
affirmait une absence, et elle était fausse — le travailleur perd des aides
fléchées, et « rien ne change » ne se dit pas (A-142). La grille le remplace.

Trois règles de format en sortent, et elles valent pour la série : les deux côtés
ne se présentent pas pareil, une perte est une carte et un gain une ligne ;
l'ordre suit la catégorie, les moins d'abord pour les perdants spontanés
(A-143) ; une grappe de gains sous un même levier se replie (A-144). Deux
contrôles neufs trouvent ces grappes — A5 par les mots, A6 par l'origine.

Le titre d'affichage de `C-30` est proposé et non validé : « Agent dont le poste
est supprimé » (A-145). Le terme du référentiel n'est pas touché.

**Troisième passe : un seul format, et une faute de fond corrigée.** L'auteur
retient la lecture linéaire ; les trois traitements fusionnent en un, qui porte
la signature Résolution — bloc-marque, filet à trois couleurs, cartouche de pied
(A-149).

**La correction qui compte n'est pas de forme.** Treize gains attribuaient leur
financement à une mesure isolée — l'abattement de 10 % sur les pensions, la
gratuité des études. Presque toute la restitution est payée par l'ensemble des
économies ; seuls le chômage et le patrimoine ont leur source propre. Neuf lignes
sur seize prennent désormais la formule commune, et le format la dit une fois en
pied (A-146). Le corpus portait un contresens attaquable, il ne le porte plus.

**Un troisième champ rédigé naît du côté gain** : la vedette, deux ou trois
signes en tête de ligne, chiffre ou mot — « 600 € », « Le temps » (A-147). Elle
amende le relevé automatique, qui passe en secours. Les seize apports sont
réécrits court : médiane de 16,5 à 12 mots, zéro signalement de registre (A-148).

`C-30` se nomme public — définition, effectif, titre d'affichage — et son gain de
salaire dit d'où il vient : la hausse des salaires nets dans le privé.

**Quatrième passe : la fiche devient un produit.** Elle ne porte plus de mentions
de travail — pied, bloc interne, étiquettes de chantier ont quitté la page
(A-154). Le fond crème cède à un aplat d'encre ; la charte reste un fil dédié, à
ouvrir après le bon à tirer du format.

Trois règles de fond s'ajoutent. **Une modalité n'est pas un gain** : la
restitution par paliers dit comment arrivent les 600 €, elle ne prend pas de
ligne (A-150). **Un capteur ne paraît pas sur la fiche d'une personne** : une
rente supprimée n'est pas une perte portée par quelqu'un (A-151). **« Qui paie »
ne qualifie pas une perte** : le cartouche ne sort que sur les fiches qui ouvrent
sur les plus, et il les clôt (A-152).

**`C-05`, l'agent public maintenu, est ouvert en pendant de `C-30`** — quatre
apports, quatre vedettes. Et quatre libellés de perte sont écrits, comblant là où
il le fallait le manque relevé en A-138 (A-153). Vingt apports rédigés sur 193.

**Cinquième passe : une correction de fait, et la fin du ressassement.** Le
0,54 M d'agents perdants est périmé — le décompte à date est de 580 000 postes
publics, et `C-05` se recalcule à 5,22 M (A-155). La note de dérivation qui
portait l'ancien chiffre reçoit un bandeau de correction.

« Qui paie » disparaît de l'affichage : une formule vraie de toutes les lignes
n'informe sur aucune. Seules restent les contreparties à lien unitaire manifeste,
chômage et retraite (A-156). L'échange d'une carte de perte **renvoie au gain par
un astérisque** au lieu de le recopier, et deux redites de maille tombent —
« votre administration ferme » recouvre l'échelon et le poste (A-157). Cinq
corrections de langue closent la passe (A-158).

**Sixième passe : l'astérisque est révoqué le jour même.** La carte de perte ne
porte plus d'échange du tout — le gain se lit en grand quelques centimètres plus
bas, la mise en page tient la raccroche. Et la perte se compose comme le gain :
une vedette d'un ou deux mots, « Le poste », « Le statut », puis une phrase
factuelle. Ni euphémisme ni dramatisation (A-159).

L'agrégat national quitte la fiche de la personne : les 30 Md€ du chômage
deviennent « Votre compte » (A-160). « En franchise » rejoint les 0,77 €, dont
il était le propos.

**Septième passe : la série s'ouvre.** L'auteur tranche la composition des
600 € — 300 € de salaire, 300 € de comptes personnels — et l'ordre à l'intérieur
des comptes : la retraite d'abord, le chômage ensuite (A-162). La contrepartie
« pensions supérieures à 1 600 euros » est retirée : elle gageait l'impôt sur le
revenu, non la restitution des cotisations, et sept lignes la portaient (A-163).
Le statut ne se réduit plus à l'emploi à vie (A-164).

**Seizième passe : la galerie corrigée, dix-huit fiches.** La dette par foyer
était une image et cesse d'être une perte au référentiel (A-185). Les concepts
officiels du corpus se reprennent tels quels — le bouclier sanitaire se nomme,
le compte éducation porte ses 6 600 euros (A-186). Et l'entreprise porte enfin
**les clients plus riches** en vedette, l'enseignant ouvre sur la liberté, le
retraité sur la niche, le locataire nomme l'APL, le chèque ciblé se nomme
(A-187).

**Quinzième passe : la galerie est arrêtée.** Dix-neuf fiches. L'usager d'une
mission facultative sort — couvert par le bénéficiaire d'un chèque et par
l'agent au poste supprimé ; l'entreprise et l'association subventionnées
fusionnent ; la personne handicapée ne porte aucune perte (A-184).

Deux corrections d'appareil : la structure commande les pertes comme les gains,
et un rappel porte la vedette du gain tel qu'il est dit chez son attache — sans
quoi le bandeau sortait vide (A-183).

**Quatorzième passe : le bloc de lancement.** La structure devient un document
— `structure_fiches.py`, arbitré fiche par fiche : titre, axe, gains d'attache
dans l'ordre, pertes. La carte le rend lisible, le générateur l'exécute (A-181).

**Vingt-deux fiches, 115 apports rédigés sur 200.** Le prototype est couvert
intégralement, les perdants de l'onglet de synthèse le sont par fiche propre ou
par fusion (A-182).

**Deux pertes manquaient au référentiel et y sont portées** : la suspension de
l'indexation automatique des pensions — au manuscrit, jamais en ligne — et la
sortie des dépenses de confort du bouclier sanitaire, que le livre distingue des
soins critiques.

**La personne handicapée ne perd rien** : elle gagne 1 100 euros par mois versés
automatiquement, en lieu et place de l'empilement des allocations.

**Treizième passe : deux couches.** L'auteur énonce ce qui manquait depuis le
début — le référentiel **décrit**, complet et sourcé ; la fiche **choisit**, et
son cherry picking répond à une logique propre. Plafond, modalités, redites,
attaches et ordre sont des règles de sélection, non des jugements sur la
matière ; le référentiel ne se coupe jamais, et plusieurs éditions choisiront
autrement sur la même matière (A-179).

L'édition en cours se déclare : **une galerie de présentation générale**, sans
trop de détail, qui balaie les grands personas.

Les attaches sont arbitrées (A-180). Le foyer porte la restitution — 20 000 €,
600 €/an de rendement, « chacun paie ses choix ». Le retraité, c'est une seule
chose : sa part des 20 000 €, en rente à vie — le complément viager et le
rendement permanent sont **le même capital, non cumulables**, et les aligner
était la faute. Le citoyen, c'est l'État efficace et utile. La personne sans
emploi porte la perte du chômage et la contextualise.

**Manque relevé** : la fin de l'indexation automatique des pensions n'est une
ligne nulle part — elle n'existe que dans un champ `attenuation`. À instruire
avant d'écrire la fiche du retraité.

**Douzième passe : l'attache et le rappel.** Le socle est révoqué le jour même —
c'était la même faute que « tout le monde », un bloc qui n'appartient à
personne. À la place : **chaque gain a une attache**, la catégorie où il est le
plus pertinent, et il s'y dit en entier ; **partout ailleurs il revient en
rappel**, sa vedette seule, sur une ligne en pied de fiche. Chaque fiche s'ancre
sur son gain principal, ou sur sa perte quand elle est d'abord perdante (A-178).

Le locataire du parc privé, que le socle avait vidé, retrouve sa raison d'être.

**Onzième passe : le socle.** La répétition revenait malgré trois contrôles,
parce qu'ils cherchent une redite de mots quand la redite est de matière. **Un
gain projeté sur deux catégories ou plus quitte les fiches et va au socle**, dit
une fois en tête de la série ; chaque fiche ne porte plus que ce qui lui est
propre. La répétition ne se corrige plus, elle devient impossible (A-177).

Dix gains au socle. Et le socle dit lesquelles des fiches n'ont pas lieu d'être :
le locataire du privé n'a rien en propre et sort de la série, le locataire HLM
n'existe que par sa perte, l'enfant et le parent portent un gain chacun et
demandent à être fondus.

**Dixième passe : la réduction croisée.** Deux contrôles neufs cherchent ce
qu'une relecture fiche par fiche ne peut pas voir. **A7** refuse qu'un même
ancrage porte deux fois le même apport — trois copies dormaient au corpus.
**A8** impose à la vedette d'être une grandeur ou un groupe nominal court, ou un
objet nommé du corpus : six phrases-vedettes sont rentrées dans la forme. Le
registre se contrôle désormais sur la vedette et la phrase ensemble (A-176).

**Neuvième passe : on resserre, et on revient en arrière.** Le bloc à vingt et
une fiches est refusé — trop long, niveaux de concept mélangés, et réécrit là où
il fallait réviser. Le dépôt revient à douze fiches.

**Une dominante et cinq items, pas un de plus** (A-173) : le plafond oblige à
trancher, et `ORDRE` dit ce qui passe. **« Tout le monde » n'est pas une
personne** (A-174) : la nation ne prend pas de fiche, on distingue le
contribuable, le citoyen, le foyer. **Réviser n'est pas réécrire** (A-175) :
une consigne de correction porte sur ce qu'elle nomme, et un exemple de l'auteur
donne le sens, non la lettre.

Appliqué de la passe : compte éducation nommé, agent public **indispensable**,
charge stable de l'entreprise et ses quatre gains valorisés, quotient familial
porté au parent, locataire HLM ouvert.

---

**Ce qui suit décrit l'état refusé, conservé pour mémoire.**

**Huitième passe : le bloc de lancement du site.** Vingt et une fiches, **130
apports rédigés sur 201**. `C-00` la nation fond dans « tout le monde » et les
gains macro vont aux personas (A-169). La charge de l'entreprise ne monte pas —
« gain net » était trompeur — et la simplification, la rerégulation, la fusion
et l'attractivité sont valorisées (A-170). Le corpus nomme ses objets, les
fiches aussi : compte épargne personnel, compte éducation ; et l'agent public
devient **indispensable** (A-171). Les perdants de l'onglet synthèse sont
adressés en propre, quatorze libellés de perte écrits (A-172).

**Le compte épargne personnel est nommé** — le corpus ne l'avait jamais fait —
et la retraite puis le chômage s'y disent une fois, ensemble (A-166). L'ordre de
lecture devient propre à chaque catégorie : une table `ORDRE` par catégorie, là
où les promesses ne donnaient que la chaîne doctrinale (A-167). Et une catégorie
ne recopie plus sa voisine : elle varie l'angle ou elle replie — le jeune adulte
passe de seize lignes à dix (A-168). **Une vedette se mérite.**

**Huit catégories du proto sont écrites** — 52 apports, 52 vedettes, cinq
libellés de perte. Le corpus porte **72 apports rédigés sur 194**, contre 20 le
matin. `C-02`, `C-03` et `C-00` restent en attente d'A-141 (A-165).

---

**Ce qui suit est antérieur à la septième passe.** Une question était partie à
l'auteur : la composition des 600 €. Le corpus décompose
275 € de CSG-CRDS et 292 € d'autres économies, ce second terme reconstitué par
différence — écrire « 300 € sur votre compte retraite » fabriquerait un chiffre
(A-161).

---

## 20260827 — L'auteur tranche le perdant, et le contre-PLF reste au même projet

**Deux arbitrages de fond, et ils simplifient le chantier au lieu de l'alourdir.**

Sur les opérateurs, **c'est notre décompte qui sort** : les comptes externes
bougent tous les ans et portent plusieurs variantes. Ce qui reste de
l'instruction du matin est la seule règle qui ne dépende d'aucune source
extérieure — notre 1 104 contient les 434 opérateurs et les 318 commissions, donc
on sort le total, ou la ventilation, jamais les deux en enfilade.

**Il n'y a pas de perdant ultime, seulement des perdants ponctuels.** Une perte se
raccroche toujours, et le gagnant varie selon le sujet — en général le
travailleur, parfois le ménage, le citoyen, l'enfant. La maille de restitution
cesse donc d'être une question : elle est déclarée ligne à ligne et le référentiel
la porte déjà, 56 catégories et 8 groupes. Le perdant relatif au statu quo
disparaît avec le contrefactuel qu'il aurait fallu construire.

**Le chiffrage du chantier est mesuré, et le côté perte est écrit.** Quarante-neuf
perdants sur quarante-neuf portent leur justification et leur raccroche,
quarante-sept sur quarante-neuf leur relais ; les vingt-deux capteurs et les huit
diagnostics sont complets. Tout ce qui reste est le côté gain : **182 apports et
183 contreparties sur 194 lignes**, soit trois cent soixante-sept textes courts,
médiane dix-huit mots. Une unité de préparation, puis neuf unités d'écriture
découpées par groupe.

Un constat qui allège la jonction : **les 194 gains portent déjà tous leur
grandeur dérivée.** L'incidence par population n'est donc pas une matière à
ventiler sur les catégories — la table de rapprochement devient un contrôle de
concordance, non une alimentation.

**Le contre-PLF n'ouvre pas de second projet.** Un second projet devrait porter
l'archive, les référentiels et les cinq classeurs pour que la chaîne tourne :
seconde copie du corpus, second point de vérité. Ce que le chantier ajoute au
coffre est faible — le recensement est un dérivé qui ne se verse pas, et trente
amendements pèsent une centaine de kilo-octets sur une archive qui en fait 1 238.
Le découpage se fait par conversation, ce qui est déjà la règle.

**Reste ouvert** : le périmètre du site et ce qui est public, le nombre
d'amendements et leur ordre de dépôt, le registre de l'amendement, le calendrier
du PLF suivant, le recouvrement de C-01, C-02 et C-03, et la date du bon à tirer.

---

## 20260827 — Trois chantiers cadrés, et ce que chacun attend

Le corpus est repris entier : archive technique dépliée, documents restaurés par
copie d'octets, cinq classeurs sectoriels reconvertis et le socle rejoué. `make`
passe sans erreur, `make controle` sort zéro échec, zéro anomalie, zéro écart
ouvert, trente-deux bouclages sur trente-deux. La couche des chiffres est ce
qu'elle disait être.

**Un `R1` s'est présenté à l'ouverture et il ne cachait pas un faux.** La feuille
de route du dépôt fait dix-neuf lignes de plus que son empreinte. Deux fils
auxiliaires distincts ont redemandé le document au coffre : même empreinte les
deux fois, identique au fichier écrit. La chaîne coffre → transcript → copie
d'octets ne fait pas intervenir de modèle, donc c'est l'empreinte qui a retardé,
et la cause est celle que A-72 avait déjà nommée. Ce qui en sort est une règle de
conduite : devant un `R1`, la preuve n'est ni la taille ni l'allure du contenu,
c'est une seconde lecture indépendante du coffre.

**Trois chantiers ont désormais une carte**, `methode/carte_des_chantiers.md`,
qui dit pour chacun son périmètre, ce dont il dépend, ce qu'il rend, et quand.
L'ordre vient des dépendances : gagnants-perdants est en amont du site, qui
n'ajoute aucune matière et n'expose que la sienne ; le contre-PLF est parallèle
et dépend du même socle. Le contre-PLF est le seul dont la date ne se négocie
pas, et le seul qui demande de construire une capacité qui n'existe pas.

**Quatre questions d'architecture se sont révélées déjà tranchées**, et les
rouvrir aurait coûté une session. Le site est une vitrine, A-60 le dit. Une base
autonome qui diverge viole le point de vérité, donc le site est un dérivé que
Vercel déploie sans jamais l'écrire. Une jonction entre deux mailles qui ne se
superposent pas s'écrit à la main, comme les faits rapprochés et les douze lignes
d'opérateur. Et un amendement s'accroche à une ligne budgétaire, pas à un nœud de
doctrine — c'est ce qui décide par où le recensement commence.

**Le document de Génération Libre versé le matin est ouvert et digéré.** Un docx
à la racine du coffre ne se déplace pas ; il se déclare là où il est, et le
chantier entre par sa digestion, `sources/gabarit_expose_sommaire.md`. Cette
digestion signale deux endroits où la forme GL et le corpus divergent : la
proportion du constat, une cinquantaine de mots sur deux cent cinquante, et le
vocabulaire, qui est fait pour un post et non pour la séance. Le contrôle de
sortie prendra un jeu de règles par registre ; lequel s'applique à un amendement
revient à l'auteur.

**Le point à vérifier avant tout emploi est instruit.** Notre 1 104 agences est
une somme de quatre familles qui contient les 434 opérateurs et les 318
commissions : les deux chiffres ne se citent pas côte à côte. Le 103 du document
GL est un décompte du Conseil d'État de 2012, non un chiffre de 2025 ; la
synthèse du Sénat de juillet 2025 donne 434 opérateurs, 317 organismes
consultatifs et 1 153 organismes publics nationaux. Le « 12 000 » de l'exemple GL
ne s'y retrouve pas, et l'écart porterait sur un facteur dix — à vérifier sur la
pièce elle-même, que la session n'a pas pu ouvrir.

**Reste ouvert, et cela seul** : le périmètre du site et ce qui est public, la
définition de perdant et la maille de restitution, le nombre d'amendements et
leur ordre de dépôt, le registre de l'amendement, le chiffre d'agences à citer,
ce qui sort du coffre, le calendrier du PLF suivant, et la date du bon à tirer.

---

## 20260827 — La couche budgétaire prend sa forme : titres, traitements, unités

L'onglet budgétaire ne se lisait qu'à travers quinze cellules repérées à la main.
Il en porte deux cent vingt-sept lignes et vingt et une colonnes, et ce qu'il
cachait est la pièce qui manquait au chiffrage.

**Une nomenclature paraît**, écrite une fois pour toutes et à laquelle tout se
réfère désormais : les sept titres de l'article 5 de la LOLF, les dix catégories
que le classeur retient, les sept traitements que l'auteur applique, et les huit
qualifications de montant. Chaque qualification porte son unité **et ce avec
quoi elle se somme** — une assiette avec rien, un paramètre avec rien. Une
assiette additionnée à son économie double le chiffrage : la table l'interdit au
lieu de le déconseiller.

Cette règle a corrigé quatre postes sur-le-champ. « Sur culture », « sur
FrComp. », « sur ville » et « MPR (Anah) » étaient rangés en assiette par une
règle de préfixe. Ce sont des économies. Le préfixe « sur » quitte la règle
mécanique, les quatre postes s'écrivent à la main, et chacun est vérifié contre
l'arbre des économies.

**Le traitement est la couche de décision, et elle se lit enfin.** Chaque
programme porte, pour chacune des cinq catégories de transfert, un mot — Oui, En
3 ans, Fusion CI, Bourse, Sécu, Flux OM — qui dit si le crédit est supprimé,
reporté, ou seulement déplacé. Fusion CI et Bourse ne sont pas des économies : le
crédit change de véhicule. Sécu non plus : la dépense quitte l'État sans quitter
la dépense publique. Les compter en économie gonflerait le chiffrage de ce qui
n'a fait que bouger.

Cette lecture se prouve. La part supprimable dès l'année 1 affichée en tête se
retrouve exactement, catégorie par catégorie, en sommant les crédits des
programmes marqués « Oui » : 6 728,42 · 21 827,40 · 7 761,51 · 13 543,42 M€,
quatre sur quatre. Les 128 programmes font les 35 missions, les 35 missions font
la grille des dix catégories, dix sur dix.

**La part budgétaire cesse d'être un résidu.** Elle se déduisait par
soustraction — la ligne du chiffrage moins ce que les taxes recomposent —, et un
résidu n'est pas une source. Elle est écrite, poste par poste, avec sa catégorie
et sa qualification : 0,434 Md€ sur France Compétences, 2,734 sur France Travail
en titre 2 et titre 6, 0,517 sur la culture, 0,921 sur l'ADEME, 1,333 sur
MaPrimeRénov' en transfert aux ménages. Les cinq lignes qui restaient ouvertes se
ferment. **Trente-deux bouclages sur trente-deux** : plus une seule ligne du
chiffrage dont l'origine se devine.

**La couverture se dit.** Trente-quatre programmes du PLF échappent à la couche
de décision, et le contrôle les nomme avec leur montant plutôt que de laisser
croire à une couverture totale : 141 Md€ de remboursements et dégrèvements,
crédits évaluatifs hors périmètre par nature ; 1,15 Md€ de comptes d'affectation
spéciale ; 273 M€ sur deux programmes ordinaires. Le programme 368 manque au
bloc de détail alors que sa ligne de mission le compte — l'agrégat n'est pas
faux, le détail est incomplet, et le contrôle le sort case par case.

Une cellule que le classeur laisse en erreur — la part supprimable de la
catégorie 62 — se recompose depuis les traitements, 15 282,13 M€, et s'affiche en
le disant. **Recomposer n'est pas corriger** : l'auteur garde sa source.

Le classeur de synthèse passe à douze onglets. Un onglet « Nomenclature » porte
les quatre tables en clair ; l'onglet « Budget général » porte la grille, les
paramètres, les postes qualifiés et les 128 programmes avec leur traitement.

La réconciliation des opérateurs reçoit le traitement de son programme, et un
croisement paraît : le régime de l'opérateur contre le traitement de la
subvention. **Ce n'est pas une table de fautes** — un EPIC qui vit de ses
recettes n'a plus besoin de subvention, un opérateur internalisé la rend au
ministère. La seule case qui se regarde est « suppression × rien » : dix-huit
opérateurs qu'on supprime dont le programme garde sa subvention intacte. Et
encore : cette subvention est à la maille du programme, que d'autres partagent.

---

## 20260827 — L'auteur tranche : le jaune, l'ANAH, les ODAC, la source validée

Quatre décisions ferment quatre ouvertures posées le matin même.

**La base d'emplois vient du jaune, pas de l'annexe.** Les 46 440 ETP hors France
Travail et les 53 200 de France Travail sont tirés du jaune budgétaire
« Opérateurs de l'État ». Le jaune donne le plafond d'emplois, l'annexe donne
l'exécution : les deux ne comptent pas la même chose. Les écarts de 393 et de 148
ETP cessent d'être ouverts et deviennent un **écart de concept**, documenté et
clos. Le contrôle distingue désormais trois verdicts de dérivation — accord,
écart de concept, écart ouvert — et **il n'y a plus aucun écart ouvert**.

**MaPrimeRénov' se rattache à l'ANAH, qui le distribue.** La ligne quitte la
maille des dispositifs, qui disparaît. L'ANAH porte deux économies : 0,4 Md€ de
restitution de sa taxe affectée et 1,3 Md€ de crédits MaPrimeRénov', soit
1,7 Md€. La réconciliation tient désormais une **liste** d'économies par
opérateur, non une ligne — une clé unique aurait écrasé la première et perdu un
milliard. L'assiette devient les programmes 174 et 135, et elle couvre la ligne.

**Les budgets initiaux sont sourcés ailleurs.** Les 14,2 Md€ chiffrés d'après les
budgets initiaux 2025 de France Compétences, France Travail et l'ADEME ne sont
plus une réserve. Le signalement reste, parce qu'il dit d'où vient le montant ;
il cesse d'être un avertissement. **Une pièce absente qu'on n'a pas cherchée est
un trou ; une pièce absente du corpus mais sourcée ailleurs est un renvoi**, et
les confondre ferait passer un chiffrage validé pour un chiffrage douteux.

**Les affectataires hors liste ne sont pas hors de tout.** Les trois lignes
qu'aucun opérateur ne portait se rattachent à la liste ODAC-ODAL, où elles ont un
identifiant, un nombre d'entités et un régime : Action Logement Services à
l'ODAC-223, les chambres consulaires à l'ODAC-730 pour 273 structures, les
établissements publics fonciers à l'ODAC-731 pour 40. Les trois sont en régime de
vente. La maille « affectataire hors liste » — un constat de manque déguisé en
catégorie — disparaît ; il reste trois mailles : opérateur du PLF, ODAC-ODAL,
résidu.

Chaque rattachement publie **les deux comptes** plutôt que d'en choisir un :
l'annexe des taxes nomme des affectataires, l'ODAC compte des structures. Deux
affectataires consulaires contre 273 chambres, 34 affectataires fonciers contre
40 établissements — six n'ont pas de taxe affectée au PLF 2026, et cela se lit.

La portée dépasse ces trois lignes : les 145 affectataires de taxe qui ne sont
pas opérateurs du PLF sont rattachables de la même façon. Le travail des 269
appariements change de cible — ce n'est plus la liste des opérateurs, c'est **la
liste des opérateurs ou celle des ODAC-ODAL**.

`make controle` : zéro échec, zéro anomalie, zéro écart ouvert.

---

## 20260827 — L'arbre des économies rattaché à son assiette, et ce qui n'y tient pas

Le chiffrage cesse d'être affiché pour devenir traçable. L'onglet du classeur qui
porte l'arbre des économies entre au socle : deux périmètres, dix rubriques,
vingt-deux lignes de détail, et pour chacune ce que le classeur écrit — les deux
temps de la restitution, le code de destination, l'hypothèse en toutes lettres,
l'incidence par population quand elle est allouée. La grande synthèse entre avec
lui, et elle apporte ce qu'aucune autre pièce ne portait : **la source citée
poste par poste**.

Le classeur de calculs fait exception à la règle des deux couches. Il n'y a pas
en lui un socle publié et une interprétation ajoutée : il est de l'auteur de bout
en bout. Ses entrées portent donc `classeur` et `lecture`, et non `socle` et
`interpretation`.

Chaque ligne d'opérateur est rattachée à son assiette, à la main, et le
rattachement révèle une chose que la réconciliation ne pouvait pas dire : **les
lignes d'opérateurs ne sont pas toutes des opérateurs.** Sept visent un opérateur
de la liste officielle, trois un affectataire de taxe qui n'y figure pas — Action
Logement Services, les chambres consulaires, les trente-quatre établissements
publics fonciers —, une un dispositif qui n'est pas un organisme, et la dernière
est un résidu que le classeur ne détaille pas. Le périmètre des opérateurs ne
couvre pas le chiffrage, et c'est une information, non un défaut.

Six lignes se recomposent exactement depuis les taxes affectées de leur
assiette ; l'écart résiduel tient dans l'arrondi d'affichage du classeur et se
nomme comme tel. Quatre sont budgétaires : le programme se nomme, la part que
l'auteur y taille ne s'en déduit pas, et elle reste écrite en clair comme part
budgétaire plutôt que d'être absorbée. Vingt-sept bouclages en accord, du détail
à la rubrique, de la rubrique à la tête, et de l'incidence par population aux
trois totaux de tête.

La chaîne des emplois et des charges se rejoue enfin depuis la synthèse du budget
général. Les charges courantes d'État sont le fonctionnement et l'investissement
non régaliens à quatre-vingts pour cent ; les départs de fonctionnaires sont la
masse salariale non régalienne à quatre-vingt-dix pour cent de départs et trente
pour cent non maintenus ; les soixante et un mille quatre cents emplois supprimés
sont cette même masse divisée par le salaire moyen. Cinq dérivations sur sept
tombent juste. **Les deux qui ne tombent pas restent ouvertes** : la base d'ETP
retenue pour les opérateurs n'est pas celle du PLF 2026 — quarante-six mille
quatre cent quarante contre quarante-six mille huit cent trente-trois hors France
Travail, cinquante-trois mille deux cents contre cinquante-trois mille
cinquante-deux pour France Travail.

L'économie chiffrée descend sur la ligne d'opérateur : sept opérateurs la
portent, pour dix-huit virgule sept milliards, avec leur canal, leur part
recomposée par les taxes, leur part budgétaire, leur hypothèse et l'endroit où
l'économie retombe une fois reclassée. Trois d'entre eux — France Compétences,
France Travail, l'ADEME — sont chiffrés d'après leur budget initial, **pièce
absente du corpus**, et la ligne le dit.

Le classeur de synthèse passe à onze onglets. Le Makefile passe enfin au socle
les deux classeurs qu'il ne lui donnait pas, celui du budget général et celui des
calculs. `make controle` ne relève aucun échec et aucune anomalie.

Le journal est remis dans son ordre déclaré, le plus récent en tête.

---

## 20260827 — Les sept classeurs inventoriés, les opérateurs tracés, un classeur de synthèse

### La réponse honnête à « tout est-il digéré ? » : non

**Quarante-neuf feuilles sur sept classeurs.** Huit sont importées — leurs
lignes sont au socle et se recomposent. Quatorze sont lues — structure et
agrégats ouverts et consignés. **Vingt-sept ne sont pas lues**, et c'est dit.

Ce n'est pas une déclaration mais un état : il vit à l'onglet `Couverture` du
classeur de synthèse, et il se régénère.

Trois des non lues sont nommément utiles et attendent : l'onglet
**Méthodologie** de l'annexe des dépenses fiscales, qui donne la fiabilité du
chiffrage dépense par dépense ; l'onglet **Références juridiques**, qui donne
l'article du code pour chacune ; et les **Échéances**, qui datent la fin du fait
générateur.

### Le socle s'étend au budget général

Quatre imports de plus : les **2 351 lignes du PAP 2026** — mission × programme
× action × sous-action × nature —, la ventilation de l'onglet Synthèse par
nature et par destinataire, les **749 ODAC-ODAL** avec leur régime, et la
nomenclature des missions et des **128 programmes**.

**Un bouclage de plus, et il ferme une boucle ouverte** : l'onglet ODAC-ODAL
compte 700 organismes dont 372 déjà traités au titre des opérateurs du PLF —
700 − 372 = 328, exactement les organismes hors PLF de la synthèse des agences.
Les deux onglets se répondent.

Le classeur des dépenses porte des cellules en erreur, `#VALUE!`, que le socle
reprend telles quelles : **ce n'est pas au socle de réparer une formule
cassée**.

### Les opérateurs, tracés faute d'identifiant

La liste officielle est l'onglet `Opérateurs` : 180 lignes, 434 entités. Tout
s'y rattache par le libellé, et le libellé est instable — « ADEME - Agence de
l'environnement… » ici, « Ademe » là, « ANSC Agence du numérique… » ailleurs.

Cinq passes mécaniques, de la plus sûre à la moins sûre : nom normalisé, sigle
avant tiret, forme longue, forme longue sans tiret, sigle en tête confirmé par
sa forme longue. **Rien ne s'apparie sur un score** — le meilleur voisin de
« Communes » est « Ordre de la Libération - Conseil National des communes » avec
un score de 1,00, et c'est faux. Ce que la mécanique n'attrape pas sort en
candidat et se tranche à la main.

**Le taux de rappel est mesuré, non supposé.** Sur les 376 ODAC que le classeur
déclare déjà traités en opérateur, l'appariement en retrouve 107 — **28 %**.
Les 269 autres sont un travail borné et nommé, ligne à ligne.

Côté taxes affectées : 168 libellés d'affectataire, 23 appariés, 6 candidats, et
137 sans voisin plausible — collectivités, organismes de sécurité sociale,
personnes privées, qui ne sont pas des opérateurs du PLF et n'ont pas à l'être.

### Le classeur de synthèse

Neuf onglets, 449 formules, zéro erreur au recalcul. Les totaux sont des
formules, jamais des valeurs calculées : il recalcule quand ses entrées
changent.

`Lecture` dit ce qu'il est et ce qu'il n'est pas. `Couverture` porte l'état des
quarante-neuf feuilles. `Bouclages` met côte à côte ce que le socle recompose et
ce que le classeur affiche, **avec l'écart en formule** — seize lignes, somme
des écarts absolus à un millionième près. `Chaîne` rejoue les cinquante-sept
opérations du corpus avec leur tolérance déclarée et un verdict : **cinquante-
sept « juste », zéro « à voir »**. Puis le détail — affectataires, niches,
opérateurs, budget général — et les seize hypothèses.

**Il ne remplace rien.** Les classeurs de l'auteur restent la source officielle ;
celui-ci est la vue de ce qu'on en a lu.

---

## 20260827 — Le gage CSG requalifié, les onglets manquants repris, les opérateurs réconciliés

### Une correction de vocabulaire qui change une lecture

**Arbitré par l'auteur.** En budgétaire — et **seulement** en budgétaire — le
« gage CSG » n'est pas une nature de recette : c'est **ce qui est restituable dès
l'année 1**, et le « solde » est **ce qui est restitué ensuite**. La vraie
économie valorisable restituée est **leur total**.

Les nommer « gage » et « économie en sus » laissait croire à deux natures
différentes. Ce sont deux temps de la même restitution. Les champs du socle sont
renommés `restitue_annee_1`, `restitue_ensuite`, `economie_restituee_totale`, et
la grille de lecture le dit en toutes lettres.

**La règle ne vaut pas pour les dépenses fiscales** : là, le gage net et l'effet
macroéconomique sont deux grandeurs distinctes qui ne s'additionnent pas.

### Les onglets manquants sont repris

Neuf feuilles de plus au socle. Les cinq feuilles latérales de l'annexe des
dépenses fiscales portent la **même clé** que l'onglet des chiffrages — le
numéro de dépense fiscale — et ne se lisent donc pas séparément : elles
enrichissent la même entrée. **465 sur 465** pour chacune.

Chaque dépense fiscale porte désormais sa réalisation et ses prévisions 2025 et
2026, ses dates de création, de dernière modification, de fin du fait générateur
et d'incidence budgétaire, la nature et le nombre de ses bénéficiaires, sa norme
de référence avec son code et son article, son programme de rattachement — et
**la fiabilité que l'administration déclare de son propre chiffrage**.

Cette dernière compte : un gage bâti sur un ordre de grandeur ne vaut pas un
gage bâti sur une simulation, et le classeur de synthèse le compte par ligne.

S'y ajoutent les 1 405 lignes de crédits exécutés et les 322 lignes d'emplois
exécutés du rapport annuel de performance 2024 — l'**exécuté** là où le projet
annuel porte le **prévu**.

**La couverture passe de 8 importées, 14 lues, 27 non lues à 16, 17 et 16.**

### La réconciliation des opérateurs

Statut, emplois, taxes affectées, subvention pour charges de service public,
transferts de titre 6 — sur une ligne par opérateur, pour les 180 de la liste
officielle.

**Les mailles ne sont pas les mêmes, et c'est la limite qui devait être dite.**
Statut, emplois et taxes se rapportent à l'opérateur. La subvention et le titre 6
se rapportent au **programme** : le projet annuel de performance ne nomme jamais
l'opérateur. Trente programmes sur cinquante-quatre portent plus d'un opérateur,
et pour ceux-là le montant ne leur est pas imputable un par un. La ligne le dit,
et les deux colonnes ne se totalisent pas.

Deux constats assumés. **Le statut n'est connu que pour 23 opérateurs**, parce
qu'il ne se lit que dans l'annexe des taxes affectées. **La subvention n'est à la
maille de l'opérateur que dans 24 cas.** Les afficher quand même en le disant
vaut mieux que de les taire.

Les libellés de mission et de programme de l'onglet Opérateurs sont des formules
que la conversion rend en `#NAME?`. Ils se réparent par la nomenclature de
l'annexe État, qui les porte en clair indexés par numéro de programme :
**180 sur 180**.

### Le classeur

Dix onglets, 638 formules, zéro erreur. L'onglet `Opérateurs réconciliés` porte
les quatre canaux, avec la colonne « maille » qui dit quand la subvention est
partagée. Les bouclages passent à seize lignes et gagnent l'économie restituée
totale ; l'onglet des dépenses fiscales gagne deux colonnes de fiabilité.

Chaîne toujours à 57 « juste », zéro « à voir ». Bouclages à zéro échec.
`make controle` à zéro anomalie.

---

## 20260825 — Le référentiel des faits tient debout, et il dit ce qu'il ignore

Première exécution vérifiée du générateur, sur le proto Données restauré. **257
entrées** — 59 des notes du manuscrit, 89 du `REF_doctrine`, 109 du proto. Le
compte annoncé au journal du 21 août se confirme, cette fois contre une
exécution.

**Ce que les cent neuf candidats donnent réellement.** Tous sans source, tous à
confiance nulle, aucun sourcé à la main. Cinquante-quatre sans unité, dont
vingt-six portent une unité déclarée en attribut du proto que le relevé garde à
part, et vingt-huit n'en portent nulle part. Aucun en millésime budgétaire :
tous prennent le 2024 de convention, et la branche budgétaire de la convention
est inatteignable pour eux par construction, puisqu'elle se déclenche sur la
source et qu'ils n'en ont aucune.

**Et trente-neuf des cent neuf ne portent pas le fait qu'ils paraissent porter.**
Huit sont des adresses web dont le relevé a pris le numéro pour une valeur,
treize sont des lignes de tableau découpées, vingt-trois ont une année en tête de
valeur parce que le corpus écrit « en 2024, X vaut Y » et que le relevé prend le
premier nombre. Les trois classes se recoupent et leur union fait trente-neuf.
Soixante-dix candidats restent, dont quinze sans unité.

**Le rapprochement des faits est écrit.** `MEME_QUE` porte vingt-cinq faits et
cinquante-trois entrées : chaque groupe nomme le fait, désigne son entrée de
référence par confiance décroissante, et dit pourquoi ces entrées portent la même
chose. Le contrôle `F7` distingue désormais trois verdicts — accord, tête
décalée, discordance — et signale à part les unités divergentes.

**Trois couples ne concordent pas.**

- **L'assiette de la CSG** : 98 % au paramètre `D3-2-1-p6` contre 98,25 % au
  proto. Le paramètre porte par ailleurs un complément de 1,75 %, qui est celui
  de 98,25 et non celui de 98.
- **Les pensions de retraite versées en 2024** : 407 Md€ à la note `e74` du
  manuscrit, droits dérivés, charges de gestion et action sociale inclus, contre
  388 Md€ au proto dont 39 de droit dérivé. Deux périmètres, à trancher avant que
  l'un des deux sorte.
- **Le rendement annuel du patrimoine restitué** : 265 €/an à la promesse
  `D7-2-2-e2` contre 264,71 €/an à l'illustration du lexique. Arrondi.

**Six têtes décalées** disent que la valeur est bien aux deux énoncés mais pas en
tête : salaire médian, effet inflationniste, retraites au-delà de 1 600 €,
cotisations chômage, postes supprimés. **Dix-sept unités divergent** sur un même
fait — « milliards » contre « Md€ », « Md€ » contre « Md€/an », « mois » lu comme
« M » de millions.

**Une divergence hors du champ du rapprochement, relevée en propre.** L'aide
personnalisée au logement vaut **16 Md€** au sous-item `D2-4-1-s1` et **17,7 Md€**
dans la chaîne de l'effet `D2-4-1-e2`, où elle entre dans le total de 27,5 Md€.
Écart de 1,7 Md€ sur le même poste. Le rapprochement ne la voit pas — elle oppose
une entrée à la déclinaison d'une autre — et le contrôle arithmétique ne la voit
pas non plus, puisque les deux comptes tombent chacun de leur côté.

Reste ouvert : le sourçage par lots, et la reprise de la tête de valeur au
relevé.

---

## 20260825 — Les trois discordances tranchées, et le lot chômage-retraites-santé

Arbitrages de l'auteur : on prend l'exact pour la CSG, les chiffres du manuscrit
pour tout le reste. Le classeur et le manuscrit ont été ouverts pour les porter.

**L'assiette de la CSG passe à 98,25 %.** Le paramètre `D3-2-1-p6` affichait 98
alors que son propre champ `exact` et l'onglet CSG du classeur portent 98,25 —
un point de CSG au SMIC brut y vaut 1 801,80 × 98,25 % × 1 % = 17,702685 €. Son
abattement de 1,75 % pour frais professionnels était d'ailleurs le complément de
98,25 et non de 98. Le verdict du nœud passe de `RECONSTITUÉ` à `EXACT`.

**L'écart sur l'APL n'existe pas.** La ligne 20 du tableau de référence du
classeur s'intitule « Extinction des chèques ciblés aux particuliers (dont
APL) » et vaut 17,7 Md€ : c'est un agrégat, et les 16 Md€ du sous-item sont
l'APL seule. C'est la chaîne du `REF_doctrine` qui était mal libellée, en
écrivant « chèques ciblés dont APL 17,7 » là où on lit « APL = 17,7 ». Libellé
corrigé. Reste que le détail des chèques ciblés ne couvre que 16 des 17,7.

**Les retraites : le manuscrit porte 125 Md€, et c'est le chiffre fort.** La
note de fin `e74` donne 407 Md€ de pensions versées en 2024 et 282 Md€ de
ressources ; **le corps du livre en tire un déficit spontané de 125 Md€ par an,
« les deux-tiers du déficit public »**. Le proto, au périmètre étroit de
388 Md€, donnait 106 Md€ et un taux de couverture de 73 %. Au périmètre du
livre, la couverture est de 69,3 %. L'écart de périmètre est de 19 Md€ : les
charges de gestion et l'action sociale. Les deux sources s'accordent sur les
ressources — 282 et 282,4 Md€.

Le périmètre du proto est écarté. Il ne se supprime pas : c'est une archive. Le
rapprochement porte désormais un champ `arbitrage` qui dit quelle valeur sort,
qui l'a décidé et pourquoi, et le contrôle range la discordance en décision
visible plutôt qu'en échec.

**Le corps du manuscrit n'est relevé par rien.** Le générateur lit les notes de
fin, le `REF_doctrine` et le proto. Les 125 Md€ sont au corps du livre : ils ne
sont donc à aucun référentiel, et aucun contrôle ne les voit. C'est le défaut
qui a fait qu'une discordance sur les retraites a pu vivre au corpus alors que
le livre l'avait déjà tranchée.

### Le lot chômage, retraites, santé

Trente-sept entrées sourcées ou redressées à la main. Les candidats sans source
passent de 109 à 93.

**Chômage.** Sources déclarées par le proto lui-même et reprises : Unédic pour
les comptes 2024 et les allocataires, Dares pour les durées et le tableau des
allocations. Tout tombe : 32,6 + 3,3 + 1,1 + 0,1 = 37,059 Md€ d'allocations ;
619 jours d'ancienneté moyenne des inscrits, soit les vingt mois du manuscrit,
contre 580 jours de droit, soit ses dix-neuf mois. La chaîne d'économie est
exacte — 37,1 × ((1 − 37 %) + 37 % × (1 − 52 %)) = 29,96 Md€, qui se décompose
en 17,8 Md€ repris par le crédit d'impôt social et 12,2 Md€ d'économie nette.
La décomposition est exacte par construction, non par coïncidence.

**Deux chiffres du tableau Dares ne se citent pas ensemble.** Le taux de
remplacement brut de 64 % n'est pas 42 / 71, qui fait 59,2 %, et l'allocation
mensuelle de 1 150 € n'est pas 42 × 28, qui fait 1 176 €. Ce sont des
statistiques calculées allocataire par allocataire : la moyenne des rapports
n'est pas le rapport des moyennes. Les citer côte à côte expose à une division
que n'importe qui refait.

**Santé.** Le bloc est cohérent et **il n'a presque aucune source** : hors
« Institut Santé » pour les 134 Md€ d'affections de longue durée, rien n'est
déclaré. Les entrées gardent donc leur confiance nulle, avec leur millésime,
leur unité et leur arithmétique vérifiée. Ce qui tombe : 200,5 public + 32,5
mutuelles + 20 de reste à charge = 253 Md€ de dépenses médicales ; les soins de
longue durée se décomposent deux fois, par objet et par financeur ; les frais de
gestion 7 + 1,2 + 8,7 = 16,9 Md€, que la note `e129` du manuscrit source ; les
recettes sociales socle à 367,6 arrondies à 368 ; l'architecture cible 142 + 100
= 242 et 100 + 41 de mutuelles = 141 Md€ de compte santé.

**Ce qui ne tombe pas : les 242 Md€.** Public médical 200,5 + longue durée
publique 38,3 + prévention publique 6,1 font 244,9. Il manque 2,9 Md€
d'explication, et c'est le total sur lequel repose toute l'architecture cible.

**Et une unité fausse d'un facteur mille.** Le proto écrit « Total dépenses de
fonctionnement ROBSS+FSV : 14 261 Md€ » là où ce sont des M€, soit 14,3 Md€ —
ses propres composantes le montrent, CNAF 3 132 M€ et branche maladie 7 391 M€.
Corrigé au sourçage, pas au proto, qui est une archive.

### Deux acquis d'appareil

Le contrôle ramène désormais les montants à l'euro avant de comparer : « 37 059
M€ » et « 37,1 Md€ » ne sont plus une discordance, « Md€ » et « milliards » ne
sont plus une divergence d'unité. Et la comparaison porte sur le nombre seul —
un « par an » perdu se dit au relevé des unités, pas en désaccord de chiffre.

Le sourçage à la main peut redresser la valeur de tête quand le relevé a pris
une année ou un libellé pour un nombre. L'entrée porte alors `tete_redressee`.

---

## 20260825 — Le classeur ouvert, les calculs rejoués, les autres protos relevés

### Le détail des 17,7 Md€ existait, il fallait aller le chercher

Onglet Détail Economies, ligne 17. Le poste « Chèques aux ménages » vaut
19,9 Md€ et se décompose : **APL 16,1 + chèque énergie 0,6 + autres 1,0 = 17,7**,
les 2,2 Md€ restants étant l'aide médicale d'État et les exonérations d'emploi à
domicile, que le tableau de référence classe ailleurs — l'une aux aides
inconditionnelles, l'autre aux aides à l'emploi. Il ne manquait rien.

Le reste de la chaîne de `D2-4-1-e2` se recompose aussi : les 22,5 Md€
d'emploi-insertion sont France Compétences 10,6 + France Travail 2,7 + aides
emploi-apprentissage 6,9 + aide emploi-insertion 2,3 ; les entreprises 22,5 +
6,6 + 12,3 = 41,4 ; les particuliers 17,7 + 3,6 + 3,2 + 3,0 = 27,5.

### Les 30 Md€ de chômage sont une économie, et le REF le disait mal

Arbitré par l'auteur. Le classeur les porte deux fois comme telle : ligne 20 des
baisses de dépenses de l'onglet Manifeste, « Économies sur l'assurance
chômage » ; et onglet Capitalisation, « Transformation assurance chômage (base
de dépenses = 37,1 Md€) ». **Le mot « cotisations » n'était ni au classeur ni au
proto** : le nœud `D8-3-1-e2` est requalifié, avec l'opération du proto pour
dérivation et une chaîne de quatre composantes. Et les 184 Md€ de baisses de
dépenses se recomposent : État et agences 82,45 + collectivités 53,5 + chômage
30 + patrimoine 18 = 183,95.

### Ce que le classeur apporte en appui

L'onglet Gages **déclare ses sources poste par poste** : PLF 2026 Voies et
moyens tomes 1 et 2 et données des projets annuels de performance, budgets
initiaux 2025 de France Compétences, France Travail et l'Ademe, Insee comptes de
la nation 2023 en données COFOG, Cour des comptes RALFSS 2024 chapitre IV,
PLACSS 2024 annexe 1. Huit entrées de plus sont sourcées.

L'onglet Capitalisation donne les **636,1 Md€ d'actifs à valoriser** —
participations financières 208,28, foncier public 200,20, logements publics
57,73, parc social 169,89 — et un rendement de 2,9 % qui fait les 18,4469 Md€.
**Deux écarts avec la doctrine, tous deux dans le sens de la prudence** : elle
annonce 3 % de rendement là où le classeur applique 2,9, et 20 000 € par foyer
supposent 600 Md€ répartis quand le classeur en valorise 636,1.

Le parc social s'y lit aussi : 513,34 Md€ d'actif brut moins 171,9 d'encours de
dette font 341,44, que la note e118 arrondit à 340 milliards.

### Les calculs se rejouent désormais

**Une dérivation écrite en prose ne prouve rien.** Quarante-sept opérations du
corpus sont portées sous une forme que la machine évalue, avec leur résultat
attendu et la tolérance admise — et `F8` les rejoue à chaque contrôle. Elles
tombent toutes. Une tolérance ne s'écrit qu'avec sa raison : le seul cas qui
dépasse le centième est l'actif net du parc social, où le manuscrit arrondit
341,44 en « estimé à 340 milliards ».

L'évaluateur n'accepte qu'une expression arithmétique : ni appel, ni nom, ni
attribut. Un contrôle qui exécuterait du code écrit dans un fichier de données
ne serait plus un contrôle.

### Les six autres protos, relevés

`relever_protos.py` découpe chaque proto en phrases, garde celles qui portent un
nombre, et les confronte au référentiel. **554 énoncés chiffrés** sur sept
documents. La grammaire des nombres est celle du générateur, importée et non
recopiée.

Il sort trois listes. Les **collisions** — mêmes mots, unité comparable, aucune
valeur commune : dix, à lire. Les **chiffres hors référentiel** — cent trente,
que rien ne contrôle. Et la **veille**, qui prend le problème à l'envers : on
déclare les grandeurs publiables avec les mots qui les désignent et les valeurs
admises, et toute phrase qui les emploie autrement sort en alerte.

**C'est la veille qui trouve, parce qu'elle part du fait et non du hasard
lexical.**

### Deux fautes trouvées, et une fausse alerte enfin éteinte

**Le 1-pager, qui est le document le plus diffusable du lot, se trompe deux fois
dans la même phrase.** Il écrit « Le salaire médian français est de 2 100 € par
mois, contre 5 500 € en Suisse ». Or le salaire médian net est de 2 190 € (notes
e4 et e99) ; les 2 100 € sont le **revenu médian équivalent** d'Eurostat, note
e8, que le corps du livre oppose aux **4 300 €** suisses. Les 5 500 € ne
désignent nulle part un salaire suisse : au manuscrit, c'est la dette publique
nouvelle par foyer et par an.

**La Q&A du 20260806 annonce une pension de base de « environ 1000 € par mois »**
quand le manuscrit écrit « une pension de base égale à 1 100 euros par mois pour
tous les travailleurs ». Elle est antérieure au référentiel et n'a pas été
régénérée.

**Et le fameux 2 190 contre 2 100 n'était pas une discordance.** Ce sont deux
grandeurs distinctes, chacune avec sa source : le salaire médian net de l'Insee
et le revenu médian équivalent d'Eurostat. Ce que la stratégie réseaux avait vu
de l'extérieur était une ambiguïté de dénomination, pas un désaccord de chiffre —
et le 1-pager, lui, l'a bel et bien commise.

Reste ouvert : les 130 chiffres hors référentiel, et la régénération des protos.

---

## 20260825 — La grille de lecture budgétaire, prouvée, et les hypothèses du livre

Les deux dispositifs coexistent : **les classeurs de l'auteur restent la source
officielle**, et le chantier en formalise la lecture. La grille n'a de valeur
que parce que le contrôle prouve qu'elle lit juste.

### Ce que la grille sépare

Dans les classeurs, deux choses vivent dans les mêmes lignes. **Le socle** est
ce que le document budgétaire publie — un bénéficiaire, un montant, une
référence, un effectif — et il ne se discute pas. **L'interprétation** est ce
que l'auteur y a ajouté en colonnes — le régime retenu et les montants qui en
découlent — et c'est elle qu'un PLF neuf oblige à réexaminer.

Les mélanger, c'est perdre la capacité de rejouer. Séparées, les deux se
recomposent : socle × interprétation = chiffrage. C'est la seule chose que la
grille impose ; tout le reste en découle.

Les identifiants se gardent tels quels, les nomenclatures étant stables :
numéro de dépense fiscale, SIREN de l'affectataire, code de taxe, numéro de
programme. **Une seule fragilité, nommée** : l'opérateur n'a pas de clé
numérique et les agrégats du classeur le filtrent sur son intitulé exact.

### Le socle est construit, et le bouclage est vert

`socle_budgetaire.py` lit trois classeurs sectoriels et produit **465 dépenses
fiscales, 278 taxes affectées et 180 lignes d'opérateur** pour 434 entités,
chacune avec son bloc `socle` et son bloc `interpretation`.

`controle_socle.py` recompose depuis les lignes et compare aux totaux affichés.
**Sept bouclages, zéro échec.** Les 434 entités réparties 15 · 123 · 36 · 226 ·
34 ; les 479 514 emplois répartis de même ; chaque ligne de la synthèse des
agences égale son détail ; les quatre familles font les 1 104 agences d'État ;
8 119,67 M€ de gage CSG et 17 922,39 de suppression effective ; les affectataires
isolés retrouvent leurs lignes ; 465 dépenses fiscales à 89,406 Md€ de
réalisation, 101,321 y compris la TVA des administrations publiques, 43,126 de
gage net, 29,141 d'effet macroéconomique.

**La leçon de lecture, et elle vaut pour tout le reste.** Un agrégat de la
doctrine n'est presque jamais une colonne du PLF. France Compétences, 10,6 Md€ :
onze lignes de taxe affectée font 3 374,90 de gage CSG et 6 749,80 d'économie en
sus, soit 10 124,69 M€ de suppression effective, plus 434,07 M€ de subvention
budgétaire. Chercher le chiffre tel quel au document budgétaire ne le trouve
pas.

Dix calculs de remontée sont portés au contrôle : le compte des calculs rejoués
passe de 47 à **57, tous justes**.

**Un écart relevé et non tranché** : la synthèse des agences donne 668
suppressions et 78 cessions, soit 746 structures à fermer, quand le référentiel
en déclare 750.

### Les hypothèses du livre, consignées

Le livre pose ses hypothèses en littéraire, et **aucun référentiel ne les
portait**. Seize sont consignées : quatre de méthode, huit de paramètre, deux de
comportement, deux d'estimation externe ; huit minorantes, une majorante, sept
neutres.

Une hypothèse n'est ni un fait ni un paramètre : c'est ce sous quoi un fait
vaut. La distinction porte, parce que quand un PLF neuf arrive, ce sont les
hypothèses qu'on réexamine et les faits qui se recalculent.

**Le verbatim ne se recopie pas.** Chaque hypothèse porte un repère court, et
`controle_hypotheses.py` vérifie sa présence littérale au manuscrit. Un repère
qui ne se retrouve plus est une alerte : soit le livre a changé, soit la recopie
a dérivé. Les seize se retrouvent.

Deux écarts entre l'hypothèse annoncée et celle appliquée, tous deux prudents :
la doctrine annonce 3 % de rendement du patrimoine quand le classeur applique
2,9 %, et les 20 000 € par foyer supposent 600 Md€ d'actifs quand le classeur en
valorise 636,1.

**Un manque nommé** : sur le chômage, le livre ne pose qu'un paramètre — six
mois d'indemnisation collective. Les deux autres, 37 % des inscrits sous six
mois et allocation cible à 52 %, ne sont qu'au proto Données, et ce sont eux qui
font les 30 Md€.

### Trois défauts d'appareil corrigés au passage

Le prototype de site n'avait pas de règle de génération et sortait en anomalie à
chaque contrôle. Le contrôle de l'index redoublait la liste des artefacts
délibérément hors classement, au lieu de la lire au lieu unique de l'affectation
— d'où une anomalie permanente sur la feuille de route. Et il sortait l'archive
technique en fichier non déclaré, alors qu'elle est déclarée au bloc `archives`.

**`make controle` sort désormais à zéro échec et zéro anomalie sur toute la
chaîne**, pour la première fois.

---

## 20260824 — Le référentiel des faits : annoncé, pas construit

Relevé par l'auteur et vérifié pièce par pièce. Le journal du 21 août portait
« `REF_chiffres` existe, 257 entrées ». C'était une exécution de session, pas un
artefact.

Le générateur existe et il est substantiel, 476 lignes. Tout le reste est vide :
**`sources_chiffres.py` ne porte aucune source** — le module du sourçage manuel
est en place, documenté, et son dictionnaire est vide ; **le rapprochement
`meme_que` n'est pas implémenté**, alors que A-35 l'arbitrait comme le contrôle
qui sort les discordances ; et le référentiel produit n'est versé nulle part,
l'archive technique ne portant que la doctrine, les positions et les notes.

Conséquence tenue : **les chiffres de référence ne sont pas un référentiel.** Ils
vivent rattachés à une proposition dans le `REF_doctrine` et dans les notes, sans
millésime, sans dérivation, sans source déclarée, sans niveau de confiance. Rien
ne garantit qu'un chiffre du corpus ne contredit pas un autre chiffre du corpus —
et c'est exactement le défaut que la stratégie réseaux a relevé de l'extérieur.

Deux autres mesures prises au même passage, qui corrigent des comptes annoncés
toute la journée. Le `REF_doctrine` porte **12 axes, 56 propositions, 97 effets,
57 paramètres, 21 sous-items** ; `D12` ne porte aucune proposition, et **neuf
propositions n'ont aucun effet** là où trois étaient annoncées. Le référentiel des
positions a une intégrité parfaite — zéro gagnant sans miroir, zéro perdant sans
raccroche, zéro renvoi cassé, 237 lignes sur 276 au degré « nommé » — mais **vingt
catégories sur cinquante-six ne portent qu'une ou deux lignes**, dont onze hors
rentes : écrire un apport ne réparera pas une fiche à une ligne.

L'ordre est arrêté : **les chiffres d'abord**, les apports ensuite.

---

## 20260824 — La feuille de route prend la forme de la ligne de production

Recadrage de l'auteur, et c'est le bon. Le chantier ne se décrit pas par ses
chantiers mais par **une couche de base, cinq capacités et une ligne de
production** : ce qui compte n'est pas la liste des produits, c'est la ligne. Un
produit qu'on ne sait fabriquer qu'une fois n'est pas un produit.

L'audit dans cette grille donne trois choses que la vue par livrables cachait.

**L'inventoriage a été construit trois fois sans jamais être abstrait.** Les notes
du manuscrit, les chiffres, les positions : trois structures, trois générateurs,
trois jeux de contrôles, trois vocabulaires de confiance. Le chantier général est
là — une forme d'inventaire unique, où les trois existants se rebasent et où les
suivants s'instancient. Ce qui reste à inventorier l'attend : les objections,
aujourd'hui éparpillées en trois populations de 46, 45 et 152 sans population
unique ; les entités ; les taxes et les niches ; les effets de diagnostic.

**La confrontation est un spectre de nature commune, éclaté en huit outils.** Deux
skills et six contrôles, chacun son vocabulaire de verdict, et le contrat de
projection recopié mot pour mot dans cinq skills. La robustesse ne s'obtient pas
en ajoutant des contrôles mais en n'ayant qu'une forme de chaque chose.

**La contestation a deux volets, et celui qui a de la valeur n'existe pas.** Le
volet offensif prépare la parole ; le volet introspectif corrige la doctrine. Une
objection à laquelle on ne sait pas répondre est un défaut de mesure avant d'être
un défaut d'argumentaire. Distinction à porter : angle mort **assumé**, qu'on tient
et qu'on dit, contre angle mort **ignoré**, qui est une lacune à instruire et qui
remonte au référentiel.

Deux corollaires. **La contreproposition ne s'ajoute pas aux autres capacités,
elle les compose** — découper, confronter, positionner, traduire — de sorte que
l'analyse du PLF est le produit qui traverse toute la ligne et qui dira si elle
tient ; et elle exige un véhicule que la traduction juridique ne couvre pas
encore, l'amendement. **Le site est l'inverse** : il n'ajoute aucune matière, il
expose celle des autres, et sa qualité est exactement celle des inventaires qu'il
affiche.

Consolidation du fil, pour que rien ne se perde avec le conteneur.
`generer_site.py` entre à l'appareil, la feuille de route à la méthode, tous deux
déclarés à l'index et rangés par le générateur de la carte. L'archive technique
est repliée à 31 pièces, les empreintes relevées de façon cumulative — 72
artefacts, aucun perdu — et l'ensemble versé. La skill du chantier reçoit la
tenue en dynamique et le renvoi à la feuille de route.

---

## 20260824 — Les skills reçoivent enfin la règle de nommage

La règle du nom canonique, posée le 20260821, n'était jamais descendue dans
l'outillage. Les skills nommaient leurs entrées en `Positions_AAAAMMJJ_vN.json`
et **prescrivaient d'horodater leurs sorties** : la règle était violée par ce qui
produit, pas seulement par ce qui lit. Trente-quatre renvois corrigés dans sept
skills, à l'entrée comme à la sortie ; `redaction-legistique` et
`resolution-chantier` étaient déjà propres. Chacune porte désormais un bloc qui
pose la règle et désigne l'index comme table de résolution.

Deux renvois passaient pour des manques et n'en étaient pas.
**`controle_sortie.py` existe**, 518 lignes au coffre : il était invoqué par cinq
skills et localisé par aucune, ce qui rendait inopérant leur contrôle avant
diffusion. Même chose pour `controle_arithmetique.py`. Et
`Synthèse_Calculs_Résolution_NNNN.xlsx` ne désignait aucune pièce du projet.

Une troisième piste s'ouvre sans être tranchée : **`Releve_affecte` est
peut-être reconstructible.** Le `REF_doctrine` porte des `membres: ["M-0095", …]`
sur ses propositions — les identifiants vivent dans la doctrine, c'est la couche
qu'ils désignent qui a disparu. À établir avant de la déclarer perdue : elle
bloque les tests de robustesse et les foires aux questions.

**La feuille de route est refaite à partir de ce qui existe** — les quinze
livrables demandés, la carte, l'inventaire des neuf skills. Cinq livrables ont
leur outil, trois l'ont à moitié, sept n'en ont pas ; et cinq dettes
transversales pèsent plus que les sept outils manquants, parce qu'elles rendent
inertes des outils déjà écrits. Deux corrections en sortent : la légistique est
**le mieux outillé du corpus** — trois skills, cinq fichiers de référence, un
script de diff, deux propositions de révision déjà consolidées — après avoir été
déclassée deux fois dans la journée ; et les quatre besoins tournés vers
l'extérieur ne font qu'un geste, donc un outil pour quatre livrables.

Le reste de la journée est retiré : l'inventaire des gagnants et des perdants
n'est pas le centre du chantier mais un output parmi d'autres, les cinq notes de
démonstration étaient une liste de chiffres prise aux scripts de l'agence, et les
quatre phases datées une séquence inventée. L'ordre d'un chantier se tire de ses
dépendances.

Enfin, une règle de tenue change : **les notes s'écrivent en dynamique**, dès
qu'une décision est prise, et non en un passage à la clôture du fil. Ce qui
s'inscrit au corpus ne se rapporte pas à l'auteur.

---

## 20260824 — Le chantier reprend son objet

Fin du fil de cadrage, et deux fautes relevées par l'auteur.

**Claude a qualifié un document qu'il n'a pas ouvert.** Les prétendues lacunes du
livre — un axe sans proposition, le premier axe de la doctrine sans énoncé propre,
une proposition sans gain énoncé — sont des trous du référentiel, pas du livre. Le
livre traite peut-être tout cela en prose sans que la dérivation en tire un effet
chiffrable. En avoir fait des corrections à remonter à l'éditeur, la phase
prioritaire de la feuille de route et l'objet du fil suivant, c'était violer le
garde-fou qui interdit de qualifier un document non ouvert.

Ce qui reste du chantier sur le livre est mécanique et tient en deux contrôles :
les valeurs discordantes, et les sommes qui ne tombent pas. Cela seul expire avec
le bon à tirer. Un axe vide ou une promesse mal calibrée appartiennent au
référentiel, et le livre est jugé par ses auteurs.

**Et Claude avait dispersé le centre du chantier dans un plan calqué sur celui de
l'agence.** L'auteur le remet en place : la formalisation interne de la doctrine
et de ses outils est faite ; ce qui compte maintenant est l'inventaire des
gagnants et des perdants, sa présentation au public, et le prototype de site.

C'est aussi ce que l'état du corpus disait. L'inventaire est le seul objet qui
répond à la question que tout lecteur se pose — *et moi ?* — et c'est le plus
construit : deux cent soixante-seize lignes ancrées, chacune avec son miroir et sa
raccroche. L'extrait existe et s'imprime, l'interface existe et porte déjà le
visuel du site.

**Un seul verrou commande les trois sorties, et c'est les apports.** Douze gains
sur cent quatre-vingt-douze ont le leur écrit ; les cent quatre-vingts autres se
projettent encore par une phrase du livre reprise mot pour mot, c'est-à-dire un
fragment arraché à son paragraphe et jamais une phrase adressée à quelqu'un. Tant
que ce champ est vide, l'extrait, l'interface et le site sortent du texte de livre
découpé. Ni la charte, ni le sourçage, ni l'outillage n'y changent quoi que ce
soit.

La restriction des apports aux cinq familles visées par la stratégie réseaux
tombe : une interface par situation ne peut pas laisser une situation vide. Le
coût est annoncé — environ trois cent soixante textes courts, dix unités de
travail, plusieurs fils, et c'est incompressible puisque c'est de l'écriture.

Proposé et non validé : le prototype ne publie que les familles écrites et
grandit. Une catégorie visible et vide est pire qu'une catégorie absente.

---

## 20260824 — Le livre n'est pas tout le travail, et la feuille de route se refait

Une précision de l'auteur, quelques heures après la première version, qui corrige
une déduction abusive et recompose le plan. Le livre est le point d'orgue ; ce qui
suit existe pour développer ce qu'il porte sans le dire — les calculs, les
annexes, les dispositions juridiques qu'il annonce et ne rédige pas.

**Le livre arbitre, il ne borne pas.** De « le livre fait référence », Claude
avait tiré qu'un chiffre absent du livre ne se publie pas. C'était une déduction,
non un arbitrage, et elle était fausse. Un chiffre publié qui contredit le livre
est une faute grave ; un chiffre publié qui n'y figure pas est le programme. Les
cent neuf candidats du proto Données reviennent donc dans le chemin critique :
ils ne sont pas au livre parce qu'ils sont dessous.

Une part d'entre eux expire tout de même. Sourcer cent neuf chiffres est long,
mais **vérifier si l'un d'eux contredit un chiffre imprimé est rapide et
mécanique** — le champ `meme_que` sert exactement à cela. C'est la seule part du
sourçage qui ne peut pas attendre le bon à tirer : une contradiction trouvée après
est une contradiction publiée.

**La note devient l'unité de la démonstration.** Ni page web ni volume exhaustif :
des notes téléchargeables, quelques pages, un sujet, publiées une par une. Le
public le commande — les journalistes sont la cible prioritaire, et un journaliste
ne clique pas sur une page, il cite une note. La chaîne existe déjà, la note
s'écrit en markdown et s'exporte avec les conventions typographiques ; ce qui
manque est le gabarit.

De là suit un renversement d'ordre. **La liste des notes ne se tire pas des axes
de la doctrine mais des chiffres qui vont sortir à l'écran** : la suppression de
la contribution sociale généralisée sur le travail et ses 114 milliards identifiés
ligne par ligne, le « 600 € » et la part qui en est disponible, le forfait France,
les cinq cents fortunes et les huit mois, le taux de prélèvements ramené à 36 %.

Et un renversement de séquence, tiré du plan de l'agence lui-même. Le script 2
finit par « Le détail est en lien. Vérifiez-nous. » ; la bio du compte porte « Nos
propositions ⬇️ ». Les deux pointent vers rien. **Un contenu qui appelle à la
vérification et renvoie vers le vide est plus dangereux qu'un contenu sans
source** : c'est la promesse de transparence prise en défaut, sur le seul terrain
où le dispositif se déclare imbattable. Donc la note précède le contenu qu'elle
démontre. On ne publie pas pour approfondir ensuite.

**Le site reste une vitrine.** Il présente le livre et le mouvement, les notes se
téléchargent depuis lui sans être lui. Il ne devient pas une infrastructure à
livrer avant l'ouverture des comptes.

**La légistique descend en date, non en rang.** La première version la déclassait
en accessoire de crédibilité. Elle est l'un des deux corps de la production
postérieure au livre, et son périmètre est arrêté : textes déposables complets,
révision constitutionnelle, loi organique, loi ordinaire, avec exposé des motifs.
Le corpus a de la matière — deux propositions de révision consolidées, le trois
colonnes, le récapitulatif de transposabilité, le recensement des innovations —
et rien n'est à réinventer.

Le renseignement qui commande reste le même : **la date du bon à tirer.**

---

## 20260824 — La feuille de route, refaite sur la date du livre

La question principale du registre est tranchée. Le chantier savait qu'il
travaillait sur une révision constitutionnelle, budgétaire et fiscale, et
l'ignorait de tout le reste : il n'avait jamais lu la stratégie réseaux du
29 juillet, pièce jointe du projet. Elle porte la date, le ton, le vocabulaire,
l'architecture des comptes et le plan de lancement. **L'essai « État partout,
justice nulle part » sort le vendredi 9 octobre 2026.** Quarante-six jours.

Le manuscrit du corpus est cet essai, et ce n'est pas une supposition : la
stratégie cite « 63 euros produits pour 23 euros nets récupérés » et « les 500
plus grandes fortunes couvriraient huit mois de dépenses publiques », qui sont
mot pour mot les lignes du bloc de la nation.

**Le chantier n'est pas le projet : il en est l'appareil de fiabilité.** La
signature du dispositif est la source à l'écran, et c'est son unique bouclier sur
un sujet aussi contesté que l'argent public. Tout le reste de la feuille de route
en découle.

De là vient l'arbitrage qui commande tous les autres. **Le livre fait référence,
il ne fait pas source.** Référence : entre les quatre comptes et les trois
auteurs, ce qui tranche est le livre, et un chiffre qui n'y est pas ne se publie
pas d'ici octobre, fût-il juste. Source : à l'écran, ce qui s'affiche n'est jamais
le livre, sous peine d'être circulaire — c'est ce que le livre cite lui-même, dans
ses cent quarante et une notes de fin.

Cet arbitrage désamorce ce qui paraissait le verrou du chantier. Les cent neuf
candidats du proto Données sortent du chemin critique : ils ne sont pas au livre,
donc ils ne se publient pas, donc ils attendent. `REF_chiffres` change de
fonction et devient la table qui relie un chiffre publiable à sa source externe
affichable. En revanche les onze notes chiffrées qu'aucun référentiel ne cite
deviennent urgentes : ce sont des chiffres du livre, donc publiables, et
l'appareil ne les voit pas.

**Le manuscrit est encore modifiable, et c'est la tâche qui expire.** Les lacunes
relevées depuis un mois remontent au livre maintenant ou jamais : le premier axe
de la doctrine sort sans un énoncé propre, `D12` ne porte aucune proposition, les
sous-items de `D2-2-1` totalisent 29,3 Md€ quand l'effet du même nœud en porte
12,4, et le « 600 € » est attaquable — l'agence l'a nommé, la moitié n'est pas de
l'argent disponible. Une correction faite maintenant est gratuite et définitive.
Corollaire tenu : toute correction régénère les dérivés, donc la fenêtre se ferme
avant que le stock ne se produise, sinon on produit deux fois.

Trois choses que le corpus avait déjà et que la stratégie réseaux croit
manquantes. Le pilier « L'État qu'on sauve », déclaré absent de tous les
documents, est la matière même des cinquante-sept pertes avec leur justification
et leur relais. La règle `RT-3`, reconstitution volontaire du flux, est l'antidote
exact à la faiblesse relevée sur la soustraction. Et le registre des apports —
deuxième personne du pluriel, aucune nomenclature interne, le manuscrit jamais
cité comme autorité — est déjà celui que l'agence prescrit. Le corpus et l'agence
ont convergé sans s'être parlé.

Deux déclassements, et ils vont contre l'ordre spontané. **La légistique descend
après le 9 octobre** : ni les journalistes ni le grand public ne lisent une
proposition de loi, et ce sont eux les deux publics prioritaires. **Les quatre
besoins tournés vers l'extérieur n'en font qu'un** — proposition externe,
contreproposition, PLF, actualité : un seul dispositif d'entrée, armé en octobre
pour tourner en novembre.

Un verrou tombe sans effort : la charte attendait la couverture du livre, absente
du projet. L'éditeur l'a, et l'identité visuelle est validée. La charte ne
s'invente plus, elle se récupère.

Reste une chose à savoir, et elle commande la séquence entière : **la date du bon
à tirer.**

---

## 20260824 — L'ouverture de session cesse d'être un rituel

Le coffre ne rend ses documents qu'en texte : seule une archive assez volumineuse
revient au dépôt comme fichier. Tout le reste — le manuscrit, la méthode, les
textes normatifs — repasse par le modèle à la restauration. La règle qui exigeait
de comparer à l'octet toute pièce restaurée était donc **inapplicable**, faute de
référence à quoi comparer, et elle a servi de garantie de façade.

Ce qu'elle a laissé passer, le jour même : le manuscrit rendu en squelette de
607 octets, et l'index rendu avec ses retours ligne échappés en clair. Aucun
contrôle ne les a vus. **Le corpus a une empreinte désormais** : chaque artefact
du coffre porte son SHA-256, sa taille et son compte de lignes, relevés au
versement, comparés au dépliage. Un octet de différence sort en anomalie
bloquante. Le relevé est cumulatif, de sorte qu'un fil qui ne déplie qu'une partie
du coffre n'efface pas la mémoire du reste.

Deux règles s'ajoutent, tirées des mêmes fautes. **Une restauration ne se délègue
jamais à un modèle** : c'est une copie d'octets ou elle n'a pas lieu. **On lit
avant de déplier**, et on ne déplie que ce que le fil courant demande — le fil du
jour disait de ne rien déplier, le rituel a déplié quand même.

Puis l'auteur a relevé la conclusion fausse qui avait fondé tout cela. « Le coffre
ne rend qu'en texte » avait été traduit par « un document lisible du coffre ne
peut revenir au dépôt sans passer par le modèle ». Faux : **le texte rendu est
écrit verbatim au transcript de session, sur le disque de l'atelier**, et il s'en
extrait par script. La restauration est donc toujours une copie d'octets. Un
document que la session n'a pas encore lu se récupère en le faisant lire par un
fil auxiliaire qui sert de tuyau — il lit, il n'écrit rien, le transcript garde
les octets. Dix-sept documents ont été repris ainsi, y compris ce qu'un fil mort
avait lu avant de disparaître.

Ce qui reste vrai, et c'est le point qui compte : **une restauration ne se délègue
jamais au jugement d'un modèle.** Trois voies, aucune quatrième — `cp`, le
dépliage d'une archive, l'extraction du transcript.

**Le manuscrit est au dépôt, et sa fidélité est prouvée de l'extérieur** :
l'extracteur de notes joué dessus redonne le référentiel des notes identique à
l'octet à celui du coffre, 141 notes dont 37 chiffrées.

Restait à prouver le dispositif lui-même, et c'est là qu'il a parlé. Restauré à
blanc dans un dépôt vierge puis comparé aux empreintes, il a trouvé ce qu'aucun
contrôle du matin ne pouvait voir : **sur seize documents restaurés par des fils
auxiliaires, dix étaient altérés.** Deux se voyaient. Les huit autres tenaient
dans un à trois octets — et deux d'entre eux étaient une réécriture du texte :
« Version » devenu « Vers », « Employer » devenu « Employé », dans les règles de
rédaction du corpus. Trois versements avaient propagé la corruption au coffre.

Tout est recousu depuis la version mécanique, patch des éditions appliqué par
`patch` et non à la main. **Le corpus est propre et il est prouvé propre** :
restauré à blanc, il ne porte plus qu'une divergence, celle d'un dérivé qui
horodate son pied de page et se régénère.

La leçon tient en une phrase. Les empreintes du matin avaient été relevées sur les
faux, et affirmaient donc que tout allait bien. **Un contrôle qui ne s'exerce que
sur le dépôt courant ne prouve rien** : il faut restaurer à blanc et comparer le
coffre à lui-même.

---

## 20260824 — Le référentiel des faits, reprise

Trois choses que le fil précédent avait posées en questions alors qu'elles se
tranchaient. **La répétition d'un chiffre n'est pas une faute** : un chiffre
énoncé trois fois au corpus fait trois entrées, et le référentiel sert à dire
qu'elles concordent. Le contrôle qui relevait « la même valeur dans deux
provenances » disparaît, et le rapprochement de deux entrées s'écrit désormais à
la main — deux nombres égaux ne parlent pas forcément de la même chose.

**Une source se transmet à l'intérieur d'une proposition.** Un sous-item vient du
même décompte que l'effet auquel il se rattache : les vingt-cinq chiffres qui
sortaient sans source sont sourcés, et il ne reste à sourcer que les cent neuf
candidats du proto Données. Ils se reprendront par lots, et **les corrections
devront repasser dans les produits** qui citaient ces chiffres.

**Les notes de fin sont de la doctrine.** L'auteur le tranche : leur énoncé a sa
place au référentiel des faits, au même titre qu'un énoncé du corps. La règle qui
interdisait d'y porter le texte d'une note tombe pour ce qui se régénère, et
continue de valoir pour ce qui s'écrit à la main.

Reste la question principale, et la seule qui revienne à l'auteur : à quoi sert
ce chantier dans les six prochains mois, et dans quel ordre. L'appareil est
propre, la production est vide, et la feuille de route parle encore d'un autre
projet.

---

## 20260821 — La procédure de travail rattrape le partage du travail

La skill du chantier portait encore la conduite d'avant : une question fermée à
la fois, et un feu vert avant chaque génération. Elle est réécrite. Le partage du
travail passe en tête, avec ses quatre garde-fous, et la validation préalable
généralisée disparaît — **demander un feu vert pour de la tambouille devient une
faute, au même titre que trancher seul une question de fond.**

Quatre acquis récents y entrent, qui n'y étaient pas : le classement par contenu
et le lieu unique de son affectation, les documents que nul script ne restaure,
le contrôle du dépliage à l'octet, et le référentiel des faits avec ses quatre
niveaux de confiance et l'interdiction de sortir un chiffre non sourcé.

La skill est en lecture seule en session : elle est livrée, elle ne prend effet
qu'enregistrée.

---

## 20260821 — Le référentiel des faits paraît, et déclare ses trous

Le plus lourd des manquants tombe. `REF_chiffres` existe : un chiffre par
entrée, avec sa valeur, son unité, son millésime, sa source, sa dérivation, ses
déclinaisons, son code d'origine et son niveau de confiance. Deux cent
cinquante-sept entrées, relevées de trois lieux — cinquante-neuf des notes de fin
du manuscrit, quatre-vingt-neuf du référentiel de doctrine, cent neuf du proto
Données. Le sourçage écrit à la main vit à part et survit à chaque régénération,
comme les justifications et les apports du référentiel des positions.

**Ce référentiel vaut d'abord par ce qu'il déclare ignorer.** Cent trente-quatre
entrées sur deux cent cinquante-sept sont sans source, les cent neuf candidats du
proto comprises. Aucune n'a été comblée. Le relevé ne devine ni unité, ni
millésime, ni source : il prend ce que le corpus écrit, et laisse le champ vide
quand le corpus ne l'écrit pas. Soixante-seize entrées sont sans unité, deux cent
vingt-cinq sans millésime, et cela se lit.

Quatre niveaux de confiance, et une distinction qui compte : **une opération
rejouée dit que le compte est juste, non qu'il est sourcé.** Elle vaut un
ancrage, jamais une source. De la même logique, l'ancre d'un nœud de doctrine
n'est pas une source, et l'unité que le proto déclarait en attribut de ligne ne
se rapporte pas d'office à la valeur de tête.

Le contrôle du référentiel des faits entre à la chaîne. Il vérifie que les
candidats restent tous à confiance nulle, qu'aucune confiance ne s'écarte de ce
que les champs portent, qu'aucune source écrite à la main ne vise une entrée
morte — et il relève seize valeurs qui apparaissent dans deux provenances à la
fois. Ce dernier relevé est le plan de travail : le corpus dit le même nombre
deux fois, et lequel fait foi reste à trancher, entrée par entrée.

---

## 20260821 — L'atelier reprend la carte, et le trois colonnes se vérifie

La carte redevient un dérivé. Son générateur porte désormais la table des onze
familles, l'index en importe le champ `famille`, et la version régénérée est
identique à celle qui avait été écrite à la main — au seul bloc de dette
technique près, qui tombe puisque la dette est payée. Un contrôle de plus refuse
un artefact que le classement ne range nulle part.

L'index cesse de dépendre de ce qu'un conteneur contient. Les sources se
déclarent au lieu de se relever de l'arborescence : une pièce jointe non
restaurée y disparaissait sans bruit. Vingt documents portent l'aveu qu'aucun
script ne les remet à l'atelier — les dix-sept pièces jointes du projet, et trois
documents binaires que le coffre porte comme documents et non comme octets. Les
deux pièces mortes de la veille sortent. Le renvoi du guide de légistique se
résout par alias sur sa digestion, et `REF_chiffres` entre enfin aux manquants
déclarés, où la carte le nommait déjà seule.

**Le trois colonnes porte bien le texte projeté, et non le texte nu.** Vérifié
fichier ouvert, Constitution et LOLF. Deux corrections en sortent. L'ordre des
colonnes est texte actuel, réforme visée, rédaction révisée : le projeté est en
troisième colonne, la justification en deuxième — la formule qui circulait
inversait les deux dernières. Et la première colonne n'est un verbatim entre
guillemets que pour vingt-six blocs sur trente-sept à la Constitution, vingt-et-un
sur vingt-neuf à la LOLF ; ailleurs c'est un résumé, juste pour un article
nouveau, trompeur pour un article existant. Le point de vérité du texte en
vigueur reste donc le texte nu de référence, et la carte le dit.

Un incident de restauration, qui vaut règle. Le coffre ne déplie par script que
son archive technique ; tout le reste repasse par le modèle, et la recopie du
manuscrit a rendu cent espaces insécables en espaces ordinaires, dans les
montants et les pourcentages des notes de fin. Rien n'a été versé, la copie a été
refaite et contrôlée à l'octet. Deux règles portées à la localisation et aux
instructions permanentes : toute pièce restaurée se compare avant emploi, et rien
de recopié ne se reverse.

Les vingt documents hors atelier n'ont pas été ouverts dans ce fil. Leur famille
est celle de la carte validée la veille, non une qualification nouvelle.

---

## 20260821 — Le corpus se classe par contenu

La question ouverte est tranchée, bloc à bloc. Trois surfamilles commandent
désormais la lecture du corpus — ce qui entre, ce avec quoi on travaille, ce qui
sort — et neuf familles dessous. La doctrine reçoit ses annexes : les huit
classeurs et les précédents restes à payer font vérité au même rang que le
manuscrit pour ce qu'ils décomptent.

Ce que le chantier a appris vaut plus que le rangement. **Une matière de fond et
le document qu'on en tire sont deux artefacts** — trois occurrences le même jour,
le texte à trois colonnes et les propositions de loi, les candidats chiffrés et
la page qui les rédige, l'analyse de transposabilité et le récapitulatif
externalisé. L'ancien rangement les fusionnait sous une même étiquette
d'archive. De là suit la promotion : ce qui monte de la sortie vers l'entrée,
c'est le document gelé, jamais la matière qui l'a produit.

Cinq autres règles s'écrivent. Où passe la frontière entre une référence et une
méthode — vérifiable au dehors, ou décidé par nous. Comment une source externe
entre au corpus : par sa digestion, qui cite ses autorités, jamais par son
fichier. Ce qu'un document externalisé interdit de réécrire. Quel dérivé mérite
le coffre : celui que l'auteur lit, non celui que la machine relit. Et qu'un
travail non relu, si abouti soit-il, reste au bac à sable.

**Le classement est une vue, et les adresses ne bougent pas.** Déplacer un
document du projet suppose de le recopier entièrement : le manuscrit et les
textes normatifs passeraient par le modèle, et une dérive de recopie corrompt la
strate 1 en silence. La carte porte donc les neuf familles et donne pour chaque
document son adresse réelle. Règle générale : un document ne se déplace, ne se
réécrit et ne se reformate que si sa recopie ne risque pas de le déformer.

Ce que le classement rend visible, et que l'ancien masquait : cinq artefacts en
sortie, dont aucun ne passe les contrôles en l'état. La surfamille la plus pauvre
du corpus est celle qui en est le grand objet. Les quatre documents finis de
juillet et août redescendent en matière : leur texte tient, leurs chiffres n'ont
jamais été confrontés au référentiel.

Un manquant de plus, le plus lourd. `REF_chiffres`, référentiel des faits, n'a
jamais été produit — spécifié en août, jamais construit. `REF_doctrine` en assure
une part, celle des chiffres rattachés à une proposition, sans millésime ni
dérivation ni confiance. Les chiffres de diagnostic autonomes et les données des
classeurs restent sans point de vérité unique. Un manquant de moins en revanche :
le guide de légistique n'est pas perdu, il est digéré dans `structure_ppl`, qui
bascule des références vers la méthode.

Deux pièces mortes sont supprimées, le bootstrap et l'ancien script de contrôle.

Reste ouvert : le générateur de la carte, qui ne sait pas produire les neuf
familles ; la vérification que le trois colonnes porte le texte projeté. Prochaine
étape, la feuille de route, avant la rentrée.

---

## 20260821 — Le registre des arbitrages s'ouvre

Les décisions ont enfin un lieu. Huit entrées, validées : le projet comme coffre,
la fin des horodatages, la délégation de la mécanique des renvois, les trois
statuts de propriété avec le contenu qui commande le format, un coffre réduit à
l'input, l'output et les briques de production, le cas par cas sur les sorties
gelées, le cadrage actif des fils, et la primauté du rythme sur l'approfondissement.

Une question qui figure au registre ne se repose plus. Trois restent ouvertes et
sont nommées comme telles : la feuille de route périmée, le classement par
contenu, la couche de preuve absente.

---

## 20260821 — Le coffre rangé par dossiers

Le coffre cesse d'être une liste plate. Quarante-trois documents en sept
dossiers. Le rangement du coffre ne suit pas celui du dépôt, où `sources/` reste
plat comme copie de travail ; la correspondance se lit au champ `chemin_coffre`
de l'index.

L'appareil et les référentiels tiennent désormais en un document unique plutôt
que deux. Les dix-sept pièces jointes du projet restent une liste plate : Claude
n'a pas la main sur elles, et seule la carte leur donne un ordre.

---

## 20260821 — Carte du projet, et repli de la couche technique

Le coffre devient la vue de l'auteur, et cesse d'être un dépotoir technique. Les
vingt-et-une pièces de l'appareil et les trois référentiels se replient en deux
archives opaques ; ne restent visibles que dix-huit documents, un par chose qu'on
peut ouvrir. Le pliage et le dépliage sont réversibles à l'octet, vérifié.

La carte du projet paraît : un fichier unique qui dit tout ce que le chantier
porte, sous quel statut de propriété, spécifié par quoi, et ce qui manque.

Les modalités de travail sont enregistrées en transversal, hors du corpus : une
skill `resolution-chantier` qui porte la procédure opérationnelle, et un bloc
court destiné aux instructions permanentes du projet. Trois propriétés de fichier
sont arrêtées — l'input de l'auteur en lecture seule, les travaux de Claude
régénérables, les outputs communs soumis à validation.

---

## 20260821 — Coffre, index et fin des horodatages

Le corpus reçoit un lieu de survie et une table de résolution. Le projet Claude
devient le coffre : le corpus vivant y est versé sous ses chemins canoniques, et
les soixante documents à plat horodatés qui le doublaient sont retirés.

La règle de nommage change : un nom canonique par artefact, aucun horodatage,
l'historique dans git et dans ce journal. `methode/index.json` porte pour chaque
artefact son rôle, son chemin, son générateur, ses consommateurs et les noms
horodatés qu'il remplace, de sorte qu'un renvoi ancien résout encore.

Trois pièces perdues rentrent : le générateur de l'arbre de lecture, le relevé
lisible des notes devenu dérivé — cent quarante et une notes, dont trente-sept
chiffrées — et la dérivation de l'axe D2. Quatre renvois de skills qui ne
résolvent nulle part sont nommés comme manquants.

---

## 20260820 — Bascule du projet en dépôt

Reprise du corpus au terme du fil « premier extrait lisible » : référentiel de
doctrine corrigé, référentiel des positions doté de l'éventail, des groupes, des
promesses et des champs rédigés côté gain, extrait et interface régénérés dessus.
Douze apports rédigés, tous ceux du travailleur, qui servent de référence de
registre. Cent quatre-vingt-deux gains restent en régime transitoire.

## Sections sans fragment, reprises à l'historique le 20261001

*Ce journal a été supprimé du projet le 20261001 sur une présence au dépôt qui
n'existait pas, puis retrouvé le même jour et remis ici — identique à l'octet,
sha256 `faad6e948ae0fffe007c3a1f15b7da53954ebb623059b7c47a4684a787a5de1e`,
295 275 o, 4 875 lignes. Tout ce qui précède est son contenu d'origine, repris
verbatim et jamais repassé par le modèle.*

*Les sections ci-dessous étaient sous la ligne de marque, mais les fragments qui
les avaient produites ne sont plus au coffre : un assemblage les aurait
effacées. Elles sont remontées ici, où rien ne les réécrit.*

## 20260917 — ecart-classeurs

**Sept classeurs mis au propre sont entrés au projet, l'écart avec les six
antérieurs est mesuré, et l'appareil est rebranché dessus.** Les classeurs du
20260917 sont désormais la source officielle, seuls.

**Ce qui ne bouge pas.** Les 278 lignes de taxe affectée, les 465 dépenses
fiscales et leurs huit feuilles, les 184 opérateurs, les 777 ODAC-ODAL, les 202
lignes de mission et de programme, les onglets PAP et RAP : **0 divergence de
valeur**, cellule à cellule. 8 119,670 / 9 802,722 / 17 922,392 M€ de taxes
restituées ; 465 dépenses fiscales, 89,406 Md€ de réalisation, 43,126 de gage ;
434 opérateurs, 1 104 agences, 479 514 emplois. Le total des économies reste
236,054667 Md€ et le gain en année 1 reste 127,352167.

**Ce qui bouge.** L'arbre des économies gagne +4,8 Md€ d'État (77,7 → 82,5) et
+13,9 sur les collectivités (39,5 → 53,4). **La cause est mesurée et la règle
est arrêtée** : une économie de masse salariale se restitue en totalité, 30 % en
année 1 et 70 % au solde, là où seuls les 30 % étaient comptés. Le rapport est
exact — 0,300000 — sur les trois lignes qui le portent. La capitalisation baisse
de 636,100143 à 606,972666 Md€ et son taux de rendement passe de 2,9 % à 3 %,
ce qui referme le premier des deux écarts que la grille relevait entre
l'hypothèse annoncée et l'hypothèse appliquée.

**Ce qui disparaît.** Les onglets `Manifeste` et `Perdants`, sans équivalent, et
le bloc des postes nommés de l'onglet `Synthèse` des dépenses, dont 18 postes sur
22 ne se retrouvent nulle part.

**L'appareil.** `socle_budgetaire.py` lit désormais les classeurs du 20260917 :
trois onglets en ` R`, `Chiffrages Résolution`, `Flux`, et la couche budgétaire
répartie entre `Economies R` et `SynthèseR`. La clé d'un poste nommé devient une
adresse de cellule. Le Makefile cesse de sauter en silence quand un classeur
manque. **`S17` est neuf** — la restitution salariale, vérifiée exactement — avec
son jeu de fautes et son jeu de justes : huit codes levés, six silences, zéro
défaut.

**Les bouclages sur les nouvelles pièces.** `S1` à `S7`, `S9`, `S10` et `S17`
passent. **`S8` rend 30 bouclages sur 32** : les deux échecs sont France
Compétences et le CNC, dont la part budgétaire n'est plus écrite nulle part. Ils
ne se corrigent pas. `S11` à `S16` restent injouables — le module est en dette au
dépôt et cinq de leurs six onglets sources ont disparu.

**Le référentiel des chiffres.** 257 entrées, 93 sans source, 0 échec au
contrôle, 57 calculs rejoués justes. Neuf des 45 sources écrites à la main citent
une adresse qui n'existe plus ; aucune n'a été réécrite.

**Le classeur des graphiques est une extraction** : 2 151 valeurs sur 2 162
viennent des douze onglets `Graph…` de l'ancienne synthèse, 11 sont inédites.

**Ordre des lots, corrigé par l'auteur** : après ce fil viennent **les parties
faciles de la liasse**, et **la sortie des fonctionnaires en dernier — c'est un
bloc juridique.**

**Reste ouvert** : six questions de fond à `methode/a_trancher.md`, et le paquet
de dépôt `methode/paquet_depot_ecart_20260917.md`, à pousser depuis
claude.ai/code après le second cercle du socle.
## 20260917 — fil-application

**Le lot C gagne son garde-fou, et les termes manquants trouvent leur source.**
Les montants des bilans de blocs, recopiés à la main dans `blocs.json`, sont
désormais confrontés aux paramètres des énoncés : série `D1` à `D3` de
`controle_blocs.py`, éprouvée sur un jeu de fautes et un jeu de justes. Une seule
anomalie au corpus sain, et elle est réelle — `B-07` citait 108,56 Md€ que le
paquet ne porte nulle part.

Les sept bilans déséquilibrés sont instruits : dix termes, **3 portés, 6 estimés,
1 absent**, chacun avec son onglet et son bouclage quand il en a un. La grille de
lecture budgétaire a été rejouée sur les annexes courantes — dix bouclages sur
dix, zéro échec. Cinq des six termes estimés le sont pour la même raison : leur
onglet n'est pas importé au socle. Les importer ferait basculer cinq verdicts
sans produire un chiffre neuf.

**Les fichiers cumulatifs cessent d'être un goulot.** Un fil ne les écrit plus :
il dépose un fragment daté que `appareil/fragments.py` assemble, idempotemment.
Deux fils peuvent désormais travailler en parallèle sans qu'aucun n'écrase
l'autre. C'est la question 17 tranchée, et ce fragment en est le premier emploi.
## 20260917 — socle

**Second cercle du socle budgétaire.** Six onglets importés, sept bouclages
neufs, zéro valeur produite. `Fusion taxes`, `CI unique`, `CSG`, `Perdants` et
`GraphAFU` au classeur de calculs ; `Figure 9.1` au classeur DEPP de l'état de
l'École, qui n'avait jamais été ouvert. `Gages` était importé depuis l'origine et
comparé à rien : il l'est désormais.

`controle_socle.py` passe de dix bouclages à dix-sept, tous verts.
`appareil/epreuve_controle_socle.py` est neuf : quatorze fautes qui lèvent toutes
leur code, sept justes qui ne lèvent rien. `make controle` joue les deux.

**Ce que la confrontation a rendu, et qui vaut plus que les comptes** : les deux
têtes de l'onglet `Gages` retrouvent les deux têtes de l'arbre des économies,
colonne par colonne — 44,0 / 33,7 / 77,7 pour l'État, 33,3 / 6,1 / 39,49 contre
39,5 pour les collectivités. Le même chiffrage est écrit à deux endroits par deux
chemins, et les deux disent la même chose.

**Relevé de comblement mis à jour.** Cinq termes passent de `estimé` à `porté` —
la contrepartie du solde de `B-05`, le coût brut de `B-06`, le perdant de `B-07`,
les rendements de `B-09`, la dépense remplacée de `B-15` — et le total de
`B-07` passe de « porté en composantes » à « porté en total ». Il reste **un
terme estimé**, la dotation par enfant de `B-15`, et son motif a changé : ce
n'est plus un défaut d'import mais une absence de dérivation, donc un travail de
chiffrage et non d'appareil. **Un terme à produire**, la reprise par l'État des
missions de solidarité départementales.

**L'origine du « 108,56 Md€ » est au socle** — onglet `CSG`, ligne « Données
2024 », colonne CSG, contre 114,46 pour CSG + CRDS activité. Le contrôle `D2` de
`controle_blocs.py` le sortait sans origine déclarée ; la correction appartient au
fil qui rouvre les blocs.

**Deux écarts affichés et non comblés.** À l'onglet `Perdants`, les quatre têtes
écrites font 65,4 M contre 68 M de résidents : 2,6 M ne relèvent d'aucune tête, et
l'onglet ne prétend pas partitionner la population. À la tête « Economies Etat »
de l'onglet `Gages`, le gain indirect vaut 33,7 quand ses six détails font 33,9 :
la tête vient de l'arbre, non de son propre détail, et l'écart tient dans les
arrondis d'affichage.

**Quarante-cinq artefacts du coffre étaient absents de la table curée de
l'index** — seize déjà à l'index, vingt-neuf nulle part. Portés en un passage.
L'index passe de 252 à 287 artefacts, `make reindex` n'en perd plus aucun, et
`controle_index.py` sort zéro anomalie bloquante. Une règle de classement par
dossier est ajoutée à `generer_carte.py` pour que le cas ne revienne pas.

**Deux motifs du fichier de construction ne trouvaient plus leur classeur** —
celui du budget général et celui des calculs — sans que rien ne casse. Corrigés.
Le classeur DEPP entre au fichier de construction sous `PLF_EDUC`.

**Reste ouvert.** Le compte éducation, 6 600 € par an, est un paramètre posé
qu'aucune dérivation du corpus ne produit. Les déflateurs de la série d'éducation
antérieurs à 2024 sont chaînés et non vérifiables à la feuille. L'assiette de
1 561 Md€ sur laquelle reposent les deux taux implicites d'impôt sur le revenu
n'est écrite nulle part à l'onglet `CI unique` : le bouclage vérifie seulement que
les deux reposent sur la même.

**Correction du jour, après relecture de l'auteur.** Le prompt du lot suivant
écrit par ce fil est ramené à *proposé, non validé* : désigner le lot suivant
n'est pas de son ressort. Ses deux arbitrages internes sont ressortis en
questions 23 et 24 du registre à trancher.
## 20260921 — digestion-archives

**Les trois pièces en attente de décision de retrait sont vérifiées, et aucune
ne se retire.** `livrables/digestion_archives_20260921.md`.

**La réserve d'arguments est à garder** — 167 unités, **3 digérées, 1 reformulée,
163 absentes**. C'est cohérent avec son propre critère de sélection, qui était la
nouveauté contre le corpus au 20260806 ; rien n'y est entré depuis, le travail
des cinq dernières semaines ayant porté sur le budgétaire, la norme et la
légistique. Fait qui pèse au-delà des cases : **`appareil/relever_protos.py`,
module vivant, prend cette pièce en entrée** — son en-tête nomme « une réserve
d'arguments » et son usage lit `../sources/*.html`. La retirer retire une entrée
à un contrôle en service. A-128 posait déjà la question sur cette pièce, la plus
lourde des gelées à 92 ko ; A-6 y répond.

**L'input gagnants-perdants est à garder** — 52 unités dont une sans contenu,
**39 digérées, 12 absentes**. La dérivation du 20260820 a fait son travail : les
catégories de l'input sont nommées au bloc `CATEGORIES` de
`construire_positions.py`, et deux unités y sont citées comme venant de lui —
`C-38` porte « input brouillon : environ 12 % des élus, non instruit ». **Le seul
manque structurel est le résident étranger** : quatre des douze absentes en
relèvent, et le référentiel des positions ne porte aucune catégorie d'étranger du
côté gain — `C-44` n'existe que comme perdant de l'AME. Les huit autres sont
ponctuelles : l'État plus riche à une génération, les grands sujets de société
hors contrainte étatique, le doublement du salaire en vingt ans, le choix laissé
au salarié sur les chèques, les « près de deux cents impôts », la robustesse de
l'entreprise, la transition de dix-huit mois au chômage, le travail après l'âge
minimal sans cotisation.

**L'archive des arbitrages est une copie unique, et elle n'est pas dormante.**
Le dépôt a été cloné : sa sous-racine `chantier/` ne porte que `appareil/`,
`referentiels/`, le `Makefile` et le `.gitignore` — aucun `.md` de méthode, rien
dans l'historique. Le coffre est son seul porteur. Et **51 des 99 renvois `A-nnn`
cités dans les modules vivants du dépôt ne résolvent que par elle**, dont `A-35`
et `A-57`, que l'en-tête de `relever_protos.py` donne pour la raison d'être de
son dispositif. Une copie unique ne se retire pas.

**La vérification est mécanique, trois passes** : 5-grammes littéraux sur le
texte normalisé, trigrammes de mots pleins, co-occurrence des deux termes les
plus rares de chaque unité dans une fenêtre de 500 caractères. Ce que les passes
sortent est ensuite lu une à une. Le corpus vivant interrogé est le manuscrit,
`REF_doctrine`, `notes_manuscrit`, les 89 modules d'`appareil/` et le `Makefile` ;
`positions.json` n'étant ni au coffre ni au dépôt, il a été lu par ses
générateurs — `construire_positions.py`, `justifications.py`, `apports.py`.

**Rien n'a été digéré, réécrit ni retiré.** Le retrait est une action
d'interface, à la main de l'auteur, et les trois verdicts disent qu'il n'a lieu
sur aucune des trois.
## 20260921 — etat-site

**Produit** : `livrables/etat_site_20260921.md`, trois relevés — ce que le site
porte, ce qui est disponible pour l'augmenter, ce qui manque et qui le fournit.
Aucune page, aucun gabarit, aucun texte rédigé, aucun chiffre mis en forme.

**Constat qui commande la suite.** La refonte de la chaîne du site, décrite par
`methode/passation_site.md` le 20260904 — couture `referentiels/donnees_site.json`,
produite par `appareil/exporter_site.py`, lue par `appareil/generer_site.py`,
un seul chemin de code ici et au dépôt — **n'est pas au dépôt du corpus**.
Mesuré sur le clone `Resolution-2027` au commit `8dbe040` du 20260917 : les deux
premières pièces sont absentes, et `generer_site.py` y est la version antérieure
à la refonte, celle qui lit `positions.json`, `REF_doctrine.json` et le proto
1-pager et écrit 26 fichiers. Le `Makefile` appelle cette version. Elle ne
connaît ni `fiches.html`, ni `videos.html`, ni `manifeste.pdf`, tous trois
servis. **Le partage « le fond ici, la forme au dépôt » n'est pas opérant depuis
le corpus.**

**Non ouvert, et donc non qualifié** : le dépôt `resolution-ib-dev/Site-ETNP`,
privé, clone refusé depuis l'atelier. Les constats sur le site portent sur les
pages servies, relevées une par une le 20260921.

**Autres constats.** `resolution_une_page.html` est servi et lié de nulle part.
La fiche consommateur porte encore « et à meilleur prix » à la ligne *Le choix*,
signalée non tranchée le 20260904. La rubrique *Vidéos*, déclarée sans
destination par la chaîne du corpus, mène en ligne à une page réelle.

**Matière relevée pour les sept entrées.** Extrait d'ouverture : complet
(`livre/texte_livre.json`, EP3 verbatim, prologue au folio 7). Bios : texte
complet au livre, folios 173-177 ; **photos absentes du corpus**. Notices :
141 notes de fin sur 67 sections, tri et classement à faire. Classeurs du
20260917 : présents et mesurés, **non publiables en l'état** — état faisant foi
non déclaré, `socle_0910.py` en dette, 5 bouclages de S8 en échec, S11 à S16
injouables, 9 sources citant un onglet disparu. Graphiques : 12 onglets de
données, aucun rendu. Cartes : D2, D3, D7 et les onglets correspondants, pas de
gabarit.

**Reste ouvert, porté au document et dû à `methode/a_trancher.md`** : le plan de
la vitrine augmentée, le sort de `resolution_une_page.html`, la formule de la
fiche consommateur, et le rapatriement ou non de la chaîne de rendu.

*Le mandat de production n'est pas ouvert par ce fil : il nommera les pièces une
par une, et il est de l'auteur.*
## 20260921 — purge-a-trancher

**Quatre questions tranchées par l'auteur, trois arbitrages du 20260917 portés
au registre, et `methode/a_trancher.md` purgé d'autant.** Sept entrées neuves au
registre, `A-413` à `A-419`.

**Le vocabulaire bascule** *(question 26)*. `methode/grille_lecture_budgetaire.md`
est réécrit sur les termes du 20260917 : vingt et un remplacements, un tableau
de concordance en tête qui dit d'où l'on vient, et plus aucun ancien terme dans
le corps — hors un renvoi délibéré vers `appareil/socle_0910.py`, qui porte
désormais les libellés antérieurs avec les adresses de la même génération. **La
bascule porte sur le vocabulaire, pas sur les adresses** : celles-ci restent
notées avec leur état antérieur, parce que l'adaptateur en dépend.

**Les deux écarts de valorisation du patrimoine sont clos** *(question 27)* :
3 % de rendement, 600 Md€ à restituer sur 606,972666 valorisés, et la marge de
6,97 Md€ est la prudence assumée. La grille ne les relève plus.

**`Manifeste` et `Perdants` : la mesure a changé la réponse** *(question 29)*.
La consigne était de garder le contenu ; il l'est déjà, intégralement, à
`livrables/extrait_classeurs_anterieurs_20260917.md` — recopie cellule à
cellule, 35×13 et 16×8. Ce qui restait n'était pas une extraction mais une
déclaration : ce document est le porteur durable, et `S15` comme les deux
entrées de `REF_chiffres` qui citaient `Manifeste` s'y sourcent désormais.
*Rejouer l'extraction aurait produit une seconde copie du même chiffre.*

**La doctrine reprend 82,5 et 53,4, en une passe dédiée** *(question 30)* :
manuscrit, fiches et site basculent d'un coup, non au fil des régénérations. Le
total général ne bouge pas — 236,054667 Md€. **Cela ouvre un lot, dont le mandat
est de l'auteur** ; ce fil ne se donne pas son successeur.

**Les trois arbitrages du 20260917 en attente sont emportés.** Ils restaient à
`methode/a_trancher.md` tant que la question 17 n'avait pas donné sa règle de
concurrence ; elle l'a donnée — écriture par fragments — et ce fil est le
premier à écrire au registre après elle. Ils y sont, datés de leur arbitrage.

**Quatre questions de plus tranchées par l'auteur, et l'une d'elles annule sa
propre catégorie.** `A-420` à `A-423` au registre.

**Le « nœud de mise en œuvre » n'existe pas comme objet** *(question 23)*.
Interrogé sur sa forme, l'auteur ne reconnaît pas le terme : ce sont des blocs
de travail juridique à venir, préidentifiés, et rien de plus. Pas de famille
d'artefacts, pas de gabarit, pas de contrôle de gabarit.
`methode/prompt_fil_noeud_mise_en_oeuvre.md` est caduc.

**Et il faut le dire net : le terme était de nous.** Il est né le 20260917 dans
un prompt de Claude marqué *proposé, non validé*, et `a_trancher.md` portait
quatre jours plus tard « le nœud de mise en œuvre existe comme objet — tranché
par l'auteur ». **L'attribution était douteuse**, et `A-418` est réduit à ce qui
tient : un chantier à la fois, la sortie des fonctionnaires d'abord, « sept »
restant une estimation que le corpus n'a jamais énumérée — il n'en nomme que
deux. *Un concept forgé par un fil pour son usage se lit comme du vocabulaire
acquis dès le lendemain.*

**`Capitalisation` s'importe au socle avec son bouclage** *(question 24)* :
l'horizon de sept ans cesse d'être `estimé`. Lot d'appareil à venir, jeu de
fautes et jeu de justes compris.

**La part budgétaire de France Compétences et du CNC se retire** *(question
28)* : « on peut retirer, on reconstruira au besoin ». Les deux bouclages de
`S8` qui la visaient sont retirés, non laissés en échec. Le chiffrage garde 10,6
et 1,3 Md€, et sa décomposition s'arrête aux taxes.

**`S16` garde son millésime** *(question 31)*. L'absence de successeur au
20260917 n'est pas un retard.

**`methode/a_trancher.md` descend à six questions ouvertes** — 11, 21, 22, 32,
plus les blocs de procédure A.1 à A.6 et de méthode de lecture B.7 à B.16.
## 20260921 — rapprochement-proto

**Les 93 candidats du proto Données sont rapprochés du corpus un par un. Le fil
lit et rapproche ; il ne calcule pas, il n'ouvre aucun classeur, il ne corrige
aucune valeur.** Livrable : `livrables/rapprochement_proto_20260921.md`.

**Le compte.** 93 candidats instruits — `concordant` 8, `contradictoire` 2,
`divergence d'hypothèse` 5, `sans vis-à-vis` 78. Six avaient déjà un
rapprochement écrit le 20260921 ; **les 87 autres étaient non instruits, et le
sont**. La règle du sous-jacent est donc opposable sur la totalité du proto : ce
qui ne contredit pas la doctrine se conserve, et on sait maintenant de quoi il
s'agit.

**Les deux contradictions sont closes le jour même par l'auteur** — *le livre et
ses annexes prévalent* —, et elles ne se referment pas de la même façon.
`P-D-102` — 540 000 agents et 9 % contre 580 000 postes et −10 % — est **écrite
et jouée** : le groupe `postes publics facultatifs supprimés` porte le candidat
et un bloc `arbitrage`, `F7` reste vert, l'écart reste visible au contrôle.
`P-D-067` — 106 Md€ contre les « environ 125 milliards d'euros par an » du corps
du livre — est close au fond et **reste inécrivable** : les 125 Md€ ne sont
entrés dans aucune entrée, et un groupe `MEME_QUE` apparie des entrées. Elle
attend que le corps du livre entre au référentiel, ce que la question 33 a déjà
décidé.

**Une divergence d'hypothèse était connue, quatre ne l'étaient pas.** `P-D-101`
— 950 €/an sur douze ans contre « au moins 500 € par an » sur vingt-quatre à la
note e119 — était relevée. S'y ajoutent `P-D-066`, taux de couverture des
retraites à 73 % au lieu de 69,3 %, qui vit sur le périmètre de dépense écarté le
20260825 ; `P-D-035`, 431 opérateurs du PLF 2026 contre 434 agences nationales du
décompte arrêté des 1 104 ; `P-D-002`, la dépense publique à 50 % du PIB sur
l'assiette PO + CI + bouclier + déficit contre les 57 % du manuscrit.

**Deux rapprochements neufs, écrits et éprouvés.** `P-D-108` rejoint le groupe de
la hausse des salaires nets, que le manuscrit porte pour les enseignants en
P3-C4 ; `P-D-095` et la note e15 portent le même prélèvement forfaitaire unique à
30 %. Avec l'arbitrage des effectifs, le patch est joué sur le clone : `MEME_QUE`
passe de 25 à 26 groupes, le référentiel de 53 à **57** entrées rapprochées,
`controle_chiffres.py` sort **`0 échec`**, 2 discordances arbitrées et aucune
discordance de valeur. Il est au paquet
`methode/paquet_depot_rapprochement_20260921.md` et **il ne se pousse pas d'ici**
(A-393).

**Un troisième rapprochement a été écrit, joué, et retiré.** « Population de la
France » — `R-D7-2-1-p1` et `P-D-026` — semblait concordant : 68 M au corpus,
68,6 M au 1er janvier 2025 au proto. Joué, le groupe sort en `DISCORDANCE` et ne
passe qu'avec une **tolérance posée à 0,6 M**. La question 15 dit ce que vaut une
tolérance posée, et le 20260917 elle avait déjà masqué trois lignes de taxe
affectée. **Groupe retiré, `P-D-026` reclassé en divergence d'hypothèse** : le
corpus ne date pas sa population, le proto la date.

**Ce que le sous-jacent rapporte, mesuré sur trois cas.** `P-D-079` chiffre les
trois postes que la note e129 nomme sans les chiffrer, et leur somme redonne
`N-e129-1`. `P-D-061` et `P-D-062` décomposent les 30 Md€ de `R-D8-3-1-e2`.
`P-D-099` porte le calcul des « +25 % d'offre locative privée » de
`R-D7-3-1-e1` — 1,77 M de logements remis sur 7,2 M de parc privé. **C'est
exactement ce que l'arbitrage du 20260921 appelle source de source, et c'est le
rendement net de la conservation du proto.**

**Quatre divergences internes au proto sont relevées, aucune tranchée** : les
mutuelles à 32,5 puis 41 Md€, les revenus déclarés à 1 457 puis 1 466 Md€, la CSG
hors activité à 14 Md€ quand la différence en laisse 45,2, et 242 Md€ portés deux
fois sous deux identifiants. Une pièce citée comme source de source doit être
cohérente ; ce fil ne la rend pas cohérente, il dit où elle ne l'est pas.

**L'état reçu est mesuré, non déclaré.** `referentiels/REF_chiffres.json`, hors
coffre, régénéré : **257 entrées, 93 sans source, `0 échec` au contrôle**, 57
calculs rejoués justes. Le manuscrit est prouvé de l'extérieur —
`extraire_notes.py` rejoué rend `referentiels/notes_manuscrit.json` **identique à
l'octet**.

**L'index n'est pas régénéré, et c'est délibéré**, pour le motif déjà inscrit le
20260921 : `appareil/generer_index.py` au clone est antérieur aux quarante-cinq
artefacts portés le 20260917. Les trois pièces nées de ce fil — le livrable et
les deux fragments — **sont dues à la table curée**, avec la dette déjà ouverte.

**Les deux cumulatifs sont assemblés, et la mesure a corrigé une croyance.** Le
fil de purge avait assemblé à 09:27 **sans les deux fragments de ce fil**, versés
à 09:18 : `journal.md` et `arbitrages.md` au coffre ne les portaient pas. Les
quinze fragments et les deux cumulatifs ont été restaurés — les fragments par
copie d'octets depuis le transcript, les deux cumulatifs par `cp` du fichier
rendu —, puis `fragments.py assembler` a été joué. **Tête identique à l'octet
avant et après** — 247 519 o au journal, 292 687 o au registre —, un seul ajout
par cible, idempotent à la seconde passe. Reversés.

*Ce qui a permis la mesure : neuf des quinze fragments ne sont pas à l'index, donc
`restaurer.py` ne sait pas les placer. Ils se relèvent par `moisson()` à leur
propre chemin, le chemin au coffre et le chemin au dépôt étant les mêmes. **La
dette de table curée coûte déjà un détour.***

**Les trois questions ouvertes le matin sont closes le soir.** 34, 35 et 36
tombent ensemble sous la règle de préséance énoncée par l'auteur, et elles sont
marquées tranchées à `methode/a_trancher.md`.

**Reste ouvert** : les 87 candidats instruits restent **sans source** — instruire
n'est pas sourcer. Les 125 Md€ du corps du livre ne sont entrés nulle part, et
tant qu'ils n'y sont pas la contradiction de `P-D-067` ne s'écrit pas. Le statut
technique du sous-jacent reste à l'auteur.
## 20260921 — reconfirmation-chiffres

**Les chiffres du manuscrit sont relevés un par un et confrontés au référentiel
des faits. Le fil relève, il ne corrige pas.** Livrable :
`livrables/reconfirmation_chiffres_20260921.md`.

**Le compte.** 311 chiffres relevés au manuscrit — `identique` 74, `divergent` 0,
`absent` 225, `ambigu` 12. 71 des 257 entrées du référentiel sont atteintes par
un chiffre du manuscrit. Les 93 entrées sans source : 2 retrouvées au manuscrit,
5 dérivées d'un chiffre du manuscrit, **86 d'origine inconnue**.

**La case `divergent` est vide côté manuscrit, et ce n'est pas une absence de
divergence.** Aucun chiffre du manuscrit n'a trouvé, à son propre ancrage, une
entrée portant le même fait sous une autre valeur. Les divergences se lisent dans
l'autre sens, et elles sont **onze** : une entrée adossée à une note de fin porte
une valeur qu'aucun chiffre de cette note ne porte — `N-e35-2`, `N-e38-1`,
`N-e71-1`, `N-e74-1`, `N-e79-2`, `N-e83-2`, `N-e99-2`, `N-e106-1`, `N-e106-2`,
`N-e135-1`, `N-e135-4`. **Toutes portent un millésime, un numéro de rapport, un
rang de classement ou un compte de pages** : c'est le relevé du référentiel qui a
pris une référence pour une grandeur. Le manuscrit fait foi ; rien n'est corrigé.

**Ce que la case `absent` mesure.** 225 chiffres sur 311 — 72 % — n'ont aucun
correspondant au référentiel. Ce n'est pas une anomalie : le référentiel agrège
les notes de fin porteuses d'un chiffre, les nœuds chiffrés de la doctrine et les
candidats du proto, jamais le corps du livre. **C'est la première mesure de cet
écart.**

**L'ancrage de la doctrine au manuscrit ne résout pas.** 56 entrées de provenance
`ref_doctrine` déclarent des codes de preuve en `M-nnnn`, qui renvoient à
`referentiels/releve_affecte.json` — introuvable, et déjà au bloc `manquants` de
l'index. Leur rattachement est invérifiable ; l'appariement s'est fait par la
valeur et le libellé seuls. Ce fil ne le rouvre pas.

**Le manuscrit est prouvé de l'extérieur.** `extraire_notes.py` rejoué sur
`manuscrit/manuscrit.html` restauré rend `referentiels/notes_manuscrit.json`
**identique à l'octet** — 141 notes, 37 portant un chiffre.
`referentiels/REF_chiffres.json` est hors coffre : régénéré par
`generer_ref_chiffres.py`, il rend exactement l'état du 20260917 — 257 entrées,
93 sans source, `0 échec` au contrôle, 57 calculs rejoués justes.

**Les notes de fin sont relevées à part, et le détecteur y laisse des grandeurs
dehors.** Le manuscrit porte 141 notes ; `extraire_notes.py` en déclare 37
porteuses d'un chiffre et `REF_chiffres` en représente exactement 37 — la
couverture du référentiel est celle du détecteur. **Le relevé de ce fil en trouve
51.** Sur les 14 notes d'écart, **six portent une grandeur** que le référentiel
n'a jamais vue — `e40` (140 kg), `e48` (101 dossiers, 15 et 13 ans), `e60`
(2 600 articles), `e61` (438 taxes, le même chiffre qu'au corps), `e103` (taux
multiplié par 10), `e114` (16 m² contre 25 m²). Les huit autres sont des renvois
— pagination, numéro de fiche, subdivision d'article, adresse web — et ce sont
les faux positifs du relevé de ce fil, déclarés comme tels. *`extraire_notes.py`
reste prouvé à l'octet : c'est son détecteur qui est en cause, pas sa copie.*

**Les neuf sources qui citent un onglet disparu sont relevées telles quelles,
aucune n'est réécrite.** Relevé repris de `livrables/ecart_classeurs_20260917.md`.

**L'index n'est pas régénéré, et c'est délibéré.** `appareil/generer_index.py` au
clone est antérieur aux quarante-cinq artefacts portés le 20260917 : un
`make reindex` d'ici les perdrait. Les trois pièces nées de ce fil — le livrable
et les deux fragments — **sont dues à la table curée**, avec la dette déjà
ouverte. Rien n'est généré.

**Reste ouvert** : les 86 entrées sans source d'origine inconnue, à instruire une
par une ; deux questions portées à `methode/a_trancher.md` (32 et 33). Les sept
vérifications du second cercle du socle restent perdues — ce fil ne les rejoue
pas.
## 20260923 — manifeste

Fil de révision du manifeste. Le texte servi à `france-resolution.fr/manifeste.html`
a été repris phrase par phrase avec l'auteur et arrêté — `livrables/manifeste_20260923.md`,
606 mots contre 627. Aucun fichier touché pendant le fil, rien poussé.

Dix corrections de fond, dont trois fermaient une attaque directe : les sept
missions du livre, réduites à trois en vitrine, sont rétablies en trois axes ;
le 6 % portait sur « ces missions » et chiffrait donc les trois axes, il nomme
désormais son périmètre, défense police justice ; la CSG et la CRDS cessent
d'être appelées cotisations sociales ; la retraite de base par répartition,
absente, est rétablie en principe ; le rendement des actifs publics entre dans
l'énumération des 236 milliards, qui n'en comptait que 218 ; les cotisations
chômage sont qualifiées de restitution et renvoyées en fin de liste.

**La passe 82,5 / 53,4 ne mord pas sur le manifeste** : ni 77,7 ni 39,5 n'y
figuraient, sous aucune forme, ni en dérivé. Relevé joué avant reprise.

**Une faute de méthode, et elle a coûté deux tours.** Le fil a mesuré les
chiffres du manifeste sur `livre/texte_livre.json` et conclu « non sourcé » pour
la division par dix et les 303 agences. `texte_livre.json` est le **corps** du
livre, 180 folios ; **les annexes n'y sont pas**, et les deux chiffres y vivent.
Le verdict juste était « absent d'EP3 », pas « absent du livre ». La règle est
portée en mémoire projet.

Mise en ligne et régénération du PDF dues au dépôt `Site-ETNP` — prompt écrit à
`methode/prompt_session_code_manifeste.md`, pour une session `claude.ai/code`.
## 20260923 — passe-825-534

**Mandat `A-413` : porter le manuscrit, les fiches et le site de 77,7 et 39,5 à
82,5 et 53,4, d'un coup. Mesuré : il n'y avait rien à porter.**

Le relevé est versé avant toute modification —
`livrables/releve_passe_825_534_20260923.md` — et **aucune pièce du corpus n'a
été touchée**.

**Ce qui a été balayé, et il ne manque rien.** Le clone du dépôt ; les
**164 documents du projet**, lus un par un et écrits à l'octet ; le manuscrit,
le livre, les deux protos ; et **les trois avals régénérés par la chaîne** —
`make` joué, site refait en 26 fichiers et 196 987 o, galerie refaite en
18 fiches, `REF_chiffres` refait en 257 entrées, compte identique à celui du fil
d'écart. `notes_manuscrit.json` et `REF_doctrine.json` régénérés sont
**identiques au clone à l'octet** : la chaîne jouée ici rend bien l'état que la
session suivante recevra.

**Le résultat.** 48 occurrences de 77,7 · 39,5 · 77,9 · 39,49 dans tout le
corpus, sur 14 fichiers. **Zéro sur les 57 fichiers d'aval.** Les 44 occurrences
du coffre sont dans la méthode, le registre, le constat antérieur et le prompt
du mandat lui-même ; les 4 de l'appareil sont dans `leviers_collocs.py`, où
`39,5` désigne le périmètre de dépense locale et non un total de tête. **Le
mandat excluait nommément tous ces endroits.**

**La prémisse était une déclaration, pas une mesure.** `A-413`, la question 30
de `a_trancher.md` et le fragment `20260921-purge-a-trancher.md` écrivent, dans
les mêmes termes, que « le manuscrit, les fiches et le site portent encore 77,7
et 39,5 ». C'est le quatrième mécanisme — *déclarer au lieu de mesurer* — et il
a frappé le mandat lui-même. Coût de la mesure : une chaîne rejouée et un
balayage.

**Ce que les avals portent, en revanche, et qui a bougé.** Le balayage des
26 valeurs que le fil d'écart déclare mouvantes rend 60 occurrences, dont
**51 homonymes écartés un par un** — les 2,8 millions de demandes de logement
social ne sont pas le résidu « autres » de 2,8 Md€, les 2,9 % du PIB de 1982 ne
sont pas le taux de rendement du patrimoine. Restent neuf occurrences vraies :
`D2-2-1-s3` France Travail **2,7** quand le classeur porte 5,254667, « autres »
**2,8** contre 2,745333, et l'entrée `R-D7-2-2-e2` de `REF_chiffres` qui écrit
encore **636,1 Md€ × 2,9 %** et « le classeur applique 2,9 % là où la doctrine
annonce 3 % », **quand l'arbitrage `A-421` du 20260921 a clos les deux écarts.**

**Les contrôles, et le troisième dit autre chose que ce qu'on croyait.**
Contrôle 1 vert, mais vert **avant** la passe. Contrôle 2 vert, écart nul à la
neuvième décimale, joué **directement sur le classeur** faute de socle
régénérable — et il oblige à corriger l'énoncé du mandat : le total général ne
se décompose pas en « 82,5 + 53,4 + le reste », les deux nomenclatures se
joignent à 135,954667 et non 135,9, **le pont valant exactement l'arrondi de la
ligne « autres »**. Contrôle 4 vert, 0 échec.

**Contrôle 3 : S17 n'est pas perdu.** `controle_socle.py` du clone le porte,
`epreuve_s17_salaire.py` est au dépôt. Ce qui manque est l'intrant : le socle ne
se régénère pas tant que `socle_0910.py` n'est pas poussé. **Le contrôle du
socle est donc amputé de ses dix-sept bouclages, pas d'un seul** ; et la pièce
réellement perdue est `epreuve_controle_socle.py`. Deux des trois lignes de S17
ont été rejouées à la pièce : **0,300000 exact** sur les départs d'État comme
sur les départs locaux.

**Une reprise de `controle_index` qui vaut d'être notée.** Le premier passage
rendait 79 anomalies bloquantes ; **39 étaient un artefact de l'atelier** — le
coffre restauré à ses adresses de coffre et non aux adresses canoniques. Après
restauration correcte, **40 anomalies réelles** : 34 fichiers au dépôt non
déclarés à l'index, dont **29 documents produits depuis le 20260917**, et 6 noms
horodatés hors archive. Le fil du second cercle en avait porté 45 d'un coup il y
a six jours ; **il s'en est réaccumulé 34 depuis.** Le stock a été traité, le
flux ne l'est pas.

<!-- fragments : tout ce qui suit est régénéré par appareil/fragments.py -->

## 20260930 — arbitrages-phase1

**Mandat.** Instruire et faire trancher par l'auteure les trois arbitrages qui ferment la
phase 1 — le critère des structures visées, le champ du mot « association », les secteurs
écartés de la suppression des niches. Fil au projet doctrine : aucune rédaction, aucun
amendement, aucune adresse. `disposition-cible`, `redaction-legistique` et `expose-sommaire`
n'ont pas été activées.

**Ce qui est rendu.** Les trois arbitrages sont tranchés, au fragment
`methode/fragments/arbitrages/20260930-arbitrages-phase1.md`. Une question fermée par
arbitrage, trois posées, trois répondues.

**Trois décisions, en une ligne chacune.** M-002 : la liste close, organisée par les
critères. M-016 : le tiers non public et non lucratif, quel que soit le payeur. M-026 :
différés et non exclus, transition progressive et restitution dans la fusion.

**Ce que le fil n'a pas écrit, et qui est dû.** Trois reprises, toutes hors de son mandat :

- la règle « pas de cas nommés » de `livrables/arborescence_mesures_20260928.md` est fausse
  telle qu'écrite — elle vaut pour la présentation, non pour le dispositif ;
- la borne de M-026 à la même arborescence — « liste des ~30 Md€ de secteurs écartés » —
  porte une exception de champ là où la décision est une exception de calendrier ;
- M-016 devient une mesure à deux jambes, PLF et PLFSS, par entrée du versant social au
  champ. La scission n'est pas portée par l'arborescence.

**Ce qui reste ouvert, et qui n'est pas de ce fil.** L'ordre des critères d'organisation de
la liste de M-002 — tambouille du fil qui l'établira. La durée de la progressivité de M-026,
et son écriture par secteur ou en bloc. Le montant du versant social de M-016, non ventilé
au millésime.

**Assemblage.** `appareil/fragments.py` n'est pas au clone : ce fil dépose, il n'assemble
pas. `journal.md` et `arbitrages.md` au coffre ne portent pas encore ces deux fragments.

## 20260930 — correction-forfaits-cotisation

## 20260930 — La ligne « forfaits de cotisation » est rattachée, et le résidu grandit

**Le seul trou du côté du schéma est fermé.** La ligne « dont forfaits de
cotisation », 8,8 Md€, reçoit les deux prélèvements de l'épargne salariale du
référentiel — forfait social 6 690,2 et contributions sur stock-options et
attributions gratuites 1 669,1, ensemble 8 359,3 M€ en 2026. Les 24 lignes
d'agrégat du schéma reçoivent désormais toutes au moins un prélèvement.

**Le rattachement traverse la frontière d'assiette, et c'est la seule affectation
de la table qui le fasse.** Le schéma lit ces prélèvements par leur fonction —
substituts de cotisation sur des rémunérations qui y échappent — quand le
référentiel les classe par leur assiette juridique, en contributions sociales sur
les revenus. La clé suit le schéma, parce que c'est lui qu'elle sert. Les 81
autres prélèvements des assiettes 1 et 2 restent hors périmètre.

**Les taux bougent peu, le résidu beaucoup.** Périmètre du schéma 320
prélèvements ; couverture 13,4 % après libellé, 87,2 % après ligne d'agrégat.
Mais le passage des bases verse 7,33 Md€ de masse 2024 du côté du recensement
sans rien ajouter du côté du schéma, où les 8,8 étaient déjà comptés : **l'écart
réel passe de 5,5 à 12,8 Md€**. Sur la ligne elle-même, le rapprochement
s'améliore — 11,2 d'écart avant, 3,9 après.

**Un signalement, non tranché.** La ventilation 2024 du recensement donne 7,33
aux deux prélèvements rattachés, quand forfait social plus contribution
solidarité autonomie feraient 8,77 — soit les 8,8 du schéma à l'arrondi près. La
coïncidence est relevée ; le mandat nomme l'épargne salariale, et c'est ce
rattachement qui est porté. Le sort de la contribution solidarité autonomie reste
entier.

**Les 41 non atteints sont requalifiés au relevé.** Ce n'est pas un défaut
d'appariement mais une catégorie sans réceptacle au schéma — la contrepartie
invoquée. Leur sort est un arbitrage de l'étape suivante ; trois voies sont
nommées, aucune n'est ouverte.

## 20260930 — inscription-registre

## 20260930 — inscription-registre

**Dix-huit artefacts entrent à l'index et à la carte. Le plan de rédaction en
sept phases et l'arborescence des mesures sont désormais des pièces du corpus,
et ils commandent l'aval du découpage doctrinal.**

**Ce qui est entré.** Les neuf pièces `cgi_expert_*` — cinq référentiels, trois
livrables de lecture, les règles d'emploi — plus
`livrables/predigestion_cgi_20260929.md` et le fragment
`methode/fragments/a_trancher/20260929-cgi-expert.md` ;
`livrables/mecanique_gages_restitutions_20260929.md` ;
`referentiels/prelevements_forces_20260930.tsv`,
`livrables/recensement_prelevements_20260930.md` et
`methode/prompt_fil_sort_prelevements.md` ;
`livrables/arborescence_mesures_20260928.md` et
`methode/plan_sept_phases_20260930.md` ; et le fragment de journal de ce fil.
L'index passe de 292 à 310 artefacts, 234 à 252 au coffre, 66 à 73 dérivés.
Aucun manquant résolu, aucun retiré.

**Le rattachement des pièces `cgi_expert_*` est double.** Au chantier 1, elles
sont la matière des lots `F` et `G` : la rédaction cible de l'auteur sur
2 376 articles du code général des impôts alimente la colonne C du trois colonnes
à l'étape E4. Au chantier 2, elles sont une quatrième population de test, la
seule qui atteigne cette échelle — mais elle ne se joue qu'après lecture de
`reference/cgi_expert_regles_de_lecture.md`, faute de quoi le banc mesurerait
l'écart de millésime et non la machine : le droit de départ est au 1er mai 2026,
254 articles ont bougé depuis, 74 commentaires ne sont pas tranchés.

---

### Le plan de rédaction en sept phases

Arrêté par l'auteure. Il corrige une version antérieure qui plaçait la
restitution avant la concentration et rattachait l'aide fondamentale et le taux
unique de l'IR à la restitution.

**Le principe.** Une phase est un noyau narratif qui tient seul devant le
rapporteur. Une phase abandonnée ne fait pas tomber les suivantes. Chacune se
dépose comme un bloc lisible. **La concentration précède la restitution** : sans
elle il n'y a rien à restituer, et la suppression des niches appartient à la
concentration — ce sont des subventions déguisées.

| phase | objet | ce qui la commande |
|---|---|---|
| **0 — matière** | mécanique des gages et des restitutions, tri des impositions, pré-digestion du CGI réécrit | rendue le 20260929-30, **sauf le sort des prélèvements** |
| **1 — concentration** | structures facultatives, effectifs, indemnisation des agents, subventions, aides aux entreprises, interdiction du chèque fléché, suppression des niches | rien — **seul parallélisme sûr du plan** |
| **2 — restitution** | suppression de la CSG et de la CRDS sur les revenus d'activité | chronométrée avec la bascule du statut, qui en tire sa contrepartie |
| **3 — fusion fiscale** | aide fondamentale, aide par enfant, taux unique de l'IR, demi-part de bascule, tri des 438, TVA, taxes spécifiques, IS en solde, droits de mutation, taxe foncière unique | s'écrit **contre l'état produit par la phase 1** — lien irréductible qui impose l'ordre |
| **4 — patrimoine et comptes** | cessions, fonds de défaisance, logements sociaux, compte d'épargne personnel | deuxième étage de la fusée |
| **5 — ouvertures** | chômage, retraite, soin : principe et cadre en loi, exécution renvoyée | peu de rédaction, beaucoup d'arbitrage politique |
| **6 — éducation** | scindée, traitée à part | périmètre non tranché |

**Quatre temps par mesure, dans chaque phase** : rédaction cible contre le droit
en vigueur ; disposition modificative dérivée, prouvée par réapplication ;
accroche et recevabilité évaluées au cas par cas, la recevabilité conjointe se
décidant là ; exposé et gage, servis par la matière de phase 0.

**Trois règles transversales, et elles mordent sur le corpus.** La base de
travail est **le droit en vigueur, jamais le PLF 2026** : le rattachement au
texte en discussion est fabriqué et se déclare comme tel, il ne se lit pas comme
un résultat de chaîne. La concurrence se traite par insertion de force quand le
texte en discussion modifie lui-même l'article visé — trois formes selon ce qu'il
fait, la rédaction cible ne changeant dans aucune des trois. La chaîne de gage
suit la chaîne du raisonnement, les contournements de procédure n'interviennent
qu'en bout, **un euro n'appartient qu'à un seul circuit**.

**Le lot `H` est supprimé, et c'est la propagation la plus lourde du plan.** La
passe à blanc n'existe plus : la valise est branchée dès la première passe,
quatre rôles ouverts, et la valeur du matériel se mesure sur le banc des liasses
déposées par un tiers, jamais sur nos propres mesures. Le contrôle sur les rôles
disponibles et non ouverts reste armé — un énoncé livré sans arguments sourcés,
sans principe ou sans paramètres sort à « à vérifier avant dépôt ». La carte des
chantiers est corrigée le jour même : le chemin critique va désormais du
découpage à la liasse sans répétition générale.

---

### Les décisions de relecture portées par l'arborescence

**49 relevées, 52 annoncées au mandat.** Le compte est mécanique : 49 blocs
« Décision de l'auteure » dans `livrables/arborescence_mesures_20260928.md`.
L'écart de trois n'est pas comblé par déduction et se porte à l'auteure. Second
écart de la même pièce : l'en-tête annonce 66 mesures, le corps en porte 65.

La pièce rend par ailleurs sept mouvements plus un transversal, 17 blocs,
157 composantes juridiques typées et 26 bornes. Les types de composante sont
`EXISTENCE`, `RECETTE`, `AFFECTATION`, `COMPÉTENCE`, `PRESTATION`, `TRANSITION`,
`GAGE`, `RENVOI`, `CADRE`.

**Ce que les décisions fixent, et qui n'était écrit nulle part ailleurs.**

*Sur la structure de l'État.* Le dispositif d'indemnisation des agents est une
économie et non un coût, et sans lui M-007 ne vole pas — c'est le nœud identifié.
La bascule du statut appelle une contrepartie, et le plan de départ obligatoire
n'en est pas une. La réinternalisation du régalien est confirmée comme transfert
à l'État, non comme exemple.

*Sur la fiscalité.* La suppression des taxes affectées se rattache à la fusion
fiscale, pas à la fermeture des structures : ce qui compte ici est la suppression
de l'affectation. Le résultat du tri n'est pas exactement quatre impôts, mais
quatre grands plus des petits tactiques harmonisés et rattachés aux grands. La
sortie des taux réduits de TVA est progressive sur trois ans et porte surtout sur
l'alimentation — **c'est pourquoi elle ne gage pas la restitution salariale**.
L'IS fait le solde : cadre et principes en loi, trajectoire renvoyée au règlement
sur critères clairs. La taxe foncière unique se fixe par un taux communal dans une
fourchette parlementaire, sur une valeur locative actualisée au plus tous les cinq
ans par l'INSEE, avec plafond soutenable comme justification devant le Conseil
constitutionnel.

*Sur le social.* On entre par l'aide fondamentale, le reste est le solde ; chaque
jambe est automatique et autonome, soldant en macro et au niveau de la personne.
La demi-part de bascule va avec l'aide fondamentale et la fusion de l'IR, parce
qu'elle compense la hausse de taux sur les petites retraites. L'âge légal ne se
supprime pas pendant la transition. Le reste à charge s'ouvre par un principe
positif — soutenable, uniforme, sans exception, avec plafond —, l'ajustement
renvoyé au règlement et la surveillance à un comité refondu d'experts et de
parlementaires.

*Sur le patrimoine.* Les fonds de défaisance ont mission claire — valoriser au
mieux puis fermer, sur le modèle de la résolution bancaire —, découpés à une
taille absorbable par thème ou par région. Le parc social entre de force dans le
régime des actifs publics à céder : c'est le principal sujet juridico-financier
du bloc, le flux s'éteint immédiatement et la SRU est supprimée.

*Sur la conduite de l'exposé.* Ne pas parler des pensions dans l'exposé des
niches sociales. Ne pas présenter la dépense de soin par les soins de confort,
mais par des critères positifs — service médical rendu, criticité. Tout geler par
défaut sur les indexations : revaloriser doit être un acte politique responsable.

**Trois règles de forme, qui valent pour toute la série.** Un amendement porte
une unité de sens politique, et la procédure n'impose de scinder que sur deux
frontières — loi de finances contre loi de financement, et recettes contre
dépenses. **Pas de cas nommés** : une mesure qui nomme un bénéficiaire crée un
plaignant ; cinq cas sont sortis et redescendus en matière d'exposé, deux restent
ouverts. Le typage des composantes est une lecture déclarée de l'auteur, **il ne
vaut pas balayage** : l'étape qui cherche le siège juridique refait le sien
intégralement sans le lire, puis compare, et tout écart se déclare.

---

**Ce qui reste ouvert, et la pièce le dit elle-même.** Le sort des
420 prélèvements recensés, qui est le plus gros poste de travail restant et ne
bloque que la phase 3. Le format du compte d'épargne personnel, qui commande
B-10, B-11, B-12 et le compte santé. La contrepartie de la bascule du statut. Ce
qui est atteignable en texte financier — M-010, M-059, B-16 en entier, M-022 par
voie indirecte. La contrainte formelle sur les droits de mutation. L'emploi du
gage sur M-026 et M-030. Le périmètre du mouvement 7. Les deux mesures orphelines
de ressource : B-07 à 114,46 Md€, B-05 à −20,5 Md€ de solde.

**Ce qui n'est pas inscrit, et volontairement.** Le rendu visuel de
l'arborescence est un artefact publié, hors projet : il ne figure ni à l'index ni
à la carte, et n'est porté qu'en alias de la pièce markdown.

**Ce qui est dû.** L'index a été écrit au coffre ; sa table curée vit dans
`appareil/generer_index.py`, au dépôt, où l'écriture depuis Cowork reste fermée
(A-393) — les dix-huit entrées sont donc à repousser d'une session
claude.ai/code. `methode/empreintes.json` n'a pas été touché : le relevé
d'empreintes est mécanique et se prend à `make coffre`, qu'un fil Cowork ne joue
pas. Les dix-huit artefacts y sont dus.

**Relevé au passage, non corrigé.** Le rôle `etat_machine` désigne deux
artefacts à l'index — `appareil/etat_machine.py` et `livrables/etat_machine.html` :
un renvoi vers ce rôle résout de façon ambiguë. Le défaut est antérieur à ce fil
et se répare au générateur de l'index, au dépôt.

## 20260930 — perimetre-fiscal

## 20260930 — traduction-perimetre-fiscal

**L'arbitrage de périmètre fiscal de l'auteure est versé et propagé. Aucun fond
produit, aucune pièce neuve hors le fragment reçu.**

**Ce qui est versé.**
`methode/fragments/arbitrages/20260930-perimetre-fiscal.md`, copie d'octets du
versement de l'auteure. Il tranche quatre points : les prélèvements sociaux sur
le capital — prélèvements de solidarité, 15,6 Md€, et prélèvements sur les
revenus du patrimoine et des placements — prennent le sort **non touché** et ne
comptent ni au gage ni à la restitution ; la fusion de la flat tax dans l'impôt
sur le revenu par la rédaction de l'expert est une opération de rédaction sans
portée doctrinale ; les **33 prélèvements à contrepartie invoquée** restés sans
sort s'auditent une par une, par défaut supprimer et fondre, repli jamais pris
par commodité, le principe primant le montant sous le milliard ; et la phase 1 se
lance sur un petit nombre de mesures d'abord.

**Ce qui est propagé, le jour même.**

`methode/prompt_fil_sort_prelevements.md` — remis à jour. Il était antérieur aux
deux fragments d'arbitrage du 20260930 et ne les portait pas. Il porte désormais
son **lot 0** — la correction de la table de passage sur la ligne « dont forfaits
de cotisation » —, les quatre défauts de réconciliation D-1 à D-4, le périmètre
fiscal arrêté, et ce que le fil ne fait pas : aucune adresse, aucune skill de
rédaction. Sa ligne de lancement est reprise en conséquence. **Le fil
d'attribution n'attend plus aucun arbitrage.**

`methode/socle_prompt_fil.md` — la **frontière de projet** y entre comme règle
opposable, avant la liste de ce que tout fil respecte : doctrine d'un côté,
machine valise branchée de l'autre, et une ligne de lancement du projet doctrine
qui n'active jamais `disposition-cible`, `redaction-legistique` ni
`expose-sommaire`. Elle a été enfreinte deux fois le 20260930, dans les deux cas
par une ligne de lancement de phase 1. Elle est inscrite là où les lignes de
lancement s'écrivent, donc là où elle se vérifie.

`methode/carte_des_chantiers.md` — trois inscriptions. Le **relevé de siège**
entre au chantier 1 : 105 prélèvements sans siège renseigné, dû avant la phase 3,
sur ceux qui reçoivent un sort autre que « non touché » ou « hors mandat » — son
périmètre exact n'est connu qu'à la sortie du fil d'attribution. Il n'était
inscrit à aucun plan. La **frontière de projet** entre à « ce qui traverse tout ».
Les **trois arbitrages qui bloquent la phase 1** — critère des structures visées,
champ du mot « association », secteurs écartés de la suppression des niches —
entrent à « ce qui revient à l'auteur ».

**Ce qui reste ouvert, et ce fil ne le touche pas.**

- Les **trois arbitrages de phase 1** ne sont pas rendus. La phase 1 ne s'ouvre
  pas sans eux.
- L'**assemblage des fragments** n'est pas joué : `appareil/fragments.py` n'est
  pas au clone, et ce fil est un fil de conversation — il n'a rien déplié, rien
  cloné, joué aucun `make`. `journal.md` et `arbitrages.md` au coffre ne portent
  donc pas encore ce fragment ni ceux du 20260930.
- Le **rattrapage du générateur de l'index** reste dû — 253 artefacts rendus
  contre 311 au corpus à la dernière mesure, et ce fil y ajoute deux fragments
  sans avoir rejoué le compte. Aucun `make reindex` avant le rattrapage.
- Les **empreintes** des artefacts du 20260930 restent à relever, dans la même
  session que ce rattrapage.

**Ce que ce fil n'a pas fait, et volontairement.** Aucun contrôle joué, aucune
mesure, aucun livrable neuf, aucun paquet de dépôt : le mandat n'en nomme pas.
Les comptes repris ici — 105 prélèvements sans siège, 33 redevances, 129 au
solde, 83 cotisations, 253 contre 311 — sont ceux des pièces citées, non des
mesures de ce fil.

## 20260930 — sort-prelevements

Fil Cowork « sort des prélèvements ». Lot 0 corrigé, sort attribué aux 420
prélèvements, bouclage écrit en quatre lignes de solde.

**Mesure d'ouverture.** La table de passage reprise se retrouve à l'octet sur
trois grandeurs indépendantes — 420 prélèvements, 420 libellés distincts, 188
sans montant publié, 876,749 Md€ de rendement connu — et le total des taxes à
supprimer du schéma se recompose à −137,05 Md€ depuis ses vingt-trois lignes.

**Lot 0.** Défaut D-4 appliqué : deux lignes changent, et deux seulement. La
contribution solidarité autonomie, 2 563,2 M€, entre à « dont forfaits de
cotisation » ; les contributions sur les attributions d'options et d'actions
gratuites, 1 669,1 M€, en sortent. Les quatre compteurs d'étape sont inchangés,
la correction étant un échange. La concordance de la ligne servie passe de 1,47
à 0,03 Md€ d'écart : 8,8 Md€ au schéma contre 6,30 + 2,47 = 8,77 au recensement.
**Le fichier du coffre n'a pas été réécrit** — voir le fragment d'arbitrages.

**Attribution.** 420 prélèvements, aucun sans sort, un seul `en attente`.
4 conservés, 50 fondus, 193 supprimés, 50 maintenus à part, 25 sortis du
périmètre des prélèvements obligatoires, 11 non touchés, 83 hors mandat,
3 hors champ. Aucun prélèvement ne se fond dans la TVA, et c'est un résultat
mesuré, non un trou : les taxes spécifiques que le schéma supprime ne
transfèrent pas leur assiette, qui est déjà dans le champ de la TVA.

**Audit des 41 à contrepartie invoquée, ligne à ligne.** 16 supprimés et fondus
pour 1,869 Md€, 25 sortis du périmètre pour 0,470 Md€. Quatre points saillants
remontés : contribution de sécurité immobilière 814,6 M€ supprimée, assiette ad
valorem et non coût de service ; rémunération au comité professionnel des stocks
stratégiques pétroliers 591,0 M€ supprimée, bien public ; frais de contrôle ACPR
et AMF 386,5 M€ supprimés, police administrative ; redevances domaniales et de
spectre 258,8 M€ sorties du périmètre, l'occupation privative du domaine public
se loue.

**Bouclage.** Quatre lignes de solde. Des 1 250,76 Md€ de prélèvements
obligatoires 2024 aux 624,9 du schéma, par un résidu de 625,86 rendu par
différence et déclaré comme tel. Des 876,749 Md€ recensés en base 2026 aux
689,776 du périmètre du schéma, puis aux 687,438 atteints par la clé. Des 689,776
en base 2026 aux 639,17 de masse réelle 2024, soit 50,61 Md€ d'écart de millésime
et de convention, non séparables. Et un résidu réel de +14,27 Md€ entre le
périmètre de recensement et le périmètre de doctrine, que le lot 0 a élargi de
12,8 à 14,27 en rendant visible une matière déjà portée.

**Un écart de source relevé et non arbitré :** le mandat porte 1 250,76 Md€ de
prélèvements obligatoires 2024, le classeur en porte 1 251,8 en `F3`. Écart
1,04 Md€.

**Contrôles.** Treize contrôles joués sur l'onglet produit et non sur les
chiffres du relevé, tous verts. Jeu de fautes de six cas, six levées. Jeu de
justes de quatre cas, quatre passés — dont les 4 prélèvements chiffrés à zéro,
qui ne se confondent pas avec un montant absent, et les 10 libellés portant des
guillemets internes, intacts après écriture.

**Pièces versées.** `livrables/sort_prelevements_20260930.md` et
`referentiels/sort_prelevements_20260930.tsv`. Le classeur
`reforme_prelevements_20260930.xlsx`, onglets `Réforme`, `Synthèse` et `Lot 0`,
autoportant et exportable, ne peut pas être versé — le projet ne stocke pas de
binaire — et est remis à l'auteure.

**Aucune adresse n'a été écrite.** `disposition-cible`, `redaction-legistique` et
`expose-sommaire` n'ont pas été activées.

## 20260930 — table-de-passage

## 20260930 — La clé du schéma aux prélèvements, et son taux

**La table de passage est construite et sa couverture est mesurée.** 420
prélèvements, 24 lignes d'agrégat du schéma sous-lignes comprises, une affectation
par prélèvement et zéro double affectation. Sur les 318 prélèvements du périmètre
du schéma, l'appariement par libellé en attrape 12,9 %, l'appariement par ligne
d'agrégat porte le cumul à 87,1 %. Les 41 restants sont nommés un par un.

**L'écart des bases se range en trois causes, et pas une de plus.** Le périmètre
d'abord, à millésime constant : 876,7 moins les cotisations sociales, les
contributions sociales et le hors champ — 196,2 Md€, 102 prélèvements — puis moins
les 41 sans réceptacle — 2,3 —, égale 678,2. Le millésime ensuite, à périmètre
constant : 680,5 en 2026 brut contre 630,4 en 2024 net, soit 50,1 d'exercice et de
convention, que les pièces ne permettent pas de séparer. Reste 5,5 Md€ d'écart
réel entre le périmètre de doctrine et le périmètre de recensement.

**Deux trous sont constatés et non comblés.** La ligne « dont forfaits de
cotisation, 8,8 Md€ » du schéma ne reçoit aucun prélèvement : aucun libellé du
référentiel ne porte ce terme. Et les 41 redevances, rémunérations et frais de
contrôle de l'assiette 7 n'ont aucune ligne au schéma — absence de réceptacle, non
défaut d'appariement.

**Le solde à compenser concorde.** −67,75 au schéma, +67,75 en hausses
d'équilibre, mêmes grandeurs qu'au circuit B de la mécanique des gages. Constaté,
non recalculé, aucun écart.

**Reste ouvert.** Le partage des 50,1 Md€ entre exercice et convention exigerait
une ventilation par assiette des remboursements et des crédits d'impôt, qu'aucune
pièce ne porte. Le solde des 5,5 Md€ exigerait une masse réelle 2024 au
prélèvement, qui n'existe pas davantage. Le sort des prélèvements n'est pas
attribué : ce fil construit la clé, il ne décide de rien.

## 20260930 — versement-reprise

## 20260930 — versement-reprise

**Les deux pièces du 20260928-30 sont reversées en-têtes corrigés, et les deux
opérations d'appareil du mandat sont mesurées bloquées.**

**Ce qui est versé.** `livrables/arborescence_mesures_20260928.md` et
`methode/plan_sept_phases_20260930.md`, en remplacement des versions du matin.
L'arborescence porte désormais son compte juste : **66 mesures sur 65 lignes**,
M-067 et M-068 — deux directions sans dispositif — partageant une ligne ; et
**49 décisions de relecture, dont 45 sur une mesure et 4 sur la portée d'un bloc
ou d'un mouvement**. Les deux écarts que le fil d'inscription avait portés à
l'auteure sont clos : ils étaient d'en-tête, non de fond. Le plan déclare
explicitement la suppression du lot `H`.

La carte reprend ces comptes. L'index ne bouge pas : ses deux entrées portent le
rôle, le chemin, la voie et la famille, aucun chiffre d'en-tête.

---

### Le générateur de l'index a décroché — 253 contre 310

`appareil/generer_index.py`, joué au clone du dépôt, rend **253 artefacts dont
195 au coffre**. Le coffre porte **310 artefacts, 252 au coffre**. L'écart est de
cinquante-sept : les **dix-huit** entrées du 20260930, et **trente-neuf**
déclarations antérieures que la table curée du générateur n'a jamais reçues.

**Conséquence, et c'est elle qui compte.** Un `make index` joué en l'état ne
perdrait pas les dix-huit entrées de ce fil : il en perdrait cinquante-sept. La
table curée se rattrape **avant** tout rejeu de l'index, et le rattrapage porte
sur les trente-neuf autant que sur les dix-huit. Rien n'a été poussé.

**La poussée est refusée, et la mesure nomme son motif.** Le mandataire git rend
un `403` : le dépôt `resolution-ib-dev/Resolution-2027` n'est pas dans l'ensemble
des dépôts autorisés de la session, donc aucune identité n'est injectée. Le clone
en lecture passe. C'est la fermeture d'A-393 constatée mécaniquement, et elle se
lève en déclarant le dépôt aux sources de la session — non depuis ce fil.

### Les empreintes ne sont pas prises

`make coffre` relève l'empreinte de chaque artefact du coffre **au dépôt
courant**, c'est-à-dire aux fichiers que le fil porte. Ce fil ne porte que les
deux pièces reversées : relever sur cet état écrirait deux empreintes et
laisserait les seize autres artefacts du 20260930 sans référence, sans que rien
ne le dise. Le relevé est cumulatif, donc rien ne serait détruit — mais une
empreinte partielle passée pour un relevé complet est exactement ce que le
module interdit. Les dix-huit empreintes restent dues, et elles se prennent dans
la même session que le rattrapage du générateur, sur un coffre déplié.

**Ce que ce fil n'a pas fait, et volontairement.** Aucun contrôle joué, aucune
pièce neuve, aucun paquet de dépôt écrit : le mandat n'en nomme pas.

## 20261001 — courroies

## 20261001 — courroies

**Consigne de l'auteure : la tenue des courroies est le travail de Claude, en
gestion active. Inscrite, et outillée d'un fil.**

**Inscrit au socle des prompts de fil.** La tenue des courroies — versement,
assemblage des registres, index, mémoire, propagation d'une règle le jour même —
se fait d'office, sans go et sans compte rendu au-delà d'une ligne. Ne remontent
à l'auteure que les arbitrages de fond et les actes qu'elle seule peut poser
matériellement. Une demande de poussée de code se fait armée : paquet unique,
autonome, verbatim, ordre d'application et points d'arrêt. Ajouté aussi à ce que
tout fil rend : **une reprise déclarée hors mandat se porte à l'endroit où le fil
suivant la lira**, sans quoi elle est perdue — trois reprises ont été déclarées le
20260930 dans ce cas.

**Écrit.** `methode/prompt_fil_courroies.md`, fil Cowork qui mesure les trois
courroies — fragments non assemblés, table curée de l'index, modules dus — et rend
**un paquet de dépôt unique et autonome** pour une seule session `claude.ai/code`.

**Une faute évitée, et elle méritait de l'être.** Un prompt de fil `claude.ai/code`
avait été rédigé d'abord, qui renvoyait la session de code à des chemins du
coffre — `carte_des_chantiers.md`, `a_trancher.md`, les paquets — que cette
session ne peut pas lire, et qui reprenait des comptes hérités au lieu de les
faire mesurer. C'est la faute mesurée le 20260924, celle qui avait produit un fil
de nuit dont six lots sur huit étaient sans objet. Le prompt a été supprimé avant
versement et remplacé par le fil Cowork ci-dessus : **Cowork mesure et écrit le
paquet, la session de code applique et pousse.**

**Rappel de frontière, demandé et rendu.** L'analyse d'un nouveau texte financier
est au projet doctrine, chantier 3 — solde, portes ouvertes, mouvements sur nos
objets, écart à nos positions. Le projet machine ne reçoit que le rattachement de
nos mesures au texte déposé, et ce rattachement est fabriqué et déclaré comme tel.

---

**Le fil a tourné. Mesure du 20261001, 13 h 05 UTC+2, clone `main` à `4e6e1a4`.**

**La question préalable est fermée, et par la mesure.** Un fragment déposé depuis
Cowork n'est **pas** au clone que la session de code lit : le dépôt ne porte que
`chantier/Makefile`, `chantier/.gitignore`, `chantier/appareil/` — 92 modules —,
`chantier/referentiels/` — 5 JSON —, et à sa racine `data/`, `codes.json`,
`droit.py`, `essai.py`, `extraire_legi.py`, `README.md`. Ni `methode/`, ni
`livrables/`, ni `reference/`, ni `methode/fragments/`. Le paquet porte donc son
contenu verbatim.

**Courroie 1 — fragments.** 20 déposés au coffre, 2 assemblés
(`20260930-inscription-registre` et `20260930-versement-reprise`, tous deux au
journal), **18 en attente** : 7 au journal, 9 aux arbitrages, 2 à `a_trancher`.
*Le compte de 15 déposés et 13 en attente n'a pas été repris.* **Et l'assemblage
n'attend plus de session de code** : `appareil/fragments.py` est au clone depuis
le 20260930, donc un fil Cowork qui clone le dépôt peut assembler et reverser.
La limite inscrite le 20260917 — « un fil qui ne l'a pas ne peut que déposer » —
est levée.

**Courroie 2 — table curée.** Premier delta, générateur du clone contre
`methode/index.json` : **nul**, 315 des deux côtés, mêmes huit comptes. Second
delta, index contre documents réels : **47 documents déclarés nulle part**, et
**52 déclarations de voie `coffre` dont le document n'existe plus**. Les 47 sont
écrits verbatim au paquet, prêts à coller, avec les 47 familles jumelles pour
`generer_carte.py`. Comptes attendus : 315 → 362 artefacts, 313 → 360 classés,
`sans famille` inchangé à 2.

**Courroie 3 — modules dus.** Les 99 chemins que l'index déclare au dépôt y sont
tous : **dette nulle**. Reste deux trous de déclaration — `appareil/index_mesures.py`
et `appareil/socle_0910.py`, nommés dus par le registre, ni au dépôt ni aux
manquants de l'index — et la correction d'`A-421` à `appareil/sources_chiffres.py`,
qui n'est pas appliquée : le module porte encore `636,1 Md€ × 2,9 %`. C'est la
question 38 d'`a_trancher`, et elle reste ouverte.

**Rendu.** `methode/paquet_depot_courroies_20261001.md` — un seul paquet, une
seule opération, poussée d'essai à vide en premier geste, point d'arrêt à chaque
étape, comptes avant et après. Ses blocs verbatim ont été réextraits de son propre
texte et rejoués sur une copie neuve du clone : les deux générateurs rendent les
nombres annoncés. Aucune poussée, aucun fond, aucun livrable neuf.

## 20261001 — lecture-2027

## 20261001 — lecture-2027

**Le millésime 2027 est annoncé. Le prompt de lecture est écrit et versé ; les
annexes ne sont pas parues.**

**Ce qui est versé.** `methode/prompt_fil_lecture_textes_2027.md`. Quatre blocs
inchangés — solde, portes ouvertes, mouvements sur nos objets, écart à nos
positions —, six lots, chacun ouvrant sur sa mesure de présence et se sautant
proprement si sa pièce manque. **Les lots qui dépendent des annexes partent
suspendus et se rejouent seuls à leur arrivée** : une rubrique sans pièce sort
*suspendue*, nommée, avec ce qui la rouvrira, jamais vide et jamais à zéro. Les
deux véhicules suffisent à jouer L1, L2 et L4 dès le dépôt.

**Ce que le prompt porte, et qui vient de fautes mesurées.** Le gabarit 2026 se
modifie et ne se reconstruit pas — le fil 2026 l'avait reconstruit trois fois.
Les deux PDF se joignent, les deux : le fil 2026 n'avait pas celui du PLF.
Un agrégat se rejoue avec sa recette déclarée avant, jamais écrite en cours. Le
séparateur de milliers, la géométrie de colonne instable, les tableaux du PLFSS
logés dans les alinéas, le repère obligatoire sur chaque valeur, le format
réinscrit en tête de chaque passe.

**Le point sensible du millésime, énoncé par l'auteure.** Le texte 2027 travaille
sur le droit en vigueur, **aux entrées en vigueur différées déjà votées près**.
Le droit applicable au 1er janvier 2027 n'est donc pas partout le droit en
vigueur au dépôt : ces sièges se relèvent à part et toute confrontation qui les
touche porte la mention du décalage. C'est un relevé obligatoire du fil, au même
titre que les montées en charge.

**Les deux bornes reconduites.** Tout verdict côté loi de financement plafonne à
`plaidable` tant que la grille des portes du domaine n'est pas relevée — le fil
ne forge pas plus fort et ne relève pas la grille au passage. Le rattachement au
texte déposé reste fabriqué et se déclare comme tel ; la base de travail est le
droit en vigueur.

**Lot 7 ajouté après relecture de l'auteure, et il manquait.** Le prompt ne
rendait que la matière analytique : ni l'index des mesures, ni les fiches
lisibles par les participants. Les deux existent au corpus comme gabarit ou comme
dû — `livrables/index_mesures_plf.md`, 410 mesures sur 82 articles pour 2026, et
`methode/procedure_contre_plf.md` qui déclare la fiche courte par mesure
principale **à industrialiser pour l'analyse du PLF 2027**. Le lot 7 les porte,
pour les deux véhicules, avec les relevés de mots de portée et d'absences
attendues. **Critère de « mesure principale » tranché par défaut et révocable** :
montant propre dans un état, une annexe ou un tableau d'équilibre ; ou objet de
L3 touché ; ou article parmi les plus chargés en adresses ouvertes.

**Porté à la carte des chantiers** : le millésime 2027 au chantier 3, les pièces
à joindre, et la ligne de date.

## 20261001 — lecture-plf2027

**Le PLF 2027 est lu. L'index des mesures et les fiches de mesure principale sont
versés. Le PLFSS n'est pas dans le champ de ce fil : il est déclaré traité
ailleurs, non suspendu.**

**Mesure d'entrée, jouée avant toute lecture.** PDF du PLF 2027, enregistré à la
présidence de l'Assemblée nationale le 1er octobre 2026, n° XXXX. sha256
`b0b802d3cafb313435e9afa16b2760f367a614a758a3f717bcbd58b94944cb54`. **407 pages.
90 en-têtes d'article relevés** — article liminaire plus articles 1 à 89. Le
relevé n'est parti d'aucune liste : il part de la mesure des en-têtes du corps,
pas du sommaire.

**Le repère de page est le folio imprimé, et il a fallu le mesurer.** Le folio a
été extrait des 391 pages qui en portent un et confronté à l'index de page du
PDF : **écart constant de 0**. En revanche **le sommaire du texte déposé est
désynchronisé du folio** — l'écart apparaît à l'article 8 (+2) et croît jusqu'à
**+21** à l'article 89 ; le sommaire annonce l'état A à la page 296 quand il
commence au folio 274. Les pages de l'index et des fiches sont les folios, jamais
les renvois du sommaire. *Une valeur sans repère ne s'écrit pas : le repère
lui-même se mesure.*

**Index des mesures — `livrables/index_mesures_plf2027.md`.** **475 mesures sur
90 articles**, une ligne par mesure, dans l'ordre du texte, au gabarit de
`livrables/index_mesures_plf.md`. Repère de volume 2026 : 410 sur 82. Chaque
ligne porte sa référence, sa subdivision, sa page et ses sièges de droit.
**120 lignes sortent sans siège**, et c'est un état et non un vide : sous-mesure
dont le siège est nommé au bloc parent, ou disposition sans siège — crédits,
plafonds, garanties, entrée en vigueur.

**Fiches — `livrables/fiches_mesures_plf2027.md`.** **54 articles retenus sur
90**, par les trois critères du prompt appliqués mécaniquement. Les 36 non
retenus sont listés en fin de pièce, avec quatre cas signalés d'office : la
sélection est un relevé, elle se conteste, et la contester ne fait pas rejouer
l'index.

**La règle de chiffre a tenu, et elle coûte.** Le chiffre se prend au dispositif,
à un état législatif annexé ou au tableau d'équilibre, jamais à l'exposé des
motifs. **Les exposés des motifs du PLF 2027 ne portent aucun tableau de
chiffrage par mesure.** Conséquence mesurée : pour la quasi-totalité des mesures
fiscales, la valeur sort `introuvable au véhicule` avec son motif — le texte
déposé ne porte pas ces montants, et ce sont les annexes non parues qui les
rouvriront. Les chiffres rendus sont ceux du tableau d'équilibre (solde général
**-156 394 M€**), des états B à E, des articles d'évaluation (PSR collectivités
**43 096 363 228 €**, PSR-UE **30 905 520 986 €**), des plafonds d'emplois
(**2 032 750** ETPT État, **397 282** opérateurs, **3 140** EAF, **1 810** API)
et de deux lignes de l'état A relevées par confrontation de libellé
(**5 200 000 000 €** sur la contribution exceptionnelle IS, **916 126 398 €** sur
l'écrêtement de la taxe sur les gestionnaires d'infrastructures).

**Écarts relevés, non arbitrés.** Plafond d'emplois des opérateurs : le texte fixe
397 282 ETPT, l'exposé annonce **-4 107** sur la LFI 2026 quand l'écart au PLF
2026 déposé — 401 310 — est de **-4 028** ; la LFI 2026 n'est pas au véhicule, le
rapprochement ne se fait pas ici. CPEB : l'exposé annonce **2,5 Md€** de rendement
quand **aucun montant n'est au dispositif** et qu'aucune ligne d'état A n'a été
trouvée sous ce libellé. Article 60 : les crédits de paiement des comptes de
concours financiers excèdent les autorisations d'engagement de **301 684 616 €**.
Article 44 : le plafond du tarif de l'aviation civile est fixé **au niveau exact
du rendement prévisionnel**, quand l'exposé le présente comme un plafonnement au
niveau des dépenses du budget annexe. Article 25 : l'exposé annonce « trois
aménagements ponctuels » là où l'article porte **17 mesures** sur huit sièges.

**Deux relevés obligatoires rendus, et tenus courts.** Mots de portée : « peut »,
« par dérogation » et « notamment » sont les trois discriminants, nommés article
par article ; « à compter de » et « au titre de » sont généraux et ne signalent
rien. Absences attendues : quatre familles instanciées — plafond posé sans
indexation, taux modifié sans mouvement d'assiette, suppression sans transitoire,
dispositif créé ou prorogé sans évaluation.

**Montées en charge et entrées en vigueur différées.** Rendues en relevé séparé.
**Cinq articles portent un effet rétroactif** à un exercice clos ou en cours
(13, 14, 20, 28, 32), **quatre un effet partiel sur 2027 et plein à partir de
2028** (72 au 1er juillet, 78 au 1er septembre, 79 au 1er décembre, 82 en deux
temps), **cinq un effet reporté hors de l'exercice** (19, 24, 42, 46, 89), et
**six renvoient la date réelle au pouvoir réglementaire** (9, 24, 42, 82, 88, 89).
*L'article 79 est le cas d'école : une entrée en vigueur au 1er décembre 2027
affiche un douzième du coût en régime.*

**Réserve non levée, et elle est due.** Les sièges touchés par une entrée en
vigueur différée **déjà votée** n'ont pas été relevés à part : les relever suppose
une lecture du droit en vigueur que le mandat de ce fil ne porte pas. La reprise
est portée à `methode/fragments/a_trancher/20261001-lecture-plf2027.md`, pour le
§ B de `methode/a_trancher.md`, avec deux autres questions ouvertes par ce fil.

**Appareil.** `appareil/index_mesures.py` n'est pas au clone — il n'y a pas de
clone à l'atelier de ce fil. **L'index a été relevé sans lui**, par une grammaire
écrite ici : découpage par en-tête d'article, séparation dispositif / exposé,
descente à deux niveaux de subdivision, blanchiment des passages entre guillemets
avant toute détection de siège, garde d'ordre sur les marqueurs et garde de rang 1
sur le sous-découpage. **Les gardes viennent chacune d'une divergence mesurée** et
sont inscrites au fragment d'arbitrages, avec le nombre qui les a imposées. La
sortie versée fait spécification pour le module dû.
`appareil/confronter_lecture.py` n'est pas davantage au clone : **la confrontation
mécanique de la table de repères n'a pas été jouée**, et le fil le dit plutôt que
de la remplacer par un contrôle tiré de ce qu'il a produit.

**Pièce due, et où elle est portée.** `appareil/index_mesures.py` est déjà nommé
par `methode/paquet_depot_courroies_20261001.md`, section « ce qui reste après »,
comme trou de déclaration — ni au dépôt, ni aux manquants de l'index. **Ce fil ne
constitue pas un second paquet et ne réécrit pas celui des courroies** : il verse
sa spécification sous forme de sortie et de grammaire inscrite, et laisse le
paquet en l'état.

**Fragments déposés, non assemblés** — il n'y a pas de clone à l'atelier, donc pas
de `appareil/fragments.py`. **Les trois fragments de ce fil sont postérieurs à la
mesure du paquet des courroies (20261001, 13 h 05) et n'y sont donc pas
déclarés** : `20261001-lecture-plf2027.md` au journal, aux arbitrages et à
`a_trancher`. Le fil qui reprendra la table curée les porte avec les autres. *Dit
ici parce que c'est l'endroit où le fil suivant le lira.*

**Ce qui n'a pas été ouvert, et c'est le mandat qui le veut.** L1, L2, L4 puis L3
ne sont pas joués : le premier rendu est clos et versable à lui seul, et il l'est.
Le fil rend son état et s'arrête ; il ne se donne pas son successeur.

## 20261001 — lecture-plfss-2027

**Mandat.** Lire le PLFSS 2027 déposé. Premier rendu, seul en priorité : la fiche
de lecture — index des mesures et fiches de mesure principale. Le PLF est hors du
champ de ce fil ; il n'est pas suspendu, il est traité ailleurs.

**Mesure de présence, en entrant.**

- Pièce : `PLFSS_2027.pdf`, texte soumis à la délibération du Conseil des ministres,
  NOR CPPX2620963L/Bleue-1. **121 pages.** sha256
  `71010873c0af8a776436e3c22628d3a1dc048ea406632afa2107dc83be7c598d`.
- **49 articles relevés** : un article liminaire et les articles 1er à 48. Compte
  mécanique, sur la ligne de titre d'article isolée.
- **Index des mesures du PLFSS : absent du coffre.** Le millésime 2026 porte
  `livrables/index_mesures_plf.md` et `referentiels/index_mesures_plf.tsv` — PLF
  seulement. Le fil l'a donc produit au même gabarit, comme son mandat le prévoit.
- `appareil/index_mesures.py` : **absent du clone**, et déjà déclaré trou de
  déclaration au paquet de dépôt des courroies du 20261001. Le fil a rendu sans lui,
  par une grammaire de relevé locale déclarée au fragment d'arbitrages.
- `appareil/confronter_lecture.py` : présent à l'index, non joué — la confrontation
  relève des blocs L1 à L4, non du premier rendu.
- Annexes 3, 4 et 9 : **non jointes**. L'annexe A, rapport pluriannuel 2027-2030,
  est en revanche **dans la pièce**, pages 113 à 121, et n'a pas été dépouillée par
  cette passe.

**Ce qui est fait.**

- `livrables/index_mesures_plfss_2027.md` — **314 mesures sur 49 articles**, dont
  **95 à siège vide**. Gabarit de `livrables/index_mesures_plf.md`, repris tel quel,
  chapeaux comptés comme mesures comme en 2026.
- `livrables/fiches_mesures_plfss_2027.md` — **33 fiches couvrant 36 des 49
  articles**, au critère de mesure principale du prompt de fil.
- `livrables/lecture_plfss2027_lisible.md` — **la note externalisable**, au format
  arrêté le jour même par le fil de lecture du PLF 2027 et repris tel quel :
  en trois phrases, combien exactement, ce qui change pour les gens, qui paie, la
  dette et la trésorerie, les trois choses à surveiller, les incohérences relevées.
  *Oubli du premier rendu, rattrapé après rappel de l'auteure : le format existait,
  il n'a pas été cherché. Réutilisation avant réinvention.*

**Agrégats rejoués, recette déclarée avant exécution.**

| agrégat | recette | résultat | ligne du texte |
|---|---|---|---|
| soldes de branche 2026 (art. 1er) | somme des cinq soldes | −21,8 | −21,8 — concordant |
| soldes de branche 2027 (art. 16) | somme des cinq soldes | −12,7 | −12,7 — concordant |
| sous-objectifs ONDAM 2026 (art. 2) | somme des six lignes | **273,5** | **273,3** — écart 0,2 |
| sous-objectifs ONDAM 2027 (art. 43) | somme des six lignes | 278,7 | 278,7 — concordant |
| objectifs de branche (art. 42, 45 à 48) | comparaison à la colonne Dépenses de l'art. 16 | 5 égalités | 5 sur 5 |
| dotations aux opérateurs (art. 41) | somme des I à XI, puis + XII | 1 170,35 puis 1 400,88 M€ | — |
| dette amortie fin 2026 | 274,7 (LFSS 2026) + 16,0 (art. 1er, 3°) | 290,7 | 290,7 — concordant |

**Sept écarts relevés, aucun arbitré** : total ONDAM 2026 contre somme de ses
sous-objectifs ; total ONDAM 2026 contre l'exposé des motifs (274,4) ; compensation
des exonérations, 8,9 au dispositif contre 8,87 à l'exposé ; contribution CNSA aux
ARS, « 2027 » au dispositif contre « exercice 2026 » à l'exposé ; renvois internes
non remplis à l'article 13 — « l'article XX de la loi XXX » ; référence à
« l'article L. 1613 ter du code général des impôts », quand le code porte un article
1613 ter sans lettre ; branche AT-MP, +1,3 Md€ à l'exposé de l'article 45 contre
+1,4 aux tableaux. Un huitième item, de même nature, est porté à la note lisible :
l'affectation du produit de la taxe sucre au régime agricole est annoncée à l'exposé
de l'article 8 et **n'a de siège dans aucune de ses dispositions**.

**Deux divergences de gabarit avec 2026, constatées et non corrigées.**

1. **Le texte 2027 titre ses articles.** La liste 2026 note que « le texte ne donne
   aucun titre à ses articles ». Le PLFSS 2027 en porte un pour chacun, centré sous
   le numéro. L'index les reprend du texte ; ce ne sont plus les nôtres.
2. **Trois parties, non quatre.** Première partie : rectification de 2026. Deuxième :
   recettes et équilibre 2027. Troisième : dépenses 2027. Aucune partie ne porte sur
   le dernier exercice clos. Constaté, non qualifié — la grille des portes du domaine
   des lois de financement n'est pas relevée et ce fil ne la relève pas.

**Piège du véhicule, mesuré.** Les tableaux vivent bien dans les alinéas et non
hors-alinéa : les tableaux d'équilibre des articles 1er et 16, le tableau ONDAM des
articles 2 et 43, les barèmes de l'article 8 et la répartition départementale de
l'article 13 sont tous dans des alinéas numérotés. Aucune conclusion au trou n'a été
tirée avant d'avoir regardé là. Les lignes brutes des tableaux ont été conservées ;
aucun n'a été aplati en prose.

**Trois bornes tenues.** Aucun verdict rendu — le bloc L4 n'est pas joué, et il
plafonnera à `plaidable`. Aucune de nos mesures raccrochée au texte lu. Le PLF 2027
déclaré traité ailleurs, jamais suspendu.

**Ce que le fil ne rend pas, et qui reste ouvert, dans l'ordre du mandat.**

1. **L1** — le solde et sa construction : équilibre par branche, objectif national de
   dépenses, effets de périmètre. L'annexe A, présente dans la pièce aux pages 113 à
   121, est la matière qui reste à dépouiller.
2. **L2** — les portes ouvertes, couples (texte, article) que le véhicule modifie
   lui-même. L'index en porte la matière brute : 314 mesures, dont 219 à siège relevé.
3. **L4** — l'écart à nos positions, chaque proposition du corpus confrontée au texte,
   verdict plafonné à `plaidable`, jambe unique déclarée.
4. **L3** — mouvements sur nos objets, portés par le véhicule seul.
5. **Rubriques suspendues** : L3.b dépenses fiscales et le détail des économies de
   l'ONDAM attendent les annexes 3, 4 et 9, non parues au dépôt. Elles se rejouent
   seules à leur arrivée, sans toucher au reste.

**Reprise due, portée ici faute d'endroit où le fil suivant la lirait autrement.**
Le prompt de fil `methode/prompt_fil_lecture_textes_2027.md` ne nomme pas la note
lisible parmi ce que le fil rend — il s'arrête à l'index et aux fiches. Les deux fils
du 20261001 l'ont pourtant produite. **La pièce est à inscrire au prompt de fil**,
sans quoi le millésime suivant la perdra. Porté à `methode/a_trancher.md` par ce fil
si l'auteure ne tranche pas avant.

## 20261001 — liste-plfss-2027

**Mandat.** Rendre `livrables/PLFSS2027_liste.md` au gabarit arrêté le jour même sur
le PLF 2027, puis le PDF par le script. Deux pièces, pas une de plus.

**Mesure de présence, en entrant.** `reference/gabarit_liste_articles.md` : présent,
fait foi. `livrables/rendre_liste_pdf.py` : présent. `markdown` et `weasyprint` :
absents de l'atelier, installés. Polices `TeX Gyre Termes` et `Liberation Serif` :
présentes. `livrables/PLFSS2027_liste.md` existait déjà, hors gabarit : **modifié,
non reconstruit.**

**Ce qui est fait.** La liste au gabarit — en-tête dans l'ordre prescrit, deux
partitions, verbe en tête de ligne, grandeurs en gras, remarque en italique, quatre
lignes au plus. **49 articles**, rendus sur **5 pages**.

**Contrôle joué.** Substitution du script rejouée sur le markdown, comptage des
`<span class="art">` : **49 sur 49**, **zéro `<li>` sans numéro**. Un article non
reconnu aurait perdu numéro et pastilles sans que le PDF ne signale rien.

**L'annexe A, qui n'avait pas été dépouillée, l'est.** Elle change la lecture du
texte sur trois points, portés à la liste :

- **L'amélioration de 9,1 Md€ ne tient pas** : le déficit remonte à **−14,4 Md€ dès
  2028** et **−17,0 en 2030**, « en raison notamment du caractère non pérenne » de la
  contribution des complémentaires, reconduite pour la seule année 2027.
- **1,6 Md€ d'économies sur les prestations familiales** — maintien au niveau de
  2026 pour 0,5, action sociale 0,5, allocation de rentrée scolaire 0,6 — **dont
  aucune n'a d'article dans le texte**. Idem pour **1,2 Md€** de hausses de tickets
  modérateurs décidées par voie réglementaire en 2026 et comptées dans l'ONDAM 2027.
- **L'écart à la loi de programmation est chiffré** : **−0,6 Md€** de dépenses en
  2026, **−9,6 Md€** en 2027, ONDAM à **2,0 %** contre **2,9 %** en programmation.
  *La programmation ne porte pas de cible de solde sur ce champ : elle n'est
  invoquée que pour caler des taux au-delà de 2027.*

**Un écart de plus, relevé et non arbitré.** La revalorisation différenciée des
pensions est chiffrée **trois fois** : 4,0 Md€ à l'exposé de l'article 35 sous
hypothèse de gel, 3,0 à l'annexe A après effets de CSG, 4,5 à l'annexe A dans
l'écart à la programmation. Et le seuil diverge : **1 281 €** au texte et à son
exposé, **1 260 € par mois** à l'annexe A.

**Deux lignes portées au gabarit**, là où la règle est lue, et nulle part ailleurs :
le numéro d'article doit tenir dans sa colonne de 7,5 mm — **l'article liminaire se
note `lim.`**, faute de quoi la césure sort « limi‐naire » —, et le contrôle de
rendu en une ligne. *Y est aussi inscrit ce que la loi de financement a de propre :
ses deux partitions, l'exception de référentiel pour les transferts vers les
complémentaires et les départements, et le fait que l'annexe jointe est de la pièce.*

**Reprise due, nommée ici parce que je ne l'ai pas faite.** `PLF2027_liste.md` porte
encore `liminaire` et subira la même césure à son prochain rendu. Un mot à changer.

## 20261001 — outillage-textes-2027

**Mandat.** Outiller la machine sur les textes 2027 comme elle l'avait été sur
2026 — produire, au schéma du millésime 2026, ce que la chaîne consomme.

**Ce qui est fait.**

`appareil/socle_texte_2027.py` — le socle des deux véhicules depuis le PDF
déposé. Une entrée par article : numéro, partie, intitulé, rédaction exacte,
folio imprimé, exposé des motifs rattaché. **PLF 2027 : 90 articles**, liminaire
plus 1 à 89, 57 en première partie et 32 en seconde, folios 33 à 268.
**PLFSS 2027 : 49 articles**, liminaire plus 1 à 48, sur trois parties, folios 1
à 112. Aucun article sans intitulé, sans dispositif ni sans exposé.

`appareil/portes_ouvertes.py` — le module que l'index déclarait manquant. Il
rend `referentiels/articles_ouverts_<véhicule>2027.tsv` au schéma de 2026, celui
qui alimente la colonne `variante` de `REF_norme`. **PLF : 449 adresses,
56 textes. PLFSS : 191 adresses, 23 textes** — et c'est le premier relevé de
portes jamais fait côté loi de financement, 2026 compris n'en ayant qu'un pour
chaque véhicule.

`appareil/pieces_nommees.py` — la table close des pièces, neuve.

**Contrôles joués, tous mécaniques.** Déterminisme du socle et du relevé : deux
exécutions, même empreinte. Couverture : aucun numéro d'article manquant sur les
deux véhicules. Jeu de fautes sur le socle — article retiré, dispositif vidé,
folio cassé : les trois levés. Jeu de justes sur le blanchiment — un siège cité
entre guillemets n'en ressort pas ; un siège modificatif y survit.

**Ce qui reste ouvert.** Les blocs L1 à L4 ne sont pas joués. Le module
`controle_socle_plf.py` n'est pas écrit. L'attribution de pièce porte le défaut
du millésime 2026 et il est déclaré au fragment d'arbitrages du jour. Les deux
socles pèsent 1,27 Mo et 344 ko : ils restent à l'atelier, le coffre ne reçoit
que les modules et les deux référentiels.

**Dépôt.** Les trois modules sont de voie `depot` et un fil Cowork ne pousse
pas : ils attendent une session `claude.ai/code`, avec le paquet de courroies du
jour qui n'a pas abouti.

## 20261001 — plan-vehicule

**Mandat.** Deux temps, le second conditionné au premier. Temps 1 : porter au plan sept
phases une seconde dimension — PLF première partie, PLF seconde partie, PLFSS — et faire
trancher par l'auteure ce qui commande l'ordre quand phase et véhicule divergent, et ce qui
se publie par véhicule plutôt que par phase. Temps 2 : porter à
`livrables/arborescence_mesures_20260928.md` les trois arbitrages du 20260930 et les trois
reprises qu'ils ouvrent. Fil au projet doctrine : `disposition-cible`,
`redaction-legistique` et `expose-sommaire` n'ont pas été activées.

**Correction du mandat en cours de fil.** Le fil commanditaire a retiré du temps 1 la reprise
de la règle de rattachement : un texte financier en discussion n'est pas du droit en vigueur,
la règle n'est donc pas périmée par le dépôt du PLF 2027, et le point est porté par le fil de
lecture des textes financiers 2027. La question avait été posée à l'auteure et n'a pas été
jouée. Le temps 1 s'est limité à la dimension véhicule.

**Temps 1 — rendu.** Une question fermée posée, une répondue : la règle de l'entonnoir. Le
véhicule commande l'entrée dans une phase, la phase commande la suite ; la publication se
fait par phase en bloc, le dépôt jambe par jambe au rythme des fenêtres. `methode/plan_sept_phases_20260930.md`
gagne une section « La seconde dimension — le véhicule » portant les trois colonnes, la règle
du calendrier de publication et l'entonnoir, et une note de renvoi sous « Base de travail »
pour que la question du rattachement ne se repose pas à chaque dépôt. Aucune ventilation des
mesures en jambes.

**Première question mal rendue.** La question initiale a été posée par le widget de choix et
l'auteure n'a pas pu la lire en entier à l'écran. Reposée en texte clair, elle a été
répondue. *À retenir : une question fermée se pose en clair dans le fil, pas dans un
composant qui tronque.*

**Temps 2 — rendu.** Six éditions à l'arborescence, aucune reconstruction.

1. En-tête — ligne de reprise du 20261001 ajoutée.
2. Section « Pas de cas nommés » — la règle devient un principe de présentation, opposable à
   l'exposé des motifs et à l'exposé sommaire, et cesse de borner le dispositif, qui peut
   porter une liste close fondée sur des critères.
3. M-002 — la borne « critère ou liste : les 750 structures visées » est remplacée par une
   ligne `TRANCHÉ` : liste close organisée par les critères, 746 lignes, 78 cessions et 668
   suppressions, 8,632 Md€ tenus, hors champ rappelés, ordre des critères laissé ouvert
   comme tambouille.
4. M-016 — la borne « champ association : fléchage local inclus ? » est remplacée par une
   ligne `TRANCHÉ` portant le tiers non public et non lucratif quel que soit le payeur, et
   une ligne `SCISSION` neuve porte les deux jambes PLF et PLFSS, avec le montant du versant
   social déclaré non ventilé.
5. M-026 — la borne « liste des ~30 Md€ de secteurs écartés » est remplacée par une ligne
   `TRANCHÉ` : exception de calendrier et non de champ, aucune niche conservée, liste du
   classeur qualifiée d'hypothèse de chiffrage, durée de la progressivité laissée ouverte.
6. M-026, composante `TRANSITION` — « Suppression immédiate, solde dans la refonte » devient
   « Deux vitesses — suppression immédiate d'un côté ; extinction progressive avec restitution
   renvoyée à la refonte fiscale de l'autre ».

Les trois bornes fermées ne sont pas supprimées en silence : elles sont remplacées en place
par la décision qui les ferme. C'est une décision de tambouille, inscrite au fragment
d'arbitrages du jour.

**Ce qui n'a pas été fait, et c'est le mandat.** Aucune ventilation des 66 mesures en jambes,
aucune autre borne tranchée. La qualification se fait au projet machine.

**Ce qui reste ouvert, et qui n'est pas de ce fil.** L'ordre des critères d'organisation de la
liste de M-002. La durée de la progressivité de M-026 et son écriture par secteur ou en bloc.
Le montant du versant social de M-016. Les trois sont inscrits aux lignes `TRANCHÉ` et
`SCISSION` de l'arborescence, là où le fil suivant les lira.

**Assemblage.** `appareil/fragments.py` n'est pas au clone : ce fil dépose, il n'assemble pas.
`journal.md` et `arbitrages.md` au coffre ne portent ni ces deux fragments, ni les deux du
20260930 qui attendent déjà.

## 20261001 — reprise-grille-lecture

**Mandat.** Corriger les consignes défaillantes relevées par les deux fils de
lecture des textes financiers 2027, et propager la correction aux pièces déjà
versées.

**Mesure d'entrée.** Deux index versés le même jour, deux grilles de relevé
différentes : le fil PLF avait arrêté sept règles, chacune imposée par une
divergence mesurée ; le fil PLFSS avait écrit la sienne sans les lire. **Faute de
réutilisation**, pas de méthode.

**Ce qui est fait.**

1. **Grille reprise.** Les sept règles du fil PLF portées à la grammaire du PLFSS.
   Delta : **314 → 251 mesures**, **95 → 68 sièges vides**, profondeur ramenée de
   quatre niveaux à deux. Le blanchiment des passages cités pèse le plus — l'article
   9 passe de 20 à 6 adresses.
2. **Quatre pièces du PLFSS régénérées ou recomptées** : index, fiches (une fiche
   ajoutée, l'article 4, qui entre au critère sous la grille reprise), liste par
   article, note lisible.
3. **`methode/prompt_fil_lecture_textes_2027.md` corrigé**, là où la règle est lue.
   Six corrections, chacune signalée dans le texte : les **quatre** pièces de
   lecture au lieu de deux ; la grille de relevé en sept règles ; le critère de
   mesure principale à la maille de l'article, avec versement des non-retenus ; la
   consigne d'entrées en vigueur différées **bornée au relevé interne**, le reste
   étant hors mandat et renvoyé à `a_trancher` ; la règle que les intitulés
   d'article ne sont pas acquis d'un millésime à l'autre ; et l'obligation, pour le
   fil qui lit le second véhicule, de lire d'abord ce que le fil du premier a versé.

**Ce qui n'est pas fait, et pourquoi.** Les fiches des articles 20, 28 et 32 étaient
retenues au titre des articles les plus chargés sous l'ancienne grille ; elles n'y
sont plus. Elles sont **conservées et déclarées**, non retirées : la règle du fil PLF
est qu'un critère de sélection se reprend par l'auteure, pas à la main par le fil.
Porté à `methode/a_trancher.md`.

**Ce qui reste ouvert, inchangé.** Les blocs L1 à L4 du PLFSS ne sont pas joués.
Les questions de fond 40 à 42 du § B restent non tranchées.

## 20261001 — tenue-apres-poussee

Fil de tenue, après la poussée de la table curée. Les trois temps mandatés ont
été mesurés, deux se sont révélés destructifs ou impossibles, et le fil a été
rendu responsable de la réparation. Ce fragment porte la mesure et la
réparation.

## La mesure

**Le clone.** `main` à `45fea39`, seize refs balayées, 180 chemins distincts.
Le dépôt porte `chantier/Makefile`, `chantier/appareil/`,
`chantier/referentiels/` (5 JSON), plus `data/`, `codes.json`, `droit.py`,
`essai.py`, `extraire_legi.py`, `README.md`. **Aucun chemin `methode/`,
`livrables/`, `reference/`, `livre/`, `input/` ni `archive/` sur aucune ref, à
aucun moment de l'historique.** Le dépôt ne porte pas et n'a jamais porté le
coffre lisible : la règle de délestage, qui veut une présence au clone, était
inapplicable depuis le jour où elle a été écrite.

**`methode/journal.md` est perdu.** Sorti du projet le 20261001 sur cette
présence supposée. Introuvable au coffre, au dépôt et dans tout transcript
atteignable. Seule reste son empreinte au relevé du 20260930 : sha256
`faad6e94…`, 295 275 o, 4 875 lignes.

**L'assemblage des arbitrages était destructif.** Cumulatif restauré à
345 467 o, tête 292 687, queue 52 700 portant 11 sections. Assemblage joué sur
copie jetable : 335 604 o, 35 sections, **11 perdues** — les fragments de
20260917, 20260921, 20260923 et 20260924 ne sont plus au coffre. Deux de ces
onze n'ont jamais eu de fragment : écriture à la main sous la marque. La perte
ne coûtait que 9 863 o : **la taille ne voit pas la faute, seules les sections
la voient.**

**L'index régénéré rend 363 artefacts** — 305 au coffre, 99 au dépôt, 90
dérivés, 43 sources, 15 manquants, 2 sans famille. Le compte exact qu'annonçait
le paquet de courroies ; le rattrapage des 48 est effectif.

## La réparation

**Archive.** Les 172 documents du projet écrits par copie d'octets depuis le
transcript, via dix-neuf fils auxiliaires servant de tuyau. Empreintes relevées
à neuf sur l'ensemble : 246. Archive remise à l'auteure,
`coffre_resolution_20261001.tar.gz`, 5 501 055 o décompressés, sha256
`776b1606…`. **Relecture après écriture : 172 conformes, 0 divergent, 0
absent.**

**Poussée refusée.** Le mandataire git rend un 403 :
`resolution-ib-dev/Resolution-2027` n'est pas aux sources autorisées de la
session. Le commit d'archive (`6559a6b`, branche `coffre-20261001`) existe en
atelier et sera perdu avec lui.

**Délestage.** 15 documents sortis, 1 617 384 o — la liste de l'étape 3 du
socle, que la présence établie rendait enfin jouable. Registre à
`methode/sorties_du_projet_20261001.md`, une ligne par pièce avec taille et
sha256. **Aucun fragment n'est sorti.**

**`methode/index.json` versé** à 363 artefacts.

**`methode/arbitrages.md` rebâti.** Les 11 sections sans fragment reprises
verbatim au-dessus de la ligne de marque, où rien ne les réécrit, puis
assemblage des 14 fragments. 390 475 o, 79 sections, **0 perdue**, rejeu
inchangé.

**`methode/journal.md` rebâti.** Tête neuve portant le constat de la perte et
l'empreinte du document disparu, pour qu'une copie retrouvée se reconnaisse et
se remette ; puis assemblage des 13 fragments. 58 995 o, 21 sections, rejeu
inchangé.

**Socle corrigé.** Trois conditions cumulatives à toute sortie, l'interdiction
absolue de sortir un fragment, et l'obligation de jouer un assemblage sur copie
jetable en comptant les sections.

## Ce qui reste ouvert

La poussée de l'archive, bloquée sur les sources autorisées du projet. Le
binaire de `input/Note_Retraite_20250619.docx`, que le coffre ne rend qu'en
texte. Les deux pièces d'appareil dues — la cible `a_trancher` et le contrôle
d'assemblage. La dette de table curée née après le paquet du 20261001.

## 20261002 — arbitrages-de-forme

**Fil 1 de la carte des dix fils — conversation. Il ne déplie rien, ne joue aucun
`make`, et n'ouvre aucun référentiel du millésime.**

**Lu en ouverture** : `methode/passation_20261002.md`,
`methode/contrat_chaine_amendement.md`, `methode/socle_prompt_fil.md`,
`methode/controle_avant_transmission.md`, `methode/carte_des_chantiers.md`,
`methode/a_trancher.md`, `methode/arbitrages.md`,
`livrables/valise_phase1_20261002.md`,
`reference/cgi_expert_regles_de_lecture.md`, puis
`reference/gabarit_expose_sommaire.md` sur demande de l'auteure.

**Vérification au registre avant de poser les questions** — application de la
règle du 20261001. Le registre a été balayé sur les quatre sujets. **Aucun des
quatre n'y est clos** : les quatre questions du § 6 étaient ouvertes pour de bon.

## Ce qui a changé au corpus

**Quatre arbitrages de forme rendus.** Dates IR et IS : régime mixte par type
d'avantage. Progressivité de M-026 : trois rangs en cascade, défaut en flux.
Affectations : le traitement se lit sur le sort du bénéficiaire. **Taxe sur la
valeur ajoutée : trois états dans la journée, et le troisième vaut** — les 21
taux réduits restent en phase 1 au 1er juillet 2027, en jambe propre hors clause
générale, corrélés aux suppressions de taxes sectorielles de même date.

**Trois règles transversales** : un arbitrage se rend en règle et non en liste de
cas ; une contrepartie se corrèle et ne s'affecte pas ; une question de date se
pose avec son effet net, jamais comme un calendrier.

**Trois chantiers levés, inscrits, non ouverts** — règle d'entrée en vigueur,
réservoir d'arguments du livre, croisement taxes supprimées / taux réduits. Le
§ 5 de la passation passe de trois à six chantiers hors plan.

**Deux fautes nouvelles au § 7** : un rôle du contrat se mesure rempli ou vide ;
une question posée à nu reçoit une réponse qu'il faut révoquer.

**Une règle de tenue, tranchée par le fil** : la passation ne porte plus le texte
des arbitrages, seulement leur état et le renvoi au registre. Elle a été
réécrite trois fois en une heure parce qu'elle dupliquait ce que le fragment
portait déjà. Le § 6 est désormais un tableau de quatre lignes.

## La mesure qui a produit le chantier du livre

Question de l'auteure : les exposés exploitent peu les idées et les sources du
livre — y ont-ils accès et indication ?

**Mesuré, et la réponse est non aux deux.** Le projet machine porte le socle, les
six référentiels du millésime et quatre classeurs. La valise phase 1 remplit le
rôle « réservoir d'arguments sourcés » avec les onze principes de l'auteure et
rien d'autre. Aucune note de fin du manuscrit n'a jamais atteint un fil de
production. **Et la règle ne l'interdit pas** : le gabarit pose que le livre ne
fait pas source (A-49), et dans la même ligne que ce qui s'affiche est ce que le
livre cite lui-même.

## Ce qui reste ouvert, et qui n'est pas de ce fil

- Le net en euros par secteur de la corrélation TVA / taxes sectorielles : **non
  mesurable** avant la parution de l'annexe des dépenses fiscales 2027. Le
  croisement des périmètres, lui, est calculable aujourd'hui — fil 13.
- La collision entre la jambe TVA de M-026 et M-029 sur `278` et `278-0 bis` —
  portée au fil 8.
- Le critère qui désigne un secteur sensible ou signalé, rangs 2 et 3 de la
  progressivité.
- La lecture retenue de « compensation contemporaine molle » et le maintien de la
  jambe TVA dans M-026 plutôt qu'en treizième mesure : **les deux sont du fil et
  révocables en une ligne**.

**Les quatre bornes de fond du § 6 ne sont pas touchées.**

**Dette d'appareil, et elle grossit.** `appareil/fragments.py` n'est pas jouable
depuis Cowork : ce fil **dépose** ses deux fragments et **n'assemble pas**. Le
§ 11 de la passation porte désormais le dossier des fragments dans ce qu'un fil
neuf lit en ouverture — faute de quoi il lira un registre amputé de tout ce qui
a été déposé depuis le 20260917.

## 20261002 — bascule-et-liasse-de-nuit

# Journal — bascule de fil et liasse de nuit (2 octobre 2026)

## La liasse de nuit est arrivée

Douze pièces, PLF 2027 première partie, rédigées le 2 octobre sur le texte initial
déposé le 1er octobre, droit lu sur l'extrait LEGI du 1er octobre. Toutes portent
le bandeau « projet de travail — ne pas déposer en l'état » et leur liste de
reprises, non intégrées.

État déclaré par la liasse : 4 pièces à reprendre (01, 02, 03, 08, 12), 7 à
vérifier sur précédent. Points communs relevés : ligne « présenté par » vide,
entrées en vigueur à revoir selon les arbitrages, clause type de restitution
restée à rédiger, exposés renvoyant à une « phase suivante » — renvoi à supprimer,
chaque exposé devant se lire seul.

Collisions déclarées : 01, 03 (part impôt sur le revenu) et 04 à 11 sont des
replis de 02 et ne se cumulent pas avec lui.

## Ce que la clause de lien change pour cette liasse

La clause type manquante est désormais arrêtée (voir l'arbitrage du même jour).
Reprise à passer sur les douze : remplacer les entrées en vigueur rédigées au jugé
par la forme G ou H selon la nature de la jambe, et déplacer les renvois croisés
du dispositif vers l'exposé.

## Bascule de fil

Le fil courant a déjà été compacté une fois. Un fil code tourne encore (entrées
code de la fonction publique et loi de financement 2026 au référentiel des codes,
puis extraction des articles). La bascule ne se joue pas avant son retour : son
résultat doit être intégré par le fil qui l'a lancé.

Ordre arrêté : retour du fil code → intégration → ouverture d'un fil de
conversation neuf pour le rebasage des douze pièces, avec en entrée la passation
du 2 octobre, l'ordre des fils, l'arbitrage sur la clause de lien et l'archive de
la liasse de nuit. Le fil courant ne produit plus de pièce après la bascule.

## 20261002 — mesure-depot

**Mesure rendue par le fil code du 20261002, et deux mesures du fil chef de file.
Aucun fond produit.**

## Ce que le fil code a mesuré, et pourquoi il s'est arrêté

**Le paquet des courroies est déjà appliqué.** Les trois blocs sont dans le code,
chacun une fois et à l'identique — 125 lignes dans `ARTEFACTS`, 6 dans
`COFFRE_DOCUMENT`, 51 dans `IMPLICITES` —, entrés par le commit `f8834f3` du
20261001 à 11 h 55, déjà dans `origin/main`. Le compte « avant » vaut **363
artefacts et 361 classés**, et non 315 et 313.

Le fil s'est arrêté à l'étape 1 et n'a rien inséré. **C'est le comportement
juste** : réappliquer le paquet aurait déclaré les 48 documents en double. Le
paquet a été mesuré sur `4e6e1a4` et son état de départ est périmé.

**`methode/paquet_depot_courroies_20261001.md` est donc épuisé.** Plus aucun
paquet n'attend d'application. La dette de voie `depot` est nulle.

**Poussée.** Aucun `403` : l'essai à vide `55cfd14` est passé. Le mandataire git
n'est plus le verrou — **la poussée depuis une session de code fonctionne**.

**Mesure d'entrée, et c'est la sortie utile du fil.** `chantier/appareil/`
contient 97 fichiers. **Quatre des cinq modules du millésime 2027 y sont** —
`socle_texte_2027.py`, `pieces_nommees.py`, `portes_ouvertes.py`,
`index_mesures_2027.py`. **`redaction_2027.py` est absent.**

*Reste non mesuré, et il le reste faute d'accès : si le `portes_ouvertes.py` du
dépôt est bien celui corrigé le 20261002, ou l'état antérieur. À confronter au
prochain passage, par empreinte.*

## Deux mesures du fil chef de file

**Le dépôt n'est pas accessible depuis une session Cowork.** Ni clone, ni API
REST : « GitHub access to this repository is not enabled for this session ».
Conséquence qui n'était pas écrite : **un fil Cowork ne peut pas davantage
mesurer le dépôt qu'y pousser.** Toute mesure du dépôt passe par une session de
code. Le partage « Cowork mesure et écrit le paquet » vaut pour le coffre, **pas
pour le dépôt**.

**Ce qui est parti aux tiers au millésime précédent n'était pas la machine.**
`livrables/paquet_machine.md` porte le paquet du 20260916 : `PASSATION.md`, le
découpage en 71 énoncés, l'index de vérité-terrain gelé et la valise. Aucun
module, aucun référentiel de sièges, aucun code — le paquet déclare lui-même que
le référentiel de sièges est **vide par construction**, parce qu'il servait à
mesurer un écart.

**Le paquet 2027 est donc un objet neuf, pas une reconduction.** Il porte la
chaîne elle-même : modules, référentiels du millésime, accès au droit, mode
d'emploi, mini-lot. Sa spécification est à
`methode/controle_avant_transmission.md`, et ce document est calibré sur quatre
modules et quatre référentiels quand le millésime en porte cinq et six.

## 20261002 — organisation-et-deploiement

**Fil chef de file — conversation. Il ne produit aucun fond.**

## La mesure d'entrée, et elle a invalidé le mandat que j'allais écrire

Avant d'écrire la ligne de lancement du fil code, recherche au corpus sur les
paquets de dépôt. **Trois bornes que je portais sont périmées.**

**`appareil/fragments.py` est au clone depuis le 20260930.** L'assemblage des
fragments se fait depuis Cowork et n'attend **aucune** session de code. La limite
du 20260917 a été levée le 20261001, mesurée levée, et écrite levée au journal.
**Je l'ai pourtant recopiée trois fois dans la journée**, dont une fois au § 8 de
la passation en la qualifiant de « dette qui coûte le plus cher ». Deuxième
occurrence du mécanisme en deux jours.

**La dette des six paquets de dépôt antérieurs est nulle.** Les 99 chemins que
l'index déclare au dépôt y sont tous. Ces paquets ne sont plus des documents du
projet. La section « Dette d'appareil » d'`a_trancher` est périmée sur ce point.
J'allais en nommer cinq dans une ligne de lancement.

**`methode/controle_avant_transmission.md` est calibré sur quatre modules et
quatre référentiels.** Le millésime 2027 en porte cinq et six.

**Règle qui en sort, et c'est la contre-mesure qui manquait** : *une borne se
vérifie par une recherche au corpus sur le nom de la pièce, jamais par la
relecture du document qui la porte.* Un document de méthode ne sait pas qu'il
est périmé ; la pièce, elle, est datée.

## Ce qui a changé au corpus

**Trois décisions de l'auteure, portées à
`methode/fragments/arbitrages/20261002-organisation-et-deploiement.md`.**

L'ordre des fils passe au fil chef de file — **révocation de la règle « l'ordre
des lots est de l'auteur »**, portée deux fois à `a_trancher` et au socle. Le
fond, l'input et l'output restent à l'auteure.

Le livre devient le réservoir d'arguments de fond, avec la distinction qui
manquait : **il fait argument, ses notes font citation**. A-49 intact. Quatre
bornes d'emploi, et un contrôle négatif : aucun exposé ne reprend un argument mot
à mot.

La remise en cohérence devient **récurrente** — une passe après chaque paire de
fils de rédaction, plus une seule à la fin.

**Pièce neuve : `methode/ordre_des_fils.md`**, qui porte les deux chantiers
parallèles, leurs dépendances et les trois boucles. Le § 10 de la passation n'y
renvoie plus que par une ligne — il ne porte plus la table.

**`methode/passation_20261002.md` repris** : § 2, 5, 6, 7, 8, 9, 10 et 11. Le
§ 8 est réécrit entier, les bornes périmées retirées et l'état réel substitué.

## Ce qui reste ouvert

- Lesquels des cinq modules du millésime 2027 sont effectivement au dépôt :
  **non mesuré**, et c'est la mesure d'entrée du fil code. L'index déclare
  `portes_ouvertes.py` manquant ; la passation le dit corrigé hors dépôt. Tant
  que ce n'est pas tranché par la mesure, **la passe 1 de la transmission n'est
  pas jouable**.
- L'assemblage des fragments — fil Cowork, en tête de l'ordre, sans dépendance.
- Les quatre bornes de fond de la phase 1, inchangées.

## 20261009 — site-publier-desactive

## Ce qui a changé au corpus

- `make publier` refuse au lieu de régénérer et pousser le site : le site se
  maintient à la main dans `Site-ETNP/site/` (PR #18). `CLAUDE.md` dit où le
  site se publie désormais.
- Côté Site-ETNP : README et CLAUDE.md décrivent la procédure manuelle, script
  de capture `outils/capture.mjs`, note de report au référentiel supprimée.

## Ce qui reste ouvert

- `appareil/generer_site.py` et `appareil/generer_carte.py` mentionnent encore
  `make publier` ; ils ne servent plus au site.
