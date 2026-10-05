# Prompt — fil « lecture des textes financiers 2027 »

*Fil Cowork, chantier 3. Il lit le PLF et le PLFSS déposés et rend le résumé en
forme fixe. Il ne rédige aucun amendement, ne qualifie aucune mesure en droit, ne
produit aucune adresse : c'est un fil du projet doctrine.*

**La seule date du chantier qui ne se négocie pas.** Un texte déposé ne se relit
pas l'année suivante : les pièces disparaissent des points d'accès et la lecture
en creux — amendements, sorts, débats — n'existe plus. Ce fil se joue à chaud.

**Corrigé le 20261001, après deux passes mesurées.** Les deux fils du jour — PLF et
PLFSS — ont produit des pièces que ce prompt ne nommait pas, ont dû reprendre sa
grille de relevé, et **ont propagé une consigne périmée** (voir « les bornes »).
Les corrections sont intégrées et signalées *[corrigé 20261001]*. Ce qui relève du
fond est à `methode/a_trancher.md`, § B, questions 40 à 44.

---

## Ligne de lancement

> Fil Cowork — lecture des textes financiers 2027. Socle : `methode/socle_prompt_fil.md`. Pièces à joindre : le PLF 2027 et le PLFSS 2027 en PDF, **les deux** ; et, si elles sont parues, l'annexe 2 du tome I de l'évaluation des voies et moyens (taxes affectées) et l'annexe 3 du tome II (dépenses fiscales). Activer `methode/prompt_fil_lecture_textes_2027.md`, `livrables/resume_attendu_texte_financier_2026.md`, `livrables/bordereau_confrontation_resume_2026.md`, `livrables/index_mesures_plf.md`, `livrables/PLFSS2026_liste.md`, `reference/gabarit_liste_articles.md`, `methode/procedure_contre_plf.md`, `methode/grille_lecture_budgetaire.md`, `referentiels/REF_doctrine.json`, `methode/a_trancher.md` (§ B). Mandat : rendre les **quatre pièces de lecture** d'un véhicule — index des mesures, fiches de mesure principale, liste par article, note lisible — **puis** le résumé attendu du texte financier 2027 dans le gabarit des quatre blocs L1 à L4, par **modification** des gabarits 2026 et non par reconstruction, chaque lot commençant par sa mesure de présence et se sautant proprement si sa pièce manque. Aucune rédaction, aucun amendement, aucune adresse.

---

## Ce que le fil trouve en entrant, et qui le dispense de tout réinventer

Le millésime 2026 est lu, gelé et confronté. **Il n'est pas un précédent : c'est
le gabarit.** `livrables/resume_attendu_texte_financier_2026.md` donne les quatre
blocs ; `livrables/bordereau_confrontation_resume_2026.md` donne ce qui s'est
confronté et ce qui est sorti introuvable ; `livrables/index_mesures_plf.md` donne
le gabarit de l'index ; **`reference/gabarit_liste_articles.md` fait foi pour la
liste par article et son rendu PDF.**

**Le fil 2026 a reconstruit son livrable trois fois de zéro au lieu de le
modifier.** C'est le premier des quatre mécanismes de faute du corpus. **On
modifie, on ne reconstruit pas** : chaque rubrique sort dans un des quatre états —
*reprise et à jour*, *modifiée*, *sans objet cette année*, *suspendue faute de
pièce*.

**Réutilisation avant réinvention vaut aussi entre les deux véhicules du même
millésime.** *[corrigé 20261001 — les deux fils du jour ont écrit la même pièce
chacun de son côté, et deux grilles de relevé différentes.]* **Le fil qui lit le
second véhicule lit d'abord ce que le fil du premier a versé** : ses livrables, son
fragment d'arbitrages, son fragment `a_trancher`. Il reprend sa grille et ses
formats, il ne les réinvente pas.

**Et il vérifie l'état du corpus avant de répéter une borne.** *[corrigé 20261001 —
ce prompt a porté pendant un mois une consigne que le corpus avait démentie, et
deux fils l'ont recopiée dans leurs livrables.]* **Une borne écrite ici ne se
recopie pas : elle se vérifie à `methode/arbitrages.md` et au registre avant
d'être redite.**

---

## Les quatre blocs — ils ne bougent pas d'un millésime à l'autre

**L1 — Le solde et sa construction.** Article liminaire, article d'équilibre,
équilibre par branche, objectif national de dépenses, effets de périmètre.

**L2 — Les portes ouvertes.** Une porte ouverte est un couple (texte, article)
que la disposition du véhicule modifie elle-même. **L'exposé des motifs n'en
ouvre aucune** : il est de l'indice, jamais de la porte.

**L3 — Les mouvements sur nos objets.** Impositions affectées, plafonnées ou
déplafonnées ; dépenses fiscales ; opérateurs — créés, fusionnés, supprimés,
dotés.

**L4 — L'écart à nos positions.** Chaque proposition du corpus confrontée au
texte : le texte va dans notre sens, il va contre, il ne dit rien. **La règle de
verdict exige un acte du texte sur le siège même que la mesure vise** ; elle a été
posée au fil 2026 faute d'arbitrage antérieur et n'est toujours pas validée. Le
fil l'applique telle quelle et le déclare.

---

## Les lots, et leur mesure de présence

**Règle générale : chaque lot commence par mesurer la présence de sa pièce, et se
saute en continuant si elle manque. Aucun lot absent n'arrête le fil entier.**
Une pièce absente produit une rubrique **suspendue**, nommée, avec ce qui la
rouvrira — jamais une rubrique vide, jamais un zéro.

**Lot 1 — les deux véhicules.** PLF et PLFSS en PDF. Empreinte sha256 relevée et
inscrite, compte de pages, compte d'articles. **Si un seul des deux manque, le fil
traite l'autre en entier et déclare le premier suspendu.**

**Lot 2 — L1 et L2.** Ne dépendent que des véhicules. Ils se jouent toujours.

**Lot 3 — L3.a, impositions affectées.** Dépend de l'article du PLF qui porte le
tableau d'affectation à des tiers, **et** de l'annexe 2 du tome I pour le mouvement
d'un exercice à l'autre. **Sans l'annexe : le stock se rend, le mouvement se
déclare suspendu.**

**Lot 4 — L3.b, dépenses fiscales.** Dépend de l'annexe 3 du tome II. **Sans elle,
la rubrique entière est suspendue** — et c'est une suspension, pas un néant.

**Lot 5 — L3.c, opérateurs.** Dépend des véhicules pour les créations,
suppressions et fusions. Le recensement des opérateurs du PLF n'a jamais été
ouvert ; le classeur de synthèse en tient lieu à une autre maille, et l'écart de
maille se déclare.

**Lot 6 — L4.** Dépend de `REF_doctrine` et des deux véhicules. Se joue toujours.

**Lot 7 — les quatre pièces de lecture.** *[corrigé 20261001 : le prompt n'en
nommait que deux, et les deux fils du jour ont produit les quatre.]* C'est la
sortie lisible du fil. Elle ne dépend que des véhicules, **se joue toujours, et se
rend en premier** : elle est close et versable à elle seule.

1. **L'index des mesures** — `index_mesures_<véhicule><millésime>.md`. Une ligne
   par mesure, par article, dans l'ordre du texte. La mesure est **la subdivision
   la moins profonde sous laquelle un seul siège de droit est modifié**. **Un siège
   vide n'est pas une mesure sans objet** : c'est une adresse que la grammaire n'a
   pas captée, ou une disposition sans siège.
2. **Les fiches de mesure principale** — `fiches_mesures_<véhicule><millésime>.md`.
   Une fiche courte **par article principal**, lisible par un tiers : le verbe, le
   vrai chiffre, la mécanique, ce que l'exposé des motifs dit et ce qu'il tait.
3. **La liste par article** — `<VÉHICULE><millésime>_liste.md` et son PDF.
   **Gabarit : `reference/gabarit_liste_articles.md`, qui fait foi**, y compris
   pour l'ordre du chapeau, l'entame des lignes, le balayage des pièges et le rendu.
4. **La note lisible** — `lecture_<véhicule><millésime>_lisible.md`, pour un lecteur
   qui n'ouvrira aucune des trois autres.

`appareil/index_mesures.py` est de voie `depot` : si le module n'est pas au clone,
le fil rend les quatre pièces par une grammaire locale **déclarée avant exécution à
son fragment d'arbitrages**, et livre son paquet de dépôt. Il ne renonce pas.

---

## La grille de relevé, et elle ne se réinvente plus

*[inscrit le 20261001. Sept règles mesurées par le fil de lecture du PLF 2027,
chacune imposée par une divergence constatée. Le fil PLFSS a d'abord relevé sans
elles — 314 mesures, 95 sièges vides — puis repris sa grille : 251 et 68. **Une
divergence ne se corrige pas au résultat : c'est la grille qu'on reprend.**]*

1. **Le repère de page est le folio imprimé, mesuré, jamais le renvoi du
   sommaire.** *Mesuré au PLF 2027 : écart nul sur 391 pages pour le folio, écart
   croissant jusqu'à +21 pour le sommaire.*
2. **La profondeur de découpage d'une mesure est bornée à deux niveaux.**
3. **Garde d'ordre sur les marqueurs** : un marqueur n'est retenu que si sa valeur
   excède celle du précédent au même niveau.
4. **Garde de rang 1** : un bloc ne se découpe que si son premier sous-marqueur est
   `I`, `A`, `1°` ou `a`.
5. **`I`, `V` et `X` ne sont pas des marqueurs de second niveau.**
6. **Les passages entre guillemets sont blanchis avant toute détection de siège, et
   le blanchiment traverse les lignes.** **Offsets préservés.** *Mesuré au PLF :
   41 sièges faux.*
7. **Le contexte de pièce se porte le long de l'article et ne se met à jour que sur
   une formule de modification.**

**Ce que cette grille ne fait pas, et qui se déclare** : elle relève les adresses
**citées**, pas seulement celles que la subdivision modifie. Le tri des portes est
l'affaire du bloc L2.

---

## Le critère de mesure principale

**Il s'applique à la maille de l'article, non de la mesure.** *[corrigé 20261001 :
appliqué à la mesure, il retenait 206 mesures au PLF. À la maille de l'article :
54 sur 90 au PLF, 37 sur 49 au PLFSS.]*

Un article est principal s'il porte un montant propre dans un état, une annexe ou
un tableau d'équilibre ; s'il touche un de nos objets au sens de L3 ; ou s'il est
parmi les plus chargés en adresses ouvertes. **La sélection est elle-même un relevé
et se verse avec sa liste de non-retenus.**

**Un montant écrit dans le texte cité du dispositif est un chiffre du texte, pas un
chiffre de l'exposé.** Les paramètres — taux, plafonds, seuils — se rendent sous le
nom de « chiffre porté par le dispositif ».

**Au lancement, les annexes ne sont pas parues.** Les lots 3 et 4 partent suspendus
et **se rejouent seuls à leur arrivée, sans toucher au reste**.

---

## Les pièges mesurés, et comment on ne les rejoue pas

**Un agrégat ne se lit pas, il se rejoue**, recette déclarée **avant**. Sans
recette, la valeur sort `introuvable` avec son motif.

**Un séparateur de milliers est une seule espace suivie de trois chiffres.**

**La mise en page est l'information là où la pièce compose un tableau.** Côté
PLFSS, les tableaux vivent dans les alinéas et non hors-alinéa : ne pas conclure au
trou avant d'avoir regardé là.

**La géométrie de colonne n'est pas stable.** Une colonne qui ne se découpe pas à
bornes fixes se déclare **non relevée** ; elle ne se devine pas.

**Toute valeur porte son repère** : pièce, article, emplacement, page, libellé
exact de la ligne.

**Les intitulés d'article ne sont pas acquis d'un millésime à l'autre.** Le PLFSS
2026 ne titrait pas ses articles ; **le PLFSS 2027 les titre lui-même**. Le fil
mesure lequel des deux cas s'applique et le déclare.

**Le format du livrable se réinscrit en tête de chaque passe.**

---

## Les deux relevés obligatoires

**Les montées en charge.** L'entrée en vigueur est-elle au 1er janvier, et la
trajectoire court-elle au-delà de l'exercice ? **Relevé mécanique obligatoire ;
restitution seulement là où c'est significatif.** Le relevé intégral reste à
l'atelier et ne constitue pas une pièce.

**Les entrées en vigueur différées déjà votées.**
***[corrigé 20261001 — la consigne telle qu'elle était écrite ne peut pas être
tenue par ce fil.]*** Le relevé se tire du **droit en vigueur**, pas du véhicule, et
lire le droit en vigueur n'est pas dans ce mandat. **Ce que le fil rend** : les
entrées différées **internes** au texte qu'il lit. **Ce qu'il ne rend pas** : les
entrées différées antérieures — toute confrontation qui touche ces sièges porte la
mention du décalage sans pouvoir le qualifier. Question 40 du § B.

---

## Les bornes que le fil ne franchit pas

***[corrigé 20261001 — la première borne portait un motif faux depuis le
20260902.]***

**Tout verdict côté loi de financement plafonne à `plaidable`.** *Le motif n'est
pas que la grille des portes manque : **elle est relevée depuis le 20260902**,
arbitrage A-336 — 31 portes, 0 échec, en verbatim au dépôt de droit, portée par
`appareil/portes_domaine_lfss.py` et `reference/domaine_lfss_LO111-3.md`. Le motif
est l'arbitrage n° 3 de `methode/procedure_contre_plf.md` : **le rattachement se
plaide par l'implicite budgétaire et le contrefactuel, non par une porte du
domaine**, et la grille passe au second rang — elle dit ce qui est acquis sans
plaidoirie, pas ce qu'on tente.* **Le fil ne relève donc pas la grille : elle
existe.** Il vérifie sa date — un extrait de plus de 45 jours se déclare périmé, et
celui du 20260902 se périme le **17 octobre 2026**.

**Le rattachement au texte déposé est fabriqué et se déclare comme tel.** La base
de travail du corpus est le droit en vigueur, jamais le texte en discussion.

**Une mesure que les deux textes touchent se déclare à jambe unique** : verdict
rendu pour le véhicule lu, sans préjuger de l'autre. La jonction est un fil
distinct.

---

## Ce que le fil rend

1. **Les quatre pièces de lecture de chaque véhicule** — index, fiches, liste par
   article, note lisible. *Elles se rendent en premier et sont versables seules.*
2. `livrables/resume_attendu_texte_financier_2027.md`, quatre blocs, chaque
   rubrique dans un des quatre états.
3. La table de repères du résumé, extraite **mécaniquement**, et son relevé de
   confrontation joué par `appareil/confronter_lecture.py`. *Si le module n'est pas
   au clone, le fil rend la table seule, le dit, et continue.*
4. Le relevé des entrées en vigueur différées internes et des montées en charge.
5. La liste des rubriques suspendues, avec la pièce qui les rouvrira.
6. Son fragment de journal, et un fragment d'arbitrages s'il a tranché de la
   tambouille — **dont sa grammaire de relevé, déclarée avant exécution**.

**Ce qu'il ne rend pas** : aucune rédaction, aucun amendement, aucune adresse,
aucun verdict de recevabilité, aucun chiffre neuf au référentiel des faits.
