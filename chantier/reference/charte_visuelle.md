# Charte visuelle Résolution — document de référence

*Relevé le 20260930 sur `site/fiche.css`, dépôt `resolution-ib-dev/Site-ETNP`,
désormais synchronisé au projet. **Ce document fait foi** pour tout fil qui
produit un visuel : il évite de reconstituer la charte de mémoire ou au pixel.
Les valeurs sont celles du CSS en production, sauf la palette des graphiques,
qui est une couche arrêtée par l'auteur le 20260925 et ne figure pas au CSS.*

---

## 1. Trois langues visuelles, elles ne se mélangent pas

| langue | où | fond | typo | usage |
|---|---|---|---|---|
| **la garde** (`.a-fond`) | accueil | brique `#b23a10` | Archivo condensé 900 | elle annonce |
| **le manifeste** (`.g-page`) | manifeste | brique strié | Archivo condensé | il proclame |
| **la fiche** (`.page`, `.s-page`, `.m-page`) | tout le reste | papier `#fdfcfa` | Archivo + Source Serif 4 | elle démontre |

Règle héritée (A-200, A-213) : *la garde annonce, la fiche démontre.* On ne
mélange pas les deux dans un même écran.

Règle héritée (A-218) : **la charte de la couverture donne la palette et la
typographie, pas les corps ni les graisses.** Une affiche et une page de lecture
n'ont pas la même échelle.

---

## 2. Les variables, telles qu'elles sont au CSS

### Bloc `:root` — la fiche

```
--enc   #1a1a1a   encre, texte courant
--pap   #fdfcfa   papier
--creme #f6f2ea
--fil   #ddd7cd   filets et séparateurs
--gain  #1f5c3a   vert profond — voir § écarts
--perte #8a2f22   brique sombre
--ocre  #6b5b3e   intertitres, petites capitales
--gris  #6d6a64   texte secondaire
--rose  #fbeae7   fond des cartes « perte »
--sable #f7f3e8   survol
--nuit  #16150f   fond de page hors colonne
```

### Bloc `.a-fond` / `.g-page` — la garde et le manifeste

```
--briq  #b23a10   brique
--briqc #b84923   brique claire, rayure du strié
--dor   #ffd24a   or
--crm   #fffdf2   crème
--voile rgba(178,58,16,.74)   voile sur photo
```

### Filets

- **Fiche** : filet tricolore en dégradé, `linear-gradient(90deg, #000091, #fff 50%, #e1000f)`, hauteur 3 px.
- **Manifeste** : trois segments d'or décroissants — `#ffd24a` plein (flex 1), crème à 50 % (flex .45), crème à 22 % (flex .2), hauteur 4 px.
- **Strié du manifeste** : `repeating-linear-gradient(90deg, #b84923 0 2px, transparent 2px 22px)`.

---

## 3. Typographie

```
--titre  Archivo, 'Helvetica Neue', Arial, sans-serif
--texte  'Source Serif 4', 'Source Serif Pro', Georgia, serif
--chif   Archivo  (identique à --titre : tous les chiffres sont en Archivo)
```

Archivo est chargée en **variable** : `wdth 62..125, wght 400..900`.

**Réglages arrêtés :**

| élément | réglage |
|---|---|
| titres de garde, manifeste, fiche, carte | `wdth 66, wght 700 à 900`, capitales, `letter-spacing −.008em` |
| promesse de garde | `wdth 84, wght 800` |
| affirmation du manifeste | `wdth 94, wght 700` |
| petites capitales (intertitres, bandes, labels) | Archivo 700, `letter-spacing .14em à .28em`, capitales |
| texte courant | Source Serif 4, `16.5px / 1.52` |
| chiffres | Archivo 700, `font-variant-numeric: tabular-nums`, `word-spacing −.06em` |

Substituts hors Archivo : `Archivo Narrow`, `Arial Narrow`, Arial. Hors Source
Serif 4 : Georgia.

---

## 4. Règles de composition arrêtées

- **Colonne** : 40 rem (fiche, sommaire), 44 rem (texte suivi), 46 rem (manifeste).
- **L'or sur le brique ne dépasse pas 3:1 de contraste** : il tient pour un filet, un chiffre ou une vedette, **jamais pour du texte suivi**. Les intertitres sur brique passent en crème, l'or reste au filet qui les souligne. (A-213)
- **Aucune transparence sur le fond strié** : elle laisse un voile gris illisible. L'appui se distingue de l'affirmation par le **poids**, pas par l'opacité. (A-215)
- **Le gras ne reste que sur l'affirmation**, qui est ce qui doit ressortir.
- **Trois appels, arrêtés** : *J'adhère au manifeste* en crème plein · *Je m'exprime* en or filaire · *Précommander le livre* en or plein. (A-219)
- **À l'impression** : le fond brique et l'or sont **conservés** sur le manifeste (`print-color-adjust: exact`) ; les pages de fiche passent au blanc.

---

## 5. Palette des graphiques — couche arrêtée le 20260925

**Elle ne figure pas au CSS.** Arrêtée par l'auteur, elle s'applique à toute
dataviz, infographie et visuel de présentation.

| rôle | valeurs |
|---|---|
| orange du mouvement, clair → foncé | `#f2c4ac` · `#e1865c` · `#d2490a` · `#b03c07` |
| bleu, clair → foncé | `#a8c4d8` · `#6d96b5` · `#2f5d87` |
| violet | `#8a6f93` |
| gris neutre | `#6d6a64` |

**Grammaire — la couleur porte du sens, elle ne décore pas :**

- **orange** = ce qui est discuté, cessible, restituable, hors du périmètre essentiel ; l'intensité monte avec la portée de la mesure
- **bleu** = ce qui est conservé
- **violet** = sécurité sociale et santé, ni l'un ni l'autre : les mettre en orange laissait croire qu'elles étaient facultatives
- **gris** = charge de la dette seulement, qui n'est pas une politique publique
- une couleur porteuse de sens (rouge, brique) ne se pose **jamais** sur une grandeur qui n'a pas ce sens

**Le vert est proscrit** des graphiques et visuels du projet.

### Règles de rendu

- **Chiffres** : deux significatifs, trois au besoin ; une décimale seulement sous 10. 392, 231, 49, 13 — mais 8,9 et 3,5.
- Chaque montant porte son **unité et son signe** : − ce qui s'arrête, + ce qui revient.
- **Quatre corps fixes**, jamais calculés sur la largeur d'écran. L'agrégat ne dépasse jamais son libellé de plus du double. Pas de capitales dans les tuiles. Aucun mot coupé.
- **Filets** : trait plein 3 px autour d'un groupe, tirets de 20 px espacés de 12 à l'intérieur, même blanc. C'est l'épaisseur qui dit le niveau, jamais le style. Aucun titre ne chevauche un filet.
- **Hachures** : 7 % d'opacité, 2 px tous les 15 — visibles seulement en les cherchant.
- **Échelles** : jamais tronquées, toujours ancrées à zéro.
- **Marges** : réduites au minimum, pour que les graphiques soient hauts et les écarts vertigineux.
- **Source en pied de chaque pièce**, chaque chiffre traçable à sa cellule.
- Un titre est au moins aussi grand que le chiffre qu'il porte ; jamais un chiffre isolé de sa légende.

### Formes retenues

treemap pour les répartitions · grille (un carré = une unité) pour les
comptages · aires empilées pour les évolutions · pyramide centrée pour la
représentativité · colonnes pour les comparaisons entre pays · chaîne
rapetissante pour les cascades.

---

## 6. Écarts relevés au 20260930 — à trancher

1. **Le vert est en production.** `--gain: #1f5c3a` est un vert profond, porté par toutes les valeurs de gain de la galerie (18 fiches), les bandes, les listes. L'auteur a proscrit le vert des graphiques le 20260925. Les deux décisions coexistent sans avoir été confrontées. **Arbitrage ouvert : on aligne le site sur la proscription, ou on borne la proscription aux seuls graphiques.**

2. **Le relevé au pixel du 20260924 était faux sur la brique.** Il donnait `#8C3315` ; le CSS porte `#b23a10`. L'or (`#ffd24a`) et la crème (`#fffdf2`) étaient exacts. Toute pièce produite entre le 20260924 et le 20260930 sur la foi du relevé porte une brique fausse et est à reprendre.

3. **L'orange du mouvement n'est pas au CSS.** `#d2490a` (graphiques) et `#b23a10` (site) sont deux oranges différents, proches mais distincts. Ils cohabitent sans règle écrite. **Arbitrage ouvert.**

---

## 7. Comment ce document se maintient

`Site-ETNP` est synchronisé au projet depuis le 20260930 — `site/fiche.css`,
`README.md`, `CLAUDE.md` ; le dossier `site/` complet est exclu (limite de
taille). Toute modification du CSS au dépôt se propage à la synchro ; ce
document, lui, ne se met pas à jour tout seul : **il se relève à nouveau à
chaque changement de charte au dépôt.**
