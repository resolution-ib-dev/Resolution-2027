---
name: vecteur-mesure
description: "Trouve le siège juridique à modifier pour porter une mesure — le vecteur, distinct du véhicule. Couvre la loi de finances, la loi de financement de la sécurité sociale et la loi ordinaire, y compris la jambe d'une mesure scindée entre deux véhicules. Utiliser dès qu'il s'agit de savoir « quel article on modifie », « où ça s'amende », « quel est le siège juridique de », de partir d'un énoncé en langage naturel (« supprimer l'ADEME », « plafonner la taxe XYZ », « diviser par deux les subventions à ZZZ ») pour rendre une ou plusieurs adresses de droit, ou de contrôler une adresse déjà relevée. Déclencher aussi pour toute demande mentionnant vecteur, siège juridique, adresse d'article, article de code à viser, ou « où est-ce écrit dans le droit ». Ne pas déclencher pour rédiger la disposition elle-même — c'est disposition-cible — ni pour savoir si la mesure peut voyager dans le véhicule visé, qui est le test de rattachement."
---

# Vecteur d'une mesure — l'adresse, jamais le texte

Le **vecteur** dit *quel article de quel texte on modifie*. Le **véhicule** dit
*dans quel texte on dépose*. Les deux ne se confondent jamais, et un contrôle le
refuse.

Le rattachement se plaide ; **le vecteur ne se plaide pas : il se trouve, ou il
n'existe pas.** Une mesure parfaitement rattachable et sans vecteur identifié
n'est pas rédigeable — et c'est un résultat, pas un échec.

**Un vecteur est un identifiant, jamais du verbatim.** « Article L. 131-3 du code
de l'environnement » est une adresse ; le texte de cet article est autre chose.
C'est ce qui rend la recherche légitime : elle repère, elle ne copie pas. **Ne
jamais rendre le texte d'un article.**

---

## 0. Ce que « à blanc » retire, et ce qu'il ne retire pas

**À lire avant tout le reste, parce que c'est le défaut le plus coûteux mesuré
sur cette étape.**

> **Le mode à blanc retire la valise** — le réservoir d'arguments, le référentiel
> de sièges déjà relevés, les tables d'un auteur.
>
> **Il ne retire ni le contexte fourni par l'utilisateur, ni les annexes du texte
> chargé, ni la recherche publique.** Ces trois rôles sont publics, ils se
> téléchargent, et **ils restent dus à cette étape** autant qu'à l'exposé
> sommaire.

**Une annexe publique ne se demande pas : elle se va chercher.** Une adresse
rendue `a_trouver` sans avoir ouvert un rôle disponible n'est pas une
dégradation : c'est un **manque**, et il s'écrit comme tel.

**Et un manque coûte quelque chose** : le dossier sort à l'état `à vérifier avant
dépôt` tant que le rôle n'est pas ouvert ou que son inaccessibilité n'est pas
établie sur pièce. *Un manque proprement déclaré qui ne coûte rien est un manque
qui se reproduit.*

*Coût mesuré : sur un lot de six énoncés, la recherche publique n'a été ouverte
que pour trouver un dépôt clonable de codes, jamais pour relever une adresse —
qui est son emploi le plus rentable. Deux dossiers en sont morts.*

## 0 bis. Les véhicules couverts — des sous-cas, et la méthode ne change pas

**L'adresse de droit ne dépend pas du véhicule.** Un article de code est un
article de code. Ce que le véhicule commande, ce sont trois choses seulement : la
famille de siège (§ 1), les rangs de l'échelle des sources qui répondent (§ 4) et
la variante (§ 9). **Tout le reste de la skill se joue à l'identique.**

| véhicule | ce qui change, et rien d'autre |
|---|---|
| **loi de finances** | le levier des crédits vise l'état B ; le rang 4 dispose de l'annexe des voies et moyens et de l'annexe des taxes affectées ; la table des articles ouverts rend la variante `article_ouvert` jouable |
| **loi de financement de la sécurité sociale** | le siège est au code de la sécurité sociale ; les portes utiles sont aux articles `LO 111-3-6` à `LO 111-3-8` ; le monopole de l'article `LO 111-3-16` tire les exonérations de cotisations ; la table des articles ouverts est celle du texte de financement, et le rang 4 dispose des annexes propres à ce texte |
| **loi ordinaire** | il n'y a ni état B ni annexe financière : **le levier des crédits est `sans objet` et le rang 4 tombe.** L'échelle descend 1, 2, 3, 3 bis, 5, 6 — et le rang 2 n'existe que si un texte est effectivement en discussion |
| **strate supérieure** — loi organique, révision constitutionnelle | l'adresse se relève de la même façon, **mais la strate se qualifie d'abord** : c'est `analyse-transposabilite` qui dit si la mesure passe à ce niveau, et cette étape ne tranche pas à sa place |

**Une mesure scindée porte deux vecteurs et deux véhicules** (§ 1), et **chaque
jambe descend l'échelle pour son compte** : une jambe de loi ordinaire ne perd pas
son vecteur parce que l'autre jambe a trouvé le sien en loi de finances.

**Le véhicule est une donnée du dossier, jamais une déduction de l'étape.** Quand
il n'est pas donné, l'étape relève l'adresse et laisse le véhicule à sa place —
le test de rattachement —, sans rien conclure.

---

## 1. Qualifier le statut de la dépense — il décide de la famille de siège

**Avant tout le reste.** Une mesure d'économie a souvent plusieurs adresses
possibles, et **on cherche le siège de l'effet, jamais celui de l'objet.**

| statut de la dépense | véhicule | siège à chercher |
|---|---|---|
| crédits d'État | PLF, état B | interne au PLF — aucun siège de droit à chercher, l'adresse est la ligne plus la catégorie |
| dépense fiscale | PLF, 1re partie | l'article dérogatoire, porté par l'annexe |
| **dépense sociale** | **PLFSS** | code de la sécurité sociale ; la porte utile est aux articles **`LO 111-3-6` à `LO 111-3-8`**, une par partie du texte — `LO 111-3` ne définit plus que les trois espèces de lois de financement |
| **dépense locale** | PLF pour la ressource, **loi ordinaire pour la norme** | **trois sièges distincts** : dotations au CGCT, recettes au CGI et à la fiscalité affectée, compétence ou obligation au code sectoriel |
| **dépense d'opérateur** | PLF, 1re ou 2de partie | **deux sièges** : création au code ou à la loi fondatrice, financement à l'article de taxe affectée — plus le **cadre budgétaire**, qui vit dans des articles de lois de finances antérieures et non dans un code |

**Une intention peut n'être portable par aucun véhicule unique, et la scission se
rend.** Le monopole des lois de financement — `LO 111-3-16` — tire vers le PLFSS
la part d'une mesure qui touche aux réductions ou exonérations de cotisations,
sans y attirer la part qui touche à l'impôt. La skill rend alors **les deux jambes
avec leurs deux véhicules**, chacune portant son vecteur.

*Ce que le défaut coûte, mesuré* : sur la participation des employeurs à l'effort
de construction, la skill a rendu l'article du code général des impôts qui porte
la **cotisation** quand l'amendement visait l'article du code de la construction
qui porte l'**obligation**. Adresse plausible, mauvais levier.

## 2. Balayer les quatre leviers EN ENTIER — avant toute conclusion d'inexistence

**C'est une obligation, pas une méthode.** Une intention n'a pas un vecteur : elle
en a autant que son objet a de prises.

| levier | ce qu'on touche | où est l'adresse |
|---|---|---|
| **ressource** | le prélèvement lui-même | l'article qui l'institue |
| **affectation** | le chemin du prélèvement vers l'entité | l'article d'affectation, ou le plafond |
| **crédits** | la dotation budgétaire | la **ligne de l'état B** — mission, programme — plus la **catégorie de dépense** |
| **emploi** | le dispositif que l'entité sert, ou la norme qui produit la dépense | le texte qui crée le droit, l'aide ou l'obligation |

**L'étape écrit ce qu'elle trouve à chacun des quatre, « rien » compris, et
`inexistant` se déclare PAR LEVIER, jamais par intention.** Un état rendu pour la
mesure entière masque le seul levier qui compte.

*Coût mesuré : sur un énoncé de conditionnalité, trois leviers étaient fermés et
un était ouvert. L'état rendu pour l'intention entière a masqué l'ouvert, et le
dossier est sorti vide.*

**Et le balayage reste dû quand la ligne sort du domaine du véhicule.** Une ligne
rendue hors domaine sort avec sa jambe déclarée — le véhicule réel — **et la
skill cherche en plus le levier portable dans le véhicule visé**, quand il en
existe un. *Coût mesuré : sur treize lignes sorties d'un domaine, deux portaient
un levier substitué portable dans le véhicule, signalé et non rédigé ; les onze
autres n'ont pas été cherchées.*

### Le levier des crédits ne se déclare JAMAIS `inexistant` faute d'article de code

**Son vecteur est `sans objet` par construction.** L'état B se vote par
programme, non par bénéficiaire : un organisme, une commission ou un dispositif
sans ligne propre reste atteignable par le programme qui le finance, dès lors que
ce programme est identifié.

**Son adresse est la ligne de l'état B plus la catégorie de dépense** de la
justification au premier euro. **Un énoncé qui nomme une classe de
bénéficiaires** — associations, opérateurs, entreprises, ménages, collectivités —
**nomme par là même une catégorie du titre 6**, et la règle de baisse s'écrit sur
elle.

La table des catégories est un rôle : *la nomenclature par nature des dépenses de
l'État*, sept titres, dix-huit catégories, fixée par l'article 5 de la loi
organique. Le dossier dit quel fichier la tient.

**Trois subtilités, et elles se déclarent dans le relevé.**

- **Une catégorie ne capte jamais toute la classe.** Les associations sont en
  **64**, mais aussi en **32** quand la subvention rémunère une charge de service
  public déléguée, et en **62** quand l'association exerce une activité
  économique. Un amendement qui ne vise que 64 laisse les deux autres en place,
  **et cela se dit**.
- **La catégorie 64 ne contient pas que des associations** : elle porte aussi les
  transferts aux opérateurs qui ne sont pas des subventions pour charges de
  service public, aux organismes internationaux, aux fondations. La règle de
  baisse touche donc plus large que l'énoncé.
- **La catégorie n'est pas un objet votable.** Elle sert la règle de baisse et la
  justification, jamais l'adresse. Un amendement qui prétendrait abroger une
  catégorie est irrecevable.

**Une mesure de crédits est de plein exercice et de rang législatif.** L'état B
est voté, les crédits sont limitatifs. Ne jamais présenter un amendement de
crédits comme infra-législatif au motif qu'il porte sur des plafonds.

**Une mesure de crédits ne se paramètre jamais sur un montant en dur** : sur la
ligne — mission, programme, catégorie — et sur la règle de baisse. Le montant se
reprend au texte en discussion.

**La forme d'appel est le DERNIER recours, jamais le premier.** Ordre, et il ne
s'inverse pas : la ligne chiffrée → le proxy documenté → l'estimation montrée →
et seulement après ces trois échecs, la minoration d'un euro sur le programme
porteur, l'exposé nommant la cible et la portée réelle, **avec son motif écrit**.
*Coût mesuré des deux côtés : son absence a coûté un dossier entier — une
commission consultative sans imposition affectée et sans crédits identifiés,
rendue hors capacité alors qu'un programme nommé finançait son action ; et son
emploi trop précoce a produit deux amendements à un euro, refusés, remplacés par
deux amendements chiffrés.*

## 3. La règle du levier substitué, et son pendant sur l'énoncé

### 3.1 Le levier demandé est vide

> Quand le levier demandé est vide, la chaîne ne s'arrête pas : elle rend **le
> levier portable le plus proche**, étiqueté `variante — levier substitué`, avec
> une phrase disant en quoi il diffère de la demande. L'auteur arbitre. **Une
> sortie vide n'est jamais préférable à une sortie étiquetée.**
>
> **L'interdit d'inventer porte sur l'adresse, jamais sur la voie.** Une adresse
> fausse envoie l'amendement au mauvais endroit ; une voie substituée et déclarée
> ne trompe personne.

Ordre de proximité, fixé : même organisme et même exercice > même organisme, autre
exercice > même programme > même mission.

*C'est la faute mère d'un lot entier : l'interdit réel est « aucune adresse ne
s'invente », et il avait été étendu en « aucune voie de substitution ne se
propose ». Le premier protège contre du faux droit. Le second ne produit rien et
se déguise en rigueur.*

### 3.2 L'énoncé est indéterminé — le pendant, et il manquait

**La règle du § 3.1 traite le levier vide. Celle-ci traite l'énoncé incomplet**,
et la frontière entre « le sens ne s'invente pas » et « la voie substituée se
déclare » se tenait jusqu'ici au jugement, cas par cas.

| ce que l'énoncé porte | conduite |
|---|---|
| **une direction sans dispositif** — « ubériser le transport sanitaire », « simplifier le régime de X » | **on rédige à la lecture la plus étroite qui produise l'effet, et la lecture se déclare** |
| **aucune direction** — un objet et un paramètre sans verbe, dont ni la hausse ni la baisse ne se déduisent | **on ne rédige pas.** `non portable — le sens de la modification n'est pas porté` |
| **deux lectures défendables** — un taux qui peut être un total ou une part, un délai qui peut se lire dans les deux sens | **on rend les deux lectures**, on rédige celle qui sert le sens général, et l'autre s'écrit. *Cas tranché : un taux qui est la somme de deux prélèvements votés séparément désigne le total* |
| **un paramètre chiffré absent qui commande le dispositif** | il se prend aux paramètres du dossier ; à défaut on le choisit, on l'écrit, on le porte à la notice. **Jamais `hors_capacite` pour ce seul motif, jamais une valeur alignée en silence sur un énoncé voisin** |

*Coût mesuré : sur un lot de vingt-cinq lignes, trois rendues non portables faute
d'un élément que la pièce ne portait pas, une quatrième rédigée sur la lecture la
plus étroite d'une direction sans dispositif — quatre décisions justes, aucune
règle derrière.*

## 4. L'échelle des sources d'adresse — six rangs, un repli, et le rang atteint s'écrit

**L'étape descend l'échelle jusqu'à ce qu'une source réponde, et elle écrit à quel
rang elle s'est arrêtée.**

| rang | source | ce qu'elle prouve |
|---|---|---|
| 1 | le **texte déposé**, quand il nomme l'article | l'adresse **et son voisinage** — preuve la plus forte |
| 2 | la **table des articles ouverts** | le couple (texte, article), **jamais la subdivision** |
| 3 | le **dépôt de droit** cloné | l'adresse **et** le verbatim, quand le texte y est |
| **3 bis** | un **dépôt secondaire** — miroir, base d'éditeur, reproduction dans un rapport | l'adresse et un verbatim **dégradé** |
| 4 | les **annexes du texte chargé** | l'annexe des voies et moyens rattache une dépense fiscale à son article ; l'annexe des taxes affectées rattache une imposition au sien. L'adresse, avec un chiffre en prime |
| 5 | la **base publique des amendements déposés** | l'adresse, **et un précédent de recevabilité** — gratuit |
| 6 | le **rapport de commission** | l'adresse, et la controverse |

**Les rangs qui répondent dépendent du véhicule (§ 0 bis)** : hors texte financier,
le rang 4 n'existe pas et le rang 2 suppose un texte effectivement en discussion.
**Un rang qui n'existe pas pour le véhicule ne se compte pas comme descendu** : il
se déclare sans objet, et l'étape continue de descendre.

**`a_trouver` ne se rend qu'après avoir descendu les six rangs.** Une adresse
relevée au rang 4, 5 ou 6 **est une adresse relevée**, même si son verbatim reste
indisponible : l'adresse et le verbatim sont deux dépendances distinctes, et
abroger un article entier n'a pas besoin de son texte.

*Coût mesuré : l'étape n'a longtemps connu que les rangs 1 et 2, et s'arrêtait au
second. Sur un lot, six adresses sont sorties `a_trouver` pour ce seul motif ; sur
un autre, les sièges des droits de mutation — parmi les plus documentés du droit
fiscal français — sont sortis « aucune adresse relevée ».*

### Le rang 3 bis est fait pour un dépôt joignable mais intermittent

**Un dépôt de droit qui répond sur dix articles et refuse le onzième n'est ni
`hors_perimetre` ni `absent` : il est intermittent.** Sans rang pour ce cas, la
parade s'improvise à chaque refus, et rien dans la sortie ne distingue le verbatim
ainsi relevé des autres.

**Un verbatim relevé au rang 3 bis porte une dégradation propre** : il se cite avec
sa source secondaire, **il ne vaut pas preuve de version**, et il porte un item de
notice. *Coût mesuré : trois articles refusés en accès direct sur une même passe,
chacun relevé par une source différente choisie au coup par coup.*

### Savoir qu'un article est ouvert dit qu'on peut s'accrocher, jamais où

**Quand l'article est ouvert, la subdivision se cherche, et le rang 4 est fait
pour cela.** *Coût mesuré : une branche fiscale entière perdue sur un énoncé à
trois branches, alors que l'article était ouvert par le texte déposé et que la
subdivision se relevait sur l'annexe qui chiffre la dépense fiscale.*

### Le voisinage est une piste, jamais une adresse

Quand le texte déposé nomme un article d'un code, **les articles voisins du même
chapitre sont la première piste pour les objets connexes de l'énoncé.** Elle **se
confirme sur pièce avant d'écrire l'adresse.** *Coût mesuré : un régime connexe
était à quelques articles de l'article que le texte déposé nommait, et le
voisinage n'a pas été suivi.*

## 5. Joindre au relevé AVANT de chercher

**Un référentiel de sièges déjà relevés est une commodité, jamais une
dépendance** : la skill nomme le rôle, le dossier dit quel fichier le tient. Quand
il en est joint un, il se joint **avant toute recherche**. Chercher d'abord
gaspille une requête et fabrique un doublon.

Joindre sur le **libellé exact du référentiel**. Une clé qui ne joint rien sort en
échec ; elle **ne s'apparie jamais au plus proche** — le meilleur voisin de
« Communes » est « Ordre de la Libération - Conseil National des communes », score
1,00, et c'est faux.

## 6. Chercher — une requête par cible

**Le shell ne cherche pas.** La recherche se fait par l'outil du fil. Un script
dérive, joint et contrôle ; il ne trouve jamais un vecteur.

**Requête type** : nom exact de l'organisme ou du dispositif + code présumé +
numéro d'article présumé, domaine restreint à `legifrance.gouv.fr`. Le numéro
présumé peut être faux : c'est une amorce, la réponse le corrige.

**Ce qui fait une bonne réponse : le titre de section nomme lui-même la cible.**
« Section 3 : France compétences », « Chapitre V : Impositions affectées au Centre
national du cinéma et de l'image animée ». Quand le titre porte le nom, la
fourchette d'articles qui le suit **est** le vecteur, sans interprétation. Quand il
ne le porte pas, **on descend d'un rang de l'échelle du § 4** ; on ne comble pas.

**Coût mesuré, non estimé** : lot pilote de onze cibles, onze réponses au premier
essai, dix-huit vecteurs rendus — 1,6 par cible.

### Chercher les deux vecteurs, pas un

Un organisme est **créé** par un texte et **financé** par un autre. Les agences de
l'eau : une section du code de l'environnement pour l'institution, une autre pour
les redevances. **Une mesure d'économie vise presque toujours le financement.**

Cinq rôles, et chaque vecteur déclare le sien : `creation` · `financement` ·
`competence` · `montant` · `derogation`.

### Ce que la structure du financement commande

- **Affectation directe non plafonnée** : ressource et affectation sont ouvertes
  toutes deux, et leurs effets diffèrent — supprimer le prélèvement l'éteint pour
  tous, supprimer l'affectation le renvoie au budget général.
- **Affectation plafonnée** : l'écrêtement existe déjà. Abaisser le plafond ne rend
  au budget général que la part au-dessus du plafond et laisse le socle intact.
- **Affectation indirecte** — la ressource transite par un tiers, un fonds de
  fonds, une caisse qui reverse à une autre : **le vecteur n'est pas chez l'entité
  visée, il est au point où l'affectation est écrite.** On remonte le circuit
  jusque-là ; à défaut on descend l'échelle, on ne vise pas l'entité faute de
  mieux.
- **Subvention pour charges de service public** : le levier des crédits atteint
  l'entité elle-même, catégorie 32.
- **Crédits pour compte de tiers** — l'entité n'est qu'opérateur payeur : le levier
  des crédits atteint **le dispositif, pas l'entité**. Les deux intentions ne se
  confondent pas.
- **Ressources propres** — redevances, produits, ventes : les trois premiers
  leviers n'y mordent pas. Restent l'emploi, ou l'existence même de l'entité.

Trois règles de conduite :

- **Nommer l'intention avant de choisir le levier.** Supprimer l'entité, réduire
  son activité, supprimer le dispositif qu'elle porte : trois intentions, trois
  jeux de leviers.
- **Un levier se déclare pour ce qu'il fait, jamais pour ce qu'on en attend.** Un
  écrêtement n'est pas une suppression.
- **Le levier des crédits est le seul annuel**, les trois autres modifient du droit
  permanent. Une décomposition mêle donc des vecteurs de nature différente et elle
  le rend.

### Trois pièges, tous rencontrés

- **La partie réglementaire ne sert à rien.** Un décret fondateur n'est pas à
  portée d'un amendement. Seule la partie législative compte, et **une mesure dont
  le seul vecteur est réglementaire sort avec ce motif.**
- **La loi codifiée et le code disent la même chose deux fois.** L'ADEME a sa loi
  de 1990 et ses articles de code. Abroger l'une n'équivaut pas à abroger les
  autres : **le relevé porte les deux et ne choisit pas.**
- **Une ligne d'économie n'est pas toujours un organisme.** « CCI et chambres
  d'agriculture » est une ligne et deux vecteurs. Inversement les 34
  établissements publics fonciers tiennent dans un seul article.

## 7. Décomposer l'adresse — quatre niveaux, aucun collage

**code · siège · article · subdivision.** `158-5-a` n'est pas une adresse, c'est
trois niveaux collés — et abroger l'article, le 5 ou le a ne vise pas le même
objet.

**Aucune épissure.** Un fragment qui ne commence pas par un numéro est une
**subdivision de l'article précédent**, écrite comme telle. « art. 199 undecies B,
C, D » est un article et deux subdivisions, pas trois articles.

Trois formes qui piègent le découpage : la lettre de partie est bornée à **L, R,
D** — `A 2°` est une subdivision ; un nombre nu suivi du signe ordinal est une
subdivision ; et le numéro admet un suffixe après l'ordinal — `278 sexies-0 A` ne
se coupe pas en `278 sexies` plus `0 A`.

## 8. Le code ne s'affirme jamais

**Déduire le code de la numérotation est une affirmation déguisée.** Elle a été
fausse sur 55 entrées : `L. 312-xx` et `L. 421-xx` sont au code des impositions
sur les biens et services, `L. 2333-55-3` au code général des collectivités
territoriales.

Chaque vecteur déclare **la règle de déduction qui l'a produit**, avec son motif,
son identifiant de code, son siège, sa date de vérification et la requête qui l'a
établie. **Ce qu'aucune règle ne couvre sort en `indéterminé`** — jamais en code
par défaut, et **un code posé sans règle est en faute.**

## 9. Poser la variante — et elle commande le TYPE d'adresse

Trois valeurs : `article_ouvert` quand le texte déposé rouvre déjà l'article —
c'est le cas le moins cher en recevabilité, en vecteur et en débat ; `absolu` pour
un article additionnel, le plus cher ; `a_determiner` tant que le socle du texte
déposé n'est pas connu.

- Sur un **article ouvert**, le dispositif porte le plus souvent sur les **alinéas
  du texte déposé** — « au deuxième alinéa du I de l'article 2, supprimer… ». Il
  n'y a alors **aucun article de code à viser**, et en produire un est une
  surqualification. **Mais la subdivision du texte déposé se cherche** (§ 4).
- Sur un **article additionnel**, la mesure vise soit un article de code existant,
  soit un **article nouveau non codifié** — une clause de caducité, une obligation
  de rapport n'ont pas de siège préexistant.

**La variante `article_ouvert` suppose la table des articles ouverts**, donc le
rang 2 de l'échelle. **Quand elle n'est pas disponible, la skill le déclare et
travaille en `absolu`** : c'est une dégradation réelle, parce qu'elle fait perdre
la forme la moins coûteuse en recevabilité — et elle ne se découvre pas en cours
de route, elle se lit au manifeste. **Hors texte en discussion, `absolu` n'est pas
une dégradation : c'est le régime normal, et il se déclare comme tel.**

**La carte des ouvertures se rend classée par coût d'immixtion**, du moins cher au
plus cher : insertion dans un alinéa existant, substitution d'un alinéa, insertion
d'une subdivision, réécriture de l'article, article additionnel. **Le rang retenu
se justifie.** C'est `disposition-cible` qui rédige ; c'est ici que la carte se
relève.

## 10. Les six états, et quatre ne sont pas des manques

| état | ce qu'il dit | ce qu'il appelle |
|---|---|---|
| `trouve` | l'adresse est relevée, avec son rang de source | on rédige |
| `sans_objet` | mesure de crédits — pas de vecteur codifié | la ligne et la catégorie |
| `siege_non_codifie` | la mesure crée une règle nouvelle sans modifier d'article existant. **Rédigeable** | l'analogie |
| **`hors_perimetre`** | **le siège existe, le dépôt de droit ne le porte pas** | **la cible s'ajoute à la configuration et la passe rejoue.** Ce n'est pas un échec |
| `a_trouver` | les six rangs de l'échelle ont été descendus sans réponse | le rang atteint s'écrit |
| `inexistant` | **par levier**, jamais par intention | la cascade ci-dessous |

**`hors_perimetre` ne se confond jamais avec une adresse fausse.** Trois
situations, trois conduites :

| situation | conduite |
|---|---|
| article **absent d'un code présent** | l'adresse est fausse — l'étape **lève** |
| numéro absent d'une **série** dont le code porte les voisins | **l'extraction est en cause, non l'adresse.** L'étape le déclare et descend d'un rang |
| texte **absent du périmètre** du dépôt | `hors_perimetre` — **on ajoute et on rejoue** |

*Coût mesuré : « un article absent de l'extrait lève » a été appliqué aux trois
cas. Les textes non codifiés — un article de loi de finances antérieure, une
ordonnance d'affectation — étaient à portée d'une ligne de configuration chacun,
et trois dossiers sont morts de cette confusion. Sur un autre lot, une série
entière absente d'un code pourtant chargé a rendu un renvoi invérifiable.*

**La cascade de `inexistant`, et son premier cran est le plus utile.**

> **0. Le levier de crédits du programme porteur.** L'état B se vote par
> programme, non par bénéficiaire. **Ce cran s'épuise avant tout autre**, et
> l'échec déclaré ne se prend qu'après lui. **Hors texte financier, ce cran est
> sans objet et la cascade commence au 1.**
>
> 1. Une règle générale dont l'effet atteint l'objet sans le nommer.
> 2. À défaut, une obligation d'information ou de compte rendu rattachée à une
>    annexe générale qui existe déjà.
> 3. À défaut, l'échec déclaré, qui reste une réponse.

**Le dernier cran ne se prend qu'en dernier**, et un vecteur de crédits disponible
l'exclut. **La cascade n'est pas une licence à fabriquer une adresse** —
l'interdit sur le vecteur inventé prime.

## 11. Écrire le relevé — la skill capitalise

Toute recherche neuve entre au relevé tenu à la main. Une entrée par cible : `cle`
(libellé exact du socle), `population`, `releve_le`, `requete`, puis un ou
plusieurs `vecteurs` portant rôle, provenance, **rang de source**, strate, texte,
code, siège, article, subdivision, identifiant Légifrance, note.

**Provenances, alignées sur l'échelle du § 4** : `1 texte_depose` ·
`2 table_ouverts` · `3 depot_droit` · `3bis depot_secondaire` · `4 annexe` ·
`5 amendements_deposes` · `6 rapport_commission` · `0 a_trouver`.

## 12. Contrôler — neuf contrôles, et ils se jouent à chaque relevé

**Ils sont mécaniques et aucun ne demande de jugement.** Ils s'implémentent une
fois, avec leur jeu d'essai ; **une règle implémentée deux fois est deux règles.**

| | ce qu'il vérifie |
|---|---|
| **1** | le vecteur et le véhicule ne se confondent pas — aucune ligne de rattachement en vecteur |
| **2** | l'adresse est décomposée en quatre niveaux, aucun collage |
| **3** | chaque vecteur porte sa provenance, son rang de source et sa date |
| **4** | **la dérivation depuis l'annexe se rejoue et l'écart sort.** C'est le seul contrôle total |
| **5** | une clé qui ne joint rien sort en échec, jamais appariée au plus proche |
| **6** | **deux mesures qui visent la même adresse se signalent.** Deux amendements qui abrogeraient le même article se neutralisent ou se contredisent. **Il est dû sur toute liasse** : une collision trouvée à la main ne se trouve pas deux fois |
| **7** | une mesure dont le seul vecteur est réglementaire sort avec ce motif |
| **8** | **`a_trouver` sans rang atteint est en faute.** Le rang s'écrit ou l'état ne se rend pas |
| **9** | **`inexistant` rendu pour l'intention entière est en faute.** Il se déclare par levier, les quatre balayés. Et **un code posé sans règle de déduction est refusé** |

**Ce que le contrôle ne voit pas, et qui se dit** : si l'article existe encore,
s'il a été recodifié, s'il porte bien ce qu'on croit. D'où la date obligatoire, et
la règle : **un vecteur de plus d'un an se rejoue avant rédaction ; un vecteur qui
sert à un amendement déposé se rejoue la semaine du dépôt.**

---

## La fiche de vecteur — ce que la skill rend

```
Cible          le libellé exact, et sa population
Énoncé         la mesure telle qu'elle a été demandée
Véhicule       donnée du dossier — loi de finances, loi de financement, loi
               ordinaire — ou « non donné ». Il commande la famille de siège,
               les rangs qui répondent et la variante, RIEN D'AUTRE
Lecture        quand l'énoncé est indéterminé : la lecture retenue, celle qui
               a été écartée, et le paramètre choisi faute d'être porté
Gisements      contexte fourni · annexes du texte chargé · recherche publique ·
               référentiel de sièges — DISPONIBLES, chacun « ouvert » ou
               « non ouvert ». Un rôle disponible et non ouvert est un MANQUE
Pièces         les pièces publiques effectivement ouvertes, avec leur adresse
Leviers        les QUATRE, chacun avec ce qu'on y trouve — « rien » compris,
               et son état propre ; hors texte financier, le levier des
               crédits sort « sans objet — véhicule »
Vecteurs       un bloc par vecteur :
                 rôle · code (+ identifiant) · siège · article · subdivision
                 provenance · RANG DE SOURCE · identifiant Légifrance ·
                 relevé le · requête
                 règle de déduction du code, ou « indéterminé »
Variante       absolu · article_ouvert · a_determiner — et, si la table des
               articles ouverts n'est pas disponible, la dégradation déclarée ;
               hors texte en discussion, `absolu` de régime normal
Ouvertures     la carte des points d'accroche, classée par coût d'immixtion,
               et le rang retenu justifié
Substitution   « variante — levier substitué », et en quoi elle diffère
Jambe          quand la ligne sort du domaine : le véhicule réel, et le levier
               portable ici s'il en existe un
Collisions     les mesures qui visent déjà la même adresse (contrôle 6)
Réserves       partie réglementaire, loi et code concurrents, vecteur périmé,
               catégorie qui capte plus large que l'énoncé, verbatim de rang
               3 bis
État           par levier : trouve · a_trouver · inexistant · sans_objet ·
               siege_non_codifie · hors_perimetre
```

## Ce que l'épreuve a mesuré, et ce qu'elle dit de se méfier

Éprouvée sur un lot de référence de 36 amendements réellement déposés, en aveugle
sur l'exposé sommaire seul, **à blanc** : **22 cas, 14 concordances — 63,6 % —,
8 voisinages, zéro discordance.** Aucune adresse n'a envoyé l'amendement au mauvais
endroit.

**Les trois manques disent où se méfier**, et ils tiennent tous à l'étape 1 : un
levier confondu avec un autre sur une dépense d'obligation, un siège cherché dans
un code quand il était dans une loi de finances antérieure, un crédit d'impôt
déclaré sans siège alors qu'il en avait un. **Le taux chute là où le statut de la
dépense n'a pas été qualifié d'abord.**

**Ce qu'un second lot a ajouté** : le taux ne chute pas seulement là. Il chute
aussi là où l'étape s'est arrêtée au deuxième rang de l'échelle des sources, là où
elle a conclu à l'inexistence sans balayer les quatre leviers, et là où elle a
traité un texte hors périmètre comme une adresse fausse.

**Et ce que l'épreuve n'a PAS mesuré se déclare** : les deux lots de référence sont
des amendements de loi de finances. **Aucun taux n'est établi pour la loi de
financement ni pour la loi ordinaire** — la méthode y est la même, sa performance
y est inconnue, et un relevé rendu sur ces deux véhicules le dit.

## Les interdits

- **Aucun vecteur ne s'invente et aucun trou ne se comble.** Un vecteur
  vraisemblable est plus dangereux qu'un vecteur absent.
- **Ne jamais rendre le texte d'un article.** L'adresse, l'identifiant, la date.
- **Ne jamais nommer un véhicule comme vecteur** d'une mesure codifiée. « Loi de
  finances » n'est pas une adresse de droit.
- **Ne jamais déduire le véhicule de l'adresse trouvée.** Le véhicule est une
  donnée du dossier, et sa détermination appartient au test de rattachement.
- **Ne jamais apparier une clé au plus proche.** Échec déclaré, arbitrage à la
  main.
- **Ne jamais présenter un vecteur non vérifié comme relevé.** La provenance, le
  rang et la date sont obligatoires.
- **Ne jamais citer un verbatim de rang 3 bis comme une preuve de version.**
- **Ne jamais rendre `a_trouver` sans avoir descendu les six rangs**, ni
  `inexistant` sans avoir balayé les quatre leviers. Un rang sans objet pour le
  véhicule se déclare, il ne se compte pas comme descendu.
- **Ne jamais rédiger un énoncé qui ne porte aucune direction.** Le sens ne
  s'invente pas — et une direction sans dispositif se rédige à la lecture la plus
  étroite, déclarée.
- **Ne jamais lever sur un texte hors périmètre.** On ajoute et on rejoue.
- **Ne jamais opposer le mode à blanc à la recherche publique.** À blanc retire la
  valise, pas les pièces publiques.