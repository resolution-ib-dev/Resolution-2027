# Bilan au fil commanditaire du tri — fil tri-porte, 20261103

*Mandat reçu : « vérification approfondie du tri des prélèvements, relecture des annexes et ajout aux liasses des cas non traités ». Branche `claude/pensive-mayer-c4pyn3` de `Resolution-2027`, rien sur `Site-ETNP`, aucune publication. Chiffres recomptés sur `referentiels/sort_prelevements_20261103.tsv` au moment de l’écrire ; droit relu au millésime LEGI 20261031, version applicable au 1er juillet 2027.*

---

## 1. Où en est chaque objectif du mandat

| § du mandat | objectif | état | pièce |
|---|---|---|---|
| 3 | inscrire les règles des 2 et 3 novembre | **fait** — six devenirs, CSG et CRDS, blocs, ventilation par qui paie, niches, sièges complétés (2 confirmés au dépôt de droit, 4 hors dépôt) | `methode/arbitrages.md`, « 20261103 — tri-porte » |
| 4.2 | 32 écarts > 20 % | **fait** — recomptés à 35 ; les 5 écarts de source corrigés à l’état A ; les 6 révisions > 50 % qualifiées (5 révisions de rendement, 1 changement de périmètre : éolien en mer) | `livrables/tri_prelevements/relecture_annexes_20261103.tsv` |
| 4.3 | 178 rangs sans annexe | **non fait** — 179 au recompte ; les pièces publiques (LFSS annexe 4, rapport sur les prélèvements obligatoires, comptes DGCL) ne sont pas au dépôt | idem, colonne `decision` |
| 4.3 | 44 ressources de l’annexe 2027 sans rang | **fait** — appariées par code de ressource ; 16 rangs ajoutés au tri, les autres sont des fractions ou des homonymes nommés | `relecture_annexes_…`, rapport § 3 |
| 4.3 | sorts contre le schéma (colonne H) | **fait**, écarts expliqués ligne par ligne ; restent à trancher les jeux (6,7 Md€ au tri contre 0,3 au schéma) et les DMTO et DMTG, partiels au schéma et entiers au tri | `sorts_contre_schema_20261103.tsv` |
| 5.1 | vérification des 120 cas | **fait** — voir § 2 | `verification_porteurs_20261103.tsv` |
| 5.1 | contrôle inverse | **fait** — 2 impositions abrogées sans rang, ajoutées ; 2 visas à relire | rapport § 1 |
| 5.1 | niches contre la clause générale | **fait, après correction** — voir § 4 | `niches_clause_generale_20261103.tsv` |
| 5.2 | amendements manquants | **rédigés, en projet** — 5 pièces ; vérification exigeante confiée au fil machine | § 3 |
| 5.3 | points ouverts | **faits** : TSCA fusionnée, papiers graphiques retirés, petit colis au bloc UE ; **non fait** : éclater les 7 agrégats (le tome I digéré ne porte pas leurs composantes) | rapport |
| 6 | nouveau tri, classeur, version exportable | **fait** — 434 rangs ; export contrôlé mécaniquement (0 mention interne, 0 décimale au-delà de 10) | `referentiels/sort_prelevements_20261103.tsv`, `Tri_prelevements_travail_20261103.xlsx`, `Tri_prelevements_export.xlsx` |
| 7 | rapport à l’auteur | **fait**, et récapitulatif avant/après | `rapport_auteur_20261103.md`, `recap_avant_apres_20261103.md` |

---

## 2. Les prélèvements remplacés ou fondus

**Les 120 cas de l’annexe A** : 14 portés par un alinéa des liasses (relevé) · 2 portés par une clause ou par construction (prélèvement de solidarité par le schéma des 30 % du n° 20, ANCOLS par l’abrogation de la PEEC) · 54 portés par les amendements nouveaux · 8 par la voie réglementaire · 7 déjà abrogés au droit en vigueur · 6 sortis du « remplacé » par les réponses de l’auteur · 1 rang retiré · **28 non portés** : 13 suspendus à une qualification, 5 sièges n.d., 3 agrégats, 7 sans siège ou sans disposition d’affectation trouvée.

**Les 297 rangs remplacés ou fondus du tri** : 155 portés · 9 par clause ou construction · 78 par les amendements nouveaux · 11 par la voie réglementaire · 8 déjà abrogés · **36 non portés**. Le recoupement du 3 novembre en comptait 169 portés, dont 34 qui ne l’étaient pas.

**Les 13 qualifications en suspens** (une décision de l’auteur chacune) : médecine du travail · amende FCPR (1763 B, sanction et non prélèvement) · contribution REP emballages · CVO équarrissage · accidents du travail agricoles (1622) · fonds de garantie des soins · UNOCAM (siège douteux) · déshérence (recette non fiscale ?) · droits d’enregistrement génériques (à fusionner avec les DMTO ?) · contribution équivalente aux droits de plaidoirie (liée à la cotisation des avocats, donc liasse ultérieure ?) · deux redevances hydroélectriques · garantie de l’or (extinction à confirmer).

---

## 3. Les amendements touchés

| pièce | nature | contenu | état |
|---|---|---|---|
| P1 n° 25 | **inchangé** | modifié puis rétabli : la taxe aurifère de Guyane, affectée, reste supprimée ; cinquante-sept impositions | identique à l’original |
| P1 n° 35 | nouveau, art. 15 | suppression du troisième exercice de la contribution exceptionnelle | en projet |
| P1 n° 36 | nouveau, après l’art. 19 | 27 impositions d’État (I au 1er juillet 2027, II pour 2028) ; III : Caisse des dépôts à l’IS | en projet |
| P1 n° 37 | nouveau, après l’art. 27 | 18 impositions locales, alignées sur la taxe foncière unique ; casinos au 1er juillet 2027 | en projet |
| P1 n° 38 | nouveau, après l’art. 42 | 13 taxes affectées hors CGI | en projet |
| PLFSS n° 9 | nouveau, après l’art. 14 | 18 contributions sociales | en projet |

Liasses : 81 amendements avant, **86 après** (P1 34 → 38, P2 39, PLFSS 8 → 9). Source unique des textes : `appareil/tri_porte/amendements.py`. PDF et docx du site non régénérés.

**Défauts connus, confiés au fil machine** : deux reports à 2028 sans motif (n° 36, II, 2° ; remontées mécaniques et sites nordiques au n° 37) ; deux divisions « impositions annuelles » à rédiger nommément (n° 38, II, B ; PLFSS n° 9, II, B) ; sept textes cités hors dépôt de droit ; recevabilité financière des pertes de tiers non instruite ; renvois entrants non relevés. Mandat : `methode/prompt_fil_machine_tri_porte.md`.

---

## 4. Ce que le fil a corrigé de lui-même

- **Niches de TVA** : le premier compte (« 38 exclues par le II, 4° ») était faux, fait sur les articles du CGI recodifiés au CIBS au 1er janvier 2027. Corrigé : 28 taux réduits portés par le n° 21, 10 exonérations atteintes par le I, sous réserve du II, 3°.
- **Prélèvement de solidarité** : d’abord abrogé au n° 36, contre l’arbitrage du 20261007 qui en laisse l’articulation à la pièce D ; retiré du n° 36 sur la réponse de l’auteur.
- **Taxe aurifère** : retirée du n° 25 sur une première lecture, rétablie sur la précision de l’auteur.
- **Taxe d’aménagement et TGAP** : sièges mal pris au tri, rétablis au contrôle inverse (1635 quater A et 299 CGI, que les n° 29 et 22 abrogent).

---

## 5. Ce que le commanditaire a à décider ou à lancer

1. **Millésime des rendements** : prévision 2026 du PLF 2026 (état actuel) ou prévision 2026 révisée du PLF 2027 (en colonne d’attente, 118 rangs changent). La réponse « oui » ne choisit pas.
2. **« En R »** : lu comme voie réglementaire pour les redevances. Si c’était recette non fiscale, 11 rangs basculent.
3. **Les 13 qualifications** du § 2.
4. **Les deux écarts au schéma** : jeux (le tri supprime, le schéma ne retient que 0,3 Md€) ; DMTO et DMTG partiels au schéma.
5. **TVA** : fin des taux réduits au 1er juillet 2027 aux exposés des n° 22 et 25, au 1er juillet 2028 au dispositif du n° 21.
6. **Lancer le fil machine** sur `methode/prompt_fil_machine_tri_porte.md`, puis valider les cinq pièces qu’il rendra.
7. **Verser les pièces publiques manquantes** si les 179 rangs sans annexe doivent être sourcés : LFSS annexe 4, rapport sur les prélèvements obligatoires, comptes DGCL ; et les fiches détaillées du tome I pour éclater les 7 agrégats.
8. **Promouvoir le tri** : `sort_prelevements_20261103.tsv` ne devient la référence (au lieu du 20261015, encore défaut de `controle_sieges_prelevements.py`) qu’après validation.

---

## 6. Contrôles au versement

Sièges : 0 échec, 10 signaux déclarés. Crédits : 0 anomalie bloquante. Index : 0 anomalie bloquante. `make controle` : arrêt antérieur au fil (commit `7c2ed1d` absent du clone superficiel), inchangé ; lexique : 5 livrables de plus en anomalie, tous sur l’accroche commune « prélèvements obligatoires ».
