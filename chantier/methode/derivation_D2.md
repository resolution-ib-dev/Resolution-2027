# Dérivation des positions sur l'axe D2 — banc d'essai de la méthode

> **Correction du 20260828 — le 0,54 M est périmé.** L'auteur tranche : le
> décompte à date est de **580 000 postes publics**, soit 10 % des 5,8 M
> d'agents, conformément à A-130 qui pose que c'est notre décompte qui sort.
> Les occurrences de « 0,54 M » ci-dessous datent de la lecture du classeur et
> **ne sortent plus dans aucun livrable**. Le référentiel des positions est
> corrigé : `C-30` porte 580 000 postes publics, `C-05` 5,22 M.

Recentrage de l'État sur ses missions indispensables. Étapes 2 à 4 du fil
« inventaire des gagnants et des perdants ». Aucune écriture au
`referentiels/REF_doctrine.json` (état de la v19 au moment du banc d'essai).

---

## 1. Relevé des trois sources sur le périmètre D2

### 1.1 Manuscrit — huit sections d'ancrage

| section | ce qu'elle nomme |
|---|---|
| `P2-C1-pour-etre-fort-letat-ne-peut-pas-etre-ecartele` | les 7 missions, par définition en creux de tout le reste |
| `P2-C4-fermons-les-structures-non-indispensables-aux-fr` | ANCT, IFCE, CNPF ; 750 sur 1 104 ; « chaque agence, comité, délégataire, prestataire dilue l'action publique » |
| `P2-C4-et-si-nous-arretions-les-frais` | conseil national du bruit ; opéra-comique, centre national des arts plastiques, aides à la presse et à la radio ; producteurs d'huîtres, associations de médiation animale ; 36 €/mois par foyer pour justice et prisons contre 115 €/mois pour les loisirs subventionnés |
| `P2-C4-laissons-les-citoyens-libres-de-leurs-choix` | Fondation de France, Emmaüs, Société nationale de sauvetage en mer ; aide au développement |
| `P1-C3-leuro-detourne` | commission nationale des titres restaurant, élus et syndicats qui la composent, sociétés émettrices de titres ; bailleurs par la démonstration sur les loyers |
| `P1-C3-la-subvention-est-un-poison-pour-la-democratie` | Sanofi (CIR, plus de 100 M€/an), hôtels de luxe en Polynésie, jeux vidéo (66 M€/an) ; grosses entreprises bien introduites ; adjoint au maire et sous-directeur d'administration dont la signature vaut des centaines de millions ; lobbyistes ; « ceux qui savent naviguer dans la complexité de dispositifs parfois faits sur mesure » |
| `P1-C4-les-niches-fiscales-sont-des-subventions-masquee` | 45 % des crédits d'impôt sont des chèques, non des impôts réduits |
| `P1-C4-derriere-une-mission-facultative-il-y-a-une-bure` | la bureaucratie comme sujet d'intérêt propre : « augmenter ses crédits, élargir ses missions et se rendre incontournable » |

Le manuscrit nomme donc massivement des **capteurs**, et il les nomme dans les
sections de diagnostic, non dans les sections de mesure. Les sections de mesure
nomment les perdants ; les sections de diagnostic nomment ceux qui vivent du
dispositif. C'est le premier acquis du banc d'essai.

### 1.2 Classeur — onglet Perdants, lignes rattachables à D2

Trois lignes sur treize touchent D2. Aucune n'est rattachée à un nœud dans le
classeur.

| ligne | effectif | perdants à 1 an | nœud de cause | nœud de raccroche |
|---|---|---|---|---|
| agents publics | 5,8 M | 0,54 M | `D2-2-1` | `D6-2-2` |
| sans emploi, catégorie A | 3,3 M | 3,3 M | `D2-4-1` (aides à l'emploi, 22,5 Md€) | `D3-2` et `D8` |
| locataires HLM | 10,4 M | 3,5 M | `D2-4-1` (APL, 17,7 Md€) | `D7-3-1` et `D9-2-1` |

0,54 M sur 5,8 M font 9,3 % des agents publics. L'input brouillon annonce
« 10 % environ » : les deux concordent, l'input arrondit.

La ligne HLM est plus étroite que la mesure : l'APL couvre aussi le parc privé,
que le classeur ne dénombre pas. Écart de périmètre, à qualifier et non à
réconcilier.

### 1.3 Input brouillon — huit énoncés rattachables à D2

Rubriques « tous les citoyens » (disparition des aides et régimes particuliers ;
interruption des missions facultatives ; grands sujets de société hors contrainte
publique), « dirigeant d'association », « salarié du privé » (chèques
conditionnés), « salarié du public » (10 %, plan de départ), « chef
d'entreprise » (arrêt des subventions), « étranger en situation irrégulière »
(AME).

---

## 2. Dérivation des positions, nœud par nœud

Six propositions, cinq leviers, 33 effets — 9 positifs, 1 neutre, 23 de
diagnostic. Vingt-cinq effets sur trente-trois ne nomment pas de bénéficiaire, et
vingt-trois de ces vingt-cinq sont les effets de diagnostic de l'axe.

### D2-1-1 — Concentration de l'État sur 7 missions

`D2-1-1-e1` est de nature `agrégat` : ses 236,055 Md€ sont la somme de
`D2-2-1`, `D2-4-1`, `D2-5-1`, `D8-3-1-e2` et `D7-2-2-e2`. Il ne porte donc
**aucune position propre** : perdants, gagnants et capteurs appartiennent à ses
composants. Lui en attribuer produirait un double compte.

Position propre du nœud, hors agrégat : l'usager d'une mission facultative perd
la mission. Le manuscrit le nomme sans le chiffrer — producteurs d'huîtres,
médiation animale, opéra-comique. Échelle micro, nature `service`, degré
*nommé*, sans ordre de grandeur individuel.

Bénéficiaire écrit : « finances publiques ». Grandeur, non personne. À
requalifier en *contribuable*, sur l'ancre `P1-C2-a-la-fin-ce-sont-toujours-les-citoyens-qui-paien`.

### D2-2-1 — Fermeture des agences et instances facultatives

| position | qui | échelle | nature | grandeur | degré | raccroche |
|---|---|---|---|---|---|---|
| perdant | agents des 750 structures | micro | revenu, statut | 0,54 M personnes | *indiqué* (classeur) | `D6-2-2`, plan de départ |
| perdant | usagers des services fermés | micro | service | non chiffré | *nommé* | `D3-2`, pouvoir d'achat rendu |
| capteur | la structure elle-même comme sujet d'intérêt propre | méso | statut | 750 structures | *nommé* | sans objet |
| capteur | délégataires et prestataires des agences | méso | revenu | non chiffré | *nommé* | sans objet |
| gagnant | contribuable | macro | revenu | 12,4 Md€/an, soit 34,53 € par mois et par foyer | *indiqué* pour l'agrégat, *déduit* pour le montant par foyer | sans objet |

Le capteur est ici *nommé*, pas *implicite* : le manuscrit consacre une section
entière à établir que la structure facultative poursuit sa propre survie. C'est
la formulation la plus directe du capteur dans tout le corpus.

**Écart relevé.** Les onze sous-items du nœud totalisent 29,3 Md€ quand
`D2-2-1-e2` porte 12,4 Md€. Les sous-items décrivent des flux d'aides versés
*par* ces opérateurs — France Compétences 10,6 Md€ « sortie des aides en 3 ans »,
France Travail 2,7, agences de l'eau 2,1 — qui sont comptés en `D2-4-1`, non le
fonctionnement des structures. Fermer la structure et éteindre l'aide qu'elle
verse sont deux opérations distinctes, portées au même endroit. Les positions
diffèrent : la fermeture a pour perdant l'agent, l'extinction a pour perdant
l'allocataire.

`D2-2-1-e3`, « Rien ne se passe. », est un effet sans bénéficiaire, sans chiffre
et de signe positif. Il énonce l'absence d'effet. Position : aucune, et c'est
exact — un effet nul n'a pas de miroir. Il doit sortir de la population des
effets muets à peupler.

### D2-3-1 — Réinternalisation du régalien

55 agences réinternalisées, ancre manuscrit « une cinquantaine ».

| position | qui | échelle | nature | degré |
|---|---|---|---|---|
| perdant | dirigeants et instances des 55 agences | méso | statut | *déduit* |
| capteur | délégataires du régalien — amendes, titres d'identité | méso | revenu | *nommé* |
| gagnant | citoyens, responsabilité directe | macro | service | *nommé*, qualitatif |

Aucune perte de revenu individuel : la réinternalisation transfère l'agent, elle
ne le licencie pas. Nature `statut`, non `revenu`. C'est la distinction que
l'input brouillon écrase en mêlant « +13 % de salaire » et « forte réduction du
risque de crise financière » sur une même ligne.

### D2-3-2 — Autonomie des établissements patrimoniaux

303 établissements conservés. Signe `+` au référentiel, position ambivalente à la
dérivation : l'établissement gagne son autonomie de gestion et perd sa subvention
d'équilibre. Perdant en second rang : l'usager, si le tarif d'entrée porte
désormais ce que la subvention portait. Degré *déduit*, échelle méso, nature
mixte `statut` et `service`.

Aucun capteur.

**À arbitrer** : un effet dont la position est ambivalente porte-t-il deux
entrées de signe opposé, ou une entrée de signe `±` ? Le champ `signe` du
référentiel ne connaît aujourd'hui que `+`, `−` et `·`.

### D2-4-1 — Extinction des subventions et aides ciblées

68,948 Md€, dont 41,448 aux entreprises et 27,5 aux particuliers et associations.
C'est le nœud le plus riche de l'axe.

**Perdants**

| qui | grandeur | échelle | nature | degré | raccroche |
|---|---|---|---|---|---|
| allocataires APL, parc social et privé | 17,7 Md€ ; 3,5 M en HLM | micro | revenu | *nommé* pour la mesure, *indiqué* pour l'effectif | `D9-2-1` aide universelle, `D7-3-1` détente du marché locatif |
| bénéficiaires d'aides à l'emploi, apprentissage, insertion | 22,5 Md€ ; 3,3 M sans emploi | micro | revenu | *nommé* et *indiqué* | `D3-2` salaire rendu |
| entreprises aidées, dont aides locales | 41,4 Md€ | méso | revenu | *nommé* | `D4` impôts de production, clientèle plus riche |
| associations subventionnées | 3,2 Md€ | méso | revenu | *nommé* | mécénat privé, `D3-2` reste à vivre |
| bénéficiaires de l'APD | 3,0 Md€ | macro | revenu | *nommé* | **aucune** — perdant hors du corps électoral |
| bénéficiaires de l'AME, hors 10 % de soins urgents | 1,1 Md€ | micro | service, risque | *nommé* | **aucune** — renvoi `D9-2-2` |
| hébergés d'urgence hors socle de 20 % | 2,5 Md€ | micro | service | *nommé* | **aucune** |

Trois perdants sans voie de raccroche. `RT-2` exige que toute perte ait une
raccroche nommée : sur ces trois, la règle ne peut être satisfaite, et c'est un
choix doctrinal assumé, non une lacune de peuplement. Le champ `raccroche` doit
donc admettre une valeur explicite « aucune, par construction », faute de quoi le
contrôle sortira trois anomalies permanentes.

**Capteurs** — la trouvaille de l'axe

| qui | dispositif capté | degré |
|---|---|---|
| sociétés émettrices de titres restaurant et chèques vacances | niche sociale sur les titres | *nommé* — « des marges à faire pâlir d'envie les géants de la tech » |
| commission nationale des titres restaurant, élus et syndicats qui la composent | agrément des commerçants | *nommé* |
| bailleurs | APL | *implicite* — « Subventionner les loyers augmente les loyers, pas le nombre de logements » |
| grosses entreprises bien implantées et bien introduites | aides arbitraires et opaques | *nommé* |
| lobbyistes | accès au guichet | *nommé* — « faire la queue ou du lobbying devient un bon investissement » |
| décideurs publics dont la signature emporte l'attribution | subvention discrétionnaire | *nommé* — « la signature d'un adjoint au maire ou d'un sous-directeur d'administration peut valoir des centaines de millions d'euros » |

Le capteur du bailleur est le cas type du degré *implicite* : le manuscrit
démontre le mécanisme de capture et ne qualifie jamais le bailleur de capteur. Sa
démonstration se cite comme un passage.

**Gagnants**

`D2-4-1-e1` porte le solde de +220 €/mois, dont la lacune est déjà déclarée : la
perte est par foyer, le gain par personne, les deux ne se soustraient pas.
Position gagnante réelle : le contribuable, 68,948 Md€, soit 191,52 € par mois et
par foyer — grandeur *déduite*, non ancrée.

### D2-5-1 — Abolition des niches fiscales et sociales

143,2 Md€, dont 52,1 restitués directement et 91,1 compensés en baisse de taux.

**Perdants nommés et concrets** — c'est le nœud qui remplit l'exigence du fil :
Sanofi, plus de 100 M€/an au titre du CIR ; les hôtels de luxe de Polynésie, au
titre du crédit d'impôt pour l'investissement outre-mer ; les entreprises de jeux
vidéo, 66 M€/an. Degré *nommé*, échelle méso, nature `revenu`.

Perdant de masse : le bénéficiaire de niche en général, 486 niches recensées.

**Capteur** : l'intermédiaire de l'optimisation, « ceux qui savent naviguer dans
la complexité de dispositifs parfois faits sur mesure ». Degré *implicite* pour
le mécanisme, *complété* pour la nomination des professions — conseils fiscaux,
cabinets d'agrégation de crédit d'impôt.

Le fil prévoyait des capteurs rares sur l'axe fiscal. Ils n'y sont pas rares :
ils sont d'une autre espèce. Sur la subvention, le capteur s'interpose dans le
versement. Sur la niche, il s'interpose dans l'accès — il vend la capacité à
franchir la complexité. La prévision est à corriger, la méthode ne l'est pas.

**Non-perdants par exception** : outre-mer hors crédits et réductions d'impôt, et
agriculture, écartés de la restitution immédiate pour environ 30 Md€ non
instruits (`D2-5-1-p5`, verdict NON INSTRUIT). Ce n'est pas une position, c'est
une condition. À ne pas porter au bloc `categories`.

**Gagnant** : contribuable, 52,1 Md€ restitués, soit 144,72 € par mois et par
foyer — *déduit*.

---

## 3. Confrontation à l'input brouillon

**Ce qui retombe** — six des huit énoncés rattachables à D2 ressortent de la
dérivation, au nœud près :

| énoncé de l'input | nœud dérivé |
|---|---|
| disparition des aides, subventions et régimes particuliers | `D2-4-1`, `D2-5-1` |
| interruption des missions facultatives | `D2-2-1` |
| dirigeant d'association : fin des subventions, donateurs plus riches | `D2-4-1` (3,2 Md€) et sa raccroche |
| salarié : chèques conditionnés transformés en salaire | `D2-5-1` (niches sociales, 18 Md€) |
| agent public : 10 %, plan de départ | `D2-2-1` cause, `D6-2-2` raccroche |
| chef d'entreprise : arrêt des subventions, clientèle plus prospère | `D2-4-1` (41,4 Md€) et sa raccroche |
| étranger en situation irrégulière : disparition de l'AME | `D2-4-1-s7` |

**Ce qui déborde** — sept positions dérivées que l'input ne porte pas :

1. tous les capteurs, sans exception — l'input le déclare lui-même ;
2. les bénéficiaires de l'aide publique au développement, 3,0 Md€ ;
3. les hébergés d'urgence hors socle de 20 %, 2,5 Md€ ;
4. les allocataires APL du parc privé, absents comme catégorie ;
5. les 303 établissements patrimoniaux autonomisés ;
6. les 55 agences réinternalisées ;
7. les collectivités locales, qui versent 12,3 Md€ d'aides aux entreprises et
   perdent un instrument sans perdre de revenu.

**Ce qui manque** — un seul énoncé de l'input ne se dérive pas de D2 : les 12 %
d'élus dont le mandat est interrompu. Il relève d'un autre axe. Ce n'est pas un
défaut de la méthode, c'est une confirmation qu'elle borne correctement le
périmètre.

**Ce que le classeur donne et que la dérivation retrouve** : les trois lignes
rattachables à D2 se retrouvent toutes, avec leur nœud de cause et leur nœud de
raccroche — que le classeur, lui, ne porte pas.

---

## 4. Ce que la dérivation impose au référentiel

Cinq règles sont sorties du banc d'essai. Aucune n'était écrite dans le fil.

**R-a. Un effet de nature `agrégat` ne porte aucune position.** Les positions
appartiennent aux effets élémentaires. `D2-1-1-e1` agrège cinq nœuds ; lui
attribuer des perdants les compterait deux fois.

**R-b. Les positions se lisent d'abord dans les effets de diagnostic.** Vingt-trois
des vingt-cinq effets muets de D2 sont des effets de diagnostic, et ce sont eux
qui nomment les capteurs. Les peupler en `beneficiaire` serait un contresens :
ils décrivent le système actuel, donc ils portent un `capteur` et un perdant
d'aujourd'hui, pas un bénéficiaire de demain.

**R-c. « finances publiques » n'est pas un bénéficiaire.** Trois effets de D2 le
portent. La requalification en *contribuable* est ancrée au manuscrit, section
`P1-C2-a-la-fin-ce-sont-toujours-les-citoyens-qui-paien`. Même défaut que
« complexité fiscale » en `D4-3-2-e1` et « économie » en `D11-e1`.

**R-d. Le champ `raccroche` doit admettre l'absence assumée.** Trois perdants de
`D2-4-1` n'ont aucune voie de raccroche, par construction doctrinale. Sans valeur
explicite, `RT-2` sortira trois anomalies permanentes qui masqueront les vraies.

**R-e. Un effet nul n'a pas de miroir.** `D2-2-1-e3`, « Rien ne se passe. », est
correctement muet. La population des effets à peupler n'est pas celle des effets
muets.

---

## 5. Nomenclature `categories` — proposition soumise à arbitrage

### 5.1 Choix de structure

La dérivation tranche une question que le fil laissait ouverte. Le fil pose
qu'« une catégorie n'est pas une population, c'est une position dans un
transfert ». La dérivation montre que la même personne occupe des positions
opposées selon l'effet : l'entreprise est perdante en `D2-4-1` et gagnante en
`D4` ; l'établissement patrimonial est les deux dans le même effet.

Conséquence : **le bloc `categories` nomme des ensembles de personnes ; la
position est portée par l'effet, pas par la catégorie.** Les champs `perdant`,
`capteur` et `beneficiaire` de l'effet pointent chacun vers un identifiant de
catégorie. Le principe du fil est préservé — la position reste dans le transfert,
elle n'est simplement pas un attribut de la personne.

### 5.2 Schéma d'une entrée, sur le modèle du `lexique`

```
{
  "id": "C-nn",
  "terme": "",
  "definition": "",
  "population": "",          renvoi au lexique : foyer, personne, travailleur type
  "effectif": "",
  "statut_ancre": "",        manuscrit | classeur | absent des deux
  "source_ancre": "",
  "variantes": [],
  "emplois": [],             identifiants d'effets
  "regle": ""
}
```

### 5.3 Les vingt catégories que D2 produit

Numérotation du banc d'essai, antérieure à la nomenclature fermée aujourd'hui
tenue par `appareil/construire_positions.py`. Elle se lit comme un relevé
d'espèces, non comme la table en vigueur.

| id | terme | positions occupées sur D2 |
|---|---|---|
| C-01 | contribuable | gagnant |
| C-02 | citoyen | gagnant |
| C-03 | foyer | gagnant |
| C-04 | travailleur type | gagnant |
| C-05 | entreprise cliente | gagnant |
| C-06 | association bénévole et donatrice | gagnant |
| C-07 | établissement patrimonial autonome | gagnant et perdant |
| C-08 | agent d'une structure fermée | perdant |
| C-09 | usager d'une mission facultative | perdant |
| C-10 | allocataire d'aide ciblée | perdant |
| C-11 | entreprise subventionnée | perdant |
| C-12 | association subventionnée | perdant |
| C-13 | bénéficiaire de niche fiscale | perdant |
| C-14 | bénéficiaire hors du corps électoral | perdant sans raccroche |
| C-15 | collectivité locale | perdante d'instrument |
| C-16 | structure administrative facultative | capteur |
| C-17 | délégataire et prestataire public | capteur |
| C-18 | émetteur de titres et intermédiaire de l'aide | capteur |
| C-19 | intermédiaire de l'optimisation fiscale | capteur |
| C-20 | décideur public attributaire de faveurs | capteur |

Douze axes ne produiront pas douze fois vingt catégories : les gagnants sont
largement communs. La croissance portera sur les perdants et les capteurs.

---

## 6. Anomalies et écarts consignés

1. `D2-2-1` — sous-items à 29,3 Md€ contre 12,4 Md€ à l'effet du même nœud. Deux
   opérations distinctes portées au même endroit.
2. `D2-1-1-e1`, `D2-2-1-e2`, `D2-4-1-e2` — bénéficiaire « finances publiques »,
   grandeur écrite là où une personne est attendue.
3. `D2-3-2-e1` — signe `+` sur un effet ambivalent.
4. `D2-4-1` — trois perdants sans raccroche possible, par construction.
5. `D2-5-1-p5` — 30 Md€ de secteurs écartés, verdict NON INSTRUIT, sans cellule
   au classeur ni énoncé au manuscrit. Chiffre à établir ou à retirer.
6. `RT-2` porte `noeuds: []` et le verdict À QUALIFIER. La dérivation de D2 lui
   donne ses premiers nœuds d'application.
7. Contrôle structurel sur la v19 — quatre alertes, dont `D6-2-2-p2`, « 7 ans au
   plus » présenté comme valeur unique, qui est précisément la raccroche des
   0,54 M agents publics. À traiter avant tout emploi externe de cette raccroche.
8. Au moment du banc d'essai, le montage projet ne portait plus l'arbre du REF,
   `controle_sortie.py`, le contrat de projection ni les règles de forme
   canonique. Le contrôle de sortie et les règles de forme n'ont donc pas pu être
   appliqués à ce document. Défaut de montage, corrigé depuis par la bascule en
   dépôt.

---

[interne] Étapes 2 à 4 du fil « inventaire des gagnants et des perdants »,
20260820. Aucune écriture au référentiel. Les degrés *complété* signalés dans ce
document appellent arbitrage des auteurs avant toute sortie externe.
