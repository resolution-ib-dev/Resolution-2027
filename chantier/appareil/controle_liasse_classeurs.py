#!/usr/bin/env python3
"""Contrôle de la liasse de crédits contre les classeurs du site — 20261116.

Trois commandes, un seul fichier :

  construire <Dépenses de l'État.xls> <Synthèse des chiffrages.xlsx>
      relit les deux classeurs (valeurs en cache, xlrd ; le .xls n'est jamais
      réenregistré), le registre § 4, les trois autres documents de calendrier,
      l'état B 2027 et la liasse, et écrit
      `referentiels/parametres_credits_20261116.tsv`.

  controler [--cible classeur|registre|mixte|projet|liasse]
      rejoue la comparaison depuis le TSV et la liasse, sans aucun classeur.
      Sort en échec (code 1) dès qu'un amendement s'écarte du paramètre.
        classeur  brut × taux du classeur × part de première année  (défaut)
        registre  chaîne du § 1 du registre sur les paramètres du § 4
        mixte     taux et rythme du classeur × part d'année de la date du § 4,
                  CP au résiduel du § 3
        projet    la règle retenue le 20261116 : brut × taux du classeur ×
                  rythme du § 4 × fraction d'exercice du § 4, CP au résiduel
                  du § 3 ; taux et rythme du classeur là où le registre est
                  muet. C'est la cible de la liasse régénérée : 0 échec.
        liasse    brut × fraction de l'ancien `chaine_credits.py` : la règle
                  d'avant le 20261116, que la liasse régénérée ne suit plus.

  faute
      injecte une faute de 1 000 € dans une ligne de la liasse lue en mémoire
      et exige que le contrôle, cible `projet`, la morde.

  ecarts
      imprime en markdown les tables du document des écarts.

  reperes
      rejoue les repères `A!Kn/Ln` du § 14 du registre sur l'onglet
      « A — Crédits » du classeur de suivi, versé en texte le 20261116.

Les colonnes `regle_*`, `retenu`, `amendement_mission` et `etatB_2027_*` du
TSV sont la table de paramètres que lisent `chaine_credits.py` et
`generer_liasse_p2.py`. Ce fichier ne modifie ni la liasse ni aucun classeur.
"""
import csv, re, sys, unicodedata
from collections import defaultdict, OrderedDict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TSV = RACINE / 'referentiels/parametres_credits_20261116.tsv'
LIASSE = RACINE / 'livrables/depot_2027/LIASSE_PLF_P2.md'
REGISTRE = RACINE / 'livrables/registre_calcul_etatB.md'
SUIVI = RACINE / 'livrables/suivi_trajectoire_20261015.md'
EXCEPTIONS = RACINE / 'livrables/registre_exceptions_dates.md'
FLUX = RACINE / 'referentiels/Flux_par_agent_20261015.xlsx'
ETATB = RACINE / 'referentiels/etatB_2027_bg.tsv'
CORRESPONDANCE = RACINE / 'referentiels/correspondance_programmes_pap2026_etatB2027.tsv'
TOL = 2  # euros, par programme : arrondis de la liasse


def norm(s):
    s = unicodedata.normalize('NFKD', str(s).replace('’', "'"))
    s = s.encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def entier(s):
    return int(re.sub(r'[^\d]', '', s) or 0)


# ---------------------------------------------------------------- la liasse
def lire_liasse(chemin=LIASSE):
    """Lignes de programme des amendements « Retirer les crédits » :
    {n°: {mission, ligne_titre, programmes: [(libellé, AE−, CP−, ligne du fichier)],
          totaux: (AE, CP)}}."""
    amendements, cur = OrderedDict(), None
    for i, l in enumerate(open(chemin, encoding='utf-8'), 1):
        m = re.match(r'## Amendement n°\s*(\d+) \[(.*)\]', l)
        if m:
            cur = None
            mm = re.search(r'Retirer les crédits.*mission «\s*(.*?)\s*»', m.group(2))
            if mm:
                cur = int(m.group(1))
                amendements[cur] = dict(mission=mm.group(1), ligne_titre=i,
                                        programmes=[], totaux=None)
            continue
        if cur and l.startswith('|') and not l.startswith('|---') \
                and not l.startswith('| Programmes'):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if 'TOTAUX' in c[0]:
                amendements[cur]['totaux'] = (entier(c[2]), entier(c[4]))
            elif 'dont titre 2' in c[0]:
                continue
            elif not c[0].startswith('**'):
                amendements[cur]['programmes'].append((c[0], entier(c[2]), entier(c[4]), i))
    return amendements


# ------------------------------- règle d'avant le 20261116 (ancien chaine_credits)
# Gardée pour mémoire : c'est elle qui redonnait à l'euro la liasse du 16 octobre.
# `chaine_credits.py` ne la porte plus : il lit la table de paramètres.
DATE_CAT = {21: '1er juil.', 22: '1er juil.', 23: '1er juil.', 31: '1er juil.',
            61: '1er juil.', 32: '1er janv.', 62: '1er janv.', 63: '1er janv.',
            64: '1er janv.', 51: '1er janv.', 52: '1er janv.', 53: '1er janv.',
            71: '1er janv.'}
FRACTION = {'1er juil.': 0.5, '1er janv.': 1.0, '1er avril': 0.75}
RESIDUEL_CAT = {21: 0.0, 22: 0.0, 23: 0.0, 32: 0.0, 61: 0.0, 64: 0.0, 62: 0.20, 63: 0.25}
RESIDUEL_TITRE = {1: 0.0, 2: 0.0, 4: 0.0, 5: 0.80}
COEF_T2 = 0.90 * 0.30   # socle a = 0,90 et indemnité de 70 % : il reste 30 %


def residuel(titre, cat):
    if titre == 2:
        return 0.0
    if cat in RESIDUEL_CAT:
        return RESIDUEL_CAT[cat]
    return RESIDUEL_TITRE.get(titre, 0.15)


# -------------------------------------------------------- lecture du registre
def _cellules(l):
    return [c.strip() for c in l.strip().strip('|').split('|')]


def _nu(s):
    return s.replace('*', '').replace('⚑', '').strip()


def _nombre(s):
    s = _nu(s).replace(',', '.').replace(' ', '')
    try:
        return float(s)
    except ValueError:
        return None


def lire_tableau_lignes(chemin, debut, fin):
    """Tableau « ligne doctrinale » du registre § 4 ou du suivi § 1."""
    out, dedans = {}, False
    for i, l in enumerate(open(chemin, encoding='utf-8'), 1):
        if l.startswith(debut):
            dedans = True
            continue
        if dedans and l.startswith(fin):
            break
        if dedans and l.startswith('|') and re.search(r'\| D\d+ \|', l):
            c = _cellules(l)
            cel = c[1]
            socle = _nu(c[3])
            rythme = _nu(c[5])
            date = _nu(c[7])
            out[cel] = dict(libelle=_nu(c[0]), F=_nombre(c[2]), socle=socle,
                            F_net=_nu(c[4]), rythme=rythme, acteur=_nu(c[6]),
                            date=date, fraction=_nu(c[8]), an2027=_nombre(c[9]),
                            programme=_nu(c[-2] if 'registre' in str(chemin) else c[-1]),
                            ligne_fichier=i)
    return out


def date_normale(d):
    """Mois d'effet 2027 retenu pour le calcul : janv, avril ou juil."""
    if not d:
        return ''
    if 'avril' in d:
        return '1er avril'
    if 'janv' in d:
        return '1er janv.'
    if 'juil' in d:
        return '1er juil.'
    return d


def socle_nombre(s):
    m = re.match(r'(\d+)\s*%', s)
    return int(m.group(1)) / 100 if m else 0.0


def rythme_nombre(s):
    if s.startswith('⅓'):
        return 1 / 3
    if s.startswith('1/6'):
        return 1 / 6
    return 1.0


def fraction_nombre(s):
    m = re.match(r'(\d+)/12', s)
    return int(m.group(1)) / 12 if m else 1.0   # « — » : rythme déjà net de la date


# ---------------------------------------- rattachement au registre (§ 4, § 14)
def ligne_registre(prog, cm, cat, action, rang):
    """Ligne doctrinale du § 4 et étiquette d'action. Les repères de ligne du
    PAP sont ceux du § 14 du registre, vérifiés sur le classeur du site."""
    if cat in (21, 22, 23):
        return 'D38', ''
    if cat in (31, 51, 52, 53):
        if prog == 203 and action == '04':
            return 'D37', '04 Routes – Entretien'
        if prog == 203:
            return 'D37', 'hors 04 Routes – Entretien'
        return 'D37', ''
    if cat == 32:
        if prog == 103 and action == '04':
            return 'D5', '04 Financement des structures de la formation professionnelle et de l’emploi'
        if prog == 103:
            return 'D16', 'hors action 04'
        if prog == 102 and rang == 2267:
            return 'D6', '02 Structures de mise en œuvre de la politique de l’emploi, ligne 2267'
        if prog == 102:
            return 'D16', 'hors ligne 2267'
        if prog == 181:
            return 'D12', ''
        if prog == 135:
            return 'D14', ''
        return 'D16', ''
    if cat == 61:
        if prog == 109:
            return 'D18', ''
        if prog == 135:
            return 'D15', ''
        if prog == 183:
            return ('D19', '02 Aide médicale de l’État') if action == '02' \
                else ('D22', 'hors action 02')
        if prog == 174:
            return ('D20', '02 Accompagnement transition énergétique') if action == '02' \
                else ('D22', 'hors action 02')
        if prog == 103:
            return ('D21', 'ligne 2290, particuliers employeurs') if rang == 2290 \
                else ('non rangée', 'hors ligne 2290')
        return 'D22', ''
    if cat == 62:
        if prog == 103:
            return ('D21', 'ligne 2305, particuliers employeurs') if rang == 2305 \
                else ('D25', 'hors ligne 2305')
        if prog == 102:
            return 'D32', ''
        if cm == 'AV':
            return 'D26', ''
        if cm == 'ZD':
            return 'D24', ''
        return 'D27', ''
    if cat == 64:
        if cm == 'AD':
            return 'D30', ''
        if prog == 177:
            return 'D29', ''
        if prog == 303:
            return 'D31', ''
        if prog == 102:
            return ('D32', '03 Accompagnement des personnes les plus éloignées du marché du travail') \
                if action == '03' else ('non rangée', 'hors action 03')
        if cm == 'AV':
            return 'D33', ''
        if prog == 131:
            return 'D34', ''
        if prog == 147:
            return 'D35', ''
        return 'D36', ''
    return 'aucune', ''   # catégorie 63 : aucune ligne au § 4


# ----------------------------------------------- rattachement au classeur
def poste_classeur(prog, cm, cat, drapeau, action):
    """Poste de `SynthèseR`, taux, part de première année, et leurs adresses.
    Les coefficients sont ceux des formules de `SynthèseR`, relues en clair."""
    def p(nom, cellules, taux, an1, adr_taux, adr_an1, note=''):
        return dict(poste=nom, adresse=cellules, taux=taux, an1=an1,
                    adr_taux=adr_taux, adr_an1=adr_an1, note=note)
    if cat == 22:
        # Onglet « Mesure » du classeur de suivi, ligne 41 : « Catégorie 22 non arrêtée
        # directement — suit le sort de la catégorie 21 ». Poste à part : SynthèseR!D6 ne
        # compte que les catégories 21 et 23, et la preuve du rattachement ne bouge pas.
        return p('Cotisations employeur — suit le sort des salaires', 'aucune cellule à SynthèseR', 0.9, 0.3,
                 "classeur de suivi, onglet « Mesure », ligne 41 : suit le sort de la catégorie 21 ; "
                 "coefficients de SynthèseR!D7 (× 0,3 × 0,9)", 'SynthèseR!D7, par renvoi',
                 'catégorie 22 : le classeur du site ne la chiffre pas ; retirée avec la catégorie 21 (20261117)')
    if cat in (21, 23):
        return p('Salaires', 'SynthèseR!D6:D8', 0.9, 0.3,
                 "SynthèseR!D7 =('Economies R'!G4+J4)*0.3*0.9 ; D8 =D7*7/3", 'SynthèseR!D7')
    if cat == 31:
        if prog == 203 and action == '04':
            return p('Fonctionnement', 'SynthèseR!E6:E7', 0.0, 1.0,
                     "SynthèseR!E7 =('Economies R'!L4-233)*85/100 : les 233 retirés", 'SynthèseR!E7',
                     'entretien des routes nationales maintenu')
        return p('Fonctionnement', 'SynthèseR!E6:E7', 0.85, 1.0,
                 "SynthèseR!E7 =('Economies R'!L4-233)*85/100", 'SynthèseR!E7 ; E8 vide')
    if cat in (51, 52, 53):
        if prog == 203 and action == '04':
            return p('Investissement', 'SynthèseR!F6:F7', 0.0, 1.0,
                     "SynthèseR!F7 =('Economies R'!N4-51)*85/100 : les 51 retirés", 'SynthèseR!F7',
                     'entretien des routes nationales maintenu')
        return p('Investissement', 'SynthèseR!F6:F7', 0.85, 1.0,
                 "SynthèseR!F7 =('Economies R'!N4-51)*85/100", 'SynthèseR!F7 ; F8 vide')
    if drapeau == 'En 3 ans':
        col = {32: 'I14', 62: 'J14', 64: 'K14'}.get(cat, '')
        return p('Hors restitution salariale, schéma en 3 ans', f'SynthèseR!{col}', None, None,
                 f'SynthèseR!{col} : total seul', 'aucune',
                 'total hors restitution ; ni taux ni première année au classeur')
    if cat == 32:
        if prog == 102:
            return p('Subvention opérateurs — France Travail', 'SynthèseR!C19:D21', None, None,
                     'SynthèseR!C20 =3896*0.9*0.3 ; D20 =1869*0.9*(1+1/3)/2', 'SynthèseR!C20:D20',
                     'le classeur chiffre sur le budget de l’opérateur (3 896 et 1 869 M€ en dur), '
                     'non sur la subvention de l’État, retranchée de « Autres » par P176')
        if prog == 135:
            return p('Subvention opérateurs — Anah', 'SynthèseR!E19:E21', 0.9, 0.65,
                     "SynthèseR!E20 ='Economies R'!P65*0.9*(0.3+1)/2", 'SynthèseR!E20:E21')
        if prog == 181:
            return p('Subvention opérateurs — Ademe', 'SynthèseR!G19:G21', 0.837, 0.33 / 0.93,
                     "SynthèseR!G20 ='Economies R'!P90*0.9*(0.3*0.1+1/3*0.9) ; G21 =P90*0.9*(2/3*0.9)",
                     'SynthèseR!G20:G21')
        return p('Subvention opérateurs — Autres', 'SynthèseR!H19:H21', 0.9, 0.65,
                 "SynthèseR!H20 =('Economies R'!Q4-P176-P90-P65)*0.9*(0.3+1)/2", 'SynthèseR!H20:H21')
    if cat == 61:
        if prog == 109:
            return p('Subvention ménages — APL', 'SynthèseR!C31:C33', 1.0, 1 / 3,
                     "SynthèseR!C31 ='Economies R'!R63", 'SynthèseR!C32 =C31/3')
        if prog == 135:
            return p('Subvention opérateurs — MaPrimeRénov’', 'SynthèseR!F19:F20', 1.0, 1.0,
                     "SynthèseR!F20 ='Economies R'!R65", 'SynthèseR!F20 ; F21 vide')
        if prog == 183:
            return p('Subvention ménages — AME', 'SynthèseR!D31:D32', 0.9, 1.0,
                     "SynthèseR!D32 ='Economies R'!R155*0.9", 'SynthèseR!D31 =D32')
        if prog == 103:
            return p('Subvention ménages — Emploi service', 'SynthèseR!E31:E33', 0.9, 1 / 3,
                     "SynthèseR!E31 ='Economies R'!R177*0.9", 'SynthèseR!E32 =E31/3')
        if prog == 174 and action == '04':
            return p('Subvention ménages — Autres', 'SynthèseR!F31:F32', 0.0, 1.0,
                     "SynthèseR!F32 =(…-197.995)*0.9 : les 197,995 de l’après-mines retirés",
                     'SynthèseR!F31 =F32', 'gestion de l’après-mines maintenue')
        return p('Subvention ménages — Autres', 'SynthèseR!F31:F32', 0.9, 1.0,
                 "SynthèseR!F32 =('Economies R'!S4-C31-D31-F20-E31-197.995)*0.9", 'SynthèseR!F31 =F32')
    if cat == 62:
        if cm == 'TB':
            return p('Subvention entreprises — Travail', 'SynthèseR!C25:C27', 1.0, 1 / 3,
                     "SynthèseR!C25 ='Economies R'!U32", 'SynthèseR!C26 =C25/3')
        if cm == 'ZD':
            return p('Subvention entreprises — Audiovisuel public', 'SynthèseR!D25:D26', 1.0, 1.0,
                     "SynthèseR!D25 ='Economies R'!U39", 'SynthèseR!D26 =D25')
        if cm == 'AV':
            return p('Subvention entreprises — France 2030', 'SynthèseR!E25:E27', 1.0, 1 / 3,
                     "SynthèseR!E25 ='Economies R'!U19", 'SynthèseR!E26 =E25/3')
        return p('Subvention entreprises — Autres', 'SynthèseR!F25:F26', 0.9, 1.0,
                 "SynthèseR!F26 =('Economies R'!U4-C25-D25-E25)*0.9", 'SynthèseR!F25 =F26')
    if cat == 64:
        if cm == 'AD':
            return p('Subvention associations — APD', 'SynthèseR!C37:C39', 1.0, 1 / 3,
                     "SynthèseR!C37 ='Economies R'!Y8", 'SynthèseR!C38 =C37/3')
        if prog == 177:
            return p('Subvention associations — Hébergement', 'SynthèseR!D37:D38', 0.8, 1.0,
                     "SynthèseR!D38 ='Economies R'!X68*0.8", 'SynthèseR!D37 =D38')
        if cm == 'TB':
            return p('Subvention associations — Travail', 'SynthèseR!E37:E39', 1.0, 1 / 3,
                     "SynthèseR!E37 ='Economies R'!Y32", 'SynthèseR!E38 =E37/3')
        if cm == 'AV':
            return p('Subvention associations — France 2030', 'SynthèseR!F37:F39', 1.0, 1 / 3,
                     "SynthèseR!F37 ='Economies R'!Y19", 'SynthèseR!F38 =F37/3')
        return p('Subvention associations — Autres', 'SynthèseR!G37:G38', 0.9, 1.0,
                 "SynthèseR!G38 =('Economies R'!Y4-X68-C37-E37-F37)*0.9", 'SynthèseR!G37 =G38')
    if cat == 63:
        return p('Subvention collectivités — aucun poste à SynthèseR', 'Economies R!W4', None, None,
                 'aucune', 'aucune',
                 'arrêtée à Economies R (colonne W), sans colonne à SynthèseR')
    return p('?', '', None, None, '', '')


# ------------------------------------------------- la règle retenue, 20261116
# Tranché par le pilotage, révocable (mandat du 20261116 et sa correction du
# même jour) : montant = brut du PAP × taux d'économie du classeur × rythme du
# § 4 du registre × fraction d'exercice du § 4 ; CP au résiduel du § 3.
# Le classeur ne garde la main que sur le brut et le taux. Là où le registre
# est muet (catégorie 63, D14, D21, lignes non rangées), le taux et le rythme
# sont ceux du classeur et la date est celle de la ligne la plus proche du
# § 4 : ces cas sont marqués « registre muet ».
OBJET = {
    'D5': 'le financement des structures de la formation professionnelle',
    'D6': 'la subvention à France Travail',
    'D12': 'la subvention à l’Agence de la transition écologique',
    'D14': 'la subvention à l’Agence nationale de l’habitat',
    'D15': 'les aides à la rénovation énergétique des logements',
    'D16': 'les subventions aux opérateurs',
    'D18': 'les aides personnelles au logement',
    'D19': 'l’aide médicale de l’État',
    'D20': 'le chèque énergie',
    'D21': 'la compensation des exonérations d’emploi à domicile',
    'D22': 'les transferts aux ménages',
    'D24': 'l’audiovisuel public',
    'D25': 'les aides à l’emploi et à l’apprentissage',
    'D26': 'les aides aux entreprises',
    'D27': 'les aides aux entreprises',
    'D29': 'l’hébergement d’urgence',
    'D30': 'l’aide publique au développement',
    'D31': 'les subventions aux associations',
    'D32': 'les aides à l’insertion',
    'D33': 'les subventions aux associations',
    'D34': 'les subventions aux associations',
    'D35': 'les subventions aux associations',
    'D36': 'les subventions aux associations',
    'D37': 'le fonctionnement courant et l’investissement',
    'D38': 'les rémunérations',
    'aucune': 'les transferts aux collectivités',
}
# date de la ligne la plus proche du § 4, quand le registre est muet
PROCHE = {('D14', 32): ('D16', 'opérateur de l’État, comme les « autres opérateurs »'),
          ('D21', 61): ('D22', 'transfert aux ménages, comme les « autres ménages »'),
          ('D21', 62): ('D25', 'même programme, même catégorie, même poste du classeur que « emploi et apprentissage »'),
          ('non rangée', 61): ('D22', 'transfert aux ménages, comme les « autres ménages »'),
          ('non rangée', 64): ('D36', 'défaut écrit au § 14 du registre : « autres associations »'),
          ('aucune', 63): ('D42', 'personne morale (R-P) ; même rythme et même date que « collectivités — charges courantes »')}
NET_INDEMNITE = 0.30   # § 10 du registre : M × a × d − I, I = 70 % ; classeur, SynthèseR!D7 (× 0,3)


def regle(lr, cat, titre, prog, pc, s4, drapeau, type_mission, ouvert):
    """Paramètres retenus pour une ligne, et le cas dont elle relève."""
    r = dict(regle_taux='', regle_rythme='', regle_date='', regle_fraction='', regle_part_conservee=0,
             regle_net_indemnite=1, regle_residuel=residuel(titre, cat), regle_cas='', regle_origine='',
             objet_expose=OBJET.get(lr, 'les transferts aux ménages' if cat == 61 else
                                    'les subventions aux associations' if cat == 64 else ''),
             retenu='oui', motif_hors_liasse='')
    p4 = s4.get(lr)

    def date_de(cel):
        q = s4[cel]
        ry = rythme_nombre(q['rythme'])
        return ry, date_normale(q['date']), fraction_nombre(q['fraction'])

    if drapeau == 'En 3 ans':
        ry, da, fr = date_de(lr)
        r.update(regle_taux=1.0, regle_rythme=1 / 3, regle_date=da, regle_fraction=FRACTION[da],
                 regle_cas='classeur muet et registre muet',
                 regle_origine='pilotage, 20261117 (« les liasses sur mesure ») : intégrée à un tiers la première '
                               'année ; classeur : « En 3 ans », total seul (SynthèseR!I14:K14), ni taux ni première '
                               'année ; registre § 1 : socle 0 % par défaut, rythme ⅓ si sortie en trois ans ; '
                               f'date et fraction de la ligne {lr} du § 4')
    elif pc['taux'] == 0:
        ry, da, fr = date_de(lr)
        r.update(regle_taux=0.0, regle_rythme=ry, regle_date=da, regle_fraction=fr,
                 regle_cas='registre', regle_origine=f"classeur : {pc['note']} ({pc['adr_taux']})",
                 retenu='non', motif_hors_liasse=f"maintenu : {pc['note']}")
    elif cat == 63:
        cel, pourquoi = PROCHE[('aucune', 63)]
        _, da, fr = date_de(cel)
        r.update(regle_taux=1.0, regle_rythme=1 / 3, regle_date=da, regle_fraction=fr,
                 regle_cas='registre muet',
                 regle_origine='pilotage, 20261116, règle 4 : par tiers sur trois ans, un tiers en 2027 ; taux : arrêtée '
                               f'en entier à Economies R (colonne W) ; date de la ligne {cel} du § 4 — {pourquoi}')
    elif lr == 'D6':
        ry, da, fr = date_de(lr)
        r.update(regle_taux=1 - socle_nombre(p4['socle']), regle_rythme=ry, regle_date=da, regle_fraction=fr,
                 regle_part_conservee=1 / 6, regle_cas='registre, classeur muet',
                 regle_origine='pilotage, 20261116, règle 5 : règle du registre — § 4, ligne D6 : 10 % conservés, tiers '
                               'par an, 1er janvier ; § 3 : un sixième conservé en 2027. Le classeur chiffre sur le budget '
                               'de l’opérateur, non sur la subvention')
    elif (lr, cat) in PROCHE:
        cel, pourquoi = PROCHE[(lr, cat)]
        _, da, _ = date_de(cel)
        r.update(regle_taux=pc['taux'], regle_rythme=pc['an1'], regle_date=da, regle_fraction=FRACTION[da],
                 regle_cas='registre muet',
                 regle_origine=f"pilotage, 20261116, règle 5 : taux et rythme du classeur ({pc['adr_taux']}) ; "
                               f"date de la ligne {cel} du § 4 — {pourquoi}")
    elif pc['taux'] is None:      # programme 102, catégorie 32, hors subvention à France Travail
        ry, da, fr = date_de(lr)
        r.update(regle_taux=1 - socle_nombre(p4['socle']), regle_rythme=ry, regle_date=da, regle_fraction=fr,
                 regle_cas='registre, classeur muet',
                 regle_origine=f'le classeur retranche tout le programme des « autres opérateurs » sans le chiffrer ; '
                               f'registre § 4, ligne {lr} : socle, rythme et date')
    else:
        ry, da, fr = date_de(lr)
        r.update(regle_taux=pc['taux'], regle_rythme=ry, regle_date=da, regle_fraction=fr, regle_cas='registre',
                 regle_origine=f"taux : classeur ({pc['adr_taux']}) ; rythme, date et fraction : registre § 4, ligne {lr}")
        if titre == 2:
            r.update(regle_net_indemnite=NET_INDEMNITE,
                     regle_origine=r['regle_origine'] + ' ; indemnité de départ retranchée, registre § 10 '
                                                        '(I = 70 %, classeur SynthèseR!D7)')
    if r['retenu'] == 'oui':
        if type_mission != 'BG':
            r.update(retenu='non', motif_hors_liasse={
                'CCF': 'compte de concours financiers : état D, hors de l’état B de l’article 58 ; porté en première '
                       'partie (liasse P1, amendement sur le compte d’avances à l’audiovisuel public)',
                'CAS': 'compte d’affectation spéciale : état D, hors de l’état B de l’article 58 ; aucun amendement '
                       'de la liasse ne le porte' + (' ; ligne « En 3 ans » restée dehors pour ce seul motif'
                                                      if drapeau == 'En 3 ans' else '')}.get(type_mission, 'hors budget général'))
        elif ouvert is None:
            r.update(retenu='non', motif_hors_liasse='programme sans ligne à l’état B 2027')
        elif ouvert[0] == 0:
            r.update(retenu='non', motif_hors_liasse='aucune autorisation d’engagement ouverte à l’état B 2027 : un '
                                                     'amendement de crédits n’y retire rien (registre § 15) ; article '
                                                     'normatif dû')
    for k in ('regle_taux', 'regle_rythme', 'regle_fraction', 'regle_part_conservee'):
        if r[k] != '':
            r[k] = round(r[k], 6)
    return r


def lire_etatB():
    """{libellé normalisé : (libellé 2027, mission 2027, AE, CP, titre 2)}."""
    eb, mission, cur = {}, None, None
    for r in csv.DictReader(open(ETATB, encoding='utf-8'), delimiter='\t'):
        if r['rang'] == 'mission':
            mission = r['libelle']
        elif r['rang'] == 'programme':
            cur = norm(r['libelle'])
            eb[cur] = [r['libelle'], mission, int(r['ae']), int(r['cp']), 0]
        elif r['rang'] == 'titre2' and cur:
            eb[cur][4] = int(r['ae'])
    return eb


def lire_correspondance():
    return {int(r['programme']): r for r in csv.DictReader(open(CORRESPONDANCE, encoding='utf-8'), delimiter='\t')}


COL_ECO = {21: ('F', 5), 22: ('H', 7), 23: ('I', 8), 31: ('K', 10), 51: ('M', 12), 52: ('M', 12),
           53: ('M', 12), 32: ('P', 15), 61: ('R', 17), 62: ('T', 19), 63: ('V', 21), 64: ('X', 23)}
COL_DRAPEAU = {32: ('Q', 16), 61: ('S', 18), 62: ('U', 20), 63: ('W', 22), 64: ('Y', 24)}

COLONNES = [
    'n', 'poste_classeur', 'adresse_poste', 'ligne_registre', 'libelle_registre',
    'type_mission', 'code_mission', 'mission', 'programme', 'libelle_programme',
    'categorie', 'titre', 'action',
    'brut_ae', 'brut_cp', 'adresse_pap',
    'drapeau_classeur', 'adresse_drapeau',
    'taux_classeur', 'adresse_taux', 'part_an1_classeur', 'adresse_part_an1',
    'plein_cp_classeur', 'an1_cp_classeur', 'note_classeur',
    's4_F', 's4_socle', 's4_F_net', 's4_rythme', 's4_acteur', 's4_date', 's4_fraction',
    's4_2027', 's4_programme', 'adresse_s4',
    'socle_s4_contre_classeur', 'rythme_s4_contre_classeur',
    'date_registre_s4', 'date_suivi_trajectoire', 'date_registre_exceptions',
    'date_flux_par_agent', 'date_chaine_credits', 'dates',
    'amendement', 'liasse_inclus', 'fraction_liasse', 'coefficient_liasse', 'residuel_liasse',
    'liasse_ae_ligne', 'liasse_cp_ligne',
    'liasse_ae_programme', 'liasse_cp_programme', 'adresse_liasse',
    'etatB_2027_ae', 'etatB_2027_cp', 'ecretement',
    'cible_classeur_ae', 'cible_classeur_cp', 'cible_registre_ae', 'cible_registre_cp',
    'cible_mixte_ae', 'cible_mixte_cp',
    # --- la règle retenue (pilotage, 20261116) : ce que lit `chaine_credits.py`
    'etatB_2027_mission', 'etatB_2027_programme', 'etatB_2027_titre2', 'correspondance_2027',
    'regle_taux', 'regle_rythme', 'regle_date', 'regle_fraction', 'regle_part_conservee',
    'regle_net_indemnite', 'regle_residuel', 'regle_cas', 'regle_origine', 'objet_expose',
    'retenu', 'motif_hors_liasse', 'amendement_mission',
    'cible_projet_ae', 'cible_projet_cp',
]


# ------------------------------------------------------------- construire
def rejouer_flux(s4):
    """Le flux mensuel par agent rejoue-t-il les dates du § 4 ? Rend, par
    ligne doctrinale, l'agent et l'écart maximal de son rejeu sur 2027."""
    import openpyxl
    w = openpyxl.load_workbook(FLUX, data_only=True)
    mens = {}
    for row in w['Mensuel par agent'].iter_rows(min_row=5, values_only=True):
        if row[0]:
            mens[row[0].replace('’', "'")] = [x or 0 for x in row[1:13]]
    cle = {}
    for row in w[[n for n in w.sheetnames if n.startswith('La clé')][0]].iter_rows(min_row=5, values_only=True):
        if row[0]:
            for d in re.findall(r'D\d+', row[1] or ''):
                cle.setdefault(d, []).append(row[0].replace('’', "'"))
    restit = [0, 0, 0, 0, 0, 0, 1.59, 3.18, 4.77, 6.36, 7.95, 9.54]   # registre § 2
    calc = {a: [0.0] * 12 for a in mens}
    for d, agents in cle.items():
        if d not in s4:
            continue
        deb = {'1er janv.': 0, '1er avril': 3, '1er juil.': 6}[date_normale(s4[d]['date'])]
        par_mois = s4[d]['an2027'] / (12 - deb) / len(agents)
        for a in agents:
            if a in calc:
                for m in range(deb, 12):
                    calc[a][m] -= par_mois
    for a in calc:
        part = 0.9 if 'transferts' in a else 0.1 if a.startswith('Agents') else 0
        for m in range(12):
            calc[a][m] += restit[m] * part
    ecart = {a: max(abs(calc[a][m] - mens[a][m]) for m in range(12)) for a in mens if a in calc
             and not a.upper().startswith('TOTAL')}
    return {d: (' + '.join(ag), max(ecart.get(a, 9) for a in ag)) for d, ag in cle.items()}


def construire(xls, xlsx):
    import xlrd
    b = xlrd.open_workbook(xls)
    pap = b.sheet_by_name('Données PAP 2026')
    eco = b.sheet_by_name('Economies R')

    # Economies R : une ligne par programme, drapeaux d'arrêt et périmètre
    prog_eco = {}
    for r in range(40, eco.nrows):
        v = eco.row_values(r)
        if v[0] == 'P':
            prog_eco[int(v[2])] = (r + 1, v)

    s4 = lire_tableau_lignes(REGISTRE, '## 4. Le tableau', '## 5.')
    suivi = lire_tableau_lignes(SUIVI, '## 1. Ligne par ligne', '## 2.')
    assert len(s4) == 27 and len(suivi) == 27, (len(s4), len(suivi))
    exc = EXCEPTIONS.read_text(encoding='utf-8')
    assert re.search(r'\*\*1er avril 2027\*\* \|[^\n]*hébergement', exc)
    assert re.search(r'\*\*1er juin 2027\*\* \|[^\n]*aide au logement', exc)
    assert re.search(r'\*\*1er novembre 2027\*\* \|[^\n]*structures dissoutes', exc)
    flux = rejouer_flux(s4)
    etatb = lire_etatB()
    corr = lire_correspondance()
    ouverts = {k: (v[2], v[3]) for k, v in etatb.items()}

    liasse = lire_liasse()
    par_prog_liasse = {}
    for n, a in liasse.items():
        for lib, ae, cp, lig in a['programmes']:
            par_prog_liasse[norm(lib)] = (n, ae, cp, lig)

    # agrégation du PAP au grain programme × catégorie × ligne du registre
    groupes = OrderedDict()
    for r in range(1, pap.nrows):
        v = pap.row_values(r)
        if v[3] == '' or v[9] == '':
            continue
        prog, cat, titre = int(v[3]), int(v[9]), int(v[10])
        if prog not in prog_eco:
            continue
        erow, e = prog_eco[prog]
        if cat in COL_DRAPEAU:
            drapeau = e[COL_DRAPEAU[cat][1]]
            if drapeau not in ('Oui', 'En 3 ans'):
                continue
            adr_dr = f"Economies R!{COL_DRAPEAU[cat][0]}{erow}"
        elif cat in (21, 22, 23, 31, 51, 52, 53):
            if e[4] != '':
                continue
            drapeau = 'périmètre non essentiel'
            adr_dr = f"Economies R!E{erow} vide"
        else:
            continue
        ae, cp = v[11] or 0, v[12] or 0
        if not ae and not cp:
            continue
        lr, action = ligne_registre(prog, v[2], cat, str(v[5]), r + 1)
        # la seule action que le classeur isole hors du registre : l'après-mines
        act_cl = '04' if (prog == 174 and cat == 61 and str(v[5]) == '04') else \
                 ('04' if prog == 203 and str(v[5]) == '04' else '')
        if prog == 174 and cat == 61 and str(v[5]) != '02':
            action = ('04 Gestion économique et sociale de l’après-mines' if str(v[5]) == '04'
                      else '03 Aides à l’acquisition de véhicules propres')
        k = (prog, cat, lr, action)
        g = groupes.setdefault(k, dict(type=v[0], mission=v[1], cm=v[2], lprog=v[4], titre=titre,
                                       ae=0.0, cp=0.0, rangs=[], drapeau=drapeau, adr_dr=adr_dr,
                                       act_cl=act_cl))
        g['ae'] += ae
        g['cp'] += cp
        g['rangs'].append(r + 1)

    missions_2026 = {norm(pap.cell_value(r, 1)) for r in range(1, pap.nrows) if pap.cell_value(r, 1)}
    titres_liasse = {norm(a['mission']): n for n, a in liasse.items()}
    dernier_numero = max(int(x) for x in re.findall(r'^## Amendement n° (\d+) \[',
                                                    LIASSE.read_text(encoding='utf-8'), re.M))
    lignes = []
    for n, ((prog, cat, lr, action), g) in enumerate(groupes.items(), 1):
        pc = poste_classeur(prog, g['cm'], cat, g['drapeau'], g['act_cl'])
        d = OrderedDict((c, '') for c in COLONNES)
        d.update(n=n, poste_classeur=pc['poste'], adresse_poste=pc['adresse'],
                 ligne_registre=lr, type_mission=g['type'], code_mission=g['cm'],
                 mission=g['mission'], programme=prog, libelle_programme=g['lprog'],
                 categorie=cat, titre=g['titre'], action=action,
                 brut_ae=round(g['ae']), brut_cp=round(g['cp']),
                 adresse_pap='Données PAP 2026!L:M, lignes ' + ';'.join(map(str, g['rangs'])),
                 drapeau_classeur=g['drapeau'], adresse_drapeau=g['adr_dr'],
                 adresse_taux=pc['adr_taux'], adresse_part_an1=pc['adr_an1'],
                 note_classeur=pc['note'])
        if pc['taux'] is not None:
            d.update(taux_classeur=round(pc['taux'], 4), part_an1_classeur=round(pc['an1'], 4),
                     plein_cp_classeur=round(g['cp'] * pc['taux']),
                     an1_cp_classeur=round(g['cp'] * pc['taux'] * pc['an1']),
                     cible_classeur_ae=round(g['ae'] * pc['taux'] * pc['an1']),
                     cible_classeur_cp=round(g['cp'] * pc['taux'] * pc['an1']))
        # --- registre § 4
        p4 = s4.get(lr)
        if p4:
            d.update(libelle_registre=p4['libelle'], s4_F=p4['F'], s4_socle=p4['socle'],
                     s4_F_net=p4['F_net'], s4_rythme=p4['rythme'], s4_acteur=p4['acteur'],
                     s4_date=p4['date'], s4_fraction=p4['fraction'], s4_2027=p4['an2027'],
                     s4_programme=p4['programme'],
                     adresse_s4=f"livrables/registre_calcul_etatB.md § 4, ligne {p4['ligne_fichier']}",
                     date_registre_s4=date_normale(p4['date']),
                     date_suivi_trajectoire=date_normale(suivi[lr]['date']))
            so, ry, fr = socle_nombre(p4['socle']), rythme_nombre(p4['rythme']), fraction_nombre(p4['fraction'])
            if g['titre'] == 2:                       # § 10 : M × a × d − I, I = 70 %
                k_ae = k_cp = 0.90 * fr * 0.30
            else:
                k_ae = (1 - so) * ry * fr * (5 / 6 if lr == 'D6' else 1)
                k_cp = k_ae * (1 - residuel(g['titre'], cat))
            d.update(cible_registre_ae=round(g['ae'] * k_ae),
                     cible_registre_cp=round(min(g['cp'], g['ae']) * k_cp))
            if pc['taux'] is not None:        # taux et rythme du classeur, part d'année du § 4
                k_m = pc['taux'] * pc['an1'] * FRACTION[date_normale(p4['date'])]
                d.update(cible_mixte_ae=round(g['ae'] * k_m),
                         cible_mixte_cp=round(min(g['cp'], g['ae']) * k_m * (1 - residuel(g['titre'], cat))))
            if pc['taux'] is None:
                d['socle_s4_contre_classeur'] = d['rythme_s4_contre_classeur'] = 'registre seul'
            else:
                d['socle_s4_contre_classeur'] = 'identique' if abs((1 - so) - pc['taux']) < 0.005 \
                    else f"diffère : registre {1 - so:.0%} conservé du brut, classeur {pc['taux']:.1%}"
                # rythme de première année, hors date : celui du registre est le rythme annuel
                ry_an = 1 / 3 if lr == 'D25' else ry
                d['rythme_s4_contre_classeur'] = 'identique' if abs(ry_an - pc['an1']) < 0.005 \
                    else f"diffère : registre {ry_an:.3f}, classeur {pc['an1']:.3f}"
            ag, ec = flux.get(lr, ('', 9))
            d['date_flux_par_agent'] = (f"{date_normale(p4['date'])} (agent {ag} ; rejeu du § 4, écart "
                                        f"max {ec:.3f} Md€)" if ec <= 0.005 else
                                        f"non rejouée (agent {ag}, écart {ec:.3f} Md€)")
        else:
            d['libelle_registre'] = {'D14': 'Agence nationale de l’habitat', 'D21': 'Exonérations emploi à domicile',
                                     'aucune': '', 'non rangée': ''}.get(lr, '')
            d['adresse_s4'] = ('livrables/registre_calcul_etatB.md § 4 : hors tableau (première partie ou jambe sociale)'
                               if lr in ('D14', 'D21') else
                               'livrables/registre_calcul_etatB.md § 14 : non rangée' if lr == 'non rangée'
                               else 'livrables/registre_calcul_etatB.md § 4 : aucune ligne')
            d['socle_s4_contre_classeur'] = d['rythme_s4_contre_classeur'] = \
                'classeur seul' if pc['taux'] is not None else 'ni l’un ni l’autre'
        d['date_registre_exceptions'] = {
            'D29': '1er avril 2027 (§ 2, pièce 2.6-C)',
            'D18': '1er juin 2027 (§ 2, pièce 2.6-A : dépôt de la demande)',
            'D16': 'aucune ; 1er novembre 2027 pour les seuls « établissements vivant de leur patrimoine » '
                   '(§ 2, ligne due non rattachée à un programme)',
        }.get(lr, 'aucune exception inscrite : date commune, non précisée')
        d['date_chaine_credits'] = DATE_CAT[cat]
        if p4:
            d['dates'] = 'concordent' if d['date_registre_s4'] == DATE_CAT[cat] else 'se contredisent'
        else:
            d['dates'] = 'registre muet'
        # --- la liasse
        lib27 = corr[prog]['libelle_etatB_2027'] if prog in corr else g['lprog']
        e27 = etatb.get(norm(lib27))
        pl = par_prog_liasse.get(norm(lib27)) or par_prog_liasse.get(norm(g['lprog']))
        inclus = bool(pl) and g['drapeau'] != 'En 3 ans' and cat != 22 and \
            not (prog == 203 and cat in (31, 51, 52, 53) and action.startswith('04'))
        fr_l = FRACTION[DATE_CAT[cat]]
        coef = COEF_T2 if g['titre'] == 2 else 1.0
        res = residuel(g['titre'], cat)
        d.update(fraction_liasse=fr_l, coefficient_liasse=round(coef, 2), residuel_liasse=res,
                 liasse_inclus='oui' if inclus else 'non')
        if pl:
            d.update(amendement=pl[0], liasse_ae_programme=pl[1], liasse_cp_programme=pl[2],
                     adresse_liasse=f"livrables/depot_2027/LIASSE_PLF_P2.md, ligne {pl[3]}")
        if inclus:
            d.update(liasse_ae_ligne=round(g['ae'] * fr_l * coef, 2),
                     liasse_cp_ligne=round(min(g['cp'], g['ae']) * fr_l * coef * (1 - res), 2))
        if e27:
            d.update(etatB_2027_ae=e27[2], etatB_2027_cp=e27[3], etatB_2027_mission=e27[1],
                     etatB_2027_programme=e27[0], etatB_2027_titre2=e27[4],
                     correspondance_2027=(f"{corr[prog]['statut']} : {corr[prog]['preuve']}" if prog in corr
                                          else 'relevé : même libellé'))
        # --- la règle retenue
        rg = regle(lr, cat, g['titre'], prog, pc, s4, g['drapeau'], g['type'], (e27[2], e27[3]) if e27 else None)
        if rg['retenu'] == 'oui':
            # l'amendement de la mission : par son nom de 2027, ou par son nom de 2026 si la mission a été renommée
            m27 = norm(e27[1])
            num = titres_liasse.get(m27)
            if num is None and m27 not in missions_2026:
                num = titres_liasse.get(norm(g['mission']))
            if num is None:
                # Mission sans amendement : elle prend le numéro qui suit le dernier de la
                # liasse. Aucun numéro en place ne change (pilotage, 20261117).
                num = titres_liasse[m27] = dernier_numero = dernier_numero + 1
                print(f"mission « {e27[1]} » sans amendement dans la liasse : n° {num}, en dernier numéro")
            rg['amendement_mission'] = num
        d.update(rg)
        if rg['regle_taux'] != '':
            k = rg['regle_taux'] * rg['regle_rythme'] * rg['regle_fraction'] * (1 - rg['regle_part_conservee']) \
                * rg['regle_net_indemnite']
            d.update(cible_projet_ae=round(g['ae'] * k),
                     cible_projet_cp=round(min(g['cp'], g['ae']) * k * (1 - rg['regle_residuel'])))
        lignes.append(d)

    # écrêtement : relevé programme par programme
    somme = defaultdict(lambda: [0.0, 0.0])
    for d in lignes:
        if d['liasse_inclus'] == 'oui':
            somme[d['programme']][0] += d['liasse_ae_ligne']
            somme[d['programme']][1] += d['liasse_cp_ligne']
    for d in lignes:
        if d['amendement'] != '' and d['etatB_2027_ae'] != '':
            d['ecretement'] = 'oui' if somme[d['programme']][0] > d['etatB_2027_ae'] + TOL else 'non'


    with open(TSV, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, COLONNES, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(lignes)
    print(f"{TSV.relative_to(RACINE)} : {len(lignes)} lignes, {len(COLONNES)} colonnes")

    # preuve du rattachement : la somme des lignes redonne chaque poste de SynthèseR
    syn = b.sheet_by_name('SynthèseR')
    def cel(a):
        col = ord(a[0]) - 65
        return syn.cell_value(int(a[1:]) - 1, col)
    attendus = {'Salaires': 'D6', 'Fonctionnement': 'E6', 'Investissement': 'F6',
                'Subvention opérateurs — Anah': 'E19', 'Subvention opérateurs — MaPrimeRénov’': 'F19',
                'Subvention opérateurs — Ademe': 'G19', 'Subvention opérateurs — Autres': 'H19',
                'Subvention entreprises — Travail': 'C25', 'Subvention entreprises — Audiovisuel public': 'D25',
                'Subvention entreprises — France 2030': 'E25', 'Subvention entreprises — Autres': 'F25',
                'Subvention ménages — APL': 'C31', 'Subvention ménages — AME': 'D31',
                'Subvention ménages — Emploi service': 'E31', 'Subvention ménages — Autres': 'F31',
                'Subvention associations — APD': 'C37', 'Subvention associations — Hébergement': 'D37',
                'Subvention associations — Travail': 'E37', 'Subvention associations — France 2030': 'F37',
                'Subvention associations — Autres': 'G37'}
    tot = defaultdict(float)
    for d in lignes:
        if d['plein_cp_classeur'] != '':
            tot[d['poste_classeur']] += d['plein_cp_classeur']
    print("\nposte | somme des lignes, régime plein, M€ | SynthèseR | écart")
    for poste, a in attendus.items():
        print(f"{poste} | {tot[poste] / 1e6:.3f} | {a} = {cel(a):.3f} | {tot[poste] / 1e6 - cel(a):+.3f}")
    parametres_s4(s4, cel, xlsx)
    return 0


SYNTHESE_R = {  # ligne du registre -> cellules de SynthèseR (total, première année)
    'D6': ('C19+D19', 'C20+D20'), 'D12': ('G19', 'G20'), 'D14': ('E19', 'E20'), 'D15': ('F19', 'F20'),
    'D16': ('H19', 'H20'), 'D18': ('C31', 'C32'), 'D19': ('D31', 'D32'), 'D21': ('E31', 'E32'),
    'D22': ('F31', 'F32'), 'D24': ('D25', 'D26'), 'D25': ('C25', 'C26'), 'D26': ('E25', 'E26'),
    'D27': ('F25', 'F26'), 'D29': ('D37', 'D38'), 'D30': ('C37', 'C38'), 'D32': ('E37', 'E38'),
    'D33': ('F37', 'F38'), 'D34': ('G40', 'G40'), 'D35': ('G41', 'G41'), 'D36': ('G37', 'G38'),
    'D37': ('E6+F6', 'E7+F7'), 'D38': ('D6', 'D7')}


def parametres_s4(s4, cel, xlsx):
    """Chaque paramètre du § 4 face aux deux classeurs du site, en Md€."""
    import openpyxl
    de = openpyxl.load_workbook(xlsx, data_only=True)['Détail Economies']
    som = lambda e: sum(cel(a) for a in e.split('+')) / 1000
    print("\ncel. | ligne | F § 4 | F Détail Economies | total SynthèseR | 2027 § 4 | an 1 Détail Economies (D) "
          "| an 1 SynthèseR | socle § 4 | rythme § 4 | hypothèse Détail Economies (G)")
    for c in sorted(set(s4) | {'D14', 'D21'}, key=lambda x: int(x[1:])):
        r = int(c[1:])
        p = s4.get(c, {})
        sr = SYNTHESE_R.get(c)
        print(f"{c} | {p.get('libelle', de.cell(r, 3).value)} | {p.get('F', '—')} | {de.cell(r, 6).value} | "
              f"{som(sr[0]):.3f} ({sr[0]})" if sr else
              f"{c} | {p.get('libelle', de.cell(r, 3).value)} | {p.get('F', '—')} | {de.cell(r, 6).value} | —",
              f"| {p.get('an2027', '—')} | {de.cell(r, 4).value} | " +
              (f"{som(sr[1]):.3f} ({sr[1]})" if sr else '—') +
              f" | {p.get('socle', '—')} | {p.get('rythme', '—')} | {de.cell(r, 7).value or ''}")


# ---------------------------------------------------------------- contrôler
CIBLES = {'classeur': ('cible_classeur_ae', 'cible_classeur_cp'),
          'registre': ('cible_registre_ae', 'cible_registre_cp'),
          'mixte': ('cible_mixte_ae', 'cible_mixte_cp'),
          'projet': ('cible_projet_ae', 'cible_projet_cp'),
          'liasse': ('liasse_ae_ligne', 'liasse_cp_ligne')}


def lire_tsv():
    return list(csv.DictReader(open(TSV, encoding='utf-8'), delimiter='\t'))


def comparer(cible, liasse=None, lignes=None):
    """Par amendement et par programme : montant inscrit, montant du paramètre,
    écart, et part de la liasse restée sans paramètre."""
    liasse = liasse or lire_liasse()
    lignes = lignes or lire_tsv()
    col_ae, col_cp = CIBLES[cible]
    par = defaultdict(list)
    for d in lignes:
        if cible == 'projet':
            if d['retenu'] == 'oui':
                par[norm(d['etatB_2027_programme'])].append(d)
        elif d['liasse_inclus'] == 'oui':
            par[norm(d['etatB_2027_programme'] or d['libelle_programme'])].append(d)
    res = []
    for n, a in liasse.items():
        progs = []
        for lib, ae, cp, lig in a['programmes']:
            rows = par.get(norm(lib), [])
            c_ae = c_cp = sans_ae = sans_cp = 0.0
            for d in rows:
                if d[col_ae] == '':
                    sans_ae += float(d['liasse_ae_ligne'] or 0)
                    sans_cp += float(d['liasse_cp_ligne'] or 0)
                else:
                    c_ae += float(d[col_ae])
                    c_cp += float(d[col_cp])
            if rows and rows[0]['etatB_2027_ae'] != '':      # minoration ≤ crédit ouvert
                oa, oc = int(rows[0]['etatB_2027_ae']), int(rows[0]['etatB_2027_cp'])
                brut_ae = c_ae + sans_ae
                if cible in ('liasse', 'projet'):
                    c_ae = min(c_ae, oa)
                    c_cp = min(c_cp, c_ae, oc)
                else:
                    c_ae = min(c_ae, oa)
                    c_cp = min(c_cp, oc)
                    if brut_ae > oa and sans_ae:     # part sans paramètre, ramenée au crédit ouvert
                        sans_cp *= (ae / brut_ae) if brut_ae else 0
                        sans_ae *= (ae / brut_ae) if brut_ae else 0
            progs.append(dict(programme=lib, ligne=lig, ae=ae, cp=cp, cible_ae=c_ae, cible_cp=c_cp,
                              sans_ae=sans_ae, sans_cp=sans_cp, lignes=len(rows)))
        if cible == 'projet':       # un programme retenu par la table et absent de l'amendement
            presents = {norm(p['programme']) for p in progs}
            for k, rows in par.items():
                if k not in presents and str(rows[0]['amendement_mission']) == str(n):
                    c_ae = min(sum(float(d[col_ae]) for d in rows), int(rows[0]['etatB_2027_ae']))
                    if c_ae > TOL:
                        progs.append(dict(programme=rows[0]['etatB_2027_programme'] + ' (absent de la liasse)',
                                          ligne=0, ae=0, cp=0, cible_ae=c_ae, cible_cp=0, sans_ae=0, sans_cp=0,
                                          lignes=len(rows), absent=True))
        res.append(dict(n=n, mission=a['mission'], totaux=a['totaux'], programmes=progs))
    return res


def controler(cible, liasse=None, muet=False):
    res = comparer(cible, liasse)
    echecs = 0
    tot = [0.0] * 6
    out = []
    for a in res:
        ae = sum(p['ae'] for p in a['programmes'])
        cp = sum(p['cp'] for p in a['programmes'])
        c_ae = sum(p['cible_ae'] for p in a['programmes'])
        c_cp = sum(p['cible_cp'] for p in a['programmes'])
        s_ae = sum(p['sans_ae'] for p in a['programmes'])
        s_cp = sum(p['sans_cp'] for p in a['programmes'])
        motifs = []
        if a['totaux'] is None or abs(a['totaux'][0] - ae) > TOL or abs(a['totaux'][1] - cp) > TOL:
            motifs.append('total de l’amendement ≠ somme de ses programmes')
        for p in a['programmes']:
            if not p['lignes']:
                motifs.append(f"programme sans ligne au TSV : {p['programme']}")
            elif p['sans_ae'] > TOL:
                motifs.append(f"sans paramètre : {p['programme'][:40]}")
            elif abs(p['ae'] - p['cible_ae']) > TOL or abs(p['cp'] - p['cible_cp']) > TOL:
                motifs.append(f"écart : {p['programme'][:40]} "
                              f"AE {p['ae'] - p['cible_ae']:+,.0f} CP {p['cp'] - p['cible_cp']:+,.0f}")
        etat = 'ÉCHEC' if motifs else 'tenu'
        echecs += bool(motifs)
        for i, x in enumerate((ae, cp, c_ae, c_cp, s_ae, s_cp)):
            tot[i] += x
        out.append(f"n° {a['n']:>2} {etat:5} AE {ae:>15,.0f} cible {c_ae:>15,.0f} "
                   f"écart {ae - c_ae - s_ae:>+15,.0f} sans paramètre {s_ae:>14,.0f}  {a['mission'][:44]}")
        if not muet:
            for m in motifs:
                out.append(f"        · {m}")
    out.append(f"TOTAL       AE {tot[0]:>15,.0f} cible {tot[2]:>15,.0f} écart {tot[0] - tot[2] - tot[4]:>+15,.0f} "
               f"sans paramètre {tot[4]:>14,.0f}")
    out.append(f"            CP {tot[1]:>15,.0f} cible {tot[3]:>15,.0f} écart {tot[1] - tot[3] - tot[5]:>+15,.0f} "
               f"sans paramètre {tot[5]:>14,.0f}")
    out.append(f"cible « {cible} » : {len(res)} amendements, {echecs} en échec.")
    if not muet:
        print('\n'.join(out).replace(',', ' '))
    return echecs


def faute(cible='projet'):
    """Le contrôle doit pouvoir échouer : une faute de 1 000 € injectée en
    mémoire dans la première ligne de la liasse, sous la cible qui passe."""
    if controler(cible, muet=True) != 0:
        print(f'La cible « {cible} » ne passe pas : le jeu de faute ne prouve rien.')
        return 1
    liasse = lire_liasse()
    n = next(iter(liasse))
    lib, ae, cp, lig = liasse[n]['programmes'][0]
    liasse[n]['programmes'][0] = (lib, ae + 1000, cp, lig)
    mordu = controler(cible, liasse=liasse, muet=True)
    print(f"faute de 1 000 € injectée, amendement n° {n}, « {lib} » : "
          f"{'mordue' if mordu else 'NON MORDUE'} ({mordu} amendement en échec).")
    return 0 if mordu == 1 else 1


# ------------------------------------------------------------------ écarts
def md(x):
    return f"{x:,.0f}".replace(',', ' ').replace('-', '−')


def ecarts():
    lignes = lire_tsv()
    cl = {a['n']: a for a in comparer('classeur')}
    rg = {a['n']: a for a in comparer('registre')}
    print("| n° | mission | liasse, AE | classeurs, AE | écart | registre § 4, AE | écart | sans paramètre au classeur | au registre |")
    print("|---:|---|---:|---:|---:|---:|---:|---:|---:|")
    T = [0.0] * 5
    for n in cl:
        s = lambda a, k: sum(p[k] for p in a['programmes'])
        ae = s(cl[n], 'ae')
        v = (ae, s(cl[n], 'cible_ae'), s(rg[n], 'cible_ae'), s(cl[n], 'sans_ae'), s(rg[n], 'sans_ae'))
        for i in range(5):
            T[i] += v[i]
        print(f"| {n} | {cl[n]['mission']} | {md(v[0])} | {md(v[1])} | {md(v[0] - v[1] - v[3])} | "
              f"{md(v[2])} | {md(v[0] - v[2] - v[4])} | {md(v[3])} | {md(v[4])} |")
    print(f"| | **Total** | **{md(T[0])}** | **{md(T[1])}** | **{md(T[0] - T[1] - T[3])}** | "
          f"**{md(T[2])}** | **{md(T[0] - T[2] - T[4])}** | **{md(T[3])}** | **{md(T[4])}** |")
    print()
    for nom, res in (('classeurs', cl), ('registre § 4', rg)):
        plus = moins = 0.0
        for a in res.values():
            for p in a['programmes']:
                e = p['ae'] - p['cible_ae'] - p['sans_ae']
                plus += max(e, 0)
                moins += min(e, 0)
        print(f"Écarts d'AE par programme, {nom} : en trop {md(plus)}, en moins {md(moins)}, "
              f"en valeur absolue {md(plus - moins)}.")
    print()
    mx = {a['n']: a for a in comparer('mixte')}
    print("| n° | liasse, AE | taux et rythme du classeur × part d'année du § 4, AE | écart | sans paramètre | CP | écart de CP |")
    print("|---:|---:|---:|---:|---:|---:|---:|")
    T = [0.0] * 6
    for n in mx:
        s = lambda k: sum(p[k] for p in mx[n]['programmes'])
        v = (s('ae'), s('cible_ae'), s('sans_ae'), s('cp'), s('cible_cp'), s('sans_cp'))
        for i in range(6):
            T[i] += v[i]
        print(f"| {n} | {md(v[0])} | {md(v[1])} | {md(v[0] - v[1] - v[2])} | {md(v[2])} | {md(v[4])} | {md(v[3] - v[4] - v[5])} |")
    print(f"| **Total** | **{md(T[0])}** | **{md(T[1])}** | **{md(T[0] - T[1] - T[2])}** | **{md(T[2])}** | **{md(T[4])}** | **{md(T[3] - T[4] - T[5])}** |")
    print()
    # par poste du classeur
    pp = OrderedDict()
    for d in lignes:
        if d['liasse_inclus'] != 'oui':
            continue
        g = pp.setdefault(d['poste_classeur'], [0.0] * 5)
        g[0] += float(d['brut_ae'])
        g[1] += float(d['liasse_ae_ligne'])
        g[2] += float(d['cible_classeur_ae'] or 0)
        g[3] += float(d['cible_registre_ae'] or 0)
        g[4] += float(d['cible_mixte_ae'] or 0)
    print("| poste du classeur | brut PAP, AE | liasse, AE reconstituée | classeurs, première année | registre § 4 | classeur × part d'année |")
    print("|---|---:|---:|---:|---:|---:|")
    for k, g in sorted(pp.items(), key=lambda x: -x[1][1]):
        print(f"| {k} | {md(g[0])} | {md(g[1])} | {md(g[2])} | {md(g[3])} | {md(g[4])} |")
    print()
    print("| n° | liasse, CP | classeurs, CP | écart | registre § 4, CP | écart | sans paramètre au classeur | au registre |")
    print("|---:|---:|---:|---:|---:|---:|---:|---:|")
    T = [0.0] * 5
    for n in cl:
        s = lambda a, k: sum(p[k] for p in a['programmes'])
        v = (s(cl[n], 'cp'), s(cl[n], 'cible_cp'), s(rg[n], 'cible_cp'), s(cl[n], 'sans_cp'), s(rg[n], 'sans_cp'))
        for i in range(5):
            T[i] += v[i]
        print(f"| {n} | {md(v[0])} | {md(v[1])} | {md(v[0] - v[1] - v[3])} | {md(v[2])} | "
              f"{md(v[0] - v[2] - v[4])} | {md(v[3])} | {md(v[4])} |")
    print(f"| **Total** | **{md(T[0])}** | **{md(T[1])}** | **{md(T[0] - T[1] - T[3])}** | **{md(T[2])}** | "
          f"**{md(T[0] - T[2] - T[4])}** | **{md(T[3])}** | **{md(T[4])}** |")
    print()
    # contradictions de dates, par ligne du registre × catégorie
    vus = OrderedDict()
    for d in lignes:
        k = (d['ligne_registre'], d['categorie'])
        g = vus.setdefault(k, dict(d=d, progs=set(), ae=0.0, inclus=0))
        g['progs'].add(d['programme'])
        if d['liasse_inclus'] == 'oui':
            g['ae'] += float(d['liasse_ae_ligne'])
            g['inclus'] += 1
    print("| ligne | cat. | registre § 4 | suivi de trajectoire § 1 | registre des exceptions | flux par agent | `DATE_CAT` | fraction liasse | programmes | AE dans la liasse | lecture |")
    print("|---|---:|---|---|---|---|---|---:|---:|---:|---|")
    nb = defaultdict(int)
    for (lr, cat), g in sorted(vus.items(), key=lambda x: (x[1]['d']['dates'], x[0][0], int(x[0][1]))):
        d = g['d']
        nb[d['dates']] += 1
        print(f"| {lr} {d['libelle_registre']} | {cat} | {d['date_registre_s4'] or '—'} | "
              f"{d['date_suivi_trajectoire'] or '—'} | {d['date_registre_exceptions']} | "
              f"{d['date_flux_par_agent'] or '—'} | {d['date_chaine_credits']} | {d['fraction_liasse']} | "
              f"{len(g['progs'])} | {md(g['ae'])} | {d['dates']} |")
    print()
    print(dict(nb))
    return 0


A_CREDITS = RACINE / 'sources/projet_20261116/23_tsv_suivi_depenses__A_Credits.tsv'


def reperes():
    """Rejoue les repères `A!Kn/Ln` du § 14 du registre sur l'onglet « A — Crédits »
    du classeur de suivi (rendu en texte au projet le 20261116) : la ligne n porte-t-elle
    le programme et la catégorie annoncés, est-elle « arrêtée », et ses montants arrêtés
    sont-ils le brut de la table de paramètres ?"""
    A = {int(r['ligne']): r for r in csv.DictReader(open(A_CREDITS, encoding='utf-8'), delimiter='\t')}
    brut = defaultdict(lambda: [0.0, 0.0])
    for d in lire_tsv():
        if d['drapeau_classeur'] != 'En 3 ans':
            brut[(d['programme'], d['categorie'])][0] += float(d['brut_ae'])
            brut[(d['programme'], d['categorie'])][1] += float(d['brut_cp'])
    n = ok = 0
    dedans = False
    for l in open(REGISTRE, encoding='utf-8'):
        if l.startswith('## 14.'):
            dedans = True
        elif dedans and l.startswith('## '):
            break
        if not (dedans and l.startswith('- **D')):
            continue
        m = re.match(r'- \*\*(D\d+)\*\* :', l)
        if not m:
            continue
        cel = m.group(1)
        for prog, cat, k, k2 in re.findall(r'(\d+)/(\d+) `A!K(\d+)/L(\d+)`', l):
            n += 1
            r = A.get(int(k))
            motifs = []
            if not r or k != k2:
                motifs.append('ligne absente')
            else:
                if (r['C'], r['F']) != (prog, cat):
                    motifs.append(f"porte {r['C']}/{r['F']}")
                if r['J'] != 'arrêté':
                    motifs.append(f"statut « {r['J']} »")
                b = brut.get((prog, cat))
                if b is None:
                    motifs.append('sans ligne à la table de paramètres')
                elif abs(float(r['K']) * 1e6 - b[0]) > 1 or abs(float(r['L']) * 1e6 - b[1]) > 1:
                    motifs.append(f"arrêté {float(r['K']):.3f} / {float(r['L']):.3f} M€, table "
                                  f"{b[0] / 1e6:.3f} / {b[1] / 1e6:.3f}")
            ok += not motifs
            if motifs:
                print(f"{cel} {prog}/{cat} A!K{k} : " + ' ; '.join(motifs))
    print(f"{n} repères `A!` du § 14 rejoués, {ok} concordants, {n - ok} en écart.")
    return 0 if n == ok else 1


def main(argv):
    if argv and argv[0] == 'reperes':
        return reperes()
    if not argv or argv[0] == 'controler':
        cible = argv[argv.index('--cible') + 1] if '--cible' in argv else 'classeur'
        return 1 if controler(cible) else 0
    if argv[0] == 'construire':
        return construire(argv[1], argv[2])
    if argv[0] == 'faute':
        return faute(argv[argv.index('--cible') + 1] if '--cible' in argv else 'projet')
    if argv[0] == 'ecarts':
        return ecarts()
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
