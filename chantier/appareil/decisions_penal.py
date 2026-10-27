#!/usr/bin/env python3
"""Passe 2 — contrôle des décisions article par article.

Lit revision/decisions/*.json et le registre de la passe 1, et vérifie, lot par lot :

  D1  couverture : chaque article du périmètre du lot porte une décision, dans ce
      lot ou dans un autre ; un article ne porte qu'une décision dans tout le corpus
  D2  forme : verbe connu, principe de la grille, motif non vide, ligne rouge renseignée
  D3  opérations : pour S, R, D, les opérations s'appliquent (contrôles C2 et C3 de
      revision_penale.py) ; A et G n'en portent pas ; F nomme sa destination
  D4  renvois : tout article abrogé ou fusionné qui est cité ailleurs dans le
      périmètre est listé, avec les articles à coordonner ; un renvoi d'un autre code ne
      compte que si le texte nomme le code de l'article cité
  D5  ligne rouge : un article signalé en passe 1 (liberté, nullité, peine) porte
      une ligne rouge explicitement examinée
  D6  délits (revision/bareme/*.json) : le délit figure au barème, la décision est
      du vocabulaire, le principe de la grille, le motif non vide, et le TSV
      régénéré par bareme_delits.py porte la même décision

Sorties : referentiels/decisions_penal_bilan.json, et le tableau de bord par lot
sur la sortie standard. Échoue (--strict) sur toute anomalie.
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
GRILLE = CHANTIER / "revision" / "grille_principes.json"
VERBES = set("GSFADMRC")
BAREME = CHANTIER / "referentiels" / "bareme_delits.tsv"
DEC_DELITS = CHANTIER / "revision" / "bareme"
VERBES_DELITS = {"garder", "relever", "amende délictuelle", "contravention C5",
                 "sanction administrative", "abroger"}
NOMS_CODES = {"cpp": "code de procédure pénale", "cp": "code pénal", "penitentiaire": "code pénitentiaire"}
RE_PREFIXE = re.compile(r"\b(?:L|R|D|A)\.\s?\d+(?:-\d+)*")
RE_LISTE = re.compile(r"articles? (\d+(?:-\d+)*(?:(?:, | et | à | ou )\d+(?:-\d+)*)*)")


def renvois(t):
    """Tous les numéros cités : préfixés (L. 5251-1) et listes d'anciens numéros (720, 720-1 et 721)."""
    out = {x.replace(" ", "") for x in RE_PREFIXE.findall(t)}
    for m in RE_LISTE.findall(t):
        out |= set(re.findall(r"\d+(?:-\d+)*", m))
    return out


def main():
    strict = "--strict" in sys.argv
    reg = list(csv.DictReader(REG.open(encoding="utf-8"), delimiter="\t"))
    parcle = {(r["code"], r["num"]): r for r in reg}
    grille = {p["id"] for p in json.loads(GRILLE.read_text(encoding="utf-8"))["principes"]}
    anomalies, lots = [], []
    textes = {}
    for code in ("cpp", "cp", "penitentiaire"):
        for vs in droit.charger(code).values():
            j = "2029-01-01"   # les trois codes se jugent dans leur version coordonnée par l'ordonnance n° 2025-1091
            ap = [v for v in vs if droit.applicable(v, j)]
            if ap:
                textes[(code, ap[-1]["num"])] = (ap[-1]["texte"] or "", ap[-1].get("section") or "")
    # les renvois de chaque texte, normalisés une fois pour tous les lots
    refs = {k: [droit.norm_num(x) for x in renvois(t)] for k, (t, _) in textes.items()}
    partout = collections.defaultdict(list)
    for f in sorted(DEC.glob("*.json")):
        for d in json.loads(f.read_text(encoding="utf-8"))["decisions"]:
            partout[(d["code"], d["num"])].append(f.name)
    for (c, n), fs in partout.items():
        if len(fs) > 1:
            anomalies.append(f"D1 : {c} {n} jugé dans {len(fs)} lots : {', '.join(fs)}")
    for f in sorted(DEC.glob("*.json")):
        lot = json.loads(f.read_text(encoding="utf-8"))
        per = lot["perimetre"]
        attendus = {(c, n) for (c, n), (t, s) in textes.items()
                    if c == per["code"] and per["section_contient"] in s and n.startswith(per.get("prefixe", ""))
                    and (c, n) in parcle}   # le registre de passe 1 est le périmètre de la réécriture
        decides = {(d["code"], d["num"]): d for d in lot["decisions"]}
        manq = {k for k in attendus - set(decides) if k not in partout}
        if manq:
            anomalies.append(f"{f.name} D1 : {len(manq)} article(s) sans décision : {sorted(n for _, n in manq)[:8]}")
        cpt = collections.Counter()
        retires = []
        for (c, n), d in decides.items():
            cpt[d["decision"]] += 1
            if d["decision"] == "C":   # création : un numéro libre, rédigé en entier
                if (c, n) in textes:
                    anomalies.append(f"{f.name} D2 : {c} {n} créé alors qu'il existe")
                if [op.get("op") for op in d.get("operations", [])] != ["rediger"]:
                    anomalies.append(f"{f.name} D3 : {n} création sans rédaction unique")
            elif (c, n) not in parcle:
                anomalies.append(f"{f.name} D2 : {c} {n} absent du registre")
            if d["decision"] not in VERBES:
                anomalies.append(f"{f.name} D2 : {n} verbe inconnu {d['decision']}")
            if d.get("principe") not in grille:
                anomalies.append(f"{f.name} D2 : {n} principe {d.get('principe')} hors grille")
            if not d.get("motif", "").strip():
                anomalies.append(f"{f.name} D2 : {n} sans motif")
            if not d.get("ligne_rouge", "").strip():
                anomalies.append(f"{f.name} D2 : {n} ligne rouge non renseignée")
            r = parcle.get((c, n), {})
            if r.get("ligne_rouge") and d.get("ligne_rouge", "").strip().lower() == "aucune":
                anomalies.append(f"{f.name} D5 : {n} signalé ({r['ligne_rouge'][:40]}) mais déclaré sans ligne rouge")
            ops = d.get("operations", [])
            if d["decision"] in "SRD" and not ops:
                anomalies.append(f"{f.name} D3 : {n} décision {d['decision']} sans opération")
            if d["decision"] in "AG" and ops:
                anomalies.append(f"{f.name} D3 : {n} décision {d['decision']} avec opérations")
            if d["decision"] == "F" and not d.get("vers"):
                anomalies.append(f"{f.name} D3 : {n} fusion sans destination")
            t = textes.get((c, n), ("", ""))[0]
            for op in ops:
                try:
                    t, _ = rp.appliquer(t, op)
                except rp.Anomalie as e:
                    anomalies.append(f"{f.name} D3 : {n} {e}")
            if d["decision"] in "AF":
                retires.append((c, n))
        # D4 : renvois vers les articles retirés, hors du lot lui-même
        coord = collections.defaultdict(list)
        cibles = {droit.norm_num(n): (c, n) for c, n in retires}
        for c, n in retires:   # l'ancien numéro, cité par la partie réglementaire
            anc = parcle.get((c, n), {}).get("num_actuel")
            if anc:
                cibles.setdefault(droit.norm_num(anc), (c, f"{n} (ancien {anc})"))
        for (c, n), (t, _) in textes.items():
            if (c, n) in decides:
                continue
            for k in refs[(c, n)]:
                # un renvoi vers un autre code ne compte que si le texte nomme ce code (registre 8.4)
                if k in cibles and (cibles[k][0] == c or NOMS_CODES[cibles[k][0]] in t):
                    coord[cibles[k][1]].append(n)
        lots.append({"lot": f.name, "attendus": len(attendus), "decides": len(decides),
                     "decisions": dict(cpt), "a_coordonner": {k: sorted(v) for k, v in coord.items()}})
    bar = {(r["code"], r["num"]): r for r in csv.DictReader(BAREME.open(encoding="utf-8"), delimiter="\t")}
    delits = collections.Counter()
    for f in sorted(DEC_DELITS.glob("*.json")):
        for d in json.loads(f.read_text(encoding="utf-8"))["decisions"]:
            k, n = (d["code"], d["num"]), f"{d['code']} {d['num']}"
            delits[d["decision"]] += 1
            if k not in bar:
                anomalies.append(f"{f.name} D6 : {n} absent du barème")
            elif bar[k]["decision"] != d["decision"] or bar[k]["motif"] != d.get("motif", ""):
                anomalies.append(f"{f.name} D6 : {n} — le TSV ne porte pas la décision, rejouer bareme_delits.py")
            if d["decision"] not in VERBES_DELITS:
                anomalies.append(f"{f.name} D6 : {n} décision inconnue {d['decision']}")
            if d.get("principe") not in grille:
                anomalies.append(f"{f.name} D6 : {n} principe {d.get('principe')} hors grille")
            if not d.get("motif", "").strip():
                anomalies.append(f"{f.name} D6 : {n} sans motif")
    couverture = sum(l["decides"] for l in lots)
    out = {"articles_registre": len(reg), "decides": couverture,
           "part_jugee": round(couverture / len(reg), 4), "lots": lots,
           "delits": {"au_bareme": len(bar), "decides": sum(delits.values()), "decisions": dict(delits)},
           "anomalies": anomalies}
    (CHANTIER / "referentiels" / "decisions_penal_bilan.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for l in lots:
        print(f"{l['lot']} : {l['decides']}/{l['attendus']} jugés, {l['decisions']}")
        for k, v in l["a_coordonner"].items():
            print(f"   {k} est cité par {len(v)} article(s) : {', '.join(v[:10])}")
    print(f"délits : {sum(delits.values())}/{len(bar)} jugés, {dict(delits)}")
    print(f"registre : {couverture}/{len(reg)} articles jugés ({out['part_jugee']:.2%}), {len(anomalies)} anomalie(s)")
    for a in anomalies:
        print("  ANOMALIE", a)
    if strict and anomalies:
        sys.exit(1)


if __name__ == "__main__":
    main()
