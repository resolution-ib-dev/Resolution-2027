# Compte complet du calendrier des flux, 2027-2030 — note de lecture, 20261117

**Fichiers.**

- `referentiels/calendrier_compte_complet_20261117.tsv` — 105 mesures, 118 lignes mesure × agent, 48 mois de janvier 2027 à décembre 2030.
- `referentiels/calendrier_compte_complet_niches_20261117.tsv` — 257 dépenses fiscales supprimées, une par ligne, avec la division du IV de l'amendement n° 1 qui les date.
- `referentiels/compte_complet_parametres_20261117.tsv` — 33 valeurs relevées aux classeurs du site et au registre, avec leur adresse de cellule.

**Produits par** `python3 appareil/calendrier_compte_complet.py construire`. **Rejoués par** `… controler` (39 contrôles). Tableaux de l'état : `… etat`. Leviers du § 17 : `… leviers`. Le croisé du 20261116 n'est pas modifié ; `calendrier_mesures_mois.py controler` reste à 0 échec.

**Unité et signe.** Md€, en mesure, hors règle de CP résiduel. **Montant positif = le solde public s'améliore = l'agent privé de la ligne paie ou perd.** Le croisé du 20261116 a le même signe (positif = économie). Pour lire le compte d'un agent, on change le signe.

**Ce que le fichier porte que le croisé ne portait pas** : les niches fiscales et sociales, les huit lignes de première partie et sociale, la baisse de CSG, l'assurance chômage, le rendement du patrimoine, l'épargne rendue, et les lignes de la refonte que le registre date (§ 17 et § 18).

## Colonnes du fichier principal

| colonne | contenu | statut |
|---|---|---|
| `id` | cellule du registre (D5 à D43), `CSG`, `NAnn` et `NBnn` (niches fiscales, gage et solde), `NSA`, `NSB`, `TVA21`, `TS`, `TRI`, `P1-35`, `CHO-`, `CHO+`, `PAT`, `EPA` | — |
| `circuit` | **A** : la restitution, les 236,4 Md€ du classeur. **B** : la refonte « à rendement constant », pour les seules lignes que le registre date et chiffre | *tranché en propre* |
| `nature`, `famille`, `mesure` | ce que la ligne est | *relevé* |
| `agent`, `part` | l'agent privé qui paie ou reçoit, et sa part de la mesure | voir « Agents » |
| `date_effet`, `regle_de_calendrier` | la date d'application et la règle qui place les montants dans les mois | date *relevée*, sauf mention ; mois *déduits* |
| `piece` | la pièce et l'adresse | *relevé* |
| `statut` | relevé, hérité, déduit, posé ou calculé, ligne par ligne | — |
| `2027-01` … `2030-12` | le montant du mois, pour cet agent | *déduit* |
| `total_AAAA` | somme des douze mois | *déduit* |

Une mesure partagée entre deux agents fait deux lignes de même `id` : la somme des lignes d'un `id` redonne la mesure.

## Agents

Huit lignes d'agents privés. Six viennent du § 6 du registre. Deux sont ajoutées, et dites :

- **« Ménages actifs — épargne »** : ce qui est porté au compte d'épargne, indisponible jusqu'à la retraite (amendement n° 27, IV). Ce n'est pas de l'argent sur la paie.
- **« Ménages, non répartis »** : les ménages que la pièce ne partage pas entre actifs et sans revenus d'activité — l'onglet `Bénéficiaires` dit « Ménages » sans plus, le versement de patrimoine est égal par personne. *Tranché en propre* : aucune clé n'est inventée pour les répartir.

**Niches fiscales** : l'agent est la colonne « Nature » de l'onglet `Bénéficiaires` (*relevé*). « Entreprises et ménages » : moitié, moitié. « Véhicules » : ménages (`Détail Niches`!L21). « Locaux », « Parcelles » : moitié, moitié (*posé*, 0,24 Md€). Deux corrections relevées à `Détail Niches` : l'abattement de 10 % sur les pensions va aux ménages sans revenus d'activité (N10) ; les exonérations salariales, marquées « S » au classeur, aux ménages actifs (M9).

**Niches sociales** : un tiers aux actifs, deux tiers aux entreprises (`Détail Niches`!M24 et O24, *relevé*).

**Coupes** : clé du croisé du 20261116, inchangée (clé posée, non mesurée).

**Huit lignes de première partie** : clé *posée* sur la règle du 20261116 — logement aux ménages, eau moitié ménages moitié entreprises, cinéma, transports et chambres consulaires aux entreprises.

## Les niches fiscales : comment chaque dépense reçoit sa date

Le IV de l'amendement n° 1 de la liasse P1 fixe sept régimes. Le module lit au texte les listes d'items du III que les B, C, C bis, E et F nomment, puis rattache chaque dépense fiscale :

1. **par l'item du III qui abroge son siège** (colonne `rattachement` = « III, n° ») : la référence juridique de l'annexe est comparée, article et alinéa, aux 350 items. **116 dépenses, 23,53 Md€ de gage.**
2. **par l'impôt**, quand le IV ne distingue pas (TVA, accises et autres droits au D ; droits d'enregistrement et impositions locales au A) : **107 dépenses, 15,24 Md€.**
3. **par la nature de l'avantage**, quand le III abroge par intitulé de division du code et non par article : dons au F ; agriculture, services à la personne, garde au E ; épargne, parts et quotient au C ; réductions, crédits et déductions au B ; le reste au A. **34 dépenses, 4,36 Md€ — *déduit*, à relire.**

| division du IV | date d'application (*relevée*) | première incidence (*déduite*) | gage, Md€ par an |
|---|---|---|---:|
| D — TVA, accises, autres droits | fait générateur à compter du 1er juillet 2027 | juillet 2027, par douzièmes | 13,84 |
| A — impôt sur le revenu | impôt dû au titre de 2026 | septembre à décembre 2027 (solde), puis par douzièmes | 8,31 |
| A — impôt sur les sociétés | exercices clos à compter du 1er janvier 2027 | janvier 2027, par douzièmes | 1,84 |
| A — enregistrement ; impôts locaux, IFI | 1er janvier 2027 ; dus au titre de 2027 | janvier 2027 ; septembre à décembre 2027 | 0,36 ; 0,93 |
| B — impôt sur les sociétés | dépenses et investissements à compter du 1er janvier 2027 | janvier 2027, par douzièmes | 5,38 |
| B — impôt sur le revenu | dépenses et investissements à compter du 1er janvier 2027 | septembre à décembre 2028 | 3,11 |
| C — salaires et produits d'épargne | revenus et opérations à compter du 1er janvier 2028 | janvier 2028, par douzièmes (retenue à la source) | 5,02 |
| C — parts, quotient, décote | impôt dû au titre de 2028 | septembre à décembre 2029 | 1,96 |
| E — agriculture, services à la personne | un tiers en 2027, deux tiers en 2028, tout en 2029 | par tiers | 0,55 |
| F — dons | moitié au 1er juillet 2027, tout au 1er janvier 2028 | sociétés : juillet 2027 ; revenu : septembre 2028 | 1,81 |

**Règle de mesure, *déduite* et unique** : une dépense fiscale rend son montant annuel une fois par an à compter de sa première année d'incidence ; la première année est placée dans les mois où l'impôt se paie, les suivantes par douzièmes. **Trois limites, dites** :

- l'impôt sur les sociétés est compté dans l'exercice où il naît ; son encaissement tombe au solde, en mai de l'année suivante : **7,60 Md€ comptés en 2027 ne sont en caisse qu'en mai 2028** ;
- le G du IV maintient les avantages nés d'engagements antérieurs « jusqu'au terme » : le stock n'est chiffré par aucune pièce, et les lignes du B (8,50 Md€) sont donc des **majorants** les premières années ;
- le double encaissement d'une première année (solde de l'année passée et retenue à la source de l'année en cours) n'est pas compté.

**Familles** : « revenus » = impôt sur le revenu et autres impôts directs de l'annexe ; « sociétés » = impôt sur les sociétés et catégorie mixte « impôt sur le revenu et impôt sur les sociétés » ; « énergie et autres » = accises, autres droits, impôts locaux, enregistrement. Le classeur range une part de la catégorie mixte à l'impôt sur le revenu : **19,78 et 8,21 au classeur, 19,42 et 8,57 ici** ; TVA 9,94 et autres 5,20 des deux côtés ; total 43,13 des deux côtés.

## Les autres lignes

| ligne | montant | date | statut |
|---|---|---|---|
| huit lignes de première partie et sociale (D7 à D14, D21) | 8,30 Md€ en régime plein (*relevé*, `Détail Economies` F) | **1er janvier 2027, *tranché en propre*** d'après R-P : le registre ne les date pas. D21 : par tiers, 1er juillet 2027, 1er janvier 2028, 1er janvier 2029 (*relevé*, PLFSS n° 1, IV) | rythme *relevé* à la colonne G ; redonne la colonne D du classeur à 0,2 Md€ près |
| baisse de CSG | § 2 du registre | six marches, juillet à décembre 2027 | *relevé* |
| niches sociales | 9 + 9 Md€ | périodes d'activité à compter du 1er juillet 2027 | *relevé* |
| taux réduits de TVA (n° 21) | § 17 | 1er juillet 2028, 2029, 2030 | *relevé* |
| taxe sur les salaires (PLFSS n° 3) | § 17 | par tiers, 2028, 2029, 2030 | *relevé* |
| suppressions du tri | § 18 : −12,1 en 2027, −32,6 ensuite | 1er juillet 2027 ; plein en 2028 | *relevé* ; minorant |
| contribution exceptionnelle (n° 35) | −5,2 en 2027 | par douzièmes, *posé* : « non mensualisé » au § 18 | montant *relevé* |
| assurance chômage | 29,6 Md€ | **1er janvier 2028, *posée*** : aucune disposition de la liasse ne porte la transformation | montant *relevé* ; deux lignes, ce que perdent les allocataires et ce que reçoivent les actifs en épargne |
| rendement du patrimoine | 17,60 Md€ au classeur ; 18,2 au simulateur | 1er janvier 2028 (*relevé*, n° 27, VIII) | la contrepartie publique n'est établie par aucune pièce |
| épargne rendue | *calculée* | jamais avant le 1er janvier 2028 | voir ci-dessous |

**Épargne rendue.** Règle du classeur (*relevée*, `Input Capitalisation` E2 à E8) : tout ce qui dépasse la baisse de CSG va à l'épargne. Le surplus est le solde du circuit A hors chômage et hors patrimoine. La ligne `EPA` rend chaque mois le surplus cumulé qui ne sera plus repris — le plus bas des cumuls à venir —, de sorte que le cumul ne passe jamais sous zéro.

## Ce que les contrôles prouvent, et ce qu'ils ne prouvent pas

Ils prouvent : les 27 coupes sont celles du croisé, au mois ; coupes, restitution et solde redonnent le § 5 ; les huit lignes atteignent 8,30 ; les niches redonnent 43,126 et 29,141, dépense par dépense ; le IV est lu sans doublon ni item hors du III ; TVA, taxe sur les salaires et tri redonnent les § 17 et 18 ; la somme des privés est l'opposé du solde public chaque mois ; le fichier se régénère à l'identique ; l'épargne rendue ne rend jamais le cumul négatif.

Ils ne prouvent pas : qu'une dépense fiscale est rattachée à la bonne division (le rattachement par nature est une déduction) ; que les clés d'agent sont justes ; que la mesure est la caisse.
