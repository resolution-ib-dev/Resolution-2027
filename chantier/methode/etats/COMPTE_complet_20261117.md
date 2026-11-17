# Compte complet du calendrier des flux, 2027-2030 — état du 20261117

**Porteur** : fil d'exécution « calendrier, compte complet », branche `claude/calendrier-compte-complet`. **Destinataire** : fil de pilotage.
**Mandat** : fermer le compte du calendrier des flux — niches, autres recettes, épargne rendue, compte par agent et par mois (règles de l'auteure du 20261116 : agents tous privés, « le solde public est l'inverse de la somme des privés », « tout doit se compenser »).
**Pièces produites** : `referentiels/calendrier_compte_complet_20261117.tsv` (105 mesures, 118 lignes mesure × agent, 48 mois), sa note `_lisez_moi.md`, `referentiels/calendrier_compte_complet_niches_20261117.tsv` (257 dépenses fiscales), `referentiels/compte_complet_parametres_20261117.tsv` (33 relevés), `appareil/calendrier_compte_complet.py`.
**Contrôles** : `calendrier_compte_complet.py controler`, 39 contrôles, 0 échec ; `calendrier_mesures_mois.py controler`, 0 échec, croisé du 20261116 inchangé.
**Couche** : tout est **en mesure**, en Md€, hors CP résiduel. Dans les tableaux par agent, **positif = l'agent reçoit**, négatif = il paie ou perd ; le solde public est l'opposé de la somme.
**Provenance** : chaque chiffre de cet état sort de `calendrier_compte_complet.py etat` ou `leviers`, joué sur les fichiers au moment d'écrire. Les statuts — *relevé*, *hérité*, *déduit*, *posé*, *tranché en propre* — sont au § 4.

---

## 1. La page

### Par agent et par an, 2027-2030, toutes lignes comprises

| | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|
| Ménages actifs — transferts monétaires | +17,60 | +77,32 | +71,58 | +68,90 |
| Ménages actifs — services en nature | −18,91 | −26,35 | −32,50 | −32,50 |
| Ménages actifs — épargne | +0,00 | +104,87 | +84,65 | +88,26 |
| Ménages sans revenus d'activité | −7,23 | −38,00 | −38,00 | −38,00 |
| Ménages, non répartis | −3,41 | +0,06 | −10,10 | −13,91 |
| Agents publics | −1,97 | +0,84 | +0,12 | +0,12 |
| Entreprises | −36,54 | −54,15 | −66,34 | −64,32 |
| Associations | −2,37 | −5,50 | −7,03 | −7,80 |
| **Agents privés** | −52,81 | +59,08 | +2,37 | +0,73 |
| **Solde public** | +52,81 | −59,08 | −2,37 | −0,73 |
| dont circuit de restitution, hors patrimoine | +48,70 | −48,70 | −0,00 | +0,00 |
| dont rendement du patrimoine rendu | +0,00 | −17,60 | −17,60 | −17,60 |
| dont refonte, lignes datées au registre | +4,11 | +7,22 | +15,24 | +16,87 |
| **Solde public cumulé, fin d’exercice** | +52,81 | −6,27 | −8,63 | −9,37 |

### Par agent et par mois, 2027

| | janv | févr | mars | avril | mai | juin | juil | août | sept | oct | nov | déc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Ménages actifs — transferts monétaires | −0,12 | −0,12 | −0,12 | −0,12 | −0,12 | −0,12 | +0,25 | +1,68 | +1,96 | +3,39 | +4,82 | +6,25 |
| Ménages actifs — services en nature | −1,50 | −1,50 | −1,50 | −1,50 | −1,50 | −1,50 | −1,65 | −1,65 | −1,65 | −1,65 | −1,65 | −1,65 |
| Ménages actifs — épargne | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 |
| Ménages sans revenus d'activité | +0,00 | +0,00 | +0,00 | −0,21 | −0,21 | −0,21 | −0,30 | −0,30 | −1,50 | −1,50 | −1,50 | −1,50 |
| Ménages, non répartis | −0,05 | −0,05 | −0,05 | −0,05 | −0,05 | −0,05 | −0,31 | −0,31 | −0,63 | −0,63 | −0,63 | −0,63 |
| Agents publics | −0,06 | −0,06 | −0,06 | −0,06 | −0,06 | −0,06 | −0,67 | −0,51 | −0,35 | −0,19 | −0,03 | +0,13 |
| Entreprises | −2,15 | −2,15 | −2,15 | −2,15 | −2,15 | −2,15 | −3,78 | −3,78 | −4,02 | −4,02 | −4,02 | −4,02 |
| Associations | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | −0,40 | −0,40 | −0,40 | −0,40 | −0,40 | −0,40 |
| **Agents privés** | −3,88 | −3,88 | −3,88 | −4,09 | −4,09 | −4,09 | −6,85 | −5,26 | −6,58 | −4,99 | −3,40 | −1,81 |
| **Solde public** | +3,88 | +3,88 | +3,88 | +4,09 | +4,09 | +4,09 | +6,85 | +5,26 | +6,58 | +4,99 | +3,40 | +1,81 |
| dont circuit de restitution, hors patrimoine | +3,70 | +3,70 | +3,70 | +3,91 | +3,91 | +3,91 | +6,75 | +5,16 | +5,88 | +4,29 | +2,70 | +1,11 |
| dont rendement du patrimoine rendu | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 |
| dont refonte, lignes datées au registre | +0,18 | +0,18 | +0,18 | +0,18 | +0,18 | +0,18 | +0,10 | +0,10 | +0,70 | +0,70 | +0,70 | +0,70 |
| **Solde public cumulé** | +3,88 | +7,76 | +11,64 | +15,73 | +19,82 | +23,91 | +30,76 | +36,02 | +42,61 | +47,60 | +51,00 | +52,81 |

### Par agent et par mois, 2028

| | janv | févr | mars | avril | mai | juin | juil | août | sept | oct | nov | déc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Ménages actifs — transferts monétaires | +6,67 | +6,67 | +6,67 | +6,67 | +6,67 | +6,67 | +6,22 | +6,22 | +6,22 | +6,22 | +6,22 | +6,22 |
| Ménages actifs — services en nature | −2,20 | −2,20 | −2,20 | −2,20 | −2,20 | −2,20 | −2,20 | −2,20 | −2,20 | −2,20 | −2,20 | −2,20 |
| Ménages actifs — épargne | +52,61 | +3,91 | +3,91 | +3,91 | +3,91 | +3,91 | +4,89 | +4,89 | +5,73 | +5,73 | +5,73 | +5,73 |
| Ménages sans revenus d'activité | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 |
| Ménages, non répartis | +0,78 | +0,78 | +0,78 | +0,78 | +0,78 | +0,78 | +0,03 | +0,03 | −1,17 | −1,17 | −1,17 | −1,17 |
| Agents publics | +0,07 | +0,07 | +0,07 | +0,07 | +0,07 | +0,07 | +0,07 | +0,07 | +0,07 | +0,07 | +0,07 | +0,07 |
| Entreprises | −3,93 | −3,93 | −3,93 | −3,93 | −3,93 | −3,93 | −5,08 | −5,08 | −5,11 | −5,11 | −5,11 | −5,11 |
| Associations | −0,40 | −0,40 | −0,40 | −0,40 | −0,40 | −0,40 | −0,52 | −0,52 | −0,52 | −0,52 | −0,52 | −0,52 |
| **Agents privés** | +50,44 | +1,74 | +1,74 | +1,74 | +1,74 | +1,74 | +0,25 | +0,25 | −0,14 | −0,14 | −0,14 | −0,14 |
| **Solde public** | −50,44 | −1,74 | −1,74 | −1,74 | −1,74 | −1,74 | −0,25 | −0,25 | +0,14 | +0,14 | +0,14 | +0,14 |
| dont circuit de restitution, hors patrimoine | −48,70 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | −0,00 | −0,00 | −0,00 |
| dont rendement du patrimoine rendu | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 |
| dont refonte, lignes datées au registre | −0,27 | −0,27 | −0,27 | −0,27 | −0,27 | −0,27 | +1,22 | +1,22 | +1,60 | +1,60 | +1,60 | +1,60 |
| **Solde public cumulé** | +2,37 | +0,64 | −1,10 | −2,84 | −4,57 | −6,31 | −6,56 | −6,81 | −6,68 | −6,54 | −6,40 | −6,27 |

### Tout se compense-t-il ?

**Non, pas chaque année. Oui pour le circuit de restitution, en cumul, à compter de janvier 2028 — et à une condition.** Quatre écarts, une cause chacun.

| écart sur le solde public | 2027 | 2028 | 2029 | 2030 | cause |
|---|---:|---:|---:|---:|---|
| circuit de restitution, hors patrimoine | **+48,70** | **−48,70** | 0,00 | 0,00 | **le compte d'épargne n'existe qu'au 1er janvier 2028** (liasse P1, amendement n° 27, VIII, *relevé*) : le surplus de 2027 reste douze mois dans la sphère publique, puis il est rendu. Cumul nul à compter de janvier 2028 |
| rendement du patrimoine rendu | 0,00 | **−17,60** | **−17,60** | **−17,60** | **un versement sans ressource de flux en face** : c'est le rendement d'un stock transféré. Aucune pièce n'établit ce que la sphère publique cesse de percevoir ou se met à payer ; 17,60 est un majorant |
| refonte, lignes datées au registre | **+4,11** | **+7,22** | **+15,24** | **+16,87** | **le registre ne date qu'une partie de la refonte** : le solde des niches (38,1 Md€ par an) et la TVA y sont, les suppressions d'impôts n'y sont que pour 50,5 Md€ sur 137,05, le taux unique de l'impôt sur les sociétés et la taxe foncière unique n'y sont pas (§ 3.4) |
| **solde public** | **+52,81** | **−59,08** | **−2,37** | **−0,73** | |
| solde public cumulé | +52,81 | −6,27 | −8,63 | −9,37 | |

**Hors fenêtre** : 16,00 Md€ par an de départs d'agents, la part encore indemnisée, « à terme » (registre § 5).

**Le point dur de 2028 a disparu du circuit de restitution, en mesure.** Le registre le chiffrait à −29,24 Md€ parce qu'il ne comptait que les coupes. Avec les niches (49,23 Md€ en 2028) et les huit lignes de première partie (6,60), le surplus de 2028 est de **+26,57 Md€**, et aucun mois de la fenêtre n'est négatif. **Il reste mince au premier semestre 2028 : +1,44 Md€ par mois**, contre 9,54 de baisse de CSG. Le plus bas de la fenêtre est décembre 2027, +1,11.

**La condition** : que les niches rapportent à leur date. Sur le surplus de 2027 et 2028, 77,87 Md€ viennent des niches. Trois réserves pèsent dessus, chiffrées au § 3.1 : 7,60 Md€ d'impôt sur les sociétés comptés en 2027 ne sont en caisse qu'en mai 2028 ; 8,50 Md€ par an sont des majorants tant que les engagements antérieurs courent ; 4,36 Md€ sont datés par déduction.

**Les niches ne rapportent pas 52,1 Md€ la première année.** *Relevé* au IV de l'amendement n° 1 et au IV de l'amendement n° 1 du PLFSS : **28,64 Md€ en 2027, 49,23 en 2028, 52,12 en 2029.** Le classeur compte 52,1 dès l'année 1.

---

## 2. Le compte, mois par mois

Les quatre exercices, par agent, toutes lignes comprises.

### Par agent et par mois, 2029

| | janv | févr | mars | avril | mai | juin | juil | août | sept | oct | nov | déc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Ménages actifs — transferts monétaires | +6,19 | +6,19 | +6,19 | +6,19 | +6,19 | +6,19 | +5,74 | +5,74 | +5,74 | +5,74 | +5,74 | +5,74 |
| Ménages actifs — services en nature | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 |
| Ménages actifs — épargne | +6,59 | +6,59 | +6,59 | +6,59 | +6,59 | +6,59 | +7,19 | +7,19 | +7,68 | +7,68 | +7,68 | +7,68 |
| Ménages sans revenus d'activité | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 |
| Ménages, non répartis | −0,49 | −0,49 | −0,49 | −0,49 | −0,49 | −0,49 | −0,81 | −0,81 | −1,38 | −1,38 | −1,38 | −1,38 |
| Agents publics | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 |
| Entreprises | −5,35 | −5,35 | −5,35 | −5,35 | −5,35 | −5,35 | −5,69 | −5,69 | −5,72 | −5,72 | −5,72 | −5,72 |
| Associations | −0,52 | −0,52 | −0,52 | −0,52 | −0,52 | −0,52 | −0,65 | −0,65 | −0,65 | −0,65 | −0,65 | −0,65 |
| **Agents privés** | +0,55 | +0,55 | +0,55 | +0,55 | +0,55 | +0,55 | −0,08 | −0,08 | −0,20 | −0,20 | −0,20 | −0,20 |
| **Solde public** | −0,55 | −0,55 | −0,55 | −0,55 | −0,55 | −0,55 | +0,08 | +0,08 | +0,20 | +0,20 | +0,20 | +0,20 |
| dont circuit de restitution, hors patrimoine | −0,00 | −0,00 | −0,00 | −0,00 | −0,00 | −0,00 | −0,00 | −0,00 | −0,00 | −0,00 | −0,00 | −0,00 |
| dont rendement du patrimoine rendu | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 |
| dont refonte, lignes datées au registre | +0,91 | +0,91 | +0,91 | +0,91 | +0,91 | +0,91 | +1,55 | +1,55 | +1,66 | +1,66 | +1,66 | +1,66 |
| **Solde public cumulé** | −6,82 | −7,37 | −7,92 | −8,48 | −9,03 | −9,58 | −9,50 | −9,42 | −9,22 | −9,03 | −8,83 | −8,63 |

### Par agent et par mois, 2030

| | janv | févr | mars | avril | mai | juin | juil | août | sept | oct | nov | déc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Ménages actifs — transferts monétaires | +5,74 | +5,74 | +5,74 | +5,74 | +5,74 | +5,74 | +5,74 | +5,74 | +5,74 | +5,74 | +5,74 | +5,74 |
| Ménages actifs — services en nature | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 | −2,71 |
| Ménages actifs — épargne | +7,35 | +7,35 | +7,35 | +7,35 | +7,35 | +7,35 | +7,35 | +7,35 | +7,35 | +7,35 | +7,35 | +7,35 |
| Ménages sans revenus d'activité | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 | −3,17 |
| Ménages, non répartis | −1,00 | −1,00 | −1,00 | −1,00 | −1,00 | −1,00 | −1,32 | −1,32 | −1,32 | −1,32 | −1,32 | −1,32 |
| Agents publics | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 | +0,01 |
| Entreprises | −5,20 | −5,20 | −5,20 | −5,20 | −5,20 | −5,20 | −5,52 | −5,52 | −5,52 | −5,52 | −5,52 | −5,52 |
| Associations | −0,65 | −0,65 | −0,65 | −0,65 | −0,65 | −0,65 | −0,65 | −0,65 | −0,65 | −0,65 | −0,65 | −0,65 |
| **Agents privés** | +0,38 | +0,38 | +0,38 | +0,38 | +0,38 | +0,38 | −0,26 | −0,26 | −0,26 | −0,26 | −0,26 | −0,26 |
| **Solde public** | −0,38 | −0,38 | −0,38 | −0,38 | −0,38 | −0,38 | +0,26 | +0,26 | +0,26 | +0,26 | +0,26 | +0,26 |
| dont circuit de restitution, hors patrimoine | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 | +0,00 |
| dont rendement du patrimoine rendu | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 | −1,47 |
| dont refonte, lignes datées au registre | +1,09 | +1,09 | +1,09 | +1,09 | +1,09 | +1,09 | +1,72 | +1,72 | +1,72 | +1,72 | +1,72 | +1,72 |
| **Solde public cumulé** | −9,01 | −9,39 | −9,76 | −10,14 | −10,52 | −10,90 | −10,64 | −10,39 | −10,13 | −9,88 | −9,62 | −9,37 |

### Par famille de mesures et par an

Signe de cette table et de la suivante : **positif = le solde public s'améliore**. Les huit lignes de première partie sont rangées aux pans « Opérateurs » (D7 à D14) et « Chèques » (D21).

| | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|
| A · dépense · Opérateurs | +12,70 | +22,18 | +29,09 | +29,24 |
| A · dépense · Chèques | +4,21 | +11,48 | +17,22 | +19,90 |
| A · dépense · Entreprises | +5,42 | +11,83 | +15,20 | +15,20 |
| A · dépense · Associations | +5,02 | +9,53 | +11,83 | +12,60 |
| A · dépense · Charges | +3,80 | +3,80 | +3,80 | +3,80 |
| A · dépense · Départs État | +0,45 | +0,90 | +0,90 | +0,90 |
| A · dépense · Collectivités | +21,85 | +32,10 | +39,37 | +39,37 |
| A · restitution · salaire net | −33,39 | −114,48 | −114,48 | −114,48 |
| A · recette · niches — TVA | +4,97 | +9,94 | +9,94 | +9,94 |
| A · recette · niches — revenus | +8,32 | +16,70 | +19,42 | +19,42 |
| A · recette · niches — sociétés | +7,60 | +8,39 | +8,57 | +8,57 |
| A · recette · niches — énergie et autres | +3,25 | +5,20 | +5,20 | +5,20 |
| B · recette · niches — TVA | +4,97 | +9,94 | +9,94 | +9,94 |
| B · recette · niches — revenus | +2,23 | +5,61 | +6,84 | +6,84 |
| B · recette · niches — sociétés | +7,47 | +8,13 | +8,17 | +8,17 |
| B · recette · niches — énergie et autres | +2,24 | +4,19 | +4,19 | +4,19 |
| A · recette · niches — sociales | +4,50 | +9,00 | +9,00 | +9,00 |
| B · recette · niches — sociales | +4,50 | +9,00 | +9,00 | +9,00 |
| B · recette · TVA | +0,00 | +8,91 | +21,62 | +29,21 |
| B · perte de recette · taxe sur les salaires | +0,00 | −5,96 | −11,92 | −17,88 |
| B · perte de recette · impôts supprimés | −17,30 | −32,60 | −32,60 | −32,60 |
| A · dépense · chômage | +0,00 | +29,60 | +29,60 | +29,60 |
| A · épargne · chômage | +0,00 | −29,60 | −29,60 | −29,60 |
| A · épargne · patrimoine | +0,00 | −17,60 | −17,60 | −17,60 |
| A · épargne · épargne rendue | +0,00 | −75,27 | −55,05 | −58,66 |

---

## 3. Le détail, bloc par bloc

### 3.1 Les niches fiscales et sociales

**Montants** (*relevé*) : 43,126 Md€ de gage sur la CSG et 29,141 de solde rendu en taxes, somme des colonnes N et O de l'onglet `Chiffrages Résolution` de `Niches fiscales.xls`, 257 dépenses fiscales à montant non nul ; 9 + 9 Md€ de niches sociales (`Flux`!C13 et E13). 43,126 + 9 = 52,13, soit les 52,1 de l'`Annexe Manuscrit`.

**Dates** (*relevé*) : IV de l'amendement n° 1 de la liasse P1, sept régimes ; IV de l'amendement n° 1 de la liasse PLFSS, 1er juillet 2027. L'onglet `Echéances` du classeur des niches donne la fin du fait générateur et la fin d'incidence budgétaire **en droit actuel** ; il ne date pas la suppression, et il n'a servi qu'à cela.

**Par famille, part gagée sur la CSG, Md€** :

| famille | 2027 | 2028 | 2029 | 2030 | régime plein |
|---|---:|---:|---:|---:|---:|
| énergie et autres | 3,25 | 5,20 | 5,20 | 5,20 | 5,20 |
| revenus | 8,32 | 16,70 | 19,42 | 19,42 | 19,42 |
| sociétés | 7,60 | 8,39 | 8,57 | 8,57 | 8,57 |
| TVA | 4,97 | 9,94 | 9,94 | 9,94 | 9,94 |

| | 2027 | 2028 | 2029 | 2030 | régime plein |
|---|---:|---:|---:|---:|---:|
| sociales | 4,50 | 9,00 | 9,00 | 9,00 | 9,00 |
| **toutes niches, gage** | **28,64** | **49,23** | **52,12** | **52,13** | **52,13** |
| solde rendu en taxes (circuit B), fiscales | 16,91 | 27,87 | 29,13 | 29,14 | 29,14 |
| solde, sociales | 4,50 | 9,00 | 9,00 | 9,00 | 9,00 |

**Ce qui tombe quand** (gage, Md€ par an en régime plein) : au 1er juillet 2027, la TVA, les accises et les autres droits, 13,84 ; à l'automne 2027, l'impôt sur le revenu dû au titre de 2026, 8,31, dont l'abattement de 10 % sur les pensions, 4,80 ; sur l'exercice 2027, l'impôt sur les sociétés, 7,23, dont le crédit d'impôt recherche, 3,90 ; au 1er janvier 2028, l'épargne salariale et les livrets, 5,02 ; à l'automne 2028, les réductions et déductions de l'impôt sur le revenu, 3,11, et les dons ; à l'automne 2029, les demi-parts, 1,96.

**Qui paie** (gage fiscal, régime plein, *relevé* à l'onglet `Bénéficiaires`) : entreprises 21,68 ; ménages non répartis 11,85 ; ménages actifs 4,80 ; ménages sans revenus d'activité 4,80. Niches sociales : actifs 3,00, entreprises 6,00.

**Rattachement des 257 dépenses à leur date** : 116 par l'item du III qui abroge leur siège (23,53 Md€) ; 107 par l'impôt, quand le IV ne distingue pas (15,24) ; **34 par la nature de l'avantage, 4,36 Md€, *déduit*.** Le détail, dépense par dépense, est au fichier des niches.

**Trois réserves, chiffrées.**

1. **Impôt sur les sociétés : mesure et caisse.** 7,60 Md€ sont comptés en 2027, exercice où l'impôt naît. Ils sont encaissés au solde de mai 2028. En caisse, le surplus à rendre en janvier 2028 serait de 41,10 et non de 48,70 ; l'écart se referme en mai.
2. **Engagements antérieurs** (G du IV) : un avantage né d'un investissement ou d'une dépense d'avant 2027 court « jusqu'au terme ». Les lignes du B — 5,38 Md€ à l'impôt sur les sociétés, 3,11 à l'impôt sur le revenu — sont comptées en entier dès leur première année. **Aucune pièce ne chiffre le stock** : ce sont des majorants.
3. **Frontière des familles** : le classeur donne 19,78 à l'impôt sur le revenu et 8,21 à l'impôt sur les sociétés ; l'annexe, par catégorie, donne 19,42 et 8,57. Total identique, 43,13.

### 3.2 Les autres lignes du circuit de restitution

| ligne | 2027 | 2028 | 2029 | 2030 | date | pièce | statut |
|---|---:|---:|---:|---:|---|---|---|
| 27 coupes | 48,94 | 85,22 | 109,11 | 112,71 | § 4 | croisé du 20261116 | *relevé*, inchangé |
| 8 lignes de première partie et sociale | 4,52 | 6,60 | 8,30 | 8,30 | 1er janvier 2027 ; D21 par tiers dès le 1er juillet 2027 | `Détail Economies` F7 à F14, F21 ; PLFSS n° 1, IV | montants et rythmes *relevés* ; **date des sept premières *tranchée en propre*** (R-P) |
| baisse de CSG | −33,39 | −114,48 | −114,48 | −114,48 | juillet à décembre 2027 | registre § 2 | *relevé* |
| assurance chômage, allocataires | 0 | +29,60 | +29,60 | +29,60 | **1er janvier 2028, *posée*** | `Annexe Manuscrit`!F27 | montant *relevé* ; **date manquante** |
| assurance chômage, épargne des actifs | 0 | −29,60 | −29,60 | −29,60 | idem | idem | idem |
| rendement du patrimoine | 0 | −17,60 | −17,60 | −17,60 | 1er janvier 2028 | n° 27, III, C et VIII ; `Annexe Manuscrit`!F28 | date *relevée* ; montant du classeur |
| épargne rendue | 0 | −75,27 | −55,05 | −58,66 | 1er janvier 2028 | n° 27, III, B et VIII | *calculé* |

Les huit lignes redonnent 4,52 Md€ en 2027 contre 4,7 à la colonne D du classeur.

**L'assurance chômage se compense sur elle-même** par construction : ce que les allocataires perdent, les actifs le reçoivent en épargne, le même mois. Elle ne pèse pas sur le solde public ; elle pèse **29,60 Md€ par an sur les ménages sans revenus d'activité**, qui n'ont rien en face dans ce compte.

### 3.3 L'épargne rendue

**Règle** (*relevée*, `Input Capitalisation` E2 à E8, `Flux`!C6) : tout ce qui dépasse la baisse de CSG va au compte d'épargne. Première année au classeur : 129,46 = 114,46 + 15,00. Régime plein : 236,40 = 114,46 + 121,94.

**Surplus disponible** = coupes + huit lignes + niches gagées − baisse de CSG, hors chômage et patrimoine.

| | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|
| surplus de l'exercice | +48,70 | +26,57 | +55,05 | +58,66 |
| surplus cumulé, fin d'exercice | 48,70 | 75,27 | 130,32 | 188,98 |
| épargne rendue | 0,00 | 75,27 | 55,05 | 58,66 |

**Mois par mois** (surplus, cumul, épargne rendue, cumul après épargne) :

| mois | surplus | cumul | épargne rendue | cumul après épargne |
|---|---:|---:|---:|---:|
| 2027-01 | +3,70 | +3,70 | +0,00 | +3,70 |
| 2027-02 | +3,70 | +7,39 | +0,00 | +7,39 |
| 2027-03 | +3,70 | +11,09 | +0,00 | +11,09 |
| 2027-04 | +3,91 | +15,00 | +0,00 | +15,00 |
| 2027-05 | +3,91 | +18,91 | +0,00 | +18,91 |
| 2027-06 | +3,91 | +22,81 | +0,00 | +22,81 |
| 2027-07 | +6,75 | +29,56 | +0,00 | +29,56 |
| 2027-08 | +5,16 | +34,72 | +0,00 | +34,72 |
| 2027-09 | +5,88 | +40,60 | +0,00 | +40,60 |
| 2027-10 | +4,29 | +44,89 | +0,00 | +44,89 |
| 2027-11 | +2,70 | +47,59 | +0,00 | +47,59 |
| 2027-12 | +1,11 | +48,70 | +0,00 | +48,70 |
| 2028-01 | +1,44 | +50,15 | +50,15 | +0,00 |
| 2028-02 | +1,44 | +51,59 | +1,44 | +0,00 |
| 2028-03 | +1,44 | +53,03 | +1,44 | +0,00 |
| 2028-04 | +1,44 | +54,47 | +1,44 | +0,00 |
| 2028-05 | +1,44 | +55,91 | +1,44 | +0,00 |
| 2028-06 | +1,44 | +57,35 | +1,44 | +0,00 |
| 2028-07 | +2,43 | +59,78 | +2,43 | +0,00 |
| 2028-08 | +2,43 | +62,20 | +2,43 | +0,00 |
| 2028-09 | +3,27 | +65,47 | +3,27 | +0,00 |
| 2028-10 | +3,27 | +68,74 | +3,27 | +0,00 |
| 2028-11 | +3,27 | +72,01 | +3,27 | +0,00 |
| 2028-12 | +3,27 | +75,27 | +3,27 | +0,00 |
| 2029-01 | +4,12 | +79,40 | +4,12 | +0,00 |
| 2029-02 | +4,12 | +83,52 | +4,12 | +0,00 |
| 2029-03 | +4,12 | +87,65 | +4,12 | −0,00 |
| 2029-04 | +4,12 | +91,77 | +4,12 | −0,00 |
| 2029-05 | +4,12 | +95,89 | +4,12 | −0,00 |
| 2029-06 | +4,12 | +100,02 | +4,12 | −0,00 |
| 2029-07 | +4,72 | +104,74 | +4,72 | −0,00 |
| 2029-08 | +4,72 | +109,47 | +4,72 | −0,00 |
| 2029-09 | +5,21 | +114,68 | +5,21 | −0,00 |
| 2029-10 | +5,21 | +119,89 | +5,21 | −0,00 |
| 2029-11 | +5,21 | +125,11 | +5,21 | −0,00 |
| 2029-12 | +5,21 | +130,32 | +5,21 | −0,00 |
| 2030-01 | +4,89 | +135,21 | +4,89 | −0,00 |
| 2030-02 | +4,89 | +140,10 | +4,89 | −0,00 |
| 2030-03 | +4,89 | +144,99 | +4,89 | −0,00 |
| 2030-04 | +4,89 | +149,87 | +4,89 | −0,00 |
| 2030-05 | +4,89 | +154,76 | +4,89 | −0,00 |
| 2030-06 | +4,89 | +159,65 | +4,89 | −0,00 |
| 2030-07 | +4,89 | +164,54 | +4,89 | −0,00 |
| 2030-08 | +4,89 | +169,43 | +4,89 | −0,00 |
| 2030-09 | +4,89 | +174,31 | +4,89 | −0,00 |
| 2030-10 | +4,89 | +179,20 | +4,89 | −0,00 |
| 2030-11 | +4,89 | +184,09 | +4,89 | −0,00 |
| 2030-12 | +4,89 | +188,98 | +4,89 | −0,00 |


**À partir de quand.** Le surplus est positif chaque mois des quarante-huit : le cumul ne redescend jamais. **Tout le surplus peut donc être rendu dès que le compte existe, le 1er janvier 2028**, et le cumul public du circuit reste à zéro, jamais dessous : 50,15 Md€ en janvier 2028 — les 48,70 de 2027 et le surplus du mois —, puis le surplus de chaque mois.

**À quelles conditions.**

1. **Le compte d'épargne ouvre le 1er janvier 2028 et les premiers versements sont dus au titre de 2028** (amendement n° 27, VIII). Rien ne peut être rendu en 2027.
2. **Le taux du versement de restitution est fixé chaque année par la loi de finances ; à défaut, il est nul** (n° 27, III, B). Rendre en 2028 le surplus de 2027 suppose que la loi de finances pour 2028 fixe un taux qui le couvre. Le compte donne **75,27 Md€ au titre de 2028**, soit 66 % de la baisse de CSG d'une année.
3. **Les niches rapportent à leur date** (§ 3.1). Sans les 7,60 Md€ d'impôt sur les sociétés encaissés en mai 2028, le versement de janvier 2028 se limite à 41,10 Md€.
4. **Le versement suit le surplus constaté, non le surplus prévu.** Le premier semestre 2028 ne dégage que 1,44 Md€ par mois.

**Contre le classeur**, une cause par écart :

| | classeur | ce compte | écart | cause |
|---|---:|---:|---:|---|
| épargne de la première année pleine de CSG | 15,00 | 26,57 (surplus de 2028) | +11,57 | les coupes de 2028 sont la deuxième année des sorties en trois ans : 91,82 avec les huit lignes, contre 77,36 d'année 1 au classeur (+14,46) ; les niches de 2028 font 49,23 contre 52,1 (−2,87) |
| surplus de 2027, que le classeur ne compte pas | — | 48,70 | +48,70 | la baisse de CSG ne coûte que 33,39 en 2027, étalée de juillet à décembre |
| surplus en régime plein | 74,74 | 58,66 (2030) | −16,08 | les départs d'agents restent à 30 % sur la fenêtre : 16,00 « à terme » |

### 3.4 La refonte — ce que le registre date, et ce qui manque

Le classeur ferme la refonte par construction (`Refonte fiscalité`, ligne 13, *relevé*) : solde des niches 29,2 + gisement 40,1 − taxes supprimées 137,05 = −67,75, compensé par 67,75 de hausses d'équilibre — 25,69 d'impôt sur les sociétés au taux unique (K34), 42,06 de taxe foncière unique (K37). Le solde des niches sociales, 9, va à l'aide fondamentale (C64).

| ligne | 2027 | 2028 | 2029 | 2030 | régime plein au classeur | pièce | état |
|---|---:|---:|---:|---:|---:|---|---|
| solde des niches fiscales | +16,91 | +27,87 | +29,13 | +29,14 | 29,2 | n° 1, IV | daté ici |
| solde des niches sociales | +4,50 | +9,00 | +9,00 | +9,00 | 9 (aide fondamentale) | PLFSS n° 1, IV | daté ici |
| taux réduits de TVA | 0 | +8,91 | +21,62 | +29,21 | 33 (2031) | n° 21, IV ; § 17 | *relevé* |
| taxe sur les salaires | 0 | −5,96 | −11,92 | −17,88 | dans les −137,05 | PLFSS n° 3 ; § 17 | *relevé* |
| suppressions du tri | −12,10 | −32,60 | −32,60 | −32,60 | dans les −137,05 | § 18 | *relevé*, minorant : 26 rangs non chiffrés |
| contribution exceptionnelle | −5,20 | 0 | 0 | 0 | — | n° 35 ; § 18 | montant *relevé*, mois *posés* |
| **lignes datées** | **+4,11** | **+7,22** | **+15,24** | **+16,87** | | | |
| impôt sur les sociétés au taux unique | ? | ? | ? | ? | +25,69 | n° 23, IV : exercices ouverts à compter du 1er juillet 2027 | **produit par an non chiffré** |
| taxe foncière unique | 0 | ? | ? | ? | +42,06 | n° 29, V : impositions de 2028 | **produit par an non chiffré** |
| autres impôts supprimés | ? | ? | ? | ? | −86,57 | n° 19, 22, 25, 29 | **ni datés ni chiffrés au registre** |
| autres gisements | ? | ? | ? | ? | +7,10 | `Refonte fiscalité`!G13 − G15 | idem |

**La refonte ne se ferme sur aucun des quatre exercices avec les seules lignes du registre** : elle est excédentaire de 4,11 à 16,87 Md€, parce que les recettes sont datées et qu'une part des suppressions ne l'est pas. En régime plein, les lignes datées donnent +20,66 (TVA à 33) ; les lignes manquantes, −11,72 ; le reste, +8,94, est le solde des niches sociales affecté à l'aide fondamentale, qui est un troisième circuit, absent du registre et de ce compte.

### 3.5 Les leviers de date du registre, rejoués

Le registre (§ 5 et § 17) chiffrait quatre leviers contre un besoin de 2028 de 11,45 Md€ (14,41 avant TVA et taxe sur les salaires ; 29,24 depuis la mise à niveau du 16 novembre).

| levier | 2027 | 2028 | 2029 | 2030 | circuit | au registre, 2028 |
|---|---:|---:|---:|---:|---|---:|
| première marche de TVA au 1er janvier 2028 | 0 | +8,91 | 0 | 0 | refonte | +8,91 |
| taxe sur les salaires décalée d'un an | 0 | +5,96 | +5,96 | +5,96 | refonte | +5,96 |
| sorties en trois ans ramenées à deux, État hors aide au logement | +4,30 | +8,49 | +0,92 | 0 | restitution | +8,49 |
| sorties en trois ans ramenées à deux, collectivités | +3,63 | +7,27 | 0 | 0 | restitution | +7,30 |

*Rejoué* : les quatre effets de 2028 concordent avec le registre, à 0,03 près sur le dernier (D41 à 12,21 depuis le 16 novembre).

**Ce qu'il en reste.** Sur le compte complet, le circuit de restitution dégage +26,57 Md€ en 2028 sans aucun levier. **Les deux leviers de rythme ne servent plus à fermer 2028** : ils ajouteraient 15,76 Md€ à l'épargne rendue de 2028 et 7,93 à celle de 2027, au prix d'une sortie plus rapide pour les entreprises et les collectivités. **Les deux leviers de la refonte ne se jugent pas ici** : la refonte n'est pas datée en entier, et ses lignes datées sont déjà excédentaires. **Le seul point de calendrier qui demeure** est le premier semestre 2028, +1,44 Md€ par mois : un retard de 1,44 Md€ par mois sur les niches ou les coupes le rend négatif, et un levier de rythme sur l'État (+0,71 par mois en moyenne sur 2028) ou sur les collectivités (+0,61) élargit la marge de moitié.

---

## 4. Relevé, hérité, déduit, posé

| statut | quoi |
|---|---|
| ***relevé* dans ce fil** | les 33 paramètres des classeurs du site, téléchargés le 20261117 (`Synthèse des chiffrages.xlsx`, SHA-256 `ac56012f…e64e84a`, celui que le pilotage a lu ; `Niches fiscales.xls`, SHA-256 `6d89483a…fd22fb29`, identique à `sources/projet_20261116/14_…xls`, que l'outil lit) ; le III et le IV de l'amendement n° 1 de la liasse P1 ; les amendements n° 21, 23, 27, 29 et 35 ; les amendements n° 1, 3 et 9 du PLFSS ; les § 1 à 7 et 15 à 18 du registre ; les onglets `Chiffrages Résolution`, `Bénéficiaires`, `Références juridiques`, `Echéances` du classeur des niches |
| ***hérité*, non rejoué** | le croisé du 20261116 et sa clé d'agents ; le produit de la taxe sur les salaires (§ 17) ; les rendements du § 18 ; la part de l'alimentation dans la TVA (§ 17) |
| ***déduit*** | le mois d'incidence de chaque niche, d'après le mode de perception de l'impôt ; le rattachement de 34 dépenses fiscales par la nature de l'avantage ; l'épargne rendue |
| ***posé*, faute de pièce** | la date de l'assurance chômage ; la mensualisation de la contribution exceptionnelle ; la clé d'agents des huit lignes de première partie ; la moitié-moitié des « locaux » et « parcelles » ; la taxe sur les salaires et les suppressions du tri portées aux entreprises |
| ***tranché en propre*, révocable** | la date du 1er janvier 2027 pour D7 à D14 ; la séparation en deux circuits ; l'agent « Ménages, non répartis » ; l'agent « Ménages actifs — épargne » ; le montant du patrimoine au classeur (17,60) et non au simulateur (18,2) |

**Non ouvert** : les amendements n° 2 à 18 de la liasse P1, qui portent des niches que le n° 1 emporte aussi — leurs dates propres ne sont pas confrontées à celles du IV ; les amendements n° 19, 20, 22, 24, 25, 28 et 30 à 34, hors de leur clause d'entrée en vigueur ; `LIASSE_PLF_P2.md` ; la liste des 24 dispositions sociales abrogées par le PLFSS n° 1.

## 5. Dates et montants qui manquent

1. **Assurance chômage transformée** : aucune disposition de la liasse, aucune date. 29,6 Md€ au classeur, 30,0 par la note de l'auteure.
2. **Versement de patrimoine** : le montant global est renvoyé à la loi de finances de chaque année ; trois valeurs coexistent, 17,60 (classeur), 18,2 (simulateur), 3 % de 600 Md€ (livre). **La contrepartie publique n'est écrite nulle part.**
3. **Taux du versement de restitution** : renvoyé à la loi de finances ; nul à défaut.
4. **Lignes D7 à D14** : le registre les déclare « de première partie » sans les dater.
5. **Départs d'agents** : le passage de 30 % au plein n'est fixé par aucune pièce (registre § 5) ; 16,00 Md€ par an hors fenêtre.
6. **Produit par an du taux unique de l'impôt sur les sociétés et de la taxe foncière unique** : non chiffré.
7. **Impôts supprimés hors § 18** : 86,57 Md€ en régime plein, ni datés ni chiffrés au registre ; 26 rangs du § 18 sans rendement.
8. **Stock d'engagements antérieurs** préservé par le G du IV : non chiffré.
9. **Répartition des ménages** entre actifs et sans revenus d'activité, pour les niches, la TVA et le patrimoine : aucune clé. La ligne « Ménages, non répartis » la porte : −3,41 · +0,06 · −10,10 · −13,91.
10. **Part des employeurs publics dans la taxe sur les salaires** : non isolée ; elle est interne à la sphère publique et ne devrait pas figurer chez les entreprises.
11. **Aide fondamentale** (P1 n° 28, PLFSS n° 7, 1er janvier 2028) : troisième circuit, absent du registre et du compte.
12. **Caisse** : le compte est en mesure. Le § 15 du registre pose 4,7 Md€ de marge sur la part État de 2027 ; elle n'est pas rejouée et viendrait en déduction du surplus de 2027.

## 6. Ce que le fil n'a pas touché

`methode/arbitrages.md`, `methode/journal.md`, `appareil/generer_index.py`, `methode/index.json`, les liasses, `PILOTAGE.md`, le registre de calcul et le croisé du 20261116. **Les quatre fichiers neufs de `referentiels/`, le module d'`appareil/` et cet état ne sont pas déclarés à l'index.** Le § 6 du registre dit encore que le compte « ne porte ni les niches ni l'épargne rendue » : la phrase est à mettre à jour par le fil qui tient le registre. `PILOTAGE.md`, chantier 5 : à mettre à jour par le pilotage. Aucun sas ouvert : tout est sur la branche.

## 7. Entrées de registre — titrées, datées, sans numéro

### Compte complet du calendrier des flux : construit, deux circuits — 20261117

*Exécuté.* `referentiels/calendrier_compte_complet_20261117.tsv`, 105 mesures, 118 lignes mesure × agent, 48 mois ; `appareil/calendrier_compte_complet.py`, 39 contrôles à 0 échec ; le croisé du 20261116 est inchangé. *Tranché en propre, révocable* : le compte se lit en deux circuits — la restitution (coupes, huit lignes de première partie, niches gagées, baisse de CSG, chômage, patrimoine, épargne rendue), complète ; la refonte, pour les seules lignes que le registre date (§ 17 et § 18). *Relevé* : solde public tous circuits de +52,81 · −59,08 · −2,37 · −0,73 Md€, cumul −9,37 fin 2030.

### Niches : 28,64 Md€ en 2027, 49,23 en 2028, 52,12 en 2029 — 20261117

*Relevé* au IV de l'amendement n° 1 de la liasse P1 et au IV de l'amendement n° 1 du PLFSS, dépense par dépense (257 dépenses, 43,126 Md€ de gage ; niches sociales 9 Md€). Le classeur compte 52,1 Md€ dès la première année. Écart de 2027, −23,46 Md€ : la TVA, les accises et les niches sociales ne courent que du 1er juillet ; l'épargne, les parts et les réductions de l'impôt sur le revenu tombent en 2028 et 2029. *Déduit* : le mois d'incidence, d'après le mode de perception ; 34 dépenses (4,36 Md€) rattachées par la nature de l'avantage. *Réserves* : 7,60 Md€ d'impôt sur les sociétés comptés en 2027 et encaissés en mai 2028 ; 8,50 Md€ par an majorants tant que les engagements antérieurs courent (G du IV).

### Le point dur de 2028 disparaît du circuit de restitution, en mesure — 20261117

*Relevé au compte.* Surplus du circuit de restitution, hors chômage et patrimoine : +48,70 · +26,57 · +55,05 · +58,66 Md€ ; positif chaque mois, au plus bas +1,11 en décembre 2027 et +1,44 par mois au premier semestre 2028. Le −29,24 du § 5 ne comptait que les coupes. Les leviers de rythme du § 17 (+8,49 et +7,27 en 2028, *rejoués*) ne servent plus à fermer 2028 ; ceux de la refonte ne se jugent pas tant qu'elle n'est pas datée en entier.

### Épargne rendue : rien en 2027, 75,27 Md€ au titre de 2028 — 20261117

*Calculé*, sur la règle du classeur (tout ce qui dépasse la baisse de CSG). *Relevé* : le compte d'épargne ouvre le 1er janvier 2028, les premiers versements sont dus au titre de 2028, le taux est fixé par la loi de finances et nul à défaut (liasse P1, amendement n° 27, III et VIII). Le surplus de 2027, 48,70 Md€, reste donc douze mois dans la sphère publique : c'est le seul écart du circuit, et il se referme en janvier 2028. Épargne rendue : 75,27 · 55,05 · 58,66 Md€ de 2028 à 2030. Contre le classeur : 15,00 la première année, 74,74 en régime plein ; les écarts tiennent au rythme des sorties en trois ans, au calendrier des niches et aux départs d'agents à 30 %.

### Rendement du patrimoine : 17,60 Md€ par an sans contrepartie de flux — 20261117

**Constaté, à l'auteure.** Le versement de patrimoine (amendement n° 27, III, C) est rendu aux personnes à compter de 2028. Aucune pièce ne dit ce que la sphère publique cesse de percevoir ou se met à payer. Par la règle « le solde public est l'inverse de la somme des privés », il creuse le solde de 17,60 Md€ par an : c'est le seul écart durable du circuit de restitution.

### Assurance chômage : aucune disposition, aucune date — 20261117

**Constaté.** Les 29,6 Md€ du classeur ne sont portés par aucun amendement des trois liasses. *Posé* pour le compte : 1er janvier 2028, jour du compte d'épargne. La ligne se compense sur elle-même ; elle pèse 29,60 Md€ par an sur les ménages sans revenus d'activité.

### Huit lignes de première partie et sociale : datées pour le compte — 20261117

*Tranché en propre, révocable* : D7, D8, D9, D10, D11, D13 et D14 au 1er janvier 2027 (R-P), au rythme de la colonne G du classeur ; D21 par tiers au 1er juillet 2027, 1er janvier 2028 et 1er janvier 2029 (*relevé*, PLFSS n° 1, IV). 4,52 · 6,60 · 8,30 · 8,30 Md€. Le registre § 4 ne les date pas.

### Refonte : le registre n'en date qu'une partie — 20261117

**Constaté.** Lignes datées (solde des niches, TVA, taxe sur les salaires, suppressions du tri) : +4,11 · +7,22 · +15,24 · +16,87 Md€. Manquent, en régime plein au classeur : +25,69 d'impôt sur les sociétés au taux unique, +42,06 de taxe foncière unique, −86,57 d'impôts supprimés, +7,10 de gisements. La refonte ne se ferme sur aucun exercice tant que ces lignes n'ont ni date ni produit annuel.
