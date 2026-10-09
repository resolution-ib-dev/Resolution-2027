# CR au fil de tête — table de couverture du CGI de l'expert, et tenue du coffre — 20261009

**Porteur** : fil de la table de couverture du CGI de l'expert, Cowork, 20261009.
**Mandat** : l'auteure, 20261009 — régénérer la table de couverture spécifiée à
`methode/etats/T2.md`, la verser à `referentiels/couverture_cgi_expert.tsv`, et dégager la
place au coffre si elle manque.
**Domicile** : `methode/cr_couverture_cgi_expert_20261009.md`.
**Appui** : `methode/etats/T2.md` · `methode/etats/FIL1_verification_20261009.md`, liste 2 ·
`methode/ordre_du_jour_revue_P1_20261009.md` · `methode/etats/FIL0_regroupement_20261009.md` (R-G) ·
`reference/cgi_expert_regles_de_lecture.md` · `methode/arbitrages.md`, D-1 ·
`methode/appui_des_passes.md`, R-G, R-H, R-I, R-V, R8 · `livrables/registre_colonnes_depot_2027.md` ·
skills `resolution-chantier`, `confrontation` · dépôt de droit `Resolution-2027` cloné,
millésime LEGI **20261007**, `droit.py etat` joué, 62 textes.

**Ce CR ne demande rien d'autre qu'une confirmation.** Aucune pièce n'est touchée, aucun
exposé n'est écrit, rien n'est retiré du coffre.

---

## 1. Mesure d'entrée — rendue avant toute écriture

| objet | mesure |
|---|---|
| articles en entrée aux quatre tables de l'expert | **1 743** distincts · **1 746** avec les 3 portés au seul `cgi_expert_articles_bouges.tsv` |
| pièces du paquet citant un article du code général des impôts | **32 sur 64** — 26 première partie, 2 loi de financement, 2 sans colonne, 2 à la racine |
| place disponible au coffre | **31 810 octets** sur 2 000 000 |

## 2. Fait — la table est régénérée, et elle n'est pas versée

**1 746 lignes, neuf colonnes, 289 251 octets.** Droit lu au millésime LEGI 20261007 ; clause
prise **au coffre**, le dépôt portant encore l'ancien III à 396 rangs.

| verdict | articles |
|---|---:|
| intégré conforme | 583 |
| intégré divergent | 69 |
| absent de nos pièces | 1 028 |
| hors périmètre PLF 2027 | 66 |
| **total** | **1 746** |

**Ce que la passe a dû résoudre, et qui n'existait pas au 20261007.** Le regroupement du
20261009 a remplacé 220 abrogations nominatives par 171 désignations de division. Un relevé
qui ne lit que les numéros d'article déclare ces 220 articles absents de nos pièces. La
résolution est celle que le fil 0 a versée avec son contrôle — mêmes modules `clause.py` et
`designer.py`, même index de divisions —, et **0 désignation reste non résolue**.

## 3. Deux objets annoncés que la mesure ne trouve pas

**Les quatre pièces portant une section de reprise de l'expert dans leur texte déposable
n'existent pas.** Deux pièces portent une telle section — `P1/4_2_refonte_taxes_D_plus_values.md`
et `P1/n5_compte_epargne_personnel.md` — et **les deux sont sous le bloc `[interne]`**, donc hors
du texte déposable. **Rien à descendre, et le fil 2 n'a rien à reprendre de ce chef.**

**Le retrait prévu ne dégage pas la place.** Retirer les originaux des trois lots libère
150 935 octets ; avec les 31 810 disponibles, **182 745 contre 289 251 — il manque 106 506**.
Détruire du coffre sans que la pièce y entre n'a pas de sens : le fil s'arrête là (R-V).

## 4. Proposé — la table ne se verse pas, le générateur si

**La table est un dérivé daté, non une table d'arbitrages à consulter.**

| ce que portent les 1 746 lignes | volatil |
|---|---|
| 1 012 lignes sans rang | non |
| 360 lignes « III quater / III quinquies » | non — c'est une division, pas un numéro |
| 284 rangs du III de la clause | **oui** — le III est passé de 396 à 389 le 20261009 |
| 90 rangs de colonne P1-xx | **oui** — le recalcul du 20261008 en a déplacé 59 sur 62 |

Retirer la colonne de rang ne gagne que **13 736 octets** : le poids n'est pas là. Les colonnes
verdict, écart et bloc sont stables tant que le millésime et les pièces ne bougent pas,
c'est-à-dire jusqu'à la prochaine passe de rédaction.

**Ce qui se verse à sa place** : le générateur, **quatre modules, 25 398 octets**, qui refait la
table à l'identique au millésime du jour et porte la résolution des divisions. La règle du
corpus est déjà écrite : un dérivé qui se régénère à l'identique ne se verse pas au coffre.

## 5. Proposé — deux retraits du coffre, mesurés, sans perte de source

| retrait | octets | ce qui est perdu |
|---|---:|---|
| `livrables/depot_2027/LIASSE_20261008.md` — les trois colonnes réunies | **364 360** | rien : les trois liasses par colonne la reconstituent, et les quatre tirages portent déjà l'ancien III, régénération due |
| les 33 originaux de `liasse_nuit_plf2027_p1/`, `liasse_arrets_immediats/` et `lot_2_2_effectifs/` | **150 935** | rien : au dépôt depuis la fusion du 20261008, notices `.PERIME.md` conservées |
| **total** | **515 295** | coffre à 1 453 KB, **547 KB disponibles** |

**L'étage suivant, et il ne se fait pas d'ici.** **Dix-huit modules sont versés au coffre alors
qu'ils sont de voie `depot`** — fil 0 de regroupement, fil 1 de vérification, chaîne A,
versement, scission de liasse, contrôle d'adresses. Ils se poussent au dépôt par un fil
claude.ai/code, puis se retirent du coffre. Un fil Cowork ne peut pas pousser (A-393).

## 6. Ce que le fil de tête a à confirmer — trois points

1. **La table ne se verse pas au coffre ; le générateur s'y verse à sa place**, et la table se
   rejoue à la demande au millésime du jour.
2. **Les deux retraits du § 5 sont joués** — la liasse unique et les 33 originaux.
3. **Un fil claude.ai/code est ouvert** pour pousser au dépôt les dix-huit modules d'appareil et
   les retirer du coffre.

**Tout ce qui précède est proposé, rien n'est validé.** Les trois points sont indépendants :
le refus de l'un ne bloque pas les deux autres.

## 7. Mesure de sortie — le mandat point par point

| point du mandat | verdict |
|---|---|
| mesurer et rendre le compte avant écriture | **joué** |
| cloner le dépôt, millésime LEGI 20261007 | **joué** |
| régénérer la table, une ligne par article | **joué** — 1 746 lignes, 289 251 octets |
| la verser à `referentiels/couverture_cgi_expert.tsv` | **non joué** — place insuffisante, et la pièce est un dérivé daté (§ 4) |
| retirer du coffre les originaux des trois lots | **non joué** — le retrait seul ne suffit pas ; proposé au § 5 avec un second retrait qui, lui, suffit |
| constater les quatre pièces portant la section dans le texte déposable | **joué — objet non trouvé** : 2 pièces, les deux sous `[interne]` |
| ne corriger aucune pièce, ne rédiger aucun exposé | **tenu** — 0 pièce touchée |
