#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confirme — ou infirme — qu'un article du véhicule ouvre bien une adresse.

La table des articles ouverts est un relevé, et un relevé se vérifie. Le défaut
qu'il porte est toujours le même : la correspondance de préfixe. « 235 ter X »
donné ouvert par un article qui ne nomme que « 235 ter XB ». Sept lignes sur
quatre cent quarante-deux sont dans ce cas sur la loi de finances 2027.

Ce script rouvre le dispositif de l'article annoncé et y cherche l'adresse avec
une frontière de mot. Il rend :

    OUVERT      l'adresse est nommée par le dispositif — la pièce s'y adresse
    PREFIXE     seule une adresse plus longue est nommée — faux de la table
    ABSENT      l'adresse n'est pas dans le dispositif — vaut « aucun »

Usage :
    python3 44_SCRIPT_article_ouvert.py SOCLE.json "<article du véhicule>" "<adresse>"
    python3 44_SCRIPT_article_ouvert.py SOCLE.json --table ARTICLES_OUVERTS.tsv

Le socle est `socle_texte_plf2027.json` ou `socle_texte_plfss2027.json`, au clone
du dépôt. La table est le `.tsv` du même millésime et du même véhicule.
"""
import json
import re
import sys


def norm(s):
    """Apostrophes et espaces — la base et le texte déposé ne les écrivent pas
    pareil, et une comparaison brute échoue sur ce seul motif."""
    return (s.replace("’", "'").replace(" ", " ")
             .replace(" ", " ").replace("–", "-").replace("‑", "-"))


def dispositifs(chemin):
    """Rend {numéro d'article du véhicule: dispositif}."""
    d = json.load(open(chemin, encoding="utf-8"))
    out = {}
    for a in d.get("articles", []):
        t = a.get("dispositif") or ""
        out[str(a.get("numero", "")).strip()] = norm(t if isinstance(t, str)
                                                     else "\n".join(t))
    return out


def juger(disp, adresse):
    """OUVERT, PREFIXE ou ABSENT, pour une adresse dans un dispositif donné."""
    a = norm(adresse).strip()
    # frontière : ni lettre, ni chiffre, ni tiret ne suit l'adresse. Sans quoi
    # « 235 ter X » mord sur « 235 ter XB », et c'est tout le défaut.
    if re.search(re.escape(a) + r"(?![\w-])", disp):
        return "OUVERT"
    if a in disp:
        return "PREFIXE"
    return "ABSENT"


def lire_table(chemin):
    """Rend (texte, adresse, articles du véhicule) par ligne de la table."""
    for l in open(chemin, encoding="utf-8"):
        if l.startswith("#") or not l.strip():
            continue
        c = l.rstrip("\n").split("\t")
        if len(c) >= 7:
            yield c[0].strip(), c[1].strip(), c[6].strip()


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    socle = argv[1]
    disp = dispositifs(socle)

    if argv[2] == "--table":
        if len(argv) < 4:
            print("  table attendue après --table")
            return 2
        compte = {"OUVERT": 0, "PREFIXE": 0, "ABSENT": 0}
        faux = []
        for texte, adresse, arts in lire_table(argv[3]):
            verdicts = set()
            for n in re.split(r"[,; ]+", arts):
                n = n.strip()
                if n in disp:
                    verdicts.add(juger(disp[n], adresse))
            v = ("OUVERT" if "OUVERT" in verdicts
                 else "PREFIXE" if "PREFIXE" in verdicts else "ABSENT")
            compte[v] += 1
            if v != "OUVERT":
                faux.append((v, texte, adresse, arts))
        total = sum(compte.values())
        print(f"\n{total} lignes jugées sur {socle}")
        for k, n in compte.items():
            print(f"  {k:8} {n}")
        if faux:
            print("\n  lignes à ne pas employer comme articles ouverts :")
            for v, texte, adresse, arts in faux:
                print(f"    {v:8} {texte} · {adresse} · annoncé article {arts}")
        return 1 if faux else 0

    if len(argv) < 4:
        print("  adresse attendue")
        return 2
    art, adresse = argv[2].strip(), argv[3]
    if art not in disp:
        print(f"  ABSENT  l'article {art} n'est pas au socle")
        return 1
    v = juger(disp[art], adresse)
    print(f"  {v:8} {adresse} · article {art} du véhicule")
    if v == "PREFIXE":
        m = re.search(re.escape(norm(adresse)) + r"[\w-]+", disp[art])
        if m:
            print(f"           le dispositif nomme « {m.group(0)} », pas « {adresse} »")
    return 0 if v == "OUVERT" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
