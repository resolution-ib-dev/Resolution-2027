# -*- coding: utf-8 -*-
"""L'état de la machine à amendements, en deux grilles, zéro chiffre à la main.

Un état tenu à la main raconte au lieu de compter. Ce module porte donc **ce qui
s'écrit** — la liste des étapes, l'échelle des états, la capacité déclarée par
véhicule et par contexte — et **rien de ce qui se compte** : tous les nombres
sortent de `referentiels/lots_epreuve.json`, qui est le banc d'épreuve.

Un taux qu'aucun lot ne porte ne s'affiche pas. Une case vide est un résultat.

Usage : python3 etat_machine.py ../referentiels/lots_epreuve.json ../livrables/etat_machine.html
"""
import html
import json
import sys

# L'échelle des états. Une étape a un état, pas un pourcentage.
ECHELLE = [
    ('ecrite', 'écrite', 'la procédure existe, sous forme de document'),
    ('enregistree', 'enregistrée', 'elle est jouable telle quelle'),
    ('eprouvee', 'éprouvée', 'un taux a été mesuré sur un lot de référence'),
    ('generalisee', 'généralisée', 'aucune dépendance interne, aucun déposant nommé'),
    ('degradee', 'dégradée proprement', 'elle tourne socle absent et le déclare'),
]

VEHICULES = [('plf', 'loi de finances'),
             ('plfss', 'loi de financement'),
             ('ppl', 'proposition de loi'),
             ('pplo', 'loi organique'),
             ('pplc', 'révision')]

CONTEXTES = [('doctrine', 'doctrine interne disponible'),
             ('tiers', 'input d\'un tiers'),
             ('texte', 'documentation du texte chargée'),
             ('public', 'source publique seule')]

# Ce qui s'écrit à la main, et cela seul. Un état déclaré ici est une
# constatation sur pièce, jamais une intention.
#
#   lot     la clé du lot d'épreuve où lire le taux de l'étape, s'il y en a un
#   mesure  la clé de l'étape dans ce lot
ETAPES = [
    {'cle': 'E0', 'nom': 'Qualification',
     'porte': 'le statut de la mesure, et le levier',
     'etats': {'ecrite': True, 'enregistree': True, 'eprouvee': False,
               'generalisee': True, 'degradee': True},
     'lot': None, 'mesure': None,
     'vehicules': {'plf': 'ok', 'plfss': 'ok', 'ppl': 'ok', 'pplo': 'ok',
                   'pplc': 'ok'},
     'contextes': {'doctrine': 'ok', 'tiers': 'ok', 'texte': 'ok',
                   'public': 'ok'},
     'note': "Portée par l'étape 0 de la skill du vecteur. Sur la dépense "
             "locale, elle cherche les trois leviers — recette, dotation, "
             "norme — et dit lequel est portable dans le véhicule visé."},
    {'cle': 'E1', 'nom': 'Rattachement',
     'porte': 'la mesure peut-elle voyager dans ce véhicule',
     'etats': {'ecrite': True, 'enregistree': False, 'eprouvee': False,
               'generalisee': True, 'degradee': False},
     'lot': 'plf_2026_tiers', 'mesure': 'rattachement',
     'vehicules': {'plf': 'ok', 'plfss': 'porte corrigée', 'ppl': 'sans objet',
                   'pplo': 'sans objet', 'pplc': 'sans objet'},
     'contextes': {'doctrine': 'ok', 'tiers': 'ok', 'texte': 'ok',
                   'public': 'partiel'},
     'note': "Écrite et non outillée. C'est la dépendance la plus lourde : "
             "sans elle, la machine rédige des amendements irrecevables."},
    {'cle': 'E2', 'nom': 'Vecteur',
     'porte': "l'adresse de droit à modifier",
     'etats': {'ecrite': True, 'enregistree': True, 'eprouvee': True,
               'generalisee': True, 'degradee': True},
     'lot': 'plf_2026_tiers', 'mesure': 'vecteur',
     'vehicules': {'plf': 'mesuré', 'plfss': 'mesuré', 'ppl': 'déclaré',
                   'pplo': 'déclaré', 'pplc': 'déclaré'},
     'contextes': {'doctrine': 'ok', 'tiers': 'ok', 'texte': 'ok',
                   'public': 'mesuré'},
     'note': "Le seul taux mesuré en aveugle de toute la chaîne, et il l'a été "
             "socle absent : il se lit comme un plancher."},
    {'cle': 'E3', 'nom': 'Droit applicable',
     'porte': 'le texte en vigueur, et les renvois entrants',
     'etats': {'ecrite': True, 'enregistree': True, 'eprouvee': True,
               'generalisee': True, 'degradee': False},
     'lot': 'droit_applicable_20260902', 'mesure': 'droit_applicable',
     'vehicules': {'plf': 'ok', 'plfss': 'ok', 'ppl': 'ok', 'pplo': 'ok',
                   'pplc': 'partiel'},
     'contextes': {'doctrine': 'ok', 'tiers': 'ok', 'texte': 'ok',
                   'public': 'ok'},
     'note': "Vingt codes hors ligne. Ne dégrade pas proprement : sans le "
             "dépôt, l'étape ne rend rien — le verbatim ne se supplée pas de "
             "mémoire. Le droit non codifié n'est pas couvert."},
    {'cle': 'E4', 'nom': 'Rédaction cible',
     'porte': "le texte révisé de l'article — A + B = C",
     'etats': {'ecrite': False, 'enregistree': False, 'eprouvee': False,
               'generalisee': False, 'degradee': False},
     'lot': 'plf_2026_tiers', 'mesure': 'disposition',
     'vehicules': {'plf': '—', 'plfss': '—', 'ppl': '—', 'pplo': '—',
                   'pplc': '—'},
     'contextes': {'doctrine': '—', 'tiers': '—', 'texte': '—', 'public': '—'},
     'note': "La case vide qui bloque la chaîne. Elle a son prompt. Le signe "
             "« = » du trois colonnes : elle rend le texte tel qu'il sera, et "
             "la forme modificative s'en dérive. Les crédits n'en relèvent pas."},
    {'cle': 'E5', 'nom': 'Exposé sommaire',
     'porte': "l'exposé en trois temps, et les renvois signalés",
     'etats': {'ecrite': True, 'enregistree': True, 'eprouvee': False,
               'generalisee': True, 'degradee': True},
     'lot': 'plf_2026_tiers', 'mesure': 'expose_sommaire',
     'vehicules': {'plf': 'ok', 'plfss': 'ok', 'ppl': 'hors capacité',
                   'pplo': 'hors capacité', 'pplc': 'hors capacité'},
     'contextes': {'doctrine': 'ok', 'tiers': 'ok', 'texte': 'ok',
                   'public': 'ok'},
     'note': "Quatre gisements de sources, cumulatifs. Éval inverse écrite, "
             "non jouée : la forme est comptée, les sources ne le sont pas. "
             "L'exposé des motifs d'une proposition de loi est un autre objet."},
    {'cle': 'E6', 'nom': 'Contrôles de sortie',
     'porte': 'forme, généralisation, registre',
     'etats': {'ecrite': True, 'enregistree': True, 'eprouvee': False,
               'generalisee': True, 'degradee': True},
     'lot': None, 'mesure': None,
     'vehicules': {'plf': 'partiel', 'plfss': 'partiel', 'ppl': 'partiel',
                   'pplo': 'partiel', 'pplc': 'partiel'},
     'contextes': {'doctrine': 'ok', 'tiers': 'ok', 'texte': 'ok',
                   'public': 'ok'},
     'note': "La généralisation est mécanique depuis le 20260902. La forme "
             "l'est. Le registre ne l'est pas encore : le jeu de règles en "
             "vigueur est calibré sur un autre registre que celui de la séance."},
    {'cle': 'E7', 'nom': 'Liasse',
     'porte': 'assemblage, ordre de dépôt, chutes',
     'etats': {'ecrite': False, 'enregistree': False, 'eprouvee': False,
               'generalisee': False, 'degradee': False},
     'lot': None, 'mesure': None,
     'vehicules': {'plf': '—', 'plfss': '—', 'ppl': '—', 'pplo': '—',
                   'pplc': '—'},
     'contextes': {'doctrine': '—', 'tiers': '—', 'texte': '—', 'public': '—'},
     'note': "N'existe pas. Sa dernière colonne — quelles pièces tombent si une "
             "autre est adoptée — est de la stratégie parlementaire et revient "
             "à l'auteur."},
]

CLASSES = {'ok': 'oui', 'mesuré': 'mes', 'mesure': 'mes', 'déclaré': 'dec',
           'partiel': 'par', 'porte corrigée': 'par', 'sans objet': 'so',
           'hors capacité': 'hc', '—': 'vide'}

CSS = """
:root{--encre:#171410;--papier:#fbf7ef;--trait:#d9cfbe;--ocre:#b8862a;
--rouge:#a8321c;--vert:#1f4d3a;--gris:#6d6a64}
*{box-sizing:border-box}
body{margin:0;background:var(--papier);color:var(--encre);
font:15px/1.55 Fraunces,"Iowan Old Style",Georgia,serif}
.page{max-width:1120px;margin:0 auto;padding:48px 28px 72px}
h1{font-size:1.9rem;line-height:1.15;margin:0 0 .2em;letter-spacing:-.01em}
h2{font-size:1.1rem;margin:2.6em 0 .5em;text-transform:uppercase;
letter-spacing:.13em;font-weight:700}
h2::after{content:"";display:block;height:3px;width:120px;margin-top:.5em;
background:linear-gradient(90deg,var(--vert) 0 33%,var(--ocre) 33% 66%,
var(--rouge) 66% 100%)}
.chapeau{color:var(--gris);max-width:62ch;margin:0 0 .4em}
.mono{font-family:"JetBrains Mono",ui-monospace,Menlo,Consolas,monospace}
table{border-collapse:collapse;width:100%;margin:.8em 0 .4em;font-size:.86rem}
th,td{border:1px solid var(--trait);padding:7px 9px;text-align:left;
vertical-align:top}
thead th{background:#f2ebdd;font-size:.72rem;text-transform:uppercase;
letter-spacing:.08em;font-weight:700}
td.cle{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:700;
white-space:nowrap}
td.c{text-align:center;font-size:.78rem;white-space:nowrap}
.oui{background:#e6efe8;color:var(--vert);font-weight:700}
.mes{background:#efe6d2;color:var(--ocre);font-weight:700}
.dec{color:var(--gris)}
.par{background:#f6ecd9;color:#8a6a1f}
.so{color:var(--gris);font-style:italic}
.hc{background:#f5e2de;color:var(--rouge)}
.vide{color:#c3bcae}
.note{font-size:.82rem;color:var(--gris)}
.taux{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:700;
color:var(--rouge)}
.legende{font-size:.8rem;color:var(--gris);margin-top:.6em}
.legende span{display:inline-block;margin-right:1.2em}
.pied{margin-top:3em;padding-top:1em;border-top:1px solid var(--trait);
font-size:.8rem;color:var(--gris)}
.wrap{overflow-x:auto}
"""


def _taux(lots, cle_lot, cle_etape):
    """La dernière mesure jouée sur cette étape, ou None. Aucun calcul."""
    if not cle_lot or not cle_etape:
        return None
    lot = next((l for l in lots['lots'] if l['cle'] == cle_lot), None)
    if lot is None:
        return None
    e = lot['etapes'].get(cle_etape)
    if not e or not e.get('mesures'):
        return None, e
    return _derniere(e['mesures']), e


def _derniere(mesures):
    """La mesure la plus récente d'une étape.

    Le banc écrit `mesures` de deux façons, et les deux sont légitimes : une
    **liste**, quand l'étape a été jouée plusieurs fois et que la suite compte —
    c'est le cas du vecteur —, et un **objet unique**, quand une seule mesure
    porte tous ses critères d'un coup, comme la rédaction cible. Ce générateur
    ne lisait que la liste et levait sur l'objet : depuis le 20260904, l'état de
    la machine ne se régénérait plus, et rien ne le disait — c'est le défaut que
    A-364 avait déjà relevé sur la carte, à un autre endroit.
    """
    return mesures[-1] if isinstance(mesures, list) else mesures


def _mesures_par_vehicule(lots, cle_etape):
    """Pour chaque véhicule, la dernière mesure de cette étape, s'il y en a."""
    par = {}
    for lot in lots['lots']:
        e = lot['etapes'].get(cle_etape)
        if e and e.get('mesures'):
            par.setdefault(lot['vehicule'], []).append(
                (lot, _derniere(e['mesures'])))
    return par


def rendre(lots):
    e = html.escape
    o = ['<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         '<title>État de la machine à amendements</title>',
         f'<style>{CSS}</style></head><body><div class="page">']
    o.append('<h1>État de la machine à amendements</h1>')
    o.append('<p class="chapeau">Une étape a un état, pas un pourcentage. '
             'Ce qui se compte ici sort du banc d\'épreuve ; ce qu\'aucun lot '
             'ne porte reste vide, et une case vide est un résultat.</p>')

    # --- grille 1 : étapes × état
    o.append('<h2>Les étapes et leur état</h2>')
    o.append('<div class="wrap"><table><thead><tr><th>étape</th><th>ce qu\'elle rend</th>')
    for _, nom, _ in ECHELLE:
        o.append(f'<th>{e(nom)}</th>')
    o.append('<th>mesuré</th></tr></thead><tbody>')
    for et in ETAPES:
        o.append(f'<tr><td class="cle">{e(et["cle"])} {e(et["nom"])}</td>'
                 f'<td>{e(et["porte"])}<div class="note">{e(et["note"])}</div></td>')
        for k, _, _ in ECHELLE:
            v = et['etats'].get(k)
            o.append(f'<td class="c {"oui" if v else "vide"}">'
                     f'{"oui" if v else "—"}</td>')
        m = _taux(lots, et['lot'], et['mesure'])
        cellule = '—'
        if m and m[0]:
            mes, bloc = m
            if 'taux' in mes:
                pop = bloc.get('population_notee')
                cellule = (f'<span class="taux">{mes["taux"]*100:.1f} %</span>'
                           f'<div class="note">{mes["concordance"]}/{pop} · '
                           f'{e(bloc.get("degradation",""))}'
                           + ('' if mes.get('comparable', True)
                              else ' · non comparable') + '</div>')
            elif 'mediane_mots' in mes:
                cellule = (f'<span class="taux">{mes["dans_la_fourchette"]}'
                           f'/{bloc["population_notee"]}</span>'
                           f'<div class="note">forme ; sources non éprouvées</div>')
            elif 'amendements_visant_du_texte_a_abrogation_programmee' in mes:
                n = mes['amendements_visant_du_texte_a_abrogation_programmee']
                cellule = (f'<span class="taux">{n}</span><div class="note">'
                           f'pièces visant du texte à abrogation programmée '
                           f'sur {bloc["population_notee"]} adresses</div>')
        elif m and m[1] is not None:
            cellule = '<span class="vide">non joué</span>'
        o.append(f'<td class="c">{cellule}</td>')
        o.append('</tr>')
    o.append('</tbody></table></div>')
    o.append('<p class="legende">'
             + ' '.join(f'<span><b>{e(n)}</b> — {e(d)}</span>'
                        for _, n, d in ECHELLE) + '</p>')

    # --- grille 2 : étapes × véhicules et contextes
    o.append('<h2>Les étapes, les véhicules et les contextes</h2>')
    o.append('<p class="chapeau">Le véhicule est une donnée du dossier, jamais '
             'une hypothèse d\'étape : une étape qui ne sait pas traiter un '
             'véhicule le déclare et s\'arrête. Le contexte dit de quels '
             'gisements l\'étape disposait.</p>')
    o.append('<div class="wrap"><table><thead><tr><th>étape</th>')
    for _, nom in VEHICULES:
        o.append(f'<th>{e(nom)}</th>')
    for _, nom in CONTEXTES:
        o.append(f'<th>{e(nom)}</th>')
    o.append('</tr></thead><tbody>')
    for et in ETAPES:
        o.append(f'<tr><td class="cle">{e(et["cle"])} {e(et["nom"])}</td>')
        mesures = _mesures_par_vehicule(lots, et['mesure']) if et['mesure'] else {}
        for k, _ in VEHICULES:
            v = et['vehicules'].get(k, '—')
            sup = ''
            for lot, mes in mesures.get(k, []):
                if 'taux' in mes:
                    sup = (f'<div class="note">{mes["taux"]*100:.0f} % · '
                           f'{lot["etapes"][et["mesure"]]["population_notee"]} cas</div>')
            o.append(f'<td class="c {CLASSES.get(v,"dec")}">{e(v)}{sup}</td>')
        for k, _ in CONTEXTES:
            v = et['contextes'].get(k, '—')
            o.append(f'<td class="c {CLASSES.get(v,"dec")}">{e(v)}</td>')
        o.append('</tr>')
    o.append('</tbody></table></div>')

    # --- les lots, tels qu'ils sont
    o.append('<h2>Le banc d\'épreuve</h2>')
    o.append('<div class="wrap"><table><thead><tr><th>lot</th><th>véhicule</th>'
             '<th>unité</th><th>population</th><th>contaminés</th>'
             '<th>étapes jouées</th></tr></thead><tbody>')
    for lot in lots['lots']:
        pop = ' · '.join(
            f'{v} {k}' if not isinstance(v, dict)
            else k + ' ' + ', '.join(f'{a} {b}' for b, a in v.items())
            for k, v in lot['population'].items())
        jouees = [k for k, v in lot['etapes'].items() if v.get('mesures')]
        # Un lot peut ne déclarer aucun contaminé et ne pas porter la clé du
        # tout — c'est le cas du lot du droit applicable, dont l'unité est
        # l'adresse. Une case vide est un résultat, et elle ne lève pas.
        cont = lot.get('contamines', [])
        o.append(f'<tr><td class="cle">{e(lot["cle"])}</td>'
                 f'<td>{e(lot["vehicule"])}</td>'
                 f'<td>{e(lot.get("unite", "—"))}</td>'
                 f'<td>{e(pop)}</td>'
                 f'<td class="c">{len(cont)}</td>'
                 f'<td>{e(", ".join(jouees)) or "—"}</td></tr>')
    for v in lots['vehicules_sans_lot']:
        o.append(f'<tr><td class="cle vide">aucun</td><td>{e(v["vehicule"])}</td>'
                 f'<td colspan="4" class="note">{e(v["note"])}</td></tr>')
    o.append('</tbody></table></div>')

    o.append('<div class="pied">Généré depuis le banc d\'épreuve. Aucun chiffre '
             'n\'est saisi ici : une correction se porte au référentiel des '
             'lots, et la page se régénère.</div>')
    o.append('</div></body></html>')
    return '\n'.join(o)


def main(argv):
    lots = json.load(open(argv[1], encoding='utf-8'))
    page = rendre(lots)
    with open(argv[2], 'w', encoding='utf-8') as f:
        f.write(page)
    joues = sum(1 for lot in lots['lots'] for v in lot['etapes'].values()
                if v.get('mesures'))
    print(f'{argv[2]} écrit — {len(ETAPES)} étapes, {len(lots["lots"])} lots, '
          f'{joues} étape(s) mesurée(s), {len(page)} octets')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
