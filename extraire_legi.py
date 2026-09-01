#!/usr/bin/env python3
"""Extrait, de la base LEGI de la DILA, les seuls codes dont le chantier a besoin.

Ne tourne PAS dans l'atelier : il tourne dans l'action programmée du dépôt.
L'atelier ne lit que ce que ce script a écrit — `droit.py` s'en charge.

Principe de prudence : le script ne présume ni de l'adresse du dépôt de la
DILA, ni de la disposition interne de l'archive. Il DÉCOUVRE l'une par l'API
de data.gouv.fr et l'autre en balayant l'archive. Quand un code ne rend aucun
article, il ne devine pas : il écrit un diagnostic et il échoue.

Sortie, un fichier par code : data/<court>.jsonl.gz, une ligne par article.
  {id, num, code, etat, date_debut, date_fin, section, texte}
Plus data/_manifeste.json : millésime du dump, comptes, empreintes.
"""
import gzip
import hashlib
import io
import json
import os
import pathlib
import re
import sys
import tarfile
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict

RACINE = pathlib.Path(__file__).parent
DATA = RACINE / "data"
DATA.mkdir(exist_ok=True)

# Le jeu de données LEGI sur data.gouv.fr. On passe par l'API du portail plutôt
# que par une adresse de fichier en dur : les noms d'archives portent un
# horodatage et changent à chaque publication.
DATASET = "legi-codes-lois-et-reglements-consolides"
API = f"https://www.data.gouv.fr/api/1/datasets/{DATASET}/"

AGENT = {"User-Agent": "resolution-droit/1.0 (+chantier Resolution)"}


def journal(*a):
    print(*a, flush=True)


# --------------------------------------------------------------------------
# 1. Trouver l'archive


def resoudre_archive():
    """Rend (url, titre) de l'archive LEGI complète la plus récente."""
    req = urllib.request.Request(API, headers=AGENT)
    with urllib.request.urlopen(req, timeout=120) as r:
        meta = json.load(r)

    ressources = meta.get("resources", [])
    journal(f"jeu de données : {meta.get('title')} — {len(ressources)} ressource(s)")

    def horodatage(r):
        m = re.search(r"(20\d{6})", (r.get("title") or "") + " " + (r.get("url") or ""))
        return m.group(1) if m else ""

    # On veut un dump COMPLET (« Freemium_legi_global » ou titre portant
    # « global »), jamais un incrémental journalier.
    complets = [
        r for r in ressources
        if re.search(r"\.tar\.gz$|\.tgz$", r.get("url", ""), re.I)
        and re.search(r"global|complet|full", (r.get("title", "") + r.get("url", "")), re.I)
    ]
    if not complets:
        complets = [r for r in ressources if re.search(r"\.tar\.gz$|\.tgz$", r.get("url", ""), re.I)]

    if not complets:
        diagnostic({"motif": "aucune archive tar.gz dans le jeu de données",
                    "ressources": [{"titre": r.get("title"), "url": r.get("url")} for r in ressources[:40]]})
        sys.exit("ÉCHEC — aucune archive exploitable. Voir data/_diagnostic.json.")

    complets.sort(key=horodatage, reverse=True)
    choisie = complets[0]
    journal(f"archive retenue : {choisie.get('title')} — {choisie.get('url')}")
    return choisie["url"], (horodatage(choisie) or "inconnu")


# --------------------------------------------------------------------------
# 2. Balayer l'archive en flux


def texte_de(el):
    """Texte d'un sous-arbre, balises inline aplaties, espaces normalisés."""
    if el is None:
        return ""
    brut = "".join(el.itertext())
    brut = brut.replace(" ", " ")
    lignes = [re.sub(r"[ \t]+", " ", l).strip() for l in brut.splitlines()]
    return "\n".join(l for l in lignes if l).strip()


def premier(el, *noms):
    """Premier descendant portant l'un de ces noms de balise, insensible au cas."""
    cibles = {n.upper() for n in noms}
    for sous in el.iter():
        if sous.tag.upper().split("}")[-1] in cibles:
            return sous
    return None


def lire_article(donnees):
    """Rend le dict d'un article, ou None si le XML n'en porte pas."""
    try:
        racine = ET.fromstring(donnees)
    except ET.ParseError:
        return None
    art = racine if racine.tag.upper().endswith("ARTICLE") else premier(racine, "ARTICLE")
    if art is None:
        return None

    def champ(*noms):
        el = premier(art, *noms)
        return (el.text or "").strip() if el is not None and el.text else ""

    ident = champ("ID")
    if not ident.startswith("LEGIARTI"):
        return None
    contenu = premier(art, "BLOC_TEXTUEL")
    texte = texte_de(premier(contenu, "CONTENU") if contenu is not None else None)
    if not texte:
        texte = texte_de(premier(art, "CONTENU"))
    return {
        "id": ident,
        "num": champ("NUM"),
        "etat": champ("ETAT") or "INCONNU",
        "date_debut": champ("DATE_DEBUT"),
        "date_fin": champ("DATE_FIN"),
        "texte": texte,
    }


def lire_structure(donnees):
    """Rend {LEGIARTI: 'Titre > Chapitre > Section'} depuis un fichier de structure."""
    try:
        racine = ET.fromstring(donnees)
    except ET.ParseError:
        return {}
    chemins = {}

    def descendre(el, pile):
        nom = el.tag.upper().split("}")[-1]
        if nom in ("SECTION_TA", "TM", "LIEN_SECTION_TA"):
            titre = el.get("titre") or ""
            if not titre:
                t = premier(el, "TITRE_TA", "TITRE_TM")
                titre = texte_de(t)
            if titre:
                pile = pile + [titre.strip()]
        if nom == "LIEN_ART":
            ident = el.get("id") or ""
            if ident.startswith("LEGIARTI"):
                chemins[ident] = " > ".join(pile)
        for sous in list(el):
            descendre(sous, pile)

    descendre(racine, [])
    return chemins


def balayer(url, cibles):
    """cibles : {LEGITEXT: court}. Rend articles et sections par code."""
    articles = defaultdict(dict)   # court -> {id: dict}
    sections = defaultdict(dict)   # court -> {id: chemin}
    echantillon = []
    vus = 0

    req = urllib.request.Request(url, headers=AGENT)
    with urllib.request.urlopen(req, timeout=1800) as flux:
        with tarfile.open(fileobj=flux, mode="r|gz") as tar:
            for membre in tar:
                if not membre.isfile() or not membre.name.endswith(".xml"):
                    continue
                vus += 1
                if vus % 200000 == 0:
                    journal(f"  {vus} fichiers balayés…")
                if len(echantillon) < 25 and "LEGITEXT" in membre.name:
                    echantillon.append(membre.name)

                court = None
                for legitext, c in cibles.items():
                    if legitext in membre.name:
                        court = c
                        break
                if court is None:
                    continue

                f = tar.extractfile(membre)
                if f is None:
                    continue
                donnees = f.read()

                if b"<LIEN_ART" in donnees or b"<STRUCT" in donnees:
                    sections[court].update(lire_structure(donnees))
                if b"<ARTICLE" in donnees:
                    a = lire_article(donnees)
                    if a:
                        articles[court][a["id"]] = a

    journal(f"balayage terminé : {vus} fichiers XML")
    return articles, sections, echantillon


# --------------------------------------------------------------------------
# 3. Écrire


def diagnostic(charge):
    (DATA / "_diagnostic.json").write_text(
        json.dumps(charge, ensure_ascii=False, indent=2), encoding="utf-8")


def ecrire(court, cle, arts, sect):
    chemin = DATA / f"{court}.jsonl.gz"
    h = hashlib.sha256()
    n = 0
    with gzip.open(chemin, "wt", encoding="utf-8", compresslevel=9) as sortie:
        for ident in sorted(arts):
            a = dict(arts[ident])
            a["code"] = cle
            a["section"] = sect.get(ident, "")
            ligne = json.dumps(a, ensure_ascii=False, sort_keys=True)
            sortie.write(ligne + "\n")
            h.update(ligne.encode())
            n += 1
    return {"fichier": chemin.name, "articles": n,
            "octets": chemin.stat().st_size, "sha256": h.hexdigest()}


def main():
    cfg = json.loads((RACINE / "codes.json").read_text(encoding="utf-8"))
    cibles = {c["legitext"]: c["court"] for c in cfg["codes"]}
    libelles = {c["court"]: c["cle"] for c in cfg["codes"]}

    url, millesime = resoudre_archive()
    articles, sections, echantillon = balayer(url, cibles)

    vides = [libelles[c] for c in libelles if not articles.get(c)]
    if vides:
        diagnostic({
            "motif": "codes sans aucun article extrait",
            "codes_vides": vides,
            "archive": url,
            "echantillon_de_chemins": echantillon,
            "comptes": {libelles[c]: len(articles.get(c, {})) for c in libelles},
        })
        sys.exit("ÉCHEC — " + ", ".join(vides) + ". Voir data/_diagnostic.json.")

    manifeste = {"millesime_legi": millesime, "archive": url,
                 "extrait_le": os.environ.get("DATE_EXTRACTION", ""), "codes": {}}
    for court, cle in libelles.items():
        en_vigueur = {i: a for i, a in articles[court].items() if a["etat"].upper() == "VIGUEUR"}
        manifeste["codes"][cle] = ecrire(court, cle, en_vigueur, sections.get(court, {}))
        manifeste["codes"][cle]["court"] = court
        manifeste["codes"][cle]["sections_rattachees"] = sum(
            1 for i in en_vigueur if sections.get(court, {}).get(i))
        journal(f"  {cle} : {manifeste['codes'][cle]['articles']} articles en vigueur")

    (DATA / "_manifeste.json").write_text(
        json.dumps(manifeste, ensure_ascii=False, indent=2), encoding="utf-8")
    if (DATA / "_diagnostic.json").exists():
        (DATA / "_diagnostic.json").unlink()
    journal("manifeste écrit.")


if __name__ == "__main__":
    main()
