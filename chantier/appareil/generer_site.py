#!/usr/bin/env python3
"""Le site — un index et dix-huit fiches, en pages statiques.

Dérivé. Ne se corrige jamais à la main : il se régénère (A-123). Un chiffre qui
change se corrige au référentiel, `make` régénère, on redéploie.

Structure arbitrée par l'auteur le 20260828 : vingt fichiers.

    site/index.html            l'entrée, puis les dix-huit fiches listées par
                               groupe, chacune avec son axe
    site/fiches/<slug>.html    une fiche par page, avec son adresse
    site/fiche.css             la feuille de la galerie, plus la couche du site
    site/404.html

Chaque fiche a son adresse : c'est ce qui la rend citable et envoyable, et c'est
la raison de cette structure (A-48, le journaliste cite). Le prix payé est
qu'on ne lit plus la série d'un trait, et il est assumé.

Le rendu d'une carte ne se redessine pas ici : `generer_fiches.py` le porte, et
ce module l'importe. Une seule source pour la fiche, comme
`structure_fiches.py` est la seule source de la série.

Ce que le site ne porte pas, et le déclare par son silence : ni manifeste, ni
note, ni vidéo. A-59 interdit d'annoncer ce qui n'existe pas.

L'entrée ne porte aucun chiffre. Hiérarchiser les montants est un arbitrage
d'édition et il appartient à l'auteur (A-179) ; les dix-huit axes sont la
promesse, et ils sont écrits.

Emploi : python3 generer_site.py ../referentiels/positions.json \
                                 ../referentiels/REF_doctrine.json ../site \
                                 ../sources/1pager_20260806_v1_proto.html
"""
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generer_fiches import (  # noqa: E402
    FICHES, STYLE, e, fiche, matiere,
)
import manifeste as MANIF  # noqa: E402

MARQUE = 'Résolution'
SERVICE = 'Ce que le plan change pour vous'

# Une seule ligne de copie neuve dans tout le site. Elle dit la règle de
# lecture, elle ne promet rien qu'une fiche ne tienne.
CHAPEAU = ('Dix-huit situations. Chaque fiche dit ce que le plan vous donne, '
           'et ce qu’il vous retire.')


def slug(titre):
    """L'adresse d'une fiche se dérive de son titre arbitré, jamais d'une table.

    Une table de slugs écrite à la main serait un second endroit où le nom
    d'une fiche vit, donc un endroit d'où il peut diverger.
    """
    t = unicodedata.normalize('NFKD', titre)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = t.lower().replace('’', ' ').replace("'", ' ')
    t = re.sub(r'[^a-z0-9]+', '-', t)
    return t.strip('-')


# --- la page de garde, projetée ---------------------------------------------
#
# `sources/ResolutionD1a.png` est la page de garde arrêtée par l'auteur : fond
# brique strié, sans condensé très gras, titre en deux couleurs, les auteurs et
# la marque en tête, trois appels à l'action, la promesse chiffrée, une barre de
# rubriques et la date de parution. Le site s'ouvre dessus.
#
# Tout ce qui s'y lit vient de cette page de garde. Ce qui n'existe pas encore —
# le manifeste, les vidéos, les trois appels — est **marqué comme tel** au lieu
# d'être promis en silence (A-59). Le seul lien qui mène quelque part est celui
# des propositions : les dix-huit fiches.
BRIQUE = '#b23a10'
BRIQUE_CLAIR = '#b84923'
OR = '#ffd24a'
CREME_GARDE = '#fffdf2'

AUTEURS = [('Ingrid', 'Barrat'), ('Arthur', 'Marle'), ('Moïse', 'Mitterrand')]
TITRE_UN = 'État partout,'
TITRE_DEUX = 'justice nulle part'
PROMESSE_A = 'Vous rendre'
PROMESSE_CHIFFRE = '600 €'
PROMESSE_B = 'par mois'
PARUTION = 'le 9 octobre'
# Le lien de précommande existe : « Le livre » cesse donc d'être un appel mort et
# devient le seul appel qui mène quelque part. Les deux autres restent marqués.
PRECOMMANDE = ('https://www.amazon.fr/%C3%89tat-partout-justice-nulle-part'
               '/dp/236602648X')
CONTACT = 'contact@france-resolution.fr'
# Le site est statique : il ne collecte rien lui-même (A-190). L'adhésion se
# recueille donc par courrier électronique — l'adresse arrive dans la boîte du
# mouvement, sans base, sans formulaire, sans traitement intermédiaire.
MAILTO_ADHESION = (
    f'mailto:{CONTACT}'
    '?subject=J%E2%80%99adh%C3%A8re%20au%20manifeste'
    '&body=Je%20soutiens%20le%20manifeste%20R%C3%A9solution.%0A%0A'
    'Nom%20%3A%0APr%C3%A9nom%20%3A%0A%0A'
    'J%E2%80%99accepte%20de%20recevoir%20le%20manifeste%20et%20les%20nouvelles'
    '%20du%20mouvement%20%C3%A0%20cette%20adresse.%0A')
MAILTO_EXPRESSION = (
    f'mailto:{CONTACT}'
    '?subject=Je%20m%E2%80%99exprime')
# (intitulé, plein, adresse ou None)
# (intitulé, style, adresse) — style : 'plein' crème, 'filaire' or, 'vif' or
# plein. Les trois viennent de la page de garde, sauf la précommande, que
# l'auteur veut en or plein et nommée : c'est le seul appel qui vend le livre.
APPELS = [('J’adhère au manifeste', 'plein', 'adherer'),
          ('Je m’exprime', 'filaire', 'contact'),
          ('Précommander le livre', 'vif', PRECOMMANDE)]
# Les intitulés et les couleurs sont ceux de la page de garde, et ils ne
# changent pas : « Le livre » reste « Le livre », le premier appel reste en
# crème plein, les deux autres en or filaire. Seules les adresses ont été
# ajoutées. Une modification qui ne vient pas d'une consigne est une occasion
# de se tromper (A-212).
RUBRIQUES = [('Manifeste', 'manifeste'), ('Propositions', 'propositions'),
             ('Vidéos', None)]
# Les mêmes destinations, écrites selon la forme : fragments pour la page
# unique, fichiers pour le site déployé. Une seule table, deux résolutions.
LIENS_FRAGMENTS = {'propositions': '#sommaire', 'manifeste': '#manifeste',
                   'adherer': '#adherer', 'accueil': '#accueil',
                   'contact': '#contact'}
LIENS_FICHIERS = {'propositions': 'index.html#sommaire',
                  'manifeste': 'manifeste.html', 'adherer': 'adherer.html',
                  'accueil': 'index.html', 'contact': 'contact.html'}

STYLE_GARDE = """
/* --- la page de garde -----------------------------------------------------
   Projection de `ResolutionD1a`. Elle a sa propre langue typographique — un
   sans condensé très gras sur fond brique — et elle ne partage rien avec la
   fiche, qui reste en Fraunces sur papier crème. Les deux se suivent sans se
   mélanger : la garde annonce, la fiche démontre. */
@import url('https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&display=swap');

.a-fond{
 --briq:BRIQUE; --briqc:BRIQUE_CLAIR; --dor:OR; --crm:CREME_GARDE;
 margin:-1.4rem -1rem;padding:2.4rem clamp(1.2rem,4vw,3.2rem) 1.4rem;
 background:var(--briq);
 background-image:repeating-linear-gradient(90deg,
   var(--briqc) 0 2px, transparent 2px 22px);
 min-height:calc(100vh + 1.4rem);display:flex;flex-direction:column;
 font-family:Archivo,'Archivo Narrow','Arial Narrow','Helvetica Neue',
   Arial,sans-serif;color:var(--crm)}
.a-cond{font-weight:900;font-stretch:66%;
 font-variation-settings:'wdth' 66,'wght' 900;
 text-transform:uppercase;line-height:.88;letter-spacing:-.008em}

.a-haut{display:flex;flex-wrap:wrap;gap:1.4rem 2rem;
 justify-content:space-between;align-items:flex-start}
.a-sig{margin:0;font-size:clamp(1.05rem,2.4vw,1.5rem);line-height:1.32;
 color:var(--dor);max-width:22ch}
.a-sig b{color:var(--crm);font-weight:700}
.a-marque{display:block;margin-top:.6rem;font-size:.7rem;font-weight:700;
 letter-spacing:.42em;text-transform:uppercase;color:var(--dor)}

.a-appels{display:flex;flex-wrap:wrap;gap:.55rem;align-items:flex-start}
.a-appel{position:relative;font:700 .95rem/1 Archivo,'Arial Narrow',Arial,sans-serif;
 padding:.85rem 1.25rem;border:1px solid var(--dor);background:none;
 color:var(--dor);cursor:not-allowed}
.a-appel.a-plein{background:var(--crm);border-color:var(--crm);
 color:var(--briq)}
.a-appel.a-lien{cursor:pointer;text-decoration:none;display:inline-block}
.a-appel.a-lien:hover{background:rgba(255,210,74,.16)}
.a-appel.a-lien.a-plein:hover{background:var(--dor);border-color:var(--dor)}
.a-appel.a-lien:focus-visible{outline:2px solid var(--crm);outline-offset:3px}
/* La précommande en or plein : c'est le seul appel qui vend le livre, et il se
   distingue des deux autres. Arbitrage de l'auteur. */
.a-appel.a-vif{background:var(--dor);border-color:var(--dor);
 color:var(--briq)}
.a-appel.a-vif:hover{background:var(--crm);border-color:var(--crm)}
.a-bientot{display:block;margin-top:.3rem;font:400 .6rem/1 Archivo,'Arial Narrow',Arial,sans-serif;
 letter-spacing:.14em;text-transform:uppercase;opacity:.72}

.a-corps{flex:1;display:flex;flex-direction:column;justify-content:center;
 padding:2.6rem 0 1.4rem}
.a-titre{font-size:clamp(2.9rem,11.2vw,8.2rem);margin:0;color:var(--crm);
 text-wrap:balance}
.a-titre span{display:block;color:var(--dor)}
.a-promesse{display:flex;flex-wrap:wrap;align-items:baseline;
 gap:.5rem 1.8rem;margin:2.2rem 0 0}
.a-promesse p{margin:0;font-size:clamp(1.4rem,4.4vw,2.5rem);font-weight:800;
 font-variation-settings:'wdth' 84,'wght' 800;line-height:1.04;
 color:var(--crm)}
.a-promesse b{color:var(--dor);font-weight:800}
.a-parici{font:700 1.05rem/1 Archivo,'Arial Narrow',Arial,sans-serif;color:var(--dor);
 text-decoration:none;border-bottom:2px solid var(--dor);padding-bottom:.28rem}
.a-parici:hover{color:var(--crm);border-color:var(--crm)}
.a-parici:focus-visible,.a-rub a:focus-visible{outline:2px solid var(--crm);
 outline-offset:4px}

.a-filet{border:0;border-top:1px solid rgba(255,210,74,.42);margin:0}
.a-bas{display:flex;flex-wrap:wrap;gap:.7rem 2.4rem;align-items:baseline;
 justify-content:space-between;padding-top:1.1rem}
.a-rub{display:flex;flex-wrap:wrap;gap:.7rem 2.2rem;list-style:none;
 margin:0;padding:0}
.a-rub a,.a-rub span{font-size:.76rem;font-weight:700;letter-spacing:.24em;
 text-transform:uppercase;text-decoration:none;color:var(--crm);
 border-bottom:2px solid transparent;padding-bottom:.2rem}
.a-rub a:hover{color:var(--dor);border-bottom-color:var(--dor)}
.a-rub span{color:rgba(255,253,242,.44)}
.a-rub span::after{content:' · à venir';letter-spacing:.1em;
 text-transform:none;font-weight:400}
.a-date{margin:0;font-size:.86rem;color:var(--dor)}
.a-date b{color:var(--crm);font-weight:700}
""".replace('BRIQUE_CLAIR', BRIQUE_CLAIR).replace('BRIQUE', BRIQUE) \
   .replace('OR', OR).replace('CREME_GARDE', CREME_GARDE)


def page_garde(liens):
    """La page de garde codée. Rien n'y est inventé : tout est sur l'image."""
    sig = ' · '.join(f'{p} <b>{n}</b>' for p, n in AUTEURS)
    SUFFIXE = {'plein': ' a-plein', 'vif': ' a-vif', 'filaire': ''}

    def un_appel(t, style, lien):
        suf = SUFFIXE[style]
        if not lien:
            return (f'<button class="a-appel{suf}" type=button '
                    f'aria-disabled=true>{e(t)}'
                    f'<span class=a-bientot>bientôt</span></button>')
        cible = (' target=_blank rel="noopener noreferrer"'
                 if lien.startswith('http') else '')
        return (f'<a class="a-appel a-lien{suf}" href="{lien}"{cible}>'
                f'{e(t)}</a>')

    def resoudre(cle):
        return liens.get(cle, cle) if cle else None

    appels = ''.join(
        un_appel(t, style, lien if (lien or '').startswith('mailto:')
                 or (lien or '').startswith('http') else resoudre(lien))
        for t, style, lien in APPELS)
    rubs = ''.join(
        (f'<li><a href="{resoudre(lien)}">{e(t)}</a></li>' if lien
         else f'<li><span>{e(t)}</span></li>')
        for t, lien in RUBRIQUES)
    return (
        '<div class=a-fond>'
        '<div class=a-haut>'
        f'<p class=a-sig>{sig}<span class=a-marque>{MARQUE}</span></p>'
        f'<div class=a-appels>{appels}</div>'
        '</div>'
        '<div class=a-corps>'
        f'<h1 class="a-titre a-cond">{e(TITRE_UN)}'
        f'<span>{e(TITRE_DEUX)}</span></h1>'
        '<div class=a-promesse>'
        f'<p class=a-cond>{e(PROMESSE_A)} <b>{e(PROMESSE_CHIFFRE)}</b> '
        f'{e(PROMESSE_B)}</p>'
        f'<a class=a-parici href="{resoudre("manifeste")}">'
        f'C’est par ici →</a>'
        '</div></div>'
        '<hr class=a-filet>'
        f'<div class=a-bas><ul class=a-rub>{rubs}</ul>'
        f'<p class=a-date>En librairie <b>{e(PARUTION)}</b></p></div>'
        '</div>')


# --- le manifeste et l'adhésion --------------------------------------------
STYLE_PAGES = """
/* --- manifeste et adhésion ------------------------------------------------
   Même papier crème que la fiche, colonne de lecture plus étroite : c'est du
   texte suivi, pas une carte. */
.m-page{max-width:44rem;margin:0 auto 1.4rem;background:var(--pap);
 box-shadow:0 2px 0 rgba(0,0,0,.35)}

/* Le manifeste porte la charte du livre, non celle de la fiche : fond brique
   strié, Archivo, or et crème. C'est le produit phare, il parle la langue de
   la couverture. Arbitrage de l'auteur du 20260828. */
.g-page{--briq:#b23a10; --briqc:#b84923; --dor:#ffd24a; --crm:#fffdf2;
 max-width:46rem;margin:0 auto 1.4rem;background:var(--briq);
 background-image:repeating-linear-gradient(90deg,
   var(--briqc) 0 2px, transparent 2px 22px);
 color:var(--crm);
 font-family:Archivo,'Archivo Narrow','Arial Narrow',Arial,sans-serif}
.g-page .g-corps{padding:2.2rem clamp(1.3rem,4.4vw,3rem) 2.8rem}
.g-marque{display:flex;align-items:baseline;justify-content:space-between;
 gap:1rem;font:700 11px/1 Archivo,'Arial Narrow',sans-serif;
 letter-spacing:.34em;text-transform:uppercase;color:var(--crm)}
.g-marque em{font-style:normal;letter-spacing:.1em;text-transform:none;
 font-weight:400}
.g-filet{display:flex;height:4px;margin:.9rem 0 1.6rem}
.g-filet i{flex:1;background:var(--dor)}
.g-filet i:nth-child(2){flex:.45;background:rgba(255,253,242,.5)}
.g-filet i:nth-child(3){flex:.2;background:rgba(255,253,242,.22)}
.g-page.m-page .m-titre{font-size:clamp(1.9rem,6.4vw,3.3rem);font-weight:900;
 font-stretch:66%;font-variation-settings:'wdth' 66,'wght' 900;
 text-transform:uppercase;line-height:.92;letter-spacing:-.008em;
 color:var(--crm);margin:0 0 2.2rem}
/* L'or sur le brique ne dépasse pas 3:1 de contraste : il tient pour un filet
   ou une vedette, pas pour du texte. Les intertitres passent donc en crème, et
   l'or reste à la ligne qui les souligne. */
.g-page.m-page h2{font:600 10.5px/1 Archivo,'Arial Narrow',sans-serif;
 letter-spacing:.28em;text-transform:uppercase;color:var(--crm);
 margin:2.8rem 0 1.1rem;padding-bottom:.55rem;
 border-bottom:1px solid rgba(255,210,74,.55)}
.g-page.m-page .bloc{margin:0 0 1.5rem}
/* Un peu plus petit, un peu plus aéré, un peu moins gras : le texte suivi se
   lit, il ne s'affiche pas. Le gras reste sur l'affirmation seule. */
.g-page.m-page .affirmation{display:inline;margin:0;font-weight:700;
 font-variation-settings:'wdth' 94,'wght' 700;font-size:1rem;line-height:1.6;
 color:var(--crm)}
/* Aucune transparence sur le fond strié : elle laissait un gris illisible.
   L'appui se distingue de l'affirmation par le poids, pas par l'opacité. */
.g-page.m-page .appui{display:inline;margin:0;font-size:.97rem;
 line-height:1.66;color:var(--crm);font-weight:400}
.g-page.m-page ul.mesures{list-style:none;margin:0;padding:0;display:grid;
 gap:1.3rem}
.g-page.m-page li.mesure{padding-left:1.15rem;
 border-left:2px solid var(--dor)}
.g-outils{display:flex;flex-wrap:wrap;gap:.6rem;margin:2.6rem 0 0;
 padding-top:1.5rem;border-top:1px solid rgba(255,210,74,.38)}
.g-bouton{font:700 .9rem/1 Archivo,'Arial Narrow',Arial,sans-serif;
 cursor:pointer;text-decoration:none;padding:.85rem 1.25rem;
 border:1px solid var(--dor);background:none;color:var(--dor);
 display:inline-block}
.g-bouton.g-plein{background:var(--crm);border-color:var(--crm);
 color:var(--briq)}
.g-bouton:hover{background:rgba(255,210,74,.16)}
.g-bouton.g-plein:hover{background:var(--dor);border-color:var(--dor)}
.g-bouton:focus-visible{outline:2px solid var(--crm);outline-offset:3px}
/* Ces règles sont celles de la fiche — Fraunces sur papier crème. Le
   manifeste partage les mêmes classes de contenu et porte une autre
   charte : il est exclu ici, une fois, au lieu de surenchérir en
   spécificité à chaque règle (A-215, A-220). */
.m-page:not(.g-page) .m-corps{padding:1.6rem clamp(1.2rem,4vw,2.6rem) 2.2rem}
.m-titre{font-size:clamp(1.9rem,5.4vw,3rem);line-height:1.04;font-weight:700;
 margin:.2rem 0 1.4rem;color:var(--enc);text-wrap:balance}
.m-page:not(.g-page) .m-corps h2{font:700 11px/1 var(--mono);letter-spacing:.22em;
 text-transform:uppercase;color:var(--ocre);margin:2.2rem 0 .7rem;
 padding-bottom:.5rem;border-bottom:1px solid var(--fil)}
.m-page:not(.g-page) .m-corps .bloc{margin:0 0 1.1rem}
.m-page:not(.g-page) .m-corps .affirmation{margin:0;font-weight:700;font-size:1.06rem;
 line-height:1.4;color:var(--enc)}
.m-page:not(.g-page) .m-corps .appui{margin:.2rem 0 0;font-size:1rem;line-height:1.5;
 color:var(--gris)}
.m-page:not(.g-page) .m-corps .bloc .appui{display:inline}
.m-page:not(.g-page) .m-corps .bloc .affirmation{display:inline}
.m-page:not(.g-page) .m-corps ul.mesures{list-style:none;margin:0;padding:0;display:grid;
 gap:.85rem}
.m-page:not(.g-page) .m-corps li.mesure{padding-left:1rem;border-left:3px solid var(--gain)}
.m-page:not(.g-page) .m-corps li.mesure .affirmation{font-weight:700}
.m-page:not(.g-page) .m-corps li.mesure .appui{color:var(--gris)}
.m-outils{display:flex;flex-wrap:wrap;gap:.6rem;margin:2.4rem 0 0;
 padding-top:1.4rem;border-top:1px solid var(--fil)}
.m-bouton{font:700 .86rem/1 var(--titre);cursor:pointer;text-decoration:none;
 padding:.75rem 1.1rem;border:1px solid var(--enc);background:none;
 color:var(--enc)}
.m-bouton.m-plein{background:var(--gain);border-color:var(--gain);
 color:var(--pap)}
.m-bouton:hover{background:var(--sable)}
.m-bouton.m-plein:hover{background:var(--enc);border-color:var(--enc)}
.m-bouton:focus-visible{outline:2px solid var(--gain);outline-offset:3px}

.m-rgpd{margin:1.6rem 0 0;padding:1.1rem 1.2rem;background:var(--sable);
 border-left:3px solid var(--ocre)}
.m-rgpd h3{font:700 11px/1 var(--mono);letter-spacing:.18em;
 text-transform:uppercase;color:var(--ocre);margin:0 0 .6rem}
.m-rgpd p{margin:0 0 .5rem;font-size:.88rem;line-height:1.5;color:var(--gris)}
.m-rgpd p:last-child{margin-bottom:0}
.m-rgpd a{color:var(--gain);text-decoration-thickness:1px;
 text-underline-offset:2px}
.m-rgpd a:hover{color:var(--enc)}
.m-partage{display:flex;flex-wrap:wrap;gap:.5rem;margin:1rem 0 0}
.m-chapeau{margin:.5rem 0 0;font-size:1rem;line-height:1.5;color:var(--gris);
 max-width:38rem}
.m-note{margin:.9rem 0 0;font-size:.92rem;line-height:1.5;color:var(--gris)}
.m-note a{color:var(--gain)}
.m-adresse{margin:.6rem 0 0;padding:1.1rem 1.2rem;background:var(--sable);
 border-left:3px solid var(--gain)}
.m-adr-lab{margin:0;font:700 10px/1 var(--mono);letter-spacing:.2em;
 text-transform:uppercase;color:var(--ocre)}
.m-adr{margin:.45rem 0 0;font:700 clamp(1.05rem,3.4vw,1.5rem)/1.2 var(--mono);
 color:var(--enc);word-break:break-all;user-select:all}
.m-part{font:700 .8rem/1 var(--mono);letter-spacing:.06em;text-decoration:none;
 padding:.65rem .95rem;border:1px solid var(--fil);color:var(--enc)}
.m-part:hover{background:var(--sable);border-color:var(--enc)}
.m-etape{font:700 11px/1 var(--mono);letter-spacing:.18em;
 text-transform:uppercase;color:var(--ocre);margin:1.8rem 0 .5rem}

@media print{
 body{background:#fff;padding:0}
 .m-page{box-shadow:none;max-width:none}
 .s-nav,.s-retour,.m-outils,.g-outils,.s-pied{display:none}
 /* À l'impression le fond brique disparaît — l'encre coûte, et le texte doit
    rester lisible en noir sur blanc. La signature tient par le filet et par
    la typographie. */
 .g-page{background:#fff;background-image:none;color:#1a1a1a;max-width:none;
  margin:0}
 .g-page .affirmation,.g-page .m-titre{color:#1a1a1a}
 .g-page .appui{color:#3a3a3a}
 .g-page h2{color:#6b5b3e;border-bottom-color:#ddd7cd}
 .g-marque{color:#6b5b3e}
 .g-page li.mesure{border-left-color:#1f5c3a}
 .g-filet i{background:#1f5c3a}
 .g-filet i:nth-child(2){background:#6b5b3e}
 .g-filet i:nth-child(3){background:#8a2f22}
}
"""

RESEAUX = [
    ('Facebook', 'https://www.facebook.com/sharer/sharer.php?u='),
    ('X', 'https://twitter.com/intent/tweet?url='),
    ('LinkedIn', 'https://www.linkedin.com/sharing/share-offsite/?url='),
    ('Bluesky', 'https://bsky.app/intent/compose?text='),
    ('WhatsApp', 'https://api.whatsapp.com/send?text='),
    ('Telegram', 'https://t.me/share/url?url='),
    ('Reddit', 'https://www.reddit.com/submit?url='),
    ('Threads', 'https://www.threads.net/intent/post?text='),
    ('Mastodon', 'https://mastodonshare.com/?url='),
    ('Courriel', 'mailto:?subject=Le%20manifeste%20R%C3%A9solution&body='),
]

# Le partage a besoin de l'adresse de la page, qui n'est pas connue à la
# génération : le script la lit au clic. Aucun lien n'est donc écrit en dur.
SCRIPT_PARTAGE = """
(function () {
  // Le lecteur d'une page publiée bloque la navigation « mailto: » depuis un
  // cadre isolé : le bouton restait sans effet. L'adresse est donc toujours
  // écrite en clair, et un bouton la copie. Le lien mailto reste, en second.
  var boutons = document.querySelectorAll('[data-copier]');
  for (var i = 0; i < boutons.length; i++) {
    (function (b) {
      var dit = b.textContent;
      b.addEventListener('click', function () {
        var t = b.getAttribute('data-copier');
        function fini(ok) {
          b.textContent = ok ? 'Copié' : 'Sélectionnez l\u2019adresse';
          setTimeout(function () { b.textContent = dit; }, 2200);
        }
        try {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(t).then(function () { fini(true); },
                                                  function () { fini(false); });
            return;
          }
        } catch (err) { /* rien : on retombe sur la sélection */ }
        var cible = document.getElementById(b.getAttribute('data-cible'));
        if (cible && window.getSelection) {
          var r = document.createRange();
          r.selectNodeContents(cible);
          window.getSelection().removeAllRanges();
          window.getSelection().addRange(r);
        }
        fini(false);
      });
    })(boutons[i]);
  }
})();

(function () {
  var liens = document.querySelectorAll('[data-partage]');
  for (var i = 0; i < liens.length; i++) {
    (function (a) {
      a.addEventListener('click', function (ev) {
        ev.preventDefault();
        var u = encodeURIComponent(location.href.split('#')[0]);
        window.open(a.getAttribute('data-partage') + u, '_blank',
                    'noopener,noreferrer,width=640,height=560');
      });
    })(liens[i]);
  }
})();
"""


def bloc_manifeste(proto):
    """Le corps du manifeste : le texte du proto, corrigé et rien de plus."""
    d = proto.index('<article id="1-pager">')
    d = proto.index('>', d) + 1
    f = proto.index('</article>')
    corps = MANIF.corriger(proto[d:f])
    # Le titre était laissé en attente au proto ; il est arrêté depuis.
    corps = re.sub(r'<p class="titre-a-arreter"[^>]*>.*?</p>',
                   f'<p class=m-titre>{e(MANIF.TITRE)}</p>', corps,
                   count=1, flags=re.S)
    return corps.strip()


def page_manifeste(proto, liens=None, fichier=None):
    """Le manifeste, à la charte du livre. Affichable, imprimable, téléchargeable."""
    liens = liens or LIENS_FICHIERS
    outils = [f'<a class="g-bouton g-plein" href="{liens["adherer"]}">'
              f'J’adhère au manifeste</a>',
              '<button class=g-bouton type=button onclick="window.print()">'
              'Télécharger en PDF</button>']
    if fichier:
        outils.append(f'<a class=g-bouton href="{fichier}" download>'
                      f'Télécharger la page</a>')
    return ('<div class="m-page g-page"><div class="m-corps g-corps">'
            f'<div class=g-marque><span>{MARQUE}</span>'
            f'<em>En librairie {e(PARUTION)}</em></div>'
            '<div class=g-filet><i></i><i></i><i></i></div>'
            + bloc_manifeste(proto)
            + '<div class=g-outils>' + ''.join(outils) + '</div>'
            + '</div></div>')


def bloc_adresse(mailto, intitule):
    """L'adresse en clair, un bouton qui la copie, et le courriel en second.

    La navigation « mailto: » est bloquée depuis le cadre isolé d'une page
    publiée : un bouton qui n'ouvre rien est pire que pas de bouton. L'adresse
    est donc toujours lisible et copiable, et le lien ne fait que rendre service
    quand il fonctionne.
    """
    return (
        '<div class=m-adresse>'
        f'<p class=m-adr-lab>Écrivez à</p>'
        f'<p class=m-adr id=adr-{intitule}>{CONTACT}</p>'
        '<div class=m-outils style="border:0;padding:0;margin:.7rem 0 0">'
        f'<button class="m-bouton m-plein" type=button '
        f'data-copier="{CONTACT}" data-cible="adr-{intitule}">'
        f'Copier l’adresse</button>'
        f'<a class=m-bouton href="{mailto}">Ouvrir mon logiciel de courrier</a>'
        '</div></div>')


def bloc_rgpd():
    return (
        '<div class=m-rgpd>'
        '<h3>Ce que nous recueillons, et ce que nous en faisons</h3>'
        '<p>Cette page n’enregistre rien : le site est un ensemble de pages '
        'statiques, sans base de données et sans formulaire. Votre message '
        'arrive dans la boîte du mouvement, et nulle part ailleurs.</p>'
        '<p><b>Données recueillies</b> : votre adresse électronique, et le nom '
        'et le prénom si vous les indiquez. Rien d’autre.</p>'
        '<p><b>Finalité</b> : vous envoyer le manifeste et les nouvelles du '
        'mouvement. Aucune cession, aucune vente, aucun transfert à un tiers.</p>'
        '<p><b>Durée</b> : jusqu’à votre demande de retrait.</p>'
        f'<p><b>Vos droits</b> : accès, rectification, effacement et '
        f'opposition, en écrivant à la même adresse. Un seul message suffit, '
        f'et il est traité sans condition.</p>'
        '</div>')


def bloc_partage():
    parts = ''.join(
        f'<a class=m-part href="#" data-partage="{base}">{e(nom)}</a>'
        for nom, base in RESEAUX)
    return (f'<div class=m-partage>{parts}</div>')


def page_adhesion(liens=None):
    """L'adhésion : l'adresse, le partage, et le détail à la fin."""
    liens = liens or LIENS_FICHIERS
    return (
        '<div class=m-page><div class=m-corps>'
        '<p class=m-titre>J’adhère au manifeste</p>'
        '<p class=m-chapeau>Le mouvement se compte. Envoyez votre adresse : '
        'vous recevrez le manifeste et les nouvelles du mouvement.</p>'
        '<p class=m-etape>Première étape — adhérer</p>'
        + bloc_adresse(MAILTO_ADHESION, 'adhesion')
        + f'<p class=m-note>Indiquez votre nom et votre prénom si vous le '
          f'souhaitez, et dites que vous acceptez de recevoir le manifeste à '
          f'cette adresse. '
          f'<a href="{liens["manifeste"]}">Lire le manifeste d’abord</a>.</p>'
        + '<p class=m-etape>Deuxième étape — faire connaître</p>'
        '<p class=m-chapeau>Le manifeste se diffuse mieux partagé que reçu.</p>'
        + bloc_partage()
        + bloc_rgpd()
        + '</div></div>')


def page_contact(liens=None):
    """« Je m'exprime » : l'adresse, et rien qui puisse ne pas marcher."""
    liens = liens or LIENS_FICHIERS
    return (
        '<div class=m-page><div class=m-corps>'
        '<p class=m-titre>Je m’exprime</p>'
        '<p class=m-chapeau>Une question, une objection, une correction, une '
        'proposition : écrivez, on répond.</p>'
        + bloc_adresse(MAILTO_EXPRESSION, 'contact')
        + '<p class=m-etape>Faire connaître</p>'
        + bloc_partage()
        + bloc_rgpd()
        + '</div></div>')


STYLE_SITE = """
/* --- couche du site -------------------------------------------------------
   Sélecteurs de classe uniquement : la feuille de la galerie garde la main sur
   les éléments nus, et les deux couches ne se disputent rien. */
.s-page{max-width:40rem;margin:0 auto}
.s-tete{background:var(--pap);padding:0 0 1.6rem;margin-bottom:1.4rem;
 box-shadow:0 2px 0 rgba(0,0,0,.35)}
.s-h1{font:700 2.4rem/1.06 var(--titre);margin:0;padding:0 1.8rem;
 color:var(--enc)}
.s-chapeau{margin:.8rem 0 0;padding:0 1.8rem;font-size:1rem;line-height:1.45;
 color:var(--gris)}

.s-groupe{background:var(--pap);margin-bottom:1.4rem;padding:0 0 .9rem;
 box-shadow:0 2px 0 rgba(0,0,0,.35)}
.s-gt{font:700 12px/1 var(--mono);letter-spacing:.22em;text-transform:uppercase;
 color:var(--ocre);margin:0;padding:1.2rem 1.8rem .5rem}
.s-gc{margin:0;padding:0 1.8rem .9rem;font-size:.9rem;color:var(--gris);
 border-bottom:1px solid var(--fil)}
.s-liste{list-style:none;margin:0;padding:0}
.s-liste li{border-bottom:1px solid var(--fil)}
.s-liste li:last-child{border-bottom:0}
.s-liste a{display:block;padding:.95rem 1.8rem;text-decoration:none;
 color:var(--enc)}
.s-liste a:hover{background:var(--sable)}
.s-liste a:focus-visible{outline:2px solid var(--gain);outline-offset:-2px}
.s-qui{display:block;font-weight:700;font-size:1.12rem;line-height:1.2}
.s-axe{display:block;margin-top:.2rem;font-size:.9rem;color:var(--gris);
 line-height:1.35}

.s-retour{max-width:40rem;margin:0 auto .5rem;display:flex;
 flex-wrap:wrap;gap:.5rem 1.2rem;justify-content:space-between;
 align-items:baseline}
.s-retour a{font:700 11px/1.4 var(--mono);letter-spacing:.16em;
 text-transform:uppercase;text-decoration:none;color:var(--sable);
 border-bottom:1px solid rgba(246,242,234,.32);padding-bottom:.15rem}
.s-retour a:hover{color:var(--pap);border-bottom-color:var(--pap)}
.s-retour a:focus-visible{outline:2px solid var(--sable);outline-offset:3px}
.s-retour .s-marque{letter-spacing:.32em;border-bottom-color:transparent}

.s-nav{max-width:40rem;margin:0 auto 1.4rem;background:var(--pap);
 box-shadow:0 2px 0 rgba(0,0,0,.35);display:flex;gap:1px;
 border-bottom:1px solid var(--fil)}
.s-nav a,.s-nav span{flex:1;padding:.8rem 1rem;font:700 11px/1.3 var(--mono);
 letter-spacing:.1em;text-transform:uppercase;text-decoration:none;
 color:var(--enc)}
.s-nav span{color:var(--fil)}
.s-nav a:hover{background:var(--sable)}
.s-nav .s-suiv{text-align:right}
.s-nav .s-idx{flex:0 0 auto;text-align:center;color:var(--ocre)}

.s-voisins{max-width:40rem;margin:0 auto;background:var(--pap);
 padding:0 0 .9rem;box-shadow:0 2px 0 rgba(0,0,0,.35)}
.s-pied{max-width:40rem;margin:1.4rem auto 0;padding:0 1.8rem;
 font:400 11px/1.5 var(--mono);letter-spacing:.08em;text-transform:uppercase;
 color:#8d8a83}
.s-pied a{color:#8d8a83}
"""


def enveloppe(titre, description, corps, prefixe=''):
    """Une page du site. Le titre et la description partent au partage."""
    return (
        '<!doctype html><html lang=fr><meta charset=utf-8>'
        '<meta name=viewport content="width=device-width,initial-scale=1">'
        f'<title>{e(titre)}</title>'
        f'<meta name=description content="{e(description)}">'
        f'<meta property="og:title" content="{e(titre)}">'
        f'<meta property="og:description" content="{e(description)}">'
        '<meta property="og:type" content="article">'
        f'<link rel=stylesheet href="{prefixe}fiche.css">'
        + corps + '</html>'
    )


def bandeau(prefixe=''):
    return ('<div class=marque>'
            f'<a class=nom href="{prefixe}index.html"'
            ' style="text-decoration:none;color:inherit">'
            f'{MARQUE}</a>'
            f'<span class=quoi>{SERVICE}</span></div>'
            '<div class=filet><i></i><i></i><i></i></div>')


def page_index(series, groupes):
    """L'entrée : la règle de lecture, puis les dix-huit axes par groupe."""
    par_groupe = {}
    for entree in series:
        par_groupe.setdefault(entree['groupe'], []).append(entree)

    blocs = []
    for g in groupes:
        entrees = par_groupe.get(g['titre'])
        if not entrees:
            continue
        items = ''.join(
            f'<li><a href="fiches/{x["slug"]}.html">'
            f'<span class=s-qui>{e(x["titre"])}</span>'
            f'<span class=s-axe>{e(x["axe"])}</span></a></li>'
            for x in entrees)
        blocs.append(f'<section class=s-groupe><h2 class=s-gt>{e(g["titre"])}'
                     f'</h2><p class=s-gc>{e(g["chapeau"])}</p>'
                     f'<ul class=s-liste>{items}</ul></section>')

    corps = (page_garde(LIENS_FICHIERS)
             + barre_retour(LIENS_FICHIERS, sommaire=True)
             + '<div class=s-page id=sommaire>'
             '<header class=s-tete>' + bandeau()
             + f'<h1 class=s-h1>{e(SERVICE)}</h1>'
             f'<p class=s-chapeau>{e(CHAPEAU)}</p></header>'
             + ''.join(blocs)
             + f'<p class=s-pied>{MARQUE}</p></div>')
    return enveloppe(f'{TITRE_UN} {TITRE_DEUX}', CHAPEAU, corps)


def barre_retour(liens, sommaire=False):
    """Où l'on va depuis une page intérieure : l'accueil, et le manifeste ou
    le sommaire. Aucune page du site n'est un cul-de-sac."""
    droite = (f'<a href="{liens["manifeste"]}">Le manifeste</a>' if sommaire
              else f'<a href="{liens["propositions"]}">Les dix-huit fiches</a>')
    return ('<div class=s-retour>'
            f'<a class=s-marque href="{liens["accueil"]}">← {MARQUE}</a>'
            + droite + '</div>')


def page_fiche(entree, precedent, suivant, voisins, liens=None):
    """Une fiche à son adresse : sa carte, et de quoi aller aux autres."""
    liens = liens or LIENS_FICHIERS
    nav = ['<nav class=s-nav>']
    nav.append(f'<a href="{precedent["slug"]}.html">‹ {e(precedent["titre"])}</a>'
               if precedent else '<span>‹</span>')
    nav.append(f'<a class=s-idx href="{liens["propositions"]}">Sommaire</a>')
    nav.append(f'<a class=s-suiv href="{suivant["slug"]}.html">'
               f'{e(suivant["titre"])} ›</a>'
               if suivant else '<span class=s-suiv>›</span>')
    nav.append('</nav>')

    bloc_voisins = ''
    if voisins:
        items = ''.join(
            f'<li><a href="{x["slug"]}.html">'
            f'<span class=s-qui>{e(x["titre"])}</span>'
            f'<span class=s-axe>{e(x["axe"])}</span></a></li>'
            for x in voisins)
        bloc_voisins = (
            f'<section class=s-voisins><h2 class=s-gt>{e(entree["groupe"])}'
            f'</h2><ul class=s-liste>{items}</ul></section>')

    corps = (barre_retour(liens) + ''.join(nav) + entree['carte']
             + bloc_voisins
             + f'<p class=s-pied><a href="{liens["accueil"]}">{MARQUE}</a>'
             f' · <a href="{liens["adherer"]}">J’adhère</a></p>')
    return enveloppe(f'{entree["titre"]} — {MARQUE}', entree['axe'], corps,
                     prefixe='../')


def page_404():
    corps = ('<div class=s-page><header class=s-tete>' + bandeau()
             + '<h1 class=s-h1>Cette page n’existe pas</h1>'
             '<p class=s-chapeau>Les dix-huit fiches sont listées à '
             'l’accueil.</p></header>'
             '<p class=s-pied><a href="index.html">'
             'Revenir à l’accueil</a></p></div>')
    return enveloppe(f'{MARQUE} — page introuvable',
                     'Les dix-huit fiches sont listées à l’accueil.', corps)


# Le réglage « Root Directory » de Vercel n'est modifiable qu'en choisissant un
# dossier qui existe déjà au dépôt : sur un dépôt neuf, le champ est verrouillé
# sur la racine. Ce fichier dit donc à Vercel où sont les pages, depuis le dépôt
# lui-même, et l'auteur n'a aucun champ à remplir. `framework: null` et
# `installCommand` vide interdisent toute détection de projet et toute
# construction : le dépôt est servi tel quel.
VERCEL_JSON = """{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "framework": null,
  "installCommand": "",
  "outputDirectory": "SOUS_DOSSIER",
  "cleanUrls": false,
  "trailingSlash": false
}
"""


# --- variante en un fichier ------------------------------------------------
#
# Le site en vingt-deux fichiers demande un hébergement. Quand il n'y en a pas,
# la même matière se rend en **une page** dont chaque fiche garde une adresse :
# un fragment, `…#retraite`. Ce n'est pas un mur — la page n'affiche qu'une vue
# à la fois —, et un lien vers une fiche reste un lien vers cette fiche.
#
# Sans JavaScript, tout s'affiche à la suite : la matière ne disparaît jamais.
#
# Ce fichier ne remplace pas `site/` : il le double, pour les cas où le
# déploiement n'est pas disponible. La même structure, le même rendu, une seule
# source.
ROUTAGE = """
/* --- routage par fragment -------------------------------------------------
   Sans script, chaque vue reste affichée : la page se lit à la suite. Le
   script ajoute `routed` et n'en montre plus qu'une. */
.routed .s-vue{display:none}
.routed .s-vue.on{display:block}
"""

SCRIPT = """
(function () {
  var body = document.body || document.getElementsByTagName('body')[0];
  body.className += ' routed';
  var vues = document.querySelectorAll('.s-vue');
  var connus = {};
  for (var i = 0; i < vues.length; i++) { connus[vues[i].id] = 1; }
  function montrer() {
    var cle = (location.hash || '').replace('#', '');
    if (!cle || !connus[cle]) { cle = 'accueil'; }
    for (var j = 0; j < vues.length; j++) {
      vues[j].className = (vues[j].id === cle) ? 's-vue on' : 's-vue';
    }
    window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', montrer);
  montrer();
})();
"""


def page_un_fichier(series, groupes, proto):
    """Tout le site en une page, une adresse par fiche via son fragment."""
    par_groupe = {}
    for entree in series:
        par_groupe.setdefault(entree['groupe'], []).append(entree)

    blocs = []
    for g in groupes:
        entrees = par_groupe.get(g['titre'])
        if not entrees:
            continue
        items = ''.join(
            f'<li><a href="#{x["slug"]}">'
            f'<span class=s-qui>{e(x["titre"])}</span>'
            f'<span class=s-axe>{e(x["axe"])}</span></a></li>'
            for x in entrees)
        blocs.append(f'<section class=s-groupe><h2 class=s-gt>{e(g["titre"])}'
                     f'</h2><p class=s-gc>{e(g["chapeau"])}</p>'
                     f'<ul class=s-liste>{items}</ul></section>')

    sommaire = ('<div class="s-vue" id=sommaire>'
                + barre_retour(LIENS_FRAGMENTS, sommaire=True)
                + '<div class=s-page>'
                '<header class=s-tete>'
                '<div class=marque><span class=nom>' + MARQUE + '</span>'
                f'<span class=quoi>{SERVICE}</span></div>'
                '<div class=filet><i></i><i></i><i></i></div>'
                f'<h1 class=s-h1>{e(SERVICE)}</h1>'
                f'<p class=s-chapeau>{e(CHAPEAU)}</p></header>'
                + ''.join(blocs)
                + f'<p class=s-pied>{MARQUE}</p></div></div>')

    accueil = ('<div class="s-vue" id=accueil>'
               + page_garde(LIENS_FRAGMENTS) + '</div>')
    manif = ('<div class="s-vue" id=manifeste>'
             + barre_retour(LIENS_FRAGMENTS)
             + page_manifeste(proto, LIENS_FRAGMENTS) + '</div>')
    adh = ('<div class="s-vue" id=adherer>'
           + barre_retour(LIENS_FRAGMENTS)
           + page_adhesion(LIENS_FRAGMENTS) + '</div>')
    cont = ('<div class="s-vue" id=contact>'
            + barre_retour(LIENS_FRAGMENTS)
            + page_contact(LIENS_FRAGMENTS) + '</div>')
    vues = [accueil, sommaire, manif, adh, cont]
    for i, entree in enumerate(series):
        precedent = series[i - 1] if i else None
        suivant = series[i + 1] if i + 1 < len(series) else None
        nav = ['<nav class=s-nav>']
        nav.append(f'<a href="#{precedent["slug"]}">‹ {e(precedent["titre"])}</a>'
                   if precedent else '<span>‹</span>')
        nav.append('<a class=s-idx href="#sommaire">Sommaire</a>')
        nav.append(f'<a class=s-suiv href="#{suivant["slug"]}">'
                   f'{e(suivant["titre"])} ›</a>'
                   if suivant else '<span class=s-suiv>›</span>')
        nav.append('</nav>')

        voisins = [x for x in series
                   if x['groupe'] == entree['groupe'] and x['id'] != entree['id']]
        bloc_voisins = ''
        if voisins:
            items = ''.join(
                f'<li><a href="#{x["slug"]}">'
                f'<span class=s-qui>{e(x["titre"])}</span>'
                f'<span class=s-axe>{e(x["axe"])}</span></a></li>'
                for x in voisins)
            bloc_voisins = (
                f'<section class=s-voisins><h2 class=s-gt>'
                f'{e(entree["groupe"])}</h2>'
                f'<ul class=s-liste>{items}</ul></section>')

        vues.append(f'<div class="s-vue" id={entree["slug"]}>'
                    + barre_retour(LIENS_FRAGMENTS) + ''.join(nav)
                    + entree['carte'] + bloc_voisins
                    + '<p class=s-pied><a href="#accueil">' + MARQUE
                    + '</a> · <a href="#adherer">J’adhère</a></p></div>')

    return (f'<title>{e(TITRE_UN)} {e(TITRE_DEUX)}</title>\n'
            f'<style>{STYLE}{STYLE_GARDE}{STYLE_SITE}{STYLE_PAGES}'
            f'{ROUTAGE}</style>\n'
            + '\n'.join(vues)
            + f'\n<script>{SCRIPT}{SCRIPT_PARTAGE}</script>\n')


def main(argv):
    if len(argv) < 5:
        print(__doc__)
        return 2
    positions = json.load(open(argv[1], encoding='utf-8'))
    ref = json.load(open(argv[2], encoding='utf-8'))
    racine = argv[3]
    proto = open(argv[4], encoding='utf-8').read()

    rang = {c: (i, j) for i, g in enumerate(positions['groupes'])
            for j, c in enumerate(g['categories'])}

    series = []
    for cid in sorted(FICHES, key=lambda c: rang.get(c, (99, 99))):
        ctx, gains, pertes = matiere(positions, ref, cid)
        series.append({
            'id': cid,
            'titre': ctx['titre'],
            'axe': ctx['axe'] or ctx['definition'],
            'groupe': ctx['groupe'],
            'slug': slug(ctx['titre']),
            'carte': fiche(ctx, gains, pertes, cid),
        })

    doublons = [s for s in {x['slug'] for x in series}
                if sum(1 for x in series if x['slug'] == s) > 1]
    if doublons:
        print('ÉCHEC — deux fiches partagent une adresse : '
              + ', '.join(sorted(doublons)))
        return 1

    dossier_fiches = os.path.join(racine, 'fiches')
    os.makedirs(dossier_fiches, exist_ok=True)

    ecrits = []

    def ecrire(chemin, contenu):
        with open(chemin, 'w', encoding='utf-8') as f:
            f.write(contenu)
        ecrits.append((chemin, os.path.getsize(chemin)))

    ecrire(os.path.join(racine, 'fiche.css'),
           STYLE + STYLE_GARDE + STYLE_SITE + STYLE_PAGES)
    ecrire(os.path.join(racine, 'index.html'),
           page_index(series, positions['groupes']))
    ecrire(os.path.join(racine, '404.html'), page_404())

    ecrire(os.path.join(racine, 'manifeste.html'),
           enveloppe(f'Manifeste — {MANIF.TITRE}',
                     'Le manifeste Résolution, en une page.',
                     barre_retour(LIENS_FICHIERS)
                     + page_manifeste(proto, LIENS_FICHIERS,
                                      fichier='manifeste.html')
                     + f'<script>{SCRIPT_PARTAGE}</script>'))

    ecrire(os.path.join(racine, 'adherer.html'),
           enveloppe(f'J’adhère au manifeste — {MARQUE}',
                     'Envoyez votre adresse : vous recevrez le manifeste et '
                     'les nouvelles du mouvement.',
                     barre_retour(LIENS_FICHIERS)
                     + page_adhesion(LIENS_FICHIERS)
                     + f'<script>{SCRIPT_PARTAGE}</script>'))

    ecrire(os.path.join(racine, 'contact.html'),
           enveloppe(f'Je m’exprime — {MARQUE}',
                     f'Écrivez au mouvement : {CONTACT}.',
                     barre_retour(LIENS_FICHIERS)
                     + page_contact(LIENS_FICHIERS)
                     + f'<script>{SCRIPT_PARTAGE}</script>'))

    for i, entree in enumerate(series):
        voisins = [x for x in series
                   if x['groupe'] == entree['groupe'] and x['id'] != entree['id']]
        ecrire(os.path.join(dossier_fiches, entree['slug'] + '.html'),
               page_fiche(entree,
                          series[i - 1] if i else None,
                          series[i + 1] if i + 1 < len(series) else None,
                          voisins, LIENS_FICHIERS))

    # Le fichier de configuration ne va pas dans `site/` : il vit à la racine du
    # dépôt de publication, à côté du dossier qu'il désigne. `make publier` le
    # pose. On l'écrit ici pour qu'il n'existe qu'une source.
    ecrire(os.path.join(racine, 'resolution_une_page.html'),
           page_un_fichier(series, positions['groupes'], proto))

    ecrire(os.path.join(racine, 'vercel.json.modele'),
           VERCEL_JSON.replace('SOUS_DOSSIER',
                               os.path.basename(racine.rstrip('/')) or 'site'))

    total = sum(o for _, o in ecrits)
    print(f'{racine}/ — {len(ecrits)} fichier(s), {total} o · '
          f'{len(series)} fiche(s) à leur adresse')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
