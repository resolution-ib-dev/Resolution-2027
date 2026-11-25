# Paramètres de la liasse de crédits — note de lecture, 20261116

**Fichier** : `referentiels/parametres_credits_20261116.tsv` — 296 lignes et 81 colonnes depuis le 20261117 (§ 8) ; 285 lignes et 62 colonnes à l'origine. Tabulations, UTF-8.
**Produit par** : `python3 appareil/controle_liasse_classeurs.py construire <Dépenses de l'État.xls> <Synthèse des chiffrages.xlsx>`. Rien n'y est saisi à la main.
**Rejoué par** : `python3 appareil/controle_liasse_classeurs.py controler` (TSV et liasse seuls, sans classeur).
**Mandat** : pilotage, 20261116, chantiers n° 3 et 5. Aucun amendement n'est modifié.

## 1. Les pièces lues

| pièce | où | état |
|---|---|---|
| `Dépenses de l'État.xls`, onglets `SynthèseR`, `Economies R`, `Données PAP 2026` | téléchargée de `france-resolution.fr/donnees/`, 1 543 168 octets, SHA-256 `b07c6a47…4e1714` depuis la correction du 20261117 (`8a4a08fd…a566dd` avant) | *relevé* ; lue en cache par `xlrd`, jamais réenregistrée. Son identité avec `Site-ETNP/site/donnees/` est **héritée** du pilotage : l'attache du dépôt privé n'a pas abouti dans ce fil |
| `Synthèse des chiffrages.xlsx`, onglets `Détail Economies`, `Flux` | même adresse, 344 594 octets, SHA-256 `ac56012f…e64e84a` | *relevé*, même réserve. `Flux!C6` = 129,459 ; `Flux!G6` = 227,445 ; le 236,402 du mandat n'a pas été recherché, il ne sert pas ici |
| `livrables/registre_calcul_etatB.md`, § 1, 3, 4, 5, 6, 10, 14 | dépôt | *relevé* ; le § 4 est lu par l'outil, 27 lignes |
| `livrables/suivi_trajectoire_20261015.md`, § 0 et 1 | dépôt | *relevé* ; 27 lignes lues par l'outil |
| `livrables/registre_exceptions_dates.md`, entier | dépôt | *relevé* ; trois dates de 2027 touchent des crédits de l'État |
| `livrables/flux_par_agent_20261015.md` et `referentiels/Flux_par_agent_20261015.xlsx` | dépôt | *relevé* ; le mensuel 2027 est rejoué par l'outil |
| `appareil/chaine_credits.py`, `DATE_CAT` | dépôt | *relevé* ; l'outil vérifie à chaque construction que la table n'a pas changé |
| `livrables/depot_2027/LIASSE_PLF_P2.md` | dépôt | *relevé* ; 22 amendements, 57 lignes de programme |
| `referentiels/etatB_2027_bg.tsv` | dépôt | *relevé* ; crédits ouverts par programme |

Les formules de `SynthèseR` ont été lues en clair sur une copie de travail convertie hors dépôt ; les valeurs, elles, viennent du cache du `.xls`.

## 2. Le grain

**Une ligne = un poste du classeur × un programme × une catégorie**, coupée par action là où le registre (§ 14) ou le classeur isole une action : programmes 102, 103, 174, 183 et 203.

Entrent toutes les lignes que `Economies R` arrête :

- catégories 21, 23, 31 et titre 5 des programmes hors « périmètre essentiel » (colonne E vide) ;
- catégories 32, 61, 62, 63, 64 marquées « Oui » ou « En 3 ans ».

Somme du brut des lignes hors « En 3 ans » : **67 494,166 M€ d'AE et 73 160,944 M€ de CP** — *relevé*. Ce sont les totaux « arrêtés » de la table A du classeur de suivi absent (67 494,2 et 73 160,9, `methode/suivi_depenses_20261007.md` § 4). **La table A se retrouve donc depuis le classeur du site, et ses montants « arrêtés » sont bruts.**

Restent hors du fichier : la catégorie 22 (le classeur ne l'arrête pas), et les drapeaux « Fusion CI », « Bourse », « Flux OM », « Sécu », qui ne sont pas des économies restituées.

226 lignes sont dans la liasse, 59 n'y sont pas (§ 5).

## 3. Les colonnes, et d'où vient chaque valeur

| colonnes | contenu | statut |
|---|---|---|
| `poste_classeur`, `adresse_poste` | poste de `SynthèseR` et ses cellules | *déduit* de la formule du poste ; prouvé au § 4 |
| `ligne_registre`, `libelle_registre` | ligne du § 4 (cellule de `Détail Economies`) | *déduit* du § 14 du registre. « aucune » : catégorie 63. « non rangée » : le § 14 la laisse hors de toute ligne. D14 et D21 : hors du tableau du § 4 |
| `brut_ae`, `brut_cp`, `adresse_pap` | somme des colonnes L et M de `Données PAP 2026`, en euros, avec les numéros de ligne | *relevé* |
| `drapeau_classeur`, `adresse_drapeau` | « Oui », « En 3 ans » ou « périmètre non essentiel » | *relevé* |
| `taux_classeur`, `adresse_taux` | part du brut que le classeur supprime en régime plein | *relevé* sur la formule citée |
| `part_an1_classeur`, `adresse_part_an1` | part du régime plein atteinte « à horizon 1 an » | *relevé* sur la formule citée |
| `plein_cp_classeur`, `an1_cp_classeur` | brut de CP × taux, puis × part de première année | *déduit* ; la somme par poste retombe sur `SynthèseR` (§ 4) |
| `s4_*`, `adresse_s4` | les colonnes du § 4 : F, socle, « F net », rythme, acteur, date, fraction, montant 2027, programme | *relevé*. **Ces valeurs sont celles de la ligne doctrinale entière** et se répètent sur chacune de ses lignes : elles ne s'additionnent pas |
| `socle_s4_contre_classeur`, `rythme_s4_contre_classeur` | identique, diffère, registre seul, classeur seul | *déduit* |
| `date_registre_s4`, `date_suivi_trajectoire` | mois d'effet 2027 lu à chaque tableau | *relevé* |
| `date_registre_exceptions` | exception inscrite, s'il y en a une | *relevé* |
| `date_flux_par_agent` | la pièce ne porte aucune date par ligne ; l'outil rejoue le flux mensuel 2027 de l'agent avec les dates du § 4 et donne l'écart | *déduit* |
| `date_chaine_credits` | `DATE_CAT` de la catégorie | *relevé* |
| `dates` | « concordent », « se contredisent », « registre muet » | *déduit* : § 4 contre `DATE_CAT` |
| `amendement`, `liasse_ae_programme`, `liasse_cp_programme`, `adresse_liasse` | montant inscrit au programme, répété sur ses lignes | *relevé* |
| `fraction_liasse`, `coefficient_liasse`, `residuel_liasse` | règle de `chaine_credits.py` : fraction de la catégorie ; 0,27 pour le titre 2 (0,90 × 30 %) ; résiduel de CP | *relevé* au code |
| `liasse_ae_ligne`, `liasse_cp_ligne` | part de la ligne dans le montant du programme, avant écrêtement | *déduit* ; la somme redonne les 57 montants inscrits à 1 € près |
| `etatB_2027_ae`, `etatB_2027_cp`, `ecretement` | crédit ouvert ; « oui » si la liasse est ramenée à ce crédit | *relevé*, puis *déduit* |
| `cible_classeur_*` | brut × taux × part de première année. Année pleine, sans date ni résiduel | *déduit* |
| `cible_registre_*` | chaîne du § 1 du registre : brut × (1 − socle) × rythme × fraction ; CP au résiduel du § 3 ; titre 2 selon le § 10 | *déduit* |
| `cible_mixte_*` | taux et rythme du classeur × part d'année de la date du § 4 ; CP au résiduel | *déduit* |

Une cible vide veut dire **sans paramètre** : le classeur ne donne ni taux ni première année (catégorie 63, subvention à France Travail, « En 3 ans »), ou le § 4 ne porte pas la ligne.

## 4. La preuve du rattachement

Somme des lignes en régime plein contre la cellule de `SynthèseR`, en M€ — *relevé*, sortie de `construire` :

| poste | lignes | `SynthèseR` | écart |
|---|---:|---:|---:|
| Salaires | 2 958,736 | D6 = 2 958,736 | 0 |
| Fonctionnement | 2 704,238 | E6 = 2 704,140 | +0,099 |
| Investissement | 1 075,475 | F6 = 1 075,455 | +0,020 |
| Anah, MaPrimeRénov', Ademe, autres opérateurs | 152,910 · 1 333,325 · 921,354 · 3 764,591 | E19, F19, G19, H19 | 0 |
| Entreprises : travail, audiovisuel, France 2030, autres | 6 902,470 · 3 878,313 · 3 223,795 · 1 149,796 | C25, D25, E25, F25 | 0 |
| Ménages : APL, AME, emploi service | 16 116,736 · 1 094,670 · 1 062,106 | C31, D31, E31 | 0 |
| Ménages : autres | 1 604,633 | F31 = 1 604,633 (1 820,310 avant le 20261117) | 0 |
| Associations : APD, hébergement, travail, France 2030, autres | 2 953,202 · 2 454,587 · 2 276,823 · 1 639,971 · 3 244,669 | C37, D37, E37, F37, G37 | 0 |

Trois écarts, tous expliqués :

- **Fonctionnement et investissement** : la formule retire 233 et 51, arrondis de 232,884 et 50,976 (action « Routes – Entretien » du programme 203).
- **Autres ménages, 215,7 M€ — corrigé le 20261117** (demande de l'auteur : « corrige l'erreur et propage »). `SynthèseR!F32` retranchait l'AME et l'emploi service après leur abattement de 10 % alors qu'elle partait du brut : les 10 % conservés de ces deux postes revenaient dans « Autres ». La formule devient `=('Economies R'!S4-C31-F20-197,995)*0,9-D31-E31` (`Site-ETNP/outils/retoucher_depenses_menages.py`, mêmes jetons réordonnés, fichier de même taille). *Relevé* : six cellules changent — F32, F31, I7, I6, C7, C6. Le classeur de synthèse portait déjà les bonnes valeurs (chèques aux ménages : 8,4 la première année, 19,9 en régime plein) et ne bouge pas ; la liasse non plus.

## 5. Les lignes du classeur absentes de la liasse

59 lignes — *relevé* :

- **« En 3 ans »**, 13,2 Md€ d'AE au budget général : le classeur les sort de la restitution salariale et n'en donne que le total (`SynthèseR!I14:K14`).
- **Comptes spéciaux** : avances à l'audiovisuel public (3,88 Md€, état D), quatre comptes d'affectation spéciale.
- **Budget général, 1,45 Md€ d'AE et 6,50 Md€ de CP** : mission « Investir pour la France de 2030 » (programmes 421 à 425, AE presque nulles), programmes 149, 205, 349 et 379, et l'entretien des routes du 203.

## 6. Limites

- Les deux classeurs sont ceux du 16 novembre 2026. Une retouche de `SynthèseR` change les taux : `construire` se rejoue.
- Le rattachement d'une ligne à un poste repose sur les formules de `SynthèseR`, qui visent des cellules (`P65`, `R155`, `X68`…) ; si une ligne s'insère dans `Economies R`, la preuve du § 4 le montre.
- `cible_classeur_cp` n'applique pas le CP résiduel : le classeur raisonne en économie, non en caisse.
- Les colonnes R à V de `Détail Economies` (incidence par acteur) ne sont pas reprises : elles ne portent de valeur que pour les ménages, les actifs et les entreprises.

## 7. La règle retenue — colonnes ajoutées le 20261116 (régénération)

Le fichier passe à **81 colonnes** ; les 62 premières gardent leur sens. Les 19 dernières sont **la table de paramètres que lisent `chaine_credits.py` et `generer_liasse_p2.py`**, qui ne portent plus aucune constante de calcul.

| colonnes | contenu | statut |
|---|---|---|
| `etatB_2027_mission`, `etatB_2027_programme`, `etatB_2027_titre2`, `correspondance_2027` | mission, libellé et titre 2 ouverts à l'état B 2027 ; pour quatre programmes renommés (149, 205, 349, 379), la correspondance vient de `referentiels/correspondance_programmes_pap2026_etatB2027.tsv`, qui dit son statut | *relevé* ; *déduit* pour 149 et 349 |
| `regle_taux` | part du brut supprimée en régime plein : classeur du site | *relevé* (colonne `adresse_taux`) |
| `regle_rythme`, `regle_date`, `regle_fraction` | rythme, date d'effet et fraction d'exercice : § 4 du registre | *relevé* ; *tranché par le pilotage* là où le registre est muet |
| `regle_part_conservee` | un sixième pour la subvention à France Travail (registre § 3) | *relevé* |
| `regle_net_indemnite` | 0,30 sur le titre 2 : indemnité de départ retranchée (registre § 10 ; `SynthèseR!D7`) | *relevé* |
| `regle_residuel` | résiduel de CP du § 3 du registre | *relevé* |
| `regle_cas`, `regle_origine` | « registre », « registre muet », « registre, classeur muet », « classeur muet et registre muet », et la phrase qui dit d'où vient chaque paramètre | *déduit* |
| `objet_expose` | le nom public de la ligne, pour la phrase de date de l'exposé | *tranché en propre* |
| `retenu`, `motif_hors_liasse`, `amendement_mission` | la ligne entre-t-elle dans un amendement de mission, sinon pourquoi, et lequel | *déduit* |
| `cible_projet_ae`, `cible_projet_cp` | brut × taux × rythme × fraction × (1 − part conservée) × net d'indemnité ; CP au résiduel. Avant plafond du programme | *déduit* |

**Tranché par le pilotage le 20261116, révocable** : le classeur ne garde la main que sur le brut et le taux ; le rythme et la date sont ceux du § 4 du registre. `cible_mixte_*` (rythme du classeur) reste au fichier pour mémoire : la liasse ne la suit plus.

Les colonnes `liasse_*`, `amendement` et `adresse_liasse` décrivent la liasse **en place au moment de la construction**, sous l'ancienne règle de reconstitution : elles ne servent plus qu'aux cibles `classeur`, `registre`, `mixte` et `liasse` du contrôle.

## 8. Les liasses sur mesure — table reconstruite le 20261117

**296 lignes, 81 colonnes** ; 261 lignes retenues dans un amendement de mission, 35 hors liasse. *Relevé* à la reconstruction ; la colonne `n` est renumérotée (onze lignes insérées dans l'ordre du PAP).

- **Catégorie 22, 11 lignes ajoutées** (1 995 722 820 € bruts) : cotisations de l'employeur des programmes hors périmètre essentiel. Poste à part, « Cotisations employeur — suit le sort des salaires » : `SynthèseR!D6` ne compte que les catégories 21 et 23 et la preuve du § 4 ne bouge pas. Règle : celle du titre 2 (0,90 × 6/12 × 0,30), d'après l'onglet « Mesure » du classeur de suivi, ligne 41. *Tranché par le pilotage, révocable.*
- **« En 3 ans », 10 lignes** : `retenu` passe à « oui » pour les huit lignes du budget général (taux 1, rythme ⅓, date et fraction de la ligne du § 4). Les deux lignes du compte d'affectation spéciale « Développement agricole et rural » (775, 776) restent hors liasse : état D.
- **Programme 162** : `amendement_mission` = 40, mission « Outre-mer ». Une mission sans amendement prend le numéro qui suit le dernier de la liasse ; aucun numéro en place ne change.
- Les colonnes `liasse_*` et les cibles `classeur`, `registre`, `mixte` et `liasse` décrivent toujours l'ancienne règle ; la catégorie 22 n'y entre pas.
