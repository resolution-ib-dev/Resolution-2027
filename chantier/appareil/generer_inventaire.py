# -*- coding: utf-8 -*-
"""Inventaire des gagnants et des perdants.

Jointure du REF_doctrine et du référentiel des positions. Aucune valeur n'est
écrite ici : intitulés, chiffres, atténuations et ancres sont lus au REF ;
positions, catégories, échelles, natures, degrés, miroirs et raccroches sont lus
au référentiel des positions.

Classement primaire par catégorie de personne, secondaire par échelle. Chaque
ligne remonte à sa mesure : axe, levier, proposition, effet.

Usage : python3 generer_inventaire.py REF.json Positions.json sortie.html
"""
import json, sys, html as H

ECH_RANG = {"micro": 0, "méso": 1, "macro": 2, "": 3}
POS_RANG = {"perdant": 0, "capteur": 1, "gagnant": 2}
AUCUNE = "aucune, par construction"
RECONST = "reconstitution volontaire du flux"


# ------------------------------------------------------------------- indexation
def indexer(ref):
    """Index de tout objet du REF pouvant servir d'ancrage à une ligne."""
    idx = {}
    for a in ref["axes"]:
        ctx_a = {"axe": a["id"], "axe_t": a.get("intitule", "")}
        for l in a.get("leviers", []):
            ctx_l = dict(ctx_a, levier=l["id"], levier_t=l.get("intitule", ""))
            for p in l.get("propositions", []):
                ctx_p = dict(ctx_l, proposition=p["id"],
                             proposition_t=p.get("intitule", ""),
                             verbe=p.get("verbe", ""), ancre=p.get("ancre", ""))
                idx[p["id"]] = dict(ctx_p, type="proposition", enonce="",
                                    chiffre="", attenuation="", signe="",
                                    certitude="", nature_ref="",
                                    ne_fait_pas=p.get("ne_fait_pas", ""))
                for s in p.get("sous_items", []):
                    idx[s["id"]] = dict(ctx_p, type="sous-item",
                                        enonce=s.get("intitule", ""),
                                        chiffre=s.get("chiffre", ""),
                                        attenuation=s.get("hypothese", ""),
                                        signe="", certitude="", nature_ref="",
                                        ne_fait_pas="")
                for e in p.get("effets", []):
                    idx[e["id"]] = dict(ctx_p, type="effet",
                                        enonce=e.get("enonce", ""),
                                        chiffre=e.get("chiffre", ""),
                                        attenuation=e.get("attenuation", ""),
                                        signe=e.get("signe", ""),
                                        certitude=e.get("certitude", ""),
                                        nature_ref=e.get("nature", ""),
                                        beneficiaire_ref=e.get("beneficiaire", ""),
                                        ne_fait_pas="")
        for k, lib in (("gains_indirects", "gain indirect"),
                       ("effets_diagnostic", "diagnostic")):
            for e in a.get(k, []):
                idx[e["id"]] = dict(ctx_a, levier="", levier_t="",
                                    proposition="", proposition_t="", verbe="",
                                    ancre=e.get("ancre", ""), type=lib,
                                    enonce=e.get("enonce", ""),
                                    chiffre=e.get("chiffre", ""),
                                    attenuation=e.get("attenuation", ""),
                                    signe=e.get("signe", ""),
                                    certitude=e.get("certitude", ""),
                                    nature_ref="",
                                    beneficiaire_ref=e.get("beneficiaire", ""),
                                    ne_fait_pas="")
    return idx


def effets_du_ref(ref):
    ids = []
    for a in ref["axes"]:
        for l in a.get("leviers", []):
            for p in l.get("propositions", []):
                ids += [e["id"] for e in p.get("effets", [])]
        for k in ("gains_indirects", "effets_diagnostic"):
            ids += [e["id"] for e in a.get(k, [])]
    return ids


# ------------------------------------------------------------------- assemblage
def assembler(ref, pos, notes=None):
    notes = notes or {}
    idx = indexer(ref)
    for m in pos.get("ancrages_manuscrit", []):
        # Le texte vient du relevé des notes, jamais du référentiel des positions.
        cites = [notes[i] for i in m.get("notes", []) if i in notes]
        manquantes = [i for i in m.get("notes", []) if i not in notes]
        corps = m.get("libelle", "")
        if cites:
            corps += ' — ' + ' '.join(f'[{n["id"]}] {n["texte"]}' for n in cites)
        idx[m["id"]] = {"axe": "manuscrit", "axe_t": "", "levier": "", "levier_t": "",
                        "proposition": "", "proposition_t": "", "verbe": "",
                        "ancre": m["section"], "type": "passage du manuscrit",
                        "enonce": corps, "chiffre": "", "attenuation": "",
                        "signe": "+", "certitude": "", "nature_ref": "",
                        "beneficiaire_ref": "", "ne_fait_pas": "",
                        "notes_manquantes": manquantes}
        if manquantes:
            idx[m["id"]]["_alerte"] = manquantes
    cats = {c["id"]: c for c in pos["categories"]}
    lignes, anomalies = [], []

    brutes = [l for l in pos["lignes"] if l["position"]]
    ecartees = [l for l in pos["lignes"] if not l["position"]]

    # tri stable avant numérotation : catégorie, échelle, position, ancrage
    brutes.sort(key=lambda l: (l["categorie"], ECH_RANG.get(l["echelle"], 3),
                               POS_RANG.get(l["position"], 3), l["ancrage"]))
    cle = {}
    for i, l in enumerate(brutes, 1):
        l["id"] = f"L-{i:04d}"
        cle[f"{l['ancrage']}|{l['position']}|{l['categorie']}"] = l["id"]

    for l in brutes:
        a = idx.get(l["ancrage"])
        if a is None:
            anomalies.append(("ancrage introuvable au REF", l["id"], l["ancrage"]))
            a = {}
        l["ctx"] = a
        if l["categorie"] not in cats:
            anomalies.append(("catégorie hors nomenclature", l["id"], l["categorie"]))
        # grandeur : REF d'abord, dérivation ensuite
        l["grandeur"] = l["grandeur_derivee"] or a.get("chiffre", "")
        if not l["grandeur"]:
            anomalies.append(("effet muet : ni grandeur ni déclaration qualitative",
                              l["id"], l["ancrage"]))
        # résolution des renvois
        for champ in ("miroir", "raccroche"):
            v = l[champ]
            if v and v not in (AUCUNE, RECONST):
                if v not in cle:
                    anomalies.append((f"{champ} non résolu", l["id"], v))
                    l[champ + "_id"] = ""
                else:
                    l[champ + "_id"] = cle[v]
            else:
                l[champ + "_id"] = ""
        # RT-2
        if l["position"] == "gagnant" and not (l["miroir"] or "").strip():
            anomalies.append(("RT-2 : gain sans miroir nommé", l["id"], l["ancrage"]))
        if l["position"] in ("perdant", "capteur") and not (l["raccroche"] or "").strip():
            anomalies.append(("RT-2 : perte sans raccroche nommée", l["id"], l["ancrage"]))
        if l["position"] in ("perdant", "capteur") and not (l.get("justification") or "").strip():
            anomalies.append(("perte sans justification écrite", l["id"], l["ancrage"]))
        if (l["position"] in ("perdant", "capteur") and l["raccroche"] != AUCUNE
                and not (l.get("relais") or "").strip()):
            anomalies.append(("perte raccrochée sans relais", l["id"], l["ancrage"]))
        if l["raccroche"] == RECONST and not (l.get("relais") or "").strip():
            anomalies.append(("RT-3 : reconstitution annoncée sans voie nommée",
                              l["id"], l["ancrage"]))

    for m in pos.get("ancrages_manuscrit", []):
        for i in idx.get(m["id"], {}).get("notes_manquantes", []):
            anomalies.append(("note citée absente du relevé", m["id"], i))

    # couverture des effets du REF
    ancres = {l["ancrage"] for l in pos["lignes"]}
    non_couverts = [e for e in effets_du_ref(ref) if e not in ancres]
    return brutes, ecartees, anomalies, non_couverts, cats, idx


# ------------------------------------------------------------------------ rendu
CSS = """
:root{--enc:#1a1a1a;--pap:#fdfcfa;--fil:#d8d2c8;--gain:#1f5c3a;--perte:#8a2f22;
--capt:#6b5b3e;--gris:#6d6a64}
*{box-sizing:border-box}
body{margin:0;padding:2.2rem 1.4rem 5rem;background:var(--pap);color:var(--enc);
font:15px/1.55 Georgia,"Iowan Old Style",serif;max-width:64rem;margin-inline:auto}
h1{font-size:1.5rem;margin:0 0 .3rem;font-weight:600}
h2{font-size:1.1rem;margin:2.6rem 0 .6rem;padding-bottom:.25rem;
border-bottom:1px solid var(--fil)}
h3{font-size:.95rem;margin:1.4rem 0 .3rem;font-weight:600}
.meta{color:var(--gris);font-size:.84rem;margin:0 0 1.4rem}
table{border-collapse:collapse;width:100%;font-size:.83rem;margin:.5rem 0 1.4rem}
th,td{border-top:1px solid var(--fil);padding:.34rem .5rem;text-align:left;
vertical-align:top}
th{font-weight:600;color:var(--gris);font-size:.78rem}
td.num{text-align:right;white-space:nowrap}
code{font:.9em ui-monospace,Menlo,monospace;background:#f2eee7;padding:.05em .3em;
border-radius:2px}
.g{color:var(--gain);font-weight:600}
.p{color:var(--perte);font-weight:600}
.c{color:var(--capt);font-weight:600}
.eff{color:var(--gris);font-size:.8rem}
.just{display:block;margin-top:.3rem;font-size:.82rem}
.rel{display:block;margin-top:.2rem;font-size:.82rem;color:var(--gain);font-style:italic}
.chap{font-size:.85rem;margin:.4rem 0 .2rem}
.clos{font-size:.85rem;margin:.2rem 0 1.6rem;color:var(--gain);font-style:italic}
.ctrl{border:1px solid var(--fil);border-left:3px solid var(--capt);
padding:.8rem 1rem;margin:1.2rem 0;background:#faf7f2;font-size:.85rem}
.som{columns:3;font-size:.85rem;margin:.6rem 0 1.6rem}
.som a{color:var(--enc)}
footer{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--fil);
color:var(--gris);font-size:.8rem}
"""


def e(x):
    return H.escape(str(x or ""))


def rendre(brutes, ecartees, anomalies, non_couverts, cats, idx, ref_nom, date):
    o = ['<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">',
         '<title>Inventaire des gagnants et des perdants</title>',
         f'<style>{CSS}</style></head><body>']
    o.append('<h1>Inventaire des gagnants et des perdants</h1>')
    o.append(f'<p class="meta">Projeté depuis <code>{e(ref_nom)}</code> le {e(date)}. '
             f'{len(brutes)} lignes, {len(cats)} catégories. Classement par catégorie '
             f'de personne, puis par échelle. Chaque ligne remonte à sa mesure. '
             f'Aucune valeur n’est écrite dans ce document : tout est projeté.</p>')

    # sommaire
    par_cat = {}
    for l in brutes:
        par_cat.setdefault(l["categorie"], []).append(l)
    o.append('<div class="som">')
    ordre = sorted(par_cat)
    for cid in ordre:
        c = cats.get(cid, {"terme": cid})
        o.append(f'<a href="#{e(cid)}">{e(c["terme"])}</a> ({len(par_cat[cid])})<br>')
    o.append('</div>')

    # contrôles
    o.append('<div class="ctrl"><b>Contrôles</b><table>'
             '<tr><th>contrôle</th><th>résultat</th></tr>')
    for lib, n in (("lignes portant une position", len(brutes)),
                   ("gagnants", sum(1 for l in brutes if l["position"] == "gagnant")),
                   ("perdants", sum(1 for l in brutes if l["position"] == "perdant")),
                   ("capteurs", sum(1 for l in brutes if l["position"] == "capteur")),
                   ("pertes sans aucune voie de raccroche",
                    sum(1 for l in brutes if l["raccroche"] == AUCUNE)),
                   ("pertes portant une justification écrite",
                    sum(1 for l in brutes if l["position"] in ("perdant","capteur")
                        and (l.get("justification") or "").strip())),
                   ("pertes portant un relais en langue ordinaire",
                    sum(1 for l in brutes if l["position"] in ("perdant","capteur")
                        and (l.get("relais") or "").strip())),
                   ("pertes raccrochées par reconstitution volontaire (RT-3)",
                    sum(1 for l in brutes if l["raccroche"] == RECONST)),
                   ("lignes de degré complété, à arbitrer",
                    sum(1 for l in brutes if l["degre"] == "complété")),
                   ("effets écartés, sans position", len(ecartees)),
                   ("effets du REF sans aucune ligne", len(non_couverts)),
                   ("anomalies", len(anomalies))):
        o.append(f'<tr><td>{e(lib)}</td><td class="num">{n}</td></tr>')
    o.append('</table>')
    if anomalies:
        o.append('<table><tr><th>anomalie</th><th>ligne</th><th>objet</th></tr>')
        for t, i, v in anomalies:
            o.append(f'<tr><td>{e(t)}</td><td><code>{e(i)}</code></td>'
                     f'<td><code>{e(v)}</code></td></tr>')
        o.append('</table>')
    o.append('</div>')

    # corps
    for cid in ordre:
        c = cats.get(cid, {})
        o.append(f'<h2 id="{e(cid)}">{e(c.get("terme", cid))} '
                 f'<code>{e(cid)}</code></h2>')
        d = [e(c.get("definition", ""))]
        if c.get("effectif"):
            d.append(f'Effectif : {e(c["effectif"])}.')
        if c.get("population"):
            d.append(f'Population de rattachement : {e(c["population"])}.')
        if c.get("statut_ancre"):
            d.append(f'Ancre : {e(c["statut_ancre"])}'
                     + (f' — {e(c["source_ancre"])}' if c.get("source_ancre") else '') + '.')
        o.append('<p class="meta">' + ' '.join(d) + '</p>')

        lg = par_cat[cid]
        np_ = sum(1 for x in lg if x["position"] == "perdant")
        nc_ = sum(1 for x in lg if x["position"] == "capteur")
        ng_ = sum(1 for x in lg if x["position"] == "gagnant")
        chap = []
        if np_: chap.append(f'{np_} perte' + ('s' if np_ > 1 else ''))
        if nc_: chap.append(f'{nc_} rente supprimée' + ('s' if nc_ > 1 else ''))
        if ng_: chap.append(f'{ng_} gain' + ('s' if ng_ > 1 else ''))
        o.append('<p class="chap"><b>Ce que le projet déplace ici :</b> '
                 + ', '.join(chap) + '.</p>')
        o.append('<table><tr><th>ligne</th><th>position</th><th>échelle</th>'
                 '<th>nature</th><th>degré</th><th>effet et mesure</th>'
                 '<th>grandeur</th><th>miroir ou raccroche</th></tr>')
        for l in sorted(par_cat[cid],
                        key=lambda x: (POS_RANG.get(x["position"], 3),
                                       ECH_RANG.get(x["echelle"], 3))):
            ctx = l["ctx"]
            cls = {"gagnant": "g", "perdant": "p", "capteur": "c",
               "diagnostic": "d"}[l["position"]]
            chemin = ' › '.join(x for x in (ctx.get("axe"), ctx.get("levier"),
                                            ctx.get("proposition")) if x)
            if ctx.get("axe") == "manuscrit":
                chemin = 'manuscrit › ' + str(ctx.get("ancre", ""))
            enonce = ctx.get("enonce") or ctx.get("proposition_t") or ""
            mesure = (f'<code>{e(l["ancrage"])}</code> · {e(ctx.get("type",""))}'
                      f'<br><span class="eff">{e(enonce)}</span>'
                      f'<br><span class="eff">{e(chemin)} — '
                      f'{e(ctx.get("verbe",""))} {e(ctx.get("proposition_t",""))}</span>')
            if l.get("justification"):
                mesure += f'<br><span class="just">{e(l["justification"])}</span>'
            if l.get("relais"):
                mesure += f'<br><span class="rel">{e(l["relais"])}</span>'
            if l["note"]:
                mesure += f'<br><span class="eff">{e(l["note"])}</span>'
            renv = []
            if l["miroir"]:
                renv.append('miroir : ' + (f'<code>{e(l["miroir_id"])}</code>'
                                           if l["miroir_id"] else e(l["miroir"])))
            if l["raccroche"]:
                renv.append('raccroche : ' + (f'<code>{e(l["raccroche_id"])}</code>'
                                              if l["raccroche_id"] else e(l["raccroche"])))
            o.append(f'<tr><td><code>{e(l["id"])}</code></td>'
                     f'<td class="{cls}">{e(l["position"])}</td>'
                     f'<td>{e(l["echelle"])}</td><td>{e(l["nature"])}</td>'
                     f'<td>{e(l["degre"])}</td><td>{mesure}</td>'
                     f'<td>{e(l["grandeur"])}</td><td>{"<br>".join(renv)}</td></tr>')
        o.append('</table>')
        rel = [x["relais"] for x in lg if x.get("relais")]
        if rel:
            o.append(f'<p class="clos">{e(rel[0])}</p>')
        elif ng_:
            o.append('<p class="clos">Aucune perte n’est portée à cette catégorie : '
                     'elle ne figure ici qu’au titre de ses gains.</p>')
        else:
            o.append('<p class="clos">Rente supprimée, sans contrepartie prévue par '
                     'le projet. Le corpus l’assume.</p>')

    # écartés et non couverts
    if ecartees:
        o.append('<h2>Effets écartés, sans position</h2><table>'
                 '<tr><th>ancrage</th><th>motif</th></tr>')
        for l in ecartees:
            o.append(f'<tr><td><code>{e(l["ancrage"])}</code></td>'
                     f'<td>{e(l["note"])}</td></tr>')
        o.append('</table>')
    if non_couverts:
        o.append('<h2>Effets du référentiel sans aucune ligne</h2>'
                 '<p class="meta">Chacun est soit un énoncé rhétorique sans '
                 'transfert, soit une position manquante.</p><table>'
                 '<tr><th>effet</th><th>énoncé</th></tr>')
        for i in non_couverts:
            o.append(f'<tr><td><code>{e(i)}</code></td>'
                     f'<td class="eff">{e(idx.get(i,{}).get("enonce",""))[:180]}</td></tr>')
        o.append('</table>')

    o.append('<footer>[interne] Dérivé du <code>REF_doctrine</code> et du '
             'référentiel des positions. Ne se corrige pas à la main : se '
             'régénère. Les lignes de degré <i>complété</i> appellent arbitrage '
             'des auteurs avant sortie externe.</footer></body></html>')
    return '\n'.join(o), anomalies


def main(argv):
    if len(argv) < 5:
        print("usage : generer_inventaire.py REF.json Positions.json Notes.json sortie.html")
        return 2
    ref = json.load(open(argv[1], encoding="utf-8"))
    pos = json.load(open(argv[2], encoding="utf-8"))
    notes = {n["id"]: n for n in json.load(open(argv[3], encoding="utf-8"))["notes"]}
    import subprocess
    date = subprocess.check_output(["date", "+%Y%m%d"]).decode().strip()
    b, ec, an, nc, cats, idx = assembler(ref, pos, notes)
    doc, an = rendre(b, ec, an, nc, cats, idx, argv[1].split('/')[-1], date)
    open(argv[4], "w", encoding="utf-8").write(doc)
    print(f"{argv[4]} écrit — {len(b)} lignes, {len(cats)} catégories")
    print(f"  gagnants {sum(1 for l in b if l['position']=='gagnant')} · "
          f"perdants {sum(1 for l in b if l['position']=='perdant')} · "
          f"capteurs {sum(1 for l in b if l['position']=='capteur')}")
    print(f"  {len(an)} anomalie(s), {len(nc)} effet(s) du REF sans ligne")
    for t, i, v in an:
        print(f"    {t} — {i} — {v}")
    return 1 if any(a[0].startswith("RT-2") or "non résolu" in a[0]
                    or "introuvable" in a[0] for a in an) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
