# Relevé d’écarts — épreuve EP2 contre le manuscrit

*Fil long de relecture comparée, clos le 20260908.*

Épreuve `9782366026481_EP2_PDF.pdf`, 180 pages, composée le 04/09/2026, contre
`manuscrit/manuscrit.html` restauré du coffre par copie d’octets — empreinte
`5ec342cb…e38f32`, 224 422 octets, 868 lignes, identique au relevé, et prouvé
de l’extérieur : `extraire_notes.py` rejoué dessus redonne
`referentiels/notes_manuscrit.json` à l’octet.

**Le détail vit dans `livrables/releve_epreuve_EP2.tsv`** — un écart par ligne :
page d’épreuve, flux, classe, motif, ancienneté, ancre au manuscrit, et les deux
versions. Ce document-ci n’en donne que le compte et le contrôle des chiffres.

Rien n’a été corrigé, rien n’a été réécrit, aucun écart de fond n’a été tranché.

## Le compte par classe

| classe | nombre | dont apparus entre EP1 et EP2 |
|---|---|---|
| fond | 297 | 245 |
| perte | 171 | 148 |
| coquille | 390 | 179 |
| forme | 134 | — |

**858 écarts détaillés**, plus 134 comptés en forme.
Sur les 858 détaillés, **572 sont apparus
entre la première épreuve et celle-ci** ; 286 étaient déjà là.
La première épreuve ne divergeait du manuscrit que par 374 écarts : la refonte
rédactionnelle s’est jouée entre les deux épreuves, pas avant.

### Le fond, par motif

- **chiffre** — 47
- **nom propre** — 70
- **rédaction** — 180

### La perte, par motif

- **texte absent** — 161
- **note ajoutée** — 5
- **note retirée** — 5

Dont **21 phrases entières que l’épreuve ajoute** et que le manuscrit
ne porte pas, et **18 passages du manuscrit que l’épreuve ne porte plus**
(seuils : dix mots).

### La coquille, par motif

- **orthographe ou casse** — 234
- **ponctuation** — 105
- **appel de note** — 39
- **appel de note déplacé** — 12

### Les notes

141 au manuscrit, 141 à l’épreuve, mais ce n’est pas la même liste :
**5 notes ajoutées** (n° 40, 74, 110, 118, 135 à l’épreuve),
**5 notes retirées** (n° 72, 97, 115, 136, 137 au manuscrit),
et **78 notes renumérotées** par contrecoup.
L’appariement des notes ne s’est pas fait par numéro — il aurait été faux dès la
quarantième — mais par alignement global de leurs textes.

## Contrôle arithmétique des valeurs relevées

*Repris le 20260908 après relevé de l'auteur : la première version posait deux
identités qui n'existent pas au corpus, et déclarait faux deux comptes justes.
Les deux contrôles fautifs sont retirés, et le seul endroit où l'arithmétique
bloque réellement est nommé.*

Les identités du corpus, rejouées sur les valeurs telles que l'épreuve les
imprime.

| contrôle | obtenu | attendu | verdict |
|---|---|---|---|
| aide de l'enfant = moitié de l'aide fondamentale — `D9-4-1-p1` | 275 | 550 / 2 = 275 | juste |
| net par euro gagné = 1 − taux unique — `D9-3-1-e1` | 77 centimes | 100 − 23 = 77 | juste |
| restitution mensuelle rapportée au salaire médian, p. 89 et note 99 | 300 / 2 190 = 13,7 % | 13 % annoncés | juste |
| économies rapportées à la dépense publique, p. 33 et p. 88 | 236 / 1 714 = 13,8 % | 14 % annoncés | juste |
| patrimoine cédé rapporté au patrimoine public, p. 106 | 600 / 4 500 = 13,3 % | 13 % annoncés | juste |
| capital par foyer × 30 millions de foyers — `D7-2-1-p1` | 20 000 × 30 M = 600 Md€ | 600 Md€ | juste |
| restitution totale = feuille de paie + compte épargne, p. 89 et p. 90 | 300 + 300 = 600 | 600 €/mois | juste |
| montée de la restitution, p. 141 : latence de six mois, puis +2 points par mois | 6 à 7 × 2 = 12 à 14 points | 13 % au bout d'un an | juste |
| **pension de base = socle contributif + aide fondamentale — `D9-2-3-p2`, posé par la note 124 de l'épreuve elle-même** | **socle 1 100 + aide 550 = 1 650** | **1 100 €/mois** | **faux** |

### Le seul endroit où l'arithmétique bloque : p. 105

Le manuscrit écrit « un socle contributif par répartition **avec une pension de
base** égale à 1 100 euros par mois ». L'épreuve écrit « un socle contributif par
répartition **égale** à 1 100 euros par mois ». Le membre de phrase retiré était
le référent du nombre : dans le manuscrit, 1 100 est la **pension de base**, donc
le socle vaut 550 et se complète des 550 de l'aide fondamentale ; dans l'épreuve,
1 100 est le **socle seul**.

**La note 124 de l'épreuve est inchangée** et pose l'identité en toutes lettres :
« le socle contributif forme **avec l'aide fondamentale** une pension de retraite
de base ». Le corps de l'épreuve et sa propre note ne disent donc plus la même
chose, et l'écart vaut **550 euros par mois et par retraité**.

*Deux traces de la coupe, sur la même ligne* : l'accord au féminin — « un socle
contributif … égale » — n'a de sens que devant « pension de base », et l'aide
fondamentale disparaît du dispositif de retraite alors qu'elle est versée à tous
les citoyens (p. 113).

*Cet écart est au relevé détaillé, p. 105, en classe `fond`, motif `rédaction`.*
Le contrôle des chiffres ne l'avait pas vu : il comparait 1 100 au bon nombre
sans voir que le référent du nombre avait changé. **Un chiffre inchangé dont la
définition bouge est un écart de chiffre**, et c'est la leçon de la reprise.

### Ce que la première version disait à tort

**« Le compte éducation devrait valoir douze fois l'aide de l'enfant. »** Faux :
l'épreuve écrit p. 123 « **en plus de** l'aide fondamentale universelle de 275
euros par mois, versons à chaque enfant 6 600 euros par an ». Les deux se
cumulent. Le 6 600 est estimé sur le coût public réel de l'éducation (note 133),
et le `550 × 12` du contrôle du corpus se rapporte à l'aide fondamentale de
l'adulte, non à celle de l'enfant.

**« +2 % par mois pendant douze mois font 24 points. »** Faux : l'épreuve pose
p. 141 une latence — « **au bout de six mois**, les premières économies seront
constatées et rendues » — puis la montée. Six à sept mois à +2 points encadrent
les 13 % annoncés au bout d'un an.

### Les valeurs telles que l'épreuve les imprime

| grandeur | page | épreuve | manuscrit |
|---|---|---|---|
| economies annee pleine Md | 88 | 236 | 236 |
| part des depenses publiques pct | 88 | 14 | 14 |
| restitution mensuelle euro | 88 | 600 | 600 |
| hausse salaire net pct | 89 | 13 | 13 |
| hausse mensuelle par mois pct | 141 | 2 | 2 |
| salaire type gain euro | 89 | 300 | 300 |
| smic gain euro | 89 | 180 | 180 |
| aide fondamentale euro | 113 | 550 | 550 |
| aide enfant euro | 115 | 275 | 275 |
| compte education annuel euro | 123 | 6 600 | 6 600 |
| pension socle euro | 105 | 1 100 | 1 100 |
| taux unique ir pct | 114 | 23 | 23 |
| net par euro centimes | 114 | 77 | 77 |
| capital par foyer euro | 106 | 20 000 | 20 000 |
| patrimoine a ceder Md | 106 | 600 | 600 |
| patrimoine public total Md | 106 | 4 500 | 4 500 |
| part patrimoine cede pct | 106 | 13 | 13 |
| taux prelevements cible pct | 99 | 36 | 36 |
| postes fermes | 78 | 580 000 | 580 000 |
| baisse effectifs pct | 78 | 10 | 10 |
| restitution annee 1 | 142 | 236 milliards d’euros d’économie ⚠ | la moitié des économies |

**Une seule grandeur diffère entre le manuscrit et l'épreuve** : la part des
économies acquise à la fin de la première année, p. 142 — « la moitié des
économies » devient « 236 milliards d'euros d'économie », deux paragraphes avant
que la même page écrive « la seconde moitié des économies ».

`make controle` du corpus passe par ailleurs à zéro échec sur ses 23 consignes.

## Ce qui ne se verse pas

Les épreuves elles-mêmes, binaires, ne sont pas au coffre. Le TSV du relevé et ce
compte le sont, et eux seuls. Deux écarts sont déclarés **non décidables sur le
texte extrait** — une césure de composition que l’extraction recolle sans son
tiret ; ils se vérifient à l’œil sur l’épreuve, p. 40 et p. 147.
