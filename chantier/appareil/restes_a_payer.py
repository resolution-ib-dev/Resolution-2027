#!/usr/bin/env python3
"""Restes à payer — la coupe en dépense finale, 2027-2030 — 20261118.

Le croisé mesure × mois (`referentiels/calendrier_mesures_mois_20261116.tsv`)
compte chaque coupe à sa date d'effet, « en mesure », hors règle de CP
résiduel. Ce module en tire la coupe **en dépense finale** : ce que les agents
privés cessent effectivement de recevoir, mois par mois, une fois réglés les
engagements déjà pris.

Deux couches, et une seule par ligne :

  - **État** — la ligne retire des crédits dont l'État est le payeur final
    (titres 2, 3, 5 et 6 versés à un privé). Le CP résiduel du § 3 du registre
    règle les engagements en cours (R-R) ; il s'étale sur les exercices
    suivants par une clé de décaissement.
  - **Agence ou collectivité** — l'État coupe un transfert à une entité
    publique (subvention pour charges de service public, concours aux
    collectivités) ; l'entité baisse sa propre dépense finale plus lentement
    (contrats, conventions, marchés en cours). L'écart se finance sur sa
    trésorerie ; il pèse sur le solde public consolidé, qui est l'opposé de
    la somme des privés (règle de l'auteur, 20261116).

**La clé de décaissement** (forme *posée*, taux *relevé* ou *déduit*) :
une tranche de coupe entrée au mois τ garde, pendant sa k-ième année
(mois τ + 12(k−1) à τ + 12k − 1), une part r^k de la dépense antérieure.
C'est le profil stationnaire géométrique : si chaque génération d'AE se paie
pour (1 − r) l'année de l'engagement puis pour r^j(1 − r) la j-ième année
suivante, l'arrêt des AE laisse r la première année, r² la deuxième, et un
stock de restes à payer égal à r / (1 − r) années de paiement. La première
année redonne exactement la règle du § 1 du registre (CP minorés =
AE × (1 − résiduel)).

  construire   écrit `referentiels/restes_a_payer_20261118.tsv` et imprime
               le résumé utilisé par la note
               `methode/etats/RESTES_a_payer_20261118.md`.
  controler    rejoue le calcul, le confronte au TSV écrit et aux pièces ;
               code 1 au premier écart.

Md€, signe positif = économie. Ne modifie ni le registre ni les calendriers.
"""
import csv, re, subprocess, sys
from collections import OrderedDict, defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SITE = RACINE.parent.parent / 'Site-ETNP' / 'site' / 'donnees'
REGISTRE = RACINE / 'livrables/registre_calcul_etatB.md'
MESURE = RACINE / 'referentiels/calendrier_mesures_mois_20261116.tsv'
COMPTE = RACINE / 'referentiels/calendrier_compte_complet_20261117.tsv'
PARAM = RACINE / 'referentiels/parametres_credits_20261116.tsv'
OPER = RACINE / 'referentiels/operateurs_jaune2026_20261112.tsv'
JAUNE = SITE / 'PLF 2026_Jaune - Operateurs.pdf'
SORTIE = RACINE / 'referentiels/restes_a_payer_20261118.tsv'

ANNEES = (2027, 2028, 2029, 2030)
COLS = [f'{a}-{m:02d}' for a in ANNEES for m in range(1, 13)]
N = len(COLS)                  # 48 mois
QUEUE = 12 * 10                # horizon de la queue après 2030, en mois
TOL = 0.0051


def fl(s):
    s = (s or '').strip().replace(' ', '').replace(' ', '').replace(',', '.')
    s = s.replace('−', '-').replace('*', '')
    try:
        return float(s)
    except ValueError:
        return None


def par_an(serie):
    return [sum(serie[12 * i:12 * i + 12]) for i in range(4)]


# ---------------------------------------------------------------- lectures

def lire_mesure():
    """Le croisé mesure × mois, 27 lignes D (relevé)."""
    lignes = OrderedDict()
    with open(MESURE, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            lignes[r['cellule']] = {
                'ligne': r['ligne_doctrinale'], 'pan': r['pan'], 'agent': r['agent'],
                'perimetre': r['perimetre'], 'date': r['date_effet_2027'],
                'rythme': r['rythme'], 'programme': r['programme_porteur'],
                'mois': [float(r[c]) for c in COLS],
                's5': [fl(r[f'registre_s5_{a}']) for a in ANNEES],
            }
    return lignes


def section(texte, debut, fin):
    i = texte.index(debut)
    j = texte.index(fin, i + len(debut))
    return texte[i:j]


def lire_registre():
    """§ 2 (restitution), § 3 (résiduel par régime), § 5 (totaux) — relevés."""
    t = REGISTRE.read_text(encoding='utf-8')
    # § 3 : table des régimes
    s3 = section(t, '## 3. Le CP résiduel', '### 3 bis')
    reg = {}
    for l in s3.splitlines():
        c = [x.strip() for x in l.strip('|').split('|')]
        if len(c) == 4 and c[3].startswith('**') and '%' in c[3]:
            reg[c[0]] = (c[1], fl(c[3].split('%')[0]) / 100)
    res = {
        'titre 2': reg['AE = CP par texte'][1],
        'cat. 61 et 64': reg['AE = CP à l\'arrondi'][1],
        'plancher': reg['plancher commun'][1],
        'cat. 62': reg['stock de dossiers'][1],
        'cat. 63': reg['stock de conventions'][1],
        'titre 5': reg['opérations engagées'][1],
    }
    # § 2 : restitution mensuelle 2027 et rythme annuel
    s2 = section(t, '## 2. La restitution', '## 3. Le CP résiduel')
    m27 = []
    for l in s2.splitlines():
        c = [x.strip() for x in l.strip('|').split('|')]
        if len(c) == 3 and c[0] and c[0] not in ('mois 2027',) and not c[0].startswith('---'):
            v = fl(c[2])
            if v is None:
                continue
            m27 += [v] * (6 if c[0].startswith('janvier à juin') else 1)
    an = re.search(r'([\d,]+) Md€ en 2027 · ([\d,]+) Md€ en rythme annuel', s2)
    total27, annuel = fl(an.group(1)), fl(an.group(2))
    restit = m27 + [annuel / 12] * 36
    # § 5 : coupes, restitution, solde
    s5 = section(t, '## 5. Trajectoire consolidée 2027-2030', '### Mise à niveau du 20261118')
    tot = {}
    for l in s5.splitlines():
        c = [x.strip() for x in l.strip('|').split('|')]
        for cle in ('Coupes, 27 lignes', 'Restitution', 'Solde du budget'):
            if c and c[0] == f'**{cle}**':
                tot[cle] = [fl(x) for x in c[1:5]]
    return res, restit, total27, annuel, tot


def lire_parametres():
    """Par ligne D : poids de chaque nature (AE cible du projet), règle de
    résiduel et rapport CP/AE de la cible (relevés à la tablette)."""
    out = defaultdict(lambda: defaultdict(lambda: [0.0, 0.0, None]))
    tot_ae = tot_cp = 0.0
    with open(PARAM, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            ae, cp = fl(r['cible_projet_ae']) or 0.0, fl(r['cible_projet_cp']) or 0.0
            if r['retenu'] == 'oui':
                tot_ae += ae
                tot_cp += cp
            cat = r['categorie']
            cls = 'titre 5' if r['titre'] == '5' else f'cat. {cat}'
            a = out[r['ligne_registre']][cls]
            a[0] += ae
            a[1] += cp
            a[2] = float(r['regle_residuel'])
    return out, tot_ae / 1e9, tot_cp / 1e9


def lire_operateurs():
    """Financement de l'État 2026 par opérateur (k€, taxes en €) — relevé."""
    out = {}
    with open(OPER, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            k = sum(fl(r[c]) or 0 for c in ('scsp_2026', 'investissement_2026',
                                             'transferts_2026', 'dotations_2026'))
            out[r['operateur']] = (k / 1e6, (fl(r['taxes_affectees_2026']) or 0) / 1e9)
    return out


def lire_jaune():
    """Jaune « Opérateurs de l'État », PLF 2026 (classeurs du site) :
    restes à payer de l'Ademe au 31/12/2024 et trésorerie 2022-2024."""
    txt = subprocess.run(['pdftotext', '-layout', str(JAUNE), '-'],
                         capture_output=True, text=True, check=True).stdout
    L = txt.split('\n')
    # restes à payer de l'Ademe : bloc « Engagements hors bilan »
    i0 = next(i for i, l in enumerate(L)
              if l.startswith('Dettes et engagements hors bilan des opérateurs') and '....' not in l)
    ia = next(i for i in range(i0, len(L)) if L[i].startswith('ADEME'))
    rap = None
    for l in L[ia:ia + 40]:
        m = re.search(r'Restes à payer\s+([\d ]+)$', l.strip())
        if m:
            rap = int(m.group(1).replace(' ', '')) / 1e6
            break
    # trésorerie : table « Trésorerie 2022/2024 des opérateurs de l'État »
    it = [i for i, l in enumerate(L) if l.strip().startswith("Trésorerie 2022/2024 des opérateurs de l'État")][-1]
    fin = next(i for i in range(it, len(L)) if "Données immobilières" in L[i])
    hdr, tot, rows = None, defaultdict(float), {}
    for l in L[it:fin]:
        if re.search(r'2022\s+2023\s+2024', l):
            hdr = {y: l.index(y) + 4 for y in ('2022', '2023', '2024')}
            continue
        if not hdr:
            continue
        for m in re.finditer(r'-?\d{1,3}(?: \d{3})*(?=\s{2,}|$)', l):
            if m.start() < 60:
                continue
            y = min(hdr, key=lambda k: abs(hdr[k] - m.end()))
            if abs(hdr[y] - m.end()) > 6:
                continue
            v = int(m.group().replace(' ', '')) / 1e6
            tot[y] += v
            rows.setdefault(l[:60].strip(), {})[y] = v
    page_tr = '\n'.join(L[:it]).count('\f') + 1   # page du PDF
    page_hb = '\n'.join(L[:ia]).count('\f') + 1
    def treso(prefixe):
        k = next(k for k in rows if k.startswith(prefixe))
        return rows[k].get('2024')
    return {'rap_ademe': rap, 'page_hb': page_hb, 'page_tr': page_tr,
            'tresorerie_totale': dict(tot), 'n_operateurs': len(rows),
            'treso': {'D12': treso('ADEME'), 'D5': treso('France Compétences'),
                      'D6': treso('France Travail'), 'D15': treso('ANAH')}}


def lire_compte():
    """Compte complet : circuit de restitution (A), hors épargne, chômage et
    patrimoine, par mois — le « surplus du circuit » du registre § 5."""
    surplus = [0.0] * N
    dlignes = defaultdict(lambda: [0.0] * N)
    with open(COMPTE, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['circuit'] != 'A' or r['nature'].startswith('épargne') or r['famille'] in ('chômage', 'patrimoine'):
                continue
            v = [float(r[c]) for c in COLS]
            surplus = [a + b for a, b in zip(surplus, v)]
            if re.fullmatch(r'D\d+', r['id']) and r['nature'] == 'dépense':
                dlignes[r['id']] = [a + b for a, b in zip(dlignes[r['id']], v)]
    return surplus, dlignes


# ----------------------------------------------------------- hypothèses

def hypotheses(res, par, ope, jau):
    """Une liste de composantes par ligne : (part, r bas, r central, r haut,
    statut, couche, terme, nul_2027, source). r = part de la dépense
    antérieure gardée la première année ; la k-ième année garde r^k."""
    H = OrderedDict()
    J = 'Jaune « Opérateurs de l’État » PLF 2026'

    def etat(cel, r, statut, source, bas=None, haut=None, terme=None, nul27=False):
        H[cel] = [(1.0, r if bas is None else bas, r, r if haut is None else haut,
                   statut, 'État', terme, nul27, source)]

    def entite(cel, couche, bas, r, haut, statut, source, terme=None):
        H[cel] = [(1.0, bas, r, haut, statut, couche, terme, False, source)]

    # ---- État, sans reste à payer : guichet, chèques, titre 2
    s3 = 'registre § 3'
    for cel, src in (('D18', s3 + ', cat. 61 ; P2/2_6_extinction_aide_logement : « aucune marge de reste à payer »'),
                     ('D19', s3 + ', cat. 61'),
                     ('D20', s3 + ', cat. 61 ; restes à payer de la campagne 2026 déjà dans la mesure (arbitrage du 20261116)'),
                     ('D22', s3 + ', cat. 61')):
        etat(cel, res['cat. 61 et 64'], 'relevé', src)
    for cel in ('D38', 'D43'):
        etat(cel, res['titre 2'], 'relevé', s3 + ', titre 2 (LOLF art. 8) ; indemnité déjà à 30 % dans la mesure')
    # ---- État, transferts aux entreprises (cat. 62)
    for cel in ('D25', 'D27'):
        etat(cel, res['cat. 62'], 'relevé', s3 + ', cat. 62, stock de dossiers', bas=0.0)
    # D32 : cat. 62 et 64, poids des AE cibles
    p = par['D32']
    w62 = p['cat. 62'][0] / (p['cat. 62'][0] + p['cat. 64'][0])
    H['D32'] = [(w62, 0.0, res['cat. 62'], res['cat. 62'], 'relevé (taux) ; déduit (poids AE)', 'État', None, False,
                 s3 + ', cat. 62 ; poids à parametres_credits'),
                (1 - w62, 0.0, res['cat. 61 et 64'], res['cat. 61 et 64'], 'relevé', 'État', None, False, s3 + ', cat. 64')]
    # D37 : cat. 31 au plancher, titre 5 à 80 %, poids des AE cibles
    p = par['D37']
    a31, a5 = p['cat. 31'][0], p['titre 5'][0]
    H['D37'] = [(a31 / (a31 + a5), res['plancher'], res['plancher'], res['plancher'], 'relevé (taux) ; déduit (poids AE)',
                 'État', None, False, s3 + ', plancher commun, cat. 31'),
                (a5 / (a31 + a5), res['titre 5'] * 0.75, res['titre 5'], res['titre 5'], 'relevé (taux) ; posé (borne basse)',
                 'État', None, False, s3 + ', titre 5, opérations engagées')]
    # ---- associations : conventions, terme au 1er janvier 2029 (P2/etatB_02)
    terme29 = COLS.index('2029-01')
    src_a = ('P2/etatB_02 : AE éteintes dès le 1er jour, restes à payer en CP sur 2027 et 2028, terme au '
             '1er janvier 2029, ventilation « à chiffrer » ; taux transposé du registre § 3, cat. 63')
    for cel in ('D31', 'D34', 'D35', 'D36'):
        etat(cel, res['cat. 63'], 'posé (taux, transposé) ; relevé (terme)', src_a, bas=0.0, haut=0.5, terme=terme29)
    # D30 : aide au développement — CP cible / AE cible < 1 à la tablette
    p = par['D30']
    r30 = 1 - p['cat. 64'][1] / p['cat. 64'][0]
    etat('D30', r30, 'déduit', 'parametres_credits : 1 − CP/AE des cibles du projet (cat. 64)',
         bas=0.0, haut=r30, terme=terme29)
    # D29 : hébergement d'urgence — marge de reste à payer de 10 % à la pièce
    etat('D29', 0.10, 'relevé (pièce, non repris par la liasse)',
         'P2/2_6_socle_hebergement_urgence : « marge de reste à payer de dix pour cent » ; non reprise par etatB_03',
         bas=0.0)
    # ---- France 2030 : AE 2027 nulles, rien ne se retire en 2027 sans article
    for cel in ('D26', 'D33'):
        etat(cel, res['cat. 62'], 'relevé (2027 nul) ; relevé (clé cat. 62 ensuite)',
             'registre § 15 : AE 2027 nulles, programmes 421 à 425 ; ensuite registre § 3, cat. 62',
             bas=0.0, nul27=True)
    # ---- agences
    fin_ademe = sum(ope[next(k for k in ope if k.startswith('ADEME'))])
    q_ademe = jau['rap_ademe'] / (jau['rap_ademe'] + fin_ademe)
    entite('D12', 'Agence', 0.45, q_ademe, q_ademe, 'déduit',
           f'{J}, p. {jau["page_hb"]} : restes à payer {jau["rap_ademe"]:.2f} Md€ au 31/12/2024 ; '
           f'financement de l’État 2026 {fin_ademe:.2f} Md€ (operateurs_jaune2026) ; r = RAP / (RAP + flux)')
    entite('D5', 'Agence', 0.05, 0.15, 0.30, 'posé',
           'France Compétences : financements engagés (CPF, CFA) payés au service fait ; plafond : trésorerie 2024')
    entite('D6', 'Agence', 0.05, 0.15, 0.30, 'posé',
           'France Travail : masse salariale et marchés ; un sixième déjà conservé dans la mesure')
    entite('D16', 'Agence', 0.05, 0.15, 0.30, 'posé',
           'opérateurs sous subvention pour charges de service public : personnel, marchés, conventions')
    entite('D24', 'Agence', 0.15, 0.30, 0.50, 'posé',
           'sociétés de l’audiovisuel public : contrats de production et de diffusion pluriannuels')
    entite('D15', 'Agence', 0.25, 0.50, 0.75, 'posé',
           'Anah : « les dossiers déjà engagés sont payés » (P2/etatB_01) ; prime versée à la fin des travaux')
    # ---- collectivités qui restent
    entite('D40', 'Collectivité', 0.05, 0.15, 0.30, 'posé',
           'dépense culturelle locale : personnel, subventions annuelles, équipements ; transposé du plancher § 3')
    entite('D41', 'Collectivité', 0.15, 0.25, 0.50, 'posé',
           'coll_P2_04, IV (relevé) : engagements juridiques souscrits avant 2027 exécutés jusqu’à leur terme ; '
           'taux transposé du registre § 3, cat. 63')
    entite('D42', 'Collectivité', 0.10, 0.15, 0.30, 'posé',
           'marchés de fonctionnement en cours ; taux transposé du plancher commun § 3 (cat. 31)')
    return H


# --------------------------------------------------------------- calcul

def garde(r, s, t, terme, nul27):
    """Part de la dépense antérieure encore payée au mois t, pour une tranche
    entrée au mois s (relatif à la tranche : t − s ≥ 0)."""
    if nul27 and t < 12:
        return 1.0
    if terme is not None and t >= terme:
        return 0.0
    return r ** ((t - s) // 12 + 1)


def depense_finale(mois, comp, choix=2, decale=0, horizon=N):
    """mois : mesure mensuelle (N valeurs). choix : 1 bas, 2 central, 3 haut.
    decale : nombre de mois dont l'horloge de la clé avance (piste c)."""
    delta = [mois[0]] + [mois[t] - mois[t - 1] for t in range(1, N)]
    out = [0.0] * horizon
    for t in range(horizon):
        v = 0.0
        for s in range(min(t + 1, N)):
            if delta[s] == 0:
                continue
            g = 0.0
            for c in comp:
                r = c[choix]
                g += c[0] * garde(r, s - decale, t, c[6], c[7])
            v += delta[s] * (1 - g)
        out[t] = v  # au-delà de 2030, la mesure reste à son niveau de décembre 2030
    return out


def calcul(H, M, choix=2, decale_lignes=(), decale=0):
    df, rap = OrderedDict(), OrderedDict()
    queue = 0.0
    for cel, d in M.items():
        dec = decale if cel in decale_lignes else 0
        f = depense_finale(d['mois'], H[cel], choix, dec, N + QUEUE)
        df[cel] = f[:N]
        rap[cel] = [a - b for a, b in zip(d['mois'], f[:N])]
        queue += sum(d['mois'][-1] - x for x in f[N:])
    return df, rap, queue


def somme(series):
    return [sum(v[t] for v in series) for t in range(N)]


def bascule(solde):
    """Premier mois où le solde mensuel passe sous zéro, après un mois positif."""
    for t in range(1, N):
        if solde[t - 1] >= 0 > solde[t]:
            return COLS[t]
    return None


def resultats():
    M = lire_mesure()
    res, restit, total27, annuel, s5 = lire_registre()
    par, liasse_ae, liasse_cp = lire_parametres()
    ope = lire_operateurs()
    jau = lire_jaune()
    surplus_a, dcompte = lire_compte()
    H = hypotheses(res, par, ope, jau)
    R = {}
    for nom, ch in (('bas', 1), ('central', 2), ('haut', 3)):
        R[nom] = calcul(H, M, ch)
    mes = somme([d['mois'] for d in M.values()])
    out = {'M': M, 'H': H, 'res': res, 'restit': restit, 'total27': total27, 'annuel': annuel,
           's5': s5, 'par': par, 'liasse': (liasse_ae, liasse_cp), 'jau': jau, 'ope': ope,
           'surplus_a': surplus_a, 'dcompte': dcompte, 'R': R, 'mes': mes}
    # sensibilité : une famille d'hypothèses à la fois, bas puis haut
    familles = OrderedDict([
        ('collectivités, D40-D42 (posé)', ('D40', 'D41', 'D42')),
        ('agences sous subvention, D5, D6, D16, D24 (posé)', ('D5', 'D6', 'D16', 'D24')),
        ('Anah, D15 (posé)', ('D15',)),
        ('Ademe, D12 (déduit)', ('D12',)),
        ('associations, D29-D36 (posé / déduit)', ('D29', 'D30', 'D31', 'D34', 'D35', 'D36')),
        ('État, cat. 62 et France 2030 après 2027 (relevé ; bas = rythme déjà net)', ('D25', 'D26', 'D27', 'D32', 'D33')),
        ('État, titre 5 de D37 (relevé ; bas = 60 %)', ('D37',)),
    ])
    sens = OrderedDict()
    for nom, cels in familles.items():
        v = {}
        for ch in (1, 3):
            Hx = OrderedDict((c, H[c] if c not in cels else
                              [(k[0], k[1], k[ch], k[3], k[4], k[5], k[6], k[7], k[8]) for k in H[c]])
                             for c in H)
            df, _, _ = calcul(Hx, M, 2)
            v[ch] = par_an(somme(df.values()))
        sens[nom] = v
    out['sens'] = sens
    # pistes de modulation
    df_c, rap_c, _ = R['central']
    dfs = somme(df_c.values())
    ecart = [a - b for a, b in zip(mes, dfs)]
    # a) marche de restitution de 2028 calée sur la dépense finale
    e28 = par_an(ecart)[1]
    restit_a = restit[:12] + [x - e28 / 12 for x in restit[12:24]] + restit[24:]
    # b) restes à payer de 2028 sur conventions et dossiers de l'État, soldés par anticipation en 2027
    lignes_b = ('D25', 'D27', 'D29', 'D30', 'D31', 'D32', 'D34', 'D35', 'D36')
    b28 = sum(par_an(rap_c[c])[1] for c in lignes_b)
    dfs_b = list(dfs)
    for t in range(12):
        dfs_b[t] -= b28 / 12
    for t in range(12, 24):
        dfs_b[t] += b28 / 12
    # c) gel des engagements au 1er janvier 2027 pour les lignes datées du 1er juillet qui portent un reste à payer
    lignes_c = tuple(c for c, d in M.items() if 'juil' in d['date'] and any(k[2] > 0 for k in H[c]))
    df_cc, _, _ = calcul(H, M, 2, lignes_c, 6)
    dfs_c = somme(df_cc.values())
    out['pistes'] = {'a': (e28, restit_a), 'b': (b28, lignes_b, dfs_b), 'c': (lignes_c, dfs_c)}
    return out


# --------------------------------------------------------------- écriture

def fmt(x):
    return f'{x:.6f}'


def construire():
    o = resultats()
    M, H = o['M'], o['H']
    df, rap, queue = o['R']['central']
    entete = ['cellule', 'ligne_doctrinale', 'serie', 'couche', 'agent', 'date_effet_2027',
              'cle_r_bas', 'cle_r_central', 'cle_r_haut', 'terme', 'statut', 'source'] + COLS + \
             [f'total_{a}' for a in ANNEES]
    rows = []

    def row(cel, lib, serie, couche, agent, date, comp, statut, source, vals):
        rb = ' + '.join(f'{k[0]:.3f}×{k[1]:.3f}' for k in comp) if comp else ''
        rc = ' + '.join(f'{k[0]:.3f}×{k[2]:.3f}' for k in comp) if comp else ''
        rh = ' + '.join(f'{k[0]:.3f}×{k[3]:.3f}' for k in comp) if comp else ''
        terme = '; '.join(sorted({COLS[k[6]] for k in comp if k[6] is not None})) if comp else ''
        rows.append([cel, lib, serie, couche, agent, date, rb, rc, rh, terme, statut, source] +
                    [fmt(v) for v in vals] + [f'{v:.4f}' for v in par_an(vals)])

    for cel, d in M.items():
        comp = H[cel]
        couche = comp[0][5]
        statut = ' ; '.join(dict.fromkeys(k[4] for k in comp))
        source = ' | '.join(dict.fromkeys(k[8] for k in comp))
        for serie, vals in (('mesure', d['mois']), ('depense_finale', df[cel]), ('reste_a_payer', rap[cel])):
            row(cel, d['ligne'], serie, couche, d['agent'], d['date'], comp, statut, source, vals)
    mes = o['mes']
    restit = o['restit']
    agr = OrderedDict()
    agr['coupes_mesure'] = mes
    for nom in ('bas', 'central', 'haut'):
        agr[f'coupes_depense_finale_{nom}'] = somme(o['R'][nom][0].values())
    for couche in ('État', 'Agence', 'Collectivité'):
        agr[f'reste_a_payer_{couche}'] = somme([rap[c] for c in M if H[c][0][5] == couche])
    agr['restitution'] = restit
    agr['solde_mesure'] = [a - b for a, b in zip(mes, restit)]
    for nom in ('bas', 'central', 'haut'):
        agr[f'solde_depense_finale_{nom}'] = [a - b for a, b in zip(agr[f'coupes_depense_finale_{nom}'], restit)]
    ecart = [a - b for a, b in zip(mes, agr['coupes_depense_finale_central'])]
    agr['circuit_A_surplus_mesure'] = o['surplus_a']
    agr['circuit_A_surplus_depense_finale'] = [a - b for a, b in zip(o['surplus_a'], ecart)]
    e28, restit_a = o['pistes']['a']
    agr['piste_a_restitution'] = restit_a
    agr['piste_a_solde'] = [a - b for a, b in zip(agr['coupes_depense_finale_central'], restit_a)]
    agr['piste_b_coupes'] = o['pistes']['b'][2]
    agr['piste_b_solde'] = [a - b for a, b in zip(o['pistes']['b'][2], restit)]
    agr['piste_c_coupes'] = o['pistes']['c'][1]
    agr['piste_c_solde'] = [a - b for a, b in zip(o['pistes']['c'][1], restit)]
    for k, v in agr.items():
        rows.append(['TOTAL', '', k, '', '', '', '', '', '', '', 'calculé', ''] +
                    [fmt(x) for x in v] + [f'{x:.4f}' for x in par_an(v)])
    with open(SORTIE, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(entete)
        w.writerows(rows)
    print(f'écrit {SORTIE.relative_to(RACINE)} : {len(rows)} lignes')
    resume(o, agr, queue)


def resume(o, agr, queue):
    p = lambda v: ' · '.join(f'{x:+.2f}' for x in par_an(v))
    q = lambda v: ' · '.join(f'{x:.2f}' for x in par_an(v))
    print('\n== résidus relevés au § 3 ==', o['res'])
    print('liasse P2 (parametres_credits, cibles du projet, lignes retenues) : AE %.2f, CP %.2f, écart %.2f Md€' %
          (o['liasse'][0], o['liasse'][1], o['liasse'][0] - o['liasse'][1]))
    j = o['jau']
    print('Jaune : RAP Ademe %.3f Md€ (p. %d) ; trésorerie des opérateurs %s (p. %d, %d lignes) ; %s' %
          (j['rap_ademe'], j['page_hb'], {k: round(v, 2) for k, v in j['tresorerie_totale'].items()},
           j['page_tr'], j['n_operateurs'], {k: round(v, 3) for k, v in j['treso'].items()}))
    print('\n== par exercice ==')
    for k in ('coupes_mesure', 'coupes_depense_finale_bas', 'coupes_depense_finale_central',
              'coupes_depense_finale_haut', 'reste_a_payer_État', 'reste_a_payer_Agence',
              'reste_a_payer_Collectivité', 'restitution', 'solde_mesure', 'solde_depense_finale_bas',
              'solde_depense_finale_central', 'solde_depense_finale_haut', 'circuit_A_surplus_mesure',
              'circuit_A_surplus_depense_finale', 'piste_a_restitution', 'piste_a_solde',
              'piste_b_coupes', 'piste_b_solde', 'piste_c_coupes', 'piste_c_solde'):
        print(f'{k:40s} {p(agr[k])}')
    print('queue au-delà de 2030 (central) : %.2f Md€' % queue)
    print('\n== bascule mensuelle ==')
    for k in ('solde_mesure', 'solde_depense_finale_bas', 'solde_depense_finale_central',
              'solde_depense_finale_haut', 'piste_a_solde', 'piste_b_solde', 'piste_c_solde',
              'circuit_A_surplus_mesure', 'circuit_A_surplus_depense_finale'):
        v = agr[k]
        cum, mn = 0, (None, 1e9)
        neg = [COLS[t] for t in range(N) if v[t] < 0]
        cumul = [sum(v[:t + 1]) for t in range(N)]
        cneg = next((COLS[t] for t in range(N) if cumul[t] < 0), '—')
        print(f'{k:36s} cumul négatif dès {cneg} ; bascule {bascule(v)} ; mois négatifs {len(neg)} '
              f'(premier {neg[0] if neg else "—"}) ; min {min(v):+.2f} en {COLS[v.index(min(v))]}')
    print('\n== mois, 2027-07 à 2028-06 ==')
    for t in range(6, 18):
        print(COLS[t], ' '.join(f'{agr[k][t]:+7.2f}' for k in ('coupes_mesure', 'coupes_depense_finale_central',
                                                              'restitution', 'solde_mesure',
                                                              'solde_depense_finale_central',
                                                              'circuit_A_surplus_mesure',
                                                              'circuit_A_surplus_depense_finale')))
    print('\n== par ligne (central), écart mesure − dépense finale ==')
    df, rap, _ = o['R']['central']
    for c, d in o['M'].items():
        print(f"{c:4s} {o['H'][c][0][5]:12s} r={'+'.join(f'{k[2]:.3f}' for k in o['H'][c]):12s} "
              f"mesure {q(d['mois'])} | RAP {q(rap[c])}")
    print('\n== sensibilité (coupes en dépense finale, bas / haut, par exercice) ==')
    cen = par_an(agr['coupes_depense_finale_central'])
    for nom, v in o['sens'].items():
        print(f'{nom:70s} bas {" · ".join(f"{a - b:+.2f}" for a, b in zip(v[1], cen))} | '
              f'haut {" · ".join(f"{a - b:+.2f}" for a, b in zip(v[3], cen))}')
    e28 = o['pistes']['a'][0]
    print('\npiste a : restitution 2028 réduite de %.2f Md€, soit %.2f point de taux sur 9,70' %
          (e28, e28 / o['annuel'] * 9.70))
    print('piste b : %.2f Md€ de restes à payer de 2028 soldés en 2027, lignes %s' %
          (o['pistes']['b'][0], ', '.join(o['pistes']['b'][1])))
    print('piste c : lignes %s' % ', '.join(o['pistes']['c'][0]))
    # trésorerie des agences : écart cumulé contre trésorerie 2024
    print('\n== écart cumulé des agences contre leur trésorerie 2024 ==')
    for c, tr in j['treso'].items():
        cum = [sum(rap[c][:t + 1]) for t in range(N)]
        print(f'{c} trésorerie {tr:.3f} ; écart cumulé max {max(cum):.3f} (fin 2027 {cum[11]:.3f}, fin 2028 {cum[23]:.3f})')
    cum_ag = [sum(agr['reste_a_payer_Agence'][:t + 1]) for t in range(N)]
    print(f'toutes agences : écart cumulé max {max(cum_ag):.2f} contre trésorerie totale 2024 '
          f'{j["tresorerie_totale"]["2024"]:.2f}')
    cum_co = [sum(agr['reste_a_payer_Collectivité'][:t + 1]) for t in range(N)]
    print(f'collectivités : écart cumulé max {max(cum_co):.2f} (fin 2027 {cum_co[11]:.2f})')


# --------------------------------------------------------------- contrôle

def controler():
    o = resultats()
    M = o['M']
    ech = 0

    def tenir(lib, ecart, tol=TOL):
        nonlocal ech
        ok = abs(ecart) <= tol
        ech += not ok
        print(f'{"tenu " if ok else "ÉCHEC"} {lib} : écart {ecart:+.4f} (tolérance {tol})')

    # 1. la mesure lue redonne le § 5, ligne à ligne
    for c, d in M.items():
        for i, a in enumerate(par_an(d['mois'])):
            tenir(f'{c} {ANNEES[i]} mesure = registre § 5', a - d['s5'][i]) if abs(a - d['s5'][i]) > TOL else None
    tenir('mesure, total 2028, contre registre § 5', par_an(o['mes'])[1] - o['s5']['Coupes, 27 lignes'][1])
    # 2. la restitution lue redonne le § 2 et le § 5
    tenir('restitution 2027 = § 2', par_an(o['restit'])[0] - o['total27'])
    tenir('restitution 2028 = § 5', par_an(o['restit'])[1] - o['s5']['Restitution'][1])
    # 3. les résidus du § 3 sont ceux de la tablette des paramètres
    vus = {round(k[2], 4) for cls in o['par'].values() for k in cls.values()}
    attendus = {o['res'][k] for k in ('titre 2', 'plancher', 'cat. 62', 'cat. 63', 'titre 5')}
    tenir('résidus de parametres_credits ⊂ résidus du § 3', len(vus - attendus))
    # 4. identité mesure = dépense finale + reste à payer, et dépense finale ≤ mesure
    df, rap, queue = o['R']['central']
    for c in M:
        tenir(f'{c} identité', max(abs(M[c]['mois'][t] - df[c][t] - rap[c][t]) for t in range(N)), 1e-9) \
            if max(abs(M[c]['mois'][t] - df[c][t] - rap[c][t]) for t in range(N)) > 1e-9 else None
    tenir('reste à payer ≥ 0, tous mois, toutes lignes', min(0.0, min(min(v) for v in rap.values())), 1e-9)
    # 5. la première année d'une ligne d'État redonne la chaîne du § 1 : CP = mesure × (1 − r)
    d = M['D27']
    tenir('D27 2027 : dépense finale = mesure × (1 − 0,20)', par_an(df['D27'])[0] - par_an(d['mois'])[0] * (1 - o['res']['cat. 62']))
    # 6. les lignes D du compte complet redonnent la mesure lue (même croisé)
    for c in M:
        e = max(abs(o['dcompte'][c][t] - M[c]['mois'][t]) for t in range(N)) if c in o['dcompte'] else 0.0
        if e > 1e-4:
            tenir(f'{c} compte complet = croisé', e, 1e-4)
    # 7. le TSV écrit redonne le calcul
    if SORTIE.exists():
        with open(SORTIE, encoding='utf-8') as f:
            lu = {(r['cellule'], r['serie']): [float(r[c]) for c in COLS] for r in csv.DictReader(f, delimiter='\t')}
        e = max(abs(lu[(c, 'depense_finale')][t] - df[c][t]) for c in M for t in range(N))
        tenir('TSV = calcul (dépense finale, 27 lignes)', e, 1e-6)
        e = max(abs(lu[('TOTAL', 'coupes_mesure')][t] - o['mes'][t]) for t in range(N))
        tenir('TSV = calcul (coupes en mesure)', e, 1e-6)
    else:
        tenir('TSV présent', 1.0, 0)
    # 8. aucun reste à payer sur les lignes sans engagement (titre 2, cat. 61)
    for c in ('D18', 'D19', 'D20', 'D22', 'D38', 'D43'):
        tenir(f'{c} sans reste à payer', max(abs(x) for x in rap[c]), 1e-12)
    # 9. associations : plus rien après le 1er janvier 2029
    for c in ('D30', 'D31', 'D34', 'D35', 'D36'):
        tenir(f'{c} terme au 1er janvier 2029', max(abs(x) for x in rap[c][24:]), 1e-12)
    print(f'{ech} contrôle(s) en échec.')
    return 1 if ech else 0


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'construire'
    if cmd == 'construire':
        construire()
    elif cmd == 'controler':
        sys.exit(controler())
    else:
        sys.exit(__doc__)
