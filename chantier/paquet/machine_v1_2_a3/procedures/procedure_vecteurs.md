# Procédure des vecteurs — comment on trouve le siège juridique, et comment on le contrôle

*Écrite le 20260831, éprouvée le même jour sur un lot réel de onze organismes.
Elle répond à deux questions : **quand** on cherche un vecteur, et **comment**
on garantit qu'il est juste.*

Elle se lit avec `procedures/test_rattachement.md`, qui dit si la mesure peut
voyager.

---

## Ce qu'on cherche, et ce qu'on ne cherche pas

**Le vecteur est un identifiant, jamais du verbatim.** « Article L. 131-3 du
code de l'environnement » est une adresse ; le texte de cet article est autre
chose.

C'est ce qui rend la recherche web légitime ici, et c'est une décision antérieure lue jusqu'au
bout : l'outil de récupération passe par un modèle, **il repère, il ne copie
pas**. Chercher une adresse est du repérage. Le jour où il faudra le texte —
pour le trois colonnes, pour une disposition modificative rédigée —, il entrera
par pièce jointe et pas autrement.

**Corollaire d'atelier, vérifié** : le shell de l'atelier n'atteint ni
Légifrance ni un moteur de recherche — la passerelle n'admet que les registres
de paquets. La recherche se fait donc par l'outil du fil, jamais par
script. **Un script ne trouvera jamais un vecteur ; il ne fait que dériver,
joindre et contrôler.**

---

## Où le chercher — trois sources, par ordre de coût croissant

**1. L'annexe budgétaire, quand elle le porte.** L'annexe des dépenses fiscales
nomme, pour chacune des 465, l'article du code et la norme de référence à
laquelle elle déroge. **Ce lot ne se cherche pas : il se dérive**, par
script, et il se revérifie à chaque régénération sans réseau.

**2. Vos pièces de référence, quand elles le portent.** Un récapitulatif de transposabilité
donne le vecteur article par article pour 59 mesures de l'axe du consentement.
Le champ `droit_existant` de votre référentiel de positions en donne un indice pour 10
propositions sur 56 — **un indice de siège, pas un vecteur** : il nomme le
texte, rarement l'article.

**3. Légifrance, pour tout le reste.** Une recherche par cible.

---

## La recherche, pas à pas

**La requête type** : le nom exact de l'organisme ou du dispositif, plus le code
présumé, plus un numéro d'article présumé. Le domaine est restreint à
`legifrance.gouv.fr`. Le numéro présumé peut être faux : il sert d'amorce, la
réponse le corrige.

**Ce qui fait une bonne réponse, et c'est le point qui rend l'exercice fiable** :
**le titre de section de Légifrance nomme lui-même la cible.** « Section 3 :
France compétences », « Chapitre V : Impositions affectées au Centre national du
cinéma et de l'image animée et perçues par lui ». Quand le titre porte le nom,
la fourchette d'articles qui le suit est le vecteur, et il n'y a rien à
interpréter.

**Ce qu'on retient** : le code ou le texte, la fourchette d'articles,
l'identifiant Légifrance — `LEGISCTA…`, `LEGIARTI…`, `JORFTEXT…`, douze chiffres
—, et la date du relevé.

### Les quatre pièges, tous rencontrés au lot pilote

**Un organisme a souvent deux vecteurs, et l'économie porte sur le second.** Les
agences de l'eau sont créées par une section du code de l'environnement et
financées par une autre. **Supprimer l'organisme et supprimer sa ressource ne se
font pas au même endroit**, et une mesure d'économie vise presque toujours le
financement. Chaque vecteur déclare donc son **rôle** — création, financement,
compétence, montant, dérogation.

**La partie réglementaire ne sert à rien.** L'AFITF a un décret fondateur et des
articles du code des transports ; seule la partie législative est à portée d'un
amendement. Le contrôle `N7` sort les mesures dont le seul vecteur est
réglementaire.

**La loi codifiée et le code disent la même chose deux fois.** L'ADEME a sa loi
de 1990 et ses articles du code de l'environnement. Abroger la loi ou abroger
les articles n'est pas équivalent, et le choix s'instruit — le relevé porte les
deux.

**Une ligne d'économie n'est pas toujours un organisme.** « CCI et chambres
d'agriculture » est une ligne, et ce sont **deux vecteurs** dans deux sections
différentes du code général des impôts. Inversement, les 34 établissements
publics fonciers tiennent dans **un seul** article — c'est ce qui rend cette
ligne bon marché.

---

## Ce qu'on écrit

Les vecteurs relevés à la main vivent dans un fichier de relevé dédié, jamais dans
le référentiel produit — même dispositif que `sources_chiffres.py`. Une entrée
par cible :

```
cle          le libellé EXACT du socle. C'est la clé de jointure, et elle ne
             se normalise pas : une clé qui ne joint aucune ligne sort en
             échec, elle ne s'apparie pas au plus proche.
population   operateur · odac_odal · taxe_affectee · proposition
releve_le    la date. Un vecteur vieillit.
requete      ce qui a été cherché, pour que le relevé se rejoue.
vecteurs     un ou plusieurs, chacun : rôle, provenance, strate, texte,
             articles, identifiant Légifrance, note.
```

**Quatre provenances, et une seule est mécanique** — c'est le dispositif des
niveaux de confiance de vos chiffres sourcés, appliqué au droit :

| | provenance | ce qu'elle dit |
|---|---|---|
| 3 | `annexe` | dérivé d'une annexe importée au socle. Se revérifie sans réseau. |
| 2 | `legifrance` | relevé par recherche, identifiant et date portés. Se recontrôle sur pièce. |
| 1 | `documentation` | porté par une pièce de votre documentation de travail. |
| 0 | `a_trouver` | pas de vecteur. **Ce n'est pas un défaut tant que c'est dit.** |

**Aucun vecteur ne s'invente et aucun trou ne se comble.** Un vecteur
vraisemblable est plus dangereux qu'un vecteur absent : il a l'apparence d'une
adresse et il envoie l'amendement au mauvais endroit — c'est une règle antérieure transposée du
chiffrage au droit.

---

## Les huit contrôles, et ce qu'ils ne voient pas

Un script de contrôle de norme.

| | ce qu'il vérifie | rang |
|---|---|---|
| `N1` | un vecteur codifié nomme un texte de droit, pas un véhicule | échec |
| `N2` | la référence d'article a une forme reconnue | échec |
| `N3` | un relevé Légifrance porte son identifiant et sa date | échec |
| `N4` | les vecteurs dérivés de l'annexe s'y retrouvent, rejoués | échec |
| `N5` | l'état déclaré concorde avec ce que l'entrée porte | échec |
| `N6` | deux mesures ne visent pas le même article | signalement |
| `N7` | un vecteur seulement réglementaire n'est pas amendable | signalement |
| `N8` | la couverture par population se dit | compte |

**`N4` est le seul contrôle total.** Il rejoue la dérivation depuis le socle et
compare : si l'annexe change au millésime suivant, l'écart sort.

**`N1` est le contrôle qu'une décision antérieure demande** : il refuse qu'une entrée porte « loi
de finances » comme vecteur d'une mesure codifiée. Le véhicule et le vecteur ne
se confondent jamais.

**`N6` a déjà trouvé quelque chose** : 55 articles du code général des impôts
sont visés par plus d'une dépense fiscale. Deux amendements qui abrogeraient le
même article se neutralisent ou se contredisent. **C'est exactement le risque
que la colonne vecteur est faite pour voir**, et aucune lecture par mesure ne
l'aurait montré.

**Ce que le contrôle ne peut pas voir, et qui se dit** : si l'article existe
encore, s'il a été recodifié, s'il porte bien ce qu'on croit. Cela se vérifie
sur pièce. La date du relevé est là pour dire quand cela a été fait, et un
vecteur de plus d'un an se rejoue avant rédaction.

---

## Le plan par étapes

**Le coût est mesuré, pas estimé.** Le lot pilote a demandé **une recherche par
cible, onze cibles, onze réponses au premier essai**, et il a rendu **dix-huit
vecteurs** — 1,6 par cible, parce qu'un organisme en a souvent deux.

### Étape 0 — faite le 20260831

Le référentiel des normes existe : **1 856 entrées, 621 vecteurs déclarés.**

- **465 dépenses fiscales** — vecteur dérivé de l'annexe, 100 %.
- **128 programmes** — vecteur unique et connu d'avance, l'état B.
- **11 organismes** relevés sur Légifrance : ils couvrent **les 11 lignes
  d'économie d'opérateur qui nomment une cible, soit 22,7 Md€**. La douzième est
  le résidu « autres », 2,8 Md€, qui n'a pas d'assiette nommée et ne peut donc
  pas avoir de vecteur.
- **10 propositions** portent un indice de siège.

### Étape 1 — les 20 dépenses fiscales dont la référence n'est pas exploitable

`N2` sort **31 dépenses fiscales sur 465 dont la référence de l'annexe n'est pas
une adresse d'article** : un renvoi à une doctrine administrative (`BOI-…`,
`DB…`), une mention d'alinéa, ou du texte libre dans la cellule. **20 d'entre
elles portent un régime de suppression, pour 4,25 Md€.**

C'est le lot le plus rentable qui reste : 20 recherches, et le lot V2 passe de
93 % à 100 % d'adresses exploitables.

### Étape 2 — les taxes affectées du régime « Oui »

87 taxes — 76 en régime `Oui`, 11 en `Flux OM` — soit le lot PLF utile. Les 86
du régime `Collocs` et les 52 du régime `Sécu` sont deux lots à part : les
premières relèvent d'une porte établie mais d'un arbitrage ouvert, les secondes
du PLFSS et attendent leur tour.

*Économie probable* : plusieurs taxes partagent leur section — les neuf du CNC
tiennent dans un chapitre, les 34 des établissements fonciers dans un article.
**Le compte de recherches est inférieur au compte de taxes**, et de beaucoup.

### Étape 3 — les organismes, par montant et non par ordre alphabétique

424 organismes portent un régime de suppression, d'internalisation ou de vente.
**On ne les prend pas dans l'ordre de la liste : on les prend par ce qu'ils
débloquent.** Les 11 qui portent une ligne d'économie sont faits. Restent 55
opérateurs en suppression, puis 233 ODAC-ODAL.

Lots de 25 à 30 cibles par fil, soit une dizaine de fils. **C'est le poste le
plus lourd du chantier, et il ne se compresse pas** — mais il est parallélisable
et il ne bloque rien d'autre.

### Étape 4 — les propositions

Les 44 propositions arrêtées. Les 12 esquissées attendent que leur norme cible
soit écrite : **chercher un vecteur sous une norme non arrêtée, c'est le
chercher deux fois.**

Le récapitulatif de transposabilité couvre déjà l'axe du consentement. **Ce qui
s'en reprend et que le référentiel des normes ne prévoit pas encore : la colonne repli**, avec
son écart déclaré. Un vecteur inexistant appelle un repli, pas un abandon.

---

## Ce qui périme, et quand on rejoue

**Un vecteur dérivé de l'annexe se rejoue à chaque millésime**, et `N4` sort
l'écart tout seul.

**Un vecteur relevé sur Légifrance périme en silence.** Un texte se modifie, se
recodifie, s'abroge. Rien ici ne le voit — c'est pourquoi la date du relevé est
obligatoire. **Règle : un vecteur de plus d'un an se rejoue avant rédaction**,
et un vecteur qui sert à un amendement déposé se rejoue la semaine du dépôt.

---

## Ce qui reste à l'utilisateur

1. **Combien d'abrogations pour 424 organismes.** Une par organisme, une
   disposition de portée générale renvoyant à une liste annexée, ou un lot
   restreint et exemplaire. C'est ce qui décide du poids réel de l'étape 3, et
   ce n'est pas une question technique.
2. **Le contre-budget 2026 d'un déposant** — quand et comment le
   mobiliser. S'il porte des amendements de crédits déjà rédigés, il donne le
   gabarit de l'exposé sommaire et l'ordre de grandeur des baisses, et l'étape
   des crédits en sort accélérée. *Il n'est pas joint ; il entre par pièce
   jointe.*
3. **La révision du code général des impôts préparée par l'expert.** La question
   qu'on lui pose a changé : les vecteurs des niches sont connus, elle est
   précieuse sur les articles que la fiscalité à quatre impôts réécrit et qui ne
   sont pas des dépenses fiscales.
4. **Abroger la loi fondatrice ou les articles du code**, quand un organisme
   porte les deux. Le relevé porte les deux et ne choisit pas.
