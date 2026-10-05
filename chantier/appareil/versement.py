#!/usr/bin/env python3
"""Versement projet -> dépôt, en trois gestes, par copie d'octets.

  preparer   (Cowork)        extrait du transcript les documents lus par un fil
                             « tuyau », les mesure contre un clone du dépôt, et
                             monte versement_AAAAMMJJ.zip + son manifeste.
  appliquer  (session code)  dans un clone de main : contrôle les empreintes
                             « avant », copie, contrôle les empreintes « après »,
                             inscrit le versement à l'index, un commit.
  verifier   (Cowork)        sur un clone neuf : rend la liste des documents du
                             projet dont la copie au dépôt est identique, donc
                             supprimables du projet après accord de l'auteure.

Règles tenues par le code : rien ne s'écrit sans empreinte ; une empreinte
« avant » qui diffère arrête tout ; rien ne se supprime du projet ici.

Usage :
  python3 versement.py preparer --transcript T.jsonl --liste L.tsv --clone DIR --sortie DIR
  python3 versement.py appliquer --paquet versement_X.zip --clone DIR [--commit]
  python3 versement.py verifier --manifeste MANIFESTE_VERSEMENT.json --clone DIR

Liste L.tsv : chemin_projet<TAB>statut (decision|travail|valide|perime)[<TAB>chemin_depot]
Par défaut chemin_depot = chantier/<chemin_projet> ; travail/depot_2027/X -> chantier/livrables/depot_2027/X.
"""
import argparse, datetime, hashlib, json, os, shutil, subprocess, sys, zipfile

def sha(b): return hashlib.sha256(b).hexdigest()

def destination(chemin, explicite=None):
    if explicite: return explicite
    if chemin.startswith("travail/depot_2027/"):
        return "chantier/livrables/depot_2027/" + chemin[len("travail/depot_2027/"):]
    return "chantier/" + chemin

def extraire(transcript):
    """Documents rendus par project_read dans un transcript de fil : {chemin: octets}."""
    docs = {}
    for l in open(transcript, encoding="utf-8"):
        try: r = json.loads(l)
        except ValueError: continue
        c = r.get("message", {}).get("content")
        if not isinstance(c, list): continue
        for b in c:
            if b.get("type") != "tool_result": continue
            cont = b.get("content")
            txt = cont if isinstance(cont, str) else "".join(
                x.get("text", "") for x in cont if isinstance(x, dict))
            try: d = json.loads(txt)
            except ValueError: continue
            if isinstance(d, dict) and d.get("method") == "project_read":
                if "content" in d:
                    docs[d["path"]] = d["content"].encode("utf-8")
                elif "local_file" in d and os.path.exists(d["local_file"]):
                    # gros document : le texte est rendu dans un fichier à part
                    docs[d["path"]] = open(d["local_file"], "rb").read()
    return docs

def preparer(a):
    docs = extraire(a.transcript)
    liste = [l.rstrip("\n").split("\t") for l in open(a.liste, encoding="utf-8")
             if l.strip() and not l.startswith("#")]
    manquants = [c[0] for c in liste if c[0] not in docs]
    if manquants:
        print("ARRÊT — documents non lus par le tuyau :", len(manquants)); print("\n".join(manquants)); return 1
    jour = datetime.date.today().strftime("%Y%m%d")
    os.makedirs(a.sortie, exist_ok=True)
    zpath = os.path.join(a.sortie, f"versement_{jour}.zip")
    lignes = []
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for c in liste:
            chemin, statut = c[0], c[1]
            dest = destination(chemin, c[2] if len(c) > 2 and c[2] else None)
            b = docs[chemin]
            cible = os.path.join(a.clone, dest)
            avant = sha(open(cible, "rb").read()) if os.path.exists(cible) else None
            action = "ajout" if avant is None else ("identique" if avant == sha(b) else "remplacement")
            if action != "identique": z.writestr(dest, b)
            lignes.append({"chemin_projet": chemin, "chemin_depot": dest, "statut": statut,
                           "octets": len(b), "sha256": sha(b), "sha256_avant": avant, "action": action})
        man = {"versement": jour, "documents": lignes}
        z.writestr("MANIFESTE_VERSEMENT.json", json.dumps(man, ensure_ascii=False, indent=1))
    n = {k: sum(1 for x in lignes if x["action"] == k) for k in ("ajout", "remplacement", "identique")}
    print(zpath, "|", len(lignes), "documents |", n, "|", sum(x["octets"] for x in lignes), "octets")
    return 0

def appliquer(a):
    z = zipfile.ZipFile(a.paquet)
    man = json.loads(z.read("MANIFESTE_VERSEMENT.json"))
    ecarts = []
    for d in man["documents"]:
        cible = os.path.join(a.clone, d["chemin_depot"])
        actuel = sha(open(cible, "rb").read()) if os.path.exists(cible) else None
        if d["action"] != "identique" and actuel != d["sha256_avant"]:
            ecarts.append((d["chemin_depot"], d["sha256_avant"], actuel))
    if ecarts:
        print("ARRÊT — le dépôt a changé depuis la préparation :")
        for e in ecarts: print(" ", *e)
        return 1
    for d in man["documents"]:
        if d["action"] == "identique": continue
        cible = os.path.join(a.clone, d["chemin_depot"])
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        open(cible, "wb").write(z.read(d["chemin_depot"]))
        if sha(open(cible, "rb").read()) != d["sha256"]:
            print("ARRÊT — empreinte après copie fausse :", d["chemin_depot"]); return 1
    idx = os.path.join(a.clone, "chantier/methode/index_versements.json")
    hist = json.load(open(idx, encoding="utf-8")) if os.path.exists(idx) else []
    hist.append(man)
    os.makedirs(os.path.dirname(idx), exist_ok=True)
    json.dump(hist, open(idx, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("appliqué :", sum(1 for d in man["documents"] if d["action"] != "identique"), "fichiers")
    if a.commit:
        subprocess.run(["git", "-C", a.clone, "add", "-A"], check=True)
        subprocess.run(["git", "-C", a.clone, "commit", "-m",
                        f"Versement {man['versement']} : {len(man['documents'])} documents du projet"], check=True)
    return 0

def verifier(a):
    man = json.load(open(a.manifeste, encoding="utf-8"))
    ok, ko = [], []
    for d in man["documents"]:
        cible = os.path.join(a.clone, d["chemin_depot"])
        s = sha(open(cible, "rb").read()) if os.path.exists(cible) else None
        (ok if s == d["sha256"] else ko).append(d)
    print(f"identiques au dépôt : {len(ok)} | absents ou différents : {len(ko)}")
    print("# supprimables du projet, après accord de l'auteure (statut valide ou perime seulement) :")
    for d in ok:
        if d["statut"] in ("valide", "perime"): print(d["chemin_projet"])
    for d in ko: print("# NON VERSÉ :", d["chemin_projet"])
    return 0 if not ko else 1

if __name__ == "__main__":
    p = argparse.ArgumentParser(); s = p.add_subparsers(dest="geste", required=True)
    x = s.add_parser("preparer"); x.add_argument("--transcript", required=True); x.add_argument("--liste", required=True); x.add_argument("--clone", required=True); x.add_argument("--sortie", required=True)
    x = s.add_parser("appliquer"); x.add_argument("--paquet", required=True); x.add_argument("--clone", required=True); x.add_argument("--commit", action="store_true")
    x = s.add_parser("verifier"); x.add_argument("--manifeste", required=True); x.add_argument("--clone", required=True)
    a = p.parse_args()
    sys.exit({"preparer": preparer, "appliquer": appliquer, "verifier": verifier}[a.geste](a))
