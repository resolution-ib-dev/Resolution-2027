# -*- coding: utf-8 -*-
"""Contrôle des interdits de projection. Ouvre chaque cible et lit son contenu."""
import os,re,sys,glob

RACINE=sys.argv[1]
INTERDITS=[
 ("nom de personne", r"\b(Ingrid\s+Barrat|Arthur\s+Marle|Moïse\s+Mitterrand)\b"),
 ("nom d'organisation du projet", r"\bR[ée]solution\b"),
 ("titre de l'ouvrage", r"État partout|justice nulle part"),
 ("nomenclature doctrinale interne", r"\bD\d+(-\d+)*(-[pe]\d+)?\b"),
 ("nomenclature de positions interne", r"\bC-\d{2}\b"),
 ("nomenclature d'arbitrages interne", r"\bA-\d{2,4}\b"),
 ("nomenclature de contrôles interne", r"\b[RVIEDN]\d\b"),
 ("renvoi à un fichier du corpus", r"[\w/]+\.(json|py|xlsx|xls|html|tsv)\b"),
 ("chemin de l'atelier ou du coffre", r"/mnt/|referentiels/|appareil/|methode/|livrables/"),
 ("historique de maison", r"\b(coffre|atelier|fil courant|banc des chouchous|make controle|skill)\b"),
]
# M-0NN est l'identifiant stable du découpage : il est admis.
ADMIS=re.compile(r"^M-\d{3}$")

def presents(racine):
    """Un renvoi vers une pièce du paquet lui-même est admis : la machine l'a."""
    noms=set()
    for d,_,fs in os.walk(racine):
        for f in fs:
            noms.add(f)
            noms.add(re.sub(r'\d{8}','AAAAMMJJ',f))
    return noms

DANS_LE_PAQUET=presents(RACINE)
anomalies=[]
fichiers=sorted(glob.glob(os.path.join(RACINE,'**','*.md'),recursive=True)+
                glob.glob(os.path.join(RACINE,'**','*.tsv'),recursive=True))
for f in fichiers:
    txt=open(f,encoding='utf-8').read()
    for nom,motif in INTERDITS:
        for m in re.finditer(motif,txt,re.I):
            s=m.group(0)
            if ADMIS.match(s) or s in DANS_LE_PAQUET: continue
            ligne=txt[:m.start()].count('\n')+1
            anomalies.append((os.path.relpath(f,RACINE),ligne,nom,s))

print(f"{len(fichiers)} cibles ouvertes et lues")
if anomalies:
    print(f"{len(anomalies)} anomalie(s) :")
    for a in anomalies[:60]: print(' ',a)
else:
    print("0 anomalie — aucun nom, aucune nomenclature interne, aucun renvoi hors portée")
