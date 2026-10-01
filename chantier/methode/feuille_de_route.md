# FEUILLE DE ROUTE — Résolution

Consolidée le 24 août 2026. Document unique : il remplace la feuille de route
« production visuelle et analytique » et toutes les versions du jour.

**À porter aux instructions permanentes du projet.**

---

## 1. Le principe

Le manuscrit est la source. Rien ne s'en déduit à la main : tout passe par une
**couche de base** — les référentiels — que **cinq capacités** exploitent, et
qu'une **ligne de production** enchaîne pour sortir un produit.

Ce qui compte n'est pas la liste des produits, c'est la ligne. Un produit qu'on
ne sait fabriquer qu'une fois n'est pas un produit, c'est un coup de chance.

**Cinq capacités, et une seule est mûre.**

| capacité | ce qu'elle fait | état |
|---|---|---|
| **Inventorier** | recenser une population d'objets et la qualifier | instanciée trois fois, sans forme commune |
| **Confronter** | vérifier contre le corpus : cohérence, compatibilité, conformité, arithmétique | éclatée en huit outils, sans forme commune |
| **Traduire en droit** | porter une mesure dans une norme déposable | **mûre**, à répliquer |
| **Contester** | produire les objections, en deux volets | volet offensif seul, volet introspectif absent |
| **Contreproposer** | opposer une rédaction précise à un texte tiers | inexistante |

---

## 2. La couche de base

Trois référentiels, tous vivants, aucun complet.

**Le `REF_doctrine`** — 12 axes, 56 propositions, 97 effets, 57 paramètres,
21 sous-items, ancrés au manuscrit. C'est le plus mûr. Il porte des
`membres: ["M-nnnn"]` dont la couche de preuve a disparu.

Trois trous mesurés, et ils sont de la doctrine, non de l'appareil : **`D12` ne
porte aucune proposition** ; **neuf propositions n'ont aucun effet** — `D1-1-1`,
`D1-2-1`, `D1-3-1`, `D4-2-2`, `D5-3-4`, `D7-4-2`, `D8-2-3`, `D11-1-1`,
`D11-4-3` ; et 56 propositions ne portent que 97 effets, soit moins de deux en
moyenne.

**`REF_chiffres` — annoncé, pas construit.** Vérifié pièce par pièce le
24 août. Le générateur existe et il est substantiel, `generer_ref_chiffres.py`.
Tout le reste est vide : **`sources_chiffres.py`, où le sourçage s'écrit à la
main, ne porte aucune source** ; le rapprochement `meme_que`, arbitré en A-35
pour détecter deux valeurs discordantes du même fait, **n'est pas implémenté** ;
le référentiel produit n'est versé nulle part, et l'archive technique ne porte que
trois référentiels — doctrine, positions, notes.

**Les chiffres de référence ne sont donc pas un référentiel.** Ils vivent
rattachés à une proposition dans le `REF_doctrine` et dans les notes du
manuscrit : consultables, mais sans millésime, sans dérivation, sans source
déclarée et sans niveau de confiance. Rien ne dit aujourd'hui qu'un chiffre du
corpus ne contredit pas un autre chiffre du corpus.

**C'est la couche à construire en premier**, avant tout livrable chiffré — donc
avant le site, le manifeste, les notes et les posts.

**Le référentiel des positions** — 276 lignes, miroir et raccroche sur chacune,
les justifications et relais des 57 pertes écrits. **12 apports rédigés sur
194** : tout ce qui s'adresse à quelqu'un sort encore d'une phrase du livre
découpée.

**Ce qui manque à la couche de base**, et ce n'est pas rien : la couche de preuve
`Releve_affecte`, les identifiants la réclament et trois capacités en dépendent.
Elle est peut-être reconstructible depuis le manuscrit — à établir avant de la
déclarer perdue.

---

## 3. Les cinq capacités

### Inventorier

Recenser exhaustivement une population, la qualifier ligne à ligne, déclarer ce
qu'on ignore. C'est la modalité générale du chantier, et c'est là que l'audit est
le plus net.

**Ce qui est fait.** Trois inventaires existent — les notes du manuscrit, les
chiffres, les positions — et **aucun ne partage sa forme avec les deux autres.**
Trois structures, trois générateurs, trois jeux de contrôles, trois vocabulaires
de confiance. Le corpus a construit trois fois la même chose sans jamais
l'abstraire.

**Le chantier.** Une **forme d'inventaire unique** : une population, une unité de
ligne, un jeu de qualifications, un champ de source, un niveau de confiance, une
règle de contrôle. Les trois inventaires existants s'y rebasent, et les suivants
s'y instancient au lieu d'être réinventés.

**Ce qu'il reste à inventorier**, et qui attend cette forme : les **objections**
— aujourd'hui éparpillées entre 46 entrées du relevé, 45 de la réserve
d'arguments et 152 du proto de questions, sans population unique ; les **entités**
— agences, opérateurs, effectifs ; les **taxes et les niches**, dont les
classeurs sont au projet ; les **effets** de diagnostic, qui nomment les capteurs
et ne sont peuplés nulle part.

**Réemployable.** La forme, une fois posée, sert tout inventaire à venir.
**Découpable.** Un inventaire à la fois, une tranche de population à la fois.

### Confronter

Vérifier une chose contre le corpus. Cohérence interne, compatibilité doctrinale,
conformité avant diffusion, exactitude arithmétique, résolution des renvois.

**Ce qui est fait.** Beaucoup, et en désordre : deux skills — `audit-conformite`,
`compatibilite-doctrine` — et six contrôles d'appareil, structurel, arithmétique,
notes, chiffres, index, restauration. Le **contrat de projection est recopié mot
pour mot dans cinq skills** : une correction se porte cinq fois ou quatre
divergent en silence.

**Le chantier.** C'est un spectre de nature commune, il doit avoir une forme
commune : un contrat unique, importé et non dupliqué ; un vocabulaire de verdict
unique ; une sortie d'anomalie unique. Aujourd'hui chaque outil a le sien.

**Réemployable.** Par définition : rien ne sort sans passer là.
**Découpable.** Par type de contrôle.

### Traduire en droit

Porter une mesure dans un texte déposable.

**Ce qui est fait.** **La capacité mûre du chantier.** Trois skills, cinq
fichiers de référence, un script de diff, une procédure de bouclage bloquante.
Deux propositions de révision constitutionnelle consolidées, en modificative et
en substitution, avec exposé des motifs. Le trois colonnes Constitution, 37 blocs.
Le trois colonnes LOLF, 29 blocs, transcrit et jamais relu.

**Le chantier : répliquer.** La compétence est prouvée sur un véhicule, la
Constitution. Elle doit se porter sur la **loi organique** et la **loi
ordinaire**, et — c'est le point que le PLF impose — sur l'**amendement**, qui
est le véhicule court dont on aura besoin en novembre et que rien ne couvre.

**Réemployable.** Le trois colonnes est la strate maître : on le met à jour, puis
on rejoue les textes.
**Découpable.** Par véhicule, puis par article.

### Contester

Produire les objections. **Deux volets, et ils ne servent pas à la même chose.**

**Volet offensif — se préparer.** Ce qu'on va nous opposer, classé par
dangerosité, et la riposte qui répond. Existe : `contestabilite` et `qa-riposte`,
avec trois contradicteurs typés — opposant, citoyen méfiant, expert.

**Volet introspectif — nous tester.** Est-ce que la mesure tient vraiment ? Où
est l'angle mort, et **est-il assumé ou seulement ignoré ?** Cela n'existe pas.
C'est pourtant le volet qui a de la valeur pour nous : le premier prépare la
parole, le second corrige la doctrine. Une objection à laquelle on ne sait pas
répondre est un défaut de mesure avant d'être un défaut d'argumentaire.

**Le chantier.** Ouvrir le volet introspectif, et le brancher en amont : ce qu'il
trouve remonte au référentiel, pas au script de réponse. Une distinction à
porter : **angle mort assumé** — on l'a vu, on le tient, on le dit — contre
**angle mort ignoré**, qui est une lacune à instruire.

**Réemployable.** Les objections servent la Q&A, les fiches, les posts, la prise
de parole.
**Découpable.** Par mesure.

### Contreproposer

Opposer à un texte tiers une rédaction précise, ciblée, chiffrée.

**Ce qui est fait.** Rien. Les classeurs du PLF sont au projet, et c'est tout.

**Le chantier.** C'est la capacité manquante, et elle est composite : elle
suppose de **découper** un texte qu'on ne maîtrise pas — donc d'inventorier une
population externe —, de le **confronter** au référentiel, de produire une
position, puis de la **traduire** en amendement. Elle ne s'ajoute pas aux quatre
autres : elle les compose.

**Réemployable.** Un seul dispositif pour quatre usages — proposition externe,
contreproposition, PLF, réaction à l'actualité.
**Découpable.** Le dispositif d'abord, éprouvé sur un cas ciblé ; les usages
ensuite.

---

## 4. La ligne de production

Toute commande suit le même trajet. C'est ce qui rend la production répétable.

**Entrée** — une commande, et son destinataire. Journaliste, grand public,
parlementaire, nous-mêmes.

**1. Le référentiel dit ce qui est vrai.** Aucun produit ne porte un chiffre ou
un énoncé qui n'y est pas. Un chiffre de confiance nulle ne sort pas.

**2. L'inventaire dit qui est concerné et dans quelle mesure.** Effets, gains,
pertes, objections, entités : selon le produit.

**3. La contestation éprouve.** Volet introspectif d'abord — la mesure tient-elle,
l'angle mort est-il assumé. Ce qui casse ici remonte au référentiel et ne
descend pas dans le produit.

**4. La projection écrit.** Une skill ou un générateur, jamais à la main, jamais
en recopiant le manuscrit.

**5. La confrontation contrôle.** Verbatim, sources, ancrage doctrinal, registre,
cohérence entre documents, vocabulaire.

**6. La mise en forme sort.** Web, document, note, fiche, image, texte
déposable.

**Sortie** — le produit, plus la trace de ce qui l'a fabriqué : le produit se
régénère, il ne se corrige pas à la main.

**La règle qui tient la ligne : un livrable ne se corrige jamais en aval.** Une
erreur remonte à l'étage où elle est née, et on rejoue.

---

## 5. Les cinq produits, et leur trajet

| produit | ce qu'il traverse | ce qui lui manque |
|---|---|---|
| **Manifeste** — le 1-pager repris | référentiel · inventaire des constats · confrontation | l'inventaire des effets de diagnostic ; la matière existe, `1pager` proto |
| **Qui gagne, qui perd** | référentiel · inventaire des positions · projection | 182 apports sur 194 ; l'extrait et l'interface se génèrent déjà |
| **Q&A** | inventaire des objections · contestation · projection · confrontation | la population unique d'objections ; `Releve_affecte` ; une Q&A de référence |
| **Site** | tous les inventaires, sans en ajouter | il n'ajoute pas de matière, il l'expose — donc il dépend de tout le reste |
| **Analyse et contreproposition au PLF** | **les cinq capacités** | la capacité de contreproposition, et le véhicule amendement |

**Le PLF est le produit qui traverse toute la ligne.** Découper le texte,
confronter chaque poste au référentiel, produire une position, la rédiger en
amendement, la contrôler. C'est lui qui dira si la ligne tient — et il a une date
que nous ne fixons pas.

**Le site est l'inverse** : il n'ajoute aucune matière, il expose celle des
autres. Sa qualité est exactement celle des inventaires qu'il affiche, et pas
davantage.

---

## 6. La robustesse

Elle ne s'obtient pas en ajoutant des contrôles, mais en n'ayant qu'une forme de
chaque chose.

**Une forme d'inventaire**, instanciée, jamais réinventée. **Un contrat de
projection**, importé, jamais recopié. **Un vocabulaire de confiance** et **un
vocabulaire de verdict**. **Une table de résolution des renvois** —
`methode/index.json` — et un bloc `manquants` pour ce qui ne résout pas.

**Trois règles qui ne se négocient pas.** Aucune source ne s'invente et aucun
trou ne se comble. Un contrôle annoncé est un contrôle mécanique. Un dérivé se
régénère et ne se corrige jamais à la main.

**Un nom canonique par artefact, aucun horodatage**, à l'entrée comme à la
sortie.

---

## 7. Ce qui attend l'auteur

- **Enregistrer les sept skills corrigées.** Sans cela, aucune capacité de
  projection ne résout ses entrées.
- **Porter ce document aux instructions permanentes.**
- **Par quelle capacité on entre.** La forme d'inventaire commande le plus de
  choses ; la traduction juridique est prête et n'attend qu'une commande ; la
  contreproposition a une date.
- **La date du bon à tirer** du livre, qui borne le seul travail qui expire : le
  contrôle arithmétique.
