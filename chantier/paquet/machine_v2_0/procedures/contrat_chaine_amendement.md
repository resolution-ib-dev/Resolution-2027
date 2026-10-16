# Contrat de la chaîne de l'amendement

*Écrit le 20260902. Il dit ce que chaque étape reçoit, ce qu'elle rend, et ce
qu'elle déclare avoir douté. Il est **véhicule-agnostique par construction** :
c'est lui qui rend la machine généralisable, et il s'écrit avant la troisième
skill, faute de quoi celle-ci fixerait un contrat implicite.*

Il se lit avec `procedures/test_rattachement.md` — qui dit si la mesure peut
voyager — et `procedures/procedure_vecteurs.md` — qui dit comment on trouve le
siège. Ces deux-là décrivent **une** étape chacun ; celui-ci décrit **ce qui
passe entre elles**.

---

## 1. Ce que la chaîne est, et ce qu'elle n'est pas

**C'est une procédure outillée**, pas un lot d'amendements. Elle prend l'énoncé
d'une mesure en langage naturel et rend un amendement déposable, pour n'importe
qui, sur n'importe quel véhicule — projet de loi de finances, projet de loi de
financement de la sécurité sociale, proposition de loi ordinaire, organique ou
constitutionnelle.

**Elle outille un travail juridique, elle ne l'automatise pas.** Une chaîne qui
prétendrait le contraire sortirait des dispositions plausibles et fausses, et
une disposition plausible est plus dangereuse qu'une disposition absente.

**L'avancée ne se mesure pas en amendements produits.** Elle se mesure à l'état
des étapes : `n'existe pas` → `écrite` → `enregistrée` → `éprouvée` →
`généralisée` → `dégradée proprement`. Le compte des amendements est celui d'une
passe.

---

## 2. La forme du passage — un objet unique, à lecture bornée

**Arbitré le 20260902**, dans ces termes : *les étapes doivent être
découpables pour être décomposables et recomposables, mais l'utilisateur ne doit
pas voir cette complexité — il voit la boucle complète.*

Deux exigences, et elles sont l'une et l'autre tenues par une seule forme.

**Un objet unique voyage** — le **dossier de mesure**. Chaque étape y ajoute son
bloc et n'efface jamais rien. L'utilisateur donne un énoncé et reçoit un
amendement : il ne compose pas des étapes, il ne recopie rien d'une étape à la
suivante, et il n'a pas à connaître ce découpage.

**Chaque étape déclare ce qu'elle lit.** Un bloc `lit` et un bloc `ecrit`, écrits
dans la skill et vérifiés mécaniquement. Une étape qui lit un bloc qu'elle n'a
pas déclaré est en faute. C'est ce qui garde ce découpage réel : une étape se
rejoue seule en ne lui donnant que les blocs qu'elle déclare lire, et son taux se
mesure sans que le reste du dossier lui souffle la réponse.

*Ce que cela écarte, et pourquoi.* Le relevé par étape — chaque étape rend une
fiche autonome — s'éprouve aussi bien mais fait recopier le contexte à la main
entre deux étapes, donc à l'utilisateur ; c'est la complexité que vous refusez
de lui montrer. Le relevé par étape doublé d'un socle commun recopié met le même
énoncé en plusieurs exemplaires : deux points de vérité dès qu'une étape le
corrige, ce qu'une décision antérieure interdit.

---

## 3. Le dossier de mesure

Un objet, huit blocs, une entrée par étape. Les trois premiers champs de chaque
bloc sont les mêmes partout, et c'est l'invariant du contrat.

```
mesure                      identifiant local du dossier, sans signification
vehicule                    plf · plfss · ppl · pplo · pplc · a_determiner
                            DONNÉE DU DOSSIER, jamais hypothèse d'une étape

<bloc d'étape>
  etape                     le nom de l'étape
  recu                      la liste EXACTE des blocs lus, et rien d'autre
  doutes                    ce dont l'étape a douté dans ce qu'elle a reçu,
                            un doute par ligne, avec ce qui le lèverait
  gisements                 les rôles de matériel effectivement remplis,
                            nommés par leur rôle et jamais par un fichier
  degradation               complet · partiel · a_blanc
  hors_capacite             vide, ou la raison pour laquelle l'étape ne sait
                            pas traiter ce véhicule ou ce cas
  <les champs propres à l'étape>
```

**`recu` et `doutes` sont obligatoires et ne se laissent jamais vides.** Une
étape qui n'a douté de rien écrit `aucun`. C'est l'invariant : *chaque étape
déclare ce qu'elle a reçu et si elle en a douté.* Un doute tu se retrouve en
séance.

**`hors_capacite` rempli arrête la chaîne à cette étape et la rend telle
quelle.** Il ne se contourne pas par une réponse approchante. C'est la règle du
vecteur appliquée à toute la chaîne : *un résultat vraisemblable est plus
dangereux qu'un résultat absent.*

---

## 4. Les huit étapes

### E0 — Qualification

| | |
|---|---|
| reçoit | l'énoncé en langage naturel, le véhicule visé s'il est dit |
| rend | le **statut** de la mesure, le **levier** quand il y a lieu, et le véhicule qualifié |
| doute type | l'énoncé mêle deux mesures ; le statut n'est pas déterminable sur l'énoncé seul |

Le statut décide de la famille de siège, et il se qualifie **avant** de chercher
quoi que ce soit : crédits d'État, dépense fiscale, dépense sociale, dépense
locale, dépense d'opérateur, mesure de pure norme.

**Sur la dépense locale, le levier est triple et se cherche en entier** —
arbitré le 20260902. Trois sièges, dans cet ordre :

| ordre | levier | siège | véhicule |
|---|---|---|---|
| 1 | la **recette** — dotations et fiscalité affectée | code général des collectivités territoriales pour les dotations ; code général des impôts et fiscalité affectée pour les recettes | loi de finances |
| 2 | la **dotation** — prélèvement sur recettes et concours | code général des collectivités territoriales | loi de finances |
| 3 | la **norme** — la compétence ou l'obligation qui produit la dépense | code sectoriel | loi ordinaire |

L'étape rend **les trois adresses quand elles existent** et dit, pour chacune, si
elle est portable dans le véhicule visé. Elle ne choisit pas : réduire la
ressource ne commande pas l'emploi, et la collectivité peut arbitrer contre la
mesure — cela se dit plutôt que de se découvrir en séance.

### E1 — Rattachement

| | |
|---|---|
| reçoit | E0 |
| rend | le verdict — `acquis`, `plaidable`, `fragile`, `non rattachable` —, la partie, les quatre canaux avec leur montant et leur pièce, la qualification, le contrefactuel |
| doute type | un canal sans montant documenté ; un contrefactuel qui ne tient qu'en tendanciel |

Procédure entière à `procedures/test_rattachement.md`. **Elle est écrite et non
outillée** : c'est le trou le plus coûteux de la chaîne, parce qu'une machine qui
rédige sans elle produit des amendements irrecevables.

**Véhicule-agnostique** : le test change de porte selon le véhicule et ne change
pas de forme. Pour une loi de finances, les portes du domaine ; pour une loi de
financement, les articles du code de la sécurité sociale qui portent les
dispositions facultatives — **et non l'article `LO 111-3`, qui ne définit plus
depuis 2022 que les trois espèces de lois de financement**. Pour une proposition
de loi, le test est sans objet et l'étape rend `sans_objet`, pas un verdict vide.

### E2 — Vecteur

| | |
|---|---|
| reçoit | E0, E1 |
| rend | une ou plusieurs **adresses** décomposées — code · siège · article · subdivision —, chacune avec son rôle, sa provenance, son identifiant et sa date de relevé |
| doute type | le code se déduit d'une numérotation au lieu d'être nommé ; deux mesures visent la même adresse |

**Le vecteur et le véhicule ne se confondent jamais** : le vecteur dit quel
article on modifie, le véhicule dit dans quel texte on dépose. Une ligne de
rattachement — « après l'article 65 » — nomme le véhicule.

**L'adresse se décompose du macro au micro et rien ne se recolle.** `158-5-a`
n'est pas une adresse, c'est trois niveaux collés.

Trois états possibles, et le troisième n'est pas un échec : `trouve`,
`a_trouver`, `siege_non_codifie` — la mesure est rédigeable, elle n'a pas
d'article à modifier.

### E3 — Droit applicable

| | |
|---|---|
| reçoit | E2 |
| rend | le **texte en vigueur** de chaque adresse, avec son identifiant et sa date de version ; les **renvois entrants**, chacun avec sa certitude ; l'avertissement d'abrogation programmée |
| doute type | un article applicable dont l'abrogation est déjà votée ; un renvoi de certitude `ambigu` |

**L'applicabilité se lit aux dates, jamais à l'état.** Un article peut
s'appliquer aujourd'hui et porter une abrogation déjà votée ; le filtrer sur son
état seul fait disparaître du droit en vigueur sans un message.

**Les renvois entrants sont le trou que rien ne comblait.** Modifier un article
laisse derrière lui les articles qui le citent. Trois certitudes, fixées par une
règle de déduction et jamais par une impression : `nomme`, `interne`, `ambigu`.

**Le régime dépend du véhicule, et c'est le seul endroit du contrat où il en
dépend** — arbitré le 20260902 :

| véhicule | régime des renvois |
|---|---|
| amendement | **service minimum** : on ne coordonne pas, on signale. La liste va en fin d'exposé sommaire. |
| proposition de loi | **la boucle va jusqu'au bout** : chaque renvoi se traite ou se déclare sans objet avant dépôt. |

**Ce qui n'est pas couvert se dit** : le droit non codifié. Un siège logé dans
une loi de finances antérieure n'est pas dans l'extrait, et l'étape le déclare
plutôt que de rendre l'adresse la plus proche.

### E4 — Rédaction cible

| | |
|---|---|
| reçoit | E0, E2, E3 |
| rend | pour chaque adresse, trois colonnes — **A** le texte en vigueur, **B** la réforme visée, **C** le texte révisé — et, dérivée de la comparaison A → C, la forme modificative |
| doute type | deux rédactions produisent le même effet et diffèrent de portée ; l'article est déjà rouvert par le texte déposé et C ne se porte pas au même endroit |

**Le cœur de l'étape est le signe « = ».** A plus B égale C. Elle produit **le
texte de l'article tel qu'il sera**, pas la phrase qui l'y amène. C'est un
travail qui ne dépend d'aucun véhicule : on écrit une modification du droit, on
la branche ensuite.

**Ce travail a déjà été fait deux fois** — sur la Constitution et sur la
loi organique relative aux lois de finances. Le trois colonnes est la forme
éprouvée : texte actuel · réforme visée · rédaction révisée, la justification en
deuxième colonne et en note de la troisième. Elle se transpose, et elle se
transpose mieux qu'alors : **la colonne A n'était un verbatim que pour 26 blocs
sur 37 et 21 sur 29** ; elle l'est désormais toujours, le texte en vigueur venant
du dépôt de droit avec son identifiant et sa date.

**L'étape a deux niveaux, et le mur est au premier.**

**Niveau 1 — le plan de mesure.** Une mesure n'attaque presque jamais un seul
article. Elle éclate en **lots**, chacun avec son siège, son verbe et sa raison.
C'est ce qui se fait déjà à la main sur le logement social, et c'est la
partie qui décide de tout : une rédaction impeccable sur un plan incomplet donne
une loi incohérente, et rien en aval ne le rattrape.

Huit verbes, relevés sur cette note et sur la révision constitutionnelle :

| verbe | ce qu'il fait |
|---|---|
| `abroger` | l'article ou la fourchette disparaît |
| `abroger sauf` | le bloc disparaît, les exceptions sont nommées une à une |
| `supprimer une subdivision` | le III, le 4° alinéa, le 7 du II |
| `maintenir avec adaptation` | l'article reste, sa portée change |
| `coordonner` | un article neuf fait la bascule d'un régime à l'autre |
| `transitionner` | le sort des contrats et situations en cours, avec son délai |
| `ponctionner` | le sort du patrimoine, avec son prix |
| `rien à faire` | **c'est un résultat, et il se déclare** |

**`rien à faire` est le verbe qui sépare un plan complet d'un plan qu'on croit
complet.** Un lot muet ne se distingue pas d'un lot oublié.

**La grille de complétude — six fonctions.** Le plan est complet quand les six
sont répondues, « sans objet » compris. Cinq sont relevées sur la note de référence,
la sixième est ajoutée par déduction et attend l'utilisateur.

1. **la norme** — ce qui oblige, interdit ou réserve ;
2. **les privilèges** — fiscalité dérogatoire, ressource affectée, garantie ;
3. **le statut** — l'existence et la forme juridique des acteurs ;
4. **les contrats et situations en cours** — baux, conventions, droits acquis ;
5. **le patrimoine** — fonds propres, titres, prix de transfert ;
6. **le contrôle et le reporting devenus sans objet** — *ajouté, à valider*.

**Niveau 2 — la rédaction, lot par lot.** C'est là que le trois colonnes
s'applique, et là seulement.

---

**Trois procédures, et elles ne sont pas des variantes : elles s'enchaînent.**

**Le levier et ses dépendants — elle décide.** On nomme le **segment** qui porte
la norme attaquée, un seul, avec sa raison ; C s'écrit d'abord là. Puis on suit
la cascade à l'intérieur de l'article et de son voisinage : définitions
employées, dérogations et exceptions qui le visent, renvois internes numérotés,
renumérotation, clause de sanction, clause d'entrée en vigueur. **Cette cascade
est en grande partie mécanique** — un renvoi interne est un motif, pas un
jugement. C'est la coordination du dépôt de droit, un cran plus bas : celle-là
voit qui cite l'article, celle-ci voit ce qui, dans l'article, dépend du segment.

**Le balayage de couverture — il contrôle, et il ne rédige pas.** L'article se
relit segment par segment, du premier au dernier, avec une seule question
fermée : *ce segment reste-t-il vrai sous la mesure ?* Trois verdicts —
`inchangé`, `touché, traité`, `touché, non traité`. **Le troisième est la sortie
utile** : c'est ce que le levier et la cascade ont manqué. Le balayage finit
quand chaque segment porte un verdict ; un segment sans verdict est une
rédaction incomplète, et cela se compte.

*Pourquoi dans cet ordre, et pas l'inverse.* Lire du haut et corriger au fil fait
rédiger dans l'ordre de lecture : la portée dérive, et il faut plusieurs boucles
d'harmonisation qui ne convergent pas. **Une passe de jugement, une passe de
vérification, aucune oscillation.**

**L'analogie — elle génère, et seulement là où A est vide.** On prend un
dispositif existant comparable et on en transpose le **squelette** — assiette,
bénéficiaire, taux, plafond, fait générateur, sanction, entrée en vigueur,
renvoi au pouvoir réglementaire — jamais les mots, faute de quoi on importe le
régime du modèle sans le savoir. **L'écart au modèle est le contrôle** : chaque
écart est délibéré et déclaré, ou c'est un oubli.

*Elle sert deux cas et deux seulement* : l'article créé qui **porte** la mesure —
rédigé —, et l'article de coordination ou de transition — **signalé, non
rédigé** : la skill dit qu'il en faut un, ce qu'il doit régler et sur quel
précédent le modeler ; le délai, le prix et qui paie sont des décisions
politiques et reviennent à l'utilisateur.

---

**Six opérations sur le texte, du plus simple au plus lourd.** C'est l'échelle de
difficulté de l'étape, et c'est par elle qu'elle se borne.

| | opération | ce que C vaut |
|---|---|---|
| 1 | abroger l'article entier | C est vide |
| 2 | abroger une subdivision | C = A moins la subdivision, la renumérotation déclarée |
| 3 | remplacer un membre de phrase, un nombre, un taux | C = A, un fragment changé |
| 4 | compléter — un alinéa, une subdivision, une phrase | C = A plus un fragment, à sa place |
| 5 | réécrire l'article | C ne se lit plus dans A |
| 6 | créer un article qui n'existe pas | A est vide, C est tout |

Le cas dur n'est aucun des six pris seul : c'est leur combinaison sur un même
article — *ceci à la place de cela, et cela en plus*. Il se rend en une seule
colonne C, jamais en une liste d'instructions.

**La forme modificative n'est pas une rédaction, c'est une dérivation.**
« L'article X est abrogé », « au deuxième alinéa, les mots … sont remplacés par
… », « il est inséré un article ainsi rédigé » se déduisent de la comparaison
entre A et C, dans la grammaire du véhicule et selon le répertoire de formules.

*Et elle se contrôle mécaniquement* : **la forme modificative, réappliquée à A,
doit redonner C à l'octet.** Une forme qui ne redonne pas C est fausse, et cela
se voit sans jugement. C'est le seul endroit de la chaîne où une sortie rédigée
se prouve.

**Ce qui n'est pas une rédaction cible et sort de l'étape : les crédits.** Un
amendement de crédits ne modifie aucun texte — il porte un tableau sur une ligne
de l'état, mission, programme, catégorie, **jamais un montant en dur**. Il n'a ni
A ni C, et le faire passer par le « = » serait plier un objet dans une forme qui
n'est pas la sienne. Il relève d'un gabarit propre, écrit une fois.

**Elle ne se juge pas en égalité de rédaction** : deux rédacteurs écrivent deux
textes qui produisent le même effet de droit. Ce qui se compare est la
**correspondance** — même article visé, même opération, même portée.

Elle **nomme** ce qui reste à trancher — le branchement sur le texte déposé, le
gage, l'entrée en vigueur, le fait générateur, l'avertissement d'abrogation
programmée — et elle ne le décide pas.

### E5 — Exposé sommaire

| | |
|---|---|
| reçoit | E0, E1, E3 (renvois), E4 |
| rend | l'en-tête à quatre éléments et l'exposé en trois temps, 200 à 300 mots, sources entre parenthèses avec note, **plus la liste des renvois signalés en fin d'exposé** |
| doute type | une pièce opposable manque et le constat repose sur vos seules notes de travail |

Le critère central commande le reste : *un exercice pédagogique d'exposition d'un
dispositif technique, mis en rapport avec un objectif politique clairement
identifiable.* Le lecteur visé est double — la séance et le journaliste — et
c'est ce qui borne la langue.

**Sur les trois temps, être plus strict que le gold standard est un défaut ; sur
les sources, l'être est l'objectif.**

**Le registre est arbitré** — 20260902 : **le français parlementaire
l'emporte** quand il diverge de notre vocabulaire. L'exposé s'écrit dans la
langue de la séance, ce qui est la condition pour que l'outil serve n'importe
qui. *Trois mots tenus sont proposés, non validés* : **restitution**,
**bureaucratie**, **intermédiaires** — ils portent le fond et non le style. La
liste se révoque d'un mot.

**La règle de décompte des mots se déclare**, et elle n'était pas déclarée : les
appels de note, le texte des notes et le texte des références **ne comptent pas**
dans les 200 à 300 mots. Sur une borne à 200, quatorze mots décident.

### E6 — Contrôles de sortie

| | |
|---|---|
| reçoit | tout le dossier |
| rend | la liste des contrôles joués, leur rang — échec ou signalement — et leur verdict |
| doute type | aucun : un contrôle qui doute est un contrôle mal écrit |

Trois familles, et elles ne se mélangent pas. **La forme** — gabarit, longueur,
en-tête, sources. **La généralisation** — contrôle `G`, aucune sortie ne nomme un
déposant, un projet, un référentiel interne. **Le registre** — un jeu de règles
par registre, celui de la séance et non celui du réseau.

### E7 — Liasse

| | |
|---|---|
| reçoit | plusieurs dossiers clos |
| rend | l'assemblage, la numérotation, l'ordre de dépôt, et **quelles pièces tombent si une autre est adoptée** |
| doute type | deux dossiers visent la même adresse et se neutralisent |

La dernière colonne est de la stratégie parlementaire : elle ne se déduit
d'aucune donnée et revient à l'utilisateur. L'étape la porte, elle ne la calcule pas.

---

## 5. Les quatre règles qui traversent toutes les étapes

### G1 — Le véhicule est une donnée, jamais une hypothèse

Aucune étape ne suppose le véhicule à partir de ce qu'elle voit. Elle le lit au
dossier. **Chaque étape déclare les véhicules qu'elle sait traiter** ; devant un
autre, elle remplit `hors_capacite` et s'arrête. Une étape qui traite un
véhicule inconnu comme s'il était une loi de finances est en faute, même quand
elle tombe juste.

### G2 — Aucune étape ne dépend d'une documentation interne pour fonctionner

Une étape qui exige le socle, un texte de fond ou vos positions pour rendre un
résultat n'est pas une étape de la machine : c'est une étape d'une passe.
**Elle doit tourner à blanc et le déclarer.**

**La distinction qui commande tout le reste est celle de la dépendance et de la
commodité** — arbitré le 20260907. Le matériel n'est pas interdit,
il est facultatif. Une étape s'en sert quand il est là, et rend un résultat de
moindre portée quand il ne l'est pas ; elle n'échoue jamais de son absence.

**Une étape nomme un rôle, jamais un fichier.** « Un réservoir d'arguments
sourcés », « une source de niches », « les annexes du texte déposé », « un
référentiel de sièges déjà relevés ». **C'est le dossier qui dit quel fichier
tient le rôle**, et un tiers y branche les siens. C'est ce qui rend la chaîne
diffusable sans la priver de matière.

**Le matériel vit dans un dossier de matière séparable et optionnel**, retiré pour
diffuser et gardée pour l'usage propre. Ce qu'il porte y entre **projeté en
clair** — arguments et chiffres sourcés, sans nomenclature interne : la
projection n'est pas un coût de production, c'est elle qui sépare la chaîne de sa
source.

Quatre rôles, cumulatifs, aucun ne plafonne le registre : le contexte fourni par
l'utilisateur, les annexes du texte chargé, la recherche publique, le réservoir
d'arguments quand le matériel optionnel est là. Chaque étape déclare ceux dont elle a
disposé, et sa dégradation — `complet`, `partiel`, `a_blanc`.

**Le taux d'une étape se lit avec sa dégradation, et les deux configurations se
mesurent l'une contre l'autre.** Un taux mesuré à blanc est un plancher. Le même
banc rejoué équipé, **sur la même population aveugle**, donne le second taux, et
**l'écart entre les deux est la valeur du matériel** — un chiffre, non une
impression. À blanc est le mode de base ; équipé est l'environnement cible.

### G3 — Aucune sortie ne nomme un déposant, un projet, un référentiel interne

Ni dans le corps, ni dans le frontmatter, ni dans la description enregistrée —
c'est là que la fuite a survécu le plus longtemps. Le contrôle `G` le vérifie
mécaniquement, et il bloque : une règle qu'on tient à l'œil se perd, et elle
s'est perdue quatorze fois.

**L'input d'un tiers se prend à face value**, de manière neutre. Sans quoi
l'outil n'est pas public.

### G4 — La ligne fait / conclusion

Les faits, les calculs et les arguments voyagent ; seule la **mesure proposée**
ne voyage pas. La coupe passe entre ce qui *soutient* et ce qui *décide*, jamais
entre les faits et les idées.

---

## 6. Ce que le contrat rend contrôlable

Trois choses se vérifient mécaniquement dès qu'un dossier existe, et elles ne
demandent aucun jugement.

**Un bloc d'étape sans `recu` ou sans `doutes` est incomplet.** L'invariant se
compte.

**Une étape qui lit un bloc hors de sa déclaration est en faute.** C'est ce qui
prouve que ce découpage est réel et non affiché.

**Une étape qui rend un résultat en `a_blanc` sans l'avoir déclaré est en
faute**, et une étape qui ne rend rien à blanc sort au contrôle `G`. **Une étape
qui nomme un fichier de ce matériel au lieu de son rôle est en faute de la même
manière**, et le contrôle `G` la voit.

Ce que le contrat ne rend pas contrôlable, et qui se dit : la justesse d'une
adresse, la portée d'une rédaction, la force d'un plaidoyer. Cela se mesure sur
un banc d'épreuve, jamais par un contrôle
de forme.

---

## 7. Ce qui reste ouvert

1. **E1 n'est pas outillée.** La procédure est écrite, rien ne la joue. C'est la
   dépendance la plus lourde de la chaîne.
2. **E7 n'existe pas**, et sa dernière colonne revient à l'utilisateur.
3. **Les trois mots tenus de E5 sont proposés, non validés.**
4. **Le gabarit du bloc de crédits de E4**, et si l'étape rend une seule
   rédaction ou les variantes concurrentes.
