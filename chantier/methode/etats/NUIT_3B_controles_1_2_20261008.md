# Contrôles de sortie 1 et 2 — phase 3.B de la procédure de nuit, dépôt 2027

**Porteur** : fil Cowork de contrôle de sortie, phase 3.B de la procédure de nuit, dépôt 2027, 20261008.
**Mandat** : `methode/procedure_nuit_20261008.md`, phase 3.B — jouer les contrôles 1 (adresses) et 2 (checklist rédactionnelle) sur la liasse, rendre des verdicts, ne corriger aucune pièce ; `methode/procedure_fin_de_chantier_depot_2027.md` § 6, contrôles 1 et 2 ; **les exposés ne sont pas contrôlés — un fil frère les régénère** ; **les contrôles 3 (rattachement) et 4 (contestabilité) ne sont pas joués — ils sont de la phase 4** ; **deux constats légués à mesurer et à rendre sans les trancher**.
**Domicile** : `methode/etats/NUIT_3B_controles_1_2_20261008.md`.
**Appui** : `methode/procedure_nuit_20261008.md` · `methode/procedure_fin_de_chantier_depot_2027.md`, § 0, § 0 bis (R-A, R-B), § 3 (R-C à R-G) et § 6 · `methode/controle_avant_transmission.md` · `methode/regles_redactionnelles.md`, **lue ligne à ligne : c'est le contrôle 2** · `methode/appui_des_passes.md`, table « type de passe → appui dû », R-G et R-H · `reference/guide_legistique.md`, partie IV (fiches 3.3.1, 3.4.1, 3.4.2, 3.8.1 à 3.8.3) · `methode/etats/NUIT_2_colonnes_20261008.md`, table des trois colonnes — **le périmètre** · `methode/etats/NUIT_2bis_versement_20261008.md` · `livrables/registre_exceptions_dates.md` · dépôt de droit cloné à `/home/claude/droit/`, **millésime LEGI 20261001**, et `chantier/referentiels/socle_texte_plf2027.json`.
**Mesure** : **63 pièces mesurées sous `livrables/depot_2027/`** · **2 844 occurrences d'adresse contrôlées, 1 428 adresses distinctes, millésime LEGI 20261001** · **22 occurrences `ABSENT` en 8 adresses distinctes, 11 occurrences `ABROGE` en 11 adresses distinctes** · **690 occurrences laissées hors contrôle, 4 motifs** · **85 blocs de dispositif isolés, 176 241 octets, 62 pièces porteuses** · **15 règles mécanisables jouées, 1 758 occurrences relevées, 1 436 écarts qualifiés après lecture** · **2 constats légués mesurés, 1 tranché, 1 rendu sans être tranché** · **0 pièce corrigée, 0 pièce ouverte, 0 exposé touché, 0 registre touché**.

---

## 0. Ce que ce fil a mesuré avant de contrôler

**Le paquet.** 63 fichiers sous `livrables/depot_2027/` — 30 en `P1/`, 18 en `P2/`, 10 en `SS/`, 4 en `sans_colonne/`, 1 à la racine (clause générale). La table des trois colonnes de `NUIT_2_colonnes_20261008.md` leur attribue **62 rangs actifs** répartis en P1 33 · P2 19 · SS 10, et 4 rangs vacants barrés.

**Le droit.** `python3 /home/claude/droit/droit.py etat` rend **millésime LEGI 20261001, fraîcheur 7 jours, 62 textes portés**. Tous les verdicts du contrôle 1 sont joués sur ce millésime et sur lui seul.

**Les dispositifs.** Le contrôle 2 ne porte que sur les dispositifs. Ils ont été isolés mécaniquement, du marqueur d'ouverture (`AMENDEMENT`, `## PROPOSITION DE LOI`, y compris en bloc cité) jusqu'à `EXPOSÉ SOMMAIRE`, `[interne]` ou `ANNEXE` : **85 blocs, 62 pièces porteuses, 176 241 octets**. Une seule pièce du paquet ne porte aucun dispositif — `P1/4_7_abrogations_cgi.md`, qui est une notice de péremption : c'est conforme, et c'est déclaré ici.

**Ce qui n'a pas été fait, et pourquoi.** Aucune pièce n'a été corrigée ni ouverte. Aucun exposé n'a été lu ni contrôlé : un fil frère les régénère en ce moment, et un verdict pris sur eux serait périmé en sortant. Les contrôles 3 et 4 de `procedure_fin_de_chantier` § 6 ne sont pas joués : ils sont de la phase 4.

---

# Contrôle 1 — adresses

## 1.1 Comment il a été joué

Un script, pas une lecture à l'œil. Trois passes :

1. **Extraction.** Toute citation de la forme « article X [du code Y] » relevée sur les 63 pièces, segment par segment — cartouche, dispositif, exposé, bloc interne, annexe. La grammaire de numéro reprend celle de LEGI en entier : `1636 B sexies`, `199 terdecies-0 AB`, `150 VC`, `302 bis MB`, `46 quater-0 YZD`, `1594-0 F sexies`. **3 534 citations brutes relevées.**
2. **Rattachement.** Le code d'une citation se tranche **par l'existence au dépôt de droit**, jamais par la seule proximité : un jeu de codes candidats est formé (code nommé à la proposition même, puis codes nommés à ±400 caractères, puis codes dominants de la pièce), et le candidat retenu est celui où l'adresse existe. Une version vivante l'emporte toujours sur une version abrogée. « Du même code » hérite du dernier code explicitement nommé.
3. **Verdict.** Chaque adresse retenue est passée à `droit.py article`. Versions applicables au millésime → `EXISTE` ou `EXISTE_FIN_PROGRAMMEE` ; versions seulement futures → `VIGUEUR_DIFF` ; versions seulement passées → `ABROGE` ; aucune version → `ABSENT`.

## 1.2 Le compte

| | |
|---|---|
| millésime | **LEGI 20261001**, 62 textes, fraîcheur 7 jours |
| citations brutes relevées | 3 534 |
| **occurrences contrôlées** | **2 844** |
| **adresses distinctes contrôlées** | **1 428** |
| occurrences laissées hors contrôle | 690 |

**Verdicts, en occurrences** : `EXISTE` 2 366 · `EXISTE_FIN_PROGRAMMEE` 275 · `VIGUEUR_DIFF` 167 · `EXISTE:VIGUEUR_DIFF` 3 · **`ABROGE` 10 + 1 (`EXISTE:ABROGE`)** · **`ABSENT` 22**.

**Verdicts, en adresses distinctes** : `EXISTE` 1 155 · `EXISTE_FIN_PROGRAMMEE` 140 · `VIGUEUR_DIFF` 111 · `EXISTE:VIGUEUR_DIFF` 3 · **`ABROGE` 10 + 1** · **`ABSENT` 8**.

## 1.3 Verdict sur la règle « rien d'`ABSENT` ni d'`ABROGE` ne sort »

### Les 11 occurrences `ABROGE` — **conforme**

**Aucune n'est au dispositif.** Dix sont au bloc interne de `clause_generale_niches_20261005.md` : ce sont les **constats propres de la pièce**, la table du § 9 qui dit pourquoi tel rang a été retiré (« retiré — article L. 312-73 abrogé »). Citer un article abrogé pour dire qu'on ne l'abroge pas est l'usage correct. La onzième est au cartouche de `P1/4_3_aide_fondamentale_et_taux_unique.md`, dans une note de mesure.

| adresse | pièce | segment |
|---|---|---|
| CGI, 199 vicies A | `P1/4_3_aide_fondamentale_et_taux_unique.md` | cartouche |
| CGI, 199 quater B · 244 quater M · 199 ter L · 220 N · 1414 | `clause_generale_niches_20261005.md` | interne |
| CIBS, L. 312-73 · L. 312-78 · L. 421-78-1 · L. 421-147 | `clause_generale_niches_20261005.md` | interne |
| code des douanes, 266 nonies | `clause_generale_niches_20261005.md` | interne |

### Les 8 adresses `ABSENT` — **7 déclarées, 1 non déclarée**

| adresse | pièces | segment | qualification |
|---|---|---|---|
| CGCT, **L. 1614-1-2** | `P1/4_2_refonte_taxes_C_dmto_franchise.md` · `P1/coll_P1_01_dotations_face_aux_reductions_de_champ.md` · `P1/coll_P1_03_tva_sur_justification.md` | cartouche, dispositif, interne | **création voulue**, portée par `coll_P1_01`, amendement A, III — déclarée nommément |
| CSS, **L. 177-3** | `SS/2_3_subventions_associations_social.md` | dispositif | **création voulue** par la pièce même — déclarée nommément |
| CSS, **L. 160-13-1** | `SS/n5_cadre_bouclier_sanitaire.md` | cartouche, dispositif | **création voulue** par la pièce même — déclarée nommément |
| CGI, **231 B** | `SS/nuit1c_suppression_taxe_salaires.md` | dispositif, interne | **création voulue** par la pièce même — déclarée nommément |
| CSS, « **L. 242-1 II** » | `clause_generale_niches_20261005.md` | interne | **artefact de lecture** : l'extracteur a agrégé le numéro et la division. L'article L. 242-1 `EXISTE` |
| CGI, « **article 1** » | `SS/n7b_ss03_liste_niches_sociales.md` | interne | **artefact de lecture** : il s'agit de « l'article 1er de la clause générale », non d'un article du CGI |
| CGI, **46 quater-0 YZD** | `clause_generale_niches_20261005.md` | interne | **article réglementaire, hors extrait LEGI** — la pièce le dit elle-même : « renvoi de doctrine sans siège légal » |
| **CGI, 721** | `P1/nuitp1_06_cession_reprise_entreprise.md` | cartouche | **le seul `ABSENT` non déclaré de la liasse.** Le cartouche cite « les articles 721 et 726 » ; 726 `EXISTE`, **721 n'existe à aucune version du millésime**. À reprendre — question Q5 |

**Verdict de la règle.** Aucune adresse `ABSENT` ni `ABROGE` ne sort **au dispositif**. Le seul point ouvert est au cartouche d'une pièce, non à son texte normatif.

## 1.4 Les 690 occurrences laissées hors contrôle, et la raison de chacune

| motif | occurrences | ce que c'est |
|---|---|---|
| **texte en discussion ou accroche** | 538 | « article 11 du texte déposé », « ARTICLE 58 », « ARTICLE ADDITIONNEL APRÈS L'ARTICLE 7 », rangs de la clause. Ces articles sont ceux du PLF 2027 et du PLFSS 2027 en discussion : ils ne sont pas au droit en vigueur et **ne peuvent pas y être cherchés**. Ils se contrôlent au socle du texte déposé, non à LEGI |
| **code non rattachable** | 119 | citation dont aucun candidat de code ne porte l'adresse, et qui ne nomme aucun code à la proposition même. Le fil **ne devine pas** : il déclare |
| **numéro abrégé** | 19 | « l'article 1er », « l'article 2 » employés seuls, sans code, pour désigner un article de la pièce elle-même |
| **renvoi interne au corpus** | 14 | renvoi à une division d'une autre pièce de la liasse, pas à un texte en vigueur |
| **total** | **690** | |

## 1.5 Verdicts pièce par pièce

Colonnes : occurrences contrôlées · `EXISTE` · fin programmée · `VIGUEUR_DIFF` · `ABROGE` · `ABSENT` · hors contrôle.

| pièce | occ | EX | FP | VD | AB | ABS | hors |
|---|---:|---:|---:|---:|---:|---:|---:|
| `P1/2_4_armateurs_tonnage.md` | 4 | 4 | 0 | 0 | 0 | 0 | 4 |
| `P1/2_4_credit_impot_famille.md` | 5 | 5 | 0 | 0 | 0 | 0 | 6 |
| `P1/2_4_credit_impot_recherche.md` | 6 | 6 | 0 | 0 | 0 | 0 | 10 |
| `P1/2_4_deductions_exceptionnelles.md` | 4 | 4 | 0 | 0 | 0 | 0 | 13 |
| `P1/2_4_exonerations_par_zone.md` | 18 | 16 | 2 | 0 | 0 | 0 | 13 |
| `P1/2_4_sortie_agricole_trois_ans.md` | 20 | 14 | 6 | 0 | 0 | 0 | 6 |
| `P1/2_4_tarifs_reduits_accise.md` | 13 | 6 | 7 | 0 | 0 | 0 | 3 |
| `P1/4_2_refonte_taxes_A_taxes_etat.md` | 90 | 73 | 16 | 1 | 0 | 0 | 25 |
| `P1/4_2_refonte_taxes_B_taxes_affectees.md` | 236 | 160 | 73 | 2 | 0 | 0 | 40 |
| `P1/4_2_refonte_taxes_C_dmto_franchise.md` | 143 | 135 | 5 | 0 | 0 | 3 | 12 |
| `P1/4_2_refonte_taxes_D_plus_values.md` | 97 | 96 | 1 | 0 | 0 | 0 | 18 |
| `P1/4_3_aide_fondamentale_et_taux_unique.md` | 56 | 53 | 2 | 0 | **1** | 0 | 13 |
| `P1/4_4_taxe_fonciere_unique.md` | 146 | 141 | 5 | 0 | 0 | 0 | 19 |
| `P1/4_5_solde_refonte_is_tf.md` | 72 | 69 | 0 | 3 | 0 | 0 | 12 |
| `P1/4_6_tva_taux_reduits.md` | 16 | 0 | 0 | 16 | 0 | 0 | 3 |
| `P1/4_7_abrogations_cgi.md` | 0 | 0 | 0 | 0 | 0 | 0 | 12 |
| `P1/coll_P1_01_dotations_face_aux_reductions_de_champ.md` | 70 | 67 | 0 | 1 | 0 | **2** | 27 |
| `P1/coll_P1_02_fusion_dotation_forfaitaire_taxe_fonciere.md` | 33 | 33 | 0 | 0 | 0 | 0 | 9 |
| `P1/coll_P1_03_tva_sur_justification.md` | 28 | 22 | 0 | 3 | 0 | **3** | 4 |
| `P1/n5_compte_epargne_personnel.md` | 60 | 60 | 0 | 0 | 0 | 0 | 3 |
| `P1/nuitp1_01_rendre_le_don.md` | 21 | 6 | 15 | 0 | 0 | 0 | 3 |
| `P1/nuitp1_04_pret_taux_zero.md` | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| `P1/nuitp1_05_investissement_industriel.md` | 2 | 2 | 0 | 0 | 0 | 0 | 3 |
| `P1/nuitp1_06_cession_reprise_entreprise.md` | 3 | 2 | 0 | 0 | 0 | **1** | 2 |
| `P1/nuitp1_07_credit_impot_competitivite.md` | 2 | 1 | 1 | 0 | 0 | 0 | 2 |
| `P1/nuitp1_08_avantages_culturels.md` | 7 | 7 | 0 | 0 | 0 | 0 | 2 |
| `P1/nuitp1_09_impot_agricole.md` | 5 | 5 | 0 | 0 | 0 | 0 | 2 |
| `P1/nuitp1_10_impot_selon_adresse.md` | 2 | 2 | 0 | 0 | 0 | 0 | 3 |
| `P1/nuitp1_11_abroger_mises_a_jour.md` | 13 | 13 | 0 | 0 | 0 | 0 | 4 |
| `P1/nuitp1_12_affectation_article_42.md` | 3 | 2 | 1 | 0 | 0 | 0 | 7 |
| `P2/2_1_dissolution_structures_facultatives.md` | 3 | 3 | 0 | 0 | 0 | 0 | 4 |
| `P2/2_1_etablissements_ressources_propres.md` | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| `P2/2_1_missions_rendues_aux_ministeres.md` | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| `P2/2_2_indemnite_depart_agents.md` | 3 | 3 | 0 | 0 | 0 | 0 | 7 |
| `P2/2_6_cheque_energie.md` | 3 | 3 | 0 | 0 | 0 | 0 | 11 |
| `P2/2_6_extinction_aide_logement.md` | 1 | 1 | 0 | 0 | 0 | 0 | 13 |
| `P2/2_6_socle_hebergement_urgence.md` | 7 | 7 | 0 | 0 | 0 | 0 | 5 |
| `P2/coll_P2_01_abrogation_concours_discretionnaires.md` | 27 | 26 | 0 | 1 | 0 | 0 | 7 |
| `P2/coll_P2_02_credits_etat_B.md` | 12 | 8 | 0 | 4 | 0 | 0 | 11 |
| `P2/coll_P2_03_suppression_articles_85_86_87.md` | 1 | 1 | 0 | 0 | 0 | 0 | 35 |
| `P2/coll_P2_04_facultes_et_obligations_de_baisse.md` | 59 | 56 | 0 | 3 | 0 | 0 | 13 |
| `P2/etatB_01_structures_facultatives.md` | 5 | 5 | 0 | 0 | 0 | 0 | 14 |
| `P2/etatB_02_subventions_associations.md` | 5 | 5 | 0 | 0 | 0 | 0 | 13 |
| `P2/etatB_03_aides_ciblees.md` | 5 | 5 | 0 | 0 | 0 | 0 | 20 |
| `P2/etatB_04_titre2_plafond_emplois.md` | 6 | 6 | 0 | 0 | 0 | 0 | 45 |
| `P2/n6_defaisance_participations.md` | 19 | 19 | 0 | 0 | 0 | 0 | 9 |
| `P2/n6_logement_social_flux.md` | 14 | 14 | 0 | 0 | 0 | 0 | 4 |
| `P2/n6_typologies_de_depenses.md` | 6 | 6 | 0 | 0 | 0 | 0 | 4 |
| `SS/2_3_subventions_associations_social.md` | 7 | 6 | 0 | 0 | 0 | **1** | 8 |
| `SS/3_3_restitution_salariale_coordination.md` | 11 | 11 | 0 | 0 | 0 | 0 | 9 |
| `SS/3_3_restitution_salariale_principale.md` | 64 | 64 | 0 | 0 | 0 | 0 | 16 |
| `SS/arrets_04_m024_prolongation_droits_soins.md` | 19 | 18 | 1 | 0 | 0 | 0 | 13 |
| `SS/n5_amorce_extinction_repartition.md` | 1 | 1 | 0 | 0 | 0 | 0 | 2 |
| `SS/n5_cadre_bouclier_sanitaire.md` | 48 | 45 | 0 | 0 | 0 | **3** | 7 |
| `SS/n5_extinction_aides_fondues.md` | 50 | 48 | 2 | 0 | 0 | 0 | 5 |
| `SS/n7b_m037a_gel_indexations_lfss.md` | 3 | 3 | 0 | 0 | 0 | 0 | 9 |
| `SS/n7b_ss03_liste_niches_sociales.md` | 48 | 37 | 7 | 0 | 0 | **4** | 39 |
| `SS/nuit1c_suppression_taxe_salaires.md` | 56 | 39 | 15 | 0 | 0 | **2** | 12 |
| `clause_generale_niches_20261005.md` | 1 069 | 816 | 106 | 132 | **9** | **3** | 41 |
| `sans_colonne/n7b_m022_certificats_energie.md` | 35 | 25 | 9 | 1 | 0 | 0 | 3 |
| `sans_colonne/n7b_m037b_gel_indexations_plf.md` | 7 | 7 | 0 | 0 | 0 | 0 | 6 |
| `sans_colonne/n7b_m070_depenses_nouvelles.md` | 5 | 5 | 0 | 0 | 0 | 0 | 3 |
| `sans_colonne/nuit1c_ppl_cession_participations.md` | 68 | 67 | 1 | 0 | 0 | 0 | 16 |
| **total** | **2 844** | **2 366** | **275** | **167** | **10** | **22** | **690** |

*Les 3 occurrences `EXISTE:VIGUEUR_DIFF` et la 1 occurrence `EXISTE:ABROGE` ne sont pas colonnées ci-dessus ; elles sont comptées au § 1.2.*

**Verdict d'ensemble du contrôle 1** : **joué, sur le millésime LEGI 20261001**. La liasse ne porte aucune adresse morte à son texte normatif. Un seul point à reprendre, au cartouche : CGI 721.

---

# Contrôle 2 — checklist rédactionnelle, ligne à ligne

Périmètre : **les 85 blocs de dispositif, et eux seuls**. Aucun exposé n'a été lu.
Source de la checklist : `methode/regles_redactionnelles.md`, intégralement, plus ses reprises du 20261007.
**Chaque ligne reçoit un verdict. Aucune ne reste sans verdict.** Un écart est rendu avec sa correction en clair ; **aucune correction n'est appliquée**.

## 2.1 Les lignes jouées mécaniquement

| # | ligne de la checklist | occ. relevées | lecture | verdict |
|---|---|---:|---|---|
| **R1** | Rédactions positives | 87 | Les 87 occurrences sont des **normes d'exclusion, de plafond ou de champ** — « ne sont pas dus », « aucune aide n'est due », « ne peut excéder », « le I ne s'applique pas ». Ce sont les formes légistiques propres de l'exclusion et du plafond, non les antithèses que la règle bannit. Une seule relève de la règle : `P1/4_3`, « l'aide fondamentale […] **ne constitue ni une réduction ni un crédit d'impôt** », qui est une qualification par la négative | **conforme, 1 écart** · correction proposée : « l'aide fondamentale est un élément du calcul de l'impôt. Elle s'impute avant toute réduction et tout crédit d'impôt. » |
| **R2** | Pas de virgule devant une conjonction de coordination · exception : clôture d'incise | 20 (13 pièces) | Lues une à une : **6 clôtures d'incise** (exception inscrite à la règle), **1 au texte cité** d'un intitulé de dépense fiscale (sans objet : on ne corrige pas un libellé cité), **13 écarts** — dont **7 devant « ni »**, 5 devant « ou », 1 devant « et » | **13 écarts** · correction proposée : retirer la virgule. Les 7 « ni…, ni… » sont une question, non une évidence — Q3 |
| **R3** | Pas de point-virgule au texte normatif · exception : énumérations légistiques 1° … ; 2° … | 8 (6 pièces) | **6 sont des énumérations légistiques** (exception inscrite) · **1 est un signe cité** (`P2/2_2`, « le point est remplacé par le signe : “ ; ” ») · **1 est une note de travail présente au dispositif** de l'article 3 de la clause générale | **conforme sur le fond, 1 écart de nature** — l'article 3 de la clause porte à son dispositif une phrase de travail (« Repris de la rédaction du 20261002 — pièce périmée et retirée… Rang P1-25 ; accroche à fixer »). Correction proposée : la phrase descend au bloc interne, le dispositif ne porte que la norme |
| **R4** | Apostrophes typographiques partout | **349** (29 pièces) | Mesure : 1 263 apostrophes typographiques contre **349 droites**. L'écart est réel et dispersé. Les pièces les plus touchées : `SS/3_3_restitution_salariale_principale.md` 42 · `P1/4_3_aide_fondamentale_et_taux_unique.md` 38 · `SS/n7b_ss03_liste_niches_sociales.md` 35 · `sans_colonne/n7b_m022_certificats_energie.md` 22 · `P2/2_2_indemnite_depart_agents.md` 20 | **349 écarts** · correction proposée : substitution `'` → `’` en une passe de typographie unique sur la liasse, **jamais pièce par pièce** (R-E : une pièce longue ne se réécrit pas pour une correction locale) — Q4 |
| **R5** | Guillemets français | 0 | Aucun guillemet droit relevé ; 423 guillemets français ouvrants | **conforme** |
| **R6** | Espaces insécables dans les guillemets français et devant la ponctuation haute, % et € | **1 244** (724 + 520) | Mesure : **54 espaces insécables** dans 176 241 octets, pour 423 guillemets ouvrants, 673 deux-points et 46 pour cent. La convention n'est **pas appliquée** au markdown source. La règle elle-même dit que ces règles « ne se vérifient que sur le rendu » | **écart systémique, 1 244 occurrences** · correction proposée : passe de typographie à l'export, pas à la source — Q4 |
| **R7** | « est ainsi rédigé » pour la réécriture d'un article de loi, jamais « est remplacé par les dispositions suivantes » | 0 | La formule réglementaire est **absente de la liasse entière** | **conforme** |
| **R8** | « Abroger » pour un texte et ses divisions numérotées · « supprimer » pour ce qui est à l'intérieur | 0 | Contrôle joué par extraction du **sujet grammatical** de chaque « est/sont supprimé(e)(s) » et « est/sont abrogé(e)(s) », après retrait du marqueur d'énumération de tête. 18 candidats bruts relevés, **tous écartés après lecture du sujet** : « le dernier alinéa de l'article 784 est supprimé » a pour sujet *alinéa*, non *article* | **conforme, 0 écart** — le partage est tenu sur les 85 dispositifs |
| **R9** | Aucune date au 31 décembre | **3** (2 pièces) | `P1/nuitp1_01_rendre_le_don.md` ×2 : « dans leur rédaction en vigueur **le 31 décembre 2027** » · `clause_generale_niches_20261005.md` ×1 : « exercices clos à compter du **31 décembre 2026** ». Les trois sont des dates de **référence de version** ou de **clôture d'exercice**, non des dates d'entrée en vigueur. Le registre des exceptions porte « 0 date au 31 décembre » | **3 écarts** · corrections proposées : « dans leur rédaction en vigueur le 31 décembre 2027 » → « dans leur rédaction applicable aux versements effectués avant le 1er janvier 2028 » (×2) ; « exercices clos à compter du 31 décembre 2026 » → « exercices clos à compter du 1er janvier 2027 » — à confirmer, la seconde est la formule usuelle du CGI |
| **R10** | Dates au 1er janvier ou 1er juillet, sauf exception inscrite au registre | **159** dont **45 hors des quatre dates communes** | Les quatre dates communes couvrent 114 occurrences : 1er janvier 2027 ×49 · 1er janvier 2028 ×36 · 1er juillet 2027 ×22 · 1er janvier 2029 ×7. Sur les 45 restantes, **29 sont des millésimes de textes cités** (« loi n° 2019-1479 du 28 décembre 2019 ») — sans objet, ce ne sont pas des dates d'effet. **16 sont des dates d'effet**, dont **3 inscrites au registre** (`P1/4_6_tva_taux_reduits.md`, 1er juillet 2028, 2029, 2030) | **13 écarts de tenue du registre**, détaillés au § 2.2 · correction proposée : ouvrir 13 lignes au registre, ou recaler sur une date commune — Q2 |
| **R11** | Pas de « doit » ni de futur de l'indicatif au texte normatif | 2 (1 pièce) | Les deux portent sur `P2/2_6_socle_hebergement_urgence.md`, qui remplace les mots cités « doit lui permettre » par « doit permettre à la personne accueillie ». Le « doit » est **repris du droit en vigueur**, non écrit par l'amendement. La règle des amendements minimaux (« préférer la suppression à la reformulation ; quand une phrase existante fonctionne, on la garde ») joue contre la correction | **1 écart, correction déconseillée** · le corriger obligerait à réécrire une phrase du CASF que l'amendement n'a pas de raison de toucher. Signalé, non corrigé |
| **R12** | Une phrase une norme | **31** (16 pièces) | Sur 31 phrases de plus de 65 mots : **6 sont des tableaux de crédits** lus comme une phrase par le compteur (`P2/coll_P2_02`, `P2/etatB_01` à `etatB_04`) — sans objet, un tableau n'est pas une phrase ; **10 sont des énumérations nominatives d'articles ou de lignes de tarif** — la forme fondue arrêtée au lot 19 fait de chaque rang une norme, l'énumération n'en est que le véhicule — sans objet ; **15 sont de vraies phrases normatives longues** | **15 écarts** · les plus lourdes : `P2/coll_P2_04` (D du I) · `P1/coll_P1_03` 118 et 135 mots · `P1/4_4` 139 mots · `clause`, B du IV 181 mots, C du IV 100 mots · correction proposée : scinder en phrases, une norme par phrase, sans changer le fond. **Application par copie d'octets, divisions rendues en clair** (R-E) |
| **R13** | Aucun chiffre inventé · les paramètres entre crochets sont des décisions politiques, jamais des chiffres inventés | 54 (9 pièces) | Les 54 chiffres au dispositif sont des taux et des montants **arrêtés par un lot ou repris du droit en vigueur**. Un seul paramètre reste ouvert, et il est **correctement marqué** : `sans_colonne/nuit1c_ppl_cession_participations.md`, « ne peut excéder **[un quart]** des participations ». Un écart typographique relevé au passage : `P1/4_2_refonte_taxes_D_plus_values.md` écrit « 7, 5 % » — espace parasite dans un taux cité | **conforme, 1 écart typographique** · correction proposée : « 7, 5 % » → « 7,5 % ». **Mais le taux est cité au texte en vigueur** : vérifier le verbatim du CGI avant de corriger |
| **R14** | Pas de redondance entre niveaux | — | Joué par lecture des 85 dispositifs : aucune disposition de la liasse ne recopie une norme portée par un niveau supérieur. La liasse est entièrement de niveau législatif ordinaire et organique financier ; la question du niveau constitutionnel ne s'y pose pas | **conforme** |
| **R15** | Cohérence de la hiérarchie des normes (Constitution / loi organique / loi ordinaire) | — | Une seule pièce est de niveau organique, `P1/nuitp1_12_affectation_article_42.md`, qui modifie un tableau de l'article 42 du texte déposé. Aucune disposition ne fait descendre dans un niveau ce qui relève d'un autre | **conforme** |

## 2.2 Les 13 dates d'effet hors des quatre communes et non inscrites au registre

| date | pièce | ce qu'elle porte |
|---|---|---|
| 1er juillet 2028 | `P2/2_6_extinction_aide_logement.md` | deuxième marche de la dégressivité de l'aide |
| 1er juillet 2029 | `P2/2_6_extinction_aide_logement.md` | extinction de l'aide |
| 1er janvier 2030 ×2 | `P2/2_6_extinction_aide_logement.md` | terme maximal des titres en cours · extinction définitive |
| 1er juillet 2029 | `P1/nuitp1_05_investissement_industriel.md` | achèvement des investissements agréés |
| 1er juillet 2029 | `P1/nuitp1_11_abroger_mises_a_jour.md` | achèvement des opérations engagées |
| 1er janvier 2030 | `P2/coll_P2_04_facultes_et_obligations_de_baisse.md` | abrogation des articles L. 1511-2 et L. 3232-1-2 du CGCT |
| 1er janvier 2030 | `SS/n5_extinction_aides_fondues.md` | abrogation de l'article L. 511-1 du CSS |
| 1er janvier 2030 | `SS/nuit1c_suppression_taxe_salaires.md` | entrée en vigueur des II et III |
| **30 juin 2029** | `SS/2_3_subventions_associations_social.md` | terme des conventions en cours. **Seule date de la liasse qui viole aussi la règle du jour** : ni 1er janvier, ni 1er juillet |
| 31 décembre 2027 ×2 | `P1/nuitp1_01_rendre_le_don.md` | voir R9 |
| 31 décembre 2026 | `clause_generale_niches_20261005.md` | voir R9 |

Le registre `livrables/registre_exceptions_dates.md` porte **7 exceptions** et impose, à son § 4, qu'une passe écrivant une date hors des quatre communes ouvre sa ligne **dans la même passe**. Treize dates sont écrites sans ligne. **Ce fil n'en ouvre aucune : il ne touche aucun registre.**

Correction proposée pour `SS/2_3` : « au plus tard jusqu'au 30 juin 2029 » → « au plus tard jusqu'au 1er juillet 2029 », qui respecte la règle du jour et n'ouvre qu'une exception de millésime.

## 2.3 Deux écarts de nature, relevés hors checklist

1. **`P2/coll_P2_04_facultes_et_obligations_de_baisse.md`, D du I** — le texte vise « l'article L. 1613-1 **du même code** » et « l'article L. 3334-1 **du même code** », alors que le dernier texte nommé avant ces renvois est **la loi n° 2022-1726 du 30 décembre 2022**, qui n'est pas un code. **Le « même code » n'a pas d'antécédent.** Les deux articles existent bien au CGCT. Correction proposée : nommer le code — « l'article L. 1613-1 du code général des collectivités territoriales », puis « l'article L. 3334-1 du même code ».
2. **L'article 3 de la clause générale ne porte aucun cartouche d'amendement** — ni « AMENDEMENT », ni « présenté par », ni accroche. La phase 2 avait déjà rendu cette correction en clair à son § 5.1 ; elle n'est pas appliquée. **Ce fil ne l'applique pas davantage** — Q6.

---

# Les deux constats légués

## Constat 1 — les deux pièces à rang actif portant « retirée du dépôt »

**Mesuré. Non tranché, comme le mandat le demande.**

**Deux pièces, et deux seulement.**

| pièce | rang à la table des colonnes | accroche |
|---|---|---|
| `livrables/depot_2027/P1/nuitp1_07_credit_impot_competitivite.md` | **P1-12**, colonne PLF 2027 première partie, recalculé le 20261008 — ancien rang P1-08 | `ARTICLE 11` |
| `livrables/depot_2027/P1/nuitp1_11_abroger_mises_a_jour.md` | **P1-29**, colonne PLF 2027 première partie, recalculé le 20261008 — ancien rang P1-20 | `ARTICLE 28` |

**Ce que la mention dit, au verbatim.** Les deux pièces portent, en tête de corps, immédiatement après le cartouche de versement :

> **RETIRÉE DU DÉPÔT — outre-mer hors périmètre (20261005)**
> Arbitrage de l'auteure du 20261005 : « oui on ne fait pas l'outre-mer pour le moment. »

Et chacune donne son motif propre :

- P1-12 : « La pièce supprime l'article 11 du texte déposé, qui proroge d'un an le crédit d'impôt pour la compétitivité et l'emploi applicable à **Mayotte** (code général des impôts, article 244 quater C, `ABROGE_DIFF` au droit en vigueur) : disposition propre à l'outre-mer. Copie du lot U6 ; l'original du coffre est inchangé. »
- P1-29 : « **Trois des quatre régimes abrogés sont ultramarins** (code général des impôts, articles 199 undecies C, 244 quater X et 244 quater Y, `EXISTE`). Le quatrième, l'article 39 decies C (investissement maritime, non ultramarin), reste porté par la clause générale des niches (article 2, 24°). Copie du lot U6 ; l'original du coffre est inchangé. »

**Ce que les cartouches de versement disent d'elles-mêmes.** Les deux cartouches, écrits à la phase 2 bis le 20261008, portent la même ligne :

> **Anomalie mesurée, portée à l'état de la passe et non tranchée ici** : le fichier d'origine porte en tête la mention « RETIRÉE DU DÉPÔT — outre-mer hors périmètre (20261005) », alors que la table du recalcul lui attribue un rang actif. La contradiction est rendue en clair et **le dispositif n'est pas touché**.

**La contradiction, posée.** Une pièce retirée du dépôt n'a pas de rang de dépôt ; une pièce à rang actif est au dépôt. Les deux énoncés ne peuvent pas tenir ensemble. Le retrait est du **20261005**, le rang du **20261008** : la mention est antérieure de trois jours au rang. Mais le motif du retrait — l'outre-mer hors périmètre — **n'est pas périmé par un recalcul de rangs**, et P1-29 dit elle-même qu'**un quart de son objet n'est pas ultramarin** et qu'il est déjà porté ailleurs, par la clause générale.

**Ce fil ne tranche pas.** Il n'applique ni la mention ni le rang. **Question Q1.**

## Constat 2 — l'accroche de l'abrogation des concours discrétionnaires

**Mesuré au socle du texte déposé. Tranché : l'article 83 est juste, l'article 58 ne l'est pas.**

Lecture de `/home/claude/droit/chantier/referentiels/socle_texte_plf2027.json` (véhicule `plf`, 90 articles, 8 annexes) :

| article du socle | partie et titre | intitulé | ce qu'il porte |
|---|---|---|---|
| **58** | seconde partie, titre premier — dispositions pour 2027 | **Crédits du budget général** | ouverture des AE et CP du budget général, 632 868 821 128 € et 615 139 875 333 €, par renvoi à **l'état B** |
| **83** | seconde partie, titre II — dispositions permanentes | **Répartition de la dotation globale de fonctionnement (DGF)** | modifications du titre III du livre III des deuxième et troisième parties du CGCT, 35 alinéas |

**Vérification de ce que la pièce supprime.** `P2/coll_P2_01_abrogation_concours_discretionnaires.md` écrit « ARTICLE 83 — I. Supprimer les alinéas 8 à 13 et 23. » Relevés au socle, ces alinéas sont :

| alinéa | texte au socle | article du CGCT visé | abrogé par la pièce ? |
|---:|---|---|---|
| 8 | « 5° A l'article L. 2334-40 : » | **L. 2334-40** — dotation politique de la ville | oui |
| 9 | « a) La dernière phrase du dernier alinéa du II est supprimée ; » | L. 2334-40 | oui |
| 10 | « b) La seconde phrase du premier alinéa du III est supprimée ; » | L. 2334-40 | oui |
| 11 | « 6° Au B de l'article L. 2334-42 : » | **L. 2334-42** — dotation de soutien à l'investissement local | oui |
| 12 | « a) Les mots : “, appréciée au 1er janvier…” sont supprimés ; » | L. 2334-42 | oui |
| 13 | « b) Il est complété par deux phrases ainsi rédigées : … » | L. 2334-42 | oui |
| 23 | « 3° Au dernier alinéa du 1° du I de l'article L. 3334-10, le mot : “départemental” est remplacé… » | **L. 3334-10** — dotation de soutien à l'investissement des départements | oui |

**Les sept alinéas visés portent exactement les trois dotations que la pièce abroge**, et aucune autre. Le cartouche de la pièce le dit déjà : « article 83 du texte déposé (répartition de la dotation globale de fonctionnement), **qui modifie déjà trois des articles abrogés** ».

**Verdict.** **L'accroche juste est l'article 83.** L'article 58 du texte déposé est l'article des crédits du budget général et de l'état B : c'est l'accroche de la **jambe de crédits** — `P2/coll_P2_02_credits_etat_B.md`, qui porte bien `ARTICLE 58 · ÉTAT B · Mission « Relations avec les collectivités territoriales »` — et non celle de la jambe normative. **La pièce a raison, le registre avant reprise avait tort.** Aucun registre n'est touché par ce fil : la correction est rendue, elle n'est pas appliquée.

---

# Mesure de sortie — le mandat, point par point

| point du mandat | verdict |
|---|---|
| Jouer le contrôle 1 sur toutes les pièces du paquet, dispositifs et blocs internes | **joué** — 63 pièces, 2 844 occurrences contrôlées, 1 428 adresses distinctes |
| Extraire mécaniquement, écrire un script, ne pas lire à l'œil | **joué** — extraction, rattachement et verdict par script ; aucune adresse relevée à la lecture |
| Rien d'`ABSENT` ni d'`ABROGE` ne sort | **joué** — 0 au dispositif ; 11 `ABROGE` et 7 `ABSENT` déclarés ; **1 `ABSENT` non déclaré, CGI 721, au cartouche de `P1/nuitp1_06`** |
| Une adresse `ABSENT` qui est une création voulue se déclare nommément | **joué** — 4 créations déclarées : CGCT L. 1614-1-2, CSS L. 177-3, CSS L. 160-13-1, CGI 231 B |
| Rendre le compte, les verdicts et le millésime, pièce par pièce et pour la liasse | **joué** — § 1.2 et § 1.5, **millésime LEGI 20261001** |
| Rendre le compte des références hors contrôle et la raison de chacune | **joué** — 690 occurrences, 4 motifs, § 1.4 |
| Jouer le contrôle 2 sur les dispositifs seulement, jamais les exposés | **joué** — 85 blocs isolés, 176 241 octets ; **aucun exposé lu** |
| Chaque ligne de la checklist reçoit un verdict, aucune ne reste sans verdict | **joué** — 15 lignes, 15 verdicts, § 2.1 |
| Un écart se signale avec sa correction proposée, en clair | **joué** — toutes les corrections sont au § 2.1 et § 2.2 |
| Aucune correction silencieuse, tu n'appliques rien | **joué** — **0 pièce corrigée** |
| Rédaction positive | **joué** — conforme, 1 écart |
| Pas de point-virgule au texte normatif | **joué** — conforme, 1 écart de nature |
| Une phrase une norme | **joué** — 15 écarts |
| Pas de redondance entre niveaux | **joué** — conforme |
| Aucun chiffre inventé | **joué** — conforme, 1 paramètre entre crochets correctement marqué |
| « est ainsi rédigé » pour la réécriture d'un article de loi | **joué** — conforme, 0 occurrence de la formule réglementaire |
| « abroger » / « supprimer » | **joué** — conforme, 0 écart sur 85 dispositifs |
| Aucune date au 31 décembre | **joué** — 3 écarts |
| Dates au 1er janvier ou 1er juillet, sauf exception inscrite au registre | **joué** — 13 dates d'effet non inscrites, dont 1 qui viole aussi la règle du jour |
| Typographie française, apostrophe typographique, espaces insécables | **joué** — 349 apostrophes droites, 1 244 espaces insécables manquantes |
| Constat légué 1 — deux pièces à rang actif portant « retirée du dépôt » | **mesuré et rendu, non tranché** — P1-12 et P1-29, verbatim et contradiction au § Constat 1, question Q1 |
| Constat légué 2 — article 83 ou article 58 | **tranché au socle** — **l'article 83 est juste** |
| Ne corriger aucune pièce | **tenu** |
| Ne toucher aucun exposé ni aucun registre | **tenu** |
| N'ouvrir aucune pièce nouvelle | **tenu** |
| Ne pas jouer le test de rattachement | **non joué** — il est de la phase 4 |
| Ne pas jouer la contestabilité | **non joué** — elle est de la phase 4 |

---

# Questions fermées pour le LISEZ-MOI

**Q1 — `P1/nuitp1_07_credit_impot_competitivite.md` (P1-12, `ARTICLE 11`) et `P1/nuitp1_11_abroger_mises_a_jour.md` (P1-29, `ARTICLE 28`) portent à la fois un rang actif du 20261008 et la mention « RETIRÉE DU DÉPÔT — outre-mer hors périmètre (20261005) ». Lequel vaut : le rang, ou la mention ?** Si c'est le rang, les deux mentions tombent et les deux pièces entrent à la liasse. Si c'est la mention, les deux rangs se libèrent et la colonne P1 passe de 33 à 31 rangs actifs. *Point à peser : P1-29 dit elle-même qu'un de ses quatre régimes n'est pas ultramarin, et qu'il est déjà porté par la clause générale (article 2, 24°).*

**Q2 — Treize dates d'effet de la liasse ne sont ni l'une des quatre dates communes ni inscrites au registre des exceptions. S'inscrivent-elles au registre, ou se recalent-elles sur une date commune ?** Défaut proposé : les inscrire, sauf `SS/2_3_subventions_associations_social.md` dont le **30 juin 2029** viole aussi la règle du jour et se recale au 1er juillet 2029.

**Q3 — Les sept virgules devant « ni » (« ni A, ni B ») se retirent-elles, ou l'usage est-il admis à la liasse ?** La règle les interdit ; l'usage est uniforme sur six pièces. Défaut proposé : les retirer, la règle ne porte pas d'exception pour « ni ».

**Q4 — La passe de typographie (349 apostrophes droites, 1 244 espaces insécables manquantes) se joue-t-elle sur la source markdown ou seulement à l'export ?** La règle dit que ces points « ne se vérifient que sur le rendu ». Défaut proposé : à l'export, en une passe unique sur la liasse, jamais pièce par pièce.

**Q5 — Le cartouche de `P1/nuitp1_06_cession_reprise_entreprise.md` cite « les articles 721 et 726 » du code général des impôts. L'article 726 existe ; l'article 721 n'existe à aucune version du millésime 20261001. Est-ce une coquille, ou une adresse à retirer ?**

**Q6 — L'article 3 de la clause générale ne porte aucun cartouche d'amendement, et son dispositif porte encore une phrase de travail (« Rang P1-25 ; accroche à fixer »). Quel fil écrit le cartouche et descend la phrase au bloc interne ?** La correction est rendue en clair depuis la phase 2, § 5.1, et n'est toujours pas appliquée.

**Q7 — `P2/coll_P2_04_facultes_et_obligations_de_baisse.md`, D du I, vise « l'article L. 1613-1 du même code » et « l'article L. 3334-1 du même code » alors que le dernier texte nommé est la loi n° 2022-1726. Le code se nomme-t-il, ou la phrase se réordonne-t-elle ?** Défaut proposé : nommer le code général des collectivités territoriales au premier renvoi, « du même code » au second.
