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
| 4 | Tri des impôts | version du 20 octobre récupérée à `archive/tri_20261020/` ; celle du 3 novembre ne descend pas d'elle : 26 rangs de sort différent, 27 Md€ | `methode/etats/COMPARAISON_tri_20261020_20261103.md` | à relancer après T1 à T6 | tri unique, puis classeur sur le site |
| 5 | Calendrier de mise en œuvre | les quatre documents concordent (`registre_calcul_etatB.md` § 4, 27 lignes) ; seul l'outil de la liasse s'en écarte, sur 13 lignes ; rien à demander au projet | même document que le n° 3, § 3 à 5 | avec le n° 3 | table unique des dates, puis page sur le site |
| 6 | Présentation candidat | récupérée et alignée sur le simulateur le 20261116 : 600 € pour 2 400 € nets | `livrables/presentation_candidat/` | pilotage | relire les autres chiffres contre les classeurs du site |
| 7 | Doctrine et dérivés | référentiel à 236,402 ; 101 dérivés non régénérés | `referentiels/REF_doctrine.json` | en attente | régénération quand le manuscrit est au conteneur |
| 8 | Rangement du dépôt public | 27 083 fichiers de révision pénale sur 28 000 ; 91 états, 24 mandats | `chantier/` | après 3 et 4 | page d'entrée, archivage des états périmés |
| 9 | Contrôles automatiques | aucun sur le site ; un flux `rafraichir` ici | `.github/workflows/` | après 3 | contrôles à chaque pull request |

## Décisions attendues de l'auteur

Présentées en clair dans la conversation le 20261116. Énoncé complet et effet de chaque réponse aux deux documents d'état.

| n° | question | piste du pilotage |
|---|---|---|
| T1 | Tri : quelle base pour le classeur du site | celui du 3 novembre, complété par les corrections du 20 octobre |
| T2 | Jeux : gardés ou supprimés (10 lignes, 6,7 Md€) | gardés |
| T3 | Taxe sur l'électricité : fondue dans la TVA ou gardée (5,2 Md€) | fondue |
| T4 | Taxe sur les complémentaires santé : gardée ou supprimée (6,7 Md€) | gardée |
| T5 | Montants du budget 2026 ou révisés par le budget 2027 | budget 2026 |
| T6 | « en R » sur les redevances : supprimées par décret ou sorties du tri (11 lignes) | supprimées par décret |
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
