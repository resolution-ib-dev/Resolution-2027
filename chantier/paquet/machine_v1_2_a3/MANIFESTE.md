# Manifeste — machine amendement 2027, version 1.2

Montée le 3 octobre 2026 par le fil A-3. **Non transmissible** : passe 2 jouée,
passes 1 et 3 non jouées.

**Zip** : `machine_amendement_2027_v1.2.zip`, 29 fichiers, 127 396 octets,
sha256 `201fa3a41b6957c39d803da78b3ebf19e455d70c1509d07ebe62da120b4403d0`.
Remis à l'auteure en téléchargement le 20261003. Les pièces modifiées par cette
version sont versées sous `paquet/machine_v1_2_a3/` ; les pièces inchangées restent
à leur adresse (`paquet/machine_v1_1/procedures/`, `paquet/machine_v1_0/`) et au
dépôt pour les modules.

## Collision avec un fil parallèle — à lire d'abord

Ce fil a d'abord versé sous `paquet/machine_v1_2/`, où **un autre fil montait
une v1.2 en même temps** (sa `procedures/conduite.md` est datée de 17 h 41, et
plus récente que celle de la v1.1). Trois de ses documents ont été écrasés :
`LISEZ-MOI.md`, `MANIFESTE.md`, `appareil/installer_droit.py`. Ce fil ne peut
pas les restaurer ; le fil qui les a écrits doit les reverser. Les pièces de ce
fil-ci ont été déplacées ici et retirées de `paquet/machine_v1_2/`. Le zip de ce
fil porte `conduite.md` et `depot_droit.md` de la v1.1 : **les deux montages se
fusionnent avant toute passe 1**.

## Ce qui change par rapport à la v1.1

1. **Les cinq modules du millésime sont joints.** `socle_texte_2027.py`,
   `pieces_nommees.py`, `index_mesures_2027.py` pris au dépôt (`main`, identiques
   au coffre) ; `redaction_2027.py` pris au dépôt (`4bc56de`, `6a92f11…`, classe
   `CHIFFRE` en échappements) ; `portes_ouvertes.py` pris au **coffre** — l'état
   corrigé du 20261002, que le dépôt n'a pas —, commentaires et en-tête nettoyés.
2. **Les deux relevés d'articles ouverts** : corps identique au coffre (421 et
   153), en-tête réécrit exactement comme le module nettoyé l'écrit.
3. **Les huit procédures exportées perdues sont reconstituées.** Le retrait des
   doublons du 20261002 avait supprimé leurs copies d'export en affirmant que les
   originaux les portaient : **mesuré faux, 142 fuites sur les originaux**.
   Ré-exportées depuis les originaux, fuites retirées sans toucher au fond ;
   `passation_droit_renvois.md` réduite à ses §1-2 (règle et dépôt), les §3-5
   étant de la mécanique d'atelier.
4. **Le contrôle de sortie ne porte plus aucun nom propre.** Motifs
   d'organisation et noms internes sortis dans un fichier local, non livré
   (`motifs_locaux.txt`, tenu à l'atelier et rejoué avant départ). Quatre
   angles morts fermés : `corpus`, `coffre`, `valise` sans article, chemins
   `sources/` et `paquet/`, sigle suivi d'un astérisque.
5. **`installer_droit.py` éprouvé contre le dépôt réel — et il échouait.** Il ne
   lisait ni `data/_manifeste.json` ni le millésime compact `AAAAMMJJ`. Corrigé ;
   verdict `FRAIS`, millésime 2026-10-01.
6. `droit.py`, `extraire_legi.py`, `codes.json` **ne sont pas dupliqués** dans le
   zip : ils arrivent par le clone. Une copie, pas deux.
7. Contenu : union de la forme arrêtée le 20261002 et de la v1.1 — les procédures
   restent, l'objectif de l'auteure étant qu'un tiers produise ses amendements
   avec elles.

## Contrôles joués

| contrôle | résultat |
|---|---|
| contrôle de sortie, 28 pièces, motifs livrés | 0 fuite |
| idem, motifs internes de l'atelier ajoutés | 0 fuite |
| épreuve du contrôle | verte, 18 fautes, 14 justes |
| import des modules, rendu `.docx` du mini-lot | conforme, 1 amendement, 37 160 o |
| installation du droit, dépôt réel | `FRAIS` |
| passe 2, articles ouverts PLF contre relevé manuel 424 | 352 communs, 69 / 72 d'écart, causes au LISEZ-MOI |
| passe 2, cohérence portes / relevés transversaux | 0 article orphelin, deux véhicules |

## Ce qui reste

- **Passe 1** : reproduire les six référentiels à l'octet depuis les deux PDF
  (empreintes au LISEZ-MOI §9). Les PDF ne sont ni au coffre ni au dépôt, et
  l'atelier ne joint ni l'Assemblée ni budget.gouv.fr. **Ne pas les redemander à
  l'auteure** (consigne du 20261001) : la voie est l'ouverture réseau de ces deux
  domaines, ou une session qui les atteint.
- **Le dépôt** : `portes_ouvertes.py` y est l'état antérieur ; un paquet de voie
  `depot` doit y porter le module de ce zip. Le coffre `appareil/redaction_2027.py`
  est périmé, le dépôt fait foi.
- **Passe 3**, l'épreuve à froid, après la passe 1.
- **Le dépôt public expose le corpus** : le clone que fait l'installation porte
  `chantier/` — méthode, livrables, livre. À trancher par l'auteure.

## Les 29 fichiers

| fichier | octets | sha256 |
|---|---|---|
| `LISEZ-MOI.md` | 17468 | `a7d007199f4a165f` |
| `appareil/controle_sortie.py` | 10448 | `745300312abe79ce` |
| `appareil/generateur_liasse_docx.py` | 7739 | `f1ba34330bb730fe` |
| `appareil/index_mesures_2027.py` | 5738 | `9074318f0ec534c5` |
| `appareil/installer_droit.py` | 14358 | `0fecc20ec4ca01a1` |
| `appareil/pieces_nommees.py` | 4028 | `ae065c451f5e7ad4` |
| `appareil/portes_ouvertes.py` | 8018 | `f53a5a5921c5c766` |
| `appareil/redaction_2027.py` | 11059 | `6a92f11131c7d3d2` |
| `appareil/socle_texte_2027.py` | 5391 | `ef6c3aa124591784` |
| `mini-lot/LISEZ-MOI.md` | 2665 | `fc0818f546ae454f` |
| `mini-lot/enonce.md` | 318 | `3340ba428e659688` |
| `mini-lot/sortie_attendue.md` | 12115 | `e2b0abdf93179eee` |
| `procedures/conduite.md` | 20732 | `1bca02beb3ba8ec3` |
| `procedures/contrat_chaine_amendement.md` | 24459 | `5ad80d3d624e762d` |
| `procedures/depot_droit.md` | 10584 | `b1c8592f25f3d138` |
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
| `referentiels/articles_ouverts_plf2027.tsv` | 24204 | `52d4b88498e17765` |
| `referentiels/articles_ouverts_plfss2027.tsv` | 8785 | `3c97cec7dded2196` |
| `referentiels/releves_transversaux_plf2027.tsv` | 52997 | `53136f15238d6767` |
| `referentiels/releves_transversaux_plfss2027.tsv` | 34774 | `61e1aa960516f013` |

---

*Note de restauration, 20261005.* Ce document a été reversé par le fil du montage
B, depuis sa lecture du 20261004, après que les treize pièces de
`paquet/machine_v1_2_a3/` ont disparu du projet. **C'est la seule des treize que
ce fil détenait** — les douze autres n'y sont jamais passées et ne sont pas
reconstituables ici. Le texte ci-dessus est celui lu le 20261004, sans
modification ; cette note est le seul ajout.
