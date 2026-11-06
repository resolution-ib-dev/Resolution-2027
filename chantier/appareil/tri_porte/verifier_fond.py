"""Fil machine du 20261103 — vérification de fond et de rédaction des amendements
du tri (P1 n° 35 à 38, PLFSS n° 9). Mesure, ne corrige rien.

Pour chaque visa du dispositif : dépliage des fourchettes dans l'ordre officiel
(ordre des sections, puis ordre naturel), existence au 1er juillet 2027, section,
articles de la même section laissés hors du visa, et renvois entrants relevés en
une passe sur tous les textes du dépôt, version applicable au 1er juillet 2027.

Sortie : verif_fond.json, dérivé non versé (dispositif corrigé, textes et extraits tronqués ; la table des renvois avec extraits est
`livrables/tri_prelevements/verification_machine_20261103_renvois.tsv`). Se joue depuis ce dossier."""
import sys, json, re, gzip, collections
sys.path.insert(0, '/home/user/Resolution-2027')
sys.path.insert(0, '/home/user/Resolution-2027/chantier/appareil/tri_porte')
import droit
from extraire_visas import cle, _lt

J = '2027-07-01'

# (pièce, division, code, borne basse, borne haute ou None, subdivision ou None)
V = []
def v(piece, div, code, a, b=None, sub=None):
    V.append(dict(piece=piece, div=div, code=code, a=a, b=b, sub=sub))

for x in ['235 ter ZG', '302 bis N', '302 bis O', '302 bis P', '302 bis R', '302 bis S', '302 bis T', '302 bis U',
          '302 bis V', '302 bis W', '302 bis WA', '302 bis WB', '302 bis WC', '302 bis WD', '302 bis WE', '302 bis WF',
          '302 bis WG', '302 bis X', '302 bis XA', '1605 nonies', '1609 novovicies', '1609 tricies', '1609 untricies',
          '1609 duotricies', '1609 tertricies', '1613 ter', '1613 quater', '1635 bis AE', '1635 bis AF', '1635 bis AG',
          '1635 bis AH']:
    v('P1-36', 'I, 1°', 'cgi', x)
v('P1-36', 'I, 2°', 'cgi', '1001', sub='5° ter')
for x in ['231 ter', '231 quater', '302 bis ZA', '990 D', '990 E', '990 F', '990 FA', '990 G']:
    v('P1-36', 'II, 1°', 'cgi', x)
v('P1-36', 'II, 2°', 'cibs', 'L. 421-93', 'L. 421-148')
v('P1-36', 'II, 2°', 'cibs', 'L. 421-151')
v('P1-36', 'II, 2°', 'cibs', 'L. 421-156', 'L. 421-167')
v('P1-36', 'II, 2°', 'cibs', 'L. 455-44', 'L. 455-56')
v('P1-36', 'III, A', 'cgi', '206', sub='1')
v('P1-36', 'III, B', 'monetaire', 'L. 518-16', sub='premier alinéa')

for x in ['1599 quater C', '1599 quater D', '1601', '1601-0 A', '1604', '1607 bis', '1607 ter', '1609 B', '1609 C',
          '1609 D', '1609 G', '1609 H', '1609 I']:
    v('P1-37', 'I, 1°', 'cgi', x)
v('P1-37', 'I, 1°', 'cgi', '1635 quater B', '1635 quater N')
v('P1-37', 'I, 1°', 'cgi', '1635 quater P', '1635 quater T')
v('P1-37', 'I, 2°', 'cgct', 'L. 2333-49', 'L. 2333-55-2')
v('P1-37', 'I, 2°', 'cgct', 'L. 2333-56')
v('P1-37', 'I, 2°', 'cgct', 'L. 2333-81', 'L. 2333-83')
v('P1-37', 'I, 2°', 'cgct', 'L. 2333-97')
v('P1-37', 'I, 2°', 'cgct', 'L. 3333-4', 'L. 3333-7')
v('P1-37', 'I, 2°', 'cgct', 'L. 5211-21-1')
v('P1-37', 'I, 3°', 'urbanisme', 'L. 331-1', 'L. 331-17')
v('P1-37', 'I, 4°', 'cibs', 'L. 454-39', 'L. 454-77')
v('P1-37', 'I, 5°', 'sante', 'L. 1331-7')

v('P1-38', 'I, 1°', 'travail', 'L. 3253-18')
v('P1-38', 'I, 2°', 'cgfp', 'L. 351-12', 'L. 351-15')
v('P1-38', 'I, 3°', 'sante', 'L. 4031-4')
v('P1-38', 'I, 3°', 'sante', 'L. 5141-8')
v('P1-38', 'I, 4°', 'rural', 'L. 253-8-2')
v('P1-38', 'I, 5°', 'transports', 'L. 4316-1', sub='1°')
v('P1-38', 'I, 5°', 'transports', 'L. 4316-10', 'L. 4316-12')
v('P1-38', 'I, 6°', 'environnement', 'L. 423-6', sub='deuxième et dernier alinéas')

for x in ['L. 137-13', 'L. 137-14']:
    v('SS-9', 'I, 1°', 'css', x)
v('SS-9', 'I, 1°', 'css', 'L. 137-20', 'L. 137-27')
v('SS-9', 'I, 1°', 'css', 'L. 137-30', 'L. 137-39')
v('SS-9', 'I, 1°', 'css', 'L. 137-41')
v('SS-9', 'I, 1°', 'css', 'L. 138-1', 'L. 138-9-1')
v('SS-9', 'I, 1°', 'css', 'L. 138-10', 'L. 138-16')
v('SS-9', 'I, 1°', 'css', 'L. 138-19-8', 'L. 138-19-13')
v('SS-9', 'I, 1°', 'css', 'L. 245-1', 'L. 245-5')
v('SS-9', 'I, 1°', 'css', 'L. 245-5-1 A')
v('SS-9', 'I, 1°', 'css', 'L. 245-5-1', 'L. 245-5-6')
for x in ['L. 245-6', 'L. 380-2', 'L. 382-4', 'L. 652-6', 'L. 862-3', 'L. 862-4', 'L. 862-4-1']:
    v('SS-9', 'I, 1°', 'css', x)

# Les adresses hors dépôt jusqu'au 20261105, mesurées depuis que leurs textes y sont. L'article 96 de la loi
# n° 2010-1658, abrogé au 1er janvier 2026, est retiré du n° 38 le 20261106.
v('P1-37', 'I, 6°', 'loi72_657', '3')
v('P1-38', 'I, 7°', 'forestier', 'L. 341-6')
v('P1-38', 'I, 8°', 'minier', 'L. 132-16')
v('P1-38', 'I, 9°', 'loi2003_1312', '72')
v('P1-38', 'I, 9°', 'loi2006_1666', '130')
v('SS-9', 'I, 2°', 'loi2004_803', '18')
# Siège du rang 280 du tri (prélèvements sur les loteries de la Française des jeux), abrogé par le n° 36 le 20261106.
v('P1-36', 'I, 3°', 'loi2019_486', '138', sub='I et II')

HORS = []   # tous les textes visés sont au dépôt de droit depuis le 20261105


def vivants(court):
    """version applicable au 1er juillet 2027 de chaque numéro du texte"""
    out = {}
    for k, arts in droit.charger(court).items():
        c = [a for a in arts if droit.applicable(a, J)]
        if c:
            out[k] = max(c, key=lambda x: x.get('date_debut', ''))
    return out


_viv = {}
def viv(court):
    if court not in _viv:
        _viv[court] = vivants(court)
    return _viv[court]


def chemin(a):
    return a.get('section', '')


def ordre_officiel(court):
    """ordre du code : premier article rencontré de chaque section dans l'ordre naturel
    ne suffit pas (L. 245-5-1 A) — on range par section, les sections par leur plus
    petit article, puis l'ordre naturel dans la section."""
    arts = list(viv(court).values())
    par_sec = collections.defaultdict(list)
    for a in arts:
        if cle(a['num']) is not None:
            par_sec[chemin(a)].append(a)
    def k(a):
        return cle(a['num'])
    import functools
    def cmp(x, y):
        return -1 if _lt(x, y) else (1 if _lt(y, x) else 0)
    tete = {s: min((k(a) for a in l), key=functools.cmp_to_key(cmp)) for s, l in par_sec.items()}
    secs = sorted(par_sec, key=lambda s: functools.cmp_to_key(cmp)(tete[s]))
    res = []
    for s in secs:
        res += sorted(par_sec[s], key=lambda a: functools.cmp_to_key(cmp)(k(a)))
    return res


_ord = {}
def deplier(court, a, b):
    if court not in _ord:
        _ord[court] = ordre_officiel(court)
    o = _ord[court]
    nums = [droit.norm_num(x['num']) for x in o]
    na, nb = droit.norm_num(a), droit.norm_num(b)
    if na not in nums or nb not in nums:
        return None, [x for x in (a, b) if droit.norm_num(x) not in nums]
    i, j = nums.index(na), nums.index(nb)
    if i > j:
        return None, ['ordre inversé']
    return o[i:j + 1], []


def index_renvois():
    """une passe : (cle du code cible, numéro normalisé) → citants, version au 1er juillet 2027"""
    cles = {c['cle']: droit._sans_accent(c['cle']) for c in droit._cfg()}
    idx = collections.defaultdict(list)
    for c in droit._cfg():
        try:
            arts = viv(c['court'])
        except FileNotFoundError:
            continue
        for a in arts.values():
            t = a['texte']
            for pos, numeros, fin in droit._citations(t):
                apres = droit._fenetre_apres(t, fin)
                autre = droit._code_nomme(apres, cles)
                cert = 'nomme' if autre else 'meme_texte'
                if not autre and re.match(r'\W*(?:du|de ce)\s+même\s+code', apres):
                    # « du même code » : le dernier code nommé avant la citation
                    avant = droit._sans_accent(t[:pos])
                    pos_max, autre = -1, None
                    for k_, n_ in cles.items():
                        p_ = avant.rfind(n_)
                        if p_ > pos_max or (p_ == pos_max and autre and len(k_) > len(autre)):
                            pos_max, autre = p_, k_
                    autre = autre if pos_max >= 0 else None
                    cert = 'meme_code' if autre else 'meme_texte'
                cible = autre or c['cle']
                for n in numeros:
                    idx[(cible, droit.norm_num(n))].append(dict(code=c['cle'], num=a['num'], id=a['id'],
                        extrait=droit._extrait(t, pos, fin), cert=cert))
    return idx


if __name__ == '__main__':
    sortie = []
    vises = set()
    for x in V:
        if x['b']:
            arts, manq = deplier(x['code'], x['a'], x['b'])
        else:
            a = viv(x['code']).get(droit.norm_num(x['a']))
            arts, manq = ([a], []) if a else (None, [x['a']])
        x['articles'] = [dict(num=a['num'], id=a['id'], section=a['section'], debut=a['date_debut'], fin=a['date_fin'],
                              etat=a['etat'], texte=a['texte']) for a in (arts or [])]  # texte retiré à l'écriture
        x['manquants'] = manq
        for a in x['articles']:
            vises.add((x['code'], droit.norm_num(a['num'])))
        sortie.append(x)
    # articles des mêmes sections laissés hors visa
    for x in sortie:
        secs = {a['section'] for a in x['articles']}
        reste = []
        for a in viv(x['code']).values():
            if a['section'] in secs and (x['code'], droit.norm_num(a['num'])) not in vises:
                reste.append(a['num'])
        x['hors_visa_meme_section'] = sorted(set(reste))
    idx = index_renvois()
    cle_de = {c['court']: c['cle'] for c in droit._cfg()}
    for x in sortie:
        for a in x['articles']:
            r = idx.get((cle_de[x['code']], droit.norm_num(a['num'])), [])
            r = [y for y in r if y['id'] != a['id']]
            a['renvois'] = r
            a['renvois_hors_visa'] = [y for y in r if (droit.resoudre_code(y['code'])['court'],
                                                      droit.norm_num(y['num'])) not in vises]
    for x in sortie:
        for a in x['articles']:
            a['texte'] = a['texte'][:200]
            for r in a['renvois'] + a['renvois_hors_visa']:
                r['extrait'] = r['extrait'][:160]
            a['renvois'] = len(a['renvois'])
            a['renvois_hors_visa'] = [dict(code=r['code'], num=r['num'], cert=r['cert']) for r in a['renvois_hors_visa']]
    json.dump(dict(jour=J, millesime=droit.fraicheur()[0], visas=sortie, hors_depot=HORS),
              open('verif_fond.json', 'w'), ensure_ascii=False, indent=1)
    for x in sortie:
        n = len(x['articles'])
        rh = sum(len(a['renvois_hors_visa']) for a in x['articles'])
        print(f"{x['piece']:6} {x['div']:7} {x['code']:12} {x['a']}{' à '+x['b'] if x['b'] else ''}"
              f"{' ['+x['sub']+']' if x['sub'] else ''} : {n} art. ; manquants {x['manquants']} ; "
              f"hors visa même section {x['hors_visa_meme_section'][:12]} ; renvois entrants hors visa {rh}")
