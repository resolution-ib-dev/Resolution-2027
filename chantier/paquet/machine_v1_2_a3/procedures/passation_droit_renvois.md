# Le dépôt de droit, les renvois entrants, et ce qu'ils changent

Établi le 20260902.

---

## 1. Arbitrage — les renvois entrants, 20260902

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

Voir `procedures/depot_droit.md` pour la procédure complète. Trois faits qui
commandent la rédaction :

**L'étape « texte en vigueur » n'est plus un trou.** Vingt codes, 21 Mo,
millésime LEGI du 20260901, clonables sans autorisation :
`git clone https://github.com/resolution-ib-dev/Resolution-2027 droit`.
Légifrance reste injoignable depuis l'atelier — neuf tentatives, huit `403`.

**L'applicabilité se lit aux dates, jamais à l'état.** Le CGI porte **376
articles applicables dont l'abrogation est déjà votée**, le CIBS **282**. Le
lecteur sort l'avertissement de lui-même.

**Trois des vingt-deux amendements du lot visent du droit abrogé au 1er janvier
2027** : un premier (CGI 278 bis, 279, 278 sexies), un deuxième (CGI 279),
un troisième (CGI 1594 F quinquies), plus la ligne PEEC d'un quatrième au CIBS
L. 313-1. **Rédiger dans l'absolu reste juste ; c'est le branchement qui devra en
tenir compte** — contrôle de dernier moment, arbitré en amont.

**Le droit non codifié n'est pas au dépôt.** Un siège dans une loi de finances
antérieure ne s'y trouvera pas — l'article 179 de la loi de finances pour 2020
est le cas connu. La voie existe, une ligne dans `codes.json` avec le `LEGITEXT`
du texte non codifié : **non éprouvée.**
