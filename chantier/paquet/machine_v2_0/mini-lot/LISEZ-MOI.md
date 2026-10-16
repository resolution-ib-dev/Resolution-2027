# Mini-lot — comment le jouer

Le mini-lot est la **recette** de la machine : il prouve qu'une installation
neuve rend un amendement déposable de bout en bout, et il se joue **avant tout
autre travail**. Une machine dont le mini-lot ne passe pas ne produit rien de
déposable, quoi qu'elle produise par ailleurs.

## Les trois pièces

| pièce | ce qu'elle est |
|---|---|
| `enonce.md` | la mesure en langage ordinaire, telle qu'un auteur la dit, et les six étapes que la chaîne doit jouer |
| `sortie_attendue.md` | l'amendement tel que la chaîne l'a rendu — **une pièce réelle de la liasse du dépôt 2027**, non un spécimen écrit pour le test |
| le présent fichier | le mode d'emploi |

## Comment on le joue

**Temps 1 — la chaîne d'impression, sans modèle.**

```
python3 tests/test_recette.py
```

Confronte `sortie_attendue.md` au gabarit de liasse et l'imprime en .docx, en
vérifiant que l'invariant de caractères tient. Ce temps ne demande ni base de
droit ni modèle : il mesure la chaîne d'impression et le gabarit.

**Temps 2 — la chaîne de production, avec le modèle.**

Donnez `enonce.md` à votre projet Claude, muni des procédures et des
référentiels du paquet, et laissez-le rendre l'amendement. Puis :

```
python3 tests/test_recette.py --sortie /chemin/vers/votre_amendement.md
```

## Ce qui fait recette, et ce qui n'en est pas

La recette **ne demande pas un texte identique au caractère**. Deux rédacteurs
compétents écrivent deux exposés sommaires différents sur la même mesure, et
c'est normal.

Elle demande que **quatre points concordent** :

| point | pourquoi il décide |
|---|---|
| **le vecteur** | les articles à modifier. Un vecteur faux rend l'amendement inopérant, quelle que soit sa rédaction |
| **le véhicule** | une mesure portée dans le mauvais véhicule est irrecevable |
| **l'entrée en vigueur** | une date absente ou fausse change ce que la mesure fait |
| **le gage** | une pièce qui perd une recette sans gage n'est pas déposable |

**Un écart de rédaction n'est pas un échec de recette. Un écart de vecteur en
est un.**

## Si le temps 2 échoue

L'échec nomme le point et les deux valeurs. Trois causes, dans l'ordre de
fréquence :

1. **la base de droit n'est pas installée ou son millésime est périmé** — jouer
   `python3 tests/test_droit.py` ; sans verbatim du texte en vigueur, aucun
   vecteur ne se trouve, il se devine ;
2. **une procédure n'a pas été activée** — l'énoncé nomme les six étapes et la
   procédure de chacune ; une étape sautée se voit au point qui manque ;
3. **le modèle a approché au lieu de relever** — c'est le défaut que la machine
   est faite pour empêcher. La base de droit **lève** sur un article absent
   plutôt que d'en rendre un voisin. Un vecteur qui ne se trouve pas se déclare
   introuvable.
