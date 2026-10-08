# Procédure contre-PLF — la carte des fils

Écrite le 20260831, fil de conversation, corrigée le même jour par l'auteur. Elle
ne produit aucun fond : elle dit par où on entre, dans quel ordre, ce que chaque
fil demande, ce qu'il rend, et ce qui garantit que rien ne se déforme en route.

Elle se lit avec `methode/carte_des_chantiers.md`, qui dit ce que le chantier
couvre, et avec la skill `resolution-chantier`, qui dit comment on travaille.

**Mise à jour du 20261001 — l'état d'avancement du fil 1 est corrigé.** Ce
document décrivait sa grille des portes comme à rendre ; **elle a été rendue le
20260902** (A-336). La correction est signalée *[fait 20260902]* au fil 1. Le
renvoi au relevé pointait `sources/` : la pièce vit à `reference/`.

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
pièces jointes de conversation ne comptent pas dans la jauge du coffre.

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
l'expérience de la Constitution et de la LOLF l'a montré. Sur la matière fiscale,
**l'auteur dispose d'une révision du code général des impôts préparée par un
expert** : c'est un input à verser. *[fait 20260929 — `referentiels/cgi_expert_*.tsv`
et `reference/cgi_expert_regles_de_lecture.md` sont au coffre.]*

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
ce qui est acquis sans plaidoirie, pas à décider ce qu'on tente. ***C'est cette
règle, et non l'absence de grille, qui plafonne les verdicts de loi de financement
à `plaidable`.*** *[précisé 20261001 : trois documents et deux fils ont attribué ce
plafond à une grille manquante, alors qu'elle est relevée depuis le 20260902.]*

**Une correction expresse de l'auteur, à retenir** : « information et contrôle du
Parlement sur la gestion des finances publiques » n'est pas la bonne porte qu'elle
paraît. C'est celle par laquelle on demande des rapports, faute d'avoir réfléchi à
ce qu'on veut faire. Elle n'a d'intérêt que pour un axe précis : **la transparence
absolue** — opérateurs, associations, caisses de sécurité sociale. *[fait
20260902 — l'axe existe et la grille Sécu lui donne **trois entrées**, une par
partie, contre deux au PLF.]*

**Priorité de rédaction : ce que le texte ouvre déjà.** Le Gouvernement n'est pas
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
jugement ne se délègue pas au flair d'un modèle.** Il se mécanise, par des
dispositifs qui produisent des signaux qu'ensuite on lit.

**Le trois colonnes, et il existe déjà.** On ne lit jamais une disposition
modificative seule : on lit texte en vigueur, disposition, texte résultant. Le
corpus porte déjà `Constitution_3col` et `LOLF_3col`.

**Le chiffre d'abord, et pas celui de l'EDM.** Le montant de l'article se prend à
l'état, à l'annexe ou au tableau d'équilibre. Tout écart avec le montant annoncé à
l'exposé des motifs est un signal, et il se relève, il ne s'arbitre pas.

**Le relevé mécanique des mots de portée** : peut, dans la limite de, à compter
de, au titre de, par dérogation, notamment.

**Le relevé des dates.** Entrée en vigueur, clause de fin, période transitoire. Un
décalage d'un an déplace un coût hors de l'année budgétaire sans rien changer au
fond : c'est le procédé le plus commun et le plus efficace.

**Le relevé des absences attendues** — un taux modifié sans que l'assiette bouge,
un plafond posé sans indexation, une suppression sans transitoire, un dispositif
sans évaluation.

**Le balayage des dispositions discrètes.** *[inscrit 20261001.]* Chercher sur
tous les articles `par dérogation`, `nonobstant`, `sans préjudice`, `sont
validées`, `est abrogé`, `ratifi`, `pénalité`, `sanction`, `ordonnance`, et lire
chaque occurrence. **Le relevé des mots de portée trouve ce qui est flou ; celui-ci
trouve ce qui est caché.** *Rendement mesuré au PLFSS 2027 : six dispositions
qu'aucun autre relevé n'avait vues, dont une dérogation expresse au secret médical
sous un article intitulé « renforcer la coordination ».*

**Et les amendements déposés.** Des centaines de gens ont déjà lu ce texte en
creux, chacun sur son sujet, et ils ont écrit ce qu'ils y ont vu. Un article qui
attire trente amendements porte un point sensible ; l'article qui n'en attire
aucun mérite qu'on se demande pourquoi. C'est le meilleur correcteur disponible,
et il est gratuit. *Non ouvert à ce jour, ni pour 2026 ni pour 2027.*

**Le produit** : les **quatre pièces de lecture** d'un véhicule — index des
mesures, fiches de mesure principale, liste par article et son PDF, note lisible.
*[corrigé 20261001 : ce document n'en nommait qu'une.]* Leur gabarit est à
`methode/prompt_fil_lecture_textes_2027.md` et, pour la liste et son rendu, à
`reference/gabarit_liste_articles.md`, qui fait foi.

---

## Les fils, dans l'ordre de leurs dépendances

### Fil 1 — Portes, vecteurs et véhicules — **rendu le 20260902**

**Ne demande rien à l'auteur.** Ni PDF, ni décision.

Déplie : l'archive technique, `reference/LOLF_reference`, `reference/LOLF_3col`,
`referentiels/economies.json`, et le `REF_doctrine`.

Rend quatre choses.

**La grille des portes**, relevée en verbatim — jamais de mémoire. La grille du
PLFSS se relève de même, mais **pas sur `LO 111-3`** : depuis la loi organique
n° 2022-354 du 14 mars 2022, cet article ne définit plus que les trois espèces de
lois de financement. La porte d'un amendement est aux articles **`LO 111-3-6` à
`LO 111-3-8`** du code de la sécurité sociale, et les monopoles aux `-3-14` à
`-3-16`.

***[fait 20260902, A-336.]*** **31 portes, 0 échec**, relevées en verbatim au dépôt
de droit, millésime LEGI 20260901, chaque porte avec son identifiant `LEGIARTI` et
sa date de version. Répartition : 15 facultatives, 9 obligatoires, 4 monopoles,
1 définition, 1 structure, 1 reprise. Portées par
`appareil/portes_domaine_lfss.py` ; le relevé documenté est à
**`reference/domaine_lfss_LO111-3.md`** *(et non `sources/`, chemin corrigé le
20261001)*.

> **Trois choses à savoir avant de s'en servir.**
> **a.** Deux manques sont déclarés et non comblés : `LO 111-4` et `LO 111-4-1`,
> les annexes obligatoires — **siège de toute obligation documentaire nouvelle au
> PLFSS** — ne sont pas relevés, le choix entre une annexe opposable et un rapport
> appartenant à l'auteur.
> **b.** **Le croisement avec la grille LOLF n'est pas fait** : trois portes Sécu
> renvoient au III de l'article 2 de la LOLF, et une mesure d'affectation entre
> l'État et la sécurité sociale se qualifie sur **deux** grilles à la fois.
> **c.** Un extrait du dépôt de droit de plus de 45 jours se déclare périmé :
> celui-ci se périme le **17 octobre 2026**, et se rafraîchit alors par
> `droit.py`.

**Le test de rattachement par l'implicite budgétaire.** *[fait — voir
`methode/test_rattachement.md`, cinq temps et quatre verdicts.]*

**La vérification de l'axe transparence** au `REF_doctrine`. *[fait 20260902 :
l'axe existe, et il a trois entrées au PLFSS contre deux au PLF.]*

**La ventilation par véhicule** des 41 lignes d'économie tracées. *Elle ne commande
plus le calendrier — l'auteur a tranché l'ordre par la règle de l'entonnoir, et la
dimension véhicule vit désormais à `methode/plan_sept_phases_20260930.md`.*

### Fil 2 — Socle du texte

**Demande à l'auteur** : le PDF du véhicule, joint au fil.

Rend `referentiels/socle_<véhicule>_texte.json` : une entrée par article, portant
son numéro, sa partie, son titre, **sa rédaction exacte**, sa page dans la pièce
source — **au folio imprimé, jamais au renvoi du sommaire** —, et **l'exposé des
motifs qui s'y rapporte**. L'EDM est indexé avec l'article et jamais confondu avec
lui : il est de l'indice, pas de la norme.

Plus l'extracteur et son empreinte.

***État au 20261001 : fait côté PLF, non fait côté PLFSS 2027.*** Les quatre pièces
de lecture du PLFSS 2027 sont versées, mais **ce sont des pièces de lecture, pas le
socle** : la qualification et l'appariement se jouent sur le socle, pas sur elles.

### Fil 3 — Pack public v1

**Demande le fil 1 fait, et trois articles réels du fil 2** pour éprouver les
grilles.

Rend un zip : grille de recevabilité, grille des portes, test de rattachement,
grille de qualification d'un article, dispositif de lecture en creux, grille des
cinq écarts, gabarit d'exposé sommaire, lecteur des trois annexes budgétaires
publiées. Plus une liste d'adresses de téléchargement.

**Ce qui n'y entre jamais** : le manuscrit, le `REF_doctrine`, les positions, les
apports, le registre, la stratégie réseaux, les deux classeurs de l'auteur, la
révision du CGI, et **la colonne « traitement » des 128 programmes**. Le pack
exporte les questions, pas nos réponses (A-134).

### Fil 4 — `REF_norme`

**Ne demande rien et ne dépend d'aucun texte.**

Une entrée par proposition : la norme cible, le niveau requis, **le véhicule**,
**le vecteur** (article de code ou de loi modifié, distinct du véhicule), et l'état
du vecteur : trouvé, à trouver, ou inexistant.

**Premier acte du fil** : instruire la révision du CGI préparée par l'expert.
*[fait 20260929.]* **Rien n'est porté côté PLFSS.**

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

**L'article 40 se réduit à une question** : la mesure augmente-t-elle une charge ?
Une charge n'est jamais gageable ; une recette l'est toujours. Le verrou n'est pas
l'article 40, c'est le domaine — et le domaine se plaide.

**La contorsion se dit.** Les deux gages naturels — baisse de dépense, baisse de
recette sociale — sont exactement les deux que le cadre interdit au même texte.
Chaque amendement qui a dû recycler un gage postiche porte, en deux phrases de
l'exposé sommaire, la raison pour laquelle il l'a fait.

**Rien ne traverse vers le projet ouvert avant dépôt ou publication** (A-134). La
méthode fait exception : elle part maintenant.

**Une borne écrite à un document de méthode ne se recopie pas : elle se vérifie au
registre avant d'être redite.** *[inscrit 20261001 — un plafond de verdict motivé
par une grille manquante a survécu un mois à la production de cette grille, et
trois fils l'ont recopié.]*

---

## Ce qui reste à l'auteur

Combien d'amendements, sur quels articles, dans quel ordre de dépôt, et lesquels
tombent si un autre est adopté. Le registre de l'amendement, quand le document GL
et le corpus divergent. Le calendrier du PLF et du PLFSS suivants. Le versement de
la révision du CGI *[fait]*.

Et une chose neuve : si le pack public fonctionne, des tiers déposeront des
amendements qui recoupent les nôtres. Qui dépose quoi en premier, et si deux
amendements voisins divisent un vote, cela ne se déduit d'aucune donnée.

---

## À porter au registre par le premier fil de production

1. **Le PLFSS entre au périmètre**, à parité d'appareil avec le PLF, mais **le PLF
   est prioritaire**.
2. **Le gage de recevabilité et le financement réel sont deux objets distincts.**
3. **Le rattachement se plaide par l'implicite budgétaire et le contrefactuel**,
   non par une porte du domaine. La grille des portes passe au second rang. Des
   pertes sont acceptées d'avance.
4. **« Information et contrôle du Parlement » est écartée comme porte générale.**
5. **Le rattachement et le vecteur sont deux questions distinctes.**
6. **On prioritise ce que le texte ouvre déjà.**
7. **Le socle du texte porte la rédaction exacte, les numéros et l'exposé des
   motifs rattaché à chaque article.**
8. **La lecture en creux se mécanise, elle ne se délègue pas au flair.**
9. **Le normage juridique devient une couche du corpus** (`REF_norme`).
10. **Le pack public part en deux temps.**
11. **Le dry run sur le PLF 2026 reste interne.**
12. **Le verbatim n'entre que par pièce jointe.**
13. **Ni le PLF ni le PLFSS ne vont au coffre.**

---

*20260831 — fil de conversation. Il n'a produit aucun fond.
Mise à jour d'état le 20261001 : fils 1 et 4 avancés, chemin du relevé des portes
corrigé, balayage des dispositions discrètes ajouté, quatre pièces de lecture
substituées à la seule fiche.*
