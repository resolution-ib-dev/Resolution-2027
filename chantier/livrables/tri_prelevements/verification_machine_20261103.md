# Vérification de fond et de rédaction des amendements du tri — fil machine du 20261103

*Mandat : `methode/prompt_fil_machine_tri_porte.md`. Pièces : P1 n° 35 à 38, PLFSS n° 9, **en projet, non déposables en l’état**. Source unique : `appareil/tri_porte/amendements.py` ; fiches et liasses régénérées par `verser_amendements.py` après remise des liasses à leur état antérieur au lot VI (identité à l’octet avec `cc320728~1`, mesurée). Droit : dépôt LEGI 20261031, **version applicable au 1er juillet 2027**. Mesure de fond : `appareil/tri_porte/verifier_fond.py` → `verif_fond.json` ; renvois entrants : `verification_machine_20261103_renvois.tsv`.*

*Provenance de chaque ligne : **relevé** (rejoué sur pièce dans ce fil), **hérité** (repris d’un autre fil sans rejeu), **déduit** (conclusion de ce fil à partir de relevés).*

---

## 0. Ce qui a changé au dispositif

| pièce | correction | motif | provenance |
|---|---|---|---|
| P1 n° 35 | cartouche : rang N9 ajouté ; exposé : la contribution maritime est nommée | l’article 15 du PLF porte aussi, en son II, le rétablissement pour un exercice de la contribution maritime (art. 50 de la loi n° 2025-127) : « Supprimer cet article » la fait tomber | relevé (socle, art. 15, al. 21 à 30) |
| P1 n° 36, II, 2° | L. 421-149, -150 et L. 421-152 à -155 retirés de la fourchette | double emploi : abrogés par le P1 n° 1, III, 341° et 342° | relevé (`extraire_visas.py`) |
| P1 n° 36, III, B | « Au premier alinéa de l’article L. 518-16 » → « À l’article L. 518-16 » | l’article n’a qu’un alinéa | relevé |
| P1 n° 36, IV | II, 2° recalé au 1er juillet 2027, taxes de 2027 dues sur la seule durée d’affectation ou de détention antérieure | consigne du 20261103 ; fait générateur des fréquences à l’achèvement de l’année (L. 455-48) | relevé |
| P1 n° 36, VI ; n° 37, IV ; n° 38, IV | gage maintenu : majoration du taux de l’IS (DGF en plus pour les collectivités au n° 37) | registre des sources de gage, § V : variable de solde du circuit B ; ce fil l’avait d’abord remplacé par la formule tabac, revenu sur cette erreur | relevé |
| P1 n° 37, I, 1° | 1609 H ajouté (taxe spéciale d’équipement du Grand Projet du Sud-Ouest, sœur de 1609 I) ; 1635 quater O retiré | rang 370 « taxes spéciales d’équipement » ; 1635 quater O abrogé par le P1 n° 1, III quinquies | relevé ; ajout de 1609 H **déduit** |
| P1 n° 37, I, 2° | L. 2333-55-3 retiré ; L. 5211-21-1 ajouté | L. 2333-55-3 abrogé par le P1 n° 1, III, 345° ; L. 5211-21-1 ouvre aux intercommunalités le même prélèvement sur les jeux « dans les conditions de L. 2333-54 » | relevé ; ajout **déduit** |
| P1 n° 37, II, B | remontées mécaniques, sites nordiques et assainissement collectif recalés au 1er juillet 2027 | consigne du 20261103 ; perçus par recette, accès ou raccordement | relevé |
| P1 n° 38, I, 3° et 4° | L. 5141-8 abrogé en entier (et non son seul I) ; L. 253-8-2 en entier (et non son seul VI) | le II de L. 5141-8 porte la taxe annuelle du rang 390 ; le VI de L. 253-8-2 n’est que l’affectation — l’abroger seul laissait la taxe | relevé |
| P1 n° 38, I, 5° | L. 4316-10 à L. 4316-12 ajoutés | contrôle, assiette et sanction des seules redevances du 1° | relevé ; ajout **déduit** |
| P1 n° 38, II, B | rédigé nommément : contribution de L. 351-12 CGFP, taxe annuelle du II de L. 5141-8 CSP, taxe de L. 253-8-2 CRPM | faits générateurs relevés : effectif au 31 décembre de l’année écoulée (R. 351-3), autorisations valides au 1er janvier | relevé |
| PLFSS n° 9, II, B | rédigé nommément, trois régimes : C3S due pour 2027 (fait générateur au 1er janvier, L. 137-32) ; contributions à seuil annuel dues pour 2027 (L. 138-10, L. 138-19-8, L. 380-2) ; contributions assises sur l’année dues pour 2027 sur la moitié de l’assiette (L. 137-27, L. 138-1, L. 245-1, L. 245-5-1 A, L. 245-5-1, L. 245-6, L. 862-4-1) | consigne du 20261103 ; prorata temporis, principe du II, 2° du n° 36 | relevé (faits générateurs) ; prorata validé (§ 10) |
| PLFSS n° 9, III et IV | clause réglementaire ajoutée ; gage « accise sur les tabacs » remplacé par la forme de la liasse de financement (contributions de L. 136-6 et L. 136-7, PLFSS n° 3, V) | frontière de véhicule : l’IS ne gage pas une pièce de financement | relevé |
| les cinq | exposés : en-têtes ramenés à 10–15 mots, virgules devant « et » retirées, totaux recomptés et arrondis (8,9 ; 2,9 ; 2,1 ; 19 milliards) | `41_SCRIPT_controles_expose.py` ; règle d’arrondi du 20261019 | relevé (recompte sur `sort_prelevements_20261103.tsv`) |
| cartouches | rangs `n-321`, `n-316`, `n-325` → N8, N6, N7 | trois libellés fantômes : aucun rang de ce nom au tri | relevé |

---

## 1. P1 n° 35 — article 15

| division | question de fond | verdict | pièce qui le prouve | provenance |
|---|---|---|---|---|
| « Supprimer cet article » | ce que l’article porte | I : 3e exercice de la contribution des grandes entreprises (art. 48) ; **II : la contribution maritime rétablie pour un exercice (art. 50)**. Les deux tombent | `socle_texte_plf2027.json`, art. 15 | relevé |
| idem | rien d’autre du texte déposé sans base ? | les deux I et II ne modifient que la loi n° 2025-127 ; aucun autre article du PLF ne renvoie à l’art. 15 | socle, art. 15 ; `articles_ouverts_plf2027.tsv` | relevé |
| devenir | rang 144 : remplacé par l’IS | conforme ; N9 porté (devenir remplacé par l’IS) | tri, rangs 144 et N9 | relevé |
| exposé | 7,5 / 7 / 5,2 Md€ ; 15,7 % | concordent | `annexe_recettes_bg_2027.tsv`, ligne 1441 ; art. 15, al. 11 | relevé |
| gage | aucun | 69 PASSE | `69_CONTROLE_doctrine.py` | relevé |

## 2. P1 n° 36 — impositions d’État et Caisse des dépôts

| division | question de fond | verdict | pièce qui le prouve | provenance |
|---|---|---|---|---|
| I, 1° | les 31 articles existent au 1er juillet 2027 | oui, sections entièrement visées | `verif_fond.json` | relevé |
| I, 1° (jeux) | affectations hors CGI | 1609 tricies affecté à l’ANS par L. 112-11-1, 2° C. sport : atteint par la clause V | code du sport, L. 112-11-1 | relevé |
| I, 1° (jeux) | le rang 280 (3 241 M€) est-il porté ? | **non en totalité** : 1609 novovicies est un prélèvement de 5,1 % au profit de l’ANS ; le rendement du rang renvoie au prélèvement de l’article 138 de la loi n° 2019-486, **texte hors dépôt** | 1609 novovicies ; tri, rang 280 | relevé ; siège principal **déduit** |
| I, 1° (boissons) | version applicable de 1613 quater | deux versions du 1er janvier 2027 au dépôt (`MORT_NE` et `VIGUEUR_DIFF`) ; l’abrogation de l’article entier vaut pour les deux | dépôt de droit | relevé |
| I, 2° | le 5° ter de 1001 existe sous cette désignation | oui ; réapplication conforme | `43_SCRIPT_diff_cible.py` | relevé |
| I, 2° | le PLF modifie-t-il 1001 ? | oui, art. 14 (OUVERT) : coordination en navette, dite à l’exposé | `44_SCRIPT_article_ouvert.py` | relevé |
| II, 1° | date | dues au titre de 2028 : fait générateur au 1er janvier, motif tenu | 231 ter, 990 E | hérité (calendrier du 20261103), rejoué |
| II, 2° | périmètre de L. 421-93 s. | 76 articles, tous des taxes sur l’affectation des véhicules ; six déjà au n° 1, retirés | `verif_fond.json` | relevé |
| II, 2° | le PLF modifie-t-il ces articles ? | oui : L. 421-95 et L. 421-99-3 (art. 25), L. 421-132-5 (art. 28) — navette, dite à l’exposé | 44 | relevé |
| III, A | la Caisse est-elle exonérée ailleurs ? | aucune mention aux articles 206 à 208 ; seul L. 518-16 CMF parle d’un substitut à l’IS ; réapplication conforme ; le 1 bis de 206, abrogé par le n° 1, 155°, n’interfère pas | CGI et CMF, recherche intégrale | relevé |
| III, B | cohérence du versement à l’État | « après paiement de l’impôt sur les sociétés » : cohérent ; désignation d’alinéa corrigée | 43 | relevé |
| V | renvois entrants | 116 hors visa : 5 affectations (clause V), 24 réglementaires (clause), 14 lois de finances passées (sans objet), 73 renvois morts à toiletter | `…_renvois.tsv` | relevé ; verdicts **déduits** par règle |
| VI | gage | majoration de l’IS, circuit B ; **perte des affectataires tiers non couverte par la forme** (ANS, CNAM pour les droits de 1635 bis AE, opérateurs des redevances sanitaires), déclarée | registre des sources de gage, § I et V | relevé |

## 3. P1 n° 37 — impositions locales

| division | question de fond | verdict | pièce qui le prouve | provenance |
|---|---|---|---|---|
| I, 1° | sections laissées en partie | 1599 quater E (taxe d’aménagement d’Île-de-France) : déjà abrogé par le n° 1, III quinquies ; 1609 H : ajouté | `verif_fond.json` | relevé |
| I, 1° et 3° (TA) | cohérence avec le n° 29 | 1635 quater A abrogé par le n° 29 pour les impositions « établies au titre de 2028 » ; le n° 37 vise les autorisations dont le fait générateur est postérieur au 1er janvier 2028 : même date, deux formules — à aligner au n° 29 (hors mandat) | n° 29, III et V | relevé |
| I, 3° | L. 331-1 à 17 C. urb. retire-t-il autre chose que la taxe ? | non : cinq articles subsistent (L. 331-1 à 4, L. 331-17), tous de la taxe d’aménagement ; bornes présentes | `verif_fond.json` | relevé |
| I, 2° (casinos) | la part de l’État a-t-elle un autre siège ? | non : c’est le prélèvement progressif de L. 2333-56, dans la fourchette (état A, ligne 1786 : 1,0 Md€ en 2027) | `annexe_recettes_bg_2027.tsv` | relevé |
| I, 2° (casinos) | autres effets | L. 2333-55-1 et -55-2 fixent aussi l’assiette et la liquidation des prélèvements des organismes sociaux ; la contribution de L. 136-7-1, III CSS demeure : signal | CSS, L. 136-7-1 | relevé ; effet **déduit** |
| I, 4° (TLPE) | délibérations communales | atteintes par II, C, seconde phrase | dispositif | relevé |
| I, 6° (TASCOM) | texte | loi n° 72-657, **hors dépôt** : non réapplicable | `codes.json` | relevé |
| II | dates | voir § 7 | — | — |
| III | renvois | 146 hors visa : 27 réglementaires (clause), 48 lois passées (sans objet), 66 renvois morts ; L. 2336-2 sans objet (abrogé par le n° 29) ; L. 2334-4 (potentiel fiscal) de fond, à toiletter ; L. 5211-21-1 tranché par abrogation | `…_renvois.tsv` | relevé ; verdicts déduits |
| IV | gage | DGF (forme du n° 25, V) et majoration de l’IS ; **perte des établissements publics affectataires non couverte par la forme** (établissements publics fonciers, chambres consulaires, Société des grands projets, Grand Projet du Sud-Ouest), déclarée | registre des sources de gage | relevé |

## 4. P1 n° 38 — taxes affectées hors CGI

| division | imposition | qui perd | dissous par le P2 n° 25 ? | qui la porte désormais | provenance |
|---|---|---|---|---|---|
| I, 1° | cotisation AGS (L. 3253-18) | AGS | non | crédits du budget, la dépense passe au vote (§ 10) ; l’obligation d’assurance de L. 3253-6 demeure | relevé |
| I, 2° | contribution FIPHFP (L. 351-12 à 15) | FIPHFP | oui (III, 334°) | fermeture au P2 n° 25 ; l’obligation d’emploi de L. 351-1 demeure sans sa contribution (§ 10) | relevé |
| I, 3° | contribution URPS (L. 4031-4) | URPS ; fonds de L. 221-1-2 CSS | non | crédits du budget, au vote (§ 10) | relevé |
| I, 3° | taxes vétérinaires (L. 5141-8, I et II) | ANSES | non | crédits, à inscrire | relevé |
| I, 4° | taxe phytopharmaceutique (L. 253-8-2) | ANSES ; fonds d’indemnisation des victimes de pesticides (L. 723-13-3) | non | crédits du budget pour le fonds, au vote (§ 10) | relevé |
| I, 5° | redevance hydraulique (L. 4316-1, 1°) | VNF | oui (III, 63°) | ministère, au II, A du n° 25 | relevé |
| I, 6° | droit d’examen du permis de chasser | OFB | non | crédits (0,7 M€) | relevé |
| I, 7° à 9° | défrichement, mines, conserves, IRSN, phyto mise sur le marché | — | — | **textes hors dépôt** : non réappliqués, fait générateur non relevé | relevé |
| II, B | annuelles | nommées, faits générateurs relevés | — | — | relevé |
| III | renvois | 46 hors visa : 27 réglementaires, 6 lois passées, 10 renvois morts ; 3 de fond (L. 3253-14 C. trav., L. 221-1-2 CSS, L. 723-13-3 CRPM) | `…_renvois.tsv` | — | relevé ; verdicts déduits |
| IV | gage | majoration de l’IS, circuit B ; **pertes des tiers non couvertes par la forme**, déclarées | registre des sources de gage | — | relevé |

## 5. PLFSS n° 9 — contributions sociales

| division | question de fond | verdict | pièce qui le prouve | provenance |
|---|---|---|---|---|
| I, 1° | fourchettes et ordre du code | L. 245-5-1 A précède L. 245-5-1 (section 1 contre section 2) : « L. 245-1 à L. 245-5, L. 245-5-1 A, L. 245-5-1 à L. 245-5-6 » est juste | ordre des sections, `verifier_fond.py` | relevé |
| I, 1° (L. 137-13) | double emploi | le PLFSS n° 1, III, 8° abroge le 4e alinéa du I du même article : **le n° 1, 8° devient sans objet**, à retirer à la prochaine passe du n° 1 | `extraire_visas.py` | relevé |
| I, 1° | affectations | L. 131-8, 5°, 5° bis et 8° : atteints par III ; aucun recouvrement avec le n° 2 (L. 131-8, 3°) | CSS, L. 131-8 | relevé |
| I, 1° (L. 862-3, -4) | complémentaire santé solidaire | perte de la CNAM au titre du fonds de L. 862-1 ; mission maintenue | L. 131-8, 8° | relevé |
| I, 1° (L. 652-6) | régime des avocats | perte de la CNBF ; régime maintenu | — | déduit |
| I, 2° (CTA) | domaine de la LFSS | finance un régime obligatoire de base (CNIEG) : LO 111-3-7, 1° et 2° — plaidable ; texte **hors dépôt** | LO 111-3-7 | relevé ; texte hérité |
| III | renvois | 158 hors visa : 4 affectations (clause), 74 réglementaires (clause), 18 lois passées (sans objet), 62 renvois morts | `…_renvois.tsv` | relevé ; verdicts déduits |
| IV | gage | contributions de L. 136-6 et L. 136-7, forme du PLFSS n° 3, V | registre des sources de gage, § V bis ; liasse PLFSS | relevé |

---

## 6. Recevabilité financière

**Le circuit B commande la forme** (registre des sources de gage, § V) : majoration de l’IS pour l’État, DGF pour les collectivités, contributions de L. 136-6 et L. 136-7 en loi de financement. **La forme ne couvre pas la perte d’un affectataire qui n’est ni l’État, ni une collectivité, ni la sécurité sociale** (opérateurs, associations, établissements) : le risque au titre de l’article 40 est déclaré dans le bloc interne de chaque pièce. *Relevé.*

## 7. Dates

| division | avant | après | motif | provenance |
|---|---|---|---|---|
| P1 n° 36, II, 1° | dues au titre de 2028 | inchangé | fait générateur au 1er janvier | relevé |
| P1 n° 36, II, 2° | dues au titre de 2028 | 1er juillet 2027 ; 2027 dû sur la durée antérieure | consigne du 20261103 | relevé |
| P1 n° 37, remontées et sites nordiques | dues au titre de 2028 | recettes et accès à compter du 1er juillet 2027 | perçus par passage ou accès | relevé |
| P1 n° 37, assainissement collectif | raccordements à compter du 1er janvier 2028 | raccordements à compter du 1er juillet 2027 | exigible au raccordement (L. 1331-7), aucun lien avec la taxe foncière | relevé |
| P1 n° 37, taxe d’aménagement | autorisations à compter du 1er janvier 2028 | inchangé | alignement sur le n° 29 | relevé |
| P1 n° 37, taxes annuelles | dues au titre de 2028 | inchangé | taxe foncière unique en 2028 ; fait générateur au 1er janvier | hérité, rejoué |
| P1 n° 38, II, B | « les impositions annuelles » | trois impositions nommées, dues une dernière fois pour 2027 | faits générateurs antérieurs au 1er juillet 2027 | relevé |
| PLFSS n° 9, II, B | « contributions annuelles », 2027 entier | C3S et contributions à seuil : 2027 entier ; contributions assises sur l’année : moitié de l’assiette 2027 | fait générateur ou seuil annuel relevé, article par article | relevé ; prorata proposé |

**Aucune date hors des quatre dates communes** : aucune ligne au registre des exceptions. Aucun 31 décembre. *Relevé.*

## 8. Coordinations nommées au mandat

| coordination | mesure | suite |
|---|---|---|
| PLFSS n° 1, III, 8° et n° 9, I, 1° (L. 137-13) | double emploi confirmé | n° 9 prévaut ; 8° du n° 1 à retirer (hors mandat) |
| n° 22 et 25 (exposés) contre n° 21 (dispositif) | écart confirmé ; calendrier TVA arrêté le 20261005 (n° 21 : 2028, 2029, 2030) | **corrigé** : aux exposés des n° 22 et 25, le 1er juillet 2027 est la date du taux unique de l’IS (pièces A et B et liasse) |
| n° 25, II, B (ANCOLS) | L. 313-1 CCH abrogé, le 1° de L. 342-21 réécrit, montant nul à défaut d’arrêté | **tient** : « supprimé par construction » (auteur, 20261103) |
| n° 20 et pièce D | le § « Coordination due, non rédigée » le dit toujours (prélèvement de solidarité, 1600-00 C et 1600-0 C à J) | aucune |
| 231 B CGI (PLFSS n° 3, II) | article **créé par le I du même amendement**, d’où son absence du dépôt : visa juste | aucune |
| L. 421-78-1 CIBS (P1 n° 1) | une seule version au dépôt, `MODIFIE_MORT_NE` : jamais en vigueur | visa à retirer du n° 1 (hors mandat) |

## 9. Contrôles

| contrôle | résultat | provenance |
|---|---|---|
| machine `61` (installation) | 34 passés, 0 échec, 4 non joués attendus | relevé |
| `41` exposés | 200–300 mots, en-tête, virgules, phrase de sens : 5 sur 5 ; **plafond des chiffres de preuve (≤ 2) : 0 sur 5** — signal, porté par 25 exposés sur 38 de la liasse P1, la réduction touche la voix | relevé |
| `42` sortie | 0 échec ; « réalistes » (5,2 ; 7,5 ; 15,7 ; 2,9 ; 2,1) : coïncidences de reconstruction, chiffres relevés sur pièce | relevé |
| `43` réapplication | 1001, 206, L. 518-16, L. 423-6, L. 4316-1 : CONFORME | relevé |
| `64` droit | 8 passés, 0 échec | relevé |
| `69` doctrine | n° 35 : PASSE ; n° 36 à 38 et PLFSS n° 9 : échec **connu** — le contrôle, écrit pour la machine des tiers, ne connaît pas le circuit B arbitré | relevé |
| `controle_sieges_prelevements.py` sur `sort_prelevements_20261103.tsv` | 0 échec, 10 signaux | relevé |
| `make index` | 0 anomalie bloquante | relevé |
| `controle_lexique.py` | L1 « prélèvements obligatoires » : l’accroche commune seule | relevé |
| docx des deux liasses (`liasse2docx.js`), contrôlés sur PDF | P1 : 114 pages ; PLFSS : 24 pages ; 0 séparateur de milliers double ; n° 35 à 38 et 9 présents | relevé |

**Limite déclarée du relevé des renvois** : un « du même code » sans code nommé dans l’article citant n’est pas résolu (cas de L. 112-11-1 C. sport, ajouté à la main) ; les fourchettes citées ne sont comptées que par leurs bornes. *Relevé.*

**Limite du dépôt de droit** : code forestier, code minier, lois n° 72-657, 2003-1312, 2004-803, 2006-1666, 2010-1658 et 2019-486 absents. Leur ajout à `codes.json` déclenche le rafraîchissement du dépôt, **qui ne se pousse pas d’un fil Cowork** (A-393) : à faire par le fil qui verse. *Relevé.*

---

## 10. Questions — closes sur les réponses déjà rendues

| question | réponse relevée | source |
|---|---|---|
| article 15 entier ? | oui : la contribution maritime tombe aussi | « pas de prélèvement nouveau » ; extinction de la contribution exceptionnelle avec les niches (20261103) |
| moitié d’assiette 2027 ? | oui | consigne du calendrier du 20261103 |
| missions privées de ressource ? | la dépense passe au vote : crédits du budget général, ou fermeture au P2 n° 25 | exposé du n° 38 ; devenir « fondu dans l’équilibre » du tri |
| dates de la TVA ? | n° 21 : 1er juillet 2028, 2029, 2030 | calendrier arrêté le 20261005 ; exposés des n° 22 et 25 corrigés |
| ANCOLS ? | tient par construction | réponse du 20261103 |

## 11. Compteurs au calendrier

Portés au registre de calcul, `livrables/registre_calcul_etatB.md`, § 18 : perte brute en mesure, **−17 Md€ en 2027** (dont 5,2 du n° 35 et 2,0 par mois de juillet à décembre), **−33 Md€ en régime plein**, avant la contrepartie du circuit B. *Relevé sur le tri ; minorant, 27 rangs non chiffrés.*
