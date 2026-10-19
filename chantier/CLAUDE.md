# Projet Résolution — instructions permanentes

Réforme constitutionnelle, budgétaire et fiscale française. Le projet porte le
manuscrit, les grilles qui en dérivent, l'appareil qui les traite et les
livrables diffusables.

---

## Le partage du travail

**L'auteur valide les inputs et les outputs.** Il répond à des questions
précises, pas à pas, sur les objectifs et les subtilités. On structure ensemble
les process de production compliqués.

**Claude se débrouille seul pour sa tambouille** — méthode de détail, appareil,
index, générateurs, nommage, découpage des fils, ordre d'exécution. Il tranche
et il inscrit au registre, l'auteur révoque s'il y a lieu.

**Quand l'auteur énonce une nouvelle règle, Claude consulte ce que de droit et
met à jour ce que de droit**, le jour même, sans qu'on ait à le demander.

**Claude maintient son architecture interne en dynamique**, pour ne pas
surspécifier ni surimposer. Le coût d'une décision d'organisation ne se reporte
pas sur l'auteur.

Quatre garde-fous, tirés de ce qui a déjà coûté des reprises : ne jamais classer
ni qualifier un document non ouvert, et dire quand il ne l'a pas été ; ne porter
au registre en « validé » que ce que l'auteur a dit ; aucun superlatif non
vérifié ; annoncer le coût d'une opération avant, jamais après.

**Un cinquième, et c'est le seul qui ne se mécanise pas** (A-299). À chaque
phrase versée qui décrit une pièce, un chiffre ou l'état du corpus : dire d'où
elle vient — **relevée, héritée, ou déduite**. Une phrase héritée d'un autre fil
et non rejouée se marque comme telle ; elle ne se verse pas au même rang qu'un
relevé. Trois règles en découlent, et elles ont chacune coûté :

- **un repère qui ne mord pas ne prouve rien sur la pièce** — il prouve que le
  repère ne mord pas ;
- **aucun chiffre ne s'écrit sans être recompté sur le fichier au moment de
  l'écrire** — le récit d'une passation n'est pas une source ;
- **avant de déclarer une pièce manquante**, lire les pièces jointes du projet et
  éprouver le dépôt de droit pour un texte de loi.

**Un sixième, inscrit le 20261001** : **une borne écrite à un document de méthode
ne se recopie pas — elle se vérifie à `methode/arbitrages.md` et au registre avant
d'être redite.** Un document de méthode est une pièce datée ; le registre, non.
Une borne fausse depuis un mois — « la grille des portes des lois de financement
n'est pas relevée », close par A-336 le 20260902 — a traversé quatre documents et
trois fils, dont un mandat qui demandait de relever une grille déjà relevée.

**Un septième, inscrit le 20261015, et c'est celui qui a coûté le plus en un
jour** : **avant de produire sur une matière, ouvrir la division qui la nomme,
jamais chercher le mot.** Neuf fautes en une séance, toutes la même : la pièce
qui faisait foi était à portée et n'a pas été ouverte. Un classeur bâti sur un
référentiel qui ne fait pas foi ; un vocabulaire contraire à la doctrine de
l'auteure, dont l'onglet était au projet ; un `grep` sur le mot « lisser » quand
la règle s'appelle **CP résiduel** et vit à la deuxième ligne de la première
division du registre ; une ventilation recalculée quand le registre la portait
déjà. **Un `grep` sur un mot n'est pas une mesure.** Une matière se mesure en
ouvrant sa division.

**La table de ce qui fait foi, par matière.** Elle se lit avant de produire, et
elle prime sur toute mémoire de fil.

| matière | pièce | division |
|---|---|---|
| la chaîne de calcul, et **la règle de CP** | `livrables/registre_calcul_etatB.md` | § 1, et § 3 pour les huit régimes de résiduel |
| **les crédits ouverts de 2027, par programme** | `referentiels/etatB_2027_bg.tsv` | — |
| **les ratios CP/AE par catégorie** | `referentiels/ratios_cp_ae_pap2026.tsv` | — |
| **le socle de crédits et le relevé de l'égalité AE = CP** | `livrables/registre_calcul_etatB.md` | § 3 bis |
| la restitution, mois par mois | même pièce | § 2 |
| les montants d'exercice, ligne par ligne | même pièce | § 4 |
| la trajectoire 2027-2030 | même pièce | § 5 |
| le flux mensuel par agent | même pièce | § 6 |
| la contemporanéité | même pièce | § 7 |
| mesure contre caisse | même pièce | § 15 |
| le trimestriel par pan | même pièce | § 16 |
| TVA et taxe sur les salaires | même pièce | § 17 |
| le sort des prélèvements | `referentiels/prelevements_forces_20260930.tsv`, colonne `rang` | — |
| le vocabulaire des sorts, et quelle ligne est maintenue | onglet `Refonte fiscalité` de `Synthèse Calculs Résolution` | — |
| les commissions du Jaune | `referentiels/commissions_jaune2026_20261014.tsv` | — |
| **toute matière de recettes, de dépenses fiscales ou de taxes affectées en 2027** | `methode/annexes_voies_et_moyens_2027.md` | la table « où va se servir un fil » |
| la vue d'ensemble, non la source | `livrables/suivi_trajectoire_20261015.md` | § 9 et § 10 |

**Les sept annexes des voies et moyens du PLF 2027 sont au dépôt**, en dix
tables, digérées et éprouvées à l'octet le 20261019. **Aucune ne se demande à
l'auteur, aucune ne se retélécharge, et il n'y a pas d'annexe 3 au tome I.**
`methode/annexes_voies_et_moyens_2027.md` dit laquelle porte quoi et renvoie à la
table qui répond à chaque question ; `appareil/digerer_annexes_vm2027.py verifier`
les rejoue sur les classeurs. **Avant de proposer la suppression d'une dépense
fiscale, ouvrir `annexe_evolution_df_bilan_2027.tsv` et
`annexe_evolution_df_bornees_2027.tsv`** : une dépense déjà supprimée ou déjà
éteinte ne se supprime pas deux fois, et l'économie qu'on lui prêterait est acquise
au tendanciel.

**Trois conséquences, chacune a coûté.**

- **Mesure et caisse ne se confondent jamais.** Un solde de trajectoire est **en
  mesure** : il ignore le CP résiduel, qui ne vit qu'au § 15 et sur la seule part
  État de 2027. Tout chiffre de solde se dit avec sa couche, sans exception.
- **Un référentiel qui porte ses défauts ne se publie pas**, même mis en forme.
  Le tri des prélèvements n'en porte plus qu'un : **186 rangs sans rendement
  2026**. **Le point est clos depuis le 20261019 et ne se rouvre pas sans une
  source nouvelle.** Sept sources ont été éprouvées sur la totalité des rangs
  vides — l'annexe des ressources affectées en remplit 2, et les six autres
  aucune, dont toutes les annexes des voies et moyens du PLF 2027. La raison est
  une disjonction de périmètre, non un défaut de jointure : les 186 rangs sont
  93 cotisations sociales et 92 taxes affectées à des tiers, quand les voies et
  moyens portent le budget général et les taxes plafonnées. Le relevé des sept
  mesures est à `methode/annexes_voies_et_moyens_2027.md`. **Un fil qui rouvrirait
  ce point referait sept mesures déjà faites** : les rangs restent déclarés sans
  rendement, et le référentiel garde son défaut déclaré.

  *Deux défauts sont clos le 20261016.* **Le rapprochement sur la liste IFRAP** :
  420 libellés sur 420 couverts, 0 orpheline, 14 rangs d'une autre origine
  déclarée. Il était écrit « 420 rangs contre 438 au manifeste, écart non
  expliqué » — formule fausse : **le 438 est le chiffre annoncé par la pièce
  IFRAP, dont les tables ne publient que 421**, écart de 16 sur les cotisations,
  relevé au § 5 de `reference/nomenclature_prelevements_ifrap.md` dès le
  20260902, interne à la source. En diffusion, citer 438 pour la pièce et 421
  pour le référentiel, jamais l'un pour l'autre. **La colonne `libelle_ifrap`
  porte des cellules à plusieurs valeurs jointes par « ; »** : une jointure qui
  ne les éclate pas fabrique 89 faux écarts. **Le second est le relevé des
  sièges** : les 105 sièges non établis sont tombés à **14** le 20261016, puis à
  **5** le 20261019. La répartition se lit à l'entrée « Le défaut des sièges non
  établis passe de 105 à 5 » du registre, recomptée sur le tri ; elle ne se
  recopie pas d'ici. **Un rang se qualifie en trois états** à la colonne
  `nature_ligne` — imposition, agrégat de ligne d'état A, ressource propre de
  l'Union — et **un siège ne s'exige que d'une imposition** (arbitrage de l'auteur
  du 20261019). **Le contrôle qui le prouve est
  `appareil/controle_sieges_prelevements.py`** ; il rejoue chaque siège sur sa
  pièce, exige un siège de tout rang d'imposition par sa règle S6, et refuse le
  versement sur un seul échec. **Il en sort cinq** : les cinq rangs restés non
  établis sont mesurés vides au dépôt comme aux annexes, et leur qualification
  n'est pas tranchée. Les deux défauts restants tiennent, et le classeur ne se
  publie pas.
- **Le CP se lit avant de se calculer** (inscrit le 20261016). Les crédits ouverts se lisent à
  l'état B du texte déposé avant toute minoration : comparer à un exercice antérieur a fabriqué un
  risque bloquant qui n'existait pas. Hors titre 2, **AE ≥ CP**, et l'égalité ne se pose pas, elle
  se **relève** sur la catégorie visée, qui se déclare au bloc `[interne]` de la pièce. Le contrôle
  est `appareil/controle_credits_liasse.py`.
- **Une pièce produite et non versée n'existe pas.** Le croisé mesure × agent ×
  mois a été fabriqué dans un fil, jamais versé, et il est perdu. Ce qui sort
  d'un fil passe au projet ou au dépôt le jour même.

Quand l'auteur relève une erreur, elle se traite **avant** toute autre chose.
Produire du neuf ne répare rien, cela recouvre.

---

## Les fils — ce qu'ils rendent, et lequel est seul

Trois règles, arrêtées par l'auteur le 20260902 (A-282). Elles disent comment
plusieurs fils travaillent sur le même corpus sans se marcher dessus.

**Un fil de production rend ses entrées de registre titrées et datées, sans
numéro.** C'est le fil de réconciliation qui numérote à l'insertion. Un fil ne
peut pas lire l'état du registre au moment où un autre écrira : numéroter
soi-même, c'est deviner, et deux fils l'ont déjà fait faux.

**Un fil qui touche `methode/` ou un module d'`appareil/` partagé est seul.** Les
fils qui produisent leurs propres fichiers sont parallélisables. Un seul fil joue
`make coffre`.

**Une branche meurt avec sa fusion** (inscrit le 20261016). Tout mandat de
versement se termine par la suppression de la branche distante, dans le même fil et
après la fusion. Un fil qui ne la supprime pas la laisse pour toujours : aucun autre
ne sait si elle porte encore quelque chose, et il faut rouvrir son diff pour le
savoir. **Trente-cinq branches** s'étaient accumulées au 16 octobre, dont trente
entièrement fusionnées et trois mortes de péremption. C'est au fil qui écrit le
mandat de le prévoir, jamais à l'auteur de le réclamer.

**Mais un fil claude.ai/code ne peut pas supprimer une branche distante** : le proxy
répond `403` à tout coup, éprouvé cinq fois le 20261016. La règle se tient donc d'un
réglage du dépôt, non d'un mandat : **« Automatically delete head branches »**, activé
une fois dans les réglages de `Resolution-2027`, supprime la branche à chaque fusion
et pour toujours. Les branches déjà accumulées se suppriment à la main dans
l'interface GitHub, une seule fois.

**Le mandat dit seulement** : « rendre la liste des branches distantes restantes avec,
pour chacune, sa date et son état — fusionnée, en avance de n commits, ou périmée. »
Un fil qui compte des branches les compte sur le distant, jamais sur une liste
héritée : deux erreurs de décompte en sont sorties le 20261016, une branche fantôme
et un doublon.

**Tout sas s'inscrit d'une ligne à `methode/sas.md` en fin de fil.** Un **sas**
est un document du coffre qui porte ce qu'un fil a fabriqué et que le corpus n'a
pas encore absorbé — modules d'appareil, entrées de registre, règles de
`Makefile`. Il existe parce qu'un fil de production ne touche pas `methode/`, et
**il se supprime** dès qu'il est absorbé. Un fil de réconciliation lit
`methode/sas.md` au lieu d'inspecter le projet.

*Conséquence tenue* : un sas laisse mécaniquement une empreinte en retard, parce
que le fil qui l'ouvre ne joue pas `make coffre`. Le `R1` qui en sort n'est pas un
faux, et sa preuve est une seconde lecture indépendante du coffre (A-121, A-290).

---

## Ouverture de session — on lit avant de déplier

**Trois documents d'abord, rien d'autre** : `methode/index.json`,
`methode/prompt_fil_courant.md`, `methode/arbitrages.md`. Le fil courant dit ce
dont il a besoin. **On ne déplie que cela.**

Puis, si et seulement si le fil déplie, dans cet ordre :

1. `appareil/restaurer.py amorce .` — l'index, qui est la table de tout le reste.
2. **le clone du dépôt**, qui rend l'appareil par copie d'octets :
   `git clone https://github.com/resolution-ib-dev/Resolution-2027 droit`
   puis `cp -r droit/chantier/. .`
3. `appareil/restaurer.py` pour les documents du coffre.
4. `make restauration`. **On s'arrête sur un R1.**

**Il n'y a plus d'archive technique au coffre** : elle est au dépôt sous
`chantier/` depuis le 20260909, prouvée 80 sur 80 à l'octet (A-395).
`coffre.py deplier` ne sert plus qu'à relire une archive au vieux format si une
session en récupère une ; `coffre.py plier` est retiré.

**Pour un fil de réconciliation, un quatrième** : `methode/sas.md`, la liste des
sas ouverts. Elle se lit au lieu d'inspecter le projet.

Ensuite, à mesure du besoin : `livrables/carte_du_projet.html` la carte,
`methode/classement_corpus.md` les règles de rangement, `methode/journal.md` le
récit, `methode/localisation.md`.

**Rien ne se génère à l'ouverture**, y compris un dérivé ou un référentiel absent
du dépôt. Son absence se constate ; il se refait quand le fil en a besoin.

## La restauration — toujours une copie d'octets

**Une restauration ne se délègue jamais au jugement d'un modèle**, ni auxiliaire
ni principal. Elle a exactement trois voies, et aucune quatrième :

1. **`cp`** du fichier local, quand le coffre rend le document comme fichier.
   **Plus aucune pièce du corpus n'est dans ce cas depuis le 20260910** : les
   deux référentiels de rédaction, 848 ko et 352 ko, sont au dépôt. La voie
   reste écrite pour le jour où un document franchira le seuil.
2. **`git clone` du dépôt**, puis `cp -r droit/chantier/. .`, pour les
   **quatre-vingt-quatre** artefacts de voie `depot` — tout `appareil/`, les
   cinq référentiels JSON, le `Makefile`, le `.gitignore`. Un clone est une
   copie d'octets par construction.
3. **`appareil/restaurer.py`** pour les documents du coffre. Le texte que le coffre rend est
   écrit verbatim au transcript de session, sur le disque de l'atelier : il s'en
   extrait par script. Un document que la session n'a pas encore lu se récupère
   en le faisant lire par un fil auxiliaire qui sert de **tuyau** — il lit, il
   n'écrit rien, le transcript garde les octets.

`restaurer.py` **n'écrase jamais un fichier présent** : le transcript porte l'état
d'avant, et réécrire dessus détruirait le travail de la session. Deux versions
divergentes d'un même document l'arrêtent — c'est au coffre de trancher.

**`methode/empreintes.json`** porte le SHA-256, la taille et le compte de lignes
de chaque artefact durable, **sur les deux voies**. Relevé à `make coffre`,
comparé à `make restauration`. Le relevé est cumulatif : un fil partiel n'efface
pas les empreintes de ce qu'il n'a pas déplié. **On s'arrête sur un R1.**

**Une empreinte ne décrit jamais un état qu'aucune surface permanente ne
porte.** Pour la voie `depot`, elle se relève donc **au clone**, qui est ce que
la session suivante recevra, et jamais au dépôt courant : un fil Cowork ne peut
pas pousser (A-393), et relever ici l'empreinte d'une pièce corrigée écrirait au
coffre la référence d'un fichier qui ne vit que dans un conteneur éphémère. Le
clone se passe donc à `make coffre` **et** à `make restauration`.

**Un R1 ne se lit pas de la même façon selon la voie**, et le contrôle le dit.
Sur la voie `coffre`, le fichier restauré est un faux : il se redemande au
coffre. Sur la voie `depot`, l'octet vient d'un clone :

- il diverge de l'empreinte **et du clone** → corrigé ici et non poussé. **`R6`,
  qui ne bloque pas** : `appareil/coffre.py dette` le réclame, un fil
  claude.ai/code le pousse. Sans quoi tout fil qui corrige l'appareil échouerait
  à sa propre clôture.
- il diverge de l'empreinte **et concorde avec le clone** → le dépôt est en
  retard, ou l'empreinte a été relevée ailleurs. **`R1`**, et c'est le cas qui
  compte.
- **sans clone, tout reste en `R1`.** Le comportement prudent est celui qui
  bloque.

**Une pièce restaurée se prouve, quand elle porte du verbatim.** L'empreinte dit
qu'elle est intacte ; un dérivé rejoué dessus le confirme de l'extérieur. Le
manuscrit se contrôle ainsi : `extraire_notes.py` doit redonner
`referentiels/notes_manuscrit.json` identique à l'octet.

**Un contrôle qui ne s'exerce que sur le dépôt courant ne prouve rien.** Les
empreintes peuvent avoir été relevées sur des faux — c'est arrivé. Avant de verser
une réparation, restaurer à blanc dans un dépôt vierge et comparer aux
empreintes : ce test compare le coffre à lui-même, sans passer par ce que la
session croit savoir.

`R5` distingue un dérivé divergent d'un faux. Un dérivé horodate parfois son pied
de page ; il se régénère, il ne se redemande pas.

---

## Hiérarchie des strates

**Le manuscrit est la vérité.** `manuscrit/manuscrit.html`, corps **et notes de
fin**. Il ne se révise jamais depuis l'aval. La présomption d'erreur porte sur
le calcul, jamais sur lui. **Ses annexes ont le même rang** : les huit classeurs
font vérité pour ce qu'ils décomptent.

**Les extensions complètent la doctrine.** Textes gelés et validés — la
Constitution à trois colonnes, la note de réforme budgétaire, les précédents
restes à payer. Le trois colonnes porte texte actuel, réforme visée, rédaction
révisée : le projeté est en troisième colonne. Sa première colonne n'est pas
toujours un verbatim, et **le texte en vigueur se cite au texte nu de
référence**. La Constitution à trois colonnes est la strate maître de la
révision : une mise à jour ciblée s'y fait, puis on rejoue les outputs qui en
dérivent.

**Les grilles sont des outils.** `REF_doctrine`, `REF_chiffres`, les champs
rédigés, le recensement des innovations. Elles se corrigent dès qu'elles
s'écartent du manuscrit. Elles se lisent, elles ne se recopient pas.

**Les dérivés se régénèrent.** Aucun ne se corrige à la main. Une faute dans un
livrable se corrige à sa source, puis `make`.

**Toute recherche au manuscrit balaie le corps et les notes.** L'omission de ce
balayage a laissé passer deux chiffres majeurs.

---

## Le classement par contenu

Trois surfamilles, neuf familles. `input` — doctrine, extensions, références
externes, références internes. `travail` — grilles, bac à sable, méthode,
outillage. `output` — juridique, rédactionnel, graphique.

**Le classement est une vue, pas une arborescence.** Les adresses techniques des
fichiers ne suivent pas. L'affectation vit dans `appareil/generer_carte.py`, la
carte la rend, l'index en porte le champ `famille`. **Un document ne se déplace,
ne se réécrit et ne se reformate que si sa recopie ne risque pas de le
déformer.** La carte donne famille et adresse.

Deux règles qui reviennent tout le temps :

- **Une matière de fond et le document qu'on en tire sont deux artefacts.** Le
  trois colonnes est de l'input, les PPLC qui en sortent sont de l'output.
- **Ce qui n'est pas validé n'est pas de l'input.** Un travail de Claude reste au
  bac à sable tant qu'il n'a pas été relu.

Le détail est dans `methode/classement_corpus.md`.

---

## Arborescence technique

```
manuscrit/      strate 1, jamais modifiée depuis l'aval
referentiels/   REF_doctrine, positions, notes — les valeurs
appareil/       générateurs et contrôles — le traitement
livrables/      extrait, carte, vues internes — les sorties
methode/        règles, index, journal, registre, procédures
reference/      textes normatifs et digestions
archive/        documents datés, gelés ou brouillons
```

Ces dossiers sont des adresses, pas un classement. La correspondance avec les
familles se lit à la carte, et la résolution des renvois à `methode/index.json`.

---

## La chaîne

```
make               régénère ce qui a changé
make index         concordance arborescence, index et noms canoniques
make restauration  compare chaque pièce restaurée à son empreinte
make controle      joue les contrôles, ne produit rien
make coffre        relève les empreintes et dit ce qui est dû au dépôt
make etat          où en est la rédaction des apports
make publier       désactivé : le site se maintient dans Site-ETNP/site/
```

Le référentiel des positions se construit depuis `construire_positions.py` pour
la structure, `justifications.py` pour les pertes, `apports.py` pour les gains.
La projection se fait une fois par `exporter_donnees.py` : l'extrait et
l'interface lisent le même fichier et ne peuvent pas diverger.

**La galerie des fiches a sa propre chaîne.** `structure_fiches.py` porte le
document arbitré par l'auteur — qui porte quel gain, quelle perte, dans quel
ordre. `carte_attribution.py` le rend lisible pour l'arbitrage,
`generer_fiches.py` l'exécute et écrit `livrables/galerie_fiches.html`. **Une
seule source** : la structure décide, les deux autres suivent. Rien ne s'écrit à
la main dans la galerie.

**Le site descend de la galerie, et il ne la redessine pas.**
`generer_site.py` importe `matiere()` et `fiche()` de `generer_fiches.py`, et
écrit `site/` — un index qui liste les dix-huit fiches avec leur axe, une page
par fiche à son adresse, une feuille de style, une page d'erreur. Vingt et un
fichiers, régénérés en bloc ; un seul se déclare à l'index, `site/index.html`,
et il vaut pour le dossier.

L'adresse d'une fiche se dérive de son titre arbitré : renommer une fiche change
son adresse, et une adresse déjà partagée casse. Le générateur refuse en échec
deux fiches qui partageraient une adresse.

**Le site ne porte que ce qui existe** : ni manifeste, ni note, ni vidéo. Son
entrée ne porte aucun chiffre — hiérarchiser les montants est un arbitrage
d'édition (A-179), et les dix-huit axes sont la promesse.

**Le socle du texte déposé : un extracteur, deux profils de pièce** (A-273).
`socle_plf_texte.py` porte les profils `plf` et `plfss` ; le profil se passe en
troisième argument, et sans lui les repères du PLF s'appliquent, ne se retrouvent
pas sur la pièce du PLFSS et la génération s'arrête — c'est voulu. Un second
extracteur ferait deux grammaires d'adresse, donc deux points de vérité.
`articles_ouverts_plf.py` en dérive les adresses ouvertes, et
`controle_socle_plf.py` les prouve en rouvrant la pièce.

**Les portes ouvertes** — `portes_ouvertes.py` joint `REF_norme` aux deux tables
d'articles ouverts et dit quelle mesure du corpus tombe sur un article que le
texte déposé ouvre déjà : un amendement porté là se raccroche à un article
existant du véhicule. **La jointure se fait sur l'article complet** : la colonne
`article_selon_ref_norme` des tables tronque les suffixes de rang, et joindre
dessus fait 77 faux (A-293). Une fourchette est comptée sur sa borne basse et
signalée ; elle ne se déplie pas.

**Le domaine du PLFSS n'est pas à `LO 111-3`** (A-297). Cet article ne définit
plus que les trois espèces de lois de financement depuis la loi organique
n° 2022-354. La porte d'un amendement est aux **`LO 111-3-6` à `-3-8`**, les
monopoles aux `-3-14` à `-3-16`.

**La grille est relevée depuis le 20260902** (A-336) : **31 portes, 0 échec**, en
verbatim au dépôt de droit, millésime LEGI 20260901, chaque porte avec son
identifiant `LEGIARTI`. Portée par `appareil/portes_domaine_lfss.py`, documentée à
**`reference/domaine_lfss_LO111-3.md`** *(et non `sources/` : chemin mort corrigé
le 20261001)*. **Aucun fil ne la relève à nouveau — elle existe.** Trois réserves
l'accompagnent : `LO 111-4` et `LO 111-4-1`, les annexes obligatoires, ne sont pas
relevés ; le croisement avec la grille LOLF n'est pas fait, alors que trois portes
Sécu renvoient au III de l'article 2 de la LOLF ; et le relevé **se périme le
17 octobre 2026**, après quoi il se rafraîchit par `droit.py` avant emploi.

**Ce n'est pas la grille qui plafonne les verdicts de loi de financement à
`plaidable`**, mais l'arbitrage n° 3 de `methode/procedure_contre_plf.md` : le
rattachement se plaide par l'implicite budgétaire et le contrefactuel, non par une
porte du domaine. La grille dit ce qui est acquis sans plaidoirie, pas ce qu'on
tente.

**Un texte de loi ne se demande plus à l'auteur** : le dépôt de droit rend le
verbatim de vingt codes et lève sur un article absent plutôt que d'approcher.

**Les deux pièces n'entrent que par pièce jointe** (A-234) et ne vont pas au
coffre (A-235) : elles se déposent sous `sources/plf/` et `sources/plfss/`, et
les règles de `make` sont conditionnelles à leur présence. Ne se versent pas non
plus les deux socles ni les deux JSON d'ouverts, qui se régénèrent à l'octet
(A-71). **Les deux tables plates, si** : ce sont les seules formes de cette
matière qui se lisent sans outil (A-16, A-286).

**Un PDF ne se verse pas au coffre** : les documents du projet ne stockent que du
texte, et un PDF porte des octets nuls. Un livrable PDF se rend à l'auteure et se
régénère depuis son markdown par le script qui l'a produit.

**La mise en ligne ne se fait pas depuis l'atelier** : Vercel y est injoignable
(A-196). Elle passe par un dépôt de publication relié à Vercel, qui ne reçoit
**que les pages rendues** — ni doctrine, ni référentiel, ni appareil (A-197).
**Depuis le 20260904, le site n'est plus généré d'ici** : il se maintient à la
main dans `Site-ETNP/site/` — branche, pull request vers `main`, fusion ;
Vercel redéploie. `generer_site.py` est resté à septembre, et `make publier`
refuse depuis le 20261009 : le jouer écraserait le site en ligne.

---

## Le référentiel des faits

`referentiels/REF_chiffres.json` porte un chiffre par entrée, avec sa valeur,
son unité, son millésime, sa source, sa dérivation, ses déclinaisons, son code
d'origine et son niveau de confiance. Il se régénère depuis trois lieux — les
notes du manuscrit, le `REF_doctrine`, le proto Données — et le sourçage écrit à
la main vit dans `appareil/sources_chiffres.py`, qui survit à chaque
régénération.

| confiance | ce qu'elle dit |
|---|---|
| 3 `strate1` | le manuscrit, corps ou note de fin |
| 2 `source_declaree` | un classeur nommé, une autorité citée |
| 1 `ancrage_ou_operation` | un ancrage de passage, ou une opération rejouée, sans source |
| 0 `sans_source` | un candidat, à sourcer |

**Une opération rejouée dit que le compte est juste, non qu'il est sourcé.**

**La répétition d'un chiffre n'est pas une faute.** Un chiffre énoncé trois fois
fait trois entrées, et le référentiel sert à dire qu'elles concordent. Le
rapprochement de deux entrées s'écrit à la main, par `meme_que` ; il ne se devine
jamais d'une égalité de valeur. Une source se transmet à l'intérieur d'une
proposition, marquée `source_heritee`.

**Aucune source ne s'invente, aucun trou ne se comble.** Un chiffre sans source
traçable reste déclaré sans source, et `make controle` le compte. Un chiffre de
confiance nulle ne sort dans aucun livrable diffusable.

---

## Les champs rédigés

| champ | côté | ce qu'il répond |
|---|---|---|
| `justification` | perte, rente | de quel droit |
| `relais` | perte, rente | et moi alors |
| `apport` | gain | qu'est-ce que ça me fait |
| `contrepartie` | gain | aux dépens de qui |
| `vedette` | gain, perte | deux ou trois signes en tête de ligne |

**La vedette et l'apport font une seule unité**, et ne se citent jamais
séparément. Un chiffre quand le gain en porte un, deux mots quand il n'en porte
pas — « Le temps » se lit sur le même plan que « 70 % ». La phrase ne répète pas
ce que la vedette porte.

**Qui paie se dit une fois, en pied.** Presque toute la restitution est payée par
l'ensemble des économies : `CONTREPARTIE_GENERALE` porte la formule commune.
Seuls le chômage et le patrimoine ont une contrepartie propre, nommée au corpus.

**Chaque gain a une attache, et une seule** — la catégorie où il est le plus
pertinent. Il s'y dit en entier ; partout ailleurs il revient en **rappel**, sa
vedette seule en pied de fiche. Exception : sous trois gains d'attache, une fiche
ne tient pas debout et ses rappels écrits remontent en ligne pleine (A-188).
« Tout le monde », c'est personne : pas de socle.

**Le relais parle à la première personne** : « Je perds A, je gagne B, C et D. »
**L'apport parle à la deuxième du pluriel** : « Votre salaire net monte de 13 %
en un an. » Les deux registres coexistent et ne se mélangent pas.

Un gain sans apport se projette par l'énoncé du REF, qui est une phrase du
manuscrit. C'est le régime transitoire, non la cible.

---

## Règles de rédaction, tous livrables

- **Rédaction positive.** Aucune formulation du type « X ne se décrète pas » ou
  « ne tient pas à… mais à ». Pas de point-virgule en texte normatif.
- **Rien de la nomenclature interne ne sort.** Ni identifiant de nœud, ni degré,
  ni nom de champ, ni mention du référentiel, du classeur ou du manuscrit. Une
  déclaration de source se dit « d'après notre décompte ». Un bloc `[interne]`
  en pied porte la traçabilité et se retire en une opération.
- **Une référence interne ne se cite jamais au dehors.** Les brouillons et les
  protos sont nos propres textes, pas des sources.
- **Tout gain sort avec son miroir nommé, toute perte avec sa raccroche.**
- **Le rang suit le registre.** Un constat se dit précis, une promesse en ordre
  de grandeur.
- **Nos montants sortent toujours arrondis** (règle de l’auteur, 20261019) : 114
  et non 114,46. Entier au-dessus de 10, une décimale en dessous, dans l’unité
  qui convient : 13 milliards, 2,3 milliards, 782 millions, 6,9 millions. Une
  ventilation arrondie se reboucle sur son total arrondi. Un chiffre qui a une
  source publique concrète garde sa précision. Le dispositif garde ses montants
  exacts : seul l’exposé arrondit.
- **L'écart avec les pays comparables mesure le possible ; il ne se promet pas**
  et ne se compte pas avec les pertes.
- **Aucune sortie ne se termine sur un problème.**
- Typographie française : espace insécable devant `; : ! ?` et les guillemets
  fermants, apostrophes typographiques, pas de virgule devant une conjonction de
  coordination.
- **Un séparateur de milliers est une seule espace suivie de trois chiffres.** Il
  se vérifie sur le texte extrait d'un PDF, jamais à l'œil sur une capture.

---

## L'ordre, qui vit au référentiel

`GROUPES` — les familles de personnes, du plus large au plus particulier, les
rentes en dernier. C'est l'ordre des sections.

`PROMESSES` — les ancrages qui sortent en tête d'une fiche, dans l'ordre de la
chaîne du manuscrit.

L'ordre complet d'une fiche : perte, rente, gain, diagnostic — puis les
promesses dans leur ordre, puis les axes de la doctrine, puis le chiffré avant
le qualitatif. **Ni l'identifiant ni l'alphabet ne commandent quoi que ce soit.**

`EVENTAIL` déplie un effet vers toutes les catégories qu'il atteint.

---

## Conduite de session

- **Une question ne se pose que si elle porte sur un input, un output, un
  objectif ou une subtilité.** Le reste se tranche et s'inscrit.
- Quand une question se pose, elle est fermée, avec de courtes pistes, dans les
  mots de l'auteur et non dans le jargon du corpus.
- Prévenir avant toute opération coûteuse : génération docx ou PDF, rendu page à
  page, lecture intégrale du manuscrit ou d'un classeur là où une extraction
  ciblée suffit.
- **Toute pièce restaurée du coffre se compare à son empreinte avant emploi, et
  rien de recopié ne se reverse.** Le contrôle est mécanique : `make
  restauration`. Il ne se remplace pas par une inspection à l'œil.
- Réponses courtes, résultat seul, sans narration de méthode.
- Vérifier sur un cas ciblé avant de généraliser.
- Commit à chaque unité de travail close, jamais en cours de route.
- **Un fil n'est pas un lieu de stockage.** Ce qui doit survivre passe au projet.
- **Avant d'écrire une grammaire de relevé, lire celle du fil jumeau.** Deux fils
  sur deux véhicules du même millésime ont produit deux grammaires divergentes le
  20261001 ; la reprise a fait tomber l'index de 314 mesures à 251.

---

## Lacunes ouvertes

- **Le référentiel des faits est né.** 109 entrées sur 257 restent à sourcer, tous
  les candidats du proto Données. À reprendre par lots, et **les corrections
  doivent ensuite repasser dans les produits** qui citaient ces chiffres.
- `Releve_affecte`, couche de preuve à identifiants `M-nnnn`, appelée par trois
  skills et absente du corpus.
- `D4-2-3` ne porte aucun effet positif depuis la requalification de ses trois
  énoncés en diagnostic.
- Cinq lignes muettes s'ancrent sur une proposition sans effet : `D1-1-1`,
  `D1-2-1`, `D1-3-1`, `D2-4-1`, `D5-3-4`.
- Onze catégories de **rente pure** restent hors galerie — délégataire de titres,
  intermédiaire de la complexité, lobbyiste, gestionnaire de file d'attente. Une
  fiche « ce qui s'arrête » les porterait ; non tranché.
- La charte graphique définitive appelle la couverture du livre, absente du
  projet.
- **`referentiels/socle_plfss_texte.json` n'existe pas.** Les quatre pièces de
  lecture du PLFSS 2027 sont versées, mais la qualification et l'appariement se
  jouent sur le socle, pas sur elles. `REF_norme` ne porte rien côté PLFSS.
