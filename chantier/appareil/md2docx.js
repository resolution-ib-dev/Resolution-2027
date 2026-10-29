#!/usr/bin/env node
// md2docx.js — export docx d'un livrable Résolution rédigé en markdown.
// Usage : node md2docx.js entree.md sortie.docx [profil] [--nb] [--depot]
// Profils : pplc (défaut) · note · presentation
//
// Options :
//   --nb      noir et blanc : ni fond gris en tête de tableau, filets noirs
//   --depot   version déposable : le descripteur de travail porté sous un
//             intitulé d'article ne s'imprime pas
//
// Consignes de tableau, chacune sur sa propre ligne, juste avant le tableau
// qu'elle règle, et valables pour lui seul :
//   <!-- colonnes : 0.2, 0.5, 0.3 -->  largeurs relatives des colonnes ; leur
//                                       nombre doit égaler celui des colonnes,
//                                       sans quoi les largeurs par défaut valent
//   <!-- corps : 16 -->                 corps du texte du tableau, en demi-points
//                                       (défaut 19, soit 9,5 pt)
//
// Conventions markdown reconnues :
//   bloc avant le premier « --- »  → page de titre, centrée
//   # TITRE                        → grand titre centré, saut de page avant
//   ## TITRE ...                   → intitulé de division, centré, petites capitales
//   ### Chapitre ...               → sous-division, centrée, italique
//   **Article 1er**                → intitulé d'article, centré, petites capitales
//   *[...]*                        → descripteur de travail, ignoré à l'impression
//   *texte*                        → italique en ligne
//   ligne commençant par «         → texte cité, en retrait
//   I. — / 1° / a)                 → subdivision, retrait de première ligne
//   ---                            → séparateur, saut de page en profil pplc

const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, PageBreak,
  convertInchesToTwip, LevelFormat,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  TableOfContents, HeadingLevel,
} = require('docx');

const LARGEUR_TABLE = 9072;   // DXA — 6,3 pouces utiles

const [, , SRC, OUT, PROFIL = 'pplc'] = process.argv;
const DEPOT = process.argv.includes('--depot');   // retire les descripteurs de travail
const NB = process.argv.includes('--nb');         // noir et blanc : ni fond ni filet gris
if (!SRC || !OUT) {
  console.error('usage : node md2docx.js entree.md sortie.docx [pplc|note|presentation]');
  process.exit(1);
}

const POLICE = 'Garamond';
const CORPS = 22;        // demi-points → 11 pt
const INTERLIGNE = 276;  // 1,15 ligne

// ---------------------------------------------------------------- runs en ligne
// Découpe *italique* et ** gras ** en runs. Ne touche pas aux guillemets.
// Appels de note : les exposants Unicode 5 à 9 manquent au sous-ensemble latin
// d'EB Garamond et tombaient en DejaVu. On les rend en exposant de la police.
// Corrigé le 20261016, après refus de la liasse P2 à la publication.
const EXPOSANTS = { '\u00b9': '1', '\u00b2': '2', '\u00b3': '3', '\u2074': '4',
  '\u2075': '5', '\u2076': '6', '\u2077': '7', '\u2078': '8', '\u2079': '9' };
function decouperExposants(texte, base, pousser) {
  const re = /[\u00b9\u00b2\u00b3\u2074-\u2079]+/g;
  let pos = 0, m;
  while ((m = re.exec(texte)) !== null) {
    if (m.index > pos) pousser(new TextRun({ text: texte.slice(pos, m.index), ...base }));
    const chiffres = [...m[0]].map((c) => EXPOSANTS[c]).join('');
    pousser(new TextRun({ text: chiffres, superScript: true, ...base }));
    pos = re.lastIndex;
  }
  if (pos < texte.length) pousser(new TextRun({ text: texte.slice(pos), ...base }));
  return pos > 0;
}

function runs(texte, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g;
  let pos = 0, m;
  while ((m = re.exec(texte)) !== null) {
    if (m.index > pos) decouperExposants(texte.slice(pos, m.index), base, (r) => out.push(r));
    const brut = m[0];
    if (brut.startsWith('**')) {
      out.push(new TextRun({ text: brut.slice(2, -2), bold: true, ...base }));
    } else {
      out.push(new TextRun({ text: brut.slice(1, -1), italics: true, ...base }));
    }
    pos = re.lastIndex;
  }
  if (pos < texte.length) decouperExposants(texte.slice(pos), base, (r) => out.push(r));
  if (out.length === 0) out.push(new TextRun({ text: '', ...base }));
  return out;
}

const P = (texte, opts = {}) => new Paragraph({
  children: runs(texte),
  alignment: opts.alignment ?? AlignmentType.JUSTIFIED,
  spacing: { line: INTERLIGNE, after: opts.after ?? 120 },
  indent: opts.indent,
  pageBreakBefore: opts.pageBreakBefore ?? false,
  keepLines: true,
  keepNext: opts.keepNext ?? false,
});

// Ordinaux en exposant : « Article 1er » → « Article 1<sup>er</sup> ».
function runsOrdinaux(texte, base = {}) {
  const out = [];
  const re = /(\d+|\bI)(ers?|res?|es|e)\b/g;
  let pos = 0, m;
  while ((m = re.exec(texte)) !== null) {
    if (m.index > pos) out.push(new TextRun({ text: texte.slice(pos, m.index), ...base }));
    out.push(new TextRun({ text: m[1], ...base }));
    out.push(new TextRun({ text: m[2], superScript: true, ...base }));
    pos = re.lastIndex;
  }
  if (pos < texte.length) out.push(new TextRun({ text: texte.slice(pos), ...base }));
  if (out.length === 0) out.push(new TextRun({ text: '', ...base }));
  return out;
}

const PCAPS = (texte, opts = {}) => new Paragraph({
  children: runsOrdinaux(texte, { smallCaps: true, bold: opts.bold ?? false }),
  alignment: AlignmentType.CENTER,
  spacing: { before: opts.before ?? 240, after: opts.after ?? 160 },
  pageBreakBefore: opts.pageBreakBefore ?? false,
  keepLines: true,
  keepNext: true,
  outlineLevel: opts.niveau,
  heading: opts.heading,
});

const VIDE = () => new Paragraph({ children: [new TextRun('')], spacing: { after: 120 } });

// ---------------------------------------------------------------- tables
// Convention du projet : une ligne de titre à une seule cellule, puis un
// séparateur, puis des lignes à deux cellules. La ligne de titre est fusionnée.
function cellules(ligne) {
  return ligne.replace(/^\||\|$/g, '').split('|').map((c) => c.trim());
}

// Frontières d'alinéas dans une cellule : deux passages gras qui se suivent,
// une élision « […] » isolée, ou un « <br> » explicite.
function alineas(txt) {
  const SEP = '\u0001';
  let t = txt.replace(/<br\s*\/?>/gi, SEP);
  t = t.replace(/\*\*\s+\*\*/g, `**${SEP}**`);
  t = t.replace(/\s*\[…\]\s*/g, `${SEP}[…]${SEP}`);
  const out = t.split(SEP).map((x) => x.trim()).filter(Boolean);
  return out.length ? out : [txt];
}
const separateur = (cs) => cs.every((c) => /^:?-{2,}:?$/.test(c));

function bloc2table(lignes) {
  const rows = lignes.map(cellules).filter((cs) => !separateur(cs));
  const nb = Math.max(...rows.map((r) => r.length));
  // Largeurs proportionnelles : une table de crédits porte un libellé long et
  // quatre montants. À largeur égale, un montant de treize chiffres se coupe au
  // milieu. Corrigé le 20261016, après refus de la liasse P2 à la publication.
  const PROPS = { 2: [0.42, 0.58], 3: [0.08, 0.30, 0.62], 4: [0.40, 0.20, 0.20, 0.20],
                  5: [0.28, 0.18, 0.18, 0.18, 0.18] };
  // « <!-- colonnes : 0.2, 0.5, 0.3 --> » juste avant un tableau impose ses largeurs
  const prop = (colonnesSuivantes && colonnesSuivantes.length === nb ? colonnesSuivantes : null)
    || PROPS[nb] || Array(nb).fill(1 / nb);
  colonnesSuivantes = null;
  const corpsTable = corpsSuivant || 19;
  corpsSuivant = null;
  const cols = prop.map((p) => Math.floor(LARGEUR_TABLE * p));
  const large = Math.floor(LARGEUR_TABLE / nb);
  const trs = rows.map((cs, i) => new TableRow({
    tableHeader: i === 0,
    cantSplit: true,
    children: cs.map((txt, ci) => new TableCell({
      width: { size: cs.length < nb ? LARGEUR_TABLE : cols[ci], type: WidthType.DXA },
      columnSpan: cs.length < nb ? nb : 1,
      shading: i === 0 && !NB ? { type: ShadingType.CLEAR, fill: 'F2F0EB' } : undefined,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: alineas(txt).map((al, k, tab) => new Paragraph({
        children: runs(al, { size: corpsTable }),
        alignment: cs.length < nb ? AlignmentType.CENTER : AlignmentType.LEFT,
        spacing: { line: 240, after: k === tab.length - 1 ? 0 : 80 },
        keepLines: true,
      })),
    })),
  }));
  return new Table({
    rows: trs,
    columnWidths: cols,
    width: { size: LARGEUR_TABLE, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 2, color: NB ? '000000' : 'B0AAA0' },
      bottom: { style: BorderStyle.SINGLE, size: 2, color: NB ? '000000' : 'B0AAA0' },
      left: { style: BorderStyle.SINGLE, size: 2, color: NB ? '000000' : 'B0AAA0' },
      right: { style: BorderStyle.SINGLE, size: 2, color: NB ? '000000' : 'B0AAA0' },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: NB ? '000000' : 'D4CFC4' },
      insideVertical: { style: BorderStyle.SINGLE, size: 2, color: NB ? '000000' : 'D4CFC4' },
    },
  });
}

// ---------------------------------------------------------------- lecture
const brut = fs.readFileSync(SRC, 'utf8').replace(/\r\n/g, '\n');
const blocs = brut.split(/\n---\n/);
const pageDeTitre = blocs.length > 1 ? blocs[0] : null;
const corps = blocs.length > 1 ? blocs.slice(1).join('\n---\n') : brut;

const enfants = [];

// ---------------------------------------------------------------- page de titre
if (pageDeTitre) {
  for (const l of pageDeTitre.split('\n')) {
    const t = l.trim();
    if (!t) { enfants.push(VIDE()); continue; }
    const nu = t.replace(/^\*\*|\*\*$/g, '');
    const majuscule = nu === nu.toUpperCase() && /[A-ZÉÈÀÎ]/.test(nu);
    enfants.push(new Paragraph({
      children: runs(t),
      alignment: AlignmentType.CENTER,
      spacing: { line: INTERLIGNE, after: majuscule ? 240 : 140 },
    }));
  }
  enfants.push(new Paragraph({ children: [new PageBreak()] }));
}

// ---------------------------------------------------------------- corps
let premierH1 = true;
let tampon = [];
var colonnesSuivantes = null;
var corpsSuivant = null;   // « <!-- corps : 16 --> » : corps du tableau suivant, en demi-points
const viderTampon = () => {
  if (tampon.length) {
    enfants.push(bloc2table(tampon));
    enfants.push(VIDE());
    tampon = [];
  }
};

const lignes = corps.split('\n');
for (let i = 0; i < lignes.length; i += 1) {
  const l = lignes[i].trim();
  const mCol = l.match(/^<!--\s*colonnes\s*:\s*([\d.,\s]+)-->$/);
  if (mCol) { viderTampon(); colonnesSuivantes = mCol[1].split(',').map(Number); continue; }
  const mCorps = l.match(/^<!--\s*corps\s*:\s*(\d+)\s*-->$/);
  if (mCorps) { viderTampon(); corpsSuivant = Number(mCorps[1]); continue; }

  if (l.startsWith('|')) { tampon.push(l); continue; }
  viderTampon();

  if (!l) continue;

  if (l === '---') {                                  // séparateur de partie
    if (PROFIL === 'pplc') enfants.push(new Paragraph({ children: [new PageBreak()] }));
    continue;
  }

  // descripteur de travail resté orphelin : absorbé par l'intitulé, donc ignoré ici
  if (/^\*\[[^\]]*\]\*$/.test(l)) continue;

  if (l.startsWith('#### ')) { enfants.push(PCAPS(l.slice(5), { before: 200 })); continue; }

  if (l.startsWith('### ')) {                          // chapitre
    enfants.push(new Paragraph({
      children: [new TextRun({ text: l.slice(4), italics: true })],
      alignment: AlignmentType.CENTER,
      spacing: { before: 260, after: 160 },
    }));
    continue;
  }

  if (l.startsWith('## ')) {                           // titre de division
    enfants.push(PCAPS(l.slice(3), {
      bold: true, before: 360, after: 200, heading: HeadingLevel.HEADING_2,
    }));
    continue;
  }

  if (l.startsWith('# ')) {                            // grand titre
    enfants.push(PCAPS(l.slice(2), {
      bold: true, before: 0, after: 320, pageBreakBefore: !premierH1,
      heading: HeadingLevel.HEADING_1,
    }));
    premierH1 = false;
    continue;
  }

  if (l === '[[SOMMAIRE]]') {                          // champ de table des matières
    enfants.push(new TableOfContents('Sommaire', {
      hyperlink: true, headingStyleRange: '1-3',
    }));
    enfants.push(new Paragraph({ children: [new PageBreak()] }));
    continue;
  }

  // intitulés de la présentation : « Partie 1. … », « A1. … », « A1.1 … »
  const mTitre = /^\*\*(Partie \d+\.|[A-Z]\d+\.(?=\s)|[A-Z]\d+\.\d+\s)/.exec(l);
  if (mTitre) {
    const partie = l.startsWith('**Partie ');
    const section = /^\*\*[A-Z]\d+\.(?!\d)/.test(l);
    enfants.push(new Paragraph({
      children: runs(l),
      alignment: AlignmentType.LEFT,
      spacing: { before: partie ? 360 : 280, after: 160 },
      keepLines: true,
      keepNext: true,
      heading: partie ? HeadingLevel.HEADING_1
        : section ? HeadingLevel.HEADING_2 : HeadingLevel.HEADING_3,
    }));
    continue;
  }

  if (/^\*\*Article [^*]+\*\*$/.test(l)) {             // intitulé d'article
    const titre = l.replace(/\*\*/g, '');
    // descripteur éventuel : prochaine ligne non vide entièrement entre crochets
    let j = i + 1;
    while (j < lignes.length && !lignes[j].trim()) j += 1;
    const suivante = j < lignes.length ? lignes[j].trim() : '';
    const aDescripteur = /^\*\[[^\]]*\]\*$/.test(suivante);
    const enfantsTitre = runsOrdinaux(titre, { smallCaps: true });
    if (aDescripteur && !DEPOT) {
      enfantsTitre.push(new TextRun({ text: '\u2003\u2003', size: CORPS }));
      enfantsTitre.push(new TextRun({
        text: suivante.replace(/^\*|\*$/g, ''), italics: true, size: 19,
      }));
    }
    if (aDescripteur) i = j;                          // consommé dans les deux cas
    enfants.push(new Paragraph({
      children: enfantsTitre,
      alignment: AlignmentType.CENTER,
      spacing: { before: 300, after: 160 },
    }));
    continue;
  }

  if (l.startsWith('«')) {                             // texte cité
    enfants.push(P(l, { indent: { left: convertInchesToTwip(0.5) } }));
    continue;
  }

  if (/^(I{1,3}V?|IV|V|VI{0,3})\.\s+—/.test(l) || /^\d+°\s/.test(l) || /^[a-z]\)\s/.test(l)) {
    enfants.push(P(l, { indent: { firstLine: convertInchesToTwip(0.3) } }));
    continue;
  }

  enfants.push(P(l, { indent: { firstLine: convertInchesToTwip(0.3) } }));
}

viderTampon();

// ---------------------------------------------------------------- document
const doc = new Document({
  features: { updateFields: true },
  styles: {
    default: {
      document: { run: { font: POLICE, size: CORPS }, paragraph: { spacing: { line: INTERLIGNE } } },
      heading1: { run: { font: POLICE, size: CORPS, bold: true, color: '000000' } },
      heading2: { run: { font: POLICE, size: CORPS, bold: true, color: '000000' } },
      heading3: { run: { font: POLICE, size: CORPS, bold: true, color: '000000' } },
    },
  },
  sections: [{
    properties: {
      page: {
        margin: {
          top: convertInchesToTwip(1), bottom: convertInchesToTwip(1),
          left: convertInchesToTwip(1.1), right: convertInchesToTwip(1.1),
        },
      },
    },
    children: enfants,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  console.log(`écrit : ${OUT} — ${enfants.length} paragraphes — profil ${PROFIL}`);
});