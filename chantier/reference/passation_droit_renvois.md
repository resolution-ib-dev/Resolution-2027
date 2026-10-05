# Passation — le dépôt de droit, les renvois entrants, et ce qu'ils changent

Rendu par le fil « dépôt de droit », 20260902. Ce fil ne touche pas `methode/` :
le document est en `reference/`, à ranger par le porte-plume.

---

## 1. Arbitrage de l'auteur — les renvois entrants, 20260902

Modifier un article laisse derrière lui les articles qui le **citent**. Rien ne
les cherchait : `N1` de `vecteur-mesure` refuse de confondre vecteur et
véhicule, `N6` voit deux mesures qui visent la même adresse, **aucun ne voit qui
cite la nôtre.**

**Régime arrêté :**

- **Amendement — service minimum.** On ne coordonne pas, on **signale**. Les
  renvois relevés se listent **en fin d'exposé sommaire**. *Le maquis des renvois
  ne doit pas bloquer la production.*
- **Proposition de loi — la boucle va jusqu'au bout.** Chaque renvoi se traite ou
  se déclare sans objet avant dépôt. Travail lourd, assumé comme tel.

**Outil** : `coordination.py` au dépôt de droit. Il balaie les vingt codes et
rend, pour une adresse, les articles applicables qui la citent, **chacun avec sa
certitude** — `nomme` quand la phrase nomme le code visé, `interne` quand le
citant est dans le même code, `ambigu` pour une citation nue venue d'ailleurs.
La règle de déduction est déclarée, jamais une impression.

    python3 droit/coordination.py cgi 279 --tout

*Mesuré : abroger le CGI 279 touche quatre articles applicables ; abroger
`L. 3262-1` du code du travail en touche neuf, dont cinq au code de l'éducation —
invisibles depuis le code du travail seul.*

**Conséquence sur `expose-sommaire`, déjà enregistrée** : le régime lui crée une
entrée qu'elle ne prévoit pas — la liste des renvois signalés en fin d'exposé.
Passage court à prévoir, par le fil qui la tient.

---

## 2. Ce que le dépôt de droit change pour la chaîne

Voir `reference/depot_droit.md` pour la procédure complète. Trois faits qui
commandent la rédaction :

**L'étape « texte en vigueur » n'est plus un trou.** Vingt codes, 21 Mo,
millésime LEGI du 20260901, clonables sans autorisation :
`git clone https://github.com/resolution-ib-dev/Resolution-2027 droit`.
Légifrance reste injoignable depuis l'atelier — neuf tentatives, huit `403`.

**L'applicabilité se lit aux dates, jamais à l'état.** Le CGI porte **376
articles applicables dont l'abrogation est déjà votée**, le CIBS **282**. Le
lecteur sort l'avertissement de lui-même.

**Trois des vingt-deux amendements du lot visent du droit abrogé au 1er janvier
2027** : `GL-I-31` (CGI 278 bis, 279, 278 sexies), `GL-I-32` (CGI 279),
`GL-I-28` (CGI 1594 F quinquies), plus la ligne PEEC de `GL-I-33` au CIBS
L. 313-1. **Rédiger dans l'absolu reste juste ; c'est le branchement qui devra en
tenir compte** — contrôle de dernier moment, arbitré par l'auteur.

**Le droit non codifié n'est pas au dépôt.** Un siège dans une loi de finances
antérieure ne s'y trouvera pas — l'article 179 de la loi de finances pour 2020
est le cas connu. La voie existe, une ligne dans `codes.json` avec le `LEGITEXT`
du texte non codifié : **non éprouvée.**

---

## 3. Prompt du fil `disposition-cible`

*Écrit par ce fil, à jouer par un autre. Le fil qui l'écrit ne la mesure pas.*

```
Reprends le chantier. Fil de production, contre-PLF : la skill
`disposition-cible`. Deuxième de la chaîne de l'amendement.

Lis methode/index.json, methode/prompt_fil_courant.md, methode/arbitrages.md,
puis reference/depot_droit.md, methode/regles_redactionnelles.md et
reference/structure_ppl.md. Lis aussi les references de `redaction-legistique`
— formules_modificatives.md : son répertoire de formules se réemploie, son
étape 4 non.

Déplie l'archive technique, puis par `appareil/restaurer.py` les documents de
methode/. `make restauration`, arrêt sur un R1. Ni manuscrit, ni classeurs, ni
socle : ce fil ne touche aucun chiffre du chiffrage.

Clone le dépôt de droit, qui est public :
    git clone https://github.com/resolution-ib-dev/Resolution-2027 droit
    python3 droit/droit.py etat
Vingt codes, millésime LEGI du 20260901. C'est la seule source de verbatim :
Légifrance est injoignable depuis l'atelier, et rien ne se supplée de mémoire.

=== CE QUE LA SKILL FAIT — QUATRE BLOCS, PAS UN ===

1. L'OPÉRATION ET SON SIÈGE — abroger, remplacer, compléter, insérer, et à quel
   niveau : article, alinéa, subdivision, membre de phrase. `158-5-a` n'est pas
   une adresse, c'est trois niveaux collés.

2. LA DISPOSITION RÉDIGÉE DANS L'ABSOLU, style SGG. Indépendante du véhicule :
   on rédige la modification du droit, on la branche ensuite. Quatre formes —
   modificative sur un article de code ; sur les alinéas du texte déposé quand
   la variante est `article_ouvert` ; article additionnel non codifié ; crédits
   sur la ligne, mission, programme, catégorie, JAMAIS sur un montant en dur
   (A-244). Le texte en vigueur vient du dépôt, verbatim, avec identifiant et
   date.

3. LES RENVOIS ENTRANTS, par `python3 droit/coordination.py <code> <article>`.
   Amendement : on SIGNALE, on ne coordonne pas — la liste va en fin d'exposé
   sommaire. Proposition de loi : chaque renvoi se traite ou se déclare sans
   objet. Chaque renvoi porte sa certitude — `nomme`, `interne`, `ambigu`.

4. CE QUI RESTE À TRANCHER — le branchement sur le texte déposé, le gage,
   l'entrée en vigueur, le fait générateur, et l'avertissement d'abrogation
   programmée quand le dépôt en porte un. La skill les NOMME, elle ne les
   décide pas.

=== CE QU'ELLE NE FAIT PAS, ET C'EST LE POINT DUR ===
Elle N'AUTOMATISE PAS un travail juridique, elle l'outille. Une skill qui
prétendrait le contraire sortirait des dispositions PLAUSIBLES ET FAUSSES, et
une disposition plausible est plus dangereuse qu'une disposition absente.

Elle ne se juge donc pas sur une égalité de rédaction : deux rédacteurs écrivent
deux textes qui produisent le même effet de droit. Ce qui se compare est la
CORRESPONDANCE — même article visé, même opération, même portée (A-254).

=== CE QUE CE FIL NE FAIT PAS ===
Il N'ÉPROUVE PAS la skill et NE REÇOIT PAS les liasses. Un fil qui écrit une
skill puis la mesure connaît les réponses : c'est ce qui a rendu le rejeu de
`vecteur-mesure` ininterprétable (A-271, A-272). La mesure part en fil vierge.

Il ne touche pas `expose-sommaire`, déjà enregistrée, mais il INSCRIT l'entrée
que le régime des renvois lui crée.

=== RENDU ===
La skill proposée à l'enregistrement, le prompt du fil qui la jugera, et les
entrées de registre en texte.

Non-collision : ne touche ni appareil/vecteurs.py, ni REF_norme, ni methode/,
et ne joue pas `make coffre`.
```

---

## 4. Corrections au prompt « la machine à amendements »

*Le cadrage est juste et se garde. Six points de fait ont bougé le 20260902,
tous vérifiables, et un fil qui partirait du prompt tel quel referait du travail
déjà fait.*

**§3, `vecteur-mesure` — T3 est fait, et son résultat est un résultat nul.**
Le rejeu des 22 cas rend 20 concordances, 90,9 %. **Le chiffre n'est pas
comparable aux 63,6 %** : `methode/prompt_fil_courant.md` nomme huit des
vingt-deux cas — les cinq à vérité-terrain vide et les trois manques avec leur
correction. Les quatorze restants sont exactement ceux que la version précédente
réussissait déjà. **Le rejeu ne mesure pas la correction.** Deux manques
survivent malgré la réponse donnée, et ils tiennent à la même cause : la skill ne
sait pas chercher un siège hors code.

**§3, les comptes de l'exposé — deux mesures divergent.** Le prompt donne médiane
216, plus long 660, 18 dans la fourchette, exemple de référence 240. Recompté sur
les 36 exposés extraits : **médiane 230, plus long 695, 19 dans la fourchette,
14 en dessous, 3 au-dessus**. Les trois comptes de position tombent juste, les
mesures non. **Le gabarit ne déclare pas sa règle de décompte** — appels de note,
notes de bas de page, texte des références. Sur une borne à 200, quatorze mots
comptent. À trancher avant de calibrer quoi que ce soit.
*Fait neuf : les exposés de norme sont plus courts que ceux de crédits — médiane
206 contre 247, 13 sur 24 dans la fourchette contre 6 sur 12.*

**§4.2 R1 — la case n'est plus vide de son entrée principale.** Le prompt ne
mentionne pas le dépôt de droit et s'appuie sur A-234, « le verbatim n'entre que
par pièce jointe ». Ce n'est plus la seule voie. `disposition-cible` doit cloner
le dépôt.

**§4 — les renvois entrants manquent.** Voir §1 ci-dessus : quatrième bloc de
sortie pour `disposition-cible`, entrée nouvelle pour `expose-sommaire`.

**§7, pièces à joindre — les deux sont déjà là.** La liasse PLFSS a été jouée le
20260902 : six couples, tous de nature norme, **6 concordances sur 6**, en mode
socle non disponible. *Deux d'entre eux sont contaminés — `cles_eval_gl.py`
imprime en clair les cas sans adresse relevable avant que le fil joue ; la
population réellement aveugle est de quatre.* Et le PLF 1906 comme le PLFSS 1907
sont digérés : 82 articles, 2 164 alinéas, **386 adresses ouvertes**, dix
contrôles zéro échec.
*La liasse porte **6 amendements, pas 8** : 31 numéros aux liasses PLF plus 6 fait
37, pour un contre-budget annoncé à 39. Deux manquent.*

**§7, la jauge et le clic.** Les 113 519 octets de marge sont mesurés au matin du
20260902, avant plusieurs versements — à relire à `project_info`, jamais à
supposer. Et le clic sur `vecteur-mesure` est fait : sa description enregistrée
ne nomme plus aucun lot.

**§6, dette — deux noms canoniques à retenir.** Les sorties d'éval versées par ce
fil sont `livrables/eval_gl/reponses_vecteur_mesure_plf.json` et
`livrables/eval_gl/reponses_vecteur_mesure_plfss.json`. Le fil courant en nomme
une troisième sans suffixe : c'est le fichier de travail, il ne se verse pas.

---

## 5. Défauts d'appareil inscrits, non corrigés

- **`cles_eval_gl.py` fuit la vérité-terrain par son propre résumé** : il nomme
  les cas sans adresse relevable et compte ceux qui portent un article, avant que
  le fil joue. Deux cas du lot PLFSS ont été joués en connaissance de cause.
- **`noter_eval_gl.py` lit `appareil/reponses.json`** quand le fil courant
  prescrit `livrables/eval_gl/reponses_vecteur_mesure.json` ; et il annonce le
  compte fixe des contaminés sans vérifier leur présence dans la population.
- **La notation mesure le rappel et ignore la précision** : un cas concorde dès
  qu'une adresse sur N intersecte. `GL-I-38` concorde sur un article rendu sur
  quatre, `GL-I-33` sur un sur neuf.
- **`controle_restauration.py` compte `technique/coffre.txt` parmi les non
  restaurés** alors qu'il concorde à l'octet — A-194, toujours ouvert.
- ~~**La porte du domaine du PLFSS n'est plus à `LO 111-3`** : `reference/gabarit_expose_sommaire.md`
  et les prompts de fil sont à corriger.~~ **Clos.** Le fait reste vrai — la porte
  est aux `LO 111-3-6` à `-3-8` depuis la loi organique du 14 mars 2022 — mais la
  correction est faite : trois documents corrigés le 20260902 (A-297), et
  *`gabarit_expose_sommaire.md` ne portait pas la mention*, vérification faite sur
  le document entier (A-298). **La grille est relevée depuis le 20260902** (A-336) :
  31 portes, 0 échec, `appareil/portes_domaine_lfss.py`, documentée à
  `reference/domaine_lfss_LO111-3.md`. *Ce document a porté le défaut comme ouvert
  pendant un mois après sa clôture — fermé le 20261001.*
