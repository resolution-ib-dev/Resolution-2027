# Le CGI réécrit par l'expert — règles de lecture et d'emploi

Source versée le 2026-09-29. **Source privilégiée pour la rédaction des
amendements** : elle porte la rédaction cible de l'auteur sur 2 376 articles du
code général des impôts.

---

## 1. Ce qu'est la source, et ce qu'elle n'est pas

**Ce qu'elle est.** La rédaction cible déclarée de l'auteur, article par
article. Elle alimente la **colonne C** du trois colonnes de
`methode/contrat_chaine_amendement.md` — l'étape E4, qui produit le texte tel
qu'il sera.

**Ce qu'elle n'est pas.** Ni une doctrine, ni un chiffrage, ni un véhicule. Elle
ne qualifie aucun rattachement. Elle **ne se corrige pas** : un désaccord avec
elle se porte à l'auteur, il ne se règle pas en réécrivant la source.

**Origine.** Cinq documents de rapprochement Word générés le 2026-08-17,
comparant le code général des impôts extrait de Légifrance au texte réécrit.
Les .docx ne sont pas au corpus : ils sont restés au fil de digestion.

---

## 2. Le millésime — la règle qui commande tout

**Le droit de départ est le code général des impôts à jour au 1er mai 2026,
extrait le 27 mai 2026.**

Conséquence pour tout fil qui emploie la source :

1. **La colonne A ne se lit jamais dans la source.** Elle se régénère depuis le
   dépôt de droit, à la date du texte en discussion :
   `droit.article("code général des impôts", num, jour="AAAA-MM-JJ")`.
2. **Avant d'employer un article, le contrôler dans
   `cgi_expert_articles_bouges.tsv`.** 78 articles ont changé de version depuis
   le 1er mai 2026, 4 ont disparu, 186 portent une abrogation déjà votée. Sur
   ces 268, la rédaction de l'expert part d'un état qui n'est plus le droit.
3. **41 articles applicables sont hors du périmètre des cinq pièces**, dont 31
   en contributions indirectes. La source ne dit rien d'eux : leur silence n'est
   pas un maintien.

## 3. Comment reconstruire un article

**Article abrogé** (1 338 cas, `operation = supprimé` dans
`cgi_expert_articles.tsv`) : C est vide. La disposition modificative est
« L'article N du code général des impôts est abrogé. »

**Article complété ou réécrit** (199 cas) : les segments neufs sont intégralement
dans `cgi_expert_insertions.tsv`, avec leur ancrage — les 40 caractères qui
précèdent et qui suivent. C = A, moins les suppressions, plus les insertions.

**Article allégé** (205 cas) : `cgi_expert_suppressions.tsv` donne, par alinéa,
la longueur du segment retiré et ses 26 premiers caractères, plus 14 caractères
d'ancrage amont. **Le texte supprimé n'est pas versé : il est régénérable depuis
le dépôt de droit au 1er mai 2026**, conformément à la règle du corpus selon
laquelle la colonne A est du verbatim régénérable. Si la reconstruction exacte
d'un alinéa est nécessaire et que l'ancrage ne suffit pas, la pièce .docx du fil
de digestion fait foi.

**Le désalignement du rapprochement Word.** Quand un article est supprimé et
que son voisin est réécrit, Word apparie parfois le texte neuf à la position de
l'article supprimé. Deux cas relevés, et ils sont corrigés dans les
référentiels : le crédit d'impôt universel, physiquement dispersé dans la zone
des articles 199 quater C à 199 terdecies-0 A, relève de **200 septdecies** ; la
rédaction des plus-values à long terme — imposition séparée à 30 %, reprise
d'amortissements à 23 % —, placée sous l'en-tête supprimé de 39 quaterdecies,
relève de **39 quindecies**. **Un article dont le texte semble incohérent avec
son numéro se recontrôle sur le .docx du fil avant emploi.**

**Article renuméroté** (8 cas réels) : les sept premiers sont des appariements du
rapprochement Word entre un article supprimé et son voisin conservé, et ne
portent pas de renumérotation voulue. **Seul 199 quater C → 200 septdecies en
est une**, et elle porte un contenu neuf : le crédit d'impôt universel.

## 4. Les paramètres

`cgi_expert_parametres.tsv` porte les 47 taux, montants et abattements relevés
dans l'état final, avec leur article et leur phrase. **Il se confronte au REF
avant tout emploi** : un paramètre de la source qui contredit le REF est un
écart à instruire, non une valeur à reprendre.

Les valeurs structurantes : impôt sur le revenu **23 %** (art. 197), revenus du
capital et plus-values **30 %** (art. 200 A), impôt sur les sociétés **25 %**
(art. 219), TVA **20 %** et taux réduit **7 %** (art. 278, 278-0 bis),
mutations **3 %** (art. 683, 1594 D), crédit d'impôt universel **500 €** et
**250 €** par mois (art. 200 septdecies).

## 5. Les points ouverts — ce qui est préparé pour qui les rencontrera

**Ce paragraphe n'ordonne rien et ne nomme aucun lot.** Il attache à chaque point
ouvert son critère, son instrument et son défaut, pour que la chaîne d'amendement
n'ait pas à les rouvrir quand elle arrive dessus. L'ordre des travaux ne vient pas
d'ici.

`cgi_expert_comblements_20260929.md` porte deux comblements et quatre points qui
ne se comblent pas par lecture. Ce qui est préparé pour chacun :

**Le partage entre 23 %, 25 % et 30 %.** Critère disponible :
`reference/justice_fiscale_1789_fondapol.md` pose que la progressivité n'est
constitutionnellement exigée que sur l'imposition globale du revenu — l'article
197 est du côté contraint, les assiettes catégorielles ne le sont pas.
Instruments : `analyse-transposabilite` puis `compatibilite-doctrine`. Défaut si
l'instruction ne conclut pas : le taux de l'article 197 est isolé des articles à
23 % et à 30 %, un amendement mêlant les deux registres tombant entier sur une
objection portant sur un seul. **L'article 39 quindecies mêle 30 % et 23 % dans
la même phrase** : il ne se rédige pas avant que le partage soit arrêté.

**Le taux réduit de TVA à 7 % contre le taux unique de M-029.** Critère : le
rendement du taux à 7 % confronté aux 33,4 Md€ que M-029 attache au taux unique.
Instrument : `compatibilite-doctrine` sur le chiffrage du bloc B-09. Défaut : le
corpus prime, l'article 278-0 bis tombe avec les autres taux réduits, et l'écart
à la rédaction de l'expert se déclare en exposé sommaire.

**Le taux d'impôt sur les sociétés et M-032.** Critère : le socle budgétaire
porte-t-il la hausse transitoire, son taux et son terme — mesuré, non déclaré.
Défaut : si le socle ne porte rien, M-032 n'est pas chiffrée et la disposition ne
se rédige pas ; elle se déclare en attente de chiffrage. *Une disposition bâtie
sur un paramètre que rien ne chiffre est une disposition à refaire.*

**Le siège du compte épargne au code monétaire et financier.** C'est une
rédaction nouvelle, pas une référence à retrouver : A-327 l'autorise en mode
développé, sur demande. Instrument : `disposition-cible` en mode proposition de
loi complète, squelette transposé de L. 221-30 (ouverture, titulaires),
L. 221-31 (emplois) et L. 221-32 (retraits, clôture), chaque écart au modèle
déclaré. Défaut : la disposition au CGI se rédige seule et la jambe au code
monétaire et financier se **signale** en fin d'exposé sommaire sans être rédigée
— régime par défaut de A-318 amendé par A-327.

`cgi_expert_couverture_20260929.md` porte les huit écarts entre ce que le bloc
B-09 pose et ce que le texte écrit.

`cgi_expert_commentaires_20260929.md` porte les 74 commentaires de l'expert,
aucun tranché. **Un amendement sur un article commenté se rédige après
l'arbitrage, pas avant** — la liste sert à écarter ces articles d'un lot, elle ne
dit pas lequel.

**Les renvois entrants.** Régime arrêté le 20260902, rappelé ici parce qu'il
pèse sur cette source : service minimum, on signale et on ne coordonne pas ; seuls
les renvois `nomme` et `interne` se listent, en fin d'exposé sommaire ; les
`ambigu` se comptent. A-325 : sans la règle de déduction, le compte brut est faux
d'un facteur cinq à trente, et d'autant plus que le numéro d'article est court —
ce qui vise directement les articles les plus cités de cette source.
`coordination.py` n'est pas au dépôt public (A-326).

## 6. Les pièces

| pièce | contenu |
|---|---|
| `referentiels/cgi_expert_articles.tsv` | 1 754 articles touchés : opération, volume final, commentaires |
| `referentiels/cgi_expert_insertions.tsv` | 434 segments neufs, texte intégral et ancrage |
| `referentiels/cgi_expert_suppressions.tsv` | 3 249 segments retirés : alinéa, longueur, ancrage |
| `referentiels/cgi_expert_articles_bouges.tsv` | 254 articles à contrôler avant emploi |
| `referentiels/cgi_expert_parametres.tsv` | 47 paramètres avec leur adresse |
| `livrables/cgi_expert_couverture_20260929.md` | ce que la fusion suppose et que le texte ne porte pas |
| `livrables/cgi_expert_comblements_20260929.md` | ce qui est comblé, par quoi, et ce qui reste ouvert |
| `livrables/cgi_expert_commentaires_20260929.md` | 74 commentaires non tranchés |
| `livrables/predigestion_cgi_20260929.md` | la mesure et la datation |

## 7. Ce qui n'a pas pu être versé, et où le retrouver

**L'état final accepté intégral** — la rédaction cible des 2 362 articles en
texte continu, 1,4 Mo — **ne tient pas dans la jauge du corpus** (522 Ko
disponibles au versement). Il se reconstruit depuis le dépôt de droit et les
deux tables de segments, selon le § 3.

**L'état de départ intégral** — 5,0 Mo — n'a pas vocation à être versé : c'est
du verbatim Légifrance au 1er mai 2026, régénérable en une commande.

**Pour loger durablement les deux états**, le lieu est le dépôt
`resolution-ib-dev/Resolution-2027`, comme le pose `reference/depot_droit.md`
pour les pièces trop lourdes pour le coffre. **L'écriture y est refusée tant que
le dépôt n'est pas déclaré aux sources de la session en écriture** — vérifié le
2026-09-29, refus explicite du mandataire git.
