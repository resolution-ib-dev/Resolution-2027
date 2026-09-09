#!/usr/bin/env python3
"""Scinde les liasses GL en couples (dispositif, exposé sommaire).

Garde A-249 : le dispositif est scellé — écrit sur disque, jamais affiché.
Seuls l'en-tête, le rattachement et l'exposé sommaire alimentent l'éval.

L'unité n'est pas le numéro d'amendement mais le COUPLE dispositif / exposé
sommaire : GL-II-7 porte un seul numéro et six déclinaisons, chacune avec son
tableau de crédits et son propre exposé. Découper sur le numéro perdait cinq
exposés sur six.
"""
import hashlib
import json
import pathlib
import re
from collections import Counter

SRC = pathlib.Path(__file__).parent
OUT = SRC / "scinde"
for d in ("dispositif", "edm"):
    (OUT / d).mkdir(parents=True, exist_ok=True)

# `search` et non `match` : une tête porte parfois un glyphe de police
# symbole en préfixe (U+F02C sur l'amendement II-13).
#
# Étendu à la liasse de financement : la tête y écrit `[PLFSS]`, sans partie et
# sans espace, là où les deux liasses de finances écrivent `[PLF I]` et
# `[PLF II]`. Le jeton de partie retenu est celui du nommage déjà en service —
# `I`, `II`, `PLFSS` —, de sorte que les clés d'un rejeu apparient celles du
# premier tour.
RE_TETE = re.compile(r"Amendement\s+n°\s*(\S+)\s*\[(PLF\s+I{1,2}|PLFSS)\]\s*:\s*(.*)")

RE_DISP = re.compile(r"^\s*Dispositif\s*$")
RE_EDM = re.compile(r"^\s*Expos[eé]\s+sommaire\s*$")

RE_ADD = re.compile(r"^\s*(?:Article\s+additionnel\s+)?(Avant|Apr[eè]s)\s+l[’']article\s+(\S+)", re.I)
RE_OUVERT = re.compile(r"^\s*[AÀ]?\s*(?:l[’'])?[Aa]rticle\s+(\d+)\b", re.I)
RE_BRUIT = re.compile(r"^\s*(Programmes|Mission|Autorisations|Crédits|TOTAL|SOLDE|\|)", re.I)


def partie_de(jeton):
    j = re.sub(r"\s+", " ", jeton).strip()
    return "PLFSS" if j == "PLFSS" else j.split(" ", 1)[1]


def qualifie(ligne):
    """(variante, article visé) — A-253."""
    if not ligne or RE_BRUIT.match(ligne):
        return None, None
    m = RE_ADD.match(ligne)
    if m:
        return "absolu", m.group(2).rstrip(".:")
    m = RE_OUVERT.match(ligne)
    if m:
        return "article_ouvert", m.group(1)
    return "a_determiner", None


def couples(chemin):
    lignes = chemin.read_text(encoding="utf-8").splitlines()
    marques = []
    for i, l in enumerate(lignes):
        if RE_TETE.search(l):
            m = RE_TETE.search(l)
            marques.append(("tete", i, (m.group(1).lstrip("°").strip(),
                                        partie_de(m.group(2)),
                                        m.group(3).strip())))
        elif RE_DISP.match(l):
            marques.append(("disp", i, None))
        elif RE_EDM.match(l):
            marques.append(("edm", i, None))

    tete = None
    chapeau = (None, None)  # rattachement hérité, posé par un dispositif-chapeau
    rang = 0
    out = []
    for k, (genre, i, data) in enumerate(marques):
        if genre == "tete":
            tete = data
            chapeau = (None, None)
            rang = 0
            continue
        if genre != "disp":
            continue
        # que vient-il après ce dispositif ?
        suite = marques[k + 1] if k + 1 < len(marques) else None
        deb_corps = i + 1
        fin_corps = suite[1] if suite else len(lignes)
        corps = lignes[deb_corps:fin_corps]
        ratt = next((l.strip() for l in corps if l.strip()), "")
        variante, article = qualifie(ratt)

        if suite is None or suite[0] != "edm":
            # dispositif-chapeau : il ne porte qu'un rattachement, pas de cas
            if variante:
                chapeau = (variante, article)
            continue

        i_edm = suite[1]
        suivant = marques[k + 2] if k + 2 < len(marques) else None
        fin_edm = suivant[1] if suivant else len(lignes)
        edm = "\n".join(lignes[i_edm + 1 : fin_edm]).strip()
        disp = "\n".join(corps).strip()

        # un rattachement non qualifiable hérite du chapeau : les six
        # déclinaisons de II-7 ouvrent sur un tableau de crédits, leur
        # rattachement est porté une fois en tête d'amendement.
        if variante in (None, "a_determiner") and chapeau[0]:
            variante, article = chapeau
        rang += 1
        num, partie, titre = tete if tete else ("?", "?", "")
        cle = f"GL-{partie}-{num}" + (f".{rang}" if rang > 1 or _multi(marques, k) else "")
        (OUT / "dispositif" / f"{cle}.txt").write_text(disp, encoding="utf-8")
        (OUT / "edm" / f"{cle}.txt").write_text(edm, encoding="utf-8")
        out.append(
            {
                "cle": cle,
                "partie": partie,
                "amendement": num,
                "titre": re.sub(r"\s+", " ", titre),
                "rattachement": ratt[:80],
                "variante": variante,
                "article_plf": article,
                # L'état B vit à l'article 49 du texte déposé de la loi de
                # finances 2026. Le repère est propre à ce véhicule et à ce
                # millésime : le borner à la partie évite qu'un article 49
                # d'une liasse de financement passe pour des crédits.
                "nature": ("credits"
                           if partie in ("I", "II")
                           and variante == "article_ouvert" and article == "49"
                           else "norme"),
                "disp_octets": len(disp.encode()),
                "disp_sha256": hashlib.sha256(disp.encode()).hexdigest()[:16],
                "edm_octets": len(edm.encode()),
            }
        )
    return out


def _multi(marques, k):
    """Vrai si la tête courante porte plus d'un couple."""
    n = 0
    for genre, i, _ in marques[: k + 1][::-1]:
        if genre == "tete":
            break
    debut = next(
        (j for j in range(k, -1, -1) if marques[j][0] == "tete"), 0
    )
    fin = next(
        (j for j in range(k + 1, len(marques)) if marques[j][0] == "tete"), len(marques)
    )
    for j in range(debut, fin - 1):
        if marques[j][0] == "disp" and marques[j + 1][0] == "edm":
            n += 1
    return n > 1


def main():
    fiches = []
    # Les liasses converties vivent dans `scinde/`, avec le reste de l'atelier
    # de l'éval : elles se refont d'une commande depuis les pièces jointes et
    # n'ont rien à faire au dépôt. `scinde/` est ignoré, comme `eval/` l'est
    # pour l'atelier de la rédaction cible (A-363). L'ancien emplacement — la
    # racine de `appareil/` — reste lu, pour qu'un fil qui a déjà converti là
    # ne refasse pas le travail.
    for motif in ("*PartieI.txt", "*PartieII.txt", "*PLFSS2026.txt"):
        trouve = sorted(OUT.glob(motif)) or sorted(SRC.glob(motif))
        if not trouve:
            print(f"liasse absente pour {motif} — elle entre par pièce jointe")
            continue
        fiches += couples(trouve[0])
    (OUT / "liasses_gl.json").write_text(
        json.dumps(fiches, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"{len(fiches)} couples dispositif / exposé sommaire")
    print(f"  numéros d'amendement distincts : "
          f"{len({(f['partie'], f['amendement']) for f in fiches})}")
    print("  variante :", dict(Counter(f["variante"] for f in fiches)))
    print("  nature   :", dict(Counter(f["nature"] for f in fiches)))
    print("  exposé vide :", sum(1 for f in fiches if f["edm_octets"] == 0))
    print("  dispositif vide :", sum(1 for f in fiches if f["disp_octets"] == 0))


if __name__ == "__main__":
    main()
