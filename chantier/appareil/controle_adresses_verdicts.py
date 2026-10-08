import json, sys, collections
sys.path.insert(0,"/home/claude/droit")
import droit
adr = json.load(open("adresses.json"))
res=[]
for fichier, code, num, kind, seq in adr:
    row={"f":fichier,"code":code,"num":num,"kind":kind,"seq":seq}
    for label, jour in (("auj","2026-10-07"),("2028","2028-01-01")):
        try:
            a = droit.article(code, num, jour=jour)
            row[label] = a.get("etat","?")
            row[label+"_id"]=a["id"]
        except KeyError as e:
            row[label]="CODE_NON_PORTE"
        except FileNotFoundError:
            row[label]="CODE_NON_PORTE"
        except LookupError as e:
            row[label] = "ABSENT" if "absent de l'extrait" in str(e) else "INAPPLICABLE"
    res.append(row)
json.dump(res, open("verdicts.json","w"), ensure_ascii=False)
c=collections.Counter((r["auj"],r["2028"]) for r in res)
for k,v in c.most_common(): print(v, k)
