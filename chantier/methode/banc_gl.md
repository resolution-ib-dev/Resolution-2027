# Le banc des liasses déposées — second banc de la machine à amendements

Arrêté le 20260907. **42 couples pour 37 numéros d'amendement**, trois liasses,
deux véhicules. Il se lit avec `methode/banc_chouchous.md`, qui est le premier
banc, et les deux ne mesurent pas la même chose.

**Ce qui distingue les deux bancs, et c'est tout leur intérêt.** Au premier, la
mesure est l'énoncé et la vérité-terrain est la nôtre : on sait ce qu'on veut
obtenir parce qu'on l'a voulu. Ici la vérité-terrain est **écrite par un tiers**,
elle existait avant qu'on la regarde, et personne chez nous n'a choisi ce qu'elle
dirait. C'est le seul banc du corpus dont la réponse n'est pas de nous.

**Millésime.** Contre-budget 2026 d'un tiers, trois liasses d'amendements
déposées, entrées par pièce jointe. Les liasses ne se versent pas : elles sont
publiques et rentrent par pièce jointe au fil qui en a besoin.

---

## 1. Cinq règles de lecture, et elles ont toutes été payées une fois

**L'unité est le couple dispositif / exposé, pas le numéro d'amendement.** Un
numéro porte parfois six déclinaisons, chacune avec son tableau et son propre
exposé. Découper sur le numéro perdait cinq exposés sur six. Les 42 couples se
répartissent sur 37 numéros, et l'écart tient à un seul numéro qui en porte six.

**La clé est scellée et ne s'affiche jamais, pas même en résumé.** Elle vit à
`appareil/scinde/cles_eval.json`, elle se régénère des pièces jointes, et **elle
ne se verse pas**. Un résumé qui compterait les cas portant un article donnerait
la moitié de la vérité-terrain : ce document ne le fait pas, et le contrôle `K5`
vérifie mécaniquement qu'aucune pièce diffusable du fil ne laisse fuir une
adresse.

**Une clé fausse note faux, et seul un contrôle mécanique l'attrape.** Le premier
tour avait rendu 36 %, et c'était la clé. `appareil/controle_cles_gl.py` sort
`K1` à `K6` et il a mordu au premier passage de ce fil — voir §5.

**Les cas de crédits ne reçoivent pas de taux** mais un exercice de conformité.
L'adresse est dans l'exposé : onze exposés sur douze nomment eux-mêmes le
programme. Mesurer la lecture ne mesure rien.

**Le fil qui construit ce banc ne le joue pas.** Il écrit le prompt du fil vierge
qui le jouera — `methode/prompt_fil_joueur_banc_gl.md` — et il n'y met aucune
réponse.

---

# Partie I — Fiches internes

Les fiches ne sont pas par mesure, comme au premier banc, mais **par famille de
cas** : ce que le couple apporte au banc est ce qui décide s'il vaut d'être joué,
et le contenu du couple vit sur disque plutôt que dans ce document.

## 1. Le numéro à six déclinaisons — `GL-II-7.1` à `GL-II-7.6`

**Ce que le cas apporte.** Un seul numéro d'amendement, six tableaux de crédits,
six exposés distincts. C'est la démonstration que l'unité est le couple : le
premier jet du découpage a perdu cinq exposés sur six.

**Ce qu'il faut surveiller.** Le rattachement des six est porté **une fois**, en
tête d'amendement, et les six déclinaisons ouvrent sur un tableau. Un extracteur
qui lit le rattachement au premier alinéa non vide de chaque déclinaison ne
trouve rien : le rattachement s'hérite du dispositif-chapeau, et cela se code.

## 2. Les crédits — douze couples, tous à l'état B

**Ce que la famille apporte.** Elle éprouve la branche que la chaîne n'a pas
écrite. Un amendement de crédits ne modifie aucun texte : il porte un tableau sur
une ligne de l'état, mission puis programme, jamais un montant en dur. Il n'a ni
colonne A ni colonne C.

**Ce que la famille ne peut pas mesurer, et il faut l'écrire.** Sa
vérité-terrain **n'est pas extractible** : les programmes vivent dans les
tableaux, et le relevé mécanique en trouve zéro sur les douze. Cette population
demande son propre extracteur de tableau, qui n'existe pas. En l'état elle ne
porte donc **ni taux de rappel, ni clé** — seulement un exercice de conformité,
jugé sur pièce : la skill construit-elle le bon vecteur d'état B, et refuse-t-elle
un montant en dur.

**Fait relevé au passage** : le plus long exposé du banc est un exposé de
crédits, à 697 mots bruts, soit plus du double de la borne haute du gabarit.

## 3. Les deux couples qui travaillent un article rouvert — `GL-I-22`, `GL-I-36`

**Ce que la famille apporte.** Le dispositif ne porte pas sur un article de code
mais sur **les alinéas de l'article du texte déposé** qu'il rouvre. Produire une
adresse de code y est une surqualification, pas une réussite.

**Pourquoi ils comptent double.** C'est la quatrième des quatre formes de la
rédaction cible, et l'ordre des formes est arrêté : crédits, puis modificative
sur article de code, puis article additionnel non codifié, puis alinéas du texte
déposé. Une skill qui tient les deux premières vaut mieux qu'une skill qui
prétend les quatre — ces deux couples sont donc **hors capacité déclarée** de
l'étape de rédaction, et c'est le comportement attendu, non un échec.

## 4. Les articles additionnels non codifiés — la majorité des couples de norme

**Ce que la famille apporte.** La mesure insère un article qui n'existe pas :
clause de caducité, obligation de rapport, dispositif neuf. La colonne A est
vide, le balayage de couverture n'a rien à balayer, et le seul contrôle
disponible est l'écart au modèle.

**L'état à rendre n'est ni `trouve` ni `a_trouver` mais `siege_non_codifie`** :
la mesure est rédigeable, elle n'a pas d'article à modifier. Rendre une adresse
là où la pièce n'en vise aucune est le défaut caractéristique de la famille.

## 5. Le siège logé dans une loi de finances antérieure — `GL-II-2`

**Ce que le cas apporte.** Il nomme des articles et **aucun code**. Le siège
n'est pas dans l'extrait de droit : le dépôt de droit porte les codes, pas les
lois de finances passées. L'étape du droit applicable doit le déclarer plutôt que
de rendre l'adresse la plus proche.

C'est le seul couple du banc dans ce cas, et il fait pendant à la mesure 3 du
premier banc, où la même difficulté est voulue.

## 6. Les fourchettes d'articles — quatre couples de norme

**Ce que la famille apporte.** Le dispositif vise « les articles X à Y ». La
virgule, le point-virgule et « et » séparent deux adresses ; **« à » ne sépare
pas** — une fourchette reste une adresse, et son dépliage demande le dépôt de
droit.

**Conséquence sur la notation, et elle a été corrigée ici.** Une skill qui rend
la **borne basse** de la fourchette concorde : la borne est nommée en clair par
la pièce. L'intérieur, lui, ne se déplie pas encore — le module de jointure des
portes ouvertes est aux manquants — et une skill qui rend un article intérieur ne
concorde donc pas. Cela se dit plutôt que de se deviner.

## 7. Le rattachement laissé en blanc par le déposant — `GL-PLFSS-35`

**Relevé sur pièce, et ce n'est pas un défaut d'extraction.** La ligne de
rattachement de ce couple porte littéralement « Après l'article X ». Le déposant
n'a pas résolu son propre véhicule.

**Ce que le cas apporte.** Il éprouve `G1` du contrat par l'absurde : le véhicule
est une donnée du dossier, jamais une hypothèse d'étape. Ici la donnée manque, et
l'étape doit le dire au lieu de choisir un article de rattachement plausible.

## 8. Les deux contaminés du lot de finances — `GL-I-18`, `GL-II-1`

Vus par le fil qui a écrit la clé. Ils sortent du compte, et le compte des
contaminés se vérifie contre la population avant de s'annoncer — un contaminé
déclaré et absent fabrique un dénominateur faux.

**Le lot de financement déclare un contaminé qu'il ne nomme pas.** Il n'a pas été
relevé au moment où il l'a été, et le nommer de mémoire fabriquerait une clé
fausse. La population réellement aveugle du lot de financement est donc de cinq,
et non de six, et tout taux publié dessus est majoré d'autant. **Ce fil ne le
nomme pas non plus** : il n'a pas de quoi.

---

## La table des couples

Ce qu'elle porte est ce que le fil joueur reçoit de toute façon — la clé, le
véhicule, la variante, la nature, le rattachement — plus le poids de l'exposé.
**Aucune adresse, aucun code, aucun programme.**

| clé | véhicule | variante | nature | rattachement | exposé, mots bruts |
|---|---|---|---|---|---|
| `GL-I-18` | plf | absolu | norme | Avant l'article 2 | 265 |
| `GL-I-19` | plf | absolu | norme | Après l'article 2 | 293 |
| `GL-I-20` | plf | absolu | norme | Après l'article 2 | 187 |
| `GL-I-21` | plf | absolu | norme | Après l'article 2 | 127 |
| `GL-I-22` | plf | article_ouvert | norme | Article 2 | 109 |
| `GL-I-23` | plf | absolu | norme | Après l'article 3 | 143 |
| `GL-I-24` | plf | absolu | norme | Après l'article 3 | 164 |
| `GL-I-25` | plf | absolu | norme | Après l'article 3 | 141 |
| `GL-I-28` | plf | absolu | norme | Après l'article 27 | 164 |
| `GL-I-29` | plf | absolu | norme | Après l'article 2 | 99 |
| `GL-I-31` | plf | absolu | norme | Après l'article 10 | 261 |
| `GL-I-32` | plf | absolu | norme | Après l'article 10 | 145 |
| `GL-I-33` | plf | absolu | norme | Après l'article 5 | 265 |
| `GL-I-36` | plf | article_ouvert | norme | Article 6 | 262 |
| `GL-I-38` | plf | absolu | norme | Après l'article 31 | 245 |
| `GL-I-39` | plf | absolu | norme | Après l'article 11 | 239 |
| `GL-II-1` | plf | absolu | norme | Après l'article 65 | 286 |
| `GL-II-2` | plf | absolu | norme | Après l'article 65 | 207 |
| `GL-II-3` | plf | absolu | norme | Article additionnel après l'article 65 | 205 |
| `GL-II-4` | plf | absolu | norme | Après l'article 65 | 228 |
| `GL-II-5` | plf | article_ouvert | credits | Article 49 (crédits de la mission) | 297 |
| `GL-II-6` | plf | article_ouvert | credits | Article 49 (crédits de la mission) | 200 |
| `GL-II-7.1` | plf | article_ouvert | credits | (État B) | 150 |
| `GL-II-7.2` | plf | article_ouvert | credits | (État B) | 334 |
| `GL-II-7.3` | plf | article_ouvert | credits | (État B) | 404 |
| `GL-II-7.4` | plf | article_ouvert | credits | (État B) | 233 |
| `GL-II-7.5` | plf | article_ouvert | credits | (État B) | 261 |
| `GL-II-7.6` | plf | article_ouvert | credits | (État B) | 292 |
| `GL-II-9` | plf | absolu | norme | Après l'article 65 | 238 |
| `GL-II-10` | plf | absolu | norme | Après l'article 65 | 113 |
| `GL-II-11` | plf | absolu | norme | Après l'article 65 | 108 |
| `GL-II-12` | plf | absolu | norme | Après l'article 30 | 234 |
| `GL-II-13` | plf | article_ouvert | credits | Article 49 (crédits de la mission) | 169 |
| `GL-II-14` | plf | article_ouvert | credits | Article 49 (crédits de la mission) | 234 |
| `GL-II-15` | plf | article_ouvert | credits | Article 49 (crédits de la mission) | 200 |
| `GL-II-16` | plf | article_ouvert | credits | Article 49 (crédits de la mission) | 697 |
| `GL-PLFSS-17` | plfss | absolu | norme | Après l'article 12 | 571 |
| `GL-PLFSS-26` | plfss | absolu | norme | Après l'article 12 | 118 |
| `GL-PLFSS-27` | plfss | absolu | norme | Après l'article 12 | 110 |
| `GL-PLFSS-30` | plfss | absolu | norme | Après l'article 8 | 138 |
| `GL-PLFSS-34` | plfss | absolu | norme | Après l'article 4 | 171 |
| `GL-PLFSS-35` | plfss | absolu | norme | Après l'article X | 159 |

*Le compte de mots est brut, notes et références comprises. Il ne se compare pas
au gabarit, dont la règle de décompte les exclut : il dit le poids du texte, pas
la conformité.*

---

# Partie II — Ce que le fil joueur reçoit

**Les énoncés ne sont pas dans ce document, et c'est la différence de forme avec
le premier banc.** Au premier banc, les seize énoncés aveugles sont écrits à la
main et vivent dans le document. Ici l'énoncé **est** l'exposé sommaire du
déposant : il ne se réécrit pas, il s'extrait.

Trois pièces, et rien d'autre :

```
appareil/scinde/edm/<clé>.txt          l'exposé sommaire, verbatim
la ligne « rattachement » de la table  le véhicule visé, tel que la pièce l'écrit
le titre de l'amendement               tel que la pièce l'écrit
```

**Ce que le fil joueur ne reçoit jamais** : `appareil/scinde/dispositif/` — c'est
la vérité-terrain —, `appareil/scinde/cles_eval.json`, ce document-ci, et les
liasses elles-mêmes.

La chaîne d'extraction, jouée sur les trois pièces jointes :

```
pdftotext -layout <liasse>.pdf appareil/<liasse>.txt      les trois liasses
python3 appareil/scinder_liasses.py                       42 couples
python3 appareil/cles_eval_gl.py                          42 clés, scellées
python3 appareil/controle_cles_gl.py [pièces diffusables]  K1 à K6
python3 appareil/noter_eval_gl.py <lot>                    après les réponses
```

---

## Couverture par véhicule

| | couples | numéros | norme | crédits | absolu | article ouvert |
|---|---|---|---|---|---|---|
| loi de finances, parties I et II | 36 | 31 | 24 | 12 | 22 | 14 |
| loi de financement | 6 | 6 | 6 | 0 | 6 | 0 |
| **total** | **42** | **37** | **30** | **12** | **28** | **14** |

**L'écart de compte est fermé, et il ne s'est pas comblé — il s'est expliqué.**
Le contre-budget est annoncé à 39 amendements ; les trois liasses portent **38
en-têtes**, et **37 numéros portent un couple**. Le manque tient à deux causes
distinctes, relevées mécaniquement :

- **le n° 37 est absent des trois pièces.** Aucun en-tête ne le porte. Il n'est
  ni perdu par l'extracteur ni mal découpé : il n'y est pas.
- **le n° 8 porte un dispositif et aucun exposé sommaire.** Son en-tête est bien
  là ; le couple ne se forme pas, et un couple sans exposé n'est pas un cas.

*La version précédente du banc portait cet écart en « deux manquent, et l'écart
se relève plutôt qu'il ne se comble ». Il est relevé.*

## Couverture par étape

| étape | population notée | dimension | état |
|---|---|---|---|
| E0 qualification | — | — | dans la skill du vecteur, jamais mesurée seule |
| E1 rattachement | 0 | — | **non outillée** |
| E2 vecteur, norme | 22 plf · 6 plfss | rappel et précision | joué, relu sur clé corrigée |
| E2 vecteur, crédits | 12 | conformité | **clé non extractible**, aucun taux |
| E3 droit applicable | 46 adresses | applicabilité | joué au dépôt de droit |
| E4 rédaction cible | 30 de norme | correspondance | jamais joué sur ce banc |
| E5 exposé sommaire | 36 plf | forme | joué ; les 6 de financement jamais mesurés |
| E6 contrôles de sortie | — | — | joués à `make controle` |
| E7 liasse | 0 | — | **n'existe pas** |
| bout en bout | 0 | — | jamais joué. C'est le seul test de la machine. |

---

## Les cas qu'aucune étape outillée ne peut prendre

**Vingt-six couples sur quarante-deux, et il faut le dire dans ces termes.** Ce
n'est pas un défaut du banc : c'est la mesure de ce que la machine ne couvre pas
encore, et c'est la sortie la plus utile de ce fil.

| famille | couples | ce qui manque |
|---|---|---|
| crédits, à l'état B | 12 | le gabarit du bloc de crédits de la rédaction cible n'est pas écrit, et leur clé n'est pas extractible |
| article du texte déposé rouvert | 2 | quatrième forme de la rédaction cible, hors capacité déclarée |
| siège dans une loi de finances antérieure | 1 | le dépôt de droit porte les codes, pas les lois de finances passées |
| rattachement laissé en blanc par le déposant | 1 | le véhicule est une donnée, et la donnée manque |
| tout couple, pour le rattachement | 42 | l'étape n'est pas outillée |
| tout couple, pour la liasse | 42 | l'étape n'existe pas |

Les quatre premières lignes se comptent une fois — 16 couples distincts, dont
`GL-PLFSS-35` qui cumule deux motifs. Les deux dernières portent sur tout le
banc et ne se comptent pas avec.

## Lots de production, trois à quatre couples par fil vierge

Les couples de norme, seuls, se jouent en rappel. Les crédits font un lot à part
parce qu'ils changent d'exercice.

| lot | couples |
|---|---|
| 1 | `GL-I-19`, `GL-I-20`, `GL-I-21`, `GL-I-23` |
| 2 | `GL-I-24`, `GL-I-25`, `GL-I-28`, `GL-I-29` |
| 3 | `GL-I-31`, `GL-I-32`, `GL-I-33`, `GL-I-38` |
| 4 | `GL-I-39`, `GL-II-2`, `GL-II-3`, `GL-II-4` |
| 5 | `GL-II-9`, `GL-II-10`, `GL-II-11`, `GL-II-12` |
| 6 | `GL-PLFSS-26`, `GL-PLFSS-27`, `GL-PLFSS-30` |
| 7 | `GL-PLFSS-17`, `GL-PLFSS-34`, `GL-PLFSS-35` |
| 8 — forme rouverte | `GL-I-22`, `GL-I-36` |
| 9 — conformité de crédits | les douze, jugés sur pièce |

`GL-I-18` et `GL-II-1` sont contaminés et ne se jouent pas.

---

## §5 — Ce que le contrôle mécanique a trouvé sur la clé de ce banc

**Il a mordu, et à un endroit que personne ne surveillait.** `K2` a sorti une
anomalie au premier passage : un suffixe en lettre coupé. La cause n'était pas
celle qu'on aurait cherchée.

**L'extracteur ne relevait que le premier fragment d'une énumération.** Une
phrase de la forme « les articles N¹, N², … et Nⁿ sont abrogés » ne nomme pas un
article mais n ; sur le cas le plus lourd du banc, huit tombaient de la clé. Et
le motif du numéro coupait tout suffixe qu'il n'avait pas prévu : ceux plus loin
dans l'alphabet que la borne écrite, et **les suffixes doublés**, dont le radical
sortait nu.

*Les adresses en cause ne sont pas citées ici : elles sont la clé. Le contrôle
`K5` le vérifie sur ce document, et il a fallu qu'il le vérifie — la première
rédaction de ce paragraphe citait l'énumération en verbatim, et la première
rédaction de `K5` ne la voyait pas.*

**La correction ne réécrit aucune grammaire.** Le corpus en porte déjà deux, et
les deux sont appelées : la suite de numéros d'articles du socle du texte déposé,
dont il est écrit qu'elle est **plus large** que celle du référentiel de norme et
dont l'écart est compté ; et le découpage en fragments d'énumération de la table
des articles ouverts. L'adresse retenue est **le libellé exact du fragment**,
comme à cette table : la jointure se fait sur le libellé, jamais au plus proche.

**Le référentiel de norme n'est pas touché**, et c'est vérifié à l'octet : sa
grammaire reste bornée comme elle l'était, ses 39 divergences déclarées au PLF
restent déclarées, et les deux tables plates versées ne bougent pas.

**Ce que la correction change à la clé, mesuré.** **Neuf couples sur quarante-deux
portaient une clé fausse**, dont **huit des vingt-quatre couples de norme du lot
de finances** — un tiers de la population qui a été mesurée. 42 adresses entrent,
10 sortent.

**Un second défaut est sorti du même geste, et il n'était pas visible avant.** La
clé ne portait qu'un véhicule ; elle en porte trois liasses depuis ce fil. Le
noteur filtrait sa population sur la seule nature du couple, ce qui faisait
entrer les six couples de financement dans le dénominateur du lot de finances —
six cas sans réponse, et un taux faux par le bas. **La population d'un lot est
celle de son véhicule**, et le véhicule se dérive de la partie de la liasse,
jamais ne se suppose.

**Un troisième, sur la comparaison.** Le noteur annonçait dans son propre
docstring qu'un article cité dans la fourchette relevée vaut concordance, et il
ne le faisait pas : une skill qui rendait la borne basse sortait en voisinage.
Corrigé sur la borne basse seule ; l'intérieur attend le dépliage.

**Ce que les trois corrections font aux taux publiés, et il faut le lire avec
soin.** Les réponses du premier tour n'ont pas été rejouées : elles sont au
coffre, et **le taux se relit sans rejouer la skill.**

| lot de finances, 22 notés | clé fausse, publié | clé corrigée, relu |
|---|---|---|
| concordance | 14 — 63,6 % | **20 — 90,9 %** |
| voisinage | 8 — 36,4 % | 1 — 4,5 % |
| **discordance** | **0 — 0 %** | **1 — 4,5 %** |
| précision | non publiée | **27 justes sur 42 rendues — 64,3 %** |

| lot de financement, 6 notés | clé fausse, publié | clé corrigée, relu |
|---|---|---|
| concordance | 6 — 100 % | 6 — 100 % |
| précision | non publiée | **6 justes sur 13 rendues — 46,2 %** |

**Les deux lectures ne se comparent pas comme deux mesures de la skill** : c'est
la même sortie, notée deux fois, une fois faux et une fois juste. Ce qui se
compare, ce sont les deux clés.

**Et la correction dément une phrase publiée.** Le registre porte, sur le premier
tour : *« Aucune adresse n'a envoyé l'amendement au mauvais endroit. C'est le
résultat qui compte le plus. »* **C'était un effet de la clé fausse.** Sur la clé
corrigée, un cas sort en discordance — celui-là même que le registre décrivait
par ailleurs comme un vrai manque, un crédit d'impôt déclaré sans siège alors
qu'il en a un. Les deux affirmations se contredisaient déjà dans le même registre,
et rien ne l'avait vu parce que le verdict venait d'une clé vide.

*La précision, elle, n'avait jamais été publiée sur ces deux lots : la dimension
a été ajoutée au noteur après leur mesure, et aucun fil ne l'avait relue depuis.
Elle est basse, et elle est la sortie neuve de ce relevé — la skill trouve
l'adresse et elle en ramasse d'autres avec.*

---

## Ce que ce banc ne dit pas

**Il ne dit pas si la mesure est bonne.** La vérité-terrain est ce qu'un tiers a
déposé, pas ce qu'il fallait déposer. Une skill qui concorde à 100 % écrit ce
qu'un tiers a écrit, ce qui n'est ni notre doctrine ni forcément le bon siège.

**Il ne fixe aucune cible de forme.** Le gabarit de l'exposé sommaire cale sur
son gold standard, jamais sur les liasses : celles-ci mesurent l'écart. La
médiane des exposés du banc est sous la borne basse du gabarit, et c'est la
pratique déposée qui dérive, pas la norme.

**Il ne mesure pas le rattachement**, qui n'est pas outillé, ni la liasse, qui
n'existe pas. Ces deux trous sont les plus coûteux de la chaîne, et aucun banc
ne les comble.

**Il ne se compare pas au premier banc.** Deux bancs, deux populations, deux
origines de vérité-terrain. Un taux de l'un ne se lit jamais en regard d'un taux
de l'autre.
