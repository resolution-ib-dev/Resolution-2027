# -*- coding: utf-8 -*-
"""Contrôle du balayage des générateurs — `V1` à `V5`.

Le corpus contrôlait ce qu'il portait, jamais qu'il savait encore le refaire.
Deux générateurs du coffre ont été trouvés cassés **par hasard** : la carte du
projet, qui levait depuis deux jours sur un chemin renommé (A-364), et l'état de
la machine, qui ne se refaisait plus depuis que le banc écrit ses mesures de deux
façons. Dans les deux cas, `controle_index` comptait les chemins et ne jouait
rien : il ne voit pas les renvois qu'un générateur porte dans son propre code.

**Une page qui ne se régénère plus vieillit en silence**, et c'est le pire des
états — elle a l'air d'un dérivé, elle est devenue une pièce à la main.

Le balayage joue chaque générateur **par la règle du fichier de construction**,
jamais par un appel direct : c'est A-343 pour la reproductibilité, et A-382 pour
l'écrasement — la règle porte l'ordre des arguments, et un générateur appelé à la
main avec une source en premier a déjà détruit un référentiel.

Cinq verdicts, deux rangs.

  V1  échec        le générateur lève. C'est un défaut, et il bloque.
  V2  sans règle   l'index déclare un producteur, le Makefile n'a pas de cible.
                   Le générateur ne se rejoue jamais : il bloque aussi.
  V3  cible volée  deux artefacts se produisent par la même cible make — une
                   variable affectée deux fois. La seconde règle gagne, la
                   première ne se joue plus. Elle bloque.
  V4  non produit  la règle a tourné sans écrire : elle est gardée par la
                   présence d'un intrant qui n'est pas là. Ce n'est pas un
                   défaut, cela se dit.
  V5  a bougé      le dérivé refait diffère de celui qu'on avait. Ce n'est pas
                   un défaut non plus : c'est ce qu'il faut reverser.

Le balayage **écrit au dépôt** — il régénère pour de vrai, faute de quoi il ne
prouve rien. Il relève l'empreinte d'avant pour dire ce qui a bougé.

Usage : python3 controle_generateurs.py ../methode/index.json ..
"""
import hashlib
import json
import os
import re
import subprocess
import sys

DELAI = 300


def empreinte(chemin):
    if not os.path.isfile(chemin):
        return None
    h = hashlib.sha256()
    with open(chemin, 'rb') as f:
        for bloc in iter(lambda: f.read(65536), b''):
            h.update(bloc)
    return h.hexdigest()


def variables_doublees(racine):
    """Variables du Makefile affectées deux fois — la seconde vole la cible."""
    chemin = os.path.join(racine, 'Makefile')
    if not os.path.isfile(chemin):
        return {}
    vues = {}
    for ligne in open(chemin, encoding='utf-8'):
        m = re.match(r'^([A-Z_][A-Z0-9_]*)\s*:?=\s*(.*)$', ligne)
        if m:
            vues.setdefault(m.group(1), []).append(m.group(2).strip())
    return {k: v for k, v in vues.items() if len(v) > 1}


def cibles_doublees(racine):
    """Chemins de sortie qu'au moins deux règles prétendent produire."""
    chemin = os.path.join(racine, 'Makefile')
    if not os.path.isfile(chemin):
        return {}
    # Les cibles s'écrivent en variables ; on les résout par `make` lui-même
    # plutôt que de réimplémenter son expansion.
    regles = {}
    for ligne in open(chemin, encoding='utf-8'):
        m = re.match(r'^(\$\([A-Z_][A-Z0-9_]*\)):', ligne)
        if m:
            regles.setdefault(m.group(1), 0)
            regles[m.group(1)] += 1
    return {k: n for k, n in regles.items() if n > 1}


def cibles_declarees(racine):
    """Les chemins que le fichier de construction déclare comme cibles.

    Y compris sous une garde `ifneq` inactive. C'est ce qui sépare une règle
    **absente** — le générateur ne se rejoue jamais, et c'est un défaut — d'une
    règle **conditionnelle** que l'atelier n'active pas, faute de la pièce
    jointe dont elle dérive. `make` rend le même message pour les deux.
    """
    chemin = os.path.join(racine, 'Makefile')
    if not os.path.isfile(chemin):
        return set()
    vars_, cibles = {}, set()

    def resoudre(texte):
        for _ in range(8):
            avant = texte
            texte = re.sub(r'\$\(([A-Z_][A-Z0-9_]*)\)',
                           lambda m: vars_.get(m.group(1), ''), texte)
            if texte == avant:
                break
        return texte

    for ligne in open(chemin, encoding='utf-8'):
        m = re.match(r'^([A-Z_][A-Z0-9_]*)\s*:?=\s*(.*)$', ligne)
        if m:
            vars_[m.group(1)] = resoudre(m.group(2).strip())
            continue
        m = re.match(r'^([^\s:#][^:=]*):(?!=)', ligne)
        if m:
            for mot in resoudre(m.group(1)).split():
                if '/' in mot:
                    cibles.add(mot)
    return cibles


def jouer(cible, racine):
    """`make --always-make <cible>`. Rend (code, sortie)."""
    try:
        p = subprocess.run(['make', '--always-make', cible],
                           cwd=racine, capture_output=True, text=True,
                           timeout=DELAI)
        return p.returncode, (p.stdout + p.stderr)
    except subprocess.TimeoutExpired:
        return 124, f'dépassement de {DELAI} s'
    except OSError as e:
        return 127, str(e)


SANS_REGLE = re.compile(r"No rule to make target ['`]([^'`]+)'"
                        r"|pas de règle pour fabriquer « ([^»]+) »")


def cible_sans_regle(sortie):
    """Le chemin que `make` dit ne pas savoir fabriquer, ou None.

    Le même message vaut pour deux situations qui ne se traitent pas pareil :
    la cible demandée n'a pas de règle — le générateur ne se rejoue jamais —,
    ou c'est **un de ses prérequis** qui n'en a pas, parce qu'il se dérive
    d'une pièce jointe absente de l'atelier. La seconde n'est pas un défaut.
    """
    m = SANS_REGLE.search(sortie)
    if not m:
        return None
    return m.group(1) or m.group(2)


def controler(chemin_index, racine='.'):
    index = json.load(open(chemin_index, encoding='utf-8'))
    produits = [a for a in index['artefacts']
                if a.get('produit_par') and a.get('chemin')]

    # V3 se relève sur le fichier de construction, avant de jouer quoi que ce
    # soit : une cible volée ne se voit pas à l'exécution, la règle perdante
    # n'étant jamais atteinte.
    doubles_var = variables_doublees(racine)
    doubles_cible = cibles_doublees(racine)
    declarees = cibles_declarees(racine)

    avant = {a['chemin']: empreinte(os.path.join(racine, a['chemin']))
             for a in produits}

    echecs, sans_regle, non_produits, bouges, ok = [], [], [], [], []
    for a in produits:
        code, sortie = jouer(a['chemin'], racine)
        if code != 0:
            orpheline = cible_sans_regle(sortie)
            if orpheline == a['chemin']:
                if a['chemin'] in declarees:
                    non_produits.append(
                        (a['chemin'], a['produit_par'],
                         'règle conditionnelle inactive — pièce jointe absente'))
                else:
                    sans_regle.append((a['chemin'], a['produit_par']))
            elif orpheline:
                non_produits.append((a['chemin'], a['produit_par'],
                                     f'prérequis sans règle — {orpheline}'))
            else:
                manque = re.search(r"No such file or directory: '\.\./([^']+)'",
                                   sortie)
                if manque:
                    non_produits.append((a['chemin'], a['produit_par'],
                                         f'intrant absent — {manque.group(1)}'))
                else:
                    derniere = [l for l in sortie.strip().split('\n') if l.strip()]
                    echecs.append((a['chemin'], a['produit_par'],
                                   derniere[-1][:200] if derniere else ''))
            continue
        apres = empreinte(os.path.join(racine, a['chemin']))
        if apres is None:
            non_produits.append((a['chemin'], a['produit_par'],
                                 'règle gardée, rien écrit'))
        elif avant[a['chemin']] is None:
            ok.append(a['chemin'])
        elif apres != avant[a['chemin']]:
            bouges.append((a['chemin'], a.get('coffre', False)))
            ok.append(a['chemin'])
        else:
            ok.append(a['chemin'])

    print(f"{len(produits)} générateur(s) déclaré(s) à l'index, "
          f"{len(ok)} qui tournent")

    print(f"\nV1 — {len(echecs)} générateur(s) qui lèvent")
    for chemin, gen, ligne in echecs:
        print(f"    {chemin}")
        print(f"        par {gen} — {ligne}")

    print(f"\nV2 — {len(sans_regle)} générateur(s) sans règle de construction")
    for chemin, gen in sans_regle:
        print(f"    {chemin} — déclaré produit par {gen}, aucune cible")

    volees = sorted(doubles_cible) + [
        f'${{{k}}} affectée {len(v)} fois' for k, v in sorted(doubles_var.items())]
    print(f"\nV3 — {len(volees)} cible(s) volée(s) au fichier de construction")
    for v in volees:
        print(f"    {v}")

    print(f"\nV4 — {len(non_produits)} générateur(s) en attente d'un intrant")
    for chemin, gen, motif in non_produits:
        print(f"    {chemin} — {motif}")

    print(f"\nV5 — {len(bouges)} dérivé(s) qui ont bougé au rejeu")
    for chemin, au_coffre in bouges:
        print(f"    {chemin}{' — au coffre, à reverser' if au_coffre else ''}")

    dur = len(echecs) + len(sans_regle) + len(volees)
    print(f"\n{dur} échec(s) bloquant(s), "
          f"{len(non_produits)} en attente d'un intrant, "
          f"{len(bouges)} dérivé(s) déplacé(s)")
    return 1 if dur else 0


if __name__ == '__main__':
    sys.exit(controler(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '.'))
