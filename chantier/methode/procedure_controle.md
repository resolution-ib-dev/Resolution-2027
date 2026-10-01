# PROCÉDURE DE CONTRÔLE — corpus chiffré Résolution

Version 20260820 v2. Étend la v1 au balayage des notes de fin et au référentiel
des positions.

## Ce qui échoue quand elle n'est pas suivie

Quatre erreurs commises le 20260819, quatre expressions d'un même défaut :
le chiffre est évalué avant sa phrase et avant ses voisins.

| erreur | ce qui a été fait | ce qui manquait |
|---|---|---|
| 236 Md€ de niches promus en entrée | un champ dérivé lu comme un fait | vérifier au manuscrit avant de créer |
| 1 105 ramené à 1 104 | le classeur a corrigé le manuscrit | établir le statut d'ancre d'abord |
| 8 800 € traité comme ancre | une valeur d'aval héritée sans provenance | remonter la chaîne jusqu'au texte |
| rythme de restitution jugé contradictoire | un nœud évalué seul | traverser le renvoi vers son amont |

Aucune de ces erreurs n'est arithmétique. Toutes les quatre sont des erreurs de
lecture, et toutes les quatre sont détectables par une précondition.

## Ordre de traitement, non commutatif

Chaque étape conditionne la suivante. Aucune ne s'anticipe.

### 0. La note avant la phrase

Le manuscrit explicite en note de fin ce que son corps laisse implicite :
hypothèses de calcul, sources, ordres de grandeur, contre-arguments,
définitions. Cent quarante et une notes, dont trente-sept portent un chiffre.

Un balayage qui ne lit que le corps des sections rate la moitié du raisonnement.
Le coût du risque de crise, le gain de croissance attribué à la simplification
fiscale, le multiplicateur des niches, le champ des secteurs sensibles, la
qualification en rente de ce que solde le plan de départ : tous vivent en note,
aucun n'apparaît dans le corps.

**Règle.** Toute recherche au manuscrit balaie le corps *et* les notes. Le relevé
`Notes_manuscrit_AAAAMMJJ_vN.json`, régénéré par `extraire_notes.py`, sert de
point d'entrée. Il ne se corrige jamais à la main : il se régénère à chaque
version du manuscrit.

**Ce que la note ne fait jamais.** Elle ne se recopie pas. Ni au REF, ni au
référentiel des positions, ni dans un livrable. Elle se cite par son
identifiant, et son texte est tiré du relevé au moment de la génération. Une
note recopiée est un cache que personne ne rafraîchit — le défaut commis le
20260820 sur le bloc `ANCRAGES_MANUSCRIT` et corrigé le même jour.

### 1. La phrase avant le nombre

Localiser le chiffre au manuscrit et lire la phrase entière qui le porte, plus la
précédente et la suivante. Recopier le passage en `source_ancre`, entre
guillemets français.

La phrase porte ce que le nombre ne porte pas : la base — par personne, par foyer,
par travailleur — le point de départ — « au bout de six mois » — le sens — « au
moins », « jusqu'à », « environ » — et le périmètre — « hors outre-mer », « hors
APL ». Un nombre extrait sans sa phrase a perdu exactement l'information qui
résout les contradictions apparentes.

Chercher en chiffres **et en lettres**. « Trois premiers mois » et « sept ans »
échappent à tout balayage numérique. Une entrée qu'on s'apprête à déclarer
absente se revérifie sur ses formes en lettres, sans exception.

### 2. Le statut d'ancre avant le calcul

Trois valeurs, exclusives.

| statut | règle |
|---|---|
| `manuscrit` | prévaut toujours. L'écart du classeur se consigne, jamais ne corrige |
| `classeur` | valeur de travail, à déclarer comme telle dans tout emploi externe |
| `absent des deux` | non diffusable. Ni à corriger, ni à employer, ni à arrondir |

Une valeur qui ne se retrouve nulle part n'est pas un chiffre : c'est une
corruption présumée. Elle ne devient jamais une entrée, et jamais un homonyme.

Un champ dérivé — `bornes`, `certitude`, `enonce` — n'est jamais une source. Il
peut porter une corruption depuis des années sans que rien ne le signale.

### 3. Le voisinage avant le verdict

Avant de clore une entrée, lire ses `depend`, sa `chaine`, et les `renvois` de sa
proposition. Un chiffre isolé n'a pas de sens : un rythme se compte depuis son
point de départ déclaré, un montant par tête depuis sa population déclarée, une
durée depuis son origine déclarée.

**Charge de preuve asymétrique.** Un verdict destructif — contradiction,
irréductible, non instruit, absent des deux — coûte davantage qu'un verdict
d'attente. Il exige donc davantage : deux passages du manuscrit cités côte à
côte pour une contradiction, et la trace écrite de la lecture du voisinage dans
tous les cas. À défaut, le verdict est « à instruire », jamais « contradictoire ».

### 4. L'arithmétique en dernier

Une fois la phrase lue, le statut posé, le voisinage traversé. Le calcul ne
tranche jamais un statut : il vérifie une chaîne déjà établie.

Quand un calcul ne retombe pas sur l'ancre, l'ordre de recherche de l'écart est :
arrondi de communication, base implicite, point de départ, modalité déclarée en
note, portée des mots, reste du manuscrit. Une ancre irréductible est rare, et
elle suspend.

## Ce qui rend la procédure opposable

Les règles ci-dessus ne valent que si une machine les vérifie. Trois dispositifs.

### Le schéma force la question

Dix propriétés par entrée. `statut_ancre` et `source_ancre` rendent impossible de
poser un verdict sans avoir répondu à « d'où vient ce chiffre » et « quelle phrase
le porte ».

### `controle_structurel.py` vérifie les préconditions

Quatorze règles, rejouées à chaque versement. Elles ne vérifient aucun calcul :
elles vérifient que les conditions de lecture ont été remplies.

| règle | ce qu'elle empêche |
|---|---|
| R1 | une entrée numérique non peuplée |
| R2 | une propriété manquante |
| R3 | un statut hors nomenclature |
| R4 | une ancre du manuscrit sans citation du passage |
| R5 | un verdict destructif sans voisinage instruit |
| R6 | une origine tirée d'un champ dérivé |
| R7 | une reconstitution présentée comme relevé |
| R8 | un renvoi porteur d'une chaîne propre |
| R9 | une valeur de classeur qualifiée d'ancre |
| R10 | une borne présentée comme valeur unique |
| R11 | un identifiant dupliqué |
| R12 | un renvoi vers une cible inexistante |
| R13 | une dépendance vers une entrée inexistante |
| R14 | un dépendant sans chaîne |

R4, R5 et R6 correspondent exactement aux quatre erreurs du 20260819.

### `controle_notes.py` vérifie le chaînage des notes

Deux contrôles, dans les deux sens.

| règle | ce qu'elle empêche |
|---|---|
| N1 | une citation de note sans note correspondante au relevé — référentiel en retard sur le manuscrit |
| N2 | une note portant un chiffre qu'aucun référentiel ne cite — raisonnement chiffré du manuscrit resté hors du corpus |

N2 est le contrôle utile. Sans lui, une note chiffrée reste invisible jusqu'à ce
que quelqu'un la lise par hasard. Onze notes chiffrées sont non reprises au
20260820 : elles ne bloquent pas, elles se traitent au fil.

### `controle_sortie.py` vérifie les livrables

Contrôle de sortie sur les livrables diffusables. Deux règles ajoutées le
20260820 : un gain publié sans miroir nommé, une perte publiée sans raccroche
nommée.

### `controle_apports.py` vérifie les champs rédigés du côté gain

Huit contrôles sur la vedette et l'apport, joués à `make controle`. Deux sont
des échecs qui arrêtent, six des signalements qui se lisent.

| code | ce qu'il refuse | rang |
|---|---|---|
| `A1` | un apport qui reprend l'énoncé du nœud | **échec** |
| `A2` | huit mots consécutifs du manuscrit dans un apport | **échec** |
| `A3` | un apport hors registre — pas de deuxième personne du pluriel sur l'unité vedette + phrase | signalement |
| `A4` | une contrepartie recopiée de la formule générale | **échec** |
| `A5` | deux apports d'une même catégorie qui se ressemblent | signalement |
| `A6` | trois gains ou plus sous un même levier, non repliés | signalement |
| `A7` | le même apport porté par deux catégories sur le même ancrage | **échec** |
| `A8` | une vedette hors forme — ni grandeur, ni syntagme court, ni objet nommé au corpus | signalement |

`A3` s'exerce sur **l'unité vedette + phrase**, jamais sur la phrase seule : la
vedette et l'apport ne se citent pas séparément. `A7` est un échec parce qu'une
même matière dite deux fois dans les mêmes mots est la faute que l'attache et le
rappel existent pour empêcher.

### `controle_arithmetique.py` vérifie les chaînes

Soixante-et-onze contrôles, vingt-cinq écarts consignés. Un écart consigné n'est
pas un échec : c'est un écart connu, chiffré et assumé. Un échec est une chaîne
qui ne boucle pas.

## Ce que la conversation doit fournir

Deux choses économisent le plus de travail et de risque.

**Le passage, quand il est connu.** « C'est dans le texte » suffit à déclencher
la recherche, mais la phrase elle-même supprime l'aller-retour.

**Le lien amont, quand il existe.** Signaler qu'un nœud en présuppose un autre —
un point de départ, une population, une séquence — évite d'évaluer un nœud seul.
C'est ce qui manquait sur le rythme de restitution.

Ce qui ne sert à rien : demander plus de vigilance. La vigilance ne se stocke pas
d'une session à l'autre. Une assertion dans un script, si.

## Deux référentiels de même rang

Le `REF_doctrine` porte la mesure : paramètres, effets, chiffrage, renvois. Son
unité est l'entrée numérique.

Le référentiel des positions, `Positions_AAAAMMJJ_vN.json`, porte qui gagne, qui
perd et qui captait. Son unité est le triplet ancrage × position × catégorie.
Ses ancrages sont de quatre natures — effet, proposition, sous-item, passage du
manuscrit — dont trois n'ont pas de place dans le champ `effets` du REF. C'est
pourquoi les deux référentiels restent distincts : les fusionner découperait le
second en deux moitiés.

Ils partagent la même discipline — écriture à la main, contrôle par script,
dérivés régénérés — et la même règle de circulation : une correction remonte
vers la strate 1, elle ne circule jamais latéralement.

Trois contrôles propres au référentiel des positions :

| règle | ce qu'elle empêche |
|---|---|
| P1 | un gain sans miroir nommé |
| P2 | une perte sans raccroche nommée, parmi les trois valeurs admises |
| P3 | une perte sans justification écrite, ou une perte raccrochée sans relais |

La raccroche prend trois valeurs et une seule : renvoi vers une ligne de gain,
reconstitution volontaire du flux, absence assumée. Les trois se disent.

## Cycle de versement

À chaque versement, dans cet ordre :

1. `python3 extraire_notes.py Manuscrit.html Notes_manuscrit_AAAAMMJJ_vN.json` —
   à refaire dès que le manuscrit change
2. `python3 controle_structurel.py REF_doctrine_AAAAMMJJ_vN.json` — doit sortir 0
3. `python3 controle_arithmetique.py` — doit sortir 0 échec
4. `python3 controle_notes.py Notes.json REF.json Positions.json justifications.py`
   — N1 doit sortir 0 ; N2 se consigne
5. `python3 construire_positions.py Positions_AAAAMMJJ_vN.json` — 0 justification
   manquante, 0 orpheline
6. `python3 generer_arbre.py REF.json arbre.html` — 0 anomalie T1 et T2
7. `python3 generer_inventaire.py REF.json Positions.json Notes.json inv.html` —
   0 anomalie
8. Table des croisements mise à jour, les sept croisements passés
9. `ETAT_DU_CHANTIER` réécrit
10. Copie vers `/mnt/user-data/outputs/`

Une tranche est close quand les dix étapes sont faites. Aucune ne s'omet au
motif que la modification est petite : les quatre erreurs du 20260819 portaient
chacune sur un seul champ, et l'omission du balayage des notes le 20260820 a
laissé passer deux chiffres majeurs.

## Les sept croisements

1. Agrégat contre composants
2. Unitaire contre agrégat, population déclarée
3. Conversion de base, jamais implicite
4. Rente contre rendement, jamais cumulés
5. Homonymes, deux origines nommées
6. Renvois, traversés avant tout verdict
7. Statut d'ancre, manuscrit contre classeur

8. Corps du manuscrit contre ses notes de fin
9. Gain contre son miroir, perte contre sa raccroche

Le septième a été ajouté le 20260819. C'est celui qui corrige la cause des trois
premières erreurs. Le sixième, correctement traversé, aurait évité la quatrième.

Les huitième et neuvième ont été ajoutés le 20260820. Le huitième corrige
l'omission du balayage des notes. Le neuvième rend `RT-2` et `RT-3` exécutables :
tant qu'ils étaient des intentions, rien ne les vérifiait.
