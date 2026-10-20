# Le portage des prélèvements — qui remet, qui supporte — 20261020

Calcul de l'auteur, colonne « Payeur » et cinq corrections du classeur
`T_3217_Impots_0902.xlsx` (tableau 3.217 de l'INSEE, édition 1995-2025), rejoué
puis corrigé par `appareil/portage_prelevements.py`. Tous les chiffres ci-dessous
en sortent, exercice 2025 sauf mention.

**La thèse.** Les entreprises remettent au fisc l'essentiel de ce que le secteur
privé paie, alors qu'elles ne sont pas des agents finaux mais des nœuds de
contrats : chaque euro qu'elles versent est pris sur un salaire, sur un prix ou
sur un revenu du capital. Le citoyen ne voit pas ce qu'il paie.

## 1. Le calcul de l'auteur, rejoué — relevé

| | y compris prélèvement à la source | hors prélèvement à la source |
|---|---|---|
| base « privée » | 1 153,2 | 1 153,2 |
| ménages | 130,7 — 11,3 % | 179,0 — 15,5 % |
| entreprises | 1 017,0 — 88,2 % | 968,7 — 84,0 % |
| non affecté | 5,5 — 0,5 % | 5,5 — 0,5 % |

Rejoué à l'identique.

## 2. Ce qui ne tient pas dans le calcul — relevé ou déduit

1. **La base retranche les crédits d'impôt** (prélèvements obligatoires INSEE,
   1 305,1), ce que l'auteur refuse par ailleurs (arbitrage du 20261020) et
   qu'Eurostat ne fait pas. Base brute : 1 383,6 − 6,7 non recouvré − 52,4
   imputées = 1 324,5.
2. **La correction « CSG/CRDS inactivité » retire 51,9 Md€**, soit 114 −
   CSG − CRDS. Elle ôte les revenus de remplacement, qui sont des flux publics,
   mais aussi la CSG du capital, payée par des privés. Et 114 vient d'une autre
   source et d'un autre exercice (PLACSS 2024) que les montants 2025. La part des
   revenus de remplacement dans CSG + CRDS vaut 17,5 % (table du fiscaliste,
   2024), soit 29,0 Md€ en 2025 *(déduit)*.
3. **« Cotisations sur la masse salariale publique : 30 + 70 »** n'a pas de
   source. Le 70 se confirme : cotisations employeurs des administrations
   publiques 122,5 (Eurostat, `gov_10a_main`, D12) − 52,4 imputées = 70,0
   *(relevé, soustraction déduite)*. Le 30 reste sans source.
4. **Les impôts sur la production payés par les administrations elles-mêmes**,
   13,9 Md€ (Eurostat, D29 versé par S13) — taxe sur les salaires des hôpitaux,
   versement mobilité des employeurs publics —, restaient comptés comme payés
   par des entreprises.
5. **Les prélèvements sur les revenus de capitaux mobiliers** (5,3) sont
   affectés aux ménages, le prélèvement de solidarité sur les mêmes revenus aux
   entreprises. Les deux sont retenus par l'établissement payeur : alignés sur
   « entreprises ».
6. **5,5 Md€ ne portent aucune étiquette** (1,5 d'impôts divers sur la
   production, 4,1 d'impôts sur le revenu non détaillés) : les parts ne somment
   pas à 100 %.
7. **Le ratio du prélèvement à la source**, 66 737 / 143 010, n'a pas de
   source.
8. **Le critère** : les droits de mutation, les cartes grises et les droits de
   succession sont affectés aux ménages, alors qu'un notaire ou un professionnel
   les remet. Le critère tenu est donc « qui voit la somme et la paie », non
   « qui remet ». Il est défendable ; il se déclare.

## 3. Le calcul corrigé — 2025

| | y compris prélèvement à la source | hors prélèvement à la source |
|---|---|---|
| base privée | 1 181,5 | 1 181,5 |
| ménages | 134,7 — 11,4 % | 183,0 — 15,5 % |
| entreprises | 1 041,3 — **88,1 %** | 993,0 — **84,0 %** |
| non affecté | 5,5 | 5,5 |

En retirant aussi la CSG-CRDS sur les traitements publics, 23,3 Md€ *(déduit des
taux légaux et des salaires publics 2024, Eurostat)*, la part tombe à 87,9 %.
Restent non mesurés, et ils la baisseraient encore un peu : le prélèvement à la
source sur traitements et pensions publics, la TVA sur les achats publics.

**Le résultat tient** : les corrections se compensent. « Près de neuf euros sur
dix » est robuste ; « neuf sur dix » exact suppose le prélèvement à la source,
dont le ratio reste à sourcer.

## 4. Ce que les entreprises remettent, qui le supporte — relevé

Fonction économique (Commission européenne, TAXUD), 2024, table du fiscaliste :
**travail 51,7 %, consommation 24,6 %, capital 23,7 %**. Stable depuis 1995
(51,0 / 27,9 / 21,1). La nomenclature européenne n'a pas de catégorie
« entreprise » : elle ne connaît que trois bases, le travail, la consommation et
le capital. Que le capital soit in fine porté par des personnes (actionnaires,
épargnants, retraités par capitalisation) est un raisonnement d'incidence,
*déduit*, et non une mesure.

Formulation proposée :

> Les entreprises remettent au fisc près de neuf euros sur dix de ce que le
> secteur privé paie. Elles n'en supportent aucun en dernier ressort : la
> moitié est prise sur le travail, un quart sur ce que vous achetez, un quart
> sur l'épargne et le capital.

## 5. L'objection qui viendra — relevé

**« Ils sont tous bénéficiaires » n'est pas ce que dit l'INSEE.** Ses comptes
nationaux distribués comptent **56 % de bénéficiaires nets en 2023** (Insee
Analyses n° 118, avril 2026 ; 57 % en 2019 et en 2022), de 99 % chez les 10 %
les plus modestes à 18 % chez les 10 % les plus aisés. **Et l'INSEE n'y tombe
pas dans l'illusion du portage** : il impute aux ménages les prélèvements remis
par les entreprises. L'argument du portage ne réfute donc pas ce chiffre. Ce qui
se discute est ailleurs : les services publics comptés à leur coût, les
retraites comptées comme transferts.

**L'opinion pense déjà l'inverse** : 58 % des Français estiment contribuer plus
qu'ils ne reçoivent (Elabe pour BFMTV, septembre 2025).

*Écarté par l'auteur le 20261020* : il conteste la construction de ces comptes
(qualité de l'argent à l'aller et au retour, volatilité des cas) et ne s'en sert
pas. L'objection reste à attendre en débat.

Le portage sert donc un autre argument, qui tient : **le prélèvement est rendu
invisible**, et ce qu'on ne voit pas ne se consent pas. « On leur a menti » ne
tient pas face à ces deux chiffres.

[interne] Pièces : `referentiels/insee_3217_payeur.tsv`,
`referentiels/insee_3217_payeur_corrections.tsv` (classeur de l'auteur, SHA-256
b66f4e45…8a8e, non versé), `referentiels/eurostat_prelevements_apu.tsv`
(extraction du 20261020), `referentiels/prelevements_7classements_1995_2024.tsv`.
Bac à sable.
