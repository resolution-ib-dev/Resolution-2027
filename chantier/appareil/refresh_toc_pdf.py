#!/usr/bin/env python3
"""PDF d'un .docx avec son sommaire calculé.

Pourquoi ce détour. La conversion simple laisse le champ de table des matières
vide : LibreOffice construit le sommaire sur les NIVEAUX DE PLAN, et le .docx
produit par `md2docx.js` pose bien les styles « Heading 1-3 » mais laisse le
niveau de plan à zéro. Word s'en passe — son champ TOC \\o "1-3" travaille sur
les styles — LibreOffice non.

On pose donc le niveau de plan d'après le style, au rendu seulement, puis on
met l'index à jour et on exporte. Le .docx n'est pas touché : il garde son
champ vivant, que Word recalculera à l'ouverture.
"""
import os, subprocess, sys, time, uno
from com.sun.star.beans import PropertyValue

NIVEAU = {"Heading 1": 1, "Heading 2": 2, "Heading 3": 3,
          "Titre 1": 1, "Titre 2": 2, "Titre 3": 3}


def p(n, v):
    x = PropertyValue(); x.Name = n; x.Value = v; return x


def contexte(port, essais=60):
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local)
    url = f"uno:socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext"
    for _ in range(essais):
        try:
            return resolver.resolve(url)
        except Exception:
            time.sleep(0.5)
    raise SystemExit("soffice injoignable")


def poser_niveaux(doc):
    """Rend le nombre de paragraphes dont le niveau de plan a été posé."""
    pose = 0
    en = doc.Text.createEnumeration()
    while en.hasMoreElements():
        e = en.nextElement()
        if not e.supportsService("com.sun.star.text.Paragraph"):
            continue
        n = NIVEAU.get(e.getPropertyValue("ParaStyleName"))
        if n and e.getPropertyValue("OutlineLevel") != n:
            e.setPropertyValue("OutlineLevel", n)
            pose += 1
    return pose


def main(src, out, port=2005):
    proc = subprocess.Popen([
        "soffice", "--headless", "--norestore", "--invisible",
        f"--accept=socket,host=127.0.0.1,port={port};urp;",
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        ctx = contexte(port)
        desktop = ctx.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", ctx)
        doc = desktop.loadComponentFromURL(
            uno.systemPathToFileUrl(os.path.abspath(src)), "_blank", 0,
            (p("Hidden", True),))
        pose = poser_niveaux(doc)
        nb = doc.getDocumentIndexes().getCount()
        # Deux passes : la première pose le sommaire, la seconde recale les
        # numéros de page que son insertion vient de décaler.
        for _ in range(2):
            for i in range(nb):
                doc.getDocumentIndexes().getByIndex(i).update()
        doc.storeToURL(uno.systemPathToFileUrl(os.path.abspath(out)),
                       (p("FilterName", "writer_pdf_Export"),))
        doc.close(False)
        print(f"écrit : {out} — {pose} niveaux de plan posés, {nb} index")
    finally:
        proc.terminate()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
