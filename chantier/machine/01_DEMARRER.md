# 01 — DÉMARRER

**Pour l'assistant.** L'utilisateur vous a donné ce jeu et vous a dit
« installe ». Voici ce que cela veut dire.

---

## D'abord, toujours

```
python3 68_CONTROLE_atelier.py
```

Il rend une voie. **Si vous ne pouvez pas exécuter cette ligne, vous êtes en
voie B.**

| voie | ce que vous avez | allez au § |
|---|---|---|
| **A** | `git`, `python3`, le réseau | **Voie A** |
| **B** | pas de `git`, ou pas de terminal du tout | **Voie B** |

---

## Comment ce jeu est rangé

Un seul niveau, aucun sous-dossier. **Le numéro porte l'ordre, le nom porte le
sujet.**

| tranche | contenu |
|---|---|
| `00`–`01` | ce que vous lisez |
| `02`–`07` | **les procédures** — la conduite de la chaîne et ses annexes |
| `10`–`20` | **les outils** — à consulter à chaque étape. **Ils appartiennent à l'utilisateur** : il peut les modifier |
| `30`–`31` | **les références** — ce qui se relève et ne se rédige pas |
| `40`–`43` | **les scripts** |
| `50`–`52` | **la recette** |
| `60`–`68` | **les contrôles** |
| `90`–`99` | relevé du manifeste, et le manifeste |

**Ce jeu ne porte pas les sources.** Il porte la méthode, et il vous dit où les
sources sont.

---

# Voie A — terminal complet

## Geste 1 — aller chercher les sources

```
git clone --depth 1 https://github.com/resolution-ib-dev/Resolution-2027 depot
```

Le dépôt est **public** : pas de clé, pas de compte, pas de quota.

| source | dans le clone | pour quoi |
|---|---|---|
| **la base de droit** | `depot/droit.py`, `depot/codes.json`, `depot/data/` | le verbatim du texte en vigueur — étape `E3` |
| **les socles des textes déposés** | `depot/chantier/referentiels/socle_texte_plf2027.json` · `…plfss2027.json` | le véhicule, article par article |
| **les articles ouverts** | `depot/chantier/referentiels/articles_ouverts_plf2027.tsv` · `…plfss2027.tsv` | ce que le texte déposé ouvre déjà — `E1`, `E2` |
| **les relevés transversaux** | `depot/chantier/referentiels/releves_transversaux_plf2027.tsv` · `…plfss2027.tsv` | les mesures du texte, relevées |
| **les deux textes en PDF** | `depot/chantier/sources/l17b3210_projet-loi.pdf` · `l17b3211…` | la pièce qui fait foi |
| **les extracteurs** | `depot/chantier/appareil/socle_texte_2027.py` · `articles_ouverts_plf.py` | régénérer les socles sur un millésime neuf |

**Si le clone échoue, arrêtez-vous et dites-le.** Sans les sources vous
rédigeriez de mémoire, et c'est ce que cette machine existe pour empêcher.

## Geste 2 — le droit est-il frais

```
python3 depot/droit.py etat
```

**Au-delà de quarante-cinq jours elle imprime `À REJOUER` : arrêtez-vous.** On ne
rédige pas sur un droit dont on ignore s'il a changé.

## Geste 3 — les contrôles

```
pip install python-docx
DROIT=depot python3 61_CONTROLE_jouer.py
```

**Lisez le bilan ainsi :**

- `ÉCHEC` — une mesure contredit l'attendu. **Rien ne se produit tant qu'il en
  reste un.** Nommez-le à l'utilisateur.
- `ABSENT` — la mesure n'a pas eu lieu, faute d'une pièce, et le bilan dit
  laquelle. **Ce n'est pas un succès.** Deux `ABSENT` sont attendus : le contrôle
  de fuites, sans objet ici, et le second temps de la recette.
- `PASSE` — la mesure a eu lieu et elle concorde.

## Geste 4 — la recette

Avant la première mesure réelle : lisez `50_RECETTE_enonce.md`, produisez
l'amendement qu'il demande en déroulant `02_PROCEDURE_conduite.md`, puis

```
DROIT=depot python3 66_CONTROLE_recette.py --sortie votre_piece.md
```

**Ne lisez pas `51_RECETTE_sortie_attendue.md` avant d'avoir produit.**

## Rendez quatre lignes à l'utilisateur

La voie, le millésime du droit, le bilan des contrôles, et ce qu'il peut faire
maintenant. **Pas davantage.**

---

# Ce que vous laissez derrière vous

**L'atelier s'efface, le projet reste.** Un espace de travail est effacé après
une période d'inactivité, et une installation qui n'a rien écrit ailleurs oblige
à redonner ce jeu dans le fil suivant.

**Écrivez donc, avant de rendre la main, une pièce d'amorçage au projet** —
l'espace partagé entre les fils, s'il y en a un, aux côtés des autres documents
de méthode. Nommez-la `methode/installer_la_machine.md`. Elle porte, et rien de
plus :

- l'adresse du dépôt et les trois lignes du geste d'installation ;
- la version de la machine et son compte de pièces ;
- où se trouve la base de droit après le clone, et comment la passer aux
  contrôles ;
- les deux recettes à jouer avant la première mesure réelle ;
- les lignes de la mise à jour.

**Si elle existe déjà**, comparez sa version à celle du manifeste. Plus
récente ici, vous la réécrivez. Égale, vous n'y touchez pas.

**Si le fil n'a pas de projet partagé**, dites-le à l'utilisateur en une phrase,
et dites-lui que le jeu devra être redonné au prochain fil. Ne faites pas comme
si l'installation avait survécu.

**Dès lors, le zip n'est plus la voie d'installation.** Un fil qui sait cloner
n'a rien à recevoir. Le zip ne sert que si le dépôt est injoignable depuis
l'atelier.

---

# Voie B — terminal nu, ou pas de terminal

**Dites-le d'abord à l'utilisateur, en une phrase :** dans cet atelier la machine
ne peut pas relever le droit en vigueur par elle-même, ni produire le `.docx`.
Elle reste utile — la méthode, les gabarits, les contrôles de forme — mais **la
pièce finale demandera un atelier avec terminal, ou un relevé à la main.**

## B1 — les sources en texte, par le web

Le dépôt se lit aussi en HTTPS brut, sans clé. Si vous savez consulter une page,
allez chercher ces fichiers, dont le contenu est du texte lisible :

```
https://raw.githubusercontent.com/resolution-ib-dev/Resolution-2027/main/
```

suivi de :

| fichier | ce qu'il donne |
|---|---|
| `codes.json` | **l'inventaire des textes** que la base de droit porte, et son millésime |
| `chantier/referentiels/articles_ouverts_plf2027.tsv` | les articles ouverts par le texte de finances |
| `chantier/referentiels/articles_ouverts_plfss2027.tsv` | ceux du texte de financement |
| `chantier/referentiels/releves_transversaux_plf2027.tsv` | les mesures relevées au texte de finances |
| `chantier/referentiels/releves_transversaux_plfss2027.tsv` | celles du texte de financement |
| `chantier/referentiels/socle_texte_plf2027.json` | le texte déposé, article par article |
| `chantier/referentiels/socle_texte_plfss2027.json` | idem, texte de financement |

**La base de droit ne se lit pas ainsi** : elle est en archives compressées, et
sans terminal vous ne pouvez ni les ouvrir ni les interroger.

## B2 — le verbatim du droit, puisque la base est hors d'atteinte

Relevez chaque article **sur le site public du droit**, et non de mémoire.

**Trois règles, et elles ne se négocient pas.**

1. **Copiez le texte, ne le reformulez jamais.** Une disposition modificative se
   construit sur les mots exacts.
2. **Notez la date de version et l'identifiant de l'article.** Sans eux, vous ne
   saurez pas plus tard sur quel état vous avez travaillé.
3. **Si vous ne trouvez pas l'article, dites-le et arrêtez-vous.** Un article
   voisin produit un amendement inopérant que rien ne signalera avant la séance.

**Vous n'avez pas le filet de la base de droit**, qui lève sur un article absent
plutôt que d'en rendre un approchant. Ici, c'est vous le filet. Dites-le à
l'utilisateur.

## B3 — ce que vous pouvez encore jouer

Toute la méthode : `02_PROCEDURE_conduite.md`, les outils `10` à `20`, les
gabarits. Les huit étapes se déroulent, et les contrôles de forme se jouent à la
lecture.

**Ce que vous ne pouvez pas :** les six contrôles automatiques, l'invariant de
caractères, et l'export `.docx`. Rendez la pièce **en markdown**, au gabarit de
`51_RECETTE_sortie_attendue.md`, et dites à l'utilisateur qu'un atelier avec
terminal la convertira — ou qu'il la mettra en forme lui-même aux conventions de
`19_OUTIL_impression_docx.md`.

---

## Produire, dans les deux voies

L'utilisateur donne sa mesure. Vous déroulez `02_PROCEDURE_conduite.md`, huit
étapes, en consultant à chacune l'outil qu'elle nomme.

**Quatre règles pour toute la chaîne.**

1. **Ne devinez jamais une adresse de droit.** Une absence est une information.
2. **Une étape qui ne conclut pas écrit `hors_capacite` et la chaîne s'arrête.**
3. **Ne réécrivez pas une étape antérieure en passant** : dites-le et remontez.
4. **Tout va dans le dossier de mesure**, jamais dans le fil de conversation.

## Mettre à jour

L'utilisateur dit « mets à jour la machine ».

**Voie A :**

```
python3 90_SCRIPT_relever_manifeste.py --juger
cd depot && git pull --ff-only && cd ..
python3 depot/droit.py etat
DROIT=depot python3 61_CONTROLE_jouer.py
```

**Voie B :** rechargez les fichiers de B1 depuis le web et comparez leur
millésime à celui que vous aviez.

La première ligne de la voie A dit si **ses** outils ont bougé. S'il en a modifié
un, elle le nomme, et **ce n'est pas un défaut** : les outils `10` à `20` sont à
lui. Une procédure modifiée, elle, sort en échec.

**Rendez-lui quatre lignes** : ce qui a changé chez lui, le millésime du droit, le
bilan, ce qu'il peut faire.
