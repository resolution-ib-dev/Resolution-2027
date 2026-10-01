# Relevé de couverture de la table de passage — 20260930

Mandat : construire la clé qui relie les lignes d'agrégat du schéma « Refonte
fiscalité », base 2024, aux 420 prélèvements du référentiel, base 2026. Le fil
construit la clé et mesure sa couverture. **Aucun sort n'est attribué.**

**Repris le 20260930** par un fil de correction : rattachement de la ligne
« dont forfaits de cotisation », qui ne recevait aucun prélèvement. Aucune autre
modification de la clé.

Pièce jumelle : `referentiels/table_passage_schema_prelevements_20260930.tsv` —
une ligne par prélèvement, la ligne du schéma qu'elle rejoint, et l'étape qui l'a
attrapée.

## Mesure d'ouverture

| grandeur | mesuré |
|---|---|
| prélèvements au référentiel | 420 |
| prélèvements sans montant publié | 188 |
| rendement total connu 2026 | 876,7 Md€ |
| lignes d'agrégat du schéma, sous-lignes comprises | 24 |
| total du schéma, base 2024 | 624,9 Md€ |
| sous-assiette « Épargne salariale et actionnariat » | 2 prélèvements, 8 359,3 M€ |

Les totaux du référentiel se retrouvent à l'octet. Le fil procède.

## La lecture des sous-lignes, déclarée

Les treize sous-lignes du schéma sont lues **comme des lignes d'agrégat à part
entière** : énergie, alcool-tabac-jeux, assurances, redevances sur l'eau,
services de transports, véhicules, numérique et spectacles, autres taxes sur les
produits, taxe de séjour, taxe pollution, outre-mer, forfaits de cotisation, et
les deux branches des droits de mutation. Un prélèvement rejoint la sous-ligne,
jamais la ligne mère, quand une sous-ligne le reçoit.

**L'absence de valeur dans la colonne « Taxes à supprimer » vaut maintien.**
Quatre sous-lignes sont dans ce cas — assurances 19,2, taxe de séjour 1,1,
outre-mer 1,6, forfaits de cotisation 8,8. Cette lecture est déclarée ici ; elle
n'est pas appliquée : aucun prélèvement ne reçoit de sort de ce fil.

## Un rattachement qui traverse la frontière d'assiette

**« Dont forfaits de cotisation », 8,8 Md€, reçoit les deux prélèvements de la
sous-assiette « Épargne salariale et actionnariat » du référentiel** — le forfait
social, 6 690,2 M€, et les contributions patronales et salariales sur les
attributions d'options de souscription ou d'achat des actions et sur les
attributions gratuites, 1 669,1 M€. Ensemble, **8 359,3 M€ en 2026**, contre
**8,8 Md€ en 2024** au schéma. L'écart est de millésime.

**Ce rattachement traverse une frontière d'assiette, et c'est délibéré.** Le
schéma lit ces deux prélèvements **par leur fonction** : des substituts de
cotisation, assis sur des rémunérations qui échappent à la cotisation, et rangés
à ce titre parmi les prélèvements sur la main-d'œuvre. Le référentiel les classe
**par leur assiette juridique** : ce sont des contributions sociales sur les
revenus, assiette 2, qui est hors du périmètre du schéma. Les deux lectures sont
justes chacune dans son ordre ; la clé suit celle du schéma, parce que c'est le
schéma qu'elle sert.

C'est la seule affectation de la table qui franchisse la frontière d'assiette.
Elle est déclarée ici, portée en colonne `etape` de la table, et elle ne vaut
pas précédent : les 81 autres prélèvements des assiettes 1 et 2 restent hors
périmètre.

**Un signalement, qui n'est pas tranché ici.** La ventilation 2024 du
recensement coupe l'agrégat INSEE D291 en forfait social 6,30 + solidarité
autonomie 2,47 + stock-options 1,03. Les deux prélèvements rattachés pèsent donc
**7,33 Md€ en 2024**, non 8,8 ; tandis que forfait social + contribution
solidarité autonomie feraient **8,77**. La coïncidence arithmétique est relevée,
elle n'emporte rien : le mandat nomme les deux prélèvements de l'épargne
salariale, et c'est ce rattachement qui est porté. Le sort de la contribution
solidarité autonomie reste entier.

## L'ordre d'appariement, et le taux obtenu à chaque étape

Trois étapes, dans cet ordre, et une seule affectation par prélèvement. Contrôle
mécanique : 420 lignes à la table, 420 libellés distincts, zéro double
affectation.

| étape | prélèvements | part des 420 | part du périmètre du schéma |
|---|---|---|---|
| 0 — hors périmètre du schéma | 100 | 23,8 % | — |
| 1 — appariement par libellé | 43 | 10,2 % | 13,4 % |
| 2 — appariement par ligne d'agrégat | 236 | 56,2 % | 87,2 % cumulé |
| 3 — non atteint, compté et nommé | 41 | 9,8 % | 12,8 % |

**Périmètre du schéma : 320 prélèvements. Couverture après libellé, 13,4 % ;
après ligne d'agrégat, 87,2 %. Rien n'a été comblé par déduction.**

L'étape 1 vaut par ce qu'elle rattrape que l'étape 2 manquerait : les deux
prélèvements de l'épargne salariale, qu'aucune règle d'assiette n'amènerait au
schéma ; la redevance des agences de l'eau, 2 485,7 M€, classée au référentiel en
« Transport, véhicules et déplacements » et qui rejoint « dont redevances sur
l'eau » ; la taxe additionnelle à la taxe de séjour des Bouches-du-Rhône, du Var
et des Alpes-Maritimes, classée au même endroit et qui rejoint « dont taxe de
séjour » ; la taxe générale sur les activités polluantes et les taxes annuelles
sur les véhicules de tourisme, classées à l'activité des entreprises et qui
rejoignent « dont taxe pollution » et « dont véhicules ».

## Normalisation des codes de siège

| grandeur | mesuré |
|---|---|
| codes de siège bruts au référentiel | 17 |
| codes après normalisation | 16 |
| variante résolue | `cgct` → `code général des collectivités territoriales`, 3 lignes |
| prélèvements portant un code normalisé | 315 / 420 |
| **taux d'appariement du siège** | **75,0 %** |

105 prélèvements ne portent aucun code — siège non établi. 294 portent en outre
un identifiant LEGIARTI daté. Le croisement n'est pas muet : le taux est rendu,
et le siège n'entre pas dans la clé, qui apparie par assiette et par libellé.

## La clé — ce que chaque ligne du schéma reçoit

Colonne 2024 : le schéma, en Md€. Colonnes suivantes : ce que la clé y verse,
en prélèvements du référentiel et en rendement 2026 connu. **Les deux colonnes
de montant ne se comparent pas terme à terme** — bases, millésimes et
conventions diffèrent ; le passage est écrit à la section suivante.

| ligne du schéma | 2024 Md€ | prélèvements | dont chiffrés | rendement 2026 Md€ |
|---|---|---|---|---|
| TVA | 206,3 | 1 | 1 | 242,8 |
| **Taxes sur la consommation\*** | **105,1** | **113** | **90** | **84,1** |
| dont énergie\* | 43,7 | 10 | 8 | 20,6 |
| dont alcool, tabac, jeux | 25,6 | 22 | 17 | 22,9 |
| dont assurances | 19,2 | 8 | 4 | 13,5 |
| dont redevances sur l'eau | 2,2 | 3 | 3 | 2,7 |
| dont services de transports | 1,9 | 12 | 11 | 3,6 |
| dont véhicules | 3,1 | 9 | 6 | 3,9 |
| dont numérique, spectacles | 1,8 | 18 | 15 | 1,9 |
| dont autres taxes sur les produits | 4,5 | 18 | 18 | 10,6 |
| dont taxe de séjour | 1,1 | 8 | 5 | 1,3 |
| dont taxe pollution | 1,0 | 2 | 2 | 1,4 |
| dont outre-mer | 1,6 | 3 | 1 | 1,7 |
| **Taxes sur la main d'œuvre** | **58,0** | **32** | **26** | **50,1** |
| dont forfaits de cotisation | 8,8 | 2 | 2 | 8,4 |
| IR net | 87,3 | 12 | 7 | 142,8 |
| IS net | 57,4 | 1 | 1 | 84,7 |
| Taxes sur chiffre d'affaires et bénéfices | 10,3 | 15 | 10 | 13,6 |
| Taxe foncière | 42,9 | 19 | 10 | 11,6 |
| Autres taxes sur les ménages | 6,5 | 27 | 19 | 8,2 |
| Autres taxes sur les entreprises | 13,2 | 45 | 26 | 7,3 |
| **Droits de mutation** | **37,9** | **14** | **10** | **41,2** |
| à titre onéreux | 17,1 | 7 | 7 | 19,3 |
| à titre gratuit | 20,8 | 2 | 2 | 21,4 |

**Les 24 lignes d'agrégat du schéma reçoivent désormais toutes au moins un
prélèvement.** Le rattachement de l'épargne salariale a fermé le seul trou du
côté du schéma.

Les quatre impôts que le schéma conserve sont chacun un prélèvement unique et
nommé au référentiel : TVA nette, Impôt net sur le revenu, Impôt sur les
sociétés, Taxe foncière sur les propriétés bâties — les quatre seuls portant le
rang `grand`. L'appariement par libellé les attrape tous les quatre.

## Le passage des bases — deux temps séparés

### Temps 1 — le périmètre, à millésime constant (2026)

| étape | Md€ 2026 | prélèvements |
|---|---|---|
| rendement recensé, périmètre de publication | **876,7** | 420 |
| − assiette 1, cotisations sociales | −2,2 | 83 |
| − assiette 2, hors les deux rattachés | −184,0 | 14 |
| − assiette 8, hors champ | −1,7 | 3 |
| = périmètre du schéma | **688,9** | 320 |
| − prélèvements sans ligne au schéma | −2,3 | 41 |
| = **ce que la clé atteint** | **686,5** | 279 |

Le schéma ne couvre ni les cotisations sociales ni, à deux prélèvements près, les
contributions sociales sur les revenus : son total de 624,9 Md€ est un
sous-ensemble des 1 251,8 Md€ de prélèvements obligatoires qu'il porte lui-même
en tête. C'est la première cause de l'écart, et la plus lourde en nombre — 100
prélèvements — mais non en euros, puisque 78 des 83 cotisations ne portent aucun
montant publié.

### Temps 2 — le millésime, à périmètre constant

Périmètre constant : les assiettes 3 à 7, plus les deux prélèvements rattachés.

| étape | Md€ |
|---|---|
| rendement 2026, montants bruts d'état A et d'annexe 2 | **688,9** |
| masse réelle 2024, comptes nationaux nets — 630,4 + 7,3 | **637,7** |
| **écart de millésime et de convention** | **−51,2** |

Deux causes nommées, et **elles ne se séparent pas sur les pièces disponibles** :
l'exercice — 2026 contre 2024 — et la convention — les montants d'état A sont
bruts, les comptes nationaux sont nets des remboursements et des crédits
d'impôt, que le recensement chiffre à 141,3 et 19,5 Md€ sur l'ensemble du champ.
Aucune ventilation par assiette de ces deux grandeurs n'existe au corpus ; le
partage n'est pas écrit ici, il est déclaré non mesurable.

### Le résidu — l'écart réel

| | Md€ 2024 |
|---|---|
| recensement, périmètre de la clé | 637,7 |
| schéma, total | 624,9 |
| **écart réel** | **+12,8** |

À millésime constant et à périmètre constant, le périmètre de recensement pèse
12,8 Md€ de plus que le périmètre de doctrine. **Le rattachement a élargi ce
résidu de 5,5 à 12,8**, parce qu'il verse 7,3 Md€ de masse 2024 du côté du
recensement sans rien ajouter du côté du schéma, où les 8,8 étaient déjà comptés
dans les 624,9. La correction n'a pas dégradé la mesure : elle a rendu visible
une matière que le périmètre de recensement portait déjà et que la clé
n'atteignait pas.

Sur la ligne concernée, le rapprochement s'améliore franchement : « Taxes sur la
main d'œuvre » vaut 58,0 au schéma contre 46,8 au recensement avant
rattachement — 11,2 d'écart — et 54,1 après — **3,9 d'écart**.

Le solde des 12,8 n'est pas rendu au prélèvement : il exigerait une masse réelle
2024 ligne à ligne, que nulle pièce ne porte. Sa composante nommée est
l'ensemble des 41 prélèvements ci-dessous.

## La concordance du solde à compenser — constatée

Le schéma porte, ligne 13 de l'onglet `Refonte fiscalité`, un solde à compenser
de **−67,75 Md€** et des hausses d'équilibre de **+67,75 Md€**, sous l'identité
`H = −T − G − S` que l'onglet écrit lui-même en `K9`. Le circuit B de
`livrables/mecanique_gages_restitutions_20260929.md` porte les mêmes grandeurs :
137,05 de taxes supprimées, moins 40,1 de gisement et 29,2 de solde brut, égale
67,75, décomposé en 25,69 par 27 points d'impôt sur les sociétés et 42,06 par la
taxe foncière.

**Les deux concordent. Aucun écart à signaler.** Le fil constate ; il ne
recalcule pas.

## Ce que la clé n'atteint pas — 41 prélèvements nommés

**Ce n'est pas un défaut d'appariement.** Les 41 forment **une catégorie entière
sans réceptacle au schéma** : tous relèvent de l'assiette 7 et tous portent un
motif de contrepartie invoquée — 28 redevances pour service rendu, 5 redevances
domaniales, 4 redevances de contrôle, 2 redevances domaniales sur le spectre,
1 redevance sur produits de santé, 1 rémunération pour service rendu. Le schéma
ne porte aucune ligne pour la contrepartie invoquée. Aucune règle d'appariement,
si fine soit-elle, ne les rattacherait : il n'y a rien à quoi les rattacher.

**Leur sort est un arbitrage de l'étape suivante, pas un travail de clé.** Trois
voies s'ouvrent, et aucune n'est ouverte ici : les qualifier en prélèvement forcé
et leur créer une ligne au schéma ; les tenir pour des contreparties réelles et
les sortir du champ des prélèvements obligatoires ; les traiter au cas par cas
selon que la contrepartie est effective. Ce fil les compte, les nomme et s'arrête.

Rendement 2026 connu de l'ensemble : **2,3 Md€**. 21 des 41 ne portent aucun
montant publié et ne sont comptés qu'en nombre.

**Domaine public, spectre et concessions — 9, dont 849,8 M€ chiffrés.**
Rémunération pour services rendus au comité professionnel des stocks stratégiques
pétroliers 591,0 · Redevance hydraulique 150,8 · Redevance proportionnelle sur
l'énergie hydraulique 37,7 · Redevances UMTS 2G et 3G 35,3 · Taxes sur les
stations et liaisons radioélectriques privées 23,6 · Redevance due par les
titulaires de titres d'exploitation de mines d'hydrocarbures liquides ou gazeux
11,0 · Taxe sur l'utilisation des bandes « 700 MHz » et « 800 MHz » du spectre
radioélectrique 0,4 · Participation des concessionnaires de la liaison fixe
Trans-Manche — · Redevance proportionnelle sur le résultat normatif des
concessions hydroélectriques soumises aux « délais glissants » —

**Autres redevances et droits — 7, dont 898,7 M€ chiffrés.**
Contribution de sécurité immobilière 814,6 · Droits perçus au profit de la CNAMTS
en matière de produits de santé 72,0 · Taxe relative à la mise sur le marché des
produits phytopharmaceutiques 9,5 · Redevance pour délivrance initiale du permis
de chasse 1,1 · Redevance perçue à l'occasion de l'introduction des familles
étrangères en France 0,8 · Droit d'examen du permis de chasse 0,7 · Garantie des
matières d'or et d'argent —

**Frais de contrôle et de surveillance — 3, dont 386,5 M€ chiffrés.**
Contributions pour frais de contrôle 246,1 · Droits et contributions pour frais
de contrôle 140,4 · Contributions versées par la SNCF au titre des frais de
surveillance et de contrôle des chemins de fer —

**Actes juridiques et professions réglementées — 2, dont 186,9 M€ chiffrés.**
Redevances perçues à l'occasion des procédures et formalités en matière de
propriété industrielle ainsi que de registre du commerce et des sociétés 186,9 ·
Frais d'inscription au registre des exploitants de voitures de transport avec
chauffeur —

**Contrôles sanitaires et phytosanitaires — 15, dont 16,4 M€ chiffrés.**
Taxe liée aux dossiers de demande concernant les médicaments vétérinaires ou leur
publicité 8,2 · Taxe annuelle portant sur les autorisations de médicaments
vétérinaires et les autorisations d'établissements pharmaceutiques vétérinaires
4,4 · Redevance sur les produits biocides 3,0 · Redevance pour délivrance de
certificats sanitaires et phytosanitaires 0,8 · puis onze sans montant publié :
Redevance pour l'agrément des établissements du secteur de l'alimentation animale
· Redevance pour le contrôle vétérinaire à l'importation de produits animaux ou
d'origine animale, d'animaux vivants · Redevance pour les contrôles vétérinaires
et phytosanitaires des végétaux à l'importation · Redevance relative aux
contrôles renforcés à l'importation des denrées alimentaires d'origine non
animale · Redevance sanitaire d'abattage · Redevance sanitaire de découpage ·
Redevance sanitaire de première mise sur le marché des produits de la pêche ou de
l'aquaculture · Redevance sanitaire de transformation des produits de la pêche et
de l'aquaculture · Redevance sanitaire liée à la certification des végétaux à
l'exportation · Redevance sanitaire pour le contrôle de certaines substances et
de leurs résidus · Redevances versées pour la délivrance des certificats
d'obtention végétale

**Timbre et formalités administratives — 5, aucun chiffré.**
Redevance pour examen du code de la route · Taxe d'ouverture de caveau · Taxe sur
les demandes de visa ou de renouvellement de visa de publicité et sur les dépôts
de publicité pharmaceutiques · taxe de réduction et réunion de corps · taxe de
superposition des corps

## La règle des 188

Les 188 prélèvements sans montant publié sont comptés en nombre et jamais en
euros, à toutes les lignes de ce relevé et à toutes les colonnes de la table.
Aucune somme de ce fil ne leur attribue de valeur, fût-elle nulle.

## Sources

`referentiels/prelevements_forces_20260930.tsv` ·
`livrables/recensement_prelevements_20260930.md` ·
`Synthèse Calculs Résolution_0910.xlsx`, onglets `Refonte fiscalité`, `Flux`,
`Détail Niches` · `livrables/mecanique_gages_restitutions_20260929.md` ·
`livrables/arborescence_mesures_20260928.md`, mouvement 5 · énoncés M-028 à
M-036 du découpage.
