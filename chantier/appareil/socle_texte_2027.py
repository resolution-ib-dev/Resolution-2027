#!/usr/bin/env python3
"""Socle d'un texte financier 2027 — extraction déterministe.

Une entrée par article : numéro, partie, titre, intitulé, rédaction exacte,
folio imprimé, exposé des motifs rattaché. Même PDF, même script, même JSON.
"""
import hashlib, json, re, subprocess, sys

GAB = {
    "plf": {
        "art":    re.compile(r'^\s*ARTICLE\s+(liminaire|\d+(?:\s+(?:bis|ter|quater))?)\s*:\s*(.*)$'),
        "folio":  re.compile(r'^\s*(?:Projet de loi de finances\s+(\d+)|(\d+)\s+Projet de loi de finances)\s*$'),
        "partie": re.compile(r'^\s*((?:PREMIÈRE|SECONDE|DEUXIÈME|TROISIÈME|TROISIEME|QUATRIÈME|QUATRIEME)\s+PARTIE\b.*)$'),
        "titre":  re.compile(r'^\s*(TITRE\s+[A-ZÉÈÀÂÎÔÛPREMIER0-9IVX][^a-z]*)$'),
    },
    "plfss": {
        "art":    re.compile(r'^\s*Article\s+(liminaire|\d+(?:er)?(?:\s+(?:bis|ter))?)\s*$'),
        "folio":  re.compile(r'^\s*NOR\s*:.*?(\d+)\s*/\s*\d+\s*$'),
        "partie": re.compile(r'^\s*((?:PREMIÈRE|SECONDE|DEUXIÈME|TROISIÈME|TROISIEME|QUATRIÈME|QUATRIEME)\s+PARTIE\b.*)$'),
        "titre":  re.compile(r'^\s*(TITRE\s+[IVX]+[^a-z]*)$'),
    },
}
EDM = re.compile(r'^\s*Exposé des motifs\s*$')


def pages(pdf):
    txt = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", pdf, "-"],
                         capture_output=True, text=True, check=True).stdout
    return txt.split("\f")


DEBUT = {"plf": re.compile(r'^\s*Articles du projet de loi avec exposé des motifs\s*$'),
         "plfss": None}


def socle(pdf, vehicule):
    g = GAB[vehicule]
    lignes = []          # (texte, folio)
    folio = None
    ouvert = DEBUT[vehicule] is None
    for i, p in enumerate(pages(pdf), 1):
        if not ouvert:
            if any(DEBUT[vehicule].match(l) for l in p.split("\n")):
                ouvert = True
            continue
        head = p.split("\n")[:1]
        m = g["folio"].match(head[0]) if head else None
        if m:
            folio = int(next(x for x in m.groups() if x))
            corps = p.split("\n")[1:]
        else:
            folio = folio if folio is not None else i
            corps = p.split("\n")
        for l in corps:
            lignes.append((l, folio))

    arts, cur, partie, titre = [], None, None, None
    zone = None
    suite_partie = False
    for l, f in lignes:
        # un intitule de partie se poursuit sur les lignes capitales suivantes
        if suite_partie:
            s = l.strip()
            if s and s == s.upper() and not g["art"].match(l) and not g["titre"].match(l):
                partie = partie + " " + " ".join(s.split())
                continue
            suite_partie = False
        mp = g["partie"].match(l)
        if mp:
            partie = " ".join(mp.group(1).split()); titre = None
            suite_partie = True
            if cur:
                cur["_partie_suivante"] = partie
        mt = g["titre"].match(l)
        if mt and len(l.strip()) > 6:
            titre = " ".join(mt.group(1).split())
        ma = g["art"].match(l)
        if ma:
            if cur:
                arts.append(cur)
            cur = {"numero": re.sub(r"^(\d+)er$", r"\1", " ".join(ma.group(1).split())), "partie": partie, "titre": titre,
                   "intitule": [], "dispositif": [], "expose_des_motifs": [],
                   "folio_debut": f, "folio_fin": f}
            if vehicule == "plf" and ma.lastindex and ma.group(2).strip():
                cur["intitule"].append(ma.group(2).strip())
            zone = "intitule"
            continue
        if cur is None:
            continue
        cur["folio_fin"] = f
        if EDM.match(l):
            zone = "expose_des_motifs"; continue
        if zone == "intitule":
            # fin d'intitule : ligne vide, ou — gabarit PLFSS — ligne de corps,
            # reconnue a son retrait faible la ou le titre est centre.
            creux = len(l) - len(l.lstrip())
            if l.strip() and not (vehicule == "plfss" and cur["intitule"] and creux < 15):
                cur["intitule"].append(l.strip())
                continue
            if cur["intitule"]:
                zone = "dispositif"
                if l.strip():
                    cur["dispositif"].append(l.rstrip())
            continue
        cur[zone].append(l.rstrip())
    if cur:
        arts.append(cur)

    for a in arts:
        a.pop("_partie_suivante", None)
        a["intitule"] = " ".join(a["intitule"])
        for k in ("dispositif", "expose_des_motifs"):
            a[k] = "\n".join(a[k]).strip("\n")
    return arts


def main(pdf, vehicule, out):
    arts = socle(pdf, vehicule)
    emp = hashlib.sha256(open(pdf, "rb").read()).hexdigest()
    d = {"vehicule": vehicule, "pdf_sha256": emp, "articles": arts,
         "comptes": {"articles": len(arts),
                     "sans_intitule": sum(1 for a in arts if not a["intitule"]),
                     "sans_dispositif": sum(1 for a in arts if not a["dispositif"]),
                     "sans_edm": sum(1 for a in arts if not a["expose_des_motifs"])}}
    d["sha256_json"] = hashlib.sha256(
        json.dumps(d["articles"], ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    json.dump(d, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(out, d["comptes"], "json_sha256", d["sha256_json"][:16])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
