# Audit — les pièces sans domicile, et la réparation — 20261004

## Ce qui s'est passé, et ce n'est pas un oubli

Le fil d'outillage des textes 2027 a produit **les deux socles** — une entrée par
article, numéro, partie, intitulé, **rédaction exacte**, folio imprimé, exposé rattaché.
PLF 2027 : 90 articles, folios 33 à 268. PLFSS 2027 : 49 articles, folios 1 à 112. Aucun
article sans intitulé, sans dispositif ni sans exposé. Déterminisme contrôlé, couverture
contrôlée, jeu de fautes levé.

**Puis il a écrit ceci, en toutes lettres, à son journal du 1er octobre :**

> « Les deux socles pèsent 1,27 Mo et 344 ko : **ils restent à l'atelier, le coffre ne
> reçoit que les modules et les deux référentiels.** »

**L'atelier disparaît avec la session.** Les socles ont donc été détruits le jour même de
leur production, par une décision inscrite et que personne n'a relevée — moi compris, qui
ai lu ce fragment sans en voir la conséquence. **Ce qui reste au projet n'est que du
dérivé** : index des mesures, relevés transversaux, articles ouverts, listes, fiches. Du
dérivé qui ne régénère pas sa source.

**Et la source n'est nulle part ailleurs.** Ni au dépôt, ni dans les pages publiées. Les
fichiers de ce nom au dépôt sont ceux de 2026.

## La cause, et elle est structurelle

**Un fil Cowork peut produire une pièce lourde, et cette pièce n'a nulle part où aller.**
Le coffre est borné et la refuse. Le dépôt, qui l'accepterait, n'est pas accessible depuis
Cowork. Le fil fait alors la seule chose qui lui reste : il la laisse à l'atelier, et il
le déclare — en croyant déclarer un rangement, quand il déclare une destruction.

**C'est la troisième occurrence de la même famille en trois jours.**

| défaut | l'objet | ce qui lui manquait |
|---|---|---|
| le registre des gages est resté vide alors que toutes les pièces déclaraient | un registre partagé | **un fil porteur** |
| le relevé des sièges de niches n'a jamais été produit | un référentiel attendu par un lot | **un mandat qui le nomme** |
| les socles de texte 2027 ont été détruits | une pièce lourde | **un domicile** |

**Un objet qui n'a ni porteur, ni mandat, ni domicile n'existe pas**, même quand tout le
monde le croit produit. C'est le même défaut sous trois formes, et il a coûté trois fois.

**Quatrième occurrence, ce matin, même famille** : deux fils ont monté un paquet de machine
dans le même dossier du projet, et le second a écrasé trois documents du premier, sans
retour possible. **Un dossier partagé n'avait pas de porteur.**

## Les règles, posées

**1. Une pièce lourde déclare son domicile avant d'être produite.** Trois domiciles, et
pas de quatrième : le coffre si elle y tient ; le dépôt, et le fil rend alors un paquet
pour une session de code ; ou elle ne se produit pas. **« Reste à l'atelier » n'est pas un
domicile, c'est une destruction déclarée.**

**2. Un dérivé ne remplace jamais sa source.** La règle « un dérivé qui se régénère à
l'identique ne se verse pas » ne vaut que si la source dont il se régénère est, elle,
conservée et atteignable. Un dérivé dont la source a disparu est **un orphelin**, et il
doit être signalé comme tel.

**3. Tout objet partagé — registre, référentiel, dossier de paquet — a un fil porteur et un
seul.** Les autres déclarent chez eux ; le porteur relève et inscrit.

**4. Une pièce source entrée par pièce jointe ne sort pas du fil sans que son socle soit
domicilié.** C'est le seul moment où le verbatim existe ; le laisser passer, c'est
redemander la pièce.

## La réparation

**Ce qui est perdu et ne se reconstitue pas tout seul** : la rédaction exacte, alinéa par
alinéa, des 90 articles du PLF 2027 et des 49 articles du PLFSS 2027.

**Ce qui n'est pas perdu** : les extracteurs. `socle_texte_2027.py` et `redaction_2027.py`
existent, ils sont déterministes et contrôlés. **Il ne manque que la pièce source.**

**Trois gestes, dans l'ordre.**

1. **Les deux PDF reviennent par pièce jointe.** C'est le seul chemin par lequel du
   verbatim entre : la récupération web ne rend jamais du verbatim, et les deux sites qui
   les publient sont aujourd'hui inatteignables depuis l'atelier.
2. **Une session de code rejoue les deux extracteurs et pousse les socles au dépôt**, avec
   leurs empreintes. Ni l'atelier, ni le coffre : le dépôt.
3. **Le coffre reçoit une fiche d'une page** — nom, taille, empreinte, date, extracteur —
   et rien de plus, comme pour le réservoir d'arguments.

**Tant que les socles ne sont pas revenus** : la première passe du contrôle de la machine
reste impossible, et tout relevé de siège fondé sur le texte déposé est fondé sur du
dérivé. Les pièces déjà écrites contre le droit en vigueur ne sont pas atteintes — elles ne
lisent pas le socle.

## Deux points qui ne sont pas de la mécanique

**Le dépôt de droit est public et la commande d'installation le clone en entier**, donc
avec `chantier/` : méthode, livrables, et le livre. **La mécanique est tranchée ici** —
l'installateur ne clone plus que ce dont il a besoin, et jamais `chantier/`. **Ce qui
reste à l'auteure** : garder ou non le livre et les livrables dans un dépôt public.

**Deux arbitrages attendent, inchangés.** Les collectivités : taxe sur la valeur ajoutée
seule, comme arrêté le 2 octobre, ou taxe sur la valeur ajoutée et dotation globale ?
*Inclination exprimée le 4 octobre : la taxe d'abord, après nettoyage des petits fonds
discrétionnaires ; la dotation seulement si elle se compte en recette propre et se fait
aisément en loi de finances.* Et : la restitution salariale bascule-t-elle en loi de
financement ?
