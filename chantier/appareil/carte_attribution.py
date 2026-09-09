# -*- coding: utf-8 -*-
"""Carte d'attribution : quelle catégorie porte quel gain, quelle perte.

Document de travail, pas un livrable. Il sert à trancher **avant** d'écrire :
un gain se dit en entier chez la catégorie où il est le plus pertinent, une
perte chez celle qui la subit, et chaque catégorie a un axe qu'on peut dire en
une ligne. Les catégories doivent être indépendantes et complémentaires.

Il sort trois choses que la lecture ne donne pas :

- pour chaque fiche retenue, son **axe**, ses gains d'attache et ses pertes ;
- les **orphelins** : gains et pertes qu'aucune fiche ne porterait ;
- les **doublons d'attache** : deux fiches qui revendiquent le même objet.

Usage : python3 carte_attribution.py ../referentiels/positions.json \\
                                     ../referentiels/REF_doctrine.json ../livrables
"""
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generer_fiches import libelles, e, STYLE  # noqa: E402

from structure_fiches import STRUCTURE  # noqa: E402



def main(argv):
    positions = json.load(open(argv[1], encoding='utf-8'))
    ref = json.load(open(argv[2], encoding='utf-8'))
    sortie = argv[3]
    lib = libelles(ref)
    cats = {c['id']: c for c in positions['categories']}
    dispo_g, dispo_p = {}, {}
    for l in positions['lignes']:
        if l.get('modalite'):
            continue
        if l['position'] == 'gagnant':
            dispo_g.setdefault(l['ancrage'], set()).add(l['categorie'])
        elif l['position'] == 'perdant':
            dispo_p.setdefault(l['ancrage'], set()).add(l['categorie'])

    pris_g, pris_p, doublons, faux = {}, {}, [], []
    for cid, _t, _a, gs, ps in STRUCTURE:
        for a in gs:
            if cid not in dispo_g.get(a, set()):
                faux.append((cid, a, 'gain non porté par la catégorie'))
            if a in pris_g:
                doublons.append((a, pris_g[a], cid))
            pris_g[a] = cid
        for a in ps:
            if cid not in dispo_p.get(a, set()):
                faux.append((cid, a, 'perte non portée par la catégorie'))
            # Une perte peut frapper deux populations distinctes — l'abolition
            # du statut touche l'agent public et l'enseignant. Ce n'est pas un
            # doublon, à condition que les deux libellés disent deux angles.
            pris_p[a] = cid

    retenues = {c[0] for c in STRUCTURE}
    orph_g = [(a, cs) for a, cs in sorted(dispo_g.items())
              if a not in pris_g and cs & retenues]
    orph_p = [(a, cs) for a, cs in sorted(dispo_p.items())
              if a not in pris_p and cs & retenues]

    o = ['<div class=page><div class=marque><span class=nom>Résolution</span>'
         '<span class=quoi>Carte d’attribution — document de travail</span>'
         '</div><div class=filet><i></i><i></i><i></i></div>',
         '<div class=tete><h1 class=qui>Qui porte quoi</h1>'
         f'<p class=def>{len(STRUCTURE)} fiches. Un gain se dit en entier chez '
         'la catégorie où il est le plus pertinent ; ailleurs il revient en '
         'rappel. Une perte se dit chez qui la subit.</p></div>',
         '<div class=corps>']
    groupes = {c: g['titre'] for g in positions['groupes']
               for c in g['categories']}
    dernier = None
    for cid, titre, axe, gs, ps in STRUCTURE:
        gr = groupes.get(cid, '')
        if gr != dernier:
            o.append(f'<div class="bande q">{e(gr)}</div>')
            dernier = gr
        eff = cats[cid]['effectif']
        o.append(f'<div class=carte><h3>{e(titre)}'
                 + (f'<span class=eff>{e(eff)}</span>' if eff else '')
                 + f'</h3><p class=axe>{e(axe)}</p>')
        if ps:
            o.append('<p class=lot><b class=p>Perd</b>' + ' · '.join(
                f'<i>{e(lib.get(a, a))}</i>' for a in ps) + '</p>')
        if gs:
            o.append('<p class=lot><b class=g>Porte</b>' + ' · '.join(
                f'<i>{e(lib.get(a, a))}</i>' for a in gs) + '</p>')
        if not gs and not ps:
            o.append('<p class=lot><b class=v>À instruire</b>'
                     '<i>aucune attache déclarée</i></p>')
        o.append('</div>')
    o.append('</div><div class=corps>')
    o.append('<div class="bande p">Ce qui n’est porté par personne</div>')
    for nom, lot in (('gain', orph_g), ('perte', orph_p)):
        for a, cs in lot:
            o.append(f'<p class=orph><b>{nom}</b> {e(lib.get(a, a))[:70]} '
                     f'<span>{", ".join(sorted(cs & retenues))}</span></p>')
    if doublons:
        o.append('<div class="bande p">Revendiqué deux fois</div>')
        for a, c1, c2 in doublons:
            o.append(f'<p class=orph><b>{e(a)}</b> {c1} et {c2}</p>')
    if faux:
        o.append('<div class="bande p">Attache impossible</div>')
        for cid, a, motif in faux:
            o.append(f'<p class=orph><b>{cid}</b> {e(a)} — {motif}</p>')
    o.append('</div></div>')

    css = """
.carte{border-top:1px solid var(--fil);padding:.8rem 0}
.carte h3{margin:0 0 .2rem;font-size:1.12rem;font-weight:700;
 display:flex;justify-content:space-between;align-items:baseline;gap:1rem}
.carte .eff{font:700 10px/1 var(--mono);letter-spacing:.1em;color:var(--ocre);
 white-space:nowrap}
.axe{margin:0 0 .5rem;color:var(--gris);font-size:.95rem;font-style:italic}
.lot{margin:.25rem 0;font-size:.88rem;line-height:1.7}
.lot b{display:inline-block;font:700 9px/1.6 var(--mono);letter-spacing:.12em;
 text-transform:uppercase;color:var(--pap);padding:0 .35rem;margin-right:.5rem;
 vertical-align:.1em}
.lot b.g{background:var(--gain)} .lot b.p{background:var(--perte)}
.lot b.v{background:var(--ocre)}
.lot i{font-style:normal;color:#3a3a38}
.orph{margin:.2rem 0;font-size:.86rem;color:var(--gris)}
.orph b{font:700 9px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;
 color:var(--perte);margin-right:.5rem}
.orph span{font-family:var(--mono);font-size:.85em;color:#a09a90}
"""
    page = ('<!doctype html><html lang=fr><meta charset=utf-8>'
            '<meta name=viewport content="width=device-width,initial-scale=1">'
            '<title>Résolution — carte d’attribution</title>'
            f'<style>{STYLE}{css}</style>' + ''.join(o) + '</html>')
    chemin = os.path.join(sortie, 'carte_attribution.html')
    open(chemin, 'w', encoding='utf-8').write(page)
    print(f'{chemin} — {len(STRUCTURE)} fiches, {len(orph_g)} gain(s) et '
          f'{len(orph_p)} perte(s) sans porteur, {len(doublons)} doublon(s), '
          f'{len(faux)} attache(s) impossible(s)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
