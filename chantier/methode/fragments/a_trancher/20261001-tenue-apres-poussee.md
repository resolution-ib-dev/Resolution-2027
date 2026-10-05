### Déclarer le dépôt aux sources du projet — c'est le seul vrai blocage

La poussée de l'archive du coffre a été refusée :
`resolution-ib-dev/Resolution-2027` n'est pas aux sources autorisées de la
session, et le mandataire git rend un 403. Remesuré deux fois le 20261001 :
l'outil `add_repo` que le proxy réclame n'existe pas dans une session Cowork
rattachée à un projet de chat, et le proxy n'expose aucun point d'entrée pour
l'ajouter. Ce n'est pas un réglage manquant, c'est une voie fermée pour ce type
de session.

Conséquence mesurée : **l'archive remise à l'auteure le 20261001 est le seul
exemplaire durable du coffre** tant qu'elle n'est pas déposée au dépôt.

Deux voies, et l'auteure tranche :

1. **Téléverser l'archive au dépôt par le navigateur** — `Add file` puis
   `Upload files` sur GitHub, branche neuve —, puis une session `claude.ai/code`
   la déplie sous `chantier/` et pousse. Aucun terminal.
2. **Attendre** que les projets Claude Code soient déployés sur le compte, qui
   portent un sélecteur de dépôt et les droits de poussée.

Tant que l'une des deux n'a pas abouti, **aucune sortie nouvelle du projet ne se
joue**.

### Le sort de `methode/journal.md` — RÉSOLU le 20261001

Sorti du projet le 20261001 sur une présence au dépôt supposée, et introuvable
par la mesure. **Retrouvé et remis le jour même par l'auteure**, identique à
l'octet : sha256
`faad6e948ae0fffe007c3a1f15b7da53954ebb623059b7c47a4684a787a5de1e`, 295 275 o,
4 875 lignes — les trois concordent avec l'empreinte du 20260930.

Le journal courant porte ce contenu verbatim en tête, jamais repassé par le
modèle, suivi des dix sections qui n'avaient plus de fragment, puis de la ligne
de marque et des treize fragments assemblés. 340 155 o, 104 sections, zéro
perdue, rejeu inchangé.

**Cette question est fermée.** Ce qui reste, c'est la règle qui l'a ouverte, et
elle est corrigée au socle.

### Deux pièces d'appareil dues

- **`a_trancher` comme cible de `appareil/fragments.py`.** Le registre reçoit
  des fragments — cinq au coffre — qu'aucun assemblage ne reverse. Soit la
  cible s'ajoute, soit le dépôt de fragments `a_trancher` cesse.
- **Un contrôle d'assemblage non destructeur** : compter les sections avant et
  après, refuser d'écrire s'il en perd une. La règle est au socle depuis le
  20261001 ; elle n'est pas encore outillée. Elle aurait suffi à voir les onze
  sections d'arbitrages et les dix du journal.

Les deux s'écrivent au dépôt, par un paquet, et attendent la même ouverture de
voie que la poussée de l'archive.

### Le binaire de `input/Note_Retraite_20250619.docx`

Le coffre le rend en texte, pas en octets. L'archive porte le rendu texte sous
`.docx.txt`. Le `.docx` lui-même est à redéposer si on y tient.

### Nouvelle dette de table curée

Les documents déposés au coffre après l'écriture du paquet du 20261001 ne sont
pas déclarés : les fragments et livrables des fils de lecture des textes 2027,
le registre des sorties et les fragments de ce fil. Mesure à refaire avant
d'écrire le paquet suivant.
