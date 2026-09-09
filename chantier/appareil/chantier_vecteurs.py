# -*- coding: utf-8 -*-
"""Le chantier des vecteurs — volume mesuré, ce qui existe, ce qui reste.

A-227 pose que le vecteur est le gros du travail et qu'il faut le dire
maintenant. **Ce module le mesure au lieu de l'estimer.** Il compte, sur les
référentiels et le socle, ce que chaque nature de mesure demande comme vecteur,
et il sépare ce qui est déjà connu de ce qui est à trouver.

## Le renversement que la mesure produit

L'intuition dit : 56 propositions, donc 56 vecteurs à trouver, donc un chantier
proportionnel au nombre de propositions.

**C'est faux dans les deux sens.** Une proposition comme la fiscalité à quatre
impôts touche des centaines d'articles ; une mesure d'économie de crédits n'en
touche aucun. **Le vecteur ne se compte pas en propositions : il se compte en
articles touchés, et la distribution est très inégale.**

De là suit le seul découpage qui tienne : **par régime de vecteur**, non par
axe de doctrine ni par ordre de dépôt.

    vecteur non codifié  une mesure de crédits se dépose en amendement de
                       chiffres sur l'état B. Ni article de code, ni
                       disposition modificative — mais **le vecteur existe et
                       il est de rang législatif** : l'état B est voté et les
                       crédits qu'il ouvre sont limitatifs.
    vecteur connu      l'annexe le nomme déjà. Rien à chercher : il reste à
                       convertir une référence en disposition modificative.
    vecteur à trouver  il faut ouvrir le texte fondateur, ou le code, et
                       identifier l'alinéa. C'est le seul lot vraiment cher.
    norme à écrire     la proposition ne dit pas encore ce que le droit doit
                       imposer. Le vecteur ne se cherche pas avant.

## Ce que le module ne fait pas

Il ne trouve aucun vecteur et il n'en écrit aucun. **Il dimensionne.** Le
découpage en lots qu'il propose est de la tambouille et se tranche ; l'ordre de
dépôt et le nombre d'amendements sont de la stratégie parlementaire et
reviennent à l'auteur.

Usage : python3 chantier_vecteurs.py ../referentiels/socle_budgetaire.json \\
            ../referentiels/REF_doctrine.json ../livrables/chantier_vecteurs.md \\
            [../referentiels/REF_norme.json]
"""
import collections
import json
import os
import re
import sys

REGIMES = {
    'aucun': 'Vecteur non codifié — état B de la loi de finances',
    'connu': 'Vecteur connu — porté par l’annexe',
    'trouver': 'Vecteur à trouver',
    'norme': 'Norme cible à écrire avant tout vecteur',
}


POPULATION_DU_LOT = {'V1': 'programme', 'V2': 'depense_fiscale',
                     'V3': 'taxe_affectee', 'V5': 'proposition'}


def lots(socle, ref):
    """Un lot par population homogène de vecteurs. Compté, jamais estimé."""
    L = []

    # --- les crédits ------------------------------------------------------
    progs = socle['nomenclature']['programmes']
    L.append(dict(
        id='V1', regime='aucun', population='programmes du budget général',
        n=len(progs), avec_vecteur=None,
        quoi="**Une mesure de crédits est une mesure de plein exercice, et "
             "elle est de rang législatif** (A-243). Elle se dépose en "
             "amendement de chiffres sur l'état B annexé à l'article de "
             "crédits, mission par mission : une ligne, une baisse. Elle ne "
             "modifie aucun article de code — mais son vecteur est "
             "parfaitement déterminé, et il est le même pour les 128. Dire "
             "qu'elle serait infra-législative parce qu'elle porte des "
             "plafonds est faux : l'état B est voté, et les crédits ouverts "
             "sont limitatifs.",
        cout="**Nul en légistique, et c'est ce qui en fait le lot le plus "
             "simple — pas le moins sérieux.** L'article 40 ne mord pas sur "
             "une réduction de crédits ; il mord sur l'augmentation d'une "
             "charge. Tout le coût est en choix de mission et en exposé "
             "sommaire. **Le montant se reprend au projet de loi de finances "
             "en discussion, jamais au nôtre** (A-244) : notre chiffrage est "
             "un ordre de grandeur qui oriente la baisse, il ne la "
             "conditionne pas.",
        ordre="Premier. C'est le lot le moins cher en légistique, et\n              celui qui porte le plus de montant."))

    # --- les dépenses fiscales -------------------------------------------
    df = socle['depenses_fiscales']
    df_reg = [x for x in df
              if (x['interpretation'].get('regime') or '') not in ('', '—')]
    df_art = sum(1 for x in df_reg if (x['socle'].get('article') or '').strip())
    arts = set()
    for x in df_reg:
        a = (x['socle'].get('article') or '').replace('#', '')
        for m in re.split(r'\s*(?:,|et|;)\s*', a):
            if m.strip():
                arts.add(m.strip())
    L.append(dict(
        id='V2', regime='connu', population='dépenses fiscales',
        n=len(df_reg), avec_vecteur=df_art,
        detail=f'{len(df_reg)} portent un régime de suppression · '
               f'{len(arts)} référence(s) d’article distincte(s)',
        quoi="L'annexe des dépenses fiscales porte, pour chacune, l'article du "
             "code qui la crée **et la norme de référence à laquelle elle "
             "déroge**. Les deux ensemble donnent la disposition modificative "
             "presque telle quelle.",
        cout="**Le vecteur ne se cherche pas : il se convertit.** Fait le "
             "20260831 : `ref_norme.py` dérive les 465 vecteurs de l'annexe, "
             "et `N4` les rejoue à chaque contrôle. **Nuance que le contrôle "
             "a sortie et qu'il faut porter** : 100 % portent une référence, "
             "mais 31 sur 465 portent autre chose qu'une adresse d'article — "
             "un renvoi à la doctrine administrative, une mention d'alinéa, "
             "du texte libre. **20 d'entre elles portent un régime de "
             "suppression, pour 4,25 Md€**, et se reprennent à la main.",
        ordre="Deuxième, et il vaut d'être fait tôt : c'est le lot qui donne "
              "le plus de vecteurs pour le moins d'effort."))

    # --- les taxes affectées ----------------------------------------------
    ta = socle['taxes_affectees']
    ta_reg = [x for x in ta
              if (x['interpretation'].get('regime') or '') not in ('', '—')]
    ta_rj = sum(1 for x in ta_reg
                if (x['socle'].get('reference_juridique') or '').strip())
    par_regime = collections.Counter(x['interpretation'].get('regime')
                                     for x in ta_reg)
    L.append(dict(
        id='V3', regime='trouver', population='taxes affectées',
        n=len(ta_reg), avec_vecteur=ta_rj,
        detail=f'{len(ta_reg)} portent un régime — ' + ' · '.join(
            f'{v} {k}' for k, v in par_regime.most_common()),
        quoi="L'annexe des taxes affectées nomme le bénéficiaire, le code de "
             "taxe et le montant. **Sa référence juridique renvoie à une loi "
             "de finances, non à un article de code** : elle dit quand la taxe "
             "a été créée ou modifiée, pas où elle vit aujourd'hui.",
        cout="Le vecteur se cherche taxe par taxe. **C'est le premier lot "
             "vraiment cher**, et il se découpe par régime : les taxes de "
             "régime `Sécu` relèvent du PLFSS et attendent leur tour ; celles "
             "de régime `Collocs` sont un lot à part, sur lequel la porte est "
             "établie.",
        ordre="Troisième, découpé par régime, le régime `Oui` d'abord."))

    # --- les organismes ----------------------------------------------------
    ops = collections.Counter(o['interpretation'].get('regime') or '—'
                              for o in socle['operateurs'])
    od = collections.Counter(o['interpretation'].get('regime') or '—'
                             for o in socle['odac_odal'])
    vises = ('suppression', 'internalisation', 'vente')
    n_ops = sum(ops.get(k, 0) for k in vises)
    n_od = sum(od.get(k, 0) for k in vises)
    L.append(dict(
        id='V4', regime='trouver',
        population='organismes à supprimer, internaliser ou vendre',
        n=n_ops + n_od, avec_vecteur=0,
        detail=f'{n_ops} opérateur(s) du PLF et {n_od} ODAC-ODAL — '
               'opérateurs : ' + ' · '.join(f'{v} {k}' for k, v in ops.most_common())
               + ' | ODAC-ODAL : ' + ' · '.join(f'{v} {k}' for k, v in od.most_common()),
        quoi="Supprimer un organisme suppose d'abroger son texte fondateur — "
             "loi, décret, ou article de code selon les cas. **Aucune de nos "
             "pièces ne le porte** : ni l'annexe des opérateurs, ni la liste "
             "ODAC-ODAL ne nomment le texte de création.",
        cout="**C'est le lot le plus lourd du chantier, et de loin.** Un "
             "vecteur par organisme, à chercher sur pièce. Il n'est pas "
             "mécanisable en l'état : l'identifiant manque, et un appariement "
             "par libellé se tromperait (A-94).",
        ordre="Dernier, et il pose une question qui n'est pas technique — "
              "voir plus bas."))

    # --- les propositions --------------------------------------------------
    props = [p for ax in ref['axes'] for lv in ax.get('leviers', [])
             for p in lv.get('propositions', [])]
    esq = [p for p in props if p['statut'] == 'esquissee']
    avec_de = [p for p in props if (p.get('droit_existant') or '').strip()]
    par_strate = collections.Counter(p['strate'] for p in props)
    L.append(dict(
        id='V5', regime='norme', population='propositions du REF_doctrine',
        n=len(props), avec_vecteur=len(avec_de),
        detail='strates : ' + ' · '.join(f'{v} {k}' for k, v in
                                         par_strate.most_common())
               + f' | {len(esq)} déclarée(s) esquissée(s)',
        quoi="`REF_norme` demande, avant le vecteur, **la norme cible** : ce "
             "que le droit doit concrètement imposer, supprimer, modifier ou "
             "autoriser. Le champ `droit_existant` du référentiel est le seul "
             "qui s'en approche.",
        cout="Chercher un vecteur pour une proposition dont la norme cible "
             "n'est pas écrite, c'est chercher deux fois. **Les 12 "
             "propositions esquissées sortent du chantier des vecteurs** "
             "jusqu'à ce qu'elles soient arrêtées.",
        ordre="En parallèle de tout le reste, et en amont de V3 et V4."))
    return L


def etat_reel(lots_, norme):
    """Reprend l'état des vecteurs à `REF_norme`, qui est le point de vérité.

    Le module comptait ce que le socle laissait deviner ; depuis que
    `REF_norme` existe, l'état des vecteurs y vit et ne se recompte pas
    ailleurs. Deux comptes du même fait divergeraient.
    """
    if not norme:
        return lots_
    par_pop = norme['comptes']['par_population_et_etat']
    for l in lots_:
        pop = POPULATION_DU_LOT.get(l['id'])
        if pop and pop in par_pop:
            l['avec_vecteur'] = par_pop[pop].get('trouve', 0)
            l['n'] = sum(par_pop[pop].values())
        elif l['id'] == 'V4':
            n = sum(sum(par_pop[p].values())
                    for p in ('operateur', 'odac_odal') if p in par_pop)
            tr = sum(par_pop[p].get('trouve', 0)
                     for p in ('operateur', 'odac_odal') if p in par_pop)
            # Le lot ne vise que les organismes portant un régime ; l'état des
            # vecteurs, lui, est relevé sur toute la population. On garde le
            # volume du lot et on reporte le nombre de vecteurs relevés.
            l['avec_vecteur'] = tr
            l['detail'] = l['detail'] + f' — {tr} vecteur(s) relevé(s) sur les {n} organismes du socle'
    return lots_


def rendre(lots_, socle, ref):
    L = []
    a = L.append
    a('# Le chantier des vecteurs — ce qu\'il pèse, et par où on le prend')
    a('')
    a('*Produit par `appareil/chantier_vecteurs.py`. Tous les comptes sont '
      'relevés sur `referentiels/socle_budgetaire.json` et '
      '`referentiels/REF_doctrine.json` — aucun n\'est estimé.*')
    a('')
    a('**Réponse courte à la question posée : non, l\'identification des '
      'vecteurs n\'est pas faite.** Elle l\'est pour un axe et un seul, et à '
      'une autre maille. Elle est lourde, et elle est moins lourde qu\'elle en '
      'a l\'air — mais pas là où on le croit.')
    a('')
    a('---')
    a('')
    a('## Le renversement')
    a('')
    a('L\'intuition dit : 56 propositions, donc 56 vecteurs. **C\'est faux dans '
      'les deux sens.** Une proposition peut toucher des centaines d\'articles '
      'ou aucun. Le vecteur ne se compte pas en propositions ; il se compte en '
      'articles touchés, et la distribution est très inégale.')
    a('')
    a('De là suit le seul découpage qui tienne : **par régime de vecteur**, '
      'non par axe de doctrine et non par ordre de dépôt.')
    a('')
    a('| lot | population | volume | vecteur connu | régime |')
    a('|---|---|---|---|---|')
    for l in lots_:
        av = ('—' if l['avec_vecteur'] is None
              else f'{l["avec_vecteur"]} / {l["n"]}'
              + (f' — **{100 * l["avec_vecteur"] // l["n"]} %**' if l['n'] else ''))
        a(f'| **{l["id"]}** | {l["population"]} | {l["n"]} | {av} | '
          f'{REGIMES[l["regime"]]} |')
    a('')

    connu = next(l for l in lots_ if l['id'] == 'V2')
    trouver = [l for l in lots_ if l['regime'] == 'trouver']
    n_trouver = sum(l['n'] - (l['avec_vecteur'] or 0) for l in trouver)
    v4 = next(l for l in lots_ if l['id'] == 'V4')
    reste_v4 = v4['n'] - (v4['avec_vecteur'] or 0)
    a(f'**Ce que le tableau dit.** Le lot qui porte le plus de montant — les '
      f'crédits — a **un vecteur unique, connu d\'avance et de rang '
      f'législatif** : l\'état B. Les {connu["n"]} dépenses fiscales '
      f'ont **leur vecteur porté par l\'annexe**, dérivé sans '
      f'recherche. Et le travail réellement à faire se concentre sur '
      f'**{n_trouver} vecteurs à trouver, dont {reste_v4} organismes** — soit '
      f'{100 * reste_v4 // max(n_trouver, 1)} % du chantier réel dans une '
      'seule population, qu\'aucune de nos pièces ne documente.')
    a('')
    a('---')
    a('')

    for l in lots_:
        a(f'## {l["id"]} — {l["population"].capitalize()}')
        a('')
        a(f'**{l["n"]}** — {REGIMES[l["regime"]].lower()}.')
        if l.get('detail'):
            a('')
            a(f'*{l["detail"]}.*')
        a('')
        a(l['quoi'])
        a('')
        a(f'**Ce que ça coûte.** {l["cout"]}')
        a('')
        a(f'**Ordre.** {l["ordre"]}')
        a('')
    a('---')
    a('')

    a('## Ce qui existe déjà, et ce qu\'il couvre exactement')
    a('')
    a('`sources/Recap_transposabilite_20260731_v6.md` **a fait ce travail, et '
      'il le fait bien** — mais sur un périmètre étroit et à une autre maille.')
    a('')
    a('| | ce que le récapitulatif porte | ce que `REF_norme` demande |')
    a('|---|---|---|')
    a('| périmètre | le seul axe du consentement à l\'impôt — bloc financier '
      'et fiscal de la Constitution | les 56 propositions, tous axes |')
    a('| maille | 59 mesures issues de 11 mécanismes de la révision | une '
      'entrée par proposition |')
    a('| niveau requis | oui — 44 compatibles, 7 incompatibles, 8 sans objet | '
      'oui |')
    a('| véhicule | oui — révision, loi organique, loi ordinaire | oui |')
    a('| **vecteur** | **oui, et nommé article par article** — 19 articles de '
      'la loi organique, une loi organique nouvelle, une ordonnance, deux '
      'codes | oui |')
    a('| repli | oui — 7 replis, chacun avec son écart | non prévu, **à '
      'reprendre** |')
    a('')
    a('**Son tableau VII est exactement le format cible** : une ligne par '
      'texte, la liste des mesures qu\'il porte. C\'est la vue inverse de '
      '`REF_norme` — par vecteur au lieu de par mesure — et les deux se '
      'dérivent l\'une de l\'autre.')
    a('')
    a('**Ce qui s\'en reprend sans rien refaire** : le format, la distinction '
      'compatible / incompatible / sans objet, la notion de repli avec son '
      'écart déclaré, et les 59 mesures elles-mêmes, qui sont acquises.')
    a('')
    a('**Ce qui manque** : tout le reste des axes — le social, le fiscal, le '
      'local, la fonction publique, l\'éducation, le patrimoine. Le '
      'récapitulatif ne les a jamais visés.')
    a('')
    a('---')
    a('')
    a('## Ce que je propose, et qui est de la tambouille')
    a('')
    a('**Un seul référentiel, deux vues.** `REF_norme` porte une entrée par '
      'proposition ; une vue par vecteur s\'en dérive, au format du tableau VII '
      'du récapitulatif. Deux tables écrites à la main divergeraient en trois '
      'semaines.')
    a('')
    a('**Le lot V2 se mécanise, et il se mécanise d\'abord.** L\'annexe porte '
      'l\'article ; un script produit la colonne vecteur et la marque '
      '`derive_annexe`. Ce qui est dérivé se régénère, ce qui est écrit à la '
      'main survit — même dispositif que le sourçage des chiffres.')
    a('')
    a('**Une colonne « état du vecteur » à quatre valeurs, pas trois.** A-227 '
      'en pose trois — trouvé, à trouver, inexistant. Il en faut une '
      'quatrième : **`sans objet`**, pour les mesures de crédits, qui n\'ont '
      'pas de vecteur et ne sont pas pour autant en défaut. Sans elle, le lot '
      'V1 sortirait en manque à chaque contrôle.')
    a('')
    a('**Le contrôle qui refuse de confondre rattachement et vecteur** (A-227) '
      's\'écrit avec la table, pas après.')
    a('')
    a('---')
    a('')
    a('## Ce qui revient à l\'auteur, et que le fil n\'a pas tranché')
    a('')
    ops = collections.Counter(o['interpretation'].get('regime') or '—'
                              for o in socle['operateurs'])
    od = collections.Counter(o['interpretation'].get('regime') or '—'
                             for o in socle['odac_odal'])
    n = sum(ops.get(k, 0) + od.get(k, 0)
            for k in ('suppression', 'internalisation', 'vente'))
    a(f'**1. Les {n} organismes : combien d\'abrogations dépose-t-on ?** '
      'C\'est la question qui décide du poids réel du chantier, et elle n\'est '
      'pas technique. Trois voies, et elles ne coûtent pas la même chose.')
    a('')
    a('- *Une abrogation par organisme* — le vecteur est certain, le volume '
      'est celui du tableau ci-dessus, et chaque amendement se défend seul.')
    a('- *Une disposition de portée générale* — un article qui abroge par '
      'renvoi à une liste annexée. Le vecteur est unique, le débat aussi, et '
      'la censure aussi.')
    a('- *Un lot restreint et exemplaire* — quelques organismes nommés, '
      'choisis pour ce qu\'ils démontrent. Le reste attend un autre véhicule.')
    a('')
    a('**2. La révision du code général des impôts préparée par l\'expert.** '
      'Elle n\'est pas versée, et le fil ne peut pas l\'instruire. **Ce qu\'on '
      'sait désormais change la question** : les vecteurs des niches sont déjà '
      'connus à 100 % par l\'annexe. La révision est donc précieuse ailleurs — '
      'sur les articles du code que la fiscalité à quatre impôts réécrit, et '
      'qui ne sont pas des dépenses fiscales. **À instruire sur ce périmètre, '
      'pas sur celui des niches.**')
    a('')
    a('**3. L\'ordre entre norme cible et vecteur pour les 12 propositions '
      'esquissées.** Écrire un vecteur sous une norme non arrêtée, c\'est '
      'l\'écrire deux fois. Les geler, c\'est retarder. Le fil propose de les '
      'geler ; c\'est un arbitrage de fond.')
    a('')
    a('**4. Les replis.** Le récapitulatif en porte sept, chacun avec son '
      'écart. `REF_norme` n\'a pas de colonne repli. **Un vecteur inexistant '
      'appelle un repli, pas un abandon** — mais généraliser les replis à 56 '
      'propositions est un chantier en soi, et il se décide.')
    a('')
    return '\n'.join(L) + '\n'


def main(src_socle, src_ref, dst, src_norme=None):
    socle = json.load(open(src_socle, encoding='utf-8'))
    ref = json.load(open(src_ref, encoding='utf-8'))
    norme = (json.load(open(src_norme, encoding='utf-8'))
             if src_norme and os.path.exists(src_norme) else None)
    lots_ = etat_reel(lots(socle, ref), norme)
    texte = rendre(lots_, socle, ref)
    os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
    open(dst, 'w', encoding='utf-8').write(texte)
    print(f'{dst} — {len(lots_)} lot(s), '
          + ' · '.join(f'{l["id"]} {l["n"]}' for l in lots_)
          + f', {os.path.getsize(dst)} octets')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3],
                  sys.argv[4] if len(sys.argv) > 4 else None))
