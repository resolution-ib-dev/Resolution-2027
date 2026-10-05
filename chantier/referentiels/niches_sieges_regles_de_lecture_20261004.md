# Relevé des sièges de niches — règles de lecture — 20261004

Pièce : `referentiels/niches_sieges_20261004.tsv`, 465 lignes, 157 Ko, domicile au coffre.
Elle lève la dépendance bloquante posée au § 4 de l'arbitrage du 20261004 et au § 7-5 de
`livrables/lot_3_1_niches_clause_generale_20261002.md` : la liste énumérée de l'article 2.

## 1. Mesure d'entrée

| mesure | valeur |
|---|---|
| lignes portées par l'annexe des dépenses fiscales | **465** |
| lignes portant une référence juridique renseignée | **465** |
| lignes portant un siège d'article exploitable | **461** |
| lignes sans siège légal identifiable | **4** |

Les quatre sont des dépenses fiscales dont l'annexe ne donne qu'une référence de doctrine
administrative : 120142 (prise en charge directe de prestations d'action sociale,
BOI-RSA-PENS-10-30), 150704 (gains d'opérations de bourse des clubs d'investissement,
BOI-RPPM-PVBMI-10-30-10), 160301 et 160302 (déductions forfaitaires des médecins
conventionnés, BOI-BNC-SECT-40). **Aucun siège ne leur a été inventé.** Une abrogation
nominative ne les atteint pas ; seule la clause générale du I les emporte.

## 2. Source et millésime

Annexe 3 au tome II du PLF 2026, version du 10 septembre 2026 — onglets « Références
juridiques », « Chiffrages », « Échéances », joints sur le numéro de dépense fiscale,
465 contre 465, aucun orphelin de part ni d'autre.

Le millésime du droit est celui de l'annexe, non celui du dépôt du PLF 2027.
**Toute adresse reprise en disposition modificative se recontrôle au dépôt de droit au
millésime du texte en discussion** avant emploi, conformément à la règle du corpus.

## 3. Colonnes

`numero` · `categorie` (catégorie / sous-catégorie / sous-sous-catégorie) ·
`objet_en_clair` (libellé législatif intégral) · `code_ou_texte_porteur` ·
`siege_article` (verbatim de l'annexe, préfixe `#` retiré) · `montant_M_EUR` ·
`millesime_montant` · `fin_fait_generateur` · `niveau_de_confiance` · `observation`.

## 4. Niveau de confiance — barème appliqué

- **haute** (434) : code ou loi identifié, adresse d'article isolée ou liste courte sans
  renvoi réglementaire.
- **moyenne** (27) : adresse exacte mais multiple — plus de trois articles liés, ou renvoi
  à une annexe du code général des impôts. L'adresse n'est pas douteuse ; c'est le découpage
  en abrogations distinctes qui demande un arbitrage de rédaction. Cas type : les chaînes
  de crédit d'impôt `244 quater X / 199 ter X / 220 X / 223 O-1-x`, qui ne s'abrogent pas
  par un seul alinéa.
- **non identifiable** (4) : doctrine seule, § 1.

## 5. Codes et textes porteurs

| porteur | lignes |
|---|---|
| code général des impôts | 393 |
| code des impositions sur les biens et les services | 54 |
| lois de finances et lois non codifiées | 8 |
| code des douanes | 5 |
| doctrine administrative seule | 4 |
| code général des collectivités territoriales | 1 |

## 6. Chiffrage, et le contrôle qu'il passe

324 lignes chiffrées, 141 non chiffrées — dont 91 marquées `nc` et 50 marquées `ε`.
Le montant retenu est la prévision 2026 quand elle existe (434 lignes), à défaut la
prévision 2025 (26), à défaut la réalisation 2024 (5) ; `millesime_montant` dit laquelle.

**Contrôle passé** : 305 lignes portent une prévision 2026 numérique, pour
**79 613 M€** — exactement le total relevé au § 3 du lot 3.1. Le référentiel et la pièce
de lot se recoupent à l'unité.

## 7. Ce que la pièce ne porte pas, et qui est au périmètre

1. **Les niches sociales.** L'annexe des dépenses fiscales ne recense aucune exonération
   de cotisation ni exclusion d'assiette du code de la sécurité sociale. Les sièges de la
   jambe sociale — L. 242-1 II, L. 136-1-1 — sont relevés au § 6 du lot 3.1 et nulle part
   ailleurs. **Le relevé exhaustif de la jambe sociale reste dû et sa source n'est pas ce
   fichier.**
2. **Le code du travail.** Hors annexe par construction ; les deux sièges utiles,
   L. 3262-5 et L. 3261-9, sont relevés au § 5 du lot 3.1 (M-021).
3. **Les 80 modalités de calcul de l'impôt déclassées**, portées à part par le même
   fichier, ne sont pas des niches et ne sont pas au référentiel. Elles sont dans le champ
   de la clause générale (§ 7-3 du lot 3.1) et appellent leur propre relevé si une liste
   énumérée doit les atteindre.

## 8. Contrôle au droit en vigueur — 20261005

Colonne ajoutée : `etat_droit_20261001`. Pour chaque ligne, chaque article du siège est lu sur
l'extrait LEGI du dépôt public, millésime 20261001 ; seul l'état `VIGUEUR` vaut « en vigueur ».
Les subdivisions ne sont pas contrôlées dans cette colonne.

| verdict de la ligne | lignes |
|---|---:|
| en vigueur | 306 |
| fin programmée, version suivante en vigueur à la date de fin | 88 |
| TVA ou assimilé, article éteint au 1er janvier 2027 sans version suivante — recodifié au livre II du code des impositions sur les biens et services | 50 |
| abrogé ou sans version en vigueur | 14 |
| hors de l'extrait (lois non portées) | 2 |
| sans siège légal | 4 |
| en vigueur pour la loi, renvoi à une annexe réglementaire | 1 |
| **total** | **465** |

**Ce que la colonne commande.** Une adresse abrogée ne s'abroge pas ; une adresse éteinte au
1er janvier 2027 se reprend à son siège du code des impositions sur les biens et services
(`work`, table de passage TVA du 20261005, portée au § 9 de la clause générale). La clause
générale a été corrigée en conséquence le 20261005. **Les montants ne sont pas touchés.**
