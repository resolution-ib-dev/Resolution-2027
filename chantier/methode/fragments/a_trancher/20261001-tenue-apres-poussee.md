### Déclarer le dépôt aux sources du projet — c'est le seul vrai blocage

La poussée de l'archive du coffre a été refusée :
`resolution-ib-dev/Resolution-2027` n'est pas aux sources autorisées de la
session, et le mandataire git rend un 403.

Conséquence mesurée : **l'archive remise à l'auteure le 20261001 est le seul
exemplaire durable du coffre.** Elle ne se rejoue pas toute seule ; un fil
futur ne peut pas la retrouver sans qu'on la lui redonne.

Tant que le dépôt n'est pas déclaré aux sources, **aucune sortie nouvelle du
projet ne se joue**, et la règle de délestage reste suspendue.

Un geste, aux paramètres du projet : ajouter `Resolution-2027` comme source,
avec les droits d'écriture. Le fil suivant pousse l'archive et la règle
redevient applicable.

### Le sort de `methode/journal.md`

Perdu. Rebâti le 20261001 avec une tête qui porte le constat et l'empreinte du
document disparu — sha256
`faad6e948ae0fffe007c3a1f15b7da53954ebb623059b7c47a4684a787a5de1e`, 295 275 o,
4 875 lignes.

Une seule piste reste : **le transcript de la session claude.ai du 20261001 qui
l'a sorti du projet.** Si cette conversation est encore ouverte, un fil Cowork
lancé depuis elle verra le document dans son propre transcript et pourra le
restaurer par copie d'octets. C'est à l'auteure de dire si cette session existe
encore.

Passé ce point, l'historique antérieur au 20261001 ne survit que par les
fragments encore au coffre et par `methode/arbitrages.md`.

### Deux pièces d'appareil dues

- **`a_trancher` comme cible de `appareil/fragments.py`.** Le registre reçoit
  des fragments — cinq au coffre — qu'aucun assemblage ne reverse. Soit la
  cible s'ajoute, soit le dépôt de fragments `a_trancher` cesse.
- **Un contrôle d'assemblage non destructeur** : compter les sections avant et
  après, refuser d'écrire s'il en perd une. La règle est au socle depuis le
  20261001 ; elle n'est pas encore outillée.

Les deux s'écrivent au dépôt, par un paquet, et attendent la même déclaration
de source que la poussée de l'archive.

### Le binaire de `input/Note_Retraite_20250619.docx`

Le coffre le rend en texte, pas en octets. L'archive porte le rendu texte sous
`.docx.txt`. Le `.docx` lui-même n'existe plus qu'entre les mains de l'auteure,
s'il existe encore. À redéposer si on y tient.

### Nouvelle dette de table curée

Les documents déposés au coffre après l'écriture du paquet du 20261001 ne sont
pas déclarés : trois fragments d'arbitrages (`lecture-plf2027`,
`lecture-plfss-2027`, `plan-vehicule`), leurs fragments de journal et de
a_trancher, les livrables de lecture des textes 2027, et les trois fragments et
le registre des sorties écrits par ce fil. Mesure à refaire avant d'écrire le
paquet suivant.
