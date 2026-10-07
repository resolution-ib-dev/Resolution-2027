# Appui des passes — quelle pièce s'ouvre avant quoi

**Porteur** : fil de digestion du guide de légistique, 20261007.
**Mandat** : l'auteure — « qu'est-ce qui permet d'assurer que l'info sera systématiquement vue
au bon moment par le bon fil ».
**Domicile** : `methode/appui_des_passes.md`.
**Mesure** : 2 pièces de référence, 7 types de passe.

---

## Pourquoi ce document existe

La faute du 20261006 n'était pas une pièce manquante : la checklist était sur disque et n'a pas
été ouverte. Le verrou posé alors est l'invariant d'en-tête **Appui** — les références ouvertes
avant la passe, nommées et datées —, et une passe dont la ligne `Appui` est vide n'est pas une
passe valide.

Cet invariant dit qu'il faut nommer ce qu'on a ouvert. Il ne dit pas **ce qu'il fallait ouvrir**.
Ce document le dit. Il tient en une table, il se lit en entier, et une ligne de lancement de fil
peut le nommer seul : **le fil l'ouvre, et il sait quoi ouvrir ensuite.**

## Les deux pièces de référence, et le partage entre elles

| pièce | ce qu'elle porte | ce qu'elle ne porte pas |
|---|---|---|
| `reference/guide_legistique.md` | digestion intégrale du guide de légistique du SGG : structure d'une PPL, frontière loi/règlement, renvoi au décret, langue, formules modificatives, renvois au droit positif, entrée en vigueur, abrogations, domaine des lois financières, institution d'un prélèvement | le verbatim des textes en vigueur |
| `reference/regles_credits.md` | verbatim de onze articles de la LOLF relevé au dépôt de droit, règles d'amendement des crédits, nomenclature, gabarit d'un amendement de crédits | tout ce qui relève du guide |

Les deux ne fusionnent pas : la seconde vaut par son verbatim, et la règle R8 du classement
interdit de recopier un document qui vaut par son verbatim.

**Renvois qui résolvent sur `guide_legistique.md`** : `guide_legistique`, `structure_ppl`,
`guide_redaction`, `guide_domaine_financier`.
**Renvoi qui résout sur `regles_credits.md`** : `guide_budgetaire`.

## La table

Chaque passe ouvre ce que sa ligne nomme, et l'inscrit à son invariant `Appui`. Une passe dont
l'appui est incomplet se marque et se rejoue ; elle ne se verse pas.

| type de passe | appui dû |
|---|---|
| **rédaction d'une disposition normative** (cible, modificative, clause) | `guide_legistique` parties I à IV + `redaction-legistique/references/regles_redactionnelles.md` + le texte en vigueur relevé à l'extrait |
| **amendement de crédits, état B** | `regles_credits` + `guide_legistique` partie V |
| **test de rattachement d'une mesure à un véhicule financier** | `guide_legistique` partie V + `paquet/…/procedures/domaine_lfss_LO111-3.md` + `paquet/…/procedures/test_rattachement.md` |
| **recherche d'un vecteur, adresse de droit** | le dépôt de droit + `paquet/…/procedures/procedure_vecteurs.md` |
| **exposé sommaire d'amendement** | `paquet/…/procedures/gabarit_expose_sommaire.md` |
| **exposé des motifs d'une proposition de loi** | `guide_legistique` partie I |
| **contrôle de sortie avant dépôt** | `methode/controle_avant_transmission.md` + `guide_legistique` partie IV + `regles_redactionnelles.md`, ligne à ligne |

## Quel fil pour quelle passe

Une passe ne se confie pas au même fil selon ce qu'elle touche, et la frontière n'est pas une
préférence : elle est technique.

| passe | fil | pourquoi |
|---|---|---|
| lire, écrire ou restaurer une pièce du coffre | **Cowork** | un fil Claude Code n'a aucun accès au projet, et `restaurer.py` travaille sur le transcript d'une session qui l'a lu |
| éditer l'appareil, jouer les `make`, relever les empreintes, pousser | **code** | il a le dépôt sous la main, et les empreintes exigent un clone du dépôt de droit en `droit/` |
| arbitrer, trancher une question de fond | **conversation** | il ne déplie rien et ne joue aucun `make` |

**Un fil code à qui l'on demande de restaurer une pièce du projet s'arrête**, et il a raison de
s'arrêter : le constat est exact, et la faute est dans la ligne de lancement.

## Les trois mécanismes qui portent cette table, et aucun ne suffit seul

1. **La ligne de lancement de fil** nomme la documentation à activer. C'est le mécanisme
   principal, et le seul qui agit avant que le fil ait lu quoi que ce soit. Une ligne de
   lancement qui ne nomme rien produit un fil qui n'ouvre rien.
2. **L'invariant `Appui`** de l'en-tête enregistre ce qui a été ouvert. Il ne garantit rien par
   lui-même : il rend la faute visible après coup, ce qui est déjà ce qui manquait le 20261006.
3. **`methode/index.json`** résout les renvois. Un renvoi qui ne résout pas se déclare au bloc
   `manquants` et ne meurt pas en silence.

**La conséquence pratique, et elle est la vraie réponse** : le nombre de pièces ne décide de
rien ; ce qui décide, c'est qu'une ligne de lancement nomme ce document-ci. Un fil qui ouvre
`methode/appui_des_passes.md` trouve, en une table, tout ce qu'il devait ouvrir — quel que soit
le nombre de pièces derrière.
