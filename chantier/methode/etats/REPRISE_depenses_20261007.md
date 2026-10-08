# Reprise des travaux sur les dépenses — mesure et verdicts, 20261007

**Porteur** : fil Cowork de réconciliation et de reprise des travaux sur les dépenses, 20261007.
**Mandat** : l'auteure, 20261007 — mesurer d'abord `SynthèseR!H8` et `SynthèseR!F32` et rendre le
compte avant toute écriture ; puis traiter le reste dû du § 7 de `methode/suivi_depenses_20261007.md`
dans l'ordre, de 1 à 6 ; ne rédiger aucun amendement ; la mesure de sortie reprend le mandat point
par point, avec un verdict par point, « non joué » compris.
**Domicile** : `methode/etats/REPRISE_depenses_20261007.md`.
**Appui** : `methode/appui_des_passes.md` · `methode/suivi_depenses_20261007.md` ·
`reference/regles_credits.md` · skill `confrontation` · skill `resolution-chantier` ·
et, au titre de la règle **R-G**, les trois états de la même matière et du même jour :
`methode/etats/APP_etatB.md`, `methode/etats/CROISEMENTS_20261007.md`,
`methode/cr_consolidation_20261007.md` — tous ouverts et lus intégralement avant la passe.
Pièces jointes ouvertes : `PLF26 - Depenses 2026 du BG et des BA selon nomenclatures destination
et nature_0910.xls` · `Synthèse Calculs Résolution_0910.xlsx` ·
`Synthèse ETP et agences Résolution_0910.xls` · `PLF 2026_VM tome I - Annexe 2 - Taxes
affectees_0910.xls`.
**Mesure** : 2 formules mesurées et **confirmées à la décimale par réapplication** · 1 blocage
antérieur levé · 6 points du § 7 traités — **3 joués, 1 joué et contredit, 1 joué en partie,
1 non joué faute d'objet** · **4 divergences nouvelles mesurées** · 1 pièce de travail du mandat
**absente** · **8 ensembles de références laissés hors contrôle** · 0 pièce réécrite ·
0 amendement rédigé · 3 questions fermées.

---

## 1. La mesure d'entrée — les deux formules, et le compte rendu avant toute écriture

**Instrument.** Le classeur a été lu **en valeurs de cache**, par `xlrd` sur le `.xls` d'origine,
sans aucun recalcul par un moteur tiers — règle 5.3 de `suivi_depenses`. Aucune conversion
LibreOffice n'est intervenue.

**`SynthèseR` est une feuille du classeur**, confirmé : les cinq feuilles sont `SynthèseR`,
`Economies R`, `Données PAP 2026`, `Crédits RAP 2024`, `Emplois RAP 2024`.

### 1.1 Les deux cellules portent une valeur

| cellule | valeur en cache |
|---|---:|
| `SynthèseR!H8` | **3 609,601 876 62** |
| `SynthèseR!F32` | **1 820,310 233 310 006** |

### 1.2 Les deux formules annoncées au § 2 de `suivi_depenses` sont exactes

`xlrd` ne rend pas le texte d'une formule BIFF. La preuve est donc prise par **réapplication**
(skill `confrontation`, § 5 : pièce de structure → réapplication qui doit redonner le résultat) :
la formule annoncée, rejouée sur les valeurs en cache de ses opérandes, redonne la valeur en
cache de la cellule **à la dernière décimale**.

| cellule | formule annoncée | réapplication | cellule | verdict |
|---|---|---:|---:|---|
| `H8` | `=G21+D21+C20*7/3` | 3 609,601 876 62 | 3 609,601 876 62 | **concorde** |
| `F32` | `=('Economies R'!S4−C31−D31−F20−E31−197,995)*0,9` | 1 820,310 233 310 006 | 1 820,310 233 310 006 | **concorde** |

Opérandes relevés : `G21` = 594,421 876 62 · `D21` = 560,70 · `C20` = 1 051,92 ·
`'Economies R'!S4` = 21 827,398 682 · `C31` = 16 116,735 643 · `D31` = 1 094,67 ·
`F20` = 1 333,325 022 · `E31` = 1 062,106 091 1.

### 1.3 Les deux défauts sont confirmés, et chiffrés

**`H8`** omet `E21` = 53,518 5 (Anah) et `H21` = 1 317,606 713 955. Somme omise :
**1 371,125 2 M€**. Le § 2 annonce +1 371,1 — **concorde**.

**`F32`** retranche `D31` et `E31` d'une base brute alors que les deux sont déjà nets de leur
0,9 : `'Economies R'!R155` = 1 216,30 × 0,9 = 1 094,67 = `D31` **à l'octet** ; `R177` =
1 180,117 879 × 0,9 = 1 062,106 091 1 = `E31` **à l'octet**. Base amputée de 239,641 787 9 ;
× 0,9 → **−215,677 609 1 M€**. Le § 2 annonce −215,7 — **concorde**.

### 1.4 Un blocage antérieur est levé par cette mesure

`methode/cr_consolidation_20261007.md`, § 5.2, porte : « `SynthèseR` n'existe dans aucune des sept
feuilles de `Synthèse Calculs`, et les quatre cellules du mandat ne rendent nulle part les valeurs
annoncées. **La correction du classeur est bloquée, et avec elle les croisements.** »

Les deux constats sont exacts et le blocage tombe : `SynthèseR` n'est pas dans
`Synthèse Calculs Résolution_0910.xlsx` — elle est dans
`PLF26 - Depenses 2026 du BG et des BA selon nomenclatures destination et nature_0910.xls`.
**Le classeur et la feuille sont nommés ; le blocage § 5.2 est levé.**

---

## 2. Le reste dû du § 7, point par point, dans l'ordre

### Point 1 — Poser `H8` et `F32` dans `SynthèseR` → **rendu en clair, non appliqué**

**Pourquoi non appliqué, et ce n'est pas un défaut de mesure.** Le classeur porteur est une
**pièce jointe du projet**, donc en lecture seule (`resolution-chantier`, § 2) : une correction
ne s'y écrit pas, elle produirait un classeur nouveau. Or le mandat ne nomme qu'une pièce à
écrire, le présent état, et la règle du projet veut qu'un fil ne produise que les pièces que son
mandat nomme. Un classeur corrigé est en outre un document lourd, qui attend un go.

**Les deux divisions, à appliquer telles quelles le jour du go** :

> `SynthèseR!H8` → `=G21+D21+E21+H21+C20*7/3`
> valeur attendue **4 980,727 090 575** (3 609,601 876 62 + 1 371,125 213 955)

> `SynthèseR!F32` → `=('Economies R'!S4−C31−'Economies R'!R155−F20−'Economies R'!R177−197,995)*0,9`
> valeur attendue **2 035,987 842 420 006** (1 820,310 233 310 006 + 215,677 609 11)

**Avertissement reporté de `suivi_depenses`, § 6.1** : le −215,7 ne se répartit pas sur
`Détail Economies!D19` et `D21` ; `F32` est le résidu « Autres » du bloc ménages. Le classeur
`Synthèse Calculs Résolution_corrige_20261007.xlsx` porte cette faute et ne se verse pas.

### Point 2 — Relier `Détail Economies` et `Flux` à `SynthèseR`, passer `Flux!C15`, `E15` et les totaux de bloc en sommes → **mesuré, joué en mesure, non appliqué**

**Le sens du lien est l'inverse de celui qu'on attendait, et c'est ce qui compte.**
`Détail Economies` est **déjà** relié à `Flux`, et dans ce sens-là seulement :
`Détail Economies!D3` = `=Flux!C15`, `D4` = `=Flux!C16`, `E3` = `=Flux!E15`, `F3` = `=Flux!G15`.
C'est `Flux` qui est en dur, et `Détail Economies` qui en descend. **Aucune cellule des deux
feuilles ne renvoie à `SynthèseR`** — les deux classeurs ne se parlent pas.

**Les totaux de bloc de `Flux`, mesurés contre la somme de leurs composantes :**

| total | en place | somme des composantes | écart |
|---|---:|---:|---:|
| `C8` niches fiscales | 43,1 | 43,1 | 0 |
| `E8` | 29,1 | 29,1 | 0 |
| `G8` | 72,3 | 72,3 | 0 |
| `C15` économies État | **44,0 en dur** | 44,0 | 0 |
| `E15` | **38,5 en dur** | 38,454 667 | **+0,045 333 Md€ (+45,3 M€)** |
| `G15` | 82,5 | 82,5 | 0 |
| `C22` collectivités | **33,3 en dur** | 33,4 | **−0,100 Md€ (−100 M€)** |
| `E22` | 20,1 | 20,1 | 0 |
| `G22` | **53,4 en dur** | 53,5 | **−0,100 Md€ (−100 M€)** |

**Trois divergences nouvelles, non relevées par `suivi_depenses`.** `C15` tombe juste aujourd'hui,
ce qui masque le défaut : il est en dur et ne bougera pas quand ses composantes bougeront. `E15`,
`C22` et `G22` ne tombent déjà plus juste. L'écart de 100 M€ sur les collectivités est le même en
année 1 et à terme : les quatre lignes locales somment à 33,4 et le bloc en porte 33,3.

**La division à appliquer le jour du go** : `C15` → `=SUM(C16:C21)` · `E15` → `=SUM(E16:E21)` ·
`G15` → `=SUM(G16:G21)` · `C22` → `=SUM(C23:C26)` · `E22` → `=SUM(E23:E26)` ·
`G22` → `=SUM(G23:G26)` · `C8` → `=SUM(C9:C12)` et ses deux symétriques. **Non appliqué** : même
motif qu'au point 1.

### Point 3 — Mesurer les résidus au lieu de les caler → **confirmé à la lettre**

Les quatre lignes « autres » de `Détail Economies` sont des **soldes**, le total de bloc étant
une entrée en dur :

| ligne | formule en place | résidu mesuré |
|---|---|---:|
| `D16` autres opérateurs | `=D4-SUM(D5:D15)` | **2,600 Md€** |
| `D22` autres chèques | `=D17-SUM(D18:D21)` | **0,900 Md€** |
| `D27` autres entreprises | `=D23-SUM(D24:D26)` | **1,200 Md€** |
| `D36` autres associations | `=D28-SUM(D29:D35)` | **1,400 Md€** |

Les colonnes `E` et `F` portent la même construction aux mêmes rangs.

**Recoupement avec `methode/etats/APP_etatB.md`, § 1.2** : cet état porte les quatre lignes
« autres » à 2,6 opérateurs · 0,9 chèques · 1,2 entreprises · 1,4 associations. **Les quatre
concordent à la décimale avec la mesure prise ici.** Le périmètre des quatre résidus est donc
stable entre les deux fils, et la ventilation non jouée d'`APP_etatB` porte bien sur ces
montants-là.

**Ce que le point établit, et qui reste dû** : tant que `D4`, `D17`, `D23` et `D28` sont des
entrées, toute correction d'une ligne nommée se répercute **en sens inverse** sur la ligne
« autres » du même bloc, sans que rien le signale. C'est la mécanique qui a laissé 14 500
survivre. **Le retournement — totaux en sorties, résidus en entrées — n'est pas appliqué**, même
motif qu'au point 1.

### Point 4 — `Détail Economies!A16` n'a pas de code → **joué, et le constat est contredit par la mesure**

**Mesure sur la pièce jointe `Synthèse Calculs Résolution_0910.xlsx`** :
`Détail Economies!A16` = **`O`**. La cellule porte un code, et c'est le code du bloc opérateurs.

Le résidu entre donc bien dans les `SUMIFS` d'`Annexe Manuscrit`, et le contrôle le prouve par
réapplication : `Annexe Manuscrit!E8` = `=SUMIFS('Détail Economies'!D:D,'Détail Economies'!$A:$A,"O")-1.052*42/48*10/3`.
Somme des `D` où `A` vaut `O`, **ligne 16 comprise** : 1,3 + 0,7 + 0,7 + 0,6 + 0,3 + 0,3 + 0,2 +
1,3 + **2,6** = 8,0 ; moins 3,068 333 → **4,931 666 7**, qui est exactement la valeur en cache de
`E8`. Sans la ligne 16, la réapplication rendrait 2,331 7 et ne concorderait pas.

Les trois autres résidus portent eux aussi leur code : `A22` = `M`, `A27` = `E`, `A36` = `A`.

**Verdict** : sur le classeur de référence du projet, le point 4 n'a pas d'objet. Deux lectures
possibles, et le fil ne tranche pas — soit le constat visait
`Synthèse Calculs Résolution_corrige_20261007.xlsx`, que `suivi_depenses` § 6.1 déclare fautif et
que ce fil n'a pas ouvert, soit il s'agit d'un constat erroné. **À retirer du reste dû** dès que
l'un des deux est établi.

### Point 5 — Descendre la jointure au bénéficiaire via `Opérateurs R` → **joué en mesure, jointure non construite**

`Opérateurs R` est une feuille de la pièce jointe `Synthèse ETP et agences Résolution_0910.xls`.
**Mesure du grain** :

| compte | valeur |
|---|---:|
| lignes de données opérateur × programme | **180** (et non 184 : 184 est le nombre de lignes de la feuille) |
| opérateurs portés (colonne `Nb/cat.`) | **434** |
| programmes distincts | **54** |
| missions distinctes | **24** |
| ETPT PLF 2026, total | **478 026** |
| lignes sans sort qualifié | **0** |

Sorts qualifiés, un par ligne : EPIC-études 50 · EPIC-musée 36 · Suppression 55 ·
Internalisation 24 · Vente 15.

**Ce que la mesure établit, et c'est le point dur.** Le grain bénéficiaire existe et il est
complet sur son périmètre — chaque ligne nomme un opérateur, son programme, sa mission, son
sort. **Mais il porte des emplois, non des crédits** : les colonnes utiles sont des ETPT, sous
plafond et hors plafond. Nommer un opérateur dans un exposé est donc possible ; **chiffrer sa
subvention depuis cette feuille ne l'est pas**. Et le périmètre ne couvre que **54 programmes sur
les 162 de la table A**.

**La jointure n'est pas construite** : elle produirait une pièce nouvelle, que le mandat ne nomme
pas, et la table A qui en est l'autre moitié est portée par le classeur absent (§ 3).

### Point 6 — Qualifier les 12 programmes à trois jambes → **non joué, faute d'objet**

La liste des 12 programmes, la table A, la table B et la jointure vivent toutes dans
`Suivi dépenses — crédits et vecteurs_20261007.xlsx`, que le mandat nomme comme pièce de travail.

**Mesure de présence, prise par recherche nominative** : le classeur n'est **ni une pièce jointe
du projet** (les 8 pièces jointes sont nommées, il n'y est pas), **ni un document du projet**
(une recherche nominative ne le rend pas ; `suivi_depenses` le cite comme son propre livrable),
**ni présent sur le disque de l'atelier**. **Compte : 0.**

Conformément à la règle du projet — une mesure qui ne trouve pas l'objet annoncé rend le nombre
mesuré et s'arrête, sans jouer de contrôle, sans chercher ailleurs, sans élargir son périmètre —
**le point 6 n'est pas joué et la table A n'est pas reconstruite**. Elle le serait depuis
`Données PAP 2026`, `Economies R`, l'annexe 2 des taxes affectées et l'annexe 3 des dépenses
fiscales : c'est une passe entière, elle appelle son propre mandat.

---

## 3. Références laissées hors contrôle, et la raison de chacune

| ensemble | nombre | raison |
|---|---:|---|
| `Suivi dépenses — crédits et vecteurs_20261007.xlsx` : 8 feuilles, 4 422 formules | 1 classeur | **absent du projet et de l'atelier** — mesure nominative à 0. Il porte à lui seul les tables A et B, la jointure, la règle de proxy AE/CP et la liste des 34 programmes non classés |
| tables A (718 lignes) et B (B1 278 lignes, B2 465 lignes), jointure à 162 programmes, 12 programmes à trois jambes | 1 473 lignes | portées par le classeur ci-dessus, non rejouées ; rien n'en est repris comme acquis dans cet état |
| règle de proxy AE/CP, 12 niveaux de ratio | 12 | même cause ; les seuils de `suivi_depenses` § 5.1 ne sont ni confirmés ni infirmés ici |
| `Synthèse Calculs Résolution_corrige_20261007.xlsx` | 1 classeur | déclaré fautif par `suivi_depenses` § 6.1 (« ne pas le verser en l'état ») : non ouvert, délibérément |
| `Réconciliation budgétaire-taxes affectées_20261007.xlsx` | 1 classeur | déclaré remplacé par `suivi_depenses` § 6.2 : non ouvert |
| texte BIFF des formules `H8` et `F32` | 2 | l'instrument de lecture en cache ne rend pas le texte d'une formule `.xls` ; la preuve est prise par réapplication, qui concorde à la dernière décimale. Un recalcul par moteur tiers aurait rendu le texte et falsifié les valeurs — il a été écarté |
| adresses de droit en vigueur | 0 visée | aucune disposition n'est écrite par cette passe, aucun article n'est visé à un dispositif : il n'y a rien à contrôler au dépôt de droit, et le compte de 0 est le compte exact |
| skills `vecteur-mesure` et `disposition-cible`, nommées au mandat | 2 | **non activées** : aucun siège juridique n'était à relever et aucune disposition à rédiger, le mandat interdisant de rédiger un amendement. Déclaré plutôt que joué pour la forme |

**Lecture de ce compte.** Sept des huit ensembles tiennent à une seule et même cause — **la pièce
de travail nommée au mandat n'est pas là**. L'instrument est en cause avant le texte. Les deux
points du § 7 qui en dépendent (5 pour sa moitié crédits, 6 en entier) sont les seuls à ne pas
aboutir.

---

## 4. Mesure de sortie — le mandat point par point

| n° | point du mandat | verdict | compte |
|---|---|---|---|
| 0 | ouvrir `appui_des_passes` et `suivi_depenses` ; appui `regles_credits` | **tenu** | 3 pièces ouvertes et lues intégralement |
| 0 bis | **R-G** — ouvrir les états de la même matière du même jour et les nommer à l'`Appui` | **tenu** | `APP_etatB`, `CROISEMENTS_20261007`, `cr_consolidation_20261007`, les 3 lus intégralement avant la passe et nommés à l'`Appui` ; un recoupement utile en est sorti (§ 2, point 3) et un blocage en est levé (§ 1.4) |
| 0 ter | skills `confrontation`, `vecteur-mesure`, `disposition-cible`, `resolution-chantier` | **tenu en partie, et déclaré** | 2 activées et appliquées ; 2 non activées, sans objet au mandat — voir § 3 |
| 1 | **mesurer `SynthèseR!H8` et `SynthèseR!F32` et rendre le compte avant toute écriture** | **joué** | les 2 cellules portent une valeur · les 2 formules **concordent par réapplication à la dernière décimale** · les 2 défauts confirmés et chiffrés : +1 371,125 2 et −215,677 609 1 M€ · lecture en cache, **aucun recalcul tiers** · aucune écriture avant ce compte |
| 1 bis | — effet de bord | **blocage levé** | `cr_consolidation` § 5.2 tombe : `SynthèseR` est au `.xls` des dépenses, non à `Synthèse Calculs` |
| 2 | § 7.1 — poser `H8` et `F32` | **rendu en clair, non appliqué** | 2 divisions écrites avec leur valeur attendue ; le porteur est une pièce jointe en lecture seule et le mandat ne nomme aucune pièce de sortie autre que cet état |
| 3 | § 7.2 — relier `Détail Economies` et `Flux`, passer les totaux en sommes | **joué en mesure, non appliqué** | lien mesuré **en sens inverse** de l'attendu · 3 totaux en dur confirmés · **3 divergences nouvelles** : `E15` +45,3 M€, `C22` et `G22` −100 M€ · 9 divisions rendues en clair |
| 4 | § 7.3 — mesurer les résidus au lieu de les caler | **joué, confirmé à la lettre** | 4 formules de solde relevées · 4 résidus mesurés : 2,6 · 0,9 · 1,2 · 1,4 Md€ · **concordent à la décimale avec `APP_etatB` § 1.2** |
| 5 | § 7.4 — `Détail Economies!A16` n'a pas de code | **joué, et le constat est contredit** | `A16` = `O` ; le résidu entre dans le `SUMIFS` d'`Annexe Manuscrit!E8`, prouvé par réapplication (4,931 666 7, concorde). Sans objet sur le classeur de référence |
| 6 | § 7.5 — descendre la jointure au bénéficiaire via `Opérateurs R` | **joué en mesure, jointure non construite** | 180 lignes · 434 opérateurs · 54 programmes · 24 missions · 478 026 ETPT · 0 ligne sans sort. **La feuille porte des emplois, non des crédits**, et couvre 54 programmes sur 162 |
| 7 | § 7.6 — qualifier les 12 programmes à trois jambes | **non joué — objet absent** | la pièce de travail du mandat est absente, mesure nominative à **0**. Le fil rend le nombre et s'arrête : il ne reconstruit pas la table A |
| 8 | **ne rédiger aucun amendement** | **tenu** | 0 amendement, 0 disposition, 0 exposé |
| 9 | ne réécrire aucune pièce du paquet | **tenu** | 0 pièce du paquet touchée · 11 divisions rendues en clair, aucune appliquée |
| 10 | rendre le compte des références hors contrôle et la raison de chacune | **tenu** | 8 ensembles, § 3 |
| 11 | mesure de sortie reprenant le mandat point par point, « non joué » compris | **tenu** | le présent § 4 |
| 12 | trois questions fermées au plus | **tenu** | 3, § 6 |

---

## 5. Reste dû, hors de ce fil

- **Les deux divisions de `SynthèseR`** et les **neuf divisions de `Flux`**, rendues en clair aux
  points 1 et 2, restent à appliquer. Elles supposent un classeur nouveau, donc un go.
- **Le retournement des quatre blocs** de `Détail Economies` — totaux en sorties, résidus en
  entrées — n'est pas joué, et c'est la correction de fond du point 3.
- **La ventilation des trois lignes « autres »** encore non ventilées — opérateurs 2,6, chèques
  0,9, entreprises 1,2 Md€ — reste due à `APP_etatB` ; les montants sont maintenant confirmés sur
  pièce.
- **La table A et la jointure à 162 programmes** sont à reconstruire si le classeur du 20261007
  ne revient pas. C'est une passe entière, elle appelle son propre mandat.
- **L'écart de 100 M€ sur le bloc collectivités** (`Flux!C22` et `G22`) n'est imputé à aucune des
  quatre lignes locales : il se tranche avant tout chiffrage public de ce bloc.

---

## 6. Questions fermées pour l'auteure

1. **Le classeur `Suivi dépenses — crédits et vecteurs_20261007.xlsx` n'est pas au projet.**
   Le versez-vous en pièce jointe, ou la table des crédits et des vecteurs se refait-elle depuis
   les classeurs sources, en une passe à part ?

2. **Les corrections de formule sont écrites, pas appliquées** — deux dans `SynthèseR`, neuf dans
   `Flux`. Donnez-vous le go pour produire un classeur corrigé qui les porte, ou les garde-t-on en
   clair dans cet état jusqu'à un chiffrage qui en ait besoin ?

3. **Le bloc collectivités de `Flux` porte 33,3 Md€ en année 1, et ses quatre lignes somment à
   33,4.** Lequel des deux fait foi — le total, ou les lignes ?
