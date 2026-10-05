# LISEZ-MOI

## Les trois gestes

Rien à installer, et aucune commande à taper. Le détail est plus bas ; ces trois
gestes suffisent à partir.

**1. Déposez les pièces.** Créez un projet Claude et versez-y le contenu du zip.
C'est là que vivent les pièces de méthode, et elles y restent d'une session à
l'autre.

**2. Ouvrez une tâche Cowork dans ce projet, et dites à Claude de commencer.**
Copiez cette phrase, elle suffit :

> Machine à amendements 2027. Installe-toi : recopie les pièces du paquet sur ton
> disque, clone le dépôt de droit avec `appareil/installer_droit.py`, et
> rends-moi son verdict. Ne rédige rien tant que le droit n'est pas frais.

Claude fait le reste — le clonage, la vérification de fraîcheur, l'épreuve du
contrôle de sortie. Vous lisez son compte rendu, vous ne tapez aucune commande.

**3. Écrivez votre mesure en français ordinaire.** « Supprimer tel opérateur »,
« plafonner telle taxe affectée ». La chaîne déroule selon
`procedures/conduite.md` et vous reparle à cinq moments, dont aucun n'est
bloquant.

---

## 1. Ce que c'est

Une chaîne qui prend une idée de mesure écrite en français ordinaire et rend un
amendement déposable au projet de loi de finances ou au projet de loi de
financement de la sécurité sociale pour 2027, exporté en `.docx`.

Ce n'est pas un budget alternatif. Un contre-budget prend la forme d'amendements,
c'est-à-dire d'une suite de modifications d'un texte qu'on ne maîtrise pas : le
texte déposé dit où écrire, la position politique dit seulement quoi. Et la chaîne
**outille** un travail juridique, elle ne l'automatise pas : une disposition
plausible et fausse est plus dangereuse qu'une disposition absente.

## 2. Où la chaîne se conduit, et pourquoi là

**Il faut une session Claude qui dispose d'un interpréteur** — une tâche Cowork,
ou une session de code. Pas une conversation simple.

Ce n'est pas une préférence, c'est une contrainte mesurée. Le droit en vigueur
vit dans un dépôt public sous forme d'archives compressées : plusieurs centaines
de mégaoctets une fois ouvertes, le seul code général des impôts dépassant les
dix. Les connaissances d'un projet se comptent en mégaoctets de texte. **Verser
le droit en pièce jointe ou le brancher aux connaissances d'un projet ne marche
pas** — ce qui arriverait par cette voie, c'est la liste des codes et les
scripts, jamais la loi.

Dans une tâche Cowork, Claude clone le dépôt lui-même et lit n'importe quel
article à n'importe quelle date. C'est le geste 2, et c'est lui qui fait que vous
n'avez rien à installer : l'interpréteur est celui de Claude, pas le vôtre.

Le dépôt est **public, en lecture seule, sans clé, sans compte, sans quota et
sans autorisation**. Les détails sont dans `procedures/depot_droit.md`.

## 3. Ce que contient le paquet

```
LISEZ-MOI.md
procedures/     les pièces de méthode — conduite, contrat de chaîne, rattachement,
                vecteurs, gage, gabarit d'exposé, structure de proposition de loi,
                règles rédactionnelles, forme canonique, dépôt de droit,
                domaine des lois de financement, renvois entrants, gabarit de liste
appareil/       les modules : installation du droit, lecture du texte déposé,
                contrôle de sortie, rendu .docx
referentiels/   les référentiels du millésime 2027
mini-lot/       un énoncé joué de bout en bout, avec sa sortie attendue
```

Deux pièces se lisent avant toute production : `procedures/conduite.md`, qui dit
comment une session s'ouvre, décide et se clôt, et
`procedures/contrat_chaine_amendement.md`, qui dit ce que chaque étape reçoit, ce
qu'elle rend et ce dont elle a douté. Les autres se lisent au moment où l'étape
les appelle.

## 4. Ce que Claude fait au démarrage, et ce que vous devez y voir

Le geste 2 déclenche trois choses. Elles sont décrites ici pour que vous sachiez
reconnaître un démarrage sain d'un démarrage qui a échoué.

| ce que Claude joue | ce que vous devez lire |
|---|---|
| `appareil/installer_droit.py` | un bulletin avec le millésime de la base, son âge en jours, et `VERDICT : FRAIS` |
| `appareil/controle_sortie.py --epreuve` | `ÉPREUVE : verte` |
| `appareil/generateur_liasse_docx.py` sur le mini-lot | une pièce `.docx` écrite |

**Si le verdict est `PERIME`, rien ne se rédige.** L'extrait n'est plus fiable, et
Claude doit s'arrêter là. Le repli est l'action programmée du dépôt, qui rejoue
l'extraction le 1er de chaque mois : relancez après son passage. **Un amendement
rédigé sur un droit périmé vise un texte qui n'est plus en vigueur, sans que rien
ne le signale.**

L'essai de bout en bout, lui, se conduit ensuite : Claude rejoue l'énoncé du
`mini-lot/` selon `procedures/conduite.md`, et vous comparez sa sortie à la sortie
attendue jointe dans le même dossier. Si elles concordent, votre installation est
bonne. Si elles divergent, l'écart désigne l'étape à reprendre — n'enchaînez pas.

## 5. Ce que la machine fait, et ce qu'elle ne fait pas

C'est la section qui compte. Lisez les deux tableaux, pas seulement le premier.

### Fait

| étape | ce qui sort |
|---|---|
| Accès au droit | le dépôt cloné par Claude et jugé frais ou périmé, sans geste de votre part |
| Lecture du texte déposé | le relevé des articles que le texte ouvre, par où un amendement peut entrer |
| Qualification | le statut de la mesure — crédits, dépense fiscale, dépense sociale, dépense locale, dépense d'opérateur, pure norme — et le levier |
| Vecteur | le siège juridique à modifier, c'est-à-dire l'article de code visé |
| Droit applicable | le texte en vigueur, daté, avec son identifiant de version, sur les codes portés |
| Rédaction cible | le texte de l'article tel qu'il sera, puis la disposition modificative qui en est dérivée, **prouvée par réapplication** |
| Exposé sommaire | 200 à 300 mots, trois temps, chaque chiffre avec sa source entre parenthèses et en note |
| Gage | la formule de compensation applicable au cas, relevée sur pièce et reprise au mot |
| Sortie | l'amendement en `.docx` déposable, contrôle de généralisation joué avant écriture |

### Ne fait pas — et c'est à vous

| ce qui n'est pas outillé | ce que vous faites |
|---|---|
| **La recevabilité financière et le rattachement** | La procédure est écrite — `procedures/test_rattachement.md`, et `procedures/domaine_lfss_LO111-3.md` pour les lois de financement — mais elle se conduit à la main. **Aucun contrôle n'arrêtera un amendement irrecevable.** Une charge nouvelle n'est jamais gageable : si la mesure en crée une, le gage ne la sauve pas, elle se réécrit ou elle tombe. |
| **Les renvois entrants** | Quels articles citent celui que vous modifiez. Le module qui les relevait n'existe pas au dépôt — mesuré le 3 octobre 2026. La règle tient toujours : sur un amendement on signale en fin d'exposé sans coordonner, sur une proposition de loi chaque renvoi se traite avant dépôt. Les deux se font à la main, et **le relevé se déclare incomplet** — une liste vide s'écrit « non relevé », jamais « aucun ». |
| **L'ordre de dépôt et les neutralisations réciproques d'une liasse** | Ce sont des décisions politiques. Deux amendements peuvent se contredire, se vider l'un l'autre, ou gager deux fois la même ligne : la machine ne tranche pas et ne le voit pas. Tenez le compte des lignes employées. |
| **Le droit non codifié hors des textes portés** | L'extrait porte les codes et les textes non codifiés déclarés à `codes.json`. Un siège logé ailleurs n'y est pas. Ces cas se traitent à la main — ou s'ajoutent par une ligne à `codes.json`. |
| **Le rafraîchissement, quand la source officielle ne répond pas** | Claude le tente et vous dit s'il a abouti. Sinon, le repli est l'action programmée du dépôt, tous les 1ers du mois. **Rien n'autorise à rédiger entre-temps.** |

Un piège mérite d'être nommé séparément, parce qu'il est invisible. Un texte
financier déposé en octobre modifie des articles qu'une loi promulguée en décembre
a déjà changés : au millésime courant, l'article porte le **résultat** de la
modification, pas son point de départ. Le droit en vigueur se lit donc à une date
dès que l'article visé a été touché depuis le dépôt du texte. Et la reconstruction
inverse, qui consisterait à défaire la disposition sur le texte actuel, est
fausse : le droit porte l'effet de la loi adoptée, amendements compris, pas celui
de la disposition déposée.

## 6. Le millésime, et comment vous le changez

Le paquet est réglé sur les textes déposés en 2027 : les référentiels livrés
portent les articles que ces textes ouvrent et les relevés qui en sont tirés.

Les modules de lecture, eux, ne sont pas réglés sur un millésime : ils rejouent
n'importe quel texte financier à partir de son PDF. **C'est ce qui distingue cette
machine d'une photo.** Pour l'exercice suivant, donnez à Claude le PDF du texte
déposé et demandez-lui de rejouer les modules de lecture du dossier `appareil/` —
`socle_texte_2027.py`, puis `portes_ouvertes.py`, `index_mesures_2027.py` et
`redaction_2027.py` —, puis de remplacer les fichiers de `referentiels/` par ceux
qu'ils produisent. Les commandes sont dans l'en-tête de chaque module ; vous
n'avez pas à les connaître.

Rejouez ensuite le démarrage et le `mini-lot/` pour vérifier que la chaîne tourne
sur le nouveau millésime.

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

Version `1.2`, 3 octobre 2026. Elle corrige la `1.1` sur quatre points, tous nés
d'une mesure du dépôt qui n'avait pas pu être faite plus tôt :

- **le mode d'emploi s'adresse à quelqu'un qui travaille en tâche Cowork**, et les
  gestes techniques sont ceux de Claude, non les vôtres. La `1.1` vous demandait
  de taper des commandes ; c'était la mauvaise main et le mauvais lieu ;
- **`appareil/installer_droit.py` lit le manifeste réel du dépôt** —
  `data/_manifeste.json`, clé `millesime_legi`, date au format `AAAAMMJJ`. La
  `1.1` cherchait un autre fichier, une autre clé et un autre format : elle
  refusait un dépôt parfaitement sain ;
- **`procedures/depot_droit.md` porte le compte mesuré** — 62 entrées déclarées
  et environ 40 Mo d'extraits — au lieu de « vingt codes, 21 Mo », borne recopiée
  sans vérification ;
- **les renvois entrants sont déclarés non outillés.** Le module qui les relevait
  n'existe pas au dépôt. Une étape documentée qui ne tourne pas est pire qu'une
  étape déclarée manquante.

**Ce qui a été éprouvé avant livraison**, et rien d'autre :

- `installer_droit.py` contre la forme réelle du manifeste : millésime lu, âge
  calculé, péremption vue, marqueur posé puis effacé, date absurde refusée,
  manifeste muet refusé — sans qu'aucun chemin ne substitue la date du jour ;
- le contrôle de généralisation passe son jeu de fautes et son jeu de justes ;
- les treize pièces de `procedures/`, ce mode d'emploi et le `mini-lot/` passent
  ce contrôle, sans fuite ;
- le rendu `.docx` rejoué sur le `mini-lot/`.

**Ce qui n'a pas été éprouvé**, et que vous êtes donc le premier à faire :

- l'épreuve à froid — personne n'a encore installé cette chaîne à partir du seul
  présent document. Si une étape vous arrête, c'est un défaut du paquet, pas une
  erreur de votre part : signalez-la ;
- le clonage contre le dépôt réel. La sortie réseau de l'atelier où ce paquet a
  été monté ne l'autorisait pas. Le lecteur de millésime, lui, a été éprouvé
  contre la forme exacte du manifeste mesurée au dépôt ;
- la chaîne de bout en bout sur les trois natures d'amendement (abrogation,
  crédits à l'état B, jambe en loi de financement) depuis ce paquet seul.

## 9. Les trous connus

Déclarés plutôt que tus.

**Les renvois entrants ne sont pas outillés** — voir la section 5. C'est le trou
le plus lourd après la recevabilité.

**Le rendu `.docx` ne porte pas les notes de bas de page.** `python-docx` n'écrit
pas de note ; les appels de note et leur texte sont rendus en fin de pièce, en
petit corps. Si votre dépôt exige de vraies notes, reprenez-les dans un traitement
de texte avant envoi — c'est une minute par pièce.

**Les deux fichiers de rédaction exacte ne sont pas joints.**
`referentiels/redaction_plf.json` et `referentiels/redaction_plfss.json` sont trop
volumineux pour voyager. Ils sont reproductibles : `appareil/redaction_2027.py`
les régénère à partir du PDF du texte déposé, comme en section 6.

**Onze extraits du dépôt ne sont déclarés nulle part**, dont quatre codes. Le
lecteur les refuse en disant « code inconnu ». Si un article que vous cherchez
tombe dans ce cas, il n'est pas introuvable : il est non déclaré, et une ligne
dans `codes.json` le rend lisible.

**Une asymétrie de nommage, qui n'est pas un trou mais qui trompe.** Le relevé
mécanique des portes — les couples (texte, article) que le véhicule modifie
lui-même — s'appelle `articles_ouverts_<véhicule><année>.tsv`, parce que c'est le
nom que `appareil/portes_ouvertes.py` écrit. **Il existe pour les deux
véhicules** : `referentiels/articles_ouverts_plf2027.tsv`, 421 adresses sur 62
textes, et `referentiels/articles_ouverts_plfss2027.tsv`, 153 adresses sur 22
textes. Chacun porte en tête l'empreinte `sha256` de la pièce dont il est tiré.

`referentiels/portes_ouvertes_plf2027.tsv` est **autre chose** et ne se confond
pas avec eux : six colonnes au lieu de huit, pas d'empreinte de pièce, et une
colonne `confiance` qui porte `à vérifier` sur toutes ses lignes. C'est un relevé
antérieur, de grammaire différente, conservé pour mémoire. **Le relevé qui fait
foi est le mécanique**, celui qui porte l'empreinte.
