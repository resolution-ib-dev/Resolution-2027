# -*- coding: utf-8 -*-
"""Le format des fiches gagnants-perdants, éprouvé sur deux catégories.

Un seul format, en lecture linéaire. Il naît de trois traitements mis côte à
côte et de deux relectures de l'auteur ; ce qui reste ici est ce qui a survécu.

Il s'éprouve sur `C-04`, la seule catégorie entièrement rédigée, et sur `C-30`,
le cas dur — celui où la même personne est perdante et gagnante de la même
mesure.

**Rien n'est écrit ici.** Tout vient de `referentiels/positions.json` et de
`referentiels/REF_doctrine.json` : si la fiche affiche quelque chose, c'est que
le référentiel le porte.

Les règles du format, et ce qui les a produites.

**Une vedette, une phrase.** La tête de ligne porte un chiffre quand le gain en
a un, deux mots quand il n'en a pas — « Le temps » se lit sur le même plan que
« 70 % ». La phrase ne répète pas la vedette.

**Le côté moins et le côté plus ne se présentent pas pareil.** Une perte est une
carte : elle porte sa justification et son échange. Un gain est une ligne.

**L'ordre suit la catégorie.** Les plus d'abord là où les plus dominent, les
moins d'abord pour les perdants spontanés — au-delà d'un tiers de pertes. Et
quand la fiche ouvre sur les moins, le côté plus commence par le gain auquel les
pertes se raccrochent.

**Une fiche n'affirme jamais une absence.** Le référentiel dit qu'une catégorie
ne porte aucune ligne de perte ; il ne dit pas que la personne ne perd rien.

**Qui paie se dit une fois.** Presque toute la restitution est payée par
l'ensemble des économies : la formule commune va en pied. Seules les
contreparties propres — le chômage, le patrimoine — restent sur leur ligne.

**Chaque gain a une attache, et une seule.** Un gain projeté sur plusieurs
catégories se dit **en entier là où il est le plus pertinent** — c'est son
attache. Partout ailleurs il revient en **rappel** : sa vedette seule, sur une
ligne, en pied de fiche. La personne ne perd rien, et elle ne relit jamais la
même phrase. Pas de socle : « tout le monde », c'est personne.

**Chaque fiche s'ancre sur ce qui lui appartient** — son gain principal, ou sa
perte quand elle est d'abord perdante, puis ses gains.

**Une grappe se replie.** Trois gains ou plus sous le même levier, sans vedette
propre, se rangent sous le premier. Un gain qui porte sa vedette ne se replie
jamais : il a quelque chose à dire que les autres ne disent pas.

Usage : python3 generer_fiches.py ../referentiels/positions.json \\
                                ../referentiels/REF_doctrine.json ../livrables
"""
import html
import json
import os
import re
import sys

# La série, son ordre, ses attaches et l'ordre interne de chaque fiche se
# lisent à **la carte d'attribution**, qui est le document arbitré. Une seule
# source : la carte décide, le générateur exécute.
from structure_fiches import STRUCTURE as _CARTE  # noqa: E402

FICHES = tuple(c[0] for c in _CARTE)
TITRES_CARTE = {c[0]: c[1] for c in _CARTE}
AXES = {c[0]: c[2] for c in _CARTE}
ATTACHE_CARTE = {}
ORDRE_CARTE = {}
PERTES_CARTE = {}
for _c in _CARTE:
    ORDRE_CARTE[_c[0]] = list(_c[3])
    PERTES_CARTE[_c[0]] = list(_c[4])
    for _a in _c[3]:
        ATTACHE_CARTE[_a] = _c[0]

CONTREPARTIE_GENERALE = ("Payé par l'ensemble des économies publiques, "
                         "pas par une mesure en particulier.")

# Le terme du référentiel sert à ranger, pas à s'adresser à quelqu'un. « Agent
# d'une structure fermée » ne se reconnaît pas, et il ne dit pas que l'agent est
# public. Proposition de Claude, marquée comme telle à l'écran : le terme du
# référentiel n'est pas touché, et le titre d'affichage est un output.
TITRES_PROPOSES = {
    'C-30': 'Agent public dont le poste est supprimé',
    'C-05': 'Agent public indispensable',
    'C-40': 'Locataire HLM',
}

# Une catégorie dont les pertes dépassent cette part des lignes ouvre sur les
# moins. À un tiers pile, la personne reste d'abord gagnante.
PART_PERTES = 1 / 3
# Trois gains sans vedette propre sous un même levier forment une grappe.
GRAPPE = 3
# Une dominante et cinq items. Au-delà, une fiche ne se lit plus d'un coup
# d'œil et ne tient plus sur un écran de téléphone. Ce qui sort n'est pas ce
# qui tombe au hasard : `ORDRE` dit, catégorie par catégorie, ce qui passe.
PLAFOND = 6
# Sous ce nombre de gains propres, la fiche est trop mince pour reléguer sa
# matière en pied : ses rappels écrits remontent en ligne pleine (A-188).
SEUIL_MINCE = 3
LEVIER = re.compile(r'^([A-Z]\d+-\d+)')

# --- relevé de secours, pour les gains dont la vedette n'est pas écrite -----
# Le régime transitoire porte l'énoncé du livre ; sa vedette se relève de lui,
# faute de mieux. Vocabulaire d'unités fermé, comme au relevé des chiffres.
UNITES = [
    (r'%', '%'),
    (r'milliards?(?:\s+d[’\']euros)?', 'Md€'),
    (r'millions?(?:\s+d[’\']euros)?', 'M€'),
    (r'euros?|€', '€'),
    (r'centimes?', 'centimes'),
    (r'postes?', ''),
    (r'agents?', ''),
    (r'M\b', 'M'),
]
NOMBRE = r'\d[\d   ]*(?:,\d+)?'
QUANTITE = re.compile(
    r'(?<![\w,])(' + NOMBRE + r')\s*(' + '|'.join(u for u, _ in UNITES) + r')',
    re.I)
# Une quantité qui croît porte son signe. Sans lui, « 13 % » se lit comme un
# niveau et non comme une hausse.
CROISSANCE = re.compile(r'\b(monte|montent|hausse|augment\w*|de plus|en plus|'
                        r'paliers?|progress\w*)\b', re.I)


def quantite(texte):
    """Première quantité d'un texte, normalisée. Vide si aucune."""
    m = QUANTITE.search(texte or '')
    if not m:
        return ''
    valeur = m.group(1).strip().replace(' ', ' ').replace(' ', ' ')
    brut = m.group(2)
    propre = next((p for u, p in UNITES if re.fullmatch(u, brut, re.I)), '')
    # « 77 c » ne se comprend pas. Les centimes se disent en euros.
    if propre == 'centimes':
        try:
            valeur = f'{int(valeur.replace(" ", "")) / 100:.2f}'.replace('.', ',')
            propre = '€'
        except ValueError:
            propre = 'centimes'
    signe = '+' if CROISSANCE.search(texte) else ''
    return (f'{signe}{valeur}\u202f{propre}' if propre
            else f'{signe}{valeur}')


def libelles(ref):
    """id du nœud → sa phrase courte au REF (énoncé, sinon intitulé)."""
    table = {}

    def descendre(o):
        if isinstance(o, dict):
            i = o.get('id')
            if isinstance(i, str):
                t = o.get('enonce') or o.get('intitule')
                if isinstance(t, str) and t:
                    table[i] = t.rstrip('.')
            for v in o.values():
                descendre(v)
        elif isinstance(o, list):
            for v in o:
                descendre(v)

    descendre(ref)
    return table


def vedettes_attachees(positions):
    """ancrage → la vedette écrite chez son attache.

    Un rappel porte la vedette du gain **tel qu'il est dit chez lui**. La ligne
    de la catégorie qui rappelle n'a pas d'apport écrit : sans cela, le rappel
    sort vide.
    """
    table = {}
    for l in positions['lignes']:
        if (l.get('position') == 'gagnant' and l.get('vedette')
                and ATTACHE_CARTE.get(l['ancrage']) == l['categorie']):
            table[l['ancrage']] = l['vedette']
    return table


def matiere(positions, ref, cid):
    """Tout ce qu'une fiche a le droit d'afficher, et rien de plus."""
    cats = {c['id']: c for c in positions['categories']}
    lib = libelles(ref)
    cat = cats[cid]
    groupe = next((g['titre'] for g in positions['groupes']
                   if cid in g['categories']), '')
    lignes = [l for l in positions['lignes'] if l['categorie'] == cid]
    rang = {a: i for i, a in enumerate(positions.get('promesses', []))}

    gains, pertes, tous_perdants = [], [], []
    for l in lignes:
        court = lib.get(l['ancrage'], l['ancrage'])
        if l['position'] == 'gagnant':
            # Une modalité dit comment un gain arrive ; elle ne prend pas de
            # ligne. Restituer n'est pas réciter.
            if l.get('modalite'):
                continue
            texte = l.get('apport') or ''
            vedette = l.get('vedette') or ''
            affichee = vedette or quantite(texte or court)
            gains.append({
                'cle': l['ancrage'],
                'texte': texte or court,
                'transitoire': not texte,
                'vedette': affichee,
                'ecrite': bool(vedette),
                'chiffree': bool(re.search(r'\d', affichee)),
                'contrepartie': l.get('contrepartie') or '',
                'rang': l.get('rang_fiche', 10**6),
                # Un gain dont l'attache est ailleurs revient en rappel.
                'rappel': l['ancrage'] in ATTACHE_CARTE
                and ATTACHE_CARTE[l['ancrage']] != cid,
            })
        # Un capteur est une rente supprimée, non une perte portée par une
        # personne : il ne paraît que sur la fiche d'une catégorie de rente,
        # dont il est justement le sujet.
        elif l['position'] == 'perdant' or (l['position'] == 'capteur'
                                            and 'rente' in groupe.lower()):
            tous_perdants.append(l)
            # Deux pertes qui disent le même événement à deux mailles ne font
            # pas deux cartes.
            if l.get('redite'):
                continue
            # La fiche choisit ses pertes comme ses gains : la structure
            # arbitrée dit lesquelles paraissent (A-179).
            if cid in PERTES_CARTE and l['ancrage'] not in PERTES_CARTE[cid]:
                continue
            source = l.get('grandeur_derivee')
            if source == 'qualitatif':
                source = ''
            pertes.append({
                'cle': l['ancrage'],
                'libelle': l.get('libelle') or court,
                'ecrit': bool(l.get('libelle')),
                'vedette': l.get('vedette_perte') or '',
                'chiffre': quantite(source) or quantite(l.get('justification')),
                'justification': l.get('justification') or '',
                'raccroche': l.get('raccroche') or '',
            })

    # L'ordre propre à la catégorie passe devant celui des promesses : ce qui
    # compte pour un jeune adulte n'est pas ce qui compte pour un retraité.
    rappels = [g for g in gains if g['rappel']]
    gains = [g for g in gains if not g['rappel']]
    # A-188 — une fiche trop mince ne se lit pas en pied. Sous trois gains
    # propres, les rappels **pour lesquels un apport a été écrit dans cette
    # catégorie** remontent en ligne pleine : la matière est dite ailleurs, mais
    # sous un autre angle, écrit exprès pour elle. Le rappel nu reste la règle
    # dès que la fiche tient debout toute seule.
    if len(gains) < SEUIL_MINCE:
        promus = [g for g in rappels if not g['transitoire'] and g['ecrite']]
        for g in promus:
            g['rappel'] = False
        rappels = [g for g in rappels if g['rappel']]
        gains += promus
    _va = vedettes_attachees(positions)
    for g in rappels:
        if _va.get(g['cle']):
            g['vedette'] = _va[g['cle']]
    _o = ORDRE_CARTE.get(cid, [])
    for g in gains:
        g['rang'] = _o.index(g['cle']) if g['cle'] in _o else 10**6
    gains.sort(key=lambda g: (g['rang'], rang.get(g['cle'], 10**6),
                              not g['chiffree']))

    # Les pertes suivent l'ordre de la structure, comme les gains.
    _p = PERTES_CARTE.get(cid, [])
    pertes.sort(key=lambda x: _p.index(x['cle']) if x['cle'] in _p else 10**6)

    vus = set()
    for p in pertes:
        vers = p['raccroche'].split('|')[0] if p['raccroche'] else ''
        p['vers'] = next((g for g in gains if g['cle'] == vers), None)
        p['repete'] = bool(p['vers']) and p['vers']['cle'] in vus
        if p['vers']:
            vus.add(p['vers']['cle'])

    moins_dabord = bool(tous_perdants) and len(tous_perdants) / max(
        1, len(tous_perdants) + len(gains)) > PART_PERTES

    # Le gain qui raccroche passe en tête **seulement** quand la fiche ouvre
    # sur une perte : c'est alors lui que la personne cherche. Ailleurs, l'ordre
    # des promesses commande, et une contrepartie n'est pas une promesse.
    cible = next((p['vers'] for p in pertes if p['vers']), None)
    if moins_dabord and cible is not None:
        gains.remove(cible)
        gains.insert(0, cible)

    return {
        'titre': TITRES_CARTE.get(
            cid, TITRES_PROPOSES.get(cid, cat['terme'].capitalize())),
        'axe': AXES.get(cid, ''),
        'propose': cid in TITRES_PROPOSES,
        'definition': cat['definition'],
        'effectif': cat['effectif'],
        # Le partage se lit sur tout ce que le référentiel porte, redites
        # comprises : c'est le poids de la perte qui commande l'ouverture, pas
        # le nombre de cartes que la fiche imprime.
        'moins_dabord': moins_dabord,
        'groupe': groupe,
        'grappes': grouper(gains)[:PLAFOND],
        'rappels': rappels,
    }, gains, pertes


def grouper(gains):
    """Les gains repliés par grappe : [(tête, [suite])], dans l'ordre reçu.

    La grappe se compte par levier, tête comprise. **Un gain qui porte une
    vedette écrite ne se replie jamais** : il a quelque chose que les autres
    n'ont pas, et « Le temps » ne se range pas sous « 70 % ». Il peut en
    revanche mener la grappe — c'est le cas de « Votre capital », qui coiffe
    les trois autres gains de la retraite.
    """
    def levier(g):
        m = LEVIER.match(g['cle'])
        return m.group(1) if m else g['cle']

    compte = {}
    for g in gains:
        compte[levier(g)] = compte.get(levier(g), 0) + 1

    sortie, pris = [], set()
    for g in gains:
        if g['cle'] in pris:
            continue
        lot = [x for x in gains if levier(x) == levier(g)]
        # La tête est le membre qui porte une vedette écrite, s'il est seul à
        # en porter une ; sinon le premier venu.
        avec = [x for x in lot if x['ecrite']]
        chef = avec[0] if len(avec) == 1 else lot[0]
        suite = [x for x in lot if x is not chef and not x['ecrite']]
        if len(lot) >= GRAPPE and suite:
            sortie.append((chef, suite))
            pris.add(chef['cle'])
            pris.update(x['cle'] for x in suite)
        else:
            sortie.append((g, []))
            pris.add(g['cle'])
    return sortie


# --------------------------------------------------------------------------
# Feuille. Esthétique provisoire de référence : ocre, rouge, vert profond,
# Fraunces et JetBrains Mono, grille éditoriale. La signature Résolution tient
# en trois choses — le bloc-marque en tête, le filet à trois couleurs, et le
# cartouche de pied. Rien de plus tant que la charte n'est pas écrite.
# --------------------------------------------------------------------------
STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=JetBrains+Mono:wght@400;700&display=swap');
:root{
 --enc:#1a1a1a; --pap:#fdfcfa; --creme:#f6f2ea; --fil:#ddd7cd;
 --gain:#1f5c3a; --perte:#8a2f22; --ocre:#6b5b3e; --gris:#6d6a64;
 --rose:#fbeae7; --sable:#f7f3e8; --nuit:#16150f;
 --titre:'Fraunces',Georgia,'Iowan Old Style',serif;
 --mono:'JetBrains Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
}
*{box-sizing:border-box}
body{margin:0;background:var(--nuit);color:var(--enc);padding:1.4rem 1rem;
 font:16px/1.5 var(--titre);-webkit-font-smoothing:antialiased}
.page{max-width:40rem;margin:0 auto 1.4rem;background:var(--pap);
 padding:0 0 1.6rem;box-shadow:0 2px 0 rgba(0,0,0,.35)}

/* --- signature Résolution ---------------------------------------------- */
.marque{display:flex;align-items:baseline;justify-content:space-between;
 gap:1rem;padding:1.1rem 1.8rem .7rem}
.marque .nom{font:700 12px/1 var(--mono);letter-spacing:.32em;
 text-transform:uppercase;color:var(--enc)}
.marque .quoi{font:400 10px/1.3 var(--mono);letter-spacing:.12em;
 text-transform:uppercase;color:var(--gris);text-align:right}
.filet{display:flex;height:4px;margin:0 1.8rem}
.filet i{flex:1} .filet i:nth-child(1){background:var(--gain)}
.filet i:nth-child(2){background:var(--ocre);flex:.45}
.filet i:nth-child(3){background:var(--perte);flex:.2}

/* --- tête de fiche ------------------------------------------------------ */
.tete{padding:1.5rem 1.8rem 1.1rem;border-bottom:1px solid var(--fil)}
.qui{font-size:2.1rem;line-height:1.08;font-weight:700;margin:0 0 .35rem;
 letter-spacing:-.02em}
.propose{display:inline-block;margin-left:.5rem;font:400 9px/1.6 var(--mono);
 letter-spacing:.05em;text-transform:uppercase;color:#a8632a;
 border:1px solid #e0c7a8;background:#fbf3e7;padding:0 .3rem;vertical-align:.4em}
.sur{margin:0 0 .5rem;font:700 10px/1 var(--mono);letter-spacing:.18em;
 text-transform:uppercase;color:var(--ocre)}
.def{margin:0;color:var(--gris);font-size:.95rem}
.lib{font-weight:600}
.compte{font:700 10.5px/1 var(--mono);letter-spacing:.12em;
 text-transform:uppercase;color:var(--ocre);margin:.8rem 0 0}

.corps{padding:0 1.8rem}
.bande{font:700 10.5px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;
 padding:.55rem 1.8rem;margin:1.5rem -1.8rem .9rem;color:var(--pap)}
.bande.g{background:var(--gain)} .bande.p{background:var(--perte)}

/* --- le côté moins : une carte, jamais une ligne ------------------------ */
.perte{background:var(--rose);border-left:4px solid var(--perte);
 padding:.85rem 1rem;margin:0 0 .7rem}
.perte .n{font:700 1.15rem/1 var(--titre);color:var(--perte);display:block;
 margin-bottom:.25rem;letter-spacing:-.01em}
.perte .l{font-size:1rem}
.perte .j{display:block;margin-top:.35rem;color:#6a4a44;font-size:.89rem}
.perte .r{display:block;margin-top:.6rem;padding-top:.55rem;
 border-top:1px solid #eccfc9;color:var(--gain);font-size:.93rem}
.perte .r b{font-weight:600}
.perte .r em{font-style:normal;font-family:var(--mono);font-weight:700}
.perte .r.meme{color:var(--gris);font-style:italic}
.transitoire{border-bottom:1px dotted var(--gris);color:var(--gris)}
.trou{display:inline-block;margin-left:.4rem;font:400 9px/1.6 var(--mono);
 font-style:normal;letter-spacing:.05em;text-transform:uppercase;color:#a8632a;
 border:1px solid #e0c7a8;background:#fbf3e7;padding:0 .3rem;vertical-align:.1em}

/* --- le côté plus : la tête en grand, puis des lignes ------------------- */
.dom{background:var(--gain);color:var(--pap);padding:1.4rem 1.3rem;margin:0}
.dom .v{font:700 3.6rem/.92 var(--mono);letter-spacing:-.045em;display:block;
 word-spacing:-.38em}
.dom .v.mot{font:700 2.5rem/1 var(--titre);letter-spacing:-.02em;
 word-spacing:normal}
.dom .p{margin:.55rem 0 0;font-size:1.06rem;max-width:26rem}
.dom .s{margin:.45rem 0 0;font-size:.98rem;opacity:.88;max-width:26rem}
.lg{display:grid;grid-template-columns:7.2rem 1fr;gap:.55rem 1rem;
 padding:.75rem 0;border-bottom:1px solid var(--fil);align-items:baseline}
.lg .v{text-align:right;font:700 1.45rem/1 var(--mono);color:var(--gain);
 letter-spacing:-.03em;word-spacing:-.38em;white-space:nowrap}
.lg .v.mot{font:700 1.1rem/1.2 var(--titre);letter-spacing:0;word-spacing:normal;
 white-space:normal}
.lg .v.long{font-size:1rem}
.lg .t{font-size:1rem}
.lg .m{display:block;color:var(--gris);font-size:.84rem;margin-top:.25rem}
.suite{grid-column:2;margin:.45rem 0 0;padding-left:.85rem;
 border-left:2px solid var(--fil);list-style:none}
.suite li{color:#3a3a38;font-size:.93rem;padding:.15rem 0}
.suite li::before{content:'·';color:var(--gain);font-weight:700;
 margin-right:.45rem}

/* --- qui paie, dit une fois --------------------------------------------- */


.rappel{margin:.9rem 0 0;padding:.6rem 0 0;border-top:1px solid var(--fil);
 color:var(--gris);font-size:.92rem;line-height:1.9}
.rappel span{display:block;font:700 9.5px/1 var(--mono);letter-spacing:.14em;
 text-transform:uppercase;color:var(--ocre);margin-bottom:.35rem}
.rappel b{font-weight:600;color:var(--gain);font-family:var(--mono);
 font-size:.9em;word-spacing:-.3em}
.pied{margin:1.4rem 1.8rem 0;padding-top:.8rem;border-top:1px solid var(--fil);
 color:var(--gris);font-size:.78rem}
.interne{font:400 10px/1.5 var(--mono);color:#9a958c;margin-top:.5rem}
@media(max-width:600px){
 body{padding:.8rem .5rem}
 .corps,.tete{padding-left:1.1rem;padding-right:1.1rem}
 .bande{padding-left:1.1rem;padding-right:1.1rem;margin-left:-1.1rem;
  margin-right:-1.1rem}
 .marque{padding:.9rem 1.1rem .6rem}.filet{margin:0 1.1rem}
 .qui{font-size:1.65rem}.dom .v{font-size:2.8rem}
 .lg{grid-template-columns:5.6rem 1fr}.lg .v{font-size:1.2rem}
}
"""


def e(t):
    """Échappement, et espaces insécables de la typographie française."""
    t = html.escape(t or '')
    t = re.sub(r'\s+(%|€|;|:|!|\?|»)', '\u202f\\1', t)
    t = re.sub(r'(\d)\s+(\d{3})', '\\1\u202f\\2', t)
    return t


def classe_vedette(v):
    """Un chiffre se compose en mono, un mot en Fraunces. Même plan."""
    if not v or not re.search(r'\d', v):
        return 'v mot'
    return 'v long' if len(v) > 6 else 'v'


def etiquette(p):
    """Le libellé écrit sort net ; celui qui manque sort en pointillé."""
    if p['ecrit']:
        return f'<span class=lib>{e(p["libelle"])}</span>'
    return f'<span class=transitoire>{e(p["libelle"])}</span>'


def carte_perte(p):
    """La perte se dit comme le gain : une vedette, une phrase, sa raison.

    Elle ne redit pas le gain qui la raccroche. Sur une lecture linéaire, ce
    gain se lit quelques centimètres plus bas, à sa place et en grand : le
    répéter en petit au-dessus n'ajoute rien et fatigue.
    """
    o = ['<div class=perte>']
    if p['vedette']:
        o.append(f'<span class=n>{e(p["vedette"])}</span>')
    elif p['chiffre']:
        o.append(f'<span class=n>−{e(p["chiffre"])}</span>')
    o.append(f'<div class=l>{etiquette(p)}'
             f'<span class=j>{e(p["justification"])}</span></div>')
    o.append('</div>')
    return ''.join(o)


def fiche(ctx, gains, pertes, cid):
    n_g, n_p = len(gains), len(pertes)

    moins = ['<div class="bande p">Ce que vous perdez</div>'] if pertes else []
    moins += [carte_perte(p) for p in pertes]

    tete, suite_tete = ctx['grappes'][0] if ctx['grappes'] else (None, [])
    plus = (['<div class="bande g">Ce que vous gagnez</div>']
            if ctx['grappes'] or ctx['rappels'] else [])
    if tete:
        bloc = ['<div class=dom>']
        if tete['vedette']:
            cl = 'v mot' if not re.search(r'\d', tete['vedette']) else 'v'
            bloc.append(f'<span class="{cl}">{e(tete["vedette"])}</span>')
        bloc.append(f'<p class=p>{e(tete["texte"])}</p>')
        for g in suite_tete:
            bloc.append(f'<p class=s>· {e(g["texte"])}</p>')
        bloc.append('</div>')
        plus.append(''.join(bloc))
    for g, suite in ctx['grappes'][1:]:
        v = (f'<div class="{classe_vedette(g["vedette"])}">'
             f'{e(g["vedette"]) or "+"}</div>')
        txt = (e(g['texte']) if not g['transitoire']
               else f'<span class=transitoire>{e(g["texte"])}</span>')
        prop = (f'<span class=m>{e(g["contrepartie"])}</span>'
                if g['contrepartie']
                and g['contrepartie'] != CONTREPARTIE_GENERALE else '')
        bloc = [f'<div class=lg>{v}<div class=t>{txt}{prop}</div>']
        if suite:
            bloc.append('<ul class=suite>' + ''.join(
                f'<li>{e(x["texte"])}</li>' for x in suite) + '</ul>')
        bloc.append('</div>')
        plus.append(''.join(bloc))

    # Qui paie, dit une fois. La contrepartie propre reste sur sa ligne.

    titre = e(ctx['titre'])
    def pl(n, mot):
        return f'{n} {mot}' + ('s' if n > 1 else '')

    bouts = [e(ctx['effectif'])] if ctx['effectif'] else []
    if n_p:
        bouts.append(pl(n_p, 'perte'))
    bouts.append(pl(n_g, 'gain'))
    compte = ' · '.join(bouts)

    if ctx['rappels']:
        vus, mots = set(), []
        for g in ctx['rappels']:
            v = g['vedette'] or ''
            if v and v not in vus:
                vus.add(v)
                mots.append(f'<b>{e(v)}</b>')
        if mots:
            plus.append('<p class=rappel><span>Et comme chacun</span>'
                        + ' · '.join(mots) + '</p>')

    corps = moins + plus if ctx['moins_dabord'] else plus + moins
    return ('<div class=page>'
            '<div class=marque><span class=nom>Résolution</span>'
            '<span class=quoi>Ce que le plan change pour vous</span></div>'
            '<div class=filet><i></i><i></i><i></i></div>'
            f'<div class=tete><p class=sur>{e(ctx["groupe"])}</p>'
            f'<h1 class=qui>{titre}</h1>'
            f'<p class=def>{e(ctx["axe"] or ctx["definition"])}</p>'
            f'<p class=compte>{compte}</p></div>'
            '<div class=corps>' + ''.join(corps) + '</div></div>')


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return 2
    positions = json.load(open(argv[1], encoding='utf-8'))
    ref = json.load(open(argv[2], encoding='utf-8'))
    sortie = argv[3]
    os.makedirs(sortie, exist_ok=True)
    rang = {c: (i, j) for i, g in enumerate(positions['groupes'])
            for j, c in enumerate(g['categories'])}
    corps = []
    for cid in sorted(FICHES, key=lambda c: rang.get(c, (99, 99))):
        ctx, gains, pertes = matiere(positions, ref, cid)
        corps.append(fiche(ctx, gains, pertes, cid))
    page = ('<!doctype html><html lang=fr><meta charset=utf-8>'
            '<meta name=viewport content="width=device-width,initial-scale=1">'
            '<title>Résolution — fiches gagnants-perdants</title>'
            f'<style>{STYLE}</style>' + ''.join(corps) + '</html>')
    chemin = os.path.join(sortie, 'galerie_fiches.html')
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'{chemin} — {os.path.getsize(chemin)} o · {len(FICHES)} fiche(s)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
