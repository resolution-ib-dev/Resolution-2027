#!/usr/bin/env python3
"""Contrôle mécanique de la vérité-terrain des liasses — sorties `K1` à `K6`.

**Pourquoi ce module existe.** Le premier tour a rendu 36 %, et c'était la clé
qui était fausse, pas la skill (A-261). Deux défauts, tous deux dans
l'extracteur de vérité-terrain : la ligne de rattachement relevée comme une
adresse de code, et le suffixe en lettre coupé — « 200 A » → « 200 », « 244
quater B » → « 244 quater ». Une relecture à l'œil aurait validé les 36 %.
**Une clé fausse note faux, et seul un contrôle mécanique l'attrape.**

Ce module ne juge rien et ne corrige rien : il compte, et il n'imprime jamais
le contenu d'une clé. Un contrôle qui, pour dire qu'il a trouvé, nommerait le
cas et son adresse rendrait la moitié de la vérité-terrain — c'est le défaut
d'A-306, et il ne se refait pas ici. Les cas en anomalie sortent par leur
**clé de couple seule**, jamais avec l'adresse en cause.

  K1  une adresse de la clé provient de la ligne de rattachement
  K2  un suffixe en lettre a été coupé
  K3  un couple porte un dispositif ou un exposé vide
  K4  un cas de crédits est dans la population notée en rappel
  K5  une pièce diffusable du fil laisse fuir une adresse de la clé
  K6  la clé et la liasse ne portent pas la même population

Usage : python3 controle_cles_gl.py [pièce diffusable]...
"""
import json
import pathlib
import re
import sys
import unicodedata

SRC = pathlib.Path(__file__).parent / "scinde"
CLES = SRC / "cles_eval.json"
FICHES = SRC / "liasses_gl.json"

# Reprises telles quelles de `cles_eval_gl.py` : deux motifs divergents feraient
# deux vérités.
from cles_eval_gl import RE_ART, RE_RATTACHEMENT  # noqa: E402

# Un numéro suivi d'un suffixe en lettre capitale isolée, ou d'un ordinal latin
# lui-même suivi d'une lettre. C'est la forme que la coupe détruisait.
RE_SUFFIXE = re.compile(
    r"\b(\d+(?:\s*-\s*\d+)*(?:\s+(?:bis|ter|quater|quinquies|sexies|septies|"
    r"octies|novies|decies|undecies|duodecies|terdecies|quaterdecies|"
    r"quindecies|sexdecies|septdecies|octodecies|novodecies|vicies|unvicies|"
    r"duovicies|tervicies))*)\s+([A-Z])(?![a-zé])"
)


def norm(a):
    a = unicodedata.normalize("NFKD", a).lower()
    return re.sub(r"[.\s ]+", "", a)


def main(argv):
    cles = json.loads(CLES.read_text(encoding="utf-8"))
    fiches = json.loads(FICHES.read_text(encoding="utf-8"))
    par_cle = {f["cle"]: f for f in fiches}
    anomalies = {f"K{i}": [] for i in range(1, 7)}

    for cle, vrai in cles.items():
        disp = (SRC / "dispositif" / f"{cle}.txt").read_text(encoding="utf-8")
        lignes = disp.splitlines()
        ratt = [l for l in lignes if RE_RATTACHEMENT.match(l)]
        corps = "\n".join(l for l in lignes if not RE_RATTACHEMENT.match(l))
        retenues = {norm(a) for a in vrai["articles"]}

        # K1 — ce que la seule ligne de rattachement nomme ne doit pas être
        # dans la clé, sauf si le corps le nomme aussi de son côté.
        du_ratt = {norm(m.group(2)) for l in ratt for m in RE_ART.finditer(l)}
        du_corps = {norm(m.group(2)) for m in RE_ART.finditer(corps)}
        if du_ratt & retenues - du_corps:
            anomalies["K1"].append(cle)

        # K2 — pour chaque numéro suffixé que le corps porte, la clé doit
        # porter le numéro AVEC son suffixe, et non son préfixe nu.
        for m in RE_SUFFIXE.finditer(corps):
            entier = norm(m.group(1) + m.group(2))
            nu = norm(m.group(1))
            if nu in retenues and entier not in retenues:
                anomalies["K2"].append(cle)
                break

        # K3 — un couple vide n'est pas un cas.
        f = par_cle.get(cle)
        if f is None or f["disp_octets"] == 0 or f["edm_octets"] == 0:
            anomalies["K3"].append(cle)

        # K4 — les crédits ne reçoivent pas de taux mais un exercice de
        # conformité : l'adresse est dans l'exposé, mesurer la lecture ne
        # mesure rien. Un cas de crédits qui porterait la nature `norme`
        # entrerait dans le rappel et le majorerait.
        if vrai["nature"] == "credits" and vrai["articles"]:
            anomalies["K4"].append(cle)

    # K5 — aucune pièce diffusable ne laisse fuir une adresse de la clé.
    toutes = set()
    for vrai in cles.values():
        for a in vrai["articles"]:
            if len(norm(a)) >= 3:
                toutes.add(a)
    for chemin in argv[1:]:
        p = pathlib.Path(chemin)
        if not p.exists():
            anomalies["K5"].append(f"{p} absente")
            continue
        # L'aiguille se cherche derrière « article » ET « articles ». La
        # première rédaction ne cherchait que le singulier : une énumération
        # citée en exemple — « les articles 778, 784 B … » — passait le
        # contrôle en laissant fuir neuf adresses d'un coup. **Un contrôle trop
        # étroit rassure sans rien garantir**, et celui-ci s'est fait prendre
        # sur la première pièce qu'il avait à contrôler.
        texte = norm(p.read_text(encoding="utf-8"))
        fuites = sum(1 for a in toutes
                     if norm("article" + a) in texte
                     or norm("articles" + a) in texte)
        if fuites:
            anomalies["K5"].append(f"{p.name} — {fuites} adresse(s)")

    # K6 — la clé et la liasse portent la même population.
    if set(cles) != set(par_cle):
        anomalies["K6"].append(
            f"clé {len(cles)} · liasse {len(par_cle)} · "
            f"symétrique {len(set(cles) ^ set(par_cle))}")

    print(f"clés contrôlées : {len(cles)}  (contenu jamais imprimé)")
    echecs = 0
    for code in sorted(anomalies):
        v = anomalies[code]
        echecs += len(v)
        libelle = {
            "K1": "adresse venue de la ligne de rattachement",
            "K2": "suffixe en lettre coupé",
            "K3": "couple à dispositif ou exposé vide",
            "K4": "cas de crédits porté en population de rappel",
            "K5": "fuite d'adresse dans une pièce diffusable",
            "K6": "population divergente entre clé et liasse",
        }[code]
        print(f"  {code} {len(v):>2}  {libelle}"
              + (f" — {', '.join(sorted(v))}" if v else ""))
    print(f"\n{echecs} anomalie(s)")
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
