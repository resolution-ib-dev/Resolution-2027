# Arbitrages — digestion des règles de crédits, 20261006

**Fil** : digestion 1.B (procédure de fin de chantier, § 1.B).
**Mandat** : règles d'amendement de crédits de la seconde partie.

## 1. Faux blocage annoncé, puis levé — et ce qui l'a produit

Le fil a annoncé la digestion impossible faute de droit accessible. Le constat était faux.
Chaîne de la faute, dans l'ordre : Légifrance rend `403` (constat exact et déjà connu) → la base
LEGI de la DILA rend `403` au mandataire (constat exact) → le dépôt de droit est cloné, et sa
liste de textes est imprimée **tronquée aux quarante premières lignes** → la LOLF, qui est au
rang 41 et au-delà, n'apparaît pas → absence conclue.

Le dépôt porte la LOLF : clé `loi organique n° 2001-692 du 1er août 2001`, court
`loi_org2001_692`, 73 articles, tous à l'état `VIGUEUR`, millésime LEGI `20261001`.

**Tranché** : deux règles inscrites au § 0 bis de la procédure. **R-A** — le droit se relève au
dépôt de droit, par `droit.py`, et nulle part ailleurs ; le clonage est public et ne suppose
aucune déclaration. **R-B** — une mesure ne se prend jamais sur une sortie tronquée, et on ne
déclare absent que ce qu'on a cherché par son nom.

## 2. Périmètre des articles relevés — onze, non quatre

Le mandat nomme les articles 34, 42, 44 et 47. Les quatre ne se tiennent pas seuls : la règle de
compensation (47) ne se lit qu'avec l'unité de vote (43), la spécialité et la fongibilité
asymétrique (7), les titres (5), le couple AE/CP (8) ; et la frontière avec la gestion suppose
les articles 11, 12 et 15.

**Tranché** : les onze articles sont relevés et cités. Le périmètre du mandat est tenu — rien
d'autre n'est digéré, et aucune pièce n'est rédigée.

## 3. Recueil des règles de comptabilité budgétaire — non récupéré

budget.gouv.fr rend `403` sur la page de documentation comme sur le PDF direct de la version
publiée. **Tranché** : la digestion sort sans lui, en le déclarant en tête et à la table des
autorités. Elle n'en dépend pas : la règle d'amendement de crédits est organique, et le recueil
porte l'exécution. À reprendre par pièce jointe si un lot touche l'exécution.

## 4. Versement de l'original — en attente, même cause que 1.A

Le dépôt se lit sans accréditation ; il ne s'écrit que s'il figure au jeu de dépôts autorisés en
écriture de la session. Le `push` est refusé. L'original du Guide du budgétaire 2023 n'est donc
pas versé sous `sources/`. Nom retenu quand l'écriture s'ouvrira, selon la règle de datation par
le millésime de la source : `guide_budgetaire_DB_2023.pdf`.

## 5. Indexation — les trois déclarations dues, écrites ici faute de pouvoir les poser

La digestion est versée au projet ; elle n'est **pas** déclarée à l'appareil, qui vit dans
`chantier/` au dépôt et que la session ne peut pas écrire. Les trois gestes sont tranchés, et
ils se calquent sur ceux de `structure_ppl` :

1. `appareil/generer_index.py`, table des documents externalisés —
   `'sources/regles_credits.md': 'reference/regles_credits.md'`
2. `appareil/generer_index.py`, `ALIAS_SOURCES` —
   `'sources/regles_credits.md': ['guide_budgetaire', 'guide_budgetaire_DB_2023.pdf']`
   Le renvoi `guide_budgetaire` résout ainsi sur la digestion, et le PDF d'origine n'entre pas
   au corpus par son fichier.
3. `appareil/generer_carte.py`, famille `méthode` —
   `("Règles d'amendement des crédits", ['sources/regles_credits.md'], None, None)`

Puis `make index`, `make controle`, et l'original sous `sources/guide_budgetaire_DB_2023.pdf`.
**Tant que ces trois lignes ne sont pas posées, un renvoi `guide_budgetaire` ne résout pas** :
la digestion existe, l'index l'ignore.
