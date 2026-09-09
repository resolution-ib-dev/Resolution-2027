# -*- coding: utf-8 -*-
"""Sourcing du référentiel des faits — écrit à la main, une entrée à la fois.

`generer_ref_chiffres.py` relève mécaniquement tout ce que le corpus porte déjà :
la valeur, son unité, son millésime quand il est déclaré, son code d'origine, et
la source telle que le corpus l'énonce. Ce qu'il ne peut pas faire, c'est
trouver une source à un chiffre qui n'en a pas. C'est ici que ça s'écrit.

Le module est au référentiel des faits ce que `justifications.py` et `apports.py`
sont au référentiel des positions : la part rédigée à la main, hors du
générateur, qui survit à chaque régénération.

**Une entrée sans source reste sans source.** On ne comble pas un trou par une
source vraisemblable : on laisse le trou, il se voit au contrôle, et il se
travaille. Une source écrite ici doit être vérifiable au dehors — un document,
une page, une année, un tableau nommé — ou renvoyer à un artefact du corpus.

Clé : l'identifiant de l'entrée, tel que le générateur le forme.

    N-<note>-<rang>       un chiffre relevé dans une note de fin du manuscrit
    R-<noeud>-<rang>      un chiffre porté par le REF_doctrine
    P-<code>              un candidat du proto Données, à sourcer

Valeurs admises pour chaque clé, toutes facultatives :

    source        d'où vient le chiffre, en clair et vérifiable au dehors
    millesime     l'année de la donnée, quatre chiffres
    derivation    l'opération qui le produit, en clair
    unite         quand le relevé mécanique n'a pas su la lire
    valeur        quand le relevé mécanique n'a pas su la lire
    valeur_num    quand le relevé a pris la mauvaise valeur en tête — une année
                  dans « en 2024, X vaut Y », un numéro d'adresse web. L'entrée
                  porte alors `tete_redressee`.
    note          ce que la vérification a appris, y compris un doute

**`meme_que` est la seule façon de dire que deux entrées parlent du même
chiffre.** Un chiffre énoncé trois fois au corpus fait trois entrées, et c'est
normal : le référentiel sert à dire qu'elles concordent, non à les fusionner. Le
rapprochement se fait à la lecture, jamais par égalité de valeur — deux nombres
égaux ne parlent pas forcément de la même chose. Une fois écrit, le contrôle
vérifie l'accord et sort en anomalie toute discordance.
"""

# Modèle d'une entrée, à recopier :
#
#     'P-D-005': {
#         'source': "Rapport à la Commission des comptes de la sécurité "
#                   "sociale, septembre 2025, fiche recettes",
#         'millesime': '2024',
#         'note': "vérifié sur la fiche, valeur reprise à l'euro près",
#     },
#
# ## Lot du 20260825 — chômage, retraites, santé
#
# Le proto Données déclare ses sources par des lignes d'adresse posées **avant**
# les candidats qu'elles couvrent. Ce sont ces déclarations-là qui sont reprises
# ici, et rien d'autre : un candidat qu'aucune ligne d'adresse ne couvre reste
# sans source, quelle que soit la vraisemblance de sa provenance.
#
# Les blocs santé du proto — les dépenses et l'architecture cible — n'ont aucune
# source déclarée hors « Institut Santé » pour les ALD. **Ils restent tous à
# confiance nulle**, avec leur millésime, leur unité et leur arithmétique
# vérifiée. C'est exactement ce que le référentiel doit dire : le compte tombe,
# la source manque.
SOURCES = {
    # ---------------------------------------------------- chômage : les comptes
    'P-D-037': {
        'source': "Unédic, comptes 2024",
        'millesime': '2024',
        'unite': 'Md€',
        'valeur': '37,059 Md€',
        'valeur_num': 37.059,
        'derivation': "32,6 + 3,3 + 1,1 + 0,1 = 37,059 Md€",
        'note': "Le relevé prenait 32,6 en tête, qui est la première "
                "composante. La somme des quatre composantes arrondies fait "
                "37,1 ; l'énoncé porte 37 059 M€. Les trois calculs d'économie "
                "du proto emploient 37,1.",
    },
    'P-D-039': {
        'source': "Unédic, Chiffres clés — Les indicateurs de l'Assurance "
                  "chômage, mai 2025",
        'millesime': '2024',
        'unite': 'millions',
        'note': "3,8 M de personnes prises en charge au T4 2024, dont 2,7 M "
                "d'allocataires indemnisés. Stable sur un an.",
    },
    'P-D-040': {
        'source': "Unédic, Chiffres clés — Les indicateurs de l'Assurance "
                  "chômage, mai 2025",
        'millesime': '2024',
        'note': "1 046 € d'allocation mensuelle nette moyenne au T4 2024. "
                "Moyenne d'un ensemble hétérogène : 884 € pour ceux qui "
                "cumulent avec un revenu d'activité.",
    },
    # ------------------------------------------- chômage : les durées, Dares
    'P-D-041': {
        'source': "Dares, inscrits à France Travail, données trimestrielles",
        'millesime': '2023',
        'unite': 'jours',
        'note': "580 jours de durée potentielle d'indemnisation moyenne, soit "
                "19,1 mois. C'est le « droit à indemnisation » que le "
                "manuscrit chiffre à dix-neuf mois.",
    },
    'P-D-042': {
        'source': "Dares, inscrits à France Travail, données trimestrielles",
        'millesime': '2024',
        'unite': 'jours',
        'note': "307 jours de durée moyenne d'inscription des sortants au "
                "T4 2024. À ne pas confondre avec l'ancienneté moyenne des "
                "inscrits, qui est le double.",
    },
    'P-D-043': {
        'source': "Dares, inscrits à France Travail, données trimestrielles",
        'millesime': '2024',
        'unite': 'jours',
        'note': "619 jours d'ancienneté moyenne des inscrits au T4 2024, soit "
                "20,3 mois. C'est le chiffre que le manuscrit arrondit à vingt "
                "mois pour le comparer aux dix-neuf mois de droit.",
    },
    'P-D-044': {
        'source': "Dares, inscrits à France Travail, données trimestrielles",
        'millesime': '2024',
        'unite': '%',
        'valeur': '43,3 %',
        'valeur_num': 43.3,
        'note': "43,3 % des 5,21 millions d'inscrits le sont depuis un an ou "
                "plus. Le relevé prenait « 1 an » pour valeur de tête.",
    },
    'P-D-045': {
        'source': "Dares, inscrits à France Travail, données trimestrielles",
        'millesime': '2024',
        'unite': '%',
        'valeur': '37 %',
        'valeur_num': 37.0,
        'note': "37 % des inscrits le sont depuis moins de six mois. Le proto "
                "en tire 1,94 M ; 37 % × 5,21 M donne 1,93 M. Écart d'arrondi "
                "de dix mille personnes. C'est ce taux de 37 % qui commande "
                "les trois calculs d'économie.",
    },
    # ------------------------------- chômage : le tableau des allocations, Dares
    'P-D-047': {
        'source': "Dares, tableau « Allocations d'assurance-chômage », "
                  "décembre 2022 et décembre 2023",
        'millesime': '2023',
        'unite': '€',
        'note': "Salaire journalier de référence : 70 € en décembre 2022, "
                "71 € en décembre 2023.",
    },
    'P-D-048': {
        'source': "Dares, tableau « Allocations d'assurance-chômage », "
                  "décembre 2022 et décembre 2023",
        'millesime': '2023',
        'unite': '€',
        'note': "Allocation journalière brute : 41 € puis 42 €.",
    },
    'P-D-049': {
        'source': "Dares, tableau « Allocations d'assurance-chômage », "
                  "décembre 2022 et décembre 2023",
        'millesime': '2023',
        'unite': '%',
        'note': "**Ne jamais présenter les 64 % comme le rapport des deux "
                "lignes affichées** : 42 / 71 fait 59,2 %. Le taux de "
                "remplacement est calculé allocataire par allocataire, la "
                "moyenne des rapports n'étant pas le rapport des moyennes. "
                "Citer les trois ensemble expose à une division vérifiable qui "
                "ne tombe pas.",
    },
    'P-D-051': {
        'source': "Dares, tableau « Allocations d'assurance-chômage », "
                  "décembre 2022 et décembre 2023",
        'millesime': '2023',
        'unite': '€',
        'note': "1 130 € puis 1 150 € d'allocation mensuelle brute. Même "
                "réserve que pour le taux de remplacement : 42 € × 28 jours "
                "font 1 176 € et non 1 150 €. C'est la valeur de 1 150 qui "
                "sert d'assiette aux calculs d'économie du proto.",
    },
    'P-D-054': {
        'source': "Dares, tableau « Allocations d'assurance-chômage », "
                  "décembre 2022 et décembre 2023",
        'millesime': '2023',
        'unite': '€',
        'valeur': '1 060 €',
        'valeur_num': 1060.0,
        'note': "Allocation mensuelle brute médiane, décembre 2023 : 1 060 €. "
                "Le relevé prenait « Médiane » pour un nombre. Décile 1 à "
                "445 €, décile 9 à 1 855 €, centile 99 à 4 140 € : montants "
                "arrondis au multiple de cinq le plus proche.",
    },
    # ------------------------------------------ chômage : l'hypothèse et ses trois suites
    'P-D-059': {
        'unite': 'mois',
        'valeur': '6 mois',
        'derivation': "600 € de cible sur 1 150 € d'allocation moyenne brute "
                      "= 52,2 %, arrondi à 52 %",
        'note': "Six mois d'indemnisation maximale, qui couvrent 37 % des "
                "inscrits. L'allocation moyenne brute de 1 150 € moins 550 € "
                "de crédit d'impôt social unique laisse 600 € en cible. Le "
                "proto écrit « 6M », que le relevé lit comme une unité de "
                "millions.",
    },
    'P-D-060': {
        'unite': 'Md€',
        'valeur': '30,0 Md€',
        'valeur_num': 30.0,
        'derivation': "37,1 × ((1 − 37 %) + 37 % × (1 − 52 %)) = 29,96",
        'note': "Économie brute sur les allocations. Le relevé prenait 37,1 en "
                "tête, qui est l'assiette et non le résultat. Vérifié : 29,96. "
                "C'est la valeur de la ligne 27 du tableau de référence du "
                "classeur, « Assurance chômage transformée en épargne », 30 Md€.",
    },
    'P-D-061': {
        'unite': 'Md€',
        'valeur': '17,8 Md€',
        'valeur_num': 17.8,
        'derivation': "37,1 × (1 − 52 %) = 17,81",
        'note': "Part reprise par le crédit d'impôt social. Vérifié.",
    },
    'P-D-062': {
        'unite': 'Md€',
        'valeur': '12,2 Md€',
        'valeur_num': 12.2,
        'derivation': "37,1 × (1 − 37 %) × 52 % = 12,15",
        'note': "Économie nette du crédit d'impôt social. Vérifié. La "
                "décomposition 17,8 + 12,2 = 30,0 est exacte par construction "
                "et non par coïncidence : (1−x) + x(1−y) et (1−y) + (1−x)y "
                "sont la même expression.",
    },
    # ----------------------------------------------------------- retraites
    'P-D-064': {
        'source': "Conseil d'orientation des retraites, rapport annuel, "
                  "juin 2025 ; Rapport sur les pensions de retraite de la "
                  "fonction publique annexé au PLF 2026",
        'millesime': '2024',
        'unite': 'Md€',
        'valeur': '282,4 Md€',
        'valeur_num': 282.4,
        'derivation': "269,3 − 6,9 (opérateurs) + 11 (part « normale » du CAS) "
                      "+ 9 (forfaits de cotisation) = 282,4",
        'note': "Vérifié à l'exact. Concorde avec les 282 milliards de la note "
                "de fin e74 du manuscrit, qui est la strate 1 : les deux "
                "sources s'accordent sur les ressources du système.",
    },
    'P-D-065': {
        'source': "Conseil d'orientation des retraites, rapport annuel, "
                  "juin 2025",
        'millesime': '2024',
        'unite': 'Md€',
        'note': "388 Md€ dont 39 de droit dérivé. **Périmètre écarté par "
                "l'auteur le 20260825** au profit des 407 Md€ de la note e74, "
                "qui ajoutent les charges de gestion et l'action sociale. "
                "L'écart de périmètre est de 19 Md€.",
    },
    'P-D-066': {
        'millesime': '2024',
        'unite': '%',
        'derivation': "282,4 / 388 = 72,8 %",
        'note': "Taux de couverture au périmètre du proto. **Ne se publie "
                "pas** : au périmètre du manuscrit, 282 / 407 fait 69,3 %.",
    },
    'P-D-067': {
        'millesime': '2024',
        'unite': 'Md€',
        'derivation': "388 − 282,4 = 105,6",
        'note': "Déficit implicite au périmètre du proto. **Ne se publie "
                "pas** : le corps du manuscrit porte 125 Md€ de déficit "
                "spontané, soit 407 − 282, « les deux-tiers du déficit "
                "public ». C'est cette valeur qui sort.",
    },
    # ------------------------------------------------- santé : les dépenses 2024
    'P-D-069': {
        'millesime': '2024',
        'unite': 'Md€/an',
        'derivation': "253 / 68 M habitants = 3 723 €/an/hab",
        'note': "Dépenses médicales totales, dont 121 Md€ d'hôpital. Le "
                "millésime vient du titre du bloc, « SANTE (2024) ». Somme "
                "vérifiée : public 200,5 + mutuelles 32,5 + reste à charge 20 "
                "= 253. Aucune source déclarée.",
    },
    'P-D-070': {
        'millesime': '2024',
        'unite': 'Md€/an',
        'derivation': "200,5 / 68 M habitants = 2 956 €/an/hab",
        'note': "Part publique des dépenses médicales, dont 112 Md€ d'hôpital "
                "sur les 121. Aucune source déclarée.",
    },
    'P-D-071': {
        'source': "Institut Santé",
        'millesime': '2024',
        'unite': 'Md€',
        'note': "134 Md€ d'affections de longue durée, soit plus de la moitié "
                "des 253 Md€ de dépenses médicales. Seule ligne du bloc santé "
                "qui déclare une source.",
    },
    'P-D-072': {'millesime': '2024', 'unite': 'Md€/an',
                'derivation': "32,5 / 68 M habitants = 479 €/an/hab",
                'note': "Part des mutuelles dans les dépenses médicales."},
    'P-D-073': {'millesime': '2024', 'unite': 'Md€/an',
                'derivation': "20 / 68 M habitants = 292 €/an/hab",
                'note': "Reste à charge médical des ménages."},
    'P-D-074': {
        'millesime': '2024', 'unite': 'Md€/an',
        'note': "Soins de longue durée hors médical. Deux décompositions "
                "vérifiées : par objet, handicap 15,3 + autonomie 35,9 + "
                "addictions 1 = 52,2 ; par financeur, public 38,3 + ménages 14 "
                "= 52,3, soit un dixième d'écart d'arrondi.",
    },
    'P-D-077': {'millesime': '2024', 'unite': 'Md€/an',
                'note': "Prévention : 8,7 Md€/an dont 6,1 publics."},
    'P-D-078': {
        'millesime': '2024', 'unite': 'Md€/an',
        'derivation': "sécurité sociale 7 + État 1,2 + mutuelles 8,7 = 16,9",
        'note': "Frais de gestion. Somme vérifiée. La note de fin e129 du "
                "manuscrit porte la même grandeur à 16,9 milliards : la strate "
                "1 source ce candidat.",
    },
    'P-D-080': {'millesime': '2024', 'unite': 'Md€/an',
                'note': "Accidents du travail et maladies professionnelles, "
                        "dépenses publiques."},
    'P-D-081': {
        'millesime': '2024', 'unite': 'Md€',
        'note': "**La recomposition ne tombe pas.** Public médical 200,5 + "
                "longue durée publique 38,3 + prévention publique 6,1 font "
                "244,9, et non 242 : 2,9 Md€ ne s'expliquent pas par les "
                "postes du proto. Le total de 242 est pourtant celui que toute "
                "l'architecture cible emploie. À documenter avant tout emploi.",
    },
    # ------------------------------------------------ santé : l'architecture cible
    'P-D-088': {
        'millesime': '2024', 'unite': 'Md€',
        'derivation': "cotisations 304,2 + 6,9 + CAS PFE équivalent privé 11 "
                      "+ contributions et taxes sociales 21 + CSG hors "
                      "activité 14 + remises conventionnelles 10,5 = 367,6",
        'note': "Recettes sociales socle. Somme vérifiée à 367,6, arrondie à "
                "368. Aucune source déclarée pour les composantes.",
    },
    'P-D-091': {
        'unite': 'Md€',
        'note': "Socle santé cible de 142 Md€, fourchette 120 à 170. "
                "Paramètre de conception, non un relevé.",
    },
    'P-D-092': {
        'unite': 'Md€',
        'valeur': '100 Md€',
        'note': "Dépenses à flécher sur le compte santé, fourchette 70 à 120. "
                "Le proto déclare l'unité « pt », qui est fausse : l'énoncé "
                "porte des Md€. Vérifié : 142 + 100 = 242, l'architecture "
                "cible épuise exactement le total à répartir.",
    },
    'P-D-093': {
        'unite': 'Md€',
        'derivation': "100 de dépenses fléchées + 41 de mutuelles = 141",
        'note': "Compte santé de 141 Md€. Les 41 Md€ de mutuelles concordent "
                "avec les postes du bloc dépenses : 32,5 médical + 8,7 de "
                "frais de gestion font 41,2.",
    },
    'P-D-097': {
        'unite': 'Md€',
        'valeur': '368 Md€',
        'valeur_num': 368.0,
        'derivation': "compte santé personnel 100 + retraite à flécher 122 "
                      "+ retraite socle 146 = 368",
        'note': "Réemploi des 368 Md€ de recettes sociales socle, redécoupés "
                "entre santé et retraite. Somme vérifiée. Les trois parts sont "
                "données comme approximatives et suivies d'un point "
                "d'interrogation au proto : ce sont des hypothèses de travail.",
    },
    # ================================================================ lot du classeur
    # Le classeur « Synthèse Calculs Résolution 0819 » déclare ses sources à
    # l'onglet Gages, colonne J, poste par poste. Ce sont des documents publics,
    # nommés, datés : ils sont donc reprenables tels quels. Un poste dont l'onglet
    # ne dit rien reste sans source.
    'R-D2-4-1-s1': {
        'source': "classeur Synthèse Calculs Résolution 0819, onglet Détail "
                  "Economies, ligne 18 ; PLF 2026, données des projets annuels "
                  "de performance",
        'millesime': '2026',
        'note': "Le classeur porte 16,1 Md€ d'APL sur un total supprimé, dont "
                "5,4 restitués en CSG et 10,7 de solde. Le sous-item arrondit à "
                "16. **Le détail des 17,7 Md€ de chèques ciblés est complet** : "
                "APL 16,1 + chèque énergie 0,6 + autres 1,0 = 17,7. Le poste "
                "« Chèques aux ménages » du détail vaut 19,9 ; les 2,2 Md€ "
                "d'écart sont l'aide médicale d'État et les exonérations "
                "d'emploi à domicile, que le tableau de référence classe "
                "ailleurs — l'une aux aides inconditionnelles, l'autre aux "
                "aides à l'emploi.",
    },
    'R-D2-4-1-e2': {
        'source': "classeur Synthèse Calculs Résolution 0819, onglet Détail "
                  "Economies ; PLF 2026, Voies et moyens Tomes 1 et 2 et "
                  "données des projets annuels de performance ; Insee, comptes "
                  "de la nation 2023, données COFOG",
        'millesime': '2026',
        'note': "Les quatre postes de la chaîne se recomposent tous depuis le "
                "détail : chèques ciblés 17,7, hébergement et AME 3,6, "
                "associations 3,2, aide publique au développement 3,0. Les "
                "22,5 Md€ d'emploi-insertion sont France Compétences 10,6 + "
                "France Travail 2,7 + aides emploi-apprentissage 6,9 + aide "
                "emploi-insertion 2,3. Vérifié au contrôle F8.",
    },
    'R-D2-4-1-s7': {
        'source': "classeur Synthèse Calculs Résolution 0819, onglet Détail "
                  "Economies, ligne 19 ; PLF 2026, données des projets annuels "
                  "de performance",
        'millesime': '2026',
        'note': "1,1 Md€ d'aide médicale d'État, hors les 10 % conservés pour "
                "les soins urgents. Le classeur l'écrit dans les chèques aux "
                "ménages ; le tableau de référence la classe avec l'hébergement "
                "d'urgence, d'où les 3,6 Md€ d'aides inconditionnelles.",
    },
    'R-D3-2-1-p4': {
        'source': "PLACSS 2024, Annexe 1 — cité à l'onglet Gages du classeur "
                  "Synthèse Calculs Résolution 0819",
        'millesime': '2024',
        'note': "114,46 Md€ de CSG et CRDS d'activité, dont 108,56 de CSG "
                "activité. Le proto porte les deux, sans les sourcer.",
    },
    'R-D2-1-1-e1': {
        'source': "classeur Synthèse Calculs Résolution 0819, onglet Manifeste, "
                  "ligne 3 pour les dépenses et ligne 24 pour les niches",
        'millesime': '2026',
        'note': "183,95 Md€ de baisses de dépenses et 52,1 Md€ de niches "
                "restituées font 236,05. Le gain d'année 1 est de 75,25 Md€, "
                "le reste venant en année pleine.",
    },
    'R-D8-3-1-e2': {
        'source': "classeur Synthèse Calculs Résolution 0819, onglet Manifeste, "
                  "ligne 20, « Économies sur l'assurance chômage » ; onglet "
                  "Capitalisation, « Transformation assurance chômage (base de "
                  "dépenses = 37,1 Md€) »",
        'millesime': '2024',
        'derivation': "37,1 × ((1 − 37 %) + 37 % × (1 − 52 %)) = 29,96, arrondi "
                      "à 30",
        'note': "**Qualification tranchée par l'auteur le 20260825 : les 30 Md€ "
                "sont une économie, et ils sont dans les 236.** Le classeur les "
                "porte deux fois comme telle — à la ligne 20 des baisses de "
                "dépenses de l'onglet Manifeste, et à l'onglet Capitalisation "
                "où la base est explicitement une base de **dépenses** de "
                "37,1 Md€. L'esprit du calcul est au proto : c'est l'allocation "
                "qui s'éteint au-delà de six mois, pas la cotisation qui change "
                "de destination.",
    },
    'R-D7-2-2-e2': {
        'source': "classeur Synthèse Calculs Résolution 0819, onglet "
                  "Capitalisation, lignes 2 à 7",
        'millesime': '2024',
        'derivation': "636,1 Md€ d'actifs × 2,9 % = 18,4469 Md€/an",
        'note': "Les 636,1 Md€ se décomposent en participations financières "
                "208,28, patrimoine foncier public 200,20, logements publics "
                "57,73 et parc social 169,89. **Le classeur applique 2,9 % de "
                "rendement là où la doctrine annonce 3 %.** Et les 20 000 € par "
                "foyer supposent 600 Md€ répartis sur 30 M de foyers, quand le "
                "classeur en valorise 636,1 : la promesse est prudente de "
                "36 Md€.",
    },
    'N-e118-1': {
        'note': "Le classeur donne 341,44 Md€ d'actif net du parc social — "
                "actif brut 513,34 moins 171,9 d'encours de dette — que la note "
                "arrondit à 340 milliards. Les 4,8 millions de logements "
                "concordent, à 106,9 k€ de valeur moyenne par logement.",
    },
    # ------------------------------------------ une unité fausse, à ne pas propager
    'P-D-020': {
        'unite': 'M€',
        'valeur': '14 261 M€',
        'note': "**Le proto déclare « 14 261 Md€ », qui est faux d'un facteur "
                "mille** : ce sont des M€, soit 14,3 Md€. Deux de ses "
                "composantes le montrent, dépenses de fonctionnement de la "
                "CNAF 3 132 M€ et de la branche maladie 7 391 M€. Corrigé ici, "
                "et non au proto, qui est une archive.",
    },
}


def sourcer(identifiant):
    """Ce que la main a écrit pour cette entrée, ou rien."""
    return SOURCES.get(identifiant, {})


def compte():
    return len(SOURCES)


# --------------------------------------------------------------- les mêmes faits
# A-35 : un chiffre énoncé trois fois au corpus fait trois entrées. Le
# référentiel sert à dire qu'elles **concordent**, non à les fusionner. Le
# rapprochement ne se devine pas — deux nombres égaux ne parlent pas forcément du
# même fait, et deux énoncés du même fait ne portent pas forcément le même nombre,
# ce qui est précisément ce qu'on cherche.
#
# Un groupe = un fait, et les entrées qui le portent. **La première est la
# référence** : c'est à elle que le contrôle compare les autres, et elle se choisit
# par confiance décroissante — une note du manuscrit avant un nœud du
# `REF_doctrine`, un nœud avant un candidat du proto.
#
# Le champ `motif` dit pourquoi ces entrées portent le même fait. Il se lit avant
# de conclure quoi que ce soit d'une discordance : c'est lui qui distingue un
# désaccord du corpus d'un périmètre qui n'est pas le même.
#
# Le champ `tolerance` est facultatif et **s'écrit toujours avec sa raison dans le
# motif** : il dit qu'un écart n'est pas un désaccord mais un arrondi de la même
# opération. Il s'exprime dans l'unité de la référence. Une tolérance qui servirait
# à faire taire un écart réel serait la faute que tout ce dispositif cherche à
# empêcher.
#
# Le champ `arbitrage` est facultatif. Une discordance réelle ne disparaît pas
# parce qu'on a choisi : elle reste au corpus, et le proto qui la porte est une
# archive qui ne se réécrit pas. **L'arbitrage dit laquelle des deux valeurs sort
# et qui l'a décidé.** Le contrôle cesse alors de compter la discordance en échec
# et la range en décision, toujours visible. Un arbitrage sans `retenu` valide
# n'est pas un arbitrage.
#
# Ce bloc vit ici et non dans `SOURCES` : rapprocher n'est pas sourcer. Une entrée
# rapprochée reste sans source tant que personne ne lui en a écrit une.
MEME_QUE = [
    # --- ce que gagne un travailleur ---------------------------------------
    {
        'fait': "salaire médian net mensuel, 2024",
        'entrees': ['N-e4-1', 'N-e99-2', 'P-D-012'],
        'motif': "Les trois énoncent le net médian mensuel de 2024. C'est le "
                 "chiffre que la stratégie réseaux a relevé comme divergent "
                 "entre deux documents.",
    },
    {
        'fait': "assiette de la CSG rapportée au salaire brut",
        'entrees': ['R-D3-2-1-p6', 'P-D-006'],
        'motif': "98,25 % — un abattement de 1,75 % pour frais professionnels. "
                 "Le paramètre affichait 98 % alors que son propre `exact` et "
                 "l'onglet CSG du classeur portent 98,25 : un point de CSG au "
                 "SMIC brut y vaut 1 801,80 × 98,25 % × 1 % = 17,702685 €. "
                 "Arbitrage de l'auteur du 20260825 : on prend l'exact. Corrigé "
                 "au REF_doctrine.",
    },
    {
        'fait': "effet inflationniste subi par un consommateur adulte, à un an",
        'entrees': ['R-D3-2-1-e4', 'P-D-100'],
        'motif': "L'effet du plan sur les prix, ramené à la personne et à "
                 "l'année. Le REF le porte en négatif du point de vue du "
                 "gagnant, le proto en positif du point de vue du perdant.",
    },
    # --- retraites -----------------------------------------------------------
    {
        'fait': "dépenses annuelles de pensions de retraite, 2024",
        'entrees': ['N-e74-1', 'P-D-065'],
        'arbitrage': {
            'retenu': 'N-e74-1',
            'par': 'auteur',
            'date': '20260825',
            'motif': "On prend les chiffres du manuscrit. Le corps du livre "
                     "porte les 125 Md€ de déficit spontané, qui sont "
                     "407 − 282 : le périmètre large est celui du livre.",
        },
        'motif': "La note compte 407 Md€, droits dérivés, charges de gestion et "
                 "action sociale inclus ; le proto compte 388 Md€ dont 39 de "
                 "droit dérivé. Les deux s'accordent sur les ressources — 282 "
                 "et 282,4 Md€ — et divergent de 19 Md€ sur la dépense, qui "
                 "sont la gestion et l'action sociale. **Le manuscrit tranche** : "
                 "son corps porte un déficit spontané de 125 Md€, soit "
                 "407 − 282, et non les 106 Md€ du proto. Le périmètre du proto "
                 "est abandonné.",
    },
    {
        'fait': "baisse nette des retraites au-delà de 1 600 € par mois",
        'entrees': ['N-e123-2', 'R-D9-3-1-e7'],
        'motif': "Même seuil, même baisse. La note porte le seuil en tête et "
                 "la baisse en déclinaison ; le REF fait l'inverse.",
    },
    # --- patrimoine restitué -------------------------------------------------
    {
        'fait': "rendement annuel par personne du patrimoine restitué",
        'entrees': ['R-D7-2-2-e2', 'R-lexique-capital-de-restitution-i1'],
        'tolerance': 1.0,
        'motif': "Une seule opération : 8 823,53 € par personne à 3 % de "
                 "rendement net font 264,71 €/an, que la promesse arrondit à "
                 "265. Ni l'un ni l'autre n'est au manuscrit. Tolérance d'un "
                 "euro, qui est l'arrondi de la promesse et rien d'autre.",
    },
    {
        'fait': "hypothèse de rendement net du patrimoine restitué",
        'entrees': ['N-e119-1', 'R-D7-2-2-p1'],
        'motif': "3 % de rendement net sur 24 ans de retraite, posé à la note "
                 "et repris au paramètre.",
    },
    {
        'fait': "durée maximale du bail dans le parc social cédé",
        'entrees': ['N-e118-4', 'R-D7-3-1-p3'],
        'motif': "Trois ans, alignés sur le cadre privé.",
    },
    {
        'fait': "socle conservé et décote de liquidité à la cession du parc social",
        'entrees': ['N-e118-2', 'R-D7-3-1-p1'],
        'motif': "15 % et 15 %, hypothèse prudente de la valorisation.",
    },
    # --- niches et taxes -----------------------------------------------------
    {
        'fait': "niches supprimées, cible",
        'entrees': ['R-D2-5-1-p1', 'R-D2-5-1-e2'],
        'motif': "Le paramètre et l'effet de la même proposition portent la "
                 "même cible de 143 Md€.",
    },
    {
        'fait': "part des niches restituée directement aux travailleurs",
        'entrees': ['N-e97-3', 'R-D2-5-1-p2'],
        'motif': "52 milliards restitués, à la note comme au paramètre.",
    },
    {
        'fait': "secteurs sensibles écartés de la restitution immédiate",
        'entrees': ['N-e97-2', 'R-D2-5-1-p5'],
        'motif': "Le champ de 30 Md€ que la note pose et que le paramètre "
                 "reprend sans énoncé propre.",
    },
    {
        'fait': "taxes spécifiques supprimées, charge annuelle",
        'entrees': ['N-e107-1', 'R-D4-3-2-e1'],
        'motif': "16 milliards par an, à la note comme à l'effet.",
    },
    {
        'fait': "franchise d'impôt à la transmission",
        'entrees': ['N-e108-1', 'R-D4-4-2-p1', 'R-D4-4-2-e1'],
        'motif': "Une franchise de l'ordre de 3 %, avance sur la taxation de "
                 "la plus-value.",
    },
    # --- santé et solidarité -------------------------------------------------
    {
        'fait': "frais de gestion cumulés de la santé, par an",
        'entrees': ['N-e129-1', 'P-D-078'],
        'motif': "16,9 milliards, mutuelles et administrations cumulées. La "
                 "note source le candidat du proto, qui n'a pas de source "
                 "propre.",
    },
    {
        'fait': "part des soins urgents dans l'aide médicale d'État",
        'entrees': ['N-e125-1', 'R-D9-2-2-p2'],
        'motif': "Environ 10 %, d'après les données disponibles.",
    },
    {
        'fait': "dépense annuelle d'aide médicale d'État",
        'entrees': ['R-D9-2-2-e1', 'R-D2-4-1-s7'],
        'motif': "1,1 Md€, portés une fois comme économie de la proposition "
                 "santé et une fois comme sous-item des aides supprimées.",
    },
    {
        'fait': "reste à charge par acte",
        'entrees': ['R-D8-4-1-p1', 'R-D8-4-1-e1'],
        'motif': "10 % par acte, plafond de 5 % du revenu annuel.",
    },
    {
        'fait': "total perçu au titre de l'aide fondamentale, cas du handicap",
        'entrees': ['R-D9-2-3-p2', 'R-D9-2-3-e1'],
        'motif': "1 100 €/mois, aide fondamentale et part supplémentaire "
                 "cumulées. À ne pas confondre avec la pension de base par "
                 "répartition, qui vaut le même montant sans être le même fait.",
    },
    {
        'fait': "impayés de pension alimentaire dans le système actuel",
        'entrees': ['N-e78-1', 'R-D9-4-2-p2'],
        'motif': "25 à 40 % des parents créanciers, fourchette des estimations "
                 "citées.",
    },
    # --- chômage -------------------------------------------------------------
    {
        'fait': "durée d'indemnisation collective du chômage",
        'entrees': ['R-D8-3-1-p1', 'P-D-059'],
        'motif': "Six mois. Le proto l'écrit « 6M », que le relevé lit comme "
                 "une unité de millions.",
    },
    {
        'fait': "assurance chômage transformée en épargne, par an",
        'entrees': ['R-D8-3-1-e2', 'P-D-060'],
        'motif': "30 Md€, ligne 27 du tableau de référence du classeur, "
                 "intitulée « Assurance chômage transformée en épargne ». Le "
                 "proto l'obtient par calcul sur les allocations : 37,1 Md€ × "
                 "((1 − 37 %) + 37 % × (1 − 52 %)) = 29,96. La coïncidence à "
                 "quatre centièmes près désigne la même grandeur. **Le "
                 "`REF_doctrine` l'intitule « cotisations », ce que ni le "
                 "classeur ni le proto ne disent** : à trancher par l'auteur, "
                 "voir le fil courant.",
    },
    # --- travail -------------------------------------------------------------
    {
        'fait': "hausse des salaires nets à l'horizon d'un an",
        'entrees': ['R-D3-2-1-p1', 'R-D3-2-1-e1', 'R-lexique-restitution-b1'],
        'motif': "+13 %, portés par le paramètre, l'effet et le lexique.",
    },
    {
        'fait': "capital transféré par foyer",
        'entrees': ['R-D7-2-1-p1', 'R-D7-2-1-e1'],
        'motif': "20 000 € en trois ans.",
    },
    {
        'fait': "postes publics facultatifs supprimés",
        'entrees': ['R-D6-2-1-p1', 'R-D6-2-1-e1'],
        'motif': "580 000 postes, soit −10 % des effectifs totaux. Le "
                 "paramètre porte le nombre, l'effet porte le taux.",
    },
]


# ------------------------------------------------------------------ les calculs
# **Une dérivation écrite en prose ne prouve rien.** Le corpus porte des dizaines
# d'opérations — « 32,6 + 3,3 + 1,1 + 0,1 = 37 059 M€ », « 37,1 × ((1 − 37 %) +
# 37 % (1 − 52 %)) = 30,0 » — et rien ne les rejouait. Elles sont ici sous une
# forme que la machine évalue, avec le résultat attendu et la tolérance admise.
#
# Un calcul dit ce qu'il vérifie, pas d'où viennent ses termes : les termes se
# sourcent aux entrées, l'opération se vérifie ici. Le champ `id` est facultatif —
# une recomposition d'un tableau du classeur ne vise aucune entrée en particulier
# et se vérifie quand même.
#
# La tolérance est l'arrondi admis, dans l'unité du résultat. Elle se déclare,
# elle ne se découvre pas après coup en la remontant jusqu'à ce que le compte
# tombe.
CALCULS = [
    # ---------------------------------------------- chômage : la chaîne du proto
    {'id': 'P-D-037', 'unite': 'Md€', 'tolerance': 0.05,
     'objet': "allocations d'assurance chômage, somme des quatre composantes",
     'expression': '32.6 + 3.3 + 1.1 + 0.1', 'attendu': 37.059},
    {'id': 'P-D-045', 'unite': 'millions', 'tolerance': 0.02,
     'objet': "inscrits depuis moins de six mois, 37 % de 5,21 M",
     'expression': '0.37 * 5.21', 'attendu': 1.94},
    {'id': 'P-D-059', 'unite': '%', 'tolerance': 0.25,
     'objet': "allocation cible rapportée à l'allocation moyenne brute",
     'expression': '600 / 1150 * 100', 'attendu': 52},
    {'id': 'P-D-060', 'unite': 'Md€', 'tolerance': 0.05,
     'objet': "économie brute sur les allocations chômage",
     'expression': '37.1 * ((1 - 0.37) + 0.37 * (1 - 0.52))', 'attendu': 30.0},
    {'id': 'P-D-061', 'unite': 'Md€', 'tolerance': 0.05,
     'objet': "part reprise par le crédit d'impôt social",
     'expression': '37.1 * (1 - 0.52)', 'attendu': 17.8},
    {'id': 'P-D-062', 'unite': 'Md€', 'tolerance': 0.05,
     'objet': "économie nette du crédit d'impôt social",
     'expression': '37.1 * (1 - 0.37) * 0.52', 'attendu': 12.2},
    {'unite': 'Md€', 'tolerance': 0.01,
     'objet': "la décomposition de l'économie brute est exacte par construction",
     'expression': '17.8 + 12.2', 'attendu': 30.0},
    {'unite': 'mois', 'tolerance': 0.4,
     'objet': "ancienneté moyenne des inscrits, 619 jours en mois — les vingt "
              "mois du manuscrit",
     'expression': '619 / 30.44', 'attendu': 20},
    {'unite': 'mois', 'tolerance': 0.1,
     'objet': "durée potentielle d'indemnisation, 580 jours en mois — les "
              "dix-neuf mois du manuscrit",
     'expression': '580 / 30.44', 'attendu': 19},
    # ------------------------------------------------------------- retraites
    {'id': 'P-D-064', 'unite': 'Md€', 'tolerance': 0.01,
     'objet': "cotisations totales de retraite, recomposition du proto",
     'expression': '269.3 - 6.9 + 11 + 9', 'attendu': 282.4},
    {'unite': 'Md€', 'tolerance': 0.01,
     'objet': "déficit spontané des retraites au périmètre du manuscrit, "
              "407 − 282 — le chiffre du corps du livre",
     'expression': '407 - 282', 'attendu': 125},
    {'unite': '%', 'tolerance': 0.1,
     'objet': "taux de couverture au périmètre du manuscrit",
     'expression': '282 / 407 * 100', 'attendu': 69.3},
    {'unite': 'Md€', 'tolerance': 0.01,
     'objet': "écart de périmètre entre le manuscrit et le proto — gestion et "
              "action sociale",
     'expression': '407 - 388', 'attendu': 19},
    # ----------------------------------------------------------------- santé
    {'id': 'P-D-069', 'unite': 'Md€', 'tolerance': 0.01,
     'objet': "dépenses médicales, public + mutuelles + reste à charge",
     'expression': '200.5 + 32.5 + 20', 'attendu': 253},
    {'unite': 'millions', 'tolerance': 0.1,
     'objet': "population implicite des dépenses médicales par habitant",
     'expression': '253000 / 3723', 'attendu': 68},
    {'id': 'P-D-074', 'unite': 'Md€', 'tolerance': 0.01,
     'objet': "soins de longue durée par objet",
     'expression': '15.3 + 35.9 + 1', 'attendu': 52.2},
    {'unite': 'Md€', 'tolerance': 0.15,
     'objet': "soins de longue durée par financeur",
     'expression': '38.3 + 14', 'attendu': 52.2},
    {'id': 'P-D-078', 'unite': 'Md€', 'tolerance': 0.01,
     'objet': "frais de gestion de la santé",
     'expression': '7 + 1.2 + 8.7', 'attendu': 16.9},
    {'id': 'P-D-088', 'unite': 'Md€', 'tolerance': 0.5,
     'objet': "recettes sociales socle",
     'expression': '304.2 + 6.9 + 11 + 21 + 14 + 10.5', 'attendu': 368},
    {'id': 'P-D-093', 'unite': 'Md€', 'tolerance': 0.01,
     'objet': "compte santé, dépenses fléchées et mutuelles",
     'expression': '100 + 41', 'attendu': 141},
    {'unite': 'Md€', 'tolerance': 0.01,
     'objet': "l'architecture cible épuise le total à répartir",
     'expression': '142 + 100', 'attendu': 242},
    {'id': 'P-D-097', 'unite': 'Md€', 'tolerance': 0.01,
     'objet': "charges sociales redécoupées entre santé et retraite",
     'expression': '100 + 122 + 146', 'attendu': 368},
    {'id': 'P-D-081', 'unite': 'Md€', 'tolerance': 3.0,
     'objet': "dépenses publiques de santé à répartir, recomposées depuis les "
              "postes du proto — l'écart de 2,9 Md€ est admis à ce stade, "
              "arbitrage de l'auteur du 20260825",
     'expression': '200.5 + 38.3 + 6.1', 'attendu': 242},
    # ------------------------------------- le tableau de référence du classeur
    {'unite': 'Md€', 'tolerance': 0.05,
     'objet': "chèques ciblés aux particuliers, détail de l'onglet Détail "
              "Economies : APL + chèque énergie + autres",
     'expression': '16.1 + 0.6 + 1.0', 'attendu': 17.7},
    {'unite': 'Md€', 'tolerance': 0.05,
     'objet': "les chèques aux ménages du détail moins ce que le tableau de "
              "référence classe ailleurs — AME et exonérations emploi à domicile",
     'expression': '19.9 - 1.1 - 1.1', 'attendu': 17.7},
    {'unite': 'Md€', 'tolerance': 0.05,
     'objet': "aides aux particuliers et associations, les quatre postes de la "
              "chaîne de D2-4-1-e2",
     'expression': '17.7 + 3.6 + 3.2 + 3.0', 'attendu': 27.5},
    {'unite': 'Md€', 'tolerance': 0.05,
     'objet': "aides à l'emploi, l'apprentissage et l'insertion : France "
              "Compétences, France Travail, aides emploi-apprentissage, aide "
              "emploi-insertion",
     'expression': '10.6 + 2.7 + 6.9 + 2.3', 'attendu': 22.5},
    {'unite': 'Md€', 'tolerance': 0.05,
     'objet': "aides aux entreprises, les trois postes de la chaîne",
     'expression': '22.5 + 6.6 + 12.3', 'attendu': 41.4},
    {'unite': 'Md€', 'tolerance': 0.06,
     'objet': "économies sur les subventions, entreprises et particuliers",
     'expression': '41.4 + 27.5', 'attendu': 68.9},
    {'unite': 'Md€', 'tolerance': 0.05,
     'objet': "hébergement d'urgence et aide médicale d'État",
     'expression': '2.5 + 1.1', 'attendu': 3.6},
    {'unite': 'Md€', 'tolerance': 0.06,
     'objet': "les 236 Md€ : baisses de dépenses et niches restituées",
     'expression': '183.95 + 52.1', 'attendu': 236.05},
    {'unite': 'Md€', 'tolerance': 0.01,
     'objet': "les 184 Md€ de baisses de dépenses : État et agences, "
              "collectivités, assurance chômage, rendement du patrimoine cédé "
              "— **c'est ici que les 30 Md€ de chômage entrent dans les 236**",
     'expression': '82.4547 + 53.5 + 30 + 18', 'attendu': 183.9547},
    {'unite': 'Md€', 'tolerance': 0.05,
     'objet': "niches fiscales : gain direct restituable et gains compensés",
     'expression': '52.1 + 91.1', 'attendu': 143.2},
    # ------------------------- la remontée des sectoriels vers le REF_doctrine
    # Ce que l'annexe 2 du tome I porte, ligne par ligne, et ce que le
    # référentiel en fait. Voir methode/grille_lecture_budgetaire.md : un
    # agrégat de la doctrine est une somme de lignes filtrées, plus ce qui vient
    # d'ailleurs. Chercher le chiffre tel quel au document budgétaire ne le
    # trouve pas.
    {'id': 'R-D2-2-1-s2', 'unite': 'Md€', 'tolerance': 0.05,
     'objet': "France Compétences : restitué en année 1 3 374,90 + restitué "
              "ensuite 6 749,80 = 10 124,69 M€ d'économie restituée totale, "
              "plus 434,07 de subvention budgétaire",
     'expression': '(3374.8979736 + 6749.7959472 + 434.0712519) / 1000',
     'attendu': 10.6},
    {'id': 'R-D2-2-1-s4', 'unite': 'Md€', 'tolerance': 0.02,
     'objet': "Agences de l'eau : restitué en année 1 695,12 + restitué "
              "ensuite 1 390,24",
     'expression': '(695.1201867 + 1390.2403734) / 1000', 'attendu': 2.1},
    {'id': 'R-D2-2-1-s5', 'unite': 'Md€', 'tolerance': 0.02,
     'objet': "Action Logement : restitué en année 1 636,67 + restitué "
              "ensuite 1 273,33",
     'expression': '(636.666666666667 + 1273.33333333333) / 1000',
     'attendu': 1.9},
    {'id': 'R-D2-2-1-s9', 'unite': 'Md€', 'tolerance': 0.02,
     'objet': "AFITF : restitué en année 1 seulement, rien ensuite",
     'expression': '715.690299058824 / 1000', 'attendu': 0.7},
    {'unite': 'M€', 'tolerance': 0.5,
     'objet': "économie restituée totale des taxes affectées : 8 119,67 "
              "restitués en année 1 + 9 802,72 restitués ensuite",
     'expression': '8119.66998217549 + 9802.72165393334',
     'attendu': 17922.3916361088},
    {'unite': 'entités', 'tolerance': 0.5,
     'objet': "les 434 opérateurs du PLF se répartissent entre les cinq "
              "régimes, un chacun",
     'expression': '15 + 123 + 36 + 226 + 34', 'attendu': 434},
    {'unite': 'ETPT', 'tolerance': 1.0,
     'objet': "les emplois des opérateurs se répartissent de même",
     'expression': '10476 + 99885 + 25039 + 326723 + 17391', 'attendu': 479514},
    {'unite': 'agences', 'tolerance': 0.5,
     'objet': "les 1 104 agences d'État : opérateurs du PLF, organismes hors "
              "PLF, autorités indépendantes, commissions",
     'expression': '434 + 328 + 24 + 318', 'attendu': 1104},
    {'unite': 'agences', 'tolerance': 0.5,
     'objet': "les structures à fermer selon la synthèse des agences : "
              "suppression 668 + cession d'actif 78. **Le référentiel en "
              "déclare 750 : quatre unités d'écart, à instruire.**",
     'expression': '668 + 78', 'attendu': 746},
    {'unite': 'M€', 'tolerance': 0.5,
     'objet': "dépenses fiscales : la réalisation 2024 augmentée de la TVA des "
              "administrations publiques ajoute 11,9 Md€ à ce que le PLF publie",
     'expression': '101320.988610478 - 89406', 'attendu': 11914.988610478},
    # ------------------------------------------------ patrimoine et restitution
    {'unite': 'Md€', 'tolerance': 0.01,
     'objet': "actifs à valoriser et transférer, onglet Capitalisation",
     'expression': '208.28 + 200.1954 + 57.7333 + 169.8914', 'attendu': 636.1},
    {'unite': 'Md€', 'tolerance': 0.01,
     'objet': "rendement annuel des actifs cédés, 2,9 % de 636,1",
     'expression': '636.1 * 0.029', 'attendu': 18.4469},
    {'unite': 'Md€', 'tolerance': 1.5,
     'objet': "parc social : actif brut moins encours de dette. Le classeur "
              "donne 341,44 ; la note e118 du manuscrit écrit « estimé à 340 "
              "milliards », arrondi assumé de communication",
     'expression': '513.3372 - 171.9', 'attendu': 340},
    {'id': 'R-lexique-capital-de-restitution-i1', 'unite': '€/an',
     'tolerance': 0.01,
     'objet': "rendement permanent par personne, 8 823,53 € à 3 %",
     'expression': '8823.53 * 0.03', 'attendu': 264.71},
    {'unite': '€', 'tolerance': 1.0,
     'objet': "capital par personne, 20 000 € par foyer rapportés à la taille "
              "moyenne du foyer fiscal",
     'expression': '20000 / 2.2667', 'attendu': 8823.53},
    # --------------------------------------------------------- CSG et salaires
    {'id': 'R-D3-2-1-p6', 'unite': '€', 'tolerance': 0.001,
     'objet': "un point de CSG au SMIC brut, assiette à 98,25 %",
     'expression': '1801.80 * 0.9825 * 0.01', 'attendu': 17.702685},
    {'unite': '%', 'tolerance': 0.01,
     'objet': "l'abattement de 1,75 % est le complément de 98,25, non de 98",
     'expression': '100 - 98.25', 'attendu': 1.75},
    {'id': 'R-D9-3-1-e1', 'unite': '€', 'tolerance': 0.001,
     'objet': "gain net par euro gagné au taux unique de 23 %",
     'expression': '1 - 0.23', 'attendu': 0.77},
    # ------------------------------------------------- aide fondamentale et enfants
    {'id': 'R-D9-4-1-p1', 'unite': '€/mois', 'tolerance': 0.01,
     'objet': "aide par enfant, moitié de l'aide fondamentale",
     'expression': '550 * 0.5', 'attendu': 275},
    {'id': 'R-D10-2-1-p1', 'unite': '€/an', 'tolerance': 0.01,
     'objet': "compte éducation annuel",
     'expression': '550 * 12', 'attendu': 6600},
    {'id': 'R-D9-2-3-p2', 'unite': '€/mois', 'tolerance': 0.01,
     'objet': "total perçu au titre du handicap, aide fondamentale et part "
              "supplémentaire",
     'expression': '550 + 550', 'attendu': 1100},
    {'unite': 'Md€', 'tolerance': 0.01,
     'objet': "écart entre les deux bornes de population du coût de l'aide "
              "fondamentale — onglet CI unique",
     'expression': '417.285 - 386.727', 'attendu': 30.558},
    {'unite': 'millions', 'tolerance': 0.01,
     'objet': "population 2025, adultes et enfants — onglet CI unique",
     'expression': '54.5 + 14.1', 'attendu': 68.6},
    {'unite': 'millions', 'tolerance': 0.05,
     'objet': "population fiscale 2025, adultes et enfants — onglet CI unique",
     'expression': '50.4 + 13.04', 'attendu': 63.4},
]


# ------------------------------------------------------------------- la veille
# Le détecteur de collisions de `relever_protos.py` compare des vocabulaires, et
# il rate ce qui se dit en peu de mots. « Le salaire médian français est de
# 2 100 € par mois, contre 5 500 € en Suisse » ne partage presque rien avec les
# énoncés du référentiel, et contredit pourtant le manuscrit deux fois.
#
# La veille prend le problème dans l'autre sens : **on part du fait, pas du
# hasard lexical.** Pour une grandeur qui sort à l'écran, on écrit les mots qui
# la désignent et les valeurs qui sont admises. Toute phrase d'un proto qui
# emploie ces mots et porte un autre chiffre sort en alerte.
#
# Ce bloc grandit à mesure que des grandeurs deviennent publiables. Il n'a pas
# vocation à couvrir le référentiel : seulement ce qui se dit dehors.
VEILLE = [
    {
        'fait': "salaire médian net mensuel",
        'mots': ['salaire', 'median'],
        'valeurs_admises': [2190, 300, 600, 13, 2],
        'note': "2 190 € nets par mois en 2024, notes e4 et e99 du manuscrit. "
                "**À ne pas confondre avec le revenu médian équivalent** que le "
                "corps du livre oppose à la Suisse — 2 100 € contre 4 300 €, "
                "source Eurostat, note e8. Deux grandeurs, deux sources : "
                "employer « salaire médian » pour la seconde est une faute.",
    },
    {
        'fait': "revenu médian équivalent comparé à la Suisse",
        'mots': ['suisse'],
        'valeurs_admises': [4300, 2100, 2000, 2, 8, 10, 200, 4000, 5.8,
                            170, 21, 55, 90],
        'note': "4 300 € par mois en Suisse contre 2 100 € en France, revenu "
                "réel médian, Eurostat, note e8. **5 500 € pour la Suisse n'est "
                "à aucun endroit du corpus** : au manuscrit, 5 500 € est la "
                "dette publique nouvelle par foyer et par an.",
    },
    {
        'fait': "restitution mensuelle au travailleur type",
        'mots': ['restitu'],
        'valeurs_admises': [600, 300, 13, 2, 550],
        'note': "600 €/mois au travailleur type, 300 €/mois au salaire médian "
                "pour la seule part salariale, +13 % en un an.",
    },
    {
        'fait': "pension de base par répartition",
        'mots': ['repartition'],
        'valeurs_admises': [1100, 200, 400, 550, 6, 25],
        'note': "1 100 €/mois, verbatim du manuscrit : « une pension de base "
                "égale à 1 100 euros par mois pour tous les travailleurs ». "
                "La Q&A du 20260806 écrit « environ 1000 € » : elle est "
                "antérieure et non régénérée.",
    },
    {
        'fait': "taux de prélèvements obligatoires",
        'mots': ['prelevements', 'obligatoires'],
        'valeurs_admises': [42.87, 36.33, 36, 43, 191.046, 191],
        'note': "42,87 % aujourd'hui, 36,33 % en cible, soit 191,046 Md€ de "
                "baisse.",
    },
    {
        'fait': "aide fondamentale universelle",
        'mots': ['aide', 'fondamentale'],
        'valeurs_admises': [550, 275, 1100, 18],
        'note': "550 €/mois par adulte, 275 € par enfant, 1 100 € au total "
                "pour les personnes handicapées.",
    },
    {
        'fait': "capital de restitution par personne",
        'mots': ['capital', 'restitu'],
        'valeurs_admises': [20000, 8823.53, 8800, 3, 24, 264.71, 265, 519.62,
                            600, 636.1, 150, 17, 18],
        'note': "20 000 € par foyer, 8 823,53 € par personne. Le corpus "
                "communique sur 600 Md€ d'actifs cédés là où le classeur en "
                "valorise 636,1 : la promesse est prudente.",
    },
]


def _table_meme_que():
    """identifiant → (référence du groupe, intitulé du fait)."""
    t = {}
    for groupe in MEME_QUE:
        membres = groupe['entrees']
        reference = membres[0]
        for m in membres:
            t[m] = (None if m == reference else reference, groupe['fait'])
    return t


TABLE_MEME_QUE = _table_meme_que()


def meme_que(identifiant):
    """Ce que le rapprochement écrit à la main dit de cette entrée, ou rien.

    Rend `meme_que` — l'entrée de référence du groupe, absente pour la référence
    elle-même — et `fait`, l'intitulé du fait partagé.
    """
    if identifiant not in TABLE_MEME_QUE:
        return {}
    reference, fait = TABLE_MEME_QUE[identifiant]
    out = {'fait_partage': fait}
    if reference:
        out['meme_que'] = reference
    return out


def compte_meme_que():
    return len(MEME_QUE), len(TABLE_MEME_QUE)
