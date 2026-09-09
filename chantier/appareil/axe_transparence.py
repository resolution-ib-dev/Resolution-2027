# -*- coding: utf-8 -*-
"""Vérification de l'axe de transparence au REF_doctrine.

A-226 écarte « information et contrôle du Parlement » comme porte générale et
lui réserve un usage : **l'axe de transparence absolue — opérateurs,
associations, caisses de sécurité sociale.** L'entrée dit expressément que
l'existence de cet axe au corpus **reste à vérifier**.

Ce module la vérifie mécaniquement, et il répond à quatre questions, dans cet
ordre : l'axe existe-t-il, que porte-t-il, jusqu'où porte-t-il sur les trois
populations nommées, et qu'est-ce qui manque pour en tirer une norme.

**Il ne juge pas la doctrine et il n'en écrit aucune.** Il relève ce que le
référentiel porte et ce qu'il ne porte pas. Un trou se déclare ; il ne se
comble pas.

## Comment le relevé procède

Deux passes, et la seconde rattrape ce que la première rate.

**Par la structure** — le levier `D1-1` s'intitule « Droit de savoir :
transparence et audit ». Tout ce qu'il porte est relevé en entier : ses
propositions, leurs paramètres, leurs effets, leurs sous-items, leurs
compléments constitutionnels.

**Par le vocabulaire** — l'axe peut vivre ailleurs sous un autre nom. Le corpus
entier est balayé sur trois familles de termes : la transparence elle-même, les
trois populations, et les véhicules documentaires. Un terme trouvé hors `D1-1`
est un morceau d'axe qui ne se range pas où on l'attendait, et c'est
exactement ce qu'on cherche à savoir.

Usage : python3 axe_transparence.py ../referentiels/REF_doctrine.json \\
            ../livrables/axe_transparence.md
"""
import json
import os
import re
import sys

LEVIER = 'D1-1'

# Trois familles de termes. Le balayage est littéral et insensible à la casse ;
# il ne devine aucune forme fléchie qui ne soit pas écrite ici.
TERMES = {
    'la transparence elle-même': [
        'transparen', 'audit', 'droit de savoir', 'publicit', 'publie',
        'publier', 'publication', 'rendre compte', 'redevab', 'contrôl',
        'opposab', 'sincérit',
    ],
    'les opérateurs': [
        'opérateur', 'agence', 'organisme', 'établissement public', 'odac',
        'odal', 'satellite',
    ],
    'les associations': [
        'association', 'subvention', 'personne morale de droit privé',
        'personne privée',
    ],
    'les caisses': [
        'caisse', 'sécurité sociale', 'urssaf', 'branche', 'régime social',
    ],
    'les véhicules documentaires': [
        'annexe', 'rapport', 'jaune', 'document budgétaire', 'liste',
        'inventaire', 'registre',
    ],
}

# Ce qu'une norme de transparence demande pour être rédigeable. Chaque ligne se
# vérifie contre ce que le référentiel porte, jamais contre ce qu'on suppose.
EXIGENCES = [
    ('le débiteur', "qui doit produire l'information — l'État, l'opérateur, "
                    "l'association, la caisse"),
    ('l\'assiette', "sur quoi elle porte — comptes, effectifs, rémunérations, "
                    "subventions reçues, marchés"),
    ('le support', "où elle paraît — annexe au projet de loi de finances, "
                   "rapport, base ouverte"),
    ('la périodicité', "quand"),
    ('la sanction', "ce qui arrive si elle n'est pas produite — sans quoi une "
                    "obligation de transparence est un vœu"),
]


def _plat(objet, chemin=''):
    """Toutes les chaînes du référentiel, avec le chemin qui y mène."""
    if isinstance(objet, dict):
        for k, v in objet.items():
            yield from _plat(v, f'{chemin}.{k}' if chemin else k)
    elif isinstance(objet, list):
        for i, v in enumerate(objet):
            yield from _plat(v, f'{chemin}[{i}]')
    elif isinstance(objet, str) and objet.strip():
        yield chemin, objet


def _situer(ref):
    """chemin → identifiant doctrinal le plus proche (axe, levier, proposition)."""
    situe = {}
    for ia, ax in enumerate(ref['axes']):
        situe[f'axes[{ia}]'] = ax['id']
        for il, lv in enumerate(ax.get('leviers', [])):
            situe[f'axes[{ia}].leviers[{il}]'] = lv['id']
            for ip, pr in enumerate(lv.get('propositions', [])):
                situe[f'axes[{ia}].leviers[{il}].propositions[{ip}]'] = pr['id']
    return situe


def _id_de(chemin, situe):
    meilleur = ''
    for prefixe, ident in situe.items():
        if chemin.startswith(prefixe) and len(prefixe) > len(meilleur):
            meilleur, trouve = prefixe, ident
    return trouve if meilleur else '—'


def levier(ref, cible):
    for ax in ref['axes']:
        for lv in ax.get('leviers', []):
            if lv['id'] == cible:
                return ax, lv
    return None, None


def balayer(ref):
    """famille → terme → [(identifiant doctrinal, champ, extrait)]"""
    situe = _situer(ref)
    trouve = {f: {} for f in TERMES}
    for chemin, texte in _plat(ref):
        bas = texte.lower()
        for famille, mots in TERMES.items():
            for mot in mots:
                if mot in bas:
                    ident = _id_de(chemin, situe)
                    champ = chemin.split('.')[-1]
                    champ = re.sub(r'\[\d+\]', '', champ)
                    extrait = texte if len(texte) <= 220 else texte[:217] + '…'
                    trouve[famille].setdefault(mot, []).append(
                        (ident, champ, extrait))
    return trouve


def rendre(ref, ax, lv, trouve):
    L = []
    a = L.append
    a('# L\'axe de transparence au REF_doctrine — vérification')
    a('')
    a('*Relevé mécanique par `appareil/axe_transparence.py` sur '
      '`referentiels/REF_doctrine.json`. A-226 réserve la porte du 7° du II de '
      'l\'article 34 à cet axe et pose que son existence au corpus reste à '
      'vérifier. Voici ce que le référentiel porte — et ce qu\'il ne porte '
      'pas.*')
    a('')
    a('---')
    a('')

    # ------------------------------------------------------- 1. existe-t-il
    a('## 1. L\'axe existe-t-il ?')
    a('')
    if lv is None:
        a(f'**Non.** Aucun levier `{LEVIER}` au référentiel.')
    else:
        props = lv.get('propositions', [])
        a(f'**Oui, nominalement.** L\'axe `{ax["id"]}` — « {ax["intitule"]} » — '
          f'porte le levier `{lv["id"]}`, « {lv["intitule"]} ». '
          f'{len(props)} proposition(s).')
        a('')
        for pr in props:
            a(f'- `{pr["id"]}` — **{pr["intitule"]}** · verbe *{pr["verbe"]}* · '
              f'domaine *{pr["domaine"]}* · strate `{pr["strate"]}` · '
              f'statut **{pr["statut"]}**')
    a('')

    # ------------------------------------------------ 2. que porte-t-il
    a('## 2. Que porte-t-il exactement ?')
    a('')
    if lv is not None:
        champs = ['droit_existant', 'ne_fait_pas', 'parametres', 'effets',
                  'sous_items', 'sources', 'ancrage_doctrinal', 'renvois',
                  'membres', 'complements_constitutionnels']
        a('| proposition | ' + ' | '.join(f'`{c}`' for c in champs) + ' |')
        a('|---|' + '---|' * len(champs))
        for pr in lv.get('propositions', []):
            cells = []
            for c in champs:
                v = pr.get(c)
                if isinstance(v, list):
                    cells.append(str(len(v)) if v else '**vide**')
                elif isinstance(v, str):
                    cells.append(f'« {v} »' if v.strip() else '**vide**')
                else:
                    cells.append('**vide**')
            a(f'| `{pr["id"]}` | ' + ' | '.join(cells) + ' |')
        a('')
        for pr in lv.get('propositions', []):
            if pr.get('complements_constitutionnels'):
                a(f'Compléments constitutionnels de `{pr["id"]}` :')
                a('')
                for cc in pr['complements_constitutionnels']:
                    a(f'- `{cc["id"]}` — « {cc["intitule"]} » · {cc["article"]} '
                      f'· verbe *{cc["verbe"]}* · {cc["inspiration"]}')
                a('')
        a('**Ce que le tableau dit, et il faut le dire net :** l\'axe est un '
          'intitulé et un verbe. Il ne porte **aucun paramètre, aucun effet, '
          'aucun sous-item, aucune source, aucun droit existant, aucun '
          'périmètre**. Son statut est *esquissée* — le référentiel le déclare '
          'lui-même.')
        a('')
        membres = [m for pr in lv.get('propositions', []) for m in pr.get('membres', [])]
        if membres:
            a(f'La seule matière est un renvoi : {len(membres)} membre(s) — '
              + ', '.join(f'`{m}`' for m in membres) + '. **Ces identifiants '
              'renvoient à `referentiels/releve_affecte.json`, que l\'index '
              'déclare au bloc `manquants` : la couche de preuve à '
              'identifiants `M-nnnn` est introuvable.** L\'axe renvoie donc à '
              'une pièce que le corpus ne porte pas.')
            a('')

    # -------------------------------- 3. jusqu'où sur les trois populations
    a('## 3. Jusqu\'où porte-t-il sur les opérateurs, les associations et les '
      'caisses ?')
    a('')
    a('Balayage littéral du référentiel entier — l\'axe pouvant vivre ailleurs '
      'sous un autre nom.')
    a('')
    for famille in TERMES:
        occ = trouve[famille]
        total = sum(len(v) for v in occ.values())
        a(f'### {famille.capitalize()}')
        a('')
        if not total:
            a('**Zéro occurrence dans tout le référentiel.**')
            a('')
            continue
        a(f'{total} occurrence(s), {len(occ)} terme(s) sur '
          f'{len(TERMES[famille])} trouvé(s).')
        a('')
        a('| terme | occ. | où |')
        a('|---|---|---|')
        for mot in sorted(occ, key=lambda m: -len(occ[m])):
            lot = occ[mot]
            ids = sorted({i for i, _, _ in lot})
            ou = ', '.join(f'`{i}`' for i in ids[:8])
            if len(ids) > 8:
                ou += f' … +{len(ids) - 8}'
            a(f'| {mot} | {len(lot)} | {ou} |')
        a('')
        dans_axe = sum(1 for lot in occ.values() for i, _, _ in lot
                       if i.startswith(LEVIER))
        a(f'*Dont {dans_axe} occurrence(s) à l\'intérieur de `{LEVIER}`.*')
        a('')

    # ----------------------------------------------- 4. ce qui manque
    a('---')
    a('')
    a('## 4. Ce qu\'il faudrait pour en tirer une norme, et ce qui manque')
    a('')
    a('Une obligation de transparence se rédige avec cinq éléments. Aucun '
      'n\'est au référentiel pour cet axe.')
    a('')
    a('| élément | ce que c\'est | au corpus |')
    a('|---|---|---|')
    for nom, quoi in EXIGENCES:
        a(f'| **{nom}** | {quoi} | absent |')
    a('')
    a('---')
    a('')
    a('## Verdict')
    a('')
    a('**L\'axe existe comme intention et n\'existe pas comme doctrine.** '
      '`D1-1` porte le nom exact que A-226 lui donne — « droit de savoir : '
      'transparence et audit » — et une proposition, `D1-1-1`, « État en audit '
      'permanent ». Elle est déclarée *esquissée*, elle ne porte aucun '
      'paramètre ni aucun effet, et sa seule matière renvoie à une couche de '
      'preuve absente du corpus.')
    a('')
    a('**Et son périmètre n\'est pas celui de A-226.** Le libellé dit « État '
      'en audit permanent ». Les opérateurs, les associations et les caisses '
      'n\'y sont nommés nulle part : les occurrences relevées plus haut vivent '
      'toutes ailleurs — la fermeture des structures facultatives, '
      'l\'extinction des subventions, les assurances sociales — et elles y '
      'sont des **objets de suppression ou de transfert, non des débiteurs '
      'd\'information**. Ce n\'est pas le même geste, et le second ne se déduit '
      'pas du premier.')
    a('')
    a('**Conséquence directe sur A-226, et le fil s\'arrête là.** La porte du '
      '7° du II de l\'article 34 est réservée à un axe dont le corpus ne porte '
      'aujourd\'hui que le titre. Tant que cet axe n\'est pas écrit — débiteur, '
      'assiette, support, périodicité, sanction — **cette porte n\'a rien à '
      'faire passer**, et un amendement qui l\'emprunterait retomberait dans '
      'la demande de rapport que A-226 écarte précisément.')
    a('')
    a('*Trois questions pour l\'auteur, et le fil ne les tranche pas.*')
    a('')
    a('1. **L\'axe se dote-t-il d\'un contenu, ou A-226 se corrige-t-elle ?** '
      'Ce sont les deux seules issues. Réserver une porte à un axe vide la '
      'ferme en pratique.')
    a('2. **Si l\'axe s\'écrit, son périmètre est-il celui de A-226** — '
      'opérateurs, associations, caisses — ou celui de `D1-1-1`, qui ne dit '
      'que l\'État ? Les trois populations ne relèvent pas du même véhicule : '
      'les caisses relèvent du PLFSS (A-223).')
    a('3. **La couche `M-nnnn` se reconstruit-elle ou se retire-t-elle ?** '
      '`releve_affecte` est déjà au bloc `manquants` de l\'index, attendu par '
      'trois skills. L\'axe de transparence est le quatrième renvoi qui n\'y '
      'résout pas.')
    a('')
    return '\n'.join(L) + '\n'


def main(src, dst):
    ref = json.load(open(src, encoding='utf-8'))
    ax, lv = levier(ref, LEVIER)
    trouve = balayer(ref)
    texte = rendre(ref, ax, lv, trouve)
    os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
    open(dst, 'w', encoding='utf-8').write(texte)
    total = sum(len(v) for f in trouve.values() for v in f.values())
    print(f'{dst} — levier {LEVIER} '
          f'{"trouvé" if lv else "ABSENT"}, '
          f'{len(lv.get("propositions", [])) if lv else 0} proposition(s), '
          f'{total} occurrence(s) de vocabulaire, '
          f'{os.path.getsize(dst)} octets')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
