import xlrd,csv,json,re,sys,collections
sys.path.insert(0,'.'); sys.path.insert(0,'/home/user/Resolution-2027')
import droit
n=droit.norm_num
sh=xlrd.open_workbook('/home/user/Site-ETNP/site/donnees/PLF 2026_V&M tome II - Annexe 3 - Depenses fiscales - 0910.xls').sheet_by_name('Chiffrages Résolution')
NS={r['numero']:r for r in csv.DictReader(open('/home/user/Resolution-2027/chantier/referentiels/niches_sieges_20261004.tsv'),delimiter='\t')}
BIL=open('/home/user/Resolution-2027/chantier/referentiels/annexe_evolution_df_bilan_2027.tsv').read()
BOR=open('/home/user/Resolution-2027/chantier/referentiels/annexe_evolution_df_bornees_2027.tsv').read()
V=json.load(open('visas.json'))
VA={}
for v in V: VA.setdefault(n(v['article']),[]).append(v)
rows=[]
for r in range(6,sh.nrows):
    num=str(sh.cell_value(r,3)).replace('.0','')
    if not num.strip(): continue
    cat=sh.cell_value(r,0); sort=str(sh.cell_value(r,12)); se=str(sh.cell_value(r,15)); typ=str(sh.cell_value(r,16))
    ns=NS.get(num,{})
    code=ns.get('code_ou_texte_porteur',''); art=ns.get('siege_article','')
    base=re.match(r"[A-Z]?\.?\s?[\d]+(?:-\d+)*(?: [a-z]+(?: [A-Z]+)?)?(?: [A-Z]{1,3})?", art.strip()) if art else None
    b=base.group(0).strip() if base else ''
    hits=[f"{v['liasse']} n°{v['n']}" for v in VA.get(n(b),[])] if b else []
    rows.append(dict(numero=num,cat=cat,sort=sort,se=se,typ=typ,code=code,siege=art,base=b,nominatif=sorted(set(hits)),bilan=num in BIL,bornee=num in BOR,etat=ns.get('etat_droit_20261001','')))
c=collections.Counter((x['sort'] or '(vide)') for x in rows); print(len(rows),c)
print(collections.Counter(x['code'] for x in rows).most_common(12))
json.dump(rows,open('niches.json','w'),ensure_ascii=False,indent=0)
