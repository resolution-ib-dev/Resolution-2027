# -*- coding: utf-8 -*-
"""Contrôle du référentiel des faits. Il ne produit rien.

Le référentiel des faits a une propriété que les autres n'ont pas : **il est
utile surtout par ce qu'il déclare ne pas savoir.** Un chiffre sans source y est
un chiffre sans source, et le contrôle vérifie que rien ne s'est glissé entre
les deux — ni une source apparue sans qu'on l'écrive, ni un trou refermé par
commodité.

Sept vérifications. Six échouent, une compte.

  F1  toute entrée hors proto porte une valeur lisible
  F2  la confiance déclarée se recalcule depuis les champs présents
  F3  aucun identifiant n'est porté deux fois
  F4  les candidats du proto sont tous à confiance nulle, tous marqués à sourcer
  F5  aucune source écrite à la main ne vise une entrée qui n'existe pas
  F6  compte des entrées sans unité, sans millésime, à sourcer
  F7  deux entrées déclarées identiques portent bien la même valeur

Un chiffre énoncé trois fois au corpus fait trois entrées, et c'est normal : le
référentiel sert à dire qu'elles concordent, non à les fusionner. **La répétition
n'est pas une faute ; la discordance en est une.** Deux nombres égaux ne parlent
pas forcément de la même chose, et le rapprochement ne se devine donc pas : il
s'écrit à la main, par le champ `meme_que` de `sources_chiffres.py`. `F7` ne
contrôle que ce qui a été rapproché, et il grandit à mesure du sourçage.

Usage : python3 controle_chiffres.py ../referentiels/REF_chiffres.json
"""
import ast
import json
import sys
from collections import Counter, defaultdict

import sources_chiffres

CONFIANCE = {3: 'strate1', 2: 'source_declaree',
             1: 'ancrage_ou_operation', 0: 'sans_source'}


OPERATEURS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.USub, ast.UAdd)


def evaluer(expression):
    """Évalue une expression arithmétique et rien d'autre.

    Pas d'appel, pas de nom, pas d'attribut : un contrôle qui exécuterait du
    code arbitraire écrit dans un fichier de données ne serait plus un contrôle.
    """
    def marche(n):
        if isinstance(n, ast.Expression):
            return marche(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return float(n.value)
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, OPERATEURS):
            v = marche(n.operand)
            return -v if isinstance(n.op, ast.USub) else v
        if isinstance(n, ast.BinOp) and isinstance(n.op, OPERATEURS):
            g, d = marche(n.left), marche(n.right)
            t = type(n.op)
            if t is ast.Add:
                return g + d
            if t is ast.Sub:
                return g - d
            if t is ast.Mult:
                return g * d
            if t is ast.Div:
                return g / d if d else float('nan')
            return g ** d
        raise ValueError(f"expression refusée : {ast.dump(n)[:60]}")
    return marche(ast.parse(expression, mode='eval'))


VERDICTS = {
    'accord': 'accord',
    'tete_decalee': 'tête décalée',
    'discordance': 'DISCORDANCE',
    'arbitre': 'arbitrée',
}

# Une unité vide, ou le tiret que le REF_doctrine emploie pour dire qu'il n'y en
# a pas, ne se compare à rien.
UNITE_MUETTE = (None, '', '—', '-')

# Deux entrées peuvent porter le même montant à deux échelles : « 37 059 M€ » et
# « 37,1 Md€ ». Le corpus écrit indifféremment « Md€ » et « milliards », qui sont
# le même mot. La comparaison ramène donc les montants à l'euro, en gardant la
# **dimension** — un euro par an et un euro par mois ne sont pas le même fait, et
# ne se ramènent l'un à l'autre sous aucun prétexte.
#
# `M`, `millions` et `milliards` sans euro restent hors de la table : le corpus
# les emploie aussi pour des personnes et pour des mois.
ECHELLE = {
    'Md€': (1e9, '€'), 'Md€/an': (1e9, '€/an'),
    'M€': (1e6, '€'), 'M€/an': (1e6, '€/an'),
    'k€': (1e3, '€'), 'k€/an': (1e3, '€/an'),
    '€': (1.0, '€'), '€/an': (1.0, '€/an'), '€/mois': (1.0, '€/mois'),
    'milliards': (1e9, '€'),
}


def normaliser(valeur, unite):
    """Le montant ramené à l'euro et sa dimension, ou la valeur telle quelle."""
    if valeur is None:
        return None, unite
    f, dim = ECHELLE.get(unite, (None, unite))
    if f is None:
        return valeur, unite
    return valeur * f, dim


def valeurs(e):
    """Toutes les valeurs d'une entrée : sa tête et ses déclinaisons.

    Le relevé prend en tête la première valeur de l'énoncé, qui n'est pas
    toujours celle qui porte le fait — une année d'abord, un total ensuite. La
    comparaison regarde donc l'énoncé entier avant de conclure à un désaccord.
    Chaque valeur sort ramenée à son échelle et accompagnée de sa dimension.
    """
    out = []
    if e.get('valeur_num') is not None:
        out.append(normaliser(round(float(e['valeur_num']), 6), e.get('unite')))
    for d in e.get('declinaisons') or []:
        if d.get('valeur_num') is not None:
            out.append(normaliser(round(float(d['valeur_num']), 6),
                                  d.get('unite')))
    return out


def memes_unites(a, b):
    ua = a.get('unite') if a.get('unite') not in UNITE_MUETTE else None
    ub = b.get('unite') if b.get('unite') not in UNITE_MUETTE else None
    if ua is None or ub is None:
        return ua is None and ub is None
    if ua == ub:
        return True
    # « Md€ » et « milliards » sont le même mot : ce n'est pas une divergence.
    # « Md€ » et « Md€/an » en sont deux, et l'écart se dit.
    da, db = ECHELLE.get(ua), ECHELLE.get(ub)
    return da is not None and da == db


def affiche(e):
    u = e.get('unite') or ''
    return f"{e.get('valeur')} [{e.get('valeur_num')} {u}]".strip()


def _proche(a, b, tolerance):
    return abs(a - b) <= tolerance


def comparer(e, ref, tolerance=0.0):
    """Comment cette entrée s'accorde avec la référence de son fait.

    `tolerance` s'exprime dans l'unité de la référence et ne s'emploie que pour
    un arrondi déclaré au motif du groupe.

    La comparaison porte sur le **nombre**, ramené à l'euro quand l'unité le
    permet. Elle ne porte pas sur la dimension : « 16,9 Md€ » et « 16,9 Md€/an »
    portent le même nombre, et c'est le relevé des unités divergentes qui dit
    que l'un des deux a perdu son « par an ». Deux rapports orthogonaux valent
    mieux qu'un verdict qui mélange un désaccord de chiffre et une notation.
    """
    te, tr = e.get('valeur_num'), ref.get('valeur_num')
    if te is None or tr is None:
        return 'discordance', "l'une des deux valeurs n'a pas été lue"
    ne = normaliser(round(float(te), 6), e.get('unite'))[0]
    nr = normaliser(round(float(tr), 6), ref.get('unite'))[0]
    # La tolérance est écrite dans l'unité de la référence : elle se ramène à
    # l'échelle normalisée par le même facteur.
    tol = tolerance * (ECHELLE.get(ref.get('unite'), (1.0,))[0] or 1.0)
    if _proche(ne, nr, tol):
        return 'accord', ("à l'arrondi déclaré" if ne != nr else '')
    if _proche(abs(ne), abs(nr), tol):
        return 'accord', 'au signe près, deux points de vue opposés'
    ve = {abs(v) for v, _ in valeurs(e)}
    vr = {abs(v) for v, _ in valeurs(ref)}
    for v in sorted(vr, reverse=True):
        for v2 in ve:
            if _proche(v, v2, tol):
                return ('tete_decalee',
                        f"la valeur {v2:g} est aux deux énoncés, "
                        f"mais pas en tête")
    return ('discordance',
            f"aucune valeur commune : {sorted(vr)} contre {sorted(ve)}")


def confiance_attendue(e):
    if e['provenance'] == 'note':
        return 3
    if e['source']:
        return 2
    if e['codes_preuve'] or e.get('operation_rejouee'):
        return 1
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    ref = json.load(open(argv[1], encoding='utf-8'))
    es = ref['entrees']

    print(f"{len(es)} entrée(s) au référentiel des faits — "
          + ' · '.join(f'{k} {v}' for k, v in
                       sorted(Counter(e['provenance'] for e in es).items())))

    # F1 — une valeur qu'on n'a pas su lire
    illisibles = [e['id'] for e in es
                  if e['provenance'] != 'proto' and e['valeur_num'] is None]
    print(f"\nF1 — {len(illisibles)} entrée(s) hors proto sans valeur lisible")
    for i in illisibles:
        print(f"    {i}")

    # F2 — une confiance qui ne se recalcule pas
    discordantes = [(e['id'], e['confiance'], confiance_attendue(e))
                    for e in es if e['confiance'] != confiance_attendue(e)]
    print(f"\nF2 — {len(discordantes)} confiance(s) discordante(s)")
    for i, d, a in discordantes:
        print(f"    {i} : déclarée {CONFIANCE[d]}, attendue {CONFIANCE[a]}")

    # F3 — un identifiant en double
    doubles = [i for i, n in Counter(e['id'] for e in es).items() if n > 1]
    print(f"\nF3 — {len(doubles)} identifiant(s) en double")
    for i in doubles:
        print(f"    {i}")

    # F4 — les candidats du proto
    fautifs = [e['id'] for e in es if e['provenance'] == 'proto'
               and not e['sourcee_a_la_main']
               and (e['confiance'] != 0 or not e['a_sourcer'])]
    proto = [e for e in es if e['provenance'] == 'proto']
    print(f"\nF4 — {len(proto)} candidat(s) du proto, {len(fautifs)} hors régime")
    for i in fautifs:
        print(f"    {i}")

    # F5 — une source à la main sans entrée
    connus = {e['id'] for e in es}
    orphelines = sorted(k for k in sources_chiffres.SOURCES if k not in connus)
    print(f"\nF5 — {len(orphelines)} source(s) écrite(s) à la main sans entrée")
    for k in orphelines:
        print(f"    {k}")

    # F6 — l'état du sourçage
    sans_unite = sum(1 for e in es if not e['unite'])
    sans_mil = sum(1 for e in es if not e['millesime'])
    a_sourcer = sum(1 for e in es if e['a_sourcer'])
    main = sum(1 for e in es if e['sourcee_a_la_main'])
    print(f"\nF6 — {a_sourcer} à sourcer · {sans_unite} sans unité · "
          f"{sans_mil} sans millésime · {main} sourcée(s) à la main")
    for niveau in (3, 2, 1, 0):
        n = sum(1 for e in es if e['confiance'] == niveau)
        print(f"    {niveau} {CONFIANCE[niveau]:24s} {n}")

    # F7 — les rapprochements écrits à la main, et leur accord.
    par_id = {e['id']: e for e in es}
    morts = [(i, g['fait']) for g in sources_chiffres.MEME_QUE
             for i in g['entrees'] if i not in par_id]
    print(f"\nF7a — {len(morts)} entrée(s) rapprochée(s) qui n'existe(nt) pas")
    for i, f in morts:
        print(f"    {i} — déclaré au fait « {f} »")

    discordants, decales, unites, arbitres = [], [], [], []
    print(f"\nF7 — {len(sources_chiffres.MEME_QUE)} fait(s) rapproché(s)")
    for groupe in sources_chiffres.MEME_QUE:
        membres = [par_id[i] for i in groupe['entrees'] if i in par_id]
        if len(membres) < 2:
            continue
        ref = membres[0]
        tol = float(groupe.get('tolerance') or 0.0)
        arb = groupe.get('arbitrage')
        if arb and arb.get('retenu') not in {m['id'] for m in membres}:
            morts.append((arb.get('retenu'),
                          f"{groupe['fait']} — arbitrage sans entrée retenue"))
            arb = None
        lignes = []
        for e in membres[1:]:
            verdict, detail = comparer(e, ref, tol)
            if verdict == 'discordance' and arb:
                verdict = 'arbitre'
                arbitres.append((groupe['fait'], e, ref, arb))
            elif verdict == 'discordance':
                discordants.append((groupe['fait'], e, ref, detail))
            elif verdict == 'tete_decalee':
                decales.append((groupe['fait'], e, ref, detail))
            if verdict != 'accord':
                lignes.append((verdict, e, detail))
            if not memes_unites(e, ref):
                unites.append((groupe['fait'], e, ref))
        if lignes:
            print(f"\n  « {groupe['fait'] } »   référence {ref['id']} : "
                  f"{affiche(ref)}")
            for verdict, e, detail in lignes:
                print(f"      {VERDICTS[verdict]:18s} {e['id']:36s} "
                      f"{affiche(e)}   {detail}")

    print(f"\n  {len(discordants)} discordance(s) de valeur · "
          f"{len(arbitres)} arbitrée(s) · "
          f"{len(decales)} tête(s) décalée(s) · "
          f"{len(unites)} unité(s) divergente(s)")

    if arbitres:
        print("\n  Discordances arbitrées — la valeur retenue est la seule "
              "qui sorte :")
        for fait, e, ref, arb in arbitres:
            garde = ref if arb['retenu'] == ref['id'] else e
            ecarte = e if garde is ref else ref
            print(f"    « {fait} »")
            print(f"        retenu   {garde['id']} — {affiche(garde)}")
            print(f"        écarté   {ecarte['id']} — {affiche(ecarte)}")
            print(f"        {arb['par']}, {arb['date']} : {arb['motif']}")

    if discordants:
        print("\n  Les couples qui ne concordent pas :")
        for fait, e, ref, detail in discordants:
            print(f"    « {fait} »")
            print(f"        {ref['id']} porte {affiche(ref)}")
            print(f"        {e['id']} porte {affiche(e)}")
            print(f"        {detail}")

    if unites:
        print("\n  Unités divergentes sur un même fait — notation, "
              "à normaliser :")
        for fait, e, ref in unites:
            print(f"    {ref['id']} « {ref['unite']} »  contre  "
                  f"{e['id']} « {e['unite']} »   — {fait}")

    # F8 — les calculs déclarés, rejoués.
    faux, orphelins, ok8 = [], [], 0
    for c in sources_chiffres.CALCULS:
        if c.get('id') and c['id'] not in par_id:
            orphelins.append((c['id'], c['objet']))
        try:
            obtenu = evaluer(c['expression'])
        except (ValueError, SyntaxError, ZeroDivisionError) as err:
            faux.append((c, None, str(err)))
            continue
        if abs(obtenu - c['attendu']) > float(c.get('tolerance') or 0.0):
            faux.append((c, obtenu, None))
        else:
            ok8 += 1
    print(f"\nF8 — {len(sources_chiffres.CALCULS)} calcul(s) déclaré(s), "
          f"{ok8} rejoué(s) juste(s), {len(faux)} faux, "
          f"{len(orphelins)} sans entrée")
    for c, obtenu, err in faux:
        cible = f" [{c['id']}]" if c.get('id') else ''
        print(f"    FAUX{cible} — {c['objet']}")
        if err:
            print(f"        {c['expression']} : {err}")
        else:
            print(f"        {c['expression']} = {obtenu:g}, "
                  f"attendu {c['attendu']:g} {c.get('unite') or ''} "
                  f"(tolérance {c.get('tolerance') or 0})")
    for i, objet in orphelins:
        print(f"    {i} n'existe pas au référentiel — {objet}")

    # Seule la discordance de valeur est un échec. Une tête décalée est un
    # défaut du relevé — la valeur est bien au corpus, elle n'est pas en tête —
    # et une unité divergente est une affaire de notation. Les deux se disent et
    # se corrigent, elles ne bloquent pas.
    echecs = (len(illisibles) + len(discordantes) + len(doubles)
              + len(fautifs) + len(orphelines) + len(morts) + len(discordants)
              + len(faux) + len(orphelins))
    print(f"\n{echecs} échec(s), {a_sourcer} entrée(s) à sourcer, "
          f"{len(decales) + len(unites) + len(arbitres)} signalement(s)")
    return 1 if echecs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
