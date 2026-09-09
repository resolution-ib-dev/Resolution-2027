# -*- coding: utf-8 -*-
"""Contrôle des champs rédigés du côté gain.

Un apport dit à la personne ce qu'elle y gagne. Il ne recopie pas le livre.

La raison n'est pas cosmétique. L'énoncé d'un nœud du `REF_doctrine` est une
phrase du manuscrit reprise mot pour mot : c'est le régime transitoire, celui
d'une ligne dont l'apport n'est pas écrit. Un apport qui reprend cette phrase
n'écrit rien — il donne au régime transitoire l'apparence de la cible, et le
compteur de `make etat` se met à mentir. C'est le seul défaut du côté gain
qu'aucun contrôle ne voyait.

Quatre contrôles.

A1 — un apport ne reprend pas l'énoncé du nœud qu'il projette. La comparaison
     se fait sur le texte normalisé, dans les deux sens : l'inclusion compte
     autant que l'égalité.
A2 — un apport ne porte pas un segment verbatim du manuscrit. Huit mots
     consécutifs suffisent à trahir une recopie ; en deçà, une expression
     commune est une coïncidence de langue et non un emprunt.
A3 — un apport s'écrit à la deuxième personne du pluriel, sans nomenclature
     interne et sans citer le corpus comme autorité. **Le contrôle porte sur la
     vedette et la phrase ensemble** : elles font une unité (A-147), et
     « Votre pension — le système se remet d'aplomb sans y toucher » s'adresse
     bien à quelqu'un.
A4 — une contrepartie suit les règles A1 et A2. Elle nomme qui paie ; elle ne
     recopie pas davantage.
A5 — deux apports d'une même catégorie ne se ressemblent pas. Une fiche qui
     répète quatre fois « votre retraite ne dépend plus de… » sous quatre
     tournures a quatre lignes et un seul message. Le contrôle compare les mots
     pleins deux à deux, à l'intérieur d'une catégorie, et sort les couples qui
     en partagent plus de la moitié.

A6 — trois gains ou plus d'une même catégorie sous le même levier de doctrine
     forment une grappe. La redite qu'on remarque en lisant une fiche est
     rarement lexicale — quatre phrases sur la retraite par capitalisation
     n'ont pas trois mots communs et disent la même chose. Ce qui les trahit
     est leur origine. A5 cherche les mots, A6 cherche la source ; il faut les
     deux.

A7 — un même ancrage projeté sur deux catégories ne porte pas deux fois le même
     apport. Un effet atteint plusieurs personnes, mais il ne leur fait pas la
     même chose : il y a toujours un angle. Deux apports identiques signent une
     écriture au fil, non une projection.
A8 — une vedette est **une grandeur** — un nombre et son unité — **ou un groupe
     nominal court** : article et nom, trois mots au plus, ou un objet nommé du
     corpus. « Reprendre paie » et « Rien ne baisse » sont des phrases : elles
     font autant de présentations disparates qu'il y a de lignes.

A1, A2, A4 et A7 sont des échecs. A3, A5 et A6 sont des signalements : le registre et
la redite se jugent, ils ne se prouvent pas, et l'appareil est aveugle à la voix.

Usage : python3 controle_apports.py Positions.json REF.json [manuscrit.html]
"""
import json
import re
import sys
import unicodedata

# Longueur du segment commun à partir de laquelle une coïncidence de langue
# cesse d'être plausible. Écrit ici, avec sa raison, plutôt que remonté jusqu'à
# ce que le compte tombe.
SEGMENT = 8

PERSONNE = re.compile(r'\b(vous|votre|vos)\b', re.I)
NOMENCLATURE = re.compile(r'\b([DC]-?\d{1,2}(-\d+)*(-[epsr]\d+)?|M-\d{3,4})\b')
AUTORITE = re.compile(r'\b(le manuscrit|le livre|notre essai|le référentiel|'
                      r'le REF_doctrine|le corpus)\b', re.I)

# Mots vides du français, pour la comparaison de A5. Deux apports qui partagent
# « votre », « de » et « les » ne se ressemblent pas.
VIDES = set("""a au aux avec ce ces dans de des du elle en et eux il ils je la
le les leur lui ma mais me meme mes moi mon ne nos notre nous on ou par pas pour
qu que qui sa se ses son sur ta te tes toi ton tu un une vos votre vous y est
sont etes sommes ai as ont avez avons plus moins tout tous toute toutes chaque
d l n s c j m t qu' si comme sans sous entre vers chez dont ou ainsi cela
""".split())
# Au-dessus de cette part de mots pleins communs, deux apports d'une même
# catégorie disent la même chose. Écrit ici avec sa raison : en deçà, deux
# phrases du même domaine partagent naturellement leur vocabulaire.
RESSEMBLANCE = 0.5
# À partir de trois gains d'une même catégorie sous un même levier, la fiche
# répète un thème. Deux est une insistance, trois est une liste.
GRAPPE = 3
# Le levier est le préfixe à deux niveaux de l'ancrage : `D8-2-2-e1` → `D8-2`.
LEVIER = re.compile(r'^([A-Z]\d+-\d+)')

# Objets que le corpus nomme, et qui tiennent lieu de vedette tels quels.
OBJETS = {'compte épargne', 'compte éducation', 'compte santé',
          'aide fondamentale', 'plan de départ', 'taux unique'}
# Une vedette nominale : article ou déterminant, puis un nom. Trois mots au plus.
NOMINALE = re.compile(r"^(le|la|les|l'|l’|un|une|votre|vos|mon|nos)\s*\S",
                      re.I)
GRANDEUR = re.compile(r'^[+\-−]?\d')

BALISE = re.compile(r'<[^>]+>')
ESPACES = re.compile(r'\s+')
PONCTUATION = re.compile(r'[^\w\s]', re.UNICODE)


def normalise(texte):
    """Minuscules, apostrophes unifiées, ponctuation et accents retirés.

    Une recopie qui aurait changé une apostrophe typographique en apostrophe
    droite, ou remplacé une virgule par un point, resterait une recopie.
    """
    t = unicodedata.normalize('NFD', texte or '')
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    t = t.replace('’', "'").replace('‑', '-').replace(' ', ' ')
    t = PONCTUATION.sub(' ', t.lower())
    return ESPACES.sub(' ', t).strip()


def mots(texte):
    return normalise(texte).split()


def segments(texte, n=SEGMENT):
    m = mots(texte)
    return {' '.join(m[i:i + n]) for i in range(max(0, len(m) - n + 1))}


def enonces(ref):
    """id du nœud → son énoncé ou son intitulé, partout dans le REF."""
    table = {}

    def descendre(o):
        if isinstance(o, dict):
            i = o.get('id')
            if isinstance(i, str):
                texte = o.get('enonce') or o.get('intitule') or o.get('valeur')
                if isinstance(texte, str) and texte:
                    table[i] = texte
            for v in o.values():
                descendre(v)
        elif isinstance(o, list):
            for v in o:
                descendre(v)

    descendre(ref)
    return table


def pleins(texte):
    """Mots porteurs de sens d'un texte, sans les vides ni les nombres."""
    return {m for m in mots(texte)
            if m not in VIDES and len(m) > 2 and not m.isdigit()}


def recopie(texte, source):
    """Vrai si l'un des deux textes normalisés contient l'autre."""
    a, b = normalise(texte), normalise(source)
    if not a or not b:
        return False
    return a in b or b in a


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    positions = json.load(open(argv[1], encoding='utf-8'))
    table = enonces(json.load(open(argv[2], encoding='utf-8')))

    corpus = set()
    if len(argv) > 3:
        brut = open(argv[3], encoding='utf-8').read()
        corpus = segments(BALISE.sub(' ', brut))

    gains = [l for l in positions['lignes'] if l.get('position') == 'gagnant']
    ecrits = [l for l in gains if l.get('apport')]

    a1, a2, a3, a4, a5, a6, a7, a8 = [], [], [], [], [], [], [], []
    for l in ecrits:
        cle = f"{l['ancrage']}|{l['position']}|{l['categorie']}"
        source = table.get(l['ancrage'], '')
        if source and recopie(l['apport'], source):
            a1.append((cle, l['apport'], source))
        if corpus:
            communs = sorted(segments(l['apport']) & corpus)
            if communs:
                a2.append((cle, communs))
            if l.get('contrepartie'):
                communs = sorted(segments(l['contrepartie']) & corpus)
                if communs:
                    a4.append((cle, communs))
        if source and l.get('contrepartie') \
                and recopie(l['contrepartie'], source):
            a4.append((cle, ['— contrepartie identique à l’énoncé']))
        motifs = []
        unite = f"{l.get('vedette') or ''} {l['apport']}"
        if not PERSONNE.search(unite):
            motifs.append('pas de deuxième personne du pluriel')
        if NOMENCLATURE.search(l['apport']):
            motifs.append('nomenclature interne')
        if AUTORITE.search(l['apport']):
            motifs.append('le corpus cité comme autorité')
        if motifs:
            a3.append((cle, ', '.join(motifs)))

    print(f"{len(gains)} gain(s), {len(ecrits)} apport(s) écrit(s), "
          f"{len(gains) - len(ecrits)} en régime transitoire")
    print(f"A1 — {len(a1)} apport(s) qui reprennent l’énoncé du nœud")
    for cle, apport, source in a1:
        print(f"    {cle}")
        print(f"        apport : {apport[:100]}")
        print(f"        énoncé : {source[:100]}")
    if corpus:
        print(f"A2 — {len(a2)} apport(s) portant {SEGMENT} mots consécutifs "
              f"du manuscrit")
    else:
        print("A2 — manuscrit non fourni, contrôle non joué")
    for cle, communs in a2:
        print(f"    {cle} — « {communs[0]} »")
    print(f"A3 — {len(a3)} apport(s) hors registre, signalement")
    for cle, motif in a3:
        print(f"    {cle} — {motif}")
    print(f"A4 — {len(a4)} contrepartie(s) recopiée(s)")
    for cle, communs in a4:
        print(f"    {cle} — « {communs[0]} »")

    # A5 — la redite se cherche à l'intérieur d'une catégorie : deux apports de
    # deux fiches différentes peuvent légitimement se ressembler.
    # Une modalité redit par construction le gain qu'elle qualifie : la
    # comparer à lui sortirait un signalement à chaque fois, pour rien.
    par_cat = {}
    for l in ecrits:
        if l.get('modalite'):
            continue
        par_cat.setdefault(l['categorie'], []).append(l)
    for cid, lot in sorted(par_cat.items()):
        for i, x in enumerate(lot):
            for y in lot[i + 1:]:
                px, py = pleins(x['apport']), pleins(y['apport'])
                if not px or not py:
                    continue
                part = len(px & py) / min(len(px), len(py))
                if part >= RESSEMBLANCE:
                    a5.append((cid, x['ancrage'], y['ancrage'], part,
                               sorted(px & py)))
    print(f"A5 — {len(a5)} couple(s) d’apports qui se ressemblent, signalement")
    for cid, a, b, part, communs in a5:
        print(f"    {cid} · {a} ~ {b} — {part:.0%} de mots pleins communs : "
              f"{', '.join(communs[:6])}")

    # A6 — la grappe : plusieurs gains d'une catégorie sous le même levier.
    for cid, lot in sorted(par_cat.items()):
        grappes = {}
        for l in lot:
            m = LEVIER.match(l['ancrage'])
            if m:
                grappes.setdefault(m.group(1), []).append(l['ancrage'])
        for levier, membres in sorted(grappes.items()):
            if len(membres) >= GRAPPE:
                a6.append((cid, levier, membres))
    print(f"A6 — {len(a6)} grappe(s) de gains sous un même levier, signalement")
    for cid, levier, membres in a6:
        print(f"    {cid} · {levier} — {len(membres)} gains : "
              f"{', '.join(membres)}")

    # A7 — le même ancrage sur deux catégories
    par_ancrage = {}
    for l in ecrits:
        if l.get('modalite'):
            continue
        par_ancrage.setdefault(l['ancrage'], []).append(l)
    for anc, lot in sorted(par_ancrage.items()):
        vus = {}
        for l in lot:
            n = normalise(l['apport'])
            if n in vus:
                a7.append((anc, vus[n], l['categorie'], l['apport']))
            else:
                vus[n] = l['categorie']
    print(f"A7 — {len(a7)} apport(s) recopié(s) d’une catégorie à l’autre")
    for anc, c1, c2, txt in a7:
        print(f"    {anc} · {c1} = {c2} — « {txt[:70]} »")

    # A8 — la forme de la vedette
    for l in ecrits:
        v = (l.get('vedette') or '').strip()
        if not v or l.get('modalite'):
            continue
        if GRANDEUR.match(v) or v.lower() in OBJETS:
            continue
        if NOMINALE.match(v) and len(v.split()) <= 3:
            continue
        a8.append((f"{l['ancrage']}|{l['categorie']}", v))
    print(f"A8 — {len(a8)} vedette(s) hors forme, signalement")
    for cle, v in a8:
        print(f"    {cle} — « {v} »")

    echecs = len(a1) + len(a2) + len(a4) + len(a7)
    print(f"{echecs} échec(s), "
          f"{len(a3) + len(a5) + len(a6) + len(a8)} signalement(s)")
    return 1 if echecs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
