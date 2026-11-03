"""Verse les amendements du 20261103 : une fiche par amendement (cartouche, texte,
bloc [interne] avec la preuve par réapplication), et l'ajout aux liasses P1 et PLFSS."""
import re, sys, json, gzip, functools
sys.path.insert(0, '/home/user/Resolution-2027/chantier/appareil/tri_porte')
sys.path.insert(0, '/home/user/Resolution-2027')
import droit
from amendements import AM
from extraire_visas import ART_RE, deplier, cle, _lt

D = '/home/user/Resolution-2027/chantier/livrables/depot_2027/'
J = '2027-07-01'
NB = ' '


def typo(s):
    s = s.replace("'", '’')
    s = re.sub(r' ([:;!?»%])', NB + r'\1', s)
    s = re.sub(r'« ', '«' + NB, s)
    s = re.sub(r'(\d) (\d{3})\b', r'\1' + NB + r'\2', s)
    return s


CODES = [('code général des impôts', 'cgi'), ('code des impositions sur les biens et services', 'cibs'),
         ('code général des collectivités territoriales', 'cgct'), ('code de l’urbanisme', 'urbanisme'),
         ('code de la santé publique', 'sante'), ('code de la sécurité sociale', 'css'), ('code du travail', 'travail'),
         ('code général de la fonction publique', 'cgfp'), ('code rural et de la pêche maritime', 'rural'),
         ('code des transports', 'transports'), ('code de l’environnement', 'environnement')]


def preuve(disp):
    """Réapplique chaque abrogation sur le dépôt LEGI au 1er juillet 2027 : l'article
    existe, et la section qui le porte. Les textes absents du dépôt sont déclarés."""
    lignes = []
    courant = None
    for al in disp.split('\n'):
        st = al.strip()
        if not re.match(r'^\d+°', st):
            continue
        code = None
        for nom, court in CODES:
            if nom in st:
                code = court
        if 'même code' in st:
            code = courant
        if code is None:
            lignes.append(('—', st[:90], 'texte absent du dépôt de droit : non réappliqué', ''))
            continue
        courant = code
        corps = st.split(' du code')[0].split(' du même')[0]
        sous = bool(re.match(r'^\d+°\s+(?:Le|Les|La)\s+(?:[IVX]+|\d+°(?: ter)?|deuxième)', st))
        spans = [(m.group(0).strip(), m.start(), m.end()) for m in ART_RE.finditer(corps)]
        spans = [s for s in spans if not re.fullmatch(r'\d{1,2}', s[0])]
        k = 0
        arts = []
        while k < len(spans):
            a = spans[k][0]
            if k + 1 < len(spans) and re.match(r'\s*à\s*$', corps[spans[k][2]:spans[k + 1][1]]):
                b = spans[k + 1][0]
                ex, how = deplier(code, a, b)
                arts.append((f'{a} à {b}', ex))
                k += 2
            else:
                arts.append((a, [a]))
                k += 1
        for lib, ex in arts:
            secs = set(); manq = []
            for x in ex:
                try:
                    v = droit.article(code, x, jour=J)
                    secs.add(v['section'].split(' > ')[-1][:70])
                except Exception:
                    manq.append(x)
            etat = f'{len(ex) - len(manq)} art. applicables au {J}' + (f' ; absents : {", ".join(manq)}' if manq else '')
            if sous:
                etat += ' ; subdivision seule abrogée'
            lignes.append((code, lib, etat, ' · '.join(sorted(secs))))
    return lignes


def fiche(a):
    pr = preuve(a['dispositif'])
    t = [f"# {a['titre']}", '',
         '> **PROJET — versé le 20261103, non validé par l’auteur. Ne pas déposer en l’état.**', '',
         '| cartouche | |', '|---|---|',
         f"| titre | {a['titre']} |",
         f"| véhicule | {'PLF 2027, première partie' if a['liasse']=='P1' else 'PLFSS 2027'}, {a['vise']} |",
         f"| rangs du tri portés | {', '.join(str(r) for r in a['rangs'])} |",
         f"| gage | {a['gage']} |",
         f"| rattachement | {a['lolf']} |",
         '| cartes de la carto | aucune : la carto (état du 20260924) ne porte pas de carte pour la refonte des prélèvements |',
         '', '---', '', 'AMENDEMENT', '', 'présenté par', '', '----------', '', a['entete'], '', a['dispositif'], '',
         'EXPOSÉ SOMMAIRE', '', a['expose'], '', '---', '', '## [interne]', '',
         '### Preuve par réapplication — dépôt de droit, millésime LEGI 20261031, version applicable au 1er juillet 2027', '',
         '| code | visa | réapplication | sections atteintes |', '|---|---|---|---|']
    for c, l, e, s in pr:
        t.append(f'| {c} | {l} | {e} | {s} |')
    t += ['', 'Provenance : visas **relevés** au dépôt de droit par `droit.py` le 20261103 ; les textes absents du dépôt '
          '(code forestier, code minier, lois non codifiées hors dépôt) sont cités sur la référence juridique de '
          'l’annexe des ressources affectées et **restent à relire** avant dépôt.', '']
    return typo('\n'.join(t)), pr


def bloc_liasse(a):
    return typo('\n'.join([f"## Amendement n° {a['n']} [{a['objet']}]", '', 'AMENDEMENT', '', 'présenté par', '',
                           '----------', '', a['entete'], '', a['dispositif'], '', 'EXPOSÉ SOMMAIRE', '', a['expose'],
                           '', '---', '']))


if __name__ == '__main__':
    rapport = {}
    for a in AM:
        txt, pr = fiche(a)
        open(D + a['fichier'], 'w', encoding='utf-8').write(txt)
        rapport[f"{a['liasse']} n° {a['n']}"] = pr
    # liasse P1
    p1 = open(D + 'LIASSE_PLF_P1.md', encoding='utf-8').read()
    if '## Amendement n° 35 [' not in p1:
        som = ['', '## Lot VI : Prélèvements remplacés ou fondus', '', '| n° | article visé | objet |', '|---|---|---|']
        for a in AM:
            if a['liasse'] == 'P1':
                som.append(f"| {a['n']} | {a['vise']} | {a['objet']} |")
        p1 = p1.replace('Trente-quatre amendements de première partie, répartis en cinq lots. La numérotation va de 1 à 34.',
                        'Trente-huit amendements de première partie, répartis en six lots. La numérotation va de 1 à 38.')
        i = p1.index('\n---\n\n## Amendement n° 1 [')
        p1 = p1[:i] + typo('\n'.join(som)) + '\n' + p1[i:]
        p1 = p1.rstrip('\n') + '\n\n---\n\n' + '\n'.join(bloc_liasse(a) for a in AM if a['liasse'] == 'P1')
        open(D + 'LIASSE_PLF_P1.md', 'w', encoding='utf-8').write(p1)
    ss = open(D + 'LIASSE_PLFSS.md', encoding='utf-8').read()
    if '## Amendement n° 9 [' not in ss:
        a9 = [a for a in AM if a['liasse'] == 'SS'][0]
        ss = ss.replace('La présente liasse compte huit amendements.', 'La présente liasse compte neuf amendements.')
        ligne8 = [l for l in ss.split('\n') if l.startswith('| 8 |')][0]
        ss = ss.replace(ligne8, ligne8 + '\n' + typo(f"| 9 | Article additionnel après l’article 14 | {a9['objet']} |"))
        ss = ss.rstrip('\n') + '\n\n---\n\n' + bloc_liasse(a9)
        open(D + 'LIASSE_PLFSS.md', 'w', encoding='utf-8').write(ss)
    json.dump(rapport, open('/home/user/Resolution-2027/chantier/appareil/tri_porte/preuves.json', 'w'), ensure_ascii=False, indent=1)
    for k, v in rapport.items():
        print(k)
        for l in v:
            print('   ', l)
