# -*- coding: utf-8 -*-
"""Pliage d'un paquet diffusable en un document unique, et rien d'autre.

**Pourquoi ce module existe, et pourquoi il ne rouvre pas `coffre.py plier`.**
Le 20260909, l'archive technique a quitté le coffre pour le dépôt et `plier` a
été retiré : un outil qui produit une pièce que personne ne verse est un piège.
Le cas traité ici est l'inverse — la pièce pliée **est** ce qui se verse, et le
dépôt ne porte que sa forme dépliée, qui est un dérivé.

Le besoin : un paquet diffusable est fait de dizaines de petits fichiers. Les
verser un par un inflige au coffre une liste que personne ne lit, et à la table
curée de l'index autant de lignes. Les concaténer sans rien d'autre les rendrait
irrécupérables : le compte de cibles d'un contrôle de projection cesserait de se
rejouer, et un contrôle qu'on ne peut plus rejouer ne contrôle plus rien.

Le format est **exactement celui que `coffre.py deplier` lit déjà**. Aucun
lecteur nouveau n'entre au corpus : ce module n'écrit que ce que l'autre sait
relire, et le dépliage reste l'affaire d'un seul module.

La preuve est dans le module : `plier` replie, déplie dans un répertoire
temporaire, et compare **octet par octet** chaque fichier à son original. Un
seul écart et rien n'est écrit — un paquet plié qui ne redonne pas ses fichiers
est pire qu'un paquet non plié, puisqu'il en a l'air.

Usage : python3 plier_paquet.py <racine_du_paquet> <document_plie>
        python3 coffre.py deplier <document_plie> <racine>
"""
import hashlib
import os
import shutil
import sys
import tempfile

DEBUT = '<' * 10 + ' fichier '
FIN = '>' * 10 + ' fin '


def _fichiers(racine):
    """Tous les fichiers du paquet, chemins relatifs, dans un ordre stable."""
    releve = []
    for dossier, _, noms in os.walk(racine):
        for nom in noms:
            chemin = os.path.join(dossier, nom)
            releve.append(os.path.relpath(chemin, racine))
    return sorted(releve)


def _sha(chemin):
    return hashlib.sha256(open(chemin, 'rb').read()).hexdigest()


def plier(racine, cible):
    chemins = _fichiers(racine)
    if not chemins:
        print(f'aucun fichier sous {racine}')
        return 1

    morceaux = []
    for c in chemins:
        contenu = open(os.path.join(racine, c), encoding='utf-8').read()
        if DEBUT in contenu or FIN in contenu:
            print(f'{c} porte un délimiteur du format : pliage refusé')
            return 1
        if not contenu.endswith('\n'):
            # `deplier` rend le texte compris entre le saut de ligne de l'en-tête
            # et celui qui précède la marque de fin : un fichier sans saut de
            # ligne final en gagnerait un au dépliage. On refuse plutôt que de
            # rendre un dépliage qui n'est plus une copie d'octets.
            print(f'{c} ne finit pas par un saut de ligne : pliage refusé')
            return 1
        # `deplier` prend le texte jusqu'au saut de ligne qui précède la marque
        # de fin, et ce saut-là est à la marque, non au fichier : d'où le saut
        # supplémentaire, sans lequel chaque fichier perdrait le sien.
        morceaux.append(f'{DEBUT}{c}\n{contenu}\n{FIN}{c}\n')
    texte = ''.join(morceaux)

    # La preuve avant l'écriture, jamais après.
    bac = tempfile.mkdtemp(prefix='plier_paquet_')
    try:
        provisoire = os.path.join(bac, 'plie.md')
        open(provisoire, 'w', encoding='utf-8').write(texte)
        sortie = os.path.join(bac, 'deplie')
        os.makedirs(sortie)
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import coffre
        depuis = os.dup(1)
        muet = os.open(os.devnull, os.O_WRONLY)
        os.dup2(muet, 1)
        try:
            coffre.deplier(provisoire, sortie)
        finally:
            os.dup2(depuis, 1)
            os.close(muet)
            os.close(depuis)
        divergents = [c for c in chemins
                      if not os.path.isfile(os.path.join(sortie, c))
                      or _sha(os.path.join(sortie, c))
                      != _sha(os.path.join(racine, c))]
        rendus = _fichiers(sortie)
    finally:
        shutil.rmtree(bac, ignore_errors=True)

    if divergents or rendus != chemins:
        print(f'{len(divergents)} fichier(s) divergent(s) au dépliage, '
              f'{len(rendus)} rendu(s) pour {len(chemins)} attendu(s) — '
              f'rien n\'est écrit')
        for c in divergents[:20]:
            print(f'    {c}')
        return 1

    os.makedirs(os.path.dirname(os.path.abspath(cible)), exist_ok=True)
    open(cible, 'w', encoding='utf-8').write(texte)
    print(f'{len(chemins)} fichier(s) pliés dans {cible} — '
          f'{len(texte.encode("utf-8"))} o')
    print(f'dépliage prouvé à l\'octet, {len(chemins)} sur {len(chemins)}')
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(plier(sys.argv[1], sys.argv[2]))
