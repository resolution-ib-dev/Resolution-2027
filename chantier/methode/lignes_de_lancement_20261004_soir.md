# Lignes de lancement — 4 octobre 2026, soir

**Porteur** : fil chef de file. **Domicile** : coffre. Chaque ligne se copie telle quelle dans
un fil neuf. Le mandat de session de code porte son texte verbatim et ne renvoie à aucun chemin
du coffre.

---

## A — Session de code : correctif des socles 2027, puis déclaration

*Mandat arrêté par le fil chef de file le 20261004 sur le compte rendu de la session précédente.
Les trois écarts sont corrigés ; les empreintes changent, c'est attendu et c'est inscrit.*

> Tu reprends le dépôt `resolution-ib-dev/Resolution-2027`, branche
> `claude/vibrant-ramanujan-8650k1`, à partir du commit `ca8b085`. Quatre fichiers y vivent dans
> `chantier/referentiels/` : `socle_texte_plf2027.json`, `socle_texte_plfss2027.json`,
> `redaction_plf2027.json`, `redaction_plfss2027.json`, produits par `socle_texte_2027.py` et
> `redaction_2027.py` à partir des projets de loi n° 3210 et n° 3211 de l'Assemblée nationale,
> 17e législature, extraits par pdftotext en mode `-layout -enc UTF-8`. Tu corriges trois écarts
> déclarés par la session précédente, et rien d'autre.
>
> Premier écart. L'article 23 du projet de loi de finances n'est pas détecté : dans le corps du
> document, son en-tête « ARTICLE 23 » ne porte pas de deux-points, et le motif de reconnaissance
> des deux scripts exige ce signe. Son texte tombe aujourd'hui dans l'exposé des motifs de
> l'article 22 du socle, et il est absent de la rédaction. Le compte attendu est de 90 articles,
> les fichiers en portent 89. Tu rends le signe de ponctuation facultatif dans le motif, sans
> élargir celui-ci d'aucune autre manière, et tu contrôles que le compte passe à 90 sans
> qu'aucun autre article ne se scinde ni ne fusionne.
>
> Deuxième écart. Les annexes ne sont pas isolées. Pour le projet de loi de finances, les états
> législatifs annexés A à G, pages 230 à 304, et les informations annexes, pages 305 à 349, sont
> rangés dans l'exposé des motifs de l'article 89 du socle — environ 449 000 caractères — et sont
> absents de la rédaction, qui s'arrête page 229. Pour le projet de loi de financement, le rapport
> annexé des pages 126 à 138, que son article 19 approuve, est rangé dans l'exposé des motifs de
> l'article 48 du socle et absent de la rédaction. Tu les sors de l'exposé des motifs du dernier
> article et tu les portes comme objets distincts, un par état législatif annexé, un pour les
> informations annexes, un pour le rapport annexé, chacun nommé par sa lettre ou son intitulé et
> portant ses pages de début et de fin. Un état législatif annexé est le siège des amendements de
> crédits : il doit être adressable, pas enfoui.
>
> Troisième écart. Dans `socle_texte_plfss2027.json`, tous les articles portent le folio 1 : le
> motif qui lit le numéro de page imprimé ne trouve rien dans cette pièce. `redaction_plfss2027.json`
> porte, lui, des numéros de page réels. Tu reprends dans le script de socle la méthode de
> pagination qui fonctionne dans celui de rédaction, et tu contrôles que les folios deviennent
> croissants et cohérents avec ceux de la rédaction.
>
> Tu rejoues l'extraction complète après correction, deux fois, et tu vérifies que les deux
> exécutions donnent des empreintes identiques. Tu mets à jour la table `socles_2027.sha256` avec
> les nouvelles tailles et empreintes, et tu y retires la mention de l'écart sur l'article 23
> puisqu'il est corrigé. Tu déclares les quatre fichiers à l'index et tu ajoutes une cible de
> régénération au Makefile : aujourd'hui rien ne les déclare et rien ne les refait. Tu ne touches
> ni aux fichiers 2026 `redaction_plf.json` et `redaction_plfss.json`, ni au module des articles
> ouverts, dont la version corrigée n'est pas au dépôt — si tu en as besoin, tu le dis et tu
> t'arrêtes, tu ne le réécris pas de mémoire. Tu ne cherches pas les annexes budgétaires des voies
> et moyens : elles sont bloquées à la source et leur recalage est remis à plus tard.
>
> Tu pousses sur la même branche et tu rends un compte rendu portant, pour chaque fichier, sa
> taille, son empreinte et son compte d'articles, le compte d'alinéas et d'adresses des deux
> fichiers de rédaction, la liste des objets d'annexe créés avec leurs pages, et tout écart que tu
> n'as pas corrigé.

## B — Fil de production : reprise de la clause générale sur le relevé des sièges

> Tu reprends la clause générale d'abolition des niches du 20261004 et tu l'achèves sur le relevé
> des sièges du même jour, qui a rendu. Activer : la skill de chantier Résolution, la skill de
> disposition cible, la skill de confrontation. Lire d'abord : la clause générale, le relevé des
> sièges et ses règles de lecture, le registre des colonnes de dépôt, le registre des sources de
> gage, l'arbitrage du 20261004 sur le gabarit obligatoire. Les 461 sièges exploitables s'insèrent
> au III de l'article 1er, et au III seul, dans l'ordre des articles du code général des impôts
> puis des autres codes et textes porteurs ; le I, le II et le IV ne se touchent pas. Les 27
> adresses de confiance moyenne — chaînes de crédit d'impôt à quatre articles liés — demandent un
> arbitrage de découpage en abrogations distinctes : tu le tranches et tu l'inscris. Les 4 lignes
> sans siège légal restent hors liste, nommées comme telles, emportées par la clause seule. Tu
> reprends les montants de l'annexe 2026 sans les changer : le recalage sur l'annexe 2027 est
> remis à plus tard et déclaré. Tu rends la clause reprise, et rien d'autre.

## C — Fil de contrôle : purge des quatre points de recevabilité

> Tu purges les quatre premiers points du contrôle de nuit du 20261003, qui touchent la
> recevabilité et le périmètre, et eux seuls : le gage pris sur une abrogation que la pièce porte
> elle-même, et les trois périmètres plus larges que ce qui a été décidé. Activer : la skill de
> chantier Résolution, la skill d'audit de conformité. Lire d'abord : le contrôle de nuit, le
> registre des sources de gage, la clause type de gage, le registre des colonnes de dépôt. Pour
> chaque point tu rends la pièce touchée, la correction exacte, et l'effet sur le registre de
> gage. Tu ne traites pas les vingt-deux autres points.

## D — Fil mécanique : numéros et adresses des textes 2027

> Tu reprends les 41 pièces déposables pour y porter les numéros des textes, désormais vérifiés :
> projet de loi de finances pour 2027, n° 3210 ; projet de loi de financement de la sécurité
> sociale pour 2027, n° 3211, Assemblée nationale, 17e législature. Les pièces portent aujourd'hui
> la mention « numéro non attribué ». Reprise mécanique, aucun arbitrage de fond : si une pièce en
> appelle un, tu l'inscris et tu passes. Tu contrôles en sortie qu'aucune occurrence de « numéro
> non attribué » ne subsiste.

## E — Nommé, non lancé

Recensement des concours discrétionnaires de l'État aux collectivités, par siège — condition de
l'étage 1 de l'arbitrage du 20261004. Aucun relevé de ce type n'existe au corpus. Attend un go.
