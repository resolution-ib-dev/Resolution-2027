# -*- coding: utf-8 -*-
"""Le périmètre du fil 1 : les 31 rangs actifs de la colonne PLF 2027 première partie.

La table des rangs ne se relève pas de l'arborescence : elle est **prise au
registre des colonnes**, `livrables/registre_colonnes_depot_2027.md`, § I, qui
fait foi sur le rang et la colonne de chaque pièce. Les six rangs vacants et
barrés — P1-02, P1-03, P1-12, P1-22, P1-24, P1-29 — n'y sont pas, et les trois
fichiers qui les portaient encore ne sont pas du périmètre.

Un fichier porte parfois deux rangs : la clause générale porte P1-31 (article 1er)
et P1-04 (article 3). Le contrôle se joue sur le fichier et se rend par rang.

La segmentation est celle du 20261008 (`NUIT_3B`, § 0) : du marqueur d'ouverture
d'un amendement jusqu'à `EXPOSÉ SOMMAIRE`, `[interne]` ou `ANNEXE`. Elle est
reprise à l'identique pour que les deux passes se comparent.
"""
import os
import re

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Le jeu de fautes rejoue les contrôles sur une copie du paquet où une faute
# connue a été injectée. Il la désigne par cette variable ; rien d'autre ne la
# pose, et la passe de production lit toujours le paquet du coffre.
PAQUET = os.environ.get('RESOLUTION_PAQUET') or os.path.join(RACINE, 'livrables', 'depot_2027')

# rang -> (chemin relatif au paquet, intitulé court, lot)
RANGS = {
    'P1-01': ('P1/4_3_aide_fondamentale_et_taux_unique.md', 'aide fondamentale et taux unique', '4.3'),
    'P1-04': ('clause_generale_niches_20261005.md', 'titres périmés — clause générale, article 3', '3.1'),
    'P1-05': ('P1/nuitp1_01_rendre_le_don.md', 'rendre le don à celui qui donne', '2.3'),
    'P1-06': ('P1/4_2_refonte_taxes_C_dmto_franchise.md', 'refonte des taxes — droits de mutation et franchise', '4.2 C'),
    'P1-07': ('P1/n5_compte_epargne_personnel.md', "compte d'épargne personnel", '5'),
    'P1-08': ('P1/nuitp1_04_pret_taux_zero.md', "niche de l'article 7", '2.4'),
    'P1-09': ('P1/4_2_refonte_taxes_D_plus_values.md', 'refonte des taxes — plus-values et objets précieux', '4.2 D'),
    'P1-10': ('P1/nuitp1_05_investissement_industriel.md', "niche de l'article 9", '2.4'),
    'P1-11': ('P1/nuitp1_06_cession_reprise_entreprise.md', "niche de l'article 10", '2.4'),
    'P1-13': ('P1/nuitp1_08_avantages_culturels.md', "niche de l'article 12", '2.4'),
    'P1-14': ('P1/nuitp1_09_impot_agricole.md', "niche de l'article 13", '2.4'),
    'P1-15': ('P1/2_4_credit_impot_recherche.md', "fin du crédit d'impôt recherche", '2.4'),
    'P1-16': ('P1/2_4_exonerations_par_zone.md', "exonérations d'impôt par zone", '2.4'),
    'P1-17': ('P1/2_4_armateurs_tonnage.md', "armateurs à l'impôt sur les sociétés", '2.4'),
    'P1-18': ('P1/2_4_credit_impot_famille.md', "crédit d'impôt famille", '2.4'),
    'P1-19': ('P1/2_4_deductions_exceptionnelles.md', 'déductions exceptionnelles', '2.4'),
    'P1-20': ('P1/2_4_tarifs_reduits_accise.md', "tarifs réduits d'accise", '2.4'),
    'P1-21': ('P1/2_4_sortie_agricole_trois_ans.md', 'sortie agricole en trois ans', '2.4'),
    'P1-23': ('P1/4_6_tva_taux_reduits.md', 'taux réduits de TVA de droit commun', '4.6'),
    'P1-25': ('P1/4_2_refonte_taxes_A_taxes_etat.md', "refonte des taxes — taxes de l'État", '4.2 A'),
    'P1-26': ('sans_colonne/n7b_m022_certificats_energie.md', "certificats d'économies d'énergie", '2.5'),
    'P1-27': ('P1/nuitp1_10_impot_selon_adresse.md', "niche de l'article 26", '2.4'),
    'P1-28': ('P1/4_4_taxe_fonciere_unique.md', 'taxe foncière unique', '4.4'),
    'P1-30': ('P1/4_5_solde_refonte_is_tf.md', 'solde de la refonte — IS et taxe foncière', '4.5'),
    'P1-31': ('clause_generale_niches_20261005.md', "clause générale d'abolition des niches, article 1er", '3.1'),
    'P1-32': ('P1/coll_P1_01_dotations_face_aux_reductions_de_champ.md', 'dotations face aux réductions de champ', 'collectivités'),
    'P1-33': ('P2/coll_P2_04_facultes_et_obligations_de_baisse.md', 'facultés et obligations de baisse', 'collectivités'),
    'P1-34': ('P1/coll_P1_02_fusion_dotation_forfaitaire_taxe_fonciere.md', 'fusion dotation forfaitaire / taxe foncière', 'collectivités'),
    'P1-35': ('P1/coll_P1_03_tva_sur_justification.md', 'TVA des collectivités, sur justification', 'collectivités'),
    'P1-36': ('P1/nuitp1_12_affectation_article_42.md', "affectation et recette de l'article 42", '4.1'),
    'P1-37': ('P1/4_2_refonte_taxes_B_taxes_affectees.md', 'refonte des taxes — taxes affectées', '4.2 B'),
}

# accroche au texte déposé n° 3210, prise au registre des colonnes § I.
# ('article', numéro) pour une accroche sur article du texte ;
# ('additionnel', numéro) pour un article additionnel après l'article n.
ACCROCHES = {
    'P1-01': [('article', 2)],
    'P1-04': [('additionnel', 2)],
    'P1-05': [('article', 4)],
    'P1-06': [('additionnel', 4)],
    'P1-07': [('additionnel', 6)],
    'P1-08': [('article', 7)],
    'P1-09': [('additionnel', 8)],
    'P1-10': [('article', 9)],
    'P1-11': [('article', 10)],
    'P1-13': [('article', 12)],
    'P1-14': [('article', 13)],
    'P1-15': [('additionnel', 13)],
    'P1-16': [('additionnel', 13)],
    'P1-17': [('additionnel', 13)],
    'P1-18': [('additionnel', 13)],
    'P1-19': [('additionnel', 13)],
    'P1-20': [('additionnel', 13)],
    'P1-21': [('additionnel', 13)],
    'P1-23': [('additionnel', 16)],
    'P1-25': [('additionnel', 19)],
    'P1-26': [('additionnel', 24)],
    'P1-27': [('article', 26)],
    'P1-28': [('additionnel', 27)],
    'P1-30': [('additionnel', 32)],
    'P1-31': [('additionnel', 33)],
    'P1-32': [('article', 34), ('additionnel', 34)],
    'P1-33': [('additionnel', 34)],
    'P1-34': [('additionnel', 34)],
    'P1-35': [('article', 36)],
    'P1-36': [('article', 42)],
    'P1-37': [('additionnel', 42)],
}

VACANTS = ('P1-02', 'P1-03', 'P1-12', 'P1-22', 'P1-24', 'P1-29')

OUVRE = re.compile(r'^\s*>?\s*(?:#{1,6}\s*)?(?:\*\*)?(AMENDEMENT|PROPOSITION DE LOI)\b', re.M)
FERME = re.compile(r'^\s*>?\s*(?:#{1,6}\s*)?(?:\*\*)?(EXPOSÉ SOMMAIRE|EXPOSE SOMMAIRE|\[interne\]|##\s*\[interne\]|ANNEXE)\b', re.M)
EXPOSE = re.compile(r'^\s*>?\s*(?:#{1,6}\s*)?(?:\*\*)?(EXPOSÉ SOMMAIRE|EXPOSE SOMMAIRE)\b', re.M)
INTERNE = re.compile(r'^\s*>?\s*(?:#{1,6}\s*)?\[interne\]', re.M)


def normaliser(t):
    return t.replace(' ', ' ').replace(' ', ' ')


def lire(rang):
    rel = RANGS[rang][0]
    with open(os.path.join(PAQUET, rel), encoding='utf-8') as f:
        return f.read()


def fichiers():
    """chemin relatif -> liste des rangs qu'il porte, dans l'ordre des rangs."""
    d = {}
    for rang in sorted(RANGS):
        d.setdefault(RANGS[rang][0], []).append(rang)
    return d


# Deux rangs vivent dans le même fichier et s'y découpent par division : la
# clause générale porte l'article 1er au § 2 et l'article 3 au § 5. L'article 2,
# § 4, est la jambe sociale SS-01 — hors colonne de première partie.
DECOUPE = {
    'P1-31': (r'^## 2\. Article 1er\b', r'^## 3\.'),
    'P1-04': (r'^## 5\. Article 3\b', r'^## 6\.'),
}

HORS_PIECE = 'hors pièce déposée'


def dispositifs(texte, rang=None):
    """Les blocs de dispositif : (début, fin) dans le texte.

    Un bloc dont la tête se déclare « hors pièce déposée » est un cartouche de
    travail et non un dispositif : les sept pièces du lot 2.4 ouvrent par un
    titre `# AMENDEMENT` suivi d'un cartouche de ce genre, avant le vrai
    dispositif. Le compter ferait sept dispositifs de plus qui n'existent pas.
    """
    if rang in DECOUPE:
        a = re.compile(DECOUPE[rang][0], re.M).search(texte)
        b = re.compile(DECOUPE[rang][1], re.M).search(texte, a.end()) if a else None
        if not a:
            return []
        portion = texte[a.start(): b.start() if b else len(texte)]
        decalage = a.start()
        trouves = dispositifs(portion)
        if not trouves:
            # Une division sans cartouche d'amendement : le dispositif est le
            # premier bloc cité, jusqu'à l'exposé sommaire. Le cartouche manquant
            # est un écart, relevé par le contrôle de conformité (ligne R16), non
            # une raison de ne pas contrôler la norme.
            mc = re.search(r'^> ', portion, re.M)
            if mc:
                me = EXPOSE.search(portion, mc.start())
                fin = me.start() if me else len(portion)
                # Seules les lignes citées sont du dispositif : la prose qui les
                # entoure est du commentaire de pièce, et la compter ferait
                # sortir en écart rédactionnel des phrases qui ne se déposent
                # pas.
                debut = mc.start()
                dernier = debut
                for lm in re.finditer(r'^>.*$', portion[debut:fin], re.M):
                    dernier = debut + lm.end()
                trouves = [(debut, dernier)]
        return [(decalage + d, decalage + f) for d, f in trouves]
    blocs = []
    ouvertures = [m.start() for m in OUVRE.finditer(texte)]
    for i, debut in enumerate(ouvertures):
        suivante = ouvertures[i + 1] if i + 1 < len(ouvertures) else len(texte)
        fin = suivante
        m = FERME.search(texte, debut + 1)
        if m and m.start() < fin:
            fin = m.start()
        if fin <= debut:
            continue
        if HORS_PIECE in texte[debut:debut + 300]:
            continue
        blocs.append((debut, fin))
    return blocs


def segments(texte, rang=None):
    """cartouche / dispositif / exposé / interne, en texte."""
    blocs = dispositifs(texte, rang)
    if rang in DECOUPE:
        a = re.compile(DECOUPE[rang][0], re.M).search(texte)
        b = re.compile(DECOUPE[rang][1], re.M).search(texte, a.end()) if a else None
        if a:
            debut, fin = a.start(), (b.start() if b else len(texte))
            portion = texte[debut:fin]
            disp = ''.join(texte[x:y] for x, y in blocs)
            exp = []
            for m in EXPOSE.finditer(portion):
                exp.append(portion[m.start():])
            cart = texte[debut: blocs[0][0]] if blocs else portion
            return {'cartouche': cart, 'dispositif': disp,
                    'expose': '\n'.join(exp), 'interne': '', 'tout': portion}
    disp = ''.join(texte[a:b] for a, b in blocs)
    cartouche = texte[:blocs[0][0]] if blocs else texte
    exp = []
    for m in EXPOSE.finditer(texte):
        m2 = INTERNE.search(texte, m.end())
        m3 = re.compile(r'^\s*#{1,6}\s*ANNEXE\b', re.M).search(texte, m.end())
        bornes = [x.start() for x in (m2, m3) if x]
        o = OUVRE.search(texte, m.end())
        if o:
            bornes.append(o.start())
        exp.append(texte[m.start(): min(bornes) if bornes else len(texte)])
    interne = ''
    mi = INTERNE.search(texte)
    if mi:
        interne = texte[mi.start():]
    return {'cartouche': cartouche, 'dispositif': disp,
            'expose': '\n'.join(exp), 'interne': interne, 'tout': texte}


if __name__ == '__main__':
    print(f'{len(RANGS)} rangs actifs · {len(fichiers())} fichiers · '
          f'{len(VACANTS)} rangs vacants barrés hors périmètre')
    tot = octets = 0
    for rang in sorted(RANGS):
        t = normaliser(lire(rang))
        b = dispositifs(t, rang)
        tot += len(b)
        o = sum(y - x for x, y in b)
        octets += o
        print(f'  {rang}  {len(b)} bloc(s)  {o:>7} o  {RANGS[rang][0]}')
    print(f'{tot} amendements · {octets} octets de dispositif')
