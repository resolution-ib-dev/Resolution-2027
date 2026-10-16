# FORME CANONIQUE, ARRONDIS ET APPROXIMATIONS — 20260820 v2

Règles de décision applicables à toute émission d'une grandeur du corpus
Résolution, et à la rédaction des deux champs écrits du référentiel des
positions. Elles complètent le `Contrat_projection_REF_20260820_v2.md`, dont
elles précisent les règles d'émission 5 à 7.

Ce document intègre l'additif du 20260820 relatif à la justification et au
relais.

---

## 1. La forme canonique

Chaque grandeur du référentiel porte une forme unique sous laquelle elle
s'énonce. Cette forme vit dans `valeur` pour un paramètre, dans `chiffre` pour
un effet. La précision vit dans `exact`.

**Une grandeur, une forme.** Dès qu'une forme est arrêtée, elle vaut pour toute
émission interne. Un second arrondi, même arithmétiquement correct, est un
chiffre nouveau et se traite comme tel.

C'est cette règle, et non un écart numérique, qui départage les 8 800 € par
personne des 9 000 €. Les deux sont des arrondis corrects de 8 823,53. Un seul
est la forme du corpus.

**Le nombre de chiffres significatifs suit le registre.** Un pour la
percussion, deux pour l'usage courant, trois pour un tableau — mais le choix
entre ces trois rangs se commande par ce que la grandeur sert, non par le
confort de rédaction.

| registre | ce que la grandeur sert | rang | effet recherché |
|---|---|---|---|
| constat | dénoncer l'état des choses | trois chiffres, ou l'entier | sérieux : nous avons compté |
| promesse | annoncer ce que le projet produit | un ou deux chiffres | humilité : nous annonçons un ordre de grandeur |

Le constat se dit précis. 434 agences nationales, 329 organismes centraux, 24
autorités indépendantes, 318 instances consultatives, 1 104 au total : le
décompte est la démonstration. L'arrondir affaiblirait la dénonciation, parce
qu'il laisserait croire que nous n'avons pas compté.

La promesse se dit en ordre de grandeur. Six cents euros par mois, deux cent
trente-six milliards, cinq cent cinquante euros. Le rang court protège deux
fois : il tient l'engagement à la portée de ce qui est démontré, et il évite
d'être pris au piège d'une décimale que rien n'oblige à défendre.

Un chiffre de promesse écrit à quatre décimales promet une exactitude que la
prévision ne porte pas. Un chiffre de constat arrondi perd la preuve du travail.

**Où se lit le registre.** Une entrée relève du constat quand elle figure aux
`effets_diagnostic` d'un axe, ou sous un levier de diagnostic — `D3-1`, `D4-1`,
`D5-1`, `D6-1`, `D7-1`, `D8-1`, `D9-1`, `D10-1`, `D11-1` — ou quand sa
`certitude` porte la mention d'effet du système actuel. Le REF v18 en porte 83.
Toute autre entrée relève de la promesse.

**Les dénombrements s'énoncent entiers**, quel que soit le registre : 1 104
agences est un inventaire, non une grandeur.

**La forme canonique s'écrit sans virgule.** Une décimale se lit mal, se retient
mal et se prononce mal. Elle affaiblit à l'oral ce qu'elle prétend préciser à
l'écrit.

Trois voies, dans cet ordre.

*Arrondir à l'entier.* 236,1 Md€ devient 236. 264,71 € devient 265. C'est la
voie normale : sur les trente-six valeurs du REF v18 qui portent une virgule,
vingt-six se ramènent à l'entier pour moins de un pour cent d'écart.

*Changer d'unité.* Quand l'entier ne tient pas la grandeur, l'unité descend d'un
rang plutôt que la virgule n'apparaisse. 0,77 € s'écrit 77 centimes.

*Écrire la décimale, par exception.* Admise quand aucune des deux voies
précédentes ne convient et que le passage à l'entier déplacerait la valeur de
plus de un pour cent. L'exception se justifie à l'entrée, elle ne se décide pas
à l'émission.

**Une décomposition s'écrit à un rang unique.** Dès qu'un terme appelle la
décimale, tous les termes du champ la conservent. Un agrégat entier suivi de
termes décimaux se lit comme deux grandeurs de nature différente. La somme se
contrôle sur les exacts. Un total juste dont les termes affichés ne tombent pas est régulier :
c'est l'arrondi qui se voit, non le calcul qui manque.

**Formes admises.** Une grandeur peut porter plusieurs formes, à condition
qu'elles soient déclarées au référentiel dans `formes_admises`. Une forme courte
destinée à un titre ou à une prise de parole se déclare ; elle ne s'improvise
pas à l'émission.

---

## 2. Le sens de la précision

Le sens de la variation commande, davantage que son ampleur.

**Détailler est régulier.** Aller du manuscrit vers le détail est admis dès lors
que la décomposition somme et que chaque terme est tracé. Le manuscrit recense
434 agences nationales, 329 organismes centraux, 24 autorités indépendantes et
318 instances consultatives : la décomposition se vérifie, elle se cite.

**Généraliser est réglé.** Aller du détail vers la forme courte est admis
jusqu'à la forme canonique, et jusqu'à elle seulement. Au-delà, la forme se
déclare au référentiel avant emploi.

**Remonter est suspect.** Un chiffre du livrable qui ne se retrouve ni au
manuscrit, ni au classeur, ni dans une chaîne, ni par une opération nommable
n'est pas un arrondi : c'est une valeur nouvelle. Elle s'instruit.

---

## 3. Arrondi et approximation, deux objets distincts

**L'arrondi** raccourcit l'écriture d'une même grandeur. Il ne change ni le
référent, ni la base, ni la population.

**L'approximation** substitue une grandeur voisine, ou estime une grandeur que
le corpus ne calcule pas. Elle change le degré de certitude.

Les confondre est la faute la plus coûteuse : un arrondi se défend au dixième
près en contradictoire, une approximation ne se défend que par son ordre de
grandeur.

---

## 4. Règles de décision — l'arrondi

Appliquées dans cet ordre. La première qui échoue arrête l'examen.

**A1 — Même référent.** La valeur arrondie porte la même `base`, la même
`portee` et la même population que son entrée. Un montant par foyer et un
montant par personne ne sont pas deux arrondis d'une même grandeur.

**A2 — Arrondi au rang.** L'arrondi se fait à un rang décimal, jamais à
l'estime. 8 823,53 donne 8 820 à trois chiffres, 8 800 à deux, 9 000 à un.
Toute autre écriture est une valeur nouvelle.

**A3 — Forme canonique.** Parmi les arrondis corrects, seul celui que le
référentiel porte s'emploie en interne.

**A4 — Sens prudentiel.** Quand deux écritures sont également correctes au rang
retenu — valeur à mi-rang, ou choix ouvert entre deux rangs admissibles —
l'arrondi va dans le sens qui affaiblit la démonstration. Un gain vers le bas, un
coût vers le haut, y compris quand le coût est celui du projet. Une thèse qui a
besoin de l'arrondi favorable n'est pas démontrée.

Hors ces cas, l'arrondi va au plus proche. La prudence règle les partages, elle
ne déplace pas les valeurs : arrondir 15,18 à 16 au nom de la prudence
surestimerait un coût de cinq pour cent et fausserait le bouclage.

**A4 bis — Le registre commande le rang.** Un constat s'arrondit à trois
chiffres ou reste entier ; une promesse s'arrondit à un ou deux. Le rang se
choisit avant l'arrondi, et non l'inverse.

**A5 — Respect du sens de l'entrée.** Un `sens: plancher` s'arrondit vers le
bas, un `sens: plafond` vers le bas également — les deux formulations, « au
moins » et « jusqu'à », se tiennent alors sans promesse excédentaire. Un
`sens: égal` s'arrondit au plus proche, sous réserve d'A4.

**A6 — Aucun arrondi dans une chaîne.** Une `chaine` et une `operation` se
calculent sur les exacts. Les formes canoniques servent l'affichage, jamais le
calcul. Un total se prend à son entrée et ne se reconstitue pas depuis les
termes affichés.

---

## 5. Règles de décision — l'approximation

**P1 — Déclaration.** Une approximation porte sa marque dans l'énoncé :
« environ », « de l'ordre de », « près de ». Une grandeur approchée qui s'énonce
sèchement se donne pour exacte.

**P2 — Statut.** Le verdict de l'entrée l'établit : `APPROCHÉ` pour une valeur
estimée, `À QUALIFIER` pour une valeur dont l'instruction manque. Le verdict
s'énonce dans l'appareil, jamais dans le livrable.

**P3 — Propagation.** Une somme, un produit ou un quotient qui comprend une
valeur approchée est approché. Le statut se propage au résultat, il ne se dilue
pas dans l'agrégat.

**P4 — Écart consenti.** Une entrée de `nature: illustration` tolère un écart
sensible, à condition de nommer son cas et la grandeur qu'elle illustre. Un
agrégat et une règle générale ne tolèrent que l'arrondi.

**P5 — Non-cumul.** Deux approximations d'une même grandeur ne s'additionnent
pas et ne se comparent pas entre elles. Elles se ramènent à l'entrée.

---

## 6. Régime interne et compatibilité externe

Les règles ci-dessus gouvernent le contrôle interne — ce que le corpus émet.

En compatibilité externe, l'examen porte sur l'ordre de grandeur et sur la
compatibilité doctrinale, non sur la forme. Une proposition venue du dehors qui
écrit 9 000 € là où le corpus porte 8 800 € est compatible : l'écart est un
arrondi correct au rang supérieur. La même écriture dans un livrable Résolution
est une valeur nouvelle, et se corrige.

C'est la même valeur, jugée sous deux régimes. La frontière est l'origine du
chiffre, jamais sa distance.

---

## 7. Conséquences sur le référentiel

Onze valeurs affichées du REF v18 dépassent trois chiffres significatifs. Neuf
sont de statut classeur : la précision du tableur a été portée au champ
d'affichage.

| entrée | affiché | registre | forme canonique |
|---|---|---|---|
| `D2-1-1-e1` | 236,1 Md€ · 52,1 | promesse | 236 · 52 |
| `D7-2-2-e2` | 18,0 · 264,71 €/an par personne | promesse | 18 · 265 |
| `D3-2-1-p7` | +12,04 €/mois au SMIC | promesse | +12 |
| `D3-2-1-p6` | 98,25 % | constat | 98 % |
| `D3-2-1-p4` | 114,46 Md€ | constat | 114 |
| `D3-2-1-p5` | 9,7 | constat | 9,7, exception à 3,1 % |
| `D3-2-1-e3` | −15,18 Md€ | coût du projet | −15,2, exception à 1,2 % |
| `D3-2-1-e4` | −21,18 Md€ · −29,79 €/mois | coût du projet | −21 · −30 |
| `D2-5-1-p1`, `p2`, `p3`, `e2` | 143,2 · 52,1 · 91,1 | constat | 143 · 52 · 91 |
| `D2-4-1-e2` | 68,9 et neuf termes de décomposition | constat | 69, termes au cas par cas |
| `D2-2-1-e2` | 12,4 · 8,6 · 3,8 | constat | 12,4 · 8,6 · 3,8, exceptions |
| `D5-2-1-e2`, `D6-2-2-e2` | 9,6 · 29,6 · 20,0 | constat | 9,6 exception · 30 · 20 |
| `D9-2-2-e1` | 1,1 Md€ | promesse | 1,1, exception à 9,1 % |
| `D8-3-1-e2` | 30,0 Md€ | promesse | 30 |
| `D2-2-1-p1` | 1 104 agences | constat | inchangé, dénombrement |

Trente-six valeurs affichées portent une virgule. Vingt-six passent à l'entier
pour moins de un pour cent d'écart. Dix relèvent de l'exception, toutes des
petites grandeurs en milliards où un rang entier pèse trop lourd : 1,1 · 3,2 ·
3,6 · 3,8 · 6,6 · 8,6 · 9,6 · 9,7 · 12,4 · 15,2.

Trois cas méritent d'être distingués.

`D2-1-1-e1` est le plus net : le manuscrit écrit « économiser ainsi 236
milliards d'euros par an ». La forme affichée s'écartait de l'ancre, sur la
grandeur la plus citée du corpus.

`D2-5-1-p1` reste à 143,2. C'est un constat — le montant des niches existantes —
et quatre chiffres significatifs y disent que le recensement a été fait. La
règle des trois chiffres cède devant le registre.

`D3-2-1-e3` et `e4` portent des coûts de notre propre projet. A4 n'y déplace
rien : les valeurs ne sont pas à mi-rang, l'arrondi va au plus proche. La
prudence jouerait si le partage était ouvert.

Chaque valeur d'`exact` demeure inchangée. Seule la forme d'affichage bouge.

---

## 8. La justification et le relais

Deux champs rédigés du référentiel des positions. Ils sont écrits à la main, au
référentiel, une fois. Tous les livrables les projettent sans les réécrire.

**`justification`** — pourquoi la perte est légitime. Une à deux phrases. Elle
répond à « de quel droit ».

**`relais`** — la contrepartie, en langue ordinaire. Une phrase. Elle répond à
« et moi alors ».

### Forme de la justification

**Elle décrit un mécanisme, pas une intention.** « Subventionner les loyers
augmente les loyers, pas le nombre de logements » vaut mieux que « l'aide au
logement est inefficace ». Le mécanisme se vérifie, l'intention se discute.

**Elle nomme ce qui est conservé avant ce qui est retiré**, quand quelque chose
l'est. Le socle de 20 % de l'hébergement d'urgence, les 10 % de soins urgents de
l'aide médicale d'État, les pensions inférieures à 1 200 euros, le socle de 15 %
du parc social : les dire d'abord désarme l'objection avant qu'elle se forme.

**Elle cite le manuscrit quand il porte l'argument**, corps ou note, sans
guillemets ni appel visible : la phrase se fond dans la justification. Le lecteur
externe ne rencontre jamais la nomenclature interne.

**Elle donne le chiffre qui dérange avant qu'on l'oppose.** L'abattement dit
« Papon » coûte 4,8 milliards, ne bénéficie qu'aux retraités déjà imposables et
leur rapporte moins de 1 % de leur revenu : le dire vaut mieux que de l'attendre.

**Interdits.** Les formulations négatives du type « X ne se décrète pas » ou
« ne tient pas à… mais à ». Les points-virgules en texte normatif. Le
conditionnel de précaution quand le corpus affirme.

### Forme du relais

**Structure canonique : « Je perds A, je gagne B, C et D. »** Première personne,
présent, énumération concrète. Le perdant parle.

Trois exemples de référence :

- Je perds l'aide au logement, je gagne 300 euros de salaire, 550 euros d'aide
  sans dossier, et un marché où l'offre locative privée augmente d'un quart.
- Je perds mes niches, je gagne l'assiette pleine et le taux bas, des clients
  dont le pouvoir d'achat a monté de 13 %, et un impôt que je peux calculer sans
  conseil.
- Je perds mon poste, je gagne sept ans à 70 % de mon traitement, le cumul libre
  avec un emploi privé, la maîtrise de mon temps et un métier choisi.

**Le relais est chiffré dès que le corpus le permet.** Un relais entièrement
qualitatif est un relais faible ; il se déclare tel plutôt que d'emprunter au
vocabulaire de la promesse.

**Aucun identifiant.** Ni nœud D, ni ligne, ni note. Le relais est la phrase que
le lecteur emporte.

**Le relais d'un capteur ne compense pas, il rouvre.** « Je perds la commande
captive, je gagne un client qui m'achète parce qu'il le choisit et qui dispose de
davantage pour le faire. » La rente ne se remplace pas ; le marché s'ouvre.

**Le relais d'une reconstitution nomme qui reconstitue.** Le donateur, le mécène,
l'association, le client — jamais « le privé » ni « le marché » en abstraction.

### Ce qui n'a pas de relais

Deux cas, et deux seulement.

**La dette.** Le coparent qui n'acquitte pas la pension due, le fraudeur dont la
complexité rendait la fraude rentable. Rien ne se reconstitue, et le corpus
l'assume.

**Le capteur dont la rente est l'objet même de la mesure**, quand aucun marché ne
se rouvre. Le cas est rare et se justifie ligne à ligne.

Dans les deux cas, le champ `relais` reste vide et la raccroche porte l'absence
assumée. Le silence est une valeur déclarée, jamais un oubli.

### Marqueurs d'entrée et de sortie

Ils se dérivent, ils ne s'écrivent pas.

**En tête de catégorie** : ce que le projet y déplace, en comptes — tant de
pertes, tant de rentes supprimées, tant de gains.

**En pied de catégorie** : le premier relais de la catégorie. Quand la catégorie
n'a que des gains, le dire. Quand elle n'a que des rentes supprimées, le dire
frontalement plutôt que de l'habiller.

**Ordre des lignes : perte, puis rente, puis gain.** Aucune catégorie ne se
termine sur un problème — posture d'optimisme du plan stratégique.

### Le rang selon le registre, appliqué aux positions

La règle générale de la section 1 s'applique aux grandeurs des positions comme
aux autres. Un constat se dit précis, une promesse en ordre de grandeur.

C'est ce qui sépare les deux registres de `C-00` : l'écart mesuré avec les pays
comparables est un constat et se chiffre au décimal ; le gain rendu par le plan
est une promesse et se donne en ordre de grandeur — « de l'ordre de +10 % »,
« de l'ordre de 5 points ». Les mêler décrédibilise les deux.

---

## 9. Points à instruire

**Ancre absente du référentiel.** Le manuscrit porte 5 500 euros de dette
publique par an et par foyer. Le REF ne la porte pas. Septième chiffre du
manuscrit absent du corpus.

**Forme canonique de 8 800.** La valeur ne figure pas au manuscrit : elle
dérive de 600 Md€ divisés par 68 M personnes. Son autorité vient de l'usage. Sa
déclaration comme forme canonique de `D7-2-1-p1` est donc un arbitrage à porter,
non un relevé.
