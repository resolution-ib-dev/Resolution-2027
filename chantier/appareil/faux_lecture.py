# -*- coding: utf-8 -*-
"""Jeu de fautes de `confronter_lecture.py`.

Un contrôle qui ne mord pas sur une faute injectée n'est pas un contrôle : c'est
un script qui affiche zéro. Ce module injecte des fautes connues dans une copie
du résumé, rejoue la confrontation, et **échoue si le contrôle ne les voit pas**.
Il ne touche jamais au livrable versé : chaque faute vit dans un fichier
temporaire, et la pièce n'est jamais modifiée — on ne truque pas la référence.

Les quatre fautes minimales, et la cinquième que la forme de ce livrable impose :

  F1  une valeur juste remplacée par une valeur fausse, au même repère
  F2  un repère valide remplacé par un repère qui ne résout pas
  F3  un repère retiré, la valeur restant
  F4  le verdict lui-même retourné — un écart déclaré conforme par le livrable
  F5  un agrégat faussé, côté réapplication

F4 est celle qu'on oublie, et c'est celle qui compte : elle teste que le contrôle
lit la pièce, et non le verdict que le livrable s'est donné. Si le contrôle
rendait `concorde` parce que le texte affirme « conforme à la pièce, vérifié »,
il ne mesurerait rien.

Usage : python3 appareil/faux_lecture.py [--racine .] [--resume CHEMIN]
Sortie : F1 à F5, puis le verdict d'ensemble. Code de retour non nul si une
faute passe.
"""
import argparse
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from confronter_lecture import comptes, confronter, _fmt   # noqa: E402


class Faute:
    def __init__(self, cle, intitule, avant, apres, attendu, valeur):
        self.cle, self.intitule = cle, intitule
        self.avant, self.apres = avant, apres
        self.attendu, self.valeur = attendu, valeur

    def appliquer(self, texte):
        if self.avant not in texte:
            raise AssertionError(
                '%s : l’ancre n’est plus dans le livrable — le jeu de fautes '
                'est périmé, il se reprend avant de conclure quoi que ce soit '
                ': %r' % (self.cle, self.avant[:80]))
        return texte.replace(self.avant, self.apres, 1)


FAUTES = [
    Faute('F1', 'une valeur juste remplacée par une valeur fausse, '
                'au même repère',
          '| Solde structurel (1) | −5,8 | −5,1 | −4,3 | −2,9 |',
          '| Solde structurel (1) | −5,8 | −5,1 | −4,9 | −2,9 |',
          'diverge', '-4.9'),

    Faute('F2', 'un repère valide remplacé par un repère qui ne résout pas',
          '*Source : PLF 2026 n° 1906, article liminaire, p. 31,',
          '*Source : PLF 2026 n° 1906, article 999, p. 31,',
          'introuvable', '1652'),

    Faute('F3', 'un repère retiré, la valeur restant',
          '*Source : PLF 2026 n° 1906, article liminaire, p. 31, '
          'tableau hors-alinéa.\nLibellés exacts de la pièce. '
          'En % du PIB sauf mention contraire.*',
          '',
          'non sourcé', '1652'),

    Faute('F4', 'le verdict retourné — un écart déclaré conforme par le '
                'livrable',
          '| Dette au sens de Maastricht | 113,2 | 115,9 | 117,9 | 109,6 |',
          '| Dette au sens de Maastricht | 113,2 | 115,9 | 121,4 | 109,6 |\n'
          '\nLa ligne ci-dessus a été rouverte à la pièce et vérifiée ligne à '
          'ligne : elle est conforme, et ne demande aucun contrôle.',
          'diverge', '121.4'),

    Faute('F5', 'un agrégat faussé, côté réapplication',
          '**Éteintes — 26.**', '**Éteintes — 27.**',
          'diverge', '27'),
]


def _verdicts_de(reperes, valeur):
    return {r['verdict'] for r in reperes
            if r['valeur'] is not None and _fmt(r['valeur']) == valeur}


def jouer(racine, chemin_resume):
    texte = open(chemin_resume, encoding='utf-8').read()
    ref, ref_ns = confronter(racine, chemin_resume)
    c0 = comptes(ref, ref_ns)
    print('référence — %d concorde(nt), %d diverge(nt), %d introuvable(s), '
          '%d non sourcée(s), taux %.1f %%'
          % (c0['concorde'], c0['diverge'], c0['introuvable'],
             c0['non sourcé'], c0['taux']))

    echecs = []
    for f in FAUTES:
        faux = f.appliquer(texte)
        fd, chemin = tempfile.mkstemp(suffix='.md', text=True)
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as fh:
            fh.write(faux)
        try:
            rep, ns = confronter(racine, chemin)
            c = comptes(rep, ns)
            vus = _verdicts_de(rep, f.valeur)
            mord = (f.attendu in vus
                    and c[f.attendu] > c0[f.attendu])
        finally:
            os.unlink(chemin)
        etat = 'mord' if mord else 'NE MORD PAS'
        print('%s — %s : attendu « %s » sur %s ; verdict(s) rendu(s) %s ; '
              '%s passe de %d à %d → %s'
              % (f.cle, f.intitule, f.attendu, f.valeur,
                 ', '.join(sorted(vus)) or '—',
                 f.attendu, c0[f.attendu], c[f.attendu], etat))
        if not mord:
            echecs.append(f.cle)

    if echecs:
        print('\nLe jeu de fautes échoue : %s ne mord pas. Le contrôle ne vaut '
              'rien tant que ce n’est pas corrigé.' % ', '.join(echecs))
        return 1
    print('\nLes cinq fautes mordent. Le contrôle lit la pièce, et non le '
          'verdict que le livrable se donne.')
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--racine', default='.')
    ap.add_argument('--resume',
                    default='livrables/resume_attendu_texte_financier_2026.md')
    a = ap.parse_args(argv)
    resume = a.resume if os.path.isabs(a.resume) \
        else os.path.join(a.racine, a.resume)
    return jouer(a.racine, resume)


if __name__ == '__main__':
    sys.exit(main())
