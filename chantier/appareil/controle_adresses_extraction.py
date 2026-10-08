import re, json, pathlib
from collections import Counter
BASE = pathlib.Path("/home/claude/extraction/extraction_p1/pieces")
CODES = {
 "code général des impôts":"cgi","code des impositions sur les biens et services":"cibs",
 "code de la sécurité sociale":"css","code général des collectivités territoriales":"cgct",
 "code du travail":"travail","code de la construction et de l'habitation":"cch",
 "code de l'environnement":"environnement","livre des procédures fiscales":"lpf",
 "code civil":"civil","code monétaire et financier":"monetaire","code de commerce":"commerce",
 "code de l'entrée et du séjour des étrangers et du droit d'asile":"ceseda",
 "code de l'urbanisme":"urbanisme","code rural et de la pêche maritime":"rural",
 "code du cinéma et de l'image animée":"cinema","code des douanes":"douanes",
 "code de l'action sociale et des familles":"casf","code de la santé publique":"sante",
 "code du patrimoine":"patrimoine","code de l'éducation":"education",
 "code général de la propriété des personnes publiques":"cg3p","code des assurances":"assurances",
 "code de l'énergie":"energie","code des transports":"transports","code du sport":"sport",
 "code de la commande publique":"commande_publique","code général de la fonction publique":"cgfp",
 "code de la consommation":"conso","code de la voirie routière":"voirie",
 "code de la recherche":"recherche","code de la défense":"defense","code de procédure pénale":"cpp",
}
NOMS = sorted(CODES, key=len, reverse=True)
ROMS = sorted({"quaterdecies","quatervicies","septdecies","octodecies","novodecies","quindecies",
 "sexdecies","duodecies","terdecies","undecies","quinquies","septvicies","octovicies","novovicies",
 "quinvicies","unvicies","duovicies","tervicies","sexvicies","quater","septies","octies","nonies",
 "decies","vicies","tricies","sexies","bis","ter"}, key=len, reverse=True)
ROM = "(?:" + "|".join(ROMS) + r")(?:-0)?"
NUM = (r"(?:L\.?\s?|R\.?\s?|D\.?\s?|LO\s?)?\d+(?:-\d+)*(?:\s-0)?"
       r"(?:\s" + ROM + r"\b){0,2}(?:\s[A-Z]{1,2}\b)?(?:\s" + ROM + r"\b){0,2}(?:\s[A-Z]{1,2}\b)?")
LIST = NUM + r"(?:\s*(?:,\s*|\s+et\s+|\s+ou\s+|\s+à\s+)" + NUM + r")*"
ART_RE = re.compile(r"\b(?:[Aa]rticles?|[Aa]rt\.)\s+(" + LIST + r")")
DESIG = re.compile(r"\bdu (même) (?:code|livre)\b|\b(?:du|de la|des|au) (" + "|".join(re.escape(k) for k in NOMS) + r")")

rows=[]; horsctl=[]
for f in sorted(BASE.glob("*.md")):
    txt=f.read_text(encoding="utf-8").replace("’","'").replace(" "," ").replace(" "," ")
    cut=txt.find("## [interne]"); norma = txt[:cut] if cut>0 else txt
    dernier=None; chap=None
    CHAPEAU = re.compile(r"\b(?:Le|La|Les|Du|Au) (" + "|".join(re.escape(k) for k in NOMS) + r")\b[^.]{0,60}(?:est ainsi modifié|sont ainsi modifié|est ainsi rédigé|est ainsi complété)")
    for ligne in norma.split("\n"):
        ch = CHAPEAU.search(ligne)
        if ch: chap = CODES[ch.group(1)]; dernier = chap
        for m in ART_RE.finditer(ligne):
            seq=m.group(1).rstrip(" ,.;")
            d=DESIG.search(ligne[m.end():])
            if d and d.group(2): code=CODES[d.group(2)]; dernier=code
            elif d and d.group(1) and dernier: code=dernier
            elif chap and re.search(r"\b(?:sont|est) (?:abrogé|supprimé|ainsi|remplacé|complété)", ligne):
                code=chap
            else:
                horsctl.append((f.name,seq,"aucune désignation de code exploitable")); continue
            for p in re.split(r"\s*,\s*|\s+et\s+|\s+ou\s+", seq):
                p=p.strip().rstrip(" ,.;")
                if not p: continue
                if " à " in p:
                    a,b=p.split(" à ",1)
                    rows.append([f.name,code,a.strip(),"borne-debut",seq])
                    rows.append([f.name,code,b.strip(),"borne-fin",seq])
                else:
                    rows.append([f.name,code,p,"simple",seq])
json.dump(rows,open("adresses.json","w"),ensure_ascii=False)
json.dump(horsctl,open("horsctl.json","w"),ensure_ascii=False)
print("occurrences:",len(rows)," hors contrôle:",len(horsctl))
