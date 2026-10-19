#!/usr/bin/env python3
"""Codes de la chaîne pénale en arborescence git, et relevé des frictions.

Étape 1 de methode/procedure_revision_penale.md. Lit le droit par `droit.py`,
seul canal du chantier vers la base LEGI, et écrit deux choses :

  revision/codes/<court>/<cliche>/<partie>/<num>.md
      Un fichier par article applicable le jour du cliché, texte verbatim.
      Deux clichés : `actuel` (aujourd'hui) et `2029` (le 1er janvier 2029,
      entrée en vigueur du CPP refondu par l'ordonnance n° 2025-1091).
      Une révision = un commit sur ces fichiers, le diff dit ce qui change.

  referentiels/frictions_penal.tsv
      Une ligne par article et par famille de friction relevée : délai,
      autorisation, avis, nullité, formalité, seuil, compétence, renvoi
      au règlement, coût pour l'État. C'est un repérage lexical, pas un
      jugement : il trie ce qu'on lit en premier.

Emploi :
    python3 chantier/appareil/codes_git.py                  # codes par défaut
    python3 chantier/appareil/codes_git.py cpp cp --cliche actuel
    python3 chantier/appareil/codes_git.py --controle       # relit l'écrit

Un code absent de data/ est signalé et passé, jamais suppléé.
"""
import argparse
import csv
import hashlib
import pathlib
import re
import shutil
import sys
from datetime import date

CHANTIER = pathlib.Path(__file__).resolve().parents[1]
RACINE = CHANTIER.parent
sys.path.insert(0, str(RACINE))
import droit  # noqa: E402

SORTIE = CHANTIER / "revision" / "codes"
TSV = CHANTIER / "referentiels" / "frictions_penal.tsv"

CHAINE_PENALE = ["cpp", "cp", "penitentiaire", "coj", "cjpm", "securite_interieure"]
CLICHES = {"actuel": None, "2029": "2029-01-01"}

FAMILLES = {
    "delai": r"\bdélai|\bdans les? (?:\w+ )?(?:heures|jours|mois)\b|au plus tard|sans délai|\bdurée\b",
    "autorisation": r"\bautoris|\bsur autorisation|\baccord (?:préalable|du|de la)|\bagrément|\bhabilit",
    "avis": r"\baprès avis|\bsur avis|\bavis conforme|\baprès consultation",
    "nullite": r"\bà peine de nullité|\bnullit",
    "formalite": r"procès-verbal|\bnotifi|\bmention(?:né|ne)?\b|lettre recommandée|\bcopie\b|\bsigné",
    "seuil": r"(?:supérieure?|inférieure?|égale?) à \w+|n'excède pas|\bau moins\b|\bau plus\b",
    "competence": r"juge des libertés|chambre de l'instruction|\bjuge d'instruction|\bseule? compétent|\bexclusivement",
    "renvoi_reglement": r"décret en Conseil d'(?:É|E)tat|\bpar décret|\barrêté d[ue]s? ministres?",
    "cout_etat": r"frais de justice|à la charge de l'(?:É|E)tat|aide juridictionnelle|\bindemnit",
}
RE_FAM = {k: re.compile(v, re.I) for k, v in FAMILLES.items()}


def partie(a):
    n = (a.get("num") or "").strip()
    if re.match(r"^[LRDA]\*?[\s.\-]?\d", n):
        return n[0]
    racine = (a.get("section") or "").split(" > ")[0].casefold()
    if "législative" in racine:
        return "L"
    if "conseil d" in racine:
        return "R"
    if "décrets simples" in racine:
        return "D"
    if "arrêtés" in racine:
        return "A"
    return "autre"


def nom_fichier(num):
    s = re.sub(r"[^\w\-]+", "_", (num or "sans_numero").strip())
    return s.strip("_") or "sans_numero"


def applicables(court, jour):
    index = droit.charger(court)
    for versions in index.values():
        retenues = [v for v in versions if droit.applicable(v, jour)]
        if len(retenues) > 1:
            retenues.sort(key=lambda v: v.get("date_debut") or "")
        if retenues:
            yield retenues[-1]


def ecrire(court, cliche, jour, lignes):
    dossier = SORTIE / court / cliche
    if dossier.exists():
        shutil.rmtree(dossier)
    vus, n = set(), 0
    for a in sorted(applicables(court, jour), key=lambda a: (partie(a), droit.norm_num(a["num"]))):
        p = partie(a)
        f = dossier / p / f"{nom_fichier(a['num'])}.md"
        if f in vus:  # deux numéros que l'assainissement confond
            f = f.with_name(f"{f.stem}__{a['id']}.md")
        vus.add(f)
        f.parent.mkdir(parents=True, exist_ok=True)
        tete = (f"<!-- {a['id']} | {a.get('etat')} | {a.get('date_debut')} → {a.get('date_fin')} -->\n"
                f"# {court} {a['num']}\n\n*{a.get('section') or ''}*\n\n")
        f.write_text(tete + (a.get("texte") or "") + "\n", encoding="utf-8")
        n += 1
        texte = a.get("texte") or ""
        for fam, rx in RE_FAM.items():
            occ = rx.findall(texte)
            if occ:
                m = rx.search(texte)
                ext = texte[max(0, m.start() - 50): m.end() + 70].replace("\t", " ").replace("\n", " ")
                lignes.append([court, cliche, p, a["num"], a["id"], fam, len(occ), len(texte),
                               (a.get("section") or "")[:160], ext])
    return n


def controle():
    """Chaque fichier relu doit redonner, à l'octet, le texte que rend droit.py."""
    ecarts, vus = 0, 0
    for f in SORTIE.glob("*/*/*/*.md"):
        court, cliche = f.parts[-4], f.parts[-3]
        ident = f.read_text(encoding="utf-8").split(" | ", 1)[0].removeprefix("<!-- ")
        corps = f.read_text(encoding="utf-8").split("\n\n", 2)[2].removesuffix("\n")
        jour = CLICHES[cliche]
        cible = [a for a in applicables(court, jour) if a["id"] == ident]
        vus += 1
        if len(cible) != 1 or (cible[0].get("texte") or "") != corps:
            ecarts += 1
            print("ÉCART", f)
    print(f"contrôle : {vus} fichiers relus, {ecarts} écart(s)")
    return ecarts == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("codes", nargs="*", default=CHAINE_PENALE)
    ap.add_argument("--cliche", choices=list(CLICHES), action="append")
    ap.add_argument("--controle", action="store_true")
    o = ap.parse_args()
    if o.controle:
        sys.exit(0 if controle() else 1)
    mil, age, perime = droit.fraicheur()
    print(f"base LEGI {mil} ({age} j{' — PÉRIMÉE' if perime else ''})")
    lignes, bilan = [], []
    for court in o.codes:
        try:
            droit.charger(court)
        except (KeyError, FileNotFoundError) as e:
            print(f"PASSÉ {court} : {e}".splitlines()[0])
            continue
        for cliche in (o.cliche or list(CLICHES)):
            jour = CLICHES[cliche] or str(date.today())
            n = ecrire(court, cliche, jour, lignes)
            bilan.append((court, cliche, n))
            print(f"{court:22} {cliche:7} {n:6} articles")
    TSV.parent.mkdir(parents=True, exist_ok=True)
    with TSV.open("w", encoding="utf-8", newline="") as t:
        w = csv.writer(t, delimiter="\t", lineterminator="\n")
        w.writerow(["code", "cliche", "partie", "num", "id", "famille", "occurrences",
                    "longueur", "section", "extrait"])
        w.writerows(sorted(lignes, key=lambda l: (l[0], l[1], l[2], droit.norm_num(l[3]), l[5])))
    h = hashlib.sha256(TSV.read_bytes()).hexdigest()[:12]
    print(f"{TSV.relative_to(RACINE)} : {len(lignes)} lignes, sha256 {h}")


if __name__ == "__main__":
    main()
