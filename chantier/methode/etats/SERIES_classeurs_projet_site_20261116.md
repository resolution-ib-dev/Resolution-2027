# Classeurs du projet (9 octobre) et classeurs du site (16 novembre) — comparaison cellule à cellule, 20261116

**Porteur** : fil de pilotage. **Pièces** : `sources/projet_20261116/` (les neuf pièces jointes du projet, copie d'octets, `sha256sum -c 00_SHA256SUMS.txt` : 15 sur 15) ; `Site-ETNP/site/donnees/`. **Provenance** : tout est *relevé* par lecture des valeurs en cache des deux séries.

## Résultat

- `Dépenses de l'État.xls` du site = `PLF26 - Depenses…_0910.xls` du projet, **à neuf cellules près**, toutes à `SynthèseR` : E6, E7, F6, F7 (fonctionnement et investissement à 85 % hors entretien des routes, décision du 20261116) ; H8, H6, C8, C6 (correction de H8 constatée le 20261112, appliquée le 20261116 : 3 609,6 → 4 980,7 M€) ; C7 (somme). Les onglets `Economies R`, `Données PAP 2026`, `Crédits RAP 2024`, `Emplois RAP 2024` sont identiques.
- `Synthèse des chiffrages.xlsx` du site = `Synthèse Calculs Résolution_0910.xlsx` du projet, à 72 cellules près sur cinq onglets : report des deux points ci-dessus (opérateurs 2,745 → 4,116 ; fonctionnement, note G37), collectivités (12,3 → 12,21 ; 20 → 19,864), rendement du patrimoine (3 % → 2,9 %, 30 → 29,6), et les totaux qui en découlent (236,05 → 236,40 ; 127,35 → 129,46 la première année ; 226,2 → 227,445).
- **La série du site descend de celle du projet.** Elle fait foi pour les montants et les taux ; le registre de calcul (§ 4 et 5), bâti sur la série du 9 octobre, n'est pas à jour sur : D16 (2,745 au lieu de 4,116), D37 (socle), D41, D43.
- La passation du projet (`methode/passation_calendrier_20261116.md`) § 4 est rejouée sur le registre § 5 : concordante.

## Reste ouvert

- Départs d'agents (D38, D43) : le classeur compte 30 % la première année (70 % du traitement maintenu), le registre § 5 compte la ligne entière dès 2028. Écart de 16,1 Md€ en 2028, en mesure. La formule de crédits du § 10 retire déjà l'indemnité : la liasse 2027 n'est pas touchée. Question à l'auteur.
- Le tableau mesure × mois d'origine reste introuvable ; trois noms de fichiers à rechercher hors des deux surfaces (passation, § 1). La reconstruction est en cours au fil liasse.

## Détail des cellules

```
=== Synthèse Calculs 0910 / Synthèse des chiffrages (site)
 onglets projet: ['Annexe Manuscrit', 'CSG-CRDS', 'Flux', 'Détail Niches', 'Détail Economies', 'Refonte fiscalité', 'Input Capitalisation']
 onglets site  : ['Annexe Manuscrit', 'CSG-CRDS', 'Flux', 'Détail Niches', 'Détail Economies', 'Refonte fiscalité', 'Input Capitalisation']
 [Annexe Manuscrit] 30 cellules différentes
    C11: 29.575  →  30.1248
    C12: 9.575  →  10.2605
    C13: 20  →  19.8643
    C14: 68.948  →  68.858
    C15: 41.448  →  41.358
    C18: 12.3  →  12.21
    C27: 30  →  29.6
    C28: 18  →  17.6022
    C3: 236.0547  →  236.4022
    C4: 67.0067  →  68.242
    C5: 37.4317  →  38.1172
    C8: 8.6317  →  9.3172
    E11: 8.8725  →  8.8318
    E13: 6  →  5.9593
    E3: 127.3522  →  129.4593
    E4: 39.1042  →  41.2113
    E5: 30.2317  →  32.3795
    E8: 4.9317  →  7.0795
    F11: 20.7025  →  21.293
    F12: 6.7025  →  7.388
    F13: 14  →  13.905
    F14: 32.8  →  32.71
    F15: 20  →  19.91
    F18: 2.6  →  2.51
    F27: 30  →  29.6
    F28: 18.2092  →  17.6022
    F3: 108.9117  →  106.9429
    F4: 27.9025  →  27.0307
    F5: 7.2  →  5.7377
    F8: 3.7  →  2.2377
 [Détail Economies] 17 cellules différentes
    D39: 33.3  →  33.359
    D43: 6  →  5.9593
    E16: 0.2  →  1.571
    E3: 38.5  →  39.871
    E39: 20.1  →  19.915
    E4: 13.4547  →  14.8257
    E41: 2.6  →  2.51
    E43: 14  →  13.905
    F16: 2.7453  →  4.1163
    F3: 82.5  →  83.871
    F39: 53.4  →  53.274
    F4: 28  →  29.371
    F41: 12.3  →  12.21
    F43: 20  →  19.864
    G37: Hors régalien et éducation, 80 % d'économies  →  Hors régalien, éducation et entretien des routes nationales, 85 % d'éc
    S3: -10.15  →  -10.1093
    S43: -6  →  -5.9593
 [Flux] 15 cellules différentes
    C22: 33.3  →  33.359
    C26: 6  →  5.9593
    C6: 129.4  →  129.459
    E15: 38.5  →  39.871
    E16: 13.4547  →  14.8257
    E22: 20.1  →  19.915
    E24: 2.6  →  2.51
    E26: 14  →  13.905
    E6: 96.7  →  97.886
    G15: 82.5  →  83.871
    G16: 28  →  29.371
    G22: 53.4  →  53.274
    G24: 12.3  →  12.21
    G26: 20  →  19.864
    G6: 226.2  →  227.445
 [Input Capitalisation] 8 cellules différentes
    D10: 0.03  →  0.029
    E10: 18.2092  →  17.6022
    E2: 121.7492  →  121.9872
    E4: 103.54  →  104.385
    E5: 38.5  →  39.871
    E6: 20.1  →  19.915
    E7: 30  →  29.6
    E8: 14.94  →  14.999
 [Refonte fiscalité] 2 cellules différentes
    E4: 0.3633  →  0.3633
    F4: 1060.7544  →  1060.6954

=== PLF26 Dépenses 0910 / Dépenses de l'État (site)
 onglets projet: ['SynthèseR', 'Economies R', 'Données PAP 2026', 'Crédits RAP 2024', 'Emplois RAP 2024']
 onglets site  : ['SynthèseR', 'Economies R', 'Données PAP 2026', 'Crédits RAP 2024', 'Emplois RAP 2024']
 [SynthèseR] 9 cellules différentes
    C6: 82473.2038  →  83839.4581
    C7: 44206.0851  →  44201.2142
    C8: 38267.1187  →  39638.2439
    E6: 2731.4729  →  2704.14
    E7: 2731.4729  →  2704.14
    F6: 1052.9926  →  1075.4546
    F7: 1052.9926  →  1075.4546
    H6: 9989.5543  →  11360.6795
    H8: 3609.6019  →  4980.7271
```
