# Arbitrage — la place au projet, les portes du PLFSS, la remontée collectivités

2 octobre 2026, fin de journée.

## 1. Le problème de place, et sa solution structurelle

**Mesure** : la base du projet était à 1 942 558 sur 2 000 000 — 97 % pleine. Un
versement de référentiel a été refusé dans la journée pour cette raison, et le
problème revient à chaque session.

**La cause** : des référentiels volumineux sont versés au projet alors qu'ils sont
soit **reproductibles par script**, soit **déjà au dépôt de droit**. Le projet sert
à ce qu'un fil retrouve une décision et une procédure ; il n'est pas un entrepôt de
données.

**La règle, à tenir** :

- **Ne va au projet** que ce qu'un fil doit *lire* pour décider : méthode,
  arbitrages avec leur raisonnement, passations, livrables rédigés, pièces de
  procédure.
- **Ne va pas au projet** : tout fichier reproductible par un module de l'appareil
  à partir d'une pièce qui fait foi, et tout fichier déjà porté par le dépôt
  `resolution-ib-dev/Resolution-2027`. Ces fichiers vivent au dépôt, dont la taille
  n'est pas bornée, et un fil code les y lit.
- Quand un fil a besoin d'un tel fichier, il le **régénère** ou le **lit au dépôt**.
  Il ne le cherche pas au projet.

**Nettoyage fait** : cinq référentiels `cgi_expert_*` supprimés du projet —
`articles`, `insertions`, `suppressions`, `articles_bouges`,
`parametres_etat_anterieur`. Le fil CGI du 2 octobre les a relevés **byte-conform
au dépôt**. `cgi_expert_parametres.tsv` est conservé au projet : c'est le seul dont
la copie au dépôt divergeait.

## 2. Les portes du PLFSS existent déjà

**Le défaut était de déclaration, pas de production.**
`referentiels/articles_ouverts_plfss2027.tsv` porte l'en-tête, le schéma de
colonnes et l'empreinte de pièce que `portes_ouvertes.py` écrit — même empreinte
que celle relevée sur le PDF du PLFSS par le fil de lecture du 1er octobre. 153
adresses, 22 textes.

**Décision** : le fichier est versé au paquet sous son nom attendu
`portes_ouvertes_plfss2027.tsv`, et le §9 du mode d'emploi est corrigé. Il n'est
pas rejoué depuis le PDF : il est octet pour octet la sortie du module, rejouer ne
changerait que la date du relevé. Le site du budget est refusé par la politique de
sortie réseau, et on ne contourne pas.

**Ce que ça apprend** : avant de déclarer une pièce manquante, chercher si elle
existe **sous un autre nom** — par son empreinte et son schéma de colonnes, pas par
son nom de fichier.

## 3. La remontée des économies sur les collectivités

**Décision : la taxe sur la valeur ajoutée en priorité.** La dotation reste
possible selon les cas ; elle n'est pas écartée, elle est le second choix.

## 4. Une nomenclature interne ne sort jamais vers l'auteur

Les identifiants de mesures et de blocs (M-0xx, B-0xx, et les numéros de mesure de
l'index) sont des repères d'atelier. Une question posée à l'auteur les désigne par
leur objet en clair, jamais par leur numéro. Un arbitrage posé en nomenclature
interne est un arbitrage mal posé, et il ne peut pas être tranché.
