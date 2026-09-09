# -*- coding: utf-8 -*-
"""Contrôle de lexique — les mots que le corpus ne dit pas, sauf pour les nier.

A-53 posait le 20260824 que la liste des termes n'est pas une préférence de
style mais une règle vérifiable mécaniquement, et qu'elle serait portée à
`controle_sortie.py`. **Elle ne l'a jamais été** : relevé le 20260906 en
cherchant où inscrire la règle du jour. Une règle tenue à l'œil se perd, et
celle-ci s'est perdue treize jours.

Elle a son module. Deux familles de termes, et elles ne se traitent pas pareil.

**Les proscrits simples** ont un substitut, et l'emploi du mauvais mot est une
faute de registre — « baisse d'impôt » pour restitution, « prélèvements
obligatoires » pour ce qu'on vous prend, « fonctionnaires » pour bureaucratie,
« administration » pour intermédiaires, « les actifs » pour ceux qui produisent.

**Les proscrits de doctrine** n'ont pas de substitut : ce sont des mots dont
l'emploi affirmatif contredit ce que le corpus démontre. **« Gratuit » est le
premier d'entre eux** — arbitré par l'auteur le 20260906 : rien n'est gratuit,
tout est payé par quelqu'un, et c'est la base de la doctrine. Le mot ne
s'emploie que **pour être dénoncé**.

**La dénonciation se reconnaît, elle ne se devine pas.** Un marqueur de négation
ou de fausseté dans la même phrase — « fausse gratuité », « gratuité apparente »,
« prétendument gratuit », « rien n'est gratuit », « la gratuité n'existe pas » —
et l'emploi est conforme. Sans marqueur, il sort. La fenêtre est la phrase, pas
le paragraphe : un démenti trois phrases plus loin ne rattrape pas une affirmation.

**Ce module lit des livrables, pas de la méthode.** Le registre, le journal et
les procédures parlent *du* mot ; ils sont exclus par leur chemin, sans quoi
cette page même sortirait en anomalie.

Usage : python3 controle_lexique.py <fichier|dossier> [...]
"""
import os
import json
import re
import sys

# Marque d'un proscrit de doctrine : pas de substitut, l'emploi affirmatif est
# la faute, et le mot ne se dit que pour être nié.
DOCTRINE = object()

# terme proscrit → ce qu'on dit à la place, ou DOCTRINE.
PROSCRITS = {
    r'gratuit(?:e|s|es|é|és|ément)?': DOCTRINE,
    r'baisses? d[\'’]imp[ôo]ts?': 'restitution',
    r'pr[ée]l[èe]vements obligatoires': 'ce qu’on vous prend',
    r'fonctionnaires?': 'bureaucratie',
    r'les actifs': 'ceux qui produisent',
    r'il est [ée]vident que': 'on a vérifié',
    r'il faut ': 'ce que la mesure fait',
}

# Ce qui, dans la même phrase, retourne le terme et le rend conforme.
DENONCIATION = re.compile(
    r'fauss?e?s?|apparen(?:t|te|ts|tes|ce)|pr[ée]tendu|soi-disant|'
    r'illusion|mythe|mirage|en trompe|'
    r'n[\'’]existe pas|n[\'’]est pas|ne sont pas|rien n[\'’]est|jamais|'
    r'payé par|quelqu[\'’]un paie|coûte', re.I)

# Une exemption nommée, et elle vit ici plutôt que dans le document contrôlé
# (A-303) : « à titre gratuit » est une locution du code civil qui qualifie une
# transmission, non un emploi affirmatif de la gratuité. Le contrôle la voyait
# comme une faute dans la définition d'une catégorie de personnes.
EXEMPTIONS = (re.compile(r'à titre gratuit', re.I),)

# La méthode parle des mots ; elle ne les emploie pas. Exclue par le chemin.
HORS_CHAMP = ('methode/', 'appareil/', 'reference/', 'sources/', 'archive/',
              'referentiels/', 'eval/', 'CLAUDE.md', 'DEMARRAGE.md')

EXTENSIONS = ('.html', '.md', '.txt')

PHRASE = re.compile(r'[^.!?…]*[.!?…]|[^.!?…]+')
BALISE = re.compile(r'<[^>]+>')


def phrases(texte):
    nu = BALISE.sub(' ', texte)
    for m in PHRASE.finditer(nu):
        s = m.group(0).strip()
        if s:
            yield s


def controler_texte(texte):
    """Rend la liste des (terme, phrase) fautifs."""
    fautes = []
    for ph in phrases(texte):
        for motif, substitut in PROSCRITS.items():
            m = re.search(r'\b' + motif + r'\b', ph, re.I)
            if not m:
                continue
            if any(e.search(ph) for e in EXEMPTIONS):
                continue
            if DENONCIATION.search(ph):
                continue
            fautes.append((m.group(0), substitut, ph[:160]))
    return fautes


def fichiers(cible):
    if os.path.isfile(cible):
        yield cible
        return
    for base, dossiers, noms in os.walk(cible):
        dossiers[:] = [d for d in dossiers if not d.startswith('.')]
        for n in noms:
            if n.endswith(EXTENSIONS):
                yield os.path.join(base, n)


def hors_champ(chemin):
    p = chemin.replace(os.sep, '/')
    return any(x in p for x in HORS_CHAMP)


# Le lexique est une règle de **livrable diffusable**, et c'est ce que l'index
# déclare : `consomme_par` porte « tout livrable diffusable ». Balayer
# `livrables/` en entier y faisait entrer les vues internes — l'arbre du
# référentiel, l'interface de travail, l'inventaire, les relevés de notes —,
# qui portent la nomenclature interne et du verbatim du manuscrit, et qui ne se
# réécrivent ni l'un ni l'autre. Le périmètre se lit donc à la carte : output
# seul, c'est-à-dire les familles graphique, rédactionnel et juridique.
DIFFUSABLES = ('graphique', 'rédactionnel', 'juridique')


def perimetre(chemin_index, racine='.'):
    """Les chemins que l'index range dans une famille diffusable, ou None."""
    try:
        index = json.load(open(chemin_index, encoding='utf-8'))
    except (OSError, ValueError):
        return None
    garde = set()
    for a in index['artefacts']:
        if a.get('famille') in DIFFUSABLES and a.get('chemin'):
            garde.add(a['chemin'])
            # Le site se déclare par sa seule entrée et vaut pour son dossier.
            if a['chemin'].endswith('/index.html'):
                garde.add(os.path.dirname(a['chemin']) + '/')
    return garde


def diffusable(chemin, garde):
    if garde is None:
        return True
    p = chemin.replace(os.sep, '/')
    return p in garde or any(p.startswith(g) for g in garde if g.endswith('/'))


def main(argv):
    cibles = argv[1:] or ['livrables', 'site']
    garde = perimetre('methode/index.json')
    total, fautifs = 0, 0
    for cible in cibles:
        if not os.path.exists(cible):
            continue
        for f in sorted(fichiers(cible)):
            if hors_champ(f) or not diffusable(f, garde):
                continue
            total += 1
            try:
                texte = open(f, encoding='utf-8').read()
            except (OSError, UnicodeDecodeError):
                continue
            fautes = controler_texte(texte)
            if fautes:
                fautifs += 1
                print(f'  {f}')
                for terme, substitut, ph in fautes:
                    dit = (' — proscrit de doctrine, sauf pour le nier'
                           if substitut is DOCTRINE
                           else f' — dire « {substitut} »')
                    print(f'      L1 {terme!r}{dit}')
                    print(f'         {ph}')
    print(f'L1 — {total} livrable(s) lu(s), {fautifs} en anomalie de lexique')
    return 1 if fautifs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
