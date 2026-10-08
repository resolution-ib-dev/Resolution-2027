# 04 — Fermer le maintien des droits maladie à la perte du séjour régulier

> **PROJET DE TRAVAIL — NE PAS DÉPOSER EN L'ÉTAT.**
> Rédaction du 2 octobre 2026. Droit en vigueur lu sur l'extrait LEGI du millésime 20261001 : aucun écart de millésime.
> **Jambe de loi de financement de la sécurité sociale.** Elle ne porte pas toute la mesure, et l'écart est déclaré ci-dessous.
> **Corrigé le 20261005 (lot V2)** : phrase de restitution ajoutée au II (circuit A) ; « En clair » réécrit sur la règle (condition de régularité), sans désigner de public.
> **Repris le 20261008 (phase 1.A de la procédure de nuit)** : accroche au texte déposé fixée — article additionnel après l'article 22 du projet de loi de financement de la sécurité sociale pour 2027. Le dispositif, l'exposé et les montants ne sont pas touchés.

**Mesures portées** — clé de jointure du socle.

- `M-024` prise en charge des soins des étrangers en situation irrégulière — composante `PRESTATION` : limiter la prise en charge. Bloc `B-13`, tombe avec le pivot `M-053`.

**Lot** 2.5 — arrêts immédiats. **Phase 1, jambe PLFSS**, par l'arbitrage du 20261002 sur la carte des blocs et des phases.

**Accroche au texte déposé — fixée le 20261008.** PLFSS 2027, **troisième partie, titre Ier**, **article additionnel après l'article 22**. Rang SS-04 au registre des colonnes. **Appui de la passe** : `methode/procedure_nuit_20261008.md`, phase 1.A · `livrables/registre_colonnes_depot_2027.md` · `methode/appui_des_passes.md`, R-G, R-H, R-I · `methode/COMMUN.md` · `reference/guide_legistique.md` · `methode/etats/APP_social.md` · socle `socle_texte_plfss2027.json` et `articles_ouverts_plfss2027.tsv` · dépôt de droit, millésime LEGI **20261001**.

**Écart déclaré entre le typage du dossier et le relevé de droit.** Le dossier porte « siège social, 1,1 Md€ ». **Le relevé refait intégralement dit autre chose** : la dépense visée par les 1,1 Md€ est l'aide médicale de l'État, dont le siège est aux articles `L. 251-1` et suivants du code de l'action sociale et des familles et dont l'article `L. 253-2` du même code dispose que la charge est prise par l'État. Les soins urgents de l'article `L. 254-1` sont eux aussi financés par une dotation forfaitaire versée par l'État à la Caisse nationale de l'assurance maladie. **La dépense est une dépense d'État, et sa jambe est en loi de finances — crédits et norme du code de l'action sociale et des familles.** Aucun article du code de la sécurité sociale ne porte les soins urgents ; la recherche de la série a été jouée et elle est vide.

**Ce que la loi de financement porte réellement, et c'est l'objet de cette pièce.** Le troisième alinéa de l'article `L. 160-1` du code de la sécurité sociale ouvre, à qui cesse de remplir les conditions de résidence stable **et régulière**, une prolongation d'un an de la prise en charge de ses frais de santé par l'assurance maladie et, le cas échéant, de la protection complémentaire. **Cette dépense-là est à la charge de la branche maladie**, elle entre dans le champ de la loi de financement et aucune transversale du découpage ne la couvre.

**Vecteur** — relevé refait intégralement, puis comparé. Écart déclaré ci-dessus.

| levier | ce qu'on y trouve | état |
|---|---|---|
| ressource | rien | `inexistant` |
| affectation | rien | `inexistant` |
| crédits | `sans objet` — véhicule : il n'y a ni état B ni annexe de crédits en loi de financement | `sans objet` |
| **emploi** | **code de la sécurité sociale, troisième alinéa de l'article `L. 160-1`** (`LEGIARTI000044404322`, version du 2022-05-14) | `trouve` |

**Jambe hors de cette pièce, nommée et non rédigée** — le véhicule réel est la loi de finances : norme aux articles `L. 251-1`, `L. 251-2` et `L. 254-1` du code de l'action sociale et des familles, crédits sur le programme qui porte la protection maladie. **Le mandat ne la nomme pas, elle ne s'écrit donc pas ici.**

**Variante** `absolu`. ~~**Dégradation déclarée** : la table des articles ouverts du texte de financement n'est pas disponible à ce fil.~~ **Levée le 20261008** : `articles_ouverts_plfss2027.tsv` est présent au dépôt cloné, il a été mesuré avant d'être nommé, et il fonde l'accroche ci-dessous.

**Seuil d'immixtion.** Trois formes produisaient l'effet : abroger le troisième alinéa, réécrire l'article, remplacer trois mots. **La forme la plus étroite est retenue** — le remplacement de mots —, parce qu'abroger l'alinéa entier retirerait aussi la prolongation à qui perd la seule stabilité de sa résidence, ce que la mesure ne demande pas. Une forme large qui produit plus que l'effet voulu est en faute.

**Preuve.** Opération 3, remplacement d'un membre de phrase. Fragment `les autres conditions mentionnées à l'article L. 111-2-3` : **une occurrence et une seule dans `A`**. Réappliqué à `A`, il redonne `C` à l'octet. Verdict **`PROUVE`**.

**Gage** — qualification : **diminution de charge**. L'article 40 ne l'atteint pas, aucun gage n'est dû, et rien ne s'écrit au dispositif sur ce point. Aucune ligne n'est prise au registre des sources de gage.

**Entrée en vigueur** — deux options rendues, et le coût de chacune.

| option | ligne | ce qu'elle coûte |
|---|---|---|
| **retenue** | personnes qui cessent de remplir la condition de régularité du séjour à compter du 1er janvier 2027 | elle ne touche aucun droit déjà ouvert : la prolongation en cours va à son terme. Elle retarde l'effet budgétaire d'autant |
| écartée | prolongations en cours interrompues au 1er janvier 2027 | l'effet est immédiat et entier, et il retire un droit en cours de service, ce qui ouvre un grief sérieux et un risque contentieux |

**Renvois entrants du troisième alinéa de `L. 160-1`** : aucun renvoi législatif ne vise cet alinéa en propre. Les articles `L. 160-8`, `L. 160-9-1` et `L. 861-1`, qu'il cite, ne sont pas modifiés.

**Réserves ouvertes**

- **Le rendement ne se chiffre pas ici.** Le coût de la prolongation d'un an n'est isolé dans aucune annexe ouverte à ce fil, et il ne se confond pas avec les 1,1 Md€ du dossier, qui portent sur l'aide médicale de l'État. **Aucun montant n'est inventé pour combler ce trou.**
- Les conditions de la prolongation sont renvoyées à un décret en Conseil d'État ; la restriction du champ par la loi commande ce décret, qui devra être repris.
- **La mesure ne borne pas la prise en charge aux cas vitaux et d'ordre public** : ce bornage est au code de l'action sociale et des familles, dans la jambe de loi de finances.
- **Doublon de siège avec SS-08, relevé le 20261008 et non tranché ici.** L'arbitrage de l'auteure du 20261007 au soir, point 14, a logé la fermeture du maintien d'un an au bouclier sanitaire : le 3° du I de `livrables/depot_2027/SS/n5_cadre_bouclier_sanitaire.md` **supprime le troisième alinéa de l'article L. 160-1**, que la présente pièce se borne à restreindre. **Les deux pièces portent le même siège, dans le même véhicule, à deux dates différentes** — 1er janvier 2027 ici, 1er janvier 2028 là. Le défaut de nuit sur deux rédactions concurrentes ferait vivre la plus récente ; **le fil de la phase 1.A ne touche pas aux dispositifs et ne le joue pas**. Question fermée inscrite à `methode/etats/NUIT_1A_accroches_20261008.md`.

**État** : `à vérifier avant dépôt` — le coût de la prolongation n'est pas relevé, et le doublon de siège avec SS-08 n'est pas tranché.

**À vérifier avant dépôt** — chiffrer la prolongation d'un an ; ouvrir la jambe de loi de finances ; trancher le doublon avec SS-08 ; rejouer le vecteur la semaine du dépôt.

---

AMENDEMENT

présenté par

----------

ARTICLE ADDITIONNEL

APRÈS L'ARTICLE 22, insérer l'article suivant :

I. – Au troisième alinéa de l'article L. 160-1 du code de la sécurité sociale, les mots : « les autres conditions mentionnées à l'article L. 111-2-3 » sont remplacés par les mots : « la condition de stabilité de la résidence mentionnée à l'article L. 111-2-3 ».

II. – La présente mesure concourt à la réduction des prélèvements pesant sur les revenus d'activité.

III. – Le I s'applique aux personnes qui cessent de remplir la condition de régularité du séjour à compter du 1er janvier 2027.

EXPOSÉ SOMMAIRE

Cet amendement supprime la prolongation d'un an des droits maladie après perte du séjour régulier.

Un assuré qui perd son droit au séjour conserve un an de prise en charge de ses frais de santé par l'assurance maladie ainsi que, le cas échéant, sa protection complémentaire. Celui qui cotise finance cette année-là sans l'avoir décidée : la règle tient en un alinéa qui renvoie à un décret, sans que le Parlement ait jamais eu à se prononcer sur sa durée. Le législateur a posé que la prise en charge suppose une résidence stable et régulière, puis il a lui-même ouvert la porte qu'il venait de fermer, pour une durée qu'il ne fixe pas (code de la sécurité sociale, article L. 160-1)¹.

Le présent amendement referme cette porte sur un seul des deux cas : la prolongation demeure pour qui perd la stabilité de sa résidence, elle cesse pour qui perd la régularité de son séjour. En clair : la prise en charge par l'assurance maladie suit la condition de régularité du séjour que la loi pose déjà, sans prolongation.

L'effet sur l'exercice porte sur les prestations servies à compter du 1er janvier 2027, aux personnes dont le droit au séjour cesse après cette date. Il n'est pas chiffrable ici : aucune annexe n'isole le coût de cette prolongation. L'économie entre dans la restitution, qui rend en salaire net ce que la dépense prenait aux revenus d'activité. Un amendement distinct porte le bornage de la prise en charge en loi de finances ; les deux se complètent et ne se cumulent pas sur la même dépense. Chaque régime retrouve les personnes qu'il a vocation à couvrir.

¹ Code de la sécurité sociale, article L. 160-1, version en vigueur, base LEGI, millésime du 1er octobre 2026.

---

## [interne] — phase 1.A de la procédure de nuit, 20261008

**Accroche retenue : article additionnel après l'article 22 du texte déposé.** Mesure jouée sur `articles_ouverts_plfss2027.tsv` et sur `socle_texte_plfss2027.json`.

- **Le siège de la pièce — code de la sécurité sociale, article L. 160-1 — n'est pas ouvert par le texte déposé.** La forme « ARTICLE n » est donc fermée, et la pièce reste un article additionnel.
- **L'article 22 est l'article ouvert le plus proche du siège.** Il ouvre l'article **L. 160-13** du code de la sécurité sociale, ainsi que les articles L. 162-32-1, L. 861-3 et L. 871-1 du même code. L'article L. 160-13 et l'article L. 160-1 relèvent du même chapitre — titre VI du livre Ier, prise en charge des frais de santé —, le premier à la section des participations, le second à la section 1 « Dispositions relatives aux bénéficiaires ». L'accroche est donc prise **au voisinage d'un article ouvert, sur le même chapitre du code**, ce qui est la forme la moins coûteuse en recevabilité disponible pour ce siège.
- **Division concernée** : troisième partie, titre Ier, articles 20 à 39 du texte déposé. **Le défaut de nuit — article additionnel après le dernier article de la division, soit après l'article 39 — n'est pas appliqué** : une accroche de voisinage sur article ouvert existe et elle est préférée.
- **Divergence avec SS-08, inscrite et non tranchée.** `SS/n5_cadre_bouclier_sanitaire.md`, qui porte le même siège depuis l'arbitrage du 20261007 au soir, s'accroche après l'article 30. Les deux accroches ne se contredisent pas — deux amendements distincts peuvent viser deux articles du même titre — mais le **doublon de dispositif** qu'elles portent reste entier. Question fermée inscrite à l'état de la phase.
- **Adresse recontrôlée par la passe, millésime LEGI 20261001** : CSS, art. **L. 160-1** `EXISTE` (VIGUEUR, LEGIARTI000044404322, version du 2022-05-14, section 1 « Dispositions relatives aux bénéficiaires »). **Références laissées hors contrôle par cette passe, et leur raison** : les articles L. 111-2-3, L. 160-8, L. 160-9-1 et L. 861-1, cités à l'intérieur de l'alinéa modifié et non visés par le dispositif, que la passe ne touche pas ; les articles L. 251-1, L. 251-2, L. 253-2 et L. 254-1 du code de l'action sociale et des familles, qui relèvent de la jambe de loi de finances non rédigée.
- **Ce que la passe ne touche pas** : le dispositif, l'exposé sommaire, les montants, la preuve, le gage, l'entrée en vigueur.
