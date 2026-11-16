# Passation — simulateur et liasse de crédits, 20261116

**Porteur** : fil Code du simulateur « Reprenez votre argent » (12 au 16 novembre 2026).
**Objet** : ce que ce fil laisse, la marche à suivre pour la liasse de crédits, et trois
mandats prêts à coller. Tout ce qui suit est *relevé* le 20261116 sur les deux dépôts, sauf
mention contraire.

---

## 1. Compte rendu du fil

### Ce qui est fait et en ligne

| objet | état relevé |
|---|---|
| Simulateur `Site-ETNP/site/reprenez.html` | en ligne, lié depuis aucune page ; 21 postes ; 2 400 € par défaut ; 600 € par mois à 2 400 € nets |
| Classeur `Synthèse des chiffrages.xlsx` | total 236,402 Md€ ; première année 129,459 ; fonctionnement de l'État 3,8 |
| Classeur `Dépenses de l'État.xls`, `SynthèseR` | E7 et F7 à 85 % hors entretien des routes (233 et 51 M€) ; H8 complété ; neuf cellules changées |
| Classeur `Séries des graphiques.xlsx`, `Graph236` | aux montants de l'Annexe ; graphique redessiné, tuiles à l'entier |
| Liasse `LIASSE_PLF_P2.md`, amendement n° 4 | programme 203 : 280 425 204 € d'AE, 233 985 619 € de CP ; l'entretien des routes n'est plus retiré |
| `REF_doctrine.json`, `controle_arithmetique.py`, `sources_chiffres.py` | à 236,402 ; contrôle arithmétique sans échec |
| `referentiels/simulateur_elements_20261112.tsv` | 505 éléments, 21 postes, 129,46 et 236,40 Md€ |

### Règles du simulateur arrêtées par l'auteur dans ce fil

- Trois étapes : 1 « Votre salaire net actuel », 2 « Vous gagnez », 3 « Quand l'État
  économise, vous y gagnez ». Fond clair. Cadres ronds. Pas de fenêtre : tout s'ouvre sur place.
- Tout est proportionnel au salaire, **sauf** le rendement du patrimoine, égal par personne :
  stock du classeur (607 Md€) / 68 millions, à **3,2 %**. Le total est l'arrondi de la somme.
- Pas de décimale de milliard dans la communication. Pas de centimes. Toujours l'unité.
- Pas de tournure introductive (« là où », « ce qui », « ce que »). Mots signifiants.
- L'arbre suit le statut, non la taille. Une entrée par ministère, « ministère : ce qui y est
  coupé », nommée d'après les actions du PAP ; « Autres » en dernier.
- L'entretien des routes nationales reste à l'État. Le poste garde 3,8 Md€ : 85 % du reste.

### Ce qui reste ouvert

1. **Liasse de crédits** : les 22 amendements « Retirer les crédits » n'appliquent ni socle ni
   rythme (43,69 Md€ d'AE retirés). Voir § 2.
2. **Simulateur, revue bloc par bloc** : Ministères fait ; restent Agences, Associations,
   niches communes aux revenus et aux sociétés, patrimoine (le flux affiche 19 Md€, la carte
   18), Agents publics (même règle « une entrée par ministère » à appliquer).
3. **Trois taux pour le rendement du patrimoine** : 3,2 % au simulateur, 3 % au livre et à
   `D7-2-2-e2`, 2,9 % au classeur des chiffrages.
4. **Accroche de l'accueil** : « Vous rendre 25 % de votre salaire — C'est possible, par ici → »
   vers le simulateur, à poser en fin de revue, en vérifiant que la ligne loge.
5. **Seuils et lignes du bloc « En échange »** (1 800 et 3 500 €) : proposés, non validés.
6. **Classeur de suivi des dépenses de l'auteur** : hors dépôt, non aligné sur l'amendement n° 4.
7. **Dérivés du référentiel de doctrine** : non régénérés, le manuscrit n'étant pas au conteneur.

### Écarts de procédure de ce fil, dits

- Il a touché `methode/` et deux modules partagés d'`appareil/` pendant qu'un autre fil
  renommait les classeurs du site : la règle « un fil qui touche `methode/` est seul » n'a pas
  été tenue. La fusion a été résolue le 20261116, sans perte relevée.
- `make coffre` et `make restauration` n'ont pas tourné (clone `droit` absent) : les empreintes
  de `REF_doctrine.json`, `controle_arithmetique.py` et `sources_chiffres.py` ont été relevées
  à la main.
- L'amendement n° 4 a été corrigé à la main dans le markdown, le classeur de suivi qui
  alimente `generer_liasse_p2.py` n'étant pas au dépôt.

### Branches distantes au 20261116

`Resolution-2027` : `dreamy-planck-ocma2l` et `pensive-mayer-c4pyn3` fusionnées ;
`beautiful-curie-xzsshi` en avance de 1 (20261106) ; `funny-faraday-260skj` en avance de 7
(20261111) ; `retrait-liasses-20261012` en avance de 101 (20261015) ; `bold-fermi-spo7c6` et
`clever-euler-rbeck4` en avance de 158 et 175 (octobre).

`Site-ETNP` : fusionnées — `dreamy-planck-ocma2l`, `classeurs-renommes-20261116`,
`ordre-classeurs-20261116`, `great-archimedes-kkeg6u`, `keen-galileo-325862`,
`laughing-newton-78wl2o`, `sauvegarde-avant-senateurs`, deux `ccr-…` ; en avance —
`bold-fermi-spo7c6` (1), `clever-euler-rbeck4` (2), et quatre branches de septembre et
d'octobre (28 à 60 commits).

---

## 2. La liasse de crédits : ce qui est au dépôt, ce qui n'y est pas

**Au dépôt, et suffisant pour la règle** : `livrables/registre_calcul_etatB.md` (§ 1 la chaîne,
§ 3 le résiduel, § 4 le tableau des 27 lignes avec socle, rythme, date et fraction, § 14 la
table de passage ligne → programme × catégorie), `livrables/registre_exceptions_dates.md`,
`reference/regles_credits.md`, `referentiels/etatB_2027_bg.tsv`,
`referentiels/ratios_cp_ae_pap2026.tsv`. L'assiette au grain de l'action est dans
`Site-ETNP/site/donnees/Dépenses de l'État.xls`, onglet `Données PAP 2026`.

**Pas au dépôt** : le classeur de suivi (`A — Crédits`), que `chaine_credits.py` et
`generer_liasse_p2.py` prennent pour entrée.

**Deux calendriers se contredisent, et c'est la raison de repasser par le projet** :

| ligne | registre § 4 | `chaine_credits.py`, par catégorie |
|---|---|---|
| D37 charges courantes | 1er janvier, 12/12 | catégorie 31 : 1er juillet, 6/12 (« arbitrage du 20261016 ») |
| D29 hébergement d'urgence | 1er avril, 9/12 (exception inscrite) | catégorie 64 : 1er janvier, 12/12 |
| D12 Ademe | 1er juillet, 6/12 | catégorie 32 : 1er janvier, 12/12 |

**Marche à suivre.** Trois temps, dans cet ordre, chacun dans son lieu :

1. **Projet** — arrêter la table des paramètres ligne par ligne et trancher les calendriers,
   pièces en main (classeur de suivi, pièces du dépôt 2027). Rien ne se calcule ici.
2. **Fil Code, seul sur `methode/` et `appareil/`** — confronter (retrouver la liasse actuelle
   à l'euro), appliquer la table, régénérer les 22 amendements, contrôler, poser sur le site.
3. **Fil Code simulateur** — reprendre la revue bloc par bloc, après fusion du fil 2 s'il
   touche les mêmes classeurs.

---

## 3. Mandat pour le projet — méthode et paramètres de la liasse de crédits

> **Objet.** Arrêter, avant tout calcul, la table des paramètres de la liasse de crédits du
> PLF 2027, seconde partie, et trancher ses calendriers. Tu ne modifies aucun amendement.
>
> **Le constat qui motive le mandat** (registre, entrée « Audit des canaux », 20261116). Les 22
> amendements « Retirer les crédits que la présente loi interrompt » de
> `livrables/depot_2027/LIASSE_PLF_P2.md` retirent 43,69 Md€ d'autorisations d'engagement. Les
> lignes recalculées depuis `Données PAP 2026` tombent à l'euro sur le montant brut, multiplié
> par la seule fraction d'exercice : ni socle, ni rythme. Exemples : aide médicale de l'État
> 608 150 000 € pour 547 335 000 attendus ; hébergement d'urgence 3 045 085 425 € pour 1,88 Md€ ;
> programme 103, 7 558 550 632 €. Cause lue à `appareil/chaine_credits.py` : il tient le socle
> et le rythme pour « déjà appliqués » à la table A du classeur de suivi.
>
> **À faire, dans l'ordre.**
> 1. Ouvre le classeur de suivi des dépenses, onglet `A — Crédits`. Dis si les colonnes « AE
>    arrêtées » et « CP arrêtés » portent le socle et le rythme, sur trois lignes : programme
>    183 catégorie 61, programme 177 catégorie 64, programme 203 catégorie 31. Relevé, pas
>    déduction.
> 2. Lis `livrables/registre_calcul_etatB.md` § 1, § 3, § 4 et § 14,
>    `livrables/registre_exceptions_dates.md`, et les dates écrites dans les pièces de
>    `livrables/depot_2027/P2/`. Dresse **une table, une ligne par ligne doctrinale portée par
>    l'état B** : programme, catégorie, action s'il en faut une, source de l'assiette, socle, « F
>    net ou brut », rythme, date d'effet 2027, fraction, résiduel de CP, pièce porteuse.
> 3. Pour chaque ligne, confronte la date du registre § 4, celle du registre des exceptions,
>    celle de la pièce, et celle que `chaine_credits.py` donne à la catégorie (`DATE_CAT`).
>    Liste les contradictions. Trois sont déjà relevées : D37 (1er janvier contre 1er juillet),
>    D29 (1er avril contre 1er janvier), D12 (1er juillet contre 1er janvier).
> 4. Pose à l'auteure, en questions fermées et dans ses mots, ce que la table ne tranche pas.
>    Au moins : un amendement par mission ou par ligne ; quelle date l'emporte quand le registre
>    et la chaîne diffèrent ; D37 à 85 % hors entretien des routes nationales (233 et 51 M€) ;
>    le sort des lignes marquées « due » ou « prorata ».
> 5. Verse au dépôt : `referentiels/liasse_credits_parametres_<date>.tsv` et sa note de
>    lecture, et, si le classeur de suivi reste la source de l'assiette, son onglet `A —
>    Crédits` en TSV. Sinon écris que l'assiette se lit à `Données PAP 2026`.
>
> **Garde-fous.** Chaque phrase dit si elle est relevée, héritée ou déduite. Aucun chiffre ne
> s'écrit sans être recompté sur la pièce. Une borne lue dans un document de méthode se
> vérifie au registre avant d'être redite. Entrées de registre titrées et datées, sans numéro.
>
> **Rendu.** La table, la liste des contradictions de dates, les questions et leurs réponses,
> le chemin des fichiers versés.

---

## 4. Mandat pour un fil Code — régénérer la liasse de crédits

> **Objet.** Recalculer les 22 amendements « Retirer les crédits que la présente loi
> interrompt » de `chantier/livrables/depot_2027/LIASSE_PLF_P2.md` selon la table des
> paramètres arrêtée par le projet, régénérer la liasse et la poser sur le site. Tu es seul sur
> `methode/` et `appareil/` pendant ce fil.
>
> **Lis d'abord** : `chantier/CLAUDE.md` ; `chantier/methode/etats/PASSATION_simulateur_liasses_20261116.md` ;
> les deux entrées du 20261116 de `methode/arbitrages.md` (« Liasse du PLF, amendement n° 4 »
> et « Audit des canaux ») ; `referentiels/liasse_credits_parametres_<date>.tsv` et sa note.
> Si ce dernier fichier n'existe pas, arrête-toi et dis-le : le mandat du projet n'est pas rendu.
>
> **Ce qui est déjà établi, à ne pas refaire.**
> - La ligne du programme 203 se retrouve à l'euro depuis `Site-ETNP/site/donnees/Dépenses de
>   l'État.xls`, onglet `Données PAP 2026` (colonnes AE et CP, catégories), par les règles de
>   `appareil/chaine_credits.py` : fraction par catégorie, résiduel, `CP = min(CP, AE)`.
> - `node appareil/liasse2docx.js` puis LibreOffice redonnent le PDF en ligne page pour page,
>   à condition d'installer EB Garamond et d'aliaser « Garamond » vers elle (fontconfig).
> - L'amendement n° 4 exclut déjà l'entretien des routes nationales (action « Routes –
>   Entretien » du programme 203, catégories 31 et 5x).
>
> **À faire, dans l'ordre.**
> 1. **Confronter.** Recalcule depuis le PAP, sans socle ni rythme, les 22 amendements tels
>    qu'ils sont, programme par programme. Rends le compte des lignes retrouvées à l'euro et la
>    liste de celles qui ne le sont pas, avec l'écart. Ne corrige rien avant ce compte.
> 2. **Appliquer.** Écris le calcul qui lit la table des paramètres : assiette × (1 − socle) ×
>    rythme × fraction ; CP par le résiduel ; minoration ≤ crédit ouvert à
>    `referentiels/etatB_2027_bg.tsv`. Corrige la prémisse fausse de l'en-tête de
>    `chaine_credits.py`.
> 3. **Éprouver.** Quatre lignes témoins doivent tomber sur le registre : aide médicale de
>    l'État 547 335 000 € d'AE (ou la valeur de la table), hébergement d'urgence, charges
>    courantes à 85 % hors routes, programme 103. Un contrôle qui ne peut pas échouer ne prouve
>    rien : fais-le échouer une fois sur une faute injectée.
> 4. **Régénérer** le markdown, le docx et le PDF. Compare le PDF à l'ancien page à page et
>    rends la liste des pages changées. Les renvois `#page=` de `Site-ETNP/site/propositions.html`
>    doivent tenir ; s'ils bougent, rends la table des décalages avant de toucher le site.
> 5. **Contrôler** : `controle_credits_liasse.py`, `controle_liasses.py`, `make index`.
> 6. **Verser** : dépôt de travail par pull request ; `Site-ETNP/site/amendements/` par pull
>    request (fusion = mise en ligne) ; `python3 outils/liens.py` à 0 défaut. Ne lance jamais
>    `make publier`.
> 7. **Inscrire** : une entrée de registre titrée, datée, sans numéro, qui distingue relevé,
>    hérité et déduit ; le journal ; les empreintes des fichiers d'`appareil/` touchés.
>
> **Ce qui se présente à l'auteure dans la conversation avant d'être versé** : le total retiré
> avant et après, mission par mission ; toute ligne où la table ne suffit pas.
>
> **Rendu.** Compte de confrontation, totaux avant et après, pages changées, liens des pull
> requests, liste des branches distantes restantes avec date et état.

---

## 5. Mandat pour un fil Code — reprise du simulateur

> **Objet.** Reprendre la revue bloc par bloc du simulateur « Réduisez l'État, reprenez votre
> argent » avec l'auteure, puis le brancher sur le site.
>
> **Lis d'abord** : `Site-ETNP/CLAUDE.md` et `README.md` ;
> `Resolution-2027/chantier/methode/etats/PASSATION_simulateur_liasses_20261116.md`, § 1 ;
> `chantier/referentiels/simulateur_elements_20261112_lisez_moi.md` ; les entrées de registre
> des 20261112 à 20261116 dont le titre commence par « Simulateur ».
>
> **Où sont les choses.** La page : `Site-ETNP/site/reprenez.html` (en ligne, liée depuis
> aucune page). Ses données sont produites par `python3 outils/restitution.py` depuis
> `site/donnees/Synthèse des chiffrages.xlsx`, `Dépenses de l'État.xls`, `Agences
> publiques.xlsx`, `Niches fiscales.xls`, `Dépenses locales.xlsx` et la carto ; elles ne
> s'éditent pas à la main. Les tables qui décident de l'arbre sont dans cet outil : `ARBRE`,
> `BLOCS_MINISTERES`, `ACTIONS_GARDEES`, `HYPOTHESES`. `--tsv <dossier>` écrit le référentiel
> du dépôt de travail.
>
> **État.** 600 € par mois à 2 400 € nets. Bloc Ministères revu : dix entrées « ministère : ce
> qui y est coupé », « Autres ministères » en dernier.
>
> **Reste à revoir, dans cet ordre, en questions courtes à l'auteure.**
> 1. Agences (13 Md€) : trois thèmes et deux lignes isolées au même niveau.
> 2. Agents publics : le poste de l'État est rangé par ministère puis par programme ; lui
>    appliquer la règle des Ministères.
> 3. Associations (9 Md€) : aide au développement, hébergement, asile, culture, politique de
>    la ville dans une même liste.
> 4. Niches : « Communes revenus et sociétés » apparaît des deux côtés, pour moitié.
> 5. Patrimoine : le flux affiche 19 Md€ (607 Md€ à 3,2 %), la carte 18 ; trois taux coexistent.
> 6. Bloc « En échange » : seuils de 1 800 et 3 500 €, lignes par tranche, non validés.
> 7. En dernier : accroche de l'accueil, « Vous rendre 25 % de votre salaire — C'est possible,
>    par ici → » vers le simulateur ; vérifier que la ligne loge sur téléphone ; image d'aperçu.
>
> **Règles de l'auteure, à tenir sans les redemander.** Réponses courtes, en français, sans
> émoji ni offre. Ce qui est à valider se montre en clair dans la conversation. Pas de
> tournure introductive ; des mots signifiants. Toujours l'unité. Pas de décimale de milliard,
> pas de centimes. Peu de corps de police, peu de lignes, pas de détail inutile. L'arbre suit
> le statut et la nature de la dépense, lue à l'action du PAP, jamais l'intitulé de
> communication du programme. Rien ne bouge hors de la consigne ; un effet de bord se signale
> avant.
>
> **À chaque lot.** `python3 outils/restitution.py` ; `python3 outils/onglets.py` puis
> `python3 outils/renvois.py` si un classeur change (dans cet ordre) ; `python3 outils/liens.py`
> à 0 défaut ; `node outils/capture.mjs reprenez` ; un parcours joué dans Chromium sur
> ordinateur et téléphone (gain à 1 478, 2 400 et 5 000 €, aucune erreur de script, aucun
> débordement) ; pull request vers `main`, fusion, vérification sur france-resolution.fr. Si le
> référentiel change : `--tsv`, note de lecture, registre, pull request au dépôt de travail.
>
> **Pièges relevés.** Un classeur `.xls` ne repasse pas par LibreOffice (il ne connaît pas
> `XLOOKUP`) : `outils/retoucher_depenses.py` montre la retouche en place. `onglets.py` efface
> les blocs de renvois : `renvois.py` se rejoue après. Une autre session peut modifier `main`
> pendant le fil : relire `origin/main` avant chaque fusion.
>
> **Rendu de chaque bloc.** Ce qui change à l'écran, les montants concernés, ce qui reste à
> trancher.
