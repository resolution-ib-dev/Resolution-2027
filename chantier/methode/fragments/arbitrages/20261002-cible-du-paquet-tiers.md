## La cible, verrouillée par l'auteure le 20261002

**Un tiers reçoit tout ce qu'il lui faut pour produire ses propres amendements
au PLF et au PLFSS, déposables, exportés en .docx.** Les procédures, les
référentiels, les outils, les contrôles. **Les incertitudes irréductibles se
déclarent, elles n'empêchent pas de livrer.**

**Forme : un zip de pièces jointes qu'il verse dans son propre projet Claude.**
Décision antérieure de l'auteure, rappelée ce jour et **non rediscutable**. Le
paquet de modules Python seuls n'est pas la cible et ne l'a jamais été.

**Projet d'intérêt général** : le matériel doit être exportable et utilisable
facilement, partout.

**Ce que la cible écarte** : la poussée de `redaction_2027.py` au dépôt n'est
pas sur son chemin critique. Elle relève de l'hygiène d'appareil et attend.

## Inventaire mesuré le 20261002 — ce qui tient, ce qui bloque

**Quatre étapes sur sept sont outillées** : E0 qualification et E2 vecteur par
`vecteur-mesure` ; E4 rédaction cible par `disposition-cible` et
`redaction-legistique` ; E5 exposé sommaire par `expose-sommaire`. E3 est
outillée hors skill, par le dépôt de droit.

**Deux bonnes nouvelles mesurées.** L'accès au droit ne coûte rien au tiers :
LEGI est en open data, le dépôt est public en lecture, **aucune clé, aucun
compte, aucun quota** — il lui faut `git`, Python et un accès réseau. Et la
sortie .docx déposable existe déjà : `generateur_liasse_docx.py`, Garamond,
nomenclature de liasse. **Ce n'est pas `impression-docx`, dont les trois profils
ne couvrent pas l'amendement.**

**Cinq blocages mesurés.**

1. **E1, le rattachement, n'est pas outillé.** La procédure est écrite, aucune
   skill ne la joue. C'est l'étape qui dit si l'amendement est recevable.
2. **Le contrôle `G` n'est pas outillé.** `appareil/controle_sortie.py` est nommé
   par cinq skills et **n'existe pas**. C'est la règle qui interdit à une sortie
   diffusée de nommer un déposant, un projet ou un référentiel interne — celle
   que le contrat dit perdue quatorze fois, et celle qui gouverne précisément ce
   paquet.
3. **Cinq pièces de méthode sont fortement contaminées** :
   `methode/procedure_vecteurs.md`, `reference/gabarit_expose_sommaire.md`,
   `methode/regles_redactionnelles.md`, `methode/regles_forme_canonique.md`,
   `reference/passation_droit_renvois.md`. Elles nomment une organisation tierce,
   le manuscrit, les référentiels internes et des identifiants d'amendements d'un
   déposant. Six autres sont à nettoyer légèrement.
4. **Cinq skills exigent des référentiels qui n'existeront pas chez le tiers** —
   `REF_doctrine`, `REF_chiffres`, `positions`, `notes_manuscrit`. `audit-conformite`
   en dépend, donc **E6 est inopérante en l'état**.
5. **Le dossier de mesure du contrat n'est outillé nulle part.** Aucune skill ne
   lit ni n'écrit l'objet à huit blocs. **Le tiers doit recoller les étapes à la
   main** — c'est exactement ce que le contrat voulait lui épargner, et c'est la
   différence entre « certains avaient fini par y arriver » et « il y arrive ».

**Deux manques qui se déclarent et ne bloquent pas** : E7 ne rend pas l'ordre de
dépôt ni les neutralisations réciproques ; le droit non codifié n'est pas au
dépôt, et l'extrait LEGI se périme à 45 jours sans que le tiers puisse le
régénérer.

## L'ordre de construction — tranché par le fil

1. **Écrire le contrôle `G`.** Il est à la fois une pièce du paquet et le
   garde-fou du nettoyage : sans lui, le nettoyage n'est pas vérifiable, et un
   nettoyage tenu à l'œil se perd.
2. **Nettoyer les onze pièces**, contrôle `G` joué sur chacune.
3. **Écrire le liant** : la procédure qui enchaîne E0 à E7 chez le tiers, portant
   le dossier de mesure. C'est ce qui fait la différence entre un outil que
   certains arrivent à conduire et un outil qui conduit.
4. **Monter le paquet** : pièces nettoyées, référentiels du millésime, modules de
   lecture, générateur de liasse .docx, `LISEZ-MOI` qui déclare les deux trous.

**E1 n'est pas outillée pour cette livraison : elle se déclare.** Un tiers saura
que la recevabilité reste à sa charge, avec la procédure écrite pour la conduire
à la main. Outiller E1 devient le premier chantier après la livraison.

**Exclues du paquet** : `resolution-chantier`, entièrement interne ;
`compatibilite-doctrine` et `fiche-mesure`, qui projettent une doctrine que le
tiers n'a pas. `audit-conformite` part **amputée de ses contrôles doctrinaux** et
réduite à ce qu'un tiers peut jouer : verbatim, sources, registre, forme.
`contestabilite` et `qa-riposte` partent nettoyées — elles servent un tiers et ne
dépendent pas du fond.
