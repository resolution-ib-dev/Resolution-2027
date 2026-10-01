# Sort des prélèvements — 20260930

Mandat : corriger la table de passage en lot 0, appliquer le schéma « Refonte
fiscalité » à chacun des 420 prélèvements, écrire le passage chiffré entre les
624,9 Md€ du schéma, les 876,7 Md€ de rendement recensé et les 1 251,8 Md€ de
prélèvements obligatoires. **Classement du sort et bouclage chiffré seulement.**

Pièce jumelle : `referentiels/sort_prelevements_20260930.tsv` — une ligne par
prélèvement, son sort, l'impôt qui absorbe son assiette le cas échéant, et le
fondement du sort.

---

## Mesure d'ouverture — la table reprise se retrouve à l'octet

| grandeur | mesuré | référence |
|---|---|---|
| prélèvements | 420 | 420 |
| libellés distincts | 420 | 420 |
| prélèvements sans montant publié | 188 | 188 |
| rendement total connu 2026 | 876,749 Md€ | 876,7 Md€ |
| total des taxes à supprimer du schéma | −137,05 Md€ | −137,05 Md€ |

Le fil procède.

---

## Lot 0 — la table de passage corrigée

Défaut D-4 de `methode/fragments/arbitrages/20260930-defauts-reconciliation.md`.
**Deux lignes changent, et deux seulement.**

| prélèvement | ligne d'avant | ligne d'après | étape d'après |
|---|---|---|---|
| Contribution solidarité autonomie (CSA), 2 563,2 M€ | 0 — hors périmètre du schéma | dont forfaits de cotisation | 1 — libellé |
| Contributions patronales et salariales sur les attributions d'options et sur les attributions gratuites, 1 669,1 M€ | dont forfaits de cotisation | — | 0 — hors périmètre du schéma |

### Compteurs rejoués

| étape | avant | après |
|---|---|---|
| 0 — hors périmètre du schéma | 100 | 100 |
| 1 — appariement par libellé | 43 | 43 |
| 2 — appariement par ligne d'agrégat | 236 | 236 |
| 3 — non atteint | 41 | 41 |

Les quatre compteurs d'étape sont inchangés : la correction est un échange, une
ligne entrant là où une autre sort. **Les deux lignes qui bougent sont les
suivantes.**

| ligne du schéma | prélèvements | dont chiffrés | rendement 2026 | avant |
|---|---|---|---|---|
| dont forfaits de cotisation | 2 | 2 | 9,253 Md€ | 8,4 Md€ |
| hors périmètre et non atteints | 141 | 32 | 189,3 Md€ | 190,2 Md€ |

La correction **améliore la concordance de la ligne qu'elle sert** : « dont
forfaits de cotisation » vaut 8,8 Md€ au schéma en base 2024 ; les deux
prélèvements désormais rattachés pèsent, à la ventilation 2024 du recensement,
6,30 + 2,47 = **8,77 Md€**, contre 7,33 avant. L'écart tombe de 1,47 à 0,03 Md€.
La coïncidence arithmétique signalée au relevé de couverture est ainsi confirmée
par l'arbitrage, non par la clé.

### Ce que le lot 0 laisse dû

`referentiels/table_passage_schema_prelevements_20260930.tsv` **n'a pas été
réécrit au coffre.** La clé corrigée est appliquée à toute l'attribution et les
compteurs sont rejoués sur elle ; mais la copie de travail de ce fil ne porte
que six des huit colonnes du fichier — `schema_2024_Mdeur` est reconstituable,
`siege_code_normalise` ne l'est pas ligne à ligne. Le réécrire perdrait cette
colonne : c'est une reconstruction, pas une correction. **Le patch de deux
lignes ci-dessus part au paquet de dépôt et s'applique là où le fichier vit.**

---

## La règle de sort, arrêtée

Sept sorts, et pas d'autre. La colonne « Taxes à supprimer » du schéma commande ;
la règle de doctrine dit ce que devient l'assiette.

| sort | ce qu'il dit |
|---|---|
| `conservé` | l'un des quatre impôts de M-028 |
| `fondu` | le prélèvement disparaît, son assiette revient à un impôt conservé, qui est nommé |
| `supprimé` | le prélèvement disparaît sans report d'assiette |
| `maintenu à part` | il subsiste hors des quatre, par exception nommée de M-030 ou parce que le schéma ne le supprime pas |
| `non touché` | hors du mouvement, ne compte ni au gage ni à la restitution |
| `sortie du périmètre des PO` | il subsiste, requalifié en prix d'un service, hors prélèvements obligatoires |
| `restitué en capitalisation` | il cesse, et la somme revient au salarié sur son compte d'épargne — une restitution, non une recette perdue |

Les 83 cotisations sociales ne reçoivent aucun sort (D-3) et sont portées
`hors mandat`. Les 3 produits non fiscaux de l'assiette 8 sont portés `hors champ`.

**L'ordre d'application, et il ne se discute pas.** Le schéma fait foi au niveau
de la ligne : colonne « Taxes à supprimer » vide vaut maintien, colonne servie
vaut suppression. La doctrine dit ensuite où va l'assiette, ce qui départage
`supprimé` de `fondu`. **Le sort ne rouvre jamais l'arithmétique du schéma** :
les −137,05 Md€ restent ce que le schéma écrit, qu'un prélèvement soit supprimé
ou fondu.

---

## Le dénombrement

| sort | prélèvements | dont chiffrés | rendement 2026 Md€ |
|---|---|---|---|
| `conservé` | 4 | 3 | 457,711 |
| `fondu` | 64 | 39 | 79,310 |
| `supprimé` | 179 | 132 | 252,916 |
| `maintenu à part` | 50 | 34 | 64,188 |
| `sortie du périmètre des PO` | 25 | 14 | 0,470 |
| `non touché` | 11 | 2 | 16,612 |
| `restitué en capitalisation` | 1 | 1 | 1,669 |
| `hors mandat` | 83 | 5 | 2,213 |
| `hors champ` | 3 | 2 | 1,661 |
| **total** | **420** | **232** | **876,749** |

**Aucun prélèvement n'est resté sans sort.**

### Les quatre conservés

TVA nette 242,838 · Impôt net sur le revenu 130,178 · Impôt sur les sociétés
84,694 · Taxe foncière sur les propriétés bâties, sans montant publié.

### Ce que chaque impôt conservé absorbe

| impôt absorbant | prélèvements | dont chiffrés | rendement 2026 Md€ | fondement |
|---|---|---|---|---|
| impôt sur le revenu | 25 | 16 | 53,816 | M-034 pour les plus-values, M-033 pour les mutations, M-028 pour le reste de l'assiette de revenu |
| impôt sur les sociétés | 7 | 6 | 11,937 | M-028 — assiette de bénéfice |
| taxe foncière | 32 | 17 | 13,557 | M-035 — contributions locales unifiées, y compris les 14 « Locaux d'activité » par décision de l'auteure du 20260930 |
| taxe sur la valeur ajoutée | 0 | 0 | 0,000 | — |

**Aucun prélèvement ne se fond dans la TVA, et c'est un résultat, non un trou.**
Les taxes spécifiques sur les produits et les services que le schéma supprime ne
transfèrent pas leur assiette : celle-ci est déjà dans le champ de la TVA. Elles
sont supprimées, pas fondues.

### Les maintenus à part

| ligne du schéma | prélèvements | rendement 2026 Md€ | motif |
|---|---|---|---|
| alcool, tabac, jeux | 22 | 22,897 | M-030 — produits à effets négatifs et à dépendance forte |
| dont énergie* | 7 | 15,399 | M-030 — énergies fossiles |
| assurances | 8 | 13,548 | schéma — colonne vide |
| forfaits de cotisation | 2 | 9,253 | schéma — colonne vide |
| outre-mer | 3 | 1,744 | schéma — colonne vide |
| taxe de séjour | 8 | 1,346 | schéma — colonne vide |

---

## Les points de contact, traités

### Énergie — le partage des 8 Md€ n'est pas réconcilié, et se déclare

M-030 conserve les taxes sur les produits à effets négatifs et à dépendance
forte, « notamment les énergies fossiles ». L'électricité n'en est pas. Le
partage porté au prélèvement est donc :

- **maintenues à part, 7 prélèvements, 15,399 Md€ 2026** — accises sur les
  gazoles et les essences en métropole, part régionale et fractions
  décentralisées, accise sur les carburants, accise métropole hors charbons gaz
  et électricité, accise carburants outre-mer, TIRUERT, TICPE part Grenelle ;
- **supprimées, 3 prélèvements, 5,153 Md€ 2026** — accise perçue sur
  l'électricité, parts communes et EPCI, parts départements et métropole de Lyon,
  et composante modulée sur la péréquation tarifaire.

**Le schéma supprime 8 Md€ en base 2024 ; la règle de doctrine en atteint 5,153
en base 2026. L'écart de 2,85 n'est pas rendu au prélèvement, et il ne se comble
pas.** Trois causes se nomment sans se partager : le millésime ; la note du
schéma lui-même, qui déclare la ligne « corrigée du bouclier tarifaire
électricité », donc portée à un tarif que le rendement 2026 ne porte pas ; et la
troisième ligne supprimée, dont l'assiette mêle l'électricité et les combustibles
de chauffage, qui sont fossiles. Aucune pièce du corpus ne permet de séparer les
trois.

### Alcool, tabac, jeux — les 0,3 Md€ supprimés restent sans porteur

Le schéma maintient 25,3 des 25,6 Md€ de la ligne et en supprime 0,3, sans
nommer quoi. **Le seul prélèvement de la ligne dont le rendement approche ce
montant est le droit de licence sur la rémunération des débitants de tabacs,
330,5 M€ — et D-2 le porte expressément maintenu.** Les 22 prélèvements de la
ligne sont donc tous maintenus à part, et les 0,3 Md€ sont déclarés sans porteur.
Ils ne se comblent pas par déduction.

### Assurances, taxe de séjour, outre-mer, forfaits de cotisation

Les quatre sous-lignes dont la colonne « Taxes à supprimer » est vide sont
maintenues, soit 21 prélèvements et 25,891 Md€ 2026.

### Droits de mutation

14 prélèvements, `fondu — impôt sur le revenu`, fondement M-033 : les droits
disparaissent et la franchise de 3 % sur la valeur vénale est déductible de
l'imposition de la plus-value ultérieure, que M-034 loge dans l'impôt sur le
revenu. Le schéma écrit lui-même l'arbitrage en `H43` : `max (3%val>100k€ ; IR PV)`.
Les suppressions partielles du schéma — 12,05 sur 17,1 à titre onéreux, 20,4 sur
20,8 à titre gratuit — sont un solde de rendement attendu de la franchise, non un
partage entre prélèvements maintenus et supprimés : **aucun droit de mutation
n'est maintenu.**

### Chiffre d'affaires et bénéfices

Le schéma supprime la ligne entière, −10,3 Md€. La doctrine partage l'assiette :

- **7 prélèvements assis sur le bénéfice** — C3S, contribution exceptionnelle,
  contribution sociale nette, taxation minimale des multinationales, contribution
  de la Caisse des dépôts, taxe sur les rachats d'actions, taxe sur les excédents
  de provisions — `fondu — impôt sur les sociétés`, 11,937 Md€ ;
- **8 prélèvements assis sur le chiffre d'affaires ou les dépenses** —
  contributions pharmaceutiques, TEITLD, taxe sur le chiffre d'affaires des
  exploitants agricoles — `supprimé`, M-031, impôts de production, 1,678 Md€.

La compensation passe par le taux de l'impôt sur les sociétés, que le schéma
porte en hausse d'équilibre de 25,69 Md€ (`K34`, « 27pt IS »), non par un report
d'assiette : le sort `fondu` qualifie la destination de l'assiette, il ne
reconstitue pas le rendement.

---

## L'audit des prélèvements à contrepartie invoquée — 41 lignes, une par une

Arbitrage de l'auteure du 20260930 : par défaut supprimer et fondre ; sortie du
périmètre des prélèvements obligatoires en repli, lorsque la suppression ne vole
pas ; le repli jamais par défaut ni par commodité ; sous le milliard, le principe
prime et le montant est secondaire. D-2 ramène dans le lot les huit que le texte
financier touche : **le lot est de 41, et non de 33.**

**Le critère du repli, arrêté et appliqué ligne à ligne : le fait générateur est
un acte demandé par le redevable à son seul bénéfice, et le tarif rémunère cet
acte.** À défaut — police administrative, bien public, ou assiette proportionnelle
à la valeur et non au coût du service — la suppression vole, et le prélèvement
est supprimé, le service passant au financement par le budget général.

| verdict | prélèvements | dont chiffrés | rendement 2026 |
|---|---|---|---|
| supprimé et fondu | 16 | 6 | 1,869 Md€ |
| sortie du périmètre des PO | 25 | 14 | 0,470 Md€ |
| **total** | **41** | **20** | **2,338 Md€** |

**Le principe l'emporte en euros comme en nombre** : le repli porte 20 % du
rendement du lot. Il n'a pas été pris par commodité.

### Les quatre points saillants du lot

1. **Contribution de sécurité immobilière, 814,6 M€ — supprimée et fondue.**
   C'est la plus lourde du lot. Son assiette est proportionnelle à la valeur de
   l'acte, non au coût du service de publicité foncière : c'est un droit
   d'enregistrement sous un autre nom, et le repli y serait un repli de
   commodité.
2. **Rémunération pour services rendus au comité professionnel des stocks
   stratégiques pétroliers, 591,0 M€ — supprimée et fondue.** Le stock
   stratégique est un bien public ; la contrepartie n'est individualisable pour
   aucun redevable.
3. **Frais de contrôle de l'ACPR et de l'AMF, 386,5 M€ — supprimés et fondus.**
   Le contrôle est une police administrative imposée, non un service demandé.
4. **Redevances domaniales et de spectre, 7 lignes, 258,8 M€ — sorties du
   périmètre.** L'occupation privative du domaine public se loue ; le tarif est
   un loyer, et il n'a jamais eu à être un prélèvement obligatoire.

Les 15 contrôles sanitaires et phytosanitaires se partagent : **6 sortis du
périmètre** — certificats sanitaires et phytosanitaires à l'exportation,
certification des végétaux à l'exportation, agrément des établissements de
l'alimentation animale, certificats d'obtention végétale, produits biocides,
dossiers de médicaments vétérinaires, tous délivrés sur demande de l'opérateur —
et **9 supprimés**, tous les contrôles imposés à l'importation, à l'abattage, au
découpage et aux résidus, ainsi que la taxe annuelle sur les autorisations de
médicaments vétérinaires, qui ne rémunère aucun acte.

Les 5 taxes de timbre et de formalités du lot et les 2 lignes d'actes juridiques
sortent du périmètre : examen du code de la route, ouverture de caveau,
réduction et réunion de corps, superposition de corps, visa de publicité
pharmaceutique, inscription au registre des exploitants de VTC, redevances de
l'INPI.

---

## Le bouclage — trois grandeurs, quatre lignes de solde

### Ligne 1 — des prélèvements obligatoires au périmètre du schéma, base 2024

| | Md€ 2024 | prélèvements |
|---|---|---|
| prélèvements obligatoires 2024 | **1 251,8** | — |
| − cotisations sociales et contributions sociales sur les revenus, hors les deux rattachés | −626,9 | 97 |
| = total du schéma | **624,9** | 320 |

**Cette ligne se rend par différence, et se déclare comme telle.** Aucune pièce
du corpus ne porte la masse 2024 des assiettes 1 et 2 : le résidu de 626,9 Md€
est un écart, non une mesure. Un résidu n'est pas une source.

**La valeur retenue est celle de l'Insee, décidée par l'auteure le 20260930** :
`Synthèse Calculs Résolution_0910.xlsx`, onglet `Refonte fiscalité`, cellule
`F3` — 2 919,9 Md€ de PIB à 42,871 % de taux de prélèvements obligatoires, source
Insee citée en `B8`. Les 1 250,76 Md€ qui circulaient par ailleurs sont écartés ;
l'écart de 1,04 Md€ est clos.

### Ligne 2 — du rendement recensé au périmètre du schéma, millésime constant 2026

| | Md€ 2026 | prélèvements |
|---|---|---|
| rendement recensé, périmètre de publication | **876,749** | 420 |
| − assiette 1, cotisations sociales | −2,213 | 83 |
| − assiette 2, hors les deux rattachés | −183,099 | 14 |
| − assiette 8, hors champ | −1,661 | 3 |
| = périmètre du schéma | **689,776** | 320 |
| − non atteints par la clé | −2,338 | 41 |
| = atteint par la clé | **687,438** | 279 |

### Ligne 3 — du millésime 2026 au millésime 2024, périmètre constant

| | Md€ |
|---|---|
| périmètre du schéma, base 2026, montants bruts d'état A et d'annexe 2 | **689,776** |
| masse réelle 2024, comptes nationaux nets — 630,4 + 8,77 | **639,17** |
| **écart de millésime et de convention** | **−50,61** |

Deux causes nommées et non séparables sur les pièces disponibles : l'exercice,
2026 contre 2024 ; et la convention, les montants d'état A étant bruts quand les
comptes nationaux sont nets des remboursements et des crédits d'impôt, que le
recensement chiffre à 141,3 et 19,5 Md€ sur l'ensemble du champ. Aucune
ventilation par assiette n'existe au corpus. **Le partage est déclaré non
mesurable.**

### Ligne 4 — le résidu réel

| | Md€ 2024 |
|---|---|
| recensement, périmètre de la clé | 639,17 |
| schéma, total | 624,9 |
| **résidu** | **+14,27** |

À millésime et à périmètre constants, le périmètre de recensement pèse 14,27 Md€
de plus que le périmètre de doctrine. Le lot 0 a **élargi ce résidu de 12,8 à
14,27**, parce qu'il verse 2,47 Md€ de masse 2024 du côté du recensement là où il
en retire 1,03, sans rien changer du côté du schéma, où les 8,8 étaient déjà
comptés. La correction n'a pas dégradé la mesure : elle a rendu visible une
matière que le périmètre de recensement portait déjà.

Sa composante nommée est l'ensemble des 41 prélèvements à contrepartie invoquée,
2,338 Md€ en base 2026. Le reste exigerait une masse réelle 2024 ligne à ligne,
que nulle pièce ne porte.

### La règle des 188, tenue

Les 188 prélèvements sans montant publié sont comptés en nombre et jamais en
euros, à toutes les lignes de ce relevé et à toutes les colonnes de la table.
Aucune somme n'en porte une valeur, fût-elle nulle.

---

## Les décisions de l'auteure du 20260930, appliquées

**Les 14 prélèvements « Locaux d'activité » de la ligne « Autres taxes sur les
entreprises » — CFE, taxes additionnelles pour frais de chambres de commerce et
de métiers, taxe sur les bureaux d'Île-de-France, TASCOM, surfaces de
stationnement, friches commerciales, 1,915 Md€ — sont supprimés et leur rendement
repris par la taxe foncière unique.** Le sort porté est `fondu — taxe foncière` :
c'est le terme qui dit exactement cela, la disparition du prélèvement et le
report de son assiette sur un impôt conservé. Le schéma et M-035 sont tenus
ensemble, et non l'un contre l'autre. L'arithmétique du schéma n'est pas rouverte :
les −13,5 Md€ de la ligne restent ce que le schéma écrit.

**Les prélèvements obligatoires 2024 valent 1 251,8 Md€**, chiffre Insee porté par
le classeur. Voir la ligne 1 du bouclage.

**Les quatre sous-lignes sans valeur en colonne « Taxes à supprimer » sont
maintenues à dessein** — assurances 19,2, forfaits de cotisation 8,8, outre-mer
1,6, taxe de séjour 1,1, soit 21 prélèvements et 25,891 Md€ en base 2026. La
lecture « colonne vide vaut maintien » est confirmée ; la contradiction apparente
avec M-030 est close.

---

## Ce que ce fil n'a pas fait

**Aucune adresse n'a été écrite.** 105 prélèvements du référentiel ne portent
aucun siège. Le relevé de siège reste un chantier distinct, dû avant la phase 3,
sur les prélèvements sans siège qui reçoivent un sort autre que `non touché` ou
`hors mandat`. Ce fil constate le trou et le compte ; il ne le comble pas.

`disposition-cible`, `redaction-legistique` et `expose-sommaire` n'ont pas été
activées. Ce fil est au projet doctrine : il classe et il boucle.

---

## Ce qui reste ouvert

1. **Les contributions patronales et salariales sur les attributions d'options et
   d'actions gratuites, 1 669,1 M€ — défaut orienté, à confirmer.** Trois mesures,
   et elles ne donnaient pas le sort.
   - **Le CGI réécrit par l'expert supprime les deux articles qui portent
     l'imposition de l'avantage** — `80 bis`, options de souscription et d'achat,
     et `80 quaterdecies`, attributions gratuites, tous deux à zéro caractère à
     `referentiels/cgi_expert_articles.tsv` — et retire le taux dérogatoire de
     l'avantage salarial à l'article `200 A` ainsi que le renvoi à `80 bis` dans
     le prix d'acquisition de l'article `150-0 D`. **L'avantage retombe au droit
     commun du revenu, au taux unique de M-036.** C'est le nettoyage d'assiette,
     et il est déjà écrit.
   - **Mais l'expert ne dit rien des contributions elles-mêmes** : leur siège est
     aux articles `L. 137-13` et `L. 137-14` du code de la sécurité sociale, hors
     des cinq pièces. C'est le cas général du § 8 du relevé de couverture du
     20260929 : vidé au code général des impôts, intact à son siège.
   - **Le tableau de synthèse de l'annexe ne dit rien non plus.** L'onglet
     `Annexe Manuscrit` du classeur est le tableau des économies, 236,05 Md€ ;
     **aucune de ses 26 lignes ne porte l'épargne salariale, les stock-options ni
     les attributions gratuites.**
   - **Et l'arbitrage du 20260930 sur la ligne « dont forfaits de cotisation » a
     déjà tranché le rattachement, contre le rattachement par la fonction** : les
     stock-options restent hors du périmètre du schéma, sur deux motifs, l'un
     arithmétique — 8,77 contre 7,33 — l'autre d'assiette. **Les laisser avec le
     forfait social rouvrirait cet arbitrage.** Le fil ne le rouvre pas.

   **Le défaut appliqué, sur direction de l'auteure du 20261001, et révocable en
   une ligne. Les deux jambes se séparent.**

   - **La jambe du code général des impôts est supprimée avec les niches.**
     L'avantage retourne à l'assiette de l'impôt sur le revenu ; son flux est celui
     des niches d'impôt sur le revenu, ligne « IR net » du schéma, 27 Md€ de niches
     restituées. *La ligne exacte de l'annexe 3 qui la porte n'est pas mesurée.*
   - **La jambe du code de la sécurité sociale est restituée en capitalisation, et
     ultérieurement seulement.** Elle rejoint le circuit A à la colonne
     « au-delà », jamais l'année 1 — parallèle exact avec l'assurance chômage
     transformée en épargne, que `livrables/mecanique_gages_restitutions_20260929.md`
     porte déjà à 30 Md€ en « au-delà » et à zéro en année 1.
   - **Le circuit B n'est pas rouvert.** Les 67,75 Md€ de hausses d'équilibre
     restent intacts, et c'est la raison même du choix : la contrepartie du
     circuit B ne se rouvre pas mesure par mesure.

   **Ce qui reste à confirmer** : le principe de la restitution en capitalisation,
   et sa conséquence sur le **forfait social, 6 690,2 M€**, maintenu à part le
   20260930 et que le même raisonnement atteindrait — il frappe la même épargne
   salariale.
2. **Les 0,3 Md€ supprimés de la ligne alcool, tabac, jeux**, sans porteur nommé.
3. **Les 2,85 Md€ d'écart sur le partage de la ligne énergie**, non séparables.
4. **Le patch de deux lignes de la table de passage**, dû au dépôt.

## La règle des affectataires

Aucune colonne de ce relevé ne suit l'affectataire d'un prélèvement supprimé,
fondu ou restitué. **Un flux entre administrations publiques est neutre**, et le
traiter ligne à ligne ferait apparaître un coût là où il n'y en a pas. Les
affectataires se reprennent facialement en aval, une fois les sorts arrêtés.
*Décision de l'auteure du 20261001.*

## Sources

`referentiels/prelevements_forces_20260930.tsv` ·
`referentiels/table_passage_schema_prelevements_20260930.tsv` ·
`livrables/couverture_table_de_passage_20260930.md` ·
`livrables/recensement_prelevements_20260930.md` ·
`Synthèse Calculs Résolution_0910.xlsx`, onglet `Refonte fiscalité` ·
`livrables/paquet_machine.md`, énoncés M-025 et M-028 à M-036 ·
`methode/fragments/arbitrages/20260930-defauts-reconciliation.md` ·
`methode/fragments/arbitrages/20260930-perimetre-fiscal.md` ·
`livrables/mecanique_gages_restitutions_20260929.md`

---

## Les contrôles, joués sur la pièce produite

Contrôle mécanique rejoué sur l'onglet `Réforme` du classeur, non sur les
chiffres de ce relevé.

| contrôle | mesuré |
|---|---|
| C1 — nombre de lignes | 420 |
| C2 — libellés distincts | 420 |
| C3 — aucun sort vide | 0 vide |
| C4 — vocabulaire des sorts clos à neuf termes | clos |
| C5 — impôt absorbant renseigné si et seulement si le sort est `fondu` | vérifié sur 420 |
| C6 — rendement total | 876,749 Md€ |
| C7 — prélèvements sans montant publié | 188 |
| C8 — les 83 cotisations toutes `hors mandat` | 83 / 83 |
| C9 — l'assiette 8 toute `hors champ` | 3 / 3 |
| C10 — les quatre `conservé` sont les quatre impôts de M-028 | vérifié |
| C11 — synthèse recomptée depuis l'onglet, non recopiée | 9 lignes concordantes |
| C12 — bouclage ligne 2, somme des retraits | 689,776 |
| C13 — le lot des 41 ne porte que deux verdicts | vérifié |
| C14 — les 14 « Locaux d'activité » fondus dans la taxe foncière | 14 lignes, 1,915 Md€ |
| C15 — bouclage ligne 1 | 1 251,8 − 626,9 = 624,9 |
| C16 — aucun prélèvement sans sort | 0 `en attente` |
| C17 — restitué en capitalisation | 1 ligne, 1 669,1 M€ |

**Jeu de fautes — six fautes injectées, six levées.** Sort vidé ; sort hors
vocabulaire ; impôt absorbant porté sur un prélèvement supprimé ; cotisation
sociale dotée d'un sort ; montant altéré d'une ligne ; ligne dupliquée.

**Jeu de justes — quatre cas qui ont le droit de passer, et qui passent.**
4 prélèvements chiffrés à zéro, conservés comme tels et non confondus avec un
montant absent · 110 prélèvements sans montant publié recevant un sort sans
recevoir d'euro · 10 libellés portant des guillemets internes, intacts après
écriture · un seul prélèvement `en attente`, nommé.

**Aucune faute.**
