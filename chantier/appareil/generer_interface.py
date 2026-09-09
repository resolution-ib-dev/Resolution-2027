# -*- coding: utf-8 -*-
"""Interface « Où est-ce que je me situe ». Même projection que l'extrait.

Le document se lit dans l'ordre de la doctrine. L'interface se parcourt par
personne. Les deux niveaux de lecture coexistent et se tiennent ensemble : ils
sortent de la même projection, aucune valeur n'est réécrite ici.

Usage : python3 generer_interface.py donnees.json sortie.html
"""
import json
import sys

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Archivo+Black&display=swap');
/* Palette relevée sur le visuel du site : brique, or, crème. */
:root{
  --brique:#b1390f; --brique-f:#8e2c0a; --or:#ffd249; --creme:#fffdf1;
  --creme-t:rgba(255,253,241,.72); --creme-b:rgba(255,253,241,.18);
  --vert:#7dc9a0;
}
*{box-sizing:border-box}
body{margin:0;color:var(--creme);
background:
 repeating-linear-gradient(90deg,rgba(255,210,73,.05) 0 2px,transparent 2px 9px),
 var(--brique);
font:16px/1.6 Archivo,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:62rem;margin:0 auto;padding:3rem 1.2rem 6rem}

h1{font-family:'Archivo Black',Archivo,sans-serif;
font-size:clamp(2.4rem,7vw,4.6rem);line-height:.92;margin:0 0 .8rem;
letter-spacing:-.025em;text-transform:uppercase;color:var(--creme)}
h1 em{font-style:normal;color:var(--or)}
.sous{color:var(--creme-t);font-size:1.05rem;margin:0 0 2.4rem;max-width:36rem}
.mono{font-family:Archivo,sans-serif}

.compteurs{display:grid;grid-template-columns:repeat(3,1fr);gap:.6rem;
margin:0 0 1rem}
.k{padding:1rem 1.1rem;border:1px solid var(--creme-b)}
.k b{display:block;font-family:'Archivo Black',sans-serif;font-size:2.1rem;
line-height:1;letter-spacing:-.02em}
.k span{display:block;margin-top:.4rem;font-size:.66rem;letter-spacing:.16em;
text-transform:uppercase;color:var(--creme-t);font-weight:600}
.k.g b{color:var(--creme)} .k.p b{color:var(--or)} .k.c b{color:var(--or)}

.barre{display:flex;height:6px;margin:0 0 2.6rem}
.barre i{display:block}
.barre .bg{background:var(--creme)} .barre .bp{background:var(--or)}
.barre .bc{background:rgba(255,210,73,.45)}

h2{font-size:.68rem;letter-spacing:.22em;text-transform:uppercase;
color:var(--or);font-weight:700;margin:2.8rem 0 .9rem}

#q{width:100%;padding:.9rem 1rem;font:inherit;font-size:1rem;
border:1px solid var(--creme-b);background:rgba(0,0,0,.12);
color:var(--creme);margin:0 0 1.1rem}
#q::placeholder{color:rgba(255,253,241,.45)}
#q:focus{outline:none;border-color:var(--or)}

.puces{display:flex;flex-wrap:wrap;gap:.35rem;margin:0 0 1.8rem}
.puce{padding:.42rem .85rem;border:1px solid var(--creme-b);background:none;
cursor:pointer;font:inherit;font-size:.85rem;color:var(--creme);
transition:.12s}
.puce:hover{border-color:var(--or);color:var(--or)}
.puce[aria-pressed="true"]{background:var(--or);color:var(--brique-f);
border-color:var(--or);font-weight:600}
.puce .n{font-size:.72rem;opacity:.6;margin-left:.45rem;font-weight:600}

.groupe{margin:0 0 2rem}
.gt{font-family:'Archivo Black',sans-serif;font-size:1.05rem;margin:0 0 .15rem;
text-transform:uppercase;letter-spacing:-.01em;color:var(--or)}
.gc{margin:0 0 .7rem;font-size:.9rem;color:var(--creme-t)}
.cases{display:grid;grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));
gap:.45rem}
.tuile{text-align:left;padding:.85rem .95rem;border:1px solid var(--creme-b);
background:none;cursor:pointer;font:inherit;color:var(--creme);transition:.12s}
.tuile:hover{border-color:var(--or)}
.tuile[aria-pressed="true"]{background:var(--creme);color:var(--brique-f);
border-color:var(--creme)}
.tuile .t{font-weight:600;display:block;margin-bottom:.35rem;font-size:.98rem}
.tuile .m{font-size:.72rem;letter-spacing:.09em;text-transform:uppercase;
font-weight:600;opacity:.75}
.tuile .m .vg,.tuile .m .vp,.tuile .m .vc{color:var(--or)}
.tuile[aria-pressed="true"] .m{opacity:.6}
.tuile[aria-pressed="true"] .m .vg,
.tuile[aria-pressed="true"] .m .vp,
.tuile[aria-pressed="true"] .m .vc{color:inherit}

.fiche{margin:1.6rem 0 0;padding:1.8rem 1.9rem;background:var(--creme);
color:var(--brique-f)}
.fiche h3{font-family:'Archivo Black',sans-serif;font-size:1.9rem;margin:0 0 .3rem;
text-transform:uppercase;letter-spacing:-.02em;line-height:1}
.fiche .eff{font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;
font-weight:700;color:var(--brique);margin:0 0 .9rem}
.fiche .def{color:rgba(142,44,10,.72);font-size:.95rem;margin:0 0 1.3rem}
ul{list-style:none;margin:.6rem 0 0;padding:0}
li{margin:1rem 0;padding-left:1.7rem;position:relative}
li .s{position:absolute;left:0;top:-.05rem;font-family:'Archivo Black',sans-serif;
font-size:1.05rem;line-height:1.5}
li.gain .s{color:var(--brique)} li.perte .s{color:#8e2c0a}
li.capt .s{color:#8e2c0a}
li.diag .s{color:rgba(142,44,10,.45)}
li.diag .et{color:rgba(142,44,10,.55)}
li .et{display:block;font-size:.66rem;letter-spacing:.17em;
text-transform:uppercase;font-weight:700;color:var(--brique);
margin-bottom:.2rem}
li.perte .et,li.capt .et{color:#8e2c0a}
li .j{display:block;margin-top:.35rem;color:rgba(142,44,10,.78);font-size:.95rem}
li .r{display:block;margin-top:.45rem;padding:.5rem .8rem;
background:rgba(177,57,15,.09);border-left:3px solid var(--brique);
color:var(--brique-f);font-size:.95rem;font-weight:500}
li .d{display:block;margin-top:.45rem;padding:.5rem .8rem;
background:rgba(142,44,10,.1);border-left:3px solid #8e2c0a;
color:var(--brique-f);font-size:.95rem}
.vide{color:var(--creme-t);padding:2rem 0}
footer{margin-top:4rem;padding-top:1.2rem;border-top:1px solid var(--creme-b);
color:rgba(255,253,241,.5);font-size:.78rem}
@media(max-width:34rem){.compteurs{grid-template-columns:1fr}
.fiche{padding:1.3rem 1.2rem}}
"""

JS = """
const D = DONNEES;
const $ = s => document.querySelector(s);
let axe = null, cat = null, q = "";

const SIGNE = {gagnant:"+", perdant:"\\u2212", capteur:"\\u00d7",
  diagnostic:"\\u00b7"};
const ETIQUETTE = {gagnant:"Vous gagnez", perdant:"Vous perdez",
  capteur:"Rente supprim\\u00e9e", diagnostic:"Aujourd\\u2019hui"};
const CL = {gagnant:"gain", perdant:"perte", capteur:"capt",
  diagnostic:"diag"};
// La position diagnostic décrit l'état présent : elle sort après les effets du
// plan et ne se compte pas avec eux.
const ORD = {perdant:0, capteur:1, gagnant:2, diagnostic:3};

// L'ordre d'une fiche suit la chaîne du manuscrit : les promesses en tête et
// dans leur ordre, puis les axes de la doctrine, puis le chiffré avant le
// qualitatif. L'alphabet ne commande rien.
function rangLigne(l){
  const p = D.promesses.indexOf(l.n);
  return [ORD[l.p],
          p < 0 ? D.promesses.length : p,
          parseInt((l.a || "").slice(1), 10) || 99,
          l.g ? 0 : 1];
}

function esc(s){const d=document.createElement("div");d.textContent=s||"";
  return d.innerHTML;}

// Les termes vivent en minuscule au référentiel. À l'affichage ce sont des
// intitulés : capitale initiale, casse conservée pour le reste.
function cap(s){
  s = s || "";
  return s.charAt(0).toLocaleUpperCase("fr") + s.slice(1);
}

function lignesDe(c){
  return D.lignes.filter(l => l.c === c)
    .sort((a, b) => {
      const x = rangLigne(a), y = rangLigne(b);
      for (let i = 0; i < x.length; i++) if (x[i] !== y[i]) return x[i] - y[i];
      return 0;
    });
}

function bilan(c){
  const n = {gagnant:0, perdant:0, capteur:0, diagnostic:0};
  lignesDe(c).forEach(l => n[l.p]++);
  return n;
}

function catsVisibles(){
  let ids = D.groupes.reduce((a, g) => a.concat(g.categories), [])
    .filter(c => D.cats[c]);
  if (axe) {
    const ok = new Set(D.lignes.filter(l => l.a === axe).map(l => l.c));
    ids = ids.filter(c => ok.has(c));
  }
  if (q) {
    const t = q.toLowerCase();
    ids = ids.filter(c => {
      const k = D.cats[c];
      if ((k.t + " " + k.d).toLowerCase().includes(t)) return true;
      return lignesDe(c).some(l =>
        (l.e + " " + l.j + " " + l.r).toLowerCase().includes(t));
    });
  }
  return ids;
}

function rendreAxes(){
  const n = {};
  D.lignes.forEach(l => n[l.a] = (n[l.a]||0)+1);
  const h = D.axes.filter(a => n[a.id]).map(a =>
    `<button class="puce" data-axe="${a.id}" aria-pressed="${axe===a.id}">`+
    `${esc(a.t)}<span class="n">${n[a.id]}</span></button>`).join("");
  $("#axes").innerHTML =
    `<button class="puce" data-axe="" aria-pressed="${axe===null}">Tout</button>`+h;
}

function tuile(c){
  {
    const k = D.cats[c], b = bilan(c), m = [];
    if (b.gagnant) m.push(`<span class="vg">${b.gagnant} gain`+
      `${b.gagnant > 1 ? "s" : ""}</span>`);
    if (b.perdant) m.push(`<span class="vp">${b.perdant} perte`+
      `${b.perdant > 1 ? "s" : ""}</span>`);
    if (b.capteur) m.push(`<span class="vc">${b.capteur} rente`+
      `${b.capteur > 1 ? "s" : ""} supprim\\u00e9e${b.capteur > 1 ? "s" : ""}`+
      `</span>`);
    return `<button class="tuile" data-cat="${c}" aria-pressed="${cat===c}">`+
      `<span class="t">${esc(cap(k.t))}</span>`+
      `<span class="m">${m.join(" \\u00b7 ")}`+
      `${k.e ? " \\u00b7 " + esc(k.e) : ""}</span>`+
      `</button>`;
  }
}

// La grille suit l'ordre de lecture du référentiel : du plus large au plus
// particulier, les rentes en dernier.
function rendreGrille(){
  const vus = new Set(catsVisibles());
  if (!vus.size){
    $("#grille").innerHTML = '<p class="vide">Aucune situation ne répond à '+
      'cette recherche.</p>';
    return;
  }
  $("#grille").innerHTML = D.groupes.map(g => {
    const ids = g.categories.filter(c => vus.has(c));
    if (!ids.length) return "";
    return `<section class="groupe"><h3 class="gt">${esc(g.titre)}</h3>`+
      `<p class="gc">${esc(g.chapeau)}</p>`+
      `<div class="cases">${ids.map(tuile).join("")}</div></section>`;
  }).join("");
}

function rendreFiche(){
  if (!cat){ $("#fiche").innerHTML = ""; return; }
  const k = D.cats[cat];
  const ls = lignesDe(cat).filter(l => !axe || l.a === axe);
  const corps = ls.map(l => {
    let o = `<li class="${CL[l.p]}"><span class="s">${SIGNE[l.p]}</span>`;
    o += `<span class="et">${ETIQUETTE[l.p]}</span>`;
    o += esc(cap(l.e || l.j));
    if (l.j && l.e) o += `<span class="j">${esc(l.j)}</span>`;
    if (l.k) o += `<span class="j">${esc(l.k)}</span>`;
    if (l.r) o += `<span class="r">${esc(l.r)}</span>`;
    else if (l.dur) o += `<span class="d">Rien ne se reconstitue ici, et le `+
      `plan l\\u2019assume.</span>`;
    return o + "</li>";
  }).join("");
  $("#fiche").innerHTML =
    `<div class="fiche"><h3>${esc(cap(k.t))}</h3>`+
    (k.e ? `<p class="eff">${esc(k.e)}</p>` : "")+
    (k.d ? `<p class="def">${esc(k.d)}</p>` : "")+
    `<ul>${corps}</ul></div>`;
  $("#fiche").scrollIntoView({behavior:"smooth", block:"nearest"});
}

function rendreCompteurs(){
  const src = (axe ? D.lignes.filter(l => l.a === axe) : D.lignes)
    .filter(l => l.p !== "diagnostic");
  const n = {gagnant:0, perdant:0, capteur:0};
  src.forEach(l => n[l.p]++);
  const t = n.gagnant + n.perdant + n.capteur || 1;
  $("#kg").textContent = n.gagnant;
  $("#kp").textContent = n.perdant;
  $("#kc").textContent = n.capteur;
  $("#bg").style.width = (100*n.gagnant/t)+"%";
  $("#bp").style.width = (100*n.perdant/t)+"%";
  $("#bc").style.width = (100*n.capteur/t)+"%";
}

function tout(){ rendreAxes(); rendreCompteurs(); rendreGrille(); rendreFiche(); }

document.addEventListener("click", ev => {
  const a = ev.target.closest("[data-axe]");
  if (a){ axe = a.dataset.axe || null; tout(); return; }
  const c = ev.target.closest("[data-cat]");
  if (c){ cat = (cat === c.dataset.cat) ? null : c.dataset.cat; tout(); }
});
$("#q").addEventListener("input", ev => { q = ev.target.value.trim();
  rendreGrille(); });
tout();
"""

GABARIT = """<!DOCTYPE html><html lang="fr"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ce que j’y gagne</title>
<style>{css}</style>
<div class="wrap">
<h1>Ce que <em>j&rsquo;y gagne</em></h1>
<p class="sous">Choisissez votre situation. Vous verrez ce que le plan vous
rend, ce qu&rsquo;il vous retire, et par quelle voie ce qui vous est retiré vous
revient ailleurs.</p>

<div class="compteurs">
  <div class="k g"><b id="kg">0</b><span>Ce que vous gagnez</span></div>
  <div class="k p"><b id="kp">0</b><span>Ce que vous perdez</span></div>
  <div class="k c"><b id="kc">0</b><span>Rentes supprim&eacute;es</span></div>
</div>
<div class="barre"><i class="bg" id="bg"></i><i class="bp" id="bp"></i>
<i class="bc" id="bc"></i></div>

<h2>Par domaine</h2>
<div class="puces" id="axes"></div>

<h2>Votre situation</h2>
<input id="q" type="search" placeholder="Rechercher : locataire, retraite,
imp&ocirc;t, salaire&hellip;" autocomplete="off">
<div class="grille" id="grille"></div>
<div id="fiche"></div>

<footer>[interne] Interface projet&eacute;e le {date} depuis
{pos}, sur {ref}. {n} lignes, {c} cat&eacute;gories.
Justifications et relais lus au r&eacute;f&eacute;rentiel, jamais
r&eacute;&eacute;crits. Bloc retirable en une op&eacute;ration.</footer>
</div>
<script>const DONNEES = {data};</script>
<script>{js}</script>
</html>"""


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    d = json.load(open(argv[1], encoding="utf-8"))
    from datetime import date
    txt = GABARIT.format(
        css=CSS, js=JS, data=json.dumps(d, ensure_ascii=False),
        date=date.today().strftime("%Y%m%d"),
        pos="Positions_20260820_v11.json", ref="REF_doctrine_20260820_v20.json",
        n=len(d["lignes"]), c=len(d["cats"]))
    open(argv[2], "w", encoding="utf-8").write(txt)
    print(f"{argv[2]} — {len(d['lignes'])} lignes, {len(d['cats'])} catégories")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
