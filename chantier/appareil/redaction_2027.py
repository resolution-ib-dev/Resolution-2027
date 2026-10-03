#!/usr/bin/env python3
"""Rédaction exacte des articles d'un texte financier déposé.

Verse ce que nulle autre source ne rend : la rédaction exacte des articles,
alinéa par alinéa, le hors-alinéa, et les adresses relevées à la disposition.
Le fichier se régénère intégralement depuis la pièce nommée à `_revision`, et
il n'ajoute rien qui ne s'y lise.

L'exposé des motifs est retiré : il est de l'indice, pas de la norme.
"""
import hashlib, json, re, subprocess, sys
import pieces_nommees, portes_ouvertes as PO

OUTIL = "pdftotext -layout -enc UTF-8 -eol unix"

GAB = {
    "plf": {
        "art":    re.compile(r'^\s*ARTICLE\s+(liminaire|\d+(?:\s+(?:bis|ter|quater))?)\s*:\s*(.*)$'),
        "folio":  re.compile(r'^\s*(?:Projet de loi de finances\s+(\d+)|(\d+)\s+Projet de loi de finances)\s*$'),
        "partie": re.compile(r'^\s*((?:PREMIÈRE|SECONDE|DEUXIÈME)\s+PARTIE)\s*:?\s*(.*)$'),
        "titre":  re.compile(r'^\s*(TITRE\s+(?:PREMIER|[IVX]+))\s*:?\s*(.*)$'),
        "div":    re.compile(r'^\s*((?:[IVX]+\s*[–\-]|[A-H]\s*[.\-–]+)\s*[A-ZÉÈÀÂÎÔÛ][^\n]{4,}?)\s*$'),
        "debut":  re.compile(r'^\s*Articles du projet de loi avec exposé des motifs\s*$'),
        "fin":    re.compile(r'^\s*États législatifs annexés\s*$'),
    },
    "plfss": {
        "art":    re.compile(r'^\s*Article\s+(liminaire|\d+(?:er)?(?:\s+(?:bis|ter))?)\s*$'),
        "folio":  re.compile(r'^\s*NOR\s*:.*?(\d+)\s*/\s*\d+\s*$'),
        "partie": re.compile(r'^\s*((?:PREMIÈRE|SECONDE|DEUXIÈME|TROISIÈME|TROISIEME|QUATRIÈME|QUATRIEME)\s+PARTIE)\s*:?\s*(.*)$'),
        "titre":  re.compile(r'^\s*(TITRE\s+(?:[IVX]+er?|PREMIER|Ier))\s*:?\s*(.*)$'),
        "div":    re.compile(r'^\s*(CHAPITRE\s+[IVX0-9]+.*)$'),
        "debut":  None,
        "fin":    None,
    },
}
EDM = re.compile(r'^\s*Exposé des motifs\s*$')
CHIFFRE = re.compile('-?\\d[\\d\u00a0\u202f ,.%]*$')


def est_tableau(l):
    s = l.rstrip()
    if not s.strip():
        return False
    cols = [c for c in re.split(r' {2,}', s.strip()) if c]
    return len(cols) >= 2 and any(CHIFFRE.match(c.strip()) for c in cols[1:])


def alineas(lignes):
    """Reflux déterministe : un alinéa est un paragraphe. Une zone de tableau se
    garde dans sa mise en page — là, la mise en page est l'information."""
    out, buf, pg, tab = [], [], None, False
    for txt, p in lignes:
        if not txt.strip():
            if buf:
                out.append({"numero": len(out) + 1, "page": pg, "tableau": tab,
                            "texte": ("\n".join(buf) if tab else " ".join(buf))})
                buf, tab = [], False
            continue
        if pg is None or not buf:
            pg = p
        t = est_tableau(txt)
        if t != tab and buf:
            out.append({"numero": len(out) + 1, "page": pg, "tableau": tab,
                        "texte": ("\n".join(buf) if tab else " ".join(buf))})
            buf, pg = [], p
        tab = t
        buf.append(txt.rstrip() if t else txt.strip())
    if buf:
        out.append({"numero": len(out) + 1, "page": pg, "tableau": tab,
                    "texte": ("\n".join(buf) if tab else " ".join(buf))})
    return out


def lire(pdf, vehicule):
    g = GAB[vehicule]
    pages = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", "-eol", "unix", pdf, "-"],
                           capture_output=True, text=True, check=True).stdout.split("\f")
    lignes, folio, ouvert = [], None, g["debut"] is None
    p0 = p1 = None
    for i, p in enumerate(pages, 1):
        ls = p.split("\n")
        if not ouvert:
            if any(g["debut"].match(l) for l in ls):
                ouvert, p0 = True, i
            continue
        if g["fin"] and any(g["fin"].match(l) for l in ls):
            p1 = i
            break
        m = g["folio"].match(ls[0]) if ls else None
        if m:
            folio = int(next(x for x in m.groups() if x)); ls = ls[1:]
        for l in ls:
            lignes.append((l, folio if folio is not None else i))
    return lignes, len(pages), p0 or 1, p1 or len(pages)


def articles(lignes, vehicule):
    g = GAB[vehicule]
    arts, cur = [], None
    partie = partie_i = titre = titre_i = None
    divs, zone, suite = [], None, None
    for l, f in lignes:
        mp = g["partie"].match(l)
        if mp:
            partie, partie_i = mp.group(1).strip(), " ".join(mp.group(2).split())
            titre = titre_i = None; divs = []
            suite = "partie"
            continue
        mt = g["titre"].match(l)
        if mt:
            titre, titre_i = mt.group(1).strip(), " ".join(mt.group(2).split())
            divs = []; suite = "titre"
            continue
        if (suite and l.strip() and l.strip() == l.strip().upper()
                and not (g["div"] and g["div"].match(l))):
            if suite == "partie": partie_i = (partie_i + " " + " ".join(l.split())).strip()
            else: titre_i = (titre_i + " " + " ".join(l.split())).strip()
            continue
        suite = None
        md = g["div"].match(l) if g["div"] else None
        # Une division se suit comme la partie et le titre : hors du corps, elle
        # se met à jour quel que soit l'article courant — le liminaire précède la
        # première partie, et exiger « aucun article ouvert » les perdait toutes.
        if md:
            d = " ".join(md.group(1).split())
            # Deux niveaux : le chiffre romain ouvre, la lettre subdivise. Un
            # romain neuf chasse tout ; une lettre neuve chasse les lettres.
            rom = bool(re.match(r"^[IVX]+\s*[–\-]", d))
            if rom:
                divs = [d]
            else:
                divs = [x for x in divs if re.match(r"^[IVX]+\s*[–\-]", x)] + [d]
            continue
        ma = g["art"].match(l)
        if ma:
            if cur: arts.append(cur)
            num = re.sub(r"^(\d+)er$", r"\1", " ".join(ma.group(1).split()))
            cur = {"numero": num, "titre": [], "partie": partie,
                   "partie_intitule": partie_i, "titre_division": titre,
                   "titre_division_intitule": titre_i, "divisions": list(divs),
                   "page": f, "page_fin": f, "_lignes": []}
            if vehicule == "plf" and ma.lastindex and ma.group(2).strip():
                cur["titre"].append(ma.group(2).strip())
            zone = "titre"
            continue
        if cur is None:
            continue
        if EDM.match(l):
            zone = "edm"; continue
        if zone == "edm":
            continue
        cur["page_fin"] = f
        if zone == "titre":
            creux = len(l) - len(l.lstrip())
            if l.strip() and not (vehicule == "plfss" and cur["titre"] and creux < 15):
                cur["titre"].append(l.strip()); continue
            if cur["titre"]:
                zone = "corps"
                if l.strip(): cur["_lignes"].append((l, f))
            continue
        cur["_lignes"].append((l, f))
    if cur: arts.append(cur)
    return arts


def rendre(pdf, vehicule, declaree, dest):
    lignes, npages, p0, p1 = lire(pdf, vehicule)
    arts = articles(lignes, vehicule)
    octets = open(pdf, "rb").read()
    tot_al = tot_ad = 0
    sortie = []
    for a in arts:
        al = alineas(a.pop("_lignes"))
        brut = "\n".join(x["texte"] for x in al)
        b = PO.blanchir(brut)
        refs = []
        for m in PO.ADRESSE.finditer(b):
            adr = PO.normalise(m.group("a"))
            pos = m.start()
            fin = b.find(".", pos); fin = len(b) if fin < 0 else fin
            pcs = pieces_nommees.trouver(b)
            suiv = next((n for s, e, n in pcs if pos < s < fin), None)
            prec = next((n for s, e, n in reversed(pcs) if s < pos), None)
            r = {"texte": suiv or prec or "indéterminé", "article": adr}
            if r not in refs: refs.append(r)
        a["titre"] = " ".join(a["titre"])
        a["nb_alineas"] = len(al)
        a["porte_tableau"] = any(x["tableau"] for x in al)
        a["alineas"] = al
        a["hors_alinea"] = []
        a["references"] = refs
        tot_al += len(al); tot_ad += len(refs)
        sortie.append({k: a[k] for k in ("numero", "titre", "partie", "partie_intitule",
                                         "titre_division", "titre_division_intitule",
                                         "divisions", "page", "page_fin", "nb_alineas",
                                         "porte_tableau", "alineas", "hors_alinea", "references")})
    socle_sha = hashlib.sha256(json.dumps(sortie, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    d = {"_revision": {
            "role": f"rédaction exacte des articles du texte déposé — {declaree}",
            "regle": "Verse ce que nulle autre source ne rend : la rédaction exacte des "
                     "articles, alinéa par alinéa, le hors-alinéa, et les adresses relevées "
                     "à la disposition. Le fichier se régénère intégralement depuis la pièce "
                     "nommée ci-dessous, et il n'ajoute rien qui ne s'y lise.",
            "piece": {"nom": pdf.rsplit("/", 1)[-1],
                      "sha256": hashlib.sha256(octets).hexdigest(),
                      "octets": len(octets), "pages": npages,
                      "acces": "document public, retéléchargeable à l'identique ; "
                               "aucune copie n'est jointe au fichier"},
            "extraction": {"profil": vehicule, "piece_declaree": declaree, "outil": OUTIL,
                           "version": subprocess.run(["pdftotext", "-v"], capture_output=True,
                                                     text=True).stderr.split("\n")[0],
                           "repere_debut": "Articles du projet de loi avec exposé des motifs"
                                            if vehicule == "plf" else "Article liminaire",
                           "repere_fin": "États législatifs annexés" if vehicule == "plf"
                                          else "fin de pièce",
                           "page_premiere": p0, "page_derniere": p1,
                           "marque_alinea": "paragraphe", "sommaire": vehicule == "plf",
                           "divisions_relevees": len({tuple(x["divisions"]) for x in sortie})},
            "socle_sha256": socle_sha,
            "champs_retires": {
                "redaction.lignes": "brut de mise en page ; `alineas` en est le reflux "
                                    "déterministe et porte le même verbatim",
                "expose_des_motifs": "de l'indice, pas de la norme : il raconte la "
                                     "disposition, il ne la décrit pas"},
            "articles": len(sortie), "alineas": tot_al, "adresses": tot_ad},
         "articles": sortie}
    json.dump(d, open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(dest, "|", len(sortie), "articles |", tot_al, "alinéas |", tot_ad, "adresses")


if __name__ == "__main__":
    rendre(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
