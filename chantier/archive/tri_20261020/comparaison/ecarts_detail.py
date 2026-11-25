import csv,collections
def lire(p):
    with open(p,encoding='utf-8',newline='') as f: return list(csv.DictReader(f,delimiter='\t'))
o=lire('archive/tri_20261020/versions_branche/referentiels/sort_prelevements_20261015.tsv')
m=lire('referentiels/sort_prelevements_20261015.tsv')
n=lire('referentiels/sort_prelevements_20261103.tsv')
byn={r['n']:r for r in n}
def f(x):
    try: return float(x)
    except: return 0.0
G={'auteur 20261103':[133,134,140,146,196,380,293,295],'schéma 20261020, absent du 3 nov':[6,12,194,277,280,281,282,283,284,285,286,287,289,290,211,214,215],'correction de siège 3 nov':[70]}
for k,v in G.items(): print(k,len(v),round(sum(f(o[i-1]['rendement_2026_M']) for i in v),1))
print('jeux 280-290 oct20:',round(sum(f(o[i-1]['rendement_2026_M']) for i in [280,281,282,283,284,285,286,287,289,290]),1),'élec',round(sum(f(o[i-1]['rendement_2026_M']) for i in [211,214,215]),1))
# changements oct20 vs main1015
ch=collections.Counter()
for a,b in zip(m,o):
    for c in a:
        if a[c]!=b[c]: ch[c]+=1
print('colonnes changées main1015->oct20',ch.most_common())
print('rangs dont le sort change main1015->oct20:',sum(1 for a,b in zip(m,o) if a['sort']!=b['sort']), collections.Counter((a['sort'],b['sort']) for a,b in zip(m,o) if a['sort']!=b['sort']).most_common())
# TTF
for i,r in enumerate(o,1):
    if 'transactions financi' in r['libelle'] or 'haute fr' in r['libelle']:
        b=byn[str(i)]; print(i,r['libelle'][:50],'|',r['assiette'],'|',r['sort'],r['impot_absorbant'],'|',r['ligne_schema'],'|| nov3',b['assiette'],b['devenir'],b['impot_cible'])
print('assiettes oct20',collections.Counter(r['assiette'] for r in o).most_common())
print('assiettes nov3',collections.Counter(r['assiette'] for r in n).most_common())
print('ligne_schema oct20 renseignée:',sum(1 for r in o if r['ligne_schema'] not in ('','—')),'postes',len(set(r['ligne_schema'] for r in o)))
# nov3 : questions, voie réglementaire, millésime
print('question non vide',sum(1 for r in n if r['question'].strip()), collections.Counter(r['question'][:60] for r in n if r['question'].strip()).most_common(20))
print('etat_porteur',collections.Counter(r['etat_porteur'] for r in n).most_common())
print('verdict',collections.Counter(r['verdict'] for r in n).most_common())
d=[r for r in n if r['rendement_2026_revise_plf2027_M'].strip() and r['rendement_2026_revise_plf2027_M']!=r['rendement_2026_M']]
print('révisé renseigné',sum(1 for r in n if r['rendement_2026_revise_plf2027_M'].strip()),'différent',len(d),'somme actuelle',round(sum(f(r['rendement_2026_M']) for r in d),1),'somme révisée',round(sum(f(r['rendement_2026_revise_plf2027_M']) for r in d),1))
print('part conservée',[(r['n'],r['libelle'][:40],r['part_conservee_2026_M']) for r in n if r['part_conservee_2026_M'].strip()])
print('source_rendement',collections.Counter(r['source_rendement'][:50] for r in n).most_common())
print('nature_ligne',collections.Counter(r['nature_ligne'] for r in n).most_common(), collections.Counter(r['nature_ligne'] for r in o).most_common())
print('statut_siege nov3',collections.Counter(r['statut_siege'] for r in n).most_common())
print('cotis nature nov3 à fusionner',collections.Counter(r['nature'] for r in n if r['devenir']=='à fusionner').most_common())
