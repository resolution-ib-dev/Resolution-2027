#!/usr/bin/env python3
"""Plie un ensemble de fichiers en une pièce unique, dépliable par la règle qu'elle porte.

Même convention que le paquet machine : un fichier s'ouvre par une ligne faite de dix
chevrons ouvrants, du mot « fichier » et du chemin, et se ferme par une ligne faite de dix
chevrons fermants, du mot « fin » et du même chemin.
"""
import os
import sys

OUVRE = "<" * 10 + " fichier "
FERME = ">" * 10 + " fin "


def plier(base, chemins, sortie, entete):
    out = [entete, ""]
    for c in chemins:
        txt = open(os.path.join(base, c), encoding="utf-8").read()
        assert OUVRE not in txt and FERME not in txt, c
        out.append(OUVRE + c)
        out.extend(txt.split("\n"))
        out.append(FERME + c)
    open(sortie, "w", encoding="utf-8").write("\n".join(out) + "\n")
    return len(chemins)


def deplier(source, base):
    n = 0
    cur, buf = None, []
    for L in open(source, encoding="utf-8").read().split("\n"):
        if L.startswith(OUVRE):
            cur, buf = L[len(OUVRE):].strip(), []
            continue
        if L.startswith(FERME):
            assert L[len(FERME):].strip() == cur
            p = os.path.join(base, cur)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w", encoding="utf-8").write("\n".join(buf))
            n += 1
            cur = None
            continue
        if cur is not None:
            buf.append(L)
    return n


if __name__ == "__main__":
    if sys.argv[1] == "deplier":
        print("%d fichiers dépliés" % deplier(sys.argv[2], sys.argv[3]))

