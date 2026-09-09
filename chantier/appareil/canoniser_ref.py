#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Applique la forme canonique aux valeurs affichées du REF.

Trois voies, dans l'ordre des règles : arrondir à l'entier, changer d'unité,
puis la décimale par exception quand le passage à l'entier déplacerait la valeur
de plus de un pour cent.

Seuls `valeur` d'un paramètre et `chiffre` d'un effet sont touchés. `exact`,
`operation`, `chaine`, `base` et `portee` demeurent : la précision y vit, et les
chaînes se calculent sur les exacts.

Usage : python3 canoniser_ref.py <entrée.json> <sortie.json>
"""

import json
import re
import sys

SEUIL = 0.01  # un pour cent

RE_DEC = re.compile(r"(?<![\d,])(\d{1,3}(?:[\u202f\u00a0 ]\d{3})*),(\d+)(?![\d,])")


def canoniser(texte, journal, ident, champ):
    """Rend le texte dont les décimales sont ramenées à l'entier quand l'écart
    reste sous le seuil. Journalise chaque décision.

    Une décomposition s'écrit à un rang unique : dès qu'un terme appelle la
    décimale, tous les termes du champ la conservent. Un agrégat entier suivi de
    termes décimaux se lit comme deux grandeurs de nature différente."""

    for m in RE_DEC.finditer(texte):
        val = float(
            m.group(1).replace("\u202f", "").replace("\u00a0", "").replace(" ", "")
            + "." + m.group(2)
        )
        if val and abs(val - round(val)) / abs(val) > SEUIL:
            for m2 in RE_DEC.finditer(texte):
                v2 = float(
                    m2.group(1).replace("\u202f", "").replace("\u00a0", "").replace(" ", "")
                    + "." + m2.group(2)
                )
                e2 = abs(v2 - round(v2)) / abs(v2) if v2 else 0
                journal.append((ident, champ, m2.group(0), m2.group(0), round(e2 * 100, 2), "exception"))
            return texte

    def remplacer(m):
        brut = m.group(0)
        ent_txt = m.group(1)
        val = float(
            (ent_txt.replace("\u202f", "").replace("\u00a0", "").replace(" ", ""))
            + "." + m.group(2)
        )
        entier = round(val)
        if val == 0:
            return brut
        ecart = abs(val - entier) / abs(val)
        if ecart <= SEUIL:
            # séparateur de milliers conservé quand la grandeur le portait
            sortie = "{:,}".format(entier).replace(",", "\u00a0") if entier >= 1000 else str(entier)
            journal.append((ident, champ, brut, sortie, round(ecart * 100, 2), "entier"))
            return sortie
        journal.append((ident, champ, brut, brut, round(ecart * 100, 2), "exception"))
        return brut

    return RE_DEC.sub(remplacer, texte)


def parcourir(o):
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from parcourir(v)
    elif isinstance(o, list):
        for x in o:
            yield from parcourir(x)


def main(argv):
    src, dst = argv[1], argv[2]
    d = json.load(open(src, encoding="utf-8"))
    journal = []
    for o in parcourir(d):
        ident = o.get("id")
        if not isinstance(ident, str):
            continue
        for champ in ("valeur", "chiffre"):
            v = o.get(champ)
            if isinstance(v, str) and v:
                neuf = canoniser(v, journal, ident, champ)
                if neuf != v:
                    o[champ] = neuf
    json.dump(d, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    entiers = [l for l in journal if l[5] == "entier"]
    exceptions = [l for l in journal if l[5] == "exception"]
    print("%d décimale(s) examinée(s) : %d ramenée(s) à l'entier, %d exception(s)"
          % (len(journal), len(entiers), len(exceptions)))
    print("")
    print("RAMENÉES À L'ENTIER")
    for i, c, a, b, e, _ in entiers:
        print("  %-14s %-8s %-10s → %-10s %.2f %%" % (i, c, a, b, e))
    print("")
    print("EXCEPTIONS — décimale conservée")
    for i, c, a, b, e, _ in exceptions:
        print("  %-14s %-8s %-10s %.2f %%" % (i, c, a, e))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
