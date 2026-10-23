#!/usr/bin/env python3
"""Sources markdown du dossier et de l'annexe en trois colonnes, pour l'export
Word au gabarit du chantier (skill impression-docx, md2docx.js).

Tout texte de loi vient de droit.py par les opérations des fiches : rien n'est
recopié à la main. Écrit :
  livrables/dossier_revision_penale.md
  livrables/trois_colonnes_penal.md
"""
import pathlib
import re
import sys

CHANTIER = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CHANTIER / "appareil"))
import dossier_revision_penale as d  # noqa: E402
import revision_penale as rp  # noqa: E402

OUT = CHANTIER / "livrables"
NBSP = " "
ABROGE_DESC = {"R2": "Procès-verbaux séparés pour chacun des actes (douanes, commission rogatoire et flagrance)", "L2": "Procédure d’aménagement des peines d’un an au plus avant toute incarcération"}


def typo(t):
    """Apostrophes typographiques et insécables de la typographie française."""
    t = t.replace("'", "’")
    t = re.sub(r"\s*([:;?!])(?=\s|$)", NBSP + r"\1", t)
    t = re.sub(r"«\s*", "«" + NBSP, t)
    t = re.sub(r"\s*»", NBSP + "»", t)
    return t


def cellule(t):
    """Texte d'article dans une cellule de tableau : alinéas séparés par <br>."""
    return typo(t).replace("|", "/").replace("\n", "<br>")


def phrases(t):
    """Découpe en phrases, en gardant les retours d'alinéa comme frontières."""
    out = []
    for al in t.split("\n"):
        morceaux = [p for p in re.split(r"(?<=[.;:])\s+(?=[A-ZÉÈÀÂÎÔ0-9«])", al) if p]
        fus = []
        for m in morceaux:
            if fus and re.search(r"(\b[A-Z]|\bart|\bal|\bn°)\.$", fus[-1]):
                fus[-1] += " " + m
            else:
                fus.append(m)
        out += fus
        out.append("\n")
    return out[:-1]


def resserrer(avant, apres):
    """Ne garde que les phrases qui changent ; les autres deviennent « […] »."""
    if avant is None or apres is None:
        return avant, apres
    a, b = phrases(avant), phrases(apres)
    import difflib
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    oa, ob = [], []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            bloc = [x for x in a[i1:i2] if x != "\n"]
            if bloc:
                oa.append("[…]"); ob.append("[…]")
        else:
            oa.append(re.sub(r" ?\n ?", "\n", " ".join(a[i1:i2])).strip())
            ob.append(re.sub(r" ?\n ?", "\n", " ".join(b[j1:j2])).strip())
    oa = [x for x in oa if x]; ob = [x for x in ob if x]
    return "\n".join(oa) or "—", "\n".join(ob) or "—"


def nom(code, num):
    return f"{rp.cite(num)} {rp.NOMS.get(code, code)}"


def mil(n):
    return f"{n:,}".replace(",", NBSP)


def stats_lignes(st):
    n = st["modifies"] + st["crees"] + st["abroges"]
    reecrits = st["mots_supprimes"] + st["mots_ajoutes"]
    var = (st["mots_apres"] - st["mots_avant"]) / st["mots_avant"]
    return [
        "| Indicateur | Valeur |",
        "|---|---|",
        f"| Articles touchés | {n} ({st['modifies']} modifiés, {st['crees']} créés, {st['abroges']} abrogés) |",
        "| Codes touchés | 3 (procédure pénale, code pénal, code pénitentiaire) |",
        f"| Mots des articles touchés | {mil(st['mots_avant'])} avant, {mil(st['mots_apres'])} après ({var:+.0%}) |".replace("%", NBSP + "%"),
        f"| Mots réécrits | {mil(reecrits)} ({mil(st['mots_supprimes'])} supprimés, {mil(st['mots_ajoutes'])} ajoutés) |",
        f"| Équivalent en pages de code | ≈ {reecrits / 400:.1f} pages (400 mots par page) |".replace(".", ","),
        "| Strates | 4 mesures par décret ou arrêté, 5 par la loi |",
    ]


def dossier(src, fiches, st):
    L = ["# Révision de la chaîne pénale", "",
         "### Neuf mesures pour que la peine annoncée soit la peine exécutée — dossier de présentation, octobre 2026", "",
          typo("Le projet tient en neuf mesures. Quatre passent par décret ou arrêté, cinq par la loi. "
               "Chaque texte proposé est dérivé du droit en vigueur (base LEGI de la DILA, 20 octobre 2026) "
               "et contrôlé par réapplication de la disposition modificative. Les paramètres entre crochets "
               "restent à arbitrer."), "",
          "## Statistiques de réécriture", ""]
    L += stats_lignes(st) + [""]
    L += [typo("*Lecture des rédactions : « […] » signale des phrases inchangées non reproduites. Le texte intégral figure dans l'annexe en trois colonnes.*"), ""]
    L += ["## Principes proposés et effet avant / après", "",
          "| Principe | Avant | Après | Fiche |", "|---|---|---|---|"]
    for p, av, ap, fi in d.PRINCIPES:
        L.append(f"| **{typo(p)}** | {typo(av)} | {typo(ap)} | {fi} |")
    L.append("")
    for paquet, titre in (("réglementaire", "Rédactions proposées par décret ou arrêté"),
                          ("législatif", "Rédactions proposées par la loi")):
        L += [f"# {titre}", ""]
        for f, arts in fiches:
            if f["paquet"] != paquet:
                continue
            L += [f"## {f['id']}. {typo(f['titre'])}", "", f"*{typo(f['strate'])}*", "",
                  typo(d.EXPLI[f["id"]]), ""]
            abroges = []
            for (code, num), e in arts.items():
                if e["apres"] is None:
                    abroges.append(rp.cite(num))
                    continue
                av, ap = resserrer(e["avant"], e["apres"])
                if av and len(av) > 1200 and av.count("\n") > 5:
                    ls = av.split("\n")
                    av = "\n".join(ls[:4] + ["[…]"] + ls[-1:])
                av = cellule(av) if av is not None else "*(article nouveau)*"
                L += [f"| {nom(code, num)} |", "|---|", "| *Texte en vigueur* | *Texte proposé* |",
                      f"| {av} | {cellule(ap)} |", ""]
            if abroges:
                L += [f"| {', '.join(abroges)} {rp.NOMS.get(code, '')} |", "|---|",
                      "| *Texte en vigueur* | *Texte proposé* |",
                      f"| {ABROGE_DESC[f['id']]} | *Abrogé{'s' if len(abroges) > 1 else ''}* |", ""]
    return "\n".join(L)


def annexe(src, fiches):
    L = ["**RÉVISION DE LA CHAÎNE PÉNALE**", "", "*Annexe en trois colonnes*", "",
         "Texte en vigueur, texte proposé et commentaire", "", "Base LEGI du 20 octobre 2026", "", "---", ""]
    for f, arts in fiches:
        L += [f"## {f['id']}. {typo(f['titre'])}", ""]
        premier = True
        for (code, num), e in arts.items():
            av = cellule(e["avant"]) if e["avant"] is not None else "*(article nouveau)*"
            ap = cellule(e["apres"]) if e["apres"] is not None else "*(abrogé)*"
            com = typo(d.EXPLI[f["id"]]) if premier else "Voir ci-dessus."
            premier = False
            L += [f"| {nom(code, num)} |", "|---|", "| *Texte en vigueur* | *Texte proposé* | *Commentaire* |",
                  f"| {av} | {ap} | {com} |", ""]
    return "\n".join(L)


def main():
    src, fiches, st = d.calculer()
    (OUT / "dossier_revision_penale.md").write_text(dossier(src, fiches, st), encoding="utf-8")
    (OUT / "trois_colonnes_penal.md").write_text(annexe(src, fiches), encoding="utf-8")


if __name__ == "__main__":
    main()
