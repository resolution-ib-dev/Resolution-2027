# CR — relecture externe de l'extraction P1 fiscale

**Porteur** : fil de relecture externe de l'extraction P1 fiscale, 20261007.

**Mandat** : l'auteure, 20261007 — « jouer la checklist rédactionnelle et le contrôle d'adresses, verdict ligne à ligne, puis impression docx aux conventions françaises ; ne produire aucune pièce nouvelle, signaler les écarts sans les corriger en silence ». Puis, 20261007 — « imprime la liasse ». Puis, 20261007 — le présent CR.

**Domicile** : `sortie/cr_relecture_p1_fiscale.md`.

**Mesure** : 9 fichiers de pièce lus, 11 amendements imprimables identifiés · 26 lignes de checklist, 26 verdicts · 1 077 occurrences d'adresses, 922 adresses distinctes contrôlées + 1 contrôlée hors lot · 23 écarts relevés, 1 levé, 0 corrigé · 2 livrables docx.

**Appui** : `methode/procedure_fin_de_chantier_depot_2027.md`, `methode/appui_des_passes.md` (projet, 20261007) · `redaction-legistique/references/regles_redactionnelles.md`, `redaction-legistique/references/structure_ppl.md` (skill `redaction-legistique`, disque, 20261007) · `reference/guide_legistique.md` (projet) · dépôt de droit `resolution-ib-dev/Resolution-2027`, cloné et interrogé par `droit.py`, millésime LEGI 20261001, fraîcheur 6 jours · `methode/COMMUN.md` et `LISEZ-MOI.md` du paquet · skill `impression-docx`.

---

## 1. Ce qui a été joué, et ce qui ne l'a pas été

| contrôle dû au LISEZ-MOI | mandat | état |
|---|---|---|
| checklist rédactionnelle | nommé | **joué**, 26 verdicts |
| contrôle d'adresses | nommé | **joué**, 923 adresses |
| test de rattachement | non nommé | **non joué**, reste dû |
| contestabilité | non nommé | non joué, hors périmètre |

Aucune pièce du paquet n'a été modifiée. Aucune pièce nouvelle n'a été écrite. Les deux docx produits sont des impressions, non des rédactions.

## 2. Contrôle d'adresses

**Instrument.** Dépôt de droit cloné sans jeton, `droit.py etat` joué, millésime LEGI 20261001, six jours, non périmé. Aucune recherche sur Légifrance, aucune recherche ailleurs — R-A tenue.

**Méthode.** Extraction programmée des références du dispositif de chaque pièce, bloc `[interne]` exclu. Résolution du code par trois voies : désignation explicite en fin d'énumération, « du même code » résolu sur l'antécédent nommé, chapeau modificatif (« Le code X est ainsi modifié ») qui gouverne les lignes suivantes. Chaque adresse passée à `droit.article` à trois dates.

**Résultat.**

| | 7 oct. 2026 | 1er juil. 2027 | 1er janv. 2028 |
|---|---|---|---|
| `VIGUEUR` | 740 | 740 | 740 |
| `VIGUEUR_DIFF` | 2 | 163 | 164 |
| `ABROGE_DIFF` | 95 | 18 | 17 |
| non encore applicable | 84 | 0 | 0 |
| `ABSENT` | 1 | 1 | 1 |

**Aucun `ABROGE`.** L'unique `ABSENT` est l'article 1-1 de la loi n° 86-897 du 1er août 1986, hors extrait, déjà déclaré « à vérifier » par la clause générale elle-même. Les 84 adresses non encore applicables sont les articles du livre II du CIBS issus de la recodification TVA au 1er janvier 2027 : toutes applicables aux dates d'effet des pièces, régime déclaré par les pièces.

**107 références laissées hors contrôle**, toutes non-adresses de droit : renvois internes à l'amendement, articles 73 et 74 de la Constitution, articles du texte déposé, prose de cartouche. Une seule était une vraie adresse — l'article 179 de la loi n° 2019-1479 — contrôlée hors lot : `VIGUEUR`, version du 21 février 2026, I arrêté au 33°, l'insertion d'un 34° par l'amendement 4.5-b est juste.

**Dix-sept adresses portent une fin programmée sans version successeur** à la date d'effet de la pièce qui les vise. Huit sont à la pièce 4.7, dont c'est précisément l'objet. L'article 81 du CGI (fin au 1er janvier 2029) appelle une vérification sur sa version 2029, le calendrier du IV de la clause générale plaçant certaines de ses subdivisions après cette date.

## 3. Checklist rédactionnelle — 26 verdicts

21 lignes de `regles_redactionnelles.md` + 5 conventions de `methode/COMMUN.md`.

| verdict | lignes |
|---|---|
| CONFORME | 1, 3, 4, 5 (adresses), 8, 10, 13, 20, 22, 25 |
| CONFORME SOUS RÉSERVE | 9 |
| SANS OBJET | 7, 11, 12, 14, 17, 21 |
| ÉCART | 2, 6, 15, 16, 18, 19, 23, 24, 26 |

Détail et corrections proposées : `controle_p1_fiscale.docx`, partie Deux. Aucune ligne n'est restée sans verdict.

## 4. Les vingt-trois écarts

**Cinq de fond, qui appellent un arbitrage avant toute reprise.**

| n° | pièce | écart |
|---|---|---|
| 4 | 4.5 | le taux normal de l'IS est délégué au décret entre 20 % et 28 %. L'article 34 C réserve le taux à la loi. L'exposé invoque la décision n° 87-239 DC, cons. 4 — qui vaut pour un plafond encadré, non pour la fixation du taux. |
| 5 | 4.5 | borne macroéconomique (PO/PIB) flottante au IV : aucun siège, aucune conséquence juridique. |
| 11 | 4.7 | son calendrier renvoie à « l'article 33 bis de la présente loi », qui n'existe pas. La pièce ne se suffit pas — contre le § 4 de la procédure. Elle partage par ailleurs son accroche avec la clause générale. |
| 19 | 4.2 A | l'exposé écrit que les taux réduits de TVA prennent fin au 1er juillet 2027. Ce sont les *niches* de TVA. La pièce 4.6 fait tomber les taux réduits en 2028-2030. |
| 6 et 7 | liasse, 4.6 | la règle de sortie n'est pas uniforme : la pièce 4.6, rangée au circuit B par COMMUN, porte la clause de restitution du circuit A ; la pièce 4.7 ne porte ni gage, ni clause d'équilibre, ni restitution (écart 8). |

**Quatre de complétude.**

- **9** — l'article 2 de la clause générale (jambe sociale, SS-03) n'a pas de texte dans le paquet ; le LISEZ-MOI annonce par ailleurs « aucune pièce de loi de financement », ce que la clause générale dément.
- **22** — l'exposé sommaire de l'article 1er de la clause générale est **incomplet** : un seul paragraphe écrit, sur la TVA, les autres déclarés « restent à écrire ». C'est l'article pivot de la liasse.
- **23** — l'article 3 de la clause générale n'a ni exposé sommaire ni accroche fixée.
- **10** — quatorze rangs du III portent « (Sans objet) ». Décision juste pour les renvois du IV, mais un texte déposé portant quatorze rangs vides se lit mal.

**Quatre de forme et de typographie.**

- **13** — la clause générale porte 520 apostrophes droites, zéro typographique. Les huit autres pièces n'en portent aucune.
- **14** — l'espace insécable est tenue aux pièces 4.2 A à 4.2 D, 4.5 et 4.7, absente de la clause générale, de la pièce 4.4 et de la pièce 4.6.
- **15** — la pièce 4.6 n'ouvre pas par le bloc de forme commun : pas de « présenté par », pas de filet, accroche sur une seule ligne.
- **16** — « exercices clos à compter du 31 décembre 2026 » (clause générale, IV, A) : formule consacrée, mais l'exception n'est pas inscrite comme le § 4 l'exige.

**Un de méthode.**

- **18** — aucune des neuf pièces ne porte l'invariant **Appui**. Les pièces sont antérieures au verrou du 20261006 : l'écart est historique, non fautif. Il se referme à la prochaine passe de chaque pièce.

**Trois levés ou argumentés.**

- **3 levé** — article 179 de la loi n° 2019-1479 : contrôlé, `VIGUEUR`, insertion juste.
- **4 argumenté** — la pièce cite une autorité ; l'écart tient, la pièce n'est pas muette.
- **17** — toutes les dates d'entrée en vigueur autres que celle de l'écart 16 sont des 1er janvier ou des 1er juillet.

**Quatre à vérifier** : 1, 2, 12, 21 — détail au contrôle.

## 5. Mesure de la liasse — le LISEZ-MOI est démenti sur deux comptes

| | LISEZ-MOI | mesure |
|---|---|---|
| amendements | 9 | **11** |
| exposés sommaires | 9 | **10**, dont un incomplet |
| pièces de loi de financement | aucune | **une**, l'article 2 de la clause générale, sans texte |

La pièce 4.5 porte deux amendements : le taux unique de l'IS (après l'article 32, première partie) et le rapport annuel d'équilibre (après l'article 75, seconde partie). La clause générale porte trois articles, dont deux imprimables.

**Conséquence pour le fil commanditaire** : la mesure d'entrée du paquet est fausse. Le § 0 du mandat de projet veut qu'un fil mesure avant de corriger ; la mesure du paquet n'a pas été reprise depuis l'ajout de l'amendement 4.5-b.

## 6. Ce qui reste dû

1. **Test de rattachement**, pièce par pièce, verdict et porte citée. Appui : `guide_legistique` partie V, `domaine_lfss_LO111-3.md`, `test_rattachement.md`.
2. **Les trois réserves du LISEZ-MOI**, entières : les sept rangs d'outre-mer rétablis n'ont pas eu de contrôle de champ propre ; les trois franchises sectorielles de TVA manquent au III ; les dix-huit articles créateurs du texte déposé n'ont pas été vérifiés un par un — le texte déposé n'est pas joint au paquet.
3. **Arbitrage de l'auteure** sur les écarts 4, 5, 6, 7, 11 et 19.
4. **Exposés sommaires** : article 1er de la clause générale (à achever), article 3 (à écrire). Le § 5 de la procédure veut qu'un exposé se régénère en bloc après les croisements — donc pas avant les lots 13 à 19.
5. **Lots 13 à 19 non passés** : collectivités, aides ciblées, état B. Les pièces correspondantes ne sont pas au paquet.
6. **Invariant Appui** à porter aux neuf pièces.
7. **Registre des colonnes** non joint : l'ordre d'appel des deux amendements partageant l'accroche « après l'article 33 » n'est pas vérifiable ici.

## 7. Trois reprises de méthode, pour le fil commanditaire

**7.1 — R-B s'applique à son propre instrument.** Le contrôle d'adresses a rendu successivement 409, 327, 31, 20 puis 2 `ABSENT`. Aucune de ces mesures intermédiaires n'était un constat d'absence : toutes étaient des défauts de l'extracteur — un `re.I` qui faisait correspondre `[A-Z]` à « du », un suffixe de rang tronqué, une attribution de code qui débordait d'un chapeau au suivant. **Une mesure qui rend un grand nombre d'absences suspecte l'instrument avant le texte.** Proposition : inscrire cette règle en complément de R-B, et exiger qu'un contrôle d'adresses rende, à côté de son compte d'absences, le compte des références qu'il a laissées hors contrôle et la raison de chacune. Un contrôle qui ne dit pas ce qu'il n'a pas vu ne vaut pas.

**7.2 — Deux pièces nommées au mandat ne résolvent pas.** `redaction-legistique/references/regles_redactionnelles.md` n'est pas au projet : elle vit dans la skill `redaction-legistique`. `reference/structure_ppl.md` a été supprimée le 20261007, absorbée par `reference/guide_legistique.md` ; une copie subsiste sous `paquet/machine_v1_2_a3/procedures/`. Proposition : la ligne de lancement d'un fil de contrôle nomme `methode/appui_des_passes.md` et la skill, non des chemins de projet qui ont bougé. C'est exactement ce que le § « trois mécanismes » d'`appui_des_passes.md` prévoit — il n'a pas été suivi ici.

**7.3 — La skill `impression-docx` se contredit sur le nommage.** Son § 5 prescrit un nom daté (`NomDoc_20261007.docx`) ; sa règle de résolution des renvois interdit toute date dans un nom de livrable. J'ai retenu le nom canonique sans date. Proposition : corriger le § 5.

## 8. Livrables et leur domicile

| livrable | domicile | contenu |
|---|---|---|
| `controle_p1_fiscale.docx` / `.md` | `sortie/` | contrôle de sortie : 26 verdicts, contrôle d'adresses, 21 écarts, 14 pages |
| `liasse_p1_fiscale.docx` / `.md` | `sortie/` | 11 amendements, texte déposable, 48 pages |

**Composition de la liasse imprimée** : accroche, dispositif, exposé sommaire. Cartouches d'atelier et blocs `[interne]` écartés. Les écarts ne sont pas corrigés dans l'impression — la confusion niches / taux réduits de la pièce 4.2 A y figure telle quelle. La normalisation typographique appliquée au tirage (apostrophes typographiques, espaces insécables) est une convention d'impression, déclarée ici, et elle ne remonte pas aux pièces : les écarts 13 et 14 restent entiers au paquet.

**Aucun versement au projet ni au dépôt n'a été fait** : le mandat ne le nomme pas.
