# Hypothèses dimensionnantes du rapport HCSP « France 2035-2050 » : test de robustesse

**Méthode**
- J'ai relevé chaque hypothèse dont dépendent les chiffrages ou les propositions du rapport.
- Je l'ai confrontée aux données observées et aux précédents, puis j'ai indiqué le sens du biais.
- J'ai chiffré la sensibilité de la dette avec une dynamique simplifiée, calée sur le scénario central HCSP-OFCE. Elle redonne 141 % en 2035 et 195 % en 2050, contre 140 % et 188 % dans le rapport.
- C'est un ordre de grandeur, pas le modèle de l'OFCE. Le calcul est dans /tmp/claude-0/-home-user/c7c4a21e-ca69-5935-a5ed-f1090c49f6c9/scratchpad/calc/dette.py.

## 1. Hypothèses macroéconomiques des projections

| Hypothèse | Valeur retenue | Test : données et précédents | Sens du biais |
|---|---|---|---|
| Productivité du travail | +0,7 %/an jusqu'en 2050 | Le tableau 2 du rapport donne lui-même **+0,5 %/an observé sur 2005-2025**. Le COR retenait 1,0 à 1,8 % dans les années 2010, puis 0,7 à 1,6 % depuis 2022 : ses révisions vont toujours vers le bas. Le CNP note que la productivité de 2023 restait 3,5 % sous son niveau de 2019. | Optimiste |
| Écart taux d'intérêt / croissance (r − g) | +0,5 point, constant de 115 % à 188 % de dette | Le rapport juge lui-même cette hypothèse « optimiste ». L'écart de taux avec l'Allemagne était d'environ 30 points de base en 2023 ; un relevé d'octobre 2026 le donne entre 135 et 159 points de base, au plus haut depuis 2011. Précédents de prime de risque : zone euro en 2011, gilts britanniques en 2022. | Optimiste, et non linéaire |
| Chômage structurel | 7 % | Le chômage remonte, avec un écart d'environ 2 points à la zone euro (Morlet-Lavidalie, non sourcé). | Neutre à optimiste |
| Court terme | Croissance 2026 de 0,7 %, déficit 2026 de 5,0 % | Quelques semaines plus tard, le PLF 2027 donne 5,4 % de déficit 2026 et l'Insee prévoit 0,4 % de croissance. | Déjà démenti |
| Fécondité | 1,45 à partir de 2028 | Les projections Insee 2021 retenaient 1,8 ; l'observé est de 1,56 en 2025. La seule variable dite « connue » a dérivé de 0,25 enfant par femme en quatre ans. | Désormais réaliste |
| Solde migratoire | +150 000 par an | La fourchette va de 70 000 à 230 000. Selon le rapport, l'écart pèse 3,6 millions de personnes de 20-64 ans en 2050. | Incertitude large |

## 2. Hypothèses sur les recettes

| Hypothèse | Valeur | Test | Biais |
|---|---|---|---|
| Recettes proportionnelles au PIB | Élasticité de 1 | En 2024, le PLF supposait 1,1 et le réalisé a été d'environ 0,8. Résultat : 41,5 Md€ de moins-values, et un déficit de 5,8 % contre 4,4 % voté. | Optimiste, déjà démenti |
| Barème de l'IR indexé sur les prix | +0,5 point de PIB de recettes d'ici 2050 | Cette hausse d'impôt sans vote est régulièrement neutralisée par des baisses votées. | Optimiste |
| Érosion de l'assiette énergie et véhicules | −1,2 point (et −0,4 point de plus si les objectifs climat sont tenus) | Plus la transition réussit, plus la recette disparaît. | Certaine, si la politique réussit |
| Coût d'un redressement par l'impôt | Perte de PIB de 1,9 % par l'impôt, contre 2,6 % par la dépense | Ce classement est contraire aux précédents de consolidation : Portugal, Suède, et la littérature sur la composition (Alesina-Favero-Giavazzi, 2019 : les ajustements par la dépense sont moins récessifs). Les prélèvements obligatoires sont à 43,6 % du PIB et le coin socio-fiscal à 47 %. | Biais pro-impôt |
| Lecture des leviers « à la fréquence historique » | Hausse des recettes de 2,7 %/an observée « 32 fois », baisse de la dépense « 3 fois » | Les années de hausse des recettes sont surtout celles de forte croissance d'avant 1980. Les cibles de taux d'emploi affichées (87 à 98 %) sont hors du réel. | Biais de présentation |

## 3. Hypothèses sur les dépenses

| Poste | Hypothèse | Test | Biais |
|---|---|---|---|
| Retraites | +0,2 point de PIB d'ici 2050 | Repose sur trois conditions : la levée en 2028 de la suspension de la réforme de 2023, alors que celle-ci a été suspendue deux ans après son vote ; la baisse relative des pensions par indexation sur les prix (−10 % de niveau de vie des retraités selon le COR) ; une productivité de 0,7 %. Aujourd'hui, 125 Md€ par an sont financés hors cotisations, et les droits déjà acquis représentent environ 10 000 Md€. | Fortement optimiste |
| Éducation | −0,6 point (enseignants ajustés à 60 % de la baisse des effectifs) | Le rapport propose de réinvestir cette économie (13 à 21 Md€). Les effectifs d'élèves baissent déjà, sans amélioration des résultats : dernier rang européen en mathématiques (TIMSS 2023). | Économie certaine, puis rendue |
| Santé et autonomie | +1,4 et +1,1 à 1,5 point | Plausible : la prévalence des affections de longue durée est en hausse continue. | Neutre |
| Prestations sociales | Indexées sur les prix, donc en baisse relative (−0,4 point) | Le rapport propose de les indexer sur la croissance (+0,4 point). | Économie annulée |
| Rémunérations publiques | −0,3 point, par décrochage du point d'indice | Précédent : revalorisations de rattrapage (Ségur, enseignants). | Optimiste |
| Défense | 3,5 % du PIB en 2035, soit +1,1 point (36 Md€) | Engagement pris à l'OTAN : c'est la dépense la plus certaine. | Certaine |
| Climat | +0,6 point d'investissement public par an, prise en charge publique à 47 % puis 29 % | Précédent : objectif Grenelle de 23 % de renouvelables en 2020, 19,1 % atteint ; la France est le seul pays de l'UE à l'avoir manqué. | Coût certain, résultat incertain |
| Ensemble des « priorités » | ≈ 107 Md€ par an en 2035, soit environ 3,3 points de PIB | À rapprocher d'un redressement de 4,4 points : les priorités en absorbent les trois quarts. | Dépenses certaines |

## 4. Hypothèses sur les résultats des propositions

| Proposition | Résultat supposé | Test |
|---|---|---|
| Prévention en santé | −0,5 à −0,9 point de dépense en 2050 | Le rapport ne l'intègre pas dans ses chiffres, mais l'utilise pour « sanctuariser » les enveloppes. Selon la Cour des comptes, citée par le rapport, la faiblesse vient de l'allocation des moyens, pas de leur niveau. |
| Éducation, recherche (1 % du PIB), petite enfance | Gains de productivité « non intégrés, estimations fragiles » | Le crédit d'impôt recherche (8 Md€) a une additionnalité discutée. France 2030 est jugée « impact à renforcer » par son comité d'évaluation en 2026. |
| IA | +0,3 point de productivité dans le scénario favorable | Le rapport cite Acemoglu (environ 1 % de PIB mondial en dix ans) contre Aghion : l'incertitude est totale. |
| État-plateforme, décisions confiées à des agents d'IA | Gains d'efficience | Précédents de grands systèmes d'information publics (Louvois, ONP). |
| Loi des grandes options, loi-cadre des finances publiques | Tenue du cap | Aucune loi de programmation des finances publiques n'a été tenue (2014, 2018, 2023). L'écart du PLF 2027 à la dernière programmation est de 13,6 points de dette. Le projet constitutionnel de 2011 n'a jamais été soumis au Congrès. Le Plan s'est arrêté en 1993. |
| Réassurance publique des risques climatiques, dette des collectivités, contrats pour différence | Protection | Ce sont des engagements contingents qui gonflent le hors-bilan, déjà de 2 240 Md€. Les estimations de dommages climatiques du NGFS (phase V) ont été retirées en décembre 2025. |

## 5. Sensibilité de la dette (ordre de grandeur, dette en % du PIB)

| Variante | 2035 | 2050 | Intérêts en 2050 (% du PIB) |
|---|---|---|---|
| Central recalé | 141 | 195 | 5,8 |
| Productivité de 0,5 % au lieu de 0,7 %, effet via la croissance seulement* | 142 | 196 | 5,5 |
| Recettes : choc d'élasticité de type 2023-24 (−0,5 point pérenne) | 146 | 208 | 6,2 |
| Prime de risque endogène, +2 points de base par point de dette** | 142 | 214 | 8,8 |
| Prime endogène, +4 points de base | 143 | 240 | 13,4 |
| Priorités du rapport non financées (+3,2 points) | 157 | 262 | 7,8 |
| Combinaison prudente : productivité 0,5 + prime 2 pb + choc de recettes | 149 | 235 | 9,8 |

\* Le calcul sous-estime l'effet : une productivité plus faible alourdit aussi le poids des pensions indexées sur les prix. Le scénario défavorable du rapport donne 231 %.
\*\* Je n'ai pas pu vérifier dans une source la sensibilité de la prime de risque à la dette. Les valeurs de 2 et 4 points de base sont des hypothèses de calcul.

## 6. Verdict : l'hypothèse la plus dommageable

**C'est l'écart taux/croissance (r − g) supposé constant à +0,5 point, quel que soit le niveau de dette.**

1. **C'est le moteur de la projection.** Le rapport le montre lui-même : le déficit primaire ne bouge que de 0,1 point en 25 ans, et toute la dérive vient des intérêts (de 2,2 % à 5,2 % du PIB).
2. **C'est la seule hypothèse non linéaire et irréversible.** Une erreur sur la productivité ou sur les recettes coûte quelques points de dette. Une prime de risque qui réagit à la dette les transforme en intérêts composés : de 20 à 45 points de dette de plus en 2050, une charge d'intérêts de 9 à 13 % du PIB. Et une confiance perdue ne revient pas au prix d'avant.
3. **C'est elle qui rend les priorités finançables sur le papier.** Le chapitre 4 veut « préférer l'investissement » à la consommation financée par la dette. Mais ces 3,3 points de dépenses nouvelles ne sont des « investissements » que si leur rendement dépasse le coût de la dette, et ce coût est supposé fixe.
4. **Les précédents le contredisent déjà.** L'écart de taux français est passé d'environ 30 à plus de 130 points de base, et les titres émis vers 0 % en 2016 se refinancent aujourd'hui bien plus cher.

**Le biais de fond, dans les propositions, est une triple asymétrie qui s'appuie sur cette hypothèse :**
- **Recettes incertaines.** L'élasticité de 1 a été démentie en 2024 (41,5 Md€ de moins-values). La transition détruit 1,2 à 1,6 point d'assiette fiscale. La hausse de l'IR attendue de l'indexation est réversible.
- **Dépenses certaines.** Défense, retraites (droits acquis, indexation) et intérêts sont contractuels ou juridiques. Une priorité votée devient une base qui ne redescend plus.
- **Résultats incertains.** La prévention, le recyclage du dividende scolaire, la recherche et l'IA ne sont pas chiffrés par le rapport lui-même, et les précédents (Grenelle, France 2030, programmations) sont défavorables.

**Formule possible pour l'audition :** « Le rapport chiffre ses dépenses en milliards et ses bénéfices en espérances, et il suppose que le prêteur attendra. Une dépense certaine financée par une recette incertaine, pour un résultat incertain, au taux d'aujourd'hui : c'est exactement ce qu'un prévisionniste prudent ne doit pas signer. »

Sources :
- [Sénat, rapport l24-144 (PLFG 2024, moins-values de recettes)](https://www.senat.fr/rap/l24-144-1/l24-144-10.html)
- [DG Trésor, retour sur les prévisions 2023-2024](https://www.tresor.economie.gouv.fr/Articles/2025/01/20/retour-sur-les-previsions-de-finances-publiques-pour-les-annees-2023-et-2024)
- [Insee, situation démographique 2025](https://www.insee.fr/fr/statistiques/8999231)
- [Insee, projections 2026](https://www.insee.fr/fr/statistiques/8991068)
- [COR, rapport 2026, ch. 1](https://www.cor-retraites.fr/sites/default/files/2026-06/RA_Part1_Chap1.pdf)
- [COR, hypothèses productivité/chômage](https://www.cor-retraites.fr/sites/default/files/2021-11/Doc8_Hypoth%C3%A8ses_ch%C3%B4mage_productivit%C3%A9.pdf)
- [SDES, renouvelables 2020](https://www.statistiques.developpement-durable.gouv.fr/les-energies-renouvelables-en-france-en-2020-suivi-de-la-directive-200928ce-relative-la-promotion)
- [CNP, 5e rapport](https://www.strategie-plan.gouv.fr/files/files/Publications/2025/2025-04-14%20-%20CNP%20-%20Rapport/CNP-2025-Cinqui%C3%A8me-Rapport-Synth%C3%A8se-15avril.pdf)
- [Banque de France, pertes de productivité](https://www.banque-france.fr/system/files/2024-03/BDF251_1_Pertes_productivite.pdf)
- [Trading Economics, OAT](https://fr.tradingeconomics.com/france/government-bond-yield/news/589851)
- [gold.fr, spread 2026](https://www.gold.fr/news/?p=51076)
