# Prompt — fil « courroies »

*Fil Cowork. Il ne pousse rien : il mesure l'état réel des courroies entre le
coffre et le dépôt, et il rend **un seul** paquet de dépôt, autonome, qu'une
session `claude.ai/code` applique sans rien avoir à demander.*

**Pourquoi il existe.** Les fragments s'empilent au coffre sans entrer au journal
ni au registre, les paquets de dépôt s'accumulent sans être appliqués, et
personne ne tient le compte de ce qui est dû. Chacun de ces retards est inoffensif
seul et ruineux ensemble : le jour où un `make index` se joue, ce qui n'est pas
déclaré disparaît.

## Ligne de lancement

> Fil Cowork — courroies. Socle : `methode/socle_prompt_fil.md`. Activer `methode/prompt_fil_courroies.md`, `methode/carte_des_chantiers.md`, `methode/a_trancher.md`, `methode/index.json`, et les paquets de dépôt que les deux premiers nomment. Mandat : mesurer l'état réel des trois courroies — fragments non assemblés, table curée de l'index, modules dus au dépôt — et rendre un **paquet de dépôt unique et autonome** pour une seule session `claude.ai/code`, portant verbatim tout ce que cette session ne peut pas lire. Aucun fond, aucun livrable neuf, aucune question de doctrine.

## La contrainte qui commande tout

**Une session `claude.ai/code` sur `Resolution-2027` ne voit pas le coffre.** Ni
les documents du projet, ni les registres, ni les fragments. Elle voit le dépôt,
et le dépôt seul.

Donc : **tout ce que le paquet demande doit y être écrit verbatim.** Un paquet
qui renvoie à un chemin du coffre est un paquet raté, et il coûte un aller-retour
à l'auteure. C'est la règle de conduite A — un prompt est autonome dans le
contexte de sa cible — appliquée au cas où elle mord le plus.

## Trois mesures, et chacune commence par une mesure de présence

**Chaque lot ci-dessous se saute et le fil continue** si sa pièce manque. Aucun
lot absent n'arrête le fil entier.

**1. Les fragments non assemblés.** Lister les fragments présents sous
`methode/fragments/{journal,arbitrages,a_trancher}/`, et les confronter à ce que
`methode/journal.md`, `methode/arbitrages.md` et `methode/a_trancher.md` portent
déjà. Le delta est ce qui attend `appareil/fragments.py`. *Mesurer, ne pas
déclarer : le nombre connu d'un CR est une trace datée, pas un état.*

**2. La table curée de l'index.** Confronter trois listes — ce que
`appareil/generer_index.py` rend, ce que `methode/index.json` porte, et les
documents que le projet porte réellement. Deux deltas. **Le produit attendu
n'est pas un compte : c'est la liste des déclarations à ajouter, écrite
verbatim, prête à être collée dans la table curée.** Un compte seul oblige la
session de code à redécouvrir ce qu'elle ne peut pas voir.

**3. Les modules dus au dépôt.** Relever les paquets de dépôt existants et ce
qu'ils portent encore ; mesurer lesquels sont déjà au dépôt. *Un état mesuré le
20260924 dit que la dette au dépôt était alors nulle, et un autre mesuré le
20260930 dit que le générateur avait décroché : ce sont deux objets différents et
aucun des deux ne vaut état courant. On remesure.*

## Ce que le fil rend

**Un paquet unique**, `methode/paquet_depot_courroies_<AAAAMMJJ>.md`, qui porte,
dans l'ordre d'application et avec un point d'arrêt déclaré à chaque étape :

- le contenu verbatim de chaque fichier à écrire ou à corriger au dépôt ;
- la liste verbatim des déclarations à porter à la table curée ;
- **l'interdiction formelle de jouer `make index` ou `make reindex` avant que
  cette liste soit appliquée**, et le compte attendu avant et après, pour que
  l'écart se vérifie au lieu de se supposer ;
- l'ordre des commandes, et pour chacune ce qui vaut échec et impose l'arrêt ;
- une poussée d'essai sur modification nulle **en tout premier geste** : si le
  mandataire git rend un `403`, le dépôt n'est pas déclaré aux sources de la
  session, et la session s'arrête là plutôt que de travailler pour rien.

Les paquets antérieurs qu'il absorbe sont nommés et déclarés absorbés ; ils ne se
suppriment pas dans le même fil.

## Ce que le fil ne fait pas

Il ne réécrit aucun module de mémoire — deux modules sont déclarés perdus, et un
module réécrit au jugé sous le nom d'un module perdu est pire que son absence :
il les constate et les compte. Il ne corrige aucun chiffre qui ne soit pas déjà
arbitré. Il ne touche à aucun livrable.
