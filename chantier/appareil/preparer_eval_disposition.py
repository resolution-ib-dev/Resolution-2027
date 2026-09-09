# -*- coding: utf-8 -*-
"""Le banc de l'éval de la rédaction cible — deux fichiers, et l'aveuglement.

L'éval se joue à trois fils qui ne voient pas la même chose, et ce script écrit
ce que chacun reçoit. **L'aveuglement se tient par la donnée d'entrée, jamais
par la discipline d'un fil** : un fil qui a vu la disposition de
l'administration ne peut plus juger ce qu'une skill en rend.

    terrain.json   ce que voit le fil qui rédige les énoncés — le bloc de
                   disposition tel que l'administration l'a écrit
    enonces.json   ce que voit le fil qui joue la skill — l'énoncé en langage
                   naturel, le véhicule, l'adresse d'article, rien d'autre

Le second se remplit à la main par le fil rédacteur ; ce script en pose le
gabarit, une entrée par cas, pour qu'aucun cas ne se perde et qu'aucun champ ne
s'invente.

**L'adresse est donnée, et ce n'est pas une facilité.** Le contrat de la chaîne
fait recevoir à E4 les sorties d'E2 et d'E3 : trouver le siège est le travail
d'une autre étape, déjà éprouvée. Ce qui se mesure ici est ce qu'E4 fait d'une
adresse qu'elle reçoit — la décomposer sans la recoller, choisir l'opération,
tenir la portée.

Usage : python3 preparer_eval_disposition.py ../referentiels/redaction_plf.json \\
                ../eval/echantillon.json \\
                ../eval
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from blocs_disposition import bloc_pour, texte_du_bloc
import partage_calibrage as pc

# La date à laquelle la colonne A se lit. Le millésime de l'extrait de droit est
# postérieur à l'entrée en vigueur du texte : lu au jour courant, un article que
# la loi adoptée a touché porte le résultat et non le point de départ.
DATE_DEPOT = '2025-10-01'


def operations_du_bloc(texte):
    """Les opérations que le bloc porte, relevées ligne à ligne.

    La vérité-terrain de la notation. On relève par ligne et non sur le bloc
    entier : un chapeau et ses subordonnés portent plusieurs opérations, et
    c'est le cas dur du contrat.
    """
    ops, portees = [], []
    for ligne in texte.split('\n'):
        op, _ = pc.operation(ligne)
        if op:
            ops.append(op)
            portees.append(pc.cible(ligne))
    return ops, portees


def main(src_red, src_ech, dst_dir):
    red = json.load(open(src_red, encoding='utf-8'))
    ech = json.load(open(src_ech, encoding='utf-8'))
    arts = {a['numero']: a for a in red['articles']}

    terrain, gabarit = [], []
    for c in ech['cas']:
        a = arts[c['article_texte_depose']]
        idx = next(i for i, al in enumerate(a['alineas'])
                   if al['numero'] == c['alinea'])
        pos = bloc_pour(a['alineas'], idx)
        txt = texte_du_bloc(a['alineas'], pos)
        ops, portees = operations_du_bloc(txt)
        refs = c['terrain']['references']
        terrain.append({
            'cle': c['cle'],
            'strate_du_couple': c['strate'],
            'article_texte_depose': c['article_texte_depose'],
            'alinea_chapeau': c['alinea'],
            'alineas': [a['alineas'][p]['numero'] for p in pos],
            'nb_alineas': len(pos),
            'disposition_administration': txt,
            'adresses': refs,
            'operations_terrain': ops,
            'portees_terrain': portees,
        })
        gabarit.append({
            'cle': c['cle'],
            'vehicule': 'plf',
            'adresse_donnee': [{'texte': r['texte'], 'article': r['brut']}
                               for r in refs],
            'date_de_lecture_du_droit': DATE_DEPOT,
            'enonce': None,
        })

    os.makedirs(dst_dir, exist_ok=True)
    for nom, contenu, regle in (
            ('terrain.json', terrain,
             "La disposition telle que l'administration l'a écrite. Vérité-"
             "terrain de la notation. Un fil qui a lu ce fichier ne peut plus "
             "jouer la skill ni la noter."),
            ('enonces.json', gabarit,
             "Ce que reçoit le fil qui joue la skill. `enonce` se remplit par "
             "le fil rédacteur, selon la règle de "
             "`methode/regle_enonces_eval.md`. Aucun autre champ ne s'ajoute.")):
        with open(os.path.join(dst_dir, nom), 'w',
                  encoding='utf-8', newline='') as f:
            json.dump({'_regle': regle, 'cas': contenu}, f,
                      ensure_ascii=False, indent=1)
            f.write('\n')

    n_multi = sum(1 for t in terrain if t['nb_alineas'] > 1)
    n_ops = sum(len(t['operations_terrain']) for t in terrain)
    print(f'{len(terrain)} cas — {n_multi} bloc(s) de plus d\'un alinéa, '
          f'{n_ops} opération(s) au terrain')
    print(f'{dst_dir}/terrain.json et {dst_dir}/enonces.json écrits')
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    sys.exit(main(a[0], a[1], a[2]))
