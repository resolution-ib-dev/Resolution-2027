# Valise projetée — phase 1, exercice 2027

*Constituée le 20261002. Elle remplace la valise du millésime précédent, qui
projetait un découpage en 71 énoncés aujourd'hui périmé.*

**Règle de lecture des chiffres.** Chaque valeur sort avec sa pièce, son
emplacement et le libellé exact de sa ligne. Le repère dit où l'on a lu, non ce
qu'on a lu. Une page non relevée se déclare non relevée : elle ne s'invente pas.

**Deux origines, et elles ne se confondent pas.** *Pièce publique* — document
budgétaire, rapport, base statistique ; le renvoi est complet et vérifiable.
*Calcul propre* — opération conduite sur des pièces publiques nommées ; le
résultat se donne comme calcul propre, avec ses hypothèses, jamais comme un
décompte officiel.

---

## 1. Les cinq paramètres du dossier

```
exercice                  2027
vehicule                  plf · plfss  — porté mesure par mesure, voir § 6
numero_texte              non attribué au dépôt
socle                     redaction_plf.json · redaction_plfss.json
millesime_droit           à arrêter au lancement de chaque passe
```

**Le contrôle d'arrêt du § 3.1 du contrat ne mord pas sur cet exercice.** Les
deux textes sont **déposés et non votés** : aucune loi n'est issue du socle, donc
aucun millésime de droit ne peut lui être postérieur. La conduite par défaut —
changer d'exercice — est sans objet, et le mode absolu n'a pas lieu d'être. *Ce
point a coûté trois contournements du contrôle d'arrêt au millésime précédent ; il
ne se pose plus.*

**Le millésime du droit se renseigne quand même**, parce que E3 compare la date de
version de chaque article à celle du socle et déclare l'écart. Le socle date du
1er octobre 2026.

---

## 2. Le bloc des pièces publiques

```
exercice                  2027
arrete_le                 2026-10-01
a_rafraichir_le           dépôt du texte de l'exercice 2028
texte_depose              PLF 2027  — sha256 b0b802d3cafb3134…  90 articles
                          PLFSS 2027 — sha256 71010873c0af8a77… 49 articles
voies_et_moyens_t1        NON PARUE pour 2027 — tome I annexe 2, taxes affectées
voies_et_moyens_t2        NON PARUE pour 2027 — tome II annexe 3, dépenses fiscales
etat_b                    au texte déposé, article 57, folios 203 et suivants
projets_annuels_perf      NON OUVERTS
taxes_affectees           article 42 du PLF, folios 160 à 181 — le texte porte
                          son propre tableau et il prime sur tout classeur
jaunes                    aucun ouvert
amendements_deposes       NON OUVERT — et c'est le manque le plus coûteux
```

### L'approchant 2026, et la règle qui va avec

**Les deux annexes détaillées ne sont pas parues.** Les classeurs du millésime
2026 les tiennent, et ils sont joints au dossier à ce titre et à ce titre seul.

Toute valeur qui en vient porte la mention **« approchant 2026, à rejouer »**,
entre au plus bas niveau de confiance, **ne paraît dans aucun chiffrage
déposable**, et cède devant tout chiffre du corps du texte 2027. À la parution des
annexes, seules ces valeurs se rejouent.

*La mention n'est pas une prudence d'écriture : sans elle, le jour où les annexes
paraissent, on ne saura pas quoi rejouer — donc on rejouera tout, ou rien.*

### Le manque qui coûte le plus, et il est gratuit à combler

**`amendements_deposes` n'est pas ouvert.** Le quatrième contrefactuel du test de
rattachement s'y répond, et le contrôle 11 du contrat en fait un échec de
contrôle, pas un signalement. Les amendements déposés sur le PLF 2027 et le PLFSS
2027 sont publics et consultables au point d'accès de l'Assemblée nationale, avec
le sort de chacun — irrecevable, retiré, rejeté, adopté.

**Chaque dossier de la phase 1 doit donc ouvrir cette pièce ou établir son
inaccessibilité sur pièce.** À défaut, le contrôle 10 le laisse à l'état `à
vérifier avant dépôt`.

---

## 3. Le référentiel de sièges déjà relevés

**Il est rempli, et c'est la différence avec le millésime précédent.** Au banc, il
restait vide par construction : relever un siège y revenait à souffler la réponse
à l'étape qui a pour objet de la trouver. **Cette passe ne mesure pas, elle
produit** : le référentiel est donc branché.

**Pièce** : `articles_ouverts_plf.tsv`, **421 adresses dans 62 textes**, et
`articles_ouverts_plfss.tsv`, **153 adresses dans 22 textes**. Jointure sur le
libellé exact, jamais au plus proche.

*Ces deux tables sont celles du 20261002, après correction. Les tables versées la
veille — 449 et 191 adresses — sont périmées et ne se rejouent pas : elles
comptaient comme sièges des adresses que le texte ne fait que désigner comme
point d'insertion (« après l'article L. 241-13 »), et attribuaient à la mauvaise
pièce les adresses nommées en tête de phrase. Un dossier ouvert sur une adresse
qui n'est plus à la table rend une adresse sans siège.*

**Rang de source** : ces tables sont du **rang 2** au sens de l'échelle de E2.
Elles prouvent le couple (texte, article) — **jamais la subdivision**. Savoir
qu'un article est ouvert dit qu'on peut s'y accrocher, pas où. La subdivision se
cherche au rang 1, sur le texte déposé lui-même, que `redaction_plf.json` porte en
verbatim.

**L'écart au relevé de lecture ne se résorbe pas, et il ne doit pas l'être.** Le
relevé de lecture compte les adresses que le texte **cite** ; la table des
articles ouverts compte celles qu'il **modifie**. Les deux nombres ne doivent pas
coïncider, et une adresse prise au relevé de lecture pour fonder un siège est une
faute — elle a été commise le 20261001 sur l'article 200 du code général des
impôts.

**Écart résiduel déclaré** : quelques adresses du code de la sécurité sociale
sortent sous « code de la santé publique » quand une même phrase nomme les deux
codes. À vérifier sur le verbatim avant emploi.

---

## 3 bis. Le code général des impôts réécrit par l'expert

**C'est la source privilégiée de la colonne C**, et elle n'était pas à la valise
du premier bloc. Son absence est le manque de méthode que le compte rendu du
20261002 relève.

**Ce qu'elle est** : la rédaction cible déclarée de l'auteur sur 2 376 articles du
code général des impôts. Elle alimente l'étape E4 — le texte tel qu'il sera. Elle
n'est ni une doctrine, ni un chiffrage, ni un véhicule, et **elle ne se corrige
pas** : un désaccord avec elle se porte à l'auteur.

**Pièces** : `referentiels/cgi_expert_articles.tsv`,
`cgi_expert_insertions.tsv`, `cgi_expert_suppressions.tsv`,
`cgi_expert_articles_bouges.tsv`, `cgi_expert_parametres.tsv`. Elles ne se lisent
qu'à travers `reference/cgi_expert_regles_de_lecture.md`, qui est **la pièce
d'ouverture obligatoire** : sans elle, on mesure un écart de millésime au lieu
d'une rédaction.

**Les quatre règles qui commandent l'emploi :**

1. **Le droit de départ est le code au 1er mai 2026.** La colonne A ne se lit
   jamais dans cette source : elle se régénère au dépôt de droit, à la date du
   texte en discussion.
2. **Avant d'employer un article, le contrôler dans `cgi_expert_articles_bouges.tsv`.**
   78 articles ont changé de version depuis le 1er mai 2026, 4 ont disparu, 186
   portent une abrogation déjà votée. Sur ces 268, la rédaction de l'expert part
   d'un état qui n'est plus le droit.
3. **41 articles applicables sont hors du périmètre des cinq pièces.** Leur
   silence n'est pas un maintien.
4. **Un article portant un commentaire non tranché ne part pas dans un lot
   d'amendements.** Les 74 commentaires de l'expert sont tous ouverts ;
   `livrables/cgi_expert_commentaires_20260929.md` les porte avec leur article.

**La règle de priorité, et elle est le point qui mord sur la phase 1.** Quand la
rédaction de l'expert et le corpus divergent, **le corpus prime et l'écart se
déclare en exposé sommaire**. Trois divergences sont déjà relevées et attendent
le fil qui les rencontre : le partage entre 23 %, 25 % et 30 % (article 39
quindecies mêle les deux premiers taux dans une phrase) ; le taux réduit de TVA à
7 % de l'article 278-0 bis contre le taux unique de M-029 ; l'article 219 resté à
25 % quand M-032 fait porter au taux d'impôt sur les sociétés la compensation
transitoire.

**Ce qu'elle ne couvre pas** : la phase 1 porte cinq jambes dont quatre touchent
le code général des impôts. L'article 200 — jambe 1 — est dans son périmètre ; le
tableau d'affectation de l'article 42 du PLF — jambe 5 — ne l'est pas, parce que
ce n'est pas un article de code.

---

## 4. Les principes de l'auteur

*Ils ne sont pas millésimés et ils se reprennent tels quels. Le champ `principe`
de l'en-tête se prend ici et ne se propose jamais.*

- **L'absence de vote ne vaut pas autorisation.** Une affectation à un tiers, une indexation automatique, un engagement pluriannuel reconduit sans vote sont des dépenses soustraites au consentement. C'est le vice visé, et il commande plusieurs énoncés à la fois.
- **Un euro non dépensé se restitue.** L'économie ne sert ni le désendettement, ni une dépense nouvelle, ni un redéploiement. Elle va au salaire net, puis au compte d'épargne, puis au compte du citoyen. Un énoncé qui laisse l'économie dans la sphère publique manque son objet.
- **Le gain va au net, pas au brut.** Les prélèvements visés sont assis sur la rémunération brute : le gain arrive intégralement sur le salaire net, sans effet sur le coût du travail ni sur les marges.
- **Une aide ciblée se remplace par du revenu libre d'emploi**, jamais par une aide ciblée mieux administrée. La condition, le formulaire et le guichet sont eux-mêmes le mal visé.
- **Un gain a toujours un perdant nommé.** Un gain d'efficacité supprime une rente, et le capteur de cette rente se nomme.
- **Une perte sort avec sa contrepartie**, ou avec l'aveu qu'il n'y en a pas. Trois valeurs et pas de quatrième : renvoi vers un gain nommé, reconstitution volontaire du flux en flux privé, ou absence assumée.
- **La suppression prime la réorganisation.** Fermer, éteindre, céder. Fusionner, recapitaliser, réformer le statut d'une structure facultative sont des réponses hors sujet.
- **L'exception se nomme en extension.** Les taxes conservées, les établissements conservés, les socles conservés sont énumérés, jamais laissés à l'appréciation.
- **Le chiffre se dit au rang de son registre.** Un constat se donne précis, parce que le décompte est la démonstration. Une promesse se donne en ordre de grandeur, parce que l'engagement se tient à la portée de ce qui est démontré.
- **Aucune source ne s'invente, aucun trou ne se comble.**
- **Les formules négatives s'évitent** dans tout ce qui est rédigé pour être lu, sauf dans une rubrique qui dit expressément ce que la mesure laisse inchangé.

---

## 5. La consigne de gage

*Reprise du millésime précédent. Elle était une valeur retenue faute de réponse ;
elle n'a pas été révoquée depuis.*

Le gage se prend par la **suppression ou la réduction d'une dépense fiscale**, et
non par la création ou le relèvement d'un prélèvement. Motif : la pression fiscale
ne monte pas, et un gage pris sur un prélèvement conservé — tabac, alcool,
énergies fossiles — contredirait le principe de restitution en même temps qu'il
relèverait une taxe gardée pour un autre motif.

Trois règles d'application :

1. La ligne servant de gage se désigne par **son numéro et son libellé exact**, et
   son montant se prend à la colonne de prévision de l'exercice.
2. **Une ligne déjà visée par un énoncé de la liasse ne sert pas de gage.** Gager
   une mesure sur une ligne qu'une autre supprime compterait deux fois la même
   ressource.
3. Lorsque aucune ligne ne couvre le montant à gager, **le gage se déclare
   insuffisant et le montant manquant se dit**. Un gage de façade ne se rédige
   pas.

**Difficulté propre à cet exercice, et elle se déclare au dossier.** L'annexe des
dépenses fiscales 2027 n'est pas parue. Une ligne de gage prise à l'annexe 2026
porte donc la mention « approchant 2026, à rejouer », et le contrôle 8 du contrat
— qui compare la branche de gage à la présence d'une adresse de niche du même
impôt dans le dépôt de droit — se joue sur l'adresse, non sur le montant.

**La phase 1 porte par ailleurs sa propre source de gage.** La suppression des
niches est une mesure de la phase, et son produit se décrémente dans l'ordre de
dépôt. Un euro n'appartient qu'à un seul circuit.

---

## 6. Les douze mesures de la phase 1

*Phase de concentration. Elle ne restitue rien : sans elle il n'y aurait rien à
restituer. Elle n'attend pas le sort des prélèvements — elle porte sur les
crédits, les emplois et les niches, non sur les impositions.*

**Périmètre mesuré** : 12 mesures, 33 composantes dont 31 portent un dispositif,
33 jambes après scission, dont **24 font amendement** — 5 en première partie du
PLF, 17 en seconde partie, 2 au PLFSS. Six composantes sont des transitions et se
portent dans un titre séparé de l'amendement de leur mesure, jamais en amendement
à part. Deux sont renvoyées hors phase. Une est le gage transversal.

**Deux mesures de ces blocs sont écartées de la phase, et par décision de
l'auteur** : les prélèvements sur la main-d'œuvre et les impôts de production
viennent après la restitution salariale, avec la simplification fiscale ; le
statut de la fonction publique se chronomètre avec la restitution, dont il tire sa
contrepartie. Les deux restent disponibles comme gage ponctuel.

---

### M-002 — Structures exerçant une mission facultative

**Énoncé.** Fermer les agences, organismes centraux, autorités et instances
consultatives qui exercent une mission facultative.

**Paramètres chiffrés.**
- structures recensées : 1 104 — 434 agences nationales, 329 organismes centraux, 24 autorités indépendantes, 318 instances consultatives
- périmètre opposable arrêté : **746 lignes**, dont 78 cessions d'actif et 668 suppressions. *750 est un arrondi de communication et ne s'emploie pas en dispositif.*
- économie associée : **8,632 Md€**, interventions comprises
- hors champ, nommés en extension : environ 300 établissements à patrimoine et revenus propres ; environ 50 agences régaliennes réinternalisées et non fermées

**Lecture retenue.** La liste est **close et organisée par les critères qui la
fondent** — non le seul critère. Le dispositif peut porter une liste close de
bénéficiaires dès lors que des critères la fondent et l'ordonnent ; la règle « pas
de cas nommés » vaut pour l'exposé, pas pour le dispositif.

**Composantes et jambes.**

| composante | jambe | siège |
|---|---|---|
| supprimer l'existence juridique des structures visées | PLF 2de partie | **article additionnel** |
| supprimer les taxes et redevances affectées qui les financent | **PLF 1re partie** | **ouvert — article 42 du PLF 2027** |
| supprimer crédits, subventions pour charges de service public et dotations | PLF 2de partie | état B, ouvert par nature |
| éteindre ou transférer les missions exercées | PLF 2de partie | article additionnel |
| sort des personnels et des actifs | *titre séparé* | — |

**Éclatable** par famille de structures.

**Ce que l'auteur veut obtenir** : que la structure ferme, et non qu'elle soit
réorganisée, fusionnée ou recapitalisée.

**Borne ouverte** : l'ordre des critères d'organisation de la liste.

---

### M-003 — Fonctions régaliennes externalisées

**Énoncé.** Faire exercer directement par les ministères les fonctions régaliennes
aujourd'hui confiées à des agences, notamment l'établissement des amendes et des
documents d'identité.

**Paramètres chiffrés.** Agences visées : une cinquantaine.

**Composantes.** Transférer aux ministères les fonctions déléguées — PLF 2de
partie, article additionnel. Transférer les crédits et emplois correspondants —
PLF 2de partie, états B et C et article de plafond d'emplois, ouverts par nature.

**Ce que l'auteur veut obtenir** : que la fonction régalienne redevienne exercée
par le ministère lui-même, sans intermédiaire. *Le terme à employer est
réinternalisation ou recentralisation.*

---

### M-007 — Effectifs affectés aux missions facultatives

**Énoncé.** Supprimer les postes affectés à des missions facultatives dès la
première année.

**Paramètres chiffrés.**
- postes visés : **580 000** — 151 000 à l'État et ses opérateurs, 428 500 dans les échelons locaux *(calcul propre : 90 % de départs hors régalien et éducation, socle conservé de 10 % dans les échelons locaux hors régalien, social et éducation)*
- répartition : trois quarts dans les échelons territoriaux, un quart dans les agences et les ministères
- part des effectifs publics : 10 %, sur 5,8 millions d'agents, soit un actif sur cinq
- économie associée : **29,575 Md€** de masse salariale, dont 9,575 pour l'État et ses agences et 20 pour les échelons locaux

**Composantes.** Abaisser les plafonds d'emplois de l'État et des opérateurs — PLF
2de partie, ouvert par nature. Réduire les crédits de masse salariale — PLF 2de
partie, état B, titre 2. Le volet des échelons locaux est renvoyé hors phase.

**Lien dur.** **La baisse des emplois passe seule. Le volet crédits dépend de
M-008** : sans l'indemnisation, la réduction totale des crédits ne vole pas.

**Ce que l'auteur veut obtenir** : que les postes soient supprimés dès la première
année, et non gelés ou redéployés.

---

### M-008 — Indemnisation des agents dont le poste est supprimé

**Énoncé.** Verser aux agents dont le poste est supprimé une indemnité égale à une
part de leur traitement, cumulable avec un emploi privé.

**Paramètres chiffrés.**
- taux : **70 % du traitement**
- durée : **jusqu'à sept ans** après le départ
- cumul : autorisé avec un salaire privé
- rapport au dispositif de départ volontaire en vigueur : **2,5 fois plus élevé**

**Composantes et jambes.**

| composante | jambe | siège |
|---|---|---|
| créer l'indemnité | PLF 2de partie | **ouvert — articles 72 et 73 du PLF 2027**, qui touchent le code général de la fonction publique à `L. 351-5`, `L. 513-3`, `L. 514-4`, `L. 556-10`, `L. 821-1`, `L. 824-1`, `L. 824-5`, `L. 825-4`, `L. 134-4`, `L. 134-12` |
| ouvrir les crédits de l'indemnité | PLF 2de partie | état B |
| éteindre le dispositif de départ volontaire en vigueur | PLF 2de partie | **siège partiellement réglementaire — à vérifier** |

**Ce que l'auteur veut obtenir** : que l'agent dont le poste disparaît soit
indemnisé largement et puisse travailler ailleurs sans perdre l'indemnité.
**C'est une économie, pas un coût** — le dispositif rend possible M-007, qui ne
vole pas sans lui. **C'est le nœud identifié de la phase.**

**Borne ouverte** : le coût de l'indemnité n'est pas chiffré. C'est un terme
manquant du bloc.

---

### M-016 — Subventions aux associations

**Énoncé.** Éteindre les subventions publiques aux associations.

**Paramètres chiffrés.**
- économie associée : **12,6 Md€ à terme**, dont 8 Md€ de gain direct
- dont aide publique au développement 3 Md€, subventions culturelles 0,5 Md€, politique de la ville 0,4 Md€
- versant État isolé au chiffrage : 3,2 Md€
- rythme : **extinction en deux ans** *(l'auteur a corrigé les trois ans du chiffrage)*

**Champ, arrêté.** Le **tiers non public et non lucratif, quelle que soit sa forme
juridique et quel que soit le payeur**. La forme juridique cesse d'être le
critère : fondations, fonds de dotation et coopératives d'intérêt collectif
entrent au champ, et le contournement par changement de statut est fermé. Les
personnes publiques sont hors champ.

**Scission — deux jambes.** L'entrée du versant social au champ — fonds d'action
sociale des caisses, agences régionales de santé — fait jouer la frontière entre
textes financiers. **Le montant du versant social n'est pas ventilé.**

| composante | jambe | siège |
|---|---|---|
| éteindre les crédits de subvention | PLF 2de partie | état B |
| éteindre les crédits du versant social | **PLFSS** | **article additionnel** — le relevé des portes du PLFSS ne couvre pas ce siège |
| supprimer les avantages fiscaux attachés au don et au financement associatif | **PLF 1re partie** | **ouvert — article 4 du PLF 2027, CGI `200`.** Siège exact, aucune plaidoirie à faire |
| extinction en deux ans | *titre séparé* | — |

**Dépendance de validité**, et elle s'écrit : la jambe sociale et la jambe fiscale
ne sont pas complémentaires — si la jambe de loi de finances tombe, la jambe
sociale change d'effet. Le relevé de E7 porte le type.

**Ce que l'auteur veut obtenir** : que la subvention s'éteigne, et non qu'elle
soit remplacée par un avantage fiscal équivalent.

**Lien** : la composante recette recoupe la suppression des niches (M-026). Un
euro n'appartient qu'à un seul circuit.

---

### M-017 — Aides aux entreprises

**Énoncé.** Éteindre les subventions et aides publiques aux entreprises.

**Paramètres chiffrés.**
- économie associée, État : **15,2 Md€ à terme** ; échelons locaux : 12,3 Md€, renvoyés hors phase
- dont aides à l'emploi et à l'apprentissage 6,9 Md€, aides à l'investissement 3,2 Md€
- rythme : extinction en trois ans

**Composantes et jambes.**

| composante | jambe | siège |
|---|---|---|
| éteindre les crédits de subvention et d'aide | PLF 2de partie | état B |
| supprimer les exonérations et allègements ciblés | **PLF 1re partie** | **largement ouvert** — articles 7, 9, 10, 11, 12, 13, 26 et 28 du PLF 2027 : CGI `244 quater C`, `244 quater I`, `244 quater O`, `244 quater V`, `44 sexdecies`, `44 septdecies`, `1463 A`, `1463 B`, `39 decies` G, H, I et J |
| volet échelons locaux | *renvoyé hors phase* | — |
| extinction en trois ans | *titre séparé* | — |

**Éclatable** par dispositif d'aide.

**Ce que l'auteur veut obtenir** : que l'aide s'éteigne, l'entreprise étant par
ailleurs déchargée des impôts de production. **Politiquement, commencer par les
entreprises.** Sur les exonérations, s'en tenir aux chiffres de la Cour des
comptes ; des angles morts peuvent servir ponctuellement sans changer l'équilibre
visé.

---

### M-018 — Aide publique au développement

**Énoncé.** Mettre fin à l'aide publique au développement.

**Paramètres chiffrés.** Économie associée : 3 Md€ à terme, dont 1 Md€ de gain
direct. Rythme : extinction en trois ans.

**Composantes.** Éteindre les crédits — PLF 2de partie, état B, mission Aide
publique au développement. Engagements pluriannuels et contributions
internationales en cours — titre séparé.

**Point de méthode, et il mord ici.** La mission porte des engagements
pluriannuels : l'écart entre autorisations d'engagement et crédits de paiement y
est structurel. **Le levier des crédits est donc épuisé avant d'avoir produit son
rendement, et la mesure appelle un second amendement normatif** qui éteint la
dotation. Les deux se rendent conjoints.

**Ce que l'auteur veut obtenir** : que l'aide cesse, sans redéploiement vers un
autre canal public. **L'enjeu réel est la fermeture de la modalité elle-même.**

---

### M-019 — Aides ciblées aux particuliers

**Énoncé.** Éteindre les aides ciblées aux particuliers, les minima sociaux
demeurant.

**Paramètres chiffrés.**
- économie associée : **19,9 Md€ à terme**, dont 8,4 Md€ de gain direct
- dont aide personnalisée au logement 16,1 Md€, sortie en trois ans ; chèque énergie 0,6 Md€
- perte moyenne par bénéficiaire : environ 80 € par mois
- gain de salaire net simultané : 300 € par mois, soit un solde de **+220 € par mois**

**Composantes et jambes.**

| composante | jambe | siège |
|---|---|---|
| éteindre les aides au logement et à l'énergie | PLF 2de partie | **ouvert — article 81 du PLF 2027, code de l'énergie `L. 124-1-1`, qui est le chèque énergie lui-même ; articles 74 et 78, code de la construction et de l'habitation `L. 823-4` et `L. 822-8`, et code de la sécurité sociale `L. 842-3`** |
| supprimer les crédits correspondants | PLF 2de partie | état B |
| sortie en trois ans de l'aide au logement | *titre séparé* | — |

**Éclatable** par aide.

**Transition, arrêtée par l'auteur** : suppression pour tout nouveau bail ;
extinction à début de bail plus trois ans dans le privé, de six mois à trois ans
dans le social selon l'ancienneté — plus vite idéalement, puisqu'il faut aussi
relever les loyers, et d'abord pour les non-allocataires.

**Ce que l'auteur veut obtenir** : que l'aide ciblée soit remplacée par du revenu
libre d'emploi, et non par une aide ciblée simplifiée. **C'est l'interdiction du
chèque fléché, et c'est la dernière roue de la concentration.**

**Borne ouverte** : lesquels des minima sociaux demeurent.

---

### M-023 — Hébergement d'urgence

**Énoncé.** Ramener l'hébergement d'urgence financé sur l'impôt à un socle.

**Paramètres chiffrés.**
- socle conservé : **20 %**, réservé aux femmes victimes de violences, enceintes ou avec enfant en bas âge
- économie associée : 2,5 Md€
- places du parc : 203 000 ; part réservée aux femmes vulnérables aujourd'hui : 7 % ; part occupée depuis plus d'un an par la même personne : la moitié

**Composantes.** Ramener les crédits au socle — PLF 2de partie, état B, mission
Cohésion des territoires. Définir le public du socle conservé — PLF 2de partie,
article additionnel, code de l'action sociale et des familles.

**Règle de rédaction, et elle est expresse.** La baisse de crédits **se calcule
avec 20 %, mais le taux n'entre pas en dur dans la loi.** Même modalité d'action
que les subventions aux associations.

**Ce que l'auteur veut obtenir** : que l'hébergement financé sur l'impôt soit
réservé aux situations d'urgence réelle.

**Borne ouverte** : le socle à 20 % est-il un critère ou un quantum.

---

### M-026 — Niches fiscales et sociales

**Énoncé.** Abolir les niches fiscales et les niches sociales.

**Paramètres chiffrés.**
- niches dénombrées : **486** — 465 plus 21 taux réduits de TVA
- suppression immédiate : **72,2 Md€** ; solde supprimé dans la refonte : 53 Md€
- niches sociales sur les compléments de salaire : 18 Md€
- cible totale : **143,2 Md€** ; part restituée aux travailleurs : 52 Md€, **net de recyclage**
- multiplicateur retenu sur les assiettes optimisables : 0,5
- niches dont le coût est inconnu de l'administration : **une sur huit**
- part des crédits d'impôt versés par chèque : 45 %

**Champ, arrêté.** Les secteurs écartés sont **différés et non sortis du champ** :
exception de calendrier, non d'assiette. **Aucune niche n'est conservée**, la
promesse d'intégralité tient, et les 52 Md€ restitués ne bougent pas, étant déjà
nets de ce champ. La liste du classeur — hors outre-mer sauf crédits et réductions
d'impôt, hors agriculture, hors emploi à domicile et garde d'enfant — est une
**hypothèse de chiffrage** : elle sert l'exposé, et une part lui revient au
dispositif si la progressivité s'écrit secteur par secteur.

**Cadrage de la progressivité** : de un à trois ans selon les cas. Le découpage —
quelle durée pour quel secteur, et par secteur ou en bloc — **se propose par le
fil qui rédige et se confirme par l'auteur**. La fourchette est un cadre de
travail, pas un paramètre à écrire en l'état.

**Composantes et jambes.**

| composante | jambe | siège |
|---|---|---|
| abroger les niches fiscales | **PLF 1re partie** | **le plus largement ouvert de la phase** — articles 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18, 26 et 28. L'article 28 à lui seul porte `199 terdecies`, `199 undecies C`, `244 quater X`, `244 quater Y`, `1395 G`, `150` et `39 decies C` |
| abroger les niches sociales, dont celles sur les compléments de salaire | **PLFSS**, plus une jambe CGI | **ouvert côté PLF — article 2 : CGI `80 duodecies`, `80 quinquies`, `81`, et code de la sécurité sociale `L. 136-8` ; article 49 : `L. 131-8`.** Le PLF ouvre lui-même deux sièges du code de la sécurité sociale |
| source de gage de la liasse | *transversal* | se décrémente dans l'ordre de dépôt |
| deux vitesses — suppression immédiate d'un côté, extinction progressive avec restitution renvoyée à la refonte de l'autre | *titre séparé* | — |

**Éclatable** par impôt d'assiette, avec solde par impôt.

**Verbe à considérer en premier : `neutraliser par clause générale`.** La fonction
exige un ensemble exhaustif et l'annexe 2027 n'existe pas. La clause de
non-application — toute réduction, tout crédit, tout abattement, toute exonération
et tout taux réduit applicables à un impôt, à compter d'une date, sans les nommer
— est la forme qui tient. **Trois sorties obligatoires** : la clause, la liste des
effets de bord non coordonnés, et le repli énuméré avec son motif de
non-rédaction.

**Ce que l'auteur veut obtenir** : que la niche disparaisse sans compensation
catégorielle, le rendement libéré finançant la baisse générale.

**Règle expresse** : **ne pas parler des pensions dans l'exposé.**

---

### M-001 et M-004 — les deux bornes de la phase

**M-001, périmètre de l'État.** Sept missions conservées — défense, intérieur,
justice, affaires étrangères, comptes publics, solidarité nationale, enseignement
— et missions facultatives interrompues. Économie visée 236 Md€ par an en année
pleine, 14 % des dépenses publiques, moitié de l'économie la première année.
**C'est l'enveloppe du programme, pas un dispositif.** Le dispositif est la somme
des mesures qui suivent ; il ne se complète pas ici.

**M-004, établissements à patrimoine et revenus propres.** Environ 300
établissements — musées, universités, instituts de recherche — laissés autonomes.
**C'est une exclusion de champ opposable aux autres mesures**, et elle se nomme en
extension. **Borne ouverte** : le périmètre exact.

---

## 7. Ce qui reste ouvert, et qui n'est pas à la chaîne

**Quatre bornes de fond.** Le périmètre des ~300 établissements exclus. Le coût de
l'indemnité des agents. Lesquels des minima sociaux demeurent. Le socle de
l'hébergement d'urgence, critère ou quantum.

**Trois décisions de rédaction que le fil propose et que l'auteur confirme.**
L'ordre des critères d'organisation de la liste close de M-002. Le découpage de la
progressivité de M-026. Le montant du versant social de M-016.

**Un manque de pièce, et il est gratuit.** Les amendements déposés sur les deux
textes ne sont pas ouverts.

**L'ordre de dépôt n'est pas arrêté.** `ordre_depot` vaut « à fixer ».

---

*Valise projetée en clair : arguments et chiffres sourcés, sans nomenclature
interne. Les identifiants de mesure sont des identifiants locaux de dossier, sans
signification. Aucune sortie de la chaîne ne nomme un déposant, une organisation
ou une source interne.*
