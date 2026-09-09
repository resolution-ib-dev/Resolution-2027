# -*- coding: utf-8 -*-
"""Les hypothèses de chiffrage énoncées au manuscrit, consignées à la doctrine.

Le livre pose ses hypothèses **en littéraire** : un multiplicateur de 0,5, un
socle de 15 %, une durée de retraite de 24 ans, un chiffrage déclaré prudent et
minorant. Elles commandent tous les chiffres, et jusqu'ici **aucun référentiel
ne les portait** — ni le `REF_doctrine`, qui tient des paramètres de mesure, ni
le référentiel des faits, qui tient des valeurs.

Une hypothèse n'est ni un fait ni un paramètre. C'est ce sous quoi un fait vaut.
La distinction porte : quand un PLF neuf arrive, ce sont les hypothèses qu'on
réexamine, et les faits se recalculent tout seuls.

## Ce que porte une entrée

    id            H-nn, dans l'ordre de première rédaction
    intitule      ce que l'hypothèse pose, en une ligne
    nature        methode · parametre · comportement · source_externe
    sens          minorant · majorant · neutre — dans quel sens elle penche
    domaine       fiscal · chomage · retraite · patrimoine · education ·
                  croissance · risque · methode
    note          l'identifiant de la note de fin qui la porte, ou null
    ancre         l'ancre de section du corps du manuscrit, ou null
    repere        un fragment littéral du manuscrit, court, qui permet de la
                  retrouver — **et que le contrôle vérifie**
    commande      les nœuds du REF_doctrine et les entrées du référentiel des
                  faits qui en dépendent
    varie         ce qui se passe si on la relâche, quand c'est instruit

## Le verbatim ne se recopie pas

A-21 : recopier un verbatim du manuscrit le fait passer par le modèle, et une
dérive de recopie corrompt la strate 1 en silence. Une hypothèse ne porte donc
**pas** le texte du livre : elle porte un `repere` court, dont
`controle_hypotheses.py` vérifie la présence littérale au manuscrit. Le texte
complet se tire de la note à la projection, comme A-33 le pose.

Un repère qui ne se retrouve plus est une alerte : soit le manuscrit a changé,
soit la recopie a dérivé. Dans les deux cas on s'arrête.
"""

HYPOTHESES = [
    # ------------------------------------------------------------- méthode
    {
        'id': 'H-01',
        'intitule': "Le chiffrage d'ensemble est prudent, et plusieurs leviers "
                    "ne sont pas chiffrés malgré des bénéfices tenus pour "
                    "certains",
        'nature': 'methode',
        'sens': 'minorant',
        'domaine': 'methode',
        'note': 'e5',
        'ancre': None,
        'repere': "Ces estimations reposent sur des hypothèses prudentes.",
        'commande': ['D2-1-1-e1'],
        'varie': "Non instruit. C'est l'hypothèse qui autorise à dire que le "
                 "plan rend au moins ce qu'il annonce.",
    },
    {
        'id': 'H-02',
        'intitule': "Le produit intérieur brut compte la contribution publique "
                    "à hauteur de ce qu'elle coûte, et surestime donc la "
                    "richesse collective",
        'nature': 'methode',
        'sens': 'majorant',
        'domaine': 'methode',
        'note': None,
        'ancre': None,
        'repere': "l’hypothèse maximaliste que la valeur que nous en retirons "
                  "correspond entièrement à ses coûts",
        'commande': ['D11-e1'],
        'varie': "Toute amélioration de la qualité de la dépense publique "
                 "reste invisible au produit intérieur brut : le gain réel du "
                 "plan est supérieur à ce que l'agrégat enregistre.",
    },
    {
        'id': 'H-03',
        'intitule': "La solidarité se compte à son montant réellement versé, "
                    "non à son montant facial, le non-recours étant retiré",
        'nature': 'methode',
        'sens': 'neutre',
        'domaine': 'methode',
        'note': None,
        'ancre': None,
        'repere': "on prend ainsi en compte la solidarité moyenne réelle, et "
                  "non le montant facial de l’aide",
        'commande': ['D9-2-1-p1'],
        'varie': "Un sur-recours à l'aide fondamentale, qui est automatique et "
                 "sans dossier, augmenterait la dépense à due concurrence. Le "
                 "manuscrit le dit et ne le chiffre pas.",
    },
    # -------------------------------------------------------------- fiscal
    {
        'id': 'H-04',
        'intitule': "Un multiplicateur de 0,5 s'applique aux assiettes "
                    "économiques optimisables, hors revenus de remplacement",
        'nature': 'parametre',
        'sens': 'minorant',
        'domaine': 'fiscal',
        'note': 'e97',
        'ancre': None,
        'repere': "multiplicateur de 0,5 sur les assiettes économiques "
                  "optimisables",
        'commande': ['D2-5-1-p1', 'D2-5-1-p2', 'D2-5-1-e2'],
        'varie': "Un multiplicateur de 1 doublerait le rendement attendu de la "
                 "suppression des niches sur les assiettes concernées. Le "
                 "classeur applique 0,5 par la colonne « % économie nette ».",
    },
    {
        'id': 'H-05',
        'intitule': "Un champ de l'ordre de 30 Md€ de secteurs sensibles est "
                    "écarté de la restitution immédiate",
        'nature': 'parametre',
        'sens': 'minorant',
        'domaine': 'fiscal',
        'note': 'e97',
        'ancre': None,
        'repere': "ne pouvant pas faire l’objet d’une redistribution nette "
                  "immédiate écarté de la restitution immédiate",
        'commande': ['D2-5-1-p5'],
        'varie': "Ces 30 Md€ ne sont pas perdus : ils sont différés. Le "
                 "manuscrit ne dit pas à quel horizon.",
    },
    # ------------------------------------------------------------ chômage
    {
        'id': 'H-06',
        'intitule': "L'indemnisation collective est ramenée à six mois, les "
                    "cotisations étant intégralement restituées au-delà",
        'nature': 'parametre',
        'sens': 'neutre',
        'domaine': 'chomage',
        'note': None,
        'ancre': None,
        'repere': "garder six mois d’indemnisation chômage collective et de "
                  "rendre intégralement les cotisations aux travailleurs "
                  "au-delà",
        'commande': ['D8-3-1-p1', 'D8-3-1-e2'],
        'varie': "C'est le seul paramètre de chômage que le livre pose. **Les "
                 "deux autres — 37 % des inscrits sous six mois, allocation "
                 "cible à 52 % de l'allocation moyenne — ne sont qu'au proto "
                 "Données**, et ce sont eux qui font les 30 Md€.",
    },
    {
        'id': 'H-07',
        'intitule': "La durée moyenne d'inscription au chômage dépasse d'un "
                    "mois seulement le droit à indemnisation",
        'nature': 'comportement',
        'sens': 'neutre',
        'domaine': 'chomage',
        'note': None,
        'ancre': None,
        'repere': "soit tout juste un mois de plus que le droit à "
                  "indemnisation",
        'commande': ['D8-3-1-e1'],
        'varie': "C'est l'énoncé comportemental qui fonde la mesure : la durée "
                 "d'inscription suit le droit. Le manuscrit l'affirme sans le "
                 "démontrer.",
    },
    # ----------------------------------------------------------- retraite
    {
        'id': 'H-08',
        'intitule': "Trois pour cent de rendement net et vingt-quatre ans de "
                    "durée de retraite",
        'nature': 'parametre',
        'sens': 'minorant',
        'domaine': 'retraite',
        'note': 'e119',
        'ancre': None,
        'repere': "Sous l’hypothèse prudente de 3 % de rendement net et d’une "
                  "durée de retraite de 24 ans",
        'commande': ['D7-2-2-p1', 'D7-2-2-e1', 'D7-2-2-e2'],
        'varie': "**Le classeur applique 2,9 %**, non 3 : 636,1 Md€ × 2,9 % "
                 "font les 18,4469 Md€ de rendement annuel. L'écart est dans "
                 "le sens de la prudence.",
    },
    {
        'id': 'H-09',
        'intitule': "Pendant vingt-cinq ans, la pension est calculée sur les "
                    "cotisations de l'ancien régime et le capital du nouveau, "
                    "et reste au moins équivalente à celle du régime actuel",
        'nature': 'parametre',
        'sens': 'neutre',
        'domaine': 'retraite',
        'note': None,
        'ancre': None,
        'repere': "assurant une pension au moins équivalente au régime actuel",
        'commande': ['D8-2-3-p1'],
        'varie': "Garantie de non-régression sur la transition. Elle borne "
                 "l'économie retraite à zéro pendant vingt-cinq ans.",
    },
    # --------------------------------------------------------- patrimoine
    {
        'id': 'H-10',
        'intitule': "La valorisation du parc social conserve un socle de 15 % "
                    "et applique une décote de liquidité de 15 %",
        'nature': 'parametre',
        'sens': 'minorant',
        'domaine': 'patrimoine',
        'note': 'e118',
        'ancre': None,
        'repere': "hypothèse prudente un socle de 15 % conservé et une décote "
                  "de liquidité de 15 %",
        'commande': ['D7-3-1-p1', 'D7-3-1-e1'],
        'varie': "Le manuscrit relève lui-même que la décote de liquidité est "
                 "en miroir un bénéfice pour les acquéreurs : elle ne "
                 "disparaît pas, elle change de main.",
    },
    # ---------------------------------------------------------- éducation
    {
        'id': 'H-11',
        'intitule': "Le compte éducation part du coût public réel, reste "
                    "au-dessus du seuil où la performance décroche des "
                    "dépenses, et conserve 10 à 15 % de soutien et de support",
        'nature': 'parametre',
        'sens': 'minorant',
        'domaine': 'education',
        'note': 'e132',
        'ancre': None,
        'repere': "conserve de manière prudente 10 à 15 % de dépenses de "
                  "soutien aux publics fragiles",
        'commande': ['D10-2-1-p1'],
        'varie': "Le seuil de décrochage est situé à 6 000–6 500 € par an et "
                 "par élève d'après l'OCDE ; les 6 600 € du compte éducation "
                 "sont au-dessus, de peu.",
    },
    # -------------------------------------------------------- croissance
    {
        'id': 'H-12',
        'intitule': "Le gain d'ensemble est déduit d'estimations externes, non "
                    "mesuré : perte de PIB privée documentée et perte de "
                    "productivité publique d'environ un tiers",
        'nature': 'source_externe',
        'sens': 'neutre',
        'domaine': 'croissance',
        'note': 'e32',
        'ancre': None,
        'repere': "Ordre de grandeur évalué par Résolution, et déduit des "
                  "estimations disponibles",
        'commande': [],
        'varie': "C'est l'assise des « environ 10 % » et des 10 000 € par "
                 "foyer. Un ordre de grandeur déduit, non un chiffrage.",
    },
    {
        'id': 'H-13',
        'intitule': "Passer du trente-sixième au premier rang de compétitivité "
                    "fiscale vaudrait de l'ordre de cinq points de croissance",
        'nature': 'source_externe',
        'sens': 'neutre',
        'domaine': 'croissance',
        'note': 'e106',
        'ancre': None,
        'repere': "pourrait augmenter la croissance économique de l’ordre de "
                  "5 points",
        'commande': [],
        'varie': "Ne s'additionne pas aux 10 % de H-12 sans examen : deux "
                 "leviers distincts, recouvrement non instruit.",
    },
    {
        'id': 'H-14',
        'intitule': "Les ménages épargnent par anticipation des impôts futurs, "
                    "et la hausse de déficit ne relance pas",
        'nature': 'comportement',
        'sens': 'neutre',
        'domaine': 'croissance',
        'note': None,
        'ancre': None,
        'repere': "les ménages épargnent par anticipation, et la hausse de "
                  "déficit ne relance rien",
        'commande': [],
        'varie': "Équivalence ricardienne. Elle est l'argument contre "
                 "l'objection keynésienne à la baisse de dépense, et elle est "
                 "contestée.",
    },
    # -------------------------------------------------------------- risque
    {
        'id': 'H-15',
        'intitule': "Le coût d'une rupture d'accès au crédit souverain est "
                    "d'au moins sept points, sous l'hypothèse la plus "
                    "optimiste",
        'nature': 'parametre',
        'sens': 'minorant',
        'domaine': 'risque',
        'note': 'e141',
        'ancre': None,
        'repere': "sous l’hypothèse la plus optimiste où les recettes et les "
                  "dépenses sont fixées",
        'commande': [],
        'varie': "Le manuscrit dit lui-même que l'équilibre dégradé se situe "
                 "plus probablement à plusieurs dizaines de points.",
    },
    {
        'id': 'H-16',
        'intitule': "L'économie de surface immobilière de l'État est un "
                    "minorant, l'objectif officiel ne reflétant pas la "
                    "meilleure performance possible",
        'nature': 'methode',
        'sens': 'minorant',
        'domaine': 'methode',
        'note': None,
        'ancre': None,
        'repere': "Cette estimation est un minorant",
        'commande': [],
        'varie': "Non instruit.",
    },
]


def par_id():
    return {h['id']: h for h in HYPOTHESES}


def compte():
    return len(HYPOTHESES)
