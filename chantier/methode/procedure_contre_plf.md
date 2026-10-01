# Procédure contre-PLF — la carte des fils

Écrite le 20260831, fil de conversation, corrigée le même jour par l'auteur. Elle
ne produit aucun fond : elle dit par où on entre, dans quel ordre, ce que chaque
fil demande, ce qu'il rend, et ce qui garantit que rien ne se déforme en route.

Elle se lit avec `methode/carte_des_chantiers.md`, qui dit ce que le chantier
couvre, et avec la skill `resolution-chantier`, qui dit comment on travaille.

---

## Ce qui a changé le 20260831

**Le chantier a doublé de véhicule.** Le PLFSS entre au périmètre. **Le PLF reste
prioritaire** — arbitré par l'auteur, et cet ordre ne se rediscute pas. On fait
les deux, dans cet ordre.

**Le normage juridique sort du contre-PLF.** Il devient une couche du corpus, au
même rang que `REF_chiffres`. Le contre-PLF n'en est qu'une vue.

**Le pack public part avant tout amendement.** Il ne dépend d'aucun texte,
d'aucun dépôt, d'aucune stratégie parlementaire.

---

## Les deux textes, et leur source

| | PLF 2026 | PLFSS 2026 |
|---|---|---|
| numéro | 1906 | 1907 |
| dépôt | 14 octobre 2025 | 14 octobre 2025 |
| page | `assemblee-nationale.fr/dyn/17/textes/l17b1906_projet-loi` | `…/l17b1907_projet-loi` |
| PDF | `…/l17b1906_projet-loi.pdf` | `…/l17b1907_projet-loi.pdf` |
| HTML structuré | `…/dyn/opendata/PRJLANR5L17B1906.html` | `…/dyn/opendata/PRJLANR5L17B1907.html` |
| amendements déposés | `…/dyn/17/amendements?dossier_legislatif=DLR5L17N52428` | `…?dossier_legislatif=DLR5L17N52922` |

Structure relevée du PLFSS : article liminaire, première partie, deuxième partie
titre I (recettes), titre II (équilibre), puis les dépenses. Le PLF a sa structure
propre, à relever à l'extraction.

**Le point d'accès aux amendements est la pièce la plus sous-estimée.** Il porte
tous les amendements déposés sur chaque texte, avec leur sort — irrecevable,
retiré, rejeté, adopté. Il sert deux fois : il valide la grille de recevabilité
contre du réel, et il fait la lecture en creux à notre place (voir plus bas).

---

## La règle qui commande tout le reste — d'où vient le verbatim

**L'outil de récupération web fait passer le texte par un modèle. Il ne rend
jamais du verbatim.** Il sert au repérage, à la structure, aux adresses. Jamais à
la copie.

**La passerelle de sortie de l'atelier n'admet que les registres de paquets**
(A-196). Aucun texte ne se télécharge depuis un fil de production.

**Donc le verbatim entre par pièce jointe du fil**, déposée par l'auteur. Les
pièces jointes de conversation ne comptent pas dans la jauge du coffre — c'est ce
qui rend la chose possible : le coffre est à 1 750 682 sur 2 000 000, et un PDF de
4 251 Ko n'y rentrerait pas.

**Ni le PLF ni le PLFSS ne vont au coffre.** Documents publics, retéléchargeables
à l'identique : A-71 s'y applique en plus fort qu'à un dérivé. Ce qui se verse est
ce que personne ne sait refaire — les fiches de qualification et le texte des
amendements.

**Corollaire d'appareil : l'extracteur est déterministe et son empreinte est
relevée.** Même pièce, même script, même JSON, même SHA-256. Sans cela, rien ne
garantit que la fiche de l'article 12 parle du même article 12 la semaine
suivante.

---

## Rattachement et vecteur : deux questions, jamais la même

C'est la correction la plus importante de la journée.

**Le rattachement** dit *si la mesure peut voyager en loi de finances*. C'est une
question de domaine, et elle se plaide.

**Le vecteur** dit *quel article de quel texte on modifie*. C'est une question de
légistique, et elle ne se plaide pas : elle se trouve, ou elle n'existe pas.

Une mesure peut être parfaitement rattachable et n'avoir aucun vecteur identifié :
elle n'est alors pas rédigeable. L'inverse existe aussi. `REF_norme` porte donc
**deux colonnes distinctes**, et un contrôle qui refuse de confondre l'une avec
l'autre.

**Le vecteur est le gros du travail, et il faut le dire maintenant.** La
suppression est facile : on abroge un article nommé. L'insertion ne l'est pas —
l'expérience de la Constitution et de la LOLF l'a montré, où trouver le bon
alinéa n'a jamais été direct. Sur la matière fiscale, **l'auteur dispose d'une
révision du code général des impôts préparée par un expert** : c'est un input à
verser, et il couvre peut-être une grande part des vecteurs fiscaux. À instruire
avant de refaire ce travail.

---

## Comment on plaide le rattachement

**Par l'implicite budgétaire, pas par la porte.** La méthode retenue est
d'identifier ce que la mesure produit comme dépense ou comme recette — souvent
ignoré, et à tort — puis d'interroger les contrefactuels pour établir qu'elle est
**de nature budgétaire bien que son objet soit plus large**. C'est un plaidoyer,
il n'est pas garanti, et **la perte de quelques articles n'est pas grave**. Elle
est le prix de la position.

Le contrefactuel n'est pas décoratif : la recevabilité s'apprécie contre le droit
existant, et le choix de la référence — droit constant ou évolution tendancielle —
n'est pas codifié. C'est une prise, dans les deux sens. *À instruire, à ne pas
tenir pour établi.*

**La grille des portes du domaine reste, mais au second rang.** Elle sert à savoir
ce qui est acquis sans plaidoirie, pas à décider ce qu'on tente.

**Une correction expresse de l'auteur, à retenir** : « information et contrôle du
Parlement sur la gestion des finances publiques » n'est pas la bonne porte qu'elle
paraît. C'est celle par laquelle on demande des rapports, faute d'avoir réfléchi à
ce qu'on veut faire ou d'en avoir les moyens. Elle n'a d'intérêt que pour un axe
précis : **la transparence absolue** — opérateurs, associations, caisses de
sécurité sociale. *Que cet axe soit bien au corpus reste à vérifier sur le
`REF_doctrine`, qu'un fil de conversation ne peut pas ouvrir.*

**Priorité de rédaction : ce que le PLF ouvre déjà.** Le Gouvernement n'est pas
original, et il rouvre souvent les mêmes articles. Amender un article ouvert coûte
infiniment moins qu'un article additionnel — en recevabilité, en vecteur, en
débat. L'ordre de traitement des écarts suit donc : **partielle et contraire sur
un article ouvert, avant absente**.

---

## Lire un texte budgétaire : ce qui ne se délègue pas au flair

Les mesures d'économie, de hausse d'impôt et de hausse de dépense sont souvent, à
dessein, cachées ou mal présentées. L'exposé des motifs ne les décrit pas : il les
raconte. **Il vaut comme indice, jamais comme description.**

La lecture en creux — qu'attendrait-on qui ne figure pas ? que tel terme plutôt
qu'un autre permet-il ou exclut-il ? — est la clé, et c'est un jugement. **Un
jugement ne se délègue pas au flair d'un modèle**, au même titre qu'une
restauration. Il se mécanise, par des dispositifs qui produisent des signaux
qu'ensuite on lit.

**Le trois colonnes, et il existe déjà.** On ne lit jamais une disposition
modificative seule : on lit texte en vigueur, disposition, texte résultant. Le
corpus porte déjà `Constitution_3col` et `LOLF_3col` — la méthode est éprouvée,
elle se transpose. C'est le dispositif qui rend la mécanique visible là où l'EDM
raconte une histoire.

**Le chiffre d'abord, et pas celui de l'EDM.** Le montant de l'article se prend à
l'état, à l'annexe ou au tableau d'équilibre. Tout écart avec le montant annoncé à
l'exposé des motifs est un signal, et il se relève, il ne s'arbitre pas.

**Le relevé mécanique des mots de portée** : peut, dans la limite de, à compter
de, au titre de, par dérogation, notamment. Chacun ouvre ou ferme quelque chose,
et leur liste par article se produit par script.

**Le relevé des dates.** Entrée en vigueur, clause de fin, période transitoire. Un
décalage d'un an déplace un coût hors de l'année budgétaire sans rien changer au
fond : c'est le procédé le plus commun et le plus efficace.

**Le relevé des absences attendues** — un taux modifié sans que l'assiette bouge,
un plafond posé sans indexation, une suppression sans transitoire, un dispositif
sans évaluation. La liste des absences à chercher s'écrit une fois et s'applique à
tous les articles.

**Et les amendements déposés.** Des centaines de gens ont déjà lu ce texte en
creux, chacun sur son sujet, et ils ont écrit ce qu'ils y ont vu. Un article qui
attire trente amendements porte un point sensible ; l'article qui n'en attire
aucun mérite qu'on se demande pourquoi. C'est le meilleur correcteur disponible,
et il est gratuit.

**Le produit** : une fiche courte et claire par mesure principale — le vrai
chiffre, la mécanique de la disposition, ce que l'EDM en dit et ce qu'il n'en dit
pas. À industrialiser pour l'analyse du PLF 2027.

---

## Les fils, dans l'ordre de leurs dépendances

### Fil 1 — Portes, vecteurs et véhicules

**Ne demande rien à l'auteur.** Ni PDF, ni décision.

Déplie : l'archive technique, `reference/LOLF_reference`, `reference/LOLF_3col`,
`referentiels/economies.json`, et le `REF_doctrine`.

Rend quatre choses.

**La grille des portes**, relevée en verbatim sur `LOLF_reference` — jamais de
mémoire. La grille du PLFSS se relève de même, mais **pas sur `LO 111-3`** :
depuis la loi organique n° 2022-354 du 14 mars 2022, cet article ne définit plus
que les trois espèces de lois de financement. La porte d'un amendement est aux
articles **`LO 111-3-6` à `LO 111-3-8`** du code de la sécurité sociale, et les
monopoles aux `-3-14` à `-3-16`. Le relevé des dix-huit est au coffre,
`sources/domaine_lfss_LO111-3.md` (A-297).

**Le test de rattachement par l'implicite budgétaire** — comment on identifie
l'effet budgétaire d'une mesure dont l'objet est plus large, et quels
contrefactuels on interroge.

**La vérification de l'axe transparence** au `REF_doctrine` : existe-t-il, que
couvre-t-il exactement, et jusqu'où porte-t-il sur les opérateurs, les
associations et les caisses.

**La ventilation par véhicule** des 41 lignes d'économie tracées. Elle ne commande
plus le calendrier — l'auteur a tranché l'ordre — mais elle dit combien de matière
attendra la phase PLFSS.

*C'est le fil à ouvrir en premier.*

### Fil 2 — Socle du texte, PLF d'abord

**Demande à l'auteur** : le PDF du PLF, joint au fil. Le PLFSS attend son tour.

Rend `referentiels/socle_plf_texte.json` : une entrée par article, portant son
numéro, sa partie, son titre, **sa rédaction exacte**, sa page dans la pièce
source, et **l'exposé des motifs qui s'y rapporte**. L'EDM est indexé avec
l'article et jamais confondu avec lui : il est de l'indice, pas de la norme.

Plus l'extracteur et son empreinte.

### Fil 3 — Pack public v1

**Demande le fil 1 fait, et trois articles réels du fil 2** pour éprouver les
grilles. Aucune méthode ne part sans avoir tourné une fois.

Rend un zip : grille de recevabilité, grille des portes, test de rattachement,
grille de qualification d'un article, dispositif de lecture en creux, grille des
cinq écarts, gabarit d'exposé sommaire, lecteur des trois annexes budgétaires
publiées. Plus une liste d'adresses de téléchargement — la base documentaire est
optionnelle et elle n'est pas dans le zip.

**Ce qui n'y entre jamais** : le manuscrit, le `REF_doctrine`, les positions, les
apports, le registre, la stratégie réseaux, les deux classeurs de l'auteur, la
révision du CGI, et **la colonne « traitement » des 128 programmes** — un
référentiel qui range les programmes en régalien, transférable et supprimable est
la doctrine sous forme de tableau. Le pack exporte les questions, pas nos réponses
(A-134).

Un temps 2 est réservé — un objet « PLF relu, trié, expliqué » — dont l'arbitrage
se posera quand il existera.

### Fil 4 — `REF_norme`

**Ne demande rien et ne dépend d'aucun texte.** Peut tourner en parallèle du fil 1.

Une entrée par proposition : la norme cible — ce que le droit doit concrètement
imposer, supprimer, modifier ou autoriser —, le niveau requis, **le véhicule**,
**le vecteur** (article de code ou de loi modifié, distinct du véhicule), et l'état
du vecteur : trouvé, à trouver, ou inexistant.

Le format est déjà éprouvé : `archive/Recap_transposabilite` a fait ce travail pour
la Constitution, innovations ventilées par strate et replis portant chacun son
écart. Il se généralise.

**Premier acte du fil** : instruire la révision du CGI préparée par l'expert, et
mesurer ce qu'elle couvre déjà en vecteurs fiscaux. On ne refait pas ce qui existe.

Long. Se découpe en lots, comme les apports.

### Fils suivants — qualification, appariement, écart, rédaction

Qualification des articles par lots bornés, chacun passant par le trois colonnes
et les relevés mécaniques. Appariement **par jointure sur identifiants** — numéro
de programme, de mission, d'article de code, de dépense fiscale, de taxe
affectée — jamais par appréciation ; résidu non apparié déclaré. Écart sur cinq
valeurs : conforme, partielle, neutre, contraire, absente.

**Ordre de traitement** : partielle et contraire sur article ouvert d'abord ;
absente ensuite. Un écart « absente » n'est pas une case de la matrice, c'est un
**article additionnel**, et il coûte le plus cher.

Puis rédaction.

---

## Les règles dures

**Le gage et le financement sont deux colonnes.** Le gage de recevabilité est un
prétexte : approximatif, réutilisable, il ne s'additionne pas. Le financement vient
du chiffrage, il boucle sur `economies.json`, **il ne se compte jamais deux fois**.
Si les deux se confondent, l'addition du contre-PLF ne tombe pas — et c'est
l'attaque la plus facile sur le seul terrain où le corpus est imprenable, avec 32
bouclages sur 32.

**L'article 40 se réduit à une question** : la mesure augmente-t-elle une charge ?
Une charge n'est jamais gageable ; une recette l'est toujours. Le verrou n'est pas
l'article 40, c'est le domaine — et le domaine se plaide.

**La contorsion se dit.** Les deux gages naturels — baisse de dépense, baisse de
recette sociale — sont exactement les deux que le cadre interdit au même texte.
Chaque amendement qui a dû recycler un gage postiche porte, en deux phrases de
l'exposé sommaire, la raison pour laquelle il l'a fait. Trente amendements, trente
occurrences : le contre-PLF plaide la fusion PLF-PLFSS sans jamais avoir à la
réclamer frontalement.

**Rien ne traverse vers le projet ouvert avant dépôt ou publication** (A-134). La
méthode fait exception : elle part maintenant.

---

## Ce qui reste à l'auteur

Combien d'amendements, sur quels articles, dans quel ordre de dépôt, et lesquels
tombent si un autre est adopté. Le registre de l'amendement, quand le document GL
et le corpus divergent. Le calendrier du PLF et du PLFSS suivants, qui n'est pas au
corpus et ne se suppose pas. Le versement de la révision du CGI.

Et une chose neuve : si le pack public fonctionne, des tiers déposeront des
amendements qui recoupent les nôtres. Qui dépose quoi en premier, et si deux
amendements voisins divisent un vote, cela ne se déduit d'aucune donnée.

---

## À porter au registre par le premier fil de production

Ces décisions sont prises. Elles ne sont pas encore au registre : un fil de
conversation ne déplie rien, et `methode/arbitrages.md` ne se réécrit pas à travers
un modèle sans risque de déformation. Le premier fil de production les ajoute par
script, au dépôt.

1. **Le PLFSS entre au périmètre**, à parité d'appareil avec le PLF, mais **le PLF
   est prioritaire**. Arbitré par l'auteur ; l'ordre ne se rediscute pas.
2. **Le gage de recevabilité et le financement réel sont deux objets distincts.**
   Le gage se recycle ; le financement ne se compte qu'une fois. Arbitré par
   l'auteur, en réponse à une réserve de Claude.
3. **Le rattachement se plaide par l'implicite budgétaire et le contrefactuel**,
   non par une porte du domaine. La grille des portes passe au second rang. Des
   pertes sont acceptées d'avance. Arbitré par l'auteur.
4. **« Information et contrôle du Parlement » est écartée comme porte générale** :
   c'est la porte des demandes de rapport. Elle ne sert que l'axe de transparence
   absolue. Arbitré par l'auteur ; l'existence de cet axe reste à vérifier au
   `REF_doctrine`.
5. **Le rattachement et le vecteur sont deux questions distinctes**, et `REF_norme`
   porte deux colonnes. Le vecteur est le gros du travail. Arbitré par l'auteur.
6. **On prioritise ce que le PLF ouvre déjà.** Article ouvert avant article
   additionnel. Arbitré par l'auteur.
7. **Le socle du texte porte la rédaction exacte, les numéros et l'exposé des
   motifs rattaché à chaque article.** L'EDM est indexé et jamais confondu avec la
   norme : indice, pas description. Arbitré par l'auteur.
8. **La lecture en creux se mécanise, elle ne se délègue pas au flair.** Trois
   colonnes, chiffre pris à l'état et non à l'EDM, relevé des mots de portée, des
   dates, des absences attendues, et des amendements déposés. Même rang que « une
   restauration est toujours une copie d'octets ».
9. **Le normage juridique devient une couche du corpus** (`REF_norme`), systématique
   sur les 56 propositions, indépendante du véhicule. Arbitré par l'auteur.
10. **Le pack public part en deux temps** : la méthode d'abord, sans attendre aucun
    dépôt ; l'objet « PLF relu, trié, expliqué » ensuite, s'il existe. Arbitré par
    l'auteur.
11. **Le dry run sur le PLF 2026 reste interne**, mais le pack public part dès
    maintenant. Arbitré par l'auteur.
12. **Le verbatim n'entre que par pièce jointe.** L'outil de récupération web passe
    par un modèle : il repère, il ne copie pas.
13. **Ni le PLF ni le PLFSS ne vont au coffre.** Documents publics, retéléchargeables
    à l'identique. Ce qui se verse est la qualification et les amendements.

---

*20260831 — fil de conversation. Il n'a produit aucun fond.*
