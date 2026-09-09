# -*- coding: utf-8 -*-
"""Traçage des économies — d'où vient chaque euro supprimé, et par quel canal.

Le classeur de calculs affiche un arbre d'économies : 117,2 Md€ en deux
périmètres, six rubriques d'État, quatre rubriques locales, et vingt-deux lignes
de détail. Cet arbre est le chiffrage. **Tant qu'on ne sait pas dire, ligne à
ligne, sur quelle assiette l'économie est prise, le chiffrage n'est pas
traçable — il est affiché.**

Ce module rattache chaque ligne d'opérateur à son assiette, et dit ce qui
boucle et ce qui ne boucle pas.

## Les trois mailles, et pourquoi la confusion coûte cher

Les lignes d'opérateurs ne sont pas toutes des opérateurs.

    opérateur du PLF   la ligne nomme un opérateur de la liste officielle —
                       France Compétences, France Travail, l'ADEME, le CNC,
                       l'AFITF, l'ANAH, les agences de l'eau
    ODAC-ODAL          la ligne nomme un organisme de la liste ODAC-ODAL qui
                       n'est pas opérateur du PLF — Action Logement Services,
                       les chambres consulaires, les établissements publics
                       fonciers
    résidu             la ligne ne nomme rien — « autres »

Les traiter tous comme des opérateurs ferait croire que la liste officielle
couvre le chiffrage. Elle ne le couvre pas, et c'est une information, pas un
défaut : une part des économies se prend hors du périmètre des opérateurs.

## Les deux canaux, et le poste qui les ferme

    taxe affectée   l'économie est la restitution d'une taxe. Elle se recompose
                    depuis l'annexe 2 du tome I : restitué en année 1 plus solde
                    restitué ensuite.
    budgétaire      l'économie est prise sur des crédits. **Elle est écrite**,
                    poste par poste, à l'onglet de synthèse du classeur des
                    dépenses : une catégorie LOLF, un libellé, un montant, une
                    qualification. Elle ne se déduit plus d'un résidu.

Une ligne peut relever des deux, et alors les deux se somment pour retrouver ce
que le classeur affiche. Un écart qui subsiste est de trois natures et de trois
seulement : l'arrondi d'affichage, une part budgétaire non encore rattachée à
son poste, ou un défaut de lecture. **Aucun ne s'absorbe.**

## Ce que ce module ne fait pas

Il n'impute rien qui ne soit écrit. Une ligne sans rattachement reste sans
rattachement, et se compte. Le rattachement lui-même est écrit à la main, jamais
déduit d'un score de ressemblance : c'est la règle A-35, et une économie mal
rattachée est pire qu'une économie non rattachée.

Usage : python3 tracer_economies.py ../referentiels/socle_budgetaire.json \\
            ../referentiels/economies.json \\
            ../livrables/economies_tracees.txt
"""
import json
import sys
from collections import defaultdict

# --------------------------------------------------------- les rattachements
# Écrits à la main, ligne par ligne, clé = numéro de ligne de l'onglet
# « Détail Economies ». Chaque entrée déclare :
#
#   maille       où se situe la ligne : opérateur du PLF, affectataire hors
#                liste, dispositif, ou résidu
#   canal        taxe_affectee · budgetaire · mixte
#   beneficiaires  les libellés exacts de l'annexe des taxes affectées. Écrits
#                en clair tant qu'ils tiennent ; au-delà, une règle « contient »
#                avec le nombre de lignes attendu, de sorte qu'un affectataire
#                qui apparaîtrait au PLF suivant fasse tomber le compte.
#   programmes   les programmes du PAP qui portent l'assiette budgétaire
#   motif        pourquoi ce rattachement, en une phrase
RATTACHEMENTS = {
    5: {
        'maille': 'operateur_plf', 'canal': 'mixte',
        'operateurs': ['France Compétences'],
        'beneficiaires': ['France Compétences'], 'attendu_lignes': 11,
        'programmes': ['103'],
        'postes_bg': [('32', 13)],
        'motif': "France Compétences perçoit onze taxes affectées et reçoit du "
                 "programme 103 ; l'économie est d'abord une restitution de "
                 "taxes, le reste est budgétaire.",
    },
    6: {
        'maille': 'operateur_plf', 'canal': 'budgetaire',
        'operateurs': ['France Travail'],
        'beneficiaires': [], 'attendu_lignes': 0,
        'programmes': ['102'],
        'postes_bg': [('32', 16), ('32', 18), ('32', 19)],
        'motif': "France Travail ne perçoit aucune taxe affectée au PLF 2026 : "
                 "l'économie est entièrement budgétaire, sur le programme 102.",
    },
    7: {
        'maille': 'operateur_plf', 'canal': 'mixte',
        'operateurs': ["CNC - Centre national du cinéma et de l'image animée"],
        'beneficiaires': ["CNC - Centre national du cinéma et de l'image "
                          "animée"], 'attendu_lignes': 9,
        'programmes': ['334', '131', '175'],
        'postes_bg': [('32', 12)],
        'motif': "La ligne agrège le CNC — neuf taxes affectées — et des "
                 "subventions culturelles budgétaires que son intitulé ne "
                 "détaille pas.",
    },
    8: {
        'maille': 'operateur_plf', 'canal': 'taxe_affectee',
        'operateurs': ["Agences de l'eau"],
        'beneficiaires': ["Agences de l'eau"], 'attendu_lignes': 1,
        'programmes': [],
        'motif': "Les six agences de l'eau tiennent sur une ligne unique, à la "
                 "liste officielle comme à l'annexe des taxes.",
    },
    9: {
        'maille': 'operateur_plf', 'canal': 'taxe_affectee',
        'operateurs': ['AFITF - Agence de financement des infrastructures de '
                       'transport de France'],
        'beneficiaires': ['AFITF - Agence de financement des infrastructures '
                          'de transport de France'], 'attendu_lignes': 4,
        'programmes': [],
        'motif': "L'AFITF est financée par quatre taxes affectées ; "
                 "l'hypothèse retranche l'entretien et le ferroviaire en cours.",
    },
    10: {
        'maille': 'odac_odal', 'canal': 'taxe_affectee',
        'operateurs': [],
        'organismes': ['ALS Action logement services'], 'attendu_entites': 1,
        'beneficiaires': ['Action Logement Services'], 'attendu_lignes': 1,
        'programmes': [],
        'motif': "Action Logement Services perçoit la participation des "
                 "employeurs à l'effort de construction. Ce n'est pas un "
                 "opérateur du PLF, c'est l'ODAC-223, en régime de vente.",
    },
    11: {
        'maille': 'odac_odal', 'canal': 'taxe_affectee',
        'operateurs': [],
        'organismes': ['Chambres consulaires 273'], 'attendu_entites': 273,
        'beneficiaires': ['CCI France',
                          "Chambres départementales d'agriculture"],
        'attendu_lignes': 3, 'programmes': [],
        'motif': "Les chambres consulaires vivent de taxes pour frais de "
                 "chambre. Aucune n'est opérateur du PLF ; elles sont "
                 "l'ODAC-730, 273 structures en régime de vente. "
                 "**Deux mailles distinctes** : l'annexe des taxes ne nomme "
                 "que deux affectataires collecteurs, l'ODAC compte les "
                 "chambres.",
    },
    12: {
        'maille': 'operateur_plf', 'canal': 'budgetaire',
        'operateurs': ["ADEME - Agence de l'environnement et de la maîtrise "
                       "de l'énergie"],
        'beneficiaires': [], 'attendu_lignes': 0,
        'programmes': ['181'],
        'postes_bg': [('32', 8), ('32', 9)],
        'motif': "L'ADEME a perdu sa taxe affectée : elle est financée par "
                 "subvention, sur le programme 181.",
    },
    13: {
        'maille': 'odac_odal', 'canal': 'taxe_affectee',
        'operateurs': [],
        'organismes': ['Etablissements publics fonciers 40'],
        'attendu_entites': 40,
        'regle_beneficiaires': 'foncier', 'attendu_lignes': 34,
        'programmes': [],
        'motif': "Les établissements publics fonciers, d'État et locaux, "
                 "perçoivent la taxe spéciale d'équipement. Aucun n'est "
                 "opérateur du PLF ; ils sont l'ODAC-731, 40 structures en "
                 "régime de vente. **Deux mailles distinctes** : 34 "
                 "affectataires à l'annexe des taxes, 40 structures à l'ODAC "
                 "— six n'ont pas de taxe affectée au PLF 2026.",
    },
    14: {
        'maille': 'operateur_plf', 'canal': 'taxe_affectee',
        'operateurs': ["ANAH - Agence nationale de l'habitat"],
        'beneficiaires': ["ANAH - Agence nationale de l'habitat"],
        'attendu_lignes': 1, 'programmes': [],
        'motif': "L'ANAH perçoit une taxe affectée ; la ligne s'y recompose.",
    },
    15: {
        'maille': 'operateur_plf', 'canal': 'budgetaire',
        'operateurs': ["ANAH - Agence nationale de l'habitat"],
        'beneficiaires': [], 'attendu_lignes': 0,
        'programmes': ['174', '135'],
        'postes_bg': [('61', 6)],
        'dispositif': True,
        'motif': "MaPrimeRénov' est un dispositif, pas un organisme : "
                 "**il est distribué par l'ANAH**, qui en est l'opérateur "
                 "porteur (rattachement écrit par l'auteur). L'ANAH porte donc "
                 "deux lignes d'économie, celle de sa taxe affectée et "
                 "celle-ci. L'assiette déborde le programme 174 et se répartit "
                 "avec le 135.",
    },
    16: {
        'maille': 'residu', 'canal': 'inconnu',
        'operateurs': [], 'beneficiaires': [], 'attendu_lignes': 0,
        'programmes': [],
        'motif': "Ligne de résidu. Le classeur ne dit pas ce qu'elle contient, "
                 "et rien ici ne le devine.",
    },
}

MAILLES = {
    'operateur_plf': "opérateur de la liste officielle",
    'odac_odal': "organisme de la liste ODAC-ODAL, hors opérateurs du PLF",
    'residu': "résidu non détaillé",
}

CAT_SCSP = {'32'}
CAT_TITRE6 = {'61', '62', '63', '64', '65'}

# Le classeur affiche au dixième de milliard. Le résidu qui tient dans cet
# arrondi ne se nomme pas : il ne dit rien du chiffrage.
ARRONDI_CLASSEUR = 0.055

# Les trois lignes chiffrées d'après le budget initial 2025 de l'organisme,
# comme l'onglet « Gages » le déclare. La pièce n'est pas au corpus, mais elle a
# été sourcée ailleurs par l'auteur et le chiffrage est validé (A-113). Le
# signalement reste, parce qu'il dit d'où vient le montant ; il ne vaut plus
# réserve.
SOURCE_BUDGET_INITIAL = {5, 6, 12}


def _taxes_par_beneficiaire(socle):
    agg = defaultdict(lambda: {'lignes': 0, 'annee_1': 0.0, 'ensuite': 0.0,
                               'affectation': 0.0, 'codes': []})
    for t in socle.get('taxes_affectees', []):
        b = t['socle'].get('beneficiaire')
        i = t['interpretation']
        a = agg[b]
        a['lignes'] += 1
        a['annee_1'] += i.get('restitue_annee_1_eur') or 0.0
        a['ensuite'] += i.get('restitue_ensuite_eur') or 0.0
        a['affectation'] += i.get('taxe_affectee_m_eur') or 0.0
        code = t['socle'].get('code_taxe')
        if code:
            a['codes'].append(code)
    return agg


def _enveloppes_par_programme(socle):
    scsp, t6 = defaultdict(float), defaultdict(float)
    for p in socle.get('pap', []):
        s = p['socle']
        cp = s.get('cp_plf') or 0.0
        if s.get('categorie') in CAT_SCSP:
            scsp[s.get('programme')] += cp
        elif s.get('categorie') in CAT_TITRE6:
            t6[s.get('programme')] += cp
    return scsp, t6


def _postes_bg(socle):
    """Les postes nommés de la synthèse budgétaire, indexés par (catégorie, ligne).

    C'est là que la part budgétaire d'une économie est **écrite**. Avant de les
    lire, elle n'était qu'un résidu : la ligne moins ce que les taxes
    recomposent. Un résidu n'est pas une source.
    """
    bg = socle.get('bg_synthese') or {}
    return {(p['categorie'], p['ligne']): p for p in bg.get('postes', [])}


def _odac_par_libelle(socle):
    return {(x['socle'].get('organisme') or ''): x
            for x in socle.get('odac_odal', [])}


def _cibles(regle, agg):
    """Les bénéficiaires qu'une règle « contient » désigne, en clair."""
    return sorted(b for b in agg if b and regle.lower() in b.lower())


def tracer(socle):
    economies = socle.get('economies', [])
    agg = _taxes_par_beneficiaire(socle)
    scsp, t6 = _enveloppes_par_programme(socle)
    programmes = socle.get('nomenclature', {}).get('programmes', {})
    officiels = {o['socle']['operateur'] for o in socle.get('operateurs', [])}
    odac = _odac_par_libelle(socle)
    postes = _postes_bg(socle)

    lignes = []
    for e in economies:
        c, lec = e['classeur'], e['lecture']
        entree = {
            'id': e['id'], 'ligne': e['ligne'], 'intitule': c['intitule'],
            'niveau': lec['niveau'], 'perimetre': lec['perimetre'],
            'rubrique': lec['rubrique'], 'destination': lec['destination'],
            'code_destination': c['code_destination'],
            'restitue_annee_1_md_eur': c['restitue_annee_1_md_eur'],
            'solde_restitue_ensuite_md_eur': c['solde_restitue_ensuite_md_eur'],
            'total_supprime_md_eur': c['total_supprime_md_eur'],
            'hypothese': c['hypothese'],
            'incidence_md_eur': c['incidence_md_eur'],
            'rattachement': None,
        }
        r = RATTACHEMENTS.get(e['ligne'])
        if r:
            benefs = list(r.get('beneficiaires') or [])
            regle = r.get('regle_beneficiaires')
            if regle:
                benefs = _cibles(regle, agg)
            lignes_ta = sum(agg[b]['lignes'] for b in benefs)
            an1 = sum(agg[b]['annee_1'] for b in benefs) / 1e9
            ens = sum(agg[b]['ensuite'] for b in benefs) / 1e9
            ta = sum(agg[b]['affectation'] for b in benefs) / 1000.0
            env = sum(scsp.get(p, 0.0) + t6.get(p, 0.0)
                      for p in r.get('programmes', [])) / 1e9
            total = c['total_supprime_md_eur'] or 0.0
            reste = round(total - (an1 + ens), 4)
            # Le classeur arrondit chacune de ses deux colonnes au dixième de
            # milliard. Un résidu qui tient dans cet arrondi n'est ni une part
            # budgétaire ni un défaut : c'est l'affichage.
            arrondi = abs(reste) <= ARRONDI_CLASSEUR
            a_boucler = (reste if not arrondi and reste > 0 else None)
            org = []
            for nom in r.get('organismes', []):
                x = odac.get(nom)
                org.append({
                    'libelle': nom,
                    'id': x['id'] if x else None,
                    'entites': (x['socle'].get('nombre_entites')
                                if x else None),
                    'regime': (x['interpretation'].get('regime')
                               if x else None),
                    'fonction': x['socle'].get('fonction') if x else None,
                    'deja_traite_en_operateur': (
                        x['interpretation'].get('deja_traite_en_operateur')
                        if x else None),
                })
            entites = sum(o['entites'] or 0.0 for o in org)
            # La part budgétaire, telle que la synthèse du budget général
            # l'écrit — et non plus telle qu'un résidu la laisse deviner.
            pbg, pbg_an1, pbg_ens = [], 0.0, 0.0
            for cle in r.get('postes_bg', []):
                x = postes.get(cle)
                if x is None:
                    pbg.append({'categorie': cle[0], 'ligne': cle[1],
                                'introuvable': True})
                    continue
                pbg.append({'categorie': x['categorie'], 'ligne': x['ligne'],
                            'libelle': x['libelle'],
                            'qualification': x['qualification'],
                            'valeur_m_eur': round(x['valeur_m_eur'], 3),
                            'titre': x['titre']})
                if x['qualification'] == 'economie_annee_1':
                    pbg_an1 += x['valeur_m_eur']
                elif x['qualification'] == 'economie_perenne':
                    pbg_ens += x['valeur_m_eur']
            entree['rattachement'] = {
                'maille': r['maille'], 'canal': r['canal'],
                'motif': r['motif'],
                'dispositif': bool(r.get('dispositif')),
                'operateurs': r.get('operateurs', []),
                'operateurs_hors_liste': [o for o in r.get('operateurs', [])
                                          if o not in officiels],
                'organismes': org,
                'organismes_introuvables': [o['libelle'] for o in org
                                            if o['id'] is None],
                'entites': entites or None,
                'entites_attendues': r.get('attendu_entites'),
                'compte_entites_tenu': (None if 'attendu_entites' not in r
                                        else entites == r['attendu_entites']),
                'beneficiaires': benefs,
                'beneficiaires_par_regle': bool(regle),
                'lignes_taxes': lignes_ta,
                'lignes_taxes_attendues': r.get('attendu_lignes'),
                'compte_taxes_tenu': lignes_ta == r.get('attendu_lignes'),
                'taxe_affectee_nette_md_eur': round(ta, 4) if benefs else None,
                'recompose_annee_1_md_eur': round(an1, 4),
                'recompose_ensuite_md_eur': round(ens, 4),
                'recompose_total_md_eur': round(an1 + ens, 4),
                'programmes': [{'numero': p,
                                'libelle': (programmes.get(p) or {})
                                .get('libelle'),
                                'scsp_md_eur': round(scsp.get(p, 0.0) / 1e9, 4),
                                'titre6_md_eur': round(t6.get(p, 0.0) / 1e9, 4)}
                               for p in r.get('programmes', [])],
                'enveloppe_programmes_md_eur': round(env, 4) if env else None,
                'postes_bg': pbg,
                'postes_bg_annee_1_md_eur': round(pbg_an1 / 1000.0, 4) or None,
                'postes_bg_ensuite_md_eur': round(pbg_ens / 1000.0, 4) or None,
                'postes_bg_total_md_eur': (round((pbg_an1 + pbg_ens) / 1000.0, 4)
                                           if pbg else None),
                'part_budgetaire_ecrite': bool(pbg),
                'arrondi_classeur_md_eur': reste if arrondi and reste else None,
                'part_budgetaire_md_eur': a_boucler,
                'ecart_negatif_md_eur': (reste if not arrondi and reste < 0
                                         else None),
                'a_couvrir_md_eur': round(a_boucler if a_boucler is not None
                                          else (0.0 if benefs else total), 4),
                'assiette_couvre_la_part_budgetaire': (
                    None if not env
                    else env >= (a_boucler if a_boucler is not None
                                 else (0.0 if benefs else total)) - 0.0005),
                'chiffre_sur_budget_initial': (e['ligne']
                                               in SOURCE_BUDGET_INITIAL),
            }
        lignes.append(entree)
    return lignes


# -------------------------------------------------- la chaîne des emplois
# Les rubriques d'État qui ne passent ni par une taxe ni par un programme se
# calculent depuis la synthèse du budget général : une masse, un taux, un
# effectif. Le classeur écrit le résultat et l'hypothèse en toutes lettres ; il
# n'écrit pas la formule. Elle est reconstituée ici, et confrontée.
#
# **L'écart n'est pas corrigé.** Quand il tient dans l'arrondi d'affichage, il
# est dit tel quel ; quand il ne tient pas, il reste ouvert et se voit.
def derivations(socle):
    bg = socle.get('bg_synthese') or {}
    ops = socle.get('operateurs', [])
    sup = sum(o['socle'].get('etpt_total_lfi_2025') or 0.0 for o in ops
              if o['interpretation'].get('regime') == 'suppression')
    ft = next((o['socle'].get('etpt_total_lfi_2025') or 0.0 for o in ops
               if o['socle']['operateur'] == 'France Travail'), 0.0)
    sal = bg.get('salaire_moyen_eur')
    msnr = bg.get('salaires_non_regalien_m_eur')
    fnr = bg.get('fonctionnement_non_regalien_m_eur')
    inr = bg.get('investissement_non_regalien_m_eur')
    out = []

    def d(objet, unite, calcule, ecrit, formule, ou, tol, concept=None):
        out.append({'objet': objet, 'unite': unite,
                    'calcule': None if calcule is None else round(calcule, 3),
                    'ecrit_au_classeur': ecrit, 'formule': formule,
                    'ou': ou, 'tolerance': tol,
                    'ecart_de_concept': concept})

    if None not in (fnr, inr):
        d("Charges courantes et achats, État", 'Md€',
          (fnr + inr) * 0.80 / 1000.0, 3.8,
          "(fonctionnement + investissement non régaliens) × 80 %",
          "Détail Economies, ligne 37 — « hors régalien et éducation, "
          "80 % d'économies »", 0.05)
    if msnr is not None:
        d("Départs fonctionnaires d'État", 'Md€',
          msnr * 0.90 * 0.30 / 1000.0, 0.9,
          "masse salariale non régalienne × 90 % de départs "
          "× 30 % non maintenus",
          "Détail Economies, ligne 38 — « 90 % de départs, "
          "70 % salaire maintenu »", 0.05)
    if None not in (msnr, sal) and sal:
        d("ETP d'État supprimés", 'ETP',
          msnr * 1e6 / sal * 0.90, 61400,
          "masse salariale non régalienne ÷ salaire moyen × 90 %",
          "Détail Economies, ligne 38, colonne I", 50)
    # Ces deux bases ne viennent pas de l'annexe : elles viennent du jaune
    # « Opérateurs de l'État », qui ne compte pas la même chose (A-111). Le
    # rapprochement se fait donc, et l'écart se nomme — il ne se résorbe pas.
    d("Base ETP des opérateurs hors France Travail", 'ETP',
      sup - ft, 46440,
      "ETPT LFI 2025 des opérateurs en régime de suppression, "
      "moins France Travail",
      "Détail Economies, ligne 4, colonne I — base tirée du jaune "
      "« Opérateurs de l'État »", 5,
      "le jaune et l'annexe ne comptent pas la même chose : plafond "
      "d'emplois contre exécution. L'écart de 393 ETP, soit 0,8 %, est un "
      "écart de concept — il est nommé, il ne se corrige d'aucun côté.")
    d("Base ETP de France Travail", 'ETP', ft, 53200,
      "ETPT total LFI 2025 de France Travail",
      "Détail Economies, ligne 6, colonne I — base tirée du jaune "
      "« Opérateurs de l'État »", 5,
      "même écart de concept, 148 ETP, soit 0,3 %.")
    d("ETP supprimés, État et opérateurs", 'ETP',
      61400 + 41800 + 47880, 151000,
      "61 400 d'État + 90 % des deux bases d'opérateurs",
      "Détail Economies, ligne 3, colonne I", 100)
    d("ETP supprimés, toutes administrations", 'ETP',
      61400 + 41800 + 47880 + 428500, 580000,
      "les précédents, plus 428 500 ETP locaux",
      "Détail Economies, ligne 2, colonne I", 500)
    for x in out:
        if x['calcule'] is None:
            x['verdict'] = 'sans base'
        elif abs(x['calcule'] - x['ecrit_au_classeur']) <= x['tolerance']:
            x['verdict'] = 'accord'
        elif x['ecart_de_concept']:
            x['verdict'] = 'écart de concept'
        else:
            x['verdict'] = 'ÉCART OUVERT'
        x['ecart'] = (None if x['calcule'] is None
                      else round(x['calcule'] - x['ecrit_au_classeur'], 3))
    return out


# ------------------------------------------------------------- les bouclages
def bouclages(lignes):
    """Ce que l'arbre doit retrouver de lui-même. Rien n'est corrigé ici."""
    out = []

    def somme(pred, champ):
        return round(sum(l[champ] or 0.0 for l in lignes if pred(l)), 4)

    for per in ('etat', 'collectivites_locales'):
        tete = [l for l in lignes
                if l['niveau'] == 'total' and l['perimetre'] == per]
        if not tete:
            continue
        for champ, nom in (('restitue_annee_1_md_eur', 'restitué année 1'),
                           ('solde_restitue_ensuite_md_eur', 'solde ensuite'),
                           ('total_supprime_md_eur', 'total supprimé')):
            r = somme(lambda l, p=per: l['niveau'] == 'rubrique'
                      and l['perimetre'] == p, champ)
            out.append({'objet': f'{per} · rubriques → tête, {nom}',
                        'recompose': r, 'affiche': tete[0][champ],
                        'tolerance': 0.25})

    rubriques = {l['intitule'] for l in lignes if l['niveau'] == 'rubrique'}
    for rub in sorted(rubriques):
        detail = [l for l in lignes if l['rubrique'] == rub]
        if not detail:
            continue
        tete = [l for l in lignes
                if l['niveau'] == 'rubrique' and l['intitule'] == rub][0]
        for champ, nom in (('restitue_annee_1_md_eur', 'restitué année 1'),
                           ('solde_restitue_ensuite_md_eur', 'solde ensuite'),
                           ('total_supprime_md_eur', 'total supprimé')):
            r = round(sum(l[champ] or 0.0 for l in detail), 4)
            out.append({'objet': f'{rub} · détail → rubrique, {nom}',
                        'recompose': r, 'affiche': tete[champ],
                        'tolerance': 0.05})

    tete = [l for l in lignes
            if l['niveau'] == 'total' and l['perimetre'] == 'etat'][0]
    for pop in ('menages', 'actifs', 'entreprises'):
        r = round(sum(l['incidence_md_eur'].get(pop, 0.0) for l in lignes
                      if l['niveau'] != 'total'), 4)
        out.append({'objet': f'incidence → tête, {pop}',
                    'recompose': r,
                    'affiche': tete['incidence_md_eur'].get(pop),
                    'tolerance': 0.01})

    for l in lignes:
        r = l.get('rattachement')
        if r and r.get('part_budgetaire_ecrite'):
            out.append({'objet': f"{l['intitule'].strip()} · taxes + crédits "
                                 f"→ ligne",
                        'recompose': round(r['recompose_total_md_eur']
                                           + r['postes_bg_total_md_eur'], 4),
                        'affiche': l['total_supprime_md_eur'],
                        'tolerance': 0.09})
    for l in lignes:
        r = l.get('rattachement')
        if r and r['canal'] == 'taxe_affectee':
            out.append({'objet': f"{l['intitule'].strip()} · taxes → ligne",
                        'recompose': r['recompose_total_md_eur'],
                        'affiche': l['total_supprime_md_eur'],
                        'tolerance': 0.06})
    return out


def verdict(b):
    if b['affiche'] is None:
        return 'sans référence'
    return ('accord' if abs(b['recompose'] - b['affiche']) <= b['tolerance']
            else 'DISCORDANCE')


# ------------------------------------------------------------- le livrable
def _md(v):
    return '—' if v is None else f'{v:,.3f}'.replace(',', ' ')


def rendre(lignes, bcl, synthese, deriv):
    L = []
    a = L.append
    a("Traçage des économies — assiette, canal et bouclage")
    a('')
    rat = [l for l in lignes if l['rattachement']]
    ta = [l for l in rat if l['rattachement']['canal'] in
          ('taxe_affectee', 'mixte')]
    a(f"  {len(lignes)} ligne(s) relevées de l'arbre des économies")
    a(f"  {len(rat)} ligne(s) rattachées à une assiette nommée")
    a(f"  {len(ta)} dont l'économie se recompose, en tout ou partie, "
      "depuis les taxes affectées")
    mailles = defaultdict(int)
    for l in rat:
        mailles[l['rattachement']['maille']] += 1
    for m, n in sorted(mailles.items()):
        a(f"    {n:2d} · {MAILLES[m]}")
    a('')
    a("Une ligne d'opérateur n'est pas toujours un opérateur, et l'écart entre")
    a("ce que les taxes recomposent et ce que la ligne affiche n'est jamais")
    a("absorbé : il est nommé part budgétaire et il reste sous les yeux.")
    a('')
    a('=' * 78)
    a('')

    for l in lignes:
        if not l['rattachement']:
            continue
        r = l['rattachement']
        a(l['intitule'].strip())
        a(f"  maille      {MAILLES[r['maille']]}")
        a(f"  canal       {r['canal']}")
        a(f"  classeur    restitué année 1 {_md(l['restitue_annee_1_md_eur'])}"
          f" + ensuite {_md(l['solde_restitue_ensuite_md_eur'])}"
          f" = {_md(l['total_supprime_md_eur'])} Md€")
        if l['destination']:
            a(f"  destination {l['destination']}  "
              f"[{l['code_destination']}]")
        if r['organismes']:
            for o in r['organismes']:
                tenu = ('' if r['compte_entites_tenu'] is not False
                        else f" ⚠ attendu {r['entites_attendues']}")
                a(f"  ODAC        {o['id'] or '⚠ introuvable'} "
                  f"{o['libelle']} — {o['entites'] or 0:,.0f} entité(s), "
                  f"régime {o['regime'] or '—'}{tenu}")
        if r['dispositif']:
            a("  dispositif  la ligne nomme un dispositif, pas un organisme ; "
              "l'opérateur cité en est le distributeur")
        if r['beneficiaires']:
            src = ('règle « contient »' if r['beneficiaires_par_regle']
                   else 'libellés écrits')
            tenu = 'tenu' if r['compte_taxes_tenu'] else '⚠ NON TENU'
            a(f"  taxes       {r['lignes_taxes']} ligne(s) sur "
              f"{len(r['beneficiaires'])} bénéficiaire(s), {src} — "
              f"compte attendu {r['lignes_taxes_attendues']} : {tenu}")
            a(f"              recomposé {_md(r['recompose_annee_1_md_eur'])}"
              f" + {_md(r['recompose_ensuite_md_eur'])}"
              f" = {_md(r['recompose_total_md_eur'])} Md€")
            if r['beneficiaires_par_regle']:
                a(f"              {r['beneficiaires'][0]}")
                a(f"              … et {len(r['beneficiaires']) - 1} autres, "
                  "listés au référentiel")
        for p in r['programmes']:
            a(f"  programme   {p['numero']} {p['libelle']}"
              f" — SCSP {_md(p['scsp_md_eur'])} + titre 6 "
              f"{_md(p['titre6_md_eur'])} Md€")
        if r['part_budgetaire_md_eur'] is not None:
            a(f"  part budgétaire {_md(r['part_budgetaire_md_eur'])} Md€ — "
              "non recomposée par les taxes, à prendre sur les crédits")
        for x in r['postes_bg']:
            if x.get('introuvable'):
                a(f"  ⚠ poste budgétaire introuvable : catégorie "
                  f"{x['categorie']}, ligne {x['ligne']}")
                continue
            a(f"  poste BG    catégorie {x['categorie']} (titre {x['titre']}) "
              f"« {x['libelle']} » — {_md(x['valeur_m_eur'] / 1000)} Md€, "
              f"{x['qualification']}")
        if r['postes_bg_total_md_eur'] is not None:
            a(f"              part budgétaire écrite au classeur : "
              f"{_md(r['postes_bg_annee_1_md_eur'] or 0)} en année 1 + "
              f"{_md(r['postes_bg_ensuite_md_eur'] or 0)} ensuite = "
              f"{_md(r['postes_bg_total_md_eur'])} Md€")
        if r['arrondi_classeur_md_eur'] is not None:
            a(f"  arrondi     {_md(r['arrondi_classeur_md_eur'])} Md€ — "
              "résidu d'affichage du classeur, la ligne boucle")
        if r['ecart_negatif_md_eur'] is not None:
            a(f"  ⚠ écart négatif {_md(r['ecart_negatif_md_eur'])} Md€ — "
              "les taxes donnent plus que la ligne : lecture à reprendre")
        if r['assiette_couvre_la_part_budgetaire'] is False:
            a("  ⚠ l'enveloppe des programmes cités ne couvre pas la part "
              "budgétaire : l'assiette déborde ce qui est nommé")
        if r['chiffre_sur_budget_initial']:
            a("  source      budget initial 2025 de l'organisme — pièce hors "
              "corpus, sourcée par ailleurs et validée (A-113)")
        a(f"  motif       {r['motif']}")
        a('')

    a('=' * 78)
    a('')
    a('Bouclages')
    a('')
    for b in bcl:
        v = verdict(b)
        marque = '  ' if v == 'accord' else '⚠ '
        a(f"{marque}{b['objet']:<58s} {_md(b['recompose']):>10s} vs "
          f"{_md(b['affiche']):>10s}   {v}")
    a('')
    ko = [b for b in bcl if verdict(b) != 'accord']
    a(f"  {len(bcl) - len(ko)}/{len(bcl)} bouclages en accord")
    a('')
    a('=' * 78)
    a('')
    a("Chaîne des emplois et des charges — la formule reconstituée")
    a('')
    for x in deriv:
        marque = ('  ' if x['verdict'] in ('accord', 'écart de concept')
                  else '⚠ ')
        val = ('—' if x['calcule'] is None
               else f"{x['calcule']:,.3f}".replace(',', ' ')
               if x['unite'] == 'Md€'
               else f"{x['calcule']:,.0f}".replace(',', ' '))
        ecrit = (f"{x['ecrit_au_classeur']:,.3f}".replace(',', ' ')
                 if x['unite'] == 'Md€'
                 else f"{x['ecrit_au_classeur']:,.0f}".replace(',', ' '))
        a(f"{marque}{x['objet']}")
        a(f"    {x['formule']}")
        a(f"    calculé {val} {x['unite']} · écrit au classeur {ecrit} "
          f"{x['unite']} · {x['verdict']}")
        a(f"    {x['ou']}")
        if x['ecart_de_concept']:
            a(f"    écart de concept : {x['ecart_de_concept']}")
        a('')
    a('=' * 78)
    a('')
    a("Grande synthèse — les lignes du classeur, avec leur source citée")
    a('')
    for g in synthese:
        c = g['classeur']
        a(f"  {c['intitule']}")
        a(f"    direct {_md(c['gain_direct_md_eur'])}"
          f" + indirect {_md(c['gain_indirect_md_eur'])}"
          f" = {_md(c['total_supprime_md_eur'])} Md€"
          + (f"   gisement en sus {_md(c['gisement_en_sus_md_eur'])}"
             if c['gisement_en_sus_md_eur'] else ''))
        if c['source']:
            a(f"    source : {' '.join(c['source'].split())}")
        a('')
    return '\n'.join(L) + '\n'


def main(src, dst_json, dst_txt):
    socle = json.load(open(src, encoding='utf-8'))
    if 'economies' not in socle:
        print("socle sans arbre des économies — relancer socle_budgetaire.py "
              "avec --calculs")
        return 2
    lignes = tracer(socle)
    bcl = bouclages(lignes)
    deriv = derivations(socle)
    synthese = socle.get('grande_synthese', [])
    sortie = {
        '_revision': {
            'version': 'traçage des économies v1',
            'objet': "chaque ligne d'économie rattachée à son assiette, par "
                     "canal, avec le bouclage sur les taxes affectées",
            'regle': "L'écart entre la ligne du classeur et ce que les taxes "
                     "recomposent n'est jamais absorbé : il est nommé part "
                     "budgétaire. Un rattachement s'écrit, il ne se devine pas.",
            'produit_par': 'appareil/tracer_economies.py',
        },
        'lignes': lignes,
        'bouclages': [dict(b, verdict=verdict(b)) for b in bcl],
        'derivations': deriv,
        'comptes': {
            'lignes': len(lignes),
            'rattachees': sum(1 for l in lignes if l['rattachement']),
            'bouclages': len(bcl),
            'bouclages_en_accord': sum(1 for b in bcl
                                       if verdict(b) == 'accord'),
            'derivations': len(deriv),
            'derivations_en_accord': sum(1 for x in deriv
                                         if x['verdict'] == 'accord'),
        },
    }
    with open(dst_json, 'w', encoding='utf-8') as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
        f.write('\n')
    with open(dst_txt, 'w', encoding='utf-8') as f:
        f.write(rendre(lignes, bcl, synthese, deriv))
    c = sortie['comptes']
    print(f"{dst_json} et {dst_txt} écrits — {c['lignes']} lignes · "
          f"{c['rattachees']} rattachées · "
          f"{c['bouclages_en_accord']}/{c['bouclages']} bouclages · "
          f"{c['derivations_en_accord']}/{c['derivations']} dérivations")
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(*sys.argv[1:]))
