# Paquet de dépôt — courroies, 20261001

*Un seul paquet, autonome. Une session `claude.ai/code` sur
`resolution-ib-dev/Resolution-2027` l'applique sans rien avoir à demander et
sans rien avoir à lire d'autre. Elle ne voit pas le coffre : tout ce qui suit
est écrit verbatim.*

**Mesuré le 20261001 à 13 h 05 UTC+2, clone `main` à `4e6e1a4`.**

---

## Ce que ce paquet fait, et ce qu'il ne fait pas

Il porte **une seule opération** : porter à la table curée de
`appareil/generer_index.py` les **48 documents du coffre qu'elle ne déclare
pas**, et leur famille à `appareil/generer_carte.py`.

Il ne porte aucun autre module, aucun chiffre, aucun livrable. Les fragments
non assemblés ne sont **pas** son objet : ils ne sont pas au dépôt et leur
assemblage ne passe pas par une session de code (voir la note finale).

**Paquets antérieurs absorbés** : aucun. Les six paquets de dépôt que le
registre nomme — `paquet_depot_20260914`, `paquet_depot_20260916`,
`paquet_depot_machine_20260916`, `paquet_depot_confrontation_20260916`,
`paquet_depot_application_20260917`, `paquet_depot_socle_20260917` — ne sont
plus des documents du projet, et la dette qu'ils portaient est mesurée nulle
(voir « État mesuré », courroie 3). Ils ne se suppriment pas dans ce fil.

---

## État mesuré au 20261001, 13 h 05

**Le clone ne porte pas le coffre.** `main` à `4e6e1a4` contient
`chantier/Makefile`, `chantier/.gitignore`, `chantier/appareil/` (92 modules),
`chantier/referentiels/` (5 JSON), plus `data/`, `codes.json`, `droit.py`,
`essai.py`, `extraire_legi.py`, `README.md`. Il n'y a ni `methode/`, ni
`livrables/`, ni `reference/`, ni `methode/fragments/`.

**Courroie 1 — fragments.** 20 fragments déposés au coffre à l'heure de la
mesure — 22 depuis, ce fil ayant déposé les siens —, 2 assemblés
(`20260930-inscription-registre`, `20260930-versement-reprise`, tous deux au
journal), **18 en attente à la mesure, 20 à la clôture**. Aucun n'est au dépôt. Hors
objet de ce paquet — mais les deux fragments de ce fil sont déclarés à l'étape 1,
avec les 46 autres.

**Courroie 2 — table curée.** Premier delta, générateur du clone contre
`methode/index.json` du coffre : **nul**. Les deux rendent 315 artefacts, mêmes
huit comptes. *Le constat du 20260930 — 253 contre 310 — est périmé : il a été
rattrapé par le commit `4e6e1a4`.* Second delta, index contre documents réels du
projet : **48 documents déclarés nulle part**, et 52 déclarations de voie
`coffre` dont le document n'existe plus. Ce paquet traite les 48.

**Courroie 3 — modules dus.** Les 99 chemins que l'index déclare au dépôt y
sont tous présents : **dette nulle**. `plier_paquet.py` et
`controle_projection.py`, que le registre dit perdus, **sont au clone** — le
registre est périmé sur ce point. Sept modules restent déclarés `manquants`
par l'index (`epreuve_controle_socle.py`, `controle_socle_plf.py`,
`portes_ouvertes.py`, et les quatre du relevé de mandat) : ils se réécrivent, ce
n'est pas une poussée. Deux modules nommés par le registre — `index_mesures.py`
et `socle_0910.py` — ne sont **ni au dépôt, ni déclarés manquants** : trou de
déclaration, hors objet de ce paquet.

---

## Interdit formel

**Ne pas jouer `make reindex` avant que les deux insertions ci-dessous soient
appliquées.** `reindex` réécrit `methode/index.json` depuis la table curée : joué
sur la table d'avant, il reconduit les 48 absences. Il n'y a rien à détruire —
les 48 ne sont pas non plus à l’index — mais le rejeu serait à refaire.

`make index` n'est pas `reindex` : c'est `controle_index.py`, et il échoue
nécessairement dans un clone nu, qui ne porte pas le coffre. Ne pas le jouer, ne
pas le compter comme échec.

**Aucun `methode/index.json` ne se commite** : ce fichier n'est pas au dépôt. Le
seul produit poussé est le code des deux générateurs.

---

## Compte attendu, avant et après

| | avant | après |
|---|---|---|
| `generer_index.py` — artefacts | 315 | **363** |
| au coffre | 257 | **305** |
| rendus par le dépôt | 99 | 99 |
| dérivés | 73 | **90** |
| sources | 43 | 43 |
| manquants déclarés | 15 | 15 |
| sans famille | 2 | **2** |
| pièces de l'appareil au coffre comme document | 6 | **8** |
| `generer_carte.py` — artefacts classés | 313 | **361** |
| renvois morts | 15 | 15 |

**`sans famille` doit rester à 2** (`carte`, `feuille_de_route`, les deux
`HORS_FAMILLE`). Toute autre valeur vaut échec : une insertion a été faite dans
`generer_index.py` sans sa jumelle dans `generer_carte.py`.

---

## Ordre d'application

### Étape 0 — poussée d'essai sur modification nulle. **Premier geste.**

```
git -C <clone> commit --allow-empty -m "Essai de poussée — courroies 20261001"
git -C <clone> push
```

**Vaut échec et impose l'arrêt** : tout `403` du mandataire git. Le dépôt n'est
alors pas déclaré aux sources de la session ; la session s'arrête là et le dit,
sans rien modifier. Ne pas tenter d'autre voie.

**Point d'arrêt.** Ne pas enchaîner tant que la poussée d'essai n'est pas
passée.

### Étape 1 — insertion dans `chantier/appareil/generer_index.py`

Ancre, unique dans le fichier, à l'intérieur de la liste `ARTEFACTS` :

```
    # ------------------------------------------------------------------ racine
```

Insérer le bloc ci-dessous **immédiatement avant** cette ligne, sans la
modifier. 48 tuples, format `(role, chemin, rang, coffre, produit_par,
consomme_par, alias)`.

```python
    # ------------------------------------------- rattrapage du 20261001 (fil courroies)
    # Quarante-six documents du coffre absents de la table curée. Déclarés par
    # leur adresse, au sens de l'arbitrage du 20260917 sur le classement par
    # dossier : un fait vérifiable sur où le document vit, non un jugement de
    # contenu. Consommateur générique, à préciser quand le document s'ouvre.
    ('fragment_journal_20260930_table_de_passage',
     'methode/fragments/journal/20260930-table-de-passage.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20260930_correction_forfaits_cotisation',
     'methode/fragments/journal/20260930-correction-forfaits-cotisation.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20260930_perimetre_fiscal',
     'methode/fragments/journal/20260930-perimetre-fiscal.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20260930_sort_prelevements',
     'methode/fragments/journal/20260930-sort-prelevements.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20260930_arbitrages_phase1',
     'methode/fragments/journal/20260930-arbitrages-phase1.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20261001_courroies',
     'methode/fragments/journal/20261001-courroies.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20261001_lecture_2027',
     'methode/fragments/journal/20261001-lecture-2027.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_cle_de_passage',
     'methode/fragments/arbitrages/20260930-cle-de-passage.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_correction_cle_de_passage',
     'methode/fragments/arbitrages/20260930-correction-cle-de-passage.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_csa_forfaits_de_cotisation',
     'methode/fragments/arbitrages/20260930-csa-forfaits-de-cotisation.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_defauts_reconciliation',
     'methode/fragments/arbitrages/20260930-defauts-reconciliation.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_perimetre_fiscal',
     'methode/fragments/arbitrages/20260930-perimetre-fiscal.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_sort_prelevements',
     'methode/fragments/arbitrages/20260930-sort-prelevements.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_arbitrages_phase1',
     'methode/fragments/arbitrages/20260930-arbitrages-phase1.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_sort_prelevements_decisions',
     'methode/fragments/arbitrages/20260930-sort-prelevements-decisions.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20261001_epargne_salariale_et_affectataires',
     'methode/fragments/arbitrages/20261001-epargne-salariale-et-affectataires.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20261001_courroies',
     'methode/fragments/arbitrages/20261001-courroies.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_a_trancher_20260930_sort_prelevements',
     'methode/fragments/a_trancher/20260930-sort-prelevements.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_a_trancher_20261001_courroies',
     'methode/fragments/a_trancher/20261001-courroies.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('socle_prompt_fil', 'methode/socle_prompt_fil.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_courroies', 'methode/prompt_fil_courroies.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_lecture_textes_2027',
     'methode/prompt_fil_lecture_textes_2027.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_carto', 'methode/prompt_fil_carto.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_design_graphique', 'methode/prompt_fil_design_graphique.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_site_pages_bande', 'methode/prompt_fil_site_pages_bande.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_window_dressing_site', 'methode/prompt_fil_window_dressing_site.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('audit_derives_20260924', 'methode/audit_derives_20260924.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('cr_site_arret_mesure_20260923', 'methode/cr_site_arret_mesure_20260923.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('charte_visuelle', 'reference/charte_visuelle.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('index_livre_EP3', 'livre/index_livre_EP3.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('sort_prelevements_md', 'livrables/sort_prelevements_20260930.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('reconciliation_sources_fiscales_20260930',
     'livrables/reconciliation_sources_fiscales_20260930.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('couverture_table_de_passage_20260930',
     'livrables/couverture_table_de_passage_20260930.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('graphiques_index', 'livrables/graphiques/index.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('etat_carto_20260924', 'livrables/etat_carto_20260924.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('manifeste_20260924', 'livrables/manifeste_20260924.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('manifeste_20260923', 'livrables/manifeste_20260923.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('releve_passe_825_534_20260923', 'livrables/releve_passe_825_534_20260923.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('rapprochement_proto_20260921', 'livrables/rapprochement_proto_20260921.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('etat_site_20260921', 'livrables/etat_site_20260921.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('digestion_archives_20260921', 'livrables/digestion_archives_20260921.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('reconfirmation_chiffres_20260921', 'livrables/reconfirmation_chiffres_20260921.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('zip_doctrine_lisezmoi', 'livrables/zip_doctrine_lisezmoi.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('zip_doctrine_regles_de_lecture', 'livrables/zip_doctrine_regles_de_lecture.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('extrait_classeurs_anterieurs_20260917',
     'livrables/extrait_classeurs_anterieurs_20260917.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('ecart_classeurs_20260917', 'livrables/ecart_classeurs_20260917.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('sort_prelevements_tsv', 'referentiels/sort_prelevements_20260930.tsv', 'referentiel',
     True, None, ["lecture de l'auteur"], []),
    ('table_passage_schema_prelevements',
     'referentiels/table_passage_schema_prelevements_20260930.tsv', 'referentiel',
     True, None, ["lecture de l'auteur"], []),
```

### Étape 2 — seconde insertion dans le même fichier

Ancre, unique, dans la table `COFFRE_DOCUMENT` :

```
    'referentiels/prelevements_forces_20260930.tsv':
        'referentiels/prelevements_forces_20260930.tsv',
```

Insérer **immédiatement après** ces deux lignes :

```python
    # Rattrapage du 20261001 : deux grilles du fil du sort des prélèvements,
    # au coffre à leur propre chemin et absentes du dépôt.
    'referentiels/sort_prelevements_20260930.tsv':
        'referentiels/sort_prelevements_20260930.tsv',
    'referentiels/table_passage_schema_prelevements_20260930.tsv':
        'referentiels/table_passage_schema_prelevements_20260930.tsv',
```

Sans cette insertion, les deux TSV sortent de rang `referentiel` en voie
`depot` : `restaurer.py` les chercherait au clone, où ils ne sont pas.

### Étape 3 — insertion dans `chantier/appareil/generer_carte.py`

Ancre, unique :

```
IMPLICITES = {
```

Insérer le bloc ci-dessous **immédiatement après** cette ligne. 48 entrées,
une par artefact de l'étape 1.

```python
    # --- rattrapage du 20261001, fil courroies : familles affectées par
    # l'adresse du document, au sens de l'arbitrage du 20260917 — un fait
    # vérifiable sur où le document vit, que toute ligne de carte contredit.
    'methode/fragments/journal/20260930-table-de-passage.md': 'méthode',
    'methode/fragments/journal/20260930-correction-forfaits-cotisation.md': 'méthode',
    'methode/fragments/journal/20260930-perimetre-fiscal.md': 'méthode',
    'methode/fragments/journal/20260930-sort-prelevements.md': 'méthode',
    'methode/fragments/journal/20260930-arbitrages-phase1.md': 'méthode',
    'methode/fragments/journal/20261001-courroies.md': 'méthode',
    'methode/fragments/journal/20261001-lecture-2027.md': 'méthode',
    'methode/fragments/arbitrages/20260930-cle-de-passage.md': 'méthode',
    'methode/fragments/arbitrages/20260930-correction-cle-de-passage.md': 'méthode',
    'methode/fragments/arbitrages/20260930-csa-forfaits-de-cotisation.md': 'méthode',
    'methode/fragments/arbitrages/20260930-defauts-reconciliation.md': 'méthode',
    'methode/fragments/arbitrages/20260930-perimetre-fiscal.md': 'méthode',
    'methode/fragments/arbitrages/20260930-sort-prelevements.md': 'méthode',
    'methode/fragments/arbitrages/20260930-arbitrages-phase1.md': 'méthode',
    'methode/fragments/arbitrages/20260930-sort-prelevements-decisions.md': 'méthode',
    'methode/fragments/arbitrages/20261001-epargne-salariale-et-affectataires.md': 'méthode',
    'methode/fragments/arbitrages/20261001-courroies.md': 'méthode',
    'methode/fragments/a_trancher/20260930-sort-prelevements.md': 'méthode',
    'methode/fragments/a_trancher/20261001-courroies.md': 'méthode',
    'methode/socle_prompt_fil.md': 'méthode',
    'methode/prompt_fil_courroies.md': 'méthode',
    'methode/prompt_fil_lecture_textes_2027.md': 'méthode',
    'methode/prompt_fil_carto.md': 'méthode',
    'methode/prompt_fil_design_graphique.md': 'méthode',
    'methode/prompt_fil_site_pages_bande.md': 'méthode',
    'methode/prompt_fil_window_dressing_site.md': 'méthode',
    'methode/audit_derives_20260924.md': 'méthode',
    'methode/cr_site_arret_mesure_20260923.md': 'méthode',
    'reference/charte_visuelle.md': 'méthode',
    'livre/index_livre_EP3.md': 'doctrine',
    'referentiels/sort_prelevements_20260930.tsv': 'grilles',
    'referentiels/table_passage_schema_prelevements_20260930.tsv': 'grilles',
    'livrables/sort_prelevements_20260930.md': 'bac à sable',
    'livrables/reconciliation_sources_fiscales_20260930.md': 'bac à sable',
    'livrables/couverture_table_de_passage_20260930.md': 'bac à sable',
    'livrables/graphiques/index.md': 'graphique',
    'livrables/etat_carto_20260924.md': 'bac à sable',
    'livrables/manifeste_20260924.md': 'bac à sable',
    'livrables/manifeste_20260923.md': 'bac à sable',
    'livrables/releve_passe_825_534_20260923.md': 'bac à sable',
    'livrables/rapprochement_proto_20260921.md': 'bac à sable',
    'livrables/etat_site_20260921.md': 'bac à sable',
    'livrables/digestion_archives_20260921.md': 'bac à sable',
    'livrables/reconfirmation_chiffres_20260921.md': 'bac à sable',
    'livrables/zip_doctrine_lisezmoi.md': 'bac à sable',
    'livrables/zip_doctrine_regles_de_lecture.md': 'bac à sable',
    'livrables/extrait_classeurs_anterieurs_20260917.md': 'bac à sable',
    'livrables/ecart_classeurs_20260917.md': 'bac à sable',
```

### Étape 4 — contrôle, et c'est le seul

```
cd chantier/appareil && python3 generer_index.py /tmp/index_essai.json ..
```

La sortie doit lire, mot pour mot sur les nombres :

```
/tmp/index_essai.json écrit — 363 artefacts dont 305 au coffre, 99 rendus par le dépôt, 90 dérivés, 43 sources, 15 manquant(s) déclaré(s)
    8 pièce(s) de l'appareil encore au coffre comme document, dues au dépôt :
```

puis :

```
cd chantier/appareil && python3 generer_carte.py /tmp/index_essai.json /tmp/carte_essai.html
```

doit lire :

```
/tmp/carte_essai.html écrit — 11 familles, 361 artefacts classés, 15 renvoi(s) mort(s)
```

**Vaut échec et impose l'arrêt** : un nombre qui diffère, une trace d'erreur,
ou un `sans famille` supérieur à 2 dans le JSON produit
(`python3 -c "import json;d=json.load(open('/tmp/index_essai.json'));print(d['comptes'])"`).
En cas d'échec, ne rien pousser et rendre la sortie obtenue.

**Point d'arrêt.**

### Étape 5 — poussée

```
git -C <clone> add chantier/appareil/generer_index.py chantier/appareil/generer_carte.py
git -C <clone> commit -m "Index : les 48 documents du coffre absents de la table curée"
git -C <clone> push
```

Ne rien ajouter d'autre à ce commit. `/tmp/index_essai.json` et
`/tmp/carte_essai.html` ne se commitent pas.

### Ce que la session rend

Trois lignes : le `403` ou son absence à l'étape 0 ; les deux comptes mesurés à
l'étape 4 ; le SHA du commit poussé.

---

## Ce qui reste après, et qui n'est pas de la session de code

1. **Régénérer `methode/index.json` au coffre** depuis le clone mis à jour, et
   l'y reverser — 363 artefacts attendus. Un fil Cowork le fait ; la session de
   code ne peut pas écrire au coffre.
2. **Assembler les 18 fragments.** `appareil/fragments.py` est au clone depuis
   le 20260930 : l'assemblage se fait depuis Cowork, il n'attend plus de
   session de code.
3. **Deux trous de déclaration** : `appareil/index_mesures.py` et
   `appareil/socle_0910.py`, nommés dus par le registre, ni au dépôt ni aux
   manquants de l'index.
4. **52 déclarations de voie `coffre` sans document.** Mesuré, non traité.

---

*Un fil Cowork ne pousse pas. Ce paquet est écrit pour être appliqué ailleurs,
et il ne se donne pas son successeur.*
