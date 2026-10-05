# Les textes 2027 ont un numéro et une adresse — 20261004

## Ce qui était faux dans tout le corpus

Les 41 pièces rédigées portent, à leur bandeau, « déposé le 1er octobre 2026 **(numéro non
attribué)** ». **C'est périmé.** Les deux textes sont enregistrés à l'Assemblée nationale,
17e législature :

| texte | numéro | adresse de la pièce | forme structurée |
|---|---|---|---|
| projet de loi de finances pour 2027 | **n° 3210** | `assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf` | `assemblee-nationale.fr/dyn/opendata/PRJLANR5L17B3210.html` |
| projet de loi de financement de la sécurité sociale pour 2027 | **n° 3211** | page : `assemblee-nationale.fr/dyn/17/textes/l17b3211_projet-loi` | — |

Dossiers législatifs : `dyn/17/dossiers/PLF_2027` et `dyn/17/dossiers/PLFSS_2027`.

**Réserve, et elle se lève d'une ouverture** : les adresses du 3210 sont relevées
directement ; celles du 3211 se déduisent de la symétrie du 3210 et **se vérifient avant
emploi**. Le numéro 3211, lui, est relevé.

**Reprise due, mécanique** : le bandeau des 41 pièces porte le numéro du texte, PLF ou
loi de financement selon la colonne. Elle se fait en une passe, sans toucher aux
dispositifs.

## La forme structurée vaut mieux que le PDF

L'Assemblée publie le texte déposé en HTML structuré, à la même forme que le millésime
2026 que la procédure nomme déjà. **C'est la source à essayer en premier** : elle est
légère, elle porte la structure, et elle évite l'extraction de mise en page. Le PDF reste
le repli.

**Ce qui ne change pas** : la récupération web passe par un modèle et **ne rend jamais du
verbatim**. Elle sert au repérage, à la structure et aux adresses. **Le socle ne se fait
pas depuis une page web lue par un modèle** : il se fait par un outil déterministe, dans
une session qui télécharge l'octet — ce qu'une session de code sait faire et qu'un fil
Cowork ne sait pas.

## Le défaut qui a bloqué la session de code, et sa règle

La session de code a refusé de démarrer : son mandat lui demandait de lire
`methode/audit_pieces_sans_domicile_20261004.md`, **qui est un document du coffre, et une
session de code ne voit pas le coffre.**

**Règle : un mandat de session de code ne renvoie jamais à un chemin du coffre.** Il porte
son contenu verbatim, ou il renvoie à un chemin du dépôt. C'est la faute déjà nommée le
1er octobre — un prompt de code qui pointait vers des pièces du coffre — et elle vient
d'être refaite. Elle est inscrite ici une seconde fois.

## Les annexes 2027 sont parues

Elles sont publiées à `budget.gouv.fr/documentation/documents-budgetaires/exercice-2027/PLF2027`.

**Ce que cela débloque, et ce n'est pas mince** : le registre des sources de gage porte
aujourd'hui des montants pris sur l'annexe des voies et moyens **du PLF 2026**, déclarés
majorants provisoires, en écart d'un exercice avec le véhicule. **L'annexe 2027 les remplace
et lève la réserve.** Même chose pour les 305 lignes de dépenses fiscales du relevé des
sièges, et pour le tableau des taxes affectées.

**Lot dû** : reprise des montants du registre de gage et du relevé des sièges sur les
annexes 2027, une fois celles-ci chargées.

## Reprise faite — 20261004

**Mesure d'entrée** : 20 occurrences de « numéro non attribué », une par document, sur 44 documents
de livrables relevés. Les exposés détachés et les pièces des arrêts immédiats n'en portaient aucune.

**Forme inscrite**, tranchée par le fil : le bandeau porte le numéro suivi de la mention de l'assemblée
et de la législature, entre parenthèses, et la date de dépôt passe après.

- `projet de loi de finances pour 2027, n° 3210 (Assemblée nationale, 17e législature), déposé le 1er octobre 2026`
- `projet de loi de financement de la sécurité sociale pour 2027, n° 3211 (Assemblée nationale, 17e législature)`

Le 3211 n'apparaît qu'à la clause générale du 20261004, seul document du relevé qui nomme les deux textes.

**Contrôle de sortie** : relecture des 20 documents au coffre, zéro occurrence résiduelle, et égalité à
l'octet entre ce qui a été versé et ce que le coffre rend. Aucun dispositif touché — l'écart de taille
est le seul écart du bandeau sur les 20 documents.

**Hors mandat, signalé** : `paquet/machine_v1_0/mini-lot/sortie_attendue.md` porte « numéro non attribué »
comme sortie attendue d'un mini-lot de test. Ce n'est pas une pièce déposable ; elle n'a pas été touchée.
