# Les annexes des voies et moyens du PLF 2027 — registre de digestion

**Le corpus porte la totalité des annexes des voies et moyens du PLF 2027.** Il
n'y en a aucune à demander à l'auteur, et aucune à retélécharger. Cette pièce
dit, pour chacune, quel classeur, quelle empreinte, quelle table, quelle option
du script et quel défaut relevé.

Elle se lit **avant** de conclure qu'une matière de recettes, de dépenses
fiscales ou de taxes affectées n'est pas au dépôt, et avant d'ouvrir un fil qui
toucherait à l'une d'elles.

Les classeurs sont des pièces jointes : documents publics, retéléchargeables à
l'identique, qui **ne se versent pas** (A-234, A-235). Ce qui se verse, c'est
leur table plate, et chaque table porte en tête le SHA-256 du classeur dont elle
sort. Une table se réapplique par `verifier`, qui la compare à l'octet à ce que
redonne le classeur et joue son jeu de quatre fautes.

---

## Les sept annexes, en dix tables

| annexe | SHA-256 du classeur | table versée | lignes | option |
|---|---|---|---|---|
| tome I, annexe 1 — évolution des recettes du budget général | `a5179763…913468` | `referentiels/annexe_recettes_bg_2027.tsv` | 202 | `--rb` |
| *la même* — mesures nouvelles | *le même* | `referentiels/annexe_mesures_nouvelles_2027.tsv` | 24 | `--rb` |
| tome I, annexe 2 — ressources affectées | `2f5e4cd1…6c6b122` | `referentiels/annexe_ressources_affectees_2027.tsv` | 293 | `--ra` |
| tome II, annexe 1 — dépenses fiscales | `f0f0eac4…891e89` | `referentiels/annexe_depenses_fiscales_2027.tsv` | 459 | `--df` |
| tome II, annexe 2 — évolution des dépenses fiscales, bilan | `c06c60e4…13a1d72` | `referentiels/annexe_evolution_df_bilan_2027.tsv` | 115 | `--ev` |
| *la même* — dépenses bornées | *le même* | `referentiels/annexe_evolution_df_bornees_2027.tsv` | 65 | `--ev` |
| tome II, annexe 3 — TVA toutes APU | `b6999380…ef7c430` | `referentiels/annexe_tva_apu_2027.tsv` | 44 | `--tva` |
| tome II, annexe 4 — indicateurs de performance | `519fa0ba…23fbb11` | `referentiels/annexe_indicateurs_performance_2027.tsv` | 44 | `--ind` |
| tome II, annexe 5 — top 8 des dépenses d'IR | `57449131…4ad930f6` | `referentiels/annexe_deciles_ir_2027.tsv` | 8 | `--dec` |
| *la même* — répartition par tranche de RFR | *le même* | `referentiels/annexe_deciles_ir_repartition_2027.tsv` | 150 | `--dec` |

**Il n'y a pas d'annexe 3 au tome I** : l'auteur l'a dit le 20261019. Ne pas la
chercher, ne pas la demander.

**Appel complet**, les six classeurs étant sous `<dossier>` :

```
python3 appareil/digerer_annexes_vm2027.py verifier \
  --df "<dossier>/… Tome 2 - Annexe 1 …"  --ra "<dossier>/… Tome 1 - Annexe 2 …" \
  --rb "<dossier>/… Tome 1 - Annexe 1 …"  --ev "<dossier>/… Tome 2 - Annexe 2 …" \
  --tva "<dossier>/… Tome 2 - Annexe 3 …" --ind "<dossier>/… Tome 2 - Annexe 4 …" \
  --dec "<dossier>/… Tome 2 - Annexe 5 …"
```

Un classeur absent laisse ses tables intactes et `verifier` ne se prononce pas
sur elles : **une table non éprouvée n'est pas une table prouvée.**

---

## Où va se servir un fil, selon ce qu'il cherche

| la question | la table |
|---|---|
| combien l'État attend d'un impôt en 2027 | `annexe_recettes_bg_2027.tsv`, colonne `evaluation_proposee_2027` |
| ce que le texte déposé fait déjà d'une recette | `annexe_mesures_nouvelles_2027.tsv` |
| ce qu'une taxe affectée rapporte, et son plafond | `annexe_ressources_affectees_2027.tsv` |
| ce que coûte une dépense fiscale, et à qui | `annexe_depenses_fiscales_2027.tsv` |
| **si une dépense fiscale est déjà supprimée ou modifiée** | `annexe_evolution_df_bilan_2027.tsv` |
| **si une dépense fiscale est déjà bornée ou éteinte** | `annexe_evolution_df_bornees_2027.tsv` |
| ce qu'une mesure de TVA coûte au-delà de la part État | `annexe_tva_apu_2027.tsv` |
| quel indicateur de performance suit une dépense fiscale | `annexe_indicateurs_performance_2027.tsv` |
| comment une dépense fiscale d'IR se répartit par revenu | `annexe_deciles_ir_repartition_2027.tsv` |

**Conséquence pour la rédaction d'un amendement fiscal** : avant de proposer la
suppression d'une dépense fiscale, ouvrir le bilan et les dépenses bornées. Une
dépense déjà supprimée par la loi de finances pour 2026, ou dont le fait
générateur est éteint, ne se supprime pas une seconde fois — et l'économie qu'on
lui prêterait est déjà acquise au tendanciel.

---

## Ce que chaque table porte, et ce qu'elle ne porte pas

**Recettes du budget général.** Les trois onglets de détail — `RFN` fiscales
nettes, `RNF` non fiscales, `R&D` remboursements et dégrèvements — avec
exécution 2025, évaluation révisée 2026 et évaluation proposée 2027, plus les
quatre colonnes qui expliquent l'écart. **193 des 202 lignes portent un code de
ligne budgétaire** ; les neuf autres sont des agrégats de niveau. Les onglets de
synthèse et les onglets `*_format_courant` ne sont pas digérés : les premiers
agrègent ce que les seconds redisent à nomenclature constante, et une somme se
recompte.

**Mesures nouvelles.** Les 24 mesures de recettes du texte déposé, chacune avec
sa ligne budgétaire. Le total de l'onglet, **14 331 914 894 €**, se recompte sur
ces 24 lignes et se recoupe avec les 13 931 914 894 € portés en colonne
« mesures nouvelles » des recettes fiscales nettes, plus les 400 M€ du
prélèvement CNIEG, qui est une recette non fiscale.

**Bilan des mesures sur les dépenses fiscales.** 115 mesures, avec leur sort, le
texte et l'article qui les portent, et leur effet sur 2026 et 2027. **Un signe
positif est une économie.** Les trois totaux de pied se recomptent exactement :
suppressions +56 et +2 142, créations −17 et −427, solde +39 et +1 715 M€.

**Dépenses bornées.** 65 dépenses, dont 9 parvenues à échéance et 56 au fait
générateur éteint, ces dernières rangées sous leur année d'extinction, de 1996 à
2025.

**TVA toutes APU.** 44 mesures, **39 dépenses fiscales et 5 modalités
particulières**, chacune chiffrée au PLF 2026 puis au PLF 2027, sur trois
exercices chaque fois. C'est la seule pièce qui chiffre une mesure de TVA
au-delà de la part État. Les cinq modalités particulières n'ont pas de numéro au
référentiel des dépenses fiscales — c'est leur nature, non un manque.

**Indicateurs de performance.** 44 couples indicateur × dépense fiscale, pour
**21 indicateurs**, chacun avec sa mission et son programme. **Onze dépenses
fiscales relèvent des impôts locaux** et n'ont donc pas de ligne au référentiel
des dépenses fiscales de l'État — c'est le périmètre, non un manque.

**Ventilation par décile.** Les 8 dépenses fiscales d'impôt sur le revenu du
« top 8 », et la répartition par tranche de revenu fiscal de référence pour
celles qui en publient une : **5 sur 8**, à raison de dix tranches et de trois
millésimes de revenus — 2022, 2023, 2024 — soit 150 lignes. Les trois dépenses
sans ventilation sont **120108**, **120146** et **120202** ; l'écart se relève,
il ne se comble pas.

---

## Les défauts relevés, qui sont ceux des pièces

Aucun n'est corrigé : la digestion verse le verbatim et porte le verdict.

- **Annexe 5, dépense 120401, millésime 2024** : le `TOTAL` du coût vaut
  5 347 000 là où ses dix tranches font 5 347 — un facteur mille entre le total
  et ses parts. Les dix lignes portent `ecart:cout` en colonne `controle_bloc`.
  **Aucun livrable ne cite ce bloc sans dire lequel des deux chiffres il
  retient.**
- **Annexe 5, dépense 120401, millésimes 2022 et 2023** : les tranches ne sont
  pas dans la même unité qu'en 2024. Chaque bloc concorde avec son propre total,
  et c'est tout ce que le contrôle prouve. **Le millésime fait partie de la
  clé** : des tranches de millésimes différents ne s'additionnent jamais.
- **Annexe 2, dépenses au fait générateur éteint, exercice 2027** : le total dit
  2 189 M€, les 56 lignes en font 2 179. Écart de 10 M€, interne au classeur ;
  2025 et 2026 concordent exactement. L'écart est porté au pied de la table.

---

## La question des rendements manquants est close

Les **186 rangs sans rendement 2026** du tri des prélèvements ont été éprouvés
contre **toutes** les sources disponibles :

| source | éprouvée le | rangs comblés |
|---|---|---|
| annexe des ressources affectées (T1 A2) | 20261016 | 2 |
| état A du texte déposé | 20261016 | 0 |
| liste IFRAP | 20261016 | 0 |
| recettes du budget général (T1 A1) | 20261019 | 0 |
| annexes du tome II — dépenses fiscales, évolution, TVA, indicateurs, déciles | 20261019 | 0 |
| annexe des taxes affectées du PLF 2026 | 20261019 | 0 |
| onglet « Refonte fiscalité » du classeur de calculs | 20261019 | 0 |

**Aucune pièce disponible ne porte ces rendements**, et la raison est une
disjonction de périmètre, non un défaut de jointure : les 186 rangs sont **93
cotisations sociales** et **92 taxes affectées à des tiers**, là où les voies et
moyens portent le budget général et les taxes plafonnées. La pièce qui les
porterait est hors du périmètre des annexes du PLF.

**Le point est clos, et il ne se rouvre pas sans une source nouvelle.** Un fil
qui le rouvrirait referait sept mesures déjà faites. Les 186 rangs restent
déclarés sans rendement, et le référentiel garde son défaut déclaré.

---

## Ce qui reste à faire de ces tables

- **Recaler le tri des prélèvements sur 2027.** 17 rangs du tri se retrouvent
  aux recettes du budget général. La jointure sur libellé **ne tient pas** : le
  même intitulé y porte une ligne brute, une ligne nette et des sous-lignes, et
  elle fabrique des écarts absurdes — l'impôt sur les sociétés passerait de 84,7
  à 48,5 Md€. **Le recalage demande un appariement sur le code de ligne
  budgétaire**, que le tri ne porte pas encore. Rien n'a été recalé.
- **Éprouver les mesures fiscales du corpus contre le bilan des mesures.** Une
  dépense fiscale déjà supprimée ou déjà bornée change le rendement qu'on prête
  à sa suppression.
- **Croiser la TVA toutes APU avec le sort des prélèvements.** La part non-État
  d'une mesure de TVA n'est chiffrée que là.
