Forme du paquet diffusable du millésime 2027. Une décision de l'auteure, le
reste tranché par le fil chef de file sur sa direction.

## Ce que le paquet 2027 n'est pas — mesuré

**Le paquet transmis au millésime précédent n'était pas la machine.**
`livrables/paquet_machine.md`, 20260916 : `PASSATION.md`, le découpage en 71
énoncés, l'index de vérité-terrain gelé, la valise. Aucun module, aucun code,
aucun référentiel de sièges — ce rôle y était **déclaré vide par construction**,
parce que le paquet servait à mesurer un écart et qu'une adresse transmise
souffle la réponse à l'étape qui doit la trouver.

**Le paquet 2027 est un objet neuf.** Il porte la chaîne et de quoi la faire
tourner. Il ne se dérive pas du précédent, et « les mêmes améliorations avec
moins de bugs » ne décrit pas ce qu'il est.

## Ce qui part — décision de l'auteure

**Machine seule, valise retirée.** Le destinataire reçoit la chaîne et de quoi
la faire tourner sur ses propres mesures. Les arguments, les chiffres et les
principes restent au corpus. C'est le régime prévu au contrat : la valise est
séparable et optionnelle, retirée pour diffuser et gardée pour l'usage propre.

**Conséquence sur les sorties du paquet.** Toute étape tourne donc **à blanc** et
doit le déclarer — `degradation: a_blanc`, `gisements` vides. Une étape qui ne
rend rien à blanc est en faute, et le contrôle `G` la voit. Le mini-lot joint
doit être un lot qui aboutit à blanc, faute de quoi il mesure la valise et non la
machine.

## La forme — tranchée par le fil

**Un zip que le destinataire déballe, un `LISEZ-MOI.md` à la racine comme point
d'entrée unique, deux commandes.** Ferme la question 4 d'`a_trancher`, ouverte
depuis le 20260917.

*Pourquoi pas l'objet auto-déployé.* Il ajoute un point de panne chez un
destinataire dont on ne connaît ni la machine ni l'environnement, et il déplace
la faute d'installation au lieu de la supprimer. Le zip la supprime en la
documentant.

**Contenu, et rien d'autre :**

| | |
|---|---|
| `LISEZ-MOI.md` | point d'entrée unique : ce que c'est, le prérequis, l'installation en une commande, le mini-lot en une commande, la sortie attendue, les écarts connus avec leur cause, le numéro de version et la date des trois passes |
| `appareil/` | les cinq modules du millésime |
| racine | `droit.py`, `extraire_legi.py`, `codes.json` — l'accès au droit |
| `referentiels/` | les six référentiels du millésime |
| `mini-lot/` | un énoncé de bout en bout et sa sortie attendue, pour que le destinataire vérifie son installation sans rien demander |

**Ne part pas** : le corpus, la doctrine, les documents de travail, la valise, et
tout ce qui nomme un déposant, un projet ou un référentiel interne. Le contrôle
`G` le vérifie avant départ.

**Le `LISEZ-MOI.md` porte la procédure d'installation en toutes lettres.** C'est
la faute que l'épreuve à froid avait attrapée au millésime précédent, et elle ne
se répète pas : tout ce que le fil d'épreuve doit demander, deviner ou chercher
ailleurs est un défaut du paquet.

## Deux corrections dues au document de contrôle

`methode/controle_avant_transmission.md` est calibré sur **quatre modules et
quatre référentiels** ; le millésime 2027 en porte **cinq et six**. La passe 1 se
rejoue sur ce périmètre, et le document se corrige au fil qui monte le paquet.

**La passe 1 n'est pas jouable tant que `redaction_2027.py` n'est pas au
dépôt** — mesuré absent le 20261002. Elle exige une reproduction depuis un clone
nu : un module qui n'y est pas rend la reproduction impossible, et la mettre de
côté « parce qu'on sait qu'il marche » serait la passe partielle que le document
interdit.
