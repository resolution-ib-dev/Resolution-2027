#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Impression d'une liasse d'amendements en .docx déposable.

Reconstruit le 20261016 depuis sa spécification, qui est
`methode/etats/NUIT_8_impression_20261008.md` du corpus Résolution : table des
conventions de source, typographie, mécanisme de saut de page, champs `PAGEREF`,
règle de recollage, invariant de caractères. Le générateur de la version 1.4 du
paquet est périmé — il partitionnait sur `\\newpage`, que les liasses courantes ne
portent plus.

## Les conventions de source qu'il lit

    # Titre                      grand titre centré, petites capitales grasses
    ## Lot I : …                 intitulé de division, petites capitales
    ## Amendement n° 2 [titre]   SAUT DE PAGE porté par ce paragraphe, signet,
                                 rang et titre d'une ligne, centrés, petites
                                 capitales grasses
    ---                          rien : règle de séparation, le saut suivant la
                                 redouble
    AMENDEMENT                   cartouche centré
    présenté par                 cartouche centré
    ----------                   cartouche centré
    ARTICLE …                    cartouche centré
    EXPOSÉ SOMMAIRE              intitulé de division, petites capitales
    **Article 1er**              intitulé d'article, petites capitales
    **I.** – · I. – · 1° · a)    subdivision, retrait de première ligne
    « …                          texte cité, retrait de 0,5 pouce
    ¹ …                          note de source, corps réduit
    | … | … |                    tableau, ligne de tête grisée, montants à droite

**Le saut de page est porté par le paragraphe suivant** (`pageBreakBefore`) et
non par un paragraphe de saut propre. Un paragraphe de saut produit une page
blanche chaque fois que le texte s'arrête exactement en bas de page : cinq à la
première passe du 20261008, zéro avec `pageBreakBefore`.

**Le recollage.** Un markdown enveloppé dur coupe un gras en deux et imprime ses
astérisques en clair. On recolle les lignes internes d'un paragraphe, sans
toucher un caractère — on ne supprime que des retours à la ligne. Les notes de
source, ouvertes par un appel en exposant, ne se recollent jamais entre elles.

Usage :
    python3 generateur_liasse_docx.py <source.md> [source2.md …] -o <sortie.docx>
    python3 generateur_liasse_docx.py <source.md> -o <s.docx> --numerotation-liasse
"""
import argparse
import os
import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

POLICE = "Garamond"
CORPS = Pt(11)
CORPS_NOTE = Pt(9)

EXPOSANTS = "¹²³⁴⁵⁶⁷⁸⁹"
RE_AMENDEMENT = re.compile(r"^##\s+Amendement\s+n°\s*(\S+)\s*\[(.+)\]\s*$")
RE_H2 = re.compile(r"^##\s+(.*)$")
RE_H1 = re.compile(r"^#\s+(.*)$")
RE_CARTOUCHE = re.compile(
    r"^(AMENDEMENT|présenté par|-{4,}|ARTICLE(\s+.*)?|APRÈS L[’']ARTICLE.*)$")
RE_DIVISION = re.compile(r"^(EXPOSÉ SOMMAIRE|EXPOSE SOMMAIRE)$")
RE_SUBDIVISION = re.compile(
    r"^(\*\*)?([IVXLC]+\.|[0-9]+°|[a-z]\)|[A-Z]\.)(\*\*)?\s*[–—-]?\s")
RE_NOTE = re.compile(r"^[" + EXPOSANTS + r"]\s")
RE_TABLE = re.compile(r"^\s*\|.*\|\s*$")
# Exactement trois tirets : règle de séparation de la liasse, qui ne se rend
# pas. Quatre et plus : la ligne de tirets du cartouche d'amendement, qui se
# rend. Un motif `-{3,}` avalait le cartouche — défaut relevé le 20261016 sur le
# PDF de contrôle, invisible à l'invariant de caractères parce que les deux
# côtés le supprimaient de la même façon.
RE_SEPARATEUR = re.compile(r"^-{3}$")
RE_ALIGNEMENT = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
RE_MONTANT = re.compile(r"^[\s0-9  .,%+−-]*$")


# ---------------------------------------------------------------- bas niveau

def _petites_capitales(run):
    rpr = run._element.get_or_add_rPr()
    el = OxmlElement("w:smallCaps")
    el.set(qn("w:val"), "true")
    rpr.append(el)


def _saut_avant(par):
    ppr = par._p.get_or_add_pPr()
    el = OxmlElement("w:pageBreakBefore")
    el.set(qn("w:val"), "true")
    ppr.append(el)


def _sans_cesure(par):
    ppr = par._p.get_or_add_pPr()
    el = OxmlElement("w:suppressAutoHyphens")
    el.set(qn("w:val"), "true")
    ppr.append(el)


def _signet(par, nom, ident):
    """Pose un signet Word autour du paragraphe, cible d'un PAGEREF."""
    deb = OxmlElement("w:bookmarkStart")
    deb.set(qn("w:id"), str(ident))
    deb.set(qn("w:name"), nom)
    fin = OxmlElement("w:bookmarkEnd")
    fin.set(qn("w:id"), str(ident))
    par._p.insert(0, deb)
    par._p.append(fin)


def _champ(par, instruction, repli="—"):
    """Écrit un champ Word vivant (PAGEREF, PAGE…) avec sa valeur de repli."""
    r1 = par.add_run()
    f1 = OxmlElement("w:fldChar")
    f1.set(qn("w:fldCharType"), "begin")
    r1._element.append(f1)
    r2 = par.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = f" {instruction} "
    r2._element.append(it)
    r3 = par.add_run()
    f3 = OxmlElement("w:fldChar")
    f3.set(qn("w:fldCharType"), "separate")
    r3._element.append(f3)
    r4 = par.add_run(repli)
    r5 = par.add_run()
    f5 = OxmlElement("w:fldChar")
    f5.set(qn("w:fldCharType"), "end")
    r5._element.append(f5)
    for r in (r1, r2, r3, r4, r5):
        r.font.name = POLICE
        r.font.size = CORPS


def _ombrer(cellule, teinte="D9D9D9"):
    tcpr = cellule._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear")
    sh.set(qn("w:fill"), teinte)
    tcpr.append(sh)


# ------------------------------------------------------------ texte en ligne

def _ecrire_inline(par, texte, taille=None, capitales=False):
    """Rend `**gras**` et `*italique*` sans toucher aux autres caractères."""
    taille = taille or CORPS
    morceaux = re.split(r"(\*\*.+?\*\*|(?<!\*)\*(?!\*).+?(?<!\*)\*(?!\*))", texte)
    for m in morceaux:
        if not m:
            continue
        gras = ital = False
        if m.startswith("**") and m.endswith("**") and len(m) > 4:
            m, gras = m[2:-2], True
        elif m.startswith("*") and m.endswith("*") and len(m) > 2:
            m, ital = m[1:-1], True
        run = par.add_run(m)
        run.bold, run.italic = gras, ital
        run.font.name = POLICE
        run.font.size = taille
        if capitales:
            _petites_capitales(run)
    return par


# ----------------------------------------------------------------- recollage

def recoller(lignes):
    """Rend les paragraphes entiers d'un markdown enveloppé dur.

    Ne supprime que des retours à la ligne internes à un paragraphe. Aucun autre
    caractère n'est ajouté, retiré ni substitué. Les notes de source ne se
    recollent jamais entre elles.
    """
    sortie, tampon = [], []

    def vider():
        if tampon:
            sortie.append(" ".join(tampon))
            tampon.clear()

    for ligne in lignes:
        nue = ligne.rstrip("\n")
        structurelle = (
            not nue.strip()
            or RE_H1.match(nue) or RE_H2.match(nue)
            or RE_TABLE.match(nue) or RE_SEPARATEUR.match(nue)
            or RE_CARTOUCHE.match(nue.strip()) or RE_DIVISION.match(nue.strip())
            or nue.startswith("«") or RE_NOTE.match(nue)
            or RE_SUBDIVISION.match(nue)
        )
        if structurelle:
            vider()
            sortie.append(nue)
        else:
            tampon.append(nue.strip())
    vider()
    return sortie


# ------------------------------------------------------------------- gabarit

def gabarit(numerotation_liasse=False):
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = POLICE
    st.font.size = CORPS
    st.element.rPr.rFonts.set(qn("w:eastAsia"), POLICE)
    pf = st.paragraph_format
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.line_spacing = 1.15
    pf.space_after = Pt(6)

    s = doc.sections[0]
    s.top_margin = s.bottom_margin = Inches(1)
    s.left_margin = s.right_margin = Inches(1.1)

    pied = s.footer.paragraphs[0]
    pied.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _champ(pied, "PAGE", "1")

    # La césure automatique de LibreOffice coupe les mots composés : on la pose
    # à false aux propriétés par défaut, ce qui vaut pour Word comme pour LO.
    dd = doc.styles.element.find(qn("w:docDefaults"))
    if dd is not None:
        ppd = dd.find(qn("w:pPrDefault"))
        if ppd is None:
            ppd = OxmlElement("w:pPrDefault")
            dd.append(ppd)
        ppr = ppd.find(qn("w:pPr"))
        if ppr is None:
            ppr = OxmlElement("w:pPr")
            ppd.append(ppr)
        el = OxmlElement("w:suppressAutoHyphens")
        el.set(qn("w:val"), "true")
        ppr.append(el)
    return doc


# ------------------------------------------------------------------- rendu

class Rendu:
    def __init__(self, doc):
        self.doc = doc
        self.signets = {}          # rang -> nom de signet, relevé au prescan
        self.poses = set()         # rangs dont le signet est réellement posé
        self.ident = 1
        self.amendements = 0
        self.sauts = 0
        self.pagerefs = 0          # renvois vivants écrits
        self.pagerefs_morts = 0    # lignes de sommaire sans signet à viser
        self.sommaires = 0         # tableaux ayant reçu la colonne « page »

    # -- paragraphes typés ------------------------------------------------
    def titre(self, texte):
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(12)
        _ecrire_inline(p, texte, Pt(16), capitales=True)
        for r in p.runs:
            r.bold = True
        return p

    def division(self, texte, saut=False):
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(8)
        _ecrire_inline(p, texte, Pt(12), capitales=True)
        for r in p.runs:
            r.bold = True
        if saut:
            _saut_avant(p)
            self.sauts += 1
        return p

    def en_tete_amendement(self, rang, titre):
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(14)
        p.paragraph_format.keep_with_next = True
        _ecrire_inline(p, f"Amendement n° {rang} — {titre}", Pt(12), capitales=True)
        for r in p.runs:
            r.bold = True
        _saut_avant(p)                      # le saut est porté par ce paragraphe
        self.sauts += 1
        nom = self.signets.setdefault(
            str(rang), f"amdt_{re.sub(r'[^A-Za-z0-9]', '_', str(rang))}")
        _signet(p, nom, self.ident)
        self.poses.add(str(rang))
        self.ident += 1
        self.amendements += 1
        return p

    def cartouche(self, texte):
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(4)
        _ecrire_inline(p, texte)
        return p

    def intitule_article(self, texte):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        _ecrire_inline(p, texte, capitales=True)
        for r in p.runs:
            r.bold = True
        return p

    def cite(self, texte):
        p = self.doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.5)
        _ecrire_inline(p, texte)
        return p

    def subdivision(self, texte):
        p = self.doc.add_paragraph()
        p.paragraph_format.first_line_indent = Inches(0.25)
        _ecrire_inline(p, texte)
        return p

    def note(self, texte):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        _ecrire_inline(p, texte, CORPS_NOTE)
        return p

    def courant(self, texte):
        p = self.doc.add_paragraph()
        _ecrire_inline(p, texte)
        return p

    # -- tableaux ---------------------------------------------------------
    def tableau(self, lignes, colonne_page=None):
        rangs = []
        for l in lignes:
            if RE_ALIGNEMENT.match(l):
                continue
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            rangs.append(cells)
        if not rangs:
            return None
        larg = max(len(r) for r in rangs)
        rangs = [r + [""] * (larg - len(r)) for r in rangs]
        # Un tableau de sommaire se reconnaît à sa ligne de tête : il reçoit la
        # quatrième colonne `page`, et elle seule est ajoutée au texte.
        tete = " ".join(rangs[0]).lower()
        if colonne_page is None:
            colonne_page = ("n°" in tete or "n °" in tete) and "objet" in tete
        if colonne_page:
            larg += 1
            self.sommaires += 1
        t = self.doc.add_table(rows=0, cols=larg)
        t.style = "Table Grid"
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, r in enumerate(rangs):
            cellules = t.add_row().cells
            valeurs = r + (["page"] if colonne_page and i == 0 else [""] if colonne_page else [])
            for j, v in enumerate(valeurs):
                c = cellules[j]
                c.text = ""
                p = c.paragraphs[0]
                p.paragraph_format.space_after = Pt(2)
                if colonne_page and j == larg - 1 and i > 0:
                    # renvoi vivant vers le signet de l'amendement de ce rang
                    rang = r[0].strip()
                    nom = self.signets.get(rang)
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    if nom:
                        # Repli vide, et c'est voulu : la valeur de repli d'un
                        # champ compte comme du texte. Un repli « — » ajoutait
                        # un cadratin par ligne de sommaire et faussait
                        # l'invariant de caractères — 34 sur la liasse P1, défaut
                        # relevé par le test 2 le 20261016. Le numéro se calcule
                        # à l'ouverture ; `refresh_toc_pdf.py` le pose pour le
                        # PDF de contrôle.
                        _champ(p, f"PAGEREF {nom} \\h", repli="")
                        self.pagerefs += 1
                    else:
                        _ecrire_inline(p, "—")
                        self.pagerefs_morts += 1
                    continue
                p.alignment = (WD_ALIGN_PARAGRAPH.RIGHT
                               if i > 0 and j > 0 and v and RE_MONTANT.match(v)
                               else WD_ALIGN_PARAGRAPH.LEFT)
                _ecrire_inline(p, v, capitales=False)
                if i == 0:
                    for run in p.runs:
                        run.bold = True
                    _ombrer(c)
        return t

    # -- boucle principale -------------------------------------------------
    def prescan(self, lignes):
        """Relève les rangs d'amendement avant tout rendu.

        Sans ce passage, un sommaire placé en tête de liasse ne trouve aucun
        signet à viser et sa colonne `page` sort vide. C'est le défaut que le
        premier essai du 20261016 a rendu : 0 renvoi sur 34.
        """
        for l in lignes:
            m = RE_AMENDEMENT.match(l.strip())
            if m:
                rang = m.group(1)
                nom = f"amdt_{re.sub(r'[^A-Za-z0-9]', '_', str(rang))}"
                self.signets.setdefault(str(rang), nom)

    def rendre(self, lignes, premier_bloc=True):
        i, n = 0, len(lignes)
        premier = premier_bloc
        while i < n:
            l = lignes[i]
            nue = l.strip()
            if not nue:
                i += 1
                continue
            if RE_SEPARATEUR.match(nue) and not RE_TABLE.match(nue):
                i += 1                               # règle de séparation : rien
                continue
            if RE_TABLE.match(l):
                bloc = []
                while i < n and RE_TABLE.match(lignes[i]):
                    bloc.append(lignes[i])
                    i += 1
                self.tableau(bloc)
                continue
            m = RE_AMENDEMENT.match(nue)
            if m:
                self.en_tete_amendement(m.group(1), m.group(2))
                i += 1
                continue
            m = RE_H1.match(nue)
            if m and not nue.startswith("##"):
                self.titre(m.group(1))
                i += 1
                continue
            m = RE_H2.match(nue)
            if m:
                self.division(m.group(1), saut=not premier)
                premier = False
                i += 1
                continue
            if RE_DIVISION.match(nue):
                self.division(nue)
                i += 1
                continue
            if RE_CARTOUCHE.match(nue):
                self.cartouche(nue)
                i += 1
                continue
            if nue.startswith("«"):
                self.cite(nue)
                i += 1
                continue
            if RE_NOTE.match(nue):
                self.note(nue)
                i += 1
                continue
            if re.match(r"^\*\*Article\b", nue):
                self.intitule_article(nue)
                i += 1
                continue
            if RE_SUBDIVISION.match(nue):
                self.subdivision(nue)
                i += 1
                continue
            self.courant(nue)
            i += 1
            premier = False


# ---------------------------------------------------------------- extraction

def texte_du_docx(chemin):
    """Flux de texte du docx, pour l'invariant de caractères.

    Lu sur le document, jamais sur un PDF : aucune substitution de police ne
    peut le fausser.
    """
    doc = Document(chemin)
    morceaux = []

    def _corps(element):
        for p in element.paragraphs:
            morceaux.append(p.text)
        for t in element.tables:
            for r in t.rows:
                for c in r.cells:
                    for p in c.paragraphs:
                        morceaux.append(p.text)
    _corps(doc)
    return "\n".join(morceaux)


def texte_du_source(chemins):
    """Même flux, côté markdown : balisage résolu, structure retirée."""
    morceaux = []
    for ch in chemins:
        for l in open(ch, encoding="utf-8").read().splitlines():
            nue = l.strip()
            if not nue or RE_SEPARATEUR.match(nue) and not RE_TABLE.match(nue):
                continue
            if RE_ALIGNEMENT.match(nue):
                continue
            m = RE_AMENDEMENT.match(nue)
            if m:
                morceaux.append(f"Amendement n° {m.group(1)} — {m.group(2)}")
                continue
            nue = re.sub(r"^#+\s+", "", nue)
            if RE_TABLE.match(nue):
                nue = " ".join(c.strip() for c in nue.strip("|").split("|"))
            nue = re.sub(r"\*\*(.+?)\*\*", r"\1", nue)
            nue = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\1", nue)
            morceaux.append(nue)
    return "\n".join(morceaux)


SENSIBLES = {
    "espace insécable": " ",
    "apostrophe typographique": "’",
    "guillemet français ouvrant": "«",
    "guillemet français fermant": "»",
    "tiret cadratin": "—",
    "tiret demi-cadratin": "–",
}


def comptes_sensibles(texte):
    return {nom: texte.count(c) for nom, c in SENSIBLES.items()}


# -------------------------------------------------------------------- main

def imprimer(sources, sortie, numerotation_liasse=False):
    doc = gabarit(numerotation_liasse)
    rendu = Rendu(doc)
    blocs = [recoller(open(s, encoding="utf-8").read().splitlines())
             for s in sources]
    for lignes in blocs:                     # premier passage : les rangs
        rendu.prescan(lignes)
    for k, lignes in enumerate(blocs):       # second passage : le rendu
        rendu.rendre(lignes, premier_bloc=(k == 0))
    for p in doc.paragraphs:
        _sans_cesure(p)
    doc.save(sortie)
    return rendu


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("sources", nargs="+")
    ap.add_argument("-o", "--sortie", required=True)
    ap.add_argument("--numerotation-liasse", action="store_true",
                    help="repart la pagination à 1 sur la première liasse")
    a = ap.parse_args(argv[1:])
    for s in a.sources:
        if not os.path.exists(s):
            print(f"source absente : {s}", file=sys.stderr)
            return 2
    r = imprimer(a.sources, a.sortie, a.numerotation_liasse)
    print(f"{a.sortie} — {os.path.getsize(a.sortie)} octets")
    print(f"  amendements rendus   {r.amendements}")
    print(f"  sauts de page posés  {r.sauts}")
    print(f"  signets posés        {len(r.signets)}")
    print(f"  renvois PAGEREF      {r.pagerefs}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
