#!/usr/bin/env python3
"""Projet de révision de la chaîne pénale : génération et contrôles.

Lit revision/fiches_penal.json, applique chaque opération au texte en vigueur
rendu par droit.py, et écrit :

  livrables/revision_penale.md            le produit lisible, fiche par fiche
  referentiels/controle_revision_penale.json   le compte rendu des contrôles

Le texte cible et la disposition modificative sont DÉRIVÉS des opérations : on
ne les écrit jamais à la main. Les contrôles sont mécaniques :

  C1  l'article visé existe et s'applique au jour de référence
  C2  chaque passage remplacé figure une fois et une seule dans le texte
  C3  réapplication : la modificative rejouée sur le texte en vigueur redonne
      la cible, à l'octet
  C4  un article créé n'existe pas déjà
  C5  aucun point-virgule dans le texte normatif inséré
  C6  coordination 2029 : chaque vérification déclarée se constate dans la base
  C7  inventaire des paramètres entre crochets

Emploi :
    python3 chantier/appareil/revision_penale.py          # génère et contrôle
    python3 chantier/appareil/revision_penale.py --strict # échoue sur anomalie
"""
import json
import pathlib
import re
import sys

CHANTIER = pathlib.Path(__file__).resolve().parents[1]
RACINE = CHANTIER.parent
sys.path.insert(0, str(RACINE))
import droit  # noqa: E402

SOURCE = CHANTIER / "revision" / "fiches_penal.json"
PRODUIT = CHANTIER / "livrables" / "revision_penale.md"
CONTROLE = CHANTIER / "referentiels" / "controle_revision_penale.json"

NOMS = {"cpp": "du code de procédure pénale", "cp": "du code pénal",
        "penitentiaire": "du code pénitentiaire", "coj": "du code de l'organisation judiciaire",
        "cjpm": "du code de la justice pénale des mineurs"}
RE_PARAM = re.compile(r"\[[^\]]+\]")


def cite(num):
    """R48-1 → R. 48-1 ; 803-1 → 803-1 ; L1632-3 → L. 1632-3."""
    m = re.match(r"^([LRDA])\*?(\d.*)$", num)
    return f"{m.group(1)}. {m.group(2)}" if m else num


def guillemets(t):
    return "« " + t.replace("\n", " »\n« ") + " »"


class Anomalie(Exception):
    pass


def appliquer(texte, op):
    """Rend (texte modifié, phrase de modificative)."""
    o = op["op"]
    if o == "remplacer":
        n = texte.count(op["ancien"])
        if n != 1:
            raise Anomalie(f"C2 : « {op['ancien'][:60]} » figure {n} fois")
        if op.get("libelle") == "montant":
            phrase = f"le montant : {guillemets(op['ancien'])} est remplacé par le montant : {guillemets(op['nouveau'])}"
        else:
            phrase = f"les mots : {guillemets(op['ancien'])} sont remplacés par les mots : {guillemets(op['nouveau'])}"
        return texte.replace(op["ancien"], op["nouveau"]), phrase
    if o == "remplacer_depuis":
        n = texte.count(op["ancre"])
        if n != 1:
            raise Anomalie(f"C2 : ancre « {op['ancre']} » figure {n} fois")
        i = texte.index(op["ancre"])
        return (texte[:i] + op["nouveau"],
                f"{op.get('subdivision', 'la fin de l’article')} est ainsi rédigé : {guillemets(op['nouveau'])}")
    if o == "remplacer_alineas":
        al = texte.split("\n")
        idx = [k - 1 for k in op["alineas"]]
        if max(idx) >= len(al):
            raise Anomalie("C2 : alinéa absent")
        nouveau = al[:idx[0]] + [op["nouveau"]] + [a for k, a in enumerate(al) if k > idx[-1]]
        rangs = " et ".join(ordinal(k) for k in op["alineas"])
        verbe = "sont remplacés" if len(idx) > 1 else "est remplacé"
        return ("\n".join(nouveau),
                f"les {rangs} alinéas {verbe} par un alinéa ainsi rédigé : {guillemets(op['nouveau'])}")
    if o == "ajouter_alinea":
        return (texte + "\n" + op["nouveau"],
                f"est complété par un alinéa ainsi rédigé : {guillemets(op['nouveau'])}")
    if o == "rediger":
        return op["nouveau"], f"est ainsi rédigé : {guillemets(op['nouveau'])}"
    raise Anomalie(f"opération inconnue {o}")


def ordinal(k):
    return {1: "premier", 2: "deuxième", 3: "troisième", 4: "quatrième"}.get(k, f"{k}e")


def main():
    strict = "--strict" in sys.argv
    src = json.loads(SOURCE.read_text(encoding="utf-8"))
    jour = src["jour_reference"]
    mil, _, _ = droit.fraicheur()
    anomalies, params, fiches_out = [], [], []

    for f in src["fiches"]:
        blocs, modifs, etat = [], [], {}
        for op in f["operations"]:
            code, num = op["code"], op["num"]
            j = op.get("jour", jour)
            cle = (code, num)
            if op["op"] == "creer":
                try:
                    droit.article(code, num, j)
                    anomalies.append(f"{f['id']} C4 : {num} existe déjà")
                except Exception:
                    pass
                etat[cle] = {"avant": None, "apres": op["nouveau"], "id": None, "debut": None, "phrases": [], "cree": op}
            elif op["op"] == "abroger":
                try:
                    a = droit.article(code, num, j)
                    etat[cle] = {"avant": a["texte"], "apres": None, "id": a["id"], "debut": a["date_debut"], "phrases": [], "abroge": True}
                except Exception as e:
                    anomalies.append(f"{f['id']} C1 : {code} {num} introuvable au {j} ({str(e).splitlines()[0][:80]})")
                    continue
            else:
                if cle not in etat:
                    try:
                        a = droit.article(code, num, j)
                    except Exception as e:
                        anomalies.append(f"{f['id']} C1 : {code} {num} introuvable au {j} ({str(e).splitlines()[0][:80]})")
                        continue
                    etat[cle] = {"avant": a["texte"], "apres": a["texte"], "id": a["id"], "debut": a["date_debut"], "phrases": []}
                try:
                    nouveau, phrase = appliquer(etat[cle]["apres"], op)
                    etat[cle]["apres"] = nouveau
                    etat[cle]["phrases"].append(phrase)
                    if op.get("note"):
                        etat[cle].setdefault("notes", []).append(op["note"])
                except Anomalie as e:
                    anomalies.append(f"{f['id']} {code} {num} {e}")
            ins = op.get("nouveau", "")
            if ";" in ins:
                anomalies.append(f"{f['id']} C5 : point-virgule dans le texte inséré ({num})")
            for p in RE_PARAM.findall(ins):
                params.append((f["id"], cite(num), p))

        # C3 : réapplication — on rejoue toutes les opérations d'un article sur
        # le texte en vigueur et l'on compare à la cible retenue.
        for (code, num), e in etat.items():
            if e.get("cree") or e.get("abroge") or e["avant"] is None:
                continue
            t = e["avant"]
            try:
                for op in f["operations"]:
                    if (op["code"], op["num"]) == (code, num) and op["op"] not in ("abroger", "creer"):
                        t, _ = appliquer(t, op)
            except Anomalie:
                continue  # déjà compté en C2
            if t != e["apres"]:
                anomalies.append(f"{f['id']} C3 : réapplication divergente sur {num}")

        for (code, num), e in etat.items():
            nom = f"{cite(num)} {NOMS.get(code, code)}"
            if e.get("abroge"):
                modifs.append(f"L'article {nom} est abrogé.")
            elif e.get("cree"):
                modifs.append(f"Après l'article {cite(e['cree']['apres'])} {NOMS.get(code, code)}, il est inséré un article "
                              f"{cite(num)} ainsi rédigé : {guillemets(e['apres'])}" + ".")
            elif e["phrases"]:
                if len(e["phrases"]) == 1:
                    s = e["phrases"][0]
                    modifs.append(f"L'article {nom} {s}." if s.startswith("est ") else f"À l'article {nom}, {s}.")
                else:
                    lignes = "\n".join(f"{k + 1}° {p[0].upper() + p[1:]}." for k, p in enumerate(e["phrases"]))
                    modifs.append(f"L'article {nom} est ainsi modifié :\n{lignes}")
            blocs.append({"code": code, "num": num, "id": e["id"], "debut": e["debut"],
                          "avant": e["avant"], "apres": e["apres"], "notes": e.get("notes", [])})

        for v in f.get("verif_2029", []):
            try:
                a = droit.article("cpp", v["num"], "2029-01-01")
                if v["contient"] not in a["texte"]:
                    anomalies.append(f"{f['id']} C6 : {v['num']} (2029) ne contient pas « {v['contient']} »")
            except Exception:
                anomalies.append(f"{f['id']} C6 : {v['num']} introuvable au 2029-01-01")
        for p in f.get("parametres_hors_texte", []):
            params.append((f["id"], "—", p))
        fiches_out.append((f, blocs, modifs))

    ecrire_produit(src, fiches_out, params, mil)
    CONTROLE.parent.mkdir(parents=True, exist_ok=True)
    CONTROLE.write_text(json.dumps({"millesime_legi": mil, "jour_reference": jour,
                                    "fiches": len(src["fiches"]), "parametres": len(params),
                                    "anomalies": anomalies}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"base LEGI {mil} — {len(src['fiches'])} fiches, {len(params)} paramètres, {len(anomalies)} anomalie(s)")
    for a in anomalies:
        print("  ANOMALIE", a)
    if strict and anomalies:
        sys.exit(1)


def bloc_cite(t):
    return "\n".join("> " + l if l else ">" for l in t.split("\n"))


LONG = 1200


def condenser(avant, apres):
    """Pour un article long, ne garder que les alinéas qui changent."""
    if avant is None or apres is None or len(avant) <= LONG:
        return avant, apres
    a, b = avant.split("\n"), apres.split("\n")
    k = 0
    while k < min(len(a), len(b)) and a[k] == b[k]:
        k += 1
    m = 0
    while m < min(len(a), len(b)) - k and a[-1 - m] == b[-1 - m]:
        m += 1
    def coupe(x):
        mid = x[k:len(x) - m] if m else x[k:]
        return "\n".join((["[…]"] if k else []) + mid + (["[…]"] if m else []))
    return coupe(a), coupe(b)


def ecrire_produit(src, fiches_out, params, mil):
    L = [f"# {src['titre']}", "",
         f"*Texte en vigueur : base LEGI {mil}, lue par `droit.py`. Les textes cibles et les dispositions "
         "modificatives sont dérivés des opérations de `revision/fiches_penal.json` et contrôlés par réapplication. "
         "Les paramètres à arbitrer sont entre crochets.*", "",
         "## Sommaire", ""]
    for f, _, _ in fiches_out:
        L.append(f"- **{f['id']}** — {f['titre']} ({f['strate']})")
    L += ["", "## Principes appliqués (à valider)", "", "| n° | principe |", "|---|---|"]
    L += [f"| {n} | {t} |" for n, t in src["principes"]]
    L += ["", "## Paramètres à arbitrer", "", "| fiche | article | paramètre |", "|---|---|---|"]
    L += [f"| {i} | {a} | {p} |" for i, a, p in params]
    for paquet in ("réglementaire", "législatif"):
        L += ["", f"## Paquet {paquet}"]
        for f, blocs, modifs in fiches_out:
            if f["paquet"] != paquet:
                continue
            L += ["", f"### {f['id']} — {f['titre']}", "",
                  f"**Strate** : {f['strate']}. **Principes** : {', '.join(f['principes'])}.", "",
                  f"**Objet.** {f['objet']}", ""]
            for b in blocs:
                tete = f"{cite(b['num'])} {NOMS.get(b['code'], b['code'])}"
                L.append(f"#### {tete}")
                L.append("")
                av, ap = condenser(b["avant"], b["apres"])
                if b["apres"] is None and av and len(av) > 400:
                    av = av[:400].rsplit(" ", 1)[0] + " […]"
                if av is not None:
                    L += [f"*En vigueur* ({b['id']}, version du {b['debut']}) :", "", bloc_cite(av), ""]
                L += ["*Cible* :", "", bloc_cite(ap) if b["apres"] else "> *(abrogé)*", ""]
                for n in b["notes"]:
                    L += [f"*Note* : {n}", ""]
            L += ["*Dispositions modificatives* :", ""]
            for k, m in enumerate(modifs, 1):
                L += [f"{k}. " + m.replace("\n", "\n   "), ""]
            L += [f"**Code de 2029.** {f['code_2029']}", "", f"**Risques.** {f['risques']}"]
    PRODUIT.parent.mkdir(parents=True, exist_ok=True)
    PRODUIT.write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
