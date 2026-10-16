# Registre du 16 octobre 2026 — les sièges du tri des prélèvements

**Porteur** : fil Cowork « sièges des prélèvements », 20261016.
**Pièce travaillée** : `referentiels/sort_prelevements_20261015.tsv`, 420 lignes.
**Contrôle qui prouve** : `appareil/controle_sieges_prelevements.py`.

Entrées titrées et datées, sans numéro. Le fil de réconciliation numérote.

---

## Le défaut des 105 sièges non établis est clos — il en reste 17

**20261016.** Le tri portait 105 lignes à `statut_siege = non établi`, recomptées
sur le fichier à l'ouverture du fil. Il en reste **17**. Les 88 autres se
répartissent ainsi, et chaque groupe porte son propre statut :

| statut inscrit | lignes | ce qu'il dit |
|---|---:|---|
| relevé à l'annexe des ressources affectées PLF 2027 | 51 | la colonne `reference_juridique` de l'annexe, réappariée au contrôle |
| relevé au dépôt de droit, vérifié article par article | 26 | l'article a été rouvert et son texte lu |
| relevé par renvoi exprès, vérifié | 1 | un article du dépôt nomme le texte hors dépôt |
| siège abrogé, relevé au dépôt de droit | 1 | la garantie des matières d'or |
| sans siège par construction — agrégat de ligne d'état A | 3 | — |
| hors droit national — ressource propre de l'Union | 1 | droits d'importation |
| siège réglementaire — hors du champ du relevé législatif | 2 | — |
| création du PLF — aucun article en vigueur au millésime | 3 | — |

Les deux autres défauts du tri tiennent — 188 rangs sans rendement, 420 rangs
contre 438 au manifeste — et **le classeur ne se publie pas**.

## Un libellé de ressource porte plusieurs références à l'annexe

**20261016.** L'annexe des ressources affectées compte 293 lignes pour 215
libellés distincts : un même libellé y revient avec des références juridiques
différentes. Elles s'inscrivent **toutes**, jointes par « ; », et un contrôle qui
compare la chaîne entière à une référence unique fait quatre faux — c'est arrivé
au premier jeu du contrôle, le jour même. **La comparaison se fait sur l'ensemble
des références, jamais sur la chaîne.**

## Un chapitre entier du code général des impôts peut être éteint sous une recette vivante

**20261016.** La ligne « Garantie des matières d'or et d'argent » figure au tri
sans siège. Ce n'est pas un trou : le chapitre II du titre III de la première
partie du livre premier du code général des impôts est éteint. **23 de ses 25
articles sont `ABROGE` avec effet au 1er juillet 2025** ; seuls les articles 522
et 524, titres légaux et poinçons, restent applicables en abrogation différée.
Aucun article de perception ne s'applique. Un siège éteint se relève et
s'inscrit ; il ne se laisse pas en blanc.

## Un agrégat de ligne d'état A n'a pas de siège, et le chercher est une faute de catégorie

**20261016.** Quatre lignes du tri ne sont pas des impositions : trois agrégats
de l'état A — « Autres impôts directs perçus par voie d'émission de rôles »,
« Autres taxes », « Autres droits et recettes accessoires » — et les droits
d'importation, ressource propre de l'Union. Une colonne **`nature_ligne`** les
distingue désormais, aux valeurs `imposition`, `agrégat` et
`ressource propre de l'Union`. Le fil a cherché un siège aux quatre avant de
poser la distinction ; c'est du temps perdu deux fois.

## L'évaluation des voies et moyens, tome I, ne porte aucune base juridique

**20261016, relevé sur pièce.** Les notices de ligne du tome I se limitent à
trois volets — retour sur l'exécution, révision, évaluation. Aucune rubrique de
textes de référence. **Le tome I ne sert pas à relever un siège** ; seule son
annexe 2, les taxes affectées, porte une colonne juridique. Le fil a ouvert le
document pour l'établir, et cette borne s'écrit ici pour qu'aucun fil ne le
rouvre dans ce but.

## Les statuts des établissements rendent les sièges que les référentiels n'ont pas

**20261016.** Là où le libellé ne s'apparie nulle part, l'article qui énumère les
ressources de l'organisme bénéficiaire le donne. C'est par là que sont venus la
contribution de la Caisse des dépôts, à l'article L. 518-16 du code monétaire et
financier, et les trois contributions des employeurs de main-d'œuvre étrangère, à
l'article L. 436-10 du code de l'entrée et du séjour des étrangers.

## L'extrait du code général des impôts n'est pas le code

**20261016, mesuré.** `depot/data/cgi.jsonl.gz` porte **2 584 articles
distincts**, dont 2 408 applicables, sur deux livres seulement. Vingt-neuf plages
de huit numéros ou plus y manquent, dont **901 à 952**, qui est la matière des
droits de timbre. **« Absent de l'extrait » ne vaut donc pas abrogation**, et
quatre lignes du tri restent non établies pour cette seule raison — timbre
unique, timbre de dimension, actes judiciaires et extrajudiciaires, taxe sur les
émoluments. Le défaut est au dépôt, non au classeur.

## Un grep sur un mot n'est pas une mesure, et un outil de chasse doit le dire

**20261016.** Le fil a ouvert sa matière par des recherches plein texte, ce que
le septième garde-fou proscrit. L'outil qui en sort, `appareil/chasse_siege.py`,
**ne rend que des candidats** et le dit à chaque sortie : un siège ne s'inscrit
qu'après réouverture de l'article par `droit.article` et lecture de son texte.
Deux règles mécaniques en sont tirées : l'applicabilité se lit à
`droit.applicable` et **jamais à l'état** — un article `ABROGE_DIFF` s'applique
aujourd'hui ; et le classement des candidats se fait **par longueur de texte
croissante**, un article d'institution étant court quand un état A fait deux cent
mille signes. Le tri par mots d'institution a été essayé et il remonte du bruit.

## L'écart « 420 rangs contre 438 au manifeste » est une borne recopiée, et il était expliqué depuis le 20260902

**20261016.** Le défaut est inscrit à `CLAUDE.md` et à la passation du 15 octobre
comme « écart non expliqué ». Il l'était. Le § 5 de
`reference/nomenclature_prelevements_ifrap.md`, daté du **20260902**, le relève
déjà : la pièce de la Fondation IFRAP **annonce 438 prélèvements** à ses pages 3
et 5, et **ses tables en publient 421** — 302 taxes et impôts pour 303 annoncés,
73 cotisations pour 89, 46 contributions pour 46. **L'écart de 16 porte sur les
cotisations**, il n'est pas un artefact d'extraction, et il n'est pas résolu dans
la source. La consigne de diffusion y figure aussi : citer 438 en renvoyant à la
pièce, 421 en renvoyant au référentiel, jamais l'un pour l'autre.

C'est le sixième garde-fou en situation : **une borne écrite à un document de
méthode s'est recopiée sans être vérifiée à la pièce**, et elle a traversé deux
documents en qualifiant d'inexpliqué ce qui était documenté depuis six semaines.

## Le 420 du tri n'est pas le 421 de la liste IFRAP moins un doublon

**20261016, mesuré.** `referentiels/prelevements_ifrap.tsv` porte 421 lignes pour
**420 libellés distincts** : les lignes 162 et 168, page 14, reprennent le même
prélèvement, la seconde avec un point final. Ce doublon est dans la source et
l'extraction l'a fidèlement rendu ; il est **distinct** du doublon de pages 17 et
18 que la digestion signale déjà.

**L'égalité 420 = 421 − 1 est fortuite.** Le rapprochement ligne à ligne, joué
sur la colonne `libelle_ifrap` de `referentiels/prelevements_forces_20260930.tsv`,
ne ferme pas :

| rapprochement | compte |
|---|---:|
| libellés IFRAP appariés à un rang du tri | 355 |
| lignes de la liste IFRAP sans rang correspondant | 65 |
| rangs du tri sans `libelle_ifrap` renseigné | 14 |
| `libelle_ifrap` déclarés au tri et introuvables dans la liste | 24 |

**Le défaut se reformule, il ne se clôt pas.** Ce qui reste à faire n'est pas
d'expliquer un écart de 18 contre un titre de publication — cet écart appartient
à la source — mais de **fermer le rapprochement des 420 rangs sur les 420
libellés**, ce qui demande quatre-vingt-dix-neuf décisions d'appariement. Tant
qu'elles ne sont pas prises, le tri n'est pas adossé à sa liste, et c'est cela
qui bloque, non le 438.

## Le rapprochement IFRAP est fermé, et le compte de 99 appariements était faux

**20261016.** La colonne `libelle_ifrap` de
`referentiels/prelevements_forces_20260930.tsv` **porte des cellules à plusieurs
valeurs, jointes par « ; »** : un rang du tri absorbe plusieurs lignes de la
liste — le versement mobilité et ses deux additionnels, les redevances de l'eau,
les taxes spéciales d'équipement, les taxes d'immatriculation. Vingt-trois
cellules sont dans ce cas.

Une jointure qui n'éclate pas la cellule rend **65 lignes orphelines et 24
déclarations introuvables, toutes fausses**. C'est l'état dans lequel le fil a
d'abord annoncé « 99 décisions d'appariement à prendre ». **Après éclatement :
420 libellés de la liste sur 420 couverts, 0 orpheline**, et 14 rangs qui ne
viennent pas de la liste mais portent leur provenance en colonne `origine` —
cinq de l'état A, neuf de l'annexe des ressources affectées.

Une seule correction a été nécessaire : le libellé IFRAP de la **TIRUERT** était
déclaré sans son suffixe « (remplace la TGAP carburants fossiles) ». Aligné.

**Le rapprochement est désormais contrôlé** par la règle R de
`appareil/controle_sieges_prelevements.py`, qui éclate la cellule, exige la
couverture des 420 libellés et compte à part les rangs d'une autre origine.

## Les 188 rangs sans rendement ne se comblent pas au dépôt — mesuré source par source

**20261016.** Les trois sources de rendement que le dépôt porte ont été
éprouvées, chacune sur la totalité des rangs vides :

| source | ce qu'elle rend |
|---|---|
| annexe des ressources affectées PLF 2027 | **2 rangs** remplis, 5 appariés sans montant |
| état A du texte déposé, 163 lignes extraites pour 474,2 Md€ | **0 rang** — aucun libellé n'y tombe |
| liste IFRAP | **0** — ses trois colonnes sont `categorie`, `libelle`, `page`, elle ne porte aucun montant |

Les deux rangs remplis sont l'impôt sur les spectacles, jeux et divertissements,
334,0 M€, et la taxe annuelle sur les locaux à usage de bureaux, 21,9 M€. **Le
compte tombe de 188 à 186**, et il s'arrête là.

**Le défaut est caractérisé, non levé.** Les 186 restants sont, pour 179 d'entre
eux, des lignes que seule la liste IFRAP porte : des prélèvements trop petits
pour être ligne d'état A et non affectés sous plafond, donc absents de l'annexe.
**Les combler demande une source extérieure au dépôt** — ce n'est pas un travail
de relevé, c'est une acquisition de données, et elle appelle un arbitrage sur la
source à retenir.

*Relevé de passage, non versé* : l'état A du texte déposé s'extrait proprement du
socle — 163 lignes, intitulé et évaluation 2027, total 474,2 Md€. Aucun mandat ne
nomme cette table ; elle n'est donc pas écrite.
