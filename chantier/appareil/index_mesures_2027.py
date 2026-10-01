#!/usr/bin/env python3
"""Index des mesures d'un texte financier, avec ses cinq relevés transversaux.

Le défaut qu'il corrige : l'index de lecture tronque chaque mesure, si bien que
tout comptage portant sur une formule — renvoi au décret, entrée en vigueur,
mot de portée, borne temporelle, siège abrogé — rendait un plancher sans pouvoir
dire de combien. Les relevés se calculent ici, une fois, sur le texte entier ;
toute lecture transversale ultérieure se fait sur ce seul fichier.

Il se joint à l'index de lecture par la référence de mesure (« 19.3 »).
"""
import json, re, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import portes_ouvertes as PO

# --- découpage en mesures : deux niveaux, gardes d'ordre et de rang ----------
N1 = re.compile(r'(?m)^\s*(?P<m>(?:[IVX]+|\d+°|[A-H])\s*[.–\-])\s')
N2 = re.compile(r'(?m)^\s*(?P<m>(?:\d+°|[a-h]\)|[A-H]\s*[.–\-]))\s')

# --- les cinq relevés ---------------------------------------------------------
RENVOI = re.compile(
    r"(?:par (?:un )?décret(?: en Conseil d[’']État)?|par (?:un )?arrêté"
    r"|(?:un |le )?décret(?: en Conseil d[’']État)? (?:fixe|détermine|précise|prévoit)"
    r"|(?:un |l[’'])?arrêté (?:fixe|détermine|précise|conjoint)"
    r"|dans des conditions (?:fixées|définies|prévues) par (?:décret|arrêté|voie réglementaire)"
    r"|par voie réglementaire)", re.I)
ENTREE = re.compile(
    r"(?:entre(?:nt)? en vigueur le |à compter du |applicables? (?:à compter du|au) )"
    r"(?P<d>1er |\d{1,2} )?(?P<r>janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)?\s*(?P<a>\d{4})",
    re.I)
PORTEE = ["peut", "peuvent", "dans la limite de", "à compter de", "au titre de",
          "par dérogation", "notamment", "nonobstant", "sans préjudice",
          "le cas échéant", "au plus"]
BORNE = re.compile(
    r"(?:jusqu[’']au |au plus tard le |pour une durée de |au titre des années |"
    r"entre le .{0,40}? et le |jusqu[’']à (?:l[’']expiration|la date))", re.I)
ABROGE = re.compile(r"(?:est|sont) (?:abrogés?|abrogées?|supprimés?|supprimées?)", re.I)


def mesures(art):
    """Une mesure = la subdivision la moins profonde sous laquelle un seul siège
    de droit est modifié. Profondeur bornée à deux niveaux (règle 2)."""
    d = art["dispositif"]
    cs = [m.start() for m in N1.finditer(d)]
    blocs = []
    if not cs:
        blocs = [(d, "")]
    else:
        if cs[0] > 0:
            blocs.append((d[:cs[0]], ""))
        for i, s in enumerate(cs):
            f = cs[i + 1] if i + 1 < len(cs) else len(d)
            blocs.append((d[s:f], N1.match(d, s).group("m").strip(" .–-")))
    out = []
    for texte, rang in blocs:
        ss = [m.start() for m in N2.finditer(texte)]
        ss = [s for s in ss if s > 0]
        if not ss:
            out.append((rang, texte))
            continue
        out.append((rang, texte[:ss[0]]))
        for i, s in enumerate(ss):
            f = ss[i + 1] if i + 1 < len(ss) else len(texte)
            sous = N2.match(texte, s).group("m").strip(" .–-)")
            out.append((f"{rang}.{sous}" if rang else sous, texte[s:f]))
    return [(r, t) for r, t in out if t.strip()]


def releves(t):
    """Les cinq relevés se lisent sur le texte ENTIER, passages insérés compris :
    un « par décret » placé dans un alinéa que la mesure insère est un renvoi
    réglementaire réel, c'est même la forme la plus courante. Le blanchiment des
    passages cités ne sert qu'au relevé des sièges, où citer n'est pas ouvrir."""
    ren = sorted({" ".join(m.group(0).split()).lower() for m in RENVOI.finditer(t)})
    ev = sorted({" ".join(x for x in (m.group("d"), m.group("r"), m.group("a")) if x).strip()
                 for m in ENTREE.finditer(t)})
    po = sorted({p for p in PORTEE if re.search(r"\b" + re.escape(p) + r"\b", t, re.I)})
    bo = sorted({" ".join(m.group(0).split()).lower() for m in BORNE.finditer(t)})
    ab = bool(ABROGE.search(t))
    b = PO.blanchir(t)
    sieges = sorted({PO.normalise(m.group("a")) for m in PO.ADRESSE.finditer(b)})
    return ren, ev, po, bo, ab, sieges


def rendre(socle, vehicule, dest):
    n = 0
    with open(dest, "w", encoding="utf-8") as f:
        f.write(f"# INDEX DES MESURES ET RELEVÉS TRANSVERSAUX — {vehicule.upper()} 2027\n"
                "# Se joint à l'index de lecture par la colonne `mesure`.\n"
                "# Les cinq relevés sont calculés sur le texte entier de la mesure : un\n"
                "# comptage fait ici est un total, jamais un plancher.\n"
                f"# pièce : sha256 {socle['pdf_sha256']}\n"
                "# colonnes : mesure<TAB>article<TAB>partie<TAB>folio<TAB>sieges"
                "<TAB>renvoi_reglementaire<TAB>entree_en_vigueur<TAB>mots_de_portee"
                "<TAB>borne_temporelle<TAB>siege_abroge<TAB>caracteres\n#\n")
        for art in socle["articles"]:
            for i, (rang, texte) in enumerate(mesures(art), 1):
                ren, ev, po, bo, ab, si = releves(texte)
                ref = f"{art['numero']}.{rang}" if rang else f"{art['numero']}.{i}"
                p = (art["partie"] or "").split(":")[0].strip().lower()
                f.write("\t".join([ref, art["numero"], p, str(art["folio_debut"]),
                                   " ; ".join(si), " ; ".join(ren), " ; ".join(ev),
                                   " ; ".join(po), " ; ".join(bo),
                                   "oui" if ab else "non", str(len(texte))]) + "\n")
                n += 1
    return n


if __name__ == "__main__":
    s = json.load(open(sys.argv[1], encoding="utf-8"))
    n = rendre(s, sys.argv[2], sys.argv[3])
    print(sys.argv[3], "|", n, "mesures")
