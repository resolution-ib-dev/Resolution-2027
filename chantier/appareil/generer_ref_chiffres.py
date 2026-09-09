# -*- coding: utf-8 -*-
"""REF_chiffres — le référentiel des faits, et rien que ce qui est traçable.

Le corpus portait ses chiffres à trois endroits, sans point de vérité unique : le
manuscrit et ses notes de fin, le `REF_doctrine` pour ceux qui sont rattachés à
une proposition, et un proto de relevé qui en portait cent neuf sans source. Un
même chiffre pouvait donc vivre trois fois, sous trois unités et trois
millésimes, sans que rien ne le dise.

Ce référentiel les met tous au même endroit, avec le même schéma, et **déclare ce
qu'il ne sait pas**. Il ne complète rien.

## Le schéma d'une entrée

    id            identifiant de l'entrée, formé du lieu d'origine
    valeur        la valeur telle qu'elle est écrite au corpus
    valeur_num    la même, normalisée, ou null si le relevé n'a pas su la lire
    unite         l'unité, ou null
    millesime     l'année de la donnée, ou null — jamais devinée
    source        d'où vient le chiffre, tel que le corpus l'énonce, ou null
    derivation    l'opération qui le produit, ou null
    declinaisons  les valeurs secondaires que le même énoncé porte
    code_origine  le code sous lequel il vivait avant ce référentiel
    codes_preuve  les identifiants de passage du manuscrit, quand ils existent
    confiance     0 à 3, voir plus bas
    a_sourcer     vrai quand la confiance est nulle
    provenance    note · ref_doctrine · proto
    enonce        l'énoncé qui porte le chiffre
    enonce_regenere  vrai quand l'énoncé est extrait à la génération et n'est
                     donc pas un texte du référentiel

## Les quatre niveaux de confiance

    3  strate 1 — le manuscrit, corps ou note de fin, point de vérité
    2  source déclarée au corpus — un classeur nommé, une autorité citée
    1  ancrage ou opération — rattaché à un passage du manuscrit, ou produit par
       une opération que le contrôle arithmétique rejoue, mais sans source
    0  sans source — un candidat, à sourcer

**Une opération rejouée dit que le compte est juste, non qu'il est sourcé.** Les
deux ne se confondent pas : elle vaut un ancrage, jamais une source.

**Aucune source ne s'invente et aucun trou ne se comble.** Un chiffre sans source
traçable sort en confiance nulle, marqué à sourcer, et le contrôle le compte.

## Ce que le générateur relève, et ce qu'il ne relève pas

Il relève mécaniquement : la valeur et son unité par lecture de l'énoncé, le
millésime quand le corpus l'écrit, l'opération quand elle est portée, les
identifiants d'origine et de preuve, la source telle qu'elle est énoncée.

Il hérite aussi : un sous-item ou un paramètre qui ne déclare aucune source
prend celle de l'effet de sa proposition, parce qu'il vient du même décompte.
L'entrée porte alors `source_heritee`.

Il ne relève pas : une unité qu'il faut deviner, un millésime qu'il faut inférer
d'un contexte, une source qui n'est écrite nulle part, ni chez le nœud ni chez
sa proposition. Ces champs restent nuls, et
`appareil/sources_chiffres.py` est le seul endroit où ils se remplissent, à la
main, une entrée à la fois.

**Les énoncés tirés des notes du manuscrit ne sont pas un texte du référentiel.**
Ils sont extraits de `referentiels/notes_manuscrit.json` à chaque génération et
portent `enonce_regenere`. Le manuscrit reste seul point de vérité : rien ici ne
se corrige à la main, tout se corrige à la source puis se rejoue.

Usage : python3 generer_ref_chiffres.py ../referentiels/notes_manuscrit.json \\
            ../referentiels/REF_doctrine.json \\
            ../sources/Donnees_20260806_v1_proto.html \\
            ../referentiels/REF_chiffres.json
"""
import html
import json
import re
import sys

import sources_chiffres

# Ce que le relevé écarte, et pourquoi. Rien ne se perd en silence : le compte
# sort à chaque génération.
ECARTES = []

CONFIANCE = {
    3: 'strate1',
    2: 'source_declaree',
    1: 'ancrage_ou_operation',
    0: 'sans_source',
}

# Un nombre nu compris dans cette fenêtre, seul dans son énoncé et sans unité,
# est une date de publication, non un fait. Il ne devient pas une entrée.
ANNEES = (1900, 2099)

# Vocabulaire fermé des unités. Le plus long d'abord : « Md€/an » avant « Md€ ».
# Une unité qui n'est pas là n'est pas devinée — le champ reste nul.
UNITES = [
    'Md€/an', 'M€/an', 'k€/an', '€/an', '€/mois', '€/heure', '€/h',
    'Md€', 'M€', 'k€', '€',
    'points de PIB', 'point de PIB', 'points de croissance', 'pt de PIB',
    'points', 'point', 'pts', 'pt',
    '%/an', '%',
    'millions', 'milliards', 'M', 'Md',
    'ans', 'an', 'années', 'année', 'mois', 'jours', 'jour',
    'postes', 'agences', 'pages', 'taxes', 'impôts', 'niches',
    'ETP', 'fois', 'rang',
]
UNITE_RE = '|'.join(re.escape(u) for u in UNITES)

# Un nombre à la française : signe, milliers séparés par une espace fine ou
# ordinaire, décimales à la virgule. `≈` et `environ` ne changent pas la valeur,
# ils changent le registre — ils sont retenus dans `approx`.
NOMBRE = r'(?P<approx>≈|environ\s+|de l’ordre de\s+|autour de\s+|aux alentours de\s+|près de\s+|De l’ordre de\s+|Environ\s+|Près de\s+)?' \
         r'(?P<signe>[−+-]?)\s?(?P<n>\d{1,3}(?:[   ]\d{3})+|\d+(?:,\d+)?)'
VALEUR_RE = re.compile(NOMBRE + r'\s?(?P<u>' + UNITE_RE + r')?')

# Une abréviation d'initiale — « B. Born » — n'est pas une fin de phrase.
INITIALE = re.compile(r'(?:\b[A-ZÀ-Ü]|\ball|\bn°|\bcf|\bart)\.$')


# --------------------------------------------------------- millésime par défaut
# Convention arrêtée par l'auteur le 20260824. Le corpus n'écrit son millésime
# que rarement, et un chiffre sans année est indéfendable au dehors. À défaut
# d'année déclarée, la donnée est de 2024 ; elle est de 2026 quand elle vient
# d'un document budgétaire, seul millésime où le détail existe.
#
# **Une convention n'est pas une déclaration.** Le champ `millesime_origine` dit
# lequel des deux on lit : `declare` quand le corpus l'écrit, `defaut` ou
# `defaut_budgetaire` quand c'est la convention qui parle. Aucun livrable ne cite
# un millésime de convention comme s'il était sourcé.
MILLESIME_DEFAUT = '2024'
MILLESIME_BUDGETAIRE = '2026'
SOURCE_BUDGETAIRE = re.compile(
    r'PLF|projet de loi de finances|loi de finances|LFI|budg[eé]t', re.I)


def millesime_par_convention(source):
    """Rend le millésime de convention et son origine, jamais une déclaration."""
    if source and SOURCE_BUDGETAIRE.search(source):
        return MILLESIME_BUDGETAIRE, 'defaut_budgetaire'
    return MILLESIME_DEFAUT, 'defaut'


def _est_le_millesime(d, millesime):
    """Un nombre nu qui vaut le millésime est le millésime, pas un chiffre."""
    return (d['unite'] is None and millesime
            and d['valeur_num'] is not None
            and str(int(d['valeur_num'])) == str(millesime))


def phraser(texte):
    """Découpe un énoncé en phrases, sans casser sur une initiale."""
    phrases = []
    for m in re.split(r'(?<=[.;:])\s+', texte):
        m = m.strip()
        if not m:
            continue
        if phrases and INITIALE.search(phrases[-1]):
            phrases[-1] = phrases[-1] + ' ' + m
        else:
            phrases.append(m)
    return phrases



def _num(txt):
    """« 1 270 » → 1270.0 ; « 9,2 » → 9.2 ; le reste → None."""
    t = txt.replace(' ', '').replace(' ', '').replace(' ', '')
    t = t.replace(',', '.')
    try:
        return float(t)
    except ValueError:
        return None


def est_une_date(tetes):
    """Vrai quand l'énoncé ne porte qu'un nombre nu dans la fenêtre des années."""
    if len(tetes) != 1:
        return False
    t = tetes[0]
    return (t['unite'] is None and t['valeur_num'] is not None
            and float(t['valeur_num']).is_integer()
            and ANNEES[0] <= t['valeur_num'] <= ANNEES[1])


def lire_valeurs(enonce):
    """Toutes les valeurs d'un énoncé, dans l'ordre. La première est la tête."""
    if not enonce:
        return []
    trouves = []
    for m in VALEUR_RE.finditer(enonce):
        n = _num(m.group('n'))
        if n is None:
            continue
        signe = -1 if m.group('signe') in ('−', '-') else 1
        trouves.append({
            'valeur': m.group(0).strip(),
            'valeur_num': signe * n,
            'unite': m.group('u'),
            'approche': bool(m.group('approx')),
        })
    return trouves


def millesime_de(*textes):
    """L'année, quand le corpus l'écrit. Jamais inférée d'un contexte."""
    for t in textes:
        if not t:
            continue
        m = re.search(r'donn[ée]es?\s+(\d{4})', t)
        if m:
            return m.group(1)
        m = re.search(r'\ben\s+(19|20)(\d{2})\b', t)
        if m:
            return m.group(1) + m.group(2)
    return None


def entree(ident, provenance, enonce, tetes, **champs):
    """Une entrée du référentiel, avec ses seuls champs remplis."""
    tete = tetes[0] if tetes else {}
    e = {
        'id': ident,
        'valeur': tete.get('valeur'),
        'valeur_num': tete.get('valeur_num'),
        'unite': champs.get('unite') or tete.get('unite'),
        'millesime': champs.get('millesime'),
        'source': champs.get('source'),
        'derivation': champs.get('derivation'),
        'declinaisons': [
            {'valeur': d['valeur'], 'valeur_num': d['valeur_num'],
             'unite': d['unite']} for d in tetes[1:]
            if not _est_le_millesime(d, champs.get('millesime'))
        ] + list(champs.get('declinaisons') or []),
        'code_origine': champs.get('code_origine'),
        'codes_preuve': champs.get('codes_preuve') or [],
        'provenance': provenance,
        'enonce': enonce,
        'enonce_regenere': bool(champs.get('enonce_regenere')),
        'approche': tete.get('approche', False),
    }
    # La main l'emporte sur le relevé, et seulement là où elle a écrit.
    main = sources_chiffres.sourcer(ident)
    for cle in ('source', 'millesime', 'derivation', 'unite', 'valeur'):
        if main.get(cle):
            e[cle] = main[cle]
    # `valeur_num` se réécrit à part : elle admet zéro et le négatif, et c'est
    # elle que le relevé se trompe le plus souvent à prendre — un énoncé de la
    # forme « en 2024, X vaut Y » lui donne l'année pour tête. La main la
    # redresse, et l'entrée le dit.
    if 'valeur_num' in main:
        e['valeur_num'] = main['valeur_num']
        e['tete_redressee'] = True
    if main.get('note'):
        e['note_sourcage'] = main['note']
    e['sourcee_a_la_main'] = bool(main)

    # Le rapprochement écrit à la main. Il vit dans son propre bloc :
    # **rapprocher n'est pas sourcer**, et une entrée rapprochée reste sans
    # source tant que personne ne lui en a écrit une — `sourcee_a_la_main` ne
    # bouge donc pas ici. Le bloc l'emporte sur un `meme_que` porté par
    # C'est le seul endroit où un rapprochement s'écrit.
    rapp = sources_chiffres.meme_que(ident)
    if rapp:
        e['fait_partage'] = rapp['fait_partage']
        if rapp.get('meme_que'):
            e['meme_que'] = rapp['meme_que']
        else:
            e.pop('meme_que', None)
            e['reference_du_fait'] = True

    # Le millésime : déclaré s'il est écrit, de convention sinon. Le champ dit
    # lequel, de sorte qu'un 2024 de convention ne passe jamais pour un 2024
    # relevé au corpus.
    if e['millesime']:
        e['millesime_origine'] = 'declare'
    else:
        e['millesime'], e['millesime_origine'] = millesime_par_convention(
            e['source'])

    # Une opération rejouée dit que le compte est juste, pas qu'il est sourcé.
    # Les deux ne se confondent pas : elle vaut un ancrage, pas une source.
    verifiee = bool(champs.get('operation_rejouee'))
    e['operation_rejouee'] = verifiee
    if provenance == 'note':
        e['confiance'] = 3
    elif e['source']:
        e['confiance'] = 2
    elif e['codes_preuve'] or verifiee:
        e['confiance'] = 1
    else:
        e['confiance'] = 0
    e['confiance_libelle'] = CONFIANCE[e['confiance']]
    e['a_sourcer'] = e['confiance'] == 0
    return e


# ------------------------------------------------------------------- les notes
def des_notes(chemin):
    """Les chiffres des notes de fin du manuscrit. Strate 1."""
    notes = json.load(open(chemin, encoding='utf-8'))['notes']
    out = []
    for n in notes:
        if not n['porte_un_chiffre']:
            continue
        # Une phrase par valeur : l'énoncé est découpé à la ponctuation forte,
        # et seules les phrases qui portent un nombre sortent.
        phrases = phraser(n['texte'])
        rang = 0
        for ph in phrases:
            tetes = lire_valeurs(ph)
            if not tetes:
                continue
            if est_une_date(tetes):
                ECARTES.append(('note', n['id'], ph))
                continue
            rang += 1
            out.append(entree(
                f"N-{n['id']}-{rang}", 'note', ph, tetes,
                millesime=millesime_de(ph),
                source=f"manuscrit, note de fin {n['id']}",
                code_origine=n['id'],
                codes_preuve=[n['section']],
                enonce_regenere=True))
    return out


# ------------------------------------------------------------- le REF_doctrine
def _source_ref(noeud):
    """La source telle que le nœud l'énonce. Jamais autre chose.

    `ancre` n'en est pas une : c'est l'ancre du passage qui porte l'énoncé, donc
    un ancrage. Elle part aux codes de preuve, jamais au champ `source`.
    """
    for cle in ('certitude', 'source_ancre'):
        v = noeud.get(cle)
        if v:
            return v
    return None


def _chaine(noeud):
    out = []
    for c in noeud.get('chaine') or []:
        lu = lire_valeurs(str(c.get('valeur') or ''))
        tete = lu[0] if lu else {}
        out.append({'valeur': c.get('valeur'),
                    'valeur_num': tete.get('valeur_num'),
                    'unite': tete.get('unite'),
                    'composant': c.get('composant'),
                    'origine': c.get('origine'),
                    'statut': c.get('statut')})
    return out


def _porteurs(ref):
    """Tout ce que le REF_doctrine porte de chiffré, avec son chemin.

    Troisième valeur : la source déclarée par la proposition qui porte le nœud.
    Un sous-item ou un paramètre qui ne déclare rien vient du même décompte que
    l'effet de sa proposition — ce n'est pas une source inventée, c'est la même
    source, héritée, et l'entrée le dit.
    """
    for ax in ref['axes']:
        for e in ax.get('effets_diagnostic', []):
            yield e, 'effet_diagnostic', None
        for g in ax.get('gains_indirects', []):
            yield g, 'gain_indirect', None
        for lev in ax.get('leviers', []):
            for p in lev.get('propositions', []):
                # La source de la proposition est celle du premier de ses effets
                # qui en déclare une.
                heritee = None
                for ef in p.get('effets', []):
                    heritee = _source_ref(ef)
                    if heritee:
                        break
                for pa in p.get('parametres', []):
                    yield pa, 'parametre', heritee
                for ef in p.get('effets', []):
                    yield ef, 'effet', heritee
                for si in p.get('sous_items', []):
                    yield si, 'sous_item', heritee
    for l in ref.get('lexique', []):
        terme = (l.get('terme') or 'terme').replace(' ', '-')
        for n, b in enumerate(l.get('branches', []), 1):
            yield dict(b, id=b.get('id') or f'lexique-{terme}-b{n}'), \
                'lexique_branche', l.get('source_ancre')
        for n, i in enumerate(l.get('illustrations', []), 1):
            yield dict(i, id=i.get('id') or f'lexique-{terme}-i{n}'), \
                'lexique_illustration', l.get('source_ancre')


def du_ref(chemin):
    """Les chiffres du REF_doctrine, chacun avec ce que son nœud déclare."""
    ref = json.load(open(chemin, encoding='utf-8'))
    out = []
    for noeud, genre, heritee in _porteurs(ref):
        enonce = noeud.get('chiffre') or noeud.get('valeur')
        if not enonce:
            continue
        if not isinstance(enonce, str):
            enonce = str(enonce)
        intitule = noeud.get('enonce') or noeud.get('nom') or noeud.get('intitule')
        tetes = lire_valeurs(enonce)
        # Un paramètre qui énumère un périmètre n'est pas un fait chiffré. Le
        # référentiel des faits ne porte que ce qui porte un nombre.
        if not tetes:
            ECARTES.append(('ref_doctrine', noeud.get('id'), enonce))
            continue
        if est_une_date(tetes):
            ECARTES.append(('ref_doctrine', noeud.get('id'), enonce))
            continue
        ident = 'R-' + (noeud.get('id') or noeud.get('origine') or genre)
        out.append(entree(
            ident, 'ref_doctrine', enonce, tetes,
            unite=noeud.get('unite'),
            millesime=millesime_de(noeud.get('base'), noeud.get('date_effet'),
                                   noeud.get('horizon')),
            source=_source_ref(noeud) or heritee,
            source_heritee=not _source_ref(noeud) and bool(heritee),
            derivation=noeud.get('operation'),
            declinaisons=_chaine(noeud),
            code_origine=noeud.get('id'),
            codes_preuve=(noeud.get('ids') or [])
                         + ([noeud['ancre']] if noeud.get('ancre') else []),
            operation_rejouee=bool(noeud.get('operation')
                                   and noeud.get('exact') is not None),
            intitule=intitule))
        out[-1]['intitule'] = intitule
        out[-1]['genre'] = genre
        out[-1]['source_heritee'] = (not _source_ref(noeud)) and bool(heritee)
    return out


# ------------------------------------------------------------ le proto Données
CANDIDAT = re.compile(
    r'<p class="[^"]*candidat-chiffre[^"]*"([^>]*)>(.*?)</p>', re.S)
ATTR = re.compile(r'([\w-]+)="([^"]*)"')
RUBRIQUE = re.compile(r'<section class="rubrique"[^>]*data-titre="([^"]*)"')


def du_proto(chemin):
    """Les candidats du proto. Aucun n'a de source : tous entrent à zéro."""
    s = open(chemin, encoding='utf-8').read()
    # La rubrique courante, pour situer chaque candidat sans rien inventer.
    coupes = [(m.start(), m.group(1)) for m in RUBRIQUE.finditer(s)]
    out = []
    for m in CANDIDAT.finditer(s):
        attrs = dict(ATTR.findall(m.group(1)))
        texte = re.sub(r'<[^>]+>', '', m.group(2))
        texte = html.unescape(re.sub(r'\s+', ' ', texte)).strip()
        rubrique = None
        for pos, titre in coupes:
            if pos < m.start():
                rubrique = titre
        code = attrs.get('id') or f'D-?{len(out) + 1:03d}'
        derivation = attrs.get('data-derivation')
        out.append(entree(
            'P-' + code, 'proto', texte, lire_valeurs(texte),
            # `a-documenter` n'est pas une dérivation, c'est l'aveu qu'il n'y en
            # a pas. Il ne se recopie pas dans le champ.
            derivation=None if derivation == 'a-documenter' else derivation,
            code_origine=code))
        out[-1]['rubrique'] = rubrique
        # L'unité que le proto déclare n'est pas rapportée à la valeur de tête :
        # elle porte parfois sur une autre valeur de la même ligne. Elle se
        # garde à part, telle quelle, et ne remplit pas le champ `unite`.
        out[-1]['unite_declaree_proto'] = attrs.get('data-unite')
        out[-1]['statut_origine'] = attrs.get('data-statut')
        out[-1]['derivation_a_documenter'] = derivation == 'a-documenter'
    return out


# --------------------------------------------------------------- la génération
def generer(chemin_notes, chemin_ref, chemin_proto, dst):
    entrees = des_notes(chemin_notes) + du_ref(chemin_ref) + du_proto(chemin_proto)

    par_confiance = {}
    for e in entrees:
        par_confiance[e['confiance']] = par_confiance.get(e['confiance'], 0) + 1
    par_provenance = {}
    for e in entrees:
        par_provenance[e['provenance']] = par_provenance.get(e['provenance'], 0) + 1

    ref = {
        '_revision': {
            'version': 'REF_chiffres v1',
            'objet': "référentiel des faits — un point de vérité par chiffre, "
                     "et la déclaration de ce qui n'est pas sourcé",
            'regle': "Aucune source ne s'invente, aucun trou ne se comble. Un "
                     "chiffre sans source traçable reste déclaré sans source.",
            'produit_par': 'appareil/generer_ref_chiffres.py',
            'sources_a_la_main': 'appareil/sources_chiffres.py',
        },
        'confiance': CONFIANCE,
        'entrees': entrees,
        'comptes': {
            'entrees': len(entrees),
            'par_provenance': par_provenance,
            'par_confiance': {CONFIANCE[k]: v
                              for k, v in sorted(par_confiance.items(),
                                                 reverse=True)},
            'a_sourcer': sum(1 for e in entrees if e['a_sourcer']),
            'sans_unite': sum(1 for e in entrees if not e['unite']),
            'sans_millesime': sum(1 for e in entrees if not e['millesime']),
            'millesime_par_origine': {
                k: sum(1 for e in entrees if e['millesime_origine'] == k)
                for k in ('declare', 'defaut', 'defaut_budgetaire')},
            'sourcees_a_la_main': sources_chiffres.compte(),
            'faits_rapproches': sources_chiffres.compte_meme_que()[0],
            'entrees_rapprochees': sum(1 for e in entrees
                                       if e.get('fait_partage')),
            'ecartes': len(ECARTES),
        },
    }
    with open(dst, 'w', encoding='utf-8') as f:
        json.dump(ref, f, ensure_ascii=False, indent=1)
        f.write('\n')

    c = ref['comptes']
    print(f"{dst} écrit — {c['entrees']} entrées "
          f"({', '.join(f'{k} {v}' for k, v in sorted(par_provenance.items()))})")
    print(f"  confiance : " + ' · '.join(
        f'{k} {v}' for k, v in c['par_confiance'].items()))
    print(f"  {c['a_sourcer']} à sourcer · {c['sans_unite']} sans unité · "
          f"{c['sourcees_a_la_main']} sourcée(s) à la main")
    print(f"  {c['faits_rapproches']} fait(s) rapproché(s) · "
          f"{c['entrees_rapprochees']} entrée(s) au rapprochement")
    print("  millésime : " + ' · '.join(
        f'{k} {v}' for k, v in c['millesime_par_origine'].items()))
    print(f"  {c['ecartes']} énoncé(s) écarté(s) — sans nombre, ou date seule")
    return 0


if __name__ == '__main__':
    sys.exit(generer(*sys.argv[1:5]))
