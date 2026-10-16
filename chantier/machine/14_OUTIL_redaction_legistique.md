---
name: redaction-legistique
description: "Rédaction légistique de projets et propositions de révision constitutionnelle (PPLC), de loi organique (PPLO) et de loi ordinaire (PPL) en droit français. Utiliser cette skill dès qu'il s'agit de récupérer le texte en vigueur d'un article de la Constitution, d'une loi organique (LOLF, LOLFSS...) ou d'un code sur Légifrance, de transformer un texte cible en dispositions modificatives, de produire une proposition de loi déposable avec exposé des motifs, de vérifier la conformité légistique d'un texte normatif, ou de reprendre une jambe de loi ordinaire déclarée par une chaîne d'amendement. Déclencher aussi pour toute demande mentionnant PPLC, PPLO, PPL, dispositions modificatives, texte consolidé, gage d'une proposition de loi, ou dépôt parlementaire."
---

# Rédaction légistique — révision Constitution / LO / loi

Workflow en cinq étapes. Chaque étape produit un livrable vérifié avant de passer à la suivante. Ne jamais sauter l'étape 1 : **aucun texte en vigueur ne doit venir de mémoire**.

## Vue d'ensemble

```
0. RECEVOIR    une jambe de loi ordinaire déclarée par une chaîne d'amendement,
               le cas échéant — ce qu'elle apporte et ce qu'elle n'apporte pas
1. RÉCUPÉRER   texte en vigueur exact (Légifrance, jamais de mémoire)
2. SÉCURISER   texte cible (validation rédactionnelle + gel de la version)
3. RÉDIGER     dispositions modificatives (delta en vigueur → cible)
4. FORMALISER  PPL(C/O) déposable — exposé des motifs + dispositif
5. ALTERNATIVE PPL par substitution intégrale (les articles cibles remplacent
               les articles en vigueur) — livrable distinct de l'étape 3
```

Les étapes 3 et 5 sont **deux versions différentes du même projet**, pas deux
présentations du même texte. Le livrable final est **double par défaut** : une
version modificative (étapes 3→4) et une version substitution (étapes 5→4), tous
deux construits sur les mêmes cibles gelées de l'étape 2 — ils produisent donc le
même droit, ce que le bouclage garantit. Ne produire un seul des deux que sur
instruction expresse.

## Étape 0 — Recevoir une jambe de loi ordinaire

Une chaîne d'amendement qui qualifie un programme rend, pour chaque ligne dont le
siège sort du domaine du véhicule financier, une **jambe déclarée** : le véhicule
réel, le siège probable, et le motif de sortie. **Cette jambe est une entrée de
cette skill, et elle n'est pas un texte cible.**

**Ce que la jambe apporte, et ce qui est utilisable tel quel :**

| elle apporte | statut |
|---|---|
| l'énoncé de la mesure **dans les mots de l'auteur** | utilisable — il ne se reformule pas |
| le **siège probable** — code, articles pressentis | **une piste, pas une adresse.** L'étape 1 la confirme sur Légifrance ou elle la remplace |
| le **motif de sortie du domaine** — « ni recette ni dépense d'un régime de base », « capacités d'accueil universitaires » | utilisable dans l'exposé des motifs comme raison du véhicule |
| le **levier substitué portable dans le véhicule financier**, quand il en existe un | **information de coordination** : la mesure peut alors avoir deux jambes, et le dépôt de l'une n'emporte pas l'autre |

**Ce que la jambe n'apporte pas, et qui se fait ici** : le texte en vigueur (étape 1), le texte cible (étape 2), et l'arbitrage du découpage en articles de la proposition.

**Deux règles de conduite, et elles évitent le travail perdu :**

- **Un siège relevé par une chaîne d'amendement porte un rang de source.** Un siège
  relevé au rang du texte déposé ou du dépôt de droit se confirme vite ; un siège
  relevé par déduction se rejoue entièrement à l'étape 1.
- **Une jambe déclarée n'est pas une mesure arbitrée.** La chaîne l'a sortie du
  véhicule financier ; elle n'a pas dit que l'auteur veut la déposer. **On le lui
  demande une fois, et on continue en le déclarant s'il ne répond pas.**

## Étape 1 — Texte en vigueur (Légifrance)

Lire `16_OUTIL_redaction_legifrance.md` avant la première récupération de la session.

Résumé : récupérer via `web_fetch` sur legifrance.gouv.fr (URLs LEGIARTI/LEGITEXT stables), vérifier l'état « en vigueur » et la date de version, transcrire verbatim alinéa par alinéa. En cas d'échec de fetch, passer par `web_search` puis fetch du résultat. Si aucune source fiable n'est accessible : le signaler et marquer le texte « à vérifier sur Légifrance » — ne jamais combler de mémoire.

**L'applicabilité se lit aux dates, jamais au seul état.** Un article peut s'appliquer aujourd'hui et porter une abrogation déjà votée ; le filtrer sur son état fait disparaître du droit en vigueur sans un message. Un état et un intervalle de dates qui divergent se signalent.

Livrable : le texte en vigueur verbatim, avec pour chaque article la référence de version (date d'entrée en vigueur, loi modificatrice le cas échéant).

## Étape 2 — Sécurisation du texte cible

Le texte cible est fourni explicitement en entrée (fichier, colonne C d'un tableau trois colonnes, ou texte brut). Ne jamais l'inventer ni l'extrapoler.

Deux contrôles obligatoires :

1. **Contrôle rédactionnel** : passer le texte cible au crible de `18_OUTIL_regles_redactionnelles.md`. Chaque écart est signalé à l'utilisateur avec une proposition de correction — jamais corrigé silencieusement. Le texte cible n'est gelé qu'après arbitrage.
2. **Diff structuré** : exécuter `43_SCRIPT_diff_cible.py` sur les paires (en vigueur, cible). La sortie liste, article par article et alinéa par alinéa, chaque delta typé (suppression, insertion, remplacement, abrogation, création). Ce diff est la matrice de l'étape 3 et le référentiel du contrôle de bouclage.

Livrable : texte cible gelé + diff structuré. Toute modification ultérieure du texte cible rouvre l'étape 2.

## Étape 3 — Dispositions modificatives

Lire `15_OUTIL_redaction_formules.md` avant rédaction.

Principe : une disposition par delta du diff, dans l'ordre du texte modifié, avec la formule la plus économique du répertoire légistique. Choisir le niveau de chirurgie qui maximise la lisibilité :

- delta ponctuel (mots, chiffre, référence) → substitution de mots
- alinéa profondément remanié → remplacement d'alinéa entier
- article majoritairement réécrit → « L'article X est ainsi rédigé »
  (bascule assumée vers la logique de substitution pour cet article ;
  ce n'est pas l'étape 5, qui substitue *tout*)

**Contrôle de bouclage (obligatoire)** : appliquer mécaniquement les dispositions rédigées au texte en vigueur et comparer le résultat au texte cible gelé (le script `diff_cible.py --verify` automatise la comparaison). Toute divergence est une erreur bloquante — corriger les dispositions, jamais le texte cible.

Livrable : dispositif modificatif complet, numéroté (articles 1er, 2, 3... ; subdivisions I, II ; 1°, 2° ; a), b)).

## Étape 4 — PPL(C/O) déposable

Lire `17_OUTIL_redaction_structure_ppl.md`, qui porte les maquettes de page de titre par assemblée, la convention des descripteurs de travail, la répartition des fonctions entre niveaux et les autorités citables.

**Format de travail : markdown.** Le document se rédige et se valide en md — un seul fichier maître, page de titre, exposé des motifs, dispositif. L'export vers un format de transmission n'intervient qu'au moment de remettre le texte à des tiers, et il relève d'une compétence distincte — celle de l'auteur s'il en a une —, qui porte les conventions typographiques et le contrôle sur le rendu. Ne pas générer d'export pour un usage interne : il coûte cher et n'apporte rien à la validation du texte.

Contenu dans l'ordre : page de titre (mentions propres à l'assemblée de dépôt), exposé des motifs (court : le mal, le remède, l'économie du texte — quelques paragraphes généraux puis un paragraphe par article ou groupe d'articles), dispositif, le cas échéant dispositions transitoires **et gage, dans les seuls cas où un gage existe (voir ci-dessous)**.

Trois règles de l'exposé des motifs, détaillées dans `17_OUTIL_redaction_structure_ppl.md` et à lire avant toute rédaction : **chaque niveau a une fonction propre** (l'assise pose le concept, le chapeau de division désigne le moyen, le commentaire nomme le mécanisme) ; **dire ce que l'article fait, c'est le nommer et non le restituer** — le dispositif est sous les yeux du lecteur, seul l'exposé peut fournir le nom du mécanisme et sa raison ; **les verbes de commentaire sont révise, abroge, insère**, l'exposé servant indifféremment les deux versions du dispositif.

### L'article 40 et le gage — deux régimes, et la règle antérieure les inversait

*Corrigé sur relevé. La rédaction antérieure de cette skill prévoyait un gage « uniquement pour les PPL/PPLO créant une charge ». **C'est l'inverse du droit applicable**, et une proposition ainsi construite est irrecevable au dépôt.*

L'article 40 de la Constitution vise deux choses, et elles ne se traitent pas de la même façon :

| ce que la proposition fait | régime |
|---|---|
| **elle diminue une ressource publique** | **recevable si elle est gagée.** Le gage est dû, il est une **recette**, et il bénéficie à la personne publique qui subit la perte |
| **elle crée ou aggrave une charge publique** | **irrecevable, et elle ne se gage pas.** Le texte se reformule, ou la charge se retire du dispositif |

**Quatre règles, en verbatim, relevées sur le rapport de la commission des finances de l'Assemblée nationale consacré à la recevabilité financière et sur le vademecum de la commission des finances du Sénat :**

> « Une diminution des ressources publiques doit être gagée pour être recevable »

> « Le gage doit être crédible et réel »

> « Le gage doit être correctement affecté » — *« l'augmentation de recettes déterminée par le gage doit bénéficier à la collectivité qui subit la perte de recettes »*

> « la hausse concomitante et à due proportion d'**une autre ressource** » — et, en symétrique : *« une augmentation de charge, même modeste, est, par nature, impossible à compenser par une économie »*

**Le gage est une recette, jamais une économie.** Une baisse de dépense ne gage rien.

**Et un interdit, cité comme intitulé** : *« l'interdiction de combiner entre le droit existant et le droit proposé : la jurisprudence dite beurre et argent du beurre »* — un gage se prend **hors** de ce que la proposition produit elle-même.

**Ce qui n'est PAS une charge**, et qui ne condamne donc pas une proposition : *« les dispositions ayant un effet trop indirect sur les charges publiques »* et *« la charge de gestion »*. Une obligation déclarative, un contrôle, une publication ne rendent pas un texte irrecevable du seul fait qu'ils coûtent à l'administration. **Et le doute profite à l'auteur** : *« quand il existe un doute quant aux conséquences financières d'un amendement, ce dernier est considéré comme recevable »*.

*Réserve de source : le quatrième verbatim vient du rapport de l'Assemblée, les trois autres du vademecum du Sénat. La règle est concordante entre les deux chambres, mais **le dépôt se fait dans une chambre** : sur un point de détail, la doctrine de la chambre de dépôt tranche.*

**Forme du gage, pour l'État** :

> La perte de recettes pour l'État est compensée à due concurrence par la création d'une taxe additionnelle à l'accise sur les tabacs prévue au chapitre IV du titre Ier du livre III du code des impositions sur les biens et services.

**Pour les organismes de sécurité sociale**, la formule vise la majoration d'une accise, désignée **par son chapitre de code**, et chaque chapitre employé se vérifie sur Légifrance. Pour une **faculté locale**, l'instrument n'est pas un gage d'État mais une **clause de non-compensation** portée par le dispositif.

Intitulés types :
- PPLC : « Proposition de loi constitutionnelle portant révision des articles X, Y et Z de la Constitution » ou « ... relative à [objet] »
- PPLO : « Proposition de loi organique relative à [objet] »
- PPL : « Proposition de loi relative à [objet] »

Livrable : un fichier md complet par version — modificative et substitution — sauf instruction contraire. Passe de dépôt : retrait des descripteurs, contrôle des crochets résiduels, puis export vers le format de transmission attendu par l'assemblée de dépôt.

## Étape 5 — Version par substitution intégrale

Livrable distinct de l'étape 3, construit à partir du texte cible gelé de l'étape 2 (pas à partir des dispositions de l'étape 3).

Structure : un article de la PPL par article révisé, sur le modèle :

> Article N
> L'article X de la Constitution est remplacé par les dispositions suivantes :
> « Art. X. — [texte cible intégral] »

Cas particuliers : article abrogé → « L'article X est abrogé. » ; article créé → « Après l'article X, il est inséré un article X-1 ainsi rédigé : ... » ; titre entier remanié → remplacement du titre.

Cette version privilégie la lisibilité du **résultat** (on lit directement le droit futur) ; l'étape 3 privilégie la lisibilité du **changement** (on voit exactement ce qui bouge). Présenter ce choix à l'utilisateur si la destination du document n'est pas connue.

Livrable : dispositif de substitution complet, portable en étape 4 dans sa propre version.

## Les renvois entrants — la boucle va jusqu'au bout

**C'est ce qui distingue une proposition de loi d'un amendement.** Un amendement signale les articles qui citent celui qu'il modifie ; **une proposition de loi les traite ou les déclare sans objet avant dépôt.**

Trois certitudes, fixées par une règle de déduction et jamais par une impression : `nomme` quand la phrase nomme le code visé ; `interne` quand l'article citant est dans le même code et qu'aucun autre n'est nommé ; `ambigu` pour une citation nue depuis un autre code. La partie réglementaire se compte à part — elle n'est pas à portée du texte.

**Un renvoi vers un texte non consultable est invérifiable, et cela se déclare** au lieu de se compter pour traité.

## Règles transversales

- Jamais de texte en vigueur de mémoire ; jamais de chiffre ou de référence inventé ; « [à vérifier] » en cas de doute.
- Les paramètres politiques non tranchés restent entre crochets [X] avec note.
- **Ne jamais gager une charge**, et ne jamais gager par une économie.
- Guillemets français « » pour tout texte cité dans un dispositif ; la ponctuation finale se place avant le guillemet fermant (« ...croyances. » et jamais « ...croyances ».). Cette règle vaut pour tout gabarit ou code de génération : la vérifier sur le rendu, pas seulement dans le texte source.
- Pas de virgule devant une conjonction de coordination, hors clôture d'incise. Règle transversale à tous les livrables, normatifs comme rédactionnels — voir `18_OUTIL_regles_redactionnelles.md`. **Elle se lit avant de rédiger, jamais à l'export** : jouée après coup, elle fait reprendre le tissu de chaque phrase.
- Formulations positives, y compris hors dispositif : écrire ce que la règle fait. Pas d'antithèse d'ouverture, pas de « ne tient pas à… mais à », pas de « ni… ni ». Entorse tolérée sur un manquement constaté ; exception pleine dans la section « ce que la proposition laisse intact ».
- Pas de point-virgule dans le texte normatif cible (règle de ce corpus — voir `18_OUTIL_regles_redactionnelles.md`) ; les points-virgules des énumérations légistiques du *dispositif modificatif* (1° ... ; 2° ...) restent en revanche l'usage.
- Chaque livrable est horodaté : `NomDoc_YYYYMMDD_vN` — date obtenue par `date +%Y%m%d`, jamais de mémoire.
- Toute édition de fichier HTML/texte existant passe par remplacement avec garde d'unicité (`assert count == 1`).
- **Aucune sortie ne nomme un déposant, une organisation ou une source interne.** L'énoncé d'un tiers se prend à sa valeur faciale.