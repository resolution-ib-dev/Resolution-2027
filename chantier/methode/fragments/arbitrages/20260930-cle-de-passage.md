## 20260930 — Clé de passage du schéma aux prélèvements

**A — Trois étapes, une affectation.** L'appariement se joue dans l'ordre libellé,
puis ligne d'agrégat, puis non atteint ; un prélèvement rejoint au plus une ligne
du schéma. Le contrôle est mécanique : 420 lignes à la table, 420 libellés
distincts.

**B — Les treize sous-lignes sont des lignes d'agrégat à part entière.** Un
prélèvement rejoint la sous-ligne, jamais la ligne mère, quand une sous-ligne le
reçoit. L'absence de valeur à la colonne de suppression vaut maintien, et cette
lecture se déclare au relevé sans être appliquée.

**C — Un motif de contrepartie invoquée n'a pas de réceptacle.** Redevance pour
service rendu, redevance domaniale, redevance de contrôle, rémunération pour
service rendu, redevance sur produits de santé : le schéma ne porte aucune ligne
pour ces prélèvements. Ils sortent en « non atteint » avec leur cause, et ne se
rattachent pas de force à « Autres taxes sur les ménages ».

**D — Une seule variante de code de siège est résolue.** `cgct` vaut
`code général des collectivités territoriales`, trois lignes. Aucune autre
normalisation n'est nécessaire : 17 codes bruts, 16 après résolution.

**E — La clé vit dans la table, pas dans un générateur.** Le mandat nomme deux
pièces ; l'affectation de chaque prélèvement est portée en colonne de la table de
passage, qui se relit seule. Aucun script n'est versé.
