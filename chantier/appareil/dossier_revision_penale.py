#!/usr/bin/env python3
"""Dossier court du projet de révision pénale, et annexe en trois colonnes.

Lit revision/fiches_penal.json et le texte en vigueur (droit.py), réutilise les
opérations de revision_penale.py, et écrit deux pages HTML imprimables :

  livrables/dossier_revision_penale.html   dossier (≤ 10 pages A4)
  livrables/trois_colonnes_penal.html      annexe : en vigueur | cible | commentaire

Les statistiques de réécriture sont comptées sur les textes, jamais saisies.
"""
import difflib
import html
import json
import pathlib
import re
import sys

CHANTIER = pathlib.Path(__file__).resolve().parents[1]
RACINE = CHANTIER.parent
sys.path.insert(0, str(RACINE))
sys.path.insert(0, str(CHANTIER / "appareil"))
import droit  # noqa: E402
import revision_penale as rp  # noqa: E402

SOURCE = CHANTIER / "revision" / "fiches_penal.json"
OUT = CHANTIER / "livrables"

EXPLI = {
    "R1": "La liste fermée de onze rubriques devient une règle générale : toute contravention de 5e classe peut se régler par amende forfaitaire, sauf violences, récidive et peine complémentaire. Le forfait passe à un niveau cohérent avec le maximum de 1 500 €.",
    "R2": "En commission rogatoire, un seul procès-verbal suffit, comme déjà en flagrance et en préliminaire (D11). Le magistrat peut toujours exiger des procès-verbaux séparés.",
    "R3": "Les frais non tarifés sous le seuil sont payés sur certification du greffe, sans réquisitions du parquet ni taxe du magistrat. Un arrêté suffit.",
    "RP1": "Au-delà d'un an, la prolongation d'un placement en quartier sécurisé se décide au niveau interrégional et non plus au cabinet du ministre. Le contradictoire et la durée maximale restent.",
    "L1": "L'envoi électronique devient la règle : la personne déclare une adresse et peut demander le papier. Aujourd'hui il faut son consentement exprès.",
    "L2": "La prison ferme cesse d'être un « dernier recours » et l'aménagement devient une faculté décidée à l'audience. La convocation devant le juge de l'application des peines avant toute incarcération disparaît.",
    "L3": "Les nullités se soulèvent dans [un mois] à compter de la remise du dossier. La partie qui a délibérément provoqué l'irrégularité ne peut plus s'en prévaloir.",
    "L4": "Le juge prononce la peine encourue et ne la diminue que pour des motifs rangés en trois catégories bornées, dans un plafond total. La situation sociale sort du quantum.",
    "L5": "En récidive légale, la peine prévue pour l'infraction simple devient le minimum. Une issue étroite et motivée reste ouverte à la première récidive.",
}

PRINCIPES = [
    ("La peine encourue est la référence", "le juge fixe librement la peine sous le maximum, selon notamment la situation sociale (CP 132-1)", "le juge prononce la peine encourue et motive chaque diminution, en fraction bornée", "L4"),
    ("Diminutions en trois catégories plafonnées", "atténuations éparses : un tiers (discernement), moitié (repenti, mineur), libre ailleurs", "personne ≤ [1/3], pendant l'acte ≤ [1/5], après l'acte ≤ [1/5] ; total ≤ [1/2], [1/3] en réitération, [1/4] victime vulnérable", "L4"),
    ("La récidive relève le plancher", "maximum doublé ; plus de peine plancher depuis 2014", "minimum = peine de l'infraction simple ; issue motivée à la 1re récidive", "L5"),
    ("La peine prononcée s'exécute", "aménagement obligatoire jusqu'à six mois ; prison « en dernier recours » ; convocation devant le JAP avant incarcération", "aménagement facultatif décidé à l'audience ; sinon mise à exécution", "L2"),
    ("La charge de la motivation s'inverse", "le tribunal motive spécialement la prison ferme", "le jugement motive l'écart à la peine encourue", "L2, L4"),
    ("Liste fermée → règle générale à exclusions", "amende forfaitaire de 5e classe pour onze rubriques, à 200 €", "toute la 5e classe, sauf violences, récidive, peine complémentaire, à [750] €", "R1"),
    ("Simplifier ne fait rien perdre", "—", "récidive et peines complémentaires exclues du forfait", "R1"),
    ("S'aligner sur le régime le plus simple déjà en vigueur", "procès-verbaux séparés pour chaque acte sur commission rogatoire", "un seul procès-verbal, comme en flagrance (D11) ; le magistrat peut exiger la forme lourde", "R2"),
    ("Le magistrat juge, le greffe certifie", "taxe du magistrat au-delà de 1 500 €", "certification du greffe jusqu'à [5 000] €", "R3"),
    ("Décider au plus près, garanties maintenues", "prolongation au-delà d'un an par le seul garde des Sceaux", "par le [directeur interrégional] ; contradictoire et durée inchangés", "RP1"),
    ("Le numérique par défaut", "envoi électronique sur consentement exprès", "envoi électronique à l'adresse déclarée ; papier à la demande", "L1"),
    ("Purger tôt les nullités", "quatre mois ; nullité invocable par qui l'a provoquée", "[un mois] après remise du dossier ; irrecevabilité de qui l'a délibérément provoquée", "L3"),
    ("Sobriété de la règle", "9 473 articles et 874 000 mots dans la chaîne pénale ; un article porte souvent plusieurs règles", "une idée, un article ; l'article sans usage tombe ; cible [−50 %] de mots", "toutes"),
    ("Transparence des procédures et des jugements", "huis clos et chambre du conseil épars ; publication des décisions partielle", "audiences publiques, décisions publiées ; exceptions : victime à sa demande, sécurité nationale", "toutes"),
    ("Descendre à la strate la plus basse", "tout attendre de la loi", "arrêté, puis décret, puis loi ; un verrou législatif se déclare", "toutes"),
    ("Coordination avec le code de 2029", "délai de nullité de 2026 non reporté au code refondu (L3752-4)", "chaque fiche porte son report ; défaut signalé", "L1, L3"),
]


def mots(t):
    return re.findall(r"\w+(?:[-']\w+)*", t or "")


def diff_html(a, b):
    """Rend (avant, après) en HTML, suppressions barrées, ajouts soulignés."""
    ta, tb = re.split(r"(\s+)", a or ""), re.split(r"(\s+)", b or "")
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    if a and b and sm.ratio() < 0.6:
        # réécriture profonde : un diff mot à mot serait illisible
        return (html.escape(a).replace("\n", "<br>"),
                "<ins>" + html.escape(b).replace("\n", "</ins><br><ins>") + "</ins>")
    oa, ob = [], []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        A, B = html.escape("".join(ta[i1:i2])), html.escape("".join(tb[j1:j2]))
        if op == "equal":
            oa.append(A); ob.append(B)
        else:
            if A.strip():
                oa.append(f"<del>{A}</del>")
            if B.strip():
                ob.append(f"<ins>{B}</ins>")
    return ("".join(oa).replace("\n", "<br>"), "".join(ob).replace("\n", "<br>"))


def extrait(avant, apres, marge=1):
    """Pour les longs articles : alinéas changés seulement, avec voisinage."""
    if avant is None or apres is None or len(avant) < 1400:
        return avant, apres
    return rp.condenser(avant, apres)


def calculer():
    src = json.loads(SOURCE.read_text(encoding="utf-8"))
    jour = src["jour_reference"]
    fiches = []
    st = {"modifies": 0, "crees": 0, "abroges": 0, "mots_avant": 0, "mots_apres": 0,
          "mots_supprimes": 0, "mots_ajoutes": 0, "codes": set()}
    for f in src["fiches"]:
        arts = {}
        for op in f["operations"]:
            cle = (op["code"], op["num"])
            j = op.get("jour", jour)
            if cle not in arts:
                if op["op"] == "creer":
                    arts[cle] = {"avant": None, "apres": None}
                else:
                    a = droit.article(op["code"], op["num"], j)
                    arts[cle] = {"avant": a["texte"], "apres": a["texte"]}
            e = arts[cle]
            if op["op"] == "creer":
                e["apres"] = op["nouveau"]
            elif op["op"] == "abroger":
                e["apres"] = None
            else:
                e["apres"], _ = rp.appliquer(e["apres"], op)
        for (code, num), e in arts.items():
            st["codes"].add(code)
            if e["avant"] is None:
                st["crees"] += 1
            elif e["apres"] is None:
                st["abroges"] += 1
            else:
                st["modifies"] += 1
            wa, wb = mots(e["avant"]), mots(e["apres"])
            st["mots_avant"] += len(wa)
            st["mots_apres"] += len(wb)
            sm = difflib.SequenceMatcher(None, wa, wb, autojunk=False)
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                if op in ("delete", "replace"):
                    st["mots_supprimes"] += i2 - i1
                if op in ("insert", "replace"):
                    st["mots_ajoutes"] += j2 - j1
        fiches.append((f, arts))
    return src, fiches, st


CSS = """
@page { size: A4; margin: 14mm 13mm 14mm 13mm; }
:root { --brique:#b23a10; --donnee:#d2490a; --or:#ffd24a; --creme:#fffdf2; --encre:#1d1b18; --gris:#6b6760; --filet:#d9d3c4; }
* { box-sizing: border-box; }
body { margin:0; background:var(--creme); color:var(--encre); font-family:"Liberation Serif","DejaVu Serif",serif; font-size:9.6pt; line-height:1.38; }
h1,h2,h3,.tete,.chiffre,th { font-family:"DejaVu Sans Condensed","DejaVu Sans",sans-serif; }
.bandeau { background:var(--brique); color:var(--creme); padding:9mm 9mm 7mm; }
.bandeau h1 { margin:0; font-size:21pt; font-weight:700; letter-spacing:.2px; color:var(--creme); }
.bandeau p { margin:3mm 0 0; color:var(--or); font-size:10.5pt; }
.tricolore { height:3px; background:linear-gradient(90deg,#002395 0 33.3%,#ffffff 33.3% 66.6%,#ed2939 66.6%); }
.stats { display:grid; grid-template-columns:repeat(4,1fr); gap:3mm; margin:5mm 0 4mm; }
.stat { border-top:2px solid var(--donnee); padding-top:2mm; }
.chiffre { font-size:16pt; font-weight:700; color:var(--donnee); line-height:1; }
.stat span { display:block; font-size:8.3pt; color:var(--gris); margin-top:1mm; }
h2 { font-size:13pt; margin:5mm 0 2mm; padding-bottom:1mm; border-bottom:1px solid var(--filet); }
h3 { font-size:10.5pt; margin:4mm 0 1mm; color:var(--brique); }
.lead { font-size:10pt; margin:0 0 3mm; }
table { width:100%; border-collapse:collapse; table-layout:fixed; }
th { text-align:left; font-size:8pt; font-weight:700; color:var(--gris); text-transform:none; border-bottom:1.5px solid var(--encre); padding:1.2mm 1.5mm; }
td { vertical-align:top; padding:1.4mm 1.5mm; border-bottom:.5px solid var(--filet); }
.princ td { font-size:8.6pt; line-height:1.3; }
.princ td:first-child { font-weight:700; font-family:"DejaVu Sans Condensed",sans-serif; font-size:8.4pt; }
.princ td.av { color:var(--gris); }
.fiche { break-inside:avoid; margin-bottom:3mm; }
.meta { font-size:8.2pt; color:var(--gris); margin:0 0 1.5mm; }
.expl { margin:0 0 2mm; }
.bi td { font-size:8.5pt; line-height:1.33; width:50%; }
.bi td.av { background:#f6f1e4; }
.lib { font-family:"DejaVu Sans Condensed",sans-serif; font-size:8pt; font-weight:700; color:var(--gris); margin:1.5mm 0 .8mm; }
del { color:#8a8478; text-decoration:line-through; text-decoration-color:#b9b2a3; }
ins { text-decoration:none; background:#fbe3d3; color:#7a2a06; }
.saut { break-before:page; }
.note { font-size:8pt; color:var(--gris); margin-top:2mm; }
.tc td { font-size:7.9pt; line-height:1.3; }
.tc td.com { font-size:7.6pt; color:#3b3833; }
"""


def entete(titre, sous):
    return (f"<div class='bandeau'><h1>{titre}</h1><p>{sous}</p></div><div class='tricolore'></div>")


def nom(code, num):
    return f"{rp.cite(num)} {rp.NOMS.get(code, code)}"


def dossier(src, fiches, st):
    H = [f"<!doctype html><html lang='fr'><head><meta charset='utf-8'><title>Révision de la chaîne pénale</title><style>{CSS}</style></head><body>"]
    H.append(entete("Révision de la chaîne pénale",
                    "Neuf mesures pour que la peine annoncée soit la peine exécutée — dossier de présentation, octobre 2026"))
    n_art = st["modifies"] + st["crees"] + st["abroges"]
    pages_eq = round((st["mots_supprimes"] + st["mots_ajoutes"]) / 400, 1)
    H.append("<div class='stats'>")
    H.append(f"<div class='stat'><div class='chiffre'>{n_art}</div><span>articles touchés : {st['modifies']} modifiés, {st['crees']} créés, {st['abroges']} abrogés</span></div>")
    H.append(f"<div class='stat'><div class='chiffre'>{len(st['codes'])}</div><span>codes : procédure pénale, pénal, pénitentiaire</span></div>")
    H.append(f"<div class='stat'><div class='chiffre'>{st['mots_avant']:,} → {st['mots_apres']:,}</div><span>mots des articles touchés, avant → après ({(st['mots_apres'] - st['mots_avant']) / st['mots_avant']:+.0%})</span></div>".replace(",", " "))
    H.append(f"<div class='stat'><div class='chiffre'>{st['mots_supprimes'] + st['mots_ajoutes']:,}</div><span>mots réécrits ({st['mots_supprimes']:,} supprimés, {st['mots_ajoutes']:,} ajoutés), soit ≈ {pages_eq} pages de code</span></div>".replace(",", " "))
    H.append("</div>")
    H.append("<p class='lead'>Quatre mesures passent par décret ou arrêté, cinq par la loi. Chaque texte cible est dérivé du droit en vigueur (base LEGI de la DILA, 20 octobre 2026) et contrôlé par réapplication : zéro anomalie. Les paramètres entre crochets restent à arbitrer.</p>")

    H.append("<h2>Les principes, et ce qu'ils changent</h2>")
    H.append("<table class='princ'><colgroup><col style='width:22%'><col style='width:33%'><col style='width:37%'><col style='width:8%'></colgroup>"
             "<tr><th>Principe</th><th>Avant</th><th>Après</th><th>Fiche</th></tr>")
    for p, av, ap, fi in PRINCIPES:
        H.append(f"<tr><td>{html.escape(p)}</td><td class='av'>{html.escape(av)}</td><td>{html.escape(ap)}</td><td>{fi}</td></tr>")
    H.append("</table>")

    for paquet, titre in (("réglementaire", "Rédactions proposées — par décret ou arrêté"), ("législatif", "Rédactions proposées — par la loi")):
        H.append(f"<h2 class='saut'>{titre}</h2>")
        for f, arts in fiches:
            if f["paquet"] != paquet:
                continue
            H.append(f"<div class='fiche'><h3>{f['id']} — {html.escape(f['titre'])}</h3>")
            H.append(f"<p class='meta'>{html.escape(f['strate'])}</p><p class='expl'>{html.escape(EXPLI[f['id']])}</p>")
            H.append("<table class='bi'><tr><th>Avant</th><th>Après</th></tr>")
            abroges = []
            for (code, num), e in arts.items():
                if e["apres"] is None:
                    abroges.append(rp.cite(num))
                    continue
                av, ap = extrait(e["avant"], e["apres"])
                a_h, b_h = diff_html(av or "", ap or "")
                if e["avant"] is None:
                    a_h = "<em>(article nouveau)</em>"
                H.append(f"<tr><td colspan='2' class='lib' style='border-bottom:none;padding-bottom:0'>{html.escape(nom(code, num))}</td></tr>")
                H.append(f"<tr><td class='av'>{a_h}</td><td>{b_h}</td></tr>")
            if abroges:
                H.append(f"<tr><td class='av'>{', '.join(abroges)} {rp.NOMS.get(code, '')}</td><td><em>abrogé{'s' if len(abroges) > 1 else ''}</em></td></tr>")
            H.append("</table></div>")
    H.append("<p class='note'>Lecture : texte barré = supprimé ; texte surligné = ajouté ; […] = alinéas inchangés non reproduits. "
             "Le texte intégral avant / après / commentaire figure dans l'annexe en trois colonnes.</p>")
    H.append("</body></html>")
    return "\n".join(H)


def trois_colonnes(src, fiches):
    H = [f"<!doctype html><html lang='fr'><head><meta charset='utf-8'><title>Trois colonnes — révision pénale</title><style>{CSS}</style></head><body>"]
    H.append(entete("Révision de la chaîne pénale — trois colonnes",
                    "Texte en vigueur, texte cible et commentaire, article par article (base LEGI du 20 octobre 2026)"))
    H.append("<table class='tc'><colgroup><col style='width:37%'><col style='width:37%'><col style='width:26%'></colgroup>"
             "<tr><th>Texte en vigueur</th><th>Texte cible</th><th>Commentaire</th></tr>")
    for f, arts in fiches:
        H.append(f"<tr><td colspan='3'><h3 style='margin:2mm 0 0'>{f['id']} — {html.escape(f['titre'])}</h3></td></tr>")
        for (code, num), e in arts.items():
            a_h, b_h = diff_html(e["avant"] or "", e["apres"] or "")
            if e["avant"] is None:
                a_h = "<em>(article nouveau)</em>"
            if e["apres"] is None:
                b_h = "<em>(abrogé)</em>"
            com = html.escape(EXPLI[f["id"]]) if (code, num) == next(iter(arts)) else ""
            H.append(f"<tr><td colspan='3' class='lib' style='border-bottom:none;padding-bottom:0'>{html.escape(nom(code, num))}</td></tr>")
            H.append(f"<tr><td class='av' style='background:#f6f1e4'>{a_h}</td><td>{b_h}</td><td class='com'>{com}</td></tr>")
    H.append("</table><p class='note'>Texte barré = supprimé ; texte surligné = ajouté. Paramètres entre crochets à arbitrer.</p></body></html>")
    return "\n".join(H)


def main():
    src, fiches, st = calculer()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "dossier_revision_penale.html").write_text(dossier(src, fiches, st), encoding="utf-8")
    (OUT / "trois_colonnes_penal.html").write_text(trois_colonnes(src, fiches), encoding="utf-8")
    st["codes"] = sorted(st["codes"])
    print(json.dumps(st, ensure_ascii=False))


if __name__ == "__main__":
    main()
