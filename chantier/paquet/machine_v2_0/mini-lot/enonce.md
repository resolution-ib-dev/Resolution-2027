# Mini-lot — l'énoncé

Un tiers qui installe la machine joue ce mini-lot avant tout autre travail. Il
part d'un énoncé en langage ordinaire et doit rendre un amendement déposable.

## La mesure, telle qu'un auteur l'énonce

> La contre-valeur des titres-restaurant et des titres-transport qu'un salarié
> n'a pas utilisés avant leur date de validité ne lui revient pas aujourd'hui.
> Je veux qu'elle lui soit versée, en salaire, par son employeur.

## Ce que la chaîne doit rendre

1. **le vecteur** — les articles du code du travail à modifier, trouvés et non
   devinés, par la procédure de `procedures/procedure_vecteurs.md` ;
2. **le véhicule et son rattachement** — par `procedures/test_rattachement.md` ;
3. **la disposition modificative** — par `procedures/regles_forme_canonique.md`,
   prouvée par réapplication au texte en vigueur ;
4. **l'entrée en vigueur et le gage** — par `procedures/gage.md` ;
5. **l'exposé sommaire** — par `procedures/gabarit_expose_sommaire.md`, deux
   cents à trois cents mots, trois temps ;
6. **l'amendement assemblé**, au gabarit de liasse, puis son .docx par
   `appareil/generateur_liasse_docx.py`.

## Ce qui fait recette

`mini-lot/sortie_attendue.md` porte l'amendement tel que la chaîne l'a rendu au
dépôt 2027 — c'est une pièce réelle de la liasse, non un spécimen écrit pour le
test. La recette ne demande pas un texte identique au caractère : elle demande
que **le vecteur, le véhicule, l'entrée en vigueur et le gage concordent**, et
que la pièce tienne son gabarit. Ce sont ces quatre points que
`tests/test_recette.py` mesure.

**Un écart de rédaction n'est pas un échec de recette. Un écart de vecteur en
est un.**
