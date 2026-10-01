# Prompt — fil « lecture des textes financiers 2027 »

*Fil Cowork, chantier 3. Il lit le PLF et le PLFSS déposés et rend le résumé en
forme fixe. Il ne rédige aucun amendement, ne qualifie aucune mesure en droit, ne
produit aucune adresse : c'est un fil du projet doctrine.*

**La seule date du chantier qui ne se négocie pas.** Un texte déposé ne se relit
pas l'année suivante : les pièces disparaissent des points d'accès et la lecture
en creux — amendements, sorts, débats — n'existe plus. Ce fil se joue à chaud.

---

## Ligne de lancement

> Fil Cowork — lecture des textes financiers 2027. Socle : `methode/socle_prompt_fil.md`. Pièces à joindre : le PLF 2027 et le PLFSS 2027 en PDF, **les deux** ; et, si elles sont parues, l'annexe 2 du tome I de l'évaluation des voies et moyens (taxes affectées) et l'annexe 3 du tome II (dépenses fiscales). Activer `methode/prompt_fil_lecture_textes_2027.md`, `livrables/resume_attendu_texte_financier_2026.md`, `livrables/bordereau_confrontation_resume_2026.md`, `livrables/index_mesures_plf.md`, `methode/procedure_contre_plf.md`, `methode/grille_lecture_budgetaire.md`, `referentiels/REF_doctrine.json`, `methode/a_trancher.md` (§ B). Mandat : rendre le résumé attendu du texte financier 2027 dans le gabarit des quatre blocs L1 à L4, **plus l'index des mesures des deux véhicules et les fiches de mesure principale**, par **modification** des gabarits 2026 et non par reconstruction, chaque lot commençant par sa mesure de présence et se sautant proprement si sa pièce manque. Aucune rédaction, aucun amendement, aucune adresse.

---

## Ce que le fil trouve en entrant, et qui le dispense de tout réinventer

Le millésime 2026 est lu, gelé et confronté. **Il n'est pas un précédent : c'est
le gabarit.** `livrables/resume_attendu_texte_financier_2026.md` donne les quatre
blocs et leurs rubriques ; `livrables/bordereau_confrontation_resume_2026.md`
donne ce qui s'est confronté, ce qui est sorti introuvable et pourquoi.

**Le fil 2026 a reconstruit son livrable trois fois de zéro au lieu de le
modifier.** C'est le premier des quatre mécanismes de faute du corpus, et il a
coûté sept refabrications. **On modifie, on ne reconstruit pas** : le résumé 2027
part du gabarit 2026, rubrique par rubrique, et chaque rubrique sort dans un des
quatre états — *reprise et à jour*, *modifiée*, *sans objet cette année*,
*suspendue faute de pièce*.

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
verdict exige un acte du texte sur le siège même que la mesure vise** ; elle a
été posée au fil 2026 faute d'arbitrage antérieur et n'est toujours pas validée.
Le fil l'applique telle quelle et le déclare.

---

## Les lots, et leur mesure de présence

**Règle générale : chaque lot commence par mesurer la présence de sa pièce, et se
saute en continuant si elle manque. Aucun lot absent n'arrête le fil entier.**
Une pièce absente produit une rubrique **suspendue**, nommée, avec ce qui la
rouvrira — jamais une rubrique vide, jamais un zéro.

**Lot 1 — les deux véhicules.** PLF et PLFSS en PDF. Empreinte sha256 relevée et
inscrite, compte de pages, compte d'articles. *Le fil 2026 n'avait pas le PDF du
PLF dans son atelier et a travaillé sur son seul reflux déterministe : toute
relecture à l'œil côté finances était impossible.* **Si un seul des deux
manque, le fil traite l'autre en entier et déclare le premier suspendu.**

**Lot 2 — L1 et L2.** Ne dépendent que des véhicules. Ils se jouent toujours.

**Lot 3 — L3.a, impositions affectées.** Dépend de l'article du PLF qui porte le
tableau d'affectation à des tiers, **et** de l'annexe 2 du tome I pour le
mouvement d'un exercice à l'autre. L'article suffit au stock ; l'annexe seule
donne le mouvement. **Sans l'annexe : le stock se rend, le mouvement se déclare
suspendu.**

**Lot 4 — L3.b, dépenses fiscales.** Dépend de l'annexe 3 du tome II.
**Sans elle, la rubrique entière est suspendue** — et c'est une suspension, pas
un néant : le texte ne porte pas ces chiffres.

**Lot 5 — L3.c, opérateurs.** Dépend des véhicules pour les créations,
suppressions et fusions. Le recensement des opérateurs du PLF n'a jamais été
ouvert ; le classeur de synthèse en tient lieu à une autre maille, et l'écart de
maille se déclare.

**Lot 6 — L4.** Dépend de `REF_doctrine` et des deux véhicules. Se joue toujours.

**Lot 7 — l'index des mesures, et les fiches de mesure principale.** C'est la
sortie lisible du fil, celle que les participants du projet ouvrent. Elle ne
dépend que des véhicules et se joue toujours.

- **L'index des mesures**, une ligne par mesure, par article, dans l'ordre du
  texte. La mesure est **la subdivision la moins profonde sous laquelle un seul
  siège de droit est modifié** : l'unité d'amendement, non l'unité de vote. Le
  gabarit existe — `livrables/index_mesures_plf.md`, 410 mesures sur 82 articles
  pour 2026 — et il se reprend tel quel. **Un siège vide n'est pas une mesure
  sans objet** : c'est une adresse que la grammaire de relevé n'a pas captée, ou
  une disposition sans siège — crédits, plafonds, garanties, entrée en vigueur.
  *Mesure de présence à faire en entrant : le millésime 2026 porte l'index du
  PLF ; vérifier si le PLFSS en a un, et le produire dans le même gabarit si
  non.* `appareil/index_mesures.py` est de voie `depot` : si le module n'est pas
  au clone, le fil rend l'index et livre son paquet de dépôt, il ne renonce pas.
- **Les fiches de mesure principale.** `methode/procedure_contre_plf.md` les
  déclare dues et **à industrialiser pour l'analyse du PLF 2027** : une fiche
  courte et claire par mesure principale — le vrai chiffre, la mécanique de la
  disposition, ce que l'exposé des motifs en dit et ce qu'il n'en dit pas.
  **Le chiffre d'abord, et pas celui de l'exposé des motifs** : il se prend à
  l'état, à l'annexe ou au tableau d'équilibre, et tout écart avec le montant
  annoncé à l'exposé est un signal qui se relève et ne s'arbitre pas.

**Critère par défaut de « mesure principale », tranché ici et révocable par
l'auteure** : une mesure est principale si elle remplit l'une des trois
conditions — elle porte un montant propre dans un état, une annexe ou un tableau
d'équilibre ; elle touche un de nos objets au sens de L3 ; ou son article est
parmi les plus chargés en adresses ouvertes. Les autres restent à l'index, sans
fiche.

**Deux relevés mécaniques entrent dans la fiche**, et ils s'appliquent à tous les
articles, pas aux seuls principaux : les **mots de portée** — peut, dans la
limite de, à compter de, au titre de, par dérogation, notamment —, chacun ouvrant
ou fermant quelque chose ; et les **absences attendues** — un taux modifié sans
que l'assiette bouge, un plafond posé sans indexation, une suppression sans
transitoire, un dispositif sans évaluation.

**Au lancement, les annexes ne sont pas parues.** Les lots 3 et 4 partent donc
suspendus. **Ils se rejouent seuls à l'arrivée des annexes, sans toucher au
reste** : c'est la raison d'être du découpage en lots.

---

## Les pièges mesurés en 2026, et comment on ne les rejoue pas

**Un agrégat ne se lit pas, il se rejoue.** Toute valeur dont la pièce est un
classeur ou une table sort par réapplication, avec sa recette déclarée **avant**.
Aucune recette ne s'écrit en cours d'exécution pour laisser passer ce qu'on vient
de trouver. Sans recette, la valeur sort `introuvable` avec son motif.

**Un séparateur de milliers est une seule espace suivie de trois chiffres.** La
pièce sort de `pdftotext -layout`, où les colonnes sont séparées par plusieurs
espaces : traiter toute suite d'espaces comme un séparateur colle deux nombres
en un et fait diverger des dizaines de lignes justes.

**La mise en page est l'information là où la pièce compose un tableau.** Un
alinéa de tableau garde ses lignes brutes ; l'aplatir en prose perd l'appariement
recettes / dépenses / solde et oblige à lire à l'œil. Côté PLFSS, les tableaux
vivent dans les alinéas et non hors-alinéa : ne pas conclure au trou avant
d'avoir regardé là.

**La géométrie de colonne n'est pas stable**, ni d'une page à l'autre ni à
l'intérieur d'une page. Une colonne qui ne se découpe pas à bornes fixes se
déclare **non relevée** ; elle ne se devine pas. En 2026, deux passes de lecture
sur la même colonne de rendement ont rendu deux valeurs, et aucune n'a été
retenue — c'est la bonne issue.

**Toute valeur porte son repère** : la pièce, l'article, l'emplacement —
hors-alinéa, alinéa numéroté, tableau —, la page, le libellé exact de la ligne.
Une grandeur sans repère ne s'écrit pas. C'est ce qui rend la confrontation
mécanique possible, et le taux de 2026 l'a prouvée praticable.

**Le format du livrable se réinscrit en tête de chaque passe**, et pas seulement
au départ : un fil long dérive du format demandé au fil des tours.

---

## Les deux relevés obligatoires, et ils sont faciles à oublier

**Les montées en charge.** Sur toute mesure budgétaire ou fiscale : l'entrée en
vigueur est-elle au 1er janvier, et la trajectoire court-elle au-delà de
l'exercice ? C'est ce qui décide de ce que la mesure vaut réellement, c'est
presque toujours masqué, et c'est ce qui intéresse le contribuable. **Relevé
mécanique obligatoire ; restitution seulement là où c'est significatif** — ne pas
en truffer le livrable.

**Les entrées en vigueur différées déjà votées.** Le texte 2027 travaille sur le
droit en vigueur, et c'est ce qui rend la confrontation possible — **à une
réserve près qui est le point sensible du millésime** : le droit applicable au
1er janvier 2027 n'est pas le droit en vigueur au dépôt partout où une loi
antérieure a posé une entrée en vigueur différée. Ces sièges se relèvent à part,
nommés, et toute confrontation qui les touche porte la mention du décalage.

---

## Les deux bornes que le fil ne franchit pas

**La grille des portes du domaine des lois de financement n'est pas relevée.**
Tant qu'elle manque, **tout verdict côté loi de financement plafonne à
`plaidable`** et y reste. Le fil ne forge pas un verdict plus fort, et il ne
relève pas la grille au passage — c'est un chantier de fond à part.

**Le rattachement au texte déposé est fabriqué et se déclare comme tel.** La base
de travail du corpus est le droit en vigueur, jamais le texte en discussion. Ce
fil lit le texte ; il n'y raccroche aucune de nos mesures.

---

## Ce que le fil rend

1. `livrables/resume_attendu_texte_financier_2027.md`, quatre blocs, chaque
   rubrique dans un des quatre états.
2. La table de repères du résumé, extraite **mécaniquement** du livrable, et son
   relevé de confrontation joué par `appareil/confronter_lecture.py`. *Mesure de
   présence : si le module n'est pas au clone, le fil rend la table de repères
   seule, dit que la confrontation n'est pas jouée, et continue.*
3. Le relevé des entrées en vigueur différées et des montées en charge.
4. **L'index des mesures des deux véhicules**, au gabarit de
   `livrables/index_mesures_plf.md`, et les **fiches de mesure principale** —
   c'est la sortie lisible par les participants du projet, et elle ne se replie
   pas sur le résumé analytique.
5. La liste des rubriques suspendues, avec la pièce qui les rouvrira.
6. Son fragment de journal, et un fragment d'arbitrages s'il a tranché de la
   tambouille.

**Ce qu'il ne rend pas** : aucune rédaction, aucun amendement, aucune adresse,
aucun verdict de recevabilité, aucun chiffre neuf au référentiel des faits.
