# Conduite de la chaîne — de l'énoncé à l'amendement déposable

*Cette pièce s'adresse à qui conduit la chaîne pour le compte d'un déposant.
Elle ne décrit aucune étape en détail : chaque étape a sa procédure, nommée à sa
place. Elle dit ce qui les enchaîne, ce qui passe de l'une à l'autre, et à quel
moment on parle au déposant.*

Les douze autres pièces sont une boîte à outils. Celle-ci en fait une machine :
elle tient l'ordre, elle tient l'objet de passage, et elle dit où s'arrêter.

---

## 1. La boucle, en une page

**Ce que le déposant donne.** Une phrase en langage naturel — « supprimer le
taux réduit sur tel service », « fermer tel organisme », « plafonner telle taxe
affectée ». Et, s'il le sait, le véhicule : projet de loi de finances, projet de
loi de financement de la sécurité sociale, proposition de loi.

**Ce qu'il récupère.** Un amendement déposable : un en-tête à quatre éléments,
un dispositif rédigé, un gage quand il en faut un, un exposé sommaire de 200 à
300 mots sourcé, et la liste des renvois entrants en fin d'exposé. Puis, quand
plusieurs amendements sont prêts, une liasse rendue en `.docx`.

**Ce qu'il ne fait jamais.** Nommer une étape, recopier un résultat d'une étape
à la suivante, choisir entre deux procédures. La décomposition en huit étapes
est votre affaire, pas la sienne.

**Les cinq moments où on lui parle, et il n'y en a pas d'autres.**

| moment | ce qu'on lui demande | ce qui se passe s'il ne répond pas |
|---|---|---|
| **l'entrée** | le véhicule, s'il n'est pas dans l'énoncé | la chaîne porte `a_determiner` et E0 le qualifie ; elle ne s'arrête pas |
| **le verdict de rattachement `fragile`** | dépose-t-on en sachant que l'amendement peut tomber ? | la chaîne continue, le dossier porte la réserve, et elle ressort au rendu |
| **la consigne de gage** | une consigne propre à ce dossier — « sans gage », « gager sur telle ligne » ? | la chaîne applique l'ordre de recherche de `procedures/gage.md` |
| **le principe de l'en-tête** | la ligne qui relie l'amendement à ce qu'il défend | la chaîne laisse le champ vide et le signale au rendu |
| **l'ordre de la liasse** | l'ordre de dépôt et les neutralisations réciproques | la liasse sort dans l'ordre de production, déclaré comme non arbitré |

**Ces cinq moments sont des arrêts à sa main, jamais bloquants.** Une chaîne
qui attend une réponse à chaque étape fait porter au déposant le travail de
conduite qu'elle est censée lui épargner. La règle est donc : **on déroule, on
inscrit au dossier ce qui reste à trancher, et on le rend en un bloc à la
fin.** Il reprend la main quand il veut, pas quand la chaîne le lui impose.

**Le seul arrêt réel est `hors_capacite`.** Une étape qui ne sait pas conclure
l'écrit, et la chaîne s'arrête là — elle ne devine pas, elle ne contourne pas,
elle ne rend pas une réponse approchante. *Un résultat vraisemblable est plus
dangereux qu'un résultat absent.*

---

## 2. Le dossier de mesure, rendu concret

`procedures/contrat_chaine_amendement.md` décrit l'objet. Voici sa forme exacte,
prête à être tenue.

**Un objet par mesure, un bloc par étape, rien ne s'efface jamais.** Une étape
ajoute son bloc à la suite ; elle ne réécrit pas un bloc antérieur. Si elle
estime qu'un bloc antérieur est faux, elle l'écrit dans ses `doutes` et laisse
l'autre bloc intact.

### L'en-tête du dossier

```
mesure        un identifiant local, sans signification
enonce        la phrase du déposant, verbatim
vehicule      plf · plfss · ppl · pplo · pplc · a_determiner
```

Le véhicule est **une donnée du dossier**. Aucune étape ne le suppose à partir
de ce qu'elle voit ; elle le lit ici. Une étape qui traite un véhicule inconnu
comme s'il était une loi de finances est en faute, même quand elle tombe juste.

### Le bloc d'étape

```
etape           le nom de l'étape
recu            la liste EXACTE des blocs lus, et rien d'autre
doutes          un doute par ligne, avec ce qui le lèverait ; « aucun » si rien
gisements       les rôles de matériel effectivement remplis, par leur rôle
degradation     complet · partiel · a_blanc
hors_capacite   vide, ou la raison pour laquelle l'étape ne sait pas traiter
<champs propres à l'étape>
```

**`recu` et `doutes` ne se laissent jamais vides.** C'est l'invariant : chaque
étape déclare ce qu'elle a reçu et si elle en a douté. Une étape qui lit un bloc
hors de sa déclaration est en faute — c'est ce qui rend la séparation réelle et
permet de rejouer une étape seule.

**`gisements` nomme un rôle, jamais un fichier.** « Une source de niches »,
« les annexes du texte déposé », « un réservoir d'arguments sourcés ». C'est le
dossier qui dit quel fichier tient le rôle. Une étape qui nomme un fichier au
lieu de son rôle est en faute.

**`degradation` dit à quel équipement l'étape a travaillé.** Une étape doit
tourner à blanc et le déclarer : le matériel n'est pas une dépendance, c'est une
commodité. Un résultat `a_blanc` non déclaré sort au contrôle de sortie.

### Un dossier à trois étapes remplies

```
mesure     tva-279
enonce     « supprimer le taux réduit de TVA de l'article 279 du CGI »
vehicule   plf

E0 qualification
  recu            en-tête
  doutes          aucun
  gisements       le contexte fourni par le déposant
  degradation     a_blanc
  hors_capacite   —
  statut          dépense fiscale
  levier          la recette de l'État, par le taux
  vehicule_qualifie  plf

E1 rattachement
  recu            en-tête, E0
  doutes          le montant du canal « dépense fiscale » n'est pas relevé :
                  il se prend à l'annexe des voies et moyens, tome II, et
                  l'annexe de l'exercice visé n'est pas parue
  gisements       la recherche publique
  degradation     partiel
  hors_capacite   —
  verdict         plaidable
  partie          première
  canaux          dépense directe : rien · recette de l'État : effet par le
                  taux, montant non relevé · dépense fiscale : montant non
                  relevé · effet sur un tiers : rien
  qualification   substantielle — retirer l'effet de recette retire la mesure
  contrefactuel   droit constant
  porte           aucune relevée
  precedent       non cherché

E2 vecteur
  recu            en-tête, E0, E1
  doutes          aucun
  gisements       la recherche publique
  degradation     partiel
  hors_capacite   —
  adresses        code général des impôts · article 279 · article entier
                    rôle : montant du taux
                    provenance : document_fourni
                    identifiant et date de relevé : à porter avant rédaction
  etat            trouve
```

**Lu seul, ce dossier dit tout ce qu'il faut pour reprendre la chaîne à E3** :
ce qui est acquis, ce qui est en suspens, et avec quel équipement chaque réponse
a été obtenue. C'est l'objet qui tient la chaîne. Sans lui, chaque étape repart
de zéro et le déposant redevient le seul fil conducteur.

---

## 3. L'enchaînement, étape par étape

Pour chacune : ce qu'elle lit, ce qu'elle écrit, et **à quelle condition on
passe à la suivante**.

### E0 — Qualification

| | |
|---|---|
| lit | l'en-tête |
| écrit | le statut, le levier, le véhicule qualifié |
| on passe si | le statut est posé |

Le statut décide de la famille de siège et se qualifie avant toute recherche :
crédits d'État, dépense fiscale, dépense sociale, dépense locale, dépense
d'opérateur, mesure de pure norme. Sur la dépense locale, le levier est triple —
recette, dotation, norme — et se cherche en entier : l'étape rend les trois
adresses quand elles existent et ne choisit pas.

**Si l'énoncé mêle deux mesures**, l'étape le dit dans `doutes` et scinde le
dossier en deux. Si le statut n'est pas déterminable sur l'énoncé seul, elle
remplit `hors_capacite` et la chaîne s'arrête : une qualification devinée
envoie toute la suite au mauvais endroit.

### E1 — Rattachement

| | |
|---|---|
| lit | E0 |
| écrit | le verdict, la partie, les quatre canaux, la qualification, le contrefactuel |
| on passe si | le verdict est `acquis`, `plaidable`, `fragile` ou `sans_objet` |

Procédure entière à `procedures/test_rattachement.md`. Les quatre canaux se
parcourent **tous**, et « rien » s'écrit. Un canal sans montant documenté se
déclare sans montant — on ne comble pas un trou par un ordre de grandeur
vraisemblable.

Sur `non rattachable`, la chaîne s'arrête : la mesure part dans un autre
véhicule, et cela ne dit rien de sa valeur. Sur `fragile`, elle continue et
porte la réserve jusqu'au rendu. Sur une proposition de loi, le test est sans
objet et l'étape écrit `sans_objet`, jamais un verdict vide.

### E2 — Vecteur

| | |
|---|---|
| lit | E0, E1 |
| écrit | une ou plusieurs adresses décomposées — code · siège · article · subdivision —, chacune avec son rôle, sa provenance, son identifiant et sa date de relevé |
| on passe si | l'état est `trouve` ou `siege_non_codifie` |

Procédure entière à `procedures/procedure_vecteurs.md`. **Le vecteur et le
véhicule ne se confondent jamais** : le vecteur dit quel article on modifie, le
véhicule dans quel texte on dépose. L'adresse se décompose du macro au micro et
rien ne se recolle.

Sur `a_trouver`, la chaîne s'arrête : une mesure rattachable et sans vecteur
n'est pas rédigeable, et c'est une information qu'on veut avant d'écrire. Sur
`siege_non_codifie`, elle continue — la mesure est rédigeable, elle n'a pas
d'article à modifier.

Un vecteur de plus d'un an se rejoue avant rédaction ; un vecteur qui sert à un
amendement déposé se rejoue la semaine du dépôt.

### E3 — Droit applicable

| | |
|---|---|
| lit | E2 |
| écrit | le texte en vigueur de chaque adresse, avec identifiant et date de version ; les renvois entrants avec leur certitude ; l'avertissement d'abrogation programmée |
| on passe si | chaque adresse porte son texte, ou est déclarée non couverte |

Outillée par le dépôt de droit — `procedures/depot_droit.md`. **L'applicabilité
se lit aux dates, jamais à l'état** : un article peut s'appliquer aujourd'hui et
porter une abrogation déjà votée.

Deux arrêts propres à cette étape. **L'extrait périmé** : au-delà de 45 jours, la
mention `À REJOUER` s'imprime, et l'extrait ne sert pas à rédiger — on le
rafraîchit d'abord, par `appareil/installer_droit.py`, qui le fait de lui-même,
nomme son repli quand la source ne répond pas, et s'arrête bruyamment plutôt que
de laisser passer un extrait arrêté en amont sous le millésime du jour. **Le droit non codifié** : un siège logé dans une loi de
finances antérieure n'est pas dans l'extrait, et l'étape le déclare plutôt que de
rendre l'adresse la plus proche.

**Les renvois entrants ne sont pas outillés.** Le module que ce paquet a
longtemps nommé — `coordination.py` — n'existe pas au dépôt ; mesuré le
3 octobre 2026. La règle de fond ne change pas, la main qui l'exécute change :
sur un amendement, **service minimum** — on ne coordonne pas, on signale, et la
liste va en fin d'exposé sommaire ; sur une proposition de loi, chaque renvoi se
traite ou se déclare sans objet avant dépôt. Les deux se conduisent à la main,
par recherche de la référence dans les extraits des codes portés, et **le relevé
se déclare incomplet** plutôt que présenté comme exhaustif. Une liste vide
s'écrit « non relevé », jamais « aucun ».

### E4 — Rédaction cible

| | |
|---|---|
| lit | E0, E2, E3 |
| écrit | pour chaque adresse, trois colonnes — **A** le texte en vigueur, **B** la réforme visée, **C** le texte révisé — et, dérivée de A → C, la forme modificative |
| on passe si | la forme modificative, réappliquée à A, redonne C à l'octet |

**Le cœur de l'étape est le signe « = ».** A plus B égale C. L'étape produit le
texte de l'article tel qu'il sera, pas la phrase qui l'y amène ; la forme
modificative est une dérivation, pas une rédaction.

Deux niveaux, et le mur est au premier. **Le plan de mesure** éclate la mesure en
lots, chacun avec son siège, son verbe et sa raison ; `rien à faire` est un
résultat et se déclare, faute de quoi un lot muet ne se distingue pas d'un lot
oublié. Le plan est complet quand les six fonctions sont répondues, « sans
objet » compris : norme, privilèges, statut, contrats et situations en cours,
patrimoine, contrôle devenu sans objet. **La rédaction lot par lot** vient après,
et le trois colonnes s'y applique là seulement.

**La condition de passage est mécanique et ne demande aucun jugement** : une
forme modificative qui ne redonne pas C est fausse. C'est le seul endroit de la
chaîne où une sortie rédigée se prouve. Si elle ne se prouve pas, l'étape ne
passe pas : elle reprend ou elle remplit `hors_capacite`.

Deux sorties qui ne sont pas des rédactions cibles. **Les crédits** : un
amendement de crédits porte un tableau sur une ligne de l'état — mission,
programme, catégorie —, il n'a ni A ni C. **L'article de coordination ou de
transition** : l'étape dit qu'il en faut un, ce qu'il doit régler et sur quel
précédent le modeler ; le délai, le prix et qui paie reviennent au déposant.

L'étape **nomme** ce qui reste à trancher — le branchement sur le texte déposé,
le gage, l'entrée en vigueur, le fait générateur — et elle ne le décide pas.

### E4 bis — Le gage

Il n'a pas de numéro parce qu'il n'a pas d'autonomie : il se joue au moment où
le dispositif est écrit, et il s'écrit **en dernier paragraphe du dispositif**,
jamais dans le texte cible. Procédure entière à `procedures/gage.md`.

L'ordre de recherche a quatre branches, et la première qui répond ferme la
question : pas de perte de recettes → pas de gage ; consigne du dossier →
elle prime ; niche du même impôt ou du même secteur ; à défaut, la formule
standard, au verbatim. **Une charge n'est jamais gageable ; une recette l'est
toujours.** Le support change selon qui perd la recette — État, organismes de
sécurité sociale, collectivités territoriales —, et les formules ne
s'interchangent pas.

Si le cas n'est aucun des trois relevés, la formule **se relève sur pièce** sur
un amendement récemment déposé sur le même véhicule. Elle ne se reconstitue pas
par analogie : elle est bonne parce qu'elle est employée.

### E5 — Exposé sommaire

| | |
|---|---|
| lit | E0, E1, E3 (renvois), E4 |
| écrit | l'en-tête à quatre éléments, l'exposé en trois temps de 200 à 300 mots, et la liste des renvois signalés en fin d'exposé |
| on passe si | l'exposé tient le gabarit et chaque chiffre porte sa source |

Gabarit entier à `procedures/gabarit_expose_sommaire.md`. Le critère central
commande tout : *un exercice pédagogique d'exposition d'un dispositif technique,
mis en rapport avec un objectif politique clairement identifiable.* Le lecteur
visé est double — la séance et le journaliste.

Trois règles à tenir en conduite. **Le français parlementaire l'emporte** sur le
vocabulaire propre au déposant. **Un chiffre dont la source n'est pas traçable
ne sort pas** — et les travaux du déposant ne font pas source : ils fournissent
l'argument, la pièce extérieure fournit la citation. **Les appels de note, les
notes et les références ne comptent pas** dans les 200 à 300 mots.

Un exposé à deux temps est un signalement, pas un échec. Un exposé sans pièce
opposable au constat l'écrit dans `doutes`.

### E6 — Contrôles de sortie

| | |
|---|---|
| lit | tout le dossier |
| écrit | la liste des contrôles joués, leur rang et leur verdict |
| on passe si | aucun contrôle de rang « échec » ne sort |

Trois familles qui ne se mélangent pas. **La forme** — gabarit, longueur,
en-tête, sources. **La généralisation** — aucune sortie ne nomme un déposant,
une organisation, un référentiel propre ; c'est ce que joue `controle_sortie.py`,
et il bloque. **Le registre** — celui de la séance, non celui du réseau.

Un contrôle qui doute est un contrôle mal écrit : à cette étape, `doutes` vaut
`aucun` ou le contrôle est à reprendre.

### E7 — Liasse

| | |
|---|---|
| lit | plusieurs dossiers clos |
| écrit | l'assemblage, la numérotation, l'ordre de dépôt, et quelles pièces tombent si une autre est adoptée |
| on passe si | chaque dossier assemblé est clos et le déposant a vu l'ordre |

La dernière colonne ne se déduit d'aucune donnée. Voir la section 4.

---

## 4. Les deux étapes qui ne sont pas outillées

Elles sont écrites, rien ne les joue. Les taire ferait croire à une machine
complète, et le déposant découvrirait le trou en séance.

### E1 — la recevabilité reste à sa charge

**C'est la dépendance la plus lourde de la chaîne.** La procédure de
`procedures/test_rattachement.md` est entière et se joue à la main : quatre
canaux parcourus un par un, chacun documenté sur pièce — l'état, l'annexe, le
tableau d'équilibre, **jamais l'exposé des motifs** —, puis la qualification,
puis le contrefactuel, puis la partie, puis le verdict.

**Ce que le déposant doit savoir, et qui lui est dit franchement :** une chaîne
qui rédige sans jouer cette étape produit des amendements irrecevables, et une
disposition impeccable sur une mesure hors domaine est perdue entière. Trois
points relèvent de lui et d'aucun outil : le choix du contrefactuel entre droit
constant et tendanciel ; le seuil au-delà duquel les pertes sur verdict
`fragile` coûtent en crédibilité plutôt qu'en articles ; l'emploi de l'argument
tiré de l'article 33 de la loi organique, qui est le plus fort du test et à
double tranchant.

**Ce qui se joue quand même, et gratuitement :** le précédent. Le point d'accès
aux amendements déposés porte le sort de chacun — irrecevable, retiré, rejeté,
adopté. Un amendement voisin déclaré recevable est la meilleure preuve
disponible.

### E7 — la liasse n'existe qu'à moitié

L'assemblage et la numérotation se font ; **l'ordre de dépôt et les
neutralisations réciproques sont des décisions politiques** et reviennent au
déposant. La chaîne les porte, elle ne les calcule pas.

Deux choses qu'elle sait voir et qu'il faut lui faire voir. **Deux dossiers qui
visent la même adresse se neutralisent ou se contredisent** — c'est exactement le
risque que la colonne vecteur est faite pour révéler, et aucune lecture mesure
par mesure ne le montrerait. **Une même ligne ne sert pas deux fois de gage**, et
on ne gage pas sur une ligne qu'un autre amendement de la liasse supprime.

En l'absence de réponse, la liasse sort dans l'ordre de production, et le rendu
le déclare : *ordre non arbitré*.

---

## 5. La sortie .docx

La liasse se rend en `.docx` déposable par `generateur_liasse_docx.py`.

**Il attend une liasse à cette nomenclature**, et il ne la devine pas :

```
# NOTICE
# AMENDEMENTS
# ANNEXE
```

Trois titres de premier niveau, dans cet ordre. `# NOTICE` porte ce qui présente
la liasse ; `# AMENDEMENTS` porte les pièces déposées, chacune avec son en-tête,
son dispositif et son exposé sommaire ; `# ANNEXE` porte ce qui accompagne sans
être déposé.

**L'appel :**

```
python3 generateur_liasse_docx.py <la liasse à la nomenclature ci-dessus>
```

*Aucune option, aucun argument supplémentaire et aucun jeu de profils ne sont
documentés ici : ils ne sont pas relevés. L'en-tête du générateur fait foi sur ce
point, et rien ne doit être deviné.*

**Avant de générer**, `controle_sortie.py` passe sur la liasse : il bloque, et une
fuite dans un `.docx` déjà transmis ne se rattrape pas.

---

## 6. Les cinq fautes qui coûtent le plus cher

1. **Prendre une adresse citée pour une adresse modifiée.** Un article du texte
   déposé peut en citer un autre sans le modifier ; le siège se prend à ce que le
   texte modifie, jamais à ce qu'il mentionne.
2. **Écrire le gage de l'État sur une perte sociale.** Le support est le même,
   le verbe ne l'est pas — taxe additionnelle *créée* d'un côté, accise
   *majorée* de l'autre. Les formules ne s'interchangent pas.
3. **Rédiger sur un article dont la version a changé.** Le texte en discussion a
   été écrit avant les lois promulguées depuis : au millésime courant, l'article
   porte le résultat de la modification et non son point de départ, et la colonne
   A est fausse sans que rien ne le dise.
4. **Énoncer une règle de droit sans l'avoir relevée.** Une formule de gage, une
   porte du domaine, un texte en vigueur : cela se relève sur pièce, avec son
   identifiant et sa date. Un vecteur vraisemblable envoie l'amendement au
   mauvais endroit, avec l'apparence d'une adresse.
5. **Soigner le gage et perdre l'amendement sur le domaine.** En loi de
   financement, deux filtres se succèdent et le domaine se vérifie **avant** le
   gage : un amendement parfaitement gagé tombe quand même s'il n'avait rien à
   faire dans ce véhicule.
