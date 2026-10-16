import sys, csv, re, unicodedata
sys.path.insert(0, 'appareil')
import pandas as pd
from chaine_credits import DATE_CAT, FRACTION, AGENT_CAT, TRIMESTRES, residuel, norm, INDEMNITE
from collections import defaultdict

X = sys.argv[1]
eb, t2b, cur = {}, {}, None
for r in csv.DictReader(open('referentiels/etatB_2027_bg.tsv'), delimiter='\t'):
    if r['rang'] == 'programme':
        cur = norm(r['libelle']); eb[cur] = (int(r['ae']), int(r['cp']))

d = pd.read_excel(X, 'A — Crédits', header=0); d.columns = [str(c).strip() for c in d.columns]
d = d[(d['Statut doctrine'] == 'arrêté') & (d['AE arrêtées (M€)'].astype(float) > 0)]

rows = []
for _, r in d.iterrows():
    titre, cat = int(r['Titre']), int(r['Catégorie'])
    prog = str(r['Libellé programme']); mis = str(r['Mission'])
    date = DATE_CAT.get(cat)
    if date is None: continue
    fr = FRACTION[date]; res = residuel(titre, cat)
    a = 0.90 if titre == 2 else 1.0
    net = (1 - INDEMNITE) if titre == 2 else 1.0
    ae = float(r['AE arrêtées (M€)']) * 1e6 * a * fr * net
    cp = min(float(r['CP arrêtés (M€)']), float(r['AE arrêtées (M€)'])) * 1e6 * a * fr * (1 - res) * net
    rows.append(dict(mission=mis, programme=prog, titre=titre, cat=cat, date=date,
                     ae=ae, cp=cp, agent=AGENT_CAT.get(cat, 'non classé'),
                     etatb=norm(prog) in eb))

# --- la tablette P2 : une mission, un amendement, plafonné à l'état B 2027
par = defaultdict(lambda: defaultdict(lambda: [0.0, 0.0]))
for r in rows:
    if r['etatb']: par[r['mission']][r['programme']][0] += r['ae']; par[r['mission']][r['programme']][1] += r['cp']

out = []
for mis in sorted(par, key=lambda m: -sum(v[0] for v in par[m].values())):
    lignes, pae, pcp, plaf = [], 0, 0, 0
    for prog, (ae, cp) in sorted(par[mis].items(), key=lambda x: -x[1][0]):
        o = eb[norm(prog)]
        ae_p = min(ae, o[0])
        cp_p = min(cp, o[1], ae_p)   # le CP ne dépasse jamais l'AE plafonnée
        lignes.append((prog, ae_p, cp_p, o[0], ae > o[0] or cp > o[1]))
        pae += ae_p; pcp += cp_p; plaf += o[0]
    out.append((mis, lignes, pae, pcp, plaf))

print(f"{'n°':>3} {'AE minorées':>16} {'CP minorés':>16} {'CP/AE':>6} {'pg':>3} {'% mission':>10}  mission")
tae = tcp = 0; nplaf = 0
for i, (mis, lignes, pae, pcp, plaf) in enumerate(out, 1):
    n = sum(1 for l in lignes if l[4]); nplaf += n
    print(f"{i:>3} {int(pae):>16,} {int(pcp):>16,} {pcp/pae if pae else 0:>6.3f} {len(lignes):>3} "
          f"{(100*pae/plaf if plaf else 0):>9.1f}%  {mis[:42]}{'  ·plafonné '+str(n) if n else ''}")
    tae += pae; tcp += pcp
print(f"{'':>3} {int(tae):>16,} {int(tcp):>16,} {tcp/tae:>6.3f} {sum(len(l[1]) for l in out):>3}"
      f"{'':>11}  TOTAL — {len(out)} amendements, {nplaf} lignes plafonnées")

# --- le compteur, après plafonnement
fact = {}
for mis, lignes, *_ in out:
    for prog, ae_p, cp_p, _, _ in lignes:
        k = (mis, prog); brut = par[mis][prog][0]
        fact[k] = ae_p / brut if brut else 0
tri = defaultdict(lambda: [0.0]*4)
for r in rows:
    if not r['etatb']: continue
    f = fact.get((r['mission'], r['programme']), 1.0)
    qs = TRIMESTRES[r['date']]
    for q in qs: tri[r['agent']][q-1] += r['ae'] * f / len(qs)
print(f"\n{'agent':<16} {'T1':>10} {'T2':>10} {'T3':>10} {'T4':>10} {'année':>11}")
tq = [0.0]*4
for ag, v in sorted(tri.items(), key=lambda x: -sum(x[1])):
    print(f"{ag:<16} " + " ".join(f"{x/1e6:>10.1f}" for x in v) + f" {sum(v)/1e6:>11.1f}")
    for i in range(4): tq[i] += v[i]
print(f"{'TOTAL':<16} " + " ".join(f"{x/1e6:>10.1f}" for x in tq) + f" {sum(tq)/1e6:>11.1f}")
