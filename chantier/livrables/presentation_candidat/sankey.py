# Sankey de la présentation candidat. Md€ par an. Seul le superflu sort ; le reste est conservé.
# Relevé : Graph1672Md (Insee 2024), Graph236, Flux (CSG-CRDS activité 114), Input Capitalisation (104 + 18).
# Déduit ici : ventilation par poste des dépenses conservées (ordre de grandeur).
S=0.16; X0,W,X1=178,14,440
N=chr(0xa0); F=chr(0x202f)
U='https://france-resolution.fr/'
def A(h,x): return f'<a href="{U}{h}">{x}</a>'
o=[]
def band(ya,yb,za,zb):
    m=(X0+W+X1)/2
    o.append(f'<path class="fa" d="M{X0+W},{ya:.1f} C{m},{ya:.1f} {m},{za:.1f} {X1},{za:.1f} L{X1},{zb:.1f} C{m},{zb:.1f} {m},{yb:.1f} {X0+W},{yb:.1f} Z"/>')
y=18; h=236*S; hs,hc=114*S,122*S
o.append(f'<text class="l s" x="{X0+W}" y="8" text-anchor="end">Dépenses publiques aujourd’hui</text>')
o.append(f'<rect class="na" x="{X0}" y="{y}" width="{W}" height="{h:.1f}"/>')
o.append(A('graphiques/economies.html',f'<text class="l b" x="{X0-8}" y="{y+h/2-3:.1f}" text-anchor="end">Superflu · 236</text>'))
o.append(f'<text class="l s" x="{X0-8}" y="{y+h/2+13:.1f}" text-anchor="end">rendu chaque année</text>')
ys,yc=8,106
band(y,y+hs,ys,ys+hs); band(y+hs,y+h,yc,yc+hc)
# salaire net
o.append(f'<rect class="na" x="{X1}" y="{ys}" width="10" height="{hs:.1f}"/>')
o.append(A('propositions.html#sal',f'<text class="l b g" x="{X1+20}" y="{ys+hs/2-1:.1f}">Salaire net · 114</text>'))
o.append(f'<text class="l s" x="{X1+20}" y="{ys+hs/2+19:.1f}"><tspan class="fort">+13{N}%</tspan> dès la première année</text>')
o.append(f'<text class="l s" x="{X1+20}" y="{ys+hs/2+36:.1f}">+300{N}€ par mois au salaire médian</text>')
# compte épargne : la carte
cx,cy,cw,ch=X1+10,yc-19,350,hc+38
o.append(f'<rect class="na" x="{X1}" y="{yc}" width="10" height="{hc:.1f}"/>')
o.append(f'<rect class="carte" x="{cx}" y="{cy:.1f}" width="{cw}" height="{ch:.1f}" rx="7"/>')
gx,gb=cx+14,cy+ch-14
for i,hh in enumerate((10,17,24,31)):
    o.append(f'<rect class="na" x="{gx+i*8}" y="{gb-hh:.1f}" width="5.5" height="{hh}" rx="1"/>')
o.append(A('propositions.html#eparg',f'<text class="l b g" x="{gx+44}" y="{cy+ch/2-4:.1f}">Compte épargne personnel · 122</text>'))
o.append(f'<text class="l s" x="{gx+44}" y="{cy+ch/2+15:.1f}">+300{N}€ par mois au salaire médian, à mon nom</text>')
# patrimoine rendu : la bulle d'amorce
bx,by,r=cx+cw/2-30,cy+ch+106,70
o.append(f'<circle class="bulle" cx="{bx}" cy="{by:.1f}" r="{r}"/>')
o.append(A('graphiques/patrimoine-public.html',f'<text class="l b" x="{bx}" y="{by-24:.1f}" text-anchor="middle">Patrimoine rendu</text>'))
o.append(f'<text class="l b gg" x="{bx}" y="{by+4:.1f}" text-anchor="middle">600{N}Md€</text>')
o.append(f'<text class="l s" x="{bx}" y="{by+24:.1f}" text-anchor="middle">20{F}000{N}€ par foyer</text>')
a0,a1=by-r-3,cy+ch+4
o.append(f'<path class="fl" d="M{bx},{a0:.1f} V{a1+7:.1f}"/><path class="na" d="M{bx-6},{a1+9:.1f} L{bx},{a1:.1f} L{bx+6},{a1+9:.1f} Z"/>')
o.append(f'<text class="l b" x="{bx+12}" y="{(a0+a1)/2+1:.1f}">L’amorce</text>')
o.append(f'<text class="l s" x="{bx+12}" y="{(a0+a1)/2+17:.1f}">versée d’emblée sur le compte</text>')
# conservé : un bloc, sans flux
y=y+h+8; y0=y
for (t,v,lab) in [("Social",899,"≈ 900"),("Éducation et recherche",149,"149"),("Régalien",106,"106"),("Administration",352,"≈ 350")]:
    hh=v*S
    o.append(f'<rect class="nc" x="{X0}" y="{y:.1f}" width="{W}" height="{hh:.1f}"/>')
    o.append(f'<text class="l" x="{X0-8}" y="{y+hh/2+4:.1f}" text-anchor="end">{t} · {lab}</text>')
    y+=hh+2
y1=y-2
o.append(f'<path class="acc" d="M{X0+W+5},{y0:.1f} h5 V{y1:.1f} h-5"/>')
o.append(A('graphiques/depense-publique.html',f'<text class="l b" x="{X0+W+17}" y="{(y0+y1)/2+18:.1f}">Conservé · ≈ 1{F}500</text>'))
o.append(f'<text class="l s" x="{X0+W+17}" y="{(y0+y1)/2+35:.1f}">sécurité, solidarité, éducation</text>')
H=max(y1,by+r)+4
open('sankey.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -8 810 {H+8:.0f}" role="img" aria-label="Flux annuels de la dépense publique, en milliards d\'euros">'+''.join(o)+'</svg>')
