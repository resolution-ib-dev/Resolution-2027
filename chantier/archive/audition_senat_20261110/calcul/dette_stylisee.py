# Dynamique de dette stylisée, calée sur le central HCSP-OFCE (115,6 -> 188 % en 2050, intérêts 2,2 -> 5,2 %)
def run(prod=0.7, rg=0.5, prem_bp=0.0, pd_shift=0.0, pd_path=None, infl=1.75, emploi=0.15, mat=8.0, ret_shift=0.0):
    d=115.6; eff=2.2/115.6*100
    g=prod+emploi+infl
    out={}
    for t in range(2026,2051):
        # déficit primaire tendanciel HCSP : 2,9 -> 2,5 après effort 2026, puis dérive vers 3,0 en 2050
        pd = 2.5 + 0.5*(t-2026)/24 + pd_shift + ret_shift*(t-2026)/24
        if pd_path: pd += pd_path(t)
        marg = g + rg + prem_bp/100*max(0,d-115.6)
        eff = eff + (marg-eff)/mat + 0.0
        i = eff*d/100
        d = d*(1+0)/(1+g/100) + pd + i
        out[t]=(round(d,1), round(i,1), round(marg,2))
    return out
def show(lbl,**k):
    o=run(**k); print(f"{lbl:62s} 2035: {o[2035][0]:6.1f}  2050: {o[2050][0]:6.1f}  intérêts 2050: {o[2050][1]:4.1f} % PIB  taux marginal 2050: {o[2050][2]}")
show("Central calé (prod 0,7 ; r-g +0,5)")
show("Productivité 0,5 (moyenne observée 2005-2025)",prod=0.5)
show("Prime endogène +2 pb par point de dette > 115,6",prem_bp=2)
show("Prime endogène +4 pb par point de dette",prem_bp=4)
show("Recettes : choc élasticité type 2023-24 (-0,5 pt pérenne)",pd_shift=0.5)
pr=lambda t: min(1,(t-2026)/9)*3.2
show("Priorités HCSP non financées (+3,2 pt PIB en 2035, maintenu)",pd_path=pr)
show("Combiné prudent : prod 0,5 + prime 2 pb + choc recettes",prod=0.5,prem_bp=2,pd_shift=0.5)
show("Favorable HCSP (prod 1,0 ; r-g 0)",prod=1.0,rg=0.0)
