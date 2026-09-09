# -*- coding: utf-8 -*-
"""Relevé d'écarts entre une épreuve d'imprimeur et le manuscrit du coffre.

Comparaison texte contre texte, à l'octet près sur les chaînes normalisées a
minima : rien ne se lit à l'œil, rien ne se corrige, rien ne se réécrit. Le
script rend un écart par ligne — page d'épreuve, ancre au manuscrit, les deux
versions, une classe — et il ne tranche aucun écart de fond.

Trois flux se comparent séparément, parce que l'épreuve les range autrement que
le manuscrit :

  corps     le texte courant, du prologue à la postface
  notes     les notes de fin, appariées par numéro d'appel
  paratexte ce que l'épreuve porte et que le manuscrit n'a pas — table des
            matières, annexes, page de titre — qui se compte et ne se détaille
            pas

Usage : python3 relever_ecarts_epreuve.py <manuscrit.html> <epreuve.txt>
                                          <bornes.json> <sortie.json>
"""
import difflib
import html
import json
import re
import sys
import unicodedata

# ---------------------------------------------------------------- normalisation

ESPACES = {
    ' ': ' ', ' ': ' ', ' ': ' ', ' ': ' ',
    ' ': ' ', ' ': ' ', ' ': ' ', ' ': ' ',
    ' ': ' ', ' ': ' ', '\t': ' ', '​': '',
    '﻿': '', '­': '',
}


def normaliser(t):
    """Espaces unifiés, ligatures dépliées, rien d'autre : la casse, les
    accents et la ponctuation restent tels quels — ce sont eux qu'on relève."""
    for a, b in ESPACES.items():
        t = t.replace(a, b)
    t = t.replace('ﬁ', 'fi').replace('ﬂ', 'fl')
    t = unicodedata.normalize('NFC', t)
    return re.sub(r' +', ' ', t).strip()


# ------------------------------------------------------------------- manuscrit

BALISE = re.compile(r'<[^>]+>')
APPEL = re.compile(
    r'<sup class="appel-note"[^>]*>\s*<a[^>]*>(\d+)</a>\s*</sup>')
BLOC = re.compile(
    r'<(h1|h2|h3|p|footer|li)\b([^>]*)>(.*?)</\1>', re.S)
ID = re.compile(r'id="([^"]+)"')
CLASSE = re.compile(r'class="([^"]+)"')


def blocs_manuscrit(chemin):
    """Les blocs du manuscrit, dans l'ordre du document.

    Chaque bloc porte son rang, sa nature, l'ancre de section qui le précède,
    et son texte — les appels de note y deviennent des jetons ⟦n⟧."""
    src = open(chemin, encoding='utf-8').read()
    src = APPEL.sub(r'⟦\1⟧', src)
    # L'ancre courante : le dernier id="…" rencontré avant le bloc.
    ancres = [(m.start(), m.group(1)) for m in ID.finditer(src)]
    out = []
    for m in BLOC.finditer(src):
        nature, attrs, corps = m.group(1), m.group(2), m.group(3)
        cls = CLASSE.search(attrs)
        cls = cls.group(1) if cls else ''
        texte = normaliser(html.unescape(BALISE.sub('', corps)))
        if not texte:
            continue
        ancre = ''
        for pos, val in ancres:
            if pos < m.start():
                ancre = val
            else:
                break
        if nature == 'li' and 'note' in cls:
            flux = 'notes'
        elif ancre in ('ouvrage', 'X-C0-etat-partout',
                       'X-C0-justice-nulle-part') or ancre == 'notes':
            # Page de titre, faux titres et intitulé du cahier de notes : le
            # liminaire de l'épreuve se compte, il ne se compare pas.
            flux = 'liminaire'
        else:
            flux = 'corps'
        out.append({'rang': len(out), 'nature': nature, 'classe': cls,
                    'ancre': ancre, 'texte': texte, 'flux': flux})
    return out


def notes_manuscrit(blocs):
    """numéro d'appel → texte de la note, relevé de l'ordre des <li>."""
    notes, n = {}, 0
    for b in blocs:
        if b['flux'] != 'notes':
            continue
        n += 1
        texte = re.sub(r'\s*↩\s*$', '', b['texte']).strip()
        notes[n] = texte
    return notes


# --------------------------------------------------------------------- épreuve

PIED = re.compile(
    r'^488686WXT[^\n]*$|^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}$', re.M)


def pages_epreuve(chemin):
    """Les pages de l'épreuve, pied d'imprimeur et folio retirés."""
    brut = open(chemin, encoding='utf-8').read().split('\f')
    pages = []
    for i, p in enumerate(brut, 1):
        p = PIED.sub('', p)
        lignes = [normaliser(l) for l in p.split('\n')]
        # Le folio : une ligne qui ne porte que le numéro de la page.
        lignes = [l for l in lignes
                  if l and not re.fullmatch(rf'{i}', l)]
        pages.append(lignes)
    return pages


LABEL = re.compile(
    r'^(PROLOGUE|POSTFACE|ANNEXES|TABLE DES MATIÈRES|PARTIE [IVX]+|\d{1,2})$')


def jetons_corps(pages, borne_min, borne_max, paratexte=None):
    """Le corps de l'épreuve en jetons, chacun étiqueté de sa page.

    Les appels de note se détachent du mot auquel la composition les colle, et
    ne sont retenus que s'ils continuent la suite croissante des appels — ce qui
    écarte les faux positifs du type « m2 » ou « xixe ».

    Les intitulés de rang que l'épreuve ajoute — « PARTIE I », le numéro de
    chapitre en tête de page — ne se comparent pas : ils se comptent comme
    `forme`, dans `paratexte`."""
    brut = []
    for num in range(borne_min, borne_max + 1):
        for ligne in pages[num - 1]:
            if LABEL.fullmatch(ligne):
                if paratexte is not None:
                    paratexte.append({'page': num, 'intitule': ligne})
                continue
            for mot in ligne.split(' '):
                if mot:
                    brut.append([mot, num])

    COLLE = re.compile(r'^(.*\D)(\d{1,3})([^\w]*)$')
    SEUL = re.compile(r'^(\d{1,3})([^\w]*)$')

    # Premier passage : les appels collés au mot, dans l'ordre croissant. Un
    # numéro qui n'y est pas laisse un trou, comblé au second passage.
    place = {}
    suivant = 1
    for k, (mot, _num) in enumerate(brut):
        m = COLLE.match(mot)
        if not m:
            continue
        n = int(m.group(2))
        if suivant <= n <= suivant + 3:
            place[n] = (k, m.group(1), m.group(3))
            suivant = n + 1

    # Second passage : chaque numéro manquant se cherche seul, entre les deux
    # appels qui l'encadrent — la composition l'a détaché de son mot.
    connus = sorted(place)
    for n in range(1, (connus[-1] if connus else 0) + 1):
        if n in place:
            continue
        avant = max([place[k][0] for k in place if k < n] or [-1])
        apres = min([place[k][0] for k in place if k > n] or [len(brut)])
        for k in range(avant + 1, apres):
            m = SEUL.match(brut[k][0])
            if m and int(m.group(1)) == n:
                place[n] = (k, '', m.group(2))
                break

    par_indice = {k: (n, pref, suff) for n, (k, pref, suff) in place.items()}
    jetons = []
    for k, (mot, num) in enumerate(brut):
        if k in par_indice:
            n, pref, suff = par_indice[k]
            if pref:
                jetons.append((pref, num))
            jetons.append((f'⟦{n}⟧', num))
            if suff:
                jetons.append((suff, num))
        else:
            jetons.append((mot, num))
    return jetons


def notes_epreuve(pages, borne_min, borne_max):
    """numéro → texte, relevé du cahier de notes de l'épreuve."""
    flux = []
    for num in range(borne_min, borne_max + 1):
        flux.extend(pages[num - 1])
    texte = ' '.join(l for l in flux if l and l != 'Notes')
    # Chaque note s'ouvre sur son numéro, en début de ligne à la composition ;
    # après le recollement, le numéro suit la fin de la note précédente.
    bornes = [(int(m.group(1)), m.start(), m.end())
              for m in re.finditer(r'(?:^| )(\d{1,3}) (?=[A-ZÀ-ÿ«h(])', texte)]
    retenues, suivant = [], 1
    for num, deb, fin in bornes:
        if num == suivant:
            retenues.append((num, deb, fin))
            suivant += 1
    notes = {}
    for i, (num, deb, fin) in enumerate(retenues):
        stop = retenues[i + 1][1] if i + 1 < len(retenues) else len(texte)
        notes[num] = normaliser(texte[fin:stop])
    return notes


# ------------------------------------------------------------------ comparaison

MOT = re.compile(r"[\w’'-]+|[^\w\s]", re.UNICODE)
APPEL_JETON = re.compile(r'⟦\s*\d+\s*⟧')
# Une césure de composition se recolle : le mot coupé se compare entier.
CHIFFRE = re.compile(r'\d[\d  ]*')


def mots(texte):
    return MOT.findall(texte)


def depouille(s):
    """La chaîne réduite à ses lettres et chiffres, sans casse ni accent."""
    s = APPEL_JETON.sub('', s)
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^0-9a-z]', '', s)


def chiffres(s):
    return sorted(c.replace(' ', '').replace(' ', '').strip()
                  for c in CHIFFRE.findall(APPEL_JETON.sub('', s)))


def classer(avant, apres):
    """La classe d'un écart, par critère mécanique et sans juger du sens.

    - `fond` dès qu'un chiffre bouge, ou que la rédaction change au-delà de la
      typographie : le sens *peut* changer, et c'est à l'auteur de trancher ;
    - `perte` quand un côté est vide de texte ;
    - `coquille` quand seuls la casse, les accents, la ponctuation, un appel de
      note ou une lettre d'accord diffèrent.

    `forme` ne sort pas d'ici : il se compte sur le paratexte et les natures de
    bloc, jamais sur une chaîne de texte.
    """
    if chiffres(avant) != chiffres(apres):
        return 'fond'
    da, db = depouille(avant), depouille(apres)
    if da == db:
        return 'coquille'
    if not da and not db:
        # Ni d'un côté ni de l'autre autre chose que de la ponctuation ou un
        # appel de note : c'est une coquille, pas une perte de texte.
        return 'coquille'
    if not da or not db:
        return 'perte'
    # Un mot contre un mot, à une ou deux lettres près : accord ou coquille.
    if (len(mots(APPEL_JETON.sub('', avant))) <= 2
            and len(mots(APPEL_JETON.sub('', apres))) <= 2
            and difflib.SequenceMatcher(None, da, db).ratio() >= 0.8):
        return 'coquille'
    return 'fond'


def grouper(opcodes, ecart_max=2):
    """Regroupe les opérations voisines séparées par au plus `ecart_max` mots
    identiques : une même retouche de phrase se relève d'un bloc, non éclatée
    en huit micro-écarts."""
    groupes, courant = [], None
    for op, i1, i2, j1, j2 in opcodes:
        if op == 'equal':
            if courant and (i2 - i1) > ecart_max:
                groupes.append(courant)
                courant = None
            continue
        if courant is None:
            courant = [i1, i2, j1, j2]
        else:
            courant[1], courant[3] = i2, j2
    if courant:
        groupes.append(courant)
    return groupes


def apparier_notes(m_notes, e_notes):
    """Apparie les notes des deux côtés par alignement global de leurs textes.

    Une note insérée ou retirée décale toute la numérotation qui suit : la
    correspondance ne peut donc pas se faire par numéro. Elle se fait sur la
    ressemblance des textes, par un alignement qui n'inverse jamais l'ordre —
    l'ordre des notes est celui du livre, des deux côtés.
    """
    A = [m_notes[k] for k in sorted(m_notes)]
    B = [e_notes[k] for k in sorted(e_notes)]
    ia = sorted(m_notes)
    ib = sorted(e_notes)
    na, nb = len(A), len(B)
    da = [depouille(x)[:400] for x in A]
    db = [depouille(x)[:400] for x in B]

    def sim(i, j):
        return difflib.SequenceMatcher(None, da[i], db[j]).ratio()

    TROU = -0.35
    # Needleman-Wunsch : score d'appariement = ressemblance - 0,5, de sorte
    # qu'apparier deux notes étrangères coûte plus qu'un trou de chaque côté.
    S = [[0.0] * (nb + 1) for _ in range(na + 1)]
    D = [[0] * (nb + 1) for _ in range(na + 1)]  # 1 diagonale, 2 haut, 3 gauche
    for i in range(1, na + 1):
        S[i][0] = S[i - 1][0] + TROU
        D[i][0] = 2
    for j in range(1, nb + 1):
        S[0][j] = S[0][j - 1] + TROU
        D[0][j] = 3
    for i in range(1, na + 1):
        for j in range(1, nb + 1):
            cand = ((S[i - 1][j - 1] + sim(i - 1, j - 1) - 0.5, 1),
                    (S[i - 1][j] + TROU, 2),
                    (S[i][j - 1] + TROU, 3))
            S[i][j], D[i][j] = max(cand)
    i, j, paires = na, nb, []
    while i > 0 and j > 0:
        d = D[i][j]
        if d == 1:
            paires.append((ia[i - 1], ib[j - 1]))
            i, j = i - 1, j - 1
        elif d == 2:
            paires.append((ia[i - 1], None))
            i -= 1
        else:
            paires.append((None, ib[j - 1]))
            j -= 1
    while i > 0:
        paires.append((ia[i - 1], None))
        i -= 1
    while j > 0:
        paires.append((None, ib[j - 1]))
        j -= 1
    paires.reverse()

    # Deux orphelines voisines et de côtés opposés sont une même note réécrite
    # au-delà du seuil de ressemblance, non une note perdue suivie d'une note
    # ajoutée. Elles se recollent — ce qui laisse seules les vraies insertions
    # et les vraies suppressions.
    fusion, k = [], 0
    while k < len(paires):
        a, b = paires[k]
        if k + 1 < len(paires):
            c, d = paires[k + 1]
            if a is not None and b is None and c is None and d is not None:
                fusion.append((a, d))
                k += 2
                continue
            if a is None and b is not None and c is not None and d is None:
                fusion.append((c, b))
                k += 2
                continue
        fusion.append((a, b))
        k += 1
    return fusion


def ecarts_corps(blocs, jetons, renum=None):
    """Les écarts du corps, ancrés au manuscrit et paginés à l'épreuve.

    Les appels de note se comparent comme un jeton neutre : leur numéro se
    décale dès qu'une note est insérée en amont, et ce décalage se relève une
    fois pour toutes au flux des notes, non à chaque appel."""
    m_mots, m_src = [], []
    for b in blocs:
        if b['flux'] != 'corps':
            continue
        for w in mots(b['texte']):
            m_mots.append(w)
            m_src.append(b)
    e_mots, e_page = [], []
    for jeton, page in jetons:
        for w in mots(jeton):
            e_mots.append(w)
            e_page.append(page)

    # Le numéro d'appel se neutralise pour l'alignement, et se remet ensuite.
    def masquer(suite):
        out, i = [], 0
        while i < len(suite):
            if (suite[i] == '⟦' and i + 2 < len(suite)
                    and suite[i + 2] == '⟧'):
                out.append('⟦APPEL⟧')
                out.append('⟦APPEL⟧')
                out.append('⟦APPEL⟧')
                i += 3
            else:
                out.append(suite[i])
                i += 1
        return out

    m_cle, e_cle = masquer(m_mots), masquer(e_mots)
    cmp = difflib.SequenceMatcher(None, m_cle, e_cle, autojunk=False)
    out = []
    for i1, i2, j1, j2 in grouper(cmp.get_opcodes()):
        avant = ' '.join(m_mots[i1:i2])
        apres = ' '.join(e_mots[j1:j2])
        bloc = m_src[min(i1, len(m_src) - 1)] if m_src else None
        page = e_page[min(j1, len(e_page) - 1)] if e_page else None
        out.append({
            'flux': 'corps',
            'page': page,
            'ancre': bloc['ancre'] if bloc else '',
            'nature': bloc['nature'] if bloc else '',
            'manuscrit': avant,
            'epreuve': apres,
            'avant': ' '.join(m_mots[max(0, i1 - 8):i1]),
            'apres': ' '.join(m_mots[i2:i2 + 8]),
            'classe': classer(avant, apres),
            'mots_manuscrit': i2 - i1,
            'mots_epreuve': j2 - j1,
        })
    return out


def ecarts_notes(m_notes, e_notes, pages, borne_min, borne_max, paires):
    """Les écarts des notes, sur l'appariement rendu par `apparier_notes`."""
    page_de = {}
    for num in range(borne_min, borne_max + 1):
        for l in pages[num - 1]:
            for m in re.finditer(r'(?:^| )(\d{1,3}) (?=[A-ZÀ-ÿ«h(])', l):
                page_de.setdefault(int(m.group(1)), num)
    out, renumerotees = [], []
    for na, nb in paires:
        a = m_notes.get(na, '') if na else ''
        b = e_notes.get(nb, '') if nb else ''
        ancre = (f'note-e{na}' if na else '—') + (
            f' → épreuve n° {nb}' if nb and nb != na else '')
        if na and nb and na != nb:
            renumerotees.append({'manuscrit': na, 'epreuve': nb})
        if a == b:
            continue
        if not a or not b:
            out.append({'flux': 'notes', 'page': page_de.get(nb) if nb else None,
                        'ancre': ancre, 'nature': 'note',
                        'manuscrit': a, 'epreuve': b, 'avant': '', 'apres': '',
                        'classe': 'perte',
                        'mots_manuscrit': len(mots(a)),
                        'mots_epreuve': len(mots(b))})
            continue
        ma, mb = mots(a), mots(b)
        cmp = difflib.SequenceMatcher(None, ma, mb, autojunk=False)
        for i1, i2, j1, j2 in grouper(cmp.get_opcodes()):
            avant, apres = ' '.join(ma[i1:i2]), ' '.join(mb[j1:j2])
            out.append({
                'flux': 'notes', 'page': page_de.get(nb),
                'ancre': ancre, 'nature': 'note',
                'manuscrit': avant, 'epreuve': apres,
                'avant': ' '.join(ma[max(0, i1 - 8):i1]),
                'apres': ' '.join(ma[i2:i2 + 8]),
                'classe': classer(avant, apres),
                'mots_manuscrit': i2 - i1, 'mots_epreuve': j2 - j1,
            })
    return out, renumerotees


def recoller_appels(ecarts):
    """Un appel de note déplacé se relève une fois, non deux.

    Le diff rend le retrait d'un côté et l'ajout de l'autre : les deux se
    reconnaissent à ce qu'ils ne portent qu'un jeton d'appel, et au même
    numéro."""
    SEUL_APPEL = re.compile(r'^⟦ ?(\d+) ?⟧$')
    retraits = {}
    for e in ecarts:
        m = SEUL_APPEL.match(e['manuscrit'].strip())
        if m and not e['epreuve'].strip():
            retraits.setdefault(int(m.group(1)), []).append(e)
    fusionnes, morts = [], set()
    for e in ecarts:
        m = SEUL_APPEL.match(e['epreuve'].strip())
        if m and not e['manuscrit'].strip():
            n = int(m.group(1))
            for autre in retraits.get(n, []):
                if id(autre) in morts:
                    continue
                morts.add(id(autre))
                morts.add(id(e))
                fusionnes.append({
                    **autre,
                    'page': e['page'],
                    'manuscrit': f'appel ⟦{n}⟧ après « {autre["avant"][-60:]} »',
                    'epreuve': f'appel ⟦{n}⟧ après « {e["avant"][-60:]} »',
                    'classe': 'coquille',
                    'deplacement_appel': n,
                })
                break
    return [e for e in ecarts if id(e) not in morts] + fusionnes


def main(chemin_ms, chemin_ep, chemin_bornes, chemin_sortie):
    bornes = json.load(open(chemin_bornes, encoding='utf-8'))
    blocs = blocs_manuscrit(chemin_ms)
    pages = pages_epreuve(chemin_ep)
    m_notes = notes_manuscrit(blocs)

    c1, c2 = bornes['corps']
    n1, n2 = bornes['notes']
    paratexte = []
    jetons = jetons_corps(pages, c1, c2, paratexte)
    e_notes = notes_epreuve(pages, n1, n2)

    paires = apparier_notes(m_notes, e_notes)
    ec_notes, renumerotees = ecarts_notes(
        m_notes, e_notes, pages, n1, n2, paires)
    ecarts = ecarts_corps(blocs, jetons) + ec_notes

    # Un appel de note déplacé sort en deux temps du diff — le retrait d'un
    # côté, l'ajout de l'autre. Il se recolle en un seul écart.
    ecarts = recoller_appels(ecarts)

    # `forme` — ce que l'épreuve ajoute hors du texte comparé. Se compte.
    forme = {
        'notes_renumerotees': len(renumerotees),
        'intitules_de_rang': len(paratexte),
        'pages_liminaires': bornes['liminaires'][1] - bornes['liminaires'][0] + 1,
        'pages_blanches_ou_faux_titres': len(
            bornes.get('blanches_ou_faux_titres', [])),
        'pages_annexes': bornes['annexes'][1] - bornes['annexes'][0] + 1,
        'pages_table_des_matieres': (bornes['table'][1] - bornes['table'][0] + 1),
        'blocs_liminaires_du_manuscrit_non_compares': sum(
            1 for b in blocs if b['flux'] == 'liminaire'),
    }

    comptes = {'forme': sum(forme.values())}
    for e in ecarts:
        comptes[e['classe']] = comptes.get(e['classe'], 0) + 1
    releve = {
        'epreuve': chemin_ep,
        'manuscrit': chemin_ms,
        'bornes': bornes,
        'comptes': dict(sorted(comptes.items())),
        'total': len(ecarts) + comptes['forme'],
        'forme': forme,
        'paratexte': paratexte,
        'notes_renumerotees': renumerotees,
        'appariement_notes': [{'manuscrit': a, 'epreuve': b}
                              for a, b in paires],
        'notes_manuscrit': len(m_notes),
        'notes_epreuve': len(e_notes),
        'ecarts': ecarts,
    }
    json.dump(releve, open(chemin_sortie, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f'{chemin_sortie} — {len(ecarts)} écart(s) : '
          + ', '.join(f'{k} {v}' for k, v in releve['comptes'].items()))
    print(f'  notes : {len(m_notes)} au manuscrit, {len(e_notes)} à l\'épreuve')
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:5]))
