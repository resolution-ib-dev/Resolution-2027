#!/usr/bin/env python3
"""Passe 2 — produits finaux de la réécriture complète.

Lit le registre de la passe 1, les décisions de revision/decisions/*.json et le
texte des trois codes (droit.py), applique les opérations (revision_penale.py) et
écrit :

  livrables/code_cible_penal.md          le code cible complet, dans l'ordre des codes
  referentiels/trois_colonnes_penal.tsv  ancien | 2029 | cible, avec verbe, principe et motif
  referentiels/concordance_penale.tsv    numéro actuel → numéro 2029 → numéro cible
  referentiels/code_cible_penal_bilan.json  articles et mots avant et après, par code et par verbe

Aucun texte cible ne s'écrit à la main : il se dérive des opérations. Les trois
codes se lisent dans leur version du 1er janvier 2029 (ordonnance n° 2025-1091),
la colonne « ancien » dans la version du jour.
"""
import collections
import csv
import json
import pathlib
import re
import sys

CHANTIER = pathlib.Path(__file__).resolve().parents[1]
RACINE = CHANTIER.parent
sys.path.insert(0, str(RACINE))
sys.path.insert(0, str(CHANTIER / "appareil"))
import droit  # noqa: E402
import revision_penale as rp  # noqa: E402

REG = CHANTIER / "referentiels" / "registre_penal.tsv"
DEC = CHANTIER / "revision" / "decisions"
J2029 = "2029-01-01"
CODES = (("cpp", "Code de procédure pénale"), ("cp", "Code pénal"), ("penitentiaire", "Code pénitentiaire"))
VERBES = {"G": "gardé", "S": "simplifié", "R": "réécrit", "F": "fusionné", "A": "abrogé",
          "D": "déclassé", "M": "remonté à la loi", "C": "créé"}
PREFIXES = {"L": 0, "R": 1, "D": 2, "A": 3}


def cle(num):
    """Ordre du code : préfixe de partie, puis numéros en entiers."""
    m = re.match(r"([A-Z]*)\*?(.*)", num)
    pre, reste = m.group(1), m.group(2)
    return (PREFIXES.get(pre, 4 if pre else -1),
            [(0, int(x), "") if x.isdigit() else (1, 0, x) for x in re.split(r"[-.]", reste) if x])


def mots(t):
    return len(re.findall(r"\w+", t or ""))


def textes_2029():
    out = {}
    for code, _ in CODES:
        for vs in droit.charger(code).values():
            ap = [v for v in vs if droit.applicable(v, J2029)]
            if ap:
                out[(code, ap[-1]["num"])] = (ap[-1]["texte"] or "", ap[-1].get("section") or "")
    return out


def texte_actuel(code, num):
    try:
        return droit.article(code, num)["texte"] or ""
    except Exception:
        return ""


def cible(d, t):
    """Texte cible et mention d'état, dérivés de la décision."""
    for op in d.get("operations", []):
        t, _ = rp.appliquer(t, op)
    v = d["decision"]
    if v == "A":
        return "", "abrogé"
    if v == "F":
        return "", f"fusionné dans {d.get('vers', '')}".strip()
    if v == "D":
        return t, "partie réglementaire déclassée"
    if v == "M":
        return t, "remonte à la loi"
    return t, ""


def main():
    reg = {(r["code"], r["num"]): r for r in csv.DictReader(REG.open(encoding="utf-8"), delimiter="\t")}
    dec = {}
    for f in sorted(DEC.glob("*.json")):
        for d in json.loads(f.read_text(encoding="utf-8"))["decisions"]:
            dec[(d["code"], d["num"])] = dict(d, lot=f.stem)
    textes = textes_2029()
    lignes, bilan = [], {}
    md = ["# Code cible de la chaîne pénale", "",
          "Texte dérivé des décisions de la passe 2 appliquées au texte en vigueur au 1er janvier 2029. "
          "Les paramètres entre crochets sont à arbitrer. Un article abrogé ou fusionné est mentionné à sa place.", ""]
    for code, titre in CODES:
        cles = sorted({k for k in list(reg) + list(dec) if k[0] == code}, key=lambda k: cle(k[1]))
        stat = {"articles_avant": 0, "articles_apres": 0, "mots_avant": 0, "mots_apres": 0,
                "par_verbe": collections.Counter()}
        md += [f"## {titre}", ""]
        section = None
        for k in cles:
            n = k[1]
            r = reg.get(k, {})
            d = dec.get(k)
            t29, sec = textes.get(k, ("", r.get("section", "")))
            anc_num = r.get("num_actuel", "") if code == "cpp" else n
            t_anc = texte_actuel(code, anc_num) if anc_num else ""
            if d is None:
                continue
            tc, etat = cible(d, t29)
            v = d["decision"]
            stat["par_verbe"][v] += 1
            if v != "C":
                stat["articles_avant"] += 1
                stat["mots_avant"] += mots(t29)
            if v not in "AF":
                stat["articles_apres"] += 1
                stat["mots_apres"] += mots(tc)
            if sec and sec != section:
                md += [f"### {sec}", ""]
                section = sec
            md.append(f"**Article {n}**" + (f" — *{etat}*" if etat else ""))
            md.append("")
            if tc:
                md += [a.strip() for a in tc.split("\n") if a.strip()]
                md.append("")
            num_cible = "" if v == "A" else (d.get("vers", "") if v == "F" else n)
            lignes.append({"code": code, "num_actuel": anc_num, "num_2029": "" if v == "C" else n,
                           "num_cible": num_cible, "decision": v, "principe": d.get("principe", ""),
                           "lot": d["lot"], "texte_actuel": t_anc, "texte_2029": t29, "texte_cible": tc,
                           "motif": d.get("motif", ""), "ligne_rouge": d.get("ligne_rouge", "")})
        stat["par_verbe"] = dict(stat["par_verbe"])
        bilan[code] = stat
    def plat(x):
        return (x or "").replace("\t", " ").replace("\r", "").replace("\n", " ¶ ")
    champs = ["code", "num_actuel", "num_2029", "num_cible", "decision", "principe", "lot",
              "texte_actuel", "texte_2029", "texte_cible", "motif", "ligne_rouge"]
    with (CHANTIER / "referentiels" / "trois_colonnes_penal.tsv").open("w", encoding="utf-8", newline="") as fh:
        fh.write("\t".join(champs) + "\n")
        for l in lignes:
            fh.write("\t".join(plat(l[c]) for c in champs) + "\n")
    with (CHANTIER / "referentiels" / "concordance_penale.tsv").open("w", encoding="utf-8", newline="") as fh:
        fh.write("code\tnum_actuel\tnum_2029\tnum_cible\tdecision\tprincipe\n")
        for l in lignes:
            fh.write("\t".join(l[c] for c in ("code", "num_actuel", "num_2029", "num_cible", "decision", "principe")) + "\n")
    (CHANTIER / "livrables" / "code_cible_penal.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    tot = {k: sum(b[k] for b in bilan.values()) for k in ("articles_avant", "articles_apres", "mots_avant", "mots_apres")}
    tot["par_verbe"] = dict(sum((collections.Counter(b["par_verbe"]) for b in bilan.values()), collections.Counter()))
    bilan["total"] = tot
    (CHANTIER / "referentiels" / "code_cible_penal_bilan.json").write_text(
        json.dumps(bilan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for c, b in bilan.items():
        print(f"{c} : {b['articles_avant']} → {b['articles_apres']} articles, "
              f"{b['mots_avant']} → {b['mots_apres']} mots, {b['par_verbe']}")


if __name__ == "__main__":
    main()
