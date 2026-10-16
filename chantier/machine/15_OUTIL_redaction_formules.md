# Formules modificatives — répertoire légistique

Source doctrinale : Guide de légistique (SGG/Conseil d'État), fiches sur les modifications de textes. En cas de doute sur une formule, consulter le guide (`guide_legistique_2026.pdf` si présent dans le projet) plutôt qu'improviser.

## Principes de choix

1. **Une modification = la formule la plus économique qui reste lisible.** La substitution de mots pour un delta ponctuel ; le remplacement d'alinéa quand la phrase est remaniée en profondeur ; la réécriture d'article quand plus de la moitié change.
2. **Ordre de traitement = ordre du texte modifié.** Les articles de la PPL suivent l'ordre des articles modifiés ; à l'intérieur d'un article de PPL, les subdivisions suivent l'ordre des alinéas.
3. **Désignation des alinéas par leur rang ordinal** (« au premier alinéa », « au troisième alinéa ») dans le texte *en vigueur* — jamais dans le texte résultant. Attention aux décomptes après insertion/suppression : chaque disposition se lit par rapport à l'état du texte *après application des dispositions précédentes du même article de PPL*.
4. **Texte cité entre guillemets français**, précédé de deux points, chaque élément cité commençant par une majuscule et se terminant par un point avant le guillemet fermant : `sont insérés les mots : « selon des modalités fixées par la loi organique ».`
5. **Citation multi-alinéas** (réécriture ou substitution d'article) : chaque alinéa cité ouvre par « ; le guillemet fermant » n'apparaît qu'à la fin du dernier alinéa, après sa ponctuation finale :

   > « Art. X. – Premier alinéa cité.
   > « Deuxième alinéa cité.
   > « Dernier alinéa cité. »

   La ponctuation finale du texte cité précède toujours le guillemet fermant — dans le rendu produit, pas seulement dans la source.

## Répertoire des formules

### Chapeau d'article

> L'article X de la Constitution est ainsi modifié :

(puis subdivisions 1°, 2°, 3°...). Si une seule modification, pas de chapeau : formule directe.

### Substitution de mots

> Au premier alinéa de l'article X, les mots : « A » sont remplacés par les mots : « B ».

Variantes : `le mot : « A » est remplacé par le mot : « B »` ; `les mots : « A » sont remplacés par les mots : « B » et les mots : « C » par les mots : « D »` (éviter d'enchaîner plus de deux substitutions dans une même phrase).

### Insertion de mots

> Au deuxième alinéa, après le mot : « budget », sont insérés les mots : « et de ses annexes ».
> Au deuxième alinéa, avant les mots : « la loi de finances », sont insérés les mots : « chaque année, ».
> Le premier alinéa est complété par les mots : « dans les conditions prévues par la loi organique ».

### Suppression de mots

> Au troisième alinéa, les mots : « A » sont supprimés.

### Remplacement d'alinéa

> Le deuxième alinéa est remplacé par un alinéa ainsi rédigé :
> « [texte]. »

Remplacement par plusieurs alinéas : `est remplacé par trois alinéas ainsi rédigés :`.

### Insertion d'alinéa

> Après le premier alinéa, il est inséré un alinéa ainsi rédigé :
> « [texte]. »

En tête : `Avant le premier alinéa, il est inséré...` ; en fin : `L'article X est complété par un alinéa ainsi rédigé :`.

### Suppression d'alinéa

> Le quatrième alinéa est supprimé.

(« supprimé » pour un alinéa ou des mots ; « abrogé » pour un article, un titre, un chapitre ou un texte entier.)

### Réécriture complète d'article

> L'article X de la Constitution est ainsi rédigé :
> « Art. X. — [texte intégral]. »

### Création d'article

> Après l'article X de la Constitution, il est inséré un article X-1 ainsi rédigé :
> « Art. X-1. — [texte intégral]. »

Numérotation des articles insérés dans la Constitution : suffixe numérique (61-1, 61-2). Dans les lois et codes : bis, ter, quater... ou numérotation à tiret selon l'usage du texte hôte — respecter l'usage du texte modifié.

### Abrogation

> L'article X de la Constitution est abrogé.
> Le titre VIII de la Constitution est abrogé.
> Les articles 68-1 à 68-3 de la Constitution sont abrogés.

### Modification d'intitulé

> L'intitulé du titre XII de la Constitution est ainsi rédigé : « [nouvel intitulé] ».

### Renumérotation / déplacement

À éviter autant que possible (casse les renvois externes). Si indispensable :
> L'article X devient l'article Y.
Et traiter **explicitement** chaque renvoi interne affecté par une disposition de coordination.

## Dispositions de coordination et transitoires

- **Coordination** : chaque référence, dans le reste du texte modifié ou dans d'autres textes, à un article supprimé, renuméroté ou dont le contenu change de sens, fait l'objet d'une disposition propre. Le diff structuré ne les détecte pas : les rechercher systématiquement (grep des occurrences « article X » dans le texte consolidé et les textes liés).
- **Transitoires** : entrée en vigueur différée (`La présente loi entre en vigueur le...` / `Les dispositions de l'article N s'appliquent à compter de...`), sort des situations en cours, textes réglementaires maintenus. Pour une PPLC touchant aux mandats : préciser à quels mandats/élections la règle nouvelle s'applique pour la première fois.

## Pièges récurrents

- **Décompte des alinéas** : sur Légifrance, chaque retour à la ligne compte, y compris les 1°, 2° d'une énumération. Vérifier le décompte sur le texte récupéré à l'étape 1, pas sur une édition privée.
- **« Remplacé » vs « ainsi rédigé »** : un alinéa est *remplacé par un alinéa ainsi rédigé* ; un article est *ainsi rédigé* (réécriture) ou *remplacé par les dispositions suivantes* (substitution, usage étape 5).
- **Ponctuation citée** : la ponctuation fait partie des mots cités. Pour modifier une ponctuation seule : `le signe : « ; » est remplacé par le signe : « . »` — ou inclure la ponctuation dans les mots remplacés, plus lisible.
- **Cascades internes** : quand un même article de PPL supprime le deuxième alinéa puis modifie « le quatrième », dire si le décompte s'entend avant ou après suppression. Convention retenue : chaque subdivision (1°, 2°...) se lit sur le texte tel qu'il résulte des subdivisions précédentes. En cas d'ambiguïté résiduelle, préférer remplacer l'alinéa entier.
