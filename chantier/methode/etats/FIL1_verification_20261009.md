# Fil 1 — vérification de la liasse de première partie, temps 1 — 20261009

**Porteur** : fil 1 de la liasse de première partie, Cowork, 20261009.
**Mandat** : `methode/procedure_liasse_P1_20261009.md`, § 1 et § 8, fil 1 — jouer les quatre
contrôles sur les 31 rangs, **n'en corriger aucun**, rendre quatre listes d'écarts et la colonne
d'export du registre.
**Domicile** : `methode/etats/FIL1_verification_20261009.md`.
**Appui** : `methode/procedure_liasse_P1_20261009.md`, § 1 et § 8 ·
`methode/etats/SUIVI_chantier_20261009.md` · `methode/etats/FIL0_regroupement_20261009.md` (R-G) ·
`methode/appui_des_passes.md`, R-G, R-H, R-I · `methode/etats/NUIT_3B_controles_1_2_20261008.md` ·
`livrables/registre_colonnes_depot_2027.md`, § I · `reference/cgi_expert_regles_de_lecture.md` ·
`methode/regles_redactionnelles.md` · skills `resolution-chantier`, `confrontation` ·
dépôt de droit `Resolution-2027` cloné, millésime LEGI **20261007**, `droit.py etat` joué ·
socle `referentiels/socle_texte_plf2027.json`, 90 articles, 8 annexes.
**Appareil versé** : `appareil/fil1_verification/` — `liasse.py`, `c1_conformite.py`,
`c2_cgi_expert.py`, `c3_adresses.py`, `c4_recevabilite.py`, `fautes_fil1.py`, `fil1.py`.

---

## 0. Mesure d'entrée — l'objet, mesuré avant contrôle (R-H)

| objet | mesure |
|---|---|
| rangs actifs de la colonne | **31**, pris au registre des colonnes, § I |
| amendements portés | **33** — P1-30 et P1-32 en portent deux chacun |
| fichiers | **30** ; la clause porte P1-31 (article 1er) et P1-04 (article 3) |
| rangs vacants barrés, hors périmètre | **6** — P1-02, P1-03, P1-12, P1-22, P1-24, P1-29 |
| octets de dispositif contrôlés | **121434** |
| millésime du droit | **LEGI 20261007** — les 2 844 occurrences du 20261008 l'avaient été sur 20261001 |

**Neuf pièces du périmètre étaient en retard au dépôt** et ont été reprises au coffre avant
contrôle : la clause, les quatre pièces 4.2, la pièce 4.3, la pièce 4.6, `n7b_m022` et le registre
des sources de gage. Le fil 0 les a écrites au coffre le 20261009 ; le dépôt porte encore l'état
d'avant. **Les contrôles sont joués sur l'état du coffre.**

**Deux des quatre contrôles n'existaient pas** — reprise du CGI expert, recevabilité au socle. Ils
sont écrits ici, chacun avec son jeu de fautes, et versés avec lui.

---

## 1. Les quatre contrôles, et ce qu'ils mordent

**Le jeu de fautes est la preuve des contrôles, non leur accessoire.** Seize fautes injectées —
quatre par contrôle : une valeur fausse au même repère, un repère qui ne résout pas, un repère
retiré, et **le verdict retourné**, un écart réel couvert par une déclaration de conformité.
**Les seize mordent.** `python3 appareil/fil1_verification/fautes_fil1.py` les rejoue.

| contrôle | état avant ce fil | ce qu'il passe |
|---|---|---|
| **A — conformité au corpus** | se rejouait | les 15 lignes de la checklist, sur les dispositifs |
| **B — reprise du CGI expert** | **à écrire** | section due, siège repris, ligne résolue, écart déclaré, ligne cohérente |
| **C — exactitude des références** | se rejouait | toute adresse au droit, millésime 20261007 |
| **D — recevabilité** | **à écrire** | accroches et citations du texte déposé n° 3210, au socle |

---

## Liste 1 — conformité au corpus · **22 écarts**, 8 qualifiés sans objet

Périmètre : les 33 dispositifs, et eux seuls. Aucun exposé, aucun cartouche, aucun bloc
interne. Chaque ligne reçoit un verdict ; aucune ne reste sans verdict.

| ligne | ce qu'elle passe | écarts |
|---|---|---:|
| **R1** | rédactions positives | 1 |
| **R2** | pas de virgule devant une conjonction | 3 |
| **R3** | pas de point-virgule au texte normatif | 1 |
| **R4** | apostrophes typographiques | **0** |
| **R5** | guillemets français | **0** |
| **R6** | espaces insécables | **0** |
| **R7** | « est ainsi rédigé » pour une réécriture | **0** |
| **R8** | abroger un texte, supprimer ce qui est dedans | **0** |
| **R9** | aucune date au 31 décembre | **0** |
| **R10** | dates au 1er janvier ou 1er juillet | 2 |
| **R11** | pas de « doit » ni de futur | **0** |
| **R12** | une phrase une norme | 14 |
| **R13** | aucun chiffre inventé | 1 |
| **R14** | pas de redondance entre niveaux | **0** |
| **R15** | cohérence de la hiérarchie des normes | **0** |

| rang | ligne | ce qui est constaté | correction proposée |
|---|---|---|---|
| P1-01 | R1 | rédaction positive — « “L’aide fondamentale est un élément du calcul de l’impôt et ne constitue ni une réduction ni un crédit d’impôt.”  « VI. – A. – Le 1°, l » | énoncer ce que la règle fait |
| P1-01 | R12 *(énumération, sans objet)* | phrase de 71 mots — « – La perte de recettes résultant pour l’État du V est compensée à due concurrence par les abrogations, prévues par la présente loi, de l’article 157 b » | sans objet — énumération nominative, véhicule d’une norme par rang |
| P1-06 | R12 *(énumération, sans objet)* | phrase de 69 mots — « 9° Les articles 689, 733, 742, 1584, 1584 bis, 1584 ter, 1594-0 F sexies, 1594-0 G, 1594 A, 1594 B, 1594 D, 1594 E, 1594 F ter, 1594 F quinquies, 1594 » | sans objet — énumération nominative, véhicule d’une norme par rang |
| P1-07 | R2 | virgule devant conjonction — « entionnée au I auprès d’un établissement ou d’un organisme établi en France, autre qu’un compte de dépôt à vue, et notamment :  1° Les plans d’épargne » | retirer la virgule, ou la retenir si elle clôt une incise |
| P1-09 | R13 | espace parasite dans un taux — « 7, 5 % » | retirer l’espace — contrôler le verbatim avant de corriger |
| P1-10 | R10 | date hors des quatre dates communes — « loi, demeure applicable aux investissements agréés avant cette date et réalisés avant le 1er juillet 2029. »  IV. – Compléter cet article par un III a » | inscrire au registre des exceptions, ou recaler sur une date commune |
| P1-28 | R12 | phrase de 83 mots — « Le produit de référence est la somme du produit de la taxe foncière sur les propriétés bâties et des impositions supprimées par le III du présent arti » | scinder, une norme par phrase |
| P1-30 | R12 | phrase de 95 mots — « Ce rapport présente, pour le dernier exercice clos, l’exercice en cours et l’exercice à venir, le produit des impositions supprimées, le produit suppl » | scinder, une norme par phrase |
| P1-31 | R12 | phrase de 67 mots — « ** – Les impositions mentionnées au A sont l’impôt sur le revenu, l’impôt sur les sociétés, l’impôt sur la fortune immobilière, les droits d’enregistr » | scinder, une norme par phrase |
| P1-31 | R12 | phrase de 84 mots — « > > 6° Qui sont instituées par la présente loi pour le compte d’épargne personnel, au nombre desquelles le régime d’imposition de ses retraits et le s » | scinder, une norme par phrase |
| P1-31 | R12 | phrase de 78 mots — « > 208° Le XXXV de la section II du chapitre IV du titre premier de la première partie du livre premier, les articles 199 ter I et 220 K, le k du 1 de  » | scinder, une norme par phrase |
| P1-31 | R12 | phrase de 106 mots — « 213-167, la ligne « Biens mentionnés à la ligne précédente, en Corse » qui suit la ligne « Produits agricoles et produits assimilés normalement destin » | scinder, une norme par phrase |
| P1-31 | R12 | phrase de 87 mots — « 213-230, la ligne « 140 premières représentations théâtrales, d’un concert ou d’un spectacle de cirque » et les deux lignes qui la suivent, les lignes » | scinder, une norme par phrase |
| P1-31 | R12 | phrase de 76 mots — « 213-259, les lignes « Hébergement à usage touristique », « Hébergement à usage de résidence », « Mise à disposition de terrains de camping ou caravana » | scinder, une norme par phrase |
| P1-31 | R12 | phrase de 89 mots — « 231-68, les lignes « Logements locatifs sociaux financés par un prêt locatif aidé d’intégration ainsi que les travaux d’extension ou de remise à neuf  » | scinder, une norme par phrase |
| P1-31 | R12 | phrase de 78 mots — « ** – Sous réserve des B à F, le I s’applique à l’impôt sur le revenu dû au titre de 2026, à l’impôt sur les sociétés dû au titre des exercices clos à  » | scinder, une norme par phrase |
| P1-31 | R12 *(énumération, sans objet)* | phrase de 676 mots — « ** – Sont également abrogés les 1°, 3°, 4°, 5°, 6°, 9°, 10°, 13°, 15°, 16° et 17° du 5 du VII de la 1re sous-section de la section II du chapitre prem » | sans objet — énumération nominative, véhicule d’une norme par rang |
| P1-31 | R12 *(énumération, sans objet)* | phrase de 771 mots — « ** – Sont également abrogés, à compter du 1er janvier 2028, le 6 bis du IV de la 1re sous-section de la section II du chapitre premier du titre premie » | sans objet — énumération nominative, véhicule d’une norme par rang |
| P1-31 | R12 *(énumération, sans objet)* | phrase de 181 mots — « ** – Sous réserve des C à F, pour les dispositions dont le bénéfice est subordonné à un investissement, une dépense, une souscription, un versement, u » | sans objet — énumération nominative, véhicule d’une norme par rang |
| P1-31 | R12 *(énumération, sans objet)* | phrase de 100 mots — « ** – Par dérogation aux A et B, pour les dispositions relatives à la décote, au nombre de parts et au quotient familial, aux revenus que remplace l’ai » | sans objet — énumération nominative, véhicule d’une norme par rang |
| P1-31 | R12 *(énumération, sans objet)* | phrase de 71 mots — « ** – Par dérogation aux A et B et sous réserve du F, pour les dispositions relatives aux droits de mutation à titre gratuit et au prélèvement prévu à  » | sans objet — énumération nominative, véhicule d’une norme par rang |
| P1-31 | R12 *(énumération, sans objet)* | phrase de 87 mots — « ** – Par dérogation aux A, B et D, pour les dispositions relatives aux activités agricoles, aux services à la personne et à la garde des jeunes enfant » | sans objet — énumération nominative, véhicule d’une norme par rang |
| P1-31 | R2 | virgule devant conjonction — « es lignes « Location-accession », « Accession à la propriété sous condition de prix maximum et de localisation, et travaux associés », « Accession pro » | retirer la virgule, ou la retenir si elle clôt une incise |
| P1-31 | R3 | point-virgule au texte normatif — « ajoutée (reprise du 20261005)  Les autres paragraphes de l’exposé sommaire de l’article 1er restent à écrire ; le paragraphe ci-dessous y prend place  » | scinder en deux phrases |
| P1-33 | R10 | date hors des quatre dates communes — « code.  C. – Les articles L. 1511-2 et L. 3232-1-2 du même code sont abrogés à compter du 1er janvier 2030.  D. – La réduction prévue au I est opérée,  » | inscrire au registre des exceptions, ou recaler sur une date commune |
| P1-33 | R12 | phrase de 95 mots — « 3° Sur les fractions du produit net de la taxe sur la valeur ajoutée affectées à la collectivité en application de l’article 149 de la loi n° 2016-191 » | scinder, une norme par phrase |
| P1-33 | R2 | virgule devant conjonction — « ne région accorde sur le fondement de l’article L. 1511-2 du même code ne peut excéder les deux tiers, en 2028, et le tiers, en 2029, de la moyenne de » | retirer la virgule, ou la retenir si elle clôt une incise |
| P1-35 | R12 | phrase de 118 mots — « – À compter de 2027, le montant des fractions du produit net de la taxe sur la valeur ajoutée affectées à une collectivité territoriale ou à un groupe » | scinder, une norme par phrase |
| P1-35 | R12 | phrase de 135 mots — « – À compter de 2028, le montant des fractions affectées à un département, à une région ou à une collectivité exerçant leurs compétences en application » | scinder, une norme par phrase |
| P1-36 | R12 | phrase de 69 mots — « – Au tableau du I, à la colonne F :  1° Aux lignes 2, 8, 13, 38, 51, 52, 57, 58, 59, 60, 61, 62, 63, 64, 65, 68, 70, 73, 74, 76, 77, 78, 79, 96, 97, 9 » | scinder, une norme par phrase |

---

## Liste 2 — reprise du CGI expert · **45 écarts**, 1 signalement

La règle de fond est acquise et ne se rouvre pas : *le corpus prime sur la rédaction de l'expert,
et l'écart se déclare en exposé sommaire.* Le contrôle ne juge pas qui a raison.

**Exemption nommée et motivée, versée avec le contrôle** : l'abrogation sèche d'un article que
l'expert déclare `supprimé` est la reprise même de l'expert — le § 3 des règles de lecture pose
que la colonne C est vide et que la disposition est « L'article N est abrogé. » La clause générale
abroge 396 rangs à ce titre.

| test | ce qu'il dit | écarts |
|---|---|---:|
| **B1** | la pièce touche un siège du CGI et ne porte pas la section de reprise | 23 |
| **B2** | un siège du CGI touché au dispositif que la section ne cite pas | 16 |
| **B3** | la section cite une ligne hors de sa table | 0 |
| **B4** | la pièce s'écarte de l'expert sans le déclarer à l'exposé | 6 |
| **B6** | la ligne citée et l'article nommé à côté d'elle divergent | 0 |
| *B5* | *article à contrôler avant emploi — signalement, non écart* | *1* |

| rang | test | ce qui est constaté |
|---|---|---|
| P1-01 | B1 | section « ce que la pièce reprend de l’expert » absente — 9 siège(s) du CGI au dispositif, dont 8 portés par les tables ; 6 hors abrogation sèche : 157 bis, 193, 195, 196 A bis, 200 quater B, 81 |
| P1-05 | B1 | section « ce que la pièce reprend de l’expert » absente — 3 siège(s) du CGI au dispositif, dont 3 portés par les tables ; 3 hors abrogation sèche : 200, 238 bis, 978 |
| P1-06 | B1 | section « ce que la pièce reprend de l’expert » absente — 32 siège(s) du CGI au dispositif, dont 32 portés par les tables ; 30 hors abrogation sèche : 1584, 1584 bis, 1584 ter, 1594 A, 1594 B, 1594 D, 1594 E, 1594 F quinquies, 1594 F septies, 1594 F sexies,  |
| P1-07 | B1 | section « ce que la pièce reprend de l’expert » absente — 3 siège(s) du CGI au dispositif, dont 3 portés par les tables ; 3 hors abrogation sèche : 150 UB, 163 quinquies D, 4 B |
| P1-08 | B1 | section absente — exemption retenue — 1 siège(s) portés par les tables, tous abrogés en bloc *(exemption : abrogation sèche d’un article que l’expert déclare supprimé)* |
| P1-10 | B1 | section absente — exemption retenue — 1 siège(s) portés par les tables, tous abrogés en bloc *(exemption : abrogation sèche d’un article que l’expert déclare supprimé)* |
| P1-13 | B1 | section « ce que la pièce reprend de l’expert » absente — 3 siège(s) du CGI au dispositif, dont 3 portés par les tables ; 3 hors abrogation sèche : 220 octies, 220 quindecies, 220 septdecies |
| P1-14 | B1 | section absente — exemption retenue — 1 siège(s) portés par les tables, tous abrogés en bloc *(exemption : abrogation sèche d’un article que l’expert déclare supprimé)* |
| P1-15 | B1 | section « ce que la pièce reprend de l’expert » absente — 7 siège(s) du CGI au dispositif, dont 6 portés par les tables ; 6 hors abrogation sèche : 199 ter B, 199 ter B bis, 220 B, 220 B bis, 244 quater B, 244 quater B bis |
| P1-16 | B1 | section « ce que la pièce reprend de l’expert » absente — 10 siège(s) du CGI au dispositif, dont 10 portés par les tables ; 10 hors abrogation sèche : 44 duodecies, 44 octies A, 44 quindecies, 44 quindecies A, 44 septdecies, 44 sexdecies, 44 sexies, 44 sexie |
| P1-17 | B1 | section absente — exemption retenue — 1 siège(s) portés par les tables, tous abrogés en bloc *(exemption : abrogation sèche d’un article que l’expert déclare supprimé)* |
| P1-18 | B1 | section « ce que la pièce reprend de l’expert » absente — 4 siège(s) du CGI au dispositif, dont 3 portés par les tables ; 3 hors abrogation sèche : 199 ter E, 220 G, 244 quater F |
| P1-19 | B1 | section « ce que la pièce reprend de l’expert » absente — 8 siège(s) du CGI au dispositif, dont 8 portés par les tables ; 8 hors abrogation sèche : 39 decies, 39 decies A, 39 decies B, 39 decies C, 39 decies D, 39 decies E, 39 decies F, 39 decies G |
| P1-21 | B1 | section « ce que la pièce reprend de l’expert » absente — 5 siège(s) du CGI au dispositif, dont 4 portés par les tables ; 4 hors abrogation sèche : 199 ter K, 207, 220 M, 244 quater L |
| P1-25 | B1 | section « ce que la pièce reprend de l’expert » absente — 29 siège(s) du CGI au dispositif, dont 16 portés par les tables ; 16 hors abrogation sèche : 219, 224, 234 duodecies, 234 nonies, 234 quaterdecies, 234 quindecies, 234 terdecies, 235 ter C, 235 ter X, |
| P1-26 | B1 | section « ce que la pièce reprend de l’expert » absente — 3 siège(s) du CGI au dispositif, dont 3 portés par les tables ; 2 hors abrogation sèche : 207, 219 |
| P1-27 | B1 | section « ce que la pièce reprend de l’expert » absente — 1 siège(s) du CGI au dispositif, dont 1 portés par les tables ; 1 hors abrogation sèche : 44 septdecies |
| P1-28 | B1 | section « ce que la pièce reprend de l’expert » absente — 20 siège(s) du CGI au dispositif, dont 20 portés par les tables ; 20 hors abrogation sèche : 1379, 1380, 1381, 1388, 1393, 1406 bis, 1407, 1447, 1520, 1529, 1530, 1530 bis… |
| P1-30 | B1 | section « ce que la pièce reprend de l’expert » absente — 4 siège(s) du CGI au dispositif, dont 3 portés par les tables ; 3 hors abrogation sèche : 1668, 212 bis, 219 |
| P1-31 | B1 | section « ce que la pièce reprend de l’expert » absente — 415 siège(s) du CGI au dispositif, dont 410 portés par les tables ; 410 hors abrogation sèche : 100 bis, 1020, 1028 bis, 1028 ter, 1042, 1042 A, 1042 B, 1049, 1050, 1051, 1054, 1055 bis… |
| P1-32 | B1 | section « ce que la pièce reprend de l’expert » absente — 1 siège(s) du CGI au dispositif, dont 1 portés par les tables ; 1 hors abrogation sèche : 1648 A |
| P1-34 | B1 | section « ce que la pièce reprend de l’expert » absente — 4 siège(s) du CGI au dispositif, dont 4 portés par les tables ; 4 hors abrogation sèche : 1380, 1636 B septies, 1636 B sexies, 1639 A |
| P1-37 | B1 | section « ce que la pièce reprend de l’expert » absente — 19 siège(s) du CGI au dispositif, dont 19 portés par les tables ; 19 hors abrogation sèche : 1379, 1519, 1519 HB, 1582, 1587, 1589, 1590, 1599 quater A, 1599 quater B, 1599 quinquies B, 1600, 1609 sex |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 150 U |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 150 UA |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 150 VI |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 150 VJ |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 150 VK |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 150 VL |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 1609 nonies G |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 200 B |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 200 C |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 219 |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 239 nonies |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 244 bis A |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 244 bis B |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 683 |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 719 |
| P1-09 | B2 | siège du CGI touché au dispositif et non repris à la section — 777 |
| P1-09 | B4 | écart à la rédaction de l’expert non déclaré à l’exposé sommaire — 150 VH bis (expert : allégé ; la pièce l’abroge) |
| P1-09 | B4 | écart à la rédaction de l’expert non déclaré à l’exposé sommaire — 150 VI (expert : supprimé ; la pièce ne l’abroge pas en bloc) |
| P1-09 | B4 | écart à la rédaction de l’expert non déclaré à l’exposé sommaire — 150 VJ (expert : supprimé ; la pièce ne l’abroge pas en bloc) |
| P1-09 | B4 | écart à la rédaction de l’expert non déclaré à l’exposé sommaire — 150 VK (expert : supprimé ; la pièce ne l’abroge pas en bloc) |
| P1-09 | B4 | écart à la rédaction de l’expert non déclaré à l’exposé sommaire — 150 VL (expert : supprimé ; la pièce ne l’abroge pas en bloc) |
| P1-09 | B4 | écart à la rédaction de l’expert non déclaré à l’exposé sommaire — 719 (expert : supprimé ; la pièce ne l’abroge pas en bloc) |
| P1-09 | B5 | article porté par `cgi_expert_articles_bouges.tsv` — la rédaction de l’expert part d’un état qui n’est plus le droit — 150 VH bis : version changée *(exemption : signalement, non écart)* |

---

## Liste 3 — exactitude des références, millésime LEGI 20261007 · **14 écarts**

| | |
|---|---|
| millésime | **LEGI 20261007** ; la passe du 20261008 avait joué sur **20261001** |
| occurrences contrôlées | **1816** |
| adresses distinctes | **1017** |
| occurrences laissées hors contrôle | **379** |

**Verdicts, en occurrences** : `EXISTE` 1546 · `EXISTE_FIN_PROGRAMMEE` 191 · `VIGUEUR_DIFF` 65 · `ABSENT` 14

**Les occurrences laissées hors contrôle, et la raison de chacune** — un contrôle qui ne rend que
ses absences est incomplet (reprise 1 du 20261007).

| motif | occurrences |
|---|---:|
| numéro abrégé, article de la pièce | 174 |
| code non rattachable | 119 |
| texte en discussion ou accroche | 78 |
| texte hors extrait du dépôt de droit | 8 |
| **total** | **379** |

| rang | segment | adresse | verdict | qualification |
|---|---|---|---|---|
| P1-06 | cartouche | code général des collectivités territoriales, art. L. 1614-1-2 | `ABSENT` | création voulue, portée par `coll_P1_01`, amendement A, III — déclarée |
| P1-06 | dispositif | code général des collectivités territoriales, art. L. 1614-1-2 | `ABSENT` | création voulue, portée par `coll_P1_01`, amendement A, III — déclarée |
| P1-11 | cartouche | code général des impôts, art. 721 | `ABSENT` | la pièce déclare elle-même que l’article n’existe pas au millésime — Q5 du 20261008, à reprendre |
| P1-30 | cartouche | code général des impôts, art. 179 | `ABSENT` | artefact de lecture — « l’article 179 de la loi n° 2019-1479 », au cartouche et à un tableau du bloc interne ; la loi porte bien l’article |
| P1-30 | interne | code général des impôts, art. 179 | `ABSENT` | artefact de lecture — « l’article 179 de la loi n° 2019-1479 », au cartouche et à un tableau du bloc interne ; la loi porte bien l’article |
| P1-30 | interne | code général des impôts, art. 21 | `ABSENT` | artefact de lecture — renvoi à un considérant de décision, non à un article de code |
| P1-30 | interne | code général des impôts, art. 72-2 | `ABSENT` | artefact de lecture — article 72-2 de la Constitution, texte hors extrait LEGI |
| P1-31 | expose | code des impositions sur les biens et services, art. 1 | `ABSENT` | artefact de lecture — « les références de l’article 1er au code des impositions… », l’article 1er étant celui de la clause |
| P1-32 | cartouche | code général des collectivités territoriales, art. L. 1614-1-2 | `ABSENT` | création voulue, portée par la pièce même — déclarée |
| P1-32 | cartouche | loi n° 2009-1673 du 30 décembre 2009, art. L. 1614-1-2 | `ABSENT` | création voulue, portée par la pièce même — déclarée |
| P1-35 | dispositif | code général des collectivités territoriales, art. L. 1614-1-2 | `ABSENT` | création voulue, portée par `coll_P1_01` — déclarée |
| P1-37 | interne | loi n° 2025-127 du 14 février 2025, art. L. 116-1 | `ABSENT` | artefact de lecture — table du bloc interne, le code visé n’est pas celui que la ligne nomme en tête |
| P1-37 | interne | code du travail, art. LO 111-3-14 | `ABSENT` | artefact de lecture — article du code de la sécurité sociale cité dans une table du bloc interne |
| P1-37 | interne | code du travail, art. LO 111-3-16 | `ABSENT` | artefact de lecture — article du code de la sécurité sociale cité dans une table du bloc interne |

**14 verdicts négatifs, dont 6 portent sur la pièce** : 8 sont des artefacts de lecture, tous hors dispositif, chacun nommé ci-dessus. **Aucune adresse morte au dispositif**, hors les créations voulues et déclarées.

**Verdicts par rang.**

| rang | occ. | EXISTE | fin programmée | VIGUEUR_DIFF | ABSENT | désignation fausse | hors contrôle |
|---|---:|---:|---:|---:|---:|---:|---:|
| P1-01 | 54 | 52 | 2 | 0 | 0 | 0 | 11 |
| P1-04 | 4 | 4 | 0 | 0 | 0 | 0 | 1 |
| P1-05 | 21 | 6 | 15 | 0 | 0 | 0 | 1 |
| P1-06 | 130 | 123 | 5 | 0 | 2 | 0 | 11 |
| P1-07 | 57 | 57 | 0 | 0 | 0 | 0 | 5 |
| P1-08 | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| P1-09 | 93 | 93 | 0 | 0 | 0 | 0 | 13 |
| P1-10 | 3 | 3 | 0 | 0 | 0 | 0 | 2 |
| P1-11 | 2 | 1 | 0 | 0 | 1 | 0 | 3 |
| P1-13 | 6 | 6 | 0 | 0 | 0 | 0 | 3 |
| P1-14 | 4 | 4 | 0 | 0 | 0 | 0 | 3 |
| P1-15 | 11 | 11 | 0 | 0 | 0 | 0 | 3 |
| P1-16 | 27 | 25 | 2 | 0 | 0 | 0 | 2 |
| P1-17 | 5 | 5 | 0 | 0 | 0 | 0 | 2 |
| P1-18 | 8 | 8 | 0 | 0 | 0 | 0 | 1 |
| P1-19 | 12 | 12 | 0 | 0 | 0 | 0 | 2 |
| P1-20 | 10 | 5 | 5 | 0 | 0 | 0 | 2 |
| P1-21 | 19 | 15 | 4 | 0 | 0 | 0 | 3 |
| P1-23 | 13 | 0 | 0 | 13 | 0 | 0 | 3 |
| P1-25 | 100 | 79 | 20 | 1 | 0 | 0 | 15 |
| P1-26 | 26 | 17 | 9 | 0 | 0 | 0 | 11 |
| P1-27 | 2 | 2 | 0 | 0 | 0 | 0 | 3 |
| P1-28 | 153 | 148 | 5 | 0 | 0 | 0 | 12 |
| P1-30 | 74 | 70 | 0 | 0 | 4 | 0 | 9 |
| P1-31 | 607 | 511 | 44 | 51 | 1 | 0 | 100 |
| P1-32 | 56 | 54 | 0 | 0 | 2 | 0 | 43 |
| P1-33 | 31 | 31 | 0 | 0 | 0 | 0 | 38 |
| P1-34 | 37 | 37 | 0 | 0 | 0 | 0 | 5 |
| P1-35 | 8 | 7 | 0 | 0 | 1 | 0 | 23 |
| P1-36 | 0 | 0 | 0 | 0 | 0 | 0 | 11 |
| P1-37 | 241 | 158 | 80 | 0 | 3 | 0 | 36 |

---

## Liste 4 — recevabilité, contre le socle du texte déposé n° 3210 · **1 écarts**

Le rattachement est joué et ne se refait pas. Ce contrôle passe les **accroches** et les
**citations du texte en discussion** contre le socle — 90 articles, 8 annexes.
**92 citations du texte en discussion contrôlées au socle**, qu'aucune passe n'avait
jamais passées : le contrôle d'adresses les met hors contrôle à bon droit, elles ne sont pas au
droit en vigueur.

| test | ce qu'il dit | écarts |
|---|---|---:|
| **D1** | l'article d'accroche n'est pas au socle | 0 |
| **D2** | une pièce de première partie s'accroche à un article de la seconde | 0 |
| **D3** | une citation du texte en discussion ne résout pas au socle | 0 |
| **D4** | la pièce écrit une accroche autre que celle du registre | 1 |

| rang | test | ce qui est constaté |
|---|---|---|
| P1-04 | D4 | le dispositif n’écrit aucune accroche — registre : additionnel 2 |

---

## Colonne d'export du registre — les 31 rangs, quatre verdicts

**Pleine sur les 31 rangs.** 2 rangs sortent conformes aux quatre contrôles.

| rang | A · corpus | B · CGI expert | C · références | D · recevabilité |
|---|---|---|---|---|
| **P1-01** | 1 écart | 1 écart | conforme | conforme |
| **P1-04** | conforme | conforme | conforme | 1 écart |
| **P1-05** | conforme | 1 écart | conforme | conforme |
| **P1-06** | conforme | 1 écart | 2 écarts | conforme |
| **P1-07** | 1 écart | 1 écart | conforme | conforme |
| **P1-08** | conforme | 1 écart | conforme | conforme |
| **P1-09** | 1 écart | 22 écarts | conforme | conforme |
| **P1-10** | 1 écart | 1 écart | conforme | conforme |
| **P1-11** | conforme | conforme | 1 écart | conforme |
| **P1-13** | conforme | 1 écart | conforme | conforme |
| **P1-14** | conforme | 1 écart | conforme | conforme |
| **P1-15** | conforme | 1 écart | conforme | conforme |
| **P1-16** | conforme | 1 écart | conforme | conforme |
| **P1-17** | conforme | 1 écart | conforme | conforme |
| **P1-18** | conforme | 1 écart | conforme | conforme |
| **P1-19** | conforme | 1 écart | conforme | conforme |
| **P1-20** | conforme | conforme | conforme | conforme |
| **P1-21** | conforme | 1 écart | conforme | conforme |
| **P1-23** | conforme | conforme | conforme | conforme |
| **P1-25** | conforme | 1 écart | conforme | conforme |
| **P1-26** | conforme | 1 écart | conforme | conforme |
| **P1-27** | conforme | 1 écart | conforme | conforme |
| **P1-28** | 1 écart | 1 écart | conforme | conforme |
| **P1-30** | 1 écart | 1 écart | 4 écarts | conforme |
| **P1-31** | 10 écarts | 1 écart | 1 écart | conforme |
| **P1-32** | conforme | 1 écart | 2 écarts | conforme |
| **P1-33** | 3 écarts | conforme | conforme | conforme |
| **P1-34** | conforme | 1 écart | conforme | conforme |
| **P1-35** | 2 écarts | conforme | 1 écart | conforme |
| **P1-36** | 1 écart | conforme | conforme | conforme |
| **P1-37** | conforme | 1 écart | 3 écarts | conforme |

---

## Mesure de sortie — le mandat, point par point

| point du mandat | verdict |
|---|---|
| jouer les quatre contrôles sur les 31 rangs | **joué** — 33 amendements, 30 fichiers |
| rejouer le contrôle d'adresses au millésime LEGI 20261007 | **joué** — 1816 occurrences |
| écrire le contrôle de reprise du CGI expert | **joué** — cinq tests, un signalement |
| écrire le contrôle de recevabilité au socle | **joué** — 92 citations passées au socle |
| chaque contrôle naît avec son jeu de fautes | **joué** — 16 fautes, **16 mordent** |
| n'en corriger aucun | **tenu** — 0 pièce touchée, 0 registre touché |
| rendre quatre listes d'écarts | **joué** — 22 · 45 · 14 · 1 |
| rendre la colonne d'export sur ses quatre verdicts | **joué** — pleine sur les 31 rangs |
| ne pas élargir le périmètre | **tenu** — les 6 rangs vacants barrés ne sont pas contrôlés |

**Ce qui relève du jugement et n'entre dans aucun compte** : la hiérarchie des signalés, le partage
entre une phrase longue à scinder et une énumération qui est son propre véhicule, et l'arbitrage de
chaque divergence avec la rédaction de l'expert. Ils se posent au temps 2.
