#!/usr/bin/env python3
"""Chasse au siège juridique d'une imposition, sur le texte en vigueur.

Inscrit le 20261016, après un fil qui a cherché des mots au lieu d'ouvrir
des divisions — septième garde-fou de CLAUDE.md. Cet outil ne lève pas
l'interdit : il l'encadre. Ce qu'il rend est une LISTE DE CANDIDATS, jamais
un siège. Un siège ne s'inscrit qu'après réouverture de l'article par
`droit.article` et lecture de son texte.

Trois voies, dans cet ordre :

  1. `annexe` — appariement sur la colonne `ressource_libelle` de
     `referentiels/annexe_ressources_affectees_2027.tsv`, qui porte la
     colonne `reference_juridique`. Ne couvre que les ressources affectées
     à un tiers. Rend le mode d'appariement : exact, ou variante.
  2. `codes` — recherche plein texte sur les articles APPLICABLES du dépôt
     de droit. L'applicabilité se lit à `droit.applicable`, jamais à
     l'état : un article ABROGE_DIFF s'applique aujourd'hui.
  3. `renvoi` — un article du dépôt qui NOMME un texte hors dépôt vaut
     relevé par renvoi exprès ; c'est ainsi que l'article 3 de la loi
     n° 72-657 a été relevé, nommé par l'article L. 135 Y du livre des
     procédures fiscales.

Le classement des candidats se fait par longueur de texte croissante : un
article d'institution est court, un état A fait deux cent mille signes. Le
tri par mots d'institution a été essayé et il remonte du bruit.

Usage :
    python3 appareil/chasse_siege.py annexe "<libellé>"
    python3 appareil/chasse_siege.py codes "<mot>" "<mot>" [...]
    python3 appareil/chasse_siege.py renvoi "<mot>" "<mot>" [...]
"""
import csv, difflib, gzip, json, re, sys, unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / 'depot'))
try:
    import droit
except ImportError:
    sys.exit("dépôt de droit absent : jouer le clone avant (methode/carte_du_depot.md).")

DATA = Path(droit.__file__).resolve().parent / 'data'
ANNEXE = RACINE / 'referentiels/annexe_ressources_affectees_2027.tsv'
SEUIL_VARIANTE = 0.90

_corpus = []


def norm(s):
    s = unicodedata.normalize('NFKD', str(s))
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('’', "'").replace(' ', ' ').lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def corpus():
    """Les articles applicables ce jour, tous textes du dépôt."""
    if _corpus:
        return _corpus
    for f in sorted(DATA.glob('*.jsonl.gz')):
        for ligne in gzip.open(f, 'rt', encoding='utf-8'):
            a = json.loads(ligne)
            if not droit.applicable(a):
                continue
            _corpus.append({
                'code': a['code'], 'num': a['num'], 'id': a['id'],
                'texte': a.get('texte', ''), 'n': norm(a.get('texte', '')),
                'section': a.get('section', ''),
            })
    return _corpus


def lire_annexe():
    lignes = []
    with open(ANNEXE, encoding='utf-8') as f:
        for ligne in f:
            if not ligne.startswith('#'):
                lignes.append(ligne)
    return list(csv.DictReader(lignes, delimiter='\t'))


def par_annexe(libelle):
    """Candidat tiré de la colonne `reference_juridique` de l'annexe.

    Rend (reference, mode) ou None. `mode` vaut 'exact' ou 'variante' ; une
    variante se déclare à l'inscription, elle ne se tait pas.
    """
    index = {}
    for r in lire_annexe():
        ref = r['reference_juridique'].strip()
        if ref:
            index.setdefault(norm(r['ressource_libelle']), []).append(ref)
    cle = norm(libelle)
    if cle in index:
        return index[cle], 'exact'
    proche = difflib.get_close_matches(cle, list(index), n=1, cutoff=SEUIL_VARIANTE)
    if proche:
        return index[proche[0]], 'variante'
    return None


def par_codes(*mots, limite=6):
    """Articles applicables dont le texte porte TOUS les mots. Plus courts d'abord."""
    cles = [norm(m) for m in mots if norm(m)]
    if not cles:
        return []
    trouves = [a for a in corpus() if all(c in a['n'] for c in cles)]
    trouves.sort(key=lambda a: len(a['texte']))
    return trouves[:limite]


def par_renvoi(*mots, limite=6):
    """Articles applicables qui nomment une loi ou une ordonnance non codifiée.

    Sert aux impositions dont le siège est hors des textes portés : l'article
    qui les nomme fait preuve de l'adresse, non du verbatim.
    """
    motif = re.compile(r"(loi|ordonnance|décret)\s+n°\s*\d{2,4}-\d+", re.I)
    sortie = []
    for a in par_codes(*mots, limite=limite * 4):
        nommes = motif.findall(a['texte'])
        if nommes:
            sortie.append(a)
    return sortie[:limite]


def rendre(articles):
    for a in articles:
        print(f"  {a['code']} | art. {a['num']} | {a['id']} | {len(a['texte'])} signes")
        print('     ', a['texte'][:220].replace('\n', ' '))


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    voie, args = argv[1], argv[2:]
    if voie == 'annexe':
        r = par_annexe(args[0])
        if not r:
            print('  aucun candidat à l’annexe.')
        else:
            refs, mode = r
            for ref in dict.fromkeys(refs):
                print(f'  [{mode}] {ref}')
    elif voie == 'codes':
        rendre(par_codes(*args))
    elif voie == 'renvoi':
        rendre(par_renvoi(*args))
    else:
        sys.exit(__doc__)
    print('\n  Candidats, non sièges. Rouvrir l’article avant d’inscrire.')


if __name__ == '__main__':
    main(sys.argv)
