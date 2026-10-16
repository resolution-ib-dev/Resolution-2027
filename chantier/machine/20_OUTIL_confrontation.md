---
name: confrontation
description: "Confronter un livrable à la pièce qui fait foi, et éprouver le contrôle qui le vérifie. Déclencher avant d'écrire un contrôle, avant de verser un livrable adossé à une pièce, ou dès qu'il s'agit de savoir si un résultat est vérifié."
---

# Confronter un livrable à sa pièce

Un livrable adossé à une pièce — une lecture de texte, un relevé, un chiffrage,
une fiche, un découpage — ne se vérifie pas en le relisant. Il se confronte : on
rouvre la pièce et on compare.

**Un contrôle qui ne mord pas sur une faute injectée n'est pas un contrôle.**
C'est un script qui affiche zéro. Cette skill existe parce que le cas s'est
produit : six fautes injectées, trois passées sans une anomalie, et les trois qui
passaient étaient les trois seules questions qui comptaient.

---

## 1. Le repère

Chaque affirmation du livrable porte un **repère** : la pièce, l'emplacement dans
la pièce, le libellé exact de la ligne. Le repère dit **où** l'on a lu, jamais ce
qu'on a lu.

Le livrable sort une **table à plat** — une ligne par valeur, avec son repère —
à côté du texte rédigé. C'est la table qui se confronte, pas la prose.

**Sans repère, une valeur n'est pas fausse : elle est non confrontable.** Cela se
compte à part et ne se noie pas dans le taux. Un livrable sans repères est réputé
non vérifié en entier.

## 2. Les quatre verdicts, et pas de cinquième

| verdict | ce qu'il dit |
|---|---|
| concorde | la pièce, rouverte au repère, porte la valeur |
| diverge | elle en porte une autre — **les deux s'affichent** |
| introuvable | le repère ne résout pas dans la pièce |
| non sourcé | aucun repère n'a été donné |

Deux chiffres sortent, jamais un seul : le **taux de concordance** sur les
valeurs confrontables, et le **compte des non sourcés**.

Une divergence ne s'arbitre pas ici. Elle s'affiche des deux côtés et elle
remonte.

## 3. Le contrôle, et son jeu de fautes

**Le contrôle ne lit jamais un fichier que son propre générateur vient
d'écrire.** Sinon il contrôle son générateur et sort zéro par construction —
c'est la faute la plus fréquente et la plus invisible.

**Tout contrôle neuf naît avec son jeu de fautes**, versé avec lui. Le jeu
injecte une faute connue, rejoue le contrôle, et **échoue si le contrôle ne mord
pas**. Pas de jeu de fautes, pas de contrôle.

Les quatre fautes minimales, à décliner selon la pièce :

1. une valeur juste remplacée par une valeur fausse, au même repère ;
2. un repère valide remplacé par un repère qui ne résout pas ;
3. un repère retiré, la valeur restant ;
4. **le verdict lui-même retourné** — un écart déclaré conforme.

La quatrième est celle qu'on oublie, et c'est celle qui compte : elle teste que
le contrôle lit la pièce, et non le verdict que le livrable s'est donné.

Une exemption au contrôle vit dans le module de contrôle, nommée et motivée.
**Jamais ajoutée en cours d'exécution pour laisser passer ce qu'on vient de
trouver.**

## 4. Ce qui ne se confronte pas

Une partie de tout livrable est un **jugement** : une hiérarchie, un choix de
découpe, un « cela va dans le sens ». Un appareil y est aveugle par construction,
et prétendre le contrôler est précisément la faute que cette méthode empêche.

Ce qui est de jugement sort **nommé comme tel**, et n'entre dans aucun taux.

## 5. La forme de l'opération, selon la pièce

L'opération est la même partout — rejouer sur la pièce ce que le livrable
affirme. Seule sa forme change :

- la pièce est un **texte** → comparaison au repère ;
- la pièce est une **structure** → réapplication, qui doit redonner le résultat à
  l'octet ;
- la pièce est un **jugement gelé avant la passe** → banc en aveugle : un fil qui
  ne voit ni la réponse ni son motif répond à la question, et on compare.

Un jugement qui sert de référence **se gèle et se date avant** que le livrable
soit produit. Rapproché après coup, il ne mesure plus : il réconcilie.

## 6. Le contrat d'un lot

À poser en tête de tout travail qui produira un livrable :

1. **La pièce de référence est nommée avant que le travail commence.** Un travail
   qui se choisit sa référence en cours de route se note lui-même.
2. **Pas d'outillage écrit sans mandat.** Un travail qui a besoin d'un outil le
   déclare et s'arrête ; il ne l'écrit pas en passant.
3. **Réemploi avant réinvention.** L'inventaire de ce qui existe se lit. Un
   module qui duplique un format déjà lu par un autre est refusé.
4. **Aucune dérogation ajoutée à l'exécution.**
5. **Le livrable sort avec sa table de repères, son contrôle et son jeu de
   fautes.**

## 7. Le bordereau

Trois pages au plus, et c'est le seul document que le destinataire lit :

1. le taux de concordance et le compte des non sourcés ;
2. les divergences, valeur contre valeur, avec leur repère ;
3. les introuvables ;
4. ce qui relève du jugement, une ligne par point, avec la question posée.

**Le bordereau ne bloque rien.** Le travail suivant part sans l'attendre ; les
corrections rentrent quand elles rentrent. Un arrêt de vérification est à la main
de celui qui décide, jamais une condition de passage.

---

## Ce que cette skill ne fait pas

Elle ne juge aucun contenu. Elle ne comble aucun trou : une valeur sans repère
sort sans repère et se compte. Elle n'arbitre pas une divergence. Et elle
n'exécute rien — le contrôle et son jeu de fautes sont du code, qui se verse.