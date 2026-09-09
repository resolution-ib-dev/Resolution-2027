# -*- coding: utf-8 -*-
"""Rend le relevé d'écarts exploitable pour un bon à tirer.

Prend le relevé de l'épreuve courante et celui de l'épreuve antérieure, marque
chaque écart de son ancienneté, et sort trois pièces :

  releve_bat.tsv   un écart par ligne : page, ancre, classe, les deux versions
  releve_bat.md    le même, classe par classe, le fond et les chiffres en tête
  controle_chiffres_epreuve.json  le contrôle arithmétique des valeurs relevées

Le contrôle des chiffres ne compare pas seulement : il rejoue les identités du
corpus sur les valeurs telles que l'épreuve les imprime, et il dit pour chacune
si le manuscrit porte la même — sans quoi un compte qui ne tombe pas juste se
lirait comme une faute de composition alors qu'il vient du manuscrit.

Usage : python3 rendre_releve_epreuve.py <releve_courant.json>
                                         <releve_anterieur.json>
                                         <epreuve.txt> <dossier_sortie>
"""
import json
import os
import re
import sys

ORDRE_CLASSE = {'fond': 0, 'perte': 1, 'coquille': 2, 'forme': 3}
ORDRE_MOTIF = {'chiffre': 0, 'note retirée': 1, 'note ajoutée': 2,
               'texte absent': 3, 'nom propre': 4, 'rédaction': 5}

# Les libellés sous lesquels chaque grandeur du corpus s'imprime. Le même jeu
# se joue sur l'épreuve et sur le manuscrit : une variante de rédaction se
# tolère dans le motif, jamais dans la valeur capturée.
MOTIFS = {
    'economies_annee_pleine_Md':
        r'conduit à économiser ([\d  ]+) milliards d’euros',
    'part_des_depenses_publiques_pct':
        r'[Cc]ela représente ([\d  ]+) % des dépenses publiques',
    'restitution_mensuelle_euro':
        r'gain total de ([\d  ]+) euros par mois pour un salarié type',
    'hausse_salaire_net_pct':
        r'augmenter tous les salaires nets de \+?([\d  ]+) %',
    'hausse_mensuelle_par_mois_pct':
        r'à raison de \+?([\d  ]+) % de salaire net par mois',
    'salaire_type_gain_euro':
        r'salaire net s’accroître de ([\d  ]+) euros nets? par mois',
    'smic_gain_euro':
        r'SMIC net augmentera de ([\d  ]+) euros par mois',
    'aide_fondamentale_euro':
        r'aide fondamentale universelle de ([\d  ]+) euros par mois remplace',
    'aide_enfant_euro':
        r'aide universelle égale à ([\d  ]+) euros par mois pour chaque enfant',
    'compte_education_annuel_euro':
        r'versons à chaque enfant ([\d  ]+) euros par an',
    'pension_socle_euro':
        r'par répartition (?:avec une pension de base )?égale à '
        r'([\d  ]+) euros par mois',
    'taux_unique_ir_pct':
        r'imposé à un taux unique estimé à ([\d  ]+) %',
    'net_par_euro_centimes':
        r'percevra ([\d  ]+) centimes nets? à chaque euro',
    'capital_par_foyer_euro':
        r'transférer un montant(?: moyen)? de ([\d  ]+) euros',
    'patrimoine_a_ceder_Md':
        r'à céder,? estimé à au moins ([\d  ]+) milliards d’euros',
    'patrimoine_public_total_Md':
        r'patrimoine des administrations publiques estimé au total à '
        r'([\d  ]+) milliards',
    'part_patrimoine_cede_pct':
        r'elle ne représente que ([\d  ]+) % du patrimoine des administrations',
    'taux_prelevements_cible_pct':
        r'taux de prélèvement obligatoire à (?:environ )?([\d  ]+) %',
    'postes_fermes':
        r'Environ ([\d  ]+) postes affectés à des missions facultatives',
    'baisse_effectifs_pct':
        r'baisse de ([\d  ]+) % des effectifs publics',
    'restitution_annee_1':
        r'À la fin de la première année, (.{0,70}?) sera déjà réalisée et '
        r'restituée|À la fin de la première année, (.{0,70}?) seront déjà '
        r'réalisées et restituées',
}


def cle(e):
    """L'identité d'un écart, indépendante de la page : c'est elle qui dit si
    l'épreuve antérieure portait déjà la même divergence."""
    return (e['ancre'].split(' →')[0], e['manuscrit'], e['epreuve'])


def marquer_anciennete(courant, anterieur, nom_courant, nom_anterieur):
    vus = {cle(e) for e in anterieur['ecarts']}
    for e in courant['ecarts']:
        e['depuis'] = nom_anterieur if cle(e) in vus else nom_courant
    return courant


def _capture(m):
    for g in m.groups():
        if g is not None:
            return g.strip()
    return ''


def valeurs_relevees(chemin_ep, bornes):
    """Les valeurs que l'épreuve imprime, chacune avec sa page.

    Rien ne se déduit, rien ne se suppose : une valeur introuvable se dit
    introuvable."""
    pages = open(chemin_ep, encoding='utf-8').read().split('\f')
    c1, c2 = bornes['corps']
    out = {}
    for nom, motif in MOTIFS.items():
        out[nom] = None
        for i in range(c1, min(c2, len(pages)) + 1):
            t = re.sub(r'\s+', ' ', pages[i - 1].replace('\n', ' '))
            m = re.search(motif, t)
            if m:
                out[nom] = {'page': i, 'valeur': _capture(m),
                            'extrait': t[max(0, m.start() - 60):m.end() + 60]}
                break
    return out


def texte_manuscrit(chemin_ms):
    """Le manuscrit rendu à plat, pour y chercher les mêmes libellés."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import relever_ecarts_epreuve as R
    blocs = R.blocs_manuscrit(chemin_ms)
    return re.sub(r'\s+', ' ', ' '.join(
        re.sub(r'⟦\d+⟧', '', b['texte']) for b in blocs
        if b['flux'] == 'corps'))


def confronter_au_manuscrit(vals, chemin_ms):
    """Pour chaque valeur relevée, dit si le manuscrit porte la même."""
    plat = texte_manuscrit(chemin_ms)
    for nom, motif in MOTIFS.items():
        if vals.get(nom) is None:
            continue
        m = re.search(motif, plat)
        vals[nom]['manuscrit'] = _capture(m) if m else 'introuvable'
        # Le voisinage du côté manuscrit, au même titre que l'`extrait` du
        # côté épreuve : c'est lui qui porte le référent du nombre, et une
        # valeur identique dont le référent bouge est un écart de chiffre.
        vals[nom]['manuscrit_extrait'] = (
            plat[max(0, m.start() - 60):m.end() + 60] if m else '')
        vals[nom]['meme_valeur_au_manuscrit'] = bool(
            m and re.sub(r'[  ]', '', _capture(m))
            == re.sub(r'[  ]', '', vals[nom]['valeur']))
    return vals


def nombre(v):
    if v is None:
        return None
    brut = re.sub(r'[  ]', '', v['valeur']).replace(',', '.')
    return float(brut) if re.fullmatch(r'\d+(\.\d+)?', brut) else None


def controler(vals):
    """Rejoue sur les valeurs relevées les identités que le corpus déclare."""
    ctrl = []

    def poser(nom, enonce, obtenu, attendu, appuis, tol=0.01, unite=''):
        commun = all(vals.get(a) and vals[a].get('meme_valeur_au_manuscrit')
                     for a in appuis)
        base = {'controle': nom, 'énoncé': enonce, 'appuis': list(appuis),
                'valeurs_identiques_au_manuscrit': commun}
        if obtenu is None or attendu is None:
            ctrl.append({**base, 'verdict': 'non joué — valeur introuvable'})
            return
        ecart = obtenu - attendu
        ctrl.append({**base, 'obtenu': round(obtenu, 4),
                     'attendu': round(attendu, 4), 'ecart': round(ecart, 4),
                     'unite': unite,
                     'verdict': 'juste' if abs(ecart) <= tol else 'faux'})

    v = {k: nombre(vals.get(k)) for k in MOTIFS}
    v_bruts = {k: vals.get(k) for k in MOTIFS}

    poser('aide de l’enfant = moitié de l’aide fondamentale',
          '275 = 550 / 2', v['aide_enfant_euro'],
          v['aide_fondamentale_euro'] / 2 if v['aide_fondamentale_euro']
          else None, ('aide_enfant_euro', 'aide_fondamentale_euro'),
          0.5, '€/mois')
    # Le compte éducation ne se rapporte pas à l'aide de l'enfant : la p. 123
    # les cumule — « en plus de l'aide fondamentale universelle de 275 euros
    # par mois […] versons à chaque enfant 6 600 euros par an » —, et la note
    # 133 dit que les 6 600 s'estiment sur le coût public réel de l'éducation,
    # pas sur un multiple d'une aide. L'identité posée ici le 20260907 était
    # une définition inventée, et elle sortait un faux qui n'existait pas.
    # Elle ne se rejoue pas ; ce qu'elle prétendait contrôler relève du
    # chiffrage du corpus et non du bon à tirer. Retirée le 20260908.
    # Un chiffre inchangé dont la définition bouge est un écart de chiffre, et
    # c'est le seul endroit où l'arithmétique de l'épreuve bloque. Le contrôle
    # posé le 20260907 comparait 1 100 au bon nombre sans regarder de quoi
    # 1 100 était le nom : il sortait « juste » sur une page cassée. Ce qui
    # décide n'est donc pas la valeur mais le référent que la page imprime,
    # et il se lit dans l'extrait, jamais de mémoire.
    #
    #   « par répartition **avec une pension de base** égale à 1 100 »
    #        → 1 100 est la pension de base : socle 550 + aide 550. Juste.
    #   « par répartition égale à 1 100 »
    #        → 1 100 est le socle seul, et la note 124, que l'épreuve ne
    #          touche pas, pose que le socle « forme avec l'aide fondamentale
    #          une pension de retraite de base » : celle-ci vaudrait 1 650,
    #          quand le corpus la déclare à 1 100. Faux de 550 €/mois.
    ref_ep = ((v_bruts['pension_socle_euro'] or {}).get('extrait') or '')
    ref_ms = ((v_bruts['pension_socle_euro'] or {}).get('manuscrit_extrait')
              or '')
    pension_nommee = 'pension de base' in ref_ep
    if pension_nommee:
        poser('pension de base = socle + aide fondamentale',
              '1 100 = 550 + 550', v['pension_socle_euro'],
              v['aide_fondamentale_euro'] * 2 if v['aide_fondamentale_euro']
              else None, ('pension_socle_euro', 'aide_fondamentale_euro'),
              1, '€/mois')
    else:
        poser('pension de base = socle + aide fondamentale — référent déplacé',
              'la page ne nomme plus la pension de base : 1 100 y est le socle '
              'seul, et la note 124 de l’épreuve en fait 1 100 + 550',
              v['pension_socle_euro'],
              v['pension_socle_euro'] + v['aide_fondamentale_euro']
              if v['pension_socle_euro'] and v['aide_fondamentale_euro']
              else None, ('pension_socle_euro', 'aide_fondamentale_euro'),
              1, '€/mois')
    # Le déplacement du référent se dit sur le contrôle lui-même, avec les deux
    # voisinages, plutôt que dans une entrée séparée : c'est un seul fait.
    if pension_nommee != ('pension de base' in ref_ms):
        ctrl[-1]['referent_deplace'] = {'manuscrit': ref_ms.strip(),
                                        'epreuve': ref_ep.strip()}
    poser('net par euro gagné = 1 − taux unique',
          '77 = 100 − 23', v['net_par_euro_centimes'],
          100 - v['taux_unique_ir_pct'] if v['taux_unique_ir_pct'] else None,
          ('net_par_euro_centimes', 'taux_unique_ir_pct'), 0.5, 'centimes')
    poser('patrimoine cédé rapporté au patrimoine public',
          '600 / 4 500 = 13 %', v['part_patrimoine_cede_pct'],
          100 * v['patrimoine_a_ceder_Md'] / v['patrimoine_public_total_Md']
          if v['patrimoine_a_ceder_Md'] and v['patrimoine_public_total_Md']
          else None, ('part_patrimoine_cede_pct', 'patrimoine_a_ceder_Md',
                      'patrimoine_public_total_Md'), 0.6, '%')
    poser('capital par foyer × 30 millions de foyers = patrimoine cédé',
          '20 000 × 30 M = 600 Md€', v['patrimoine_a_ceder_Md'],
          v['capital_par_foyer_euro'] * 30e6 / 1e9
          if v['capital_par_foyer_euro'] else None,
          ('capital_par_foyer_euro', 'patrimoine_a_ceder_Md'), 1, 'Md€')
    # La montée ne court pas douze mois : la p. 141 pose une latence — « au
    # bout de six mois, les premières économies seront constatées et rendues
    # […] à raison de +2 % de salaire net par mois jusqu'à atteindre +13 % au
    # bout d'un an ». Six à sept mois de montée encadrent les 13 points, et
    # le multiplicateur douze était de moi, pas du texte. L'identité se
    # rejoue sur la fenêtre que le texte donne, et elle tombe juste.
    poser('montée mensuelle sur la fenêtre annoncée = hausse annoncée',
          '+2 % par mois sur les six à sept mois qui restent après la latence '
          'de six mois, contre +13 % au bout d’un an',
          v['hausse_salaire_net_pct'],
          v['hausse_mensuelle_par_mois_pct'] * 6.5
          if v['hausse_mensuelle_par_mois_pct'] else None,
          ('hausse_mensuelle_par_mois_pct', 'hausse_salaire_net_pct'),
          1.5, 'points')
    return ctrl


# ------------------------------------------------------------------ rendus

def tsv(releve, chemin):
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write('page\tflux\tclasse\tmotif\tdepuis\tancre\tmanuscrit\t'
                'epreuve\tcontexte\n')
        for e in sorted(releve['ecarts'],
                        key=lambda x: (ORDRE_CLASSE.get(x['classe'], 9),
                                       ORDRE_MOTIF.get(x.get('motif'), 9),
                                       x['page'] or 0)):
            ligne = [str(e['page'] or ''), e['flux'], e['classe'],
                     e.get('motif', ''), e.get('depuis', ''), e['ancre'],
                     e['manuscrit'], e['epreuve'], e.get('avant', '')[-60:]]
            f.write('\t'.join(c.replace('\t', ' ').replace('\n', ' ')
                              for c in ligne) + '\n')


def md(releve, ctrl, vals, chemin, nom_courant, nom_anterieur):
    e = releve['ecarts']
    par = {}
    for x in e:
        par.setdefault(x['classe'], []).append(x)
    with open(chemin, 'w', encoding='utf-8') as f:
        w = f.write
        w('# Relevé d’écarts — épreuve contre manuscrit\n\n')
        w(f'Épreuve `{os.path.basename(releve["epreuve"])}` contre le '
          f'manuscrit du coffre, restauré par copie d’octets et vérifié à son '
          f'empreinte.\n\n')
        w('Un écart par ligne. Le manuscrit d’un côté, l’épreuve de l’autre. '
          'Rien n’est corrigé, rien n’est réécrit, aucun écart de fond n’est '
          'tranché : les arbitrages sont de l’auteur, y compris les '
          'coquilles.\n\n')
        w('## Le compte\n\n')
        w('| classe | nombre |\n|---|---|\n')
        for c, n in sorted(releve['comptes'].items(),
                           key=lambda kv: ORDRE_CLASSE.get(kv[0], 9)):
            w(f'| {c} | {n} |\n')
        n2 = sum(1 for x in e if x.get('depuis') == nom_courant)
        n1 = sum(1 for x in e if x.get('depuis') == nom_anterieur)
        w(f'\nDont **{n2} apparus entre la première épreuve et celle-ci**, et '
          f'{n1} déjà portés par la première.\n\n')

        w('## Contrôle arithmétique des valeurs relevées\n\n')
        w('Les identités du corpus, rejouées sur les valeurs telles que '
          'l’épreuve les imprime. La dernière colonne dit si le manuscrit '
          'porte les mêmes valeurs : quand il les porte, un compte faux ne '
          'vient pas de la composition.\n\n')
        w('| contrôle | obtenu | attendu | verdict | mêmes valeurs au '
          'manuscrit |\n|---|---|---|---|---|\n')
        for c in ctrl:
            w(f'| {c["controle"]} — {c["énoncé"]} | {c.get("obtenu", "—")} | '
              f'{c.get("attendu", "—")} | **{c["verdict"]}** | '
              f'{"oui" if c["valeurs_identiques_au_manuscrit"] else "non"} |\n')
        w('\n### Les valeurs telles que l’épreuve les imprime\n\n')
        w('| grandeur | page | épreuve | manuscrit |\n|---|---|---|---|\n')
        for k, val in vals.items():
            if val:
                marque = '' if val.get('meme_valeur_au_manuscrit') else ' ⚠'
                w(f'| {k.replace("_", " ")} | {val["page"]} | '
                  f'{val["valeur"]}{marque} | {val.get("manuscrit", "")} |\n')
            else:
                w(f'| {k.replace("_", " ")} | — | introuvable | |\n')

        for classe in ('fond', 'perte', 'coquille'):
            liste = sorted(par.get(classe, []),
                           key=lambda x: (ORDRE_MOTIF.get(x.get('motif'), 9),
                                          x['page'] or 0))
            w(f'\n## {classe} — {len(liste)} écart(s)\n')
            motif = None
            for x in liste:
                if x.get('motif') != motif:
                    motif = x.get('motif')
                    w(f'\n### {motif}\n\n')
                w(f'**p. {x["page"]}** · `{x["ancre"]}` · apparu en '
                  f'{x.get("depuis", "")}\n\n')
                if x.get('avant'):
                    w(f'> …{x["avant"][-70:]}\n\n')
                w(f'- manuscrit : {x["manuscrit"] or "*(rien)*"}\n')
                w(f'- épreuve : {x["epreuve"] or "*(rien)*"}\n\n')

        w('\n## forme — ce qui se compte et ne se détaille pas\n\n')
        w('| élément | nombre |\n|---|---|\n')
        for k, val in releve['forme'].items():
            w(f'| {k.replace("_", " ")} | {val} |\n')
        if releve.get('notes_renumerotees'):
            r = releve['notes_renumerotees']
            w(f'\nLes {len(r)} notes renumérotées vont du n° '
              f'{r[0]["manuscrit"]} au n° {r[-1]["manuscrit"]} du manuscrit ; '
              f'le décalage suit les notes ajoutées et retirées, relevées '
              f'plus haut.\n')
        if releve.get('cesures_non_decidables'):
            w('\n## Non décidable sur le texte extrait\n\n')
            w('La composition coupe ces mots en fin de ligne ; l’extraction '
              'les recolle sans le tiret. À vérifier à l’œil sur l’épreuve, '
              'et nulle part ailleurs.\n\n')
            for x in releve['cesures_non_decidables']:
                w(f'- p. {x["page"]} — manuscrit « {x["manuscrit"]} », '
                  f'épreuve « {x["epreuve"]} »\n')


def main(courant, anterieur, chemin_ep, sortie):
    nc = re.search(r'EP\d+', os.path.basename(courant))
    na = re.search(r'EP\d+', os.path.basename(anterieur))
    nom_courant = nc.group(0) if nc else 'courante'
    nom_anterieur = na.group(0) if na else 'antérieure'
    rc = json.load(open(courant, encoding='utf-8'))
    ra = json.load(open(anterieur, encoding='utf-8'))
    rc = marquer_anciennete(rc, ra, nom_courant, nom_anterieur)
    vals = valeurs_relevees(chemin_ep, rc['bornes'])
    vals = confronter_au_manuscrit(vals, rc['manuscrit'])
    ctrl = controler(vals)
    os.makedirs(sortie, exist_ok=True)
    tsv(rc, os.path.join(sortie, 'releve_bat.tsv'))
    md(rc, ctrl, vals, os.path.join(sortie, 'releve_bat.md'),
       nom_courant, nom_anterieur)
    json.dump({'valeurs': vals, 'controles': ctrl},
              open(os.path.join(sortie, 'controle_chiffres_epreuve.json'),
                   'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(rc, open(courant, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    faux = [c for c in ctrl if c['verdict'] == 'faux']
    injoues = [c for c in ctrl if c['verdict'].startswith('non joué')]
    print(f'{sortie}/releve_bat.tsv et releve_bat.md — '
          f'{len(rc["ecarts"])} écart(s) détaillé(s), '
          f'{rc["comptes"].get("forme", 0)} comptés en forme')
    print(f'  contrôle des chiffres : {len(ctrl) - len(faux) - len(injoues)} '
          f'juste(s), {len(faux)} faux, {len(injoues)} non joué(s)')
    for c in faux:
        print(f'    FAUX {c["controle"]} : {c["obtenu"]} contre '
              f'{c["attendu"]} {c.get("unite", "")} — mêmes valeurs au '
              f'manuscrit : '
              f'{"oui" if c["valeurs_identiques_au_manuscrit"] else "non"}')
    ecarts_valeur = [k for k, val in vals.items()
                     if val and not val.get('meme_valeur_au_manuscrit')]
    print('  valeurs qui diffèrent du manuscrit : '
          + (', '.join(ecarts_valeur) or 'aucune'))
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:5]))
