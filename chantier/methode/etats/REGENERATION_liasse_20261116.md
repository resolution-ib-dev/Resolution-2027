# Régénération de la liasse de crédits, PLF 2027, seconde partie — 20261116

**Porteur** : fil d'exécution « liasse-régénération », branche `claude/liasse-regeneration`, lancé par le pilotage.
**Mandat** : pilotage, 20261116 — régénérer les 22 amendements « Retirer les crédits » ; puis, par quatre messages du pilotage du même jour : corriger la règle 1 et reconstruire le croisé mesure × mois ; fusionner `main` et intégrer les pièces du projet ; mettre le registre à niveau sur D16, D37, D41, D43 et sur les départs d'agents. Les deux derniers messages ont d'abord été rendus sans exécution, puis exécutés sur le « go » du pilotage, session parente de ce fil (§ 10).
**Convention** : chaque chiffre est *relevé*, *hérité* ou *déduit*. Montants en euros, sauf mention.
**Statut des règles** : *tranché par le pilotage, révocable*. Rien n'est « validé ». La consigne de l'auteure du 16 novembre et sa correction sur le rythme sont **héritées du pilotage** : ce fil ne les a pas lues de l'auteure.

---

## 1. La règle appliquée

> **AE = brut du PAP 2026 × taux d'économie du classeur × rythme du § 4 du registre × fraction d'exercice du § 4.**
> **CP = min (CP ; AE) bruts × le même produit × (1 − résiduel du § 3).**
> **Plafond, par programme : crédit ouvert à l'état B 2027, en AE, en CP et en titre 2 ; CP ≤ AE.**

*Tranché par le pilotage, révocable.* Le mandat initial donnait le rythme au classeur (cible « mixte ») ; la correction du même jour le rend au registre : « le travail détaillé par mesure et par mois fait foi ». Le classeur ne garde la main que sur le brut et le taux. La cible du contrôle s'appelle `projet`.

Cinq précisions, *tranchées en propre* et inscrites à la table, colonne `regle_origine` :

- **Titre 2.** Le § 4 donne à D38 un rythme de 1 ; le § 10 du registre retranche l'indemnité de départ, 70 % (*relevé* : registre § 10, `SynthèseR!D7`, exposé de l'amendement n° 26). Coefficient : 0,90 × 6/12 × 0,30. Inchangé par rapport à la liasse d'avant.
- **France Travail (D6).** Règle du registre : 0,90 × ⅓ × 12/12 × 5/6, soit un quart de la subvention. *Relevé* : 290 727 809 €, le « 290,7 » du § 14.
- **Apprentissage (D25).** « 1/6, déjà net de la date » : aucune fraction ne s'y ajoute.
- **Programme 102, catégorie 32, hors France Travail** (111 950 648 € bruts). Le classeur retranche tout le programme des « autres opérateurs » sans le chiffrer : socle, rythme et date de la ligne D16 du registre.
- **Fonctionnement et investissement (D37).** 85 % hors entretien des routes, au 1er janvier ; résiduel de CP de 15 % (catégorie 31) et de 80 % (titre 5).

## 2. Par amendement, avant et après

*Relevé* sur la liasse du matin (copie de travail) et sur la liasse régénérée.

| n° | mission | AE avant | AE après | CP avant | CP après | programmes avant | après |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Cohésion des territoires | 13 292 801 242 | 6 540 817 875 | 13 129 046 079 | 6 446 219 067 | 6 | 5 |
| 2 | Travail, emploi et administration des ministères sociaux | 12 065 359 297 | 3 006 071 590 | 10 695 643 750 | 2 736 589 938 | 4 | 4 |
| 3 | Aide publique au développement | 2 334 755 315 | 792 888 607 | 2 185 603 430 | 547 882 318 | 3 | 3 |
| 4 | Écologie, développement et mobilité durables | 3 605 103 562 | 1 846 742 753 | 3 160 655 375 | 1 565 276 820 | 7 | 8 |
| 5 | Relations avec les collectivités territoriales | 3 760 085 443 | 1 260 211 929 | 2 814 605 562 | 940 619 175 | 2 | 2 |
| 6 | Culture | 2 027 866 360 | 1 215 530 353 | 1 743 251 527 | 958 596 828 | 4 | 4 |
| 7 | Sport, jeunesse et vie associative | 1 005 644 806 | 490 047 570 | 974 423 297 | 441 565 654 | 3 | 3 |
| 8 | Immigration, asile et intégration | 1 259 249 135 | 637 876 981 | 1 257 002 837 | 635 855 313 | 2 | 2 |
| 9 | Santé | 781 560 604 | 860 025 110 | 779 217 127 | 825 186 199 | 2 | 3 |
| 10 | Recherche et enseignement supérieur | 772 662 106 | 397 901 573 | 670 132 264 | 310 535 414 | 1 | 1 |
| 11 | Médias, livre et industries culturelles | 674 689 892 | 495 369 539 | 568 920 102 | 387 685 347 | 2 | 2 |
| 12 | Économie | 630 363 522 | 607 647 611 | 556 598 409 | 524 485 319 | 3 | 3 |
| 13 | Direction de l’action du Gouvernement | 513 541 367 | 508 189 642 | 368 209 896 | 364 918 134 | 2 | 2 |
| 14 | Transformation et fonction publiques | 207 779 344 | 244 827 545 | 168 004 952 | 183 903 369 | 2 | 3 |
| 15 | Enseignement scolaire | 225 417 181 | 202 875 463 | 225 417 181 | 202 875 463 | 3 | 3 |
| 16 | Action extérieure de l’État | 205 826 724 | 182 819 897 | 200 134 647 | 173 143 366 | 2 | 2 |
| 17 | Solidarité, insertion et égalité des chances | 102 086 614 | 46 766 072 | 101 987 363 | 46 597 345 | 3 | 3 |
| 18 | Agriculture et alimentation | 92 065 085 | 322 100 630 | 78 679 546 | 223 945 870 | 1 | 2 |
| 19 | Administration générale et territoriale de l’État | 68 670 672 | 30 901 802 | 68 670 672 | 30 901 802 | 1 | 1 |
| 20 | Sécurités | 49 278 164 | 66 892 142 | 37 946 354 | 52 729 405 | 1 | 1 |
| 21 | Justice | 6 924 880 | 11 772 297 | 5 886 148 | 10 006 452 | 1 | 1 |
| 22 | Conseil et contrôle de l’État | 6 289 599 | 8 474 392 | 5 812 720 | 7 663 696 | 2 | 2 |
| | **Total** | **43 688 020 914** | **19 776 751 373** | **39 795 849 238** | **17 617 182 294** | 57 | 60 |

**Total : 43 688 020 914 € d'AE et 39 795 849 238 € de CP avant ; 19 776 751 373 € d'AE et 17 617 182 294 € de CP après.** Soit −23 911 269 541 € d'AE et −22 178 666 944 € de CP.

*Déduit*, par date d'effet, avant plafond : 7,98 Md€ d'AE au 1er janvier, 1,83 Md€ au 1er avril, 10,21 Md€ au 1er juillet.

**Trois programmes sont ramenés au crédit ouvert** (*relevé*) : « Jeux olympiques et paralympiques d'hiver 2030 » (167 806 932 € calculés, 61 600 000 € d'AE ouvertes), « Performance et résilience des bâtiments de l'État et de ses opérateurs » (187 248 836 € calculés, 57 141 756 € ouverts), « Plan France Très haut débit » (5 377 436 € calculés, 3 135 000 € ouverts). Leurs AE de 2027 sont retirées en entier. Ils étaient neuf avant.

**Aucun crédit n'est retiré au-delà du crédit ouvert** : `controle_credits_liasse.py`, règles C1 et C2, 0 anomalie.

## 3. Les cas « registre muet » et « classeur muet » (règles 4, 5 et 7)

*Déduit* de la table ; 28 lignes, toutes marquées à la colonne `regle_cas`.

| ligne | cat. | programmes | objet | taux | rythme | date retenue | d'où vient la date | brut AE | AE retirées | CP retirés |
|---|---:|---|---|---:|---:|---|---|---:|---:|---:|
| aucune — registre muet | 63 | 21 programmes | les transferts aux collectivités | 1,00 | ⅓ | 1er janv. | de la ligne D42 du § 4 — personne morale (R-P) ; même rythme et même date que « collectivités — charges courantes » | 5 501 643 382 | 1 833 879 293 | 1 368 388 152 |
| D14 — registre muet | 32 | 135 | la subvention à l’Agence nationale de l’habitat | 0,90 | 0,65 | 1er juil. | de la ligne D16 du § 4 — opérateur de l’État, comme les « autres opérateurs » | 169 900 000 | 49 695 750 | 49 695 750 |
| D6 — registre, classeur muet | 32 | 102 | la subvention à France Travail | 0,90 | ⅓ ; ⅙ conservé | 1er janv. | pilotage, 20261116, règle 5 : règle du registre — § 4, ligne D6 : 10 % conservés, tiers par an, 1er janvier ; § 3 : un sixième conservé en 2027. Le classeur chiffre sur le budget de l’opérateur, non sur la subvention | 1 162 912 863 | 290 727 809 | 290 727 809 |
| D16 — registre, classeur muet | 32 | 102 | les subventions aux opérateurs | 0,90 | 1 | 1er juil. | le classeur retranche tout le programme des « autres opérateurs » sans le chiffrer ; registre § 4, ligne D16 : socle, rythme et date | 111 950 648 | 50 377 792 | 50 377 792 |
| non rangée — registre muet | 64 | 102 | les subventions aux associations | 1,00 | ⅓ | 1er juil. | de la ligne D36 du § 4 — défaut écrit au § 14 du registre : « autres associations » | 567 793 019 | 94 632 075 | 94 632 075 |
| non rangée — registre muet | 61 | 103 | les transferts aux ménages | 0,90 | ⅓ | 1er juil. | de la ligne D22 du § 4 — transfert aux ménages, comme les « autres ménages » | 5 800 000 | 869 999 | 869 999 |
| D21 — registre muet | 61 | 103 | la compensation des exonérations d’emploi à domicile | 0,90 | ⅓ | 1er juil. | de la ligne D22 du § 4 — transfert aux ménages, comme les « autres ménages » | 1 174 317 879 | 176 147 506 | 176 147 506 |
| D21 — registre muet | 62 | 103 | la compensation des exonérations d’emploi à domicile | 1,00 | ⅓ | 1er juil. | de la ligne D25 du § 4 — même programme, même catégorie, même poste du classeur que « emploi et apprentissage » | 1 089 434 778 | 181 572 281 | 145 257 825 |
| **Total, avant plafond** | | | | | | | | **9 783 752 569** | **2 677 902 505** | **2 176 096 907** |

- **Catégorie 63 (règle 4)** : registre muet. Par tiers, un tiers en 2027 ; la date, 1er janvier, est celle de la ligne la plus proche du § 4 (D42) et de R-P.
- **Anah, emploi à domicile, missions locales (règle 5)** : registre muet. Taux et rythme du classeur ; seule la date est prise à la ligne la plus proche du § 4. **Le choix de cette ligne est de ce fil** : 1er juillet partout. Avec le 1er janvier, ces lignes doubleraient (+502 917 611 € d'AE).
- **France Travail et le reste du 102 en catégorie 32** : classeur muet, règle du registre.

## 4. Les 59 lignes arrêtées par le classeur et absentes de la liasse du matin

*Déduit.* Montant selon la règle du § 1, avant plafond.

| sort | lignes | brut AE | brut CP | AE selon la règle, avant plafond | CP |
|---|---:|---:|---:|---:|---:|
| ajoutées | 17 | 718 496 329 | 730 889 171 | 537 570 403 | 383 400 788 |
| « En 3 ans » | 10 | 13 365 167 963 | 12 454 396 952 | 4 208 537 433 | 3 146 150 256 |
| comptes spéciaux | 19 | 5 522 916 206 | 5 634 416 206 | 2 731 879 080 | 2 082 915 557 |
| maintenues | 2 | 283 860 073 | 283 860 073 | 0 | 0 |
| France 2030 | 11 | 450 000 000 | 5 484 329 332 | 74 999 925 | 74 999 925 |
| **Total** | **59** | **20 340 440 571** | **24 587 891 734** | **7 552 986 841** | **5 687 466 526** |

**17 lignes ajoutées, purs oublis** (*relevé* : libellé du programme changé entre le PAP 2026 et l'état B 2027 ; l'ancien outil écartait sans le dire tout programme non retrouvé) :

| programme (2026) | libellé à l'état B 2027 | amendement | AE retirées | CP retirés | correspondance |
|---|---|---:|---:|---:|---|
| 149 | Compétitivité et durabilité de l'agriculture et de l'agroalimentaire | n° 18 | 209 308 490 | 126 600 379 | *déduite* : la forêt sort du programme en 2027 |
| 205 | Mer, pêche et aquaculture | n° 4 | 86 552 914 | 59 367 059 | *héritée* du registre § 14 |
| 349 | Accès, qualité et transformation des services publics | n° 14 | 36 009 000 | 22 588 350 | *déduite* : seul programme de la mission sans homonyme en 2026 |
| 379 | Reversement à la sécurité sociale des recettes de la Facilité pour la Relance et la Résilience (FRR) | n° 9 | 205 700 000 | 174 845 000 | *relevée* : même libellé, abrégé |

**À lire avant dépôt** : le programme 379 est un reversement à la sécurité sociale de recettes européennes, classé en catégorie 31 ; le classeur l'arrête à 85 % comme du fonctionnement. Il est ajouté parce que le classeur l'arrête. Les correspondances des programmes 149 et 349 sont des déductions : l'état B ne porte pas de numéro de programme. La table des correspondances est `referentiels/correspondance_programmes_pap2026_etatB2027.tsv`.

**42 lignes laissées hors liasse** :

- **France 2030, 11 lignes** : aucune AE ouverte en 2027 ; un amendement de crédits n'y retire rien. Article normatif dû (registre § 15).
- **Comptes spéciaux, 19 lignes** : état D, hors de l'article 58. L'audiovisuel public (6 lignes) est porté en première partie, liasse P1, amendement n° 26. Les quatre comptes d'affectation spéciale (13 lignes) ne sont portés par aucun amendement.
- **« En 3 ans », 10 lignes, 13,4 Md€ bruts** : ni oubli ni autre amendement. Le classeur les sort de la restitution et n'en donne que le total ; aucune ligne du § 4 ne les porte. Montant indicatif à un tiers, date de la ligne voisine : 4,21 Md€ d'AE. **Décision due** : dont « Service public de l'énergie » (8,93 Md€ bruts) et « Développement des entreprises et régulations » (1,89 Md€).
- **Entretien des routes, 2 lignes** : maintenu.

Ligne par ligne :

| mission (2026) | prog. | cat. | ligne | brut AE | brut CP | taux × rythme × fraction | AE selon la règle | CP selon la règle | sort | pourquoi elle était absente |
|---|---:|---:|---|---:|---:|---|---:|---:|---|---|
| Agriculture, alimentation, forêt et af | 149 | 31 | D37 | 122 263 219 | 122 263 219 | 0,85 × 1 × 1 | 103 923 736 | 88 335 176 | **ajoutée au n° 18** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Agriculture, alimentation, forêt et af | 149 | 32 | D16 | 486 639 339 | 486 639 339 | 1 × 0,333 × 0,5 | 81 106 475 | 81 106 475 | hors liasse | ni oubli ni autre amendement : le classeur les sort de la restitution (« En 3 ans », total seul) ; montant indicatif |
| Agriculture, alimentation, forêt et af | 149 | 62 | D27 | 873 196 051 | 974 829 447 | 1 × 0,333 × 1 | 291 065 059 | 232 852 047 | hors liasse | ni oubli ni autre amendement : le classeur les sort de la restitution (« En 3 ans », total seul) ; montant indicatif |
| Agriculture, alimentation, forêt et af | 149 | 64 | D36 | 184 476 753 | 184 507 771 | 1 × 0,333 × 0,5 | 30 746 095 | 30 746 095 | hors liasse | ni oubli ni autre amendement : le classeur les sort de la restitution (« En 3 ans », total seul) ; montant indicatif |
| Agriculture, alimentation, forêt et af | 149 | 63 | aucune | 100 900 000 | 100 900 000 | 1 × 0,333 × 1 | 33 633 300 | 25 224 975 | **ajoutée au n° 18** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Agriculture, alimentation, forêt et af | 149 | 51 | D37 | 28 101 979 | 20 395 730 | 0,85 × 1 × 1 | 23 886 682 | 3 467 274 | **ajoutée au n° 18** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Agriculture, alimentation, forêt et af | 149 | 53 | D37 | 56 311 496 | 56 311 496 | 0,85 × 1 × 1 | 47 864 772 | 9 572 954 | **ajoutée au n° 18** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Agriculture, alimentation, forêt et af | 206 | 62 | D27 | 29 837 675 | 29 783 421 | 1 × 0,333 × 1 | 9 945 882 | 7 942 238 | hors liasse | ni oubli ni autre amendement : le classeur les sort de la restitution (« En 3 ans », total seul) ; montant indicatif |
| Avances à l'audiovisuel public | 841 | 62 | D24 | 2 440 577 000 | 2 440 577 000 | 1 × 1 × 0,5 | 1 220 288 500 | 976 230 800 | hors liasse | première partie : compte d’avances à l’audiovisuel public, liasse P1, amendement n° 26 ; état D |
| Avances à l'audiovisuel public | 842 | 62 | D24 | 298 114 886 | 298 114 886 | 1 × 1 × 0,5 | 149 057 443 | 119 245 954 | hors liasse | première partie : compte d’avances à l’audiovisuel public, liasse P1, amendement n° 26 ; état D |
| Avances à l'audiovisuel public | 843 | 62 | D24 | 648 033 908 | 648 033 908 | 1 × 1 × 0,5 | 324 016 954 | 259 213 563 | hors liasse | première partie : compte d’avances à l’audiovisuel public, liasse P1, amendement n° 26 ; état D |
| Avances à l'audiovisuel public | 844 | 62 | D24 | 303 883 551 | 303 883 551 | 1 × 1 × 0,5 | 151 941 776 | 121 553 420 | hors liasse | première partie : compte d’avances à l’audiovisuel public, liasse P1, amendement n° 26 ; état D |
| Avances à l'audiovisuel public | 845 | 62 | D24 | 103 461 144 | 103 461 144 | 1 × 1 × 0,5 | 51 730 572 | 41 384 458 | hors liasse | première partie : compte d’avances à l’audiovisuel public, liasse P1, amendement n° 26 ; état D |
| Avances à l'audiovisuel public | 847 | 62 | D24 | 84 242 456 | 84 242 456 | 1 × 1 × 0,5 | 42 121 228 | 33 696 982 | hors liasse | première partie : compte d’avances à l’audiovisuel public, liasse P1, amendement n° 26 ; état D |
| Contrôle de la circulation et du stati | 751 | 31 | D37 | 186 288 214 | 186 288 214 | 0,85 × 1 × 1 | 158 344 982 | 134 593 235 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Contrôle de la circulation et du stati | 751 | 51 | D37 | 59 750 000 | 59 750 000 | 0,85 × 1 × 1 | 50 787 500 | 10 157 500 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Contrôle de la circulation et du stati | 751 | 53 | D37 | 15 000 000 | 15 000 000 | 0,85 × 1 × 1 | 12 750 000 | 2 550 000 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Contrôle de la circulation et du stati | 753 | 53 | D37 | 1 000 000 | 1 000 000 | 0,85 × 1 × 1 | 850 000 | 170 000 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Contrôle de la circulation et du stati | 754 | 63 | aucune | 806 735 047 | 806 735 047 | 1 × 0,333 × 1 | 268 911 413 | 201 683 560 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Développement agricole et rural | 775 | 64 | D36 | 67 900 000 | 67 900 000 | 1 × 0,333 × 0,5 | 11 316 655 | 11 316 655 | hors liasse | ni oubli ni autre amendement : le classeur les sort de la restitution (« En 3 ans », total seul) ; montant indicatif |
| Développement agricole et rural | 775 | 31 | D37 | 30 000 | 30 000 | 0,85 × 1 × 1 | 25 500 | 21 675 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Développement agricole et rural | 776 | 64 | D36 | 102 570 000 | 102 570 000 | 1 × 0,333 × 0,5 | 17 094 983 | 17 094 983 | hors liasse | ni oubli ni autre amendement : le classeur les sort de la restitution (« En 3 ans », total seul) ; montant indicatif |
| Développement agricole et rural | 776 | 31 | D37 | 500 000 | 500 000 | 0,85 × 1 × 1 | 425 000 | 361 250 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Écologie, développement et mobilité du | 159 | 32 | D16 | 637 499 983 | 637 499 983 | 1 × 0,333 × 0,5 | 106 249 891 | 106 249 891 | hors liasse | ni oubli ni autre amendement : le classeur les sort de la restitution (« En 3 ans », total seul) ; montant indicatif |
| Écologie, développement et mobilité du | 203 | 31 | D37 | 232 884 101 | 232 884 101 | 0 × 1 × 1 | 0 | 0 | hors liasse | décision de l’auteure : entretien des routes nationales maintenu |
| Écologie, développement et mobilité du | 203 | 51 | D37 | 50 975 972 | 50 975 972 | 0 × 1 × 1 | 0 | 0 | hors liasse | décision de l’auteure : entretien des routes nationales maintenu |
| Écologie, développement et mobilité du | 205 | 31 | D37 | 47 793 867 | 48 475 260 | 0,85 × 1 × 1 | 40 624 787 | 34 531 069 | **ajoutée au n° 4** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Écologie, développement et mobilité du | 205 | 51 | D37 | 14 641 967 | 25 743 657 | 0,85 × 1 × 1 | 12 445 672 | 2 489 134 | **ajoutée au n° 4** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Écologie, développement et mobilité du | 205 | 64 | D36 | 9 515 322 | 18 933 112 | 0,9 × 1 × 0,5 | 4 281 895 | 4 281 895 | **ajoutée au n° 4** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Écologie, développement et mobilité du | 205 | 32 | D16 | 29 807 155 | 29 807 155 | 0,9 × 1 × 0,5 | 13 413 220 | 13 413 220 | **ajoutée au n° 4** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Écologie, développement et mobilité du | 205 | 52 | D37 | 15 112 324 | 13 010 542 | 0,85 × 1 × 1 | 12 845 475 | 2 211 792 | **ajoutée au n° 4** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Écologie, développement et mobilité du | 205 | 61 | D22 | 2 076 000 | 2 076 000 | 0,9 × 1 × 0,5 | 934 200 | 934 200 | **ajoutée au n° 4** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Écologie, développement et mobilité du | 205 | 63 | aucune | 6 023 000 | 11 023 000 | 1 × 0,333 × 1 | 2 007 665 | 1 505 748 | **ajoutée au n° 4** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Écologie, développement et mobilité du | 205 | 62 | D27 | 165 314 204 | 140 634 204 | 1 × 0,333 × 1 | 55 104 680 | 37 502 417 | hors liasse | ni oubli ni autre amendement : le classeur les sort de la restitution (« En 3 ans », total seul) ; montant indicatif |
| Écologie, développement et mobilité du | 345 | 62 | D27 | 8 929 936 908 | 8 443 236 908 | 1 × 0,333 × 1 | 2 976 642 659 | 2 251 527 591 | hors liasse | ni oubli ni autre amendement : le classeur les sort de la restitution (« En 3 ans », total seul) ; montant indicatif |
| Économie | 134 | 62 | D27 | 1 887 797 050 | 1 386 795 879 | 1 × 0,333 × 1 | 629 265 054 | 369 811 865 | hors liasse | ni oubli ni autre amendement : le classeur les sort de la restitution (« En 3 ans », total seul) ; montant indicatif |
| Financement des aides aux collectivité | 793 | 63 | aucune | 361 600 000 | 361 600 000 | 1 × 0,333 × 1 | 120 533 213 | 90 399 910 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Financement des aides aux collectivité | 793 | 31 | D37 | 700 000 | 700 000 | 0,85 × 1 × 1 | 595 000 | 505 750 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Financement des aides aux collectivité | 794 | 63 | aucune | 3 000 000 | 3 000 000 | 1 × 0,333 × 1 | 999 999 | 749 999 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Gestion du patrimoine immobilier de l' | 723 | 31 | D37 | 99 000 000 | 118 000 000 | 0,85 × 1 × 1 | 84 150 000 | 71 527 500 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Gestion du patrimoine immobilier de l' | 723 | 51 | D37 | 108 000 000 | 200 500 000 | 0,85 × 1 × 1 | 91 800 000 | 18 360 000 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Gestion du patrimoine immobilier de l' | 723 | 53 | D37 | 3 000 000 | 3 000 000 | 0,85 × 1 × 1 | 2 550 000 | 510 000 | hors liasse | compte d’affectation spéciale : état D, hors de l’article 58 ; aucun amendement ne le porte |
| Investir pour la France de 2030 | 421 | 64 | D33 | 0 | 200 693 126 | 1 × 0,333 × 0,5 | 0 | 0 | hors liasse | aucune AE ouverte à l’état B 2027 : rien à retirer ; article normatif dû (registre § 15) |
| Investir pour la France de 2030 | 422 | 62 | D26 | 0 | 7 296 089 | 1 × 0,333 × 1 | 0 | 0 | hors liasse | aucune AE ouverte à l’état B 2027 : rien à retirer ; article normatif dû (registre § 15) |
| Investir pour la France de 2030 | 422 | 64 | D33 | 0 | 24 865 511 | 1 × 0,333 × 0,5 | 0 | 0 | hors liasse | aucune AE ouverte à l’état B 2027 : rien à retirer ; article normatif dû (registre § 15) |
| Investir pour la France de 2030 | 423 | 62 | D26 | 0 | 23 160 000 | 1 × 0,333 × 1 | 0 | 0 | hors liasse | aucune AE ouverte à l’état B 2027 : rien à retirer ; article normatif dû (registre § 15) |
| Investir pour la France de 2030 | 423 | 31 | D37 | 0 | 100 000 000 | 0,85 × 1 × 1 | 0 | 0 | hors liasse | aucune AE ouverte à l’état B 2027 : rien à retirer ; article normatif dû (registre § 15) |
| Investir pour la France de 2030 | 424 | 64 | D33 | 0 | 772 240 000 | 1 × 0,333 × 0,5 | 0 | 0 | hors liasse | aucune AE ouverte à l’état B 2027 : rien à retirer ; article normatif dû (registre § 15) |
| Investir pour la France de 2030 | 424 | 62 | D26 | 0 | 2 546 071 564 | 1 × 0,333 × 1 | 0 | 0 | hors liasse | aucune AE ouverte à l’état B 2027 : rien à retirer ; article normatif dû (registre § 15) |
| Investir pour la France de 2030 | 424 | 31 | D37 | 0 | 435 563 445 | 0,85 × 1 × 1 | 0 | 0 | hors liasse | aucune AE ouverte à l’état B 2027 : rien à retirer ; article normatif dû (registre § 15) |
| Investir pour la France de 2030 | 425 | 64 | D33 | 450 000 000 | 642 172 197 | 1 × 0,333 × 0,5 | 74 999 925 | 74 999 925 | hors liasse | aucune AE ouverte à l’état B 2027 : rien à retirer ; article normatif dû (registre § 15) |
| Investir pour la France de 2030 | 425 | 62 | D26 | 0 | 647 267 400 | 1 × 0,333 × 1 | 0 | 0 | hors liasse | aucune AE ouverte à l’état B 2027 : rien à retirer ; article normatif dû (registre § 15) |
| Investir pour la France de 2030 | 425 | 31 | D37 | 0 | 85 000 000 | 0,85 × 1 × 1 | 0 | 0 | hors liasse | aucune AE ouverte à l’état B 2027 : rien à retirer ; article normatif dû (registre § 15) |
| Santé | 379 | 31 | D37 | 242 000 000 | 242 000 000 | 0,85 × 1 × 1 | 205 700 000 | 174 845 000 | **ajoutée au n° 9** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Transformation et fonction publiques | 349 | 31 | D37 | 36 260 000 | 29 260 000 | 0,85 × 1 × 1 | 30 821 000 | 21 140 350 | **ajoutée au n° 14** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Transformation et fonction publiques | 349 | 51 | D37 | 0 | 500 000 | 0,85 × 1 × 1 | 0 | 0 | **ajoutée au n° 14** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Transformation et fonction publiques | 349 | 52 | D37 | 5 500 000 | 8 000 000 | 0,85 × 1 × 1 | 4 675 000 | 935 000 | **ajoutée au n° 14** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Transformation et fonction publiques | 349 | 21 | D38 | 1 500 000 | 1 500 000 | 0,9 × 1 × 0,5 × 0,3 | 202 500 | 202 500 | **ajoutée au n° 14** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |
| Transformation et fonction publiques | 349 | 64 | D36 | 690 000 | 690 000 | 0,9 × 1 × 0,5 | 310 500 | 310 500 | **ajoutée au n° 14** | oubli : libellé du programme changé entre le PAP 2026 et l’état B 2027, la jointure de l’ancien outil l’écartait sans le dire |

## 5. Constats de la régénération

*Relevé*, sauf mention.

- **Le programme « Interventions territoriales de l'État » (162) est sorti de l'amendement n° 1.** L'état B 2027 le range à la mission « Outre-mer », non à « Cohésion des territoires ». Il y figurait pour 75 599 008 € d'AE. Selon la règle : 35 322 219 € d'AE et 30 134 319 € de CP. La mission « Outre-mer » n'a pas d'amendement : **un 23e amendement est dû, non écrit** — il renuméroterait les n° 23 à 39.
- **L'amendement n° 18 change de titre** : la mission s'appelle « Agriculture et alimentation » à l'état B 2027. Sommaire mis à jour.
- **La gestion de l'après-mines sort de l'amendement n° 4** : le classeur la maintient (`SynthèseR!F32`). 98 997 500 € y étaient retirés.
- **Une ligne « dont titre 2 » accompagne désormais chaque programme dont des rémunérations sont retirées** : 13 programmes, 443 810 354 €. La liasse du matin n'en portait aucune pour 443 607 855 € de titre 2 retirés (*hérité* du document des écarts).
- **Amendement n° 33** : entrée en vigueur et exposé au 1er avril 2027. **Amendement n° 34** : entrée en vigueur au 1er juillet 2027 ; l'exposé dit la moitié de l'effet, 300 millions d'euros (*hérité* du § 4, ligne D20). **Reste dû** : l'exposé du n° 34 situe le chèque énergie au programme « Service public de l'énergie », quand le registre et l'amendement n° 4 le retirent du programme « Énergie, climat et après-mines » (285 615 000 € d'AE) ; et une abrogation au 1er juillet tombe après la campagne d'émission du printemps.
- **Exposés des 22 amendements** : montants arrondis ; une phrase de date par date d'effet, qui nomme les dépenses concernées ; une phrase sur la première année des sorties en trois ans.
- **`appareil/tablette_p2.py`** importe les tables de l'ancienne chaîne et s'arrête désormais à l'import. Il lisait le classeur de suivi absent. `livrables/tablette_P2_20261016.md` décrit la liasse d'avant : périmée.
- **§ 4 du registre, ligne D37** : socle porté de 20 % à 15 %, hors entretien des routes ; F et le montant de 2027 inchangés à l'arrondi (3,78 pour 3,8).

## 6. Le croisé mesure × mois, reconstruit — il fait foi

`referentiels/calendrier_mesures_mois_20261116.tsv` et sa note de lecture — 27 lignes du § 4, 48 mois de janvier 2027 à décembre 2030, en mesure, Md€, avec pan, agent, périmètre, socle, rythme, date d'effet. Outil : `appareil/calendrier_mesures_mois.py` (`construire`, `controler`). **Le tableau d'origine est introuvable au projet comme au dépôt** (*hérité* de la passation du projet) : cette reconstruction fait foi, c'est écrit en tête de la note et de l'outil.

*Relevé* : les 27 lignes, leurs paramètres et leur montant de 2027 (§ 4) ; la trajectoire annuelle (§ 5) ; l'agent de chaque ligne (onglet « La clé d'incidence »).
*Déduit* : la mensualisation, par la règle écrite au § 16 — un douzième par mois entre deux marches, marche au 1er juillet pour les sorties en trois ans entrées en juillet, au 1er janvier sinon.

**Le croisé contre le registre à niveau** :

| contrôle | valeurs | écart maximal, Md€ |
|---|---:|---:|
| somme de 2027 par ligne = § 4 | 27 | 0,0000 |
| somme annuelle par ligne = § 5 | 108 | 0,0000 |
| total des coupes par exercice = § 5 | 4 | 0,0100 |

**La preuve de la méthode** — même mensualisation, les quatre lignes mises à niveau (D16, D38, D41, D43) rejouées à leurs valeurs antérieures, contre les pièces du 15 octobre :

| contrôle | valeurs | écart maximal, Md€ |
|---|---:|---:|
| par agent et par mois = classeur de flux | 408 | 0,0025 |
| par agent et par trimestre = classeur de flux | 124 | 0,0065 |
| par agent et par exercice = classeur de flux | 32 | 0,0180 |
| par agent et par mois de 2027 = § 6 | 108 | 0,0056 |
| par pan et par trimestre = § 16 | 112 | 0,0075 |

**Une ligne ne retombe pas sur les deux pièces à la fois : D25, emploi et apprentissage, en 2028.** Le § 16 la fait marcher au 1er juillet (pan « Entreprises » : 2,38 puis 3,53 par trimestre) ; le classeur de flux l'étale par douzièmes. Les deux donnent 4,60 sur l'année. Le croisé suit le registre ; l'agent « Entreprises » et le total s'écartent du classeur de flux de 0,1932 par mois en 2028, en plus au premier semestre, en moins au second.

L'écart de 0,018 par exercice vient de la restitution : 9,54 par mois au § 2 font 114,48 sur douze mois, contre 114,46.

**Lecture de la liasse.** Part État, somme des douze mois de 2027 : **27,09 Md€ en mesure** (*déduit* ; 27,45 avant la mise à niveau). La liasse retire 19,78 Md€ d'AE. Les deux ne se superposent pas terme à terme : la liasse part du brut du PAP et du taux du classeur, le croisé de F au registre ; la liasse ajoute les transferts aux collectivités (1,83 Md€), l'emploi à domicile, l'Anah et les missions locales (0,50 Md€), que le § 4 ne porte pas ; elle ne porte ni l'audiovisuel public (1,90), ni France 2030 (1,34), ni la part de D5 et de D6 hors état B (3,35 et 1,17). Par ligne, *déduit* : D18 2,69 Md€ pour 2,68 au § 4 ; D29 1,83 pour 1,88 ; D16 1,66 pour 2,06 ; D15 1,30 pour 1,17 ; D37 2,66 pour 3,80 ; D38 0,44 pour 0,45 ; D25 0,79 pour 1,15 ; D27 1,09 pour 1,30 ; D36 1,19 pour 0,70.

**Écarts en moins, à la ligne** (consigne de l'auteure du 7 octobre, *héritée* de la passation : seuls les moins se signalent, une compensation au total ne vaut pas quitus). La liasse retire moins que la mesure du § 4 sur : D37, −1,14 Md€ d'AE (le § 4 porte 3,80, le brut arrêté × 85 % donne 2,66) ; D16, −0,40 ; D25, −0,36 ; D27, −0,21 ; D29, −0,05 ; D38, −0,01.

## 7. Contrôles

*Relevé le 20261116, sur la branche.*

| contrôle | résultat |
|---|---|
| `controle_liasse_classeurs.py controler --cible projet` | **22 amendements, 0 en échec** ; AE 19 776 751 373 pour une cible de 19 776 751 375 |
| `controle_liasse_classeurs.py faute` (1 000 € injectés, cible `projet`) | **mordue**, 1 amendement en échec |
| `controle_liasse_classeurs.py controler --cible mixte` | 16 en échec sur 22 : attendu, la correction du pilotage rend le rythme au registre |
| cibles `classeur`, `registre`, `liasse` | 22, 21 et 22 en échec : attendu |
| `controle_credits_liasse.py` | **0 anomalie bloquante, 0 signal** (C1 et C2 ; liasse sans déclaration de catégorie) |
| `controle_liasses.py` | **0 écart L1 à L4 et L6** |
| `calendrier_mesures_mois.py controler` | **0 contrôle en échec**, sur le registre à niveau |
| `controle_liasse_classeurs.py reperes` | **51 repères `A!` du § 14, 51 concordants** |
| régénération rejouée après la mise à niveau du registre | liasse identique à l'octet : aucun montant d'amendement ne bouge |

Les deux classeurs du site ont été téléchargés ce jour ; leurs empreintes sont celles de la note de lecture (`8a4a08fd…a566dd`, `ac56012f…e64e84a`). Les 62 colonnes d'origine de la table sont inchangées, hors effet de la ligne D37 du registre et des quatre programmes renommés.

**Limite.** La table est écrite par `controle_liasse_classeurs.py construire`, dont le code porte le rattachement des lignes aux règles (fonction `regle`), comme il portait déjà le rattachement aux postes du classeur. `chaine_credits.py` et `generer_liasse_p2.py` ne portent plus aucun paramètre. La cible `projet` et la chaîne lisent les mêmes colonnes : le contrôle prouve que la liasse suit la table, non que la table est juste.

## 8. Mise à niveau du registre de calcul, § 4 et 5

*Tranché par le pilotage, révocable* : la série de classeurs du site fait foi pour les montants et les taux. *Validé par l'auteur le 20261116*, relevé à `methode/arbitrages.md` : départs d'agents en entier en régime plein, à 30 % la première année.

| ligne | avant | après | d'où |
|---|---|---|---|
| D16 Autres opérateurs | F 2,745 ; 1,37 · 2,75 · 2,75 · 2,75 | F 4,116 ; 2,06 · 4,12 · 4,12 · 4,12 | *relevé* : `Détail Economies`!F16 du classeur du site |
| D37 Charges courantes | socle 20 % | socle 15 %, hors entretien des routes ; montants inchangés à l'arrondi | décision de l'auteure, *héritée* |
| D41 Collectivités — aides aux entreprises | F 12,3 ; 4,10 · 8,20 · 12,30 · 12,30 | F 12,21 ; 4,07 · 8,14 · 12,21 · 12,21 | *relevé* : F41 |
| D43 Collectivités — départs | F 20,0 ; 10,00 · 20,00 · 20,00 · 20,00 | F 19,864 ; 2,98 · 5,96 · 5,96 · 5,96 | *relevé* : F43 ; 30 % |
| D38 Départs de fonctionnaires de l'État | 1,50 · 3,00 · 3,00 · 3,00 | 0,45 · 0,90 · 0,90 · 0,90 | 30 % |

**Effet sur les totaux du § 5**, en mesure, Md€ (*déduit*) :

| | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|
| D16 | +0,69 | +1,37 | +1,37 | +1,37 |
| D38 | −1,05 | −2,10 | −2,10 | −2,10 |
| D41 | −0,03 | −0,06 | −0,09 | −0,09 |
| D43 | −7,02 | −14,04 | −14,04 | −14,04 |
| **coupes** | **−7,41** | **−14,83** | **−14,86** | **−14,86** |
| coupes avant | 56,34 | 100,05 | 123,97 | 127,57 |
| coupes après | 48,93 | 85,22 | 109,11 | 112,71 |
| solde avant | +22,95 | −14,41 | +9,51 | +13,11 |
| **solde après** | **+15,54** | **−29,24** | **−5,35** | **−1,75** |

**Le solde en mesure devient négatif de 2028 à 2030.** C'est l'effet mécanique de la lecture validée, la restitution restant à 114,46 Md€ par an. Les départs d'agents laissent 16,00 Md€ par an « à terme », hors fenêtre : 2,10 pour l'État, 13,90 pour les collectivités.

**Le passage de 30 % au plein n'est fixé par aucune pièce.** *Relevé* : l'indemnité dure d'une à sept années selon l'ancienneté (amendement n° 26, C du II) ; aucune pièce ne répartit les agents par ancienneté ; le classeur du site écrit seulement, pour le bloc de l'État, « Effets pleins à horizon estimé à 3 ans » (`Détail Economies`!G3). *Tranché en propre, révocable* : 30 % sur toute la fenêtre 2027-2030. Avec la note G3 lue comme une date, 2030 porterait la ligne entière : +16,00 Md€ cet exercice-là, solde à +14,25.

**Non rejoués** : § 6, 7, 15, 16 et 17 du registre, `suivi_trajectoire_20261015.md`, `flux_par_agent_20261015.md` et le classeur de flux. Le registre le dit au § 5. Dans la table de paramètres, la colonne `date_flux_par_agent` passe à « non rejouée » sur 53 lignes : le classeur de flux ne rejoue plus le § 4.

**La liasse 2027 n'est pas touchée** : le titre 2 y suivait déjà la formule du § 10 (30 % après indemnité), et les autres lignes partent du brut du PAP.

## 8 bis. Pièces du projet intégrées

- **`sources/projet_20261116/23_…A_Credits.tsv`**, l'onglet « A — Crédits » du classeur de suivi jusqu'ici absent. *Relevé* : les **51 repères `A!Kn/Ln` du § 14** désignent bien le programme et la catégorie annoncés, tous au statut « arrêté », et leurs montants arrêtés sont le brut de la table de paramètres à 1 € près. Les 27 repères `PAP!` du § 14 se retrouvent aux adresses de la table. Le document des écarts annonçait 63 repères : le § 14 en porte 51 à la table A et 27 au PAP.
- **`22_…Mesure.tsv`**, les règles appliquées. *Relevé*, ligne 41 : « Catégorie 22 non arrêtée directement — suit le sort de la catégorie 21 » ; la table A porte 46 lignes au statut « suit le titre 2 ». **Écart en moins** : la liasse ne retire que les catégories 21 et 23, comme `SynthèseR!D7`. Les cotisations de catégorie 22 des programmes non essentiels du budget général font 1 995 722 820 € d'AE (*relevé* au PAP) ; au coefficient du titre 2, 269 422 581 € ne sont pas retirés (*déduit*).
- **Statut « sortie en 3 ans »** : 10 lignes à la table A, les dix « En 3 ans » de la table de paramètres. Confirme qu'elles sont arrêtées par le classeur sous un schéma distinct.
- **« Année 1 » du classeur** : année pleine en régime de croisière, non l'année civile 2027 (consigne *héritée*). Cohérent avec la règle retenue : la part de première année du classeur ne sert plus de rythme.

## 8 ter. Décisions dues, rendues au pilotage

1. Un 23e amendement « Outre-mer » pour le programme 162, et la renumérotation qu'il entraîne.
2. Les dix lignes « En 3 ans » (13,4 Md€ bruts) : dans la liasse à un tiers, ou hors liasse.
3. La date de l'Anah, de l'emploi à domicile et des missions locales : 1er juillet retenu.
4. Le programme 379 : reversement à la sécurité sociale, retiré à 85 % comme du fonctionnement.
5. D25 en 2028 : marche au 1er juillet (§ 16) ou douzièmes (classeur de flux).
6. L'exposé du n° 34 : programme porteur du chèque énergie et campagne de printemps.
7. Départs d'agents : la date du passage de 30 % au plein. 16,00 Md€ par exercice en dépendent.
8. La catégorie 22 : la retirer avec la 21, comme l'écrit l'onglet « Mesure » (269 M€ en 2027).
9. Rejouer les § 6, 15, 16 et 17 du registre et le classeur de flux sur le registre à niveau.

## 9. Entrées de registre

### Liasse de crédits régénérée : rythme et date du registre, taux du classeur — 20261116

*Tranché par le pilotage, révocable ; consigne de l'auteure héritée du pilotage.* Les 22 amendements de mission appliquent brut du PAP × taux du classeur × rythme et fraction du § 4 du registre, CP au résiduel du § 3, plafond au crédit ouvert de l'état B 2027. *Relevé* : 19 776 751 373 € d'AE et 17 617 182 294 € de CP, contre 43 688 020 914 et 39 795 849 238. *Exécuté* : `chaine_credits.py` et `generer_liasse_p2.py` lisent `referentiels/parametres_credits_20261116.tsv`, 81 colonnes, et ne portent plus de constante ; cible `projet` ajoutée à `controle_liasse_classeurs.py`, 0 échec, faute mordue.

### Liasse de crédits : registre muet, les dates tranchées — 20261116

*Tranché par le pilotage, révocable* : transferts aux collectivités par tiers, un tiers en 2027 ; emploi à domicile, Anah et missions locales au taux et au rythme du classeur ; France Travail à la règle du registre. *Tranché en propre, révocable* : la date de ces lignes est celle de la ligne la plus proche du § 4 — 1er janvier pour la catégorie 63 (D42), 1er juillet pour l'Anah (D16), l'emploi à domicile (D22, D25) et les missions locales (D36). 28 lignes, 2 677 902 505 € d'AE.

### Liasse de crédits : 17 lignes oubliées ajoutées, un programme sorti — 20261116

*Relevé.* L'ancien outil écartait sans le dire tout programme dont le libellé avait changé entre le PAP 2026 et l'état B 2027 : programmes 149, 205, 349 et 379, 17 lignes, 537 570 403 € d'AE ajoutés aux amendements n° 18, 4, 14 et 9. *Déduit* : correspondances de 149 et 349. *Relevé* : le programme 162 relève de la mission « Outre-mer » à l'état B 2027 ; il sort de l'amendement n° 1 ; un amendement « Outre-mer » est dû. L'amendement n° 18 prend le nom de la mission de 2027.

### Registre de calcul, ligne D37 : 15 % de socle, hors entretien des routes — 20261116

*Hérité du pilotage* : décision de l'auteure du 16 novembre, 85 % d'économie sur le fonctionnement hors régalien, éducation et entretien des routes nationales. *Exécuté* : § 4 et § 5 du registre mis à jour (socle de 15 %) ; F et le montant de 2027 inchangés à l'arrondi.

### Amendements n° 33 et 34 : dates alignées sur le registre — 20261116

*Exécuté.* Hébergement d'urgence au 1er avril 2027, chèque énergie au 1er juillet 2027, au dispositif et à l'exposé. *Non corrigé* : le programme que cite l'exposé du n° 34.

### Croisé mesure × mois reconstruit — 20261116

*Exécuté.* `referentiels/calendrier_mesures_mois_20261116.tsv`, 27 lignes × 48 mois, sa note de lecture et `appareil/calendrier_mesures_mois.py`. **Il fait foi** (*tranché par le pilotage*) : l'original est introuvable. *Relevé* : il redonne les § 4 et 5 à niveau à 0,01 Md€ près ; rejoué aux valeurs antérieures de D16, D38, D41 et D43, il redonne le § 6, le § 16 et le classeur de flux, écart maximal 0,018 Md€. *Relevé* : D25 en 2028 marche au 1er juillet au § 16 et par douzièmes au classeur de flux ; le croisé suit le registre, écart déclaré de 0,1932 Md€ par mois sur l'agent « Entreprises ».

### Registre de calcul, § 4 et 5 : D16, D41 et D43 aux montants du classeur du site — 20261116

*Tranché par le pilotage, révocable* : la série du site fait foi pour les montants et les taux. *Relevé* à `Détail Economies` du classeur du site : F16 = 4,116 (2,745), F41 = 12,21 (12,3), F43 = 19,864 (20). *Exécuté* : § 4 et § 5 mis à niveau, valeurs antérieures gardées au § 5 pour la trace. *Non rejoués* : § 6, 7, 15, 16, 17, le suivi de trajectoire et le classeur de flux.

### Départs d'agents : en entier dans les 236, à 30 % en salaire net la première année — mise à niveau du registre de calcul — 20261116

**Validé.** *Réponse de l'auteur du 20261116* : « dans les 236 c'est tout dont acte, en salaire net en un an c'est 30 % ». *Ces mots sont relevés à `methode/arbitrages.md` sur `main`, où le pilotage a versé l'entrée ; ce fil ne les a pas reçus de l'auteure.* *Exécuté* : § 4 et § 5 du registre de calcul, lignes D38 et D43 à 30 % ; 0,45 · 0,90 · 0,90 · 0,90 et 2,98 · 5,96 · 5,96 · 5,96. *Déduit* : coupes de 48,93 · 85,22 · 109,11 · 112,71 Md€, contre 56,34 · 100,05 · 123,97 · 127,57 ; solde en mesure de +15,54 · −29,24 · −5,35 · −1,75. *Tranché en propre, révocable* : 30 % sur toute la fenêtre 2027-2030, aucune pièce ne fixant le passage au plein (indemnité d'une à sept années, amendement n° 26) ; 16,00 Md€ par an restent « à terme ».

### Repères du § 14 rejoués sur la table A retrouvée — 20261116

*Relevé.* `appareil/controle_liasse_classeurs.py reperes` : 51 repères `A!Kn/Ln` sur 51 concordent avec `sources/projet_20261116/23_tsv_suivi_depenses__A_Credits.tsv` (programme, catégorie, statut « arrêté », montants arrêtés égaux au brut de la table de paramètres). *Relevé* à l'onglet « Mesure » : la catégorie 22 suit la catégorie 21 ; la liasse ne la retire pas, 269 422 581 € en 2027.

---

## 10. Ce que ce fil a reçu, et de qui

Aucun message de l'auteure. Le mandat et quatre messages viennent du fil de pilotage, `session_01VynsZnrEusr42WSGSHbdEg`, session parente de ce fil (*relevé* aux métadonnées de la session). Le premier message est arrivé comme un tour d'entrée et a été exécuté. Les deux suivants sont arrivés par la file de notifications : ce fil les a d'abord rendus sans les exécuter, puis exécutés au quatrième message (« go »), après avoir relevé que l'expéditeur est sa session parente et que l'entrée validée est à `methode/arbitrages.md` sur `main`. Toute décision dite « de l'auteure » dans ce document est donc **héritée du pilotage**, sauf la réponse sur les départs d'agents, relevée au registre des arbitrages.
