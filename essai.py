#!/usr/bin/env python3
"""Épreuve à blanc : monte un extrait factice, puis exerce le lecteur.

Ne remplace pas un vrai rafraîchissement. Prouve deux choses seulement :
que le parseur d'articles et de structure lit la forme LEGI documentée, et
que le lecteur refuse ce qu'il doit refuser.
"""
import contextlib, gzip, io, json, pathlib, shutil, subprocess, sys, tarfile

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

TEXTE_META_XML = """<?xml version="1.0" encoding="UTF-8"?>
<TEXTE_VERSION>
  <META><META_COMMUN><ID>LEGITEXT000000000099</ID><NATURE>LOI</NATURE></META_COMMUN>
  <META_SPEC><META_TEXTE_VERSION>
    <TITRE>LOI n°2025-127 du 14 février 2025</TITRE>
    <TITREFULL>LOI n° 2025-127 du 14 février 2025 de finances pour 2025 (1)</TITREFULL>
  </META_TEXTE_VERSION></META_SPEC></META>
</TEXTE_VERSION>""".encode("utf-8")

CODE_META_XML = """<?xml version="1.0" encoding="UTF-8"?>
<TEXTE_VERSION>
  <META><META_COMMUN><ID>LEGITEXT000022197698</ID><NATURE>CODE</NATURE></META_COMMUN>
  <META_SPEC><META_TEXTE_VERSION>
    <TITRE>Code rural et de la pêche maritime</TITRE>
    <TITREFULL>Code rural et de la pêche maritime</TITREFULL>
  </META_TEXTE_VERSION></META_SPEC></META>
</TEXTE_VERSION>""".encode("utf-8")


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

    # classement des archives de l'index DILA, sans réseau
    INDEX = b"""<html><body>
      <a href="DILA_LEGI_Presentation.pdf">doc</a>
      <a href="Freemium_legi_global_20260615-103000.tar.gz">complete</a>
      <a href="Freemium_legi_global_20251201-090000.tar.gz">vieille complete</a>
      <a href="LEGI_20260828-035000.tar.gz">j1</a>
      <a href="LEGI_20260831-035000.tar.gz">j2</a>
      <a href="LEGI_20260101-035000.tar.gz">avant la complete</a>
    </body></html>"""
    X.recuperer = lambda url, timeout=300: INDEX
    urls, millesime = X.resoudre_archives()
    noms = [u.split("/")[-1] for u in urls]
    assert noms == ["Freemium_legi_global_20260615-103000.tar.gz",
                    "LEGI_20260828-035000.tar.gz",
                    "LEGI_20260831-035000.tar.gz"], noms
    assert millesime == "20260831", millesime
    print("index DILA : complète la plus récente, journalières postérieures dans l'ordre.")

    plancher = "2025-01-01"
    assert X.dans_l_historique({"date_fin": "2026-03-01"}, plancher), "à garder"
    assert not X.dans_l_historique({"date_fin": "2011-07-29"}, plancher), "à jeter"
    assert not X.dans_l_historique({"date_fin": "2999-01-01"}, plancher), "fin ouverte, à ignorer"
    print("dans_l_historique : garde une fin récente, jette une fin ancienne, "
          "ignore la fin ouverte.")

    lignes = [
        dict(a, code="code général des impôts", section=s["LEGIARTI000006308922"]),
        {"id": "LEGIARTI000000000002", "num": "279", "etat": "VIGUEUR",
         "date_debut": "2024-01-01", "date_fin": "2026-03-01",
         "texte": "La taxe est percue au taux reduit.", "code": "code général des impôts",
         "section": "B : Taux reduit"},
        {"id": "LEGIARTI000000000003", "num": "1er", "etat": "ABROGE",
         "date_debut": "2007-01-01", "date_fin": "2011-07-29",
         "texte": "Bouclier fiscal.", "code": "code général des impôts", "section": ""},
        # Le cas réel qui a fait échouer deux extraits : applicable aujourd'hui,
        # abrogation déjà votée. L'état dit ABROGE_DIFF, les dates disent oui.
        {"id": "LEGIARTI000053562872", "num": "279", "etat": "ABROGE_DIFF",
         "date_debut": "2026-03-01", "date_fin": "2027-01-01",
         "texte": "La taxe est perçue au taux réduit.",
         "code": "code général des impôts", "section": "B : Taux réduit"},
        # Version future : ne doit jamais sortir comme droit applicable.
        {"id": "LEGIARTI000099999999", "num": "1000", "etat": "VIGUEUR_DIFF",
         "date_debut": "2027-06-01", "date_fin": "2999-01-01",
         "texte": "Texte à venir.", "code": "code général des impôts", "section": ""},
    ]
    DATA.mkdir(exist_ok=True)
    with gzip.open(DATA / "cgi.jsonl.gz", "wt", encoding="utf-8") as f:
        for l in lignes:
            f.write(json.dumps(l, ensure_ascii=False, sort_keys=True) + "\n")
    (DATA / "_manifeste.json").write_text(json.dumps({
        "millesime_legi": "20260830", "archive": "essai",
        "codes": {"code général des impôts": {"fichier": "cgi.jsonl.gz", "court": "cgi",
                  "articles": len(lignes), "octets": 0, "sha256": "",
                  "applicables": 3, "fin_programmee": 1, "a_venir": 1,
                  "sections_rattachees": 2}}}, ensure_ascii=False, indent=2), encoding="utf-8")


def intitules():
    """Trois contrôles, sans réseau : un intitulé qui résout vers un texte non
    codifié (dossier JORFTEXT, fichier LEGITEXT), un vers un code (dossier ET
    fichier LEGITEXT, mais deux identifiants différents — le run #13 a montré
    qu'ils divergent bel et bien : `code rural et de la pêche maritime`
    rendait 0 article tant qu'on retenait celui du fichier), et un intitulé
    introuvable qui fait échouer l'extraction en se nommant.
    `_archive_en_flux` est le seul point de réseau de la résolution par
    intitulé — le remplacer suffit à l'éprouver hors ligne."""
    import extraire_legi as X

    @contextlib.contextmanager
    def flux_avec(membres):
        tampon = io.BytesIO()
        with tarfile.open(fileobj=tampon, mode="w") as tar:
            for nom, contenu in membres:
                info = tarfile.TarInfo(nom)
                info.size = len(contenu)
                tar.addfile(info, io.BytesIO(contenu))
        tampon.seek(0)
        with tarfile.open(fileobj=tampon, mode="r") as tar:
            yield tar

    membre_loi = ("legi/global/.../JORFTEXT000000546652/texte/version/LEGITEXT000000000099.xml",
                  TEXTE_META_XML)

    X._archive_en_flux = lambda url, timeout=3600: flux_avec([membre_loi])
    cibles = X.resoudre_ou_echouer(
        ["fake://archive"],
        [{"cle": "loi n° 2025-127 du 14 février 2025", "court": "loi2025_127"}])
    assert cibles == {"JORFTEXT000000546652": "loi2025_127"}, cibles
    print("intitulé résolu (texte non codifié) : « loi n° 2025-127 du 14 février 2025 » -> "
          "JORFTEXT000000546652 (l'identifiant du dossier, pas celui du fichier lu).")

    membre_code = ("legi/.../LEGITEXT000006071367/texte/struct/LEGITEXT000022197698.xml",
                   CODE_META_XML)
    X._archive_en_flux = lambda url, timeout=3600: flux_avec([membre_code])
    cibles = X.resoudre_ou_echouer(
        ["fake://archive"],
        [{"cle": "code rural et de la pêche maritime", "court": "rural"}])
    assert cibles == {"LEGITEXT000006071367": "rural"}, cibles
    print("intitulé résolu (code) : « code rural et de la pêche maritime » -> "
          "LEGITEXT000006071367, pas LEGITEXT000022197698 (l'identifiant du fichier de "
          "métadonnées lui-même, une version datée distincte du code).")

    X._archive_en_flux = lambda url, timeout=3600: flux_avec([membre_loi])
    try:
        X.resoudre_ou_echouer(
            ["fake://archive"],
            [{"cle": "loi n° 0000-000 du 1er janvier 2000", "court": "inconnue"}])
    except SystemExit as e:
        assert "loi n° 0000-000 du 1er janvier 2000" in str(e), str(e)
        print("intitulé introuvable : l'extraction échoue en le nommant.")
    else:
        sys.exit("ÉCHEC : un intitulé introuvable aurait dû faire échouer l'extraction.")


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

    a279 = D.article("cgi", "279")
    assert a279["id"] == "LEGIARTI000053562872", a279
    r = D.rendre(a279)
    assert "AVERTISSEMENT" in r and "2027-01-01" in r, r
    print("ABROGE_DIFF : applicable aujourd'hui, et l'avertissement d'abrogation sort.")

    a279_passe = D.article("cgi", "279", jour="2025-06-01")
    assert a279_passe["id"] == "LEGIARTI000000000002", a279_passe
    print("lecture au jour= : l'article 279 du 2025-06-01 rend la version d'alors, "
          "pas la version courante.")

    try:
        D.article("cgi", "1000")
    except LookupError as e:
        assert "2027-06-01" in str(e), str(e)
        print("version future : refusée, avec la date d'entrée en vigueur.")
    else:
        sys.exit("ÉCHEC : une version future est sortie comme droit applicable")

    for appel, attendu in (
        (lambda: D.article("cgi", "279 bis"), LookupError),      # absent
        (lambda: D.article("cgi", "1er"), LookupError),          # abrogé
        (lambda: D.article("code de la route", "1"), KeyError),   # code non porté
    ):
        try:
            appel()
        except attendu:
            pass
        else:
            sys.exit("ÉCHEC : un refus attendu n'a pas eu lieu.")
    print("refus : article absent, article abrogé, code non porté — les trois lèvent.")

    trouves = D.chercher("cgi", "taux")
    assert [x["id"] for x in trouves] == ["LEGIARTI000053562872"], trouves
    print("recherche par section : une seule version rendue, l'applicable.")

    lignes = D.verifier({"cgi": ["235 bis", "1er", "9999"]})
    assert [l[2] for l in lignes] == ["trouvé", "inapplicable", "absent"], lignes
    print("contrôle de lot : trouvé / inapplicable / absent.")

    mil, age, perime = D.fraicheur(seuil_jours=1)
    assert perime, "un extrait de plus d'un jour doit se déclarer périmé"
    print("fraîcheur : un extrait vieilli se signale.")


if __name__ == "__main__":
    if DATA.exists() and (DATA / "_manifeste.json").exists() and not SAUVE.exists():
        shutil.move(str(DATA), str(SAUVE))
    try:
        fixture()
        intitules()
        exercer()
        print("\nÉPREUVE PASSÉE — 15 contrôles.")
        r = subprocess.run([sys.executable, str(RACINE / "droit.py"), "etat"],
                           capture_output=True, text=True)
        print("\n$ droit.py etat\n" + r.stdout.strip())
    finally:
        shutil.rmtree(DATA, ignore_errors=True)
        if SAUVE.exists():
            shutil.move(str(SAUVE), str(DATA))
        else:
            DATA.mkdir(exist_ok=True)
