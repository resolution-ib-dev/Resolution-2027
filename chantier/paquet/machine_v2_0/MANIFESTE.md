# Manifeste — machine à amendements 2027, version 2.0

**Porteur** : fil Cowork de reconstruction, 20261016.
**Mandat** : l'auteure, 20261016 — « on avance pour faire une version à jour robuste
(prévois des modules de test) ».
**Mesure d'entrée** : v1.4, 29 fichiers, dont **20 retrouvées à l'octet au dépôt** par
confrontation de son propre manifeste, **3 reprises dans leur état avancé du dépôt**, et
**6 reconstruites**.

**Arbitrage tenu** : « une version à jour » commande l'état du dépôt. Les trois pièces que
le dépôt porte dans un état postérieur à la v1.4 sont reprises dans cet état, non gelées.

**Paquet** : 37 fichiers, 452 109 octets.

## Ce qui change par rapport à la v1.4

- **`appareil/generateur_liasse_docx.py` reconstruit.** Celui de la v1.4 partitionnait sur
  `\newpage` ; les liasses courantes n'en portent aucun — elles séparent par `---` et
  ouvrent chaque amendement par `## Amendement n° N [titre]`. Le reconstruit lit ces
  conventions, pose le saut sur le paragraphe suivant, et relève les rangs **en deux
  passages** pour qu'un sommaire placé en tête trouve ses signets.
- **`procedures/gage.md` reconstruit**, méthode seule : les onze règles de tenue du
  registre des sources, les trois formes de clause, les trois gisements de réservoir.
  Aucun montant, aucun réservoir, aucun arbitrage d'ordre — ils appartiennent au projet
  qui les a relevés.
- **`appareil/controle_sortie.py`, `procedures/regles_forme_canonique.md` et
  `procedures/regles_redactionnelles.md`** : l'état du dépôt, postérieur à la v1.4.
- **`tests/` est neuf** — cinq modules et un lanceur. La v1.4 n'en portait aucun : elle
  prouvait ses pièces par un manifeste, jamais son produit par une mesure.
- **`mini-lot/` reconstruit**, sa sortie attendue étant une pièce réelle de la liasse du
  dépôt 2027 et non un spécimen écrit pour le test.
- **`LISEZ-MOI.md` reconstruit**, § 4 refait sur la chaîne de test.

## Le défaut que les tests ont pris

Au premier essai du générateur, `test_docx` a rendu **écart +54 caractères, attendu +20**
et **34 tirets cadratin de trop sur la liasse P1**. Cause relevée dans le module, non
supposée : la valeur de repli d'un champ `PAGEREF` compte comme du texte, et le repli
était un cadratin. Repli ramené à vide, invariant exact. **Sans ce module, le défaut
partait au tiers.**

## Ce qui se déclare et n'empêche pas de livrer

- les deux PDF des textes enregistrés ne sont pas joints — 3,7 Mo, téléchargeables chez
  l'Assemblée, empreintes au relevé `referentiels/socles_2027.sha256` ;
- `test_socles` sort donc en `ABSENT` sur une installation neuve, et `test_recette` sur
  son temps 2 ;
- le relevé des portes du domaine des lois de financement **porte sa date de péremption**
  et `test_droit` la mesure. **Rafraîchi le 20261016** : relevé au millésime LEGI 20261013,
  **31 portes en verbatim, 0 en échec**, chacune avec son identifiant Légifrance. Le relevé
  précédent, au millésime 20260901, périmait le 17 octobre ; le nouveau porte au
  27 novembre 2026. La pièce livrée est désormais la grille que le module régénère, et non
  sa version documentée abrégée.

## Les pièces

| fichier | octets | sha256 |
|---|---:|---|
| `LISEZ-MOI.md` | 9053 | `6339ce7bb8095326` |
| `appareil/controle_sortie.py` | 18998 | `b2a234400bdfff80` |
| `appareil/generateur_liasse_docx.py` | 21401 | `98d94dcb9ffafdd8` |
| `appareil/index_mesures_2027.py` | 6159 | `3065070b9568da98` |
| `appareil/installer_droit.py` | 14358 | `0fecc20ec4ca01a1` |
| `appareil/pieces_nommees.py` | 4028 | `ae065c451f5e7ad4` |
| `appareil/portes_ouvertes.py` | 8888 | `2b9f61cd5118063c` |
| `appareil/redaction_2027.py` | 11805 | `f2a87e13f34016dd` |
| `appareil/relever_manifeste.py` | 3874 | `3ba0ec717da75540` |
| `appareil/socle_texte_2027.py` | 9139 | `12801c0acf98ead6` |
| `mini-lot/LISEZ-MOI.md` | 2860 | `812bc4bd3e313926` |
| `mini-lot/enonce.md` | 1720 | `0ffc4dec3d96fd8f` |
| `mini-lot/sortie_attendue.md` | 3660 | `59a2f7f446c75ab4` |
| `procedures/conduite.md` | 21188 | `788ec99f19cea1f1` |
| `procedures/contrat_chaine_amendement.md` | 24459 | `5ad80d3d624e762d` |
| `procedures/depot_droit.md` | 13065 | `9883639b24b59ab8` |
| `procedures/domaine_lfss_LO111-3.md` | 35999 | `c7fc7f96e0527e4f` |
| `procedures/gabarit_expose_sommaire.md` | 7785 | `21a2a6e98b9e91ca` |
| `procedures/gabarit_liste_articles.md` | 9155 | `9af348ba4f0e3a1a` |
| `procedures/gage.md` | 5384 | `1073b8df7e5eab75` |
| `procedures/passation_droit_renvois.md` | 2988 | `a4c5070f89e64b1f` |
| `procedures/procedure_vecteurs.md` | 12162 | `e6b4352460d5c291` |
| `procedures/regles_forme_canonique.md` | 16892 | `42ecec9215b95a2a` |
| `procedures/regles_redactionnelles.md` | 17192 | `66e597764b5b8546` |
| `procedures/structure_ppl.md` | 12771 | `514483c5b2013301` |
| `procedures/test_rattachement.md` | 12778 | `3958ff4420857f4a` |
| `referentiels/articles_ouverts_plf2027.tsv` | 25306 | `5abd05f589dbae63` |
| `referentiels/articles_ouverts_plfss2027.tsv` | 8928 | `5d771439ae814b52` |
| `referentiels/releves_transversaux_plf2027.tsv` | 54192 | `a5a4c50322cea546` |
| `referentiels/releves_transversaux_plfss2027.tsv` | 22884 | `73c8176a4a4615c0` |
| `tests/jouer.py` | 3537 | `adfb62375ef24b2e` |
| `tests/socle.py` | 3010 | `140c5a7ac8480e58` |
| `tests/test_docx.py` | 5579 | `54d163e7435ac326` |
| `tests/test_droit.py` | 5963 | `27208b61c24af9d1` |
| `tests/test_integrite.py` | 2682 | `b9b75266aea77f95` |
| `tests/test_recette.py` | 7102 | `9c56bd5df014433b` |
| `tests/test_socles.py` | 5165 | `ad62c2e912044494` |
