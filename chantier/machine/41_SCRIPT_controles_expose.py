# -*- coding: utf-8 -*-
"""
Contrôles outillés de l'exposé sommaire et de la liasse — implémentation UNIQUE.

Le contrat l'exige : « La règle s'implémente une fois, et l'implémentation vit
dans la valise avec son jeu d'essai. Deux implémentations d'une même règle sont
deux règles. »

Entrée : un fichier de liasse au format markdown de travail, dont chaque
amendement porte un cartouche, une pièce déposée et un exposé sommaire.
Sortie : un verdict par contrôle, pour chaque exposé et pour le bloc.

    python3 controles_expose.py liasse.md [--jetons "5,5 %;10 %"] [--noms "taxe x;dotation y"] [--json]
    python3 controles_expose.py --test        (joue le jeu d'essai)

  --jetons  les chiffres qui CONSTITUENT le dispositif (taux substitué, seuil
            fixé, montant plafonné), séparés par des POINTS-VIRGULES — la
            virgule est le séparateur décimal.
  --noms    les noms propres d'entités ou de dispositifs retranchés du compte
            de l'en-tête (borne asymétrique), séparés par des points-virgules.
  L'outil ne porte AUCUNE liste propre à une liasse : ce qu'il ne reçoit pas,
  il le compte.

Version 20261001-c. Couvre : décompte, virgule devant conjonction, en-tête
d'identification (borne asymétrique, périphrase), tour vide, registre
administratif, formulation interdite, phrase de sens, plafond des chiffres de
preuve, proportion du constat (cible le tiers, tolérance 30–52 %), alignements
des ouvertures, des finales et des phrases de sens, et les quatre contrôles de
liasse : concordance notice/cartouche, exhaustivité, unicité des titres,
complétude du cartouche.
"""
import re, sys, json
from collections import Counter

# ---------------------------------------------------------------- § 8 — unité
def mots(t):
    """Un mot = une suite de caractères entre deux espaces. Un nombre en
    chiffres compte pour un mot, séparateur de milliers compris. Un mot lié par
    un trait d'union compte pour un. Les appels de note ne comptent pas ; la
    parenthèse de source compte."""
    t = re.sub(r'\[\^\d+\]|[¹²³⁴⁵⚑]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'(?<=\d)[ \u00a0](?=\d)', '\u00a0', t)
    return [m for m in t.split(' ') if m.strip(' .,;:!?«»—–-')]

def compte(t):
    return len(mots(t))

# ------------------------------------------------------- motifs des contrôles
PERIPHRASE = r"\b(vise à|visent à|propose de|proposent de|a pour objet de|ont pour objet de|tend à|tendent à|entend|entendent)\b"
TOUR_VIDE  = r"\b(il s'agit de|l'objectif est de|ce dispositif consiste à|le but est de)\b"
REGISTRE   = r"\b(il apparaît que|il convient de|force est de constater|il serait souhaitable|le présent amendement vise)\b"
VIRGULE    = r",\s+(?:et|ou|mais|ni|car|or|donc)\b"
INTERDIT52 = r"échappe à l'arbitrage annuel du Parlement"
APPELS = r'\[\^\d+\]|[¹²³⁴⁵⁶⁷⁸⁹⚑]'
TOLERANCE = (30, 52)          # proportion du constat : cible le tiers, tolérance 30–52 %

def compte_entete(t, noms=()):
    """Borne asymétrique : le nom propre déclaré ne compte pas au plafond.
    Les noms se DÉCLARENT (`noms`) ; l'outil n'en connaît aucun de lui-même.
    Le plus long d'abord, et un nom n'est retranché qu'une fois."""
    low, hors = t.lower(), 0
    for n in sorted({x.strip().lower() for x in noms if x.strip()}, key=len, reverse=True):
        if n in low:
            hors += len(n.split(' '))
            low = low.replace(n, ' ', 1)
    return compte(t) - hors

def chiffres(corps, dispositif_tokens=()):
    """Arbitrage C : le plafond porte sur les chiffres de PREUVE. Le chiffre qui
    constitue le dispositif — taux substitué, seuil fixé, montant plafonné — n'y
    entre pas, non plus que l'hypothèse (A3). `dispositif_tokens` les déclare."""
    c = re.sub(APPELS, '', corps)          # un appel de note collé à une année
    c = re.sub(r'\b(19|20)\d{2}\b', ' ', c) # ne fait pas de l'année un chiffre
    # Une adresse de droit n'est pas un chiffre de preuve. Trois formes, et la
    # plus spécifique d'abord : l'article codifié (« L. 3262-1 »), l'article
    # nommé avec son rang (« article 81 », « article 1er »), et l'énumération
    # interne (« 19° », « alinéa 3 »). Les compter a déjà fait tomber un exposé
    # exact sur un plafond de deux.
    c = re.sub(r"\b(?:L|R|D|LO|A)\.?\s*\d+(?:\s*[-–‑]\s*\d+)*", ' ', c)
    c = re.sub(r"\b(?:articles?|art\.|n°)\s*(?:du\s+|de\s+l[’']|l[’'])?"
               r"\d+(?:\s*(?:er|ers|ème|e|bis|ter|quater|quinquies))?"
               r"(?:\s*[-–‑]\s*\d+)*", ' ', c, flags=re.I)
    c = re.sub(r"\b\d+\s*°", ' ', c)
    c = re.sub(r"\b(?:alinéas?|paragraphes?|paragraphe)\s*\d+", ' ', c, flags=re.I)
    bruts = [x.strip() for x in
             re.findall(r'\d[\d  ,]*\s*(?:%|€|millions?|milliards?|points?)?', c)
             if x.strip()]
    preuve = [x for x in bruts if not any(d in x for d in dispositif_tokens)]
    return bruts, preuve

# --------------------------------------------------------------------- parse
def parse(md):
    """Rend la notice et la liste des amendements. Tolère l'absence de cartouche."""
    notice = []
    m = re.search(r'# NOTICE\n\n(.*?)\n\n---', md, re.S)
    if m:
        for ln in m.group(1).split('\n'):
            if ln.strip().startswith('|') and not re.match(r'^\|[\s:\-|]+\|$', ln.strip()):
                notice.append([c.strip() for c in ln.strip().strip('|').split('|')])
        notice = notice[1:]                      # on jette l'en-tête de colonnes
    cart = re.findall(r'\*\*Titre\*\* (.+?) ·\n\*\*Chapô\*\* (.+?) ·\n(?:\*\*Intention\*\* ([^\n]*?)(?: ·)?\n)?', md, re.S)
    # marque nue (« EXPOSÉ SOMMAIRE ») ou précédée de dièses (« #### EXPOSÉ SOMMAIRE »)
    blocs = re.split(r'(?m)^(?:#+[ \t]*)?EXPOSÉ SOMMAIRE[ \t]*$', md)[1:]
    am = []
    for i, b in enumerate(blocs):
        b = b.split('\n---')[0]
        paras = [x.strip() for x in b.split('\n\n')
                 if x.strip() and not re.match(r'^[¹²³⁴⁵⁶⁷⁸⁹]\s', x.strip())]
        if not paras:
            continue
        am.append(dict(
            n=i + 1,
            entete=paras[0],
            temps=paras[1:],
            corps=' '.join(paras[1:]),
            titre=re.sub(r'\s+', ' ', cart[i][0]).strip() if i < len(cart) else None,
            chapo=re.sub(r'\s+', ' ', cart[i][1]).strip() if i < len(cart) else None,
            intention=cart[i][2].strip() if i < len(cart) else None,
        ))
    return notice, am

# ------------------------------------------------------------------ contrôles
def controler(md, dispositif_tokens=(), noms=()):
    notice, am = parse(md)
    out = {'exposes': [], 'bloc': {}, 'liasse': {}}
    debuts, finales, sens_ouv, titres = [], [], [], []

    for a in am:
        corps, ent = a['corps'], a['entete']
        n, n1 = compte(corps), compte(a['temps'][0]) if a['temps'] else 0
        pct = round(100 * n1 / n, 1) if n else 0
        m = re.search(r'(Dit simplement|En clair)[^.]*\.', corps)
        sens = m.group(0) if m else None
        finale = re.split(r'(?<=[.!?])\s+', a['temps'][-1].strip())[-1] if a['temps'] else ''
        bruts, preuve = chiffres(corps, dispositif_tokens)
        out['exposes'].append(dict(
            n=a['n'], mots=n, temps1=n1, part_constat=pct,
            fourchette_200_300=200 <= n <= 300,
            proportion_dans_tolerance=TOLERANCE[0] <= pct <= TOLERANCE[1],
            entete_mots=compte(ent), entete_mots_hors_nom=compte_entete(ent, noms),
            entete_borne=(compte(ent) >= 10 and compte_entete(ent, noms) <= 15),
            entete_periphrase=bool(re.search(PERIPHRASE, ent, re.I)),
            phrase_de_sens=bool(sens),                                        # A7
            tour_vide=bool(re.search(TOUR_VIDE, corps, re.I)),
            registre_administratif=bool(re.search(REGISTRE, corps, re.I)),
            formulation_interdite=bool(re.search(INTERDIT52, corps, re.I)),   # § 5.2
            virgules=len(re.findall(VIRGULE, corps + ' ' + ent)),             # § 12
            chiffres_bruts=len(bruts), chiffres_preuve=len(preuve),
            plafond_chiffres=len(preuve) <= 2,                                # § 5.5 + C
        ))
        debuts.append(' '.join(mots(a['temps'][0])[:3]).lower() if a['temps'] else '')
        finales.append(' '.join(mots(finale)[:2]).lower())
        if sens:
            sens_ouv.append(' '.join(mots(sens)[:4]).lower())
        if a['titre']:
            titres.append(a['titre'])

    rep = lambda xs: [k for k, c in Counter(xs).items() if c > 1]
    out['bloc'] = {
        'controle_7_ouvertures_repetees': rep(debuts),
        'controle_7bis_finales_repetees': rep(finales),
        'controle_7ter_sens_repetees': rep(sens_ouv),
        'finales_distinctes': f'{len(set(finales))}/{len(finales)}',
    }
    # ---- quatre contrôles de liasse
    conc = []
    for i, a in enumerate(am):
        if i < len(notice) and a['titre'] is not None:
            li = notice[i]
            if len(li) > 2 and (li[1].strip() != a['titre'] or li[2].strip() != a['chapo']):
                conc.append(a['n'])
    incomplets = [a['n'] for a in am
                  if not (a['titre'] and a['chapo'] and a['intention'])]
    out['liasse'] = {
        '1_concordance_notice_cartouche': conc or 'OK',
        '2_exhaustivite': (f'OK — {len(notice)} lignes / {len(am)} blocs'
                           if notice and len(notice) == len(am)
                           else f'ÉCART — {len(notice)} lignes / {len(am)} blocs'),
        '3_titres_uniques': rep(titres) or 'OK',
        '4_cartouche_complet': incomplets or 'OK',
    }
    return out

def resume(r):
    e = r['exposes']
    ko = lambda k: [x['n'] for x in e if not x[k]]
    vrai = lambda k: [x['n'] for x in e if x[k]]
    L = [
        ('corps dans 200–300 mots', ko('fourchette_200_300')),
        ('proportion du constat dans la tolérance 30–52 % (signalement)', ko('proportion_dans_tolerance')),
        ("en-tête : borne 10–15, plafond hors nom propre", ko('entete_borne')),
        ("en-tête : périphrase", vrai('entete_periphrase')),
        ('phrase de sens présente', ko('phrase_de_sens')),
        ('tour vide au pivot du temps 2', vrai('tour_vide')),
        ('registre administratif', vrai('registre_administratif')),
        ('formulation interdite du § 5.2', vrai('formulation_interdite')),
        ('virgule devant conjonction (§ 12)', [x['n'] for x in e if x['virgules']]),
        ('plafond des chiffres de preuve', ko('plafond_chiffres')),
    ]
    print(f"{len(e)} exposés\n")
    for lib, bad in L:
        print(f"  {'OK   ' if not bad else 'ÉCART'}  {lib}" + (f" → {bad}" if bad else ''))
    print()
    for k, v in r['bloc'].items():
        print(f"  {k} : {v if v else 'aucune'}")
    print()
    for k, v in r['liasse'].items():
        print(f"  {k} : {v}")

# ------------------------------------------------------------- jeu d'essai
ESSAI = """# NOTICE

| n° | titre | ce que l'amendement fait | emplacement | état | à vérifier |
|---|---|---|---|---|---|
| 1 | Un titre d'essai | Faire la chose. | art. 1er | à déposer | — |

---

## Cartouche n° 1 — *hors pièce déposée*

**Titre** Un titre d'essai ·
**Chapô** Faire la chose. ·
**Intention** essai

#### AMENDEMENT

#### EXPOSÉ SOMMAIRE

Cet amendement vise à supprimer la taxe sur la valeur ajoutée de 10 % sans délai.

Un redevable paie 1 200 € par an, et il ne sait pas pourquoi. Il convient de le
dire. Cette dépense échappe à l'arbitrage annuel du Parlement.

Il s'agit de supprimer la taxe. Le rendement est de 8,2 milliards d'euros, le coût
de gestion de 400 millions et l'assiette de 50 milliards.

Adopter cet amendement supprime la taxe.
"""

NOMS_ESSAI = ('taxe sur la valeur ajoutée',)

ATTENDU = dict(entete_periphrase=True, tour_vide=True, registre_administratif=True,
               formulation_interdite=True, phrase_de_sens=False,
               plafond_chiffres=False)

def test():
    r = controler(ESSAI, noms=NOMS_ESSAI)
    e = r['exposes'][0]
    ok = True
    for k, v in ATTENDU.items():
        got = e[k]
        statut = 'OK   ' if got == v else 'ÉCHEC'
        if got != v: ok = False
        print(f"  {statut}  {k} : attendu {v}, obtenu {got}")
    # la virgule, et la borne d'en-tête qui doit PASSER ici : 15 mots bruts,
    # moins les cinq du nom propre, soit 10 hors nom — la borne A5 est tenue.
    for k, v in (('virgules', 1), ('entete_borne', True)):
        got = e[k]; statut = 'OK   ' if got == v else 'ÉCHEC'
        if got != v: ok = False
        print(f"  {statut}  {k} : attendu {v}, obtenu {got}")
    # second cas : en-tête trop long, sans nom propre à retrancher
    long_ = ESSAI.replace(
        "Cet amendement vise à supprimer la taxe sur la valeur ajoutée de 10 % sans délai.",
        "Cet amendement supprime le taux intermédiaire et renvoie au taux normal toutes les opérations qui en relevaient.")
    e2 = controler(long_, noms=NOMS_ESSAI)['exposes'][0]
    for k, v in (('entete_borne', False), ('entete_periphrase', False)):
        got = e2[k]; statut = 'OK   ' if got == v else 'ÉCHEC'
        if got != v: ok = False
        print(f"  {statut}  [cas 2] {k} : attendu {v}, obtenu {got}")
    # cas 3 : sans déclaration du nom, l'outil ne retranche rien (aucune liste interne)
    e3 = controler(ESSAI)['exposes'][0]
    got = e3['entete_mots_hors_nom'] == e3['entete_mots']
    print(f"  {'OK   ' if got else 'ÉCHEC'}  [cas 3] aucun nom retranché sans déclaration")
    ok = ok and got
    # cas 4 : une année suivie d'un appel de note n'est pas un chiffre de preuve
    md4 = ESSAI.replace("Le rendement est de 8,2 milliards d'euros, le coût\nde gestion de 400 millions et l'assiette de 50 milliards.",
                        "Le rendement est de 8,2 milliards d'euros pour 2026¹.")
    e4 = controler(md4, noms=NOMS_ESSAI)['exposes'][0]
    got = e4['chiffres_preuve'] == 2
    print(f"  {'OK   ' if got else 'ÉCHEC'}  [cas 4] année suivie d'un appel : preuve attendue 2, obtenu {e4['chiffres_preuve']}")
    ok = ok and got
    # cas 5 : un taux à virgule décimale se déclare en jeton et sort du plafond
    md5 = md4.replace("8,2 milliards d'euros pour 2026¹.", "8,2 milliards d'euros pour 2026¹. Le taux passe à 5,5 %.")
    e5a = controler(md5, noms=NOMS_ESSAI)['exposes'][0]
    e5b = controler(md5, dispositif_tokens=jetons('5,5 %;10 %'), noms=NOMS_ESSAI)['exposes'][0]
    got = (e5a['chiffres_preuve'] == 3 and e5b['chiffres_preuve'] == 2)
    print(f"  {'OK   ' if got else 'ÉCHEC'}  [cas 5] jetons « 5,5 %;10 % » : preuve {e5a['chiffres_preuve']} → {e5b['chiffres_preuve']}")
    ok = ok and got
    # cas 6 : cartouche sans intention → contrôle de liasse 4 en écart
    md6 = ESSAI.replace("**Intention** essai\n", "")
    got = controler(md6, noms=NOMS_ESSAI)['liasse']['4_cartouche_complet'] == [1]
    print(f"  {'OK   ' if got else 'ÉCHEC'}  [cas 6] cartouche sans intention : contrôle de liasse 4 en écart")
    ok = ok and got
    # cas 7 : marques nues, sans dièses — la liasse se lit quand même
    md7 = ESSAI.replace('#### AMENDEMENT', 'AMENDEMENT').replace('#### EXPOSÉ SOMMAIRE', 'EXPOSÉ SOMMAIRE')
    got = len(controler(md7, noms=NOMS_ESSAI)['exposes']) == 1
    print(f"  {'OK   ' if got else 'ÉCHEC'}  [cas 7] marques nues : un exposé lu")
    ok = ok and got
    # cas 8 : une note ⁴ en paragraphe isolé ne compte pas au corps
    md8 = ESSAI.replace("Adopter cet amendement supprime la taxe.\n",
                        "Adopter cet amendement supprime la taxe.\n\n⁴ Note isolée qui ne doit pas compter.\n")
    got = controler(md8, noms=NOMS_ESSAI)['exposes'][0]['mots'] == e['mots']
    print(f"  {'OK   ' if got else 'ÉCHEC'}  [cas 8] note ⁴ isolée hors décompte")
    ok = ok and got
    # cas 9 : une adresse de droit n'est pas un chiffre de preuve
    t9 = ("Les articles L. 3262-1 et L. 3261-6 du code du travail, et "
          "l'article 81, 19° du code général des impôts, privent le salarié "
          "de 40 % de la valeur.")
    got = chiffres(t9)[1] == ['40 %']
    print(f"  {'OK   ' if got else 'ÉCHEC'}  [cas 9] adresses de droit hors "
          f"décompte : preuve {chiffres(t9)[1]}")
    ok = ok and got
    print('\nJEU D\'ESSAI :', 'PASSE' if ok else 'ÉCHOUE')
    return 0 if ok else 1

def jetons(s):
    """Séparateur : le point-virgule. La virgule est décimale."""
    return tuple(x.strip() for x in s.split(';') if x.strip())

def option(nom):
    if nom in sys.argv:
        i = sys.argv.index(nom)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return ''

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        sys.exit(test())
    if len(sys.argv) < 2 or sys.argv[1].startswith('--'):
        print(__doc__); sys.exit(2)
    md = open(sys.argv[1], encoding='utf-8').read()
    r = controler(md, jetons(option('--jetons')), jetons(option('--noms')))
    if not r['exposes']:
        print("AUCUN EXPOSÉ LU — la liasse ne suit pas la nomenclature du § 4.3 "
              "(marque « EXPOSÉ SOMMAIRE » seule sur sa ligne). Silence ≠ passe.")
        sys.exit(1)
    resume(r)
    if '--json' in sys.argv:
        print(json.dumps(r, ensure_ascii=False, indent=1))
