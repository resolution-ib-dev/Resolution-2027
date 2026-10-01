# Registre des arbitrages — archive

Les entrées **antérieures au 20260901**, détachées du registre courant le
20260904 parce que le registre entier ne repassait plus au coffre : sa taille
dépassait la marge de la jauge, mesurée au refus du versement.

**Elles valent exactement comme les courantes** — une question qui figure ici ne
se repose pas davantage. Le registre courant est `methode/arbitrages.md`, et il
renvoie ici.

Le plus récent en tête.

---

## 20260831 — L'adresse se décompose, et le code ne s'affirme jamais

### A-250 — J'affirmais « code général des impôts » sur 465 dépenses fiscales, et c'était faux sur 55

**Relevé par l'auteur** : « ton état vecteurs n'est pas partout assez complet
sur le champ source : il ne dit pas de quel code on parle ! »

Il est plus grave que ce que le reproche dit. `ref_norme.py` posait
`texte='code général des impôts'` sur les 465 dépenses fiscales, avec une note
qui avouait le procédé — « le code n'est pas nommé par l'annexe : il se déduit
de la numérotation ». **C'était une affirmation, pas une déduction, et elle est
fausse sur 55 entrées.**

Vérifié sur pièce le jour même : les articles `L. 312-xx` et `L. 421-xx` sont au
**code des impositions sur les biens et services** — accises sur les énergies,
taxes sur les véhicules — et `L. 2333-55-3` au **code général des collectivités
territoriales**. Un amendement rédigé sur cette base aurait visé un article du
CGI qui n'existe pas.

**C'est exactement ce qu'A-245 interdit**, et je l'ai écrit le matin même : *un
vecteur vraisemblable est plus dangereux qu'un vecteur absent, il a l'apparence
d'une adresse et il envoie l'amendement au mauvais endroit.*

**La correction.** `vecteurs.DEDUCTION_CODE` porte une table de règles, chacune
avec son motif, son code, son identifiant Légifrance, son siège, **sa date de
vérification et la requête qui l'a établie**. Chaque vecteur déclare la règle
qui l'a produit. **Ce qu'aucune règle ne couvre sort en `indéterminé`** — jamais
en CGI par défaut.

Après correction : 617 CGI · 94 code des impositions sur les biens et services ·
8 textes non codifiés, où la loi de finances est elle-même le vecteur · 1 code
général des collectivités territoriales · **4 indéterminés**, qui sont des
renvois à la doctrine administrative et un vrai résultat.

*Contrôle neuf* : **`N9` compte les codes indéterminés et refuse un vecteur dont
la règle de déduction n'est pas déclarée.** Un code posé sans règle est un échec.

### A-251 — L'adresse se décompose du macro au micro, et rien ne se recolle

**Exigé par l'auteur** : « du macro code au micro ° d'alinéa, il faut être très
précis pour que la procédure soit robuste. »

Quatre niveaux, quatre colonnes : **code · siège · article · subdivision**.
`158-5-a` n'est pas une adresse, c'est trois niveaux collés — et une disposition
modificative ne vise pas le même objet selon qu'on abroge l'article, le 5 ou
le a.

**Aucune épissure de chaîne.** La première version recollait un fragment
orphelin sur un radical tronqué et fabriquait `L. al.3` à partir de
`L. 312-35, al.3`. Un fragment qui ne commence pas par un numéro est désormais
une **subdivision de l'article précédent**, écrite comme telle ; l'article ne se
réécrit jamais.

*Trois corrections de découpage que le contrôle a sorties, chacune un faux
possible.* La lettre de partie est bornée à **L, R, D** — `A 2°` est une
subdivision, pas un article de partie A, et `[LRDA]` la lisait comme un numéro.
Un nombre nu suivi du signe ordinal — `2°` — est une subdivision. Et le numéro
admet un suffixe après l'ordinal, faute de quoi `278 sexies-0 A` se coupait en
`278 sexies` plus une subdivision `0 A`.

**Résultat mesurable** : `278 sexies – II. A 1°, A 2°, B 1° et B 2°, III,
278 sexies-0 A et 278 sexies A – I 1°, 2°, 3° a, 4°, 5°, 6° et II` se décompose
en **treize adresses justes**, article et subdivision séparés. `N2` sort zéro
référence de forme non reconnue.

### A-252 — L'état des vecteurs est une table plate, exportable telle quelle

**Demandé par l'auteur** : « il faudrait que la structure de l'état soit bien
tableau pour être quasi exportable au besoin. »

`livrables/etat_vecteurs.csv` — **une ligne par vecteur, seize colonnes
atomiques**, rien d'imbriqué et rien de collé : population, clé, libellé,
régime, rôle, code, identifiant du code, siège, article, subdivision,
provenance, confiance, variante, strate, date de relevé, montant. 880 lignes.

La page HTML rend la même table ; le CSV est le même contenu sans mise en forme.
**Un seul point de vérité, deux rendus** — ils ne peuvent pas diverger,
puisqu'ils sortent de la même fonction.

*Ce que l'auteur valide au passage, et qui reste* : la séparation création /
financement, « pour le fameux faire feu de tout bois ». Un organisme a souvent
deux vecteurs et l'économie porte presque toujours sur le second.

### A-253 — La variante « dans l'absolu » ou « article ouvert » est une colonne, pas un raffinement

**Arbitré par l'auteur** : « la dichotomie dans l'absolu / article ouvert en PLF
doit être identifiée et distinguée. Ça fait partie du macro travail de
structure. »

Elle n'attend donc pas le fil 2 pour exister : **la colonne `variante` est au
référentiel dès maintenant**, à trois valeurs — `absolu` pour un article
additionnel, `article_ouvert` pour un article que le texte déposé rouvre,
`a_determiner`.

Elle vaut `a_determiner` partout, et c'est honnête : **sans le socle du texte on
ne sait pas quels articles sont ouverts**. Ce qui compte est qu'elle soit là et
qu'elle se compte, plutôt que d'être ajoutée après coup sur mille huit cent
entrées.

*Une source partielle et gratuite, relevée par l'auteur* : les liasses de
Génération Libre **appellent elles-mêmes des articles du PLF 2026**. Elles
portent donc, en creux, une première liste d'articles ouverts — avant même le
fil 2, et pour le coût d'une lecture.

### A-254 — L'éval du vecteur est une correspondance dure ; celle de la rédaction ne l'est pas — *précise A-249*

**Relevé par l'auteur** : « pour la rédaction de disposition, l'objectif sera de
voir la correspondance, de s'inspirer, pas de rechercher une égalité de
rédaction dans l'absolu — il y a autant d'avis que de rédacteurs. Ça reste un
travail juridique lourd. »

**Les deux évals ne se jugent pas pareil, et A-249 ne le disait pas.**

**`vecteur-mesure` se juge dur.** L'article est l'article : concordance,
voisinage, discordance, et un taux de rappel sur 39 cas. Il n'y a pas deux
manières de désigner `L. 312-48`.

**`disposition-cible` ne se juge pas ainsi.** Deux rédacteurs écrivent deux
dispositions différentes qui produisent le même effet de droit ; une égalité de
texte n'est ni atteignable ni souhaitable. Ce qui se compare est **la
correspondance** — même article visé, même opération (abroger, remplacer,
compléter), même portée. La rédaction de Génération Libre est **un modèle dont
on s'inspire, pas un corrigé**.

*Et cela se dit franchement* : la rédaction reste un travail juridique lourd. La
skill l'outille, elle ne l'automatise pas — et une skill qui prétendrait le
contraire ferait sortir des dispositions plausibles et fausses, ce qui est le
pire des deux mondes.

### A-255 — Ce que j'ai fait sur les skills, et ce que je n'ai pas fait

**Question de l'auteur** : « là j'ai l'impression que tu as déjà avancé sur la
skill, mais c'est peut-être superficiel. »

**Aucune skill n'est écrite.** Ce qui existe est ce qu'une skill envelopperait,
et rien de plus : la **procédure** (`methode/procedure_vecteurs.md`),
l'**appareil** (`vecteurs.py`, `ref_norme.py`, `controle_norme.py`,
`generer_etat_vecteurs.py`), le **référentiel** (`REF_norme.json`, 1 856
entrées) et un **lot pilote** de onze cibles relevées sur pièce.

C'est la matière, pas l'outil. La skill se rédige au fil suivant, et elle sera
d'autant plus courte que la procédure est déjà écrite.

## 20260831 — La chaîne de l'amendement : trois skills, et une éval qui se mesure

### A-247 — Trois skills séparées, et la ligne avec `redaction-legistique` est le type d'objet

**Arbitré par l'auteur**, contre ma proposition de deux. J'avais recommandé deux
skills neuves plus la reprise de `redaction-legistique` pour le dispositif.
**Je sous-estimais la différence entre une proposition de loi et un
amendement** : ce ne sont pas le même objet, ni la même longueur, ni le même
gabarit, ni la même contrainte de recevabilité. La reprise que je proposais
aurait fait porter à une skill de texte déposable un travail d'amendement.

**Trois skills, chacune s'arrêtant à un produit qui se contrôle seul.**

| skill | entrée | sortie |
|---|---|---|
| `vecteur-mesure` | un énoncé en langage naturel — « plafonner la taxe XYZ », « supprimer l'ADEME », « diviser par deux les subventions à XXX » | la ou les **adresses** à modifier : population, cible jointe au socle, rôles, texte, articles, identifiant Légifrance, provenance, collisions connues |
| `disposition-cible` | une adresse et une intention | le **dispositif** de l'amendement — disposition modificative, style SGG |
| `expose-sommaire` | dispositif, rattachement, chiffrage | l'**exposé sommaire**, gabarit à trois temps, 200 à 300 mots |

**`redaction-legistique` garde son objet et ne bouge pas** : le texte déposable
complet — révision constitutionnelle, loi organique, loi ordinaire —, avec son
exposé des motifs. Une proposition de loi n'est pas un amendement.

*Ce que la séparation achète, et c'est la raison de l'auteur* : **chaque étape
s'exporte et s'éprouve seule.** Une chaîne d'un seul tenant ne se mesure pas —
et l'éval sur les exposés des motifs de Génération Libre exige précisément
d'isoler la première étape.

**Deux contraintes portées à l'écriture, et elles ne se contournent pas.**

`vecteur-mesure` **joint au socle avant de chercher.** Si la cible est aux 1 856
entrées de `REF_norme`, le vecteur y est peut-être déjà. Chercher d'abord
gaspillerait, et surtout **chaque recherche neuve doit enrichir
`appareil/vecteurs.py`** : la skill capitalise, elle ne repart pas de zéro à
chaque emploi.

**La version exportable ne lit pas `vecteurs.py`.** Nos régimes de suppression
sont la doctrine sous forme de tableau, et A-232 les exclut du pack public. La
skill publique part donc des **annexes publiques et de Légifrance seuls**. Deux
versions, ou une qui dégrade proprement — *à trancher à l'écriture, et le fil le
dira.*

*Dépendance qui commande la moitié de la première skill* : la variante
« depuis le texte déposé » — amender un article que le PLF ouvre déjà (A-228) —
**suppose le fil 2**. Sans le socle du texte, on ne sait pas quels articles sont
ouverts. La skill part avec sa moitié « article additionnel » et reçoit l'autre
quand le fil 2 aura tourné.

### A-248 — Le contre-budget 2026 de Génération Libre entre par pièce jointe

**Fourni par l'auteur** : `generationlibre.eu/contrebudget2026`. Relevé sur la
page : **39 mesures, en trois liasses PDF** — amendements PLF partie I,
amendements PLF partie II, amendements PLFSS. **Rien n'est sur la page
elle-même**, qui est un portail de distribution.

**Elles n'entrent donc pas par l'outil de récupération** — A-234, et de toute
façon la page ne les porte pas. **Trois pièces jointes, déposées par l'auteur.**

Ce qu'elles apportent, et c'est triple. Le **gabarit réel** du dispositif et de
l'exposé sommaire, à caler contre `sources/gabarit_expose_sommaire.md`, qui est
une digestion et non un exemplaire. L'**ordre de grandeur des baisses de
crédits**, qui sert directement le lot V1 (A-243). Et la **vérité-terrain** de
l'éval ci-dessous.

*Ce qu'elles ne remplacent pas* : notre doctrine. Un amendement GL dit ce que GL
propose ; nos mesures viennent du `REF_doctrine`. Les liasses sont un modèle de
forme et une source de vérification, jamais une source de fond.

### A-249 — L'éval des vecteurs se fait sur les exposés des motifs seuls, et elle donne un taux de rappel

**Proposé par l'auteur, et c'est le bon dispositif.** « Tester ces skills sur
les EDM seuls de GL et voir si on retrouve bien les articles cités dans les
amendements et/ou le texte initial. »

**Le protocole.** On donne à `vecteur-mesure` **l'exposé des motifs seul** —
qui décrit la mesure sans nommer l'article. On compare l'adresse qu'elle sort à
celle que le dispositif de l'amendement cite. Le dispositif est la vérité, et il
n'a pas été montré à la skill.

**Trois verdicts, et un seul est un succès.**

- **Concordance** — même article, ou l'article cité est dans la fourchette
  relevée.
- **Voisinage** — même code, même section, article différent. À lire : c'est
  souvent le rôle qui diffère — création contre financement (A-245) — et non
  une erreur.
- **Discordance** — autre chose. Échec, et il se compte.

**Le résultat est un taux de rappel sur 39 cas**, et il se dit tel quel. C'est
exactement A-95 : *un appariement qui ne sait pas se mesurer est un appariement
qu'on croit sur parole.* Un dispositif de vecteurs non mesuré vaudrait la même
chose.

*Deux gardes à tenir à l'exécution.* Les liasses portent le dispositif **et**
l'exposé des motifs dans la même pièce : l'extraction doit **séparer les deux
avant** de rien montrer, sinon l'éval se donne la réponse à elle-même. Et
l'éval se joue **avant** que les vecteurs des cibles GL entrent à
`vecteurs.py` : une cible déjà relevée sortirait un succès qui ne prouve rien.

## 20260831 — Les crédits sont des mesures, et les vecteurs ont leur procédure

### A-243 — Une mesure de crédits est de plein exercice et de rang législatif — *amende A-241*

**Relevé par l'auteur.** « Les mesures en crédits sont des vraies mesures, en
effet les plus simples, des amendements de chiffres avec des baisses, ça se fait
facilement et ça doit être fait en L. Inutile de dire que c'est infra-L parce
que c'est des plafonds, on veut un truc mordant. »

A-241 rangeait les 128 programmes en « aucun vecteur ». **La formule était
juste techniquement et fausse de portée** : elle laissait entendre qu'une mesure
de crédits serait de rang inférieur parce qu'elle ne modifie pas d'article de
code.

**Elle est de rang législatif, et le dire autrement affaiblit le contre-PLF.**
L'état B est voté, il fait partie de la loi de finances, et les crédits qu'il
ouvre sont limitatifs.

Le vecteur devient donc **`non codifié`** et non plus `aucun` : l'état B annexé
à l'article de crédits du budget général, mission puis programme. Il est
parfaitement déterminé, il est le même pour les 128, et `REF_norme` le porte en
`trouve`.

*Ce que cela change en pratique* : le lot des crédits est **le plus simple et le
plus mordant**, pas le moins sérieux. Une ligne, une baisse. Aucune disposition
modificative, aucune recherche. Et l'article 40 ne mord pas dessus : il mord sur
l'augmentation d'une charge, pas sur sa réduction.

*Ce qui se mobilise* : **le contre-budget 2026 de Génération Libre**, s'il porte
des amendements de crédits déjà rédigés, donne le gabarit et l'ordre de
grandeur. *Il n'est pas au corpus ; il entre par pièce jointe, et l'auteur dira
quand.*

### A-244 — Notre chiffrage oriente la baisse, il ne la conditionne pas

**Arbitré par l'auteur** : « tu noteras sur les chiffres qu'on a estimé avec ce
qu'on pouvait, la réalité du PLF 2027 sera un peu différente mais ça ne devra
pas bloquer les mesures. »

**Le montant d'un amendement de crédits se reprend au projet de loi de finances
en discussion, jamais au nôtre.** Notre chiffrage est fait sur le PLF 2026 ; le
texte qu'on amendera portera d'autres chiffres.

**Conséquence, et c'est une règle de conception** : une mesure ne se paramètre
pas sur un montant en dur. Elle se paramètre sur **la ligne** — mission,
programme, catégorie — et sur **la règle de baisse** : un taux, une part
supprimable, une cible. Le montant se recalcule au millésime.

*Ce que cela protège* : un écart entre notre chiffre et celui du PLF de l'année
n'invalide ni la mesure, ni le rattachement, ni le vecteur. **Il ne se corrige
pas non plus en silence** — il se relève, exactement comme un écart entre le
montant de l'état et celui de l'exposé des motifs (A-230).

*Ce que cela n'autorise pas* : le financement, lui, boucle et ne bouge pas
(A-224). Le gage se recycle, le chiffrage se recalcule, mais **l'addition du
contre-PLF doit tomber** sur le texte réel.

### A-245 — La procédure des vecteurs : quatre provenances, huit contrôles, et la recherche ne passe pas par script

**Demandé par l'auteur** : « il faut que tu systématises et contrôles pour tout
le corpus, par étape le cas échéant. » `methode/procedure_vecteurs.md`.

**Le vecteur est un identifiant, jamais du verbatim**, et c'est ce qui rend la
recherche légitime : A-234 dit que l'outil de récupération repère et ne copie
pas. Chercher une adresse est du repérage. Le texte de l'article, lui, entrera
par pièce jointe le jour où le trois colonnes le demandera.

**Vérifié, et cela borne l'appareil** : le shell de l'atelier n'atteint ni
Légifrance ni un moteur de recherche — la passerelle n'admet que les registres
de paquets (A-196). **Un script ne trouvera donc jamais un vecteur** ; il dérive,
il joint, il contrôle. La recherche se fait par l'outil du fil.

**Quatre provenances**, sur le dispositif des niveaux de confiance de
`REF_chiffres` : `3 annexe` dérivé et revérifiable sans réseau · `2 legifrance`
relevé avec son identifiant et sa date · `1 corpus` porté par une pièce ·
`0 a_trouver`. **Aucun vecteur ne s'invente** : un vecteur vraisemblable est
plus dangereux qu'un vecteur absent, il a l'apparence d'une adresse et il envoie
l'amendement au mauvais endroit.

**Cinq rôles**, parce qu'un organisme a souvent deux vecteurs et que l'économie
porte sur le second : création, financement, compétence, montant, dérogation.
Les agences de l'eau sont créées par une section du code de l'environnement et
financées par une autre — **supprimer l'organisme et supprimer sa ressource ne
se font pas au même endroit**.

**Huit contrôles**, `N1` à `N8`, joués à `make controle`. `N4` est le seul
total : il rejoue la dérivation depuis l'annexe et compare. `N1` est celui
qu'A-227 demande — il refuse qu'un vecteur codifié nomme un véhicule.

**Ce que le contrôle ne peut pas voir, et qui se dit** : si l'article existe
encore, s'il a été recodifié. D'où la date de relevé obligatoire, et la règle :
**un vecteur de plus d'un an se rejoue avant rédaction** ; un vecteur qui sert à
un amendement déposé se rejoue la semaine du dépôt.

*Coût mesuré, non estimé* : le lot pilote a demandé **une recherche par cible,
onze cibles, onze réponses au premier essai**, et rendu dix-huit vecteurs.
**Le titre de section de Légifrance nomme lui-même la cible** — « Section 3 :
France compétences », « Chapitre V : Impositions affectées au Centre national du
cinéma » — et quand il la nomme, la fourchette d'articles qui suit est le
vecteur, sans interprétation.

*Étape 0 close le jour même* : `REF_norme` porte **1 856 entrées et 621
vecteurs**. Les 465 dépenses fiscales et les 128 programmes sont couverts à
100 % ; les onze organismes relevés couvrent **les onze lignes d'économie
d'opérateur qui nomment une cible, 22,7 Md€** — la douzième est le résidu
« autres », qui n'a pas d'assiette nommée et ne peut donc pas avoir de vecteur.

### A-246 — Les premiers contrôles ont trouvé, et deux défauts étaient les miens

Constaté, et cela vaut d'être écrit parce que c'est la preuve que le dispositif
mord.

**Le contrôle de jointure a refusé deux clés que j'avais recopiées d'un
arbitrage au lieu du socle.** J'avais écrit « ODAC-730 · Chambres consulaires »
et « ODAC-731 · Établissements publics fonciers », d'après le tableau d'A-114 ;
le socle porte « Chambres consulaires 273 » et « Etablissements publics fonciers
40 ». La jointure sur le libellé exact a sorti les deux en échec au lieu de les
apparier au plus proche — **c'est A-94 qui tient**, et sans elle deux vecteurs
justes auraient été rattachés à rien.

**`N2` a trouvé un défaut de mon propre découpage.** Il sortait 79 références de
forme non reconnue — « D », « b », « VI ». Ce n'était pas l'annexe : mon
découpage sur la virgule fragmentait « art. 199 undecies B, C, D » en un article
et deux lettres orphelines. Corrigé : une référence qui ne commence pas par un
numéro est une **subdivision de la précédente**. Et la grammaire des ordinaux
latins s'est allongée jusqu'à `duotricies`.

**Ce qui reste après correction est un vrai résultat** : **31 dépenses fiscales
sur 465 portent, à l'annexe, autre chose qu'une adresse d'article** — un renvoi
à la doctrine administrative (`BOI-…`, `DB…`), une mention d'alinéa, du texte
libre. **20 d'entre elles portent un régime de suppression, pour 4,25 Md€.** Le
lot V2 est donc à 100 % de références et **93 % d'adresses exploitables**, et
c'est cette seconde grandeur qui compte.

**Et `N6` a sorti ce qu'aucune lecture par mesure n'aurait montré** : **55
articles du code général des impôts sont visés par plus d'une dépense
fiscale**. Deux amendements qui abrogeraient le même article se neutralisent ou
se contredisent. *C'est exactement le risque que la colonne vecteur est faite
pour voir, et il apparaît dès la première exécution.*

## 20260831 — Les collocs rentrent par la ressource, et le vecteur se mesure

### A-239 — La dépense locale ne se vote pas en loi de finances, mais ce qui la finance y est — *amende A-237*

**Relevé par l'auteur, et c'est une correction de fond.** « Certes on ne peut
tout diligenter directement, en revanche beaucoup de choses intersectent du
budgétaire ou du fiscal classique par la magie du millefeuille, des
cofinancements et du cadrage, donc à exploiter autant que possible. »

A-237 rangeait les 39,5 Md€ du périmètre des collocs en « hors véhicule
financier de l'État » et s'arrêtait là. **C'était juste sur la dépense et faux
sur le levier**, et l'erreur de raisonnement se nomme : j'ai cherché le véhicule
de la dépense au lieu de chercher le véhicule de ce qui la produit.

**Quatre prises, et elles n'ont ni le même véhicule ni la même force.**

| prise | ce qu'elle fait | véhicule | force |
|---|---|---|---|
| **la ressource** | réduit ce qui finance, laisse l'arbitrage local | loi de finances | forte en montant, indirecte en effet |
| **le cofinancement** | supprime le crédit d'État qui appelle la dépense | loi de finances | faible en montant, directe en effet |
| **la norme** | supprime la compétence ou l'obligation | loi ordinaire | c'est là que la dépense se prend |
| **le cadrage** | contraint la trajectoire | à trancher | porte non établie |

**Six leviers sur huit ont une porte au domaine**, et leurs montants sont pris
au socle, jamais estimés — `livrables/leviers_collocs.md`.

*Le fait qui emporte la correction, et il était sous les yeux* : **l'auteur a
lui-même classé 86 taxes affectées en régime `Collocs`**, pour 58,25 Md€, dans
le classeur de calculs. Et le 3° bis du I de l'article 34 de la loi organique —
relevé en verbatim le matin même — vise « les impositions de toutes natures
affectées à une personne morale autre que l'État ». **Les collectivités en
sont.** La loi de finances peut en modifier l'assiette, le taux, l'affectation
et les modalités de recouvrement, en première partie, par une porte facultative
donc ouverte. J'avais lu l'exclusion du 5° bis — qui ne porte que sur la reprise
du produit par l'État — comme si elle fermait tout le domaine.

**Deux autres portes s'ouvrent avec.** Les niches sur impôts locaux : 42
dépenses fiscales, 1,44 Md€, **article de code renseigné pour 42 sur 42**. Les
dégrèvements d'impôts locaux : programme 201, 4,62 Md€, **dépense d'État en
totalité**.

**Ce que la correction ne change pas, et qui doit se dire dans l'exposé
sommaire** : réduire la ressource ne commande pas l'emploi. La colloc arbitre,
et elle peut arbitrer contre nous — augmenter un taux, emprunter, ou couper
ailleurs que là où on voulait. C'est la limite du levier de ressource, et elle
se dit plutôt que de se découvrir en séance.

*Ce que la faute enseigne, au-delà du cas* : **on cherche le véhicule de l'effet
budgétaire, pas celui de l'objet.** C'est exactement le test de rattachement
par l'implicite budgétaire (A-225), et je ne l'ai pas appliqué à ma propre
ventilation.

### A-240 — Ce qui est tangent se signale à part et ne se qualifie pas

**Demandé par l'auteur** : « pour ce qui est tangent, tu peux signaler à part et
on verra dans un second temps si j'ai des pistes. »

Un point tangent est une intersection **plausible et non établie** entre une
matière et un véhicule. Le qualifier au jugé le ferait entrer au corpus avec
l'apparence d'un fait ; le taire perdrait la piste. Il se range donc dans un
bloc propre, avec ce qui manque pour le trancher.

Sept sont ouverts sur les collocs — le financement de la fonction publique
territoriale, les retraites des agents territoriaux, les cofinancements
pluriannuels, la TVA affectée en remplacement de la taxe d'habitation et de la
CVAE, les exonérations compensées par l'État, les dépenses prescrites par une
norme d'État, et les solidarités départementales.

**Le plus dangereux est celui des exonérations compensées** : supprimer la niche
sans supprimer la compensation ne rend rien à l'État ; supprimer la compensation
sans la niche transfère la charge à la commune. **Le chiffrage doit dire lequel
des deux il compte**, faute de quoi l'économie est comptée deux fois ou pas du
tout.

*Portée générale* : le bloc des tangents est un dispositif, pas un cas
particulier des collocs. Toute grille du contre-PLF en porte un.

### A-241 — Le vecteur se compte en articles touchés, pas en propositions

Tranché par Claude au titre d'A-23, sur mesure et non sur estimation.

A-227 pose que le vecteur est le gros du travail. **Il l'est, mais pas là où on
le croit**, et le compter le montre. `livrables/chantier_vecteurs.md`.

| lot | population | volume | vecteur connu |
|---|---|---|---|
| **V1** | programmes du budget général | 128 | *aucun vecteur* |
| **V2** | dépenses fiscales à supprimer | 383 | **100 %** |
| **V3** | taxes affectées portant un régime | 232 | 20 % |
| **V4** | organismes à supprimer, internaliser ou vendre | 424 | **0 %** |
| **V5** | propositions du REF_doctrine | 56 | norme cible d'abord |

**Trois faits que l'estimation ne donnait pas.**

**Une mesure de crédits n'a aucun vecteur.** Elle se dépose en amendement sur
l'état B. Ni article de code, ni disposition modificative. Le lot qui porte le
plus de montant est celui qui coûte le moins en légistique.

**Le vecteur des niches est déjà écrit, à 100 %.** L'annexe des dépenses
fiscales porte, pour chacune des 465, l'article du code **et la norme de
référence à laquelle elle déroge**. 383 portent un régime de suppression, et
toutes portent leur article. **Ce lot ne se cherche pas, il se convertit** — un
script lit l'annexe et remplit la colonne vecteur.

**Le chantier réel est ailleurs : 608 vecteurs à trouver, dont 424 organismes**,
soit 69 % dans une seule population qu'aucune de nos pièces ne documente. Ni
l'annexe des opérateurs ni la liste ODAC-ODAL ne nomment le texte fondateur, et
un appariement par libellé se tromperait (A-94).

*Conséquence d'appareil, tranchée ici* : **`REF_norme` porte quatre valeurs
d'état du vecteur et non trois.** A-227 en pose trois — trouvé, à trouver,
inexistant. Il en faut une quatrième, **`sans objet`**, pour les mesures de
crédits, qui n'ont pas de vecteur et ne sont pas pour autant en défaut. Sans
elle, les 128 programmes sortiraient en manque à chaque contrôle.

*Conséquence sur la révision du code général des impôts préparée par l'expert* :
elle reste à verser, et **la question qu'on lui pose change**. Les vecteurs des
niches sont déjà connus ; elle est donc précieuse ailleurs — sur les articles
que la fiscalité à quatre impôts réécrit, et qui ne sont pas des dépenses
fiscales. À instruire sur ce périmètre-là.

### A-242 — Le récapitulatif de transposabilité couvre un axe, à une autre maille

Constaté sur pièce, pas rapporté. `sources/Recap_transposabilite_20260731_v6.md`
**fait déjà le travail de `REF_norme`, et il le fait bien** — mais sur le seul
axe du consentement à l'impôt, et à une maille qui n'est pas celle des
propositions.

Il porte 59 mesures issues de 11 mécanismes de la révision : 44 compatibles à
Constitution inchangée, 7 incompatibles, 8 sans objet. **Son tableau VII est
exactement le format cible** — une ligne par texte, la liste des mesures qu'il
porte : 19 articles de la loi organique, une loi organique nouvelle, une
ordonnance organique, deux codes.

**Ce qui s'en reprend sans rien refaire** : le format, la distinction
compatible / incompatible / sans objet, et surtout **la notion de repli avec son
écart déclaré**, que `REF_norme` ne prévoit pas. Un vecteur inexistant appelle
un repli, pas un abandon.

**Ce qui manque** : tous les autres axes — social, fiscal, local, fonction
publique, éducation, patrimoine. Le récapitulatif ne les a jamais visés, et
c'est normal : il était l'annexe d'une révision constitutionnelle, pas d'un
contre-PLF.

## 20260831 — Ce que le premier fil de production a tranché en propre

### A-236 — Un verbatim se relève par repère, et un document long s'ouvre par script

Tranché par Claude au titre d'A-23, sur deux occasions du même fil, et c'est la
même règle.

**Pour citer un texte normatif, le module ne porte que le repère.** La grille
des portes demandait vingt-huit citations de la loi organique. Les écrire dans
le module serait les faire passer par le modèle, une fois à l'écriture et une
fois à chaque relecture. `appareil/portes_domaine.py` ne porte donc **aucune
phrase de loi** : il porte, par porte, un fragment littéral attendu au texte, et
le verbatim est découpé de la pièce et recopié à l'octet. **Un repère qui ne se
retrouve pas arrête la génération** et sort la porte en échec, plutôt que de la
composer.

C'est exactement A-91 — une hypothèse porte un repère, jamais le verbatim —
étendu du manuscrit aux textes normatifs. *Et le contrôle qui va avec est
mécanique* : une seconde passe indépendante recherche chaque ligne citée du
livrable dans la pièce dé-balisée, et compte celles qui s'y retrouvent
littéralement. Vingt-huit sur vingt-huit.

**Pour ajouter un bloc à un document long, on ouvre par script.**
`appareil/porter_bloc.py` insère un bloc après la préface du registre ou du
journal, et recolle le reste sans jamais le relire. Le registre fait près de
deux cent mille octets et le journal cent mille : les réécrire à travers le
modèle pour y ajouter treize entrées est précisément ce qui a produit, le
20260824, des règles de rédaction réécrites en silence (A-38).

Deux gardes, et elles ne se contournent pas. Le point d'insertion est nommé, pas
deviné — s'il ne se trouve pas là où il est attendu, rien n'est écrit. Et la
découpe est vérifiée conservative avant l'écriture.

*La preuve se prend après, et de l'extérieur* : le document neuf privé du bloc
doit redonner l'empreinte que le coffre porte. Les deux l'ont fait —
`a1b7ede2…` pour le registre, 196 533 octets et 3 818 lignes ; `9757812c…` pour
le journal, 99 266 octets et 1 733 lignes. C'est plus fort qu'une inspection :
cela compare le document à ce que le coffre portait, sans passer par ce que la
session croit savoir (A-46).

### A-237 — La ventilation par véhicule a quatre valeurs, et la quatrième est un résultat

Tranché par Claude au titre d'A-23. Ventiler les lignes d'économie entre le PLF
et le PLFSS suppose que les deux textes les couvrent. **Ils ne les couvrent
pas.**

Quatre valeurs, donc : `plf`, `plfss`, `a_trancher` — la ligne agrège des flux
des deux côtés et le partage se fait sur pièce —, et **`hors`**, qui dit
qu'aucun des deux véhicules ne porte la dépense.

**La quatrième n'est pas un échec de ventilation, c'est le résultat le plus
utile du relevé** : elle dit ce qu'un contre-PLF ne peut pas faire, et donc ce
qui demande un autre texte. Elle vaut 39,5 Md€ — le périmètre des collectivités
locales entier. Une dépense communale ne se vote pas en loi de finances ; l'État
n'y agit que par le prélèvement sur recettes, qui **réduit la ressource sans
commander l'emploi**, ou par la norme, en loi ordinaire.

*Écarté* : ranger les dépenses locales en `plf` au motif que le prélèvement sur
recettes est en loi de finances. Le prélèvement est un levier sur la ressource,
non une porte sur la dépense — les confondre ferait croire qu'un amendement de
loi de finances peut supprimer une dépense culturelle communale.

*Écarté aussi* : arbitrer les huit lignes mixtes. Le partage entre crédits et
exonérations de cotisations est une question de fait qui se lit sur pièce, et
quatre des huit sont des résidus « autres » que le classeur ne détaille pas. Le
fil les inscrit, avec leur question, et s'arrête.

### A-238 — Les trois livrables du fil restent au bac à sable

Tranché par Claude au titre d'A-23, en application directe d'A-22 : un travail
de Claude reste au bac à sable tant qu'il n'a pas été relu.

`livrables/portes_domaine.md`, `livrables/axe_transparence.md` et
`livrables/ventilation_vehicule.md` sont des dérivés, hors coffre (A-71) : ils
se régénèrent à l'identique depuis des pièces qui y sont, ou depuis les pièces
jointes du projet. Ils passeront en output — et pour la grille des portes, au
pack public — quand l'auteur les aura relus.

**Les deux documents écrits à la main vont au coffre**, eux, parce que rien ne
les refait : `methode/test_rattachement.md`, et
`methode/procedure_contre_plf.md`, qui était versée depuis le matin et
qu'aucune ligne de l'index ne déclarait.

*Rangement des quatre modules neufs, au même titre* : `portes_domaine.py` et
`ventilation_vehicule.py` portent de la matière écrite à la main — les repères,
la ventilation ligne par ligne — et vont en **grilles**, comme `apports.py` et
`sources_chiffres.py`. `axe_transparence.py` et `porter_bloc.py` ne font que
relever et placer : **outillage**.

## 20260831 — Le contre-PLF : deux textes, deux questions, et par où entre le verbatim

*Treize décisions prises au fil de conversation du 20260831, portées au registre
par le premier fil de production, par script et sans recopie du reste (A-38).
Leur exposé complet est à `methode/procedure_contre_plf.md`.*

### A-223 — Le PLFSS entre au périmètre, et le PLF reste prioritaire

**Arbitré par l'auteur.** Le chantier double de véhicule : le projet de loi de
financement de la sécurité sociale entre au périmètre, **à parité d'appareil**
avec le projet de loi de finances — mêmes grilles, même extracteur, même
qualification.

**Le PLF est prioritaire, et cet ordre ne se rediscute pas.** On fait les deux,
dans cet ordre.

*Conséquence de dérivation* : la grille des portes du domaine se relève deux
fois — sur la loi organique relative aux lois de finances pour le PLF, sur
l'article LO 111-3 du code de la sécurité sociale pour le PLFSS.

### A-224 — Le gage de recevabilité et le financement réel sont deux objets distincts

**Arbitré par l'auteur, en réponse à une réserve de Claude.**

**Le gage de recevabilité est un prétexte.** Il est approximatif, il se
réutilise d'un amendement à l'autre, et **il ne s'additionne pas**.

**Le financement vient du chiffrage.** Il boucle sur `referentiels/economies.json`
et **il ne se compte jamais deux fois**.

Ce sont deux colonnes, jamais une. Si les deux se confondent, l'addition du
contre-PLF ne tombe pas — et c'est l'attaque la plus facile sur le seul terrain
où le corpus est imprenable, avec 32 bouclages sur 32.

*Conséquence, et elle se dit dans le texte même* : les deux gages naturels —
baisse de dépense, baisse de recette sociale — sont exactement les deux que le
cadre interdit au même texte. Chaque amendement qui a dû recycler un gage
postiche porte, en deux phrases de l'exposé sommaire, la raison pour laquelle il
l'a fait. Trente amendements, trente occurrences : le contre-PLF plaide la
fusion PLF-PLFSS sans jamais avoir à la réclamer frontalement.

### A-225 — Le rattachement se plaide par l'implicite budgétaire et le contrefactuel

**Arbitré par l'auteur.** On ne cherche pas d'abord la porte du domaine par
laquelle une mesure entrerait. On identifie **ce que la mesure produit comme
dépense ou comme recette** — souvent ignoré, et à tort — puis on interroge les
contrefactuels pour établir qu'elle est **de nature budgétaire bien que son
objet soit plus large**.

**C'est un plaidoyer. Il n'est pas garanti, et la perte de quelques articles
n'est pas grave** : elle est le prix de la position. Des pertes sont acceptées
d'avance.

*Ce qui reste à instruire, et ne se tient pas pour établi* : la recevabilité
s'apprécie contre le droit existant, et le choix de la référence — droit
constant ou évolution tendancielle — n'est pas codifié. C'est une prise, dans
les deux sens.

*La grille des portes passe au second rang.* Elle sert à savoir ce qui est
acquis sans plaidoirie, jamais à décider ce qu'on tente.

### A-226 — « Information et contrôle du Parlement » est écartée comme porte générale

**Arbitré par l'auteur, en correction expresse.** La porte du 7° du II de
l'article 34 de la loi organique n'est pas la bonne porte qu'elle paraît :
**c'est celle par laquelle on demande des rapports**, faute d'avoir réfléchi à
ce qu'on veut faire ou d'en avoir les moyens.

Elle ne sert qu'un axe, et il est précis : **la transparence absolue** —
opérateurs, associations, caisses de sécurité sociale.

*L'existence de cet axe au corpus reste à vérifier au `REF_doctrine`, qu'un fil
de conversation ne peut pas ouvrir.*

### A-227 — Le rattachement et le vecteur sont deux questions distinctes

**Arbitré par l'auteur, et c'est la correction la plus importante de la
journée.**

**Le rattachement** dit *si la mesure peut voyager en loi de finances*. C'est
une question de domaine, et **elle se plaide**.

**Le vecteur** dit *quel article de quel texte on modifie*. C'est une question
de légistique, et **elle ne se plaide pas : elle se trouve, ou elle n'existe
pas**.

Une mesure peut être parfaitement rattachable et n'avoir aucun vecteur
identifié : elle n'est alors pas rédigeable. L'inverse existe aussi.
`REF_norme` porte donc **deux colonnes distinctes**, et un contrôle qui refuse
de confondre l'une avec l'autre.

**Le vecteur est le gros du travail, et il faut le dire maintenant.** La
suppression est facile : on abroge un article nommé. L'insertion ne l'est pas —
l'expérience de la Constitution et de la LOLF l'a montré, où trouver le bon
alinéa n'a jamais été direct. Sur la matière fiscale, l'auteur dispose d'une
révision du code général des impôts préparée par un expert : c'est un input à
verser, et il couvre peut-être une grande part des vecteurs fiscaux. À
instruire avant de refaire ce travail.

### A-228 — On prioritise ce que le PLF ouvre déjà

**Arbitré par l'auteur.** Le Gouvernement n'est pas original, et il rouvre
souvent les mêmes articles. **Amender un article ouvert coûte infiniment moins
qu'un article additionnel** — en recevabilité, en vecteur, en débat.

L'ordre de traitement des écarts suit donc : **partielle et contraire sur un
article ouvert, avant absente.** Un écart « absente » n'est pas une case de la
matrice, c'est un **article additionnel**, et il coûte le plus cher.

### A-229 — Le socle du texte porte la rédaction exacte, les numéros et l'exposé des motifs rattaché

**Arbitré par l'auteur.** `referentiels/socle_plf_texte.json` porte une entrée
par article : son numéro, sa partie, son titre, **sa rédaction exacte**, sa page
dans la pièce source, et **l'exposé des motifs qui s'y rapporte**.

**L'exposé des motifs est indexé avec l'article et jamais confondu avec lui :
il est de l'indice, pas de la norme.** Il ne décrit pas les mesures, il les
raconte.

*Corollaire d'appareil, tranché par Claude au titre d'A-23* : **l'extracteur est
déterministe et son empreinte est relevée.** Même pièce, même script, même JSON,
même SHA-256. Sans cela, rien ne garantit que la fiche de l'article 12 parle du
même article 12 la semaine suivante.

### A-230 — La lecture en creux se mécanise, elle ne se délègue pas au flair

**Arbitré par l'auteur, et cette entrée est du même rang que « une restauration
est toujours une copie d'octets » (A-41).**

Les mesures d'économie, de hausse d'impôt et de hausse de dépense sont souvent,
à dessein, cachées ou mal présentées. Qu'attendrait-on qui ne figure pas ? Tel
terme plutôt qu'un autre, qu'ouvre-t-il ou qu'exclut-il ? **C'est un jugement,
et un jugement ne se délègue pas au flair d'un modèle.** Il se mécanise, par des
dispositifs qui produisent des signaux qu'ensuite on lit.

Six dispositifs, et ils existent ou se transposent.

**Le trois colonnes.** On ne lit jamais une disposition modificative seule : on
lit texte en vigueur, disposition, texte résultant. Le corpus porte déjà
`Constitution_3col` et `LOLF_3col` — la méthode est éprouvée, elle se transpose.

**Le chiffre d'abord, et pas celui de l'exposé des motifs.** Le montant de
l'article se prend à l'état, à l'annexe ou au tableau d'équilibre. **Tout écart
avec le montant annoncé à l'exposé des motifs est un signal, et il se relève, il
ne s'arbitre pas.**

**Le relevé mécanique des mots de portée** : peut, dans la limite de, à compter
de, au titre de, par dérogation, notamment. Chacun ouvre ou ferme quelque chose,
et leur liste par article se produit par script.

**Le relevé des dates** — entrée en vigueur, clause de fin, période transitoire.
Un décalage d'un an déplace un coût hors de l'année budgétaire sans rien changer
au fond : c'est le procédé le plus commun et le plus efficace.

**Le relevé des absences attendues** — un taux modifié sans que l'assiette
bouge, un plafond posé sans indexation, une suppression sans transitoire, un
dispositif sans évaluation. La liste des absences à chercher s'écrit une fois et
s'applique à tous les articles.

**Et les amendements déposés.** Des centaines de gens ont déjà lu ce texte en
creux, chacun sur son sujet, et ils ont écrit ce qu'ils y ont vu. Un article qui
attire trente amendements porte un point sensible ; l'article qui n'en attire
aucun mérite qu'on se demande pourquoi. **C'est le meilleur correcteur
disponible, et il est gratuit.**

### A-231 — Le normage juridique devient une couche du corpus

**Arbitré par l'auteur.** `REF_norme` sort du contre-PLF et devient une couche
du corpus, **au même rang que `REF_chiffres`**. Le contre-PLF n'en est qu'une
vue.

Une entrée par proposition, systématique sur les 56 : la **norme cible** — ce
que le droit doit concrètement imposer, supprimer, modifier ou autoriser —, le
**niveau requis**, le **véhicule**, le **vecteur** (article de code ou de loi
modifié, distinct du véhicule), et l'**état du vecteur** : trouvé, à trouver, ou
inexistant.

Elle **ne dépend d'aucun texte en discussion** et peut se construire en
parallèle. Le format est déjà éprouvé :
`sources/Recap_transposabilite_20260731_v6.md` a fait ce travail pour la
Constitution, innovations ventilées par strate et replis portant chacun leur
écart. Il se généralise.

*Premier acte du fil* : instruire la révision du code général des impôts
préparée par l'expert, et mesurer ce qu'elle couvre déjà en vecteurs fiscaux. On
ne refait pas ce qui existe.

### A-232 — Le pack public part en deux temps

**Arbitré par l'auteur.** Le pack public — la méthode ouverte à des tiers —
**part avant tout amendement**. Il ne dépend d'aucun texte, d'aucun dépôt,
d'aucune stratégie parlementaire.

**Temps 1, maintenant** : les grilles et les gabarits. Recevabilité, portes,
test de rattachement, qualification d'un article, dispositif de lecture en
creux, grille des cinq écarts, gabarit d'exposé sommaire, lecteur des trois
annexes budgétaires publiées, et une liste d'adresses de téléchargement. La base
documentaire est optionnelle et elle n'est pas dans le zip.

**Temps 2, réservé** : un objet « PLF relu, trié, expliqué », dont l'arbitrage
se posera quand il existera.

**Ce qui n'y entre jamais**, en application d'A-134 : le manuscrit, le
`REF_doctrine`, les positions, les apports, le registre, la stratégie réseaux,
les deux classeurs de l'auteur, la révision du code général des impôts, et **la
colonne « traitement » des 128 programmes** — un référentiel qui range les
programmes en régalien, transférable et supprimable est la doctrine sous forme
de tableau. **Le pack exporte les questions, pas nos réponses.**

### A-233 — Le dry run sur le PLF 2026 reste interne, et le pack part quand même

**Arbitré par l'auteur.** L'exercice à blanc sur le PLF 2026 — qualification,
appariement, écarts, rédaction — **reste interne**. Le pack public, lui, **part
dès maintenant**, sans attendre qu'il ait tourné.

*Cela amende la règle de temps d'A-134 sur un point et un seul* : « rien ne
traverse avant d'être déposé ou publié » vaut pour la matière — le recensement
des mesures candidates, l'ordre de dépôt, les positions. **La méthode fait
exception : elle part maintenant.** Ce que le pack expose est ce que n'importe
qui peut refaire ; ce qu'il tait est ce que nous avons trouvé.

*Fait neuf porté à l'auteur, et il ne se déduit d'aucune donnée* : si le pack
public fonctionne, des tiers déposeront des amendements qui recoupent les
nôtres. Qui dépose quoi en premier, et si deux amendements voisins divisent un
vote, cela lui revient.

### A-234 — Le verbatim n'entre que par pièce jointe

**Arbitré par l'auteur, et c'est la règle qui commande tout l'appareil du
contre-PLF.**

**L'outil de récupération web fait passer le texte par un modèle. Il ne rend
jamais du verbatim.** Il sert au repérage, à la structure, aux adresses. Jamais
à la copie. C'est la même règle qu'A-41 pour la restauration, appliquée à
l'entrée plutôt qu'à la sortie.

**La passerelle de sortie de l'atelier n'admet que les registres de paquets**
(A-196) : aucun texte ne se télécharge depuis un fil de production.

**Donc le verbatim entre par pièce jointe du fil, déposée par l'auteur.** Les
pièces jointes de conversation ne comptent pas dans la jauge du coffre — c'est
ce qui rend la chose possible.

### A-235 — Ni le PLF ni le PLFSS ne vont au coffre

**Arbitré par l'auteur.** Ce sont des documents publics, retéléchargeables à
l'identique : **A-71 s'y applique en plus fort qu'à un dérivé.** Un PDF de
4 251 Ko ne rentrerait de toute façon pas dans une jauge à 1 750 682 sur
2 000 000.

**Ce qui se verse est ce que personne ne sait refaire** : les fiches de
qualification, et le texte des amendements.

*Les deux textes se retrouvent par leur adresse, portée à
`methode/procedure_contre_plf.md`* : PLF 2026 n° 1906 et PLFSS 2026 n° 1907,
déposés le 14 octobre 2025, avec pour chacun sa page, son PDF, son HTML
structuré et son point d'accès aux amendements déposés.

## 20260828 — La langue et l'air du manifeste

### A-221 — « Le remède », et la majuscule seulement où le français l'attend

**Arbitré par l'auteur.** Trois corrections de langue au manifeste.

**« La chute » devient « Le remède ».** C'était un terme de chantier, tiré du
découpage en mouvements du proto — titre, constat, solution, priorité,
propositions, chute. Le lecteur n'a pas à connaître le gabarit. « La solution »
étant déjà pris par le mouvement précédent, le dernier s'appelle *Le remède*.

**« la loi française »** et **« nos voisins européens »**, en minuscules. Règle
énoncée par l'auteur, et elle vaut pour tout livrable : *on ne met de majuscule
que là où le français l'attend.* Ni un nom commun, ni un adjectif de
nationalité n'en portent.

*Relevé et non corrigé, faute de consigne* : le proto écrit « l'Etat » sans
accent en cinq endroits, et « l'État » ailleurs. C'est une inconstance d'accent,
non de majuscule — elle attend un mot de l'auteur.

### A-222 — Le texte suivi se lit, il ne s'affiche pas

**Arbitré par l'auteur** : « c'est un tout petit peu gros pour être lisible,
aérer un peu et alléger du gras. »

Le manifeste avait été composé avec les réflexes d'une affiche : corps à
1,1 rem, graisse 800, condensé à 88, interlignes serrés. Sur cinq mille signes de
texte suivi, cela fatigue.

Corps ramené à 1 rem pour l'affirmation et 0,97 rem pour l'appui, graisse à 700,
largeur détendue à 94, interlignes à 1,6 et 1,66, l'espace entre blocs et entre
mesures augmenté de moitié, le filet des mesures affiné, les intertitres
allégés. **Le gras ne reste que sur l'affirmation**, qui est ce qui doit ressortir.

*Règle qui en sort* : **la charte de la couverture donne la palette et la
typographie, pas les corps ni les graisses.** Une affiche et une page de lecture
n'ont pas la même échelle, même quand elles parlent la même langue visuelle.

## 20260828 — Le gris, trouvé pour de bon

### A-220 — On borne une feuille, on ne surenchérit pas en spécificité

**Relevé deux fois par l'auteur, et la première correction était mauvaise.**
A-215 avait monté d'un cran la spécificité des règles du manifeste. Il restait
un cas : `.m-corps li.mesure .appui`, trois classes, écrit après — les appuis des
dix mesures sortaient en gris #6d6a64 sur brique. Courir après la spécificité
règle par règle **rate toujours un cas**, et le rate en silence.

La feuille de la fiche est donc **bornée en un point** : ses règles de contenu
s'écrivent `.m-page:not(.g-page) .m-corps …`. Le manifeste ne peut plus les
recevoir, quelle que soit la règle et quel que soit l'ordre.

*Règle générale* : quand deux chartes partagent des classes, **on exclut l'une à
la source plutôt que de renforcer l'autre partout.** Une exclusion se vérifie
d'un coup d'œil ; une surenchère se vérifie règle par règle, donc pas du tout.

**Contrôlé mécaniquement, non à l'œil** : la couleur calculée de **tous** les
descendants de la vue du manifeste est relevée dans le navigateur et confrontée à
la palette — crème, or, brique. Zéro élément hors palette. Et la fiche est
vérifiée inchangée dans le même passage.

*Ce que les deux passes coûtent, et il faut le dire* : deux allers-retours pour
un défaut que le contrôle mécanique aurait trouvé du premier coup. « Un contrôle
annoncé est un contrôle mécanique » valait déjà pour les chiffres ; il vaut aussi
pour la couleur.

## 20260828 — La précommande se distingue

### A-219 — La précommande est en or plein et se nomme, et A-212 se lit mieux

**Arbitré par l'auteur.** L'appel de précommande porte **« Précommander le
livre »** et se compose en **or plein** — le seul des trois appels sur fond, avec
l'adhésion en crème. C'est l'appel qui vend le livre, et il se distingue.

*Ce qui se corrige dans la lecture d'A-212.* Le reproche portait sur le fait
d'avoir changé ce bouton **sans consigne**, non sur le résultat. J'en ai déduit
qu'il fallait tout remettre à la page de garde, et j'ai défait ce que l'auteur
gardait. Deux passes perdues au lieu d'une.

**A-212 tient, et se précise** : ne rien changer sans consigne — *et, devant un
reproche, ne pas défier plus que ce qu'il nomme.* Un reproche sur la manière ne
dit pas que le résultat était mauvais. C'est exactement A-175 — « une consigne de
correction porte sur ce qu'elle nomme » —, appliqué cette fois à un reproche
plutôt qu'à une consigne.

Les trois appels, arrêtés : *J'adhère au manifeste* en crème plein, *Je
m'exprime* en or filaire, *Précommander le livre* en or plein.

## 20260828 — Le gris illisible, le courriel qui n'ouvrait rien

### A-215 — Une collision de cascade rendait le manifeste illisible

**Relevé par l'auteur** : « le gris du manifeste est illisible. » Ce n'était pas
un choix de couleur, c'était un défaut de construction, et il se mesure.

Le manifeste et la fiche partagent les mêmes classes de contenu — `.appui`,
`.affirmation` — parce que le texte vient du proto. Les règles de la fiche
(`.m-corps .appui`, gris ardoise sur papier crème) et celles du manifeste
(`.g-page .appui`, crème sur brique) avaient **la même spécificité**, et celles
de la fiche étaient écrites après : elles gagnaient. Le manifeste sortait donc en
gris #6d6a64 sur fond brique — deux pour un de contraste.

Corrigé en montant d'un cran la spécificité du bloc du manifeste, non en
déplaçant un bloc de feuille : un ordre d'écriture qui décide d'une couleur est
un piège qui se retend au prochain ajout. Vérifié à la couleur calculée dans le
navigateur, non à l'œil : `rgb(255, 253, 242)`.

*Ce que la faute enseigne* : **quand deux couches partagent des classes, la
seconde se distingue par la spécificité et pas par l'ordre.** Et un contrôle de
lisibilité se fait sur la couleur calculée.

*Et toute transparence disparaît du manifeste* : sur un fond strié, un texte à
94 % d'opacité laissait encore un voile. L'appui se distingue de l'affirmation
par le poids.

### A-216 — Un bouton « mailto » ne s'ouvre pas depuis une page publiée

**Relevé par l'auteur** : « je m'exprime n'ouvre pas de mail. » C'est exact, et
c'est structurel : le lecteur d'une page publiée l'isole dans un cadre qui
**bloque la navigation `mailto:`**. Le bouton ne faisait rien, et rien ne le
disait.

**L'adresse est donc toujours écrite en clair**, en gros, sélectionnable, avec un
bouton qui la copie dans le presse-papier — et le lien de courriel ne vient
qu'en second, pour les contextes où il fonctionne. Si le presse-papier est lui
aussi refusé, le bouton sélectionne l'adresse et le dit.

*Règle qui en sort* : **un appel à l'action ne dépend jamais d'un mécanisme que
le lecteur peut refuser.** Ce qui doit passer se lit à l'écran ; l'automatisme
est un confort par-dessus.

« Je m'exprime » prend donc sa page — l'adresse, le partage, le détail — au lieu
d'un lien qui ne s'ouvrait pas.

### A-217 — L'adhésion : le geste d'abord, le détail à la fin, dix réseaux

**Arbitré par l'auteur** : « il faut mettre les détails à la fin, et en deuxième
étape mettre plus d'options de réseaux sociaux. »

L'ordre de la page devient : adhérer, faire connaître, puis la mention de
traitement. Le pavé juridique s'intercalait entre les deux étapes et coupait le
geste en deux.

Dix destinations de partage au lieu de trois : Facebook, X, LinkedIn, Bluesky,
WhatsApp, Telegram, Reddit, Threads, Mastodon, et le courriel. Aucune adresse
n'est écrite en dur — la page se lit au clic, donc les mêmes boutons servent
quel que soit l'hébergement.

### A-218 — Les produits finaux du site se déclarent à l'output

**Demandé par l'auteur** : « les produits du site finaux devront bien être dans
output au bon format. »

`site/manifeste.html` devient un artefact déclaré, famille **rédactionnel** — le
critère d'A-12 tranche : son texte se lit sans sa mise en forme.
`site/index.html` reste en **graphique** : sa mise en forme porte le sens.

Le reste du dossier `site/` demeure le rendu d'un artefact et ne se déclare pas
pièce par pièce ; `controle_index.py` admet désormais **deux** chemins déclarés
sous un dossier rendu en bloc.

## 20260828 — Le manifeste est le produit phare

### A-210 — « Jusqu'à sept ans », et A-140 est tranché

**Arbitré par l'auteur**, et cela ferme A-140 : la durée du plan de départ se dit
**« jusqu'à sept ans »**. Motif donné : un contrat à durée déterminée ne conserve
pas le bénéfice au-delà de son terme. Sept ans est un plafond, non une durée
acquise.

**La règle vaut partout, et pas seulement sur ce cas.** Une promesse se dit à la
borne quand la borne est une condition d'ouverture, non au plafond.

Appliqué aux quatre `relais` du côté perte de `justifications.py`, qui portaient
« je gagne sept ans à 70 % de mon traitement », et à la correction du manifeste.
Les apports le disaient déjà.

*Ferme A-140*, ouvert depuis le 20260828 au matin.

### A-211 — Trois chiffres du manifeste, arbitrés par l'auteur

- **303 agences nationales** contre 1 104 aujourd'hui. La cible est citable, et
  le proto la laissait à « xxx ».
- **20 000 € par foyer**, et non 9 000 € par habitant. C'est l'agrégat retenu,
  celui que porte tout le reste du corpus. Le second sort.
- **438 impôts**, et non 483. Le manuscrit porte 438 ; les 483 du proto sont une
  valeur périmée.

*Ne reste non corrigé* que « 486 niches fiscales », qu'aucune pièce ne contredit.

### A-212 — Une modification qui ne vient pas d'une consigne est une faute

**Reproche de l'auteur, et il est juste.** J'avais changé de mon propre chef
l'intitulé et la couleur d'un appel de la page de garde : « Le livre » devenu
« Précommander le livre », et le filet d'or devenu un aplat d'or. La consigne
était d'y mettre un lien, pas de refaire le bouton.

**Règle de conduite, et elle s'ajoute aux quatre garde-fous** : *ne jamais faire
un changement qui ne découle pas, directement ou indirectement, d'une consigne.*
Une modification non demandée n'a pas été pesée par celui qui décide, et c'est
par là qu'on se trompe. Elle coûte deux fois : une passe pour la faire, une pour
la défaire.

Rétabli : les trois intitulés de la page de garde, et leurs couleurs — crème
plein pour le premier appel, or filaire pour les deux autres. Seules les
adresses ont été ajoutées, et les marques *bientôt* tombent puisque les trois
appels mènent désormais quelque part.

*Cette entrée prolonge A-175* — « réviser n'est pas réécrire », « une consigne de
correction porte sur ce qu'elle nomme » — et l'étend à toute production, non aux
seules corrections.

### A-213 — Le manifeste est le produit phare, et il porte la charte du livre

**Arbitré par l'auteur** : « c'est par ici pointe évidemment vers le manifeste,
qui est le produit phare, les fiches sont un add-in ».

L'appel principal de la page de garde mène donc **au manifeste**, non au
sommaire des fiches. La galerie reste accessible par la rubrique *Propositions*
et par le manifeste.

**Et le manifeste passe à la charte du livre** : fond brique strié, Archivo
condensé, or et crème — la langue de la couverture, non celle de la fiche. La
fiche garde Fraunces sur papier crème : elle démontre, le manifeste annonce.

*Deux décisions de détail, tranchées par Claude au titre d'A-23.* **L'or sur le
brique ne dépasse pas trois pour un de contraste** : il tient pour un filet ou
une vedette, pas pour du texte suivi — les intertitres passent en crème et l'or
reste au filet qui les souligne. **Et à l'impression le fond brique disparaît**,
au profit du noir sur blanc : l'encre coûte, et la signature tient par le filet
et par la typographie.

*Le téléchargement se nomme* : « Télécharger en PDF » ouvre l'impression, qui
enregistre en PDF sur tous les navigateurs. Sur le site déployé, un second
bouton télécharge la page elle-même. **Sur la page publiée chez Claude, le
téléchargement de fichier est bloqué par le lecteur** : seul le PDF par
impression fonctionne, et c'est pour cela qu'il est le bouton nommé.

### A-214 — Aucune page du site n'est un cul-de-sac

**Relevé par l'auteur** : « le sommaire ne permet toujours pas de retourner en
arrière. »

La barre de retour, écrite pour les fiches en A-209, coiffe désormais **toutes
les pages intérieures** — sommaire, manifeste, adhésion. À gauche la marque vers
l'accueil ; à droite la destination utile de la page : le manifeste depuis le
sommaire, les dix-huit fiches depuis une fiche.

## 20260828 — Le manifeste, l'adhésion, et le retour à l'accueil

### A-206 — Le manifeste est le proto remis à jour, et les corrections se déclarent

**Demandé par l'auteur** : « mets à jour le proto manifeste en corrigeant juste
ce qui doit l'être pour être à jour sans le refaire. »

Le texte reste celui de `sources/1pager_20260806_v1_proto.html`, arrêté le
20260806. `appareil/manifeste.py` ne porte que **la liste des corrections**,
chacune avec son arbitrage et son motif — même dispositif qu'`apports.py` et
`justifications.py` : ce qui est écrit à la main vit là, le produit se régénère.

**Cinq corrections, et pas une de plus.**

| corrigé | vers | au titre de |
|---|---|---|
| « salaire médian … 2 100 €, contre 5 500 € en Suisse » | « revenu médian … 2 100 €, contre 4 300 € » | A-84, A-85 |
| « salaire net de 2100 € » | « salaire net de 2 190 € » | A-85 |
| « +14 % de salaire net » | « +13 % » | référentiel des positions |
| « 540 000 emplois publics arrêtés » | « 580 000 » | A-155 |
| « xxx agences nationales (contre 1400) » | « un nombre réduit d'agences nationales — contre 1 104 » | A-130 |

**Ce qui n'est pas corrigé se déclare aussi**, dans le même module : les sept ans
d'indemnisation, parce qu'A-140 n'est pas tranché ; les 9 000 € par habitant,
parce qu'ils ne contredisent pas les 20 000 € par foyer — deux mailles ; et les
483 impôts et 486 niches, parce que rien ne prouve qu'ils soient faux. **Une
absence de correction est une décision, elle s'écrit.**

**Deux garde-fous mécaniques.** Une correction dont le texte cherché n'est pas
trouvé **arrête la génération** — un remplacement qui ne s'applique pas
laisserait sortir la vieille valeur en silence. Et **aucune correction n'invente
un chiffre** : là où le proto portait « xxx », la phrase se réécrit pour ne dire
que ce qui est sourcé, et la cible reste ouverte.

*Deux retraits de forme, non des corrections de fond* : l'en-tête de chantier du
proto — statut, format relevé, mentions non arrêtées — sort, A-154 l'interdit sur
une page qui s'affiche ; et le titre, laissé à « [TITRE ?] », prend celui du
livre, arrêté depuis.

*L'archive n'est pas touchée* (A-15) : le proto reste au coffre tel quel, le
manifeste est un artefact nouveau qui s'en dérive.

### A-207 — L'adhésion se recueille par courriel, et le site ne collecte rien

**Arbitré par l'auteur** : « j'adhère au manifeste, c'est juste le recueil de
l'adresse mail (avec les infos recueillies dans les conditions RGPD) plus une
proposition de diffusion sur les réseaux. »

Le site est statique et ne porte ni base, ni formulaire, ni collecte — cela ne
change pas. **L'adhésion passe donc par un courriel prérempli** vers
`contact@france-resolution.fr` : l'adresse arrive dans la boîte du mouvement,
sans traitement intermédiaire, sans que la page enregistre quoi que ce soit.

*Pourquoi pas un formulaire* : il faudrait un service qui reçoive, donc un point
de collecte à administrer, à sécuriser et à déclarer. Le courriel fait le même
travail et la page peut dire, sans mentir, qu'elle n'enregistre rien.

La page d'adhésion porte la mention de traitement — données recueillies,
finalité, durée, droits et adresse d'exercice — puis le partage vers Facebook, X
et LinkedIn. **Les liens de partage ne sont pas écrits en dur** : l'adresse de la
page se lit au clic, de sorte que le même fichier fonctionne quel que soit
l'hébergement.

*Ce texte est de l'output* : il se lit et se valide comme le reste.

### A-208 — « Je m'exprime » porte l'adresse de contact

**Fourni par l'auteur** : `contact@france-resolution.fr`, en attendant mieux.
L'appel cesse d'être marqué *bientôt* et ouvre un courriel. Deux des trois appels
de la garde mènent donc désormais quelque part.

### A-209 — Une fiche revient à l'accueil, et pas seulement au sommaire

**Relevé par l'auteur** : « il faut que les fiches puissent rediriger vers la
page d'accueil, là ça fait un peu cheap. »

Une fiche portait un seul retour, vers le sommaire, et la marque en pied. Elle
porte maintenant **une barre de retour au-dessus de la carte** — la marque à
gauche vers l'accueil, le sommaire à droite —, la navigation précédente et
suivante, et un pied qui mène à l'accueil et à l'adhésion.

*Tambouille, inscrite au titre d'A-23* : le défaut n'était pas la navigation
entre fiches, qui existait, mais l'absence de sortie vers le haut. Une page
d'où l'on ne peut que continuer latéralement se lit comme un cul-de-sac.

## 20260828 — La voie GitHub est fermée par l'organisation

### A-205 — Le déploiement par dépôt Git est indisponible, et ne se réessaie pas

Constaté sur l'écran de l'auteur : *« L'accès à GitHub est requis pour Claude
Code sur le web. Veuillez contacter un propriétaire de l'organisation. »*
L'organisation n'a pas activé les sessions cloud adossées à GitHub. Le sélecteur
de dépôt n'est donc pas accessible, et le lien pré-rempli non plus.

**Conséquence, et elle est nette** : la seconde voie d'A-190 — dépôt Git relié à
Vercel — est **indisponible**, non pas mal configurée. Elle ne se réessaie pas
et ne se contourne pas depuis l'atelier : ni la passerelle (A-196), ni un jeton
fourni (A-196), ni le sélecteur de dépôt. Elle rouvrira si un propriétaire de
l'organisation active l'accès, et pas autrement.

**Ce qui reste, et c'est tout.**

- **La page publiée sur claude.ai** (A-199) : en ligne, à jour, une adresse par
  fiche en fragment. C'est le site utilisable aujourd'hui.
- **Le dossier `site/` livré à l'auteur**, qu'il déploie d'une commande depuis sa
  machine pour obtenir un vrai `vercel.app`. Aucun jeton n'y transite par nous.

`make publier` et le `vercel.json` restent écrits et éprouvés : ils servent le
jour où le dépôt devient accessible. Rien n'est à refaire, seulement à rejouer.

*Ce que la séquence enseigne, et il faut l'écrire* : **on vérifie qu'une voie de
déploiement est ouverte avant d'en faire le plan.** Quatre échanges ont porté sur
des réglages d'une voie que l'organisation avait fermée d'avance — d'abord un
jeton inutilisable, puis un champ inéditable, puis un sélecteur inaccessible.
L'ordre juste est : établir ce qui est atteignable, puis construire dessus.

## 20260828 — La précommande, et un « reste » qui ne désignait rien

### A-203 — « Le reste » ne désigne rien : c'est le salaire net qui revient

**Relevé par l'auteur, et c'est une faute de langue qui cachait une faute de
sens.** L'axe de `C-32` disait « Votre salaire monte, et **le reste** vous
revient en argent libre ». Aucun reste n'est défini : le lecteur n'a rien à quoi
soustraire. Et ce qui revient, c'est **le salaire net**.

L'axe devient : **« Votre salaire net monte, et votre aide devient de l'argent
libre. »** Deux faits nommés, aucun résidu implicite.

*Portée générale, et c'est ce qui vaut d'être retenu* : **un mot de quantité
relative — le reste, le solde, la différence — n'entre dans un livrable que si
les deux termes de la soustraction y sont écrits.** Sinon il a l'air d'un chiffre
et n'en est pas. C'est le pendant, du côté de la langue, de « une contrepartie
plausible est plus dangereuse qu'une contrepartie absente » (A-163).

### A-204 — La précommande existe : « Le livre » cesse d'être un appel mort

**Fourni par l'auteur.** L'appel « Le livre » de la page de garde ne menait
nulle part et portait la marque *bientôt*. Il devient **« Précommander le
livre »**, en or plein, vers la fiche du livre chez le libraire en ligne, avec la
date de parution en dessous.

C'est le premier appel de la garde qui mène quelque part, et il lève d'autant
A-59 : le site ne promet plus, sur ce point, il livre. Les deux autres appels —
adhésion au manifeste, prise de parole — restent marqués tant qu'ils n'existent
pas.

*L'adresse vit dans `generer_site.py`*, une constante nommée. Un lien de
diffusion est de l'output : s'il change, il se corrige là et le site se
régénère.

## 20260828 — La page de garde, et deux corrections de fond

### A-200 — Le site s'ouvre sur la page de garde, et A-192 se trompait sur le prototype

**Reproche de l'auteur, et il est fondé.** Le site qu'il attendait est **la
projection de la page de garde** — `sources/ResolutionD1a.png` — avec son
graphisme et le contenu à venir. Ce qui a été livré était un sommaire nu.

*Amende A-192 sur un point, et pas des moindres.* J'y ai écarté l'ancien
`generer_site.py` en reprochant à Archivo et à la palette brique d'être « une
autre typographie que l'esthétique arrêtée ». **C'était faux** : Archivo, le
fond brique, l'or et la crème sont l'esthétique de la page de garde, et le
prototype en était la projection. J'ai qualifié une pièce sans regarder ce
qu'elle projetait — garde-fou A-24 violé.

*Ce qui reste vrai d'A-192*, et qui justifie encore le remplacement : le
prototype intégrait `interface_positions.html`, dérivé de travail jamais validé,
au lieu de la galerie arrêtée ; et il sortait une page unique quand A-190 demande
un dossier. Le motif typographique, lui, tombe.

**Deux langues typographiques, et elles ne se mélangent pas.** La garde annonce —
Archivo condensé très gras, fond brique strié, titre en deux couleurs. La fiche
démontre — Fraunces et JetBrains Mono sur papier crème. Le passage de l'une à
l'autre est le passage de l'affiche à la preuve.

**Tout ce que la garde affiche vient de la page de garde** : les trois auteurs,
la marque, le titre, la promesse des 600 €, les trois appels, les rubriques, la
date de parution. Rien n'y est inventé. Ce qui n'existe pas encore — le
manifeste, les vidéos, les trois appels — **est marqué « bientôt » ou « à
venir »** plutôt que promis en silence (A-59). Le seul lien qui mène quelque part
est celui des propositions.

*Limite de vérification, et elle se dit* : la passerelle de l'atelier bloque
`fonts.googleapis.com`. Le rendu contrôlé ici tombe donc en police de secours, et
le condensé d'Archivo ne se voit qu'à la page publiée. Une pile de secours
condensée est déclarée pour que la garde ne s'affiche jamais en large.

### A-201 — Le bénéficiaire d'un chèque gagne d'abord du salaire

**Arbitré par l'auteur** : « bénéficiaire d'un chèque ciblé ne va pas avec aide
unique, ça va avec hausse de salaire ».

`C-32` ouvrait sur les 550 € d'argent libre, et son axe disait « une aide unique,
à vous, remplace les chèques ». C'était présenter un remplacement d'aide là où le
gain premier est le revenu. Les 220 € de plus au salaire type — `D2-4-1-e1`,
déjà attaché à cette catégorie — passent en tête, et l'axe devient **« Votre
salaire monte, et le reste vous revient en argent libre. »**

*Aucune attache n'a bougé* : le gain était déjà celui de `C-32`, seul l'ordre
change. A-178 est intact.

### A-202 — Le jeune adulte est un âge de la vie

**Arbitré par l'auteur** : « jeune adulte c'est dans la catégorie âge de la vie
par définition ». `C-16` quitte « Le travail et l'entreprise » pour « La famille
et les âges de la vie », et s'y range entre l'enfance et la parentalité —
l'ordre du groupe suit les âges.

Conséquence sur la lecture : l'ordre des fiches change, la navigation du site
aussi, et les voisines de fiche du jeune adulte ne sont plus le travailleur et la
personne sans emploi mais l'enfant et la famille.

## 20260828 — Le site est en ligne, sans Vercel

### A-199 — Le site se rend aussi en une page, et cette page est publiable d'ici

Tranché par Claude au titre d'A-23, sur reproche fondé de l'auteur : trois
échanges à lui faire cliquer dans des interfaces, sans qu'une page soit en
ligne.

Une page hébergée sur claude.ai se publie **depuis l'atelier**, sans réseau
sortant vers un tiers. Elle prend un fichier HTML autonome. `generer_site.py`
sort donc, en plus de `site/`, **`site/resolution_une_page.html`** : la même
matière, la même structure, le même rendu, en un fichier.

**Une fiche y garde une adresse** : un fragment, `…#retraite`. La page n'affiche
qu'une vue à la fois — ce n'est pas le mur qu'A-195 a écarté —, et un lien vers
une fiche reste un lien vers cette fiche, citable et envoyable. C'est le bénéfice
qui commandait le choix de structure, tenu par un autre moyen.

**Sans JavaScript, tout s'affiche à la suite.** La matière ne disparaît jamais :
le script restreint l'affichage, il ne le conditionne pas.

**Ce n'est pas un remplacement.** `site/` reste la forme cible, avec ses vraies
adresses et son domaine ; la page unique la double, et sert dès maintenant. Les
deux sortent du même générateur, donc elles ne peuvent pas diverger. Une
correction se porte au référentiel, `make`, et les deux se refont.

*Ce que la faute enseigne, et c'est la vraie leçon* : **une consigne qui demande
un geste à l'auteur n'est un livrable que si aucune autre voie n'existe.** Trois
tours ont été perdus à décrire des clics — d'abord dans le mauvais ordre (A-198)
— quand un moyen de publier était disponible sans lui depuis le début. Chercher
ce qu'on peut faire soi-même passe avant expliquer ce que l'autre doit faire.

Adresse de la page : `https://claude.ai/code/artifact/04a7d513-7de5-472c-937e-5b0307a2637d`.
Elle est privée jusqu'à ce que l'auteur la partage.

## 20260828 — La chaîne de publication

### A-198 — Le dépôt porte sa configuration, parce que le champ de Vercel est verrouillé

Constaté sur l'écran de l'auteur, corrigé à l'appareil. Le réglage *Root
Directory* de Vercel ne s'édite qu'en **choisissant un dossier qui existe déjà
au dépôt** : sur un dépôt où le site n'a pas encore été poussé, le champ reste
verrouillé sur la racine. La consigne donnée à l'auteur — « saisis `site` » —
était donc inexécutable, et dans le mauvais ordre.

`generer_site.py` écrit un modèle de `vercel.json`, que `make publier` pose à la
racine du dépôt de publication : `outputDirectory` désigne le sous-dossier,
`framework: null` et `installCommand` vide interdisent toute détection de projet
et toute construction. **Le dépôt dit lui-même où sont les pages, et l'auteur
n'a aucun champ à remplir.**

*Règle qui en sort, et elle vaut au-delà de Vercel* : **une consigne qui demande
un geste dans une interface qu'on ne voit pas n'est pas une consigne, c'est une
supposition.** Quand un réglage peut vivre dans un fichier du dépôt, il y vit.
Un fichier se vérifie ; un clic se raconte.

*Écarté* : faire pousser le site à la racine du dépôt, qui écraserait le contenu
existant ; et une branche de publication séparée, qui aurait déplacé le réglage
dans un autre champ de la même interface.

Éprouvé de bout en bout contre un dépôt distant factice portant déjà du
contenu : `README.md` et `appareil/deja.py` intacts, `site/` et `vercel.json`
ajoutés, poussée réussie.

### A-197 — Le dépôt de publication ne reçoit que les pages rendues

Tranché par Claude au titre d'A-23, en application directe d'A-134. Le
déploiement passe par un dépôt Git relié à Vercel (A-190, seconde voie), seule
voie possible depuis l'atelier (A-196). Ce dépôt **n'est pas une copie du
corpus** : il reçoit `site/` et rien d'autre — les pages rendues, la feuille de
style, la page d'erreur.

Ne traversent donc jamais : le référentiel des positions, le `REF_doctrine`, les
apports, les justifications, la structure de la série, l'appareil, la méthode, le
registre, le journal. Un second dépôt portant tout cela serait un second point
de vérité, ce qu'A-133 interdit et qu'A-134 a déjà tranché pour le contre-PLF.

**Rien n'en revient.** Une correction ne se fait jamais dans le dépôt de
publication : elle se porte au référentiel, `make publier` régénère et pousse.

*Conséquence d'appareil, écrite* : `make publier` régénère le site, remplace le
contenu du dépôt de publication, commet et pousse. Vercel n'a **aucune commande
de construction** à exécuter — un dépôt de fichiers statiques à la racine se
déploie tel quel. Le moins de pièces mobiles possible : chaque réglage est un
point de rupture.

*Écarté* : faire construire le site par Vercel depuis le corpus, ce qui aurait
exigé de pousser l'appareil et le référentiel, et de dépendre d'un interpréteur
Python dans leur image de construction.

---

## 20260828 — Le squelette du site, et le mur du déploiement

### A-195 — Le squelette est l'index et les dix-huit — arbitré par l'auteur

**Tranché par l'auteur** entre les deux structures portées en A-193 : vingt
fichiers. `site/index.html` porte l'entrée et liste les dix-huit fiches par
groupe, chacune avec son axe ; `site/fiches/<slug>.html` porte une fiche à son
adresse ; plus `site/fiche.css` et `site/404.html`.

**Ce que la structure achète** : chaque fiche s'envoie et se cite. C'est ce que
A-48 commande, le journaliste étant en cible première.

**Ce qu'elle coûte, et c'est assumé** : on ne lit plus la série d'un trait. Un
mur récapitulatif n'est pas émis — il donnerait deux représentations du même
ordre de lecture, donc deux points de vérité sur cet ordre.

*Trois décisions de détail, tranchées par Claude au titre d'A-23.*

**L'adresse d'une fiche se dérive de son titre arbitré**, jamais d'une table
écrite à la main : une table serait un second endroit où le nom d'une fiche vit,
donc un endroit d'où il peut diverger. Le générateur refuse en échec deux fiches
qui partageraient une adresse. *Conséquence tenue* : renommer ou fondre une
fiche change son adresse, et une adresse déjà partagée casse. Cinq fusions ont
eu lieu en A-182 ; le prochain renommage se paie en liens morts.

**Les liens portent leur `.html`**, et le site n'a pas de `vercel.json`. Les
adresses propres auraient demandé une configuration et auraient cassé la lecture
depuis le disque. Un fichier de configuration en moins est un point de rupture
en moins.

**Le rendu d'une fiche n'est pas redessiné** : `generer_site.py` importe
`matiere()` et `fiche()` de `generer_fiches.py`. La fiche a une seule source,
comme la série n'en a qu'une.

**L'entrée ne porte aucun chiffre.** Hiérarchiser les montants en tête de site
est un arbitrage d'édition et il appartient à l'auteur (A-179). Les dix-huit
axes sont la promesse, et ils sont écrits. Une seule ligne de copie neuve dans
tout le site — la règle de lecture — et elle reste à valider.

Sortie vérifiée : 21 fichiers, 68 719 o, 18 fiches à leur adresse, **zéro fuite
de nomenclature interne**, esthétique arrêtée tenue au rendu.

### A-196 — Vercel est injoignable depuis l'atelier : la mise en ligne ne s'y fait pas

Constaté, non contournable. L'atelier sort par un proxy à liste blanche qui
n'admet que les registres de paquets — `registry.npmjs.org` et `pypi.org`
répondent, `api.vercel.com` et `vercel.com` ne répondent pas du tout. Le CLI
Vercel s'installe (59.9.1) et échoue au premier appel réseau.

**Ce n'est pas une panne et cela ne se réessaie pas.** La voie du jeton de A-190
suppose que la session qui déploie atteigne Vercel ; celle-ci ne l'atteint pas.

Deux voies restent, et chacune demande un geste de l'auteur.

- **Il déploie lui-même** : le dossier `site/` lui est livré, une commande dans
  ce dossier. Immédiat, et le jeton ne quitte jamais sa machine.
- **Le dépôt Git**, seconde voie de A-190, qui devient la voie durable :
  `github.com` est joignable en git depuis l'atelier. Un dépôt distant que
  l'auteur crée, relié une fois au projet Vercel, et chaque `make` suivi d'une
  poussée redéploie. C'est le remote que l'atelier n'avait pas.

*Conséquence sur le jeton* : celui qui a été transmis a circulé dans une
conversation. Il se révoque et se remplace, quelle que soit la voie retenue. Il
n'a été écrit nulle part : ni au dépôt, ni au coffre, ni au journal, ni dans un
commit.

---

## 20260828 — L'ouverture du fil du site

### A-191 — La galerie est au coffre, et l'index le disait faux

Constaté à l'ouverture, corrigé à la source. `livrables/galerie_fiches.html` est
versée au coffre — l'auteur l'ouvre, il l'a arbitrée fiche par fiche — et
`appareil/generer_index.py` la déclarait `coffre: false`. `restaurer.py` la
sortait donc « hors index » et refusait de l'écrire, alors que le fil courant la
demande nommément.

Le champ passe à `true` au générateur, et non à l'index, qui est un dérivé
(A-25). Conséquence à la clôture : la galerie entre au relevé d'empreintes et
devient contrôlable mécaniquement comme le reste.

*Elle n'était pas pour autant sans preuve.* Une pièce qui porte du verbatim se
prouve de l'extérieur : `generer_fiches.py` rejoué sur `positions.json` et le
`REF_doctrine` redonne la galerie **identique à l'octet** — 35 546 o,
`d89d5c869511fab6`, 18 fiches. C'est la preuve qui vaut, et elle est plus forte
qu'une empreinte, puisqu'elle refait la pièce au lieu de la comparer.

*Tambouille, inscrite au titre d'A-23.*

### A-192 — `generer_site.py` est remplacé, non repris

Tranché par Claude au titre d'A-23, sur mandat exprès de l'auteur — « regarde
s'il se reprend ou s'il se remplace, tranche, et inscris-le ». Quatre raisons,
et chacune suffirait.

**Il intègre la mauvaise pièce amont.** Il découpe
`livrables/interface_positions.html` — un dérivé de famille *bac à sable*,
« travail interne » à l'index — et en reprend le style, le balisage et le script
tels quels. La matière du site est la **galerie**, arrêtée fiche par fiche par
l'auteur le 20260828. Reprendre le prototype ferait dépendre le site d'un outil
qui n'a jamais été validé pour la diffusion.

**Il porte une autre typographie.** Archivo et Archivo Black, palette
brique/or/crème. L'esthétique provisoire arrêtée est Fraunces et JetBrains Mono,
ocre, rouge, vert profond, aplat d'encre (A-149, A-154), et c'est celle que la
galerie porte. Le rebasage coûterait la réécriture de tout sauf la plomberie.

**Il n'a pas la forme que A-190 impose.** Une page HTML autonome unique, à vues
commutées en JavaScript, contre un dossier `site/` de pages statiques déployé sur
Vercel. Ce n'est pas le même objet.

**Il déclare des sections vides et des notes « en préparation ».** Manifeste,
vidéos, cinq notes de démonstration annoncées et non écrites. A-59 l'interdit :
un contenu qui promet et ne délivre pas est plus dangereux qu'un contenu sans
source.

**Ce qui se reprend malgré tout, et c'est l'essentiel de l'économie** :
`generer_fiches.py` est déjà factorisé par fiche — `fiche()` rend une carte
complète, `matiere()` monte le contexte d'une catégorie. Le générateur du site
l'importe au lieu de redessiner la fiche. Le rendu d'une fiche reste dans un
seul fichier, et le site ne fait que la placer.

Le nom canonique ne bouge pas (A-2) : `appareil/generer_site.py` est réécrit.
`livrables/site_prototype.html` meurt comme artefact, et la sortie devient
`site/`. L'index et la chaîne s'ajustent à l'écriture, pas avant.

### A-193 — Le squelette du site — question de fond, portée à l'auteur

Non tranché. Deux structures sont proposées au fil, avec ce que chacune rend
impossible. Le fil ne les tranche pas : il s'arrête. Ce que l'auteur commande —
combien de pages, ce qu'on lit avant la galerie, comment on navigue entre
dix-huit fiches — décide de la forme du générateur, donc appartient à l'output.

*Fait établi qui la nourrit, et qui n'était pas connu du fil courant* : **les
dix-huit fiches sont entièrement rédigées** — 83 gains d'attache sur 83 portent
leur apport, 20 pertes retenues sur 20 portent leur libellé. La surface
publiable n'est pas partielle : elle est complète. Les 80 gains en régime
transitoire que `make etat` compte sont des rappels, des modalités et des lignes
que la structure ne retient pas ; aucun n'imprime d'énoncé du livre sur une
fiche (A-179, A-183).

### A-194 — Deux dérives constatées à l'ouverture, non corrigées

*Ni l'une ni l'autre n'est un faux, et aucune ne se corrige à chaud.*

**`R2` compte l'archive technique parmi les artefacts non restaurés** alors que
`technique/coffre.txt` est au dépôt et concorde à l'octet avec son empreinte —
1 392 511 o, `77a6d115…`, 33 968 lignes. L'archive est déclarée au bloc
`archives` de l'index et non au bloc `artefacts` ; `controle_restauration.py` la
cherche du mauvais côté. Un contrôle qui signale comme absent ce qui est présent
use la confiance qu'on lui porte. À reprendre au contrôle, à la clôture.

**Le fil courant se contredit sur la surface publiable.** Sa tête dit « 124
apports rédigés sur 204 » ; sa section « Ce qui attend » dit « la surface
publiable d'aujourd'hui est de seize gains : `make etat` donne 16 apports
rédigés sur 194 ». `make etat` donne aujourd'hui **124 sur 204**. Le second
paragraphe est un état périmé de plusieurs passes. Il se réécrit à la clôture, en
même temps que le reste du fil courant.

---

## 20260828 — L'épreuve de format des gagnants-perdants

### A-190 — Le site est statique, et il se déploie sur Vercel

Tranché par l'auteur. **Vercel**, site statique : pas de base, pas d'API, pas de
rendu serveur. Le site se génère au dépôt dans `site/` et se déploie depuis là.

Deux voies de déploiement, non tranchées entre elles : le **jeton** — immédiat,
`vercel deploy --prod --token=…`, le jeton venant de l'auteur — ou le **dépôt
Git** relié au projet Vercel, plus durable mais qui demande un remote que
l'atelier n'a pas.

**Un jeton ne se met jamais au dépôt ni au coffre.** Il vit dans la session qui
déploie, et nulle part ailleurs.

Conséquence sur la chaîne : le site est un dérivé comme les autres. Un chiffre
qui change se corrige au référentiel, `make` régénère, on redéploie. Rien ne se
corrige en ligne.

### A-189 — Corrections de fond de la galerie, arbitrées par l'auteur

Tranché par l'auteur, appliqué à la source :

- **Les policiers ne sont pas « plus nombreux »**, ils sont renforcés et
  présents sur le terrain. La vedette du citoyen devient « Le terrain ».
- **L'inflation ne se dit pas en économiste.** La perte du citoyen devient
  « La vérité des prix » : la surtaxe disparaît, l'impôt se déplace sur le
  résultat, les certificats d'économie d'énergie s'arrêtent, ces prix-là
  baissent, et le solde tient dans **une inflation faciale inférieure à 2 %**.
  Le relais nomme l'offre, la concurrence et le rapport qualité-prix.
- **Les +220 € sont la moyenne au salaire type**, et le disent.
- **Le chômage ne se dit pas en moyenne.** Ni « sept mois » ni « treize à
  six » du point de vue de la personne : elle n'est plus indemnisée
  collectivement **au-delà de six mois**.
- **L'APL se maintient jusqu'au terme des baux en cours** et s'arrête pour les
  nouveaux contrats. Le libellé du locataire le dit.
- **Le foyer garde le seuil, pas les 600 €** : « un seuil unique, sans niche ni
  quotient, la même loi pour vous que pour tous ». Les 300 € de frais de
  gestion passent au patient, où ils appartiennent.
- **Le bénéficiaire d'un chèque ouvre sur le libre emploi de tout son argent**
  — 550 € en argent libre, dont il dispose en totalité.
- **Le locataire porte la baisse structurelle des prix** — l'offre qui monte et
  l'APL qui cesse de pousser les loyers —, la chute des frais de notaire et la
  hausse du salaire net.
- **L'entreprise ou l'association subventionnée montre ce qu'elle gagne** : sans
  formulaire, 0 € avant profit, un seul impôt, et **des clients plus riches**.
- **Le consommateur gagne le choix** : plus d'offre, plus de concurrence,
  meilleur rapport qualité-prix.
- **La personne handicapée ne perd rien.** Le bouclier sanitaire lui revient en
  gain, dit en entier.

### A-188 — Une fiche mince dit ses rappels en entier

Le rappel nu — la vedette seule en pied — suppose une fiche qui tient debout
toute seule. **Sous trois gains propres, elle ne tient pas** : la bande verte se
vide et la personne ne voit rien de ce qu'elle gagne.

Règle : sous trois gains d'attache, les rappels **pour lesquels un apport a été
écrit dans cette catégorie** remontent en ligne pleine. La matière est dite
ailleurs aussi, mais sous un autre angle, écrit exprès pour elle — ce n'est pas
une redite de mots. Un rappel sans apport propre reste nu.

Tambouille, inscrite au titre d'A-23. Elle ne révoque pas A-178 : l'attache
reste unique, et le rappel nu reste la règle dès que la fiche a de quoi vivre.

### A-185 — La dette par foyer était une image, elle cesse d'être une perte

**Corrigé à la source sur arbitrage de l'auteur.** `D11-1-1`, « 5 500 euros par
an et par foyer de dette publique supplémentaire », figurait au référentiel des
positions comme une **perte du foyer**. C'était une image du livre, non une
ligne de perte : le foyer ne perd pas 5 500 euros, il porte une dette qui
s'accroît.

La ligne est retirée, et les trois gains qui la prenaient pour miroir sont
raccrochés à la concentration de l'État sur ses sept missions.

### A-186 — Reprendre les concepts officiels du corpus, et nommer les montants

**Reproche de l'auteur, et il porte sur toute la galerie.** Le corpus nomme ses
objets ; une fiche qui les paraphrase se prive de ce que le lecteur reconnaît.

**Le bouclier sanitaire** se nomme, et c'est un gain — la vedette du patient
devient son nom, non son pourcentage. **Le compte éducation** porte son montant
annuel, 6 600 euros. **L'aide fondamentale** et le **compte épargne personnel**
se distinguent, toujours.

*Et les indications techniques de l'auteur ne se recopient pas verbatim* : elles
donnent le sens. « Rerégulation » et « fusion » étaient son vocabulaire de
travail, pas celui d'une fiche — ils deviennent *le formulaire* et *un seul
impôt*.

### A-187 — Corrections de la galerie, arbitrées

**Le citoyen** : l'effet de prix se dit *l'inflation*, et il se formule sans
promettre l'exactitude d'un taux — la restitution pousse les prix le temps que
l'offre suive.

**Le contribuable** : le solde des niches se dit *en baisse de charges et de
taxes*, non « directement ».

**Le foyer** : le rendement de 600 euros sort — redondant avec les 20 000 € et
perturbant. Le seuil d'imposition sort — du détail sans contexte.

**L'entreprise** : **les clients plus riches** entrent en vedette propre, comme
la consigne et le manuscrit le demandaient depuis le début. La paperasse, le
formulaire, un seul impôt : la langue remplace le jargon.

**L'enseignant** ouvre sur *la liberté* — vous choisissez où et comment
enseigner, et votre rémunération se négocie — et perd *la grille*, à côté du
statut que l'agent public perd aussi. Une perte peut frapper deux populations :
ce n'est pas un doublon si les deux libellés disent deux angles.

**La famille** : *la liberté scolaire* remplace *le contrôle*.

**Le retraité** ouvre sur la niche, dite comme telle, puis l'indexation. La CSG
sort : elle ne change pas pour lui. Et la fiche « au-dessus du seuil » disparaît.

**Le locataire** nomme l'APL en perte, à côté du parc social.

**Le bénéficiaire d'un chèque ciblé** remplace l'allocataire, et ses chèques se
nomment — pass culture, chèque restaurant.

### A-183 — La fiche choisit aussi ses pertes, et un rappel porte la vedette de son attache

Deux corrections d'appareil, tirées des arbitrages de l'auteur.

**La structure commande les pertes comme les gains.** Une perte que la carte ne
déclare pas ne paraît plus, même si le référentiel la porte pour cette
catégorie. C'est l'application entière de A-179 : la fiche choisit. Sans quoi la
personne handicapée gardait une perte que l'auteur venait de retirer.

**Un rappel porte la vedette du gain tel qu'il est dit chez son attache.** La
ligne de la catégorie qui rappelle n'a pas d'apport écrit : sa vedette se
relevait de l'énoncé du livre et sortait vide. Le retraité au-dessus du seuil et
l'entreprise subventionnée avaient un bandeau vert sans rien dedans.

*Et le bandeau ne s'imprime plus quand il n'y a ni gain ni rappel.*

### A-184 — Trois arbitrages de galerie

**L'usager d'une mission facultative sort.** L'auteur : couvert dans l'esprit par
le bénéficiaire d'un chèque ciblé et par l'agent dont le poste est supprimé.

**L'entreprise et l'association subventionnées fusionnent** en une fiche — *vos
aides s'arrêtent, vos impôts de production aussi, et vos clients ont 13 % de
plus*. C'est l'exemple du professionnel qui vit de l'argent public, et un seul
suffit.

**La personne handicapée ne perd rien, confirmé.** Sa fiche ne porte aucune
perte : 1 100 euros par mois versés automatiquement, et le reste à charge
plafonné en rappel — soutenable, et encore.

**Dix-neuf fiches** au bloc de lancement.

### A-181 — La structure est un document, et le générateur l'exécute

`appareil/structure_fiches.py` porte la série : pour chaque fiche, son titre,
son **axe en une ligne**, ses gains d'attache dans l'ordre de lecture, ses
pertes. C'est le document arbitré par l'auteur. `carte_attribution.py` le rend
lisible, `proto_fiches.py` l'exécute. **Une seule source**, et l'ordre interne
d'une fiche cesse d'être une table à part.

*Application directe de A-179* : la structure est la couche de sélection, le
référentiel reste la couche de description.

### A-182 — Le bloc de lancement, arbitré fiche par fiche

**Vingt-deux fiches**, 115 apports rédigés sur 200. Couverture : **les onze
catégories du prototype, toutes** — l'enfant étant dans la famille — et les
perdants de l'onglet de synthèse, soit par une fiche propre, soit par fusion.

**Fusions arbitrées par l'auteur** : le locataire HLM rejoint le locataire — la
perte est le gros rouge, le gain sort sur le privé ; l'étudiant de la gratuité
rejoint le jeune adulte ; le chômeur de longue durée rejoint la personne sans
emploi ; le bénéficiaire de taux réduit rejoint le consommateur ; le parent seul
rejoint la famille.

**Ajouts** : l'usager d'une mission facultative — le perdant central, qui
manquait —, l'entreprise subventionnée, l'association subventionnée, le
délégataire et prestataire public, la personne handicapée.

**Corrections de fond de l'auteur, et elles portaient toutes sur le sens.**

*La personne handicapée ne perd rien* : elle gagne un versement unique de
1 100 euros par mois, automatique, en lieu et place de l'empilement des
allocations. Sa fiche ouvre sur les plus.

*Le retraité, c'est une seule chose* — sa part des 20 000 €, en rente à vie —
et le rendement **suit les performances de l'économie**, ce qui vaut mieux
qu'une indexation votée chaque année.

*« Sur votre compte éducation » ou « sur votre compte épargne »* : jamais l'un
pour l'autre, jamais « votre compte » tout court.

*L'enseignant doit valoriser l'école libre, la rémunération négociée et le
compte universel*, faute de quoi il ne dit rien de plus que l'agent public
indispensable.

*Un exemple de professionnel qui vit de la subvention* entre dans la galerie :
l'association subventionnée, dont les donateurs sont plus riches que la
subvention ne l'était, et le délégataire, dont la commande captive s'arrête.

**Une capteuse paraît désormais sur la fiche d'une catégorie de rente**, dont
elle est le sujet — amendement de A-151, qui l'interdisait sur la fiche d'une
personne et le reste.

*Reste hors galerie* : onze catégories de rentes pures, sans personne derrière.
Elles appellent une fiche à part, et l'auteur ne l'a pas tranchée.

### A-179 — Deux couches : le référentiel décrit, la fiche choisit

**Énoncé par l'auteur, et c'est la clé de tout ce qui précède.** Il y a d'un
côté **la liste objective** — gains, pertes, montants, effets, paramètres,
complète et sourcée — et de l'autre **la génération de fiches, qui répond à une
logique propre et fait du cherry picking** pour être percutante, lisible et
complémentaire.

Ce sont deux choses, et les avoir confondues explique douze passes de reprise :
on cherchait à faire dire à une fiche tout ce que le référentiel porte, alors
qu'une fiche **choisit**.

**Conséquences, et elles rangent l'appareil.**

*Le référentiel ne se coupe jamais.* Une modalité, une redite, un gain non
retenu restent au corpus et au compte. `PLAFOND`, `MODALITES`, `REDITES`,
`ATTACHE` et `ORDRE` sont des **règles de sélection**, non des jugements sur la
matière.

*La sélection dépend de l'édition.* Il y aura plusieurs versions de la même
matière — côté entreprises, côté jeunes, côté retraités. Chacune choisira
autrement, et **le référentiel ne bougera pas.**

*L'édition en cours se déclare* : **une galerie de présentation générale**, sans
trop de détail, qui donne un bon aperçu et balaie les grands personas. C'est
elle qui commande le plafond de six lignes, les attaches et les rappels.

### A-180 — Les attaches, arbitrées par l'auteur

**Le foyer porte la restitution.** Les 20 000 € de patrimoine, le rendement de
600 € par an et par foyer, et « chacun paie ses choix sur son compte » — qui
n'avait rien à faire chez le travailleur — vont ensemble : ils sont la
restitution, et la restitution a une maille, le foyer.

**Le retraité, c'est une seule chose : les 20 000 €.** Le complément viager de
500 € par an et le rendement de 265 € par personne sont **le même capital**, et
le référentiel le dit — `D7-2-2-e1` porte « non cumulable avec le rendement
permanent de 264 € par an ». Les aligner comme deux gains était la faute. La
fiche dit donc : votre part des 20 000 € vous revient en rente, à vie.

**Et ce que le retraité perd est nommé** : l'abattement de 10 % sur les pensions
imposables, et **l'indexation automatique**.

*Manque relevé, et il est réel* : la fin de l'indexation n'est **une ligne
nulle part**. Elle n'existe au corpus que dans le champ `attenuation` de
`D7-2-2-e1` — « compense la fin des niches et indexations ». Une perte que le
plan produit et que le référentiel ne porte pas ne peut pas se dire. **À
instruire avant d'écrire la fiche du retraité.**

**Le citoyen, c'est l'État efficace et utile**, et c'est son gain principal — non
l'aide fondamentale, qui reste au jeune adulte. Un État qui fait moins et qui le
fait bien : plus de policiers sur le terrain, un régalien responsable, un
interlocuteur unique, l'audit permanent, le consentement périodique.

**La personne sans emploi porte la perte du chômage.** Six mois de solidarité
puis un compte à soi, et un marché qui embauche : la fiche se contextualise au
lieu de laisser la perte à une catégorie séparée. `C-41` disparaît de la galerie.

*Écartés* : la taxe foncière du contribuable — sous-sujet ; et la fiche de
l'épargnant, redondante avec le foyer.

### A-178 — Chaque gain a une attache, et revient ailleurs en rappel

**Arbitré par l'auteur, et cela révoque A-177.** Le socle était la même faute que
« tout le monde » : un bloc qui n'appartient à personne. *Tout le monde, c'est
personne* — la règle vaut pour une fiche comme pour un socle.

**Trois gestes, et ils se tiennent.**

**Croiser chaque gain vers là où il est le plus pertinent.** Une table `ATTACHE`
donne à chaque gain projeté sur plusieurs catégories **une** catégorie d'attache :
les 600 € et le taux unique au travailleur, les 20 000 € au jeune adulte qui
démarre avec un capital plutôt qu'avec zéro, la détente locative au locataire,
l'aide fondamentale à celui qui n'a pas d'emploi, les 275 € et le choix de
l'école au parent, le compte éducation à l'enfant. Il s'y dit **en entier**.

**Ancrer chaque catégorie sur ce qui lui appartient** : son gain principal, ou sa
perte quand elle est d'abord perdante, puis ses gains.

**Rappeler ailleurs, élégamment.** Partout où le gain n'est pas attaché, il
revient en pied de fiche sous sa **vedette seule**, sur une ligne : *Et comme
chacun — +13 % · 600 € · +25 % · 0,77 €*. La personne ne perd rien, et elle ne
relit jamais la même phrase.

*Ce que le croisement a donné* : le locataire du parc privé, que le socle avait
vidé, retrouve sa raison d'être — la détente du marché locatif lui est attachée.
Le locataire HLM ouvre sur sa perte et rappelle ses deux gains. L'enfant et le
parent se partagent la famille : le compte éducation à l'un, les 275 € et le
choix de l'école à l'autre.

*Reste vraie de A-177*, et c'est tout ce qui en reste : la redite est de matière,
non de mots, et aucun contrôle lexical ne la voit.

### A-177 — Ce qui est commun se dit une fois, au socle

**Question de l'auteur : « on fait comment ? »** — après trois passes où la
répétition revenait malgré A5, A6 et A7. Elle revenait parce que les trois
contrôles cherchent une redite **de mots**, quand la redite est **de matière** :
le même gain appartient à cinq personas, et l'écrire cinq fois sous cinq angles
ne fait que rendre les angles de plus en plus tirés.

**Un gain projeté sur deux catégories ou plus n'appartient à aucune : il
appartient au plan.** Il quitte les fiches et va au **socle**, dit une fois en
tête de la série. Chaque fiche ne porte plus que ce qui lui est propre. La
répétition ne se corrige plus, elle devient impossible.

*Et c'est le bon niveau de concept*, celui que « tout le monde » ratait en A-169 :
le socle n'est pas une personne, c'est ce que le plan rend à chacun. Il n'a donc
ni définition, ni effectif, ni perte.

**Ce que la mesure a donné, sur douze fiches** : dix gains au socle — les 600 €,
les +13 %, les 0,77 €, les +25 % d'offre locative, les 20 000 € de patrimoine,
la retraite en capital, les 550 € d'aide fondamentale, les 275 € par enfant, le
choix de l'école, le compte éducation.

**Et le socle dit lesquelles des fiches n'ont pas lieu d'être** — c'est le
sous-produit le plus utile de l'opération.

| fiche | en propre | verdict |
|---|---|---|
| jeune adulte, entreprise | 8 et 7 gains | tiennent largement |
| sans emploi, agent indispensable, retraité | 4 gains | tiennent |
| travailleur, agent au poste supprimé | 3 gains | tiennent |
| consommateur | 2 gains | tient de justesse |
| **enfant, parent** | **1 gain chacun** | à fondre en une fiche famille |
| **locataire du privé** | **rien** | sort de la série |
| **locataire HLM** | **rien, une perte** | n'existe que par sa perte |

*Questions portées à l'auteur*, et le fil ne les tranche pas : fondre `C-15` et
`C-17` en une seule fiche ; et que faire d'une fiche qui n'existe que par sa
perte, comme le locataire HLM — la garder telle quelle, la fondre dans le
locataire, ou l'écrire quand elle aura un gain propre.

### A-176 — La réduction croisée est un contrôle, pas une relecture

**Relevé par l'auteur** : « tu ne peux pas juste écrire au fil ». Deux défauts
que la relecture d'une fiche ne peut pas voir, parce qu'ils vivent **entre** les
fiches.

**A7 — un même ancrage ne porte pas deux fois le même apport.** Un effet atteint
plusieurs personnes, mais il ne leur fait pas la même chose : il y a toujours un
angle. Trois copies dormaient au corpus — le patrimoine restitué chez le jeune
adulte et chez le retraité, la détente locative chez le jeune adulte et chez le
locataire, l'indépendance de la pension chez le travailleur et chez le jeune
adulte. C'est un **échec**, non un signalement.

**A8 — une vedette est une grandeur ou un groupe nominal court.** Article et
nom, trois mots au plus, ou un objet nommé du corpus — compte épargne, compte
éducation, compte santé, aide fondamentale, plan de départ, taux unique.
« Reprendre paie », « Rien ne baisse », « On recrute » sont des phrases : chacune
invente une présentation, et douze fiches en font douze. Six vedettes sont
rentrées dans la forme.

*A3 se corrige au passage* : le registre se contrôle sur **la vedette et la
phrase ensemble**, puisqu'elles font une unité (A-147). « Votre pension — le
système se remet d'aplomb sans y toucher » s'adresse bien à quelqu'un.

*Ce que l'exercice a donné, et qui ne se serait pas vu autrement* : sur douze
fiches, dix ancrages sont projetés sur plusieurs catégories. Chacun porte
désormais son angle — le patrimoine restitué dit au jeune adulte qu'il démarre
avec un capital et non avec zéro, au retraité qu'il reçoit sa part.

### A-173 — Une dominante et cinq items, pas un de plus

**Arbitré par l'auteur**, après une fiche « tout le monde » qui en portait
vingt. Au-delà de six lignes, une fiche ne se lit plus d'un coup d'œil et ne
tient plus sur un écran de téléphone.

`PLAFOND = 6` au générateur. **Ce qui sort n'est pas ce qui tombe au hasard** :
la table `ORDRE` dit, catégorie par catégorie, ce qui passe — et le plafond
oblige à trancher plutôt qu'à empiler. Le reste demeure au référentiel et au
compte, et ressortira sur d'autres supports.

### A-174 — « Tout le monde » n'est pas une personne

**Arbitré par l'auteur, et cela révoque A-169.** On distingue le contribuable, le
citoyen, le foyer : ce sont des personas, même quand ce sont des concepts. Une
fiche « tout le monde » n'a pas de niveau de concept propre — elle mélange le
pays, le guichet et la personne, et elle ouvrait sur l'aide fondamentale, qui
n'est ni le bon niveau ni la bonne priorité.

`C-00` la nation ne prend donc pas de fiche. Les gains macro s'affecteront aux
personas quand chacune sera écrite sous son angle, et une version « les gains
pour l'économie » viendra à part.

*Reste ouvert* : `C-01`, `C-02` et `C-03`, dont le recouvrement n'est toujours
pas tranché — A-141 tient.

### A-175 — Réviser n'est pas réécrire

**Reproche de l'auteur, et il est fondé.** Sur une consigne de correction,
vingt et une fiches ont été réécrites là où onze demandaient une révision. Les
exemples donnés par l'auteur ont de surcroît été repris verbatim alors qu'ils
indiquaient une direction.

**Règle de conduite** : *une consigne de correction porte sur ce qu'elle
nomme.* Ce qui a été validé, même tacitement, ne se rouvre pas au passage. Et un
exemple de l'auteur donne le sens, non la lettre.

Le dépôt est revenu à l'état à douze fiches, sur lequel les seules consignes de
la passe sont appliquées : le plafond, le compte éducation nommé, l'agent public
**indispensable**, la charge stable de l'entreprise et ses quatre gains
valorisés — simplification, rerégulation, fusion, attractivité —, le quotient
familial porté au parent, et le locataire HLM ouvert.

### A-169 — La nation fond dans « tout le monde », et les gains macro vont aux personas

**Arbitré par l'auteur**, qui tranche A-141 : on reste sur des personas, même
quand ce sont des concepts — le contribuable, le citoyen —, et **les gains macro
identifiés leur sont affectés en présentation**. `C-00` la nation fond dans
`C-02`, qui s'affiche « Tout le monde ».

Cinq gains macro remontent par éventail : la simplification (10 000 € par foyer
et par an), les cinq points de croissance, le point d'efficacité, l'attractivité
pour les investisseurs, et les deux moteurs du travail et de l'épargne pour
l'entreprise.

*Ce que cela n'interdit pas* : une version « les gains pour l'économie et la
nation » viendra à part, plus tard.

*Reste distinct* : `C-01` le contribuable — ce que vous payez et qu'on vous
rend — et `C-03` le foyer — votre patrimoine et vos aides. Leur recouvrement se
tient par l'échelle, déjà déclarée au référentiel.

### A-170 — La charge de l'entreprise ne monte pas : « gain net » était trompeur

**Arbitré par l'auteur.** Écrire que le gain de la suppression des taxes « va au
salarié, pas à vous » laissait croire à une charge nette en plus. C'est faux hors
segments sursubventionnés : **ce qui sort de l'impôt sur le revenu et du crédit
d'impôt se retrouve dans la fusion fiscale**, et la demande monte de 13 %.

Le libellé devient factuel — *le partage* : le gain va au salarié, la charge
globale ne monte pas. Et quatre gains sont valorisés qui ne l'étaient pas : **la
simplification** (un principe court contre des milliers de pages), **la
rerégulation** (l'autorisation préalable disparaît, l'abus se sanctionne), **la
fusion** (un impôt unique sur les bénéfices contre l'empilement) et
**l'attractivité**. La vedette de la fin des impôts de production devient
*0 € avant profit* : on ne paie plus avant d'avoir gagné.

### A-171 — Le corpus nomme ses objets, et la fiche les nomme comme lui

**Relevé par l'auteur.** Compte épargne personnel, **compte éducation**, compte
santé : ces objets ont un nom au corpus, et les fiches disaient « où que vous
viviez » là où il fallait dire « votre compte éducation ». Les vedettes portent
désormais le nom de l'objet.

*Et « maintenu » disparaît* : `C-05` s'affiche **agent public indispensable**.
Le mot dit ce que le plan reconnaît, non ce qu'il concède.

### A-172 — Le bloc de lancement du site : vingt et une fiches

Périmètre arrêté par l'auteur : les onze fiches corrigées, les catégories du
proto, **les perdants de l'onglet synthèse**, et quelques gagnants pour
équilibrer.

Vingt et une fiches, **130 apports rédigés sur 201** — les huit lignes
nouvelles viennent des éventails. Les perdants adressés en propre :
l'allocataire d'aide ciblée, le chômeur indemnisé au long cours, le locataire
HLM, l'étudiant de la gratuité, le retraité au-dessus du seuil, le patient, le
foyer sur le quotient familial, le contribuable sur la taxe foncière, le citoyen
sur l'effet de prix. **Quatorze libellés de perte sont écrits.**

*Le parent hérite de la perte du quotient familial* par éventail : elle vivait
sur le foyer comme unité de mesure, elle touche le parent comme personne.

### A-166 — Le compte épargne se nomme, et le chômage n'est pas un gain

**Relevé par l'auteur, deux fois.** « L'essentiel de vos comptes personnels » ne
voulait rien dire, et « Le chômage » en vedette faisait passer une couverture
pour un gain.

**Le compte épargne personnel est nommé** — le corpus ne l'avait jamais fait,
il parlait de « cotisations restituées en épargne personnelle ». La ligne de
tête du travailleur dit désormais : *300 € — sur votre compte épargne
personnel : la retraite d'abord, le chômage ensuite.* **Les deux se nomment une
fois, ensemble et directement**, au lieu de tenir deux lignes dont l'une se
lisait à l'envers.

`D8-3-1-e2` devient une modalité du compte pour le travailleur. Il garde sa
ligne propre chez la personne sans emploi, où le compte chômage est le sujet, et
sa vedette y devient « Compte épargne ».

### A-167 — L'ordre de lecture est propre à chaque catégorie

**Relevé par l'auteur** : « l'ordre de priorité n'est pas le même dans chaque
catégorie ». Les `PROMESSES` du référentiel donnent l'ordre de la **chaîne
doctrinale** ; une fiche a besoin de l'ordre d'une **vie**.

Une table `ORDRE` vit donc dans `apports.py`, une entrée par catégorie : les
ancrages qui passent devant, dans cet ordre, le reste suivant les promesses. Le
jeune adulte ouvre sur son premier salaire et son aide fondamentale, le retraité
sur le patrimoine restitué, l'entreprise sur la fin des impôts de production,
la personne sans emploi sur le salaire qu'elle retrouvera.

*L'ordre entre catégories, lui, est déjà déclaré* : c'est celui des `GROUPES` du
référentiel, du plus large au plus particulier, les rentes en dernier. Les
fiches sortent dans cet ordre et non dans celui de la liste du générateur.

### A-168 — Une catégorie ne recopie pas la voisine : elle varie ou elle renvoie

**Relevé par l'auteur** : « tu te répètes pour le jeune ». Douze des vingt gains
du jeune adulte sont les mêmes nœuds que ceux du travailleur, et les apports en
étaient la copie.

Deux gestes, et ils tiennent tous les deux au format plutôt qu'à l'inspiration.
**Varier l'angle** : les 600 € se disent au travailleur par leur répartition, au
jeune adulte par leur somme — « ce que le plan vous rend chaque mois, salaire et
compte épargne réunis ». **Replier ce qui n'a pas d'angle propre** : cinq des six
gains du levier des études perdent leur vedette et se rangent sous « Vos
études ». La fiche passe de seize lignes à dix.

*Règle qui en sort* : **une vedette se mérite.** Un gain qui n'a pas quelque
chose que les autres n'ont pas se replie sous celui qui l'a.

### A-162 — Les 300 € des comptes personnels se publient, et la retraite passe devant

**Arbitré par l'auteur**, qui tranche A-161 : la part restituée sur les comptes
personnels se dit **300 €**, en parallèle des 300 € de salaire. La ligne de tête
du travailleur porte donc les deux destinations chiffrées.

*Statut du chiffre, et il se déclare* : `D3-2-2-e1` décompose les 600 € en
275,08 € de gain CSG-CRDS et **292,22 € reconstitués par différence**. Les
300 € sont l'arrondi de communication de cette seconde part, au même titre que
les 300 € de salaire arrondissent 275,08. Il sort avec ce statut ou il ne sort
pas.

**L'ordre à l'intérieur des comptes est tranché** : la retraite est
l'essentiel, le chômage un petit bout, et la fiche le dit dans cet ordre.
`D8-2-2-e1` entre aux `PROMESSES` avant la santé et le chômage.

### A-163 — La contrepartie « pensions supérieures à 1 600 euros » était fausse

**Relevé par l'auteur**, et retiré sans délai. Les pensions supérieures à
1 600 euros gagent **l'impôt sur le revenu**, non la restitution des cotisations
retraite. Sept lignes la portaient. `C_RETRAITE` est supprimé d'`apports.py` ; la
ligne de retraite ne porte plus de contrepartie propre.

*Ce que la faute enseigne* : une contrepartie plausible est plus dangereuse
qu'une contrepartie absente. Elle a l'apparence d'une traçabilité, et elle
survit à toutes les relectures qui ne remontent pas au chiffrage. Seules deux
contreparties restent affichées, et elles se vérifient : le chômage et rien
d'autre.

### A-164 — Le statut ne se réduit pas à l'emploi à vie

**Relevé par l'auteur.** « L'emploi à vie prend fin » nommait une partie pour le
tout. Le libellé de la perte de `C-05` dit désormais ce qui s'arrête :
**le statut de la fonction publique**, dont l'emploi garanti, la carrière et les
règles propres, qui cèdent au droit du travail commun.

### A-165 — Huit catégories du prototype sont écrites

Sur demande de l'auteur, et pendant son absence : **52 apports, 52 vedettes et
cinq libellés de perte** pour les catégories du proto Données qui portent des
gains — `C-16` jeune adulte (20), `C-06` entreprise (8), `C-10` personne sans
emploi (7), `C-09` retraité (6), `C-15` enfant (4), `C-17` parent (4), `C-23`
consommateur (2), `C-11` locataire (1).

**Le corpus porte 72 apports rédigés sur 194**, contre 20 le matin.

*Deux catégories du proto sont écartées et attendent l'auteur* : `C-02` citoyen
et `C-03` foyer, bloquées par **A-141** — leur recouvrement avec `C-01`
contribuable n'est pas tranché, et les écrire avant reviendrait à les écrire
deux fois. `C-00` la nation relève du même groupe et de la même question.

*Deux règles de composition tirées du lot.* **Le gain qui raccroche ne passe en
tête que sur une fiche qui ouvre sur une perte** : ailleurs l'ordre des
promesses commande, et une contrepartie n'est pas une promesse — sans quoi le
retraité ouvrait sur 500 € de complément viager au lieu de 20 000 € de
patrimoine. Et **un agrégat national ne devient jamais une vedette** : les
30 Md€ du chômage et les 16 Md€ de taxes supprimées se disent par ce qu'ils font
à la personne.

### A-159 — Une perte se dit comme un gain, et elle ne redit pas ce qui la compense

**Arbitré par l'auteur, deux fois plutôt qu'une.** « Arrête avec les 70 % en
petit puis en gros : on garde juste gros, sans astérisque. » Le renvoi par
astérisque d'A-157 est révoqué : il réglait la redite en la rendant énigmatique.

**La carte de perte ne porte plus d'échange.** Sur une lecture linéaire, le gain
qui raccroche se lit quelques centimètres plus bas, à sa place et en grand. La
raccroche est tenue par la mise en page, non par une redite.

**Et la perte se compose comme le gain** : une **vedette** d'un ou deux mots nus
— « Le poste », « Le statut » —, puis une phrase factuelle, puis sa raison.
`justifications.py` prend ce quatrième champ. *Consigne de l'auteur, et elle
tranche le registre* : factuel basique, ni euphémisme ni dramatisation —
**on ne ment pas**, et on n'effraie pas.

*Amende A-157* sur l'astérisque et sur l'échange en pied de carte. Ce qui en
reste : les redites de maille, qui tombent bien.

### A-160 — Un agrégat national n'a rien à faire sur la fiche d'une personne

**Relevé par l'auteur** : « les 30 Md€, on s'en fiche, c'est pas lui. » Une
fiche répond à « qu'est-ce que ça me fait » ; un montant national n'y répond
pas, même quand il est juste.

La ligne du chômage garde son apport et change de vedette : **« Votre compte »**,
et la phrase dit que les cotisations alimentent une épargne au nom de la
personne. Le 30 Md€ reste au référentiel, où il sert au chiffrage.

*Deux corrections de langue avec elle.* **« En franchise » disparaît** : le
propos va avec les 0,77 €, qui le portent désormais dans leur phrase — la ligne
devient une modalité. Et **le montant restitué se dit sur ses deux
destinations** : « rendus tous les mois, sur votre salaire net et sur vos
comptes personnels ».

### A-161 — La composition des 600 € : question portée à l'auteur

**Non tranché, et c'est le seul point où la demande de l'auteur bute sur une
règle du corpus.** Il demande de nommer le compte d'épargne « avec 300 € pour
la retraite, en parallèle des +13 % à 300 € ».

Ce que le corpus porte : `D3-2-2-e1` décompose les 600 € en **275,08 €/mois de
gain CSG-CRDS** et **292,22 €/mois d'autres économies restituables**, ce second
terme étant marqué **reconstitué par différence**. Le manuscrit ne dit nulle part
qu'environ 300 € vont à l'épargne retraite : `D8-2-2`, « cotisations restituées
en épargne personnelle », ne porte aucun montant mensuel.

**Écrire « 300 € sur votre compte retraite » fabriquerait un chiffre** — un
résidu de soustraction présenté comme une destination. La fiche dit donc les deux
destinations sans les chiffrer.

*Question fermée* : publie-t-on la décomposition ~300 € de salaire / ~300 € de
comptes personnels, en assumant que la seconde part est reconstituée par
différence et non relevée ? Si oui, elle entre au référentiel des faits avec ce
statut et sort partout de la même façon.

### A-155 — Le décompte des agents perdants est 580 000, et le 0,54 M est périmé

**Arbitré par l'auteur, et c'est une correction de fait.** « Les 0,54 M sont
fautifs et obsolètes, pas la doctrine à date. » Le décompte qui vaut est celui
d'A-130 : **580 000 postes publics**, 10 % des 5,8 M d'agents.

Trois corrections au référentiel des positions. L'effectif de `C-30` passe de
« 0,54 M à un an, 580 000 postes publics à terme » à **580 000 postes
publics**. La grandeur de sa perte principale ne porte plus de chiffre. Et
`C-05` se recalcule : 5,8 M moins 580 000, soit **5,22 M** au lieu de 5,26 M.

*Le 0,54 M vit ailleurs et se signale plutôt que de se poursuivre* :
`methode/derivation_D2.md` porte la lecture du classeur qui l'a produit. Elle
reçoit un bandeau de correction en tête, sans que ses tableaux soient réécrits —
un document de dérivation dit ce qu'on a lu ce jour-là.

### A-156 — « Qui paie » saute, sauf lien unitaire manifeste

**Arbitré par l'auteur** : « c'est important pour nous pour identifier les
pertes, ici c'est creux. » La contrepartie générale reste au référentiel, où
elle sert à instruire ; **elle ne s'affiche plus**.

Ne restent visibles que les contreparties à **lien unitaire manifeste** — le
chômage, dont la restitution vient de l'indemnisation ramenée de treize à six
mois, et la retraite, gagée sur les pensions supérieures à 1 600 euros. Le
cartouche de pied disparaît.

*Amende A-146 et A-152* sur l'affichage. Le fond — la restitution est payée par
l'ensemble des économies — est intact, et c'est justement ce qui rend son
affichage creux : une formule vraie de toutes les lignes n'informe sur aucune.

### A-157 — Une lecture linéaire ne ressasse pas : l'échange renvoie, il ne recopie pas

**Relevé par l'auteur.** Le même gain se lisait deux fois sur la fiche de
l'agent public — en pied de la carte de perte, puis en tête du côté plus.

La carte de perte porte désormais **la seule vedette du gain, suivie d'un
astérisque**, et le gain visé porte le même astérisque. Le texte se lit une
fois, à sa place. *Règle générale* : un point peut reparaître sous un autre
angle, cela doit rester ponctuel.

**Deux redites de fond tombent avec.** L'échelon local supprimé et le poste
retiré du décompte national disent le même événement que la fermeture de
l'administration, à deux mailles. Un dictionnaire `REDITES` les rattache à la
carte qui les recouvre : elles restent au référentiel et au compte, elles ne
prennent pas de carte. « Votre administration ferme » suffit, et l'anxiété que
portait « l'échelon local où vous servez disparaît » avec elle.

*Conséquence de dérivation* : la part de pertes qui commande l'ordre
d'ouverture se calcule sur **tout ce que le référentiel porte, redites
comprises**. C'est le poids de la perte qui décide, pas le nombre de cartes
imprimées — sans quoi déduplicer ferait basculer la fiche du mauvais côté.

### A-158 — Cinq corrections de langue, sur demande de l'auteur

Portées à `apports.py`, sans changement de fond.

**« L'aide fondamentale » se nomme en toutes lettres** — elle ne se dit pas
« une aide inconditionnelle ».

**« Mieux armés » disparaît**, terme bancal, remplacé par « Les moyens ».

**« Promotion et primes au mérite »** figurent en clair sur la carrière de
l'agent public maintenu, là où l'on lisait « rémunération qui suit vos
résultats ».

**« Votre temps »** et non « Le temps » : l'appropriation est le gain.

**Les 13 % sont un atout du privé** et non un gain séparé, pour l'agent dont le
poste est supprimé : la ligne devient une modalité rattachée à « Le privé », qui
les porte désormais dans sa phrase.

### A-150 — Une modalité n'est pas un gain : restituer n'est pas réciter

**Arbitré par l'auteur** : « l'objectif c'est d'être pertinent dans la
restitution, pas de faire le perroquet. Les 2 % sont une modalité secondaire,
pas un gain en tant que tel. »

La restitution par paliers de 2 % par mois dit **comment** arrivent les 600 € ;
elle n'ajoute rien à ce qu'on reçoit. Un dictionnaire `MODALITES` la rattache au
gain qu'elle qualifie ; la ligne reste au référentiel, à son apport et au
compte, **elle ne prend pas de ligne de fiche**.

*Écarté* : un plafond de lignes par fiche, qui aurait fait tomber ce que l'ordre
place en dernier plutôt que ce qui n'est pas un gain. Et le retrait de l'apport,
qui aurait fait baisser le compteur de rédaction à tort.

*Portée* : la qualification se prend en écrivant, ligne par ligne. C'est une
décision de plus par gain, et elle est le prix de la pertinence.

### A-151 — Un capteur ne paraît pas sur la fiche d'une personne

Tranché par Claude au titre de A-23, sur le cas de `C-05`. Une rente supprimée
n'est pas une perte portée par l'agent public maintenu : c'est le solde d'une
rente attachée au statut. La faire figurer en « ce que vous perdez » ferait dire
à la fiche que la personne perd ce que la collectivité cesse de payer.

Les capteurs vivent au groupe des rentes supprimées, où le référentiel les range
déjà. *Conséquence* : la part de pertes qui commande l'ordre d'ouverture se
calcule sur les seuls perdants, et `C-05` ouvre sur les plus — un tiers pile
n'ouvre pas sur les moins, il faut le dépasser.

### A-152 — « Qui paie » ne qualifie pas une perte

**Relevé par l'auteur.** Le cartouche de financement qualifie une restitution.
Sur une fiche qui ouvre sur une perte, il répond à une question que personne ne
pose et il se lit de travers.

Il ne paraît donc que sur les fiches qui ouvrent sur les plus, et il **clôt la
fiche** au lieu de s'intercaler entre les deux côtés. Sur une fiche qui ouvre sur
les moins, chaque carte de perte porte déjà son échange.

### A-153 — Le libellé de perte est écrit, et le pendant de `C-30` est ouvert

Le manque relevé en A-138 se comble là où le prototype en a besoin :
`justifications.py` prend un troisième champ, cinq à huit mots du point de vue de
la personne. Quatre sont écrits — « L'agence qui vous emploie ferme »,
« L'échelon local où vous servez disparaît », « Un poste public sur dix
disparaît », « L'emploi à vie prend fin ».

**`C-05`, l'agent public maintenu, est ouvert en pendant de `C-30`**, sur demande
de l'auteur : quatre apports, quatre vedettes, un libellé de perte. Le corpus
porte vingt apports rédigés sur cent quatre-vingt-treize.

*Nommer « public »* : la définition de `C-05` et celle de `C-30` portent le mot,
comme leur effectif.

### A-154 — La page ne porte plus de mentions de travail

**Relevé par l'auteur.** Le pied « tout ce qui figure ici vient du référentiel »,
le bloc `[interne]`, les étiquettes *libellé à écrire* et *titre proposé*
sortaient sur la page. Ce sont des notes de chantier : elles se disent au fil, pas
au lecteur.

La fiche est désormais nue. Ce qui reste ouvert se rapporte à l'auteur en
conversation et vit au registre.

*Habillage, en attendant la charte* : le fond crème est remplacé par un aplat
d'encre, les bandes passent à fond perdu, et un surtitre porte le groupe du
référentiel. **La charte reste un fil dédié, à ouvrir après le bon à tirer du
format** — arbitrage de l'auteur. Les typographies en vigueur sont **Fraunces**
pour le texte et les titres, **JetBrains Mono** pour les chiffres et les
étiquettes.

### A-146 — Un contresens de contrepartie : la restitution est payée par tout, pas par une niche

**Relevé par l'auteur, et c'est une faute de fond.** Treize gains portaient une
contrepartie nominative — « payé par la fin de l'abattement de 10 % sur les
pensions les plus élevées », « payé par la fin de la gratuité apparente des
études supérieures ». Attribuer à une niche ce que finance tout le plan est un
contresens, et il est attaquable : le premier lecteur qui compare l'abattement au
montant restitué a gagné.

**La règle** : *presque toute la restitution est payée par l'ensemble des
économies.* Deux exceptions, et elles seules — le **chômage**, dont la
restitution vient de l'indemnisation ramenée de treize à six mois, et le
**patrimoine**, retraite comprise, dont la source est nommée au corpus.

`apports.py` porte donc `CONTREPARTIE_GENERALE`, et neuf lignes sur seize la
prennent. **Le format la dit une fois en pied**, sous un cartouche « Qui paie »,
au lieu de la répéter à chaque ligne. Les contreparties propres restent sur leur
ligne, en gris, où elles sont une information et non un remplissage.

### A-147 — Un gain porte une vedette, et elle n'est pas toujours un chiffre

**Arbitré par l'auteur** : « on peut mettre sur le même plan des chiffres et des
éléments non chiffrés, comme le temps pour les agents publics ».

Un troisième champ rédigé s'ajoute au côté gain : `vedette`, deux ou trois signes
en tête de ligne. Un chiffre quand le gain en porte un — « 600 € », « +13 % » —,
**deux mots quand il n'en porte pas** — « Le temps », « Votre capital »,
« Zéro impôt ». Le chiffre se compose en JetBrains Mono, le mot en Fraunces, tous
deux à la même place et au même rang.

*Amende A-137.* Le relevé automatique de la quantité depuis l'apport reste, mais
**en secours seulement**, pour les 178 gains encore en régime transitoire. Il
n'était plus tenable dès lors que la phrase cesse de répéter la quantité :
« 600 € » puis « rendus tous les mois, sur votre compte » n'offre plus rien à
relever.

**Conséquence, et elle est la vraie nouveauté de forme** : *la vedette et
l'apport font une seule unité et ne se citent pas séparément.* Tout livrable qui
projette un apport projette sa vedette avec lui.

*Deux règles de composition qui en découlent, tranchées par Claude* : une
quantité qui croît porte son signe — `+13 %`, `+2 %` —, un niveau ne le porte
pas ; et les centimes se disent en euros, `0,77 €` et non `77 c`, qui ne se lit
pas.

### A-148 — Les apports se disent court, et la grappe se coiffe par sa tête

**Arbitré par l'auteur** : « les phrases peuvent être plus courtes et punchy,
comme sur les chiffres ». Les seize apports sont réécrits, sens et chiffres
inchangés, la quantité passée en vedette. Médiane : 16,5 mots avant, **12 mots
après**. `make controle` sort désormais **zéro signalement de registre** là où il
en sortait trois.

*Correction de la grappe (A-144)* : une grappe se compte par levier, **tête
comprise**, et le gain qui porte une vedette écrite peut la mener. « Votre
capital » coiffe les trois autres gains de la retraite au lieu de flotter à côté
d'eux. Ce qui reste vrai : un gain à vedette écrite ne se replie jamais sous un
autre — c'est pourquoi « Le temps » et « Le privé » tiennent leur rang à côté de
« 70 % » chez l'agent public.

### A-149 — Un seul format, et il porte la signature Résolution

**Arbitré par l'auteur** : « lecture linéaire complète pas mal, genre B ou A.
Fais un seul format. » Les trois traitements fusionnent en un — la tête en grand
du montant, les lignes à vedette de la balance, les cartes de perte communes aux
trois. La grille et le parcours sont abandonnés.

**La signature tient en trois choses, et pas une de plus** tant que la charte
n'est pas écrite : le bloc-marque **RÉSOLUTION** en mono espacé avec sa ligne de
service, le **filet à trois couleurs** — vert, ocre, rouge, en proportions
inégales —, et le cartouche de pied. Le reste est la palette et la grille de
l'esthétique provisoire.

*Nommer « public ».* Sur demande de l'auteur, la définition de `C-30` et son
effectif portent le mot — « agent public », « 580 000 postes publics » —, et le
titre d'affichage proposé devient **« Agent public dont le poste est
supprimé »** (A-145). Le gain de salaire de cette catégorie dit désormais d'où il
vient : la hausse des salaires nets **dans le privé**, dont l'agent profite dès
qu'il y reprend un emploi, indemnité comprise.

### A-142 — Le parcours est retiré : il affirmait une absence, et elle était fausse

**Relevé par l'auteur, et c'est une faute de fond, pas de forme.** Le troisième
traitement mettait deux colonnes face à face, « ce qui s'arrête » et « ce qui
prend la place ». Pour `C-04`, qui ne porte aucune ligne de perte, la colonne de
gauche imprimait douze fois « rien ne change ».

**C'est faux.** Le référentiel dit que la catégorie ne porte aucune ligne de
perte ; il ne dit pas que la personne ne perd rien. Le travailleur perd des aides
fléchées comme tout le monde — la contrepartie de chacun de ses douze gains
l'écrit déjà, « payé par l'arrêt des missions facultatives de l'État, dont
l'usager perd le service ».

**Règle qui en sort, et elle vaut pour tout livrable** : *une fiche n'affirme
jamais une absence.* Un silence du référentiel se rend par un silence, jamais par
une négation. C'est le pendant, du côté forme, de « aucune source ne s'invente,
aucun trou ne se comble ».

*Le parcours est remplacé* par **la grille** : les moins d'un côté, les plus en
mosaïque de l'autre, sans mise en regard ligne à ligne.

### A-143 — Les deux côtés ne se présentent pas pareil, et l'ordre suit la catégorie

**Arbitré par l'auteur**, en deux points, et Claude en tire la règle mécanique.

**Une perte n'est pas une ligne, c'est une carte.** Elle porte sa justification et
sa raccroche, un gain porte une phrase. Une grille uniforme les met au même rang
et alourdit la fiche pour rien. Les trois traitements partagent désormais une
seule forme de perte — carte rose, filet rouge, l'échange en pied — et chacun a
sa forme de gain.

**On commence par les plus là où les plus dominent, par les moins pour les
perdants spontanés.** Le partage se lit au référentiel et ne se décide pas fiche
par fiche : **une catégorie dont les pertes font au moins le tiers de ses lignes
ouvre sur les moins.** `C-30` — trois pertes, quatre gains — ouvre sur les moins ;
`C-04` ouvre sur les plus. Le pied de chaque fiche dit par quel côté elle ouvre.

*Conséquence tirée par Claude* : quand la fiche ouvre sur les moins, **le côté
plus commence par le gain auquel les pertes se raccrochent**. Pour l'agent, c'est
le plan de départ et non la hausse des salaires ; c'est ce qu'il cherche.

### A-144 — Une grappe de gains se replie, et deux contrôles la trouvent

**Relevé par l'auteur** — « attention à ne pas en avoir trop qui se ressemblent ».
Quatre des douze gains de `C-04` portent sur la retraite par capitalisation :
quatre lignes de même poids pour un seul message.

**La ressemblance ne se voit pas dans les mots.** « Votre retraite se voit »,
« vous gardez la maîtrise du fruit de votre travail », « elle ne dépend plus
d'une caisse », « elle ne dépend plus d'une promesse politique » n'ont pas trois
mots communs. Ce qui les trahit est leur origine : toutes relèvent du levier
`D8-2`.

Deux contrôles, tous deux signalements. **A5** compare les mots pleins deux à
deux à l'intérieur d'une catégorie et sort les couples au-dessus de la moitié.
**A6** sort les grappes — trois gains ou plus d'une catégorie sous le même
levier. A5 trouve un couple, A6 trouve les deux grappes du prototype : `C-04`
sous `D8-2`, quatre gains ; `C-30` sous `D6-2`, trois gains.

*Conséquence de forme, et c'est le format qui absorbe le défaut* : **une grappe se
replie.** Le premier gain se dit en grand, les autres en dessous, compacts. Rien
n'est perdu, rien n'est réécrit, et la fiche retrouve un message par bloc.

### A-145 — Le titre d'affichage d'une catégorie n'est pas son terme de référentiel — *proposé*

**Relevé par l'auteur** : « agent d'une structure fermée, c'est trop cryptique ».
Le terme du référentiel sert à ranger cinquante-six catégories sans collision ;
il ne sert pas à ce que quelqu'un s'y reconnaisse.

**Proposition de Claude, non validée** : `C-30` s'affiche « Agent dont le poste
est supprimé ». Le terme du référentiel n'est pas touché — une table de titres
d'affichage vit dans le générateur, et l'écran porte la mention *titre proposé*
tant que l'auteur n'a pas tranché.

*Portée* : si la voie est retenue, les cinquante-six termes se relisent une fois,
et c'est une unité de travail à part — pas cinquante-six écritures, une relecture
avec quelques réécritures.

### A-136 — Un apport recopié du manuscrit est refusé par un contrôle, désormais écrit

Tranché par Claude au titre de A-23, sur mandat exprès de l'auteur.

Le fil courant portait « écrire le contrôle qui refuse un apport recopié du
manuscrit » comme l'un des trois actes préalables à l'écriture. Il n'existait
pas. `appareil/controle_apports.py` le porte, joué à `make controle`.

Quatre contrôles. **A1** — un apport ne reprend pas l'énoncé du nœud qu'il
projette, la comparaison portant sur le texte normalisé et dans les deux sens.
**A2** — un apport ne porte pas huit mots consécutifs du manuscrit ; en deçà de
huit, une expression commune est une coïncidence de langue. **A3** — registre :
deuxième personne du pluriel, aucune nomenclature interne, le corpus jamais cité
comme autorité. **A4** — la contrepartie suit A1 et A2.

**A1, A2 et A4 sont des échecs ; A3 est un signalement.** L'appareil contrôle
les faits et il est aveugle à la voix : un apport hors registre se juge, il ne se
prouve pas.

*Pourquoi ce contrôle et pas un autre* : une ligne sans apport se projette par
l'énoncé du REF, qui est une phrase du livre. Un apport qui recopie cette phrase
n'écrit rien et fait passer le régime transitoire pour la cible — c'est le
compteur de `make etat` qui se met à mentir, et rien ne le voyait.

Éprouvé à l'envers avant d'être admis : deux faux apports injectés, l'un recopié
d'un énoncé, l'autre d'une phrase du manuscrit, sortent en A1 et en A2. Les seize
apports du corpus sortent à zéro échec, trois signalements de registre.

### A-137 — Le chiffre affiché se relève de l'apport, non du champ `chiffre` du REF

Tranché par Claude au titre de A-23. Un format visuel a besoin d'un chiffre
court en tête de ligne. Trois sources possibles, une seule tient.

Le champ `chiffre` du `REF_doctrine` est une phrase du livre — « +13 % en un an ;
+300 €/mois salarié type ; SMIC +180 €/mois ». En extraire le premier nombre
reproduirait exactement le défaut déjà relevé au relevé des chiffres, où
trente-neuf candidats sur cent neuf ne portent pas le fait qu'ils paraissent
porter. Le champ `grandeur_derivee` ne porte pas de chiffre pour `C-04` : il vaut
`qualitatif` ou vide sur onze lignes sur douze.

**C'est donc l'apport qui donne le chiffre.** Il est écrit pour le lecteur, et la
première quantité qu'il porte est celle qu'on veut montrer. Le relevé se fait sur
un vocabulaire d'unités fermé, comme celui de `REF_chiffres` : pour cent, euro,
milliard, million, centime, et le nombre nu pour un effectif.

*Conséquence sur l'écriture, et elle est la seule contrainte nouvelle du format* :
**un apport qui porte une quantité la met en tête.** Sept des seize apports écrits
en portent une ; les neuf autres s'affichent sans chiffre, et c'est un résultat du
prototype, pas un défaut à masquer.

*Écarté* : un troisième champ rédigé `chiffre_affiche`, qui aurait ajouté cent
quatre-vingt-quatorze écritures pour redire ce que l'apport porte déjà.

### A-138 — Le côté perte n'a pas de libellé court, et c'est le seul manque que le format révèle

Constaté au référentiel, pas rapporté ailleurs. Les soixante et onze pertes et
rentes portent `justification` — médiane trente mots — et `relais` — médiane
vingt-quatre. **Aucune ne porte de phrase courte.**

Un format visuel en demande une : cinq à huit mots qui disent ce qui s'arrête, du
point de vue de la personne. Faute de quoi le prototype affiche l'énoncé du REF,
qui est écrit du point de vue des finances publiques — `C-30` reçoit ainsi
« Économies de fonctionnement local » en tête d'une perte. Les trois traitements
le marquent d'une étiquette *libellé à écrire* plutôt que de le masquer.

*Conséquence sur le coût, portée à la ré-estimation* : le côté perte, réputé
complet, ne l'est pas pour un format visuel. Quarante-neuf libellés de perte et
vingt-deux de rente s'ajoutent au volume.

### A-139 — Plusieurs pertes qui se raccrochent au même gain le disent une fois

Tranché par Claude au titre de A-23, sur constat du prototype. Les trois pertes
de `C-30` se raccrochent toutes à `D6-2-2`, le plan de départ. Le premier jet
imprimait la même phrase trois fois de suite.

La raccroche s'écrit donc sur la première perte, et les suivantes y renvoient.
Trois fois la même phrase n'est pas une insistance, c'est du bruit — et cela
affaiblit précisément ce que A-131 veut rendre visible.

*Conséquence de forme* : dans le traitement par montant, le chiffre dominant
n'est plus le premier gain chiffré mais **le gain auquel les pertes se
raccrochent**. Pour l'agent, c'est le plan de départ et non la hausse des
salaires ; c'est ce qu'il cherche en ouvrant la fiche.

### A-140 — « Jusqu'à sept ans » et « sept ans » — question de fond, portée à l'auteur

Constaté, non tranché, et c'est le seul point de ce fil qui ne se tranche pas
seul.

`D6-2-2-p2` est un **plafond** : ses conditions disent « versée jusqu'à sept ans,
non pendant sept ans », et l'alerte structurelle R10 signale déjà une borne
présentée comme valeur unique. Les quatre apports écrits ici disent donc
« versés jusqu'à sept ans ».

**Les trois `relais` du côté perte, écrits avant, disent « je gagne sept ans à
70 % de mon traitement ».** Les deux se lisent côte à côte dans la même fiche :
la perte promet sept ans, le gain en promet au plus sept.

Ce n'est pas une faute de recopie, c'est une question de registre et de rang :
une promesse se dit-elle au plafond ou à la borne ? La règle du corpus dit
« un constat se dit précis, une promesse en ordre de grandeur », ce qui plaide
pour le plafond ; la prudence de contestabilité plaide pour la borne. **À
trancher par l'auteur**, et la réponse vaut au-delà de ce cas.

### A-141 — Le recouvrement de `C-01`, `C-02` et `C-03` est instruit, non tranché

Instruit au référentiel, porté à l'auteur — il commande les cinquante-trois
apports du groupe « Tout le monde » et se pose avant la première ligne.

Ce que le référentiel porte déjà, et qui n'était pas dit : **les quatre
catégories du groupe se distinguent par leur maille et par leur échelle, pas par
leur population.**

| | maille | effectif | échelle | ce qu'elle porte |
|---|---|---|---|---|
| `C-00` la nation | personne | 68 M | macro | 20 gains, 8 diagnostics — écarts avec les pays comparables |
| `C-02` citoyen | personne | 68 M | macro sauf 3 | 16 gains, 13 qualitatifs — droits, services, libertés |
| `C-01` contribuable | foyer | 30 M foyers | macro | 12 gains, 6 en euros par mois et par foyer |
| `C-03` foyer | foyer | 30 M | micro | 5 gains — patrimoine restitué, aides reçues en propre |

**Deux recouvrements réels, et un seul est dangereux.**

`C-01` et `C-03` partagent la maille — trente millions de foyers — et se
séparent par l'échelle : `C-01` ramène un agrégat national au foyer, `C-03`
donne ce que le foyer touche en propre. Les additionner doublerait le compte.
C'est le recouvrement dangereux, et la ligne de partage existe déjà au
référentiel, colonne `echelle`.

`C-02` et `C-00` partagent la population — soixante-huit millions — et se
séparent par la nature : ce qu'on est en droit d'attendre contre ce que le pays
devient. La distinction tient à la lecture, elle est mince à vue.

*Trois voies pour l'auteur, et ce sont les seules.*

**Fondre `C-01` dans `C-03`** et ne garder qu'une fiche « votre foyer », l'échelle
devenant deux sections de la même page. Dix-sept apports au lieu de dix-sept, mais
une fiche au lieu de deux — et le risque de double compte disparaît de la
surface.

**Fondre `C-02` dans `C-00`** et ne garder qu'une fiche « tout le monde », les
gains qualitatifs et les écarts comparés se lisant ensemble. Trente-six apports,
une fiche.

**Garder les quatre** et écrire en tête de chacune ce qu'elle ne dit pas. C'est
la voie la plus coûteuse en écriture et la plus sûre contre le double compte.

*Ce que Claude ne tranche pas* : lesquelles fondre. C'est un output, il se valide.

---

## 20260827 — Un projet PLF en libre accès, et la frontière de ce qui traverse

### A-134 — Le contre-PLF prend un second projet, en libre accès, et il ne reçoit que du dérivé

**Arbitré par l'auteur**, et c'est exactement le cas d'accès que A-133 réservait :
le contre-PLF sera ouvert à des tiers, la matière se prépare ici en partie.

*Amende A-133* sur la conclusion, pas sur le raisonnement. Le risque nommé — deux
copies du corpus, deux points de vérité — se neutralise par le sens unique.

**Le projet ouvert est une publication, pas un atelier.** Il reçoit ; il n'écrit
rien qui ne se régénère ici. Même relation que le site au corpus (A-123). Rien ne
revient de lui vers le coffre.

**Ce qui traverse.**

- Les trois annexes budgétaires du PLF — taxes affectées, dépenses fiscales,
  dépenses du budget général. Ce sont des documents publiés par l'administration,
  ils ne nous appartiennent pas.
- L'appareil qui les lit : `socle_budgetaire.py` réduit à ces trois lecteurs,
  `nomenclature_lolf.py`, `controle_socle.py`. Un lecteur de document public.
- Les amendements, **une fois déposés**, avec leur exposé sommaire et leurs
  sources.

**Ce qui ne traverse jamais.** Le manuscrit et ses notes. Le `REF_doctrine`, le
référentiel des positions, les apports et les justifications. Le registre, le
journal, l'état du chantier, le fil courant. Les protos et les archives. La
stratégie réseaux et le vocabulaire qu'elle arrête. Et **les deux classeurs de
l'auteur** — `Synthèse Calculs` et `Synthèse ETP et agences` : ils portent le
chiffrage et les traitements, c'est-à-dire notre interprétation. Le projet ouvert
reçoit le PLF ; notre lecture du PLF n'y arrive que sous forme d'amendement.

**Une règle de temps, et elle est la plus importante.** *Rien ne traverse avant
d'être déposé ou publié.* Le recensement des mesures candidates et l'ordre de
dépôt sont de la stratégie parlementaire : les exposer d'avance les offre à qui
voudrait les préempter.

*Conséquence d'appareil, à la charge de Claude* : l'index prend un champ
`public`, `coffre.py` plie une **seconde archive réduite**, et `make coffre`
relève les empreintes des deux. Une unité de travail, à ouvrir quand le premier
amendement est prêt et non avant — un projet ouvert vide est une promesse en
défaut, comme A-59 le pose pour le site.

*Question à l'auteur* : **le gabarit de l'exposé sommaire ne traverse pas de
lui-même.** Il digère un document interne de Génération Libre ; le publier en
libre accès n'est pas à nous de le décider.

### A-135 — Le format des gagnants-perdants s'éprouve avant de s'écrire

Constaté au référentiel, tranché par Claude au titre de A-23, sur réserve de
l'auteur sur le format cible — accessible et visuel, non philosophique.

Écrire 367 textes courts dans un registre que le format cible refusera, c'est les
écrire deux fois. **Le format se prototype avant la production**, et le
prototypage ne coûte presque rien parce que la matière d'une fiche complète
existe déjà.

`C-04` **le travailleur** porte 12 gains et **12 apports sur 12** : c'est la seule
catégorie entièrement rédigée du référentiel, et le fil courant la désigne déjà
comme référence de registre. Elle ne demande aucune écriture.

`C-04` ne porte aucune perte. Le prototype prend donc une seconde catégorie pour
éprouver le côté perte, et la plus dure est la bonne : `C-30` **l'agent d'une
structure fermée**, 4 gains et 3 pertes, dont la justification, le relais et la
raccroche sont écrits. C'est le cas où « il n'y a pas de perdant ultime » (A-131)
doit tenir visuellement, ou pas.

**Coût du prototype : quatre apports.** Un pour cent du volume total.

*Conséquence sur l'estimation* : les neuf unités d'écriture ne valent qu'une fois
le format arrêté. La médiane de 18 mots par apport est celle d'un registre écrit ;
un format visuel peut demander un chiffre et six mots, ou une phrase et un
repère. **Le coût se ré-estime après le prototype, pas avant.**

---

## 20260827 — L'auteur tranche : la doctrine sur les opérateurs, et le perdant ponctuel

### A-130 — Sur les opérateurs, c'est notre décompte qui sort

**Arbitré par l'auteur.** Les comptes d'agences et d'opérateurs bougent tous les
ans et portent plusieurs variantes selon qui recense. **On cite notre doctrine**,
et on la cite partout de la même façon.

Ce qui vaut donc : 1 104 agences d'État, somme de quatre familles — 434
opérateurs du PLF, 328 organismes hors PLF, 24 autorités indépendantes, 318
commissions —, et 23 264 agences locales. Le décompte est vérifié par
`controle_socle.py`, six lignes de synthèse sur six.

**Ce que A-129 garde de valable, et qui ne dépend d'aucune source externe** : le
1 104 **contient** les 434 et les 318. Les citer côte à côte comme trois
populations distinctes compterait deux fois les mêmes structures. La règle
d'emploi est donc : **on sort le total, ou on sort la ventilation, jamais les
deux en enfilade.**

*Écarté* : aligner le corpus sur le décompte cité par le document GL, et
l'instruction du « 12 000 » de son exemple, qui ne nous engage pas.

### A-131 — Il n'y a pas de perdant ultime, seulement des perdants ponctuels

**Arbitré par l'auteur, et c'est la définition qui manquait.**

Une perte est **ponctuelle**. Elle se raccroche toujours : à un gain collectif, à
une alternative, au fait que tout peut être maintenu si les gens le veulent, à
des clients plus riches, à un travail qui paie mieux, à une économie qui va
mieux. **Personne ne perd au bout de la chaîne.**

Et **le gagnant varie selon le sujet** : en général le travailleur, parfois le
ménage, le citoyen, l'enfant.

*Trois conséquences de dérivation, tirées par Claude et non énoncées par
l'auteur.*

**La maille de restitution n'est pas une, elle est déclarée ligne à ligne.** Le
référentiel la porte déjà : 56 catégories, 8 groupes, une catégorie par ligne. La
question « individu type, ménage type ou catégorie » n'a pas de réponse globale —
elle a la réponse que le sujet impose, et le référentiel l'écrit déjà.

**Le troisième sens de « perdant » disparaît.** Perdant relatif au statu quo
supposait une projection à droit constant que le corpus ne porte nulle part. Une
perte ponctuelle se dit dans le temps du plan, pas contre un contrefactuel.

**Le produit n'est pas un bilan à colonne de perdants nets.** Il restitue par
sujet : qui gagne, à quel titre, et ce que la perte ponctuelle vaut avec sa
raccroche. Le référentiel est déjà bâti ainsi — **49 perdants sur 49 portent leur
justification et leur raccroche**, 47 sur 49 leur relais.

*Rend caduc* : les questions 2 et 3 du fil courant, et la partie de A-125 qui
laissait la définition ouverte.

### A-132 — La jonction position ↔ incidence est un contrôle, non une alimentation

Constaté au référentiel, pas rapporté. **Les 194 gains portent tous déjà une
grandeur dérivée** — 180 nommées, 11 indiquées, 3 déduites. Aucun n'attend un
chiffre du chiffrage.

L'incidence par population — ménages −18,9, actifs −10,15, entreprises
−17,75 Md€ — n'est donc pas une matière à ventiler sur 56 catégories : c'est
**l'incidence de la restitution par population**, et elle boucle déjà sur les
trois totaux de tête.

La table écrite à la main de A-125 reste, mais son objet change : elle **vérifie**
qu'une grandeur affichée sur une ligne de position concorde avec ce que le
chiffrage porte, à la maille où les deux existent. Elle n'invente aucun chiffre
et elle n'en descend aucun.

*Amende A-125* pour l'objet. La forme — table écrite, maille déclarée, écart
publié — est intacte.

### A-133 — Le contre-PLF n'ouvre pas un second projet Claude

Tranché par Claude au titre de A-23, sur question de l'auteur.

Un second projet devrait porter l'archive technique, les référentiels et les cinq
classeurs pour que `make` tourne. Ce serait **une seconde copie du corpus**,
donc un second point de vérité, donc exactement ce que A-124 interdit — et deux
versements à tenir à chaque clôture.

Ce que le contre-PLF ajoute au coffre est mesuré et faible : le recensement des
mesures candidates est un dérivé du socle et ne se verse pas (A-71) ; ce qui se
verse est le texte des amendements, écrit à la main, de l'ordre de 3 ko pièce.
Trente amendements pèsent une centaine de kilo-octets dans une archive qui en
fait 1 238.

**Le découpage se fait par conversation, pas par projet** — c'est déjà la règle,
et la limite de contexte est par conversation.

*La seule raison qui justifierait un second projet est une question d'accès, non
d'espace* : si le contre-PLF devait être travaillé par un tiers à qui le
manuscrit ne se montre pas. Cela ne s'est pas présenté.

*Si la jauge bloquait un versement*, la réponse n'est pas un second projet, c'est
A-6 : sortir les protos gelés les plus lourds, 208 ko disponibles sur trois
documents, sur décision de l'auteur.

---

## 20260827 — La session d'organisation : trois chantiers, une règle de propagation

### A-121 — Une empreinte en retard n'est pas un faux, et la preuve est mécanique

`make restauration` sort un `R1` sur `methode/feuille_de_route.md` : 11 345 o et
246 lignes attendus, 12 505 o et 265 lignes au dépôt.

Ce n'est pas un faux. Deux fils auxiliaires distincts ont redemandé le document
au coffre, et les deux lectures portent la même empreinte,
`f532df669f9bcd08`, identique à l'octet au fichier du dépôt. La chaîne coffre →
transcript → `restaurer.py` est une copie d'octets : aucun modèle n'y intervient.
**C'est donc `methode/empreintes.json` qui est en retard sur ce seul artefact.**

Cause de fond, déjà nommée en A-72 : un versement au coffre sans `make coffre`
derrière laisse les empreintes en arrière. Le fichier du dépôt n'est pas touché,
l'empreinte n'est pas relevée à la main ; elle se relève à la clôture.

**Règle de conduite qui en sort** : devant un `R1`, la preuve n'est ni la taille
ni l'allure du contenu, c'est **une seconde lecture indépendante du coffre**. Si
les deux lectures concordent, le coffre est ce qu'il est et l'empreinte a
retardé. Si elles divergent, `restaurer.py` s'arrête de lui-même.

### A-122 — Le document GL se déclare là où il est, et le chantier entre par sa digestion

`Exposé des motifs - rédaction GL.docx` a été versé le 20260827 à la racine du
coffre, sous un nom qui n'est pas canonique. **Il ne se déplace pas** : c'est un
docx, le coffre le porte comme document et non comme octets, et le recomposer
par le modèle fabriquerait un faux binaire (A-27).

Il est donc déclaré à l'index sous `sources/Expose_des_motifs_redaction_GL.docx`,
`restaurable: false`, famille *références externes*, avec son chemin de coffre
tel quel. Et il entre au corpus par sa digestion, comme toute référence externe
(A-14) : `sources/gabarit_expose_sommaire.md`, qui porte l'en-tête à quatre
éléments, les trois temps de l'exposé sommaire, la contrainte de 200 à 300 mots,
la règle de source entre parenthèses, et les deux points où le document GL et le
corpus divergent.

Le prompt d'ouverture de cette session, versé par l'auteur sous
`livrables/prompt_session_organisation.md`, est un markdown : il se range, lui,
et passe en `methode/`. Il est déclaré sous
`sources/prompt_session_organisation_20260827.md`.

### A-123 — Le site est un dérivé, et Vercel déploie la sortie de `make`

La question posée — fichier HTML autonome, ou base autonome qui diverge — n'était
pas ouverte : **une base autonome viole le point de vérité**, et un dérivé se
régénère sans jamais se corriger à la main. Une seule forme reste.

`make` produit `livrables/donnees.json` puis les pages ; Vercel déploie cette
sortie et n'écrit rien. Aucune donnée ne se saisit dans le site, aucune
correction ne s'y fait : elle remonte à l'étage où elle est née, puis on rejoue.

*Coût assumé* : chaque publication est un déploiement, une correction de fond est
une régénération complète. *Ce que cela évite* : trois semaines de dérive
silencieuse entre le site et le corpus.

**Ce qui reste à l'auteur** : le périmètre — vitrine seule au sens de A-60, ou
vitrine plus l'outil « ce que le plan change pour moi » — et ce qui est public.

### A-124 — La règle de propagation s'écrit une fois pour les trois chantiers

Trois chantiers qui se serviraient chacun dans le corpus à leur manière
divergeraient en trois semaines. La règle est unique et elle est déjà celle de la
ligne de production ; elle est écrite une fois, à `methode/carte_des_chantiers.md`.

Aucun produit ne porte un chiffre ou un énoncé qui ne soit pas au référentiel.
Aucun produit ne se corrige en aval. Chaque produit déclare ses entrées à
`methode/index.json`, et `controle_index.py` refuse un artefact que rien ne
déclare.

Trois adresses, une par nature de chiffre : `REF_chiffres.json` pour les faits,
`economies.json` pour le chiffrage des économies, `socle_budgetaire.json` pour ce
que le PLF publie. Un produit qui irait chercher ailleurs se voit à l'index.

### A-125 — La jonction position ↔ incidence s'écrit à la main, avec sa maille

Les positions portent 56 catégories, l'incidence trois populations — ménages,
actifs, entreprises. **Les deux mailles ne se superposent pas**, et un
rapprochement ne se devine jamais d'une ressemblance (A-35, A-94).

La jonction prend la forme déjà éprouvée deux fois — `MEME_QUE` pour les faits,
les douze lignes d'opérateur pour les économies : une table écrite à la main, une
entrée par ligne d'incidence, qui nomme les catégories qu'elle atteint, déclare
sa maille, et publie l'écart quand la recomposition ne tombe pas. **L'écart ne
s'absorbe jamais** (A-105).

*Écarté* : ventiler 18,9 Md€ sur 56 catégories au prorata d'un effectif. Ce
serait fabriquer un chiffre.

**Ce qui reste à l'auteur** : la définition de perdant et la maille de
restitution. Constat de dérivation, porté au fil courant : le perdant en flux la
première année et le perdant à terme sont l'un et l'autre instrumentés — A-98 et
l'onglet `Perdants` les portent ; **le perdant relatif au statu quo ne l'est
pas**, il suppose une projection à droit constant que le corpus ne porte nulle
part.

### A-126 — Le recensement des amendements part de la ligne budgétaire, pas du nœud

**Un nœud D ne devient pas un amendement.** Un amendement s'accroche à un article
ou à une ligne du texte en discussion ; la doctrine dit ce qu'on veut, le PLF dit
où l'écrire.

Le point d'entrée du recensement est donc la ligne budgétaire : les 128
programmes porteurs d'un traitement (A-117), les 41 lignes d'économie tracées,
les 465 dépenses fiscales avec leur fiabilité déclarée (A-100), les 278 taxes
affectées. Chaque candidat part d'une ligne qui porte déjà son montant, sa source
et sa place dans la nomenclature ; le rattachement doctrinal s'écrit ensuite.

*Écarté* : partir des 56 propositions et chercher où les poser — c'est-à-dire
écrire d'abord et chercher l'article ensuite.

### A-127 — Un jeu de règles de sortie par registre

Le vocabulaire arrêté par la stratégie réseaux et porté à `controle_sortie.py`
(A-53) est fait pour un post, pas pour la séance. Appliqué tel quel à un exposé
sommaire rédigé en français parlementaire, **il le sortirait en faute**.

`controle_sortie.py` prend donc un jeu de règles par registre au lieu d'un jeu
unique. L'outil est de la tambouille ; **le registre de l'amendement est une
question de fond** et il revient à l'auteur, avec la proportion du constat, où le
document GL et A-53 divergent d'une cinquantaine de mots sur 250.

### A-128 — La jauge du coffre ne se calcule pas depuis le dépôt

Mesure au dépôt : l'archive technique fait 1,236 Mo, ce qui concorde avec les
1,24 annoncés ; les 45 documents lisibles du coffre font 1,656 Mo de texte brut,
soit davantage que la place que le compteur du projet laisse. **La jauge ne
compte donc pas des octets bruts**, et la marge se lit là où elle s'affiche, pas
ici.

Ce que la règle impose déjà suffit à tenir : un dérivé qui se régénère à
l'identique ne se verse pas (A-71). Le site, les fiches, le classeur de synthèse
et les vues internes ne vont pas au coffre. Ce qui y va est ce qui ne se refait
pas, et cela vit dans l'archive technique, qui le compresse.

**Ce qui reste à l'auteur** : la sortie éventuelle des protos gelés les plus
lourds — `Reserve_arguments` 92 ko, `Note_entreprises` 63 ko,
`Presentation_20260731_v44` 53 ko. A-6 tient : une gelée que rien ne sait refaire
ne se supprime pas.

### A-129 — Ce que compte notre 1 104, et ce que compte le 103 du document GL

Instruit, non arbitré. Notre 1 104 agences d'État est une **somme de quatre
familles**, vérifiée par `controle_socle.py` : 434 opérateurs du PLF, 328
organismes hors PLF, 24 autorités indépendantes, 318 commissions. Il **contient**
donc les 434 opérateurs et les 318 commissions : « 1 104 agences, 434
opérateurs » compterait deux fois les mêmes structures.

La synthèse de la commission d'enquête du Sénat de juillet 2025, que la pièce Vie
Publique citée par le document GL relaie, donne 434 opérateurs, 317 organismes
consultatifs listés au jaune budgétaire, et 1 153 organismes publics nationaux
recensés par la direction du budget. **Elle mentionne 103 comme un décompte du
Conseil d'État de 2012**, opposé aux 1 244 de l'Inspection générale des finances
la même année.

Deux conséquences. Nos 318 commissions et les 317 organismes consultatifs sont le
même objet à une unité près. Et le « 12 000 organismes publics nationaux » de
l'exemple GL ne se retrouve pas dans la synthèse du Sénat, qui écrit 1 153 : **à
vérifier sur la pièce Vie Publique elle-même**, que la session n'a pas pu ouvrir.
Si l'écart se confirme, il porte sur un facteur dix, et il est dans l'exemple qui
sert de modèle.

**Le chiffre à citer se tranche par l'auteur.**

---

## 20260827 — La couche budgétaire formalisée : titres, traitements, qualifications

### A-115 — La nomenclature s'écrit une fois, et tout s'y réfère

`appareil/nomenclature_lolf.py` porte quatre tables et ne calcule rien : les
sept **titres** de l'article 5 de la LOLF, les dix **catégories** que le
classeur budgétaire retient, les sept **traitements** que l'auteur applique, et
les huit **qualifications** de montant avec leur unité.

Elle est écrite à la main, avec les libellés officiels à côté des mots du
classeur. Les deux se disent : le mot du classeur est ce qu'on lira dans une
cellule, le libellé officiel est ce qui fait foi.

**Pourquoi c'est une pièce et non un commentaire** : sans elle, la lecture du
classeur reposait sur des colonnes repérées à la main dans quinze cellules. Avec
elle, le lecteur du budget général se dérive de la table, et un PLF neuf se lit
sans rien retoucher.

### A-116 — Un montant sans qualification n'est pas un chiffre

34 096 M€ en catégorie 32 ne veut rien dire tant qu'on ne dit pas si c'est une
enveloppe portée au PLF, une part supprimable dès l'année 1, ou une économie
déjà restituée. Les trois vivent dans les mêmes cellules du même onglet, et rien
ne les distingue qu'un mot en colonne de gauche.

Huit qualifications, chacune avec son unité et **ce avec quoi elle se somme** :

| qualification | unité | se somme avec |
|---|---|---|
| crédit porté au PLF | M€ | les autres crédits |
| part supprimable dès l'année 1 | M€ | les autres parts supprimables |
| assiette d'un poste nommé | M€ | **rien** |
| économie restituée en année 1 | M€ | les autres économies d'année 1 |
| économie restituée ensuite | M€ | les autres économies pérennes |
| effectif | ETP | les autres effectifs |
| paramètre de calcul | € | **rien** |
| non qualifié | — | **rien** |

Une assiette additionnée à son économie double le chiffrage. La table l'interdit
au lieu de le déconseiller.

**Correction que cette règle a produite** : les postes « sur culture », « sur
FrComp. », « sur ville » et « MPR (Anah) » étaient rangés en assiette par une
règle de préfixe. Ce sont des **économies**. Le préfixe « sur » quitte la règle
mécanique et ces quatre postes sont écrits à la main, vérifiés un par un contre
l'arbre des économies. Un préfixe qui se trompe une fois se trompera au
millésime suivant.

### A-117 — Le traitement est la couche de décision, et elle se prouve

Chaque programme porte, pour chacune des cinq catégories de transfert, un mot :
**Oui**, **En 3 ans**, **Fusion CI**, **Bourse**, **Sécu**, **Flux OM**, ou
rien. Un septième, **X**, marque le programme comme régalien. Sept valeurs, pas
une de plus — le contrôle sort en échec tout mot absent de la table.

Ce mot dit si le crédit est supprimé, reporté, ou seulement déplacé. **Fusion CI
et Bourse ne sont pas des économies** : le crédit change de véhicule. **Sécu**
non plus : la dépense quitte l'État sans quitter la dépense publique. Les
compter en économie gonflerait le chiffrage de ce qui n'a fait que bouger.

La lecture se prouve : la part supprimable dès l'année 1 affichée en tête se
retrouve **exactement**, catégorie par catégorie, en sommant les crédits des
programmes marqués « Oui ». 6 728,42 · 21 827,40 · 7 761,51 · 13 543,42 M€,
quatre sur quatre.

### A-118 — La part budgétaire n'est plus un résidu : elle est écrite

Jusqu'ici, la part budgétaire d'une économie se déduisait par soustraction — la
ligne du chiffrage moins ce que les taxes recomposent. **Un résidu n'est pas une
source.**

L'onglet de synthèse du classeur des dépenses l'écrit, poste par poste, avec sa
catégorie et sa qualification. Les cinq lignes qui en dépendaient se ferment :

| ligne | taxes | crédits écrits | total | classeur |
|---|---|---|---|---|
| France Compétences | 10,125 | 0,434 (cat. 32) | 10,559 | 10,6 |
| France Travail | — | 2,734 (cat. 32, T2 et T6) | 2,734 | 2,7 |
| CNC et subventions culturelles | 0,705 | 0,517 (cat. 32) | 1,222 | 1,3 |
| ADEME | — | 0,921 (cat. 32) | 0,921 | 0,9 |
| MaPrimeRénov' | — | 1,333 (cat. 61) | 1,333 | 1,3 |

**Trente-deux bouclages sur trente-deux.** Plus une seule ligne du chiffrage
dont l'origine se devine.

### A-119 — La couverture de la couche de décision se dit, elle ne se suppose pas

Les 128 programmes qui portent un traitement ne sont pas tous les programmes du
PLF. Trente-quatre lui échappent, et le contrôle les nomme avec leur montant
plutôt que de laisser croire à une couverture totale.

Ce qui échappe se répartit ainsi : **141 Md€ de remboursements et dégrèvements**
(programmes 200 et 201), crédits évaluatifs qui ne sont pas une dépense de
politique publique et sortent du périmètre par nature ; **1,15 Md€ de comptes
d'affectation spéciale** ; et **273 M€ sur deux programmes ordinaires** — le
fonds de soutien aux emprunts toxiques et le programme Épargne.

Le programme 368, « Conduite et pilotage de la transformation et de la fonction
publiques », manque au bloc de détail alors que sa ligne de mission le compte :
52,9 M€ de titre 2 sont dans l'agrégat sans être dans le détail. L'agrégat n'est
pas faux, le détail est incomplet, et le contrôle le sort case par case.

### A-120 — Une cellule que le classeur laisse en erreur se recompose sans se corriger

La part supprimable de la catégorie 62 est un `#VALUE!` au classeur. Le contrôle
la recompose depuis les traitements — **15 282,13 M€** — et l'affiche en le
disant, sans la comparer à rien et sans toucher au classeur.

Recomposer n'est pas corriger. L'auteur garde sa source ; ce qui est produit
ici est une lecture qui, sur ce point, va plus loin que ce que la source affiche.

---

## 20260827 — Quatre tranchages de l'auteur sur le traçage des économies

### A-111 — La base d'ETP vient du jaune, et l'écart est un écart de concept

Les bases d'emplois du chiffrage — 46 440 hors France Travail, 53 200 pour
France Travail — ne viennent pas de l'annexe des opérateurs mais du **jaune
budgétaire « Opérateurs de l'État »**. Les deux ne comptent pas la même chose :
plafond d'emplois d'un côté, exécution de l'autre.

L'écart de 393 ETP (0,8 %) et de 148 ETP (0,3 %) est donc **documenté et clos**.
Il ne se corrige d'aucun côté et ne se réduit pas en remontant une tolérance : il
se nomme.

Le contrôle distingue désormais trois verdicts de dérivation — accord, écart de
concept, écart ouvert. **Seul le troisième reste sous les yeux.**

**Rend caduc** : A-108, qui laissait ces deux dérivations ouvertes.

**Conséquence pour le rejeu** : la bascule sur un PLF neuf devra reprendre le
jaune, non l'annexe, pour ces deux bases. Le jaune est un PDF : la règle du
chiffre qui porte sa page s'applique.

### A-112 — MaPrimeRénov' se rattache à l'ANAH, qui le distribue

MaPrimeRénov' est un dispositif et non un organisme, mais **il est distribué par
l'ANAH**. Le rattachement est écrit à la main, sur décision de l'auteur : la
ligne rejoint l'opérateur porteur.

**L'ANAH porte donc deux lignes d'économie** — 0,4 Md€ de restitution de sa taxe
affectée, 1,3 Md€ de crédits MaPrimeRénov' —, soit 1,7 Md€. La réconciliation
tient une liste par opérateur et non une seule ligne : une clé qui écraserait la
précédente perdrait un milliard.

L'assiette est reprise en conséquence : programmes 174 et 135, 2,92 Md€
d'enveloppe, et elle couvre désormais la ligne. Le champ `dispositif` reste posé,
pour que la ligne ne se lise pas comme une économie d'organisme.

**Rend caduc** : la maille `dispositif` de A-104, qui n'a plus d'occurrence.

### A-113 — Une source hors corpus validée par l'auteur cesse d'être une réserve

Les budgets initiaux 2025 de France Compétences, France Travail et l'ADEME
portent 14,2 Md€ de chiffrage et ne sont pas au corpus. **L'auteur les a sourcés
ailleurs et valide le chiffrage.**

Le signalement reste sur les trois lignes, parce qu'il dit d'où vient le montant
et qu'un lecteur doit pouvoir le retrouver. Il ne vaut plus réserve : il n'est
plus marqué d'un avertissement, et il renvoie ici.

La distinction à tenir : **une pièce absente qu'on n'a pas cherchée** est un trou
et se signale comme tel ; **une pièce absente du corpus mais sourcée ailleurs**
est un renvoi et se signale comme tel. Confondre les deux fait passer un
chiffrage validé pour un chiffrage douteux.

### A-114 — Un affectataire hors liste des opérateurs se rattache aux ODAC-ODAL

« Hors liste des opérateurs » n'est pas une maille : c'est un constat de manque.
Les trois lignes qui en relevaient se rattachent toutes à la liste ODAC-ODAL, et
elles y portent un régime.

| ligne d'économie | ODAC | entités | régime |
|---|---|---|---|
| Action Logement | ODAC-223 · ALS Action logement services | 1 | vente |
| CCI et chambres d'agriculture | ODAC-730 · Chambres consulaires | 273 | vente |
| Établissements publics fonciers | ODAC-731 · Établissements publics fonciers | 40 | vente |

La maille `affectataire_hors_plf` disparaît au profit de `odac_odal`. Il en reste
trois : opérateur du PLF, ODAC-ODAL, résidu.

**Deux mailles subsistent dans chaque ligne, et elles se déclarent.** L'annexe
des taxes nomme des affectataires — deux collecteurs consulaires, 34
établissements fonciers ; l'ODAC compte des structures — 273 chambres, 40
établissements. Ce ne sont pas les mêmes objets, et le rattachement publie les
deux comptes plutôt que d'en choisir un. Six établissements fonciers n'ont pas de
taxe affectée au PLF 2026, et cela se lit.

**Portée générale** : ce que l'auteur énonce vaut au-delà de ces trois lignes.
Les 145 affectataires de taxe qui ne sont pas opérateurs du PLF sont rattachables
de la même façon. C'est le travail des 269 appariements, désormais orienté : la
cible n'est pas seulement la liste des opérateurs, c'est **la liste des opérateurs
ou celle des ODAC-ODAL**.

---

## 20260827 — L'assiette des économies, les mailles du chiffrage

### A-103 — Le classeur de calculs n'a pas de socle : il porte `classeur` et `lecture`

Les classeurs du PLF se lisent en deux couches, ce que l'administration publie et
ce que l'auteur ajoute en colonnes. Le classeur de calculs n'a pas cette
structure : il est de l'auteur de bout en bout, et prétendre y séparer un socle
d'une interprétation serait inventer une autorité que le document n'a pas.

Ses entrées portent donc `classeur` — ce que la cellule dit, mot pour mot — et
`lecture` — la place que le module lui reconnaît dans l'arbre. Rien entre les
deux.

**Rend caduc** : rien. **Prolonge** A-70 sur les deux couches, en nommant le cas
où elles ne s'appliquent pas.

### A-104 — Une ligne d'économie n'est pas une ligne d'opérateur

Les douze lignes de la rubrique « Opérateurs » du chiffrage relèvent de trois
mailles distinctes. Sept nomment un opérateur de la liste officielle. Trois
nomment un affectataire de taxe qui n'y figure pas — Action Logement Services,
CCI France et les chambres d'agriculture, les trente-quatre établissements
publics fonciers. Une nomme un dispositif budgétaire qui n'est pas un organisme,
MaPrimeRénov'. La dernière est un résidu que le classeur ne détaille pas.

Chaque ligne rattachée déclare sa maille. Les confondre ferait croire que la
liste officielle des cent quatre-vingts opérateurs couvre le chiffrage : elle ne
le couvre pas, et **une part des économies se prend hors du périmètre des
opérateurs**.

**Rend caduc** : l'idée, implicite dans la réconciliation, qu'une économie
d'opérateur se rattache toujours à un opérateur.

### A-105 — L'écart entre la ligne et ce que les taxes recomposent ne s'absorbe jamais

Quand une ligne d'économie se recompose depuis les taxes affectées de son
assiette, l'écart avec ce que le classeur affiche relève de trois cas, et de
trois seulement.

Il tient dans l'arrondi d'affichage du classeur — cinq centièmes de milliard,
puisque chacune des deux colonnes est arrondie au dixième — et il se nomme
arrondi. Il est positif au-delà, et c'est une **part budgétaire** : une économie
prise sur des crédits, dont le programme se nomme sans que la part s'en déduise.
Il est négatif au-delà, et c'est un défaut de lecture, qui se dit comme tel.

Aucun de ces écarts ne se réduit en ajustant une tolérance. Une tolérance ne se
remonte jamais pour faire tomber un compte.

### A-106 — L'assiette budgétaire se nomme, le montant ne s'en déduit pas

Pour une économie prise sur des crédits, le projet annuel de performance donne
l'enveloppe du programme — subvention pour charges de service public et titre 6.
Il ne dit pas quelle part l'auteur y taille. Le rattachement nomme donc le ou les
programmes, publie leur enveloppe, et **s'arrête là**. Déduire la part de
l'enveloppe serait fabriquer un chiffre.

Quand l'enveloppe des programmes cités ne couvre même pas la part budgétaire, la
ligne le dit : l'assiette déborde ce qui est nommé. C'est le cas de
MaPrimeRénov', et il reste ouvert.

### A-107 — Une source hors corpus se signale sur la ligne qu'elle porte

L'onglet de la grande synthèse cite, pour France Compétences, France Travail et
l'ADEME, le budget initial 2025 de l'organisme. **Cette pièce n'est pas au
corpus.** Le montant ne se vérifie donc pas ici, et les trois lignes concernées
le portent écrit.

Signaler la pièce absente vaut mieux que la reconstituer : une reconstitution
plausible aurait l'apparence d'un bouclage.

### A-108 — Un écart de dérivation reste ouvert, il ne se corrige pas

La chaîne des emplois se rejoue depuis la synthèse du budget général. Cinq
dérivations sur sept retrouvent ce que le classeur écrit. Deux ne le retrouvent
pas : la base d'ETP retenue pour les opérateurs n'est pas celle du PLF 2026.

Ces deux-là ne sont pas des échecs de bouclage, et elles ne se corrigent ni d'un
côté ni de l'autre. Elles disent que la base de l'auteur vient d'ailleurs — d'un
exercice antérieur, ou d'un périmètre différent — et elles restent affichées
jusqu'à ce que l'auteur tranche.

### A-109 — Un rattachement par règle déclare le compte qu'il attend

Trente-quatre établissements publics fonciers ne s'écrivent pas un par un sans
que la liste devienne illisible. Le rattachement les désigne par une règle — le
libellé contient « foncier » — et **déclare à la main le nombre de lignes de taxe
attendu**. Si un affectataire apparaît ou disparaît au PLF suivant, le compte ne
tient plus et le contrôle le sort en échec.

La règle sans le compte attendu serait une heuristique silencieuse. Avec lui,
c'est un rattachement vérifiable.

### A-110 — Le journal se tient dans l'ordre qu'il déclare

Le journal dit « le plus récent en tête » et ne l'était plus : un bloc de quatre
entrées du 25 précédait deux entrées du 27. Les blocs sont remis en ordre par
date décroissante, sans qu'aucun soit réécrit — le tri porte sur des blocs
entiers, découpés sur leurs séparateurs.

Un document qui ment sur son propre ordre de lecture se lit de travers à chaque
ouverture de session.

---

## 20260827 — Le gage CSG, les mailles, la couverture complète

### A-98 — En budgétaire, gage et solde sont deux temps d'une même restitution

**Arbitré par l'auteur, et c'est une correction de lecture, non de forme.** Le
« gage CSG » d'une ligne budgétaire est ce qui est **restituable dès l'année 1** ;
le « solde » est ce qui est **restitué ensuite**. **La vraie économie valorisable
restituée est leur total.**

Les champs se renomment en conséquence : `restitue_annee_1`,
`restitue_ensuite`, `economie_restituee_totale`. « Gage » et « économie en sus »
laissaient croire à deux natures différentes.

**La règle ne vaut pas en dépense fiscale** : là, le gage net et l'effet
macroéconomique sont deux grandeurs distinctes, et elles ne s'additionnent pas.
Employer le même mot pour les deux mondes était l'erreur.

### A-99 — Une feuille latérale n'est pas une source à part : elle enrichit la même entrée

Tranché par Claude au titre de A-23. Les huit feuilles de l'annexe des dépenses
fiscales portent toutes le **numéro de dépense fiscale**. Les importer comme huit
tables séparées aurait créé huit référentiels à recroiser ; elles enrichissent
le bloc `socle` d'une seule entrée.

*Conséquence* : la fiabilité déclarée du chiffrage, l'article du code, le
programme porteur et les échéances deviennent des attributs de la dépense, et se
lisent partout où elle se lit.

### A-100 — La fiabilité déclarée qualifie tout chiffre repris

Tranché par Claude au titre de A-23. L'administration déclare, pour chaque
dépense fiscale, la fiabilité de son propre chiffrage — « Très bonne »,
« Bonne », « Ordre de grandeur » — et la méthode. **Un gage bâti sur un ordre de
grandeur ne vaut pas un gage bâti sur une simulation.**

Le classeur de synthèse le compte par ligne. C'est la matière d'une objection
qu'on nous fera, et il vaut mieux l'avoir comptée avant.

### A-101 — Réconcilier n'autorise pas à confondre les mailles

Tranché par Claude au titre de A-23, sur demande de réconciliation
statut/ETP/TA/SCSP/T6 de l'auteur.

Statut, emplois et taxes affectées se rapportent à **l'opérateur**. La
subvention pour charges de service public et les transferts de titre 6 se
rapportent au **programme** : le projet annuel de performance ne nomme jamais
l'opérateur. Trente programmes sur cinquante-quatre en portent plusieurs.

**Le tableau les met côte à côte et refuse de les totaliser.** Une colonne
« maille » dit, ligne par ligne, si la subvention est imputable à l'opérateur ou
partagée. Les additionner produirait un tableau qui paraît complet et qui compte
plusieurs fois la même subvention — c'est-à-dire exactement le défaut qu'une
réconciliation est censée empêcher.

*Deux manques assumés et affichés* : le statut n'est connu que pour 23
opérateurs, et la subvention n'est à la maille de l'opérateur que dans 24 cas.

### A-102 — Un libellé cassé se répare par la nomenclature, jamais à la main

Tranché par Claude au titre de A-23. Les libellés de mission et de programme de
l'onglet Opérateurs sont des formules, que la conversion rend en `#NAME?`.
L'annexe État porte les mêmes en clair, indexés par numéro de programme : c'est
elle qui répare, et la réparation est totale — 180 sur 180.

Une saisie à la main aurait été plus rapide et n'aurait pas survécu au millésime
suivant.

---

## 20260827 — Les opérateurs, la couverture, le classeur de synthèse

### A-93 — La liste officielle des opérateurs est l'onglet « Opérateurs »

**Arbitré par l'auteur.** Faute d'identifiant numérique, c'est le classeur ETP
et agences qui dit qui existe. Tous les autres fichiers s'y rattachent par le
libellé, et **c'est au chantier de tracer le même opérateur d'un fichier à
l'autre**.

### A-94 — Un opérateur ne s'apparie jamais sur un score

Tranché par Claude au titre de A-23, en application directe de A-35. Cinq passes
mécaniques sûres — nom normalisé, sigle avant tiret, forme longue, forme longue
sans tiret, sigle en tête confirmé par sa forme longue. Ce qu'aucune n'attrape
sort en **candidat**, avec son meilleur voisin et son score, et se tranche à la
main dans `ECRITS`.

La raison est démontrable : le meilleur voisin de « Communes » est « Ordre de la
Libération - Conseil National des communes », score 1,00, et c'est faux. **C'est
justement quand deux libellés sont proches qu'on se trompe.**

*Corollaire* : `ECARTES` porte le miroir, les libellés que la mécanique
rapprocherait à tort, chacun avec sa raison.

### A-95 — Le taux de rappel se mesure contre une vérité déclarée

Tranché par Claude au titre de A-23. L'onglet ODAC-ODAL porte une colonne
« Opérateur déjà traité » : c'est la réponse du classeur, et l'appariement doit
la retrouver, non la remplacer. Le rapport affiche donc un **taux de rappel** —
28 % au 20260827, 107 retrouvés sur 376 déclarés.

Un appariement qui ne sait pas se mesurer est un appariement qu'on croit sur
parole.

### A-96 — La couverture est un état, jamais une déclaration

Tranché par Claude au titre de A-23, sur question de l'auteur — « tous les
classeurs sont-ils digérés ? ». Trois états, et un seul se déclare sans preuve :

- **importé** — les lignes de la feuille sont au socle et se recomposent ;
- **lu** — sa structure et ses agrégats ont été ouverts et consignés ;
- **non lu** — personne ne l'a ouverte.

Au 20260827 : 8, 14 et 27 sur 49 feuilles. **Le troisième chiffre est celui qui
compte**, et il se dit en tête du classeur de synthèse plutôt qu'au fond d'une
note.

### A-97 — Le classeur de synthèse est un dérivé, et il porte ses formules

Tranché par Claude au titre de A-23, sur demande de l'auteur. Il se régénère par
`generer_classeur_synthese.py`, il ne s'édite pas : une correction se porte à la
grille de lecture.

**Ses totaux sont des formules**, y compris les écarts de bouclage et le rejeu
des cinquante-sept opérations du corpus. Un classeur de synthèse dont les
chiffres sont figés ne prouve rien : celui-ci recalcule.

*Écarté* : un export à plat des référentiels, qui aurait été lisible et muet.

---

## 20260825 — La grille de lecture, et les hypothèses du livre

### A-87 — Les deux dispositifs coexistent : le classeur est officiel, la grille est prouvée

**Arbitré par l'auteur.** Les fichiers qu'il maîtrise restent la source
officielle du chiffrage. Le chantier n'en produit pas une version concurrente :
il en **formalise la lecture**, et cette lecture ne vaut que prouvée.

*Écarté* : que l'appareil devienne maître et régénère le classeur ; et que la
grille reste une intention sans bouclage.

**La preuve est le bouclage.** `controle_socle.py` recompose les agrégats depuis
les lignes et les compare à ce que le classeur affiche. Tant qu'un bouclage est
rouge, la grille est une hypothèse ; une divergence ne se corrige jamais au
socle, c'est la grille qu'on reprend.

### A-88 — Socle et interprétation ne se mélangent pas

Tranché par Claude au titre de A-23. Chaque ligne importée porte deux blocs
distincts. Le `socle` est ce que le document budgétaire publie ;
l'`interpretation` est ce que l'auteur y a ajouté — régime, taux, montants
dérivés.

C'est la séparation qui rend le rejeu possible : un montant qui change d'un
exercice à l'autre ne dit rien de la décision prise, et une décision prise ne
dépend pas du montant.

*Conséquence de forme* : rien ne se corrige à l'import. Une cellule vide reste
vide, une mention `ε` ou `nc` du PLF se garde telle quelle et **ne se lit jamais
comme zéro**.

### A-89 — Les identifiants budgétaires se gardent tels quels

**Arbitré par l'auteur** : les nomenclatures sont stables d'un exercice à
l'autre. Pas de table de correspondance. Numéro de dépense fiscale, SIREN de
l'affectataire, code de taxe, numéro de programme.

*Fragilité nommée* : l'opérateur n'a pas de clé numérique, et les agrégats du
classeur le filtrent sur son intitulé exact. Un libellé qui change au PLF
suivant casserait un total sans bruit. Les intitulés filtrants sont donc écrits
en clair au contrôle, où un changement les fait sortir en échec.

### A-90 — Une hypothèse n'est ni un fait ni un paramètre

Tranché par Claude au titre de A-23, sur reproche de l'auteur : les hypothèses
sur les grands paramètres sont au manuscrit, en littéraire, et le chantier ne
les avait pas relevées.

Une hypothèse est **ce sous quoi un fait vaut**. Elle a sa couche propre, seize
entrées, chacune avec sa nature, son sens — minorant, majorant, neutre —, son
domaine et les nœuds qu'elle commande.

La distinction porte : quand un PLF neuf arrive, ce sont les hypothèses qu'on
réexamine, et les faits se recalculent.

### A-91 — Une hypothèse porte un repère, jamais le verbatim

Tranché par Claude au titre de A-23, en application de A-21. Recopier le texte
du livre le ferait passer par le modèle. Chaque hypothèse porte donc un
**repère** — un fragment court — dont `controle_hypotheses.py` vérifie la
présence littérale au manuscrit.

Un repère qui ne se retrouve plus est une alerte, et elle ne se lève pas seule :
soit le livre a changé, soit la recopie a dérivé.

### A-92 — Le contrôle de l'index ne redouble plus le classement

Tranché par Claude au titre de A-23. `controle_index.py` portait sa propre liste
d'artefacts hors classement, quand A-25 pose que l'affectation vit dans
`generer_carte.py` et nulle part ailleurs. Le doublon sortait la feuille de
route en anomalie à chaque exécution. La liste se lit désormais à sa source.

Deux autres anomalies permanentes tombent : le prototype de site n'avait pas de
règle de génération, et l'archive technique sortait en fichier non déclaré alors
qu'elle est déclarée au bloc `archives` et non au bloc `artefacts`.

**`make controle` sort à zéro échec et zéro anomalie**, pour la première fois.

---

## 20260825 — Ce qui prime, et la couche budgétaire à construire

### A-85 — Le salaire médian est 2 190 €, la Suisse est à 4 300 € — à corriger à la régénération

**Arbitré par l'auteur.** Les deux valeurs du 1-pager sont fausses et se
corrigent en régénérant le produit, non en éditant l'archive :

- **2 190 €** de salaire médian net prime sur les 2 100 €, qui sont le revenu
  médian équivalent d'Eurostat et ne se disent pas « salaire » ;
- **4 300 €** pour la Suisse, note e8 du manuscrit, et non 5 500 € — chiffre qui
  au manuscrit désigne la dette publique nouvelle par foyer.

De même, la pension de base est de **1 100 €/mois** et non 1 000 (Q&A du
20260806).

**La veille continue de sortir ces alertes tant que les produits ne sont pas
régénérés.** C'est voulu : une alerte qui s'éteint sur un arbitrage sans que le
produit ait bougé laisserait sortir la faute.

### A-86 — La couche budgétaire du PLF est un chantier à structurer, pas une reprise du classeur

Constaté et proposé, **non validé**. Le classeur `Synthèse Calculs` porte
1 336 formules et **aucune référence externe** : le graphe de calcul est complet
à l'intérieur, et sa jonction avec les classeurs sectoriels du PLF est une
recopie à la main.

Les sectoriels, eux, portent déjà l'interprétation : l'onglet « Chiffrages IB »
des dépenses fiscales tient 465 lignes avec, par dépense, son numéro, son
montant, un taux d'économie nette, un taux d'effet macro, un régime de
suppression — « Oui », « En 3 ans », « Fusion CI IR », « Flux OM » — et une
nature. Les agrégats s'en tirent par `SUMIFS`.

**La matière est donc là et elle est machine-lisible. Ce qui manque est la
séparation des trois couches** : le socle du PLF, l'interprétation, et le
chiffrage qui s'en dérive. Proposition portée au fil courant ; trois questions
restent ouvertes pour l'auteur — le classeur reste-t-il maître, le dictionnaire
des régimes, la stabilité des clés d'un millésime à l'autre.

---

## 20260825 — Le classeur, les calculs, les protos

### A-80 — Les 30 Md€ de chômage sont une économie, et ils sont dans les 236

**Arbitré par l'auteur.** L'esprit du calcul est au proto : c'est l'allocation
qui s'éteint au-delà de six mois, pas la cotisation qui change de destination.
Le classeur le confirme deux fois — ligne 20 des baisses de dépenses de l'onglet
Manifeste, et base de dépenses explicite à l'onglet Capitalisation.

`D8-3-1-e2` est requalifié : intitulé, portée, conditions, opération et chaîne.
La mention « transfert de destination, non baisse de dépense publique » tombe.

### A-81 — Le classeur est la couche d'appui, et il se lit onglet par onglet

Tranché par Claude au titre de A-23, sur demande de l'auteur. Le classeur n'est
pas seulement le tableau de référence : **il porte le détail de chaque agrégat,
et l'onglet Gages déclare les sources poste par poste.** Un agrégat du
`REF_doctrine` qui paraît sans détail se cherche au classeur avant d'être déclaré
lacunaire.

C'est ce qui a réglé l'APL : le détail existait, il n'avait pas été ouvert.

*Corollaire* : ce que le classeur déclare comme source — un document public,
nommé, daté — se reprend tel quel au référentiel des faits. Ce qu'il ne déclare
pas reste sans source, y compris quand la provenance est vraisemblable.

### A-82 — Une dérivation en prose ne prouve rien : les calculs se rejouent

Tranché par Claude au titre de A-23, sur demande de l'auteur. Le bloc `CALCULS`
porte chaque opération du corpus sous une forme évaluable, avec son résultat
attendu et sa tolérance ; `F8` les rejoue à chaque contrôle.

**Une tolérance ne s'écrit qu'avec sa raison**, et jamais en la remontant jusqu'à
ce que le compte tombe. L'évaluateur n'accepte qu'une expression arithmétique :
ni appel, ni nom, ni attribut.

*Écarté* : rejouer les opérations en les analysant depuis leur texte français.
Le corpus les écrit en langue, pas en formule, et un analyseur de prose
mathématique serait un second point de vérité.

### A-83 — Les protos se relèvent, et la veille prend le fait par le bon bout

Tranché par Claude au titre de A-23, sur demande de l'auteur. Les six protos
rédigés n'ont pas la balise du proto Données : leurs chiffres vivent au fil des
phrases et rien ne les contrôlait. `relever_protos.py` les découpe, garde les
phrases chiffrées, et les confronte au référentiel.

**Trois sorties, et la troisième est celle qui trouve.** Les collisions
comparent des vocabulaires et sont bruyantes ; les chiffres hors référentiel
disent seulement ce qui n'est pas couvert. La **veille** part de la grandeur
publiable — ses mots, ses valeurs admises — et attrape ce qui se dit en peu de
mots. Le détecteur générique manquait la faute du 1-pager ; la veille l'a
trouvée du premier coup.

Le script ne rapproche rien : A-35 tient, un rapprochement s'écrit à la main.

### A-84 — Le 2 190 contre 2 100 n'était pas une discordance

Constaté au manuscrit, pas rapporté. Le salaire médian net est de 2 190 € (notes
e4 et e99, Insee) ; les 2 100 € sont le **revenu médian équivalent** d'Eurostat
(note e8), que le corps du livre oppose aux 4 300 € suisses. Deux grandeurs,
deux sources, aucun désaccord.

Ce que la stratégie réseaux avait relevé de l'extérieur était une **ambiguïté de
dénomination**, et le 1-pager l'a commise en écrivant « salaire médian » pour la
seconde et en donnant 5 500 € à la Suisse, chiffre qui n'existe nulle part au
corpus — au manuscrit, 5 500 € est la dette publique nouvelle par foyer.

*Conséquence* : la veille porte cette distinction en toutes lettres, de sorte
qu'aucun livrable ne la refasse.

---

## 20260825 — Les discordances tranchées

### A-74 — Pour la CSG on prend l'exact, ailleurs on prend le manuscrit

**Arbitré par l'auteur.** Deux règles, dans cet ordre.

**L'assiette de la CSG se cite à 98,25 %**, et le calcul de synthèse aussi. Le
paramètre `D3-2-1-p6` est corrigé de 98 à 98,25 ; son verdict passe à `EXACT`.
L'arrondi à 98 était d'autant moins tenable qu'il coexistait avec un abattement
de 1,75 % qui est le complément de 98,25.

**Partout ailleurs, le chiffre du manuscrit l'emporte** sur celui du proto, du
classeur ou d'un dérivé. C'est l'application de A-56 : le livre arbitre.

### A-75 — Une discordance arbitrée reste au corpus, et se déclare

Tranché par Claude au titre de A-23. Le proto est une archive : A-15 interdit de
le réécrire, et la discordance sur les retraites y restera. La faire disparaître
du contrôle serait mentir ; la laisser en échec perpétuel rendrait le contrôle
inutile.

Un groupe de `MEME_QUE` porte donc un champ `arbitrage` facultatif : **quelle
entrée est retenue, par qui, à quelle date, et pourquoi.** Le contrôle range
alors la discordance en décision visible et cesse de la compter en échec. Un
arbitrage dont l'entrée retenue n'existe pas est refusé.

*Écarté* : supprimer le rapprochement, qui effacerait la trace ; et corriger le
proto, qui violerait A-15.

### A-76 — Une tolérance ne s'écrit qu'avec sa raison

Tranché par Claude au titre de A-23. Un groupe peut déclarer une `tolerance`
dans l'unité de sa référence, et **le motif doit dire de quel arrondi il
s'agit**. Un seul cas à ce jour : 8 823,53 € à 3 % font 264,71 €/an, que la
promesse arrondit à 265. Une tolérance qui servirait à faire taire un écart réel
serait la faute que tout ce dispositif cherche à empêcher.

### A-77 — Le contrôle compare des nombres, pas des dimensions

Tranché par Claude au titre de A-23, après une première version qui sortait cinq
fausses discordances. Les montants se ramènent à l'euro avant comparaison —
« 37 059 M€ » et « 37,1 Md€ » sont le même montant, « Md€ » et « milliards » le
même mot. Mais **la comparaison de valeur ignore la dimension** : « 16,9 Md€ »
et « 16,9 Md€/an » portent le même nombre, et c'est le relevé des unités
divergentes qui dit que l'un a perdu son « par an ». Deux rapports orthogonaux
valent mieux qu'un verdict qui mélange un désaccord de chiffre et une notation.

`M`, `millions` et `milliards` sans euro restent hors de la table d'échelle : le
corpus les emploie aussi pour des personnes et pour des mois.

### A-78 — Ce que le sourçage à la main peut redresser

Tranché par Claude au titre de A-23. `SOURCES` admet désormais `valeur_num`, et
l'entrée porte `tete_redressee`. C'est le seul moyen de corriger un candidat dont
le relevé a pris une année ou un libellé de ligne pour valeur, sans toucher au
proto ni attendre la reprise du générateur.

`meme_que` disparaît de `SOURCES` : il n'a plus qu'un lieu, le bloc `MEME_QUE`.

### A-79 — L'APL n'était pas une discordance

Constaté au classeur, pas rapporté. La ligne 20 du tableau de référence
s'intitule « Extinction des chèques ciblés aux particuliers (dont APL) » et vaut
17,7 Md€. C'est un agrégat ; les 16 Md€ du sous-item `D2-4-1-s1` sont l'APL
seule. La chaîne du `REF_doctrine` écrivait « chèques ciblés dont APL 17,7 », qui
se lit « APL = 17,7 » : le libellé est corrigé sur celui du classeur.

*Reste ouvert* : le détail des chèques ciblés ne couvre que 16 des 17,7 Md€.

---

## 20260825 — Le rapprochement des faits

Tranché par Claude au titre de A-23, sauf mention contraire.

### A-69 — Rapprocher n'est pas sourcer, et les deux ne vivent pas au même endroit

A-35 posait le champ `meme_que` et le rangeait dans `sources_chiffres.SOURCES`,
au même titre qu'une source. C'était confondre deux gestes : sourcer, c'est dire
d'où vient un chiffre ; rapprocher, c'est dire que deux entrées parlent de la
même chose. Une entrée rapprochée reste sans source, et le compte des entrées
sourcées à la main ne doit pas bouger parce qu'on a écrit un rapprochement.

Le bloc `MEME_QUE` vit donc à part, dans le même module. **Son unité est le fait,
non la paire** : un groupe nomme le fait, liste les entrées qui le portent, et
dit dans `motif` pourquoi elles le portent. La première entrée du groupe est la
référence, choisie par confiance décroissante — une note du manuscrit avant un
nœud du `REF_doctrine`, un nœud avant un candidat du proto.

*Écarté* : la paire symétrique, qui ne dit pas laquelle des deux valeurs
l'emporte, et le rapprochement par égalité de valeur, qui manque exactement ce
qu'on cherche.

*Amende A-35* pour le lieu et pour la forme. Le principe est intact.

### A-70 — Le contrôle distingue trois verdicts, et un seul est un échec

`F7` comparait tête à tête et sortait « discordant » dès que la valeur ou l'unité
différait. Sur un corpus où le relevé prend le premier nombre de l'énoncé, cela
aurait sorti en anomalie des entrées parfaitement concordantes.

Trois verdicts.

- **Accord** — même valeur, ou la même au signe près quand les deux énoncés
  prennent des points de vue opposés.
- **Tête décalée** — les deux énoncés portent la valeur, mais pas en position de
  tête. Défaut du relevé, pas du corpus. Se signale, ne bloque pas.
- **Discordance** — aucune valeur commune entre les deux énoncés, déclinaisons
  comprises. **Seul échec.**

Les unités divergentes sortent à part, comme signalements : « milliards » contre
« Md€ » est une affaire de notation, pas une contradiction. Une unité vide, ou le
tiret que le `REF_doctrine` emploie pour dire qu'il n'y en a pas, ne se compare à
rien.

### A-71 — Le référentiel des faits ne se verse pas ; son appareil, si

Le fil courant prévoyait de verser `REF_chiffres.json` au coffre. Il ne le sera
pas : il se régénère à l'identique depuis quatre pièces qui sont toutes au coffre
— les notes du manuscrit, le `REF_doctrine`, le proto Données et
`sources_chiffres.py`. Un dérivé qui se refait à l'octet n'occupe pas le coffre.

Ce qui se verse est ce qui ne se refait pas : le générateur, le sourçage écrit à
la main, le rapprochement des faits, et le contrôle. Ils sont dans l'archive
technique.

*Amende* le point 4 de l'ordre du travail du fil courant.

### A-72 — Les empreintes retardaient sur le coffre, et ce n'était pas un faux

`make restauration` a sorti deux `R1` à l'ouverture : `methode/arbitrages.md` et
`methode/prompt_fil_courant.md`. Ni l'un ni l'autre n'est un faux — les deux ont
été versés au coffre après le dernier relevé d'empreintes, et le dépôt porte donc
l'état courant du coffre pendant que `empreintes.json` porte l'état d'avant.

La règle « on s'arrête sur un R1 » tient, mais elle se lit avec sa raison : un
`R1` dit qu'une pièce ne correspond pas à son empreinte, il ne dit pas laquelle
des deux est en retard. **Quand la divergence porte sur un document que la
session a elle-même versé au coffre depuis le dernier `make coffre`, c'est
l'empreinte qui est périmée.** On le vérifie au contenu — ici, trois cent
soixante-dix lignes d'arbitrage de plus que ce que l'empreinte attendait, et un
fil courant entièrement remplacé par celui du référentiel des faits — on le dit,
et on relève les empreintes à la clôture.

*Cause de fond* : un versement au coffre sans `make coffre` derrière laisse les
empreintes en arrière. La clôture d'unité l'impose déjà ; c'est la tenue en
dynamique de A-65 qui l'a contournée.

### A-73 — Le fil courant se trompait sur ce qui manquait

Constaté, pas rapporté. Le fil disait « le rapprochement `meme_que` n'est pas
implémenté ». La plomberie l'était : le générateur lisait déjà le champ, et `F7`
existait au contrôle. Ce qui manquait était la **déclaration** — le dictionnaire
était vide, comme celui des sources.

La distinction n'est pas cosmétique : elle change ce qu'il y avait à faire, de
« écrire un contrôle » à « lire le corpus et écrire les groupes ». Le second est
du travail de fond, le premier de l'outillage.

---

## 20260824 — Purge de l'horodatage, et retrait de la surspécification

### A-65 — Les notes se tiennent en dynamique, plus à la clôture

Demandé par l'auteur. Le registre, le journal et le fil courant s'écrivent **au
fil du travail**, dès qu'une décision est prise ou qu'un état change — non en un
passage à la fermeture.

*Caduc* : « les pièces jointes ne se mettent à jour qu'à la clôture d'un fil, en
un seul passage », porté à l'état du chantier le 20260820. La raison qui la
fondait — éviter la churn — est moins coûteuse que le risque qu'elle crée : un
fil interrompu perd tout ce qu'il n'a pas encore écrit.

Reste vrai : on vérifie sur un cas ciblé avant de généraliser.

*Corollaire de conduite.* Ce qui se note au corpus ne se raconte pas à l'auteur.
La tenue de l'appareil, la mécanique des renvois, le détail des correctifs : cela
s'inscrit et cela ne se rapporte pas.

### A-66 — L'horodatage est purgé des skills, à l'entrée comme à la sortie

A-2 pose un nom canonique par artefact, aucun horodatage. Les skills ne l'avaient
jamais reçue : elles nommaient leurs entrées en `Positions_AAAAMMJJ_vN.json`,
`Contrat_projection_REF_20260820_v1.md`, et **prescrivaient d'horodater leurs
sorties** — `Fiches_mesures_AAAAMMJJ_vN.html`, `QA_<sujet>_AAAAMMJJ_vN.md`. La
règle était donc violée par l'outil qui produit, pas seulement par le renvoi qui
lit.

Trente-quatre renvois corrigés dans sept skills, à l'entrée comme à la sortie.
Chacune reçoit en fin de document un bloc **Résolution des renvois** qui pose la
règle et désigne `methode/index.json` comme table, avec le bloc `manquants` pour
ce qui ne résout pas. `redaction-legistique` et `resolution-chantier` étaient déjà
propres.

Les skills sont en lecture seule en session : elles sont livrées, elles ne
prennent effet qu'enregistrées.

### A-67 — Les renvois d'appareil sont localisés, ils n'étaient pas manquants

`controle_sortie.py` était invoqué par cinq skills et localisé par aucune. Il
existe, au coffre, 518 lignes. Même cas pour `controle_arithmetique.py`. Ce
n'était pas un manque, c'était un renvoi sans chemin — et il rendait inopérant le
contrôle avant diffusion des cinq skills de projection.

`Synthèse_Calculs_Résolution_NNNN.xlsx` ne correspondait à aucune pièce jointe :
le projet porte `Synthèse Calculs Résolution_0819.xlsx`.

### A-68 — Retrait de la surspécification du fil de cadrage

Trois choses écrites dans la journée sont retirées, faute de fondement.

**L'inventaire des gagnants et des perdants n'est pas le centre du chantier.** Il
est un output parmi d'autres — le plus construit, ce qui avait fait confondre
avancement et centralité. *Amende A-63.*

**Les cinq notes de démonstration** avaient été tirées des scripts de l'agence :
une liste de chiffres sans structure, pas un plan.

**Les quatre phases et leurs dates** étaient une séquence inventée. L'ordre d'un
chantier se tire de ses dépendances, pas d'un calendrier de diffusion.

**« Les apports sont le verrou unique »** est vrai d'un output, faux de
l'ensemble.

*Reste vrai* : le manifeste est le 1-pager repris — la matière existe,
`archive/1pager_20260806_v1_proto.html`, et le prototype de site la déclarait
absente à tort.

---

## 20260824 — Le chantier reprend son objet

Recadrage de l'auteur, à la fin du fil de cadrage. Deux fautes de Claude, et le
centre du chantier remis à sa place.

### A-62 — Le chantier ne juge pas le livre

*Amende A-51 et supprime la phase 0 telle qu'elle avait été écrite.*
**Garde-fou A-24 violé** : ne pas classer ni qualifier un document non ouvert.

Claude n'a jamais ouvert le manuscrit. Les prétendues lacunes du livre — `D12`
sans proposition, le premier axe sans énoncé propre, `D4-2-3` sans gain — sont
des trous du **référentiel**, pas du livre : le livre traite peut-être tout cela
en prose sans que la dérivation en tire un effet chiffrable. Les avoir présentées
comme des corrections à remonter à l'éditeur, et en avoir fait la phase
prioritaire de la feuille de route et l'objet du fil suivant, était une faute de
qualification.

**Ce qui reste, et c'est tout.** Un contrôle arithmétique, mécanique et sans
jugement : les valeurs discordantes — deux entrées portant le même fait avec deux
valeurs, dont l'une imprimée — et les sommes qui ne tombent pas. Cela seul expire
avec le bon à tirer.

**Ce qui sort du périmètre.** Un axe sans proposition, une proposition sans effet,
une promesse mal calibrée : constats de dérivation, ils appartiennent au
référentiel et se traitent en aval. Le livre est jugé par ses auteurs.

### A-63 — L'inventaire des gagnants et des perdants est le centre, et le site en est la sortie

Arbitré par l'auteur, qui le remet au premier plan : la formalisation interne de
la doctrine et de ses outils d'interprétation est faite ; ce qui compte
maintenant est **l'inventaire des gagnants et des perdants, sa présentation au
public, et le prototype de site.**

C'est cohérent avec l'état du corpus, et Claude l'avait dispersé dans un plan
calqué sur celui de l'agence. L'inventaire est le seul objet qui répond à la
question que tout lecteur se pose — *et moi ?* — et c'est le plus construit :
deux cent soixante-seize lignes ancrées, avec miroir et raccroche. L'extrait et
l'interface existent, l'interface porte déjà le visuel du site.

**Un seul verrou commande les trois sorties : les apports.** Douze gains sur cent
quatre-vingt-douze ont leur `apport` écrit ; les cent quatre-vingts autres se
projettent encore par l'énoncé du `REF_doctrine`, qui est une phrase du livre
reprise mot pour mot. Tant que ce champ est vide, l'extrait, l'interface et le
site sortent du texte de livre découpé. Ni la charte, ni le sourçage, ni
l'outillage ne débloquent cela.

*Caduc* : la restriction des apports aux cinq familles visées par la stratégie
réseaux, portée à la première version de la feuille de route. Une interface par
situation ne peut pas laisser une situation vide.

*Coût annoncé* : environ trois cent soixante textes courts, dix unités de travail,
plusieurs fils. Incompressible — c'est de l'écriture, pas de la génération.

### A-64 — Le prototype sort avec les familles écrites, et grandit — *proposé*

**Proposition de Claude, non validée.** Le prototype de site et l'interface ne
publient que les familles dont les apports sont écrits, et s'étendent à mesure.
Huit fiches complètes valent mieux que cinquante-six ébauches : une catégorie
visible et vide est pire qu'une catégorie absente.

*Alternative écartée par la proposition* : attendre les cent quatre-vingts apports
avant toute mise en ligne, ce qui repousserait le prototype au-delà de septembre.

---

## 20260824 — Le livre n'est pas tout le travail

Précision de l'auteur, le même jour, qui renverse une déduction abusive de A-49 et
recompose la feuille de route. Le livre est le point d'orgue ; les publications
qui suivent existent pour développer ce qui est sous-jacent, implicite ou attendu
au livre et n'y figure pas par concision — chiffres, annexes, calculs, et
dispositions juridiques.

### A-56 — Le livre arbitre, il ne borne pas

*Amende A-49.* La distinction référence / source y était juste. La conséquence
qui en avait été tirée — « un chiffre qui n'est pas au livre ne se publie pas
d'ici le 9 octobre » — était une déduction de Claude, non un arbitrage de
l'auteur, et elle est fausse.

**Arbitre** : entre les quatre comptes, entre les trois auteurs, entre deux
documents qui divergent, le livre tranche. Un chiffre publié qui le contredit est
une faute grave.

**Ne borne pas** : un chiffre publié qui n'y figure pas est le programme. Ce que
le livre a comprimé est exactement ce que la suite doit démontrer.

*Caduc* : la mise hors chemin critique des cent neuf candidats du proto Données.
Ils sont la matière des premières notes.

*Reste vrai* : le livre ne fait pas source à l'écran. Un contenu qui affiche
« source : notre essai » est circulaire. Ce qui s'affiche est ce que le livre
cite lui-même, dans ses notes de fin.

### A-57 — Ce qui expire dans le sourçage, et ce qui attend

Tranché par Claude au titre de A-23, tiré de A-56 et de la fenêtre de correction.

Sourcer cent neuf candidats est long. **Vérifier si l'un d'eux contredit un
chiffre imprimé est rapide et mécanique** : le champ `meme_que` de A-35 sert
exactement à rapprocher deux entrées et à sortir la discordance. C'est la seule
part du sourçage qui ne peut pas attendre le bon à tirer — une contradiction
trouvée après est une contradiction publiée.

Le reste du sourçage se fait ensuite, au rythme des notes qui le réclament.

### A-58 — La note est l'unité de la démonstration

Arbitré par l'auteur. Les annexes et les calculs sortent en **notes
téléchargeables, publiées une par une** : quelques pages, un sujet, registre de
note d'institut, citables et transmissibles. Ni page web, ni volume exhaustif.

Le public le commande : les journalistes sont la cible prioritaire, et **un
journaliste ne clique pas sur une page, il cite une note.**

*Conséquence d'appareil* : la chaîne existe déjà — la note s'écrit en markdown et
s'exporte par `impression-docx`, qui porte les conventions typographiques. Ce qui
manque est le gabarit, comme `fiche-mesure` porte celui de la fiche.

*Conséquence de dérivation* : **la liste des notes ne se tire pas de l'ordre de la
doctrine mais des chiffres qui vont sortir à l'écran.** L'ordre de production est
commandé par les contenus, non par les axes.

### A-59 — La note précède le contenu qu'elle démontre

Tranché par Claude au titre de A-23. Le script 2 de la stratégie réseaux finit par
« Le détail est en lien. Vérifiez-nous. » ; la bio du compte porte « Nos
propositions ⬇️ https://…… ». Les deux pointent vers rien.

**Un contenu qui appelle à la vérification et renvoie vers le vide est plus
dangereux qu'un contenu sans source** : c'est la promesse de transparence prise en
défaut, sur le seul terrain où le dispositif se déclare imbattable.

L'ordre est donc inverse de l'ordre naturel : on ne publie pas puis on
approfondit. Le contrôle de sortie vérifie qu'un script portant un appel à
vérification porte l'adresse de sa note.

### A-60 — Le site est une vitrine, les preuves sont à côté

Arbitré par l'auteur. Le site présente le livre et le mouvement ; les notes se
téléchargent depuis lui sans être lui. Deux objets, deux calendriers.

*Écarté* : le site comme porteur des preuves, qui en aurait fait une
infrastructure à livrer avant l'ouverture des comptes.

### A-61 — Les textes déposables complets sont un objectif, pas un supplément

*Amende A-48.* La légistique y était déclassée comme accessoire de crédibilité.
Elle descend en date — après le 9 octobre — mais non en rang : les dispositions
juridiques sont l'un des deux corps de la production postérieure au livre.

Périmètre arrêté par l'auteur : **textes déposables complets**, révision
constitutionnelle, loi organique, loi ordinaire, avec exposé des motifs. Ni
articles isolés, ni simple qualification de la voie normative.

Le corpus a de la matière et rien n'est à réinventer : deux propositions de
révision consolidées, en substitution et en modificative, le trois colonnes
Constitution et LOLF, le récapitulatif de transposabilité, le recensement des
innovations. Tous antérieurs aux contrôles, tous à reprendre.

---

## 20260824 — Le cadrage

Les objectifs sont recueillis, la feuille de route est refaite. La question
principale du registre — à quoi sert ce chantier dans les six prochains mois, et
dans quel ordre — est tranchée et quitte les questions ouvertes.

Le cadrage a une pièce déterminante que le corpus ne portait pas : la stratégie
réseaux du 29 juillet 2026, pièce jointe du projet, qui fixe la date de sortie de
l'essai, le ton, le vocabulaire, l'architecture des comptes et le plan de
lancement. Le chantier travaillait sans elle.

### A-48 — Le public, et ce qu'il déclasse

**Journalistes et faiseurs d'opinion d'abord, grand public et militants
ensuite.** Décideurs et spécialistes des finances publiques ne sont pas la cible :
ils sont l'arbitre. On écrit pour être relayé et pour être vérifié.

*Écarté* : les décideurs en cible directe, et l'ordre de production qui en aurait
découlé.

*Conséquence* : **la rédaction légistique descend après le 9 octobre.** Aucun des
deux publics prioritaires ne lit une proposition de loi. Elle sert la crédibilité
le jour où l'on nous opposera que rien de tout cela n'est opérationnel ; elle ne
sert pas la diffusion.

### A-49 — Le livre fait référence, il ne fait pas source

Arbitré par l'auteur. Le document de référence unique que la stratégie réseaux
appelait en livrable n° 1 **est l'essai lui-même**, non `REF_chiffres`.

Deux régimes, et les confondre est le seul moyen de perdre.

**Référence.** Entre nous, entre les quatre comptes, entre les trois auteurs, ce
qui tranche est le livre. Un chiffre qui n'y est pas ne se publie pas d'ici le
9 octobre, sans exception, y compris s'il est juste. C'est la réponse au défaut
que l'agence a relevé : deux documents donnant 2 190 € et 2 100 € de salaire
médian.

**Source.** À l'écran, ce qui s'affiche n'est jamais le livre. Un contenu qui
affiche « source : notre essai » est circulaire, et c'est l'angle par lequel le
dispositif se démonte. La source affichable est celle que le livre cite
lui-même : les cent quarante et une notes de fin, dont trente-sept portent un
chiffre.

*Conséquence sur `REF_chiffres`* : il change de fonction. Il n'est plus le point
de vérité des faits au sens où il prétendait l'être — le livre l'est — il devient
la table qui relie un chiffre publiable à sa source externe affichable. Le
sourçage des cent neuf candidats du proto Données sort du chemin critique : ils
ne sont pas au livre, donc ils ne se publient pas, donc ils attendent.

*Devient prioritaire, en revanche* : les onze notes chiffrées qu'aucun référentiel
ne cite — `e29`, `e46`, `e63`, `e65`, `e75`, `e79`, `e83`, `e92`, `e109`, `e130`,
`e139`. Ce sont des chiffres du livre, donc publiables, et l'appareil ne les voit
pas. Elles cessent d'être un point ouvert qui se traite au fil.

*Caduc* : « les cent neuf candidats se reprennent par lots » comme travail
prioritaire, porté en A-37. La règle du repassage dans les produits reste vraie
pour le jour où on les reprendra.

### A-50 — La frontière de production passe par le sourçage

Arbitré par l'auteur. Les contenus réseaux se produisent à deux : **ce qui affiche
un chiffre passe par le chantier, le reste par l'agence.**

Les deux premiers piliers éditoriaux — « Où passe votre argent », « Ce qu'on vous
rend » — sont chiffrés de bout en bout : l'essentiel du volume tombe donc du côté
du chantier. Huit contenus par semaine sur le seul compte média ne s'écrivent pas
à la main : il faut une chaîne, non des textes.

### A-51 — La fenêtre de correction du livre commande la séquence

Arbitré par l'auteur : le manuscrit est encore modifiable.

Deux conséquences qui ne se négocient pas. **Les lacunes remontent au livre
maintenant** : le premier axe de la doctrine sort sans un énoncé propre, `D12` ne
porte aucune proposition, le « 600 € » est attaquable et l'agence l'a nommé, les
sous-items de `D2-2-1` totalisent 29,3 Md€ quand l'effet du même nœud en porte
12,4. Une correction faite maintenant est gratuite et définitive ; dans trois
semaines elle se paiera en ripostes pendant deux ans.

**Et la fenêtre se ferme avant la production du stock.** Toute correction au livre
change la strate 1 et régénère tous les dérivés. Produire avant la clôture du bon
à tirer, c'est produire deux fois.

*Caduc* : la mention « à instruire au manuscrit » traitée comme un point ouvert
sans échéance. Elle a désormais une date de péremption.

### A-52 — Les quatre besoins extérieurs sont un seul dispositif

Tranché par Claude au titre de A-23. Analyse de proposition externe,
contreproposition, réaction au PLF, réaction à l'actualité : c'est le même geste
— ingérer un texte qu'on ne maîtrise pas, le qualifier, le confronter au
`REF_doctrine`, sortir une position. Un dispositif, quatre usages, armé en octobre
pour tourner en novembre.

*Écarté* : quatre procédures distinctes, qui auraient divergé dès le deuxième
emploi.

### A-53 — Le vocabulaire devient un contrôle de sortie

Tranché par Claude au titre de A-23. La liste des termes de la stratégie réseaux
n'est pas une préférence de style, c'est une règle vérifiable mécaniquement :
« restitution » et non « baisse d'impôt », « ce qu'on vous prend » et non
« prélèvements obligatoires », « bureaucratie » et non « fonctionnaires »,
« intermédiaires » et non « administration », « ceux qui produisent » et non
« les actifs », « on a vérifié » et non « il est évident que ». Jamais « il
faut ». Jamais un nom de personne. Elle est portée à `controle_sortie.py`.

S'y ajoute la règle de proportion : le constat occupe un cinquième du contenu, la
solution quatre, et aucun livrable ne se termine sur un problème.

### A-54 — Trois acquis du corpus que la stratégie réseaux ignore

Constaté par recoupement, pas rapporté.

**Le pilier « L'État qu'on sauve » n'est pas absent du corpus.** L'agence le
déclare absent de tous les documents. Les cinquante-sept pertes du référentiel des
positions portent chacune sa `justification` et son `relais` : c'est exactement
la matière de ce pilier, et elle est écrite.

**`RT-3` est l'antidote à la faiblesse relevée sur la soustraction.** L'agence
avertit qu'une campagne qui n'est que soustraction produit de l'anxiété. La
reconstitution volontaire du flux est la réponse doctrinale, déjà arbitrée, et
vingt-neuf lignes du référentiel la portent.

**Le registre est déjà le bon.** Les apports s'écrivent à la deuxième personne du
pluriel, sans nomenclature interne, sans citer le manuscrit comme autorité. Le
corpus et l'agence ont convergé sans s'être parlé.

### A-55 — Le manuscrit du corpus est l'essai qui sort le 9 octobre

Vérifié par recoupement verbatim, non supposé. La stratégie réseaux cite
« 63 euros de richesse produits pour 23 euros nets récupérés » et « les 500 plus
grandes fortunes couvriraient à peine huit mois de dépenses publiques » : ce sont
les lignes du bloc `C-00 la nation` du référentiel des positions, dérivées du
manuscrit. La strate 1 du chantier est le livre qui paraît le 9 octobre 2026.

---

## 20260824 — L'ouverture de session, réparée

Quatre fautes à l'ouverture du fil de cadrage, dont trois viennent de la
procédure elle-même. Tranché par Claude au titre de A-23, et inscrit avec les
fautes qui l'ont provoqué.

### A-38 — Ce que la restauration a réellement coûté

Constaté, pas rapporté, et **mesuré après coup, contre la version mécanique** —
la première version de cette entrée en comptait deux, il y en avait dix.

Seize documents ont été restaurés par des fils auxiliaires. **Dix sont revenus
altérés, six intacts.** Deux se voyaient : le manuscrit rendu en squelette de
607 octets, l'index rendu avec ses retours ligne échappés en clair. Les huit
autres ne se voyaient pas — un à trois octets, une ligne finale absente. Et deux
d'entre eux ne sont pas du bruit mais **une réécriture du texte** :

- `methode/procedure_controle.md` : « Version 20260820 v2 » devenu « Vers
  20260820 v2 » ;
- `methode/regles_redactionnelles.md` : « Employer "on", "nous", "chacun" »
  devenu « Employé "on", "nous", "chacun" », et une altération dans la règle de
  la virgule devant conjonction.

Ce sont les règles de rédaction du corpus, réécrites en silence par un copiste.

**Aucun contrôle ne les a vus.** Le premier a été trouvé à la taille, le second
parce qu'un script a refusé de charger le fichier ; les huit autres n'ont été
trouvés qu'au test de bout en bout, une heure plus tard. Entre-temps, un contrôle
indigent — chercher la chaîne `\n` dans les fichiers de méthode — a été présenté
comme une vérification et a conclu « les .md semblent sains ». Ils ne l'étaient
pas.

**Trois versements ont propagé la corruption au coffre** : `CLAUDE.md`,
`methode/arbitrages.md` et `methode/journal.md` ont été édités à partir de la
version altérée, puis versés. Ils sont recousus — version mécanique du coffre,
plus le patch des éditions de la session, appliqué par `patch` et non à la main.

### A-39 — Le coffre ne rend ses documents qu'en texte, et c'est la cause

Vérifié sur trois cas. `technique/coffre.txt`, 927 ko, revient au dépôt comme
**fichier** : copie à l'octet possible. `manuscrit/manuscrit.html`, environ
220 ko, et `livrables/carte_du_projet.html`, 25 ko, reviennent comme **texte** :
toute écriture repasse par le modèle.

Conséquence tenue : la règle « toute pièce restaurée se compare à l'octet avant
emploi » était **inapplicable**, faute de référence à quoi comparer. Elle a servi
de garantie de façade pendant trois sessions.

### A-40 — Les empreintes, écrites au versement, contrôlées au dépliage

`methode/empreintes.json` porte, pour chaque artefact du coffre, son SHA-256, sa
taille en octets et son compte de lignes. `appareil/empreintes.py` les relève à
`make coffre` ; `appareil/controle_restauration.py` les compare au dépliage et
sort R1 à R4. **Une divergence est un faux au dépôt** : il ne se corrige pas, il
se redemande au coffre.

Le relevé est **cumulatif** : un fil qui ne déplie qu'une partie du coffre
n'efface pas les empreintes du reste. Une session ne détruit pas ce qu'elle n'a
pas vu.

Éprouvé : un octet ajouté à `methode/journal.md` sort en R1. Les deux corruptions
de la matinée auraient été vues au dépliage.

### A-41 — Une restauration ne se délègue jamais à un modèle

Ni à un modèle auxiliaire, ni au modèle principal. Une restauration est une copie
d'octets ou elle n'a pas lieu : `cp` du fichier rendu par le coffre, ou dépliage
d'une archive. **Un document que le coffre ne rend qu'en texte n'est pas
restaurable à l'octet**, quoi qu'en dise son champ `restaurable`, et rien de ce
qui en sort ne se cite ni ne se reverse.

*Caduc* : la délégation de la restauration à des fils auxiliaires, employée le
matin même pour six lots.

### A-42 — On lit avant de déplier, et on ne déplie que ce que le fil demande

La procédure faisait déplier tout le coffre à l'étape 1 et lire le fil courant à
l'étape 5. Le fil courant du jour disait, écrit noir sur blanc : *ce fil ne
déplie pas le coffre et ne joue aucun `make`*. Il a été déplié quand même, parce
que le rituel passait avant la lecture.

L'ordre est inversé. On lit d'abord `methode/index.json`,
`methode/prompt_fil_courant.md` et `methode/arbitrages.md` — trois documents, rien
d'autre. Le fil courant dit ce dont il a besoin. **On ne déplie que cela**, on
joue `make restauration`, et on s'arrête sur un R1.

*Caduc* : le dépliage systématique en ouverture.

### A-43 — Rien ne se génère à l'ouverture, y compris un référentiel absent

`REF_chiffres` et la carte ont été régénérés à l'ouverture, alors que la règle
l'interdit et que la carte se lit au coffre. Un dérivé absent du dépôt se
constate ; il ne se refait que si le fil en a besoin.

### A-44 — Le texte rendu par le coffre est sur le disque, et il se copie

Relevé par l'auteur, contre une conclusion fausse : « le coffre ne rend qu'en
texte » avait été traduit par « un document lisible du coffre ne peut revenir au
dépôt sans passer par le modèle ». C'était faux, et cette erreur a fondé les
quatre entrées qui précèdent.

**Le texte que le coffre rend est écrit verbatim au transcript de session**, en
JSON, sur le disque de l'atelier — celui du fil principal comme celui de chaque
fil auxiliaire, y compris ceux qui sont morts avant d'écrire. Il s'en extrait par
script. La restauration est donc **toujours** une copie d'octets, exactement
comme le dépliage d'une archive.

`appareil/restaurer.py` le fait. Il relève tous les transcripts, résout
`chemin_coffre` vers `chemin` par l'index, et écrit. Deux garanties tenues :

- **il n'écrase jamais un fichier présent** — le transcript porte l'état d'avant,
  et réécrire dessus détruirait le travail de la session sans le dire. La règle
  s'est vérifiée dans l'heure : une première version sans cette garde a fait
  régresser `methode/index.json`, sauvé parce que c'est un dérivé ;
- **deux versions divergentes d'un même document arrêtent le script.** C'est au
  coffre de dire laquelle vaut.

Un document que la session n'a pas encore lu n'est pas hors d'atteinte : un fil
auxiliaire sert de **tuyau** — il lit, il n'écrit rien, et le transcript garde les
octets. Dix-sept documents ont été récupérés ainsi.

*Caduc* : « un document que le coffre ne rend qu'en texte n'est pas restaurable à
l'octet », et l'interdiction de citer un verbatim du manuscrit. Reste vraie, et
c'est le point qui compte : **une restauration ne se délègue jamais au jugement
d'un modèle.** Elle passe par `cp`, par le dépliage d'une archive, ou par
l'extraction du transcript.

### A-46 — Le dispositif se prouve à blanc, dans un dépôt vierge

Un contrôle qui ne s'exerce que sur le dépôt courant ne prouve rien : les
empreintes du matin avaient été relevées **sur les faux**, et disaient donc que
tout allait bien. C'est le test à blanc qui a trouvé les huit altérations
silencieuses.

La procédure est donc : déplier l'archive et restaurer dans un dépôt vierge, puis
comparer aux empreintes. Ce que ce test dit, aucun autre ne le dit — il compare le
coffre à lui-même, sans passer par ce que la session croit savoir.

`R5` naît du même test. Un dérivé horodate son pied de page — l'extrait porte la
date de sa projection — et divergerait à chaque session. Un dérivé qui diverge
n'est pas un faux : il se régénère. Il sort de `R1` pour ne pas noyer ce qui
compte.

### A-47 — La restauration suit la chronologie, elle n'arbitre pas

Un document lu deux fois dans une même session n'est pas un conflit : la session a
versé entre les deux, et **la lecture la plus récente vaut**. `restaurer.py` trie
par horodatage du transcript et dit quelles versions il écarte, avec leur heure.

La première version s'arrêtait sur ces cas en les appelant conflits — elle aurait
bloqué sur quatre documents dès le fil suivant, sans raison.

### A-45 — Le manuscrit est au dépôt, et sa fidélité est prouvée

224 422 octets, 868 lignes, 141 notes de fin et 141 appels — le compte que la
carte annonce —, 5 parties, 15 chapitres, 100 espaces insécables, 1 553
apostrophes typographiques.

Preuve indépendante, et c'est elle qui vaut : `extraire_notes.py` joué sur le
manuscrit restauré redonne `referentiels/notes_manuscrit.json` **identique à
l'octet** à celui que le coffre portait — 141 notes, 37 chiffrées. Un manuscrit
altéré ne produirait pas ce fichier.

Le coffre est intégralement au dépôt : 71 artefacts, 70 empreintes, zéro
divergence, zéro anomalie à `make index` et à `make controle`.

---

## 20260821 — La skill du chantier

### A-34 — `resolution-chantier` est réécrite sur A-23

La skill portait la conduite d'avant le partage du travail : « une question
fermée à la fois, avec de courtes pistes, et validation avant exécution », et
« avant toute génération, montrer le contenu prévu et attendre un feu vert ».
Les deux sont caduques. **Demander un feu vert pour de la tambouille est
désormais une faute, au même titre que trancher seul une question de fond.**

La version neuve porte en tête le partage du travail et les quatre garde-fous,
et ajoute ce que le corpus a appris depuis : le classement par contenu et le lieu
unique de l'affectation, les documents que nul script ne restaure, le contrôle du
dépliage à l'octet, le référentiel des faits et ses quatre niveaux de confiance.

Elle est en lecture seule en session : livrée à l'auteur, qui l'enregistre une
fois.

---

## 20260824 — Le référentiel des faits, reprise

Trois corrections après arbitrage de l'auteur. Le fil précédent avait posé en
questions ce qui était de la tambouille : ces trois points se tranchent ici.

### A-35 — La répétition d'un chiffre n'est pas une faute

Un chiffre énoncé trois fois au corpus fait trois entrées. Le référentiel sert à
dire qu'elles **concordent**, non à les fusionner. Le contrôle qui relevait « la
même valeur dans deux provenances » était absurde et disparaît.

**Le rapprochement de deux entrées ne se devine pas, il s'écrit.** Deux nombres
égaux ne parlent pas forcément de la même chose. Un champ `meme_que`, écrit à la
main dans `appareil/sources_chiffres.py`, dit que deux entrées portent le même
fait ; le contrôle vérifie alors leur accord et sort en anomalie toute
discordance. Il ne contrôle que ce qui a été rapproché, et il grandit à mesure du
sourçage.

### A-36 — Une source se transmet à l'intérieur d'une proposition

Un sous-item ou un paramètre qui ne déclare aucune source vient du même décompte
que l'effet de sa proposition. La source s'y hérite, marquée `source_heritee` —
ce n'est pas une source inventée, c'est la même source, dite deux fois. Les
vingt-cinq chiffres du `REF_doctrine` qui sortaient sans source sont sourcés.

Restent à sourcer les cent neuf candidats du proto Données, et eux seuls.

### A-37 — Les candidats du proto se reprennent, et les produits se repassent

Les cent neuf candidats se vérifient et se corrigent par lots, contre les
classeurs et le manuscrit. **Et il faudra repasser dessus dans les produits** :
un chiffre corrigé au référentiel ne s'arrête pas là, il remonte dans tout
livrable qui le citait. Porté au fil courant et à l'état du chantier.

---

## 20260821 — Le référentiel des faits

### A-30 — `REF_chiffres` existe, et il vaut par ce qu'il déclare ignorer

Le référentiel des faits est produit. Schéma d'abord : valeur, unité, millésime,
source, dérivation, déclinaisons, code d'origine, niveau de confiance. Il se
régénère depuis les notes du manuscrit, le `REF_doctrine` et le proto Données ;
le sourçage écrit à la main vit à part, dans `appareil/sources_chiffres.py`, et
survit à chaque régénération — même dispositif que les justifications et les
apports du référentiel des positions.

**Aucune source ne s'invente et aucun trou ne se comble.** 257 entrées, dont 134
sans source, tous les 109 candidats du proto compris. Le contrôle les compte et
ne les efface pas.

### A-31 — Quatre niveaux de confiance, et l'arithmétique n'est pas une source

`3` le manuscrit, corps ou note. `2` une source déclarée au corpus. `1` un
ancrage de passage ou une opération rejouée, sans source. `0` sans source.

**Une opération rejouée dit que le compte est juste, non qu'il est sourcé.** Les
deux ne se confondent pas : elle vaut un ancrage, jamais une source.

### A-32 — Ce que le relevé mécanique s'interdit

Il lit la valeur et son unité dans un vocabulaire d'unités fermé, prend le
millésime là où le corpus l'écrit, reprend l'opération quand elle est portée, et
la source telle qu'elle est énoncée. Il ne devine ni unité, ni millésime, ni
source. Il écarte ce qui ne porte aucun nombre et ce qui n'est qu'une date de
publication, et il compte ce qu'il écarte.

Deux conséquences tenues. L'ancre d'un nœud du `REF_doctrine` n'est pas une
source, c'est un ancrage. L'unité que le proto déclare en attribut de ligne ne
se rapporte pas d'office à la valeur de tête : elle se garde à part.

### A-33 — Les notes de fin sont de la doctrine

Arbitré par l'auteur. Une note de fin fait partie intégrante de la doctrine : son
énoncé a donc sa place au référentiel des faits, au même titre qu'un énoncé du
corps. Il y est extrait du relevé à chaque génération et l'entrée le déclare, de
sorte que le manuscrit reste seul point de vérité et qu'aucune correction ne se
fait en aval.

*Caduc* : la règle « le texte d'une note ne se recopie ni au REF, ni au
référentiel des positions, ni dans un livrable », pour la part qui visait un
dérivé régénéré. Elle continue de valoir pour tout ce qui s'écrit à la main.

---

## 20260821 — L'atelier

Tranché par Claude au titre de A-23, sans arbitrage demandé.

### A-25 — L'affectation aux familles vit dans le générateur de la carte

`appareil/generer_carte.py` porte la table du classement, et personne ne la
redouble : `appareil/generer_index.py` l'importe et reporte le champ `famille`
dans l'index, pour que toute skill puisse le lire. Les onze noms de famille de
`methode/classement_corpus.md` sont la clé exacte, et un artefact qui n'en porte
aucun sort en anomalie `I5`. La carte est de nouveau un dérivé : la version
régénérée est identique à celle écrite à la main, au seul bloc de dette
technique près, qui tombe puisque la dette est payée.

*Caduc* : la carte écrite à la main hors atelier.

### A-26 — Les sources se déclarent, elles ne se relèvent plus de l'arborescence

Le balayage de `sources/` faisait dépendre la table de résolution de ce qu'un
conteneur portait ce jour-là : une pièce jointe non restaurée disparaissait de
l'index sans bruit. La table est curée, comme tout le reste de l'appareil.

### A-27 — Ce que nul script ne restaure se déclare comme tel

Deux cas, une conséquence : les pièces jointes du projet, sur lesquelles Claude
n'a pas la main, et les documents binaires que le coffre porte comme documents et
non comme octets — un PDF, un docx. Les réécrire au dépôt supposerait de les
recomposer par le modèle, donc de fabriquer un faux. Vingt documents portent
`restaurable: false` ; leur absence de l'atelier se constate en fin de contrôle
et ne compte pas pour une anomalie.

### A-28 — `guide_legistique` est résolu, `REF_chiffres` entre aux manquants

Le renvoi mort du guide de légistique se résout par alias sur
`sources/structure_ppl.md`, qui en est la digestion. Il quitte les manquants.
`REF_chiffres`, spécifié et jamais construit, y entre : un manquant que la carte
nommait et que l'index taisait.

### A-29 — Ce que le trois colonnes porte, et ce qu'il ne porte pas

Vérifié fichier ouvert. Les trois colonnes sont **texte actuel · réforme visée ·
rédaction révisée** : le texte projeté est en troisième colonne, la justification
en deuxième et en note de la troisième. La formule « en vigueur, projeté,
justification » inversait les deux dernières.

La première colonne n'est un verbatim entre guillemets que pour 26 blocs sur 37
à la Constitution, 21 sur 29 à la LOLF ; le reste est un résumé ou un constat de
vacance, ce qui est juste pour un article nouveau et trompeur pour un article
existant. **Le point de vérité du texte en vigueur reste le texte nu de
référence**, en références externes.

---

## 20260821 — Le partage du travail

### A-23 — Qui décide quoi

**L'auteur valide les inputs et les outputs.** Ce qui entre au corpus et ce qui
en sort passe par lui.

**Il répond à des questions précises, pas à pas, sur les objectifs et les
subtilités.** Pas à des questions de rangement, de forme ou d'outillage.

**On structure ensemble les process de production compliqués.** Un enchaînement
nouveau qui va être rejoué se conçoit à deux.

**Claude se débrouille seul pour sa tambouille.** Méthode de détail, appareil,
index, générateurs, nommage, découpage des fils, ordre d'exécution : il tranche
et il inscrit.

**Quand l'auteur énonce une nouvelle règle, Claude consulte ce que de droit et
met à jour ce que de droit.** Une règle nouvelle qui contredit un document du
corpus se propage le jour même, sans qu'on ait à le demander.

**Claude maintient son architecture interne en dynamique**, pour ne pas
surspécifier ni surimposer à l'auteur. Le coût d'une décision d'organisation ne
se reporte pas sur lui.

*Caduc* : la validation préalable généralisée, et « une question fermée à la
fois, avec de courtes pistes, et validation avant exécution ».

### A-24 — Les quatre garde-fous

Tirés des cinq reprises qu'a coûtées le fil du classement.

- **Ne pas classer ni qualifier un document non ouvert**, et dire quand il ne
  l'a pas été.
- **Ne porter au registre en « validé » que ce que l'auteur a dit.** Une
  proposition va dans un bloc *proposé*.
- **Aucun superlatif non vérifié.** Distinguer ce qui est constaté de ce qui est
  rapporté.
- **Annoncer le coût d'une opération avant, jamais après.**

---

## 20260821 — Classement du corpus par contenu

Validé bloc à bloc. Le détail de l'affectation vit dans la carte du projet, les
règles dans `methode/classement_corpus.md`.

### A-9 — Trois surfamilles, neuf familles

`input` — doctrine, extensions, references externe et interne.
`travail` — grilles, bac à sable, methode, outillage.
`output` — juridique, redactionnel, graphique.

*Caduc* : les sept dossiers du coffre.

### A-10 — Une matière et le document qu'on en tire sont deux artefacts

Jamais un seul, jamais au même endroit. Trois occurrences constatées le même
jour : le trois colonnes et les PPLC ; les candidats chiffrés du proto Données et
sa section « Perdants » ; l'analyse de transposabilité et le récapitulatif
externalisé.

### A-11 — La promotion porte sur le document, pas sur la matière

Un output gelé et validé monte en `input / extensions` ; la matière reste en
`travail`. Le trois colonnes est la strate maître : une mise à jour ciblée s'y
fait, puis on rejoue les outputs.

### A-12 — Les outputs se distinguent par leur code formel

Juridique, rédactionnel, graphique. Critère de l'à-cheval : si le texte se lit
sans sa mise en forme, il est rédactionnel.

### A-13 — Référence ou méthode

Vérifiable contre une source externe : référence. Décidé par nous : méthode.

### A-14 — Une référence externe entre par sa digestion

L'original reste dehors. La digestion cite ses autorités. Le renvoi
`guide_legistique` résout sur `reference/structure_ppl.md`.

### A-15 — Un document externalisé ne se réécrit pas

Gelé au millésime de ce qu'il disait ce jour-là.

### A-16 — Le coffre ne porte que les dérivés que l'auteur lit

Restent la carte et l'extrait. Sortent `positions.json`,
`notes_manuscrit.json`, `donnees.json`, l'interface, l'inventaire, l'arbre, le
relevé des notes.

### A-17 — Rien n'entre au coffre en PDF ni en docx

Un classeur s'interroge par script et ne se verse pas. Ce qui se fabrique ne se
verse jamais.

### A-18 — Un fil n'est pas un lieu de stockage

### A-19 — La carte se lit en haut du projet

Elle est la première chose que lit un fil neuf.

### A-20 — `REF_doctrine` reste replié

Document de Claude. Une vue lisible se sort à la demande.

### A-21 — Le classement est une vue, les adresses ne bougent pas

Recopier le manuscrit ou un texte normatif ferait passer son verbatim par le
modèle. **Un document ne se déplace, ne se réécrit et ne se reformate que si sa
recopie ne risque pas de le déformer.**

### A-22 — Ce qui n'est pas validé n'est pas de l'input

Un travail de Claude reste au bac à sable tant qu'il n'a pas été relu.

### Supprimés

`bootstrap_resolution_20260820.sh` et `controle_projet_20260820_v3.py`.

---

## 20260821

### A-1 — Le corpus vit dans le projet Claude

Le projet est le coffre ; le conteneur de session est un atelier jetable.

*Écartés* : l'aller-retour de zips ; un dépôt GitHub, dont le bac à sable refuse
les identifiants ; le dossier connecté par l'application de bureau, absente à ce
jour — il reste la cible.

### A-2 — Un nom canonique par artefact, aucun horodatage

*Exception* : les documents gelés restent datés.

### A-3 — La résolution des renvois est déléguée à Claude

### A-4 — Trois statuts, et le contenu commande le format

L'input de l'auteur est en lecture seule ; les travaux de Claude se régénèrent ;
les outputs communs se valident avant diffusion. **Le statut se lit au contenu,
jamais au format.**

### A-5 — Le coffre ne montre que l'input, l'output, et les briques

### A-6 — Une sortie gelée ne part qu'au cas par cas

Une gelée que rien ne sait refaire ne se supprime pas.

### A-7 — Claude cadre et limite activement les fils

Un fil de travail ne tranche pas une question de fond : il l'inscrit et
s'arrête. Lire avec A-23 : ce qui est de la tambouille se tranche, ce qui touche
l'input, l'output ou un objectif s'inscrit et attend.

### A-8 — Tenir le contexte plutôt que creuser un point

Le risque réel n'est pas la perte de mémoire, c'est la perte de rythme.
**Borner l'effort, annoncer le périmètre, ne pas approfondir sans mandat.**
