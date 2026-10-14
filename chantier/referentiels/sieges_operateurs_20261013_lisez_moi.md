# Sièges institutifs des personnes morales du III de PLF P2-06 — note de lecture, 20261013

**Objet.** Ce référentiel donne, pour chacun des **343 rangs** de la liste énumérée du III de `livrables/depot_2027/P2/2_1_dissolution_structures_facultatives.md`, le **siège institutif** de la personne morale nommée : l’article de code ou de loi qui la crée ou qui crée la catégorie dont elle relève.

**Ce qu’un siège institutif n’est pas.** Ce n’est **ni le siège de sa ressource** — l’article qui lui affecte une taxe ou une dotation — **ni son décret d’organisation**. La distinction est celle que `chantier/appareil/vecteurs.py` tient depuis le lot pilote. Elle est reprise ici sans changement.

---

## 1. Ce que couvre le relevé

| grandeur | valeur |
|---|---:|
| rangs du III | **343** |
| rangs pourvus d’un siège | **183** |
| dont confiance haute | **180** |
| dont confiance moyenne | **3** |
| rangs sans siège | **160** |

**Quatre familles à siège commun portent 153 rangs**. Chacune a été vérifiée sur l’article lui-même, jamais supposée.

| famille | rangs | siège |
|---|---:|---|
| conseils départementaux de l’accès au droit | 86 | loi n° 91-647 du 10 juillet 1991 relative à l’aide juridique, articles 54 et 55 |
| comités de protection des personnes | 39 | code de la santé publique, article L. 1123-1 |
| centres de ressources, d’expertise et de performance sportives | 17 | code du sport, article L. 114-1 |
| opérateurs de compétences | 11 | code du travail, article L. 6332-1 |

**Trente organismes sont relevés à l’unité**, dont les huit que `vecteurs.py` portait déjà et qui ont été recontrôlés à la base de droit : ADEME, AFITF, AFPA, ANAH, CNC, France Compétences, France Travail, Action Logement Services.

---

## 2. Ce qui manque

**160 rangs restent sans siège.** Ils gardent leur seule dénomination à la pièce. Ils figurent à ce référentiel avec leurs colonnes de droit vides.

| groupe | rangs | pourquoi |
|---|---:|---|
| groupements d’intérêt public de formation continue et d’insertion professionnelle | 30 | aucun article législatif du code de l’éducation ne les institue |
| centres régionaux d’information et de documentation jeunesse | 18 | aucune occurrence à la base LEGI du dépôt |
| sociétés du groupe France Télévisions | 17 | filiales de droit commun qu’aucun texte n’institue nommément |
| maisons des adolescents | 7 | seules des dispositions réglementaires les nomment |
| orchestres | 6 | associations de droit commun |
| personnes morales isolées | 82 | relevé à l’unité non fait, siège réglementaire ou texte absent du dépôt |

**Trois causes de manque, trois seulement.** **Le texte n’est pas au dépôt** : le code forestier, le code de la sécurité intérieure et la loi n° 86-1067 du 30 septembre 1986 ne sont pas portés par l’extrait. Les sièges du Centre national de la propriété forestière, du Conseil national des activités privées de sécurité et des sociétés de l’audiovisuel public n’ont pas été lus. **Le siège est réglementaire** : un établissement créé par décret n’a pas d’article de loi à nommer. **Il n’y a pas de siège** : une association ou une société de droit commun n’est instituée par aucun texte.

**Un arbitrage est inscrit ici. Il ne se rouvre pas.** Les groupements d’intérêt public dépourvus de texte propre **ne reçoivent pas le régime général des groupements d’intérêt public comme siège institutif**. Une forme juridique n’est pas une catégorie : le chapitre II de la loi n° 2011-525 du 17 mai 2011 dit ce qu’est un groupement d’intérêt public, il n’institue aucun groupement en particulier. Les conseils départementaux de l’accès au droit sont des groupements d’intérêt public et ils ont pourtant un siège, parce qu’un article de loi les institue par leur nom.

---

## 3. Règle de lecture des colonnes

| colonne | ce qu’elle porte |
|---|---|
| `cle` | **le libellé exact que porte la liste du III**, clé d’entrée du référentiel comprise. C’est la clé de jointure et elle ne se normalise jamais. L’appariement avec la pièce est mécanique, rang par rang. |
| `denomination` | la même chaîne. Les deux colonnes ne divergeront que le jour où une dénomination légale sera substituée à la clé d’entrée, ce qui n’est pas fait. |
| `famille` | le nom de la famille à siège commun. **Vide quand l’entité est seule.** |
| `nature` | le type de personne morale, tel que l’article lu le qualifie. |
| `texte` | le code ou la loi. **Vide quand le siège n’est pas trouvé.** |
| `articles` | l’article ou la plage d’articles. |
| `identifiant` | l’identifiant Légifrance de la version lue. |
| `millesime` | la date de la version lue, soit le millésime de l’extrait LEGI du dépôt. |
| `confiance` | `haute` quand l’article a été lu au verbatim, `moyenne` quand le siège vient d’une source secondaire fiable. **Aucune autre valeur n’est admise. Une ligne sans siège n’en porte aucune.** |
| `source` | où il a été lu. |

**Les trois lignes en confiance moyenne, leur motif.** **France Travail** : siège repris de `vecteurs.py`, relevé Légifrance du 20260831, non rejoué à la base. **Société des grands projets** : l’article 7 de la loi n° 2010-597 du 3 juin 2010 n’est pas au dépôt. C’est l’article 1609 G du code général des impôts qui le nomme comme article de création. **AGS** : l’article L. 3253-14 du code du travail institue l’association sans la nommer.

**Un point à vérifier avant dépôt.** L’article L. 6123-5 du code du travail, siège de France Compétences, est en état `ABROGE_DIFF` au millésime 20261007 : sa version cesse de s’appliquer à une date déjà votée. Le rang 36° se recontrôle sur la version suivante.

---

## 4. Comment un fil ultérieur reprend ce travail pour le finir

**Quatre pas, dans cet ordre.**

1. **Ouvrir le référentiel et filtrer les lignes dont la colonne `texte` est vide.** Elles sont 160. Elles sont le mandat du fil suivant.
2. **Commencer par les trois groupes les plus rentables** : les 30 groupements de formation continue, les 18 centres d’information jeunesse, les 17 sociétés de France Télévisions. **Chacun se tranche en une fois** : soit un texte commun existe et les trois blocs tombent ensemble, soit aucun n’existe et le groupe entier reste sans siège, ce qui est aussi un résultat.
3. **Aller chercher hors du dépôt les trois textes qui lui manquent** : le code forestier pour le Centre national de la propriété forestière, le code de la sécurité intérieure pour le Conseil national des activités privées de sécurité, la loi n° 86-1067 du 30 septembre 1986 pour les sociétés de l’audiovisuel public. **Verser ces textes au dépôt de droit vaut mieux que les lire en ligne une fois** : le relevé se rejouera.
4. **Écrire les lignes nouvelles au même fichier, jamais à un fichier nouveau**, puis régénérer la liste du III depuis le référentiel. **La pièce ne s’édite pas à la main** : chaque rang pourvu prend la forme `N° dénomination, régie par l’article X du code Y.` et la reprise par « du même code » ou « de la même loi » se recalcule, un groupe interrompu par un rang sans siège renommant son texte en entier.

**Trois règles tiennent ce travail. Aucune ne souffre d’exception.** **Une adresse qui n’a pas été lue ne s’écrit pas.** **Une entité dont le siège n’est pas trouvé reste sans siège et figure à la liste des manquants.** **Le nombre de rangs du III ne change jamais** : il est de 343 avant comme après. Un rang pourvu d’un siège reste le même rang.

---

**Appui** : `livrables/depot_2027/P2/2_1_dissolution_structures_facultatives.md`, cartouche du 20261013 · `livrables/depot_2027/clause_generale_niches_20261005.md`, forme des rangs énumérés · `chantier/appareil/vecteurs.py`, règle du vecteur et des provenances · base LEGI du dépôt `resolution-ib-dev/Resolution-2027`, millésime **20261007**.
