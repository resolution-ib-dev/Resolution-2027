# -*- coding: utf-8 -*-
"""Confrontation d'un résumé de texte financier à la pièce qui fait foi.

Le résumé du lot A affirme des valeurs et donne, pour chacune, un repère : la
pièce, l'article, l'emplacement — hors-alinéa, alinéa numéroté, tableau — et la
page. Ce module rouvre la pièce **au repère** et rend l'un des quatre verdicts,
jamais un cinquième :

    concorde     la pièce, rouverte au repère, porte la valeur
    diverge      elle en porte une autre — les deux s'affichent
    introuvable  le repère ne résout pas dans la pièce
    non sourcé   aucun repère n'a été donné

Deux chiffres sortent, jamais un seul : le taux de concordance sur les valeurs
confrontables, et le compte des non sourcés.

**Ce module ne lit aucun fichier que son propre générateur vient d'écrire.** Il
lit le résumé, écrit par un autre fil et gelé, et les pièces — les deux
référentiels de rédaction, qui viennent du dépôt, les deux tables d'articles
ouverts et les trois classeurs, qui sont des pièces jointes du projet. La table
de repères qu'il verse est une sortie de la même passe, tenue en mémoire pendant
la résolution : aucun verdict ne se lit d'un fichier.

**Deux formes d'opération**, selon la pièce, et le mode est porté par chaque
ligne de la table :

* `lecture` — la pièce est un texte. Le repère se rouvre, et la valeur s'y
  cherche. L'extraction des couples (valeur, repère) est mécanique : elle lit les
  tableaux markdown du résumé sous leur ligne `*Source :*`, les en-têtes de
  colonne qui portent leur propre repère, et les valeurs de prose qui portent un
  repère entre parenthèses. Rien n'est transcrit à la main.
* `reapplication` — la pièce est une structure, et le résumé en affirme un
  agrégat. L'opération se rejoue sur la structure et doit redonner le résultat.
  Une réapplication demande une recette : elle est déclarée ici, nommée et
  motivée, jamais devinée. Un agrégat dont le résumé ne déclare pas la recette
  sort `introuvable`, motif à l'appui — on ne comble pas.

**Ce qui ne se confronte pas sort nommé et n'entre dans aucun taux** : le bloc
L4, qui est un jugement sur nos positions ; le compte par bloc, les emplacements
non relevés et les difficultés de lecture, qui sont la description que le
livrable fait de lui-même.

Usage : python3 appareil/confronter_lecture.py [--racine .]
                [--resume CHEMIN] [--table CHEMIN] [--releve CHEMIN]
                [--muet]
"""
import argparse
import json
import os
import re
import sys
import unicodedata
from decimal import Decimal, InvalidOperation

# --------------------------------------------------------------------------
# Normalisation

ESPACES = '     '
MOINS = '−–—-'

# Un séparateur de milliers est **une seule** espace suivie d'exactement trois
# chiffres. La règle n'est pas cosmétique : la pièce sort de `pdftotext -layout`,
# où les colonnes sont séparées par plusieurs espaces. Traiter toute suite
# d'espaces comme un séparateur collait « 1 652   1 696 » en 16521696 et faisait
# diverger une ligne juste — la faute d'un contrôle qui invente sa propre
# lecture au lieu de lire la pièce.
_NOMBRE = re.compile(
    r'(?<![0-9A-Za-zÀ-ÿ])'
    r'(?:[' + MOINS + r']?\d{1,3}(?:[' + ESPACES + r']\d{3})+(?!\d|[,.]\d)'
    r'|[' + MOINS + r']?\d+(?:[,.]\d+)?)')


def canon(s):
    """Minuscule, sans accent, espaces réduits — pour apparier un libellé."""
    s = unicodedata.normalize('NFD', str(s))
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('’', "'").replace('‘', "'")
    s = re.sub(r'[^0-9a-zA-Z%€\'/()+.,-]+', ' ', s.lower())
    return re.sub(r'\s+', ' ', s).strip()


def nombre(txt):
    """Un jeton numérique du texte → Decimal, ou None."""
    t = str(txt).strip()
    for c in MOINS:
        t = t.replace(c, '-')
    for c in ESPACES:
        t = t.replace(c, '')
    t = t.replace(',', '.')
    if t.count('.') > 1:               # 1.234.567 n'est pas un décimal
        t = t.replace('.', '')
    if not re.fullmatch(r'-?\d+(?:\.\d+)?', t):
        return None
    try:
        return Decimal(t)
    except InvalidOperation:
        return None


def nombres(txt):
    """Tous les nombres d'une chaîne, dans l'ordre."""
    out = []
    for m in _NOMBRE.finditer(str(txt)):
        v = nombre(m.group(0))
        if v is not None:
            out.append(v)
    return out


def egal(a, b):
    """Égalité de deux grandeurs. Zéro tolérance : une valeur arrondie par le
    livrable n'est pas la valeur de la pièce, et le dire est le travail."""
    return a is not None and b is not None and a == b


# --------------------------------------------------------------------------
# Les pièces

class Redaction:
    """Un référentiel de rédaction — `redaction_plf.json` ou `_plfss.json`."""

    def __init__(self, chemin, nom):
        self.nom = nom
        self.absente = not os.path.isfile(chemin)
        self.articles = {}
        self.piece = {}
        if self.absente:
            return
        d = json.load(open(chemin, encoding='utf-8'))
        self.piece = d.get('_revision', {}).get('piece', {})
        for a in d['articles']:
            self.articles[canon(a['numero'])] = a

    def article(self, numero):
        if numero is None:
            return None
        cle = canon(numero)
        cle = re.sub(r'^art(icle)?\.?\s*', '', cle).rstrip('.')
        # « 1er » est le numéro de la pièce, « 1 » celui que le résumé écrit
        # parfois : on essaie la forme reçue avant la forme réduite, jamais
        # l'inverse, pour ne pas confondre deux articles voisins.
        for k in (cle, re.sub(r'^(\d+)(er|ere|eme|e)$', r'\1', cle),
                  cle + 'er'):
            if k in self.articles:
                return self.articles[k]
        return None

    @staticmethod
    def lignes(art, pages=None, emplacement=None):
        """Les lignes de l'article dans le périmètre du repère.

        Rend des couples (étiquette, texte), l'étiquette servant à apparier un
        libellé. Le hors-alinéa porte les tableaux ; les alinéas portent la
        prose.
        """
        out = []
        if art is None:
            return out
        veut_alinea = emplacement and emplacement.startswith('alinea')
        num_alinea = None
        if veut_alinea:
            m = re.search(r'(\d+)', emplacement)
            num_alinea = int(m.group(1)) if m else None
        for h in art.get('hors_alinea', []):
            if pages and h.get('page') not in pages:
                continue
            if veut_alinea:
                continue
            out.append(('hors-alinéa p.%s' % h.get('page'), h.get('ligne', '')))
        for al in art.get('alineas', []):
            if pages and al.get('page') not in pages:
                continue
            if num_alinea is not None and al.get('numero') != num_alinea:
                continue
            out.append(('alinéa %s p.%s' % (al.get('numero'), al.get('page')),
                        al.get('texte', '')))
        if not out and pages:
            # La page du résumé peut viser la page d'impression du tableau, que
            # la pièce rattache à l'article sans la répéter ligne à ligne. On
            # relâche la page, et la précision du verdict le dira.
            return Redaction.lignes(art, None, emplacement)
        return out


class Table:
    """Une table d'articles ouverts, au format TSV du corpus."""

    COLONNES = ('texte', 'article', 'subdivision', 'fourchette',
                'article_selon_ref_norme', 'divergence', 'articles', 'pages')

    def __init__(self, chemin, nom):
        self.nom = nom
        self.absente = not os.path.isfile(chemin)
        self.lignes = []
        if self.absente:
            return
        with open(chemin, encoding='utf-8') as f:
            for ligne in f:
                if ligne.startswith('#') or not ligne.strip():
                    continue
                champs = ligne.rstrip('\n').split('\t')
                champs += [''] * (len(self.COLONNES) - len(champs))
                self.lignes.append(dict(zip(self.COLONNES, champs)))


class Classeur:
    """Un classeur du projet, lu feuille par feuille."""

    def __init__(self, chemin, nom):
        self.nom = nom
        self.chemin = chemin
        self.absent = not os.path.isfile(chemin)
        self._feuilles = {}
        if self.absent:
            return
        import xlrd
        self._wb = xlrd.open_workbook(chemin)

    def feuille(self, nom):
        if self.absent:
            return []
        if nom not in self._feuilles:
            s = self._wb.sheet_by_name(nom)
            self._feuilles[nom] = [[s.cell_value(r, c) for c in range(s.ncols)]
                                   for r in range(s.nrows)]
        return self._feuilles[nom]


class Pieces:
    def __init__(self, racine):
        r = lambda *p: os.path.join(racine, *p)
        self.plf = Redaction(r('referentiels', 'redaction_plf.json'), 'PLF')
        self.plfss = Redaction(r('referentiels', 'redaction_plfss.json'),
                               'PLFSS')
        self.tsv_plf = Table(r('referentiels', 'articles_ouverts_plf.tsv'),
                             'articles ouverts PLF')
        self.tsv_plfss = Table(r('referentiels', 'articles_ouverts_plfss.tsv'),
                               'articles ouverts PLFSS')
        self.annexe2 = Classeur(r('sources', 'annexe2_taxes_affectees.xls'),
                                'annexe 2 — taxes affectées')
        self.annexe3 = Classeur(r('sources', 'annexe3_depenses_fiscales.xls'),
                                'annexe 3 — dépenses fiscales')
        self.etp = Classeur(r('sources', 'synthese_etp_agences.xls'),
                            'Synthèse ETP et agences')

    def redaction(self, nom):
        return {'plf': self.plf, 'plfss': self.plfss}.get(nom)


# --------------------------------------------------------------------------
# Lecture du résumé — extraction mécanique des couples (valeur, repère)

# Les sections que le livrable consacre à lui-même : compte de ses propres
# rubriques, emplacements qu'il déclare non relevés, difficultés de lecture.
# Elles ne portent aucune affirmation sur la pièce. Exemption nommée, motivée,
# et qui vit ici — jamais ajoutée à l'exécution.
SECTIONS_HORS_CONFRONTATION = (
    'le compte, par bloc',
    'les emplacements de page non relevés',
    'les difficultés de lecture — la spécification du module',
)
# Le bloc L4 est un jugement : l'écart à nos positions se lit sur une grille
# doctrinale, pas sur la pièce. Il sort nommé et n'entre dans aucun taux.
BLOCS_DE_JUGEMENT = ("l4 — l'écart à nos positions",)

_SOURCE = re.compile(r'\*Sources?\s*:\s*(.+?)\*', re.S)
_ART = re.compile(
    r'art(?:icle)?\.?\s*(liminaire|\d+\s*(?:er|ère|e|bis|ter)?)', re.I)
_ALINEA = re.compile(r'alin[ée]as?\s*(\d+)', re.I)
_PAGE = re.compile(r'\bp+\.?\s*(\d+)(?:\s*(?:à|-|–)\s*(\d+))?', re.I)
_INLINE_NU = re.compile(
    r'art(?:icle)?\.?\s*(liminaire|\d+\s*(?:er|bis|ter)?)'
    r'(?:\s*,\s*[^.;:]{0,30}?)?\s*,?\s*\bp+\.?\s*(\d+)'
    r'(?:\s*(?:-|–|à)\s*(\d+))?', re.I)
_INLINE = re.compile(
    r'\((?:[^()]*?)art(?:icle)?\.?\s*(liminaire|\d+[^,;)]*)'
    r'[^()]*?\bp+\.?\s*(\d+)(?:\s*(?:-|–|à)\s*(\d+))?[^()]*\)', re.I)


def _veh(txt):
    """Les pièces qu'une ligne de source nomme — il y en a parfois deux."""
    t = canon(txt)
    out = []
    if 'plfss' in t:
        out.append('plfss')
    if re.search(r'\bplf\b', t):
        out.append('plf')
    if 'annexe 2' in t:
        out.append('annexe2')
    if 'annexe 3' in t:
        out.append('annexe3')
    if 'synthese etp' in t or 'etp et agences' in t:
        out.append('etp')
    if 'articles ouverts plf.tsv' in t or 'articles_ouverts_plf.tsv' in txt:
        out.append('tsv_plf')
    if 'articles ouverts plfss.tsv' in t or 'articles_ouverts_plfss.tsv' in txt:
        out.append('tsv_plfss')
    return out


def parse_repere(txt):
    """Une chaîne de source → (pièces, article, emplacement, pages)."""
    piece = tuple(_veh(txt))
    ma = _ART.search(txt)
    article = ma.group(1).strip() if ma else None
    mal = _ALINEA.search(txt)
    emplacement = ('alinea:%s' % mal.group(1)) if mal else 'hors_alinea'
    pages = set()
    for mp in _PAGE.finditer(txt):
        a = int(mp.group(1))
        b = int(mp.group(2)) if mp.group(2) else a
        if b >= a and b - a < 60:
            pages.update(range(a, b + 1))
        else:
            pages.add(a)
    return piece, article, emplacement, pages or None


# Ce qui, dans une phrase, n'est pas une grandeur affirmée mais l'adresse où
# elle se lit, ou la référence d'un texte. Masqué avant tout relevé : sinon un
# numéro d'article se compterait comme une valeur, et le compte des non sourcés
# n'aurait aucun sens.
_MASQUES = (
    r'`[^`]*`',
    r'\([^()]*\bart(?:icle)?s?\.?\s*(?:liminaire|\d)[^()]*\)',
    r'\bart(?:icle)?s?\.?\s*(?:liminaire|\d+\s*(?:er|ère|bis|ter)?)',
    r'\bpp?\.?\s*\d+(?:\s*(?:-|–|à)\s*\d+)?',
    r'\bp\d{2,4}\b',
    r'\balin[ée]as?\s+\d+(?:\s*(?:et|à|,)\s*\d+)*',
    r'n[°º]\s*[\d  -]*\d',
    r'\b[LRD]\.\s*\d[\d‑–-]*(?:\s*[A-Z]+)?',
    r'\b\d+°',
    r'\b(?:19|20)\d{2}(?:\s*[-–/]\s*(?:19|20)?\d{2,4})?\b',
    r'\bD\d+-\d+-\d+\b',
    r'\btome [IVX]+\b',
    r'\bannexe \d\b',
    r'\bl(?:es|\')\s*articles?\b.*',  # « il abroge les articles 39 AH, 92 A… »
    r'\b\d{5,6}\b',            # identifiant de dépense fiscale, sans séparateur
    r'\bA-\d{2,4}\b',          # renvoi au registre des arbitrages
    r'\b20\d{6}\b',            # une date au format du corpus : 20260916
    r'\b\d{1,2}\s+(?:janvier|février|mars|avril|mai|juin|juillet|août'
    r'|septembre|octobre|novembre|décembre)\b',          # une date
    r'\bL\d(?:\.[a-e])?\b',     # nom d'un bloc du résumé : L1, L3.a…
    # Les suffixes d'article se déclinent en toutes lettres. On ne masque PAS
    # « 16,2 Md€ » : une unité n'est pas un suffixe, et l'avoir confondu avait
    # tronqué une décimale sur douze valeurs.
    r'\b\d{1,3}\s+(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies'
    r'|decies|undecies|duodecies|vicies)\b',
)
_MASQUE = re.compile('|'.join(_MASQUES), re.I)


def masquer(ligne):
    """Blanchit les adresses et les références, garde les grandeurs."""
    return _MASQUE.sub(lambda m: ' ' * len(m.group(0)), ligne)


def _cellules(ligne):
    return [c.strip() for c in ligne.strip().strip('|').split('|')]


def _propre(s):
    return re.sub(r'\s+', ' ', re.sub(r'[*`]', '', s)).strip()


def extraire_reperes(chemin_resume):
    """Le résumé → la table de repères, à plat, une ligne par valeur.

    Le résumé est lu par paragraphes, et non ligne à ligne : un repère entre
    parenthèses se trouve souvent sur la ligne suivante de la valeur qu'il
    adresse, et le couper aurait fabriqué des introuvables qui n'en sont pas.
    """
    texte = open(chemin_resume, encoding='utf-8').read()
    lignes = texte.split('\n')
    reperes, n = [], 0
    bloc = section = ''
    src = ((), None, 'hors_alinea', None)
    i = 0

    def ajoute(**kw):
        nonlocal n
        n += 1
        d = dict(id='V%03d' % n, bloc=bloc, mode='lecture', colonne='')
        d.update(kw)
        reperes.append(d)

    while i < len(lignes):
        ligne = lignes[i]

        titre = re.match(r'^(#{2,4})\s+(.*)$', ligne)
        if titre:
            intitule = _propre(titre.group(2))
            if titre.group(1) == '##':
                section = bloc = intitule
                src = ((), None, 'hors_alinea', None)
            else:
                bloc = intitule
                # Un sous-bloc hérite de la pièce de son bloc, jamais de son
                # emplacement : « L1.e » lit la même pièce que « L1.d », à un
                # autre article, et ses en-têtes de colonne portent le leur.
                src = (src[0], None, 'hors_alinea', None)
            i += 1
            continue

        hors = canon(section) in [canon(s) for s in SECTIONS_HORS_CONFRONTATION]
        jugement = canon(section) in [canon(b) for b in BLOCS_DE_JUGEMENT]
        if hors or jugement:
            i += 1
            continue

        # --- une ligne de source ouvre un périmètre, qui vaut jusqu'au titre
        # suivant. Elle peut courir sur plusieurs lignes : on les consomme.
        if '*Source' in ligne:
            bout, j = ligne, i
            while '*' not in bout.split('*Source', 1)[1] and j + 1 < len(lignes):
                j += 1
                bout += ' ' + lignes[j]
            m = _SOURCE.search(bout)
            suite = ''
            if m:
                src = parse_repere(m.group(1))
                suite = bout[m.end():]
            i = j + 1
            # Une ligne de source peut être suivie, sur la même ligne, du début
            # de la phrase qu'elle adresse. On la traite, sans jamais réinjecter
            # la ligne dans le flux — ce qui bouclerait.
            if suite.strip() and '*Source' not in suite:
                for seg in _segments(suite):
                    mi = _INLINE.search(seg)
                    r = src
                    corps = seg
                    if mi:
                        r2 = parse_repere(mi.group(0))
                        r = r2 if r2[0] else (src[0], r2[1], r2[2], r2[3])
                        corps = seg[:mi.start()] + seg[mi.end():]
                    for v in nombres(masquer(corps)):
                        ajoute(piece=r[0], article=r[1], emplacement=r[2],
                               pages=r[3], libelle=_propre(seg)[:160],
                               valeur=v, brut=_propre(seg)[:160])
            continue

        # --- tableau markdown
        if ligne.lstrip().startswith('|') and i + 1 < len(lignes) \
                and re.match(r'^\s*\|[\s:|-]+\|\s*$', lignes[i + 1]):
            entetes = _cellules(ligne)
            rep_col = {}
            for k, e in enumerate(entetes):
                if '(' in e:
                    mi = _INLINE.search('(' + e.split('(', 1)[-1])
                    if mi:
                        rep_col[k] = parse_repere(e)
            i += 2
            while i < len(lignes) and lignes[i].lstrip().startswith('|'):
                cel = _cellules(lignes[i])
                libelle = _propre(cel[0]) if cel else ''
                for k in range(1, len(cel)):
                    v = nombre(_propre(cel[k]))
                    if v is None:
                        continue
                    r = rep_col.get(k)
                    if r and not r[0]:
                        r = (src[0], r[1], r[2], r[3])
                    r = r or src
                    ajoute(piece=r[0], article=r[1], emplacement=r[2],
                           pages=r[3], libelle=libelle,
                           colonne=_propre(entetes[k]) if k < len(entetes)
                           else '', valeur=v, brut=_propre(cel[k]))
                i += 1
            continue

        if not ligne.strip():
            i += 1
            continue

        # --- prose : on assemble le paragraphe, puis on le découpe en segments
        para, j = [ligne], i
        while j + 1 < len(lignes) and lignes[j + 1].strip() \
                and not lignes[j + 1].lstrip().startswith('|') \
                and not re.match(r'^#{2,4}\s', lignes[j + 1]) \
                and '*Source' not in lignes[j + 1]:
            j += 1
            para.append(lignes[j])
        i = j + 1
        bloc_texte = ' '.join(para)

        local = None
        for seg in _segments(bloc_texte):
            mi = _INLINE.search(seg) or _INLINE_NU.search(seg)
            if mi:
                r = parse_repere(mi.group(0))
                if not r[0]:
                    r = ((local or src)[0], r[1], r[2], r[3])
                local = r          # le repère vaut pour la suite du paragraphe
                corps = seg[:mi.start()] + seg[mi.end():]
            else:
                mal = re.match(r'\s*Alin[ée]as?\s+(\d+)\s*[,:]', seg)
                base = local or src
                if mal and base[0]:
                    r = (base[0], base[1], 'alinea:%s' % mal.group(1), base[3])
                else:
                    r = base
                corps = seg
            for v in nombres(masquer(corps)):
                ajoute(piece=r[0], article=r[1], emplacement=r[2], pages=r[3],
                       libelle=_propre(seg)[:160], valeur=v,
                       brut=_propre(seg)[:160])
    return reperes


def _segments(texte):
    """Un paragraphe → les phrases porteuses d'une valeur.

    On coupe aux points-virgules et aux puces, qui sont la ponctuation dont ce
    résumé se sert pour énumérer une valeur par adresse.
    """
    t = re.sub(r'\s+', ' ', texte).strip()
    t = re.sub(r'\s-\s(?=[a-zà-ÿ*])', ' ;§ ', t)
    bouts = []
    for a in re.split(r'\s*;§\s*|\s*;\s*', t):
        for b in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Þ*])', a):
            if b.strip():
                bouts.append(b.strip())
    return bouts



def valeurs_non_sourcees(chemin_resume, reperes):
    """Les grandeurs que le livrable affirme sans donner de repère.

    Sans repère, une valeur n'est pas fausse : elle est non confrontable. Elle
    se compte à part et ne se noie pas dans le taux.
    """
    texte = open(chemin_resume, encoding='utf-8').read()
    lignes = texte.split('\n')
    prises = {}
    for r in reperes:
        prises.setdefault(r['bloc'], set()).add(r['valeur'])
    out, bloc, section = [], '', ''
    source_ouverte = False
    for ligne in lignes:
        titre = re.match(r'^(#{2,4})\s+(.*)$', ligne)
        if titre:
            if titre.group(1) == '##':
                section = _propre(titre.group(2))
            bloc = _propre(titre.group(2))
            source_ouverte = False
            continue
        if canon(section) in [canon(s) for s in SECTIONS_HORS_CONFRONTATION]:
            continue
        if canon(section) in [canon(b) for b in BLOCS_DE_JUGEMENT]:
            continue
        if '*Source' in ligne:
            source_ouverte = True
            continue
        if source_ouverte or _INLINE.search(ligne):
            continue          # un repère a été donné, la valeur n'est pas orpheline
        if ligne.lstrip().startswith('|'):
            continue          # les tableaux sont relevés par l'extracteur
        for v in nombres(masquer(ligne)):
            if v in prises.get(bloc, set()):
                continue
            out.append(dict(bloc=bloc, valeur=v, ligne=_propre(ligne)[:160]))
    return out


# --------------------------------------------------------------------------
# Résolution — lecture

def resoudre_lecture(rep, pieces):
    """Rouvre la pièce au repère et rend (verdict, ce que porte la pièce, motif,
    précision)."""
    nom = rep['piece']
    if not nom:
        return 'non sourcé', '', 'aucune pièce nommée', ''
    red = pieces.redaction(nom)
    if red is None:
        return 'introuvable', '', 'pièce « %s » hors de la voie lecture' % nom, ''
    if red.absente:
        return 'introuvable', '', 'pièce absente de l’atelier', ''
    art = red.article(rep['article'])
    if art is None:
        if rep['article'] is None:
            return ('introuvable', '',
                    'aucun article au repère : grandeur calculée par le '
                    'livrable à partir de valeurs elles-mêmes confrontées', '')
        return ('introuvable', '',
                'article « %s » absent de %s' % (rep['article'], red.nom), '')
    lignes = Redaction.lignes(art, rep['pages'], rep['emplacement'])
    if not lignes:
        return ('introuvable', '',
                'article %s : aucun contenu au repère (%s%s)'
                % (rep['article'], rep['emplacement'],
                   '' if not rep['pages'] else
                   ', p. %s' % '-'.join(str(p) for p in sorted(rep['pages']))),
                '')

    cible = canon(rep['libelle'])
    # 1 — la ligne dont l'étiquette est le libellé
    exactes = [(e, t) for e, t in lignes if cible and _colle(cible, t)]
    if exactes:
        portees = [v for _e, t in exactes for v in nombres(t)]
        if any(egal(rep['valeur'], v) for v in portees):
            return 'concorde', _rendu(portees), '', 'ligne'
        if portees:
            return ('diverge', _rendu(portees),
                    'ligne « %s »' % _propre(exactes[0][1])[:110], 'ligne')
        # une ligne d'intitulé sans chiffre : c'est une section du tableau
        return _dans_section(rep, lignes, exactes[0][1])
    # 2 — le libellé est un intitulé de section du tableau
    sect = [(e, t) for e, t in lignes
            if cible and _colle(cible, t) is False and canon(t) == cible]
    if sect:
        return _dans_section(rep, lignes, sect[0][1])
    # 3 — repli au périmètre de l'article
    portees = [v for _e, t in lignes for v in nombres(t)]
    if any(egal(rep['valeur'], v) for v in portees):
        return ('concorde', '', '', 'article')
    return ('introuvable', '',
            'libellé « %s » absent du repère' % _propre(rep['libelle'])[:110],
            '')


def _colle(cible, texte):
    """Le libellé du résumé ouvre-t-il la ligne de la pièce ?"""
    t = canon(texte)
    if not t:
        return False
    # la pièce colle parfois un appel de note au libellé : « ... (%)1 »
    t2 = re.sub(r'(\D)\d$', r'\1', t)
    return t.startswith(cible) or t2.startswith(cible) or cible.startswith(t2) \
        and len(t2) > 12


def _dans_section(rep, lignes, entete):
    """Le libellé nomme une section du tableau : la valeur s'y cherche."""
    dedans, vu = [], False
    cible = canon(entete)
    for _e, t in lignes:
        c = canon(t)
        if c == cible:
            vu = True
            continue
        if vu:
            if t and not nombres(t) and len(c) > 8 and c != cible:
                break          # section suivante
            dedans.append(t)
    portees = [v for t in dedans for v in nombres(t)]
    if any(egal(rep['valeur'], v) for v in portees):
        return 'concorde', '', '', 'section'
    if portees:
        return ('diverge', _rendu(portees),
                'section « %s »' % _propre(entete)[:110], 'section')
    return ('introuvable', '', 'section « %s » vide' % _propre(entete)[:70], '')


def _rendu(vals):
    return ' '.join(_fmt(v) for v in vals[:14])


def _fmt(v):
    s = format(v, 'f')
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s or '0'


# --------------------------------------------------------------------------
# Résolution — réapplication. Une recette par agrégat, nommée et motivée.

class Recette:
    def __init__(self, nom, bloc, ancre, motif, calcul):
        self.nom, self.bloc, self.motif, self.calcul = nom, bloc, motif, calcul
        self.ancre = re.compile(ancre, re.I | re.S)


def _num_cell(v):
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return Decimal(str(v))
    return nombre(v) if str(v).strip() else None


def _a2_lignes(p):
    """Les lignes de taxe affectée de l'annexe 2 — entêtes à la ligne 15,
    données à partir de la 16, une ligne par taxe, repérée par son libellé."""
    f = p.annexe2.feuille('taxes affectées')
    return [r for r in f[16:] if str(r[13]).strip()]


def _a2_plafonds(p):
    out = []
    for r in _a2_lignes(p):
        out.append((_num_cell(r[19]), _num_cell(r[22])))
    return out


def _a3(p, feuille):
    f = p.annexe3.feuille(feuille)
    return [r for r in f[4:] if str(r[3]).strip()]


def _ops(p):
    """Les opérateurs du classeur — une ligne par opérateur, à partir de la 4.
    Colonne 7 : plafond LFI 2025. Colonne 10 : plafond PLF 2026."""
    f = p.etp.feuille('Opérateurs')
    return [r for r in f[4:] if str(r[4]).strip()]


def _cnt_ops(p, quoi):
    a = [_num_cell(r[7]) for r in _ops(p)]
    b = [_num_cell(r[10]) for r in _ops(p)]
    z = list(zip(a, b))
    return {'sous_plafond': sum(1 for x in b if x is not None),
            'baisse': sum(1 for x, y in z if x and y and y < x),
            'hausse': sum(1 for x, y in z if x and y and y > x),
            'inchange': sum(1 for x, y in z if x and y and y == x)}[quoi]


def _plafond_op(p, mots, col):
    """Le plafond d'un opérateur nommé, à la colonne demandée du classeur.

    L'intitulé du classeur n'est pas celui du résumé — il porte un sigle, un
    tiret, parfois le nom développé. On apparie sur les mots du résumé, tous
    présents, et on refuse s'il y a plusieurs candidats : un appariement au plus
    proche ferait dire au classeur ce qu'il ne dit pas (A-94).
    """
    if p.etp.absent:
        return None
    cand = []
    for r in _ops(p):
        lib = canon(r[4])
        if all(m in lib for m in mots):
            cand.append(r)
    if len(cand) == 1:
        return _num_cell(cand[0][col])
    if len(cand) > 1:
        tot = [_num_cell(r[col]) for r in cand]
        if all(v is not None for v in tot):
            return sum(tot)
    return None


def _art36_blocs(p):
    """Les lignes du tableau d'affectation à des tiers, art. 36 du PLF.

    Le tableau est numéroté de 1 à n en tête de ligne, et une ligne du tableau
    peut occuper plusieurs lignes de composition. On retient la numérotation
    strictement croissante d'un en un — c'est le seul repère stable de la pièce
    aplatie — et on rend un bloc par ligne du tableau.
    """
    art = p.plf.article('36')
    if art is None:
        return []
    H = art.get('hors_alinea', [])
    attendu, debuts = 1, []
    for i, h in enumerate(H):
        m = re.match(r'\s*(\d{1,3})\s+\S', h.get('ligne', ''))
        if m and int(m.group(1)) == attendu:
            debuts.append(i)
            attendu += 1
    blocs = []
    for k, i in enumerate(debuts):
        j = debuts[k + 1] if k + 1 < len(debuts) else len(H)
        blocs.append([H[t].get('ligne', '') for t in range(i, j)])
    return blocs


def _tsv(p, nom):
    return {'plf': p.tsv_plf, 'plfss': p.tsv_plfss}[nom]


def _tsv_cnt(p, nom, quoi):
    t = _tsv(p, nom)
    if t.absente:
        return None
    if quoi == 'adresses':
        return Decimal(len(t.lignes))
    if quoi == 'textes':
        return Decimal(len({l['texte'] for l in t.lignes if l['texte'].strip()}))
    if quoi == 'porteurs':
        s = set()
        for l in t.lignes:
            for a in re.split(r'[,;/ ]+', l['articles']):
                if a.strip():
                    s.add(a.strip())
        return Decimal(len(s))
    if quoi == 'fourchettes':
        return Decimal(sum(1 for l in t.lignes
                           if (nombre(l['fourchette']) or 0) != 0))
    if quoi == 'divergences':
        return Decimal(sum(1 for l in t.lignes
                           if (nombre(l['divergence']) or 0) != 0))
    return None


def _tsv_texte(p, nom, libelle):
    t = _tsv(p, nom)
    if t.absente:
        return None
    c = canon(libelle)
    return Decimal(sum(1 for l in t.lignes if canon(l['texte']) == c))


def _tsv_article(p, nom, num):
    t = _tsv(p, nom)
    if t.absente:
        return None
    n = 0
    for l in t.lignes:
        if str(num) in [a.strip() for a in re.split(r'[,;/ ]+', l['articles'])]:
            n += 1
    return Decimal(n)


def _variation_relative(p):
    if p.etp.absent:
        return None
    f = p.etp.feuille('Opérateurs')
    a, b = _num_cell(f[3][7]), _num_cell(f[3][10])
    if not a or b is None:
        return None
    return ((b - a) / a * 100).quantize(Decimal('0.01'))


def _chiffrage_df(p, ident, annee):
    """Le chiffrage d'une dépense fiscale, par son numéro — colonne 5 pour
    2024, 6 pour 2025, 7 pour 2026."""
    if p.annexe3.absent:
        return None
    for r in _a3(p, 'Chiffrages'):
        if (_num_cell(r[3]) or 0) == Decimal(ident):
            return _num_cell(r[{2024: 5, 2025: 6, 2026: 7}[annee]])
    return None


def recettes():
    """Les réapplications déclarées. Chaque entrée dit ce qu'elle rejoue et sur
    quelle pièce ; une ancre la relie à la valeur que le résumé affirme."""
    R = []
    A = R.append

    # --- L'en-tête : ce que le livrable dit des pièces qu'il a lues
    A(Recette('PLF — articles de la pièce', '',
              r'reflux\s+déterministe de la pièce[\s\S]{0,140}?,\s*(\d+) articles',
              'compte d’articles déclaré par le référentiel de rédaction',
              lambda p: Decimal(len(p.plf.articles)) if not p.plf.absente
              else None))
    A(Recette('PLFSS — articles de la pièce', '',
              r'162\s*pages,\s*(\d+) articles',
              'compte d’articles du référentiel de rédaction du PLFSS',
              lambda p: Decimal(len(p.plfss.articles)) if not p.plfss.absente
              else None))

    # --- L2, les tables d'articles ouverts
    for veh, nom in (('plf', 'PLF 2026 n° 1906'), ('plfss', 'PLFSS 2026 n° 1907')):
        A(Recette('adresses ouvertes — %s' % veh.upper(), 'L2 — Les portes ouvertes',
                  r'\|\s*%s\s*\|\s*(\d+)\s*\|' % re.escape(nom),
                  'compte des lignes de la table d’articles ouverts',
                  lambda p, v=veh: _tsv_cnt(p, v, 'adresses')))
        A(Recette('textes ouverts — %s' % veh.upper(), 'L2 — Les portes ouvertes',
                  r'\|\s*%s\s*\|\s*\d+\s*\|\s*(\d+)\s*\|' % re.escape(nom),
                  'textes distincts de la table',
                  lambda p, v=veh: _tsv_cnt(p, v, 'textes')))
        A(Recette('articles porteurs — %s' % veh.upper(), 'L2 — Les portes ouvertes',
                  r'\|\s*%s\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*(\d+)\s*\|'
                  % re.escape(nom),
                  'articles du véhicule cités par la table',
                  lambda p, v=veh: _tsv_cnt(p, v, 'porteurs')))
        A(Recette('fourchettes — %s' % veh.upper(), 'L2 — Les portes ouvertes',
                  r'\|\s*%s\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*(\d+)\s*\|'
                  % re.escape(nom),
                  'lignes portant une fourchette',
                  lambda p, v=veh: _tsv_cnt(p, v, 'fourchettes')))
        A(Recette('divergences de grammaire — %s' % veh.upper(),
                  'L2 — Les portes ouvertes',
                  r'\|\s*%s\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*(\d+)\s*\|'
                  % re.escape(nom),
                  'lignes en divergence avec REF_norme',
                  lambda p, v=veh: _tsv_cnt(p, v, 'divergences')))

    A(Recette('adresses ouvertes — les deux véhicules', 'L2 — Les portes ouvertes',
              r'\*\*(\d+) adresses ouvertes\*\*',
              'somme des deux tables',
              lambda p: (_tsv_cnt(p, 'plf', 'adresses') or 0)
              + (_tsv_cnt(p, 'plfss', 'adresses') or 0)))

    A(Recette('textes ouverts — les deux véhicules', 'L2 — Les portes ouvertes',
              r'adresses ouvertes\*\*, sur (\d+) textes',
              'textes distincts des deux tables réunies — le livrable ajoute '
              'les deux comptes par véhicule (49 + 32), et huit textes sont '
              'ouverts par les deux véhicules',
              lambda p: Decimal(len(
                  {l['texte'] for l in p.tsv_plf.lignes if l['texte'].strip()}
                  | {l['texte'] for l in p.tsv_plfss.lignes
                     if l['texte'].strip()}))
              if not p.tsv_plf.absente else None))
    A(Recette('articles porteurs — les deux véhicules',
              'L2 — Les portes ouvertes',
              r'sur \d+ textes, par (\d+) articles',
              'articles porteurs des deux tables réunies',
              lambda p: (_tsv_cnt(p, 'plf', 'porteurs') or 0)
              + (_tsv_cnt(p, 'plfss', 'porteurs') or 0)))

    # (libellé exact à la pièce, libellé tel que le résumé l'écrit, véhicule)
    for lib, dit, veh in (
            ('code général des impôts', None, 'plf'),
            ('code des impositions sur les biens et services', None, 'plf'),
            ('code général des collectivités territoriales', None, 'plf'),
            ('code de la sécurité sociale', None, 'plfss'),
            ('code de la santé publique', None, 'plfss'),
            ('code rural et de la pêche maritime', None, 'plfss'),
            ('code de l’environnement', None, 'plf'),
            ('loi n° 2025-127 du 14 février 2025',
             'loi n° 2025-127 du 14 février 2025 de finances pour 2025', 'plf'),
            ('code des pensions civiles et militaires de retraite', None,
             'plfss'),
            ('ordonnance n° 96-1122 du 20 décembre 1996', None, 'plfss')):
        ecrit = dit or lib
        A(Recette('adresses — %s' % lib, 'L2 — Les portes ouvertes',
                  r'\s+'.join(re.escape(m) for m in ecrit.split()) + r'\s+(\d+)',
                  'lignes de la table portant exactement ce libellé de texte',
                  lambda p, l=lib, v=veh: _tsv_texte(p, v, l)))

    for num in (5, 72, 12, 23, 29, 13, 21):
        A(Recette('PLF art. %d — adresses' % num, 'L2 — Les portes ouvertes',
                  r'PLF\s*:[\s\S]{0,140}?\bart\.\s*%d\s*\((\d+)' % num,
                  'lignes de la table PLF citant cet article',
                  lambda p, n=num: _tsv_article(p, 'plf', n)))
    for num in (42, 43, 34, 22, 12):
        A(Recette('PLFSS art. %d — adresses' % num, 'L2 — Les portes ouvertes',
                  r'PLFSS\s*:[\s\S]{0,140}?\bart\.\s*%d\s*\((\d+)' % num,
                  'lignes de la table PLFSS citant cet article',
                  lambda p, n=num: _tsv_article(p, 'plfss', n)))

    # --- L3.a, le tableau de l'article 36 et l'annexe 2
    A(Recette('art. 36 — lignes du tableau', 'L3.a',
              r'\*\*(\d+) lignes\*\*, numérotées',
              'numérotation strictement croissante du tableau hors-alinéa',
              lambda p: Decimal(len(_art36_blocs(p))) or None))
    A(Recette('art. 36 — lignes « Non plafonnée »', 'L3.a',
              r'\*\*(\d+) portent\s*\n?\s*«\s*Non plafonnée\s*»\*\*',
              'lignes du tableau portant la mention littérale « Non plafonnée »',
              lambda p: Decimal(sum(
                  1 for b in _art36_blocs(p)
                  if any('non plafonn' in canon(l) for l in b)))
              if _art36_blocs(p) else None))
    A(Recette('art. 36 — lignes à plafond chiffré', 'L3.a',
              r'\*\*(\d+) lignes portent un plafond d[\'’]affectation 2026\s+chiffré\*\*',
              'lignes du tableau sans la mention « Non plafonnée »',
              lambda p: Decimal(sum(
                  1 for b in _art36_blocs(p)
                  if not any('non plafonn' in canon(l) for l in b)))
              if _art36_blocs(p) else None))
    A(Recette('art. 36 — somme des plafonds 2026', 'L3.a',
              r'somme des plafonds d[\'’]affectation 2026 des lignes\s+chiffrées\s*:\s*'
              r'\n?\s*([\d    ]+) €\*\*',
              'non outillée : la colonne des plafonds ne se sépare pas de celle '
              'du rendement prévisionnel — géométrie de colonne instable, que le '
              'livrable déclare lui-même (difficulté 2, emplacement non relevé 8)',
              lambda p: None))
    A(Recette('annexe 2 — lignes de taxe affectée', 'L3.a',
              r'(\d+) lignes de taxe affectée',
              'lignes de l’onglet « taxes affectées »',
              lambda p: Decimal(len(_a2_lignes(p))) if not p.annexe2.absent
              else None))
    A(Recette('annexe 2 — plafonnées en 2025', 'L3.a',
              r'\|\s*lignes plafonnées en 2025\s*\|\s*(\d+)\s*\|',
              'lignes portant un plafond 2025 chiffré',
              lambda p: Decimal(sum(1 for a, _b in _a2_plafonds(p) if a))
              if not p.annexe2.absent else None))
    A(Recette('annexe 2 — plafonnées en 2026', 'L3.a',
              r'\|\s*lignes plafonnées en 2026\s*\|\s*(\d+)\s*\|',
              'lignes portant un plafond 2026 chiffré',
              lambda p: Decimal(sum(1 for _a, b in _a2_plafonds(p) if b))
              if not p.annexe2.absent else None))
    A(Recette('annexe 2 — nouvellement plafonnées', 'L3.a',
              r'\|\s*\*\*nouvellement plafonnées\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|',
              'plafond 2026 chiffré, plafond 2025 vide',
              lambda p: Decimal(sum(1 for a, b in _a2_plafonds(p) if b and not a))
              if not p.annexe2.absent else None))
    A(Recette('annexe 2 — déplafonnées', 'L3.a',
              r'\|\s*\*\*déplafonnées\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|',
              'plafond 2025 chiffré, plafond 2026 vide',
              lambda p: Decimal(sum(1 for a, b in _a2_plafonds(p) if a and not b))
              if not p.annexe2.absent else None))
    A(Recette('annexe 2 — plafond relevé', 'L3.a',
              r'\|\s*plafond relevé\s*\|\s*(\d+)\s*\|',
              'plafond 2026 supérieur au plafond 2025',
              lambda p: Decimal(sum(1 for a, b in _a2_plafonds(p)
                                    if a and b and b > a))
              if not p.annexe2.absent else None))
    A(Recette('annexe 2 — plafond abaissé', 'L3.a',
              r'\|\s*plafond abaissé\s*\|\s*(\d+)\s*\|',
              'plafond 2026 inférieur au plafond 2025',
              lambda p: Decimal(sum(1 for a, b in _a2_plafonds(p)
                                    if a and b and b < a))
              if not p.annexe2.absent else None))
    A(Recette('annexe 2 — plafond inchangé', 'L3.a',
              r'\|\s*plafond inchangé\s*\|\s*(\d+)\s*\|',
              'plafond 2026 égal au plafond 2025',
              lambda p: Decimal(sum(1 for a, b in _a2_plafonds(p)
                                    if a and b and b == a))
              if not p.annexe2.absent else None))
    A(Recette('annexe 2 — somme des plafonds 2025', 'L3.a',
              r'Somme\s*\n?des plafonds 2025\s*:\s*([\d    ]+)\s*€',
              'somme de la colonne « Plafond 2025 »',
              lambda p: sum((a for a, _b in _a2_plafonds(p) if a), Decimal(0))
              if not p.annexe2.absent else None))
    A(Recette('annexe 2 — somme des plafonds 2026', 'L3.a',
              r'2026\s*:\s*([\d    ]+)\s*€\s*;',
              'somme de la colonne « Plafond 2026 »',
              lambda p: sum((b for _a, b in _a2_plafonds(p) if b), Decimal(0))
              if not p.annexe2.absent else None))
    A(Recette('annexe 2 — écart des sommes', 'L3.a',
              r'\*\*écart \+([\d    ]+) €\*\*',
              'somme 2026 moins somme 2025',
              lambda p: (sum((b for _a, b in _a2_plafonds(p) if b), Decimal(0))
                         - sum((a for a, _b in _a2_plafonds(p) if a), Decimal(0)))
              if not p.annexe2.absent else None))

    A(Recette('annexe 2 — plafond de la seule création', 'L3.a',
              r'plafonné à ([\d  \u00a0\u202f]+) € en 2026',
              'plafond 2026 de la seule ligne nouvellement plafonnée',
              lambda p: next((b for a, b in _a2_plafonds(p) if b and not a),
                             None) if not p.annexe2.absent else None))
    A(Recette('écart entre le tableau de l’article 36 et le classeur', 'L3.a',
              r'soit \*\*([\d  \u00a0\u202f]+) € d’écart\*\*',
              'non outillée : l’écart se calcule sur la somme des plafonds de '
              'l’article 36, que la géométrie de colonne de la pièce ne permet '
              'pas de rejouer',
              lambda p: None))

    # --- L3.b, l'annexe 3
    A(Recette('annexe 3 — dépenses fiscales', 'L3.b',
              r'\*\*(\d+) dépenses fiscales\.?\*\*',
              'lignes de l’onglet Chiffrages portant un numéro',
              lambda p: Decimal(len(_a3(p, 'Chiffrages')))
              if not p.annexe3.absent else None))
    A(Recette('annexe 3 — éteintes', 'L3.b',
              r'\*\*Éteintes — (\d+)\.\*\*',
              'chiffrage 2025 renseigné — nombre, ε ou nc — et 2026 à « - »',
              lambda p: Decimal(sum(1 for r in _a3(p, 'Chiffrages')
                                    if str(r[6]).strip() not in ('', '-')
                                    and str(r[7]).strip() == '-'))
              if not p.annexe3.absent else None))
    A(Recette('annexe 3 — somme des chiffrages 2025 des éteintes', 'L3.b',
              r'Somme de leurs chiffrages 2025\s*:\s*\*\*([\d    ]+) M€\*\*',
              'somme des seuls chiffrages numériques des lignes éteintes ; ε et '
              'nc ne se lisent pas comme zéro',
              lambda p: sum((_num_cell(r[6]) for r in _a3(p, 'Chiffrages')
                             if str(r[7]).strip() == '-'
                             and _num_cell(r[6]) is not None), Decimal(0))
              if not p.annexe3.absent else None))
    A(Recette('annexe 3 — créées', 'L3.b',
              r'\*\*Créées — (\d+)\.\*\*',
              'chiffrage 2024 à « - » et chiffrage 2026 renseigné',
              lambda p: Decimal(sum(1 for r in _a3(p, 'Chiffrages')
                                    if str(r[5]).strip() == '-'
                                    and str(r[7]).strip()
                                    and str(r[7]).strip() != '-'))
              if not p.annexe3.absent else None))
    A(Recette('annexe 3 — bornées', 'L3.b',
              r'\*\*Bornées — (\d+) sur 465\*\*',
              'fin du fait générateur portant un millésime',
              lambda p: Decimal(sum(1 for r in _a3(p, 'Echéances')
                                    if _num_cell(r[7]) is not None))
              if not p.annexe3.absent else None))
    A(Recette('annexe 3 — non bornées', 'L3.b',
              r'contre (\d+) non bornées',
              'fin du fait générateur à « Non borné »',
              lambda p: Decimal(sum(1 for r in _a3(p, 'Echéances')
                                    if canon(r[7]) == 'non borne'))
              if not p.annexe3.absent else None))
    for an, anc in ((2026, r'\*\*(\d+) finissent en 2026\*\*'),
                    (2025, r'(\d+) en 2025, \d+ en 2027'),
                    (2027, r'\d+ en 2025, (\d+) en 2027'),
                    (2024, r'(\d+) en 2024, \d+ en\s*\n?2029'),
                    (2029, r'\d+ en 2024, (\d+) en\s*\n?2029')):
        A(Recette('annexe 3 — fin du fait générateur %d' % an, 'L3.b', anc,
                  'lignes dont la fin du fait générateur est %d' % an,
                  lambda p, a=an: Decimal(sum(
                      1 for r in _a3(p, 'Echéances')
                      if (_num_cell(r[7]) or 0) == a))
                  if not p.annexe3.absent else None))

    for veh, nom, quoi, anc in (
            ('plf', 'PLF', 'abrogation',
             r'\*\*(\d+) alinéas d[\'’]abrogation ou de suppression au PLF\*\*'),
            ('plfss', 'PLFSS', 'abrogation', r'et \*\*(\d+) au PLFSS\*\*'),
            ('plf', 'PLF', 'creation', r'\*\*(\d+) alinéas\s+de\s*\n?\s*création\*\*'),
            ('plfss', 'PLFSS', 'creation', r'et \*\*(\d+) au PLFSS\*\*, sur 26')):
        A(Recette('alinéas de %s — %s' % (quoi, nom), 'L3.b', anc,
                  'non outillée : le livrable annonce un « relevé mécanique des '
                  'formules modificatives » sans nommer les formules relevées ; '
                  'la recette n’est pas déclarée, elle ne se devine pas',
                  lambda p: None))

    A(Recette('opérateurs — variation relative du plafond global', 'L3.c',
              r'ETPT\*\*, ([\u2212-]\d+,\d+) %',
              'variation relative du plafond global, arrondie à la précision '
              'que le livrable affiche',
              lambda p: _variation_relative(p)))

    # Les chiffrages nommés, relevés par leur numéro de dépense fiscale.
    # Le livrable les écrit « (120204, 621 M€) » : le numéro est le repère, et
    # l'appariement est exact, jamais au plus proche.
    for ident, annee in ((120204, 2025), (110215, 2025), (110242, 2025),
                         (110211, 2025), (800215, 2025), (210315, 2025),
                         (210329, 2025), (70201, 2025), (190212, 2025),
                         (220109, 2026), (320149, 2026)):
        A(Recette('dépense fiscale %d — chiffrage %d' % (ident, annee), 'L3.b',
                  r'\(%d,?\s*(?:et \d+\)?\s*portent\s*)?([\d ]+)\s*(?:et \d+ )?M€'
                  % ident,
                  'chiffrage %d de la ligne portant ce numéro' % annee,
                  lambda p, i=ident, a=annee: _chiffrage_df(p, i, a)))

    A(Recette('dépense fiscale 110270 — chiffrage 2026', 'L3.b',
              r'110270 et 110271\) portent (\d+) et \d+ M€',
              'chiffrage 2026 de la ligne portant ce numéro',
              lambda p: _chiffrage_df(p, 110270, 2026)))
    A(Recette('dépense fiscale 110271 — chiffrage 2026', 'L3.b',
              r'110270 et 110271\) portent \d+ et (\d+) M€',
              'chiffrage 2026 de la ligne portant ce numéro',
              lambda p: _chiffrage_df(p, 110271, 2026)))
    A(Recette('opérateurs fusionnés', 'L3.c',
              r'\*\*Fusionnés — (\d+)\.\*\*',
              'non outillée : le balayage des formules de dissolution, de '
              'fusion et de transfert à l’État n’est pas déclaré par le '
              'livrable, et une absence ne se rejoue pas sans lui',
              lambda p: None))

    # --- L3.c, le classeur des opérateurs
    A(Recette('opérateurs — plafond global LFI 2025', 'L3.c',
              r'\*\*([\d    ]+) ETPT en LFI 2025',
              'total « LFI 2025 – ETPT sous plafond » du classeur',
              lambda p: _num_cell(p.etp.feuille('Opérateurs')[3][7])
              if not p.etp.absent else None))
    A(Recette('opérateurs — plafond global PLF 2026', 'L3.c',
              r'LFI 2025, ([\d    ]+) en\s*\n?\s*PLF 2026',
              'total « PLF 2026 – ETPT sous plafond » du classeur',
              lambda p: _num_cell(p.etp.feuille('Opérateurs')[3][10])
              if not p.etp.absent else None))
    A(Recette('opérateurs — sous plafond', 'L3.c',
              r'\*\*(\d+) opérateurs\*\* sous plafond',
              'lignes d’opérateur portant un plafond PLF 2026',
              lambda p: Decimal(_cnt_ops(p, 'sous_plafond'))
              if not p.etp.absent else None))
    A(Recette('opérateurs — en baisse', 'L3.c',
              r'\*\*(\d+) en baisse',
              'plafond 2026 inférieur au plafond 2025',
              lambda p: Decimal(_cnt_ops(p, 'baisse'))
              if not p.etp.absent else None))
    A(Recette('opérateurs — en hausse', 'L3.c',
              r'en baisse, (\d+) en hausse',
              'plafond 2026 supérieur au plafond 2025',
              lambda p: Decimal(_cnt_ops(p, 'hausse'))
              if not p.etp.absent else None))
    # Les huit baisses les plus lourdes : le classeur porte, pour chaque
    # opérateur nommé, son plafond LFI 2025 et son plafond PLF 2026. La
    # réapplication est la lecture de la ligne de l'opérateur, par son intitulé.
    for op, av, ap in (('France Travail', 49147, 48632),
                       ('AFPA', 5330, 4824),
                       ('agences régionales de santé', 8273, 8114),
                       ('Réseau Canopé', 1237, 1137),
                       ('Centre national d’art et de culture Georges-Pompidou',
                        1007, 945),
                       ('Voies navigables de France', 3990, 3950),
                       ('Office national des forêts', 7946, 7914),
                       ('Agence nationale de la cohésion des territoires',
                        350, 320)):
        mots = [m for m in re.split(r'[^0-9a-z]+', canon(op)) if len(m) > 2]
        anc = (r'\s+'.join(re.escape(m) for m in op.replace('’', "'").split())
               + r'\s+([\d   ]+)\s*(?:→|->)')
        A(Recette('opérateur %s — plafond 2025' % op, 'L3.c', anc,
                  'plafond LFI 2025 de la ligne de l’opérateur au classeur',
                  lambda p, m=mots: _plafond_op(p, m, 7)))
        anc2 = (r'\s+'.join(re.escape(m) for m in op.replace('’', "'").split())
                + r'\s+[\d   ]+\s*(?:→|->)\s*([\d   ]+)\s*\(')
        A(Recette('opérateur %s — plafond 2026' % op, 'L3.c', anc2,
                  'plafond PLF 2026 de la ligne de l’opérateur au classeur',
                  lambda p, m=mots: _plafond_op(p, m, 10)))
        anc3 = (r'\s+'.join(re.escape(m) for m in op.replace('’', "'").split())
                + r'\s+[\d\u00a0\u202f ]+\s*(?:→|->)\s*[\d\u00a0\u202f ]+'
                  r'\s*\(([\u2212-][\d\u00a0\u202f ]+)\)')
        A(Recette('opérateur %s — variation' % op, 'L3.c', anc3,
                  'plafond PLF 2026 moins plafond LFI 2025, au classeur',
                  lambda p, m=mots: (
                      None if _plafond_op(p, m, 10) is None
                      or _plafond_op(p, m, 7) is None
                      else _plafond_op(p, m, 10) - _plafond_op(p, m, 7))))

    A(Recette('opérateurs — variation du plafond global', 'L3.c',
              r'soit \*\*([\u2212-][\d\u00a0\u202f ]+) ETPT\*\*',
              'total PLF 2026 moins total LFI 2025, au classeur',
              lambda p: (_num_cell(p.etp.feuille('Opérateurs')[3][10])
                         - _num_cell(p.etp.feuille('Opérateurs')[3][7]))
              if not p.etp.absent else None))

    A(Recette('opérateurs — inchangés', 'L3.c',
              r'en hausse, (\d+)\s*\n?\s*inchangés',
              'plafond 2026 égal au plafond 2025',
              lambda p: Decimal(_cnt_ops(p, 'inchange'))
              if not p.etp.absent else None))
    return R


def resoudre_reapplications(chemin_resume, pieces):
    texte = open(chemin_resume, encoding='utf-8').read()
    out = []
    for i, rec in enumerate(recettes(), 1):
        m = rec.ancre.search(texte)
        if not m:
            continue
        brut = next((g for g in m.groups() if g), None)
        dit = nombre(brut) if brut else None
        try:
            calc = rec.calcul(pieces)
        except Exception as exc:                      # noqa: BLE001
            calc, err = None, '%s: %s' % (type(exc).__name__, exc)
        else:
            err = ''
        if dit is None:
            verdict, porte, motif = 'non sourcé', '', 'valeur non relevée'
        elif calc is None:
            verdict, porte = 'introuvable', ''
            motif = err or rec.motif
        elif egal(dit, calc):
            verdict, porte, motif = 'concorde', _fmt(calc), rec.motif
        else:
            verdict, porte, motif = 'diverge', _fmt(calc), rec.motif
        out.append(dict(id='R%03d' % i, bloc=rec.bloc, mode='reapplication',
                        piece='réapplication', article='', emplacement='',
                        pages=None, libelle=rec.nom, colonne='',
                        valeur=dit, brut=brut or '', verdict=verdict,
                        porte=porte, motif=motif, precision='réapplication'))
    return out


# --------------------------------------------------------------------------
# Passe

# La table de repères dit où le livrable a lu ; le relevé dit ce que la pièce
# porte. Les deux ne se mélangent pas : la première se relit sans les verdicts,
# et c'est elle qui se confronte.
ENTETE_TABLE = ('id', 'bloc', 'mode', 'piece', 'article', 'emplacement',
                'pages', 'libelle', 'colonne', 'valeur')
ENTETE_RELEVE = ('id', 'bloc', 'mode', 'libelle', 'valeur', 'verdict',
                 'porte_par_la_piece', 'precision', 'motif')


VOIE_LECTURE = ('plf', 'plfss')


def _court(bloc):
    return re.split(r'\s+[—–-]\s+', bloc)[0].strip()


def confronter(racine, chemin_resume):
    pieces = Pieces(racine)
    bruts = extraire_reperes(chemin_resume)
    reapp = resoudre_reapplications(chemin_resume, pieces)
    couverts = {(_court(r['bloc']), r['valeur']) for r in reapp
                if r['valeur'] is not None}

    ordre = {'concorde': 0, 'diverge': 1, 'introuvable': 2, 'non sourcé': 3}
    reperes = []
    for r in bruts:
        noms = r['piece'] or ()
        if isinstance(noms, str):
            noms = (noms,)
        lectures = [n for n in noms if n in VOIE_LECTURE]
        autres = [n for n in noms if n not in VOIE_LECTURE]

        # Une valeur déjà portée par une recette ne se compte pas deux fois :
        # la réapplication est l'opération juste, la lecture ne l'est pas.
        couvert = (_court(r['bloc']), r['valeur']) in couverts
        if couvert and (autres or not lectures):
            continue

        best = None
        for n in lectures:
            v, porte, motif, prec = resoudre_lecture(dict(r, piece=n), pieces)
            cand = (ordre[v], v, porte, motif, prec)
            if best is None or cand[0] < best[0]:
                best = cand
        if couvert and (best is None or best[1] == 'introuvable'):
            continue      # la recette porte l'opération juste pour cette valeur
        if best is not None and best[1] != 'introuvable':
            r.update(piece='+'.join(noms), verdict=best[1], porte=best[2],
                     motif=best[3], precision=best[4])
            reperes.append(r)
            continue
        if autres:
            # La pièce est un classeur ou une table : la valeur est un agrégat,
            # et un agrégat ne se lit pas à un repère, il se rejoue.
            r.update(piece='+'.join(noms), mode='reapplication',
                     verdict='introuvable', porte='', precision='',
                     motif='agrégat de « %s » : réapplication non déclarée'
                           % ', '.join(autres))
            reperes.append(r)
            continue
        if best is None:
            v, porte, motif, prec = resoudre_lecture(dict(r, piece=None), pieces)
            best = (ordre[v], v, porte, motif, prec)
        r.update(piece='+'.join(noms), verdict=best[1], porte=best[2],
                 motif=best[3], precision=best[4])
        reperes.append(r)
    reperes += reapp
    non_sourcees = valeurs_non_sourcees(chemin_resume, reperes)
    return reperes, non_sourcees


def comptes(reperes, non_sourcees):
    c = {'concorde': 0, 'diverge': 0, 'introuvable': 0, 'non sourcé': 0}
    for r in reperes:
        c[r['verdict']] = c.get(r['verdict'], 0) + 1
    confrontables = c['concorde'] + c['diverge']
    taux = (100.0 * c['concorde'] / confrontables) if confrontables else 0.0
    return dict(c, confrontables=confrontables, taux=taux,
                valeurs_sans_repere=len(non_sourcees), relevees=len(reperes))


def _champ(r, nom):
    if nom == 'pages':
        return '-'.join(str(p) for p in sorted(r['pages'])) if r.get('pages') \
            else ''
    if nom == 'valeur':
        return _fmt(r['valeur']) if r['valeur'] is not None else ''
    if nom == 'porte_par_la_piece':
        return r['porte']
    return r.get(nom) or ''


def _ligne_tsv(r, entete):
    return '\t'.join(str(_champ(r, n)).replace('\t', ' ') for n in entete)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--racine', default='.')
    ap.add_argument('--resume',
                    default='livrables/resume_attendu_texte_financier_2026.md')
    ap.add_argument('--table',
                    default='referentiels/reperes_resume_2026.tsv')
    ap.add_argument('--releve',
                    default='livrables/confrontation_resume_2026.tsv')
    ap.add_argument('--muet', action='store_true')
    a = ap.parse_args(argv)

    resume = a.resume if os.path.isabs(a.resume) \
        else os.path.join(a.racine, a.resume)
    if not os.path.isfile(resume):
        print('résumé introuvable : %s' % resume)
        return 2

    reperes, non_sourcees = confronter(a.racine, resume)
    c = comptes(reperes, non_sourcees)

    for chemin, entete in ((a.table, ENTETE_TABLE), (a.releve, ENTETE_RELEVE)):
        p = chemin if os.path.isabs(chemin) else os.path.join(a.racine, chemin)
        os.makedirs(os.path.dirname(p) or '.', exist_ok=True)
        with open(p, 'w', encoding='utf-8', newline='') as f:
            f.write('\t'.join(entete) + '\n')
            for r in reperes:
                f.write(_ligne_tsv(r, entete) + '\n')
            if entete is ENTETE_RELEVE and non_sourcees:
                f.write('\n# grandeurs affirmées sans aucun repère\n')
                f.write('# bloc\tvaleur\tligne\n')
                for n in non_sourcees:
                    f.write('#\t%s\t%s\t%s\n'
                            % (n['bloc'], _fmt(n['valeur']), n['ligne']))

    if not a.muet:
        print('C1 — %d valeur(s) relevée(s) avec repère' % c['relevees'])
        print('C2 — %d concorde(nt)' % c['concorde'])
        print('C3 — %d diverge(nt)' % c['diverge'])
        print('C4 — %d introuvable(s)' % c['introuvable'])
        print('C5 — %d non sourcée(s) au relevé' % c['non sourcé'])
        print('C6 — taux de concordance %.1f %% sur %d confrontable(s)'
              % (c['taux'], c['confrontables']))
        print('C7 — %d grandeur(s) affirmée(s) sans aucun repère'
              % c['valeurs_sans_repere'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
