# -*- coding: utf-8 -*-
"""Contrôle A — conformité au corpus : la checklist des quinze lignes.

Source de la checklist : `methode/regles_redactionnelles.md` et ses reprises du
20261007, telles que la passe du 20261008 les a mécanisées
(`methode/etats/NUIT_3B_controles_1_2_20261008.md`, § 2.1). Les quinze lignes
gardent leur numéro R1 à R15 : **l'écart entre les deux passes est la preuve**,
et il ne se lit que si la numérotation ne bouge pas.

Périmètre : **les dispositifs des 31 rangs, et eux seuls**. Aucun exposé, aucun
cartouche, aucun bloc interne.

Le contrôle **ne corrige rien** et ne lit aucun fichier qu'il aurait écrit.
"""
import re

from liasse import RANGS, lire, normaliser, segments

CONJONCTIONS = ('et', 'ou', 'mais', 'ni', 'car', 'or', 'donc')
DATES_COMMUNES = ('1er janvier 2027', '1er janvier 2028',
                  '1er juillet 2027', '1er janvier 2029')
# Exceptions de date inscrites à `livrables/registre_exceptions_dates.md`.
# Une exemption vit ici, nommée et motivée, jamais ajoutée à l'exécution.
EXCEPTIONS_DATES = {
    ('P1-23', '1er juillet 2028'): 'marche 2 des taux réduits de TVA, registre des exceptions',
    ('P1-23', '1er juillet 2029'): 'marche 3 des taux réduits de TVA, registre des exceptions',
    ('P1-23', '1er juillet 2030'): 'marche 4 des taux réduits de TVA, registre des exceptions',
}

RE_DATE = re.compile(r'\b(1er|[0-9]{1,2})(?:er)?\s+'
                     r'(janvier|février|mars|avril|mai|juin|juillet|août|'
                     r'septembre|octobre|novembre|décembre)\s+(\d{4})\b')
RE_MILLESIME = re.compile(r'n°\s*\d{2,4}-\d+\s+du\s+$')
RE_PHRASE = re.compile(r'[^.!?]+[.!?]')


def _phrases(texte):
    propre = re.sub(r'^\s*>?\s*\|.*$', '', texte, flags=re.M)      # tableaux
    propre = re.sub(r'^\s*>?\s*[-*]\s', ' ', propre, flags=re.M)
    for m in RE_PHRASE.finditer(propre):
        yield m.group(0).strip()


def controler(rang):
    """Rend la liste des écarts du rang, un dict par écart."""
    brut = lire(rang)
    # `brut` garde les espaces insécables : R4, R5 et R6 se mesurent dessus, et
    # une normalisation avant mesure les effacerait. Les autres lignes se jouent
    # sur le texte normalisé, où une insécable ne casse pas un motif.
    d_brut = segments(brut, rang)['dispositif']
    seg = segments(normaliser(brut), rang)
    d = seg['dispositif']
    ecarts = []

    def ec(ligne, libelle, extrait, correction, nature='écart'):
        ecarts.append({'rang': rang, 'ligne': ligne, 'libelle': libelle,
                       'extrait': extrait.strip()[:220], 'correction': correction,
                       'nature': nature})

    # R1 — rédaction positive : antithèses et qualifications par la négative.
    for m in re.finditer(r'ne\s+(?:se\s+)?\w+\s+(?:pas|plus)\b[^.]{0,60}?\bmais\b'
                         r'|\bne\s+constitue\s+ni\b|\bne\s+tient\s+pas\s+à\b',
                         d, re.I):
        ec('R1', 'rédaction positive', d[max(0, m.start() - 60):m.end() + 60],
           'énoncer ce que la règle fait')

    # R2 — virgule devant une conjonction de coordination.
    # Toute occurrence est un écart. La clôture d'incise est la seule exception
    # de la règle, et elle se lit : le contrôle ne la présume pas, parce qu'une
    # exemption présumée laisse passer exactement ce qu'on cherche.
    for m in re.finditer(r',\s+(?:' + '|'.join(CONJONCTIONS) + r')\b', d):
        ec('R2', 'virgule devant conjonction',
           d[max(0, m.start() - 110):m.end() + 70],
           'retirer la virgule, ou la retenir si elle clôt une incise')

    # R3 — point-virgule au texte normatif, hors énumération légistique.
    for m in re.finditer(r';', d):
        # Seule exception inscrite : le point-virgule qui sépare les termes
        # d'une énumération légistique — 1° … ; 2° …. Elle se lit **sur ce qui
        # suit** : un point-virgule dans une phrase citée entre guillemets est
        # du texte normatif comme un autre, et l'exempter laissait passer
        # exactement ce que la règle vise.
        apres = d[m.end():m.end() + 90]
        if re.match(r'\s*(?:»\s*)?(?:\n\s*)?(?:>\s*)?(?:\*\*)?\s*(?:\d+°|[a-z]\)|[A-Z]\.\s|[IVX]+\.)',
                    apres):
            continue
        ec('R3', 'point-virgule au texte normatif',
           d[max(0, m.start() - 110):m.end() + 70], 'scinder en deux phrases')

    # R4 — apostrophe droite.
    n = d_brut.count("'")
    if n:
        ec('R4', 'apostrophe droite', f'{n} occurrence(s)',
           "substitution ' → ’ en une passe de typographie unique")

    # R5 — guillemet droit.
    n = d_brut.count('"')
    if n:
        ec('R5', 'guillemet droit', f'{n} occurrence(s)', 'guillemets français')

    # R6 — espaces insécables devant la ponctuation haute, % et €,
    # et à l'intérieur des guillemets français.
    manquantes = (len(re.findall(r'(?<=\S)[ ][;:!?»%€]', d_brut))
                  + len(re.findall(r'«[ ]', d_brut)))
    if manquantes:
        ec('R6', 'espace insécable manquante', f'{manquantes} occurrence(s)',
           'passe de typographie à l’export, jamais pièce par pièce')

    # R7 — formule réglementaire au lieu de « est ainsi rédigé ».
    for m in re.finditer(r'est remplacé par les dispositions suivantes', d, re.I):
        ec('R7', 'formule réglementaire', d[max(0, m.start() - 80):m.end() + 40],
           '« est ainsi rédigé »')

    # R8 — abroger un texte ou une division numérotée, supprimer ce qui est dedans.
    for m in re.finditer(r'([^.»\n]{0,120}?)\b(?:est|sont)\s+'
                         r'(abrogée?s?|supprimée?s?)\b', d):
        sujet = re.sub(r'^\s*(?:>|\*\*|[-–—]|\d+°|[a-z]\)|«)\s*', '', m.group(1)).strip()
        tete = sujet.lower()
        verbe = 'abroger' if m.group(2).startswith('abrog') else 'supprimer'
        article = bool(re.match(r"(?:l[’']|le[s]?\s+)?articles?\b", tete)) or tete.startswith('chapitre') \
            or tete.startswith('section') or tete.startswith('titre') or tete.startswith('livre')
        interieur = bool(re.match(r"(?:l[’']|le[s]?\s+|la\s+|du\s+)?"
                                  r'(alinéa|phrase|mot|membre|dernier|second|premier|deuxième|troisième)',
                                  tete))
        if article and verbe == 'supprimer':
            ec('R8', 'supprimer employé pour un texte ou une division numérotée',
               m.group(0), '« est abrogé »')
        if interieur and verbe == 'abroger':
            ec('R8', 'abroger employé pour ce qui est à l’intérieur d’un article',
               m.group(0), '« est supprimé »')

    # R9 — aucune date au 31 décembre.
    for m in RE_DATE.finditer(d):
        if m.group(1) == '31' and m.group(2) == 'décembre':
            ec('R9', 'date au 31 décembre', d[max(0, m.start() - 90):m.end() + 60],
               'reporter au 1er janvier suivant')

    # R10 — dates au 1er janvier ou 1er juillet, sauf exception inscrite.
    for m in RE_DATE.finditer(d):
        date = f'{m.group(1)} {m.group(2)} {m.group(3)}'.replace('1er', '1er')
        if RE_MILLESIME.search(d[max(0, m.start() - 40):m.start()]):
            continue                                  # millésime d'un texte cité
        if date in DATES_COMMUNES:
            continue
        if (rang, date) in EXCEPTIONS_DATES:
            continue
        jour_valide = m.group(1) == '1er' and m.group(2) in ('janvier', 'juillet')
        ec('R10', 'date hors des quatre dates communes'
           + ('' if jour_valide else ' et hors de la règle du jour'),
           d[max(0, m.start() - 90):m.end() + 60],
           'inscrire au registre des exceptions, ou recaler sur une date commune')

    # R11 — « doit » et futur de l'indicatif au texte normatif.
    for m in re.finditer(r'\b(doit|doivent)\b|\b\w+(?:era|eront|ira|iront)\b', d):
        cite = d[max(0, m.start() - 200):m.start()].count('«') > \
            d[max(0, m.start() - 200):m.start()].count('»')
        ec('R11', 'obligation en « doit » ou futur de l’indicatif',
           d[max(0, m.start() - 80):m.end() + 60], 'présent de l’indicatif',
           'repris du droit en vigueur' if cite else 'écart')

    # R12 — une phrase une norme : plus de 65 mots.
    # Exemption nommée : une énumération nominative d'articles ou de lignes de
    # tarif n'est pas une phrase longue. La forme fondue arrêtée au lot 19 fait
    # de chaque rang une norme, et l'énumération n'en est que le véhicule.
    for p in _phrases(d):
        n = len(p.split())
        if n <= 65:
            continue
        rangs = len(re.findall(r'\b\d+°', p))
        arts = len(re.findall(r'\b(?:L\.\s?)?\d+(?:-\d+)*\s+(?:bis|ter|quater|quinquies|'
                              r'sexies|septies|octies|nonies|decies|undecies|vicies)\b', p))
        if rangs >= 3 or arts >= 5:
            ec('R12', f'phrase de {n} mots', p[:200],
               'sans objet — énumération nominative, véhicule d’une norme par rang',
               'énumération, sans objet')
            continue
        ec('R12', f'phrase de {n} mots', p, 'scinder, une norme par phrase')

    # R13 — paramètre ouvert entre crochets, et taux à espace parasite.
    for m in re.finditer(r'\[[^\]]{1,40}\]', d):
        ec('R13', 'paramètre entre crochets', m.group(0),
           'décision politique à arrêter', 'marqué, conforme')
    for m in re.finditer(r'\d+,\s+\d+\s*%', d):
        ec('R13', 'espace parasite dans un taux', m.group(0),
           'retirer l’espace — contrôler le verbatim avant de corriger')

    # R14 / R15 — redondance entre niveaux et hiérarchie des normes : la liasse
    # est entièrement de niveau législatif. Contrôle mécanique : une disposition
    # qui prétendrait modifier la Constitution ou recopier un principe de la DDHC.
    for m in re.finditer(r'\bConstitution\b[^.]{0,60}\best ainsi (?:modifié|rédigé)',
                         d):
        ec('R15', 'disposition de niveau constitutionnel dans une liasse ordinaire',
           m.group(0), 'porter la mesure au véhicule de révision')
    for m in re.finditer(r"Déclaration des droits de l[’']homme[^.]{0,80}est ainsi", d):
        ec('R14', 'recopie d’un principe de niveau supérieur', m.group(0),
           'renvoyer, ne pas recopier')

    return ecarts


LIGNES = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8',
          'R9', 'R10', 'R11', 'R12', 'R13', 'R14', 'R15']


def jouer():
    tout = []
    for rang in sorted(RANGS):
        tout.extend(controler(rang))
    return tout


if __name__ == '__main__':
    import collections
    e = jouer()
    c = collections.Counter(x['ligne'] for x in e if x['nature'] == 'écart')
    for l in LIGNES:
        print(f'{l:>4} {c.get(l, 0):>5}')
    print('total écarts', sum(c.values()), '· signalés non écarts',
          sum(1 for x in e if x['nature'] != 'écart'))
