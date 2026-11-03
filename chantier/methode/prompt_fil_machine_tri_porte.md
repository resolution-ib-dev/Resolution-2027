# Mandat — fil machine : vérification de fond et de rédaction des amendements du tri des prélèvements

*Écrit le 20261103 par le fil tri-porte, sur consigne de l’auteur. Fil de production, exigeant : **chaque verdict se prouve sur pièce, chaque phrase versée dit si elle est relevée, héritée ou déduite (A-299).** Il ne tranche aucune question de fond : il l’inscrit, la pose fermée, et continue sur le reste.*

---

## 0. Ouverture

Dépôt `resolution-ib-dev/Resolution-2027`, branche dédiée tirée de `claude/pensive-mayer-c4pyn3`. Skill `resolution-chantier`, puis `chantier/CLAUDE.md`. Machine : `chantier/machine/00_COMMENCER_ICI.md`, `01_DEMARRER.md`, `68_CONTROLE_atelier.py`. Dépôt de droit : `data/`, millésime LEGI 20261031 ; **tout article se lit dans sa version applicable au 1er juillet 2027** (`droit.article(code, num, jour='2027-07-01')`). Skills : `vecteur-mesure`, `disposition-cible`, `expose-sommaire`, `confrontation`, `audit-conformite`, `compatibilite-doctrine`, `analyse-transposabilite` pour la recevabilité.

**Lectures obligatoires avant la première écriture (R-G), et rien ne se cite sans avoir été ouvert :**

| matière | pièce |
|---|---|
| consignes des tours précédents | `methode/consignes_auteure_20261005.md` — en particulier A3, A45, B5, B16 et la table des péremptions |
| arbitrages du 20261103 | `methode/arbitrages.md`, section « 20261103 — tri-porte » (règles des devenirs, dix réponses, second tour) |
| capital et forfaitaire | `methode/arbitrages.md`, « Arbitrages — périmètre fiscal, 20260930 » ; `P1/4_2_refonte_taxes_D_plus_values.md`, § « Coordination due, non rédigée » |
| dates | `livrables/registre_exceptions_dates.md` ; `methode/etats/CALENDRIER_20261007.md` ; `livrables/tri_prelevements/calendrier_suppressions_nouvelles.md` |
| règles | `methode/COMMUN.md` ; `methode/regles_redactionnelles.md` ; `methode/appui_des_passes.md` (R-G, R-H, R-I) ; machine `18` |
| gage et recevabilité | machine `05_PROCEDURE_gage.md` (§ 2 bis, 2 ter) ; `methode/etats/CLOTURE_gage_20261007.md` ; `methode/etats/GAGE_taxes_affectees_20261007.md` ; `methode/procedure_contre_plf.md`, arbitrage n° 3 |
| rattachement | machine `03_PROCEDURE_rattachement.md` ; `reference/domaine_lfss_LO111-3.md` |
| exposés | machine `12`, `13`, `41_SCRIPT_controles_expose.py` ; `methode/registre_exposes_depot_2027.md` |
| rangs | `livrables/registre_colonnes_depot_2027.md` |
| ce que tri-porte a produit | `livrables/tri_prelevements/` ; `appareil/tri_porte/LISEZ-MOI.md` ; `referentiels/sort_prelevements_20261103.tsv` |

---

## 1. Objet et source unique

Cinq amendements nouveaux, **en projet, non déposables en l’état** : PLF 1re partie n° 35 à 38 (`livrables/depot_2027/P1/tri_35_…` à `tri_38_…`), PLFSS n° 9 (`SS/tri_09_…`), versés à `LIASSE_PLF_P1.md` (lot VI) et `LIASSE_PLFSS.md`.

**Source unique : `appareil/tri_porte/amendements.py`.** Fiches et liasses se régénèrent par `verser_amendements.py` (qui refuse un second ajout : remettre d’abord les liasses à leur état antérieur au lot VI, puis reverser). **Aucune retouche directe d’une fiche ou d’une liasse.** Le tri (`construire_tri.py`, `tables.py`, `classeurs.py`) se rejoue après tout changement de rangs portés.

---

## 2. Vérification de fond — par amendement

Pour chaque abrogation : **quel prélèvement disparaît, quel impôt en reprend le produit, qui perd une ressource, quelle mission perd son financement, et qui la porte désormais.** Une réponse manquante est une anomalie.

### 2.1 Questions communes

1. **Devenir** : chaque rang porté correspond-il au devenir du tri (remplacé par tel impôt, fondu dans l’équilibre) ? Un rang conservé ou « à fusionner » ne doit être abrogé par aucun dispositif.
2. **Périmètre exact** : l’abrogation emporte-t-elle d’autres choses que le prélèvement ? Lire chaque article abrogé en entier : une obligation de fond, une sanction, un régime, un fonds y vivent-ils aussi ? Exemples à instruire : L. 351-12 à 15 CGFP (la contribution est la sanction de l’obligation d’emploi, qui survit sans elle) ; L. 3253-18 C. trav. (seul financement de la garantie des salaires) ; L. 862-3 et L. 862-4 CSS (financement de la complémentaire santé solidaire) ; L. 652-6 CSS (ressource du régime des avocats) ; art. 18 de la loi n° 2004-803 (financement de la CNIEG) ; 1609 novovicies à tertricies CGI (Agence nationale du sport).
3. **Renvois entrants** : `droit.py renvois` sur chaque article abrogé. Tout texte qui renvoie à un article abrogé appelle une coordination, ou la clause « dispositions qui affectent… cessent » doit l’atteindre. Les lister, les trancher.
4. **Le texte déposé** : `machine/44_SCRIPT_article_ouvert.py` et `livrables/portes_ouvertes_plf2027.md`. Le PLF 2027 modifie-t-il un article abrogé (art. 20, 21, 22, 25, 27 notamment) ? Si oui : accroche à l’article ouvert, ou mention de coordination en navette, à l’exposé.
5. **Double emploi** : aucune subdivision abrogée deux fois — contre le n° 1, III (CIBS), les n° 22 et 25, le PLFSS n° 1, III, 8° (L. 137-13, quatrième alinéa).
6. **Doctrine** : `69_CONTROLE_doctrine.py` et `compatibilite-doctrine` sur chaque pièce ; aucun prélèvement nouveau ; la majoration-gage seule, déclarée postiche.

### 2.2 Par pièce

| pièce | ce qu’il faut éprouver en plus |
|---|---|
| P1 n° 35 (art. 15) | la suppression de l’art. 15 ne laisse-t-elle rien d’autre du texte déposé sans base ? Lire tout l’art. 15 (I à fin), pas seulement l’art. 48 de la loi n° 2025-127 |
| P1 n° 36 | III : l’ajout au 1 de l’art. 206 CGI et la réécriture de L. 518-16 CMF — la Caisse des dépôts est-elle exonérée ailleurs (art. 207, 208, régime de l’établissement) ? Le versement à l’État de L. 518-16 reste-t-il cohérent ? I, 1° : les prélèvements sur les jeux (1609 novovicies s.) ont-ils des affectations hors CGI (code du sport L. 112-11-1) ? II, 2° : les 82 articles CIBS L. 421-93 à 167 ne portent-ils que les taxes visées (lire les sections) ? |
| P1 n° 37 | TA : cohérence avec le n° 29 (1635 quater A, impositions de 2028) ; l’abrogation de L. 331-1 à 17 C. urb. ne retire-t-elle pas autre chose que la taxe ? TLPE : délibérations communales ; casinos L. 2333-54 à 56 : la part de l’État (état A, ligne 1786) a-t-elle un autre siège ? TASCOM : art. 3 de la loi n° 72-657, texte hors dépôt |
| P1 n° 38 | chaque organisme privé de sa ressource : est-il dissous par le P2 n° 25 (liste du III) ou financé par crédits ? Sinon, l’abrogation crée un trou de financement d’une mission maintenue : l’inscrire |
| PLFSS n° 9 | chaque contribution : affectation (L. 131-8 CSS et autres), branche ; cohérence avec la clé de répartition du PLFSS n° 2 ; la CTA (loi n° 2004-803) relève-t-elle bien du domaine de la LFSS (LO 111-3-7) ? |

### 2.3 Recevabilité financière — à instruire, non à supposer

Article 40 de la Constitution : la perte d’une ressource d’un **tiers qui n’est ni l’État, ni une collectivité, ni la sécurité sociale** (opérateurs, associations, établissements) se gage-t-elle comme le font les n° 25 et 38 (« perte de recettes pour l’État ») ? Instruire sur `05_PROCEDURE_gage.md` et la pratique relevée au corpus ; déclarer le risque à l’exposé ou corriger le gage. Le gage PLFSS sur l’accise sur les tabacs : conforme au § 2 ter, ou formule à reprendre. **Consigne de l’auteur du 20261103 : les gages sont circonstanciels** — la forme se corrige, le principe ne se rouvre pas.

---

## 3. Vérification de rédaction

1. **Disposition prouvée par réapplication** (`disposition-cible`, `43_SCRIPT_diff_cible.py`) : chaque abrogation appliquée au droit du 1er juillet 2027 rend le texte cible voulu ; chaque subdivision visée (« le 5° ter », « le VI », « le 1° », « les deuxième et dernier alinéas ») existe à cette date sous cette désignation. Les fourchettes « X à Y » : borne basse et borne haute existent, l’ordre officiel du code est celui que la fourchette suppose (cas d’école : L. 245-5-1 A, qui précède L. 245-5-1).
2. **Textes hors dépôt**, cités sur la référence de l’annexe et non réappliqués : code forestier (L. 341-6), code minier (L. 132-16), lois n° 72-657 (art. 3), 2003-1312 (art. 72), 2004-803 (art. 18), 2006-1666 (art. 130), 2010-1658 (art. 96). Les ajouter à `codes.json` et rafraîchir le dépôt, ou déclarer l’insuffisance en nommant la pièce manquante. Rien ne se supplée de mémoire.
3. **Entrée en vigueur** : reprendre `calendrier_suppressions_nouvelles.md`. Consigne de l’auteur du 20261103 : **un report à 2028 sans bonne raison ne tient pas**. Recaler au 1er juillet 2027 le n° 36, II, 2° (au prorata de la période d’affectation ou de détention) et le n° 37 pour les remontées mécaniques et les sites nordiques ; justifier ou recaler le n° 37, I, 5° ; **rédiger nommément** le n° 38, II, B et le PLFSS n° 9, II, B, imposition par imposition, fait générateur relevé. Une date hors des quatre dates communes ouvre sa ligne au registre des exceptions dans la même passe. Règle du jour : un 1er janvier ou un 1er juillet, jamais un 31 décembre.
4. **Gabarit** : vecteur, rattachement (art. 34 LOLF ou LO 111-3-7 CSS, nommé à l’interne), gage, « concourt à la réduction des prélèvements pesant sur les revenus d’activité ». Aucun point-virgule au dispositif ; rédaction positive.
5. **Exposés** : 200 à 300 mots, trois temps, accroche commune, sources entre parenthèses avec note ; régénérés par l’outil, jamais retouchés ; chaque chiffre recompté sur sa pièce au moment de l’écrire ; arrondis selon la règle de l’auteur ; lexique (`controle_lexique.py`) — « gratuites » proscrit hors négation. Les exposés suivent le dispositif recalé (dates, comptes « vingt-sept », « dix-huit », « treize », « dix-huit »).
6. **Typographie** : insécables devant `: ; ! ? » %` et après `«`, séparateur de milliers insécable, pas de virgule devant une conjonction de coordination.

---

## 4. Coordinations nommées, à mesurer

- PLFSS n° 1, III, 8° et PLFSS n° 9, I, 1° (L. 137-13).
- Exposés des P1 n° 22 et 25 (fin des taux réduits de TVA au 1er juillet 2027) contre le dispositif du P1 n° 21 (1er juillet 2028) : **mesurer, ne pas trancher**, et poser la question fermée.
- P1 n° 25, II, B (prélèvement de l’ANCOLS) : l’auteur le dit supprimé par construction ; vérifier que le texte le produit sans réécrire la pièce hors mandat.
- P1 n° 20 : il porte, à rédaction constante, le prélèvement de solidarité et les prélèvements sociaux du capital (schéma des 30 %) ; vérifier que le § « Coordination due, non rédigée » de la pièce D le dit toujours.
- Visas à relire : 231 B CGI (PLFSS n° 3, II), absent du dépôt ; L. 421-78-1 CIBS (P1 n° 1), hors vigueur.

---

## 5. Ce qui ne se rouvre pas

Les arbitrages de l’auteur du 20261103 : six devenirs ; CSG et CRDS remplacées par l’IR ; cotisations en liasse ultérieure ; redevances par la voie réglementaire ; retenues à la source et exit tax conservées avec l’IR ; pilier 2 et petit colis au bloc Union européenne ; taxe aurifère de Guyane supprimée avec les affectations ; ANCOLS supprimé par construction ; capital au schéma des 30 % ; Caisse des dépôts à l’IS ; stocks pétroliers en statu quo ; extinction des contributions IS avec les niches. Les cinq sièges n.d. (A-440).

**Ouvert, et ne se tranche pas ici** : le millésime des rendements.

---

## 6. Critères de sortie

- Machine : `41`, `42`, `43`, `64`, `69` joués sur chaque pièce, zéro anomalie bloquante, chaque signal déclaré et motivé.
- Chantier : `controle_sieges_prelevements.py` sur `sort_prelevements_20261103.tsv` à 0 échec ; `make index` à 0 anomalie bloquante ; `controle_lexique.py` sans anomalie nouvelle autre que l’accroche commune.
- Une table par pièce : **division → question de fond → verdict → pièce qui le prouve → relevé, hérité ou déduit**.
- Une table des dates : division → date avant → date après → motif.
- Les questions fermées, dans les mots de l’auteur, une par ligne.
- `.docx` des deux liasses par `appareil/liasse2docx.js`, contrôlés sur leur PDF. **Aucune publication au site.**
- Entrées de registre titrées et datées, sans numéro (A-282) ; journal ; ligne à `methode/sas.md` si un sas s’ouvre ; commit et push sur la branche du fil ; liste des branches distantes avec leur état.
