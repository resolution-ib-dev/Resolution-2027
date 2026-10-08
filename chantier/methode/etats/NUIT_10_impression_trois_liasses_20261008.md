# NUIT 10 — impression des trois liasses et de la proposition de loi ordinaire, 20261008

**Porteur** : fil Cowork d'impression du dépôt 2027.
**Mandat** : l'auteure, 20261008 — « exporter en docx les trois liasses et la proposition de loi
ordinaire », go explicite.
**Appui** : skill `anthropic-skills:impression-docx` · skill `anthropic-skills:resolution-chantier` ·
`methode/procedure_nuit_20261008.md`, § 3 — gabarit · `methode/etats/NUIT_9_tri_trois_liasses_20261008.md` ·
`methode/etats/NUIT_8_impression_20261008.md` — précédent tirage.
**Mesure d'entrée** : 5 sources, 0 retouchée · 83 amendements, 60 rangs, 90 `\newpage` attendus ·
0 police Garamond dans l'atelier.

---

## Cinq invariants d'en-tête

1. **Aucun source n'est retouché.** Les cinq fichiers markdown sont pris par copie d'octets depuis
   le paquet de la phase 9 et vérifiés identiques au coffre. **0 octet écrit sur un source.**
2. **Un amendement par page.** Chaque `\newpage` du source produit un saut réel, et un seul.
   **90 sauts attendus, 90 obtenus**, documents confondus.
3. **Les comptes tiennent.** 33 / 31, 40 / 19, 10 / 10, **somme 83 amendements et 60 rangs**.
4. **Aucun caractère de texte n'est perdu.** Écart source / docx entièrement expliqué par les
   balises markdown non imprimées et par la colonne de pages ajoutée à la table des matières.
   **0 écart de texte sur les cinq documents**, la seule exception étant une balise HTML du source.
5. **Un défaut révélé par le rendu s'inscrit et ne se corrige pas.** Six défauts de source sont
   inscrits au § 6 ; aucun n’est corrigé.

---

## Mesure de sortie — le mandat repris point par point

### 1. Les cinq documents produits

| # | fichier | pages | source |
|---|---|---|---|
| 1 | `Liasse_PLF2027_P1_20261008.docx` | **76** | `livrables/depot_2027/LIASSE_P1_20261008.md` |
| 2 | `Liasse_PLF2027_P2_20261008.docx` | **77** | `livrables/depot_2027/LIASSE_P2_20261008.md` |
| 3 | `Liasse_PLFSS2027_20261008.docx` | **21** | `livrables/depot_2027/LIASSE_PLFSS_20261008.md` |
| 4 | `PPL_cession_participations_20261008.docx` | **3** | `livrables/depot_2027/PPL_CESSION_PARTICIPATIONS_20261008.md` |
| 5 | `LISEZ-MOI_depot_2027_20261008.docx` | **13** | `livrables/depot_2027/LISEZ-MOI_20261008.md` |

**190 pages en tout.** Chacun porte son PDF de contrôle de même nom. Tous sous
`/mnt/user-data/outputs/`. **Le LISEZ-MOI est un document séparé** : il n'est réimprimé en tête
d'aucune liasse, chacune portant son encart d'une page qui y renvoie.

### 2. Contrôle 1 — sauts de page

| document | `\newpage` au source | sauts au docx | verdict |
|---|---|---|---|
| P1 | 35 | **35** | **conforme** |
| P2 | 42 | **42** | **conforme** |
| PLFSS | 12 | **12** | **conforme** |
| PPL | 1 | **1** | **conforme** |
| LISEZ-MOI | 0 | **0** | **conforme** |

**Arbitrage inscrit.** Le saut est porté par `pageBreakBefore` sur le bloc qui suit, et non par un
paragraphe de saut autonome. Le premier essai, qui employait un paragraphe autonome, produisait
**six pages blanches** — P1 aux pages 20, 24, 28 et 33, P2 aux pages 61 et 64 — chaque fois que la
page précédente se terminait pleine. **Le saut porté sur le bloc suivant les supprime toutes six
sans déplacer une ligne de texte** : P1 passe de 80 à 76 pages, P2 de 79 à 77.

### 3. Contrôle 2 — amendements et rangs

| colonne | amendements attendus | obtenus | rangs attendus | obtenus | verdict |
|---|---|---|---|---|---|
| P1 | 33 | **33** | 31 | **31** | **conforme** |
| P2 | 40 | **40** | 19 | **19** | **conforme** |
| PLFSS | 10 | **10** | 10 | **10** | **conforme** |
| **somme** | **83** | **83** | **60** | **60** | **conforme** |

**Les identifiants dérivés se reportent tels quels**, en tête de page et à la table : `P1-30 a` et
`P1-30 b`, `P1-32 a` et `P1-32 b` ; `P2-01 a` et `b`, `P2-02 a` à `c`, `P2-03 a` à `c`,
`P2-04 a` à `c`, **`P2-05 a` à `m`**, `P2-19 a` à `c`. **31 identifiants dérivés, 31 reportés.**

**Mesure au rendu, et non au source** : **0 rang absent du PDF**, et **0 rang qui ne soit pas la
première ligne de sa page** — les 83 amendements commencent en tête de page, aucun n'est coupé
sans saut voulu.

### 4. Contrôle 3 — rendu PDF

| point | P1 | P2 | PLFSS | PPL | LISEZ-MOI |
|---|---|---|---|---|---|
| page blanche | **0** | **0** | **0** | **0** | **0** |
| amendement coupé sans saut voulu | **0** | **0** | **0** | — | — |
| table des matières présente | **oui** | **oui** | **oui** | sans objet | sans objet |
| table paginée | **33 lignes, 33 pages résolues** | **40 / 40** | **10 / 10** | — | — |
| renvois recoupés | **oui** | **oui** | **oui** | — | — |
| caractères typographiques intacts | **oui** | **oui** | **oui** | **oui** | **oui** |

**La pagination de la table est un champ `PAGEREF`**, un par amendement, ancré sur un signet posé
au titre. Les champs sont résolus au rendu : **83 signets, 83 champs, 83 numéros**. La table porte
les quatre colonnes dues — **rang, titre, accroche au texte déposé, page**.

**Caractères typographiques, source contre docx, compte exact** :

| document | insécables | apostrophes | guillemets ouvrants | fermants | cadratins |
|---|---|---|---|---|---|
| P1 | 1 277 / **1 277** | 1 949 / **1 949** | 345 / **345** | 270 / **270** | 94 / **94** |
| P2 | 897 / **897** | 1 136 / **1 136** | 166 / **166** | 155 / **155** | 119 / **119** |
| PLFSS | 206 / **206** | 425 / **425** | 46 / **46** | 38 / **38** | 47 / **47** |
| PPL | 0 / **0** | 40 / **40** | 0 / **0** | 0 / **0** | 11 / **11** |
| LISEZ-MOI | 0 / **0** | 184 / **184** | 26 / **26** | 26 / **26** | 89 / **89** |

**Aucun insécable et aucune apostrophe typographique ne sont cassés à la conversion.** C'était le
risque principal nommé au mandat ; il est mesuré et il est nul. `pdftotext` normalise l'insécable
en espace ordinaire à l'extraction : le compte se prend sur le docx, qui est le livrable.

### 5. Contrôle 4 — écart de caractères et sa cause

| document | caractères source | caractères docx | écart | cause, intégralement |
|---|---|---|---|---|
| P1 | 153 163 | 153 131 | **−32** | 36 balises `#`/`##` non imprimées (−68) ; colonne de pages ajoutée : en-tête « page » et 33 valeurs (+36) |
| P2 | 90 086 | 90 047 | **−39** | 43 balises (−83) ; colonne de pages (+44) |
| PLFSS | 35 085 | 35 073 | **−12** | 13 balises et 1 filet `---` (−29) ; colonne de pages (+17) |
| PPL | 3 866 | 3 845 | **−21** | 6 balises et 2 filets `---` (−21) ; pas de table des matières |
| LISEZ-MOI | 21 082 | 21 020 | **−62** | 20 balises et 8 filets `---` (−62) |

**0 écart de texte** sur les cinq documents, hors le seul cas du § 6 ci-dessous. L'écart est donc
**entièrement imputé à la syntaxe markdown non imprimée et à la colonne de pages due au mandat** :
aucun mot, aucun chiffre, aucune référence n'est perdu ni ajouté.

### 6. Les défauts de source, inscrits et non corrigés

1. **Le LISEZ-MOI renvoie à la liasse d'avant le tri.** Il dit se lire avant
   `livrables/depot_2027/LIASSE_20261008.md`, document unique que la phase 9 a scindé en trois.
   **Le renvoi ne résout plus sur le paquet de ce tirage.**
2. **Le LISEZ-MOI porte les comptes de page de la liasse unique** — « 90 pages en tout, 89 sauts de
   page ». **Les trois liasses du présent tirage en font 174, et la proposition de loi 3.** Le
   compte du LISEZ-MOI n'est pas faux : il mesure un autre document.
3. **Le LISEZ-MOI porte une balise HTML brute**, `I<sup>er</sup>` à la question 1B-1. **Elle
   s'imprime littéralement**, le markdown ne la traitant pas. C'est le seul écart de texte mesuré
   des cinq documents.
4. **P1-04 et P1-31 portent « NE PAS DÉPOSER EN L'ÉTAT »**, P1-31 n'est pas chiffré au rang, et
   **P1-20** porte la même mention avec l'objection de droit de l'Union. La mention vit au registre
   et à la pièce ; **la liasse ne la reprend pas**, conformément au § 7 du LISEZ-MOI.
5. **Les tableaux d'état B de P2-01 et de P2-02 portent des zéros.** Le rendu les imprime tels
   quels — colonnes AE +, AE −, CP +, CP −. C'est la réserve n° 1 du § 8 du LISEZ-MOI, et elle est
   désormais **visible à l'œil sur les dix pages 3 à 12 du tirage P2**.
6. **Les 396 rangs d'abrogation du III de P1-31 restent énumérés un à un** et occupent, à eux
   seuls, **douze pages — 46 à 57 du tirage P1**. Réserve du § 2 du LISEZ-MOI, non défaut.

### 7. Ce que le rendu ajoute, et c'est de l'atelier et non du source

**La police Garamond n'est pas installée dans l'atelier**, et le réseau de polices n'y est pas
atteignable — `curl` sur Google Fonts rend un 403 du mandataire. **Les cinq docx portent bien
`Garamond` comme police de corps** : ouverts sous Word, ils s'afficheront en Garamond.
**Les PDF de contrôle, eux, sont rendus avec la substitution de LibreOffice** — TeX Gyre Termes,
clone de Times. Conséquence tenue : **les PDF joints valent contrôle de structure, de pagination
et de caractères, non contrôle de fonte.** Les petites capitales sont rendues, la justification
et les retraits aussi.

**Une ligne de la proposition de loi s'étire à la justification** — « Domicile au paquet — » page 1,
le chemin de fichier en chasse fixe qui la suit ne se coupant pas. Cosmétique, une occurrence,
non corrigée.

### 8. Le mandat, point par point

| point du mandat | verdict |
|---|---|
| skill `impression-docx` activée avant écriture | **joué** |
| skill `resolution-chantier` activée | **joué** |
| sources lues au coffre et vérifiées identiques | **joué** — P1 et le LISEZ-MOI confrontés octet à octet au rendu du coffre ; P2, PLFSS et la proposition de loi pris au paquet de la phase 9, qui les a écrits |
| quatre documents + le cinquième, LISEZ-MOI séparé | **joué** — 5 docx, 5 PDF |
| un amendement par page, saut réel par `\newpage` | **joué** — 90 / 90 |
| rang et titre en tête de chaque amendement | **joué** — 83 / 83 en première ligne de page |
| identifiants dérivés reportés tels quels | **joué** — 31 / 31, `P2-05 a` à `m` compris |
| page de garde par liasse | **joué** — véhicule, texte visé et son numéro (PLF n° 3210, PLFSS n° 3211), compte d'amendements, date du tirage |
| encart d'une page des réserves de la colonne | **joué** — 3 / 3 |
| table des matières en fin, avec numéros de page | **joué** — champs `PAGEREF`, 83 / 83 résolus |
| rang, titre, accroche à la table | **joué** — quatre colonnes |
| Garamond, corps justifié, petites capitales, guillemets français, texte cité en retrait | **joué au docx** ; **fonte substituée au PDF de contrôle** (§ 7) |
| insécables et apostrophes typographiques non cassés | **joué** — comptes exacts, § 4 |
| contrôle des sauts, premier | **joué** — § 2 |
| contrôle des amendements et des rangs | **joué** — § 3 |
| contrôle sur le PDF | **joué** — § 4, et lecture page à page sur échantillon : pages de garde, encart, premier amendement, un amendement d'état B, les deux pages de table de P1, la proposition de loi, le LISEZ-MOI |
| écart de caractères et sa cause | **joué** — § 5 |
| aucun source retouché | **joué** — 0 écriture |
| défauts inscrits et non corrigés | **joué** — 6, § 6 |
| **non joué** | **le contrôle de fonte**, faute de Garamond dans l'atelier (§ 7). Il se joue à l'ouverture des docx sous Word, et il ne se joue pas ici. |

---

## Ce qui reste ouvert, et appelle son propre mandat

1. **Le renvoi du LISEZ-MOI à la liasse unique** et ses comptes de page — une réécriture de deux
   phrases, qui est une retouche de source et n'appartient pas à ce fil.
2. **La balise `<sup>` du LISEZ-MOI**, même régime.
3. **Les montants d'état B de P2-01 et de P2-02** — bloquant pour un dépôt réel, inscrit au § 8 du
   LISEZ-MOI, inchangé.
4. **La maquette de page de titre de la proposition de loi** — législature et commission saisie —
   reste à vérifier, comme la pièce le dit elle-même.
