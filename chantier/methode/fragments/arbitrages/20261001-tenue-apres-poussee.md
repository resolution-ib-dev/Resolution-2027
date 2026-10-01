### Un assemblage se compte en sections, pas en octets

Assembler `arbitrages.md` en l'état perdait onze sections pour un rétrécissement
de 9 863 o seulement. Aucun contrôle de taille n'aurait vu la faute.

Tranché en propre : **un assemblage se joue d'abord sur une copie jetable, et
la mesure porte sur le compte des sections avant et après.** Un assemblage qui
en perd une ne se verse pas.

### Une section sans fragment se reprend au-dessus de la marque

Plutôt que d'inventer des fragments pour onze sections dont les originaux
n'existent plus — ce qui aurait fait passer du verbatim par le modèle et aurait
donné un nom de fil à deux sections qui n'en ont jamais eu —, les onze sections
ont été découpées à l'octet de la queue et replacées dans la tête, sous un
avertissement daté.

Tranché en propre : **la tête d'un cumulatif est le lieu de ce qu'aucun
fragment ne reproduit.** Un assemblage ne la touche pas, donc elle ne se reperd
pas. Résultat mesuré : 79 sections, 0 perdue, rejeu inchangé.

### Un journal perdu se rebâtit avec son constat de perte en tête

`methode/journal.md` est introuvable. Repartir d'un fichier vide aurait effacé
la perte elle-même : dans six mois, rien n'aurait dit que 4 875 lignes
manquaient.

Tranché en propre : **la tête du journal rebâti porte le constat, l'empreinte du
document disparu et la consigne de remise.** Une copie retrouvée se reconnaît à
son sha256 et se remet au-dessus de la marque sans rien réécrire de ce qui suit.

### La restauration hors table curée ne sert qu'à mesurer

Trois fragments d'arbitrages du 20261001 sortent `hors index` de
`appareil/restaurer.py`. Ils ont été restaurés par copie d'octets en appelant
`restaurer.moisson()` directement, sans écrire de module neuf.

Tranché en propre : cette voie mesure, elle ne verse pas. La dette de
déclaration qu'elle révèle s'inscrit plutôt que de se contourner.

### L'archive d'un coffre se prouve par relecture, pas par écriture

L'archive remise porte son propre manifeste — sha256, taille et chemin des 172
documents — et elle a été décompressée ailleurs puis recomparée ligne à ligne
avant d'être rendue.

Tranché en propre : **une archive n'est archivée qu'une fois relue.** 172
conformes, 0 divergent, 0 absent.

### Un délestage s'inscrit avant d'être joué

Le registre des sorties a été écrit, avec les quinze empreintes, **avant** la
première suppression.

Tranché en propre : l'ordre n'est pas cosmétique. Si la session meurt au milieu,
le registre dit déjà ce qui devait partir et où le retrouver.

### Le scratch d'atelier n'est pas de l'appareil

La moisson du transcript a eu besoin d'une variante qui relève aussi les
documents rendus comme fichier, ce que `restaurer.py` ne fait pas. Elle a été
écrite au scratchpad de session, pas sous `appareil/`.

Tranché en propre : un outil d'une seule session vit au scratchpad, ne se verse
pas, ne se pousse pas, et ne crée donc aucune dette de paquet.
