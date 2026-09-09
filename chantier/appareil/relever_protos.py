# -*- coding: utf-8 -*-
"""Relevé des chiffres des protos, et détection des collisions avec le corpus.

Le proto Données porte ses candidats en clair, dans des balises que le
générateur du référentiel des faits sait lire. **Les autres protos n'ont pas
cette balise** : ce sont des livrables rédigés — un une-page, une Q&A, une note
aux entreprises, un input logement social, une réserve d'arguments, une note de
réforme budgétaire — et leurs chiffres vivent au fil des phrases.

Ils n'en sont pas moins des chiffres du corpus, et **rien ne garantit qu'ils ne
contredisent pas le référentiel**. C'est exactement le défaut que A-57 déclare
non reportable : une contradiction trouvée après la publication est une
contradiction publiée.

## Ce que ce relevé fait, et ce qu'il ne fait pas

**Il fait** : découper chaque proto en phrases, garder celles qui portent un
nombre, et les confronter au référentiel des faits. La grammaire des nombres et
des unités est celle de `generer_ref_chiffres.py`, importée et non recopiée —
un second dialecte de lecture des nombres serait un second point de vérité.

**Il ne fait pas** de rapprochement. A-35 le pose : deux nombres égaux ne
parlent pas forcément de la même chose, et le rapprochement s'écrit à la main
dans `sources_chiffres.MEME_QUE`. Ce script produit des **candidats à la
lecture**, jamais une assertion. Il sort deux listes.

  1. **Les collisions** — un énoncé de proto et une entrée du référentiel qui
     parlent de la même chose et ne portent pas le même chiffre. Trois
     conditions, et les trois ensemble : au moins trois mots significatifs
     communs et représentant au moins le tiers du plus petit des deux
     vocabulaires, **au moins une unité présente des deux côtés** — faute de quoi les
     deux chiffres ne sont pas comparables et leur écart ne veut rien dire — et
     aucune valeur commune. C'est le profil d'une contradiction.
  2. **La veille** — les grandeurs que `sources_chiffres.VEILLE` déclare
     publiables, cherchées par leurs mots dans les protos. Une phrase qui les
     emploie et porte un autre chiffre sort en alerte. C'est le sens inverse du
     détecteur : on part du fait, non du hasard lexical, et cela attrape ce qui
     se dit en peu de mots.
  3. **Les chiffres hors référentiel** — un énoncé de proto dont aucune valeur
     ne se retrouve au référentiel. Ni faute ni concordance : un chiffre que
     rien ne contrôle.

Un proto est une archive : rien ne s'y corrige. Ce qui se corrige est le
référentiel, ou la décision de ne plus se servir du proto.

Usage : python3 relever_protos.py ../referentiels/REF_chiffres.json \\
            ../livrables/releve_protos.txt ../sources/*.html
"""
import html
import json
import re
import sys

import generer_ref_chiffres as gen
import sources_chiffres

# Les mots trop courants pour signaler quoi que ce soit. Une collision fondée
# sur « dépense » et « public » ne dit rien ; une collision fondée sur
# « allocation », « chômage » et « médiane » dit quelque chose.
VIDES = {
    'dans', 'pour', 'avec', 'sans', 'plus', 'moins', 'cette', 'leurs', 'entre',
    'elles', 'toute', 'toutes', 'tous', 'chaque', 'selon', 'aussi', 'ainsi',
    'donc', 'mais', 'alors', 'depuis', 'apres', 'avant', 'contre', 'chez',
    'euros', 'euro', 'milliards', 'millions', 'million', 'milliard', 'annee',
    'annees', 'soit', 'dont', 'meme', 'encore', 'deja', 'tres', 'etre', 'sont',
    'cela', 'celle', 'ceux', 'leur', 'nous', 'vous', 'notre', 'nos', 'que',
    'qui', 'est', 'les', 'des', 'une', 'aux', 'par', 'sur', 'son', 'ses',
}
MOT = re.compile(r"[a-zà-öø-ÿ]{4,}")
ACCENTS = str.maketrans('àâäéèêëîïôöùûüç', 'aaaeeeeiioouuuc')


def mots(texte):
    """Les mots significatifs d'un énoncé, sans accent ni casse."""
    t = texte.lower().translate(ACCENTS)
    return {m for m in MOT.findall(t) if m not in VIDES}


def texte_du_proto(chemin):
    """Le texte lisible d'un proto, balises retirées."""
    s = open(chemin, encoding='utf-8').read()
    s = re.sub(r'<(script|style)\b.*?</\1>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'[ \t ]+', ' ', s))


def enonces(chemin):
    """Les phrases chiffrées d'un proto, dans l'ordre."""
    out = []
    for bloc in texte_du_proto(chemin).split('\n'):
        for ph in gen.phraser(bloc.strip()):
            if len(ph) < 12:
                continue
            tetes = gen.lire_valeurs(ph)
            if not tetes or gen.est_une_date(tetes):
                continue
            out.append({'enonce': ph.strip(), 'valeurs': tetes})
    return out


# La normalisation des montants est celle du contrôle : « 37 059 M€ » et
# « 37,1 Md€ » sont le même montant.
ECHELLE = {'Md€': 1e9, 'Md€/an': 1e9, 'milliards': 1e9, 'M€': 1e6,
           'M€/an': 1e6, 'millions': 1e6, 'k€': 1e3, 'k€/an': 1e3}


# Deux chiffres ne se comparent que s'ils mesurent la même chose. La dimension
# est ce qui reste de l'unité une fois l'échelle retirée : « Md€ » et « M€ » ont
# la même, « €/an » et « €/mois » en ont deux.
DIMENSION = {'Md€': '€', 'M€': '€', 'k€': '€', 'milliards': '€',
             'millions': None, 'Md€/an': '€/an', 'M€/an': '€/an',
             'k€/an': '€/an'}


def cles(valeurs):
    """Les valeurs d'un énoncé, ramenées à l'échelle, en valeur absolue."""
    out = set()
    for v in valeurs:
        n = v.get('valeur_num') if isinstance(v, dict) else None
        if n is None:
            continue
        out.add(round(abs(float(n)) * ECHELLE.get(v.get('unite'), 1.0), 4))
    return out


def dimensions(valeurs):
    """Les dimensions présentes dans un énoncé, l'unité nue si inconnue."""
    out = set()
    for v in valeurs:
        u = v.get('unite') if isinstance(v, dict) else None
        if not u:
            continue
        d = DIMENSION.get(u, u)
        if d:
            out.add(d)
    return out


def valeurs_brutes(e):
    v = []
    if e.get('valeur_num') is not None:
        v.append({'valeur_num': e['valeur_num'], 'unite': e.get('unite')})
    for d in e.get('declinaisons') or []:
        if d.get('valeur_num') is not None:
            v.append({'valeur_num': d['valeur_num'], 'unite': d.get('unite')})
    return v


def valeurs_entree(e):
    v = []
    if e.get('valeur_num') is not None:
        v.append({'valeur_num': e['valeur_num'], 'unite': e.get('unite')})
    for d in e.get('declinaisons') or []:
        if d.get('valeur_num') is not None:
            v.append({'valeur_num': d['valeur_num'], 'unite': d.get('unite')})
    return cles(v)


def relever(chemin_ref, dst, protos):
    ref = json.load(open(chemin_ref, encoding='utf-8'))['entrees']
    index = [(e, valeurs_entree(e), mots((e.get('enonce') or '')
                                         + ' ' + (e.get('intitule') or '')),
              dimensions(valeurs_brutes(e)))
             for e in ref]

    lignes, compte = [], []
    collisions_tot = hors_tot = total = 0
    for chemin in protos:
        nom = chemin.rsplit('/', 1)[-1]
        items = enonces(chemin)
        collisions, hors = [], []
        for it in items:
            vals = cles(it['valeurs'])
            ms = mots(it['enonce'])
            dims = dimensions(it['valeurs'])
            partagees = {e['id'] for e, ve, _, _ in index if vals & ve}
            if not partagees:
                hors.append(it)
            for e, ve, me, de in index:
                communs = ms & me
                # Un énoncé long partage mécaniquement des mots avec tout le
                # monde. La part comptée est celle du plus petit des deux
                # vocabulaires : trois mots sur douze disent quelque chose,
                # trois mots sur soixante ne disent rien.
                part = len(communs) / max(1, min(len(ms), len(me)))
                if (len(communs) >= 3 and part >= 0.3 and (dims & de)
                        and not (vals & ve)):
                    collisions.append((it, e, sorted(communs)[:6],
                                       sorted(dims & de)))
        total += len(items)
        collisions_tot += len(collisions)
        hors_tot += len(hors)
        compte.append((nom, len(items), len(collisions), len(hors)))

        lignes.append(f"\n{'=' * 78}\n{nom} — {len(items)} énoncé(s) chiffré(s), "
                      f"{len(collisions)} collision(s), "
                      f"{len(hors)} hors référentiel\n{'=' * 78}")
        if collisions:
            lignes.append("\n-- COLLISIONS — mêmes mots, aucune valeur commune")
            for it, e, communs, dims in collisions:
                lignes.append(f"\n  proto  « {it['enonce'][:230]} »")
                lignes.append(f"  {e['id']:34s} « {(e.get('enonce') or '')[:170]} »")
                lignes.append(f"  mots communs : {', '.join(communs)}"
                              f"   ·   unité commune : {', '.join(dims)}")
        if hors:
            lignes.append("\n-- HORS RÉFÉRENTIEL — aucune valeur ne s'y retrouve")
            for it in hors:
                lignes.append(f"  « {it['enonce'][:200]} »")

    # -- la veille : les grandeurs publiables, cherchées par leurs mots
    alertes = []
    for chemin in protos:
        nom = chemin.rsplit('/', 1)[-1]
        for it in enonces(chemin):
            sansacc = it['enonce'].lower().translate(ACCENTS)
            for v in sources_chiffres.VEILLE:
                if not all(m in sansacc for m in v['mots']):
                    continue
                # Un appel de note et un millésime sont des nombres sans
                # être des chiffres. Un entier nu de moins de deux cents, ou
                # une année, ne déclenche pas d'alerte : les vrais chiffres
                # publiables portent une unité ou sortent de cette fenêtre.
                brutes = set()
                for x in it['valeurs']:
                    n = x.get('valeur_num')
                    if n is None:
                        continue
                    n = abs(float(n))
                    if not x.get('unite') and float(n).is_integer() and (
                            n <= 200 or 1900 <= n <= 2099):
                        continue
                    brutes.add(round(n, 4))
                admises = {round(abs(float(a)), 4)
                           for a in v['valeurs_admises']}
                if brutes and not (brutes & admises):
                    alertes.append((nom, v, it, sorted(brutes - admises)))
    if alertes:
        lignes.append(f"\n{'=' * 78}\nVEILLE — "
                      f"{len(alertes)} alerte(s) sur les grandeurs publiables"
                      f"\n{'=' * 78}")
        for nom, v, it, inconnues in alertes:
            lignes.append(f"\n  {nom}")
            lignes.append(f"  fait     « {v['fait']} »")
            lignes.append(f"  proto    « {it['enonce'][:230]} »")
            lignes.append(f"  valeurs hors admises : "
                          f"{', '.join(f'{x:g}' for x in inconnues)}")
            lignes.append(f"  {v['note']}")

    entete = [f"Relevé des chiffres des protos — {len(protos)} document(s), "
              f"{total} énoncé(s) chiffré(s)",
              f"{collisions_tot} collision(s) à lire, "
              f"{hors_tot} chiffre(s) qu'aucune entrée du référentiel ne porte",
              f"{len(alertes)} alerte(s) de veille sur les grandeurs publiables",
              "",
              "Ce relevé propose, il n'affirme pas. Un rapprochement s'écrit à la",
              "main dans sources_chiffres.MEME_QUE, jamais ici.",
              ""]
    for nom, n, c, h in compte:
        entete.append(f"  {nom:52s} {n:4d} chiffré · {c:3d} collision · "
                      f"{h:4d} hors référentiel")

    with open(dst, 'w', encoding='utf-8') as f:
        f.write('\n'.join(entete + lignes) + '\n')
    print('\n'.join(entete))
    print(f"\n{dst} écrit")
    return 0


if __name__ == '__main__':
    sys.exit(relever(sys.argv[1], sys.argv[2], sys.argv[3:]))
