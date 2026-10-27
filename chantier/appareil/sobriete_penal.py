#!/usr/bin/env python3
"""Passe 3 — sobriété : réécriture par titre entier et contrôles S1 à S3.

Une pièce par titre, revision/passe3/<lot>.json, écrite par l'agent qui réécrit le titre :

  {"lot": "lot_p000", "titre": "…", "ecart_volume": "",
   "articles_cible": [{"num", "texte", "verbe" (G S R D M C), "principe", "motif", "ligne_rouge"}],
   "retires": [{"num", "verbe" (A F), "vers" (F), "principe", "motif", "ligne_rouge"}],
   "phrases": {"<num>#<rang>": {"destin": "gardee|reprise|declassee|abrogee",
                                 "vers": "<num cible> | <texte de destination>", "principe", "garantie"}}}

Contrôles (à zéro avant chaque versement) :

  S1 traçabilité  chaque phrase de l'état 2029 du titre a un destin : gardée (mot pour mot dans
                  l'article cible désigné), reprise (dans quel article), déclassée (vers quel texte),
                  abrogée (par quel principe) ; chaque article 2029 est gardé, fusionné ou abrogé une fois ;
                  aucun point-virgule n'est inséré
  S2 garanties    une phrase d'un article signalé en passe 1 (ligne rouge) qui est déclassée ou abrogée
                  dit où sa garantie survit (« garantie »), et l'article retiré examine sa ligne rouge
  S3 volume       mots du titre contre la cible de son bloc ; un dépassement se motive (« ecart_volume »)

Emploi :
  sobriete_penal.py dump <lot>          le titre à réécrire, phrase par phrase, pour l'agent
  sobriete_penal.py controle [<lot>…] [--strict]
  sobriete_penal.py appliquer <lot>…    porte la pièce de passe 3 dans les décisions du lot
"""
import csv
import json
import pathlib
import re
import sys

CHANTIER = pathlib.Path(__file__).resolve().parents[1]
RACINE = CHANTIER.parent
sys.path.insert(0, str(RACINE))
import droit  # noqa: E402

REG = CHANTIER / "referentiels" / "registre_penal.tsv"
DEC = CHANTIER / "revision" / "decisions"
P3 = CHANTIER / "revision" / "passe3"
GRILLE = CHANTIER / "revision" / "grille_principes.json"
J2029 = "2029-01-01"
DESTINS = {"gardee", "reprise", "declassee", "abrogee"}
# cibles de volume (procédure, Passe 3) : variation des mots par rapport à l'état 2029
CIBLES = {("cpp", "L"): -0.40, ("cpp", "R"): -0.50, ("cp", ""): -0.25, ("penitentiaire", ""): -0.60}
RE_PHRASE = re.compile(r"(?<=[.!?])(?<!\b[A-Z]\.)(?<!\bart\.)(?<!\bArt\.)(?<!\bal\.)(?<!\bn°)\s*(?=[A-ZÉÈÀÂÎÔÇ«])")
NOMS_CODES = {"cpp": "code de procédure pénale", "cp": "code pénal", "penitentiaire": "code pénitentiaire"}


def phrases(texte):
    """Phrases d'un article : alinéa par alinéa, puis à chaque point suivi d'une majuscule."""
    out = []
    for a in (texte or "").split("\n"):
        out += [p.strip() for p in RE_PHRASE.split(a) if p.strip()]
    return out


def cle(num):
    """Ordre du code : préfixe, puis numéros en entiers."""
    m = re.match(r"([A-Z]*)\*?(.*)", num)
    return (m.group(1), [(0, int(x), "") if x.isdigit() else (1, 0, x) for x in re.split(r"[-.]", m.group(2)) if x])


def mots(t):
    return len(re.findall(r"\w+", t or ""))


def norm(t):
    return re.sub(r"\s+", " ", (t or "").replace("’", "'")).strip()


def bloc(code, num):
    if code == "cpp":
        return (code, "L" if num.startswith("L") else "R")
    return (code, "")


_CACHE = {}


def textes_2029():
    if "t" not in _CACHE:
        out = {}
        for code in NOMS_CODES:
            for vs in droit.charger(code).values():
                ap = [v for v in vs if droit.applicable(v, J2029)]
                if ap:
                    out[(code, ap[-1]["num"])] = (ap[-1]["texte"] or "", ap[-1].get("section") or "")
        _CACHE["t"] = out
    return _CACHE["t"]


def registre():
    return {(r["code"], r["num"]): r for r in csv.DictReader(REG.open(encoding="utf-8"), delimiter="\t")}


def perimetre(lot):
    """Articles 2029 du titre : ceux du périmètre du lot, au registre."""
    p = json.loads((DEC / f"{lot}.json").read_text(encoding="utf-8"))["perimetre"]
    reg = registre()
    arts = [(c, n) for (c, n), (t, s) in textes_2029().items()
            if c == p["code"] and p["section_contient"] in s and n.startswith(p.get("prefixe", "")) and (c, n) in reg]
    return p["code"], sorted(n for _, n in arts)


def lots():
    return sorted(f.stem for f in DEC.glob("*.json"))


def dump(lot):
    code, nums = perimetre(lot)
    reg = registre()
    t29 = textes_2029()
    dec = {}
    for f in DEC.glob("*.json"):
        for d in json.loads(f.read_text(encoding="utf-8"))["decisions"]:
            dec[(d["code"], d["num"])] = d
    sys.path.insert(0, str(CHANTIER / "appareil"))
    import revision_penale as rp
    total = 0
    for n in nums:
        t, sec = t29[(code, n)]
        total += mots(t)
        r = reg.get((code, n), {})
        d = dec.get((code, n), {})
        cible = t
        for op in d.get("operations", []):
            cible, _ = rp.appliquer(cible, op)
        print(f"=== {code} {n} | ancien {r.get('num_actuel', '')} | ligne rouge passe 1 : {r.get('ligne_rouge') or '—'}")
        print(f"section : {sec}")
        print(f"passe 2 : {d.get('decision', '?')} {d.get('principe', '')} {('vers ' + d['vers']) if d.get('vers') else ''} — {d.get('motif', '')}")
        for i, p in enumerate(phrases(t), 1):
            print(f"  [{n}#{i}] {p}")
        if d.get("decision") in ("A", "F"):
            print("  cible passe 2 : (retiré)")
        elif cible != t:
            print("  cible passe 2 : " + cible.replace("\n", " ¶ "))
    k = bloc(code, nums[0]) if nums else None
    print(f"\n--- {len(nums)} articles, {total} mots à l'état 2029 ; cible de volume du bloc : {CIBLES.get(k, 0):+.0%} "
          f"soit au plus {round(total * (1 + CIBLES.get(k, 0)))} mots")


def charger_p3(lot):
    f = P3 / f"{lot}.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None


def cibles_globales():
    """Numéros qui existent dans la cible : décisions non retirées, plus les articles des pièces de passe 3."""
    vivants = set()
    for f in DEC.glob("*.json"):
        for d in json.loads(f.read_text(encoding="utf-8"))["decisions"]:
            if d["decision"] not in "AF":
                vivants.add((d["code"], d["num"]))
    retires = set()
    for f in P3.glob("*.json"):
        p = json.loads(f.read_text(encoding="utf-8"))
        code, _ = perimetre(f.stem)
        vivants |= {(code, a["num"]) for a in p["articles_cible"]}
        retires |= {(code, a["num"]) for a in p.get("retires", [])}
    return vivants - retires


def controler(lot, grille, reg, vivants):
    an = []
    p = charger_p3(lot)
    code, nums = perimetre(lot)
    t29 = textes_2029()
    if p is None:
        return an, None
    cib = {a["num"]: a for a in p["articles_cible"]}
    ret = {a["num"]: a for a in p.get("retires", [])}
    # S1 — articles
    for n in nums:
        k = (n in cib) + (n in ret)
        if k != 1:
            an.append(f"{lot} S1 : {n} {'absent' if k == 0 else 'gardé et retiré'}")
    for n, a in cib.items():
        if (code, n) not in t29:
            if a.get("verbe") != "C":
                an.append(f"{lot} S1 : {n} n'existe pas en 2029 et n'est pas déclaré créé (C)")
        elif n not in nums:
            an.append(f"{lot} S1 : {n} hors du titre")
        if a.get("verbe") not in set("GSRDMC"):
            an.append(f"{lot} S1 : {n} verbe {a.get('verbe')} inconnu")
        if a.get("principe") not in grille:
            an.append(f"{lot} S1 : {n} principe {a.get('principe')} hors grille")
        if not a.get("motif", "").strip() or not a.get("ligne_rouge", "").strip():
            an.append(f"{lot} S1 : {n} motif ou ligne rouge vide")
        if not a.get("texte", "").strip():
            an.append(f"{lot} S1 : {n} texte cible vide")
    for n, a in ret.items():
        if a.get("verbe") not in ("A", "F"):
            an.append(f"{lot} S1 : {n} retiré avec le verbe {a.get('verbe')}")
        if a.get("verbe") == "F" and (code, a.get("vers", "")) not in vivants:
            an.append(f"{lot} S1 : {n} fusionné vers {a.get('vers')} absent de la cible")
        if a.get("principe") not in grille:
            an.append(f"{lot} S1 : {n} principe {a.get('principe')} hors grille")
        if not a.get("motif", "").strip():
            an.append(f"{lot} S1 : {n} retiré sans motif")
    # S1 — phrases
    ph = p.get("phrases", {})
    vers_pv = {}
    for n in nums:
        t = t29[(code, n)][0]
        lr = (reg.get((code, n), {}).get("ligne_rouge") or "").strip()
        for i, s in enumerate(phrases(t), 1):
            pid = f"{n}#{i}"
            e = ph.get(pid)
            if not e:
                an.append(f"{lot} S1 : phrase {pid} sans destin")
                continue
            d = e.get("destin")
            if d not in DESTINS:
                an.append(f"{lot} S1 : phrase {pid} destin {d} inconnu")
                continue
            if d in ("gardee", "reprise"):
                v = e.get("vers", "")
                if (code, v) not in vivants:
                    an.append(f"{lot} S1 : phrase {pid} {d} vers {v} absent de la cible")
                elif d == "gardee" and v in cib and norm(s) not in norm(cib[v]["texte"]):
                    an.append(f"{lot} S1 : phrase {pid} déclarée gardée mot pour mot, absente de {v}")
                vers_pv[v] = vers_pv.get(v, 0) + s.count(";")
            elif d == "declassee" and not e.get("vers", "").strip():
                an.append(f"{lot} S1 : phrase {pid} déclassée sans texte de destination")
            elif d == "abrogee" and e.get("principe") not in grille:
                an.append(f"{lot} S1 : phrase {pid} abrogée sans principe de la grille")
            # S2
            if lr and d in ("declassee", "abrogee") and not e.get("garantie", "").strip():
                an.append(f"{lot} S2 : phrase {pid} d'un article à ligne rouge ({lr[:40]}) {d} sans garantie dite")
        if n in ret and lr and ret[n].get("ligne_rouge", "").strip().lower() in ("", "aucune"):
            an.append(f"{lot} S2 : {n} retiré sans examen de sa ligne rouge ({lr[:40]})")
    for pid in ph:
        if pid.split("#")[0] not in nums:
            an.append(f"{lot} S1 : phrase {pid} hors du titre")
    for n, a in cib.items():
        if a["texte"].count(";") > vers_pv.get(n, 0) + (t29.get((code, n), ("",))[0].count(";") if a.get("verbe") == "G" else 0):
            an.append(f"{lot} S1 : {n} point-virgule inséré")
    # S3
    m29 = sum(mots(t29[(code, n)][0]) for n in nums)
    mc = sum(mots(a["texte"]) for a in cib.values())
    cible = CIBLES.get(bloc(code, nums[0]), 0) if nums else 0
    plafond = round(m29 * (1 + cible))
    if mc > plafond and not p.get("ecart_volume", "").strip():
        an.append(f"{lot} S3 : {mc} mots pour un plafond de {plafond} ({cible:+.0%} sur {m29}), écart non motivé")
    return an, {"lot": lot, "articles_2029": len(nums), "articles_cible": len(cib), "mots_2029": m29,
                "mots_cible": mc, "cible": cible, "plafond": plafond, "ecart": p.get("ecart_volume", "")}


def controle(args):
    strict = "--strict" in args
    choix = [a for a in args if not a.startswith("--")] or [f.stem for f in sorted(P3.glob("*.json"))]
    grille = {p["id"] for p in json.loads(GRILLE.read_text(encoding="utf-8"))["principes"]}
    reg = registre()
    vivants = cibles_globales()
    anomalies, tab = [], []
    for lot in choix:
        an, t = controler(lot, grille, reg, vivants)
        anomalies += an
        if t:
            tab.append(t)
    blocs = {}
    for t in tab:
        code, nums = perimetre(t["lot"])
        b = blocs.setdefault(f"{code}{bloc(code, nums[0])[1] if nums else ''}", [0, 0])
        b[0] += t["mots_2029"]
        b[1] += t["mots_cible"]
    out = {"lots": tab, "blocs": blocs, "anomalies": anomalies}
    if not [a for a in args if not a.startswith("--")]:
        (CHANTIER / "referentiels" / "sobriete_penal_bilan.json").write_text(
            json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for t in tab:
        print(f"{t['lot']} : {t['articles_2029']} → {t['articles_cible']} articles, {t['mots_2029']} → {t['mots_cible']} mots "
              f"(plafond {t['plafond']}){' — écart motivé' if t['ecart'] else ''}")
    for b, (a, c) in blocs.items():
        print(f"bloc {b} : {a} → {c} mots ({(c - a) / a:+.1%})" if a else f"bloc {b} : vide")
    print(f"sobriété : {len(tab)} titre(s) réécrit(s), {len(anomalies)} anomalie(s)")
    for a in anomalies:
        print("  ANOMALIE", a)
    if strict and anomalies:
        sys.exit(1)


def appliquer(lots_):
    """Porte chaque pièce de passe 3 dans les décisions : une décision par article du titre."""
    t29 = textes_2029()
    fichiers = {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in DEC.glob("*.json")}
    for lot in lots_:
        p = charger_p3(lot)
        code, nums = perimetre(lot)
        decs = []
        for a in p["articles_cible"]:
            n = a["num"]
            d = {"code": code, "num": n, "principe": a["principe"], "motif": a["motif"], "ligne_rouge": a["ligne_rouge"]}
            if (code, n) not in t29:
                d.update(decision="C", operations=[{"op": "rediger", "nouveau": a["texte"]}])
            elif a["texte"] == t29[(code, n)][0]:
                d.update(decision="G")
            else:
                d.update(decision=a["verbe"] if a["verbe"] in "SRDM" else "R",
                         operations=[{"op": "rediger", "nouveau": a["texte"]}])
            decs.append(d)
        for a in p.get("retires", []):
            d = {"code": code, "num": a["num"], "decision": a["verbe"], "principe": a["principe"],
                 "motif": a["motif"], "ligne_rouge": a.get("ligne_rouge") or "aucune"}
            if a["verbe"] == "F":
                d["vers"] = a["vers"]
            decs.append(d)
        nums_lot = {(d["code"], d["num"]) for d in decs}
        for nom, f in fichiers.items():
            if nom != lot:
                f["decisions"] = [d for d in f["decisions"] if (d["code"], d["num"]) not in nums_lot]
        # les décisions que le fichier du lot porte hors du titre restent en place
        hors = [d for d in fichiers[lot]["decisions"]
                if (d["code"], d["num"]) not in nums_lot and not (d["code"] == code and d["num"] in nums)]
        fichiers[lot]["decisions"] = decs + hors
        fichiers[lot]["passe"] = 3
    for nom, f in fichiers.items():
        (DEC / f"{nom}.json").write_text(json.dumps(f, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(lots_)} titre(s) porté(s) dans les décisions")


if __name__ == "__main__":
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "dump":
        dump(args[0])
    elif cmd == "controle":
        controle(args)
    elif cmd == "appliquer":
        appliquer(args)
