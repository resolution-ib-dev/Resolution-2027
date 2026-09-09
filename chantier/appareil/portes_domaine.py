# -*- coding: utf-8 -*-
"""La grille des portes du domaine de la loi de finances, relevée en verbatim.

**Aucune phrase de ce module n'est du texte de loi.** Le module ne porte que des
repères — un article, et un fragment littéral par lequel la porte se reconnaît.
Le texte est ensuite découpé de `sources/LOLF_reference_20260507.html` et recopié
à l'octet. Un repère qui ne se retrouve pas **arrête la génération** : la porte
sort déclarée non relevable, et rien d'approchant ne la remplace.

C'est la règle d'A-91 appliquée aux portes : une hypothèse porte un repère,
jamais le verbatim. Et c'est la seule façon de tenir « relevée en verbatim sur
LOLF_reference — jamais de mémoire ».

## Ce qu'une porte est, et ce qu'elle n'est pas

Une **porte** est un alinéa de la loi organique qui autorise une disposition à
figurer en loi de finances. Elle dit ce qui est **acquis sans plaidoirie**.

Elle ne dit pas ce qu'on tente. Le rattachement se plaide par l'implicite
budgétaire et le contrefactuel (A-225), et la grille des portes est au second
rang. On la relève pour savoir ce qu'on n'a **pas** à plaider.

## Les rangs, et ils ne se confondent pas

    définition            ce qu'une loi de finances est. Elle borne tout le
                          reste.
    domaine obligatoire   la loi de finances *doit* le porter. La disposition y
                          a sa place de droit ; elle n'a rien à plaider.
    domaine facultatif    la loi de finances *peut* le porter — « peut
                          comporter ». La place est ouverte, la disposition
                          reste soumise au lien avec les recettes ou les
                          charges de l'exercice.
    condition de fond     une exigence opposable à un dispositif existant. Elle
                          n'ouvre pas une porte : elle donne une prise, sans
                          plaidoirie de domaine.
    monopole              seule une loi de finances peut le faire. Ce n'est pas
                          une porte d'entrée : c'est une porte fermée aux
                          autres véhicules, et elle sert à l'inverse — établir
                          qu'une mesure *ne peut pas* voyager ailleurs.
    obligation de reprise la loi de finances doit tirer les conséquences de ce
                          qui se décide ailleurs. C'est l'argument du test de
                          rattachement, et il est écrit dans le texte.
    annexe obligatoire    ce qui est joint au projet de loi de finances. Siège
                          de toute obligation documentaire nouvelle.

La partie compte autant que le rang : une disposition de recettes va en
première partie, une disposition qui n'affecte pas l'équilibre en seconde. Se
tromper de partie est un motif d'irrecevabilité qui n'a rien à voir avec le
domaine.

## Ce que la pièce ne porte pas

`LOLF_reference_20260507.html` reproduit certains articles en résumé, marqués
en italique gris. Les articles 35 à 37 — tableau de financement, lois de
finances rectificatives, loi d'approbation des comptes — en sont. **Leur porte
existe et ne se relève pas ici.** Le module le déclare plutôt que de la
composer.

Usage : python3 portes_domaine.py ../sources/LOLF_reference_20260507.html \\
            ../livrables/portes_domaine.md
"""
import html
import os
import re
import sys

SOURCE = 'Loi organique n° 2001-692 du 1er août 2001 relative aux lois de finances'

# --------------------------------------------------------------- les repères
# Une entrée par porte. `repere` est un fragment littéral attendu au texte de
# l'article ; `jusqu_a` borne la fin du relevé (exclu), ou None pour aller au
# bout de l'alinéa. Rien d'autre n'est écrit à la main que le repère, le rang,
# la partie et le motif.
PORTES = [
    # ---- Titre I : ce qu'une loi de finances est -------------------------
    dict(code='P-01', article='Art. 1er', rang='definition', partie='—',
         repere="Dans les conditions et sous les réserves prévues par la présente loi organique, les lois de finances déterminent",
         jusqu_a="Ont le caractère de lois de finances",
         motif="La définition du contenu. Elle borne tout le reste : une "
               "disposition qui ne touche ni la nature, ni le montant, ni "
               "l'affectation des ressources et des charges de l'État, ni "
               "l'équilibre qui en résulte, n'a pas d'assise ici."),

    # ---- Article liminaire ------------------------------------------------
    dict(code='P-02', article='Art. 1er H', rang='obligatoire', partie='liminaire',
         repere="La loi de finances de l'année, les lois de finances rectificatives et la loi d'approbation des comptes de l'année comprennent un article liminaire",
         jusqu_a=None,
         motif="L'article liminaire est obligatoire et porte le solde "
               "structurel et le solde effectif de l'ensemble des "
               "administrations publiques — donc un objet plus large que "
               "l'État."),

    # ---- Première partie : arts. 34-I ------------------------------------
    dict(code='P-03', article='Art. 34', rang='obligatoire', partie='première',
         repere="1° Autorise, pour l'année, la perception des ressources de l'État et des impositions de toutes natures affectées à des personnes morales autres que l'État ;",
         jusqu_a=None,
         motif="L'autorisation de percevoir. Elle couvre aussi les impositions "
               "affectées à des tiers — première prise sur les opérateurs et "
               "les organismes affectataires."),
    dict(code='P-04', article='Art. 34', rang='obligatoire', partie='première',
         repere="2° Comporte les dispositions relatives aux ressources de l'État ;",
         jusqu_a=None,
         motif="La porte fiscale principale. Assiette, taux, recouvrement : "
               "tout ce qui touche une ressource de l'État entre ici, en "
               "première partie."),
    dict(code='P-05', article='Art. 34', rang='obligatoire', partie='première',
         repere="3° Comporte toutes dispositions relatives aux affectations de recettes au sein du budget de l'État ;",
         jusqu_a=None,
         motif="Les affectations internes — comptes spéciaux, budgets "
               "annexes, procédures comptables particulières."),
    dict(code='P-06', article='Art. 34', rang='facultatif', partie='première',
         repere="3° bis Peut comporter des dispositions relatives à l'assiette, au taux, à l'affectation et aux modalités de recouvrement des impositions de toutes natures affectées à une personne morale autre que l'État ;",
         jusqu_a=None,
         motif="**La porte des taxes affectées.** C'est par elle qu'on touche "
               "au financement des opérateurs et des organismes hors État "
               "sans passer par leurs crédits. Elle est facultative, donc "
               "ouverte, et elle porte l'affectation elle-même."),
    dict(code='P-07', article='Art. 34', rang='obligatoire', partie='première',
         repere="4° Institue et évalue chacun des prélèvements mentionnés à l'article 6 ;",
         jusqu_a=None,
         motif="Les prélèvements sur recettes au profit des collectivités "
               "territoriales et de l'Union européenne."),
    dict(code='P-08', article='Art. 34', rang='obligatoire', partie='première',
         repere="5° Comporte l'évaluation de chacune des recettes budgétaires ;",
         jusqu_a=None,
         motif="L'évaluation ligne à ligne des recettes."),
    dict(code='P-09', article='Art. 34', rang='obligatoire', partie='première',
         repere="5° bis Présente la liste et le produit prévisionnel de l'ensemble des impositions de toutes natures dont le produit est affecté à une personne morale autre que les collectivités territoriales, leurs établissements publics et les organismes de sécurité sociale et décide, le cas échéant, d'attribuer totalement ou partiellement ce produit à l'État ;",
         jusqu_a=None,
         motif="**La reprise du produit d'une taxe affectée par l'État.** La "
               "porte est explicite : la loi de finances *décide* d'attribuer "
               "le produit à l'État. Les collectivités, leurs établissements "
               "et les organismes de sécurité sociale en sont exclus — c'est "
               "la borne à connaître."),
    dict(code='P-10', article='Art. 34', rang='obligatoire', partie='première',
         repere="6° Fixe les plafonds des dépenses du budget général et de chaque budget annexe, les plafonds des charges de chaque catégorie de comptes spéciaux ainsi que le plafond d'autorisation des emplois rémunérés par l'État ;",
         jusqu_a=None,
         motif="Les plafonds de dépenses et le plafond d'emplois de l'État."),
    dict(code='P-11', article='Art. 34', rang='obligatoire', partie='première',
         repere="7° Arrête les données générales de l'équilibre budgétaire, présentées dans un tableau d'équilibre.",
         jusqu_a=None,
         motif="Le tableau d'équilibre, qui clôt la première partie et "
               "conditionne le passage à la seconde."),

    # ---- Seconde partie : arts. 34-II -------------------------------------
    dict(code='P-12', article='Art. 34', rang='obligatoire', partie='seconde',
         repere="1° Fixe, pour le budget général, par mission, le montant des autorisations d'engagement et des crédits de paiement ;",
         jusqu_a=None,
         motif="Les crédits par mission. C'est la porte de toute mesure "
               "d'économie ou de dépense sur le budget général — et c'est "
               "l'article 40 de la Constitution qui l'encadre, non le "
               "domaine."),
    dict(code='P-13', article='Art. 34', rang='obligatoire', partie='seconde',
         repere="2° Fixe, par budget annexe et par compte spécial, le montant des autorisations d'engagement et des crédits de paiement ouverts ou des découverts autorisés ;",
         jusqu_a=None,
         motif="Les crédits des budgets annexes et des comptes spéciaux."),
    dict(code='P-14', article='Art. 34', rang='obligatoire', partie='seconde',
         repere="3° Fixe les plafonds des autorisations d'emplois des opérateurs de l'État ;",
         jusqu_a=None,
         motif="**La porte des emplois des opérateurs.** Elle est obligatoire "
               "et nommée : le plafond d'emplois d'un opérateur se fixe en "
               "loi de finances, en seconde partie. C'est l'assise directe de "
               "toute mesure sur les effectifs des agences."),
    dict(code='P-15', article='Art. 34', rang='obligatoire', partie='seconde',
         repere="4° Autorise l'octroi des garanties de l'État et fixe leur régime ;",
         jusqu_a=None,
         motif="Les garanties de l'État."),
    dict(code='P-16', article='Art. 34', rang='obligatoire', partie='seconde',
         repere="5° Autorise l'État à prendre en charge les dettes de tiers, à constituer tout autre engagement correspondant à une reconnaissance unilatérale de dette, et fixe le régime de cette prise en charge ou de cet engagement ;",
         jusqu_a=None,
         motif="La reprise de dette d'un tiers."),
    dict(code='P-17', article='Art. 34', rang='facultatif', partie='seconde',
         repere="6° Peut comporter des dispositions relatives à l'assiette, au taux et aux modalités de recouvrement des impositions de toutes natures qui n'affectent pas l'équilibre budgétaire ;",
         jusqu_a=None,
         motif="**La porte fiscale de seconde partie.** Elle est large et "
               "sous-employée : une mesure fiscale sans effet sur l'équilibre "
               "de l'exercice — entrée en vigueur différée, mesure de "
               "structure, simplification — entre ici sans avoir à démontrer "
               "un rendement. Noter qu'elle ne porte **pas** l'affectation, à "
               "la différence du 3° bis de la première partie."),
    dict(code='P-18', article='Art. 34', rang='facultatif', partie='seconde',
         repere="7° Peut comporter toutes dispositions relatives à l'information et au contrôle du Parlement sur la gestion des finances publiques ;",
         jusqu_a=None,
         motif="**Écartée comme porte générale (A-226).** C'est la porte par "
               "laquelle on demande des rapports, faute d'avoir réfléchi à ce "
               "qu'on veut faire ou d'en avoir les moyens. Elle ne sert qu'un "
               "axe : la transparence absolue — opérateurs, associations, "
               "caisses de sécurité sociale. Sa largeur — « toutes "
               "dispositions », « la gestion des finances publiques », et non "
               "les seules finances de l'État — est ce qui la rend utile pour "
               "cet axe précis et dangereuse pour tout le reste."),
    dict(code='P-19', article='Art. 34', rang='facultatif', partie='seconde',
         repere="8° Peut comporter toutes dispositions relatives à la comptabilité de l'État et, sous réserve qu'elles présentent un lien direct avec les dépenses ou les recettes concernées, à la gestion de la dette et de la trésorerie, aux garanties, cautionnements et avals accordés par l'État, aux autorisations d'utilisation des fonds déposés auprès de l'État par des correspondants.",
         jusqu_a=None,
         motif="La comptabilité de l'État, et — sous condition expresse de "
               "lien direct — la dette, la trésorerie, les garanties. **La "
               "réserve de lien direct est écrite dans la porte elle-même** : "
               "c'est la seule du II qui la porte."),

    # ---- Les monopoles ----------------------------------------------------
    dict(code='M-01', article='Art. 2', rang='monopole', partie='—',
         repere="III. — L'affectation, totale ou partielle, à un tiers d'une ressource établie au profit de l'État ne peut résulter que d'une disposition d'une loi de finances.",
         jusqu_a=None,
         motif="**Monopole sur l'affectation d'une ressource de l'État à un "
               "tiers.** Sert à l'inverse d'une porte : il établit qu'une "
               "mesure d'affectation ou de désaffectation ne peut pas voyager "
               "ailleurs qu'en loi de finances."),
    dict(code='M-02', article='Art. 2', rang='monopole', partie='—',
         repere="IV. — L'affectation du produit d'une imposition de toute nature à un tiers ne peut résulter que d'une disposition d'une loi de finances.",
         jusqu_a=None,
         motif="Monopole sur l'affectation du produit d'une imposition. Sa "
               "borne est écrite à sa suite : les collectivités, leurs "
               "établissements et les organismes de sécurité sociale en sont "
               "exclus, sauf produit affecté en tout ou partie au budget de "
               "l'État."),
    dict(code='M-03', article='Art. 2', rang='condition', partie='—',
         repere="II. — Les impositions de toutes natures peuvent être directement affectées aux collectivités territoriales, à leurs établissements publics et aux organismes de sécurité sociale",
         jusqu_a=None,
         motif="**La condition de fond de toute taxe affectée**, et elle est "
               "une prise directe : l'affectation à un tiers ne peut être "
               "maintenue que si ce tiers est doté de la personnalité morale "
               "et si l'imposition est **en lien avec les missions de service "
               "public qui lui sont confiées**. Une taxe affectée dont le "
               "lien s'est rompu est attaquable sur ce fondement, sans "
               "plaidoirie de domaine."),
    dict(code='M-04', article='Art. 9', rang='monopole', partie='—',
         repere="Les conditions dans lesquelles des dépenses peuvent être engagées par anticipation sur les crédits de l'année suivante sont définies par une disposition de loi de finances.",
         jusqu_a=None,
         motif="Monopole sur l'engagement par anticipation."),
    dict(code='M-05', article='Art. 7', rang='monopole', partie='—',
         repere="Seule une disposition de loi de finances d'initiative gouvernementale peut créer une mission.",
         jusqu_a=None,
         motif="**Monopole gouvernemental sur la création d'une mission.** "
               "C'est une porte fermée à l'amendement parlementaire : une "
               "mesure qui suppose une mission nouvelle est irrecevable quel "
               "que soit son rattachement. Elle se réécrit en programme, ou "
               "elle ne se dépose pas."),
    dict(code='M-06', article='Art. 7', rang='monopole', partie='—',
         repere="Les crédits ne peuvent être modifiés que par une loi de finances",
         jusqu_a=None,
         motif="Monopole sur la modification des crédits, sous réserve des "
               "voies réglementaires nommées — virements, transferts, décrets "
               "d'avance, annulations."),

    # ---- L'obligation de reprise -----------------------------------------
    dict(code='R-01', article='Art. 33', rang='reprise', partie='—',
         repere="Sous réserve des dispositions de l'article 13 de la présente loi organique, lorsque des dispositions d'ordre législatif ou réglementaire sont susceptibles d'affecter les ressources ou les charges de l'État dans le courant de l'année",
         jusqu_a=None,
         motif="**L'argument le plus fort du test de rattachement, et il est "
               "écrit dans le texte.** Une disposition prise ailleurs, dont "
               "les conséquences affectent les ressources ou les charges de "
               "l'État, **doit** être évaluée et autorisée dans la plus "
               "prochaine loi de finances. Une mesure dont l'adoption oblige "
               "la loi de finances à réagir a donc avec elle un lien qui ne "
               "s'invente pas. *À double tranchant : l'invoquer, c'est "
               "admettre que la mesure pourrait être adoptée ailleurs.*"),
    dict(code='R-02', article='Art. 32', rang='reprise', partie='—',
         repere="Les lois de finances présentent de façon sincère l'ensemble des ressources et des charges de l'État.",
         jusqu_a=None,
         motif="Le principe de sincérité. Il ne rattache rien, mais il est le "
               "fondement de toute demande de complétude — et donc l'assise "
               "d'une part de l'axe de transparence, si cet axe s'écrit."),

    # ---- Les annexes ------------------------------------------------------
    dict(code='A-01', article='Art. 51', rang='annexe', partie='—',
         repere="Sont joints au projet de loi de finances de l'année",
         jusqu_a=None,
         motif="**La liste des annexes jointes au projet de loi de finances.** "
               "C'est le siège de toute obligation documentaire nouvelle — et "
               "donc l'assise naturelle de l'axe de transparence, préférable "
               "au 7° du II de l'article 34, qui ne produit qu'un rapport. "
               "Une annexe obligatoire est opposable ; un rapport ne l'est "
               "pas."),
]

# Portes que la pièce de référence ne reproduit pas intégralement. Elles se
# déclarent : le fil suivant les relèvera sur une pièce complète.
NON_RELEVABLES = [
    ('Art. 35', "Le contenu de la loi de finances rectificative — porte du "
                "collectif budgétaire."),
    ('Art. 36', "L'affectation d'une ressource établie au profit de l'État."),
    ('Art. 37', "Le contenu de la loi relative aux résultats de la gestion et "
                "portant approbation des comptes."),
    ('Art. 45', "Les lois spéciales, cinquième catégorie de lois de finances "
                "à l'article 1er."),
    ('Art. 47', "Les ordonnances en cas d'absence de vote dans les délais."),
    ('Art. 51 (8° et suivants)',
     "La suite de la liste des annexes, que la pièce abrège."),
    ('Code de la sécurité sociale, art. LO 111-3',
     "**Le domaine de la loi de financement de la sécurité sociale.** Il ne "
     "se relève pas sur la loi organique relative aux lois de finances : il "
     "est ailleurs, et il se relève par `redaction-legistique` sur sa propre "
     "pièce (A-223)."),
]

RANGS = {
    'definition': 'définition du contenu',
    'obligatoire': 'domaine obligatoire',
    'facultatif': 'domaine facultatif',
    'monopole': 'monopole de la loi de finances',
    'condition': 'condition de fond opposable',
    'reprise': 'obligation de reprise en loi de finances',
    'annexe': 'annexe obligatoire',
}


def _texte(fragment):
    """HTML d'un corps d'article vers texte, sans rien normaliser d'autre."""
    t = re.sub(r'<br\s*/?>', '\n', fragment)
    t = re.sub(r'</p>', '\n\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    return html.unescape(t)


def articles(chemin):
    """numéro d'article → (version déclarée, texte verbatim)."""
    brut = open(chemin, encoding='utf-8').read()
    trouve = {}
    for bloc in re.findall(r'<div class="art">(.*?)</div>\s*</div>', brut, re.S):
        num = re.search(r'<span class="art-num">(.*?)</span>', bloc, re.S)
        ver = re.search(r'<span class="art-version">(.*?)</span>', bloc, re.S)
        corps = re.search(r'<div class="art-body">(.*)', bloc, re.S)
        if not (num and corps):
            continue
        trouve[html.unescape(num.group(1)).strip()] = (
            html.unescape(re.sub('<[^>]+>', '', ver.group(1))).strip() if ver else '',
            _texte(corps.group(1)))
    return trouve


def relever(chemin):
    arts = articles(chemin)
    releve, manques = [], []
    for p in PORTES:
        entree = arts.get(p['article'])
        if entree is None:
            manques.append((p['code'], p['article'], 'article absent de la pièce'))
            continue
        version, texte = entree
        i = texte.find(p['repere'])
        if i < 0:
            manques.append((p['code'], p['article'], 'repère introuvable au texte'))
            continue
        if p['jusqu_a']:
            j = texte.find(p['jusqu_a'], i)
            if j < 0:
                manques.append((p['code'], p['article'], 'borne de fin introuvable'))
                continue
            verbatim = texte[i:j]
        else:
            fin = texte.find('\n', i)
            verbatim = texte[i:] if fin < 0 else texte[i:fin]
        verbatim = verbatim.strip()
        if not verbatim.startswith(p['repere'][:40]):
            manques.append((p['code'], p['article'], 'relevé décalé du repère'))
            continue
        releve.append(dict(p, verbatim=verbatim, version=version))
    return releve, manques


def rendre(releve, manques, chemin_source):
    L = []
    a = L.append
    a('# La grille des portes du domaine de la loi de finances')
    a('')
    a(f'*Relevé en verbatim sur `{chemin_source}` par '
      '`appareil/portes_domaine.py`. Aucune phrase de loi n\'est écrite à la '
      'main : le module ne porte que des repères, et un repère qui ne se '
      'retrouve pas sort la porte en manque plutôt que de la composer.*')
    a('')
    a(f'*Pièce de référence : {SOURCE} — texte verbatim Légifrance en vigueur '
      'au 07/05/2026.*')
    a('')
    a('**Cette grille est au second rang.** Elle dit ce qui est acquis sans '
      'plaidoirie ; elle ne dit pas ce qu\'on tente. Le rattachement se plaide '
      'par l\'implicite budgétaire et le contrefactuel (A-225).')
    a('')
    a('---')
    a('')
    a('## Le compte')
    a('')
    a(f'{len(releve)} porte(s) relevée(s) en verbatim, '
      f'{len(manques)} en échec de relevé, '
      f'{len(NON_RELEVABLES)} déclarée(s) non relevable(s) sur cette pièce.')
    a('')
    for cle, nom in RANGS.items():
        n = sum(1 for p in releve if p['rang'] == cle)
        if n:
            a(f'- **{nom}** — {n}')
    a('')
    a('---')
    a('')
    ordre = ['definition', 'obligatoire', 'facultatif', 'condition',
             'monopole', 'reprise', 'annexe']
    for cle in ordre:
        lot = [p for p in releve if p['rang'] == cle]
        if not lot:
            continue
        a(f'## {RANGS[cle].capitalize()}')
        a('')
        for p in lot:
            partie = ('' if p['partie'] == '—'
                      else f' · {p["partie"]} partie'
                      if p['partie'] in ('première', 'seconde')
                      else f' · article {p["partie"]}')
            a(f'### {p["code"]} — {p["article"]}{partie}')
            a('')
            for ligne in p['verbatim'].split('\n'):
                a(f'> {ligne.strip()}' if ligne.strip() else '>')
            a('')
            a(f'{p["motif"]}')
            a('')
            if p['version']:
                a(f'*{p["version"]}*')
                a('')
        a('---')
        a('')
    if manques:
        a('## Échecs de relevé')
        a('')
        a('**Une porte en échec ne se compose pas.** Le repère ne s\'est pas '
          'retrouvé au texte : soit la pièce a changé, soit le repère est '
          'faux. Dans les deux cas cela se reprend au module, jamais au '
          'livrable.')
        a('')
        for code, art, raison in manques:
            a(f'- `{code}` — {art} : {raison}')
        a('')
        a('---')
        a('')
    a('## Portes non relevables sur cette pièce')
    a('')
    a('La pièce de référence reproduit certains articles en résumé. **Leur '
      'porte existe et ne se relève pas ici** — elle se relèvera sur une pièce '
      'complète, entrée par pièce jointe du fil (A-234).')
    a('')
    for art, quoi in NON_RELEVABLES:
        a(f'- **{art}** — {quoi}')
    a('')
    a('---')
    a('')
    a('## Ce que la grille apprend, et qui ne se voyait pas avant le relevé')
    a('')
    a('**Trois portes nomment les opérateurs et les tiers, et elles sont de '
      'rangs différents.** Le 3° bis du I porte l\'assiette, le taux, '
      'l\'affectation et le recouvrement des impositions affectées à une '
      'personne morale autre que l\'État — et il est facultatif. Le 5° bis du '
      'I permet à la loi de finances de **décider d\'attribuer le produit à '
      'l\'État** — et il est obligatoire. Le 3° du II fixe les plafonds '
      'd\'emplois des opérateurs — et il est obligatoire. Une mesure sur le '
      'financement d\'une agence a donc trois assises possibles, en deux '
      'parties différentes du texte.')
    a('')
    a('**Le 5° bis exclut nommément trois catégories de bénéficiaires** — les '
      'collectivités territoriales, leurs établissements publics et les '
      'organismes de sécurité sociale. La reprise de produit ne les atteint '
      'pas. C\'est la borne qui décide, sur une taxe affectée donnée, si la '
      'porte est ouverte ou s\'il faut plaider.')
    a('')
    a('**La condition de lien de l\'article 2-II est une prise, et elle ne '
      'demande aucune plaidoirie de domaine.** Une imposition ne peut rester '
      'affectée à un tiers que si elle est en lien avec les missions de '
      'service public qui lui sont confiées. Une taxe dont le lien s\'est '
      'rompu se supprime sur ce fondement, et le fondement est écrit dans la '
      'loi organique.')
    a('')
    a('**Le 8° du II est la seule porte du II qui écrit sa propre réserve de '
      'lien direct.** Les autres n\'en portent pas — ce qui ne veut pas dire '
      'qu\'elles en sont dispensées, mais que leur limite est jurisprudentielle '
      'et non textuelle. *À instruire ; le fil ne le tranche pas.*')
    a('')
    a('**Le monopole gouvernemental sur la création d\'une mission est une '
      'porte fermée qui commande la rédaction.** Aucune plaidoirie ne '
      'l\'ouvre. Une mesure qui suppose une mission nouvelle se réécrit en '
      'programme, ou elle ne se dépose pas.')
    a('')
    a('**L\'article 51 vaut mieux que le 7° du II pour l\'axe de '
      'transparence.** Les deux sont ouverts. Le 7° produit un rapport, que '
      'l\'administration remet ou ne remet pas ; l\'article 51 produit une '
      '**annexe jointe au projet de loi de finances**, dont l\'absence est un '
      'défaut de la procédure. *Le choix entre les deux appartient à '
      'l\'auteur : le fil l\'inscrit et s\'arrête.*')
    a('')
    return '\n'.join(L) + '\n'


def main(src, dst):
    releve, manques = relever(src)
    texte = rendre(releve, manques, src.split('/')[-1])
    os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
    open(dst, 'w', encoding='utf-8').write(texte)
    print(f'{dst} — {len(releve)} porte(s) relevée(s), {len(manques)} en échec, '
          f'{os.path.getsize(dst)} octets')
    for code, art, raison in manques:
        print(f'    ÉCHEC {code} — {art} : {raison}')
    return 1 if manques else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
