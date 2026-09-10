# -*- coding: utf-8 -*-
"""Empreintes des artefacts versés au coffre.

Le coffre rend ses documents lisibles **en texte**, jamais en octets : seule une
archive assez volumineuse revient au dépôt comme fichier. Tout le reste — le
manuscrit, la méthode, les textes normatifs — repasse par le modèle à la
restauration, et une recopie normalise sans le dire. Le 20260824, une
restauration a rendu le manuscrit en squelette de 607 octets et l'index avec ses
retours ligne échappés en clair. Aucune des deux n'a été vue par un contrôle :
l'une a été trouvée à la taille, l'autre parce que le JSON ne se chargeait plus.

La règle « toute pièce restaurée se compare à l'octet avant emploi » était donc
inapplicable, faute de référence à quoi comparer. Ce fichier la rend applicable.

**Au versement**, on relève pour chaque artefact du coffre son empreinte
SHA-256, sa taille en octets et son compte de lignes, et on les écrit dans
`methode/empreintes.json`, qui part au coffre avec le reste.

**À la restauration**, `controle_restauration.py` recalcule et compare. Une
divergence est une anomalie bloquante : le fichier restauré est un faux, et il
ne s'emploie pas.

Le fichier d'empreintes est lui-même restauré par le modèle, donc corruptible.
Ce n'est pas un défaut : il ne porte aucun verbatim, et sa corruption se voit —
soit le JSON ne charge plus, soit toutes les empreintes divergent d'un coup, ce
qui ne ressemble pas à une dérive de recopie sur un fichier isolé.

Usage : python3 empreintes.py ../methode/index.json .. [clone du dépôt]
"""
import hashlib
import json
import os
import sys

# Une empreinte par artefact, à son propre chemin, et rien d'autre. Jusqu'au
# 20260909, l'archive technique en portait une de plus, la sienne, relevée à
# `coffre/coffre.txt` : c'était l'archive qui faisait l'aller-retour au coffre,
# et le fichier n'était relevé qu'en second pour prouver le dépliage. L'archive
# est au dépôt et supprimée du coffre (A-395) : les quatre-vingts fichiers
# qu'elle portait se relèvent chacun pour soi, ce qui est plus précis — une
# divergence nomme désormais son fichier au lieu de nommer l'archive entière.


def relever(chemin):
    """Empreinte d'un fichier : sha256, octets, lignes. None s'il est absent."""
    if not os.path.isfile(chemin):
        return None
    octets = open(chemin, 'rb').read()
    return {'sha256': hashlib.sha256(octets).hexdigest(),
            'octets': len(octets),
            'lignes': octets.count(b'\n')}


def generer(chemin_index, racine, clone=None):
    """Relève les empreintes de ce que les deux surfaces portent **durablement**.

    **Une empreinte ne décrit jamais un état qu'aucune surface ne porte**, et
    c'est la règle qui manquait le 20260909. Un fil Cowork qui corrige une pièce
    de l'appareil **ne peut pas la pousser** — l'écriture au dépôt est fermée
    (A-393) —, et relever son empreinte au dépôt courant écrivait au coffre la
    référence d'un fichier qui ne vit que dans un conteneur éphémère. Toute
    restauration à blanc ultérieure en sortait un `R1` qui n'était pas un faux :
    c'est A-392 par l'autre bout, où un dérivé versé qu'aucun fil ne reverse
    faisait mentir le coffre.

    Donc, pour un artefact de voie `depot` : l'empreinte se relève **au clone**,
    qui est ce que la session suivante recevra. Sans clone, elle ne se touche
    pas — l'ancienne vaut, et `coffre.py dette` porte l'écart. Pour la voie
    `coffre`, elle se relève au dépôt courant, qui est ce que le fil verse.
    """
    index = json.load(open(chemin_index, encoding='utf-8'))
    dst = os.path.join(racine, 'methode', 'empreintes.json')
    sous = (index.get('depot') or {}).get('sous_racine', 'chantier')

    # Le relevé est **cumulatif**. Un fil ne déplie que ce dont il a besoin :
    # s'il écrasait le fichier, il effacerait l'empreinte de tout ce qu'il n'a
    # pas restauré, et la session suivante croirait le coffre vide de ces
    # documents. Une session ne détruit pas ce qu'elle n'a pas vu.
    try:
        empreintes = json.load(open(dst, encoding='utf-8'))['empreintes']
    except (OSError, json.JSONDecodeError, KeyError):
        empreintes = {}

    absents, hors_clone = [], []
    for a in index['artefacts']:
        if not a['coffre'] or not a['restaurable']:
            continue
        # Le fichier d'empreintes ne porte pas la sienne : elle changerait en
        # l'écrivant.
        if a['chemin'] == 'methode/empreintes.json':
            continue
        if a.get('voie') == 'depot':
            if clone is None:
                hors_clone.append(a['chemin'])
                continue
            e = relever(os.path.join(clone, sous, a['chemin']))
        else:
            e = relever(os.path.join(racine, a['chemin']))
        if e is None:
            if a['chemin'] not in empreintes:
                absents.append(a['chemin'])
            continue
        empreintes[a['chemin']] = e

    # Cumulatif ne veut pas dire éternel. Une empreinte dont l'index ne déclare
    # plus le chemin est celle d'un artefact renommé ou mort : la garder ferait
    # croire que le coffre porte une pièce qui n'y est plus, et le compte des
    # empreintes de référence enflerait à chaque renommage. Le retrait se fait
    # sur ce que l'index déclare, jamais sur ce qui est présent au dépôt : un
    # fil qui n'a pas restauré un document ne l'efface pas pour autant.
    declares = {a['chemin'] for a in index['artefacts']
                if a['coffre'] and a['restaurable']}
    declares.add('methode/empreintes.json')
    perimees = sorted(set(empreintes) - declares)
    for c in perimees:
        del empreintes[c]

    sortie = {'_regle': "Empreintes relevées au versement, cumulatives : une "
                        "session n'efface pas celles des documents qu'elle n'a "
                        "pas dépliés. Toute pièce restaurée du coffre se compare "
                        "ici avant emploi. Une divergence est un faux, elle ne "
                        "se corrige pas au dépôt : elle se redemande au coffre.",
              'sans_empreinte': sorted(absents),
              'empreintes': dict(sorted(empreintes.items()))}
    with open(dst, 'w', encoding='utf-8') as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print(f'{dst} écrit — {len(empreintes)} empreinte(s), '
          f'{len(absents)} artefact(s) encore sans empreinte, '
          f'{len(perimees)} empreinte(s) périmée(s) retirée(s)')
    if hors_clone:
        print(f'    {len(hors_clone)} artefact(s) de voie `depot` non relevé(s), '
              f'faute de clone : leur empreinte d\'avant vaut.')
    for c in sorted(absents):
        print(f'    sans empreinte — {c}')
    for c in perimees:
        print(f'    périmée, plus déclarée à l\'index — {c}')
    return 0


if __name__ == '__main__':
    sys.exit(generer(sys.argv[1],
                     sys.argv[2] if len(sys.argv) > 2 else '.',
                     sys.argv[3] if len(sys.argv) > 3 else None))
