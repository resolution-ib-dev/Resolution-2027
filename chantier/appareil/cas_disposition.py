# -*- coding: utf-8 -*-
"""Les cas travaillés de la rédaction cible — construits, jamais retapés.

Chaque cas est un couple (texte de départ, texte révisé) plus la disposition
modificative écrite en opérations typées. Le texte de départ vient du dépôt de
droit public : rien ici n'est saisi à la main, et le rejeu se refait à
l'identique tant que le millésime du dépôt ne bouge pas.

Trois cas, un par opération dominante :

  1. abroger l'article entier          C est vide
  2. abroger deux subdivisions         la seconde renvoie aux alinéas de la
                                       première — la cascade y est réelle
  3. insérer une référence             A relevé à la date de dépôt du texte,
                                       C relevé au millésime courant. Montre le
                                       cas où la formule littérale du texte
                                       déposé échoue et l'opération passe

Usage : python3 cas_disposition.py [--ecrire <sortie.json>]
        puis : python3 reappliquer.py <sortie.json>
"""
import json
import os
import re
import sys

DROIT = os.path.join(os.path.dirname(__file__), '..', 'droit')

# Le jour où le texte en discussion a été écrit. La colonne A se lit à cette
# date et non au millésime courant : un article que la loi adoptée a modifié
# depuis porte aujourd'hui le résultat, pas le point de départ.
DEPOT_PLF = os.environ.get('DATE_DEPOT', '2025-10-01')


def _droit():
    sys.path.insert(0, os.path.abspath(DROIT))
    import droit as d
    return d


def _bloc(lignes, marque):
    """Les lignes d'une subdivision d'énumération, du marqueur au suivant."""
    i = next(k for k, l in enumerate(lignes) if l.startswith(marque))
    j = i + 1
    while j < len(lignes) and not re.match(r'^(\d+°|III\.)', lignes[j]):
        j += 1
    return i, j


def cas():
    d = _droit()
    sortie = []

    # 1 — abroger l'article entier.
    a = d.article("code monétaire et financier", "L. 221-5")
    sortie.append({
        'intitule': "abroger l'article entier — CMF L. 221-5",
        'source': a['id'], 'version': a['date_debut'],
        'a': a['texte'], 'c': '',
        'forme': [{'op': 'abroger'}],
    })

    # 2 — abroger deux subdivisions d'une énumération, avec cascade interne.
    a = d.article("code général des impôts", "150 U")
    t = a['texte']
    A = t[t.index('II. – '):t.index('III. – ')]
    lignes = A.split('\n')
    i7, j7 = _bloc(lignes, '7° ')
    i8, j8 = _bloc(lignes, '8° ')
    frag7, frag8 = '\n'.join(lignes[i7:j7]), '\n'.join(lignes[i8:j8])
    C = '\n'.join(lignes[:i7] + ['7° (Abrogé) ;', '8° (Abrogé) ;'] + lignes[j8:])
    sortie.append({
        'intitule': 'abroger une subdivision — CGI 150 U, 7° et 8° du II',
        'source': a['id'], 'version': a['date_debut'],
        'a': A, 'c': C,
        'forme': [{'op': 'remplacer', 'fragment': frag7, 'par': '7° (Abrogé) ;'},
                  {'op': 'remplacer', 'fragment': frag8, 'par': '8° (Abrogé) ;'}],
        'note': "Le 8° renvoie « aux quatrième, septième et avant-dernier "
                "alinéas du 7° du présent II » : abroger le seul 7° laisserait "
                "un renvoi mort. C'est le balayage de couverture qui le voit, "
                "pas le levier.",
    })

    # 3 — insérer une référence dans un alinéa. Les deux colonnes sont
    # **relevées**, chacune à sa date : A au jour du dépôt du texte, C au
    # millésime courant. Le cas ne suppose rien de ce qui a été voté — il
    # constate un état antérieur et un état actuel.
    #
    # Ce cas a d'abord été construit en fabriquant A depuis le texte actuel, ce
    # qui supposait que la disposition déposée était ce qui avait produit le
    # texte actuel. La supposition est fausse en général : le droit en vigueur
    # porte l'effet de la loi **adoptée**, amendements compris. Elle se trouvait
    # juste ici, ce qui est le pire des cas — une méthode fausse qui donne le
    # bon résultat une fois.
    REPERE = "4° Sous réserve des dispositions de l'article 153"

    def alinea(art):
        t = art['texte']
        deb = t.index(REPERE)
        return t[deb:t.index('\n', deb)]

    av = d.article("code général des impôts", "39", jour=DEPOT_PLF)
    ap = d.article("code général des impôts", "39")
    Aa, Cc = alinea(av), alinea(ap)
    if Aa == Cc:
        raise SystemExit("l'alinéa n'a pas changé entre les deux dates — cas à "
                         "reprendre sur pièce, jamais à retaper")
    a = ap
    sortie.append({
        'intitule': 'insérer une référence — CGI 39, premier alinéa du 4° du 1',
        'source': a['id'], 'version': a['date_debut'],
        'a': Aa, 'c': Cc,
        'forme': [{'op': 'inserer_apres', 'fragment': '231 quater, ',
                   'texte': '235 ter C, '}],
        'source_a': av['id'], 'version_a': av['date_debut'], 'date_a': DEPOT_PLF,
        'note': "A relevé au jour du dépôt, C au millésime courant. Ce que le "
                "cas montre : la formule littérale — « après la référence : "
                "« 231 quater », il est inséré la référence : « 235 ter C, » » "
                "— rejouée au mot produit « 231 quater235 ter C, , » ; "
                "l'opération porte sur le fragment séparateurs compris.",
    })
    return sortie


def main(argv):
    c = cas()
    if '--ecrire' in argv:
        chemin = argv[argv.index('--ecrire') + 1]
        with open(chemin, 'w', encoding='utf-8', newline='') as f:
            json.dump(c, f, ensure_ascii=False, indent=1)
            f.write('\n')
        print(f'{chemin} — {len(c)} cas')
    else:
        for x in c:
            print(f'{x["intitule"]} — A {len(x["a"])} o, C {len(x["c"])} o, '
                  f'{x["source"]} du {x["version"]}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
