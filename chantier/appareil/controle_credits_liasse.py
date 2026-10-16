#!/usr/bin/env python3
"""Contrôle des tables de crédits d'une liasse de seconde partie.

Quatre règles, inscrites le 20261016.

  C1 — minoration AE ≤ AE du programme à l'état B 2027.
  C2 — minoration CP ≤ CP du programme à l'état B 2027.
  C3 — AE ≥ CP. L'égalité est admise sur le titre 2, où l'article 8 de la
       LOLF l'impose, et, hors titre 2, lorsqu'elle est RELEVÉE : le ratio
       CP/AE de la catégorie visée vaut au moins 1,000 au PAP, à la
       tolérance près. Un ratio inférieur refuse l'égalité : le CP suit
       alors son régime de résiduel, puis le resize.
  C4 — signal, non bloquant : minoration AE ≤ AE de la catégorie visée,
       recalée par le resize. La ventilation par catégorie est au millésime
       2026 ; le dépassement se signale, il ne tranche pas.

La catégorie visée se déclare au bloc [interne] de la pièce, une ligne :

    Catégories visées : Service public de l'énergie → 62

Sans déclaration, l'égalité hors titre 2 est refusée : une égalité qui ne
nomme pas sa catégorie n'est pas relevée.

Pièces qui font foi :
  referentiels/etatB_2027_bg.tsv        — crédits ouverts 2027, par programme
  referentiels/ratios_cp_ae_pap2026.tsv — ratios mesurés, par catégorie

Usage : python3 appareil/controle_credits_liasse.py <liasse.md> [...]
"""
import csv, re, sys, unicodedata
from pathlib import Path

TOLERANCE = 0.005
RESIZE = 1.01288   # (CP/AE)_2027 ÷ (CP/AE)_2026, agrégat budget général

def norm(s):
    s = unicodedata.normalize('NFKD', str(s).replace('’', "'"))
    s = s.encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()

def euros(s):
    """Premier nombre de la cellule. Une cellule peut porter du texte après le
    montant — « 1 842 105 969, augmentés de la part de… » : seul le nombre de
    tête se lit."""
    s = s.strip().lstrip('*_ \u00a0').lstrip('\u2212-')
    m = re.match(r'[\d][\d\u00a0\u202f ]*', s)
    if not m:
        return 0
    n = re.sub(r'[^\d]', '', m.group())
    return int(n) if n else 0

def charger(racine):
    etatb = {}
    with open(racine / 'referentiels/etatB_2027_bg.tsv') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['rang'] == 'programme':
                etatb[norm(r['libelle'])] = (int(r['ae']), int(r['cp']))
    ratios = {}
    with open(racine / 'referentiels/ratios_cp_ae_pap2026.tsv') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['ratio_cp_ae']:
                ratios[(norm(r['programme']), int(r['categorie']))] = (
                    int(r['ae_pap2026']), float(r['ratio_cp_ae']))
    return etatb, ratios

DECL = re.compile(r'Catégories?\s+visées?\s*:\s*(.+)', re.I)

def declarations(lignes):
    """Rend {programme normalisé : catégorie}, lu aux blocs [interne]."""
    out = {}
    for ln in lignes:
        m = DECL.search(ln)
        if not m:
            continue
        for part in re.split(r'[·;]', m.group(1)):
            p = re.split(r'→|->', part)
            if len(p) == 2 and re.search(r'\d', p[1]):
                out[norm(p[0])] = int(re.search(r'\d+', p[1]).group())
    return out

EXCLUS = ('totaux', 'total', 'solde', 'soldes')

def tables(chemin):
    lignes = Path(chemin).read_text().split('\n')
    decl = declarations(lignes)
    courant, sorties = None, []
    for i, ln in enumerate(lignes):
        m = re.match(r'^#+\s*AMENDEMENT\s+N°\s*(\d+)', ln.strip(), re.I)
        if m:
            courant = m.group(1)
        if not ln.startswith('| Programmes'):
            continue
        j, rows, t2 = i + 2, [], 0
        while j < len(lignes) and lignes[j].startswith('|'):
            c = [x.strip() for x in lignes[j].strip('|').split('|')]
            if len(c) >= 5:
                libelle = c[0].strip('* ').lower()
                if 'titre 2' in libelle:
                    t2 += euros(c[2])
                elif not libelle.startswith(EXCLUS):
                    rows.append((c[0].strip('* '), euros(c[2]), euros(c[4])))
            j += 1
        sorties.append((courant, rows, t2))
    return sorties, decl

def main(argv):
    racine = Path(__file__).resolve().parent.parent
    etatb, ratios = charger(racine)
    dur = sig = 0
    for chemin in argv:
        nom = Path(chemin).name
        sorties, decl = tables(chemin)
        porte = any(ae or cp for _, rows, _ in sorties for _, ae, cp in rows)
        egalite = any(ae and ae == cp and t2 < ae
                      for _, rows, t2 in sorties for _, ae, cp in rows)
        if porte and egalite and not decl:
            # Une liasse assemblée ne porte pas les blocs [interne] : les
            # déclarations de catégorie vivent aux pièces source. C3 et C4 ne
            # s'y jouent donc pas — c'est la pièce qui se contrôle, pas le
            # dérivé.
            print('— %s : aucune déclaration de catégorie, pièce tenue pour un '
                  'dérivé ; C1 et C2 seuls joués' % nom)
        for amd, rows, t2 in sorties:
            for prog, ae, cp in rows:
                if ae == 0 and cp == 0:
                    continue
                tete = '%s n° %s — %s' % (nom, amd, prog)
                e = etatb.get(norm(prog))
                if not e:
                    print('C0 %s : programme absent de l\'état B 2027' % tete); dur += 1; continue
                if ae > e[0]:
                    print('C1 %s : AE minorées %s > %s ouvertes' % (tete, f'{ae:,}', f'{e[0]:,}')); dur += 1
                if cp > e[1]:
                    print('C2 %s : CP minorés %s > %s ouverts' % (tete, f'{cp:,}', f'{e[1]:,}')); dur += 1
                if cp > ae:
                    print('C3 %s : CP %s > AE %s' % (tete, f'{cp:,}', f'{ae:,}')); dur += 1
                elif cp == ae and t2 < ae and decl:
                    cat = decl.get(norm(prog))
                    if cat is None:
                        print('C3 %s : AE = CP hors titre 2, aucune catégorie déclarée' % tete); dur += 1
                    else:
                        v = ratios.get((norm(prog), cat))
                        if not v:
                            print('C3 %s : catégorie %d absente du PAP' % (tete, cat)); dur += 1
                        elif v[1] < 1.0 - TOLERANCE:
                            print('C3 %s : AE = CP hors titre 2, cat. %d relevée à %.3f — égalité refusée'
                                  % (tete, cat, v[1])); dur += 1
                cat = decl.get(norm(prog))
                if cat is not None:
                    v = ratios.get((norm(prog), cat))
                    if v and ae > v[0] * RESIZE:
                        print('C4 %s : AE minorées %s > %s portées par la cat. %d (2026 recalé) — signal'
                              % (tete, f'{ae:,}', f'{int(v[0] * RESIZE):,}', cat)); sig += 1
    print('%d anomalie(s) bloquante(s), %d signal(aux)' % (dur, sig))
    return 1 if dur else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or ['livrables/depot_2027/LIASSE_PLF_P2.md']))
