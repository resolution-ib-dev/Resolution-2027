# -*- coding: utf-8 -*-
"""Réconciliation des opérateurs : statut, emplois, taxes affectées, SCSP, titre 6.

Un opérateur reçoit son argent par trois canaux, et il porte des emplois. Les
quatre vivent dans trois fichiers différents, et **aucun ne se rapporte à
l'autre par un identifiant**. Cette réconciliation les met sur une ligne.

    statut   la nature juridique — établissement public administratif,
             industriel et commercial, groupement d'intérêt public…
    ETP      les emplois sous et hors plafond, à la LFI et au PLF
    TA       les taxes affectées, et ce qu'on en restitue
    SCSP     la subvention pour charges de service public, catégorie 32
    T6       les transferts, catégories 61 à 64

## Les mailles ne sont pas les mêmes, et c'est la limite à tenir

**Statut, emplois et taxes affectées se rapportent à l'opérateur.** Le statut
vient de l'annexe 2 du tome I, qui le déclare pour chaque affectataire ; les
emplois viennent de la liste officielle ; les taxes s'agrègent par affectataire
et se rattachent par appariement de libellé.

**La subvention et les transferts se rapportent au programme.** Le projet annuel
de performance ne nomme pas l'opérateur : il donne, pour chaque programme, ce
qui part en catégorie 32 et en titre 6. **Trente programmes sur cinquante-quatre
portent plus d'un opérateur** — pour ceux-là, la subvention affichée est celle
du programme, non celle de l'opérateur, et la ligne le dit.

Confondre les deux mailles produirait un tableau qui semble complet et qui
compte plusieurs fois la même subvention. Le champ `scsp_partagee` dit combien
d'opérateurs se partagent la ligne.

Usage : python3 reconcilier_operateurs.py \\
            ../referentiels/socle_budgetaire.json \\
            ../referentiels/reconciliation_operateurs.json \\
            ../livrables/reconciliation_operateurs.txt
"""
import json
import sys
from collections import defaultdict

import apparier_operateurs as app
import nomenclature_lolf as nl
import tracer_economies as eco

# Nomenclature par nature de la LOLF, pour les deux canaux budgétaires.
CAT_SCSP = {'32'}
CAT_TITRE6 = {'61', '62', '63', '64', '65'}


def par_programme(pap):
    """Ce que chaque programme porte en subvention et en transferts."""
    scsp, t6 = defaultdict(float), defaultdict(float)
    for p in pap:
        s = p['socle']
        prog, cat = s.get('programme'), s.get('categorie')
        cp = s.get('cp_plf') or 0.0
        if cat in CAT_SCSP:
            scsp[prog] += cp
        elif cat in CAT_TITRE6:
            t6[prog] += cp
    return scsp, t6


def par_affectataire(taxes, operateurs):
    """Les taxes affectées, agrégées puis rattachées à un opérateur officiel."""
    officiels = [o['socle']['operateur'] for o in operateurs]
    tables = app.index_officiel(operateurs)
    par_op = defaultdict(lambda: {'lignes': 0, 'affectation': 0.0,
                                  'annee_1': 0.0, 'ensuite': 0.0,
                                  'statuts': set(), 'regimes': set(),
                                  'libelles': set()})
    orphelines = defaultdict(lambda: {'lignes': 0, 'annee_1': 0.0,
                                      'ensuite': 0.0})
    for t in taxes:
        nom = t['socle']['beneficiaire']
        officiel, _voie, _sc = app.apparier(nom, tables, officiels)
        i = t['interpretation']
        cible = par_op[officiel] if officiel else orphelines[nom]
        cible['lignes'] += 1
        cible['annee_1'] += i.get('restitue_annee_1_eur') or 0.0
        cible['ensuite'] += i.get('restitue_ensuite_eur') or 0.0
        if officiel:
            cible['affectation'] += t['socle'].get('affectation_nette_eur') or 0.0
            if t['socle'].get('nature_juridique'):
                cible['statuts'].add(t['socle']['nature_juridique'])
            if i.get('regime'):
                cible['regimes'].add(i['regime'])
            cible['libelles'].add(nom)
    return par_op, orphelines


def _resoudre(code, nomenclature, brut):
    """Le libellé du programme, réparé par la nomenclature du PLF.

    L'onglet des opérateurs porte ses libellés de mission et de programme sous
    forme de formules, que la conversion rend en `#NAME?`. La nomenclature de
    l'annexe État porte les mêmes, en clair, indexés par le numéro de programme :
    **c'est elle qui répare, et non une saisie à la main.**
    """
    if brut and not str(brut).startswith('#'):
        return brut
    p = (nomenclature.get('programmes') or {}).get(str(code) if code else '')
    return p['libelle'] if p else None


def _mission_de(code, nomenclature, brut):
    if brut and not str(brut).startswith('#'):
        return brut
    p = (nomenclature.get('programmes') or {}).get(str(code) if code else '')
    if not p:
        return None
    return (nomenclature.get('missions') or {}).get(p.get('mission'))


def par_economie(socle):
    """L'économie chiffrée, ramenée à l'opérateur qu'elle vise.

    Le classeur chiffre l'économie sur des lignes qui ne sont pas toujours des
    opérateurs. Celles qui en visent un sont déclarées à la main dans
    `tracer_economies.RATTACHEMENTS` : c'est là, et nulle part ailleurs, que le
    rattachement s'écrit. Ici on ne fait que le suivre.
    """
    if 'economies' not in socle:
        return {}
    # Un opérateur peut porter plus d'une ligne d'économie : l'ANAH en porte
    # deux, celle de sa taxe affectée et celle de MaPrimeRénov' qu'elle
    # distribue. Une clé qui écraserait la précédente perdrait un milliard.
    par_op = defaultdict(list)
    for l in eco.tracer(socle):
        r = l.get('rattachement')
        if not r:
            continue
        for nom in r.get('operateurs') or []:
            par_op[nom].append({
                'ligne': l['id'],
                'intitule': l['intitule'].strip(),
                'rubrique': l['rubrique'],
                'destination': l['destination'],
                'canal': r['canal'],
                'total_supprime_md_eur': l['total_supprime_md_eur'],
                'restitue_annee_1_md_eur': l['restitue_annee_1_md_eur'],
                'solde_restitue_ensuite_md_eur':
                    l['solde_restitue_ensuite_md_eur'],
                'recompose_par_les_taxes_md_eur':
                    r['recompose_total_md_eur'] if r['beneficiaires'] else None,
                'part_budgetaire_md_eur': r['part_budgetaire_md_eur'],
                'hypothese': l['hypothese'],
                'chiffre_sur_budget_initial':
                    r['chiffre_sur_budget_initial'],
                'dispositif': r['dispositif'],
            })
    return par_op


def reconcilier(socle):
    operateurs = socle.get('operateurs') or []
    nomenclature = socle.get('nomenclature') or {}
    taxes = socle.get('taxes_affectees') or []
    pap = socle.get('pap') or []
    scsp, t6 = par_programme(pap)
    par_op, orphelines = par_affectataire(taxes, operateurs)
    economies = par_economie(socle)
    # Le traitement retenu programme par programme, catégorie par catégorie.
    # Il est à la maille du programme, jamais de l'opérateur : un opérateur ne
    # « porte » pas ce traitement, il en relève.
    bg = socle.get('bg_synthese') or {}
    traite = {p['programme']: p for p in bg.get('programmes', [])}

    combien_par_programme = defaultdict(int)
    for o in operateurs:
        combien_par_programme[o['socle'].get('programme')] += 1

    lignes = []
    for o in operateurs:
        s = o['socle']
        nom, prog = s['operateur'], s.get('programme')
        ta = par_op.get(nom)
        partage = combien_par_programme.get(prog, 0)
        lignes.append({
            'operateur': nom,
            'programme': prog,
            'programme_libelle': _resoudre(prog, nomenclature,
                                           s.get('programme_libelle')),
            'mission': _mission_de(prog, nomenclature, s.get('mission')),
            'regime': o['interpretation'].get('regime'),
            'entites': s.get('nombre_entites'),
            'statut': ' · '.join(sorted(ta['statuts'])) if ta and ta['statuts']
                      else None,
            'etpt_total_lfi_2025': s.get('etpt_total_lfi_2025'),
            'etpt_sous_plafond_lfi_2025': s.get('etpt_sous_plafond_lfi_2025'),
            'etpt_hors_plafond_lfi_2025': s.get('etpt_hors_plafond_lfi_2025'),
            'etpt_total_plf_2026': s.get('etpt_total_plf_2026'),
            'ta_lignes': ta['lignes'] if ta else 0,
            'ta_affectation_nette_eur': ta['affectation'] if ta else None,
            'ta_restitue_annee_1_eur': ta['annee_1'] if ta else None,
            'ta_restitue_ensuite_eur': ta['ensuite'] if ta else None,
            'ta_economie_restituee_eur': (ta['annee_1'] + ta['ensuite'])
                                         if ta else None,
            'ta_regimes': ' · '.join(sorted(ta['regimes'])) if ta else None,
            'ta_libelles': sorted(ta['libelles']) if ta else [],
            'scsp_programme_eur': scsp.get(prog),
            'titre6_programme_eur': t6.get(prog),
            'scsp_partagee': partage,
            'maille_scsp': 'opérateur' if partage == 1 else 'programme',
            'traitement_programme': ((traite.get(prog) or {})
                                     .get('traitement') or {}),
            'programme_regalien': (traite.get(prog) or {}).get('regalien'),
            'economies': economies.get(nom) or [],
        })
    return {
        '_revision': {
            'version': 'réconciliation opérateurs v1',
            'objet': "statut, emplois, taxes affectées, subvention et "
                     "transferts, sur une ligne par opérateur",
            'avertissement': "Statut, emplois et taxes affectées se rapportent "
                             "à l'opérateur. Subvention et transferts se "
                             "rapportent au programme : quand plusieurs "
                             "opérateurs le partagent, la ligne le dit et le "
                             "montant ne leur est pas imputable un par un.",
            'produit_par': 'appareil/reconcilier_operateurs.py',
        },
        'operateurs': lignes,
        'taxes_sans_operateur': {k: v for k, v in sorted(orphelines.items())},
        'comptes': {
            'operateurs': len(lignes),
            'avec_statut': sum(1 for l in lignes if l['statut']),
            'avec_taxe_affectee': sum(1 for l in lignes if l['ta_lignes']),
            'avec_scsp': sum(1 for l in lignes if l['scsp_programme_eur']),
            'scsp_a_maille_operateur': sum(1 for l in lignes
                                           if l['maille_scsp'] == 'opérateur'),
            'taxes_sans_operateur': len(orphelines),
            'avec_economie_chiffree': sum(1 for l in lignes
                                          if l['economies']),
            'lignes_economie': sum(len(l['economies']) for l in lignes),
            'economie_chiffree_md_eur': round(
                sum(e['total_supprime_md_eur'] or 0.0
                    for l in lignes for e in l['economies']), 3),
            'regime_x_traitement_scsp': _croisement(lignes),
        },
    }


def _croisement(lignes):
    """Le régime de l'opérateur croisé au traitement de sa subvention.

    **Ce n'est pas une table de fautes.** Un opérateur qu'on transforme en EPIC
    vivant de ses recettes n'a plus besoin de subvention : « epic × Oui » est
    cohérent. Un opérateur qu'on internalise rend sa subvention au ministère :
    cohérent aussi. La case qui se regarde est « suppression × rien » — on
    supprime l'opérateur et la subvention du programme reste intacte —, et
    encore : la subvention est à la maille du programme, que d'autres
    opérateurs partagent. C'est un signal, pas un verdict.
    """
    c = defaultdict(int)
    for l in lignes:
        c[(l['regime'] or '—',
           l['traitement_programme'].get('32') or '—')] += 1
    return {f'{a} × {b}': n for (a, b), n in
            sorted(c.items(), key=lambda kv: -kv[1])}


def rapport(r, dst):
    c = r['comptes']
    lignes = [
        "Réconciliation des opérateurs — statut · ETP · taxes affectées · "
        "subvention · titre 6",
        "",
        f"  {c['operateurs']} opérateur(s) de la liste officielle",
        f"  {c['avec_statut']} avec un statut juridique connu",
        f"  {c['avec_taxe_affectee']} avec au moins une taxe affectée rattachée",
        f"  {c['avec_scsp']} rattachés à un programme portant une subvention "
        f"pour charges de service public",
        f"  {c['scsp_a_maille_operateur']} pour lesquels cette subvention est "
        f"à la maille de l'opérateur — les autres la partagent",
        f"  {c['taxes_sans_operateur']} affectataire(s) de taxe qui ne sont pas "
        f"des opérateurs du PLF",
        f"  {c['avec_economie_chiffree']} portant une économie chiffrée au "
        f"classeur — {c['lignes_economie']} ligne(s), "
        f"{c['economie_chiffree_md_eur']:,.1f} Md€",
        "",
        "Le statut ne se connaît que par l'annexe des taxes affectées : un "
        "opérateur qui n'en",
        "perçoit aucune n'a pas de statut déclaré ici, et cela se voit plutôt "
        "que de se deviner.",
        "",
        "=" * 78,
    ]
    ordre = sorted(r['operateurs'],
                   key=lambda l: -((l['ta_economie_restituee_eur'] or 0.0)
                                   + (l['scsp_programme_eur'] or 0.0)))
    for l in ordre:
        if not (l['ta_lignes'] or l['scsp_programme_eur']
                or l['etpt_total_lfi_2025']):
            continue
        lignes.append(f"\n{l['operateur']}")
        lignes.append(f"  régime      {l['regime'] or '—'}"
                      f"    programme {l['programme'] or '—'} "
                      f"{(l['programme_libelle'] or '')[:44]}")
        lignes.append(f"  statut      {l['statut'] or '— non déclaré'}")
        lignes.append(f"  emplois     {l['etpt_total_lfi_2025'] or 0:,.0f} ETPT "
                      f"LFI 2025 (dont {l['etpt_sous_plafond_lfi_2025'] or 0:,.0f} "
                      f"sous plafond) · {l['etpt_total_plf_2026'] or 0:,.0f} "
                      f"PLF 2026")
        if l['ta_lignes']:
            lignes.append(
                f"  taxes       {l['ta_lignes']} ligne(s) · affectation nette "
                f"{(l['ta_affectation_nette_eur'] or 0) / 1e6:,.1f} M€ · "
                f"restitué année 1 {(l['ta_restitue_annee_1_eur'] or 0) / 1e6:,.1f} "
                f"+ ensuite {(l['ta_restitue_ensuite_eur'] or 0) / 1e6:,.1f} = "
                f"**{(l['ta_economie_restituee_eur'] or 0) / 1e6:,.1f} M€**")
        if l['scsp_programme_eur']:
            note = ('' if l['maille_scsp'] == 'opérateur'
                    else f"  ⚠ partagée entre {l['scsp_partagee']} opérateurs")
            lignes.append(f"  SCSP        "
                          f"{l['scsp_programme_eur'] / 1e6:,.1f} M€ au programme"
                          f"{note}")
        if l['titre6_programme_eur']:
            lignes.append(f"  titre 6     "
                          f"{l['titre6_programme_eur'] / 1e6:,.1f} M€ au programme")
        t = l['traitement_programme']
        if t:
            mots = ' · '.join(
                f"{k} « {v} »" for k, v in sorted(t.items())
                if v) or '—'
            lignes.append(f"  traitement  {mots}"
                          + ('   [programme régalien]'
                             if l['programme_regalien'] else ''))
            for k, v in sorted(t.items()):
                d = nl.traitement_de(v)
                if d and k == '32':
                    lignes.append(f"              catégorie 32 : {d['intitule']}"
                                  f" — {d['sens']}")
        for e in l['economies']:
            lignes.append(
                f"  ÉCONOMIE    {e['total_supprime_md_eur']:,.1f} Md€ "
                f"({e['restitue_annee_1_md_eur'] or 0:,.1f} en année 1 "
                f"+ {e['solde_restitue_ensuite_md_eur'] or 0:,.1f} ensuite) "
                f"· canal {e['canal']} · {e['ligne']}"
                + (" · dispositif distribué" if e['dispositif'] else ""))
            if e['recompose_par_les_taxes_md_eur'] is not None:
                lignes.append(
                    f"              dont {e['recompose_par_les_taxes_md_eur']:,.3f}"
                    f" Md€ recomposés depuis les taxes affectées")
            if e['part_budgetaire_md_eur'] is not None:
                lignes.append(
                    f"              part budgétaire "
                    f"{e['part_budgetaire_md_eur']:,.3f} Md€, à prendre sur "
                    f"les crédits du programme")
            if e['destination']:
                lignes.append(f"              retombe en « {e['destination']} »")
            if e['hypothese']:
                lignes.append(f"              hypothèse : {e['hypothese'].strip()}")
            if e['chiffre_sur_budget_initial']:
                lignes.append("              source : budget initial 2025 de "
                              "l'organisme, hors corpus, validée (A-113)")
    lignes.append(f"\n{'=' * 78}\nRégime de l'opérateur × traitement de la "
                  f"subvention de son programme\n{'=' * 78}")
    lignes.append("Ce n'est pas une table de fautes. Un EPIC qui vit de ses "
                  "recettes n'a plus besoin de")
    lignes.append("subvention ; un opérateur internalisé la rend au ministère. "
                  "La case qui se regarde")
    lignes.append("est « suppression × — » : l'opérateur part, la subvention "
                  "du programme reste. Et")
    lignes.append("encore : cette subvention est à la maille du programme, que "
                  "d'autres partagent.\n")
    for k, v in c['regime_x_traitement_scsp'].items():
        lignes.append(f"  {k:44s} {v:4d}")
    if r['taxes_sans_operateur']:
        lignes.append(f"\n{'=' * 78}\nAffectataires de taxe qui ne sont pas des "
                      f"opérateurs du PLF\n{'=' * 78}")
        for nom, v in sorted(r['taxes_sans_operateur'].items(),
                             key=lambda kv: -(kv[1]['annee_1']
                                              + kv[1]['ensuite'])):
            total = (v['annee_1'] + v['ensuite']) / 1e6
            if total == 0:
                continue
            lignes.append(f"  {nom[:66]:68s} {total:>10,.1f} M€ restitués")
    with open(dst, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lignes) + '\n')
    print('\n'.join(lignes[:12]))


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return 2
    socle = json.load(open(argv[1], encoding='utf-8'))
    r = reconcilier(socle)
    with open(argv[2], 'w', encoding='utf-8') as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
        f.write('\n')
    rapport(r, argv[3])
    print(f"\n{argv[2]} et {argv[3]} écrits")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
