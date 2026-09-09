# -*- coding: utf-8 -*-
"""Construit le référentiel des positions dérivées.

Aucune valeur du REF n'est recopiée ici : les intitulés, les chiffres et les
ancres sont lus au référentiel par le générateur. Ce fichier ne porte que ce que
la dérivation ajoute — position, catégorie, échelle, nature, degré, miroir,
raccroche — et les seules grandeurs qui n'existent nulle part ailleurs, chacune
avec son opération.

Référence d'une ligne : "ancrage|position|categorie".

Deux blocs structurels commandent la sortie.

`GROUPES` — l'ordre de lecture. Les catégories se rangent par familles, de la
plus large à la plus particulière, et les rentes ferment. Un livrable qui les
sort dans l'ordre alphabétique n'a pas de propos.

`EVENTAIL` — un effet atteint plusieurs catégories. Le rattachement d'origine
nomme le bénéficiaire principal ; l'éventail nomme les autres. Chaque ligne
fille reprend le miroir et la raccroche de sa ligne mère. Sans ce bloc, une
catégorie ne reçoit que les effets dont elle est le bénéficiaire principal, et
perd tout ce qui l'atteint au même titre qu'une autre.
"""
import json, sys

# --------------------------------------------------------------- nomenclature
# Bloc fermé. Une catégorie nomme un ensemble de personnes. La position est
# portée par la ligne, jamais par la catégorie : la même personne est gagnante
# ici et perdante là.
CATEGORIES = [
 # -- le gain d'ensemble, aveugle et dynamique
 ("C-00","la nation","N’importe qui dans la rue, du seul fait de vivre dans un pays plus prospère, plus sûr et moins endetté. Gain dynamique, largement qualitatif, adossé aux écarts mesurés avec les pays comparables.","personne","68 M","manuscrit","« La Nation dépasse l’État, et un pays ne se résume pas à son État »",["tous les Français","le pays"]),
 # -- personnes physiques, position transversale
 ("C-01","contribuable","Celui qui acquitte l’impôt, toutes administrations confondues.","foyer","30 M foyers","manuscrit","« à la fin, ce sont toujours les citoyens qui paient »",["contribuable honnête","finances publiques (à requalifier)"]),
 ("C-02","citoyen","Résident, toutes générations.","personne","68 M","manuscrit","« 68 millions de Français »",["Français","habitant","tous les citoyens"]),
 ("C-03","foyer","Unité de restitution du patrimoine et de mesure des aides.","foyer","30 M","manuscrit","« un montant de 20 000 euros pour chaque foyer »",["ménage"]),
 ("C-04","travailleur","Salarié, indépendant, public ou privé, temps plein ou partiel.","travailleur type","29 M","manuscrit","« le travailleur type verra 600 euros par mois rendus »",["salarié","actif","travailleur type"]),
 ("C-05","agent public maintenu","Agent public affecté à l’une des sept missions indispensables.","personne","5,22 M","classeur","5,8 M d’agents publics moins 580 000 départs",[]),
 ("C-06","entreprise","Entreprise sans dépendance à la subvention.","—","","manuscrit","« une entreprise ne supporte pas l’impôt qu’elle paie »",["entreprise générique","employeur"]),
 ("C-07","association bénévole","Association vivant de dons, de legs et de produits propres.","—","","manuscrit","Fondation de France, Emmaüs, Société nationale de sauvetage en mer",[]),
 ("C-08","établissement autonome","Musée, université, institut conservé sous statut autonome.","—","303","classeur","onglet Synthèse agences, colonnes EPIC et autorités",["université autonome"]),
 ("C-09","retraité","Titulaire d’une pension.","personne","17 M","classeur","onglet Perdants",[]),
 ("C-10","personne sans emploi","Demandeur d’emploi, toutes catégories.","personne","5,7 M","classeur","onglet Perdants",["chômeur"]),
 ("C-11","locataire","Locataire du parc privé.","personne","","absent des deux","",[]),
 ("C-12","ménage acquéreur","Ménage cherchant à acquérir son logement, jeunes et familles.","foyer","","manuscrit","« les jeunes et les familles sont pénalisés par des logements privés rares donc chers »",["primo-accédant"]),
 ("C-13","patient","Personne recourant aux soins.","personne","","manuscrit","« personne ne sera moins bien soigné qu’aujourd’hui »",[]),
 ("C-14","personne handicapée","Bénéficiaire de la part supplémentaire d’aide fondamentale.","personne","","manuscrit","allocation aux adultes handicapés fusionnée",[]),
 ("C-15","enfant","Mineur de zéro à dix-huit ans.","personne","14 M","classeur","onglet Perdants",["élève"]),
 ("C-16","jeune adulte","Étudiant, apprenti, jeune travailleur.","personne","4 M","classeur","3 M d’étudiants et 1 M d’apprentis",["étudiant"]),
 ("C-17","parent","Personne assumant la charge d’un enfant.","foyer","","manuscrit","« sans distinction de statut des parents »",[]),
 ("C-18","soignant","Professionnel de santé.","personne","","manuscrit","« mieux rémunérer de +13 % nets tous les soignants »",[]),
 ("C-19","enseignant","Professeur du primaire, du secondaire, du supérieur.","personne","","manuscrit","« le salaire net moyen des enseignants sera maintenu et augmenté de +13 % »",[]),
 ("C-20","électeur communal","Électeur et habitant d’une commune.","personne","","manuscrit","« la maison commune par excellence »",["habitant"]),
 ("C-21","héritier","Bénéficiaire d’une transmission à titre gratuit.","personne","","manuscrit","« fin des impôts cachés sur mutation et succession »",[]),
 ("C-22","épargnant","Détenteur d’un compte épargne personnel.","personne","","manuscrit","« rendre à chacun ses cotisations sur un compte épargne à son nom »",["investisseur"]),
 ("C-23","consommateur","Acheteur final de biens et de services.","personne","","manuscrit","« baisse du coût des produits français »",[]),
 ("C-24","exportateur","Entreprise vendant hors du territoire.","—","","manuscrit","« compétitivité et prix des produits français »",[]),
 # -- perdants
 ("C-30","agent d’une structure fermée","Agent public affecté à une mission facultative interrompue.","personne","580 000 postes publics","classeur","onglet Perdants, ligne agents publics",[]),
 ("C-31","usager d’une mission facultative","Bénéficiaire d’un service public hors des sept missions.","personne","","manuscrit","« chacun subventionne les producteurs d’huîtres ou les associations de médiation animale »",[]),
 ("C-32","allocataire d’aide ciblée","Bénéficiaire d’une aide sous condition ou sous statut.","foyer","","manuscrit","« environ 80 euros par mois en moins »",[]),
 ("C-33","entreprise subventionnée","Entreprise dont le modèle dépend d’une aide publique.","—","","manuscrit","« les aides aux entreprises alimentent la défiance envers le capitalisme de connivence »",[]),
 ("C-34","association subventionnée","Association dont le budget dépend de la subvention publique.","—","","manuscrit","« les subventions aux associations transforment l’élan de générosité des bénévoles en clientélisme politique »",[]),
 ("C-35","bénéficiaire de niche","Contribuable dont l’impôt est réduit par un dispositif dérogatoire.","—","486 niches","manuscrit","Sanofi au titre du crédit d’impôt recherche, hôtels de luxe en Polynésie, jeux vidéo",[]),
 ("C-36","population bénéficiaire de l’aide au développement","Population hors de la communauté nationale, sur un territoire que l’État français ne maîtrise pas.","—","","manuscrit","« l’État n’a pas de légitimité pour agir sur un territoire qu’il ne maîtrise pas »",["reste du monde"]),
 ("C-37","collectivité d’échelon supprimé","Département, région, intercommunalité et leurs services.","—","","manuscrit","« la commune, échelon local unique »",[]),
 ("C-38","élu d’échelon supprimé","Titulaire d’un mandat dans un échelon supprimé.","personne","","absent des deux","input brouillon : environ 12 % des élus, non instruit",[]),
 ("C-39","retraité au-dessus du seuil","Titulaire d’une pension supérieure à 1 600 € par mois.","personne","4,3 M","classeur","onglet Perdants, ligne retraités",[]),
 ("C-40","locataire du parc social","Occupant d’un logement social cédé.","personne","3,5 M","classeur","onglet Perdants, ligne HLM",[]),
 ("C-41","chômeur indemnisé au long cours","Demandeur d’emploi indemnisé au-delà de six mois.","personne","3,3 M","classeur","onglet Perdants, ligne sans emploi catégorie A",[]),
 ("C-42","étudiant de la gratuité","Étudiant dont le cursus est aujourd’hui financé sans contrepartie.","personne","2,3 M non-boursiers","classeur","onglet Perdants, ligne étudiants",[]),
 ("C-43","parent seul","Parent déclaré isolé percevant un supplément d’aide à ce titre.","foyer","","manuscrit","« les aides aux parents déclarés comme isolés se substituent ou se cumulent à des pensions alimentaires »",[]),
 ("C-44","personne étrangère en situation irrégulière","Bénéficiaire de l’aide médicale d’État hors pronostic vital.","personne","","manuscrit","« l’impôt doit se concentrer sur les cas graves »",[]),
 ("C-45","personne hébergée en urgence","Bénéficiaire de l’hébergement d’urgence hors socle de 20 %.","personne","","manuscrit","« hors socle de 20 % (femmes battues, enfants) »",[]),
 ("C-46","consommateur de biens à taux réduit","Acheteur de biens aujourd’hui taxés à taux réduit de TVA.","personne","","classeur","21 taux réduits non comptabilisés en niche, 33,382 Md€",[]),
 ("C-47","coparent débiteur défaillant","Parent ne versant pas la pension alimentaire due.","personne","25 à 40 % des créances","manuscrit","« facilitant de facto l’abandon parental »",[]),
 ("C-48","fraudeur","Celui dont la fraude est rendue rentable par la complexité.","—","","manuscrit","« pour les autres, la fraude devient rentable »",[]),
 # -- capteurs
 ("C-50","structure administrative facultative","Agence, comité, instance poursuivant sa propre survie.","—","750 sur 1 104","manuscrit","« une bureaucratie qui a comme premier objectif sa survie »",[]),
 ("C-51","délégataire et prestataire public","Intermédiaire à qui l’exécution d’une mission est déléguée.","—","","manuscrit","« chaque agence, comité, délégataire, prestataire dilue l’action publique »",[]),
 ("C-52","émetteur de titres conditionnés","Société émettrice de titres restaurant et chèques vacances, et instance d’agrément.","—","","manuscrit","« des marges à faire pâlir d’envie les géants de la tech »",["commission nationale des titres restaurant"]),
 ("C-53","intermédiaire de la complexité","Conseil vivant de la capacité à franchir la complexité fiscale et normative.","—","","manuscrit","« seuls les plus riches peuvent naviguer cette complexité, qui profite aux avocats fiscalistes »",["avocat fiscaliste"]),
 ("C-54","bailleur","Propriétaire dont le loyer est soutenu par l’aide au logement.","—","","manuscrit","« subventionner les loyers augmente les loyers, pas le nombre de logements »",["bailleur social"]),
 ("C-55","grande entreprise introduite","Entreprise assez implantée pour capter l’aide discrétionnaire.","—","","manuscrit","« arbitraires et opaques, les aides avantagent les grosses entreprises, bien implantées et bien introduites »",[]),
 ("C-56","décideur public attributaire","Élu ou agent dont la signature emporte l’attribution d’une faveur.","—","","manuscrit","« la signature d’un adjoint au maire ou d’un sous-directeur d’administration peut valoir des centaines de millions d’euros »",[]),
 ("C-57","organisation financée par obligation","Syndicat ou organisme financé par une obligation légale sédimentée.","—","","manuscrit","« détournent le fruit du travail des salariés vers les syndicats »",[]),
 ("C-58","gestionnaire de complémentaire santé","Organisme prélevant des frais de gestion sur la couverture santé.","—","","manuscrit","« jusqu’à 300 euros par an et par foyer de frais de gestion »",[]),
 ("C-59","gestionnaire de file d’attente","Attributaire d’un bien rationné par la file plutôt que par le prix.","—","","manuscrit","« la file d’attente se transforme en opportunité de corruption »",[]),
 ("C-60","lobbyiste","Professionnel de l’accès au guichet public.","—","","manuscrit","« faire la queue ou du lobbying devient un bon investissement »",[]),
 ("C-61","opérateur financé par l’aide","Organisme dont l’activité vit du flux d’aide qu’un opérateur redistribue.","—","","classeur","France Compétences, France Travail, agences de l’eau, Action Logement",[]),
]

# ------------------------------------------------------- ancrages au manuscrit
# Lignes dont l'origine est un passage du manuscrit sans entrée au REF.
#
# Aucun texte de note n'est recopié ici : l'ancrage cite la section et, quand le
# raisonnement vit dans une note de fin, son identifiant. Le texte est tiré du
# relevé `Notes_manuscrit_AAAAMMJJ_vN.json` au moment de la génération. Une note
# recopiée serait un cache que personne ne rafraîchit.
#
# (id, section, notes citées, libellé court du passage)
# ------------------------------------------------------------------ l'ordre
# Ordre de lecture, du plus large au plus particulier. Les rentes ferment, parce
# qu'elles sont l'argument offensif et non une situation où le lecteur se range.
GROUPES = [
 ("Tout le monde",
  "Ce que le plan change pour chacun, quel que soit son état.",
  ["C-00","C-02","C-01","C-03"]),
 ("Le travail et l'entreprise",
  "Ceux qui vivent de leur travail ou le font vivre.",
  ["C-04","C-10","C-06","C-24","C-05","C-30","C-18","C-19"]),
 # Le jeune adulte est un âge de la vie, non un statut d'emploi : arbitrage de
 # l'auteur du 20260828. Il se range entre l'enfance et la parentalité.
 ("La famille et les âges de la vie",
  "L'enfance, la parentalité, la retraite, la transmission.",
  ["C-15","C-16","C-17","C-43","C-09","C-39","C-21"]),
 ("Se loger, se soigner, se former",
  "Les services que le plan réordonne.",
  ["C-11","C-12","C-40","C-13","C-14","C-42","C-45","C-08"]),
 ("Épargner et consommer",
  "Le patrimoine, les prix, le pouvoir d'achat.",
  ["C-22","C-23","C-46"]),
 ("La vie civique et associative",
  "La commune, le mandat, l'engagement bénévole.",
  ["C-20","C-37","C-38","C-07","C-34"]),
 ("Quand un dispositif public tient lieu de ressource",
  "Les situations où le plan retire une aide et ouvre une autre voie.",
  ["C-31","C-32","C-33","C-35","C-36","C-41","C-44","C-47","C-48"]),
 ("Les rentes supprimées",
  "Ceux dont le métier était le dispositif lui-même.",
  ["C-50","C-51","C-52","C-53","C-54","C-55","C-56","C-57","C-58","C-59",
   "C-60","C-61"]),
]

# ----------------------------------------------------------- les promesses
# L'ordre d'une fiche ne se tire ni de l'identifiant ni de l'alphabet. Il suit
# la chaîne du manuscrit : ce qui est rendu d'abord, ce qui l'accompagne
# ensuite, la modalité en dernier. Les ancrages ci-dessous sortent en tête,
# dans cet ordre, partout où ils figurent. Le reste suit l'ordre des axes.
PROMESSES = [
 "D3-2-2-e1",      # 600 € par mois rendus au travailleur type
 "D3-2-1-e1",      # +13 % sur tous les salaires nets
 "D9-2-1-e1",      # aide fondamentale de 550 € versée sans dossier
 "D9-2-1",         # versement automatique de l'aide fondamentale
 "D9-4-1-e1",      # 275 € par mois et par enfant
 "D7-2-1-e1",      # 20 000 € de patrimoine public restitué par foyer
 "D7-2-2-e1",      # complément viager des retraités actuels
 "D7-2-2-e2",      # rendement annuel du patrimoine restitué
 "D10-2-1-e1",     # compte éducation, 6 600 € par an et par enfant
 "D9-3-1-e1",      # 77 centimes nets par euro gagné
 "D9-2-3-e1",      # 1 100 € par mois pour le handicap
 "D8-2-2-e1",    # la retraite en capital, l'essentiel des comptes personnels
 "D8-4-1-e1",      # reste à charge de 10 %, plafonné à 5 % du revenu
 "D8-3-1-e2",      # cotisations chômage transformées en épargne
 "D6-2-2",         # plan de départ, 70 % pendant 7 ans
 "D6-3-2-e2",      # +13 % de rémunération des agents publics
 "D7-3-1-e1",      # détente du marché locatif
 "D4-3-3-e2",      # suppression des impôts de production
 "D11-4-2",        # modalité : restitution par paliers de 2 % par mois
 "M-simplification",   # gain d'ensemble de la simplification
 "M-croissance-itci",  # points de croissance rendus par la fiscalité simple
 "D11-e1",         # taux de prélèvements ramené à 36 %
 "M-un-point",     # un point d'efficacité suffit au rythme des traités
]

# ------------------------------------------------------------- le diagnostic
# La position `diagnostic` décrit l'état présent, jamais un effet du plan. Un
# écart mesuré avec les pays comparables et un risque porté par la dette ne sont
# pas des pertes causées par la réforme : ils disent le possible et ce qui
# menace. Ils ne se comptent ni avec les gains ni avec les pertes, et ne se
# promettent pas.

# --------------------------------------------------------------- l'éventail
# "ancrage|position|categorie" de la ligne mère → catégories filles. Le gain
# atteint aussi ces catégories, par la même voie et avec le même miroir.
EVENTAIL = {
 "D6-3-1|perdant|C-05": ["C-19"],
 "D2-4-1-s1|perdant|C-32": ["C-11"],
 # -- attaches arbitrées à la carte d'attribution (A-180) : un effet se déplie
 # vers la catégorie où il est le plus pertinent
 "D7-2-2-e2|gagnant|C-02": ["C-03"],
 "D10-4-1-e5|gagnant|C-04": ["C-03"],
 "D4-ei1|gagnant|C-00": ["C-06"],
 "D4-ei2|gagnant|C-00": ["C-06"],
 "D8-ei1|gagnant|C-00": ["C-06"],
 "D9-4-2-e2|gagnant|C-15": ["C-17"],
 "D10-4-1-e3|perdant|C-42": ["C-16"],
 "D8-3-1|perdant|C-41": ["C-10"],
 "D9-3-1-e7|perdant|C-39": ["C-09"],
 "D7-3-1|perdant|C-40": ["C-11"],
 "D4-3-2|perdant|C-46": ["C-23"],
 # -- le quotient familial et les majorations touchent le parent, non le foyer
 # comme simple unité de mesure
 "D9-4-1|perdant|C-03": ["C-17"],
 # -- le salaire et la restitution atteignent tout ce qui vit du travail
 "D3-2-1-e1|gagnant|C-04": ["C-10","C-16","C-30","C-31","C-34","C-41","C-46",
                            "C-07","C-33","C-11"],
 "D3-2-2-e1|gagnant|C-04": ["C-16"],
 "D9-3-1-e1|gagnant|C-04": ["C-06","C-16","C-10"],
 "D9-3-1-e2|gagnant|C-04": ["C-16"],
 "D11-4-2|gagnant|C-04": ["C-16"],
 # -- la retraite par capitalisation vaut d'abord pour qui a une carrière devant
 "D8-2-1-e2|gagnant|C-04": ["C-16"],
 "D8-2-2-e2|gagnant|C-04": ["C-16"],
 "D8-2-2-e4|gagnant|C-04": ["C-09","C-16"],
 "D8-3-1-e2|gagnant|C-04": ["C-10","C-41"],
 "D8-3-1-e1|gagnant|C-10": ["C-41"],
 # -- l'aide fondamentale atteint toutes les situations de ressource
 "D9-2-1-e1|gagnant|C-02": ["C-10","C-32","C-43","C-31","C-40","C-45","C-41"],
 "D9-2-1|gagnant|C-16": ["C-32","C-43"],
 "D2-4-1-e1|gagnant|C-32": ["C-10"],
 # -- la solidarité envers l'enfance
 "D9-4-1-e1|gagnant|C-17": ["C-15","C-43","C-03"],
 # -- l'école et le compte éducation
 "D10-2-1-e1|gagnant|C-15": ["C-17","C-42"],
 "D10-3-1-e4|gagnant|C-15": ["C-17"],
 "D10-4-2-e1|gagnant|C-16": ["C-42"],
 # -- le patrimoine restitué
 "D7-2-1-e1|gagnant|C-03": ["C-22","C-09","C-16"],
 "D7-2-2-e1|gagnant|C-09": ["C-39"],
 # -- le logement
 "D7-3-1-e1|gagnant|C-11": ["C-16","C-40"],
 # -- la santé
 "D8-4-1-e1|gagnant|C-13": ["C-09","C-14","C-39"],
 "D8-4-2-e1|gagnant|C-03": ["C-13"],
 "D8-4-2-e2|gagnant|C-13": ["C-44"],
 # -- la fiscalité lisible et les taxes supprimées
 "D4-3-1-e1|gagnant|C-01": ["C-06","C-33","C-35"],
 "D4-3-2-e1|gagnant|C-01": ["C-23","C-46"],
 "D4-3-3-e1|gagnant|C-23": ["C-46"],
 "D4-3-3-e2|gagnant|C-06": ["C-33","C-24"],
 "D2-5-1-e1|gagnant|C-01": ["C-35","C-06"],
 "D4-4-1-e1|gagnant|C-21": ["C-03","C-11"],
 # -- la simplification et la sanction plutôt que l'autorisation
 "D4-2-3|gagnant|C-06": ["C-07","C-34","C-33","C-23"],
 "D3-ei1|gagnant|C-06": ["C-33"],
 "D4-2-1-e1|gagnant|C-02": ["C-06"],
 # -- la commune et le mandat
 "D5-2-1-e1|gagnant|C-20": ["C-02","C-38"],
 "D5-3-2-e1|gagnant|C-20": ["C-37"],
 # -- l'État recentré
 "D2-3-1-e1|gagnant|C-02": ["C-31"],
 "D6-ei2|gagnant|C-02": ["C-44"],
}

ANCRAGES_MANUSCRIT = {
 "M-suisse-revenu": ("P1-C1-tous-perdants-du-systeme-actuel", ["e8"],
  "Revenu réel médian suisse contre français, et creusement de l'écart"),
 "M-suisse-emploi": ("P1-C4-de-nul-nest-cense-ignorer-la-loi-a-nul-ne-peut-c", ["e57", "e58"],
  "Volume du code du travail et taux de chômage comparés"),
 "M-paysbas": ("P1-C1-tous-perdants-du-systeme-actuel", ["e9"],
  "Pouvoir d'achat, congés ou âge de départ à économie néerlandaise"),
 "M-productivite-heure": ("P1-C2-un-francais-est-mieux-paye-par-son-entreprise-qu", ["e12", "e13"],
  "Richesse produite par heure travaillée et part récupérée en net"),
 "M-productivite-norme": ("P2-C5-les-gains-de-productivite-devraient-etre-la-bous", ["e102"],
  "La simplification des normes, seul levier rapide de productivité"),
 "M-propriete": ("P2-C5-les-normes-soccupent-aujourdhui-deux-fois-plus-d", ["e102"],
  "La protection de la propriété comme clef de la prospérité"),
 "M-risque-crise": ("epilogue-C1-un-etat-qui-sendette-augmente-chaque-jour-le-ris", ["e140"],
  "Endettement, marges qui se réduisent et épargne de précaution"),
 "M-crise-souveraine": ("epilogue-C1-un-etat-qui-sendette-augmente-chaque-jour-le-ris", ["e141"],
  "Ajustement imposé par une rupture d'accès au crédit souverain"),
 "M-un-point": ("epilogue-C1-le-prix-du-statu-quo", [],
  "Un point d'efficacité ou de croissance suffit au rythme des traités"),
 "M-multiplicateur": ("epilogue-C1-et-si-la-france-netait-pas-destinee-a-la-defaite", [],
  "Complémentarité et effet multiplicateur des mesures"),
 "M-pauvrete": ("P1-C5-un-record-de-depenses-pas-de-solidarite", ["e70"],
  "Premier niveau de dépense, deuxième taux de sans-abri de l'OCDE"),
 "M-simplification": ("P1-C3-leuro-empeche", ["e32", "e33", "e34"],
  "Conversion du travail administratif imposé en travail productif"),
 "M-croissance-itci": ("P2-C5-supprimons-toutes-ces-taxes-en-trop-et-fusionnon", ["e106"],
  "Passage du 36e au 1er rang de compétitivité fiscale"),
 "M-estonie": ("P2-C5-faisons-simple", [],
  "Le système fiscal estonien comme référence de cible"),
 "M-ricardo": ("P1-C3-leuro-preleve", ["e27", "e140", "e12"],
  "Mesure de la pression fiscale et portée du produit intérieur brut"),
 "M-taxes-affectees": ("P2-C5-supprimons-toutes-ces-taxes-en-trop-et-fusionnon", ["e107"],
  "Taxes spécifiques et capture de leur produit"),
 "M-rente-statut": ("P2-C3-les-agents-dont-les-postes-seront-supprimes-cons", ["e93"],
  "Le plan de départ solde les rentes créées par le statut"),
 "M-frais-gestion-sante": ("P3-C3-choisissons-librement-avec-nos-cotisat", ["e129"],
  "Frais de gestion cumulés de la couverture santé"),
}

# --------------------------------------------------------------------- lignes
# (ancrage, position, categorie, echelle, nature, degre, grandeur, miroir,
#  raccroche, note)
# grandeur : "" quand le REF la porte ; "qualitatif" quand l’effet en est un ;
# sinon la valeur dérivée, précédée de son opération.
Q = "qualitatif"
AUCUNE = "aucune, par construction"
RECONST = "reconstitution volontaire du flux"

L = [
# ================================================== C-00, le gain d'ensemble
#
# Deux registres, tenus séparés. Ce que la France perd aujourd'hui, mesuré par
# l'écart avec les pays comparables : c'est un constat, il se dit précis. Ce que
# le plan rend, sobrement : un ordre de grandeur et beaucoup de qualitatif.
# L'écart mesure le possible, il ne se promet pas.
#
# -- ce que le système actuel coûte : l'écart, position perdante d'aujourd'hui
("M-productivite-heure","diagnostic","C-00","macro","revenu","nommé",
 "63 € de richesse produite par heure travaillée, 23 € nets récupérés, 11 € aux "
 "propriétaires du capital","","M-simplification|gagnant|C-00",
 "Le gisement, non le gain. L'écart entre 63 et 23 mesure ce qui se perd en "
 "route ; le plan n'en récupère qu'une part, et elle se chiffre ailleurs."),
("M-suisse-revenu","diagnostic","C-00","macro","revenu","nommé",
 "4 300 € contre 2 100 € de revenu réel médian mensuel ; écart creusé de moitié "
 "en vingt ans","","M-simplification|gagnant|C-00",
 "Illustration du possible, à ne jamais présenter comme une cible du plan."),
("M-suisse-emploi","diagnostic","C-00","macro","statut","nommé",
 "chômage supérieur à 8 % en France, plein emploi en Suisse ; 4 000 pages de "
 "code du travail contre 200","","M-simplification|gagnant|C-00",
 "Illustration du possible, à ne jamais présenter comme une cible du plan."),
("M-paysbas","diagnostic","C-00","macro","revenu","nommé",
 "+25 % de pouvoir d'achat, ou deux mois de congés supplémentaires, ou un "
 "départ en retraite à 55 ans, à économie néerlandaise","","M-simplification|gagnant|C-00",
 "Illustration du possible, à ne jamais présenter comme une cible du plan."),
("M-pauvrete","diagnostic","C-00","macro","service","nommé",
 "deuxième taux de personnes sans domicile fixe de l'OCDE malgré le premier "
 "niveau de dépense publique","","D9-2-1-e1|gagnant|C-02",""),
("M-risque-crise","diagnostic","C-00","macro","risque","nommé",
 "épargne de précaution des Français au niveau record de 18 %","",
 "D11-e1|gagnant|C-00",
 "Le risque de crise est une perte portée aujourd'hui : elle se paie en épargne "
 "immobilisée par précaution."),
("D11-1-1","diagnostic","C-00","macro","patrimoine","nommé",
 "5 500 € par an et par foyer de dette publique supplémentaire","","D11-e1|gagnant|C-00",
 "5 500 € par an et par foyer de dette publique supplémentaire."),
#
# -- ce que le plan rend : sobre, un chiffre et du qualitatif déclaré
("M-simplification","gagnant","C-00","macro","revenu","nommé",
 "de l'ordre de +10 %, soit environ 10 000 € par foyer et par an de gain de "
 "qualité de vie","M-productivite-heure|diagnostic|C-00","",
 "Le seul gain d'ensemble que le manuscrit chiffre en propre, et il le donne en "
 "ordre de grandeur. Déclaré absent du référentiel dans le bloc des lacunes."),
("M-croissance-itci","gagnant","C-00","macro","revenu","nommé",
 "de l’ordre de 5 points de croissance économique, en passant du 36e au 1er rang "
 "de l’indice de compétitivité fiscale","M-suisse-emploi|diagnostic|C-00","",
 "Seconde grandeur du gain d’ensemble, sourcée en économétrie : Christl et "
 "Köppl-Turyna 2026 sur l’International Tax Competitiveness Index, plus calculs "
 "Résolution. Porte sur la complexité fiscale. À ne pas additionner sans examen "
 "avec les 10 % de M-simplification, qui portent sur la charge administrative : "
 "les deux leviers sont distincts, leur recouvrement n’est pas instruit."),
("D11-e1","gagnant","C-00","macro","revenu","indiqué","","D11-1-1|diagnostic|C-00","",
 "42,87 % à 36,33 % du produit intérieur brut, 191,046 Md€ de prélèvements en "
 "moins. Le seul gain d'ensemble porté au référentiel."),
("M-estonie","gagnant","C-00","macro","statut","nommé",Q,"M-suisse-emploi|diagnostic|C-00","",
 "Référence de cible : quatre impôts, taux unique de 22 %, première place au "
 "classement de compétitivité fiscale, dette nette la plus faible d'Europe. Le "
 "chiffrage du gain associé est porté par M-croissance-itci, non ici. La lacune "
 "du référentiel — 5 points de croissance, aucune entrée — est exacte : "
 "l'énoncé figure au manuscrit, en note e106, et non au REF."),
("M-un-point","gagnant","C-00","macro","statut","nommé",
 "1 % d'efficacité sur la dépense publique, ou 1 % de croissance en plus, suffit "
 "à redresser le déficit au rythme des traités","M-risque-crise|diagnostic|C-00","",
 "Mesure la modestie de l'effort requis, non l'ampleur du gain."),
("M-propriete","gagnant","C-00","macro","liberté","nommé",Q,"D7-4-1|perdant|C-56","",
 "La protection du droit de propriété rend l'avenir moins risqué, libère "
 "l'innovation et élève le niveau de vie de tous."),
("M-productivite-norme","gagnant","C-00","macro","statut","nommé",Q,
 "M-productivite-heure|diagnostic|C-00","",
 "La simplification des normes est le seul levier rapide de productivité, les "
 "leviers classiques étant longs et incertains. Chiffrage porté par "
 "M-simplification, aucun autre."),
("D11-ei3","gagnant","C-00","macro","statut","nommé",Q,"D11-1-1|diagnostic|C-00","",
 "Effet multiplicateur : chaque simplification ouvre la suivante."),
("D11-ei4","gagnant","C-00","macro","revenu","nommé",Q,"D11-1-1|diagnostic|C-00","",
 "Le corpus déclare ses prévisions prudentes et le surplus non chiffré."),
("D11-ei2","gagnant","C-00","macro","statut","nommé",Q,"D11-1-1|diagnostic|C-00","",""),
("D3-ei3","gagnant","C-00","macro","statut","nommé",Q,"D2-1-1|perdant|C-31","",""),
("D3-ei4","gagnant","C-00","macro","statut","nommé",Q,"D2-1-1|perdant|C-31","",""),
("D4-ei1","gagnant","C-00","macro","risque","nommé",Q,"M-estonie|gagnant|C-00","",""),
("D4-ei2","gagnant","C-00","macro","statut","nommé",Q,"M-estonie|gagnant|C-00","",""),
("D6-ei5","gagnant","C-00","macro","statut","nommé",Q,"D6-2-1-e1|perdant|C-30","",""),
("D8-ei1","gagnant","C-00","macro","patrimoine","nommé",Q,"D8-3-1|perdant|C-41","",""),
("D8-ei2","gagnant","C-00","macro","revenu","nommé",Q,"D8-3-1|perdant|C-41","",""),
# -- apports du balayage des notes de fin
("M-crise-souveraine","diagnostic","C-00","macro","risque","nommé",
 "au moins 7 % d’ajustement des dépenses sous l’hypothèse la plus optimiste, "
 "plus probablement une ou plusieurs dizaines de points","","D11-e1|gagnant|C-00",
 "Le facteur crise, chiffré. C’est le coût du risque porté aujourd’hui, non un "
 "effet de la réforme."),
("M-ricardo","gagnant","C-00","macro","statut","nommé",Q,"M-crise-souveraine|diagnostic|C-00","",
 "Deux niveaux de lecture assumés, comme pour l’entreprise. L’agrégat classique "
 "— le taux de prélèvements obligatoires — se cite tel quel et se compare. La "
 "modulation, portée aux notes e27, e140 et e12, dit que la pression réelle se "
 "mesure à la dépense publique déficit inclus, et que le produit intérieur brut "
 "surestime la richesse collective. Les deux se tiennent ensemble : le premier "
 "chiffre, le second qualifie."),
("M-ricardo","gagnant","C-00","macro","risque","nommé",Q,"M-crise-souveraine|diagnostic|C-00","",
 "Premier gain qualitatif de la modulation : ce qui est financé par déficit est "
 "un impôt différé, donc un risque porté. Le réduire baisse le risque de crise "
 "sans qu’aucun agrégat ne l’enregistre."),
("M-ricardo","gagnant","C-00","macro","service","nommé",Q,"M-crise-souveraine|diagnostic|C-00","",
 "Second gain qualitatif : la contribution publique étant comptée à hauteur de "
 "ce qu’elle coûte, toute amélioration de la qualité de la dépense est invisible "
 "au produit intérieur brut. Le gain existe et ne se mesure pas là."),
("M-taxes-affectees","capteur","C-51","méso","revenu","nommé",
 "16 Md€ de taxes spécifiques ; eau 2,1, transports 1,9, spectacles et "
 "divertissements 0,8","",RECONST,
 "Capteur nommé par la note : le produit de la taxe affectée finance une "
 "dépense au profit de celui qui l’a obtenue."),
("M-rente-statut","capteur","C-05","méso","statut","nommé",Q,"",RECONST,
 "La note qualifie explicitement de rente ce que le plan de départ solde. Le "
 "statut est le capteur, non l’agent."),
("M-frais-gestion-sante","capteur","C-58","macro","revenu","nommé",
 "16,9 Md€ par an de frais de gestion cumulés des mutuelles, des "
 "administrations de sécurité sociale et du ministère","",RECONST,
 "Chiffre le capteur au niveau macro, là où D8-4-2 le donne par foyer."),
# ============================================================ D1
("D1-1-1","gagnant","C-02","macro","liberté","nommé",Q,"D1-1-1|perdant|C-50","",
 "Proposition sans effet au référentiel. Position dérivée de la proposition."),
("D1-1-1","perdant","C-50","méso","statut","déduit",Q,"",AUCUNE,
 "L’audit permanent prive la structure de l’opacité qui la protège."),
("D1-2-1","gagnant","C-02","macro","liberté","nommé",Q,"D1-2-1|perdant|C-31","",
 "Proposition sans effet au référentiel."),
("D1-2-1","perdant","C-31","micro","service","déduit",Q,"","D3-2-2-e1|gagnant|C-04",
 "Le consentement périodique expose chaque mission facultative au retrait."),
("D1-3-1","gagnant","C-01","macro","statut","nommé",Q,"D1-3-1|perdant|C-56","",
 "Proposition sans effet au référentiel."),
("D1-3-1","perdant","C-56","méso","statut","nommé",Q,"",AUCUNE,
 "La sanction aggravée vise celui qui tire un privilège de sa fonction."),
("D1-ed1","capteur","C-56","méso","revenu","nommé",Q,"",AUCUNE,
 "Diagnostic : « leur addition pèse des milliards chaque année »."),
# ============================================================ D2
("D2-1-1","perdant","C-31","micro","service","nommé",Q,"","D3-2-2-e1|gagnant|C-04",
 "Toute action publique hors des sept missions cesse."),
("D2-1-1-e1","","","macro","","","","","",
 "Effet de nature agrégat : aucune position propre. Les positions appartiennent "
 "à ses cinq composants, sous peine de double compte."),
("D2-2-1-e2","gagnant","C-01","macro","revenu","indiqué",
 "35 € par mois et par foyer","D2-2-1|perdant|C-30","",
 "Économies de fonctionnement des structures fermées. Opération : 12,432 Md€ "
 "/ 30 M foyers / 12 = 34,53 €, forme canonique 35 € au rang de la promesse."),
("D2-2-1","perdant","C-30","micro","revenu","indiqué",
 "qualitatif","","D6-2-2|gagnant|C-30",
 "Le décompte à date est de 580 000 postes publics, soit 10 % des 5,8 M (A-130). Le 0,54 M du classeur est périmé et ne sort plus."),
("D2-2-1","perdant","C-31","micro","service","nommé",Q,"","D9-2-1-e1|gagnant|C-02",
 "Agence nationale de la cohésion des territoires, institut français du cheval "
 "et de l’équitation, centre national de la propriété forestière, conseil "
 "national du bruit."),
("D2-2-1","capteur","C-50","méso","statut","nommé","750 structures sur 1 104","",AUCUNE,
 "Le capteur le plus directement énoncé du corpus."),
("D2-2-1","capteur","C-51","méso","revenu","nommé",Q,"",AUCUNE,""),
("D2-2-1","capteur","C-61","méso","revenu","indiqué",
 "29,3 Md€ de flux d’aides redistribués par les opérateurs fermés","",AUCUNE,
 "France Compétences 10,6 ; France Travail 2,7 ; agences de l’eau 2,1 ; Action "
 "Logement 1,9. Ces montants sont des flux d’aides comptés en D2-4, non le "
 "fonctionnement de 12,4 Md€ porté par D2-2-1-e2."),
("D2-2-1-e3","","","","","","","","",
 "« Rien ne se passe. » Effet nul : pas de miroir, position sans objet."),
("D2-3-1-e1","gagnant","C-02","macro","service","nommé",Q,"D2-3-1|capteur|C-51","",""),
("D2-3-1","capteur","C-51","méso","revenu","nommé","55 agences réinternalisées","",AUCUNE,
 "Délégataires du régalien : amendes, documents d’identité."),
("D2-3-1","perdant","C-50","méso","statut","déduit",Q,"","D6-3-1-e2|gagnant|C-05",
 "Perte d’autonomie, non de revenu : l’agent est transféré, non licencié."),
("D2-3-2-e1","gagnant","C-08","méso","statut","nommé","303 établissements","D2-3-2|perdant|C-08","",""),
("D2-3-2","perdant","C-08","méso","revenu","déduit",Q,"","D10-4-2-e1|gagnant|C-08",
 "Fin de la subvention d’équilibre. L’effet du référentiel porte le signe + sur "
 "une position ambivalente."),
("D2-4-1-e2","gagnant","C-01","macro","revenu","indiqué",
 "190 € par mois et par foyer","D2-4-1-s1|perdant|C-32","",
 "Opération : 68,948 Md€ / 30 M foyers / 12 = 191,52 €, forme canonique 190 € "
 "au rang de la promesse, arrondi prudentiel vers le bas."),
("D2-4-1-e1","gagnant","C-32","micro","revenu","nommé","","D2-4-1-s1|perdant|C-32","",
 "Lacune déclarée au référentiel : la perte est par foyer, le gain par personne, "
 "les deux ne se soustraient pas."),
("D2-4-1-s1","perdant","C-32","micro","revenu","nommé","","","D9-2-1-e1|gagnant|C-02",
 "Aide personnalisée au logement, parc social et privé. Le classeur ne dénombre "
 "que les 3,5 M de locataires du parc social."),
("D2-4-1-s2","perdant","C-33","méso","revenu","nommé","","","D4-3-3-e2|gagnant|C-06",""),
("D2-4-1-s2","perdant","C-10","micro","revenu","nommé","","","D3-2-1-e1|gagnant|C-04",""),
("D2-4-1-s3","perdant","C-33","méso","revenu","nommé","","","D4-3-3-e2|gagnant|C-06",""),
("D2-4-1-s4","perdant","C-36","macro","service","nommé","","",AUCUNE,
 "Perdant situé hors de la communauté nationale. Le projet n’a pas de voie de "
 "raccroche à lui offrir, et n’en revendique aucune : l’impôt d’un pays finance "
 "les services rendus à ceux qui l’acquittent."),
("D2-4-1-s5","perdant","C-45","micro","service","nommé","","",AUCUNE,
 "Hors socle de 20 % conservé pour les femmes battues et les enfants."),
("D2-4-1-s6","perdant","C-10","micro","revenu","nommé","","","D3-2-1-e1|gagnant|C-04",""),
("D2-4-1-s7","perdant","C-44","micro","risque","nommé","","",AUCUNE,
 "Hors 10 % de soins urgents conservés."),
("D2-4-1-s8","perdant","C-03","micro","revenu","nommé","","","D3-2-1-e1|gagnant|C-04",
 "Exonérations sur l’emploi à domicile."),
("D2-4-1-s9","perdant","C-32","micro","revenu","nommé","","","D9-2-1-e1|gagnant|C-02",
 "Chèque énergie, politique de la ville."),
("D2-4-1","gagnant","C-07","méso","revenu","déduit",Q,"D2-4-1-e2|perdant|C-34","",
 "Association vivant de dons et de produits propres : la population donatrice "
 "dispose d’un reste à vivre accru et la mission libérée par l’État lui revient. "
 "Le manuscrit nomme la Fondation de France, Emmaüs et la Société nationale de "
 "sauvetage en mer comme modèle, non comme perdants."),
("D2-4-1-e2","perdant","C-34","méso","revenu","nommé",
 "3,2 Md€ de subventions aux associations, ligne 22 du tableau de référence","","D3-2-1-e1|gagnant|C-04",
 "Raccroche par le mécénat : le donateur potentiel dispose d’un reste à vivre accru."),
("D2-4-1-e2","perdant","C-37","méso","statut","nommé",
 "12,3 Md€ d’aides locales aux entreprises, ligne 18 du tableau de référence","",AUCUNE,
 "Perte d’instrument, non de revenu : la collectivité cesse de subventionner."),
("D2-ed6","capteur","C-54","méso","revenu","implicite",Q,"",AUCUNE,
 "Le manuscrit démontre la capture sans qualifier le bailleur de capteur."),
("D2-ed8","capteur","C-52","méso","revenu","nommé",Q,"",AUCUNE,""),
("D2-ed11","capteur","C-56","méso","statut","nommé",Q,"",AUCUNE,""),
("D2-ed12","capteur","C-60","méso","revenu","nommé",Q,"",AUCUNE,""),
("D2-ed13","capteur","C-55","méso","revenu","nommé",Q,"",AUCUNE,""),
("D2-ed15","capteur","C-53","méso","revenu","nommé",Q,"",AUCUNE,""),
("D2-5-1-e2","gagnant","C-01","macro","revenu","indiqué",
 "140 € par mois et par foyer restitués directement",
 "D2-5-1|perdant|C-35","",
 "Opération : 52,1 Md€ / 30 M foyers / 12 = 144,72 €, forme canonique 140 € "
 "au rang de la promesse, arrondi prudentiel vers le bas."),
("D2-5-1-e1","gagnant","C-01","macro","statut","nommé",Q,"D2-5-1|perdant|C-35","",
 "Garantie de non-hausse de la pression fiscale."),
("D2-5-1","perdant","C-35","méso","revenu","nommé","143,2 Md€ de niches supprimées","",
 "D4-3-3-e2|gagnant|C-06",
 "Perdants nommés au manuscrit : Sanofi, plus de 100 M€ par an au titre du crédit "
 "d’impôt recherche ; hôtels de luxe en Polynésie ; jeux vidéo, 66 M€ par an."),
# ============================================================ D3
("D3-2-1-e1","gagnant","C-04","micro","revenu","nommé","","D2-1-1|perdant|C-31","",
 "La raccroche centrale du projet : tout perdant d’une aide est renvoyé ici."),
("D3-2-1-e2","perdant","C-06","macro","revenu","indiqué",
 "solde net des entreprises à un an : −38 Md€","","D4-3-3-e2|gagnant|C-06",
 "Deux niveaux de lecture assumés. Au niveau de l’entreprise, la neutralité "
 "fiscale tient : les prélèvements nets de subventions et d’aides sont stables. "
 "Le solde de −38,17 Md€ se lit au niveau du propriétaire, par la marge. "
 "L’input brouillon énonce le premier niveau, le référentiel le second."),
("D7-2-2","perdant","C-09","micro","revenu","déduit","qualitatif","",
 "D7-2-2-e1|gagnant|C-09",
 "La fin des indexations automatiques est au manuscrit — le complément viager de 500 €/an la compense explicitement, avec la fin des niches. Elle n’avait aucune ligne au référentiel avant le 20260828."),
("D3-2-1-e3","perdant","C-09","micro","revenu","nommé","","","D7-2-2-e1|gagnant|C-09",
 "Les revenus de remplacement restent hors du champ de la suppression."),
("D3-2-1-e4","perdant","C-02","macro","revenu","nommé","","","D3-2-1-e1|gagnant|C-04",
 "Effet inflation, qui réduit le gain sans l’annuler."),
("D3-2-2-e1","gagnant","C-04","micro","revenu","nommé","","D2-1-1|perdant|C-31","",""),
("D3-ei1","gagnant","C-06","macro","revenu","nommé",Q,"D2-1-1|perdant|C-31","",""),
("D3-ei2","gagnant","C-10","macro","revenu","nommé",Q,"D2-1-1|perdant|C-31","",""),
("D3-ed3","capteur","C-51","méso","revenu","implicite",Q,"",AUCUNE,
 "La chaîne de prélèvement sur la boulangerie."),
# ============================================================ D4
("D4-2-1-e1","gagnant","C-02","macro","liberté","nommé",Q,"D4-ed16|capteur|C-53","",""),
("D4-2-3","gagnant","C-06","méso","liberté","nommé",Q,"D4-2-3|perdant|C-51","",
 "Ancrage porté sur la proposition. Les trois effets e1 à e3 énoncent le "
 "système actuel et non le gain produit : requalifiés en diagnostic au REF. "
 "Lacune déclarée : D4-2-3 ne porte aucun effet positif au référentiel."),
("D4-2-3","gagnant","C-02","macro","liberté","nommé",Q,"D4-2-3|perdant|C-51","",
 "Même ancrage, même lacune. La liberté d’entreprendre sans autorisation "
 "préalable se déduit de la proposition, elle n’est pas énoncée en effet."),
("D4-2-3","perdant","C-51","méso","revenu","déduit",Q,"",AUCUNE,
 "L’autorisation préalable fait vivre l’instructeur du dossier."),
("D4-3-1-e1","gagnant","C-01","macro","statut","nommé",Q,"D4-ed17|perdant|C-48","",""),
("D4-ed17","perdant","C-48","méso","revenu","nommé",Q,"",AUCUNE,""),
("D4-ed16","capteur","C-53","méso","revenu","nommé",Q,"",AUCUNE,""),
("D4-ed18","capteur","C-57","méso","revenu","nommé",Q,"",AUCUNE,""),
("D4-3-2-e1","gagnant","C-01","macro","revenu","indiqué","","D4-3-2|perdant|C-46","",
 "Effet porté au signe négatif avec « complexité fiscale » en bénéficiaire : "
 "grandeur écrite là où une personne est attendue."),
("D4-3-2","perdant","C-46","micro","revenu","déduit",
 "21 taux réduits non comptabilisés en niche, 33 Md€","",
 "D3-2-1-e1|gagnant|C-04",
 "Le passage au taux unique de 20 % renchérit les biens aujourd’hui à taux "
 "réduit. Bornes de la grandeur reprises de D2-5-1-p1 : 33,382 Md€ exact."),
("D4-3-3-e1","gagnant","C-23","macro","revenu","nommé","","D4-3-3|perdant|C-06","",""),
("D4-3-3-e1","gagnant","C-24","méso","revenu","nommé","","D4-3-3|perdant|C-06","",""),
("D4-3-3","perdant","C-06","méso","revenu","nommé",
 "hausse transitoire de quelques points d’impôt sur les sociétés","","D4-3-3-e1|gagnant|C-23",
 "Ambivalence assumée : l’entreprise perd sur le bénéfice ce qu’elle gagne sur "
 "les impôts de production."),
("D4-3-3-e2","gagnant","C-06","méso","revenu","nommé",
 "suppression de la totalité des taxes et impôts de production","D4-3-3|perdant|C-06","",
 "Raccroche de toute entreprise perdant une subvention ou une niche."),
("D9-3-1-e3","gagnant","C-03","micro","revenu","nommé",Q,"D9-3-1-e7|perdant|C-39","",
 "Seuil d’entrée dans l’impôt stable pour un foyer type."),
("D9-4-1-e2","gagnant","C-16","micro","liberté","nommé",Q,"D9-4-1|perdant|C-43","",""),
("D9-2-1-e1","gagnant","C-16","micro","revenu","déduit",
 "550 € par mois dès dix-huit ans, versés sans dossier","D2-4-1-s1|perdant|C-32","",
 "L'aide universelle de 275 € court de la naissance à dix-huit ans ; l'aide "
 "fondamentale à taux plein prend le relais à la majorité. La solidarité de base "
 "actuelle est fermée aux moins de vingt-cinq ans : l'ouverture à dix-huit ans "
 "est le gain propre de cette catégorie, déduit de deux paramètres nommés."),
("D9-2-1","gagnant","C-16","micro","service","nommé",
 "versement automatique, sans dossier ni formulaire","D2-4-1-s1|perdant|C-32","",
 "Le formulaire actuel compte sept pages ; un tiers des éligibles n'y recourt "
 "pas. La suppression du dossier vaut d'abord pour ceux qui entrent dans la vie "
 "adulte sans historique administratif."),
("D10-3-1-e5","gagnant","C-08","méso","patrimoine","nommé",Q,"D10-4-2|perdant|C-08","",""),
("D10-4-1-e2","gagnant","C-16","micro","patrimoine","nommé",Q,"D10-4-1-e3|perdant|C-42","",""),
("D10-4-1-e4","gagnant","C-16","micro","liberté","nommé",Q,"D10-4-1-e3|perdant|C-42","",""),
("D10-4-1-e5","gagnant","C-04","micro","statut","nommé",Q,"D10-4-1-e3|perdant|C-42","",""),
("D10-4-2-e2","gagnant","C-16","micro","service","nommé",Q,"D10-4-2|perdant|C-08","",""),
("D4-4-1-e1","gagnant","C-21","micro","patrimoine","nommé",Q,"D4-4-1|perdant|C-01","",""),
("D4-4-1-e1","gagnant","C-12","micro","patrimoine","nommé",Q,"D4-4-1|perdant|C-01","",""),
("D4-4-1","perdant","C-01","macro","revenu","complété",Q,"","D4-3-3-e1|gagnant|C-23",
 "La taxe foncière unique en euros par mètre carré redistribue la charge entre "
 "propriétaires. Les perdants de la nouvelle assiette ne sont pas identifiés au "
 "corpus. À instruire."),
("D4-4-2-e1","gagnant","C-21","micro","patrimoine","nommé","","D4-4-1|perdant|C-01","",""),
# ============================================================ D5
("D5-2-1-e1","gagnant","C-20","micro","liberté","nommé",Q,"D5-2-1-e2|perdant|C-38","",""),
("D5-2-1-e2","gagnant","C-01","macro","revenu","indiqué",
 "27 € par mois et par foyer","D5-2-1-e2|perdant|C-38","",
 "Opération : 9,6 Md€ / 30 M foyers / 12 = 26,67 €, forme canonique 27 €."),
("D5-2-1-e2","perdant","C-38","micro","statut","complété",
 "input brouillon : environ 12 % des élus, sans entrée au référentiel","","D3-2-1-e1|gagnant|C-04",
 "Seule catégorie de l’input brouillon qui ne se dérivait pas de D2. Elle se "
 "dérive ici. Le chiffre reste non instruit."),
("D5-2-1-e2","perdant","C-30","micro","revenu","déduit",Q,"","D6-2-2|gagnant|C-30",
 "Agents des échelons supprimés, compris dans les 580 000 postes de D6-2-1."),
("D5-2-1-e2","perdant","C-37","méso","statut","nommé",Q,"",AUCUNE,""),
("D5-2-1-s1","perdant","C-31","micro","service","nommé","","","D9-2-1-e1|gagnant|C-02",
 "Dépenses culturelles et de loisir locales, hors investissements sportifs et "
 "socle social de 10 %."),
("D5-2-2-e1","gagnant","C-20","méso","service","nommé",Q,"D5-2-1-e2|perdant|C-37","",
 "Effet porté au signe négatif au référentiel alors que son énoncé est positif. "
 "Anomalie de signe."),
("D5-3-1-e1","gagnant","C-20","micro","liberté","nommé",Q,"D5-2-1-e2|perdant|C-37","",""),
("D5-3-2-e1","gagnant","C-20","micro","service","nommé",Q,"D5-2-1-e2|perdant|C-37","",""),
("D5-3-3-e1","gagnant","C-02","macro","service","nommé",Q,"D5-2-1-e2|perdant|C-37","",""),
("D5-3-4","gagnant","C-32","micro","service","déduit",Q,"D5-2-1-e2|perdant|C-37","",
 "Proposition sans effet au référentiel. La reprise par l’État garantit la "
 "continuité des solidarités départementales."),
# ============================================================ D6
("D6-2-1-e1","perdant","C-30","micro","revenu","nommé","","","D6-2-2|gagnant|C-30",
 "Effet au bénéficiaire « sphère publique » : grandeur écrite là où une personne "
 "est attendue."),
("D6-2-2","gagnant","C-30","micro","revenu","nommé",
 "70 % du traitement pendant 7 ans, cumul libre avec un emploi privé","D6-2-1-e1|perdant|C-30","",
 "La raccroche des agents. Alerte structurelle R10 sur D6-2-2-p2 : la durée de "
 "sept ans est une borne présentée comme valeur unique."),
("D6-2-2-e2","gagnant","C-01","macro","revenu","indiqué",
 "82 € par mois et par foyer","D6-2-1-e1|perdant|C-30","",
 "Opération : 29,6 Md€ / 30 M foyers / 12 = 82,22 €, forme canonique 82 €."),
("D6-2-2-e7","gagnant","C-30","micro","liberté","nommé",Q,"D6-2-1-e1|perdant|C-30","",""),
("D6-2-2-e4","gagnant","C-30","micro","statut","nommé",Q,"D6-2-1-e1|perdant|C-30","",""),
("D6-2-2-e3","gagnant","C-02","macro","service","nommé",Q,"D6-2-1-e1|perdant|C-30","",""),
("D6-2-2-e5","gagnant","C-01","macro","liberté","nommé",Q,"D6-2-1-e1|perdant|C-30","",""),
("D6-2-2-e6","gagnant","C-02","macro","service","nommé",Q,"D6-2-1-e1|perdant|C-30","",""),
("D6-3-1-e1","gagnant","C-05","micro","statut","nommé",Q,"D6-3-1|perdant|C-05","",""),
("D6-3-1-e2","gagnant","C-05","micro","liberté","nommé",Q,"D6-3-1|perdant|C-05","",""),
("D6-3-1","perdant","C-05","micro","statut","nommé",Q,"","D6-3-2-e2|gagnant|C-05",
 "Fin de l’emploi à vie. Perte nommée à l’input brouillon, absente du référentiel."),
("D6-3-2-e1","gagnant","C-05","micro","revenu","nommé",Q,"D6-3-1|perdant|C-05","",""),
("D6-3-2-e2","gagnant","C-05","micro","revenu","nommé",
 "+13 % de rémunération","D6-3-1|perdant|C-05","",
 "Grandeur reprise de D3-2-1-p1."),
("D6-ei2","gagnant","C-02","macro","service","nommé",Q,"D6-2-1-e1|perdant|C-30","",""),
# ============================================================ D7
("D7-2-1-e1","gagnant","C-03","micro","patrimoine","nommé","","D7-4-1|perdant|C-56","",""),
("D7-2-2-e1","gagnant","C-09","micro","patrimoine","nommé","","D7-4-1|perdant|C-56","",
 "Raccroche des retraités perdants de D3-2-1-e3 et D9-3-1-e7."),
("D7-2-2-e2","gagnant","C-02","macro","patrimoine","nommé","","D7-4-1|perdant|C-56","",""),
("D7-3-1-e1","gagnant","C-11","méso","patrimoine","nommé","","D7-3-1|perdant|C-40","",""),
("D7-3-1-e1","gagnant","C-12","micro","patrimoine","nommé","","D7-3-1|perdant|C-40","",""),
("D7-3-1","perdant","C-40","micro","statut","indiqué",
 "3,5 M de locataires HLM perdants à un an, d’après notre décompte, dont 33 % supplémentaires à trois ans","",
 "D9-2-1-e1|gagnant|C-02",
 "Socle de 15 % conservé, décote de liquidité de 15 %, priorité d’acquisition "
 "aux locataires, bail de trois ans au plus."),
("D7-3-1","capteur","C-54","méso","revenu","implicite",Q,"",AUCUNE,""),
("D7-ed3","capteur","C-59","méso","statut","nommé",Q,"",AUCUNE,""),
("D7-4-1-e1","gagnant","C-02","macro","statut","nommé",Q,"D7-4-1|perdant|C-56","",""),
("D7-4-1","perdant","C-56","méso","statut","déduit",Q,"",AUCUNE,
 "L’État actionnaire est un pouvoir de nomination autant qu’un portefeuille."),
# ============================================================ D8
("D8-2-1-e1","gagnant","C-09","macro","risque","nommé",Q,"D8-2-3|perdant|C-39","",""),
("D8-2-1-e2","gagnant","C-04","micro","patrimoine","nommé",Q,"D8-2-3|perdant|C-39","",""),
("D8-2-1-e3","gagnant","C-22","méso","patrimoine","nommé",Q,"D8-2-3|perdant|C-39","",""),
("D8-2-1-e4","gagnant","C-22","micro","patrimoine","nommé",Q,"D8-2-3|perdant|C-39","",""),
("D8-2-2-e1","gagnant","C-04","micro","liberté","nommé",Q,"D8-2-3|perdant|C-39","",""),
("D8-2-2-e2","gagnant","C-04","micro","liberté","nommé",Q,"D8-2-2|capteur|C-59","",""),
("D8-2-2-e3","gagnant","C-22","méso","patrimoine","nommé",Q,"D8-2-3|perdant|C-39","",""),
("D8-2-2-e4","gagnant","C-04","micro","risque","nommé",Q,"D8-2-3|perdant|C-39","",""),
# Écarté : « Il sera maître de son avenir » redit « Il gardera la maîtrise du
# fruit de son travail ». Les deux énoncés du manuscrit portent une seule
# position, et une ligne rédigée les tient ensemble.
# ("D8-2-2-e5","gagnant","C-04","micro","liberté","nommé",Q,"D8-2-3|perdant|C-39","",""),
("D8-2-2","capteur","C-59","méso","statut","déduit",Q,"",AUCUNE,
 "Régimes généraux et spéciaux, dont le nœud dit que l’assuré cessera de dépendre."),
("D8-2-3","perdant","C-39","micro","revenu","nommé",
 "transition de 25 ans ; pensions inférieures à 1 200 € intouchées","","D7-2-2-e1|gagnant|C-09",""),
("D8-3-1-e1","gagnant","C-10","micro","revenu","nommé",Q,"D8-3-1|perdant|C-41","",""),
("D8-3-1-e2","gagnant","C-04","macro","patrimoine","nommé","","D8-3-1|perdant|C-41","",""),
("D8-3-1","perdant","C-41","micro","revenu","indiqué",
 "3,3 M de personnes sans emploi de catégorie A perdantes à un an ; indemnisation "
 "ramenée de treize à six mois","","D8-3-1-e2|gagnant|C-04",
 "Le compte personnel prend le relais de l’indemnisation collective."),
("D8-4-1-e1","gagnant","C-13","micro","risque","nommé","","D8-4-1|perdant|C-13","",""),
("D8-4-1","perdant","C-13","micro","revenu","déduit",
 "reste à charge de 10 % par acte là où certains soins sont aujourd’hui pris en "
 "charge intégralement","","D8-4-1-e1|gagnant|C-13",
 "Ambivalence : le plafond de 5 % du revenu annuel est la raccroche interne."),
("D8-4-2-e1","gagnant","C-03","micro","revenu","nommé","","D8-4-2|capteur|C-58","",""),
("D8-4-2","capteur","C-58","méso","revenu","nommé",
 "jusqu’à 300 € par an et par foyer de frais de gestion","",AUCUNE,
 "Capteur nommé par la mesure elle-même, chiffré, et consensuel. Type même du "
 "capteur qui rend crédible l’aveu des perdants irritants."),
("D8-4-2-e2","gagnant","C-13","micro","service","nommé",Q,"D8-4-2|capteur|C-58","",""),
("D8-4-2-e3","gagnant","C-13","méso","service","nommé",Q,"D8-4-2|capteur|C-58","",""),
("D8-4-2-e4","gagnant","C-09","micro","patrimoine","nommé",Q,"D8-4-2|capteur|C-58","",""),
("D8-5-1-e1","gagnant","C-18","micro","revenu","nommé",Q,"D2-1-1|perdant|C-31","",""),
("D9-2-2-e1","gagnant","C-01","macro","revenu","indiqué","","D9-2-2|perdant|C-44","",
 "Nœud rattaché au levier D8-4 dans le référentiel alors que son identifiant "
 "relève de D9. Anomalie de rattachement."),
("D9-2-2","perdant","C-44","micro","risque","nommé",
 "périmètre conservé : pronostic vital et ordre public, environ 10 % des soins actuels","",AUCUNE,""),
# ============================================================ D9
("D9-2-1-e1","gagnant","C-02","micro","revenu","nommé",
 "aide fondamentale universelle de 550 € par mois, versée sans dossier","D2-4-1-s1|perdant|C-32","",
 "La raccroche universelle : tout perdant d’une aide ciblée est renvoyé ici."),
("D9-2-3-e1","gagnant","C-14","micro","revenu","nommé","","D9-2-3|perdant|C-14","",""),
("D9-2-3","perdant","C-14","micro","service","complété",Q,"","D9-2-3-e1|gagnant|C-14",
 "Articulation avec les prestations de compensation à trancher, selon "
 "l’atténuation portée au référentiel."),
("D9-3-1-e1","gagnant","C-04","micro","revenu","nommé","","D9-3-1-e7|perdant|C-39","",""),
("D9-3-1-e2","gagnant","C-04","micro","revenu","nommé",Q,"D9-3-1-e7|perdant|C-39","",""),
("D9-3-1-e4","gagnant","C-02","macro","statut","nommé",Q,"D9-3-1-e7|perdant|C-39","",""),
("D9-3-1-e5","gagnant","C-02","micro","liberté","nommé",Q,"D9-3-1-e7|perdant|C-39","",""),
("D9-3-1-e6","gagnant","C-06","micro","revenu","nommé",Q,"D9-3-1-e7|perdant|C-39","",""),
("D9-3-1-e7","perdant","C-39","micro","revenu","nommé","","","D7-2-2-e1|gagnant|C-09",
 "Alerte structurelle R14 : dépendance à D9-3-1-p1 sans chaîne."),
("D9-4-1-e1","gagnant","C-17","micro","revenu","nommé",
 "275 € par mois et par enfant, de zéro à dix-huit ans","D9-4-1|perdant|C-43","",""),
("D9-4-1","perdant","C-43","micro","revenu","nommé",Q,"","D9-4-2-e1|gagnant|C-43",
 "Parents seuls sans emploi dont les aides actuelles dépassent 275 € par enfant."),
("D9-4-1","perdant","C-03","micro","revenu","nommé",Q,"","D3-2-1-e1|gagnant|C-04",
 "Foyers aisés à plusieurs enfants tirant le meilleur parti du quotient familial."),
("D9-4-2-e1","gagnant","C-43","micro","revenu","nommé",
 "garantie de recouvrement là où 25 à 40 % des pensions restent impayées","D9-4-2-e2|perdant|C-47","",
 "Effet de signe neutre au référentiel : la même personne perd le supplément "
 "d’isolement et gagne la garantie."),
("D9-4-2-e2","gagnant","C-15","micro","revenu","nommé",Q,"D9-4-2-e2|perdant|C-47","",""),
("D9-4-2-e2","perdant","C-47","micro","revenu","nommé",Q,"",AUCUNE,
 "Perdant consensuel : le coparent qui n’acquitte pas la pension due."),
("D9-ei2","","","","","","","","",
 "Gain indirect de signe négatif dont l’énoncé est un diagnostic du système "
 "actuel. Classement à corriger."),
# ============================================================ D10
("D10-2-1-e1","gagnant","C-15","micro","service","nommé",
 "6 600 € par an et par enfant","D10-ed1|capteur|C-50","",
 "Grandeur reprise de D10-2-1-p1."),
("D10-3-1-e1","gagnant","C-19","micro","revenu","nommé",Q,"D10-ed1|capteur|C-50","",""),
("D10-3-1-e2","gagnant","C-19","micro","revenu","nommé",Q,"D10-ed1|capteur|C-50","",""),
("D10-3-1-e3","gagnant","C-19","micro","statut","nommé",Q,"D10-ed1|capteur|C-50","",""),
("D10-3-1-e4","gagnant","C-15","micro","service","nommé",Q,"D10-ed1|capteur|C-50","",""),
("D10-3-1-e6","gagnant","C-17","micro","liberté","nommé",Q,"D10-ed1|capteur|C-50","",""),
("D10-ed1","capteur","C-50","méso","statut","nommé",Q,"",AUCUNE,
 "La carte scolaire : rationnement administratif d’un bien, sans prix."),
("D10-4-1-e1","gagnant","C-04","micro","patrimoine","nommé",Q,"D10-4-1-e3|perdant|C-42","",""),
("D10-2-1-e1","gagnant","C-16","micro","patrimoine","nommé",
 "compte éducation versé et abondé à la majorité","D10-ed1|capteur|C-50","",
 "Le compte suit l'enfant pendant toute sa scolarité et lui est versé à ses "
 "dix-huit ans. Il s'emploie en une fois ou en différé, pour des études "
 "supérieures, une formation professionnelle ou un autre projet."),
("D10-4-2-e1","gagnant","C-16","micro","service","nommé",
 "prix réduits et bourses proposés par les universités","D10-4-2|perdant|C-08","",
 "Les bourses d'excellence et les prix réduits remplacent la gratuité "
 "apparente. Le manuscrit les nomme comme la contrepartie du compte éducation "
 "pour le jeune adulte."),
("D10-4-1-e6","gagnant","C-16","micro","revenu","nommé",Q,"D10-4-1-e3|perdant|C-42","",
 "Les jeunes travailleurs modestes cessent de financer les étudiants de familles aisées."),
("D10-4-1-e3","perdant","C-42","micro","service","nommé",Q,"","D10-2-1-e1|gagnant|C-15",
 "Le compte éducation, alimenté de 6 600 € par an, est la raccroche."),
("D10-4-2-e1","gagnant","C-08","méso","liberté","nommé",Q,"D10-4-2|perdant|C-08","",""),
("D10-4-2-e3","gagnant","C-16","micro","statut","nommé",Q,"D10-4-2|perdant|C-08","",""),
("D10-4-2","perdant","C-08","méso","revenu","déduit",Q,"","D10-4-2-e1|gagnant|C-08",
 "Fin du financement administré, cofinancement et mécénat à trouver."),
# ============================================================ D11
("D11-3-1-e1","gagnant","C-20","macro","statut","nommé",Q,"D2-1-1|perdant|C-31","",""),
("D11-3-1-e2","gagnant","C-20","macro","statut","nommé",Q,"D2-1-1|perdant|C-31","",""),
("D11-4-1-e1","gagnant","C-02","macro","statut","nommé",
 "trois mois de phase juridique puis trois mois de phase opérationnelle","D2-1-1|perdant|C-31","",""),
("D11-e1","gagnant","C-01","macro","revenu","indiqué","","D2-1-1|perdant|C-31","",
 "Effet au bénéficiaire « économie » : grandeur écrite là où une personne est "
 "attendue. Le taux passe de 42,87 % à 36,33 % du produit intérieur brut, soit "
 "191,046 Md€ de prélèvements en moins."),
("D11-4-2","gagnant","C-04","micro","revenu","nommé",
 "restitution par paliers de 2 % par mois jusqu’à 13 % de salaire net","D2-1-1|perdant|C-31","",""),
]

def main(sortie):
    from justifications import JUSTIFICATIONS as J
    from justifications import REDITES
    from apports import APPORTS as A
    from apports import MODALITES, ORDRE, ATTACHE
    cats=[dict(zip(("id","terme","definition","population","effectif","statut_ancre",
                    "source_ancre","variantes"),c)) for c in CATEGORIES]
    lignes=[]
    manquantes=[]
    # L'éventail se déplie ici : une ligne mère, autant de lignes filles que de
    # catégories atteintes. La fille reprend tout de la mère sauf sa catégorie.
    L_deplie=[]
    for t in L:
        L_deplie.append(t)
        cle=f"{t[0]}|{t[1]}|{t[2]}"
        for autre in EVENTAIL.get(cle,[]):
            if any(x[0]==t[0] and x[1]==t[1] and x[2]==autre for x in L):
                continue
            L_deplie.append((t[0],t[1],autre)+tuple(t[3:]))
    inconnues=[k for k in EVENTAIL
               if k not in {f"{t[0]}|{t[1]}|{t[2]}" for t in L}]
    for k in inconnues: print("  éventail sans ligne mère :",k)
    for t in L_deplie:
        anc,pos,cat,ech,nat,deg,gr,mir,rac,note=t
        cle=f"{anc}|{pos}|{cat}"
        # Troisième élément facultatif : le libellé court de la perte, cinq à
        # huit mots du point de vue de la personne. Les entrées à deux
        # éléments restent valides et n'en portent pas.
        _j=J.get(cle,("","","",""))
        just,rel=_j[0],_j[1]
        libelle=_j[2] if len(_j)>2 else ""
        vedette_perte=_j[3] if len(_j)>3 else ""

        # Le troisième élément, la vedette, est facultatif : un apport sans
        # quantité peut porter deux mots qui tiennent la même place qu'un
        # chiffre. Les entrées à deux éléments restent valides.
        _a=A.get(cle,("","",""))
        app,contre=_a[0],_a[1]
        vedette=_a[2] if len(_a)>2 else ""
        # RT-3 : une perte sans raccroche vers une ligne, mais dont le flux peut
        # se reconstituer volontairement, porte cette voie et non l'absence.
        if rac==AUCUNE and rel: rac=RECONST
        if pos in ("perdant","capteur") and not just:
            manquantes.append(cle)
        lignes.append({"ancrage":anc,"position":pos,"categorie":cat,"echelle":ech,
                       "nature":nat,"degre":deg,"grandeur_derivee":gr,
                       "miroir":mir,"raccroche":rac,"note":note,
                       "justification":just,"relais":rel,"vedette":vedette,
                       "libelle":libelle,"modalite":MODALITES.get(cle,""),
                       "redite":REDITES.get(cle,""),
                       "attache":ATTACHE.get(anc,""),
                       "rang_fiche":(ORDRE.get(cat,[]).index(anc)
                                     if anc in ORDRE.get(cat,[]) else 10**6),
                       "vedette_perte":vedette_perte,
                       "apport":app,"contrepartie":contre})
    orphelines=[k for k in J
                if k not in {f"{t[0]}|{t[1]}|{t[2]}" for t in L_deplie}]
    for k in manquantes: print("  justification manquante :",k)
    for k in orphelines: print("  justification orpheline :",k)
    cles={f"{t[0]}|{t[1]}|{t[2]}" for t in L_deplie}
    for k in A:
        if k not in cles: print("  apport orphelin :",k)
    sans=[c for c in cles if c.split("|")[1]=="gagnant" and c not in A]
    print(f"  {len(A)} gain(s) rédigé(s), {len(sans)} en régime transitoire")
    manuscrit=[{"id":k,"section":v[0],"notes":v[1],"libelle":v[2]}
               for k,v in ANCRAGES_MANUSCRIT.items()]
    json.dump({"_revision":{"objet":"positions dérivées, douze axes",
                            "base":"REF_doctrine_20260820_v20.json"},
               "groupes":[{"titre":g[0],"chapeau":g[1],"categories":g[2]}
                          for g in GROUPES],
               "promesses":PROMESSES,
               "categories":cats,"ancrages_manuscrit":manuscrit,"lignes":lignes},
              open(sortie,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print(f"{sortie} écrit — {len(cats)} catégories, {len(lignes)} lignes")

if __name__=="__main__":
    main(sys.argv[1])
