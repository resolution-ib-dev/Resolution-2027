# Pilotage — tableau de bord unique

**Tenu par le fil de pilotage** (`session_01VynsZnrEusr42WSGSHbdEg`). L'auteur ne parle qu'à ce
fil ; les fils d'exécution lui rendent compte et ne posent pas de question à l'auteur. Ce
tableau se met à jour à chaque fusion et à chaque point. *Relevé le 20261116.*

## Chantiers

| n° | chantier | état | où | fil porteur | prochaine étape |
|---|---|---|---|---|---|
| 1 | Classeurs du site (8) | à jour, cohérents | `Site-ETNP/site/donnees/` | pilotage | copier outils et documentation au dépôt public |
| 2 | Simulateur | en ligne, non lié ; 1 bloc revu sur 6 | `Site-ETNP/site/reprenez.html` | à lancer | revue Agences, puis Agents, Associations, niches, patrimoine, « En échange » |
| 3 | Liasse de crédits, PLF 2de partie | 22 amendements sans socle ni rythme (43,69 Md€ d'AE) | `livrables/depot_2027/LIASSE_PLF_P2.md` | `session_01VynsZmDQ62Rx22gNZrBEjT`, branche `claude/liasse-parametres` | table des paramètres, puis régénération depuis `Dépenses de l'État.xls` |
| 4 | Tri des impôts | deux versions : 20 octobre (branche orpheline, 31 fichiers) et 3 novembre (`main`) | `origin/claude/clever-euler-rbeck4` ; `appareil/tri_porte/` | `session_01VynsZkmoTfP4UpCNFSaGoa`, branche `claude/tri-impots-recuperation` | comparer les deux, récupérer, puis classeur sur le site |
| 5 | Calendrier de mise en œuvre | quatre documents, contredits par l'outil de la liasse | `livrables/registre_calcul_etatB.md` § 4 à 6 ; `registre_exceptions_dates.md` ; `suivi_trajectoire_20261015.md` ; `flux_par_agent_20261015.md` | avec le n° 3 | une table unique des dates, puis page sur le site |
| 6 | Présentation candidat | récupérée le 20261116, six fichiers ; dit « 600 € au salaire médian de 2 190 € », le simulateur dit 600 € à 2 400 € | `livrables/presentation_candidat/` | pilotage | réaligner après D6 |
| 7 | Doctrine et dérivés | référentiel à 236,402 ; 101 dérivés non régénérés | `referentiels/REF_doctrine.json` | en attente | régénération quand le manuscrit est au conteneur |
| 8 | Rangement du dépôt public | 27 083 fichiers de révision pénale sur 28 000 ; 91 états, 24 mandats | `chantier/` | après 3 et 4 | page d'entrée, archivage des états périmés |
| 9 | Contrôles automatiques | aucun sur le site ; un flux `rafraichir` ici | `.github/workflows/` | après 3 | contrôles à chaque pull request |

## Décisions attendues de l'auteur

| n° | question | depuis |
|---|---|---|
| D1 | Tri des impôts : la version du 20 octobre ou celle du 3 novembre fait-elle foi ? (écarts à présenter) | 20261116 |
| D2 | Tri : cinq points laissés sans réponse par le fil « Vérification tri des prélèvements » — millésime des rendements, sens de « en R », les 13 qualifications, écarts entre tri et schéma, date de fin | 20261103 |
| D3 | Liasse : un amendement par mission ou par ligne ; quelle date l'emporte quand le registre et l'outil diffèrent | 20261116 |
| D4 | Rendement du patrimoine : 3,2 % (simulateur), 3 % (livre) ou 2,9 % (classeur) | 20261116 |
| D6 | Présentation candidat : garder « 600 € au salaire médian de 2 190 € » ou passer à « 600 € pour 2 400 € nets » comme le simulateur | 20261116 |
| D5 | Activer « Automatically delete head branches » sur `Site-ETNP` (réglage GitHub) | 20261116 |

## Branches à traiter

`Resolution-2027` : `clever-euler-rbeck4` (tri du 20 octobre, 31 fichiers absents de `main`),
`funny-faraday-260skj` (présentation candidat, récupérée : à supprimer), `retrait-liasses-20261012` (13 fichiers anciens),
`bold-fermi-spo7c6` (rien d'absent), `beautiful-curie-xzsshi` (un lot pénal).
`Site-ETNP` : `clever-euler-rbeck4` (classeur du tri, brouillon), `bold-fermi-spo7c6` (compteur
des lettres), quatre branches de septembre et d'octobre sans ancêtre commun.

## Règles de marche

- Un fil d'exécution par chantier, sur sa branche ; un seul à la fois touche `methode/` et
  `appareil/`. Le pilotage les lance, lit leurs transcriptions, contrôle et fusionne.
- Les classeurs de `Site-ETNP/site/donnees/` font foi. Tout ce qu'un outil lit est dans un dépôt.
- Une décision de l'auteur se demande ici, en question fermée, et s'inscrit au registre le jour même.
