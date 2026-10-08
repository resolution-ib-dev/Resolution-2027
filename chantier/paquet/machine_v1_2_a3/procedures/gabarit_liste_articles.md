# Gabarit « liste des articles » — texte et rendu PDF

*Arrêté le 20261001 sur le PLF 2027, puis repris quatre fois le même jour sur le
PLFSS 2027 — lisibilité du rendu, entame des lignes, retrait des disclaimers et
relevé des pièges, ordre du chapeau. **Ce document fait foi** pour toute liste
d'articles d'un texte financier. Il se lit avec votre charte visuelle, dont
il applique la langue « fiche » : la fiche démontre, elle n'annonce pas.*

---

## 1. Le texte — `livrables/<TEXTE><ANNÉE>_liste.md`

Ordre du texte, une ligne par article, jamais par mesure.

### 1.1 L'ordre, arrêté

1. **`## En bref`** — **deux paragraphes courts, pas davantage.** Le premier porte
   les agrégats du véhicule et ce qu'ils cachent ; le second dit ce que le texte
   fait et ce qu'il ne fait pas, **sans un chiffre d'agrégat**.
2. **Le tableau `qui` · `ce qui change pour lui` · `où`** — une ligne par population
   touchée, douze à quinze lignes, rangées par poids et non par ordre du texte. La
   colonne `où` porte une espace insécable (`art.&nbsp;35`), sans quoi elle se coupe.
3. **`## Les grandeurs`** — ce que le premier paragraphe n'a pas pris : dette,
   trésorerie, agrégats de périmètre large étiquetés comme ne mesurant pas le texte
   lu, écart à la loi de programmation.
4. **`## Trois chiffres à ne pas confondre avec ceux qui circuleront`**, trois lignes.
5. Les deux partitions et les articles.
6. **`## Comment lire cette liste`, à la fin du document** — la forme d'une ligne et
   la légende des poids. *C'est un appareil de lecture : il ne se lit qu'une fois et
   ne doit pas retarder l'entrée dans le texte.*

### 1.2 Pas de disclaimers, pas de section « pièges »

**Ne s'écrivent pas** : la ligne de provenance des montants, le paragraphe de
périmètre du véhicule, l'avertissement général sur les dates, la règle du
référentiel en paragraphe, la note de clôture. *Ils protégeaient le rédacteur, pas
le lecteur.* Ce qu'ils portaient d'utile se dit **à la ligne de l'article
concerné** : la date là où elle vide la mesure, le renvoi à l'autre véhicule là où
il manque une jambe, la source là où deux sources divergent.

**Et les pièges ne font pas une section à part.** *Consigne : ils font
partie de l'analyse, ce n'est pas un bonus.* Une liste qui range ses trouvailles
dans un encadré laisse croire que le reste n'analyse rien. **Chaque piège se dit à
la ligne de l'article qui le porte**, dans la remarque en italique.

### 1.3 Le relevé des pièges — un balayage, et il est dû

**Avant d'écrire une ligne**, chercher sur l'ensemble des articles :
`par dérogation`, `nonobstant`, `sans préjudice`, `sont validées`, `est abrogé`,
`ratifi`, `pénalité`, `sanction`, `ordonnance`, `à compter du 1er janvier <N−1>` —
et **lire chaque occurrence**. *Coût : une minute. Rendement mesuré au PLFSS 2027 :
six pièges qu'aucune passe précédente n'avait vus, dont une dérogation expresse au
secret médical sous un article intitulé « renforcer la coordination ».*

**Le relevé des mots de portée et des entrées en vigueur ne suffit pas** : il trouve
ce qui est flou, pas ce qui est caché.

### 1.4 L'entame d'une ligne — ce que l'article fait à quelqu'un

**Forme :** `- **<numéro> <poids>** <verbe direct> … *<ce que le texte ne dit pas,
en italique>.*`

- **Une ligne s'ouvre sur ce que l'article fait à quelqu'un** — qui paie, qui
  obtient, qui renonce —, jamais sur la nomenclature de l'objet.
- **Un terme technique ne s'emploie que si aucun mot courant ne dit la même chose**,
  et jamais en entame.
- **Verbe direct**, jamais « vise à », « a pour objet de », « procède à ».
- **Les grandeurs en gras**, et seulement elles. **L'italique dit ce que le texte ne
  dit pas.**
- **Jamais plus de quatre lignes.** Test : lue seule, la ligne apprend quelque chose
  à quelqu'un qui n'a pas le texte sous les yeux.

**Le numéro tient dans 7,5 mm** : l'article liminaire se note `lim.`, sans quoi la
césure sort « limi‐naire ».

**Le poids suit l'effet sur les personnes, pas le volume du dispositif.** Un article
court qui touche une situation individuelle — le secret médical, le reste à charge,
une obligation d'exercice — est `●●●`, quel que soit son nombre de mesures.

| | |
|---|---|
| `●●●` | pèse sur l'équilibre d'ensemble ou sur une situation individuelle |
| `●●` | effet réel, sectoriel ou technique lourd |
| `●` | technique, ajustement ou reconduction |
| `○` | écriture entre administrations publiques ou entre branches, sans effet propre pour celui qui paie |

**Deux partitions obligatoires** : `# Première partie — les recettes` et `# Seconde
partie — dépenses, emplois, dispositions permanentes`, sous-ensembles en `##`.
*Côté loi de financement : `# Première partie — recettes, trésorerie et équilibre`
et `# Seconde partie — les dépenses pour <année>`.*

### 1.5 Quatre règles de fond

- **Juger sur pièce, jamais sur le cadrage du Gouvernement.**
- **Ne pas prendre pour un manque ce qui est hors champ.** L'absence d'un montant ne
  se signale que là où elle détonne.
- **Les montants sont ceux de l'exposé des motifs, sauf mention.** Un écart entre
  deux sources se relève, il ne s'arbitre pas.
- **Réduire les ressources des collectivités n'est pas une écriture.** *Côté loi de
  financement, l'exception vaut pour les transferts vers les complémentaires et vers
  les départements : ils finissent dans une cotisation ou dans un impôt local.*

**L'annexe jointe est de la pièce, pas du commentaire.** Elle porte des économies et
des trajectoires que les articles ne portent pas. Ce qu'elle chiffre **sans qu'aucun
article ne le vote** se signale à la ligne de l'article qui en recueille l'effet.

---

## 2. Le rendu PDF

**Note classique, pas une plaquette.**

- **Une seule famille, un Times.** `TeX Gyre Termes`, repli `Liberation Serif` puis
  `Times New Roman`. Archivo et Source Serif 4 ne sont pas à l'atelier et Google
  Fonts est bloqué par le mandataire.
- **Titres en gras bas de casse, sous-titres en italique gras.** Pas de capitales
  espacées, pas d'intertitre coloré, pas de condensé.
- **Corps 10 pt, interligne 1,34, justifié, césure française** (`lang="fr"`).
  A4, marges **24**/22/18/22 mm — la marge haute porte le filet.
- **Le filet tricolore est en tête de CHAQUE page**, porté par la boîte de marge
  `@top-center` : `content: ""`, 166 mm sur 2 px, dégradé en image de fond, marge
  basse de 4 mm. *Le `div.filet` du flux est neutralisé par `display: none` et non
  supprimé, pour que les listes déjà écrites rendent sans retouche.*
- **Colonne de gauche à trois cases** : **numéro** en gras tabulaire, **puis
  pastilles**, puis le texte. *L'ordre compte.* Numéro
  7,5 mm à droite, pastilles 6 mm, retrait pendant 13 mm.
- **Espaces insécables** sur les milliers, avant `€`, `%`, `Md`, `points`, `ETPT`,
  et dans les guillemets. **U+00A0, pas U+202F.**
- `break-inside: avoid` sur chaque article.

**Les quatre règles de lisibilité.**

- **La remarque en italique sort en 9,2 pt, gris `#3a3a3a`** — le lecteur pressé lit
  les faits en noir. *Exempter titres et sous-titre : `h2 em, .sous em { font-size:
  inherit }`.*
- **Les articles sont séparés de 2,8 mm.**
- **Pastilles décodables** : 4,2 px espacés de 1,8 px, `#111` / `#6b6b6b` /
  `#8c8c8c`, cercle vide bordé `#555` de 3,4 px pour `○`.
- **Le texte entre accents graves reste dans la famille** :
  `code, tt, kbd, samp { font-family: inherit; font-style: italic }`.

**Deux réglages de confort** : `hyphenate-limit-chars: 6 3 3`, `orphans: 2;
widows: 2`.

**Piège mesuré :** `text-indent` négatif est hérité par les boîtes `inline-block` de
la colonne de gauche. `.art, .poids { text-indent: 0; }` est obligatoire.

**Faux défaut, à ne pas corriger :** au rendu en image, `Md€` paraît collé au mot
suivant. L'espace est là — le contrôle s'extrait du PDF, il ne se juge pas à l'œil.

**Contrôle de rendu, en une ligne.** Rejouer la substitution du script sur le
markdown et compter les `<span class="art">` : leur nombre doit égaler le nombre
d'articles, et **aucun `<li>` ne doit sortir sans**. *Mesuré au PLFSS 2027 : 49 sur
49, zéro `<li>` nu.*

**Compter sept pages, pas cinq** sur un texte de cinquante articles. C'est le prix
de la lisibilité, payé une fois pour tous les millésimes.

---

## 3. L'outil

`rendre_liste_pdf.py` — Python, `markdown` + `weasyprint`
(`pip install markdown weasyprint --break-system-packages`) :

```
python3 rendre_liste_pdf.py PLFSS2027_liste.md \
  "PLFSS 2027 — les N articles" \
  "Projet de loi de financement de la sécurité sociale pour 2027, déposé le <date>."
```

Il n'est pas de l'appareil : c'est un outil de rendu, il vit à côté des procédures et se
recopie. Toute évolution du gabarit se porte **ici**, dans ce document, et dans le
script — jamais dans un troisième endroit.

**Le PDF ne se conserve pas** : il porte des octets nuls. Il se rend à
l'utilisateur, et il se régénère depuis le markdown.
