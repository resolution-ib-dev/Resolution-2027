#!/usr/bin/env python3
"""Lecteur du texte en vigueur — le seul canal du chantier vers le droit.

Il lit ce que l'action a écrit dans data/. Il n'appelle rien, il ne cherche
rien en ligne : le droit est une source déclarée, pas un fetch.

Trois interdits, tenus par le code et non par la discipline :
  - aucun article ne sort sans son identifiant et sa date de version ;
  - aucun article abrogé ne sort sans que l'état soit dit ;
  - un article demandé et absent rend un échec, jamais un texte approchant.

Emploi en ligne de commande :
    python3 droit.py article "code général des impôts" 279
    python3 droit.py article cgi "278 sexies-0 A"
    python3 droit.py section cgi "Taux réduit"
    python3 droit.py verifier vecteurs.json      # lot d'adresses à contrôler
    python3 droit.py etat

Emploi depuis un script :
    from droit import article, chercher, fraicheur
"""
import gzip
import json
import pathlib
import re
import sys
import unicodedata
from datetime import date, datetime

RACINE = pathlib.Path(__file__).parent
DATA = RACINE / "data"
FIN_OUVERTE = {"2999-01-01", "", None}

_cache = {}


# --------------------------------------------------------------------------
# normalisation


def _sans_accent(s):
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def norm_num(a):
    """« L. 2334-1 », « L2334-1 » et « l. 2334 - 1 » sont la même adresse.
    Seules la ponctuation et la casse sont normalisées, jamais le numéro :
    « 200 A » ne devient pas « 200 », et « 278 sexies-0 A » ne se coupe pas."""
    a = _sans_accent(str(a)).replace(" ", " ")
    return re.sub(r"[.\s]+", "", a)


def _cfg():
    return json.loads((RACINE / "codes.json").read_text(encoding="utf-8"))["codes"]


def resoudre_code(nom):
    """Rend l'entrée de codes.json pour un libellé exact ou un nom court.
    N'apparie jamais au plus proche (A-94) : inconnu, c'est un échec."""
    n = _sans_accent(nom).strip()
    for c in _cfg():
        if n == _sans_accent(c["cle"]) or n == c["court"]:
            return c
    connus = ", ".join(f"{c['court']} ({c['cle']})" for c in _cfg())
    raise KeyError(f"code inconnu : « {nom} ». Codes portés : {connus}")


def charger(nom):
    c = resoudre_code(nom)
    if c["court"] in _cache:
        return _cache[c["court"]]
    f = DATA / f"{c['court']}.jsonl.gz"
    if not f.exists():
        raise FileNotFoundError(
            f"{f} absent — le dépôt de droit n'a pas été rafraîchi, "
            "ou le clone est incomplet. Rien ne se supplée de mémoire.")
    index = {}
    with gzip.open(f, "rt", encoding="utf-8") as src:
        for ligne in src:
            a = json.loads(ligne)
            index.setdefault(norm_num(a["num"]), []).append(a)
    _cache[c["court"]] = index
    return index


# --------------------------------------------------------------------------
# lecture


def manifeste():
    p = DATA / "_manifeste.json"
    if not p.exists():
        raise FileNotFoundError("data/_manifeste.json absent — extrait jamais produit.")
    return json.loads(p.read_text(encoding="utf-8"))


def fraicheur(seuil_jours=45):
    """Rend (millésime, âge en jours, périmé). Un extrait vieux se dit."""
    m = manifeste()
    mil = m.get("millesime_legi", "")
    if not re.fullmatch(r"20\d{6}", mil or ""):
        return mil, None, True
    d = datetime.strptime(mil, "%Y%m%d").date()
    age = (date.today() - d).days
    return mil, age, age > seuil_jours


def applicable(a, jour=None):
    """Vrai si cette version s'applique le jour dit.

    **C'est l'intervalle de dates qui décide, jamais l'état.** LEGI marque
    `ABROGE_DIFF` une version qui s'applique aujourd'hui et dont l'abrogation
    est déjà votée : l'article 279 du code général des impôts est dans ce cas,
    applicable et abrogé au 1er janvier 2027. Filtrer sur `VIGUEUR` l'aurait
    fait passer pour absent — c'est arrivé deux fois.
    """
    jour = jour or str(date.today())
    d, f = a.get("date_debut") or "", a.get("date_fin") or ""
    if d and d > jour:
        return False
    if f and f not in FIN_OUVERTE and f <= jour:
        return False
    return True


def article(code, num, jour=None, tout=False):
    """Rend la version applicable. Lève si absente. Ne rend jamais un voisin."""
    jour = jour or str(date.today())
    index = charger(code)
    trouves = index.get(norm_num(num), [])
    if tout:
        return trouves
    if not trouves:
        raise LookupError(f"{code}, article {num} : absent de l'extrait. "
                          "Vérifier le numéro ou le code — aucune approximation.")
    vivants = [a for a in trouves if applicable(a, jour)]
    if not vivants:
        futurs = sorted((a for a in trouves if (a.get("date_debut") or "") > jour),
                        key=lambda a: a["date_debut"])
        if futurs:
            raise LookupError(
                f"{code}, article {num} : aucune version applicable au {jour}. "
                f"Une version entre en vigueur le {futurs[0]['date_debut']} "
                f"({futurs[0]['id']}). Ne pas rédiger sur un texte non encore applicable.")
        etats = ", ".join(sorted({a.get("etat", "?") for a in trouves}))
        raise LookupError(f"{code}, article {num} : aucune version applicable au {jour} "
                          f"(états portés : {etats}). Ne pas rédiger dessus.")
    vivants.sort(key=lambda a: a.get("date_debut", ""), reverse=True)
    return vivants[0]


def chercher(code, motif, limite=40):
    """Cherche un motif dans les titres de section et les numéros."""
    index = charger(code)
    m = _sans_accent(motif)
    sortie = []
    for arts in index.values():
        for a in arts:
            if not applicable(a):
                continue
            if m in _sans_accent(a.get("section", "")) or m in _sans_accent(a.get("num", "")):
                sortie.append(a)
    sortie.sort(key=lambda a: (a.get("section", ""), a.get("num", "")))
    return sortie[:limite]


def rendre(a, avec_texte=True):
    """Le gabarit de l'étape 1 de redaction-legistique — jamais de texte nu."""
    mil, age, perime = fraicheur()
    lignes = [f"### Article {a['num']} [{a['code']}]",
              f"Version applicable depuis le {a.get('date_debut') or '[non porté]'}",
              f"Identifiant : {a['id']}   état LEGI : {a.get('etat', '?')}",
              f"Source : base LEGI, millésime {mil}"
              + (f" — extrait vieux de {age} j, À REJOUER" if perime else "")]
    if a.get("section"):
        lignes.append(f"Section : {a['section']}")
    # Un article dont la disparition est déjà votée ne se laisse pas amender en
    # silence : le rédacteur doit le savoir avant d'écrire, pas après le dépôt.
    if a.get("date_fin") not in FIN_OUVERTE:
        lignes.append(f"AVERTISSEMENT — cette version cesse de s'appliquer le "
                      f"{a['date_fin']} (état {a.get('etat', '?')}). "
                      "Vérifier ce que le texte devient à cette date avant de rédiger.")
    return "\n".join(lignes) + ("\n\n" + a["texte"] if avec_texte else "")


# --------------------------------------------------------------------------
# contrôle de lot


def verifier(adresses):
    """adresses : [{code, articles:[...]}] ou {code: [articles]}.
    Rend une ligne par adresse : trouvé / abrogé / absent."""
    if isinstance(adresses, dict):
        adresses = [{"code": k, "articles": v} for k, v in adresses.items()]
    lignes = []
    for bloc in adresses:
        for num in bloc.get("articles", []):
            try:
                a = article(bloc["code"], num)
                lignes.append((bloc["code"], str(num), "trouvé", a["id"], a.get("date_debut", "")))
            except LookupError as e:
                verdict = "absent" if "absent de l'extrait" in str(e) else "inapplicable"
                lignes.append((bloc["code"], str(num), verdict, "", ""))
            except (KeyError, FileNotFoundError) as e:
                lignes.append((bloc.get("code", "?"), str(num), "erreur", str(e)[:60], ""))
    return lignes


# --------------------------------------------------------------------------


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd = argv[1]

    if cmd == "etat":
        m = manifeste()
        mil, age, perime = fraicheur()
        print(f"millésime LEGI {mil}" + (f" — {age} j" if age is not None else "")
              + ("  PÉRIMÉ, rejouer l'action" if perime else "  frais"))
        for cle, info in m["codes"].items():
            print(f"  {cle:<46} {info.get('applicables', info['articles']):>6} appl.  "
                  f"{info.get('fin_programmee', 0):>5} à fin programmée  "
                  f"{info.get('a_venir', 0):>4} à venir  "
                  f"{info['octets']/1e6:>5.1f} Mo")
        return 0

    if cmd == "article" and len(argv) >= 4:
        print(rendre(article(argv[2], " ".join(argv[3:]))))
        return 0

    if cmd == "section" and len(argv) >= 4:
        for a in chercher(argv[2], " ".join(argv[3:])):
            print(f"{a['num']:<22} {a['id']}  {a.get('section','')[:90]}")
        return 0

    if cmd == "verifier" and len(argv) >= 3:
        charge = json.loads(pathlib.Path(argv[2]).read_text(encoding="utf-8"))
        for l in verifier(charge):
            print(f"{l[0]:<46} {l[1]:<20} {l[2]:<8} {l[3]:<22} {l[4]}")
        return 0

    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
