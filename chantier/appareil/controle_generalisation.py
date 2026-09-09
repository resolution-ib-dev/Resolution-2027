# -*- coding: utf-8 -*-
"""Contrôle `G` — une skill ne nomme ni déposant, ni projet, ni corpus interne.

Quatorze mentions d'un déposant nommé ont été rattrapées à la main, en deux
fois, dont la plus exposée : la **description enregistrée** de la skill, visible
dans toute liste de skills sans que le fichier soit ouvert. Une règle qu'on tient
à l'œil se perd. Elle devient donc mécanique, et le frontmatter est dans le
périmètre.

Deux rangs, et le partage est celui du risque.

  G1 à G6  ÉCHEC. Ce qui identifie quelqu'un ou quelque chose : un déposant
           nommé, le nom du projet, le manuscrit, le coffre, un référentiel
           interne, la nomenclature interne. Une skill qui en porte un n'est pas
           publiable, et le savoir après diffusion ne sert à rien.
  G7 à G8  SIGNALEMENT. Ce qui est seulement suspect : une étape dont rien ne
           dit qu'elle rend un résultat socle absent, un chemin de dépôt cité.
           Cela se juge, cela ne se prouve pas.

Les exemptions vivent ici et nulle part ailleurs. Une exemption qui vivrait dans
la skill contrôlée serait une porte que la skill s'ouvre elle-même. Deux formes,
et la seconde est bornée.

  - **générale** : le dépôt de droit public. Une skill qui lit le texte en
    vigueur doit nommer l'adresse qu'elle clone ; c'est une ressource publique,
    pas un référentiel interne.
  - **nommée** : un terme, dans une skill et une seule, avec son motif écrit.
    Elle ne vaut que là où elle est déclarée, et un même terme reste un échec
    partout ailleurs. Une exemption sans motif n'existe pas.

Usage : python3 controle_generalisation.py <fichier> [fichier ...]
        sortie non nulle dès qu'un échec existe.
"""
import io
import os
import re
import sys

# L'adresse publique du dépôt de droit, et elle seule. Les segments sont écrits
# séparément pour que ce module ne se dénonce pas lui-même à sa propre lecture.
EXEMPTIONS = (re.compile(r'https?://github\.com/[\w.-]+/[\w.-]+'),)

# Exemptions nommées — un terme, une skill, un motif. Bornées par construction :
# la clé est le nom déclaré au frontmatter, donc l'exemption ne peut pas fuir
# vers une autre skill.
# Vide, et c'est le bon état. La seule exemption qui ait jamais servi couvrait
# une skill qui nommait un référentiel interne comme source de niches de gage.
# `A-376` l'a rendue inutile : la skill nomme désormais **un rôle** — « un
# réservoir de niches » — et le dossier dit quel fichier le tient. Une exemption
# était le contournement d'un défaut de vocabulaire, pas une nécessité.
EXEMPTIONS_NOMMEES = {}

# ---------------------------------------------------------------------------
# LE PÉRIMÈTRE — quelles skills le rang ÉCHEC concerne
#
# Une skill interne n'a pas à se cacher son propre sujet : la procédure de
# travail parle du coffre et de l'appareil, c'est son objet et non une fuite.
# Une skill externalisable, elle, doit pouvoir servir un tiers — elle peut
# nommer la doctrine **ponctuellement**, à condition que la référence soit
# **contournable** : la skill dit ce qu'elle rend quand la base manque.
#
# Deux régimes depuis l'arbitrage du 20260907 : la famille de projection est
# interne. Deux réserves y sont portées et ne se perdent pas — `qa-riposte`
# admettrait une version neutre externalisable, non prioritaire ; la méthode de
# `contestabilite` est peut-être générique, sans emploi prévu ailleurs.
REGIME = {
    # Internes — leur entrée est notre doctrine ou notre atelier. Arbitré par
    # l'auteur le 20260907 : « en projection, pour l'essentiel c'est interne ».
    'resolution-chantier':     ('interne', "procédure de travail : le coffre et l'appareil sont son sujet"),
    'impression-docx':         ('interne', "outil d'atelier, jamais diffusé"),
    'compatibilite-doctrine':  ('interne', "la plus interne par définition — auteur, 20260907"),
    'fiche-mesure':            ('interne', "projette un nœud de doctrine ; l'objet voisin sur le texte déposé est un autre produit"),
    'audit-conformite':        ('interne', "contrôle un livrable contre le corpus ; non nommée par l'auteur, classée par le même motif"),
    'qa-riposte':              ('interne', "notre doctrine vaut ; une version neutre est imaginable, non prioritaire — auteur, 20260907"),
    'contestabilite':          ('interne', "usage interne ; sa méthode est peut-être générique, aucun emploi prévu ailleurs — auteur, 20260907"),
    # Externalisables — elles peuvent nommer la doctrine ponctuellement, à
    # condition que la référence soit contournable et le repli déclaré.
    'analyse-transposabilite': ('externalisable', "droit constitutionnel, pas notre doctrine"),
    'redaction-legistique':    ('externalisable', "légistique générale"),
    'vecteur-mesure':          ('externalisable', "rend une adresse de droit"),
    'disposition-cible':       ('externalisable', "rend une disposition modificative"),
    'expose-sommaire':         ('externalisable', "sert un auteur interne comme un tiers, déclaré au frontmatter"),
}

# Ce qui ne se contourne jamais, quel que soit le régime : un numéro de registre
# et le nom du projet ne veulent rien dire hors du corpus, et aucun repli ne les
# rattrape. Une skill diffusable qui en porte un est à corriger, pas à exempter.
INCONTOURNABLES = ('G2', 'G6')

ECHECS = [
    ('G1', 'déposant nommé', re.compile(
        r'g[ée]n[ée]ration\s*libre|generationlibre|\bGL-[IV]+-\d+|'
        r'\bGL\b|'
        r'contre-?budget\s+20\d\d', re.I)),
    ('G2', 'nom du projet', re.compile(
        r'(?:projet|chantier|corpus|mouvement|think\s*tank)\s+R[ée]solution|'
        r'France[- ]R[ée]solution|france-resolution|\bR[ÉE]SOLUTION\b')),
    ('G3', 'manuscrit ou doctrine interne', re.compile(
        r'\bmanuscrit\b|REF_doctrine|r[ée]f[ée]rentiel\s+des\s+positions|'
        r'notes?\s+de\s+fin\s+du\s+livre', re.I)),
    ('G4', 'coffre et appareil de session', re.compile(
        r'\bcoffre\b|make\s+coffre|project_read|technique/coffre|'
        r'\barchive\s+technique\b', re.I)),
    ('G5', 'référentiel interne', re.compile(
        r'REF_norme|REF_chiffres|REF_doctrine|socle_budgetaire|'
        r'\bpositions\.json\b|\beconomies\.json\b|lots_epreuve|'
        r'referentiels?/|appareil/|methode/', re.I)),
    ('G6', 'nomenclature interne', re.compile(
        r'\bD\d+(?:-\d+){1,3}(?:-[a-z]\d+)?\b|\bC-\d{2}\b|\bA-\d{1,3}\b|'
        r'\bM-\d{4}\b|\bN\d\b\s*(?:refuse|sort|voit|compte)')),
]

SIGNALEMENTS = [
    ('G7', 'aucune dégradation déclarée', None),   # traité à part : c'est une absence
    ('G8', 'chemin de dépôt cité', re.compile(
        r'\blivrables?/|\bsources?/|\bmanuscrit/|\bMakefile\b|make\s+controle')),
]

# Ce qui prouve qu'une étape rend un résultat quand la base documentaire manque.
DEGRADATION = re.compile(
    r'socle\s+absent|socle\s+non\s+disponible|sans\s+socle|'
    r'base\s+documentaire\s+absente|documentation\s+absente|'
    r'd[ée]grad', re.I)


NOM_FRONTMATTER = re.compile(r'^name:\s*([\w.-]+)\s*$', re.M)


def _nom_declare(texte, chemin):
    """Le nom que la skill déclare, à défaut celui de son répertoire."""
    m = NOM_FRONTMATTER.search(texte)
    if m:
        return m.group(1)
    return os.path.basename(os.path.dirname(os.path.abspath(chemin)))


def _masquer(texte, nom=None):
    """Retire du texte ce qu'une exemption couvre, avant toute recherche."""
    for motif in EXEMPTIONS:
        texte = motif.sub(' ', texte)
    for motif, _motif_ecrit in EXEMPTIONS_NOMMEES.get(nom, ()):
        texte = motif.sub(' ', texte)
    return texte


def _lignes(texte, motif):
    """Numéro de ligne et extrait, pour chaque occurrence."""
    trouve = []
    for n, ligne in enumerate(texte.splitlines(), 1):
        m = motif.search(ligne)
        if m:
            trouve.append((n, m.group(0), ligne.strip()[:78]))
    return trouve


def controler(chemin):
    brut = open(chemin, encoding='utf-8').read()
    texte = _masquer(brut, _nom_declare(brut, chemin))
    echecs, signalements = [], []
    for code, quoi, motif in ECHECS:
        for n, extrait, ligne in _lignes(texte, motif):
            echecs.append((code, quoi, n, extrait, ligne))
    for code, quoi, motif in SIGNALEMENTS:
        if motif is None:
            continue
        for n, extrait, ligne in _lignes(texte, motif):
            signalements.append((code, quoi, n, extrait, ligne))
    nomme_une_base = any(c in ('G3', 'G5') for c, _q, _n, _x, _l in echecs)
    if nomme_une_base and not DEGRADATION.search(texte):
        signalements.append(('G7', 'aucune dégradation déclarée', 0, '', ''))
    return echecs, signalements


def regime(nom):
    return REGIME.get(nom, ('externalisable', 'non déclaré au périmètre'))


def _dedoublonner(chemins):
    """Un même fichier atteint par deux racines ne se contrôle qu'une fois."""
    vus, garde = set(), []
    for c in chemins:
        reel = os.path.realpath(c)
        if reel not in vus:
            vus.add(reel)
            garde.append(c)
    return garde


def releve(fichiers):
    """L'audit : par skill, son régime, ce qui est nu et ce qui est contournable."""
    import collections
    lignes, tot = [], collections.Counter()
    for chemin in fichiers:
        brut = open(chemin, encoding='utf-8').read()
        nom = _nom_declare(brut, chemin)
        if nom not in REGIME:
            continue
        echecs, signalements = controler(chemin)
        par = collections.Counter(c for c, _q, _n, _x, _l in echecs)
        nu = sum(par[c] for c in INCONTOURNABLES)
        chemins = sum(1 for c, _q, _n, x, _l in echecs
                      if c == 'G5' and x.endswith('/'))
        doctrine = len(echecs) - nu - chemins
        reg, motif = regime(nom)
        repli = not any(c == 'G7' for c, _q, _n, _x, _l in signalements)
        lignes.append((nom, reg, len(echecs), nu, chemins, doctrine, repli, motif))
        tot['echecs'] += len(echecs)
        tot['nu'] += nu
        tot['chemins'] += chemins
        tot['doctrine'] += doctrine
    ordre = {'externalisable': 0, 'a_trancher': 1, 'interne': 2}
    lignes.sort(key=lambda l: (ordre[l[1]], -l[2]))
    print('RELEVÉ DE GÉNÉRALISATION — par skill, et par nature de ce qui fuit')
    print()
    print('  nu        : nom du projet, numéro de registre. Aucun repli ne les')
    print('              rattrape ; ils se suppriment.')
    print('  chemin    : une adresse du dépôt. Se remplace par ce que le fichier')
    print('              porte.')
    print('  doctrine  : manuscrit, référentiel. Admis dans une skill')
    print('              externalisable **si la référence est contournable**,')
    print('              c\'est-à-dire si le repli est déclaré.')
    print()
    print(f"{'skill':<25}{'régime':<16}{'éch':>5}{'nu':>5}{'chemin':>8}"
          f"{'doctr.':>8}  repli")
    reg_vu = None
    for nom, reg, e, nu, ch, doc, repli, motif in lignes:
        if reg != reg_vu:
            print(f'  — {reg} —')
            reg_vu = reg
        etat = 'déclaré' if repli else ('—' if doc == 0 else 'ABSENT')
        print(f"{nom:<25}{reg:<16}{e:>5}{nu:>5}{ch:>8}{doc:>8}  {etat}")
    print()
    print(f"total : {tot['echecs']} échecs — {tot['nu']} nus, "
          f"{tot['chemins']} chemins, {tot['doctrine']} doctrine")
    return 0


def main(argv):
    argv = list(argv)
    mode_releve = '--releve' in argv
    if mode_releve:
        argv.remove('--releve')
    fichiers = _dedoublonner(argv[1:])
    if mode_releve:
        return releve(fichiers)
    if not fichiers:
        print('G — AUCUN FICHIER DE SKILL ATTEINT : le contrôle n\'a rien vu.')
        print('    Ce n\'est pas un succès. Une skill enregistrée hors du dépôt '
              'échappe au contrôle')
        print('    tant qu\'aucun chemin ne la lui donne — voir SKILLS au '
              'Makefile.')
        return 0
    total_e = total_s = 0
    internes = []
    for chemin in fichiers:
        try:
            echecs, signalements = controler(chemin)
        except OSError as exc:
            print(f'G — illisible : {exc}')
            return 1
        try:
            brut = io.open(chemin, encoding='utf-8').read()
        except OSError:
            brut = ''
        reg, motif = regime(_nom_declare(brut, chemin))
        if reg == 'interne':
            internes.append((chemin, len(echecs), motif))
            continue
        total_e += len(echecs)
        total_s += len(signalements)
        print(f'{chemin} — {len(echecs)} échec(s), '
              f'{len(signalements)} signalement(s)')
        for code, quoi, n, extrait, ligne in echecs:
            print(f'    ÉCHEC {code} {quoi} — ligne {n} : « {extrait} »')
            print(f'          {ligne}')
        for code, quoi, n, extrait, ligne in signalements:
            if code == 'G7':
                print(f'    signal {code} {quoi} — rien ne dit ce que la skill '
                      f'rend quand la base documentaire manque')
            else:
                print(f'    signal {code} {quoi} — ligne {n} : « {extrait} »')
    if internes:
        print()
        print(f'Hors périmètre — {len(internes)} skill(s) interne(s), '
              f'{sum(n for _c, n, _m in internes)} renvoi(s) au corpus, '
              'attendus :')
        for chemin, n, motif in sorted(internes):
            print(f'    {os.path.basename(os.path.dirname(chemin))} — '
                  f'{n} renvoi(s) ; {motif}')
    print()
    print(f'G — {len(fichiers) - len(internes)} skill(s) diffusable(s) '
          f'contrôlée(s), {total_e} échec(s), {total_s} signalement(s)')
    if total_e:
        print('Une skill qui nomme un déposant, un projet ou un référentiel '
              'interne n\'est pas publiable.')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
