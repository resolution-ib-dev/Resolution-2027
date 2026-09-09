# -*- coding: utf-8 -*-
"""Pliage et dépliage de la couche technique du coffre.

Le coffre est aussi la vue de l'auteur sur son projet. Y verser vingt-quatre
fichiers de Python et de JSON, c'est lui infliger une liste qu'il ne peut pas
lire et qui masque ses vrais produits. La couche technique se replie donc en
une archive unique et opaque, qu'il n'ouvre jamais et qu'il n'a pas à déplacer,
et que Claude déplie en ouverture de session.

Ce qui reste visible au coffre : le manuscrit, la méthode, les produits, la
carte. Un fichier par chose qu'on peut ouvrir.

  plier    lit les fichiers d'un groupe et écrit son archive
  deplier  lit une archive et réécrit les fichiers à leur chemin

Le format d'archive n'est pas du markdown : il tient à deux lignes de
délimitation improbables dans du code, ce qui vaut mieux qu'une clôture de bloc
qu'un fichier pourrait contenir. Les deux délimiteurs se composent à l'exécution
et n'apparaissent nulle part en clair dans ce fichier, faute de quoi l'archive
qui le contient romprait son propre format.

Usage : python3 coffre.py plier ../methode/index.json ..
        python3 coffre.py deplier ../coffre/coffre.txt ..
"""
import json
import os
import sys

DEBUT = '<' * 10 + ' fichier '
FIN = '>' * 10 + ' fin '

# groupe : (chemin de l'archive au coffre, rangs pliés)
GROUPES = {
    'corpus': ('technique/coffre.txt', ('appareil', 'referentiel')),
}

ENTETE = (
    "Archive technique du chantier Résolution — ne pas ouvrir, ne pas éditer.\n"
    "Écrite et relue par l'appareil. Chaque fichier est encadré par une ligne\n"
    "d'ouverture et une ligne de clôture qui portent son chemin.\n"
    "Le dépliage se fait par : python3 appareil/coffre.py deplier <archive> <racine>\n"
)


def a_plier(index, groupe):
    """Ce que l'archive porte, **lu à l'index et non déduit du rang**.

    Corrigé le 20260903. La sélection se faisait sur le seul rang, quand
    l'index déclare déjà où chaque artefact se lit au coffre : un référentiel
    versé comme document — parce qu'il pèse plus que l'archive entière — s'y
    retrouvait replié **en plus** de son versement propre, et l'archive doublait
    de taille en silence. Le rang borne le groupe, `chemin_coffre` tranche.
    """
    chemin, rangs = GROUPES[groupe]
    return [a for a in index['artefacts']
            if a['rang'] in rangs and a['coffre']
            and a['chemin_coffre'] == chemin]


def plier(chemin_index, racine):
    index = json.load(open(chemin_index, encoding='utf-8'))
    dossier = os.path.join(racine, 'coffre')
    os.makedirs(dossier, exist_ok=True)
    for groupe in GROUPES:
        artefacts = a_plier(index, groupe)
        morceaux = [ENTETE]
        for a in artefacts:
            src = os.path.join(racine, a['chemin'])
            contenu = open(src, encoding='utf-8').read()
            assert DEBUT not in contenu and FIN not in contenu, \
                f"délimiteur présent dans {a['chemin']}"
            morceaux.append(f"\n{DEBUT}{a['chemin']}\n{contenu}"
                            f"\n{FIN}{a['chemin']}\n")
        dst = os.path.join(dossier, os.path.basename(GROUPES[groupe][0]))
        open(dst, 'w', encoding='utf-8').write(''.join(morceaux))
        poids = os.path.getsize(dst)
        print(f'{dst} — {len(artefacts)} fichier(s), {poids} octets')
    return 0


def deplier(chemin_archive, racine):
    texte = open(chemin_archive, encoding='utf-8').read()
    ecrits = []
    i = 0
    while True:
        d = texte.find(DEBUT, i)
        if d < 0:
            break
        fin_ligne = texte.index('\n', d)
        chemin = texte[d + len(DEBUT):fin_ligne].strip()
        marque_fin = f'\n{FIN}{chemin}\n'
        f = texte.index(marque_fin, fin_ligne)
        contenu = texte[fin_ligne + 1:f]
        cible = os.path.join(racine, chemin)
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        open(cible, 'w', encoding='utf-8').write(contenu)
        ecrits.append(chemin)
        i = f + len(marque_fin)
    print(f'{len(ecrits)} fichier(s) dépliés depuis {chemin_archive}')
    for c in ecrits:
        print(f'    {c}')
    return 0 if ecrits else 1


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    mode = sys.argv[1]
    if mode == 'plier':
        sys.exit(plier(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '.'))
    if mode == 'deplier':
        sys.exit(deplier(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '.'))
    print(__doc__)
    sys.exit(2)
