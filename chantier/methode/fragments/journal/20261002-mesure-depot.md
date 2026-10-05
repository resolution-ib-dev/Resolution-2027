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
