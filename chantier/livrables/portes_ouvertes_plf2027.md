# Portes ouvertes par le PLF 2027

*Bloc L2 de la lecture du millésime. Une porte ouverte est un couple
(texte, article) que le PLF modifie lui-même. L'exposé des motifs n'en ouvre
aucune : il est de l'indice, jamais de la porte.*

**424 couples (texte, article) ouverts, dans 66 textes**, par les 89 articles du
PLF 2027 déposé le 1er octobre 2026.

Référentiel : `referentiels/portes_ouvertes_plf2027.tsv` — une ligne par couple,
colonnes `texte`, `article`, `articles_du_PLF`, `mesures`, `pages`, `confiance`.
La colonne `mesures` renvoie à `livrables/index_mesures_plf2027.md`, où chaque
référence porte sa subdivision exacte et son texte.

## Où le texte ouvre le plus

| texte | portes |
|---|---|
| code des impositions sur les biens et services | 92 |
| code général des impôts | 86 |
| code général des collectivités territoriales | 35 |
| code du travail | 18 |
| code des pensions civiles et militaires de retraite | 14 |
| code général de la fonction publique | 13 |
| code de l'énergie | 12 |
| livre des procédures fiscales | 12 |
| loi de finances pour 2021 | 11 |
| lois de finances pour 2005 et 2006 | 14 |
| code des assurances, code de la construction, code forestier, code des transports | 6 chacun |

Les 55 autres textes portent de 1 à 6 portes : code de l'environnement, code de la
santé publique, code de l'éducation, code de la route, code des douanes, code
monétaire et financier, code de procédure pénale, code électoral, code de la
défense, code rural, code du tourisme, code de la mutualité, code de la recherche,
code de la commande publique, code de l'action sociale et des familles, et une
vingtaine de lois de finances antérieures.

## Ce que le relevé permet, et ce qu'il ne dit pas

**Il permet** de savoir, pour toute mesure du corpus, si le véhicule touche déjà
son siège — donc si l'amendement se greffe sur un article existant du PLF ou
exige un article additionnel. C'est l'entrée de `vecteur-mesure` et le préalable
de tout test de rattachement.

**Il ne dit pas** si la mesure est recevable, ni quelle rédaction opposer. Et il
porte sur le **droit en vigueur au dépôt** : là où une loi antérieure a posé une
entrée en vigueur différée, le siège ouvert n'est pas celui qui sera applicable au
1er janvier 2027. Ce relevé-là reste dû.

## Trente et une adresses marquées « à vérifier »

La grammaire de relevé rattache un article à la dernière pièce déclarée modifiée.
Trente et une lignes sortent sous une forme étrangère à leur texte — un numéro nu
dans un code qui numérote en `L.`, ou l'inverse — et sont marquées comme telles
dans le référentiel. Contrôle fait sur échantillon : ce sont des renvois, non des
sièges. « Code général des collectivités territoriales, art. 73 » est l'article 73
**de la Constitution** ; les articles 2, 3, 7, 10 à 12, 19, 20, 27 à 51 attribués
au code des impositions sur les biens et services sont ceux de l'ordonnance qui
porte sa partie législative. **Elles ne se corrigent pas ici** : elles se
retranchent à la lecture, et la grammaire se reprend au module dû.

Les 393 autres sont relevées.
