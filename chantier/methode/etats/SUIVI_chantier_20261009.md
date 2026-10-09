# Suivi de chantier — dépôt 2027, état au 20261009

**Pièce de référence du chantier.** Elle dit où en est chaque chose, ce qui tourne, ce qui attend
et qui attend quoi. **Elle se lit avant d'ouvrir un fil, et elle se recale à chaque clôture.**

**Porteur** : fil de reprise, Cowork, 20261009.
**Domicile** : `methode/etats/SUIVI_chantier_20261009.md`.
**Elle complète** `methode/etats/REPRISE_bilan_20261008.md`, qui reste la mesure du 20261008, et
`methode/passation_20261009.md`, qui porte la chaîne des dépenses.

---

## 1. Mesure d'entrée — vérifiée au dépôt le 20261009

| objet | mesure | verdict |
|---|---|---|
| **fusion du versement** | `05d77d1` est bien un ancêtre de `main` (`f163486`) | **acquis** |
| **extraction du droit** | jouée, commit `2e0758c`, **millésime LEGI 20261007** | **acquise** |
| **C-1, chaîne hiérarchique** | **CGI 3 484/3 484, CIBS en entier — 100 %** · tous textes 160 952/165 098, **97,5 %** | **acquis en production** |
| **tables du CGI expert** | `referentiels/cgi_expert_{articles,articles_bouges,insertions,parametres,suppressions}.tsv` et `reference/cgi_expert_regles_de_lecture.md` | **présentes au dépôt, absentes du coffre** |
| **socles des textes déposés** | `socle_texte_plf2027.json`, `socle_texte_plfss2027.json`, `articles_ouverts_plf2027.tsv`, `articles_ouverts_plfss2027.tsv` | **présents au dépôt** |
| **pièces de la colonne P1** | 30 fichiers sous `chantier/livrables/depot_2027/P1/` | **conforme au coffre** |
| **paquet** | 63 pièces, 60 rangs actifs — P1 31 · P2 19 · SS 10 —, 6 rangs vacants barrés | inchangé |

**Aucun pépin côté code.** La chaîne technique est entière : fusion faite, extraction jouée,
correction mesurée en production sur les deux codes qui comptent.

---

## 2. Les deux dérives mesurées, et ce qu'elles coûtent

### 2.1 — Le dépôt est en retard de neuf documents sur le coffre

Écrits au coffre depuis le versement et **absents du dépôt** : `livrables/registre_calcul_etatB.md` ·
`methode/passation_20261009.md` · `methode/etats/CALCUL_etatB_20261009.md` ·
`methode/procedure_revue_fond_depot_2027.md` · `methode/manifeste_paquet_depot_20261008.md` ·
`methode/fragments/journal/20261008-versement-depot.md` · les trois fragments d'arbitrage des
20261008 et 20261009.

**Règle arrêtée, et elle est de la tambouille.** **Le coffre est le front, le dépôt est l'archive.**
Un fil Cowork écrit au coffre et ne peut pas écrire au dépôt ; le dépôt se recale **à chaque clôture
d'unité de travail, par un fil code**, sur la liste tenue ci-dessus. **La dérive se mesure, elle ne
s'évite pas** : c'est le prix de la séparation des accès, et il est faible tant que la liste est
tenue.

### 2.2 — Le millésime du droit a changé sous la liasse

Les **2 844 adresses** de la liasse ont été contrôlées au millésime **20261001**. Le dépôt est
maintenant au **20261007**. **Un recontrôle d'adresses est dû avant tout dépôt réel** : mécanique,
d'un geste, et il n'appelle aucun arbitrage.

---

## 3. Les deux chaînes, et elles ne partagent aucun fichier

### Chaîne A — montants et dates, autonome

Elle tourne sans l'auteure et **rend un bilan des décisions à confirmer à la fin**.

1. **combler les huit programmes porteurs** — D5, D6, D16, D19, D22, D25, D27, D32 — et en déduire
   le résiduel de crédits de paiement ligne par ligne
2. **mesurer l'écart mesure / caisse sur 2027** et poser la marge de prudence : la trajectoire est
   calculée **en mesure**, le résiduel n'y est pas, et **68 % de la part État de 2027 a un résiduel
   inconnu**
3. **recalculer** les montants de `coll_P2_02`, périmés, et porter les deux lignes de `etatB_01`
4. **construire le tableau trimestriel par pan**, projection du registre, et y chiffrer les rythmes
   de TVA et de taxe sur les salaires, aujourd'hui hors trajectoire

**Écrit dans** : `livrables/registre_calcul_etatB.md`, `livrables/depot_2027/P2/etatB_*.md`,
`P2/coll_P2_02_credits_etat_B.md`.

### Chaîne B — liasse P1, avec l'auteure

Procédure : `methode/procedure_liasse_P1_20261009.md`, cinq temps.

1. regroupement des abrogations sur la clause, **avec le retrait des dix-neuf rangs ultramarins
   dans la même passe**
2. vérification — quatre contrôles mécaniques
3. revue ensemble sur les signalés, l'auteure ayant la liasse imprimée
4. décisions et passe de correction unique
5. vérification rejouée, puis format de sortie

**Écrit dans** : `livrables/depot_2027/P1/*`, `clause_generale_niches_20261005.md`,
`livrables/registre_colonnes_depot_2027.md` (colonne d'export).

**Un seul fichier commun aux deux chaînes** : le registre des colonnes. **La chaîne B seule y
écrit.**

---

## 4. Ce qui est tranché depuis le 20261008

- **l'outre-mer sort du dépôt** — définitif, question Q1 close ; **les investissements outre-mer non
  propres aux résidents restent dans la clause** (auteure, 20261009) : aucun rang retiré, fil 0 joué
- **les tarifs réduits d'accise** — un rang, trois paragraphes, règle prise au corpus
- **la restitution principale ne s'étale pas, les socles cibles ne bougent pas** — le pilotage du
  calendrier se fait sur les rythmes de CP, les pentes de montée en charge et, à la marge, les
  rythmes de refonte fiscale
- **la correction de `lire_structure` fusionnée fait foi** — mesurée en production, le fil de
  confrontation ne s'ouvre pas

---

## 5. Ce qui attend encore l'auteure

- **l'exercice 2028 n'est pas financé à 21,6 Md€ près** — levier retenu : accélérer les sorties en
  trois ans et piloter les rythmes de TVA et de taxe sur les salaires, à chiffrer par la chaîne A
- **deux agents portent un écart sans contrepartie** — ménages sans revenus d'activité, et agents
  publics dont l'indemnité de départ n'est chiffrée nulle part
- **les trente-trois questions du LISEZ-MOI**, plus Q34 et Q35 inscrites le 20261008, toutes avec
  leur défaut écrit : aucune n'arrête un fil

---

## 6. Ce qui reste dû, hors des deux chaînes

- la **régénération des trois liasses assemblées**, qui portent encore la ligne retirée de SS-01
- la **passe de lecture des 213 virgules de coordination**
- les **renvois entrants** sur les sièges abrogés, jamais relevés et déclarés bloquants
- le **PLFSS**, dix rangs, après P1
