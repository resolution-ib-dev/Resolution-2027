# Contrôle avant transmission d'un paquet de machine

*Posé le 20261001, après qu'une transmission antérieure a sorti deux versions
buggées. La règle n'est pas « faire attention » : c'est une procédure à trois
passes, et aucune version ne part sans les trois.*

**Un paquet transmis est irrattrapable.** Il part chez un tiers, il n'a pas de
canal de correction, et une faute s'y découvre à l'usage, trop tard. C'est la
seule pièce du corpus dans ce cas.

---

## Passe 1 — reproduction depuis le dépôt nu

**Ce qu'elle éprouve :** que le paquet produit bien ce qu'on dit qu'il produit,
et depuis rien d'autre que lui-même.

Un clone nu du dépôt, les deux PDF des textes déposés, aucune autre pièce. On
rejoue les **cinq modules** du millésime — `socle_texte_2027.py`,
`pieces_nommees.py`, `portes_ouvertes.py`, `index_mesures_2027.py`,
`redaction_2027.py` — dans l'ordre du mode d'emploi, et on compare, **à
l'octet**, les **six référentiels** obtenus — `articles_ouverts`,
`releves_transversaux` et `redaction`, chacun pour le PLF et pour le PLFSS — à
ceux que le paquet porte ou déclare. *Corrigé le 20261003 : le document était
calibré sur quatre modules et quatre référentiels.*

**Les deux PDF se reconnaissent à leur empreinte, pas à leur nom** : les textes
enregistrés, au dépôt sous `chantier/sources/` — PLF 2027 n° 3210
`sha256 132274b83bed4861a9e1a147d0d16abda2d729cdad2373ef804e26747c43d881`,
349 pages ; PLFSS 2027 n° 3211
`sha256 47f5fc0d1581c90634449516281070495b92cfe062c20c2a366919622906eab6`,
138 pages. *Recalé le 20261005 (arbitrage de l'auteure) : les tirages `b0b802d3…`
et `71010873…` sont abandonnés.* Un autre tirage du même texte — le numéro de dépôt ajouté, par
exemple — change l'empreinte, que les référentiels portent en tête : la passe
échouerait sur la pièce, non sur la chaîne.

**Les deux référentiels de rédaction ne voyagent pas** — trop volumineux. Le
paquet en porte l'empreinte attendue, et la passe 1 les régénère et compare
l'empreinte.

**Un octet de divergence vaut échec et arrête la transmission.** Il dit qu'une
pièce du paquet n'est pas celle qui a servi, ou qu'un module dépend de quelque
chose qui n'y est pas.

## Passe 2 — confrontation à la pièce qui fait foi

**Ce qu'elle éprouve :** que les chiffres sont justes, non que la chaîne tourne.

Chaque référentiel se confronte à la pièce du corpus qui fait foi, **texte par
texte et compte par compte**, et l'écart se chiffre. Un écart n'interdit pas la
transmission : il s'écrit au mode d'emploi, avec sa cause. Ce qui interdit la
transmission, c'est un écart non mesuré.

*Les écarts connus au 20261001 : 449 sièges relevés côté PLF contre 424 au relevé
qui fait foi — énumérations captées en plus, et 31 adresses que ce relevé déclare
lui-même à vérifier. L'attribution de pièce porte le défaut du millésime 2026 sur
quelques adresses du code de la sécurité sociale.*

## Passe 3 — l'épreuve à froid

**Ce qu'elle éprouve :** que le paquet se suffit. C'est la seule passe qui
attrape la faute qui a coûté cher — la procédure d'installation manquante.

Un fil vierge, qui n'a rien vu de la fabrication, reçoit le paquet et **le seul
mode d'emploi**. Il joue le mini-lot. Tout ce qu'il doit demander, deviner ou
chercher ailleurs est un **défaut du paquet**, jamais du fil, et se corrige au
paquet.

**Le fil d'épreuve ne corrige rien lui-même** : il bute et il déclare. Un fil qui
répare en route masque le défaut qu'il devait révéler.

---

## Ce qui part, et sous quel nom

Une version transmise porte un numéro et la date de ses trois passes, écrits au
mode d'emploi. Sans eux, on ne saura pas laquelle est chez qui — et c'est ainsi
que deux versions buggées ont circulé.

**Aucune reprise ne se transmet sans rejouer les trois passes.** Une correction
d'un caractère est une version neuve : elle repasse l'ensemble. Une passe
partielle « parce qu'on n'a touché qu'à ça » est la faute d'origine.
