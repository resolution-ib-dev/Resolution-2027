# -*- coding: utf-8 -*-
"""Notation de l'éval de la rédaction cible — en correspondance, jamais en égalité.

Deux rédacteurs écrivent deux textes qui produisent le même effet de droit. Ce
qui se compare n'est donc pas la lettre mais la **correspondance**, sur les
trois critères du contrat, notés séparément :

    article    l'adresse visée, décomposée et normalisée, sans collage
    operation  laquelle des opérations, parmi la liste fermée
    portee     l'article entier, ou une subdivision

**Le même détecteur lit les deux côtés.** Les opérations et les portées se
relèvent par `partage_calibrage.operation` et `partage_calibrage.cible`, sur la
disposition de l'administration comme sur la forme littérale que la skill rend.
Une notation qui lirait la sortie de la skill avec d'autres yeux que le terrain
mesurerait le lecteur.

**`chapeau` n'est pas une opération.** « L'article X est ainsi modifié : »
annonce, il ne prescrit pas. Il sort des deux côtés, faute de quoi une
disposition qui l'écrit serait comptée fausse contre une qui ne l'écrit pas.

**Le contrôle de réapplication n'est pas une note, c'est une porte.** Il se
rejoue ici — jamais cru sur la parole du fil qui a rendu la disposition — et
son taux se publie à part. Une disposition qui ne redonne pas C à l'octet est
fausse ; elle sort du compte des correspondances complètes et elle se compte
dans son propre taux.

**Le critère de portée n'est pas mesurable en l'état, et cela se dit.**
`partage_calibrage.cible` lit la portée à la tête de la phrase — « Le second
alinéa … est supprimé ». Il ne sait pas lire une cible en complément
circonstanciel — « Au deuxième alinéa, les mots : « X » sont remplacés par … »,
qui est la forme la plus courante du texte réel. Sur ce banc, il rend
`indetermine` sept fois sur dix, **des deux côtés**. Le taux de portée se publie
avec ce compte, et il ne se lit pas comme une note de la skill : c'est une note
du détecteur. Le rendre mesurable est un travail d'appareil, pas de rédaction.

**Trois populations, et elles ne se confondent pas.**

    échantillon   ce qui a été tiré
    dicible       moins les cas dont l'effet ne se dit pas sans nommer une
                  subdivision — une limite du banc, pas une note
    notée         moins les cas où le siège est absent de l'extrait de droit —
                  droit non codifié, code non porté. La skill les déclare
                  `hors_capacite`, ce qui est le comportement attendu, et ils ne
                  se notent pas : il n'y a pas de colonne A.

Le banc d'atelier et ce qui se verse ne vivent pas au même endroit : `eval/`
porte le terrain, l'échantillon et les réponses brutes — hors index, hors
coffre —, `livrables/eval_disposition/` porte les trois pièces qui se versent.

Usage : python3 noter_eval_disposition.py ../eval ../livrables/eval_disposition
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import partage_calibrage as pc
import reappliquer

SEPARATEURS = re.compile(r'\s*,\s*|\s+et\s+')

# --------------------------------------------------------------- équivalences
# **Proposée, non validée.** Deux rédacteurs écrivent deux textes qui produisent
# le même effet de droit : c'est la prémisse de la notation en correspondance, et
# elle ne s'arrête pas au verbe. Compléter un article par un alinéa et insérer un
# alinéa après le dernier écrivent le même droit ; supprimer une subdivision et
# l'abroger aussi ; créer un article et l'insérer aussi.
#
# Cette table est un jugement de légistique, donc un jugement de fond : elle
# revient à l'auteur. Tant qu'elle n'est pas validée, **les deux taux se
# publient** — le strict, qui ne l'emploie pas, et celui en équivalence, qui
# l'emploie. Aucun des deux ne remplace l'autre.
EQUIVALENCES = {
    'suppression': 'abrogation',
    'completement': 'insertion',
    'creation': 'insertion',
    'retablissement': 'insertion',
    'redaction_nouvelle': 'remplacement',
}


def nature(op):
    return EQUIVALENCES.get(op, op)


def articles(brut):
    """Une énumération d'adresses se décompose ; une fourchette reste entière.

    « L. 314-2, L. 314-3 et L. 314-4 » fait trois adresses. « L. 314-2 à
    L. 314-4 » en fait une, marquée : déplier une fourchette demande de savoir
    ce qu'elle contient, et cela ne se devine pas.
    """
    if not brut:
        return set()
    return {p.strip() for p in SEPARATEURS.split(brut.strip()) if p.strip()}


def cite(numero, texte):
    """Le numéro d'article apparaît-il dans le texte, en entier ?

    La sous-chaîne ne suffit pas : `L. 314-12` est contenu dans `L. 314-12-1`,
    qui est un autre article. On exige donc que rien de la numérotation ne suive.
    """
    if not numero or not texte:
        return False
    return re.search(re.escape(numero) + r'(?![\w.\-])', texte) is not None


def _lignes(txt):
    return [l for l in (txt or '').split('\n') if l.strip()]


def releve(txt):
    """Les opérations et les portées d'un texte de disposition, ligne à ligne."""
    ops, portees = [], []
    for ligne in _lignes(txt):
        op, _ = pc.operation(ligne)
        if op and op != 'chapeau':
            ops.append(op)
            portees.append(pc.cible(ligne))
    return ops, portees


def jaccard(a, b):
    a, b = set(a), set(b)
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b)


def noter(terrain, reponse):
    """La note d'un cas. Rend un dict, jamais un verdict seul."""
    att_art = set()
    for ad in terrain['adresses']:
        att_art |= articles(ad['brut'])
    obt_art = set()
    for col in reponse.get('colonnes') or []:
        obt_art |= articles(col.get('adresse_article'))
    for ad in reponse.get('adresses_visees') or []:
        obt_art |= articles(ad.get('article'))

    att_ops, att_por = releve(terrain['disposition_administration'])
    obt_txt = '\n'.join((c.get('forme_litterale') or '')
                        for c in (reponse.get('colonnes') or []))
    obt_ops, obt_por = releve(obt_txt)

    # La réapplication se rejoue ici, colonne par colonne.
    verdicts = []
    for col in reponse.get('colonnes') or []:
        if col.get('a') is None or col.get('c') is None or not col.get('forme'):
            verdicts.append('ABSENT')
            continue
        v, _ = reappliquer.controler({'a': col['a'], 'c': col['c'],
                                      'forme': col['forme']})
        verdicts.append(v)

    art_ok = att_art == obt_art and bool(att_art)
    # L'adresse déclarée et l'adresse écrite ne suivent pas la même convention
    # sur l'insertion d'un article : le socle relève l'article d'ancrage — « après
    # l'article L. 314-12 » —, la skill nomme l'article créé — « L. 314-12-1 ».
    # Les deux sont justes, et la disposition écrite porte les deux. Le second
    # critère lit donc ce que la skill a **écrit**, et non ce qu'elle a déclaré.
    art_cite = bool(att_art) and all(cite(a, obt_txt) for a in att_art)
    ops_ok = sorted(att_ops) == sorted(obt_ops)
    por_ok = sorted(att_por) == sorted(obt_por)
    # En nature : l'ensemble des opérations, une fois les équivalences
    # appliquées. Le compte ne joue plus — « les articles X et Y sont abrogés »
    # et deux phrases d'abrogation écrivent le même droit.
    nat_att = {nature(o) for o in att_ops}
    nat_obt = {nature(o) for o in obt_ops}
    nat_ok = nat_att == nat_obt and bool(nat_att)
    # La couverture est un critère à part, et c'est le plus dur : une skill qui
    # traite trois effets sur huit a bien choisi ses opérations et manqué la
    # mesure. Elle se compte sur les effets, pas sur les phrases.
    couverture = (min(1.0, len(obt_ops) / len(att_ops)) if att_ops
                  else (1.0 if not obt_ops else 0.0))
    return {
        'cle': terrain['cle'],
        'nb_alineas_terrain': terrain['nb_alineas'],
        'article': {'attendu': sorted(att_art), 'obtenu': sorted(obt_art),
                    'exact': art_ok, 'recouvrement': jaccard(att_art, obt_art),
                    'cite_dans_la_disposition': art_cite},
        'operation': {'attendu': sorted(att_ops), 'obtenu': sorted(obt_ops),
                      'exact': ops_ok, 'recouvrement': jaccard(att_ops, obt_ops)},
        'portee': {'attendu': sorted(att_por), 'obtenu': sorted(obt_por),
                   'exact': por_ok, 'recouvrement': jaccard(att_por, obt_por)},
        'nature': {'attendu': sorted(nat_att), 'obtenu': sorted(nat_obt),
                   'exact': nat_ok, 'recouvrement': jaccard(nat_att, nat_obt)},
        'couverture': couverture,
        'reapplication': verdicts,
        'prouve': bool(verdicts) and all(v == 'PROUVE' for v in verdicts),
        'correspondance_complete': art_ok and ops_ok and por_ok,
        'correspondance_en_nature': art_cite and nat_ok and couverture >= 1.0,
    }


def main(atelier, dossier):
    terrain = {c['cle']: c for c in json.load(
        open(os.path.join(atelier, 'terrain.json'), encoding='utf-8'))['cas']}
    enonces = {c['cle']: c for c in json.load(
        open(os.path.join(dossier, 'enonces.json'), encoding='utf-8'))['cas']}

    reponses = {}
    for i in range(1, 99):
        p = os.path.join(atelier, f'reponses_lot_{i}.json')
        if not os.path.exists(p):
            continue
        for c in json.load(open(p, encoding='utf-8'))['cas']:
            reponses[c['cle']] = c

    manquants = [k for k in terrain if k not in reponses]
    indicibles = [k for k, c in enonces.items() if c.get('indicible')]
    hors_capacite = [k for k, c in reponses.items()
                     if c.get('hors_capacite') and not c.get('saute')]

    notes = []
    for cle, t in terrain.items():
        r = reponses.get(cle)
        if r is None or r.get('saute') or r.get('hors_capacite'):
            continue
        notes.append(noter(t, r))

    n = len(notes)
    def taux(f):
        return sum(1 for x in notes if f(x)) / n if n else 0.0
    def moy(cle):
        return sum(x[cle]['recouvrement'] for x in notes) / n if n else 0.0

    portees = [p for x in notes for p in x['portee']['attendu'] + x['portee']['obtenu']]
    colonnes = [v for x in notes for v in x['reapplication']]
    prouvees = sum(1 for v in colonnes if v == 'PROUVE')

    resultat = {
        'population': {
            'echantillon': len(terrain),
            'indicibles': len(indicibles),
            'hors_capacite': len(hors_capacite),
            'sans_reponse': len(manquants),
            'notee': n,
        },
        'correspondance': {
            'article_exact': taux(lambda x: x['article']['exact']),
            'article_cite': taux(
                lambda x: x['article']['cite_dans_la_disposition']),
            'operation_exacte': taux(lambda x: x['operation']['exact']),
            'portee_exacte': taux(lambda x: x['portee']['exact']),
            'les_trois': taux(lambda x: x['correspondance_complete']),
            'nature_exacte': taux(lambda x: x['nature']['exact']),
            'couverture_complete': taux(lambda x: x['couverture'] >= 1.0),
            'couverture_moyenne': (sum(x['couverture'] for x in notes) / n
                                   if n else 0.0),
            'les_trois_en_nature': taux(
                lambda x: x['correspondance_en_nature']),
            'article_recouvrement_moyen': moy('article'),
            'operation_recouvrement_moyen': moy('operation'),
            'portee_recouvrement_moyen': moy('portee'),
        },
        'portee_mesurable': {
            'relevees': len(portees),
            'indeterminees': portees.count('indetermine'),
            'part_indeterminee': (portees.count('indetermine') / len(portees)
                                  if portees else 0.0),
            '_reserve': "Le détecteur ne lit pas une cible en complément "
                        "circonstanciel. Tant que cette part est haute, le taux "
                        "de portée note le détecteur et non la skill.",
        },
        'reapplication': {
            'colonnes': len(colonnes),
            'prouvees': prouvees,
            'taux': prouvees / len(colonnes) if colonnes else 0.0,
            'verdicts': {v: colonnes.count(v) for v in sorted(set(colonnes))},
        },
        'correspondance_et_preuve': taux(
            lambda x: x['correspondance_complete'] and x['prouve']),
        'indicibles': sorted(indicibles),
        'hors_capacite': sorted(hors_capacite),
        'sans_reponse': sorted(manquants),
        'notes': notes,
    }

    # Le relevé condensé : ce qui se verse au coffre. Les colonnes A et C
    # pèsent un demi-mégaoctet et A est du verbatim de droit, régénérable depuis
    # le dépôt. Ce qui ne se régénère pas — l'adresse visée, la forme littérale,
    # le verdict, les doutes — tient en un dixième de la place.
    releve = []
    for cle in terrain:
        r = reponses.get(cle)
        if r is None:
            continue
        releve.append({
            'cle': cle,
            'saute': bool(r.get('saute')),
            'hors_capacite': r.get('hors_capacite'),
            'adresses_visees': r.get('adresses_visees'),
            'dispositions': [{'adresse_article': c.get('adresse_article'),
                              'forme_litterale': c.get('forme_litterale')}
                             for c in (r.get('colonnes') or [])],
            'doutes': r.get('doutes'),
        })
    with open(os.path.join(dossier, 'releve.json'), 'w',
              encoding='utf-8', newline='') as f:
        json.dump({'_regle': "Ce que la skill a rendu, sans les colonnes A et C "
                             "— A est du verbatim régénérable depuis le dépôt de "
                             "droit, C se refait en rejouant l'éval.",
                   'cas': releve}, f, ensure_ascii=False, indent=1)
        f.write('\n')

    dst = os.path.join(dossier, 'notation.json')
    with open(dst, 'w', encoding='utf-8', newline='') as f:
        json.dump(resultat, f, ensure_ascii=False, indent=1)
        f.write('\n')

    p = resultat['population']
    print(f"échantillon {p['echantillon']} — indicibles {p['indicibles']}, "
          f"hors capacité {p['hors_capacite']}, sans réponse "
          f"{p['sans_reponse']} → population notée {p['notee']}")
    c = resultat['correspondance']
    print(f"  article  exact {c['article_exact']:.0%}   "
          f"recouvrement {c['article_recouvrement_moyen']:.0%}")
    print(f"  opération exact {c['operation_exacte']:.0%}   "
          f"recouvrement {c['operation_recouvrement_moyen']:.0%}")
    pm = resultat['portee_mesurable']
    print(f"  portée   exact {c['portee_exacte']:.0%}   "
          f"recouvrement {c['portee_recouvrement_moyen']:.0%}"
          f"   — NON MESURABLE : {pm['part_indeterminee']:.0%} des portées "
          f"relevées sont indéterminées, des deux côtés")
    print(f"  les trois ensemble {c['les_trois']:.0%}   (notation stricte)")
    print(f"  --- en équivalence, table proposée et non validée")
    print(f"  article  cité dans la disposition {c['article_cite']:.0%}")
    print(f"  nature   exact {c['nature_exacte']:.0%}")
    print(f"  couverture complète {c['couverture_complete']:.0%}   "
          f"moyenne {c['couverture_moyenne']:.0%}")
    print(f"  article + nature + couverture {c['les_trois_en_nature']:.0%}")
    r = resultat['reapplication']
    print(f"réapplication — {r['prouvees']}/{r['colonnes']} colonne(s) "
          f"prouvée(s) à l'octet, {r['taux']:.0%} ; {r['verdicts']}")
    print(f"correspondance complète ET prouvée — "
          f"{resultat['correspondance_et_preuve']:.0%}")
    print(f'{dst} écrit')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
