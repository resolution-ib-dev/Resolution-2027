# Produit le sankey (SVG) de la présentation candidat. Md€ par an.
# Relevé : Graph1672Md (Insee 2024, 1 672), Graph236 (236), Flux (CSG-CRDS activité 114),
# Input Capitalisation (104 + 18 = 122). Déduit ici : ventilation des 166 Md€ de dépenses
# supprimées entre postes (chômage 30 et hébergement/AME 4 sur le social, le reste sur le reliquat).
S=0.14; X0,X1,W=232,500,10
conserves=[("Social","retraites, santé, solidarité",899,"≈ 900"),
           ("Éducation et recherche","",149,"149"),
           ("Régalien","défense, intérieur, justice",106,"106"),
           ("Reliquat","administrations, infrastructures, dette",352,"≈ 350")]
o=[]
def band(ya,yb,za,zb,cls):
    m=(X0+W+X1)/2
    o.append(f'<path class="{cls}" d="M{X0+W},{ya} C{m},{ya} {m},{za} {X1},{za} L{X1},{zb} C{m},{zb} {m},{yb} {X0+W},{yb} Z"/>')
# superflu
y=20; h=236*S
o.append(f'<rect class="na" x="{X0}" y="{y}" width="{W}" height="{h:.1f}"/>')
o.append(f'<text class="l b" x="{X0-8}" y="{y+h/2-2:.1f}" text-anchor="end">Dépenses superflues · 236</text>')
o.append(f'<text class="l s" x="{X0-8}" y="{y+h/2+11:.1f}" text-anchor="end">dont 52 de niches et 18 de rendement</text>')
hs,hc=114*S,122*S
ys,yc=2,54
band(y,y+hs,ys,ys+hs,"fa"); band(y+hs,y+h,yc,yc+hc,"fa")
for (yy,hh,t,v,s1) in [(ys,hs,"Salaire net","114","+13 % de net dès la première année, +300 € par mois"),
                       (yc,hc,"Capitalisation","122","comptes épargne retraite personnels, +300 € par mois")]:
    o.append(f'<rect class="na" x="{X1}" y="{yy}" width="{W}" height="{hh:.1f}"/>')
    o.append(f'<text class="l b" x="{X1+W+8}" y="{yy+hh/2-2:.1f}">{t} · {v}</text>')
    o.append(f'<text class="l s" x="{X1+W+8}" y="{yy+hh/2+11:.1f}">{s1}</text>')
y=96; y0=y
for (t,s,v,lab) in conserves:
    h=v*S
    o.append(f'<rect class="nc" x="{X0}" y="{y}" width="{W}" height="{h:.1f}"/>')
    band(y,y+h,y,y+h,"fc")
    o.append(f'<rect class="nc" x="{X1}" y="{y}" width="{W}" height="{h:.1f}"/>')
    if s and h>30:
        o.append(f'<text class="l b" x="{X0-8}" y="{y+h/2-2:.1f}" text-anchor="end">{t} · {lab}</text>')
        o.append(f'<text class="l s" x="{X0-8}" y="{y+h/2+11:.1f}" text-anchor="end">{s}</text>')
    else:
        o.append(f'<text class="l b" x="{X0-8}" y="{y+h/2+4:.1f}" text-anchor="end">{t} · {lab}</text>')
    y+=h+6
y1=y-6
o.append(f'<path class="acc" d="M{X1+W+6},{y0} h5 V{y1} h-5"/>')
o.append(f'<text class="l b" x="{X1+W+18}" y="{(y0+y1)/2-2:.1f}">Dépenses conservées · ≈ 1 500</text>')
o.append(f'<text class="l s" x="{X1+W+18}" y="{(y0+y1)/2+11:.1f}">sécurité, solidarité, éducation : inchangées en volume</text>')
H=y1+4
open('sankey.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 {H:.0f}" role="img" aria-label="Flux annuels de la dépense publique, en milliards d\'euros">'+''.join(o)+'</svg>')
print(H)
