# -*- coding: utf-8 -*-
"""L'état des vecteurs, en une page que l'auteur ouvre.

`referentiels/REF_norme.json` porte 1 856 entrées ; il n'est pas lisible. Cette
page l'est : elle dit ce qui est trouvé, ce qui reste, et ce que les contrôles
signalent — sans qu'on ait à ouvrir un JSON ni à jouer un script.

Même statut que `livrables/carte_du_projet.html` : un dérivé, régénéré par
`make`, jamais corrigé à la main. Une correction se porte à `vecteurs.py` ou à
l'annexe, et on rejoue.

**Elle ne porte aucun texte de loi.** Uniquement des adresses — code,
fourchette d'articles, identifiant Légifrance — et le lien qui y mène. C'est la
règle du vecteur : un identifiant, jamais du verbatim (A-245).

Usage : python3 generer_etat_vecteurs.py ../referentiels/REF_norme.json \\
            ../referentiels/socle_budgetaire.json ../livrables/etat_vecteurs.html
"""
import collections
import csv
import html
import json
import os
import sys

import controle_norme
import vecteurs

CSS = """
:root{--ocre:#9C6B00;--rouge:#B5291C;--vert:#1B5E35;--encre:#1A1A1A;
--papier:#FFFEF9;--bg:#F7F4ED;--gris:#5A5A5A;--bord:#D9D2C4;--pale:#EFEAE0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Fraunces',Georgia,serif;background:var(--bg);color:var(--encre);
font-size:15px;line-height:1.6}
.tete{background:var(--encre);color:var(--papier);padding:38px 0 30px}
.in{max-width:1180px;margin:0 auto;padding:0 34px}
.sur{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:10px;
letter-spacing:.2em;text-transform:uppercase;color:rgba(255,254,249,.45);margin-bottom:12px}
h1{font-size:clamp(24px,3vw,36px);font-weight:700;letter-spacing:-.02em;line-height:1.12}
.sous{color:rgba(255,254,249,.6);font-size:14px;margin-top:10px;max-width:70ch}
.filet{height:4px;display:flex}
.filet i{display:block;height:100%}
.filet i:nth-child(1){background:var(--vert);flex:5}
.filet i:nth-child(2){background:var(--ocre);flex:2}
.filet i:nth-child(3){background:var(--rouge);flex:1}
main{max-width:1180px;margin:0 auto;padding:0 34px 90px}
section{margin-top:44px}
h2{font-size:20px;font-weight:700;color:var(--encre);margin-bottom:6px;
padding-bottom:8px;border-bottom:2px solid var(--encre)}
h3{font-size:15px;font-weight:700;margin:24px 0 8px}
p{margin:10px 0;max-width:82ch}
.note{font-size:13px;color:var(--gris);font-style:italic;max-width:82ch}
.cartes{display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:12px;margin:18px 0}
.carte{background:var(--papier);border:1px solid var(--bord);border-left:3px solid var(--ocre);padding:13px 15px}
.carte .n{font-family:'JetBrains Mono',monospace;font-size:23px;font-weight:600;color:var(--encre)}
.carte .l{font-size:11.5px;color:var(--gris);margin-top:3px;line-height:1.35}
.carte.ok{border-left-color:var(--vert)}
.carte.att{border-left-color:var(--rouge)}
table{width:100%;border-collapse:collapse;background:var(--papier);
border:1px solid var(--bord);margin:14px 0;font-size:13px}
th{background:var(--pale);text-align:left;padding:8px 11px;font-size:10.5px;
font-family:'JetBrains Mono',monospace;letter-spacing:.1em;text-transform:uppercase;
color:var(--gris);border-bottom:1px solid var(--bord);white-space:nowrap}
td{padding:8px 11px;border-bottom:1px solid #EDE8DD;vertical-align:top}
tr:last-child td{border-bottom:none}
td.m,th.m{font-family:'JetBrains Mono',monospace;font-size:12px}
td.num{text-align:right;font-family:'JetBrains Mono',monospace;font-size:12px;white-space:nowrap}
.jauge{display:inline-block;height:7px;background:var(--pale);width:88px;
vertical-align:middle;margin-right:7px;border:1px solid var(--bord)}
.jauge i{display:block;height:100%;background:var(--vert)}
.jauge.b i{background:var(--rouge)}
.et{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:10px;
padding:2px 6px;border-radius:2px;white-space:nowrap}
.et.t{background:#DCEEE2;color:var(--vert)}
.et.a{background:#FBE4E1;color:var(--rouge)}
.et.p3{background:#DCEEE2;color:var(--vert)}
.et.p2{background:#FBF0D8;color:var(--ocre)}
.et.p1{background:var(--pale);color:var(--gris)}
a{color:var(--vert)}
a.lf{font-family:'JetBrains Mono',monospace;font-size:11px;text-decoration:none;
border-bottom:1px dotted rgba(27,94,53,.4)}
.enc{background:var(--papier);border:1px solid var(--bord);border-left:3px solid var(--rouge);
padding:14px 17px;margin:16px 0}
.enc.o{border-left-color:var(--ocre)}
.enc h4{font-size:14px;margin-bottom:6px}
footer{background:var(--encre);color:rgba(255,254,249,.4);padding:22px 0;
font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.06em}
@media(max-width:820px){.in,main{padding-left:16px;padding-right:16px}table{font-size:12px}}
"""

LF = 'https://www.legifrance.gouv.fr/'


def _e(s):
    return html.escape(str(s)) if s is not None else ''


def _lien(ident):
    if not ident:
        return ''
    if ident.startswith('LEGISCTA'):
        u = f'{LF}codes/id/{ident}'
    elif ident.startswith('LEGIARTI'):
        u = f'{LF}codes/article_lc/{ident}'
    elif ident.startswith('JORFTEXT'):
        u = f'{LF}loda/id/{ident}'
    else:
        u = f'{LF}search/all?query={ident}'
    return f'<a class="lf" href="{u}">{_e(ident)}</a>'


COLONNES = ['population', 'cle', 'libelle', 'regime', 'role', 'code',
            'code_identifiant', 'siege', 'article', 'subdivision',
            'provenance', 'confiance', 'variante', 'strate', 'releve_le',
            'montant_eur']


def aplatir(norme):
    """Une ligne par vecteur, colonnes atomiques, du macro au micro.

    C'est la forme exportable : rien d'imbriqué, rien de collé. Le code, le
    siège, l'article et la subdivision sont quatre colonnes, parce qu'une
    disposition modificative ne vise pas le même objet selon le niveau.
    """
    lignes = []
    for e in norme['entrees']:
        for v in e['vecteurs']:
            lignes.append({
                'population': e['population'],
                'cle': e['cle'],
                'libelle': e['libelle'],
                'regime': e.get('regime') or '',
                'role': v['role'],
                'code': v.get('texte') or '',
                'code_identifiant': v.get('identifiant') or '',
                'siege': v.get('siege') or '',
                'article': v.get('article') or (v.get('articles') or ''),
                'subdivision': v.get('subdivision') or '',
                'provenance': v['provenance'],
                'confiance': vecteurs.PROVENANCES[v['provenance']][0],
                'variante': v.get('variante') or 'a_determiner',
                'strate': v.get('strate') or '',
                'releve_le': e.get('releve_le') or v.get('code_releve_le') or '',
                'montant_eur': e.get('montant_eur') or '',
            })
    lignes.sort(key=lambda r: (r['population'], r['cle'], r['role']))
    return lignes


def ecrire_csv(lignes, dst):
    with open(dst, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=COLONNES, delimiter=';')
        w.writeheader()
        w.writerows(lignes)
    return len(lignes)


def _md(v):
    if not v:
        return '—'
    return f'{v / 1e9:,.2f}'.replace(',', ' ').replace('.', ',') + ' Md€'


def _jauge(tr, tot, seuil=50):
    p = 100 * tr // tot if tot else 0
    cl = '' if p >= seuil else ' b'
    return (f'<span class="jauge{cl}"><i style="width:{p}%"></i></span>'
            f'{tr} / {tot} — {p} %')


LOTS = [
    ('programme', 'V1', 'Programmes du budget général',
     "Vecteur non codifié et **de rang législatif** : l'état B annexé à "
     "l'article de crédits. Le même pour les 128."),
    ('depense_fiscale', 'V2', 'Dépenses fiscales',
     "Vecteur dérivé de l'annexe, rejoué à chaque contrôle par N4."),
    ('taxe_affectee', 'V3', 'Taxes affectées',
     "La référence de l'annexe est une loi de finances : elle date la taxe, "
     "elle ne la localise pas."),
    ('operateur', 'V4a', 'Opérateurs du PLF',
     "Aucune pièce ne nomme le texte fondateur. Une recherche par cible."),
    ('odac_odal', 'V4b', 'ODAC-ODAL',
     "Même chose, sur une population quatre fois plus large."),
    ('proposition', 'V5', 'Propositions du REF_doctrine',
     "La norme cible s'écrit avant que le vecteur se cherche."),
]


def rendre(norme, socle):
    E = norme['entrees']
    plat = aplatir(norme)
    ppe = norme['comptes']['par_population_et_etat']
    tot = len(E)
    trouve = sum(v.get('trouve', 0) for v in ppe.values())
    releves = [e for e in E if any(v['provenance'] == 'legifrance'
                                   for v in e['vecteurs'])]
    collisions = controle_norme.n6_collision(E)
    ind, _sr = controle_norme.n9_code(E)
    hors_forme = controle_norme.n2_forme(E)
    cles_hf = {c for _, c, _ in hors_forme}
    idx = {e['cle']: e for e in E if e['population'] == 'depense_fiscale'}
    hf_regime = [c for c in cles_hf if idx[c]['regime'] not in (None, '—')]
    hf_mt = sum(idx[c]['montant_eur'] or 0 for c in hf_regime)

    o = []
    a = o.append
    a('<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">')
    a('<meta name="viewport" content="width=device-width,initial-scale=1">')
    a('<title>État des vecteurs — Résolution</title>')
    a('<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@'
      '9..144,400;9..144,700&family=JetBrains+Mono:wght@400;600&display=swap" '
      'rel="stylesheet">')
    a(f'<style>{CSS}</style></head><body>')

    a('<div class="tete"><div class="in">')
    a('<div class="sur">Résolution · contre-PLF · REF_norme</div>')
    a('<h1>L\'état des sources juridiques à modifier</h1>')
    a('<p class="sous">Une entrée par mesure, son véhicule et son vecteur. '
      'Le vecteur est une adresse — code, fourchette d\'articles, identifiant '
      'Légifrance — et jamais du texte de loi.</p>')
    a('</div></div><div class="filet"><i></i><i></i><i></i></div>')
    a('<main>')

    # ------------------------------------------------------------ le compte
    a('<section><h2>Où on en est</h2>')
    a('<div class="cartes">')
    a(f'<div class="carte"><div class="n">{tot}</div>'
      '<div class="l">entrées au référentiel</div></div>')
    a(f'<div class="carte ok"><div class="n">{trouve}</div>'
      '<div class="l">vecteurs trouvés</div></div>')
    a(f'<div class="carte att"><div class="n">{tot - trouve}</div>'
      '<div class="l">à trouver</div></div>')
    a(f'<div class="carte"><div class="n">{len(releves)}</div>'
      '<div class="l">cibles relevées sur Légifrance</div></div>')
    durs = [x for x in collisions if x[2] > 1]
    a(f'<div class="carte att"><div class="n">{len(durs)}</div>'
      '<div class="l">articles visés en entier par plusieurs mesures</div>'
      '</div>')
    a(f'<div class="carte att"><div class="n">{len(ind)}</div>'
      '<div class="l">adresses de code indéterminé</div></div>')
    a('</div>')

    a('<table><thead><tr><th class="m">lot</th><th>population</th>'
      '<th>couverture</th><th>ce qui la commande</th></tr></thead><tbody>')
    for pop, lot, nom, quoi in LOTS:
        d = ppe.get(pop, {})
        n = sum(d.values())
        tr = d.get('trouve', 0)
        if not n:
            continue
        a(f'<tr><td class="m">{lot}</td><td><b>{_e(nom)}</b></td>'
          f'<td class="num">{_jauge(tr, n)}</td>'
          f'<td class="note">{quoi}</td></tr>')
    a('</tbody></table>')
    a('<p class="note">Le vecteur est trouvé ou il ne l\'est pas. Il ne '
      's\'invente jamais : un vecteur vraisemblable est plus dangereux qu\'un '
      'vecteur absent, il a l\'apparence d\'une adresse et il envoie '
      'l\'amendement au mauvais endroit.</p>')
    a('</section>')

    # ---------------------------------------------------- la table plate
    a('<section><h2>La table — une ligne par vecteur</h2>')
    a('<p>Colonnes atomiques, du macro au micro : <b>code · siège · article · '
      'subdivision</b>. Une disposition modificative ne vise pas le même objet '
      'selon le niveau, et une adresse collée n\'est pas une adresse. '
      f'<b>{len(plat)} lignes</b>, exportées telles quelles à '
      '<code>livrables/etat_vecteurs.csv</code>.</p>')
    a('<div class="enc o"><h4>Le code n\'est jamais affirmé</h4>'
      '<p class="note">L\'annexe des dépenses fiscales ne nomme pas le code : '
      'elle donne « 1465 A », « L. 312-48 ». Le code est donc <b>déduit par '
      'une règle écrite et datée</b>, portée sur chaque ligne. Ce qu\'aucune '
      'règle ne couvre sort en <i>indéterminé</i> — jamais en code général des '
      'impôts par défaut.</p></div>')
    a('<table><thead><tr>'
      '<th>cible</th><th class="m">rôle</th><th>code</th><th>siège</th>'
      '<th class="m">article</th><th class="m">subdivision</th>'
      '<th class="m">prov.</th><th class="m">variante</th>'
      '<th class="m">relevé</th></tr></thead><tbody>')
    montrees = [r for r in plat if r['provenance'] != 'annexe'
                and r['role'] != 'montant']
    for r in montrees:
        ident = _lien(r['code_identifiant']) if r['code_identifiant'] else ''
        code = _e(r['code']) + (f'<br>{ident}' if ident else '')
        cl = ('p3' if r['confiance'] == 3
              else 'p2' if r['confiance'] == 2 else 'p1')
        a(f'<tr><td><b>{_e(r["cle"])}</b>'
          f'<div class="note">{_e(r["population"])} · '
          f'{_e(r["regime"] or "—")}</div></td>'
          f'<td class="m">{_e(r["role"])}</td><td>{code}</td>'
          f'<td class="note">{_e(r["siege"] or "—")}</td>'
          f'<td class="m">{_e(r["article"])}</td>'
          f'<td class="m">{_e(r["subdivision"] or "—")}</td>'
          f'<td><span class="et {cl}">{_e(r["provenance"])}</span></td>'
          f'<td class="m">{_e(r["variante"])}</td>'
          f'<td class="m">{_e(r["releve_le"] or "—")}</td></tr>')
    a('</tbody></table>')
    a(f'<p class="note">Les {len(plat) - len(montrees)} lignes dérivées de '
      'l\'annexe et le vecteur des crédits ne sont pas listés ici : ils sont '
      'au fichier exporté. La page montre ce qui a demandé une recherche.</p>')
    a('<div class="enc"><h4>La variante n\'est pas encore renseignée</h4>'
      '<p class="note">« Dans l\'absolu » — article additionnel — contre '
      '« article ouvert par le texte déposé ». Amender un article que le PLF '
      'ouvre déjà coûte infiniment moins, mais <b>sans le socle du texte on ne '
      'sait pas lesquels sont ouverts</b>. La colonne existe et vaut '
      '<i>à déterminer</i> partout : elle se remplit au fil 2, et les liasses '
      'de Génération Libre en donneront une première part.</p></div>')
    a('<div class="enc o"><h4>Un organisme a souvent deux vecteurs, et '
      'l\'économie porte sur le second</h4>'
      '<p class="note">Les agences de l\'eau sont créées par une section du '
      'code de l\'environnement et financées par une autre. Supprimer '
      'l\'organisme et supprimer sa ressource ne se font pas au même endroit. '
      'C\'est pourquoi chaque vecteur déclare son rôle — et c\'est ce qui '
      'permet de faire feu de tout bois.</p></div>')
    a('</section>')

    # ------------------------------------------- ce que les contrôles sortent
    a('<section><h2>Ce que les contrôles signalent</h2>')

    a('<h3>Les références que l\'annexe ne donne pas comme adresse '
      'd\'article</h3>')
    a(f'<p><b>{len(cles_hf)} dépenses fiscales</b> sur '
      f'{sum(ppe["depense_fiscale"].values())} portent, à l\'annexe, autre '
      'chose qu\'une adresse exploitable — un renvoi à la doctrine '
      'administrative, une mention d\'alinéa, du texte libre. '
      f'<b>{len(hf_regime)} d\'entre elles portent un régime de suppression, '
      f'pour {_md(hf_mt)}.</b></p>')
    a('<table><thead><tr><th class="m">n°</th><th>libellé</th>'
      '<th class="m">ce que l\'annexe porte</th><th class="m">régime</th>'
      '<th class="m">montant</th></tr></thead><tbody>')
    par_cle = collections.defaultdict(list)
    for _, c, ref in hors_forme:
        par_cle[c].append(ref)
    for c in sorted(par_cle, key=lambda x: -(idx[x]['montant_eur'] or 0))[:18]:
        e = idx[c]
        a(f'<tr><td class="m">{_e(c)}</td><td>{_e(e["libelle"][:88])}</td>'
          f'<td class="m">{_e(" · ".join(par_cle[c])[:60])}</td>'
          f'<td class="m">{_e(e["regime"] or "—")}</td>'
          f'<td class="num">{_md(e["montant_eur"])}</td></tr>')
    a('</tbody></table>')
    if len(par_cle) > 18:
        a(f'<p class="note">{len(par_cle) - 18} autres, de montant '
          'inférieur.</p>')

    a('<h3>Les articles visés par plus d\'une mesure</h3>')
    a(f'<p><b>{len(collisions)} adresses</b> sont visées par plus d\'une '
      f'mesure, dont <b>{len(durs)} en entier par plusieurs</b>. Deux '
      'amendements qui abrogeraient le même article se neutralisent — et à '
      'l\'inverse, <b>un seul amendement sur <code>L. 312-48</code> '
      'supprimerait onze dépenses fiscales d\'un coup</b>. Efficace ou piège '
      'selon l\'intention, et cela se voit ici et nulle part ailleurs.</p>')
    a('<table><thead><tr><th>code</th><th class="m">article</th>'
      '<th class="m">mesures</th><th class="m">sur l\'article entier</th>'
      '<th class="m">visé par</th></tr></thead><tbody>')
    for (texte, art), qui, entier in sorted(collisions,
                                            key=lambda x: -x[2])[:14]:
        a(f'<tr><td class="note">{_e(texte)}</td><td class="m">{_e(art)}</td>'
          f'<td class="num">{len(qui)}</td><td class="num">{entier}</td>'
          f'<td class="m">{_e(", ".join(c for _, c in qui[:5]))}'
          + (' …' if len(qui) > 5 else '') + '</td></tr>')
    a('</tbody></table>')
    if len(collisions) > 14:
        a(f'<p class="note">{len(collisions) - 14} autres.</p>')
    a('</section>')

    # ------------------------------------------------------------ ce qui reste
    a('<section><h2>Ce qui reste, dans l\'ordre</h2>')
    etapes = [
        ("Les dépenses fiscales sans adresse exploitable",
         f'{len(hf_regime)} recherches', _md(hf_mt),
         "Le lot le plus rentable qui reste : après lui, les niches sont à "
         "100 % d'adresses exploitables."),
        ("Les taxes affectées des régimes « Oui » et « Flux OM »",
         '87 taxes', '—',
         "Le compte de recherches est très inférieur au compte de taxes : une "
         "section couvre souvent plusieurs taxes. Les 86 « Collocs » et les "
         "52 « Sécu » sont deux lots à part."),
        ("Les organismes, par montant et non par ordre alphabétique",
         f'{sum(ppe[p].get("a_trouver", 0) for p in ("operateur", "odac_odal"))} cibles',
         '—',
         "Lots de 25 à 30 par fil, une dizaine de fils. Poste le plus lourd, "
         "parallélisable, ne bloque rien."),
        ("Les propositions arrêtées",
         '44 propositions', '—',
         "Les 12 esquissées attendent leur norme cible : chercher un vecteur "
         "sous une norme non arrêtée, c'est le chercher deux fois."),
    ]
    a('<table><thead><tr><th class="m">étape</th><th>ce que c\'est</th>'
      '<th class="m">volume</th><th class="m">enjeu</th>'
      '<th>pourquoi cet ordre</th></tr></thead><tbody>')
    for i, (nom, vol, mt, pq) in enumerate(etapes, 1):
        a(f'<tr><td class="m">{i}</td><td><b>{_e(nom)}</b></td>'
          f'<td class="m">{_e(vol)}</td><td class="num">{mt}</td>'
          f'<td class="note">{pq}</td></tr>')
    a('</tbody></table>')
    a('</section>')

    # --------------------------------------------------------------- lecture
    a('<section><h2>Comment lire une ligne</h2>')
    a('<table><thead><tr><th class="m">champ</th><th>ce qu\'il dit</th>'
      '</tr></thead><tbody>')
    for r in vecteurs.ROLES:
        d = {'creation': "le texte qui institue l'organisme ou le dispositif",
             'financement': "le texte qui lui affecte une ressource — "
                            "<b>c'est presque toujours là que porte "
                            "l'économie</b>",
             'competence': 'le texte qui lui donne sa mission',
             'montant': "le siège du chiffre voté, qui n'est pas codifié",
             'derogation': "l'article qui porte la dépense fiscale"}[r]
        a(f'<tr><td class="m">rôle · {r}</td><td>{d}</td></tr>')
    for k, (n, d) in sorted(vecteurs.PROVENANCES.items(),
                            key=lambda x: -x[1][0]):
        a(f'<tr><td class="m">provenance · {k} <span class="et p'
          f'{min(n, 3) if n else 1}">{n}</span></td><td>{_e(d)}</td></tr>')
    a('</tbody></table>')
    a('<p class="note">Cette page ne porte aucun texte de loi : uniquement '
      'des adresses. Le texte d\'un article entre au corpus par pièce jointe, '
      'jamais par une recherche — l\'outil de récupération repère, il ne '
      'copie pas.</p>')
    a('</section>')

    a('</main>')
    a('<footer><div class="in">Dérivé de referentiels/REF_norme.json par '
      'appareil/generer_etat_vecteurs.py — ne se corrige pas à la main, se '
      'régénère. Une correction se porte à appareil/vecteurs.py ou à '
      'l\'annexe.</div></footer>')
    a('</body></html>')
    return '\n'.join(o)


def main(src_norme, src_socle, dst, dst_csv=None):
    norme = json.load(open(src_norme, encoding='utf-8'))
    socle = json.load(open(src_socle, encoding='utf-8'))
    page = rendre(norme, socle)
    os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
    open(dst, 'w', encoding='utf-8').write(page)
    if dst_csv:
        n = ecrire_csv(aplatir(norme), dst_csv)
        print(f'{dst_csv} écrit — {n} ligne(s), {len(COLONNES)} colonnes')
    ppe = norme['comptes']['par_population_et_etat']
    tr = sum(v.get('trouve', 0) for v in ppe.values())
    print(f"{dst} écrit — {len(norme['entrees'])} entrées, {tr} vecteur(s) "
          f"trouvé(s), {os.path.getsize(dst)} octets")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3],
                  sys.argv[4] if len(sys.argv) > 4 else None))
