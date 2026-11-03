import csv,xlrd,collections,json
R='/home/user/Resolution-2027/chantier/referentiels/'
S=list(csv.DictReader(open(R+'sort_prelevements_20261015.tsv'),delimiter='\t'))
F=list(csv.DictReader(open(R+'prelevements_forces_20260930.tsv'),delimiter='\t'))
A27=[r for r in csv.DictReader((l for l in open(R+'annexe_ressources_affectees_2027.tsv') if not l.startswith('#')),delimiter='\t')]
EA=[r for r in csv.DictReader((l for l in open(R+'annexe_recettes_bg_2027.tsv') if not l.startswith('#')),delimiter='\t')]
sh=xlrd.open_workbook('/home/user/Site-ETNP/site/donnees/PLF 2026_V&M tome I - Annexe 2 - Taxes affectees_0910.xls').sheet_by_name('taxes affectées')
p26=collections.defaultdict(float); p26lib={}
for r in range(3,sh.nrows):
    c=str(sh.cell_value(r,12)).replace('.0','')
    v=sh.cell_value(r,21)
    if c and v not in ('',None):
        try: p26[c]+=float(v)/1e6; p26lib[c]=sh.cell_value(r,13)
        except: pass
a27=collections.defaultdict(float); a27lib={}; a27has=set()
for r in A27:
    c=r['ressource_code']; a27has.add(c); a27lib[c]=r['ressource_libelle']
    if r['rendement_previsionnel_2026']: a27[c]+=float(r['rendement_previsionnel_2026'])/1e6
ea={r['ligne']:r for r in EA if r['ligne']}
def f(x):
    try: return float(x)
    except: return None
out=[]
for i,(s,fr) in enumerate(zip(S,F),1):
    code=fr['code_annexe'].replace('.0',''); la=fr['ligne_etat_A'].replace('.0','')
    tri=f(s['rendement_2026_M']); aff=f(fr['rendement_affecte_2026_M']); et=f(fr['rendement_etat_2026_M'])
    d=dict(n=i,libelle=s['libelle'],nature_ligne=s['nature_ligne'],origine=fr['origine'],tri=tri,tri_etat=et,tri_affecte=aff,code_annexe=code,ligne_etat_A=la,
           plf26=round(p26[code],1) if code in p26 else None, plf27_rev26=round(a27[code],1) if code in a27has else None,
           etatA_lfi26=round(float(ea[la]['evaluation_initiale_2026_lfi'])/1e6,1) if la in ea and ea[la]['evaluation_initiale_2026_lfi'] else None,
           etatA_rev26=round(float(ea[la]['evaluation_revisee_2026_plf2027'])/1e6,1) if la in ea and ea[la]['evaluation_revisee_2026_plf2027'] else None,
           etatA_2027=round(float(ea[la]['evaluation_proposee_2027'])/1e6,1) if la in ea and ea[la]['evaluation_proposee_2027'] else None)
    # verdicts
    if code:
        src='ressources affectées'
        ref=aff if aff is not None else tri
        if code not in a27has: v='intitulé absent de l’annexe 2027'
        elif ref in (None,0) and not a27[code]: v='concordant : sans rendement des deux côtés'
        elif ref in (None,0): v='annexe seule'
        elif not a27[code]: v='rendement au tri, absent de l’annexe'
        else:
            e=(a27[code]-ref)/ref; d['ecart_pct']=round(100*e,1)
            v='concordant' if abs(e)<=0.02 else 'écart'
    elif la:
        src='état A'; ref=et if et is not None else tri
        L=d['etatA_lfi26']
        if L is None or L==0: v='rendement au tri, absent de l’annexe' if ref else 'concordant : sans rendement des deux côtés'
        elif ref in (None,0): v='annexe seule'
        else:
            e=(L-ref)/ref; d['ecart_pct']=round(100*e,1)
            v='concordant' if abs(e)<=0.02 else 'écart'
    else: src='aucune annexe'; v='rang sans ligne d’annexe ni d’état A'
    d['source']=src; d['verdict']=v
    out.append(d)
c=collections.Counter((d['source'],d['verdict']) for d in out)
for k,v in sorted(c.items()): print(v,k)
json.dump(out,open('relecture.json','w'),ensure_ascii=False,indent=0)
