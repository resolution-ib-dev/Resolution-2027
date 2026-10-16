# Récupération du texte en vigueur sur Légifrance

Objectif : obtenir le texte **exact, en vigueur à la date du jour**, verbatim, avec traçabilité de version. Aucune restitution de mémoire n'est acceptable, même pour des articles célèbres : les textes bougent (révisions constitutionnelles, LO modificatives) et la fiabilité de toute la chaîne dépend de cette étape.

## Ordre des méthodes

### 1. web_fetch direct (méthode principale)

URLs stables utiles :

| Texte | URL |
|---|---|
| Constitution de 1958 (consolidée) | `https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006071194` |
| DDHC 1789 | `https://www.legifrance.gouv.fr/contenu/menu/droit-national-en-vigueur/constitution/declaration-des-droits-de-l-homme-et-du-citoyen-de-1789` |
| LOLF (LO 2001-692) | `https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000394028` |
| Article isolé | `https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI{id}` ou `https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI{id}` |

Attention : `web_fetch` n'accepte que des URLs déjà présentes dans la conversation (fournies par l'utilisateur ou issues d'un `web_search`/fetch antérieur). Ne pas construire un identifiant LEGIARTI de mémoire : passer par la recherche.

### 2. web_search puis fetch (méthode courante)

Requêtes efficaces (courtes) :
- `légifrance article 47 constitution`
- `légifrance LOLF article 8`
- `article 34 constitution en vigueur`

Prendre le résultat legifrance.gouv.fr, le fetcher, extraire le texte.

### 3. Échec des deux méthodes

Signaler explicitement l'échec. Deux options à proposer : l'utilisateur colle le texte, ou le passage est marqué `[texte en vigueur à vérifier sur Légifrance — non récupéré le YYYYMMDD]`. Ne jamais poursuivre silencieusement avec un texte de mémoire.

## Contrôles à la réception

1. **État de vigueur** : la page Légifrance affiche « Version en vigueur au [date] ». Vérifier que la version affichée est la version courante, pas une version archivée (les URLs de versions datées contiennent souvent `/lta/` ou un paramètre de date).
2. **Dernière modification** : relever la loi modificatrice mentionnée en tête d'article (« Modifié par LOI constitutionnelle n° ... » / « Modifié par LOI organique n° ... »). Cette référence figure dans le livrable.
3. **Intégrité** : compter les alinéas et vérifier qu'aucun n'a été tronqué par l'extraction HTML (les pages Légifrance intercalent parfois liens et notes ; nettoyer sans rien perdre).
4. **Cohérence croisée** : si le texte récupéré contredit une donnée du contexte projet (versions trois colonnes, etc.), le signaler — Légifrance fait foi pour le droit en vigueur ; les fichiers projet font foi pour le texte cible.

## Format du livrable de l'étape 1

Pour chaque article :

```
### Article 47 [Constitution]
Version en vigueur — modifié par LOI constitutionnelle n°2008-724 du 23 juillet 2008
Source : legifrance.gouv.fr, consulté le YYYYMMDD

[alinéa 1 verbatim]

[alinéa 2 verbatim]
...
```

Numéroter mentalement les alinéas dès cette étape (règle de décompte : chaque retour à la ligne du texte publié = un alinéa, y compris les éléments d'énumération) : la désignation « au troisième alinéa » de l'étape 3 en dépend.
