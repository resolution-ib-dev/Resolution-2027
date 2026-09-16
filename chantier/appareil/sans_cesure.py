#!/usr/bin/env python3
"""Coupe la césure automatique dans un .docx.

Word laisse la césure désactivée par défaut ; LibreOffice, à l'import, applique
la sienne et coupe les mots composés — « lui-/même », « dix-/sept ». On pose donc
`suppressAutoHyphens` aux propriétés de paragraphe par défaut, ce qui vaut pour
les deux et ne change rien au texte.
"""
import re, shutil, sys, zipfile, os

BAL = '<w:suppressAutoHyphens w:val="true"/>'

def poser(chemin):
    tmp = chemin + ".tmp"
    with zipfile.ZipFile(chemin) as src, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as dst:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == "word/styles.xml":
                x = data.decode("utf-8")
                if BAL not in x:
                    if "<w:pPrDefault><w:pPr>" in x:
                        x = x.replace("<w:pPrDefault><w:pPr>", "<w:pPrDefault><w:pPr>" + BAL, 1)
                    elif "<w:pPrDefault/>" in x:
                        x = x.replace("<w:pPrDefault/>", "<w:pPrDefault><w:pPr>" + BAL + "</w:pPr></w:pPrDefault>", 1)
                    else:
                        x = x.replace("<w:docDefaults>", "<w:docDefaults><w:pPrDefault><w:pPr>" + BAL + "</w:pPr></w:pPrDefault>", 1)
                data = x.encode("utf-8")
            dst.writestr(item, data)
    shutil.move(tmp, chemin)
    print(f"césure coupée : {chemin}")

if __name__ == "__main__":
    for c in sys.argv[1:]:
        poser(c)
