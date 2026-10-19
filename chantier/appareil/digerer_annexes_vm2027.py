#!/usr/bin/env python3
"""Digère les annexes des voies et moyens du PLF 2027 en référentiels plats.

Les classeurs sont des pièces jointes : documents publics, retéléchargeables à
l'identique, qui ne se versent pas (A-234, A-235). Ce qui se verse, c'est leur
table plate, seule forme de cette matière qui se lit sans outil (A-16, A-286).
Chaque table porte en tête l'empreinte SHA-256 du classeur dont elle sort.

- `referentiels/annexe_depenses_fiscales_2027.tsv` vient du tome II, annexe 1
  « Dépenses fiscales ». Elle porte une ligne par numéro de dépense fiscale.
  L'onglet « Chiffrages » fixe la population, et les onglets « Echéances »,
  « Bénéficiaires », « Méthodologie » et « Références juridiques » s'y joignent
  sur le numéro, à raison d'une ligne chacun. L'onglet « Programme de
  rattachement », à plusieurs lignes par numéro, se replie dans la colonne
  `programmes`. L'onglet « Modalités de calcul de l'impôt » porte des modalités
  déclassées et non des dépenses fiscales : il n'est pas digéré.
- `referentiels/annexe_ressources_affectees_2027.tsv` vient du tome I, annexe 2
  « Ressources affectées ». Elle porte une ligne par ligne de données de
  l'onglet unique, dans l'ordre du classeur.
- `referentiels/annexe_recettes_bg_2027.tsv` vient du tome I, annexe 1
  « Évolution des recettes du budget général ». Elle porte une ligne par ligne
  de données des trois onglets de détail — `RFN` les recettes fiscales nettes,
  `RNF` les non fiscales, `R&D` les remboursements et dégrèvements — repérée
  par la colonne `onglet`. Les onglets `*_format_courant` ne sont pas digérés :
  ils redisent les mêmes lignes à nomenclature constante, et la grammaire
  d'adresse du PLF 2027 est celle des onglets de détail. Les onglets de
  synthèse ne le sont pas non plus : `Recettes` agrège ce que `RFN` et `RNF`
  détaillent, et une somme se recompte, elle ne se verse pas.
- `referentiels/annexe_mesures_nouvelles_2027.tsv` vient du même classeur,
  onglet « MN au présent PLF ». Elle porte une ligne par mesure nouvelle, avec
  sa ligne budgétaire : c'est par elle qu'une mesure du corpus se raccroche à
  une recette, quand le texte déposé en porte déjà une du même objet.
- `referentiels/annexe_evolution_df_bilan_2027.tsv` vient du tome II, annexe 2
  « Évolution des dépenses fiscales », onglet « Bilan mesures 2026-2027 » : une
  ligne par mesure de création, d'augmentation, de diminution ou de suppression,
  avec son sort, le texte et l'article qui la portent, et son effet sur 2026 et
  2027. **Un signe positif est une économie.** C'est la pièce qui dit ce que le
  droit en vigueur et le texte déposé font déjà d'une dépense fiscale : une
  mesure du corpus qui vise une dépense déjà supprimée se raccroche ou tombe.
- `referentiels/annexe_evolution_df_bornees_2027.tsv` réunit les deux autres
  onglets du même classeur, de grammaire commune : les dépenses parvenues à
  échéance et celles dont le fait générateur est éteint, distinguées par la
  colonne `volet`. Pour les secondes, l'onglet range les dépenses sous l'année
  d'extinction, reportée en colonne `annee_extinction`.
- `referentiels/annexe_tva_apu_2027.tsv` vient du tome II, annexe 3 « TVA toutes
  APU ». Elle porte une ligne par mesure de TVA, dépense fiscale (`DF`) ou
  modalité particulière (`MP`), avec son coût toutes administrations publiques
  tel que chiffré au PLF 2026 puis au PLF 2027. C'est la seule pièce qui chiffre
  une mesure de TVA au-delà de la part État.
- `referentiels/annexe_indicateurs_performance_2027.tsv` vient du tome II,
  annexe 4. L'onglet est en blocs : un indicateur, sa mission, son programme,
  puis les dépenses fiscales qu'il mesure, chacune suivie de son impôt. La table
  aplatit le bloc en **une ligne par couple indicateur × dépense fiscale**, et
  reporte mission et programme sur chacune.
- `referentiels/annexe_deciles_ir_2027.tsv` vient du tome II, annexe 5, onglet
  « Top 8 Dfi IR » : une ligne par dépense fiscale d'impôt sur le revenu dont la
  distribution est publiée.
- `referentiels/annexe_deciles_ir_repartition_2027.tsv` vient des autres onglets
  du même classeur, un par dépense fiscale : une ligne par tranche de revenu
  fiscal de référence, repérée par `numero_df`. La ligne `TOTAL` de chaque
  onglet sert de contrôle et ne se verse pas. **Toutes les dépenses du « Top 8 »
  n'ont pas d'onglet de répartition** : l'écart se relève, il ne se comble pas.

Ce classeur-ci est au format `xlsx` et se lit par `openpyxl` ; les deux autres
sont au format `xls` et se lisent par `xlrd`. Le format se déduit du suffixe du
chemin, jamais d'un argument.

Les cellules sont reprises **au verbatim** : aucun libellé n'est normalisé, ni
espace ni espace insécable. Un nombre entier s'écrit sans décimale. Un nombre
non entier s'écrit sous sa forme la plus courte qui se relit à l'identique. Les
montants restent dans l'unité du classeur : M€ pour les dépenses fiscales, euros
pour les ressources affectées. Les symboles de l'annexe (« - », « ε », « nc »)
sont repris tels quels. Une tabulation, un retour à la ligne ou une barre
oblique inverse se notent `\\t`, `\\n`, `\\r` et `\\\\` : l'échappement est
réversible, et `lire()` rend la cellule au verbatim.

Usage :
    python3 appareil/digerer_annexes_vm2027.py ecrire   [--df X] [--ra Y] [--rb Z] [--ev E] [--tva T] [--ind I] [--dec D]
    python3 appareil/digerer_annexes_vm2027.py verifier  [--df X] [--ra Y] [--rb Z] [--ev E] [--tva T] [--ind I] [--dec D]

`methode/annexes_voies_et_moyens_2027.md` tient le registre des annexes : pour
chacune, son profil, sa table, son empreinte et son état.

Chaque classeur passé rend ses tables ; un classeur absent laisse les siennes
intactes, et `verifier` ne se prononce pas sur elles. Les deux classeurs du
premier appel se passent aussi en positionnel, dans l'ordre `DF` puis `RA`.

`verifier` régénère les tables en mémoire et les compare **à l'octet** aux
tables versées. Il joue ensuite son jeu de fautes, et sort en échec si une table
diverge ou si une faute ne mord pas.
"""

import hashlib
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(ICI, '..', 'referentiels')
SORTIE_DF = os.path.join(REF, 'annexe_depenses_fiscales_2027.tsv')
SORTIE_RA = os.path.join(REF, 'annexe_ressources_affectees_2027.tsv')
SORTIE_RB = os.path.join(REF, 'annexe_recettes_bg_2027.tsv')
SORTIE_MN = os.path.join(REF, 'annexe_mesures_nouvelles_2027.tsv')
SORTIE_EVB = os.path.join(REF, 'annexe_evolution_df_bilan_2027.tsv')
SORTIE_EVE = os.path.join(REF, 'annexe_evolution_df_bornees_2027.tsv')
SORTIE_TVA = os.path.join(REF, 'annexe_tva_apu_2027.tsv')
SORTIE_IND = os.path.join(REF, 'annexe_indicateurs_performance_2027.tsv')
SORTIE_DEC = os.path.join(REF, 'annexe_deciles_ir_2027.tsv')
SORTIE_REP = os.path.join(REF, 'annexe_deciles_ir_repartition_2027.tsv')

# onglet : (première ligne de données, index 0 ; {colonne : index de cellule})
DF_FEUILLES = {
    'Chiffrages': (4, {'categorie': 0, 'sous_categorie': 1, 'sous_sous_categorie': 2,
                       'libelle': 4, 'realisation_2025': 5, 'prevision_2026': 6,
                       'prevision_2027': 7}),
    'Echéances': (4, {'creation': 5, 'derniere_modification': 6, 'fin_fait_generateur': 7,
                      'fin_incidence_budgetaire': 8, 'suppression': 9,
                      'creation_suppression_posterieure': 10,
                      'motif_creation_suppression': 11}),
    'Bénéficiaires': (2, {'beneficiaire_nature': 5, 'beneficiaire_nombre': 6}),
    'Méthodologie': (2, {'fiabilite_du_realise': 5, 'methode_de_chiffrage': 6,
                         'changement_de_methode': 7}),
    'Références juridiques': (2, {'norme_de_reference': 5, 'code': 6, 'reference': 7}),
}
DF_COLONNES = ['numero'] + [c for _, (_, cols) in DF_FEUILLES.items() for c in cols] + \
              ['programmes', 'ligne_chiffrages']

RA_COLONNES = ['secteur', 'categorie_repartition', 'nature_juridique', 'siren', 'programme',
               'rattachement_mission', 'rattachement_programme', 'code_affectation',
               'beneficiaire_code', 'beneficiaire_libelle', 'ressource_code', 'ressource_libelle',
               'execution_2025', 'plafond_2025', 'reversement_bg_2025',
               'rendement_previsionnel_2026', 'plafond_2026', 'reversement_bg_2026',
               'rendement_previsionnel_2027', 'plafond_2027', 'reversement_bg_2027',
               'debut_plafonnement', 'reference_juridique']
RA_PREMIERE = 4

# Les trois onglets de détail de l'annexe 1 partagent une seule grammaire : la
# ligne budgétaire en B, la désignation en C, puis huit colonnes de montants.
RB_FEUILLES = ('RFN', 'RNF', 'R&D')
RB_COLONNES = ['onglet', 'ligne', 'designation', 'execution_2025',
               'evaluation_initiale_2026_lfi', 'evaluation_revisee_2026_plf2027',
               'effet_evolution_spontanee', 'mesures_anterieures',
               'mesures_nouvelles', 'mesures_perimetre_transfert',
               'evaluation_proposee_2027']
RB_PREMIERE = 4          # index 0 ; les quatre premières lignes sont l'en-tête
RB_CELLULES = range(1, 11)

EVB_FEUILLE = 'Bilan mesures 2026-2027'
EVB_COLONNES = ['impot', 'numero', 'libelle', 'sort', 'texte', 'article', 'nature',
                'effet_2026', 'effet_2027']
EVE_FEUILLES = {'DFi parvenues à échéance': 'echeance',
                'DFI fait générateur éteint': 'fait_generateur_eteint'}
EVE_COLONNES = ['volet', 'annee_extinction', 'impot', 'numero', 'libelle',
                'cout_2025', 'cout_2026', 'cout_2027']
NUMERO_DF = re.compile(r'\d{5,6}')      # le dégrèvement 70201 n'en porte que cinq

TVA_FEUILLE = 'DF et MP coût TVA APU'
TVA_COLONNES = ['type', 'numero', 'libelle',
                'cout_plf2026_2024', 'cout_plf2026_2025', 'cout_plf2026_2026',
                'cout_plf2027_2025', 'cout_plf2027_2026', 'cout_plf2027_2027']
TVA_PREMIERE = 3
TVA_CELLULES = range(0, 9)

IND_FEUILLE = 'Indicateurs'
IND_COLONNES = ['numero_indicateur', 'libelle_indicateur', 'mission', 'programme',
                'numero_df', 'libelle_df', 'impot']
IND_PREMIERE = 4

DEC_FEUILLE = 'Top 8 Dfi IR'
DEC_COLONNES = ['numero_df', 'impot', 'libelle', 'cout_2025', 'cout_2026', 'cout_2027',
                'beneficiaires_2025', 'commentaire']
DEC_PREMIERE = 2
DEC_CELLULES = range(0, 8)

REP_COLONNES = ['numero_df', 'millesime_revenus', 'borne_inferieure_rfr',
                'borne_superieure_rfr', 'foyers_concernes', 'cout_M', 'controle_bloc']
REP_SOURCE = re.compile(r'fichier des revenus\s+(\d{4})', re.I)

MN_FEUILLE = 'MN au présent PLF'
MN_COLONNES = ['impot', 'ligne_budgetaire', 'libelle', 'nature', 'montant_2027']
MN_PREMIERE = 3
MN_CELLULES = range(1, 6)


def cellule(v):
    if v is None:          # une cellule vide d'un classeur xlsx ; xlrd rend '' et n'y passe pas
        return ''
    if isinstance(v, bool) or not isinstance(v, (int, float, str)):
        raise ValueError(f'cellule de type inattendu : {type(v).__name__}')
    if isinstance(v, float):
        return str(int(v)) if v == int(v) else repr(v)
    return (str(v).replace('\\', '\\\\').replace('\t', '\\t')
            .replace('\n', '\\n').replace('\r', '\\r'))


ECHAPPES = {'\\\\': '\\', '\\t': '\t', '\\n': '\n', '\\r': '\r'}


def restituer(c):
    """Défait l'échappement de `cellule` : rend la cellule au verbatim."""
    return re.sub(r'\\[\\tnr]', lambda m: ECHAPPES[m.group(0)], c)


def lire(chemin):
    """Relit une table digérée : (empreinte de la pièce, lignes en dictionnaires, au verbatim)."""
    sha, cols, lignes = None, None, []
    for l in open(chemin, encoding='utf-8').read().split('\n'):
        if l.startswith('# pièce : sha256 '):
            sha = l.rsplit(' ', 1)[1]
        elif not l or l.startswith('#'):
            continue
        elif cols is None:
            cols = l.split('\t')
        else:
            lignes.append(dict(zip(cols, (restituer(c) for c in l.split('\t')))))
    return sha, lignes


def empreinte(chemin):
    return hashlib.sha256(open(chemin, 'rb').read()).hexdigest()


def classeur(chemin):
    import xlrd  # seule la lecture du classeur en a besoin : `lire()` s'en passe
    return xlrd.open_workbook(chemin, logfile=open(os.devnull, 'w'))


def grille(chemin, nom):
    """Rend un onglet en liste de lignes de cellules brutes, quel que soit le format.

    Un `xlsx` se lit par `openpyxl`, un `xls` par `xlrd`. Les lignes d'un `xlsx`
    sont raccourcies à droite : on les complète pour que tout index de cellule
    nommé plus haut existe, et qu'une colonne vide en bout d'onglet ne décale rien.
    """
    if chemin.lower().endswith('.xlsx'):
        import openpyxl
        ws = openpyxl.load_workbook(chemin, data_only=True, read_only=True)[nom]
        lignes = [[c.value for c in r] for r in ws.iter_rows()]
        large = max((len(r) for r in lignes), default=0)
        return [r + [None] * (large - len(r)) for r in lignes]
    ws = classeur(chemin).sheet_by_name(nom)
    return [ws.row_values(r) for r in range(ws.nrows)]


def table_df(chemin):
    wb = classeur(chemin)
    lignes, ordre = {}, []
    for nom, (debut, cols) in DF_FEUILLES.items():
        ws = wb.sheet_by_name(nom)
        for r in range(debut, ws.nrows):
            n = cellule(ws.cell_value(r, 3))
            if not n:
                continue
            if nom == 'Chiffrages':
                lignes[n] = {'numero': n, 'ligne_chiffrages': str(r + 1)}
                ordre.append(n)
            elif n not in lignes:
                raise ValueError(f'{nom} : numéro {n} absent de « Chiffrages »')
            for c, i in cols.items():
                if c in lignes[n]:
                    raise ValueError(f'{nom} : numéro {n} en double')
                lignes[n][c] = cellule(ws.cell_value(r, i))
    ws = wb.sheet_by_name('Programme de rattachement')
    prog = {}
    for r in range(4, ws.nrows):
        n = cellule(ws.cell_value(r, 3))
        if n:
            prog.setdefault(n, []).append(f'{cellule(ws.cell_value(r, 5))} ({cellule(ws.cell_value(r, 7))})')
    for n in ordre:
        lignes[n]['programmes'] = ' ; '.join(prog.get(n, []))
        manque = [c for c in DF_COLONNES if c not in lignes[n]]
        if manque:
            raise ValueError(f'numéro {n} : colonnes absentes {manque}')
    entete = [
        '# ANNEXE DES DÉPENSES FISCALES — PLF 2027, voies et moyens, tome II, annexe 1',
        f'# pièce : sha256 {empreinte(chemin)}',
        '# digérée par appareil/digerer_annexes_vm2027.py ; montants en M€, symboles de l\'annexe repris',
        f'# {len(ordre)} dépenses fiscales · une ligne par numéro',
        '# colonnes : ' + '<TAB>'.join(DF_COLONNES),
        '#',
        '\t'.join(DF_COLONNES),
    ]
    return '\n'.join(entete + ['\t'.join(lignes[n][c] for c in DF_COLONNES) for n in ordre]) + '\n'


def table_ra(chemin):
    ws = classeur(chemin).sheet_by_name('Ressources affectées')
    if ws.ncols != len(RA_COLONNES):
        raise ValueError(f'{ws.ncols} colonnes au classeur, {len(RA_COLONNES)} attendues')
    corps = []
    for r in range(RA_PREMIERE, ws.nrows):
        row = [cellule(v) for v in ws.row_values(r)]
        if any(row):
            corps.append('\t'.join(row + [str(r + 1)]))
    cols = RA_COLONNES + ['ligne_classeur']
    entete = [
        '# ANNEXE DES RESSOURCES AFFECTÉES — PLF 2027, voies et moyens, tome I, annexe 2',
        f'# pièce : sha256 {empreinte(chemin)}',
        '# digérée par appareil/digerer_annexes_vm2027.py ; montants en euros, cellules au verbatim',
        f'# {len(corps)} lignes · une ligne par ligne de données de l\'onglet « Ressources affectées »',
        '# colonnes : ' + '<TAB>'.join(cols),
        '#',
        '\t'.join(cols),
    ]
    return '\n'.join(entete + corps) + '\n'


def table_rb(chemin):
    corps = []
    for nom in RB_FEUILLES:
        lignes = grille(chemin, nom)
        tete = [cellule(v) for v in lignes[2]]
        if tete[1] != 'Ligne' or tete[2] != 'Désignation des recettes':
            raise ValueError(f'{nom} : en-tête inattendu {tete[1:3]}')
        for r in range(RB_PREMIERE, len(lignes)):
            row = [cellule(lignes[r][i]) for i in RB_CELLULES]
            if any(row):
                corps.append('\t'.join([nom] + row + [str(r + 1)]))
    cols = RB_COLONNES + ['ligne_classeur']
    entete = [
        '# ANNEXE DES RECETTES DU BUDGET GÉNÉRAL — PLF 2027, voies et moyens, tome I, annexe 1',
        f'# pièce : sha256 {empreinte(chemin)}',
        "# digérée par appareil/digerer_annexes_vm2027.py ; montants en euros, cellules au verbatim",
        f'# {len(corps)} lignes · onglets de détail {", ".join(RB_FEUILLES)}, dans leur ordre',
        '# colonnes : ' + '<TAB>'.join(cols),
        '#',
        '\t'.join(cols),
    ]
    return '\n'.join(entete + corps) + '\n'


def table_mn(chemin):
    lignes = grille(chemin, MN_FEUILLE)
    tete = [cellule(v) for v in lignes[2]]
    if tete[1] != 'Impôt' or tete[2] != 'Ligne budgétaire':
        raise ValueError(f'{MN_FEUILLE} : en-tête inattendu {tete[1:3]}')
    corps, somme, total = [], 0, None
    for r in range(MN_PREMIERE, len(lignes)):
        row = [cellule(lignes[r][i]) for i in MN_CELLULES]
        if not any(row):
            continue
        # L'onglet se clôt sur sa propre somme. Une somme se recompte, elle ne se
        # verse pas : la ligne sert de contrôle et sort de la table.
        if not row[1] and row[0].startswith('Mesures nouvelles'):
            total = float(row[4])
            continue
        somme += float(row[4]) if row[4] else 0
        corps.append('\t'.join(row + [str(r + 1)]))
    if total is None:
        raise ValueError(f'{MN_FEUILLE} : ligne de total absente')
    if abs(total - somme) > 0.5:
        raise ValueError(f'{MN_FEUILLE} : total {total:.0f} contre {somme:.0f} recomptés')
    cols = MN_COLONNES + ['ligne_classeur']
    entete = [
        '# MESURES NOUVELLES DU PRÉSENT PLF — PLF 2027, voies et moyens, tome I, annexe 1',
        f'# pièce : sha256 {empreinte(chemin)}',
        "# digérée par appareil/digerer_annexes_vm2027.py ; montants en euros, cellules au verbatim",
        f'# {len(corps)} mesures · total de l\'onglet {total:.0f} €, recompté sur ces lignes',
        '# colonnes : ' + '<TAB>'.join(cols),
        '#',
        '\t'.join(cols),
    ]
    return '\n'.join(entete + corps) + '\n'


def entete(titre, chemin, unite, compte, cols):
    return [
        titre,
        f'# pièce : sha256 {empreinte(chemin)}',
        f'# digérée par appareil/digerer_annexes_vm2027.py ; {unite}, cellules au verbatim',
        f'# {compte}',
        '# colonnes : ' + '<TAB>'.join(cols),
        '#',
        '\t'.join(cols),
    ]


def table_evb(chemin):
    """Le bilan des mesures. Les trois totaux de pied contrôlent, ils ne se versent pas."""
    lignes = grille(chemin, EVB_FEUILLE)
    tete = [cellule(v) for v in lignes[1]]
    if tete[0] != 'Impôt' or tete[3] != 'Sort':
        raise ValueError(f'{EVB_FEUILLE} : en-tête inattendu {tete[:4]}')
    corps, totaux = [], {}
    for r in range(2, len(lignes)):
        row = [cellule(lignes[r][i]) for i in range(9)]
        if NUMERO_DF.fullmatch(row[1].strip()):
            corps.append('\t'.join(row + [str(r + 1)]))
        elif row[0].upper().startswith(('TOTAL DES SUPPRESSIONS', 'TOTAL DES CREATIONS', 'SOLDE')):
            totaux[row[0].split('*')[0].strip()] = (nombre(row[7]), nombre(row[8]))
    if len(totaux) != 3:
        raise ValueError(f'{EVB_FEUILLE} : {len(totaux)} totaux de pied, trois attendus')
    etat = []
    for annee, i in (('2026', 0), ('2027', 1)):
        vus = [nombre(l.split('\t')[7 + i]) for l in corps]
        plus = sum(v for v in vus if v and v > 0)
        moins = sum(v for v in vus if v and v < 0)
        dits = {k: v[i] for k, v in totaux.items()}
        sup = next(v for k, v in dits.items() if k.startswith('TOTAL DES SUPPRESSIONS'))
        cre = next(v for k, v in dits.items() if k.startswith('TOTAL DES CREATIONS'))
        sol = next(v for k, v in dits.items() if k.startswith('SOLDE'))
        verdict = ('concorde' if abs(sup - plus) <= 1 and abs(cre - moins) <= 1
                   and abs(sol - (sup + cre)) <= 1 else 'ECART')
        etat.append(f'{annee} suppressions {sup:+.0f} / recomptées {plus:+.0f} · '
                    f'créations {cre:+.0f} / recomptées {moins:+.0f} · solde {sol:+.0f} ({verdict})')
    cols = EVB_COLONNES + ['ligne_classeur']
    return '\n'.join(entete(
        '# ÉVOLUTION DES DÉPENSES FISCALES, BILAN DES MESURES — PLF 2027, voies et moyens, tome II, annexe 2',
        chemin, "effets en M€, signe positif = économie, symboles de l'annexe repris",
        f'{len(corps)} mesures · onglet « {EVB_FEUILLE} »', cols)[:-1]
        + ['# contrôle : ' + ' | '.join(etat), '#', '\t'.join(cols)] + corps) + '\n'


def table_eve(chemin):
    """Les dépenses bornées : échéance atteinte, ou fait générateur éteint.

    Le second onglet range ses dépenses sous l'année d'extinction, portée seule
    en première cellule. L'année se reporte sur les lignes qui la suivent ; une
    dépense rencontrée avant toute année arrête la digestion.
    """
    corps, controles = [], []
    for feuille, volet in EVE_FEUILLES.items():
        lignes = grille(chemin, feuille)
        tete = [cellule(v) for v in lignes[1]]
        if tete[0] != 'Impôt' or not tete[2].startswith('Dépenses fiscales'):
            raise ValueError(f'{feuille} : en-tête inattendu {tete[:3]}')
        annee, vus, total = '', {}, None
        for r in range(2, len(lignes)):
            row = [cellule(lignes[r][i]) for i in range(6)]
            a, n = row[0].strip(), row[1].strip()
            if NUMERO_DF.fullmatch(n):
                if volet == 'fait_generateur_eteint' and not annee:
                    raise ValueError(f'{feuille} ligne {r + 1} : dépense hors année d’extinction')
                corps.append('\t'.join([volet, annee] + row + [str(r + 1)]))
                for i in range(3, 6):
                    vus[i] = vus.get(i, 0) + (nombre(row[i]) or 0)
            elif re.fullmatch(r'\d{4}', a) and not n:
                annee = a
            elif a.upper() == 'TOTAL':
                total = [nombre(row[i]) for i in range(3, 6)]
        if total is None:
            raise ValueError(f'{feuille} : ligne de total absente')
        ecarts = [str(2022 + i) for i in range(3, 6)
                  if abs((total[i - 3] or 0) - vus.get(i, 0)) > 1]
        controles.append(f'{volet} : total {"/".join(f"{t:.0f}" for t in total)} ; '
                         f'recompté {"/".join(f"{vus.get(i, 0):.0f}" for i in range(3, 6))}'
                         + (f' — ÉCART sur {", ".join(ecarts)}' if ecarts else ' — concorde'))
    cols = EVE_COLONNES + ['ligne_classeur']
    return '\n'.join(entete(
        '# ÉVOLUTION DES DÉPENSES FISCALES, DÉPENSES BORNÉES — PLF 2027, voies et moyens, tome II, annexe 2',
        chemin, "coûts en M€, symboles de l'annexe repris",
        f'{len(corps)} dépenses · onglets « ' + ' » et « '.join(EVE_FEUILLES) + ' »',
        cols)[:-1] + ['# contrôle : ' + ' | '.join(controles), '#', '\t'.join(cols)] + corps) + '\n'


def table_tva(chemin):
    lignes = grille(chemin, TVA_FEUILLE)
    tete = [cellule(v) for v in lignes[2]]
    if tete[0] != 'DF' or tete[2] != 'Libellé de la mesure':
        raise ValueError(f'{TVA_FEUILLE} : en-tête inattendu {tete[:3]}')
    corps = []
    for r in range(TVA_PREMIERE, len(lignes)):
        row = [cellule(lignes[r][i]) for i in TVA_CELLULES]
        if any(row):
            corps.append('\t'.join(row + [str(r + 1)]))
    cols = TVA_COLONNES + ['ligne_classeur']
    return '\n'.join(entete(
        '# TVA TOUTES APU — PLF 2027, voies et moyens, tome II, annexe 3',
        chemin, "coûts en M€, symboles de l'annexe repris",
        f"{len(corps)} mesures · onglet « {TVA_FEUILLE} »", cols) + corps) + '\n'


def table_ind(chemin):
    """Aplatit les blocs de l'annexe 4 en couples indicateur × dépense fiscale.

    Un bloc s'ouvre sur une ligne qui porte un numéro d'indicateur en deuxième
    cellule. Suivent la mission, le programme, puis les dépenses fiscales, chacune
    repérée par un numéro de six chiffres et suivie de la ligne qui nomme son
    impôt. Toute ligne qui ne se range pas dans cette forme arrête la digestion :
    une forme inattendue se relève, elle ne se devine pas.
    """
    lignes = grille(chemin, IND_FEUILLE)
    tete = [cellule(v) for v in lignes[1]]
    if tete[1] != 'Numéro' or tete[2] != 'Indicateur de performance':
        raise ValueError(f'{IND_FEUILLE} : en-tête inattendu {tete[1:3]}')
    corps, bloc, df = [], None, None

    def clore():
        if df and not df['impot']:
            raise ValueError(f"dépense fiscale {df['numero_df']} sans impôt")

    for r in range(IND_PREMIERE, len(lignes)):
        b, c = cellule(lignes[r][1]).strip(), cellule(lignes[r][2]).strip()
        if not b and not c:
            continue
        if re.fullmatch(r'\d{6}', b):                        # une dépense fiscale
            if bloc is None:
                raise ValueError(f'ligne {r + 1} : dépense fiscale hors indicateur')
            clore()
            df = dict(bloc, numero_df=b, libelle_df=c, impot='')
            corps.append((df, r + 1))
        elif b:                                              # un indicateur neuf
            clore()
            bloc, df = {'numero_indicateur': b, 'libelle_indicateur': c,
                        'mission': '', 'programme': ''}, None
        elif c.startswith('Mission'):
            bloc['mission'] = c
        elif c.startswith('Programme'):
            bloc['programme'] = c
        elif df is not None and not df['impot']:
            df['impot'] = c
        else:
            raise ValueError(f'ligne {r + 1} : forme non reconnue « {c[:60]} »')
    clore()
    cols = IND_COLONNES + ['ligne_classeur']
    indicateurs = len({d['numero_indicateur'] for d, _ in corps})
    return '\n'.join(entete(
        '# INDICATEURS DE PERFORMANCE — PLF 2027, voies et moyens, tome II, annexe 4',
        chemin, 'sans montant', f'{len(corps)} couples · {indicateurs} indicateurs', cols)
        + ['\t'.join([d[c] for c in IND_COLONNES] + [str(l)]) for d, l in corps]) + '\n'


def table_dec(chemin):
    lignes = grille(chemin, DEC_FEUILLE)
    tete = [cellule(v) for v in lignes[1]]
    if tete[0] != 'Dépense fiscale' or tete[1] != 'Impôt':
        raise ValueError(f'{DEC_FEUILLE} : en-tête inattendu {tete[:2]}')
    corps = []
    for r in range(DEC_PREMIERE, len(lignes)):
        row = [cellule(lignes[r][i]) for i in DEC_CELLULES]
        if re.fullmatch(r'\d{6}', row[0].strip()):
            corps.append('\t'.join(row + [str(r + 1)]))
    cols = DEC_COLONNES + ['ligne_classeur']
    return '\n'.join(entete(
        '# DÉPENSES FISCALES D’IR VENTILÉES — PLF 2027, voies et moyens, tome II, annexe 5',
        chemin, "coûts en M€, symboles de l'annexe repris",
        f"{len(corps)} dépenses fiscales · onglet « {DEC_FEUILLE} »", cols) + corps) + '\n'


def table_rep(chemin):
    """Les onglets de répartition, un par dépense fiscale.

    Chaque onglet porte **plusieurs ventilations**, une par millésime du fichier
    des revenus : un en-tête « Borne inférieure », dix tranches, un `TOTAL`, puis
    la ligne « Source : … fichier des revenus AAAA » qui donne le millésime. Les
    tranches d'un millésime ne s'additionnent pas à celles d'un autre : le
    millésime fait partie de la clé. Le `TOTAL` contrôle son bloc et ne se verse
    pas ; l'écart toléré est celui des arrondis du classeur, une demi-unité par
    tranche. Un bloc sans `TOTAL` ou sans millésime arrête la digestion.
    """
    import openpyxl
    noms = [n for n in openpyxl.load_workbook(chemin, read_only=True).sheetnames
            if re.fullmatch(r'\d{6}', n)]
    if not noms:
        raise ValueError('aucun onglet de répartition')
    corps, blocs = [], []
    for nom in noms:
        lignes = grille(chemin, nom)
        bloc = None
        for r in range(len(lignes)):
            row = [cellule(lignes[r][i]) if i < len(lignes[r]) else '' for i in range(4)]
            tete = row[0].strip()
            if tete.startswith('Borne inférieure'):
                if bloc is not None:
                    raise ValueError(f'{nom} ligne {r + 1} : ventilation ouverte sur une autre')
                bloc = {'tranches': [], 'total': None, 'millesime': None}
            elif bloc is None:
                continue
            elif tete == 'TOTAL':
                bloc['total'] = (nombre(row[2]), nombre(row[3]))
            elif nombre(row[2]) is not None:
                # Une tranche se reconnaît à son nombre de foyers, non à sa borne
                # inférieure : celle de la première tranche est parfois laissée vide.
                bloc['tranches'].append((row, r + 1))
            elif bloc['total'] is not None:
                m = REP_SOURCE.search(restituer(row[0]))
                if not m:
                    continue                    # note de chiffrage ; la source suit
                bloc['millesime'] = m.group(1)
                ecarts = verifier_bloc(nom, bloc)
                verdict = 'concorde' if not ecarts else 'ecart:' + ','.join(ecarts)
                for row_t, ligne in bloc['tranches']:
                    corps.append('\t'.join([nom, bloc['millesime']] + row_t[:4]
                                           + [verdict, str(ligne)]))
                blocs.append((nom, bloc, ecarts))
                bloc = None
        if bloc is not None:
            raise ValueError(f'{nom} : dernière ventilation sans millésime')
    cols = REP_COLONNES + ['ligne_classeur']
    millesimes = sorted({b['millesime'] for _, b, _ in blocs})
    fautifs = [f"{nom} {b['millesime']} ({'+'.join(e)})" for nom, b, e in blocs if e]
    etat = ('tous les TOTAUX concordent' if not fautifs else
            f"{len(fautifs)} ventilation(s) en écart au classeur : {' · '.join(fautifs)}")
    return '\n'.join(entete(
        '# RÉPARTITION PAR REVENU FISCAL DE RÉFÉRENCE — PLF 2027, voies et moyens, tome II, annexe 5',
        chemin, 'coûts en M€',
        f'{len(corps)} tranches · {len(noms)} dépenses ventilées ({", ".join(noms)}) '
        f'× {len(millesimes)} millésimes de revenus ({", ".join(millesimes)})',
        cols)[:-1] + [f'# contrôle : {etat}', '#', '\t'.join(cols)] + corps) + '\n'


def verifier_bloc(nom, bloc):
    """Recompte le TOTAL d'une ventilation. Rend la liste des colonnes en écart.

    Un écart ne bloque pas : il vient du classeur, qui donne pour une ventilation
    un total en euros là où ses tranches sont en M€. La digestion ne corrige
    aucun chiffre — elle verse le verbatim et porte le verdict sur chaque ligne.
    """
    n = len(bloc['tranches'])
    if not n:
        raise ValueError(f'{nom} : ventilation sans tranche')
    if bloc['total'] is None:
        raise ValueError(f'{nom} : ventilation sans TOTAL')
    ecarts = []
    for i, colonne in ((2, 'foyers'), (3, 'cout')):
        somme = sum(nombre(row[i]) or 0 for row, _ in bloc['tranches'])
        attendu = bloc['total'][i - 2]
        if attendu is None:
            raise ValueError(f'{nom} : TOTAL sans {colonne}')
        if abs(attendu - somme) > max(0.5 * n, 1e-6 * abs(attendu)):
            ecarts.append(colonne)
    return ecarts


def nombre(c):
    try:
        return float(restituer(c).replace(' ', '').replace(' ', ''))
    except ValueError:
        return None


def comparer(attendu, verse):
    """Réapplication : la table versée doit être celle que redonne le classeur, à l'octet."""
    if attendu == verse:
        return []
    a, v = attendu.split('\n'), verse.split('\n')
    ecarts = [(i + 1, x, y) for i, (x, y) in enumerate(zip(a, v)) if x != y]
    if len(a) != len(v):
        ecarts.append(('compte', len(a), len(v)))
    return ecarts


def fautes(texte):
    L = texte.split('\n')
    # La première ligne non commentée porte les colonnes ; la faute se joue sur la
    # suivante. Compter les lignes d'en-tête casse dès qu'une table en porte une de
    # plus — corrigé le 20261019, après l'ajout du pied de contrôle de l'annexe 5.
    i = next(k for k, l in enumerate(L) if l and not l.startswith('#')) + 1
    def mut(f):
        M = list(L); f(M); return '\n'.join(M)
    def valeur(M):
        c = M[i].split('\t'); j = next(k for k, x in enumerate(c) if x.isdigit() and k > 0)
        c[j] = str(int(c[j]) + 1); M[i] = '\t'.join(c)
    return {
        '1 valeur fausse au même repère': mut(valeur),
        '2 empreinte de pièce altérée': mut(lambda M: M.__setitem__(1, M[1][:-1] + ('0' if M[1][-1] != '0' else '1'))),
        '3 ligne retirée': mut(lambda M: M.pop(i)),
        '4 libellé normalisé (espace insécable rendue simple)': mut(lambda M: M.__setitem__(i, M[i].replace(' ', ' ') if ' ' in M[i] else M[i] + ' ')),
    }


def chemins(argv):
    """Rend {profil : chemin de classeur} ; positionnels anciens = df puis ra."""
    choix, reste, i = {}, [], 0
    while i < len(argv):
        if argv[i] in ('--df', '--ra', '--rb', '--tva', '--ind', '--dec', '--ev'):
            choix[argv[i][2:]] = argv[i + 1]
            i += 2
        else:
            reste.append(argv[i])
            i += 1
    for profil, chemin in zip(('df', 'ra'), reste):
        choix.setdefault(profil, chemin)
    if not choix:
        raise SystemExit('aucun classeur passé : --df, --ra, --rb, --ev, --tva, --ind ou --dec')
    return choix


def main(argv):
    mode = argv[1]
    choix = chemins(argv[2:])
    tables = []
    if 'df' in choix:
        tables.append((SORTIE_DF, table_df(choix['df'])))
    if 'ra' in choix:
        tables.append((SORTIE_RA, table_ra(choix['ra'])))
    if 'rb' in choix:
        tables.append((SORTIE_RB, table_rb(choix['rb'])))
        tables.append((SORTIE_MN, table_mn(choix['rb'])))
    if 'ev' in choix:
        tables.append((SORTIE_EVB, table_evb(choix['ev'])))
        tables.append((SORTIE_EVE, table_eve(choix['ev'])))
    if 'tva' in choix:
        tables.append((SORTIE_TVA, table_tva(choix['tva'])))
    if 'ind' in choix:
        tables.append((SORTIE_IND, table_ind(choix['ind'])))
    if 'dec' in choix:
        tables.append((SORTIE_DEC, table_dec(choix['dec'])))
        tables.append((SORTIE_REP, table_rep(choix['dec'])))
    if mode == 'ecrire':
        for chemin, texte in tables:
            open(chemin, 'w', encoding='utf-8', newline='').write(texte)
            print(f'{os.path.relpath(chemin, os.path.join(ICI, ".."))} : {texte.count(chr(10)) - 7} lignes')
        return 0
    ok = True
    for chemin, texte in tables:
        verse = open(chemin, encoding='utf-8', newline='').read()
        e = comparer(texte, verse)
        nom = os.path.basename(chemin)
        print(f'{nom} : ' + ('identique au classeur, à l\'octet' if not e else f'{len(e)} écart(s) {e[:2]}'))
        ok &= not e
        for f, t in fautes(verse).items():
            mord = bool(comparer(texte, t))
            print(f"  faute {f} : {'mord' if mord else 'NE MORD PAS'}")
            ok &= mord
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
