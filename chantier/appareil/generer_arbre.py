#!/usr/bin/env python3
"""Génère l'arbre de lecture du REF_doctrine.

Rejouable à chaque versement du REF. Aucune valeur n'est écrite à la main :
tout est projeté depuis le JSON, et les écarts consignés sont lus de la sortie
de `controle_arithmetique.py`.

La génération est elle-même un contrôle. Trois vérifications sont produites sur
la sortie standard et reportées en pied de l'arbre :

  T1  couverture du schéma — toute clé présente au JSON est rendue ou écartée
      nommément ; toute clé attendue par le générateur est présente au JSON
  T2  intégrité des renvois — depend, renvois, emplois du lexique, nœuds des
      règles transversales et des mécanismes pointent vers une cible existante
  T3  compteurs — confrontés à ceux du contrôle structurel

Usage : python3 generer_arbre.py REF_doctrine.json sortie.html
"""

import html
import json
import re
import subprocess
import sys

# --------------------------------------------------------------------- attendu
# Compteurs opposables, tenus par `controle_structurel.py`.
ATTENDU = {'entrees': 154, 'peuplees': 66, 'propositions': 56, 'axes': 12,
           'leviers': 45, 'lexique': 9, 'mecanismes': 11, 'effets_normatifs': 59}

# Clés consommées par le générateur, par conteneur. Toute clé du JSON absente de
# ces listes est signalée en T1 comme perdue en silence.
CONSOMMEES = {
    'racine': {'axes', '_revision', 'lexique', 'regles_transversales',
               'couverture_normative', 'complements_normatifs'},
    'axe': {'id', 'intitule', 'leviers', 'complements_constitutionnels',
            'gains_indirects', 'effets_diagnostic'},
    'levier': {'id', 'intitule', 'propositions', 'complements_constitutionnels'},
    'proposition': {'id', 'ancre', 'intitule', 'domaine', 'strate', 'statut',
                    'droit_existant', 'sources', 'ne_fait_pas', 'parametres',
                    'effets', 'membres', 'verbe', 'sous_items',
                    'ancrage_doctrinal', 'renvois', 'complements_constitutionnels',
                    'lacunes'},
    'entree': {'id', 'nom', 'valeur', 'unite', 'variable', 'bornes', 'date_effet',
               'ids', 'enonce', 'signe', 'beneficiaire', 'chiffre', 'horizon',
               'certitude', 'attenuation', 'depend', 'ancre', 'note_diffusion',
               'origine', 'base', 'portee', 'sens', 'operation', 'exact',
               'verdict', 'chaine', 'statut_ancre', 'source_ancre', 'conditions',
               'nature'},
    'chainon': {'composant', 'valeur', 'base', 'origine', 'statut'},
    'sous_item': {'id', 'intitule', 'chiffre', 'hypothese', 'renvois'},
    'renvoi': {'vers', 'motif'},
    'complement_c': {'id', 'intitule', 'article', 'verbe', 'inspiration', 'niveau'},
    'terme': {'terme', 'definition', 'statut_ancre', 'source_ancre', 'variantes',
              'verdict', 'lacune', 'emplois', 'regle', 'correction_manuscrit',
              'branches', 'illustrations'},
    'rt': {'id', 'intitule', 'enonce', 'statut_ancre', 'source_ancre', 'nature',
           'elements_presents_au_manuscrit', 'ce_qui_manque', 'corollaire',
           'noeuds', 'strates', 'verdict', 'construction', 'complements_normatifs'},
    'complements_normatifs': {'objet', 'sources', 'nomenclature_strates',
                              'synthese', 'principe', 'mecanismes'},
    'mecanisme': {'id', 'intitule', 'effets', 'noeuds_rattaches'},
    'effet_normatif': {'id', 'effet', 'siege_constitutionnel',
                       'droit_en_vigueur_deplace', 'voie_basse', 'fondement',
                       'strate_atteignable'},
}

# Clés rendues nulle part et écartées à dessein. Vide : tout est rendu.
ECARTEES = {}

T1, T2 = [], []


def t1(conteneur, obj):
    """Confronte les clés d'un objet à celles que le générateur consomme."""
    ref = CONSOMMEES[conteneur]
    for k in obj:
        if k not in ref and (conteneur, k) not in ECARTEES:
            T1.append(f'{conteneur} : clé « {k} » présente au JSON, non rendue')


def e(x):
    return html.escape(str(x)) if x is not None else ''


def txt(x):
    """Rend une valeur scalaire ou une liste de scalaires."""
    if isinstance(x, list):
        return ' · '.join(e(v) for v in x)
    return e(x)


# ============================================================ chargement
def charger(path):
    d = json.load(open(path, encoding='utf-8'))
    t1('racine', d)
    return d


def indexer(d):
    """Index des cibles de renvoi : propositions, entrées, termes, mécanismes."""
    idx = {'prop': {}, 'entree': {}, 'terme': {}, 'meca': {}, 'effet_n': {},
           'axe': {}, 'levier': {}}
    for a in d['axes']:
        idx['axe'][a['id']] = a
        for l in a['leviers']:
            idx['levier'][l['id']] = l
            for p in l['propositions']:
                idx['prop'][p['id']] = p
                for x in p['parametres'] + p['effets']:
                    idx['entree'][x['id']] = x
    for t in d['lexique']:
        idx['terme'][t['terme']] = t
    for m in d['complements_normatifs']['mecanismes']:
        idx['meca'][m['id']] = m
        for f in m['effets']:
            idx['effet_n'][f['id']] = f
    return idx


ANCRAGES = (('entree', 'e-'), ('prop', 'p-'), ('levier', 'l-'), ('axe', 'a-'),
            ('meca', 'm-'), ('effet_n', 'fn-'))
ID_TETE = re.compile(r'^\s*(?:Ancrage\s*:\s*)?(D\d+(?:-\d+)*(?:-[pes]\d+)?|M\d+(?:\.\d+)?)\b')


def _ancre(cible, idx):
    for cle, prefixe in ANCRAGES:
        if cible in idx[cle]:
            return prefixe + cible
    return None


def lien(cible, idx, ctx=''):
    """Lien interne vérifié.

    Un renvoi conforme donne un lien. Un renvoi qui mêle la cible et son motif
    dans une même chaîne est signalé en T2 comme non normalisé, la cible étant
    tout de même liée. Une cible inexistante est signalée et rendue en clair.
    """
    a = _ancre(cible, idx)
    if a:
        return f'<a href="#{e(a)}">{e(cible)}</a>'
    m = ID_TETE.match(cible)
    if m and _ancre(m.group(1), idx):
        tete = m.group(1)
        T2.append(f'renvoi non normalisé{ctx} : cible « {tete} » noyée dans « {cible[:70]} »')
        reste = cible[m.end():].lstrip(' :;,—-')
        return (f'<a href="#{e(_ancre(tete, idx))}">{e(tete)}</a> '
                f'<span class="nn">{e(reste)}</span>')
    T2.append(f'renvoi mort{ctx} : « {cible[:70]} »')
    return f'<span class="mort">{e(cible)} — cible inexistante</span>'


# ============================================================ écarts consignés
def lire_ecarts(script='controle_arithmetique.py'):
    """Écarts consignés, lus de la sortie du contrôle arithmétique."""
    try:
        r = subprocess.run([sys.executable, script], capture_output=True,
                           text=True, timeout=120)
    except Exception as exc:
        return [], f'contrôle arithmétique injouable : {exc}'
    lignes = []
    for ln in r.stdout.splitlines():
        m = re.match(r'^CSG (\S+)\s+(.+?)\s{2,}(-?[\d.]+)\s*(\S*)$', ln)
        if m:
            lignes.append(m.groups())
    fin = [ln for ln in r.stdout.splitlines() if 'écart(s) consigné' in ln]
    return lignes, (fin[0].strip() if fin else '')


# ============================================================ rendu — entrées
BADGES = {
    'statut_ancre': {
        'manuscrit': ('ok', 'ancre du manuscrit — prévaut sur toute autre valeur'),
        'implicite au manuscrit': ('ok', 'implicite au manuscrit — démontré sans être énoncé'),
        'classeur': ('att', 'valeur de classeur — à déclarer comme telle en emploi externe'),
        'absent des deux': ('int', 'absent du manuscrit et du classeur — NON DIFFUSABLE'),
    },
    'nature': {
        'règle générale': ('ok', 'règle générale — se propage telle quelle'),
        'illustration': ('att', 'illustration — vaut pour le cas nommé, ne se propage jamais comme règle'),
        'agrégat': ('neu', 'agrégat — somme, sans destinataire individuel'),
        'hypothèse': ('att', 'hypothèse — paramètre de calcul déclaré, non un engagement'),
    },
}


def badge(champ, valeur):
    cls, libelle = BADGES[champ].get(valeur, ('int', f'{valeur} — valeur hors nomenclature'))
    if valeur not in BADGES[champ]:
        T1.append(f'{champ} : valeur « {valeur} » hors nomenclature du générateur')
    return f'<span class="b b-{cls}">{e(libelle)}</span>'


def rendre_entree(x, kind, idx):
    t1('entree', x)
    eid = x['id']
    o = []
    peuplee = 'verdict' in x
    titre = x.get('nom') or x.get('enonce') or ''
    classe = 'ent' + ('' if peuplee else ' vide')
    marque_vide = ('' if peuplee else
                   ' <span class="b b-neu">non peuplée — hors grille de référence</span>')
    o.append(f'<div class="{classe}" id="e-{e(eid)}">')
    o.append(f'<p class="eid"><code>{e(eid)}</code> <span class="kind">{kind}</span>'
             f'{marque_vide}</p>')
    if titre:
        o.append(f'<p class="titre">{e(titre)}</p>')

    # --- valeur affichée contre valeur exacte, distinctes visuellement
    aff = x.get('valeur') or x.get('ancre') or x.get('chiffre') or ''
    if aff:
        o.append(f'<p class="aff"><span class="et">affiché</span> {e(aff)}</p>')
    if x.get('ancre') and x.get('valeur'):
        o.append(f'<p class="aff"><span class="et">ancre</span> {e(x["ancre"])}</p>')
    if peuplee:
        o.append(f'<p class="exa"><span class="et">exact</span> {e(x["exact"])}</p>')

    if peuplee:
        o.append('<p class="badges">' + badge('statut_ancre', x['statut_ancre'])
                 + ' ' + badge('nature', x['nature']) + '</p>')
        o.append(f'<p class="src"><span class="et">source de l’ancre</span> {e(x["source_ancre"])}</p>')
        o.append(f'<p class="verd"><span class="et">verdict</span> {e(x["verdict"])}</p>')

        # --- conditions littérales, jamais repliées
        if x['conditions']:
            o.append('<div class="cond"><p class="et">conditions littérales</p><ul>')
            o += [f'<li>{e(c)}</li>' for c in x['conditions']]
            o.append('</ul></div>')
        else:
            o.append('<p class="cond vide">aucune condition littérale attachée</p>')

        # --- appareil
        o.append('<dl class="app">')
        for k, lib in (('origine', 'origine'), ('base', 'base'), ('portee', 'portée'),
                       ('sens', 'sens'), ('operation', 'opération')):
            o.append(f'<dt>{lib}</dt><dd>{e(x[k])}</dd>')
        o.append('</dl>')

        # --- chaîne
        o.append('<table class="ch"><caption>chaîne de constitution</caption>'
                 '<tr><th>composant</th><th>valeur</th><th>base</th>'
                 '<th>origine</th><th>statut</th></tr>')
        for c in x['chaine']:
            t1('chainon', c)
            st = c['statut']
            if st not in ('relevé', 'reconstitué'):
                T1.append(f'chaine.statut : valeur « {st} » hors nomenclature')
            cls_st = 'r' if st == 'relevé' else 'x'
            o.append(f'<tr><td>{e(c["composant"])}</td><td>{e(c["valeur"])}</td>'
                     f'<td>{e(c["base"])}</td><td>{e(c["origine"])}</td>'
                     f'<td class="st-{cls_st}">{e(st)}</td></tr>')
        o.append('</table>')

    # --- propriétés de forme, selon paramètre ou effet
    autres = []
    for k, lib in (('unite', 'unité'), ('variable', 'variable'), ('bornes', 'bornes'),
                   ('date_effet', 'date d’effet'), ('signe', 'signe'),
                   ('beneficiaire', 'bénéficiaire'), ('chiffre', 'chiffre'),
                   ('horizon', 'horizon'), ('certitude', 'certitude'),
                   ('attenuation', 'atténuation'), ('note_diffusion', 'note de diffusion')):
        if x.get(k):
            autres.append(f'<dt>{lib}</dt><dd>{e(x[k])}</dd>')
    if autres:
        o.append('<dl class="frm">' + ''.join(autres) + '</dl>')

    liens = []
    if x.get('depend'):
        liens.append('dépend de ' + ', '.join(lien(v, idx, f' [depend de {eid}]') for v in x['depend']))
    if x.get('ids'):
        liens.append('marqueurs manuscrit ' + txt(x['ids']))
    if liens:
        o.append('<p class="ln">' + ' — '.join(liens) + '</p>')
    o.append('</div>')
    return '\n'.join(o)


# ============================================================ rendu — propositions
def rendre_proposition(p, idx, meca_par_noeud):
    t1('proposition', p)
    pid = p['id']
    o = [f'<details class="prop" id="p-{e(pid)}"><summary><code>{e(pid)}</code> '
         f'<b>{e(p["verbe"])} {e(p["intitule"])}</b> '
         f'<span class="meta">{e(p["domaine"])} · strate {e(p["strate"])} · {e(p["statut"])}</span>'
         f'</summary>']
    if p.get('ancre'):
        o.append(f'<p class="aff"><span class="et">ancre</span> {e(p["ancre"])}</p>')
    for k, lib in (('droit_existant', 'droit existant'), ('ne_fait_pas', 'ne fait pas'),
                   ('sources', 'sources')):
        if p.get(k):
            o.append(f'<p class="pmeta"><span class="et">{lib}</span> {e(p[k])}</p>')
    if p.get('membres'):
        o.append(f'<p class="pmeta"><span class="et">marqueurs manuscrit</span> {txt(p["membres"])}</p>')
    if p.get('ancrage_doctrinal'):
        o.append(f'<p class="pmeta"><span class="et">ancrage doctrinal</span> {txt(p["ancrage_doctrinal"])}</p>')

    if p.get('renvois'):
        items = []
        for r in p['renvois']:
            t1('renvoi', r)
            items.append(f'<li>{lien(r["vers"], idx, f" [renvoi de {pid}]")} — {e(r["motif"])}</li>')
        o.append('<div class="ren"><p class="et">renvois</p><ul>' + ''.join(items) + '</ul></div>')

    if p.get('sous_items'):
        items = []
        for s in p['sous_items']:
            t1('sous_item', s)
            rv = ''
            if s['renvois']:
                ctx = f' [sous-item {s["id"]}]'
                parts = []
                for r in s['renvois']:
                    t1('renvoi', r)
                    m = e(r['motif'])
                    parts.append(lien(r['vers'], idx, ctx) + (f' — {m}' if m else ''))
                rv = ' — renvois ' + ', '.join(parts)
            items.append(f'<li><code>{e(s["id"])}</code> {e(s["intitule"])} '
                         f'<span class="meta">{e(s["chiffre"])} · {e(s["hypothese"])}</span>{rv}</li>')
        o.append('<div class="ren"><p class="et">sous-items</p><ul>' + ''.join(items) + '</ul></div>')

    o.append(rendre_complements_c(p['complements_constitutionnels'], 'proposition'))

    if pid in meca_par_noeud:
        o.append('<p class="pmeta"><span class="et">mécanismes normatifs rattachés</span> '
                 + ', '.join(f'{lien(m, idx, f" [proposition {pid}]")} {e(idx["meca"][m]["intitule"])}'
                             for m in meca_par_noeud[pid]) + '</p>')

    if p.get('lacunes'):
        o.append('<div class="lac"><p class="et">lacunes</p><ul>'
                 + ''.join(f'<li>{e(x)}</li>' for x in p['lacunes']) + '</ul></div>')

    for lib, coll, kind in (('paramètres', p['parametres'], 'paramètre'),
                            ('effets', p['effets'], 'effet')):
        if coll:
            o.append(f'<h5>{lib} — {len(coll)}</h5>')
            o += [rendre_entree(x, kind, idx) for x in coll]
    o.append('</details>')
    return '\n'.join(o)


def rendre_complements_c(coll, niveau):
    if not coll:
        return ''
    items = []
    for c in coll:
        t1('complement_c', c)
        items.append(f'<li><code>{e(c["id"])}</code> {e(c["verbe"])} — <b>{e(c["intitule"])}</b> '
                     f'<span class="meta">{e(c["article"])} · {e(c["niveau"])}</span>'
                     f'<br><span class="insp">{e(c["inspiration"])}</span></li>')
    return (f'<div class="cc"><p class="et">compléments constitutionnels — {niveau}</p>'
            '<ul>' + ''.join(items) + '</ul></div>')


def rendre_registre_axe(items, titre, kind, idx):
    if not items:
        return ''
    o = [f'<details class="reg"><summary>{titre} — {len(items)}</summary>']
    o += [rendre_entree(x, kind, idx) for x in items]
    o.append('</details>')
    return '\n'.join(o)


# ============================================================ blocs transversaux
def rendre_lexique(d, idx):
    o = [f'<h2 id="lexique">Lexique — {len(d["lexique"])} termes</h2>']
    for t in d['lexique']:
        t1('terme', t)
        o.append(f'<details class="prop" id="lex-{e(t["terme"].replace(" ", "-"))}">'
                 f'<summary><b>{e(t["terme"])}</b> <span class="meta">{e(t["verdict"])}</span></summary>')
        o.append(f'<p>{e(t["definition"])}</p>')
        o.append('<p class="badges">' + badge('statut_ancre', t['statut_ancre']) + '</p>')
        o.append(f'<p class="src"><span class="et">source de l’ancre</span> {e(t["source_ancre"])}</p>')
        o.append(f'<p class="pmeta"><span class="et">variantes admises</span> '
                 f'{txt(t["variantes"]) or "aucune"}</p>')
        o.append(f'<p class="pmeta"><span class="et">règle de variation</span> '
                 f'{e(t.get("regle")) or "<i>non écrite</i>"}</p>')
        o.append('<p class="pmeta"><span class="et">emplois</span> '
                 + (', '.join(lien(v, idx, f' [lexique {t["terme"]}]') for v in t['emplois']) or 'aucun') + '</p>')
        if t.get('lacune'):
            o.append(f'<div class="lac"><p class="et">lacune</p><p>{e(t["lacune"])}</p></div>')
        if t.get('correction_manuscrit'):
            o.append(f'<div class="lac"><p class="et">correction au manuscrit</p>'
                     f'<p>{e(t["correction_manuscrit"])}</p></div>')
        if t.get('branches'):
            o.append('<table class="ch"><caption>branches</caption>'
                     '<tr><th>branche</th><th>support</th><th>chiffre</th><th>nœuds</th></tr>')
            for b in t['branches']:
                o.append(f'<tr><td>{e(b["branche"])}</td><td>{e(b["support"])}</td>'
                         f'<td>{e(b["chiffre"])}</td>'
                         f'<td>{", ".join(lien(v, idx, " [lexique branches]") for v in b["noeuds"])}</td></tr>')
            o.append('</table>')
        if t.get('illustrations'):
            o.append('<table class="ch"><caption>illustrations d’usage — ne se propagent pas comme règles</caption>'
                     '<tr><th>usage</th><th>receveur</th><th>valeur</th><th>nœud</th></tr>')
            for i in t['illustrations']:
                o.append(f'<tr><td>{e(i["usage"])}</td><td>{e(i["receveur"])}</td>'
                         f'<td>{e(i["valeur"])}</td><td>{lien(i["noeud"], idx, " [lexique illustrations]")}</td></tr>')
            o.append('</table>')
        o.append('</details>')
    return '\n'.join(o)


def rendre_rt(d, idx):
    o = [f'<h2 id="rt">Règles transversales — {len(d["regles_transversales"])}</h2>']
    for r in d['regles_transversales']:
        t1('rt', r)
        o.append(f'<details class="prop" id="rt-{e(r["id"])}" open>'
                 f'<summary><code>{e(r["id"])}</code> <b>{e(r["intitule"])}</b> '
                 f'<span class="meta">{e(r["verdict"])}</span></summary>')
        o.append(f'<p>{e(r["enonce"])}</p>')
        o.append('<p class="badges">' + badge('statut_ancre', r['statut_ancre'])
                 + ' ' + badge('nature', r['nature']) + '</p>')
        o.append(f'<p class="src"><span class="et">source de l’ancre</span> {e(r["source_ancre"])}</p>')
        o.append(f'<p class="pmeta"><span class="et">construction</span> {e(r["construction"])}</p>')
        if r['elements_presents_au_manuscrit']:
            o.append('<div class="cond"><p class="et">démonstration citée au manuscrit</p><ul>'
                     + ''.join(f'<li>{e(x)}</li>' for x in r['elements_presents_au_manuscrit'])
                     + '</ul></div>')
        o.append(f'<p class="pmeta"><span class="et">ce qui manque</span> '
                 f'{e(r["ce_qui_manque"]) or "rien"}</p>')
        o.append(f'<p class="pmeta"><span class="et">corollaire</span> {e(r["corollaire"])}</p>')
        o.append('<p class="pmeta"><span class="et">nœuds</span> '
                 + ', '.join(lien(v, idx, f' [{r["id"]} noeuds]') for v in r['noeuds']) + '</p>')
        o.append(f'<p class="pmeta"><span class="et">strates</span> {txt(r["strates"])}</p>')
        o.append('<p class="pmeta"><span class="et">effets normatifs</span> '
                 + ', '.join(lien(v, idx, f' [{r["id"]} effets]') for v in r['complements_normatifs']) + '</p>')
        o.append('</details>')
    return '\n'.join(o)


def rendre_complements_normatifs(d, idx):
    cn = d['complements_normatifs']
    t1('complements_normatifs', cn)
    nb_eff = sum(len(m['effets']) for m in cn['mecanismes'])
    o = [f'<h2 id="cn">Compléments normatifs — {len(cn["mecanismes"])} mécanismes, {nb_eff} effets</h2>']
    o.append(f'<p>{e(cn["objet"])}</p>')
    o.append(f'<p class="pmeta"><span class="et">principe de partage</span> {e(cn["principe"])}</p>')
    o.append(f'<p class="pmeta"><span class="et">sources</span> {txt(cn["sources"])}</p>')

    o.append('<table class="ch"><caption>nomenclature des strates</caption>'
             '<tr><th>strate</th><th>définition</th><th>effets</th></tr>')
    par_strate = {}
    for m in cn['mecanismes']:
        for f in m['effets']:
            par_strate.setdefault(f['strate_atteignable'], []).append((m['id'], f))
    for k, v in cn['nomenclature_strates'].items():
        n = sum(len(x) for s, x in par_strate.items() if s == k)
        o.append(f'<tr><td>{e(k)}</td><td>{e(v)}</td><td>{n}</td></tr>')
    o.append('</table>')
    o.append(f'<p class="pmeta"><span class="et">synthèse déclarée</span> '
             f'{e(json.dumps(cn["synthese"], ensure_ascii=False))}</p>')

    # --- vue par mécanisme, navigable vers les nœuds
    o.append('<h3>Par mécanisme</h3>')
    for m in cn['mecanismes']:
        t1('mecanisme', m)
        o.append(f'<details class="prop" id="m-{e(m["id"])}">'
                 f'<summary><code>{e(m["id"])}</code> <b>{e(m["intitule"])}</b> '
                 f'<span class="meta">{len(m["effets"])} effets</span></summary>')
        o.append('<p class="pmeta"><span class="et">nœuds doctrinaux rattachés</span> '
                 + ', '.join(lien(v, idx, f' [mecanisme {m["id"]}]') for v in m['noeuds_rattaches']) + '</p>')
        o.append('<table class="ch"><tr><th>effet</th><th>énoncé</th>'
                 '<th>siège constitutionnel</th><th>droit déplacé</th>'
                 '<th>voie basse</th><th>fondement</th><th>strate</th></tr>')
        for f in m['effets']:
            t1('effet_normatif', f)
            if f['strate_atteignable'] not in cn['nomenclature_strates']:
                T1.append(f'strate_atteignable : « {f["strate_atteignable"]} » hors nomenclature')
            o.append(f'<tr id="fn-{e(f["id"])}"><td><code>{e(f["id"])}</code></td>'
                     f'<td>{e(f["effet"])}</td><td>{e(f["siege_constitutionnel"])}</td>'
                     f'<td>{e(f["droit_en_vigueur_deplace"])}</td><td>{e(f["voie_basse"])}</td>'
                     f'<td>{e(f["fondement"])}</td><td>{e(f["strate_atteignable"])}</td></tr>')
        o.append('</table></details>')

    # --- vue par strate, même matière regroupée autrement
    o.append('<h3>Par strate</h3>')
    for s in sorted(par_strate, key=lambda k: -len(par_strate[k])):
        o.append(f'<details class="reg"><summary>{e(s)} — {len(par_strate[s])} effets</summary><ul>')
        for mid, f in par_strate[s]:
            o.append(f'<li>{lien(f["id"], idx)} — {e(f["effet"])} '
                     f'<span class="meta">{e(f["siege_constitutionnel"])}</span></li>')
        o.append('</ul></details>')
    return '\n'.join(o)


def rendre_couverture(d):
    c = d['couverture_normative']
    o = ['<h2 id="couv">Couverture normative</h2>',
         f'<p>{e(c["constat"])}</p>']
    o.append('<pre class="js">' + e(json.dumps(
        {k: v for k, v in c.items() if k != 'constat'},
        ensure_ascii=False, indent=1)) + '</pre>')
    return '\n'.join(o)


# ============================================================ registres
def rendre_registres(d, idx, ecarts, resume_ecarts):
    o = ['<h2 id="registres">Registres</h2>']

    lac = [(p['id'], x) for p in idx['prop'].values() for x in p.get('lacunes', [])]
    o.append(f'<details class="reg" open><summary>Lacunes — {len(lac)} sur '
             f'{len({a for a, _ in lac})} propositions</summary><ul>')
    o += [f'<li>{lien(a, idx, " [lacunes]")} — {e(x)}</li>' for a, x in lac]
    o.append('</ul></details>')

    o.append(f'<details class="reg"><summary>Écarts consignés — {len(ecarts)}, '
             f'lus du contrôle arithmétique</summary>'
             '<table class="ch"><tr><th>nœud</th><th>libellé</th><th>valeur</th><th>unité</th></tr>')
    for nid, lib, val, un in ecarts:
        cible = (lien(nid, idx, " [écarts]") if _ancre(nid, idx)
                 else f'<code>{e(nid)}</code> <span class="meta">cellule de classeur, hors référentiel</span>')
        o.append(f'<tr><td>{cible}</td><td>{e(lib)}</td>'
                 f'<td class="num">{e(val)}</td><td>{e(un)}</td></tr>')
    o.append(f'</table><p class="meta">{e(resume_ecarts)}</p></details>')

    vides = [x for x in idx['entree'].values() if 'verdict' not in x]
    o.append(f'<details class="reg"><summary>Entrées non peuplées — {len(vides)} sur '
             f'{len(idx["entree"])}</summary>'
             '<p class="meta">Hors grille de référence des chiffres. Ni verdict, '
             'ni statut d’ancre, ni chaîne. Non diffusables au titre de la grille.</p><ul>')
    o += [f'<li>{lien(x["id"], idx)} — {e(x.get("nom") or x.get("enonce") or "")[:120]}</li>'
          for x in vides]
    o.append('</ul></details>')

    nd = [x for x in idx['entree'].values() if x.get('statut_ancre') == 'absent des deux']
    cl = [x for x in idx['entree'].values() if x.get('statut_ancre') == 'classeur']
    ill = [x for x in idx['entree'].values() if x.get('nature') == 'illustration']
    o.append(f'<details class="reg" open><summary>Interdits de diffusion en l’état — '
             f'{len(nd)} absentes des deux</summary><ul>')
    o += [f'<li>{lien(x["id"], idx)} — {e(x.get("nom") or x.get("enonce"))}</li>' for x in nd]
    o.append('</ul></details>')
    o.append(f'<details class="reg"><summary>À déclarer comme valeur de travail — '
             f'{len(cl)} de statut classeur</summary><ul>')
    o += [f'<li>{lien(x["id"], idx)} — {e(x.get("nom") or x.get("enonce"))}</li>' for x in cl]
    o.append('</ul></details>')
    o.append(f'<details class="reg"><summary>À ne jamais propager comme règle — '
             f'{len(ill)} illustrations</summary><ul>')
    o += [f'<li>{lien(x["id"], idx)} — {e(x.get("nom") or x.get("enonce"))}</li>' for x in ill]
    o.append('</ul></details>')
    return '\n'.join(o)


# ============================================================ assemblage
CSS = """
body{font-family:Georgia,serif;max-width:72em;margin:2em auto;line-height:1.5;padding:0 1.2em;font-size:15px;color:#1a1a1a}
h1{border-bottom:3px solid #000;padding-bottom:.2em}
h2{margin-top:2em;background:#efe9dd;padding:.35em .6em;border-left:6px solid #7a3b2e}
h3{margin:1.4em 0 .4em;color:#333;border-bottom:1px solid #ccc}
h5{margin:.9em 0 .2em;font-size:.9em;text-transform:uppercase;letter-spacing:.06em;color:#555}
code,.num{font-family:"JetBrains Mono",Consolas,monospace;font-size:.88em}
summary{cursor:pointer}
details.ax{margin:.6em 0}
details.lev{margin:.4em 0 .4em 1.2em}
details.prop{margin:.4em 0 .4em 1.2em;border-left:4px solid #7a9a6d;padding:.3em .7em;background:#fbfaf6}
details.reg{margin:.4em 0;border-left:4px solid #8a7a5c;padding:.3em .7em;background:#faf8f3}
.meta{font-family:sans-serif;font-size:.8em;color:#666}
.et{font-family:sans-serif;font-size:.72em;text-transform:uppercase;letter-spacing:.07em;color:#8a6d00;margin-right:.5em}
.ent{margin:.6em 0 .6em 1em;padding:.4em .7em;border-left:3px solid #b0a48c;background:#fff}
.ent.vide{border-left-style:dotted;background:#f6f6f4;color:#555}
.eid{margin:0 0 .2em}.kind{font-family:sans-serif;font-size:.75em;color:#777}
.titre{margin:.1em 0;font-style:italic}
.aff{margin:.15em 0;font-size:1.02em}
.exa{margin:.15em 0;font-size:1.02em;background:#f2f6ef;border-left:3px solid #4a6b3d;padding:.1em .5em}
.verd{margin:.2em 0;font-weight:bold}
.badges{margin:.3em 0}
.b{display:inline-block;font-family:sans-serif;font-size:.75em;padding:.1em .5em;border:1px solid;border-radius:2px;margin-right:.3em}
.b-ok{border-color:#4a6b3d;background:#eef4ea;color:#2e4a24}
.b-att{border-color:#8a6d00;background:#fdf6e0;color:#6a5400}
.b-int{border-color:#8c2f22;background:#fbeae7;color:#7a2519;font-weight:bold}
.b-neu{border-color:#888;background:#f2f2f2;color:#555}
.cond{margin:.35em 0;padding:.25em .6em;background:#fdf6e0;border-left:3px solid #8a6d00}
.cond ul{margin:.2em 0;padding-left:1.2em}.cond.vide{color:#777;font-style:italic;background:none;border-left-color:#ccc}
.app,.frm{display:grid;grid-template-columns:9em 1fr;gap:.1em .8em;margin:.35em 0;font-size:.93em}
.app dt,.frm dt{font-family:sans-serif;font-size:.75em;text-transform:uppercase;letter-spacing:.05em;color:#666;padding-top:.15em}
.app dd,.frm dd{margin:0}
table.ch{border-collapse:collapse;width:100%;font-size:.85em;margin:.4em 0}
table.ch caption{text-align:left;font-family:sans-serif;font-size:.72em;text-transform:uppercase;letter-spacing:.07em;color:#8a6d00;padding-bottom:.2em}
table.ch th{text-align:left;border-bottom:1.5px solid #999;padding:.2em .4em;font-family:sans-serif;font-size:.9em}
table.ch td{border-bottom:1px solid #ddd;padding:.2em .4em;vertical-align:top}
.st-r{color:#2e4a24}.st-x{color:#6a5400;font-style:italic}
.cc,.ren,.lac{margin:.35em 0;font-size:.92em}
.cc ul,.ren ul,.lac ul{margin:.2em 0;padding-left:1.2em}
.lac{background:#fbeae7;border-left:3px solid #8c2f22;padding:.25em .6em}
.insp{font-size:.85em;color:#555}
.pmeta{margin:.2em 0;font-size:.93em}
.ln{margin:.25em 0;font-size:.85em;font-family:sans-serif;color:#555}
.mort{color:#8c2f22;font-weight:bold}
.nn{color:#6a5400;font-size:.9em}
pre.js{background:#f6f5f1;padding:.6em;font-size:.8em;overflow-x:auto;border-left:3px solid #b0a48c}
.ctrl{border:2px solid #000;padding:.6em 1em;margin:1em 0;background:#fbfaf6}
.ctrl td{padding:.15em .6em}
a{color:#7a3b2e}
"""


def generer(src, dst):
    d = charger(src)
    idx = indexer(d)
    ecarts, resume = lire_ecarts()

    meca_par_noeud = {}
    for m in d['complements_normatifs']['mecanismes']:
        for n in m['noeuds_rattaches']:
            meca_par_noeud.setdefault(n, []).append(m['id'])

    rev = d['_revision']
    o = ['<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">',
         f'<title>REF_doctrine {e(rev["version"])} — arbre de lecture</title>',
         f'<style>{CSS}</style></head><body>',
         f'<h1>REF_doctrine {e(rev["version"])} — arbre de lecture</h1>',
         f'<p class="meta">Généré depuis <code>{e(src)}</code> le {e(rev["date"])}. '
         'Document de travail interne : la nomenclature D, les marqueurs manuscrit '
         'et les identifiants de mécanismes y sont visibles. Aucune valeur n’est '
         'écrite à la main, tout est projeté du référentiel.</p>']

    # ------------------------------------------------------------ compteurs
    nb = {'axes': len(d['axes']),
          'leviers': sum(len(a['leviers']) for a in d['axes']),
          'propositions': len(idx['prop']),
          'entrees': len(idx['entree']),
          'peuplees': sum(1 for x in idx['entree'].values() if 'verdict' in x),
          'lexique': len(d['lexique']),
          'mecanismes': len(idx['meca']),
          'effets_normatifs': len(idx['effet_n'])}
    o.append('<div class="ctrl"><b>Compteurs — arbre contre contrôle structurel</b>'
             '<table><tr><th>objet</th><th>arbre</th><th>attendu</th><th>état</th></tr>')
    for k, att in ATTENDU.items():
        etat = 'concordant' if nb[k] == att else f'ÉCART de {nb[k] - att}'
        o.append(f'<tr><td>{k}</td><td class="num">{nb[k]}</td>'
                 f'<td class="num">{att}</td><td>{etat}</td></tr>')
    o.append(f'<tr><td>entrées non peuplées</td><td class="num">{nb["entrees"] - nb["peuplees"]}</td>'
             f'<td class="num">{ATTENDU["entrees"] - ATTENDU["peuplees"]}</td>'
             f'<td>{"concordant" if nb["entrees"] - nb["peuplees"] == ATTENDU["entrees"] - ATTENDU["peuplees"] else "ÉCART"}</td></tr>')
    o.append('</table></div>')

    # ------------------------------------------------------------ légende
    o.append('<h2 id="legende">Légende</h2><p class="meta">Chaque marque porte son '
             'libellé en clair : aucune couleur ne fait sens à elle seule.</p><p class="badges">'
             + ' '.join(badge('statut_ancre', k) for k in BADGES['statut_ancre'])
             + '</p><p class="badges">'
             + ' '.join(badge('nature', k) for k in BADGES['nature']) + '</p>')

    # ------------------------------------------------------------ arbre
    o.append('<h2 id="arbre">Arbre doctrinal</h2>')
    for a in d['axes']:
        t1('axe', a)
        nprop = sum(len(l['propositions']) for l in a['leviers'])
        o.append(f'<details class="ax" id="a-{e(a["id"])}" open>'
                 f'<summary><b>{e(a["id"])} — {e(a["intitule"])}</b> '
                 f'<span class="meta">{len(a["leviers"])} leviers · {nprop} propositions</span></summary>')
        o.append(rendre_complements_c(a['complements_constitutionnels'], 'axe'))
        for l in a['leviers']:
            t1('levier', l)
            o.append(f'<details class="lev" id="l-{e(l["id"])}">'
                     f'<summary><code>{e(l["id"])}</code> {e(l["intitule"])} '
                     f'<span class="meta">{len(l["propositions"])} propositions</span></summary>')
            o.append(rendre_complements_c(l['complements_constitutionnels'], 'levier'))
            o += [rendre_proposition(p, idx, meca_par_noeud) for p in l['propositions']]
            o.append('</details>')
        o.append(rendre_registre_axe(a['gains_indirects'], 'Gains indirects de l’axe',
                                     'gain indirect', idx))
        o.append(rendre_registre_axe(a['effets_diagnostic'], 'Effets de diagnostic de l’axe',
                                     'effet de diagnostic', idx))
        o.append('</details>')

    o.append(rendre_lexique(d, idx))
    o.append(rendre_rt(d, idx))
    o.append(rendre_complements_normatifs(d, idx))
    o.append(rendre_couverture(d))
    o.append(rendre_registres(d, idx, ecarts, resume))

    # ------------------------------------------------------------ révision
    o.append('<h2 id="rev">Révision</h2><pre class="js">'
             + e(json.dumps(rev, ensure_ascii=False, indent=1)) + '</pre>')

    # ------------------------------------------------------------ traversée
    o.append('<h2 id="trav">Contrôle de traversée</h2>')
    for lib, lst in (('T1 — couverture du schéma', T1), ('T2 — intégrité des renvois', T2)):
        if lst:
            uniq = sorted(set(lst))
            o.append(f'<div class="lac"><p class="et">{lib} — {len(uniq)} anomalies</p><ul>'
                     + ''.join(f'<li>{e(x)}</li>' for x in uniq) + '</ul></div>')
        else:
            o.append(f'<p class="badges"><span class="b b-ok">{e(lib)} — aucune anomalie</span></p>')
    o.append('</body></html>')

    open(dst, 'w', encoding='utf-8').write('\n'.join(o))

    # ------------------------------------------------------------ sortie console
    print(f'{dst} écrit')
    for k, att in ATTENDU.items():
        if nb[k] != att:
            print(f'  COMPTEUR {k} : {nb[k]} contre {att} attendus')
    print(f'  {len(set(T1))} anomalie(s) T1, {len(set(T2))} anomalie(s) T2, '
          f'{len(ecarts)} écart(s) consigné(s) repris')
    for x in sorted(set(T1)) + sorted(set(T2)):
        print(f'    {x}')
    return 1 if (T1 or T2) else 0


if __name__ == '__main__':
    sys.exit(generer(sys.argv[1], sys.argv[2]))
