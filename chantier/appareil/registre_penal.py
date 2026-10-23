#!/usr/bin/env python3
"""Registre de la réécriture complète — passe 1, mécanique, sur TOUS les articles.

Chaque article du périmètre reçoit une ligne : ses mesures, ses signaux, les
principes qui le concernent, la ligne rouge éventuelle et une décision
PROPOSÉE. Aucune décision n'est définitive en passe 1 : la passe 2 juge chaque
article (revision/decisions/<lot>.json) et le registre consolidé refuse un
article sans décision motivée.

Périmètre par défaut :
  cpp  : partie législative du code de 2029 (L…), partie réglementaire en
         vigueur au 1er janvier 2029 (R, D, A) ;
  cp   : code pénal applicable ;
  penitentiaire : code pénitentiaire applicable.

Sorties :
  referentiels/registre_penal.tsv         une ligne par article
  referentiels/registre_penal_bilan.json  comptes par code, partie, décision
  referentiels/concordance_cpp.tsv        ancien numéro → numéro 2029 (par similarité)

Décisions (verbes) : G garder · S simplifier · F fusionner · A abroger ·
D déclasser au règlement · M remonter à la loi · R réécrire au fond · C créer.

Emploi : python3 chantier/appareil/registre_penal.py
"""
import collections
import csv
import json
import pathlib
import re
import sys
from datetime import date

CHANTIER = pathlib.Path(__file__).resolve().parents[1]
RACINE = CHANTIER.parent
sys.path.insert(0, str(RACINE))
import droit  # noqa: E402

REF = CHANTIER / "referentiels"
DECISIONS = CHANTIER / "revision" / "decisions"
J2029 = "2029-01-01"

# ------------------------------------------------------------------ signaux
S = {k: re.compile(v, re.I) for k, v in {
    "delai": r"\bdélai|\bdans les? (?:\w+ )?(?:heures|jours|mois)\b|au plus tard",
    "autorisation": r"\bsur autorisation|\bautoris[ée]\w* par\b|\baccord préalable|\bagrément",
    "avis_obligatoire": r"\baprès avis|\bsur avis|\bavis conforme",
    "nullite": r"\bà peine de nullité|\bnullit",
    "notification": r"lettre recommandée|\bnotifi|\bconvoqu|\bsignifi",
    "formalite": r"procès-verbal|\bmention(?:né|ne)?\b|\bcopie\b|\bsigné|\bémargé",
    "derogation": r"\bpar dérogation|\bsauf\b|\btoutefois\b|\bà l'exception\b",
    "renvoi_reglement": r"décret en Conseil d'(?:É|E)tat|\bpar décret|\barrêté d[ue]s? ministres?",
    "peine": r"\bemprisonnement\b|\bréclusion\b|\bamende\b|\bpeine\b",
    "amenagement": r"\baménag|semi-liberté|surveillance électronique|libération (?:conditionnelle|sous contrainte)|réduction de peine",
    "liberte": r"garde à vue|détention provisoire|\bperquisition|\binterception|\bgéolocalisation|\bcontrôle judiciaire|\brétention|privation de liberté|\bfouille",
    "victime": r"\bvictime|partie civile",
    "outre_mer": r"Nouvelle-Calédonie|Polynésie|Wallis|Saint-Pierre|Mayotte|Martinique|Guadeloupe|Guyane|La Réunion|Saint-Barthélemy|Saint-Martin",
    "jury": r"\bjur[ée]s?\b|\bjury\b|assesseur",
    "liste": r"(?:suivant(?:e)?s|ci-après)\s*:",
    "publicite": r"huis clos|chambre du conseil|non publique|publicité des débats|\bsecret\b|\bconfidentiel",
}.items()}

PRINCIPES = {   # signal → principes de la grille qui jugent l'article
    "amenagement": ["P10", "P14"], "peine": ["P14", "P27"], "nullite": ["P11"],
    "notification": ["P12"], "liste": ["P2"], "avis_obligatoire": ["P15", "P1"],
    "autorisation": ["P16"], "derogation": ["P3"], "renvoi_reglement": ["P1"],
    "outre_mer": ["P3"], "jury": ["P17"], "victime": ["P18"], "delai": ["P11", "P19"],
    "publicite": ["P26"],
}
LIGNE_ROUGE = {"liberte": "art. 66 C, CEDH art. 5 : contrôle d'un juge", "nullite": "art. 16 DDHC : droits de la défense",
               "peine": "art. 8 DDHC : nécessité, individualisation au prononcé"}

RE_RENVOI = re.compile(r"articles? ((?:L\.|R\.|D\.|A\.)\s?\d+(?:-\d+)*|\d+(?:-\d+)+)")
RE_MOTS = re.compile(r"\w+(?:[-']\w+)*")


def mots(t):
    return RE_MOTS.findall(t or "")


def corpus():
    """Rend la liste des articles du périmètre, au jour qui les concerne."""
    out = []
    idx = droit.charger("cpp")
    for vs in idx.values():
        ap = [v for v in vs if droit.applicable(v, J2029)]
        if ap:
            a = ap[-1]
            n = a["num"] or ""
            if re.match(r"^[LRDA]\*?\d", n):
                out.append(("cpp", a, J2029))
    for code in ("cp", "penitentiaire"):
        for vs in droit.charger(code).values():
            ap = [v for v in vs if droit.applicable(v)]
            if ap:
                out.append((code, ap[-1], str(date.today())))
    return out


def partie(a):
    s = (a.get("section") or "").split(" > ")
    return (s[1] if len(s) > 1 else s[0])[:60]


def concordance(arts):
    """Ancien article du CPP → article L du code de 2029, par 6-grammes partagés."""
    idx = droit.charger("cpp")
    anciens = []
    for vs in idx.values():
        ap = [v for v in vs if droit.applicable(v)]
        if ap and re.match(r"^\d", ap[-1]["num"] or ""):
            anciens.append(ap[-1])
    def grammes(t):
        w = [x.lower() for x in mots(t)]
        return {" ".join(w[i:i + 6]) for i in range(max(0, len(w) - 5))}
    inv = collections.defaultdict(set)
    ga = {}
    for a in anciens:
        g = grammes(a["texte"])
        ga[a["num"]] = g
        for x in g:
            inv[x].add(a["num"])
    res = {}
    for code, a, _ in arts:
        if code != "cpp" or not (a["num"] or "").startswith("L"):
            continue
        g = grammes(a["texte"])
        if not g:
            continue
        cpt = collections.Counter()
        for x in g:
            if len(inv.get(x, ())) <= 20:
                cpt.update(inv[x])
        if cpt:
            num, n = cpt.most_common(1)[0]
            score = n / max(len(g), 1)
            if score >= 0.3:
                res[a["num"]] = (num, round(score, 2))
    return res


def doublons(arts):
    """Paires d'articles quasi identiques dans un même code : candidats à la fusion."""
    sig = collections.defaultdict(list)
    for code, a, _ in arts:
        w = [x.lower() for x in mots(a["texte"])]
        if len(w) < 25:
            continue
        # empreinte : le texte sans les numéros d'articles ni les noms de territoires
        t = re.sub(r"\d[\d-]*", "#", " ".join(w))
        t = S["outre_mer"].sub("@", t)
        sig[(code, t)].append(a["num"])
    paires = {}
    for (code, _), nums in sig.items():
        if len(nums) > 1:
            for n in nums:
                paires[(code, n)] = nums[0] if n != nums[0] else nums[1]
    return paires


def proposer(code, a, sig, dbl, entrants):
    """Décision proposée, avec le principe qui la porte et sa raison. Ordre fixe."""
    n, t = a["num"] or "", a.get("texte") or ""
    if not t.strip() or re.match(r"^\s*(?:\(?abrogé|\[abrogé)", t, re.I):
        return "A", "P20", "article vide ou abrogé"
    if (code, n) in dbl:
        return "F", "P3", f"texte identique à {dbl[(code, n)]} hors références"
    if sig["outre_mer"] and "outre-mer" in (a.get("section") or "").lower():
        return "S", "P3", "adaptation outre-mer : clause d'application générale"
    if sig["amenagement"] and code in ("cpp", "cp", "penitentiaire"):
        return "R", "P10", "régime d'aménagement ou d'exécution"
    if sig["nullite"]:
        return "R", "P11", "régime de nullité"
    if sig["avis_obligatoire"]:
        return "S", "P15", "avis obligatoire préalable"
    if sig["notification"] and n[:1] in "RDA":
        return "S", "P12", "notification ou lettre recommandée"
    if n.startswith("L") and not sig["liberte"] and not sig["peine"] and re.search(
            r"\bmodalités\b|\bformes?\b|\bcontenu de\b|\bmentions?\b", t, re.I) and len(mots(t)) < 120:
        return "D", "P1", "règle de forme ou de modalité dans la loi"
    if sig["liste"] and sig["derogation"]:
        return "S", "P2", "liste fermée assortie de dérogations"
    return "G", "P21", "à confirmer : nécessité à établir (charge de la preuve à la norme)"


def charger_decisions():
    dec = {}
    if DECISIONS.exists():
        for f in sorted(DECISIONS.glob("*.json")):
            for d in json.loads(f.read_text(encoding="utf-8")).get("decisions", []):
                dec[(d["code"], d["num"])] = d
    return dec


def main():
    arts = corpus()
    textes = {(c, a["num"]): a["texte"] or "" for c, a, _ in arts}
    # renvois entrants, comptés dans tout le périmètre
    entrants = collections.Counter()
    for c, a, _ in arts:
        for r in set(RE_RENVOI.findall(a["texte"] or "")):
            entrants[(c, droit.norm_num(r.replace(" ", "")))] += 1
    dbl = doublons(arts)
    conc = concordance(arts)
    dec = charger_decisions()
    lignes, bilan = [], collections.Counter()
    for c, a, jour in arts:
        t = a["texte"] or ""
        sig = {k: bool(rx.search(t)) for k, rx in S.items()}
        verbe, principe, raison = proposer(c, a, sig, dbl, entrants)
        princ = sorted({p for k, v in sig.items() if v for p in PRINCIPES.get(k, [])} | {principe})
        rouge = " ; ".join(v for k, v in LIGNE_ROUGE.items() if sig[k])
        d = dec.get((c, a["num"]))
        anc = conc.get(a["num"], ("", ""))
        lignes.append([
            c, a["num"], a["id"], partie(a), (a.get("section") or "").split(" > ")[-1][:80],
            anc[0], anc[1], len(mots(t)), entrants[(c, droit.norm_num(a["num"]))],
            ",".join(k for k, v in sig.items() if v), ",".join(princ), rouge,
            verbe, principe, raison,
            d["decision"] if d else "", d.get("motif", "") if d else "", "jugé" if d else "à juger"])
        bilan[(c, verbe)] += 1
    REF.mkdir(parents=True, exist_ok=True)
    with (REF / "registre_penal.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["code", "num", "id", "partie", "section", "num_actuel", "concordance_score", "mots",
                    "renvois_entrants", "signaux", "principes", "ligne_rouge",
                    "proposition", "principe_proposition", "raison", "decision", "motif", "etat"])
        w.writerows(lignes)
    with (REF / "concordance_cpp.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["num_2029", "num_actuel", "score"])
        for k, (v, s) in sorted(conc.items(), key=lambda x: droit.norm_num(x[0])):
            w.writerow([k, v, s])
    par_code = collections.defaultdict(dict)
    for (c, v), n in bilan.items():
        par_code[c][v] = n
    juges = sum(1 for l in lignes if l[-1] == "jugé")
    out = {"articles": len(lignes), "juges": juges, "a_juger": len(lignes) - juges,
           "mots": sum(l[7] for l in lignes), "propositions": par_code,
           "concordance_cpp": len(conc)}
    (REF / "registre_penal_bilan.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
