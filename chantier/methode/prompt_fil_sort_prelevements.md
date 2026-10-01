# Prompt — fil « sort des prélèvements »

## Ligne de lancement (Cowork)

> Fil Cowork — sort des prélèvements. Activer `referentiels/prelevements_forces_20260930.tsv`, `livrables/recensement_prelevements_20260930.md`, `Synthèse Calculs Résolution_0910.xlsx` onglet « Refonte fiscalité », `livrables/paquet_machine.md` (M-028 à M-036), `methode/fragments/arbitrages/20260930-defauts-reconciliation.md`, `methode/fragments/arbitrages/20260930-perimetre-fiscal.md`, skill `compatibilite-doctrine`, skill `vecteur-mesure`. Mandat : corriger d'abord la table de passage en lot 0, puis appliquer le schéma à chaque prélèvement — supprimé, fondu dans un des quatre impôts conservés avec lequel, maintenu à part, non touché, hors champ — et écrire le passage chiffré entre les 624,9 Md€ du schéma, les 876,7 Md€ de rendement recensé et les 1 250,76 Md€ de prélèvements obligatoires. Le schéma de l'auteur fait foi : il ne se discute pas, il s'applique. Classement du sort et bouclage chiffré seulement, aucune rédaction, aucun amendement.

## Ce que le fil trouve en entrant

420 prélèvements classés en huit assiettes — cotisations sociales, contributions
sociales sur les revenus, taxes sur la masse salariale, revenu des personnes,
activité des entreprises, consommation, propriété et droits d'usage, hors champ —
dont 232 chiffrés et 294 adressés en droit.
Aucun ne porte de sort. Le référentiel versé au projet porte tout le recensement ;
le classeur `tri_impositions_20260930.xlsx`, qui en est la mise en forme, ne peut
pas être versé — le projet ne stocke pas de binaire — et se demande à l'auteur.
Le classeur est un recensement pur : son onglet de réforme a été retiré parce
qu'il portait une proposition du fil précédent, non arbitrée et non exportable.
Le chapitre « Ce que le fil précédent a tenté » dit pourquoi, et ce qu'il faut
faire à la place — le lire avant de commencer.

La table de passage entre les vingt-trois lignes du schéma et les 420
prélèvements est construite et sa couverture mesurée —
`referentiels/table_passage_schema_prelevements_20260930.tsv` et
`livrables/couverture_table_de_passage_20260930.md`. Le fil ne la refait pas :
il la corrige en lot 0 (voir plus bas), puis attribue.

## La règle de conduite

Le schéma « Refonte fiscalité » est la doctrine de l'auteur. Un prélèvement dont
le sort découle du schéma prend ce sort. Un prélèvement que le schéma ne nomme
pas prend le sort de sa ligne d'agrégat dans le schéma, et le fil l'inscrit
comme tel. Un prélèvement que ni le schéma ni son agrégat n'atteignent est porté
en attente, nommé, non comblé par déduction.

## Les points de contact à traiter explicitement

- Maintenus par le schéma et non par la nomenclature du recensement : jeux
  (dans les 25,6 Md€ « alcool, tabac, jeux »), assurances (19,2), taxe de séjour
  (1,1), outre-mer (1,6), forfaits de cotisation (8,8).
- Énergie : le schéma ne supprime que 8 Md€ sur 43,7. Le partage est à porter
  au prélèvement.
- Droits de mutation : 37,9 Md€ traités à part par le schéma, dont 32,45
  supprimés et remplacés par une franchise. Le recensement les classe dans la
  propriété — le sort suit le schéma, pas la nomenclature.
- Chiffre d'affaires et bénéfices (10,3) soldés sur l'impôt sur les sociétés :
  schéma et recensement concordent.

## Le bouclage à écrire

624,9 Md€, base 2024, périmètre de doctrine, d'un côté. 876,7 Md€ de rendement
recensé, base 2026, périmètre de publication, de l'autre. Et 1 250,76 Md€ de
prélèvements obligatoires 2024 au-dessus des deux. Le passage entre les trois
se rend en lignes de solde explicites, pas en commentaire.

Rappel de périmètre : 188 prélèvements sur 420 ne portent aucun montant publié.
Le bouclage ne peut pas les chiffrer et n'a pas à le faire ; il les compte.

## Ce que le fil précédent a tenté, et ce qui lui a manqué

Ce chapitre existe pour que l'onglet soit refait autrement, pas repris.

**Ce qui a été tenté.** Le sort a été déduit de la nomenclature : les quatre
impôts conservés posés comme têtes de leur assiette, tout prélèvement partageant
leur assiette marqué « se fond dedans », les accises sur l'énergie, le tabac et
l'alcool marquées « maintenu à part », le reste « ne se fond dans aucun ». Quatre
catégories, appliquées d'un bloc aux 420 lignes, sans jamais lire le schéma de
l'auteur ligne à ligne.

**Pourquoi c'était faux.** Ce n'est pas la doctrine, c'est une déduction faite
depuis le classement du fil lui-même. Le classement est un outil de lecture ; il
ne porte aucune intention de réforme. Un prélèvement partage l'assiette d'un
impôt conservé sans que rien n'impose de l'y fondre, et le schéma de l'auteur en
maintient plusieurs que cette règle supprimait. Le résultat avait la forme d'un
constat alors qu'il n'était qu'une proposition, et il était mêlé au recensement
dans le même classeur : on ne pouvait plus distinguer ce qui était mesuré de ce
qui était supposé.

**Ce qui a manqué, par ordre d'importance.**

1. **La table de passage entre le schéma et le référentiel.** Le schéma tient en
   vingt-trois lignes d'agrégat en base 2024 ; le référentiel en 420 prélèvements
   en base 2026. Aucune clé ne relie les deux. C'est cette table qui manque, et
   c'est elle qu'il faut construire en premier : pour chaque ligne du schéma, la
   liste des prélèvements qu'elle recouvre, avec le rendement recouvert et le
   solde non couvert. Tant qu'elle n'existe pas, tout sort porté est une
   supposition. Elle se construit par libellé, puis par agrégat pour ce que le
   libellé n'attrape pas, et le reste se compte sans se combler.

2. **La doctrine elle-même, et pas seulement l'onglet.** Le schéma dit des
   montants ; les fiches M-028 à M-036 disent les règles — ce que devient la TVA
   à taux unique, ce que couvre la suppression des impôts de production, ce que
   fait la franchise sur les mutations. Le sort d'un prélèvement se lit dans la
   règle, pas dans le montant de la ligne qui le contient.

3. **La réconciliation des bases.** 2024 contre 2026, doctrine contre
   publication, net contre brut. Sans elle, les totaux du sort ne peuvent être
   vérifiés contre rien, et l'écart entre 624,9 et 876,7 reste un mystère plutôt
   qu'une somme de causes nommées.

4. **Une règle pour les 188 prélèvements sans montant publié.** Un sort peut leur
   être attribué, leur poids non. Il faut décider ce qu'on en fait dans les
   totaux — comptés en nombre, jamais en euros — et l'écrire avant de commencer,
   pas après.

**La méthode qui en découle.** Construire la table de passage, mesurer sa
couverture, ne porter le sort qu'ensuite, et l'écrire dans un classeur distinct
du recensement. Un prélèvement dont ni la règle ni l'agrégat ne décident reste
en attente, nommé : c'est un arbitrage pour l'auteur, pas un trou à combler.

## Les pièces attendues

Deux, pas davantage : la colonne de sort ajoutée au référentiel, et un onglet de
réforme autoportant, exportable, dans un classeur distinct du recensement.

---

# Ce qui a été tranché après l'écriture de ce prompt — 20260930

*Deux fragments d'arbitrage sont tombés le 20260930 après l'écriture ci-dessus.
Ils commandent le lot 0 et le sort du solde. Ils priment sur toute lecture
antérieure de ce prompt.*

## Lot 0 — la table de passage se corrige avant d'être relue

Défaut D-4 de `methode/fragments/arbitrages/20260930-defauts-reconciliation.md`.
`referentiels/table_passage_schema_prelevements_20260930.tsv` porte encore
l'ancien rattachement de la ligne « dont forfaits de cotisation » : la
contribution solidarité autonomie entre à la ligne, les contributions sur les
attributions d'options et d'actions gratuites en sortent vers « 0 — hors
périmètre du schéma ». Les compteurs de
`livrables/couverture_table_de_passage_20260930.md` se rejouent dans le même
mouvement. **C'est le lot 0 du fil : rien ne s'attribue avant.**

## Les défauts de réconciliation s'appliquent sans autre instruction

- **D-1.** Quand le CGI réécrit par l'expert et le schéma tranchent
  différemment, le corpus prime et l'écart se déclare en exposé sommaire — taxe
  foncière, taux de TVA, droits de mutation à titre gratuit.
- **D-2.** Un article-siège touché par le texte financier ne vaut ni maintien ni
  suppression par lui-même. Le droit de licence sur les débitants de tabacs est
  **maintenu** ; les huit prélèvements que le texte touche parmi les 41 à
  contrepartie invoquée restent dans leur lot et suivent son arbitrage.
- **D-3.** Les 83 cotisations sociales restent hors mandat et ne reçoivent aucun
  sort. Le solde du fil reste à 129.

## Le périmètre fiscal est arrêté

`methode/fragments/arbitrages/20260930-perimetre-fiscal.md`, de l'auteure.

**Prélèvements sociaux sur le capital — sort « non touché ».** Les prélèvements
de solidarité, 15,6 Md€, et les prélèvements sociaux sur les revenus du
patrimoine et des placements prennent le sort **non touché** et ne comptent ni
au gage ni à la restitution. Motif : la restitution salariale porte sur les
revenus d'activité ; M-025 supprime la CSG et la CRDS sur l'activité, non sur le
capital. La question est close, elle ne se rouvre pas dans ce fil.

**Flat tax.** La fusion du prélèvement forfaitaire unique dans l'impôt sur le
revenu, par la rédaction de l'expert, est une opération technique de rédaction.
Elle ne change ni le schéma, ni la situation des redevables ordinaires, et
n'appelle aucun arbitrage.

**Les 33 redevances et rémunérations pour service rendu s'auditent une par une.**
Redevances, rémunérations pour service rendu, frais de contrôle — les
prélèvements à contrepartie invoquée restés sans sort s'éprouvent **ligne à
ligne** contre les principes de la doctrine :

- **par défaut, supprimer et fondre** ;
- **sortie du périmètre des prélèvements obligatoires en repli**, lorsque la
  suppression ne vole pas ;
- **le repli ne se prend jamais par défaut ni par commodité** : chaque ligne
  s'éprouve ;
- **sous le milliard d'euros, le principe prime et le montant est secondaire.**

Le fil rend une solution justifiée pour chacune et **ne remonte à l'auteure que
les points saillants**. Un audit rendu en bloc, ou un repli appliqué à la série,
est une faute.

## Ce que ce fil ne fait pas

**Il n'écrit aucune adresse.** 105 prélèvements du référentiel ne portent aucun
siège — dont les prélèvements de solidarité, 15,6 Md€. Un sort s'attribue sans
adresse ; le relevé de siège est un chantier distinct, dû avant la phase 3, sur
les prélèvements sans siège qui reçoivent un sort autre que « non touché » ou
« hors mandat ». Ce fil constate le trou et le compte, il ne le comble pas.

**Il n'active ni `disposition-cible`, ni `redaction-legistique`, ni
`expose-sommaire`.** La qualification, le rattachement, le vecteur, la rédaction
cible et l'exposé se font au projet machine, valise branchée. Ce fil est au
projet doctrine : il classe et il boucle.
