#!/usr/bin/env python3
"""Passe 2 — contrôle des décisions article par article.

Lit revision/decisions/*.json et le registre de la passe 1, et vérifie, lot par lot :

  D1  couverture : chaque article du périmètre du lot porte une décision
  D2  forme : verbe connu, principe de la grille, motif non vide, ligne rouge renseignée
  D3  opérations : pour S, R, D, les opérations s'appliquent (contrôles C2 et C3 de
      revision_penale.py) ; A et G n'en portent pas ; F nomme sa destination
  D4  renvois : tout article abrogé ou fusionné qui est cité ailleurs dans le
      périmètre est listé, avec les articles à coordonner
  D5  ligne rouge : un article signalé en passe 1 (liberté, nullité, peine) porte
      une ligne rouge explicitement examinée

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
            j = "2029-01-01" if code == "cpp" else None
            ap = [v for v in vs if droit.applicable(v, j)]
            if ap:
                textes[(code, ap[-1]["num"])] = (ap[-1]["texte"] or "", ap[-1].get("section") or "")
    for f in sorted(DEC.glob("*.json")):
        lot = json.loads(f.read_text(encoding="utf-8"))
        per = lot["perimetre"]
        attendus = {(c, n) for (c, n), (t, s) in textes.items()
                    if c == per["code"] and per["section_contient"] in s and n.startswith(per.get("prefixe", ""))}
        decides = {(d["code"], d["num"]): d for d in lot["decisions"]}
        manq = attendus - set(decides)
        if manq:
            anomalies.append(f"{f.name} D1 : {len(manq)} article(s) sans décision : {sorted(n for _, n in manq)[:8]}")
        cpt = collections.Counter()
        retires = []
        for (c, n), d in decides.items():
            cpt[d["decision"]] += 1
            if (c, n) not in parcle:
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
        cibles = {droit.norm_num(n): n for _, n in retires}
        for c, n in retires:   # l'ancien numéro, cité par la partie réglementaire
            anc = parcle.get((c, n), {}).get("num_actuel")
            if anc:
                cibles.setdefault(droit.norm_num(anc), f"{n} (ancien {anc})")
        for (c, n), (t, _) in textes.items():
            if (c, n) in decides:
                continue
            for x in renvois(t):
                k = droit.norm_num(x)
                if k in cibles:
                    coord[cibles[k]].append(n)
        lots.append({"lot": f.name, "attendus": len(attendus), "decides": len(decides),
                     "decisions": dict(cpt), "a_coordonner": {k: sorted(v) for k, v in coord.items()}})
    couverture = sum(l["decides"] for l in lots)
    out = {"articles_registre": len(reg), "decides": couverture,
           "part_jugee": round(couverture / len(reg), 4), "lots": lots, "anomalies": anomalies}
    (CHANTIER / "referentiels" / "decisions_penal_bilan.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for l in lots:
        print(f"{l['lot']} : {l['decides']}/{l['attendus']} jugés, {l['decisions']}")
        for k, v in l["a_coordonner"].items():
            print(f"   {k} est cité par {len(v)} article(s) : {', '.join(v[:10])}")
    print(f"registre : {couverture}/{len(reg)} articles jugés ({out['part_jugee']:.2%}), {len(anomalies)} anomalie(s)")
    for a in anomalies:
        print("  ANOMALIE", a)
    if strict and anomalies:
        sys.exit(1)


if __name__ == "__main__":
    main()
