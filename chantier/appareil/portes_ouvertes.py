#!/usr/bin/env python3
"""Portes ouvertes par un texte financier — relevé mécanique depuis le socle.

Une porte ouverte est un couple (texte, article) que la disposition du véhicule
modifie elle-même. L'exposé des motifs n'en ouvre aucune : il est de l'indice,
jamais de la porte.

Grammaire de relevé — les sept règles du millésime 2027 :
 1. le repère de page est le folio imprimé, porté par le socle ;
 2-5. la répartition en mesures est l'affaire de l'index, pas de ce relevé ;
 6. les passages entre guillemets sont blanchis avant toute détection de siège,
    le blanchiment traverse les lignes et les offsets sont préservés ;
 7. le contexte de pièce se porte le long de l'article et ne se met à jour que
    sur une formule de modification.

Sortie : `articles_ouverts_<vehicule><millesime>.tsv`, une ligne par couple
(texte, article) ouvert.
"""
import json, re, sys
import pieces_nommees

# --- numéros d'alinéa du texte enregistré -----------------------------------
# « (12) » en tête de ligne au PLF, un glyphe de police privée au PLFSS. Blanchis
# à longueur égale, les offsets restent justes ; sans quoi « (20) » suivant le
# nom d'un code se lisait comme un article. Sans effet sur un autre tirage.
ALINEA = re.compile(r"(?m)^[ \t]*(?:\(\d+\)|[\ue000-\uf8ff]+)(?=[ \t])")

# --- règle 6 : blanchiment des passages cités -------------------------------
PAIRES = [("«", "»"), ("“", "”")]


def blanchir(t):
    """Règle 6 — les passages cités sont blanchis avant toute détection, le
    blanchiment traverse les lignes et les offsets sont préservés.

    Le guillemet français NE S'IMBRIQUE PAS en légistique : chaque alinéa inséré
    rouvre un « sans que le précédent soit fermé, et un seul » referme le bloc.
    Compter la profondeur blanchissait tout le reste de l'article — l'article 19
    du PLF 2027 tombait de 11 669 à 492 octets utiles, et ses 30 sièges avec.
    Un « jamais refermé ne blanchit que jusqu'à la fin de sa ligne.
    """
    out = list(t)
    for ouv, fer in PAIRES:
        i = 0
        while True:
            d = t.find(ouv, i)
            if d < 0:
                break
            f = t.find(fer, d + 1)
            if f < 0:
                f = t.find("\n", d + 1)
                f = len(t) - 1 if f < 0 else f - 1
            for j in range(d, f + 1):
                if out[j] != "\n":
                    out[j] = " "
            i = f + 1
    return "".join(out)


# --- règle 7 : le contexte de pièce ------------------------------------------
# Grammaire élargie le 20261016 : elle tronquait les adresses longues, que la
# frontière de mot rejetait ensuite sans les faire entrer. Trois manques.
#  - le suffixe latin : l'alternative prenait « ter » avant « terdecies », et
#    « 199 terdecies-0 » se lisait « 199 ter ». Les composés passent devant, et
#    le « -0 » qui suit un suffixe se lit avec lui ;
#  - la lettre de rang : une seule était lue, « 235 ter XB » se lisait
#    « 235 ter X ». Jusqu'à trois capitales, à condition qu'aucune lettre ni
#    chiffre ne suive — « article 4 Les » reste « 4 » ;
#  - l'ordinal : « article 1er » se lisait « 1 », et partait au mauvais texte.
LATIN = (r"(?:vicies|novodecies|octodecies|septdecies|sexdecies|quindecies"
         r"|quaterdecies|terdecies|duodecies|undecies|decies|nonies|octies"
         r"|septies|sexies|quinquies|quater|ter|bis)(?![\w])")
RANG = r"[A-Z]{1,3}(?![\w])"

ADRESSE = re.compile(
    r"\b(?:articles?|art\.)\s+"
    r"(?P<a>[LRD]\.?\s?\d+(?:[\-‑]\d+)*(?:\s" + LATIN + r")?"
    r"|1er(?![\w])"
    r"|\d+(?:[\-‑]\d+)*(?:\s?(?:-0)?\s?" + RANG + r"(?:\s" + LATIN + r")?)?"
    r"(?:\s" + LATIN + r"(?:-0)?(?![\w\-])(?:\s" + RANG + r")?)?"
    r"(?:\s" + RANG + r")?)")

SUITE = re.compile(
    r"\s*(?:,|\set\s|\sou\s)\s*"
    r"(?P<a>[LRD]\.?\s?\d+(?:[\-‑]\d+)*(?:\s(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies|terdecies|quaterdecies|quindecies|sexdecies|septdecies))?)"
    r"(?![\w\-])")

# Ce qui ne peut pas suivre une adresse entière.
FRONTIERE = re.compile(r"[\w\-‑]")

INSERTION = re.compile(
    r"(?:après|avant|au même|du même|à la fin du|mentionnés? (?:à|au)|"
    r"mentionnées? (?:à|au)|prévus? (?:à|au)|prévues? (?:à|au)|"
    r"défini(?:e|s|es)? (?:à|au)|visés? (?:à|au)|dans les conditions prévues (?:à|au))"
    r"\s+(?:l[’']|le |la |les )?(?:articles?|art\.)?\s*$", re.I)

MODIF = re.compile(
    r"est ainsi modifié|sont ainsi modifié|est ainsi rédigé|sont ainsi rédigé"
    r"|est abrogé|sont abrogé|est remplacé|sont remplacé|il est inséré|sont insérés"
    r"|est complété|sont complétés|est ainsi rétabli|est supprimé|sont supprimés", re.I)


def normalise(a):
    a = " ".join(a.split())
    a = re.sub(r"^([LRD])\.?\s*", r"\1. ", a)
    return a.replace("‑", "-")


# --- les cellules de tableau coupées en fin de ligne ---------------------------
# Règle ajoutée le 20261016. Dans un tableau du texte enregistré — l'état des
# taxes affectées de l'article 42 du PLF 2027 —, une adresse se coupe au tiret en
# fin de cellule, et sa suite est une ou deux lignes plus bas, à la même colonne :
# « (création) et art. L. 116- », puis « 1, 6° du code du cinéma ». Lue telle
# quelle, la ligne donnait « L. 116 », que la frontière rejette.
#
# L'adresse se recompose à part, sur le texte brut, et **le texte du dispositif
# n'est pas réécrit** : le réécrire déplaçait les pièces des autres rangées et
# changeait leur rattachement. Sa pièce se lit dans la seule suite de la
# cellule — ses lignes à la même colonne, jusqu'au premier blanc — et doit lui
# être accolée. À défaut elle sort `indéterminé`, jamais sous la pièce
# précédente, qui est celle d'une autre rangée ; un nom de pièce coupé entre
# deux colonnes (« code du cinéma » sans « et de l'image animée ») n'est pas
# reconnu, et c'est voulu.
COUPEE = re.compile(r"\b(?:articles?|art\.)\s+"
                    r"(?P<a>[LRD]\.\s?\d+(?:[\-‑]\d+)*[\-‑])(?=\s{2,}|\s*$)")
SUITE_CELLULE = re.compile(r"\d+(?:[\-‑]\d+)*\b")
NOUVELLE_RANGEE = re.compile(r"^\s{0,4}\d{1,3}\s{2,}\S")
ACCOLEE = re.compile(r"\s*(?:,\s*\d+°\s*)?"
                     r"(?:(?:,|\s+et)\s+L\.\s?\d+(?:[\-‑]\d+)*\s*)*"
                     r"(?:du|de\s+la|de\s+l[’'])\s*$")

# Dans la prose, la même coupure — « l'article L. 286- » en fin de ligne, « 5 »
# en tête de la suivante — se recolle dans le texte même : seul le blanc entre
# le tiret et le chiffre s'ôte, et aucune pièce ne change de place.
COUPURE_PROSE = re.compile(r"(?<=\b[LRD]\.\s\d)(\d*(?:[\-‑]\d+)*[\-‑]) (?=\d)")


def _fragment(s, c):
    """Le texte de la cellule qui commence à la colonne `c`, ou None."""
    if len(s) <= c or s[c] == " " or (c and s[c - 1] != " "):
        return None
    g = re.search(r"\s{2,}", s[c:])
    return s[c:c + (g.start() if g else len(s) - c)]


def recollees(texte):
    """Les adresses coupées en fin de cellule : [(adresse, pièce accolée)]."""
    lignes = texte.split("\n")
    out = []
    for i, l in enumerate(lignes):
        for m in COUPEE.finditer(l):
            if INSERTION.search(l[max(0, m.start() - 60):m.start()]):
                continue
            ecart = [g.end() for g in re.finditer(r"\s{2,}", l[:m.start()])]
            c = ecart[-1] if ecart else len(l) - len(l.lstrip())
            for j in range(i + 1, min(i + 4, len(lignes))):
                if NOUVELLE_RANGEE.match(lignes[j]) and j > i + 1:
                    break
                f = _fragment(lignes[j], c)
                if f is None:
                    continue
                n = SUITE_CELLULE.match(f)
                if not n:
                    break
                morceaux = []
                for k in range(j, min(j + 3, len(lignes))):
                    f = _fragment(lignes[k], c)
                    if f is None:
                        break
                    morceaux.append(f)
                suite = " ".join(" ".join(morceaux).split())
                adresse = normalise(m.group("a") + n.group(0))
                reste = suite[n.end():]
                piece = next((nom for s, e, nom in pieces_nommees.trouver(reste)
                              if ACCOLEE.match(reste[:s])), None)
                out.append((adresse, piece or "indéterminé"))
                break
    return out


def portes(socle):
    lignes = {}
    for art in socle["articles"]:
        brut = blanchir(ALINEA.sub(lambda m: " " * len(m.group(0)), art["dispositif"]))
        d = brut
        # Le texte enregistré coupe les noms de pièce et les tournures « de la loi »
        # en fin de ligne. Une fois les citations blanchies, les blancs se
        # ramènent à un seul : les positions ne servent qu'à ordonner, entre elles.
        d = re.sub(r"\s+", " ", d)
        d = COUPURE_PROSE.sub(r"\1", d)
        if not MODIF.search(d):
            continue
        pieces = pieces_nommees.trouver(d)
        adrs = []
        for m in ADRESSE.finditer(d):
            # Règle ajoutée le 20261002. Un article cité comme POINT D'INSERTION
            # — « après l'article X, il est inséré… », « mentionné à l'article X »
            # — n'est pas modifié : il sert de repère. L'ancienne règle le
            # comptait ouvert, et deux sièges faux ont voyagé jusqu'à la
            # rédaction.
            if INSERTION.search(d[max(0, m.start() - 60):m.start()]):
                continue
            # Règle ajoutée le 20261016 — frontière de mot. Une capture que suit
            # une lettre, un chiffre ou un tiret est le préfixe d'une adresse
            # plus longue que la grammaire n'a pas su lire : « 235 ter X » dans
            # « 235 ter XB », « L. 116 » dans « L. 116- 1 ». La table la donnait
            # ouverte — seize lignes fausses sur le PLF 2027. Elle se rejette.
            if FRONTIERE.match(d, m.end("a")):
                continue
            adrs.append((m.start(), normalise(m.group("a")), m.end()))
            # énumération : « les articles L. 1, L. 2 et L. 3 » — les suivants
            # n'ont pas de mot « article » devant eux et seraient perdus.
            q = m.end()
            while True:
                s = SUITE.match(d, q)
                if not s:
                    break
                adrs.append((s.start("a"), normalise(s.group("a")), s.end("a")))
                q = s.end()
        # règle 7 — le contexte de pièce se porte le long de l'article. La pièce
        # d'une adresse est celle que la même phrase nomme après elle (« l'article
        # L. 1 du code X »), à défaut la dernière pièce déclarée avant elle.
        for pos, a, fin_adr in adrs:
            # Règle corrigée le 20261002. La pièce d'une adresse est celle que la
            # tournure « l'article X DU code Y » accole immédiatement après elle.
            # L'ancienne règle prenait la pièce suivante dans la phrase, si loin
            # fût-elle : « L. 136-8 du code de la sécurité sociale » sortait sous
            # le code général des impôts dès que la phrase le nommait plus loin.
            # Le 20261005 : « de » et « la » peuvent être séparés par un retour à
            # la ligne (texte enregistré).
            accolee = next((n for s, e, n in pieces
                            if fin_adr <= s <= fin_adr + 40
                            and re.match(r"\s*(?:,\s*\d+°\s*)?(?:du|de\s+la|de\s+l[’'])\s*$", d[fin_adr:s])), None)
            fin_phrase = d.find(".", pos)
            fin_phrase = len(d) if fin_phrase < 0 else fin_phrase
            suivante = next((n for s, e, n in pieces if pos < s < fin_phrase), None)
            precedente = next((n for s, e, n in reversed(pieces) if s < pos), None)
            contexte = accolee or precedente or suivante or "indéterminé"
            cle = (contexte, a)
            e = lignes.setdefault(cle, {"articles": set(), "pages": set()})
            e["articles"].add(art["numero"])
            e["pages"].add(art["folio_debut"])
        vus = {a for _, a, _ in adrs}
        # Sur le texte blanchi, lignes gardées : une cellule citée entre
        # guillemets est du texte inséré, et n'ouvre rien.
        cellules = recollees(brut)
        rattachees = {a for a, c in cellules if c != "indéterminé"}
        for a, contexte in cellules:
            if contexte == "indéterminé" and (a in vus or a in rattachees):
                continue
            e = lignes.setdefault((contexte, a), {"articles": set(), "pages": set()})
            e["articles"].add(art["numero"])
            e["pages"].add(art["folio_debut"])
    return lignes


def rendre(socle, vehicule, millesime, dest):
    lignes = portes(socle)
    def tri(n):
        return (0, int(n)) if n.isdigit() else (1, n)
    cles = sorted(lignes, key=lambda c: (c[0], c[1]))
    textes = {c[0] for c in cles}
    with open(dest, "w", encoding="utf-8") as f:
        f.write(f"# ARTICLES OUVERTS PAR LE TEXTE DÉPOSÉ — {vehicule.upper()} {millesime}\n")
        f.write("# Un vecteur dont le couple (texte, article) figure ici est `article_ouvert`,\n"
                "# `absolu` ailleurs.\n"
                "# Jointure sur le libellé exact, jamais au plus proche.\n"
                "# Ouvert = modifié par la disposition, jamais cité. L'exposé des motifs ne\n"
                "# compte pas : il est de l'indice, pas de la norme.\n")
        f.write(f"# pièce : sha256 {socle['pdf_sha256']}\n")
        f.write(f"# {len(cles)} adresses · {len(textes)} textes · relevé au folio imprimé\n")
        f.write(f"# colonnes : texte<TAB>article<TAB>subdivision<TAB>fourchette"
                f"<TAB>article_selon_ref_norme<TAB>divergence<TAB>articles_{vehicule.upper()}<TAB>pages\n#\n")
        for c in cles:
            e = lignes[c]
            arts = ",".join(sorted(e["articles"], key=tri))
            pages = ",".join(str(p) for p in sorted(e["pages"]))
            f.write(f"{c[0]}\t{c[1]}\t\t0\t\t0\t{arts}\t{pages}\n")
    print(dest, "|", len(cles), "adresses |", len(textes), "textes")
    return lignes


if __name__ == "__main__":
    s = json.load(open(sys.argv[1], encoding="utf-8"))
    rendre(s, sys.argv[2], sys.argv[3], sys.argv[4])
