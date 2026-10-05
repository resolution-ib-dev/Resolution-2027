# Le dépôt de droit — comment obtenir le texte en vigueur

Ce document explique comment lire le droit applicable hors ligne, sans dépendre
d'un accès direct à Légifrance.

Il répond à un blocage constaté et mesuré : la lecture directe de Légifrance
depuis une session de travail échoue le plus souvent — neuf tentatives, un
succès et huit `403`, sur `/codes/article_lc/`, `/codes/section_lc/` et
`/loda/id/`, retestées à dix minutes d'intervalle. Le collage manuel est le seul
repli si l'on s'en tient à ce canal.

## Le principe

**Le droit est une source déclarée, jamais un fetch.** Un dépôt GitHub public
porte les codes utiles, extraits de la base LEGI de la DILA par une action
programmée. Vous le clonez et vous lisez hors ligne.

**Aucune clé, aucun compte, aucun quota, aucune autorisation** : LEGI est
publiée en open data et le dépôt est public en lecture. Un `git clone` suffit,
depuis n'importe quelle machine.

**Adresse** : `https://github.com/resolution-ib-dev/Resolution-2027`.

Le dépôt est en lecture seule pour vous : vous le clonez, vous n'y écrivez pas.

## Ce que le dépôt contient

| pièce | rôle |
|---|---|
| `codes.json` | les codes portés, un `LEGITEXT` et un article témoin par ligne. Seul lieu où l'on ajoute un code. |
| `extraire_legi.py` | tourne dans l'action programmée. Découvre l'archive par l'index de la DILA, applique la base complète puis toutes les journalières postérieures, écrit un `jsonl.gz` par code. |
| `droit.py` | le lecteur : un article, une recherche par section, un contrôle de lot. |
| ~~`coordination.py`~~ | **n'existe pas au dépôt.** Voir la section « Les renvois entrants » plus bas : l'étape est écrite, rien ne la joue. |
| `.github/workflows/rafraichir.yml` | à la main, le 1er de chaque mois, et à toute modification de `codes.json` ou de l'extracteur. |
| `essai.py` | épreuve à blanc, douze contrôles, sans réseau. |

## Emploi

**Le clonage et le rafraîchissement ne sont pas des gestes manuels.** Ils sont
dans la chaîne, et une seule commande les porte :

```
python3 appareil/installer_droit.py
```

Elle clone si le dépôt est absent, met à niveau s'il est là, lit le millésime de
la base **dans le manifeste de l'extrait et jamais à l'horloge**, et rend
`FRAIS` ou `PERIME`. Sur `PERIME` elle tente le rafraîchissement ; s'il
n'aboutit pas, elle sort en erreur, écrit `BULLETIN_DROIT.json` et dépose un
marqueur `EXTRAIT_PERIME` dans le clone. Rien n'échoue en silence, et rien ne
porte la date du jour qui ne vienne de l'extrait.

Ce qui suit reste vrai et sert à la lecture, une fois le clone en place :

```
git clone https://github.com/resolution-ib-dev/Resolution-2027 droit
python3 droit/droit.py etat
python3 droit/droit.py article "code général des impôts" 279
python3 droit/droit.py verifier mes_vecteurs.json
python3 droit/coordination.py cgi 279 --tout
```

Depuis un script : `droit.article(code, num)` puis `droit.rendre(a)` ;
`coordination.entrants(code, num)` rend les renvois.

## L'état de l'extrait — mesuré au dépôt le 3 octobre 2026

**62 entrées déclarées à `codes.json`**, et elles se répartissent en codes et en
textes non codifiés consolidés.

| | octets |
|---|---|
| extraits de codes déclarés et lisibles | 37 445 310 |
| extraits de textes non codifiés déclarés | 1 935 838 |
| tous les extraits du dossier `data/` | 40 155 084 |

**La liste des codes portés ne se recopie pas : elle se lit dans
`codes.json`.** C'est le seul endroit où l'on ajoute un code, donc le seul où
l'on en lit la liste. Une version antérieure de ce document annonçait « vingt
codes, 21 Mo » : la borne avait été recopiée d'un millésime à l'autre sans être
vérifiée, et elle était fausse de moitié. Une borne se vérifie avant d'être
redite.

**Ajouter un code est une ligne dans `codes.json`** : le balayage lit l'archive
entière dans tous les cas, un code de plus coûte quelques mégaoctets et zéro
minute.

**Onze extraits du dossier `data/` ne sont déclarés ni à `codes.json` ni au
manifeste**, dont quatre codes. `droit.py` les refuse — « code inconnu ». Ce
sont des restes d'un millésime antérieur. Un article qu'on y chercherait n'est
pas introuvable : il est non déclaré, ce qui n'est pas la même chose et se
corrige par une ligne à `codes.json`.

## Ce qui ne tient pas dans un projet, et pourquoi

Les extraits sont du **gzip binaire**. Le seul code général des impôts fait
10 870 869 octets une fois ouvert ; l'ensemble est de l'ordre de plusieurs
centaines de mégaoctets. Les connaissances d'un projet se comptent en
mégaoctets de texte.

**Conséquence, et elle commande la forme de tout ce paquet** : le droit ne
s'atteint pas en versant le dépôt dans les connaissances d'un projet, ni en
pièce jointe. Il s'atteint depuis une session qui dispose d'un interpréteur —
une tâche Cowork, une session de code. C'est là que la chaîne se conduit, et
c'est pour cela que le mode d'emploi s'adresse à quelqu'un qui y travaille.

## Les quatre refus, tenus par le code

- Aucun article ne sort sans son identifiant `LEGIARTI` et sa date de version.
- Un article sans version applicable lève, avec ses états — il ne rend pas son texte.
- Un article absent lève. **Jamais d'appariement au plus proche.**
- Un code non porté lève en nommant les codes portés — il ne se confond pas avec
  un article périmé.

## La fraîcheur — péremption à 45 jours

Le millésime LEGI est porté dans chaque sortie. **Au-delà de 45 jours, la
mention `À REJOUER` s'imprime** : l'extrait n'est plus fiable, le droit a pu
changer depuis.

**Ce qui se fait alors, et ce n'est plus à vous de le déclencher** :
`appareil/installer_droit.py` tente le rafraîchissement de lui-même, dans cet
ordre et en le disant à chaque fois.

| ce qui est tenté | ce qui se passe si ça ne répond pas |
|---|---|
| mise à niveau du clone depuis le dépôt public | le clone local est conservé **et le repli est nommé** — « le dépôt n'a pas répondu » —, jamais pris pour une mise à niveau réussie |
| rejeu de l'extraction depuis la source officielle | le module **sort en erreur** (code 5), écrit `BULLETIN_DROIT.json` et dépose `EXTRAIT_PERIME` dans le clone |

**Le repli documenté, quand les deux échouent** : l'action programmée du dépôt
rejoue l'extraction le 1er de chaque mois. Relancez le module après son passage,
ou reclonez. **Rien n'autorise à rédiger entre-temps**, et le marqueur est là
pour buter dessus même si personne n'a lu la console.

Un extrait périmé ne s'utilise pas : il donne un texte qui n'est plus celui en
vigueur, sans le dire autrement que par cette mention.

**Le pire cas, et il est interdit par le code.** Un extrait arrêté en amont et
estampillé du millésime du jour se lit frais, il est faux, et rien ne le
signale. Le millésime se lit donc dans le manifeste de l'extrait, à défaut dans
la sortie de `droit.py etat`, et **nulle part ailleurs** : le module refuse une
date qui viendrait de l'horloge plutôt que de l'extrait, et s'arrête (code 4)
quand il ne peut lire aucune des deux. Il ne devine pas.

## L'historique récent — la colonne A d'un texte déjà modifié

**Le piège.** Il ne suffit pas de garder ce qui s'applique aujourd'hui. Un
rédacteur a besoin du texte **tel qu'il était quand le texte en discussion a été
écrit**. Un projet de loi de finances déposé en octobre modifie des articles
que la loi promulguée en décembre a déjà changés : au millésime courant,
l'article porte le **résultat** de la modification et non son point de départ.
La colonne A d'un trois colonnes est alors fausse sur tout article que le texte
a touché — et le trou est invisible.

Mesuré sur un relevé d'adresses d'un texte déposé, contre un extrait postérieur :
la moitié environ des adresses étaient en version postérieure au dépôt, et
l'extrait donnait C là où le rédacteur attendait A.

**Ce que l'extrait fait.** `extraire_legi.py` garde toute version qui a cessé de
s'appliquer **après un plancher** — `2025-01-01` par défaut,
`PLANCHER_HISTORIQUE` pour le déplacer —, et le manifeste porte le plancher et,
par code, le compte des versions historiques. Au-delà du plancher, l'historique
ne sert plus et il multiplierait le dépôt. `droit.py` lit à une date par
`article … --au AAAA-MM-JJ`, ou `droit.article(code, num, jour="…")` depuis un
script. `essai.py` porte douze contrôles sans réseau : la version d'alors sort
au lieu de celle d'aujourd'hui, et le plancher garde après lui, jette avant.

**La voie à ne pas prendre, et qui est fausse** : reconstruire A en défaisant la
disposition sur le texte actuel. Le droit en vigueur porte l'effet de la loi
**adoptée**, amendements compris, et non l'effet de la disposition déposée :
deux inconnues, pas une. Une méthode qui tombe juste une fois n'est pas une
méthode.

## L'applicabilité se lit aux dates, jamais à l'état LEGI

**C'est l'intervalle de dates qui décide.** `ABROGE_DIFF` marque une version qui
s'applique aujourd'hui et dont l'abrogation est déjà votée. Filtrer sur
`VIGUEUR` fait disparaître l'article 279 du code général des impôts et tout le
bloc TVA, sans un message.

Le CGI porte **376 articles applicables à fin programmée**, le CIBS **282** : la
recodification fiscale est en cours. Le lecteur sort l'avertissement de
lui-même, et une version future est refusée avec sa date d'entrée en vigueur
plutôt que rendue comme du droit applicable.

## Le témoin, et pourquoi il existe

Chaque code déclare un article qu'il doit porter. Son absence **fait échouer
l'extraction** plutôt que de livrer un code amputé. Le manifeste porte, par
code, **dix articles dont l'applicabilité est prouvée par l'extrait** :
épingler un témoin ne demande pas d'aller sur le web.

**Le code des douanes est à témoin non épinglé** — son contrôle est en veille,
le manifeste le déclare, et `266 sexies` est le candidat relevé.

## Les renvois entrants — **écrits, non outillés**

**`coordination.py` n'existe pas au dépôt.** Mesuré le 3 octobre 2026 : le
fichier n'est dans aucune branche. Ce document l'a présenté comme une pièce
livrée ; il ne l'était pas, et une étape documentée qui ne tourne pas est pire
qu'une étape déclarée manquante.

Ce qui suit décrit donc **ce que les renvois entrants exigent de vous**, et se
conduit à la main.

Un renvoi entrant est un article applicable qui cite l'adresse qu'on s'apprête à
modifier. C'est un trou que la recherche de vecteur ne comble pas : elle voit
deux mesures qui visent la même adresse, elle ne voit pas les articles qui
citent la vôtre.

**À la main, sans outil dédié** : on cherche la référence de l'article visé dans
les extraits des codes portés. Le relevé est incomplet par construction, et il
se déclare comme tel.

**Amendement — service minimum.** On ne coordonne pas, on **signale** : les
renvois relevés se listent **en fin d'exposé sommaire**. Le maquis des renvois
ne doit pas bloquer la production.

**Proposition de loi — la boucle va jusqu'au bout.** Chaque renvoi se traite ou
se déclare sans objet avant dépôt. C'est un travail lourd, assumé comme tel.

Chaque renvoi porte sa **certitude**, fixée par une règle de déduction et non
par une impression : `nomme` quand la phrase nomme le code visé ; `interne`
quand l'article citant est dans le même code et qu'aucun autre n'est nommé ;
`ambigu` pour une citation nue depuis un autre code, à qualifier à la main.

*Mesuré à l'époque où l'outil existait : abroger l'article 279 du CGI touche
quatre articles applicables ; abroger `L. 3262-1` du code du travail en touche
neuf, dont cinq au code de l'éducation, invisibles depuis le code du travail
seul. Ces deux chiffres disent l'ordre de grandeur du trou, pas l'état de
l'outillage.*

**Ce que vous devez en retenir, concrètement.** Sur un amendement, un relevé de
renvois absent ou partiel ne bloque pas le dépôt : il se déclare en fin
d'exposé sommaire, ou l'exposé ne porte pas de liste. Sur une proposition de
loi, où chaque renvoi doit être traité ou déclaré sans objet avant dépôt,
l'absence d'outil est une charge de travail réelle et il faut la prévoir.

## Ce qui n'est pas couvert, et qui se dit

**Le droit non codifié.** Un renvoi porté par une loi non codifiée n'est pas vu,
et un siège dans une loi de finances antérieure n'est pas dans l'extrait. Les
textes non codifiés consolidés entrent par le même mécanisme — une ligne dans
`codes.json` avec leur `LEGITEXT` — mais **ce n'est pas éprouvé**. C'est la voie
vers des sièges comme l'article 179 de la loi de finances pour 2020, qu'une
recherche de vecteur ne trouve pas sans cela.

**Le texte déposé du PLF et du PLFSS** n'est pas ici : c'est une autre source.

Ni jurisprudence, ni doctrine, ni réglementaire hors codes. Ni l'API PISTE, qui
demanderait un compte et deux secrets pour un service que LEGI rend sans clé.
