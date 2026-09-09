#!/usr/bin/env python3
"""Note l'éval du vecteur : compare les sorties de la skill à la vérité-terrain.

Trois verdicts, et un seul est un succès :

  concordance   même article, ou l'article cité est dans la fourchette relevée
  voisinage     même code, article différent — souvent le rôle qui diffère,
                création contre financement, pas une erreur
  discordance   autre chose. Échec, et il se compte.

**Deux dimensions, et pas une.** La version précédente mesurait le rappel et
ignorait la précision : un cas concordait dès qu'une adresse sur N intersectait
la clé. Une skill qui rendrait neuf adresses dont une juste aurait obtenu le même
verdict qu'une skill qui en rend une, juste. Le rappel dit si l'adresse est
trouvée ; la précision dit ce qu'il a fallu rendre pour la trouver. Les deux se
publient, jamais l'une pour l'autre.

**Le chemin des réponses est celui que la méthode prescrit**, et il se déduit du
lot. La version précédente lisait `reponses.json` à côté d'elle-même, ce que
plus aucun fil ne produisait.

**Les contaminés se vérifient contre la population.** Annoncer un compte fixe de
cas exclus sans regarder s'ils sont là fait sortir un dénominateur faux.

Usage : python3 noter_eval_gl.py [lot] [chemin des réponses]
        lot par défaut : le premier lot du banc d'épreuve
"""
import json
import pathlib
import re
import sys
import unicodedata

RACINE = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path(__file__).parent / "scinde"
LOTS = RACINE / "referentiels" / "lots_epreuve.json"


def chemin_reponses(lot):
    """Le chemin prescrit, dérivé du véhicule du lot. Un nom par lot : deux lots
    qui écriraient au même endroit se recouvriraient en silence."""
    return RACINE / "livrables" / "eval_gl" / (
        f"reponses_vecteur_mesure_{lot['vehicule']}.json")


def norm_art(a):
    """« L. 2334-1 » et « L2334-1 » sont la même adresse ; « 200 A » et
    « 200A » aussi. On ne normalise que la ponctuation et la casse, jamais
    le numéro."""
    a = unicodedata.normalize("NFKD", a)
    a = a.lower().replace(" ", " ")
    return re.sub(r"[.\s]+", "", a)


def norm_code(c):
    c = unicodedata.normalize("NFKD", c.lower())
    c = "".join(ch for ch in c if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", c).strip()


def atomes(adresses):
    """Les adresses comparables d'un jeu.

    Une fourchette — « L. 3334-1 à L. 3334-16-3 » — est UNE adresse au relevé,
    et le libellé entier ne s'apparie avec rien. Sa **borne basse** est
    pourtant une adresse à part entière, nommée en clair par la pièce : elle
    entre donc au jeu comparable, à côté du libellé entier.

    Le docstring du module l'annonçait — « l'article cité est dans la
    fourchette relevée » vaut concordance — et `verdict` ne le faisait pas :
    une skill qui rendait la borne basse sortait en voisinage. C'est un
    voisinage faux, et il ne se voit qu'ici.

    **L'intérieur de la fourchette ne se déplie pas.** Il demande le dépôt de
    droit et `plages_articles.py` ; `portes_ouvertes.py` est aux manquants. Une
    skill qui rend un article intérieur ne concorde donc pas encore, et cela se
    dit plutôt que de se deviner.
    """
    out = set()
    for a in adresses:
        out.add(norm_art(a))
        if " à " in a:
            out.add(norm_art(a.split(" à ", 1)[0]))
    return out


def verdict(mien, vrai):
    """mien / vrai : dicts portant `codes` et `articles`."""
    ma = atomes(mien["articles"])
    va = atomes(vrai["articles"])
    mc = {norm_code(x) for x in mien["codes"]}
    vc = {norm_code(x) for x in vrai["codes"]}
    if not va:
        # le dispositif ne cite aucun article : la cible n'a pas de siège codifié
        return ("concordance" if not ma else "voisinage"), len(ma & va), len(ma)
    if ma & va:
        return "concordance", len(ma & va), len(ma)
    if mc & vc:
        return "voisinage", 0, len(ma)
    if not mc or not vc:
        # l'un des deux ne nomme pas de code : on ne conclut pas au voisinage
        return ("voisinage" if not ma else "discordance"), 0, len(ma)
    return "discordance", 0, len(ma)


def main(argv):
    banc = json.loads(LOTS.read_text(encoding="utf-8"))
    cle_lot = argv[1] if len(argv) > 1 else banc["lots"][0]["cle"]
    lot = next((l for l in banc["lots"] if l["cle"] == cle_lot), None)
    if lot is None:
        print(f"lot inconnu : {cle_lot}. Lots au banc : "
              + ", ".join(l["cle"] for l in banc["lots"]))
        return 2
    rep_path = pathlib.Path(argv[2]) if len(argv) > 2 else chemin_reponses(lot)
    if not rep_path.exists():
        print(f"réponses absentes — {rep_path}")
        print("Le fil qui joue l'éval les écrit là, et pas ailleurs.")
        return 2

    cles = json.loads((SRC / "cles_eval.json").read_text(encoding="utf-8"))
    rep = json.loads(rep_path.read_text(encoding="utf-8"))

    # Les contaminés se vérifient : un compte annoncé sans regarder la
    # population fabrique un dénominateur faux.
    declares = [c for c in lot["contamines"] if c != "a_relever"]
    a_relever = [c for c in lot["contamines"] if c == "a_relever"]
    # La population d'un lot est celle de SON véhicule. Le filtre sur la
    # seule nature suffisait tant que la clé ne portait qu'une liasse ;
    # depuis qu'elle porte les trois, il faisait entrer les couples de
    # financement dans le dénominateur du lot de finances — six cas sans
    # réponse, et un taux faux par le bas.
    population = {k for k, v in cles.items()
                  if v["nature"] == "norme"
                  and v.get("vehicule", lot["vehicule"]) == lot["vehicule"]}
    contamines = [c for c in declares if c in population]
    fantomes = [c for c in declares if c not in population]

    lignes = []
    for cle, vrai in cles.items():
        if (vrai["nature"] != "norme" or cle not in population
                or cle in contamines):
            continue
        mien = rep.get(cle)
        if mien is None:
            lignes.append((cle, "absent", 0, 0, "", ""))
            continue
        v, justes, rendues = verdict(mien, vrai)
        lignes.append((cle, v, justes, rendues,
                       ", ".join(mien["articles"]) or "—",
                       ", ".join(vrai["articles"]) or "—"))

    if not lignes:
        print("aucun cas à noter")
        return 2

    largeur = max(len(l[0]) for l in lignes)
    print(f"lot {lot['cle']} — véhicule {lot['vehicule']}, "
          f"unité {lot['unite']}")
    print(f"réponses lues : {rep_path}\n")
    print(f"{'cas':<{largeur}}  {'verdict':<13} {'j/r':<7} "
          f"{'sorti':<34} attendu")
    print("-" * (largeur + 90))
    for cle, v, justes, rendues, mien, vrai in sorted(lignes,
                                                      key=lambda x: (x[1], x[0])):
        jr = f"{justes}/{rendues}" if rendues else "—"
        print(f"{cle:<{largeur}}  {v:<13} {jr:<7} {mien[:33]:<34} {vrai[:38]}")

    n = len(lignes)
    c = sum(1 for l in lignes if l[1] == "concordance")
    vo = sum(1 for l in lignes if l[1] == "voisinage")
    di = sum(1 for l in lignes if l[1] == "discordance")
    ab = sum(1 for l in lignes if l[1] == "absent")
    justes = sum(l[2] for l in lignes)
    rendues = sum(l[3] for l in lignes)

    print()
    print(f"population de norme au lot : {len(population)}")
    if contamines:
        print(f"  exclus pour contamination, vérifiés présents : "
              f"{len(contamines)} — {', '.join(sorted(contamines))}")
    if fantomes:
        print(f"  DÉCLARÉS CONTAMINÉS ET ABSENTS DE LA POPULATION : "
              f"{len(fantomes)} — {', '.join(sorted(fantomes))}")
        print("  le banc d'épreuve est en retard sur la clé ; le dénominateur "
              "annoncé serait faux.")
    if a_relever:
        print(f"  {len(a_relever)} contaminé(s) déclaré(s) au banc mais non "
              f"nommé(s) : la population aveugle réelle est inférieure de "
              f"{len(a_relever)}, et le taux ci-dessous est majoré d'autant.")
    print(f"  notés : {n}" + (f", dont {ab} sans réponse" if ab else ""))
    print()
    print("RAPPEL — l'adresse est-elle trouvée")
    print(f"  concordance  {c:>2}  {100*c/n:5.1f} %")
    print(f"  voisinage    {vo:>2}  {100*vo/n:5.1f} %")
    print(f"  discordance  {di:>2}  {100*di/n:5.1f} %")
    print(f"  rappel élargi (concordance + voisinage) : {100*(c+vo)/n:.1f} %")
    print()
    print("PRÉCISION — ce qu'il a fallu rendre pour la trouver")
    if rendues:
        print(f"  {justes} adresse(s) juste(s) sur {rendues} rendue(s) — "
              f"{100*justes/rendues:5.1f} %")
    else:
        print("  aucune adresse rendue")
    diffuses = [(l[0], l[2], l[3]) for l in lignes
                if l[1] == "concordance" and l[3] > 1]
    if diffuses:
        print(f"  {len(diffuses)} concordance(s) obtenue(s) sur plus d'une "
              f"adresse rendue :")
        for cle, j, r in sorted(diffuses, key=lambda x: -x[2]):
            print(f"      {cle} — {j} juste(s) sur {r} rendue(s)")
    print()
    print("Les deux taux se publient ensemble. Un rappel seul dit qu'on trouve, "
          "il ne dit pas ce qu'on ramasse avec.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
