# Les sas ouverts — ce qu'un fil de réconciliation doit absorber

Un **sas** est un document du coffre qui ne fait pas partie du corpus : il porte
ce qu'un fil de production a fabriqué et que le corpus n'a pas encore absorbé —
des modules d'appareil, des entrées de registre, des règles de Makefile. Il
existe parce qu'un fil de production ne touche pas `methode/` et ne joue pas
`make coffre`, et il **se supprime** dès qu'il a été absorbé.

**Un fil qui ouvre un sas l'inscrit ici en fin de fil, d'une ligne** (A-282). Un
fil de réconciliation lit ce fichier au lieu d'inspecter le projet — c'est la
différence entre une liste tenue et une fouille.

**Un sas non inscrit ici est un sas qu'on ne trouvera pas.** Le 20260902, **six
documents du coffre attendaient une entrée d'index sans figurer dans ce
tableau**, et l'un d'eux l'écrivait dans son propre texte ; **deux autres étaient
déclarés au coffre sans y être**. Les huit n'ont été trouvés qu'en confrontant un
par un les documents du projet à ce que l'index déclare, ce qu'aucun script ne
sait faire (A-289). Cinq des six ont reçu leur entrée ; le sixième, le prompt de
versement du fil PLFSS, a été **supprimé** sur arbitrage de l'auteur, son fil
étant clos et sa matière portée ici (A-292).

| sas | ouvert le | par | contient | absorbé |
|---|---|---|---|---|
| `reference/justice_fiscale_1789_fondapol.md` — artefact de corpus, non sas : seule sa dernière section attend | 20260902 | fil de digestion « Fondapol n° 1, justice fiscale » | quatre entrées de registre titrées et datées, sans numéro ; aucun module, aucune règle de `make` | — |
| `reference/nomenclature_prelevements_ifrap.md`, `referentiels/prelevements_ifrap.tsv` et `reference/sourcage_ir_dgfip.md` — artefacts de corpus, non sas : seules leurs dernières sections attendent | 20260902 | fil de digestion « IFRAP n° 277 et DGFiP Stat n° 32 » | **treize** entrées de registre titrées et datées, sans numéro — neuf dans la digestion IFRAP, quatre dans le sourçage DGFiP ; trois entrées d'index à créer, rang `source` pour les deux notes et `referentiel` pour le TSV ; deux sorties à acter de `reference/digestions_attendues.md` §3 ; **deux fichiers du projet à supprimer** et **un report à `methode/carte_des_chantiers.md` §3**, cf. les deux lignes ci-dessous ; aucun module, aucune règle de `make` | — |
| `reference/imposition_du_capital_fondapol.md` — artefact de corpus, non sas : seule sa dernière section attend | 20260902 | fil de digestion « Fondapol, l'impasse de la taxe Zucman » | **six** entrées de registre titrées et datées, sans numéro — dont une **à généraliser hors de cette digestion**, cf. le point 3 ci-dessous ; une entrée d'index à créer, rang `source`, famille `références externes` ; une sortie à acter de `reference/digestions_attendues.md` §3 ; **un fichier du projet à supprimer** — `fondapollimpassedelataxezucman_fr_20260608_formatweb_w.pdf`, l'original que R5 chasse maintenant que sa digestion existe ; **un manquant à instruire** — date et numéro de l'avis du Conseil d'État sur la « taxe Zucman » light, que la pièce ne donne pas ; aucun module, aucune règle de `make` | — |

**Ce que le fil IFRAP–DGFiP demande à la réconciliation, hors registre
(20260902).** Trois actes qu'un fil de digestion ne peut pas poser lui-même.

1. **Supprimer deux fichiers du projet.**
   `etude_fondation_ifrap_liste_des_impots_et_taxes.pdf` (versé le 20260807) et
   `dgfip_stat_32_2025.pdf` (versé le 20260424) sont au projet **en violation du
   §3 de `classement_corpus.md`**. Leur digestion existe désormais, et R5 dit ce
   qui les chasse : **une digestion chasse son original.** Le second pèse 1,2 Mo
   pour 10 ko de sourçage. Un fil de digestion n'a pas la main sur les fichiers
   du projet.
2. **Porter le référentiel à `methode/carte_des_chantiers.md` §3** comme
   **cinquième base du recensement du contre-PLF**, à côté des 128 programmes,
   41 lignes d'économie, 465 dépenses fiscales et 278 taxes affectées — avec la
   réserve qu'il est de nature différente : il ne porte aucun montant et vient
   d'un tiers, non de l'administration. **Arbitrage de l'auteur du 20260902 :
   c'est une base à consulter et à réconcilier pour le PLF, non une pièce de
   passage.** La §7 de la digestion porte les trois réconciliations dues —
   contre les 278 taxes affectées, contre les 243 taxes à faible rendement de la
   Cour, contre la révision du code général des impôts.
3. **Arbitrer le dépassement de jauge**, ci-dessous.

**Dépassement déclaré par le fil IFRAP–DGFiP (20260902).** Les trois documents
pèsent **81 061 octets** — 28 409 pour la digestion IFRAP, 42 528 pour le
référentiel tabulaire, 10 124 pour le sourçage DGFiP — contre **35 000 annoncés**
au fil. Le référentiel est irréductible : 421 lignes de nomenclature. La
digestion avait été resserrée sous son plafond de 25 ko, puis a repris 3 259
octets sur arbitrage de l'auteur, qui a demandé que l'usage permanent du
référentiel soit écrit (§7). Le sourçage tient 10 124 octets contre 8 ko
annoncés, et ne descend plus sans perdre un des cinq tableaux demandés. **Rien
n'a été tronqué.** La suppression des deux fichiers du point 1 rend bien
davantage que ce que le fil a consommé.

**Ce que le fil Zucman demande à la réconciliation, hors registre (20260902).**
Trois actes, et une pesée.

1. **Supprimer un fichier du projet** :
   `fondapollimpassedelataxezucman_fr_20260608_formatweb_w.pdf`. La pièce est
   entrée par pièce jointe, sa digestion existe, et R5 la chasse. Elle pèse
   1,7 Mo pour 30 ko de digestion.
2. **Instruire un manquant** : la pièce invoque un avis du Conseil d'État sur la
   constitutionnalité de la « taxe Zucman » dite *light* sans en donner ni la
   date ni le numéro — seulement sa référence de séance (*JORF*, Compte rendu
   intégral, Assemblée nationale, 2ᵉ séance du 31 octobre 2025, p. 8518 et
   p. 8524). Cet avis est le maillon le plus directement employable de la
   digestion en débat législatif ; il ne se cite pas en l'état.
3. **Généraliser l'arbitrage de statut aux autres digestions de référence
   externe.** L'auteur a tranché le 20260902, après clôture du fil : **une
   digestion de référence externe est une source de faits et un gisement
   d'inspiration, jamais une cible d'alignement.** Aucun paramètre du corpus ne
   se justifie par le fait qu'une pièce le retienne, ni ne se disqualifie par le
   fait qu'elle le combatte ; les paramètres viennent de la doctrine, qui
   confirme ou écarte. **Règle de citation qui en découle : un énoncé repris se
   cite par son autorité d'origine — décision, article, rapport — jamais par le
   nom de la pièce qui le rapporte.** Le statut est écrit en tête de
   `reference/imposition_du_capital_fondapol.md` ; il vaut identiquement pour
   `reference/justice_fiscale_1789_fondapol.md`,
   `reference/nomenclature_prelevements_ifrap.md` et
   `reference/sourcage_ir_dgfip.md`, qui ne le portent pas encore — **vérifié
   par recherche au 20260902 : seule la digestion Zucman le porte.** **Un fil de
   digestion ne peut pas écrire dans le produit d'un autre fil.**

**Un risque de perte à connaître sur ce fichier-ci (20260902).** `project_write`
**remplace le document entier** ; il n'existe pas d'écriture partielle. Trois
fils de digestion ont tourné en parallèle le 20260902 et ont chacun fait une
lecture-modification-réécriture de `methode/sas.md`. **Le dernier qui écrit
efface la ligne de celui qui a lu avant lui et écrit après.** Les trois lignes
coexistent à l'instant où ceci est écrit — vérifié par relecture. Mais un fil
encore ouvert qui écrirait depuis une lecture antérieure à cette version ferait
disparaître les lignes postérieures **sans aucun signal**. Deux parades, à
arbitrer : relire immédiatement avant d'écrire et n'écrire que le fichier
complet relu — ce que ce fil a fait — ou donner à chaque fil son propre fichier
de sas, absorbé puis supprimé. **La seconde supprime le point de contention ; la
première ne fait que le réduire.**

**Pesée du fil Zucman.** `reference/imposition_du_capital_fondapol.md` tient
**31 796 octets** contre 30 ko annoncés au fil. La digestion était rendue à
**30 165 octets**, dans son plafond ; l'auteur a ensuite demandé que le statut
d'emploi soit écrit, ce qui a coûté **1 631 octets nets** après compression du
volet de contestation du diagnostic de « régressivité », qui n'était pas demandé.
**Rien de la matière commandée n'a été tronqué** : les six matières sont
complètes. La suppression du PDF au point 1 rend 1,7 Mo.

## Ce qu'un sas doit porter

Relevé sur les deux passations du socle du texte, qui ont fonctionné, et sur le
prompt de versement que le fil PLF avait écrit pour le fil PLFSS — **supprimé le
20260902 une fois cette liste portée ici** (A-292). Un sas qui omet un de ces
six points fait faire au fil de réconciliation un travail que le fil de
production seul pouvait faire.

1. **Les modules d'appareil**, au format d'archive de `coffre.py` —
   `<<<<<<<<<< fichier <chemin>` / `>>>>>>>>>> fin <chemin>`, chemins canoniques.
   **Preuve obligatoire avant de rendre la main** : déplier son propre dépôt dans
   un répertoire temporaire et vérifier le SHA-256 de chaque module contre
   l'original. Un dépôt non rejoué ne vaut rien.
2. **Les entrées de registre en texte, titrées et datées, sans numéro** (A-282).
   Les renvois internes sont relatifs ; **un renvoi vers l'autre bloc se signale**,
   faute de quoi il périme au décalage (A-284).
3. **Le bloc de journal**, daté, au niveau de titre du journal.
4. **Les entrées d'index** de chaque artefact — `role`, chemin, rang, `coffre`
   oui ou non, `produit_par`, `consomme_par`, famille. Y compris les fichiers
   intermédiaires que les règles de `make` écrivent : un fichier au dépôt que
   personne ne déclare est un échec `I2`.
5. **Les règles de `Makefile`**, conditionnelles à la présence des pièces qui
   entrent par pièce jointe (A-234).
6. **Les empreintes SHA-256** de chaque module, et **l'état de la jauge lu à
   `project_info`** avant et après écriture — jamais une prévision par somme
   d'octets, qui s'est révélée fausse d'un facteur trois (A-128, A-281).

**Une empreinte annoncée dans un récit n'est pas une empreinte relevée** : deux
passations en ont annoncé deux différentes pour le même module. Ce qui fait foi
est ce que le script imprime, et un correctif porte son ancre, sa substitution et
ses deux empreintes (A-283).

## Ce que ce fichier n'est pas

Il ne double pas `methode/index.json` : un sas n'est pas un artefact du corpus,
il n'a ni rôle, ni famille, ni consommateur. Il n'a qu'une date d'ouverture et
une date d'absorption, et sa ligne disparaît d'ici quand il est absorbé.

**Ce fichier-ci, lui, est un artefact** et se déclare à l'index, rang `methode`
(A-287) : il survit à l'absorption des sas qu'il tenait.

## Ce qui a été absorbé, et quand

Le récit de chaque absorption vit au journal, et les décisions au registre. Cette
liste ne dit que ce qui est passé par ici.

| sas | ouvert le | absorbé le |
|---|---|---|
| `technique/depot_socle_plf.txt` | 20260901 | supprimé le 20260902 sans être plié — il portait une version périmée des mêmes chemins canoniques (A-2, A-124) |
| `technique/depot_socle_plfss.txt` | 20260902 | 20260902 |
| `technique/correctif_socle_plf_divisions.txt` | 20260902 | 20260902 |
| `methode/passation_socle_plf.md` | 20260901 | 20260902 |
| `methode/passation_socle_plfss.md` | 20260902 | 20260902 |
