# Croisé mesure × mois, 2027-2030 — note de lecture, 20261116

**Cette reconstruction fait foi.** Le tableau mesure × mois d'origine est introuvable, au dépôt comme au projet (`methode/passation_calendrier_20261116.md` § 1, *hérité*). *Tranché par le pilotage, révocable.*

**Fichier** : `referentiels/calendrier_mesures_mois_20261116.tsv` — 27 lignes doctrinales du § 4 du registre, 48 mois de janvier 2027 à décembre 2030. En mesure, en Md€, signe positif = économie. Hors règle de CP résiduel.
**Produit par** : `python3 appareil/calendrier_mesures_mois.py construire`. **Rejoué par** : `… controler`.

| colonnes | contenu | statut |
|---|---|---|
| `cellule`, `ligne_doctrinale`, `F_regime_plein`, `socle`, `F_net_du_socle`, `rythme`, `date_effet_2027`, `fraction_2027`, `programme_porteur` | § 4 du registre | *relevé* |
| `pan` | bloc de `Détail Economies`, comme au § 16 | *relevé* |
| `agent` | onglet « La clé d'incidence » de `Flux_par_agent_20261015.xlsx` | *relevé* |
| `perimetre` | « État » ou « hors état B de l'État » (D40 à D43) | *déduit* du § 4 |
| `marche_annuelle` | 1er juillet pour une sortie en trois ans entrée en juillet, 1er janvier sinon | *déduit* du § 16 |
| `regime_plein_hors_fenetre` | départs d'agents : ce qui reste à venir après 2030 | *déduit* |
| `2027-01` … `2030-12` | la mensualisation : le montant de l'exercice (§ 5), un douzième par mois entre deux marches ; 2027 par parts égales du mois d'effet à décembre | *déduit* |
| `total_AAAA`, `registre_s5_AAAA` | somme des douze mois, et la valeur du § 5 | *déduit*, *relevé* |

**Départs d'agents (D38, D43)** : 30 % de la ligne sur toute la fenêtre. *Validé par l'auteur le 20261116* (relevé à `methode/arbitrages.md`) : le régime plein compte la ligne entière, la première année 30 %. Le moment du passage au plein n'est fixé par aucune pièce : l'indemnité dure d'une à sept années selon l'ancienneté. *Tranché en propre, révocable* : 30 % jusqu'en 2030, le reste « à terme ».

**D25 en 2028** : marche au 1er juillet, comme au § 16 ; le classeur de flux du 15 octobre l'étale par douzièmes. Même total annuel.

**Les pièces du 15 octobre** (§ 6 et § 16 du registre, `flux_par_agent_20261015.md`, `Flux_par_agent_20261015.xlsx`) sont antérieures à la mise à niveau de D16, D38, D41 et D43. Le contrôle les rejoue avec les valeurs antérieures de ces quatre lignes, gardées au § 5 : c'est la preuve de la méthode, non de l'état à jour.
