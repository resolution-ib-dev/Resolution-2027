# -*- coding: utf-8 -*-
"""La part irréproductible du socle du texte déposé — ce qui se verse au coffre.

**Écrit le 20260903, en application d'A-342 et de sa clause de repli.** Le socle
du texte déposé se régénère depuis une pièce jointe, donc depuis l'extérieur du
coffre : sa chaîne de régénération est rompue, et il se verse. Mesuré, il ne
tient pas : le socle de la loi de finances pèse **494 461 jetons** à la jauge du
projet, pour une marge de **310 550**. La clause de repli d'A-342 s'applique
alors, et elle est explicite — *c'est sa part irréproductible qui se verse, et
jamais la part qu'une autre source sait rendre.*

Ce module découpe cette part. Il ne relève rien de la pièce : il lit le socle,
en retire deux champs, et rend un JSON compact. **Aucun octet de rédaction n'est
retouché.**

**Ce qui se verse, et pourquoi.**

- la structure de l'article — numéro, partie, titre de division, intitulés,
  pages de début et de fin ;
- **les alinéas, un par entrée, avec leur numéro, leur page et leur texte
  exact** — c'est la forme qu'une disposition modificative adresse, et celle que
  la colonne A du trois colonnes consomme ;
- **le hors-alinéa** — états législatifs, plafonds d'emplois, tableau
  d'équilibre. Rien d'autre ne le porte ;
- **les adresses relevées à la disposition**, avec leur statut et leur alinéa ;
- **l'empreinte de la pièce et celle du socle**, pour qu'un rejeu se vérifie au
  lieu de se croire.

**Ce qui ne se verse pas, et c'est un choix dit et non subi.**

- `redaction.lignes` — le brut de mise en page de `pdftotext -layout`, dont
  `alineas` est le reflux déterministe de l'extracteur. Les deux champs portent
  **le même verbatim dans deux rendus** ; en verser les deux coûte 602 852
  octets pour aucune information de plus. On garde celui que la chaîne consomme.
  *Ce que la coupe coûte* : la mise en page brute ne se relit plus au coffre. Le
  tableau, qui en dépend, est gardé à part par `hors_alinea`.
- `expose_des_motifs` — de l'indice, pas de la norme (A-229). *Ce que la coupe
  coûte, et il faut le dire* : le quatrième relevé de la lecture en creux —
  montants annoncés à l'exposé sans contrepartie à la rédaction — ne se rejoue
  pas depuis le coffre seul. Il se rejoue depuis la pièce jointe, comme
  aujourd'hui.

**Déterminisme.** Même socle, même script, même JSON, même SHA-256. Sortie
compacte, clés triées à leur ordre de déclaration, `ensure_ascii` faux.

Usage : python3 redaction_deposee.py <socle.json> <sortie.json>
"""
import hashlib
import json
import sys

# Les deux champs retirés, et le motif de leur retrait. La liste est fermée :
# une coupe nouvelle est un arbitrage, pas une optimisation.
RETIRES = {
    'redaction.lignes': 'brut de mise en page ; `alineas` en est le reflux '
                        'déterministe et porte le même verbatim',
    'expose_des_motifs': "de l'indice, pas de la norme (A-229)",
}


def reduire(socle):
    rev = socle['_revision']
    articles = []
    for art in socle['articles']:
        red = art['redaction']
        articles.append({
            'numero': art['numero'],
            'titre': art['titre'],
            'partie': art['partie'],
            'partie_intitule': art['partie_intitule'],
            'titre_division': art['titre_division'],
            'titre_division_intitule': art['titre_division_intitule'],
            'divisions': art['divisions'],
            'page': art['page'],
            'page_fin': art['page_fin'],
            'nb_alineas': red['nb_alineas'],
            'porte_tableau': red['porte_tableau'],
            'alineas': red['alineas'],
            'hors_alinea': red['hors_alinea'],
            'references': art['references'],
        })
    return {
        '_revision': {
            'role': 'rédaction exacte du texte déposé — part irréproductible '
                    'du socle, ' + rev['extraction']['piece_declaree'],
            'regle': "Verse ce que nulle autre source ne rend : la rédaction "
                     "exacte des articles, alinéa par alinéa, le hors-alinéa, "
                     "et les adresses relevées à la disposition. Le socle "
                     "complet se régénère depuis la pièce jointe ; il ne tient "
                     "pas à la jauge, et A-342 fait alors verser sa seule part "
                     "irréproductible.",
            'piece': rev['piece'],
            'extraction': rev['extraction'],
            'socle_sha256': socle_sha(socle),
            'champs_retires': RETIRES,
            'articles': len(articles),
            'alineas': sum(a['nb_alineas'] for a in articles),
            'adresses': sum(len(a['references']) for a in articles),
        },
        'articles': articles,
    }


def socle_sha(socle):
    """L'empreinte du socle dont ce document est la coupe.

    Relevée sur la sérialisation du socle telle que `socle_plf_texte.py`
    l'écrit — indentation 1, `ensure_ascii` faux —, et non sur le fichier, pour
    que le renvoi tienne même si l'appel ne dispose que de l'objet.
    """
    texte = json.dumps(socle, ensure_ascii=False, indent=1) + '\n'
    return hashlib.sha256(texte.encode('utf-8')).hexdigest()


def main(src, dst):
    socle = json.load(open(src, encoding='utf-8'))
    sortie = reduire(socle)
    with open(dst, 'w', encoding='utf-8', newline='') as f:
        json.dump(sortie, f, ensure_ascii=False, separators=(',', ':'))
        f.write('\n')
    rev = sortie['_revision']
    with open(dst, 'rb') as f:
        octets = f.read()
    print(f'{rev["extraction"]["piece_declaree"]} — {rev["articles"]} '
          f'article(s), {rev["alineas"]} alinéa(s), {rev["adresses"]} '
          f'adresse(s)')
    print(f'  {len(octets)} o — sha256 '
          f'{hashlib.sha256(octets).hexdigest()}')
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:3]))
