# Audit — pourquoi j'ai erré, et les cinq règles qui l'empêchent

*Écrit le 20260924, sur mandat de l'auteur, après la découverte que l'énoncé
« EP3 est le corps du livre, les annexes n'y sont pas » était faux et avait
orienté plusieurs fils.*

---

## Les cinq fautes, nommées

### 1. J'ai hérité d'un énoncé de périmètre et je l'ai propagé sans le rejouer

La ligne « EP3 est le corps du livre — 180 folios — pas le livre entier : les
annexes n'y sont pas » était en mémoire projet. Je l'ai appliquée pendant
plusieurs tours sans jamais ouvrir la pièce pour la vérifier.

**Pire : ce jour-là je l'ai réinscrite au registre des arbitrages**, en recopiant
le fragment du fil du manifeste. J'ai donc renforcé l'erreur au moment même où je
consolidais le corpus. Un faux recopié dans une pièce cumulative devient très
difficile à déloger : il gagne l'autorité du registre.

*Le corpus avait déjà la règle et je l'ai violée* : garde-fou A-24 —
**« ne pas classer ni qualifier un document non ouvert »**.

### 2. J'ai fait une mesure qui ne mesurait pas ce que je prétendais, et j'ai conclu dessus

Pour établir si EP3 portait les notes, j'ai cherché la chaîne `note` dans le JSON
sérialisé. Dix-huit occurrences. J'en ai conclu, et écrit à l'auteur, que **« EP3
ne contient pas les notes »**.

La pièce range son texte sous `pages[].lignes[]`. Les notes y sont numérotées, pas
intitulées ; et j'avais interrogé une sérialisation, pas la structure. **Je
n'avais pas regardé le schéma de la pièce avant de compter dedans.** La mesure
était vide de sens, et je l'ai présentée comme un fait établi, en tableau.

Il a fallu que l'auteur me contredise pour que j'ouvre la table des matières —
qui donne, en clair : Notes 145, Annexes 163.

### 3. J'ai lu huit pièces entières pour connaître leur taille

Pour mesurer ce qui pesait lourd dans le projet, j'ai appelé `project_read` sur
huit gros documents et j'ai lu leur contenu intégral — le manuscrit, deux textes
de référence, deux trois-colonnes. **Environ 300 000 jetons pour obtenir huit
nombres.** Le coût est passé sur le compte de l'auteur, pour une information que
la seule taille du fichier rendue au retour aurait donnée.

### 4. J'ai rendu compte de l'annoncé au lieu du mesuré

Les CR que j'ai relayés reprenaient des énoncés antérieurs — « les 303 agences
sont aux annexes », « la division par dix est aux annexes » — comme des faits
constatés. Aucun des deux n'avait été mesuré. Le premier était vrai par accident,
le second était faux : le chiffre avait été retiré du livre.

### 5. J'ai posé des questions dont je pouvais trancher la réponse

« Je reporte les repères et je sors le manuscrit, ou je le garde ? » — la réponse
était dans les faits que je venais d'établir : EP3 est complet, le manuscrit a
deux épreuves de retard. Il n'y avait rien à arbitrer. J'ai renvoyé à l'auteur une
décision de tambouille, ce que ses consignes interdisent explicitement.

---

## Les cinq règles, et elles sont mécaniques

**R1 — Un énoncé de périmètre se mesure sur la pièce, jamais ne s'hérite.**
Avant d'écrire ou de relayer « X contient / ne contient pas Y », j'ouvre X et je
compte. Un énoncé de périmètre trouvé en mémoire, au registre ou dans un CR est
un **candidat à vérifier**, pas un fait. Il porte sa date de mesure, ou il n'en
est pas un.

**R2 — Une affirmation d'absence est le plus fragile des énoncés, et se re-mesure
à chaque emploi.** Prouver qu'une chose est là demande une occurrence ; prouver
qu'elle n'y est pas demande d'avoir bien cherché, partout, avec le bon motif. Les
trois énoncés faux redressés aujourd'hui étaient tous des affirmations d'absence.

**R3 — On regarde le schéma avant de compter dedans.** Sur une pièce structurée,
la première opération est de rendre ses clés et la forme d'un élément. Un compte
d'occurrences sur une sérialisation n'est pas une mesure de contenu, et ne se
présente jamais comme telle.

**R4 — On ne lit jamais une pièce entière pour connaître sa taille, son format ou
sa structure.** La taille, le nombre d'entrées, les clés se prennent sans charger
le contenu. Lire est réservé à ce qu'on doit comprendre.

**R5 — Ce qu'établissent les faits du tour ne se repose pas en question.** Si la
mesure que je viens de rendre tranche la question, je tranche et j'inscris. Une
question à l'auteur porte sur ce que lui seul sait : une intention, un
arbitrage éditorial, une priorité. Jamais sur une conséquence de mes propres
mesures.

---

## Ce que cet audit dit du dispositif, et pas seulement de moi

Le corpus portait déjà A-24 et la règle du mandat qui commence par une mesure.
**Elles n'ont pas mordu, parce qu'elles s'appliquent à ce qu'un fil produit, pas à
ce qu'un fil hérite.** Un énoncé faux entré une fois au registre a traversé cinq
fils sans qu'aucun contrôle ne le voie : aucun contrôle ne relit le registre
contre les pièces.

*Conséquence opposable, et c'est le vrai remède* : **les énoncés de périmètre du
corpus — ce que telle pièce contient, ce qu'elle ne contient pas — forment une
classe à part, et ils se rejouent.** Ils portent leur date de mesure. Un énoncé
de périmètre sans date de mesure se traite comme non mesuré.
