# Paquet de versement au dépôt — Résolution 2027, 20261008

**Ce que c'est.** L'intégralité du coffre du projet Résolution, **267 documents, 5 481 948 octets**,
récupérés **octet pour octet** et rangés sous `chantier/` à leur adresse définitive dans le dépôt.
C'est la matière de l'intégration **C-2** (versement du paquet au dépôt) et de **C-3** (empreintes),
et elle porte aussi les trois scripts de **l'intégration des contrôles d'adresses et de la scission
des liasses**.

**Pourquoi un paquet, et pas un accès.** Aucun fil ne tient à la fois le coffre et le dépôt. Un fil
Cowork a le coffre et le dépôt de droit, il n'écrit pas au dépôt du chantier ; un fil code a le
dépôt et n'a aucun accès au projet. **Le paquet est le pont, et il ne se refait pas** : une fois
C-2 joué, le dépôt porte le corpus et la question ne se repose plus.

**Comment il a été fait, et pourquoi il ne peut pas être déformé.** Chaque document a été lu au
coffre, puis **extrait du transcript de session et écrit sur disque sans jamais repasser par le
modèle** — c'est la voie `restaurer.py` de la procédure de chantier, et c'est la seule qui garantit
la copie d'octets. **Aucun document n'a été recopié, résumé, reformaté ou régénéré.** Le contrôle
est mécanique : `empreintes_paquet_20261008.json` porte le SHA-256, la taille et le compte de lignes
des 267 documents.

---

## 1. Le contenu

| répertoire | compte | ce que c'est |
|---|---:|---|
| `chantier/livrables/` | **130** | le paquet déposable — 63 pièces sous `depot_2027/`, les 7 assemblages, les registres, et les lots antérieurs dont les périmés marqués `.PERIME.md` |
| `chantier/methode/` | **114** | procédures, passations, registres d'arbitrages, les 14 états `NUIT_*`, l'état de reprise du 20261008, `index.json` |
| `chantier/paquet/` | **15** | la machine à amendements, millésimes 1.2 à 1.4 |
| `chantier/appareil/` | **4** | **les trois scripts à intégrer** et `versement.py` |
| `chantier/reference/` | **2** | guide de légistique digéré, règles de crédits |
| `chantier/input/`, `chantier/CLAUDE.md` | 2 | entrée de l'auteure, consignes de dépôt |

**Les trois scripts à intégrer** sont déjà à leur place sous `chantier/appareil/`, et ils sont
**identiques à l'octet** à ceux de la pièce jointe du 20261008 — vérifié par empreinte :

| script | SHA-256 (16) | ce qu'il fait |
|---|---|---|
| `controle_adresses_extraction.py` | `14880f83cbefc220` | extrait les adresses d'un dispositif, nomme une à une les références laissées hors contrôle |
| `controle_adresses_verdicts.py` | `13ef63253f494e29` | passe chaque adresse au droit à trois dates — jour, 1er juillet 2027, 1er janvier 2028 |
| `scinder_liasse_trois_colonnes.py` | `03d40798c8d710ba` | scinde la liasse unique en trois par véhicule, lettre les rangs, régénère les tables |

**`temoins/`** porte deux fichiers **à ne pas intégrer** : `imprimer_extraction_p1.py`, périmé par le
script de scission, et `md2docx.js`, qui appartient à la skill `impression-docx` et ne vit pas au
dépôt.

---

## 2. Ce que le fil code en fait, dans cet ordre

1. **Verser.** Copier `chantier/` à la racine du dépôt. Les adresses sont déjà les bonnes :
   `chantier/livrables/depot_2027/P1/…` est l'adresse que les pièces déclarent elles-mêmes à leur
   ligne `Domicile`.
2. **Contrôler le versement, mécaniquement.** Rejouer les empreintes du paquet et les confronter à
   `empreintes_paquet_20261008.json`. **Un seul écart arrête le versement** : un document qui diverge
   est un faux, il ne se corrige pas au dépôt, il se redemande au coffre.
3. **Relever les empreintes du dépôt** — `make coffre` — et jouer `make restauration`. **S'arrêter
   sur un R1.**
4. **Régénérer `methode/index.json`** : une centaine de documents nés depuis le 20261007 n'y sont pas
   déclarés, et les renvois qui les visent ne résolvent pas. C'est l'intégration **C-4**.
5. **Jouer C-1** — `extraire_legi.py`, fonction `lire_structure` : `descendre(racine, [])` construit
   le chemin à l'intérieur d'un seul fichier XML, et un fichier de section LEGI ne porte jamais ses
   ascendants. **0 article sur 11 614 porte une chaîne hiérarchique.** Rejouer l'extraction ne change
   rien, le défaut est de conception. **C'est la seule intégration qui change le texte déposable** :
   elle commande le regroupement des abrogations par bloc, et les 396 rangs du III de P1-31 occupent
   douze pages à eux seuls.

**Ce que le fil code ne fait pas** : il ne corrige aucune pièce, ne tranche aucune question, ne
réécrit aucun exposé. **Il verse, il contrôle, il outille.**

---

## 3. Deux états à connaître avant de verser

**Le paquet et ses assemblages divergent d'une ligne.** La note de forme qui fuyait au texte
déposable de SS-01 est retirée de la pièce `livrables/depot_2027/SS/n7b_ss03_liste_niches_sociales.md`
le 20261008, mais elle figure encore aux deux assemblages qui reprennent ce rang —
`LIASSE_20261008.md` et `LIASSE_PLFSS_20261008.md`. **Les assemblages ne se corrigent pas à la
main** : leur régénération est un geste de `scinder_liasse_trois_colonnes.py`, et elle appelle son
propre mandat.

**Les 213 virgules de coordination.** Mesure du 20261008 sur les trois liasses : 12 devant « ni »,
195 devant « et », 5 devant « ou », 1 devant « donc ». La règle du corpus n'est pas en cause ; c'est
la passe de typographie qui n'a traité que « ni ». **Une passe de lecture est due** — la clôture
d'incise est l'exception inscrite, et chaque occurrence se lit avant d'être corrigée.

Les deux sont inscrits à `chantier/methode/appui_des_passes.md`, reprises 9 et 10 du 20261008, et à
`chantier/methode/etats/REPRISE_bilan_20261008.md`.

---

## 4. Ligne de lancement du fil code

> Versement du paquet Résolution au dépôt et intégration de l'appareil — déplier
> `paquet_depot_2027_20261008.zip`, copier `chantier/` à la racine du dépôt, puis contrôler le
> versement sur `empreintes_paquet_20261008.json`, **un écart arrête** ; lire
> `chantier/MANIFESTE.md`, `chantier/methode/etats/REPRISE_bilan_20261008.md`,
> `chantier/methode/passation_20261008.md` § 5 et `chantier/methode/appui_des_passes.md` ; jouer
> ensuite `make coffre` et `make restauration`, régénérer `methode/index.json` (C-4), puis corriger
> `lire_structure` d'`extraire_legi.py` (C-1), qui commande le regroupement des abrogations par
> bloc ; ne corriger aucune pièce, ne trancher aucune question, ne régénérer aucun assemblage sans
> mandat qui le nomme ; la mesure de sortie reprend ce mandat point par point, « non joué » compris.
