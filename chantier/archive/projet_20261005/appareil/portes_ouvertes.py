#!/usr/bin/env python3
"""Portes ouvertes par un texte financier — relevé mécanique depuis le socle.

Une porte ouverte est un couple (texte, article) que la disposition du véhicule
modifie elle-même. L'exposé des motifs n'en ouvre aucune : il est de l'indice,
jamais de la porte (A-229).

Grammaire de relevé — les sept règles du millésime 2027 :
 1. le repère de page est le folio imprimé, porté par le socle ;
 2-5. le découpage en mesures est l'affaire de l'index, pas de ce relevé ;
 6. les passages entre guillemets sont blanchis avant toute détection de siège,
    le blanchiment traverse les lignes et les offsets sont préservés ;
 7. le contexte de pièce se porte le long de l'article et ne se met à jour que
    sur une formule de modification.

Sortie au schéma de `referentiels/articles_ouverts_<vehicule>.tsv` (millésime
2026), qui alimente la colonne `variante` de REF_norme.
"""
import json, re, sys
import pieces_nommees

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
ADRESSE = re.compile(
    r"\b(?:articles?|art\.)\s+"
    r"(?P<a>[LRD]\.?\s?\d+(?:[\-‑]\d+)*(?:\s(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies|terdecies|quaterdecies|quindecies|sexdecies|septdecies|octodecies|novodecies|vicies))?"
    r"|\d+(?:[\-‑]\d+)*(?:\s?(?:-0)?\s?[A-Z](?:\s(?:bis|ter|quater))?)?"
    r"(?:\s(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies|terdecies|quaterdecies|quindecies|sexdecies|septdecies|octodecies|novodecies|vicies))?"
    r"(?:\s[A-Z])?)")

SUITE = re.compile(
    r"\s*(?:,|\set\s|\sou\s)\s*"
    r"(?P<a>[LRD]\.?\s?\d+(?:[\-‑]\d+)*(?:\s(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies|terdecies|quaterdecies|quindecies|sexdecies|septdecies))?)"
    r"(?![\w\-])")

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


def portes(socle):
    lignes = {}
    for art in socle["articles"]:
        d = blanchir(art["dispositif"])
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
            accolee = next((n for s, e, n in pieces
                            if fin_adr <= s <= fin_adr + 40
                            and re.match(r"\s*(?:du|de la|de l[’'])\s*$", d[fin_adr:s])), None)
            fin_phrase = d.find(".", pos)
            fin_phrase = len(d) if fin_phrase < 0 else fin_phrase
            suivante = next((n for s, e, n in pieces if pos < s < fin_phrase), None)
            precedente = next((n for s, e, n in reversed(pieces) if s < pos), None)
            contexte = accolee or precedente or suivante or "indéterminé"
            cle = (contexte, a)
            e = lignes.setdefault(cle, {"articles": set(), "pages": set()})
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
        f.write("# Alimente la colonne `variante` de REF_norme : `article_ouvert` sur les\n"
                "# vecteurs dont le couple (texte, article) figure ici, `absolu` ailleurs.\n"
                "# Jointure sur le libellé exact, jamais au plus proche (A-94).\n"
                "# Ouvert = modifié par la disposition, jamais cité. L'exposé des motifs ne\n"
                "# compte pas : il est de l'indice, pas de la norme (A-229).\n")
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
