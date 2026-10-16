---
name: impression-docx
description: Export docx d'un livrable rédigé en markdown, pour transmission à des tiers — proposition de loi déposable, note, document de présentation. Utiliser cette skill dès qu'il s'agit de produire un .docx à partir d'un fichier md déjà validé, d'appliquer les conventions typographiques françaises d'un document normatif (Garamond, corps justifié, petites capitales, guillemets français avec espaces insécables, texte cité en retrait), ou de contrôler un rendu docx sur son PDF. Déclencher pour toute demande d'impression, d'export, de version envoyable, de « docx », de « Word », ou de mise en forme finale d'un livrable. Ne pas déclencher pour rédiger ou réviser le texte lui-même : le texte se travaille en md.
---

# Impression docx d'un livrable markdown

Le texte se rédige, se révise et se valide **en markdown**. Le docx est un export
terminal, destiné à des tiers. Il coûte du temps et des jetons et n'apporte rien à la
validation du fond : ne jamais l'engager avant que le md soit arrêté.

## Séquence

```
0. INSTALLER    écrire le générateur sur disque (§ Générateur, en fin de skill)
1. CONTRÔLER    le md est arrêté : contrôles de sortie passés
2. GÉNÉRER      node /home/claude/md2docx.js entree.md sortie.docx [profil]
3. RENDRE       soffice --headless --convert-to pdf sortie.docx
4. VÉRIFIER     pdftoppm puis lecture des images, page par page
5. LIVRER       copie dans /mnt/user-data/outputs + present_files
```

L'étape 4 est obligatoire et ne se délègue pas au texte source : plusieurs règles
typographiques ne se vérifient que sur le rendu.

## Étape 1 — Contrôles de sortie du markdown

À passer avant génération, en une commande :

```python
import re
t = open(src, encoding='utf-8').read()
corps = '\n'.join(l for l in t.split('\n') if not l.startswith(('#', '---')))
assert not re.findall(r',\s+(?:et|ou|mais|ni|car|or|donc)\b', corps)   # virgule de coordination
assert corps.count("'") == 0                                          # apostrophes typographiques
assert not re.findall(r'(?m)^\*\[[^\]]*\]\*$', t)                     # descripteurs résiduels
print(sorted(set(re.findall(r'\[[^\]]*\]', corps))))                   # crochets : inspecter
```

Les crochets admis sont les paramètres politiques non tranchés et les blancs de la page
de titre. Tout autre crochet est une erreur.

## Étape 2 — Génération

```bash
node /home/claude/md2docx.js entree.md sortie.docx pplc
node …/md2docx.js entree.md depot.docx pplc --depot    # passe de dépôt : descripteurs retirés
```

Profils : `pplc` (saut de page à chaque séparateur `---`), `note`, `presentation`.

Conventions markdown reconnues par le script :

| markdown | rendu |
|---|---|
| bloc avant le premier `---` | page de titre centrée, suivie d'un saut de page |
| `# TITRE` | grand titre centré, petites capitales gras, saut de page avant sauf le premier |
| `## TITRE …` | intitulé de division, centré, petites capitales gras |
| `### Chapitre …` | sous-division, centrée, italique |
| `**Article 1er**` | intitulé d'article, centré, petites capitales |
| `*[…]*` seul sur sa ligne | descripteur de travail, rendu en italique centré sous l'intitulé ; **retiré par l'option `--depot`** |
| ligne commençant par `«` | texte cité, retrait de 0,5 pouce |
| `I. — `, `1° `, `a) ` | subdivision, retrait de première ligne |
| `*texte*`, `**texte**` | italique, gras en ligne |
| bloc de lignes `\| … \|` | tableau ; une ligne à cellule unique est fusionnée sur toute la largeur et grisée, les suivantes forment les colonnes |

Convention d'encadré : ligne de titre à une seule cellule portant le
nom de l'article, séparateur, puis lignes à deux cellules — texte en vigueur et version
cible. Le script fusionne la ligne de titre et la centre.

Corps : Garamond 11 points, justifié, interligne 1,15, marges 1 pouce en haut et en bas,
1,1 pouce à gauche et à droite.

## Étape 3 et 4 — Rendu et vérification

```bash
soffice --headless --convert-to pdf sortie.docx --outdir .
pdftoppm -jpeg -r 100 sortie.pdf page
ls page-*.jpg        # puis lire les images
```

`pandoc -t plain sortie.docx` en repli si la lecture d'image est indisponible : elle
donne la structure textuelle mais pas la typographie.

### Ce qui ne se vérifie que sur le rendu

- **Ponctuation avant le guillemet fermant** : « …croyances. » et non « …croyances ».
  La règle s'inverse pour les mots isolés cités, où la ponctuation de la phrase
  enclosante se place après le guillemet fermant. Les deux règles coexistent dans un
  même document.
- **Espaces insécables** autour des guillemets français et devant les deux-points, le
  point-virgule, le point d'interrogation et le point d'exclamation. Un insécable
  manquant ne se voit qu'au rejet de ligne.
- **Petites capitales** effectivement appliquées : selon la police disponible, elles
  peuvent tomber en capitales pleines.
- **Sauts de page** aux bons endroits, en particulier entre exposé des motifs et
  dispositif, et absence de titre orphelin en bas de page.
- **Césures** dans les mots composés et les références d'articles.

## Étape 5 — Livraison

Copier dans `/mnt/user-data/outputs`, nommer `NomDoc.docx` avec la date
obtenue par `date +%Y%m%d`, jamais de mémoire, puis appeler `present_files` avec le docx
en premier.

## Dépendances

`docx` (npm, préinstallé — ne pas lancer `npm install` avant d'avoir essayé
`require('docx')`) · `soffice` · `pdftoppm` · `pandoc`.

Lire la documentation docx de votre atelier avant toute intervention sortant du cadre du
script : édition d'un docx existant, commentaires, révisions suivies, tableaux.

## Avertissement de persistance

Le répertoire de travail d'un atelier n'est pas persistant : c'est un répertoire du conteneur,
peuplé par copie à son démarrage. Toute modification apportée ici disparaît à la
réinitialisation. Après avoir modifié cette skill, exporter le dossier complet dans
`/mnt/user-data/outputs` et le faire réinstaller. Les scripts de rendu du chantier
ont déjà été perdus deux fois de cette manière.


---

## Générateur — `md2docx.js`

Cette skill est autonome : aucun fichier annexe. Avant toute génération, écrire le
bloc ci-dessous dans `/home/claude/md2docx.js` (heredoc `cat > /home/claude/md2docx.js << 'MD2DOCX_EOF'`),
puis vérifier le module : `npm ls docx || npm install docx`.

```javascript
#!/usr/bin/env node
// md2docx.js — export docx d'un livrable rédigé en markdown.
// Usage : node md2docx.js entree.md sortie.docx [profil]
// Profils : pplc (défaut) · note · presentation
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
if (!SRC || !OUT) {
  console.error('usage : node md2docx.js entree.md sortie.docx [pplc|note|presentation]');
  process.exit(1);
}

const POLICE = 'Garamond';
const CORPS = 22;        // demi-points → 11 pt
const INTERLIGNE = 276;  // 1,15 ligne

// ---------------------------------------------------------------- runs en ligne
// Découpe *italique* et ** gras ** en runs. Ne touche pas aux guillemets.
function runs(texte, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g;
  let pos = 0, m;
  while ((m = re.exec(texte)) !== null) {
    if (m.index > pos) out.push(new TextRun({ text: texte.slice(pos, m.index), ...base }));
    const brut = m[0];
    if (brut.startsWith('**')) {
      out.push(new TextRun({ text: brut.slice(2, -2), bold: true, ...base }));
    } else {
      out.push(new TextRun({ text: brut.slice(1, -1), italics: true, ...base }));
    }
    pos = re.lastIndex;
  }
  if (pos < texte.length) out.push(new TextRun({ text: texte.slice(pos), ...base }));
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
  const large = Math.floor(LARGEUR_TABLE / nb);
  const trs = rows.map((cs, i) => new TableRow({
    tableHeader: i === 0,
    cantSplit: true,
    children: cs.map((txt) => new TableCell({
      width: { size: cs.length < nb ? LARGEUR_TABLE : large, type: WidthType.DXA },
      columnSpan: cs.length < nb ? nb : 1,
      shading: i === 0 ? { type: ShadingType.CLEAR, fill: 'F2F0EB' } : undefined,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: alineas(txt).map((al, k, tab) => new Paragraph({
        children: runs(al, { size: 19 }),
        alignment: cs.length < nb ? AlignmentType.CENTER : AlignmentType.LEFT,
        spacing: { line: 240, after: k === tab.length - 1 ? 0 : 80 },
        keepLines: true,
      })),
    })),
  }));
  return new Table({
    rows: trs,
    columnWidths: Array(nb).fill(large),
    width: { size: LARGEUR_TABLE, type: WidthType.DXA },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 2, color: 'B0AAA0' },
      bottom: { style: BorderStyle.SINGLE, size: 2, color: 'B0AAA0' },
      left: { style: BorderStyle.SINGLE, size: 2, color: 'B0AAA0' },
      right: { style: BorderStyle.SINGLE, size: 2, color: 'B0AAA0' },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: 'D4CFC4' },
      insideVertical: { style: BorderStyle.SINGLE, size: 2, color: 'D4CFC4' },
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
```

---

## Renvois — règle de nommage

**Un nom canonique par artefact, aucun horodatage.** L'historique vit dans git et
dans le journal du projet, jamais dans un nom de fichier. Cette règle vaut pour ce
que cette skill **lit** comme pour ce qu'elle **écrit** : un livrable ne porte
jamais de date ni de numéro de version dans son nom.

L'index du projet est la table de résolution. Un nom cité ici s'y retrouve par
son champ `chemin` ; un nom ancien s'y résout par son champ `alias`. Un renvoi qui
ne résout pas se déclare au bloc `manquants` de l'index — il ne se devine pas et
il ne se comble pas.

Seule exception : `sources/`, où une archive est datée par nature.
