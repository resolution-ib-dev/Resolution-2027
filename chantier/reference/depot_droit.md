# Le dépôt de droit — comment un fil obtient le texte en vigueur

Écrit le 20260901, **mis à jour le 20260902 : le dépôt est en service, vingt
codes, et il porte la recherche des renvois entrants.**

Il répond au blocage constaté le 20260901 : Légifrance refuse la lecture directe
depuis l'atelier — neuf tentatives, un succès et huit `403`, sur
`/codes/article_lc/`, `/codes/section_lc/` et `/loda/id/`, retestées à dix
minutes d'intervalle. `redaction-legistique` fait pourtant reposer toute son
étape 1 sur ce canal, avec pour seul repli le collage manuel.

## Le principe

**Le droit est une source déclarée de la session, jamais un fetch.** Même forme
qu'A-196 pour le dépôt de publication et qu'A-234 pour le verbatim. Un dépôt
GitHub public porte les codes utiles, extraits de la base LEGI de la DILA par une
action programmée. Chaque fil le clone et lit hors ligne.

Aucune clé, aucun compte, aucun quota : LEGI est publiée en open data.

**Adresse** : `https://github.com/resolution-ib-dev/Resolution-2027`.
Le dépôt est **public en lecture** — un fil le clone sans autorisation. **Écrire
demande qu'il soit déclaré aux sources de la session**, et l'autorisation du
compte n'y suffit pas : le mandataire git refuse d'injecter un jeton pour un
dépôt hors du jeu déclaré, et le refus est explicite — *« not in this session's
authorized repository set »*. Vérifié le 20260904, l'accès accordé par
l'administrateur ne débloque pas le `push` tant que le dépôt n'est pas aux
sources de la session.

## Ce que le dépôt contient

| pièce | rôle |
|---|---|
| `codes.json` | les codes portés, un `LEGITEXT` et un article témoin par ligne. Seul lieu où l'on ajoute un code. |
| `extraire_legi.py` | tourne dans l'action, jamais dans l'atelier. Découvre l'archive par l'index de la DILA, applique la base complète puis toutes les journalières postérieures, écrit un `jsonl.gz` par code. |
| `droit.py` | le lecteur : un article, une recherche par section, un contrôle de lot. |
| `coordination.py` | **les renvois entrants** — qui cite l'article qu'on modifie, à travers les vingt codes. |
| `.github/workflows/rafraichir.yml` | à la main, le 1er de chaque mois, et à toute modification de `codes.json` ou de l'extracteur. |
| `essai.py` | épreuve à blanc, dix contrôles, sans réseau. |

## Emploi depuis un fil

```
git clone https://github.com/resolution-ib-dev/Resolution-2027 droit
python3 droit/droit.py etat
python3 droit/droit.py article "code général des impôts" 279
python3 droit/droit.py verifier mes_vecteurs.json
python3 droit/coordination.py cgi 279 --tout
```

Depuis un script : `droit.article(code, num)` puis `droit.rendre(a)`, qui sort au
gabarit de l'étape 1 de `redaction-legistique` ; `coordination.entrants(code, num)`
rend les renvois.

## L'état au 20260902

**Vingt codes, 21 Mo, millésime LEGI du 1er septembre 2026.** Code général des
impôts · impositions sur les biens et services · sécurité sociale · collectivités
territoriales · travail · construction et habitation · environnement · livre des
procédures fiscales · civil · propriété des personnes publiques · monétaire et
financier · commerce · éducation · action sociale et familles · sport ·
patrimoine · transports · défense · énergie · douanes.

Ils couvrent la table de vérité-terrain de l'appareil d'éval. **Ajouter un code
est une ligne dans `codes.json`** : le balayage lit l'archive entière dans tous
les cas, un code de plus coûte quelques mégaoctets et zéro minute.

## Les quatre refus, tenus par le code

- Aucun article ne sort sans son identifiant `LEGIARTI` et sa date de version.
- Un article sans version applicable lève, avec ses états — il ne rend pas son texte.
- Un article absent lève. **Jamais d'appariement au plus proche** (A-94).
- Un code non porté lève en nommant les codes portés — il ne se confond pas avec
  un article périmé.

S'y ajoute la fraîcheur : le millésime LEGI est porté dans chaque sortie, et
au-delà de 45 jours la mention `À REJOUER` s'imprime. C'est la règle du vecteur
périmé de `vecteur-mesure`, appliquée au texte.

## L'historique récent — la colonne A d'un texte déjà modifié

**Corrigé le 20260904, sur un fait mesuré.** L'extrait ne gardait que ce qui
s'applique et ce qui s'appliquera : *« l'historique périmé ne sert à rien à un
rédacteur d'amendement »*. C'était faux, et le trou était invisible.

Un rédacteur a besoin du texte **tel qu'il était quand le texte en discussion a
été écrit**. Un projet de loi de finances déposé en octobre modifie des articles
que la loi promulguée en décembre a déjà changés : au millésime courant,
l'article porte le **résultat** de la modification et non son point de départ.
La colonne A d'un trois colonnes est alors fausse sur tout article que le texte a
touché.

**Mesuré sur les 552 adresses relevées à la disposition du texte déposé**, contre
l'extrait du 1er septembre 2026 : **274** en version postérieure au 1er janvier
2026 — l'extrait donne C —, 181 absentes ou code non porté, **78 seulement
lisibles telles quelles**, 12 sans texte nommé, 7 fourchettes non dépliées.
Preuve sur pièce : l'insertion de « 235 ter C, » que l'article 3 du texte
prescrit est déjà dans le code ; l'article 39 AH que son article 5 abroge n'y est
plus ; le 5° du 1 de l'article 93 y est déjà à `(Abrogé)`.

**Ce que le correctif fait.** `extraire_legi.py` garde désormais toute version
qui a cessé de s'appliquer **après un plancher** — `2025-01-01` par défaut,
`PLANCHER_HISTORIQUE` pour le déplacer —, et le manifeste porte le plancher et,
par code, le compte des versions historiques. Au-delà du plancher, l'historique
ne sert plus et il multiplierait le dépôt. `droit.py` lit à une date par
`article … --au AAAA-MM-JJ`, ou `droit.article(code, num, jour="…")` depuis un
script ; le lecteur savait déjà le faire, c'est l'extrait qui ne le portait pas.
`essai.py` passe de dix à **douze contrôles**, sans réseau : la version d'alors
sort au lieu de celle d'aujourd'hui, et le plancher garde après lui, jette avant.

**Le correctif est en service depuis le 20260904**, fusionné par la demande de
tirage n° 1 et rejoué par l'action de rafraîchissement. Millésime LEGI 20260903,
plancher au 1er janvier 2025, **9 372 versions historiques** gardées sur vingt
codes. Le manifeste porte `plancher_historique` et, par code, le compte
`historiques`.

**Ce qu'il change, mesuré sur les 552 adresses du texte déposé** : la colonne A
se relève désormais à la date du dépôt sur **337** d'entre elles, contre 78
lisibles telles quelles avant — dont **237 où A diffère du texte actuel**, c'est
à dire les cas que l'ancien extrait rendait faux en silence. Restent 196 adresses
absentes de l'extrait et 19 écartées.

**La voie que le correctif rend inutile, et qui était fausse** : reconstruire A
en défaisant la disposition sur le texte actuel. Le droit en vigueur porte
l'effet de la loi **adoptée**, amendements compris, et non l'effet de la
disposition déposée : deux inconnues, pas une. Une méthode qui tombe juste une
fois n'est pas une méthode.

## La règle qui a coûté deux extraits — l'applicabilité se lit aux dates

**C'est l'intervalle de dates qui décide, jamais l'état LEGI.** `ABROGE_DIFF`
marque une version qui s'applique aujourd'hui et dont l'abrogation est déjà
votée. Filtrer sur `VIGUEUR` a fait disparaître l'article 279 du code général des
impôts et tout le bloc TVA de deux extraits successifs, sans un message.

Le CGI porte **376 articles applicables à fin programmée**, le CIBS **282** : la
recodification fiscale est en cours. Le lecteur sort l'avertissement de lui-même,
et une version future est refusée avec sa date d'entrée en vigueur plutôt que
rendue comme du droit applicable.

## Le témoin, et pourquoi il existe

Chaque code déclare un article qu'il doit porter. Son absence **fait échouer
l'extraction** plutôt que de livrer un code amputé. Il a payé trois fois : le
trou TVA, puis un mauvais choix de ma part — l'article 2 du code des douanes,
retenu sur une date d'URL prise pour une preuve de vigueur, abrogé depuis le
1er mai 2026.

Le manifeste porte désormais, par code, **dix articles dont l'applicabilité est
prouvée par l'extrait** : épingler un témoin ne demande plus d'aller sur le web.
**Le code des douanes est à témoin non épinglé** — son contrôle est en veille, le
manifeste le déclare, et `266 sexies` est le candidat relevé.

## Les renvois entrants — régime arrêté par l'auteur le 20260902

`coordination.py` relève, à travers les vingt codes, les articles applicables qui
citent l'adresse qu'on s'apprête à modifier. C'est le trou que rien ne comblait :
`N6` de `vecteur-mesure` voit deux mesures qui visent la même adresse, il ne voit
pas les articles qui citent la nôtre.

**Amendement — service minimum.** On ne coordonne pas, on **signale** : les
renvois relevés se listent **en fin d'exposé sommaire**. Le maquis des renvois ne
doit pas bloquer la production.

**Proposition de loi — la boucle va jusqu'au bout.** Chaque renvoi se traite ou
se déclare sans objet avant dépôt. C'est un travail lourd, assumé comme tel.

Chaque renvoi porte sa **certitude**, fixée par une règle de déduction et non par
une impression : `nomme` quand la phrase nomme le code visé ; `interne` quand
l'article citant est dans le même code et qu'aucun autre n'est nommé ; `ambigu`
pour une citation nue depuis un autre code, à qualifier à la main.

*Mesuré : abroger l'article 279 du CGI touche quatre articles applicables ;
abroger `L. 3262-1` du code du travail en touche neuf, dont cinq au code de
l'éducation, invisibles depuis le code du travail seul.*

## Ce qui n'est pas couvert, et qui se dit

**Le droit non codifié.** Un renvoi porté par une loi non codifiée n'est pas vu,
et un siège dans une loi de finances antérieure n'est pas dans l'extrait. Les
textes non codifiés consolidés entrent par le même mécanisme — une ligne dans
`codes.json` avec leur `LEGITEXT` — mais **ce n'est pas éprouvé**. C'est la voie
vers l'article 179 de la loi de finances pour 2020, siège que l'éval a montré que
la skill ne trouvait pas (A-273).

**Le texte déposé du PLF et du PLFSS** n'est pas ici : c'est une autre source,
digérée le 20260902 par les fils du socle.

Ni jurisprudence, ni doctrine, ni réglementaire hors codes. Ni l'API PISTE, qui
demanderait un compte et deux secrets pour un service que LEGI rend sans clé.

## Entrée d'index due

`reference/depot_droit.md`, rang `methode`, famille `méthode`, coffre `true`.
Les pièces du dépôt vivent hors corpus : elles ne se versent pas au coffre, la
jauge étant comptée en dizaines de kilo-octets. Le dépôt est leur lieu.
