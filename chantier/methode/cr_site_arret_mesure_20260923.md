# CR — fil de production site, arrêt sur mesure (20260923)

## Mandat reçu
Dépôt `resolution-ib-dev/Site-ETNP` seul. Quatre pièces et rien d'autre :
(1) page « Le livre », (2) page « Les auteurs », (3) page « Mentions légales »,
(4) retrait de `resolution_une_page.html` + suppression de « et à meilleur prix »
à la fiche consommateur. Forme `fiche.css`, Archivo et Source Serif 4.
Pas de poussée en production.

## Mesure d'ouverture

| objet annoncé | mesuré |
|---|---|
| dépôt `Site-ETNP` | **0 fichier.** Clone HTTPS refusé ; API GitHub 403 — « GitHub access to this repository is not enabled for this session ». Le jeton de session s'authentifie (`/user` → `resolution-ib-dev`) mais le dépôt n'est pas attaché. Aucun outil d'attachement de dépôt dans cette session Cowork. |
| pièce jointe couverture | **0 fichier.** Aucune pièce jointe à la conversation ; aucune image parmi les 8 fichiers du projet (8 classeurs). |
| pièce jointe photo des auteurs | **0 fichier.** Idem. |
| `livrables/etat_site_20260921.md` | lu |
| `methode/passation_site.md` | lu |
| `livre/texte_livre.json` | présent au projet, **non ouvert** — le fil s'arrête avant. |

## Décision
Arrêt immédiat, conformément à la règle : mesure vide → le fil rend le nombre et
ne joue aucun contrôle.

## Ce que le fil a produit
Rien. Aucune page, aucun fichier, aucun export, aucune écriture au projet.
Le site en ligne est inchangé.

## Ce qui reste à faire, inchangé
- page « Le livre » — n'existe pas
- page « Les auteurs » — n'existe pas
- page « Mentions légales » — n'existe pas
- `resolution_une_page.html` — toujours servi, lié de nulle part
- « et à meilleur prix », fiche consommateur, ligne *Le choix* — toujours en ligne
  (signalé le 20260904, non tranché au 20260921, non corrigé au 20260923)

## Matière désormais complète, à porter au fil suivant
- **Éditeur** : Éditions Chronique, 57 rue Gaston-Tessier, 75019 Paris.
  ISBN 978-2-36-602648-1. Parution octobre 2026. Précommande.
- **Mentions légales** (input auteur, reçu le 20260923) : éditeur association
  Résolution, association déclarée n° 991 580 622, siège 113 avenue de Verdun,
  92130 Issy-les-Moulineaux, contact@france-resolution.fr ; directeur de la
  publication Moïse Mitterrand, président ; hébergeur Vercel Inc.,
  440 N Barranca Ave #4133, Covina CA 91723, États-Unis.
- **Bios** : `livre/texte_livre.json`, folios 173-177 (Barrat 173-174,
  Marle 174-175, Mitterrand 175-177). Quatrième de couverture aux folios 5-6.
- **Forme** : `fiche.css`, Archivo (titres, petites capitales, chiffres) et
  Source Serif 4 (texte courant). Arbitrage 6 du relevé du 20260921 — le site
  fait foi, les pièces neuves suivent le site.

## Deux conditions d'ouverture d'un fil site
1. **Le dépôt.** Session `claude.ai/code` avec `Site-ETNP` sélectionné. Cowork
   n'a pas de sélecteur de dépôt — mur relevé au 20260904, confirmé au 20260923.
2. **Les deux images.** Couverture et photo des auteurs à joindre à la
   conversation, pour les pages « Le livre » et « Les auteurs ».

Sans ces deux conditions, un fil site rendra la même mesure vide. *Le fil window
dressing du 20260923 (`methode/prompt_fil_window_dressing_site.md`) ne requiert
que la première : il ne touche à aucune page à image.*

## Tranché par ce fil
- `resolution_une_page.html` : **retrait**, et non raccrochage. Le relevé du
  20260921 posait l'alternative ; le mandat vaut arbitrage, tranché le 20260923.
- Un mandat touchant le dépôt va en session `claude.ai/code` avec le dépôt
  sélectionné, jamais en Cowork ; aucune pièce jointe n'est nommée dans un mandat
  sans avoir été vérifiée présente.
