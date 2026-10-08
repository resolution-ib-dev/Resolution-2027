# Arbitrages — geste 2, restauration et déclarations, 20261007

**Fil** : Cowork, suite de la digestion du guide de légistique.
**Mandat** : l'auteure, 20261007 — « résous tout partout point par point en vérifiant les accès ».
**Domicile** : `methode/fragments/arbitrages/20261007-geste2-restauration.md`.
**Mesure** : 9 pièces restaurées, 1 supprimée, 14 déclarations posées, 150 anomalies bloquantes
contre 153 avant, I4 et I5 à zéro. Versé à `main` au commit `0f1d138` le 20261007.
**Appui** : le dépôt cloné à `claude/gracious-bell-z4jsz1` (`3ec82d1`), le transcript de cette
session, `methode/classement_corpus.md` (R5, R8), `methode/appui_des_passes.md`.

---

## 1. La règle qui manquait — un fil code ne restaure pas

Le fil code a buté sur le geste 2 et il a eu raison de s'arrêter. **Ce n'était pas un échec, c'est
structurel** : un fil Claude Code n'a aucun accès au coffre, et `restaurer.py` travaille sur le
transcript d'une session **qui a lu le coffre**. Un fil code n'en lit jamais.

**Tranché, et inscrit au § « ce qui bloque quoi » de la procédure** : la restauration d'une pièce
du projet vers le dépôt est toujours le travail d'un fil Cowork. Au fil code reviennent l'édition
de l'appareil, les `make`, le relevé des empreintes et la poussée. La ligne de lancement du
20261007 était fautive sur ce point, et la faute est à moi.

## 2. Ce qui a été restauré, et comment

Neuf pièces, **sans qu'aucun octet passe par le modèle**. Huit sont copiées du disque de cet
atelier, telles qu'écrites. `reference/regles_credits.md` est extrait du transcript de session par
script, son contenu étant celui rendu par le coffre : ses dix-neuf identifiants LEGIARTI sont
intacts, et la règle R8 est tenue.

`reference/structure_ppl.md` est supprimé — son contenu est intégralement repris par
`reference/guide_legistique.md` —, **et ses trois déclarations partent dans la même passe**. C'est
ce qui lève les deux alias revendiqués deux fois : I4 passe de 2 à 0.

## 3. Les trois corrections du fil code, reprises

Justes toutes les trois, et elles valent pour les fils suivants : les chemins de l'appareil se
comptent à partir de `chantier/` et non avec ce préfixe ; `generer_carte.py` porte l'apostrophe
typographique ; **`make index` ne fait que contrôler, l'index se régénère par `make reindex`**.

## 4. Ce que ce fil a tranché en propre

- **`guide_public_budgetaire` sort des manquants.** Son original est au dépôt depuis `a142a66` et
  il est digéré par `regles_credits`. La ligne « sorti du projet, non digéré » était périmée.
- **Les deux entrées de carte adressent la pièce et non la source** — `reference/…` et non
  `sources/…` —, faute de quoi l'artefact reste sans famille.
- **Famille `références externes` pour les deux digestions**, et non `méthode` : une digestion se
  vérifie contre une source externe, c'est R4.
- **Neuf artefacts déclarés à l'index**, les deux digestions, les deux documents de méthode et les
  cinq fragments du jour. I5 passe de 9 à 0.

## 5. Versement — fait le 20261007

`main` porte le commit `0f1d138`. Contrôlé mécaniquement sur un clone neuf :
`reference/guide_legistique.md` et `reference/regles_credits.md` présents,
`reference/structure_ppl.md` absent, `methode/appui_des_passes.md` et
`methode/procedure_fin_de_chantier_depot_2027.md` présents, six fragments d'arbitrage des
20261006 et 20261007. `make controle` rejoué par le fil code : 150 anomalies bloquantes, I4 à 0,
I5 à 0, 14 manquants déclarés — le compte attendu. `make coffre` joué, empreintes relevées.

**La voie qui a fonctionné, et qui devient la voie par défaut** : le paquet complet remis au fil
code en pièce jointe, zip unique avec son manifeste sha256, le fil dépliant, contrôlant,
branchant, fusionnant et poussant seul. L'auteure ne touche ni à git ni au navigateur. Les
contournements par bundle, par upload web fichier à fichier et par branche manipulée à la main
ont tous été écrits pour rien, sur une impossibilité supposée et non mesurée.

**Reste une branche morte** : `claude/gracious-bell-z4jsz1`, à `3ec82d1`, que le fil code n'a pas
pu supprimer — cinq tentatives, connexion coupée à chaque fois, alors que les poussées passaient
par la même voie. Son contenu est intégralement repris par `main`. `geste2-20261007` est à
l'identique de `main` et peut partir avec elle.
