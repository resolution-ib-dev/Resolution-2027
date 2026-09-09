# -*- coding: utf-8 -*-
"""Export des données projetées, source unique des livrables aval.

La jointure du REF et du référentiel des positions se fait une seule fois, ici.
L'extrait et l'interface se servent du même fichier : aucun des deux ne rejoue
la projection pour son compte, et aucun ne peut diverger de l'autre.

Ce script existait jusqu'ici en ligne de commande, rejoué à la main à chaque
génération. Un dérivé se régénère, il ne se retape pas.

Usage : python3 exporter_donnees.py REF.json Positions.json Notes.json sortie.json
"""
import importlib.util
import json
import os
import sys


def charger(nom, fichier):
    ici = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location(nom, os.path.join(ici, fichier))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv):
    if len(argv) < 5:
        print(__doc__)
        return 2
    ref_p, pos_p, notes_p, sortie = argv[1:5]
    gi = charger("gi", "generer_inventaire.py")
    g2 = charger("g2", "generer_extrait.py")

    ref = json.load(open(ref_p, encoding="utf-8"))
    pos = json.load(open(pos_p, encoding="utf-8"))
    notes = json.load(open(notes_p, encoding="utf-8"))
    if isinstance(notes, dict) and "notes" in notes:
        notes = notes["notes"]
    if isinstance(notes, list):
        notes = {n["id"]: n for n in notes}

    brutes, _, anomalies, _, cats, _ = gi.assembler(ref, pos, notes)
    if anomalies:
        for a in anomalies:
            print("  anomalie :", a)
        print(f"{len(anomalies)} anomalie(s) de jointure — le livrable ne sort pas")
        return 1

    # Le degré `complété` est ce que la dérivation a ajouté et que les auteurs
    # n'ont pas validé. Il ne sort pas.
    gardees = [l for l in brutes if l["degre"] != "complété"]
    ecartees = len(brutes) - len(gardees)

    out = {
        "axes": [{"id": a["id"], "t": a["intitule"]} for a in ref["axes"]],
        "groupes": pos.get("groupes", []),
        "promesses": pos.get("promesses", []),
        "cats": {}, "lignes": [],
    }
    vues = set()
    for l in gardees:
        vues.add(l["categorie"])
        apport = g2.epurer_texte(l.get("apport"))
        out["lignes"].append({
            "c": l["categorie"], "p": l["position"],
            "a": l["ctx"].get("axe", ""), "n": l["ancrage"],
            "e": apport or g2.enonce(l),
            "g": g2.grandeur(l),
            "j": g2.epurer_texte(l.get("justification")),
            "k": g2.epurer_texte(l.get("contrepartie")),
            "r": g2.epurer_texte(l.get("relais")),
            "dur": l.get("raccroche") == g2.AUCUNE,
        })
    for c in sorted(vues):
        if c in cats:
            k = cats[c]
            out["cats"][c] = {"t": k["terme"],
                              "d": g2.epurer_texte(k.get("definition", "")),
                              "e": (k.get("effectif") or "").strip()}

    json.dump(out, open(sortie, "w", encoding="utf-8"), ensure_ascii=False)
    rediges = sum(1 for l in gardees
                  if l["position"] == "gagnant" and (l.get("apport") or "").strip())
    gains = sum(1 for l in gardees if l["position"] == "gagnant")
    print(f"{sortie} — {len(out['lignes'])} ligne(s), {len(out['cats'])} "
          f"catégorie(s), {ecartees} écartée(s) au degré complété")
    print(f"  {rediges} gain(s) rédigé(s), {gains - rediges} en régime transitoire")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
