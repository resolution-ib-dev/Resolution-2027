# Simulateur « Reprenez votre argent » — éléments, règles et sources, 20261112

**Objet.** La page `Site-ETNP/site/reprenez.html` laisse un lecteur saisir son
salaire net, puis décocher les économies qu’il préfère garder ; elle dit ce que
chacune lui rapporte par mois, en salaire net et en épargne. Ce référentiel porte
tout ce que la page calcule : **chaque élément cochable**, son poste, son
ministère et ses montants. Cette note dit d’où vient chaque montant et quelles
règles sont de l’auteur, lesquelles ont été tranchées en propre.

| fichier | une ligne par | lignes |
|---|---|---:|
| `simulateur_elements_20261112.tsv` | élément cochable | **502** |
| `comptes_strates_locales_20261112.tsv` | ligne de compte d’une strate locale | **144** |

**Le générateur** est `Site-ETNP/outils/restitution.py`. Il lit les classeurs
servis par le site et les cartes de la carto, inscrit les données dans la page,
et, avec `--tsv <dossier>`, écrit ces deux fichiers. Tout chiffre de cette note
est *relevé* sur les deux fichiers le jour de l’écriture, sauf mention contraire.

---

## 1. Les grandeurs

| grandeur | valeur |
|---|---:|
| éléments cochables | **502** |
| économies de première année | **129,46 Md€** |
| économies en régime plein | **236,40 Md€** |
| dont rendu en salaire net | **114,46 Md€** |
| dont rendu en épargne, première année | **15,00 Md€** |
| dont rendu en épargne, régime plein | **121,94 Md€** |
| ministères | **19**, plus **7** blocs hors ministère |

Colonnes de `simulateur_elements_20261112.tsv` : `groupe`, `carte`, `poste`,
`theme`, `element`, `ministere_ou_bloc`, `niche_commune` (« oui » pour une niche
comptée pour moitié sous deux postes), puis cinq montants en milliards d’euros
par an : `premiere_annee_mde`, `regime_plein_mde`, `dont_salaire_mde`,
`dont_epargne_premiere_annee_mde`, `dont_epargne_regime_plein_mde`.

## 2. Du salaire saisi aux euros par mois

**Le gain plein** est la CSG et la CRDS sur les revenus d’activité, **la même
part du salaire net pour tous** : 12,56 %, la ligne « Net médian » de l’onglet
`CSG-CRDS` de `Synthèse Chiffres` (« tout est parfaitement proportionnel […] juste
un même ratio », auteur, 20261112).

**Un milliard d’euros vaut le gain plein divisé par 114,46**, la masse de CSG et
de CRDS d’activité. Au salaire de 2 300 € nets, cela fait 289 € par mois de
salaire et 308 € par mois d’épargne en régime plein (*relevé sur la page*).

**L’épargne est proportionnelle au salaire**, au même prix par milliard
(*validé*, auteur, 20261112). L’ordre de grandeur retombe sur
les 600 € par mois de la carto.

## 3. La ventilation entre salaire et épargne

**Règle de l’auteur** (« patrimoine et chômage doivent être entièrement en
épargne. le reste ventilé au pro rata de ce qui reste (ou de notre calendrier ?) »,
20261112), exécutée sur le calendrier du classeur :

- l’économie de **première année** d’un élément paie la CSG et la CRDS d’activité
  à hauteur de 114,46 / 129,46, et son reliquat va à l’épargne ;
- tout ce qui vient **après la première année** va à l’épargne ;
- l’assurance chômage et le rendement du patrimoine, nuls la première année, sont
  donc entièrement en épargne.

La première année et le régime plein de chaque poste sont les colonnes « Gain en
année 1 » et « Gain supp. en année pleine » de l’onglet `Annexe Manuscrit`.

## 4. L’arbre, et la source de chaque poste

L’arbre est celui de la carto : cinq groupes, onze cartes, dix-neuf postes.

| poste | éléments | première année | régime plein | détail tiré de |
|---|---:|---:|---:|---|
| Agences fermées et leurs interventions | 40 | 7,08 | 9,32 | lignes « O » de `Détail Economies` ; taxes affectées par bénéficiaire ; subvention arrêtée d’un programme partagée entre ses opérateurs au prorata de leur subvention au jaune |
| Fonctionnement des administrations de l’État | 50 | 3,8 | 3,8 | programmes non indispensables de `Economies R` : 80 % du fonctionnement et de l’investissement |
| Audiovisuel public | 1 | 3,8 | 3,8 | une ligne |
| Fonctionnement des échelons locaux | 8 | 6,1 | 9,6 | fonctions 01 et 06 du classeur des collectivités, hors communes, puis strates |
| Culture et loisirs locaux | 15 | 11,6 | 11,6 | fonction 08, puis strates |
| Départs d’agents de l’État et des agences | 64 | 2,87 | 10,26 | État : programmes non indispensables, au prorata des salaires ; agences : opérateurs supprimés, au prorata de leurs emplois |
| Départs d’agents locaux | 11 | 5,96 | 19,86 | « Rémunération des salariés » par fonction, puis strates |
| Aides à l’emploi, à l’apprentissage et à l’insertion | 5 | 8,45 | 22,55 | lignes « AE » de `Détail Economies` |
| Aides à l’investissement | 4 | 3,3 | 6,6 | lignes « E » |
| Aides locales aux entreprises | 24 | 9,7 | 12,21 | fonction 04, puis strates |
| Chèques ciblés aux particuliers | 3 | 6,9 | 17,7 | lignes « M » |
| Aide médicale de l’État | 1 | 1,1 | 1,1 | une ligne |
| Hébergement d’urgence | 1 | 2,5 | 2,5 | une ligne |
| Subventions aux autres associations | 4 | 3,2 | 3,2 | lignes « A » |
| Aide publique au développement | 1 | 1,0 | 3,0 | une ligne |
| Niches sur les revenus | 113 | 28,8 | 28,8 | 465 niches du classeur des dépenses fiscales, gage en CSG |
| Niches sur la TVA et les sociétés | 155 | 23,3 | 23,3 | idem |
| Cotisation chômage rendue en épargne | 1 | 0 | 29,6 | une ligne |
| Rendement du patrimoine restitué | 1 | 0 | 17,6 | une ligne |

**Chaque détail retombe sur le montant de son poste**, et le générateur s’arrête
sinon. Deux postes ne retombent qu’après recalage :

- **les niches** : chaque famille est ramenée à sa ligne de l’onglet `Flux`, écart
  inférieur à 3 % ;
- **les agences** : les organismes nommés gardent leur montant de régime plein
  (8,90 Md€). Le reste du poste, **0,42 Md€**, est une ligne à part, « Autres
  agences fermées : fonctionnement », du même montant aux deux horizons
  (« ligne autres », auteur, 20261112). Les organismes nommés portent seuls
  l’écart restant de première année : ils sont relevés de **1,23** (6,66 Md€ pour
  5,40 au classeur). Les salaires
  des agents des agences ne sont pas à ce poste : l’Annexe les compte à celui des
  agents.

## 5. Ce qui a été tranché en propre, poste par poste

**Rangement des lignes de l’Annexe sous les cartes de la carto.** Audiovisuel
public et fonctionnement de l’État sous Ministères ; culture locale sous Échelons
locaux ; aide médicale sous Particuliers ; hébergement d’urgence sous
Associations. La carto ne le dit pas.

**Thèmes des niches.** Quinze thèmes, sept côté revenus et huit côté TVA et
sociétés, bâtis sur les catégories du classeur. 257 niches sur 465 portent un
gage et sont cochables ; les 208 autres sont listées par thème, sans case.

**Niches communes à l’impôt sur le revenu et à l’impôt sur les sociétés.** *Validé
dans son principe* (« niches communes tombent ensemble », auteur, 20261112).
Exécution : une même case sous les deux postes, chacun en portant la moitié, ce
que fait déjà le classeur. Vingt lignes du fichier, soit dix niches chiffrées.

**Agences sans montant, par thème.** *Validé* (« 2 oui par thème », auteur,
20261112) : aucun montant n’est fabriqué au prorata pour un organisme que le
classeur ne chiffre pas. 335 organismes sont listés sans case.

**Opérateurs dont la subvention s’arrête.** Le classeur arrête la subvention de
tout un programme : des opérateurs qui deviennent autonomes, l’Opéra de Paris par
exemple, figurent donc parmi les éléments, avec leur sort entre parenthèses.

**Strates locales.** *Proposé par l’auteur* (« on a ça qu’on pourrait croiser en
proxy (thème puis strate ?) », 20261112). Le classeur des collectivités donne
l’économie par fonction, toutes collectivités confondues ; les comptes Insee 3.207
à 3.209 donnent la dépense de chaque strate par nature, non par fonction. Chaque
thème est partagé au prorata de la dépense de même nature en 2023 : consommation
intermédiaire pour le fonctionnement et la culture, rémunérations pour les
agents, subventions et transferts en capital pour les aides aux entreprises.
C’est le calcul du classeur quand il écrit « hors communes (75 %) ». **La clé est
la même pour tous les thèmes d’un poste.** *Relevé* : 17,2 Md€ aux départements,
12,9 aux régions, 23,2 aux communes. *Non vérifié sur pièce* : que le compte
« communes » de l’Insee inclue les intercommunalités.

**Programme de chaque ligne de subvention.** Le classeur ne l’écrit pas ligne par
ligne ; il a été posé ainsi, et commande le ministère : France Compétences,
emploi à domicile, aides à l’emploi et à l’apprentissage au 103 ; France Travail
et insertion au 102 ; chambres consulaires au 134 ; France 2030 au 424 ; aides au
logement au 109 ; chèque énergie au 174 ; immigration et asile au 303 ;
subventions culturelles au 131 ; politique de la ville au 147 ; aide médicale au
183 ; hébergement d’urgence au 177 ; aide au développement au 209 ; audiovisuel
public à la Culture. Les trois lignes « autres » vont à « Plusieurs ministères ».

**Ministère d’une niche** : celui de son programme de rattachement à titre
principal, que le classeur des dépenses fiscales donne pour les 465.

## 6. Les règles de présentation énoncées par l’auteur

Toutes du 20261112, sur la page.

- **Peu de corps de police** (« ne pas trop faire varier les tailles de polices,
  ça fait brouillon et surtout c’est illisible »). Tenu à quatre : 14, 17, 24 et
  48 px, ce dernier pour le seul total.
- **Toujours l’unité** (« toujours bien mettre l’unité par mois / par an »).
- **Le total d’abord, puis deux flux visibles** : salaire net en un an, épargne
  personnelle.
- **Le pourcentage ne s’isole pas** : « +13 % » se dit du salaire, non du total.
- **Pas de curseur** : une case à remplir, 2 300 suggéré.
- **Peu de lignes et d’espaces** : une ligne par poste.
- **Distinguer la fiche et la case** : la case coche et descend dans le détail,
  « Fiche » ouvre l’explication.
- **Beaucoup de données, peu de clics** : regroupements, listes à dérouler.
- **La page s’ouvre sur le régime plein.**
- **Un signalé discret de ce qu’on laisse**, en bas.

## 7. Ce qui reste fragile ou ouvert

- Le classeur a été corrigé et ajusté le 20261112 : voir le registre, « Le total porté à 236,4 ».
- Le relèvement des organismes nommés des agences la première année (§ 4).
- La clé unique par poste pour les strates (§ 5).
- Les textes de la page écrits en propre : titre, chapeau, libellés des postes,
  phrases de « En échange ».
- La page est en ligne, liée depuis aucune autre.

## 8. Comment le référentiel se rejoue

Depuis le dépôt du site, avec les modules Python `openpyxl` et `xlrd` :

```bash
python3 outils/restitution.py --tsv <dossier>
```

Le jaune des opérateurs entre par le classeur ETP, où `outils/jaune.py` porte ses
colonnes ; voir `operateurs_jaune2026_20261112_lisez_moi.md`.

---

## Annexe — `comptes_strates_locales_20261112.tsv`

Les trois tableaux Insee « Dépenses et recettes » des communes (3.207), des
départements (3.208) et des régions (3.209), comptes nationaux base 2020, de 2019
à 2024, en milliards d’euros : 48 lignes par strate, rangées en dépenses, recettes
et soldes. Les classeurs sont au dépôt du site, `site/donnees/T_3207_Communes.xlsx`,
`T_3208_Departements.xlsx` et `T_3209_Regions.xlsx`, remis par l’auteur le
20261112. Le simulateur n’en lit que quatre lignes de dépenses de 2023 :
consommation intermédiaire, rémunération des salariés, subventions, transferts en
capital à payer.
