#!/usr/bin/env python3
"""Passe 3 — sources markdown du dossier de relecture et de l'annexe en trois colonnes,
pour l'export Word au gabarit du chantier (md2docx.js, profil presentation).

Tout chiffre se compte sur les pièces de passe 3 (revision/passe3/*.json), le bilan de
sobriété et le registre des arbitrages ; tout texte vient de droit.py (état 2029) ou des
pièces (cible). Rien n'est recopié à la main, hors les phrases d'explication des exemples.
Écrit :
  livrables/dossier_revision_penale_passe3.md
  livrables/trois_colonnes_penal_passe3.md
"""
import collections
import json
import pathlib
import re
import sys

CHANTIER = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CHANTIER.parent))
sys.path.insert(0, str(CHANTIER / "appareil"))
import code_cible_penal as ccp  # noqa: E402
import revision_penale as rp  # noqa: E402
from dossier_revision_penale_md import typo, cellule, resserrer, mil, NBSP  # noqa: E402

P3 = CHANTIER / "revision" / "passe3"
DEC = CHANTIER / "revision" / "decisions"
OUT = CHANTIER / "livrables"
REGISTRE = CHANTIER / "revision" / "registre_arbitrages_penal.md"
GRILLE = CHANTIER / "revision" / "grille_principes.json"
BILAN = CHANTIER / "referentiels" / "sobriete_penal_bilan.json"

BLOCS = (("cppL", "Code de procédure pénale, partie législative", 0.40),
         ("cppR", "Code de procédure pénale, partie réglementaire", 0.50),
         ("cp", "Code pénal", 0.25),
         ("penitentiaire", "Code pénitentiaire", 0.60))
NOMS = {"cpp": "du code de procédure pénale", "cp": "du code pénal", "penitentiaire": "du code pénitentiaire"}

# principes validés par l'auteur, avec la date (procédure et registre, sections 1)
VALIDES = {"P14": "validé 20261020", "P20": "validé 20261023", "P26": "validé 20261023",
           "P27": "validé 20261023"}

# libellés des verbes de la cible, au pluriel
VERBES_PL = {"G": "gardés", "S": "simplifiés", "R": "réécrits", "D": "partiellement déclassés",
             "M": "remontés à la loi", "C": "créés"}
DESTINS_PL = {"gardee": "gardées", "reprise": "reprises", "declassee": "déclassées", "abrogee": "abrogées"}

# technique, principes, avant, après ; l'effet se compte sur le principe propre de la technique (premier cité)
TECHNIQUES = (
    ("1. Outre-mer", "P3", "Les articles qui recopient le droit commun pour une collectivité.",
     "Une clause d'application par collectivité et une table d'adaptations ; les incriminations et privations de liberté restent hors table."),
    ("2. Une règle générale par matière", "P2, P23", "Délais, notifications, publicité, recours répétés article par article.",
     "Un article général, les exceptions listées : publicité à L. 1, notification à L. 1632-5, nullités et forclusion aux règles générales."),
    ("3. Procédures particulières", "P2", "Un régime complet par matière (terrorisme, criminalité organisée, santé, environnement).",
     "Un régime commun, la liste des matières qui y entrent, les seuls écarts propres."),
    ("4. Déclassement", "P1", "Modalités écrites dans la loi ou le décret en Conseil d'État.",
     "Les modalités descendent au décret, à l'arrêté ou au règlement type ; un droit de la personne reste au code avec sa limite."),
    ("5. Rappels et redites", "P20", "« Sans préjudice », « conformément à », articles miroirs d'un autre code.",
     "La redite tombe et renvoie à la règle qui la porte."),
    ("6. Phrase", "P23", "Phrases longues, plusieurs idées, plusieurs mots pour une notion.",
     "Une idée par phrase, le verbe au présent, un mot par notion."),
)

# (lot, code, numéro, explication) : principales réécritures, en deux colonnes
EXEMPLES = (
    ("lot_p322", "cpp", "L1", "Publicité (P26) : une règle unique pour tout le code. La chambre du conseil ne joue que dans les cas qu'elle énumère ; les huis clos particuliers disparaissent des articles qui les répétaient."),
    ("lot_p293", "cpp", "L1632-5", "Notification (P12, P20) : une clause générale vaut pour toute lettre recommandée du code et pour son équivalent électronique ; les formules répétées tombent."),
    ("lot_p056", "cp", "132-1", "Individualisation (P25, P14) : la peine se fixe selon les faits et la personne, dans les limites du barème, qui devient la référence."),
    ("lot_p264", "cpp", "L2221-15", "Anonymat des enquêteurs (P23) : une seule échelle de peines pour la révélation d'identité, les exceptions propres à chaque régime gardées, aucune peine perdue."),
    ("lot_p298", "cpp", "L7215-1", "Pourvoi en cassation (P2) : sept articles qui disaient chacun une issue du pourvoi en un seul."),
    ("lot_p120", "penitentiaire", "R412-96", "Santé au travail en détention (P20, P3) : les articles qui recopiaient le code du travail le visent, et chaque écart propre à la détention, dont la visite du mineur, est écrit."),
    ("lot_p321", "cpp", "D599", "Outre-mer (P3) : une clause d'application et sa table d'adaptations, chaque adaptation disant les mots qu'elle remplace."),
    ("lot_p328", "cpp", "R40-30", "Fichiers (P2, P25) : une journalisation commune à quatre traitements, qui garde la traçabilité de toute opération sur la plate-forme des interceptions."),
)

# sections de l'annexe en trois colonnes
ANNEXE = ("lot_p322", "lot_p106", "lot_p293", "lot_p278", "lot_p182", "lot_p189", "lot_p306")


def pieces():
    out = {}
    for f in sorted(P3.glob("*.json")):
        p = json.loads(f.read_text(encoding="utf-8"))
        d = DEC / f.name
        code = json.loads(d.read_text(encoding="utf-8"))["perimetre"]["code"] if d.exists() else "?"
        out[f.stem] = dict(p, code=code)
    return out


def comptes(ps):
    destins, verbes, retraits = collections.Counter(), collections.Counter(), collections.Counter()
    par_principe = collections.defaultdict(collections.Counter)
    ecarts = 0
    for p in ps.values():
        for v in p["phrases"].values():
            destins[v["destin"]] += 1
        for a in p["articles_cible"]:
            verbes[a["verbe"]] += 1
            for pr in re.findall(r"P\d+", a.get("principe", "")):
                par_principe[pr]["cible " + a["verbe"]] += 1
        for r in p["retires"]:
            retraits[r["verbe"]] += 1
            for pr in re.findall(r"P\d+", r.get("principe", "")):
                par_principe[pr]["retiré " + r["verbe"]] += 1
        ecarts += bool(p.get("ecart_volume", "").strip())
    return destins, verbes, retraits, par_principe, ecarts


def registre():
    """Lignes du registre : (section, n°, point, décision, principe, statut)."""
    out, section = [], ""
    for ligne in REGISTRE.read_text(encoding="utf-8").splitlines():
        if ligne.startswith("## "):
            section = ligne[3:].strip()
        elif re.match(r"\| \d+\.\d+ \|", ligne):
            c = [x.strip() for x in ligne.strip().strip("|").split("|")]
            if len(c) == 4:   # section 8 : n° | point | décision | statut
                c = [c[0], c[1], c[2], "", c[3]]
            out.append([section] + c[:5])
    return out


def court(t, n=900):
    """Cellule d'exemple bornée : au-delà de n signes, la suite devient « […] »."""
    if len(t) <= n:
        return t
    coupe = t.rfind(". ", 0, n)
    return t[:coupe + 1 if coupe > 0 else n] + "\n[…]"


def pct(x):
    return f"{x:+.0%}".replace("%", NBSP + "%").replace("-", "−")


def dossier(ps, bilan, textes):
    destins, verbes, retraits, par_pr, ecarts = comptes(ps)
    av = sum(v[0] for v in bilan["blocs"].values())
    ap = sum(v[1] for v in bilan["blocs"].values())
    art_av = sum(l["articles_2029"] for l in bilan["lots"])
    art_ap = sum(l["articles_cible"] for l in bilan["lots"])
    L = ["# Révision de la chaîne pénale", "",
         "### Passe 3 : sobriété — dossier de relecture, octobre 2026", "",
         typo(f"La passe 3 réécrit les trois codes de la chaîne pénale titre par titre : {len(ps)} titres, "
              "chacun réécrit en entier puis relu en adversaire sur les garanties et les abrogations. "
              "Chaque phrase de l'état du 1er janvier 2029 a un destin écrit : gardée, reprise, déclassée ou abrogée. "
              "Les paramètres entre crochets restent à arbitrer. Les décisions déléguées se soumettent ici à confirmation."), "",
         "## Statistiques", "",
         "<!-- colonnes : 0.40, 0.15, 0.15, 0.15, 0.15 -->", "| Bloc | Mots en 2029 | Mots cible | Variation | Cible |", "|---|---|---|---|---|"]
    for k, nom, c in BLOCS:
        a, b = bilan["blocs"][k]
        L.append(f"| {nom} | {mil(a)} | {mil(b)} | {pct(b / a - 1)} | {pct(-c)} |")
    L += [f"| **Ensemble** | **{mil(av)}** | **{mil(ap)}** | **{pct(ap / av - 1)}** | {pct(-0.45)} environ |", ""]
    tot = sum(destins.values())
    L += ["<!-- colonnes : 0.28, 0.72 -->", "| Indicateur | Valeur |", "|---|---|",
          f"| Titres réécrits | {len(ps)}, dont {ecarts} avec un dépassement du plafond motivé |",
          f"| Articles | {mil(art_av)} en 2029, {mil(art_ap)} dans la cible ({pct(art_ap / art_av - 1)}) |",
          f"| Articles retirés | {mil(retraits['F'])} fusionnés, {mil(retraits['A'])} abrogés |",
          "| Articles de la cible | " + ", ".join(f"{mil(verbes[v])} {VERBES_PL[v]}" for v in "GSRDMC" if verbes[v]) + " |",
          f"| Phrases de 2029 suivies | {mil(tot)} : " + ", ".join(
              f"{mil(destins[d])} {DESTINS_PL[d]}" for d in DESTINS_PL) + " |",
          "| Contrôles avant chaque versement | S1 traçabilité, S2 garanties, S3 volume, D1 à D5, C1 à C7 : 0 anomalie |",
          ""]
    L += [typo("*Lecture : la variation se mesure sur l'état du 1er janvier 2029, avant la passe 2. Un dépassement de plafond "
               "tient aux garanties à garder écrites (art. 34 et 66 C, vie privée, défense) ; il est motivé titre par titre.*"), ""]
    L += ["## Principes et effet avant / après", "",
          "<!-- colonnes : 0.17, 0.09, 0.24, 0.32, 0.18 -->", "| Technique | Principe | Avant | Après | Effet compté |", "|---|---|---|---|---|"]
    vus = set()
    for tech, pr, avant, apres in TECHNIQUES:
        propre = re.findall(r"P\d+", pr)[0]
        if propre in vus:
            e = "compté à la technique 2"
        else:
            vus.add(propre)
            eff = par_pr[propre]
            e = ", ".join(f"{mil(n)} {k.replace('retiré F', 'fusions').replace('retiré A', 'abrogations')}"
                          for k, n in eff.most_common() if k.startswith("retiré")) or "—"
        L.append(f"| **{tech}** | {pr} | {typo(avant)} | {typo(apres)} | {e} |")
    L += ["", typo("*Effet compté : articles retirés dont la décision cite le principe propre de la technique (le premier cité) ; un article qui en cite plusieurs compte pour chacun.*"), ""]
    L += ["# Principales réécritures", ""]
    for lot, code, num, expli in EXEMPLES:
        p = ps[lot]
        art = next(a for a in p["articles_cible"] if a["num"] == num)
        fus = [r["num"] for r in p["retires"] if r.get("vers") == num]
        avant = textes.get((code, num), ("", ""))[0]
        for f in fus:
            avant += "\n" + f"[{f}] " + textes.get((code, f), ("", ""))[0]
        a, b = resserrer(avant.strip(), art["texte"])
        a, b = court(a), court(b)
        titre = f"Article {rp.cite(num)} {NOMS[code]}" + (f" (avec {', '.join(rp.cite(x) for x in fus[:6])}{'…' if len(fus) > 6 else ''})" if fus else "")
        L += [f"## {typo(titre)}", "", typo(expli), "",
              "<!-- colonnes : 0.5, 0.5 -->", "| *État 2029* | *Texte cible* |", "|---|---|", f"| {cellule(a)} | {cellule(b)} |", ""]
    L += ["# Grille des principes", "", "<!-- colonnes : 0.07, 0.75, 0.18 -->", "| n° | Principe | Statut |", "|---|---|---|"]
    for p in json.loads(GRILLE.read_text(encoding="utf-8"))["principes"]:
        L.append(f"| {p['id']} | {typo(p['enonce'])} | {VALIDES.get(p['id'], 'à confirmer')} |")
    L += ["", typo("*Les lignes 1.1 à 1.5 du registre citent P4 et P5 au sens du barème ; la grille range le barème sous P14.*"), ""]
    L += ["# Registre des arbitrages délégués", "",
          typo("Une ligne par décision déléguée, à confirmer ou révoquer. Les décisions validées par l'auteur n'y figurent pas."), "",
          "<!-- corps : 16 -->", "<!-- colonnes : 0.07, 0.12, 0.69, 0.12 -->", "| n° | Point | Décision | Principe |", "|---|---|---|---|"]
    for sec, n, point, dec, pr, statut in registre():
        if statut.startswith("délégué"):
            L.append(f"| {n} | {typo(point)} | {typo(dec)} | {pr} |")
    return "\n".join(L) + "\n"


def annexe(ps, textes):
    L = ["**RÉVISION DE LA CHAÎNE PÉNALE — PASSE 3**", "", "*Annexe en trois colonnes*", "",
         "État au 1er janvier 2029, texte cible et motif", "", "Base LEGI du 20 octobre 2026", "", "---", ""]
    for lot in ANNEXE:
        p = ps[lot]
        code = p["code"]
        L += [f"## {typo(p['titre'])}", "", "<!-- colonnes : 0.37, 0.37, 0.26 -->", "| *État 2029* | *Texte cible* | *Motif* |", "|---|---|---|"]
        ret = collections.defaultdict(list)
        for r in p["retires"]:
            ret[r.get("vers") or ""].append(r)
        for a in p["articles_cible"]:
            t29 = textes.get((code, a["num"]), ("", ""))[0]
            av = f"**{a['num']}**<br>" + (cellule(t29) if t29 else "*(article nouveau)*")
            L.append(f"| {av} | **{a['num']}**<br>{cellule(a['texte'])} | {typo(a.get('motif', ''))} |")
            for r in ret.get(a["num"], []):
                L.append(f"| **{r['num']}**<br>{cellule(textes.get((code, r['num']), ('', ''))[0])} | *Fusionné dans {a['num']}* | {typo(r.get('motif', ''))} |")
        for r in ret.get("", []):
            L.append(f"| **{r['num']}**<br>{cellule(textes.get((code, r['num']), ('', ''))[0])} | *Abrogé* | {typo(r.get('motif', ''))} |")
        nums = {a["num"] for a in p["articles_cible"]}
        for v, rs in ret.items():
            if v and v not in nums:
                for r in rs:
                    L.append(f"| **{r['num']}**<br>{cellule(textes.get((code, r['num']), ('', ''))[0])} | *Fusionné dans {v}* | {typo(r.get('motif', ''))} |")
        L.append("")
    return "\n".join(L)


def main():
    ps = pieces()
    bilan = json.loads(BILAN.read_text(encoding="utf-8"))
    textes = ccp.textes_2029()
    (OUT / "dossier_revision_penale_passe3.md").write_text(dossier(ps, bilan, textes), encoding="utf-8")
    (OUT / "trois_colonnes_penal_passe3.md").write_text(annexe(ps, textes), encoding="utf-8")


if __name__ == "__main__":
    main()
