# Reconfirmation des chiffres du manuscrit — 20260921

*Relevé. Aucune valeur neuve, aucun recalcul, aucune source écrite, aucun chiffre du manuscrit remis en cause. Le manuscrit fait foi ; un écart se relève, il ne se tranche pas.*

## Le compte

**311 chiffres relevés au manuscrit — identique 74 · divergent 0 · absent 225 · ambigu 12.** 71 des 257 entrées du référentiel sont atteintes par un chiffre du manuscrit. Les 93 entrées sans source : retrouvées au manuscrit 2 · dérivées 5 · d'origine inconnue 86. 11 divergences relevées côté référentiel, et neuf sources citant un onglet disparu.

## Ce que le compte veut dire

**La case `divergent` est vide côté manuscrit.** Aucun chiffre du manuscrit n'a trouvé, à son propre ancrage, une entrée du référentiel portant le même fait sous une autre valeur ou une autre unité. Les divergences existent, mais elles se lisent dans l'autre sens : une entrée adossée à une note porte une valeur qu'aucun chiffre de cette note ne porte. Elles sont isolées plus bas.

**La case `absent` est la plus grosse, et ce n'est pas une anomalie.** Le référentiel n'a jamais été un relevé exhaustif du manuscrit : il agrège les notes de fin porteuses d'un chiffre, les nœuds chiffrés de la doctrine et les candidats du proto. 225 chiffres du corps et des notes n'y ont donc aucun correspondant. C'est la mesure de l'écart, non un défaut à corriger ici.

**L'ancrage du référentiel à la doctrine ne résout pas.** 56 entrées de provenance `ref_doctrine` déclarent des codes de preuve en `M-nnnn`. Ces identifiants renvoient à `referentiels/releve_affecte.json`, que le bloc `manquants` de l'index déclare introuvable. Leur rattachement au manuscrit est donc invérifiable, et leur appariement ci-dessous s'est fait par la valeur et le libellé seuls. **Ce point n'est pas de ce fil** : il est déjà aux manquants.

## Comment le relevé a été fait

Mécaniquement, en deux passes, sur `manuscrit/manuscrit.html` restauré du coffre et prouvé de l'extérieur : `extraire_notes.py` rejoué dessus rend `referentiels/notes_manuscrit.json` **identique à l'octet**. `referentiels/REF_chiffres.json` est hors coffre ; il a été régénéré par `generer_ref_chiffres.py` — 257 entrées, 93 sans source, `0 échec` au contrôle, 57 calculs rejoués justes, ce qui est l'état relevé le 20260917.

Ce qui est écarté du relevé, et pourquoi : une année seule sans unité (c'est une date), un numéro d'article, d'alinéa, de page, de décret ou de rapport, un quantième de date, un ordinal. Une somme d'argent ne se compare qu'à une somme d'argent : l'échelle (€, M€, Md€) ne se devine pas. Deux valeurs sont dites égales à 0,5 % près.

## Les notes de fin, prises à part

Le manuscrit porte **141 notes de fin**. `extraire_notes.py` en déclare **37** porteuses d'un chiffre, et `REF_chiffres` en représente exactement **37** : la couverture du référentiel est celle du détecteur, ni plus ni moins. **Le relevé de ce fil en trouve 51** — 14 notes portent un nombre que le détecteur n'a pas vu, pour 23 nombres.

**L'écart se partage, et il ne se tranche pas ici.** La nature proposée ci-dessous est un jugement de fait de Claude, *proposé et non validé* : un renvoi n'a pas à entrer au référentiel, une grandeur oui.

| note | nombres relevés | nature apparente *(proposé)* | ce que le nombre désigne |
|---|---|---|---|
| `e16` | 1, 2.6 | renvoi | numérotation de paragraphe « 2.6.2 » |
| `e18` | 5, 116 | renvoi | pagination « pages 113 à 116 » |
| `e26` | 677 | renvoi | pagination « 677–688 » |
| `e40` | 140 kg | grandeur | 140 kg de cocaïne saisis |
| `e48` | 101, 15 ans, 15 ans, 13 ans | grandeur | 101 dossiers ; âges médians 15 et 13 ans |
| `e60` | 2 600 articles | grandeur | 2 600 articles au code de l’urbanisme |
| `e61` | 438 taxes | grandeur | 438 taxes — le même chiffre qu’au corps |
| `e62` | 2 | renvoi | fragment d’adresse web |
| `e81` | 13 | renvoi | numéro de fiche |
| `e93` | 4 | renvoi | subdivision « 4° » d’un article |
| `e98` | 1, 1, 2 | renvoi | tomes 1 et 2 d’une annexe |
| `e103` | 10, 11 | grandeur | taux multiplié par 10 ; numéro de fiche 11 en renvoi |
| `e114` | 16 m2, 25 m2 | grandeur | 16 m² contre 25 m² de surface par poste |
| `e137` | 33 | renvoi | numéro de département « (33) » |

**6 notes sur 14 portent une grandeur** — `e40`, `e48`, `e60`, `e61`, `e103`, `e114`. Elles n'ont aucune entrée au référentiel, et le détecteur de `extraire_notes.py` est la cause. Les 8 autres sont des renvois — pagination, numéro de fiche, subdivision d'article, adresse web — que le relevé de ce fil a pris pour des chiffres : **ce sont ses propres faux positifs, et ils sont déclarés.**

`extraire_notes.py` reste prouvé : rejoué sur le manuscrit restauré, il rend `referentiels/notes_manuscrit.json` identique à l'octet. **Ce qui est en cause n'est pas la copie, c'est le détecteur** — il reproduit fidèlement un relevé qui laisse des grandeurs dehors.

## Table des chiffres du manuscrit

| emplacement | libellé | valeur | case | entrée | remarque |
|---|---|---|---|---|---|
| Prologue / prologue-C0-la-france-nest-pas-en-crise-son-etat… | N’en jetez plus, 90 % des Français sont conscients de ce déclin. | 90 % | `absent` | — |  |
| Prologue / prologue-C0-la-france-nest-pas-en-crise-son-etat… | Ce sont les 68 millions de Français qui font le génie de leur pays, et les plus illustres étaient tous, à leur façon, critiques de l’État, de Molière… | 68 millions | `absent` | — |  |
| Prologue / prologue-C0-pourquoi-ne-pas-se-resigner | Elle a traversé et sauvé le pays à tout juste 17 ans. | 17 ans | `absent` | — |  |
| Prologue / prologue-C0-comment-faire | L’Assemblée constituante, qui a planché sur sa rédaction tout l’été après avoir aboli les privilèges, l’a inclus en deux endroits, aux articles 14 et… | 15 | `absent` | — | même valeur portée par N-e118-2, R-D7-3-1-p1 — aucun libellé ne recoupe la phrase |
| Prologue / prologue-C0-pour-un-nouveau-contrat-social | Notre plan est clair et chiffré : concentrer l’Etat sur 7 missions indispensables, interrompre ses missions facultatives et économiser ainsi 236 mill… | 7 | `absent` | — | même valeur portée par N-e141-1, R-D6-2-2-p2 — aucun libellé ne recoupe la phrase |
| Prologue / prologue-C0-pour-un-nouveau-contrat-social | Notre plan est clair et chiffré : concentrer l’Etat sur 7 missions indispensables, interrompre ses missions facultatives et économiser ainsi 236 mill… | 236 milliards d’euros | `absent` | — | même valeur portée par R-D2-1-1-e1 — aucun libellé ne recoupe la phrase |
| Prologue / prologue-C0-pour-un-nouveau-contrat-social | Lorsqu’on dépense moins, on taxe moins : le travailleur type verra 600 euros par mois rendus sur sa feuille de paie. | 600 euros | `identique` | `R-D3-2-2-e1` (600 €/mois) | apparié hors ancrage, par la valeur et le libellé |
| Prologue / prologue-C0-pour-un-nouveau-contrat-social | Côté patrimoine, restituer 600 milliards d’euros d’actifs publics non indispensables à céder aux Français : chaque ménage recevra 20 000 euros de cap… | 600 milliards d’euros | `absent` | — |  |
| Prologue / prologue-C0-pour-un-nouveau-contrat-social | Côté patrimoine, restituer 600 milliards d’euros d’actifs publics non indispensables à céder aux Français : chaque ménage recevra 20 000 euros de cap… | 20 000 euros | `ambigu` | `R-D7-2-1-p1` (20 000) | 2 entrées de même valeur et de libellé proche |
| L’ÉTAT NOUS APPAUVRIT / P1-C1 / P1-C1-lenfer-nest-pas-les-a… | Pourtant, la France resterait encore dans le peloton des pays les plus dépensiers au monde : les dépenses publiques baisseraient de 57 % à 51 % de la… | 57 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C1 / P1-C1-lenfer-nest-pas-les-a… | Pourtant, la France resterait encore dans le peloton des pays les plus dépensiers au monde : les dépenses publiques baisseraient de 57 % à 51 % de la… | 51 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C1 / P1-C1-lenfer-nest-pas-les-a… | Confisquer l’intégralité des 500 plus grandes fortunes de France couvrirait à peine huit mois de dépenses publiques. | 500 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C1 / P1-C1-lenfer-nest-pas-les-a… | Si l’on pousse encore le curseur plus loin et que l’on envisage de saisir 100 % du bénéfice annuel de toutes les entreprises de France, des plus impo… | 100 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C1 / P1-C1-tous-perdants-du-syst… | Un Suisse dispose d’un revenu réel médian deux fois supérieur à un Français : 4 300 euros par mois contre 2 100 euros par mois en France. | 4 300 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C1 / P1-C1-tous-perdants-du-syst… | Un Suisse dispose d’un revenu réel médian deux fois supérieur à un Français : 4 300 euros par mois contre 2 100 euros par mois en France. | 2 100 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C1 / P1-C1-tous-perdants-du-syst… | Un Danois aussi vit bien mieux qu’un Français, avec un salaire médian de 3 400 euros par mois. | 3 400 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C1 / P1-C1-tous-perdants-du-syst… | Si notre économie était aussi florissante qu’aux Pays-Bas, nous gagnerions 25 % de pouvoir d’achat, aurions deux mois de vacances en plus des congés… | 25 % | `absent` | — | même valeur portée par N-e78-1, R-D7-3-1-e1 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C1 / P1-C1-tous-perdants-du-syst… | Si notre économie était aussi florissante qu’aux Pays-Bas, nous gagnerions 25 % de pouvoir d’achat, aurions deux mois de vacances en plus des congés… | 55 ans | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C1 / P1-C1-tous-perdants-du-syst… | Sur un total de 1,7 million de Français établis à l’étranger, la Suisse est le premier pays d’accueil, choisie par près de 10 % d’entre eux. | 1,7 million | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C1 / P1-C1-tous-perdants-du-syst… | Sur un total de 1,7 million de Français établis à l’étranger, la Suisse est le premier pays d’accueil, choisie par près de 10 % d’entre eux. | 10 % | `absent` | — | même valeur portée par N-e65-1, N-e92-1, N-e120-1, N-e125-1… — aucun libellé ne recoupe l… |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-4-500-euros-par-mois-… | 4 500 euros par mois. | 4 500 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-un-francais-est-mieux… | Pour une heure de travail, le travailleur moyen produit 63 euros de richesse mais récupère seulement 23 euros nets. | 63 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-un-francais-est-mieux… | Pour une heure de travail, le travailleur moyen produit 63 euros de richesse mais récupère seulement 23 euros nets. | 23 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-un-francais-est-mieux… | Les propriétaires du capital (actionnaires, bailleurs, créanciers) ne perçoivent que 11 euros, dont moitié de bénéfice de l’entreprise. | 11 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-un-francais-est-mieux… | La part du lion est prélevée de force par l’État : 29 euros en impôt immédiat et 4 euros en impôt futur par le déficit. | 29 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-un-francais-est-mieux… | La part du lion est prélevée de force par l’État : 29 euros en impôt immédiat et 4 euros en impôt futur par le déficit. | 4 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-reconsiderons-donc-no… | Il coûte à chaque foyer français 54 000 euros par an. | 54 000 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-elle-ne-pese-pas-seul… | Le travail est plus lourdement taxé que tous les autres revenus : 47 % du salaire moyen. | 47 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-la-personne-la-plus-t… | Lorsque son salaire augmente et qu’il perd le bénéfice de la prime d’activité ou du RSA, le gain du travailleur est de 0 euro : son effort est taxé à… | 0 euro | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-la-personne-la-plus-t… | Lorsque son salaire augmente et qu’il perd le bénéfice de la prime d’activité ou du RSA, le gain du travailleur est de 0 euro : son effort est taxé à… | 100 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-les-francais-ne-sont-… | En 2025, 40 % des entreprises de l’industrie et presque autant dans les services rencontraient des difficultés à recruter. | 40 % | `absent` | — | même valeur portée par N-e83-1 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C2 / P1-C2-tous-au-ralenti | L’agriculture en est le témoin éclatant : la mécanisation a éradiqué les famines tout en ne mobilisant aujourd’hui que 2 % des actifs, contre plus de… | 2 % | `absent` | — | même valeur portée par N-e6-1, N-e14-1 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C3 / P1-C3-le-cercle-vicieux | La puissance publique prélève et dépense sans cesse : 1 714 milliards d’euros dépensés en 2025, record mondial en proportion de la production. | 1 714 milliards d’euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C3 / P1-C3-leuro-empeche | Des administrations que nous finançons réglementent à temps plein, avec constance : 67 000 pages par an au journal officiel. | 67 000 pages | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C3 / P1-C3-leuro-empeche | Si le ministère de l’agriculture comptait moins de personnel que les 20 000 agents actuels, les normes européennes, qui ne sont pas connues pour être… | 20 000 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C3 / P1-C3-leuro-empeche | Transformer les heures de travail administratif imposé en heures créatrices de valeur nous enrichirait immédiatement de l’ordre de +10 %, soit un gai… | 10 % | `absent` | — | même valeur portée par N-e65-1, N-e92-1, N-e120-1, N-e125-1… — aucun libellé ne recoupe l… |
| L’ÉTAT NOUS APPAUVRIT / P1-C3 / P1-C3-leuro-empeche | Transformer les heures de travail administratif imposé en heures créatrices de valeur nous enrichirait immédiatement de l’ordre de +10 %, soit un gai… | 10 000 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C3 / P1-C3-la-subvention-est-un-… | Le crédit d’impôt recherche (CIR), niche fiscale la plus coûteuse, bénéficie pour plus de 100 millions d’euros par an à Sanofi, le crédit d’impôt pou… | 100 millions d’euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C3 / P1-C3-la-subvention-est-un-… | Le crédit d’impôt recherche (CIR), niche fiscale la plus coûteuse, bénéficie pour plus de 100 millions d’euros par an à Sanofi, le crédit d’impôt pou… | 66 millions d’euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C3 / P1-C3-si-letat-gerait-mal-l… | Seulement 6 % de ses dépenses participent à notre sécurité (armées, intérieur et justice), première de ses missions, régalienne par excellence. | 6 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-trop-detat-tue-letat | On recense 434 agences nationales, 329 organismes centraux, 24 autorités indépendantes, et 318 instances consultatives. | 434 agences | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-trop-detat-tue-letat | On recense 434 agences nationales, 329 organismes centraux, 24 autorités indépendantes, et 318 instances consultatives. | 329 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-trop-detat-tue-letat | On recense 434 agences nationales, 329 organismes centraux, 24 autorités indépendantes, et 318 instances consultatives. | 24 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-trop-detat-tue-letat | On recense 434 agences nationales, 329 organismes centraux, 24 autorités indépendantes, et 318 instances consultatives. | 318 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-trop-detat-tue-letat | La France compte 5,8 millions d’agents publics, soit un actif sur cinq. | 5,8 millions | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-trop-detat-tue-letat | Par comparaison, le plus gros groupe privé de France, Carrefour, emploie environ 170 000 personnes. | 170 000 personnes | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-trop-detat-tue-letat | France Travail compte 55 000 collaborateurs, contre 21 000 employés chez LinkedIn pour le monde entier. | 55 000 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-trop-detat-tue-letat | France Travail compte 55 000 collaborateurs, contre 21 000 employés chez LinkedIn pour le monde entier. | 21 000 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-trop-detat-tue-letat | Pourtant, plus de 90 % des nouveaux contrats de travail sont signés sans jamais passer par France Travail. | 90 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-nos-impots-alimentent… | L’Élysée mobilise aujourd’hui 800 personnes, dont 80 à l’intendance et 70 à la correspondance présidentielle, pour un total de 127 millions d’euros p… | 800 personnes | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-nos-impots-alimentent… | L’Élysée mobilise aujourd’hui 800 personnes, dont 80 à l’intendance et 70 à la correspondance présidentielle, pour un total de 127 millions d’euros p… | 80 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-nos-impots-alimentent… | L’Élysée mobilise aujourd’hui 800 personnes, dont 80 à l’intendance et 70 à la correspondance présidentielle, pour un total de 127 millions d’euros p… | 70 | `absent` | — | même valeur portée par R-D6-2-2-p1 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-nos-impots-alimentent… | L’Élysée mobilise aujourd’hui 800 personnes, dont 80 à l’intendance et 70 à la correspondance présidentielle, pour un total de 127 millions d’euros p… | 127 millions d’euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-nos-impots-alimentent… | La Mairie de Paris compte davantage d’agents de la ville chargés de communication (229) que de la gestion des égouts de la capitale (207). | 229 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-nos-impots-alimentent… | La Mairie de Paris compte davantage d’agents de la ville chargés de communication (229) que de la gestion des égouts de la capitale (207). | 207 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-lexces-detat-nuit-la-… | En conséquence, ils ne se mobilisent plus dans les urnes : on n’enregistre que 33 % de participation pour les élections régionales et départementales. | 33 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-lexces-detat-nuit-la-… | Le Parlement coûte près d’un milliard d’euros par an, pour 925 élus. | 925 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-lexces-detat-nuit-la-… | Le Conseil Economique Social et Environnemental (CESE) ajoute un coût de 44 millions d’euros par an et s’auto-saisit la plupart du temps tant il se c… | 44 millions d’euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-lexces-detat-nuit-la-… | Au bout de 4 votes, la décision finale représente déjà moins de 7 % des électeurs initiaux (soit 51 % multiplié 4 fois par lui-même). | 4 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-lexces-detat-nuit-la-… | Au bout de 4 votes, la décision finale représente déjà moins de 7 % des électeurs initiaux (soit 51 % multiplié 4 fois par lui-même). | 7 % | `absent` | — | même valeur portée par N-e141-1 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-lexces-detat-nuit-la-… | Au bout de 4 votes, la décision finale représente déjà moins de 7 % des électeurs initiaux (soit 51 % multiplié 4 fois par lui-même). | 51 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-lexces-detat-nuit-la-… | Au bout de 4 votes, la décision finale représente déjà moins de 7 % des électeurs initiaux (soit 51 % multiplié 4 fois par lui-même). | 4 fois | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-de-nul-nest-cense-ign… | Notre code du travail compte près de 4 000 pages, contre à peine 200 pages pour le code du travail suisse. | 4 000 pages | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-de-nul-nest-cense-ign… | Notre code du travail compte près de 4 000 pages, contre à peine 200 pages pour le code du travail suisse. | 200 pages | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-de-nul-nest-cense-ign… | Pour autant notre taux de chômage dépasse 8 %, alors que la Suisse est au plein emploi et compte même plus d’emplois que d’actifs grâce à ses nombreu… | 8 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-de-nul-nest-cense-ign… | Nos 521 pages de code de la route sont synthétisées en un manuel lisible par des jeunes de 16 ans. | 521 pages | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-de-nul-nest-cense-ign… | Nos 521 pages de code de la route sont synthétisées en un manuel lisible par des jeunes de 16 ans. | 16 ans | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-de-nul-nest-cense-ign… | Si un test de 40 questions suffit pour conduire, alors le code entier lui-même peut se résumer en si peu de mots. | 40 | `absent` | — | même valeur portée par N-e83-1 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-la-creature-a-echappe… | Prenons par exemple le code de la commande publique : une chaise ou une cafetière payée 160 euros au lieu de 60 euros afflige les contribuables qui p… | 160 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-la-creature-a-echappe… | Prenons par exemple le code de la commande publique : une chaise ou une cafetière payée 160 euros au lieu de 60 euros afflige les contribuables qui p… | 60 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-la-creature-a-echappe… | Le volume du droit a doublé depuis vingt ans selon un phénomène de boule de neige, de 25 à 49 millions de mots. | 25 | `absent` | — | même valeur portée par N-e78-1, R-D7-3-1-e1, R-D8-2-3-p1, R-D9-4-2-p2 — aucun libellé ne… |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-la-creature-a-echappe… | Le volume du droit a doublé depuis vingt ans selon un phénomène de boule de neige, de 25 à 49 millions de mots. | 49 millions | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-438-impots-486-niches… | 438 impôts, 486 niches fiscales et 1,7 milliard de combinaisons de charges sur le travail | 438 impôts | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-438-impots-486-niches… | 438 impôts, 486 niches fiscales et 1,7 milliard de combinaisons de charges sur le travail | 486 niches fiscales | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-438-impots-486-niches… | 438 impôts, 486 niches fiscales et 1,7 milliard de combinaisons de charges sur le travail | 1,7 milliard | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-regardons-ce-que-nous… | Elle compte 12 catégories fiscales sur le seul chocolat et ses taux réduits favorisent les navettes en Corse, les œuvres d’art, l’équitation ou les t… | 12 | `absent` | — | même valeur portée par N-e92-2, R-D3-2-1-p7 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-regardons-ce-que-nous… | Cette somme de taxe peut dépasser 50 % du prix de vente réel : c’est le cas du litre d’essence, taxé jusqu’à 60 %. | 50 % | `absent` | — | même valeur portée par N-e99-1, P-D-109 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-regardons-ce-que-nous… | Cette somme de taxe peut dépasser 50 % du prix de vente réel : c’est le cas du litre d’essence, taxé jusqu’à 60 %. | 60 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-regardons-ce-que-nous… | Cette usine à gaz coûte désormais 208 euros par an à chaque foyer sur sa facture énergétique. | 208 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C4 / P1-C4-les-niches-fiscales-s… | Certaines n’ont même plus aucun lien avec l’impôt : 45 % des crédits d’impôts sont des chèques envoyés par l’administration fiscale et non des impôts… | 45 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-et-si-nous-navions-pa… | La solidarité de base du RSA ne bénéficie ni aux jeunes de moins de 25 ans au chômage, ni aux 34 % d’éligibles qui n’y recourent pas, soit près d’un… | 25 ans | `absent` | — | même valeur portée par R-D8-2-3-p1 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-et-si-nous-navions-pa… | La solidarité de base du RSA ne bénéficie ni aux jeunes de moins de 25 ans au chômage, ni aux 34 % d’éligibles qui n’y recourent pas, soit près d’un… | 34 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-et-si-nous-navions-pa… | Le formulaire du RSA compte 7 pages, plusieurs colonnes et plus d’une centaine de lignes à remplir. | 7 pages | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-et-si-nous-navions-pa… | Comment juger des détresses ? 13 000 foyers sont non imposables à l’impôt sur le revenu tout en payant l’impôt sur la fortune immobilière. | 13 000 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-un-record-de-depenses… | Ainsi seulement 7 % des places d’hébergement « d’urgence » sont réservées aux femmes vulnérables à la rue, battues, enceintes ou avec enfant en bas â… | 7 % | `absent` | — | même valeur portée par N-e141-1 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-un-record-de-depenses… | Ce parc compte un total de 203 000 places, dont la moitié est occupée depuis plus d’un an par la même personne et au moins 60 % bénéficie à des perso… | 203 000 places | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-un-record-de-depenses… | Ce parc compte un total de 203 000 places, dont la moitié est occupée depuis plus d’un an par la même personne et au moins 60 % bénéficie à des perso… | 60 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-un-record-de-depenses… | Il offre un avantage de loyer de 180 euros par mois, à durée illimitée. | 180 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-un-record-de-depenses… | Si vous gagnez moins de 2500 euros par mois, vous y êtes éligible, comme trois foyers français sur quatre. | 2500 euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-un-record-de-depenses… | Il y a 2,8 millions de demandes en attente alors qu’un locataire du parc social sur dix dépasse les plafonds d’éligibilité, soit environ un demi-mill… | 2,8 millions | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-un-record-de-depenses… | Les locataires du parc privé doivent fournir un effort financier supérieur à ceux du parc social : 25 % de leur revenu contre 15 %. | 25 % | `absent` | — | même valeur portée par N-e78-1, R-D7-3-1-e1 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-un-record-de-depenses… | Les locataires du parc privé doivent fournir un effort financier supérieur à ceux du parc social : 25 % de leur revenu contre 15 %. | 15 % | `ambigu` | — | 2 entrée(s) de même valeur et de libellé partiellement recoupé |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-votre-retraite-depend… | Malgré un taux de cotisation qui a doublé, le déficit spontané du système des retraites est environ de 125 milliards d’euros par an, soit les deux-ti… | 125 milliards d’euros | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-votre-retraite-depend… | À titre illustratif, pour équilibrer le système des retraites dans les conditions actuelles, il faudrait tous partir à environ 69 ans ou baisser les… | 69 ans | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-votre-retraite-depend… | À 65 ans, il nous reste aujourd’hui encore vingt-deux ans à vivre, dont onze ans en pleine santé. | 65 ans | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-pour-son-premier-enfa… | Pour son premier enfant, un couple au SMIC bénéficie de 0 euro par mois d’aide sociale ou fiscale. | 0 euro | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-le-systeme-scolaire-f… | Seuls 7,4 % des élèves de milieux modestes se placent parmi les 25 % meilleurs élèves en mathématiques, soit le 4e plus mauvais score parmi 78 pays r… | 7,4 % | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-le-systeme-scolaire-f… | Seuls 7,4 % des élèves de milieux modestes se placent parmi les 25 % meilleurs élèves en mathématiques, soit le 4e plus mauvais score parmi 78 pays r… | 25 % | `absent` | — | même valeur portée par N-e78-1, R-D7-3-1-e1 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-le-systeme-scolaire-f… | Seuls 7,4 % des élèves de milieux modestes se placent parmi les 25 % meilleurs élèves en mathématiques, soit le 4e plus mauvais score parmi 78 pays r… | 78 | `absent` | — |  |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-la-tutelle-de-letat-s… | Par exemple, un élève de collège en Corse est 23 % mieux doté en euros que la moyenne nationale. | 23 % | `absent` | — | même valeur portée par R-D9-3-1-p1 — aucun libellé ne recoupe la phrase |
| L’ÉTAT NOUS APPAUVRIT / P1-C5 / P1-C5-luniversite-na-pas-le… | Seuls 30 % des inscrits obtiennent leur licence en trois ans. | 30 % | `absent` | — | même valeur portée par N-e15-2, P-D-095 — aucun libellé ne recoupe la phrase |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C1 / P1-C5-la-gratuite-des-… | L’État indispensable en 7 missions | 7 | `absent` | — | même valeur portée par N-e141-1, R-D6-2-2-p2 — aucun libellé ne recoupe la phrase |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C1 / P2-C1-pour-etre-fort-l… | En échange de nos impôts, l’État doit se concentrer sur 7 missions que lui seul peut et doit assurer. | 7 | `absent` | — | même valeur portée par N-e141-1, R-D6-2-2-p2 — aucun libellé ne recoupe la phrase |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C1 / P2-C1-la-societe-depas… | Certes, les occupations des 28 autres ministères ne sont pas vaines ou sans importance. | 28 | `absent` | — | même valeur portée par P-D-050 — aucun libellé ne recoupe la phrase |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C2 / P2-C2-seul-le-maire-pr… | Le vote des Français parle de lui-même : la participation aux municipales s’établit à 57 %, contre 33 % aux élections régionales et départementales. | 57 % | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C2 / P2-C2-seul-le-maire-pr… | Le vote des Français parle de lui-même : la participation aux municipales s’établit à 57 %, contre 33 % aux élections régionales et départementales. | 33 % | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C3 / P2-C3-et-si-nous-pouvi… | Un appareil public concentré sur 7 missions indispensables nécessite moins d’effectifs. | 7 | `absent` | — | même valeur portée par N-e141-1, R-D6-2-2-p2 — aucun libellé ne recoupe la phrase |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C3 / P2-C3-et-si-nous-pouvi… | Environ 580 000 postes affectés à des missions facultatives, où l’État s’est substitué aux citoyens sans bonne raison, sont à fermer la première anné… | 580 000 postes | `ambigu` | `R-D6-2-1-p1` (580 000) | 1 entrée(s) de même valeur et de libellé partiellement recoupé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C3 / P2-C3-et-si-nous-pouvi… | Cela représente une baisse de 10 % des effectifs publics totaux. | 10 % | `ambigu` | `N-e132-2` (10) | 1 entrée(s) de même valeur et de libellé partiellement recoupé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C3 / P2-C3-les-agents-dont-… | Les agents dont les postes seront supprimés conserveront en indemnités 70 % de leur traitement jusqu’à sept ans après leur départ. | 70 % | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C3 / P2-C3-les-agents-dont-… | C’est 2,5 fois plus généreux que le dispositif actuel en cas de départ volontaire et garantira leur sécurité matérielle. | 2,5 fois | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C3 / P2-C3-le-sens-de-linte… | Les militaires sont même plus de trois fois plus souvent sous contrat que les agents civils des ministères (68 % contre 20 %). | 68 % | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C3 / P2-C3-le-sens-de-linte… | Les militaires sont même plus de trois fois plus souvent sous contrat que les agents civils des ministères (68 % contre 20 %). | 20 % | `absent` | — | même valeur portée par R-D4-3-2-p1, P-D-101 — aucun libellé ne recoupe la phrase |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C3 / P2-C3-le-sens-de-linte… | Leur rémunération sera libérée et augmentée de +13 % grâce au recentrage de l’État. | 13 % | `absent` | — | même valeur portée par R-D3-2-1-p1, R-D3-2-1-e1, R-lexique-restitution-b1, P-D-108 — aucu… |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C3-le-sens-de-linte… | 236 milliards d’euros d’économies | 236 milliards d’euros | `identique` | `R-D2-1-1-e1` (236 Md€/an) | apparié hors ancrage, par la valeur et le libellé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-si-nous-arret… | On s’attendrait ainsi à une majorité franche de « oui » pour disposer d’une justice et de prisons, dont le total coûte 36 euros par mois à chaque foy… | 36 euros | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-si-nous-arret… | On s’attendrait ainsi à une majorité franche de « oui » pour disposer d’une justice et de prisons, dont le total coûte 36 euros par mois à chaque foy… | 115 euros | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-fermons-les-stru… | Sans que leur objet soit blâmable, 750 agences et instances sur 1104 au total coûtent cher alors qu’elles exercent des missions facultatives. | 750 agences | `identique` | `R-D2-2-1-p1` (750 agences) | apparié hors ancrage, par la valeur et le libellé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-fermons-les-stru… | Sans que leur objet soit blâmable, 750 agences et instances sur 1104 au total coûtent cher alors qu’elles exercent des missions facultatives. | 1104 | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-fermons-les-stru… | Les établissements publics qui gèrent un patrimoine public et des revenus propres pourront rester autonomes, soit environ 300 musées, universités et… | 300 | `identique` | `R-D2-3-2-p1` (≈ 300) | apparié hors ancrage, par la valeur et le libellé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-baisser-les-impo… | Les Français préféreront toujours recevoir des billets bleus indiquant 20 euros sur un décor gothique et libres d’emploi, plutôt que des tickets de r… | 20 euros | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-restituer-600-eu… | Restituer 600 euros par mois | 600 euros | `identique` | `R-D3-2-2-e1` (600 €/mois) | apparié hors ancrage, par la valeur et le libellé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-restituer-600-eu… | Concentrer l’État sur ses 7 missions indispensables conduit à économiser 236 milliards d’euros en année pleine. | 7 | `absent` | — | même valeur portée par N-e141-1, R-D6-2-2-p2 — aucun libellé ne recoupe la phrase |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-restituer-600-eu… | Concentrer l’État sur ses 7 missions indispensables conduit à économiser 236 milliards d’euros en année pleine. | 236 milliards d’euros | `absent` | — | même valeur portée par R-D2-1-1-e1 — aucun libellé ne recoupe la phrase |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-restituer-600-eu… | Cela représente 14 % des dépenses publiques actuelles, sans affecter la santé ni l’éducation. | 14 % | `absent` | — | même valeur portée par N-e135-3 — aucun libellé ne recoupe la phrase |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-restituer-600-eu… | Rendre l’intégralité de ces dépenses non réalisées représente un gain total de 600 euros par mois pour un salarié type. | 600 euros | `identique` | `R-D3-2-2-e1` (600 €/mois) | apparié hors ancrage, par la valeur et le libellé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-si-on-augment… | Et si on augmentait tous les salaires nets de +13 % en un an ? | 13 % | `ambigu` | `R-D3-2-1-p1` (+13) | 4 entrées de même valeur et de libellé proche |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-si-on-augment… | Nous proposons ainsi d’augmenter tous les salaires nets de +13 % en un an. | 13 % | `ambigu` | `R-D3-2-1-p1` (+13) | 4 entrées de même valeur et de libellé proche |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-si-on-augment… | Le salarié type verra son salaire net s’accroître de 300 euros nets par mois et le SMIC net augmentera de 180 euros par mois. | 300 euros | `ambigu` | `R-lexique-restitution-b2` (300 €/mois) | 1 entrée(s) de même valeur et de libellé partiellement recoupé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-si-on-augment… | Le salarié type verra son salaire net s’accroître de 300 euros nets par mois et le SMIC net augmentera de 180 euros par mois. | 180 euros | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-si-on-augment… | Pour un bénéficiaire moyen, cela représente environ 80 euros par mois en moins, contre 300 euros de salaire mensuel en plus, soit un gain net de 220… | 80 euros | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-si-on-augment… | Pour un bénéficiaire moyen, cela représente environ 80 euros par mois en moins, contre 300 euros de salaire mensuel en plus, soit un gain net de 220… | 300 euros | `ambigu` | `R-lexique-restitution-b2` (300 €/mois) | 1 entrée(s) de même valeur et de libellé partiellement recoupé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-si-on-augment… | Pour un bénéficiaire moyen, cela représente environ 80 euros par mois en moins, contre 300 euros de salaire mensuel en plus, soit un gain net de 220… | 220 euros | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-si-on-augment… | C’est surtout la liberté d’utiliser ces 80 euros perçus en euros sonnants et trébuchants sans contrainte plutôt qu’au format formulaire. | 80 euros | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-investir-dans-so… | Un travailleur type recevra 300 euros par mois d’épargne personnelle en plus du salaire net. | 300 euros | `ambigu` | `R-lexique-restitution-b2` (300 €/mois) | 1 entrée(s) de même valeur et de libellé partiellement recoupé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-les-normes-soccu… | Le code du travail fait mieux, ou plutôt pire : il compte plus de 11 000 articles, soit le double du code de l’environnement. | 11 000 articles | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-les-normes-soccu… | Il pourra contrôler efficacement 2 règles au lieu de se disperser entre 20 règles mal appliquées. | 2 | `absent` | — | même valeur portée par N-e6-1, N-e14-1, R-D11-4-2-p1 — aucun libellé ne recoupe la phrase |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-les-normes-soccu… | Il pourra contrôler efficacement 2 règles au lieu de se disperser entre 20 règles mal appliquées. | 20 | `absent` | — | même valeur portée par R-D4-3-2-p1, P-D-101 — aucun libellé ne recoupe la phrase |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-faisons-simple | Le système fiscal estonien est un modèle de clarté : 4 impôts et un taux unique (22 %), premier pays au classement mondial de la compétitivité fiscal… | 4 impôts | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-faisons-simple | Le système fiscal estonien est un modèle de clarté : 4 impôts et un taux unique (22 %), premier pays au classement mondial de la compétitivité fiscal… | 22 % | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-supprimons-toute… | Supprimons toutes ces taxes en trop et fusionnons-les en 4 impôts bien connus. 75 % des recettes budgétaires reposent déjà sur seulement ces 4 impôts. | 4 impôts | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-supprimons-toute… | Supprimons toutes ces taxes en trop et fusionnons-les en 4 impôts bien connus. 75 % des recettes budgétaires reposent déjà sur seulement ces 4 impôts. | 75 % | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-supprimons-toute… | Supprimons toutes ces taxes en trop et fusionnons-les en 4 impôts bien connus. 75 % des recettes budgétaires reposent déjà sur seulement ces 4 impôts. | 4 impôts | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-supprimons-toute… | À la place des taxes et taux réduits qui se cumulent et s’annulent, imposons une TVA unique au taux actuel de 20 %. | 20 % | `identique` | `R-D4-3-2-p1` (20) | apparié hors ancrage, par la valeur et le libellé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-supprimons-toute… | Remplaçons les impôts cachés, comme les « frais de notaire » et les « droits de succession » qui masquent des impôts taxant la jeunesse comme la mort… | 60 % | `absent` | — |  |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-supprimons-toute… | Le coût des produits produits en France, qui représentent 81 % de la consommation moyenne, baissera. | 81 % | `identique` | `R-D4-3-3-e1` (81 %) | apparié hors ancrage, par la valeur et le libellé |
| SAUVONS L’ÉTAT DE LUI-MÊME / P2-C5 / P2-C5-la-baisse-nette-… | La baisse nette des impôts réduira le taux de prélèvement obligatoire à 36 % de la richesse produite. | 36 % | `identique` | `R-D11-e1` (36 %) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-cotisons-vra… | Plus de débat politique incessant entre 62 et 64 ans pour ce qui est d’abord une étape intime de vie. | 62 | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-cotisons-vra… | Plus de débat politique incessant entre 62 et 64 ans pour ce qui est d’abord une étape intime de vie. | 64 ans | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-cotisons-vra… | Le travail revalorisé de +13 % permet de partir plus tôt, ou de gagner plus en partant plus tard. | 13 % | `absent` | — | même valeur portée par R-D3-2-1-p1, R-D3-2-1-e1, R-lexique-restitution-b1, P-D-108 — aucu… |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-epargner-ses… | Nous proposons que cette épargne retraite personnelle s’ajoute à un socle contributif par répartition avec une pension de base égale à 1 100 euros pa… | 1 100 euros | `identique` | `R-D8-2-1-p1` (1 100) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | Nous proposons de transférer un montant de 20 000 euros pour chaque foyer. | 20 000 euros | `identique` | `R-D7-2-1-p1` (20 000) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | Ce montant représente 16 % du patrimoine net d’un foyer type, pour un patrimoine public non essentiel à céder estimé à au moins 600 milliards d’euros. | 16 % | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | Ce montant représente 16 % du patrimoine net d’un foyer type, pour un patrimoine public non essentiel à céder estimé à au moins 600 milliards d’euros. | 600 milliards d’euros | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | Cette somme est réaliste : elle ne représente que 13 % du patrimoine des administrations publiques estimé au total à 4 500 milliards d’euros par l’In… | 13 % | `absent` | — | même valeur portée par R-D3-2-1-p1, R-D3-2-1-e1, R-lexique-restitution-b1, P-D-108 — aucu… |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | Cette somme est réaliste : elle ne représente que 13 % du patrimoine des administrations publiques estimé au total à 4 500 milliards d’euros par l’In… | 4 500 milliards d’euros | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | L’État immobilise 97 millions de mètres carrés au niveau central, dont près de la moitié en bureaux et logements. | 97 millions | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | On en compte 5 fois plus au niveau local. | 5 fois | `absent` | — | même valeur portée par P-D-058 — aucun libellé ne recoupe la phrase |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | Ces bâtiments sont sous-occupés d’au moins 36 %. | 36 % | `absent` | — | même valeur portée par N-e106-2, R-D11-e1 — aucun libellé ne recoupe la phrase |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | L’État gère mal notre argent : de 2013 à 2023, le rendement de l’agence des participations de l’État (APE) a été de 5,3 % par an contre 9,8 % pour le… | 5,3 % | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | L’État gère mal notre argent : de 2013 à 2023, le rendement de l’agence des participations de l’État (APE) a été de 5,3 % par an contre 9,8 % pour le… | 9,8 % | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | Cumulé sur dix ans, cette perte de 4,5 % de rendement annuel se transforme grâce aux intérêts composés en un écart de richesse de 52 %. | 4,5 % | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-nous-detenon… | Cumulé sur dix ans, cette perte de 4,5 % de rendement annuel se transforme grâce aux intérêts composés en un écart de richesse de 52 %. | 52 % | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-la-grande-re… | Cette transition progressive aura un effet positif immédiat : +25 % d’offre sur le marché locatif privé, un flux annuel de transactions immobilières… | 25 % | `identique` | `R-D7-3-1-e1` (+25 %) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C1 / P3-C1-la-grande-re… | Transformer ce capital en revenu viager représenterait pour les retraités actuels un complément de retraite d’au moins 500 euros par an par personne,… | 500 euros | `identique` | `R-D7-2-2-e1` (500 €/an) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C2 / P3-C2-une-aide-fon… | Une aide fondamentale universelle de 550 euros par mois remplace toutes les aides actuelles, sociales et fiscales. | 550 euros | `identique` | `R-D9-2-1-p1` (550) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C2 / P3-C2-assurer-le-g… | Chaque travailleur verra son revenu net imposé à un taux unique estimé à 23 % ( et conservera le plein bénéfice de l’aide fondamentale versée à tous… | 23 % | `identique` | `R-D9-3-1-p1` (23) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C2 / P3-C2-assurer-le-g… | Ce système lui garantit qu’il percevra 77 centimes nets à chaque euro gagné, en plus de 550 euros par mois d’aide fondamentale fixe. | 77 centimes | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C2 / P3-C2-assurer-le-g… | Ce système lui garantit qu’il percevra 77 centimes nets à chaque euro gagné, en plus de 550 euros par mois d’aide fondamentale fixe. | 550 euros | `identique` | `R-D9-2-1-p1` (550) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C2 / P3-C2-chaque-enfan… | Une aide universelle égale à 275 euros par mois pour chaque enfant de sa naissance à ses 18 ans remplace toutes les allocations sociales et les avant… | 275 euros | `identique` | `R-D9-4-1-p1` (275) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C2 / P3-C2-chaque-enfan… | Une aide universelle égale à 275 euros par mois pour chaque enfant de sa naissance à ses 18 ans remplace toutes les allocations sociales et les avant… | 18 ans | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C3 / P3-C3-et-si-nous-p… | Plus grave, nous sommes mal classés s’agissant de la mortalité infantile, meilleur signe de notre capacité à protéger les plus fragiles : 23e sur 27… | 27 | `absent` | — | même valeur portée par N-e63-1 — aucun libellé ne recoupe la phrase |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C3 / P3-C3-limpot-doit-… | Pour les soins critiques, un bouclier sanitaire rassure et responsabilise chaque citoyen en rendant le reste à charge prévisible et soutenable : 10 %… | 10 % | `ambigu` | `R-D8-4-1-p1` (10 %) | 2 entrées de même valeur et de libellé proche |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C3 / P3-C3-limpot-doit-… | Pour les soins critiques, un bouclier sanitaire rassure et responsabilise chaque citoyen en rendant le reste à charge prévisible et soutenable : 10 %… | 5 % | `absent` | — | même valeur portée par P-D-058, P-D-096 — aucun libellé ne recoupe la phrase |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C3 / P3-C3-choisissons-… | La fin des doublons entre sécurité sociale et mutuelles, qui traitent aujourd’hui deux fois les mêmes dossiers pour quelques centimes, fera même écon… | 300 euros | `identique` | `R-D8-4-2-e1` (300 €/an) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C3 / P3-C3-arretons-la-… | La Cour des comptes note que plusieurs hôpitaux publics « ont proposé des missions de 24 heures à plus de 2 700 euros bruts » à des médecins et signa… | 24 heures | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C3 / P3-C3-arretons-la-… | La Cour des comptes note que plusieurs hôpitaux publics « ont proposé des missions de 24 heures à plus de 2 700 euros bruts » à des médecins et signa… | 2 700 euros | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C3 / P3-C3-soyons-seuls… | Mieux rémunérer de +13 % nets tous les soignants grâce à la restitution des économies sur les feuilles de paie viabilisera partout un service de qual… | 13 % | `ambigu` | — | 2 entrée(s) de même valeur et de libellé partiellement recoupé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C4 / P3-C4-chaque-eleve… | En plus de l’aide fondamentale universelle de 275 euros par mois, versons à chaque enfant 6 600 euros par an sur un compte éducation à son nom, géré… | 275 euros | `identique` | `R-D9-4-1-p1` (275) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C4 / P3-C4-chaque-eleve… | En plus de l’aide fondamentale universelle de 275 euros par mois, versons à chaque enfant 6 600 euros par an sur un compte éducation à son nom, géré… | 6 600 euros | `identique` | `R-D10-2-1-p1` (6 600) | apparié hors ancrage, par la valeur et le libellé |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C4 / P3-C4-chaque-eleve… | Le coût normal d’une école sera largement couvert : 139 000 euros par an pour une classe de 21 élèves (moyenne OCDE au primaire, contre 22 en France)… | 139 000 euros | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C4 / P3-C4-chaque-eleve… | Le coût normal d’une école sera largement couvert : 139 000 euros par an pour une classe de 21 élèves (moyenne OCDE au primaire, contre 22 en France)… | 21 élèves | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C4 / P3-C4-chaque-eleve… | Le coût normal d’une école sera largement couvert : 139 000 euros par an pour une classe de 21 élèves (moyenne OCDE au primaire, contre 22 en France)… | 22 | `absent` | — |  |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C4 / P3-C4-chaque-eleve… | Le salaire net moyen des enseignants sera maintenu et augmenté de +13 % grâce à la restitution. | 13 % | `absent` | — | même valeur portée par R-D3-2-1-p1, R-D3-2-1-e1, R-lexique-restitution-b1, P-D-108 — aucu… |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C4 / P3-C4-chaque-eleve… | Cela permettra d’attirer les meilleurs plutôt que de diminuer les critères d’admission pour remplir des classes à la hâte : la barre d’admissibilité… | 5 | `absent` | — | même valeur portée par P-D-058, P-D-096 — aucun libellé ne recoupe la phrase |
| CHOISISSONS UN AVENIR MEILLEUR / P3-C4 / P3-C4-chaque-eleve… | Cela permettra d’attirer les meilleurs plutôt que de diminuer les critères d’admission pour remplir des classes à la hâte : la barre d’admissibilité… | 20 | `absent` | — | même valeur portée par R-D4-3-2-p1, P-D-101 — aucun libellé ne recoupe la phrase |
| Alors peut-être… / epilogue-C1 / epilogue-C1-un-etat-qui-se… | Les Français le savent et épargnent au niveau record de 18 % en vue de lendemains qui déchantent, dans le même temps leur État est en déficit depuis… | 18 % | `absent` | — | même valeur portée par N-e139-1 — aucun libellé ne recoupe la phrase |
| Alors peut-être… / epilogue-C1 / epilogue-C1-un-etat-qui-se… | Les Français le savent et épargnent au niveau record de 18 % en vue de lendemains qui déchantent, dans le même temps leur État est en déficit depuis… | 52 ans | `absent` | — |  |
| Alors peut-être… / epilogue-C1 / epilogue-C1-un-etat-qui-se… | Nos finances publiques sont dans un état grave : 5 500 euros de dette publique en plus par an par foyer français. | 5 500 euros | `identique` | `R-D11-1-1-p1` (5 500) | apparié hors ancrage, par la valeur et le libellé |
| Alors peut-être… / epilogue-C1 / epilogue-C1-le-privilege-d… | Elle fut de 17,5 % en 1958. | 17,5 % | `absent` | — |  |
| Alors peut-être… / epilogue-C1 / epilogue-C1-le-privilege-d… | Lors du tournant de la rigueur de 1983 de François Mitterrand, la dévaluation cumulée est du même ordre, sous la pression d’un déficit budgétaire alo… | 2,9 % | `absent` | — |  |
| Alors peut-être… / epilogue-C1 / epilogue-C1-le-prix-du-sta… | Pour redresser le déficit au rythme attendu par les traités, il suffit de gagner 1 % d’efficacité sur les dépenses publiques ou de croissance en plus… | 1 % | `absent` | — | même valeur portée par N-e120-2, P-D-026, P-D-030, P-D-052… — aucun libellé ne recoupe la… |
| Alors peut-être… / epilogue-C1 / epilogue-C1-le-prix-du-sta… | La France compte aujourd’hui 62 % de plus de fonctionnaires par habitant qu’en 1962, période de prospérité inédite de l’histoire de France. | 62 % | `absent` | — |  |
| Alors peut-être… / epilogue-C1 / epilogue-C1-et-si-la-franc… | Notre plan repose sur des principes simples et efficaces : concentrer l’État sur 7 missions indispensables, rendre aux Français le fruit de leur trav… | 7 | `absent` | — | même valeur portée par N-e141-1, R-D6-2-2-p2 — aucun libellé ne recoupe la phrase |
| Alors peut-être… / epilogue-C1 / epilogue-C1-et-si-la-franc… | Restituer les 236 milliards d’euros économisés rendra 600 euros au travailleur type sur sa feuille de paie. | 236 milliards d’euros | `absent` | — | même valeur portée par R-D2-1-1-e1 — aucun libellé ne recoupe la phrase |
| Alors peut-être… / epilogue-C1 / epilogue-C1-et-si-la-franc… | Restituer les 236 milliards d’euros économisés rendra 600 euros au travailleur type sur sa feuille de paie. | 600 euros | `identique` | `R-D3-2-2-e1` (600 €/mois) | apparié hors ancrage, par la valeur et le libellé |
| Alors peut-être… / epilogue-C1 / epilogue-C1-dabord-la-meth… | Par exemple, pour les 486 niches fiscales, il faut imaginer autant de dispositions existantes à abroger avec leurs coordinations et leurs phases de t… | 486 niches fiscales | `absent` | — |  |
| Alors peut-être… / epilogue-C1 / epilogue-C1-enfin-les-resu… | Elles seront restituées de manière progressive et croissante, à raison de +2 % de salaire net par mois jusqu’à atteindre +13 % au bout d’un an. | 2 % | `absent` | — | même valeur portée par N-e6-1, N-e14-1 — aucun libellé ne recoupe la phrase |
| Alors peut-être… / epilogue-C1 / epilogue-C1-enfin-les-resu… | Elles seront restituées de manière progressive et croissante, à raison de +2 % de salaire net par mois jusqu’à atteindre +13 % au bout d’un an. | 13 % | `ambigu` | `R-lexique-restitution-b1` (+13 %) | 1 entrée(s) de même valeur et de libellé partiellement recoupé |
| note de fin e4 | Entendu comme un travailleur à temps plein au salaire médian, qui s’élevait à 2 190 € nets en 2024. | 2 190 € | `identique` | `N-e4-1` (2 190 €) |  |
| note de fin e6 | De l’ordre de 2 % de perte de PIB par rapport au scénario contrefactuel, estimé par B. | 2 % | `identique` | `N-e6-1` (De l’ordre de 2 %) |  |
| note de fin e14 | Soulignons en particulier que l’impôt le plus général qui soit, la TVA, est réparti à hauteur d’un quart en faveur de la sécurité sociale, un quart e… | 2 % | `identique` | `N-e14-1` (2 %) |  |
| note de fin e15 | Il est encore élevé même sur des salaires faibles : 41 % pour 1 900 € nets par mois. | 41 % | `identique` | `N-e15-1` (41 %) |  |
| note de fin e15 | Il est encore élevé même sur des salaires faibles : 41 % pour 1 900 € nets par mois. | 1 900 € | `absent` | — |  |
| note de fin e15 | La taxation du travail est ainsi supérieure à celle des autres revenus : 30 % sur les revenus du capital, 14 % sur les pensions de retraites, 6 % sur… | 30 % | `identique` | `N-e15-2` (30 %) |  |
| note de fin e15 | La taxation du travail est ainsi supérieure à celle des autres revenus : 30 % sur les revenus du capital, 14 % sur les pensions de retraites, 6 % sur… | 14 % | `absent` | — | même valeur portée par N-e135-3 — aucun libellé ne recoupe la phrase |
| note de fin e15 | La taxation du travail est ainsi supérieure à celle des autres revenus : 30 % sur les revenus du capital, 14 % sur les pensions de retraites, 6 % sur… | 6 % | `absent` | — |  |
| note de fin e16 | Rapport d’évaluation des politiques de sécurité sociale, Annexe 1 financement, 2.6.2 du projet de loi d’approbation des comptes de la sécurité social… | 1 | `absent` | — | même valeur portée par N-e120-2, P-D-026, P-D-030, P-D-052… — aucun libellé ne recoupe la… |
| note de fin e16 | Rapport d’évaluation des politiques de sécurité sociale, Annexe 1 financement, 2.6.2 du projet de loi d’approbation des comptes de la sécurité social… | 2.6 | `absent` | — |  |
| note de fin e18 | Voir Jean-Christophe Savineau La contribution sur les portes et fenêtres : un impôt sur l’air et la lumière, dans Gestion & Finances Publiques 2017/5… | 5 | `absent` | — | même valeur portée par P-D-058, P-D-096 — aucun libellé ne recoupe la phrase |
| note de fin e18 | Voir Jean-Christophe Savineau La contribution sur les portes et fenêtres : un impôt sur l’air et la lumière, dans Gestion & Finances Publiques 2017/5… | 116 | `absent` | — |  |
| note de fin e26 | Cross-Sectional Evidence on Satiation and Cross-Country Heterogeneity, Soc Indic Res 179, 677–688, juin 2025 | 677 | `absent` | — |  |
| note de fin e29 | Par exemple, les frais de gestion de l’agence du Pass’ culture sont de 8,5 %. | 8,5 % | `identique` | `N-e29-1` (8,5 %) |  |
| note de fin e32 | Une perte de PIB de 3,94 % pour la sphère privée est documentée par Pellegrino et Zheng, et une perte de productivité de la sphère publique d’environ… | 3,94 % | `identique` | `N-e32-1` (3,94 %) |  |
| note de fin e35 | Le taux implicite moyen d’impôt sur les sociétés mesuré par l’Insee s’établissait à 21,4 % pour les petites et moyennes entreprises (PME) contre 14,3… | 21,4 % | `identique` | `N-e35-1` (21,4 %) |  |
| note de fin e35 | Le taux implicite moyen d’impôt sur les sociétés mesuré par l’Insee s’établissait à 21,4 % pour les petites et moyennes entreprises (PME) contre 14,3… | 14,3 % | `absent` | — |  |
| note de fin e38 | Voir à ce sujet par exemple, parmi d’autres scandales d’attribution de marchés publics ou de logement social, le cas de l’OPH de Bobigny, dont les ir… | 18 millions d’euros | `absent` | — |  |
| note de fin e40 | « Le début d’année 2022 a été marquée par la fin du procès, à Rennes, d’un réseau de onze personnes, dont plusieurs dockers employés par TGO, impliqu… | 140 kg | `absent` | — |  |
| note de fin e46 | Ainsi « 92 % des chefs d’établissement du second degré ont déjà été alertés par leurs personnels ou leurs élèves au sujet de la température des salle… | 92 % | `identique` | `N-e46-1` (92 %) |  |
| note de fin e48 | On apprend dans une note de l’Observatoire des violences envers les femmes de la Seine-Saint-Denis que sur 101 dossiers de victimes mineures de prost… | 101 | `absent` | — |  |
| note de fin e48 | On apprend dans une note de l’Observatoire des violences envers les femmes de la Seine-Saint-Denis que sur 101 dossiers de victimes mineures de prost… | 15 ans | `absent` | — |  |
| note de fin e48 | On apprend dans une note de l’Observatoire des violences envers les femmes de la Seine-Saint-Denis que sur 101 dossiers de victimes mineures de prost… | 15 ans | `absent` | — |  |
| note de fin e48 | On apprend dans une note de l’Observatoire des violences envers les femmes de la Seine-Saint-Denis que sur 101 dossiers de victimes mineures de prost… | 13 ans | `absent` | — |  |
| note de fin e60 | « avec près de 2 600 articles, [le code de l’urbanismes comporte] désormais plus de dispositions consacrées aux modes d’élaboration des documents d’u… | 2 600 articles | `absent` | — |  |
| note de fin e61 | Ifrap, La liste des 438 taxes, impôts, contributions et cotisations en France, 2026. | 438 taxes | `absent` | — |  |
| note de fin e62 | Voir le bulletin officiel des finances publiques sur le sujet. https://bofip.impots.gouv.fr/bofip/2033-PGP.html/identifiant=BOI-TVA-LIQ-30-10-10-2024… | 2 | `absent` | — | même valeur portée par N-e6-1, N-e14-1, R-D11-4-2-p1 — aucun libellé ne recoupe la phrase |
| note de fin e63 | Calcul Résolution, à partir de la hausse en volume de +27 % intervenue en 2026 et du rapport sur la 5e période par la Cour des comptes, Les certifica… | 27 % | `identique` | `N-e63-1` (+27 %) |  |
| note de fin e63 | Ce rapport chiffre le coût total des CEE à 6 milliards d’euros annuels avant la hausse de janvier 2026. | 6 milliards d’euros | `identique` | `N-e63-2` (6 milliards) |  |
| note de fin e65 | Par exemple, l’estimation du coût du « pacte Dutreil » a été multiplié par 10 d’une année sur l’autre, passant de 0,5 à 5 milliards d’euros. | 10 | `identique` | `N-e65-1` (10) |  |
| note de fin e65 | Par exemple, l’estimation du coût du « pacte Dutreil » a été multiplié par 10 d’une année sur l’autre, passant de 0,5 à 5 milliards d’euros. | 0,5 | `absent` | — | même valeur portée par N-e97-1 — aucun libellé ne recoupe la phrase |
| note de fin e65 | Par exemple, l’estimation du coût du « pacte Dutreil » a été multiplié par 10 d’une année sur l’autre, passant de 0,5 à 5 milliards d’euros. | 5 milliards d’euros | `absent` | — |  |
| note de fin e71 | La revue de dépenses sur l’hébergement d’urgence de juillet 2025 précise dans son encadré 6 que sur 100 000 personnes au statut connu, 39 000 sont en… | 6 | `absent` | — | même valeur portée par R-D8-3-1-p1, P-D-059 — aucun libellé ne recoupe la phrase |
| note de fin e71 | La revue de dépenses sur l’hébergement d’urgence de juillet 2025 précise dans son encadré 6 que sur 100 000 personnes au statut connu, 39 000 sont en… | 100 000 personnes | `absent` | — |  |
| note de fin e71 | La revue de dépenses sur l’hébergement d’urgence de juillet 2025 précise dans son encadré 6 que sur 100 000 personnes au statut connu, 39 000 sont en… | 39 000 | `absent` | — |  |
| note de fin e71 | La revue de dépenses sur l’hébergement d’urgence de juillet 2025 précise dans son encadré 6 que sur 100 000 personnes au statut connu, 39 000 sont en… | 13 000 | `absent` | — |  |
| note de fin e71 | La revue de dépenses sur l’hébergement d’urgence de juillet 2025 précise dans son encadré 6 que sur 100 000 personnes au statut connu, 39 000 sont en… | 8 200 | `absent` | — |  |
| note de fin e71 | La revue de dépenses sur l’hébergement d’urgence de juillet 2025 précise dans son encadré 6 que sur 100 000 personnes au statut connu, 39 000 sont en… | 60 % | `absent` | — |  |
| note de fin e74 | En 2024, les pensions de retraites versées, y compris droits dérivés, charges de gestion et action sociale, se sont élevées à 407 milliards d’euros,… | 407 milliards d’euros | `absent` | — |  |
| note de fin e74 | En 2024, les pensions de retraites versées, y compris droits dérivés, charges de gestion et action sociale, se sont élevées à 407 milliards d’euros,… | 282 milliards d’euros | `identique` | `P-D-064` (282,4 Md€) | apparié hors ancrage, par la valeur et le libellé |
| note de fin e75 | A 10,9 % pour les retraités contre 20,6 % pour les moins de 18 ans en 2021. | 10,9 % | `identique` | `N-e75-1` (10,9 %) |  |
| note de fin e75 | A 10,9 % pour les retraités contre 20,6 % pour les moins de 18 ans en 2021. | 20,6 % | `absent` | — |  |
| note de fin e75 | A 10,9 % pour les retraités contre 20,6 % pour les moins de 18 ans en 2021. | 18 ans | `absent` | — |  |
| note de fin e76 | Le niveau de vie moyen des retraités était estimé à 1 994 € par mois contre 2 226 € pour les actifs en 2022. | 1 994 € | `identique` | `N-e76-1` (1 994 €) |  |
| note de fin e76 | Le niveau de vie moyen des retraités était estimé à 1 994 € par mois contre 2 226 € pour les actifs en 2022. | 2 226 € | `absent` | — |  |
| note de fin e78 | « La part des parents créanciers victimes d’impayés de pension a fait l’objet d’estimations à partir d’enquêtes ou de données administratives, qui va… | 25 % | `identique` | `N-e78-1` (25 %) |  |
| note de fin e78 | « La part des parents créanciers victimes d’impayés de pension a fait l’objet d’estimations à partir d’enquêtes ou de données administratives, qui va… | 40 % | `absent` | — | même valeur portée par N-e83-1 — aucun libellé ne recoupe la phrase |
| note de fin e79 | La moyenne de l’OCDE s’élève à 10,2 % en moyenne et des meilleures performances dépassant 15 %. | 10,2 % | `identique` | `N-e79-1` (10,2 %) |  |
| note de fin e79 | La moyenne de l’OCDE s’élève à 10,2 % en moyenne et des meilleures performances dépassant 15 %. | 15 % | `absent` | — | même valeur portée par N-e118-2, R-D7-3-1-p1 — aucun libellé ne recoupe la phrase |
| note de fin e81 | Données de la fiche 13 de L’Etat de l’école 2025, Direction de l'évaluation, de la prospective et de la performance (Depp). | 13 | `absent` | — | même valeur portée par R-D3-2-1-p1, R-D3-2-1-e1, R-lexique-restitution-b1, P-D-108 — aucu… |
| note de fin e83 | A 40 % contre 60 %. | 40 % | `identique` | `N-e83-1` (40 %) |  |
| note de fin e83 | A 40 % contre 60 %. | 60 % | `absent` | — |  |
| note de fin e92 | Entre 10 et 13 % pour les communes de plus de 100 000 habitants contre 21 à 23 % pour celles de moins de 3 500 habitants. | 10 | `identique` | `N-e92-1` (10) |  |
| note de fin e92 | Entre 10 et 13 % pour les communes de plus de 100 000 habitants contre 21 à 23 % pour celles de moins de 3 500 habitants. | 13 % | `absent` | — | même valeur portée par R-D3-2-1-p1, R-D3-2-1-e1, R-lexique-restitution-b1, P-D-108 — aucu… |
| note de fin e92 | Entre 10 et 13 % pour les communes de plus de 100 000 habitants contre 21 à 23 % pour celles de moins de 3 500 habitants. | 100 000 habitants | `absent` | — |  |
| note de fin e92 | Entre 10 et 13 % pour les communes de plus de 100 000 habitants contre 21 à 23 % pour celles de moins de 3 500 habitants. | 21 | `absent` | — |  |
| note de fin e92 | Entre 10 et 13 % pour les communes de plus de 100 000 habitants contre 21 à 23 % pour celles de moins de 3 500 habitants. | 23 % | `absent` | — | même valeur portée par R-D9-3-1-p1 — aucun libellé ne recoupe la phrase |
| note de fin e92 | Entre 10 et 13 % pour les communes de plus de 100 000 habitants contre 21 à 23 % pour celles de moins de 3 500 habitants. | 3 500 habitants | `absent` | — |  |
| note de fin e92 | Cour des comptes, annexe 12 de Les finances publiques locales, juillet 2024. | 12 | `identique` | `N-e92-2` (12) |  |
| note de fin e93 | Au sens de l’article L553-1 du code de la fonction publique, notamment son 4°. | 4 | `absent` | — |  |
| note de fin e97 | L’estimation repose sur les hypothèses prudentes suivantes : multiplicateur de 0,5 sur les assiettes économiques optimisables (hors revenus de rempla… | 0,5 | `identique` | `N-e97-1` (0,5) |  |
| note de fin e97 | L’estimation repose sur les hypothèses prudentes suivantes : multiplicateur de 0,5 sur les assiettes économiques optimisables (hors revenus de rempla… | 30 Md€ | `identique` | `N-e97-2` (de l’ordre de 30 Md€) |  |
| note de fin e97 | Le solde de la suppression de l’intégralité des niches après restitution de 52 milliards d’euros aux travailleurs est restitué au sein de la refonte… | 52 milliards d’euros | `identique` | `N-e97-3` (52 milliards) |  |
| note de fin e98 | PLACSS 2024, Annexe 1 ; | 1 | `absent` | — | même valeur portée par N-e120-2, P-D-026, P-D-030, P-D-052… — aucun libellé ne recoupe la… |
| note de fin e98 | Projet de loi de finances (PLF) pour 2026, Voies et moyens Tomes 1 et 2, projets annuels de performance (PAP) ; | 1 | `absent` | — | même valeur portée par N-e120-2, P-D-026, P-D-030, P-D-052… — aucun libellé ne recoupe la… |
| note de fin e98 | Projet de loi de finances (PLF) pour 2026, Voies et moyens Tomes 1 et 2, projets annuels de performance (PAP) ; | 2 | `absent` | — | même valeur portée par N-e6-1, N-e14-1, R-D11-4-2-p1 — aucun libellé ne recoupe la phrase |
| note de fin e99 | Au niveau du salaire médian, qui représente la limite entre les 50 % les mieux payés et les 50 % les moins bien payés. | 50 % | `identique` | `N-e99-1` (50 %) |  |
| note de fin e99 | Au niveau du salaire médian, qui représente la limite entre les 50 % les mieux payés et les 50 % les moins bien payés. | 50 % | `identique` | `N-e99-1` (50 %) |  |
| note de fin e99 | Il s’élevait en 2024 à 2190 € nets par mois. | 2190 € | `identique` | `N-e4-1` (2 190 €) | apparié hors ancrage, par la valeur et le libellé |
| note de fin e103 | Le taux des récidivistes légaux en part des condamnés a été multiplié par 10 entre 1989 et 2023, tant s’agissant des crimes que des délits. | 10 | `absent` | — | même valeur portée par N-e65-1, N-e92-1, N-e120-1, N-e125-1… — aucun libellé ne recoupe l… |
| note de fin e103 | Données issues du Service statistique du ministère de la Justice, Justice pénale, Fiche 11 Le traitement judiciaire des auteurs d’infractions pénales… | 11 | `absent` | — |  |
| note de fin e106 | Selon leurs estimations, qui reposent sur le International Tax Competitiveness Index (ITCI) de la Tax Foundation, et nos calculs, passer de la comple… | 5 points | `absent` | — | même valeur portée par P-D-058, P-D-096 — aucun libellé ne recoupe la phrase |
| note de fin e107 | Les taxes spécifiques à supprimer représentent une charge de 16 milliards d’euros par an. | 16 milliards d’euros | `identique` | `N-e107-1` (16 milliards) |  |
| note de fin e107 | Elles sont souvent du même ordre de grandeur que les taux réduits de TVA (la complexité en plus) : redevances sur l’eau (2,1 milliards d’euros), taxe… | 2,1 milliards d’euros | `identique` | `N-e107-2` (2,1 milliards) |  |
| note de fin e107 | Elles sont souvent du même ordre de grandeur que les taux réduits de TVA (la complexité en plus) : redevances sur l’eau (2,1 milliards d’euros), taxe… | 1,9 milliard d’euros | `absent` | — | même valeur portée par R-D2-2-1-s5 — aucun libellé ne recoupe la phrase |
| note de fin e107 | Elles sont souvent du même ordre de grandeur que les taux réduits de TVA (la complexité en plus) : redevances sur l’eau (2,1 milliards d’euros), taxe… | 0,8 milliard d’euros | `absent` | — |  |
| note de fin e108 | Au moment de la transmission, une franchise d’impôt de l’ordre de 3 % s’appliquera, comme avance sur la taxation de la réalisation de la plus-value. | 3 % | `identique` | `N-e108-1` (de l’ordre de 3 %) |  |
| note de fin e109 | Les taxes sur la main d’œuvre à supprimer outre la CSG et CRDS activité pèsent 48 milliards d’euros. | 48 milliards d’euros | `identique` | `N-e109-1` (48 milliards) |  |
| note de fin e114 | Définie comme le ratio entre l’objectif officiel de surface utile brute (SUB) par poste de 16 m2 sur la SUB moyenne constatée de 25 m2 renseignée en… | 16 m2 | `absent` | — |  |
| note de fin e114 | Définie comme le ratio entre l’objectif officiel de surface utile brute (SUB) par poste de 16 m2 sur la SUB moyenne constatée de 25 m2 renseignée en… | 25 m2 | `absent` | — | même valeur portée par R-D9-4-2-p2 — aucun libellé ne recoupe la phrase |
| note de fin e118 | L’actif net des organismes HLM (4,8 millions de logements) est estimé à 340 milliards d’euros. | 4,8 millions | `identique` | `N-e118-1` (4,8 millions) |  |
| note de fin e118 | L’actif net des organismes HLM (4,8 millions de logements) est estimé à 340 milliards d’euros. | 340 milliards d’euros | `absent` | — |  |
| note de fin e118 | La valorisation prend pour hypothèse prudente un socle de 15 % conservé et une décote de liquidité de 15 %. | 15 % | `identique` | `N-e118-2` (15 %) |  |
| note de fin e118 | La valorisation prend pour hypothèse prudente un socle de 15 % conservé et une décote de liquidité de 15 %. | 15 % | `identique` | `N-e118-2` (15 %) |  |
| note de fin e118 | Soit environ 200 Md€ de produits de cession à restituer sur ces logements, incluant ceux détenus par les administrations publiques pour leurs agents. | 200 Md€ | `identique` | `N-e118-3` (environ 200 Md€) |  |
| note de fin e118 | Elle passera par une convergence progressive des loyers vers les loyers de marché, et par une limitation du bail à une durée alignée sur le cadre pri… | 3 ans | `identique` | `N-e118-4` (3 ans) |  |
| note de fin e119 | Sous l’hypothèse prudente de 3 % de rendement net et d’une durée de retraite de 24 ans. | 3 % | `identique` | `N-e119-1` (3 %) |  |
| note de fin e119 | Sous l’hypothèse prudente de 3 % de rendement net et d’une durée de retraite de 24 ans. | 24 ans | `absent` | — |  |
| note de fin e120 | Une des principales niches fiscales est l’abattement dit « Papon » de 10 % sur les pensions de retraite, pour un coût estimé à 4,8 milliards d’euros… | 10 % | `identique` | `N-e120-1` (10 %) |  |
| note de fin e120 | Une des principales niches fiscales est l’abattement dit « Papon » de 10 % sur les pensions de retraite, pour un coût estimé à 4,8 milliards d’euros… | 4,8 milliards d’euros | `absent` | — |  |
| note de fin e120 | Cette niche bénéficie seulement aux retraités redevables de l’impôt sur le revenu, pour un gain généralement inférieur à 1 % du revenu. | 1 % | `identique` | `N-e120-2` (1 %) |  |
| note de fin e123 | Les retraites à moins de 1200 € pour une carrière complète ne sont ainsi pas touchées par la refonte de la fiscalité. | 1200 € | `identique` | `N-e123-1` (1200 €) |  |
| note de fin e123 | Les retraites au-delà de 1600 € par mois subissent une baisse nette d’environ 6 %, et une baisse intermédiaire entre les deux. | 1600 € | `identique` | `N-e123-2` (1600 €) |  |
| note de fin e123 | Les retraites au-delà de 1600 € par mois subissent une baisse nette d’environ 6 %, et une baisse intermédiaire entre les deux. | 6 % | `absent` | — |  |
| note de fin e125 | Aujourd’hui, seuls environ 10 % de l’aide médicale d’Etat sont dédiés aux « soins urgents » d’après les données disponibles. | 10 % | `identique` | `N-e125-1` (environ 10 %) |  |
| note de fin e129 | Calcul Résolution, à partir des frais de gestion des mutuelles et des administrations de sécurité sociale et du ministère de la santé, qui s’élèvent… | 16,9 milliards d’euros | `identique` | `N-e129-1` (16,9 milliards) |  |
| note de fin e130 | Bien que conscients de l’illégalité et du caractère répréhensible du non-respect des plafonds réglementaires en termes de rémunération, les hôpitaux,… | 559 | `identique` | `N-e130-1` (559) |  |
| note de fin e130 | Bien que conscients de l’illégalité et du caractère répréhensible du non-respect des plafonds réglementaires en termes de rémunération, les hôpitaux,… | 662 millions d’euros | `absent` | — |  |
| note de fin e130 | Bien que conscients de l’illégalité et du caractère répréhensible du non-respect des plafonds réglementaires en termes de rémunération, les hôpitaux,… | 43 | `absent` | — |  |
| note de fin e130 | Bien que conscients de l’illégalité et du caractère répréhensible du non-respect des plafonds réglementaires en termes de rémunération, les hôpitaux,… | 50 % | `absent` | — | même valeur portée par N-e99-1, P-D-109 — aucun libellé ne recoupe la phrase |
| note de fin e132 | Il est supérieur au seuil où les performances ne sont plus corrélées aux dépenses, estimé autour de 6 000 à 6 500 € par an par éléve d’après les donn… | 6 000 | `identique` | `N-e132-1` (autour de 6 000) |  |
| note de fin e132 | Il est supérieur au seuil où les performances ne sont plus corrélées aux dépenses, estimé autour de 6 000 à 6 500 € par an par éléve d’après les donn… | 6 500 € | `absent` | — |  |
| note de fin e132 | Il est corrigé des surcontributions aux retraites publiques, et conserve de manière prudente 10 à 15 % de dépenses de soutien aux publics fragiles (é… | 10 | `identique` | `N-e132-2` (10) |  |
| note de fin e132 | Il est corrigé des surcontributions aux retraites publiques, et conserve de manière prudente 10 à 15 % de dépenses de soutien aux publics fragiles (é… | 15 % | `absent` | — | même valeur portée par N-e118-2, R-D7-3-1-p1 — aucun libellé ne recoupe la phrase |
| note de fin e133 | Le salaire net moyen des enseignants est de 2920 € net par mois. | 2920 € | `identique` | `N-e133-1` (2920 €) |  |
| note de fin e133 | Pour les professeurs des écoles, il est aujourd’hui à 2 680 € nets en moyenne. https://www.vie-publique.fr/en-bref/299897-enseignants-titulaires-un-s… | 2 680 € | `identique` | `N-e133-2` (2 680 €) |  |
| note de fin e133 | Pour les professeurs des écoles, il est aujourd’hui à 2 680 € nets en moyenne. https://www.vie-publique.fr/en-bref/299897-enseignants-titulaires-un-s… | 299897 | `identique` | `N-e133-3` (299897) |  |
| note de fin e135 | Cette surcontribution d’équilibre, divergeant d’une cotisation retraite normale, peut être estimée à 17 Md€ pour le seul enseignement primaire et sec… | 17 Md€ | `identique` | `N-e135-2` (17 Md€) |  |
| note de fin e135 | Cela représente ainsi au moins 14 % de la dépense publique d’enseignement scolaire retracée actuellement. | 14 % | `identique` | `N-e135-3` (14 %) |  |
| note de fin e137 | Juge et partie, il s’exonère lui-même de normes de sécurité en une matière pourtant vitale, comme le souligne le Rapport d’enquête de sécurité établi… | 33 | `absent` | — |  |
| note de fin e139 | D’environ +18 %, d’après les données du Céreq, Enquête Génération 2013 (menée en 2016). | 18 % | `identique` | `N-e139-1` (environ +18 %) |  |
| note de fin e141 | D’au moins 7 %, sous l’hypothèse la plus optimiste où les recettes et les dépenses sont fixées et pas affectées par le contexte économique ayant décl… | 7 % | `identique` | `N-e141-1` (7 %) |  |

## Les 93 entrées sans source, en sens inverse

| entrée | valeur | rubrique du proto | issue | emplacement au manuscrit | détail |
|---|---|---|---|---|---|
| `P-D-078` | 16,9 Md€/an | Prestations sociales | retrouvée au manuscrit | note de fin e129 | « 16,9 milliards d’euros » — recouvrement 0.33 |
| `P-D-108` | +13 % | Perdants | retrouvée au manuscrit | SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-s… | « 13 % » — recouvrement 0.67 |
| `P-D-012` | 2024 | 3 axes de simplification | dérivée d’un chiffre du manuscrit | note de fin e4 | opérande(s) retrouvée(s) : 2190 (note de fin e4) |
| `P-D-100` | +1,4 % | Perdants | dérivée d’un chiffre du manuscrit | SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-s… | opérande(s) retrouvée(s) : 13 (SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-), 300 (SAUVONS L’… |
| `P-D-101` | environ 20 | Perdants | dérivée d’un chiffre du manuscrit | note de fin e92 | opérande(s) retrouvée(s) : 10 (note de fin e92), 600 (SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4… |
| `P-D-102` | 9 % | Perdants | dérivée d’un chiffre du manuscrit | SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-s… | opérande(s) retrouvée(s) : 13 (SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-) |
| `P-D-103` | 3,3 millions | Perdants | dérivée d’un chiffre du manuscrit | SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-C4-et-s… | opérande(s) retrouvée(s) : 13 (SAUVONS L’ÉTAT DE LUI-MÊME / P2-C4 / P2-) |
| `P-D-001` | 1270 | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-002` | 1270 | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-003` | 1990 | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-004` | 922276 | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-005` | 2024 | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-006` | 2024 | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-007` | 2024 | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-008` | 2024 | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-009` | 8657156 | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-010` | 2024 | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-011` | 2024 | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-013` | 1801,80 € | 3 axes de simplification | d’origine inconnue | — | — |
| `P-D-014` | 2026 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-015` | 2025 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-016` | 2024 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-017` | 7 075 M€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-018` | 3 132 M€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-019` | 7 391 M€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-020` | 14 261 M€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-021` | 3817 M€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-022` | 2023 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-023` | 5014911 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-024` | 14,1 M | Prestations sociales | d’origine inconnue | — | — |
| `P-D-025` | 54,5 M | Prestations sociales | d’origine inconnue | — | — |
| `P-D-026` | 1 | Prestations sociales | d’origine inconnue | — | 5 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-027` | 2021 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-028` | 2025 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-029` | 2021 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-030` | 1 | Prestations sociales | d’origine inconnue | — | 5 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-031` | 2021 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-032` | 2023 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-033` | 1176 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-034` | 350 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-035` | 431 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-036` | 2024 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-038` | 2025 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-046` | 2022 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-050` | 28,0 | Prestations sociales | d’origine inconnue | — | 1 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-052` | 1 | Prestations sociales | d’origine inconnue | — | 5 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-053` | 1 | Prestations sociales | d’origine inconnue | — | 5 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-055` | 3 | Prestations sociales | d’origine inconnue | — | 3 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-056` | 9 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-057` | 99 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-058` | 5 | Prestations sociales | d’origine inconnue | — | 5 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-059` | 6 mois | Prestations sociales | d’origine inconnue | — | 1 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-060` | 30,0 Md€ | Prestations sociales | d’origine inconnue | — | 1 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-061` | 17,8 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-062` | 12,2 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-063` | 7767061 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-066` | 73 % | Prestations sociales | d’origine inconnue | — | — |
| `P-D-067` | 106 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-068` | 2024 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-069` | 253 Md€/an | Prestations sociales | d’origine inconnue | — | — |
| `P-D-070` | 200,5 Md€/an | Prestations sociales | d’origine inconnue | — | 1 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-072` | 32,5 Md€/an | Prestations sociales | d’origine inconnue | — | — |
| `P-D-073` | 20 Md€/an | Prestations sociales | d’origine inconnue | — | — |
| `P-D-074` | 52,2 Md€/an | Prestations sociales | d’origine inconnue | — | 1 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-075` | 15,3 Md€/an | Prestations sociales | d’origine inconnue | — | — |
| `P-D-076` | 38,3 Md€/an | Prestations sociales | d’origine inconnue | — | — |
| `P-D-077` | 8,7 Md€/an | Prestations sociales | d’origine inconnue | — | — |
| `P-D-079` | 7 Md€/an | Prestations sociales | d’origine inconnue | — | — |
| `P-D-080` | 16,3 Md€/an | Prestations sociales | d’origine inconnue | — | — |
| `P-D-081` | 242 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-082` | 1457 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-083` | 304,2 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-084` | 11 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-085` | 21 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-086` | 14 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-087` | 10,5 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-088` | 368 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-089` | 200 Md€ | Prestations sociales | d’origine inconnue | — | 1 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-090` | 242 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-091` | 142 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-092` | 100 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-093` | 41 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-094` | 10 pt | Prestations sociales | d’origine inconnue | — | 10 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-095` | 30 % | Prestations sociales | d’origine inconnue | — | 2 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-096` | 5 pt | Prestations sociales | d’origine inconnue | — | 4 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-097` | 368 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-098` | 1457 Md€ | Prestations sociales | d’origine inconnue | — | — |
| `P-D-099` | 2024 | Prestations sociales | d’origine inconnue | — | — |
| `P-D-104` | 1,5 | Perdants | d’origine inconnue | — | — |
| `P-D-105` | 3,8 % | Perdants | d’origine inconnue | — | — |
| `P-D-106` | 2,3 millions | Perdants | d’origine inconnue | — | — |
| `P-D-107` | 3 | Perdants | d’origine inconnue | — | 3 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |
| `P-D-109` | environ +50 % | Perdants | d’origine inconnue | — | 4 chiffre(s) de même valeur au manuscrit, aucun libellé ne recoupe |

## Les divergences

**11.** Chacune est une entrée que le référentiel adosse à une note du manuscrit, et dont la valeur n'est portée par aucun chiffre relevé à cette note. Elles appellent une décision ; aucune n'est tranchée ici.

| entrée | valeur au référentiel | confiance | ancrage déclaré | chiffres relevés à cet endroit |
|---|---|---|---|---|
| `N-e106-1` | 1754 | 3 | note:e106 · corps:P2-C5-supprimons-toutes-ces-taxes-en-trop… | 20 %, 4 impôts, 5 points, 60 %, 75 %, 81 % |
| `N-e106-2` | 36 | 3 | note:e106 · corps:P2-C5-supprimons-toutes-ces-taxes-en-trop… | 20 %, 4 impôts, 5 points, 60 %, 75 %, 81 % |
| `N-e135-1` | 2024 | 3 | note:e135 · corps:P3-C4-un-meilleur-apprentissage-passe-par… | 14 %, 17 Md€ |
| `N-e135-4` | 2025 | 3 | note:e135 · corps:P3-C4-un-meilleur-apprentissage-passe-par… | 14 %, 17 Md€ |
| `N-e35-2` | 112 | 3 | note:e35 · corps:P1-C3-la-subvention-est-un-poison-pour-la-… | 100 millions d’euros, 14,3 %, 21,4 %, 66 millions d’euros |
| `N-e38-1` | 2021 | 3 | note:e38 · corps:P1-C3-la-subvention-est-un-poison-pour-la-… | 100 millions d’euros, 18 millions d’euros, 66 millions d’euros |
| `N-e71-1` | 2025 | 3 | note:e71 · corps:P1-C5-un-record-de-depenses-pas-de-solidar… | 100 000 personnes, 13 000, 15 %, 180 euros, 2,8 millions, 203 000 places, 25 %, 2500 euros, 39 000, 6, 60 %,… |
| `N-e74-1` | 2024 | 3 | note:e74 · corps:P1-C5-votre-retraite-depend-aujourdhui-dun… | 125 milliards d’euros, 282 milliards d’euros, 407 milliards d’euros, 65 ans, 69 ans |
| `N-e79-2` | 2022 | 3 | note:e79 · corps:P1-C5-le-systeme-scolaire-francais-est-un-… | 10,2 %, 15 %, 25 %, 7,4 %, 78 |
| `N-e83-2` | 2023 | 3 | note:e83 · corps:P1-C5-luniversite-na-pas-le-monopole-de-la… | 30 %, 40 %, 60 % |
| `N-e99-2` | 2024 | 3 | note:e99 · corps:P2-C4-restituer-600-euros-par-mois | 14 %, 2190 €, 236 milliards d’euros, 50 %, 600 euros, 7 |

Toutes portent une valeur qui, au manuscrit, n'est pas un chiffre : un millésime, un numéro de rapport, un rang de classement, un compte de pages. Le manuscrit fait foi : c'est le relevé du référentiel qui a pris une date ou une référence pour une grandeur. **Cela ne se corrige pas ici.**

## Les sources qui citent un onglet disparu

Neuf des 45 sources écrites à la main dans `appareil/sources_chiffres.py` citent une adresse qui n'existe plus dans les classeurs déposés le 20260917. **Aucune n'est réécrite.** Relevé repris tel quel de `livrables/ecart_classeurs_20260917.md`, section 4.

| entrée | valeur | onglet cité | état |
|---|---|---|---|
| `R-D2-1-1-e1` | 236 Md€/an | `Manifeste`, L3 et L24 | onglet disparu |
| `R-D8-3-1-e2` | 30 Md€/an | `Manifeste` L20 ; `Capitalisation` | deux onglets disparus |
| `R-D3-2-1-p4` | 114 | `Gages` | renommé `Flux` |
| `R-D3-2-1-p5` | 9,7 | `CSG` H3 et I3 | renommé `CSG-CRDS`, bloc retiré |
| `R-D3-2-1-p6` | 98,25 | `CSG` | renommé |
| `R-D3-2-1-p7` | +12 | `CSG` G8 | renommé |
| `R-D3-2-1-e3` | −15,18 Md€/an | `CSG`, bloc Effets généraux | bloc disparu |
| `R-D3-2-1-e4` | −21 Md€/an | `CSG`, ligne Effet inflation | bloc disparu |
| `R-D7-2-2-e2` | 18 Md€/an | `Capitalisation` L2:L7 | renommé `Input Capitalisation` |

Toutes nomment par ailleurs le millésime `0819` ou `0804`. Elles restent vraies de l'état qu'elles citent ; elles ne décrivent plus l'état déposé.

## Ce qui reste à instruire

- Les 86 entrées sans source qui ne se retrouvent pas au manuscrit restent à instruire une par une. Ce fil les identifie, il ne les résout pas.
- Les sept vérifications du second cercle du socle sont perdues et cinq de leurs six onglets sources n'existent plus. Ce fil ne les rejoue pas.
- Les 56 entrées de doctrine dont l'ancrage `M-nnnn` ne résout pas : c'est le manquant `releve_affecte` de l'index, pas une question de ce fil.

