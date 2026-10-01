# Carte des chantiers

**Réécrite le 20260917.** La version du 20260827 ne portait que trois chantiers —
site, gagnants-perdants, contre-PLF. Trois autres sont nés depuis et occupent
aujourd'hui l'essentiel du travail. Elle ne produit aucun fond : elle dit ce qui
est fait, ce qui est prêt, ce qui bloque quoi, et ce qui revient à l'auteur.

**L'ordre vient des dépendances, jamais d'un calendrier.**

---

## Vue d'ensemble

| chantier | état | ce qui le bloque |
|---|---|---|
| **1. Projection du programme** — du livre à la liasse | en cours, chemin critique | rien : la matière des lots F et G est versée |
| **2. Machine d'amendement** | 5 étapes sur 7, transférée au projet machine | l'écart se mesure désormais sur le banc des liasses d'un tiers |
| **3. Lecture des textes financiers** | 2026 lu, module non outillé | date imposée par le dépôt du texte suivant |
| **4. Socle budgétaire et grille** | dix bouclages verts, premier cercle | rien : lot suivant écrit |
| **5. Révision constitutionnelle** | PPLC consolidée, présentation à jour | arbitrage de diffusion |
| **6. Gagnants-perdants** | côté perte écrit, côté gain à 6 % | le format cible n'est pas arrêté |
| **7. Site** | architecture tranchée, périmètre ouvert | gagnants-perdants, et le périmètre |

**Parallélisable depuis le 20260917.** Les fichiers cumulatifs s'écrivent par
fragments datés (`appareil/fragments.py`) : deux fils peuvent travailler en même
temps sans qu'aucun n'écrase l'autre. C'était le goulot unique, il est levé.

---

## 1. Projection du programme — du livre à la liasse

**Ce que ça vise.** Une liasse qui décline le programme sur le texte financier
déposé. Exhaustive, par morceaux, chaque morceau tenant seul.

### Fait

**Le découpage doctrinal est clos.** 71 énoncés, **17 blocs**, un pivot par bloc,
listes de solidaires closes et datées, bilan à cinq lignes, rang doctrinal motivé.
Quatre blocs portants, douze structurants, un d'accompagnement.

**Le contrôle est mécanique et il attrape.** `controle_blocs.py` sort `B1`–`C4` à
zéro et, depuis le 20260917, une série `D` qui confronte chaque grandeur du bilan
aux paramètres de l'énoncé nommé — 107 grandeurs vérifiées, **une anomalie
réelle** : `B-07` citait 108,56 Md€ que le paquet ne porte nulle part. Le contrôle
est éprouvé sur un jeu de fautes et un jeu de justes.

**Les sept bilans déséquilibrés sont instruits.** Dix termes manquants,
**3 portés, 6 estimés, 1 absent**, chacun avec son onglet et son bouclage —
`livrables/comblement_termes_manquants.md`.

**Trois arbitrages pris le 20260917.** Le programme ne boucle qu'au total, jamais
bloc par bloc : `B-05` et `B-07` restent déséquilibrés et le disent. Le nœud de
mise en œuvre existe comme objet, et on en écrit **un seul d'abord**. Un terme
qu'aucune pièce ne porte est à produire, non absent.

**La matière des lots F et G est versée — 20260928 au 20260930.** Quatre pièces
commandent désormais l'aval du découpage.

`methode/plan_sept_phases_20260930.md` — le plan de rédaction arrêté par
l'auteure. Sept phases, une par noyau narratif tenant seul devant le rapporteur ;
la concentration précède la restitution ; quatre temps par mesure. Il ordonne les
lots F et G et **il révoque la passe à blanc** (voir ci-dessous).

`livrables/arborescence_mesures_20260928.md` — sept mouvements, 17 blocs,
**66 mesures portées sur 65 lignes**, M-067 et M-068 — deux directions sans
dispositif — partageant une ligne ; 157 composantes juridiques typées ;
**49 décisions de relecture de l'auteure, dont 45 sur une mesure et 4 sur la
portée d'un bloc ou d'un mouvement** ; 26 bornes. C'est l'unité de découpe des morceaux du lot `F` et le
gabarit des dossiers du lot `G`. Son rendu visuel est un artefact publié, hors
projet, et n'appartient pas au corpus.

**Le CGI réécrit par l'expert** — neuf pièces `cgi_expert_*`, plus
`livrables/predigestion_cgi_20260929.md`. Rédaction cible de l'auteur sur
2 376 articles : elle alimente la colonne C du trois colonnes à l'étape E4, donc
le lot `G`. Son emploi est borné par
`reference/cgi_expert_regles_de_lecture.md` — millésime au 1er mai 2026,
254 articles à contrôler avant emploi, 74 commentaires non tranchés.

`livrables/mecanique_gages_restitutions_20260929.md` et
`referentiels/prelevements_forces_20260930.tsv` — la matière de gage et le
recensement des 420 prélèvements. Le sort des prélèvements n'est pas attribué :
c'est le plus gros poste restant, et il ne bloque que la phase 3.

### Prêt à partir

**Le tri par véhicule.** Prompt écrit et versé, n'attend aucun chiffre. Son point
de rupture dira quelles transitions sont urgentes.

**Le nœud de mise en œuvre.** Gabarit à écrire, puis rempli sur la sortie des
fonctionnaires — trois énoncés qui ne disent ni le séquencement, ni le coût année
par année, ni le régime de ceux qui restent, ni le sort de celui qui refuse.

**Le sort des prélèvements est attribué — 20260930.** 420 prélèvements, aucun
sans sort, **un seul `en attente`** : les contributions sur les attributions
d'options et d'actions gratuites, 1,67 Md€, question de doctrine remontée à
l'auteure. 4 conservés, 50 fondus, 193 supprimés, 50 maintenus à part, 25 sortis
du périmètre des PO, 11 non touchés, 83 hors mandat, 3 hors champ. Les 41
prélèvements à contrepartie invoquée sont audités ligne à ligne — 16 supprimés,
25 repliés, le repli portant 20 % du lot en euros. Bouclage en quatre lignes de
solde. Pièces : `livrables/sort_prelevements_20260930.md`,
`referentiels/sort_prelevements_20260930.tsv`, et le classeur
`reforme_prelevements_20260930.xlsx` remis à l'auteure — le coffre ne stocke pas
de binaire.

**Les trois arbitrages de phase 1 sont tranchés — 20260930.** M-002 : la liste
close, organisée par les critères — 746 lignes à établir, 8,632 Md€ tenus.
M-016 : le tiers non public et non lucratif, quel que soit le payeur — le
versant social entre au champ, donc **la mesure devient à deux jambes, PLF et
PLFSS**. M-026 : les secteurs écartés sont **différés et non sortis du champ** —
exception de calendrier, pas de champ ; aucune niche n'est conservée.
`methode/fragments/arbitrages/20260930-arbitrages-phase1.md`.

### Reste

| lot | produit | dépend de |
|---|---|---|
| `D` tri par véhicule | transposabilité puis rattachement, mesure par mesure | découpage |
| `V` valise outillée | arguments, chiffres, réservoir de gage, indexés par bloc | découpage |
| `F` blocs de rattachement | morceaux, ordre de passage arrêté | `D` + arborescence |
| `G` dossiers de mesure | treize contrôles joués | `F` + `V` + CGI réécrit |
| `J` liasse déposée | — | `G` + ré-ingestion |

**Chemin critique** : découpage → tri par véhicule → morceaux → dossiers →
liasse. Il est dégagé jusqu'au bout.

**Trois corrections dues à `livrables/arborescence_mesures_20260928.md`, et
aucun fil ne les porte.** Déclarées par le fil des arbitrages de phase 1, hors de
son mandat : la règle « pas de cas nommés » vaut pour la présentation et ne borne
pas le dispositif ; la borne de M-026 porte une exception de champ là où la
décision est une exception de calendrier ; M-016 devient une mesure à deux
jambes, et la scission n'est pas portée. **Tant qu'elles ne sont pas écrites,
l'arborescence contredit le registre sur trois points.**

**La table de passage au coffre n'est pas corrigée, et c'est délibéré.**
`referentiels/table_passage_schema_prelevements_20260930.tsv` porte encore
l'ancien rattachement de « dont forfaits de cotisation » : la copie de travail du
fil ne portait que six des huit colonnes, et réécrire le fichier aurait perdu
`siege_code_normalise` — une reconstruction, pas une correction. **La clé
corrigée est appliquée à toute l'attribution** ; le patch de deux lignes est
rendu au livrable et dû au dépôt. Les compteurs de
`livrables/couverture_table_de_passage_20260930.md` sont rejoués au livrable du
sort, non au fichier. Tout fil qui ouvre le TSV lit un état antérieur à
l'attribution.

**Les prélèvements obligatoires 2024 valent 1 251,8 Md€**, chiffre Insee repris
du classeur. Les 1 250,76 qui circulaient sont écartés. *La propagation du
chiffre à `REF_chiffres` et aux pièces qui le citent n'est pas faite.*

**Le relevé de siège — inscrit le 20260930, dû avant la phase 3.**
`methode/fragments/arbitrages/20260930-perimetre-fiscal.md` mesure que
**105 prélèvements du référentiel ne portent aucun siège renseigné**, dont les
prélèvements de solidarité, 15,6 Md€. Un sort s'attribue sans adresse ; un
amendement ne s'écrit pas sans elle. Le trou ne mord pas à l'attribution du
sort ; il mord à la rédaction. Le relevé porte sur les prélèvements sans siège
qui reçoivent un sort autre que « non touché » ou « hors mandat » — son périmètre
exact n'est donc connu qu'à la sortie du fil d'attribution. Il n'était inscrit à
aucun plan avant ce jour. **Son périmètre est désormais calculable** : les sorts
sont attribués, et le croisement du référentiel de sort avec les prélèvements
sans siège le rend. Le croisement n'est pas joué.

**Le lot `H` n'existe plus — 20260930, déclaré au plan en sept phases.** La passe
à blanc est supprimée : la valise est branchée dès la première passe, quatre rôles ouverts, et
la valeur du matériel se mesure sur le banc des liasses déposées par un tiers,
jamais sur nos propres mesures. Le contrôle sur les rôles disponibles et non
ouverts reste armé — un énoncé livré sans arguments sourcés, sans principe ou sans
paramètres sort à « à vérifier avant dépôt ». La base de travail est le droit en
vigueur, jamais le PLF 2026 : le rattachement au texte en discussion est fabriqué
et se déclare comme tel.

### Les lettres de lot — réglé le 20260917

`plan_bataille.md` appelait `D` la valise et `E` le tri par véhicule, quand le
prompt du tri s'appelait déjà `prompt_lot_D`. **Le tri par véhicule est le lot
`D`, la valise devient le lot `V`, la lettre `E` n'est plus employée.** Les
lettres nomment, elles ne classent pas.

---

## 2. Machine d'amendement

**Ce que ça vise.** Une procédure outillée qui prend l'énoncé d'une mesure en
langage naturel et rend un amendement déposable, pour n'importe qui, sur
n'importe quel véhicule.

### État

**Cinq étapes sur sept existent.** Le rattachement n'est pas outillé et ne le sera
pas en v1 ; la liasse n'existe pas. Sur les quarante-deux couples du banc des
liasses déposées, **seize ne peuvent être pris par aucune étape outillée**.

**Trois bancs, et ils ne mesurent pas la même chose.** Rédaction cible — 42
couples, joué, corrections dues. Liasses déposées — 42 couples, construit, jamais
joué. Chouchous — 15 mesures, construit, jamais joué.

**La machine a déménagé** : son point de vérité est au projet machine, et le
coffre n'en garde aucune copie vivante.

**Une quatrième population de test est versée depuis le 20260929** : les neuf
pièces `cgi_expert_*`. Elles portent une rédaction cible déclarée sur
2 376 articles du code général des impôts, avec leurs segments d'insertion et de
suppression — donc de quoi éprouver E4 et la réapplication à une échelle qu'aucun
des trois bancs n'atteint. Elle ne se joue qu'en ayant lu
`reference/cgi_expert_regles_de_lecture.md` : 254 articles partent d'un état qui
n'est plus le droit, et un banc joué dessus mesurerait l'écart de millésime, non
la machine.

### Reste

L'écart à blanc contre équipé, sur la liasse déposée par un tiers — deux passes
sur la même population, et l'écart entre les deux taux est la valeur du matériel.
C'est la seule mesure de valeur que le plan du 20260930 admette encore.
**L'écart mesuré est un minorant** et se publie comme tel : la population est faite
des mesures d'un tiers, la valise porte notre doctrine.

Neuf des treize contrôles du contrat ne sont pas outillés. Aucun véhicule autre
que la loi de finances n'est éprouvé sur un banc.

---

## 3. Lecture des textes financiers

**Ce que ça vise.** Un module qui rend le texte déposé en forme fixe le jour où il
tombe — quatre blocs qui ne bougent pas d'un millésime à l'autre : solde, portes
ouvertes, mouvements sur nos objets, écart à nos positions.

### État

2026 est lu : listes PLF et PLFSS, différences, formats, index des mesures,
articles ouverts, confrontation et son bordereau. Le résumé attendu est écrit et
gelé.

### Le millésime 2027 arrive — 20261001

**Annoncé par l'auteure.** Le PLF et le PLFSS 2027 travailleront sur le droit en
vigueur, aux entrées en vigueur différées déjà votées près : la confrontation au
droit est donc possible, et ces décalages sont le point sensible du millésime.

**Les annexes ne sont pas parues à ce jour.** Le prompt est écrit et versé —
`methode/prompt_fil_lecture_textes_2027.md` — et il est découpé pour ça : les
lots qui dépendent des annexes partent **suspendus** et se rejouent seuls à leur
arrivée, sans toucher au reste. Les deux véhicules suffisent à jouer L1, L2 et
L4 dès le dépôt.

**Pièces à joindre au lancement** : le PLF et le PLFSS en PDF, **les deux** — le
fil 2026 n'avait pas le PDF du PLF et n'a pas pu relire à l'œil côté finances.

### Reste

Le module n'est pas outillé. **Deux modules manquent et se réécrivent avant le
dépôt, pas après** : `portes_ouvertes.py` et `controle_socle_plf.py` — aucun n'a
de sortie versée qui vaudrait spécification.

**La grille des portes du domaine des lois de financement n'est pas relevée** :
dix-huit verdicts plafonnent à `plaidable` et y resteront tant qu'elle manque.

### Date

**La seule date qui ne se négocie pas.** Le texte déposé ne se relit pas l'année
suivante. Le calendrier d'examen n'est pas au corpus : il se confirme.

---

## 4. Socle budgétaire et grille de lecture

**Ce que ça vise.** Lire les classeurs de l'auteur de façon rejouable, en tenant
séparés ce que le document budgétaire publie et ce que l'auteur y a ajouté.

### Fait

**Dix bouclages, zéro échec**, rejoués le 20260917 sur les annexes courantes :
434 entités et un régime chacune, 479 514 emplois, 1 104 agences en quatre
familles, 17 922,39 M€ de taxes restituées, 465 dépenses fiscales, 32 bouclages
sur 32 de l'arbre des économies, 5 dérivations sur 7 avec 2 écarts de concept
documentés, la part supprimable retrouvée sur 4 catégories sur 4.

### Prêt à partir — et c'est le plus rentable qui soit visible

**Le second cercle.** Cinq onglets des classeurs ne sont pas importés au socle —
`CI unique`, `Fusion taxes`, `CSG`, `Perdants`, `GraphAFU` — et le classeur DEPP
n'est pas ouvert. Un sixième, `Gages`, est importé et n'est comparé à rien.

Les importer avec leurs bouclages fait passer **cinq chiffrages de « estimé » à
« prouvé » sans produire un seul chiffre neuf**. Prompt écrit :
`methode/prompt_fil_socle_second_cercle.md`.

### Ramification

**Les annexes vont être remplacées par des versions à jour.** Tout chiffre qui en
est tiré se rejoue après remplacement. La grille est écrite pour que la bascule
soit un rapport et non une reprise : quatre listes sortent — disparus, nouveaux,
montants qui bougent, périmètres qui changent — et le reste se rejoue seul.

---

## 5. Révision constitutionnelle

PPLC consolidée en deux formes — modificative et substitution —, présentation,
récapitulatif de transposabilité, recensement des innovations, trois colonnes de
la Constitution à jour. L'état du chantier vit dans
`methode/etat_revision_constitutionnelle.md`.

**Ce qui reste est un arbitrage de diffusion**, non un travail.

---

## 6. Gagnants-perdants

**Le côté perte est écrit** — 49 positions perdant, justification et raccroche
complètes. **Le côté gain ne l'est pas** : 194 gains, **12 apports sur 194**, 11
contreparties sur 194. Il reste 367 textes courts.

**La définition est tranchée** : il n'y a pas de perdant ultime, seulement des
perdants ponctuels ; le gagnant varie selon le sujet. La maille est déclarée ligne
à ligne.

**Ce qui bloque, et ce n'est pas le volume** : le format cible n'est pas arrêté.
Écrire 367 textes dans un registre que le format refusera, c'est les écrire deux
fois. **Le prototype coûte quatre apports** — un pour cent du volume — sur `C-30`,
l'agent d'une structure fermée, le cas où « pas de perdant ultime » doit tenir
visuellement ou pas.

**C'est le verrou unique du chantier 7.**

---

## 7. Site

**Architecture tranchée et non rouvrable** : le site est un dérivé, `make` produit
les pages, Vercel déploie la sortie et n'écrit rien. Aucune donnée ne se saisit
dans le site.

**La surface publiable aujourd'hui est de douze gains** — ceux qui portent un
apport. Et 93 chiffres sur 257 restent à sourcer ; un chiffre de confiance nulle
ne sort dans aucun livrable diffusable.

**La date ne vient pas du site** : le jour où un contenu public pointe vers lui,
il existe.

---

## Ce qui traverse tout

### Le point de vérité et la propagation

Aucun produit ne porte un chiffre qui ne soit pas au référentiel. Aucun produit ne
se corrige en aval : une erreur remonte à l'étage où elle est née, puis on rejoue.
Trois adresses, une par nature de chiffre — les faits, le chiffrage des économies,
ce que le PLF publie.

### La frontière de projet — 20260930

Le découpage des mesures, les énoncés, les paramètres, les arguments et leur
vérification se font **au projet doctrine**. La qualification, le rattachement, le
vecteur, la rédaction cible, l'exposé sommaire et la liasse se font **au projet
machine, valise branchée**. Une ligne de lancement du projet doctrine n'active
jamais `disposition-cible`, `redaction-legistique` ni `expose-sommaire` ; elle
peut activer `compatibilite-doctrine` et `vecteur-mesure`. Règle portée au socle
des prompts de fil, où elle se vérifie à chaque lancement — enfreinte deux fois
le 20260930.

### L'écriture concurrente — levée le 20260917

Un fil n'écrit plus aux fichiers cumulatifs : il dépose un fragment daté, et
`appareil/fragments.py` assemble. L'historique est repris verbatim, la queue se
régénère, **l'assemblage est idempotent**. Éprouvé sur six cas.

### La dette d'appareil

**Cinq modules attendent une session claude.ai/code** — un fil Cowork ne peut pas
pousser. Ils voyagent au paquet
`methode/paquet_depot_application_20260917.md`, plus les deux paquets antérieurs.

**Le générateur de l'index a décroché de l'index — mesuré le 20260930.**
`appareil/generer_index.py`, au clone du dépôt, rend **253 artefacts** quand le
coffre en porte **310**. Trente-neuf déclarations antérieures à ce fil n'y sont
pas, plus les dix-huit du 20260930. Un `make index` joué en l'état **détruirait
les cinquante-sept**. La table curée se rattrape avant tout rejeu de l'index, et
la reprise ne se fait pas depuis Cowork : le mandataire git refuse la poussée
tant que le dépôt n'est pas déclaré aux sources de la session.

**Deux modules sont perdus** : `plier_paquet.py` et `controle_projection.py`,
déclarés de voie `depot` et absents du clone.

**Quatre documents sont au coffre et absents de l'index** — ils disparaissent au
premier `make reindex` et ne se restaurent pas. C'est arrivé deux fois.

### Le stock de règles sans garde-fou

Le corpus compte désormais les règles écrites qu'aucun contrôle ne joue. C'est ce
stock qui produit les fautes, et il ne diminue pas seul.

---

## Ce qui revient à l'auteur

1. **Le format des fiches gagnants-perdants** — il commande 367 textes, et il se
   prototype pour quatre apports.
2. **Le site** — vitrine seule, ou vitrine plus l'outil « ce que le plan change
   pour moi » ? Et qu'est-ce qui est public.
3. **Le recouvrement de `C-01`, `C-02`, `C-03`** — contribuable, citoyen, foyer.
   Il commande 53 apports et se pose avant la première ligne.
4. **Le registre de l'amendement** — GL ou Résolution, quand les deux divergent.
5. **La stratégie de dépôt** — combien d'amendements, sur quels articles, dans
   quel ordre, lesquels tombent si un autre passe.
6. **Le calendrier du texte financier suivant** — il n'est pas au corpus.
7. **La diffusion de la révision constitutionnelle.**
8. ~~**Les trois arbitrages qui bloquent la phase 1.**~~ **Rendus le 20260930.**
   La phase 1 est ouverte — sur un petit nombre de mesures d'abord.
9. **Le sort des contributions sur les attributions d'options et d'actions
   gratuites** — supprimées comme prélèvement sur la main-d'œuvre, ou détaxées ?
   1,67 Md€, seul prélèvement des 420 en attente, et il commande la cohérence
   entre M-025, M-031, M-034 et M-043.

---

## Ce qui a une date

| chantier | date | d'où elle vient |
|---|---|---|
| Lecture du texte financier 2027 | dépôt des textes — annoncé, annexes non parues au 20261001 | extérieure, **à confirmer** |
| Essai | 9 octobre 2026 | arrêtée |
| Tout le reste | aucune | dépendances seules |

---

*20260917 — réécrite par le fil d'application. Elle n'a produit aucun fond.*
*20260930 — le fil d'inscription au registre y porte la matière des lots F et G,
la quatrième population de test, et la suppression du lot `H`. Aucun fond produit.*
*20260930 — le fil de versement y reprend les en-têtes corrigés de
l'arborescence et le décrochage du générateur de l'index. Aucun fond produit.*
*20260930 — le fil de traduction y inscrit le relevé de siège, la frontière de
projet et les trois arbitrages dus. Aucun fond produit.*
*20260930 — le même fil y porte le bilan des deux fils lancés en parallèle :
sort attribué, trois arbitrages rendus, et les quatre reprises qu'aucun fil ne
porte. Aucun fond produit.*
