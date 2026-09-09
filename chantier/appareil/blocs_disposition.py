# -*- coding: utf-8 -*-
"""Le bloc de disposition — l'unité que la rédaction cible rend, et qu'on note.

Relevé le 20260904, en construisant l'échantillon du banc. **Le couple (alinéa,
adresse) n'est pas l'unité de la disposition.** Il l'est pour le partage
calibrage / épreuve, qui compte des occasions de modifier ; il ne l'est pas pour
la notation, qui compare ce que la skill rend à ce que l'administration a écrit.

Le texte déposé écrit ses modifications en arbre :

    6° Au I de l'article 1418 :                     ← le chapeau porte l'adresse
    a) La première phrase … est complétée par …     ← l'opération est ici
    b) Après le troisième alinéa, il est inséré …   ← et ici
    « … »                                           ← le texte cité
    c) Au dernier alinéa, après le mot … »          ← et ici

Le couple ne retient que le chapeau, parce que c'est lui qui nomme l'article :
les subordonnés disent « le deuxième alinéa » et n'ont pas d'adresse à eux.
Noter la skill sur le chapeau seul, ce serait la noter sur « Au I de l'article
1418 : » — une phrase qui ne prescrit rien. **Et écarter les chapeaux ferait un
banc plus facile que le texte réel** : ce sont eux qui portent le cas dur du
contrat, plusieurs opérations sur un même article, rendues en une seule
colonne C.

Le bloc est donc : l'alinéa du couple, plus, s'il ouvre par un deux-points, tous
les alinéas qui le suivent jusqu'au premier de niveau égal ou supérieur.

Le niveau se lit au marqueur de tête, et rien d'autre — pas d'indentation dans
la sortie de l'extracteur :

    0   I. · II. · V. –   ·   A. · B. –
    1   1° · 12°
    2   a) · b)
    3   – en tête
    9   continuation : texte cité entre guillemets, ou phrase qui déborde

Une continuation appartient toujours au bloc en cours : un texte cité n'est
jamais une opération, c'est ce qu'elle écrit.

Usage : from blocs_disposition import bloc_pour, niveau
"""
import re

M_ROMAIN = re.compile(r'^\s*(?:[IVXLC]+|[A-H])\s*(?:\.|\s–|\s-)\s')
M_DEGRE = re.compile(r'^\s*\d+°\s*(?:bis|ter|quater)?\s')
M_LETTRE = re.compile(r'^\s*[a-z]{1,2}\s*\)\s')
M_TIRET = re.compile(r'^\s*[–-]\s')

CONTINUATION = 9


def niveau(texte):
    """Le niveau de l'alinéa dans l'arbre de la disposition."""
    t = texte.lstrip()
    if t.startswith('«'):
        return CONTINUATION
    if M_ROMAIN.match(t):
        return 0
    if M_DEGRE.match(t):
        return 1
    if M_LETTRE.match(t):
        return 2
    if M_TIRET.match(t):
        return 3
    return CONTINUATION


def ouvre_un_bloc(texte):
    """Un alinéa qui annonce ce qui suit se termine par un deux-points.

    On lit le dernier caractère significatif, hors guillemet fermant : « ainsi
    rédigé : » et « ainsi modifié : » finissent tous deux par le même signe, et
    c'est ce signe qui fait le chapeau, non la formule.
    """
    return texte.rstrip().rstrip('»').rstrip().endswith(':')


def bloc_pour(alineas, index):
    """Les alinéas du bloc ouvert à `index`. Rend la liste des positions.

    `alineas` est la liste des alinéas de l'article du texte déposé, dans
    l'ordre. Un alinéa qui n'ouvre pas de bloc est un bloc à lui seul.
    """
    tete = alineas[index]['texte']
    if not ouvre_un_bloc(tete):
        return [index]
    n0 = niveau(tete)
    if n0 == CONTINUATION:
        return [index]
    pris = [index]
    for j in range(index + 1, len(alineas)):
        nj = niveau(alineas[j]['texte'])
        if nj != CONTINUATION and nj <= n0:
            break
        pris.append(j)
    return pris


def texte_du_bloc(alineas, positions):
    return '\n'.join(alineas[p]['texte'] for p in positions)
