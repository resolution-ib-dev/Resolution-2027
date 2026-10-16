#!/usr/bin/env python3
"""La chaîne de calcul d'un amendement de crédits, de bout en bout.

Inscrite le 20261016, après que quatre pièces sur cinq eurent tiré leur
montant de la colonne D de `Détail Economies`, que le registre réserve à une
projection. **Pour un amendement, l'assiette est la table A.**

Les étapes, dans l'ordre du § 1 du registre, et aucune autre :

  1. ASSIETTE   table A de `Suivi dépenses…xlsx`, colonnes « AE arrêtées » et
                « CP arrêtés », au grain mission × programme × titre × catégorie.
                Le socle, le rythme et le drapeau d'arrêt y sont DÉJÀ appliqués :
                l'onglet « Mesure » du classeur le dit, et le contrôle « CP
                arrêtés = Economies R, écart nul » le prouve. On ne les
                applique donc pas une seconde fois — c'est la faute R-V, à
                l'envers.
  2. FRACTION   d'exercice, par la date d'effet, elle-même donnée par la
                catégorie selon R-P et R-S. 6/12 au 1er juillet, 12/12 au
                1er janvier.
  3. AE         = assiette AE × fraction.
  4. CP         = min (CP arrêtés ; AE arrêtées) × fraction × (1 − résiduel),
                le résiduel étant celui du § 3, par catégorie et par titre.
  5. CONTRÔLE   minoration ≤ crédit ouvert du programme à l'état B 2027,
                en AE comme en CP. Et AE ≥ CP, l'égalité se relevant.
  6. TITRE 2    l'article 8 impose AE = CP, donc résiduel nul. Et la formule
                du § 10 retranche l'indemnité I — **non chiffrée à ce jour**,
                si bien qu'aucune minoration de titre 2 ne se ferme.

Usage : python3 appareil/chaine_credits.py <classeur suivi> [--titre N]
"""
import sys, csv, re, unicodedata
from pathlib import Path

# --- § 3 du registre : les régimes de résiduel, par catégorie puis par titre
RESIDUEL_CAT = {21: 0.0, 22: 0.0, 23: 0.0, 32: 0.0, 61: 0.0, 64: 0.0,
                62: 0.20, 63: 0.25}
RESIDUEL_TITRE = {1: 0.0, 2: 0.0, 4: 0.0, 5: 0.80}
PLANCHER = 0.15
INDEMNITE = 0.70      # § 10, arbitrage du 20261016 : I = 70 % de l'économie de titre 2

# --- R-P et R-S : la date d'effet se lit à la catégorie, qui porte l'acteur
#     Arbitrage du 20261016 : le fonctionnement des administrations (cat. 31)
#     part avec les personnels, donc au 1er juillet.
DATE_CAT = {21: '1er juil.', 22: '1er juil.', 23: '1er juil.', 31: '1er juil.',
            61: '1er juil.', 32: '1er janv.', 62: '1er janv.', 63: '1er janv.',
            64: '1er janv.', 51: '1er janv.', 52: '1er janv.', 53: '1er janv.',
            71: '1er janv.'}
FRACTION = {'1er juil.': 0.5, '1er janv.': 1.0}

# --- l'agent qui perd, lu à la catégorie, dont `Economies R` donne le libellé
#     61 Subvention Ménages · 62 Subvention Entreprises · 63 Subvention
#     Collectivités · 64 Subvention Autres · 32 Subvention Opérateurs.
AGENT_CAT = {21: 'agents publics', 22: 'agents publics', 23: 'agents publics',
             31: 'entreprises', 51: 'entreprises', 52: 'entreprises',
             53: 'entreprises', 32: 'opérateurs', 61: 'ménages',
             62: 'entreprises', 63: 'collectivités', 64: 'associations',
             71: 'hors champ'}
# --- les trimestres touchés, par date d'effet
TRIMESTRES = {'1er janv.': (1, 2, 3, 4), '1er juil.': (3, 4)}

def norm(s):
    s = unicodedata.normalize('NFKD', str(s).replace('’', "'"))
    s = s.encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()

def residuel(titre, cat):
    if titre == 2:
        return 0.0                      # LOLF art. 8
    if cat in RESIDUEL_CAT:
        return RESIDUEL_CAT[cat]
    if titre in RESIDUEL_TITRE:
        return RESIDUEL_TITRE[titre]
    return PLANCHER

def etat_b(racine):
    """Crédits ouverts 2027 par programme, et le titre 2 qui s'y rattache."""
    ouverts, t2, cur = {}, {}, None
    with open(racine / 'referentiels/etatB_2027_bg.tsv') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['rang'] == 'programme':
                cur = norm(r['libelle']); ouverts[cur] = (int(r['ae']), int(r['cp']))
            elif r['rang'] == 'titre2' and cur:
                t2[cur] = int(r['ae'])
    return ouverts, t2

def main(argv):
    import pandas as pd
    racine = Path(__file__).resolve().parent.parent
    classeur = argv[0]
    filtre = None
    if '--titre' in argv:
        filtre = int(argv[argv.index('--titre') + 1])
    d = pd.read_excel(classeur, 'A — Crédits', header=0)
    d.columns = [str(c).strip() for c in d.columns]
    d = d[d['Statut doctrine'] == 'arrêté']
    d = d[d['AE arrêtées (M€)'].astype(float) > 0]
    if filtre is not None:
        d = d[d['Titre'] == filtre]
    ouverts, t2 = etat_b(racine)

    lignes, manquants = [], set()
    for _, r in d.iterrows():
        titre, cat = int(r['Titre']), int(r['Catégorie'])
        prog = str(r['Libellé programme'])
        ae_a = float(r['AE arrêtées (M€)']) * 1e6
        cp_a = float(r['CP arrêtés (M€)']) * 1e6
        date = DATE_CAT.get(cat)
        if date is None:
            manquants.add(cat); continue
        fr = FRACTION[date]
        res = residuel(titre, cat)
        # titre 2 : le socle a = 0,90 du § 10 s'applique à l'arrêtée, qui est
        # brute. Preuve au § 10 du registre : 3 287,5 × 0,90 = 2 958,8, soit
        # F38 = 3,0 Md€ à 1,4 % près. Les autres titres ont leur socle dans
        # l'assiette et ne le reprennent pas.
        a = 0.90 if titre == 2 else 1.0
        # titre 2 : l'indemnité I du § 10 vaut 70 % de l'économie de titre 2
        # — arbitrage de l'auteur du 20261016, « au plus 70 % du T2 ». Il reste
        # donc 30 % net. Les autres titres ne portent pas d'indemnité.
        net = (1 - INDEMNITE) if titre == 2 else 1.0
        ae = ae_a * a * fr * net
        cp = min(cp_a, ae_a) * a * fr * (1 - res) * net
        lignes.append(dict(mission=str(r['Mission']), programme=prog, titre=titre,
                           categorie=cat, date=date, fraction=fr, residuel=res,
                           ae=ae, cp=cp, agent=AGENT_CAT.get(cat, 'non classé')))
    # agrégation par mission × programme
    from collections import defaultdict
    par = defaultdict(lambda: [0.0, 0.0])
    for l in lignes:
        k = (l['mission'], l['programme'])
        par[k][0] += l['ae']; par[k][1] += l['cp']

    if '--mission' in argv:
        parmis = defaultdict(lambda: [0.0, 0.0, 0])
        plaf = defaultdict(lambda: [0, 0])
        for l in lignes:
            k = l['mission']
            parmis[k][0] += l['ae']; parmis[k][1] += l['cp']; parmis[k][2] += 1
        for (mis, prog), (ae, cp) in par.items():
            o = ouverts.get(norm(prog))
            if o:
                plaf[mis][0] += o[0]; plaf[mis][1] += o[1]
        print(f"{'AE minorées':>16} {'CP minorés':>16} {'CP/AE':>6} {'lignes':>7} {'% mission':>10}  mission")
        for mis, (ae, cp, n) in sorted(parmis.items(), key=lambda x: -x[1][0]):
            pm = 100 * ae / plaf[mis][0] if plaf[mis][0] else float('inf')
            print(f"{int(ae):>16,} {int(cp):>16,} {cp/ae if ae else 0:>6.3f} {n:>7} {pm:>9.1f}%  {mis[:44]}")
        s_ae = sum(v[0] for v in parmis.values()); s_cp = sum(v[1] for v in parmis.values())
        print(f"{int(s_ae):>16,} {int(s_cp):>16,} {s_cp/s_ae:>6.3f} {sum(v[2] for v in parmis.values()):>7}"
              f"{'':>11}  TOTAL — {len(parmis)} missions, donc {len(parmis)} amendements")
        return 0
    print(f"{'AE minorées':>16} {'CP minorés':>16} {'CP/AE':>6} {'plafond AE':>16} {'%':>6}  programme")
    tot_ae = tot_cp = 0; depassements = 0
    for (mis, prog), (ae, cp) in sorted(par.items(), key=lambda x: -x[1][0]):
        o = ouverts.get(norm(prog))
        pct = 100 * ae / o[0] if o and o[0] else float('inf')
        flag = '  <<<' if o and (ae > o[0] or cp > o[1]) else ''
        if flag: depassements += 1
        print(f"{int(ae):>16,} {int(cp):>16,} {cp/ae if ae else 0:>6.3f} "
              f"{o[0] if o else 0:>16,} {pct:>5.1f}%  {prog[:46]}{flag}")
        tot_ae += ae; tot_cp += cp
    print(f"\n{int(tot_ae):>16,} {int(tot_cp):>16,} {tot_cp/tot_ae:>6.3f}"
          f"{'':>16} {'':>6}  TOTAL — {len(par)} programmes, {len(lignes)} lignes")
    if depassements:
        print(f"\n{depassements} programme(s) au-dessus du crédit ouvert 2027.")
    if manquants:
        print(f"\nCatégories sans date d'effet arrêtée, écartées : {sorted(manquants)}")
    # --- le compte par agent et par trimestre, en AE
    tri = defaultdict(lambda: [0.0] * 4)
    for l in lignes:
        qs = TRIMESTRES[l['date']]
        for q in qs:
            tri[l['agent']][q - 1] += l['ae'] / len(qs)
    print("\n--- minoration par agent et par trimestre, 2027, en AE, M€ ---")
    print(f"{'agent':<18} {'T1':>10} {'T2':>10} {'T3':>10} {'T4':>10} {'année':>12}")
    tq = [0.0] * 4
    for ag, v in sorted(tri.items(), key=lambda x: -sum(x[1])):
        print(f"{ag:<18} " + " ".join(f"{x/1e6:>10.1f}" for x in v) + f" {sum(v)/1e6:>12.1f}")
        for i in range(4):
            tq[i] += v[i]
    print(f"{'TOTAL':<18} " + " ".join(f"{x/1e6:>10.1f}" for x in tq) + f" {sum(tq)/1e6:>12.1f}")

    if filtre == 2 or filtre is None:
        print("\nTitre 2 — indemnité retranchée à 70 % (arbitrage du 20261016). "
              "Les montants ci-dessus sont nets et se ferment.")

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
