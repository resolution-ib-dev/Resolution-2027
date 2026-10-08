# État du fil classeur — chiffrage, dépôt 2027, 20261007

**Porteur** : fil Cowork classeur, dépôt 2027, 20261007. Matière unique : le chiffrage.
**Mandat** : l'auteure, 20261007 — mesurer `SynthèseR!H8`, `E21`, `H21`, `F32` et rendre le compte
avant toute écriture ; poser les deux formules dans un classeur produit à part ; relier
`Détail Economies` et `Flux` à `SynthèseR` et passer `Flux!C15`, `E15` et les totaux de bloc en
sommes ; mesurer les quatre résidus au lieu de les caler ; reprendre les trois divergences du fil
précédent ; relever les treize cellules dues avant dépôt. Ne toucher aucune pièce du paquet,
aucun registre, aucun exposé. N'inventer aucun montant.
**Domicile** : `methode/etats/APP_classeur_20261007.md`.
**Appui**, au titre de **R-G** — états de la même matière et du même jour, tous ouverts et lus
intégralement avant la passe : `methode/suivi_depenses_20261007.md` (§ 2 et § 7) ·
`methode/etats/REPRISE_depenses_20261007.md` · `methode/passation_20261007.md` (§ 5.2 et § 5.3) ·
`methode/appui_des_passes.md` · `methode/etats/APP_etatB.md`. Skill `resolution-chantier` activée.
Pièces jointes ouvertes, en **lecture seule** : `PLF26 - Depenses 2026 du BG et des BA selon
nomenclatures destination et nature_0910.xls` · `Synthèse Calculs Résolution_0910.xlsx`.
**Mesure** : 4 cellules mesurées, **4 portent une valeur** · 2 formules posées, effet net
**+1 155,4 M€** sur l'économie totale · **96 cellules** passées en formule ou en entrée · 3
divergences du fil précédent reprises, **2 confirmées, 1 étendue** · **1 divergence nouvelle
relevée dans `REPRISE` elle-même** · 4 résidus retournés · **13 cellules relevées, 13 résolvent**
· 7 ensembles de références laissés hors contrôle · 1 classeur produit · **0 pièce jointe
touchée, 0 pièce du paquet, 0 registre, 0 exposé** · 3 questions fermées.

---

## 1. Mesure d'entrée — rendue avant toute écriture

**Instrument** : `xlrd` sur le `.xls` d'origine, **valeurs de cache, aucun recalcul tiers**
(règle 5.3 de `suivi_depenses`). `SynthèseR` est bien une feuille du classeur des dépenses ;
les cinq feuilles sont `SynthèseR`, `Economies R`, `Données PAP 2026`, `Crédits RAP 2024`,
`Emplois RAP 2024`.

| cellule | objet | valeur en cache |
|---|---|---:|
| `SynthèseR!H8` | subventions aux opérateurs, au-delà d'1 an | **3 609,601 876 62** |
| `SynthèseR!E21` | Anah, au-delà d'1 an | **53,518 5** |
| `SynthèseR!H21` | Autres opérateurs, au-delà d'1 an | **1 317,606 713 955 000 5** |
| `SynthèseR!F32` | résidu « Autres », chèques aux ménages, à 1 an | **1 820,310 233 310 006** |

**Les quatre résolvent. Aucune n'est morte.** Le compte est rendu ; l'écriture commence après.

---

## 2. Le classeur produit

**`Chiffrage corrigé Résolution_20261007.xlsx`**, à la racine de l'atelier. Nom distinct de
`Synthèse Calculs Résolution_corrige_20261007.xlsx`, qui porte la faute du § 6.1 de
`suivi_depenses` et **n'a pas été ouvert**.

Il part de `Synthèse Calculs Résolution_0910.xlsx` et y importe **en valeurs de cache** les deux
feuilles `SynthèseR` et `Economies R` du `.xls`. Les liens sont donc **internes** : aucun renvoi
externe vers une pièce jointe, aucune pièce jointe modifiée. Dix feuilles, dont une feuille
`Contrôle 20261007` qui porte les 96 cellules avant/après, les quatre résidus, les écarts de
reconstruction, les treize cellules et les références hors contrôle.

**Preuve de la passe** : le classeur a été recalculé deux fois et rend les mêmes valeurs aux deux
passages. Le recalcul tiers n'intervient qu'**après** la mesure d'entrée, pour éprouver des
formules posées — jamais pour établir l'existence d'une valeur.

---

## 3. Mandat point par point — verdict, et effet chiffré

### Point 1 — Poser les deux formules → **joué**

| cellule | formule posée | avant | après | effet |
|---|---|---:|---:|---:|
| `SynthèseR!H8` | `=C21+D21+E21+F21+G21+H21` | 3 609,601 876 62 | **4 980,727 090 575** | **+1 371,125 213 955** |
| `SynthèseR!F32` | `=('Economies R'!S4-C31-'Economies R'!R155-F20-'Economies R'!R177-197,995)*0,9` | 1 820,310 233 310 006 | **1 604,632 624 200 01** | **−215,677 609 110** |

`H8` est écrite comme la somme de la ligne 21 du bloc de détail — `C21` vaut `C20*7/3` à l'octet
(2 454,48), et la forme en somme fait entrer `E21` (Anah) et `H21` (Autres) que la formule
d'origine omettait. **Contrôle de bouclage** : avec `H8` corrigée, `H6 = H7 + H8` vaut
**11 360,679 542**, qui est exactement la somme de la ligne `Total` du bloc opérateurs
(`C19:H19`). Le bloc ferme ; il ne fermait pas avant.

**Divergence relevée dans `REPRISE_depenses_20261007.md`, § 2, point 1.** Cet état annonce pour
`F32` une « valeur attendue **2 035,987 842 420 006** (1 820,310 233 310 006 + 215,677 609 11) ».
**L'addition est fausse** : la correction remplace `D31` (1 094,67) et `E31` (1 062,106 091 1) par
leurs bruts `R155` (1 216,30) et `R177` (1 180,117 879), donc elle **retranche davantage** de la
base. Réapplication : 21 827,398 682 − 16 116,735 643 − 1 216,30 − 1 333,325 022 − 1 180,117 879
− 197,995 = 1 782,925 138, × 0,9 = **1 604,632 624**. Le signe rendu est celui que
`suivi_depenses` § 2 et `REPRISE` § 1.3 portent tous deux — **−215,7 M€**. Seule la ligne
« valeur attendue » de `REPRISE` § 2 est à corriger.

**Effet des deux corrections sur les agrégats de tête de `SynthèseR`** :

| agrégat | avant | après | effet |
|---|---:|---:|---:|
| `C6` économie totale restituée | 82 473,203 8 | **83 628,651 4** | **+1 155,447 605** |
| `C7` économie à 1 an | 44 206,085 1 | **43 990,407 5** | **−215,677 609** |
| `C8` économie au-delà d'1 an | 38 267,118 7 | **39 638,243 9** | **+1 371,125 214** |

Par surcroît, et par réapplication confirmée à l'octet sur les valeurs d'origine, les agrégats
`C6:K8` et les lignes `Total` des quatre blocs de détail (19, 25, 31, 37) sont passés en sommes :
`H7`, `I7`, `I8`, `J7`, `J8`, `K7`, `K8` redonnent leur valeur en cache à la dernière décimale
avant correction. `F31` suit `F32` et passe à 1 604,632 624. Restent des **entrées** : `G7` et
`G8` (taxes affectées, portées par `Synthèse TA`, classeur non monté), `D7`, `D8`, `D9`, `D10`
(salaires et ETP), qu'aucun bloc de détail ne reconstruit.

### Point 2 — Relier `Détail Economies` et `Flux` à `SynthèseR`, totaux en sommes → **joué**

**Le sens du lien est celui qu'a mesuré `REPRISE`** : `Détail Economies` descendait de `Flux`, et
`Flux` était en dur. Le point de vérité est désormais `SynthèseR`, et il descend.

`Flux!C16:C21` ← ligne 7 de `SynthèseR` ; `E16:E21` ← ligne 8 ; `G16:G21` = `C+E`. `C15`, `E15`,
`G15`, `C22`, `E22`, `G22`, `C8`, `E8`, `G8` passent en `SUM` de leurs composantes.

| cellule | avant | après | effet |
|---|---:|---:|---:|
| `Flux!C15` économies État, an 1 | 44,0 **en dur** | **43,990 407** | −9,6 M€ |
| `Flux!E15` supplémentaire à terme | 38,5 **en dur** | **39,638 244** | **+1 138,2 M€** |
| `Flux!G15` total à terme | 82,5 | **83,628 651** | **+1 128,7 M€** |
| `Flux!C22` collectivités, an 1 | 33,3 **en dur** | **33,4** | **+100 M€** |
| `Flux!E22` | 20,1 | 20,1 | 0 |
| `Flux!G22` | 53,4 **en dur** | **53,5** | **+100 M€** |
| `Flux!C6` total général an 1 | 129,4 | **129,490 407** | +90,4 M€ |
| `Flux!E6` | 96,7 | **97,838 244** | +1 138,2 M€ |
| `Flux!G6` | 226,2 | **227,428 651** | +1 228,7 M€ |

**Ligne à ligne, l'écart entre la valeur arrondie en dur et le lien** (M€) : opérateurs an 1
−0,05, ménages **+25,6**, entreprises +3,5, associations −10,7, charges courantes −15,5, départs
−12,4 ; à terme supplémentaire : **opérateurs +1 329,1**, ménages −47,4, entreprises −49,2,
associations −20,0, départs −28,9. Tous sont des arrondis sauf deux, qui sont des divergences de
fond et sont traitées au point 4 et au § 4.

### Point 3 — Mesurer les résidus au lieu de les caler → **joué, retournement appliqué**

Les quatre lignes « autres » de `Détail Economies` étaient des **soldes** : `D16 = D4−SUM(D5:D15)`
et ses trois homologues, le total de bloc étant une entrée. **Le sens est retourné** : le total
devient une sortie (`D4 = SUM(D5:D16)`), le résidu une entrée, figée à la valeur mesurée ce jour.

| bloc | ligne | D — année 1 | E — supp. à terme | F — total |
|---|---|---:|---:|---:|
| opérateurs | 16 | **2,600 000** | 0,200 000 | 2,745 333 |
| chèques aux ménages | 22 | **0,900 000** | 0,100 000 | 1,000 000 |
| aides aux entreprises | 27 | **1,200 000** | 0,100 000 | 1,300 000 |
| subventions aux associations | 36 | **1,400 000** | 0,000 000 | 1,400 000 |

Les quatre concordent à la décimale avec `APP_etatB` § 1.2 et avec `REPRISE` § 2 point 3.
`D3`, `E3`, `F3` passent en sommes des six totaux de bloc : la feuille se reconstruit désormais
**du bas vers le haut**, et ne peut plus absorber une correction en sens inverse sans le dire.
`Détail Economies!D39` et `F39` passent en sommes et portent l'écart des collectivités
(33,4 et 53,5).

**Ce que le retournement rend visible — et qui n'était mesurable d'aucune façon avant** : l'écart
entre la reconstruction ascendante et le point de vérité.

| jambe | `Détail Economies` | `Flux` (= `SynthèseR`) | écart |
|---|---:|---:|---:|
| année 1 | 44,000 000 | 43,990 407 | **+9,6 M€** |
| supplémentaire à terme | 38,454 667 | 39,638 244 | **−1 183,6 M€** |
| total à terme | 82,500 000 | 83,628 651 | **−1 128,7 M€** |

Le premier est de l'arrondi. **Les deux autres sont la correction de `H8` qui n'est pas redescendue
dans le détail** : la jambe au-delà d'un an des subventions aux opérateurs a gagné 1 371,1 M€ à
`SynthèseR`, et aucune ligne nommée de `Détail Economies` ne la porte. C'est une ventilation due,
non un défaut de formule. **Question fermée n° 1.**

**Contrôle de non-régression** : `Annexe Manuscrit!E8`, qui agrège par `SUMIFS` sur le code `O`,
rend **4,931 666 7** après la passe comme avant. La ligne 16 porte bien son code et le retournement
ne l'a pas sortie du périmètre.

### Point 4 — Les trois divergences du fil précédent → **2 confirmées, 1 étendue**

| divergence | verdict |
|---|---|
| `Flux!E15` **+45,3 M€** | **confirmée** à l'identique : 38,5 en dur contre 38,454 667 de somme. Elle est **absorbée et dépassée** par le lien à `SynthèseR` : `E15` vaut désormais 39,638 244, et l'écart réel au point de vérité est **−1 138,2 M€**, non +45,3 |
| `Flux!C22` **−100 M€** | **confirmée** : 33,3 en dur, quatre lignes locales à 33,4. Corrigée en somme |
| `Flux!G22` **−100 M€** | **confirmée, et étendue** : le même écart de 100 M€ est porté par `Détail Economies!D39` et `F39`, qui étaient en dur à 33,3 et 53,4 sans lien avec `Flux`. **Deux feuilles portaient le même faux total à deux endroits.** Les deux sont corrigées |

**Le fond n'est pas tranché** : l'écart de 100 M€ est imputé au total, non aux lignes — le classeur
corrigé fait désormais foi des lignes. **Question fermée n° 2.**

### Point 5 — Les treize cellules dues avant dépôt → **relevées, 13 sur 13 résolvent**

Relevées sur la pièce jointe `Synthèse Calculs Résolution_0910.xlsx`, dans son état d'origine.
Le blocage 5.3 de `passation_20261007.md` est levé.

| feuille | cellule | objet | valeur | verdict |
|---|---|---|---:|---|
| `Détail Economies` | `D12` | Ademe | 0,3 Md€ | résout |
| `Détail Economies` | `D14` | Agence nationale de l'habitat | 0,2 Md€ | résout |
| `Détail Economies` | `D15` | MaPrimeRénov' | 1,3 Md€ | résout |
| `Détail Economies` | `D18` | APL | 5,4 Md€ | résout |
| `Détail Economies` | `D20` | chèque énergie | 0,6 Md€ | résout |
| `Détail Economies` | `D29` | hébergement d'urgence | 2,5 Md€ | résout |
| `Détail Economies` | `D31` | immigration et asile | 0,9 Md€ | résout |
| `Détail Economies` | `D34` | subventions culturelles | 0,5 Md€ | résout |
| `Détail Economies` | `D35` | politique de la ville | 0,4 Md€ | résout |
| `Détail Economies` | `D38` | départs fonctionnaires État | 0,9 Md€ | résout — **le libellé porte « départs », l'arbitrage du lot 15 dit « fermetures de postes »** |
| `Détail Economies` | `G38` | hypothèse de `D38` | « Hors régalien et éducation, 90 % de départs, 70 % salaire maintenu » | résout — c'est une hypothèse, non un montant |
| `Détail Economies` | `J38` | ETP État supprimés | 61 400 | résout — **`SynthèseR!D9` porte 61 391,982 7 : écart de 8,02 ETP entre les deux classeurs** |
| `Flux` | `C17` | chèques aux ménages, année 1 | 8,4 Md€ | résout — **contredit par `SynthèseR!I7`, qui vaut 8,425 583 après correction : +25,6 M€** |

**Aucune des treize ne manque.** Trois portent un verdict au-delà de leur valeur : `D38` et `G38`
sur le libellé, `J38` sur l'écart d'ETP, `C17` sur l'écart de montant. Les montants repris des
pièces antérieures de `APP_etatB` sont **confirmés à la décimale** ; aucun amendement d'état B ne
bouge de ce fait.

### Points tenus par interdiction

| point | verdict |
|---|---|
| ne toucher aucune pièce jointe | **tenu** — 0 écriture ; le classeur produit est un fichier nouveau |
| ne toucher aucune pièce du paquet, aucun registre, aucun exposé | **tenu** — 0, 0, 0 |
| ne pas reprendre `Synthèse Calculs Résolution_corrige_20261007.xlsx` | **tenu** — non ouvert |
| n'inventer aucun montant | **tenu** — tout chiffre de cet état porte sa cellule |

### Non joué

| point | raison |
|---|---|
| ventiler les 1 371,1 M€ de `H8` sur les lignes nommées de `Détail Economies` | hors mandat, et c'est une question de fond — § 5, question 1 |
| imputer les 100 M€ du bloc collectivités à l'une des quatre lignes locales | hors mandat — § 5, question 2 |
| reconstruire la table A et la jointure à 162 programmes | la pièce `Suivi dépenses — crédits et vecteurs_20261007.xlsx` reste **absente**, mesure nominative à 0. Le fil rend le nombre et s'arrête |
| relier `Synthèse TA` à `SynthèseR!G7` et `G8` | classeur non monté sur ce fil |

---

## 4. Références laissées hors contrôle, et la raison de chacune

| ensemble | nombre | raison |
|---|---:|---|
| `Economies R` : 206 lignes × 25 colonnes | 1 feuille | importée en valeurs de cache ; **3 cellules seules contrôlées** — `S4`, `R155`, `R177` — les autres n'étant opérandes d'aucune formule posée |
| `Données PAP 2026`, `Crédits RAP 2024`, `Emplois RAP 2024` | 3 feuilles, 4 085 lignes | non importées ; aucune formule posée ne les vise |
| `Synthèse TA` : `SynthèseR!G7` et `G8` | 2 cellules | classeur porteur non monté ; elles restent des entrées, et la jambe taxes affectées n'est donc pas reconstruite |
| `SynthèseR!D7`, `D8`, `D9`, `D10` | 4 cellules | salaires et ETP ; aucun bloc de détail ne les reconstruit, elles restent des entrées |
| texte BIFF des formules du `.xls` | toutes | l'instrument de lecture en cache ne le rend pas ; la preuve des deux formules d'origine est prise par réapplication, confirmée à la dernière décimale par `REPRISE` § 1.2 |
| `Suivi dépenses — crédits et vecteurs_20261007.xlsx` | 1 classeur | **toujours absent** du projet et de l'atelier — mesure nominative à 0 |
| `Synthèse Calculs Résolution_corrige_20261007.xlsx` | 1 classeur | déclaré fautif par `suivi_depenses` § 6.1 ; **non ouvert, délibérément** |

**Lecture de ce compte** : aucun des sept ne tient à une faute de lecture. Quatre tiennent à un
périmètre que le mandat ne nomme pas, deux à un classeur absent ou écarté, un à l'instrument.

---

## 5. Questions fermées

1. **La correction de `H8` ajoute 1 371,1 M€ à la jambe au-delà d'un an des opérateurs, et aucune
   ligne nommée de `Détail Economies` ne la porte** — l'écart apparaît en bloc. Ces 1 371,1 M€
   vont-ils à la ligne « autres » du bloc opérateurs, ou se ventilent-ils sur les lignes nommées ?

2. **Le bloc collectivités porte 33,3 Md€ en année 1 et ses quatre lignes somment à 33,4** ; le
   classeur corrigé fait foi des lignes. Confirmez-vous que ce sont les lignes qui valent, ou le
   total de 33,3 est-il l'arbitrage ?

3. **`J38` porte 61 400 ETP et `SynthèseR!D9` en porte 61 391,98** ; les amendements de titre 2
   de `etatB_04` sont bâtis sur 61 400. Garde-t-on 61 400 comme chiffre arrêté, le classeur étant
   alors en écart de 8 ETP ?

---

## 6. Reste dû, hors de ce fil

- **Ventilation des 1 371,1 M€** et **imputation des 100 M€**, après réponse aux questions 1 et 2.
- **Correction de `REPRISE_depenses_20261007.md` § 2, point 1** : la « valeur attendue » de `F32`
  y est portée à 2 035,99 par addition, quand la correction retranche. La bonne valeur est
  **1 604,632 624**.
- **Jambe taxes affectées** : relier `Synthèse TA` à `SynthèseR!G7` et `G8` demande que le
  classeur des taxes affectées soit monté — passe à part.
- **Table A et jointure à 162 programmes** : la pièce de travail reste absente.
- **Recalage du libellé « départs » en « fermetures de postes »** à `Détail Economies!D38` et
  `G38` — matière d'exposé, hors de ce fil.

---

## 7. Ligne de lancement du fil suivant

Fil **de conversation** — il tranche, il ne déplie rien.

> Arbitrage du chiffrage après la passe classeur du 20261007 — ouvrir
> `methode/etats/APP_classeur_20261007.md` ; trancher les trois questions fermées du § 5 ;
> ne produire aucune pièce.
