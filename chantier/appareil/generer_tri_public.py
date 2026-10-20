#!/usr/bin/env python3
"""Le classeur public du tri des prélèvements.

Inscrit le 20261020. Écrit, depuis le tri qui fait foi, le classeur destiné à la
page « Données » du site, sans rien de la nomenclature interne : ni fondement
numéroté, ni statut de relevé, ni chemin de fichier.

  entrée  referentiels/sort_prelevements_20261015.tsv   le sort, rang par rang
          referentiels/prelevements_forces_20260930.tsv  affectataires, code du siège
  sortie  livrables/tri_public/Tri des prélèvements Résolution.xlsx
          livrables/tri_public/a_confirmer.md            ce que l'auteur tranche avant
                                                        mise en ligne

Le classeur porte des formules (synthèses) : il se recalcule par LibreOffice
quand `soffice` est présent, pour que les valeurs s'affichent à l'ouverture.
"""
import csv
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
REF = RACINE / "referentiels"
SORTIE = RACINE / "livrables/tri_public"
NOM = "Tri des prélèvements Résolution.xlsx"

SORTS = ["conservé et absorbe", "fondu par rattachement", "fondu dans l’équilibre", "maintenu à part", "hors champ"]
DEFINITIONS = [
    ("Conservé et absorbe", "L’un des quatre impôts que la refonte garde : taxe sur la valeur ajoutée, impôt sur "
     "le revenu, impôt sur les sociétés, taxe foncière. Il reprend le produit des prélèvements fondus en lui."),
    ("Fondu par rattachement", "Le prélèvement disparaît ; son produit est repris par l’impôt conservé qui porte "
     "la même assiette (colonne « Impôt qui le reprend »)."),
    ("Fondu dans l’équilibre", "Le prélèvement disparaît ; son produit est repris par les hausses d’équilibre des "
     "quatre impôts conservés, sans rattachement à l’un d’eux."),
    ("Maintenu à part", "Le prélèvement demeure, en complément de l’impôt qu’il prolonge (colonne « Impôt qui le "
     "reprend »)."),
    ("Hors champ", "Recette publique qui n’est pas un prélèvement obligatoire (produit d’enchères, recette "
     "non fiscale) : recensée, non triée."),
]
COLONNES = ["Prélèvement", "Nature", "Assiette", "Sous-catégorie", "Poste du schéma de refonte", "Sort",
            "Impôt qui le reprend", "Rendement 2026 (M€)", "Bénéficiaire", "Siège juridique"]


def tsv(nom):
    return list(csv.DictReader((REF / nom).open(encoding="utf-8"), delimiter="\t"))


def poste(ligne):
    p = ligne.replace("*", "").strip()
    if p in ("—", ""):
        return ""
    return (p[5:] if p.startswith("dont ") else p).capitalize()


def siege(r, f):
    art = r["siege_article"].strip()
    if not art:
        return ""
    code = (f or {}).get("siege_code", "").strip()
    if code and not art.lower().startswith(("art", "loi", "décret", "ordonnance")):
        art = re.sub(r"\b(LO|L|R|D|A)(\d)", r"\1. \2", art)
        art = f"{code}, art. {art}"
    return art[:1].upper() + art[1:]


def beneficiaire(f):
    if not f:
        return ""
    b = f.get("affectataires", "").strip()
    if not b and f.get("rendement_etat_2026_M", "").strip():
        b = "État (budget général)"
    return b


def lignes():
    forces = {r["libelle"]: r for r in tsv("prelevements_forces_20260930.tsv")}
    out = []
    for r in tsv("sort_prelevements_20261015.tsv"):
        f = forces.get(r["libelle"])
        rend = float(r["rendement_2026_M"]) if r["rendement_2026_M"] else None
        out.append([r["libelle"].strip(), r["nature"], r["assiette"], r["sous_categorie"], poste(r["ligne_schema"]),
                    r["sort"][:1].upper() + r["sort"][1:], r["impot_absorbant"] or r["complement_de"], rend,
                    beneficiaire(f), siege(r, f)])
    return out


def classeur(data):
    import openpyxl
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.worksheet.table import Table, TableStyleInfo
    gras, gris = Font(bold=True), PatternFill("solid", fgColor="EEEEEE")
    titre = Font(bold=True, size=14)
    wb = openpyxl.Workbook()

    lm = wb.active
    lm.title = "Lisez-moi"
    texte = [
        ("Le tri des prélèvements", titre),
        (f"{len(data)} prélèvements obligatoires recensés, un par un, et le sort que la refonte fiscale de "
         "Résolution réserve à chacun.", None),
        ("", None),
        ("Les cinq sorts", gras),
        *[(f"{a} — {b}", None) for a, b in DEFINITIONS],
        ("", None),
        ("Lire le tri", gras),
        ("Assiette : la matière taxée — les cotisations sociales, les contributions sociales sur les revenus, la "
         "masse salariale, le revenu des personnes, l’activité des entreprises, la consommation, la propriété.", None),
        ("Rendement 2026 : ce que l’État publie, prélèvement par prélèvement. Une case vide ne vaut pas zéro : "
         f"l’État ne publie pas le rendement de {sum(1 for l in data if l[7] is None)} prélèvements sur "
         f"{len(data)}, cotisations sociales et taxes affectées à des organismes pour l’essentiel.", None),
        ("Siège juridique : l’article de loi qui institue le prélèvement, au texte en vigueur.", None),
        ("", None),
        ("Sources", gras),
        ("Projet de loi de finances pour 2026 : état A et Évaluation des voies et moyens, tome I, annexe 2 (taxes "
         "affectées). Projet de loi de finances pour 2027 : annexe des ressources affectées. Fondation IFRAP, "
         "recensement des prélèvements obligatoires, La Revue n° 277, avril 2026. Codes et lois en vigueur, "
         "base LEGI de la DILA.", None),
        ("Calculs et tri : Résolution.", None),
    ]
    for i, (t, f) in enumerate(texte, 1):
        c = lm.cell(i, 1, t)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if f:
            c.font = f
    lm.column_dimensions["A"].width = 120

    ws = wb.create_sheet("Tri")
    ws.append(COLONNES)
    for l in data:
        ws.append(l)
    n = len(data) + 1
    for c in ws[1]:
        c.font, c.fill = gras, gris
        c.alignment = Alignment(wrap_text=True, vertical="bottom")
    for row in ws.iter_rows(min_row=2, min_col=8, max_col=8):
        row[0].number_format = "#,##0.0"
    for col, w in zip("ABCDEFGHIJ", (60, 22, 30, 34, 26, 22, 26, 14, 40, 30)):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = "B2"
    tab = Table(displayName="Tri", ref=f"A1:J{n}")
    tab.tableStyleInfo = TableStyleInfo(name="TableStyleLight1", showRowStripes=True)
    ws.add_table(tab)

    def synthese(nom, entete, cle_col, valeurs, note=None):
        s = wb.create_sheet(nom)
        s.append([entete, "Prélèvements", "Rendement 2026 publié (M€)", "Part du rendement publié"])
        for c in s[1]:
            c.font, c.fill = gras, gris
        for i, v in enumerate(valeurs, 2):
            s.append([v, f"=COUNTIF(Tri!${cle_col}$2:${cle_col}${n},A{i})",
                      f"=SUMIF(Tri!${cle_col}$2:${cle_col}${n},A{i},Tri!$H$2:$H${n})",
                      f"=IFERROR(C{i}/C${len(valeurs) + 2},0)"])
        t = len(valeurs) + 2
        s.append(["Total", f"=SUM(B2:B{t - 1})", f"=SUM(C2:C{t - 1})"])
        s.cell(t, 1).font = gras
        for r in range(2, t + 1):
            s.cell(r, 3).number_format = "#,##0.0"
            s.cell(r, 4).number_format = "0.0%"
        if note:
            s.cell(t + 2, 1, note)
        s.column_dimensions["A"].width = 46
        for col in "BCD":
            s.column_dimensions[col].width = 18

    synthese("Par sort", "Sort", "F", [x[:1].upper() + x[1:] for x in SORTS])
    synthese("Par assiette", "Assiette", "C", sorted({l[2] for l in data}))
    synthese("Par impôt qui reprend", "Impôt", "G",
             ["Taxe sur la valeur ajoutée", "Impôt sur le revenu", "Impôt sur les sociétés", "Taxe foncière"],
             "Prélèvements fondus par rattachement et maintenus en complément.")
    return wb


def recalculer(chemin):
    if not shutil.which("soffice"):
        return False
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx:Calc MS Excel 2007 XML",
                        "--outdir", d, str(chemin)], capture_output=True, timeout=300)
        sortie = Path(d) / chemin.name
        if sortie.exists():
            shutil.copy(sortie, chemin)
            return True
    return False


def main():
    data = lignes()
    SORTIE.mkdir(parents=True, exist_ok=True)
    chemin = SORTIE / NOM
    classeur(data).save(chemin)
    rec = recalculer(chemin)
    c = Counter(l[5] for l in data)
    print(f"{len(data)} rangs ; " + " ; ".join(f"{k} {v}" for k, v in c.most_common()))
    print(f"{chemin.relative_to(RACINE)} — {chemin.stat().st_size // 1024} Ko — recalculé : {rec}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
