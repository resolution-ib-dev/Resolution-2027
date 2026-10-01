# Classement du corpus par contenu

Validé bloc à bloc le 20260821. Remplace le rangement par nature technique —
`sources/`, `referentiels/`, `appareil/`, `archive/` — qui prenait le format pour
la substance.

**Ce document porte les règles. L'affectation vit dans la carte du projet**, qui
donne pour chaque document sa famille et son adresse réelle. Un seul lieu pour
chacune des deux choses.

---

## 1. Trois surfamilles, neuf familles

| surfamille | famille | contenu |
|---|---|---|
| **input** | `doctrine` | le manuscrit et ses annexes |
| | `extensions` | textes gelés et validés qui complètent la doctrine |
| | `références externes` | sources de confiance où la doctrine puise |
| | `références internes` | brouillons, proto-doctrine |
| **travail** | `grilles` | ce avec quoi on lit la doctrine |
| | `bac à sable` | mes travaux non relus |
| | `méthode` | les règles qu'on s'est données |
| | `outillage` | générateurs et contrôles |
| **output** | `juridique` | code formel légistique |
| | `redactionnel` | code formel des règles de forme |
| | `graphique` | code formel de la charte |

La carte se lit en haut du projet, hors famille.

**Ces onze noms sont exacts.** Ils sont la clé du champ `famille` de
`methode/index.json`, et `appareil/controle_index.py` refuse un artefact qui n'en
porte aucun. L'affectation, elle, vit dans `appareil/generer_carte.py` : la carte
la rend, l'index l'importe, personne ne la redouble.

---

## 2. Les huit règles

### R1 — Une matière de fond et le document qu'on en tire sont deux artefacts

Jamais un seul, jamais au même endroit. Trois occurrences constatées le même
jour : le texte à trois colonnes et les PPLC ; les candidats chiffrés du proto
Données et sa section « Perdants » ; l'analyse de transposabilité et le
récapitulatif externalisé. C'est ce que le rangement par nature technique
coûtait de plus cher.

### R2 — La promotion porte sur le document, pas sur la matière

Un document d'`output` monte en `input / extensions` quand il est gelé et
validé. La matière qui l'a produit reste en `travail`.

**Plan de travail qui en découle** : la Constitution à trois colonnes est la
strate maître. Une mise à jour ciblée se fait sur elle, puis on rejoue les
outputs concernés — les deux PPLC et la présentation.

### R3 — Les outputs se distinguent par leur code formel

Juridique, rédactionnel, graphique : trois métiers, trois jeux de contraintes,
trois contrôles. Critère de l'à-cheval : **si le texte se lit sans sa mise en
forme, il est rédactionnel ; si la mise en forme porte le sens, il est
graphique.** Le rendu graphique d'une note publiable est une couche, pas une
famille.

### R4 — Référence ou méthode

**Si on peut le vérifier contre une source externe, c'est une référence ; si
c'est nous qui l'avons décidé, c'est de la méthode.** Un document mixte se range
à ce qui domine, en gardant ses autorités citées à l'intérieur.

### R5 — Une référence externe entre par sa digestion

Pas par son fichier. La digestion cite ses autorités — fiche, décision, article —
et l'original reste dehors. Coût d'une digestion : une lecture, une fois. Coût de
l'original : une lecture à chaque emploi. **Une digestion sans ses autorités est
une hallucination en sursis.**

`reference/structure_ppl.md` est la digestion du guide de légistique du SGG,
augmentée de nos règles : le renvoi `guide_legistique` résout sur elle.

### R6 — Un document externalisé ne se réécrit pas

Gelé au millésime de ce qu'il disait ce jour-là. Une version neuve est un
artefact neuf.

### R7 — Ce qui n'est pas validé n'est pas de l'input

Un travail de Claude, si abouti soit-il, reste au bac à sable tant qu'il n'a pas
été relu.

### R8 — Un document ne se déplace que si sa recopie ne risque pas de le déformer

Déplacer un document du projet n'est pas un déplacement : il faut le lire
entièrement, le réécrire ailleurs, supprimer l'ancien. Le verbatim du manuscrit
ou d'un texte normatif passerait alors par le modèle, et une dérive de recopie
corrompt la strate 1 en silence.

**Conséquence** : le classement est une vue. Les adresses techniques restent, la
carte porte les familles. La règle vaut au-delà du rangement : elle interdit
aussi de reformater ou de « nettoyer » un document qui vaut par son verbatim.

---

## 3. Régime de format, et coût de la mémoire

**Ce qui se lit** — doctrine, méthode, textes, produits. Coûte à chaque ouverture.
Un PDF se lit page par page en images, un docx se déballe : un ordre de grandeur
au-dessus du même contenu en html ou en md. **Rien n'entre au projet en PDF ni en
docx.** Un document apporté reste pièce jointe, sa transcription md va au projet,
et c'est elle qui sert.

**Ce qui se décompte** — les classeurs. Ne coûte rien tant qu'on ne le lit pas.
Un xlsx s'interroge par script ; seul l'extrait chiffré sourcé se verse.

**Ce qui se fabrique** — docx, PDF, PNG. Ne se verse jamais. La source html reste,
le reste se régénère.

**Les dérivés.** Un dérivé que l'auteur lit reste au projet ; un dérivé que seule
la machine lit n'y va pas. Restent la carte et l'extrait. Sortent
`positions.json`, `notes_manuscrit.json`, `donnees.json`, l'interface,
l'inventaire, l'arbre, le relevé des notes.

**Un fil n'est pas un lieu de stockage.** Ce qui n'existe que dans une
conversation est perdu.
