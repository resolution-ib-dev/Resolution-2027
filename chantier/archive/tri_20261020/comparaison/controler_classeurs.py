import csv,collections,openpyxl
def lire(p):
    with open(p,encoding='utf-8',newline='') as f: return list(csv.DictReader(f,delimiter='\t'))
n=lire('referentiels/sort_prelevements_20261103.tsv')
def f(x):
    try: return float(x)
    except: return None
d=[(r['n'],r['libelle'][:45],f(r['rendement_2026_M']),f(r['rendement_2026_revise_plf2027_M'])) for r in n if f(r['rendement_2026_revise_plf2027_M']) is not None and f(r['rendement_2026_revise_plf2027_M'])!=f(r['rendement_2026_M'])]
print('révisé numériquement différent:',len(d)); print('dont actuel vide:',sum(1 for x in d if x[2] is None))
dd=[x for x in d if x[2] is not None]; print('les deux renseignés et différents:',len(dd),round(sum(x[2] for x in dd),1),round(sum(x[3] for x in dd),1))
for x in sorted(dd,key=lambda x:-abs(x[3]-x[2]))[:8]: print('  ',x)
tot_si=sum((f(r['rendement_2026_revise_plf2027_M']) if f(r['rendement_2026_revise_plf2027_M']) is not None else (f(r['rendement_2026_M']) or 0)) for r in n)
print('total si révisé appliqué là où il existe:',round(tot_si,1))
wb=openpyxl.load_workbook('archive/tri_20261020/livrables/tri_public/Tri des prélèvements Résolution.xlsx'); ws=wb['Tri']
rows=list(ws.iter_rows(min_row=2,values_only=True)); print('xlsx oct20',len(rows),collections.Counter(r[5] for r in rows).most_common(), round(sum(r[7] for r in rows if isinstance(r[7],(int,float))),1), sum(1 for r in rows if r[7] in (None,'')))
print([ [c.value for c in row] for row in wb['Lisez-moi'].iter_rows()][:19])
wb=openpyxl.load_workbook('livrables/tri_prelevements/Tri_prelevements_export.xlsx'); ws=wb['Prélèvements']
rows=list(ws.iter_rows(min_row=2,values_only=True)); print('xlsx nov3',len(rows),collections.Counter(r[5] for r in rows).most_common(), round(sum(r[3] for r in rows if isinstance(r[3],(int,float))),1), sum(1 for r in rows if r[3] in (None,'')))
for row in wb['Présentation'].iter_rows(values_only=True): print('   ',row)
for row in wb['Synthèse'].iter_rows(values_only=True): print('   ',row)
