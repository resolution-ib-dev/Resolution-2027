#!/usr/bin/env python3
"""Note l'éval de `expose-sommaire` — quatre dimensions, quatre résultats.

L'éval donne le **dispositif** de chaque amendement GL et scelle son exposé.
La skill rédige ; ce module compare. A-254 commande la façon de comparer : ce
n'est pas une égalité de rédaction, c'est une correspondance.

Quatre dimensions, et elles ne se moyennent pas.

  forme      fourchette tenue sous la règle de décompte de la skill, trois
             temps présents, part du constat déclarée. Entièrement mécanique.
  sources    **le taux qui compte.** La skill retrouve-t-elle une pièce
             opposable ? Une pièce DIFFÉRENTE de celle de GL mais également
             opposable est une réussite : on mesure la qualité de la recherche,
             pas la conformité à GL.
  objectif   l'objectif politique nommé. Se note à la main, les deux textes
             côte à côte : aucune balise ne le porte, et le deviner par script
             fabriquerait une clé fausse.
  constat    les faits avancés recoupent-ils ceux de GL. À la main.

Le corpus de GL n'est pas le plafond. Sur les sources, il tient sa propre règle
dans 10 exposés sur 36 : **une sortie mieux sourcée que GL n'est pas un écart,
c'est l'objectif.** Le module le dit plutôt que de le compter en faute.
"""
import json
import pathlib
import re
import unicodedata

ICI = pathlib.Path(__file__).parent
SRC = ICI / "scinde"
CLES = json.loads((SRC / "cles_eval_expose.json").read_text(encoding="utf-8"))
REP = ICI / "reponses_expose_sommaire.json"
CONTAMINES = set()  # aucun : les exposés n'ont jamais été lus comme sorties


def plat(s):
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))


# Une pièce est opposable si son émetteur est une autorité publique, une
# juridiction financière, un institut statistique ou une publication datée.
# La liste est ouverte : elle sert à reconnaître, jamais à restreindre.
OPPOSABLES = [
    "cour des comptes", "conseil des prelevements", "ocde", "insee", "dares",
    "unedic", "tresor", "vie publique", "senat", "assemblee nationale",
    "conseil d'etat", "conseil d etat", "igf", "inspection generale",
    "legifrance", "eurostat", "banque de france", "drees", "depp",
    "france strategie", "haut conseil", "commission europeenne",
    "rapport", "annexe", "projet annuel de performance", "voies et moyens",
]
RE_ANNEE = re.compile(r"\b(?:19|20)\d{2}\b")


def opposable(note):
    """Une note est opposable si elle nomme un émetteur reconnaissable ET porte
    une date. Sans date, une pièce ne se retrouve pas."""
    p = plat(note)
    return bool(RE_ANNEE.search(note)) and any(o in p for o in OPPOSABLES)


def verdict_sources(mien, vrai):
    """Trois issues, et la deuxième n'est pas un échec.

    concordance   au moins une pièce opposable, et une autorité commune avec GL
    equivalence   au moins une pièce opposable, aucune autorité commune —
                  la skill a trouvé ailleurs, et aussi bien
    defaut        aucune pièce opposable. **Seul échec.**
    """
    miennes = [n for n in mien.get("notes", []) if opposable(n)]
    if not miennes:
        return "defaut"
    aut_gl = {a for n in vrai["notes"] for a in n["autorites"]}
    aut_gl.discard("GenerationLibre")
    if not aut_gl:
        # GL ne source rien d'opposable : toute pièce opposable est un gain net
        return "concordance"
    mp = plat(" ".join(miennes))
    if any(plat(a) in mp for a in aut_gl):
        return "concordance"
    return "equivalence"


def main():
    if not REP.exists():
        print(f"absent : {REP.name}")
        print("Le fil de mesure écrit ses sorties là, une entrée par cas :")
        print('  {"GL-I-19": {"mots": 248, "temps": 3, "part_constat": 0.31,')
        print('               "notes": ["Cour des comptes, ..., 2025"],')
        print('               "objectif_politique": "..."}}')
        return 1

    rep = json.loads(REP.read_text(encoding="utf-8"))
    lignes = []
    for cle, vrai in CLES.items():
        if cle in CONTAMINES:
            continue
        mien = rep.get(cle)
        if mien is None:
            lignes.append((cle, "absent", "absent", None, None))
            continue
        n = mien.get("mots")
        forme = "conforme" if (n and 200 <= n <= 300) else "hors fourchette"
        if mien.get("temps", 3) < 3:
            forme += " · deux temps"
        lignes.append((cle, forme, verdict_sources(mien, vrai), n, vrai["mots"]))

    larg = max(len(l[0]) for l in lignes)
    print(f"{'cas':<{larg}}  {'forme':<26} {'sources':<13} {'mots':>5} {'GL':>5}")
    print("-" * (larg + 56))
    for cle, forme, src, n, gl in sorted(lignes, key=lambda x: (x[2], x[0])):
        print(f"{cle:<{larg}}  {forme:<26} {src:<13} "
              f"{str(n or '—'):>5} {str(gl):>5}")

    tot = len(lignes)
    conf = sum(1 for l in lignes if l[1].startswith("conforme"))
    co = sum(1 for l in lignes if l[2] == "concordance")
    eq = sum(1 for l in lignes if l[2] == "equivalence")
    de = sum(1 for l in lignes if l[2] == "defaut")
    print()
    print(f"{tot} cas notés")
    print(f"  FORME — dans la fourchette : {conf}/{tot}  {100*conf/tot:.1f} %")
    print(f"          référence GL sous la même règle : "
          f"{sum(1 for v in CLES.values() if v['dans_fourchette'])}/{len(CLES)}")
    print(f"  SOURCES — concordance {co}  équivalence {eq}  "
          f"**défaut {de}**  → opposable dans {100*(co+eq)/tot:.1f} % des cas")
    print(f"          référence GL : 10 exposés sur 36 portent une note")
    print()
    print("  OBJECTIF POLITIQUE et CONSTAT : à noter à la main, les deux textes")
    print("  côte à côte. Aucune balise ne les porte.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
