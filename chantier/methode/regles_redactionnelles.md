# Règles rédactionnelles — révision constitutionnelle
## Version synthétique — 30 juillet 2026

---

## Principes de rédaction

**Rédactions positives.** Toujours formuler ce qu'une institution peut ou doit faire, jamais ce qu'une autre ne peut pas faire. « Il revient au seul Parlement » plutôt qu'une interdiction visant nommément le Conseil constitutionnel.

La règle vaut pour **tous les livrables**, normatifs comme rédactionnels — exposés des motifs, présentation, notes. Écrire ce que la règle fait, non ce qu'elle ne fait pas. Bannir les antithèses d'ouverture du type « X ne se décrète pas, il s'organise » et les tours « ne tient pas à… mais à », « ni… ni ». Entorse tolérée lorsque la négation porte un manquement constaté et non une règle. Deux exceptions pleines : la section « ce que la proposition laisse intact » d'un exposé des motifs, où la négation porte l'engagement de non-modification, et la restriction « ne… que », qui énonce un régime d'exception.

**Pas de virgule devant une conjonction de coordination** — et, ou, mais, ni, car, or, donc. Seule exception : la clôture d'une incise, « …des exercices ultérieurs, et arrête leur emploi ». Contrôle automatisable : `re.findall(r',\s+(?:et|ou|mais|ni|car|or|donc)\b', texte)`.

**Pas de point-virgule dans le texte normatif.** Les points-virgules des énumérations légistiques d'un dispositif modificatif — 1° … ; 2° … — restent en revanche l'usage.

**Apostrophes typographiques** partout, jamais d'apostrophe droite. Guillemets français avec espaces insécables. La ponctuation du texte cité se place avant le guillemet fermant ; pour un mot isolé cité, la ponctuation de la phrase enclosante se place après. Les deux règles coexistent et ne se vérifient que sur le rendu.

**Amendements minimaux.** Ne changer la forme des phrases que si c'est indispensable. Préférer la suppression à la reformulation. Quand une phrase existante fonctionne, on la garde.

**Cohérence de la hiérarchie des normes.**
— Constitution : principes et bornes
— Loi organique : mécanique et paramètres
— Loi ordinaire : application
Ne pas faire descendre dans la Constitution ce qui relève de la loi organique, ni l'inverse.

**Pas de redondance entre niveaux.** Si un principe est dans la DDHC, l'article 34 n'a pas à le recopier — sauf intention délibérée de filiation textuelle, qui est une technique constitutionnelle classique et assumée.

**Renvois organiques sobres.** Un renvoi à la loi organique sans précision de contenu suffit — la loi organique peut elle-même déléguer. Inutile de constitutionnaliser les modalités.

**Obligations procédurales directes.** Sur le modèle de l'article 40 : une phrase sèche, sans renvoi organique. Les assemblées développent leurs propres modalités de contrôle.

---

## Règles sur les formulations

**Singulier pour les interdictions individuelles.** Quand on interdit quelque chose acte par acte (charge par charge, ressource par ressource), le singulier ferme la brèche des compensations croisées. Le pluriel autorise implicitement la compensation par agrégation.

**« Soit… soit » pour les énumérations d'irrecevabilité.** Structure d'origine de la Constitution de 1958 — plus lisible que « ou », fidèle au style constitutionnel.

**Ordre logique des membres d'une énumération.** Du plus grave au moins grave, du plus fondamental au plus procédural. L'ordre dit quelque chose de politique — il ne doit pas être arbitraire.

**Trois phrases pour poser une compétence exclusive :**
1. Ce que la loi fait
2. Que c'est sa compétence exclusive
3. L'obligation procédurale qui en découle
Ne pas inverser 2 et 3.

**Plafonds et bornes intégrés dans les articles de domaine.** Un plafond fiscal a sa place dans l'article qui définit les impositions, pas dans un article nouveau flottant. La borne est inséparable de la compétence qu'elle limite.

**Distinguer unité et universalité.** L'unité désigne un acte unique — une seule loi de finances portant l'ensemble. L'universalité désigne la non-affectation et la non-contraction : aucune ressource n'est affectée à une dépense, tout transite par le budget. Les deux principes sont distincts et leur confusion est une faute de fond. Elle est peu visible au niveau constitutionnel, où l'article 47 ne porte que l'universalité formelle. Elle devient centrale au niveau organique. Les cinq principes budgétaires coexistent : annualité, unité, universalité, spécialité, sincérité.

**« Contribution commune répartie entre tous les citoyens. »** Reprise de l'article 13 DDHC — assumée, pas maladroite. Pose l'universalité de l'assiette sans promettre une contribution effective identique pour tous.

**Asymétries délibérées.** Quand deux situations semblables ont des régimes différents (ex. nationalisation vs privatisation), l'asymétrie doit être visible dans le texte et justifiée par la gravité respective.

---

## Règles sur le Conseil constitutionnel

**Le bloc de constitutionnalité est figé par la loi organique, pas par un article constitutionnel ad hoc.** Le Parlement statuant par loi organique reconnaît de nouveaux principes constitutionnels — formulation positive.

**La QPC est limitée aux textes expressément listés.** Supprime les PFRLR et OVC d'origine prétorienne. Le champ du contrôle est défini par les textes, pas par le juge.

**Le dialogue constitutionnel est structuré, pas unilatéral.** Le Parlement peut préciser l'interprétation d'une décision du CC par loi organique à la majorité des 3/5 — pas de clause nonobstant. La voie de recours est organisée.

---

## Règle sur les droits sociaux et le préambule de 1946

**Le préambule de 1946 n'est pas une source de droits opposables dans ce projet.** Son intégration au bloc de constitutionnalité est une construction prétorienne (décision CC n° 71-44 DC du 16 juillet 1971), non un choix du constituant de 1958. Ce projet ne lui reconnaît aucun effet normatif autonome au-delà de ce que la loi organique désigne expressément.

**Les droits sociaux sont déterminés par le Parlement seul, dans la seule mesure qu'il fixe.** L'étendue de la protection de la santé, de la retraite, de la famille ou de toute autre protection sociale est une compétence législative, pas un droit constitutionnel à contenu prédéfini. Le Parlement peut la limiter à des périmètres étroits (urgences vitales, handicap, etc.) sans que cela constitue une inconstitutionnalité.

**Ne jamais invoquer le préambule de 1946 comme contrainte sur une rédaction.** Si une rédaction soulève une tension avec l'alinéa 11 (protection de la santé), l'alinéa 13 (égal accès à l'instruction) ou tout autre alinéa, la réponse est : le Parlement tranche, le juge ne peut pas substituer son appréciation à celle du législateur sur l'étendue du droit social, dès lors que le mécanisme de dialogue CC/Parlement (art. 62 révisé) est opérationnel.

**Implication pratique pour les rédactions :** aucun plancher de remboursement, aucun niveau minimal de prestation, aucune « protection essentielle » ne doit être inscrit dans la loi organique au titre d'une exigence constitutionnelle. Ces niveaux relèvent de la loi ordinaire et du vote annuel de la loi de finances.

---

## Règles sur la normalisation budgétaire des dépenses automatiques (AM, retraites, prestations)

**Les dépenses à droits ouverts sont des crédits limitatifs comme les autres.** La distinction entre crédits évaluatifs (dépenses automatiques) et crédits limitatifs est abandonnée pour les dépenses de protection sociale. Elles sont inscrites en loi de finances comme tout programme, avec un plafond voté.

**Mécanisme de réserve de précaution dédiée.** Pour les programmes à forte volatilité infraannuelle (assurance maladie notamment), une fraction des crédits — calibrée sur la volatilité historique du programme — est mise en réserve dès le début d'exercice. Cette réserve est mobilisable par décret sans collectif tant qu'elle n'est pas épuisée. Elle joue le même rôle que la réserve de précaution générale, avec un taux adapté.

**Tiers payant = les prestataires sont des fournisseurs de l'État.** Les médecins, hôpitaux, pharmaciens et autres prestataires de soins avancent les prestations et portent une créance sur l'État, remboursée sur crédits votés. Leur situation juridique est celle d'un titulaire de marché public ou d'un fournisseur ordinaire : la créance est réelle, son règlement est conditionné à l'existence des crédits. Ce cadrage est cohérent avec la séparation ordonnateur/comptable et le visa a priori renforcé.

**Capacité réglementaire de modulation des taux en cas d'épuisement des crédits.** Si la réserve de précaution est consommée et que les crédits du programme sont sur le point d'être épuisés, un décret peut abaisser les taux de remboursement pour la durée restante de l'exercice. La loi de finances fixe le taux plafond ; le décret peut descendre en dessous. Ce n'est pas une rupture du droit à remboursement — c'est un ajustement du niveau de prise en charge, dans le cadre de la compétence réglementaire normale.

**Pas de plancher organique ni constitutionnel.** L'étendue minimale de la couverture est une décision politique annuelle du Parlement, pas une contrainte juridique supérieure.

---

## Règles de l'exposé des motifs et de la proposition de loi

Ces règles ne figurent pas ici mais dans la skill `redaction-legistique`, à
`references/structure_ppl.md` : répartition des fonctions entre l'assise, les chapeaux de
division et les commentaires d'articles ; règle du nommage — dire ce que l'article fait,
c'est nommer le mécanisme et non restituer la disposition ; verbes de commentaire révise,
abroge, insère ; ordre par hiérarchie d'importance ; maquettes de page de titre par
assemblée ; descripteurs de travail et leur retrait à la passe de dépôt ; autorités
citables, fiche 3.1.1 du guide de légistique, décisions n° 2009-579 DC et n° 2023-13 FNR,
CE 12 mars 1975 Sieur Bailly.

---

## Format trois colonnes

**Colonne A** : texte actuel, résumé fidèle, parties supprimées soulignées.
**Colonne B** : réforme visée, courte, avec flèche ↳.
**Colonne C** : texte tel qu'il sera après révision — ajouts en gras, suppressions absentes. Jamais d'instructions méta. Notes en bas pour signaler ce qui a changé.

---

## Procédure de travail

**Formats de travail.** Le texte se rédige et se valide en **markdown**, les tableaux de révision en **HTML** trois colonnes. Le **docx** est un export terminal, destiné aux tiers, produit par la skill `impression-docx` — jamais pour un usage interne.

**Deux HTML horodatés par session** : `Constitution_3col_YYYYMMDD.html` et `LOLF_3col_YYYYMMDD.html` — uploadés dans le projet après chaque session, ils sont les points de vérité courants pour chacun des deux chantiers.

**Les documents joints au projet sont la référence à date pour tous les fils.** Un fil produit dans `/mnt/user-data/outputs`, l'utilisateur téléverse, le document devient la référence. Rien n'est durable avant téléversement : `/mnt/project` est en lecture seule et `/mnt/skills/user` n'est pas persistant.

**Un fil par phase de travail**, non par document. Chaque fil met à jour les documents que sa phase touche et signale les mises à jour dues aux autres.

**Les paramètres entre crochets [X] sont des décisions politiques à prendre**, jamais des chiffres inventés. Ils sont signalés dans chaque document par une note.

**Une conversation par chantier.** Finances publiques, collectivités, institutions — chaque chantier dense mérite sa propre conversation pour préserver la qualité du contexte.

---

## Règles des livrables de diffusion

Ajoutées le 7 août 2026 par le fil « Sorties pédagogiques ». Elles valent pour
les fiches mesure, les Q&A, les argumentaires et toute sortie destinée à un
lecteur extérieur au projet. Les règles de rédaction normative qui précèdent
demeurent inchangées.

### Préséance des chiffres

Le manuscrit prime. Un arrondi du manuscrit l'emporte sur une estimation du
tableau portant sur le même objet : le manuscrit reste sobre pour rester
accessible. Le tableau fournit le détail que le manuscrit tait — niveaux
intermédiaires, ressource engagée, repères d'ordre de grandeur, financement.
Chaque ligne chiffrée porte son origine. Un écart entre les deux sur un même
objet se résout en faveur du manuscrit et se signale hors livrable.

### Nouveauté et acquis

Une disposition que le projet introduit se présente comme une nouveauté, jamais
comme un état de fait. La rubrique « ce que la mesure ne change pas » n'accueille
que ce qui subsiste réellement du droit en vigueur. Confondre les deux fait
passer une réforme pour une évidence et désarme le livrable.

### Les perdants

Le manuscrit ne nomme les perdants qu'en creux : c'est un choix d'écriture, non
une donnée. Les livrables de diffusion, eux, les nomment. Chercher le perdant
direct, croiser l'onglet Perdants du classeur, distinguer la perte durable de la
perte transitoire, énoncer sans dramatiser ni euphémiser. Lorsque la perte est
l'objet même de la mesure, le dire. Un chiffre de perdants valant pour le plan
d'ensemble ne se porte pas sur une mesure particulière tant qu'il n'est pas
ventilé.

### Adresse et vocabulaire

Pas de vouvoiement : ni le contradicteur ni le lecteur ne se prennent à partie.
Employer « on », « nous », « chacun », ou l'impersonnel. Pas de soustraction
seule : dire ce qui est rendu, ouvert, rendu possible.

Vocabulaire arrêté par le plan stratégique réseaux : restitution plutôt que
baisse d'impôt, bureaucratie plutôt que fonctionnaires, intermédiaires plutôt
qu'administration, ce qu'on nous prend plutôt que prélèvements obligatoires,
ceux qui produisent plutôt que les contribuables, on a vérifié plutôt qu'il est
évident que.

Cinq postures : humilité, clarté, sincérité, optimisme — aucun livrable ne se
termine sur un problème —, colère froide, respect des personnes.

### Appareil interne

Identifiants, statuts, strates, axes, leviers, paramètres, effets, renvois,
noms d'onglets et ancres du manuscrit restent hors du corps de tout livrable
destiné à l'extérieur. Ils se déposent en bloc de pied, ouvert par `[interne]`,
retirable d'un trait pour diffusion.

### Exports

Le livrable de travail est le format source, markdown ou HTML. La génération de
docx, PDF et PNG attend une consigne explicite et se fait en une passe, à la
fin, une fois le contenu arrêté.

---

## Reprises du 20261007 — légistique des textes financiers

Inscrites par le fil d'intégration de `methode/reprise_20261007.md` (§ 2 et § 3). Elles
complètent les principes de rédaction ci-dessus et priment sur tout usage antérieur contraire.
Source : digestion du guide de légistique du SGG, `reference/guide_legistique.md`.

**Formule de réécriture.** La réécriture d'un article de loi s'écrit **« est ainsi rédigé »**.
« Est remplacé par les dispositions suivantes » est la formule réglementaire : elle ne s'emploie
pas dans un texte de loi ni dans un amendement.

**Abroger et supprimer.** **« Abroger »** vaut pour un texte entier et pour ses divisions
numérotées — article, section, chapitre, titre, livre, et les 1°, 2°, a, b d'une énumération.
**« Supprimer »** vaut pour ce qui est à l'intérieur : un alinéa, une phrase, un membre de phrase,
un mot.

**Abroger par bloc.** Partout où un bloc entier tombe — section, chapitre, sous-section —,
**l'abrogation vise le bloc, non ses articles un par un**. Seules les abrogations partielles se
nomment article par article. Les rangs vides, « (Sans objet) » ou autres, se suppriment.
**Lorsque des rangs servent de renvois, la renumérotation et la reprise des renvois se font dans
la même passe que le regroupement, jamais séparément.** Le contrôle du caractère entier d'un bloc
se joue sur le dépôt de droit : il n'est pas à la portée d'un fil qui ne l'a pas sous la main.

**Dates communes d'entrée en vigueur : quatre, non deux.** Le registre des exceptions se recale
en conséquence ; toute date qui n'est pas l'une des quatre est une exception, et s'inscrit comme
telle.

**Virgule devant une conjonction — le symétrique.** La règle générale ci-dessus interdit la
virgule devant et, ou, mais, ni, car, or, donc. Son symétrique : **la virgule est due lorsqu'elle
clôt une incise ouverte avant la conjonction**, faute de quoi l'incise reste ouverte et la phrase
change de sens. Les deux faces se contrôlent ensemble ; une occurrence relevée par le contrôle
automatique se lit avant d'être corrigée.

**Constat chiffré de l'exposé sommaire.** Le constat chiffré occupe **le premier tiers** de
l'exposé, et la borne de longueur passe de 300 à **350 mots**. Règle appliquée à la régénération
en bloc des exposés, après les croisements, jamais avant.
