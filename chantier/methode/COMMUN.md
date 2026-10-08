# Règles communes aux lots de nuit — 20261005

Tu écris des amendements déposables au PLF 2027 (texte n° 3210) ou au PLFSS 2027 (n° 3211),
pour le projet Résolution. Tu travailles seul, sans poser de question. Ce que tu ne peux pas
trancher se note en une ligne, question fermée, à la fin de ton fichier d'état.

## Où sont les choses (lecture seule, sauf ton domicile)

- **Droit en vigueur** : extrait LEGI local, `/home/claude/droit/` (`_manifeste.json`, puis
  `<code>.jsonl.gz`, une ligne par version d'article : `num`, `etat`, `date_debut`, `date_fin`,
  `texte`). Outil : `import sys; sys.path.insert(0,'/home/claude/audit'); import droit;
  droit.statut('cgi','219')` rend `(verdict, enregistrement)`. **Seul l'état `VIGUEUR` compte.**
  `ABROGE_DIFF` = en vigueur avec fin programmée (2222-02-22 = date indéterminée) ;
  `VIGUEUR_DIFF` = à venir. **La TVA est recodifiée au livre II du code des impositions sur les
  biens et services (CIBS) au 1er janvier 2027** : vise les articles du CIBS en `VIGUEUR_DIFF`
  quand la mesure s'applique en 2027 ou après, et dis-le. Table de passage :
  `/home/claude/work/passage_tva_cgi_cibs_20261005.tsv`.
- **Texte déposé** : `/home/claude/r27/chantier/referentiels/socle_texte_plf2027.json` et
  `socle_texte_plfss2027.json` (champ `articles` : `numero`, `intitule`, `dispositif`) ;
  articles ouverts : `.../articles_ouverts_plf2027.tsv`, `..._plfss2027.tsv`.
- **Annexes chiffrées (vérité des montants)** : `/home/claude/work/synthese_calculs.xlsx`
  (onglets `Refonte fiscalité`, `Flux`, `Détail Niches`, `Détail Economies`, `CSG-CRDS`,
  `Annexe Manuscrit`, `Input Capitalisation`) ; `/home/claude/work/annexe2.xls` (taxes
  affectées) ; `/home/claude/work/annexe3.xls` et `annexe3_chiffrages.json` (dépenses fiscales,
  onglet `Chiffrages Résolution`). Lis avec openpyxl / xlrd, cellules ciblées.
- **Coffre local** (`/home/claude/coffre/`) : `methode/objectifs_depot_2027.md` (le fond, fait
  foi), `methode/plan_liasse_2027_20261005.md` (la mécanique), `livrables/registre_colonnes_depot_2027.md`,
  `livrables/registre_sources_gage.md`, `referentiels/sort_prelevements_20260930.tsv` (sort de
  chaque prélèvement), `referentiels/concours_discretionnaires_collectivites_20261004.md`,
  `methode/clause_type_gage_20261002.md`, et deux pièces modèles de forme :
  `livrables/piece_4_4_taxe_fonciere_unique.md`, `livrables/lot_4_3_aide_fondamentale_et_taux_unique.md`.
- **Gabarits** : `/home/claude/r27/chantier/reference/gabarit_expose_sommaire.md`,
  `/home/claude/r27/chantier/reference/structure_ppl.md`.
- **Projet claude.ai** (outil `Projects`, `project_read` / `project_search` seulement — **n'écris
  jamais au projet, ne supprime rien**) pour les pièces absentes du coffre local.

## La mécanique — ne pas confondre

- **Circuit A, restitution** : parts restituées des niches, dépenses supprimées, aides ciblées ;
  fermé par la baisse de CSG et de CRDS puis le compte d'épargne. Pièce de dépense : phrase
  « La présente mesure concourt à la réduction des prélèvements pesant sur les revenus
  d'activité. »
- **Circuit B, refonte** : taxes supprimées, contre le solde non restitué des niches, le gisement
  (taux réduits de TVA, DMTG) et **l'impôt sur les sociétés et la taxe foncière unique, qui
  varient en dernier**. Taux plein de TVA fixe. Gage d'une pièce B qui perd une recette :
  « La perte de recettes pour l'État est compensée, à due concurrence, par la majoration du taux
  de l'impôt sur les sociétés prévu à l'article 219 du code général des impôts. » — pour les
  collectivités : « La perte de recettes pour les collectivités territoriales est compensée, à
  due concurrence, par la majoration de la dotation globale de fonctionnement. La perte de
  recettes pour l'État est compensée, à due concurrence, par la majoration du taux de l'impôt
  sur les sociétés prévu à l'article 219 du code général des impôts. »
- **Circuit C, aide fondamentale** : impôt sur le revenu à taux unique égal à l'aide
  fondamentale, revenus de 2028 (N+1).
- Un euro n'appartient qu'à un circuit. Aucune niche nommée ne gage une pièce B.

## Règles de rédaction

- **N'invente aucune adresse ni aucun montant.** Chaque article visé est lu sur l'extrait au
  moment d'écrire ; chaque montant vient d'une cellule nommée (onglet, cellule). Un doute : « à
  vérifier », jamais une approximation.
- Rédaction positive. Pas de point-virgule dans le texte normatif. Typographie française
  (espaces insécables devant ; : ! ? », apostrophe typographique). Séparateur de milliers : une
  espace.
- Dates : jamais un 31 décembre comme terme ; un 1er janvier ou un 1er juillet.
- Gabarit d'une pièce : cartouche (titre, chapô, intention, mesures) ; `AMENDEMENT` ; accroche
  (`ARTICLE n` ou `ARTICLE ADDITIONNEL — APRÈS L'ARTICLE n, insérer l'article suivant :`) ;
  dispositif en I, II, III… ; entrée en vigueur ; phrase de restitution ou gage ; `EXPOSÉ
  SOMMAIRE` (court, une idée par paragraphe, aucun nom de référentiel interne, aucune
  nomenclature du corpus) ; puis bloc `[interne]` : sources des montants (onglet, cellule),
  verdict de chaque adresse au droit (`EXISTE` / `VIGUEUR_DIFF` / `ABROGE_DIFF`), points à
  vérifier.
- En-tête de chaque fichier : **Porteur** (lot Nn), **Mandat** (plan de liasse du 20261005),
  **Domicile** (chemin dans le paquet), **Mesure** (le compte d'entrée : nombre d'articles
  visés, contrôlés).

## Contrôle avant de rendre

Rejoue toi-même le contrôle des adresses : extrais toutes les références « article X du code Y »
de tes pièces et passe-les à `droit.statut`. Rien d'`ABSENT` ni d'`ABROGE` ne sort. Note le
compte dans ton fichier d'état.

## Ce que tu rends

1. Tes pièces, dans ton domicile seulement :
   `/home/claude/versement_20261005/chantier/livrables/depot_2027/<P1|P2|SS|sans_colonne>/<nom>.md`.
2. Un fichier d'état `/home/claude/versement_20261005/etats/<lot>.md` : pièces écrites, adresses
   contrôlées (compte et verdicts), montants et leur cellule, ce qui reste, questions fermées
   pour l'auteure (une ligne chacune, trois au plus).
3. En réponse finale : cinq lignes au plus — fichiers écrits, compte des adresses contrôlées,
   points bloquants.

Tu ne touches à aucun autre fichier : ni coffre, ni dépôt cloné, ni projet.
