# Conduite de la chaîne — de l'énoncé à l'amendement déposable

Écrite le 20261016 pour un utilisateur extérieur, dans un atelier Claude qui
dispose d'un terminal. Elle ne suppose aucune doctrine, aucun corpus, aucun
projet d'origine : seulement cette procédure, les outils qu'elle nomme, et le
dépôt public de droit.

---

## 0. Le contrat

**Vous donnez un énoncé en français ordinaire. La chaîne rend un amendement
déposable, ou elle dit pourquoi elle n'y arrive pas.** Elle ne devine jamais, et
elle ne vous rend jamais une pièce dont une étape n'a pas conclu.

**Trois choses qu'elle ne fera pas à votre place**, et c'est écrit ici pour que
vous ne le découvriez pas en séance :

1. **décider de la mesure** — elle porte une méthode, pas une opinion ;
2. **chiffrer** — un montant se relève à l'annexe de l'exercice, par vous ;
3. **plaider la recevabilité** — elle instruit, elle ne décide pas (§ 3, `E1`).

**Un seul arrêt est bloquant** : `hors_capacite`. Une étape qui ne sait pas
conclure l'écrit, et la chaîne s'arrête là. Tous les autres arrêts sont à votre
main : si vous ne répondez pas, la chaîne continue en portant son incertitude en
clair.

---

## 1. La boucle, en une page

```
énoncé  →  E0 qualifier  →  E1 rattacher  →  E2 vecteur  →  E3 droit
                                                                ↓
liasse  ←  E7  ←  E6 contrôles  ←  E5 exposé  ←  E4bis gage  ←  E4 rédiger
   ↓
 .docx
```

| étape | ce qu'elle rend | outil |
|---|---|---|
| **E0** | la nature de la mesure et son véhicule | la présente procédure |
| **E1** | un verdict de rattachement, motivé sur pièce | `03_PROCEDURE_rattachement.md` — **à votre main** |
| **E2** | l'article à modifier, ou `introuvable` | `10_OUTIL_vecteur_mesure.md` |
| **E3** | le texte en vigueur, en verbatim | `depot/droit.py` |
| **E4** | le texte cible, puis la disposition modificative | `11_OUTIL_disposition_cible.md` |
| **E4bis** | la clause de gage, ou l'insuffisance chiffrée | `05_PROCEDURE_gage.md` |
| **E5** | l'exposé sommaire | `12_OUTIL_expose_sommaire.md` |
| **E6** | les contrôles joués et leur verdict | `41_SCRIPT_controles_expose.py` |
| **E7** | la liasse assemblée, puis son `.docx` | `40_SCRIPT_imprimer_liasse.py` |

---

## 2. Le dossier de mesure

Une mesure, un fichier. Il s'ouvre à `E0` et se remplit étape par étape. **Rien
ne s'écrit ailleurs** : pas de notes dans le fil, pas de mémoire implicite.

```
mesure: <l'énoncé, mot pour mot>
vehicule: PLF | PLFSS | loi ordinaire | a_determiner
ouvert: AAAAMMJJ

## E0 — qualification
verdict:
doutes:

## E1 — rattachement
verdict:        rattachable | plaidable | fragile | non_rattachable
canal:
piece:
contrefactuel:
doutes:

## E2 — vecteur
adresse:
etat:           trouve | a_trouver | introuvable
doutes:
```

**Trois règles de remplissage, et elles valent pour toutes les étapes.**

- **`doutes` vaut `aucun` ou il nomme le doute.** Vide n'est pas une réponse.
- **Une étape qui ne conclut pas écrit `hors_capacite` et s'arrête.** Elle ne
  passe pas la main en espérant que la suivante rattrape.
- **Aucune étape ne réécrit une étape antérieure.** Si `E4` découvre que le
  vecteur de `E2` est faux, elle le dit et la chaîne remonte à `E2`. Elle ne
  corrige pas en passant.

---

## 3. Les étapes, une à une

### E0 — Qualification

Lit l'énoncé. Rend la nature de la mesure — suppression de recette, création de
recette, modification de dépense, mesure d'organisation — et le véhicule.

Sur un véhicule que l'énoncé ne dit pas, elle porte `a_determiner` et le
qualifie : une mesure de prélèvement obligatoire affecté à la sécurité sociale
va au texte de financement, le reste au texte de finances. **Une qualification
devinée empoisonne les six étapes suivantes** : sur un doute réel, `hors_capacite`.

### E1 — Rattachement

**C'est la dépendance la plus lourde de la chaîne, et elle reste à votre main.**
Un amendement peut être parfait et irrecevable ; une disposition impeccable sur
une mesure hors domaine est perdue entière.

La procédure est à `03_PROCEDURE_rattachement.md`, et elle se joue sur pièce :
quatre canaux parcourus un par un, chacun documenté — l'état, l'annexe, le
tableau d'équilibre — **et jamais l'exposé des motifs**, qui n'engage personne.

**Trois décisions sont les vôtres**, et aucun outil ne les prendra : le
contrefactuel entre droit constant et tendanciel ; le seuil au-delà duquel un
verdict `fragile` coûte en crédibilité plutôt qu'en articles ; l'emploi de
l'argument tiré de l'article 33 de la loi organique, qui est le plus fort du
test et à double tranchant.

**Ce qui se joue gratuitement, et que presque personne ne fait** : le précédent.
Le point d'accès public aux amendements déposés porte le sort de chacun —
irrecevable, retiré, rejeté, adopté. **Un amendement voisin déclaré recevable
est la meilleure preuve disponible.** Cherchez-le avant de plaider.

Sur `non_rattachable`, la chaîne s'arrête : la mesure part dans un autre
véhicule, et c'est une autre chaîne.

### E2 — Vecteur

Trouve le siège juridique : l'article que la mesure modifie. Procédure à
`10_OUTIL_vecteur_mesure.md`.

**Le vecteur se trouve, il ne se devine pas.** Sur `a_trouver`, la chaîne
s'arrête : une mesure rattachable sans vecteur est une mesure qu'on ne sait pas
écrire, et une adresse approchée produit un amendement inopérant que rien ne
signalera.

### E3 — Droit applicable

```
python3 depot/droit.py article "<intitulé du code>" "<numéro d'article>"
```

Rend le **verbatim** du texte en vigueur, avec son identifiant de version et sa
date. **La base lève sur un article absent plutôt que d'en rendre un voisin** :
une absence est une information, pas un échec.

**Deux arrêts propres à cette étape.** L'extrait périmé : au-delà de quarante-cinq
jours, la base imprime `À REJOUER` et la chaîne s'arrête — on ne rédige pas sur
un droit dont on ignore s'il a changé. L'article absent de la base : soixante-dix
textes y sont, pas tous ; le reste se relève sur le site public du droit, et la
référence se vérifie avant emploi.

### E4 — Rédaction cible

Écrit **l'article tel qu'il sera**, puis en dérive la disposition modificative, et
la prouve par réapplication : on applique la disposition au texte en vigueur et on
doit retomber sur la cible, au caractère. Procédure à `11_OUTIL_disposition_cible.md`.

**La preuve par réapplication n'est pas une formalité.** C'est le seul contrôle qui
attrape une formule modificative qui dit autre chose que ce qu'on voulait.

**Elle se joue, elle ne se déclare pas.** Le dossier porte la commande exacte et
sa sortie verbatim. `preuve: jouée` sans trace d'exécution est une étape non
conclue, et la chaîne s'arrête. Le piège le plus courant est `completer` sur un
alinéa qui finit par un point : il ajoute après le point, et la preuve le voit.

### E4 bis — Le gage

Une mesure qui diminue une ressource publique porte une clause de gage, sans quoi
elle est irrecevable. Procédure à `05_PROCEDURE_gage.md`.

**Quand aucune source ne couvre le montant, le gage se déclare insuffisant et le
manquant se dit.** Un gage de façade rend la pièce irrecevable sans le dire, ce
qui est pire que pas de gage du tout.

### E5 — Exposé sommaire

Deux cents à trois cents mots, trois temps, sources entre parenthèses avec note.
Gabarit à `12_OUTIL_expose_sommaire.md`.

### E6 — Contrôles de sortie

```
python3 41_SCRIPT_controles_expose.py <dossier.md>
```

Trois familles qui ne se mélangent pas. **La forme** — gabarit, longueur, en-tête,
sources. **La généralisation** — aucune sortie ne nomme un déposant, une
organisation, un référentiel propre. **Le registre** — celui de la séance, non
celui du réseau.

**Un contrôle qui doute est un contrôle mal écrit** : à cette étape, `doutes` vaut
`aucun`, ou le contrôle est à reprendre.

### E7 — Liasse

```
python3 40_SCRIPT_imprimer_liasse.py <liasse.md> -o <sortie.docx>
```

L'assemblage et la numérotation se font. **L'ordre de dépôt et les neutralisations
réciproques sont des décisions politiques et vous reviennent.**

Deux choses mécaniques que la chaîne sait voir, et qu'il faut lui faire voir :
**deux dossiers qui visent la même adresse** se neutralisent ou se contredisent, et
**une même ligne ne sert pas deux fois de gage** — on ne gage pas non plus sur une
ligne qu'un autre amendement de la liasse supprime.

Sans réponse de votre part, la liasse sort dans l'ordre de production et le rendu
le déclare : *ordre non arbitré*.

---

## 4. Les cinq moments où la chaîne vous parle

| moment | ce qu'elle demande | si vous ne répondez pas |
|---|---|---|
| **l'entrée** | le véhicule, s'il n'est pas dans l'énoncé | `E0` le qualifie et continue |
| **après `E1`** | votre verdict de rattachement | elle porte `plaidable` et continue, en le déclarant |
| **après `E2`** | arbitrer entre deux adresses possibles | elle prend la plus étroite et le déclare |
| **après `E4 bis`** | la source de gage, si plusieurs sont ouvertes | elle déclare l'insuffisance |
| **avant `E7`** | l'ordre de dépôt | *ordre non arbitré* |

**Aucun n'est bloquant.** Une chaîne qui s'arrête parce que vous n'avez pas
répondu est une chaîne mal écrite.

---

## 5. Les cinq fautes qui coûtent le plus cher

1. **Rédiger sans avoir joué `E1`.** La pièce est parfaite et irrecevable.
2. **Approcher un vecteur.** Un article voisin produit un amendement inopérant que
   rien ne signale avant la séance.
3. **Citer un texte de mémoire.** Le droit change ; votre souvenir non.
4. **Écrire un gage de façade** pour franchir `E4 bis`.
5. **Sauter `E6`** parce que la pièce « a l'air bien ». Les trois familles de
   contrôle attrapent des choses différentes, et la deuxième — ce qui ne doit pas
   sortir — ne se voit pas à la relecture.
