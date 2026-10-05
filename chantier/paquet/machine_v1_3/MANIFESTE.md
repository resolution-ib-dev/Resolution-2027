# Manifeste — machine amendement 2027, version 1.3 (fusion des deux montages v1.2)

**Porteur** : fil Cowork de reprise de la machine, 20261005. **Mandat** : l'auteure, 20261005 —
fusion des deux montages v1.2, passe 1, paquet A-2 ter. **Domicile** : zip remis à l'auteure ;
au projet, ce manifeste seul. **Mesure d'entrée** : zip v1.2 `201fa3a4…` concordant ; 29 / 29
fichiers concordants avec les empreintes du manifeste a3.

**Non transmissible** : passe 2 jouée (v1.2), passe 1 bloquée, passe 3 non jouée.

**Zip** : `machine_amendement_2027_v1.3.zip`, 29 fichiers, 128 493 octets,
sha256 `b237c7d0d59e1fed7f356913928837036d66e45ab39d1cba8b77679211537767`.

## Ce qui change par rapport à la v1.2

- `procedures/conduite.md` et `procedures/depot_droit.md` : ceux du montage parallèle
  (`paquet/machine_v1_2/procedures/`), plus récents. Tout le reste : pièces du montage a3, à l'octet.
- Les deux montages v1.2 sont fusionnés : il n'en existe plus qu'un.

## Contrôles joués le 20261005

| contrôle | résultat |
|---|---|
| épreuve du contrôle de sortie | verte, 18 fautes, 14 justes |
| contrôle de sortie, 28 pièces, motifs livrés | 0 fuite |
| idem, motifs locaux de l'atelier | 0 fuite |
| compilation des huit modules | conforme |

Le contrôle de sortie se relève lui-même (24 occurrences : ses propres motifs et son jeu
d'épreuve) ; il est hors du compte, comme en v1.2.

**Motifs locaux** : `motifs_locaux_atelier.txt` (non livré) est **reconstitué** le 20261005, l'original
du 20261003 ayant été perdu à la purge du projet. Le nom de produit « Cowork » n'y figure pas : c'est
un nom public, qu'un destinataire utilise.

## Passe 1 — bloquée

Les deux PDF attendus (PLF `b0b802d3…`, 407 pages ; PLFSS `71010873…`, 121 pages) sont hors
d'atteinte : l'atelier ne joint ni l'Assemblée nationale, ni budget.gouv.fr, ni securite-sociale.fr
(connexion refusée par le mandataire réseau). **Le dépôt porte un autre tirage** — les textes
enregistrés n° 3210 et n° 3211 (`132274b8…`, 349 pages ; `47f5fc0d…`, 138 pages), sur lesquels
sont assis les socles du dépôt. Rejouer la passe 1 sur ce tirage est possible ici ; les référentiels
régénérés porteraient alors cette empreinte en tête, et le paquet changerait de pièce de référence :
c'est une décision, non une correction.

## Dépôt — A-2 ter

Paquet `paquet_depot_A2ter_20261005.zip` remis : `portes_ouvertes.py` de la machine
(`f53a5a59…`) à porter sur `main` en remplacement de `da8f123d…`. À remettre à une session de code.

## Les deux pièces qui changent

| fichier | octets | sha256 |
|---|---|---|
| `procedures/conduite.md` | 21188 | `788ec99f19cea1f1` |
| `procedures/depot_droit.md` | 13065 | `9883639b24b59ab8` |

Les 27 autres : empreintes du manifeste v1.2 (`paquet/machine_v1_2_a3/MANIFESTE.md`).
