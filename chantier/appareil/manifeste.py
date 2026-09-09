# -*- coding: utf-8 -*-
"""Le manifeste — le proto 1-pager remis à jour, et rien de plus.

**On ne le refait pas.** Le texte est celui de
`sources/1pager_20260806_v1_proto.html`, arrêté le 20260806. Ce module ne porte
que la **liste des corrections** que le corpus impose depuis, chacune avec son
arbitrage. Tout le reste passe mot pour mot.

C'est le même dispositif que `apports.py` et `justifications.py` : ce qui est
écrit à la main vit ici, le produit se régénère.

Deux garanties, et elles se contrôlent :

- **une correction dont le texte cherché n'est pas trouvé arrête la génération.**
  Un remplacement silencieux qui ne s'applique pas, c'est un livrable qui sort
  avec la vieille valeur sans que rien ne le dise.
- **aucune correction n'invente un chiffre.** Là où le proto porte un trou —
  le nombre d'agences cibles, resté à `xxx` — la phrase se réécrit pour ne dire
  que ce qui est sourcé, et le trou est déclaré ouvert plutôt que comblé.
"""

# (texte cherché, texte de remplacement, arbitrage, motif)
CORRECTIONS = [
    (
        'Le salaire médian français est de 2 100 € par mois, contre 5 500 € en '
        'Suisse.',
        'Le revenu médian français est de 2 100 € par mois, contre 4 300 € en '
        'Suisse.',
        'A-84, A-85',
        'Les 2 100 € sont le revenu médian équivalent d’Eurostat, non un '
        'salaire : la dénomination était fausse. Et la Suisse est à 4 300 € '
        '(note e8 du manuscrit) ; les 5 500 € sont la dette publique nouvelle '
        'par foyer, portés ici par erreur.',
    ),
    (
        'soit pour un salaire net de 2100 € par mois',
        'soit pour un salaire net de 2 190 € par mois',
        'A-85',
        'Le salaire médian net est de 2 190 € (notes e4 et e99, Insee). '
        'C’est bien un salaire net ici, donc c’est cette valeur qui vaut.',
    ),
    (
        '300 € par mois restitués dès la première année, soit +14 % de salaire '
        'net pour tous,',
        '300 € par mois restitués dès la première année, soit +13 % de salaire '
        'net pour tous,',
        'référentiel des positions',
        'Le corpus porte +13 % partout, y compris dans la galerie des fiches. '
        'Le +14 % est un état antérieur du chiffrage.',
    ),
    (
        '540 000 emplois publics arrêtés',
        '580 000 emplois publics arrêtés',
        'A-155',
        'Le décompte qui vaut est 580 000 postes publics, 10 % des 5,8 M '
        'd’agents. Les 0,54 M sont déclarés fautifs et obsolètes.',
    ),
    (
        'Huit ministères, aucun secrétariat d’Etat et xxx agences nationales '
        '(contre 1400 aujourd’hui).',
        'Huit ministères, aucun secrétariat d’État et 303 agences nationales '
        '(contre 1 104 aujourd’hui).',
        'A-130 et A-211',
        'La cible est 303 agences, fournie par l’auteur le 20260828 : elle est '
        'citable. Et le décompte actuel du corpus est 1 104 agences d’État, '
        'non 1 400.',
    ),
    (
        '600 milliards d’€ de patrimoine public rendu à chaque Français, soit '
        '9 000 € par habitant.',
        '600 milliards d’€ de patrimoine public rendu aux Français, soit '
        '20 000 € par foyer.',
        'A-211',
        'L’agrégat retenu est 20 000 € par foyer, arbitré par l’auteur, et '
        'c’est celui que porte tout le reste du corpus. Les 9 000 € par '
        'habitant sortent.',
    ),
    (
        ': 483 impôts, 486 niches fiscales',
        ': 438 impôts, 486 niches fiscales',
        'A-211, le manuscrit',
        'Le manuscrit porte 438 impôts. Les 483 du proto sont une valeur '
        'périmée.',
    ),
    (
        '<h2>La chute</h2>',
        '<h2>Le remède</h2>',
        'A-221',
        'Arbitré par l’auteur : « La chute » est un terme de chantier, tiré du '
        'découpage en mouvements du proto. Le mouvement s’appelle « Le remède » '
        '— « La solution » est déjà pris par le mouvement précédent.',
    ),
    (
        'des 76 codes de la Loi Française.',
        'des 76 codes de la loi française.',
        'A-221',
        'On ne met de majuscule que là où le français l’attend. Ni « loi » ni '
        '« française » n’en portent ici.',
    ),
    (
        'nos voisins Européens les plus sobres.',
        'nos voisins européens les plus sobres.',
        'A-221',
        'Adjectif de nationalité : minuscule. Même règle que ci-dessus.',
    ),
    (
        'indemnisé à 70 % du salaire pendant 7 ans',
        'indemnisé à 70 % du salaire jusqu’à sept ans',
        'A-210',
        'Sept ans est un plafond, non une durée acquise : un contrat à durée '
        'déterminée ne conserve pas le bénéfice au-delà de son terme. Tranché '
        'par l’auteur, et la règle vaut partout.',
    ),
]

# Ce que le manifeste ne corrige pas, et pourquoi. À lire avec les corrections :
# une absence de correction est une décision, elle se déclare aussi.
NON_CORRIGE = [
    ('« 486 niches fiscales »',
     'Le socle porte 465 dépenses fiscales au PLF 2026, à une autre date et à '
     'un autre périmètre. Rien ne prouve que ce nombre soit faux : il ne se '
     'corrige donc pas, il reste à instruire.'),
]

# Le titre était laissé à « [TITRE ?] » au proto. Il est arrêté depuis, et c'est
# celui du livre et de la page de garde.
TITRE = 'État partout, justice nulle part'

# Le proto portait un en-tête de chantier — statut, format relevé, mentions non
# arrêtées. A-154 l'interdit sur une page qui s'affiche.
RETIRER_ENTETE = True


def corriger(texte):
    """Applique les corrections déclarées, et s'arrête si l'une ne s'applique pas."""
    for cherche, remplace, arbitrage, _motif in CORRECTIONS:
        if texte.count(cherche) != 1:
            raise SystemExit(
                f'ÉCHEC — correction du manifeste ({arbitrage}) : '
                f'{texte.count(cherche)} occurrence(s) de « {cherche[:60]}… », '
                f'1 attendue. Le proto a changé, ou la correction est périmée.')
        texte = texte.replace(cherche, remplace)
    return texte
