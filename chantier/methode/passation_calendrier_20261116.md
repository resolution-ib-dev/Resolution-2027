# Passation — calendrier de mise en œuvre, état des lieux du projet, 20261116

**Porteur** : fil Cowork d'état des lieux, 20261116. **Destinataire** : fil code de pilotage.
**Mandat** : l'auteure, 20261116 — retrouver et rendre ce que le projet porte sur le calendrier de
mise en œuvre, sans rien produire de neuf ; puis « cr et zip passation ».
**Mesuré sur** : le projet Claude (99 documents, 9 pièces jointes soit 62 onglets, mémoire du
projet) et le dépôt `Resolution-2027`, `main` à `088112c`, 2 110 commits.
**Provenance** : tout énoncé est *relevé* dans ce fil, sauf mention *hérité*. Rien n'est
reconstruit de mémoire.
**Domicile proposé au dépôt** : `chantier/methode/passation_calendrier_20261116.md`.

---

## 1. Résultat

**Le tableau mesures × mois est introuvable**, au projet comme au dépôt. Trois pièces le déclarent
perdu : `CLAUDE.md` du projet, `methode/passation_20261015.md` § 4,
`livrables/flux_par_agent_20261015.md`.

**Trois noms de fichiers sont à rechercher hors des deux surfaces.** Aucun n'est au projet, aucun
n'est dans l'arbre du dépôt, aucun commit de `main` ne les porte.

| fichier | qui le nomme | ce qui en est dit |
|---|---|---|
| `etats/suivi_calendrier_flux.tsv` | `methode/etats/L2.md` (revue du 20261005) ; `methode/etats/CALCUL_etatB_20261009.md` § 12 | « Suivi mensuel par flux et par agent, à auditer en fin de revue » ; « déclarées au corpus et jamais ouvertes […] Si leur trajectoire diffère de celle du registre, c'est la leur qui fait foi » |
| `etats/suivi_mensuel_2027_restitution.tsv` | mêmes pièces | idem |
| `livrables/suivi_effets_mensuels_2027.md` | `methode/passation_20261009.md` § 1 ; en-tête du registre | absorbé par le registre et supprimé le 20261009 |

Ce fil ne lit pas les conversations d'origine. La recherche est à la main de l'auteure.

**Ce qui s'approche du tableau perdu**, sans être par mesure et par mois : 27 mesures × 4 exercices
(registre § 5) · 8 agents × 12 mois 2027 (registre § 6) · 8 agents × 48 mois
(`referentiels/Flux_par_agent_20261015.xlsx`, onglet « Mensuel par agent ») · 7 pans × 16 trimestres
(registre § 16).

---

## 2. Ce que le zip porte

Dix-sept fichiers à plat, noms sans accent ni espace. `00_SHA256SUMS.txt` permet le contrôle
d'un geste : `sha256sum -c 00_SHA256SUMS.txt`.

**Les neuf pièces jointes du projet, en copie d'octets** — aucune n'est au dépôt.

| fichier du zip | nom exact au projet | octets | SHA-256 |
|---|---|---:|---|
| `10_Suivi_depenses_credits_et_vecteurs_20261007.xlsx` | `Suivi dépenses — crédits et vecteurs_20261007.xlsx` | 220 140 | `3411f9650dbd51047c93ed2467a1af8b41bb7f3e25dba1571230c18b29d32c30` |
| `11_Synthese_Calculs_Resolution_0910.xlsx` | `Synthèse Calculs Résolution_0910.xlsx` | 352 149 | `3264cd06e973d16e1bf3e374da6f59733411fc6be081cea6f019ead1783ac44d` |
| `12_PLF26_Depenses_2026_BG_BA_destination_nature_0910.xls` | `PLF26 - Depenses 2026 du BG et des BA selon nomenclatures destination et nature_0910.xls` | 1 543 168 | `cbc2dda7e603e3daa93be1748a7db6ac6b60e7dec92b7550e4941f5ebf0f2762` |
| `13_PLF2026_VM_tome_I_Annexe_2_Taxes_affectees_0910.xls` | `PLF 2026_VM tome I - Annexe 2 - Taxes affectees_0910.xls` | 209 920 | `bda4d27671b67e8bfe65cf6531bdb2ed23d03272efc1fe0203be31f2f6dfafb4` |
| `14_PLF2026_VM_tome_II_Annexe_3_Depenses_fiscales_0910.xls` | `PLF 2026_VM tome II - Annexe 3 - Depenses fiscales - 0910.xls` | 1 286 144 | `6d89483a7c467f028fded9cf083d43ca2c0ae96cb4dd89f351400209fd22fb29` |
| `15_Synthese_ETP_et_agences_Resolution_0910.xls` | `Synthèse ETP et agences Résolution_0910.xls` | 495 104 | `9782a2c220a288c06e4af9c5a752de454017b48e0063453673fe46304b97b455` |
| `16_Synthese_Graphiques_Resolution_0910.xlsx` | `Synthèse Graphiques Résolution_0910.xlsx` | 173 343 | `a8a6f04ade72fc3b5d9c3cf589dbba524b65ca5de7fe06037a0fd9a241d59654` |
| `17_T_3305_APUL_Resolution_0910.xlsx` | `T_3305_APUL_Résolution_0910.xlsx` | 192 604 | `7b31996972e52198eb442d7e4e6b45aa606a1f31755e6a1df25ec2871bea571b` |
| `18_deppee2025_depense_education_251219IB.xlsx` | `deppee2025donneesfiche09ladepensepourleducation25 12 19IB.xlsx` | 308 070 | `a9d1e34c703cce7cc41ad925180becba8d4994d16b2b91788a289efe87025dbe` |

**Six onglets rendus en texte**, pour lecture sans outil. Première colonne : numéro de ligne de
l'onglet ; en-tête : lettres de colonne ; valeurs telles que stockées, sans arrondi ; lignes vides
omises. Le compte de cellules non vides de chaque fichier a été contrôlé égal à celui de l'onglet.

| fichier du zip | classeur | onglet | lignes × colonnes | cellules |
|---|---|---|---:|---:|
| `20_tsv_synthese_calculs__Detail_Economies.tsv` | `11_…` | `Détail Economies` | 43 × 22 | 254 |
| `21_tsv_synthese_calculs__Flux.tsv` | `11_…` | `Flux` | 23 × 10 | 154 |
| `22_tsv_suivi_depenses__Mesure.tsv` | `10_…` | `Mesure` | 40 × 3 | 84 |
| `23_tsv_suivi_depenses__A_Credits.tsv` | `10_…` | `A — Crédits` | 720 × 15 | 10792 |
| `24_tsv_suivi_depenses__B1_taxes_affectees.tsv` | `10_…` | `B1 — Vecteur taxes affectées` | 280 × 16 | 4054 |
| `25_tsv_suivi_depenses__B2_depenses_fiscales.tsv` | `10_…` | `B2 — Vecteur dépenses fiscales` | 467 × 20 | 9317 |

Les classeurs ne se versent pas au dépôt (règle A-235, *héritée*) : ils servent à la lecture.

---

## 3. Les classeurs du projet ne sont pas ceux que le pilotage a lus le 20261116

Colonne de droite *héritée* de `referentiels/parametres_credits_20261116_lisez_moi.md` § 1 et § 2.

| | pièce jointe du projet | classeur lu par le pilotage |
|---|---|---|
| synthèse — nom | `Synthèse Calculs Résolution_0910.xlsx` | `Synthèse des chiffrages.xlsx` (site, `/donnees/`) |
| synthèse — taille | 352 149 octets | 344 594 octets |
| synthèse — SHA-256 | `3264cd06…783ac44d` | `ac56012f…e64e84a` |
| synthèse — `Flux`!C6, gain année 1 | **129,4** | **129,459** |
| synthèse — `Flux`!G6, total supprimé à terme | **226,2** | **227,445** |
| dépenses — nom | `PLF26 - Depenses 2026 du BG et des BA…_0910.xls` | `Dépenses de l'État.xls` (site) |
| dépenses — taille | 1 543 168 octets | 1 543 168 octets |
| dépenses — SHA-256 | `cbc2dda7…ebf0f2762` | `8a4a08fd…a566dd` |
| suivi des dépenses | `Suivi dépenses — crédits et vecteurs_20261007.xlsx` | déclaré absent |

Les deux classeurs de dépenses ont la même taille et des empreintes différentes. Le registre
§§ 4 et 5 cite `Synthèse Calculs Résolution_0910.xlsx`. Ce fil n'a comparé aucune paire cellule à
cellule : les classeurs du site ne sont pas au projet. Les deux séries sont maintenant côte à côte
chez le pilotage.

Consigne de l'auteure qui s'y rapporte, 20261007 (*héritée*, mémoire du projet) : « ce qui fait foi,
ce sont les classeurs Excel détaillés, pas les classeurs de publication qui les recopient ».

---

## 4. Écarts mesurés

**Vue du projet contre registre §§ 4, 5 et 6** — comparaison mécanique, cellule à cellule : **aucun
écart de valeur** sur 27 lignes. Écarts de forme seulement : deux colonnes de plus au registre § 4
(« 2027 au 20261008 », « pièce »), une ligne de plus au § 5 (« solde au 20261008, double socle »),
neuf libellés abrégés dans la vue.

**`livrables/flux_par_agent_20261015.md` contre `Flux_par_agent_20261015.xlsx`** — 180 valeurs
comparées, annuel et trimestriel : aucun écart au-delà du centième, sept arrondis au demi-centième.
Le titre de la pièce annonce « mesure × agent × mois » ; elle ne porte ni tableau mensuel ni
tableau par mesure.

**Un même chiffre sous trois formes** : ménages sans revenus d'activité, 2027 — −2,42 (registre § 6,
vue § 3), −2,43 (`flux_par_agent`, `passation_20261015`), −2,425 (classeur).

**Registre § 18** : `methode/sas_machine_tri_porte_20261103.md`, au projet, le porte dans son état
du 20261105 (P1 n° 36 à 38, 27 rangs non chiffrés). Le dépôt porte l'état recompté le 20261106 et
regroupé le 20261109. Montants identiques.

### La montée en charge du classeur contre celle du registre

Classeur joint au projet, onglet `Détail Economies` : colonne D « Restitué en CSG » (année 1),
colonne E « Solde à restituer », colonne F « Total supprimé ». Registre §§ 4 et 5, dépôt. Md€.

| cel. | ligne du registre | rythme au registre | classeur, année 1 (D) | classeur, en sus à terme (E) | classeur, total (F) | registre 2027 | registre 2028 | registre 2028 − classeur année 1 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| D5 | France Compétences / CPF | ⅓ | 3,8 | 6,7 | 10,6 | 3,53 | 7,07 | +3,27 |
| D6 | France Travail | ⅓ | 2,2 | 3,055 | 5,255 | 1,46 | 3,50 | +1,30 |
| D12 | Ademe | ⅓ | 0,3 | 0,6 | 0,9 | 0,15 | 0,45 | +0,15 |
| D15 | MaPrimeRénov' | 1 | 1,3 | 0 | 1,3 | 1,17 | 1,17 | −0,13 |
| D16 | Autres opérateurs | 1 | 2,6 | 0,2 | 2,745 | 1,37 | 2,75 | +0,15 |
| D18 | Aide au logement | ⅓ | 5,4 | 10,7 | 16,1 | 2,68 | 8,05 | +2,65 |
| D19 | Aide médicale de l'État | 1 | 1,1 | 0 | 1,1 | 0,55 | 1,10 | 0,00 |
| D20 | Chèque énergie | 1 | 0,6 | 0 | 0,6 | 0,30 | 0,60 | 0,00 |
| D22 | Autres ménages | 1 | 0,9 | 0,1 | 1 | 0,50 | 1,00 | +0,10 |
| D24 | Audiovisuel public | 1 | 3,8 | 0 | 3,8 | 1,90 | 3,80 | 0,00 |
| D25 | Emploi et apprentissage | 1/6, déjà net de la date | 2,3 | 4,6 | 6,9 | 1,15 | 4,60 | +2,30 |
| D26 | France 2030, entreprises | ⅓ | 1,1 | 2,1 | 3,2 | 1,07 | 2,13 | +1,03 |
| D27 | Autres entreprises | 1 | 1,2 | 0,1 | 1,3 | 1,30 | 1,30 | +0,10 |
| D29 | Hébergement d'urgence | 1 | 2,5 | 0 | 2,5 | 1,88 | 2,50 | 0,00 |
| D30 | Aide publique au développement | ⅓ | 1 | 2 | 3 | 0,50 | 1,50 | +0,50 |
| D31 | Immigration et asile | 1 | 0,9 | 0 | 0,9 | 0,45 | 0,90 | 0,00 |
| D32 | Aide à l'emploi et à l'insertion | ⅓ | 0,8 | 1,5 | 2,3 | 0,77 | 1,53 | +0,73 |
| D33 | France 2030, associations | ⅓ | 0,5 | 1,1 | 1,6 | 0,27 | 0,80 | +0,30 |
| D34 | Subventions culturelles | 1 | 0,5 | 0 | 0,5 | 0,25 | 0,50 | 0,00 |
| D35 | Politique de la ville | 1 | 0,4 | 0 | 0,4 | 0,20 | 0,40 | 0,00 |
| D36 | Autres associations | 1 | 1,4 | 0 | 1,4 | 0,70 | 1,40 | 0,00 |
| D37 | Charges courantes et achats | 1 | 3,8 | 0 | 3,8 | 3,80 | 3,80 | 0,00 |
| D38 | Départs de fonctionnaires de l'État | 1 | 0,9 | 2,1 | 3 | 1,50 | 3,00 | +2,10 |
| D40 | Dépenses culturelles des collectivités | 1 | 11,6 | 0 | 11,6 | 11,60 | 11,60 | 0,00 |
| D41 | Collectivités — aides aux entreprises | ⅓ | 9,7 | 2,6 | 12,3 | 4,10 | 8,20 | −1,50 |
| D42 | Collectivités — charges courantes | ⅓ | 6,1 | 3,5 | 9,6 | 3,20 | 6,40 | +0,30 |
| D43 | Collectivités — départs | 1 | 6 | 14 | 20 | 10,00 | 20,00 | +14,00 |
| | **27 lignes** | | **72,7** | **54,955** | **127,7** | **56,35** | **100,05** | **+27,35** |

Les valeurs du classeur sont rendues à trois décimales au plus ; les sommes du registre sont celles des 27 lignes affichées (56,35 pour 56,34 au total du § 4, arrondi d'affichage).

**Lecture, sans conclusion.** Le régime plein concorde : 127,7 contre 127,57, l'écart étant le socle
de D15. Les deux pièces ne montent pas au même pas.

- **Départs d'agents, D38 et D43.** Le classeur compte 30 % en année 1 (0,9 sur 3 ; 6 sur 20) et le
  reste à terme ; l'onglet `Flux` écrit « Transfert des agents publics (compensés à 70 %) vers les
  actifs ». Le registre les compte au rythme 1 dès le 1er juillet 2027 : 3,00 et 20,00 en 2028.
  **Écart : 16,1 Md€ en 2028.** D38 est déjà relevé par
  `referentiels/parametres_credits_20261116.tsv` (« registre 1.000, classeur 0.300 ») ; **D43, hors
  crédits de l'État, ne l'est pas**.
- **Deux lignes où le registre est sous le classeur** : D41, 8,20 en 2028 contre 9,7 en année 1 ;
  D15, 1,17 contre 1,3, écart de socle.
- **L'exercice auquel l'« année 1 » du classeur se compare n'est fixé par aucune pièce du projet.**
  Convention de l'auteure (*héritée*, mémoire du projet) : « année 1 » désigne l'année pleine, le
  régime de croisière, et non l'année civile du dépôt.

### L'agent qui porte

Les colonnes R à V de `Détail Economies` ne portent une incidence que pour **14 des 27 lignes**.
L'acteur des 13 autres lignes du registre § 4 n'y figure pas : D12, D15, D16, D19, D24, D29, D30,
D31, D34, D35, D36, D37, D42. D38 et D43 y sont en colonne « Actifs » ; le registre écrit « agents
publics ».

---

## 5. Consignes de l'auteure que le dépôt ne voit pas

Mémoire du projet, lignes reprises et abrégées par endroits (*héritées* de fils antérieurs ; seuls
les guillemets sont ses mots).

- **20261005** — « les chiffrages macro, inutiles, on fait juste ceux dont on a besoin, on donne des
  indications vagues quand c'est attendu, et quand il existe le mien vaut. »
- **20261007 — règle de signalement des écarts, calendrier mensuel.** « On fait comme ça vient » :
  un écart en plus ne contredit pas frontalement les estimations annuelles illustratives et ne
  remonte pas. Seuls les moins se signalent — un montant mesuré inférieur à l'affiché, une ligne
  surestimée, un gisement qui se réduit. Corollaire qu'elle pose en même temps : maintenir les
  compteurs mensuels multiagents, c'est ce qui rend la règle tenable d'un fil à l'autre.
- **20261007 — règle de correction** : ce qui compte est le caractère correct au niveau granulaire
  le plus fin, l'agrégation se voit ensuite. Une compensation au niveau agrégé ne vaut pas quitus
  pour la ligne : un écart granulaire se porte aux compteurs et se revoit à la revue globale, même
  quand le total boucle.
- **20261007** — ce qui fait foi, ce sont les classeurs Excel détaillés, pas les classeurs de
  publication qui les recopient. Le travail attendu à partir d'eux : des tableaux de suivi ligne à
  ligne, financiers et juridiques. Ses classeurs fonctionnent chez elle : un défaut constaté sur une
  copie convertie est un défaut de l'instrument de lecture.
- **Règle permanente d'analyse — les montées en charge.** Sur toute mesure budgétaire ou fiscale,
  relever systématiquement l'entrée en vigueur (est-elle au 1er janvier ?) et la trajectoire (le
  flux est-il croissant, court-il au-delà de l'exercice ?). Relevé mécanique obligatoire ;
  restitution seulement là où c'est significatif.
- **Vocabulaire** — « année 1 » désigne l'année pleine, le régime de croisière atteint une fois la
  montée en charge terminée ; une comparaison avec la contrepartie se fait à cette même date, en
  mensualisé.

Documents du projet (*relevés*) :

- `methode/etats/SUIVI_chantier_20261009.md` § 4, tranché entre le 20261008 et le 20261009 : la
  restitution principale ne s'étale pas, les socles cibles ne bougent pas ; le pilotage du
  calendrier se fait sur les rythmes de CP, les pentes de montée en charge et, à la marge, les
  rythmes de refonte fiscale.
- `methode/sas_machine_tri_porte_20261103.md`, 20261103 : « un report sans bonne raison ne tient
  pas » ; 20261105 : « j'ai déjà répondu à tout ».

---

## 6. Ce qui reste ouvert, et qui le porte

| point | porteur |
|---|---|
| rechercher les trois fichiers du § 1 | l'auteure — hors des deux surfaces |
| départs d'agents : le registre s'aligne-t-il sur les 30 % d'année 1 du classeur ? Enjeu 16,1 Md€ en 2028 | l'auteure — question posée le 20261116, réponse attendue |
| quelle série de classeurs fait foi, celle du projet ou celle du site (§ 3) | l'auteure |
| D43 et les trois autres lignes de collectivités, absentes des paramètres de crédits | pilotage |
| acteur de 13 lignes du registre § 4, sans appui au classeur | pilotage |

**Pièce du projet absente du dépôt, non transmise** : `methode/sas_machine_tri_porte_20261103.md`.
C'est un correctif déjà appliqué — le registre § 18 du dépôt en porte le résultat, recompté depuis.
Les dix autres documents du projet lus par ce fil et vérifiés sont au dépôt sous le même nom.

**Non comparé par ce fil** : l'identité à l'octet entre les documents du projet et leurs copies du
dépôt (identiques à la lecture) ; les onglets `B1` et `B2` du classeur de suivi, non confrontés au
dépôt.

---

## Annexe — toutes les pièces du projet qui portent un calendrier, un rythme ou un compteur mensuel

Toutes ouvertes par ce fil. Tailles en lignes × colonnes : hors en-tête pour les tableaux des
documents, plage utile pour les onglets.

| pièce | au projet depuis | tableaux | contenu |
|---|---|---|---|
| `livrables/suivi_trajectoire_20261015.md` | 20261015 | § 1 : 28 × 11 · § 2 : 32 × 5 · § 3 : 9 × 14 · § 5 : 16 × 14 et 6 × 5 · § 7 : 1 × 6, 2 × 5, 4 × 3 | vue du registre §§ 4, 5, 6, 7, 15, 16, 17 ; au dépôt sous le même nom |
| `livrables/flux_par_agent_20261015.md` | 20261015 | clé : 8 × 3 · annuel : 9 × 5 · trimestriel : 9 × 17 | flux par agent 2027-2030 ; au dépôt |
| `methode/passation_20261015.md` | 20261015 | trajectoire : 4 × 4 · annuel par agent : 9 × 5 · trimestriel 2027 par agent : 9 × 6 | le trimestriel 2027 y est une somme de mois arrondis : total −23,01 contre −22,95 ; au dépôt |
| `methode/passation_20261009.md` | 20261009 | aucun | règles de date R-M à R-U résumées ; chiffres d'avant correction du double socle (2028 à −21,6 ; agents à −1,99 et −6,51), à ne pas reprendre ; au dépôt |
| `methode/etats/SUIVI_chantier_20261009.md` | 20261009 | aucun | § 4, arbitrage de calendrier ; au dépôt |
| `methode/sas_machine_tri_porte_20261103.md` | 20261103, contenu au 20261105 | compteurs : 6 × 6 et 2 × 8 · dates : 8 × 5 | correctif portant le registre § 18 ; absent du dépôt |
| `CLAUDE.md` | 20261001, contenu au 20261015 | 13 × 3 | table de ce qui fait foi ; au dépôt |
| `Synthèse Calculs Résolution_0910.xlsx` | 20260917 | `Détail Economies` 43 × 22 · `Flux` 28 × 10 · `CSG-CRDS` 16 × 10 | par mesure : gain année 1, gain à terme, hypothèse de rythme et de socle, incidence par agent. `CSG-CRDS` : montants mensuels par niveau de salaire, aucun calendrier |
| `Suivi dépenses — crédits et vecteurs_20261007.xlsx` | 20261008 | `A — Crédits` 720 × 15 · `B1` 280 × 16 · `B2` 467 × 20 | statut « en 3 ans » par ligne de crédit ; économie à 1 an et au-delà par taxe affectée ; fin du fait générateur et fin d'incidence par dépense fiscale |
| `PLF 2026_VM tome II - Annexe 3 - Depenses fiscales - 0910.xls` | 20260917 | `Echéances` 469 × 12 · `Chiffrages Résolution` 471 × 17 | échéances des dépenses fiscales |
| `PLF26 - Depenses 2026 du BG et des BA…_0910.xls` | 20260917 | `Economies R` 206 × 25 | drapeaux « Oui / En 3 ans » par programme × catégorie |
| `T_3305_APUL_Résolution_0910.xlsx` | 20260917 | `T_3305` 898 × 40 | 22 cellules portent « en 3 ans » ; non lu au-delà |

Balayés sans calendrier : `Synthèse Graphiques`, `Synthèse ETP et agences`, `Annexe 2 — taxes
affectées`, dépense d'éducation. Ils sont au zip pour que la série soit complète.
