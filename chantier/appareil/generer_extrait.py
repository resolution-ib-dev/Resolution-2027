# -*- coding: utf-8 -*-
"""Extrait lisible « gagnants et perdants », ordre du lecteur d'ensemble.

Projection du référentiel des positions vers un document diffusable. Aucune
valeur n'est écrite ici : intitulés et chiffres sont lus au REF, justifications
et relais au référentiel des positions. La jointure est celle de
`generer_inventaire_20260820_v5.py`, importée et non réécrite.

Ce que l'extrait ne porte jamais : identifiant de nœud, identifiant de ligne,
degré, nom de champ, mention du référentiel. Le bloc `[interne]` de pied porte
seul la traçabilité et se retire en une opération.

Usage : python3 generer_extrait.py REF.json Positions.json Notes.json sortie.html
"""
import html
import importlib.util
import json
import os
import re
import sys

AUCUNE = "aucune, par construction"
RECONST = "reconstitution volontaire du flux"

# L'ordre du document est celui de la doctrine : axes D1 à D12, dans l'ordre du
# référentiel. Une catégorie se range sous l'axe qui porte le plus de ses lignes.
AXE_MANUSCRIT = "manuscrit"

# Catégories tenues hors du corps : elles ouvrent ou elles ferment.
C_NATION = "C-00"

CSS = """
:root{--enc:#1a1a1a;--pap:#fdfcfa;--fil:#ddd7cd;--gain:#1f5c3a;--perte:#8a2f22;
--capt:#6b5b3e;--gris:#6d6a64}
*{box-sizing:border-box}
body{margin:0;padding:2.6rem 1.4rem 5rem;background:var(--pap);color:var(--enc);
font:16px/1.62 Georgia,"Iowan Old Style",serif;max-width:44rem;margin-inline:auto}
h1{font-size:1.75rem;line-height:1.25;margin:0 0 .5rem;font-weight:600}
h2{font-size:1.22rem;margin:3rem 0 .2rem;padding-bottom:.3rem;
border-bottom:2px solid var(--enc);font-weight:600}
h3{font-size:1.02rem;margin:2rem 0 .1rem;font-weight:600}
p{margin:.5rem 0}
.chapeau{color:var(--gris);font-size:.95rem;margin:0 0 1.6rem}
.intro{font-size:1.02rem;margin:.8rem 0 1.4rem}
.fam{color:var(--gris);font-size:.9rem;margin:.4rem 0 1.2rem;font-style:italic}
.compte{color:var(--gris);font-size:.82rem;margin:.15rem 0 .7rem;
text-transform:uppercase;letter-spacing:.04em}
ul{list-style:none;margin:.4rem 0 .9rem;padding:0}
li{margin:.55rem 0 .55rem 1.5rem;position:relative}
li .s{position:absolute;left:-1.5rem;font-weight:700;width:1.1rem}
li.gain .s{color:var(--gain)}
li.perte .s{color:var(--perte)}
li.capt .s{color:var(--capt)}
li.diag .s{color:var(--gris)}
.just{display:block;margin-top:.2rem;color:var(--gris);font-size:.94rem}
.rel{display:block;margin-top:.25rem;color:var(--gain);font-size:.94rem;
font-style:italic}
.dur{display:block;margin-top:.25rem;color:var(--perte);font-size:.94rem;
font-style:italic}
li.redite{color:var(--gris);font-size:.94rem}
li.redite .s{opacity:.55}
.clos{margin:.5rem 0 1.4rem;padding-left:.9rem;border-left:3px solid var(--gain);
color:var(--gain);font-style:italic}
.bloc{margin:1.4rem 0;padding:1rem 1.2rem;background:#f6f2ea;
border-left:3px solid var(--enc)}
.bloc p{margin:.35rem 0}
.bloc .t{font-weight:600;font-style:normal;color:var(--enc)}
footer{margin-top:4rem;padding-top:1rem;border-top:1px solid var(--fil);
color:var(--gris);font-size:.82rem}
"""


def e(x):
    return html.escape(x or "")


def phrase(t):
    """Termine une projection par un point quand elle n'en porte pas."""
    t = (t or "").strip()
    if t and t[-1] not in ".!?…»":
        t += "."
    return t


# Renvois d'appareil : ils portent la traçabilité, ils ne se publient pas.
RENVOI = re.compile(
    r"\s*[(\[][^()\[\]]*(?:renvoi|bornes de|sous-items)[^()\[\]]*[)\]]"
    r"|\s*,?\s*par renvoi à\s+[A-Z]\d[\w-]*"
    r"|\s*sous-items du nœud\s*:?", re.I)
NOEUD = re.compile(r"\s*\b[A-Z]\d{1,2}(?:-\d+)+(?:-[a-z]\d+)?\b")


def epurer(t):
    """Retire de la projection tout ce qui relève de l'appareil interne."""
    t = re.split(r"\s+—\s+\[e\d+\]", t or "")[0]
    t = RENVOI.sub("", t)
    t = NOEUD.sub("", t)
    t = re.sub(r"[ \t]+([,.])", r"\1", t)
    # La ponctuation double appelle une espace insécable en français.
    t = re.sub(r"[ \u00a0\u202f]*([;:!?»])", "\u202f\\1", t)
    t = re.sub(r"(«)[ \u00a0\u202f]*", "\\1\u202f", t)
    t = re.sub(r"\s{2,}", " ", t).strip(" ;,")
    return t.strip()


def grandeur(l):
    """Forme affichable d'une grandeur : le résultat, jamais l'opération."""
    g = (l.get("grandeur") or "").strip()
    if g == "qualitatif":
        return ""
    if "=" in g:
        g = g.split("=")[-1].strip()
    return epurer(g)


def enonce(l):
    """Texte de tête. Une perte écrite se donne par sa justification : son
    énoncé du REF la répéterait. Une ligne muette se dit par sa proposition."""
    txt = (l["ctx"].get("enonce") or "").strip()
    # Les ancrages du manuscrit portent le texte de leurs notes en appareil.
    # La note se cite, elle ne se publie pas.
    txt = epurer(txt)
    g = grandeur(l)
    if not txt:
        txt = (l["ctx"].get("proposition_t") or "").strip()
    if (l.get("justification") or "").strip():
        # La justification porte le contenu : un énoncé de tête la répéterait.
        return g
    if txt and g:
        return f"{phrase(txt)[:-1]} — {g}."
    return phrase(txt or g)


# Une même ligne sert plusieurs catégories. Sa première sortie est complète, les
# suivantes sont brèves : la répétition s'assume, elle ne s'étale pas.
VUS = set()


def epurer_texte(t):
    """Un appel de note trace la source pour les auteurs ; il ne se publie pas.
    Le lecteur extérieur ne rencontre jamais la nomenclature interne."""
    t = re.sub(r"\s*\((?:cf\.\s*)?notes?\s+e\d+(?:\s*,\s*e\d+)*\)", "", t or "")
    t = re.sub(r"[ \t]+([,.])", r"\1", t)
    # La ponctuation double appelle une espace insécable en français.
    t = re.sub(r"[ \u00a0\u202f]*([;:!?»])", "\u202f\\1", t)
    t = re.sub(r"(«)[ \u00a0\u202f]*", "\\1\u202f", t)
    return re.sub(r"\s{2,}", " ", t).strip()


def ligne(l, bref=None):
    cl = {"gagnant": "gain", "perdant": "perte", "capteur": "capt",
          "diagnostic": "diag"}[l["position"]]
    signe = {"gagnant": "+", "perdant": "−", "capteur": "×",
             "diagnostic": "·"}[l["position"]]
    # Un gain rédigé se projette par son apport ; à défaut, par l'énoncé du REF.
    app = epurer_texte(l.get("apport"))
    contre = epurer_texte(l.get("contrepartie"))
    tete = app or enonce(l)
    j = epurer_texte(l.get("justification"))
    r = epurer_texte(l.get("relais"))
    cle = (tete or j)[:90]
    if bref is None:
        bref = cle in VUS
    VUS.add(cle)
    if bref:
        court = tete or j
        return (f'<li class="{cl} redite"><span class="s">{signe}</span>'
                f'{e(phrase(court))}</li>')
    o = [f'<li class="{cl}"><span class="s">{signe}</span>{e(tete)}'
         if tete else f'<li class="{cl}"><span class="s">{signe}</span>']
    if j:
        o.append(f'<span class="just">{e(phrase(j))}</span>')
    if contre:
        o.append(f'<span class="just">{e(phrase(contre))}</span>')
    if r:
        o.append(f'<span class="rel">{e(phrase(r))}</span>')
    elif l["position"] in ("perdant", "capteur") and l.get("raccroche") == AUCUNE:
        o.append('<span class="dur">Rien ne se reconstitue ici, et le plan '
                 'l’assume.</span>')
    o.append("</li>")
    return "".join(o)


PROMESSES = []


def poids(l):
    """Ordre de sortie à l'intérieur d'une catégorie.

    Perte, rente, gain, diagnostic. À l'intérieur d'un même côté, les promesses
    du manuscrit sortent en tête et dans leur ordre, puis les axes de la
    doctrine dans le leur, puis ce qui porte un chiffre avant ce qui reste
    qualitatif. Ni l'identifiant ni l'alphabet ne commandent quoi que ce soit.
    """
    a = l["ancrage"]
    promesse = PROMESSES.index(a) if a in PROMESSES else len(PROMESSES)
    axe = l["ctx"].get("axe", "") if l.get("ctx") else ""
    rang_axe = int(axe[1:]) if axe[1:].isdigit() else 99
    return ({"perdant": 0, "capteur": 1, "gagnant": 2,
             "diagnostic": 3}[l["position"]],
            promesse,
            rang_axe,
            0 if grandeur(l) else 1,
            {"macro": 0, "méso": 1, "micro": 2}.get(l["echelle"], 3),
            a)


def compte(lot):
    n = {"perdant": 0, "capteur": 0, "gagnant": 0, "diagnostic": 0}
    for l in lot:
        n[l["position"]] += 1
    m = []
    if n["perdant"]:
        m.append(f"{n['perdant']} perte" + ("s" if n["perdant"] > 1 else ""))
    if n["capteur"]:
        m.append(f"{n['capteur']} rente supprimée" if n["capteur"] == 1
                 else f"{n['capteur']} rentes supprimées")
    if n["gagnant"]:
        m.append(f"{n['gagnant']} gain" + ("s" if n["gagnant"] > 1 else ""))
    return " · ".join(m)


def bloc_categorie(cat, lot, bref=None):
    """Un bloc par catégorie. Ordre : perte, rente, gain. Pied sur le relais."""
    lot = sorted(lot, key=poids)
    titre = cat["terme"][0].upper() + cat["terme"][1:]
    eff = (cat.get("effectif") or "").strip()
    o = [f"<h3>{e(titre)}</h3>"]
    tete = compte(lot)
    if eff:
        tete = f"{eff} · {tete}"
    o.append(f'<p class="compte">{e(tete)}</p>')
    o.append("<ul>" + "".join(ligne(l, bref) for l in lot) + "</ul>")
    rel = [l["relais"] for l in lot
           if l["position"] in ("perdant", "capteur") and (l.get("relais") or "").strip()]
    if len(rel) > 1:
        o.append(f'<p class="clos">{e(phrase(rel[0]))}</p>')
    elif not any(l["position"] in ("perdant", "capteur") for l in lot):
        o.append('<p class="clos">Cette catégorie ne porte que des gains.</p>')
    return "".join(o)


def axe_dominant(lot):
    n = {}
    for l in lot:
        a = l["ctx"].get("axe", "")
        n[a] = n.get(a, 0) + 1
    n.pop(AXE_MANUSCRIT, None)
    if not n:
        return "D99"
    return max(sorted(n), key=lambda k: (n[k], -int(k[1:]) if k[1:].isdigit() else 0))


def rendre(brutes, cats, axes, date, ref_nom, pos_nom, ecartees_n, groupes=None):
    """Ordre du document, dans l'esprit du manuscrit.

    1. Ce que le plan produit — la promesse d'ensemble, chiffres en tête.
    2. Les familles de personnes, du plus large au plus particulier.
    3. Le risque qui diminue — l'état présent, qui se constate et ne se promet
       pas. Il vient après les gains, jamais avant.
    4. Les rentes supprimées — l'argument offensif, qui ferme.
    """
    par_cat = {}
    for l in brutes:
        par_cat.setdefault(l["categorie"], []).append(l)

    groupes = groupes or []
    nation = par_cat.get(C_NATION, [])
    diagnostics = [l for l in brutes if l["position"] == "diagnostic"]
    rentes = groupes[-1] if groupes else None

    o = ['<!DOCTYPE html><html lang="fr"><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         "<title>Ce que le plan donne et ce qu\u2019il retire</title>",
         f"<style>{CSS}</style>",
         "<h1>Ce que le plan donne, et ce qu\u2019il retire</h1>",
         '<p class="chapeau">Qui gagne, qui perd, et par quelle voie chacun '
         'retrouve ailleurs ce qu\u2019il perd ici.</p>']

    # ---- 1. Ce que le plan produit
    o.append("<h2>Ce que le plan produit</h2>")
    o.append('<p class="intro">Le plan rend au pays une part de ce qu\u2019il produit '
             'déjà. Cette part se donne en ordre de grandeur, parce qu\u2019un '
             'engagement se tient à la portée de ce qui est démontré.</p>')
    ouverture = sorted([l for l in nation if l["position"] == "gagnant"], key=poids)
    o.append("<ul>" + "".join(ligne(l) for l in ouverture) + "</ul>")

    # ---- 2. Les familles de personnes
    for g in groupes:
        if rentes is not None and g is rentes:
            continue
        lots = [(cats[c], [l for l in par_cat.get(c, [])
                           if l["position"] in ("perdant", "gagnant")])
                for c in g["categories"] if c in cats and c != C_NATION]
        lots = [(c, lot) for c, lot in lots if lot]
        if not lots:
            continue
        o.append(f'<h2>{e(g["titre"])}</h2>')
        o.append(f'<p class="fam">{e(g["chapeau"])}</p>')
        for c, lot in lots:
            o.append(bloc_categorie(c, lot))

    # ---- 3. Le risque qui diminue
    if diagnostics:
        o.append("<h2>Le risque qui diminue</h2>")
        o.append('<p class="intro">Ce qui suit décrit l\u2019état présent, non un effet '
                 'du plan. L\u2019écart mesuré avec les pays comparables dit le '
                 'possible, et la dette dit le risque. Le plan en récupère la part '
                 'qu\u2019il démontre, et rien de plus.</p>')
        o.append("<ul>" + "".join(ligne(l) for l in sorted(diagnostics, key=poids))
                 + "</ul>")

    # ---- 4. Les rentes supprimées
    o.append("<h2>Les rentes supprimées</h2>")
    o.append('<p class="intro">Chaque dispositif supprimé nourrissait quelqu\u2019un '
             'dont le métier était le dispositif lui-même. Le marché se rouvre, '
             'la commande captive disparaît.</p>')
    ids = rentes["categories"] if rentes is not None else []
    for c in ids:
        lot = [l for l in par_cat.get(c, []) if l["position"] == "capteur"]
        if lot and c in cats:
            o.append(bloc_categorie(cats[c], lot, bref=False))
    ailleurs = [l for l in brutes
                if l["position"] == "capteur" and l["categorie"] not in ids]
    par_a = {}
    for l in ailleurs:
        par_a.setdefault(l["categorie"], []).append(l)
    for c, lot in par_a.items():
        if c in cats:
            o.append(bloc_categorie(cats[c], lot, bref=False))

    o.append(f'<footer>[interne] Extrait projeté le {date} depuis '
             f'<code>{e(pos_nom)}</code>, sur <code>{e(ref_nom)}</code>. '
             f'{len(brutes)} ligne(s) projetée(s), {ecartees_n} écartée(s) au '
             f'degré complété. Ordre des sections : groupes du référentiel des '
             f'positions. Justifications et relais lus au référentiel, jamais '
             f'réécrits. Bloc retirable en une opération.</footer>')
    o.append("</html>")
    return "\n".join(o)


def main(argv):
    if len(argv) < 5:
        print(__doc__)
        return 2
    ref_p, pos_p, notes_p, sortie = argv[1:5]
    ici = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(ici, "generer_inventaire.py")
    spec = importlib.util.spec_from_file_location("gi", src)
    gi = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gi)

    ref = json.load(open(ref_p, encoding="utf-8"))
    pos = json.load(open(pos_p, encoding="utf-8"))
    notes = json.load(open(notes_p, encoding="utf-8"))
    if isinstance(notes, dict) and "notes" in notes:
        notes = notes["notes"]
    if isinstance(notes, list):
        notes = {n["id"]: n for n in notes}
    brutes, _, anomalies, _, cats, _ = gi.assembler(ref, pos, notes)

    gardees = [l for l in brutes if l["degre"] != "complété"]
    ecartees = len(brutes) - len(gardees)

    from datetime import date as _d
    PROMESSES[:] = pos.get("promesses", [])
    txt = rendre(gardees, cats, ref["axes"], _d.today().strftime("%Y%m%d"),
                 os.path.basename(ref_p), os.path.basename(pos_p), ecartees,
                 pos.get("groupes"))
    open(sortie, "w", encoding="utf-8").write(txt)
    print(f"{sortie} — {len(gardees)} ligne(s), {ecartees} écartée(s), "
          f"{len(anomalies)} anomalie(s) de jointure")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
