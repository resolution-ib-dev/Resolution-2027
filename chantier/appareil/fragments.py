#!/usr/bin/env python3
"""Les fichiers cumulatifs du coffre, écrits par fragments datés.

**Le problème, mesuré.** `methode/journal.md` et `methode/arbitrages.md` ont
divergé entre deux fils le 20260916 — +2 295 o et +7 878 o après un versement.
Un fil restaure au début et reverse à la fin : il écrase ce qu'un autre a écrit
entre-temps. La garantie de `restaurer.py` bloque plutôt qu'elle ne fusionne,
parce qu'aucun script ne peut décider laquelle de deux versions vaut.

**La règle, arrêtée par l'auteur le 20260917.** Un fil n'écrit plus au fichier
cumulatif : il dépose un **fragment daté**, à lui seul, sous
`methode/fragments/<cible>/<AAAAMMJJ>-<fil>.md`. Deux fils qui travaillent en
même temps écrivent deux fichiers différents, et il n'y a plus de collision
possible — **un fragment ne se fusionne pas, il s'ajoute.**

**L'assemblage est idempotent, et c'est ce qui le rend sûr.** Le fichier
cumulatif porte une ligne de marque ; tout ce qui la précède est l'historique,
repris verbatim et jamais réécrit ; tout ce qui la suit est régénéré depuis les
fragments, triés par date puis par nom de fil. Deux fils qui assemblent en même
temps produisent le même octet, pourvu qu'ils voient les mêmes fragments. Le
dernier versement gagne, et il ne perd rien.

Ce qui est interdit et que le contrôle refuse : écrire à la main sous la ligne de
marque, et déposer deux fragments du même fil le même jour pour la même cible.

Usage : python3 fragments.py deposer <cible> <fil> <fichier|->
        python3 fragments.py assembler <cible> [...]
        python3 fragments.py etat
        python3 fragments.py epreuve
"""
import os
import re
import sys

RACINE = os.environ.get(
    "RESOLUTION_RACINE",
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Les cibles sont nommées ici et nulle part ailleurs : un fichier cumulatif qui
# n'y est pas continue de s'écrire à l'ancienne, et cela se voit.
CIBLES = {
    "journal": "methode/journal.md",
    "arbitrages": "methode/arbitrages.md",
}

MARQUE = "<!-- fragments : tout ce qui suit est régénéré par appareil/fragments.py -->"

NOM = re.compile(r"^(\d{8})-([a-z0-9][a-z0-9_-]*)\.md$")


def _dossier(cible):
    return os.path.join(RACINE, "methode", "fragments", cible)


def _cumulatif(cible):
    return os.path.join(RACINE, CIBLES[cible])


def _lire(p):
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""


def fragments(cible):
    """Les fragments d'une cible, triés par date puis par fil. Ordre stable."""
    d = _dossier(cible)
    if not os.path.isdir(d):
        return []
    out = []
    for f in os.listdir(d):
        m = NOM.match(f)
        if m:
            out.append((m.group(1), m.group(2), os.path.join(d, f)))
    return sorted(out)


def deposer(cible, fil, source):
    """Dépose un fragment. Refuse d'écraser : un fil, une date, une cible."""
    if cible not in CIBLES:
        return "cible inconnue — %s" % ", ".join(sorted(CIBLES))
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", fil):
        return "nom de fil invalide : minuscules, chiffres, tiret, souligné"
    import datetime
    jour = datetime.date.today().strftime("%Y%m%d")
    d = _dossier(cible)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "%s-%s.md" % (jour, fil))
    if os.path.exists(p):
        return ("fragment déjà déposé — %s. Un fil ne dépose qu'une fois par "
                "jour et par cible : complète le fragment existant." % p)
    txt = sys.stdin.read() if source == "-" else _lire(source)
    if not txt.strip():
        return "fragment vide — rien n'est déposé"
    open(p, "w", encoding="utf-8").write(txt.rstrip("\n") + "\n")
    return None


def assembler(cible):
    """Régénère la queue du fichier cumulatif depuis les fragments.

    L'historique — tout ce qui précède la ligne de marque — est repris verbatim.
    Il ne repasse jamais par le modèle et ne se réécrit pas.
    """
    p = _cumulatif(cible)
    courant = _lire(p)
    if MARQUE in courant:
        tete = courant.split(MARQUE)[0].rstrip("\n")
    else:
        tete = courant.rstrip("\n")
    corps = []
    for jour, fil, chemin in fragments(cible):
        corps.append("## %s — %s\n\n%s" % (jour, fil, _lire(chemin).strip()))
    neuf = tete + "\n\n" + MARQUE + "\n\n" + "\n\n".join(corps) + "\n"
    if neuf == courant:
        return 0, len(corps)
    open(p, "w", encoding="utf-8").write(neuf)
    return 1, len(corps)


def etat():
    lignes = []
    for cible in sorted(CIBLES):
        fr = fragments(cible)
        p = _cumulatif(cible)
        present = os.path.exists(p)
        marque = MARQUE in _lire(p) if present else False
        lignes.append("%-12s %2d fragment(s) · cumulatif %s · marque %s"
                      % (cible, len(fr),
                         "présent" if present else "ABSENT",
                         "posée" if marque else "à poser"))
        for jour, fil, _ in fr:
            lignes.append("    %s  %s" % (jour, fil))
    return "\n".join(lignes)


# --------------------------------------------------------------- l'épreuve
# Une règle sans son contrôle est une règle sans garde-fou. Celle-ci se prouve
# sur un corpus jetable : deux fils qui écrivent en même temps, et l'assemblage
# qui doit rendre le même octet quel que soit l'ordre.

def epreuve():
    import shutil
    import tempfile
    global RACINE
    vrai, echecs = RACINE, 0
    base = tempfile.mkdtemp(prefix="epreuve_fragments_")
    try:
        RACINE = base
        os.makedirs(os.path.join(base, "methode"), exist_ok=True)
        hist = "# Journal\n\n## 20260901 — avant les fragments\n\nHistorique.\n"
        open(os.path.join(base, "methode", "journal.md"), "w",
             encoding="utf-8").write(hist)

        d = _dossier("journal")
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "20260917-fil-a.md"), "w",
             encoding="utf-8").write("Ce que le fil A a fait.")
        open(os.path.join(d, "20260917-fil-b.md"), "w",
             encoding="utf-8").write("Ce que le fil B a fait.")

        assembler("journal")
        un = _lire(os.path.join(base, "methode", "journal.md"))

        # 1 — l'historique est intact
        ok = un.startswith(hist.rstrip("\n"))
        print("    %-46s %s" % ("l'historique est repris verbatim",
                                "ok" if ok else "ÉCHEC"))
        echecs += 0 if ok else 1

        # 2 — les deux fils sont là, aucun n'a écrasé l'autre
        ok = "fil A a fait" in un and "fil B a fait" in un
        print("    %-46s %s" % ("les deux fils coexistent",
                                "ok" if ok else "ÉCHEC"))
        echecs += 0 if ok else 1

        # 3 — l'assemblage est idempotent
        change, _ = assembler("journal")
        ok = change == 0 and _lire(os.path.join(base, "methode", "journal.md")) == un
        print("    %-46s %s" % ("rejouer l'assemblage ne change rien",
                                "ok" if ok else "ÉCHEC"))
        echecs += 0 if ok else 1

        # 4 — un fragment arrivé après ne perd pas les précédents
        open(os.path.join(d, "20260918-fil-c.md"), "w",
             encoding="utf-8").write("Ce que le fil C a fait.")
        assembler("journal")
        deux = _lire(os.path.join(base, "methode", "journal.md"))
        ok = all(x in deux for x in ("fil A a fait", "fil B a fait", "fil C a fait"))
        print("    %-46s %s" % ("un fragment tardif n'écrase rien",
                                "ok" if ok else "ÉCHEC"))
        echecs += 0 if ok else 1

        # 5 — l'ordre de dépôt ne change pas le résultat
        os.remove(os.path.join(d, "20260917-fil-a.md"))
        assembler("journal")
        open(os.path.join(d, "20260917-fil-a.md"), "w",
             encoding="utf-8").write("Ce que le fil A a fait.")
        assembler("journal")
        ok = _lire(os.path.join(base, "methode", "journal.md")) == deux
        print("    %-46s %s" % ("l'ordre de dépôt ne change pas la sortie",
                                "ok" if ok else "ÉCHEC"))
        echecs += 0 if ok else 1

        # 6 — deux dépôts du même fil le même jour sont refusés
        import datetime
        jour = datetime.date.today().strftime("%Y%m%d")
        open(os.path.join(d, "%s-fil-d.md" % jour), "w",
             encoding="utf-8").write("premier")
        src = os.path.join(base, "src.md")
        open(src, "w", encoding="utf-8").write("second")
        ok = deposer("journal", "fil-d", src) is not None
        print("    %-46s %s" % ("un second dépôt du même fil est refusé",
                                "ok" if ok else "ÉCHEC"))
        echecs += 0 if ok else 1
    finally:
        RACINE = vrai
        shutil.rmtree(base, ignore_errors=True)
    print("\nÉPREUVE : %s" % ("passée" if not echecs else "%d échec(s)" % echecs))
    return 1 if echecs else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    cmd = sys.argv[1]
    if cmd == "deposer":
        err = deposer(sys.argv[2], sys.argv[3],
                      sys.argv[4] if len(sys.argv) > 4 else "-")
        if err:
            print(err)
            sys.exit(1)
        print("fragment déposé")
    elif cmd == "assembler":
        cibles = sys.argv[2:] or sorted(CIBLES)
        for c in cibles:
            change, n = assembler(c)
            print("%s — %d fragment(s), %s" % (c, n,
                  "réécrit" if change else "inchangé"))
    elif cmd == "etat":
        print(etat())
    elif cmd == "epreuve":
        sys.exit(epreuve())
    else:
        print(__doc__)
        sys.exit(2)

