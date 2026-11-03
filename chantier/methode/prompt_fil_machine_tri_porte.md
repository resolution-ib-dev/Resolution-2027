# Mandat — fil machine : vérifier et consolider les amendements du tri des prélèvements

*Écrit le 20261103 par le fil tri-porte, sur consigne de l’auteur : « repasser la balle pour vérif et consolider à un fil machine ». Fil de production. Il ne tranche aucune question de fond : il l’inscrit et s’arrête sur elle.*

## 0. Ouverture

Dépôt `resolution-ib-dev/Resolution-2027`, branche dédiée tirée de `claude/pensive-mayer-c4pyn3`. Skill `resolution-chantier`, puis `chantier/CLAUDE.md`. La machine se joue depuis `chantier/machine/` : `00_COMMENCER_ICI.md`, `01_DEMARRER.md`, contrôle `68_CONTROLE_atelier.py`. Dépôt de droit : `data/`, millésime LEGI 20261031, version applicable au **1er juillet 2027**.

**À ouvrir avant d’écrire (R-G de `methode/appui_des_passes.md`), toutes, et rien citer sans l’avoir ouvert :**

| matière | pièce |
|---|---|
| consignes arrêtées des tours précédents | `methode/consignes_auteure_20261005.md` (A3, A45, B5, B16 et la table de péremption) |
| dates | `livrables/registre_exceptions_dates.md` ; `methode/etats/CALENDRIER_20261007.md`, § 4 (règle « se caler sur 2026 si besoin ») |
| règles communes et de rédaction | `methode/COMMUN.md` ; `methode/regles_redactionnelles.md` ; machine `18_OUTIL_regles_redactionnelles.md` |
| gage | machine `05_PROCEDURE_gage.md` (§ 2 bis et 2 ter) ; `methode/etats/CLOTURE_gage_20261007.md` |
| rattachement | machine `03_PROCEDURE_rattachement.md` ; `reference/domaine_lfss_LO111-3.md` |
| exposés | machine `12_OUTIL_expose_sommaire.md`, `13_OUTIL_expose_sommaire_releves.md` ; `methode/registre_exposes_depot_2027.md` |
| rangs et colonnes | `livrables/registre_colonnes_depot_2027.md` |
| ce que l’auteur a arrêté le 20261103 | `methode/arbitrages.md`, section « 20261103 — tri-porte » |
| ce que le fil tri-porte a produit | `livrables/tri_prelevements/` (rapport, récapitulatif, calendrier) ; `appareil/tri_porte/LISEZ-MOI.md` |

## 1. Périmètre

Cinq amendements nouveaux, en projet : PLF 1re partie n° 35 à 38 (`P1/tri_35_…` à `P1/tri_38_…`), PLFSS n° 9 (`SS/tri_09_…`), versés à `LIASSE_PLF_P1.md` (lot VI) et `LIASSE_PLFSS.md`. **Source unique des textes : `appareil/tri_porte/amendements.py`** ; les fiches et les liasses s’en régénèrent par `verser_amendements.py`. Une correction s’écrit à la source, puis se reverse.

Hors périmètre : les 81 amendements antérieurs, sauf coordination nommée au § 2, point 6.

## 2. Ce qu’il y a à faire

1. **Calendrier.** Reprendre `livrables/tri_prelevements/calendrier_suppressions_nouvelles.md`. Consigne de l’auteur du 20261103 : *un report à 2028 sans bonne raison ne tient pas.* Recaler au 1er juillet 2027 ce que la table marque « à recaler » (n° 36, II, 2° ; n° 37, remontées mécaniques et sites nordiques) ; justifier ou recaler le n° 37, I, 5° ; **rédiger nommément** le n° 38, II, B et le PLFSS n° 9, II, B, imposition par imposition, avec le fait générateur relevé au dépôt de droit. Toute date hors des quatre dates communes ouvre sa ligne au registre des exceptions dans la même passe.
2. **Chaîne de la machine, pièce par pièce** : vecteur (`04`), disposition et réapplication (`11`, `43_SCRIPT_diff_cible.py`), rattachement (`03`), gage (`05`), exposé (`12`, `13`, `41_SCRIPT_controles_expose.py`), sortie (`42_SCRIPT_controle_sortie.py`), droit (`64_CONTROLE_droit.py`), doctrine (`69_CONTROLE_doctrine.py`).
3. **Gage.** Le réflexe de la machine est sans hausse ; le PLFSS n° 9 gage sur l’accise sur les tabacs, le n° 36, III assujettit la Caisse des dépôts à l’IS. L’auteur a dit le 20261103 que **les gages sont circonstanciels** : appliquer `05` § 2 ter, et porter à l’exposé ce que la formule a de postiche.
4. **Textes hors dépôt de droit**, cités sur la référence de l’annexe et non réappliqués : code forestier (L. 341-6), code minier (L. 132-16), lois n° 72-657 (art. 3), 2003-1312 (art. 72), 2004-803 (art. 18), 2006-1666 (art. 130), 2010-1658 (art. 96). Les ajouter à `codes.json` et rafraîchir le dépôt de droit, ou déclarer l’insuffisance. Aucun verbatim ne se supplée de mémoire.
5. **Exposés** : 200 à 300 mots, trois temps, accroche commune ; les régénérer par l’outil, non par retouche. Recompter chaque chiffre sur sa pièce.
6. **Coordinations nommées** :
   - PLFSS n° 1, III, 8° (quatrième alinéa de L. 137-13) et PLFSS n° 9, I, 1° (L. 137-13 entier) ;
   - P1 n° 1, III (lignes du CIBS) et P1 n° 36 (CIBS L. 421-93 à 167, L. 455-44 à 56) : aucune subdivision abrogée deux fois ;
   - exposés des P1 n° 22 et 25 (fin des taux réduits de TVA au 1er juillet 2027) contre le dispositif du P1 n° 21 (1er juillet 2028) : **mesurer, ne pas trancher** ;
   - P1 n° 25, II, B (prélèvement de l’ANCOLS maintenu) : l’auteur l’a dit supprimé par construction le 20261103 ; vérifier que le texte le dit, sans réécrire la pièce.
7. **Consolidation** : rangs au registre des colonnes, sommaires des liasses, `.docx` par `appareil/liasse2docx.js`. **Aucune publication** au site, aucune fusion sans l’auteur.

## 3. Ce qui ne se rouvre pas

Les dix réponses de l’auteur du 20261103 (registre, section « 20261103 — tri-porte »), dont : redevances par la voie réglementaire ; cotisations en liasse ultérieure ; prélèvements sociaux du capital portés par le schéma du forfaitaire à 30 % du n° 20 ; taxe aurifère de Guyane supprimée avec les affectations (n° 25) ; Caisse des dépôts à l’IS. Les cinq sièges n.d. (A-440).

**Reste ouvert, et ne se tranche pas ici** : le millésime des rendements (réponse de l’auteur à préciser).

## 4. Ce que le fil rend

- Les cinq pièces consolidées, contrôles de la machine à zéro anomalie ou anomalies déclarées une à une.
- Une table : division → date avant → date après → motif.
- Entrées de registre titrées et datées, sans numéro (A-282) ; une entrée de journal ; une ligne à `methode/sas.md` si un sas s’ouvre.
- Commit sur sa branche, push ; la liste des branches distantes restantes avec leur état.
