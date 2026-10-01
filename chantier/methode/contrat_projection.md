# CONTRAT DE PROJECTION DU CORPUS CHIFFRÉ — 20260820 v2

Contrat commun aux cinq skills qui projettent le référentiel chiffré vers un
livrable : `fiche-mesure`, `audit-conformite`, `qa-riposte`,
`compatibilite-doctrine`, `contestabilite`.

Il s'écrit ici une fois. Les trois blocs qui suivent sont repris mot pour mot
dans chacune des cinq. Toute divergence de formulation entre deux skills est un
défaut.

Référence de schéma : `REF_doctrine_20260820_v18.json`. Les décomptes portés au
présent document et aux règles de forme ont été mesurés sur ce millésime.

Ce document intègre l'additif du 20260820 relatif au référentiel des positions.

---

## Volet 1 — Ce que la skill lit du corpus

### Les trois sources

| source | unité | ce qu'elle porte |
|---|---|---|
| `REF_doctrine_AAAAMMJJ_vN.json` | l'entrée numérique | paramètres, effets, chiffrage, renvois, lacunes |
| `Positions_AAAAMMJJ_vN.json` | ancrage × position × catégorie | qui gagne, qui perd, qui captait, justification, relais |
| `Notes_manuscrit_AAAAMMJJ_vN.json` | la note de fin | hypothèses de calcul, sources, raisonnements implicites |

Les trois sont des référentiels : ils se lisent, ils ne se recopient pas. Aucune
skill ne réécrit à la main ce qu'ils portent, et aucune ne les corrige — une
correction remonte vers la strate 1.

**Le relevé des notes se consulte systématiquement.** Le manuscrit explicite en
note ce que son corps laisse implicite. Un chiffre introuvable dans le corps s'y
trouve souvent. L'omission de ce balayage le 20260820 a laissé passer le coût
d'une rupture d'accès au crédit souverain et le gain de croissance attribué à la
simplification fiscale.

### Par entrée chiffrée

Une entrée chiffrée est un `parametre -pN` ou un `effet -eN`. Elle porte douze
propriétés, qui se lisent toutes avant tout emploi.

| propriété | ce qu'elle règle |
|---|---|
| `statut_ancre` | l'origine de la valeur au corpus |
| `source_ancre` | le passage qui porte l'ancre, cité tel quel |
| `nature` | le rang d'énonciation de la valeur |
| `verdict` | le degré d'instruction de l'entrée |
| `conditions` | les conditions littérales attachées à la valeur |
| `base` | personne ou foyer · mois ou an · brut ou net · stock ou flux · population · millésime |
| `portee` | l'ensemble couvert et les exclusions, en extension |
| `sens` | égal · plancher · plafond |
| `origine` | le nœud où le chiffre est produit, une seule fois |
| `operation` | le calcul écrit qui produit la valeur |
| `chaine` | les composants et leur statut, relevé ou reconstitué |
| `exact` | la valeur non arrondie, vide quand le sens l'interdit |

Nomenclatures fermées du schéma v18, à employer telles quelles :

**`statut_ancre`** — `manuscrit` · `implicite au manuscrit` · `classeur` ·
`absent des deux`.

**`nature`** — `règle générale` · `illustration` · `agrégat` · `hypothèse`.

**`verdict`** — `POSÉ` · `RECONSTITUÉ` · `APPROCHÉ` · `NON INSTRUIT` ·
`À QUALIFIER`, et leurs formes composites, qui répartissent le degré
d'instruction entre l'agrégat et l'unitaire, ou entre l'ancre et son opération.
La forme composite se lit entière : elle vaut instruction pour un terme et
lacune pour l'autre.

Une skill qui cite un chiffre sans avoir lu son `statut_ancre` est en faute,
quelle que soit la justesse du chiffre.

### Par terme employé

Le bloc `lexique` porte neuf termes — `foyer`, `personne`, `travailleur type`,
`mission indispensable`, `restitution`, `aide fondamentale`, `économies
restituables`, `capital de restitution`, `cotisation`. Chacun porte sa
`definition`, ses `variantes`, sa `regle` de variation, ses `emplois` et son
propre `statut_ancre`.

Tout terme du lexique employé dans un livrable se prend avec sa `regle`. Une
variation lexicale est admise quand le référent est unique et que le contexte le
fixe ; elle appelle arbitrage quand elle emporte un changement de base ou de
population.

### Par règle transversale

`regles_transversales` porte `RT-1`, fongibilité des cotisations sociales, de
`statut_ancre: implicite au manuscrit`. Ce que le manuscrit démontre sans
l'énoncer se cite comme un passage, au même titre qu'une ancre écrite.

### Par proposition citée en strate normative

`complements_normatifs` porte onze mécanismes `M1` à `M11` et cinquante-neuf
effets. Chaque effet porte son `siege_constitutionnel`, le
`droit_en_vigueur_deplace`, sa `voie_basse`, son `fondement` et sa strate. La
nomenclature des strates est fermée et se lit à `nomenclature_strates`.

Une strate non figée se cite « en chantier ».

### Par position

Chaque ligne du référentiel des positions porte son **degré d'origine**, qui
commande sa diffusabilité comme `statut_ancre` commande celle d'un chiffre.
Nomenclature fermée.

| degré | origine | diffusable |
|---|---|---|
| nommé | écrit au manuscrit, corps ou note | oui |
| indiqué | écrit au classeur ou en annexe | oui, statut déclaré |
| implicite | démontré sans être énoncé, cité comme passage | oui |
| déduit | conséquence d'une entrée, tracée par sa chaîne | oui, déduction signalée |
| complété | apporté par l'inventaire | après arbitrage des auteurs |

**Le degré `complété` est le seul qui bloque une sortie externe.** Il signale ce
que la dérivation a ajouté et que les auteurs n'ont pas encore validé.

### Par catégorie

Le bloc `categories` du référentiel des positions est fermé, sur le modèle du
`lexique`. Une catégorie nomme un **ensemble de personnes**, jamais une position
et jamais une grandeur.

**La position est portée par la ligne, non par la catégorie.** La même personne
occupe des positions opposées selon la mesure : l'entreprise perd sa subvention
et gagne la suppression des impôts de production. Sans cette séparation, le solde
par personne ne serait plus calculable.

**Une grandeur n'est jamais un bénéficiaire.** « Finances publiques »,
« économie », « complexité fiscale », « sphère publique » sont des grandeurs
écrites là où une personne était attendue. Elles se requalifient.

---

## Volet 2 — Les huit règles d'émission

Identiques dans les cinq skills, reprises mot pour mot. Les cinq premières
règlent l'émission d'une grandeur, les trois suivantes celle d'un gain ou d'une
perte.

1. **Diffusabilité.** Une valeur sort quand son `statut_ancre` vaut `manuscrit`,
   `implicite au manuscrit` ou `classeur`. Le statut `absent des deux` réserve
   la valeur au registre interne du REF, en tout emploi.

2. **Déclaration du statut classeur.** Une valeur de `statut_ancre: classeur`
   sort accompagnée de sa déclaration : elle se donne comme décompte de
   classeur, distincte d'une ancre du manuscrit.

3. **Rang de l'illustration.** Une entrée de `nature: illustration` sort en
   nommant son cas. Une règle générale se prend à une entrée de `nature: règle
   générale`.

4. **Conditions littérales.** Les `conditions` attachées à l'entrée accompagnent
   la valeur partout où elle sort. Elles règlent le sens au même titre que le
   chiffre.

5. **Forme de l'ancre.** Une grandeur s'énonce dans sa forme canonique — la
   `valeur` d'un paramètre, le `chiffre` d'un effet — et cette forme s'écrit sans
   virgule. Trois voies dans l'ordre : arrondir à l'entier, changer d'unité, puis
   la décimale par exception justifiée à l'entrée. Le rang suit le registre : un
   constat se dit précis, à trois chiffres significatifs ou entier, parce que le
   décompte est la démonstration ; une promesse se dit en ordre de grandeur, à un
   ou deux chiffres, parce que l'engagement se tient à la portée de ce qui est
   démontré. L'`exact` vient en appui, à la relance et dans l'appareil. Une autre
   forme se déclare au référentiel avant emploi. Arrondis et approximations se
   règlent par `Regles_forme_canonique_20260820_v2.md`.

6. **Un gain sort avec son miroir.** Tout gain porté par le projet a une perte en
   miroir, et cette perte se nomme. Un gain d'efficacité n'y échappe pas : il
   supprime une rente, et le capteur de cette rente est le perdant. Un gain dont
   aucun capteur ne se nomme est à requalifier, non à publier.

7. **Une perte sort avec sa raccroche.** Trois valeurs, exclusives — renvoi vers
   une ligne de gain quand le perdant accède à une contrepartie nommée du projet,
   reconstitution volontaire du flux quand le flux public supprimé peut se
   reconstituer en flux privé équivalent, absence assumée quand ni l'un ni
   l'autre. La troisième se dit au même titre que les deux autres. Une perte
   présentée sans sa raccroche est un livrable incomplet, pas un livrable
   prudent.

8. **Un chiffre de note se cite, il ne se recopie pas.** Un chiffre publié qui
   vient d'une note de fin porte l'identifiant de cette note. Le texte de la note
   reste au relevé. Recopier une note dans un référentiel ou un livrable crée un
   cache que personne ne rafraîchit.

---

## Volet 3 — La passe de contrôle à la sortie

Le contrôle structurel vérifie le référentiel. Le contrôle arithmétique vérifie
ses bouclages. Ni l'un ni l'autre ne vérifie ce qui sort d'une skill. C'est
l'objet de cette passe.

**Forme arrêtée : un script, `controle_sortie.py`, appelé par les cinq skills.**

Motif de la forme. Les cinq skills partagent déjà une échelle de gravité — trois
rangs chez `fiche-mesure`, `qa-riposte` et `audit-conformite`, quatre contrôles
ordonnés chez `compatibilite-doctrine`, aucun chez `contestabilite`. Une section
de prose supplémentaire s'ajouterait à un appareil déjà inégal et resterait
déclarative. Une sixième skill dépendrait de son déclenchement. Un script
s'exécute, rend le même verdict à chaque passage, et se régénère avec le REF :
un dérivé se régénère, il ne se corrige jamais à la main.

**Ce que le script fait.** Il relève toute grandeur du livrable produit, la
rapproche des entrées du REF, et rend par chiffre : l'entrée trouvée, son
`statut_ancre`, sa `nature`, son `verdict`, et l'état des cinq règles
d'émission. Il rend en outre les grandeurs qu'aucune entrée ne porte.

Le champ du contrôle est celui des grandeurs : une valeur y entre quand elle
porte une unité du corpus — monétaire, taux, ou population arrêtée — et qu'elle
ne s'écrit pas comme un millésime. Les autres nombres d'un livrable sont des
dates, des références et des identifiants, et relèvent du contrôle des sources.

**Deux régimes, selon l'origine du chiffre.**

*Contrôle interne* — les chiffres que la skill affirme depuis le REF. Ils se
contrôlent tous : entrée retrouvée, statut lu, cinq règles tenues.

*Compatibilité externe* — les chiffres venus du dehors : proposition soumise à
instruction, donnée d'un tiers, valeur avancée par un contradicteur. Ils
s'instruisent. Un chiffre que le référentiel ne porte pas est un ancrage à
créer, non une faute.

Cette distinction est celle qui sépare les deux sens de la chaîne. Une skill qui
projette la doctrine vers l'aval opère en contrôle interne. Une skill qui
instruit une idée venue du dehors opère en compatibilité externe sur ce qu'elle
reçoit, et en contrôle interne sur ce qu'elle oppose.

**Ce qui relève du contrôle interne.** Trois formes, toutes tracées au corpus.

*L'entrée* — un `parametre -pN` ou un `effet -eN`, avec ses douze propriétés.

*Le composant de chaîne* — un sous-chiffre nommé dans la `chaine` d'une entrée,
avec son statut relevé ou reconstitué et son origine, laquelle peut être une
cellule de classeur. La règle 2 s'y applique, la règle 5 non : un composant
n'est pas une ancre.

*Le dérivé* — un chiffre reconstructible depuis le référentiel par une opération
nommable. Il est régulier, et se verse au REF avec son opération et sa chaîne.
Ce qui est proscrit est la dérivation muette, non la dérivation.

**L'arrondi de communication.** Une ancre s'écrit arrondie. Le rapprochement
admet donc un écart d'un millième, et rend l'entrée approchée plutôt que de
reconstruire la valeur par une opération fortuite.

**Ce qu'il rend.** Quatre niveaux. Les deux premiers seuls commandent une suite.

| niveau | cas | suite |
|---|---|---|
| ÉCHEC | contrôle interne, une règle d'émission franchie | le livrable ne sort pas |
| À INSTRUIRE | aucune entrée, aucun composant, aucune dérivation | ancrage à créer |
| RÉALISTE | reconstructible depuis le référentiel | à verser au REF, bas de page |
| TENU | entrée ou composant retrouvé, cinq règles tenues | bas de page |

Le rapport tient en une ligne de tête et deux blocs : échecs, puis chiffres à
instruire. Le reste vit en bas de page et ne perturbe pas la lecture.

**Ce que la passe ne fait pas.** Elle établit qu'un chiffre est tenu par le
corpus, non qu'il est juste. Un chiffre faux mais reconstructible ressort
réaliste. La confrontation à l'ancre du manuscrit relève d'`audit-conformite`,
contrôle 2, et la vérification des bouclages de `controle_arithmetique.py`.
Trois contrôles distincts, qui ne se remplacent pas.

**Régime par skill.**

| skill | sens | régime dominant |
|---|---|---|
| `fiche-mesure` | projection vers l'aval | contrôle interne sur la totalité |
| `audit-conformite` | projection vers l'aval | interne sur le corpus, externe sur les sources tierces |
| `qa-riposte` | projection vers l'aval | interne sur la riposte, externe sur le chiffre adverse repris |
| `compatibilite-doctrine` | instruction depuis le dehors | externe sur X, interne sur ce que la skill oppose |
| `contestabilite` | instruction depuis le dehors | externe sur la donnée adverse, interne sur la cible |

**Quand il s'exécute.** En dernière opération de la skill, sur le livrable
produit, avant toute remise. Une skill qui rend un livrable sans cette passe
rend un livrable non contrôlé, et le dit.

**Sur les formats que le script ne lit pas** — docx, xlsx, pdf, png — les
contrôles se conduisent à la lecture, et le rapport le mentionne en tête.

**Contrôles de position et de note.** Cinq règles s'ajoutent aux quatre niveaux
ci-dessus, opposables à tout livrable qui nomme un gain ou une perte.

| règle | ce qu'elle empêche |
|---|---|
| P1 | un gain sans miroir nommé |
| P2 | une perte sans raccroche, parmi les trois valeurs admises |
| P3 | une perte sans justification, ou une perte raccrochée sans relais |
| N1 | une citation de note sans note correspondante au relevé |
| N2 | une note chiffrée qu'aucun référentiel ne cite |

P1 à P3 tournent à la génération de l'inventaire. N1 et N2 tournent par
`controle_notes_20260820_v1.py`. N1 bloque, N2 se consigne.

---

## Règle de tenue

Aucune skill ne porte de valeur du REF en dur. Un repère de contrôle se nomme
par son identifiant de nœud — `D2-1-1-e1`, `D7-2-1-p1`, `D11-e1` — et la valeur
se lit au référentiel à l'exécution. Une valeur recopiée dans une skill est un
cache que personne ne rafraîchit : elle contrôle contre un état périmé du
corpus. La même règle vaut pour les trois sources : ni position, ni justification,
ni texte de note ne se porte en dur.

La hiérarchie des strates est inchangée : le manuscrit reste seul point de
vérité, les référentiels se contrôlent, les dérivés se régénèrent.
