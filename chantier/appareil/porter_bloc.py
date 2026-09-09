# -*- coding: utf-8 -*-
"""Insertion d'un bloc en tête du registre ou du journal, par copie d'octets.

Le registre des arbitrages porte près de deux cent mille octets, le journal
cent mille. Les réécrire à travers le modèle pour y ajouter un bloc ferait passer
tout le reste par une recopie — c'est exactement ce qui a produit, le 20260824,
des règles de rédaction réécrites en silence (A-38). Les deux s'ouvrent donc par
script : l'ancien texte n'est jamais relu, il est découpé une fois et recollé à
l'octet.

Les deux documents ont la même forme — une préface, un séparateur, puis les blocs
du plus récent au plus ancien. Le script sert l'un comme l'autre.

Le bloc neuf est lu depuis un fichier séparé, écrit à la main. Le script ne
compose rien : il place.

Deux gardes, et elles ne se contournent pas.

  - **Le point d'insertion est nommé, pas deviné.** Le bloc entre juste après le
    premier séparateur de tête, celui qui clôt la préface du registre. Si ce
    séparateur ne se trouve pas là où il est attendu, le script s'arrête.
  - **Rien ne se perd.** Les octets d'avant et d'après l'insertion sont
    comparés à l'original : leur concaténation doit redonner le fichier reçu.

Usage : python3 porter_bloc.py ../methode/arbitrages.md ../bloc.md
        python3 porter_bloc.py ../methode/journal.md ../bloc.md
        python3 porter_bloc.py <cible> <bloc> <ancre littérale>
"""
import os
import sys

# Fin de la préface : la ligne de séparation qui précède le bloc le plus récent.
# Le fil courant n'a pas cette forme — sa préface est son titre — et l'ancre se
# passe alors en argument. Elle est toujours nommée, jamais devinée.
SEPARATEUR = '\n---\n\n'


def porter(chemin_cible, chemin_bloc, ancre=SEPARATEUR):
    ancien = open(chemin_cible, encoding='utf-8', newline='').read()
    bloc = open(chemin_bloc, encoding='utf-8', newline='').read().strip('\n')

    coupe = ancien.find(ancre)
    if coupe < 0:
        print('ancre de préface introuvable — rien n\'est écrit')
        return 1
    tete = ancien[:coupe + len(ancre)]
    reste = ancien[coupe + len(ancre):]

    if tete + reste != ancien:
        print('découpe non conservative — rien n\'est écrit')
        return 1
    if bloc in reste:
        print('bloc déjà porté — rien n\'est écrit')
        return 1

    neuf = tete + bloc + '\n\n' + reste
    # Le registre neuf doit contenir l'ancien à l'octet près, en deux morceaux.
    assert neuf.startswith(tete) and neuf.endswith(reste), 'recollage rompu'

    open(chemin_cible, 'w', encoding='utf-8', newline='').write(neuf)
    print(f'{chemin_cible} — {len(ancien.encode())} o avant, '
          f'{os.path.getsize(chemin_cible)} o après, '
          f'{len(bloc.encode())} o portés')
    return 0


if __name__ == '__main__':
    sys.exit(porter(sys.argv[1], sys.argv[2],
                    sys.argv[3] if len(sys.argv) > 3 else SEPARATEUR))
