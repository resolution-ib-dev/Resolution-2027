# Prompt du fil design graphique (20260924)

Fil Cowork neuf, projet Résolution. Pièce jointe : `fiche.css` du site, à demander au fil code (« rends-moi `fiche.css` en clair, intégral ») ou à copier depuis le dépôt `Site-ETNP`. Sans elle, le fil est aveugle sur la charte et ne doit pas produire.

---

Projet Résolution, chantier site, design graphique.

**Lis d'abord** `areas/site_etnp.md` et `preferences.md` en mémoire projet ; puis au projet `livrables/etat_site_20260921.md` § « graphiques thématiques », `livrables/ecart_classeurs_20260917.md` § 5, `livre/index_livre_EP3.md`. Charge la skill `dataviz` avant la première ligne de code.

**Charte.** Celle du site, et elle seule : le `fiche.css` joint fait foi pour les couleurs (ses variables), les polices — Archivo aux titres, petites capitales et chiffres, Source Serif 4 au texte — et les espacements. Aucune valeur inventée ni approchée ; pas l'esthétique provisoire Fraunces / JetBrains du projet. Si `fiche.css` n'est pas joint : mesure, dis-le, arrête-toi.

**Matière.** `Synthèse Graphiques Résolution_0910.xlsx`, pièce du projet, douze onglets — `GraphGov`, `GraphRDB`, `GraphVA`, `GraphCodes`, `Graph51pc`, `Graph1672Md`, `GraphETP`, `Graph236`, `GraphAgences`, `GraphPatrimoine`, `GraphIR`, `GraphAFU`. Chaque onglet porte un graphique déjà construit par l'auteure au-dessus de ses données, et pour sept d'entre eux une adresse de source en tête d'onglet.

**Mandat : reprendre les douze graphiques existants et les rendre dans la charte du site. Pas de redessin.** Pour chaque graphique, relever dans le classeur son type, ses séries, ses libellés, son titre, son ordre et ses unités, et les reproduire à l'identique ; ne changent que la police, les couleurs, les corps et la mise en page. Rendu par graphique : HTML autonome + PNG haute définition, lisible sur mobile, source en pied (l'onglet, et l'adresse inscrite en tête d'onglet quand il y en a une). Chaque chiffre affiché est traçable à sa cellule.

**Deux temps, chacun s'arrête.**
1. **`Graph236`, la vedette** — le tableau des 236 Md€ d'économies, aussi au folio 170 du livre (`livre/texte_livre.json`). Il doit ressortir plus que les autres. Rendu en clair (le PNG affiché dans la réponse), validation de l'auteure, arrêt.
2. **Sur go seulement** : les onze autres, un par un, même gabarit, chacun affiché en clair.

**Ce que le fil ne fait pas.** Aucun CSS de site, aucune page, aucun placement : ce sont des pièces. Le placement est acquis — « pour approfondir » dans les fiches et le manifeste, page Données qui rassemble — et se fera par le fil code après validation. Aucune autre pièce que les graphiques nommés. Pas d'export PDF sans go.

**Livrable de clôture** : les fichiers HTML et PNG, versés au projet sous `livrables/graphiques/`, et une ligne par graphique — onglet, type, source. Rien d'autre.
