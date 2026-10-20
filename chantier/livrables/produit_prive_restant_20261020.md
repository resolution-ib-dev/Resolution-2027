# Produit privé et produit privé restant — analyse du classeur de l'auteur — 20261020

Pièce : `T_1101_1103_PIBtoPPR.xlsx`, remise par l'auteur le 20261020 (SHA-256
`f77645d2…4745b`). Comptes INSEE base 2020, 1949-2025 : 1.101, 1.103, 3.201,
7.301, 7.401. Données versées sans retouche :
`referentiels/insee_comptes_pib_apu_menages_1949_2025.tsv`, formules de l'auteur
à `referentiels/produit_prive_formules_auteur.tsv`. Calcul rejoué et corrigé par
`appareil/produit_prive_restant.py` ; tous les chiffres ci-dessous en sortent.

La méthode est celle de Rothbard (*Power and Market*, ch. 5) : retirer du PIB ce
que les administrations y ajoutent à leur coût (produit privé, PP), puis retirer
du produit privé ce que les administrations en prélèvent, ou en dépensent si
elles dépensent plus (produit privé restant, PPR). La note de fin e12 du livre
en porte l'idée ; elle ne nomme pas Rothbard dans l'état du manuscrit au corpus.

## 1. Le classeur, rejoué — relevé

Concorde à l'identique, 2024 et 2025. En 2024 :

| | Md€ | % |
|---|---|---|
| PIB | 2 935,2 | |
| valeur ajoutée publique (rémunérations et excédent brut) | 485,6 | 16,5 % du PIB |
| **produit privé** | **2 449,7** | 83,5 % du PIB |
| dépense publique vers le privé (DG) | 1 353,0 | |
| recette publique nette (RG) | 1 183,9 | 48,3 % du PP |
| **produit privé restant** | **1 096,7** | **44,8 % du PP** |

Les retraits du circuit sont justes dans leur principe : les cotisations des
employeurs publics (D12, imputées comprises), les cotisations et impôts des
salariés publics, estimés à 29,2 et 38,2 Md€ *(déduits)*. Le 29,6 de 2025
confirme le « 30 » sans source du calcul de portage.

## 2. Ce qui ne tient pas — relevé

1. **Le produit privé restant retranche la dépense, pas le maximum** (ligne 21 :
   `PP − DG`, alors que la ligne 19 calcule `MG`). Faux les années d'excédent :
   1959-1966, 1972, 1974.
2. **La ligne 6 renvoie à une ligne vide** (`BZ5 − BZ15`) : « l'écart à la
   croissance du PIB privé » rend la croissance du PIB elle-même. Il faut la
   ligne 14.
3. **La ligne 25 s'intitule `PP − DG` et calcule `PP − RG`.**
4. **La recette retranche l'excédent brut d'exploitation public (109,8) et les
   autres acquisitions d'actifs (5,0)**, qui ne sont pas des recettes. Le
   retrait est symétrique de la dépense, ce qui garde le déficit, mais la
   « recette nette » et le « taux de taxation facial » (48,3 %) sont sous-évalués
   d'autant : 53,0 % une fois rétablis.
5. **La production immobilisée pour compte propre (32,0)** reste des deux côtés.
   L'INSEE la signale comme élément imputé : ce n'est pas un flux.
6. **Les crédits d'impôt sont retirés des deux côtés**, en prenant le montant
   inscrit en dépense (19,8) aussi pour la recette, qui porte 19,6. Retirés,
   ils sont traités comme des impôts négatifs, ce que l'arbitrage du jour
   écarte.
7. **L'excédent brut d'exploitation public est retiré de la dépense.** C'est un
   choix, non une erreur : il évite de compter le capital public deux fois,
   comme valeur ajoutée retirée du PIB puis comme investissement dans la
   dépense. Mais les salaires publics le sont, deux fois, et c'est le principe
   de Rothbard : la production publique est retirée du produit parce qu'elle n'a
   pas de prix de marché, et sa dépense est retirée parce qu'elle prend des
   ressources au privé. Le capital suit la même règle que le travail, ou bien la
   règle se déclare.

## 3. Le calcul corrigé — 2024 — déduit

| variante | DG | RG | PPR | % du PP | % du PIB |
|---|---|---|---|---|---|
| classeur de l'auteur | 1 353,0 | 1 183,9 | 1 096,7 | 44,8 % | 37,4 % |
| choix de l'auteur gardé, erreurs levées (1, 5) | 1 321,0 | 1 152,0 | 1 128,7 | 46,1 % | 38,5 % |
| Rothbard, crédits retirés | 1 435,9 | 1 266,9 | 1 013,8 | 41,4 % | 34,5 % |
| **Rothbard, crédits gardés** (arbitrage du jour) | **1 455,6** | **1 286,5** | **994,0** | **40,6 %** | **33,9 %** |

Dans les trois versions corrigées, la dépense moins la recette retombe sur le
déficit public des comptes (169,1). La variante de référence des tablettes est
la dernière.

**La série** (tablette T2) : il restait **61 € sur 100 € de produit privé en
1959, 57 € en 1974, 41 € en 1995, 35 € en 2020, 41 € en 2024.**

## 4. Les « 29 euros » — proposition — déduit

Le livre : « Pour une heure de travail, le travailleur moyen produit 63 euros de
richesse mais récupère seulement 23 euros net. […] 29 euros en impôt immédiat et
4 euros en impôt futur par le déficit. »

Le 63 se retrouve : PIB 2024 / 46,27 milliards d'heures travaillées (Eurostat) =
**63,4 €**. Le 29 ne se retrouve sur aucune notion courante : prélèvements
obligatoires INSEE 27,1 € ; notion du projet 27,5 €.

Proposition, sur la même heure et sur les comptes 2024 (tablette T1) :

| par heure travaillée, 2024 | € |
|---|---|
| richesse comptée au PIB | 63,4 |
| dont production publique comptée à son coût | 10,5 |
| **produit privé** | **52,9** |
| prélevé tout de suite (impôts et cotisations, hors circuit public) | 24,6 |
| encaissé autrement (ventes, revenus de la propriété, transferts) | 3,2 |
| emprunté sur l'impôt futur (déficit) | 3,7 |
| **reste à ceux qui l'ont produit** | **21,5** |

Rédaction possible :

> Une heure de travail produit 63 euros au compte du PIB, dont 10,5 de
> production publique comptée à ce qu'elle coûte. Reste 53 euros de vraie
> production. L'État en prend 28 tout de suite et en emprunte 4 sur nos impôts
> futurs : il en reste 21,5 à ceux qui l'ont produite.

Elle remplace la répartition « 23 net, 11 capital, 29 État » par une seule
lecture, qui somme. Le partage des 21,5 € entre travail et capital n'est pas fait :
il demande la ventilation de la dépense publique entre ce qui revient aux
salariés et aux détenteurs du capital, que les comptes ne portent pas.

Le manuscrit ne se révise pas depuis l'aval : la proposition attend l'auteur.

## 5. Les tablettes

`appareil/generer_tablettes_prelevements.py` écrit sept tablettes, en TSV et
dans `livrables/tablettes/Tablettes_prelevements.xlsx` (un onglet chacune, plus
les sources) :

| | tablette | période |
|---|---|---|
| T1 | une heure de travail | 2022-2025 |
| T2 | produit privé restant | 1959-2025 |
| T3 | la glissade de la cotisation à la contribution, % du PIB | 1995-2025 |
| T4 | du brut aux prélèvements obligatoires | 2023-2025 |
| T5 | qui remet le prélèvement privé | 2025 |
| T6 | sur quoi porte le prélèvement (TAXUD) | 1995-2024 |
| T7 | un même euro, sept classements | 2024 |

Rien n'est publié. La page « Données » du site peut les porter après validation.

[interne] Bac à sable. Contrôle de rejeu : `produit_prive_restant.py`, code
retour 1 si le classeur de l'auteur ne se rejoue pas à 10⁻⁴ près.

---

## 6. Relecture des textes originaux — 20261020, second passage — relevé

**Rothbard, *America's Great Depression* (1963)**, appendice « Government and
the National Product, 1929-1932 » : produit privé = PNB − revenu né dans les
administrations et les entreprises publiques ; produit privé restant = produit
privé − le plus élevé de la dépense ou de la recette publique, intérêts versés
compris. Le calcul est aussi donné sur le produit net (NPP).

**Rothbard, *Power and Market* (1970)**, ch. 5, appendice « The Role of
Government Expenditures in National Product Statistics » : on part du produit
national **net** ; on retire le revenu né dans les administrations (les
traitements) ; puis les déprédations : achats aux entreprises, achats des
entreprises publiques, transferts. Forme simple : produit net − le plus élevé de
la dépense totale ou de la recette totale. Les traitements y sont retranchés une
fois.

**Geloso et Reilly, « National output without government? State capacity and
welfare measurement », *Journal of Government and Economics*, vol. 19, 2025**
(document de travail GMU 25-21) : PPR = Y − Y_G − max(E, R), sur le produit net,
États-Unis 1889-2024, le PPR tenu pour borne basse du produit national et le PIB
pour borne haute. C'est la formule de 1963 sur le produit net. *Article non
ouvert (accès refusé) : formule relevée sur la présentation qu'en donne le
Human Action Podcast de l'Institut Mises, juin 2025.*

**Ce qui en découle pour l'excédent brut public.** Aucun des trois textes ne
compte la production publique à son coût : elle est retirée en entier du
produit. Le capital public suit le même sort, mais du côté du produit : en
passant au produit net, l'amortissement de toute l'économie sort, et avec lui
l'excédent brut public, qui n'est que l'amortissement du capital public compté
à son coût. Du côté de la dépense, les trois textes retranchent les achats
publics en brut, investissement compris. Retirer l'excédent brut public de la
dépense, comme le fait le classeur, n'a de répondant dans aucun d'eux : cela
revient à nettoyer l'investissement public en gardant le produit privé brut.

| 2024 | formule | PPR, Md€ | % du produit privé | % du PIB |
|---|---|---|---|---|
| classeur de l'auteur | brut, EBE retiré de la dépense | 1 096,7 | 44,8 % | 37,4 % |
| Rothbard 1963, brut | GPP − max(E, R) | 1 013,8 | 41,4 % | 34,5 % |
| **Rothbard 1963, net = Geloso et Reilly 2025** | PNN − Y_G − max(E, R) | **588,7** | **29,1 %** | **20,1 %** |
| Rothbard 1970 | PNN − max(E, R) | 779,1 | 38,5 % | 26,5 % |

Dépense et recette hors circuit public (cotisations et impôts sur la masse
salariale publique), hors production pour compte propre, crédits d'impôt nettés
comme le fait l'auteur. Amortissements : Eurostat, `nasa_10_nf_tr`, P51C, 1978-2024
(`referentiels/eurostat_ccf.tsv`). La forme de 1970 garde le circuit dans la
dépense : les traitements, cotisations comprises, n'y sont comptés qu'une fois.

Série, formule Geloso et Reilly, PPR en % du produit privé net : 42,5 % en 1978,
38,7 % en 1990, 37,3 % en 2000, 36,0 % en 2007, 32,7 % en 2019, 21,6 % en 2020,
29,1 % en 2024.

*Proposé, non validé* : la formule de Geloso et Reilly comme référence, publiée
et relue, et la plus proche de la structure du classeur.
