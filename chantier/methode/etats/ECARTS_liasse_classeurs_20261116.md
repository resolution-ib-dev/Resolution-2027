# Écarts entre la liasse de crédits et les classeurs — 20261116

**Porteur** : fil d'exécution « liasse-paramètres », lancé par le pilotage.
**Mandat** : chantiers n° 3 et 5 de `PILOTAGE.md`. Aucun amendement, aucun module existant, aucun classeur n'est modifié.
**Pièces** : `referentiels/parametres_credits_20261116.tsv` et sa note ; `appareil/controle_liasse_classeurs.py`, qui produit toutes les tables ci-dessous (`ecarts`).
**Convention** : chaque table dit en tête si ses chiffres sont *relevés*, *hérités* ou *déduits*. Montants en euros.

---

## 1. Le constat du pilotage, rejoué

*Relevé.* Les 22 amendements portent 57 lignes de programme : **43 688 020 914 € d'AE et 39 795 849 238 € de CP** (somme des lignes ; les totaux imprimés donnent 43 688 020 912 et 39 795 849 239, écart d'arrondi).

*Relevé, puis déduit.* La règle de `chaine_credits.py`, jouée sur `Données PAP 2026` du classeur du site, **redonne les 57 montants à 1 € près** :

- 47 programmes : brut × fraction de la catégorie ; titre 2 à 0,90 × 6/12 × 30 % ; CP au résiduel ;
- 9 programmes écrêtés au crédit ouvert de l'état B 2027 : 110, 131, 147, 209, 334, 343, 348, 384, 385 ;
- le programme 203, corrigé à la main le 16 novembre (entretien des routes exclu).

**Aucun socle, aucun rythme, sauf sur le titre 2.** Le constat tient, avec une précision : les rémunérations portent déjà le socle de 10 % et l'indemnité de 70 %.

*Relevé.* Le périmètre retenu est celui d'`Economies R` : drapeau « Oui » pour les subventions, programmes hors « périmètre essentiel » pour les rémunérations, le fonctionnement et l'investissement. La somme de ce périmètre, 67 494,2 M€ d'AE et 73 160,9 M€ de CP, est celle de la table A absente : **ses montants « arrêtés » sont bruts**. La prémisse de l'en-tête de `chaine_credits.py` est fausse.

---

## 2. Écart par amendement

Trois lectures du paramètre, toutes *déduites* du TSV :

- **classeurs** : brut × taux × part de première année de `SynthèseR`. Année pleine, sans date ;
- **registre § 4** : brut × (1 − socle) × rythme × fraction d'exercice, CP au résiduel ;
- **classeur × part d'année** : taux et rythme du classeur, date du § 4, CP au résiduel.

« Sans paramètre » : montant de la liasse que la lecture ne sait pas chiffrer. Il n'entre pas dans l'écart.

### Autorisations d'engagement

| n° | mission | liasse, AE | classeurs, AE | écart | registre § 4, AE | écart | sans paramètre au classeur | au registre |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Cohésion des territoires | 13 292 801 242 | 10 102 003 708 | 2 771 507 735 | 6 288 264 332 | 6 415 347 111 | 419 289 799 | 589 189 799 |
| 2 | Travail, emploi et administration des ministères sociaux | 12 065 359 297 | 4 076 907 334 | 6 590 588 452 | 2 510 915 628 | 7 184 156 932 | 1 397 863 511 | 2 370 286 736 |
| 3 | Aide publique au développement | 2 334 755 315 | 1 432 789 241 | 886 966 074 | 802 276 460 | 1 517 478 855 | 15 000 000 | 15 000 000 |
| 4 | Écologie, développement et mobilité durables | 3 605 103 562 | 2 483 605 454 | 347 975 403 | 1 663 125 513 | 1 168 455 344 | 773 522 705 | 773 522 705 |
| 5 | Relations avec les collectivités territoriales | 3 760 085 443 | 10 624 298 | 694 501 | 9 999 339 | 1 319 460 | 3 748 766 644 | 3 748 766 644 |
| 6 | Culture | 2 027 866 360 | 1 497 627 395 | 202 967 698 | 1 149 160 072 | 551 435 021 | 327 271 267 | 327 271 267 |
| 7 | Sport, jeunesse et vie associative | 1 005 644 806 | 748 376 870 | 255 284 523 | 510 412 932 | 492 373 104 | 1 983 413 | 2 858 770 |
| 8 | Immigration, asile et intégration | 1 259 249 135 | 1 225 907 422 | 33 341 713 | 702 444 550 | 556 804 585 | 0 | 0 |
| 9 | Santé | 781 560 604 | 1 261 590 761 | −480 030 157 | 658 835 060 | 122 725 544 | 0 | 0 |
| 10 | Recherche et enseignement supérieur | 772 662 106 | 497 159 329 | 275 502 777 | 393 531 888 | 379 130 218 | 0 | 0 |
| 11 | Médias, livre et industries culturelles | 674 689 892 | 549 079 207 | 125 610 685 | 522 553 708 | 152 136 184 | 0 | 0 |
| 12 | Économie | 630 363 522 | 687 597 601 | −60 369 079 | 617 990 154 | 9 238 368 | 3 135 000 | 3 135 000 |
| 13 | Direction de l’action du Gouvernement | 513 541 367 | 600 829 135 | −87 287 768 | 490 197 888 | 23 343 479 | 0 | 0 |
| 14 | Transformation et fonction publiques | 207 779 344 | 238 735 865 | −30 956 521 | 205 153 818 | 2 625 526 | 0 | 0 |
| 15 | Enseignement scolaire | 225 417 181 | 405 750 926 | −180 333 745 | 225 417 181 | 0 | 0 | 0 |
| 16 | Action extérieure de l’État | 205 826 724 | 301 129 586 | −95 302 862 | 192 170 701 | 13 656 023 | 0 | 0 |
| 17 | Solidarité, insertion et égalité des chances | 102 086 614 | 87 818 593 | 14 268 021 | 51 042 786 | 51 043 828 | 0 | 0 |
| 18 | Agriculture, alimentation, forêt et affaires rurales | 92 065 085 | 162 195 777 | −70 130 692 | 109 063 404 | −16 998 319 | 0 | 0 |
| 19 | Administration générale et territoriale de l’État | 68 670 672 | 61 803 605 | 6 867 067 | 34 335 336 | 34 335 336 | 0 | 0 |
| 20 | Sécurités | 49 278 164 | 71 670 127 | −22 391 963 | 63 952 785 | −14 674 621 | 0 | 0 |
| 21 | Justice | 6 924 880 | 11 772 297 | −4 847 417 | 11 079 809 | −4 154 929 | 0 | 0 |
| 22 | Conseil et contrôle de l’État | 6 289 599 | 11 544 149 | −5 254 550 | 8 160 167 | −1 870 568 | 0 | 0 |
| | **Total** | **43 688 020 914** | **26 526 518 680** | **10 474 669 895** | **17 220 083 511** | **18 637 906 482** | **6 686 832 339** | **7 830 030 921** |

Écarts d'AE par programme, classeurs : en trop 12 720 696 455, en moins −2 246 026 560, en valeur absolue 14 966 723 015.
Écarts d'AE par programme, registre § 4 : en trop 19 266 363 456, en moins −628 456 974, en valeur absolue 19 894 820 429.

### Crédits de paiement

| n° | liasse, CP | classeurs, CP | écart | registre § 4, CP | écart | sans paramètre au classeur | au registre |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 13 129 046 079 | 10 133 948 166 | 2 693 679 977 | 6 229 070 994 | 6 428 657 149 | 301 417 936 | 471 317 936 |
| 2 | 10 695 643 750 | 4 264 718 002 | 5 063 812 237 | 2 288 648 472 | 6 285 345 497 | 1 367 113 511 | 2 121 649 781 |
| 3 | 2 185 603 430 | 1 171 572 951 | 1 002 780 479 | 555 657 154 | 1 618 696 276 | 11 250 000 | 11 250 000 |
| 4 | 3 160 655 375 | 2 420 660 081 | 159 853 265 | 1 469 620 545 | 1 110 892 801 | 580 142 029 | 580 142 029 |
| 5 | 2 814 605 562 | 10 968 760 | −7 938 181 | 3 226 779 | −196 200 | 2 811 574 983 | 2 811 574 983 |
| 6 | 1 743 251 527 | 1 428 996 185 | 73 306 198 | 924 869 569 | 577 432 814 | 240 949 144 | 240 949 144 |
| 7 | 974 423 297 | 712 488 397 | 261 092 448 | 462 955 521 | 510 460 649 | 842 452 | 1 007 127 |
| 8 | 1 257 002 837 | 1 261 365 883 | −4 363 046 | 700 198 252 | 556 804 585 | 0 | 0 |
| 9 | 779 217 127 | 1 264 586 244 | −485 369 117 | 655 085 497 | 124 131 630 | 0 | 0 |
| 10 | 670 132 264 | 484 547 596 | 185 584 668 | 311 304 915 | 358 827 349 | 0 | 0 |
| 11 | 568 920 102 | 534 153 416 | 34 766 686 | 411 829 845 | 157 090 257 | 0 | 0 |
| 12 | 556 598 409 | 762 722 226 | −208 475 067 | 531 670 773 | 22 576 386 | 2 351 250 | 2 351 250 |
| 13 | 368 209 896 | 627 784 436 | −259 574 540 | 355 353 658 | 12 856 238 | 0 | 0 |
| 14 | 168 004 952 | 356 160 875 | −188 155 923 | 157 083 333 | 10 921 619 | 0 | 0 |
| 15 | 225 417 181 | 405 831 926 | −180 414 745 | 225 417 181 | 0 | 0 | 0 |
| 16 | 200 134 647 | 301 472 731 | −101 338 084 | 183 063 377 | 17 071 270 | 0 | 0 |
| 17 | 101 987 363 | 90 114 214 | 11 873 149 | 50 883 984 | 51 103 379 | 0 | 0 |
| 18 | 78 679 546 | 174 554 886 | −95 875 340 | 94 525 382 | −15 845 836 | 0 | 0 |
| 19 | 68 670 672 | 61 803 605 | 6 867 067 | 34 335 336 | 34 335 336 | 0 | 0 |
| 20 | 37 946 354 | 70 388 767 | −32 442 413 | 50 586 444 | −12 640 090 | 0 | 0 |
| 21 | 5 886 148 | 11 772 297 | −5 886 149 | 9 417 837 | −3 531 689 | 0 | 0 |
| 22 | 5 812 720 | 11 544 149 | −5 731 429 | 7 397 160 | −1 584 440 | 0 | 0 |
| **Total** | **39 795 849 238** | **26 562 155 793** | **7 918 052 141** | **15 712 202 008** | **17 843 404 981** | **5 315 641 304** | **6 240 242 249** |

### Taux et rythme du classeur, part d'année du registre

| n° | liasse, AE | taux et rythme du classeur × part d'année du § 4, AE | écart | sans paramètre | CP | écart de CP |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 13 292 801 242 | 6 370 839 177 | 6 332 772 266 | 589 189 799 | 6 310 343 048 | 6 347 385 095 |
| 2 | 12 065 359 297 | 2 080 422 811 | 6 339 786 238 | 3 645 150 248 | 1 857 815 049 | 5 441 315 409 |
| 3 | 2 334 755 315 | 787 889 256 | 1 531 866 059 | 15 000 000 | 544 132 749 | 1 630 220 681 |
| 4 | 3 605 103 562 | 1 489 622 892 | 1 341 957 965 | 773 522 705 | 1 299 802 973 | 1 280 710 373 |
| 5 | 3 760 085 443 | 10 624 298 | 694 501 | 3 748 766 644 | 3 428 452 | −397 873 |
| 6 | 2 027 866 360 | 1 008 640 045 | 691 955 048 | 327 271 267 | 780 480 532 | 721 821 851 |
| 7 | 1 005 644 806 | 407 560 494 | 595 003 003 | 3 081 309 | 358 126 426 | 615 247 880 |
| 8 | 1 259 249 135 | 618 007 882 | 641 241 253 | 0 | 615 986 214 | 641 016 623 |
| 9 | 781 560 604 | 644 075 085 | 137 485 519 | 0 | 640 091 173 | 139 125 954 |
| 10 | 772 662 106 | 301 111 790 | 471 550 316 | 0 | 213 745 630 | 456 386 634 |
| 11 | 674 689 892 | 453 977 743 | 220 712 149 | 0 | 346 293 550 | 222 626 552 |
| 12 | 630 363 522 | 581 167 107 | 46 061 415 | 3 135 000 | 498 004 816 | 56 242 343 |
| 13 | 513 541 367 | 495 996 211 | 17 545 156 | 0 | 352 724 704 | 15 485 192 |
| 14 | 207 779 344 | 200 893 884 | 6 885 460 | 0 | 153 390 357 | 14 614 595 |
| 15 | 225 417 181 | 202 875 463 | 22 541 718 | 0 | 202 875 463 | 22 541 718 |
| 16 | 205 826 724 | 182 819 896 | 23 006 828 | 0 | 173 143 366 | 26 991 281 |
| 17 | 102 086 614 | 44 471 721 | 57 614 893 | 0 | 44 302 994 | 57 684 369 |
| 18 | 92 065 085 | 112 792 140 | −20 727 055 | 0 | 97 345 490 | −18 665 944 |
| 19 | 68 670 672 | 30 901 802 | 37 768 870 | 0 | 30 901 802 | 37 768 870 |
| 20 | 49 278 164 | 66 892 142 | −17 613 978 | 0 | 52 729 404 | −14 783 050 |
| 21 | 6 924 880 | 11 772 297 | −4 847 417 | 0 | 10 006 452 | −4 120 304 |
| 22 | 6 289 599 | 8 474 392 | −2 184 793 | 0 | 7 663 697 | −1 850 977 |
| **Total** | **43 688 020 914** | **16 111 828 528** | **18 471 075 415** | **9 105 116 971** | **14 593 334 341** | **17 687 367 272** |

### Par poste du classeur

AE, lignes présentes dans la liasse, avant écrêtement.

| poste du classeur | brut PAP, AE | liasse, AE reconstituée | classeurs, première année | registre § 4 | classeur × part d'année |
|---|---:|---:|---:|---:|---:|
| Subvention ménages — APL | 16 116 735 643 | 8 058 367 822 | 5 372 245 214 | 2 686 122 607 | 2 686 122 607 |
| Subvention entreprises — Travail | 6 625 411 497 | 6 625 411 497 | 2 208 470 500 | 1 057 439 907 | 1 055 893 998 |
| Subvention collectivités — aucun poste à SynthèseR | 5 430 065 397 | 5 430 065 397 | 0 | 0 | 0 |
| Subvention opérateurs — Autres | 4 153 071 302 | 4 153 071 302 | 2 429 546 712 | 1 776 696 909 | 1 394 534 450 |
| Subvention associations — Autres | 3 947 083 674 | 3 947 083 674 | 3 552 375 306 | 1 973 541 838 | 1 776 187 652 |
| Subvention associations — APD | 3 857 396 141 | 3 857 396 141 | 1 285 798 713 | 642 899 358 | 642 899 358 |
| Subvention associations — Hébergement | 3 043 480 925 | 3 043 480 925 | 2 434 784 740 | 1 826 088 555 | 1 826 088 555 |
| Subvention associations — Travail | 2 031 759 968 | 2 031 759 968 | 677 253 323 | 557 882 843 | 418 095 123 |
| Subvention opérateurs — France Travail | 1 274 863 511 | 1 274 863 511 | 0 | 341 106 008 | 0 |
| Subvention entreprises — Autres | 1 217 768 727 | 1 217 768 727 | 1 095 991 856 | 1 217 768 727 | 1 095 991 856 |
| Subvention opérateurs — Ademe | 1 100 781 253 | 1 100 781 253 | 326 932 032 | 165 117 188 | 163 466 016 |
| Subvention ménages — Autres | 1 998 098 672 | 999 049 336 | 1 620 093 305 | 999 049 337 | 810 046 651 |
| Investissement | 939 683 576 | 939 683 576 | 798 731 041 | 751 746 863 | 798 731 041 |
| Fonctionnement | 1 626 409 575 | 813 204 788 | 1 382 448 138 | 1 301 127 659 | 1 382 448 138 |
| Subvention opérateurs — MaPrimeRénov’ | 1 303 981 782 | 651 990 891 | 1 303 981 782 | 1 173 583 604 | 1 303 981 782 |
| Subvention ménages — AME | 1 216 300 000 | 608 150 000 | 1 094 670 000 | 547 735 000 | 547 335 000 |
| Subvention ménages — Emploi service | 1 180 117 879 | 590 058 940 | 354 035 364 | 0 | 0 |
| Salaires | 3 285 984 114 | 443 607 855 | 887 215 709 | 443 607 856 | 443 607 856 |
| Subvention opérateurs — Anah | 169 900 000 | 169 900 000 | 99 391 500 | 0 | 0 |

### Lecture

- **Total des écarts d'AE contre les classeurs : +10 474 669 895 €**, soit 12,72 Md€ retirés en trop et 2,25 Md€ en moins, **plus 6 686 832 339 € sans paramètre**. En CP : +7 918 052 141 €, plus 5 315 641 304 €.
- Contre le registre § 4 : **+18 637 906 482 € d'AE**, plus 7 830 030 921 € sans paramètre.
- La liasse retire **moins** que le classeur là où elle prend 6/12 d'une dépense que le classeur compte en année pleine : rémunérations, fonctionnement, aide médicale de l'État, MaPrimeRénov', autres ménages. Dix amendements sont dans ce cas : n° 9, 12, 13, 14, 15, 16, 18, 20, 21 et 22.
- Les quatre lignes témoins du pilotage, *relevées* : aide médicale de l'État, 608 150 000 € inscrits, 543 735 000 € au registre sur l'action 02 seule (547 335 000 sur le programme entier), 1 094 670 000 € au classeur ; hébergement d'urgence, 3 043 480 925 € inscrits en catégorie 64, 1 826 088 555 € au registre, 2 434 784 740 € au classeur ; programme 103, 7 558 550 632 € inscrits ; fonctionnement, 813 204 788 € inscrits pour 1 382 448 138 € au classeur.

### Sans paramètre

*Déduit.*

| objet | AE dans la liasse | pourquoi |
|---|---:|---|
| Transferts aux collectivités, catégorie 63, 20 programmes | 5 430 065 397 | `Economies R` les arrête (colonne W), `SynthèseR` n'a pas de colonne pour eux, le § 4 n'a pas de ligne |
| Subvention à France Travail, programme 102, catégorie 32 | 1 274 863 511 | le classeur chiffre sur le budget de l'opérateur (3 896 et 1 869 M€ écrits en dur), non sur la subvention ; le registre la porte (D6, D16) |
| Emploi à domicile, programme 103 (D21) | 1 676 593 718 | au classeur (« Emploi service », ⅓) ; hors du § 4, « jambe sociale » |
| Agence nationale de l'habitat, 135, catégorie 32 (D14) | 169 900 000 | au classeur (90 %, 65 % la première année) ; hors du § 4 |
| Missions locales et 103 hors particuliers employeurs | 570 693 019 | au classeur ; « non rangées » au § 14 |

Les trois premières lignes sont avant écrêtement ; la table par amendement les donne après.

---

## 3. Les dates

### Ce que portent les quatre documents

*Relevé.*

- **`registre_calcul_etatB.md` § 4** : une date et une fraction par ligne, 27 lignes. C'est le seul document qui date chaque ligne.
- **`suivi_trajectoire_20261015.md` § 1** : copie du § 4. 27 dates sur 27 identiques.
- **`registre_exceptions_dates.md`** : trois dates de 2027 sur des crédits de l'État — 1er avril (hébergement), 1er juin (dépôt des demandes d'aide au logement), 1er novembre (« établissements vivant de leur patrimoine », ligne due, sans programme). Il est muet sur les autres lignes : date commune, sans dire laquelle.
- **`flux_par_agent_20261015.md`** : aucune date par ligne. *Déduit* : son flux mensuel 2027, rejoué avec les dates du § 4, retombe à 0,001 Md€ près sur les huit agents. Il porte donc le calendrier du § 4.
- **Les deux classeurs du site** : aucune date, aucune fraction d'exercice. Recherche sur toutes les cellules de texte des onglets de synthèse, *relevé* : rien.

**Les quatre documents ne se contredisent pas entre eux. La contradiction est entre eux et `DATE_CAT`**, qui date par catégorie quand le registre date par ligne.

### Les 13 contradictions

*Relevé pour les dates, déduit pour les montants.* Une ligne du registre × une catégorie. **11 touchent la liasse, pour 22 220 344 388 € d'AE** ; D24 et D33 n'y sont pas.

| ligne | cat. | registre § 4 | suivi de trajectoire § 1 | registre des exceptions | flux par agent | `DATE_CAT` | fraction de la liasse | programmes | AE dans la liasse |
|---|---:|---|---|---|---|---|---:|---:|---:|
| D12 Ademe | 32 | 1er juil. | 1er juil. | aucune | 1er juil. (Opérateurs) | 1er janv. | 1.0 | 1 | 1 100 781 253 |
| D15 MaPrimeRénov' | 61 | 1er janv. | 1er janv. | aucune | 1er janv. (Ménages actifs — transferts monétaires) | 1er juil. | 0.5 | 1 | 651 990 891 |
| D16 Autres opérateurs | 32 | 1er juil. | 1er juil. | aucune ; 1er novembre 2027 pour les seuls « établissements vivant de leur patrimoine » (§ 2, ligne due non rattachée à un programme) | 1er juil. (Opérateurs) | 1er janv. | 1.0 | 25 | 3 650 454 102 |
| D24 Audiovisuel public | 62 | 1er juil. | 1er juil. | aucune | 1er juil. (Opérateurs) | 1er janv. | 1.0 | 6 | 0 |
| D25 Emploi et apprentissage | 62 | 1er juil. | 1er juil. | aucune | 1er juil. (Entreprises) | 1er janv. | 1.0 | 1 | 4 736 589 452 |
| D29 Hébergement d'urgence | 64 | 1er avril | 1er avril | 1er avril 2027 (§ 2, pièce 2.6-C) | 1er avril (Ménages sans revenus d'activité) | 1er janv. | 1.0 | 1 | 3 043 480 925 |
| D30 Aide publique au développement | 64 | 1er juil. | 1er juil. | aucune | 1er juil. (Associations) | 1er janv. | 1.0 | 3 | 3 857 396 141 |
| D31 Immigration et asile | 64 | 1er juil. | 1er juil. | aucune | 1er juil. (Associations) | 1er janv. | 1.0 | 1 | 938 985 853 |
| D33 France 2030, associations | 64 | 1er juil. | 1er juil. | aucune | 1er juil. (Associations) | 1er janv. | 1.0 | 4 | 0 |
| D34 Subventions culturelles | 64 | 1er juil. | 1er juil. | aucune | 1er juil. (Associations) | 1er janv. | 1.0 | 1 | 361 923 930 |
| D35 Politique de la ville | 64 | 1er juil. | 1er juil. | aucune | 1er juil. (Associations) | 1er janv. | 1.0 | 1 | 436 084 781 |
| D36 Autres associations | 64 | 1er juil. | 1er juil. | aucune | 1er juil. (Associations) | 1er janv. | 1.0 | 38 | 2 629 452 273 |
| D37 Charges courantes et achats | 31 | 1er janv. | 1er janv. | aucune | 1er janv. (Entreprises) | 1er juil. | 0.5 | 46 | 813 204 788 |

### Les 6 cas où le registre est muet

7 847 252 134 € d'AE dans la liasse.

| ligne | cat. | registre § 4 | suivi de trajectoire § 1 | registre des exceptions | flux par agent | `DATE_CAT` | fraction de la liasse | programmes | AE dans la liasse |
|---|---:|---|---|---|---|---|---:|---:|---:|
| D14 Agence nationale de l’habitat | 32 | — | — | aucune | — | 1er janv. | 1.0 | 1 | 169 900 000 |
| D21 Exonérations emploi à domicile | 61 | — | — | aucune | — | 1er juil. | 0.5 | 1 | 587 158 940 |
| D21 Exonérations emploi à domicile | 62 | — | — | aucune | — | 1er janv. | 1.0 | 1 | 1 089 434 778 |
| aucune | 63 | — | — | aucune | — | 1er janv. | 1.0 | 25 | 5 430 065 397 |
| non rangée | 61 | — | — | aucune | — | 1er juil. | 0.5 | 1 | 2 900 000 |
| non rangée | 64 | — | — | aucune | — | 1er janv. | 1.0 | 1 | 567 793 019 |

### Autres points de date

*Relevé.*

- **Fonctionnement, catégorie 31.** `chaine_credits.py` invoque un « arbitrage du 20261016 : le fonctionnement part avec les personnels, donc au 1er juillet ». Aucun des quatorze titres du 16 octobre de `methode/arbitrages.md` ne porte cette matière, et la phrase n'existe dans aucun autre fichier du chantier.
- **Aide au logement.** Deux dates par construction : dossiers au 1er juin, versements au 1er juillet. La fraction est 6/12 partout.
- **Autres opérateurs.** Le 1er novembre des « établissements vivant de leur patrimoine » n'est rattaché à aucun programme : inapplicable en l'état.
- **Amendement n° 33 de la même liasse** (ligne 1867) : le recentrage de l'hébergement « prend effet au 1er janvier 2027 ». Le registre et le registre des exceptions disent 1er avril.
- **Amendement n° 34** (ligne 1901) : le chèque énergie est supprimé « au 1er janvier 2027 », 600 M€ d'économie sur l'exercice. Le § 4 dit 1er juillet et 0,30 Md€ ; l'amendement n° 4 retire 6/12.
- **Exposés des 22 amendements** : 19 portent « 1er janvier pour les personnes morales, 1er juillet pour les personnes physiques » ; deux (n° 15 et 21) le 1er juillet seul ; un (n° 19) le 1er janvier seul. Le § 4 date au 1er juillet des subventions versées à des opérateurs et à des associations.

### Les 15 concordances

| ligne | cat. | registre § 4 | suivi de trajectoire § 1 | registre des exceptions | flux par agent | `DATE_CAT` | fraction de la liasse | programmes | AE dans la liasse |
|---|---:|---|---|---|---|---|---:|---:|---:|
| D18 Aide au logement | 61 | 1er juil. | 1er juil. | 1er juin 2027 (§ 2, pièce 2.6-A : dépôt de la demande) | 1er juil. (Ménages actifs — transferts monétaires) | 1er juil. | 0.5 | 1 | 8 058 367 822 |
| D19 Aide médicale de l'État | 61 | 1er juil. | 1er juil. | aucune | 1er juil. (Ménages sans revenus d'activité) | 1er juil. | 0.5 | 1 | 604 150 000 |
| D20 Chèque énergie | 61 | 1er juil. | 1er juil. | aucune | 1er juil. (Ménages actifs — transferts monétaires) | 1er juil. | 0.5 | 1 | 317 350 000 |
| D22 Autres ménages | 61 | 1er juil. | 1er juil. | aucune | 1er juil. (Ménages actifs — transferts monétaires) | 1er juil. | 0.5 | 19 | 685 699 336 |
| D26 France 2030, entreprises | 62 | 1er janv. | 1er janv. | aucune | 1er janv. (Entreprises) | 1er janv. | 1.0 | 4 | 0 |
| D27 Autres entreprises | 62 | 1er janv. | 1er janv. | aucune | 1er janv. (Entreprises) | 1er janv. | 1.0 | 24 | 1 220 087 591 |
| D32 Aide à l'emploi et à l'insertion | 62 | 1er janv. | 1er janv. | aucune | 1er janv. (Ménages actifs — services en nature) | 1er janv. | 1.0 | 1 | 797 068 403 |
| D32 Aide à l'emploi et à l'insertion | 64 | 1er janv. | 1er janv. | aucune | 1er janv. (Ménages actifs — services en nature) | 1er janv. | 1.0 | 1 | 1 044 603 786 |
| D37 Charges courantes et achats | 51 | 1er janv. | 1er janv. | aucune | 1er janv. (Entreprises) | 1er janv. | 1.0 | 20 | 588 644 429 |
| D37 Charges courantes et achats | 52 | 1er janv. | 1er janv. | aucune | 1er janv. (Entreprises) | 1er janv. | 1.0 | 11 | 41 172 799 |
| D37 Charges courantes et achats | 53 | 1er janv. | 1er janv. | aucune | 1er janv. (Entreprises) | 1er janv. | 1.0 | 17 | 309 866 348 |
| D38 Départs de fonctionnaires de l'État | 21 | 1er juil. | 1er juil. | aucune | 1er juil. (Agents publics) | 1er juil. | 0.5 | 13 | 432 733 293 |
| D38 Départs de fonctionnaires de l'État | 23 | 1er juil. | 1er juil. | aucune | 1er juil. (Agents publics) | 1er juil. | 0.5 | 8 | 10 874 563 |
| D5 France Compétences / CPF | 32 | 1er janv. | 1er janv. | aucune | 1er janv. (Ménages actifs — services en nature + Entreprises) | 1er janv. | 1.0 | 1 | 614 567 848 |
| D6 France Travail | 32 | 1er janv. | 1er janv. | aucune | 1er janv. (Ménages actifs — services en nature + Entreprises) | 1er janv. | 1.0 | 1 | 1 162 912 863 |

---

## 4. Les paramètres du § 4 face aux classeurs du site

*Relevé* sur `Détail Economies` (colonnes D, F, G) et `SynthèseR` ; table complète en sortie de `construire`.

| paramètre | identique | diffère | registre seul |
|---|---|---|---|
| **F, régime plein** | 24 lignes, à l'arrondi du registre | D16 (2,745 au registre, 4,116 au classeur) · D41 (12,3 / 12,21) · D43 (20,0 / 19,864) | — |
| **socle** | D5, D16, D19, D29, D38, D40 ; et l'absence de socle sur D18, D24, D25, D26, D30, D32, D33 | D12 (10 % / 16,3 %) · D15 (10 % / aucun) · D37 (20 % / 15 % hors routes) · D20, D22, D27, D31, D34, D35, D36 (aucun au registre / 10 % au classeur) | D6 ; D43 (15 % « par défaut », le classeur dit « 10 à 20 % ») |
| **F net du socle** | — | — | toutes : c'est une déduction du registre |
| **rythme** | D15, D18, D19, D20, D22, D24, D25, D26, D27, D29, D30, D31, D32, D33, D34, D35, D36, D37 | D5 (⅓ / 0,65 sur la subvention, 0,36 sur la ligne entière) · D12 (⅓ / 0,355) · D16 (1 / 0,65) · D38 (1 / 0,30) · D41 (⅓ / 0,79) · D42 (⅓ / 0,64) · D43 (1 / 0,30) | D6 |
| **acteur et incidence** | D5, D6, D18, D20, D22, D25, D26, D27, D32, D40, D41 | D33, D38, D43 | les autres : colonnes R à V vides |
| **date 2027, fraction** | — | — | toutes |
| **montant 2027** | — | — | toutes ; le classeur donne une « année 1 » de douze mois (colonne D) |
| **programme porteur** | par programme, à `Economies R` | — | le découpage par action du § 14 ; les parts « 5 % » et « 20 % » de D5 et D6 |

D25 : le registre écrit « 1/6, déjà net de la date », soit ⅓ × 6/12 ; le classeur écrit ⅓. Même rythme.
Dans `SynthèseR`, le chèque énergie (D20) et l'immigration (D31) n'ont pas de poste : ils sont dans « Autres », à 90 %.

---

## 5. Ce qui ne se trouverait que dans les deux classeurs absents

| classeur absent | ce que le registre y lit | état |
|---|---|---|
| `Suivi dépenses — crédits et vecteurs_20261007.xlsx`, `A — Crédits`, colonnes K et L, « Statut doctrine » | l'assiette par programme × catégorie | **retrouvée** depuis le classeur du site, totaux à 0,05 M€ près, liasse à 1 € près |
| même classeur, numéros de ligne `A!K…/L…` du § 14 (D16, D22, D27, D32) | 63 repères | **non vérifiables** ; les programmes et catégories qu'ils désignent sont au TSV |
| même classeur, onglet `Mesure` | la phrase sur laquelle `chaine_credits.py` tient le socle pour déjà appliqué | **seule pièce réellement manquante**, et sans effet : les montants prouvent le contraire |
| même classeur, `A — Contrôle mission`, `B1 — Vecteur taxes affectées` | part arrêtée par mission ; taxes de France Compétences | hors du champ des crédits |
| `Synthèse Calculs Résolution_0910.xlsx`, `Détail Economies`, F, G, R à V | F, socle, incidence du § 4 | **son descendant est sur le site** ; trois valeurs de F ont changé depuis (D16, D41, D43), ainsi que la note G37 |

**Rien n'est à demander à l'auteure sur ces deux classeurs.** Ce qui manque n'est dans aucun classeur : la date et la fraction de chaque ligne (registre seul), et le sort de la catégorie 63.

---

## 6. Questions à l'auteure

Six questions fermées. Elles passent par le pilotage.

**1. La liasse retire-t-elle une année pleine ou la part de 2027 ?**
- a) la première année du classeur, sur douze mois ;
- b) le taux et le rythme du classeur, pour les seuls mois qui suivent la date d'effet ;
- c) le montant brut × la part d'année, comme aujourd'hui.

*Piste : b.* Un crédit de 2027 ne se retire que pour les mois où la dépense s'arrête.
*Ce que ça change* : a) 26,5 Md€ d'AE sur les lignes chiffrées ; b) 16,1 Md€ ; c) 43,7 Md€, inchangé.

**2. Quand deux dates diffèrent, laquelle l'emporte ?**
- a) la date du projet, ligne par ligne (tableau du registre) ;
- b) la date de l'outil, par nature de dépense.

*Piste : a, règle unique.* Les quatre documents disent la même chose ; l'outil est seul contre eux.
*Ce que ça change* : 11 lignes changent de date, 22,2 Md€ d'AE. Les subventions aux associations et aux opérateurs passent au 1er juillet, MaPrimeRénov' et le fonctionnement au 1er janvier, l'hébergement au 1er avril.
*La règle ne suffit pas pour* : les transferts aux collectivités (question 4) ; l'emploi à domicile, l'Anah et les missions locales, sans date au projet (question 5) ; le fonctionnement (question 3) ; le chèque énergie et l'hébergement, que les amendements n° 33 et 34 datent du 1er janvier.

**3. Le fonctionnement courant s'arrête-t-il le 1er janvier ou le 1er juillet ?**
- a) 1er janvier, comme les investissements (projet) ;
- b) 1er juillet, avec les départs d'agents (outil).

*Piste : a.* L'« arbitrage du 16 octobre » que cite l'outil n'est écrit nulle part ailleurs.
*Ce que ça change* : a) 1,38 Md€ d'AE à 85 % hors entretien des routes ; b) 0,69 Md€. La liasse inscrit 0,81 Md€.

**4. Les transferts de l'État aux collectivités restent-ils dans la liasse ?**
- a) oui, en entier (aujourd'hui : 5,43 Md€ d'AE) ;
- b) oui, par tiers sur trois ans, comme les économies des collectivités ;
- c) non, tant qu'aucun classeur ne les chiffre.

*Piste : b.* Le classeur les arrête et les compte dans les économies des collectivités, « dont financements État ».
*Ce que ça change* : a) 5,43 Md€ ; b) 1,81 Md€ ; c) 0. L'amendement n° 5 en dépend presque entier.

**5. L'emploi à domicile, l'Anah, les missions locales et la subvention à France Travail sont-ils retirés par la liasse de crédits ?**
- a) oui, au taux et au rythme du classeur ;
- b) non : ils relèvent de la première partie et du budget de la sécurité sociale.

*Piste : a pour les trois premiers ; pour France Travail, la règle du projet (10 % conservés, tiers par an, un sixième conservé en 2027).* Le projet note déjà qu'une minoration est due sur l'emploi à domicile et qu'aucune pièce ne la porte.
*Ce que ça change* : 3,69 Md€ d'AE inscrits aujourd'hui ; 1,35 Md€ en année pleine avec la piste (1,01 pour les trois premiers, 0,34 pour France Travail).

**6. Un amendement par mission, ou un par ligne d'économie ?**
- a) par mission : 22 amendements, comme aujourd'hui ;
- b) par ligne d'économie : 24 amendements, dont plusieurs à cheval sur des missions ;
- c) par ligne et par mission : 105 amendements.

*Piste : a.* Le vote des crédits se fait par mission ; le détail par ligne se lit dans la table des paramètres.
*Ce que ça change* : rien aux montants. b) et c) refont le sommaire, les exposés et les renvois du site.

---

## 7. Constats rendus au pilotage, sans question

- `SynthèseR!F32` compte 215,7 M€ de trop dans « Autres ménages » (note de lecture, § 4).
- 59 lignes que le classeur arrête ne sont pas dans la liasse, dont la mission « Investir pour la France de 2030 », l'audiovisuel public et les programmes 149, 205, 349 et 379 (note de lecture, § 5).
- Le registre range la catégorie 62 du programme 102 à D32 ; le classeur range toute la mission « Travail » en catégorie 62 à D25. Les deux ont le même rythme.
- Le registre (§ 4) garde 20 % de socle sur le fonctionnement ; la décision du 16 novembre est 85 % hors entretien des routes. Le § 4 n'est pas à jour sur cette ligne.
- L'identité des deux classeurs téléchargés avec ceux de `Site-ETNP` est héritée du pilotage ; leurs empreintes sont dans la note de lecture.

---

## 8. Contrôle

`python3 appareil/controle_liasse_classeurs.py controler --cible <classeur|registre|mixte|liasse>` — *relevé le 20261116* :

| cible | amendements en échec | code de sortie |
|---|---:|---:|
| `liasse` (la règle actuelle) | 0 sur 22 | 0 |
| `classeur` (défaut) | 22 sur 22 | 1 |
| `registre` | 21 sur 22 (le n° 15 tient) | 1 |
| `mixte` | 22 sur 22 | 1 |

`faute` : 1 000 € injectés dans la première ligne de la liasse lue en mémoire, cible `liasse` : **mordue**, un amendement en échec.

Le contrôle échoue aussi sur un programme sans ligne au TSV, sur une ligne sans paramètre, et sur un total d'amendement qui ne serait pas la somme de ses programmes.

---

## 9. Entrées de registre

### Liasse de crédits : la règle actuelle retrouvée à l'euro, et sa prémisse démentie — 20261116

*Relevé.* `chaine_credits.py`, joué sur `Données PAP 2026` du classeur du site avec les drapeaux d'`Economies R`, redonne les 57 lignes de programme des 22 amendements à 1 € près : 47 par brut × fraction, 9 écrêtées au crédit ouvert de l'état B 2027, le programme 203 par sa correction du jour. Le périmètre ainsi retenu somme à 67 494,2 M€ d'AE et 73 160,9 M€ de CP, totaux « arrêtés » de la table A du classeur de suivi absent : ces montants sont bruts. Seul le titre 2 porte un socle (0,90) et l'indemnité (70 %). *Non corrigé* : l'en-tête de `chaine_credits.py`.

### Liasse de crédits : table des paramètres et contrôle contre les classeurs — 20261116

*Exécuté.* `referentiels/parametres_credits_20261116.tsv` (285 lignes, poste du classeur × programme × catégorie, action s'il y a lieu), sa note de lecture, `appareil/controle_liasse_classeurs.py` (`construire`, `controler`, `faute`, `ecarts`) et `methode/etats/ECARTS_liasse_classeurs_20261116.md`. *Déduit* : contre la première année du classeur, la liasse retire 10,47 Md€ d'AE de trop en net (12,72 en trop, 2,25 en moins) et 6,69 Md€ sans paramètre ; contre le § 4 du registre, 18,64 Md€ de trop et 7,83 Md€ sans paramètre. *Tranché en propre* : le grain, le rattachement des lignes aux postes de `SynthèseR` (prouvé poste par poste) et aux lignes du § 4 (d'après le § 14), l'écrêtement des cibles au crédit ouvert. *Proposé, non validé* : les six questions du § 6.

### Calendrier : les quatre documents concordent, l'outil est seul contre eux — 20261116

*Relevé.* Le § 4 du registre date 27 lignes ; le suivi de trajectoire le recopie, 27 sur 27 ; le registre des exceptions ne porte que trois dates de 2027 sur des crédits de l'État, cohérentes avec lui ; le flux par agent ne porte aucune date par ligne et rejoue le § 4 à 0,001 Md€ près ; les deux classeurs du site ne portent aucune date. `DATE_CAT` contredit le § 4 sur 13 couples ligne × catégorie, dont 11 dans la liasse pour 22,22 Md€ d'AE ; le registre est muet sur 6 autres, 7,85 Md€. L'« arbitrage du 20261016 » sur le fonctionnement, cité par `chaine_credits.py`, n'a pas d'entrée au registre des arbitrages. *Proposé, non validé* : la date du § 4 l'emporte.

### `SynthèseR` : 215,7 M€ comptés deux fois dans « Autres ménages » — 20261116

*Relevé, puis déduit.* `SynthèseR!F32` part du brut (`Economies R!S4`) et en retranche l'aide médicale de l'État et l'emploi service nets de leur abattement de 10 % (D31, E31) : les 10 % conservés de ces deux postes, 121,6 et 118,0 M€, sont repris dans « Autres » à 90 %. *Non corrigé* : le classeur fait foi et n'est pas de ce mandat.
