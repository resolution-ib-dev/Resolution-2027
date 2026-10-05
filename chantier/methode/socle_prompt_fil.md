# Socle des prompts de fil

*Ce qui vaut pour tout fil du chantier. Un prompt de fil ne le recopie pas : il
le cite en une ligne — « socle : `methode/socle_prompt_fil.md` » — et n'écrit
que ce qui lui est propre.*

## Ce que tout fil lit d'abord

`methode/index.json`, `methode/arbitrages.md`, `methode/a_trancher.md`.
Le prompt du fil nomme ce qu'il faut lire **en plus**, et rien d'autre.

## Le projet est un plan de travail, pas le miroir du coffre

*Règle posée le 20261001, corrigée le 20261001 même, après avoir fait disparaître
`methode/journal.md` — 295 275 o, 4 875 lignes. Le journal a été retrouvé et remis
à l'octet le jour même ; la règle reste corrigée, parce que la prochaine fois il
n'y aura pas de copie.*

**Le coffre porte tout. Le projet porte ce qu'un fil lit en ouverture.** Une
pièce sortie du projet n'est pas perdue **si et seulement si** elle vit ailleurs.

### Les trois conditions d'une sortie, et elles sont cumulatives

1. **La présence ailleurs est mesurée sur la pièce elle-même** — son sha256
   relevé là où elle va vivre, pas la présence d'un dossier, pas le souvenir
   d'une restauration, pas la mention d'un versement au journal. *Le journal a
   été sorti sur une présence au clone « établie par la restauration du
   20260917 ». Le dépôt ne porte aucun chemin `methode/` sur aucune de ses seize
   refs, et n'en a jamais porté.*
2. **La sortie s'inscrit à `methode/sorties_du_projet_<AAAAMMJJ>.md`** avant
   d'être jouée : où vit l'archive, son empreinte, et une ligne par pièce avec
   sa taille et son sha256. Une pièce sortie sans sa ligne est une pièce perdue
   avec un délai.
3. **Aucun fragment ne sort, jamais.** `appareil/fragments.py` régénère la queue
   d'un cumulatif depuis les fragments qu'il voit : un fragment sorti du coffre
   n'est plus vu, et sa section disparaît au prochain assemblage. Onze sections
   d'arbitrages ont été perdues ainsi entre le 20260917 et le 20260924.

### Avant tout assemblage

**Un assemblage se joue d'abord sur une copie jetable, et se compte en
sections, pas en octets.** Un cumulatif qui perd onze sections ne rétrécit que
de 9 863 o : la taille ne voit pas la faute. Si l'assemblage perd une section,
il ne se verse pas — les sections sans fragment se reprennent au-dessus de la
ligne de marque, où rien ne les réécrit.

### Déjà fait le 20261001

Les documents du projet sont archivés par copie d'octets, relecture vérifiée
pièce à pièce ; 15 documents sont sortis, 1 617 384 o — le registre des sorties
dit lesquels et où. `methode/journal.md` et `methode/arbitrages.md` sont
rebâtis, assemblage idempotent, zéro section perdue. Le journal porte son
contenu d'origine verbatim, remis par l'auteure et vérifié identique à l'octet.

### Ce qui reste dû

- **La poussée de l'archive au dépôt.** Refusée, et pas par un réglage
  manquant : remesuré deux fois, l'outil que le mandataire git réclame n'existe
  pas dans une session Cowork rattachée à un projet de chat. La voie est le
  téléversement de l'archive au dépôt par le navigateur, puis son dépliage par
  une session `claude.ai/code`. **Tant qu'elle n'a pas abouti, aucune sortie
  nouvelle ne se joue.**
- **`a_trancher` comme cible de `appareil/fragments.py`.** Le registre reçoit
  des fragments qu'aucun assemblage ne reverse.
- **Un contrôle d'assemblage** qui compte les sections avant et après et refuse
  d'écrire s'il en perd une.

Un fil qui verse une pièce volumineuse au coffre ne la verse pas au projet par
défaut : il la verse au projet seulement si un fil la lira en ouverture.

## La frontière de projet — elle se vérifie à chaque lancement

*Arbitrage de l'auteure du 20260930,
`methode/fragments/arbitrages/20260930-perimetre-fiscal.md`. Enfreinte deux fois
le jour même, dans les deux cas par une ligne de lancement de phase 1 écrite au
projet doctrine.*

- **Projet doctrine** : le découpage des mesures, les énoncés, les paramètres,
  les arguments et leur vérification.
- **Projet machine, valise branchée** : la qualification, le rattachement, le
  vecteur, la rédaction cible, l'exposé sommaire et la liasse.

**Une ligne de lancement du projet doctrine n'active donc jamais
`disposition-cible`, `redaction-legistique` ni `expose-sommaire`.** Elle peut
activer `compatibilite-doctrine` et `vecteur-mesure`.

## Ce que tout fil respecte

- **Partage du travail (A-23).** L'auteur tranche le fond et l'ordre des lots.
  Le fil tranche sa tambouille — méthode de détail, appareil, nommage, ordre
  d'exécution — et l'inscrit. Demander un feu vert sur de la tambouille est une
  faute ; trancher seul une question de fond aussi.
- **Une question de fond s'inscrit à `methode/a_trancher.md` et attend.**
- **On mesure, on ne déclare pas.** On ne part jamais d'une liste : on part du
  delta entre la liste et la mesure.
- **On modifie, on ne reconstruit pas.** Une faute coûte une correction.
- **Un contrôle annoncé est un contrôle mécanique.** Si le fil annonce une
  vérification, il la joue et rend ses nombres.
- **Un contrôle neuf porte son jeu de fautes et son jeu de justes.**
- **Une restauration est toujours une copie d'octets** (A-41, A-44).
- **Une divergence ne se corrige pas au socle** : elle dit que la grille est
  fausse, et c'est la grille qu'on reprend.
- **Une règle qu'un fil outille s'inscrit là où la règle est lue**, jamais dans
  un document neuf qui doublerait un document existant.
- **Aucun `make index` ni `make reindex` tant que la table curée n'est pas
  rattrapée** — mesure du 20260930 : le générateur rend 253 artefacts quand le
  coffre en porte plus de 310, et un rejeu en l'état détruit les cinquante-sept
  déclarations manquantes. Le rattrapage ne se fait pas depuis Cowork.
- **Les quatre garde-fous** : ne pas classer un document non ouvert ; n'inscrire
  comme validé que ce que l'auteur a dit ; pas de superlatif non vérifié ;
  annoncer le coût d'une opération avant, pas après.

## Ce que tout fil rend

1. Ses livrables, versés au coffre à leur adresse.
2. Ses contrôles, avec leurs nombres mesurés.
3. `methode/fragments/journal/<AAAAMMJJ>-<fil>.md`, et un fragment d'arbitrages
   s'il a tranché de la tambouille. **Le fragment ne porte pas son titre
   `## AAAAMMJJ — <fil>`** : `appareil/fragments.py` l'écrit. Déposer, assembler,
   reverser `journal.md` et `arbitrages.md`.
4. Son paquet de dépôt s'il a touché à de l'appareil — **un fil Cowork ne pousse
   pas** (A-393), et un fil qui écrit de l'appareil sans livrer son paquet a
   écrit pour rien (A-394).
5. Ce qu'il laisse ouvert.

**Il ne se donne pas son successeur.** Il rend son état et s'arrête.
