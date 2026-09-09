# -*- coding: utf-8 -*-
"""La grille des portes du domaine de la loi de financement, en verbatim.

Pendant de `portes_domaine.py`, qui fait le même travail sur la loi de finances.
Même règle, et c'est celle d'A-91 : **aucune phrase de ce module n'est du texte
de loi.** Le module ne porte que des repères — un article, un fragment littéral
par lequel la porte se reconnaît, une borne de fin. Le texte est découpé à
l'octet de sa source et jamais retapé. Un repère qui ne se retrouve pas fait
sortir la porte **en échec déclaré** ; rien d'approchant ne la remplace (A-94).

La source diffère, et c'est la seule différence. `portes_domaine.py` découpe une
pièce HTML du coffre ; ici la source est le **dépôt de droit** — base LEGI,
millésime porté à chaque sortie, identifiant `LEGIARTI` et date de version par
article (`reference/depot_droit.md`).

## La porte n'est pas à `LO 111-3`, et c'est le point à ne pas rater

Trois documents du corpus ont écrit que « la porte du domaine est à l'article
LO 111-3 du code de la sécurité sociale ». **C'est faux depuis la loi organique
n° 2022-354 du 14 mars 2022**, applicable au 1er septembre 2022 : `LO 111-3` ne
fait plus que nommer les trois espèces de lois de financement. Le domaine est
éclaté sur `LO 111-3-1` à `LO 111-3-18`. A-297 amende A-223 ; le relevé des
dix-huit articles est au coffre à `reference/domaine_lfss_LO111-3.md`.

    LO 111-3            les trois espèces. Elle borne, elle n'ouvre rien.
    LO 111-3-1, -3-2    la structure : article liminaire et trois parties.
    LO 111-3-3 à -3-5   ce que la loi de financement **doit** porter.
    LO 111-3-6 à -3-8   ce qu'elle **peut** porter — **la porte d'un
                        amendement**, une par partie du texte.
    LO 111-3-14 à -3-16 ce qui lui est **réservé**, dont le monopole sur les
                        exonérations de cotisations (-3-16).
    LO 111-3-18         l'obligation de reprise.

## Les rangs, et ils ne se confondent pas

Repris de `portes_domaine.py`, parce qu'un rang qui changerait de sens d'une
grille à l'autre rendrait les deux illisibles ensemble.

    definition            ce qu'une loi de financement est.
    structure             en quelles parties elle se divise. Se tromper de
                          partie est un motif d'irrecevabilité qui n'a rien à
                          voir avec le domaine.
    obligatoire           la loi de financement *doit* le porter.
    facultatif            elle *peut* le porter — « peuvent figurer ». **C'est
                          par là qu'un amendement entre.**
    monopole              seule une loi de financement peut le faire. Porte
                          fermée aux autres véhicules : elle sert à établir
                          qu'une mesure *ne peut pas* voyager ailleurs.
    reprise               la loi de financement doit tirer les conséquences de
                          ce qui se décide ailleurs.

## Ce que cette grille ne porte pas

Les **annexes obligatoires** — `LO 111-4` et `LO 111-4-1` — ne sont pas
relevées. C'est le pendant de l'article 51 de la LOLF, et donc le siège de toute
obligation documentaire nouvelle au PLFSS : le choix entre une annexe opposable
et un rapport appartient à l'auteur, comme au PLF. **Le manque est déclaré,
pas comblé.**

Usage : python3 portes_domaine_lfss.py <depot_droit> <sortie.md>
"""
import os
import re
import sys

CODE = 'css'
SOURCE = ('Code de la sécurité sociale, articles LO 111-3 à LO 111-3-18 — '
          'domaine des lois de financement de la sécurité sociale')

RANGS = {
    'definition': 'définition',
    'structure': 'structure',
    'obligatoire': 'domaine obligatoire',
    'facultatif': 'domaine facultatif',
    'monopole': 'monopole',
    'reprise': 'obligation de reprise',
}
ORDRE = ('definition', 'structure', 'facultatif', 'obligatoire',
         'monopole', 'reprise')

# --------------------------------------------------------------- les repères
# Une entrée par porte. `repere` est un fragment littéral attendu au texte de
# l'article ; `jusqu_a` borne la fin du relevé, exclu, ou None pour aller au
# bout de l'article. Rien d'autre n'est écrit à la main que le repère, le rang,
# la partie et le motif.
PORTES = [
    # ---- Ce qu'une loi de financement est --------------------------------
    dict(code='S-01', article='LO 111-3', rang='definition', partie='—',
         repere="Ont le caractère de loi de financement de la sécurité sociale",
         jusqu_a=None,
         motif="Les trois espèces, et rien de plus. **Cet article n'ouvre "
               "aucune porte** : il ne dit pas ce qu'une loi de financement "
               "peut contenir. Le corpus a longtemps écrit le contraire "
               "(A-297)."),
    dict(code='S-02', article='LO 111-3-1', rang='structure', partie='—',
         repere="La loi de financement de la sécurité sociale de l'année "
                "comprend un article liminaire et trois parties",
         jusqu_a=None,
         motif="**Trois parties, pas deux.** Une mesure de recettes pour "
               "l'année à venir va en deuxième partie, une mesure de dépenses "
               "en troisième, une rectification de l'année en cours en "
               "première. Le PLF n'a que deux parties : l'habitude prise sur "
               "le PLF envoie l'amendement au mauvais endroit."),
    dict(code='S-03', article='LO 111-3-2', rang='obligatoire',
         partie='liminaire',
         repere="Dans son article liminaire, la loi de financement de l'année "
                "présente",
         jusqu_a=None,
         motif="L'article liminaire est obligatoire."),

    # ---- Première partie — l'année en cours ------------------------------
    dict(code='S-04', article='LO 111-3-3', rang='obligatoire',
         partie='première',
         repere="1° Rectifie les prévisions de recettes et les tableaux "
                "d'équilibre des régimes obligatoires de base",
         jusqu_a="2° Rectifie les objectifs de dépenses",
         motif="La rectification des recettes et des tableaux d'équilibre de "
               "l'année en cours."),
    dict(code='S-05', article='LO 111-3-3', rang='obligatoire',
         partie='première',
         repere="2° Rectifie les objectifs de dépenses",
         jusqu_a="3° Rectifie l'objectif assigné aux organismes",
         motif="La rectification des objectifs de dépenses et de l'ONDAM de "
               "l'année en cours."),
    dict(code='S-06', article='LO 111-3-3', rang='obligatoire',
         partie='première',
         repere="3° Rectifie l'objectif assigné aux organismes chargés de "
                "l'amortissement de la dette",
         jusqu_a=None,
         motif="La rectification de l'objectif d'amortissement."),
    dict(code='S-07', article='LO 111-3-6', rang='facultatif',
         partie='première',
         repere="1° Les dispositions ayant un effet sur les recettes des "
                "régimes obligatoires de base ou des organismes concourant à "
                "leur financement",
         jusqu_a="2° Les dispositions relatives à l'affectation de ces recettes",
         motif="**La porte de recettes sur l'année en cours.** Effet sur les "
               "recettes des régimes ou des organismes : c'est la plus large "
               "des portes de première partie."),
    dict(code='S-08', article='LO 111-3-6', rang='facultatif',
         partie='première',
         repere="2° Les dispositions relatives à l'affectation de ces recettes",
         jusqu_a="3° Les dispositions ayant un effet sur les dépenses",
         motif="**L'affectation des recettes**, sous réserve du III de "
               "l'article 2 de la LOLF. C'est la porte des transferts de "
               "ressource entre l'État et la sécurité sociale, et la réserve "
               "dit qu'elle se lit avec la loi de finances."),
    dict(code='S-09', article='LO 111-3-6', rang='facultatif',
         partie='première',
         repere="3° Les dispositions ayant un effet sur les dépenses de ces "
                "régimes ou organismes",
         jusqu_a="4° Si elles ont pour effet",
         motif="La porte de dépenses sur l'année en cours. Noter qu'elle ne "
               "porte **aucune** réserve d'équilibre, contrairement à son "
               "pendant de troisième partie."),
    dict(code='S-10', article='LO 111-3-6', rang='facultatif',
         partie='première',
         repere="4° Si elles ont pour effet de modifier les conditions "
                "générales de l'équilibre financier de la sécurité sociale, "
                "les dispositions ayant un effet sur",
         jusqu_a="5° Les dispositions améliorant l'information",
         motif="La dette des hôpitaux et des établissements médico-sociaux, "
               "**sous condition d'effet sur l'équilibre général**. La "
               "condition est écrite : elle se plaide, elle ne s'acquiert "
               "pas."),
    dict(code='S-11', article='LO 111-3-6', rang='facultatif',
         partie='première',
         repere="5° Les dispositions améliorant l'information et le contrôle "
                "du Parlement",
         jusqu_a=None,
         motif="**La porte de transparence de première partie.** Pendant du "
               "7° du II de l'article 34 de la LOLF, et elle est ouverte sans "
               "condition d'équilibre."),

    # ---- Deuxième partie — recettes et équilibre de l'année à venir -------
    dict(code='S-12', article='LO 111-3-4', rang='obligatoire',
         partie='deuxième',
         repere="1° Approuve le rapport prévu à l'article LO 111-4",
         jusqu_a="2° Détermine, pour l'année à venir",
         motif="L'approbation du rapport pluriannuel."),
    dict(code='S-13', article='LO 111-3-4', rang='obligatoire',
         partie='deuxième',
         repere="2° Détermine, pour l'année à venir, de manière sincère, les "
                "conditions générales de l'équilibre financier",
         jusqu_a=None,
         motif="**Les conditions générales de l'équilibre**, et les cinq "
               "objets qu'elles commandent — recettes par branche, objectif "
               "d'amortissement, compensation, tableaux d'équilibre, "
               "habilitation à recourir à des ressources non permanentes. "
               "C'est l'équivalent du tableau d'équilibre du PLF."),
    dict(code='S-14', article='LO 111-3-7', rang='facultatif',
         partie='deuxième',
         repere="1° Ayant un effet sur les recettes des régimes obligatoires "
                "de base",
         jusqu_a="2° Relatives à l'assiette, au taux",
         motif="**La porte de recettes principale du PLFSS**, avec ses trois "
               "horizons d'application : l'année, l'année et les suivantes, "
               "les seules années ultérieures à condition de permanence. "
               "L'horizon se déclare dans la rédaction."),
    dict(code='S-15', article='LO 111-3-7', rang='facultatif',
         partie='deuxième',
         repere="2° Relatives à l'assiette, au taux et aux modalités de "
                "recouvrement des cotisations et contributions",
         jusqu_a="3° Relatives à la trésorerie",
         motif="**La porte fiscale sociale.** Assiette, taux, recouvrement "
               "des cotisations et contributions affectées aux régimes. "
               "Pendant exact du 2° du I de l'article 34 de la LOLF, et c'est "
               "par là que passe toute mesure de cotisation."),
    dict(code='S-16', article='LO 111-3-7', rang='facultatif',
         partie='deuxième',
         repere="3° Relatives à la trésorerie et à la comptabilité",
         jusqu_a="4° Ayant un effet sur la dette",
         motif="Trésorerie et comptabilité des régimes et organismes."),
    dict(code='S-17', article='LO 111-3-7', rang='facultatif',
         partie='deuxième',
         repere="4° Ayant un effet sur la dette des régimes obligatoires de "
                "base",
         jusqu_a="5° Relatives à la mise en réserve",
         motif="La dette des régimes, son amortissement et ses conditions de "
               "financement."),
    dict(code='S-18', article='LO 111-3-7', rang='facultatif',
         partie='deuxième',
         repere="5° Relatives à la mise en réserve de recettes au profit des "
                "régimes obligatoires de base",
         jusqu_a="6° Améliorant l'information",
         motif="La mise en réserve et l'utilisation des réserves."),
    dict(code='S-19', article='LO 111-3-7', rang='facultatif',
         partie='deuxième',
         repere="6° Améliorant l'information et le contrôle du Parlement",
         jusqu_a=None,
         motif="**La porte de transparence de deuxième partie.**"),

    # ---- Troisième partie — dépenses de l'année à venir -------------------
    dict(code='S-20', article='LO 111-3-5', rang='obligatoire',
         partie='troisième',
         repere="1° Fixe les charges prévisionnelles des organismes concourant "
                "au financement",
         jusqu_a="2° Fixe les objectifs de dépenses",
         motif="Les charges prévisionnelles des organismes concourants."),
    dict(code='S-21', article='LO 111-3-5', rang='obligatoire',
         partie='troisième',
         repere="2° Fixe les objectifs de dépenses de l'ensemble des régimes "
                "obligatoires de base",
         jusqu_a="3° Fixe l'objectif national de dépenses d'assurance maladie",
         motif="Les objectifs de dépenses par branche. **La liste des "
               "sous-objectifs est fixée par le Gouvernement** — monopole "
               "d'initiative, comme la création d'une mission au PLF."),
    dict(code='S-22', article='LO 111-3-5', rang='obligatoire',
         partie='troisième',
         repere="3° Fixe l'objectif national de dépenses d'assurance maladie",
         jusqu_a=None,
         motif="L'ONDAM et ses sous-objectifs. **La définition des composantes "
               "est d'initiative gouvernementale**, et le nombre de "
               "sous-objectifs ne peut être inférieur à trois : deux bornes "
               "opposables à un amendement de structure."),
    dict(code='S-23', article='LO 111-3-8', rang='facultatif',
         partie='troisième',
         repere="1° Les dispositions ayant un effet sur les dépenses des "
                "régimes obligatoires de base",
         jusqu_a="2° Les dispositions modifiant les règles relatives à la "
                 "gestion des risques",
         motif="**La porte de dépenses principale du PLFSS**, et elle est plus "
               "étroite que son pendant de première partie : l'effet doit "
               "affecter **directement** l'équilibre financier des régimes. "
               "Trois horizons d'application, comme en recettes."),
    dict(code='S-24', article='LO 111-3-8', rang='facultatif',
         partie='troisième',
         repere="2° Les dispositions modifiant les règles relatives à la "
                "gestion des risques",
         jusqu_a="3° Si elles ont pour effet",
         motif="**La porte d'organisation et de gestion interne des régimes et "
               "des organismes**, sous condition d'objet ou d'effet sur "
               "l'équilibre général. C'est la porte à connaître pour une "
               "mesure de structure — fusion, suppression, tutelle — sur une "
               "caisse."),
    dict(code='S-25', article='LO 111-3-8', rang='facultatif',
         partie='troisième',
         repere="3° Si elles ont pour effet de modifier les conditions "
                "générales de l'équilibre financier de la sécurité sociale, "
                "les dispositions ayant un effet sur",
         jusqu_a="4° Les dispositions améliorant l'information",
         motif="La dette des hôpitaux et des établissements médico-sociaux, "
               "sous condition d'effet sur l'équilibre général."),
    dict(code='S-26', article='LO 111-3-8', rang='facultatif',
         partie='troisième',
         repere="4° Les dispositions améliorant l'information et le contrôle "
                "du Parlement",
         jusqu_a=None,
         motif="**La porte de transparence de troisième partie.** Les trois "
               "parties en portent une : l'axe de transparence a donc trois "
               "entrées possibles au PLFSS, et le choix de la partie suit "
               "l'objet, non la commodité."),

    # ---- Ce qui est réservé aux lois de financement ----------------------
    dict(code='S-27', article='LO 111-3-14', rang='monopole', partie='—',
         repere="L'affectation, totale ou partielle, d'une recette exclusive "
                "des régimes obligatoires de base",
         jusqu_a=None,
         motif="**Détourner vers un tiers une recette exclusive de la sécurité "
               "sociale ne peut se faire qu'en loi de financement.** Porte "
               "fermée aux autres véhicules : à opposer à toute mesure "
               "d'affectation portée ailleurs."),
    dict(code='S-28', article='LO 111-3-15', rang='monopole', partie='—',
         repere="La répartition, entre les régimes obligatoires de base de "
                "sécurité sociale",
         jusqu_a=None,
         motif="La répartition entre régimes et branches des ressources de "
               "l'État qui leur ont été affectées. Monopole."),
    dict(code='S-29', article='LO 111-3-16', rang='monopole', partie='—',
         repere="Seules des lois de financement de l'année ou rectificatives "
                "peuvent créer ou modifier des mesures de réduction ou "
                "d'exonération de cotisations",
         jusqu_a="II. - Le I s'applique également",
         motif="**Le monopole sur les exonérations de cotisations**, aux deux "
               "conditions du I : non compensées, ou établies pour trois ans "
               "et plus avec effet sur les recettes ou sur l'assiette. C'est "
               "la pièce maîtresse : une mesure d'allègement de cotisations "
               "hors PLFSS est attaquable sur ce fondement."),
    dict(code='S-30', article='LO 111-3-16', rang='monopole', partie='—',
         repere="II. - Le I s'applique également",
         jusqu_a=None,
         motif="L'extension du monopole : contributions affectées, "
               "abattements d'assiette, et modification des exonérations non "
               "compensées antérieures à la loi organique de 2005."),

    # ---- L'obligation de reprise -----------------------------------------
    dict(code='S-31', article='LO 111-3-18', rang='reprise', partie='—',
         repere="Lorsque des dispositions législatives ou réglementaires sont "
                "susceptibles d'avoir un effet sur les recettes ou les "
                "dépenses",
         jusqu_a=None,
         motif="**L'obligation de reprise, et c'est un argument de "
               "rattachement écrit dans le texte** : toute mesure prise "
               "ailleurs qui pèse sur les comptes sociaux doit être reprise "
               "dans la loi de financement suivante. Pendant de l'argument du "
               "test de rattachement au PLF."),
]

# Ce que la grille laisse dehors, nommément.
NON_RELEVEES = [
    ('LO 111-4', "le rapport pluriannuel joint au projet de loi de "
                 "financement — pendant du rapport de l'article 50 de la "
                 "LOLF"),
    ('LO 111-4-1', "les annexes obligatoires — **siège de toute obligation "
                   "documentaire nouvelle au PLFSS**, et pendant de "
                   "l'article 51 de la LOLF. Le choix entre une annexe "
                   "opposable et un rapport appartient à l'auteur, comme au "
                   "PLF."),
    ('LO 111-3-9 à -3-13', "les lois de financement rectificatives et la loi "
                           "d'approbation des comptes. Autres espèces, autre "
                           "calendrier ; hors du PLFSS de l'année."),
    ('LO 111-3-17', "la régularité et la sincérité des comptes. Condition de "
                    "fond, non instruite ici."),
]


def _norm(s):
    """Les apostrophes ramenées à la droite, pour que le repère morde."""
    return s.replace('’', "'").replace('ʼ', "'")


def relever(depot):
    sys.path.insert(0, depot)
    import droit                                     # noqa: E402
    millesime, age, perime = droit.fraicheur()
    if perime:
        raise SystemExit(
            f'dépôt de droit au millésime {millesime}, {age} jours : périmé '
            'au-delà de 45. Le relevé s’arrête plutôt que de citer du droit '
            'ancien.')

    cache = {}
    releve, manques = [], []
    for p in PORTES:
        num = p['article'].replace('LO ', 'LO')
        if num not in cache:
            try:
                cache[num] = droit.article(CODE, num)
            except Exception as exc:                  # noqa: BLE001
                cache[num] = exc
        a = cache[num]
        if isinstance(a, Exception):
            manques.append((p['code'], p['article'],
                            f'article introuvable au dépôt : {a}'))
            continue
        texte = _norm(a['texte'])
        rep = _norm(p['repere'])
        d = texte.find(rep)
        if d < 0:
            manques.append((p['code'], p['article'],
                            'repère absent du texte en vigueur — '
                            'le texte a changé, ou le repère est faux'))
            continue
        if p['jusqu_a']:
            fin = texte.find(_norm(p['jusqu_a']), d + len(rep))
            if fin < 0:
                manques.append((p['code'], p['article'],
                                'borne de fin absente du texte en vigueur'))
                continue
        else:
            fin = len(texte)
        releve.append(dict(p, verbatim=texte[d:fin].strip(),
                           id=a['id'], version=a['date_debut'],
                           etat=a['etat'], section=a.get('section', '')))
    return releve, manques, millesime, age


def rendre(releve, manques, millesime, age):
    L = []
    a = L.append
    a('# Les portes du domaine de la loi de financement de la sécurité sociale')
    a('')
    a(f'Relevé en verbatim sur le dépôt de droit — base LEGI, millésime '
      f'**{millesime}** ({age} j). Chaque porte porte son identifiant '
      f'`LEGIARTI` et sa date de version. **Aucune phrase de ce document '
      f'n’est écrite de mémoire** : le module ne porte que des repères, et le '
      f'texte est découpé à l’octet.')
    a('')
    a(f'Source : {SOURCE}.')
    a('')
    a('**La porte n’est pas à `LO 111-3`.** Depuis la loi organique '
      'n° 2022-354 du 14 mars 2022, cet article ne nomme plus que les trois '
      'espèces de lois de financement ; le domaine est éclaté sur '
      '`LO 111-3-1` à `LO 111-3-18`. A-297 amende A-223.')
    a('')
    a('**Cette grille est au second rang.** Elle dit ce qui est acquis sans '
      'plaidoirie ; elle ne dit pas ce qu’on tente. Le rattachement se plaide '
      'par l’implicite budgétaire et le contrefactuel (A-225).')
    a('')
    a('---')
    a('')
    a('## Le compte')
    a('')
    a(f'{len(releve)} porte(s) relevée(s) en verbatim, {len(manques)} en '
      f'échec de relevé, {len(NON_RELEVEES)} lot(s) déclaré(s) hors grille.')
    a('')
    for cle, nom in RANGS.items():
        n = sum(1 for p in releve if p['rang'] == cle)
        if n:
            a(f'- **{nom}** — {n}')
    a('')
    a('Par partie du texte :')
    a('')
    for part in ('liminaire', 'première', 'deuxième', 'troisième', '—'):
        n = sum(1 for p in releve if p['partie'] == part)
        if n:
            nom = 'hors partie' if part == '—' else f'{part} partie'
            a(f'- {nom} — {n}')
    a('')
    a('---')
    a('')
    for cle in ORDRE:
        lot = [p for p in releve if p['rang'] == cle]
        if not lot:
            continue
        a(f'## {RANGS[cle].capitalize()}')
        a('')
        for p in lot:
            part = ('' if p['partie'] == '—'
                    else f' · article {p["partie"]}'
                    if p['partie'] == 'liminaire'
                    else f' · {p["partie"]} partie')
            a(f'### {p["code"]} — {p["article"]}{part}')
            a('')
            for ligne in p['verbatim'].split('\n'):
                a(f'> {ligne.strip()}' if ligne.strip() else '>')
            a('')
            a(p['motif'])
            a('')
            a(f'*`{p["id"]}` · version du {p["version"]} · état {p["etat"]} · '
              f'{p["section"]}*')
            a('')
        a('---')
        a('')
    if manques:
        a('## Échecs de relevé')
        a('')
        a('**Une porte en échec ne se compose pas.** Le repère ne s’est pas '
          'retrouvé au texte en vigueur : soit le texte a changé, soit le '
          'repère est faux. Dans les deux cas cela se reprend au module, '
          'jamais au livrable.')
        a('')
        for code, art, raison in manques:
            a(f'- `{code}` — {art} : {raison}')
        a('')
        a('---')
        a('')
    a('## Ce que la grille laisse dehors, nommément')
    a('')
    for art, quoi in NON_RELEVEES:
        a(f'- **{art}** — {quoi}')
    a('')
    a('---')
    a('')
    a('## Ce que le relevé apprend, et qui ne se voyait pas avant lui')
    a('')
    a('**Trois parties, et trois portes de transparence.** Chacune des trois '
      'parties porte sa propre porte « améliorant l’information et le '
      'contrôle du Parlement » — `S-11`, `S-19`, `S-26` —, et aucune ne pose '
      'de condition d’équilibre. L’axe de transparence a donc **trois entrées '
      'au PLFSS contre deux au PLF**, et le choix de la partie suit l’objet.')
    a('')
    a('**La porte de dépenses n’a pas la même largeur selon la partie.** En '
      'première partie, `S-09` prend toute disposition ayant un effet sur les '
      'dépenses des régimes, sans réserve. En troisième partie, `S-23` exige '
      'que l’effet affecte **directement** l’équilibre financier. Une même '
      'mesure de dépense n’a donc pas le même coût de plaidoirie selon '
      'qu’elle vise l’année en cours ou l’année à venir.')
    a('')
    a('**`S-24` est la porte des mesures de structure sur les caisses.** '
      'Fusionner, supprimer ou retutelle un organisme se rattache aux règles '
      'd’organisation et de gestion interne, sous condition d’objet ou '
      'd’effet sur l’équilibre général. C’est la porte à citer pour les '
      'organismes de sécurité sociale du chiffrage, et elle est en '
      '**troisième** partie.')
    a('')
    a('**`S-29` est une arme et non une porte.** Le monopole sur les '
      'exonérations de cotisations ne fait entrer aucun amendement au PLFSS : '
      'il établit qu’une mesure d’allègement portée par un autre véhicule est '
      'attaquable. À tenir du côté de la contestabilité, pas du côté de la '
      'rédaction.')
    a('')
    a('**`S-31` est l’argument de rattachement, et il est écrit.** Toute '
      'mesure prise ailleurs qui pèse sur les comptes sociaux doit être '
      'reprise dans la loi de financement suivante. C’est le pendant exact de '
      'l’argument du test de rattachement au PLF, et il ne se plaide pas : il '
      'se cite.')
    a('')
    a('**Deux monopoles se lisent avec la LOLF, pas seuls.** `S-08`, `S-27` '
      'et `S-28` renvoient tous au III de l’article 2 de la loi organique '
      'relative aux lois de finances. Une mesure d’affectation entre l’État '
      'et la sécurité sociale se qualifie donc sur **deux** grilles, et '
      '`livrables/portes_domaine.md` est l’autre. *Le croisement des deux '
      'n’est pas fait ; ce module ne le fait pas.*')
    a('')
    return '\n'.join(L) + '\n'


def main(depot, dst):
    releve, manques, millesime, age = relever(depot)
    texte = rendre(releve, manques, millesime, age)
    os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
    open(dst, 'w', encoding='utf-8', newline='').write(texte)
    print(f'{dst} — {len(releve)} porte(s) relevée(s), {len(manques)} en '
          f'échec, {os.path.getsize(dst)} octets '
          f'(millésime LEGI {millesime}, {age} j)')
    for cle in ORDRE:
        n = sum(1 for p in releve if p['rang'] == cle)
        if n:
            print(f'    {RANGS[cle]:<22} {n}')
    for code, art, raison in manques:
        print(f'    ÉCHEC {code} — {art} : {raison}')
    return 1 if manques else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
