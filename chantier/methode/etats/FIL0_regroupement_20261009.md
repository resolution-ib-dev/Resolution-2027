# État du fil 0 — regroupement des abrogations par bloc, outre-mer — 20261009

**Porteur** : fil 0 de la liasse de première partie, Cowork, 20261009.
**Mandat** : l'auteure, 20261009 — `methode/procedure_liasse_P1_20261009.md`, § 8, fil 0.
**Domicile** : `methode/etats/FIL0_regroupement_20261009.md`.
**Appui** : `methode/procedure_liasse_P1_20261009.md` · `methode/etats/SUIVI_chantier_20261009.md` ·
`methode/fragments/arbitrages/20261009-outre-mer-sorti.md` · `methode/etats/T3.md` ·
`livrables/registre_colonnes_depot_2027.md` · `methode/regles_redactionnelles.md` ·
`methode/appui_des_passes.md` (R-G, R-H, R-I, R8) · skills `resolution-chantier`, `redaction-legistique`,
`confrontation` · dépôt de droit `Resolution-2027` cloné, millésime LEGI **20261007**.
**Objet écrit** : `livrables/depot_2027/clause_generale_niches_20261005.md` (P1-31, P1-04, SS-01), et les
renvois qui citent son III : pièces 4.2 A, B, C, D, 4.3, 4.6, `n7b_m022`, `n7b_ss03`, registre des sources de gage.

---

## 1. Mesure d'entrée — rendue à l'auteure avant écriture

| objet | mesure |
|---|---|
| rangs du III portant au moins un article d'un bloc entier | **88 sur 396**, dont **66** en totalité |
| articles du III quater dans un bloc entier | **84 sur 181** |
| articles du III quinquies dans un bloc entier | **62 sur 183** |
| blocs entiers (chapitre, section, sous-section, subdivision numérotée) | **185** |
| rangs ultramarins relevés à `T3.md` | **19** : 12 sortis le 20261007, **7 présents** (143° à 145°, 187°, 219° à 221°) |
| exclusion des articles 73 et 74 au II | **déjà écrite**, réserve de domicile comprise |

Le message d'entrée portait 85 rangs et 183 blocs : il comptait le III après retrait des sept rangs
ultramarins. Ce retrait n'est pas joué (§ 2) ; les comptes ci-dessus sont ceux du III entier.

**Caractère entier** : joué sur le dépôt de droit — toute version d'article applicable au 1er janvier 2027
ou après, rangée sous la division, doit être abrogée en entier par la clause (III, III quater ou III
quinquies). Rangement relevé au champ `section` du dépôt, chaîne hiérarchique complète.

## 2. Mesure de sortie — le mandat point par point

| point du mandat | verdict | mesure |
|---|---|---|
| mesurer d'abord, rendre le compte avant écriture | **joué** | § 1, rendu par message avant toute écriture |
| regrouper par bloc partout où le bloc tombe entier, par script | **joué** | **171 blocs regroupés** : III 76 blocs (104 articles), III quater 56 (68), III quinquies 39 (48) |
| — sauf | **non joué, motivé** | **14 blocs laissés article par article** : 13 dont les articles relèvent de deux divisions ou de deux dates (les regrouper changerait une date) · 1 sans numéro au code (« Disposition générale », article 1020) |
| laisser article par article les abrogations partielles | **joué** | aucune subdivision d'article touchée ; ensemble des subdivisions abrogées identique avant et après |
| retirer les dix-neuf rangs ultramarins | **non joué — arbitrage de l'auteure du 20261009** | 12 déjà sortis le 20261007 (« déjà fait ») · 7 maintenus : investissements outre-mer non propres aux résidents, abolis comme les autres niches |
| renuméroter le III | **joué** | **396 → 389 rangs** ; 5 fusions de rangs ; 68 rangs réécrits sur leur bloc ; les autres inchangés à l'octet |
| reprendre tous les renvois dans la même passe | **joué** | clause : IV (B, C, C bis, E, F, quatrième phrase du C), § 10.1, [interne] des taux, § 3.1, § 6 points 5 et 9, § 10.1 « Outre-mer », comptes · pièces : 4.2 A (1), 4.2 B (2), 4.2 C (4), 4.2 D (8), 4.3 (2), 4.6 (5), `n7b_m022` (3), `n7b_ss03` (5) · registre des sources de gage (20 lignes, reprise inscrite) |
| écrire au II l'exclusion 73-74 et Nouvelle-Calédonie, la rendre en clair | **non joué — déjà écrite** | texte en vigueur à la pièce rendu en clair à l'auteure, non tenu pour validé |
| rendre la table de passage | **joué** | § 11 de la clause, reprise au § 4 ci-dessous |
| ne corriger aucun autre dispositif, aucun exposé, aucune question fermée | **tenu** | dispositif : seuls III, III quater, III quinquies et IV touchés ; exposé intact |

**Contrôle** : `appareil/fil0_regroupement/controle_regroupement.py` — lit la clause avant passe (pièce qui
fait foi) et la clause écrite, résout chaque désignation de division sur le dépôt de droit. Quatre tests :
numérotation continue · couverture des listes du IV et du § 10.1 · conservation exacte des articles et
subdivisions abrogés (III, III quater, III quinquies) · lettre du IV de chaque rang identique à celle de ses
articles d'origine. **0 anomalie.** Jeu de fautes `fautes_regroupement.py` : désignation fausse, article
retiré, rang dupliqué, lettre retournée — **les quatre mordent**.

## 3. Constats inscrits, non corrigés

1. **Pièce 4.3, renvois de gage déjà faux avant la passe** : « 129°, 54°, 62°, 56°, 137°, 139° et 167° »
   décalés d'un rang sur le III du 20261007 (157 bis était au 128°). Recalés sur l'article nommé, non
   sur le numéro : 126°, 51°, 59°, 53°, 134°, 136°, 159°. Le cartouche daté de la reprise V1 garde son
   « 139° ».
2. **Registre des colonnes, P1-31** : porte « III à 396 rangs ». Compte d'état, non renvoi : non touché,
   dû au prochain recalage du registre (chaîne B).
3. **Liasses assemblées du 20261008** : elles portent l'ancien III. Dérivés, régénération déjà due
   (`SUIVI`, § 6).
4. **Dépôt** : les dix fichiers écrits ici et le présent état s'ajoutent à la liste du recalage du dépôt.

## 4. Table de passage

**Elle fait foi pour résoudre tout renvoi au III antérieur au 9 octobre 2026**, dans la présente pièce — cartouches datés et §§ 7, 8 et 9 compris — comme dans toute autre pièce du paquet ou registre. Un renvoi antérieur au 20261007 se résout d’abord par la table du § 10.1 de la reprise du 20261007, puis par celle-ci.

**Rangs fusionnés** — chaque rang fusionné abroge la division qui portait les articles des rangs réunis : 30° + 31° → **30°** · 35° + 36° → **34°** · 158° + 159° + 160° + 161° → **156°** · 209° + 210° → **204°** · 220° + 221° → **214°**. **Aucun rang n’est retiré ni ne change de lettre du IV.**

| ancien rang (20261007) | rang nouveau (20261009) |
|---|---|
| 1° à 30° | 1° à 30° |
| 31° à 35° | 30° à 34° |
| 36° à 158° | 34° à 156° |
| 159° | 156° |
| 160° | 156° |
| 161° à 209° | 156° à 204° |
| 210° à 220° | 204° à 214° |
| 221° à 396° | 214° à 389° |

