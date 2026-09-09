# -*- coding: utf-8 -*-
"""Les cinq relevés de lecture en creux, sur le socle du texte déposé (A-230).

A-230 range la lecture en creux au rang d'A-41 : **un jugement ne se délègue pas
au flair d'un modèle, il se mécanise par des dispositifs qui produisent des
signaux qu'ensuite on lit.** Ce module produit les signaux. Il ne les lit pas, ne
les hiérarchise pas et ne conclut rien : chaque relevé est une liste, à charge
de l'auteur de la lire.

A-230 nomme six dispositifs. **Cinq se calculent sur le socle, sans rouvrir le
PDF** ; le sixième — les amendements déposés — demande une pièce que le corpus
ne porte pas, et il n'est pas ici.

  1  mots de portée          — liste fermée d'A-230, par article et par alinéa
  2  dates                   — entrée en vigueur, clause de fin, transitoire
  3  absences attendues      — quatre tests, liste fermée d'A-230
  4  chiffre pris à l'état   — écart entre la rédaction et l'exposé des motifs
  5  deux colonnes           — texte en vigueur en regard de la disposition

**Sur le cinquième, et c'est une limite déclarée.** A-230 demande trois
colonnes : texte en vigueur, disposition, **texte résultant**. Les deux
premières se relèvent à l'octet — l'une au dépôt de droit, l'autre au socle. La
troisième suppose d'appliquer la modification, ce qui est un acte de légistique
et non un relevé : c'est le travail de `redaction-legistique`, et
`Constitution_3col` comme `LOLF_3col` ont été composés à la main. Ce module rend
donc **les deux colonnes vérifiables** et déclare la troisième pour ce qu'elle
est. Fabriquer un texte résultant par script serait inventer du droit.

Usage : python3 lecture_en_creux.py <socle.json> <sortie.json> <sortie.txt>
                                    [depot_droit]
        sans dépôt de droit, le cinquième relevé se déclare non joué.
"""
import json
import os
import re
import sys

# --- 1. Les mots de portée --------------------------------------------------
# **Liste fermée, celle d'A-230 et rien de plus.** Chacun ouvre ou ferme quelque
# chose. Y ajouter un mot de notre cru ferait passer un choix de lecture pour un
# relevé ; la liste s'étend par arbitrage, pas par intuition.
MOTS_DE_PORTEE = (
    'peut', 'dans la limite de', 'à compter de', 'au titre de',
    'par dérogation', 'notamment',
)
# « peut » se cherche en mot plein — « peuple » n'est pas « peut » — et les
# formes fléchies du même verbe comptent pour le même mot de portée.
FLEXIONS = {'peut': r'\b(?:peut|peuvent|pourra|pourront)\b'}


def _motif(mot):
    if mot in FLEXIONS:
        return re.compile(FLEXIONS[mot], re.I)
    return re.compile(re.escape(mot).replace(r'\ ', r'\s+'), re.I)


MOTIFS_PORTEE = {m: _motif(m) for m in MOTS_DE_PORTEE}


def mots_de_portee(art):
    releve = []
    for al in art['redaction']['alineas']:
        for mot, mot_re in MOTIFS_PORTEE.items():
            for m in mot_re.finditer(al['texte']):
                releve.append(dict(mot=mot, alinea=al['numero'],
                                   page=al['page'],
                                   occurrence=m.group(0),
                                   contexte=_contexte(al['texte'], m)))
    return releve


def _contexte(txt, m):
    """Les quelques mots qui encadrent l'occurrence, verbatim et bornés."""
    d = max(0, m.start() - 60)
    f = min(len(txt), m.end() + 60)
    return ('…' if d else '') + txt[d:f] + ('…' if f < len(txt) else '')


# --- 2. Les dates -----------------------------------------------------------
# Trois familles, et le mot qui introduit la date dit laquelle. Un décalage d'un
# an déplace un coût hors de l'année budgétaire sans rien changer au fond : A-230
# le donne pour le procédé le plus commun.
JOUR = (r'(?:1er|\d{1,2})\s+'
        r'(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre'
        r'|octobre|novembre|décembre)\s+(?:19|20)\d{2}')
ANNEE = r'(?:19|20)\d{2}'
FAMILLES_DATE = (
    ('entrée en vigueur',
     rf'\b(?:à compter (?:du|de l’|de la|de)|entre? en vigueur le|'
     rf'applicable(?:s)? (?:à compter du|au|le)|s’applique (?:à compter du|au))'
     rf'\s*(?:{JOUR}|1er\s+\w+\s+{ANNEE}|{ANNEE})'),
    ('clause de fin',
     rf'\b(?:jusqu’au|jusqu’à|au plus tard le|cesse[nt]? de|'
     rf'prend fin le|expire le|avant le)\s*(?:{JOUR}|{ANNEE})'),
    ('période transitoire',
     rf'\b(?:à titre transitoire|pendant une période de|'
     rf'par dérogation[^.;]{{0,80}}(?:{JOUR}|{ANNEE})|'
     rf'pour les (?:exercices|impositions|années) (?:clos|établies|)\s*'
     rf'[^.;]{{0,40}}{ANNEE})'),
)
MOTIFS_DATE = [(nom, re.compile(m, re.I)) for nom, m in FAMILLES_DATE]


def dates(art):
    releve = []
    for al in art['redaction']['alineas']:
        for nom, mot_re in MOTIFS_DATE:
            for m in mot_re.finditer(al['texte']):
                releve.append(dict(famille=nom, alinea=al['numero'],
                                   page=al['page'],
                                   occurrence=re.sub(r'\s+', ' ',
                                                     m.group(0)).strip()))
    return releve


# --- 3. Les absences attendues ----------------------------------------------
# Quatre tests, ceux qu'A-230 nomme, et la liste s'écrit une fois. Chaque test
# est un couple : ce que l'article fait, et ce qui manquerait alors. Un test qui
# sort n'est pas une faute de l'article — c'est une question à poser.
TESTS_ABSENCE = (
    ('taux modifié sans que l’assiette bouge',
     r'\btaux\b', r'\b(?:assiette|base d’imposition|base imposable)\b'),
    ('plafond posé sans indexation',
     r'\b(?:plafond|plafonné|dans la limite de)\b',
     r'\b(?:index|indexé|indexation|revaloris|évolution de l’indice)'),
    ('suppression sans transitoire',
     r'\b(?:est abrogé|sont abrogés|est abrogée|sont abrogées'
     r'|est supprimé|sont supprimés|est supprimée|sont supprimées)\b',
     r'\b(?:à compter du|transitoire|demeure applicable|reste applicable'
     r'|continue[nt]? de|pour les (?:exercices|impositions))'),
    ('dispositif sans évaluation',
     r'\b(?:il est (?:institué|créé)|est instituée?|est créée?|'
     r'crédit d’impôt|réduction d’impôt|exonération)\b',
     r'\b(?:évaluation|rapport|bilan|remet au Parlement|rend compte)\b'),
)
MOTIFS_ABSENCE = [(nom, re.compile(d, re.I), re.compile(a, re.I))
                  for nom, d, a in TESTS_ABSENCE]


def absences(art):
    texte = ' '.join(al['texte'] for al in art['redaction']['alineas'])
    releve = []
    for nom, decl, att in MOTIFS_ABSENCE:
        m = decl.search(texte)
        if m and not att.search(texte):
            releve.append(dict(test=nom,
                               declencheur=re.sub(r'\s+', ' ',
                                                  m.group(0)).strip()))
    return releve


# --- 4. Le chiffre pris à l'état --------------------------------------------
# A-230 : le montant de l'article se prend à l'état, à l'annexe ou au tableau
# d'équilibre, **jamais à l'exposé des motifs**, et tout écart entre les deux se
# relève sans s'arbitrer.
#
# Le relevé est donc une confrontation de deux ensembles, celui des montants que
# la rédaction porte et celui des montants que l'exposé annonce. Un montant
# annoncé et absent de la rédaction est un signal ; l'inverse aussi. Le module
# ne dit pas lequel est juste.
MONTANT = re.compile(
    r'(\d[\d\s .,]*)\s*'
    r'(milliards? d’euros|millions? d’euros|milliards?|millions?|€|euros)',
    re.I)


def _montants(lignes):
    vus = {}
    for l in lignes:
        for m in MONTANT.finditer(l):
            brut = re.sub(r'\s+', ' ', m.group(0)).strip()
            vus.setdefault(brut, 0)
            vus[brut] += 1
    return vus


def chiffre_a_l_etat(art):
    # Le hors-alinéa est ce que la pièce compose en tableau — état, plafond
    # d'emplois, tableau d'équilibre. **C'est précisément là que le montant se
    # prend**, et il y vit ligne par ligne, non en alinéa.
    red = _montants([al['texte'] for al in art['redaction']['alineas']]
                    + [h['ligne'] for h in art['redaction']['hors_alinea']])
    mot = _montants(art['expose_des_motifs']['lignes'])
    return dict(
        montants_a_la_redaction=sorted(red),
        montants_a_l_expose=sorted(mot),
        annonces_sans_contrepartie=sorted(set(mot) - set(red)),
        rediges_non_annonces=sorted(set(red) - set(mot)),
    )


# --- 5. Les deux colonnes vérifiables ---------------------------------------
def deux_colonnes(art, droit, court_par_texte):
    """Le texte en vigueur en regard de la disposition, adresse par adresse.

    Une adresse dont le code n'est pas au dépôt, ou dont l'article n'y est pas,
    sort en manque déclaré. **Aucun texte approchant n'est jamais rendu** : le
    dépôt lève, et on écrit qu'il a levé (A-94).
    """
    par_alinea = {al['numero']: al['texte']
                  for al in art['redaction']['alineas']}
    sortie = []
    for r in art['references']:
        if r['statut'] != 'modifie':
            continue
        court = court_par_texte.get(r['texte'])
        entree = dict(texte=r['texte'], article=r['brut'],
                      alinea=r['alinea'], page=r['page'],
                      fourchette=r.get('fourchette', False),
                      disposition=par_alinea.get(r['alinea'], ''),
                      en_vigueur=None, id=None, version=None, etat=None,
                      manque=None)
        if court is None:
            entree['manque'] = ('code hors dépôt de droit — '
                                'colonne « en vigueur » non relevable')
            sortie.append(entree)
            continue
        if entree['fourchette']:
            entree['manque'] = ('adresse en fourchette — se déplie par '
                                'plages_articles.py, pas ici')
            sortie.append(entree)
            continue
        try:
            a = droit.article(court, r['brut'])
        except Exception as exc:                      # noqa: BLE001
            entree['manque'] = f'dépôt de droit : {exc}'
            sortie.append(entree)
            continue
        entree.update(en_vigueur=a['texte'], id=a['id'],
                      version=a['date_debut'], etat=a['etat'])
        sortie.append(entree)
    return sortie


# ---------------------------------------------------------------------------
def main(socle, dst_json, dst_txt, depot=None):
    soc = json.load(open(socle, encoding='utf-8'))
    piece = soc['_revision']['piece']['nom']
    profil = soc['_revision']['extraction']['profil']

    droit = court_par_texte = None
    millesime = age = None
    if depot:
        sys.path.insert(0, depot)
        import droit as _d                            # noqa: E402
        droit = _d
        millesime, age, perime = droit.fraicheur()
        if perime:
            raise SystemExit(
                f'dépôt de droit au millésime {millesime}, {age} jours : '
                'périmé au-delà de 45. La génération s’arrête.')
        cfg = json.load(open(os.path.join(depot, 'codes.json'),
                             encoding='utf-8'))['codes']
        court_par_texte = {c['cle']: c['court'] for c in cfg}

    entrees = []
    for art in soc['articles']:
        e = dict(numero=art['numero'], page=art['page'],
                 partie=art['partie'], titre_division=art['titre_division'],
                 mots_de_portee=mots_de_portee(art),
                 dates=dates(art),
                 absences=absences(art),
                 chiffre=chiffre_a_l_etat(art))
        e['colonnes'] = (deux_colonnes(art, droit, court_par_texte)
                         if droit else None)
        entrees.append(e)

    n_portee = sum(len(e['mots_de_portee']) for e in entrees)
    n_dates = sum(len(e['dates']) for e in entrees)
    n_abs = sum(len(e['absences']) for e in entrees)
    n_ecart = sum(len(e['chiffre']['annonces_sans_contrepartie'])
                  for e in entrees)
    art_ecart = [e['numero'] for e in entrees
                 if e['chiffre']['annonces_sans_contrepartie']]
    n_col = sum(len(e['colonnes'] or []) for e in entrees)
    n_col_relev = sum(1 for e in entrees for c in (e['colonnes'] or [])
                      if c['en_vigueur'] is not None)

    obj = dict(
        _revision=dict(
            role=f'lecture en creux — {piece}',
            regle=('Cinq relevés mécaniques d’A-230. Le module produit des '
                   'signaux et ne les lit pas. La troisième colonne du '
                   'dispositif trois colonnes — le texte résultant — n’est '
                   'pas rendue : elle suppose d’appliquer la modification, '
                   'ce qui est un acte de légistique et non un relevé.'),
            piece=piece,
            profil=profil,
            mots_de_portee=list(MOTS_DE_PORTEE),
            tests_absence=[n for n, _, _ in TESTS_ABSENCE],
            familles_date=[n for n, _ in FAMILLES_DATE],
            depot_droit=(dict(millesime=millesime, age_jours=age)
                         if depot else None),
            comptes=dict(articles=len(entrees), mots_de_portee=n_portee,
                         dates=n_dates, absences=n_abs,
                         ecarts_de_montant=n_ecart,
                         adresses_modificatives=n_col,
                         colonnes_relevees=n_col_relev),
        ),
        articles=entrees,
    )
    os.makedirs(os.path.dirname(dst_json) or '.', exist_ok=True)
    with open(dst_json, 'w', encoding='utf-8', newline='') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')

    lig = [f'# LECTURE EN CREUX — {piece} (profil « {profil} »)',
           '# Cinq relevés mécaniques d’A-230. Des signaux, pas des verdicts.',
           '']
    for e in entrees:
        tete = f'ARTICLE {e["numero"]} — page {e["page"]}'
        if e['partie']:
            tete += f' · {e["partie"]} / {e["titre_division"]}'
        lig.append(tete)
        for m in e['mots_de_portee']:
            lig.append(f'    portée   [{m["mot"]}] al. {m["alinea"]} — '
                       f'{m["contexte"]}')
        for d in e['dates']:
            lig.append(f'    date     [{d["famille"]}] al. {d["alinea"]} — '
                       f'{d["occurrence"]}')
        for a in e['absences']:
            lig.append(f'    absence  {a["test"]} — déclenché par '
                       f'« {a["declencheur"]} »')
        c = e['chiffre']
        if c['annonces_sans_contrepartie']:
            lig.append('    montant  annoncé à l’exposé, absent de la '
                       'rédaction : '
                       + ', '.join(c['annonces_sans_contrepartie']))
        if c['rediges_non_annonces']:
            lig.append('    montant  à la rédaction, non annoncé à l’exposé : '
                       + ', '.join(c['rediges_non_annonces']))
        lig.append('')
    os.makedirs(os.path.dirname(dst_txt) or '.', exist_ok=True)
    with open(dst_txt, 'w', encoding='utf-8', newline='') as f:
        f.write('\n'.join(lig))

    print(f'{piece} — {len(entrees)} article(s)')
    print(f'  1 mots de portée      {n_portee} occurrence(s), '
          f'{len(MOTS_DE_PORTEE)} mots à la liste fermée')
    print(f'  2 dates               {n_dates} occurrence(s) sur '
          f'{len(FAMILLES_DATE)} familles')
    print(f'  3 absences attendues  {n_abs} signal(aux) sur '
          f'{len(TESTS_ABSENCE)} tests')
    print(f'  4 chiffre à l’état    {n_ecart} montant(s) annoncé(s) à '
          f'l’exposé sans contrepartie à la rédaction, sur '
          f'{len(art_ecart)} article(s)')
    if droit:
        print(f'  5 deux colonnes       {n_col_relev}/{n_col} adresse(s) '
              f'modificative(s) avec leur texte en vigueur relevé au dépôt '
              f'(millésime {millesime})')
    else:
        print('  5 deux colonnes       non joué — dépôt de droit non fourni')
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
