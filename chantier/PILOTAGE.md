# Pilotage — tableau de bord unique

**Tenu par le fil de pilotage** (`session_01VynsZnrEusr42WSGSHbdEg`). L'auteur ne parle qu'à ce
fil ; les fils d'exécution lui rendent compte et ne posent pas de question à l'auteur. Ce
tableau se met à jour à chaque fusion et à chaque point. *Relevé le 20261116.*

## Chantiers

| n° | chantier | état | où | fil porteur | prochaine étape |
|---|---|---|---|---|---|
| 1 | Classeurs du site (8) | à jour, cohérents | `Site-ETNP/site/donnees/` | pilotage | copier outils et documentation au dépôt public |
| 2 | Simulateur | en ligne, non lié ; 1 bloc revu sur 6 ; **en pause** jusqu'à la fin de la consolidation (auteur, 20261116) | `Site-ETNP/site/reprenez.html` | pilotage | revue Agences, puis Agents, Associations, niches, patrimoine, « En échange » |
| 3 | Liasse de crédits, PLF 2de partie | écarts mesurés le 20261116 : 43,7 Md€ d'AE inscrits, 26,5 selon les classeurs en année pleine, 16,1 avec les dates du registre ; 6,7 Md€ sans paramètre | `methode/etats/ECARTS_liasse_classeurs_20261116.md` ; `referentiels/parametres_credits_20261116.tsv` ; `appareil/controle_liasse_classeurs.py` | à relancer après L1 à L6 | régénération des 22 amendements |
| 4 | Tri des impôts | **tri unique rendu le 20261116** : 434 rangs, six devenirs, classeur `Tri des impôts.xlsx` ; contrôles à 0 échec ; 34 rangs supprimés sans amendement porteur (11,4 Md€) | `referentiels/sort_prelevements_20261116.tsv` ; `methode/etats/TRI_unique_20261116.md` | pilotage | relecture de l'auteur, puis classeur sur le site ; reprise des amendements P1 n° 22 et PLFSS n° 9 |
| 5 | Calendrier de mise en œuvre | état des lieux du projet versé (`methode/passation_calendrier_20261116.md`, `sources/projet_20261116/`) ; tableau mesure × mois d'origine introuvable, reconstruction en cours ; registre de calcul à remettre à niveau sur D16, D37, D41, D43 | `methode/etats/SERIES_classeurs_projet_site_20261116.md` | `session_01VynsZoLRKKjX26FzRNV2Rn`, branche `claude/liasse-regeneration` | croisé mesure × mois, puis page sur le site |
| 6 | Présentation candidat | récupérée et alignée sur le simulateur le 20261116 : 600 € pour 2 400 € nets | `livrables/presentation_candidat/` | pilotage | relire les autres chiffres contre les classeurs du site |
| 7 | Doctrine et dérivés | référentiel à 236,402 ; 101 dérivés non régénérés | `referentiels/REF_doctrine.json` | en attente | régénération quand le manuscrit est au conteneur |
| 8 | Rangement du dépôt public | 27 083 fichiers de révision pénale sur 28 000 ; 91 états, 24 mandats | `chantier/` | après 3 et 4 | page d'entrée, archivage des états périmés |
| 9 | Contrôles automatiques | aucun sur le site ; un flux `rafraichir` ici | `.github/workflows/` | après 3 | contrôles à chaque pull request |

## Décisions attendues de l'auteur

Présentées en clair dans la conversation le 20261116. Énoncé complet et effet de chaque réponse aux deux documents d'état.

| n° | question | piste du pilotage |
|---|---|---|
| J1 | Jeux supprimés (auteur, 20261116) : le tableau « Refonte fiscalité » n'en supprime que 0,3 Md€ ; l'aligner porte la taxe foncière d'équilibre de 42,1 à 48,5 Md€ | aligner le tableau |
| L1 | Liasse : année pleine du classeur, part de 2027 après la date d'effet, ou brut × part d'année | part de 2027 au taux et au rythme du classeur |
| L2 | Dates : celles du registre, ligne par ligne, ou celles de l'outil | registre |
| L3 | Fonctionnement courant : 1er janvier ou 1er juillet | 1er janvier |
| L4 | Transferts aux collectivités (5,43 Md€) : en entier, par tiers, ou hors liasse | par tiers |
| L5 | Emploi à domicile, Anah, missions locales, France Travail : dans la liasse de crédits ou non | oui, au taux et au rythme du classeur |
| L6 | Un amendement par mission ou par ligne | par mission |
| D4 | Rendement du patrimoine : 3,2 % (simulateur), 3 % (livre) ou 2,9 % (classeur) | — |
| D5 | Activer « Automatically delete head branches » sur `Site-ETNP` (réglage GitHub) | oui |

## Constats à traiter par le pilotage, sans question

- `SynthèseR!F32` du classeur des dépenses : 215,7 M€ comptés deux fois dans « Autres ménages ».
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
