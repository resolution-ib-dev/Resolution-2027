# -*- coding: utf-8 -*-
"""Nomenclature — les titres, les catégories, les traitements, les unités.

**Un montant sans qualification n'est pas un chiffre, c'est une apparence.**
34 096 M€ en catégorie 32 ne veut rien dire tant qu'on ne dit pas si c'est une
enveloppe portée au PLF, une part supprimable dès l'année 1, ou une économie
déjà restituée. Les trois se lisent dans les mêmes cellules du même onglet, et
rien dans le classeur ne les distingue — sinon un mot en colonne de gauche.

Ce module écrit ces distinctions une fois, à la main, et tout le reste s'y
réfère. Il ne calcule rien.

## Quatre tables

`TITRES` et `CATEGORIES` — la nomenclature par nature de la LOLF, telle que
l'article 5 de la loi organique la fixe. Elle est stable d'un exercice à
l'autre : c'est elle qui permet le rejeu.

`TRAITEMENTS` — le régime que l'auteur applique à une ligne de crédit, un mot
par programme et par catégorie. Ce n'est pas du PLF : c'est la décision.

`QUALIFICATIONS` — ce qu'un montant *est*. Une assiette n'est pas une économie ;
une économie d'année 1 n'est pas une économie pérenne ; un paramètre n'est ni
l'une ni l'autre. Chaque qualification porte son unité.

Rien ici ne se devine d'un libellé. Un mot inconnu se signale et reste inconnu.
"""

# ------------------------------------------------------------------ les titres
# Article 5 de la LOLF. Le titre 2 est le seul dont le plafond est limitatif au
# sens de l'article 7 : c'est pourquoi il se lit à part partout.
TITRES = {
    '1': "Dotations des pouvoirs publics",
    '2': "Dépenses de personnel",
    '3': "Dépenses de fonctionnement",
    '4': "Charges de la dette de l'État",
    '5': "Dépenses d'investissement",
    '6': "Dépenses d'intervention",
    '7': "Dépenses d'opérations financières",
}

# -------------------------------------------------------------- les catégories
# Les dix catégories que le classeur budgétaire retient, avec la colonne où il
# les porte. `court` est le mot que le classeur emploie en tête de colonne ;
# `officiel` est le libellé de la nomenclature. Les deux se disent, parce que
# c'est le premier qu'on lira dans une cellule et le second qui fait foi.
CATEGORIES = {
    '21': {'titre': '2', 'court': 'Salaires',
           'officiel': "Rémunérations d'activité", 'colonne': 'E'},
    '22': {'titre': '2', 'court': 'Cotisations',
           'officiel': "Cotisations et contributions sociales",
           'colonne': 'F'},
    '23': {'titre': '2', 'court': 'Prestations',
           'officiel': "Prestations sociales et allocations diverses",
           'colonne': 'G'},
    '31': {'titre': '3', 'court': 'Fonctionnement',
           'officiel': "Dépenses de fonctionnement autres que celles de "
                       "personnel", 'colonne': 'H'},
    '5': {'titre': '5', 'court': 'Investissement',
          'officiel': "Dépenses d'investissement", 'colonne': 'I'},
    '32': {'titre': '3', 'court': 'Opérateurs',
           'officiel': "Subventions pour charges de service public",
           'colonne': 'K', 'colonne_traitement': 'L'},
    '61': {'titre': '6', 'court': 'Ménages',
           'officiel': "Transferts aux ménages",
           'colonne': 'M', 'colonne_traitement': 'N'},
    '62': {'titre': '6', 'court': 'Entreprises',
           'officiel': "Transferts aux entreprises",
           'colonne': 'O', 'colonne_traitement': 'P'},
    '63': {'titre': '6', 'court': 'Collectivités',
           'officiel': "Transferts aux collectivités territoriales",
           'colonne': 'Q', 'colonne_traitement': 'R'},
    '64': {'titre': '6', 'court': 'Autres',
           'officiel': "Transferts aux autres collectivités",
           'colonne': 'S', 'colonne_traitement': 'T'},
}

# Les catégories que le classeur traite programme par programme. Les cinq
# autres — le titre 2 et le fonctionnement — se traitent par un taux global,
# non par une décision ligne à ligne.
CATEGORIES_TRAITEES = ('32', '61', '62', '63', '64')

# ------------------------------------------------------------- les traitements
# Le mot que l'auteur porte à côté d'un montant, pour un programme et une
# catégorie. Sept valeurs, aucune autre. `supprime` dit si le traitement retire
# le crédit ; `delai` dit en combien de temps.
TRAITEMENTS = {
    'Oui': {'intitule': "suppression immédiate",
            'sens': "le crédit est supprimé dès l'exercice",
            'supprime': True, 'delai': "année 1"},
    'En 3 ans': {'intitule': "extinction en trois ans",
                 'sens': "le crédit s'éteint progressivement ; une part est "
                         "restituée en année 1, le solde ensuite",
                 'supprime': True, 'delai': "trois ans"},
    'Fusion CI': {'intitule': "absorbé par le crédit d'impôt unique",
                  'sens': "le crédit ne disparaît pas, il change de véhicule "
                          "— ce n'est pas une économie",
                  'supprime': False, 'delai': None},
    'Bourse': {'intitule': "basculé en bourse",
               'sens': "le crédit devient une bourse ; ce n'est pas une "
                       "économie mais un changement de forme",
               'supprime': False, 'delai': None},
    'Sécu': {'intitule': "transféré à la sécurité sociale",
             'sens': "le crédit quitte le budget de l'État sans disparaître "
                     "de la dépense publique",
             'supprime': False, 'delai': None},
    'Flux OM': {'intitule': "laissé au flux outre-mer",
                'sens': "le crédit est maintenu au titre de la continuité "
                        "territoriale",
                'supprime': False, 'delai': None},
    'X': {'intitule': "mission régalienne",
          'sens': "marque le programme comme régalien — il sort des assiettes "
                  "« hors régalien »",
          'supprime': False, 'delai': None},
}

# --------------------------------------------------------- les qualifications
# Ce qu'un montant est. C'est la table qui manque partout ailleurs, et sans
# laquelle deux nombres de même unité se somment alors qu'ils ne devraient pas.
QUALIFICATIONS = {
    'credit_plf': {
        'intitule': "crédit porté au PLF", 'unite': 'M€',
        'sens': "les crédits de paiement de la catégorie, tels que le projet "
                "annuel de performance les publie. C'est du socle.",
        'sommable_avec': ('credit_plf',),
    },
    'suppression_immediate': {
        'intitule': "part supprimable dès l'année 1", 'unite': 'M€',
        'sens': "la fraction des crédits portée par des programmes dont le "
                "traitement retire le crédit sans délai.",
        'sommable_avec': ('suppression_immediate',),
    },
    'assiette': {
        'intitule': "assiette d'un poste nommé", 'unite': 'M€',
        'sens': "l'enveloppe sur laquelle une économie est prise. **Ce n'est "
                "pas une économie** : la confondre avec elle double le "
                "chiffrage.",
        'sommable_avec': (),
    },
    'economie_annee_1': {
        'intitule': "économie restituée en année 1", 'unite': 'M€',
        'sens': "ce que le classeur appelle « gage CSG » en budgétaire — la "
                "part restituable dès le premier exercice.",
        'sommable_avec': ('economie_annee_1',),
    },
    'economie_perenne': {
        'intitule': "économie restituée ensuite", 'unite': 'M€',
        'sens': "ce que le classeur appelle « pérenne » — le solde, restitué "
                "après l'année 1. **L'économie valorisable est le total des "
                "deux** (A-98).",
        'sommable_avec': ('economie_perenne',),
    },
    'emploi': {
        'intitule': "effectif", 'unite': 'ETP',
        'sens': "un nombre d'emplois, jamais un montant.",
        'sommable_avec': ('emploi',),
    },
    'parametre': {
        'intitule': "paramètre de calcul", 'unite': '€',
        'sens': "une valeur unitaire qui entre dans une formule — un salaire "
                "moyen. Ne se somme avec rien.",
        'sommable_avec': (),
    },
    'emploi_ou_montant_inconnu': {
        'intitule': "non qualifié", 'unite': None,
        'sens': "le classeur porte un montant sans mot pour le dire. Il reste "
                "non qualifié plutôt que d'être rangé au jugé.",
        'sommable_avec': (),
    },
}

# Les mots que le classeur emploie en tête de poste, et ce qu'ils qualifient.
# **Écrits à la main.** Un mot absent de cette table laisse le poste non
# qualifié — il ne se devine pas d'une ressemblance.
MOTS_DE_POSTE = {
    'gage csg': 'economie_annee_1',
    'pérenne': 'economie_perenne',
    'éco pérenne': 'economie_perenne',
    'éco t6 pérenne': 'economie_perenne',
    'taxes affectées': 'assiette',
    'hors frtravail': 'assiette',
    'nb etp etat supprimés': 'emploi',
    'salaire moyen en €': 'parametre',
    'non régalien': 'assiette',
    'en 3 ans': 'assiette',
    'fusion ci': 'assiette',
    'bourse': 'assiette',
    "fusion ci (budgétaire + fiscal)": 'assiette',
    'bourse (cb et ta)': 'assiette',
    # « sur X » n'est pas une assiette : c'est l'économie budgétaire prise sur
    # un poste, en année 1. La règle des préfixes la rangeait en assiette, ce
    # qui l'aurait comptée deux fois. Écrite à la main, vérifiée ligne à ligne
    # contre l'arbre des économies (A-116).
    'sur culture': 'economie_annee_1',
    'sur frcomp.': 'economie_annee_1',
    'sur ville': 'economie_annee_1',
    'mpr (anah)': 'economie_annee_1',
}

# Les préfixes qui marquent une assiette nommée. « dont X » découpe la
# catégorie, « T2/T6 X » isole une masse. **« sur X » n'en est pas** : c'est
# une économie, et elle est écrite à la table ci-dessus.
PREFIXES_ASSIETTE = ('dont ', 't2 ', 't6 ', 'fusion ci ', 'bourse ')


def qualifier(libelle):
    """La qualification d'un poste, d'après le mot que le classeur écrit.

    Rend un couple (qualification, certitude). La certitude est `ecrite` quand
    le mot figure aux tables, `deduite` quand seul un préfixe le désigne,
    `absente` quand rien ne le dit — et dans ce dernier cas le poste reste non
    qualifié.
    """
    if not libelle:
        return 'emploi_ou_montant_inconnu', 'absente'
    net = ' '.join(str(libelle).split()).lower()
    if net in MOTS_DE_POSTE:
        return MOTS_DE_POSTE[net], 'ecrite'
    for p in PREFIXES_ASSIETTE:
        if net.startswith(p):
            return 'assiette', 'deduite'
    return 'emploi_ou_montant_inconnu', 'absente'


def unite_de(qualification):
    return (QUALIFICATIONS.get(qualification) or {}).get('unite')


def titre_de(categorie):
    c = CATEGORIES.get(str(categorie))
    return c['titre'] if c else None


def libelle_de(categorie):
    c = CATEGORIES.get(str(categorie))
    return c['officiel'] if c else None


def traitement_de(mot):
    """Le sens d'un traitement, ou None si le mot n'est pas de la table."""
    return TRAITEMENTS.get(mot) if mot else None


if __name__ == '__main__':
    print(__doc__)
    print(f"{len(TITRES)} titres · {len(CATEGORIES)} catégories · "
          f"{len(TRAITEMENTS)} traitements · "
          f"{len(QUALIFICATIONS)} qualifications")
