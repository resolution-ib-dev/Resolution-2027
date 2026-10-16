# Structure d'une PPL(C/O) déposable

## Choix du véhicule

| Objet | Véhicule | Base |
|---|---|---|
| Révision de la Constitution | PPLC | art. 89 C |
| Loi organique (LOLF, LOLFSS, statut des magistrats...) | PPLO | art. 46 C |
| Loi ordinaire | PPL | art. 39 C |

Un même projet politique peut exiger plusieurs véhicules (révision constitutionnelle + LO d'application) : produire alors des documents séparés, avec dans l'exposé des motifs de chacun un renvoi à l'économie d'ensemble.

## Ordre du document

1. **Page de titre**
2. **Exposé des motifs**
3. **Dispositif** (« PROPOSITION DE LOI [CONSTITUTIONNELLE / ORGANIQUE] », puis les articles)
4. Le cas échéant : chapitre de **dispositions transitoires et finales**
5. Le cas échéant (PPL/PPLO uniquement) : **gage** en dernier article

## Page de titre

Mentions, dans l'ordre (modèle Assemblée nationale ; adapter pour le Sénat) :

```
ASSEMBLÉE NATIONALE                        [ou : SÉNAT]
CONSTITUTION DU 4 OCTOBRE 1958
[DIX-SEPTIÈME] LÉGISLATURE                 [Sénat : SESSION ORDINAIRE DE 20XX-20XX]

Enregistré à la Présidence de l'Assemblée nationale le [date]

N° [___]

PROPOSITION DE LOI CONSTITUTIONNELLE
[intitulé]

présentée par
[M./Mme Prénom NOM], député[e/s]   [ou : sénateur/sénatrice]

(Renvoyée à la commission des lois constitutionnelles, de la législation
et de l'administration générale de la République, à défaut de constitution
d'une commission spéciale...)
```

Numéro et date d'enregistrement laissés en blanc `[___]` : remplis au dépôt.

## Intitulé

- Neutre et descriptif ; pas de slogan. Formes : « portant révision de l'article X de la Constitution », « portant révision des articles X, Y et Z de la Constitution », « relative à [objet] », « visant à [objet] » (forme plus militante, admise pour les PPL).
- Un intitulé qui liste plus de quatre ou cinq articles bascule vers la forme thématique (« relative à la sincérité budgétaire et au consentement à l'impôt »).

## Exposé des motifs

Court. Mouvement obligé : **des principes vers les conséquences** — le lecteur doit d'abord adhérer à des principes compréhensibles, clairs et rassurants, avant de rencontrer la technique.

1. **Les principes** (1-2 paragraphes) : les principes simples que la réforme sert, formulés positivement et sans jargon — ce que chacun peut approuver (le consentement à l'impôt, la continuité de l'État, l'égalité devant la loi...). Rassurer : dire ce qui ne change pas autant que ce qui change. Le constat du mal vient à l'appui des principes, pas avant eux ; au plus deux ou trois chiffres sourcés.
2. **Les conséquences** (1 paragraphe) : comment le texte tire de ces principes des règles précises — l'économie générale, en une transition courte.
3. **Le commentaire par article** : un paragraphe par article ou groupe cohérent (« Les articles 3 à 5 tirent les conséquences de... »). Chaque paragraphe relie l'article au principe dont il découle, dit exactement ce qu'il fait, sans paraphraser le dispositif.

Ton : sobre, affirmatif, sans adjectifs d'intensité. Concision stricte : chaque phrase supprimée qui ne manque pas devait l'être. Tout chiffre est sourcé ou entre crochets `[à vérifier]`.

## Dispositif

- `Article 1er`, puis `Article 2`, `Article 3`...
- Subdivisions internes : `I. / II.`, puis `1° / 2°`, puis `a) / b)`.
- Un article de PPL = un objet cohérent (typiquement : un article modifié du texte hôte). Regrouper dans un même article de PPL des modifications de plusieurs articles hôtes seulement si elles forment un tout indissociable.

## Gage (PPL et PPLO)

Uniquement si le texte crée ou aggrave une charge publique ou diminue une ressource (art. 40 C). Formule usuelle :

> La charge pour l'État est compensée à due concurrence par la création d'une taxe additionnelle à l'accise sur les tabacs prévue au chapitre IV du titre Ier du livre III du code des impositions sur les biens et services.

Les PPLC ne sont pas soumises à l'article 40 : pas de gage.

## Recevabilité — points de vigilance

- **PPLC** : limites de l'art. 89 (pas de révision pendant une vacance ou une atteinte à l'intégrité du territoire ; forme républicaine du Gouvernement non révisable).
- **PPLO** : rester dans le domaine organique tel que la Constitution le renvoie ; toute disposition de nature ordinaire glissée dans une LO sera déclassée.
- **PPL** : art. 40 (charge) et art. 41 (domaine réglementaire).
- Signaler dans une note au demandeur, hors document, tout risque identifié — ne pas l'écrire dans l'exposé des motifs.

## Production docx

Lire la documentation docx de votre atelier avant génération. Conventions de mise en forme : corps de texte justifié, articles en petites capitales centrées (« Article 1er »), texte cité en retrait avec guillemets français, exposé des motifs avant le dispositif séparé par un saut de page, page de titre centrée. Nom de fichier : `PPLC_[objet]_YYYYMMDD_vN.docx` (date via `date +%Y%m%d`).
