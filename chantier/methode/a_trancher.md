# À trancher — les questions qu'un fil de méthode doit reprendre

*Une ligne par question ouverte, avec le CR qui la pose. Un fil de méthode lit ce
fichier en premier et n'a besoin de rien d'autre pour savoir ce qui l'attend.*

**Un fil qui tranche une question la retire d'ici et l'inscrit au registre des
arbitrages. Un fil qui en ouvre une l'ajoute ici, avec son CR.**

**Deux familles, et elles ne se tranchent pas dans le même fil.** Les questions de
**procédure** commandent la façon dont tout fil travaille et produit : elles se
tranchent d'abord, et elles sont bloquantes pour le reste. Les questions de
**méthode de lecture** ne portent que sur la façon de lire un texte financier.

---

# A. Procédures et organisation des travaux

*De `CR machine d'amendement 20260917` — passe du 20260911 au 20260917 : livrable
final conforme, sept refabrications, douze fautes en deux jours, dont cinq vues
par quelqu'un d'autre et une par le destinataire après livraison.*

**Le diagnostic du CR tient en trois mécanismes, et le premier produit sept
fautes sur douze :** reconstruire au lieu de comparer ; écrire un contrôle tiré
de ce qu'on a produit au lieu de ce que le destinataire doit trouver ; rejouer un
arbitrage au lieu de le lire.

> **Ces trois mécanismes se sont reproduits à l'identique dans le fil de lecture
> des textes financiers 2026, indépendamment.** Le livrable y a été **reconstruit
> trois fois de zéro** au lieu d'être modifié ; le contrôle de confrontation
> listait ce que le livrable disait avant qu'un contrôle tiré de la pièce ne
> rende le compte des articles manquants ; et deux instructions déjà écrites —
> le format attendu d'un livrable, et la règle qu'un socle de texte n'est pas un
> livrable — ont été contredites alors qu'elles étaient consignées. **Le
> diagnostic ne vaut donc pas pour un projet : il vaut pour la manière de
> travailler.**

> **Un quatrième mécanisme, ajouté le 20260917 par
> `methode/cr_socle_second_cercle_20260917.md` : déclarer au lieu de mesurer.**
> Le mandat de ce fil nommait quatre documents à porter à la table curée de
> l'index. La mesure — la sortie du générateur confrontée à l'index du coffre et
> à la liste des documents du projet — en a compté **quarante-cinq**, dont
> quarante et un que ni le registre, ni un prompt, ni un CR ne mentionnaient.
> C'était le troisième constat du même genre après A-364 et A-381, et les deux
> premiers avaient été traités à l'unité. **La contre-mesure est celle du premier
> mécanisme appliquée en amont : on ne part pas de la liste, on part du delta.**
> Coût de la mesure : une commande et une confrontation de trois listes.

1. **Où vit un arbitrage tranché, et à quel moment il est relu.** Trois endroits
   aujourd'hui — instructions permanentes, documents du projet, mémoire
   transversale — et celui qui a failli est celui qui n'était pas relu au moment
   de produire. Un seul endroit lu en ouverture de tout fil qui produit, ou trois
   avec une règle de préséance écrite ?
   *Donnée du 20260917 : le fil du second cercle du socle a reçu ce fichier dans
   les trois documents nommés par son prompt, et le troisième mécanisme ne s'est
   pas produit. Un seul endroit, nommé par le prompt de chaque fil qui produit, a
   suffi.*
2. **Comment une règle écrite devient un contrôle joué.** Cinq règles sans
   garde-fou côté machine, et le stock ne diminuera pas seul. **Refuse-t-on
   d'inscrire une règle sans son contrôle**, quitte à en inscrire moins ?
   *Donnée du 20260917 : sur le second cercle du socle, l'épreuve des sept
   bouclages neufs a représenté moins d'un cinquième du lot, écriture et mise au
   point comprises. Le surcoût n'a pas été un obstacle.*
3. **Ce qu'est un livrable, et ce qui le laisse partir.** Proposition à
   instruire : aucun livrable ne part sans comparaison à la version précédente,
   contrôle joué sur un déballage tiers, date du jour vérifiée, relecture de ce
   qui est émis. Les quatre sont mécanisables, trois le sont déjà.
4. **La forme du paquet diffusable** — un zip que le destinataire déballe, ou un
   objet qui se déploie seul ? La faute de la procédure d'installation manquante
   n'existe pas dans le second cas.
5. **Le coût de la reprise.** La question n'est pas « comment éviter les fautes »
   mais **« comment une faute coûte une correction et pas une refabrication »**.
   La réponse est probablement dans le premier mécanisme : on ne reconstruit pas,
   on modifie.
6. **Question ajoutée par le fil de lecture 2026.** Un fil long dérive du format
   demandé au fil des tours. **Le format d'un livrable se réinscrit-il en tête de
   chaque passe**, ou se contrôle-t-il à la sortie comme le reste ?

*De `methode/cr_socle_second_cercle_20260917.md` — 20260917*

21. **Une garde qui neutralise une règle doit-elle dire ce qu'elle a
    neutralisé ?** Deux motifs du fichier de construction ne trouvaient plus leur
    classeur — `Depenses_BG` contre `Depenses_2026_du_BG`, `Synthese_Calculs`
    sans accent contre un nom qui en porte deux. **Rien ne cassait** : la règle
    était gardée, le socle se refaisait sans la couche budgétaire ni l'arbre des
    économies, et `make` sortait vert. On ne sait pas depuis quand, et rien ne
    pouvait le dire. C'est le défaut de la question 11 — *un contrôle qui n'a
    jamais rien attrapé ne prouve pas qu'il regarde* — déplacé sur les **gardes**,
    avec cette différence qu'un contrôle aveugle se découvre par une épreuve
    quand une garde silencieuse ne laisse aucune trace. Le corpus en compte
    plusieurs dizaines. *Réponse possible et bornée : un récapitulatif en fin de
    `make` listant les règles sautées faute de pièce — le pendant, côté chaîne, du
    jeu de justes côté contrôle.*
22. **Les garde-fous de la skill du chantier valent-ils absolument, ou portent-ils
    une issue déclarée quand les tenir coûte plus que les enfreindre ?** Le
    premier — *ne pas classer ni qualifier un document non ouvert* — et le refus
    par `controle_index.py` d'un artefact sans famille rendaient, ensemble,
    impossible la seule opération qui sauvait vingt-neuf documents du coffre : les
    porter à la table curée sans les ouvrir. Les ouvrir coûtait une session
    entière pour un lot d'appareil ; les laisser dehors, c'était les perdre au
    prochain `make reindex`. **Tranché en propre par le fil du second cercle** :
    une règle de classement **par adresse** dans `generer_carte.py`, en dernier
    recours, déclarée pour ce qu'elle est — un fait vérifiable sur où le document
    vit, non un jugement de contenu — et que toute ligne de carte contredit. Les
    trois autres garde-fous n'ont pas été éprouvés.
23. **Un nœud de mise en œuvre est-il un artefact du corpus à part entière** —
    son propre fichier, sa propre famille — **ou une section des bilans de
    blocs ?** La question commande le gabarit, qui commande le premier nœud :
    elle se tranche avant, pas pendant. *Argument versé au débat, et rien de
    plus : sept nœuds logés dans les bilans les rendraient illisibles.*
    **Non tranchée. Le fil du second cercle l'avait tranchée en propre dans un
    prompt ; c'était une faute, et elle est retirée.**

---

# B. Méthode de lecture d'un texte financier

*De `methode/cr_lecture_textes_2026.md` — 20260917*

7. **Les montées en charge entrent-elles au gabarit du relevé**, comme colonne, et
   le balayage des formules d'entrée en vigueur rejoint-il les cinq relevés de
   lecture en creux ? *La règle d'analyse est acquise et portée aux conventions ;
   reste son inscription à l'appareil.*
8. **Une mesure à deux jambes — une dans chaque texte financier — porte-t-elle un
   identifiant traversant, ou deux lignes liées par un renvoi ?**
9. **L'exposé des motifs gagne-t-il un second usage** — source d'aveu opposable, à
   côté de son statut d'indice que fixe A-230 ?
10. **Les marques de poids d'un livrable de lecture sont un jugement non outillé.**
    Contre-lecture aveugle, ou pas de vérification sur ce point ?

*De `methode/cr_confrontation_20260916.md` — 20260916*

11. **Le jeu de justes devient-il obligatoire** à côté du jeu de fautes, pour tout
    contrôle neuf ?
    *Appliquée avec la valeur retenue le 20260917 sur les sept bouclages du
    second cercle du socle — `appareil/epreuve_controle_socle.py`, quatorze fautes
    et sept justes —, et inscrite à `methode/grille_lecture_budgetaire.md`, là où
    la règle est lue. **Le cas rend une donnée nette : le jeu de justes a servi et
    le jeu de fautes non.*** Les quatorze fautes ont toutes levé leur code du
    premier coup — elles ont confirmé, elles n'ont rien appris. Écrire les justes
    a obligé à répondre à « qu'est-ce qui a le droit de bouger sans que rien ne
    sonne ? », et cette question a fait apparaître, à l'onglet `Perdants`, que
    deux natures de lien s'y cachaient — une partition qui épuise sa tête, un
    sous-ensemble qui n'épuise rien. Un bouclage naïf aurait sorti en échec un
    dénombrement croisé, et on aurait « corrigé » le classeur. *Reste à valider ou
    à révoquer par l'auteur : un fil ne porte pas en validé ce que l'auteur n'a
    pas dit.*
12. **La précision du verdict entre-t-elle au gabarit du relevé**, et un taux se
    publie-t-il sans elle ?
13. **Un repère de bloc est-il un repère** au sens de la skill `confrontation` ?
14. **Scinde-t-on `confronter_lecture.py`** en socle générique et recettes par
    livrable ?
15. **L'égalité reste-t-elle à zéro tolérance ?** La tolérance existe déjà de
    fait, sur deux recettes, et elle n'est pas écrite.
    *Donnée du 20260917 : les sept bouclages du second cercle du socle emploient
    une tolérance **calculée** depuis le nombre de lignes sommées — `n × 0,05`,
    parce que le classeur arrondit chaque colonne au dixième à l'affichage — et
    non posée. Une tolérance posée à la main se remonte pour faire tomber un
    compte ; une tolérance calculée ne le peut pas.*
    **Seconde donnée du 20260917, et elle coûte cher.** Le bouclage « taxes +
    crédits → ligne » porte une tolérance **posée à 0,09 Md€**, l'une des deux
    que ce fichier disait « de fait, et pas écrites ». Elle a masqué pendant tout
    ce temps **trois lignes de taxe affectée manquantes** au rattachement du CNC
    — le Centre national de la musique et l'association pour le soutien du
    théâtre privé, 44,4810514 M€ sur douze lignes. Le bouclage sortait à
    −0,077667 Md€ et passait ; à 0,05 il serait sorti. *La tolérance posée n'a
    pas seulement laissé du jeu : elle a laissé passer une omission de source.*
    À l'inverse, une tolérance à 0,05 sec ferait tomber « dont France Travail »
    à −0,066167, où l'écart est un vrai arrondi d'affichage sur deux cellules
    saisies au dixième — donc `2 × 0,05`. **La bonne tolérance n'est ni 0,09 ni
    0,05 : c'est le compte des cellules arrondies qui entrent dans la
    comparaison.** Reste à l'écrire.
16. **Le bordereau ne bloque rien — et ensuite ?** Le corpus n'a aucun seuil de
    diffusion.

*De `methode/cr_socle_second_cercle_20260917.md` — 20260917*

24. **L'onglet `Capitalisation` s'importe-t-il au socle avec son bouclage, ou se
    cite-t-il sans ?** Il porte l'horizon de sept ans de la sortie des
    fonctionnaires, et il est le dernier onglet du classeur de calculs que le
    second cercle n'a pas importé. L'importer est un lot d'appareil sur le modèle
    des sept bouclages neufs ; le citer sans bouclage laisse le terme `estimé`.
    *Argument versé au débat : un nœud bâti sur un chiffre sans garde-fou est un
    nœud qu'il faudra refaire.* **Non tranchée, pour le même motif que la 23.**

*De `livrables/ecart_classeurs_20260917.md` — 20260917*

26. **Le vocabulaire des classeurs a changé dans quatre classeurs sur six ; le
    corpus suit-il, ou tient-il une table de concordance ?** « Gage CSG »
    devient « Economie à horizon 1 an », « économie pérenne en sus » devient
    « Economie supplémentaire », « effet macro » devient « solde PO »,
    « suppression immédiate » devient « champ non indispensable », « CI unique »
    devient « aide fondamentale universelle », « niches supprimées » devient
    « niches restituées ». **Les valeurs sont identiques à l'octet** : c'est une
    requalification de ce que le nombre est, non un nombre neuf.
    `methode/grille_lecture_budgetaire.md` écrit l'ancien vocabulaire en toutes
    lettres, colonne par colonne. Réécrire la grille ou porter les deux
    vocabulaires ? *Argument versé au débat et rien de plus : « effet macro » et
    « solde PO » ne disent pas la même chose du même nombre, et c'est un
    jugement de fond, pas un renommage.*
27. **Les deux écarts entre l'hypothèse annoncée et l'hypothèse appliquée sont
    refermés par le classeur ; le corpus les referme-t-il ?** La grille relève
    que « la doctrine annonce 3 % de rendement du patrimoine quand le classeur
    applique 2,9 % » et qu'« elle promet 20 000 € par foyer, ce qui suppose
    600 Md€ d'actifs, quand le classeur en valorise 636,1 ». Les pièces du
    20260917 appliquent **3 %** et valorisent **606,972666 Md€**. Le premier
    écart est clos, le second réduit de 36,1 à 6,97 Md€. *Le fil d'écart ne
    referme rien : c'est un texte de fond.*
28. **La part budgétaire d'une économie se réécrit-elle, ou redevient-elle un
    résidu ?** Le bloc des postes nommés de l'onglet `Synthèse` du classeur des
    dépenses disparaît ; **18 de ses 22 postes ne se retrouvent nulle part** aux
    sept classeurs. C'était la seule pièce du corpus qui écrivait cette part, et
    la grille le dit : « Elle se déduisait par soustraction. Un résidu n'est pas
    une source. » Trois des cinq bouclages tombés se relisent à leur nouvelle
    adresse ; **deux ne se recomposent pas, et c'est mesuré** : « sur FrComp. »
    434,071252 M€ et « sur culture » 516,998084 M€ ne sont atteints par aucune
    combinaison à un ou deux termes des 2 810 valeurs distinctes du socle, et le
    projet annuel de performance ne peut pas les rendre — la subvention y est à
    la maille du programme, et les deux programmes sont partagés, **103 entre
    quatre opérateurs et 334 entre six**. Ils ne sont pas non plus fondus dans
    « Autres » : le nouveau « Autres » à horizon 1 an, 2 446,983897 M€, plus
    l'Anah, 99,3915, font exactement l'ancien « dont autre », 2 546,375397. **Ils
    sont sortis, pas absorbés.** Pour fermer : le budget initial 2025 de France
    Compétences — pièce hors corpus, déjà nommée par A-113 — rendrait le premier
    vérifiable ; le second demande de savoir ce que « sur culture » agrégeait, et
    l'auteur seul le sait. **Mesure reprise après correction des taxes du CNC :**
    la ligne recompose désormais 0,749816 Md€ au lieu de 0,705335, et l'écart au
    classeur tombe de 0,594665 à 0,550184 Md€. « Sur culture », 516,998084 M€,
    n'est toujours pas ce résidu — il en diffère de 33,186 M€.
29. **`Manifeste` et `Perdants` disparaissent sans équivalent : la ventilation
    gagnants / perdants sort-elle du classeur ?** `Perdants` portait le
    dénombrement des populations et des perdants à 1 an et à 3 ans ; `Manifeste`
    portait la ventilation des baisses de dépense par catégorie. S15 n'a plus de
    source. Deux entrées de `REF_chiffres` — 236 Md€/an et 30 Md€/an — citent
    `Manifeste` comme source.
30. **La doctrine reprend-elle 82,5 et 53,4 ?** L'origine des +4,8 et +13,9 Md€
    est mesurée et la règle est arrêtée : la masse salariale compte en totalité,
    30 % en année 1 et 70 % au solde (voir `S17` à la grille). Reste la
    conséquence éditoriale : le manuscrit, les fiches et le site portent 77,7 et
    39,5. Le total général ne bouge pas — 236,054667 Md€ —, **ce sont les deux
    totaux de tête qui bougent sans lui.** *Question ouverte : reprend-on les
    aval d'un coup, ou au fil des régénérations ?*
    **Mesuré le 20260923 et faux tel quel** (`livrables/releve_passe_825_534_20260923.md`,
    `methode/cr_passe_825_534_20260923.md`) : **ni le manuscrit, ni les fiches, ni
    le site ne portent 77,7 ou 39,5**, sous aucune forme, et `REF_chiffres`,
    `REF_doctrine` et `positions` non plus — 57 fichiers d'aval balayés, zéro
    occurrence. Les 48 occurrences du corpus sont toutes dans la méthode, le
    registre, le constat antérieur ou `appareil/leviers_collocs.py`. **La
    conséquence éditoriale n'existe pas ; la question se referme par la mesure, et
    son énoncé est à retirer ou à corriger sous peine de faire rejouer une passe
    vide.**
31. **S16 porte-t-il encore sur le même millésime que les quinze autres ?** Le
    classeur de la dépense d'éducation est le seul des sept antérieurs à n'avoir
    pas de successeur au 20260917.

*De `livrables/reconfirmation_chiffres_20260921.md` — 20260921*

32. **Onze entrées du référentiel prennent une référence pour une grandeur : on
    les retire, on les requalifie, ou on les laisse ?** `N-e35-2`, `N-e38-1`,
    `N-e71-1`, `N-e74-1`, `N-e79-2`, `N-e83-2`, `N-e99-2`, `N-e106-1`,
    `N-e106-2`, `N-e135-1`, `N-e135-4` sont adossées à une note de fin du
    manuscrit et portent une valeur qu'aucun chiffre de cette note ne porte : un
    millésime (2021, 2022, 2023, 2024, 2025), un numéro de rapport (1754), un
    rang de classement (36e), un compte (112). **Le manuscrit fait foi : ce sont
    des dates et des renvois, pas des grandeurs.** Le relevé automatique de
    `generer_ref_chiffres.py` ne sait pas les distinguer, et elles sortent en
    confiance 3 — `strate1` —, c'est-à-dire au plus haut niveau de confiance du
    corpus. *Deux voies : une règle d'exclusion au générateur, qui vaut pour
    l'avenir, ou une liste d'exclusions écrite à la main dans
    `sources_chiffres.py`, qui vaut pour ces onze. La première est de la
    tambouille ; la seconde inscrit un jugement de fait, donc elle revient à
    l'auteur.*
33. ~~**Le référentiel des faits doit-il couvrir le manuscrit ?**~~
    **Tranché par l'auteur le 20260921 : oui, tout chiffre du livre.** Porté au
    registre des arbitrages. Ce que la décision ouvre, et qui n'est pas une
    question mais un travail : 225 chiffres du manuscrit sur 311 sont hors
    référentiel, et six grandeurs de notes de fin — `e40`, `e48`, `e60`, `e61`,
    `e103`, `e114` — échappent au détecteur d'`extraire_notes.py`. Le corps du
    livre n'est source d'aucune des trois provenances de
    `generer_ref_chiffres.py` : **le générateur ne peut pas produire ce
    périmètre en l'état.**

*De `livrables/rapprochement_proto_20260921.md` — 20260921*

34. ~~**Le proto contredit le manuscrit sur la sortie des fonctionnaires.**~~
    **Tranché par l'auteur le 20260921 : le livre et ses annexes prévalent.** Le
    proto vient de `Données_Résolution_0112.docx`, antérieur aux classeurs 0819
    comme à ceux du 0910 : là où il diverge, il est périmé. On retient 580 000
    postes et −10 % des effectifs. *Écrit et joué le jour même* : le groupe
    `postes publics facultatifs supprimés` porte `P-D-102` et un bloc
    `arbitrage`, `F7` reste vert, l'écart reste visible au contrôle. Le patch est
    à `methode/paquet_depot_rapprochement_20260921.md` et **dû au dépôt**.
35. ~~**L'arbitrage du 20260825 sur les dépenses de retraite se propage-t-il ?**~~
    **Tranché par la même règle, le 20260921 : oui.** Le taux de couverture du
    livre est 69,3 % et son déficit spontané 125 Md€ ; les 73 % et les 106 Md€ du
    proto sont périmés. *Ce que la décision ouvre, et qui n'est pas une question
    mais un travail* : **les 125 Md€ du corps du livre ne sont entrés dans aucune
    entrée du référentiel**, donc la contradiction de `P-D-067` ne peut toujours
    pas s'écrire à `MEME_QUE`, qui apparie des entrées. Elle s'écrira quand le
    corps du livre y entrera — c'est la question 33, déjà tranchée, dont le
    travail reste entier.
36. ~~**Deux nomenclatures dénombrent les mêmes structures.**~~ **Tranché par la
    même règle, le 20260921 : le livre fait foi**, donc le corpus retient son
    décompte des 1 104, dont 434 agences nationales. Les 431 opérateurs de la
    liste du PLF 2026 restent du contexte de sous-jacent, citables comme source
    de source. **Aucun groupe `MEME_QUE` n'est écrit** : les deux têtes ne
    portent pas le même objet, et une discordance arbitrée y serait un artifice.

*De `methode/cr_lot_C_20260917.md` — 20260917, portées par le fil d'application*

*De `methode/cr_passe_825_534_20260923.md` — 20260923*

37. **Les deux sous-lignes de l'arbre des économies que `REF_doctrine` porte
    encore à l'état antérieur se reprennent-elles ?** `D2-2-1-s3` « France
    Travail » écrit **2,7 Md€** quand le classeur du 20260917 porte 5,254667 ;
    la ligne « autres » des opérateurs écrit **2,8** contre 2,745333. Les deux
    se propagent à `positions`, `REF_chiffres`, l'arbre et l'inventaire.
    *C'est du fond : y porter un chiffre neuf n'est pas de la tambouille.*
38. **`R-D7-2-2-e2` de `REF_chiffres` contredit un arbitrage déjà pris.** Elle
    écrit `636,1 Md€ × 2,9 % = 18,4469` et, en `note_sourcage`, « le classeur
    applique 2,9 % là où la doctrine annonce 3 % » et « la promesse est prudente
    de 36 Md€ » — quand `A-421` (question 27) a clos les deux écarts : **3 % de
    rendement, 606,972666 Md€ valorisés, marge de 6,97 Md€**. La correction se
    fait à `appareil/sources_chiffres.py`, **voie `depot`, non poussable depuis
    Cowork (A-393)**. *La seule reprise que le mandat de la passe autorisait sans
    arbitrage neuf.*
39. **Le flux des documents hors index n'est pas traité, seulement son stock.**
    Le fil du second cercle a porté 45 documents à la table de l'index le
    20260917 ; `controle_index.py` en compte **34 de plus le 20260923**, dont
    29 produits depuis — livrables, CR, fragments, paquets de dépôt, prompts de
    fil. *Un fil porte-t-il sa propre production à `generer_index.py` avant de
    clore, ou la table se régénère-t-elle par balayage ?*

---

# Tranché le 20260917 par l'auteur — à porter au registre des arbitrages

*Ces trois arbitrages sont pris. Ils restent ici, et non à `methode/arbitrages.md`,
tant que la question 17 n'a pas donné sa règle de concurrence : les y porter
depuis un fil qui a restauré un état antérieur du registre reproduirait
exactement la divergence du 20260916. **Le premier fil qui écrit au registre
après la question 17 les emporte.***

**Le bouclage d'ensemble n'est pas un objet du corpus.** Le programme assume de
ne boucler qu'au total, jamais bloc par bloc. `B-05` et `B-07` restent
déséquilibrés et le disent ; aucune pièce ne sera écrite pour dire ce qui finance
quoi. *Conséquence pour le lot C : les deux bilans sont clos en l'état, et le
relevé des bilans déséquilibrés est un état définitif, non une liste de travaux.*
*(ancienne question 18)*

**Le nœud de mise en œuvre existe comme objet, et on en écrit un seul d'abord.**
Le gabarit se rédige, puis se remplit sur la sortie des fonctionnaires — le seul
nœud du premier lot. Les six autres attendent ce que ce premier aura coûté. Sept
reste une proposition, pas un décompte. *(ancienne question 19)*

**Un terme qu'aucune pièce du corpus ne porte est à produire, non absent
définitivement.** Le verdict `absent` du relevé de comblement ouvre un travail ;
il ne clôt rien. Le seul terme dans ce cas au 20260917 — la reprise par l'État
des missions de solidarité départementales, que `B-03` suppose — est un nœud de
mise en œuvre, et il rejoint la file derrière la sortie des fonctionnaires.
*(ancienne question 20)*

**Les fichiers cumulatifs du coffre s'écrivent par fragments datés.** Un fil ne
les écrit plus : il dépose `methode/fragments/<cible>/<AAAAMMJJ>-<fil>.md`, et
`appareil/fragments.py` assemble. L'historique, avant la ligne de marque, est
repris verbatim et ne se réécrit jamais ; la queue se régénère depuis les
fragments, triés par date puis par fil. **L'assemblage est idempotent** : deux
fils qui l'exécutent produisent le même octet. C'est ce qui rend le travail en
parallèle possible, et c'est la seule des trois voies où la fusion est mécanique.
Éprouvé sur six cas — historique intact, coexistence de deux fils, idempotence,
fragment tardif, ordre de dépôt indifférent, double dépôt refusé. *(ancienne
question 17)*

*Appliqué le jour même* : `journal.md` et `arbitrages.md` restaurés à 247 518 o
et 292 686 o — les deux contributions du 20260916 sont intactes —, assemblés avec
le fragment de ce fil, reversés à 248 841 o et 294 586 o. La tête est identique à
l'octet avant et après.

> **Limite constatée le 20260917 par le fil du second cercle du socle.**
> `appareil/fragments.py` n'est pas au clone : c'est une dette du fil
> d'application. **Un fil qui ne l'a pas ne peut que déposer, pas assembler.** Ce
> fil a déposé `methode/fragments/arbitrages/20260917-socle.md` et
> `methode/fragments/journal/20260917-socle.md` ; `journal.md` et `arbitrages.md`
> au coffre ne les portent pas encore. C'est un état, pas un oubli, et le premier
> fil qui disposera du module les emportera. *La voie tient — aucune concurrence
> d'écriture, aucun écart d'octets — mais elle n'est complète qu'une fois le
> module poussé.*

**Ordre des lots — à reprendre par le fil chef de file. Ce fichier ne le porte
plus.** Deux fils l'y ont reformulé en deux jours, et les deux fois la
reformulation était fausse. Ce qui est établi, et rien de plus :

- le second cercle du socle est **fait** (`methode/cr_socle_second_cercle_20260917.md`) ;
- l'écart des classeurs mis au propre est **fait** (`livrables/ecart_classeurs_20260917.md`) ;
- **la sortie des fonctionnaires est un bloc juridique : elle se résout après
  les parties faciles de la liasse, pas avant.** *Énoncé par l'auteur le
  20260917.* C'est une position relative — elle ne dit pas par quoi on commence,
  et **elle ne se convertit pas en plan**.

> **Règle qui se rappelle, et que ce fil a enfreinte deux fois :** l'ordre des lots
> est de l'auteur. Un fil rend son état et s'arrête ; il ne se donne pas son
> successeur, et il ne déduit pas le lot suivant d'une remarque sur un ordre
> relatif.

> **Précision du 20260917, et elle corrige une faute de ce fil-là.** Le fil du
> second cercle a écrit `methode/prompt_fil_noeud_mise_en_oeuvre.md` et y a
> tranché deux questions de fond. **Ce n'était pas à lui** : l'ordre des lots est
> de l'auteur, et **c'est au fil chef de file de dicter la suite** — quel fil
> s'ouvre, sous quelle forme, avec quel mandat. Le document est ramené à ce qu'il
> est : de la matière préparatoire, marquée *proposé, non validé*, et ses deux
> arbitrages sont ressortis en questions 23 et 24. *Un fil de travail inscrit et
> s'arrête ; il ne se donne pas son successeur.*

---

# Dette d'appareil, pour mémoire

Ces pièces sont de voie `depot` et **ne sont pas poussées** : un fil Cowork ne
peut pas pousser (A-393). Elles attendent une session claude.ai/code.

- `appareil/index_mesures.py` — l'index des mesures par article
- `appareil/socle_plf_texte.py` — correction `lignes_brutes` sur l'alinéa de
  tableau, et ses deux dérivés PLFSS
- les deux modules de confrontation, au paquet
  `methode/paquet_depot_confrontation_20260916.md`
- `appareil/controle_blocs.py` — série `D` ajoutée le 20260917, et
  `appareil/epreuve_controle_blocs.py`, son jeu de fautes et son jeu de justes ;
  avec `appareil/rendre_blocs.py` et `appareil/plier_lot.py`, dus depuis le
  20260916 ; et `appareil/fragments.py`, qui porte l'écriture par fragments et
  son épreuve. Les cinq sont au paquet
  `methode/paquet_depot_application_20260917.md`.
- **sept pièces du second cercle du socle**, au paquet
  `methode/paquet_depot_socle_20260917.md` : `socle_budgetaire.py`,
  `controle_socle.py`, `epreuve_controle_socle.py` (neuf), `generer_index.py`,
  `generer_carte.py`, le `Makefile`, et `trois_colonnes_regle_dor.py` que le
  coffre porte comme document depuis le 20260908. **Mesurées par `make coffre`,
  non déclarées de mémoire** — `D1` 5, `D2` 1, `D3` 1.

- `appareil/socle_0910.py` — l'adaptateur d'adresses des classeurs mis au propre
  du 20260917. Il ne déplace que des adresses, là où la confrontation cellule à
  cellule a prouvé que la matière est identique ; il ne change aucun calcul.
  **Tant qu'il n'est pas au dépôt, le socle ne se régénère pas sur les pièces du
  20260917.** Reste à trancher au fil qui poussera : pièce séparée, ou
  `socle_budgetaire.py` portant les deux jeux d'adresses avec le millésime en
  paramètre. *Tambouille — ne remonte pas à l'auteur.*

**Deux modules déclarés de voie `depot` par l'index et absents du clone** —
`appareil/plier_paquet.py` et `appareil/controle_projection.py`. Ce n'est pas
une dette d'écriture mais une perte : ils se réécrivent ou se retrouvent, et
leur sortie versée fait spécification. Constat rejoué mécaniquement le 20260917
par `restaurer.py`, qui compte 93 artefacts de voie `depot`, 88 présents au
clone, 5 absents.

**~~Quatre documents sont au coffre et absents de l'index.~~ Il y en avait
quarante-cinq, et ils sont portés** *(20260917, second cercle du socle)*. La
mesure a dit la taille que le registre ne disait pas : vingt-neuf absents de la
table curée **et** de l'index, seize à l'index sans être à la table — donc perdus
au prochain `make reindex`. Les quarante-cinq sont à `appareil/generer_index.py`.
L'index passe de 252 à 291 artefacts, `controle_index.py` sort zéro anomalie
bloquante, et `generer_carte.py` porte désormais une règle de classement par
dossier pour que le cas ne revienne pas — voir la question 22. *La pièce reste
due au dépôt tant qu'un fil claude.ai/code ne l'a pas poussée.*

# Chantiers de fond ouverts, hors procédure

*Du CR machine d'amendement, § 6 — ils ne sont pas des arbitrages mais des
travaux dus.*

- la grille des portes du domaine des lois de financement n'est pas relevée :
  tout verdict de loi de financement plafonne à `plaidable` ;
- le dossier de mesure n'est pas le livrable de la chaîne, donc les treize
  contrôles du contrat ne se jouent sur rien ;
- neuf des treize contrôles ne sont pas outillés ;
- aucun véhicule autre que la loi de finances n'est éprouvé sur un banc ;
- les crédits par mission — état B — restent hors de la zone d'extraction du
  socle du texte financier.
