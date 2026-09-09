# -*- coding: utf-8 -*-
"""Table plate des articles ouverts par le texte déposé.

**Réécrit le 20260903** — le module était invoqué par le `Makefile`, déclaré aux
manquants de l'index, et absent du dépôt comme du coffre. Les deux tables qu'il
produit étaient, elles, versées : leur sortie à l'octet est donc la
spécification, et le réemploi se prouve au lieu de se croire.

Ce que le module rend, et rien d'autre : **une ligne par couple (texte,
article)** que la *disposition* du projet de loi modifie. Trois sorties, le même
relevé :

- le JSON, pour la jointure de `REF_norme` ;
- le relevé texte, pour la lecture de l'auteur ;
- **la table plate TSV, qui est ce qui se verse au coffre** — elle porte
  l'empreinte de sa pièce source, donc son rejeu se vérifie.

**Ouvert = modifié, jamais cité (A-229).** Une référence de statut autre que
`modifie` ne fait pas entrer d'adresse, et **aucune adresse ne se relève depuis
l'exposé des motifs** : le socle a déjà séparé les deux champs, ce module ne lit
que `references`.

**La grammaire d'adresse n'est pas dupliquée.** Le découpage d'un fragment en
article et subdivision est celui de `ref_norme.decouper_articles`, et il est
appelé, jamais réécrit — un second point de vérité ferait tomber la jointure
(A-94). Ce que le module ajoute est **le découpage d'une énumération** : le
socle relève « L. 314-2, L. 314-3 et L. 314-4 » comme un seul brut, quand ce
sont trois adresses qu'une mesure peut viser séparément. La virgule, le
point-virgule et « et » séparent ; **« à » ne sépare pas** — une fourchette
reste une adresse unique, marquée comme telle, et son dépliage vit à
`plages_articles.py`.

**La divergence de grammaire se déclare, elle ne se corrige pas.** Quand
`decouper_articles` ne rend pas le fragment entier — « 1383 C ter » se lit
« 1383 C » plus la subdivision « ter », « L. 2334-40 à L. 2334-42 » se lit sur
sa borne basse —, la colonne `article` garde le libellé de la pièce et la
colonne `article_selon_ref_norme` dit ce que la grammaire en fait. **La
jointure se fait sur le libellé exact** ; la colonne de divergence est là pour
qu'un écart se voie au lieu de se deviner.

Déterminisme : même socle, même script, même TSV, même SHA-256. L'ordre est
celui du libellé de texte puis du libellé d'article ; les articles du projet de
loi et les pages sont joints **dans leur ordre d'apparition dans la pièce**, ce
qui est un ordre du texte et non un tri.

Usage : python3 articles_ouverts_plf.py <socle.json> <sortie.json> \
                <releve.txt> <table.tsv>
"""
import collections
import json
import re
import sys

import ref_norme

# Une énumération d'adresses dans un même brut. « à » est délibérément absent :
# il borne une fourchette, il ne sépare pas deux adresses.
ENUMERATION = re.compile(r'\s*(?:,|;| et )\s*')

# Ce qui marque une fourchette dans le libellé de la pièce.
FOURCHETTE = ' à '

# Le socle laisse `texte` à `None` quand la disposition modifie une adresse sans
# nommer son texte de rattachement — « l'article L. 3212 est ainsi modifié »,
# sans code. Ce n'est pas `indéterminé`, qui est le mot de `vecteurs.py` pour un
# texte nommé que la grammaire ne sait pas rattacher : ici la pièce elle-même ne
# nomme rien, et la table le dit dans ces termes. La ligne sort quand même —
# c'est une adresse ouverte, dont le siège se tranche à la main.
SANS_TEXTE = 'aucun texte nommé'

COLONNES = ('texte', 'article', 'subdivision', 'fourchette',
            'article_selon_ref_norme', 'divergence', 'articles_{sigle}',
            'pages')


def _sigle(socle):
    """`PLF` ou `PLFSS`, relevé à la pièce déclarée et jamais supposé."""
    declaree = socle['_revision']['extraction']['piece_declaree']
    return declaree.split()[0]


def relever(socle):
    """Les couples ouverts, dans l'ordre d'apparition dans la pièce."""
    acc = collections.OrderedDict()
    for art in socle['articles']:
        for ref in art['references']:
            if ref['statut'] != 'modifie':
                continue
            texte = ref['texte'] or SANS_TEXTE
            for frag in ENUMERATION.split((ref['brut'] or '').strip()):
                frag = ref_norme.PREFIXES.sub('', frag.strip())
                if not frag:
                    continue
                decoupe = ref_norme.decouper_articles(frag)
                selon = decoupe[0][0] if decoupe else frag
                cle = (texte, frag, ref.get('subdivision') or '')
                e = acc.setdefault(cle, {
                    'texte': texte,
                    'article': frag,
                    'subdivision': ref.get('subdivision') or '',
                    'fourchette': FOURCHETTE in frag,
                    'article_selon_ref_norme': selon,
                    'divergence': selon != frag,
                    'articles': [],
                    'pages': [],
                })
                if art['numero'] not in e['articles']:
                    e['articles'].append(art['numero'])
                if ref['page'] not in e['pages']:
                    e['pages'].append(ref['page'])
    return acc


def _lignes_triees(acc):
    return sorted(acc.values(), key=lambda e: (e['texte'], e['article'],
                                               e['subdivision']))


def ecrire_tsv(dst, socle, lignes, sigle):
    piece = socle['_revision']['piece']
    declaree = socle['_revision']['extraction']['piece_declaree']
    textes = len({e['texte'] for e in lignes})
    fourchettes = sum(1 for e in lignes if e['fourchette'])
    divergences = sum(1 for e in lignes if e['divergence'])
    tete = [
        f'# ARTICLES OUVERTS PAR LE TEXTE DÉPOSÉ — {declaree}',
        '# Alimente la colonne `variante` de REF_norme : `article_ouvert` sur les',
        '# vecteurs dont le couple (texte, article) figure ici, `absolu` ailleurs.',
        '# Jointure sur le libellé exact, jamais au plus proche (A-94).',
        "# Ouvert = modifié par la disposition, jamais cité. L'exposé des motifs ne",
        "# compte pas : il est de l'indice, pas de la norme (A-229).",
        f'# pièce : {piece["nom"]} — sha256 {piece["sha256"]}',
        f'# {len(lignes)} adresses · {textes} textes · {fourchettes} '
        f'fourchettes · {divergences} divergences de grammaire avec ref_norme',
        '# colonnes : ' + '<TAB>'.join(
            c.format(sigle=sigle) for c in COLONNES),
        '#',
    ]
    with open(dst, 'w', encoding='utf-8', newline='') as f:
        for l in tete:
            f.write(l + '\n')
        for e in lignes:
            f.write('\t'.join((
                e['texte'],
                e['article'],
                e['subdivision'],
                '1' if e['fourchette'] else '0',
                e['article_selon_ref_norme'] if e['divergence'] else '',
                '1' if e['divergence'] else '0',
                ','.join(str(x) for x in e['articles']),
                ','.join(str(x) for x in e['pages']),
            )) + '\n')


def ecrire_releve(dst, socle, lignes, sigle):
    declaree = socle['_revision']['extraction']['piece_declaree']
    par_texte = collections.OrderedDict()
    for e in lignes:
        par_texte.setdefault(e['texte'], []).append(e)
    with open(dst, 'w', encoding='utf-8', newline='') as f:
        f.write(f'ARTICLES OUVERTS PAR LE TEXTE DÉPOSÉ — {declaree}\n')
        f.write(f'{len(lignes)} adresse(s) sur {len(par_texte)} texte(s). '
                f'Ouvert = modifié par la disposition, jamais cité.\n\n')
        for texte, entrees in par_texte.items():
            f.write(f'{texte} — {len(entrees)} adresse(s)\n')
            for e in entrees:
                marques = []
                if e['fourchette']:
                    marques.append('fourchette')
                if e['divergence']:
                    marques.append(
                        f'ref_norme lit « {e["article_selon_ref_norme"]} »')
                queue = f'  [{" ; ".join(marques)}]' if marques else ''
                arts = ','.join(str(x) for x in e['articles'])
                pages = ','.join(str(x) for x in e['pages'])
                f.write(f'    {e["article"]:<32} art. {sigle} {arts}'
                        f'  p. {pages}{queue}\n')
            f.write('\n')


def ecrire_json(dst, socle, lignes, sigle):
    piece = socle['_revision']['piece']
    sortie = {
        '_revision': {
            'role': 'articles ouverts par le texte déposé — '
                    + socle['_revision']['extraction']['piece_declaree'],
            'regle': 'Une entrée par couple (texte, article) que la '
                     'disposition modifie. Ouvert = modifié, jamais cité '
                     "(A-229). La jointure avec REF_norme se fait sur le "
                     'libellé exact, jamais au plus proche (A-94).',
            'piece': piece,
            'sigle': sigle,
            'adresses': len(lignes),
            'textes': len({e['texte'] for e in lignes}),
            'fourchettes': sum(1 for e in lignes if e['fourchette']),
            'divergences': sum(1 for e in lignes if e['divergence']),
        },
        'ouverts': [{
            'texte': e['texte'],
            'article': e['article'],
            'subdivision': e['subdivision'] or None,
            'fourchette': e['fourchette'],
            'article_selon_ref_norme': e['article_selon_ref_norme'],
            'divergence': e['divergence'],
            'articles_texte_depose': list(e['articles']),
            'pages': list(e['pages']),
        } for e in lignes],
    }
    with open(dst, 'w', encoding='utf-8', newline='') as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
        f.write('\n')


def main(src, dst_json, dst_txt, dst_tsv):
    socle = json.load(open(src, encoding='utf-8'))
    sigle = _sigle(socle)
    lignes = _lignes_triees(relever(socle))
    ecrire_json(dst_json, socle, lignes, sigle)
    ecrire_releve(dst_txt, socle, lignes, sigle)
    ecrire_tsv(dst_tsv, socle, lignes, sigle)
    print(f'{socle["_revision"]["extraction"]["piece_declaree"]} — '
          f'{len(lignes)} adresse(s), '
          f'{len({e["texte"] for e in lignes})} texte(s), '
          f'{sum(1 for e in lignes if e["fourchette"])} fourchette(s), '
          f'{sum(1 for e in lignes if e["divergence"])} divergence(s) de '
          f'grammaire')
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:5]))
