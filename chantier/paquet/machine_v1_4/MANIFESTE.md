# Manifeste — machine amendement 2027, version 1.4 (recalée sur les textes enregistrés)

**Porteur** : fil Cowork de reprise de la machine, 20261005. **Mandat** : l'auteure, 20261005 —
« il faut recaler correctement, ça fait partie des exigences ». **Domicile** : zip remis à l'auteure ;
au projet, ce manifeste seul. **Mesure d'entrée** : v1.3 (`b237c7d0…`), 29 fichiers.

**Non transmissible** : passe 1 jouée, passe 2 à rejouer sur le tirage enregistré, passe 3 non jouée.

**Zip** : `machine_amendement_2027_v1.4.zip`, 29 fichiers, 130 725 octets,
sha256 `32cc3330922108cd1cae7907a21cd98362f0817ec32e03483f4d693502ffe4b4`.

## Pièces de référence

Textes enregistrés à l'Assemblée nationale, au dépôt sous `chantier/sources/` :
PLF 2027 n° 3210, `132274b83bed4861a9e1a147d0d16abda2d729cdad2373ef804e26747c43d881`, 349 pages ;
PLFSS 2027 n° 3211, `47f5fc0d1581c90634449516281070495b92cfe062c20c2a366919622906eab6`, 138 pages.
Elles remplacent les tirages `b0b802d3…` et `71010873…`, hors d'atteinte et absents du dépôt.

## Ce qui change par rapport à la v1.3

- `appareil/socle_texte_2027.py` et `appareil/redaction_2027.py` : ceux du dépôt `main` (article 23
  du PLF, annexes adressables) — le paquet portait un état antérieur.
- `appareil/index_mesures_2027.py` : numéros d'alinéa du texte enregistré retirés avant découpage.
  Sans cette correction, 139 et 50 mesures au lieu de 1 013 et 396.
- `appareil/portes_ouvertes.py` : numéros d'alinéa blanchis, blancs ramenés à un seul après
  blanchiment, rattachement « de la loi » toléré sur retour à la ligne.
- `appareil/controle_sortie.py` : l'exception des référentiels de rédaction couvre leur nom millésimé.
- Les quatre relevés joints sont régénérés sur les textes enregistrés.
- `LISEZ-MOI.md` : commandes du § 6 corrigées (la troisième entrée de `redaction_2027.py` est
  l'intitulé de la pièce, non le relevé ; noms millésimés), § 8 version 1.4, § 9 empreintes et comptes.

## Passe 1 — jouée le 20261005

| référentiel | résultat |
|---|---|
| `socle_texte_plf2027.json`, `socle_texte_plfss2027.json` | identiques à l'octet aux socles du dépôt |
| `redaction_plf2027.json`, `redaction_plfss2027.json` | identiques à l'octet à ceux du dépôt |
| `articles_ouverts_plf2027.tsv` (442 · 61 textes), `..._plfss2027.tsv` (155 · 23) | identiques à l'octet d'une exécution à l'autre ; remplacent ceux du dépôt, tirés de l'ancien tirage |
| `releves_transversaux_plf2027.tsv` (1 013), `..._plfss2027.tsv` (396) | idem |

**Écart avec les relevés de la v1.2**, à porter à la passe 2 : PLF, 394 couples communs, 48 nouveaux,
27 disparus ; PLFSS, 149 communs, 6 nouveaux, 4 disparus. Contre le droit en vigueur, la part
d'adresses retrouvées est la même qu'avant (269 au PLF, 100 au PLFSS) : les écarts tiennent surtout au
rattachement des adresses à leur pièce et aux articles créés par les textes.

## Contrôles

Épreuve du contrôle verte ; 0 fuite sur 28 pièces, avec et sans motifs locaux ; huit modules
compilés ; rendu du mini-lot conforme (1 amendement, 37 160 octets).

## Dépôt

Paquet `paquet_depot_A2ter_20261005.zip`, étendu : `portes_ouvertes.py`, `index_mesures_2027.py`
et les quatre relevés, avec mesure d'entrée. À remettre à une session de code.

## Les 29 fichiers

| fichier | octets | sha256 |
|---|---|---|
| `LISEZ-MOI.md` | 18073 | `745c12580b2f6ecd` |
| `appareil/controle_sortie.py` | 10458 | `3f78d1461a042459` |
| `appareil/generateur_liasse_docx.py` | 7739 | `f1ba34330bb730fe` |
| `appareil/index_mesures_2027.py` | 6159 | `3065070b9568da98` |
| `appareil/installer_droit.py` | 14358 | `0fecc20ec4ca01a1` |
| `appareil/pieces_nommees.py` | 4028 | `ae065c451f5e7ad4` |
| `appareil/portes_ouvertes.py` | 8888 | `2b9f61cd5118063c` |
| `appareil/redaction_2027.py` | 11805 | `f2a87e13f34016dd` |
| `appareil/socle_texte_2027.py` | 9139 | `12801c0acf98ead6` |
| `mini-lot/LISEZ-MOI.md` | 2665 | `fc0818f546ae454f` |
| `mini-lot/enonce.md` | 318 | `3340ba428e659688` |
| `mini-lot/sortie_attendue.md` | 12115 | `e2b0abdf93179eee` |
| `procedures/conduite.md` | 21188 | `788ec99f19cea1f1` |
| `procedures/contrat_chaine_amendement.md` | 24459 | `5ad80d3d624e762d` |
| `procedures/depot_droit.md` | 13065 | `9883639b24b59ab8` |
| `procedures/domaine_lfss_LO111-3.md` | 5061 | `17585159a4d491a6` |
| `procedures/gabarit_expose_sommaire.md` | 7785 | `21a2a6e98b9e91ca` |
| `procedures/gabarit_liste_articles.md` | 9155 | `9af348ba4f0e3a1a` |
| `procedures/gage.md` | 17055 | `82801a558025a768` |
| `procedures/passation_droit_renvois.md` | 2988 | `a4c5070f89e64b1f` |
| `procedures/procedure_vecteurs.md` | 12162 | `e6b4352460d5c291` |
| `procedures/regles_forme_canonique.md` | 11848 | `fb1f1b93dc565ad8` |
| `procedures/regles_redactionnelles.md` | 13811 | `e484077013c9bc13` |
| `procedures/structure_ppl.md` | 12771 | `514483c5b2013301` |
| `procedures/test_rattachement.md` | 12778 | `3958ff4420857f4a` |
| `referentiels/articles_ouverts_plf2027.tsv` | 25306 | `5abd05f589dbae63` |
| `referentiels/articles_ouverts_plfss2027.tsv` | 8928 | `5d771439ae814b52` |
| `referentiels/releves_transversaux_plf2027.tsv` | 54192 | `a5a4c50322cea546` |
| `referentiels/releves_transversaux_plfss2027.tsv` | 22884 | `73c8176a4a4615c0` |
