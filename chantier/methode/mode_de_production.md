# Mode de production — Résolution

**Porteur** : fil chef de file. **Mandat** : l'auteure, le 20261004, après la journée où quatre
fautes de la même famille ont coûté un chantier. **Domicile** : coffre.

**Cette pièce prime sur toute autre règle d'organisation.** Elle dit comment on produit —
n'importe quel produit. Ce qu'on produit est dans `methode/objectifs_depot_2027.md`.

**Le principe, et il explique tout le reste : on ne remplace pas une faute par une règle, on la
rend impossible ou visible.** Les règles de cette semaine étaient justes et elles ont été
enfreintes, y compris le jour de leur écriture. Ce qui suit est fait de contraintes et de
contrôles, non de bonnes intentions.

---

## 1. Les quatre invariants

**Porteur** — qui produit. **Mandat** — ce qui le nomme. **Domicile** — où l'objet vit.
**Mesure** — le compte d'entrée.

Ce sont les quatre champs d'un **en-tête obligatoire**, en tête de toute pièce. Une pièce sans
eux ne se verse pas. Les quatre défauts de la semaine sont exactement les quatre champs
manquants : un registre sans porteur, un relevé sans mandat, des socles sans domicile, un
mandat de code qui pointait du mauvais côté.

**La mesure passe avant tout.** Trois croyances ont coûté des heures le 4 octobre : le droit
réputé inaccessible, alors qu'il était dans le dépôt ; un travail de septembre réputé perdu,
alors qu'il était fusionné ; une branche réputée porter une extraction concurrente, alors
qu'elle recompressait le même contenu. **Un mandat de correction commence par un comptage et
s'arrête si le compte sort vide.** Un contrôle annoncé est un contrôle joué.

---

## 2. Deux mémoires — ici on décide, là-bas on prouve

### Là-bas — le dépôt, mémoire de preuve

Tout ce qui se contrôle, se régénère, se date ou se confronte au droit.

```
data/                        le droit — millésime LEGI, rafraîchi le 1er du mois
droit.py  extraire_legi.py  codes.json
chantier/
  appareil/                  scripts, générateurs, contrôles
  reference/                 Constitution, LOLF, DDHC, digestions externes, gabarits
  input/                     ce que l'auteure fournit et qui ne se régénère pas
  livre/                     le texte EP3 et son index
  referentiels/              socles 2027, relevés, tables, REF_doctrine
  livrables/
    depot_2027/P1 P2 SS      les pièces déposables, nommées par leur rang
    REGISTRE.md              colonnes et gages
  sources/                   les textes déposés
  methode/index.json         la table de résolution
```

**Une seule branche, `main`.** Une branche de versement naît le matin et meurt le soir ; elle
porte un nom donné par l'auteure ou par le fil de tête, jamais par la machine. Une branche qui
survit à sa session est un échec, pas un état.

**Attention : une session de code peut pousser mais ne peut pas supprimer une branche
distante** — le mandataire git le refuse. La suppression se fait à la main, dans le navigateur,
sur la page des branches du dépôt.

### Ici — le coffre, mémoire de décision

Ce qui ne se prouve pas, ne se régénère pas, et doit se lire d'un fil à l'autre.

```
methode/mode_de_production.md     comment on travaille
methode/objectifs_depot_2027.md   ce qu'on produit
methode/passation_<date>.md       l'état — une seule vivante
methode/fragments/arbitrages/     les décisions de l'auteure, une par fragment
```

**Et rien d'autre.** Pas de pièce déposable, pas de référentiel lourd, pas de dérivé. Le coffre
est borné à 2 Mo ; il doit porter une cinquantaine de documents, pas trois cents.

### Le critère, en une ligne

**Si un objet doit un jour être confronté au droit, régénéré ou prouvé, il vit au dépôt.** Une
pièce déposable cite des articles : elle est confrontable par construction, donc elle naît
là-bas.

### Le droit se lit depuis n'importe quel fil

Le dépôt est public. `data/_manifeste.json` donne le millésime et le fichier de chaque code ;
chaque `data/<code>.jsonl.gz` porte une ligne par article avec `num`, `etat`, `date_debut`,
`date_fin`, `id`, `texte`. On télécharge, on filtre sur l'état `VIGUEUR`, on lit le texte.
**Aucun fil ne devine une adresse. Légifrance refuse toute lecture automatique et n'est jamais
la source.**

---

## 3. Ce qui joint les deux mondes : l'index

`chantier/methode/index.json` déclare chaque artefact avec sa **voie** — coffre ou dépôt —, son
rôle, sa famille, ses alias, et **ce qui le consomme**. C'est le seul endroit où un fil apprend
qu'une pièce existe.

**La règle d'ouverture tient en une phrase : un fil télécharge l'index, et il sait tout ce qui
existe et où le lire.** Plus de passation qui récite la liste des pièces, plus de fil qui
redécouvre le corpus. Le champ `consomme_par` est le plus utile et le moins exploité : il dit à
quoi une pièce sert, pas seulement qu'elle existe.

**Pour que ça tienne, l'index doit être régénéré à chaque versement**, et deux contrôles le
gardent : l'index contre l'arborescence, le registre contre `depot_2027/`.

---

## 4. Le cycle d'une pièce — six gestes, toujours les mêmes

1. **Situer** — le siège juridique, lu sur l'extrait, jamais de mémoire.
2. **Rattacher** — le véhicule qui peut la porter.
3. **Rédiger la cible, en dériver la disposition modificative**, et la prouver par
   réapplication.
4. **Monter au gabarit** — dispositif cadre, liste de tous les articles modifiés ou abrogés,
   transition, renvois réglementaires, clause de restitution ou de gage.
5. **Exposer** — l'exposé sommaire, adossé au réservoir d'arguments du livre.
6. **Contrôler et verser** — adresses contre le droit, place aux registres, commit.

---

## 5. Trois couches — ce qui rend la chaîne réutilisable

**La matière** — le droit, le livre, les référentiels, la doctrine. **Elle ne bouge jamais.**

**Le gabarit** — la forme du produit. C'est ce que portent les skills : exposé sommaire, fiche
mesure, disposition cible, Q&A, impression.

**Le contrôle** — ce qui refuse de verser. Propre à chaque produit.

**Un produit nouveau, c'est un gabarit et un contrôle, et rien d'autre.** La matière et le cycle
ne se réécrivent pas. C'est la condition pour produire en flux.

---

## 6. Les contrôles mécaniques

**Adresses contre le droit** — chaque référence existe, est en vigueur au millésime, et la
subdivision visée existe. Verdicts : `EXISTE`, `ABSENT`, `ABROGE`, `SUBDIVISION_INTROUVABLE`.

**Index contre arborescence** — un fichier non déclaré, un chemin déclaré absent, et ça sort.

**Registre contre `depot_2027/`** — un rang sans fichier, un fichier sans rang. Tue les
collisions de numérotation.

**Preuve par réapplication** — le fragment remplacé apparaît une fois et une seule, et la
réapplication redonne la cible à l'octet.

**En-tête des quatre invariants** — présent ou absent.

---

## 7. Le flux — un versement par jour

Le fil de tête écrit, décide, inscrit. En fin de journée il rend **un paquet de versement** :
tout ce qui est preuve part au dépôt, l'index se régénère, les contrôles tournent, la branche se
ferme. **Ce qui part du coffre y est effacé** — c'est ce qui l'empêche de se remplir, et surtout
d'avoir deux vérités.

L'auteure pousse ce paquet. **Une ligne, une fois par jour.**

**Un mandat de session de code ne renvoie jamais à un chemin du coffre.** Il porte son contenu
verbatim, ou il renvoie à un chemin du dépôt.

**Un fil se clôt sans rien laisser sans domicile.** S'il ne peut pas pousser, il rend son paquet
avant de se fermer.

**Les chiffres ne bloquent jamais les textes.** Montants provisoires déclarés, recalage au
dernier moment, et le recalage ne change aucune adresse.

---

## 8. Procédure (i) — notre travail

**Ouverture.** Le fil de tête lit la dernière passation et l'index. Il rend l'état en dix lignes
et attend.

**Production.** Un sous-fil par objet, chacun avec ses quatre invariants et un domicile qui ne
croise aucun autre. Domiciles disjoints, ils tournent en parallèle ; domiciles communs, en
série. Le fil de tête relit la sortie, pas seulement le compte rendu.

**Arbitrage.** Ce qui touche un objectif, un input, un output ou une subtilité remonte à
l'auteure, en une ligne, en question fermée, dans ses mots. Le reste se tranche et s'inscrit.

**Clôture.** Paquet de versement, passation, arbitrages inscrits.

**Audit.** À intervalle choisi par l'auteure : pièces contre registres, registres contre
arborescence, adresses contre le droit. L'audit est mécanique ; ce qu'il ne peut pas juger — la
voix, l'ordre de lecture, ce qui frappe — se relit, et on ne confond pas les deux.

---

## 9. Procédure (ii) — la machine

**Ce qu'elle est.** Un paquet qu'un tiers déplie et fait tourner sans nous, et qui rend, d'un
énoncé en langage naturel, un amendement déposable : siège contrôlé, disposition prouvée, exposé
au gabarit, gage et place en liasse.

**Ce qui lui manque :** deux montages concurrents jamais fusionnés, un installateur de droit
absent du dépôt, un mini-lot d'essai jamais rejoué de bout en bout contre un socle réparé.
**Elle n'est pas livrable.**

**Ce qui la rend livrable, dans l'ordre.**

1. Fusionner les quatre montages en un paquet unique. Sur l'installateur et le contrôle de
   sortie, la version a3 fait foi ; ses procédures ne sont pas des doublons — un relevé a mesuré
   142 fuites sur les originaux.
2. Verser l'installateur de droit au dépôt et corriger ce qu'il suppose : il cherche un dossier
   `droit/` qui n'existe pas, le manifeste étant à `data/_manifeste.json`.
3. Rejouer le mini-lot d'essai de bout en bout contre le socle réparé.
4. Une seule porte d'entrée : une commande qui installe, juge la fraîcheur du droit, et rend la
   main.

**La règle de livraison** : la machine se juge sur un tiers qui l'installe sans nous, et sur rien
d'autre.

---

## 10. Le passage à cette architecture — trois mandats, dans l'ordre

1. **Vider le coffre de ses preuves.** Les 41 pièces déposables, les registres, les relevés —
   sièges de niches fiscales et sociales, concours discrétionnaires, tables de passage — vont au
   dépôt. Le coffre tombe à une cinquantaine de documents.
2. **Réparer l'index et ajouter les deux contrôles.** Les 98 anomalies bloquantes se purgent là.
3. **La machine**, avec le paquet des quatre montages.

Le premier est le plus lourd et le plus urgent : tant qu'il n'est pas fait, le travail de la
journée n'est ni versionné, ni contrôlable, ni visible d'une session de code.

---

## 11. Ce qui reste à l'auteure

Le fond : objectifs, périmètre, paramètres, arbitrages. Et un geste matériel : pousser le paquet
de versement. **Un par jour.**
