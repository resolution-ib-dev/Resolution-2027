# Prompt — le gabarit du nœud de mise en œuvre, et le premier nœud

> **PROPOSÉ, NON VALIDÉ.** Ce document est de la matière préparatoire, pas
> l'ouverture d'un lot. **Le lot lui-même est de l'auteur** — il est à
> `methode/a_trancher.md`, bloc « Tranché le 20260917 par l'auteur » : *second
> cercle du socle, puis le gabarit du nœud et la sortie des fonctionnaires, puis
> le tri par véhicule.* Ce qui suit en rassemble la matière trouvée en chemin ;
> **c'est au fil chef de file de dicter la suite**, et de décider si ce prompt
> l'ouvre, sous quelle forme et avec quel mandat. Un fil de travail inscrit et
> s'arrête.

*Si un fil s'ouvre là-dessus, ce sera un **fil Cowork** : il rédige, il remplit,
il contrôle, il verse.*

**Rassemblé le 20260917 par le fil du second cercle du socle**, qui a fait passer
cinq termes de `estimé` à `porté` sans produire aucune valeur, et qui laisse
derrière lui **un terme à produire et un seul** : la reprise par l'État des
missions de solidarité départementales, que `B-03` suppose et qu'aucune pièce du
corpus ne porte.

---

## 0. Ce que ce fil est

**Il produit de la matière neuve, et c'est ce qui le sépare du précédent.** Le
second cercle du socle n'a rien créé : il a rendu rejouable ce qui ne l'était pas.
Celui-ci écrit ce qui n'existe pas — un gabarit, puis un nœud rempli.

**Il en écrit un seul.** C'est l'arbitrage du 20260917 : *le nœud de mise en
œuvre existe comme objet, et on en écrit un seul d'abord. Les six autres
attendent ce que ce premier aura coûté. Sept reste une proposition, pas un
décompte.* Écrire les sept d'un coup serait refaire la faute que le CR de la
machine d'amendement nomme en premier — reconstruire au lieu d'avancer.

**Le premier nœud est la sortie des fonctionnaires**, et il l'est par l'ordre des
lots, non par choix de ce fil.

---

## 1. Ce qu'il reçoit

Les trois documents d'usage — `methode/index.json`,
`methode/prompt_fil_courant.md`, `methode/arbitrages.md` — puis, et cela seul :

```
methode/a_trancher.md                        les questions ouvertes et la dette
livrables/comblement_termes_manquants.md     ce qui est porté, ce qui reste
methode/grille_lecture_budgetaire.md         comment se lisent les annexes
livrables/blocs_lot_C.md                     les bilans des blocs, dont B-02
```

**Le socle budgétaire se refait, il ne se déplie pas** : c'est un dérivé, il ne
va pas au coffre. Les classeurs sont des pièces jointes et se convertissent dans
l'atelier :

```
soffice --headless --convert-to xlsx --outdir sources/plf <fichier>.xls
make referentiels/socle_budgetaire.json
make controle
```

**Ce que le socle porte désormais et qui sert directement ici** : la chaîne des
emplois et des charges (`S9`), l'onglet `Capitalisation` — *non importé*, mais
c'est lui qui porte l'horizon de sept ans —, et l'arbre des économies avec ses
hypothèses en toutes lettres.

---

## 2. Ce qui se fait, dans l'ordre des dépendances

### 2.1 Le gabarit d'abord, et il se rédige avant d'être rempli

Un nœud de mise en œuvre répond à quatre questions, et le gabarit les fixe une
fois pour toutes :

- **qui reprend** — l'entité qui hérite de la charge, nommée ;
- **à quel rythme** — le calendrier, et ce qui se passe à chaque palier ;
- **à quel coût** — le chiffrage, avec sa qualification au sens de la grille :
  assiette, part supprimable, économie restituée, paramètre ;
- **ce qu'il advient des cas non repris** — le résidu, qui est la question que
  l'on oublie et qui revient toujours.

**Le gabarit n'est pas un plan de document, c'est un contrat de contenu.** Ce que
`methode/contrat_chaine_amendement.md` est à la chaîne d'amendement, celui-ci
l'est au nœud : il dit ce qu'un nœud doit porter pour être un nœud, et un
contrôle doit pouvoir le vérifier.

**Question de fond, inscrite et non tranchée** — portée à `methode/a_trancher.md`
sous le n° 23 : un nœud de mise en œuvre est-il un artefact du corpus à part
entière — son propre fichier, sa propre famille — ou une section des bilans de
blocs ? *L'argument qu'on peut verser au débat, et rien de plus : sept nœuds
logés dans les bilans les rendraient illisibles.*

### 2.2 Le premier nœud, rempli sur pièce

La sortie des fonctionnaires est le nœud dont le corpus porte déjà le plus :

| ce qui existe | où | bouclage |
|---|---|---|
| 90 % de départs, 70 % du traitement maintenu | `Détail Economies`, colonne Hypothèses | `S9` |
| l'horizon de sept ans | `Capitalisation`, « Année 7 fonctionnaires » | aucun — **onglet non importé** |
| 61 400 ETP d'État, 151 000 État et opérateurs, 580 000 toutes administrations | `Détail Economies`, notes de dérivation | `S9`, avec deux écarts de concept ouverts |
| 0,9 Md€ d'économie, **déjà nette de l'indemnité** | `Détail Economies` et `Gages` | `S9`, `S11` |

**La conséquence de lecture de `B-02` se reporte ici et elle est contre-intuitive** :
l'économie de masse salariale du corpus est déjà nette de l'indemnité. Le nœud ne
doit donc pas la retrancher une seconde fois — c'est exactement le genre de
double compte que le relevé de comblement a rendu visible.

**Ce que le nœud devra produire et que rien ne porte** : le profil de l'indemnité
dans le temps, le sort des agents que la sortie ne couvre pas, et ce qui advient
au terme des sept ans. Ce sont des valeurs neuves, elles se produisent ici, et
**elles se déclarent comme produites** — pas comme lues.

### 2.3 L'onglet `Capitalisation`, à trancher

Il porte l'horizon de sept ans et il n'est pas importé au socle. **Question de fond, inscrite et non
tranchée** — portée à `methode/a_trancher.md` sous le n° 24. Deux voies :
l'importer avec son bouclage, ce qui est un lot d'appareil sur le modèle du
second cercle ; ou citer la ligne sans bouclage et déclarer le terme `estimé`.
*L'argument qu'on peut verser au débat : un nœud bâti sur un chiffre sans
garde-fou est un nœud qu'il faudra refaire.*

---

## 3. Ce que ce fil ne fait pas

Il n'écrit pas les six autres nœuds. Il ne rouvre pas les bilans de blocs — y
reporter une valeur est un lot de production, et il vient après. Il ne corrige
pas `controle_blocs.py`, dont le contrôle `D2` attend que l'origine du
« 108,56 Md€ » soit déclarée : elle est au socle depuis le 20260917, et c'est le
fil qui rouvre les blocs qui la porte. Il ne pousse rien au dépôt (A-393).

Il n'écrit pas à la main au journal ni au registre : **il dépose un fragment
daté** — `methode/fragments/<cible>/<AAAAMMJJ>-noeud.md` — et
`appareil/fragments.py` assemble.

---

## 4. La règle qui précède l'écriture

**Un contrôle neuf porte son jeu de fautes et son jeu de justes.** Le second
cercle du socle l'a appliqué sur sept bouclages —
`appareil/epreuve_controle_socle.py`, quatorze fautes et sept justes — et le jeu
de justes a fait son travail : il a obligé à séparer, à l'onglet `Perdants`, ce
qui se somme de ce qui ne se somme pas.

Si ce fil écrit un contrôle du gabarit — et il le devrait, sans quoi le gabarit
est une intention —, il porte les deux jeux. C'est la question 11 du registre,
appliquée avec la valeur retenue faute de réponse, et désormais inscrite à
`methode/grille_lecture_budgetaire.md`.

---

## 5. La dette, qui ne se laisse pas derrière

Le paquet `methode/paquet_depot_socle_20260917.md` porte six pièces d'appareil
dues au dépôt et la liste de ce qui restait des fils antérieurs. **Deux modules
sont perdus, non dus** : `appareil/plier_paquet.py` et
`appareil/controle_projection.py`, déclarés de voie `depot` et absents du clone.

Ce qui était dû le matin du 20260917 et qui est **fait** : les quarante-cinq
artefacts du coffre absents de la table curée sont portés, l'index passe de 252 à
287, et `make reindex` n'en perd plus aucun.

---

## 6. Ce qu'il rend

1. Le gabarit du nœud de mise en œuvre, et son contrôle avec ses deux jeux.
2. Le premier nœud, rempli sur la sortie des fonctionnaires, avec pour chaque
   valeur : lue ou produite, et sous quelle qualification.
3. Ce que ce premier nœud aura coûté — c'est ce que les six autres attendent.
4. Le paquet de dépôt à jour.
5. Ce qu'il laisse ouvert, inscrit à `methode/a_trancher.md`. **Il ne désigne pas
   le lot suivant** : c'est au fil chef de file de le dicter.

## 7. Conduite

Ce fil produit. **Une question de fond s'inscrit et attend** — elle ne se tranche
pas en propre, et elle ne se règle pas par une « valeur retenue » glissée dans un
prompt. Ce qui se tranche seul est la tambouille : méthode de détail, appareil,
index, nommage, ordre d'exécution. **Une règle qu'il outille s'inscrit là où
la règle est lue** — jamais dans un document nouveau qui doublerait un document
existant.

**Une divergence ne se corrige pas au socle.** Elle dit que la grille est fausse,
et c'est la grille qu'on reprend.
