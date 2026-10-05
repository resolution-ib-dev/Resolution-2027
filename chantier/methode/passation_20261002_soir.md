# Passation du soir — 2 octobre 2026

Complète `methode/passation_20261002.md`, qui reste valable pour tout ce qu'elle
porte. Celle-ci porte la journée et, surtout, **les raisonnements** — pas seulement
les conclusions. C'est le défaut diagnostiqué ce soir : une passation qui ne
transmet que des arbitrages oblige le fil suivant à re-dériver, et il re-dérive
mal.

---

## 1. Ce qui est livré et tient

**La machine exportable, version 1.0.** 35 fichiers, contrôle de sortie à zéro
fuite. Le générateur `.docx` est écrit et éprouvé sur une liasse réelle de douze
amendements. Deux faux positifs du contrôle corrigés, dont un qui bloquait la
formule canonique du gage (« le livre III du code des impositions »).

**La liasse de nuit est arrivée** : douze pièces PLF 2027 première partie, avec
leurs reprises déclarées non intégrées.

**Le fil code a rendu** : code général de la fonction publique rétabli au
référentiel des codes, extrait CGFP livré, 46 sections. Non fait : LFSS 2026 et
rafraîchissement, DILA coupée.

---

## 2. Les trois corrections de la soirée — avec leur raisonnement

### 2.1 Le gage d'une suppression de taxe n'est pas le gage d'une suppression de niche

**Le raisonnement, en entier.** Une suppression de niche rapporte : elle n'a
besoin que d'un affichage politique de ce que le produit devient. Une suppression
de taxe coûte : elle a besoin d'un gage, et ce gage est le point où notre schéma
boucle ou ne boucle pas.

Le gage tabac est un prétexte mort : il compense facialement et ne pointe sur
rien. Il convient quand la pièce est isolée. Il ne convient pas à notre schéma,
parce que notre schéma a, par construction, un instrument de restitution qui est
la contrepartie réelle de la suppression. Le gage doit donc **pointer sur notre
instrument** et s'y solder — même mécanique que le tabac (majoration plafonnée,
constat renvoyé au réglementaire), mais l'instrument gagé est le nôtre, de sorte
que gage et restitution sont la même chose vue des deux bouts.

**Erreur commise et à ne pas refaire** : avoir réduit la clause à la forme tabac
en changeant seulement le nom de l'imposition. La forme riche — renvoi de lien,
plafond, solde constaté — est la bonne ; elle s'ajuste à la marge, elle ne se
rabat pas.

**Ce qui reste à faire, et c'est le mandat d'ouverture du fil suivant** : il n'y a
pas un candidat unique de gage. Il y a une **logique d'organisation des blocs**,
avec des liens irréductibles entre eux — quelles suppressions appellent quel
instrument, lesquelles ne peuvent pas être séparées, lesquelles peuvent partir
seules. Cette carte des liens irréductibles est à identifier et à proposer ;
l'auteur valide. Tant qu'elle n'est pas posée, toute rédaction de gage est une
improvisation au cas par cas, c'est-à-dire exactement ce que le projet refuse.

### 2.2 La TVA n'entre pas dans la clause

Elle relève de la contemporanéité et du parallélisme d'affichage, pas d'un
automatisme de rédaction. La vraie grande restitution passe devant. La recoller
dans la clause de lien était un réflexe, pas un raisonnement.

### 2.3 Une pièce ne préempte pas ce qu'une autre doit porter

Remplir dans un article une case qui appartient à un autre article du plan est la
même faute que ci-dessus : elle anticipe un arbitrage non rendu. L'ordre des blocs
commande ; une pièce n'écrit que ce que son rang lui donne.

---

## 3. La règle des trous de droit

Versée séparément : `methode/fragments/arbitrages/20261002-trous-de-droit-et-mentions-a-verifier.md`.

En deux lignes : un trou n'autorise pas une erreur, il autorise un contournement
— dossier législatif de l'Assemblée, puis celui de la loi modificatrice, puis le
Journal officiel. Et la mention « à vérifier » va **en note, jamais dans le
corps**.

---

## 4. Le défaut de conception du paquet, nommé

**Le clonage du dépôt de droit et son rafraîchissement sont décrits comme des
gestes manuels. Ils doivent être inclus.** Un tiers ne doit pas avoir à savoir
qu'un dépôt existe : il doit lancer la chaîne, et la chaîne s'occupe du droit.

Et le rafraîchissement ne peut pas dépendre de la DILA, qui est coupée plus
souvent qu'elle ne répond. Il faut donc, dans l'ordre : l'extrait embarqué ou
cloné sans intervention ; un repli documenté quand la source officielle ne répond
pas ; et jamais un échec silencieux — un extrait arrêté en amont sous le millésime
du jour est le pire des cas, et le fil code l'a signalé comme possible.

C'est un chantier de paquet, à mener avant la version 1.1.

---

## 5. Ce que la nuit doit être, et pourquoi la proposition faite ce soir était trop pauvre

La proposition faite était : un fil de rebasage, un fil droit, un fil paquet.
C'est une séquence, pas un déploiement. **Or tout l'intérêt du découpage est de
pouvoir tout lancer en même temps et réconcilier ensuite.** C'est la raison pour
laquelle le plan stratégique a été établi, et ne pas s'en servir revient à l'avoir
établi pour rien.

La condition pour déployer large est la carte des liens irréductibles du 2.1 :
sans elle, des fils parallèles produiront des pièces qui se contredisent et la
réconciliation coûtera plus que le parallélisme n'aura gagné. Avec elle, chaque
bloc part dans son fil, et la réconciliation est bornée d'avance.

**Donc : la carte d'abord, courte, puis l'éventail.** Ce n'est pas un report, c'est
la seule façon que le parallélisme tienne.

---

## 6. Le défaut de fond, nommé sans détour

L'auteur le constate à chaque bascule et dans chaque fil : du travail se perd, et
le fil suivant re-dérive ce qui était acquis. La cause n'est pas l'oubli — les
arbitrages sont bien versés. La cause est que **les arbitrages sont versés sans
leur raisonnement**. Un fil qui reçoit « le gage pointe sur notre instrument » sans
recevoir pourquoi le tabac ne convient pas rabat sur le tabac à la première
difficulté. C'est exactement ce qui s'est produit ce soir.

**Contre-mesure, à tenir** : tout arbitrage versé porte le raisonnement qui l'a
produit et l'erreur qu'il corrige. Un arbitrage sans son « pourquoi pas
autrement » est incomplet et se re-dérivera mal.

---

## 7. État au moment de poser

| objet | état |
|---|---|
| Machine exportable v1.0 | livrée |
| Clonage et rafraîchissement inclus | à faire — chantier paquet |
| Portes PLFSS | non produites |
| Trois gestes en tête du mode d'emploi | à faire |
| Carte des liens irréductibles entre blocs | **à produire — mandat d'ouverture** |
| Rebasage des douze pièces | en attente de la carte |
| LFSS 2026 et rafraîchissement du droit | bloqués DILA |
| Rattachement de la mesure 72.24 | à trancher par l'auteur |
| Instrument maison du gage | à trancher par l'auteur, sur la carte |
