import re, pathlib, sys, collections
SRC = pathlib.Path(sys.argv[1])
lignes = SRC.read_text(encoding="utf-8").split("\n")

# bornes des trois colonnes (1-indexées au grep : 15, 2389, 4135, fin 4721)
def section(deb, fin):
    bloc = lignes[deb-1:fin]
    # on part du premier titre d'amendement
    i = next(k for k,l in enumerate(bloc) if l.startswith("## "))
    return bloc[i:]

COL = {"P1": section(15, 2388), "P2": section(2389, 4134), "SS": section(4135, 4721)}

RE_T = re.compile(r"^## ([A-Z0-9]+-[0-9]+) — (.+)$")

def lettrer(bloc):
    rangs = [RE_T.match(l).group(1) for l in bloc if RE_T.match(l)]
    c = collections.Counter(rangs)
    vus = collections.Counter()
    out, toc = [], []
    accroche = None
    for l in bloc:
        m = RE_T.match(l)
        if m:
            r, titre = m.group(1), m.group(2)
            if c[r] > 1:
                vus[r] += 1
                r = f"{r} {chr(96+vus[r])}"
            out.append(f"## {r} — {titre}")
            toc.append([r, titre, None])
            accroche = len(toc) - 1
            continue
        if accroche is not None and toc[accroche][2] is None and l.startswith("*") and l.endswith("*") and len(l) > 2:
            toc[accroche][2] = l.strip("*")
        out.append(l)
    return out, toc

NOMS = {"P1": "PLF 2027 — première partie", "P2": "PLF 2027 — seconde partie", "SS": "PLFSS 2027"}
FRONT = {"P1": "front_p1.md", "P2": "front_p2.md", "SS": "front_ss.md"}
mesure = {}

for k, bloc in COL.items():
    corps, toc = lettrer(bloc)
    texte = "\n".join(corps).strip("\n")
    texte = re.sub(r"(?m)^\\newpage$", "---", texte)
    tdm = [f"# Table des matières — {NOMS[k]}", "",
           "| rang | titre | accroche au texte déposé |", "|---|---|---|"]
    for r, titre, acc in toc:
        tdm.append(f"| **{r}** | {titre} | {acc or ''} |")
    doc = (pathlib.Path(FRONT[k]).read_text(encoding="utf-8").strip("\n")
           + "\n\n---\n\n" + texte + "\n\n---\n\n" + "\n".join(tdm) + "\n")
    pathlib.Path(f"liasse_{k.lower()}.md").write_text(doc, encoding="utf-8")
    mesure[k] = (len(set(r.split(" ")[0] for r, _, _ in toc)), len(toc))
    print(k, "rangs", mesure[k][0], "| amendements", mesure[k][1], "| sauts", doc.count("\n---\n"))
