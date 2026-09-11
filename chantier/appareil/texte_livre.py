#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Texte du livre imprimé — extraction mécanique de l'épreuve validée.

Rend `livre/texte_livre.json`, qui porte le verbatim du livre tel qu'il est
composé : une entrée par page, les lignes de composition dans leur ordre,
et rien d'autre. C'est la strate 1 du corpus depuis le bon à tirer.

RÈGLES D'EXTRACTION, et elles sont toutes mécaniques
----------------------------------------------------
1. Le texte vient de `pdftotext -layout`, jamais du modèle. Aucune ligne
   n'est retapée.
2. **Le pied de composition se retire.** Chaque page porte en dernière ligne
   le nom du fichier InDesign, le folio et l'horodatage de composition —
   `488686WXT_..._PC.indd 105    10/09/2026 14:08:30`. Ce n'est pas du livre,
   c'est de l'atelier d'imprimerie. Le folio qu'il porte sert à contrôler
   celui de la tête de page, puis il tombe.
3. **Le folio de tête se retire et se garde comme numéro.** La première ligne
   non vide d'une page de corps est le folio seul. Il devient le champ `folio`
   et sort du texte : c'est de la pagination, pas de la rédaction. **Il ne se
   retire que s'il concorde avec le folio du pied**, qui fait autorité : une
   ouverture de chapitre porte en tête son numéro de chapitre, et le retirer
   sans ce départage effacerait une ligne du livre — quatorze fois.
4. **Aucune césure n'est recollée dans le versé.** Une ligne qui finit par un
   trait d'union reste telle quelle. Le recollement est un jugement — le
   trait d'union appartient au mot (« sous-directeur ») ou à la composition
   (« comp-table ») — et un jugement ne se plie pas dans du verbatim. Il est
   rendu à part, au champ `coupes`, par la règle du § 5, et le texte coulant
   se dérive à la demande par `couler()`.
5. **La règle de coupe, et elle se recompte.** Un mot coupé en fin de ligne
   garde son trait d'union si le même composé, trait d'union compris, se
   retrouve d'un seul tenant ailleurs dans le livre ; à défaut, si **ses deux
   éléments sont capitalisés** et qu'un composé de même élément de gauche
   s'écrit entier — c'est ce qui tranche « Cross-Sectional » par
   « Cross-Country », sur la même ligne du même titre, comme le 20260910 l'a
   tranché sur pièce. Sinon le trait d'union est une césure et il tombe.
   Chaque coupe porte son verdict et son motif, et les deux verdicts rendus
   sur pièce le 20260910 — p. 40 « sous-directeur », p. 147
   « Cross-Sectional » — se reproduisent.

   *La capitalisation n'est pas un ornement de la règle, elle en est la
   borne.* Sans elle, le repli sur l'élément de gauche gardait quatre traits
   d'union qui étaient des césures — « main-tenir », « entre-prises »,
   « sur-monté », « de-France » —, et un verbatim faux est pire qu'un
   verbatim coupé.

CE QUE CE MODULE NE FAIT PAS
----------------------------
Il ne compare rien, il ne note rien, il ne relève aucun écart. La comparaison
d'une épreuve à une autre est l'affaire des modules de relevé d'épreuve.

Usage :
    python3 appareil/texte_livre.py <epreuve.pdf> <sortie.json>
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

# Pied de composition : nom du document InDesign, folio, horodatage.
PIED = re.compile(r"^\S+\.indd\s+(\d+)\s+\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2}\s*$")
# Folio de tête : une ligne qui ne porte qu'un nombre.
FOLIO = re.compile(r"^(\d{1,3})$")
# Un mot coupé en fin de ligne : au moins une lettre, puis le trait d'union.
COUPE = re.compile(r"(\w[\w’']*)-$", re.UNICODE)
# Le premier mot de la ligne suivante.
SUITE = re.compile(r"^(\w[\w’']*)", re.UNICODE)


def pdftotext(pdf: Path) -> str:
    """Rend le texte de l'épreuve, mise en page conservée."""
    sortie = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        capture_output=True,
        check=True,
    )
    return sortie.stdout.decode("utf-8")


def empreinte(chemin: Path) -> str:
    h = hashlib.sha256()
    with chemin.open("rb") as f:
        for bloc in iter(lambda: f.read(1 << 16), b""):
            h.update(bloc)
    return h.hexdigest()


def decouper(brut: str) -> list[dict]:
    """Découpe le texte en pages, retire le pied et le folio, garde le reste."""
    pages = []
    for rang, page in enumerate(brut.split("\f"), start=1):
        if rang == 1 and not page.strip():
            continue
        lignes = page.split("\n")
        folio_pied = None
        gardees = []
        for ligne in lignes:
            m = PIED.match(ligne.strip())
            if m:
                folio_pied = int(m.group(1))
                continue
            gardees.append(ligne.rstrip())

        # Le folio de tête est la première ligne non vide, si elle n'est qu'un
        # nombre ET si ce nombre est celui du pied, qui fait autorité. Une
        # ouverture de chapitre porte son numéro de chapitre au même endroit.
        folio_tete = None
        for i, ligne in enumerate(gardees):
            if not ligne.strip():
                continue
            m = FOLIO.match(ligne.strip())
            if m and folio_pied is not None and int(m.group(1)) == folio_pied:
                folio_tete = int(m.group(1))
                gardees = gardees[:i] + gardees[i + 1 :]
            break

        # On ne garde que les lignes porteuses, sans les blancs de tête et de pied.
        while gardees and not gardees[0].strip():
            gardees.pop(0)
        while gardees and not gardees[-1].strip():
            gardees.pop()

        pages.append(
            {
                "rang": rang,
                "folio": folio_tete if folio_tete is not None else folio_pied,
                "folio_tete": folio_tete,
                "folio_pied": folio_pied,
                "lignes": [l.strip() for l in gardees],
            }
        )
    if pages and pages[-1]["rang"] > 1 and not pages[-1]["lignes"]:
        # `pdftotext` referme sur un saut de page vide.
        if pages[-1]["folio"] is None:
            pages.pop()
    return pages


def _nu(mot: str) -> str:
    """Forme comparable d'un mot : sans accents, sans casse, apostrophe unifiée."""
    mot = mot.replace("’", "'")
    mot = unicodedata.normalize("NFD", mot)
    return "".join(c for c in mot if unicodedata.category(c) != "Mn").lower()


def relever_coupes(pages: list[dict]) -> list[dict]:
    """Relève chaque mot coupé en fin de ligne et tranche son trait d'union.

    Un composé qui se retrouve entier ailleurs dans le livre garde son trait
    d'union ; les autres coupes sont des césures de composition.
    """
    # Vocabulaire des composés écrits d'un seul tenant, hors fin de ligne.
    entiers = set()
    gauches = set()
    compose = re.compile(r"\w[\w’']*-\w[\w’']*", re.UNICODE)
    for page in pages:
        for ligne in page["lignes"]:
            for m in compose.finditer(ligne):
                if m.end() == len(ligne):  # c'est peut-être une coupe : on ignore
                    continue
                entiers.add(_nu(m.group(0)))
                gauches.add(_nu(m.group(0).split("-", 1)[0]))

    coupes = []
    for page in pages:
        lignes = page["lignes"]
        for i, ligne in enumerate(lignes[:-1]):
            m = COUPE.search(ligne)
            if not m:
                continue
            s = SUITE.match(lignes[i + 1].lstrip())
            if not s:
                continue
            gauche, droite = m.group(1), s.group(1)
            avec = f"{gauche}-{droite}"
            if _nu(avec) in entiers:
                verdict = "trait d’union du mot"
                motif = "le composé se retrouve entier ailleurs dans le livre"
            elif gauche[:1].isupper() and droite[:1].isupper() and _nu(gauche) in gauches:
                verdict = "trait d’union du mot"
                motif = "composé à deux éléments capitalisés, dont l’élément de gauche s’écrit entier"
            else:
                verdict = "césure"
                motif = "aucun emploi entier du composé ni de son élément de gauche"
            coupes.append(
                {
                    "folio": page["folio"],
                    "rang": page["rang"],
                    "ligne": i,
                    "gauche": gauche,
                    "droite": droite,
                    "recolle": avec if verdict == "trait d’union du mot" else gauche + droite,
                    "verdict": verdict,
                    "motif": motif,
                }
            )
    return coupes


def couler(page: dict, coupes: list[dict]) -> str:
    """Rend le texte coulant d'une page, coupes recollées par leur verdict.

    Dérivé : ne se verse pas, se rejoue.
    """
    par_ligne = {c["ligne"]: c for c in coupes if c["rang"] == page["rang"]}
    morceaux = []
    for i, ligne in enumerate(page["lignes"]):
        c = par_ligne.get(i)
        if c is not None:
            garde = c["verdict"] == "trait d’union du mot"
            morceaux.append(ligne if garde else ligne[:-1])
            morceaux.append("")  # pas d'espace : le mot se referme sur la suite
        else:
            morceaux.append(ligne)
            morceaux.append(" ")
    return "".join(morceaux).strip()


def rendre(pdf: Path) -> dict:
    brut = pdftotext(pdf)
    pages = decouper(brut)
    coupes = relever_coupes(pages)
    for page in pages:
        page.pop("folio_tete", None)
        page.pop("folio_pied", None)
    return {
        "_source": {
            "epreuve": pdf.name,
            "sha256": empreinte(pdf),
            "octets": pdf.stat().st_size,
            "pages": len(pages),
            "extracteur": "pdftotext -layout",
        },
        "_regles": [
            "pied de composition retiré",
            "folio de tête retiré et porté au champ folio",
            "aucune césure recollée dans le versé — voir coupes",
        ],
        "coupes": coupes,
        "pages": pages,
    }


def controler(doc: dict) -> list[tuple[str, str, bool]]:
    """Contrôles mécaniques du rendu. Rend (code, libellé, passé)."""
    pages = doc["pages"]
    v = []
    v.append(("T1", f"{len(pages)} pages extraites — 180 attendues", len(pages) == 180))

    discord = [
        p["rang"] for p in pages if p["folio"] is not None and p["rang"] != p["folio"]
    ]
    v.append(
        ("T2", f"{len(discord)} page(s) dont le folio diffère du rang", not discord)
    )

    reste = [p["rang"] for p in pages for l in p["lignes"] if PIED.match(l)]
    v.append(("T3", f"{len(reste)} pied(s) de composition non retiré(s)", not reste))

    vides = [p["rang"] for p in pages if not p["lignes"]]
    v.append(("T4", f"{len(vides)} page(s) sans aucune ligne", True))  # déclaratif

    # T5 — les verbatim que le relevé du 20260910 publie doivent se retrouver.
    coupes = doc["coupes"]
    index = {p["rang"]: couler(p, coupes) for p in pages}
    attendus = [
        (105, "socle contributif par répartition égale à 1 100 euros par mois"),
        (142, "la moitié des 236 milliards d’euros par an d’économie sera déjà réalisée"),
        (88, "un total de 600 euros par mois pour un salarié type"),
        (40, "sous-directeur"),
        (147, "Cross-Sectional"),
    ]
    manques = [f"p. {p}" for p, texte in attendus if texte not in index.get(p, "")]
    v.append(
        (
            "T5",
            f"{len(manques)} verbatim du relevé EP3 introuvable(s)"
            + (f" — {', '.join(manques)}" if manques else ""),
            not manques,
        )
    )
    return v


def controler_perte(doc: dict, brut: str) -> tuple[str, str, bool]:
    """T6 — aucune ligne du livre n'est perdue à l'extraction.

    Les lignes non vides rendues par `pdftotext`, moins les pieds de
    composition et les folios de tête retirés, doivent se retrouver une à une
    dans le versé. Ce contrôle est externe au découpage : il recompte la
    source, il ne relit pas la sortie.
    """
    from collections import Counter

    source = Counter()
    for page in brut.split("\f"):
        for ligne in page.split("\n"):
            l = ligne.strip()
            if l and not PIED.match(l):
                source[l] += 1
    rendu = Counter(l for p in doc["pages"] for l in p["lignes"] if l.strip())
    retires = source - rendu
    # Les folios de tête retirés sont les seules disparitions admises.
    faux = {l: n for l, n in retires.items() if not FOLIO.match(l)}
    return (
        "T6",
        f"{sum(faux.values())} ligne(s) du livre perdue(s) à l’extraction"
        + (f" — {list(faux)[:5]}" if faux else "")
        + f" ; {sum(retires.values())} folio(s) de tête retiré(s)",
        not faux,
    )


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    pdf, sortie = Path(argv[1]), Path(argv[2])
    doc = rendre(pdf)
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(
        json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )

    echecs = 0
    print(f"{sortie} — {sortie.stat().st_size} o, {len(doc['pages'])} pages")
    print(f"  {len(doc['coupes'])} coupe(s) de fin de ligne relevée(s)")
    gardes = [c for c in doc["coupes"] if c["verdict"] == "trait d’union du mot"]
    print(f"  dont {len(gardes)} trait(s) d’union du mot, {len(doc['coupes']) - len(gardes)} césure(s)")
    verdicts = controler(doc) + [controler_perte(doc, pdftotext(pdf))]
    for code, libelle, passe in verdicts:
        print(f"  {code} {'ok ' if passe else 'ÉCHEC'} {libelle}")
        if not passe:
            echecs += 1
    return 1 if echecs else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
