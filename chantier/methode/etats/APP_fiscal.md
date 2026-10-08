# État APP_fiscal — application du lot 19 et de l’observation 2.1 à la matière fiscale

**Porteur** : fil Cowork d’application, dépôt 2027, matière fiscale — refonte et abrogations du code général des impôts, 20261007, seconde passe (la première s’était arrêtée sur une mesure vide).

**Mandat** : périmètre recalé par le fil de tête après mesure — le regroupement des abrogations par bloc sort du mandat, instrument insuffisant ; le reste de l’observation 2.1 de `methode/reprise_20261007.md` et les arbitrages du lot 19 (`methode/etats/L15_L17_L19.md`) sont jouables et joués. Ordre dû : dispositif, entrée en vigueur, gage, bloc interne. L’exposé ne bouge pas. Aucune pièce nouvelle.

**Domicile** : `methode/etats/APP_fiscal.md`.

**Appui** : `methode/appui_des_passes.md` · `methode/COMMUN.md` · `methode/regles_redactionnelles.md`, section du 20261007 · `reference/guide_legistique.md`, parties I à V · `methode/etats/L15_L17_L19.md` · `methode/etats/U7.md` · `methode/reprise_20261007.md` · `methode/etats/APP_fiscal.md`, état du fil arrêté. Dépôt de droit cloné à `/home/claude/droit/`, millésime LEGI **20261001**, `droit.py etat` joué.

**Mesure** : 9 pièces au mandat, 9 lues · **5 pièces écrites**, 4 vérifiées et non touchées · 412 rangs en entrée au III de la clause, **396 en sortie** (18 supprimés, 2 ajoutés) · **366 articles fondus**, 1 pièce périmée · **25 renvois entrants vérifiés un par un**, 5 appliqués, 20 rendus en clair · **12 adresses contrôlées au dépôt**, 0 `ABSENT` non attendu · 3 questions fermées.

---

## 1. Mesure de sortie — point par point, verdict par point

| n° | point du mandat | verdict |
|---|---|---|
| 0 | **Regroupement des abrogations par bloc** (section, chapitre, sous-section) | **non joué, instrument insuffisant.** Hors mandat par recalage du fil de tête. Mesure rejouée et confirmée : le champ `section` de `data/cgi.jsonl.gz` ne donne que le titre de la division feuille, 938 titres distincts dont beaucoup réemployés ; le regroupement par blocs contigus rend 2 700 blocs pour 3 484 enregistrements, taille médiane 1. Déblocage : passe d’enrichissement de l’extraction, autre fil |
| 1 | **Rangs « (Sans objet) » supprimés, renumérotation, reprise des renvois au IV — une seule passe** | **joué.** 18 rangs supprimés (anciens 35°, 141°, 150°, 236°, 261° à 264°, 271°, 275°, 281°, 282°, 293°, 302°, 305°, 306°, 357°, 407°), III renuméroté de 1° à 396°. **Sept listes de rangs reprises dans la même passe** — A, B, C, C bis, D, E, F du IV et du § 10.1 —, chacune rendant autant de rangs en sortie qu’en entrée, et **leur réunion couvre les 396 rangs sans trou ni doublon**. Compte au § 3 |
| 2 | **Forme fondue, un porteur et un seul par article abrogé** | **joué.** La pièce 4.7 est fondue : ses 181 articles d’avantage deviennent le **III quater** de la clause (date du H du IV), ses 185 articles d’assiette et de procédure le **III quinquies** (1er janvier 2028), son III devient le second alinéa du III quinquies, son IV est absorbé par le H du IV et le second alinéa du VI. La pièce devient une notice de péremption. **Table des porteurs au § 2** |
| 3 | **Deux régimes de dates ; les dates communes d’entrée en vigueur sont quatre, non deux** | **joué.** Les deux régimes sont écrits aux III quater et III quinquies. Les quatre dates communes, lues sur le IV de la clause, sont le **1er janvier 2027** (A, B), le **1er juillet 2027** (D, amorce du C, première marche du F), le **1er janvier 2028** (C, C bis, totalité du F, III quinquies, défaut du H) et le **1er janvier 2029** (E). Inscrites à la pièce 4.6, qui porte trois dates hors de ces quatre (1er juillet 2028, 2029 et 2030) et les déclare comme exceptions, avec leur motif |
| 4 | **Articles 1608, 1609 et 1609 F ne se recopient nulle part ; six sièges vivants à viser** | **joué, contrôlé au dépôt.** Les trois périmés sont `ABSENT` de l’extrait et **ne figurent dans aucune des neuf pièces du mandat** (recherche jouée sur les neuf textes lus). Les six sièges vivants sont tous `VIGUEUR` : 1607 bis (depuis 2025-02-16), 1607 ter (2024-04-11), 1609 B (2026-07-01), 1609 C (2023-12-31), 1609 D (2023-12-31), 1609 G (2025-02-16) |
| 5 | **Siège du tableau des plafonds : article 125 de la loi n° 2025-127, non le I de l’article 46 de la loi de finances pour 2012** | **joué, avec un écart de mesure inscrit.** Le I de l’article 46 de la loi n° 2011-1977 est « (Abrogé) » ; l’article est `ABROGE_DIFF`, fin de version au 1er janvier 2030. **Écart avec le mandat** : il n’y subsiste pas que le III bis — le II (assiette du plafond) et le III (reversement de l’excédent, frais de recouvrement) subsistent aussi. Le tableau des plafonds est au I de l’**article 125 de la loi n° 2025-127 du 14 février 2025** (`VIGUEUR`, version du 21 février 2026, LEGIARTI000053563909). Corrigé en trois endroits de la pièce 4.2 B, avec la coordination due sur le III bis de l’article 46 |
| 6 | **Article 81, fin programmée au 1er janvier 2029 — vérifier et inscrire la conséquence** | **joué, et le point se ferme.** L’article 81 est `ABROGE_DIFF`, fin de version au 1er janvier 2029. **Aucun rang visant l’article 81 n’est daté au-delà** : les rangs 52° à 55° et 61° relèvent du C (impôt dû au titre de 2028), tous les autres du A (revenus de 2026). **Le E, seule lettre datée du 1er janvier 2029, ne vise aucun rang de l’article 81.** Le 19° est abrogé au titre de 2026 : le point « sort du 19° au-delà du 1er janvier 2029 », ouvert au § 8 de la clause depuis le 20261004, est clos |
| 7 a | **Prélèvements sur les jeux supprimés** | **non joué — vecteur non tranché.** Sièges relevés à `etats/U7.md` : CGI, articles 302 bis ZJ, 302 bis ZK, 302 bis ZL, 302 bis ZM, 302 bis ZO, 1609 novovicies, 1609 tricies, 1609 untricies, 1609 duotricies, 1609 tertricies, 1609 quatertricies, avec les définitions communes des articles 302 bis ZG, 302 bis ZH et 302 bis ZI, retenues pour coordination. Une part de leur produit est affectée à des régimes obligatoires de base : le vecteur est partagé entre loi de finances et loi de financement, et le partage n’est pas arbitré. **Question fermée n° 3** |
| 7 b | **Redevances sanitaires alignées au minimum autorisé par le règlement (UE) 2017/625** | **non joué — source tarifaire hors du dépôt.** Sièges : CGI, articles 302 bis N à 302 bis XA, exclus du dispositif de 4.2 A par motif européen. L’alignement « au minimum autorisé » exige les taux minimaux de l’annexe IV du règlement, **qui n’est pas au dépôt de droit et dont aucun chiffre ne s’invente** (règle : aucun montant approximé). **Question fermée n° 2** |
| 8 | **193 articles de transposition du droit de l’Union, maintenus** | **sans écriture due, vérifié.** Le 3° du II de la clause est en place et les couvre. Aucune ligne écrite |
| 9 | **Trois franchises sectorielles de taxe sur la valeur ajoutée manquant au III** | **joué.** Relevées au dépôt et inscrites à deux rangs : **297°**, article **L. 213-105** du code des impositions sur les biens et services — franchise des activités lucratives accessoires des organismes sans but lucratif, qui renvoie au premier alinéa du 1 bis de l’article 206 du code général des impôts — et **341°**, articles **L. 233-10** et **L. 233-11** du même code — plafonds de franchise propres à l’avocat, à l’avocat au Conseil d’État et à la Cour de cassation, à l’auteur d’œuvre de l’esprit et à l’artiste-interprète. Les trois sont `VIGUEUR_DIFF` au 1er janvier 2027. **La franchise générale de l’article L. 233-9 est maintenue et n’est visée nulle part.** Les deux rangs relèvent du D du IV, 1er juillet 2027 |
| 10 | **Pièce 4.6 au circuit A — vérifier seulement** | **vérifié, conforme.** Cartouche, intention et V du dispositif concordants, au mot près de la formule commune du circuit A. Aucune ligne de dispositif touchée. L’écart déjà déclaré par la pièce — la section « Correspondance avec la refonte » lit encore le gisement en circuit B — est rappelé et reste dû au registre des sources de gage |
| 11 | **Typographie : apostrophes droites et espaces insécables à la clause, à 4.4 et à 4.6** | **joué sur les trois.** Clause générale : 1 011 apostrophes droites converties, 0 restante. Pièce 4.6 : 73 converties, 0 restante. Pièce 4.4 : 162 converties, 0 restante. Espaces insécables posées devant `;`, `:`, `!`, `?`, `%` et à l’intérieur des guillemets français, sur les trois pièces (et sur 4.2 B, réécrite par ailleurs : 267 apostrophes converties) |
| 12 | **Pièce de suppression de la taxe sur les salaires** | **signalée, comme demandé, et non écrite.** Due, hors mandat. Arbitrée supprimée progressivement en 2028, 16 Md€, dernier maillon ; les listes la portent encore comme « imposition maintenue, hors champ de la clause » ; son vecteur est en **loi de financement**, la taxe étant affectée aux régimes de base. Sièges relevés à `etats/U7.md` : CGI, articles 231, 231 A, 231 bis D, 231 bis I, 231 bis L, 231 bis N, 231 bis P, 231 bis Q, 231 bis R, 231 bis S, 231 bis U, 231 bis V, 1679 et 1679 A |
| 13 | **Gage : un euro, un circuit ; aucune niche nommée ne gage une pièce du circuit B ; chaque pièce qui perd une recette porte sa clause** | **contrôlé sur les neuf pièces, un écart déjà déclaré, aucun nouveau.** Clause générale : aucun gage dû, elle fait croître la recette · 4.2 A : gage État · 4.2 B : gage double, collectivités puis État · 4.2 C : gage double · 4.2 D : gage État · 4.4 : gage double · 4.6 : aucun gage, circuit A, clause de restitution · SS-03 : aucun gage, circuit A, clause de restitution · III quater et III quinquies de la clause : aucun gage, silence délibéré du lot 19, inscrit comme tel. **Aucune niche nommée ne gage une pièce du circuit B** : toutes les clauses de gage du circuit B visent la majoration du taux de l’article 219 et la dotation globale de fonctionnement, jamais une source nommée. **Écart déjà déclaré, non nouveau** : la ligne de 4.6 au registre des sources de gage doit passer du circuit B au circuit A |

---

## 2. Table des porteurs d’abrogation — le contrôle « exactement un porteur »

| porteur | ce qu’il abroge | compte | date |
|---|---|---|---|
| clause, article 1er, **III** (396 rangs) | subdivisions et articles portant une niche, relevés sur l’annexe des dépenses fiscales, et deux rangs de franchise sectorielle | 461 lignes d’annexe exploitables + 2 franchises, sur 396 rangs | calendrier du IV, lettres A à F, par le H |
| clause, article 1er, **III bis** | lignes de tableaux de taux et renvois du code des impositions sur les biens et services | 21 points | 1er juillet 2027 |
| clause, article 1er, **III ter** | part Corse des fonds d’investissement de proximité | 1 point | 1er janvier 2027 |
| clause, article 1er, **III quater** (ex-4.7, I) | articles entiers portant un avantage fiscal, qu’aucune autre pièce n’abroge | **181 articles**, 12 plages | date du H, à défaut 1er janvier 2028 |
| clause, article 1er, **III quinquies** (ex-4.7, II) | articles entiers d’assiette, de procédure, de recouvrement, de barème ou sans objet | **185 articles**, 16 plages | 1er janvier 2028 |
| clause, **article 2** (= SS-03) | niches sociales | 24 rangs, 13 articles distincts | 1er juillet 2027, par tiers pour deux rangs |
| **4.2 A** | sièges de 21 impositions de l’État | 42 adresses, 116 articles développés | 1er juillet 2027 et 1er janvier 2028 |
| **4.2 B** | sièges de 57 impositions affectées | 63 adresses, 698 articles développés | 1er juillet 2027 et 1er janvier 2028 |
| **4.2 C** | droits de mutation locaux et abattements des droits à titre gratuit | 42 articles | 1er janvier 2028 |
| **4.2 D** | abattements, exonérations, taxe forfaitaire sur les objets précieux, surtaxe des plus-values | 20 articles | 1er janvier 2028 |
| **4.4** | impositions fondues dans la taxe foncière unique, impôt sur la fortune immobilière compris, et dotations de péréquation | 34 articles du code général des impôts, 24 du code général des collectivités territoriales | 1er janvier 2028 |
| **4.5**, **4.6** | aucune abrogation : taux et paramètres | 0 | — |

**Verdict du contrôle : chaque article abrogé a un porteur et un seul.** Les 366 articles des III quater et III quinquies sont, par construction du lot U7, ceux qu’aucune autre pièce n’abroge — 316 articles abrogés ailleurs en ont été retirés avant écriture, et le contrôle « déjà abrogés ailleurs » a été rejoué par le lot V1 contre la clause dans son état final.

**Six adresses portent un double visa interne, à deux niveaux différents, et ce n’est pas une double abrogation** : la clause les abroge en partie à son III et en entier aux III quater et III quinquies, à la même date — articles 35 bis, 199 duovicies, 237 bis A et 1051 (III quater) ; articles 150 VJ et 788 (III quinquies). **La fonte les ramène dans une seule pièce** : le contrôle, qui demandait auparavant de croiser deux amendements, se joue désormais à l’intérieur d’un seul article.

**Zéro article à zéro porteur relevé** sur le périmètre mesuré ; les 301 articles retenus pour coordination ne sont pas abrogés, et c’est voulu : un article qu’un article maintenu cite encore attend la coordination de ce renvoi. La pièce de coordination est due et n’est au mandat d’aucun fil.

---

## 3. Renvois repris et vérifiés — le compte

### 3.1 Renvois internes à la clause, repris dans la même passe que la renumérotation

| liste | rangs en entrée | rangs en sortie | perdus | ajoutés |
|---|---:|---:|---:|---:|
| IV, A (§ 10.1) | 91 | 91 | 0 | 0 |
| IV, B | 102 | **109** | 0 | **7** |
| IV, C | 45 | 45 | 0 | 0 |
| IV, C bis | 20 | 20 | 0 | 0 |
| IV, D (§ 10.1) | 90 | **92** | 0 | **2** |
| IV, E | 32 | 32 | 0 | 0 |
| IV, F | 7 | 7 | 0 | 0 |
| **réunion** | 387 | **396** | **0** | **9** |

**Les sept listes sont vérifiées une par une.** Aucun rang n’est perdu. Les neuf ajouts sont tous motivés : **sept** sont les rangs d’investissement outre-mer rétablis le 20261005 et jamais classés — ils tombaient au A par défaut alors que l’avantage y est la contrepartie d’un investissement, et ils vont au B par application de la règle de classement du § 10.1 ; **deux** sont les rangs de franchise sectorielle ajoutés, qui vont au D. **Couverture entière : les 396 rangs sont classés, aucun n’est orphelin, aucun n’est classé deux fois.** Le A n’est plus un reliquat implicite : il est énuméré.

Autres renvois internes repris : § 3.1 (répartition par texte porteur, 295 · 93 · 2 · 1 · 5), § 6 points 5 et 9 (rangs 129° et 257°), bloc [interne] des taux après abrogation (rangs 301°, 302°, 312°, 314°, 321°), § 10.1 en entier.

### 3.2 Renvois entrants, depuis les autres pièces du mandat — 25 relevés, vérifiés un par un

| pièce | ancien rang | nouveau rang | état |
|---|---|---|---|
| 4.2 B | 298° | **285°** | **appliqué** |
| 4.2 B | 389° | **374°** | **appliqué** |
| 4.2 B | 401° | **386°** | **appliqué** |
| 4.6 | 316° | **301°** | **appliqué** |
| 4.6 | 347° | **332°** | **appliqué** |
| SS-03 | 47° · 50° · 51° · 65° · 67° | **46° · 49° · 50° · 64° · 66°** | **rendu en clair, application due** |
| 4.2 C | 237° · 242° · 243° · 252° · 259° · 266° | **233° · 238° · 239° · 248° · 255° · 258°** | **rendu en clair, application due** |
| 4.2 D | 47° · 51° · 52° · 87° · 88° · 90° · 94° · 99° · 108° | **46° · 50° · 51° · 86° · 87° · 89° · 93° · 98° · 107°** | **rendu en clair, application due** |

**Pourquoi vingt renvois sont rendus en clair et non appliqués.** `methode/appui_des_passes.md` : « Une pièce qui porte de longues énumérations — listes nominatives d’articles, tableaux de verdicts — ne se réécrit pas pour une correction locale : ses divisions corrigées se rendent en clair et s’appliquent par copie d’octets, R8. Le critère est le risque de déformation, et il se juge pièce par pièce. » Les pièces SS-03, 4.2 C et 4.2 D portent chacune un tableau de verdicts article par article, aucune n’est nommée par le mandat pour une correction de fond, et **les vingt renvois sont tous dans un bloc `[interne]`, aucun dans un dispositif** : aucun amendement déposable n’est atteint. La correction se pose en une passe de copie d’octets, sur la table ci-dessus.

La table de passage complète, ancien rang → nouveau rang, se reconstruit en une ligne : un rang garde son numéro diminué du nombre de rangs « (Sans objet) » qui le précèdent, augmenté de 1 au-delà de l’ancien 312° et de 1 encore au-delà de l’ancien 355°.

---

## 4. Adresses contrôlées, et leurs verdicts — millésime LEGI 20261001

**12 adresses contrôlées au dépôt par la présente passe**, chacune une à une :

| adresse | verdict | précision |
|---|---|---|
| CGI, 1608 | **ABSENT** | attendu : périmé, ne se recopie nulle part |
| CGI, 1609 | **ABSENT** | attendu |
| CGI, 1609 F | **ABSENT** | attendu |
| CGI, 1607 bis | `VIGUEUR` | version du 2025-02-16 |
| CGI, 1607 ter | `VIGUEUR` | version du 2024-04-11 |
| CGI, 1609 B | `VIGUEUR` | version du 2026-07-01 |
| CGI, 1609 C | `VIGUEUR` | version du 2023-12-31 |
| CGI, 1609 D | `VIGUEUR` | version du 2023-12-31 |
| CGI, 1609 G | `VIGUEUR` | version du 2025-02-16 |
| CGI, 81 | `ABROGE_DIFF` | fin de version au 2029-01-01 |
| loi n° 2011-1977, art. 46 | `ABROGE_DIFF` | fin au 2030-01-01 ; **son I est « (Abrogé) »**, son II, son III et son III bis subsistent |
| loi n° 2025-127, art. 125 | `VIGUEUR` | version du 2026-02-21, LEGIARTI000053563909, porte le tableau des affectations et des plafonds |

**3 adresses relevées et contrôlées pour l’inscription des franchises** : CIBS, L. 213-105, L. 233-10, L. 233-11 — les trois `VIGUEUR_DIFF` au 1er janvier 2027. Adresse de contexte lue et non visée : CIBS, L. 233-9 (franchise générale), `VIGUEUR_DIFF`, maintenue.

**366 adresses entrées à la clause par la fonte** : contrôlées une à une au lot U7 et **non rejouées ici** — 345 `EXISTE`, 21 `ABROGE_DIFF`, aucun `ABSENT`, aucun `ABROGE`. Le texte des deux énumérations est repris sans un caractère de différence.

**Total : 0 `ABSENT` non attendu, 0 `ABROGE`.** Les trois `ABSENT` sont ceux que le mandat annonçait, et ils ne sont visés par aucune pièce.

---

## 5. Références laissées hors contrôle, et la raison de chacune

Reprise n° 1 du 20261007 — un contrôle dit ce qu’il n’a pas vu.

| ensemble | nombre | raison |
|---|---:|---|
| les 433 références distinctes du dispositif de l’article 1er de la clause, contrôlées le 20261005 | 433 | **non rejouées** : la passe ne touche aucune d’elles. Le III est renuméroté, non réécrit : les adresses sont reportées caractère pour caractère par la table de passage |
| les 698 articles développés du dispositif de 4.2 B et les 116 de 4.2 A | 814 | **non rejoués** : la passe ne touche aucun dispositif de ces deux pièces |
| renvois entrants sur les 396 rangs du III et sur les 366 articles des III quater et III quinquies | **non dénombrés** | relevé déclaré dû et non fait depuis le 20261004 ; à ce volume il appelle son propre fil et un relevé mécanique |
| les 301 articles retenus pour coordination | 301 | cités par un article maintenu : ils ne s’abrogent qu’avec la coordination de ce renvoi, qui est un autre mandat |
| article 1-1 de la loi n° 86-897 du 1er août 1986 ; article 107 de la loi n° 2021-1104 | 2 | hors extrait LEGI — déjà déclarés par la clause, inchangés |
| annexe IV du règlement (UE) 2017/625 (taux minimaux des redevances de contrôle officiel) | 1 | hors du dépôt de droit, qui ne porte aucun texte de l’Union : le point 7 b ne se joue pas sans elle |
| sièges des prélèvements sur les jeux au code de la sécurité sociale (part affectée aux régimes de base) | **non relevés** | le vecteur n’est pas arbitré : relever les sièges d’un véhicule non choisi serait du travail perdu |
| structure hiérarchique des divisions du code général des impôts | — | **instrument vide**, mesuré deux fois : 0 article sur 3 484 porte une chaîne hiérarchique |

---

## 6. Pièce par pièce

| pièce | écrite | ce qui a bougé |
|---|---|---|
| `clause_generale_niches_20261005.md` | **oui** | III renuméroté, 412 → **396** rangs (18 supprimés, 2 ajoutés) · III quater et III quinquies créés, 366 articles · IV, B, C, C bis, E et F : listes de rangs reprises · H élargi aux III quater et III quinquies · VI élargi à leurs textes réglementaires · § 1, § 3, § 6, § 7, § 8, § 9 et § 10 recalés · cartouche de passe et invariant `Appui` portés · § 9 condensé, les 45 lignes identiques de recodification de la TVA rendues en une · **typographie : 1 011 apostrophes converties** · exposé non touché |
| `P1/4_7_abrogations_cgi.md` | **oui** | **périmée et fondue** : notice de péremption, table de ce que la fonte a déplacé, contrôle du porteur unique, rang P1-24 périmé. Les listes nominatives et le contrôle d’adresse restent à `etats/U7.md`, non recopiés (R8) |
| `P1/4_2_refonte_taxes_B_taxes_affectees.md` | **oui** | **siège du tableau des plafonds corrigé** en trois endroits (article 125 de la loi n° 2025-127) · coordination due sur le III bis de l’article 46 inscrite · 3 renvois au III repris · point à vérifier n° 6 ajouté · invariant `Appui` porté · typographie |
| `P1/4_6_tva_taux_reduits.md` | **oui** | 2 renvois au III repris (332°, 301°) · franchises sectorielles ajoutées au périmètre lu · **quatre dates communes inscrites**, trois marches déclarées exceptions · circuit A vérifié conforme · invariant `Appui` complété · typographie |
| `P1/4_4_taxe_fonciere_unique.md` | **oui** | **typographie** · invariant `Appui` porté · **écart de paramètre de péréquation signalé** : le dispositif écrit 2 % + 2 %, l’arbitrage du 20261005 dit 3 points + 3 % — environ 5 Md€ de masse du fonds. Non corrigé : arbitrage de fond, question fermée n° 1. **Le cartouche, le dispositif et l’exposé ne bougent pas** : l’écart reste visible, inscrit au premier point à vérifier de la pièce |
| `P1/4_2_refonte_taxes_A_taxes_etat.md` | non | vérifiée : aucun renvoi au III de la clause, aucun point du mandat ne la touche au dispositif. Les deux points non joués (jeux, redevances sanitaires) la viseraient : ils attendent un arbitrage |
| `P1/4_2_refonte_taxes_C_dmto_franchise.md` | non | vérifiée : **6 renvois au III rendus en clair**, R8 |
| `P1/4_2_refonte_taxes_D_plus_values.md` | non | vérifiée : **9 renvois au III rendus en clair**, R8 |
| `SS/n7b_ss03_liste_niches_sociales.md` | non | vérifiée : **5 renvois au III rendus en clair**, R8. 24 rangs inchangés, gage et circuit conformes |
| `P1/4_5_solde_refonte_is_tf.md` | **non touchée** | hors mandat par consigne expresse |

---

## 7. Questions fermées pour l’auteure

1. **Taxe foncière unique, prélèvement de péréquation** : le dispositif de 4.4 écrit 2 % des valeurs locatives et 2 % du produit ; l’arbitrage du 20261005 dit « 3 % prélevé en pt de TF partout et 3 % du montant de TF partout ». Garde-t-on le 2 % + 2 % écrit, ou passe-t-on à 3 points + 3 % comme l’arbitrage le dit ?
2. **Redevances sanitaires** : l’alignement « au minimum autorisé » exige les taux de l’annexe IV du règlement (UE) 2017/625, hors du dépôt de droit. La pièce renvoie-t-elle au minimum réglementaire sans écrire de chiffre, ou l’auteure fournit-elle la source tarifaire pour écrire des tarifs en dur ?
3. **Prélèvements sur les jeux** : leur suppression s’écrit-elle en loi de finances à la pièce 4.2 A, ou en loi de financement avec la taxe sur les salaires, une part de leur produit étant affectée aux régimes obligatoires de base ?
