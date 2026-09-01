#!/usr/bin/env python3
"""Épreuve à blanc : monte un extrait factice, puis exerce le lecteur.

Ne remplace pas un vrai rafraîchissement. Prouve deux choses seulement :
que le parseur d'articles et de structure lit la forme LEGI documentée, et
que le lecteur refuse ce qu'il doit refuser.
"""
import gzip, json, pathlib, shutil, subprocess, sys

RACINE = pathlib.Path(__file__).parent
DATA = RACINE / "data"
SAUVE = RACINE / "_data_reelle"

ARTICLE_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<ARTICLE>
  <META><META_COMMUN><ID>LEGIARTI000006308922</ID><NATURE>Article</NATURE></META_COMMUN>
    <META_SPEC><META_ARTICLE><NUM>235 bis</NUM><ETAT>VIGUEUR</ETAT>
      <DATE_DEBUT>2019-05-24</DATE_DEBUT><DATE_FIN>2999-01-01</DATE_FIN>
    </META_ARTICLE></META_SPEC></META>
  <BLOC_TEXTUEL><CONTENU><p>Les employeurs assujettis acquittent une cotisation.</p>
  <p>Un decret fixe les modalites.</p></CONTENU></BLOC_TEXTUEL>
</ARTICLE>"""

STRUCT_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<TEXTELR><STRUCT>
  <LIEN_SECTION_TA id="LEGISCTA000006179826" titre="Section VII : Cotisation">
    <LIEN_ART id="LEGIARTI000006308922" num="235 bis"/>
  </LIEN_SECTION_TA>
</STRUCT></TEXTELR>"""


def fixture():
    sys.path.insert(0, str(RACINE))
    import extraire_legi as X
    a = X.lire_article(ARTICLE_XML)
    assert a and a["id"] == "LEGIARTI000006308922", a
    assert a["num"] == "235 bis" and a["etat"] == "VIGUEUR", a
    assert "cotisation" in a["texte"] and "decret" in a["texte"], a["texte"]
    s = X.lire_structure(STRUCT_XML)
    assert s.get("LEGIARTI000006308922", "").endswith("Cotisation"), s
    print("parseur LEGI : article et structure lus.")

    lignes = [
        dict(a, code="code général des impôts", section=s["LEGIARTI000006308922"]),
        {"id": "LEGIARTI000000000002", "num": "279", "etat": "VIGUEUR",
         "date_debut": "2024-01-01", "date_fin": "2999-01-01",
         "texte": "La taxe est percue au taux reduit.", "code": "code général des impôts",
         "section": "B : Taux reduit"},
        {"id": "LEGIARTI000000000003", "num": "1er", "etat": "ABROGE",
         "date_debut": "2007-01-01", "date_fin": "2011-07-29",
         "texte": "Bouclier fiscal.", "code": "code général des impôts", "section": ""},
    ]
    DATA.mkdir(exist_ok=True)
    with gzip.open(DATA / "cgi.jsonl.gz", "wt", encoding="utf-8") as f:
        for l in lignes:
            f.write(json.dumps(l, ensure_ascii=False, sort_keys=True) + "\n")
    (DATA / "_manifeste.json").write_text(json.dumps({
        "millesime_legi": "20260830", "archive": "essai",
        "codes": {"code général des impôts": {"fichier": "cgi.jsonl.gz", "court": "cgi",
                  "articles": len(lignes), "octets": 0, "sha256": "",
                  "sections_rattachees": 2}}}, ensure_ascii=False, indent=2), encoding="utf-8")


def exercer():
    import droit as D
    D._cache.clear()

    a = D.article("cgi", "235 bis")
    assert a["id"] == "LEGIARTI000006308922"
    assert D.article("code général des impôts", "235bis")["id"] == a["id"], "normalisation"
    print("lecture par libellé exact et par nom court : ok, ponctuation normalisée.")

    rendu = D.rendre(a)
    assert "LEGIARTI000006308922" in rendu and "2019-05-24" in rendu and "20260830" in rendu
    assert "Section VII" in rendu
    print("gabarit de sortie : identifiant, date de version et millésime présents.")

    for appel, attendu in (
        (lambda: D.article("cgi", "279 bis"), LookupError),      # absent
        (lambda: D.article("cgi", "1er"), LookupError),          # abrogé
        (lambda: D.article("code des douanes", "1"), KeyError),  # code non porté
    ):
        try:
            appel()
        except attendu:
            pass
        else:
            sys.exit("ÉCHEC : un refus attendu n'a pas eu lieu.")
    print("refus : article absent, article abrogé, code non porté — les trois lèvent.")

    assert [x["num"] for x in D.chercher("cgi", "taux reduit")] == ["279"]
    print("recherche par titre de section : ok.")

    lignes = D.verifier({"cgi": ["235 bis", "1er", "9999"]})
    assert [l[2] for l in lignes] == ["trouvé", "abrogé", "absent"], lignes
    print("contrôle de lot : trouvé / abrogé / absent.")

    mil, age, perime = D.fraicheur(seuil_jours=1)
    assert perime, "un extrait de plus d'un jour doit se déclarer périmé"
    print("fraîcheur : un extrait vieilli se signale.")


if __name__ == "__main__":
    if DATA.exists() and (DATA / "_manifeste.json").exists() and not SAUVE.exists():
        shutil.move(str(DATA), str(SAUVE))
    try:
        fixture()
        exercer()
        print("\nÉPREUVE PASSÉE — 7 contrôles.")
        r = subprocess.run([sys.executable, str(RACINE / "droit.py"), "etat"],
                           capture_output=True, text=True)
        print("\n$ droit.py etat\n" + r.stdout.strip())
    finally:
        shutil.rmtree(DATA, ignore_errors=True)
        if SAUVE.exists():
            shutil.move(str(SAUVE), str(DATA))
        else:
            DATA.mkdir(exist_ok=True)
