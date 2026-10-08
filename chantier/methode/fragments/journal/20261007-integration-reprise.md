# 20261007 — Fil Cowork d'intégration de la reprise du 20261007

**Porteur** : fil Cowork d'intégration. **Mandat** : appliquer les sections 1 à 4 de
`methode/reprise_20261007.md` aux lots 1 à 13, sans produire de pièce nouvelle ni toucher aucun
exposé. **Appui** : `methode/appui_des_passes.md` · `methode/reprise_20261007.md` ·
`methode/regles_redactionnelles.md` · `reference/guide_legistique.md` · dépôt de droit cloné dans
l'atelier, millésime LEGI 20261001. **Mesure** : 9 objets nommés au mandat, 9 présents ;
5 documents écrits au coffre ; 6 arbitrages, 4 appliqués, 2 tenus ; 2 rédactions provisoires
passées à la checklist.

## Ce qui a changé au corpus

- **Pièce 4.5** — taux de l'impôt sur les sociétés écrit en dur à 27 %, corridor réglementaire
  supprimé (arbitrage 4) ; borne prélèvements obligatoires sur produit intérieur brut sortie du
  dispositif, l'ancien V devient le IV (arbitrage 5). Le dernier membre du 34° de 4.5-b, qui
  annonçait le taux envisagé dans le corridor, perd son objet et tombe ; la dépendance de 4.5-a à
  4.5-b disparaît.
- **Pièce 4.6** — reclassée au circuit A, clause de restitution conservée, dispositif intact
  (arbitrages 6 et 7).
- **Lot 10** — les deux rédactions marquées `rédaction provisoire, passe checklist due` ont reçu
  leur passe : 9 lignes de contrôle, 9 verdicts, 3 corrections. Marquage levé.
- **Méthode** — reprises 4 à 7 du § 3, règle d'abrogation par bloc et borne d'exposé à 350 mots
  inscrites aux règles rédactionnelles ; reprises 1 et 2 inscrites à l'appui des passes.
- **Invariant `Appui`** porté aux deux pièces touchées (reprise 11, écart historique).

## Ce qui reste ouvert

- **Arbitrages 8 et 11, pièce 4.7** — tenus. La date en dur suppose de ventiler les 181 articles
  du I entre les dates du IV de la clause générale ; il y faut les listes nominatives de l'état du
  lot U7, qui n'est pas au coffre. Le lot 19 commande cette passe.
- **Observation 2.1, clause générale** — le regroupement par bloc du III, la renumérotation et la
  reprise des renvois se font en une seule passe, à l'application du lot validé.
- **Exposés** — aucun touché. À la régénération en bloc : l'erreur de fait de la pièce 4.2 A
  (taux réduits de taxe sur la valeur ajoutée écrits à la place des niches, arbitrage 19), et les
  deux exposés de 4.5, qui décrivent encore le corridor et doivent recevoir l'objectif de
  non-hausse et la borne de prélèvements obligatoires.
- **Registre des sources de gage** — la pièce 4.6 y figure encore au circuit B ; reprise due, avec
  le contrôle « un euro, un circuit » des croisements.
- **Typographie** — laissée entière au paquet, comme la reprise 12 le prescrit.
- **`impression-docx`, § 5** — contradiction de nommage signalée, non corrigeable depuis le coffre.

## Constat d'appareil, qui corrige une croyance

**Le dépôt de droit se clone depuis une session Cowork.** Vérifié ce jour :
`git clone --depth 1 https://github.com/resolution-ib-dev/Resolution-2027 droit` puis
`python3 droit/droit.py etat` rendent `millésime LEGI 20261001 — 6 j frais`, neuf codes lisibles
hors ligne. **Un fil Cowork n'a donc pas à renvoyer au fil code une passe qui demande le droit en
vigueur** : il a le coffre et le droit ensemble, ce que le fil code n'a pas. Le partage des fils
est recalé en conséquence à `methode/appui_des_passes.md`.

## Décisions prises en propre

1. **Les pièces portant du verbatim ne se réécrivent pas pour une correction locale lorsque la
   recopie risque de les déformer.** La pièce 4.7 porte 366 numéros d'articles en deux
   énumérations : ses corrections se rendent en clair et s'appliquent par copie d'octets. Les
   pièces 4.5 et 4.6, dont les corrections portaient sur des divisions identifiées, ont été
   réécrites en entier avec report verbatim du reste.
2. **La conséquence mécanique d'un arbitrage s'applique avec lui, et se déclare** — ici, la phrase
   du 34° de 4.5-b privée d'objet par la suppression du corridor.
3. **Un paramètre politique écrit en dur sans arbitrage repasse entre crochets** — le délai de
   réexamen de l'incapacité, lot 10, porté à « [deux à cinq] ans ».
