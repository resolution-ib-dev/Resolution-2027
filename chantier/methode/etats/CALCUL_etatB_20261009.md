# État — fil de calcul des montants d'état B, 20261008 et 20261009

**Porteur** : fil Cowork de portage des montants d'état B, dépôt 2027.
**Mandat** : l'auteure, 20261008 — « montants d'état B de P2-01 et P2-02 », puis la chaîne d'arbitrages des 8 et 9 octobre.
**Domicile** : `methode/etats/CALCUL_etatB_20261009.md`.
**Appui** : `methode/appui_des_passes.md` R-G, R-H, R-I, R8 · `methode/suivi_depenses_20261007.md` § 2, § 4, § 7, § 9 · `reference/regles_credits.md` · `livrables/registre_exceptions_dates.md` · `livrables/registre_colonnes_depot_2027.md` · `methode/etats/L2.md` · `methode/etats/APP_classeur_20261007.md` § 5 · pièces jointes `Suivi dépenses — crédits et vecteurs_20261007.xlsx` et `Synthèse Calculs Résolution_0910.xlsx` · dépôt de droit, millésime LEGI 20261001.
**Mesure** : 13 cellules et 2 formules mesurées à l'entrée · 27 lignes doctrinales renseignées sur 9 paramètres · 4 exercices projetés · 8 contrôles mécaniques joués, 8 tenus · 3 fautes propres corrigées · 21 arbitrages de l'auteure inscrits · 12 points laissés ouverts · 3 pièces écrites, 1 supprimée.

---

## 1. Ce qui fait foi à la sortie du fil

| pièce | rôle |
|---|---|
| **`livrables/registre_calcul_etatB.md`** | **point de vérité unique** du socle, du rythme, de la fraction d'exercice, de l'acteur, du résiduel de crédits de paiement et de la trajectoire. Aucun montant d'état B ne s'écrit sans que sa ligne y soit renseignée |
| `livrables/depot_2027/P2/coll_P2_02_credits_etat_B.md` | 3 lignes de montant portées sur 4 — **périmées**, antérieures à la chaîne |
| `methode/suivi_depenses_20261007.md`, § 9 | régime des classeurs, R-J à R-L |

**`livrables/suivi_effets_mensuels_2027.md` est supprimé** : deux tableaux sur les mêmes lignes sont une divergence en attente. Son contenu est absorbé par le registre.

---

## 2. Mesure d'entrée — R-H

**Les treize cellules** relevées le 20261007, remesurées sur `Synthèse Calculs Résolution_0910.xlsx` : **13 sur 13 résolvent**, valeurs inchangées.

**Les deux formules** `SynthèseR!H8` (`=G21+D21+C20*7/3`, cache 3 609,60) et `SynthèseR!F32` (`=('Economies R'!S4-C31-D31-F20-E31-197,995)*0,9`, cache 1 820,31) : **toujours en place, toujours fausses**, +1 371,1 et −215,7 M€. **Elles ne seront pas corrigées** : les synthèses de l'auteure sont de l'input, l'écart s'y note (R-J).

---

## 3. Contrôles mécaniques joués — 8 sur 8 tenus

| contrôle | résultat |
|---|---|
| **complétude** des 27 lignes sur 9 paramètres | **tenue** — cellule source, régime plein, socle, rythme, acteur, incidence, date, fraction, montant. Seul le **programme porteur manque, sur 8 lignes** |
| **somme de la matrice mensuelle = total annuel 2027** | **51,69 contre 51,69, écart 0,0000** |
| **solde de la matrice = restitution − coupes** | **−18,30 contre −18,30** |
| **périmètre** : 27 lignes + 8 lignes de première partie et sociale contre `Flux`!C6 | **128,09 contre 129,40 — écart 1,31 Md€, soit 1,0 %** |
| **titre 2** : table A contre `Détail Economies`!F38 | **2 958,8 contre 3 000 — écart −1,4 %** |
| **contemporanéité** des transferts monétaires aux ménages actifs | **tenue** — creux cumulé **−0,59 Md€** en juin, refermé dès juillet |
| **plafonds d'état B 2027** sur les montants déjà portés à `coll_P2_02` | 6 sur 6 tenus, mais **les montants sont périmés** |
| **aucun second tableau sur les mêmes lignes** | tenu — une seule pièce porte les paramètres |

---

## 4. Trois fautes propres, corrigées

**4.1 — Double proratisation de l'apprentissage.** Le rythme de 1/6 est **déjà net de la date d'effet** ; je l'avais réduit une seconde fois de moitié. La ligne passe de 0,58 à **1,15 Md€** et le total 2027 de 51,12 à **51,69**. Règle inscrite : *un rythme déjà net de la date ne se proratise pas une seconde fois.*

**4.2 — Imputation du chèque énergie.** Il n'est pas au programme 345 « Service public de l'énergie », classé « sortie en 3 ans », mais au **programme 174, catégorie 61**, arrêté. Le constat antérieur « la doctrine contredit l'annexe sur le chèque énergie » **est faux et retiré**.

**4.3 — Socle présumé universel.** Les 10 % avaient été appliqués aux 27 lignes ; **dix seulement en portent un**. Sans socle, l'aide au logement se reconstitue à **−0,5 %** du classeur au lieu de −10,4 % — et c'est cette coïncidence qui avait masqué, un temps, que le ⅓ est une marche de régime et non une économie d'exercice.

---

## 5. Divergences de compteurs, mesurées et non résorbées

| compteur | mesure du fil | pièce de référence | écart |
|---|---:|---|---:|
| économies de régime plein | 128,09 Md€ | `Flux`!C6 — 129,40 | **1,31 Md€, 1,0 %** |
| titre 2, régime plein | 2 958,8 M€ | `Détail Economies`!F38 — 3 000 | **−1,4 %** |
| aide au logement, 2027 | 2 683 M€ | `Détail Economies`!D18 — 5 400 | **facteur 2,0**, expliqué par la date d'effet |
| départs de fonctionnaires, 2027 | 1 350 M€ | `Détail Economies`!D38 — 900 | écart de calendrier et d'échelonnement, non instruit |
| entreprises, flux 2027 | −12,90 Md€ | registre, § 6 — −12,91 | **arrondi de 0,01**, sans effet sur le total |

**Aucune de ces divergences n'est une erreur de chaîne** : ce sont deux mesures du même périmètre, l'une en régime plein à la synthèse, l'autre à l'annexe et au calendrier. Elles se notent, elles ne se résorbent pas (R-K).

---

## 6. Récapitulatif par agent — exercice 2027

| agent | flux 2027 | premier mois négatif | creux cumulé | contrepartie |
|---|---:|---|---:|---|
| **Ménages actifs — transferts monétaires** | **+25,40** | janvier | **−0,59** | restitution dès juillet — **tenu** |
| Ménages actifs — services en nature | −13,45 | janvier | −13,45 | hors contrôle, R-T |
| Ménages sans revenus d'activité | −1,99 | avril | −1,99 | **aucune — écart structurel** |
| Agents publics | −6,51 | juillet | −6,51 | **indemnité de départ, non chiffrée — écart structurel** |
| Entreprises | −12,90 | janvier | −12,90 | baisse du coût du travail dès juillet — assumé |
| Associations | −2,37 | juillet | −2,37 | restitution à leurs salariés — indirect |
| Opérateurs | −3,27 | juillet | −3,27 | restitution à leurs agents — indirect |
| Collectivités | −3,20 | janvier | −3,20 | hors exercice |
| **Solde tous agents** | **−18,30** | — | — | bascule en **octobre 2027** |

Restitution 33,39 Md€ · coupes 51,69 Md€ · **gain net du budget 18,30 Md€**.

**Trajectoire** : coupes 51,69 · 92,85 · 116,20 · 119,79 ; restitution 33,39 · 114,46 · 114,46 · 114,46 ; **solde +18,30 · −21,61 · +1,74 · +5,33**.

---

## 7. Arbitrages de l'auteure, inscrits

Millésime 2026 avec contrôle sur l'état B 2027 · ligne à ligne des annexes et compteurs propres · synthèses non corrigées, écart noté · socle non universel, lu à la ligne · résiduel de crédits de paiement d'au moins 15 % sauf AE = CP par construction · titre 5 à 20 % récupérables · fin de versement = fin de dossier + 1 mois · simultanéité pour les citoyens concernés · contrôle de contemporanéité seul, seuil au cas par cas · un seul tableau · MaPrimeRénov' et CPF arrêtés au 1er janvier 2027 · chèque énergie à 6/12 · France Travail au 1er janvier avec un sixième conservé · aide au logement : demandes au 1er juin 2027, versements au 1er juillet · sous-cas du parc conventionné récent **sans repousser la date de fin** · schéma d'apprentissage à trois étages validé · trajectoire consolidée à l'agrégat.

---

## 8. Douze points ouverts

**Bloquants pour écrire un montant d'amendement :**

1. **Le programme porteur manque sur 8 lignes** — D5, D6, D16, D19, D22, D25, D27, D32. C'est le seul chaînon qui empêche de descendre le socle et le rythme sur les 265 lignes d'annexe arrêtées.
2. **Les montants de `coll_P2_02` sont périmés** et à recalculer.
3. **La ligne 119 du volet collectivités** reste sans montant : la catégorie 63 porte la dotation générale de décentralisation entière, et ses crédits de paiement de 2026 excèdent de 73,5 M€ ceux ouverts en 2027.

**Paramètres manquants :**

4. Borne du socle des départs de fonctionnaires locaux — « 10 à 20 % », 15 % retenu par défaut.
5. Partage de la ligne D25 entre « aides à l'emploi » et « apprentissage ».
6. Clé de répartition de la restitution entre ménages actifs et agents publics — 90/10 posé, non mesuré.
7. Taux de rotation du parc locatif, pour isoler l'effet de la fermeture du flux neuf.
8. Montant unitaire et durée de l'indemnité de départ (`P2/2_2_indemnite_depart_agents.md`), et masse salariale par programme au texte déposé 2027.
9. Régime de l'aide à l'apprentissage pour les contrats démarrant à compter du 1er janvier 2027 — hors du champ du décret n° 2026-168, **à vérifier sur Légifrance**.

**Questions de fond :**

10. **L'exercice 2028 n'est pas financé, à 21,6 Md€ près** : la restitution passe en régime plein dès janvier quand les coupes n'ont franchi qu'une marche sur trois. Trois sorties : étaler la dernière marche de restitution, accélérer les sorties en trois ans d'un exercice, ou assumer et financer l'à-coup.
11. **Deux écarts structurels sans contrepartie** : les ménages sans revenus d'activité (−1,99 Md€), que seul le socle protège, et les agents publics (−6,51 Md€), dont la contrepartie est une indemnité non chiffrée.
12. **Deux pièces déclarées au corpus et jamais ouvertes** : `etats/suivi_calendrier_flux.tsv` et `etats/suivi_mensuel_2027_restitution.tsv`, nommées à `methode/etats/L2.md`. Si leur trajectoire diffère de celle du registre, **c'est la leur qui fait foi**.

---

## 9. Reprises dues aux pièces, rendues en clair et non appliquées (R8)

Au registre, § 11 : le I de l'article L. 822-2-1 de `P2/2_6_extinction_aide_logement.md`, recalé sur le dépôt de la demande au 1er juin 2027 · le II bis nouveau, sous-cas du parc conventionné récent, une marche de moins et le même terme · une ligne à ouvrir au registre des exceptions de dates, le **1er juillet 2027**, premier versement supprimé.

---

## 10. Mesure de sortie — le mandat point par point

| point | verdict |
|---|---|
| mesurer les treize cellules et les deux formules | **joué** — 13/13, 2/2 |
| rendre le compte avant toute écriture | **joué** |
| porter les montants à `P2/etatB_01` | **non joué** — 2 lignes dues, aucune source |
| porter les montants à `P2/coll_P2_02` | **joué puis périmé** — 3 lignes sur 4, antérieures à la chaîne de calcul |
| établir la chaîne de calcul | **joué** — 8 règles, R-M à R-U |
| tenir les tableaux d'effets par acteur et par mois | **joué** — 7 acteurs, ménages scindés, 12 mois |
| consolider la trajectoire | **joué** — 4 exercices, contrôle de périmètre à 1,0 % |
| un seul tableau | **joué** — pièce fusionnée, doublon supprimé |
| écrire la liasse des 31 amendements | **non joué** — bloqué par les 8 programmes porteurs |
