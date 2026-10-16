#!/usr/bin/env node
// liasse2docx.js — Word d'une liasse d'amendements à partir de son markdown.
// Usage : node liasse2docx.js entree.md sortie.docx
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, PageBreak, HeadingLevel,
  convertInchesToTwip, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
} = require('docx');

const [, , SRC, OUT] = process.argv;
const POLICE = 'Garamond', CORPS = 22, INTERLIGNE = 276, LARGEUR = 9072;
const NB = ' ';
const SUP = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9' };

// Typographie : insécables, guillemets, séparateurs de milliers.
function typo(s) {
  return s
    .replace(/ /g, NB)
    .replace(/ ([:;!?»])/g, `${NB}$1`)
    .replace(/« /g, `«${NB}`)
    .replace(/(\d) (?=\d{3}(?!\d))/g, `$1${NB}`)
    .replace(/(\d) (?=\d{3}(?!\d))/g, `$1${NB}`)
    .replace(/(\d) %/g, `$1${NB}%`)
    .replace(/n° /g, `n°${NB}`);
}

// Runs : gras, italique, exposants (chiffres en exposant Unicode, ordinaux).
function runs(texte, base = {}) {
  const out = [];
  const push = (t, o = {}) => {
    // ordinaux et appels de note
    const re = /(\d+)(er|re|ers|res|e|es)\b|([⁰¹²³⁴⁵⁶⁷⁸⁹]+)/g;
    let pos = 0, m;
    while ((m = re.exec(t)) !== null) {
      if (m.index > pos) out.push(new TextRun({ text: t.slice(pos, m.index), ...base, ...o }));
      if (m[3]) out.push(new TextRun({ text: [...m[3]].map((c) => SUP[c]).join(''), superScript: true, ...base, ...o }));
      else { out.push(new TextRun({ text: m[1], ...base, ...o })); out.push(new TextRun({ text: m[2], superScript: true, ...base, ...o })); }
      pos = re.lastIndex;
    }
    if (pos < t.length) out.push(new TextRun({ text: t.slice(pos), ...base, ...o }));
  };
  const t = typo(texte);
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g;
  let pos = 0, m;
  while ((m = re.exec(t)) !== null) {
    if (m.index > pos) push(t.slice(pos, m.index));
    if (m[0].startsWith('**')) push(m[0].slice(2, -2), { bold: true });
    else push(m[0].slice(1, -1), { italics: true });
    pos = re.lastIndex;
  }
  if (pos < t.length) push(t.slice(pos));
  if (!out.length) out.push(new TextRun({ text: '', ...base }));
  return out;
}

const corps = (t, o = {}) => new Paragraph({
  children: runs(t), alignment: o.align ?? AlignmentType.JUSTIFIED,
  spacing: { line: INTERLIGNE, after: 120 }, indent: o.indent ?? { firstLine: 431 }, keepLines: true,
});
const centre = (t, o = {}) => new Paragraph({
  children: runs(t, { smallCaps: !!o.sc, bold: !!o.b, size: o.size }),
  alignment: AlignmentType.CENTER, heading: o.heading,
  spacing: { before: o.before ?? 0, after: o.after ?? 120, line: INTERLIGNE },
  keepNext: o.keepNext ?? true, keepLines: true, pageBreakBefore: !!o.pb,
});

// Tableaux
const cellules = (l) => l.replace(/^\||\|$/g, '').split('|').map((c) => c.trim());
const estSep = (cs) => cs.every((c) => /^:?-{2,}:?$/.test(c));
function table(lignes) {
  const brut = lignes.map(cellules);
  const sep = brut.find(estSep);
  const rows = brut.filter((cs) => !estSep(cs));
  const nb = Math.max(...rows.map((r) => r.length));
  const droite = sep ? sep.map((c) => /-:$/.test(c)) : Array(nb).fill(false);
  const tete = rows[0].map((c) => c.toLowerCase());
  let parts;
  if (tete[0] === 'n°' && nb === 3) parts = [7, 30, 63];
  else if (tete[0] === 'programmes' && nb === 5) parts = [28, 18, 18, 18, 18];
  else parts = Array(nb).fill(100 / nb);
  const larg = parts.map((p) => Math.round((LARGEUR * p) / 100));
  const fil = (c) => ({ style: BorderStyle.SINGLE, size: 2, color: c });
  return new Table({
    width: { size: LARGEUR, type: WidthType.DXA }, columnWidths: larg,
    borders: { top: fil('B0AAA0'), bottom: fil('B0AAA0'), left: fil('B0AAA0'), right: fil('B0AAA0'),
      insideHorizontal: fil('D4CFC4'), insideVertical: fil('D4CFC4') },
    rows: rows.map((cs, i) => new TableRow({
      tableHeader: i === 0, cantSplit: true,
      children: Array.from({ length: nb }, (_, k) => new TableCell({
        width: { size: larg[k], type: WidthType.DXA },
        shading: i === 0 ? { type: ShadingType.CLEAR, fill: 'F2F0EB' } : undefined,
        margins: { top: 50, bottom: 50, left: 90, right: 90 },
        children: [new Paragraph({
          children: runs(cs[k] ?? '', { size: 19 }),
          alignment: droite[k] && i > 0 ? AlignmentType.RIGHT : AlignmentType.LEFT,
          spacing: { line: 240, after: 0 }, keepLines: true,
        })],
      })),
    })),
  });
}

// Lecture
const src = fs.readFileSync(SRC, 'utf8').replace(/\r\n/g, '\n');
const iSep = src.search(/\n---\n/);
const couverture = src.slice(0, iSep), reste = src.slice(iSep + 5);
const enfants = [];

couverture.split('\n').map((x) => x.trim()).filter(Boolean).forEach((l, k) => {
  const titre = l.startsWith('# ') ? l.slice(2) : (k === 0 && /^\*\*[^*]+\*\*$/.test(l) ? l.slice(2, -2) : null);
  if (titre !== null) enfants.push(centre(titre, { sc: true, b: true, size: 34, after: 360, keepNext: false }));
  else enfants.push(centre(l, { after: 240, keepNext: false }));
});
enfants.push(new Paragraph({ children: [new PageBreak()] }));

let tampon = [];
let premierAmdt = true;
const vider = () => { if (tampon.length) { enfants.push(table(tampon)); enfants.push(new Paragraph({ children: [], spacing: { after: 120 } })); tampon = []; } };

for (const brut of reste.split('\n')) {
  const l = brut.trim();
  if (l.startsWith('|')) { tampon.push(l); continue; }
  vider();
  if (!l || l === '---') continue;
  if (l.startsWith('## Amendement')) {
    enfants.push(centre(l.slice(3), { sc: true, b: true, before: 0, after: 200, heading: HeadingLevel.HEADING_2, pb: true }));
    premierAmdt = false; continue;
  }
  if (l.startsWith('## ')) { enfants.push(centre(l.slice(3), { sc: true, b: true, before: 360, after: 200, heading: HeadingLevel.HEADING_2 })); continue; }
  if (l.startsWith('# ')) { enfants.push(centre(l.slice(2), { sc: true, b: true, size: 30, after: 240 })); continue; }
  if (/^-{4,}$/.test(l)) { enfants.push(centre('————————————', { after: 200 })); continue; }
  if (l === 'AMENDEMENT' || l === 'présenté par' || l === 'ARTICLE ADDITIONNEL' || /^ARTICLE \d/.test(l)) {
    enfants.push(centre(l, { sc: true, b: true, before: l === 'AMENDEMENT' ? 0 : 120, after: 120 })); continue;
  }
  if (l === 'EXPOSÉ SOMMAIRE') { enfants.push(centre(l, { sc: true, b: true, before: 200, after: 140 })); continue; }
  if (/^APRÈS L’ARTICLE/.test(l)) { enfants.push(centre(l, { after: 200 })); continue; }
  enfants.push(corps(l));
}
vider();

const doc = new Document({
  creator: 'Résolution', title: src.split('\n')[0].replace(/^# /, ''),
  styles: { default: {
    document: { run: { font: POLICE, size: CORPS }, paragraph: { spacing: { line: INTERLIGNE } } },
    heading2: { run: { font: POLICE, size: CORPS, bold: true, color: '000000' } },
  } },
  sections: [{
    properties: { page: { margin: {
      top: convertInchesToTwip(1), bottom: convertInchesToTwip(1),
      left: convertInchesToTwip(1.1), right: convertInchesToTwip(1.1) } } },
    children: enfants,
  }],
});
Packer.toBuffer(doc).then((b) => { fs.writeFileSync(OUT, b); console.log(`${OUT} : ${enfants.length} blocs`); });
