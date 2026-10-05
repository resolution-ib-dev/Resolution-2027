# Passation — 4 octobre 2026, soir

**Porteur** : fil chef de file. **Domicile** : coffre. Elle périme
`methode/passation_20261004.md` du matin. Un fil neuf n'a rien d'autre à lire que ce qu'elle
nomme.

---

## 1. L'état en cinq lignes

La clause générale est **achevée** : 441 rangs au III. Les quatre points de recevabilité sont
**purgés et reportés** sur les trois pièces. Les numéros 3210 et 3211 sont **portés partout**.
Les socles de texte 2027 sont **réparés, régénérables et déclarés**. Il reste **une seule
opération avant que la liasse P1 soit transmissible** : le contrôle d'adresse au dépôt de droit.

## 2. L'accès au droit — la question est close, et voici la réponse

**L'accès à Légifrance n'est pas un chantier ouvert : il est résolu, et depuis longtemps.** Le
site `legifrance.gouv.fr` refuse toute lecture automatique, de n'importe quelle session — c'est
une protection du site, pas une configuration à corriger, et il ne faut plus perdre une heure
dessus. **Le droit ne se lit pas sur le site. Il se lit sur l'extrait LEGI du dépôt**, sous
`droit/`, avec son manifeste `data/_manifeste.json`, sa clé `millesime_legi`, son lecteur
`droit.py` et son extracteur `extraire_legi.py`, que l'action programmée du dépôt rejoue le
1er de chaque mois. `installer_droit.py` clone, rafraîchit, juge la fraîcheur à 45 jours, et
dépose un marqueur `EXTRAIT_PERIME` qui bloque la rédaction si l'extrait a vieilli.

**Le chaînage fonctionne donc en mode normal — dans une session de code, et là seulement.** Un
fil Cowork ne peut pas l'atteindre : le coffre plafonne à 2 Mo et l'extrait du seul code général
des impôts le dépasse. La synchronisation du dépôt n'apporte ici que `codes.json`, l'index des
identifiants Légifrance, et c'est tout ce qu'elle peut apporter.

**La répartition est donc définitive, et elle ne se rediscute plus** : la rédaction et les
arbitrages se font au coffre ; **tout ce qui touche au verbatim du droit — relever une adresse,
la contrôler, prendre un texte en vigueur — se fait en session de code sur `droit/`.** Un fil
qui a besoin d'une adresse certaine ne la devine pas et ne la cherche pas sur le web : il la
déclare « à contrôler au dépôt de droit » et il continue.

## 3. Ce qui a été fait le 4 octobre

| pièce | ce qu'elle rend |
|---|---|
| `methode/objectifs_depot_2027.md` | les objectifs de l'auteure, la construction type, l'objectif terminal |
| `livrables/clause_generale_niches_20261004.md` | la clause achevée — 441 rangs, découpage des chaînes tranché |
| `methode/purge_recevabilite_20261004.md` | les quatre corrections de recevabilité, verbatim |
| `methode/passe_numeros_et_corrections_20261004.md` | le report des corrections et des numéros sur les pièces |
| `methode/analyse_ordre_concours_collectivites_20261004.md` | l'ordre des coupes aux collectivités, chiffré |
| trois arbitrages du jour | trois étages des concours ; rupture assumée et DMTO ; dénominateur et classement de la DGF |

**Arbitrages de l'auteure, tranchés et inscrits** : on joue en loi de finances, la baisse de
ressource voyage avec le retrait de compétence ; les concours discrétionnaires tombent d'abord
et intégralement ; la dotation globale absorbe les refontes ; **la cotisation foncière des
entreprises reste fondue dans la taxe foncière unique** ; les chiffres se recalent au dernier
moment, les textes s'achèvent d'abord.

## 4. Le mandat de session de code — un seul, à pousser ce soir, texte verbatim

> Tu travailles sur le dépôt `resolution-ib-dev/Resolution-2027`, branche
> `claude/vibrant-ramanujan-8650k1`. Tu fais deux choses, dans cet ordre, et rien d'autre.
>
> **Premièrement, le contrôle d'adresse.** Le dossier `chantier/livrables/` porte une pièce
> nommée clause générale d'abolition des niches, dont le III de l'article 1er énumère 441 rangs
> d'abrogation. Si cette pièce n'est pas au dépôt, dis-le et passe au second travail : elle vit
> au coffre et elle te sera portée verbatim dans un prochain mandat. Si elle y est, tu contrôles
> chacune de ses adresses contre l'extrait LEGI de `droit/`, au millésime que porte
> `data/_manifeste.json`. Commence par jouer `installer_droit.py` : si le verdict est périmé, tu
> t'arrêtes et tu le dis, tu ne rédiges pas sur un extrait vieilli. Pour chaque rang, tu vérifies
> trois choses : que l'article existe, qu'il est en vigueur au millésime, et que la subdivision
> visée existe bien dans cet article. Tu rends un tableau à quatre colonnes — rang, adresse,
> verdict parmi EXISTE, ABSENT, ABROGE, SUBDIVISION_INTROUVABLE, et la citation courte qui le
> prouve. Tu ne corriges aucune adresse et tu n'en inventes aucune : tu mesures et tu rends.
> Deux points sont déjà signalés et demandent ton attention particulière : un rang abroge
> l'article 194 du code général des impôts en entier tandis qu'un autre n'abroge que son II ; un
> rang abroge l'article 223 O en entier alors que onze autres rangs n'en abrogent que des lettres
> nommées. Dis, pour ces deux cas, ce que porte réellement le droit.
>
> **Deuxièmement, la fusion des deux montages de la machine.** Le dépôt porte deux paquets,
> `machine_v1_2` et `machine_v1_2_a3`, montés le même jour par deux fils parallèles. Ils sont
> disjoints et chacun corrige des points que l'autre ne corrige pas ; leurs deux manifestes
> disent qu'aucun des deux ne part avant fusion. Sur `installer_droit.py` et sur
> `controle_sortie.py`, c'est la version a3 qui fait foi. Les procédures que porte a3 sous
> `procedures/` ne sont pas des doublons des originaux : un relevé a mesuré 142 fuites sur les
> originaux, et les retirer referait une erreur déjà commise. Tu produis un paquet unique qui
> prend le meilleur des deux, tu rejoues le mini-lot d'essai de bout en bout contre le socle de
> texte 2027 réparé, et tu rends un installable qu'un tiers déplie et fait tourner sans nous.
> L'installateur ne clone pas `chantier/`.
>
> Tu pousses sur la même branche, en un seul jeu de commits, et tu rends un compte rendu portant
> le tableau de contrôle d'adresse, le compte des verdicts par catégorie, l'état du mini-lot
> rejoué, et tout écart que tu n'as pas corrigé.

## 5. Ce qui reste, par ordre, et qui n'est pas bloquant ce soir

1. **Le relevé des niches sociales par siège.** Seul trou de liste qui subsiste ; il donne à
   l'article 2 de la clause l'équivalent de son III.
2. **Les vingt-deux sièges manquants de la pièce 4.4**, qui est aujourd'hui plus étroite que la
   mesure décidée, et **le repli énuméré à 746 lignes du lot 2.1**.
3. **Les vingt-deux points restants du contrôle de nuit**, à purger avant toute transmission.
4. **Le recensement des concours discrétionnaires par siège**, condition de l'étage 1 du volet
   collectivités.
5. **Le recalage des montants sur les annexes 2027**, quand l'auteure aura déposé les deux tomes
   des voies et moyens dans la conversation. Il ne change aucun rang : les sièges se lisent sur
   le droit, non sur le chiffrage.
6. **Le périmètre de la refonte des droits de mutation à titre onéreux**, à arrêter par
   l'auteure avant qu'un fil s'ouvre.

## 6. L'objectif de revoyure

**La liasse P1 du projet de loi de finances, transmissible.** Il lui manque le contrôle
d'adresse — le mandat du § 4 — et le recoupement de la clause contre ses replis. Tout le reste
est fait.
