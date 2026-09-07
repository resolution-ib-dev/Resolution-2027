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
    python3 droit.py article cgi 279 --au 2025-06-01
    python3 droit.py section cgi "Taux réduit"
    python3 droit.py renvois cgi "200 quindecies"    # renvois entrants, tous codes
    python3 droit.py verifier vecteurs.json      # lot d'adresses à contrôler
    python3 droit.py etat

Emploi depuis un script :
    from droit import article, chercher, fraicheur, renvois
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
# renvois entrants


# Suffixes ordinaux portés par un numéro LEGI, du plus long au plus court —
# l'ordre compte : sans lui, l'alternative « ter » captait le début de
# « terdecies » et laissait « decies » de côté.
_SUFFIXES = tuple(sorted((
    "bis", "ter", "quater", "quinquies", "sexies", "septies", "octies", "nonies",
    "decies", "undecies", "duodecies", "terdecies", "quaterdecies", "quindecies",
    "sexdecies", "septdecies", "octodecies", "novodecies", "vicies", "er"),
    key=len, reverse=True))

RE_ARTICLE_KW = re.compile(r"\barticles?\b|\bart\.", re.IGNORECASE)

# Un numéro : préfixe de subdivision (L, R, D), corps numérique, suffixe
# ordinal, tirets de sous-numérotation, puis — seulement ici, jamais en
# ignorant la casse — une lettre de subdivision isolée. C'est cette dernière
# qui distingue « 200 quindecies » de « 200 quindecies A » : la lettre fait
# partie du numéro rendu, donc de sa forme normalisée, et les deux ne
# s'égalent plus jamais par accident.
RE_NUM_TOKEN = re.compile(
    r"(?:[LRDlrd]\.?\s*)?\d+(?:\s*(?:%s)\b)?(?:-\d+)*(?:\s+[A-Z]\b)?"
    % "|".join(f"(?i:{s})" for s in _SUFFIXES))

RE_SEPARATEUR = re.compile(r"\s*(?:,|;|\bet\b|\bou\b|\bà\b)\s*", re.IGNORECASE)

# Marqueurs d'un renvoi vers une subdivision précise de l'article cité : un
# chiffre romain de tête de subdivision, un degré, ou un ordinal en toutes
# lettres. Les romains restent sensibles à la casse — « il », « la » lus en
# insensible à la casse matcheraient comme chiffres romains autrement.
RE_ROMAIN = re.compile(r"\b(?:I|II|III|IV|V|VI|VII|VIII|IX|X)\b")
RE_DEGRE = re.compile(r"\b\d+°")
RE_ORDINAL_LETTRES = re.compile(
    r"\balin[ée]as?\b|\bpremier\b|\bdeuxi[èe]me\b|\btroisi[èe]me\b|\bquatri[èe]me\b",
    re.IGNORECASE)


def _citations(texte):
    """Rend, pour chaque « article(s) »/« art. » suivi d'au moins un numéro,
    (position du mot, [numéros bruts], position juste après la liste).

    Une énumération — « articles 33 ter et 33 quater » — ou un intervalle —
    « articles 156 à 168 » — rend chacun de ses numéros ; l'intervalle n'est
    pas déplié, seules ses bornes comptent comme numéros cités.
    """
    sorties = []
    for m in RE_ARTICLE_KW.finditer(texte):
        blanc = re.match(r"\s+", texte[m.end():])
        if not blanc:
            continue
        pos = m.end() + blanc.end()
        numeros = []
        while True:
            mt = RE_NUM_TOKEN.match(texte, pos)
            if not mt:
                break
            numeros.append(mt.group())
            pos = mt.end()
            sep = RE_SEPARATEUR.match(texte, pos)
            if not sep:
                break
            pos = sep.end()
        if numeros:
            sorties.append((m.start(), numeros, pos))
    return sorties


def _fenetre_apres(texte, pos, taille=100):
    """Le reste de la phrase courante, borné — c'est là qu'un nom de code se lit."""
    fin_phrase = texte.find(".", pos)
    limite = pos + taille if fin_phrase == -1 else min(pos + taille, fin_phrase + 1)
    return texte[pos:limite]


def _fenetre_avant(texte, pos, taille=60):
    """Le début de la phrase courante, borné — c'est là qu'une subdivision se lit."""
    debut_phrase = texte.rfind(".", max(0, pos - taille), pos)
    debut = debut_phrase + 1 if debut_phrase != -1 else max(0, pos - taille)
    return texte[debut:pos]


def _code_nomme(fenetre, cles_norm):
    """Rend le libellé du code nommé dans la fenêtre, ou None. Le plus long
    des libellés trouvés l'emporte, pour ne pas se faire couper par un nom
    de code plus court apparu par hasard dans la même fenêtre."""
    f = _sans_accent(fenetre)
    trouves = [cle for cle, n in cles_norm.items() if n in f]
    return max(trouves, key=len) if trouves else None


def _extrait(texte, pos, fin, avant=40, apres=60):
    """Le passage cité, sans jamais l'ouvrir ni le fermer au milieu d'un mot."""
    debut = max(0, pos - avant)
    if debut:
        espace = texte.find(" ", debut)
        if 0 <= espace < pos:
            debut = espace + 1
    limite = min(len(texte), fin + apres)
    if limite < len(texte):
        espace = texte.rfind(" ", fin, limite)
        if espace > fin:
            limite = espace
    return texte[debut:limite].strip()


def _interne(fenetre_avant):
    return bool(RE_ROMAIN.search(fenetre_avant) or RE_DEGRE.search(fenetre_avant)
                or RE_ORDINAL_LETTRES.search(fenetre_avant))


def renvois(code, num, limite=200):
    """Rend les renvois entrants vers l'article `num` de `code`, tous les
    codes portés balayés. Chaque renvoi : {code, num, subdivision, extrait,
    certitude}.

    La certitude se lit sur une règle, jamais sur une proximité :
      - `nomme`   — le code cité est nommé et c'est celui de la cible, ou
                     l'article citant appartient lui-même au code de la
                     cible (l'identité du code ne fait alors aucun doute) ;
      - `interne` — aucun code n'est identifiable, mais le renvoi vise une
                     subdivision précise de l'article (chiffre romain, degré,
                     alinéa) — trop spécifique pour être fortuit ;
      - `ambigu`  — le numéro est trouvé seul, sans code ni subdivision.
    Une citation qui nomme EXPLICITEMENT un autre code que la cible est
    écartée : ce n'est pas un renvoi vers l'article demandé, quel que soit le
    numéro qui coïncide. L'article cible s'exclut de ses propres renvois, et
    seule la version aujourd'hui applicable d'un article citant est retenue.
    """
    cfg = resoudre_code(code)
    cible = article(code, num)
    cible_cle = cfg["cle"]
    cible_num = norm_num(cible["num"])
    cles_norm = {c["cle"]: _sans_accent(c["cle"]) for c in _cfg()}

    sorties = []
    for c in _cfg():
        try:
            index = charger(c["court"])
        except FileNotFoundError:
            continue
        for arts in index.values():
            # Une seule version par numéro — la même que rendrait `article()` —
            # jamais une par version historique : sans quoi un article qui
            # chevauche brièvement sa propre nouvelle version citerait deux
            # fois la cible pour un seul renvoi réel.
            candidats = [a for a in arts if applicable(a)]
            if not candidats:
                continue
            a = max(candidats, key=lambda x: x.get("date_debut", ""))
            if a["id"] == cible["id"]:
                continue
            trouve = None
            for pos, numeros, fin in _citations(a["texte"]):
                if any(norm_num(n) == cible_num for n in numeros):
                    trouve = (pos, fin)
                    break
            if not trouve:
                continue
            pos, fin = trouve
            autre = _code_nomme(_fenetre_apres(a["texte"], fin), cles_norm)
            if autre and autre != cible_cle:
                continue
            if autre == cible_cle or c["cle"] == cible_cle:
                certitude = "nomme"
            elif _interne(_fenetre_avant(a["texte"], pos)):
                certitude = "interne"
            else:
                certitude = "ambigu"
            sorties.append({
                "code": c["cle"], "num": a["num"],
                "subdivision": a.get("section", ""),
                "extrait": _extrait(a["texte"], pos, fin),
                "certitude": certitude,
            })
    ordre = {"nomme": 0, "interne": 1, "ambigu": 2}
    sorties.sort(key=lambda r: (ordre[r["certitude"]], r["code"], r["num"]))
    return sorties[:limite]


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
            # KeyError est une sous-classe de LookupError : capturée en second,
            # elle ressortait en « inapplicable » — un code non porté passait
            # pour un article périmé. L'ordre compte.
            except (KeyError, FileNotFoundError) as e:
                lignes.append((bloc.get("code", "?"), str(num), "code absent", str(e)[:48], ""))
            except LookupError as e:
                verdict = "absent" if "absent de l'extrait" in str(e) else "inapplicable"
                lignes.append((bloc["code"], str(num), verdict, "", ""))
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
        reste = argv[3:]
        jour = None
        if "--au" in reste:
            i = reste.index("--au")
            if i + 1 >= len(reste):
                sys.exit("--au attend une date AAAA-MM-JJ.")
            jour = reste[i + 1]
            reste = reste[:i] + reste[i + 2:]
        print(rendre(article(argv[2], " ".join(reste), jour=jour)))
        return 0

    if cmd == "section" and len(argv) >= 4:
        for a in chercher(argv[2], " ".join(argv[3:])):
            print(f"{a['num']:<22} {a['id']}  {a.get('section','')[:90]}")
        return 0

    if cmd == "renvois" and len(argv) >= 4:
        for r in renvois(argv[2], " ".join(argv[3:])):
            print(f"{r['code']:<46} {r['num']:<18} {r['certitude']:<8} "
                  f"{r['subdivision'][:40]:<40} {r['extrait'][:90]}")
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
