#!/usr/bin/env python3
"""Vérité-terrain de l'éval de `expose-sommaire` — l'éval en sens inverse.

L'éval du vecteur donnait l'exposé sommaire et scellait le dispositif.
Celle-ci **donne le dispositif et scelle l'exposé** : même corpus, même
appareil, direction opposée. Aucun fil n'a lu les exposés en tant que sorties
attendues, donc cette direction n'est pas contaminée.

Ce qui se relève mécaniquement, et cela seul :

  notes      les pièces que GL cite en bas de page — la clé du taux de rappel
             sur les sources, qui est le taux qui compte
  mots       le compte sous la règle de décompte de la skill
  longueur   dans la fourchette 200-300, ou l'écart

Ce qui NE se relève pas et se note à la main, l'exposé de GL et la sortie de la
skill côte à côte : **l'objectif politique nommé**. Il n'est marqué par aucune
balise, et le deviner par script fabriquerait une clé fausse — c'est exactement
la faute d'A-261, où la ligne de rattachement passait pour une adresse.

Le fichier est écrit et **jamais affiché** : seul `noter_eval_expose.py` le lit.
"""
import json
import pathlib
import re
import unicodedata

SRC = pathlib.Path(__file__).parent / "scinde"
FICHES = json.loads((SRC / "liasses_gl.json").read_text(encoding="utf-8"))

# Une note de bas de page s'ouvre sur une ligne ne portant que son numéro ;
# son texte court sur les lignes suivantes jusqu'à la note suivante.
RE_NUM_SEUL = re.compile(r"^\s*(\d{1,2})\s*$")
# Un éditeur ou une autorité nommée dans une note : c'est la clé de rappel.
# On ne relève pas la note entière — un titre se reformule — mais **l'autorité
# et l'année**, qui sont ce qu'un tiers doit retrouver.
RE_ANNEE = re.compile(r"\b(19|20)\d{2}\b")


def sans_accent(s):
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))


AUTORITES = [
    ("cour des comptes", r"cour des comptes"),
    ("conseil des prélèvements obligatoires", r"conseil des prelevements|^cpo\b|\bcpo\b"),
    ("OCDE", r"\bocde\b"),
    ("Insee", r"\binsee\b"),
    ("Dares", r"\bdares\b"),
    ("Unédic", r"\bunedic\b"),
    ("direction générale du Trésor", r"dg tresor|direction generale du tresor"),
    ("Vie Publique", r"vie publique"),
    ("Le Figaro", r"le figaro"),
    ("GenerationLibre", r"generationlibre|generation libre"),
    ("rapport Woerth", r"woerth"),
    ("rapport Noyer", r"noyer"),
    ("Conseil d'État", r"conseil d.?etat"),
    ("Sénat", r"\bsenat\b"),
    ("Assemblée nationale", r"assemblee nationale"),
    ("Agence des participations de l'État", r"agence des participations"),
]


def notes(texte):
    """Rend les notes de bas de page, chacune avec ses autorités et son année."""
    lignes = texte.splitlines()
    debuts = [i for i, l in enumerate(lignes) if RE_NUM_SEUL.match(l)]
    out = []
    for k, i in enumerate(debuts):
        fin = debuts[k + 1] if k + 1 < len(debuts) else len(lignes)
        corps = " ".join(l.strip() for l in lignes[i + 1 : fin]).strip()
        if not corps:
            continue
        plat = sans_accent(corps)
        autorites = [nom for nom, motif in AUTORITES if re.search(motif, plat)]
        annees = sorted({m.group(0) for m in RE_ANNEE.finditer(corps)})
        out.append({
            "numero": RE_NUM_SEUL.match(lignes[i]).group(1),
            "autorites": autorites,
            "annees": annees,
            "texte": corps[:200],
        })
    return out


# La phrase de clôture que GL écrit lui-même, et qui est le seul point de coupe
# NOMMÉ du document : elle ferme le corps, les notes suivent. Présente sur 34
# des 36 exposés.
RE_CLOTURE = re.compile(
    r"Cet amendement est issu des travaux de\s*Generation\s*Libre\s*\.?", re.I
)


def corps_sans_notes(texte):
    """Le corps des trois temps : l'exposé privé de ses notes de bas de page.

    **Le point de coupe est nommé, pas devine** — c'est A-236, et je l'ai violé
    deux fois avant de l'appliquer. Couper au premier chiffre isolé prenait un
    appel de note en milieu de texte pour le début du bloc, et tronquait
    l'exemple de référence de 249 mots à 139. Le reconnaître « à l'allure d'une
    note » mangeait la moitié du corps, un paragraphe court ressemblant à un
    titre de note.

    Le document écrit lui-même sa clôture : « Cet amendement est issu des
    travaux de GenerationLibre. » Elle ferme le corps sur 34 des 36 exposés.
    **Les deux qui ne la portent pas se déclarent** et gardent leur texte
    entier : mieux vaut un compte majoré et dit qu'une troncature silencieuse.
    """
    # 1. La queue au-delà de la clôture sort.
    m = None
    for m in RE_CLOTURE.finditer(texte):
        pass
    corps = texte[: m.end()] if m is not None else texte

    # 2. Les notes que `pdftotext` place en bas de page tombent au milieu du
    #    corps. Chacune s'ouvre sur son numéro seul et court **jusqu'à la ligne
    #    vide suivante** : une note est un paragraphe, et la borne est locale.
    lignes = corps.splitlines()
    garde, i = [], 0
    while i < len(lignes):
        if RE_NUM_SEUL.match(lignes[i]):
            i += 1
            while i < len(lignes) and lignes[i].strip():
                i += 1
            continue
        garde.append(lignes[i])
        i += 1
    return "\n".join(garde)


RE_MOT = re.compile(r"\d[\d  ]*\d|\d|[^\W\d_]+(?:[’'-][^\W\d_]+)*", re.UNICODE)


def compte(texte):
    """Règle de décompte de la skill : corps des trois temps, parenthèses de
    source comprises, appels et notes exclus. Un nombre en chiffres compte pour
    un mot, séparateur de milliers compris ; un mot lié par trait d'union pour
    un."""
    t = re.sub(r"(?<=[a-zà-ÿ»\).])\d{1,2}\b", "", texte)  # appels de note collés
    return len(RE_MOT.findall(t))


def main():
    cles = {}
    for f in FICHES:
        edm = (SRC / "edm" / f"{f['cle']}.txt").read_text(encoding="utf-8")
        corps = corps_sans_notes(edm)
        n = compte(corps)
        cles[f["cle"]] = {
            "nature": f["nature"],
            "variante": f["variante"],
            "titre": f["titre"],
            "notes": notes(edm),
            "mots": n,
            "dans_fourchette": 200 <= n <= 300,
            "objectif_politique": None,  # se note à la main, voir la docstring
        }
    (SRC / "cles_eval_expose.json").write_text(
        json.dumps(cles, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # On ne rend QUE des comptes, jamais le contenu.
    avec = [k for k, v in cles.items() if v["notes"]]
    aut = [a for v in cles.values() for n in v["notes"] for a in n["autorites"]]
    from collections import Counter
    print(f"clés écrites : {len(cles)}  (scellées, non affichées)")
    print(f"  exposés portant au moins une note : {len(avec)}/{len(cles)}")
    print(f"  notes relevées : {sum(len(v['notes']) for v in cles.values())}")
    print(f"  notes dont l'autorité est reconnue : "
          f"{sum(1 for v in cles.values() for n in v['notes'] if n['autorites'])}")
    print(f"  dans la fourchette : {sum(1 for v in cles.values() if v['dans_fourchette'])}"
          f"/{len(cles)}")
    print("  autorités les plus citées :", dict(Counter(aut).most_common(6)))
    print("  objectif politique : à noter à la main, 36 champs vides")


if __name__ == "__main__":
    main()
