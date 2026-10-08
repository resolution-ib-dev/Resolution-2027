# Gestion projet · dépôt · archives — règle en vigueur

**Porteur** : fil Cowork, 20261005. **Mandat** : l'auteure, 20261005 — « une solution robuste clef
en main activable ». **Domicile** : projet, `methode/`. **Mesure** : 290 documents au projet
(≈ 1,94 Mo sur 2 Mo) ; 223 proposés au premier versement, 66 restent.

## 1. Trois lieux, un rôle chacun

| lieu | ce qu'il porte | qui y écrit | taille |
|---|---|---|---|
| **projet** | les **décisions** (règles, objectifs, consignes, arbitrages, passation, plan, index) et le **travail en cours** (pièces en revue) | tout fil | bornée : 60 % visés, alerte à 85 % |
| **dépôt** (`resolution-ib-dev/Resolution-2027`, `main`) | le **validé** (`chantier/livrables/depot_2027/`), les **archives** (même chemin que dans le projet, sous `chantier/`), la machine, les sources, le droit, l'index des versements | les **sessions de code** seules | sans borne utile |
| **zip** | le transport, jamais le stockage | Cowork le monte, la session de code l'applique | — |

Une pièce n'est qu'à un seul endroit à la fois. En tête de chaque pièce : `Statut : decision`,
`travail`, `valide` (date, arbitrage) ou `perime`.

## 2. Le cycle d'un document

`travail` (projet) → validé par l'auteure en revue → `valide` → versé au dépôt → retiré du projet.
`decision` reste au projet ; quand elle est absorbée ou périmée, elle passe `perime`, est versée, puis
retirée.

## 3. L'outil : `versement.py`, trois gestes

1. **préparer** — fil Cowork. Un sous-fil « tuyau » lit au projet les documents de la liste (il ne
   recopie rien) ; `versement.py preparer` les extrait du transcript, les mesure contre un clone du
   dépôt, et monte `versement_AAAAMMJJ.zip` avec son manifeste (chemin, empreinte, empreinte attendue
   au dépôt avant écriture, action : ajout, remplacement ou identique).
2. **appliquer** — session de code. `versement.py appliquer --commit` dans un clone de `main` :
   s'arrête si un seul fichier du dépôt a changé depuis la préparation, copie, contrôle chaque
   empreinte après copie, inscrit le versement à `chantier/methode/index_versements.json`, un seul
   commit, poussé sur `main`.
3. **vérifier** — fil Cowork. `versement.py verifier` sur un clone neuf rend la liste des documents
   identiques au dépôt. **L'auteure valide la liste** ; le fil les retire du projet, et seulement eux.

Essai à blanc joué le 20261005 sur trois documents : préparé, appliqué, vérifié identique ; le second
passage s'arrête, le dépôt ayant changé. La garde de concurrence tient.

## 4. Règles qui ne se négocient pas

- **Aucune suppression au projet sans copie vérifiée identique au dépôt**, ni sans liste validée par
  l'auteure. Une purge ne vise que ce qu'une pièce de méthode déclare `perime`.
- **Seules les sessions de code poussent**, une à la fois, par paquet avec mesure d'entrée ; aucune
  branche ne survit à sa session.
- **Les archives ne se suppriment jamais du dépôt.**
- **Pour retrouver une pièce archivée** : `chantier/<chemin d'origine>` au dépôt ; l'index des
  versements dit quand et pourquoi elle est partie. Un fil Cowork la lit par clone ; un fil de
  conversation la cite par son chemin.

## 5. Rituels

- **Ouverture de fil** : mesurer le remplissage du projet ; au-delà de 85 %, proposer un versement.
- **Clôture de lot validé** : passer ses pièces en `valide` ; elles partent au versement suivant.
- **Fin de journée** : un versement, s'il y a lieu.
