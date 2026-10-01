# La règle des énoncés d'entrée de l'éval de la rédaction cible

Écrite le 20260904, **avant qu'un seul énoncé soit rédigé**, et avant que le fil
rédacteur soit ouvert. Sans elle, l'éval mesure la complaisance de celui qui
écrit les entrées.

---

## Le problème qu'elle résout

La skill reçoit un énoncé en langage naturel et une adresse. Elle rend trois
colonnes et une disposition modificative. **Un énoncé rédigé trop près de la
disposition de l'administration fabrique la réponse** : écrire « abroger le 7°
du II de l'article 150 U » donne à la fois l'opération et la portée, et il ne
reste rien à mesurer.

À l'inverse, un énoncé trop lointain ne mesure pas la rédaction cible mais la
divination : si l'énoncé ne dit pas quel effet est cherché, deux rédactions
différentes sont également justes et la correspondance ne veut plus rien dire.

L'énoncé doit donc porter **l'effet de droit voulu, entièrement**, et **aucune
indication de la forme qui l'écrit**.

---

## Ce que l'énoncé porte

1. **L'effet de droit recherché, en entier.** Tout ce que la disposition de
   l'administration produit doit être déductible de l'énoncé par un juriste qui
   a le droit en vigueur sous les yeux. Un effet omis est une entrée fausse, pas
   un cas difficile.
2. **Le texte et le numéro d'article visés** — « l'article 150 U du code général
   des impôts ». C'est l'adresse que le contrat fait recevoir à E4 depuis E2 :
   la trouver est le travail d'une autre étape, déjà éprouvée.
3. **Rien d'autre.**

## Ce que l'énoncé ne porte jamais

- **Aucun verbe de la grammaire modificative** : abroger, supprimer, remplacer,
  insérer, compléter, rétablir, réécrire, créer, ainsi rédigé, ainsi modifié.
  Ce sont les six opérations du contrat, et c'est ce qu'on mesure.
- **Aucun numéro de subdivision** — pas de I, de 1°, de a), de « deuxième
  alinéa », de « dernière phrase ». Choisir le segment attaqué est le travail de
  la skill.
- **Aucun compte** : ni « en trois endroits », ni « les deux articles ».
- **Aucun mot repris à la disposition de l'administration**, hors les termes du
  droit en vigueur qu'on ne peut pas ne pas employer — un nom d'impôt, un
  intitulé de dispositif.

## Comment il se rédige

**Depuis le droit en vigueur, jamais depuis l'alinéa.** Le rédacteur lit
l'article visé au dépôt de droit, à la date du dépôt du texte — `2025-10-01` —,
puis dit ce que la mesure change à ce qu'il vient de lire. La disposition de
l'administration ne sert qu'à savoir **quel** effet décrire, jamais **comment**
le dire.

**Une à quatre phrases**, à l'indicatif présent ou à l'infinitif, dans la langue
d'un cabinet qui commande une mesure — pas dans celle d'un légiste.

**Quand l'effet ne se laisse pas dire sans nommer une subdivision** — un
dispositif dont le seul nom est sa place dans l'article —, le cas se déclare
`indicible` et sort du compte. Il se compte à part : c'est une limite du banc,
pas une note.

---

## Le contrôle

`appareil/controle_enonces.py` vérifie mécaniquement, sur chaque énoncé :

- aucun verbe de la liste fermée ;
- aucun marqueur de subdivision ;
- l'article visé nommé une fois au moins ;
- la longueur.

Un énoncé qui sort au contrôle se réécrit **avant** que la skill soit jouée,
jamais après avoir vu ce qu'elle en fait.
