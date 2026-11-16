# Tri des prélèvements — ce qui se tranche avant mise en ligne — 20261020

Classeur public : `livrables/tri_public/Tri des prélèvements Résolution.xlsx`,
écrit par `appareil/generer_tri_public.py` depuis
`referentiels/sort_prelevements_20261015.tsv`. Carte de la page « Données »
préparée sur la branche `claude/clever-euler-rbeck4` de Site-ETNP, sans pull
request.

## Tranché par l'auteur le 20261020, appliqué

- **Les cotisations sociales** (81 rangs) : sort « cotisations sociales à
  unifier », hors de la refonte fiscale.
- **Le reste se reconstruit sur les tableaux annexes** : chaque poste du schéma
  « Refonte fiscalité » confronté aux rangs du tri
  (`appareil/passage_schema_tri.py` → `passage_schema_tri.tsv`, onglet « Par
  poste du schéma » du classeur public). Corrections tirées du schéma et de la
  composition INSEE de ses postes :
  - **jeux** (10 rangs, 6,7 Md€) : maintenus à part, comme le poste « alcool,
    tabac, jeux » que le schéma maintient (25,3 sur 25,6) ;
  - **électricité** (3 rangs, 5,2 Md€) : fondue dans la TVA ; le schéma
    supprime 8 Md€ d'énergie, l'accise sur l'électricité hors bouclier, et le
    motif du tri le disait déjà (« l'électricité n'est pas un produit à effets
    négatifs ») ;
  - **taxe de solidarité additionnelle** (6,7 Md€) : au poste « assurances »,
    maintenu, où l'INSEE la compte (19,2 = 11,3 + 6,2 + 1,7) ;
  - **majoration de la taxe sur les assurances de protection juridique** :
    maintenue avec son poste ;
  - **contributions sur les indemnités de rupture et de mise à la retraite** :
    au poste « Taxes sur la main d'œuvre », où l'INSEE les compte (D291) ;
  - **TTF et opérations à haute fréquence** : au poste « autres taxes sur les
    produits », fondu dans la TVA.

## Reste ouvert, déclaré au tableau de passage

- **Alcool, tabac, jeux** : 0,3 Md€ supprimés au schéma, aucun rang identifié.
- **Services de transports** : 3,6 Md€ rangés en 2026 pour 1,9 au schéma en
  2024 (taxe d'aéroport, taxe sur la distance autoroutière) ; sort cohérent.
- **Taxe sur les boissons sucrées** (0,97) et contribution sur les boissons
  édulcorées : fondues au poste « autres taxes sur les produits » ; l'INSEE les
  compte peut-être avec les alcools, poste maintenu. Non prouvé.
- **Contribution tarifaire d'acheminement** (2,2) : au poste « autres taxes sur
  les produits », dont la composition INSEE ne la porte pas. Non localisée.
- **Motifs** : pas de colonne publique ; textes du « Lisez-moi » et de la carte
  à relire.

## Relevé, sans décision attendue

- 420 prélèvements ; rendement publié pour 234, 877,1 Md€ ; vide pour 186.
- Siège juridique pour 402 rangs ; les 18 autres sont des agrégats, des
  créations du PLF, des sièges réglementaires ou les 5 n.d. arbitrés.
- Le classeur interne `Tri_prelevements_20261015.xlsx` est en retard sur le tri
  qui fait foi (sièges relevés les 16 et 19 octobre, onglet « Ce qui reste à
  lever ») : il ne se publie pas, le classeur public le remplace.
