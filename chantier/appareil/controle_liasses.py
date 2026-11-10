"""controle_liasses.py — numérotation et liens logiques des trois liasses de dépôt.

Mesure, ne corrige rien. Se joue depuis chantier/ : python3 appareil/controle_liasses.py
Contrôles, par liasse :
  L1  amendements numérotés de 1 à n sans trou ni doublon ; en-tête et sommaire concordants
      (nombre annoncé, numéros, intitulés) ;
  L2  dans chaque dispositif, divisions de premier rang (I, II, II bis…) dans l'ordre, sans saut ;
      lettres (A, B, C…) et numéros (1°, 2°…) continus dans chaque division — le texte cité
      entre guillemets (rédaction insérée dans un code) n'est pas compté ;
  L3  renvois internes « au III », « le 7° du I », « aux A et B », « les I à III » :
      la division visée existe au présent article ; pour un amendement à un article du projet,
      au texte déposé (referentiels/socle_texte_*.json) ou dans ce que l'amendement insère ;
  L4  renvois d'un amendement à un autre (« le n° 28 », « P1 n° 25 ») : l'amendement existe ;
  L5  doubles emplois : un même article de code abrogé par deux amendements ;
  L6  porteurs du tri (referentiels/sort_prelevements_20261103.tsv) : l'amendement et la division
      de premier rang existent ;
  L7  dates citées par l'exposé et absentes du dispositif (à lire : une date d'une autre mesure peut
      s'y citer à bon droit).
Sortie : livrables/controle_liasses.md (rapport) ; code de retour 1 s'il y a un écart L1 à L4 ou L6."""
import re, sys, csv, json, collections, pathlib, subprocess

C = pathlib.Path(__file__).resolve().parents[1]
D = C / 'livrables' / 'depot_2027'
LIASSES = {'PLF P1': 'LIASSE_PLF_P1.md', 'PLF P2': 'LIASSE_PLF_P2.md', 'PLFSS': 'LIASSE_PLFSS.md'}
NB = ' '
ROM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
SUF = ['', 'bis', 'ter', 'quater', 'quinquies', 'sexies', 'septies', 'octies', 'nonies', 'decies']
LETTRES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NOMBRES = {'un': 1, 'deux': 2, 'trois': 3, 'quatre': 4, 'cinq': 5, 'six': 6, 'sept': 7, 'huit': 8, 'neuf': 9, 'dix': 10,
           'onze': 11, 'douze': 12, 'treize': 13, 'quatorze': 14, 'quinze': 15, 'seize': 16, 'vingt': 20, 'trente': 30,
           'quarante': 40, 'cinquante': 50, 'soixante': 60}


def nombre(mots):
    """« Trente-cinq » → 35 ; « trente-huit » → 38 ; None si illisible"""
    m = mots.lower().replace(' et ', '-').replace(' ', '-').split('-')
    tot, ok = 0, False
    for x in m:
        if x in NOMBRES:
            tot += NOMBRES[x]; ok = True
        elif x:
            return None
    return tot if ok else None


def cle_div(d):
    r, _, s = d.partition(' ')
    return (ROM.index(r) if r in ROM else 99, SUF.index(s) if s in SUF else 99)


def blocs(t):
    parts = re.split(r'\n## Amendement n° (\d+) \[(.*?)\]\n', t)
    tete = parts[0]
    out = []
    for i in range(1, len(parts), 3):
        corps = parts[i + 2]
        out.append((int(parts[i]), parts[i + 1], corps))
    return tete, out


def dispositif(corps):
    d = corps.split('EXPOSÉ SOMMAIRE')[0]
    k = d.find('suivant')
    k = d.find(':', k) + 1 if k >= 0 else 0
    if k <= 0:
        m = re.search(r'\n(?:\*\*)?I\. –', d)
        k = m.start() if m else 0
    return d[k:]


def structure(disp):
    """[(division, [(lettre ou '', [numéros])])] hors texte cité ; et la liste des écarts L2"""
    ecarts, divs = [], collections.OrderedDict()
    cur = None
    for ligne in disp.split('\n'):
        l = ligne.strip().replace('**', '')
        if not l or l.startswith(('«', '"', '“', '|', '>')):
            continue
        m = re.match(r'^([IVX]+)(?: (bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies))?\.(?: – (.*))?$', l)
        if m:
            cur = m.group(1) + (' ' + m.group(2) if m.group(2) else '')
            if cur in divs:
                ecarts.append(f'division {cur} en double')
            divs[cur] = collections.OrderedDict({'': []})
            reste = m.group(3) or ''
            m2 = re.match(r'^([A-Z])(?: (bis|ter))?\. – (.*)$', reste)
            if m2:
                divs[cur][m2.group(1) + (' ' + m2.group(2) if m2.group(2) else '')] = []
                reste = m2.group(3)
            m3 = re.match(r'^(\d+)° ', reste)
            if m3:
                divs[cur][list(divs[cur])[-1]].append(int(m3.group(1)))
            continue
        if cur is None:
            continue
        m2 = re.match(r'^([A-Z])(?: (bis|ter))?\. – (.*)$', l)
        if m2:
            divs[cur][m2.group(1) + (' ' + m2.group(2) if m2.group(2) else '')] = []
            l = m2.group(3)
        m3 = re.match(r'^(\d+)°(?: (bis|ter|quater))? ', l)
        if m3 and not m3.group(2):
            divs[cur][list(divs[cur])[-1]].append(int(m3.group(1)))
    # ordre des divisions
    vues = list(divs)
    for a, b in zip(vues, vues[1:]):
        ka, kb = cle_div(a), cle_div(b)
        if not (kb > ka):
            ecarts.append(f'divisions {a} puis {b} : ordre rompu')
        elif kb[1] == 0 and kb[0] != ka[0] + 1:
            ecarts.append(f'divisions {a} puis {b} : saut')
    if vues and vues[0] != 'I':
        ecarts.append(f'première division {vues[0]}')
    for dv, lettres in divs.items():
        ls = [x for x in lettres if x]
        base = [x for x in ls if ' ' not in x]
        if base and [LETTRES.index(x) for x in base] != list(range(len(base))):
            ecarts.append(f'{dv} : lettres {", ".join(ls)} non continues')
        for lt, nums in lettres.items():
            if nums and nums != list(range(1, len(nums) + 1)):
                ecarts.append(f'{dv}{", " + lt if lt else ""} : numéros {nums[:12]}{"…" if len(nums) > 12 else ""} non continus')
    return divs, ecarts


RENV = re.compile(r'\b(?:au|du|le|les|aux|des|la|par le|mentionnés? au|mentionnées? aux?|prévus? aux?|prévues? aux?)\s+'
                  r'((?:\d+° (?:et \d+° )?(?:du |des ))?(?:[A-Z] (?:et [A-Z] )?(?:du |des ))?'
                  r'(?:[IVX]+(?: bis| ter| quater| quinquies)?)(?:(?:, | et | à )(?:[IVX]+(?: bis| ter| quater| quinquies)?))*)\b(?!\.)')


def renvois(disp, divs, n):
    """L3 : renvois aux divisions du présent article"""
    ec = []
    txt = re.sub(r'«[^»]*»', ' ', disp.replace('\n', ' '))
    for m in RENV.finditer(txt):
        # la suite jusqu'à la fin de la phrase : un renvoi suivi d'un article, d'un code ou d'une
        # subdivision de code vise ce texte, non le présent article
        fin = txt.find('. ', m.end())
        apres = txt[m.end():(fin if fin > 0 else m.end() + 200)][:220]
        if re.search(r"(?:de l’article|des articles|de la loi|du code|de l’annexe|du même|de ce code|de la (?:\d+(?:re|e) )?sous-section|de la section|du chapitre|du titre|du livre|de la (?:première|seconde|deuxième) partie|de l’état|de l’ordonnance|du tableau)", apres) \
                and not re.match(r"\s*du présent article", apres):
            continue
        cible = m.group(1)
        romains = re.findall(r'\b([IVX]+(?: bis| ter)?)\b', cible)
        for r in romains:
            if r not in divs:
                ec.append(f'renvoi « {m.group(0).strip()} » : division {r} absente')
        m2 = re.match(r'(\d+)° (?:et (\d+)° )?(?:du|des) ([IVX]+(?: bis| ter)?)$', cible)
        if m2 and m2.group(3) in divs:
            maxi = max([max(v) if v else 0 for v in divs[m2.group(3)].values()] or [0])
            for x in (m2.group(1), m2.group(2)):
                if x and int(x) > maxi:
                    ec.append(f'renvoi « {m.group(0).strip()} » : {x}° absent du {m2.group(3)} ({maxi} au plus)')
        m3 = re.match(r'([A-Z]) (?:et ([A-Z]) )?(?:du|des) ([IVX]+(?: bis| ter)?)$', cible)
        if m3 and m3.group(3) in divs:
            for x in (m3.group(1), m3.group(2)):
                if x and x not in divs[m3.group(3)]:
                    ec.append(f'renvoi « {m.group(0).strip()} » : {x} absent du {m3.group(3)}')
    return sorted(set(ec))


SOCLES = {}


def present_au_projet(lib, corps, ecart):
    """le renvoi signalé absent du dispositif existe-t-il au texte déposé, ou dans ce que l'amendement insère ?"""
    m = re.search(r'ARTICLE (\d+)', corps)
    if not m:
        return False
    nom = 'socle_texte_plfss2027.json' if lib == 'PLFSS' else 'socle_texte_plf2027.json'
    if nom not in SOCLES:
        SOCLES[nom] = {a['numero']: a for a in json.load(open(C / 'referentiels' / nom, encoding='utf-8'))['articles']}
    art = SOCLES[nom].get(m.group(1))
    txt = re.sub(r'\(\d+\)\s*', '\n', art['dispositif']) if art else ''
    txt += '\n' + '\n'.join(re.sub(r'^«\s*', '', l) for l in corps.split('\n') if l.strip().startswith('«'))
    r = re.search(r'renvoi « .*? » : (?:division ([IVX]+(?: bis| ter)?) absente|(\S+) absent du ([IVX]+(?: bis| ter)?))', ecart)
    if not r:
        return False
    if r.group(1):
        return bool(re.search(rf'(?:^|\n)\s*{re.escape(r.group(1))}\.\s*[–-]', txt))
    sub, dv = r.group(2), r.group(3)
    mdv = re.search(rf'(?:^|\n)\s*{re.escape(dv)}\.\s*[–-](.*?)(?=\n\s*[IVX]+(?: bis| ter)?\.\s*[–-]|$)', txt, re.S)
    corps_dv = mdv.group(1) if mdv else ''
    if sub.endswith('°'):
        return bool(re.search(rf'(?:^|\n|\s){re.escape(sub[:-1])}°', corps_dv))
    return bool(re.search(rf'(?:^|\n|–\s*){re.escape(sub)}\.\s*[–-]', corps_dv))


def main():
    rapport, bloquant = ['# Contrôle des liasses — numérotation et liens logiques', ''], 0
    nums_par = {}
    struct = {}
    alire = {}
    for lib, f in LIASSES.items():
        t = (D / f).read_text(encoding='utf-8')
        tete, bl = blocs(t)
        nums = [n for n, _, _ in bl]
        nums_par[lib] = set(nums)
        ec = []
        if nums != list(range(1, len(nums) + 1)):
            ec.append(f'L1 numéros {nums}')
        m = re.search(r'([A-Z][a-zé-]+(?:-[a-zé]+)*) amendements', tete) or re.search(r'(\d+) amendements', tete)
        if m:
            v = int(m.group(1)) if m.group(1).isdigit() else nombre(m.group(1))
            if v != len(nums):
                ec.append(f'L1 en-tête : « {m.group(0)} » pour {len(nums)} amendements')
        m = re.search(r'compte ([a-zé-]+) amendements', tete)
        if m and nombre(m.group(1)) != len(nums):
            ec.append(f'L1 en-tête : « {m.group(0)} » pour {len(nums)} amendements')
        m = re.search(r'numérotation (?:continue )?va de 1 à (\d+)|de 1 à (\d+)', tete)
        if m and int(m.group(1) or m.group(2)) != len(nums):
            ec.append(f'L1 en-tête : « {m.group(0)} »')
        som = dict(re.findall(r'^\| (\d+) \| [^|]*\| (.*?) \|$', tete, re.M))
        titres = {n: ti for n, ti, _ in bl}
        if som:
            if sorted(map(int, som)) != nums:
                ec.append(f'L1 sommaire : numéros {sorted(map(int, som))} contre blocs {nums}')
            for n, o in som.items():
                if int(n) in titres and o.strip() != titres[int(n)].strip():
                    ec.append(f'L1 sommaire n° {n} : « {o[:60]}… » contre « {titres[int(n)][:60]}… »')
        m = re.search(r'répartis en ([a-z]+) lots', tete)
        if m:
            nl = len(re.findall(r'^## Lot ', tete, re.M))
            if nombre(m.group(1)) != nl:
                ec.append(f'L1 en-tête : « {m.group(0)} » pour {nl} lots')
        for n, ti, corps in bl:
            disp = dispositif(corps)
            divs, e2 = structure(disp)
            struct[(lib, n)] = divs
            additionnel = 'ARTICLE ADDITIONNEL' in corps.split('EXPOSÉ SOMMAIRE')[0]
            if additionnel:
                ec += [f'L2 n° {n} : {x}' for x in e2]
                ec += [f'L3 n° {n} : {x}' for x in renvois(disp, divs, n)]
            else:
                # amendement à un article du projet : ses renvois se lisent contre le texte déposé
                # (referentiels/socle_texte_plf*.json) et contre les divisions que l'amendement insère
                for x in renvois(disp, divs, n):
                    if not present_au_projet(lib, corps, x):
                        ec.append(f'L3 n° {n} (article du projet) : {x}')
        rapport += [f'## {lib} — {len(nums)} amendements', ''] + ([f'- {x}' for x in ec] or ['- aucun écart']) + ['']
        bloquant += len(ec)
    # L7 : dates de l'exposé absentes du dispositif (cohérence de l'amendement avec lui-même)
    ec7 = []
    DATE = re.compile(r'1er (janvier|juillet|octobre|avril) (20\d\d)')
    for lib, f in LIASSES.items():
        _, bl = blocs((D / f).read_text(encoding='utf-8'))
        for n, ti, corps in bl:
            disp, _, expo = corps.partition('EXPOSÉ SOMMAIRE')
            expo = re.split(r'\n[¹²³⁴⁵⁶⁷⁸⁹]', expo)[0]
            dd = {m.group(0) for m in DATE.finditer(disp)}
            de = {m.group(0) for m in DATE.finditer(expo)}
            hors = sorted(de - dd)
            if hors and dd:
                ec7.append(f'{lib} n° {n} : exposé {", ".join(hors)} ; dispositif {", ".join(sorted(dd))}')
    rapport += ['## Dates de l’exposé absentes du dispositif (L7, à lire)', ''] + ([f'- {x}' for x in ec7] or ['- aucune']) + ['']
    # L4 : renvois entre amendements
    ec4 = []
    for lib, f in LIASSES.items():
        t = (D / f).read_text(encoding='utf-8')
        _, bl = blocs(t)
        for n, ti, corps in bl:
            for m in re.finditer(r'\b(PLF P1|PLF P2|P1|P2|PLFSS)\s?n°\s?(\d+)', corps):
                cible = {'P1': 'PLF P1', 'P2': 'PLF P2'}.get(m.group(1), m.group(1))
                if int(m.group(2)) not in nums_par[cible]:
                    ec4.append(f'{lib} n° {n} : renvoi à {cible} n° {m.group(2)}, absent')
    rapport += ['## Renvois entre amendements (L4)', ''] + ([f'- {x}' for x in ec4] or ['- aucun écart']) + ['']
    bloquant += len(ec4)
    # L5 : doubles emplois d'abrogation (visas extraits par tri_porte/extraire_visas.py)
    ec5 = []
    try:
        subprocess.run([sys.executable, 'extraire_visas.py', '/tmp/visas_controle.json'], cwd=C / 'appareil' / 'tri_porte',
                       check=True, capture_output=True)
        V = json.load(open('/tmp/visas_controle.json'))
        par = collections.defaultdict(set)
        for v in V:
            if not v.get('partiel') and v.get('code') and v.get('article') and 'abrog' in (v.get('alinea', '') + v.get('chapeau', '')).lower():
                par[(v['code'], v['article'])].add(f"{v['liasse']} n° {v['n']}")
        for (code, art), am in sorted(par.items()):
            if len(am) > 1:
                ec5.append(f'{code} {art} : {", ".join(sorted(am))}')
    except Exception as e:  # le relevé des visas est un appoint : son échec se déclare
        ec5.append(f'relevé des visas non joué : {e}')
    rapport += ['## Articles abrogés en entier par plusieurs amendements (L5)', '']
    rapport += [f'- {x}' for x in ec5] or ['- aucun']
    rapport += ['']
    # L6 : porteurs du tri
    ec6 = []
    for r in csv.DictReader(open(C / 'referentiels' / 'sort_prelevements_20261103.tsv', encoding='utf-8'), delimiter='\t'):
        p, a = r['amendement_porteur'], r['alinea']
        m = re.match(r'(PLF P1|PLF P2|PLFSS) n° (\d+)$', p)
        if not m:
            continue
        lib, n = m.group(1), int(m.group(2))
        if n not in nums_par[lib]:
            ec6.append(f'rang {r["n"]} : {p} absent'); continue
        dv = re.match(r'([IVX]+(?: bis| ter)?)\b', a or '')
        if dv and dv.group(1) not in struct[(lib, n)]:
            ec6.append(f'rang {r["n"]} : {p}, {a} — division {dv.group(1)} absente')
    rapport += ['## Porteurs du tri (L6)', ''] + ([f'- {x}' for x in ec6] or ['- aucun écart']) + ['']
    bloquant += len(ec6)
    (C / 'livrables' / 'controle_liasses.md').write_text('\n'.join(rapport), encoding='utf-8')
    print('\n'.join(rapport))
    print(f'{bloquant} écart(s) L1 à L4 et L6 ; {len(ec5)} article(s) visé(s) par plusieurs amendements.')
    return 1 if bloquant else 0


if __name__ == '__main__':
    sys.exit(main())
