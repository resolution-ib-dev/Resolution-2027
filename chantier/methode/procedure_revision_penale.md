# Procédure — révision accélérée de la chaîne pénale, strate par strate

Pièce de méthode. Ouverte le 20261019. Elle dit comment on révise la procédure
pénale et les codes de la chaîne pénale : d'abord la partie réglementaire (R, D,
A), puis la partie législative (L), sous la doctrine du livre.

## Ce que l'auteur a arrêté (validé)

- La révision se conduit **par strate** : la partie réglementaire d'abord, la loi ensuite.
- Le **guide d'interprétation**, ce sont les lectures les plus rigoureuses de la DDHC
  sur **la propriété et la sûreté**.
- Les arguments du Conseil constitutionnel se **retournent** : il faut cesser de punir
  collectivement les contribuables et les innocents.
- On fait **au plus simple et au plus efficace**, selon la doctrine du livre.
- On peut s'appuyer sur des sources de confiance.

## Ancrage doctrinal (livre EP3)

| folio | énoncé |
|---|---|
| 16 | « Un État inefficace est la pire des injustices. L'État existe pour nous protéger de la loi du plus fort. » |
| 68 | Mission Intérieur : « assurer la sécurité de nos personnes et de nos biens » ; mission Justice : « l'égalité devant la loi suppose […] de la faire respecter équitablement ». |
| 69 | « Assurer la sécurité de tous les citoyens, jusqu'aux plus pauvres et plus faibles […] est une dépense sociale par excellence. » |
| 92-93 | « Un droit plus simple, c'est une justice plus rapide, donc plus humaine. » « des peines rapides et complètes, conformément à la volonté des citoyens exprimée par le législateur ». |
| 93 | La charge de la preuve incombe à la norme : elle démontre sa nécessité et sa proportionnalité. |
| 94 | Les régimes d'autorisation font peser sur les citoyens honnêtes une charge qui ne devrait incomber qu'à ceux qui enfreignent les règles. |
| 96 | Un « code essentiel » de quelques dizaines de pages par domaine. |

## Grille DDHC (proposé — à valider par l'auteur)

Lecture retenue : la sûreté est la protection effective de la personne et des
biens contre l'atteinte d'autrui, et pas seulement la garantie contre une
arrestation arbitraire. La force publique est instituée pour l'avantage de tous
(art. 12). Son coût est une contribution commune (art. 13) dont l'emploi doit
être constaté et suivi (art. 14).

| article | lecture rigoureuse | effet sur une disposition de procédure |
|---|---|---|
| 2 | La sûreté et la propriété sont des droits que l'association politique *conserve* : c'est une obligation de résultat. | Une formalité qui retarde la protection doit prouver sa nécessité. |
| 12 | Le but de la force publique, c'est l'avantage de tous. | Est suspecte une procédure qui sert l'organisation interne au lieu du justiciable. |
| 13-14 | Le contribuable paie la force publique et en constate l'emploi. | Le coût d'une étape (temps OPJ, greffe, expertise) se mesure et se justifie. |
| 17 | La propriété est inviolable. | La victime d'une atteinte aux biens est indemnisée vite. La saisie et la confiscation du produit de l'infraction sont la règle. |
| 8 | Les peines sont strictement et évidemment nécessaires… et « légalement appliquée[s] ». | Une peine prononcée et non exécutée viole l'article 8 autant qu'une peine excessive. |
| 9 | Toute rigueur inutile envers la personne arrêtée est réprimée. | Cette limite tient. On la respecte sans en tirer un formalisme de nullité. |
| 16 | Garantie des droits. | Elle couvre les droits de la victime et ceux du tiers, pas seulement ceux de la personne poursuivie. |

### Arguments du Conseil constitutionnel à retourner (proposé)

Le Conseil reconnaît lui-même les objectifs qui jouent pour la révision. On leur
donne le poids maximal dans sa propre balance.

| jurisprudence | ce qu'elle dit | usage |
|---|---|---|
| CC 80-127 DC, 20 janv. 1981 | La recherche des auteurs d'infractions est nécessaire à la sauvegarde de droits de valeur constitutionnelle. | La sûreté de la victime entre dans la balance au même rang que la liberté du suspect. |
| CC 2003-467 DC, 13 mars 2003 | La prévention des atteintes à l'ordre public est un objectif de valeur constitutionnelle. | Elle fonde les mesures de flux et de capacité. |
| CC 2009-595 DC, 3 déc. 2009 | La bonne administration de la justice est un objectif de valeur constitutionnelle. | Délais, purge des nullités, audiencement. |
| CC 2003-473 DC, 26 juin 2003 | Le bon usage des deniers publics est une exigence constitutionnelle (art. 14 et 15 DDHC). | Coût par étape, argument « contribuables ». |
| CC 2007-554 DC, 9 août 2007 | Les peines minimales sont conformes si le juge garde l'individualisation. | Modèle de rédaction des seuils. |
| CC 2010-14/22 QPC, 30 juil. 2010 | La garde à vue sans avocat est censurée. | C'est la limite : on la contourne par la capacité, pas par la suppression du droit. |
| CC 2026-909 DC, 23 juil. 2026 | Généalogie génétique et portrait-robot génétique censurés faute d'encadrement. | Toute mesure d'enquête intrusive porte son encadrement dans le texte. |

**Murs tenus (pas de révision prévue)** :

- art. 66 C ;
- art. 9 DDHC, présomption d'innocence ;
- individualisation des peines ;
- art. 3 CEDH ;
- contrôle du juge sur toute privation de liberté.

Une mesure qui les franchit sort du plan et va à `analyse-transposabilite`.

Toutes les références de décisions sont à confronter au texte des décisions
avant tout livrable diffusable.

## Les huit étapes

1. **Cartographier.**
   - `appareil/codes_git.py` extrait les codes de la chaîne pénale : un fichier
     par article, rangé par partie (L, R, D, A).
   - Il étiquette chaque article selon sa friction : délai, autorisation, avis,
     nullité, seuil, formalité, compétence.
   - Sorties : `revision/codes/` et `referentiels/frictions_penal.tsv`.
2. **Mesurer.**
   - Chaque friction retenue reçoit un coût : délai, stock, temps d'agent.
   - Sources : annuaire statistique de la Justice et rapports budgétaires
     (`REF_chiffres`).
   - Une friction sans coût mesuré ne monte pas en tête de liste.
3. **Classer par strate.**
   - Classes : R autonome (art. 37 C), R d'application (renvoi de la loi), L, LO,
     ou mur.
   - Skills : `vecteur-mesure`, `analyse-transposabilite`.
4. **Paquet réglementaire.**
   - Décret en Conseil d'État (R), décret simple (D), arrêtés (A).
   - Avis de la CNIL dès qu'il touche des données.
   - Base légale verrouillée article par article, contre le référé-suspension.
5. **Paquet législatif.**
   - Véhicule préféré : la loi de ratification de l'ordonnance n° 2025-1091, qui a
     un lien direct avec le CPP. À défaut, un projet en procédure accélérée.
   - Pré-test devant `contestabilite` sur la grille ci-dessus.
   - Rédaction : `disposition-cible`, puis `redaction-legistique`.
6. **Décrets d'application.** Ils s'écrivent pendant la navette et se publient la
   semaine de la promulgation.
7. **Moyens.** Crédits en loi de finances (places, OPJ, greffe, expertise), par la
   chaîne d'amendements de crédits.
8. **Mesure ex post.** Quatre ou cinq indicateurs fixés à l'étape 2, publiés chaque
   trimestre.

**Double numérotation** : le nouveau CPP issu de l'ordonnance n° 2025-1091
s'applique au 1er janvier 2029. Toute disposition se rédige dans le code actuel
et dans le code de 2029, avec la table de concordance. La base porte déjà les
4 184 articles L du code de 2029. Elle porte aussi les premiers articles R et D
issus du décret n° 2026-907 du 30 septembre 2026.

## Codes de la chaîne pénale

| code | court | dans la base au 20261019 |
|---|---|---|
| code de procédure pénale | cpp | oui (L, R, D, A, versions actuelle et 2029) |
| code de la sécurité intérieure | securite_interieure | oui |
| code pénal | cp | ajouté au 20261019, extrait au prochain passage de l'action |
| code pénitentiaire | penitentiaire | idem |
| code de l'organisation judiciaire | coj | idem |
| code de la justice pénale des mineurs | cjpm | idem |
