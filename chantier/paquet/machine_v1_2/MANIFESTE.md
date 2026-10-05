# Manifeste — machine amendement 2027, version 1.2 (montage B)

> **Deux montages portent le numéro 1.2, et ils sont disjoints.** Celui-ci et
> celui du fil A-3, versé sous `paquet/machine_v1_2_a3/`. Chacun corrige quatre
> points que l'autre n'a pas. Ce manifeste et les trois pièces qu'il nomme ont
> été écrasés par le fil A-3 le 20261003, puis reversés ici le 20261004 depuis
> l'atelier d'origine, intacts. **Aucun des deux zips ne part avant fusion** —
> voir la dernière section.

Versée le 3 octobre 2026. Corrige la `1.1` sur quatre points, tous nés de la
mesure du dépôt de droit qu'un fil Cowork ne pouvait pas faire et qu'une session
de code a rendue le même jour.

**Zip livré** : `machine_amendement_2027_v1.2.zip`, 30 fichiers,
sha256 `4dec4663001d0406ed3641817f2a9e0d40d7cb5834af7d004258be3b0fcb7757`.

---

## Ce que la mesure a établi, et qui commande tout le reste

**Le droit ne peut pas entrer dans les connaissances d'un projet.** Les extraits
sont du gzip binaire : 37,4 Mo pour les codes déclarés, 40,2 Mo pour l'ensemble
du dossier `data/`, et le seul code général des impôts fait 10 870 869 octets une
fois ouvert. La jauge d'un projet se compte en mégaoctets de texte.

**Et aucun élagage ne sauve cette voie.** Réduire l'extrait aux articles que les
textes déposés ouvrent — 574 adresses, PLF et PLFSS confondus — avait été
envisagé puis écarté par l'auteure, et elle a raison : le vecteur d'une mesure est
presque toujours un article que le texte déposé ne touche pas. « Supprimer
l'ADEME » atterrit au code de l'environnement, à mille lieues de ce que la loi de
finances ouvre. Un extrait élagué sur les articles ouverts ne couvre que les
mesures dont on n'a pas besoin.

**Conséquence, et c'est l'objet 1.** Le lieu d'exécution n'est pas une
conversation simple mais une session disposant d'un interpréteur — une tâche
Cowork, une session de code. Là, Claude clone le dépôt lui-même et lit n'importe
quel article à n'importe quelle date. Le problème n'a jamais été l'installation :
c'était le lieu, et la main. La `1.1` demandait à l'utilisateur de taper des
commandes ; c'était la mauvaise main.

**Le dépôt n'a donc pas été monté pour rien.** Il résout le blocage mesuré —
Légifrance, huit refus sur neuf — et il le résout entièrement pour une session
outillée. Ce qu'il ne fait pas, c'est servir un Claude sans interpréteur.

---

## Les quatre objets

### 1. Le mode d'emploi s'adresse à un lecteur en tâche Cowork

Les trois gestes deviennent : déposer les pièces dans un projet, ouvrir une tâche
Cowork et **donner à Claude une phrase d'amorçage copiable**, écrire sa mesure.
Le clonage, la vérification de fraîcheur et l'épreuve du contrôle sont des gestes
de Claude ; l'utilisateur lit un compte rendu.

Une section neuve, « Où la chaîne se conduit, et pourquoi là », porte la
contrainte mesurée plutôt que de la taire. Une autre, « Ce que Claude fait au
démarrage », donne les trois sorties auxquelles reconnaître un démarrage sain —
`VERDICT : FRAIS`, `ÉPREUVE : verte`, un `.docx` écrit — pour qu'un échec se voie.

### 2. `installer_droit.py` lit le manifeste réel

Mesuré : le manifeste est à `data/_manifeste.json`, sa clé est `millesime_legi`,
sa date s'écrit `20261001`. La `1.1` cherchait `manifeste.json` à la racine, une
clé finissant par `millesime`, et une date ISO. **Elle refusait donc un dépôt
parfaitement sain, en code 4.**

Le défaut était du bon côté — le module n'a jamais inventé de date — mais il
bloquait tout le monde, et c'est exactement l'item que la `1.1` déclarait « non
éprouvé faute de réseau ».

Corrigé : la liste des manifestes s'ouvre sur `data/_manifeste.json`, la clé se
cherche par `search` et non par ancrage de fin, et les deux formats de date du
dépôt sont lus et normalisés — `AAAA-MM-JJ` et `AAAAMMJJ`.

**Cinq épreuves rejouées contre la forme réelle du manifeste**, toutes conformes :
millésime lu et verdict `FRAIS` ; millésime reculé de 200 jours, verdict `PERIME`,
code 5, marqueur posé ; retour au frais, marqueur effacé ; date absurde
`20261345`, refus en code 4 ; manifeste muet, refus en code 4. **Aucun chemin ne
substitue la date du jour.**

### 3. `depot_droit.md` porte le compte mesuré

« Vingt codes, 21 Mo » devient **62 entrées déclarées à `codes.json`** — 37,4 Mo
d'extraits de codes, 1,9 Mo de textes non codifiés, 40,2 Mo pour le dossier
entier. La liste des codes n'est plus recopiée dans le document : elle se lit
dans `codes.json`, qui est le seul endroit où l'on ajoute un code, donc le seul
où l'on en lit la liste.

La borne fausse avait traversé plusieurs millésimes par recopie. Le document le
dit en une ligne, parce qu'une borne qui se recopie recommencera.

**Onze extraits orphelins** sont déclarés : présents dans `data/`, absents de
`codes.json` et du manifeste, refusés par le lecteur. Dont quatre codes.

### 4. Les renvois entrants sont déclarés non outillés

`coordination.py` n'existe dans aucune branche du dépôt. `depot_droit.md` le
présentait comme une pièce livrée et l'étape E3 de `conduite.md` faisait reposer
sur lui la liste des renvois en fin d'exposé sommaire.

Les deux documents disent maintenant que l'étape est écrite et que rien ne la
joue, et que le relevé fait à la main **se déclare incomplet** : une liste vide
s'écrit « non relevé », jamais « aucun ». Le `LISEZ-MOI` le porte au tableau des
choses non outillées, au rang immédiatement après la recevabilité.

Une étape documentée qui ne tourne pas est pire qu'une étape déclarée manquante :
le tiers la croit jouée.

---

## Les contrôles rejoués

| contrôle | résultat |
|---|---|
| `installer_droit.py` contre la forme réelle du manifeste | **5 épreuves conformes** |
| `controle_sortie.py --epreuve` | **verte** — 18 fautes, 14 justes |
| contrôle de sortie sur les 17 pièces rédigées | **0 fuite sur 17 pièces** |
| rendu `.docx` du mini-lot | **1 amendement rendu**, 37 160 octets |
| rejeu complet depuis un déballage neuf du zip | **conforme** sur les trois |

---

## Ce qui reste mesuré et non traité

**Les 40 fuites du contrôle de sortie sur les 30 fichiers** restent en l'état, et
l'arbitrage de forme qui les concerne n'est pas rendu : 27 dans
`controle_sortie.py`, qui porte par construction les noms qu'il interdit ; 7 dans
`appareil/portes_ouvertes.py` ; 3 dans chacun des deux `.tsv` mécaniques.

**Le clonage contre le dépôt réel** n'est toujours pas éprouvé : la sortie réseau
de l'atelier le refuse. Le lecteur de millésime, lui, l'a été contre la forme
exacte mesurée au dépôt.

**Le code général de la fonction publique est mesuré orphelin.** Une passation du
2 octobre le donnait « rétabli au référentiel des codes » ; au dépôt mesuré le
lendemain, `cgfp` est dans `data/` et absent de `codes.json`. Le rétablissement
n'a pas atteint la branche mesurée, ou il attend ailleurs. Non traité : hors des
quatre objets.

**La passe 3, l'épreuve à froid**, n'est pas jouée.

---

## Ce qui est versé, et où

| pièce | emplacement | état |
|---|---|---|
| Mode d'emploi | `paquet/machine_v1_2/LISEZ-MOI.md` | **réécrit** |
| Installation du droit | `paquet/machine_v1_2/appareil/installer_droit.py` | **corrigé** |
| Dépôt de droit | `paquet/machine_v1_2/procedures/depot_droit.md` | **corrigé** |
| Conduite de la chaîne | `paquet/machine_v1_2/procedures/conduite.md` | **corrigé** |
| Contrôle de sortie | `paquet/machine_v1_1/appareil/controle_sortie.py` | inchangé depuis la 1.1 |
| Les 11 autres procédures, les 6 autres modules, les 5 référentiels, le mini-lot | `paquet/machine_v1_0/` et racine du projet | inchangés |

Les pièces inchangées ne sont pas recopiées. Le zip, lui, les porte toutes.

---

## La fusion due avant toute transmission

Le fil A-3 a monté une 1.2 le même jour, sur des objets différents. Les deux
montages ne se recouvrent sur aucun point : chacun porte, pour les pièces que
l'autre a touchées, l'état de la 1.1.

| pièce | montage B (ici) | montage A-3 |
|---|---|---|
| `procedures/conduite.md` | **corrigé** — renvois entrants non outillés | état 1.1 |
| `procedures/depot_droit.md` | **corrigé** — 62 entrées, renvois, lieu d'exécution | état 1.1 |
| `LISEZ-MOI.md` | **réécrit** — lecteur en tâche Cowork | réécrit autrement |
| `appareil/installer_droit.py` | **corrigé** — manifeste réel | corrigé de même, éprouvé contre le dépôt réel |
| `appareil/controle_sortie.py` | état 1.1 | **corrigé** — motifs internes sortis du livrable |
| `appareil/portes_ouvertes.py` | état 1.1 | **corrigé** — commentaires nettoyés |
| les deux relevés d'articles ouverts | état 1.1 | **en-têtes réécrits** |
| huit procédures exportées | état 1.1 | **reconstituées**, 142 fuites retirées |
| les cinq modules du millésime | joints | joints, pris au dépôt |

**Le point le plus lourd est le `LISEZ-MOI.md`** : les deux fils l'ont réécrit
entièrement, et les deux réécritures sont incompatibles ligne à ligne. Elle se
tranche, elle ne se fusionne pas mécaniquement.

**Le second est `installer_droit.py`** : les deux fils ont trouvé et corrigé le
même défaut. Celui d'A-3 a été éprouvé contre le dépôt réel, pas celui-ci.
**Celui d'A-3 fait foi.**

Pour le reste, les deux montages s'additionnent sans conflit : chaque pièce est
corrigée d'un côté et inchangée de l'autre.
