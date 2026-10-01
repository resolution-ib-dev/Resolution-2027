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
