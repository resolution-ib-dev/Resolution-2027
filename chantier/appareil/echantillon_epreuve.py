# -*- coding: utf-8 -*-
"""L'échantillon du lot d'épreuve — la règle, écrite avant le premier regard.

Le lot d'épreuve de la rédaction cible fait 380 couples. Les jouer tous demande
un fil par poignée de cas et plusieurs heures ; l'éval se ferait alors une fois
et jamais plus. **Un banc qu'on ne rejoue pas ne mesure pas une correction.**
On échantillonne donc, et la règle s'écrit ici, en code, avant que le premier
couple soit regardé — même exigence qu'A-330 sur le partage lui-même.

La règle, et ses quatre clauses.

**Stratifié, proportionnel à la population du lot d'épreuve.** Une strate qui
pèse un quart du lot pèse un quart de l'échantillon. Les huit strates sont
représentées, plus les couples hors strate — ceux dont l'opération n'est pas à
la liste fermée : les écarter ferait un banc plus facile que le texte réel.

**Le tirage est un pas régulier, jamais une graine.** Dans chaque strate, on
prend un couple sur `k = round(N_strate / n_strate)` en partant du premier, dans
l'ordre du texte (article, alinéa, adresse). Une graine pseudo-aléatoire est un
choix caché : personne ne peut recompter. Un pas régulier se recompte, et il
couvre tout le texte au lieu de tasser l'échantillon sur les premiers articles —
ce que ferait « les n premiers de chaque strate ».

**Une strate trop petite rend ce qu'elle a.** Trois couples de rédaction
nouvelle donnent au plus trois cas ; on ne complète pas ailleurs pour faire le
compte rond, sinon la proportion est fausse et le taux ne se lit plus.

**Le lot de calibrage ne rentre jamais.** Il est déjà vu ; un cas vu est
contaminé (règle de lecture du banc).

Usage : python3 echantillon_epreuve.py ../referentiels/redaction_plf.json \\
                                       ../referentiels/lots_epreuve.json \\
                                       ../livrables/eval_disposition/echantillon.json \\
                                       [taille]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import partage_calibrage as pc

TAILLE = 40


def echantillonner(epreuve, taille=TAILLE):
    """Le tirage stratifié à pas régulier. Rend (cas, répartition)."""
    par_strate = {}
    for c in epreuve:
        par_strate.setdefault(c['strate'] or 'hors_strate', []).append(c)
    for v in par_strate.values():
        v.sort(key=lambda c: c['_tri'])

    total = len(epreuve)
    # Quota proportionnel, au moins un par strate non vide. L'arrondi se fait
    # au plus proche ; l'écart au total voulu se dit, il ne se rattrape pas en
    # piochant dans la strate la plus grosse.
    quotas = {}
    for s, v in par_strate.items():
        q = round(taille * len(v) / total)
        quotas[s] = max(1, min(len(v), q))

    cas = []
    for s in sorted(par_strate):
        v, q = par_strate[s], quotas[s]
        pas = max(1, round(len(v) / q))
        pris = v[::pas][:q]
        # Le pas peut rendre moins que le quota quand il arrondit vers le haut :
        # on complète par la fin de la strate, qui n'est pas encore prise.
        if len(pris) < q:
            deja = {c['cle'] for c in pris}
            pris += [c for c in v if c['cle'] not in deja][-(q - len(pris)):]
            pris.sort(key=lambda c: c['_tri'])
        for c in pris:
            cas.append({k: v2 for k, v2 in c.items() if k != '_tri'})
    return cas, {s: (len(par_strate[s]), quotas[s]) for s in sorted(par_strate)}


def main(src_red, src_lots, dst, taille=TAILLE):
    red = json.load(open(src_red, encoding='utf-8'))
    couples = pc.population(red)
    _strates, calibrage, epreuve, _vides, _ps, _el = pc.partager(couples)
    cles_calibrage = {c['cle'] for c in calibrage}
    assert not (cles_calibrage & {c['cle'] for c in epreuve})

    cas, repartition = echantillonner(epreuve, taille)

    # Le texte de l'alinéa et les adresses relevées, portés au cas : c'est la
    # vérité-terrain, et c'est ce que le fil qui rédige les énoncés voit. Le fil
    # qui joue la skill ne reçoit jamais ce bloc.
    textes, refs_par = {}, {}
    for a in red['articles']:
        for al in a['alineas']:
            textes[(a['numero'], al['numero'])] = al['texte']
        for r in a['references']:
            if r['statut'] == 'modifie':
                refs_par.setdefault((a['numero'], r['alinea']), []).append(r)
    for c in cas:
        k = (c['article_texte_depose'], c['alinea'])
        c['terrain'] = {
            'alinea_texte': textes.get(k, ''),
            'references': [{'texte': r['texte'], 'brut': r['brut']}
                           for r in refs_par.get(k, [])],
        }

    sortie = {
        '_regle': __doc__.split('\n\n', 1)[1].split('\nUsage')[0].strip(),
        '_ecrite_avant_le_tirage': True,
        'source': src_red,
        'lot_epreuve': len(epreuve),
        'taille_voulue': taille,
        'taille_obtenue': len(cas),
        'repartition': {s: {'lot_epreuve': n, 'echantillon': q}
                        for s, (n, q) in repartition.items()},
        'cas': cas,
    }
    os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
    with open(dst, 'w', encoding='utf-8', newline='') as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
        f.write('\n')

    print(f'lot d\'épreuve — {len(epreuve)} couple(s) ; échantillon — '
          f'{len(cas)} cas (voulu {taille})')
    for s, (n, q) in repartition.items():
        print(f'    {s:34} {n:4} → {q:3}')
    print(f'{dst} écrit')
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    sys.exit(main(a[0], a[1], a[2], int(a[3]) if len(a) > 3 else TAILLE))
