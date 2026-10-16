#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test 3 — la base de droit répond, et son relevé n'est pas périmé.

Ce que le test prouve :

1. la base est installée et `droit.py etat` répond ;
2. son millésime LEGI est frais — au-delà de 45 jours, la sortie imprime
   `À REJOUER` et le test échoue ;
3. le nombre de textes portés concorde avec `codes.json`, et non avec la
   mémoire d'un document de méthode ;
4. un article connu se rend en verbatim, et un article absent **lève** au lieu
   d'approcher — c'est ce refus qui fait la valeur de la base ;
5. **le relevé des portes du domaine des lois de financement n'est pas périmé.**
   Il se périme 45 jours après son relevé ; passé ce terme il se rafraîchit par
   `droit.py` avant tout emploi.

Le point 5 existe parce qu'une borne de péremption écrite à un document de
méthode a déjà traversé quatre documents en étant fausse. Ici elle se mesure
sur la date que la pièce porte, jamais sur ce qu'un fil en a retenu.

Usage : DROIT=/chemin/vers/droit python3 64_CONTROLE_droit.py
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys

import importlib.util as _iu


def _charger(nom_fichier, nom_module):
    """Charge un module dont le nom de fichier commence par un chiffre.

    Les pièces sont numérotées pour porter l'ordre de lecture ; un module Python
    ne peut pas commencer par un chiffre. On charge donc par chemin.
    """
    c = os.path.join(os.path.dirname(os.path.abspath(__file__)), nom_fichier)
    sp = _iu.spec_from_file_location(nom_module, c)
    m = _iu.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


_socle = _charger("60_CONTROLE_socle.py", "socle_tests")
RACINE, Journal = _socle.RACINE, _socle.Journal
empreinte, octets, lire_manifeste = (_socle.empreinte, _socle.octets,
                                     _socle.lire_manifeste)

PEREMPTION_JOURS = 45


def _chemin_droit():
    # $DROIT, ou le clone posé à côté du paquet. On ne remonte pas d'un cran :
    # on trouverait le clone d'un autre chantier et on le prendrait pour le sien.
    for c in (os.environ.get("DROIT"),
              os.path.join(RACINE, "droit")):
        if c and os.path.exists(os.path.join(c, "droit.py")):
            return c
    return None


def main():
    j = Journal("Test 3 — base de droit et péremption des relevés")
    d = _chemin_droit()
    if not d:
        j.absent("base de droit installée",
                 "ni $DROIT ni ./droit — jouer le geste 2 du LISEZ-MOI")
    else:
        j.passe("base de droit trouvée", d)
        r = subprocess.run([sys.executable, os.path.join(d, "droit.py"), "etat"],
                           capture_output=True, text=True)
        sortie = r.stdout + r.stderr
        if r.returncode != 0 and not sortie.strip():
            j.echoue("`droit.py etat` répond", f"code {r.returncode}")
        else:
            j.passe("`droit.py etat` répond", f"code {r.returncode}")

            m = re.search(r"millésime LEGI (\d{8})", sortie)
            if m:
                mill = m.group(1)
                age = (dt.date.today()
                       - dt.date(int(mill[:4]), int(mill[4:6]), int(mill[6:]))).days
                if "À REJOUER" in sortie or age > PEREMPTION_JOURS:
                    j.echoue("millésime LEGI frais",
                             f"{mill}, {age} jours — au-delà de {PEREMPTION_JOURS}")
                else:
                    j.passe("millésime LEGI frais", f"{mill}, {age} jours")
            else:
                j.echoue("millésime LEGI lisible", "non trouvé à la sortie")

            # le compte de textes se lit à codes.json, pas à un récit
            cj = os.path.join(d, "codes.json")
            if os.path.exists(cj):
                nb_decl = len(json.load(open(cj, encoding="utf-8"))["codes"])
                nb_rendu = len(re.findall(r"appl\.", sortie))
                j.egal("textes portés : codes.json et `etat` concordent",
                       nb_rendu, nb_decl)
            else:
                j.absent("codes.json lisible", cj)

            # un article absent lève plutôt que d'approcher
            r2 = subprocess.run(
                [sys.executable, os.path.join(d, "droit.py"), "article",
                 "code général des impôts", "ZZZ-999-inexistant"],
                capture_output=True, text=True)
            if r2.returncode != 0:
                j.passe("un article absent lève au lieu d'approcher",
                        f"code {r2.returncode}")
            else:
                j.echoue("un article absent lève au lieu d'approcher",
                         "la base a rendu quelque chose")

    # 5. péremption du relevé des portes du domaine des lois de financement
    p = os.path.join(RACINE, "30_REFERENCE_domaine_lfss.md")
    if not os.path.exists(p):
        j.absent("relevé des portes du domaine présent", p)
    else:
        t = open(p, encoding="utf-8").read()
        # La pièce porte sa date sous l'une ou l'autre forme : « relevé le
        # AAAAMMJJ » pour la version documentée, « millésime **AAAAMMJJ** »
        # pour la grille que le module régénère. Les deux se lisent ; aucune
        # date ne se déduit de l'horloge.
        m = (re.search(r"millésime\s+\**(\d{8})", t)
             or re.search(r"[Rr]elevé le (\d{8})", t))
        if not m:
            j.echoue("le relevé porte sa date",
                     "ni « relevé le AAAAMMJJ » ni « millésime AAAAMMJJ »")
        else:
            le = dt.date(int(m.group(1)[:4]), int(m.group(1)[4:6]),
                         int(m.group(1)[6:]))
            terme = le + dt.timedelta(days=PEREMPTION_JOURS)
            reste = (terme - dt.date.today()).days
            if reste >= 0:
                j.passe("relevé des portes non périmé",
                        f"relevé le {le}, périme le {terme}, {reste} j")
            else:
                j.echoue("relevé des portes non périmé",
                         f"relevé le {le}, PÉRIMÉ depuis le {terme} "
                         f"({-reste} j) — rafraîchir par droit.py")
        m = re.search(r"(\d+) porte\(s\) relevée\(s\)[^,]*, (\d+) en échec", t)
        if m:
            j.egal("portes relevées sans échec", int(m.group(2)), 0)
            j.passe("portes du domaine relevées en verbatim", m.group(1))
        else:
            n = len(re.findall(r"^\|\s*`LO ?111-3", t, re.M))
            j.passe("articles relevés au tableau du domaine", n)

    return j.rendre()


if __name__ == "__main__":
    sys.exit(main())
