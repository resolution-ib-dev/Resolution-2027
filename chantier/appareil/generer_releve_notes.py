# -*- coding: utf-8 -*-
"""Relevé lisible des notes de fin du manuscrit.

Le relevé est un dérivé : il ne se corrige jamais à la main, il se régénère
depuis `referentiels/notes_manuscrit.json`. Il sert à la lecture humaine et au
repérage à l'œil des notes chiffrées qu'aucun référentiel ne cite ; le compte
opposable, lui, est tenu par `controle_notes.py`.

Une ligne par note : identifiant, section d'ancrage tronquée, texte tronqué.
Les deux troncatures sont volontaires — le relevé donne à reconnaître, pas à
citer. Toute citation se prend au manuscrit.

Usage : python3 generer_releve_notes.py ../referentiels/notes_manuscrit.json ../livrables/notes_manuscrit_releve.txt
"""
import json
import sys

SECTION = 44   # largeur de la colonne de section
TEXTE = 290    # largeur du texte donné à reconnaître


def generer(src, dst):
    d = json.load(open(src, encoding='utf-8'))
    notes = d['notes']
    lignes = [f'{len(notes)} notes', '']
    for n in notes:
        lignes.append(f'{n["id"]} [{n["section"][:SECTION]}] {n["texte"][:TEXTE]}')
    open(dst, 'w', encoding='utf-8').write('\n'.join(lignes) + '\n')
    chiffrees = sum(1 for n in notes if n.get('porte_un_chiffre'))
    print(f'{dst} écrit — {len(notes)} notes, dont {chiffrees} chiffrée(s)')
    return 0


if __name__ == '__main__':
    sys.exit(generer(sys.argv[1], sys.argv[2]))
