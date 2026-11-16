#!/usr/bin/env python3
"""Le tri unique des impôts, du 20261116.

Base : le tri du 20261103 (six devenirs, 434 rangs). On y reporte ce que la
version du 20261020 portait de plus (archive/tri_20261020/) et l'on applique les
règles du mandat du 20261116. Rien n'est recalculé en amont : ce module lit deux
tables et en écrit trois.

  lit    referentiels/sort_prelevements_20261103.tsv
         archive/tri_20261020/versions_branche/referentiels/sort_prelevements_20261015.tsv
         referentiels/schema_refonte_fiscalite_2024.tsv
  écrit  referentiels/sort_prelevements_20261116.tsv
         livrables/tri_prelevements/rangs_deplaces_20261116.tsv
         livrables/tri_prelevements/passage_tableau_20261116.tsv

Se joue de n'importe où : python3 appareil/tri_porte/tri_unique.py
Code retour 1 si un invariant casse (434 rangs, six devenirs, un bloc par rang
conservé en complément, aucun « False » en colonne `question`).
"""
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent
REF = RACINE / 'referentiels'
OUT = RACINE / 'livrables/tri_prelevements'
BASE = REF / 'sort_prelevements_20261103.tsv'
OCT = RACINE / 'archive/tri_20261020/versions_branche/referentiels/sort_prelevements_20261015.tsv'
SCHEMA = REF / 'schema_refonte_fiscalite_2024.tsv'
SORTIE = REF / 'sort_prelevements_20261116.tsv'

GRAND, REMPL, FONDU, COMPL, FUSION, RNF = (
    'grand impôt conservé', 'remplacé par un grand impôt', 'fondu dans l’équilibre des quatre grands impôts',
    'conservé en complément', 'à fusionner', 'recette non fiscale')
DEVENIRS = [GRAND, REMPL, FONDU, COMPL, FUSION, RNF]
BLOCS = {'Accise (sur-TVA)', 'Simili TVA', 'Taxe de séjour unique', 'Fonds de garantie', 'Fiscalité outre-mer',
         'Union européenne'}
TVA = 'Taxe sur la valeur ajoutée'
SANS_OBJET = 'sans objet (devenir sans abrogation)'

AUTEURE = 'réponse de l’auteure'
PILOTAGE = 'tranché par le pilotage, révocable'
FIL = 'tranché par ce fil sur les règles écrites, révocable'

# ------------------------------------------------------------------ les rangs déplacés ou requalifiés
# n : (devenir, impôt cible, bloc, règle du mandat, statut, motif) — None laisse la valeur en place.
MOUV = {
    # règle 1 — report de la version du 20 octobre
    '6': (FONDU, '', '', 1, PILOTAGE, 'indemnités de rupture conventionnelle : taxe sur la main-d’œuvre, elle n’ouvre aucun droit (reclassement validé par l’auteure le 20261020)'),
    '12': (FONDU, '', '', 1, PILOTAGE, 'indemnités de mise à la retraite : taxe sur la main-d’œuvre, elle n’ouvre aucun droit (reclassement validé par l’auteure le 20261020)'),
    '135': (REMPL, TVA, '', 1, PILOTAGE, 'taxe sur les transactions financières : rattachée au poste « autres taxes sur les produits », qui porte ses euros, donc à la TVA (troisième échange du 20261020)'),
    '137': (REMPL, TVA, '', 1, PILOTAGE, 'ordres annulés à haute fréquence : suit la taxe sur les transactions financières (troisième échange du 20261020)'),
    # règle 3 — le tableau « Refonte fiscalité » fait foi : énergie
    '211': (REMPL, TVA, '', 3, PILOTAGE, 'électricité : le tableau supprime 8 Md€ sur l’énergie, la taxe sur l’électricité est fondue dans la TVA, carburants et gaz gardés'),
    '214': (REMPL, TVA, '', 3, PILOTAGE, 'électricité, part des communes : fondue dans la TVA avec la taxe sur l’électricité'),
    '215': (REMPL, TVA, '', 3, PILOTAGE, 'électricité, part des départements : fondue dans la TVA avec la taxe sur l’électricité'),
    # règle 3 — assurances : rien de supprimé
    '194': (COMPL, '', 'Simili TVA', 3, PILOTAGE, 'taxe de solidarité additionnelle : le tableau garde les 19,2 Md€ d’assurances, qui la comprennent'),
    '277': (COMPL, '', 'Simili TVA', 3, PILOTAGE, 'protection juridique : majoration de la taxe sur les conventions d’assurance, gardée avec elle'),
    'N7': (COMPL, '', 'Simili TVA', 3, FIL, 'contribution des complémentaires santé (L. 862-4-1 CSS) : mêmes redevables et même assiette que la taxe de solidarité additionnelle (relevé au dépôt de droit), elle la suit'),
    # règle 4 — les 13 qualifications en attente
    '128': (None, None, None, 4, FIL, 'médecine du travail : cotisation des employeurs par salarié (L. 4622-6 C. trav.), taxe sur la main-d’œuvre, reste fondue dans l’équilibre'),
    '136': (RNF, '', '', 4, FIL, 'quota d’investissement des fonds de capital-risque : amende (art. 1763 C CGI, « redevable d’une amende »), non un impôt'),
    '171': (RNF, '', '', 4, FIL, 'emballages : contribution versée à un éco-organisme privé contre la prise en charge des déchets, aucune recette publique'),
    '172': (RNF, '', '', 4, FIL, 'équarrissage : cotisation interprofessionnelle étendue, perçue par une interprofession privée, aucune recette publique'),
    '187': (COMPL, '', 'Fonds de garantie', 4, FIL, 'accidents du travail des exploitants agricoles : fonds adossé à une assurance obligatoire, restitué dans la réforme des régimes comme l’agriculture'),
    '188': (COMPL, '', 'Fonds de garantie', 4, FIL, 'fonds de garantie des dommages de soins (L. 426-1 C. assur.) : fonds adossé à une assurance obligatoire, le bloc s’étend à lui'),
    '189': (COMPL, '', 'Simili TVA', 4, FIL, 'contribution UNOCAM : même objet que la contribution des complémentaires santé (L. 862-4-1 CSS), elle la suit ; rang sans rendement propre'),
    '326': (RNF, '', '', 4, FIL, 'assurance-vie en déshérence : sommes acquises à l’État, non un impôt'),
    '339': (None, None, None, 4, FIL, 'droits d’enregistrement, ligne générique sans rendement propre : suit les droits de mutation, remplacés par la taxe foncière'),
    '363': (None, None, None, 4, FIL, 'droits de plaidoirie : un particulier, pour un acte — impôt sur le revenu (règle des six devenirs, qui nomme la plaidoirie)'),
    '382': (None, None, None, 4, FIL, 'redevance hydraulique : une entreprise, pour le domaine public — impôt sur les sociétés (règle des six devenirs) ; les redevances restent au tri'),
    '388': (None, None, None, 4, FIL, 'redevance des concessions hydroélectriques : même règle que la redevance hydraulique'),
    '417': (None, None, None, 4, FIL, 'garantie de l’or et de l’argent : une entreprise, pour son activité — impôt sur les sociétés (règle des six devenirs, qui la nomme)'),
    # règle 5 — un bloc pour le rang conservé en complément qui n'en avait pas
    '300': (None, None, 'Fiscalité outre-mer', 5, FIL, 'droits de place : rangés au poste « outre-mer » du tableau, avec l’octroi de mer ; le bloc suit le poste'),
}
# reclassements d'assiette et de nature validés le 20261020 (fragment archivé)
ASSIETTE = {'6': 'les revenus', '12': 'les revenus', '135': 'la propriété et les droits d’usage',
            '137': 'la propriété et les droits d’usage'}
NATURE = {'6': 'contribution sociale', '12': 'contribution sociale'}
QUALIF13 = ['128', '136', '171', '172', '187', '188', '189', '326', '339', '363', '382', '388', '417']
JEUX = ['280', '281', '282', '283', '284', '285', '286', '287', '289', '290']

# poste du tableau pour les seize rangs ajoutés le 20261103, absents de la version du 20 octobre (déduit, par analogie)
POSTE_N = {'N1': 'Taxe foncière', 'N2': 'Taxe foncière', 'N3': 'dont services de transports',
           'N4': 'Autres taxes sur les ménages', 'N5': 'Autres taxes sur les entreprises',
           'N6': 'dont alcool, tabac, jeux', 'N7': 'dont assurances', 'N8': 'Taxe foncière',
           'N9': "Taxes sur chiffre d'affaires et bénéfices"}

# ------------------------------------------------------------------ lecture du passage, poste par poste
LECTURE = {
    'TVA': 'Grand impôt conservé. Le tableau est en montants de 2024, le tri en prévision 2026.',
    'dont énergie*': 'Le tableau supprime 8 000. Le tri fond dans la TVA les trois lignes de la taxe sur '
                     'l’électricité, 5 153, et garde carburants et gaz. Reste 2 847 que le tableau supprime et '
                     'qu’aucun prélèvement du tri ne porte ; le montant du tableau est corrigé du bouclier tarifaire.',
    'dont alcool, tabac, jeux': 'Le tableau supprime 300. Le tri supprime les jeux en entier : 6 692 pour dix '
                                'prélèvements, 6 867 avec la contribution sur la publicité des jeux, créée en 2025. '
                                'Écart de 6 392 sur les dix prélèvements. Tabac et alcool gardés.',
    'dont assurances': 'Rien de supprimé au tableau, rien de supprimé au tri : concordant.',
    "dont redevances sur l'eau": 'Supprimé en entier des deux côtés. Écart de montant entre 2024 et 2026.',
    'dont services de transports': 'Supprimé en entier des deux côtés. Le tri y range 3 624, dont la taxe sur les '
                                   'billets d’avion (1 447), la taxe d’aéroport (1 192) et la taxe sur les autoroutes '
                                   '(776), pour 1 900 au tableau.',
    'dont véhicules': 'Supprimé en entier des deux côtés. Les 6 400 du tableau comprennent 3 300 de niches restituées, '
                      'que le tri ne compte pas.',
    'dont numérique, spectacles': 'Supprimé en entier des deux côtés. Écart de montant entre 2024 et 2026.',
    'dont autres taxes sur les produits': 'Supprimé en entier au tableau. Le tri supprime tout, dont la taxe sur les '
                                          'transactions financières (2 630), et garde la taxe sur les petits colis '
                                          '(400), créée en 2026, règle de l’Union européenne.',
    'dont taxe de séjour': 'Gardé au tableau. Le tri garde la taxe de séjour et fond dans l’équilibre les remontées '
                           'mécaniques et le ski de fond (90).',
    'dont taxe pollution': 'Supprimé en entier des deux côtés. Écart de montant entre 2024 et 2026.',
    'dont outre-mer': 'Gardé des deux côtés : concordant.',
    "Taxes sur la main d'œuvre": 'Le tableau supprime 48 000 et garde 8 800 de forfaits. Le tri fond dans l’équilibre '
                                 'les 32 prélèvements du poste, 42 646, dont les indemnités de rupture et de mise à la '
                                 'retraite (895). Écart de 5 354 ; sept prélèvements du poste sont sans rendement publié.',
    'dont forfaits de cotisation': 'Gardé des deux côtés : concordant.',
    'IR net': 'Grand impôt conservé, avec les retenues à la source. Le tri remplace par l’impôt sur le revenu les '
              'petites impositions du poste (3 081). La CSG et la CRDS, remplacées par l’impôt sur le revenu, sont '
              'hors tableau.',
    'IS net': 'Grand impôt conservé. Écart de montant entre 2024 et 2026.',
    "Taxes sur chiffre d'affaires et bénéfices": 'Supprimé en entier au tableau. Le tri supprime 16 416, dont la '
                                                 'contribution exceptionnelle sur les bénéfices des grandes entreprises '
                                                 '(7 300), créée en 2025, et garde la taxation minimale des '
                                                 'multinationales (500), règle de l’Union européenne.',
    'Taxe foncière': 'Grand impôt conservé ; son rendement n’est pas publié aux annexes du budget (impôt local), d’où '
                     'l’écart de montant. Le tri y fond 21 taxes locales et immobilières, 11 679, dont l’enlèvement '
                     'des ordures ménagères (5 859) et l’impôt sur la fortune immobilière (3 095) : elles rejoignent la '
                     'taxe foncière, que le tableau garde.',
    'Autres taxes sur les ménages': 'Supprimé en entier des deux côtés ; un prélèvement requalifié en recette non '
                                    'fiscale (36).',
    'Autres taxes sur les entreprises': 'Supprimé en entier au tableau. Le tri supprime tout, sauf deux fonds de '
                                        'garantie gardés (4) et deux contributions privées requalifiées, sans '
                                        'rendement publié. 19 prélèvements du poste sont sans rendement publié.',
    'Droits de mutation': 'Ligne de total du tableau : ses montants se lisent aux deux lignes suivantes. Cinq '
                          'prélèvements génériques y sont rangés, 478.',
    'à titre onéreux': 'Le tableau garde 5 050 et supprime 12 050. Le tri applique la même part gardée, au prorata : '
                       'droit ramené à 1 % et 3 %.',
    'à titre gratuit': 'Le tableau garde 6 000 et supprime 20 400, dont 5 600 de niches et de gisement, que le tri ne '
                       'compte pas. Le tri applique la même part gardée, au prorata.',
}
AGREGATS = {'Taxes sur la consommation*': 'Total des douze lignes de consommation qui suivent.'}


def f(x):
    return float(x) if x not in ('', None) else 0.0


def lire(p):
    with open(p, encoding='utf-8') as fh:
        return list(csv.DictReader(fh, delimiter='\t'))


def construire():
    base = lire(BASE)
    oct_ = {str(i): r for i, r in enumerate(lire(OCT), 1)}
    rows, mouv = [], []
    for r in base:
        n = r['n']
        d = dict(r)
        avant = (r['devenir'], r['impot_cible'], r['bloc'])
        # règle 1 — la colonne « poste du tableau »
        poste = oct_[n]['ligne_schema'] if n in oct_ else POSTE_N.get(n, '—')
        assert not n.isdigit() or oct_[n]['libelle'] == r['libelle'], n
        # règle 5 — « False » n'est pas une question
        if d['question'] == 'False':
            d['question'] = ''
        motif = statut = ''
        regle = ''
        if n in MOUV:
            dev, cible, bloc, regle, statut, motif = MOUV[n]
            if dev is not None:
                d['devenir'], d['impot_cible'] = dev, cible
            if bloc is not None:
                d['bloc'] = bloc
            if n in ASSIETTE:
                d['assiette'] = ASSIETTE[n]
            if n in NATURE:
                d['nature'] = NATURE[n]
            if n in QUALIF13:
                d['question'] = ''
            apres = (d['devenir'], d['impot_cible'], d['bloc'])
            if d['devenir'] != r['devenir']:
                # le porteur suit le devenir : un rang gardé n'a plus d'abrogation à porter, un rang supprimé en attend une
                ancien = r['amendement_porteur']
                if d['devenir'] in (COMPL, RNF):
                    d['amendement_porteur'] = d['alinea'] = ''
                    d['verdict'] = d['etat_porteur'] = SANS_OBJET
                    if ancien:
                        d['observation'] = (f'à retirer de l’amendement {ancien}' + (f', {r["alinea"]}' if r['alinea'] else '')
                                            + ' (tri unique du 20261116)' + (' ; ' + d['observation'] if d['observation'] else ''))
                    if d['devenir'] == RNF:
                        d['nature'] = d['nature_ligne'] = 'recette non fiscale'
                        d['assiette'] = ''
                else:
                    d['amendement_porteur'] = d['alinea'] = ''
                    d['verdict'], d['etat_porteur'] = 'C', 'non porté'
            mouv.append(dict(n=n, libelle=r['libelle'], rendement_2026_M=r['rendement_2026_M'],
                             devenir_avant=avant[0], cible_ou_bloc_avant=avant[1] or avant[2],
                             devenir_apres=apres[0], cible_ou_bloc_apres=apres[1] or apres[2],
                             change='devenir' if avant[0] != apres[0] else ('impôt cible ou bloc' if avant != apres else 'confirmé'),
                             regle=regle, statut=statut, motif=motif, porteur_avant=r['amendement_porteur']))
        # règle 2 — les jeux : supprimés, réponse de l'auteure du 20261116 (aucun déplacement, le tri du 3 novembre les supprimait)
        if n in JEUX:
            statut, regle = AUTEURE, 2
            motif = 'jeux supprimés : réponse de l’auteure du 20261116 (« oui on supprime, cf synthèse refonte »)'
        # règle 5 — le septième libellé devient une mention
        mention = ''
        if d['part_conservee_2026_M']:
            mention = 'droit ramené à 1 % et 3 %, part gardée'
        elif d['amendement_porteur'].startswith('voie réglementaire'):
            mention = 'supprimé par voie réglementaire'
        out = {}
        for k, v in d.items():
            out[k] = v
            if k == 'bloc':
                out['mention'] = mention
                out['poste_tableau'] = poste
        out['regle_20261116'] = regle
        out['statut_20261116'] = statut
        out['motif_20261116'] = motif
        rows.append(out)
    return base, rows, mouv


def comptes(rows):
    c = {d: [0, 0.0, 0] for d in DEVENIRS}
    for r in rows:
        x = c[r['devenir']]
        x[0] += 1
        x[1] += f(r['rendement_2026_M'])
        x[2] += r['rendement_2026_M'] == ''
    return c


def passage(rows):
    """Chaque poste du tableau face aux rangs du tri qui s'y rattachent. Montants en M€."""
    schema = lire(SCHEMA)
    par = defaultdict(list)
    for r in rows:
        par[r['poste_tableau']].append(r)
    out = []
    for s in schema:
        p = s['poste']
        if p == 'Total':
            continue
        rs = par.get(p, [])
        tot = sum(f(r['rendement_2026_M']) for r in rs)
        sup = sum(f(r['rendement_2026_M']) - f(r['part_conservee_2026_M']) for r in rs if r['devenir'] in (REMPL, FONDU))
        autres = sum(f(r['rendement_2026_M']) for r in rs if r['devenir'] in (FUSION, RNF))
        c = f(s['montant_2024']) * 1000
        h = -f(s['taxes_a_supprimer']) * 1000
        agg = p in AGREGATS
        out.append(dict(poste=p, montant_2024_M=round(c, 1), a_supprimer_2024_M=round(h, 1),
                        rangs='' if agg else len(rs), sans_rendement='' if agg else sum(1 for r in rs if r['rendement_2026_M'] == ''),
                        rendement_2026_M='' if agg else round(tot, 1),
                        supprime_2026_M='' if agg else round(sup, 1),
                        garde_2026_M='' if agg else round(tot - sup - autres, 1),
                        ecart_montant_M='' if agg else round(tot - c, 1),
                        ecart_supprime_M='' if agg else round(sup - h, 1),
                        lecture=AGREGATS.get(p) or LECTURE[p]))
    hors = par.get('—', [])
    for dev in DEVENIRS:
        rs = [r for r in hors if r['devenir'] == dev]
        if not rs:
            continue
        tot = sum(f(r['rendement_2026_M']) for r in rs)
        sup = tot if dev in (REMPL, FONDU) else 0.0
        out.append(dict(poste=f'hors tableau — {dev}', montant_2024_M='', a_supprimer_2024_M='', rangs=len(rs),
                        sans_rendement=sum(1 for r in rs if r['rendement_2026_M'] == ''),
                        rendement_2026_M=round(tot, 1), supprime_2026_M=round(sup, 1),
                        garde_2026_M=round(tot - sup, 1) if dev in (GRAND, COMPL) else 0.0,
                        ecart_montant_M='', ecart_supprime_M='',
                        lecture='Le tableau détaille les impôts et taxes des comptes nationaux ; ces prélèvements n’y ont '
                                'pas de ligne propre.'))
    return out


def ecrire(p, lignes):
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(lignes[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(lignes)


def main():
    base, rows, mouv = construire()
    pas = passage(rows)
    ko = []
    if len(rows) != 434:
        ko.append(f'{len(rows)} rangs au lieu de 434')
    if set(r['devenir'] for r in rows) != set(DEVENIRS):
        ko.append('les devenirs ne sont pas les six de la règle')
    sans_bloc = [r['n'] for r in rows if r['devenir'] == COMPL and r['bloc'] not in BLOCS]
    if sans_bloc:
        ko.append(f'conservé en complément sans bloc : {sans_bloc}')
    if any(r['question'] == 'False' for r in rows):
        ko.append('« False » en colonne question')
    sans_cible = [r['n'] for r in rows if r['devenir'] == REMPL and not r['impot_cible']]
    if sans_cible:
        ko.append(f'remplacé sans impôt cible : {sans_cible}')
    # millésime : aucun rendement de la base n'est touché
    if any(a['rendement_2026_M'] != b['rendement_2026_M'] for a, b in zip(base, rows)):
        ko.append('un rendement a changé')
    ecrire(SORTIE, rows)
    ecrire(OUT / 'rangs_deplaces_20261116.tsv', mouv)
    ecrire(OUT / 'passage_tableau_20261116.tsv', pas)

    for nom, t in (('avant (20261103)', base), ('après (20261116)', rows)):
        c = comptes(t)
        print(f'\n{nom} — {len(t)} rangs, {sum(v[1] for v in c.values()):.1f} M€, {sum(v[2] for v in c.values())} sans rendement')
        for d in DEVENIRS:
            print(f'  {d:<48} {c[d][0]:>4} {c[d][1]:>10.1f} {c[d][2]:>4}')
    ch = Counter(m['change'] for m in mouv)
    print(f'\nrangs touchés : {len(mouv)} — {dict(ch)}')
    print('jeux :', len(JEUX), 'rangs,', round(sum(f(r['rendement_2026_M']) for r in rows if r['n'] in JEUX), 1), 'M€')
    print('blocs :', dict(Counter(r['bloc'] for r in rows if r['devenir'] == COMPL)))
    print('mentions :', dict(Counter(r['mention'] for r in rows if r['mention'])))
    print('rangs supprimés sans porteur :', sum(1 for r in rows if r['etat_porteur'] == 'non porté'),
          round(sum(f(r['rendement_2026_M']) for r in rows if r['etat_porteur'] == 'non porté'), 1), 'M€')
    if ko:
        print('\nÉCHEC :', ' ; '.join(ko))
        return 1
    print('\n0 échec : 434 rangs, six devenirs, un bloc par rang conservé en complément.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
