# Où le travail vit, et comment il se transmet

Ce document répond à deux questions qui ont coûté cher : **où** le corpus
survit entre deux sessions, et **comment** un renvoi trouve son fichier. Il se
lit en ouverture de session, avec `CLAUDE.md` et `methode/journal.md`.

---

## 1. Trois lieux, trois rôles

| lieu | rôle | qui déplace | persistance |
|---|---|---|---|
| **Le conteneur de session** | l'atelier — on y exécute `make`, `git`, les générateurs | personne, tout y est déjà | **éphémère** : réclamé après inactivité |
| **Le projet Claude** | le coffre — le corpus vivant y est versé sous ses chemins canoniques | Claude, par appel d'outil | permanente, visible dans toutes les conversations du projet |
| **Les fichiers du projet** | l'archive froide — classeurs, PDF, protos gelés | l'auteur, à l'occasion | permanente |

**Les deux lieux permanents ne se voient pas au même endroit, et c'est la
source d'erreur numéro un.** Le **coffre** est ce que Claude verse : il est
rangé en dossiers — `methode/`, `reference/`, `input/`… — et il compte dans le
budget de connaissance. Les **pièces jointes** sont ce que l'auteur dépose :
classeurs, PDF, image ; elles forment une liste plate, ne comptent pas dans le
budget, et Claude ne peut ni les ranger ni les supprimer. Une même pièce peut
donc exister d'un côté et pas de l'autre, **ou de ni l'un ni l'autre** :
`input/NL_cba-guidance.pdf` a été au coffre du 20260821 au 20260901 sans jamais
être une pièce jointe, et au 20260902 il n'est plus ni au coffre ni aux pièces
jointes — l'index le déclarait encore, et c'est la confrontation d'inventaire qui
l'a sorti (A-289). **Une session qui dit où est une pièce dit toujours dans
lequel des deux lieux, et depuis quand.**

**Aucun échange de fichiers n'incombe à l'auteur.** Le coffre se lit et s'écrit
par Claude. L'auteur n'ouvre une session que pour dire ce qu'il veut fait.

Ce qui suit du choix du coffre, et qu'il faut tenir pour vrai :

- **Le coffre ne porte que le corpus vivant qui n'est pas au dépôt** —
  manuscrit, méthode, références, sources gelées. L'appareil et les trois
  référentiels JSON sont au dépôt depuis le 20260909 (A-395). Les dérivés de
  `livrables/` ne se versent nulle part : ils se régénèrent par `make`. Verser
  un dérivé, c'est créer une seconde vérité.
- **Le coffre ne porte pas `.git`.** L'historique fin vit dans le conteneur le
  temps de la session, et le récit de ce qui a changé vit dans
  `methode/journal.md`, qui est au coffre. Une session nouvelle hérite de l'état
  et du récit, pas des diffs.
- **Le budget du coffre est borné** à 2 000 000 de jetons de connaissance
  indexée, et **il se lit à `project_info`, dans son unité, jamais converti en
  octets** (A-312). Relevé le 20260909 après le versement de l'appareil au
  dépôt : **1 377 172 sur 2 000 000, marge 622 828**. Toute nouvelle version
  remplace la précédente au même chemin, mais **elle n'est pas créditée de la
  place que l'ancienne libère** : une grosse pièce se supprime avant de se
  réécrire.

---

## 2. Comment le coffre est rangé

**Le coffre est aussi la vue de l'auteur sur son projet.** Il y est donc rangé
par dossiers, et l'auteur n'y voit que ce qu'il peut ouvrir.

| dossier | quoi | combien |
|---|---|---|
| `manuscrit/` | la strate 1 | 1 |
| `methode/` | règles, contrats, index, journal, registre des sas | 22 |
| `livrables/` | les produits qu'il lit — l'extrait, la carte, la galerie, l'état des vecteurs | 4 |
| `livrables/eval_gl/` | **hors règle** — réponses d'éval, que seule la machine lit | 2 |
| `reference/` | textes normatifs en vigueur, mises en forme, digestions | 9 |
| `archive/` | nos sorties gelées, antérieures aux gabarits | 15 |
| `input/` | documents de l'auteur ou de tiers versés comme documents | 2 |
| `referentiels/` | référentiels lisibles à l'œil, en TSV | 2 |
| racine | `CLAUDE.md`, `racine/DEMARRAGE.md` | 2 |

**`technique/` n'existe plus.** Il ne portait qu'une pièce, `technique/coffre.txt`,
l'archive opaque de l'appareil. Elle a été versée au dépôt et supprimée du coffre
le 20260909 (A-395), prouvée 80 sur 80 à l'octet.

**Soixante documents au 20260902 au soir, relevés à `project_info` et confrontés
un par un à ce que l'index déclare : 60 pour 60, aucun déclaré et absent, aucun
présent et non déclaré.**

**Ce compte est un contrôle, pas une décoration** : il se confronte à l'état réel
du projet à chaque clôture d'unité de travail, et tout écart se nomme avant de se
corriger. **Il se relève à `project_info`, jamais depuis le dépôt** — A-128 le
pose pour la jauge et cela vaut pour l'inventaire, par la même raison : le coffre
et le dépôt ne portent pas les mêmes choses (A-291). *Aucun script ne sait faire
cette confrontation*, les documents du coffre n'étant pas au dépôt.

*Ce que la confrontation du 20260902 a trouvé, et qui n'était pas su.* **Six
documents étaient au coffre sans être déclarés à l'index** — le registre des sas,
le registre des digestions, la note du dépôt de droit, le prompt de versement du
socle PLFSS, et les deux réponses d'éval de `livrables/eval_gl/`. Cinq ont reçu
leur entrée ; **le prompt de versement a été supprimé**, son fil étant clos et sa
matière portée à `methode/sas.md` (A-292). Et **deux étaient déclarés au coffre
sans y être** : `input/NL_cba-guidance.pdf` et
`input/guide-public-du-budgetaire-2023.pdf`, deux pièces publiques qui l'ont
quitté. Elles rentrent désormais par pièce jointe, et leur digestion reste due
(A-289).

*Ce que le tableau ci-dessus ne compte plus.* Les quatre sas du socle du texte ont
été absorbés et supprimés le 20260902. `referentiels/` porte deux tables plates
depuis que celle du PLFSS est versée.

Le rangement du coffre ne suit pas celui du dépôt :
`sources/` est plat au dépôt, parce que c'est la copie de travail, et rangé au
coffre, parce que c'est la vue. La table de correspondance vit dans
`appareil/generer_index.py` et se lit au champ `chemin_coffre` de l'index.

**La couche technique n'est plus au coffre : elle est au dépôt.** Tout
`appareil/`, les trois référentiels JSON, le `Makefile` et le `.gitignore` — 80
fichiers — vivent à `resolution-ib-dev/Resolution-2027`, branche `main`, sous la
sous-racine `chantier/`. Ils étaient repliés dans une archive unique du coffre
jusqu'au 20260909 ; elle a été versée au dépôt et supprimée après preuve à
l'octet 80 sur 80 (A-395). Le motif du repli tient toujours — l'auteur ne voit au
coffre que ce qu'il peut ouvrir — et le dépôt rend deux services de plus : la
restauration est un `git clone`, donc une copie d'octets sans format maison, et
l'appareil ne pèse plus rien à la jauge. **623 934 jetons rendus.**

**Deux corpus dans un dépôt, deux racines distinctes** : le dépôt de droit à la
racine, l'appareil du chantier sous `chantier/`, chacun avec son propre
`.gitignore`. Ne pas les mêler — celui du chantier ignore `droit/`, et posé à la
racine il masquerait le dépôt de droit tout entier.

**L'écriture au dépôt est fermée depuis Cowork** (A-393) : une pièce de l'appareil
corrigée ici ne peut pas être poussée par le fil qui la corrige. Elle se déclare,
et `appareil/coffre.py dette` dit ce qui est dû — pièces divergentes du clone,
pièces absentes du clone, et pièces de l'appareil encore versées au coffre comme
documents. Le versement passe par une session claude.ai/code, qui pousse et ne
voit pas le coffre (A-394).

**Deux référentiels échappent au dépôt**, et l'exception a sa raison : les tables
plates des articles ouverts, `referentiels/articles_ouverts_plf.tsv` et
`…_plfss.tsv`. Ce sont les seules formes de cette matière qui se lisent sans
outil, par l'auteur comme par les fils aval — c'est le critère d'A-16, le même
que pour `livrables/`. Elles sont de rang `derive` et vont au coffre comme
documents. Les JSON équivalents ne se versent pas du tout.

**Quatre pièces de l'appareil sont encore au coffre comme documents, et elles
sont dues au dépôt** : les deux référentiels de rédaction du texte déposé
— 848 ko et 352 ko, environ 360 000 jetons de jauge à rendre — et les deux
modules de la réapplication. Elles n'étaient pas dans l'archive au moment du
versement, donc elles ne sont pas parties avec elle.

Deux artefacts de racine ne peuvent pas porter un nom nu au coffre, qui les
rangerait d'office ailleurs : ils prennent le préfixe `racine/`.

L'index dit tout cela. Le champ **`voie`** donne la surface qui rend l'artefact —
`coffre`, `depot`, `piece_jointe`, `hors_coffre` — et le champ **`chemin_coffre`**
donne où il se lit **sur cette voie** : son propre chemin au coffre, un chemin
préfixé, ou son chemin dans le dépôt sous `chantier/`. Le bloc **`depot`** porte
la commande de clone, la sous-racine, les 80 chemins rendus par le dépôt, et
celles des pièces de l'appareil qui sont encore au coffre. Il remplace l'ancien
bloc `archives`, disparu avec l'archive.

`methode/index.json` est la première chose à lire au coffre : il énumère tout le
reste.

Le reste de `sources/` vit au coffre sous ses noms d'origine, comme fichiers ou
documents versés autrefois : le coffre ne les redouble pas.

Les dix-sept pièces jointes du projet — classeurs, PDF, page de garde — ne sont
pas rangeables : Claude ne peut ni les déplacer, ni les renommer, ni les
supprimer. Elles restent une liste plate, et seule la carte du projet leur donne
un ordre logique. **Relevées à `project_info` le 20260902 : dix-sept, le compte
tient.**

---

## 3. Ouverture de session

Une phrase de l'auteur suffit : *reprends le chantier*. Ce que Claude fait
alors, dans cet ordre, sans rien demander :

1. Lire `methode/index.json` au coffre, puis le restaurer par
   `appareil/restaurer.py amorce .` — c'est l'amorce, et la seule pièce dont la
   voie soit connue sans consulter l'index.
2. **Cloner le dépôt**, qui rend les 80 pièces de voie `depot` par copie
   d'octets :

   ```
   git clone https://github.com/resolution-ib-dev/Resolution-2027 droit
   cp -r droit/chantier/. .
   ```

   Puis `appareil/restaurer.py ../methode/index.json ..` pour les artefacts de
   voie `coffre`, de leur `chemin_coffre` vers leur `chemin`. **Il n'y a plus
   d'archive à déplier** (A-395) : `coffre.py deplier` ne sert qu'à relire une
   archive au vieux format si une session en récupère une.
3. Confronter les pièces jointes du projet aux inputs que l'index déclare, et
   signaler toute dérive — une pièce nouvelle, absente ou renommée. Aucun script
   ne peut le faire : les pièces jointes ne sont pas dans le dépôt.
4. `make restauration` — chaque pièce restaurée comparée à son empreinte, sur
   les deux voies. **On s'arrête sur un R1.**
5. `git init` et premier commit de l'état reçu, pour que tout écart de la
   session soit lisible en `git diff`.
6. `make index` — la concordance entre l'arborescence, l'index et la règle de
   nommage.
7. `make controle` — les contrôles de fond, qui ne produisent rien.
8. `make etat` — le compte des apports rédigés.
9. Lire `CLAUDE.md`, `methode/localisation.md`, `methode/journal.md`,
   `methode/prompt_fil_courant.md`.
10. Rendre l'état en quelques lignes, et attendre.

Rien n'est généré à l'ouverture. Un `make` qui régénère un livrable avant que
l'auteur ait dit sur quoi on travaille est une faute.

**Les deux voies se contrôlent à l'octet, et aucune ne passe par le modèle.** Le
clone du dépôt est une copie d'octets par construction. Les documents du coffre
reviennent du transcript de session, qui porte leur texte verbatim, et se
comparent à `methode/empreintes.json`. Ce qui passerait par le modèle normalise
sans le dire : constaté le 20260821, cent espaces insécables du manuscrit rendues
en espaces ordinaires, dans les montants et les pourcentages des notes de fin.

**Un document que le coffre rend comme fichier se restaure par `cp`**, et c'est
la première des trois voies de `CLAUDE.md`. Les deux référentiels de rédaction
sont dans ce cas — 848 ko et 352 ko : `restaurer.py` ne moissonne au transcript
que ce qui y revient en texte, et il compte leur absence plutôt que de la taire.

Deux règles en sortent. **Toute pièce restaurée se compare à sa version du coffre
avant d'être employée** — le contrôle est mécanique et se délègue. **Rien de
recopié ne se reverse** : un document que la session n'a pas délibérément modifié
ne repart pas au coffre, faute de quoi la dérive de recopie s'y installe.

---

## 4. Clôture d'une unité de travail

Une unité de travail est close quand une catégorie, un produit ou une tranche
est finie et relue — jamais en cours de route.

1. `make` puis `make controle`, et relecture de la sortie.
2. Commit local. Le message dit ce qui change **au corpus**, pas quels fichiers
   bougent.
3. `appareil/generer_index.py` si un artefact est né, mort ou a changé de rôle.
4. `make coffre`, puis versement de ce qui a bougé et qui porte `coffre` —
   l'archive technique d'un bloc, les documents lisibles un par un.
5. Une ligne au `methode/journal.md` : la date, ce qui a changé, ce qui reste
   ouvert.

Une seule tranche active à la fois. Si le corpus a été modifié ailleurs
entretemps, le dire avant de reprendre.

---

## 5. Les noms, et la fin des horodatages

**Un nom canonique par artefact, aucun horodatage.** `referentiels/REF_doctrine.json`,
jamais `REF_doctrine_20260820_v20.json`. L'historique est porté par git et par
le journal, jamais par le nom du fichier.

La convention horodatée a produit trois maux, tous constatés :

- des consommateurs qui pointent une version périmée — les cinq skills chiffrées
  appellent encore le contrat de projection et les règles de forme en `v1`, quand
  le corpus est en `v2` ;
- des doublons qui survivent à côté de leur remplaçante — le REF en `v19` et en
  `v20`, l'interface en `v9` et en `v10` ;
- des inventaires qui rouillent — l'inventaire à rang de l'état du chantier citait
  six fichiers dans une version que le projet ne portait plus.

`methode/index.json` est la table de résolution. Chaque artefact y porte son
rôle, son chemin unique, son rang, son générateur, ses consommateurs, et **les
noms horodatés qu'il remplace**. Un renvoi ancien résout donc encore, par alias.

L'index est un dérivé : la table curée vit dans `appareil/generer_index.py`, au
même titre que `GROUPES` et `EVENTAIL`. Elle ne se corrige pas dans le JSON.

`appareil/controle_index.py`, joué par `make index`, tient cinq vérifications :
tout chemin déclaré existe, tout fichier est déclaré, aucun nom horodaté ne
subsiste hors de `sources/`, aucun alias n'est revendiqué deux fois, et tout
artefact porte une famille du classement par contenu.

`sources/` est l'exception assumée : une archive est datée par nature, et le nom
d'un document gelé porte le millésime de ce qu'il décompte.

---

## 6. Les manquants déclarés

Un renvoi qui ne résout pas se nomme, il ne se laisse pas mourir en silence. Le
bloc `manquants` de l'index porte aujourd'hui **trois** entrées, dont une grave :

**`releve_affecte`** est cité comme couche de preuve à identifiants `M-nnnn` par
`compatibilite-doctrine`, `contestabilite` et `qa-riposte`. Il n'existe dans
aucun des trois lieux. Tout verdict qui prétend y remonter est invérifiable. Il
se reconstruit depuis `referentiels/notes_manuscrit.json` et le manuscrit, ou il
se retire des trois skills.

Les deux autres — la couverture du livre, une Q&A à statut de référence — sont
documentées à l'index avec leur motif et leur demandeur. **Le guide de
légistique a quitté cette liste** : il n'est pas perdu, il est digéré dans
`sources/structure_ppl.md`, qui en porte l'alias (A-28).

---

## 7. Ce que ce dispositif ne fait pas encore

**Le dossier connecté.** Si l'auteur ouvre l'application Claude de bureau et
connecte le dossier du dépôt, Claude travaille directement sur son disque :
`.git` réel, aucune limite de taille, classeurs inclus. C'est la cible. Le coffre
devient alors le miroir de contrôle, et le disque l'atelier.

**Le dépôt distant.** L'API GitHub est joignable depuis le bac à sable, mais
l'injection d'identifiants échoue et le dépôt n'est pas dans les sources
autorisées de la session. À ne pas retenter sans piste nouvelle : soit une
autorisation GitHub au niveau du compte, soit l'inscription du dépôt aux sources
autorisées.

**Les skills.** Elles sont en lecture seule dans une session. Leurs renvois
périmés se corrigent en les réécrivant et en les livrant à l'auteur, qui les
enregistre une fois. Après quoi elles pointent des rôles stables et ne se
périment plus.
