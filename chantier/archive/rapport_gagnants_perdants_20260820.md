# ÉTAT DU CHANTIER — 20260820 v22

Remplace le v20 et clôt le fil. Porte les corrections au corpus, la génération v20 du
`REF_doctrine` et v10 du référentiel des positions, le premier extrait lisible
et son interface, et l'inventaire à rang mis à jour.

## Objet de la session

Inventaire des gagnants et des perdants. Dérivation systématique depuis les
mesures de ce que le projet donne et de ce qu'il retire, à qui, à quelle
échelle, et par quelle voie un perdant se raccroche à un gain.

Le fil prévoyait une épreuve de méthode sur l'axe `D2` avant extension. L'épreuve
a été concluante et l'extension a été menée dans la même session, sur les douze
axes.

## Ce qui en sort

Un référentiel nouveau, de même rang que le `REF_doctrine`. Un relevé des notes
de fin du manuscrit, dérivé de la strate 1, dont l'absence avait laissé passer
deux chiffres majeurs. Trois règles transversales rendues exécutables. Cinq
skills mises à niveau.

---

## Le référentiel des positions

`Positions_20260820_v8.json` — 56 catégories, 204 lignes, dont 201 portant une
position.

| position | lignes |
|---|---|
| gagnant | 122 |
| perdant | 57 |
| capteur | 22 |

Le rapport de la v19 du `REF_doctrine` — 88 effets positifs contre 7 négatifs —
devient 122 contre 79. Les pertes existaient au corpus ; elles n'étaient pas
interrogeables, vivant dans le champ `signe` et le texte libre d'`attenuation`.

Vingt-deux capteurs sortent, dont dix-sept que le référentiel ne portait nulle
part. Le manuscrit les nomme dans ses sections de diagnostic et dans ses notes,
jamais dans ses sections de mesure. C'est le premier acquis de la méthode.

### Pourquoi deux référentiels et non une fusion

L'unité du `REF_doctrine` est l'entrée numérique, rattachée à un effet. L'unité
du référentiel des positions est le triplet ancrage × position × catégorie, et
ses ancrages sont de quatre natures : effet, proposition, sous-item, passage du
manuscrit. Trois d'entre elles n'ont pas de place dans le champ `effets`.

Fusionner découperait le référentiel des positions en deux moitiés, l'une dans
le REF, l'autre dehors. Deux référentiels assumés valent mieux qu'un référentiel
et un reliquat.

**Arbitrage du 20260820 : les deux référentiels restent distincts, de même rang,
avec la même discipline.** Écriture à la main, contrôle par script, dérivés
régénérés, correction qui remonte vers la strate 1 et ne circule jamais
latéralement.

### Structure d'une ligne

| champ | rôle |
|---|---|
| `ancrage` | effet, proposition, sous-item ou passage du manuscrit |
| `position` | gagnant, perdant, capteur |
| `categorie` | identifiant de la nomenclature fermée `categories` |
| `echelle` | macro, méso, micro |
| `nature` | revenu, patrimoine, service, risque, liberté, statut |
| `degre` | nommé, indiqué, implicite, déduit, complété |
| `grandeur_derivee` | vide quand le REF la porte, sinon la valeur et son opération |
| `miroir` | identifiant de ligne, obligatoire si gagnant |
| `raccroche` | identifiant de ligne, reconstitution volontaire, ou absence assumée |
| `justification` | pourquoi la perte est légitime |
| `relais` | la contrepartie en langue ordinaire |
| `note` | ce que la dérivation a relevé |

`miroir` et `raccroche` pointent vers un identifiant de ligne, non vers un nœud.
C'est ce qui rend `RT-2` exécutable : le contrôle devient une jointure, non une
vérification de texte libre.

### La catégorie nomme des personnes, la position est portée par la ligne

Le fil posait qu'une catégorie est une position dans un transfert. La dérivation
montre que la même personne occupe des positions opposées selon l'effet :
l'entreprise perd en `D2-4-1` et gagne en `D4-3-3` ; l'établissement patrimonial
est gagnant et perdant dans le même effet.

**Arbitrage : le bloc `categories` nomme des ensembles de personnes ; la position
reste portée par la ligne.** Le principe du fil est préservé — la position reste
dans le transfert — elle n'est simplement pas un attribut de la personne.
Autrement le solde par personne, objet même de l'inventaire, ne serait plus
calculable.

---

## `C-00 la nation` — deux registres tenus séparés

Le gain d'ensemble, aveugle et dynamique : n'importe qui dans la rue, du seul
fait de vivre dans un pays plus prospère, plus sûr et moins endetté. Vingt-trois
lignes.

**Ce que le système actuel coûte** — position perdante d'aujourd'hui, constats
précis. 63 € produits par heure travaillée contre 23 € nets récupérés. 4 300 €
contre 2 100 € de revenu médian suisse, écart creusé de moitié en vingt ans.
Chômage au-dessus de 8 % contre plein emploi, 4 000 pages de code du travail
contre 200. À économie néerlandaise, 25 % de pouvoir d'achat en plus. Deuxième
taux de sans-abri de l'OCDE avec la première dépense publique. Épargne de
précaution à 18 %. 5 500 € de dette nouvelle par foyer et par an. Au moins 7 %
d'ajustement en cas de rupture d'accès au crédit souverain, plus probablement
plusieurs dizaines de points.

**Ce que le plan rend** — sobre, trois chiffres et du qualitatif déclaré.

| grandeur | levier | source |
|---|---|---|
| de l'ordre de +10 %, environ 10 000 € par foyer et par an | charge administrative | note e32 |
| de l'ordre de 5 points de croissance | complexité fiscale | note e106 |
| 42,87 % à 36,33 % du produit intérieur brut, 191,046 Md€ | prélèvements | `D11-e1` |

**Arbitrage : l'écart mesure le possible, il ne se promet pas.** Trois lignes
portent la mention explicite « illustration du possible, à ne jamais présenter
comme une cible du plan ». Les relais des pertes du système actuel pointent vers
le gain sobre, jamais vers l'écart.

**Point de vigilance.** Les 10 % et les 5 points ne s'additionnent pas sans
examen : le premier porte sur la charge administrative, le second sur la
complexité fiscale. Deux leviers distincts, recouvrement non instruit.

---

## Trois règles transversales

### `RT-2` — miroir et raccroche

Portée à la v19 avec le verdict `À QUALIFIER` et `noeuds: []`. Elle reçoit ses
premiers nœuds et devient un contrôle exécutable : tout gagnant sans miroir
résolu, tout perdant sans raccroche résolue sortent en anomalie.

### `RT-3` — reconstitution volontaire du flux

**Nouvelle, arbitrée le 20260820.** Si tout le monde en est d'accord, l'état
actuel du monde peut être entièrement maintenu : les flux publics se
reconstituent en flux privés d'un montant égal, versés par des Français plus
riches. Ce qui disparaît n'est pas le service, c'est l'obligation de le financer
sans l'avoir choisi.

Conséquence directe : les capteurs de rente ne sont pas sans contrepartie. Celui
qui perd une rente gagne des clients plus riches et un marché plus libre. Vingt-
neuf lignes portent cette voie.

La règle ne vaut pas pour une dette. Le coparent défaillant et le fraudeur ne se
reconstituent pas : deux lignes portent l'absence assumée, et c'est le compte
juste.

### Les deux niveaux de lecture

**Arbitrage étendu.** Là où un agrégat classique et une modulation coexistent,
les deux se tiennent ensemble plutôt que d'en sacrifier un.

Pour l'entreprise : au niveau de l'entreprise la neutralité fiscale tient, les
prélèvements nets de subventions et d'aides sont stables ; au niveau du
propriétaire le solde de −38,17 Md€ à un an se lit dans la marge.

Pour la pression fiscale : au niveau de l'agrégat le taux de prélèvements se
cite et se compare ; au niveau de la mesure réelle, notes e27, e140 et e12, la
pression se lit à la dépense publique déficit inclus, et le produit intérieur
brut surestime la richesse collective.

De la seconde modulation sortent deux gains qualitatifs qu'aucun agrégat
n'enregistre : ce qui est financé par déficit étant un impôt différé, le réduire
baisse le risque de crise ; et la contribution publique étant comptée à hauteur
de ce qu'elle coûte, toute amélioration de la qualité de la dépense reste
invisible au produit intérieur brut.

---

## Le relevé des notes de fin

`Notes_manuscrit_20260820_v1.json` — 141 notes, dont 37 portant un chiffre,
chacune rattachée à sa section appelante.

**Défaut relevé et corrigé.** L'inventaire a d'abord été bâti sur le référentiel,
le corps des sections du manuscrit, le classeur et l'input, sans balayer les
notes. Deux chiffres majeurs y ont échappé : les 5 points de croissance attribués
au passage du 36ᵉ au 1ᵉʳ rang de compétitivité fiscale, note e106, et le coût
d'une rupture d'accès au crédit souverain, note e141.

**Règle : toute recherche au manuscrit balaie le corps et les notes.** Portée à
la procédure de contrôle, étape 0.

**Le manuscrit reste seul point de vérité.** Le relevé est un dérivé, régénéré
par `extraire_notes_20260820_v1.py`, jamais corrigé à la main. Le texte d'une note ne se
recopie ni au REF, ni au référentiel des positions, ni dans un livrable : il se
cite par son identifiant et se tire du relevé à la génération.

Un défaut de ce type a été commis puis corrigé le même jour dans le bloc
`ANCRAGES_MANUSCRIT` du référentiel des positions, qui recopiait le texte de dix
notes.

### `controle_notes_20260820_v1.py`

| règle | ce qu'elle empêche |
|---|---|
| N1 | une citation de note sans note correspondante — référentiel en retard |
| N2 | une note chiffrée qu'aucun référentiel ne cite — raisonnement resté dehors |

Au 20260820 : N1 à zéro, N2 à onze. Les onze se traitent au fil, elles ne
bloquent pas.

---

## Corrections au corpus, à porter

1. **`generer_arbre_20260820_v2.py`** portait `ATTENDU` aux valeurs de la v18 — 149, 63, 54 —
   et un compteur littéral `== 86`. Les deux sont corrigés, le second dérivé.
   Versé en `generer_arbre_20260820_v2.py`.
2. **Lacune de `D2-5-1-p5`** — les 30 Md€ de secteurs sensibles y sont déclarés
   sans cellule ni énoncé. La note e97 les porte, avec le multiplicateur de 0,5.
   Lacune à requalifier.
3. **48 Md€ de taxes sur la main-d'œuvre** hors contribution sociale généralisée
   et contribution au remboursement de la dette sociale — note e109, absent du
   REF, déjà déclaré au bloc des lacunes.
4. **`D5-2-2-e1`** porte un signe négatif sur un énoncé positif.
5. **`D9-2-2`** est rattaché au levier `D8-4` alors que son identifiant relève de
   `D9`.
6. **`D9-ei2`** est un diagnostic classé en gain indirect.
7. **Cinq effets portent une grandeur en bénéficiaire** — « finances publiques »
   trois fois, « complexité fiscale », « économie », « sphère publique ».
   Requalification ancrée au manuscrit, section
   `P1-C2-a-la-fin-ce-sont-toujours-les-citoyens-qui-paien`.
8. **Sous-items de `D2-2-1`** — ils totalisent 29,3 Md€ quand l'effet du même
   nœud porte 12,4 Md€. Fermer une structure et éteindre l'aide qu'elle verse
   sont deux opérations aux perdants différents, portées au même endroit.

---

## Cinq règles que la dérivation impose

**R-a.** Un effet de nature `agrégat` ne porte aucune position propre. Les
positions appartiennent aux effets élémentaires, sous peine de double compte.

**R-b.** Les positions se lisent d'abord dans les effets de diagnostic. Ce sont
eux qui nomment les capteurs, et les peupler en `beneficiaire` serait un
contresens : ils décrivent le système actuel.

**R-c.** Une grandeur n'est pas un bénéficiaire.

**R-d.** Le champ `raccroche` admet trois valeurs et une seule : renvoi vers une
ligne, reconstitution volontaire, absence assumée. Les trois se disent.

**R-e.** Un effet nul n'a pas de miroir. `D2-2-1-e3`, « Rien ne se passe. », est
correctement muet.


---

## Inventaire du montage

Bloc lu par `controle_projet_20260820_v3.py`. Il est le manifeste : une
citation en prose peut viser une version remplacée, elle ne vaut pas déclaration
de présence. Un fichier sans rang sort en M3 ;
un fichier de rang `source` ne sort pas. Six rangs.

| rang | ce qu'il désigne | régime |
|---|---|---|
| `strate1` | le manuscrit, point de vérité unique | jamais révisé en aval |
| `referentiel` | ce qui porte les valeurs | se lit, ne se recopie pas |
| `appareil` | générateurs et contrôles | se rejoue |
| `derive` | ce qu'un générateur produit | se régénère, jamais corrigé à la main |
| `methode` | règles, procédures, état du chantier | se réécrit |
| `source` | corpus amont, classeurs, documentation, protos | entre au projet, ne sort pas d'ici |

```rangs
strate1	Manuscrit_20260820_v4.html
referentiel	Notes_manuscrit_20260820_v1.json
referentiel	Positions_20260820_v16.json
referentiel	REF_doctrine_20260820_v20.json
appareil	apports_20260820_v1.py
appareil	canoniser_ref.py
appareil	construire_positions_20260820_v16.py
appareil	controle_arithmetique.py
appareil	controle_notes_20260820_v1.py
appareil	controle_projet_20260820_v3.py
appareil	controle_sortie.py
appareil	controle_structurel.py
appareil	extraire_notes_20260820_v1.py
appareil	generer_extrait_20260820_v8.py
appareil	generer_interface_20260820_v8.py
appareil	generer_inventaire_20260820_v5.py
appareil	justifications_20260820_v6.py
derive	Derivation_D2_20260820_v1.md
derive	Extrait_gagnants_perdants_20260820_v10.html
derive	Interface_positions_20260820_v9.html
derive	Inventaire_gagnants_perdants_20260820_v9.html
derive	Notes_manuscrit_releve_20260820_v1.txt
derive	REF_doctrine_arbre_20260820_v7.html
methode	Contrat_projection_REF_20260820_v2.md
methode	Croisements_corpus_20260819_v1.md
methode	ETAT_DU_CHANTIER_20260820_v22.md
methode	Procedure_controle_20260820_v2.md
methode	Prompt_fil_apports_20260820_v1.md
methode	Regles_forme_canonique_20260820_v2.md
methode	Regles_redactionnelles_synthese_20260807.md
source	1pager_20260806_v1_proto.html
source	201701LIBERunepropositionrealiste_generationlibre.pdf
source	20250619_Note_Retraite_IB.docx
source	Comparaison_internationale.pdf
source	Constitution_3col_20260730_v44.html
source	Constitution_reference_20260806_v1.html
source	DDHC_20260806_v1.html
source	Donnees_20260806_v1_proto.html
source	France_Resolution_Strategie_Reseaux_2.pdf
source	Input_HLM_20260806_v1_proto.html
source	Input_gagnants_perdants_20260820_v1_brouillon.html
source	LOLF_3col_20260507_v7.html
source	LOLF_reference_20260507.html
source	NL_cba-guidance.pdf
source	Note_entreprises_20260806_v1_proto.html
source	Note_n__1_Justice_fiscalecomment_nous_avons_trahi_1789.pdf
source	PLF26__Depenses_2026_du_BG_et_des_BA_selon_nomenclatures_destination_et_nature_IB_1127.xls
source	PLF_2026_VM_tome_II__Annexe_3__Depenses_fiscales__IB__1126.xls
source	PLF_2026_VM_tome_I__Annexe_2__Taxes_affectees_IB_1113.xls
source	PPLC_consolidee_modificative_20260730_v6.md
source	PPLC_consolidee_substitution_20260730_v6.md
source	Plan_presentation_20260730_v6.md
source	Precedents_restes_a_payer_20260721.md
source	Presentation_20260731_v44.md
source	QA_20260806_v1_proto.html
source	RAPPORTLemodelesocialfrancaisGenerationLibreFevrier2025.pdf
source	Recap_transposabilite_20260731_v6.md
source	Recensement_innovations_20260731_v1.md
source	Reserve_arguments_20260806_v1.html
source	ResolutionD1a.png
source	Synthèse_Calculs_Résolution_0819.xlsx
source	Synthèse_ETP_et_agences_Résolution_0819.xls
source	T_3207_Communes_IB_1113.xlsx
source	T_3305_APUL_IB_1118.xlsx
source	deppee2025donneesfiche09ladepensepourleducation25_12_19IB.xlsx
source	dgfip_stat_32_2025.pdf
source	etude_fondation_ifrap_liste_des_impots_et_taxes.pdf
source	fondapollimpassedelataxezucman_fr_20260608_formatweb_w.pdf
source	guide-public-du-budgetaire-2023.pdf
source	note_reforme_budgetaire_20260730_v12.html
source	structure_ppl.md
```

**Ce qu'un versement emporte.** Le fichier, sa ligne au tableau des livrables, sa
ligne à l'inventaire à rang, le retrait de sa remplaçante, et son générateur
quand il en a un. Les cinq actes ensemble, ou aucun.

**Ce qui ne se verse pas.** Un intermédiaire de travail, une sortie de contrôle,
une variante écartée. Le critère est le rang : ce qui ne relève d'aucun des six
reste en sortie.

---

## Livrables versés à la clôture du fil

| fichier | contenu |
|---|---|
| `REF_doctrine_20260820_v20.json` | trois effets requalifiés en diagnostic, un renvoi d'appareil retiré |
| `Positions_20260820_v16.json` | 276 lignes, éventail déplié, `diagnostic`, champs rédigés côté gain, ordre des promesses |
| `construire_positions_20260820_v16.py` | générateur du référentiel : `GROUPES`, `EVENTAIL`, appel des apports |
| `justifications_20260820_v6.py` | justifications et relais des pertes et des rentes |
| `apports_20260820_v1.py` | apports et contreparties des gains, douze écrits sur cent quatre-vingt-douze |
| `generer_extrait_20260820_v8.py` | générateur de l'extrait |
| `Extrait_gagnants_perdants_20260820_v10.html` | extrait diffusable, ordre des familles |
| `generer_interface_20260820_v8.py` | générateur de l'interface |
| `Interface_positions_20260820_v9.html` | interface par situation, charte du visuel du site |
| `controle_projet_20260820_v3.py` | M1 à M3, fondés sur l'inventaire à rang |
| `Prompt_fil_apports_20260820_v1.md` | ouverture du fil suivant |
| `ETAT_DU_CHANTIER_20260820_v22.md` | ce document |

---

## Anomalie de projet à signaler

Quatre fichiers listés à l'ouverture du fil ont disparu du montage
`/mnt/project` en cours de session, alors qu'ils restent visibles dans
l'interface : `REF_doctrine_arbre_20260820_v7.html`, `controle_sortie.py`,
`Contrat_projection_REF_20260820_v1.md`, `Regles_forme_canonique_20260820_v1.md`.

Conséquences tenues :

- le contrôle à la sortie n'a pas pu être appliqué aux livrables de cette
  session ;
- les règles de forme canonique n'ont pas pu être vérifiées ;
- `Contrat_projection_REF` et `Regles_forme_canonique` reçoivent des **additifs**
  et non des remplacements, pour ne rien écraser à l'aveugle.

L'arbre v7 est reproductible à l'identique par `generer_arbre_20260820_v2.py`.

**Levée au 20260820.** Les quatre fichiers sont revenus au montage. Les deux
additifs sont fusionnés dans leurs documents cibles et disparaissent.

---

## Points ouverts

### 1. Régénération des produits aval

54 fiches mesures, 152 questions, protos du 20260806. Toutes sont antérieures au
référentiel des positions et ne portent donc ni miroir, ni raccroche, ni relais.
Les contrôles P1 et P2 les feraient sortir en anomalie.

### 2. Onze notes chiffrées non reprises

`e29`, `e46`, `e63`, `e65`, `e75`, `e79`, `e83`, `e92`, `e109`, `e130`, `e139`.
Chacune porte un chiffre du manuscrit qu'aucun référentiel ne cite.

### 3. Quatre-vingt-trois effets du REF sans ligne

Presque tous sont des effets de diagnostic ou des gains indirects. Chacun est
soit un énoncé rhétorique sans transfert, soit une position manquante. La liste
sort au bas de l'inventaire.

### 4. `D12` sans aucune ligne

L'axe ne porte aucune proposition au référentiel. Quatre leviers déclarés, zéro
contenu. C'est un trou du corpus, non de la méthode.

### 5. Trois propositions de `D1` sans effet

`D1-1-1`, `D1-2-1`, `D1-3-1` n'ont aucun effet au référentiel. Leurs positions
sont dérivées de la proposition elle-même, ce qui est un pis-aller.

### 6. Le document lisible

L'inventaire est l'appareil. Le document diffusable en est une extraction, au cas
par cas, sans nomenclature D ni identifiants de ligne ni degrés apparents. Le
premier sera vraisemblablement très complet.

### Points 2 à 8 de la v12

Inchangés. Quatre ancres sans opération, deux valeurs absentes des deux sources,
six chiffres du manuscrit absents du REF, quatre alertes de formulation, cinq
corrections classeur, extension du rattachement normatif, calibrage du contrôle
de sortie.

---

## Fil suivant

Régénération des produits aval sur le référentiel des positions, puis extraction
du premier document lisible.

Le site reste indépendant et peut s'ouvrir en parallèle.

---

## Lacunes ouvertes au 20260820

**`D4-2-3` sans effet positif.** La requalification de ses trois effets en
diagnostic laisse la proposition « Sanction plutôt qu'autorisation préalable »
sans énoncé de gain. Le gain de liberté se déduit, il ne se cite pas. À
instruire au manuscrit.

**Cinq lignes muettes.** `D1-1-1`, `D1-2-1`, `D1-3-1`, `D2-4-1`, `D5-3-4`
s'ancrent sur une proposition sans effet. Trois portent le premier axe de la
doctrine : consentement et redevabilité sort sans un seul énoncé propre.

**Recouvrement de `C-01`, `C-02`, `C-03`.** Contribuable, citoyen et foyer
portent la même matière sous trois découpages. Arbitrage d'auteur.

**Charte graphique.** L'interface est rebasée sur le visuel du site : brique
`#b1390f`, or `#ffd249`, crème `#fffdf1`, rayures verticales en or à cinq pour
cent, titres en grotesque noire condensée, capitales espacées pour la
navigation, fiche en carton crème sur fond brique. La charte définitive appelle
encore la couverture du livre, qui n'est pas au montage.

L'extrait reste sur son rendu documentaire : il se lit et s'imprime, quand
l'interface se parcourt.

**Instabilité du montage.** `justifications_20260820_v4.py` a disparu du montage
en cours de session ; il portait l'ensemble des justifications et des relais, et
sa perte empêcherait toute régénération du référentiel des positions. Il est
reversé à l'identique.

`generer_arbre_20260820_v2.py` a disparu et n'a pas pu être reversé : aucune
copie n'en subsistait. L'arbre `REF_doctrine_arbre_20260820_v7.html` reste au
montage et se lit ; il ne se régénère plus tant que le générateur n'est pas
rattaché depuis l'interface.

---

## Purge des mentions internes dans les champs diffusables

Le lecteur extérieur ne rencontre jamais la nomenclature du projet. Huit
mentions sortaient encore.

**Au référentiel des positions**, corrigées au générateur. Deux justifications
citaient le manuscrit comme autorité — « le manuscrit qualifie lui-même de
rente », « le manuscrit raisonne sur la solidarité moyenne » : la substance est
conservée, l'autorité ne se cite plus. Trois grandeurs déclaraient leur source
par le mot « classeur » : la déclaration devient « d'après notre décompte », qui
tient la règle d'émission sans le jargon. Une grandeur portait « atténuation
portée au référentiel » : la mention descend en note, et 38,17 Md€ passe à
38 Md€ au rang de la promesse.

**À la projection**, sept appels de note de la forme « (note e15) » sortaient
dans les justifications. Ils tracent la source pour les auteurs et ne se
publient pas : le générateur les retire à l'émission, le référentiel les garde.

## Sur les fichiers de correction

Le relevé `Corrections_corpus` est supprimé. Les corrections sont portées au
corpus, et ce qui reste ouvert vit ici, à l'état du chantier. Un relevé de
corrections qui survit à leur application devient un second point de vérité.

---

## Registre de l'interface

L'interface s'adresse au lecteur, non aux auteurs. Trois règles arrêtées.

**Le titre dit ce que le lecteur y cherche.** « Ce que j'y gagne », et non une
question de situation. Le chapeau lui dit quoi faire : choisir sa situation.

**La typographie suit l'usage courant.** Capitale initiale aux noms de
catégorie, qui vivent en minuscule au référentiel et sont des intitulés à
l'affichage. Espace insécable devant les deux-points, le point-virgule et les
guillemets fermants. Capitale en tête de chaque ligne.

**Les comptes se lisent en toutes lettres.** « 3 gains · 1 perte » remplace
« +3 −1 ». Chaque ligne porte son étiquette — vous gagnez, vous perdez, rente
supprimée — au lieu d'un signe seul.

Le vocabulaire interne sort des intitulés : « Par domaine » remplace « par
levier », « Votre situation » remplace « par situation ».

---

## L'éventail des bénéficiaires, porté à la structure

**Le constat.** Sur 114 ancrages de gain, 108 ne servaient qu'une seule
catégorie. La dérivation nommait le bénéficiaire principal et s'arrêtait là. Une
catégorie ne recevait donc que les effets dont elle était le bénéficiaire
principal, et perdait tout ce qui l'atteignait au même titre qu'une autre.

**La correction est structurelle.** Le générateur du référentiel porte deux
blocs nouveaux.

`EVENTAIL` — pour chaque ligne mère, les autres catégories que l'effet atteint.
La ligne fille reprend le miroir, la raccroche, l'échelle et le degré de sa
mère : seule la catégorie change. Trente-cinq effets sont dépliés, et le
référentiel passe de 207 à 277 lignes, dont 274 portant une position.

`GROUPES` — l'ordre de lecture, du plus large au plus particulier, les rentes en
dernier. Il vit au référentiel et non dans un livrable : l'extrait s'en sert pour
ranger les catégories à l'intérieur d'un axe, l'interface pour bâtir sa grille.

**Ce que l'éventail rend visible.** Le jeune adulte passe de six à vingt lignes :
aide fondamentale dès dix-huit ans, compte éducation versé à la majorité,
bourses, salaire, restitution, patrimoine, détente du marché locatif. Le chômeur
de longue durée, qui ne portait qu'une perte, porte désormais quatre gains
nommés. L'étudiant de la gratuité, le locataire du parc social, la personne
hébergée en urgence, l'usager d'une mission facultative : toutes ces catégories
avaient une perte et aucune contrepartie.

**Ce qui reste sans gain, et le reste à bon droit.** Les douze catégories de
rente, dont la contrepartie est un marché qui se rouvre et non un gain propre.
Le coparent défaillant et le fraudeur, deux dettes que le corpus assume. La
population bénéficiaire de l'aide au développement, point dur déclaré.


---

## La position `diagnostic`

**Le défaut.** Huit lignes portaient la position `perdant` sur la nation :
l'écart de revenu avec la Suisse, le pouvoir d'achat néerlandais, la
productivité horaire, le taux de sans-abri, la dette de 5 500 € par foyer, le
risque de rupture d'accès au crédit. Aucune n'est une perte causée par le plan.
Toutes décrivent l'état présent, et le plan n'en résout qu'une part qu'il
démontre : l'écart mesure le possible, la dette mesure un risque qui diminue.

Les compter avec les pertes revenait à imputer au projet ce dont il hérite, et
les placer en tête revenait à ouvrir sur un problème qu'il ne règle pas.

**La correction.** Une position propre, `diagnostic`, portée au générateur. Elle
ne se compte ni avec les gains ni avec les pertes. Elle sort dans une section
dédiée, « Le risque qui diminue », placée après les familles de personnes et
avant les rentes supprimées, avec sa mention expresse : ce qui suit décrit l'état
présent, non un effet du plan.

## L'ordre du document

L'extrait suivait les douze axes de la doctrine. Il suit désormais les familles
de personnes du référentiel, qui sont l'ordre du manuscrit et l'ordre de
l'interface.

1. Ce que le plan produit — la promesse d'ensemble, chiffres en tête.
2. Tout le monde.
3. Le travail et l'entreprise.
4. La famille et les âges de la vie.
5. Se loger, se soigner, se former.
6. Épargner et consommer.
7. La vie civique et associative.
8. Quand un dispositif public tient lieu de ressource.
9. Le risque qui diminue.
10. Les rentes supprimées.

Un seul ordre, tenu par le référentiel, servi par les deux livrables.

---

## Les champs rédigés du côté gain

**Le défaut.** Le référentiel portait deux champs rédigés du côté des pertes,
`justification` et `relais`, et aucun du côté des gains. Le générateur ne
disposait donc, pour un gain, que de l'énoncé du REF, qui est une phrase du
manuscrit reprise mot pour mot. L'extrait redécoupait le manuscrit parce qu'il
n'avait rien d'autre à projeter. Sur 195 gains, 106 sortaient sans un chiffre et
33 comme des fragments arrachés à leur paragraphe.

**La correction.** Deux champs nouveaux, symétriques des deux premiers, portés
par un module dédié sur le modèle des justifications.

`apport` — ce que la personne y gagne, en langue ordinaire, à la deuxième
personne du pluriel. Une à deux phrases.

`contrepartie` — qui le paie, en toutes lettres. Une phrase. Elle reste vide
quand le miroir est une rente supprimée et non une perte portée par une personne.

**État.** Douze apports écrits, ceux du travailleur, qui servent de référence de
registre. Cent quatre-vingts gains restent en régime transitoire, projetés par
l'énoncé du REF. Le générateur les compte et le dit à chaque exécution.

**Effet second.** Les champs rédigés font apparaître les doublons du manuscrit :
« Il gardera la maîtrise du fruit de son travail » et « Il sera maître de son
avenir » portent une seule position. La seconde ligne est écartée, commentée au
générateur. Le référentiel passe de 277 à 276 lignes.

## Méthode de tenue arrêtée en fin de fil

Les pièces jointes ne se mettent à jour qu'à la clôture d'un fil, en un seul
passage. En cours de fil, les modifications se font en conteneur, se vérifient
sur un cas ciblé, et ne se généralisent qu'une fois le cas validé.

---

## L'ordre à l'intérieur d'une catégorie

**Le défaut.** Les lignes d'une fiche se rangeaient par identifiant d'ancrage,
donc par ordre alphabétique. Le travailleur voyait la modalité des paliers de
2 % avant la hausse de 13 % et avant les 600 euros rendus. L'alphabet commandait
la hiérarchie du propos.

**La correction, au référentiel.** Un bloc `PROMESSES` porte les ancrages qui
sortent en tête, dans l'ordre de la chaîne du manuscrit : ce qui est rendu
d'abord, ce qui l'accompagne ensuite, la modalité en dernier. Vingt et un
ancrages y figurent, des 600 euros mensuels au taux de prélèvements ramené à
36 %.

L'ordre complet d'une fiche se lit ainsi : perte, rente supprimée, gain,
diagnostic — et à l'intérieur d'un même côté, les promesses dans leur ordre,
puis les axes de la doctrine dans le leur, puis ce qui porte un chiffre avant ce
qui reste qualitatif. Ni l'identifiant ni l'alphabet ne commandent quoi que ce
soit.

Le bloc vit au référentiel et sert les deux livrables. Le travailleur ouvre
désormais sur les 600 euros, puis la hausse de 13 %, puis les 77 centimes nets
par euro gagné. Le jeune adulte ouvre sur les 600 euros et l'aide fondamentale
dès dix-huit ans. La nation ouvre sur le gain d'ensemble de 10 %.
