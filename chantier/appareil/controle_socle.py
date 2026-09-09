# -*- coding: utf-8 -*-
"""Bouclage du socle budgétaire sur les totaux du classeur.

**Tant que ce contrôle n'est pas vert, la grille de lecture est une hypothèse.**
Le classeur de l'auteur reste la source officielle ; ce que ce module prétend,
c'est le lire correctement. La seule preuve possible est de recomposer ses
agrégats depuis les lignes et de retrouver ce qu'il affiche.

Une divergence ne se corrige pas au socle : elle dit que la grille est fausse,
et c'est la grille qu'on reprend.

Neuf bouclages.

  S1  les opérateurs se comptent, un régime chacun
  S2  les emplois des opérateurs se répartissent entre les régimes
  S3  la synthèse des agences se somme ligne à ligne
  S4  les quatre familles font le total des agences d'État
  S5  les taxes affectées se somment aux totaux de tête — en budgétaire, le
      « gage CSG » est ce qui est restituable en année 1 et le « solde » ce qui
      est restitué ensuite ; **l'économie valorisable restituée est leur total**
  S6  les taxes d'un bénéficiaire nommé se somment à sa ligne de tête
  S7  les dépenses fiscales se somment aux totaux de tête
  S8  l'arbre des économies se somme de bas en haut, et chaque ligne rattachée
      se recompose depuis les taxes affectées de son assiette
  S9  la chaîne des emplois et des charges se rejoue depuis la synthèse du
      budget général — un écart ouvert reste ouvert
  S10 la couche budgétaire se recompose de bas en haut : les 128 programmes
      font les 35 missions, les missions font la grille des dix catégories, et
      **la part supprimable dès l'année 1 se retrouve depuis les traitements
      écrits programme par programme**. C'est ce dernier point qui prouve que
      la couche de décision est lue correctement.

Usage : python3 controle_socle.py ../referentiels/socle_budgetaire.json
"""
import json
import sys

import nomenclature_lolf as nl
import tracer_economies as eco_mod

# Les totaux que le classeur affiche, relevés à la main dans ses cellules de
# tête. Ce sont eux qui font foi : le socle doit les retrouver, pas l'inverse.
#
# Une tolérance en unité de la grandeur, et large là où le classeur arrondit à
# l'affichage. Elle ne se remonte jamais pour faire tomber un compte.
ATTENDUS = {
    'operateurs_entites': (434, 0.5, "onglet Opérateurs, F3"),
    'operateurs_par_regime': ({'vente': 15, 'suppression': 123,
                               'epic_musee': 36, 'epic_enseignement': 226,
                               'internalisation': 34}, 0.5,
                              "onglet Opérateurs, N3:R3"),
    'etpt_par_regime': ({'vente': 10476, 'suppression': 99885,
                         'epic_musee': 25039, 'epic_enseignement': 326723,
                         'internalisation': 17391}, 1.0,
                        "onglet Opérateurs, N4:R4 — sur l'ETPT total LFI 2025"),
    'etpt_total_lfi': (479514, 1.0, "onglet Opérateurs, G4"),
    'etpt_total_plf': (478026, 1.0, "onglet Opérateurs, J4"),
    'agences_etat_total': (1104, 0.5, "onglet Synthèse agences, D5"),
    'taxes_restitue_annee_1_m_eur': (8119.66998217549, 0.01,
                             "onglet taxes affectées, K10"),
    'taxes_restitue_ensuite_m_eur': (9802.72165393334, 0.01,
                             "onglet taxes affectées, L10"),
    'taxes_economie_restituee_m_eur': (17922.3916361088, 0.02,
                                          "onglet taxes affectées, N10"),
    'df_nombre': (465, 0.5, "onglet Chiffrages IB, F6"),
    'df_realisation_2024_md_eur': (89.406, 0.001,
                                   "onglet Chiffrages IB, G6"),
    'df_realisation_yc_tva_md_eur': (101.320988610478, 0.001,
                                     "onglet Chiffrages IB, G7"),
    'df_gage_net_md_eur': (43.1263651708428, 0.001,
                           "onglet Chiffrages IB, K7"),
    'df_effet_macro_md_eur': (29.1407851708428, 0.001,
                              "onglet Chiffrages IB, L7"),
}

# Les bénéficiaires que la tête de l'onglet des taxes affectées isole, avec le
# libellé exact sur lequel ses SUMIFS filtrent. Un libellé qui changerait au PLF
# suivant casserait le total sans bruit : c'est pourquoi il est écrit ici.
BENEFICIAIRES = {
    'France Compétences': (3374.8979736, 6749.7959472),
    "Agences de l'eau": (695.1201867, 1390.2403734),
    'Action Logement Services': (636.666666666667, 1273.33333333333),
}

FAMILLES = ('operateurs_plf', 'organismes_hors_plf',
            'autorites_independantes', 'commissions')


def proche(a, b, tol):
    return a is not None and b is not None and abs(a - b) <= tol


def somme(lignes, bloc, champ):
    return sum(l[bloc].get(champ) or 0.0 for l in lignes)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    s = json.load(open(argv[1], encoding='utf-8'))
    echecs = []

    def verifier(cle, obtenu):
        attendu, tol, ou = ATTENDUS[cle]
        if isinstance(attendu, dict):
            for k, v in attendu.items():
                if not proche(obtenu.get(k), v, tol):
                    echecs.append((f'{cle}.{k}', obtenu.get(k), v, ou))
            return
        if not proche(obtenu, attendu, tol):
            echecs.append((cle, obtenu, attendu, ou))

    ops = s.get('operateurs') or []
    taxes = s.get('taxes_affectees') or []
    dfs = s.get('depenses_fiscales') or []
    agences = s.get('agences') or {}

    # S1 — les opérateurs, et un seul régime chacun
    multiples = [o['id'] for o in ops if o['interpretation']['regimes_multiples']]
    sans = [o['id'] for o in ops if o['interpretation']['sans_regime']]
    print(f"S1 — {len(ops)} ligne(s) d'opérateur, {len(multiples)} à régimes "
          f"multiples, {len(sans)} sans régime")
    for i in multiples:
        print(f"    régimes multiples — {i}")
    verifier('operateurs_entites', somme(ops, 'socle', 'nombre_entites'))
    par_regime = {}
    etpt_regime = {}
    for o in ops:
        r = o['interpretation']['regime']
        if not r:
            continue
        par_regime[r] = par_regime.get(r, 0.0) \
            + (o['socle'].get('nombre_entites') or 0.0)
        etpt_regime[r] = etpt_regime.get(r, 0.0) \
            + (o['socle'].get('etpt_total_lfi_2025') or 0.0)
    verifier('operateurs_par_regime', par_regime)

    # S2 — les emplois par régime
    print(f"\nS2 — emplois des opérateurs par régime")
    for r in sorted(etpt_regime):
        print(f"    {r:20s} {etpt_regime[r]:>10,.0f} ETPT")
    verifier('etpt_par_regime', etpt_regime)
    verifier('etpt_total_lfi', somme(ops, 'socle', 'etpt_total_lfi_2025'))
    verifier('etpt_total_plf', somme(ops, 'socle', 'etpt_total_plf_2026'))

    # S3 — la synthèse des agences, ligne à ligne
    print(f"\nS3 — {len(agences)} ligne(s) de synthèse des agences")
    for nom, l in sorted(agences.items()):
        total = l.get('total')
        detail = sum(v or 0.0 for k, v in l.items() if k != 'total')
        etat = 'OK ' if proche(detail, total, 0.5) else 'ÉCART'
        print(f"    {etat} {nom:26s} détail {detail:>8,.0f} "
              f"contre total {total or 0:>8,.0f}")
        if not proche(detail, total, 0.5):
            echecs.append((f'agences.{nom}', detail, total,
                           'onglet Synthèse agences'))

    # S4 — les quatre familles font les agences d'État
    familles = sum((agences.get(f) or {}).get('total') or 0.0
                   for f in FAMILLES)
    print(f"\nS4 — les quatre familles font {familles:,.0f}")
    verifier('agences_etat_total', familles)

    # S5 — les taxes affectées
    gage = somme(taxes, 'interpretation', 'restitue_annee_1_eur') / 1e6
    eco = somme(taxes, 'interpretation', 'restitue_ensuite_eur') / 1e6
    print(f"\nS5 — {len(taxes)} ligne(s) de taxe affectée")
    print(f"    restitué année 1 {gage:,.3f} M€ · restitué ensuite "
          f"{eco:,.3f} M€ · économie restituée totale {gage + eco:,.3f} M€")
    verifier('taxes_restitue_annee_1_m_eur', gage)
    verifier('taxes_restitue_ensuite_m_eur', eco)
    verifier('taxes_economie_restituee_m_eur', gage + eco)

    # S6 — les bénéficiaires nommés
    print(f"\nS6 — {len(BENEFICIAIRES)} bénéficiaire(s) isolé(s) en tête")
    for nom, (att_gage, att_eco) in BENEFICIAIRES.items():
        lignes = [t for t in taxes if t['socle']['beneficiaire'] == nom]
        g = somme(lignes, 'interpretation', 'restitue_annee_1_eur') / 1e6
        e = somme(lignes, 'interpretation', 'restitue_ensuite_eur') / 1e6
        ok = proche(g, att_gage, 0.01) and proche(e, att_eco, 0.01)
        print(f"    {'OK ' if ok else 'ÉCART'} {nom:28s} "
              f"{len(lignes):3d} ligne(s) · gage {g:>10,.3f} · éco {e:>10,.3f}")
        if not ok:
            echecs.append((f'beneficiaire.{nom}', (round(g, 3), round(e, 3)),
                           (round(att_gage, 3), round(att_eco, 3)),
                           'onglet taxes affectées, K2:L9'))

    # S7 — les dépenses fiscales
    print(f"\nS7 — {len(dfs)} dépense(s) fiscale(s)")
    verifier('df_nombre', float(len(dfs)))
    verifier('df_realisation_2024_md_eur',
             somme(dfs, 'socle', 'realisation_2024_m_eur') / 1000)
    verifier('df_realisation_yc_tva_md_eur',
             somme(dfs, 'interpretation', 'realisation_yc_tva_apu_m_eur') / 1000)
    verifier('df_gage_net_md_eur',
             somme(dfs, 'interpretation', 'gage_net_csg_m_eur') / 1000)
    verifier('df_effet_macro_md_eur',
             somme(dfs, 'interpretation', 'effet_macro_m_eur') / 1000)

    # S8 — l'arbre des économies, et le rattachement de chaque ligne
    # S9 — la chaîne des emplois et des charges, formule reconstituée
    if 'economies' in s:
        lignes_eco = eco_mod.tracer(s)
        bcl = eco_mod.bouclages(lignes_eco)
        ko = [b for b in bcl if eco_mod.verdict(b) != 'accord']
        rat = [l for l in lignes_eco if l['rattachement']]
        print(f"\nS8 — {len(lignes_eco)} ligne(s) d'économie, {len(rat)} "
              f"rattachées · {len(bcl) - len(ko)}/{len(bcl)} bouclages")
        for b in ko:
            echecs.append((f"economies.{b['objet']}", round(b['recompose'], 3),
                           b['affiche'], 'onglet Détail Economies'))
        # Un compte de lignes de taxe qui ne tient plus dit qu'un affectataire
        # est apparu ou a disparu : le rattachement est à reprendre.
        for l in rat:
            r = l['rattachement']
            if not r['compte_taxes_tenu']:
                echecs.append((f"economies.taxes.{l['intitule'].strip()}",
                               r['lignes_taxes'], r['lignes_taxes_attendues'],
                               'annexe 2 du tome I — rattachement à reprendre'))
        deriv = eco_mod.derivations(s)
        concept = [d for d in deriv if d['verdict'] == 'écart de concept']
        ouverts = [d for d in deriv if d['verdict'] == 'ÉCART OUVERT']
        print(f"\nS9 — {len(deriv)} dérivation(s) de la chaîne des emplois, "
              f"{len(concept)} écart(s) de concept, {len(ouverts)} ouvert(s)")
        for d in concept:
            print(f"    concept  {d['objet']} — calculé {d['calcule']} "
                  f"contre {d['ecrit_au_classeur']} écrit, écart {d['ecart']}")
        for d in ouverts:
            print(f"    ÉCART    {d['objet']} — calculé {d['calcule']} "
                  f"contre {d['ecrit_au_classeur']} écrit ({d['ou']})")
        print("    Un écart de concept est documenté et clos : les deux "
              "sources ne comptent pas\n    la même chose. Un écart ouvert ne "
              "l'est pas, et il reste sous les yeux.")

    # S10 — la couche budgétaire : grille, missions, programmes, traitements
    bg = s.get('bg_synthese') or {}
    if bg.get('grille'):
        grille = {g['categorie']: g for g in bg['grille']}
        missions, programmes = bg['missions'], bg['programmes']
        cats = list(grille)
        print(f"\nS10 — {len(grille)} catégorie(s), {len(missions)} mission(s), "
              f"{len(programmes)} programme(s) porteurs d'un traitement")

        # les missions font la grille
        for c in cats:
            att = grille[c]['credit_plf_m_eur']
            obt = sum((m['credit_plf_m_eur'].get(c) or 0.0) for m in missions)
            if not proche(obt, att, 0.02):
                echecs.append((f'bg.grille.{c}', round(obt, 2), att,
                               'onglet Synthèse, ligne 4'))

        # les programmes font les missions
        par_mission = {}
        for p in programmes:
            par_mission.setdefault(p['mission'], []).append(p)
        trous = []
        for m in missions:
            for c in cats:
                att = m['credit_plf_m_eur'].get(c) or 0.0
                obt = sum((p['credit_plf_m_eur'].get(c) or 0.0)
                          for p in par_mission.get(m['code'], []))
                if not proche(obt, att, 0.02):
                    trous.append((m['code'], c, round(obt, 2), round(att, 2)))
        print(f"    {len(trous)} case(s) où le détail programme ne fait pas "
              f"sa mission")
        for code, c, obt, att in trous:
            print(f"      mission {code} catégorie {c} — détail {obt} contre "
                  f"{att} à la ligne mission : un programme manque au bloc")

        # la suppression immédiate se retrouve depuis les traitements
        print("    part supprimable dès l'année 1, recomposée depuis les "
              "traitements écrits :")
        for c in nl.CATEGORIES_TRAITEES:
            att = grille[c]['suppression_immediate_m_eur']
            obt = sum((p['credit_plf_m_eur'].get(c) or 0.0) for p in programmes
                      if p['traitement'].get(c) == 'Oui')
            if att is None:
                print(f"      {c} — {obt:12,.2f} M€ recomposés ; le classeur "
                      f"laisse la cellule en erreur, elle n'est pas comparée")
                continue
            etat = 'OK ' if proche(obt, att, 0.02) else 'ÉCART'
            print(f"      {etat} {c} — {obt:12,.2f} contre {att:12,.2f}")
            if not proche(obt, att, 0.02):
                echecs.append((f'bg.suppression.{c}', round(obt, 2), att,
                               'onglet Synthèse, ligne 4, colonne de '
                               'traitement'))

        inconnus = bg.get('traitements_inconnus') or []
        if inconnus:
            echecs.append(('bg.traitements_inconnus', inconnus, [],
                           'un mot de traitement absent de la nomenclature'))
        # la couverture : ce que la couche de décision ne touche pas
        au_bloc = {p['programme'] for p in programmes}
        hors = {}
        for x in s.get('pap', []):
            y = x['socle']
            pr = y.get('programme')
            if not pr or pr in au_bloc:
                continue
            if y.get('categorie') in nl.CATEGORIES_TRAITEES:
                hors.setdefault(pr, {'libelle': y.get('programme_libelle'),
                                     'type': y.get('type_mission'),
                                     'm_eur': 0.0})
                hors[pr]['m_eur'] += (y.get('cp_plf') or 0.0) / 1e6
        gros = sorted((v for v in hors.values() if v['m_eur'] >= 1),
                      key=lambda v: -v['m_eur'])
        print(f"    {len(gros)} programme(s) hors couche de décision, "
              f"{sum(v['m_eur'] for v in gros):,.0f} M€ de crédits traitables :")
        for v in gros:
            print(f"      {v['m_eur']:12,.1f} M€  [{v['type']}] {v['libelle']}")

    print(f"\n{len(echecs)} bouclage(s) en échec")
    for cle, obtenu, attendu, ou in echecs:
        print(f"    {cle}")
        print(f"        socle   {obtenu}")
        print(f"        classeur{'':1s} {attendu}   ({ou})")
    if not echecs:
        print("La grille de lecture retrouve tous les totaux du classeur.")
    return 1 if echecs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
