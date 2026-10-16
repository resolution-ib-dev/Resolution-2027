# LISEZ-MOI — machine à amendements 2027

Cette machine produit des **amendements déposables** au projet de loi de finances
et au projet de loi de financement de la sécurité sociale, exportés en `.docx`.
Elle est livrée pour que vous produisiez les vôtres, sur vos propres mesures.

---

## Les quatre gestes

**1. Déposez les pièces jointes.** Créez un projet Claude, versez-y tout le
contenu du zip. Rien à installer : les procédures et les référentiels se lisent
tels quels.

**2. Clonez le droit.** Une commande, qui clone, rafraîchit, et refuse de vous
laisser rédiger sur un extrait périmé :

```
python3 appareil/installer_droit.py
```

**3. Jouez la chaîne de test.** Avant toute rédaction :

```
python3 tests/jouer.py
```

**4. Écrivez l'énoncé.** Une phrase en français ordinaire — « supprimer le taux
réduit sur tel service », « plafonner telle taxe affectée » — et laissez la
chaîne dérouler selon `procedures/conduite.md`. Elle vous reparle à cinq
moments, et aucun n'est bloquant.

---

## 1. Ce que c'est

Une méthode, des référentiels, des outils et des contrôles. **Pas un modèle** :
c'est votre projet Claude qui rédige, et ce paquet lui donne de quoi le faire
sans inventer.

Ce qu'il change par rapport à une rédaction à main nue :

- **le texte en vigueur se relève, il ne se cite pas de mémoire.** La base de
  droit rend le verbatim de soixante-dix textes et **lève sur un article absent
  plutôt que d'en rendre un voisin**. Une absence est une information ;
- **le siège juridique se trouve par procédure**, et quand il ne se trouve pas il
  se déclare introuvable ;
- **les textes déposés sont lus**, article par article, et la machine sait quels
  articles le véhicule ouvre déjà ;
- **tout se contrôle**, et un contrôle qui ne peut pas s'exercer le dit au lieu
  de passer.

## 2. Ce que contient le paquet

| dossier | ce qu'on y trouve |
|---|---|
| `appareil/` | les outils — installation du droit, lecture des textes déposés, relevé des articles ouverts, contrôle de sortie, **impression `.docx`** |
| `procedures/` | la méthode — conduite de chaîne, vecteurs, rattachement, forme canonique, gage, gabarits d'exposé et de liste d'articles, domaine des lois de financement, structure d'une proposition de loi |
| `referentiels/` | les articles ouverts par chacun des deux textes déposés, et les relevés transversaux |
| `mini-lot/` | la recette — un énoncé, la sortie attendue, le mode d'emploi |
| `tests/` | les cinq modules de test et leur lanceur |

## 3. L'installation

Il vous faut `git`, Python 3.9 ou plus, et un accès réseau pour le premier
clonage. Pour l'impression `.docx`, `python-docx` :

```
pip install python-docx
```

Le droit vit dans un dépôt public qui porte les codes en vigueur lisibles hors
ligne — **en lecture seule, sans clé, sans compte, sans quota et sans
autorisation**.

```
python3 appareil/installer_droit.py
```

Cette commande clone le dépôt s'il est absent, le met à niveau s'il est là, lit
le millésime **dans le manifeste de l'extrait** et rend un verdict : `FRAIS` ou
`PERIME`. Sur `PERIME`, elle tente le rafraîchissement, et si celui-ci n'aboutit
pas elle sort en erreur et dépose un marqueur dans le clone.

Elle refuse trois choses, et ce sont elles qui comptent :

- **elle ne déduit jamais le millésime de l'horloge.** Il se lit dans l'extrait.
  Un extrait arrêté en amont et estampillé du jour se lirait frais, il serait
  faux, et rien d'autre ne le dirait ;
- **elle ne se replie pas en silence.** Quand la source officielle ne répond pas,
  elle dit laquelle, sur quoi elle se replie, et ce que vaut ce repli ;
- **elle n'échoue pas discrètement.** Code de sortie non nul, bulletin écrit sur
  disque, marqueur dans le clone.

Options : `--etat` juge l'existant sans rien toucher · `--racine CHEMIN` choisit
où poser le clone · `--peremption N` déplace le seuil, qui est de 45 jours.

## 4. Le premier essai

```
python3 tests/jouer.py
```

Cinq modules, et chacun dit ce qu'il mesure :

| module | ce qu'il prouve |
|---|---|
| `test_integrite` | chaque pièce du paquet est à l'octet celle que le manifeste déclare |
| `test_docx` | l'impression ne perd ni ne substitue **aucun caractère** — insécables, apostrophes, guillemets et tirets comptés un à un |
| `test_droit` | la base répond, son millésime est frais, un article absent lève, **et aucun relevé n'est périmé** |
| `test_socles` | les socles se régénèrent **à l'octet** depuis les textes enregistrés |
| `test_recette` | la chaîne rend un amendement déposable de bout en bout |

**Lire le bilan.** `ÉCHEC` — une mesure contredit l'attendu : rien ne se livre.
`ABSENT` — la mesure n'a pas eu lieu, faute d'une pièce ; **ce n'est pas un
succès**, et le bilan nomme ce qui manque. `PASSE` — la mesure a eu lieu et elle
concorde.

Deux `ABSENT` sont normaux sur une installation neuve : `test_socles` sans les
deux PDF des textes déposés, et le temps 2 de `test_recette` tant que vous
n'avez pas fait produire votre première pièce.

## 5. Ce que la machine fait, et ce qu'elle ne fait pas

### Fait

- relève le texte en vigueur, en verbatim, avec l'identifiant de version
- trouve le siège juridique d'une mesure, ou déclare qu'il ne se trouve pas
- dit si la mesure passe dans le véhicule visé, et par quelle porte
- écrit la disposition modificative et la prouve par réapplication
- écrit l'entrée en vigueur, le gage et, s'il y a lieu, le bloc de crédits
- écrit l'exposé sommaire à son gabarit
- assemble la liasse et l'imprime en `.docx`, sommaire paginé compris

### Ne fait pas, et c'est à vous

- **décider de la mesure.** La machine porte une méthode, pas une doctrine
- **chiffrer.** Un montant vient de l'annexe de l'exercice, relevé par vous
- **arbitrer l'ordre de consommation des gages** entre vos pièces
- **déposer.** Le dépôt se fait sur l'extranet de l'assemblée concernée

## 6. Le millésime, et comment vous le changez

Le paquet est calé sur les textes **enregistrés à l'Assemblée nationale** :
**PLF 2027 n° 3210** et **PLFSS 2027 n° 3211**. Les deux PDF ne sont pas joints —
ils pèsent 3,7 Mo et se téléchargent chez l'Assemblée. Leurs empreintes SHA-256
sont au relevé `referentiels/socles_2027.sha256`, et `test_socles` les vérifie.

Pour un autre millésime : déposez les deux PDF sous `sources/`, rejouez
`appareil/socle_texte_2027.py` avec son profil, puis `articles_ouverts_plf.py`.
**L'extracteur refuse le profil tacite** : sans son troisième argument, les
repères du texte de finances s'appliquent, ne se retrouvent pas sur le texte de
financement et la génération s'arrête. C'est voulu — un second extracteur ferait
deux grammaires d'adresse, donc deux points de vérité.

## 7. Ce que vous devez chercher vous-même

- **les montants.** Ils vivent dans les annexes « Voies et moyens », tome I pour
  les taxes affectées, tome II pour les dépenses fiscales, et dans l'état B pour
  les crédits. Le paquet dit où lire et comment lire ; il ne porte pas les
  chiffres
- **les textes non portés par la base.** Soixante-dix sont là ; les autres se
  relèvent sur le site public du droit, et la référence se vérifie
- **l'opportunité politique.** La machine dit ce qui est possible en droit

## 8. Version et contrôles

| | |
|---|---|
| version | **2.0**, 20261016 |
| textes de référence | PLF 2027 n° 3210 · PLFSS 2027 n° 3211 |
| base de droit | 70 textes |
| manifeste | `MANIFESTE.md`, une ligne par pièce avec octets et SHA-256 |

**Le manifeste est le test, pas un inventaire.** `test_integrite` confronte
chaque pièce à sa ligne et refuse une pièce que le manifeste ignore. C'est ce qui
a manqué à la version précédente : son manifeste était exact, et cinq de ses
pièces n'existaient plus nulle part ailleurs.

## 9. Les trous connus

Ils se déclarent, et ils n'empêchent pas de produire.

- **le relevé des portes du domaine des lois de financement se périme.** Il porte
  sa date ; `test_droit` la mesure et échoue au terme. Le relevé joint est au
  millésime LEGI 20261013 — **31 portes en verbatim, 0 en échec** — et il porte
  au 27 novembre 2026. Passé ce terme, il se rafraîchit en une commande, depuis
  la base de droit, et le test repasse au vert
- **les annexes obligatoires des lois de financement ne sont pas relevées** — le
  domaine l'est, ces deux articles non
- **le croisement entre le domaine des lois de financement et celui des lois de
  finances n'est pas fait**, alors que trois portes y renvoient
- **le rattachement d'une mesure à un texte financier se plaide**, il ne se
  prouve pas par une porte du domaine. La procédure le dit à chaque verdict
- **l'impression pose les renvois de pagination en champs vivants** : ils se
  calculent à l'ouverture du document. Un lecteur qui n'actualise pas les champs
  voit la colonne `page` vide ; c'est voulu, et c'est ce qui garde l'invariant de
  caractères exact
