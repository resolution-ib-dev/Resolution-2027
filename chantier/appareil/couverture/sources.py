# -*- coding: utf-8 -*-
"""Les entrées de la table de couverture : l'expert, le droit, nos pièces.

Le contrôle ne lit aucun fichier que ce module écrit : les quatre tables et le
droit viennent du dépôt de droit, les pièces du paquet (clause au coffre).
"""
import csv, gzip, json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REF = os.path.join(RACINE, 'referentiels')
PAQUET = os.path.join(RACINE, 'livrables', 'depot_2027')
sys.path.insert(0, '/home/claude/droit')
sys.path.insert(0, os.path.join(RACINE, 'appareil', 'fil0_regroupement'))
import droit                                                   # noqa
import designer as DES                                         # noqa

CGI = 'code général des impôts'
JOUR = '2026-10-07'

TABLES = {'ART': 'cgi_expert_articles.tsv', 'INS': 'cgi_expert_insertions.tsv',
          'SUP': 'cgi_expert_suppressions.tsv', 'PAR': 'cgi_expert_parametres.tsv'}


def _tsv(nom):
    with open(os.path.join(REF, nom), encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE))


def entree():
    """article -> opération de l'expert, en une ligne. 1 746 articles."""
    art = {x['article'].strip(): x for x in _tsv(TABLES['ART']) if x['article'].strip()}
    ins, sup, par = (set(x['article'].strip() for x in _tsv(TABLES[k]) if x['article'].strip())
                     for k in ('INS', 'SUP', 'PAR'))
    bouges = {x['article'].strip(): x for x in _tsv('cgi_expert_articles_bouges.tsv')
              if x['article'].strip()}
    out = {}
    for n, x in art.items():
        op = x['operation']
        det = []
        if n in ins: det.append('segments insérés')
        if n in sup: det.append('segments retirés')
        if n in par: det.append('paramètre')
        if x['car_final'] not in ('', '0'): det.append(f"{x['car_final']} car. finaux")
        out[n] = {'op_expert': op, 'detail_expert': ' · '.join(det),
                  'commente': x['commentaires'] not in ('', '0'),
                  'bouge': bouges.get(n, {}).get('etat', ''),
                  'tables': 'ART' + ('·INS' if n in ins else '') + ('·SUP' if n in sup else '')
                            + ('·PAR' if n in par else '')}
    for n, x in bouges.items():
        if n not in out:
            out[n] = {'op_expert': 'non porté par les quatre tables',
                      'detail_expert': '', 'commente': False,
                      'bouge': x['etat'], 'tables': 'BOUGES'}
    return out


def etat_droit(num):
    """L'état de l'article au millésime, sans jamais approcher."""
    try:
        a = droit.article(CGI, num, jour=JOUR)
    except (KeyError, FileNotFoundError):
        return 'CODE_NON_PORTE'
    except LookupError as e:
        m = str(e)
        if "absent de l'extrait" in m: return 'ABSENT'
        if 'entre en vigueur le' in m: return 'VIGUEUR_DIFF'
        return 'ABROGE'
    et = a.get('etat', '?')
    if et.startswith('ABROGE') and et.endswith('_DIFF'):
        return 'EXISTE_FIN_PROGRAMMEE'
    return 'EXISTE'


# ---------------------------------------------------------------- divisions
def divisions_cgi():
    """chemin de division -> articles qu'elle porte, version applicable au millésime.

    La version se prend comme `droit.article` la prend — celle qui s'applique au
    jour dit —, et non sur les enregistrements bruts : filtrer sur `date_fin`
    écartait les articles dont une version antérieure est close, donc des
    divisions entières, et cinq blocs regroupés sur six ne se résolvaient plus.
    """
    c = droit.resoudre_code(CGI)
    f = gzip.open(os.path.join('/home/claude/droit', 'data', c['court'] + '.jsonl.gz'),
                  'rt', encoding='utf-8')
    par_num = {}
    for l in f:
        d = json.loads(l)
        par_num.setdefault(d['num'], []).append(d)
    par_chemin = {}
    for num, vs in par_num.items():
        v = [x for x in vs if x['date_debut'] <= JOUR
             and (x['date_fin'] in droit.FIN_OUVERTE or x['date_fin'] > JOUR)]
        v = v[0] if v else max(vs, key=lambda x: x['date_debut'])
        ch = v.get('section') or ''
        els = ch.split(' > ')
        for i in range(1, len(els) + 1):
            par_chemin.setdefault(' > '.join(els[:i]), set()).add(num)
    return par_chemin


def designations():
    """désignation française -> articles, pour toute division du CGI."""
    out = {}
    for ch, arts in divisions_cgi().items():
        try:
            d = DES.designer(ch)
        except Exception:
            continue
        d = re.sub(r'^(?:Le |La |L’|le |la |l’)', '', d)
        if len(d) < 12:
            continue
        out.setdefault(d, set()).update(arts)
    return out
