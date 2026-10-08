# NUIT 8 — impression docx de la liasse déposable, dépôt 2027 — 20261008

**Porteur** : fil Cowork d'impression, **phase 8 de la procédure de nuit**, dépôt 2027. Phase seule. **Matière unique : l'export. Aucun texte n'est retouché, aucune pièce n'est écrite.**
**Mandat** : l'auteure, 20261008 — « exporte en docx en l'état, la liasse au propre ». Gabarit : `methode/procedure_nuit_20261008.md`, § 3. Le LISEZ-MOI s'imprime en tête, avant la première page de garde ; la table des matières reçoit les numéros de page que le markdown n'a pas.
**Domicile** : `methode/etats/NUIT_8_impression_20261008.md`.
**Appui** : skill `impression-docx` — **elle fait foi sur la forme** · skill `resolution-chantier` · `livrables/depot_2027/LIASSE_20261008.md` (source, non retouchée) · `livrables/depot_2027/LISEZ-MOI_20261008.md` (source, non retouchée) · `methode/etats/NUIT_7_exposes_appliques_20261008.md`, § 5.2 · `methode/etats/NUIT_5_6_liasse_20261008.md` · `methode/procedure_nuit_20261008.md`, § 3 · `methode/appui_des_passes.md`.
**Mesure** : **186 pages au docx — 14 de LISEZ-MOI, 172 de liasse, contre 90 attendues** · **90 sauts de page réels — 89 pour les 89 `\newpage` de la liasse, 1 pour la césure LISEZ-MOI / liasse** · **83 amendements rendus sur 83, 60 rangs sur 60, 0 rang vacant** · **écart de caractères +12, et il est entièrement expliqué** · **table des matières paginée, 83 lignes, 83 renvois recoupés exacts sur 83** · **0 page blanche, 0 en-tête orphelin, 0 amendement partageant sa page** · **2 défauts du source inscrits, 0 corrigé** · **2 questions fermées**.

---

## 0. Ce que ce fil a fait, et ce qu'il n'a pas fait

**Fait** : l'écriture du générateur, l'export docx, le rendu PDF, le contrôle mécanique des comptes, le contrôle du rendu page par page sur images, l'invariant de caractères, et le présent état.

**Non fait, et c'est le mandat.** Aucun texte n'est réécrit, aucun exposé corrigé, aucune question tranchée sur le fond, aucune pièce du paquet touchée, aucun registre modifié. Les deux défauts du source que le rendu révèle sont **inscrits au § 6 et non corrigés**.

**Écart assumé sur le nommage.** Le § 5 de la skill `impression-docx` prescrit un nom daté, là où la règle de résolution des renvois du corpus prescrit un nom canonique sans horodatage. **Le nom daté l'emporte, par mandat** : la liasse imprimée est un **tirage**, non un artefact canonique du corpus, et deux tirages du même texte doivent pouvoir coexister. Les fichiers livrés vivent sous `/mnt/user-data/outputs/` et ne sont pas versés à l'index.

---

## 1. Comment l'export est joué

**Un générateur propre au gabarit de la liasse**, dérivé de `md2docx.js` de la skill. Le générateur de la skill partitionne sur `---` et n'aurait pas tenu ce source : la liasse porte `\newpage` comme séparateur de page et `---` comme simple règle horizontale, et elle emploie `##` pour l'en-tête d'amendement et non pour une division.

| convention du source | rendu docx |
|---|---|
| `\newpage` en ligne seule | **saut de page porté par le paragraphe suivant** (`pageBreakBefore`), et non par un paragraphe de saut propre |
| `---` en ligne seule | rien — c'est une règle de séparation que le saut de page suivant redouble |
| `# Titre` | grand titre centré, petites capitales grasses |
| `## P1-04 — titre` | **rang et titre d'une ligne, centrés, petites capitales grasses, et ancre de table des matières** |
| `*accroche*` sous l'en-tête | ligne d'accroche centrée, italique |
| `AMENDEMENT` · `présenté par` · `----------` · `ARTICLE …` | cartouche centré |
| `EXPOSÉ SOMMAIRE` | intitulé de division, petites capitales |
| `**Article 1er**` | intitulé d'article, **petites capitales**, ordinal en exposé |
| ligne ouverte par `«` | texte cité, retrait de 0,5 pouce |
| `I. — ` · `1° ` · `a) ` | subdivision, retrait de première ligne |
| bloc `\| … \|` | tableau, ligne de tête grisée, colonnes de montants alignées à droite |

Corps **Garamond 11 points**, justifié, interligne 1,15, marges 1 pouce haut et bas, 1,1 pouce gauche et droite. **Numéro de page en pied, centré** — sans lui, une table des matières paginée ne renvoie à rien.

**Le saut de page est porté par le paragraphe suivant et non par un paragraphe propre.** Ce choix n'est pas cosmétique : la première passe, qui employait un paragraphe de saut, produisait **cinq pages blanches** là où le texte s'arrêtait exactement en bas de page. Le second tirage en porte **zéro**.

**Le LISEZ-MOI est recollé avant rendu.** Son markdown est enveloppé dur à 95 colonnes, et un gras y enjambe le retour à la ligne : rendu ligne à ligne, il aurait imprimé **58 astérisques en clair** et perdu autant de passages gras. Le recollage rend les paragraphes entiers. **Il ne touche aucun caractère** : il ne fait que supprimer des retours à la ligne internes à un paragraphe. Deux parties du dispositif de la liasse sont enveloppées de la même manière — SS-02 et SS-03 — et bénéficient du même recollage. Les notes de source, ouvertes par un appel en exposant, ne se recollent jamais entre elles.

---

## 2. La table des matières, et ses numéros de page

**Elle n'est pas réécrite.** Les trois tableaux du source sont rendus tels quels, et **une quatrième colonne « page » leur est ajoutée**. Chaque cellule de cette colonne porte un **champ `PAGEREF`** renvoyant à un signet posé sur l'en-tête de l'amendement correspondant : le numéro se calcule à l'ouverture et il suit la pagination réelle, quelle que soit la machine.

| mesure | compte |
|---|---:|
| signets posés sur les en-têtes d'amendement | **83** |
| champs `PAGEREF` écrits à la table des matières | **83** |
| lignes de table des matières | **83** |
| **renvois recoupés contre la page réelle du PDF** | **83 exacts sur 83** |

**Le recoupement est mécanique** : le rang lu à la ligne de table des matières et le numéro de page qu'elle affiche sont comparés au rang et à la page de l'en-tête d'amendement de même rang dans le PDF rendu. **0 faux renvoi.**

---

## 3. Le contrôle des comptes

| contrôle | attendu | obtenu | verdict |
|---|---:|---:|---|
| **sauts de page du source** | 89 | **89** | **conforme** — plus 1 saut propre à la césure LISEZ-MOI / liasse, soit **90 au docx** |
| **chaque `\newpage` produit un saut réel** | 89 sur 89 | **89 sur 89** | **tenu** |
| **pages du docx** | **90** (liasse) | **172** (liasse) · **186** (document entier, LISEZ-MOI compris) | **NON CONFORME — voir § 4** |
| **amendements rendus** | 83 | **83** | **conforme** |
| **rangs distincts rendus** | 60 | **60** | **conforme** |
| **rangs vacants ou barrés présents** | 0 | **0** sur 6 — P1-02, P1-03, P1-12, P1-22, P1-24, P1-29 | **tenu** |
| **pages de garde de colonne** | 3 | **3** — PLF 1<sup>re</sup> partie p. 16, PLF 2<sup>e</sup> partie p. 93, PLFSS p. 160 | **conforme** |
| **table des matières en fin, avant l'annexe** | oui | **p. 180**, annexe **p. 184** | **conforme** |
| **annexe de loi ordinaire après la table des matières** | oui | **oui** | **conforme** |
| **pages blanches** | 0 | **0** | **tenu** |
| **pages portant deux amendements** | 0 | **0** | **tenu** |
| **en-têtes d'amendement orphelins en bas de page** | 0 | **0** | **tenu** |

---

## 4. Les 90 pages attendues et les 172 obtenues — ce que la mesure dit

**Le compte de 90 pages du LISEZ-MOI et de la phase 7 est un compte de pages de markdown** : 1 page de tête, 3 pages de garde, 83 pages d'amendement, 1 table des matières, 2 pages d'annexe — c'est-à-dire **le compte des blocs séparés par `\newpage`**, et non le compte de feuilles imprimées.

**À l'impression, un bloc n'occupe pas une feuille.** Un amendement porte son cartouche, son dispositif et un exposé sommaire de 200 à 350 mots : au corps prescrit, il déborde.

| mesure sur le PDF | valeur |
|---|---:|
| amendements tenant **sur une seule feuille** | **30 sur 83** |
| feuilles par amendement — **moyenne** | **1,96** |
| feuilles par amendement — **minimum** | **1** |
| feuilles par amendement — **maximum** | **18** (P1-31, clause générale, article 1<sup>er</sup> — la division porte 396 rangs) |

**La consigne « un amendement par page » est tenue dans ce qu'elle commande et ne l'est pas dans ce qu'elle compte.** Ce qu'elle commande — **aucun amendement ne partage sa feuille avec un autre, chacun ouvre sur une feuille neuve** — est **tenu, 83 sur 83, 0 exception**. Ce qu'elle compte — une feuille par amendement — **ne l'est pas, et ne peut pas l'être** : il faudrait descendre le corps sous le lisible ou retirer les exposés.

**Réserve de mesure, et elle est honnête.** **Garamond est absent du conteneur** : le docx déclare bien `Garamond`, et il s'imprimera en Garamond sur la machine de l'auteure, mais **le PDF de contrôle est rendu avec un substitut de chasse Times** (`TeX Gyre Termes`, alias posé pour ce tirage). Garamond étant d'une chasse plus étroite d'environ 8 %, **la pagination réelle en Garamond sera plus courte que les 186 feuilles mesurées ici** — de l'ordre de 170 à 175. **Aucun compte de ce § ne vaut au feuillet près ; tous les comptes des § 2, 3, 5 et 6, qui ne dépendent pas de la police, valent exactement.**

---

## 5. L'invariant de caractères

**Comparaison du texte du source et du texte extrait du docx**, balisage markdown résolu, blancs neutralisés.

| mesure | valeur |
|---|---:|
| caractères du source — LISEZ-MOI et liasse | **296 073** |
| caractères extraits du docx | **296 085** |
| **écart** | **+12** |

**La cause de l'écart est unique et elle est voulue** : les trois tableaux de la table des matières reçoivent chacun un intitulé de colonne `page`, soit **3 × 4 = 12 caractères**. **Aucun autre caractère n'est ajouté, perdu ni substitué.**

| caractère sensible | source | docx | verdict |
|---|---:|---:|---|
| **espace insécable** `U+00A0` | 2 380 | **2 380** | **intact** |
| **apostrophe typographique** `’` | 3 665 | **3 665** | **intact** |
| **guillemet français ouvrant** `«` | 576 | **576** | **intact** |
| **guillemet français fermant** `»` | 482 | **482** | **intact** |
| **tiret cadratin** `—` | 319 | **319** | **intact** |
| **tiret demi-cadratin** `–` | 361 | **361** | **intact** |
| astérisque littéral (`nuitp1_*`) | 2 | **2** | **intact** |

**Le risque principal nommé au mandat — casser les insécables et les apostrophes à la conversion — ne s'est pas réalisé.** Le contrôle est joué sur le flux de texte du docx, non sur le PDF, de sorte qu'aucune substitution de police ne le fausse.

---

## 6. Les défauts du source que le rendu révèle — inscrits, non corrigés

| # | défaut | compte | pièces |
|---|---|---:|---|
| **8-D1** | **Neuf amendements portent `AMENDEMENT` mais ni la ligne `présenté par` ni la ligne de tirets du cartouche.** Au rendu, leur cartouche est amputé de deux lignes sur quatre, là où les soixante-quatorze autres le portent entier | **9 sur 83** | **P1-07** · **P1-23** · **P1-26** · **P2-10** · **P2-11** · **SS-06** · **SS-07** · **SS-08** · **SS-09** |
| **8-D2** | **La table des matières porte des rangs en double sans que rien ne les distingue** : huit rangs y figurent deux fois ou plus, un par amendement. C'est conforme au registre — un rang peut porter plusieurs amendements — mais la ligne ne le dit pas, et un lecteur y voit une répétition | **8 rangs, 23 lignes** | P1-30, P1-32, P2-01, P2-02, P2-03, P2-04, P2-05, P2-19 |

**Ni l'un ni l'autre n'est corrigé.** 8-D1 touche le cartouche des pièces, hors mandat et hors R8. 8-D2 touche le texte de la table des matières, que le mandat interdit de retoucher.

**Ce que le rendu ne révèle pas, et c'est à dire** : aucune fuite de bloc interne, aucune mention « ne pas déposer », aucune mention « RETIRÉE DU DÉPÔT », aucun renvoi au registre des colonnes, aucune notation locale de lot n'apparaît au corps de la liasse imprimée. **Les trois identifiants `LEGIARTI` subsistent**, en notes de source d'exposé, comme les phases 5 et 7 l'avaient arbitré.

---

## 7. Questions fermées — deux

| # | question | défaut retenu | état |
|---|---|---|---|
| **8-1** | **Les 90 pages du gabarit ne sont pas atteignables à l'impression** : au corps prescrit, un amendement occupe 1,96 feuille en moyenne, et 30 sur 83 seulement tiennent sur une feuille. **Faut-il descendre le corps, élargir la page, ou tenir le corps et accepter 172 feuilles ?** | **tenir le corps et accepter le débordement.** La typographie est prescrite par le gabarit de l'auteure et par la skill ; le compte de 90 est un compte de blocs de markdown, non une contrainte de mise en page. **Ce qui commande — un amendement n'ouvre jamais sur une feuille déjà commencée — est tenu sans exception** | **tranchée au défaut, inscrite** |
| **8-2** | **Le pied de page porte un numéro de page sur toutes les feuilles, LISEZ-MOI compris.** Le gabarit ne prescrit ni pied de page ni point de départ de la numérotation. **La numérotation repart-elle à 1 sur la page de tête de la liasse ?** | **numérotation continue d'un bout à l'autre, LISEZ-MOI compris.** Sans elle, les renvois de la table des matières ne désignent rien de lisible. **Un mot suffit à la faire repartir à 1 sur la liasse** : c'est un paramètre du générateur, aucune pièce ne bouge | **tranchée au défaut, inscrite** |

---

## 8. Mesure de sortie — le mandat repris point par point, verdict par point

| point du mandat | verdict | compte |
|---|---|---|
| **exporter la liasse en docx, en l'état** | **joué** | `Liasse_depot_2027_20261008.docx`, **141 417 octets** |
| **le LISEZ-MOI s'imprime en tête, avant la première page de garde** | **tenu** | **p. 1 à 14**, page de tête de la liasse p. 15, première page de garde p. 16 |
| **un amendement par page — 89 sauts pour 90 pages, chacun produisant un saut réel** | **tenu sur les sauts, non tenu sur les pages** | **89 `\newpage` → 89 sauts réels, 89 sur 89.** **0 amendement ne partage sa feuille, 83 sur 83.** **Mais 172 feuilles de liasse et non 90** — § 4, question 8-1 |
| **chaque amendement porte son rang en tête et son titre d'une ligne** | **tenu** | **83 sur 83**, en petites capitales grasses centrées |
| **trois colonnes dans l'ordre, chacune ouverte par sa page de garde** | **tenu** | PLF 1<sup>re</sup> partie p. 16 · PLF 2<sup>e</sup> partie p. 93 · PLFSS p. 160 |
| **la proposition de loi ordinaire est en annexe, après la table des matières** | **tenu** | table des matières p. 180, annexe p. 184 |
| **la table des matières est en fin de document** | **tenu** | p. 180 à 183 |
| **lui ajouter les numéros de page** | **joué** | **83 champs `PAGEREF` sur 83 signets · 83 renvois recoupés exacts sur 83** |
| **Garamond, corps justifié, petites capitales des intitulés d'articles, guillemets français avec insécables, texte cité en retrait** | **tenu au docx** | police déclarée **Garamond 11 pt**, corps justifié, petites capitales appliquées aux intitulés d'article et aux en-têtes, retrait de 0,5 pouce sur le texte cité. **Contrôlé à l'œil sur images ; la police de rendu est un substitut** — § 4 |
| **ne pas casser les insécables et les apostrophes typographiques** | **tenu, et prouvé** | **2 380 insécables, 3 665 apostrophes, 576 + 482 guillemets, 680 tirets : comptes identiques au caractère** |
| **compter les pages du docx et les comparer aux 90 attendues** | **joué** | **186 au document, 172 à la liasse. Écart de +82 feuilles, cause nommée au § 4** |
| **compter les sauts de page et les comparer aux 89** | **joué** | **89 attendus, 89 obtenus pour la liasse**, plus 1 de césure, **90 au docx** |
| **compter les amendements au rendu — 83 attendus** | **joué** | **83** |
| **compter les rangs — 60 attendus** | **joué** | **60**, et **0 rang vacant** sur les 6 |
| **rendre le docx en PDF et contrôler le rendu sur le PDF** | **joué** | `Liasse_depot_2027_20261008.pdf`, **186 pages, 1 865 786 octets** |
| **— pas de page orpheline** | **tenu** | **0 page blanche, 0 en-tête d'amendement orphelin en bas de page** |
| **— pas d'amendement coupé entre deux pages sans saut voulu** | **tenu** | **0 feuille portant deux en-têtes d'amendement.** Un amendement long se poursuit sur la feuille suivante, ce qui est un débordement et non une coupure fautive |
| **— table des matières présente et paginée** | **tenu** | **83 lignes, 83 numéros, 83 exacts** |
| **— caractères typographiques intacts** | **tenu** | § 5 |
| **vérifier qu'aucun caractère n'a été perdu ou substitué, dire l'écart et sa cause** | **joué** | **écart +12 caractères. Cause unique : les trois intitulés de colonne `page` ajoutés à la table des matières, que le mandat prescrit. 0 caractère perdu, 0 substitué** |
| **inscrire les défauts du source sans les corriger** | **joué** | **2 défauts inscrits — 8-D1 et 8-D2 — 0 corrigé** |
| **ne retoucher ni la liasse, ni le LISEZ-MOI, ni aucune pièce** | **tenu** | **0 fichier du paquet écrit.** Les deux sources sont lues par copie d'octets et jamais réécrites |
| **écrire le docx et le PDF sous `/mnt/user-data/outputs/`, les fichiers de travail à part** | **tenu** | travail sous `/home/claude/travail/`, livrables sous `/mnt/user-data/outputs/` |
| **nom daté, malgré la règle de résolution des renvois** | **tenu, et l'écart est inscrit** | § 0 |
| **règle de nuit — aucune question fermée n'arrête le fil** | **tenue** | **2 questions, 0 arrêt, 2 inscrites** |
| **rejouer un contrôle de fond, d'adresses ou de rattachement** | **NON JOUÉ, et c'est le verdict** | hors mandat. Les quatre contrôles de la nuit sont ceux du LISEZ-MOI, § 3, joués sur **LEGI 20261001** |
| **corriger les neuf cartouches amputés de 8-D1** | **NON JOUÉ, et c'est le verdict** | hors mandat, et R8 l'interdit |
| **lever le blocage du regroupement des abrogations** | **NON JOUÉ, et c'est le verdict** | il relève du fil code de l'extracteur, qui n'est pas de la nuit — LISEZ-MOI, § 2 |

---

## 9. Ce que ce fil livre

| fichier | nature |
|---|---|
| `/mnt/user-data/outputs/Liasse_depot_2027_20261008.docx` | **le tirage** — LISEZ-MOI en tête, liasse de 83 amendements en trois colonnes, table des matières paginée, annexe de loi ordinaire. **141 417 octets** |
| `/mnt/user-data/outputs/Liasse_depot_2027_20261008.pdf` | **le PDF de contrôle**, 186 pages, rendu avec un substitut de police — **il contrôle, il ne se diffuse pas** |
| `methode/etats/NUIT_8_impression_20261008.md` | le présent état |

**Aucun autre fichier n'est écrit. Aucune pièce, aucune liasse, aucun LISEZ-MOI, aucun registre.**
