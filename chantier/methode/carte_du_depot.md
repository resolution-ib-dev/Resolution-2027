# Carte du dépôt — où tout se trouve

Inscrite le 20261014. Elle remplace `methode/carte_des_domiciles_20261012.md` et
complète `methode/adressage.md`, qui porte la grammaire des adresses et le geste
d'ouverture.

**Pourquoi cette pièce existe.** Le coffre ne garde plus que sept documents. Tout
le reste du corpus vit au dépôt, et c'est ici qu'on apprend à l'y chercher. Une
pièce absente du coffre n'est pas une pièce absente du projet.

---

## Le geste d'ouverture, sans lequel rien n'est disponible

```
git clone --depth 1 https://github.com/resolution-ib-dev/Resolution-2027 depot
cp -r depot/chantier/. .
python3 depot/droit.py etat
```

Après ces trois lignes, toute adresse du corpus est valide telle quelle :
`methode/arbitrages.md`, `livrables/depot_2027/P1/4_7_abrogations_cgi.md`,
`referentiels/REF_doctrine.json`. Le préfixe `chantier/` du dépôt est effacé par
le `cp` et ne s'écrit jamais dans une règle ni dans un mandat.

Le droit fait exception : il vit à la racine du dépôt, donc sous `depot/` après
le clone — `depot/droit.py`, `depot/codes.json`, `depot/data/`.

Un fil qui n'a pas joué ces trois lignes n'a pas de corpus et ne déclare aucune
pièce absente.

---

## Ce que porte chaque dossier

État mesuré au 14 octobre 2026, `main` à `a7ed0a0`.

| dossier | pièces | poids | ce qu'on y trouve |
|---|---:|---:|---|
| `livre/` | 2 | 316 ko | **le livre EP3 en entier** — `texte_livre.json`, 180 folios, corps, postface, notes et annexes. `index_livre_EP3.md` donne le folio de chaque section. On ouvre l'index, puis le folio, jamais les 180 pages. |
| `referentiels/` | 35 | 6,9 Mo | les valeurs — `REF_doctrine.json`, `notes_manuscrit.json`, les socles des deux textes déposés, les champs rédigés, les tables de niches et de sièges, l'annexe des dépenses fiscales. |
| `reference/` | 19 | 674 ko | les textes normatifs et leurs digestions — Constitution à trois colonnes, LOLF, Déclaration de 1789, guide de légistique, règles de crédits, domaine de la loi de financement, gabarits d'exposé et de liste d'articles. |
| `methode/` | 106 | 3,0 Mo | les règles, les arbitrages, le journal, les procédures et les passations. Dont `methode/etats/`, **79 états** de fil, datés. |
| `livrables/` | 81 | 2,6 Mo | les sorties. `livrables/depot_2027/` porte les pièces d'amendement, rangées en `P1`, `P2`, `SS` et `sans_colonne`, et les liasses assemblées. |
| `appareil/` | 107 | 1,8 Mo | les générateurs et les contrôles, plus les sous-dossiers de fil — `couverture`, `fil0_regroupement`, `fil1_verification`, `tirage`. |
| `sources/` | 4 | 14 Mo | les pièces jointes lourdes — les deux projets de loi déposés, le guide de légistique et le guide budgétaire en PDF. |
| `paquet/` | 8 | 59 ko | les paquets de machine, `v1_2` à `v1_4`. |
| `input/`, `archive/`, `racine/` | 6 | 93 ko | les documents de départ, les brouillons gelés, le mode d'emploi d'installation. |

À la racine du dépôt, hors `chantier/` : `droit.py`, `codes.json`,
`extraire_legi.py`, `essai.py`, `README.md` et `data/`.

---

## Les six questions qu'on se pose, et où aller

**« Que dit le livre sur X ? »** — `livre/index_livre_EP3.md` donne le folio,
`livre/texte_livre.json` donne le texte. Les notes de fin sont aux folios 145 à
159, les annexes de 163 à 171, le détail des 236 milliards au folio 170.

**« Quel est le texte en vigueur de l'article Y ? »** —
`python3 depot/droit.py article "<intitulé du code>" "<numéro>"`. La base porte
**74 textes** au millésime LEGI du 7 octobre 2026, listés dans
`depot/codes.json`. Elle lève sur un article absent plutôt que d'approcher : une
absence est une information. `--au AAAA-MM-JJ` lit la version applicable à une
date passée. Au-delà de 45 jours, la sortie imprime `À REJOUER`.

**« Qu'est-ce qui a été arbitré sur Z ? »** — `methode/arbitrages.md` pour le
registre, `methode/fragments/arbitrages/` pour les arbitrages datés du jour, et
`methode/a_trancher.md` pour ce qui reste ouvert. Un arbitrage se vérifie au
registre avant d'être redit : une borne recopiée d'un document de méthode a déjà
traversé quatre documents en étant fausse.

**« Où en était le chantier ? »** — `methode/etats/` porte les états de fil,
datés et nommés par fil. `methode/` porte les passations, dont seule la dernière
fait foi. Le journal est à `methode/journal.md` et aux fragments de
`methode/fragments/journal/`.

**« Comment se rédige une pièce ? »** — `reference/guide_legistique.md` pour le
partage loi-règlement et la légistique, `reference/gabarit_expose_sommaire.md`
et `reference/gabarit_liste_articles.md` pour les gabarits,
`reference/regles_credits.md` pour les amendements de crédits,
`reference/domaine_lfss_LO111-3.md` pour les portes de la loi de financement,
`methode/regles_redactionnelles.md` pour le registre de rédaction.

**« Quelle pièce porte telle mesure ? »** — `livrables/depot_2027/` et ses
quatre sous-dossiers. `methode/index.json` résout les renvois,
`livrables/carte_du_projet.html` donne la vue d'ensemble.

---

## Qui fait foi

| matière | surface |
|---|---|
| le livre, les référentiels, le droit, les guides, les sources | **dépôt** |
| les pièces de liasse, la méthode, les livrables, l'appareil | **dépôt**, depuis le nettoyage du 20261014 |
| les sept pièces restées au coffre | **coffre** |

Avant le 14 octobre 2026, le coffre faisait foi sur la méthode et les
livrables. Ce n'est plus le cas : ils n'y sont plus, et le dépôt est désormais
le point de vérité pour tout ce qui ne figure pas dans la liste ci-dessous.

## Ce qui reste au coffre, et seulement cela

- `CLAUDE.md` — les instructions permanentes du chantier
- `methode/adressage.md` — la grammaire des adresses et le geste d'ouverture
- `methode/carte_du_depot.md` — la présente pièce
- `methode/appui_des_passes.md` — les règles d'appui sur les sources
- `methode/a_trancher.md` — ce qui attend un arbitrage de l'auteure
- `methode/etats/SUIVI_chantier_20261009.md` — l'état d'avancement
- `methode/passation_20261009.md` — la dernière passation

Tout le reste se clone.

---

## Verser au dépôt

Un fil Cowork lit le dépôt et ne pousse pas. Toute pièce nouvelle ou corrigée
part par un fil claude.ai/code, qui est la seule surface qui pousse — et **ce
fil n'accède pas au coffre** : les pièces qu'il doit verser lui sont jointes en
fichier ou rassemblées dans un zip.

Après un versement, `make index` déclare les pièces nouvelles, sans quoi le
contrôle les signale comme non déclarées.
