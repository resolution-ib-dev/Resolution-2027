# Pilotage — tableau de bord unique

**Tenu par le fil de pilotage** (`session_01VynsZnrEusr42WSGSHbdEg`). L'auteur ne parle qu'à ce
fil ; les fils d'exécution lui rendent compte et ne posent pas de question à l'auteur. Ce
tableau se met à jour à chaque fusion et à chaque point. *Relevé le 20261116.*

## Chantiers

| n° | chantier | état | où | fil porteur | prochaine étape |
|---|---|---|---|---|---|
| 1 | Classeurs du site (8) | à jour, cohérents | `Site-ETNP/site/donnees/` | pilotage | copier outils et documentation au dépôt public |
| 2 | Simulateur | en ligne, non lié ; retouché le 20261116 (patrimoine à 18 Md€, chômage redit, niches par sujet), à valider par l'auteur ; 1 bloc revu sur 6 | `Site-ETNP/site/reprenez.html` | pilotage | validation, puis revue Agences, Agents, Associations, « En échange » |
| 3 | Liasses du budget 2027 | **sur mesure et en ligne le 20261117** : seconde partie à 40 amendements (24,3 Md€ d'AE, 21,0 Md€ de CP de crédits retirés), première partie et sécurité sociale alignées sur le tri unique ; 84 amendements au site | `livrables/depot_2027/` ; `methode/etats/LIASSES_par_mesure_20261117.md` ; `Site-ETNP/site/amendements/` | pilotage | 25 impôts supprimés sans amendement porteur (5,0 Md€) ; jeux et électricité à compléter ; programme 379 |
| 4 | Tri des impôts | **tri unique rendu le 20261116** : 434 rangs, six devenirs, classeur `Tri des impôts.xlsx` ; contrôles à 0 échec ; 34 rangs supprimés sans amendement porteur (11,4 Md€) | `referentiels/sort_prelevements_20261116.tsv` ; `methode/etats/TRI_unique_20261116.md` | pilotage | relecture de l'auteur, puis classeur sur le site ; reprise des amendements P1 n° 22 et PLFSS n° 9 |
| 5 | Calendrier de mise en œuvre (interne, pas de page sur le site) | compte complet rendu le 20261117 ; à tenir en trois comptes séparés (auteur, 20261117) : circuit de restitution, patrimoine rendu hors flux, refonte fiscale à ses dates | `referentiels/calendrier_compte_complet_20261117.tsv` ; `methode/etats/COMPTE_complet_20261117.md` | pilotage | séparer les trois comptes ; dater la refonte depuis les liasses |
| 6 | Présentation candidat | récupérée et alignée sur le simulateur le 20261116 : 600 € pour 2 400 € nets | `livrables/presentation_candidat/` | pilotage | relire les autres chiffres contre les classeurs du site |
| 7 | Doctrine et dérivés | référentiel à 236,402 ; 101 dérivés non régénérés | `referentiels/REF_doctrine.json` | en attente | régénération quand le manuscrit est au conteneur |
| 8 | Rangement du dépôt public | 27 083 fichiers de révision pénale sur 28 000 ; 91 états, 24 mandats | `chantier/` | après 3 et 4 | page d'entrée, archivage des états périmés |
| 9 | Contrôles automatiques | aucun sur le site ; un flux `rafraichir` ici | `.github/workflows/` | après 3 | contrôles à chaque pull request |

## Décisions rendues — à relire avant toute question

**Une question déjà tranchée ne se repose jamais : elle s'applique** (règle du 20261117, après cinq questions reposées à tort).

| sujet | décision de l'auteur | date |
|---|---|---|
| Ce qui fait foi | les classeurs du site, pour montants et taux ; le travail par mesure et par mois (registre de calcul), pour dates et rythmes | 20261116 |
| Liasses | sur mesure, chaque amendement colle à sa mesure ; le site ne porte que les liasses | 20261117 |
| Dates d'effet | personnes physiques au 1er juillet 2027, personnes morales au 1er janvier ; la raison se dit dans l'exposé | octobre, redit le 20261116 |
| Chèque énergie | droit éteint au 1er janvier 2027 ; 300 M€ en 2027 (restes à payer de la campagne précédente) | 20261116 |
| Départs d'agents | en entier dans les 236 ; 30 % en salaire net la première année | 20261116 |
| Fonctionnement des ministères | 85 % hors entretien des routes nationales | 20261116 |
| Programme 379 (fonds européens, hôpitaux) | gardé, qualifié par sa dépense finale | 20261117 |
| Jeux | toutes les taxes supprimées | 20261116, redit le 20261117 |
| Électricité | plancher européen | redit le 20261117 |
| Impôts sans amendement porteur | abrogés selon les mêmes règles que les autres | 20261117 |
| Tri des impôts | base du 3 novembre, corrections du 20 octobre reportées ; le tableau de refonte fait foi pour l'énergie et les assurances | 20261116 |
| Calendrier | interne ; trois comptes séparés : restitution, patrimoine rendu, refonte fiscale | 20261117 |
| Flux par agent | agents tous privés, agents publics compris ; solde public = opposé de la somme des privés ; coupes d'agences et de collectivités réparties sur des privés | 20261116-17 |
| Présentation candidat | hors du site ; alignée sur 600 € pour 2 400 € nets | 20261116-17 |
| Population du simulateur (capital par personne) | inchangée pour l'instant, à reprendre plus tard | 20261118 |
| Devenir de chaque ligne | « Conservé. » et « Arrêté. » au second rang de l'explication, après le contenu ; « Prudence » écarté | 20261118 |
| Simulateur, lecture | trois strates ; « qui : quoi », dépense finale lue à l'action ; « administration » pour le ministère lui-même ; « Autres » en fin de liste ; ordre échelons, agences, ministères, agents ; agents liés aux structures | 20261117 |
| Simulateur, montants | patrimoine à 3 %, 18 Md€, à part du compte de flux ; 600 € à 2 400 € nets ; chômage en deux lignes ; niches par sujet | 20261116-17 |
| Agriculture | « administration, guichets d'aides » | 20261117 |
| Agents communaux du logement | en ligne libre | 20261117 |

## Décisions attendues de l'auteur

| n° | question | piste du pilotage |
|---|---|---|
| — | aucune | — |

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
