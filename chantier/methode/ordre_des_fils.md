# Ordre des fils

*Tenu par le fil chef de file depuis le 20261002 — décision de l'auteure,
`methode/fragments/arbitrages/20261002-organisation-et-deploiement.md`. Il
remplace la table du § 10 de la passation. **L'ordre vient des dépendances,
jamais d'un calendrier.***

**Ce document est un plan de travail, pas un engagement de date.** Il se réécrit
à chaque fil clos.

---

## Deux chantiers parallèles, et ils ne se gênent pas

**A — l'export de la machine 2027.** Une version transmissible à des tiers,
numérotée, avec la date de ses trois passes.

**B — la production du plan.** La liasse, phase par phase, dans l'ordre des
dépendances.

A ne consomme que de l'appareil, B que de la doctrine et du droit.

---

## Chantier A — export de la machine 2027

**Gouverné par `methode/controle_avant_transmission.md` : trois passes, aucune
version ne part sans les trois.** Corrigé le 20261003 pour cinq modules et six
référentiels.

**Forme arrêtée le 20261002** —
`methode/fragments/arbitrages/20261002-forme-du-paquet.md` : un zip, un
`LISEZ-MOI.md` à la racine comme point d'entrée unique, deux commandes.
**Machine seule, valise retirée** : toute étape tourne à blanc et le déclare.

| jalon | fil | ce qu'il fait | état |
|---|---|---|---|
| A-0 | fil code — courroies | — | **ÉPUISÉ**. Le paquet était déjà appliqué au commit `f8834f3` du 20261001. Dette au dépôt nulle, et la poussée fonctionne : pas de `403` |
| A-1 | **fil Cowork — paquet `redaction_2027.py`** | porte verbatim le module absent du dépôt, avec sa poussée d'essai et ses points d'arrêt | **CLOS le 20261002**. Paquet versé à `methode/paquet_depot_redaction_2027_20261002.md`, et remis en **pièce jointe** au fil code le 20261003 après un premier passage à vide |
| A-2 | **session de code** | applique A-1 et pousse | **JOUÉ le 20261003, NON ABOUTI.** Aucun `403`, contrôle d'import passé, commit `3030acf` — mais poussé sur `claude/loving-mayer-4siugc`, pas sur `main`. Doute de transmission déclaré sur la ligne `CHIFFRE` |
| A-2 bis | **session de code** | fusionne sur `main` et reprend la ligne `CHIFFRE` en échappements | **CLOS le 20261003.** Fusion en avance rapide `bab7f73..3030acf`, puis commit `4bc56de` sur `main` portant la seule ligne `CHIFFRE`. `sha256` du module : `6a92f11131c7d3d25d54349848f6a92f8faa177a53a89bbef43358af93ae8de4`. **Le blocage de la passe 1 est levé : les cinq modules du millésime sont sur `main`** |
| A-3 | **fil Cowork — paquet machine 2027** | monte le zip au contenu arrêté, écrit le `LISEZ-MOI.md` et le mini-lot, corrige le document de contrôle, joue les **passes 1 et 2** | **JOUÉ le 20261003, PASSE 2 SEULE.** Zip v1.2 monté (29 fichiers, `201fa3a4…`), remis à l'auteure ; manifeste et pièces modifiées à `paquet/machine_v1_2_a3/`. Document de contrôle corrigé (cinq et six). **Passe 1 non jouée** : PDF 2027 hors d'atteinte — ne pas les redemander à l'auteure. **Collision** : un fil parallèle montait `paquet/machine_v1_2/` ; trois de ses documents ont été écrasés (`LISEZ-MOI.md`, `MANIFESTE.md`, `appareil/installer_droit.py`) et sont à reverser par lui ; les deux montages se fusionnent avant la passe 1 |
| A-2 ter | **session de code** | porte au dépôt `portes_ouvertes.py` de `paquet/machine_v1_2_a3/appareil/`, en pièce jointe ; réaligne le coffre sur `redaction_2027.py` de `main` | **PAQUET PRÊT le 20261005** : `paquet_depot_A2ter_20261005.zip` remis à l'auteure, à joindre à une session de code ; le réalignement côté coffre reste à faire |
| A-4 | **fil vierge — épreuve à froid** | reçoit le zip et **le seul `LISEZ-MOI.md`**, joue le mini-lot, bute et déclare. **Il ne corrige rien** | après A-3 |
| A-5 | **transmission** | numéro de version et date des trois passes écrits au `LISEZ-MOI.md` | après A-4 |

**Deux dettes ouvertes, et elles sont pour A-3.**

1. **`redaction_2027.py` du coffre est périmé.** La copie versée à
   `appareil/redaction_2027.py` porte encore la classe `CHIFFRE` en littéral,
   aplatie. **Le dépôt fait foi pour ce module** — `main`, `4bc56de`,
   `sha256 6a92f11…` —, et le coffre se réaligne dessus au premier fil de code
   qui y passe.
2. **`portes_ouvertes.py` n'est toujours pas confronté.** Le dépôt rend
   `sha256 da8f123d3f125eb7f0e7144aa55d09e710cfcb38972f19ff754ebee6677b58fe`,
   6 653 octets. **Mesuré le 20261003 côté coffre : divergent.** La copie
   `appareil/portes_ouvertes.py` du coffre, versée le 20261002 et portant les deux
   corrections datées de ce jour, rend 8 122 octets,
   `sha256 90440ef3510e08eaf6c90191c8fb74faf794938b8986b0b3359524ca6dc31dfb`.
   Le dépôt ne porte donc pas l'état corrigé ; selon toute vraisemblance il porte
   l'antérieur — non établi, faute de l'avoir lu. Conséquence : la passe 1
   rejouée sur `main` rendrait l'ancien relevé, 449 adresses, contre 421 au
   paquet. **À aligner avant la passe 1**, par paquet de voie `depot` remis en
   pièce jointe.

**Mesure du 20261003, fil A-3, côté coffre.** Modules : les cinq sont au
coffre ; `redaction_2027.py` est périmé (classe `CHIFFRE` aplatie),
`portes_ouvertes.py` diverge du dépôt (ci-dessus). Référentiels : quatre sur six —
`articles_ouverts_plf2027.tsv`, `articles_ouverts_plfss2027.tsv`,
`releves_transversaux_plf2027.tsv`, `releves_transversaux_plfss2027.tsv`.
**`redaction_plf.json` et `redaction_plfss.json` ne sont pas au coffre** : trop
volumineux, régénérables par `redaction_2027.py` depuis les PDF. Le paquet ne
peut donc les porter qu'en les régénérant dans une session qui a les deux PDF —
et ni le coffre ni l'atelier Cowork ne les ont. A-3 s'est arrêté là, sans rien
monter, sans corriger le document de contrôle.

**Mesure du 20261002** : `chantier/appareil/` portait 97 fichiers ; quatre des
cinq modules du millésime y étaient, `redaction_2027.py` était absent.

**Correction du 20261003 : un fil Cowork LIT le dépôt.** Le clone public en
lecture passe (`git clone`), seule l'API et la poussée restent fermées. Mesure
faite au fil A-3 sur `main` `4bc56de` : les cinq modules y sont ;
`portes_ouvertes.py` y est **l'état antérieur aux corrections du 20261002**
(diff contre le coffre : la règle d'insertion et la pièce accolée manquent) ;
`articles_ouverts_plf2027.tsv` et `..._plfss2027.tsv` y portent **449 et 191
adresses**, l'ancien relevé, contre 421 et 153 au coffre ;
`redaction_plf.json` et `redaction_plfss.json` y sont **ceux du millésime 2026**
(pièces `PLF2026_1906.pdf` et `PLFSS2026_1907.pdf`). **Aucun PDF 2027 n'est au
dépôt, sur aucune branche ni dans l'historique.** Les deux sites qui les
publient sont refusés par la politique réseau de l'organisation, depuis Cowork
comme à l'outil de récupération.

**Un fil Cowork ne peut ni pousser ni interroger l'API du dépôt**. Toute mesure du dépôt passe par une session de
code ; le partage « Cowork mesure et écrit le paquet » ne vaut que pour le
coffre.

**Règle tirée de l'échec du 20261003, et elle vaut pour tout paquet de voie
`depot`** : une session de code **ne voit pas le coffre**. Un paquet ne se
transmet donc **jamais par son chemin de coffre** — il se remet **en pièce
jointe**, et la ligne de lancement dit en toutes lettres de ne pas le chercher
au dépôt. Un chemin de coffre dans une ligne de lancement destinée au code est
une ligne fausse.

**Deuxième règle du 20261003 — la branche se nomme.** Une session de code
travaille par défaut sur une branche de travail, et une poussée nue n'atteint
pas `main`. La passe 1 clonant `main`, **tout paquet de voie `depot` nomme sa
branche d'arrivée à l'étape de poussée**, et la session rend le nom de la
branche effectivement poussée parmi ses lignes de sortie.

**Troisième règle du 20261003 — aucun caractère invisible dans un paquet, ni
dans une pièce de méthode.** Un paquet traverse plusieurs copies avant
d'arriver au dépôt, et chaque passage peut normaliser une espace insécable en
espace ordinaire sans que rien ne le signale. **Tout caractère non ASCII
porteur de sens s'écrit en échappement** — la suite de six caractères
`backslash u 0 0 a 0` pour l'insécable, `backslash u 2 0 2 f` pour l'insécable
fine — **jamais en littéral**. La classe `CHIFFRE` de `redaction_2027.py` est
le cas qui a révélé la règle : trois espaces y étaient écrites en littéral, et
trois espaces ASCII identiques n'ont aucun sens dans une classe de caractères.
Corrigé au dépôt le 20261003.

**Règle qui ne se négocie pas** : une correction d'un caractère est une version
neuve et repasse les trois passes.

---

## Chantier B — production du plan

### Le lot qui s'ouvre maintenant — trois fils indépendants, parallélisables

| fil | ce qu'il fait | pourquoi en tête |
|---|---|---|
| **B-1 — assemblage et tenue** | clone le dépôt, joue `appareil/fragments.py` sur copie jetable, compte les sections avant et après, refuse si une section se perd, reverse `journal.md` et `arbitrages.md` ; remesure la table curée | le registre est amputé de tous les fragments déposés depuis le 20260917 : **tout fil qui lit le registre seul lit faux** |
| **B-2 — réservoir d'arguments du livre** | arguments de fond indexés par mesure et par bloc, chacun avec la citation opposable qui le soutient quand elle existe ; quatre bornes d'emploi, contrôle négatif | tout exposé écrit avant lui sera à réécrire |
| **B-3 — règle d'entrée en vigueur** | le test qui classe une niche entre rétroactivité admise et avantage protégé, verbatim de jurisprudence relevé au dépôt de droit | **aucun exposé n'énonce le principe de non-rétroactivité avant lui** |

### Le lot suivant

| fil | dépend de |
|---|---|
| **B-4 — clause type de restitution** — rédaction unique, test au regard de l'article 40 et de l'universalité | rien ; commande B-6, B-7 et B-8 |
| **B-5 — croisement taxes supprimées / taux réduits** — les 193 prélèvements supprimés contre les assiettes à taux réduit | rien ; dû avant la jambe TVA |

### Les fils de rédaction

| fil | dépend de |
|---|---|
| **B-6 — clause générale sur les niches** — 465 niches par la clause ; la jambe TVA en sort, datée au 1er juillet 2027 et corrélée ; impôts locaux compris ; J1 et J3 fondus dedans | B-2, B-3, B-4 ; la jambe TVA attend en outre B-5 et le calendrier de B-10 |
| **B-7 — allègements aux entreprises** — nouvelle forme, outre-mer retiré, agriculture sur trois ans ; articles 10 et 4 B renvoyés aux droits de mutation | B-2, B-3, B-4 |
| **B-8 — compléments de salaire** — volet CSG, cohérence avec la jambe PLFSS | B-2, B-4 |
| **B-9 — affectations refondues** — toutes, par sous-cas, avec la porte de sortie juridique | B-2 |
| **B-10 — nettoyage du texte déposé** — relever les niches créées ou prorogées par le PLF, trancher pour chacune | B-2 ; relevé Cowork, arbitrage en une ligne à l'auteure |
| **B-11 — suppression de taxes** — recollage du solde de gage, coordination des entrées en vigueur | B-9 ; **B-6 a besoin de savoir lesquelles tombent au 1er juillet 2027** |

### La cohérence, et elle n'est plus terminale

**Une passe de remise en cohérence après chaque paire de fils de rédaction.**
Elle tient la carte des collisions **au niveau du programme**, pas du bloc.

Collision déjà connue, à porter dès la première passe : la jambe TVA de M-026 et
M-029 visent `278` et `278-0 bis`, dans deux phases différentes.

---

## Les boucles

**Révision** — le fil se relit sur ses propres contrôles avant de rendre.
Mécanique, ne remonte à personne.

**Relecture** — l'auteure lit **la pièce déposée seule** : titre, dispositif,
exposé, et cinq lignes au plus de ce qui reste à trancher. Jamais le dossier. À
sa main et **jamais bloquante par défaut**.

**Remise en cohérence** — une passe transverse après chaque paire de fils de
rédaction, puis une avant dépôt de la liasse.

---

## Ce qui remonte à l'auteure, et ce qui ne remonte pas

**Remonte** : un arbitrage de fond, posé en une ligne, avec la conséquence de
chaque branche. Une pièce déposée à relire. Un coût avant de l'engager.

**Ne remonte pas** : l'ordre des fils, le découpage, le nommage, l'appareil, la
méthode de détail, le choix du moment. Le chef de file tranche et inscrit ;
l'auteure révoque si elle veut.

---

## Les quatre bornes de fond toujours ouvertes

Elles ne bloquent aucun fil de ce plan, et elles bloquent le dépôt des mesures
qui les portent : le périmètre des ~300 établissements exclus ; le coût de
l'indemnité des agents ; lesquels des minima sociaux demeurent ; le socle de
l'hébergement d'urgence, critère ou quantum.

Hors phase de concentration : qui supporte la perte des impôts locaux supprimés.

**Reprise du 20261005 (fil Cowork, machine).** Les deux montages v1.2 sont fusionnés en **v1.3**
(`paquet/machine_v1_3/MANIFESTE.md`) : contrôle de sortie à zéro fuite, avec et sans motifs locaux.
**Passe 1 bloquée** : les PDF `b0b802d3…` et `71010873…` sont hors d'atteinte ; le dépôt porte le
tirage enregistré (`132274b8…`, `47f5fc0d…`). A-4 et A-5 attendent la passe 1.

**Recalage du 20261005 (arbitrage de l'auteure).** La machine passe en **v1.4**, sur les textes
enregistrés n° 3210 et n° 3211 (`paquet/machine_v1_4/MANIFESTE.md`). **Passe 1 jouée** : socles et
rédaction identiques à l'octet au dépôt, relevés reproductibles. Le paquet A-2 ter est étendu à
`index_mesures_2027.py` et aux quatre relevés. Reste : passe 2 sur le nouveau tirage, A-2 ter poussé,
puis A-4 et A-5.

