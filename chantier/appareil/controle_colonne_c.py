#!/usr/bin/env python3
"""Contrôle : la colonne C du trois colonnes contre le texte de la proposition
par substitution.

Deux écritures du même droit vivent côte à côte sans qu'aucun contrôle ne les
rapproche. Le 20260914 a montré ce que cela coûte : la colonne C avait perdu un
alinéa entier depuis six semaines, et la colonne B le déclarait conservé.

Ce module aligne chaque ligne d'article du tableau sur l'article correspondant
de la proposition par substitution, et signale tout écart de fond.

Usage :
    python3 appareil/controle_colonne_c.py \
        reference/Constitution_3col_AAAAMMJJ_vNN.html \
        livrables/PPLC_consolidee_substitution_AAAAMMJJ_vN.md

Sortie : un relevé par article, et un code de retour non nul s'il reste un
écart. Un contrôle qui ne sort rien n'est pas un contrôle qui passe : le
relevé dit toujours combien d'articles ont été appariés.
"""

import html
import re
import sys
import unicodedata

# --------------------------------------------------------------------------
# Normalisation
# --------------------------------------------------------------------------

GUILLEMETS = "«»“”„″\""
APOSTROPHES = "’ʼ′"
TIRETS = "‐‑‒–—―−"


def normaliser(texte):
    """Ramène deux écritures du même droit à une forme comparable.

    Ne touche qu'à ce qui est typographique : guillemets, apostrophes, tirets,
    espaces (insécables comprises). Aucun mot n'est retiré.
    """
    t = unicodedata.normalize("NFC", texte)
    for c in GUILLEMETS:
        t = t.replace(c, "")
    for c in APOSTROPHES:
        t = t.replace(c, "'")
    for c in TIRETS:
        t = t.replace(c, "-")
    t = t.replace(" ", " ").replace(" ", " ").replace(" ", " ")
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def mots(texte):
    return normaliser(texte).split(" ")


# --------------------------------------------------------------------------
# Lecture de la colonne C
# --------------------------------------------------------------------------

RE_ROW = re.compile(r'<div class="art-row">(.*?)\n</div>', re.S)
RE_LABEL = re.compile(r'<span class="art-label[^"]*">(.*?)</span>', re.S)
RE_CELL_C = re.compile(r'<div class="cell cell-c">(.*?)</div>', re.S)
RE_NOTE = re.compile(r'<span class="note">.*?</span>', re.S)
RE_TAG = re.compile(r"<[^>]+>")


def depouiller(fragment):
    """Retire le balisage et les notes de bas de cellule."""
    f = RE_NOTE.sub(" ", fragment)
    f = f.replace("<br>", "\n")
    f = RE_TAG.sub("", f)
    return html.unescape(f)


def lire_colonne_c(chemin):
    """Rend {label : texte de la colonne C}, dans l'ordre du document."""
    source = open(chemin, encoding="utf-8").read()
    # Les lignes d'article sont des blocs <div class="art-row"> imbriqués :
    # on les découpe sur le marqueur d'ouverture plutôt que par appariement.
    blocs = source.split('<div class="art-row">')[1:]
    lignes = {}
    for bloc in blocs:
        label = RE_LABEL.search(bloc)
        cellule = RE_CELL_C.search(bloc)
        if not label or not cellule:
            continue
        lignes[depouiller(label.group(1)).strip()] = depouiller(cellule.group(1))
    return lignes


# --------------------------------------------------------------------------
# Lecture de la proposition par substitution
# --------------------------------------------------------------------------

RE_ART_SUB = re.compile(
    r"[«\"]\s*Art\.\s*(\d+(?:\s*-\s*\d+)?(?:\s*er)?)\s*\.?\s*[-–—]+\s*",
)


RE_BORNE = re.compile(r"^(?:\*\*Article |#{2,4} |\*\[)", re.M)


def lire_substitution(chemin):
    """Rend {numéro d'article : texte cible}.

    Un article de la proposition ouvre le texte cible par « Art. N. — ». Il se
    referme au premier de : l'article suivant de la proposition, un intitulé de
    titre ou de chapitre, ou le prochain bloc de proposition. **La borne
    compte autant que l'ouverture** : prise trop loin, le contrôle compare le
    texte cible à la table des matières qui le suit et sort un écart faux.
    """
    source = open(chemin, encoding="utf-8").read()
    debuts = [(m.start(), m.end(), m.group(1)) for m in RE_ART_SUB.finditer(source)]
    cibles = {}
    for i, (deb, fin, num) in enumerate(debuts):
        plafond = debuts[i + 1][0] if i + 1 < len(debuts) else len(source)
        borne = plafond
        m = RE_BORNE.search(source, fin, plafond)
        if m:
            borne = m.start()
        cibles[cle_article(num)] = source[fin:borne]
    return cibles


def cle_article(brut):
    """« 34 », « 61-1 », « 1er » → clé comparable."""
    b = normaliser(brut).lower().replace(" ", "").replace("er", "")
    return b.strip(".-") or brut


RE_LABEL_NUM = re.compile(r"(\d+(?:\s*-\s*\d+)?)")


def cle_label(label):
    m = RE_LABEL_NUM.search(label)
    return cle_article(m.group(1)) if m else None


# --------------------------------------------------------------------------
# Comparaison
# --------------------------------------------------------------------------

# Une cellule ne montre pas toujours l'article entier : le tableau abrège par
# une coupure « […] », par un renvoi d'alinéa « Al. 3 : », ou par une annotation
# entre crochets « [Alinéas 1, 2 et 4 conservés.] ». Les trois formes coexistent
# et aucune n'est une divergence : **un extrait se contrôle par inclusion, pas
# par égalité.**
RE_CROCHETS = re.compile(r"\[[^\]]*\]")
RE_RENVOI_AL = re.compile(
    r"Al(?:\.|in[ée]as?)\s*"
    r"(?:\d+(?:\s*(?:,|et|à|-)\s*\d+)*|final|dernier|premier|nouveau)"
    r"[^:.]{0,40}?\s*:\s*",
    re.I,
)
RE_LABEL_AL = re.compile(r"\bal(?:\.|in[ée]a)", re.I)


def est_extrait(texte, label=""):
    """La cellule montre-t-elle un fragment plutôt que l'article entier ?"""
    if RE_LABEL_AL.search(label):
        return True
    return bool(RE_CROCHETS.search(texte) or RE_RENVOI_AL.search(texte))


def segments(texte):
    """Découpe une cellule d'extrait en morceaux contigus attendus.

    Les annotations du tableau — crochets et renvois d'alinéa — ne sont pas du
    texte de droit : elles bornent les morceaux, elles n'en font pas partie.
    """
    t = RE_CROCHETS.sub("\n", texte)
    t = RE_RENVOI_AL.sub("\n", t)
    morceaux = [normaliser(x) for x in t.split("\n")]
    # Un morceau d'un ou deux mots ne prouve rien : il se retrouve partout.
    return [m for m in morceaux if len(m.split(" ")) >= 3]


def ecart_extrait(cellule, cible):
    """Chaque morceau de l'extrait doit se retrouver tel quel dans la cible.

    Rend None si tout concorde, sinon le premier morceau introuvable.
    """
    ref = normaliser(cible)
    for seg in segments(cellule):
        if seg not in ref:
            return seg
    return None


def premier_ecart(a, b):
    """Rend (index, contexte a, contexte b) au premier mot qui diverge."""
    ma, mb = mots(a), mots(b)
    n = min(len(ma), len(mb))
    for i in range(n):
        if ma[i] != mb[i]:
            return i, " ".join(ma[max(0, i - 8):i + 8]), " ".join(mb[max(0, i - 8):i + 8])
    if len(ma) != len(mb):
        i = n
        return i, " ".join(ma[max(0, i - 8):i + 8]), " ".join(mb[max(0, i - 8):i + 8])
    return None


def controler(chemin_3col, chemin_sub):
    colonne_c = lire_colonne_c(chemin_3col)
    cibles = lire_substitution(chemin_sub)

    apparies, ecarts, orphelins_tableau, orphelins_proposition = [], [], [], []
    vus = set()

    for label, texte in colonne_c.items():
        cle = cle_label(label)
        if cle is None or cle not in cibles:
            orphelins_tableau.append(label)
            continue
        vus.add(cle)
        if est_extrait(texte, label):
            manquant = ecart_extrait(texte, cibles[cle])
            if manquant is None:
                apparies.append(label + " (extrait)")
            else:
                ecarts.append((label + " (extrait)", (None, manquant, "")))
            continue
        ecart = premier_ecart(texte, cibles[cle])
        if ecart is None:
            apparies.append(label)
        else:
            ecarts.append((label, ecart))

    for cle in cibles:
        if cle not in vus:
            orphelins_proposition.append(cle)

    return apparies, ecarts, orphelins_tableau, orphelins_proposition


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    apparies, ecarts, orph_t, orph_p = controler(sys.argv[1], sys.argv[2])

    print(f"appariés et concordants : {len(apparies)}")
    print(f"appariés et divergents  : {len(ecarts)}")
    print(f"au tableau seulement    : {len(orph_t)}")
    print(f"à la proposition seule  : {len(orph_p)}")
    print()

    for label, (i, ctx_a, ctx_b) in ecarts:
        if i is None:
            print(f"--- {label} — morceau introuvable à la substitution")
            print(f"    colonne C    : …{ctx_a}…")
            print()
            continue
        print(f"--- {label} — premier écart au mot {i}")
        print(f"    colonne C    : …{ctx_a}…")
        print(f"    substitution : …{ctx_b}…")
        print()

    if orph_t:
        print("Lignes du tableau sans article correspondant à la proposition :")
        for label in orph_t:
            print(f"    {label}")
        print()
    if orph_p:
        print("Articles de la proposition sans ligne au tableau :")
        for cle in orph_p:
            print(f"    art. {cle}")
        print()

    if not apparies:
        print("AUCUN APPARIEMENT — le contrôle n'a rien mesuré, il ne passe pas.")
        return 2
    return 1 if (ecarts or orph_p) else 0


if __name__ == "__main__":
    sys.exit(main())
