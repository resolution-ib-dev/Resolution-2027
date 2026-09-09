#!/usr/bin/env python3
"""Relève, dans chaque dispositif scellé, l'adresse que l'amendement vise.

C'est la VÉRITÉ-TERRAIN de l'éval (A-249). Elle est écrite sur disque et
**jamais affichée** : le fil qui joue l'éval ne doit pas la voir, sinon il se
donne la réponse. Seul `noter.py` la lit, pour comparer.

Le relevé est mécanique et ne juge rien : il prend les références d'article et
les codes que le texte du dispositif nomme lui-même.
"""
import json
import pathlib
import re

import ref_norme

SRC = pathlib.Path(__file__).parent / "scinde"
FICHES = json.loads((SRC / "liasses_gl.json").read_text(encoding="utf-8"))

# Un code nommé en clair dans le dispositif.
CODES = [
    ("code général des impôts", r"code g[ée]n[ée]ral des imp[ôo]ts"),
    ("code des impositions sur les biens et services", r"code des impositions sur les biens et services"),
    ("code général des collectivités territoriales", r"code g[ée]n[ée]ral des collectivit[ée]s territoriales"),
    ("code de l'environnement", r"code de l[’']environnement"),
    ("code du travail", r"code du travail"),
    ("code de la sécurité sociale", r"code de la s[ée]curit[ée] sociale"),
    ("code de l'éducation", r"code de l[’'][ée]ducation"),
    ("code de la construction et de l'habitation", r"code de la construction"),
    ("code monétaire et financier", r"code mon[ée]taire et financier"),
    ("code de commerce", r"code de commerce"),
    ("code du patrimoine", r"code du patrimoine"),
    ("code du sport", r"code du sport"),
    ("code de l'action sociale et des familles", r"code de l[’']action sociale"),
    ("code des transports", r"code des transports"),
    ("code de la défense", r"code de la d[ée]fense"),
    ("code de l'énergie", r"code de l[’']([ée]nergie)"),
    ("code des douanes", r"code des douanes"),
    ("livre des procédures fiscales", r"livre des proc[ée]dures fiscales"),
]

ORD = (r"(?:bis|ter|quater|quinquies|sexies|septies|octies|novies|decies|undecies|"
       r"duodecies|terdecies|quaterdecies|quindecies|sexdecies|septdecies|"
       r"octodecies|novodecies|vicies|unvicies|duovicies|tervicies)")
# Le numéro admet un suffixe en lettre capitale — « 200 A », « 790 G »,
# « 244 quater B », « 278 sexies-0 A ». Le couper produit une fausse adresse,
# et c'est la faute d'A-251 refaite ici : on la borne explicitement.
RE_ART = re.compile(
    r"[Aa]rticles?\s+((?:L|R|D)\.?\s*)?"
    r"(\d+(?:\s*-\s*\d+)*(?:\s+" + ORD + r")*(?:\s*-\s*\d+)?(?:\s+[A-Z](?![a-zé]))?)"
)

# Le troisième piège de la même famille que les deux d'A-261, attrapé par `K2`
# et non par une relecture. « Les articles 778, 784 B, 787 A, 790 B, 790 D,
# 790 E, 790 F, 790 G et 796-0 bis sont abrogés » ne nomme pas un article mais
# neuf : `RE_ART` ne relevait que le premier fragment de l'énumération, et les
# huit autres tombaient de la clé. Le même défaut coupait tout suffixe que
# `RE_ART` ne prévoit pas — « 223 O », « 1965 L », « 150 UC », « 150 VM ».
#
# **Rien de cette grammaire ne s'écrit ici.** Le corpus la porte déjà à deux
# endroits, et les deux sont appelés :
#
#   `socle_plf_texte.REFERENCE`        la suite de numéros d'articles, avec la
#                                      grammaire large — ordinaux du plus long
#                                      au plus court, suffixe de capitales
#                                      répétable. Elle est **déclarée plus
#                                      large que celle de `ref_norme`**, dont
#                                      l'écart est compté et non absorbé.
#   `articles_ouverts_plf.ENUMERATION` le découpage en fragments : la virgule,
#                                      le point-virgule et « et » séparent,
#                                      **« à » ne sépare pas** (A-343).
#
# **L'adresse retenue est le libellé exact du fragment**, comme à la table des
# articles ouverts : la jointure se fait sur le libellé, jamais au plus proche.
# `ref_norme.decouper_articles` n'est donc pas appelé pour trancher l'adresse —
# il tronquerait « 244 quater I » en « 244 quater » —, et sa lecture n'est pas
# reportée à la clé : ce que la clé doit porter est ce que le dispositif écrit.
import articles_ouverts_plf
import socle_plf_texte

FOURCHETTE = articles_ouverts_plf.FOURCHETTE

# La ligne de rattachement — « Après l'article 65 » — nomme le VÉHICULE, pas le
# vecteur. La relever comme adresse est l'erreur qu'`N1` refuse. Elle sort du
# corps avant toute extraction.
RE_RATTACHEMENT = re.compile(
    r"^\s*(?:Article\s+additionnel\s+)?(?:Avant|Apr[eè]s|[AÀ])\s+l[’']article\s+\S+|"
    r"^\s*Article\s+\d+\s*(?:\(.*\))?\s*$|"
    r"^\s*Ins[ée]rer\s|^\s*Le\s+pr[ée]sent\s+article\s*$",
    re.I,
)
# Un amendement de crédits vise une mission et des programmes, pas un article.
RE_PROG = re.compile(r"\b(?:programme|Programme)\s+(\d{3})\b")
RE_MISSION = re.compile(r"mission\s+[«\"']?\s*([A-ZÀ-Ý][^»\"'\n(]{2,60})")


def adresse(disp):
    codes = [nom for nom, motif in CODES if re.search(motif, disp, re.I)]
    arts, fourchettes = [], []
    for m in socle_plf_texte.REFERENCE.finditer(disp):
        brut = re.sub(r"\s+", " ", m.group(1)).strip(" ,.;:")
        for frag in articles_ouverts_plf.ENUMERATION.split(brut):
            frag = ref_norme.PREFIXES.sub("", frag.strip())
            if not frag:
                continue
            arts.append(frag)
            # Une fourchette reste UNE adresse, marquée comme telle. Son
            # dépliage vit à `plages_articles.py` et ne se fait pas ici.
            if FOURCHETTE in frag:
                fourchettes.append(frag)
    # dédoublonnage en conservant l'ordre
    vus, uniq = set(), []
    for a in arts:
        if a not in vus:
            vus.add(a)
            uniq.append(a)
    progs = sorted({m.group(1) for m in RE_PROG.finditer(disp)})
    missions = sorted({re.sub(r"\s+", " ", m.group(1)).strip(" ,;") for m in RE_MISSION.finditer(disp)})
    return {"codes": codes, "articles": uniq,
            "fourchettes": sorted(set(fourchettes)),
            "programmes": progs, "missions": missions}


def main():
    cles = {}
    for f in FICHES:
        disp = (SRC / "dispositif" / f"{f['cle']}.txt").read_text(encoding="utf-8")
        corps = "\n".join(l for l in disp.splitlines() if not RE_RATTACHEMENT.match(l))
        a = adresse(corps)
        a["nature"] = f["nature"]
        a["variante"] = f["variante"]
        a["article_plf"] = f["article_plf"]
        # Le véhicule du couple, dérivé de la partie de la liasse et jamais
        # supposé — G1 du contrat. Il est nécessaire depuis que la clé porte
        # les trois liasses : `noter_eval_gl.py` filtrait sa population sur la
        # seule nature, ce qui était juste tant que la clé ne portait qu'un
        # véhicule, et qui fait entrer les couples de financement dans le
        # dénominateur du lot de finances dès qu'elle en porte deux.
        a["vehicule"] = "plfss" if f["partie"] == "PLFSS" else "plf"
        cles[f["cle"]] = a
    (SRC / "cles_eval.json").write_text(
        json.dumps(cles, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    # Le résumé ne rend QUE ce que le fil connaît déjà par la liasse : combien
    # de couples, et leur ventilation par nature et par variante. Rien qui
    # renseigne sur la réponse.
    #
    # La version précédente nommait en clair les cas sans adresse relevable et
    # comptait ceux qui portent un article : c'était donner la moitié de la clé
    # avant que le fil joue, et deux cas du lot de financement ont été joués en
    # connaissance de cause. La vérité-terrain est scellée ou elle n'est pas.
    par_nature = {}
    par_variante = {}
    for v in cles.values():
        par_nature[v["nature"]] = par_nature.get(v["nature"], 0) + 1
        par_variante[v["variante"]] = par_variante.get(v["variante"], 0) + 1
    print(f"clés écrites : {len(cles)}  (scellées, non affichées)")
    print("  nature   " + ", ".join(f"{n} {c}" for n, c in sorted(par_nature.items())))
    print("  variante " + ", ".join(f"{n} {c}" for n, c in sorted(par_variante.items())))
    print("  le détail de la clé ne s'affiche pas : seul `noter_eval_gl.py` le lit,")
    print("  et il ne se lit qu'après que les réponses ont été écrites.")


if __name__ == "__main__":
    main()
