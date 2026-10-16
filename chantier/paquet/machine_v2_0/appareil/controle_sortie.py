#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""controle_sortie.py — passe de contrôle à la sortie des skills.

Le contrôle structurel vérifie le référentiel. Le contrôle arithmétique vérifie
ses bouclages. Celui-ci vérifie ce qui sort d'une skill : tout nombre du
livrable se retrouve au REF, avec son statut, et n'a franchi aucune des cinq
règles d'émission du contrat de projection.

Usage :
    python3 controle_sortie.py <livrable> <REF_doctrine.json> [--appareil]

Formats lus : txt, md, html. Sur docx, xlsx, pdf, png le script refuse et le
dit : les contrôles se conduisent alors à la lecture.

Sorties : 0 si aucun échec, 1 sinon.
"""

import json
import re
import sys
import html as _html
import unicodedata

# --------------------------------------------------------------------------
# Nomenclatures fermées du schéma v18
# --------------------------------------------------------------------------

STATUTS_DIFFUSABLES = {"manuscrit", "implicite au manuscrit", "classeur"}
STATUT_RESERVE = "absent des deux"
STATUT_A_DECLARER = "classeur"
NATURE_ILLUSTRATION = "illustration"
VERDICTS_A_DECLARER = ("NON INSTRUIT", "À QUALIFIER")

# Marques admises pour la déclaration d'un statut classeur dans le livrable.
MARQUES_CLASSEUR = (
    "classeur", "décompte", "decompte", "recensement",
    "tableau de référence", "tableau de reference",
)

# Marques admises pour qu'une illustration nomme son cas.
MARQUES_ILLUSTRATION = (
    "par exemple", "exemple", "cas", "illustration", "à titre",
    "a titre", "ainsi", "soit un", "pour un",
)

FORMATS_NON_LUS = (".docx", ".xlsx", ".xls", ".pdf", ".png", ".jpg", ".pptx")

# --------------------------------------------------------------------------
# Lecture du REF
# --------------------------------------------------------------------------


def parcourir(o):
    """Rend tous les dictionnaires du REF, à toute profondeur."""
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from parcourir(v)
    elif isinstance(o, list):
        for x in o:
            yield from parcourir(x)


def normaliser_nombre(t):
    """Rend la forme canonique d'un nombre écrit : '20 000' -> '20000',
    '236,1' -> '236.1'. Rend None si le jeton n'est pas un nombre."""
    t = unicodedata.normalize("NFKC", t)
    t = t.replace("\u202f", "").replace("\u00a0", "").replace("\u2009", "").replace(" ", "")
    t = t.replace("\u2212", "-").replace("−", "-")
    t = t.replace(",", ".")
    if re.fullmatch(r"-?\d+(\.\d+)?", t):
        return t.rstrip("0").rstrip(".") if "." in t else t
    return None


RE_NOMBRE = re.compile(
    r"-?\d{1,3}(?:[\u202f\u00a0\u2009 ]\d{3})+(?:[.,]\d+)?"  # séparateur de milliers
    r"|-?\d+(?:[.,]\d+)?"                                    # forme simple
)


RE_IDENT = re.compile(r"[A-Za-zÀ-ÿ]-?$")


def est_identifiant(texte, debut):
    """Vrai quand le nombre prolonge un identifiant : M-0501, D9-2, RT-1."""
    return RE_IDENT.search(texte[max(0, debut - 3):debut]) is not None


def nombres_de(texte):
    """Rend l'ensemble des formes canoniques des nombres d'un texte,
    les fragments d'identifiant écartés."""
    out = set()
    for m in RE_NOMBRE.finditer(texte):
        if est_identifiant(texte, m.start()):
            continue
        n = normaliser_nombre(m.group(0))
        if n is not None:
            out.add(n)
    return out


def charger_ref(chemin):
    """Rend l'index : forme canonique de nombre -> liste d'entrées."""
    d = json.load(open(chemin, encoding="utf-8"))
    index = {}
    entrees = []
    for o in parcourir(d):
        ident = o.get("id")
        if not isinstance(ident, str):
            continue
        if "statut_ancre" not in o:
            continue
        entree = {
            "id": ident,
            "statut_ancre": o.get("statut_ancre", ""),
            "source_ancre": o.get("source_ancre", ""),
            "nature": o.get("nature", ""),
            "verdict": o.get("verdict", ""),
            "conditions": o.get("conditions", ""),
            "base": o.get("base", ""),
            "portee": o.get("portee", ""),
            "sens": o.get("sens", ""),
            "origine": o.get("origine", ""),
            "operation": o.get("operation", ""),
            "chaine": o.get("chaine", ""),
            "exact": o.get("exact", ""),
            "affiche": o.get("valeur", o.get("chiffre", o.get("enonce", ""))),
        }
        entrees.append(entree)
        champs = " | ".join(
            aplatir(o.get(k, "")) for k in ("valeur", "chiffre", "exact", "nom", "enonce", "bornes")
        )
        for n in nombres_de(champs):
            index.setdefault(n, []).append(entree)

        # Composants de chaîne. Un sous-chiffre nommé dans la chaîne d'une entrée
        # relève du contrôle interne au même titre que l'entrée : il est tracé au
        # corpus, par un nœud ou par une cellule de classeur.
        for c in o.get("chaine", []) or []:
            if not isinstance(c, dict) or "composant" not in c:
                continue
            origine = aplatir(c.get("origine", ""))
            composant = {
                "id": "%s ← %s" % (ident, c.get("composant", "")),
                "statut_ancre": "classeur" if "classeur" in origine.lower() else entree["statut_ancre"],
                "source_ancre": "",
                "nature": entree["nature"],
                "verdict": aplatir(c.get("statut", "")).upper(),
                "conditions": "",
                "base": aplatir(c.get("base", "")),
                "portee": entree["portee"],
                "sens": "",
                "origine": origine,
                "operation": "",
                "chaine": "",
                "exact": "",
                "affiche": aplatir(c.get("valeur", "")),
                "composant": True,
            }
            entrees.append(composant)
            for n in nombres_de(aplatir(c.get("valeur", ""))):
                index.setdefault(n, []).append(composant)
    return d, index, entrees


# --------------------------------------------------------------------------
# Lecture du livrable
# --------------------------------------------------------------------------


def lire_livrable(chemin):
    bas = chemin.lower()
    for ext in FORMATS_NON_LUS:
        if bas.endswith(ext):
            return None
    t = open(chemin, encoding="utf-8", errors="replace").read()
    if bas.endswith(".html") or bas.endswith(".htm"):
        t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S | re.I)
        t = re.sub(r"<[^>]+>", " ", t)
        t = _html.unescape(t)
    return t


def contextes(texte, brut):
    """Rend les fenêtres de texte autour de chaque occurrence d'un nombre."""
    out = []
    for m in re.finditer(re.escape(brut), texte):
        a = max(0, m.start() - 240)
        b = min(len(texte), m.end() + 240)
        out.append(texte[a:b].lower())
    return out


# Unités du corpus. Un nombre entre dans le champ du contrôle quand il en porte
# une : les autres nombres d'un livrable sont des dates, des références, des
# effectifs externes ou des identifiants, et relèvent du contrôle des sources.
RE_UNITE = re.compile(
    r"\s*(?:"
    r"Md\s*€|M\s*€|milliards?|millions?|€|%|pts?\b|points?\b|ETP\b"
    r"|emplois?\b|postes?\b|agents?\b|agences?\b|op[ée]rateurs?\b"
    r"|[ée]tablissements?\b|organismes?\b|imp[ôo]ts?\b|taxes?\b"
    r"|foyers?\b|m[ée]nages?\b|personnes?\b|habitants?\b"
    r"|retrait[ée]s?\b|travailleurs?\b|actifs?\b|salari[ée]s?\b"
    r"|ans?\b|mois\b|ann[ée]es?\b"
    r")",
    re.I,
)

RE_ANNEE = re.compile(r"^(19|20)\d\d$")


def porte_une_unite(texte, fin):
    """Vrai quand une unité du corpus suit immédiatement le nombre."""
    return RE_UNITE.match(texte, fin) is not None


def occurrences(texte):
    """Rend forme canonique -> liste des écritures brutes rencontrées.

    Le champ du contrôle est celui des grandeurs : un nombre y entre quand il
    porte une unité du corpus et qu'il ne s'écrit pas comme un millésime."""
    out = {}
    for m in RE_NOMBRE.finditer(texte):
        brut = m.group(0)
        n = normaliser_nombre(brut)
        if n is None:
            continue
        if RE_ANNEE.match(n):
            continue
        if not porte_une_unite(texte, m.end()):
            continue
        out.setdefault(n, set()).add(brut)
    return out


# --------------------------------------------------------------------------
# Les cinq règles d'émission
# --------------------------------------------------------------------------


def presente(fenetres, marques):
    return any(any(mq in f for mq in marques) for f in fenetres)


def mots_significatifs(t, seuil=6):
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return {w for w in re.findall(r"[a-z]{%d,}" % seuil, t)}


def aplatir(v):
    """Rend une chaîne, que le champ porte un texte ou une liste."""
    if isinstance(v, list):
        return " · ".join(aplatir(x) for x in v)
    if isinstance(v, dict):
        return " · ".join(aplatir(x) for x in v.values())
    return "" if v is None else str(v)


def controler_entree(entree, fenetres, cle=None, approx=False):
    """Rend la liste des règles franchies, sous forme (numéro, libellé)."""
    manques = []
    statut = aplatir(entree["statut_ancre"]).strip()
    nature = aplatir(entree["nature"]).strip()
    verdict = aplatir(entree["verdict"]).strip()

    # R1 — diffusabilité
    if statut == STATUT_RESERVE:
        manques.append((1, "statut « absent des deux », valeur réservée au registre interne"))

    # R2 — déclaration du statut classeur
    if statut == STATUT_A_DECLARER and not presente(fenetres, MARQUES_CLASSEUR):
        manques.append((2, "statut classeur employé sans sa déclaration"))

    # R3 — rang de l'illustration
    if nature == NATURE_ILLUSTRATION and not presente(fenetres, MARQUES_ILLUSTRATION):
        manques.append((3, "illustration employée sans que son cas soit nommé"))

    # R4 — conditions littérales
    cond = aplatir(entree["conditions"]).strip()
    if cond:
        cles = mots_significatifs(cond)
        if cles:
            vus = set()
            for f in fenetres:
                vus |= mots_significatifs(f)
            if not (cles & vus):
                manques.append((4, "conditions littérales absentes du voisinage de la valeur"))

    # R5 — forme de l'ancre. Un composant de chaîne n'est pas une ancre : la
    # règle porte sur la valeur affichée d'une entrée, non sur ses composants.
    #
    # Arrondi non conforme. En contrôle interne, l'ancre fixe la forme : une
    # écriture voisine de la grandeur, qui ne reprend ni l'ancre ni l'exact, est
    # un arrondi que le corpus ne porte pas. En compatibilité externe le même
    # écart est admis, l'enjeu y étant l'ordre de grandeur et non la forme.
    if statut == "manuscrit" and not entree.get("composant"):
        exact = normaliser_nombre(aplatir(entree["exact"])) if entree["exact"] else None
        affiche = normaliser_nombre(aplatir(entree["affiche"])) if entree["affiche"] else None
        # règle éprouvée seulement quand les deux formes diffèrent
        if exact and affiche and exact != affiche:
            trouve_affiche = any(affiche in "".join(nombres_de(f)) for f in fenetres)
            if not trouve_affiche:
                manques.append((5, "exact employé là où l'ancre du manuscrit s'énonce"))

    # signalement complémentaire, non bloquant
    alertes = []
    if any(v in verdict for v in VERDICTS_A_DECLARER):
        alertes.append("verdict %s, à donner comme tel" % verdict)
    return manques, alertes


# --------------------------------------------------------------------------
# Dérivation — un chiffre absent du référentiel mais reconstructible
# --------------------------------------------------------------------------

TOLERANCE = 0.001  # 0,1 % en écart relatif
ECHELLES = (12, 100, 1000)


def proche(a, b):
    if b == 0:
        return abs(a) < 1e-12
    return abs(a - b) / abs(b) <= TOLERANCE


def formes_affichables(entree):
    """Rend les formes canoniques sous lesquelles l'entrée s'énonce.

    L'ancre et l'exact sont les deux seules formes admises : la première pour
    l'énoncé, la seconde pour l'appui. Toute autre écriture de la grandeur est
    un arrondi que le corpus ne porte pas."""
    formes = set()
    for champ in ("affiche", "exact"):
        formes |= nombres_de(aplatir(entree.get(champ, "")))
    return formes


def approcher(cle, index):
    """Rend les entrées dont la valeur approche la clé, à la tolérance près.

    Une ancre de communication s'écrit arrondie. Le rapprochement exact la
    manquerait, et la dérivation la reconstruirait par une opération fortuite."""
    try:
        x = float(cle)
    except ValueError:
        return None
    for autre, entrees in index.items():
        try:
            y = float(autre)
        except ValueError:
            continue
        if y and proche(abs(x), abs(y)):
            return entrees
    return None


def deriver(x, valeurs):
    """Cherche une opération nommable qui produit x depuis le référentiel.

    La recherche est volontairement étroite. Un quotient libre entre deux
    valeurs quelconques couvre presque tous les nombres : il reconnaîtrait
    n'importe quoi. Quatre formes seulement sont admises, chacune correspondant
    à une opération que le corpus pratique.

    1. changement d'échelle — mois vers année, unité vers millier, taux
    2. produit par un coefficient du référentiel, valeur inférieure à dix
    3. somme de deux valeurs de même ordre de grandeur
    4. différence de deux valeurs de même ordre de grandeur

    Rend le libellé de l'opération, ou None."""
    if not x:
        return None
    ax = abs(x)

    # Le changement d'échelle se lit sur une grandeur, non sur un petit entier :
    # neuf multiplié par mille reconnaîtrait n'importe quel millier.
    for v in valeurs:
        if abs(v) < 10:
            continue
        for f in ECHELLES:
            if proche(ax, abs(v) * f):
                return "%g × %d" % (v, f)
            if proche(ax, abs(v) / f):
                return "%g ÷ %d" % (v, f)

    # Un coefficient s'écrit court. Trois décimales significatives ne sont pas
    # un coefficient, ce sont deux nombres qui se rencontrent.
    def coefficient_court(v):
        return abs(round(v, 2) - v) < 1e-9

    coefficients = [v for v in valeurs if 0 < abs(v) < 10 and coefficient_court(v)]
    grandeurs = [v for v in valeurs if abs(v) >= 10]
    for v in grandeurs:
        for k in coefficients:
            if proche(ax, abs(v) * k):
                return "%g × %g" % (v, k)

    vs = sorted(abs(v) for v in valeurs if abs(v) > 0)
    for i, a in enumerate(vs):
        for b in vs[i:]:
            if b > a * 20:
                break
            if proche(ax, a + b):
                return "%g + %g" % (a, b)
            if proche(ax, b - a):
                return "%g − %g" % (b, a)
    return None


# --------------------------------------------------------------------------
# Rapport
# --------------------------------------------------------------------------


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    chemin_livrable, chemin_ref = argv[1], argv[2]
    appareil = "--appareil" in argv

    texte = lire_livrable(chemin_livrable)
    if texte is None:
        print("FORMAT NON LU — %s" % chemin_livrable)
        print("Les contrôles se conduisent à la lecture, et le rapport le")
        print("mentionne en tête. Convertir en texte pour la passe mécanique.")
        return 2

    _, index, entrees = charger_ref(chemin_ref)
    occ = occurrences(texte)

    echecs, alertes, realistes, ok = [], [], [], []
    valeurs_ref = []
    for cle in index:
        try:
            valeurs_ref.append(float(cle))
        except ValueError:
            pass
    valeurs_ref = sorted(set(v for v in valeurs_ref if 0 < abs(v) < 1e9))

    for n, bruts in sorted(occ.items(), key=lambda kv: -len(kv[0])):
        # les entiers courts sont du numérotage, non des grandeurs
        if re.fullmatch(r"-?\d{1,2}", n):
            continue
        cands = index.get(n)
        brut = sorted(bruts, key=len, reverse=True)[0]
        approx = False
        if not cands:
            # la valeur approche une entrée sans en reprendre la forme
            cands = approcher(n, index)
            approx = bool(cands)
        if not cands:
            try:
                x = float(n)
            except ValueError:
                x = None
            op = deriver(x, valeurs_ref) if x is not None else None
            if op:
                realistes.append((brut, op))
            else:
                alertes.append((brut, "aucune entrée ni composant de chaîne ne porte cette valeur"))
            continue
        fen = []
        for b in bruts:
            fen += contextes(texte, b)
        # une entrée suffit à couvrir l'occurrence : retenir la moins en défaut
        bilans = [(e,) + controler_entree(e, fen, n, approx) for e in cands]
        bilans.sort(key=lambda t: len(t[1]))
        e, manques, alrt = bilans[0]
        if manques:
            for num, lib in manques:
                echecs.append((brut, e["id"], num, lib))
        else:
            marque = "composant" if e.get("composant") else "entrée"
            ok.append((brut, e["id"], aplatir(e["statut_ancre"]), marque, aplatir(e["verdict"]) or "—"))
        for a in alrt:
            alertes.append((brut, "%s — %s" % (e["id"], a)))

    print("CONTRÔLE À LA SORTIE — %s" % chemin_livrable)
    print("%d échec(s) · %d à instruire · %d réaliste(s) · %d tenu(s)"
          % (len(echecs), len(alertes), len(realistes), len(ok)))
    print("")

    if echecs:
        print("ÉCHECS — le livrable ne sort pas")
        for brut, ident, num, lib in echecs:
            print("  R%d  %-14s %-16s %s" % (num, brut, ident, lib))
        print("")

    if alertes:
        print("À INSTRUIRE — compatibilité externe, ancrage à créer")
        for brut, lib in alertes:
            print("  %s" % brut)
        print("")

    # Bas de page. Ce qui tient ne perturbe pas la lecture du rapport.
    if realistes or (appareil and ok):
        print("—" * 60)
    if realistes:
        print("Réalistes — reconstructibles depuis le référentiel, à verser")
        for brut, op in realistes:
            print("  %-14s %s" % (brut, op))
        print("")
    if appareil and ok:
        print("Appareil — chiffres tenus")
        for brut, ident, statut, marque, verdict in ok:
            print("  %-14s %-34s %-12s %-12s %s" % (brut, ident, statut, marque, verdict))
        print("")

    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
