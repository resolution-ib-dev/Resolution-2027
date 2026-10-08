# Structure d'une PPL(C/O) déposable

## Choix du véhicule

| Objet | Véhicule | Base |
|---|---|---|
| Révision de la Constitution | PPLC | art. 89 C |
| Loi organique (LOLF, LOLFSS, statut des magistrats...) | PPLO | art. 46 C |
| Loi ordinaire | PPL | art. 39 C |

Un même projet politique peut exiger plusieurs véhicules (révision constitutionnelle + LO d'application) : produire alors des documents séparés, avec dans l'exposé des motifs de chacun un renvoi à l'économie d'ensemble.

## Ordre du document

1. **Page de titre**
2. **Exposé des motifs**
3. **Dispositif** (« PROPOSITION DE LOI [CONSTITUTIONNELLE / ORGANIQUE] », puis les articles)
4. Le cas échéant : chapitre de **dispositions transitoires et finales**
5. Le cas échéant (PPL/PPLO uniquement) : **gage** en dernier article

## Page de titre

Mentions, dans l'ordre (modèle Assemblée nationale ; adapter pour le Sénat) :

```
ASSEMBLÉE NATIONALE                        [ou : SÉNAT]
CONSTITUTION DU 4 OCTOBRE 1958
[DIX-SEPTIÈME] LÉGISLATURE                 [Sénat : SESSION ORDINAIRE DE 20XX-20XX]

Enregistré à la Présidence de l'Assemblée nationale le [date]

N° [___]

PROPOSITION DE LOI CONSTITUTIONNELLE
[intitulé]

présentée par
[M./Mme Prénom NOM], député[e/s]   [ou : sénateur/sénatrice]

(Renvoyée à la commission des lois constitutionnelles, de la législation
et de l'administration générale de la République, à défaut de constitution
d'une commission spéciale...)
```

Numéro et date d'enregistrement laissés en blanc `[___]` : remplis au dépôt.

## Intitulé

- Neutre et descriptif ; pas de slogan. Formes : « portant révision de l'article X de la Constitution », « portant révision des articles X, Y et Z de la Constitution », « relative à [objet] », « visant à [objet] » (forme plus militante, admise pour les PPL).
- Un intitulé qui liste plus de quatre ou cinq articles bascule vers la forme thématique (« relative à la sincérité budgétaire et au consentement à l'impôt »).

## Exposé des motifs

Court. Mouvement obligé : **des principes vers les conséquences** — le lecteur doit d'abord adhérer à des principes compréhensibles, clairs et rassurants, avant de rencontrer la technique.

1. **Les principes** (1-2 paragraphes) : les principes simples que la réforme sert, formulés positivement et sans jargon — ce que chacun peut approuver (le consentement à l'impôt, la continuité de l'État, l'égalité devant la loi...). Rassurer : dire ce qui ne change pas autant que ce qui change. Le constat du mal vient à l'appui des principes, pas avant eux ; au plus deux ou trois chiffres sourcés.
2. **Les conséquences** (1 paragraphe) : comment le texte tire de ces principes des règles précises — l'économie générale, en une transition courte.
3. **Le commentaire par article** : un paragraphe par article ou groupe cohérent (« Les articles 3 à 5 tirent les conséquences de... »). Chaque paragraphe relie l'article au principe dont il découle, dit exactement ce qu'il fait, sans paraphraser le dispositif.

Ton : sobre, affirmatif, sans adjectifs d'intensité. Concision stricte : chaque phrase supprimée qui ne manque pas devait l'être. Tout chiffre est sourcé ou entre crochets `[à vérifier]`.

### Page de titre — maquettes par assemblée

Les mentions diffèrent selon l'assemblée de dépôt et ne sont pas interchangeables.
À revérifier sur le site de l'assemblée concernée avant tout dépôt réel.

**Sénat.** Ni mention « CONSTITUTION DU 4 OCTOBRE 1958 » ni numéro de législature :
ce sont les mentions de l'Assemblée nationale. Minuscule à « commission des lois ».
Numéro, date et noms laissés en blanc.

```
N° [___]

SÉNAT
SESSION ORDINAIRE DE 20XX-20XX

Enregistré à la Présidence du Sénat le [___]

PROPOSITION DE LOI CONSTITUTIONNELLE

[intitulé, sans le mot « proposition »]

(version en dispositions modificatives | version en substitution intégrale)

PRÉSENTÉE

Par M. [Prénom NOM], Mme [Prénom NOM], [...],
Sénateurs

(Renvoyée à la commission des lois constitutionnelles, de législation,
du suffrage universel, du Règlement et d'administration générale,
sous réserve de la constitution éventuelle d'une commission spéciale
dans les conditions prévues par le Règlement.)
```

**Assemblée nationale.** Porte en tête « CONSTITUTION DU 4 OCTOBRE 1958 » puis la
mention de la législature (« XVIIe LÉGISLATURE »), « Enregistré à la Présidence de
l'Assemblée nationale le [___] », auteurs « Députés », et le renvoi à la commission
des lois constitutionnelles, de la législation et de l'administration générale de la
République.

La mention de version se place sous l'intitulé lorsque deux versions du même texte
circulent — modificative et substitution.

### Descripteurs de travail

En cours de rédaction, chaque article peut porter sous son numéro une ligne unique en
italique entre crochets, registre objet et non finalité, sans article initial ni virgule.
Les articles seuls dans leur division en sont dispensés. Ces lignes sont des repères de
navigation, **retirées en bloc à la passe de dépôt** par un motif unique — paragraphe
italique intégralement entre crochets sous un numéro d'article :
`re.sub(r'(?m)^\*\[[^\]]*\]\*\n\n', '', texte)`.

Contrôle de sortie : aucun crochet résiduel hors les paramètres politiques non tranchés
et les blancs de la page de titre.

### Répartition des fonctions entre niveaux (règle impérative)

Chaque niveau a une fonction propre et une seule. Un niveau qui empiète sur le
suivant produit une redite : le lecteur relit sans avancer. C'est le défaut le
plus fréquent des exposés des motifs.

| Niveau | Fonction | Registre | Interdit |
|---|---|---|---|
| Assise de principes | pose les principes préexistants et le diagnostic | affirmatif, sans technique | numéro d'article, nom de mécanisme, chiffre |
| Chapeau de division (titre, partie) | rattache à chaque principe le moyen qui le sert | déductif, une phrase par subdivision | détail des mesures, noms de mécanismes |
| Commentaire d'article | nomme les mécanismes que l'article institue | descriptif, technique, sobre | reprise d'un principe, justification politique |

Chaîne à tenir : **concept → objectif → moyen.** L'assise porte le concept,
le chapeau porte l'objectif et désigne le moyen, le commentaire nomme le
mécanisme qui est ce moyen.

### Autorités

Guide de légistique, fiche 3.1.1 (mise à jour du 5 décembre 2024) : l'exposé des motifs
« ne doit, en aucun cas, être une paraphrase du texte du projet de loi ». Il expose, de
manière simple et concise, quatre objets — les raisons pour lesquelles le texte est soumis
au Parlement, l'esprit dont il procède, les objectifs qu'il se fixe, les modifications
qu'il apporte au droit existant. Structure en deux parties, une partie générale puis une
partie article par article ; **pour les textes longs, une explication par division (titre,
chapitre) peut suffire**.

Conseil constitutionnel, décision n° 2009-579 DC du 9 avril 2009, confirmée par la décision
n° 2023-13 FNR du 20 avril 2023 : tradition républicaine ayant pour objet de présenter les
principales caractéristiques du texte et de **mettre en valeur l'intérêt qui s'attache à son
adoption**. Cet intérêt est donc une composante attendue, que la sobriété ne doit pas effacer :
il se porte à l'assise et aux chapeaux de division, non aux commentaires d'articles.

Conseil d'État, 12 mars 1975, Sieur Bailly : l'exposé figure aux travaux préparatoires et le
juge peut s'y référer en cas de doute sur les intentions du législateur. Conséquence pratique :
tout énoncé interprétatif de l'exposé engage l'intention du constituant, et un silence sur un
point sensible sera lui aussi interprété.

L'obligation organique de l'article 7 de la loi organique n° 2009-403 du 15 avril 2009 ne vise
que les projets de loi. Pour une proposition, l'usage seul s'applique et la structure reste libre.

### « Dire ce que l'article fait » ne veut pas dire le restituer

Le lecteur a le dispositif sous les yeux quelques lignes plus bas. Restituer
ses phrases ne lui apprend rien et consomme le budget de l'exposé. Ce que
l'exposé seul peut fournir, c'est **le nom du mécanisme et sa raison**, qu'aucune
disposition n'énonce jamais — un dispositif institue, il ne se désigne pas.

Règle opératoire : le paragraphe **nomme** ce que l'article institue ; il ne
restitue verbatim que les paramètres indevinables — un plafond, une quotité,
un délai, un terme ; il ne reprend jamais la structure de phrase du dispositif.

Tout mécanisme institué doit recevoir un nom, et une seule fois dans l'exposé.
Dresser l'inventaire des noms avant de rédiger : leur absence est le signe que
le commentaire paraphrase. Exemples de noms tirés d'un chantier antérieur :
monopole des lois de finances, bouclier fiscal constitutionnel, règle d'or
démocratique, équilibre effectif opposé à l'équilibre de présentation,
compétence pluriannuelle accessoire, universalité, unité, douzième provisoire,
sincérité du vote, sursis-saisine, injonction de correction.

Quand un nom porte une qualification doctrinale, elle vaut mieux qu'un
développement : « règle d'or démocratique » distingue en un adjectif la règle
de la discipline budgétaire européenne et rattache la contrainte à son
fondement, la protection des contribuables suivants.

### Verbes de commentaire

L'exposé des motifs sert indifféremment une version modificative et une version
en substitution. Aucun verbe ne doit donc présupposer la technique retenue :

- **révise** — toute modification, quelle qu'en soit l'ampleur
- **abroge** — abrogation d'article, de titre ou de chapitre
- **insère** — création d'article

« Réécrit », « remplace », « est ainsi rédigé » sont bannis du commentaire :
ils décrivent la seule version en substitution.

### Ordre des paragraphes de commentaire

L'exposé des motifs échappe à la règle légistique de l'ordre du texte modifié :
il suit la **hiérarchie d'importance**, du mécanisme au plus large effet vers le
plus étroit. À l'intérieur d'un paragraphe, même règle. Les coordinations et les
modifications de portée mineure ferment le paragraphe en une phrase unique.

### Formulations

Privilégier les tours positifs : écrire ce que la règle fait. Éviter les
antithèses d'ouverture (« X ne se décrète pas, il s'organise ») et les tours
« ne tient pas à… mais à », « ni… ni ». Entorse tolérée lorsque la négation
porte un manquement constaté et non une règle. Exception pleine : la section
« ce que la proposition laisse intact », où la négation porte l'engagement de
non-modification.

Pas de virgule devant une conjonction de coordination, sauf clôture d'une
incise (« …des exercices ultérieurs, et arrête leur emploi »).

## Dispositif

- `Article 1er`, puis `Article 2`, `Article 3`...
- Subdivisions internes : `I. / II.`, puis `1° / 2°`, puis `a) / b)`.
- Un article de PPL = un objet cohérent (typiquement : un article modifié du texte hôte). Regrouper dans un même article de PPL des modifications de plusieurs articles hôtes seulement si elles forment un tout indissociable.

## Gage (PPL et PPLO)

Uniquement si le texte crée ou aggrave une charge publique ou diminue une ressource (art. 40 C). Formule usuelle :

> La charge pour l'État est compensée à due concurrence par la création d'une taxe additionnelle à l'accise sur les tabacs prévue au chapitre IV du titre Ier du livre III du code des impositions sur les biens et services.

Les PPLC ne sont pas soumises à l'article 40 : pas de gage.

## Recevabilité — points de vigilance

- **PPLC** : limites de l'art. 89 (pas de révision pendant une vacance ou une atteinte à l'intégrité du territoire ; forme républicaine du Gouvernement non révisable).
- **PPLO** : rester dans le domaine organique tel que la Constitution le renvoie ; toute disposition de nature ordinaire glissée dans une LO sera déclassée.
- **PPL** : art. 40 (charge) et art. 41 (domaine réglementaire).
- Signaler dans une note au demandeur, hors document, tout risque identifié — ne pas l'écrire dans l'exposé des motifs.

## Production docx

Lire la skill docx (`/mnt/skills/public/docx/SKILL.md`) avant génération. Conventions de mise en forme : corps de texte justifié, articles en petites capitales centrées (« Article 1er »), texte cité en retrait avec guillemets français, exposé des motifs avant le dispositif séparé par un saut de page, page de titre centrée. Nom de fichier : `PPLC_[objet]_YYYYMMDD_vN.docx` (date via `date +%Y%m%d`).
