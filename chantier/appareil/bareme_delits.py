#!/usr/bin/env python3
"""Peines de référence des délits : tri entre l'essentiel et l'affichage (P27).

Lit referentiels/incriminations.tsv (articles L qui punissent d'emprisonnement),
corrigé par revision/bareme_hors_releve.json (articles qui n'incriminent rien, ajouts),
relit chaque article par `droit.py` et le range en trois classes :

- noyau : atteinte aux personnes, aux biens, à la nation, à la justice ou à la
  confiance publique ; la peine encourue est la référence (barème) et se
  vérifie contre la hiérarchie de sa famille ;
- formel : manquement à une obligation de déclaration, d'autorisation, de
  registre ou de forme, sans dommage nommé ; l'emprisonnement y est une peine
  d'affichage présumée : proposition de requalifier en amende délictuelle,
  contravention de 5e classe ou sanction administrative ;
- à juger : ni l'un ni l'autre au relevé lexical ; décision en passe 2.

C'est un tri de passe 1, à confirmer article par article, puis par l'usage
(condamnations par NATINF, casier judiciaire) quand la donnée sera obtenue.

La passe 2 s'écrit dans revision/bareme/<famille>.json, jamais dans le TSV : le
script reverse chaque décision et son motif dans les colonnes `decision` et
`motif`, et `decisions_penal.py` (D6) contrôle la source et l'accord du TSV.

Emploi :
    python3 chantier/appareil/bareme_delits.py
"""
import csv
import json
import pathlib
import re
import sys
from collections import Counter
from datetime import date

CHANTIER = pathlib.Path(__file__).resolve().parents[1]
RACINE = CHANTIER.parent
sys.path.insert(0, str(RACINE))
import droit  # noqa: E402

SRC = CHANTIER / "referentiels" / "incriminations.tsv"
TSV = CHANTIER / "referentiels" / "bareme_delits.tsv"
BILAN = CHANTIER / "referentiels" / "bareme_delits_bilan.json"
DECISIONS = CHANTIER / "revision" / "bareme"
HORS = CHANTIER / "revision" / "bareme_hors_releve.json"   # exclusions et ajouts au relevé (registre 2.8)


def decisions():
    """(code, num) → décision de passe 2, lue dans revision/bareme/*.json."""
    out = {}
    for f in sorted(DECISIONS.glob("*.json")):
        for d in json.loads(f.read_text(encoding="utf-8"))["decisions"]:
            out[(d["code"], d["num"])] = d
    return out

NOYAU = re.compile(
    r"\bviolence|\bmort\b|\bdécès|\bblessure|incapacité totale de travail|\bmeurtre|\bviol\b|agression|"
    r"\bmenace|\bvol\b|\bescroquer|\bextorsion|\brecel|\bdétourne|\bfraud|\bfaux\b|\bcontrefaçon|"
    r"\bcorrupt|trafic d'influence|\bstupéfiant|\barmes?\b|\bexplosi|terror|\bmineur|vulnérab|"
    r"mise en danger|risque immédiat|\bséquestr|\btraite\b|\bproxénét|\bblanchi|\bincendi|\bdestruction|"
    r"\bdégrad|\bharcèle|\bentrave à la justice|\bsubornation|\bévasion|\brébellion|\boutrage|"
    r"atteinte à la sécurité|santé publique|\bempoisonn|\bdopage|\bclandestin", re.I)
FORMEL = re.compile(
    r"sans (?:avoir (?:obtenu|souscrit|déclaré|sollicité)|autorisation|agrément|déclaration|l'autorisation|l'agrément)|"
    r"\bdéfaut de (?:déclaration|tenue|présentation|communication|mention|affichage)|"
    r"\bde ne pas (?:tenir|déclarer|communiquer|présenter|transmettre|afficher|informer|mentionner|respecter)|"
    r"\ben méconnaissance (?:des|de l')|\bregistre\b|\bobstacle aux? (?:fonctions|contrôle)|"
    r"\bentrav(?:e|er) (?:à |l')(?:l'exercice|l'accomplissement|contrôle)|\bformalit|\bnon-respect|"
    r"\bde ne pas procéder|\bsans être (?:titulaire|agréé|inscrit|déclaré|habilité|muni)|\bentraver l'action|"
    r"\bsans respecter|\bcontrairement aux dispositions|\bméconnaissant", re.I)
MOIS = {"deux mois": 2, "trois mois": 3, "six mois": 6, "un an": 12, "deux ans": 24, "trois ans": 36,
        "quatre ans": 48, "cinq ans": 60, "sept ans": 84, "dix ans": 120}


def mois(p):
    for k, v in MOIS.items():
        if k in p:
            return v
    return ""


def main():
    jour = str(date.today())
    lignes, bilan, par_code = [], Counter(), Counter()
    passe2 = decisions()
    hors = json.loads(HORS.read_text(encoding="utf-8")) if HORS.exists() else {"exclus": [], "ajouts": []}
    exclus = {(e["code"], e["num"]) for e in hors["exclus"]}
    source = [r for r in csv.DictReader(SRC.open(encoding="utf-8"), delimiter="\t")
              if r["nature"] == "délit" and (r["code"], r["num"]) not in exclus]
    source += [dict(a, nature="délit") for a in hors["ajouts"]]
    for r in source:
        a = droit.article(r["code"], r["num"], r.get("jour") or jour)
        t = (a or {}).get("texte") or ""
        n, f = NOYAU.search(t), FORMEL.search(t)
        if n:
            cl, prop = "noyau", "peine encourue = référence ; contrôler la hiérarchie de la famille"
        elif f:
            cl, prop = "formel", "emprisonnement d'affichage présumé : amende délictuelle, contravention de 5e classe ou sanction administrative"
        else:
            cl, prop = "à juger", "passe 2"
        bilan[cl] += 1
        par_code[(r["code"], cl)] += 1
        d = passe2.get((r["code"], r["num"]), {})
        lignes.append([r["code"], r["num"], r["peine_relevee"], mois(r["peine_relevee"]), cl,
                       (n or f).group(0) if (n or f) else "", prop, d.get("decision", ""), d.get("motif", "")])
    with TSV.open("w", encoding="utf-8", newline="") as h:
        w = csv.writer(h, delimiter="\t", lineterminator="\n")
        w.writerow(["code", "num", "peine_relevee", "mois", "classe", "indice", "proposition", "decision", "motif"])
        w.writerows(sorted(lignes, key=lambda l: (l[0], droit.norm_num(l[1]))))
    codes = {}
    for (c, cl), v in par_code.items():
        codes.setdefault(c, {})[cl] = v
    out = {"jour": jour, "delits": len(lignes), "classes": dict(bilan),
           "decisions": dict(Counter(l[7] for l in lignes if l[7])),
           "par_code": dict(sorted(codes.items(), key=lambda kv: -sum(kv[1].values())))}
    BILAN.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("delits", "classes")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
