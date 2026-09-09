# -*- coding: utf-8 -*-
"""Les leviers d'État sur la dépense des collocs, et leur véhicule.

`ventilation_vehicule.py` rangeait les 39,5 Md€ du périmètre local en « hors
véhicule financier de l'État » et s'arrêtait là. **C'était juste sur la dépense
et faux sur le levier.** Une dépense communale ne se vote pas en loi de
finances ; mais la ressource qui la finance, le cofinancement qui l'appelle et
la norme qui la prescrit y sont, pour une large part.

Ce module relève ces leviers, chacun avec **son montant pris au socle**, son
véhicule et la porte du domaine par laquelle il entre.

## Ce qui commande la lecture

**On n'atteint pas la dépense, on atteint ce qui la rend possible.** Quatre
prises, et elles ne se confondent pas.

    la ressource      la fiscalité locale, les prélèvements sur recettes, les
                      dégrèvements et les compensations d'exonérations. Réduire
                      la ressource ne commande pas l'emploi : la collectivité
                      arbitre. C'est un levier fort et indirect.
    le cofinancement  les crédits d'État qui appellent une dépense locale —
                      concours, dotations d'investissement, contrats. Ce sont
                      des crédits d'État : un amendement de crédits les touche
                      directement. Levier faible en montant, direct en effet.
    la norme          la compétence, le statut, les normes techniques. Hors
                      loi de finances. C'est là que se prend la dépense
                      elle-même, et c'est un autre texte.
    le cadrage        la trajectoire de dépense locale et sa contractualisation.
                      Son siège était la loi de programmation ; la réforme
                      l'abroge. **Sa porte est à instruire.**

## Ce que le module ne fait pas

**Il n'additionne rien.** Les montants de ressource et les montants d'économie
sont deux objets : 58 Md€ de taxes affectées aux collocs et 39,5 Md€
d'économies locales ne se somment pas, et le module refuse de les mettre dans
un même total.

**Il n'arbitre aucun levier.** Ce qui est établi porte son montant et sa porte ;
ce qui est plausible mais non établi va au bloc des tangents, signalé à part.

Usage : python3 leviers_collocs.py ../referentiels/socle_budgetaire.json \\
            ../referentiels/economies.json ../livrables/leviers_collocs.md
"""
import collections
import json
import os
import re
import sys

# --------------------------------------------------------------- les leviers
# Écrits à la main. `mesure` nomme la fonction qui va chercher le montant au
# socle — jamais un chiffre en dur. Une mesure qui ne trouve rien sort « non au
# socle », et cela se lit.
LEVIERS = [
    dict(id='L1', nature='ressource', vehicule='PLF', portes=['P-03', 'P-06'],
         partie='première',
         intitule='La fiscalité affectée aux collocs',
         mesure='taxes_collocs',
         quoi="Les impositions dont le produit est affecté à une collectivité, "
              "à un de ses établissements ou à un organisme local. **L'auteur "
              "les a déjà classées lui-même** : le classeur porte un régime "
              "`Collocs` sur chacune.",
         porte_dit="Le 3° bis du I vise « les impositions de toutes natures "
                   "affectées à une personne morale autre que l'État » — les "
                   "collectivités en sont. La loi de finances peut donc en "
                   "modifier **l'assiette, le taux, l'affectation et les "
                   "modalités de recouvrement**, en première partie. C'est la "
                   "porte la plus large du lot, et elle est facultative donc "
                   "ouverte.",
         garde="Le 5° bis exclut nommément les collectivités de la **reprise du "
               "produit par l'État**. On peut donc supprimer ou réduire une "
               "taxe locale ; on ne peut pas s'en attribuer le produit par "
               "cette porte-là.",
         doctrine='D5-3-1 — taxe foncière intégralement communale'),

    dict(id='L2', nature='ressource', vehicule='PLF', portes=['P-04', 'P-06'],
         partie='première',
         intitule='Les niches sur impôts locaux',
         mesure='niches_locales',
         quoi="Les dépenses fiscales de catégorie « Impôts locaux » — "
              "exonérations et abattements de taxe foncière, de cotisation "
              "foncière des entreprises, de cotisation sur la valeur ajoutée. "
              "**Une part est compensée par l'État**, et la compensation est "
              "alors une dépense budgétaire.",
         porte_dit="Ce sont des dispositions relatives à des impositions ; "
                   "leur article de code est nommé à l'annexe.",
         garde="**Le vecteur est connu à 100 %** : l'annexe des dépenses "
               "fiscales porte l'article du code général des impôts pour "
               "chacune. C'est le seul lot du chantier où le vecteur ne se "
               "cherche pas.",
         doctrine='D2-5 — abolition des niches fiscales et sociales'),

    dict(id='L3', nature='ressource', vehicule='PLF', portes=['P-12'],
         partie='seconde',
         intitule="Les dégrèvements d'impôts locaux",
         mesure='degrevements_locaux',
         quoi="Le programme 201 : l'État prend à sa charge l'impôt local que "
              "le contribuable ne paie pas. **C'est une dépense d'État en "
              "totalité**, et elle est évaluative.",
         porte_dit="Crédits du budget général, seconde partie.",
         garde="Crédits évaluatifs : ils s'imputent au-delà des crédits "
               "ouverts. Les réduire par amendement de crédits ne réduit pas "
               "la charge — il faut toucher au dégrèvement lui-même, donc au "
               "code, donc à L2.",
         doctrine=None),

    dict(id='L4', nature='cofinancement', vehicule='PLF', portes=['P-12'],
         partie='seconde',
         intitule='Les concours budgétaires aux collocs',
         mesure='concours_credits',
         quoi="Les crédits d'État qui financent ou cofinancent une dépense "
              "locale — mission « Relations avec les collectivités "
              "territoriales », équipement des collectivités, interventions "
              "territoriales, politique de la ville, urbanisme et habitat.",
         porte_dit="Crédits par mission, seconde partie. **Un amendement de "
                   "crédits sur l'état B suffit : ni vecteur de code, ni "
                   "disposition modificative.**",
         garde="C'est le levier le plus direct et le plus faible en montant. "
               "Il ne demande aucune légistique — tout son coût est en "
               "recevabilité et en exposé sommaire.",
         doctrine=None),

    dict(id='L5', nature='cofinancement', vehicule='PLF', portes=['P-12'],
         partie='seconde',
         intitule='Les transferts aux collectivités au budget général',
         mesure='transferts_bg',
         quoi="La ligne « transferts aux collectivités territoriales » de la "
              "nomenclature par nature, tous programmes confondus. Elle "
              "recoupe L4 sans s'y réduire : le transfert est une catégorie de "
              "dépense, le concours une mission.",
         porte_dit="Crédits du budget général, seconde partie.",
         garde="**Recoupement avec L4 : ne pas additionner.** L4 compte des "
               "missions, L5 une nature de dépense ; les mêmes euros y "
               "figurent en partie deux fois.",
         doctrine=None),

    dict(id='L6', nature='ressource', vehicule='PLF', portes=['P-07'],
         partie='première',
         intitule='Les prélèvements sur recettes',
         mesure='psr',
         quoi="La dotation globale de fonctionnement, le fonds de "
              "compensation de la TVA, les compensations d'exonérations. "
              "**C'est le premier levier en montant, et de loin.**",
         porte_dit="Le 4° du I : la loi de finances « institue et évalue » "
                   "chacun des prélèvements. L'article 6 ajoute qu'ils sont "
                   "« évalués de façon précise et distincte » et qu'ils sont "
                   "institués par une loi de finances, **qui précise l'objet "
                   "du prélèvement et les catégories de collectivités "
                   "bénéficiaires**. Le régime, pas seulement le montant.",
         garde="**Le montant n'est pas au socle** : l'annexe des prélèvements "
               "sur recettes n'est pas au corpus. Il se relèvera sur pièce. "
               "Ce qui est établi ici est la porte, pas la grandeur.",
         doctrine='D5-3 — financement de l’échelon communal'),

    dict(id='L7', nature='cadrage', vehicule='à trancher', portes=[],
         partie='—',
         intitule='Le cadrage de la dépense locale',
         mesure=None,
         quoi="La trajectoire de dépense des collectivités et sa "
              "contractualisation.",
         porte_dit="**Sa porte est à instruire.** Son siège était la loi de "
                   "programmation des finances publiques, que la réforme "
                   "abroge (M4.8 du récapitulatif de transposabilité, "
                   "incompatible à Constitution inchangée, repli R5). Reporté "
                   "sur l'article liminaire, il change de nature : "
                   "l'article liminaire constate, il ne prescrit pas aux "
                   "collectivités.",
         garde="Un levier dont la porte n'est pas établie ne se plaide pas. "
               "Il s'inscrit.",
         doctrine='D11-4 — séquencement et transitions'),

    dict(id='L8', nature='norme', vehicule='hors loi de finances', portes=[],
         partie='—',
         intitule='La compétence, le statut, la norme',
         mesure=None,
         quoi="Ce qui décide de la dépense elle-même : la répartition des "
              "compétences au code général des collectivités territoriales, "
              "le statut de la fonction publique territoriale, les normes "
              "techniques prescrites.",
         porte_dit="Aucune. Loi ordinaire, et pour partie règlement.",
         garde="**C'est là que se prend la dépense, et c'est hors du "
               "contre-PLF.** Une mesure de compétence déposée en loi de "
               "finances tombe sur le domaine, quel que soit son effet "
               "budgétaire.",
         doctrine='D5-2-1 — la commune, échelon local unique'),
]

# ------------------------------------------------------------- les tangents
# Ce dont l'intersection avec le budgétaire ou le fiscal d'État est plausible
# et non établie. Signalé à part, à reprendre dans un second temps.
TANGENTS = [
    ('T1', "Le financement de la fonction publique territoriale",
     "Le Centre national de la fonction publique territoriale et les centres "
     "de gestion figurent parmi les bénéficiaires de taxes affectées relevées "
     "au socle. Leur ressource est assise sur la masse salariale locale. "
     "**Cotisation ou imposition de toute nature ?** Le véhicule en dépend : "
     "une imposition entre par le 3° bis, une cotisation n'y entre pas."),
    ('T2', "Les retraites des agents territoriaux",
     "La Caisse nationale de retraites des agents des collectivités locales "
     "relève de la sphère sociale. **Véhicule PLFSS, pas PLF** — et c'est de "
     "la matière que le chantier PLFSS aura à porter, pas le contre-PLF."),
    ('T3', "Les cofinancements pluriannuels",
     "Contrats de plan État-région, volet territorialisé de France 2030. "
     "L'autorisation d'engagement est en loi de finances ; la convention qui "
     "l'engage ne l'est pas. **Réduire l'autorisation ne défait pas "
     "l'engagement pris**, et l'écart entre les deux est exactement ce que le "
     "régime des autorisations d'engagement doit traiter."),
    ('T4', "La TVA affectée en remplacement de la taxe d'habitation et de la CVAE",
     "C'est une fraction d'une ressource d'État partagée, non une imposition "
     "locale propre. **La porte est le 2° du I — dispositions relatives aux "
     "ressources de l'État — plutôt que le 3° bis.** Le montant n'est pas au "
     "socle sous cette forme."),
    ('T5', "Les exonérations compensées par l'État",
     "Le socle en porte plusieurs sous « Exonérations compensées par l'État ». "
     "**Supprimer la niche sans supprimer la compensation ne rend rien à "
     "l'État ; supprimer la compensation sans la niche transfère la charge à "
     "la commune.** Les deux se tiennent, et le chiffrage doit dire lequel des "
     "deux il compte — faute de quoi l'économie est comptée deux fois ou pas "
     "du tout."),
    ('T6', "Les dépenses locales prescrites par une norme d'État",
     "Normes techniques, revalorisations imposées, obligations de service. "
     "L'économie serait réelle et le vecteur est réglementaire ou législatif "
     "ordinaire. **Aucun montant au corpus.**"),
    ('T7', "Les dépenses sociales départementales",
     "`D5-3-4` — reprise par l'État des solidarités départementales — est la "
     "seule proposition du corpus qui **déplace** une dépense locale vers "
     "l'État au lieu de la supprimer. Elle est déclarée *esquissée* et ne "
     "porte aucun effet. Son véhicule dépend de ce qu'elle deviendra."),
]

# Les quatre lignes du périmètre local, et les leviers qui pourraient les
# produire. Écrit à la main, ligne par ligne (A-35).
RATTACHEMENT_LIGNES = {
    'ECO-40': dict(leviers=['L8', 'L6', 'L1'], tangents=['T6'],
                   motif="La dépense culturelle locale est une compétence "
                         "facultative : elle se ferme par la compétence (L8), "
                         "ou se contraint par la ressource (L6, L1). "
                         "*Attention au double compte : les subventions "
                         "culturelles d'État sont déjà comptées à `ECO-34`, "
                         "périmètre État.*"),
    'ECO-41': dict(leviers=['L8', 'L2', 'L4'], tangents=['T3', 'T5'],
                   motif="Les aides locales aux entreprises relèvent de la "
                         "compétence régionale (L8), mais leur volet fiscal — "
                         "exonérations facultatives de cotisation foncière et "
                         "de cotisation sur la valeur ajoutée — a son régime "
                         "au code général des impôts, donc en loi de finances "
                         "(L2). Le volet cofinancé passe par les crédits (L4)."),
    'ECO-42': dict(leviers=['L6', 'L1', 'L8'], tangents=['T6'],
                   motif="Les charges courantes se financent sur ressources "
                         "générales : le levier est la ressource (L6, L1), et "
                         "il ne commande pas l'emploi. La norme (L8) est le "
                         "seul levier qui atteigne la dépense."),
    'ECO-43': dict(leviers=['L8', 'L6'], tangents=['T1', 'T2'],
                   motif="Le statut de la fonction publique territoriale est "
                         "hors loi de finances (L8). La ressource contraint "
                         "l'effectif sans le décider (L6). Le financement des "
                         "organismes de la filière — formation, gestion, "
                         "retraites — est tangent et se qualifie avant de se "
                         "chiffrer."),
}


# ----------------------------------------------------------- les mesures
def taxes_collocs(socle):
    lot = [x for x in socle['taxes_affectees']
           if (x['interpretation'].get('regime') or '') == 'Collocs']
    v = sum(x['socle'].get('affectation_nette_eur') or 0 for x in lot)
    return (f"{len(lot)} taxe(s) affectée(s) de régime « Collocs »",
            v, 'annexe 2 du tome I des Voies et moyens, régime déclaré par '
               "l'auteur à l'onglet des chiffrages")


def niches_locales(socle):
    lot = [x for x in socle['depenses_fiscales']
           if (x['socle'].get('categorie') or '') == 'Impôts locaux']
    sup = [x for x in lot
           if (x['interpretation'].get('regime') or '') not in ('', '—')]
    art = sum(1 for x in lot if (x['socle'].get('article') or '').strip())
    v = sum((x['socle'].get('realisation_2024_m_eur') or 0) for x in lot) * 1e6
    return (f"{len(lot)} dépense(s) fiscale(s) sur impôts locaux, dont "
            f"{len(sup)} portent un régime de suppression — "
            f"**article de code renseigné pour {art} sur {len(lot)}**",
            v, 'annexe 3 du tome II des Voies et moyens, réalisation 2024')


def degrevements_locaux(socle):
    v = sum(p['socle'].get('cp_plf') or 0 for p in socle['pap']
            if str(p['socle'].get('programme')) == '201')
    return ('programme 201 — remboursements et dégrèvements d\'impôts locaux, '
            'crédits évaluatifs', v, 'projet annuel de performance, crédits de '
                                     'paiement du PLF 2026')


def concours_credits(socle):
    cibles = {'119', '122', '754', '162', '112', '147'}
    v = sum(p['socle'].get('cp_plf') or 0 for p in socle['pap']
            if str(p['socle'].get('programme')) in cibles)
    return (f'{len(cibles)} programme(s) — concours financiers, concours '
            'spécifiques, équipement des collectivités, interventions '
            'territoriales, aménagement du territoire, politique de la ville',
            v, 'projet annuel de performance, crédits de paiement du PLF 2026')


def transferts_bg(socle):
    v = (socle.get('bg_synthese', {}).get('transferts_collectivites_m_eur') or 0)
    return ('nomenclature par nature, ligne des transferts aux collectivités '
            'territoriales', v * 1e6,
            'onglet de synthèse du classeur des dépenses du budget général')


def psr(socle):
    return ("dotation globale de fonctionnement, fonds de compensation de la "
            "TVA, compensations d'exonérations", None,
            "**annexe des prélèvements sur recettes — pièce absente du "
            "corpus**")


MESURES = {'taxes_collocs': taxes_collocs, 'niches_locales': niches_locales,
           'degrevements_locaux': degrevements_locaux,
           'concours_credits': concours_credits, 'transferts_bg': transferts_bg,
           'psr': psr}

NATURES = {'ressource': 'La ressource', 'cofinancement': 'Le cofinancement',
           'cadrage': 'Le cadrage', 'norme': 'La norme'}


def _md(v):
    if v is None:
        return 'non au socle'
    return f'{v / 1e9:,.2f}'.replace(',', ' ').replace('.', ',') + ' Md€'


def rendre(socle, eco):
    lignes = {l['id']: l for l in eco['lignes']}
    L = []
    a = L.append
    a('# Les leviers d\'État sur la dépense des collocs')
    a('')
    a('*Produit par `appareil/leviers_collocs.py`. Chaque montant est pris au '
      'socle budgétaire et porte sa pièce ; un levier dont le montant n\'y est '
      'pas le déclare. Le rattachement des lignes d\'économie aux leviers est '
      'écrit à la main, ligne par ligne (A-35).*')
    a('')
    a('**Ce document corrige `A-237`.** La ventilation par véhicule rangeait '
      'les 39,5 Md€ du périmètre local en « hors véhicule financier de '
      'l\'État ». C\'était juste sur la dépense et faux sur le levier : la '
      'ressource qui la finance et le cofinancement qui l\'appelle sont en '
      'loi de finances ; seules la norme qui la prescrit et le cadrage qui la '
      'contraint n\'y sont pas. **Six leviers sur huit ont une porte au '
      'domaine.**')
    a('')
    a('---')
    a('')
    a('## Ce qui commande la lecture')
    a('')
    a('**On n\'atteint pas la dépense locale, on atteint ce qui la rend '
      'possible.** Quatre prises, et elles n\'ont ni le même véhicule, ni la '
      'même force, ni le même coût de rédaction.')
    a('')
    a('| prise | ce qu\'elle fait | véhicule | force |')
    a('|---|---|---|---|')
    a('| **la ressource** | réduit ce qui finance, laisse l\'arbitrage local | '
      'loi de finances | forte en montant, indirecte en effet |')
    a('| **le cofinancement** | supprime le crédit d\'État qui appelle la '
      'dépense | loi de finances | faible en montant, directe en effet |')
    a('| **la norme** | supprime la compétence ou l\'obligation | loi '
      'ordinaire | c\'est là que la dépense se prend, et c\'est hors du '
      'contre-PLF |')
    a('| **le cadrage** | contraint la trajectoire | à trancher | porte non '
      'établie depuis l\'abrogation de la loi de programmation |')
    a('')
    a('**Deux montants ne se somment jamais** : ce qu\'un levier de ressource '
      'pèse, et ce qu\'une ligne d\'économie vaut. Le premier est une recette '
      'locale, le second une dépense locale. Les additionner doublerait tout.')
    a('')
    a('---')
    a('')

    # ------------------------------------------------------------- le compte
    a('## Le compte des leviers')
    a('')
    a('| levier | nature | véhicule | partie | montant | portes |')
    a('|---|---|---|---|---|---|')
    mesures = {}
    for lv in LEVIERS:
        if lv['mesure']:
            mesures[lv['id']] = MESURES[lv['mesure']](socle)
            montant = _md(mesures[lv['id']][1])
        else:
            montant = '—'
        portes = ', '.join(f'`{p}`' for p in lv['portes']) or '—'
        a(f'| **{lv["id"]}** {lv["intitule"]} | {NATURES[lv["nature"]]} | '
          f'{lv["vehicule"]} | {lv["partie"]} | {montant} | {portes} |')
    a('')
    en_lf = [lv for lv in LEVIERS if lv['vehicule'] == 'PLF']
    a(f'**{len(en_lf)} leviers sur {len(LEVIERS)} sont en loi de finances.** '
      'Deux ne le sont pas : la norme, qui est le seul levier atteignant la '
      'dépense elle-même, et le cadrage, dont la porte n\'est plus établie.')
    a('')
    a('---')
    a('')

    # ------------------------------------------------------------ le détail
    for nature in ('ressource', 'cofinancement', 'cadrage', 'norme'):
        lot = [lv for lv in LEVIERS if lv['nature'] == nature]
        if not lot:
            continue
        a(f'## {NATURES[nature]}')
        a('')
        for lv in lot:
            a(f'### {lv["id"]} — {lv["intitule"]}')
            a('')
            if lv['mesure']:
                quoi, val, source = mesures[lv['id']]
                a(f'**{_md(val)}** — {quoi}.')
                a('')
                a(f'*Source : {source}.*')
                a('')
            a(lv['quoi'])
            a('')
            a(f'**La porte.** {lv["porte_dit"]}')
            a('')
            a(f'**La garde.** {lv["garde"]}')
            a('')
            if lv['doctrine']:
                a(f'*Ancrage doctrinal : {lv["doctrine"]}.*')
                a('')
        a('---')
        a('')

    # --------------------------------------------- reprise des quatre lignes
    a('## Les quatre lignes du périmètre local, reprises')
    a('')
    a('Les montants sont ceux du chiffrage : ce sont des **dépenses locales**, '
      'et le levier qui les produit n\'a pas le même montant qu\'elles.')
    a('')
    a('| ligne | intitulé | Md€ | leviers | tangents |')
    a('|---|---|---|---|---|')
    for i, r in RATTACHEMENT_LIGNES.items():
        l = lignes.get(i)
        if not l:
            continue
        a(f'| `{i}` | {l["intitule"]} | '
          f'{_md((l["total_supprime_md_eur"] or 0) * 1e9).replace(" Md€","")} | '
          + ', '.join(f'`{x}`' for x in r['leviers']) + ' | '
          + (', '.join(f'`{x}`' for x in r['tangents']) or '—') + ' |')
    a('')
    for i, r in RATTACHEMENT_LIGNES.items():
        if i not in lignes:
            continue
        a(f'**`{i}` — {lignes[i]["intitule"]}.** {r["motif"]}')
        a('')
    a('---')
    a('')

    # ---------------------------------------------------------- les tangents
    a('## Ce qui est tangent — signalé, non instruit')
    a('')
    a('*Sept points où l\'intersection avec le budgétaire ou le fiscal d\'État '
      'est plausible et non établie. Le fil les signale et s\'arrête ; ils se '
      'reprennent dans un second temps.*')
    a('')
    for code, titre, texte in TANGENTS:
        a(f'**{code} — {titre}.** {texte}')
        a('')
    a('---')
    a('')

    # ------------------------------------------------------------- le verdict
    a('## Ce que la reprise change, et ce qu\'elle ne change pas')
    a('')
    tc = mesures['L1'][1] or 0
    nl = mesures['L2'][1] or 0
    dg = mesures['L3'][1] or 0
    cc = mesures['L4'][1] or 0
    a(f'**Ce qu\'elle change.** Le contre-PLF a prise sur les collocs, et la '
      f'prise est large : {_md(tc)} de fiscalité affectée dont la loi de '
      f'finances peut modifier l\'assiette, le taux et l\'affectation ; '
      f'{_md(nl)} de niches sur impôts locaux **dont l\'article de code est '
      f'connu à 100 %** ; {_md(dg)} de dégrèvements qui sont une dépense '
      f'd\'État en totalité ; {_md(cc)} de concours budgétaires qu\'un simple '
      'amendement de crédits atteint. Et par-dessus, les prélèvements sur '
      'recettes, premier levier en montant, dont la porte est établie et dont '
      'le montant reste à relever.')
    a('')
    a('**Ce qu\'elle ne change pas.** La dépense locale elle-même ne se vote '
      'pas en loi de finances. Réduire la ressource ne commande pas l\'emploi : '
      'la collectivité arbitre, et elle peut arbitrer contre nous — augmenter '
      'un taux, emprunter, ou couper ailleurs que là où nous voulions. '
      '**C\'est la limite du levier de ressource, et elle se dit dans '
      'l\'exposé sommaire plutôt que de se découvrir en séance.**')
    a('')
    a('**Et le décompte des véhicules ne bouge pas.** Les 39,5 Md€ restent des '
      'dépenses que la loi de finances ne vote pas. Ce qui change est qu\'ils '
      'cessent d\'être hors de portée : ils deviennent une dépense qu\'on '
      'atteint par sa ressource, avec ce que cela coûte en effet indirect.')
    a('')
    a('## Ce que le fil inscrit et ne tranche pas')
    a('')
    a('1. **Le montant des prélèvements sur recettes.** L\'annexe n\'est pas au '
      'corpus. C\'est le premier levier en montant et le seul dont la grandeur '
      'manque — il entre par pièce jointe (A-234).')
    a('2. **Le choix entre couper la ressource et couper la compétence.** Les '
      'deux atteignent la même dépense, par deux véhicules différents, avec '
      'deux effets différents. Ce n\'est pas une question de technique, c\'est '
      'une question de doctrine, et `D5-2-1` la tranche pour l\'échelon mais '
      'pas pour la dépense.')
    a('3. **Le sort des exonérations compensées** (`T5`), qui décide si une '
      'économie est comptée une fois, deux fois ou pas du tout.')
    a('4. **La porte du cadrage** (`L7`), perdue avec l\'abrogation de la loi '
      'de programmation et non retrouvée.')
    a('')
    return '\n'.join(L) + '\n'


def main(src_socle, src_eco, dst):
    socle = json.load(open(src_socle, encoding='utf-8'))
    eco = json.load(open(src_eco, encoding='utf-8'))
    manquants = [i for i in RATTACHEMENT_LIGNES
                 if i not in {l['id'] for l in eco['lignes']}]
    if manquants:
        print('ARRÊT — rattachement portant sur des lignes absentes : '
              + ', '.join(manquants))
        return 1
    texte = rendre(socle, eco)
    os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
    open(dst, 'w', encoding='utf-8').write(texte)
    print(f'{dst} — {len(LEVIERS)} levier(s), {len(TANGENTS)} tangent(s), '
          f'{len(RATTACHEMENT_LIGNES)} ligne(s) reprise(s), '
          f'{os.path.getsize(dst)} octets')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
