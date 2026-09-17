#!/usr/bin/env python3
"""Contrôle mécanique du lot C — découpage doctrinal en blocs.

B1  un pivot et un seul par bloc                                  bloque
B2  liste des solidaires close et datée                           bloque
B3  les cinq lignes du bilan remplies ou déclarées vides           bloque
B4  chaque perte porte une raccroche parmi les trois valeurs       bloque
C1  couverture : tout énoncé dans un bloc, un seul                 bloque
C2  aucun énoncé marqué direction n'est pivot                      bloque
C3  aucune ligne de gage employée (réservoir intact au lot C)      bloque
C4  interdits du paquet : nom d'organisation, adresse d'article,
    véhicule, verdict de recevabilité, renvoi à un fichier absent   bloque
D1  grandeur citée sous renvoi : aux paramètres de l'énoncé nommé   bloque
D2  grandeur sans renvoi : à un énoncé du bloc, à un énoncé nommé
    d'ailleurs, ou origine déclarée dans la phrase                  bloque
D3  agrégat annoncé par « soit » : se recalcule sur ses composantes bloque

Le contrôle du renvoi se joue en ouvrant la cible, jamais en lisant le nom.

**La série D se tire de ce que le destinataire doit trouver.** Les montants des
bilans sont recopiés à la main dans `blocs.json` : c'est le seul endroit du lot C
où une valeur peut mentir sans qu'aucun rejeu ne la contredise, puisque les
dix-sept fichiers se régénèrent fidèlement de cette source. Le contrôle ne lit
donc pas ce que le bilan dit de lui-même — il prend chaque grandeur du bilan et
exige de la retrouver là où le lecteur ira la chercher : aux paramètres chiffrés
de l'énoncé nommé. Une grandeur qui n'est nulle part n'est pas une imprécision de
rédaction, c'est un chiffre sans source dans une pièce qui se donne pour sourcée.

Trois sorties admises, et pas une quatrième : la grandeur est **aux paramètres**
de l'énoncé sous lequel elle est citée ; elle est **portée par un énoncé nommé
d'un autre bloc**, et le renvoi se compte ; ou son **origine est déclarée dans la
phrase** — décompte propre, calcul propre du paquet, annexe, corpus de fond,
constat, estimation, hypothèse, ordre de grandeur. Un agrégat fait exception à
l'exception : annoncé par « soit » et absent des paramètres, il ne vaut que s'il
se recalcule sur les composantes de même unité qui le précèdent.
"""
import json
import os
import re
import sys

# La racine se laisse déplacer : c'est ce qui permet à l'épreuve du contrôle de
# le jouer sur un corpus muté, sans toucher au corpus.
RACINE = os.environ.get(
    "RESOLUTION_RACINE",
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BLOCS = os.path.join(RACINE, "livrables", "blocs")
DECOUPAGE = os.path.join(RACINE, "livrables", "paquet_machine", "decoupage")
PAQUET = os.path.join(RACINE, "livrables", "paquet_machine")

RACCROCHES = {"renvoi vers un gain nommé", "reconstitution volontaire du flux",
              "absence assumée"}

# Une grandeur n'est jamais un perdant.
GRANDEUR = re.compile(
    r"^(les finances publiques|l'économie|la sphère publique|l'État|le budget"
    r"|les comptes publics|la croissance|le pays)\b", re.I)

INTERDITS = [
    ("nom d'organisation", re.compile(
        r"Cour des comptes|OCDE|Insee|INSEE|DGFiP|DREES|Fondapol|Ifrap|iFRAP"
        r"|Conseil des prélèvements obligatoires|Conseil d'orientation des retraites"
        r"|Assemblée nationale|Sénat|Union sociale pour l'habitat"
        r"|Secrétariat général du gouvernement")),
    ("adresse d'article", re.compile(
        r"\barticles?\s+(L\.|R\.|D\.|LO\s)|\barticle\s+\d|\bart\.\s*\d")),
    ("véhicule", re.compile(
        r"projet de loi de finances|loi de finances|loi de financement|PLFSS|\bPLF\b"
        r"|première partie|seconde partie|amendement")),
    ("verdict de recevabilité", re.compile(
        r"irrecevab|recevabilité|cavalier (budgétaire|social)")),
]

# Le bilan cite des pièces publiques par leur nature, jamais par leur auteur : la
# mention « annexe des dépenses fiscales » est l'emplacement d'une valeur transmise
# par le paquet, non un véhicule. Elle est la seule tolérance, et elle est nommée.
TOLERE = re.compile(r"annexe des dépenses fiscales")

# --- série D : la grandeur du bilan contre les paramètres de l'énoncé ---------

# Une origine se déclare dans la phrase qui porte la grandeur, jamais ailleurs.
ORIGINE = re.compile(
    r"décompte propre|calcul propre du paquet|annexe des dépenses fiscales"
    r"|corpus de fond|relevé des défauts du paquet|données 20\d\d"
    r"|constatée?s?|constaté|estimée?s?|estimé|hypothèses?|ordre de grandeur"
    r"|dénombrées?|recensés?|décrite?s?")

# Un millésime n'est pas une grandeur : il date, il ne compte pas.
MILLESIME = re.compile(r"\b20\d{6}\b")
ANNEE = re.compile(r"^20\d\d$")

NOMBRE = re.compile(
    r"(\d[\d   ]*(?:,\d+)?)\s*(Md€|M€|€|%|m²|millions|million)?")

AGREGAT = re.compile(
    r"soit (?:au moins |environ |plus de )?"
    r"(\d[\d   ]*(?:,\d+)?)\s*(Md€|M€|€|%|m²)?")

# Le bilan sépare ses termes par le point-virgule et par la phrase.
SEGMENT = re.compile(r"(?<=[.;])\s+")


def _norm(s):
    return re.sub(r"\s+", " ", s.replace(" ", " ").replace(" ", " ")).strip()


def _cle(valeur, unite):
    return (_norm(valeur) + " " + unite).strip()


def _flottant(v):
    return float(v.replace(" ", "").replace(",", "."))


def _nettoyer(segment):
    """Le segment sans ce qui n'est pas une grandeur : identifiants, millésimes.

    Les positions rendues par cette fonction sont celles du texte nettoyé : tout
    ce qui compare des places — l'agrégat et ses composantes, le « dont » qui les
    borne — travaille sur ce même texte, jamais sur le segment d'origine.
    """
    return MILLESIME.sub("", re.sub(r"M-\d{3}", "", segment))


def _grandeurs(t):
    """Les grandeurs d'un segment nettoyé, avec leur place dans ce texte."""
    out = []
    for m in NOMBRE.finditer(t):
        v, u = _norm(m.group(1)), m.group(2) or ""
        if not u and ANNEE.match(v.replace(" ", "")):
            continue
        out.append((v, u, _norm(m.group(0)), m.start()))
    return out


def _parametres(ident):
    """Les paramètres chiffrés d'un énoncé, lus en ouvrant son fichier."""
    f = os.path.join(DECOUPAGE, ident + ".md")
    if not os.path.exists(f):
        return ""
    m = re.search(r"\*\*Paramètres chiffrés\.\*\*(.*?)(?:\n\*\*|\Z)",
                  lire(f), re.S)
    return _norm(m.group(1)) if m else ""


def lire(p):
    return open(p, encoding="utf-8").read()


def main():
    data = json.load(open(os.path.join(BLOCS, "blocs.json"), encoding="utf-8"))
    blocs = data["blocs"]
    ids = sorted(f[:-3] for f in os.listdir(DECOUPAGE)
                 if re.fullmatch(r"M-\d{3}\.md", f))
    statuts = {}
    for i in ids:
        m = re.search(r"^\*\*Statut\.\*\*\s*(\w+)", lire(os.path.join(DECOUPAGE, i + ".md")), re.M)
        statuts[i] = m.group(1) if m else ""

    anomalies = {k: [] for k in ("B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4",
                                 "D1", "D2", "D3")}

    # Les paramètres chiffrés de toute la population, lus une fois.
    parametres = {i: _parametres(i) for i in ids}
    verifiees = renvois = 0

    place = {}
    for b in blocs:
        bid = b["id"]
        listes = [b["pivot"]] + [e[0] for cle in ("tombent", "conditions", "directions")
                                 for e in b.get(cle, [])]

        # B1 — un pivot et un seul
        if not isinstance(b.get("pivot"), str) or not b["pivot"]:
            anomalies["B1"].append("%s : pivot absent" % bid)
        if len(set(listes)) != len(listes):
            anomalies["B1"].append("%s : un énoncé figure deux fois dans le bloc" % bid)

        # C2 — un énoncé `direction` n'est pas pivot
        if statuts.get(b["pivot"]) == "direction":
            anomalies["C2"].append("%s : le pivot %s est marqué direction" % (bid, b["pivot"]))

        for e in listes:
            place.setdefault(e, []).append(bid)

        # B2 — liste close et datée, dans le fichier rendu
        f = os.path.join(BLOCS, bid + ".md")
        if not os.path.exists(f):
            anomalies["B2"].append("%s : fichier de bloc absent" % bid)
            continue
        txt = lire(f)
        if "Liste close et datée le 20260916" not in txt:
            anomalies["B2"].append("%s : clôture ou date absente" % bid)

        # B3 — les cinq lignes
        bl = b["bilan"]
        for ligne, val in (("supprime", bl.get("supprime")), ("rend", bl.get("rend")),
                           ("gage", bl.get("gage"))):
            if not val or not str(val).strip():
                anomalies["B3"].append("%s : ligne « %s » ni remplie ni déclarée vide" % (bid, ligne))
        if not bl.get("raccroches"):
            anomalies["B3"].append("%s : ligne « ce qui raccroche » vide" % bid)

        # B4 — chaque perte porte une raccroche admise, et chaque perdant en a une
        vus = set()
        for q, v, m in bl.get("raccroches", []):
            if v not in RACCROCHES:
                anomalies["B4"].append("%s : valeur de raccroche hors des trois admises — « %s »" % (bid, v))
            if not m or not m.strip():
                anomalies["B4"].append("%s : raccroche sans motif — « %s »" % (bid, q))
            if q in vus:
                anomalies["B4"].append("%s : perdant porté deux fois — « %s »" % (bid, q))
            vus.add(q)
            if GRANDEUR.search(q):
                anomalies["B4"].append("%s : une grandeur est écrite là où une personne était attendue — « %s »" % (bid, q))

        # C3 — aucune ligne de gage employée
        if "Absence de gage déclarée" not in bl.get("gage", ""):
            anomalies["C3"].append("%s : une ligne de gage est employée au lot C" % bid)

        # C4 — interdits, et renvois ouverts
        for nom, motif in INTERDITS:
            for m in motif.finditer(txt):
                deb = max(0, m.start() - 40)
                extrait = txt[deb:m.end() + 10].replace("\n", " ")
                if TOLERE.search(extrait):
                    continue
                anomalies["C4"].append("%s : %s — « %s »" % (bid, nom, m.group(0)))
        for m in re.finditer(r"\bM-\d{3}\b", txt):
            cible = os.path.join(DECOUPAGE, m.group(0) + ".md")
            if not os.path.exists(cible):
                anomalies["C4"].append("%s : renvoi vers un fichier absent du paquet — %s"
                                       % (bid, m.group(0)))
            else:
                lire(cible)  # ouverture effective de la cible

        # D1 à D3 — chaque grandeur du bilan contre les paramètres de l'énoncé
        pool_bloc = " ".join(parametres.get(e, "") for e in listes)
        for ligne in ("supprime", "rend"):
            for seg in SEGMENT.split(bl.get(ligne, "") or ""):
                nommes = re.findall(r"M-\d{3}", seg)
                sc = _nettoyer(seg)
                gs = _grandeurs(sc)
                if not gs:
                    continue
                pool = " ".join(parametres.get(e, "") for e in nommes)
                agregats = {}
                for m in AGREGAT.finditer(sc):
                    agregats[_norm(m.group(1))] = (m.group(2) or "", m.start())
                for v, u, brut, pos in gs:
                    cle = _cle(v, u)
                    ailleurs = sorted(e for e in parametres if cle in parametres[e])
                    if nommes and cle in pool:
                        verifiees += 1
                        continue
                    if not nommes and cle in pool_bloc:
                        verifiees += 1
                        continue
                    if v in agregats:
                        unite, place_agr = agregats[v]
                        # « dont » ouvre une décomposition, pas une addition : les
                        # composantes d'une somme sont celles qui suivent le dernier
                        # « dont » précédant l'agrégat, et elles seules.
                        debut = 0
                        for m in re.finditer(r"\bdont\b", sc[:place_agr]):
                            debut = m.end()
                        comp = [g for g in gs if debut <= g[3] < place_agr
                                and g[1] == unite and g[0] not in agregats]
                        # Une addition ne se contrôle que s'il y a quelque chose
                        # à additionner : « soit » introduit aussi des dérivations
                        # qui ne sont pas des sommes, et celles-là se prouvent par
                        # les paramètres ou par leur origine déclarée, comme le reste.
                        if len(comp) >= 2:
                            if abs(sum(_flottant(g[0]) for g in comp) - _flottant(v)) > 0.011:
                                anomalies["D3"].append(
                                    "%s.%s : agrégat « %s » ≠ somme de %s"
                                    % (bid, ligne, brut, " + ".join(g[2] for g in comp)))
                            else:
                                verifiees += 1
                            continue
                    if ailleurs:
                        if nommes:
                            anomalies["D1"].append(
                                "%s.%s : « %s » citée sous %s, portée par %s"
                                % (bid, ligne, brut, "/".join(nommes), ", ".join(ailleurs)))
                        else:
                            renvois += 1
                        continue
                    if ORIGINE.search(sc):
                        verifiees += 1
                        continue
                    cible = "D1" if nommes else "D2"
                    anomalies[cible].append(
                        "%s.%s : « %s » ni aux paramètres%s, ni ailleurs au paquet, "
                        "ni d'origine déclarée — « %s »"
                        % (bid, ligne, brut,
                           " de " + "/".join(nommes) if nommes else " du bloc",
                           _norm(seg)[:120]))

    # C1 — couverture
    for e in ids:
        n = len(place.get(e, []))
        if n == 0:
            anomalies["C1"].append("%s : dans aucun bloc" % e)
        elif n > 1:
            anomalies["C1"].append("%s : dans %d blocs — %s" % (e, n, ", ".join(place[e])))
    for e in place:
        if e not in ids:
            anomalies["C1"].append("%s : placé mais absent de la population" % e)

    print("population : %d énoncés, dont %d marqués direction"
          % (len(ids), sum(1 for i in ids if statuts[i] == "direction")))
    print("blocs      : %d, énoncés placés : %d" % (len(blocs), len(place)))
    print("grandeurs  : %d vérifiées aux paramètres ou d'origine déclarée, "
          "%d par renvoi à un énoncé d'un autre bloc" % (verifiees, renvois))
    echecs = 0
    for k in ("B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3"):
        a = anomalies[k]
        print("%s : %d" % (k, len(a)))
        for x in a[:20]:
            print("    " + x)
        echecs += len(a)
    print("TOTAL anomalies : %d" % echecs)
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())

