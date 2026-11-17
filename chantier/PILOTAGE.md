# Pilotage — tableau de bord unique

**Tenu par le fil de pilotage** (`session_01VynsZnrEusr42WSGSHbdEg`). L'auteur ne parle qu'à ce
fil ; les fils d'exécution lui rendent compte et ne posent pas de question à l'auteur. Ce
tableau se met à jour à chaque fusion et à chaque point. *Relevé le 20261116.*

## Chantiers

| n° | chantier | état | où | fil porteur | prochaine étape |
|---|---|---|---|---|---|
| 1 | Classeurs du site (8) | à jour, cohérents | `Site-ETNP/site/donnees/` | pilotage | copier outils et documentation au dépôt public |
| 2 | Simulateur | en ligne, non lié ; retouché le 20261116 (patrimoine à 18 Md€, chômage redit, niches par sujet), à valider par l'auteur ; 1 bloc revu sur 6 | `Site-ETNP/site/reprenez.html` | pilotage | validation, puis revue Agences, Agents, Associations, « En échange » |
| 3 | Liasse de crédits, PLF 2de partie | **régénérée et en ligne le 20261116** : 19,8 Md€ d'AE et 17,6 Md€ de CP ; exposés avec la règle de date ; chèque énergie au 1er janvier ; 68 pages | `livrables/depot_2027/LIASSE_PLF_P2.md` ; `Site-ETNP/site/amendements/` | pilotage | second passage : amendement « Outre-mer », dix lignes « en 3 ans », catégorie 22 |
| 4 | Tri des impôts | **tri unique rendu le 20261116** : 434 rangs, six devenirs, classeur `Tri des impôts.xlsx` ; contrôles à 0 échec ; 34 rangs supprimés sans amendement porteur (11,4 Md€) | `referentiels/sort_prelevements_20261116.tsv` ; `methode/etats/TRI_unique_20261116.md` | pilotage | relecture de l'auteur, puis classeur sur le site ; reprise des amendements P1 n° 22 et PLFSS n° 9 |
| 5 | Calendrier de mise en œuvre | **croisé mesure × mois reconstruit** (27 lignes, 48 mois), il fait foi ; registre de calcul à niveau sur D16, D37, D38, D41, D43 ; § 6, 15, 16, 17 et classeur de flux non rejoués | `referentiels/calendrier_mesures_mois_20261116.tsv` ; `appareil/calendrier_mesures_mois.py` | pilotage | rejouer les projections, puis page sur le site |
| 6 | Présentation candidat | récupérée et alignée sur le simulateur le 20261116 : 600 € pour 2 400 € nets | `livrables/presentation_candidat/` | pilotage | relire les autres chiffres contre les classeurs du site |
| 7 | Doctrine et dérivés | référentiel à 236,402 ; 101 dérivés non régénérés | `referentiels/REF_doctrine.json` | en attente | régénération quand le manuscrit est au conteneur |
| 8 | Rangement du dépôt public | 27 083 fichiers de révision pénale sur 28 000 ; 91 états, 24 mandats | `chantier/` | après 3 et 4 | page d'entrée, archivage des états périmés |
| 9 | Contrôles automatiques | aucun sur le site ; un flux `rafraichir` ici | `.github/workflows/` | après 3 | contrôles à chaque pull request |

## Décisions attendues de l'auteur

Présentées en clair dans la conversation le 20261116. Énoncé complet et effet de chaque réponse aux deux documents d'état.

| n° | question | piste du pilotage |
|---|---|---|
| J1 | Jeux supprimés (auteur, 20261116) : le tableau « Refonte fiscalité » n'en supprime que 0,3 Md€ ; l'aligner porte la taxe foncière d'équilibre de 42,1 à 48,5 Md€ | aligner le tableau |
| S1 | Simulateur : patrimoine à 3 % entre 63,4 millions de personnes (18 Md€, 600 € à 2 400 €) | oui |
| D5 | Activer « Automatically delete head branches » sur `Site-ETNP` (réglage GitHub) | oui |

## Constats à traiter par le pilotage, sans question

- Départs d'agents : 30 % tant que l'indemnité court (une à sept années selon l'ancienneté, amendement n° 26), la ligne entière à terme, dans les 236 (auteur, 20261116). Le flux mensuel par agent (§ 6) est rejoué ; restent à rejouer les § 15, 16, 17 et le classeur de flux.

- 59 lignes arrêtées par le classeur et absentes de la liasse, dont France 2030 et l'audiovisuel public.
- Le § 4 du registre de calcul garde 20 % de socle sur le fonctionnement ; la décision du 16 novembre est 85 % hors entretien des routes.
- Les amendements n° 33 et 34 datent l'hébergement et le chèque énergie du 1er janvier, contre le registre.
- Tri : 13 qualifications menues (201 M€) à trancher par le fil qui reprend le tri ; quatre échanges de l'auteur du 20 octobre à verser au registre à leur date.

## Branches à traiter

`Resolution-2027` : `clever-euler-rbeck4` (tri du 20 octobre, récupéré : à supprimer), `tri-impots-recuperation` et `liasse-parametres` (fusionnées le 20261116),
`funny-faraday-260skj` (présentation candidat, récupérée : à supprimer), `retrait-liasses-20261012` (13 fichiers anciens),
`bold-fermi-spo7c6` (rien d'absent), `beautiful-curie-xzsshi` (un lot pénal).
`Site-ETNP` : `clever-euler-rbeck4` (classeur du tri, brouillon), `bold-fermi-spo7c6` (compteur
des lettres), quatre branches de septembre et d'octobre sans ancêtre commun.

## Règles de marche

- Un fil d'exécution par chantier, sur sa branche ; un seul à la fois touche `methode/` et
  `appareil/`. Le pilotage les lance, lit leurs transcriptions, contrôle et fusionne.
- Les classeurs de `Site-ETNP/site/donnees/` font foi. Tout ce qu'un outil lit est dans un dépôt.
- Une décision de l'auteur se demande ici, en question fermée, et s'inscrit au registre le jour même.
