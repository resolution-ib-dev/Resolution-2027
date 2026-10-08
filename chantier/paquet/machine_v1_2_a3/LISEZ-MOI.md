# LISEZ-MOI

## Les trois gestes

Rien d'autre à faire pour commencer. Le détail de chacun est plus bas ; ces
trois lignes suffisent à partir.

**1. Déposez les pièces jointes.** Créez un projet Claude, versez-y tout le
contenu du zip. Il n'y a rien à installer : les pièces de méthode et les
référentiels se lisent tels quels.

**2. Clonez le droit.** Une commande, et elle s'occupe de tout — clonage,
rafraîchissement, et refus de vous laisser rédiger sur un extrait périmé :

```
python3 appareil/installer_droit.py
```

**3. Écrivez l'énoncé.** Une phrase en français ordinaire — « supprimer le taux
réduit sur tel service », « plafonner telle taxe affectée » —, et laissez la
chaîne dérouler selon `procedures/conduite.md`. Elle vous reparle à cinq
moments, et aucun n'est bloquant.

---

## 1. Ce que c'est

Une chaîne qui prend une idée de mesure écrite en français ordinaire — « supprimer
tel opérateur », « plafonner telle taxe » — et rend un amendement déposable au
projet de loi de finances ou au projet de loi de financement de la sécurité
sociale pour 2027, exporté en `.docx`.

Ce n'est pas un budget alternatif. Un contre-budget prend la forme d'amendements,
c'est-à-dire d'une suite de modifications d'un texte qu'on ne maîtrise pas : le
texte déposé dit où écrire, la position politique dit seulement quoi. Et la chaîne
**outille** un travail juridique, elle ne l'automatise pas : une disposition
plausible et fausse est plus dangereuse qu'une disposition absente.

## 2. Ce que contient le paquet

```
LISEZ-MOI.md
procedures/     les treize pièces de méthode — conduite, contrat de chaîne,
                rattachement, vecteurs, gage, gabarit d'exposé, structure de
                proposition de loi, règles rédactionnelles, forme canonique, dépôt
                de droit, domaine des lois de financement, renvois entrants,
                gabarit de liste
appareil/       les huit modules :
                  installer_droit.py          installation et fraîcheur du droit
                  socle_texte_2027.py         lecture du texte déposé, article par article
                  pieces_nommees.py           table close des codes, utilisée par les deux suivants
                  portes_ouvertes.py          relevé des articles que le texte modifie
                  index_mesures_2027.py       index des mesures et relevés transversaux
                  redaction_2027.py           rédaction exacte, alinéa par alinéa
                  controle_sortie.py          contrôle qu'aucune pièce ne nomme ce qu'elle ne doit pas
                  generateur_liasse_docx.py   rendu .docx
referentiels/   les référentiels du millésime 2027 — voir section 9
mini-lot/       un énoncé joué de bout en bout, avec sa sortie attendue
```

`droit.py`, `extraire_legi.py` et `codes.json`, qui lisent le droit, ne sont pas
dans le zip : ils arrivent avec le dépôt de droit que la commande d'installation
clone. Une seule copie, celle du dépôt, et elle ne peut pas diverger.

Deux pièces se lisent avant toute production : `procedures/conduite.md`, qui dit
comment une session s'ouvre, décide et se clôt, et
`procedures/contrat_chaine_amendement.md`, qui dit ce que chaque étape reçoit, ce
qu'elle rend et ce dont elle a douté. Les autres se lisent au moment où l'étape
les appelle.

## 3. L'installation

Geste 1 : créez un projet Claude, versez-y le contenu du zip. C'est tout pour les
pièces de méthode et les référentiels.

Geste 2 : le droit. Il vit dans un dépôt public qui porte les codes en vigueur
lisibles hors ligne — **en lecture seule, sans clé, sans compte, sans quota et
sans autorisation**. Il vous faut `git`, Python et un accès réseau.

```
python3 appareil/installer_droit.py
```

**Cette commande remplace les gestes manuels de la version précédente.** Elle
clone le dépôt s'il est absent, le met à niveau s'il est là, lit le millésime de
la base dans le manifeste de l'extrait, et rend un verdict : `FRAIS` ou `PERIME`.
Sur `PERIME`, elle tente le rafraîchissement, et si celui-ci n'aboutit pas elle
**sort en erreur et dépose un marqueur `EXTRAIT_PERIME` dans le clone**. Vous ne
pouvez pas la rater.

Elle refuse trois choses, et ce sont elles qui comptent :

- **elle ne déduit jamais le millésime de l'horloge.** Il se lit dans l'extrait,
  et nulle part ailleurs. Un extrait arrêté en amont et estampillé du jour se lit
  frais, il est faux, et rien d'autre ne le dirait ;
- **elle ne se replie pas en silence.** Quand la source officielle ne répond pas,
  elle dit laquelle, sur quoi elle se replie, et ce que vaut ce repli ;
- **elle n'échoue pas discrètement.** Code de sortie non nul, bulletin écrit sur
  disque (`BULLETIN_DROIT.json`), marqueur dans le clone.

Options utiles : `--etat` juge l'existant sans rien toucher ; `--racine CHEMIN`
choisit où poser le clone ; `--peremption N` déplace le seuil, qui est de 45
jours.

Pourquoi ce détour plutôt qu'une lecture directe du site public du droit : celle-ci
échoue le plus souvent depuis une session de travail — neuf tentatives, un succès,
huit refus. Le dépôt supprime cette dépendance. Les détails sont dans
`procedures/depot_droit.md`.

## 4. Le premier essai

```
python3 appareil/installer_droit.py --etat
cd appareil
python3 controle_sortie.py --epreuve
python3 generateur_liasse_docx.py ../mini-lot/sortie_attendue.md -o /tmp/essai.docx
```

La première ligne doit rendre `VERDICT : FRAIS`. La deuxième éprouve le contrôle
de généralisation sur son propre jeu de fautes et son jeu de justes : elle doit
répondre `ÉPREUVE : verte`. La troisième rend une pièce en `.docx` et vérifie du
même coup que le contrôle, la lecture du markdown et l'écriture du document
s'enchaînent.

L'essai de bout en bout, lui, se conduit à la main : il rejoue l'énoncé du
`mini-lot/` selon `procedures/conduite.md`. Comparez la sortie
obtenue à la sortie attendue jointe dans le même dossier : si elles concordent,
votre installation est bonne et vous pouvez lancer votre premier énoncé. Si elles
divergent, l'écart désigne l'étape à reprendre — n'enchaînez pas.

## 5. Ce que la machine fait, et ce qu'elle ne fait pas

C'est la section qui compte. Lisez les deux tableaux, pas seulement le premier.

### Fait

| étape | ce qui sort |
|---|---|
| Accès au droit | le dépôt cloné et jugé frais ou périmé, sans geste manuel — `appareil/installer_droit.py` |
| Lecture du texte déposé | le relevé des articles que le texte ouvre, par où un amendement peut entrer |
| Qualification | le statut de la mesure — crédits, dépense fiscale, dépense sociale, dépense locale, dépense d'opérateur, pure norme — et le levier |
| Vecteur | le siège juridique à modifier, c'est-à-dire l'article de code visé |
| Droit applicable | le texte en vigueur, daté, avec son identifiant de version, et les renvois entrants relevés à travers les vingt codes portés |
| Rédaction cible | le texte de l'article tel qu'il sera, puis la disposition modificative qui en est dérivée, **prouvée par réapplication** |
| Exposé sommaire | 200 à 300 mots, trois temps, chaque chiffre avec sa source entre parenthèses et en note |
| Gage | la formule de compensation applicable au cas, relevée sur pièce et reprise au mot |
| Sortie | l'amendement en `.docx` déposable — `appareil/generateur_liasse_docx.py`, une liasse ou une pièce par fichier, contrôle de généralisation joué avant écriture |

### Ne fait pas — et c'est à vous

| ce qui n'est pas outillé | ce que vous faites |
|---|---|
| **La recevabilité financière et le rattachement** | La procédure est écrite — `procedures/test_rattachement.md`, et `procedures/domaine_lfss_LO111-3.md` pour les lois de financement — mais elle se conduit à la main. **Aucun contrôle n'arrêtera un amendement irrecevable.** Une charge nouvelle n'est jamais gageable : si la mesure en crée une, le gage ne la sauve pas, elle se réécrit ou elle tombe. |
| **L'ordre de dépôt et les neutralisations réciproques d'une liasse** | Ce sont des décisions politiques. Deux amendements peuvent se contredire, se vider l'un l'autre, ou gager deux fois la même ligne : la machine ne tranche pas et ne le voit pas. Tenez le compte des lignes employées. |
| **Le droit non codifié** | L'extrait porte vingt codes. Un siège logé dans une loi de finances antérieure ou dans une loi non codifiée n'y est pas, et un renvoi porté par un texte non codifié n'est pas vu. Ces cas se traitent à la main. |
| **Le rafraîchissement, quand la source officielle ne répond pas** | Le module d'installation le tente et vous dit s'il a abouti. S'il n'aboutit pas, le repli est l'action programmée du dépôt, qui rejoue l'extraction le 1er de chaque mois : relancez le module après son passage, ou reclonez. **Rien n'autorise à rédiger entre-temps** — et le marqueur `EXTRAIT_PERIME` est là pour vous le rappeler si vous avez fermé la console. |

Un piège mérite d'être nommé séparément, parce qu'il est invisible. Un texte
financier déposé en octobre modifie des articles qu'une loi promulguée en décembre
a déjà changés : au millésime courant, l'article porte le **résultat** de la
modification, pas son point de départ. Le droit en vigueur se lit donc à une date
— `python3 droit/droit.py article <code> <numéro> --au AAAA-MM-JJ` — dès que
l'article visé a été touché depuis le dépôt du texte. Et la reconstruction
inverse, qui consisterait à défaire la disposition sur le texte actuel, est
fausse : le droit porte l'effet de la loi adoptée, amendements compris, pas celui
de la disposition déposée.

## 6. Le millésime, et comment vous le changez

Le paquet est réglé sur les textes déposés en 2027 : les référentiels livrés
portent les articles que ces textes ouvrent et les relevés qui en sont tirés.

Les modules de lecture, eux, ne sont pas réglés sur un millésime : ils rejouent
n'importe quel texte financier à partir de son PDF. **C'est ce qui distingue cette
machine d'une photo.** Pour l'exercice suivant :

1. Récupérez le PDF du texte déposé — projet de loi de finances ou projet de loi
   de financement de la sécurité sociale de l'exercice visé.
2. Rejouez dessus les modules de lecture du dossier `appareil/` — commande :
   ```
   cd appareil
   python3 socle_texte_2027.py  <texte.pdf> plf<AAAA>  socle.json
   python3 portes_ouvertes.py   socle.json plf<AAAA> <AAAA-MM-JJ> ../referentiels/articles_ouverts_plf<AAAA>.tsv
   python3 index_mesures_2027.py socle.json plf<AAAA> ../referentiels/index_mesures_plf<AAAA>.md
   python3 redaction_2027.py    <texte.pdf> plf<AAAA> ../referentiels/articles_ouverts_plf<AAAA>.tsv ../referentiels/redaction_plf.json
   ```

   Remplacez `plf` par `plfss` pour le projet de loi de financement. Remplacez
   ensuite les fichiers du dossier `referentiels/` par ceux qu'ils produisent.
3. Rejouez `python3 appareil/installer_droit.py` avant de rédiger, puis rejouez le
   `mini-lot/` pour vérifier que la chaîne tourne sur le nouveau millésime.

Les pièces de méthode, elles, ne changent pas : elles sont écrites
véhicule-agnostiques et millésime-agnostiques.

## 7. Ce que vous devez chercher vous-même

**Les annexes détaillées du projet de loi de finances pour 2027 n'étaient pas
parues à la constitution du paquet.** La conséquence est concrète et elle touche
le gage.

Les lignes de dépense fiscale qui servent à gager se prennent à l'annexe
« Évaluation des voies et moyens, tome II — Dépenses fiscales ». Chaque ligne y
porte un numéro, un libellé exact et un chiffrage par exercice : c'est ce numéro et
ce libellé que le gage reprend, un gage qui dirait « une niche de l'impôt sur le
revenu » ne désigne rien.

**Où la chercher** : partez de la page consacrée au projet de loi de finances de
l'exercice visé sur le site de l'Assemblée nationale, rubrique des annexes
budgétaires, et suivez la liste jusqu'au tome II des voies et moyens. Les mêmes
documents sont mis en ligne par le ministère chargé du budget. *L'adresse exacte
n'est pas relevée ici et ne doit pas être devinée.*

**En attendant la parution**, travaillez sur l'annexe de l'exercice 2026 : elle
couvre les mêmes lignes à quelques créations et extinctions près. Toute valeur
reprise d'un millésime antérieur porte alors, **dans vos notes de travail et non
dans l'amendement**, la mention « approchant 2026, à rejouer ».

Deux pièges de lecture de cette annexe : les symboles `ε`, `nc` et `-` ne sont pas
des nombres et ne se lisent jamais comme zéro — une ligne portant `nc` ne peut pas
servir de gage chiffré ; et une même ligne ne sert pas deux fois de gage dans une
liasse.

Reste également à votre charge le texte déposé lui-même : il n'est pas dans le
dépôt de droit, c'est une autre source.

## 8. Version et contrôles

Version `1.2`, 3 octobre 2026. **Non transmissible en l'état** : elle n'a passé
qu'une des trois passes de contrôle. Elle corrige la `1.1` sur quatre points :
les cinq modules de lecture du texte déposé sont joints ; le relevé des articles
ouverts est celui qui ne compte plus les articles cités comme point d'insertion ;
la commande d'installation lit le millésime tel que le dépôt réel l'écrit ; le
contrôle de sortie ne porte plus aucun nom propre — vos propres noms se déclarent
dans un fichier `motifs_locaux.txt` posé à côté du contrôle, une expression
régulière par ligne.

| passe | ce qu'elle éprouve | état |
|---|---|---|
| 1 — reproduction | les modules rejoués sur les deux PDF rendent à l'octet les référentiels joints | **non jouée** |
| 2 — confrontation | les référentiels confrontés au relevé qui fait foi | **jouée le 3 octobre 2026** — écarts ci-dessous |
| 3 — épreuve à froid | une installation faite à partir du seul présent document | **non jouée** |

**Éprouvé avant livraison, et rien d'autre :**

- `python3 appareil/installer_droit.py`, joué contre le dépôt réel : clonage,
  millésime lu dans le manifeste, verdict `FRAIS`. Le premier essai réel a révélé
  que la `1.1` ne savait pas lire ce millésime ; c'est corrigé ;
- le contrôle de sortie passe son jeu de fautes et son jeu de justes, et les
  vingt-sept autres fichiers du paquet le passent sans fuite ;
- les modules s'importent et le rendu `.docx` du `mini-lot/` aboutit.

**Écart de la passe 2, mesuré.** Le relevé des articles ouverts du projet de loi
de finances porte 421 couples (texte, article) ; un relevé indépendant, fait à la
main, en porte 424. **352 sont communs, 69 ne sont que dans le relevé joint, 72
que dans le relevé manuel.** Causes connues : le relevé manuel déclare lui-même
31 de ses adresses « à vérifier », comme renvois plutôt que sièges ; le relevé
joint capte les énumérations — « les articles L. 1, L. 2 et L. 3 » — que le
relevé manuel ne prenait qu'en tête. Les plus forts écarts par texte : code des
impositions sur les biens et services (+7), code de l'éducation (+5), loi
n° 2020-1721 du 29 décembre 2020 (−5), code des assurances (−4). Pour la loi de
financement, aucun relevé indépendant n'existe : l'écart n'est pas mesurable.
Côté cohérence interne, tout article qui porte une porte ouverte figure dans les
relevés transversaux, sur les deux véhicules.

## 9. Les trous connus

Déclarés plutôt que tus.

**Le rendu `.docx` ne porte pas les notes de bas de page.** `python-docx` n'écrit
pas de note ; les appels de note et leur texte sont rendus en fin de pièce, en
petit corps. Si votre dépôt exige de vraies notes, reprenez-les dans un traitement
de texte avant envoi — c'est une minute par pièce.

**Les deux fichiers de rédaction exacte ne sont pas joints.**
`referentiels/redaction_plf.json` et `referentiels/redaction_plfss.json` sont trop
volumineux pour voyager. Ils sont reproductibles : `appareil/redaction_2027.py`
les régénère à partir du PDF du texte déposé, comme en section 6. Un fil qui en a
besoin les reconstruit, il ne les cherche pas.

**Les pièces que les référentiels joints supposent.** Chacun porte en tête
l'empreinte `sha256` du PDF dont il est tiré : projet de loi de finances pour
2027, `b0b802d3cafb313435e9afa16b2760f367a614a758a3f717bcbd58b94944cb54`,
407 pages ; projet de loi de financement de la sécurité sociale pour 2027,
`71010873c0af8a776436e3c22628d3a1dc048ea406632afa2107dc83be7c598d`, 121 pages.
Un autre tirage du même texte — avec son numéro d'enregistrement, par exemple —
change l'empreinte : vos référentiels régénérés ne seront alors pas identiques à
l'octet aux référentiels joints, sans que la chaîne soit en faute.

**Une asymétrie de nommage, qui n'est pas un trou mais qui trompe.** Le relevé
mécanique des portes — les couples (texte, article) que le véhicule modifie
lui-même — s'appelle `articles_ouverts_<véhicule><année>.tsv`, parce que c'est le
nom que `appareil/portes_ouvertes.py` écrit. **Il existe pour les deux
véhicules** : `referentiels/articles_ouverts_plf2027.tsv`, 421 adresses sur 62
textes, et `referentiels/articles_ouverts_plfss2027.tsv`, 153 adresses sur 22
textes. Les relevés transversaux, `referentiels/releves_transversaux_plf2027.tsv`
et `..._plfss2027.tsv`, portent 989 et 390 mesures, cinq relevés chacune.
