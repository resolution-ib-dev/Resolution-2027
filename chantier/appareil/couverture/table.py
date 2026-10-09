# -*- coding: utf-8 -*-
"""Table de couverture du CGI de l'expert — générateur.

**Cette table ne se verse pas au coffre.** C'est un dérivé daté : 284 de ses
lignes portent un rang du III de la clause, 90 un rang de colonne, et les deux
numérotations bougent à chaque passe. Le générateur se verse à sa place, et la
table se rejoue au millésime du jour. **Chaque régénération rend la table à
l'auteure en pièce jointe** — condition posée par le fil de tête le 20261009.

---

## Spécification des neuf colonnes

| # | colonne | ce qu'elle porte | d'où elle vient |
|---|---|---|---|
| 1 | `article` | le numéro d'article du code général des impôts, graphie du dépôt de droit | union des quatre tables de l'expert, plus les articles portés au seul relevé de datation |
| 2 | `operation_expert` | l'opération de l'expert en une ligne — supprimé, allégé, réécrit, complété, renuméroté — suivie du détail : segments insérés, segments retirés, paramètre, volume final | `cgi_expert_articles.tsv`, croisé avec insertions, suppressions et paramètres |
| 3 | `etat_du_droit_20261007` | `EXISTE`, `EXISTE_FIN_PROGRAMMEE`, `VIGUEUR_DIFF`, `ABSENT`, `ABROGE` | `droit.article`, version applicable au jour du millésime |
| 4 | `operation_de_nos_pieces` | abrogation entière, abrogation partielle, réécriture, modification, gage, citation — vide si nos pièces ne touchent pas l'article | dispositifs du paquet, clause prise au coffre |
| 5 | `rang` | le rang de l'amendement qui porte l'opération, et la division de la clause quand c'est elle | registre des colonnes, et le III, III quater ou III quinquies de la clause |
| 6 | `verdict` | intégré conforme · intégré divergent · absent de nos pièces · hors périmètre PLF 2027 — quatre verdicts, pas de cinquième | comparaison des colonnes 2 et 4 |
| 7 | `ecart_ou_motif` | ce qui diverge, ou pourquoi l'article sort du périmètre ; porte le signalement d'un article dont la version a changé depuis la base de l'expert | règle D-1 : le corpus prime, l'écart se déclare |
| 8 | `bloc` | la division du code qui porte l'article, jusqu'au chapitre | chemin hiérarchique du dépôt de droit, jamais une étiquette écrite à la main |
| 9 | `piece_qui_devrait_le_porter` | le rang qui traite déjà l'article, à défaut la pièce qui traite le plus d'articles du même bloc, à défaut « pièce de complément due » | relevé sur le paquet |

**Règle de fond, acquise et non rouverte (D-1)** : le corpus prime sur la
rédaction de l'expert, et l'écart se déclare. La table ne juge pas qui a raison ;
elle dit où les deux divergent.

**Ce que la table ne porte pas** : aucun arbitrage, aucune correction, aucun
exposé. Elle se lit, elle ne se corrige pas.

Emploi :

    python3 appareil/couverture/table.py      # écrit la table et rend sa mesure
"""

import collections, csv, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
sys.path.insert(0, '/home/claude/droit')
import droit                                                    # noqa
import sources, pieces, nos_pieces                              # noqa

SORTIE = os.path.join(RACINE, 'referentiels', 'couverture_cgi_expert.tsv')
CGI = 'code général des impôts'
JOUR = sources.JOUR
FORT = {'abrogation entière': 4, 'abrogation partielle': 3, 'réécriture': 3,
        'modification': 2, 'gage': 1, 'citation': 0}


def chemins():
    """article -> chemin hiérarchique de sa version applicable au millésime."""
    out = {}
    for ch, arts in sources.divisions_cgi().items():
        for a in arts:
            if len(ch) > len(out.get(a, '')):
                out[a] = ch
    return out


def bloc(ch):
    """La division porteuse, au niveau du chapitre quand il existe."""
    els = [e.split(' : ')[0].strip() for e in ch.split(' > ')]
    garde = [e for e in els if e.startswith(('Livre', 'Première Partie', 'Deuxième Partie',
                                             'Troisième Partie', 'Titre', 'Chapitre'))]
    return ' > '.join(garde[:4]) or (els[0] if els else '')


def nos_operations():
    """article -> (opération, rang, repère)."""
    out = dict((k, v) for k, v in nos_pieces.clause_sur_cgi().items())
    nommes, _ = pieces.nommes()
    for num, faits in nommes.items():
        rang, op, rel = max(faits, key=lambda x: FORT.get(x[1], 0))
        if op in ('citation', 'gage') and num in out:
            continue
        if num in out and FORT.get(op, 0) <= FORT.get(out[num][0], 0):
            continue
        out[num] = (op, rang, rel)
    return out


HORS = 'hors périmètre PLF 2027'


def verdict(ope, etat, ch, num):
    """Les quatre verdicts, et pas de cinquième."""
    if etat in ('ABSENT', 'ABROGE'):
        return HORS, 'absent ou abrogé du droit au millésime — la rédaction part d’un état périmé'
    if ch.startswith('Livre II'):
        return HORS, 'livre II — recouvrement et procédure, hors des objectifs du dépôt'
    if num.startswith('1600-0'):
        return HORS, 'renvoi du CGI — le siège est au code de la sécurité sociale'
    nous = ope[0] if ope else None
    if nous in (None, 'citation', 'gage'):
        return 'absent de nos pièces', '' if nous is None else f'seulement {nous}'
    exp = ope and None
    return None, ''


def tranche(op_expert, nous):
    """Verdict de comparaison, quand les deux opérations se comparent."""
    e = (op_expert or '').split(' (')[0]
    if e == 'supprimé':
        if nous == 'abrogation entière':
            return 'intégré conforme', ''
        return ('intégré divergent',
                'l’expert abroge l’article entier, nos pièces n’en traitent qu’une part '
                f'({nous})')
    if e in ('allégé', 'réécrit', 'complété'):
        if nous == 'abrogation entière':
            return ('intégré divergent',
                    f'l’expert {e} l’article, nos pièces l’abrogent en entier')
        return ('intégré conforme',
                f'l’expert {e} l’article, nos pièces en traitent une part ({nous}) — '
                'arbitrage de rédaction dû')
    if e.startswith('renuméroté'):
        return 'intégré divergent', f'l’expert renumérote ({op_expert}), nos pièces non'
    return 'intégré divergent', f'opération de l’expert non comparable : {op_expert}'


def construire():
    ent = sources.entree()
    ope = nos_operations()
    ch = chemins()
    lignes = []
    for num in sorted(ent, key=_tri):
        e = ent[num]
        etat = sources.etat_droit(num)
        c = ch.get(num, '')
        b = bloc(c)
        o = ope.get(num)
        v, motif = verdict(o, etat, c, num)
        if v is None:
            v, motif = tranche(e['op_expert'], o[0])
        if e['bouge'] == 'version changée' and v != HORS:
            motif = (motif + ' · ' if motif else '') + \
                'article à contrôler avant emploi — version changée depuis la base de l’expert'
        lignes.append({
            'article': num,
            'operation_expert': e['op_expert'] + (' — ' + e['detail_expert']
                                                  if e['detail_expert'] else ''),
            'etat_du_droit_20261007': etat,
            'operation_de_nos_pieces': o[0] if o else '',
            'rang': o[1] if o else '',
            'verdict': v,
            'ecart_ou_motif': motif,
            'bloc': b,
            'piece_qui_devrait_le_porter': '',
        })
    _porteur(lignes, ope)
    return lignes


def _porteur(lignes, ope):
    """Par bloc : la pièce qui en traite déjà le plus d'articles."""
    par_bloc = collections.defaultdict(collections.Counter)
    for l in lignes:
        if l['rang']:
            par_bloc[l['bloc']][l['rang'].split(',')[0]] += 1
    for l in lignes:
        if l['verdict'] == HORS:
            l['piece_qui_devrait_le_porter'] = '—'
            continue
        if l['rang']:
            l['piece_qui_devrait_le_porter'] = l['rang'].split(',')[0]
            continue
        c = par_bloc.get(l['bloc'])
        l['piece_qui_devrait_le_porter'] = (c.most_common(1)[0][0] + ' (bloc)') if c \
            else 'pièce de complément due'


def _tri(n):
    try:
        import clause
        return clause.cle(n)
    except Exception:
        return ((9, 0, n),)


COLS = ['article', 'operation_expert', 'etat_du_droit_20261007', 'operation_de_nos_pieces',
        'rang', 'verdict', 'ecart_ou_motif', 'bloc', 'piece_qui_devrait_le_porter']

if __name__ == '__main__':
    L = construire()
    with open(SORTIE, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, COLS, delimiter='\t', quoting=csv.QUOTE_NONE,
                           escapechar=None, lineterminator='\n')
        w.writeheader()
        for l in L:
            w.writerow({k: str(v).replace('\t', ' ') for k, v in l.items()})
    print(len(L), 'lignes ·', os.path.getsize(SORTIE), 'octets')
    for k, v in collections.Counter(l['verdict'] for l in L).most_common():
        print(f'  {k:<26} {v}')
