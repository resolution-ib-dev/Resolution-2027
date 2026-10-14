#!/usr/bin/env python3
"""Digère deux annexes des voies et moyens du PLF 2027 en référentiels plats.

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

Les cellules sont reprises **au verbatim** : aucun libellé n'est normalisé, ni
espace ni espace insécable. Un nombre entier s'écrit sans décimale. Un nombre
non entier s'écrit sous sa forme la plus courte qui se relit à l'identique. Les
montants restent dans l'unité du classeur : M€ pour les dépenses fiscales, euros
pour les ressources affectées. Les symboles de l'annexe (« - », « ε », « nc »)
sont repris tels quels. Une tabulation, un retour à la ligne ou une barre
oblique inverse se notent `\\t`, `\\n`, `\\r` et `\\\\` : l'échappement est
réversible, et `lire()` rend la cellule au verbatim.

Usage :
    python3 appareil/digerer_annexes_vm2027.py ecrire   <classeur DF 2027> <classeur RA 2027>
    python3 appareil/digerer_annexes_vm2027.py verifier <classeur DF 2027> <classeur RA 2027>

`verifier` régénère les deux tables en mémoire et les compare **à l'octet** aux
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


def cellule(v):
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
    i = next(k for k, l in enumerate(L) if l and not l.startswith('#') and k > 7)
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


def main(argv):
    mode, df, ra = argv[1:4]
    tables = ((SORTIE_DF, table_df(df)), (SORTIE_RA, table_ra(ra)))
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
