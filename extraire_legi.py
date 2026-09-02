#!/usr/bin/env python3
"""Extrait, de la base LEGI de la DILA, les seuls codes dont le chantier a besoin.

Ne tourne PAS dans l'atelier : il tourne dans l'action programmée du dépôt.
L'atelier ne lit que ce que ce script a écrit — `droit.py` s'en charge.

Principe de prudence : le script ne présume ni de l'adresse du dépôt de la
DILA, ni de la disposition interne de l'archive. Il DÉCOUVRE l'une par l'API
de data.gouv.fr et l'autre en balayant l'archive. Quand un code ne rend aucun
article, il ne devine pas : il écrit un diagnostic et il échoue.

Sortie, un fichier par code : data/<court>.jsonl.gz, une ligne par article.
  {id, num, code, etat, date_debut, date_fin, section, texte}
Plus data/_manifeste.json : millésime du dump, comptes, empreintes.
"""
import datetime
import gzip
import hashlib
import io
import json
import os
import pathlib
import re
import sys
import tarfile
import urllib.request
import xml.etree.ElementTree as ET
from html.entities import html5, name2codepoint
from collections import Counter, defaultdict

RACINE = pathlib.Path(__file__).parent
DATA = RACINE / "data"
DATA.mkdir(exist_ok=True)

# Le dépôt ouvert de la DILA. La fiche data.gouv.fr ne porte pas de fichier :
# sa ressource « base LEGI » est ce répertoire, qu'il faut lire soi-même.
# Constaté le 20260901 — trois ressources, aucune archive directe.
BASE = "https://echanges.dila.gouv.fr/OPENDATA/LEGI/"

AGENT = {"User-Agent": "Mozilla/5.0 (compatible; resolution-droit/2.0)"}

# Une archive complète porte « global » dans son nom ; les autres sont les
# livraisons journalières, qui s'appliquent par-dessus dans l'ordre du temps.
# Le motif n'est pas présumé : on lit l'index et on classe ce qu'on y trouve.
RE_ARCHIVE = re.compile(r'href="([^"]+\.tar\.gz)"', re.I)
RE_HORODATAGE = re.compile(r"(20\d{6})[-_](\d{6})")


def recuperer(url, timeout=300):
    req = urllib.request.Request(url, headers=AGENT)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def journal(*a):
    print(*a, flush=True)


# --------------------------------------------------------------------------
# 1. Trouver l'archive


def horodatage(nom):
    m = RE_HORODATAGE.search(nom)
    return m.group(1) + m.group(2) if m else ""


def resoudre_archives(max_journalieres=800):
    """Rend (liste d'URL dans l'ordre d'application, millésime).

    La base complète est remplacée une ou deux fois l'an ; les livraisons
    journalières portent le delta. Prendre la complète seule laisserait le
    droit vieux de plusieurs mois — on applique donc la complète, puis toutes
    les journalières postérieures, dans l'ordre. Une version d'article plus
    récente écrase la précédente par son identifiant.
    """
    try:
        html = recuperer(BASE, timeout=120).decode("utf-8", "replace")
    except Exception as e:
        diagnostic({"motif": "index de la DILA illisible", "base": BASE, "erreur": repr(e)})
        sys.exit(f"ÉCHEC — index DILA illisible : {e!r}. Voir data/_diagnostic.json.")

    noms = RE_ARCHIVE.findall(html)
    noms = [n.split("/")[-1] for n in noms]
    noms = sorted(set(n for n in noms if n.endswith(".tar.gz")))
    journal(f"index DILA : {len(noms)} archive(s) listée(s)")

    if not noms:
        diagnostic({"motif": "aucune archive .tar.gz dans l'index",
                    "base": BASE, "extrait_html": html[:4000]})
        sys.exit("ÉCHEC — aucune archive dans l'index. Voir data/_diagnostic.json.")

    completes = [n for n in noms if "global" in n.lower()]
    if not completes:
        diagnostic({"motif": "aucune archive complète repérée — le mot « global » ne figure "
                             "dans aucun nom ; le classement complet/journalier est à revoir",
                    "base": BASE, "archives_listees": noms[:60]})
        sys.exit("ÉCHEC — archive complète non repérée. Voir data/_diagnostic.json.")

    completes.sort(key=horodatage)
    pleine = completes[-1]
    seuil = horodatage(pleine)

    journalieres = sorted(
        (n for n in noms if "global" not in n.lower() and horodatage(n) > seuil),
        key=horodatage)
    if len(journalieres) > max_journalieres:
        diagnostic({"motif": "trop de livraisons journalières à appliquer",
                    "complete": pleine, "journalieres": len(journalieres)})
        sys.exit("ÉCHEC — trop de journalières. Voir data/_diagnostic.json.")

    journal(f"complète : {pleine}")
    journal(f"journalières postérieures : {len(journalieres)}")
    millesime = (horodatage(journalieres[-1]) if journalieres else seuil)[:8]
    return [BASE + n for n in [pleine] + journalieres], millesime


# --------------------------------------------------------------------------
# 2. Balayer l'archive en flux


def texte_de(el):
    """Texte d'un sous-arbre, balises inline aplaties, espaces normalisés."""
    if el is None:
        return ""
    brut = "".join(el.itertext())
    brut = brut.replace(" ", " ")
    lignes = [re.sub(r"[ \t]+", " ", l).strip() for l in brut.splitlines()]
    return "\n".join(l for l in lignes if l).strip()


def premier(el, *noms):
    """Premier descendant portant l'un de ces noms de balise, insensible au cas."""
    cibles = {n.upper() for n in noms}
    for sous in el.iter():
        if sous.tag.upper().split("}")[-1] in cibles:
            return sous
    return None


RE_DOCTYPE = re.compile(rb"<!DOCTYPE[^>]*(\[[^\]]*\])?[^>]*>", re.S)
RE_ENTITE = re.compile(rb"&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9A-Fa-f]+);)([A-Za-z][A-Za-z0-9._-]*);")


def analyser(donnees):
    """Rend la racine XML, ou lève. Deux passes.

    La seconde rattrape ce qui a fait perdre le bloc TVA du CGI au premier
    tour : une déclaration de type et des entités nommées qu'ElementTree ne
    connaît pas. Elles étaient jusqu'ici avalées en silence — un article perdu
    ne disait rien, et un trou contigu passait pour un code court.
    """
    try:
        return ET.fromstring(donnees)
    except ET.ParseError:
        pass
    reduit = RE_DOCTYPE.sub(b"", donnees)
    reduit = RE_ENTITE.sub(_resoudre_entite, reduit)
    return ET.fromstring(reduit)


def _resoudre_entite(m):
    """« &ccedil; » devient « ç », pas « &amp;ccedil; ».

    Une entité échappée laisserait le verbatim faux — « per&ccedil;ue » au lieu
    de « perçue » —, et un verbatim faux dans un amendement déposé est pire
    qu'un article absent. Une entité inconnue est échappée, faute de mieux, et
    elle reste visible dans le texte plutôt que de faire perdre l'article.
    """
    nom = m.group(1).decode("ascii", "replace")
    car = html5.get(nom + ";") or html5.get(nom)
    if car is None:
        car = chr(name2codepoint[nom]) if nom in name2codepoint else None
    if car is None:
        return b"&amp;" + m.group(1) + b";"
    return ("&#%d;" % ord(car[0])).encode("ascii") if len(car) == 1 else \
        "".join("&#%d;" % ord(c) for c in car).encode("ascii")


def lire_article(donnees):
    """Rend le dict d'un article, ou None si le XML n'en porte pas.
    Lève si le XML est illisible — l'appelant compte et signale."""
    racine = analyser(donnees)
    art = racine if racine.tag.upper().endswith("ARTICLE") else premier(racine, "ARTICLE")
    if art is None:
        return None

    def champ(*noms):
        el = premier(art, *noms)
        return (el.text or "").strip() if el is not None and el.text else ""

    ident = champ("ID")
    if not ident.startswith("LEGIARTI"):
        return None
    contenu = premier(art, "BLOC_TEXTUEL")
    texte = texte_de(premier(contenu, "CONTENU") if contenu is not None else None)
    if not texte:
        texte = texte_de(premier(art, "CONTENU"))
    return {
        "id": ident,
        "num": champ("NUM"),
        "etat": champ("ETAT") or "INCONNU",
        "date_debut": champ("DATE_DEBUT"),
        "date_fin": champ("DATE_FIN"),
        "texte": texte,
    }


def lire_structure(donnees):
    """Rend {LEGIARTI: 'Titre > Chapitre > Section'} depuis un fichier de structure."""
    try:
        racine = analyser(donnees)
    except ET.ParseError:
        return {}
    chemins = {}

    def descendre(el, pile):
        nom = el.tag.upper().split("}")[-1]
        if nom in ("SECTION_TA", "TM", "LIEN_SECTION_TA"):
            titre = el.get("titre") or ""
            if not titre:
                t = premier(el, "TITRE_TA", "TITRE_TM")
                titre = texte_de(t)
            if titre:
                pile = pile + [titre.strip()]
        if nom == "LIEN_ART":
            ident = el.get("id") or ""
            if ident.startswith("LEGIARTI"):
                chemins[ident] = " > ".join(pile)
        for sous in list(el):
            descendre(sous, pile)

    descendre(racine, [])
    return chemins


def balayer(urls, cibles):
    """cibles : {LEGITEXT: court}. Balaie les archives dans l'ordre reçu.

    Une archive postérieure écrase par identifiant ce qu'une antérieure a
    posé : c'est ainsi que les livraisons journalières mettent à jour la base
    complète, y compris quand un article passe de VIGUEUR à ABROGE.
    """
    articles = defaultdict(dict)   # court -> {id: dict}
    sections = defaultdict(dict)   # court -> {id: chemin}
    echecs = defaultdict(int)      # court -> XML illisibles
    exemples_echec = []
    chemins = defaultdict(list)    # court -> chemins d'exemple, pour le diagnostic
    echantillon = []
    total = 0

    for rang, url in enumerate(urls, 1):
        vus = touches = 0
        try:
            req = urllib.request.Request(url, headers=AGENT)
            with urllib.request.urlopen(req, timeout=3600) as flux:
                with tarfile.open(fileobj=flux, mode="r|gz") as tar:
                    for membre in tar:
                        if not membre.isfile() or not membre.name.endswith(".xml"):
                            continue
                        vus += 1
                        if len(echantillon) < 25 and "LEGITEXT" in membre.name:
                            echantillon.append(membre.name)

                        court = None
                        for legitext, c in cibles.items():
                            if legitext in membre.name:
                                court = c
                                break
                        if court is None:
                            continue
                        if len(chemins[court]) < 15:
                            chemins[court].append(membre.name)

                        f = tar.extractfile(membre)
                        if f is None:
                            continue
                        donnees = f.read()
                        touches += 1

                        if b"<LIEN_ART" in donnees:
                            sections[court].update(lire_structure(donnees))
                        if b"<ARTICLE" in donnees:
                            try:
                                a = lire_article(donnees)
                            except Exception as e:
                                echecs[court] += 1
                                if len(exemples_echec) < 12:
                                    exemples_echec.append(
                                        {"chemin": membre.name, "erreur": repr(e)[:200]})
                                continue
                            if a:
                                articles[court][a["id"]] = a
        except Exception as e:
            # Une journalière illisible ne doit pas perdre le travail déjà fait ;
            # la complète, si.
            if rang == 1:
                diagnostic({"motif": "archive complète illisible", "url": url, "erreur": repr(e)})
                sys.exit(f"ÉCHEC — archive complète illisible : {e!r}.")
            journal(f"  [{rang}/{len(urls)}] ILLISIBLE, ignorée : {url.split('/')[-1]} — {e!r}")
            continue

        total += vus
        journal(f"  [{rang}/{len(urls)}] {url.split('/')[-1]} — {vus} XML, {touches} retenus")

    journal(f"balayage terminé : {total} fichiers XML sur {len(urls)} archive(s)")
    if sum(echecs.values()):
        journal("XML illisibles par code : " + json.dumps(dict(echecs)))
    return articles, sections, echantillon, dict(echecs), exemples_echec, dict(chemins)


# --------------------------------------------------------------------------
# 3. Écrire


FIN_OUVERTE = ("2999-01-01", "", None)


def applicable(a, jour):
    """Vrai si cette version s'applique le jour dit.

    **L'état ne décide pas, l'intervalle de dates décide.** LEGI marque
    `ABROGE_DIFF` une version qui s'applique aujourd'hui et dont l'abrogation
    est programmée : filtrer sur `VIGUEUR` jetait ces articles-là. Le CGI en
    porte 375, dont tout le bloc TVA, et c'est ce qui a fait disparaître
    l'article 279 de deux extraits successifs.
    """
    d = a.get("date_debut") or ""
    f = a.get("date_fin") or ""
    if d and d > jour:
        return False
    if f and f not in FIN_OUVERTE and f <= jour:
        return False
    return True


def a_venir(a, jour):
    """Version dont l'application commence après le jour dit."""
    d = a.get("date_debut") or ""
    return bool(d) and d > jour


def diagnostic(charge):
    (DATA / "_diagnostic.json").write_text(
        json.dumps(charge, ensure_ascii=False, indent=2), encoding="utf-8")


def ecrire(court, cle, arts, sect):
    chemin = DATA / f"{court}.jsonl.gz"
    h = hashlib.sha256()
    n = 0
    with gzip.open(chemin, "wt", encoding="utf-8", compresslevel=9) as sortie:
        for ident in sorted(arts):
            a = dict(arts[ident])
            a["code"] = cle
            a["section"] = sect.get(ident, "")
            ligne = json.dumps(a, ensure_ascii=False, sort_keys=True)
            sortie.write(ligne + "\n")
            h.update(ligne.encode())
            n += 1
    return {"fichier": chemin.name, "articles": n,
            "octets": chemin.stat().st_size, "sha256": h.hexdigest()}


def main():
    cfg = json.loads((RACINE / "codes.json").read_text(encoding="utf-8"))
    cibles = {c["legitext"]: c["court"] for c in cfg["codes"]}
    libelles = {c["court"]: c["cle"] for c in cfg["codes"]}

    temoins = {c["court"]: c.get("temoin") for c in cfg["codes"]}
    jour = datetime.date.today().isoformat()
    journal(f"jour de référence : {jour}")

    urls, millesime = resoudre_archives()
    articles, sections, echantillon, echecs, exemples, chemins = balayer(urls, cibles)

    vides = [libelles[c] for c in libelles if not articles.get(c)]
    if vides:
        diagnostic({
            "motif": "codes sans aucun article extrait",
            "codes_vides": vides,
            "archives": urls[:3] + (["…"] if len(urls) > 3 else []),
            "echantillon_de_chemins": echantillon,
            "comptes": {libelles[c]: len(articles.get(c, {})) for c in libelles},
        })
        sys.exit("ÉCHEC — " + ", ".join(vides) + ". Voir data/_diagnostic.json.")

    # Un XML illisible n'est plus une perte silencieuse : il compte et il bloque.
    if sum(echecs.values()):
        diagnostic({"motif": "fichiers XML illisibles — extraction incomplète",
                    "echecs_par_code": {libelles[c]: n for c, n in echecs.items()},
                    "exemples": exemples})
        sys.exit(f"ÉCHEC — {sum(echecs.values())} XML illisibles. "
                 "Voir data/_diagnostic.json.")

    # Témoin : un article ordinaire que chaque code DOIT porter. C'est ce qui
    # aurait attrapé, au premier tour, le trou du bloc TVA du CGI — 2 031
    # articles, un job vert, et l'article 279 absent.
    def num_normal(s):
        return re.sub(r"[.\s]+", "", (s or "").lower())

    manquants, detail = [], {}
    for court, cle in libelles.items():
        t = temoins.get(court)
        if not t:
            continue
        par_num = defaultdict(list)
        for a in articles[court].values():
            par_num[num_normal(a["num"])].append(a)
        cible = par_num.get(num_normal(t), [])
        if any(applicable(a, jour) for a in cible):
            continue
        manquants.append(f"{cle} : témoin « {t} » absent")
        # Tout ce qu'il faut pour trancher sans relancer : le témoin est-il là
        # sous un autre état, quels numéros l'entourent, et à quoi ressemblent
        # les chemins réels de l'archive pour ce code.
        tete = re.match(r"^([LRD]?)\.?\s*(\d+)", t or "")
        base = int(tete.group(2)) if tete else None
        voisins = []
        if base is not None:
            for a in articles[court].values():
                m = re.match(r"^([LRD]?)\.?\s*(\d+)", a["num"] or "")
                if m and m.group(1) == tete.group(1) and abs(int(m.group(2)) - base) <= 30:
                    voisins.append(a["num"])
        detail[cle] = {
            "temoin": t,
            "present_sous_un_autre_etat": [
                {"id": a["id"], "etat": a["etat"], "date_debut": a["date_debut"],
                 "date_fin": a["date_fin"]} for a in cible],
            "articles_retenus": len(articles[court]),
            "etats": dict(Counter(a["etat"] for a in articles[court].values())),
            "numeros_voisins": sorted(set(voisins))[:40],
            "chemins_exemple": chemins.get(court, []),
        }
    if manquants:
        diagnostic({"motif": "témoins absents — extraction incomplète",
                    "manquants": manquants, "detail": detail,
                    "comptes": {libelles[c]: len(articles[c]) for c in libelles}})
        sys.exit("ÉCHEC — " + " ; ".join(manquants) + ". Voir data/_diagnostic.json.")

    manifeste = {"millesime_legi": millesime, "jour_de_reference": jour,
                 "archives": len(urls), "archive": urls[0],
                 "extrait_le": os.environ.get("DATE_EXTRACTION", ""), "codes": {}}
    for court, cle in libelles.items():
        # On garde ce qui s'applique aujourd'hui et ce qui s'appliquera ;
        # l'historique périmé ne sert à rien à un rédacteur d'amendement et il
        # multiplierait le dépôt par dix.
        vivants = {i: a for i, a in articles[court].items()
                   if applicable(a, jour) or a_venir(a, jour)}
        manifeste["codes"][cle] = ecrire(court, cle, vivants, sections.get(court, {}))
        manifeste["codes"][cle]["court"] = court
        app = sum(1 for a in vivants.values() if applicable(a, jour))
        prog = sum(1 for a in vivants.values()
                   if applicable(a, jour) and a.get("date_fin") not in FIN_OUVERTE)
        manifeste["codes"][cle]["applicables"] = app
        manifeste["codes"][cle]["a_venir"] = len(vivants) - app
        manifeste["codes"][cle]["fin_programmee"] = prog
        manifeste["codes"][cle]["etats"] = dict(Counter(a["etat"] for a in vivants.values()))
        manifeste["codes"][cle]["sections_rattachees"] = sum(
            1 for i in vivants if sections.get(court, {}).get(i))
        journal(f"  {cle} : {app} applicables ({prog} à fin programmée), "
                f"{len(vivants) - app} à venir, sur {len(articles[court])} versions")

    (DATA / "_manifeste.json").write_text(
        json.dumps(manifeste, ensure_ascii=False, indent=2), encoding="utf-8")
    if (DATA / "_diagnostic.json").exists():
        (DATA / "_diagnostic.json").unlink()
    journal("manifeste écrit.")


if __name__ == "__main__":
    main()
