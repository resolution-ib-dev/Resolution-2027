# 00 — COMMENCER ICI

**Assistant : lisez cette page, puis `01_DEMARRER.md`, puis exécutez. Ne
demandez rien à l'utilisateur avant d'avoir joué le contrôle 0.**

**Et à la fin, écrivez la pièce d'amorçage au projet** — § « Ce que vous laissez
derrière vous » de `01_DEMARRER.md`. Une installation qui ne survit pas au fil
oblige à redonner ce jeu dans le suivant, et c'est le défaut qu'elle existe pour
éviter.

---

Ce jeu de fichiers est une **machine à amendements**. Elle produit des
amendements déposables au projet de loi de finances et au projet de loi de
financement de la sécurité sociale, exportés en `.docx`.

## À l'utilisateur, en trois lignes

Donnez ces fichiers à votre assistant et dites-lui **« installe »**. Il saura.

Puis donnez-lui votre mesure en français ordinaire : *« supprimer le taux réduit
de TVA sur tel service »*, *« plafonner telle taxe affectée »*. Il vous rend
l'amendement, puis son `.docx`.

Plus tard : **« mets à jour la machine »**.

## Où ça marche

**Il faut un assistant qui dispose d'un terminal** — Claude dans Cowork ou Claude
Code. C'est là que la machine donne tout : le texte de loi en vigueur au
caractère près, les contrôles, et le `.docx` déposable.

**Dans un projet Claude ordinaire, sans terminal, elle ne s'installe pas.**
L'assistant pourra lire la méthode et raisonner sur votre mesure, mais pas
relever le droit ni produire le fichier à déposer — c'est-à-dire pas les deux
choses qui rendent un amendement déposable. `01_DEMARRER.md` décrit une voie de
repli pour ce cas, et elle est honnête sur ce qu'elle ne donne pas.

## Ce que la machine ne fera pas à votre place

**Décider de la mesure** — elle porte une méthode, pas une opinion.
**Chiffrer** — un montant se relève à l'annexe de l'exercice, et c'est vous qui
le relevez. **Plaider la recevabilité** — elle instruit le dossier, vous
décidez ; un amendement peut être parfait et irrecevable. **Déposer** — cela se
fait sur l'extranet de l'assemblée.

## Elle vous parlera cinq fois au plus, jamais pour vous bloquer

Le véhicule si votre énoncé ne le dit pas · votre avis sur la recevabilité ·
l'arbitrage entre deux articles possibles · la ressource qui gage la mesure ·
l'ordre de dépôt. **Si vous ne répondez pas, elle continue** en portant son
incertitude en clair.

Elle s'arrête vraiment une seule fois : quand une étape ne sait pas conclure.
Elle dit laquelle, et elle ne devine pas.

## Les outils sont à vous

Les pièces `10` à `20` sont les outils que l'assistant consulte à chaque étape.
**Lisez-les, modifiez-les** : ce sont des documents, pas une boîte noire. La mise
à jour vous dira lesquels vous avez changés et ne les écrasera pas.

Les pièces `02` à `07` sont la méthode : si vous les changez, les contrôles le
signalent comme une anomalie, et c'est voulu.

---

## Assistant : les réflexes par défaut, que l'utilisateur n'a pas à énoncer

**Aucun prélèvement nouveau, aucune hausse de prélèvement.** La chaîne ne crée
pas de taxe et n'en majore aucune, y compris pour gager une perte. La seule
exception est la formule standard de recevabilité, État seulement, dont le
caractère postiche s'explique à l'exposé — `05_PROCEDURE_gage.md` § 2 bis et
2 ter.

**L'utilisateur peut lever ce réflexe**, en clair et au dossier. Lui seul.
Sans sa ligne, la chaîne ne l'écrit pas.

**Une formule qui n'est pas arbitrée ne s'invente pas.** Elle se relève sur une
pièce réelle, ou la chaîne déclare l'insuffisance en nommant le perdant.

## Assistant : une mesure en une ligne se produit en entier

**Quand l'utilisateur donne une mesure, vous produisez l'amendement complet —
cartouche, dispositif, entrée en vigueur, gage, exposé sommaire, `.docx` — sans
lui poser de question et sans lui rendre un plan.** S'il n'y a pas
d'installation dans l'atelier, vous l'installez d'abord, en silence.

Les cinq moments où la chaîne parlerait sont à sa main et **aucun n'est
bloquant** : sans réponse, elle tranche et le déclare en clair dans la pièce
(§ 4 de `02_PROCEDURE_conduite.md`). Un seul arrêt est réel, `hors_capacite` :
une étape qui ne sait pas conclure. Vous dites laquelle, et vous ne devinez pas.

**Une chaîne qui s'arrête pour demander un arbitrage est une chaîne mal jouée.**

## Assistant : la suite, exactement

```
python3 68_CONTROLE_atelier.py
```

Il rend une **voie**, `A` ou `B`. Allez au paragraphe correspondant de
`01_DEMARRER.md` et jouez ses gestes dans l'ordre. **Si vous ne pouvez pas
exécuter cette ligne, vous êtes en voie B** : allez-y directement.
