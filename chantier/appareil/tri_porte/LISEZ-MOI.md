# tri_porte — vérification des porteurs du tri des prélèvements (20261103)

Se joue depuis ce dossier (`cd appareil/tri_porte`), le dépôt de droit à `../../../data`.

1. `python3 extraire_visas.py visas.json` — articles visés par les 81 (puis 86) dispositifs, chapeaux « Sont abrogés » hérités.
2. `python3 art42.py` — tableau de l’article 42 du PLF 2027 (`art42.json`).
3. `python3 matcher.py` puis `python3 dossier.py` — sièges du tri contre visas (`match.json`, `dossier.json`).
4. `python3 relecture.py` — relecture croisée des annexes (`relecture.json`).
5. `python3 hors120.py`, `python3 inverse.py`, `python3 niches.py` — rangs hors annexe A, contrôle inverse, niches.
6. `verdicts.py` porte les verdicts tranchés sur pièce (annexe A) ; `amendements.py` le texte des cinq amendements nouveaux.
7. `python3 verser_amendements.py` — fiches et ajout aux liasses (refuse un second ajout).
8. `python3 construire_tri.py`, `python3 tables.py`, `python3 classeurs.py` — tri du 20261103, tables et classeurs de `livrables/tri_prelevements/`.

`classeurs.py` contrôle mécaniquement la version exportable : aucune mention interne, aucune décimale au-delà de 10.
