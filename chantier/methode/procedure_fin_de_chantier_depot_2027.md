# Procédure — de la revue au dépôt, millésime 2027

**Porteur** : fil de revue du dépôt 2027. **Mandat** : l'auteure, 20261006 — « proposer une
procédure précise, complète et robuste ; ces errements ne doivent plus se reproduire » ; reprise
du 20261007 par le fil d'application des corrections, puis **par le fil de consolidation du
20261007, qui porte la règle R-G à l'étape 3**. **Domicile** :
`methode/procedure_fin_de_chantier_depot_2027.md`. **Mesure** : 7 étapes, 2 digestions faites,
10 lots de revue restants, 2 invariants nouveaux, **5 règles d'application (R-C à R-G)**.

---

## 0. La faute à ne plus commettre, et le verrou qui l'empêche

**Ce qui s'est passé le 20261006.** Une checklist de validation existait —
`redaction-legistique/references/regles_redactionnelles.md` — et n'a pas été ouverte avant de
rédiger. Quatre corrections de l'auteure sur la clause générale et sur l'aide fondamentale sont
des lignes de cette checklist : rédaction positive, pas de redondance entre niveaux, une phrase
une norme, aucun chiffre inventé. Le fil reconstituait de mémoire une règle qu'il avait sur
disque.

**Le verrou est un cinquième invariant d'en-tête, et rien d'autre.** Les quatre invariants
existants — porteur, mandat, domicile, mesure — sont déjà tenus et contrôlés. Il s'y ajoute :

> **Appui** : les références ouvertes avant la passe, nommées et datées.

**Une passe de rédaction dont la ligne `Appui` est vide n'est pas une passe valide**, et son
produit ne se verse pas.

**Ce que chaque type de passe doit avoir ouvert se lit à `methode/appui_des_passes.md`**, qui
porte la table « type de passe → appui dû », et nulle part ailleurs. L'invariant dit qu'il faut
nommer ce qu'on a ouvert ; cette table dit ce qu'il fallait ouvrir. Pour une passe de rédaction
normative, l'appui minimal reste `regles_redactionnelles.md` (checklist) +
`reference/guide_legistique.md`, parties I à IV + le texte en vigueur relevé à l'extrait.

**Et le contrôle de sortie reprend la checklist ligne à ligne**, comme il reprend déjà les
adresses : chaque ligne reçoit un verdict, aucune ne reste sans verdict. Un écart se signale avec
sa correction proposée ; aucune correction silencieuse.

---

## 0 bis. Le faux blocage, et les deux règles qui le ferment

**Ce qui s'est passé le 20261006, au fil de digestion 1.B.** Le fil a cherché la LOLF sur
Légifrance, a reçu les `403` attendus, a ouvert le dépôt de droit, a listé son contenu **avec
une sortie tronquée aux quarante premières lignes**, n'y a pas vu la loi organique, et a conclu
que le droit était introuvable. Il l'avait sur disque : le dépôt porte la LOLF, 73 articles, à
l'adresse `loi_org2001_692`, millésime `20261001`. La digestion a été annoncée impossible et
elle ne l'était pas.

**La même faute s'est reproduite le 20261007**, sur six pièces et un état : « la loi organique
n'est pas versée au dépôt de droit » y laissait huit références hors contrôle. Le croisement l'a
relevée, la reprise du 20261007 bis l'a corrigée — LOLF, articles 19, 21, 34 et 47, tous
`VIGUEUR`. **Une faute que la procédure nomme peut se reproduire : elle ne disparaît que par le
contrôle, non par l'écriture de la règle.**

**Deux règles, et elles ne se contournent pas.**

### R-A — Le droit se relève au dépôt de droit, et il ne se cherche nulle part ailleurs

Légifrance refuse la lecture depuis l'atelier : le constat est ancien, il est écrit dans le
`README` du dépôt de droit, et il ne se rejoue pas à chaque fil. La base LEGI de la DILA est
elle aussi fermée au mandataire de l'atelier. **Le canal du chantier vers le droit est
`droit/droit.py`, et il est le seul.**

L'ordre est fixe, et il tient en trois gestes :

```bash
git clone --depth 1 https://github.com/resolution-ib-dev/Resolution-2027 droit
python3 droit/droit.py etat                      # millésime et fraîcheur
python3 droit/droit.py article <court> <numéro>   # le verbatim, son identifiant, sa version
```

Le clonage est **public et sans jeton** — aucune déclaration de source n'est requise pour lire.
Un fil qui annonce ne pas pouvoir atteindre le droit sans avoir joué ces trois lignes rend un
constat faux.

**Un texte réputé absent du dépôt se vérifie sur `codes.json`, jamais sur une impression.**
`codes.json` est la liste close des textes couverts ; `data/_manifeste.json` dit ce que
l'extraction en a tiré. Si le texte y figure et que `droit.py` ne le rend pas, c'est l'extraction
qui est en cause et cela s'inscrit. S'il n'y figure pas, l'ajout d'une entrée à `codes.json` est
le seul geste correct — et il est de la tambouille, il se tranche sans être posé.

*Cette règle vaut aussi contre `legifrance_retrieval.md`, qui donne encore `web_fetch` sur
Légifrance comme méthode principale. Pour ce chantier, le dépôt de droit passe avant, et
Légifrance n'est plus une méthode mais un cas d'échec connu.*

### R-B — Une mesure ne se prend jamais sur une sortie tronquée

Une liste coupée par `head`, une table rendue partiellement, un extrait limité en pages : aucun
de ces objets ne fonde un constat d'absence. **Un constat d'absence se prend sur un compte, non
sur un affichage** — `len()`, `wc -l`, une recherche nominative sur la clé cherchée, jamais un
coup d'œil sur les premières lignes.

Et la conséquence tient en une phrase : **on ne déclare absent que ce qu'on a cherché par son
nom.** Le mandat du projet veut qu'un fil s'arrête quand la mesure sort vide ; cette règle dit
ce qui compte comme mesure.

---

## 1. Digestions — faites, et ce qui reste à poser

Une référence externe entre au corpus par sa digestion, jamais par son fichier (classement, R5).
Les deux digestions dues sont faites. Ce qui reste n'est plus une digestion : c'est le versement
des originaux et la déclaration à l'appareil, l'un et l'autre au dépôt.

**1.A — Guide de légistique. FAITE les 20261006 et 20261007.** La digestion couvre la
proposition de loi et les commentaires d'articles (fiche 3.1.1), la frontière loi/règlement
(1.3.2), les formules de renvoi au décret (3.5.1, et non 3.3.1 — voir le fragment d'arbitrage du
20261006), la langue du texte (3.3.1), les modifications et insertions (3.4.1), les renvois au
droit positif (3.4.2), l'entrée en vigueur, les situations en cours et les abrogations (3.8.1 à
3.8.3), le domaine des lois de finances (1.3.4) et des lois de financement de la sécurité sociale
(1.3.5), et l'institution d'un prélèvement fiscal obligatoire (5.7).

Sortie : **`reference/guide_legistique.md`**, pièce unique depuis le 20261007, qui absorbe et
remplace `reference/structure_ppl.md`, `reference/regles_redaction_guide.md` et
`reference/domaine_lois_financieres.md`, supprimées. Elle porte en annexe la table des fiches du
guide et de leurs pages : une fiche non digérée se lit sans rouvrir le sommaire.

**1.B — Règles budgétaires, pour la seconde partie. FAITE le 20261006.** Objet : les
amendements de crédits et l'état B. Digérés : LOLF, articles 5, 7, 8, 11, 12, 15, 34, 42, 43, 44
et 47 — dont la règle de compensation entre programmes d'une même mission —, et la nomenclature
mission / programme / action / titre. Sortie : `reference/regles_credits.md`, sur laquelle
résout le renvoi `guide_budgetaire`. **Cette pièce ne fusionne avec aucune autre** : elle porte
du verbatim relevé au dépôt de droit, et R8 l'interdit.

> **Reste ouvert sur 1.B** : le recueil des règles de comptabilité budgétaire de l'État n'a pas
> été récupéré — budget.gouv.fr rend 403 sur la page comme sur le PDF. La digestion n'en dépend
> pas : la règle d'amendement est organique. À reprendre si un lot touche l'exécution des
> crédits, et par une pièce jointe de l'auteure.

**Quatre corrections du corpus** sont relevées en tête de `reference/guide_legistique.md` et
n'ont pas été appliquées aux pièces : la formule de réécriture d'un article de loi est « est
ainsi rédigé », non « est remplacé par les dispositions suivantes » ; « abroger » vaut pour un
texte et ses divisions numérotées, « supprimer » pour ce qui est à l'intérieur ; les dates
communes d'entrée en vigueur sont quatre et non deux ; la règle de virgule devant une conjonction
a un symétrique. Elles se reprennent à l'étape 3, par lot validé.

**Régime commun des digestions** : fil Cowork court, un par digestion, qui récupère, digère en md
avec autorités citées, verse au projet. Aucun PDF ni docx au projet. Le fil ne rédige aucune
pièce.

**Où vit l'original.** La règle de format ferme le projet aux PDF, elle ne ferme pas le dépôt :
rien n'y est lu tant qu'on ne le demande pas. **L'original de chaque guide se verse au dépôt,
sous `sources/`, daté par le millésime de la source, et tel quel — sans zip** : un PDF est déjà
compressé, et un zip interdit la lecture page à page. Noms arrêtés :
`guide_legistique_SGG_4e_edition_20260312.pdf` et `guide_budgetaire_DB_2023.pdf`. La chaîne
devient : le renvoi résout sur la digestion, la digestion cite ses autorités, l'autorité se
vérifie sur l'original au dépôt.

**Les originaux sont versés, et l'appareil est déclaré. FAIT le 20261007.** Les deux PDF sont au
dépôt au commit `a142a66`, sous `chantier/sources/guide_legistique_2026.pdf` et
`chantier/sources/guide-public-du-budgetaire-2023.pdf` — le premier prouvé identique à l'octet à
la pièce jointe, empreinte `d10720ad…`. Les déclarations d'appareil sont posées, les neuf pièces
neuves restaurées, `reference/structure_ppl.md` supprimé avec ses trois déclarations, et
`guide_public_budgetaire` sorti des manquants. `make controle` compte 150 anomalies bloquantes
contre 153 avant, avec I4 et I5 à zéro.

**Versé à `main` le 20261007, commit `0f1d138`.** Contrôlé sur un clone neuf, et `make controle`
rejoué : 150 anomalies bloquantes, I4 et I5 à zéro, 14 manquants déclarés.

> **Lecture et écriture ne se mesurent pas ensemble.** Le dépôt se **lit** sans rien déclarer :
> il est public. Il ne s'**écrit** que si la session le porte dans son jeu de dépôts autorisés
> en écriture — sans quoi le mandataire refuse d'injecter une accréditation et le `push` rend
> `403`. C'est le seul blocage réel constaté les 20261006 sur 1.A et 1.B, et il est à la main de
> l'auteure. **Un fil ne confond pas les deux** : il ne renonce jamais à lire le droit au motif
> qu'il ne peut pas écrire au dépôt.

---

## 2. Lots de revue restants — l'auteure arbitre, le fil inscrit

Dix lots, dans l'ordre du document de ping-pong, qui va du plus structurant au plus fin :

| | lot | véhicule |
|---|---|---|
| 10 | Aides fondues dans l'aide fondamentale | PLFSS |
| 11 | Compte d'épargne personnel | PLF |
| 12 | Collectivités | PLF |
| 13 | Aides ciblées et aide au logement | PLF et PLFSS |
| 14 | Structures, agents, associations | PLF et PLFSS |
| 15 | État B | PLF, seconde partie |
| 16 | Bouclier sanitaire | PLFSS |
| 17 | Répartition | PLFSS |
| 18 | Arrêts immédiats et principes budgétaires | PLF et PLFSS |
| 19 | Abrogations du code général des impôts | PLF |

**Règle de lot** : un lot se pose en trois à cinq questions fermées, chacune avec son défaut ;
ce qui relève de la tambouille se tranche et s'inscrit sans être posé ; toute contradiction entre
documents se signale et se tranche dans le lot. Un état par lot ou par groupe de lots, qui porte
les cinq invariants.

**Le lot 15 est ouvert** : la digestion 1.B qui le bloquait est faite.

**Deux points arrêtés par l'auteure le 20261006, et ils commandent les lots 14 et 15.**
Une suppression d'opérateur est un cavalier budgétaire : la création, les missions,
l'organisation et le fonctionnement d'un organisme extérieur à l'État ne s'écrivent pas dans un
véhicule financier. **Ce qui s'y porte est l'extinction des crédits, assortie d'un dispositif
d'extinction ordonnée** ; la suppression de l'organisme lui-même est une jambe de loi ordinaire.
Et le basculement des taxes affectées en première partie du PLF est déjà porté par l'adossement
des pièces au texte déposé du PLF 2027 : pas de reprise générale due, contrôle au cas par cas à
la passe d'application.

**Un arbitrage ne se relit pas, une rédaction si.** Les réponses de l'auteure sont définitives dès
qu'elles sont rendues, et les digestions n'y changent rien. En revanche, toute **rédaction clef**
produite dans un lot avant la digestion 1.A est provisoire : elle se marque `rédaction provisoire,
passe checklist due` à l'état du lot, et la passe de l'étape 3 la reprend. Le marquage est la
garantie ; la mémoire n'en est pas une.

---

## 3. Application aux pièces — par lot validé, jamais à la réponse

**La règle de versement est la copie, pas la recopie.** Une pièce absente de l'atelier ne se
réécrit pas de mémoire : ses divisions corrigées se rendent en clair à l'état du lot, et
s'appliquent par copie d'octets au fil qui détient la pièce. C'est déjà le régime de M-025.

Ordre d'application : dispositif, puis entrée en vigueur, puis gage, puis bloc interne. L'exposé
ne bouge pas à ce stade.

### R-C — L'application commence par une mesure du paquet, et cette mesure périme vite

**Ce qui s'est passé le 20261007.** Une mesure du paquet prise à 14 h 19 a conclu que les pièces
des lots 14 à 19 n'existaient ni au coffre ni au dépôt, et a déclaré l'application arrêtée. Le
versement du paquet est intervenu douze minutes plus tard. Le fil suivant a rouvert sur un constat
faux.

**Règle.** Un fil d'application **rejoue la mesure du paquet à son ouverture**, et il ne reprend
jamais celle d'un fil antérieur, fût-elle du même jour. La mesure se prend sur un compte —
règle R-B — et elle porte, par lieu, le nombre de pièces présentes. **Une mesure de paquet n'a
pas de durée de validité au-delà du fil qui l'a prise.**

### R-D — Un état de lot ne fait pas foi contre une reprise postérieure

**Ce qui s'est passé.** L'état du lot 5 porte « corridor 20 % – 28 %, par décret ». La reprise du
20261007 a supprimé le corridor et mis le taux en dur à 27 %, et la pièce 4.5 porte la reprise.
L'état du lot, lui, porte toujours l'arbitrage mort, sans le dire.

**Règle.** Un arbitrage s'applique **à sa date**. Avant d'appliquer une ligne d'état de lot,
l'application la confronte à la dernière reprise qui touche le même objet ; la plus récente
l'emporte, et **l'état dépassé se marque sur place**. Un état de lot est une trace, non une
autorité : l'autorité est la dernière décision rendue.

### R-E — Une pièce longue ne se réécrit pas parce qu'elle est à portée

La règle de la copie valait pour une pièce **absente**. Elle vaut aussi pour une pièce
**présente** qui porte de longues énumérations — listes nominatives d'articles, tableaux de
sièges, tableaux de verdicts : le risque est la déformation à la recopie, non l'accès. Ses
divisions corrigées se rendent en clair, division par division, avec le fondement de chaque
correction, et s'appliquent par copie d'octets. Le critère se juge pièce par pièce, et il se
déclare.

**Et une correction de date se rend en deux temps** : la division d'entrée en vigueur réécrite,
puis la liste nominative des autres endroits de la pièce où la date se reporte — cartouche,
tableaux du bloc interne, exposé, collisions. Une date corrigée au seul dispositif laisse une
pièce qui se contredit.

### R-F — Un fil d'application ne tranche pas un conflit d'arbitrage

Deux arbitrages inconciliables du même rang se constatent, s'inscrivent au § « conflits » de
l'état, et se posent en question fermée. Le fil applique ce qui n'en dépend pas et laisse le
reste. **Il ne choisit pas la valeur la plus récente quand les deux sont du même jour**, et il ne
déduit pas un arbitrage d'un autre.

### R-G — Un fil ouvre les états des fils frères du même jour, avant sa passe

> **Un fil ouvre les états des fils qui ont tourné sur la même matière le même jour, avant sa
> passe, et les nomme à son `Appui`.** La table « type de passe → appui dû » de
> `methode/appui_des_passes.md` ne les connaît pas : le parallélisme les crée après qu'elle a été
> écrite. **Un fil qui déclare une pièce non jouée sans avoir ouvert ces états rend un constat
> faux.**

**Ce qui s'est passé le 20261007, deux fois.** La chaîne est passée de séquentielle à parallèle :
six fils d'application ont tourné le même après-midi sans se connaître.

1. **Le fil fiscal a déclaré dix pièces bloquées.** Cinq avaient leurs divisions corrigées rendues
   en clair dans un état écrit deux heures plus tôt, qu'il n'a pas ouvert. Sa seconde passe, cet
   état ouvert, a écrit cinq pièces et n'a laissé qu'un seul point bloqué.
2. **Le fil de croisement a rendu vingt-trois anomalies sans ouvrir ni le CR de consolidation ni
   l'état d'application des corrections.** Il a donc mesuré les pièces sans les cinq divisions
   rendues en clair : quatre de ses constats sont faux ou incomplets, dont celui des dates
   d'abrogation de deux articles, où l'anomalie réelle est plus lourde que celle qu'il décrit.

**Comment le fil sait quels sont ses frères.** Il relève les états du jour portant sa matière,
sous `methode/etats/`, et le dernier état de passation en vigueur, qui les nomme tous. **Un état
postérieur à sa propre ligne de lancement compte aussi** : la ligne est écrite avant que le fil
frère ait fini.

**Le critère est la matière, non la date seule.** Un fil n'ouvre pas tout ce qui a été écrit dans
la journée ; il ouvre ce qui touche sa matière. **Et il inscrit à son `Appui` ceux qu'il a
ouverts, nommément.**

---

## 4. Croisements — une seule passe, après le dernier lot

Rien ne sert de croiser avant que tous les paramètres soient arrêtés. La passe contrôle, sur
l'ensemble de la liasse :

- **dates** : toute date d'entrée en vigueur est un 1er janvier ou un 1er juillet, sauf exception
  inscrite à `livrables/registre_exceptions_dates.md` ; deux pièces liées portent la même date ;
  **une pièce LFSS de dépense qui vise le 1er janvier porte sa propre date** — les dispositions de
  la troisième partie d'une LFSS n'entrent pas en vigueur au 1er janvier mais le lendemain de la
  publication ;
- **gages** : un euro n'appartient qu'à un circuit ; aucune niche nommée ne gage une pièce du
  circuit B ; chaque pièce qui perd une recette porte sa clause ; **aucun amendement de crédits
  ne porte de gage** — le gage compense une perte de recettes, jamais une charge ;
- **crédits** : tout amendement de crédits tient les six invariants de `reference/regles_credits.md`
  — une mission, un tableau AE et CP, somme des majorations égale aux minorations à l'euro, une
  ligne par programme, aucun abondement du titre 2 depuis un autre titre, motivation portée ;
- **autonomie des jambes** : chaque amendement est complet et se suffit, même si un autre
  amendement de la liasse atteint le même objet ; une taxe affectée va à zéro quand bien même la
  taxe est supprimée ailleurs ;
- **porteur unique d'une abrogation** : chaque article abrogé a exactement un porteur, inscrit au
  registre des colonnes — contrepartie de la forme fondue retenue au lot 19 ;
- **renvois** : aucun renvoi mort, aucun renvoi à une division supprimée ou renumérotée ;
- **registre des colonnes** : un rang par pièce, aucun doublon, aucun rang orphelin ;
- **suivi mensuel** : toute ligne du suivi par agent est datée ; le bouclage est nul à chaque
  mois.

**La passe de croisement est soumise à R-G comme toute autre** : elle ouvre les états
d'application du jour **et** le dernier état de passation, faute de quoi elle mesure des pièces
dont les corrections sont rendues mais non appliquées, et rend des constats à reprendre.

---

## 5. Exposés — après les croisements, jamais avant

Un exposé se régénère en bloc, il ne se patche pas. **Les écarts exposé / dispositif se tiennent à
`methode/registre_exposes_depot_2027.md`**, où toute passe qui modifie un dispositif sans toucher
l'exposé ouvre une ligne dans la même passe. Règles tenues : 200 à 300 mots, trois temps, aucun
déposant nommé, aucun nom de référentiel interne, aucune nomenclature du corpus, deux chiffres de
preuve au plus. **On valorise le caractère graduel et ordonné ; on ne fait état d'aucun excédent
de trésorerie ; on ne nomme aucun perdant.** La mise en regard des taxes supprimées est
optionnelle, légère, et seulement quand elle sert.

---

## 6. Contrôles de sortie — mécaniques, et annoncés veut dire joués

Quatre contrôles, dans cet ordre, sur la liasse complète :

1. **Adresses** : toute référence passée au dépôt de droit au millésime du dépôt ; rien
   d'`ABSENT` ni d'`ABROGE` ne sort ; le compte et les verdicts vont à l'état. **Le millésime se
   lit à `droit.py etat` et s'inscrit à l'état du lot** : un contrôle d'adresses qui ne dit pas
   sur quel millésime il a été joué ne vaut pas. **Et un contrôle rend aussi le compte des
   références laissées hors contrôle, avec la raison de chacune.**
2. **Checklist rédactionnelle** : ligne à ligne, un verdict par ligne.
3. **Rattachement** : joué pièce par pièce, verdict et porte citée. **Le crible est la motivation
   type des cavaliers budgétaires et le critère de l'effet suffisamment direct pour les cavaliers
   sociaux**, l'un et l'autre en partie V de `reference/guide_legistique.md`.
4. **Contestabilité** : jouée sur la liasse, objections classées, non traitées ici.

Un contrôle annoncé est un contrôle joué. Une inspection à l'œil présentée comme une vérification
est une faute. **Et un constat d'absence pris sur une sortie tronquée n'est pas un contrôle**
(règle R-B).

---

## 7. Dépôt

Accroches relevées sur le texte déposé, ordre de la liasse arrêté par l'auteure, rangs de dépôt
inscrits au registre des colonnes. Export docx seulement sur go explicite, et seulement sur un
texte validé en clair.

---

## Ce qui bloque quoi

```
1.A digestion légistique ── FAITE ──┐
                                    ├──> 3 application ──> 4 croisements ──> 5 exposés ──> 6 contrôles ──> 7 dépôt
2 lots 10 à 19 ─────────────────────┘
1.B digestion budgétaire ── FAITE ──> lot 15 ouvert ──┘
```

Les deux digestions étant faites, les originaux versés, l'appareil déclaré et le tout poussé sur
`main`, **plus rien ne bloque l'ouverture d'un lot ni l'écriture d'une correction**. Le paquet du
20261005 est versé au projet depuis le 20261007 : **l'étape 3 est ouverte sur les 32 pièces du
paquet**, et seules deux pièces du registre restent à leur adresse antérieure.

**Et une règle de répartition des fils en sort, qui n'était écrite nulle part.** Un fil Claude
Code ne voit pas le coffre : `restaurer.py` travaille sur le transcript d'une session qui l'a lu,
et un fil code n'en lit jamais. **Une pièce du projet se prépare donc toujours en Cowork**, puis
se remet au fil code **en pièce jointe, zip unique avec son manifeste sha256** : le fil déplie,
contrôle les empreintes, branche, fusionne et pousse seul. Au fil code reviennent l'édition de
l'appareil, les `make`, le relevé des empreintes — qui exige un clone du dépôt de droit en
`droit/` — les branches et la poussée. **L'auteure ne touche ni à git ni au navigateur.**
