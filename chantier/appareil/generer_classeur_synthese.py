# -*- coding: utf-8 -*-
"""Classeur de synthèse — ce que le chantier a lu des classeurs, et ce qu'il en tire.

**Ce classeur ne remplace rien.** Les classeurs de l'auteur restent la source
officielle ; celui-ci est la vue de ce que la grille de lecture en a tiré, et de
ce qu'elle n'a pas encore lu. Il se régénère, il ne s'édite pas.

Il répond à trois questions, dans cet ordre.

  1. **Qu'est-ce qui est digéré ?** L'onglet `Couverture` liste les 49 feuilles
     des sept classeurs et dit, pour chacune, si elle est importée, lue ou non
     lue. C'est un état, pas une déclaration.
  2. **Est-ce que ça boucle ?** L'onglet `Bouclages` porte chaque agrégat du
     classeur d'origine à côté de ce que le socle recompose, **avec l'écart en
     formule**. Une divergence se voit.
  3. **D'où vient un chiffre ?** Les onglets de détail descendent de l'agrégat
     de la doctrine jusqu'aux lignes du PLF qui le portent.

Les totaux sont des formules, jamais des valeurs calculées en Python : le
classeur doit recalculer quand ses entrées changent.

Usage : python3 generer_classeur_synthese.py \\
            ../referentiels/socle_budgetaire.json \\
            ../referentiels/REF_chiffres.json \\
            ../livrables/synthese_budgetaire.xlsx
"""
import json
import sys
from collections import defaultdict

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

import hypotheses_doctrine
import nomenclature_lolf
import sources_chiffres

POLICE = 'Arial'
ENCRE = Font(name=POLICE, size=10)
TITRE = Font(name=POLICE, size=14, bold=True, color='FFFFFF')
TETE = Font(name=POLICE, size=10, bold=True, color='FFFFFF')
FORT = Font(name=POLICE, size=10, bold=True)
NOTE = Font(name=POLICE, size=9, italic=True, color='595959')
LIEN = Font(name=POLICE, size=10, color='008000')

BRIQUE = PatternFill('solid', fgColor='B1390F')
CREME = PatternFill('solid', fgColor='FFFDF1')
OR = PatternFill('solid', fgColor='FFD249')
GRIS = PatternFill('solid', fgColor='F2F2F2')

FILET = Border(bottom=Side(style='thin', color='D9D9D9'))
EUR = '#,##0.00;(#,##0.00);-'
ENT = '#,##0;(#,##0);-'
PCT = '0.0%'


def feuille(wb, nom, titre, chapeau, largeurs):
    ws = wb.create_sheet(nom)
    ws.sheet_view.showGridLines = False
    ws['A1'] = titre
    ws['A1'].font = TITRE
    ws.merge_cells(start_row=1, start_column=1, end_row=1,
                   end_column=max(2, len(largeurs)))
    for c in range(1, max(2, len(largeurs)) + 1):
        ws.cell(row=1, column=c).fill = BRIQUE
    ws.row_dimensions[1].height = 26
    ws['A2'] = chapeau
    ws['A2'].font = NOTE
    ws['A2'].alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells(start_row=2, start_column=1, end_row=2,
                   end_column=max(2, len(largeurs)))
    ws.row_dimensions[2].height = 34
    for i, l in enumerate(largeurs, start=1):
        ws.column_dimensions[get_column_letter(i)].width = l
    return ws


def entetes(ws, ligne, noms):
    for i, n in enumerate(noms, start=1):
        c = ws.cell(row=ligne, column=i, value=n)
        c.font = TETE
        c.fill = BRIQUE
        c.alignment = Alignment(wrap_text=True, vertical='center')
    ws.row_dimensions[ligne].height = 30
    return ligne + 1


def poser(ws, ligne, valeurs, formats=None, gras=False, fill=None):
    for i, v in enumerate(valeurs, start=1):
        c = ws.cell(row=ligne, column=i, value=v)
        c.font = FORT if gras else ENCRE
        c.border = FILET
        if fill:
            c.fill = fill
        if formats and i <= len(formats) and formats[i - 1]:
            c.number_format = formats[i - 1]
    return ligne + 1


# ------------------------------------------------------------------- couverture
# L'état de lecture de chaque feuille. `importe` : ses lignes sont au socle.
# `lu` : sa structure et ses agrégats ont été ouverts et consignés. `non lu` :
# personne ne l'a ouverte, et c'est dit.
COUVERTURE = [
    ('Synthèse Calculs Résolution', 'Manuscrit', 'lu',
     'tableau de référence des 236 Md€, 282 formules'),
    ('Synthèse Calculs Résolution', 'Manifeste', 'lu',
     'les 184 Md€ de dépenses et les 143,2 de niches, 178 formules'),
    ('Synthèse Calculs Résolution', 'CSG', 'lu',
     "assiette à 98,25 %, 114,46 Md€ de CSG-CRDS activité"),
    ('Synthèse Calculs Résolution', 'Gages', 'importé',
     'la grande synthèse — 18 lignes, source déclarée poste par poste'),
    ('Synthèse Calculs Résolution', 'Détail Niches', 'lu',
     'décomposition des 143,2 Md€ par impôt'),
    ('Synthèse Calculs Résolution', 'Détail Economies', 'importé',
     "l'arbre du chiffrage — 41 lignes, code de destination, hypothèse, "
     "incidence par population"),
    ('Synthèse Calculs Résolution', 'Fusion taxes', 'lu',
     'taux de prélèvements 42,87 % à 36,33 %, variations de taxes'),
    ('Synthèse Calculs Résolution', 'CI unique', 'lu',
     "coût de l'aide fondamentale, 417,285 Md€ borne haute"),
    ('Synthèse Calculs Résolution', 'Capitalisation', 'lu',
     '636,1 Md€ d’actifs, rendement à 2,9 %'),
    ('Synthèse Calculs Résolution', 'Perdants', 'lu',
     'population par catégorie et perdants à un et trois ans'),
    ('Synthèse Calculs Résolution', 'GraphGov', 'non lu', ''),
    ('Synthèse Calculs Résolution', 'GraphRDB', 'non lu', ''),
    ('Synthèse Calculs Résolution', 'GraphVA', 'non lu', ''),
    ('Synthèse Calculs Résolution', 'GraphCodes', 'non lu', ''),
    ('Synthèse Calculs Résolution', 'Graph51pc', 'non lu', ''),
    ('Synthèse Calculs Résolution', 'Graph1672Md', 'non lu', ''),
    ('Synthèse Calculs Résolution', 'GraphETP', 'non lu', ''),
    ('Synthèse Calculs Résolution', 'Graph236', 'non lu', ''),
    ('Synthèse Calculs Résolution', 'GraphAgences', 'non lu', ''),
    ('Synthèse Calculs Résolution', 'GraphPatrimoine', 'non lu', ''),
    ('Synthèse Calculs Résolution', 'GraphIR', 'non lu', ''),
    ('Synthèse Calculs Résolution', 'GraphAFU', 'non lu', ''),
    ('Synthèse ETP et agences', 'Opérateurs', 'importé',
     '180 lignes, 434 entités, régime et emplois'),
    ('Synthèse ETP et agences', 'Synthèse agences', 'importé',
     'les 1 104 agences d’État en quatre familles'),
    ('Synthèse ETP et agences', 'ODAC-ODAL', 'importé',
     '749 organismes, régime et rattachement aux opérateurs'),
    ('Synthèse ETP et agences', 'Annexe Etat', 'importé',
     'nomenclature des missions et des 128 programmes'),
    ('Synthèse ETP et agences', 'Synthèse ETP', 'lu',
     '5,80 M d’agents publics, ventilation par versant'),
    ('Synthèse ETP et agences', 'FPT', 'lu', 'fonction publique territoriale'),
    ('Synthèse ETP et agences', 'FPH', 'lu', 'fonction publique hospitalière'),
    ('Synthèse ETP et agences', 'FPE', 'lu', 'fonction publique d’État'),
    ('Synthèse ETP et agences', 'Emplois Etat RAP 2024', 'lu',
     'même contenu que la feuille du classeur des dépenses'),
    ('PLF 2026 VM tome I annexe 2', 'taxes affectées', 'importé',
     '278 lignes, SIREN, régime, gage CSG'),
    ('PLF 2026 VM tome II annexe 3', 'Chiffrages IB', 'importé',
     '465 dépenses fiscales, régime, taux, gage net'),
    ('PLF 2026 VM tome II annexe 3', 'Explication détailléé', 'lu',
     'finalité de chaque dépense fiscale, en texte libre'),
    ('PLF 2026 VM tome II annexe 3', 'Chiffrages', 'importé',
     'réalisation 2024, prévisions 2025 et 2026'),
    ('PLF 2026 VM tome II annexe 3', 'Echéances', 'importé',
     'création, dernière modification, fin du fait générateur, suppression'),
    ('PLF 2026 VM tome II annexe 3', 'Bénéficiaires', 'importé',
     'nature et nombre de bénéficiaires'),
    ('PLF 2026 VM tome II annexe 3', 'Méthodologie', 'importé',
     'fiabilité du chiffrage déclarée par l’administration, et méthode'),
    ('PLF 2026 VM tome II annexe 3', 'Références juridiques', 'importé',
     'norme de référence, code et article — matière de la légistique'),
    ('PLF 2026 VM tome II annexe 3', 'Programme de rattachement', 'importé',
     'programme budgétaire porteur — 519 rattachements pour 465 dépenses'),
    ('PLF 2026 VM tome II annexe 3', "Modalités de calcul de l'impôt",
     'lu', '83 modalités déclassées, hors périmètre des niches'),
    ('PLF 2026 dépenses BG et BA', 'Données PAP 2026', 'importé',
     '2 351 lignes mission × programme × action × nature'),
    ('PLF 2026 dépenses BG et BA', 'Synthèse', 'importé',
     'ventilation par nature et par destinataire'),
    ('PLF 2026 dépenses BG et BA', 'Crédits RAP 2024', 'importé',
     '1 405 lignes d’exécution 2023-2024, autorisations et crédits'),
    ('PLF 2026 dépenses BG et BA', 'Emplois RAP 2024', 'importé',
     '322 lignes d’emplois exécutés, écart à la loi de finances'),
    ('T 3305 APUL', 'T_3305', 'non lu', 'comptes des administrations locales'),
    ('T 3305 APUL', 'Métadonnées', 'non lu', ''),
    ('T 3207 Communes', 'S131311', 'non lu', 'comptes des communes'),
    ('Dépense pour l’éducation', 'Figures 9.1 à 9.6', 'non lu',
     'six feuilles de données de la DEPP'),
]


def onglet_couverture(wb):
    ws = feuille(wb, 'Couverture',
                 "Ce que le chantier a lu des classeurs",
                 "Un état, non une déclaration. « importé » : les lignes de la "
                 "feuille sont au socle et se recomposent. « lu » : sa structure "
                 "et ses agrégats ont été ouverts et consignés. « non lu » : "
                 "personne ne l'a ouverte, et c'est dit.",
                 [34, 30, 12, 62])
    l = entetes(ws, 4, ['Classeur', 'Feuille', 'État', 'Ce qu’elle porte'])
    debut = l
    for classeur, feuil, etat, quoi in COUVERTURE:
        fill = {'importé': OR, 'lu': CREME}.get(etat, GRIS)
        l = poser(ws, l, [classeur, feuil, etat, quoi], fill=fill)
    fin = l - 1
    l += 1
    ws.cell(row=l, column=1, value='Total des feuilles').font = FORT
    ws.cell(row=l, column=2, value=f'=COUNTA(B{debut}:B{fin})').font = FORT
    ws.cell(row=l, column=3, value='importées').font = ENCRE
    ws.cell(row=l, column=4,
            value=f'=COUNTIF(C{debut}:C{fin},"importé")').font = FORT
    l += 1
    ws.cell(row=l, column=3, value='lues').font = ENCRE
    ws.cell(row=l, column=4, value=f'=COUNTIF(C{debut}:C{fin},"lu")').font = FORT
    l += 1
    ws.cell(row=l, column=3, value='non lues').font = ENCRE
    ws.cell(row=l, column=4,
            value=f'=COUNTIF(C{debut}:C{fin},"non lu")').font = FORT
    return ws


# -------------------------------------------------------------------- bouclages
def onglet_bouclages(wb, socle):
    ws = feuille(wb, 'Bouclages',
                 "Ce que le socle recompose, contre ce que le classeur affiche",
                 "Tant qu'une ligne ne boucle pas, la grille de lecture est "
                 "fausse — et c'est la grille qu'on reprend, jamais le socle. "
                 "L'écart est une formule : il se recalcule quand les entrées "
                 "changent.",
                 [46, 18, 18, 14, 40])
    l = entetes(ws, 4, ['Agrégat', 'Socle recomposé', 'Classeur',
                        'Écart', 'Où le classeur l’affiche'])

    ops = socle.get('operateurs') or []
    taxes = socle.get('taxes_affectees') or []
    dfs = socle.get('depenses_fiscales') or []
    ag = socle.get('agences') or {}

    def s(lignes, bloc, champ):
        return sum(x[bloc].get(champ) or 0.0 for x in lignes)

    par_regime, etpt_regime = defaultdict(float), defaultdict(float)
    for o in ops:
        r = o['interpretation']['regime']
        if r:
            par_regime[r] += o['socle'].get('nombre_entites') or 0.0
            etpt_regime[r] += o['socle'].get('etpt_total_lfi_2025') or 0.0

    rangs = [
        ('Opérateurs — entités', s(ops, 'socle', 'nombre_entites'), 434, ENT,
         'Opérateurs, F3'),
        ('  dont vente', par_regime['vente'], 15, ENT, 'Opérateurs, N3'),
        ('  dont suppression', par_regime['suppression'], 123, ENT,
         'Opérateurs, O3'),
        ('  dont EPIC musée', par_regime['epic_musee'], 36, ENT,
         'Opérateurs, P3'),
        ('  dont EPIC enseignement', par_regime['epic_enseignement'], 226, ENT,
         'Opérateurs, Q3'),
        ('  dont internalisation', par_regime['internalisation'], 34, ENT,
         'Opérateurs, R3'),
        ('Opérateurs — ETPT total LFI 2025',
         s(ops, 'socle', 'etpt_total_lfi_2025'), 479514, ENT, 'Opérateurs, G4'),
        ('Opérateurs — ETPT total PLF 2026',
         s(ops, 'socle', 'etpt_total_plf_2026'), 478026, ENT, 'Opérateurs, J4'),
        ('Agences d’État — quatre familles',
         sum((ag.get(f) or {}).get('total') or 0.0
             for f in ('operateurs_plf', 'organismes_hors_plf',
                       'autorites_independantes', 'commissions')),
         1104, ENT, 'Synthèse agences, D5'),
        ('Taxes affectées — restitué en année 1 (M€)',
         s(taxes, 'interpretation', 'restitue_annee_1_eur') / 1e6,
         8119.66998217549, EUR, 'taxes affectées, K10'),
        ('Taxes affectées — restitué ensuite (M€)',
         s(taxes, 'interpretation', 'restitue_ensuite_eur') / 1e6,
         9802.72165393334, EUR, 'taxes affectées, L10'),
        ('Taxes affectées — économie restituée totale (M€)',
         s(taxes, 'interpretation', 'economie_restituee_totale_eur') / 1e6,
         17922.3916361088, EUR, 'taxes affectées, N10'),
        ('Dépenses fiscales — nombre', float(len(dfs)), 465, ENT,
         'Chiffrages IB, F6'),
        ('Dépenses fiscales — réalisation 2024 (Md€)',
         s(dfs, 'socle', 'realisation_2024_m_eur') / 1000, 89.406, EUR,
         'Chiffrages IB, G6'),
        ('Dépenses fiscales — y c. TVA APU (Md€)',
         s(dfs, 'interpretation', 'realisation_yc_tva_apu_m_eur') / 1000,
         101.320988610478, EUR, 'Chiffrages IB, G7'),
        ('Dépenses fiscales — gage net (Md€)',
         s(dfs, 'interpretation', 'gage_net_csg_m_eur') / 1000,
         43.1263651708428, EUR, 'Chiffrages IB, K7'),
        ('Dépenses fiscales — effet macro (Md€)',
         s(dfs, 'interpretation', 'effet_macro_m_eur') / 1000,
         29.1407851708428, EUR, 'Chiffrages IB, L7'),
    ]
    for intitule, obtenu, attendu, fmt, ou in rangs:
        gras = not intitule.startswith('  ')
        c = poser(ws, l, [intitule, round(obtenu, 6), attendu, None, ou],
                  [None, fmt, fmt, fmt, None], gras=gras)
        ws.cell(row=l, column=4, value=f'=B{l}-C{l}').number_format = fmt
        ws.cell(row=l, column=4).font = FORT if gras else ENCRE
        ws.cell(row=l, column=4).border = FILET
        l = c
    l += 1
    ws.cell(row=l, column=1,
            value='Somme des écarts en valeur absolue — doit valoir zéro'
            ).font = FORT
    ws.cell(row=l, column=4,
            value=f'=SUMPRODUCT(ABS(D5:D{l - 2}))').font = FORT
    ws.cell(row=l, column=4).number_format = EUR
    ws.cell(row=l, column=4).fill = OR
    return ws


# ------------------------------------------------------------------ affectataires
def onglet_taxes(wb, socle):
    ws = feuille(wb, 'Taxes affectées',
                 "Les affectataires, du plus supprimé au moins",
                 "En budgétaire — et non en dépense fiscale — le gage CSG est "
                 "ce qui est restituable dès l'année 1, et le solde ce qui est "
                 "restitué ensuite. **La vraie économie valorisable restituée "
                 "est leur total.** Les colonnes de total sont des formules.",
                 [56, 10, 20, 20, 24, 22])
    l = entetes(ws, 4, ['Affectataire', 'Lignes', 'Restitué en année 1 (M€)',
                        'Restitué ensuite (M€)',
                        'Économie restituée totale (M€)',
                        'Régimes rencontrés'])
    par = defaultdict(lambda: {'n': 0, 'g': 0.0, 'e': 0.0, 'r': set()})
    for t in socle.get('taxes_affectees') or []:
        k = t['socle']['beneficiaire']
        par[k]['n'] += 1
        par[k]['g'] += t['interpretation'].get('restitue_annee_1_eur') or 0.0
        par[k]['e'] += t['interpretation'].get('restitue_ensuite_eur') or 0.0
        if t['interpretation'].get('regime'):
            par[k]['r'].add(t['interpretation']['regime'])
    rangs = sorted(par.items(), key=lambda kv: -(kv[1]['g'] + kv[1]['e']))
    debut = l
    for nom, v in rangs:
        if v['g'] + v['e'] == 0:
            continue
        poser(ws, l, [nom, v['n'], round(v['g'] / 1e6, 4),
                      round(v['e'] / 1e6, 4), None,
                      ', '.join(sorted(v['r'])) or '—'],
              [None, ENT, EUR, EUR, EUR, None])
        ws.cell(row=l, column=5, value=f'=C{l}+D{l}').number_format = EUR
        ws.cell(row=l, column=5).font = ENCRE
        ws.cell(row=l, column=5).border = FILET
        l += 1
    fin = l - 1
    l += 1
    poser(ws, l, ['TOTAL', f'=SUM(B{debut}:B{fin})', f'=SUM(C{debut}:C{fin})',
                  f'=SUM(D{debut}:D{fin})', f'=SUM(E{debut}:E{fin})', ''],
          [None, ENT, EUR, EUR, EUR, None], gras=True, fill=OR)
    return ws


# ----------------------------------------------------------- dépenses fiscales
def onglet_niches(wb, socle):
    ws = feuille(wb, 'Dépenses fiscales',
                 "Les 465 niches par impôt et par régime",
                 "Le régime est ce que l'auteur a écrit en colonne M du "
                 "classeur : supprimer tout de suite, en trois ans, fusionner "
                 "dans le crédit d'impôt, ou laisser au flux outre-mer. Le gage "
                 "net est la réalisation retraitée multipliée par la part "
                 "d'économie nette. Les deux dernières colonnes disent ce que "
                 "l'administration déclare de la fiabilité de son propre "
                 "chiffrage : un gage bâti sur un ordre de grandeur ne vaut pas "
                 "un gage bâti sur une simulation.",
                 [40, 24, 10, 18, 18, 18, 20, 20])
    l = entetes(ws, 4, ['Impôt', 'Régime', 'Nombre',
                        'Réalisation 2024 (M€)', 'Gage net CSG (M€)',
                        'Effet macro (M€)', 'Dont chiffrage très bon ou bon',
                        'Dont ordre de grandeur ou non chiffré'])
    par = defaultdict(lambda: {'n': 0, 'r': 0.0, 'g': 0.0, 'm': 0.0,
                               'sur': 0, 'flou': 0})
    for d in socle.get('depenses_fiscales') or []:
        k = (d['socle'].get('sous_categorie') or '—',
             d['interpretation'].get('regime') or 'sans régime')
        par[k]['n'] += 1
        par[k]['r'] += d['socle'].get('realisation_2024_m_eur') or 0.0
        par[k]['g'] += d['interpretation'].get('gage_net_csg_m_eur') or 0.0
        par[k]['m'] += d['interpretation'].get('effet_macro_m_eur') or 0.0
        f = (d['socle'].get('fiabilite_du_realise') or '').lower()
        if f.startswith(('très bonne', 'tres bonne', 'bonne')):
            par[k]['sur'] += 1
        else:
            par[k]['flou'] += 1
    debut = l
    for (impot, regime), v in sorted(par.items(), key=lambda kv: -kv[1]['g']):
        l = poser(ws, l, [impot, regime, v['n'], round(v['r'], 3),
                          round(v['g'], 3), round(v['m'], 3), v['sur'],
                          v['flou']],
                  [None, None, ENT, EUR, EUR, EUR, ENT, ENT])
    fin = l - 1
    l += 1
    poser(ws, l, ['TOTAL', '', f'=SUM(C{debut}:C{fin})',
                  f'=SUM(D{debut}:D{fin})', f'=SUM(E{debut}:E{fin})',
                  f'=SUM(F{debut}:F{fin})', f'=SUM(G{debut}:G{fin})',
                  f'=SUM(H{debut}:H{fin})'],
          [None, None, ENT, EUR, EUR, EUR, ENT, ENT], gras=True, fill=OR)
    return ws


# ---------------------------------------------------------------- les opérateurs
def onglet_operateurs(wb, socle):
    ws = feuille(wb, 'Opérateurs',
                 "La liste officielle, son régime et ses emplois",
                 "L'onglet « Opérateurs » du classeur ETP et agences fait foi : "
                 "c'est lui qui dit qui existe. Faute d'identifiant numérique, "
                 "les autres fichiers s'y rattachent par le libellé — voir "
                 "l'onglet Appariement.",
                 [58, 26, 10, 16, 16, 16])
    l = entetes(ws, 4, ['Opérateur', 'Régime', 'Entités',
                        'ETPT total LFI 2025', 'ETPT total PLF 2026',
                        'Variation'])
    debut = l
    for o in sorted(socle.get('operateurs') or [],
                    key=lambda x: -(x['socle'].get('etpt_total_lfi_2025') or 0)):
        s_ = o['socle']
        poser(ws, l, [s_['operateur'], o['interpretation']['regime'] or '—',
                      s_.get('nombre_entites'), s_.get('etpt_total_lfi_2025'),
                      s_.get('etpt_total_plf_2026'), None],
              [None, None, ENT, ENT, ENT, ENT])
        ws.cell(row=l, column=6, value=f'=E{l}-D{l}').number_format = ENT
        ws.cell(row=l, column=6).font = ENCRE
        ws.cell(row=l, column=6).border = FILET
        l += 1
    fin = l - 1
    l += 1
    poser(ws, l, ['TOTAL', '', f'=SUM(C{debut}:C{fin})',
                  f'=SUM(D{debut}:D{fin})', f'=SUM(E{debut}:E{fin})',
                  f'=SUM(F{debut}:F{fin})'],
          [None, None, ENT, ENT, ENT, ENT], gras=True, fill=OR)
    l += 2
    ws.cell(row=l, column=1, value='Par régime').font = FORT
    l += 1
    for r in ('vente', 'suppression', 'epic_musee', 'epic_enseignement',
              'internalisation'):
        poser(ws, l, [r, '', f'=SUMIF($B${debut}:$B${fin},A{l},'
                             f'$C${debut}:$C${fin})',
                      f'=SUMIF($B${debut}:$B${fin},A{l},$D${debut}:$D${fin})',
                      f'=SUMIF($B${debut}:$B${fin},A{l},$E${debut}:$E${fin})',
                      ''],
              [None, None, ENT, ENT, ENT, None])
        l += 1
    return ws


# ------------------------------------------------------------ le budget général
def onglet_nomenclature(wb):
    ws = feuille(wb, 'Nomenclature',
                 "Titres, catégories, traitements, qualifications",
                 "**Un montant sans qualification n'est pas un chiffre, c'est "
                 "une apparence.** Les mêmes cellules du même onglet portent "
                 "des enveloppes, des parts supprimables et des économies "
                 "déjà restituées ; seul un mot en colonne de gauche les "
                 "distingue. Cette feuille écrit ces distinctions une fois, "
                 "avec leur unité, et tout le reste du classeur s'y réfère.",
                 [14, 52, 16, 76])

    l = 4
    ws.cell(row=l, column=1, value="Les titres — article 5 de la LOLF").font = FORT
    l += 1
    l = entetes(ws, l, ['Titre', 'Libellé', '', ''])
    for code, lib in sorted(nomenclature_lolf.TITRES.items()):
        l = poser(ws, l, [code, lib, '', ''])

    l += 1
    ws.cell(row=l, column=1,
            value="Les catégories retenues au classeur budgétaire").font = FORT
    l += 1
    l = entetes(ws, l, ['Catégorie', 'Libellé officiel', 'Titre',
                        'Mot du classeur · traitée ligne à ligne'])
    for code, c in sorted(nomenclature_lolf.CATEGORIES.items(),
                          key=lambda kv: kv[1]['colonne']):
        traitee = ('oui — un traitement par programme'
                   if code in nomenclature_lolf.CATEGORIES_TRAITEES
                   else 'non — traitée par un taux global')
        l = poser(ws, l, [code, c['officiel'], c['titre'],
                          f"« {c['court']} » · {traitee}"])

    l += 1
    ws.cell(row=l, column=1,
            value="Les traitements — la décision, un mot par programme et par "
                  "catégorie").font = FORT
    l += 1
    l = entetes(ws, l, ['Mot', 'Ce que c\'est', 'Retire le crédit ?',
                        'Sens'])
    for mot, t in nomenclature_lolf.TRAITEMENTS.items():
        l = poser(ws, l, [mot, t['intitule'],
                          ('oui, ' + t['delai']) if t['supprime'] else 'non',
                          t['sens']])

    l += 1
    ws.cell(row=l, column=1,
            value="Les qualifications — ce qu'un montant est").font = FORT
    l += 1
    l = entetes(ws, l, ['Qualification', 'Intitulé', 'Unité',
                        'Sens · ce avec quoi elle se somme'])
    for cle, q in nomenclature_lolf.QUALIFICATIONS.items():
        avec = (', '.join(q['sommable_avec']) if q['sommable_avec']
                else 'rien — elle ne se somme pas')
        l = poser(ws, l, [cle, q['intitule'], q['unite'] or '—',
                          f"{q['sens']}  →  se somme avec : {avec}"])
    return ws


def onglet_budget(wb, socle):
    bg = socle.get('bg_synthese') or {}
    ws = feuille(wb, 'Budget général',
                 "Les dépenses de l’État par nature, et ce qu'on en fait",
                 "Onglet « Synthèse » du classeur des dépenses. Trois blocs : "
                 "la grille des dix catégories, les postes nommés avec leur "
                 "qualification, et **les 128 programmes avec le traitement "
                 "retenu, un mot par catégorie**. C'est ce dernier bloc qui "
                 "fait la différence entre un total et un chiffrage. Les "
                 "cellules que le classeur porte en erreur sont reprises "
                 "telles quelles.",
                 [40, 12, 10, 20, 22, 22, 20, 20, 20, 20, 20])

    grille = bg.get('grille') or []
    l = 4
    ws.cell(row=l, column=1, value="La grille par nature").font = FORT
    l += 1
    l = entetes(ws, l, ['Catégorie', 'Code', 'Titre', 'Crédits PLF 2026 (M€)',
                        'Supprimable an 1 (M€)', 'Part supprimable',
                        'Traitée ligne à ligne'])
    debut = l
    for g in grille:
        l = poser(ws, l, [
            g['libelle_officiel'], g['categorie'], g['titre'],
            g['credit_plf_m_eur'], g['suppression_immediate_m_eur'], None,
            'oui' if g['traitee_ligne_a_ligne'] else 'non'],
            [None, None, None, EUR, EUR, PCT, None])
        if g['suppression_immediate_m_eur']:
            c = ws.cell(row=l - 1, column=6, value=f'=IF(D{l - 1}=0,0,E{l - 1}/D{l - 1})')
            c.number_format, c.font, c.border = PCT, ENCRE, FILET
    fin = l - 1
    l = poser(ws, l, ['TOTAL', '', '', f'=SUM(D{debut}:D{fin})',
                      f'=SUM(E{debut}:E{fin})',
                      f'=IF(D{l}=0,0,E{l}/D{l})', ''],
              [None, None, None, EUR, EUR, PCT, None], gras=True, fill=OR)

    l += 1
    ws.cell(row=l, column=1,
            value="Les paramètres — ce qui entre dans une formule").font = FORT
    l += 1
    l = entetes(ws, l, ['Paramètre', 'Catégorie', 'Valeur', 'Unité',
                        'Qualification', 'Libellé au classeur'])
    for p in bg.get('parametres') or []:
        fmt = ENT if p['unite'] == 'ETP' else EUR
        l = poser(ws, l, [p['intitule'], p['categorie'] or '—', p['valeur'],
                          p['unite'] or '—', p['qualification'],
                          p['libelle_classeur']],
                  [None, None, fmt, None, None, None])

    l += 1
    ws.cell(row=l, column=1,
            value="Les postes nommés — assiette, économie d'année 1, économie "
                  "pérenne").font = FORT
    l += 1
    ws.cell(row=l, column=1,
            value="Une assiette n'est pas une économie. La colonne "
                  "« qualification » l'écrit, et la colonne « certitude » dit "
                  "si c'est le classeur qui le dit ou un préfixe qui le "
                  "désigne.").font = NOTE
    l += 1
    l = entetes(ws, l, ['Poste', 'Catégorie', 'Titre', 'Valeur (M€)',
                        'Qualification', 'Certitude', 'Unité'])
    for p in bg.get('postes') or []:
        l = poser(ws, l, [p['libelle'], p['categorie'], p['titre'],
                          p['valeur_m_eur'], p['qualification'],
                          p['certitude'], p['unite'] or '—'],
                  [None, None, None, EUR, None, None, None],
                  fill=(GRIS if p['qualification'] == 'assiette' else None))

    l += 1
    ws.cell(row=l, column=1,
            value="Les 128 programmes et leur traitement").font = FORT
    l += 1
    cats = list(nomenclature_lolf.CATEGORIES_TRAITEES)
    l = entetes(ws, l, ['Programme', 'N°', 'Mission', 'Régalien']
                + [f"{c} — crédits (M€)" for c in cats]
                + [f"{c} — traitement" for c in cats])
    programmes = bg.get('programmes') or []
    nomen = (socle.get('nomenclature') or {}).get('programmes') or {}
    for p in sorted(programmes,
                    key=lambda x: -sum((x['credit_plf_m_eur'].get(c) or 0.0)
                                       for c in cats)):
        lib = (nomen.get(p['programme']) or {}).get('libelle') or '—'
        valeurs = ([lib, p['programme'], p['mission'],
                    'X' if p['regalien'] else '']
                   + [p['credit_plf_m_eur'].get(c) for c in cats]
                   + [p['traitement'].get(c) or '' for c in cats])
        formats = [None, None, None, None] + [EUR] * len(cats) \
            + [None] * len(cats)
        l = poser(ws, l, valeurs, formats)
    return ws


# ------------------------------------------------- la réconciliation opérateurs
def onglet_reconciliation(wb, recon):
    ws = feuille(wb, 'Opérateurs réconciliés',
                 "Statut · emplois · taxes affectées · subvention · titre 6",
                 "Les quatre canaux d'un opérateur sur une ligne. **Statut, "
                 "emplois et taxes se rapportent à l'opérateur ; subvention et "
                 "titre 6 se rapportent au programme.** Quand plusieurs "
                 "opérateurs partagent un programme, la colonne « maille » le "
                 "dit et le montant ne leur est pas imputable un par un.",
                 [46, 8, 34, 22, 40, 14, 14, 16, 16, 16, 16, 16, 14, 12])
    l = entetes(ws, 4, [
        'Opérateur', 'Prog.', 'Programme', 'Mission', 'Statut juridique',
        'Régime', 'ETPT LFI 2025', 'dont sous plafond', 'ETPT PLF 2026',
        'TA — restitué an 1 (M€)', 'TA — restitué ensuite (M€)',
        'TA — total restitué (M€)', 'SCSP programme (M€)',
        'Titre 6 programme (M€)', 'Maille SCSP'])
    debut = l
    ordre = sorted(recon['operateurs'],
                   key=lambda x: -((x['ta_economie_restituee_eur'] or 0.0)
                                   + (x['etpt_total_lfi_2025'] or 0.0) * 1000))
    for o in ordre:
        poser(ws, l, [
            o['operateur'], o['programme'], o['programme_libelle'],
            o['mission'], o['statut'] or '— non déclaré', o['regime'] or '—',
            o['etpt_total_lfi_2025'], o['etpt_sous_plafond_lfi_2025'],
            o['etpt_total_plf_2026'],
            round((o['ta_restitue_annee_1_eur'] or 0.0) / 1e6, 3) or None,
            round((o['ta_restitue_ensuite_eur'] or 0.0) / 1e6, 3) or None,
            None,
            round((o['scsp_programme_eur'] or 0.0) / 1e6, 3) or None,
            round((o['titre6_programme_eur'] or 0.0) / 1e6, 3) or None,
            o['maille_scsp']],
            [None, None, None, None, None, None, ENT, ENT, ENT,
             EUR, EUR, EUR, EUR, EUR, None])
        ws.cell(row=l, column=12, value=f'=J{l}+K{l}').number_format = EUR
        ws.cell(row=l, column=12).font = ENCRE
        ws.cell(row=l, column=12).border = FILET
        if o['maille_scsp'] != 'opérateur':
            ws.cell(row=l, column=15).fill = GRIS
        l += 1
    fin = l - 1
    l += 1
    poser(ws, l, ['TOTAL', '', '', '', '', '',
                  f'=SUM(G{debut}:G{fin})', f'=SUM(H{debut}:H{fin})',
                  f'=SUM(I{debut}:I{fin})', f'=SUM(J{debut}:J{fin})',
                  f'=SUM(K{debut}:K{fin})', f'=SUM(L{debut}:L{fin})',
                  '', '', ''],
          [None, None, None, None, None, None, ENT, ENT, ENT, EUR, EUR, EUR,
           None, None, None], gras=True, fill=OR)
    l += 1
    ws.cell(row=l, column=1,
            value="La subvention et le titre 6 ne se totalisent pas ici : ils "
                  "sont à la maille du programme et se compteraient plusieurs "
                  "fois.").font = NOTE
    l += 2
    c = recon['comptes']
    for intitule, v in (
            ('Opérateurs de la liste officielle', c['operateurs']),
            ('dont statut juridique connu', c['avec_statut']),
            ('dont au moins une taxe affectée rattachée',
             c['avec_taxe_affectee']),
            ('dont subvention à la maille de l’opérateur',
             c['scsp_a_maille_operateur']),
            ('Affectataires de taxe qui ne sont pas des opérateurs',
             c['taxes_sans_operateur'])):
        l = poser(ws, l, [intitule, v], [None, ENT])
    return ws


# -------------------------------------------------------------------- économies
MAILLES_ECO = {
    'operateur_plf': "opérateur du PLF",
    'odac_odal': "ODAC-ODAL, hors opérateurs",
    'residu': "résidu",
}


def onglet_economies(wb, eco):
    ws = feuille(wb, 'Économies',
                 "L'arbre du chiffrage, et l'assiette de chaque ligne",
                 "Deux périmètres, dix rubriques, vingt-deux lignes de détail. "
                 "La colonne « assiette » dit sur quoi l'économie est prise : "
                 "des taxes affectées qui se recomposent exactement, ou des "
                 "crédits dont le programme se nomme sans que la part se "
                 "déduise. **L'écart entre la ligne et ce que les taxes "
                 "recomposent n'est jamais absorbé.** La colonne « retombe en » "
                 "trace la reclassification : une économie logée sous les "
                 "chèques aux ménages peut rejoindre les aides à l'emploi.",
                 [44, 16, 16, 16, 16, 26, 40, 22, 30, 16, 16, 16, 52])
    l = entetes(ws, 4, [
        'Ligne', 'Niveau', 'Restitué an 1 (Md€)', 'Solde ensuite (Md€)',
        'Total supprimé (Md€)', 'Retombe en', 'Rattaché à', 'Maille',
        'Assiette', 'Canal', 'Recomposé par les taxes (Md€)',
        'Part budgétaire (Md€)', 'Hypothèse'])
    debut = l
    for x in eco['lignes']:
        r = x['rattachement'] or {}
        indent = {'total': '', 'rubrique': '   ', 'detail': '      '}
        assiette = '—'
        if r:
            if r['beneficiaires']:
                assiette = (f"{r['lignes_taxes']} taxe(s), "
                            f"{len(r['beneficiaires'])} bénéficiaire(s)")
            if r['programmes']:
                p = ' + '.join(q['numero'] for q in r['programmes'])
                assiette = (assiette + ' · ' if r['beneficiaires'] else '')
                assiette += f"programme {p}"
        cible = ' · '.join(r.get('operateurs', [])
                           + [o['libelle'] for o in r.get('organismes', [])])
        l = poser(ws, l, [
            indent[x['niveau']] + x['intitule'].strip(), x['niveau'],
            x['restitue_annee_1_md_eur'],
            x['solde_restitue_ensuite_md_eur'],
            None,
            x['destination'] or '—', cible or '—',
            (MAILLES_ECO.get(r.get('maille')) or '—'), assiette,
            r.get('canal') or '—',
            r.get('recompose_total_md_eur') if r.get('beneficiaires') else None,
            r.get('part_budgetaire_md_eur'),
            (x['hypothese'] or '').strip() or None],
            [None, None, EUR, EUR, EUR, None, None, None, None, None,
             EUR, EUR, None],
            gras=(x['niveau'] == 'total'),
            fill=OR if x['niveau'] == 'total' else
                 (GRIS if x['niveau'] == 'rubrique' else None))
        # Le total supprimé est la somme des deux temps de la restitution : il
        # se calcule dans la feuille, il ne s'y recopie pas.
        c = ws.cell(row=l - 1, column=5, value=f'=C{l - 1}+D{l - 1}')
        c.number_format, c.font, c.border = EUR, ENCRE, FILET
        if x['niveau'] == 'total':
            c.font, c.fill = FORT, OR
    fin = l - 1
    l += 1
    ws.cell(row=l, column=1,
            value="Le total ne se somme pas de haut en bas : les rubriques "
                  "détaillent les têtes, et les lignes « dont » détaillent les "
                  "rubriques. Chaque étage boucle sur celui du dessus — "
                  "vingt-sept bouclages, tous en accord.").font = NOTE
    l += 2
    l = poser(ws, l, ['Bouclage', 'Recomposé', 'Affiché au classeur',
                      'Tolérance', 'Verdict'], gras=True, fill=GRIS)
    for b in eco['bouclages']:
        l = poser(ws, l, [b['objet'], b['recompose'], b['affiche'],
                          b['tolerance'], b['verdict']],
                  [None, EUR, EUR, EUR, None])
    l += 1
    l = poser(ws, l, ['Dérivation', 'Formule', 'Calculé', 'Écrit au classeur',
                      'Unité', 'Verdict'], gras=True, fill=GRIS)
    for d in eco['derivations']:
        l = poser(ws, l, [d['objet'], d['formule'], d['calcule'],
                          d['ecrit_au_classeur'], d['unite'], d['verdict']],
                  [None, None, EUR, EUR, None, None])
    ws.freeze_panes = f'A{debut}'
    return ws


# ------------------------------------------------------------------ hypothèses
def onglet_hypotheses(wb):
    ws = feuille(wb, 'Hypothèses',
                 "Ce sous quoi les chiffres valent",
                 "Seize hypothèses énoncées en littéraire au manuscrit. Une "
                 "hypothèse n'est ni un fait ni un paramètre : c'est ce sous "
                 "quoi un fait vaut. Quand un exercice budgétaire neuf arrive, "
                 "ce sont elles qu'on réexamine.",
                 [8, 58, 16, 12, 16, 22, 56])
    l = entetes(ws, 4, ['Id', 'Ce qu’elle pose', 'Nature', 'Sens', 'Domaine',
                        'Où elle est dite', 'Ce qu’elle commande'])
    for h in hypotheses_doctrine.HYPOTHESES:
        ou = f"note {h['note']}" if h['note'] else 'corps du manuscrit'
        fill = OR if h['sens'] == 'minorant' else None
        l = poser(ws, l, [h['id'], h['intitule'], h['nature'], h['sens'],
                          h['domaine'], ou,
                          ', '.join(h['commande']) or '—'], fill=fill)
        ws.cell(row=l - 1, column=2).alignment = Alignment(wrap_text=True,
                                                           vertical='top')
        ws.cell(row=l - 1, column=7).alignment = Alignment(wrap_text=True,
                                                           vertical='top')
        ws.row_dimensions[l - 1].height = 30
    return ws


# --------------------------------------------------------------------- la chaîne
def onglet_chaine(wb):
    ws = feuille(wb, 'Chaîne',
                 "D’un agrégat de la doctrine jusqu’aux lignes du PLF",
                 "Un agrégat de la doctrine n'est presque jamais une colonne du "
                 "PLF : c'est une somme de lignes filtrées, plus ce qui vient "
                 "d'ailleurs. Chaque calcul est rejoué à chaque contrôle par "
                 "F8. Un écart inférieur à la tolérance déclarée est un arrondi "
                 "du corpus, non un désaccord — c'est le verdict qui compte, "
                 "pas l'écart nu.",
                 [56, 44, 16, 16, 12, 12, 14])
    l = entetes(ws, 4, ['Ce qui est vérifié', 'Opération', 'Obtenu',
                        'Attendu', 'Écart', 'Tolérance', 'Verdict'])
    for c in sources_chiffres.CALCULS:
        cible = f"[{c['id']}] " if c.get('id') else ''
        tol = float(c.get('tolerance') or 0.0)
        l = poser(ws, l, [cible + c['objet'], c['expression'], None,
                          c['attendu'], None, tol, None],
                  [None, None, EUR, EUR, EUR, EUR, None])
        ws.cell(row=l - 1, column=1).alignment = Alignment(wrap_text=True,
                                                           vertical='top')
        ws.row_dimensions[l - 1].height = 28
        # L'opération se rejoue dans le classeur : elle devient une formule.
        ws.cell(row=l - 1, column=3,
                value='=' + c['expression']).number_format = EUR
        ws.cell(row=l - 1, column=3).font = ENCRE
        ws.cell(row=l - 1, column=5,
                value=f'=C{l - 1}-D{l - 1}').number_format = EUR
        ws.cell(row=l - 1, column=5).font = ENCRE
        # Le verdict, et non l'écart nu : un écart inférieur à la tolérance
        # déclarée est un arrondi du corpus, pas un désaccord.
        ws.cell(row=l - 1, column=7,
                value=f'=IF(ABS(E{l - 1})<=F{l - 1},"juste","À VOIR")')
        ws.cell(row=l - 1, column=7).font = ENCRE
    l += 1
    ws.cell(row=l, column=1,
            value='Calculs hors tolérance — doit valoir zéro').font = FORT
    ws.cell(row=l, column=7,
            value=f'=COUNTIF(G5:G{l - 2},"À VOIR")').font = FORT
    ws.cell(row=l, column=7).number_format = ENT
    ws.cell(row=l, column=7).fill = OR
    return ws


# ------------------------------------------------------------------ la lecture
def onglet_lecture(wb):
    ws = feuille(wb, 'Lecture', "Classeur de synthèse budgétaire",
                 "", [110])
    textes = [
        ('Ce que ce classeur est', True),
        ("La vue de ce que le chantier a lu des classeurs sectoriels, et de ce "
         "qu'il en tire. Il se régénère par", False),
        ("appareil/generer_classeur_synthese.py et ne s'édite pas : une "
         "correction se porte à la grille de lecture,", False),
        ("jamais ici.", False),
        ('', False),
        ('Ce que ce classeur n’est pas', True),
        ("Une source. Les classeurs de l'auteur restent la source officielle du "
         "chiffrage. Celui-ci ne les remplace", False),
        ("pas, ne les corrige pas, et n'ajoute aucun chiffre qu'ils ne portent.",
         False),
        ('', False),
        ('Comment le lire', True),
        ("Couverture — ce qui est importé, lu, non lu. C'est un état, pas une "
         "déclaration.", False),
        ("Bouclages — ce que le socle recompose contre ce que le classeur "
         "affiche. Tant qu'une ligne ne boucle", False),
        ("  pas, la grille de lecture est fausse, et c'est la grille qu'on "
         "reprend.", False),
        ("Chaîne — les opérations du corpus, rejouées ici en formules.", False),
        ("Taxes affectées, Dépenses fiscales, Opérateurs, Budget général — le "
         "détail, du plus gros au plus petit.", False),
        ("Hypothèses — ce sous quoi tous ces chiffres valent.", False),
        ('', False),
        ('Deux mises en garde', True),
        ("Les cellules que le classeur d'origine porte en erreur sont reprises "
         "telles quelles.", False),
        ("Les opérateurs n'ont pas d'identifiant numérique : les fichiers s'y "
         "rattachent par le libellé, et", False),
        ("l'appariement mécanique n'en retrouve qu'une part. Le reste se tranche "
         "à la main.", False),
    ]
    l = 4
    for t, gras in textes:
        c = ws.cell(row=l, column=1, value=t)
        c.font = FORT if gras else ENCRE
        l += 1
    return ws


def generer(chemin_socle, chemin_chiffres, dst, chemin_recon=None,
            chemin_eco=None):
    socle = json.load(open(chemin_socle, encoding='utf-8'))
    recon = (json.load(open(chemin_recon, encoding='utf-8'))
             if chemin_recon else None)
    eco = (json.load(open(chemin_eco, encoding='utf-8'))
           if chemin_eco else None)
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    onglet_lecture(wb)
    onglet_couverture(wb)
    onglet_bouclages(wb, socle)
    onglet_chaine(wb)
    onglet_taxes(wb, socle)
    onglet_niches(wb, socle)
    onglet_operateurs(wb, socle)
    if recon:
        onglet_reconciliation(wb, recon)
    onglet_nomenclature(wb)
    onglet_budget(wb, socle)
    if eco:
        onglet_economies(wb, eco)
    onglet_hypotheses(wb)
    wb.save(dst)
    print(f"{dst} écrit — {len(wb.sheetnames)} onglets : "
          + ', '.join(wb.sheetnames))
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(2)
    sys.exit(generer(sys.argv[1], sys.argv[2], sys.argv[3],
                     sys.argv[4] if len(sys.argv) > 4 else None,
                     sys.argv[5] if len(sys.argv) > 5 else None))
