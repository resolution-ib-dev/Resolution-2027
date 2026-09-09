# -*- coding: utf-8 -*-
"""Contrôle du coffre et des renvois.

Il remplace l'ancien contrôle du montage projet, qui vérifiait un inventaire à
rang horodaté. L'objet a changé : ce n'est plus un montage qu'on vérifie, c'est
la concordance entre trois choses — l'arborescence du dépôt, l'index de
résolution, et la règle de nommage canonique.

Cinq vérifications. Aucune ne produit quoi que ce soit.

  I1  tout chemin de l'index existe au dépôt
  I2  tout fichier du dépôt figure à l'index
  I3  aucun nom horodaté `_AAAAMMJJ_vN` ne subsiste hors de `sources/`
  I4  aucun alias n'est revendiqué par deux artefacts
  I5  tout artefact déclaré porte une famille du classement par contenu

`sources/` est une archive : un document y est daté par nature, et son nom porte
le millésime de ce qu'il décompte ou de ce qu'il gelait. La règle canonique vaut
pour le corpus vivant, pas pour ce qui est figé.

I1 et I2 échouent : un renvoi qui ne résout pas, ou un fichier que personne ne
déclare, sont l'un et l'autre des trous. I3 et I4 échouent aussi : le premier
fait revenir la maladie qu'on vient de soigner, le second rend la résolution
ambiguë. I5 échoue parce qu'un artefact hors classement est un artefact qu'on
retrouvera par hasard.

Ce que l'index déclare non restaurable ne sort pas en I1 — pièces jointes du
projet, documents binaires que le coffre porte comme documents. Leur absence du
conteneur se constate et se dit, elle ne se corrige pas.

Les manquants déclarés à l'index ne sortent pas en I1 : ils sont connus, nommés,
et leur absence est documentée. Ils se rappellent en fin de sortie.

Usage : python3 controle_index.py methode/index.json .
"""
import json
import os
import re
import sys

HORODATE = re.compile(r'_\d{8}_v\d+(\.|$)')
# `coffre/` est un répertoire de construction : les archives s'y replient par
# `make coffre` et n'ont pas d'histoire.
# `sources/plf` est un cache de conversion : les classeurs sectoriels sont des
# pièces jointes du projet, et leur version convertie en xlsx ne s'y déclare pas.
# `droit` est le dépôt de droit, cloné par le fil pour lire le texte en
# vigueur. Ses quinze fichiers vivent à leur dépôt et ne se déclarent pas
# (`reference/depot_droit.md`) ; sans cette exclusion, suivre la procédure
# qu'écrit le corpus faisait sortir I2 à 15.
# `eval` est l'atelier des évaluations : le terrain, l'échantillon et les
# réponses brutes des fils joueurs. Ils se refont en rejouant l'éval — sauf les
# réponses, qui ne se refont pas à l'identique et dont le relevé condensé, lui,
# est versé. Rien de tout cela n'a de place au coffre ni à l'index.
# `machine` et `skills_maj` sont des ateliers de fil : le premier porte les
# **projections** destinées au projet dédié — le point de vérité de chaque pièce
# projetée est son original au coffre —, le second les copies de travail des
# skills, dont le point de vérité est la skill enregistrée. Ni l'un ni l'autre
# ne se verse.
# Les répertoires du conteneur, quand la racine du dépôt **est** le répertoire
# personnel de la session. C'était le cas le 20260909, et `I2` sortait à
# 29 297 : 29 295 fichiers de cache d'outils, deux du corpus. Un contrôle qui
# crie 29 297 fois ne sert plus à rien, et c'est A-337 à l'identique — la
# procédure que le corpus prescrit cassait un contrôle que le corpus tient.
# Aucun de ces chemins n'est un artefact, et aucun ne le deviendra.
CONTENEUR = {'.cache', '.npm', '.npm-global', '.config', '.ssh', '.local',
             '.cargo', '.venv', '.ipython', '.gitconfig', '.wget-hsts',
             '.bash_history', '.python_history', '.profile', '.bashrc'}
IGNORES = {'.git', '__pycache__', '.claude', 'node_modules', 'coffre',
           'plf', 'plfss', 'droit', 'eval', 'machine', 'skills_maj',
           'epreuve'} | CONTENEUR
# Dérivé exclu du suivi git par `.gitignore`, et à ce titre non déclaré.
TOLERES = set()
# Ce que le classement laisse délibérément dehors. **La liste ne se redouble
# pas ici** : elle est lue dans `generer_carte.HORS_FAMILLE`, qui est le lieu
# unique de l'affectation (A-25). Un doublon, c'était l'anomalie I5 qui sortait
# à chaque exécution sur la feuille de route.
try:
    from generer_carte import HORS_FAMILLE as HORS_CLASSEMENT
except ImportError:  # pragma: no cover
    HORS_CLASSEMENT = {'livrables/carte_du_projet.html'}


# Un dossier rendu en bloc : un seul de ses fichiers se déclare, et il vaut
# pour le dossier entier. Les vingt pages du site et sa feuille de style ne sont
# pas des artefacts — elles sont le rendu d'un artefact, elles n'ont ni nom
# canonique ni histoire propre, et `generer_site.py` les refait toutes ensemble.
# Déclarer vingt et un chemins pour une pièce qui se régénère en un geste
# gonflerait l'index sans rien y ajouter.
BLOCS = {'site': {'site/index.html', 'site/manifeste.html'}}


def fichiers(racine):
    trouves = []
    for base, dossiers, noms in os.walk(racine):
        dossiers[:] = [d for d in dossiers if d not in IGNORES]
        for n in noms:
            chemin = os.path.relpath(os.path.join(base, n), racine)
            if any(p in IGNORES for p in chemin.split(os.sep)):
                continue
            chemin = chemin.replace(os.sep, '/')
            tete = chemin.split('/', 1)[0]
            if tete in BLOCS and chemin not in BLOCS[tete]:
                continue
            trouves.append(chemin)
    return sorted(trouves)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    chemin_index = argv[1]
    racine = argv[2] if len(argv) > 2 else '.'

    index = json.load(open(chemin_index, encoding='utf-8'))
    artefacts = index['artefacts']
    declares = {a['chemin']: a for a in artefacts}
    presents = set(fichiers(racine))

    # I1 — un renvoi de l'index qui ne résout pas.
    # Ce que l'index déclare non restaurable en sort : une pièce jointe du
    # projet, ou un document binaire que le coffre porte comme document et non
    # comme octets. Le réécrire au dépôt supposerait de le recomposer par le
    # modèle, donc de fabriquer un faux. Son absence du conteneur est une
    # constatation ; son absence du projet se voit à l'œil et se dit à
    # l'ouverture de session.
    # Un fil ne déplie que ce dont il a besoin. Un chemin absent du dépôt mais
    # dont `methode/empreintes.json` porte l'empreinte n'est pas un trou : le
    # coffre le tient, ce fil ne l'a pas demandé. Le confondre avec un vrai
    # manquant ferait crier le contrôle à chaque fil partiel, et un contrôle qui
    # crie toujours ne sert plus à rien.
    try:
        connus = set(json.load(open(os.path.join(racine, 'methode',
                                                 'empreintes.json'),
                                    encoding='utf-8'))['empreintes'])
    except (OSError, json.JSONDecodeError, KeyError):
        connus = set()
    absents = sorted(c for c in declares if c not in presents
                     and declares[c].get('restaurable', True)
                     and c not in connus)
    non_deplies = sorted(c for c in declares if c not in presents
                         and declares[c].get('restaurable', True)
                         and c in connus)
    hors_atelier = sorted(c for c in declares if c not in presents
                          and not declares[c].get('restaurable', True))

    # I2 — un fichier que l'index ne déclare pas.
    # Le bloc `archives` a disparu le 20260909 avec l'archive qu'il décrivait
    # (A-395) : il fallait en exclure `technique/coffre.txt`, qui n'était pas un
    # artefact mais en contenait quatre-vingts. Chacun se déclare aujourd'hui.
    non_declares = sorted(c for c in presents
                          if c not in declares and c not in TOLERES)

    # I3 — un nom horodaté survivant, hors archive
    horodates = sorted(c for c in presents
                       if not c.startswith('sources/')
                       and HORODATE.search(os.path.basename(c)))

    # I4 — un alias revendiqué deux fois
    proprietaire = {}
    doubles = []
    for a in artefacts:
        for al in a.get('alias', []):
            if al in proprietaire and proprietaire[al] != a['role']:
                doubles.append((al, proprietaire[al], a['role']))
            else:
                proprietaire[al] = a['role']

    print(f"{len(presents)} fichier(s) au dépôt, {len(declares)} chemin(s) à "
          f"l'index, {len(proprietaire)} alias résolus")

    print(f"\nI1 — {len(absents)} chemin(s) déclaré(s) mais absent(s) du dépôt")
    for c in absents:
        print(f"    {c}")

    print(f"\nNon déplié — {len(non_deplies)} document(s) que le coffre tient et "
          f"que ce fil n'a pas demandé")
    for c in non_deplies:
        print(f"    {c}")

    print(f"\nHors atelier — {len(hors_atelier)} document(s) déclaré(s) que "
          f"nul script ne restaure")
    for c in hors_atelier:
        print(f"    {c}")

    print(f"\nI2 — {len(non_declares)} fichier(s) du dépôt non déclaré(s) à l'index")
    for c in non_declares:
        print(f"    {c}")
    if non_declares:
        print("    → les porter à la table de generer_index.py, ou les retirer.")

    print(f"\nI3 — {len(horodates)} nom(s) horodaté(s) subsistant hors archive")
    for c in horodates:
        print(f"    {c}")
    if horodates:
        print("    → renommer au nom canonique : l'historique vit dans git.")

    print(f"\nI4 — {len(doubles)} alias revendiqué(s) deux fois")
    for al, r1, r2 in doubles:
        print(f"    {al} : {r1} et {r2}")

    # I5 — un artefact que le classement par contenu ne range nulle part.
    # La carte est la seule exception : elle est la vue, non une pièce de ce
    # qu'elle range.
    sans_famille = sorted(a['chemin'] for a in artefacts
                          if not a.get('famille')
                          and a['chemin'] not in HORS_CLASSEMENT)
    print(f"\nI5 — {len(sans_famille)} artefact(s) sans famille")
    for c in sans_famille:
        print(f"    {c}")
    if sans_famille:
        print("    → leur donner une ligne de carte dans generer_carte.py.")

    # I6 — le coffre porte une pièce que l'index ne déclare pas.
    # C'est la faute qui a coûté le plus cher au 20260902 : quatorze documents
    # au coffre, hors index, dont deux portaient le travail qu'un fil réclamait
    # en pièce jointe. Un document qu'aucune table ne déclare n'est pas perdu :
    # il est invisible, ce qui est pire, parce qu'on conclut sans lui.
    #
    # L'inventaire se relève à `project_info` en ouverture et ne se verse pas —
    # c'est une photo de session. Sans lui, le contrôle le dit et ne bloque pas.
    inv = os.path.join(racine, 'methode', 'inventaire_coffre.tsv')
    # Seule la voie `coffre` a un chemin au coffre : ce qui vient du dépôt n'y
    # est plus, et l'y chercher ferait sortir quatre-vingts pièces en I6.
    declares = {a.get('chemin_coffre') for a in artefacts
                if a['coffre'] and a.get('voie', 'coffre') != 'depot'}
    muets = []
    if os.path.isfile(inv):
        porte = []
        for ligne in open(inv, encoding='utf-8'):
            ligne = ligne.rstrip('\n')
            if not ligne or ligne.startswith('#') or ligne.startswith('chemin_coffre'):
                continue
            porte.append(ligne.split('\t')[0])
        muets = sorted(set(porte) - declares)
        print(f"\nI6 — {len(muets)} pièce(s) au coffre non déclarée(s) à l'index")
        for c in muets:
            print(f"    {c}")
        if muets:
            print("    → les ouvrir avant de conclure sur ce que le corpus porte.")
    else:
        print("\nI6 — inventaire du coffre absent, non contrôlé")

    manquants = index.get('manquants', [])
    print(f"\nManquants déclarés — {len(manquants)}, absence documentée")
    for m in manquants:
        print(f"    {m['role']} → {m['chemin_attendu']}")
        print(f"        attendu par {', '.join(m['attendu_par'])}")

    # `I1` ne compte pas parmi les échecs, et A-338 le pose depuis le 20260902 :
    # il mesure ce qu'un fil a régénéré, pas ce que le corpus porte, et sa valeur
    # ne se compare qu'à périmètre identique. Le compter faisait sortir en erreur
    # tout fil qui ne déplie qu'une partie du coffre — c'est-à-dire tous. La
    # règle était au registre et pas dans le code : c'est A-349, encore.
    echecs = (len(non_declares) + len(horodates) + len(doubles)
              + len(sans_famille) + len(muets))
    print(f"\n{echecs} anomalie(s) bloquante(s), {len(absents)} dérivé(s) non "
          f"régénéré(s) — hors compte —, {len(manquants)} manquant(s) déclaré(s)")
    return 1 if echecs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
