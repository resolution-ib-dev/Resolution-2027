import csv,collections,sys
def lire(p):
    with open(p,encoding='utf-8',newline='') as f: return list(csv.DictReader(f,delimiter='\t'))
o=lire('archive/tri_20261020/versions_branche/referentiels/sort_prelevements_20261015.tsv')
m=lire('referentiels/sort_prelevements_20261015.tsv')
n=lire('referentiels/sort_prelevements_20261103.tsv')
def f(x):
    try: return float(x)
    except: return 0.0
# même ordre oct20 / main1015 ?
print('ordre identique oct20/main1015:',[r['libelle'] for r in o]==[r['libelle'] for r in m])
lo=collections.Counter(r['libelle'] for r in o); print('doublons libellé oct20',[k for k,v in lo.items() if v>1])
ln=collections.Counter(r['libelle'] for r in n); print('doublons libellé nov3',[k for k,v in ln.items() if v>1])
# n du 3 nov = numéro de ligne du 1015 ?
byn={r['n']:r for r in n}
ok=sum(1 for i,r in enumerate(o,1) if str(i) in byn and byn[str(i)]['libelle']==r['libelle'])
print('rang i oct20 = n nov3 avec même libellé:',ok)
abs_=[(i,r['libelle']) for i,r in enumerate(o,1) if str(i) not in byn]; print('rangs oct20 absents nov3',abs_)
diff_lib=[(i,r['libelle'][:50],byn[str(i)]['libelle'][:50]) for i,r in enumerate(o,1) if str(i) in byn and byn[str(i)]['libelle']!=r['libelle']]; print('libellés changés',diff_lib)
nouv=[(r['n'],r['libelle'][:70],r['devenir'],r['rendement_2026_M']) for r in n if not r['n'].isdigit() or int(r['n'])>420]; print('ajoutés nov3',len(nouv)); [print('  ',x) for x in nouv]
EQ={'fondu par rattachement':'remplacé par un grand impôt','cotisations sociales à unifier':'à fusionner','maintenu à part':'conservé en complément','fondu dans l’équilibre':'fondu dans l’équilibre des quatre grands impôts','conservé et absorbe':'grand impôt conservé','hors champ':'recette non fiscale'}
X=collections.Counter(); XR=collections.defaultdict(float); div=[]; cib=[]; rdt=[]
for i,r in enumerate(o,1):
    b=byn.get(str(i))
    if not b: continue
    X[(r['sort'],b['devenir'])]+=1; XR[(r['sort'],b['devenir'])]+=f(r['rendement_2026_M'])
    if EQ[r['sort']]!=b['devenir']: div.append((i,r,b))
    elif r['sort']=='fondu par rattachement' and r['impot_absorbant']!=b['impot_cible']: cib.append((i,r,b))
    if r['rendement_2026_M']!=b['rendement_2026_M']: rdt.append((i,r['libelle'][:60],r['rendement_2026_M'],b['rendement_2026_M']))
print('croisé:'); [print(f'  {v:4d} {XR[k]:11.1f}  {k[0]} -> {k[1]}') for k,v in sorted(X.items(),key=lambda x:-x[1])]
print('sort divergent:',len(div), round(sum(f(r['rendement_2026_M']) for _,r,_ in div),1))
w=csv.writer(open(sys.argv[1],'w',newline=''),delimiter='\t'); w.writerow(['n','libelle','sort_20261020','impot_absorbant_20261020','devenir_20261103','impot_cible_20261103','bloc_20261103','rendement_2026_M_20261020','rendement_2026_M_20261103','nature_ecart'])
for i,r,b in div: w.writerow([i,r['libelle'],r['sort'],r['impot_absorbant'],b['devenir'],b['impot_cible'],b['bloc'],r['rendement_2026_M'],b['rendement_2026_M'],'sort'])
for i,r,b in cib: w.writerow([i,r['libelle'],r['sort'],r['impot_absorbant'],b['devenir'],b['impot_cible'],b['bloc'],r['rendement_2026_M'],b['rendement_2026_M'],'impôt de remplacement'])
print('impôt cible divergent (même sort):',len(cib), round(sum(f(r['rendement_2026_M']) for _,r,_ in cib),1))
print(collections.Counter((r['impot_absorbant'],b['impot_cible']) for _,r,b in cib).most_common())
print('rendement différent:',len(rdt)); [print('  ',x) for x in rdt]
for i,r,b in div: print(i,'|',r['libelle'][:62],'|',r['sort'],'/',r['impot_absorbant'],'->',b['devenir'],'/',b['impot_cible'],b['bloc'],'|',r['rendement_2026_M'])
