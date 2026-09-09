# -*- coding: utf-8 -*-
"""Justification et relais des pertes.

Deux champs par ligne perdante ou capteuse : pourquoi la perte est légitime,
et par quelle contrepartie concrète elle se rattrape. Le relais se dit en langue
ordinaire, sans identifiant de nœud ni de ligne — c'est la phrase que le lecteur
emporte.

Deux champs facultatifs s'y ajoutent, symétriques du côté gain : la **vedette**
— un ou deux mots nus, « Le poste », « Le statut » — et le **libellé**, une
phrase factuelle qui dit ce qui s'arrête. Ni euphémisme ni dramatisation : on ne
ment pas, et on n'effraie pas.

Le libellé, donc : cinq à huit mots
qui disent ce qui s'arrête, du point de vue de la personne. Sans lui, une fiche
affiche l'énoncé du livre, écrit du point de vue des finances publiques — un
agent public y lit « Économies de fonctionnement local » en tête de sa perte.

Clé : "ancrage|position|categorie", identique au référentiel des positions.
Le champ relais vaut la chaîne vide pour les capteurs sans contrepartie : la
rente supprimée ne se remplace pas, et le corpus l'assume.
"""

# Deux pertes qui disent le même événement à deux mailles ne font pas deux
# cartes : « votre administration ferme » recouvre l'échelon local supprimé et
# le poste retiré du décompte national. La redite reste au référentiel et au
# compte, elle ne prend pas de carte de fiche.
REDITES = {
    "D5-2-1-e2|perdant|C-30": "D2-2-1|perdant|C-30",
    "D6-2-1-e1|perdant|C-30": "D2-2-1|perdant|C-30",
}

JUSTIFICATIONS = {

"D2-4-1-s1|perdant|C-11": (
 "Subventionner les loyers augmente les loyers, pas le nombre de logements. "
 "L’aide au logement enrichit le bailleur avant le locataire, qui la paie deux "
 "fois : par l’impôt, puis par le loyer qu’elle a fait monter.",
 "Je perds l’aide au logement, je garde la mienne jusqu’au terme de mon bail, "
 "je gagne 550 euros d’aide fondamentale sans dossier et un marché où l’offre "
 "locative privée augmente d’un quart.",
 "L’APL s’arrête pour les nouveaux contrats et se maintient jusqu’au terme "
 "des baux en cours.", "L’APL"),

"D6-3-1|perdant|C-19": (
 "Le sens du métier ne dépend pas d’une grille. Une rémunération qui suit le "
 "travail fait mieux qu’un avancement à l’ancienneté, et l’école qui vous "
 "recrute vous choisit pour ce que vous savez faire.",
 "Je perds le statut et l’avancement à la grille, je gagne une rémunération "
 "négociée, le choix de mon école et 13 % de net en plus.",
 "Le statut et l’avancement à la grille prennent fin.",
 "La grille"),

"D10-4-1-e3|perdant|C-16": (
 "Des études gratuites en apparence sont payées par les jeunes travailleurs "
 "modestes qui n\u2019y accèdent pas. Payer avec l\u2019argent de son propre compte "
 "fait choisir, et fait choisir mieux.",
 "Je perds la gratuité apparente, je gagne un compte éducation du même "
 "montant pour tous et des établissements qui doivent me convaincre.",
 "Vos études se paient sur votre compte éducation.", "La gratuité"),

"D8-3-1|perdant|C-10": (
 "Treize mois d\u2019indemnisation collective font vivre les organismes qui la "
 "gèrent autant que ceux qui la perçoivent. Six mois de solidarité, puis un "
 "compte qui est le vôtre : ce que vous n\u2019utilisez pas vous reste.",
 "Je ne suis plus indemnisé collectivement au-delà de six mois, je gagne un "
 "compte personnel alimenté par mes cotisations et un marché du travail où "
 "l\u2019embauche redevient rentable.",
 "L\u2019indemnisation passe de treize à six mois.", "Au-delà de six mois"),

"D9-3-1-e7|perdant|C-09": (
 "L\u2019abattement de 10 % sur les pensions ne bénéficie qu\u2019aux retraités "
 "déjà imposables, et il coûte 4,8 milliards par an à ceux qui travaillent.",
 "Je perds l\u2019abattement de 10 %, je gagne au moins 500 euros par an de "
 "rente issue du patrimoine public qui m\u2019est rendu.",
 "L\u2019abattement de 10 % sur les pensions imposables s\u2019arrête.",
 "L\u2019abattement"),

"D7-3-1|perdant|C-11": (
 "L\u2019actif net des organismes de logement social est estimé à 340 milliards "
 "d\u2019euros. Le céder rend aux occupants la propriété de ce qu\u2019ils habitent "
 "et remet quatre millions et demi de logements sur le marché.",
 "Je perds mon bail social tel qu\u2019il était, je gagne la possibilité "
 "d\u2019acheter mon logement et un marché locatif où l\u2019offre augmente "
 "d\u2019un quart.",
 "Les logements sociaux sont proposés à la vente en trois ans.",
 "Le parc social"),

"D4-3-2|perdant|C-23": (
 "Un taux réduit est une niche qui se cache dans un prix : il fait payer par "
 "tous l\u2019avantage consenti à quelques-uns. Un taux unique se voit, se "
 "discute et se baisse.",
 "Je perds les taux réduits sur certains achats, je gagne 16 milliards de "
 "taxes spécifiques supprimées et des produits français moins chers.",
 "Les taux réduits de TVA disparaissent : tout passe à 20 %.",
 "Les taux réduits"),

"D7-2-2|perdant|C-09": (
 "L’indexation automatique promet une revalorisation que le déficit rend "
 "chaque année plus incertaine. Un capital qui rapporte suit les performances "
 "de l’économie, non le vote d’un budget.",
 "Je perds l’indexation automatique de ma pension, je gagne au moins 500 euros "
 "par an de rente issue du patrimoine public qui m’est rendu.",
 "L’indexation automatique des pensions est suspendue.",
 "L’indexation"),


"D9-4-1|perdant|C-17": (
 "Le quotient familial rapporte d’autant plus que le revenu est élevé : "
 "c’est une aide à l’enfance qui croît avec l’aisance. Une aide égale par "
 "enfant la remplace.",
 "Je perds le quotient familial et les majorations, je gagne 275 euros par "
 "mois et par enfant, versés sans dossier.",
 "Le quotient familial et les majorations pour enfants s’arrêtent.",
 "Le quotient familial"),

# ---------------------------------------------------------------------- D1
"D1-1-1|perdant|C-50": (
 "Une structure qui refuse l’audit demande à être financée sans être jugée. "
 "L’argent public n’est dû qu’à ce qui accepte d’être vérifié.",
 "Je perds mon financement d’office, je gagne le droit de me faire "
 "financer par ceux qui veulent de moi, avec l’argent qu’ils ont "
 "récupéré."),
"D1-2-1|perdant|C-31": (
 "Une mission maintenue par défaut, année après année, n’a jamais été choisie : "
 "elle a seulement échappé à la question. La soumettre au vote ne la supprime "
 "pas, elle l’expose au consentement.",
 "Je perds la certitude que le service continuera sans qu’on me demande mon "
 "avis, je gagne le droit de dire lesquels je veux payer.",
 "Les missions reconduites sans vote sont soumises au consentement.",
 "Le vote"),
"D1-3-1|perdant|C-56": (
 "Celui qui dispose de l’argent des autres doit répondre plus lourdement de son "
 "abus, non moins. Le privilège de la fonction n’est pas une atténuation.",
 "Je perds le privilège attaché à ma fonction, je gagne un cadre où ma "
 "responsabilité est la même que celle de tout le monde."),
"D1-ed1|capteur|C-56": (
 "Pris un par un ces abus sont anecdotiques ; additionnés ils pèsent des "
 "milliards et sapent la confiance dans la démocratie.",
 "Je perds l’avantage tiré de ma position, je gagne un pays où la "
 "confiance publique cesse d’être une ressource en voie d’épuisement."),

# ---------------------------------------------------------------------- D2
"D2-1-1|perdant|C-31": (
 "L’État qui s’occupe de tout échoue sur l’essentiel. Chacun paie aujourd’hui "
 "des missions qu’il n’a pas choisies et dont il ignore souvent l’existence.",
 "Je perds une action publique à laquelle je tenais, je gagne 600 euros par "
 "mois et le choix d’en financer moi-même ce qui compte pour moi.",
 "L’État se concentre sur sept missions ; les autres s’arrêtent.",
 "Le service"),
"D2-2-1|perdant|C-30": (
 "Une agence n’est pas un emploi, c’est une mission. Quand la mission n’est "
 "plus voulue, maintenir l’agence revient à payer un travail dont personne ne "
 "veut plus — ce qui est la manière la plus sûre de le dévaloriser.",
 "Je perds mon poste, je gagne jusqu’à sept ans à 70 % de mon traitement, le droit de "
 "cumuler librement avec un emploi privé, et la maîtrise de mon temps.",
 "Votre administration ferme, et votre poste avec elle.",
 "Le poste"),
"D2-2-1|perdant|C-31": (
 "Personne n’a voté pour l’institut français du cheval et de l’équitation ni "
 "pour le conseil national du bruit. Ces structures ne sont pas blâmables, "
 "elles sont simplement facultatives.",
 "Je perds un service que l’État rendait, je gagne 550 euros par mois sans "
 "dossier et la liberté d’acheter ailleurs ce que je veux vraiment."),
"D2-2-1|capteur|C-50": (
 "Derrière une mission facultative il y a une bureaucratie dont le premier "
 "objectif est sa survie : augmenter ses crédits, élargir ses missions, se "
 "rendre incontournable. Aucune administration n’a intérêt à réussir si bien "
 "qu’elle en perdrait son objet.",
 "Je perds ma dotation automatique, je gagne le droit d’exister par "
 "ceux qui me veulent : rien n’interdit de me reconstituer en "
 "association ou en entreprise, financée par les mêmes Français "
 "devenus plus riches de 600 euros par mois."),
"D2-2-1|capteur|C-51": (
 "Chaque agence, comité, délégataire, prestataire dilue l’action publique et "
 "prélève au passage. Le consentement à l’impôt ne se délègue pas en chaîne.",
 "Je perds la commande captive, je gagne un client qui m’achète parce "
 "qu’il le choisit et qui dispose de davantage pour le faire."),
"D2-2-1|capteur|C-61": (
 "France Compétences, France Travail, les agences de l’eau, Action Logement "
 "font vivre tout un secteur du flux qu’elles redistribuent. Le bénéficiaire "
 "final n’en reçoit qu’une part.",
 "Je perds le flux public que je redistribuais, je gagne un marché de "
 "la formation, de l’emploi et du logement où l’offre se vend à des "
 "clients dont le revenu net a monté de 13 %."),
"D2-3-1|capteur|C-51": (
 "Établir une amende ou délivrer un document d’identité est le propre de "
 "l’État. Déléguer ces actes à une entité extérieure crée une rente sur "
 "l’exercice même de la souveraineté.",
 "Je perds la délégation régalienne, je gagne tout le champ non "
 "régalien, qui s’ouvre à mesure que l’État s’en retire.",
 "Les actes régaliens délégués rentrent au ministère.",
 "La délégation"),
"D2-3-1|perdant|C-50": (
 "Une agence régalienne n’est pas supprimée, elle rentre dans son ministère. "
 "Elle perd son autonomie, pas ses agents ni sa mission.",
 "Je perds mon indépendance de gestion, je gagne une chaîne de responsabilité "
 "claire et un supérieur qui répond devant les électeurs."),
"D2-3-2|perdant|C-08": (
 "Un musée ou une université qui gère un patrimoine et des revenus propres n’a "
 "pas besoin d’une subvention d’équilibre pour exister. Elle en a besoin pour "
 "ne pas avoir à convaincre.",
 "Je perds ma dotation automatique, je gagne la liberté de fixer mes tarifs, "
 "de chercher du mécénat et de garder ce que je gagne."),
"D2-4-1-s1|perdant|C-32": (
 "Subventionner les loyers augmente les loyers, pas le nombre de logements. "
 "L’aide au logement enrichit le bailleur avant le locataire, et le locataire "
 "la paie deux fois : par l’impôt, puis par le loyer qu’elle a fait monter.",
 "Je perds l’aide au logement, je gagne 300 euros de salaire, 550 euros d’aide "
 "sans dossier, et un marché où l’offre locative privée augmente d’un quart.",
 "L’aide personnalisée au logement s’arrête.",
 "L’APL"),
"D2-4-1-s2|perdant|C-33": (
 "Une aide à l’emploi payée par l’impôt sur le travail taxe les emplois "
 "existants pour en subventionner d’autres. Elle déplace l’emploi, elle n’en "
 "crée pas.",
 "Je perds mes aides à l’embauche, je gagne la disparition totale des impôts "
 "de production et des clients au pouvoir d’achat augmenté de 13 %."),
"D2-4-1-s2|perdant|C-10": (
 "Un dispositif d’aide à l’emploi qui finance le contrat plutôt que le travail "
 "rend le retour à l’emploi dépendant du guichet. Ce qui rend l’emploi "
 "attractif, c’est son salaire.",
 "Je perds l’aide attachée à mon contrat, je gagne un salaire net supérieur de "
 "13 % dès mon embauche et des employeurs qui recrutent parce qu’ils le veulent.",
 "Les aides attachées à votre contrat s’arrêtent.",
 "L’aide au contrat"),
"D2-4-1-s3|perdant|C-33": (
 "L’investissement administré empêche d’autres d’innover : l’État choisit les "
 "projets à la place du marché, avec l’argent de ceux qu’il n’a pas choisis. "
 "Aucune des technologies du quotidien ne lui revient.",
 "Je perds la subvention à l’investissement, je gagne un cadre fiscal stable, "
 "sans piège, et des consommateurs plus riches pour financer mes projets.",
 "Les aides à l’investissement et les plans de soutien s’arrêtent.",
 "Les plans"),
"D2-4-1-s4|perdant|C-36": (
 "L’impôt d’un pays finance les services rendus à ceux qui l’acquittent. "
 "L’État n’a pas de légitimité pour agir sur un territoire qu’il ne maîtrise "
 "pas et où il ne peut fournir aucun service en contrepartie.",
 "Le flux public cesse, le flux privé peut le remplacer à l’identique "
 ": les Français donneront pour les causes qu’ils estiment justes dès "
 "lors qu’ils disposeront plus librement de leur argent."),
"D2-4-1-s5|perdant|C-45": (
 "L’hébergement d’urgence est conservé pour les situations qui l’exigent — "
 "femmes battues, enfants — à hauteur d’un socle de 20 %. Sur la moitié du parc "
 "dont le statut est connu, 60 % des personnes hébergées sont en situation "
 "administrative irrégulière ou précaire, et le fait que l’autre moitié échappe "
 "au décompte dit l’essentiel du pilotage de ces subventions (note e71).",
 "Le socle reste public ; au-delà, l’hébergement se reconstitue par des "
 "associations financées par une population donatrice dont le reste à vivre a "
 "augmenté de 600 euros par mois."),
"D2-4-1-s6|perdant|C-10": (
 "L’insertion financée par dispositif fait vivre l’opérateur d’insertion avant "
 "l’inséré. Ce qui insère durablement, c’est un emploi qui paie.",
 "Je perds mon accompagnement subventionné, je gagne 550 euros par mois sans "
 "condition et un marché du travail où l’embauche redevient rentable.",
 "Les dispositifs d’insertion financés par l’État s’arrêtent.",
 "L’insertion"),
"D2-4-1-s7|perdant|C-44": (
 "Le pronostic vital et l’ordre public, dont les maladies contagieuses graves, "
 "restent couverts sans condition. Seuls 10 % environ de l’aide médicale d’État "
 "vont aujourd’hui aux soins urgents, et cette définition même est élargie aux "
 "soins chroniques, ce qui nourrit une attractivité et un recours croissants "
 "(note e125).",
 "L’urgence vitale reste couverte ; au-delà, rien n’interdit à la générosité "
 "privée de reconstituer la prise en charge, et elle en a désormais les moyens."),
"D2-4-1-s8|perdant|C-03": (
 "Une exonération sur l’emploi à domicile est une niche : elle réduit l’impôt "
 "de ceux qui peuvent employer, et le fait payer aux autres.",
 "Je perds l’exonération sur l’emploi à domicile, je gagne 300 euros de "
 "salaire net par mois, davantage que ce que l’avantage me rapportait.",
 "L’exonération sur l’emploi à domicile s’arrête.",
 "L’emploi à domicile"),
"D2-4-1-s9|perdant|C-32": (
 "Le chèque ciblé décide à votre place de ce que vous devez acheter. Ce qui "
 "compte est la solidarité réellement perçue, non le barème affiché : une part "
 "des droits n’est jamais réclamée, et le barème surestime donc ce que les "
 "familles touchent vraiment.",
 "Je perds mes chèques fléchés, je gagne la même somme en argent libre, versée "
 "sans dossier, que je dépense où je veux.",
 "Les chèques ciblés — pass culture, chèque restaurant — s’arrêtent.",
 "Les chèques"),
"D2-4-1-e2|perdant|C-34": (
 "Les subventions aux associations transforment l’élan de générosité des "
 "bénévoles en clientélisme politique : l’association finit par écrire ses "
 "projets pour plaire au guichet plutôt qu’à ses donateurs.",
 "Je perds ma subvention, je gagne des donateurs dont le reste à vivre a "
 "augmenté de 600 euros par mois et une mission que l’État me laisse.",
 "Votre subvention publique s’arrête.",
 "La subvention"),
"D2-4-1-e2|perdant|C-37": (
 "Une collectivité qui subventionne les entreprises se met en concurrence avec "
 "sa voisine sur l’argent du contribuable, sans qu’aucune n’y gagne à la fin.",
 "Je perds mon guichet d’aides aux entreprises, je gagne la taxe foncière "
 "entièrement versée à ma commune et une compétence claire."),
"D2-ed6|capteur|C-54": (
 "L’aide au logement se capitalise dans le loyer. Le propriétaire encaisse "
 "l’aide que le locataire croit recevoir.",
 "Je perds l’aide qui gonflait mon loyer, je gagne un marché où les "
 "transactions doublent et où mon locataire paie de sa poche, sans "
 "intermédiaire."),
"D2-ed8|capteur|C-52": (
 "Les titres restaurant et chèques vacances diminuent votre salaire et vous "
 "empêchent d’en disposer. Les sociétés qui les émettent dégagent des marges à "
 "faire pâlir d’envie les géants de la technologie, et une commission "
 "nationale occupe élus et syndicats à départager les commerçants agréés.",
 "Je perds l’avantage fiscal qui rendait mon titre obligatoire, je "
 "gagne le droit de vendre le même service à des salariés qui touchent "
 "leur salaire en entier et peuvent me le payer."),
"D2-ed11|capteur|C-56": (
 "La subvention transforme l’élu en guichet dont on espère s’attirer les "
 "faveurs. La signature d’un adjoint au maire ou d’un sous-directeur peut "
 "valoir des centaines de millions d’euros.",
 "Je perds le guichet, je gagne un mandat qui pèse et des électeurs "
 "qui savent ce que je décide."),
"D2-ed12|capteur|C-60": (
 "Quand la faveur se distribue, faire la queue ou du lobbying devient un bon "
 "investissement. L’énergie qui devrait aller au produit va au guichet.",
 "Je perds la rente de l’accès au guichet, je gagne un marché où "
 "l’effort se porte sur le produit et non sur l’antichambre."),
"D2-ed13|capteur|C-55": (
 "Arbitraires et opaques, les aides avantagent les grosses entreprises, bien "
 "implantées et bien introduites. Le taux implicite d’impôt sur les sociétés "
 "s’établissait en 2022 à 21,4 % pour les petites et moyennes entreprises "
 "contre 14,3 % pour les grandes, et l’écart se creuse depuis 2016 (note e35).",
 "Je perds l’aide que ma taille me permettait d’obtenir, je gagne la "
 "disparition intégrale des impôts de production et des clients plus riches."),
"D2-ed15|capteur|C-53": (
 "Les faveurs bénéficient d’abord à ceux qui savent naviguer dans la "
 "complexité de dispositifs parfois faits sur mesure. La complexité n’est pas "
 "un défaut du système, elle en est le péage.",
 "Je perds la rente de la complexité, je gagne un conseil qui se vend "
 "sur sa valeur et une clientèle élargie à ceux qui ne pouvaient pas "
 "se le payer."),
"D2-5-1|perdant|C-35": (
 "Une niche est une subvention masquée : ce que l’un ne paie pas, les autres "
 "le paient. Le crédit d’impôt recherche rapporte plus de cent millions "
 "d’euros par an à un seul laboratoire, le crédit d’impôt outre-mer finance "
 "des hôtels de luxe en Polynésie.",
 "Je perds mes niches, je gagne l’assiette pleine et le taux bas, des clients "
 "dont le pouvoir d’achat a monté de 13 %, et un impôt que je peux calculer "
 "sans conseil."),

# ---------------------------------------------------------------------- D3
"D3-2-1-e2|perdant|C-06": (
 "Deux niveaux de lecture, tous deux assumés. L’entreprise est neutre : ses "
 "prélèvements nets de subventions et d’aides sont stables. Le propriétaire "
 "porte le solde par la marge, parce que c’est lui qui percevait la subvention.",
 "Je perds sur ma marge, je gagne la disparition des impôts de production, un "
 "cadre stable et une clientèle dont le revenu net augmente de 13 %.",
 "Le gain de la suppression des taxes sur les salaires va au salarié, non à l’entreprise.",
 "Le gain net",
 "Le gain de la suppression des taxes va au salarié. Votre charge globale, "
 "elle, ne monte pas.",
 "Le partage"),
"D3-2-1-e3|perdant|C-09": (
 "Le travail est le revenu le plus taxé de France : 41 % dès 1 900 euros nets "
 "par mois, contre 30 % sur les revenus du capital, 14 % sur les pensions et "
 "6 % sur le patrimoine (note e15). Décharger le travail sans décharger les "
 "revenus de remplacement n’est pas un oubli, c’est le sens de la mesure.",
 "Je ne gagne rien sur ma pension, je gagne 20 000 euros de patrimoine public "
 "restitué à mon foyer et une rente viagère d’au moins 500 euros par an.",
 "La suppression de la CSG porte sur les salaires, non sur les pensions.",
 "La CSG"),
"D3-2-1-e4|perdant|C-02": (
 "Les prix disent enfin ce que les choses coûtent. La surtaxe disparaît, "
 "l’impôt se déplace sur le résultat, les certificats d’économie d’énergie "
 "s’arrêtent, et ces prix-là baissent. Le solde tient dans une inflation "
 "faciale inférieure à 2 %.",
 "Je vois une inflation faciale inférieure à 2 %, je gagne 300 euros de "
 "salaire net, plus d’offre, plus de concurrence et un meilleur rapport "
 "qualité-prix.",
 "Les prix se réajustent, avec une inflation faciale inférieure à 2 %.",
 "La vérité des prix"),
"D3-ed3|capteur|C-51": (
 "Taxer davantage une boulangerie, c’est augmenter le prix du pain, renoncer à "
 "un apprenti, diminuer la rémunération du boulanger. La chaîne de prélèvement "
 "vit de ce qu’elle prélève.",
 "Je perds ma part de la chaîne de prélèvement, je gagne une économie "
 "où la boulangerie embauche son apprenti."),

# ---------------------------------------------------------------------- D4
"D4-2-3|perdant|C-51": (
 "L’autorisation préalable fait vivre celui qui instruit le dossier. Elle fait "
 "peser sur les citoyens honnêtes une charge qui ne devrait incomber qu’à ceux "
 "qui enfreignent les règles.",
 "Je perds l’instruction des autorisations, je gagne le contrôle et la "
 "sanction des abus réels, qui est le travail utile.",
 "L’instruction des autorisations préalables s’arrête.",
 "L’instruction"),
"D4-ed17|perdant|C-48": (
 "La fraude n’est pas une anomalie, elle est le produit de la complexité "
 "exploitée par les moins scrupuleux. Une règle simple peut être appliquée "
 "entièrement, donc équitablement.",
 ""),
"D4-ed16|capteur|C-53": (
 "Seuls les plus riches peuvent naviguer cette complexité, qui profite aux "
 "avocats fiscalistes. L’erreur fait peur au contribuable honnête ; pour "
 "l’autre, la fraude devient rentable.",
 "Je perds la rente de la complexité fiscale, je gagne des clients "
 "plus nombreux pour un conseil qui crée de la valeur au lieu d’en "
 "contourner."),
"D4-ed18|capteur|C-57": (
 "Des obligations sédimentées depuis des décennies détournent le fruit du "
 "travail des salariés vers des organisations qui ne répondent plus à leurs "
 "priorités.",
 "Je perds le financement par obligation, je gagne des adhérents qui "
 "cotisent parce qu’ils me choisissent, avec un salaire net supérieur "
 "de 13 %."),
"D4-3-2|perdant|C-46": (
 "Un taux réduit de taxe sur la valeur ajoutée est une niche comme une autre : "
 "il baisse le prix d’un bien pour tous, y compris pour ceux qui n’en ont pas "
 "besoin, et le fait payer par le taux normal que supportent les autres.",
 "Je perds le taux réduit sur certains achats, je gagne 300 euros de salaire "
 "net par mois et une taxe que je comprends au premier regard."),
"D4-3-3|perdant|C-06": (
 "L’impôt sur les bénéfices frappe ce qui a réussi, l’impôt de production "
 "frappe ce qui essaie. Déplacer la charge du second vers le premier, même de "
 "quelques points et à titre transitoire, favorise celui qui démarre.",
 "Je perds quelques points sur mes bénéfices, je gagne la disparition "
 "intégrale des taxes qui me frappaient avant même d’être rentable.",
 "L’impôt sur les sociétés augmente, en échange des impôts de production supprimés.",
 "L’impôt sur les bénéfices"),
"D4-4-1|perdant|C-01": (
 "Une taxe foncière en euros par mètre carré remplace des valeurs locatives "
 "cadastrales figées depuis un demi-siècle. Elle redistribue la charge entre "
 "propriétaires, et les perdants de la nouvelle assiette ne sont pas encore "
 "identifiés au corpus.",
 "Je perds sur l’assiette nouvelle, je gagne la fin des droits de mutation et "
 "de succession déguisés, et une base que je peux vérifier moi-même."),

# ---------------------------------------------------------------------- D5
"D5-2-1-e2|perdant|C-38": (
 "Quand quatre échelons se partagent la même compétence, aucun n’en répond. "
 "Moins d’élus, mais dont le mandat pèse : c’est le vote qui y gagne, pas "
 "l’administration.",
 "Je perds mon mandat, je gagne le droit de reprendre ma vie antérieure ou de "
 "briguer une fonction où ma voix compte davantage."),
"D5-2-1-e2|perdant|C-30": (
 "Les agents des échelons supprimés sont compris dans le plan de départ : "
 "aucune suppression n’est prononcée sans la contrepartie qui l’accompagne.",
 "Je perds mon poste, je gagne jusqu’à sept ans à 70 % de mon traitement et le droit "
 "de cumuler librement avec un emploi privé.",
 "L’échelon local où vous servez disparaît."),
"D5-2-1-e2|perdant|C-37": (
 "Le département et la région se sont ajoutés à la commune sans jamais la "
 "remplacer. La commune est le seul échelon où l’électeur connaît celui qu’il "
 "élit et voit ce qu’il en fait.",
 "L’échelon disparaît, la compétence revient à la commune et à "
 "l’association libre des communes : rien de ce qui était fait ne "
 "devient impossible."),
"D5-2-1-s1|perdant|C-31": (
 "Chacun paie 115 euros par mois et par foyer pour les loisirs subventionnés, "
 "contre 36 euros pour la justice et les prisons. La question n’est pas la "
 "valeur de ces activités, c’est de savoir qui décide de les payer.",
 "Je perds une offre culturelle et sportive subventionnée, je gagne 600 euros "
 "par mois et le choix de financer celle que je fréquente vraiment.",
 "Les dépenses culturelles et de loisir locales s’arrêtent.",
 "La culture locale"),

# ---------------------------------------------------------------------- D6
"D6-2-1-e1|perdant|C-30": (
 "580 000 postes correspondent à des missions que l’État cesse d’exercer, non "
 "à des agents jugés inutiles. Aucune mission indispensable, aucun agent de "
 "terrain n’est touché.",
 "Je perds mon poste, je gagne jusqu’à sept ans à 70 % de mon traitement, le cumul "
 "libre avec un emploi privé, la maîtrise de mon temps et un métier choisi.",
 "Un poste public sur dix disparaît."),
"D6-3-1|perdant|C-05": (
 "Le sens de l’intérêt général ne dépend pas d’un statut. La Suisse a supprimé "
 "le sien en 2002 sans que son administration s’effondre, et la Déclaration "
 "des droits ne connaît d’autre distinction que les vertus et les talents.",
 "Je perds l’emploi à vie, je gagne 13 % de rémunération nette en plus, une "
 "carrière que je gère moi-même et une rémunération qui suit mes résultats.",
 "Le statut de la fonction publique prend fin. Emploi garanti, carrière et "
 "règles propres cèdent au droit du travail commun.",
 "Le statut"),

# ---------------------------------------------------------------------- D7
"D7-3-1|perdant|C-40": (
 "L’actif net des organismes de logement social — 4,8 millions de logements — "
 "est estimé à 340 milliards d’euros, soit environ 200 milliards de produits de "
 "cession après un socle conservé de 15 % et une décote de liquidité de 15 % "
 "(note e118). La sortie court sur trois ans, commence par les ménages les plus "
 "aisés et les attributions les plus anciennes, les loyers convergent "
 "progressivement vers le marché et le bail s’aligne sur le cadre privé.",
 "Je perds mon statut de locataire social, je gagne la priorité d’acquisition "
 "sur mon logement, 550 euros par mois d’aide, et un marché où la décote de "
 "liquidité devient un bénéfice de prix pour tous les ménages.",
 "Votre logement social vous est proposé à la vente.",
 "Le parc social"),
"D7-3-1|capteur|C-54": (
 "Le bailleur, social ou privé, encaisse l’aide que le locataire croit "
 "recevoir. Restituer le parc supprime l’aide et l’intermédiaire d’un même "
 "mouvement.",
 "Je perds l’aide capitalisée dans le loyer, je gagne un marché où les "
 "transactions doublent et un locataire solvable par son salaire."),
"D7-ed3|capteur|C-59": (
 "Un bien rationné par la file d’attente et non par le prix crée "
 "inéluctablement une opportunité de corruption : celui qui gère la file "
 "détient une valeur qu’il n’a pas produite.",
 "Je perds le pouvoir d’attribuer, je gagne un marché où le logement "
 "se trouve par le prix et non par la file."),
"D7-4-1|perdant|C-56": (
 "L’État actionnaire est un pouvoir de nomination autant qu’un portefeuille. "
 "Un contrôleur qui détient le secteur qu’il contrôle ne contrôle rien.",
 "Je perds le pouvoir de nomination, je gagne des entreprises "
 "publiques devenues des entreprises, et un État qui contrôle enfin le "
 "secteur."),

# ---------------------------------------------------------------------- D8
"D8-2-2|capteur|C-59": (
 "Régimes généraux, régimes spéciaux, caisses : la tuyauterie coûte, et elle "
 "n’assure pas. Un travailleur paie des cotisations sans être plus assuré "
 "qu’un inactif.",
 "Je perds la gestion du régime obligatoire, je gagne un marché de "
 "l’épargne retraite alimenté de 30 milliards par an de cotisations "
 "rendues."),
"D8-2-3|perdant|C-39": (
 "La transition court sur vingt-cinq ans et les pensions inférieures à 1 200 "
 "euros ne sont pas touchées. L’effort est demandé à ceux dont la pension "
 "excède ce seuil, et il est étalé sur une génération.",
 "Je perds une part de ma pension future, je gagne une pension qui ne dépend "
 "plus d’un déficit de 125 milliards par an ni d’une décision politique "
 "annuelle.",
 "La transition des retraites court sur vingt-cinq ans.",
 "La transition"),
"D8-3-1|perdant|C-41": (
 "Treize mois d’indemnisation collective font vivre les organismes qui la "
 "gèrent autant que ceux qui la perçoivent. Six mois de solidarité, puis un "
 "compte qui est le vôtre : ce que vous n’utilisez pas vous reste.",
 "Je ne suis plus indemnisé collectivement au-delà de six mois, je gagne un compte personnel "
 "alimenté de 30 milliards par an de cotisations rendues, et un marché du "
 "travail où l’embauche redevient rentable."),
"D8-4-1|perdant|C-13": (
 "Un reste à charge de 10 % rend visible le coût du soin sans le rendre "
 "inaccessible : il est plafonné à 5 % du revenu annuel, de sorte que la "
 "maladie grave ne ruine personne.",
 "Je perds la gratuité apparente de certains actes, je gagne une règle simple, "
 "un plafond que je connais d’avance et jusqu’à 300 euros par an de frais de "
 "gestion en moins.",
 "Un reste à charge de 10 % par acte apparaît, plafonné à 5 % de votre "
 "revenu, et les dépenses de confort sortent du bouclier.",
 "Le reste à charge"),
"D8-4-2|capteur|C-58": (
 "Jusqu’à 300 euros par an et par foyer partent en frais de gestion de la "
 "complémentaire santé. C’est le prix d’un intermédiaire obligatoire entre "
 "vous et votre soin.",
 "Je perds la complémentaire obligatoire, je gagne une concurrence "
 "libre où je vends mes tarifs à des assurés qui comparent et qui ont "
 "de quoi payer."),
"D9-2-2|perdant|C-44": (
 "Le pronostic vital et l’ordre public, dont les maladies contagieuses graves, "
 "restent couverts sans condition. Au-delà, la solidarité nationale suppose "
 "d’appartenir à la nation qui la finance.",
 "L’urgence vitale et l’ordre public restent couverts sans condition ; "
 "au-delà, la générosité privée peut reconstituer la prise en charge, "
 "et elle en a désormais les moyens."),
"D9-2-3|perdant|C-14": (
 "L’empilement des allocations et de leurs compléments oblige à prouver son "
 "handicap dossier après dossier. Un versement unique de 1 100 euros par mois "
 "supprime la démarche, pas le droit.",
 "Je perds l’empilement des allocations et de leurs compléments, je gagne "
 "1 100 euros par mois versés automatiquement, sans dossier à refaire.",
 "L’empilement des allocations et de leurs compléments s’arrête.",
 "Les dossiers"),
"D9-3-1-e7|perdant|C-39": (
 "L’abattement dit « Papon » de 10 % sur les pensions coûte 4,8 milliards "
 "d’euros par an, ne bénéficie qu’aux retraités déjà imposables, leur rapporte "
 "généralement moins de 1 % de leur revenu, et ne repose sur aucun fondement "
 "économique — contrairement à l’abattement pour frais professionnels des "
 "actifs, qui compense des frais réels (note e120). Les pensions inférieures à "
 "1 200 euros ne sont pas touchées.",
 "Je perds environ 6 % au-delà de 1 600 euros de pension, je gagne 20 000 euros "
 "de patrimoine restitué à mon foyer et une rente d’au moins 500 euros par an."),
"D9-4-1|perdant|C-43": (
 "L’aide par enfant est identique quelle que soit la situation des parents. "
 "Le supplément attaché au statut d’isolé revenait à faire dépendre le droit "
 "de l’enfant de la déclaration de ses parents.",
 "Je perds le supplément lié à mon statut, je gagne le recouvrement de la "
 "pension alimentaire par l’administration fiscale, là où un quart à deux "
 "cinquièmes des pensions restent aujourd’hui impayées."),
"D9-4-1|perdant|C-03": (
 "Le quotient familial rapporte d’autant plus que le revenu est élevé : c’est "
 "une aide à l’enfance qui croît avec l’aisance. Une aide de 275 euros par "
 "enfant donne à chaque enfant la même part.",
 "Je perds l’avantage du quotient familial, je gagne 275 euros par mois et par "
 "enfant, et 300 euros de salaire net en plus."),
"D9-4-2-e2|perdant|C-47": (
 "Entre un quart et deux cinquièmes des parents créanciers subissent des "
 "impayés. Le Québec a instauré dès 1995 le prélèvement à la source de la "
 "pension par l’administration fiscale et son reversement au parent créancier, "
 "le versement direct restant possible d’un commun accord ; en contrepartie, il "
 "n’y existe ni prestation spécifique aux familles monoparentales ni garantie "
 "publique en cas d’impayé (note e78). Le projet reprend les deux volets.",
 ""),

# ---------------------------------------------------------------------- D10
"D10-ed1|capteur|C-50": (
 "La carte scolaire prive vos enfants d’un meilleur enseignement. Les classes "
 "moyennes et les familles modestes restent piégées par ce déterminisme "
 "administratif, quand les autres contournent.",
 "Je perds la carte scolaire, je gagne des écoles financées par un "
 "compte de 6 600 euros par an et par enfant, qui suit l’élève où "
 "qu’il aille."),
"D10-4-1-e3|perdant|C-42": (
 "Des études gratuites en apparence sont payées par les jeunes travailleurs "
 "modestes qui n’y accèdent pas. Payer avec l’argent de son propre compte fait "
 "réfléchir à deux fois avant de s’engager dans une filière sans débouché.",
 "Je perds la gratuité apparente, je gagne un compte éducation alimenté de "
 "6 600 euros par an dont je dispose à ma majorité, en une fois ou en différé."),
"D10-4-2|perdant|C-08": (
 "Une université qui reçoit sa dotation quoi qu’elle enseigne n’a pas à "
 "démontrer l’intérêt de ses formations. Les meilleures universités du monde "
 "vivent de leurs résultats, pas de leur ancienneté.",
 "Je perds ma dotation administrée, je gagne la liberté de mes tarifs, de mes "
 "bourses, du mécénat, et des étudiants qui viennent parce qu’ils choisissent."),

# ---------------------------------------------------------------------- D11
# La dette par foyer était une image, non une perte portée : la ligne est
# retirée du référentiel le 20260828. Sa justification part avec elle.
# ------------------------------------------------- C-00, pertes du système actuel
# Ces lignes ne décrivent pas un effet de la réforme mais ce que le statu quo
# coûte. Leur relais est le gain sobre du plan, jamais l'écart lui-même.
"M-productivite-heure|diagnostic|C-00": (
 "Pour une heure de travail, le travailleur moyen produit 63 euros de richesse "
 "et n’en récupère que 23 nets, quand les propriétaires du capital en "
 "perçoivent 11. La différence ne va à personne en particulier : elle se perd "
 "dans le trajet.",
 "Le pays perd aujourd’hui 40 euros sur 63 dans le trajet ; le plan en récupère "
 "une part, de l’ordre de 10 %, sans prétendre combler l’écart."),
"M-suisse-revenu|diagnostic|C-00": (
 "Un Suisse dispose d’un revenu réel médian deux fois supérieur à celui d’un "
 "Français, et l’écart s’est creusé de moitié en vingt ans. Ce n’est pas une "
 "fatalité géographique : c’est un résultat de politiques publiques.",
 "L’écart mesure ce qui est possible, il ne se promet pas. Ce que le plan rend "
 "se chiffre à part : de l’ordre de 10 % de gain de qualité de vie et six "
 "points de prélèvements en moins."),
"M-suisse-emploi|diagnostic|C-00": (
 "Notre code du travail compte près de 4 000 pages contre 200 pages au code "
 "suisse, et notre chômage dépasse 8 % quand la Suisse est au plein emploi. La "
 "protection écrite n’est pas la protection obtenue.",
 "L’écart mesure ce qui est possible. Le plan promet la simplification, non le "
 "plein emploi : c’est le seul levier rapide de productivité, et son rendement "
 "est donné en ordre de grandeur."),
"M-paysbas|diagnostic|C-00": (
 "À économie néerlandaise, les Français gagneraient 25 % de pouvoir d’achat, "
 "ou deux mois de congés supplémentaires, ou un départ en retraite à 55 ans. "
 "Même contexte européen, résultats différents.",
 "L’écart mesure ce qui est possible, il ne se promet pas. Le plan rend un "
 "ordre de grandeur de 10 %, et le dit tel quel."),
"M-pauvrete|diagnostic|C-00": (
 "Si la dépense publique était la recette contre la pauvreté, personne ne "
 "serait à la rue en France. Nous portons le deuxième taux de personnes sans "
 "domicile fixe de l’OCDE avec le premier niveau de dépense.",
 "Le pays perd aujourd’hui sur les deux tableaux ; il gagne une aide "
 "fondamentale de 550 euros par mois versée sans dossier, là où le maquis "
 "actuel laisse un tiers des droits non réclamés."),
"M-risque-crise|diagnostic|C-00": (
 "Un État qui s’endette augmente chaque jour le risque d’une crise tout en "
 "réduisant ses marges pour l’absorber. Les Français le savent et épargnent au "
 "niveau record de 18 %, en prévision de lendemains qui déchantent.",
 "Le pays perd aujourd’hui cette épargne immobilisée par précaution ; il gagne "
 "des prélèvements ramenés de 42,9 % à 36,3 % de la richesse produite et des "
 "marges reconstituées."),
"D11-1-1|diagnostic|C-00": (
 "Chaque foyer s’endette de 5 500 euros par an sans l’avoir voté. Il n’existe "
 "ni rythme idéal de redressement ni seuil de faillite automatique, mais une "
 "dette qui progresse pendant que les marges se réduisent.",
 "Le pays perd chaque année 5 500 euros par foyer de dette nouvelle ; il gagne "
 "un redressement qui ne demande qu’un point d’efficacité ou un point de "
 "croissance pour tenir le rythme des traités."),
# ------------------------------------------------ apports des notes de fin
"M-crise-souveraine|diagnostic|C-00": (
 "Ne plus pouvoir emprunter n’est pas une hypothèse d’école : la France a connu "
 "la faillite dite des deux tiers en 1797 et une quinzaine de dévaluations, "
 "défauts partiels et répudiations depuis Clovis. L’ajustement subi serait "
 "d’au moins 7 % des dépenses, et plus vraisemblablement de plusieurs dizaines "
 "de points par emballement, comme ailleurs en zone euro.",
 "Le pays porte aujourd’hui ce risque sans contrepartie ; il gagne un "
 "redressement choisi de 6,5 points de prélèvements, qui vaut mieux qu’un "
 "ajustement subi de plusieurs dizaines."),
"M-taxes-affectees|capteur|C-51": (
 "Une taxe affectée n’est pas un impôt, c’est un circuit fermé : elle prélève "
 "sur tous pour dépenser au profit de celui qui l’a obtenue. Le cinéma en est "
 "l’exemple le plus net, l’eau, les transports et les spectacles suivent.",
 "Je perds ma taxe dédiée, je gagne un public dont le revenu net a monté de "
 "13 % et qui peut acheter mon offre directement.",
 "Votre taxe affectée est supprimée.",
 "La taxe dédiée"),
"M-rente-statut|capteur|C-05": (
 "Le statut a créé une rente lorsqu’il a été étendu à des missions "
 "facultatives. Le plan de départ ne compense pas une perte, il solde cette "
 "rente — c’est ce qui justifie son niveau élevé.",
 "Je perds la rente attachée au statut, je gagne jusqu’à sept ans à 70 % du traitement "
 "pour la solder, et un métier que je choisis ensuite."),
"M-frais-gestion-sante|capteur|C-58": (
 "16,9 milliards d’euros par an partent en frais de gestion cumulés entre les "
 "mutuelles, les administrations de sécurité sociale et le ministère. C’est le "
 "prix de la superposition de deux étages obligatoires entre le patient et son "
 "soin.",
 "Je perds la complémentaire obligatoire, je gagne une concurrence libre où mes "
 "tarifs se comparent, devant des assurés qui ont de quoi payer."),
}
