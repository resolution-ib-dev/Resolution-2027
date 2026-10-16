#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confirme — ou infirme — qu'un article du véhicule ouvre bien une adresse.

La table des articles ouverts est un relevé, et un relevé se vérifie. Le défaut
le plus courant est la correspondance de préfixe : « 235 ter X » donné ouvert
par un article qui ne nomme que « 235 ter XB ». **Le compte de lignes fausses se
mesure en jouant `--table`, il ne se recopie pas d'une notice.**

Ce script rouvre le dispositif de l'article annoncé et y cherche l'adresse avec
une frontière de mot des deux côtés. Il rend :

    OUVERT      l'adresse est nommée par le dispositif — la pièce s'y adresse
    DOUTEUX     adresse courte et purement numérique, presque toujours un
                « article 1er » tronqué au relevé — ne vaut pas OUVERT
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

ORDRE = ("OUVERT", "DOUTEUX", "PREFIXE", "ABSENT")


def norm(s):
    """Apostrophes, espaces, tirets — la base et le texte déposé ne les écrivent
    pas pareil, et une comparaison brute échoue sur ce seul motif.

    Le point de la lettre de code se normalise aussi : un texte déposé écrit
    « L 31-10-7 » là où la table met « L. 31-10-7 », et sans cela une ligne
    juste sort ABSENT. Le cas est à l'article 7 de la loi de finances 2027.
    """
    s = (s.replace("’", "'").replace(" ", " ")
          .replace(" ", " ").replace("–", "-").replace("‑", "-"))
    return re.sub(r"\b(LO|[LRD])\.?[ ]+(?=\d)", r"\1. ", s)


def dispositifs(chemin):
    """Rend {numéro d'article du véhicule: dispositif}."""
    d = json.load(open(chemin, encoding="utf-8"))
    out = {}
    for a in d.get("articles", []):
        t = a.get("dispositif") or ""
        out[str(a.get("numero", "")).strip()] = norm(t if isinstance(t, str)
                                                     else "\n".join(t))
    return out


def discriminant(texte):
    """Ce qui distingue le texte porteur dans le dispositif.

    Pour une loi ou une ordonnance, son numéro — « n° 2022-1157 ». Pour un
    code, son nom. Sans ce discriminant, « l'article 1er de la loi n° 2022-1158 »
    fait passer pour ouverte une ligne qui annonce la loi n° 2022-1157, et la
    ligne est fausse. Le cas est à l'article 7 de la loi de financement 2027.
    """
    m = re.search(r"n°\s*([\d-]+)", norm(texte))
    return ("n° " + m.group(1)) if m else norm(texte).strip()


def juger(disp, adresse, texte=None):
    """Le verdict d'une adresse dans un dispositif donné.

    Trois pièges, et chacun a produit un verdict faux :

    - la frontière de fin. Sans elle « 235 ter X » mord sur « 235 ter XB » ;
    - la frontière de début. Sans elle « 1 » mord sur « 2026-103 » ;
    - le rang ordinal. Le dispositif écrit « article 1er », la table relève
      « 1 », et la frontière de mot ne voit pas la différence parce que le
      « 1 » nu se trouve ailleurs dans la pièce. Une adresse numérique dont le
      dispositif ne nomme que la forme ordinale sort DOUTEUX, jamais OUVERT :
      elle se relève en entier sur la pièce avant emploi.
    """
    a = norm(adresse).strip()
    frontiere = r"(?<![\w-])" + re.escape(a) + r"(?![\w-])"
    if a.isdigit():
        nu = r"(?:articles?|art\.)[^.;]{0,24}?" + frontiere
        ordinal = (r"(?:articles?|art\.)[^.;]{0,24}?(?<![\w-])"
                   + re.escape(a) + r"(?:er|ers|bis|ter|quater|quinquies)\b")
        # Une adresse nue ne suffit pas : elle doit être nommée au voisinage du
        # texte que la ligne annonce. Sinon l'article d'un texte voisin la fait
        # passer pour ouverte.
        d = discriminant(texte) if texte else None
        # Un code se nomme souvent « du même code » ou « du présent code » :
        # la fenêtre l'accepte, sans quoi la quasi-totalité des lignes de code
        # sortirait douteuse.
        reprise = r"(?:m[êe]me|pr[ée]sent)\s+code"
        for m in re.finditer(nu, disp, re.I):
            f = disp[m.start():m.end() + 200]
            if d is None or d in f or re.search(reprise, f, re.I):
                return "OUVERT"
        if re.search(nu, disp, re.I) or re.search(ordinal, disp, re.I):
            return "DOUTEUX"
        return "ABSENT"
    if re.search(frontiere, disp):
        return "OUVERT"
    return "PREFIXE" if a in disp else "ABSENT"


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
        compte = {k: 0 for k in ORDRE}
        faux = []
        for texte, adresse, arts in lire_table(argv[3]):
            verdicts = {juger(disp[n.strip()], adresse, texte)
                        for n in re.split(r"[,; ]+", arts)
                        if n.strip() in disp}
            v = next((k for k in ORDRE if k in verdicts), "ABSENT")
            compte[v] += 1
            if v != "OUVERT":
                faux.append((v, texte, adresse, arts))
        total = sum(compte.values())
        print(f"\n{total} lignes jugées sur {socle}")
        for k in ORDRE:
            print(f"  {k:8} {compte[k]}")
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
            print(f"           le dispositif nomme « {m.group(0)} », "
                  f"pas « {adresse} »")
    if v == "DOUTEUX":
        print("           adresse d'un ou deux chiffres : à relever en entier "
              "sur la pièce avant emploi")
    return 0 if v == "OUVERT" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
