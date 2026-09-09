# -*- coding: utf-8 -*-
"""La couche technique : où elle vit, et ce qui lui est dû.

**Ce module ne plie plus rien.** Jusqu'au 20260909, la couche technique — tout
`appareil/`, les trois référentiels JSON, le `Makefile` et le `.gitignore` — se
repliait dans une archive unique du coffre, `technique/coffre.txt`, que l'auteur
n'ouvrait jamais et que Claude dépliait en ouverture de session. Le motif tient
toujours : le coffre est aussi la vue de l'auteur, et y verser quatre-vingts
fichiers de Python et de JSON lui infligeait une liste qu'il ne peut pas lire.

Le 20260909, cette archive a été versée au dépôt et supprimée du coffre (A-395),
après preuve à l'octet 80 sur 80. **Le dépôt rend le même service et deux de
plus** : la restauration est une copie d'octets par `git clone`, sans passer par
un format d'archive maison, et l'appareil ne pèse plus rien à la jauge du coffre.

`plier` a donc été retiré. Le garder aurait été pire qu'inutile : un fil l'aurait
joué, aurait vu une archive apparaître dans `coffre/`, et aurait cru avoir versé
quelque chose. **Un outil qui produit une pièce que personne ne verse est un
piège**, et A-364 nomme déjà la maladie — un dérivé versé que nul ne pense à
reverser.

Deux modes restent, et un troisième naît.

  deplier  relit une archive au vieux format, si une session en récupère une.
           C'est le seul lecteur de ce format ; le retirer rendrait illisible
           une archive qui resurgirait d'un transcript ou d'une sauvegarde.
  dette    dit ce qui est dû au dépôt : les pièces de l'appareil qui divergent
           du clone, celles qui n'y sont pas, et celles qui vivent encore au
           coffre comme documents. **L'écriture au dépôt est fermée depuis
           Cowork** (A-393) : ce mode ne pousse rien, il déclare.

Usage : python3 coffre.py deplier <archive> <racine>
        python3 coffre.py dette ../methode/index.json .. ../droit
"""
import hashlib
import json
import os
import sys

DEBUT = '<' * 10 + ' fichier '
FIN = '>' * 10 + ' fin '


def deplier(chemin_archive, racine):
    texte = open(chemin_archive, encoding='utf-8').read()
    ecrits = []
    i = 0
    while True:
        d = texte.find(DEBUT, i)
        if d < 0:
            break
        fin_ligne = texte.index('\n', d)
        chemin = texte[d + len(DEBUT):fin_ligne].strip()
        marque_fin = f'\n{FIN}{chemin}\n'
        f = texte.index(marque_fin, fin_ligne)
        contenu = texte[fin_ligne + 1:f]
        cible = os.path.join(racine, chemin)
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        open(cible, 'w', encoding='utf-8').write(contenu)
        ecrits.append(chemin)
        i = f + len(marque_fin)
    print(f'{len(ecrits)} fichier(s) dépliés depuis {chemin_archive}')
    for c in ecrits:
        print(f'    {c}')
    return 0 if ecrits else 1


def _sha(chemin):
    if not os.path.isfile(chemin):
        return None
    return hashlib.sha256(open(chemin, 'rb').read()).hexdigest()


def dette(chemin_index, racine, clone):
    """Ce qui est dû au dépôt, comparé octet par octet au clone.

    Le clone est la référence, jamais le dépôt courant : c'est lui que la
    session suivante recevra. Une pièce qui diverge est une pièce que le fil a
    corrigée sans pouvoir la pousser — elle se déclare, et elle se perd si
    personne ne la porte.
    """
    index = json.load(open(chemin_index, encoding='utf-8'))
    depot = index['depot']
    sous = depot['sous_racine']

    divergents, absents, identiques = [], [], 0
    for a in index['artefacts']:
        if a.get('voie') != 'depot':
            continue
        ici = _sha(os.path.join(racine, a['chemin']))
        la = _sha(os.path.join(clone, sous, a['chemin']))
        if ici is None:
            continue  # ce fil ne l'a pas au dépôt courant : rien à dire
        if la is None:
            absents.append(a['chemin'])
        elif ici != la:
            divergents.append((a['chemin'],
                               os.path.getsize(os.path.join(racine, a['chemin'])),
                               ici[:16], la[:16]))
        else:
            identiques += 1

    documents = depot.get('au_coffre_comme_document', [])

    print(f'{depot["nom"]}, branche {depot["branche"]}, sous-racine {sous}/')
    print(f'{identiques} pièce(s) identique(s) au clone, '
          f'{len(divergents)} divergente(s), {len(absents)} absente(s) du clone, '
          f'{len(documents)} encore au coffre comme document\n')

    print(f'D1 — {len(divergents)} pièce(s) modifiée(s) ici et non poussée(s)')
    for c, o, ici, la in divergents:
        print(f'    {c} — {o} o, ici {ici}, au clone {la}')

    print(f'\nD2 — {len(absents)} pièce(s) que le clone ne porte pas')
    for c in absents:
        print(f'    {c}')

    print(f'\nD3 — {len(documents)} pièce(s) de l\'appareil au coffre comme '
          f'document, dues au dépôt')
    for c in documents:
        print(f'    {c}')

    du = len(divergents) + len(absents) + len(documents)
    if du:
        print(f'\n{du} pièce(s) due(s) au dépôt. {depot["ecriture"]}')
        print(f'    clone de référence : {depot["clone"]}')
    else:
        print('\nRien n\'est dû au dépôt : le clone porte l\'appareil à l\'octet.')
    # Une dette n'est pas un échec de contrôle : elle est déclarative, et
    # `make coffre` ne doit pas s'arrêter dessus. Le code de retour reste nul.
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    mode = sys.argv[1]
    if mode == 'deplier':
        sys.exit(deplier(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '.'))
    if mode == 'dette':
        sys.exit(dette(sys.argv[2],
                       sys.argv[3] if len(sys.argv) > 3 else '.',
                       sys.argv[4] if len(sys.argv) > 4 else '../droit'))
    if mode == 'plier':
        print(__doc__)
        print("\n`plier` est retiré depuis le 20260909 (A-395, A-396) : "
              "l'archive technique\nn'est plus au coffre, elle est au dépôt. "
              "Il n'y a rien à replier.")
        sys.exit(2)
    print(__doc__)
    sys.exit(2)
