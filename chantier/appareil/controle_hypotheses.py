# -*- coding: utf-8 -*-
"""Contrôle des hypothèses consignées : chaque repère se retrouve au manuscrit.

Une hypothèse ne porte pas le verbatim du livre, elle porte un **repère** — un
fragment court qui permet de la retrouver. Ce contrôle vérifie que le fragment
est bien là, littéralement. C'est la seule garantie possible contre une dérive
de recopie : si le modèle a déformé un mot en écrivant l'hypothèse, le fragment
ne se retrouve plus et le contrôle s'arrête.

Cinq vérifications.

  H1  chaque repère se retrouve littéralement au manuscrit, corps ou note
  H2  chaque note citée existe au relevé des notes
  H3  chaque nœud commandé existe au REF_doctrine
  H4  les identifiants sont uniques et la nomenclature est fermée
  H5  compte par domaine et par sens — ce que le chiffrage doit à ses hypothèses

Usage : python3 controle_hypotheses.py ../manuscrit/manuscrit.html \\
            ../referentiels/notes_manuscrit.json \\
            ../referentiels/REF_doctrine.json
"""
import html
import json
import re
import sys
from collections import Counter

import hypotheses_doctrine

NATURES = {'methode', 'parametre', 'comportement', 'source_externe'}
SENS = {'minorant', 'majorant', 'neutre'}
DOMAINES = {'fiscal', 'chomage', 'retraite', 'patrimoine', 'education',
            'croissance', 'risque', 'methode'}


def texte_du_manuscrit(chemin):
    s = open(chemin, encoding='utf-8').read()
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s))


def noeuds_du_ref(chemin):
    ref = json.load(open(chemin, encoding='utf-8'))
    vus = set()

    def marche(o):
        if isinstance(o, dict):
            if isinstance(o.get('id'), str):
                vus.add(o['id'])
            for v in o.values():
                marche(v)
        elif isinstance(o, list):
            for v in o:
                marche(v)
    marche(ref)
    return vus


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return 2
    texte = texte_du_manuscrit(argv[1])
    notes = {n['id'] for n in
             json.load(open(argv[2], encoding='utf-8'))['notes']}
    noeuds = noeuds_du_ref(argv[3])
    hyp = hypotheses_doctrine.HYPOTHESES

    print(f"{len(hyp)} hypothèse(s) consignée(s)")

    # H1 — le repère se retrouve au manuscrit
    perdus = []
    for h in hyp:
        r = re.sub(r'\s+', ' ', h['repere']).strip()
        if r not in texte:
            perdus.append((h['id'], r))
    print(f"\nH1 — {len(perdus)} repère(s) introuvable(s) au manuscrit")
    for i, r in perdus:
        print(f"    {i} — « {r[:90]} »")

    # H2 — la note citée existe
    orphelines = [(h['id'], h['note']) for h in hyp
                  if h['note'] and h['note'] not in notes]
    print(f"\nH2 — {len(orphelines)} note(s) citée(s) sans note correspondante")
    for i, n in orphelines:
        print(f"    {i} renvoie à {n}")

    # H3 — les nœuds commandés existent
    morts = [(h['id'], n) for h in hyp for n in h['commande']
             if n not in noeuds]
    print(f"\nH3 — {len(morts)} nœud(s) commandé(s) inexistant(s)")
    for i, n in morts:
        print(f"    {i} commande {n}, qui n'existe pas")

    # H4 — nomenclature
    doubles = [i for i, n in Counter(h['id'] for h in hyp).items() if n > 1]
    hors = [(h['id'], c, h[c]) for h in hyp
            for c, permis in (('nature', NATURES), ('sens', SENS),
                              ('domaine', DOMAINES))
            if h[c] not in permis]
    print(f"\nH4 — {len(doubles)} identifiant(s) en double, "
          f"{len(hors)} valeur(s) hors nomenclature")
    for i in doubles:
        print(f"    {i}")
    for i, c, v in hors:
        print(f"    {i} : {c} = {v}")

    # H5 — ce que le chiffrage doit à ses hypothèses
    print("\nH5 — répartition")
    for cle in ('domaine', 'nature', 'sens'):
        c = Counter(h[cle] for h in hyp)
        print(f"    {cle:9s} " + ' · '.join(f'{k} {v}'
                                            for k, v in sorted(c.items())))
    sans_noeud = [h['id'] for h in hyp if not h['commande']]
    print(f"    {len(sans_noeud)} hypothèse(s) sans nœud commandé — "
          f"{', '.join(sans_noeud)}")
    print("      Ce ne sont pas des orphelines : une hypothèse de méthode ou "
          "une estimation externe pèse sur le propos sans commander un nœud.")

    echecs = len(perdus) + len(orphelines) + len(morts) + len(doubles) + len(hors)
    print(f"\n{echecs} échec(s)")
    return 1 if echecs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
