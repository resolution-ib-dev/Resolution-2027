#!/usr/bin/env python3
"""Télécharge la nomenclature NATINF depuis data.gouv.fr.

Ne tourne PAS dans l'atelier, où data.gouv.fr est injoignable : il tourne dans
l'action du dépôt, en deux temps.

  python3 natinf.py              avant l'extraction LEGI : découvre la
                                 ressource CSV du jeu par l'API, la télécharge
                                 et écrit data/natinf.csv.gz. Un échec coûte
                                 quelques secondes, pas l'extraction.
  python3 natinf.py --manifeste  après l'extraction, qui réécrit le manifeste :
                                 y porte la provenance et les empreintes.

Même prudence que extraire_legi.py : l'adresse du fichier n'est pas présumée,
elle se lit sur la fiche du jeu. Pas de CSV, ou plusieurs sans ordre possible :
diagnostic, et échec.
"""
import gzip
import hashlib
import json
import pathlib
import sys
import urllib.request

RACINE = pathlib.Path(__file__).parent
DATA = RACINE / "data"
SORTIE = DATA / "natinf.csv.gz"
PROVENANCE = DATA / "_natinf.json"   # passe d'un temps à l'autre, puis s'efface

JEU = "62c7daa168ebd3a2212821c5"
API = f"https://www.data.gouv.fr/api/1/datasets/{JEU}/"
AGENT = {"User-Agent": "Mozilla/5.0 (compatible; resolution-droit/2.0)"}


def recuperer(url, timeout=300):
    req = urllib.request.Request(url, headers=AGENT)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def echec(charge, message):
    DATA.mkdir(exist_ok=True)
    (DATA / "_diagnostic.json").write_text(
        json.dumps(charge, ensure_ascii=False, indent=2), encoding="utf-8")
    sys.exit(f"ÉCHEC — {message}. Voir data/_diagnostic.json.")


def telecharger():
    try:
        fiche = json.loads(recuperer(API, timeout=120))
    except Exception as e:
        echec({"motif": "fiche NATINF illisible", "api": API, "erreur": repr(e)},
              f"fiche NATINF illisible : {e!r}")
    ressources = fiche.get("resources") or []
    csv = [r for r in ressources if (r.get("format") or "").lower() == "csv"]
    if not csv:
        echec({"motif": "aucune ressource CSV sur la fiche NATINF", "api": API,
               "ressources": [{k: r.get(k) for k in ("id", "title", "format", "url")}
                              for r in ressources]},
              "aucune ressource CSV sur la fiche NATINF")
    csv.sort(key=lambda r: r.get("last_modified") or "")
    r = csv[-1]
    try:
        brut = recuperer(r["url"])
    except Exception as e:
        echec({"motif": "CSV NATINF illisible", "url": r["url"], "erreur": repr(e)},
              f"CSV NATINF illisible : {e!r}")
    if not brut.strip():
        echec({"motif": "CSV NATINF vide", "url": r["url"]}, "CSV NATINF vide")

    # La fiche publie parfois sa propre empreinte : si elle est là, elle doit tenir.
    somme = r.get("checksum") or {}
    algo, attendu = (somme.get("type") or "").lower(), somme.get("value")
    if attendu and algo in hashlib.algorithms_available:
        lu = hashlib.new(algo, brut).hexdigest()
        if lu != attendu:
            echec({"motif": "empreinte de la fiche non tenue", "url": r["url"],
                   "algo": algo, "attendu": attendu, "lu": lu},
                  "empreinte NATINF non tenue")

    DATA.mkdir(exist_ok=True)
    # mtime à zéro : à contenu égal, le .gz est identique à l'octet d'un run à l'autre.
    with open(SORTIE, "wb") as f, gzip.GzipFile(fileobj=f, mode="wb", mtime=0,
                                                 compresslevel=9) as g:
        g.write(brut)
    info = {"jeu": JEU, "ressource": r.get("id"), "titre": r.get("title"),
            "url": r["url"], "derniere_modification": r.get("last_modified"),
            "lignes": brut.count(b"\n"), "octets_csv": len(brut),
            "sha256_csv": hashlib.sha256(brut).hexdigest(),
            "fichier": SORTIE.name, "octets": SORTIE.stat().st_size,
            "sha256": hashlib.sha256(SORTIE.read_bytes()).hexdigest()}
    PROVENANCE.write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"NATINF : {info['lignes']} lignes, ressource {info['ressource']}, "
          f"modifiée le {info['derniere_modification']}, sha256 {info['sha256']}")


def au_manifeste():
    p = DATA / "_manifeste.json"
    if not PROVENANCE.exists() or not SORTIE.exists() or not p.exists():
        echec({"motif": "NATINF ou manifeste absent au moment de l'inscription"},
              "NATINF non inscrit au manifeste")
    info = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    if hashlib.sha256(SORTIE.read_bytes()).hexdigest() != info["sha256"]:
        echec({"motif": "data/natinf.csv.gz a changé entre le téléchargement et l'inscription"},
              "NATINF modifié en cours de run")
    m = json.loads(p.read_text(encoding="utf-8"))
    m["natinf"] = info
    p.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")
    PROVENANCE.unlink()
    print(f"NATINF inscrit au manifeste : sha256 {info['sha256']}")


if __name__ == "__main__":
    au_manifeste() if "--manifeste" in sys.argv[1:] else telecharger()
