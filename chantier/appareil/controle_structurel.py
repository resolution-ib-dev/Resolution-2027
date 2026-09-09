#!/usr/bin/env python3
"""Contrôle structurel du REF_doctrine.

Ne vérifie aucun calcul : `controle_arithmetique.py` s'en charge. Vérifie que les
conditions de lecture ont été remplies avant qu'un verdict ne soit posé.

Les quatre erreurs de la session du 20260819 sont chacune détectables ici.

Usage : python3 controle_structurel.py REF_doctrine_AAAAMMJJ_vN.json
"""

import json
import re
import sys

ECHECS = []
ALERTES = []

VERDICTS_DESTRUCTIFS = ('CONTRADICTOIRE', 'IRRÉDUCTIBLE', 'NON INSTRUIT', 'absent des deux')
STATUTS = ('manuscrit', 'implicite au manuscrit', 'classeur', 'absent des deux')
PROPS = ('origine', 'base', 'portee', 'sens', 'operation', 'exact', 'verdict',
         'chaine', 'statut_ancre', 'source_ancre', 'conditions', 'nature')

NATURES = ('règle générale', 'illustration', 'agrégat', 'hypothèse')

# Marqueurs de condition littérale. Un texte qui en porte un doit porter la
# condition en clair dans `conditions`, faute de quoi elle se perd en aval.
MARQUEURS = (r'sauf|hors\b|sous réserve|à condition|dans la limite|au moins|'
             r'jusqu[’\']à|à titre|dès lors|tant que|sans préjudice|en priorité|'
             r'à l[’\']exception|exclut|exclus|ne vaut|ne s[’\']applique|'
             r'non cumulable|suppose|indépendam')
VERDICTS_LEX = ('POSÉ', 'À QUALIFIER', 'À ARRÊTER')


def ech(eid, regle, detail):
    ECHECS.append((eid, regle, detail))


def alerte(eid, regle, detail):
    ALERTES.append((eid, regle, detail))


def charger(path):
    d = json.load(open(path, encoding='utf-8'))
    idx, prop_de, props, cibles = {}, {}, {}, set()
    for a in d['axes']:
        cibles.add(a['id'])
        for lv in a['leviers']:
            cibles.add(lv['id'])
            for p in lv['propositions']:
                props[p['id']] = p
                cibles.add(p['id'])
                for x in p['parametres'] + p['effets']:
                    idx[x['id']] = x
                    prop_de[x['id']] = p
    return d, idx, prop_de, props, cibles


def controler(path):
    d, idx, prop_de, props, cibles = charger(path)
    num = re.compile(r'\d')

    for eid, x in idx.items():
        peuplee = 'verdict' in x
        porte_valeur = num.search(str(x.get('valeur', '') or x.get('chiffre', '')))

        # R1 — toute entrée porteuse de valeur est peuplée
        if porte_valeur and not peuplee:
            ech(eid, 'R1 entrée numérique non peuplée', x.get('valeur') or x.get('chiffre'))
        if not peuplee:
            continue

        # R2 — les dix propriétés sont présentes
        for k in PROPS:
            if k not in x:
                ech(eid, 'R2 propriété absente', k)

        # R3 — le statut d'ancre est l'une des trois valeurs admises
        if x.get('statut_ancre') not in STATUTS:
            ech(eid, 'R3 statut_ancre hors nomenclature', x.get('statut_ancre'))

        # R4 — une ancre du manuscrit cite son passage entre guillemets français,
        # ou se déclare explicitement comme renvoi ou comme dérivée
        sa = x.get('source_ancre', '')
        if x.get('statut_ancre') == 'manuscrit':
            if '«' not in sa and not sa.startswith(('renvoi', 'dérivé', 'somme')):
                ech(eid, 'R4 ancre manuscrit sans citation du passage', sa[:70])

        # R4bis — un implicite assumé cite la démonstration qui le porte
        if x.get('statut_ancre') == 'implicite au manuscrit' and '«' not in sa:
            ech(eid, 'R4bis implicite sans démonstration citée', sa[:70])

        # R5 — un verdict destructif exige que le voisinage ait été lu.
        # La preuve de lecture est la présence des voisins en chaîne ou en depend.
        v = str(x.get('verdict', '')) + ' ' + str(x.get('statut_ancre', ''))
        if any(t in v for t in VERDICTS_DESTRUCTIFS):
            voisins = set(x.get('depend', []) or [])
            voisins |= {c.get('origine', '') for c in x.get('chaine', [])}
            voisins |= {r.get('vers', '') for r in prop_de[eid].get('renvois', [])}
            amont = {n for n in voisins if re.match(r'^D\d', str(n))}
            if not amont:
                ech(eid, 'R5 verdict destructif sans voisinage instruit', x.get('verdict'))

        # R6 — aucune entrée ne tire son origine d'un champ dérivé d'une autre entrée
        for c in x.get('chaine', []):
            o = str(c.get('origine', ''))
            if re.search(r'\bbornes\b|\bcertitude\b|\bchiffre\b de\b', o):
                ech(eid, 'R6 origine tirée d’un champ dérivé', o[:70])

        # R7 — un composant reconstitué ne se présente pas comme relevé
        for c in x.get('chaine', []):
            if c.get('statut') not in ('relevé', 'reconstitué'):
                ech(eid, 'R7 statut de composant hors nomenclature', c.get('statut'))

        # R8 — un renvoi n'a pas de chaîne propre au-delà de son origine
        if str(x.get('origine', '')).startswith('renvoi') and len(x.get('chaine', [])) > 1:
            alerte(eid, 'R8 renvoi porteur d’une chaîne propre', len(x['chaine']))

        # R9 — une valeur de statut classeur ne se dit pas exacte contre une ancre
        if x.get('statut_ancre') == 'classeur' and 'ancre' in str(x.get('exact', '')).lower():
            alerte(eid, 'R9 valeur de classeur qualifiée d’ancre', x.get('exact')[:60])

        # R10 — un sens de plancher ou de plafond ne porte pas un exact unique
        if x.get('sens', '').startswith(('plancher', 'plafond')) and x.get('exact'):
            if not re.search(r'plancher|plafond|au moins|jusqu|contre|·', str(x['exact'])):
                alerte(eid, 'R10 borne présentée comme valeur unique', x['exact'][:60])

        # R20 — la nature est déclarée, dans la nomenclature
        if x.get('nature') not in NATURES:
            ech(eid, 'R20 nature hors nomenclature', x.get('nature'))

        # R21 — une illustration nomme son cas en première condition
        if x.get('nature') == 'illustration':
            cs = x.get('conditions') or []
            if not cs or not str(cs[0]).startswith('Cas :'):
                ech(eid, 'R21 illustration sans cas nommé', (cs[0] if cs else '')[:50])

        # R22 — une règle générale ne se restreint pas à un cas
        if x.get('nature') == 'règle générale':
            if any(str(c).startswith('Cas :') for c in x.get('conditions') or []):
                ech(eid, 'R22 règle générale restreinte à un cas', '')

        # R15 — toute condition littérale du texte est portée en clair
        txt = ' '.join(str(x.get(k, '')) for k in ('portee', 'sens', 'operation', 'base'))
        if re.search(MARQUEURS, txt, re.I) and not x.get('conditions'):
            ech(eid, 'R15 condition littérale non portée en clair', txt[:60])

        # R16 — une entrée de sens plancher ou plafond le dit dans ses conditions
        if x.get('sens', '').startswith(('plancher', 'plafond')):
            if not any(re.search(r'plancher|plafond|au moins|jusqu', str(c), re.I)
                       for c in x.get('conditions', [])):
                ech(eid, 'R16 borne non portée en condition', x.get('sens')[:50])

    # R17 — le lexique est présent, chaque terme est défini une fois et situé
    lex = d.get('lexique', [])
    if not lex:
        ech('lexique', 'R17 bloc lexique absent', '')
    termes = [t.get('terme') for t in lex]
    for t in lex:
        if termes.count(t.get('terme')) > 1:
            ech(t.get('terme'), 'R17 terme défini plusieurs fois', '')
        if t.get('verdict') not in VERDICTS_LEX:
            ech(t.get('terme'), 'R17 verdict lexical hors nomenclature', t.get('verdict'))
        if t.get('statut_ancre') == 'manuscrit' and '«' not in str(t.get('source_ancre', '')):
            ech(t.get('terme'), 'R17 terme du manuscrit sans citation', '')
        for e in t.get('emplois', []):
            if e not in idx:
                ech(t.get('terme'), 'R17 emploi vers une entrée inexistante', e)
        if t.get('verdict') in ('À QUALIFIER', 'À ARRÊTER') and not t.get('lacune'):
            ech(t.get('terme'), 'R17 terme non arrêté sans lacune écrite', '')

        # R19 — un terme à variantes porte la règle qui les autorise et les borne
        # R23 — un terme à illustrations les distingue de sa règle
        if t.get('illustrations') and 'illustration' not in str(t.get('regle', '')):
            ech(t.get('terme'), 'R23 illustrations non distinguées de la règle', '')

        if t.get('variantes') and not t.get('regle'):
            ech(t.get('terme'), 'R19 variantes admises sans règle écrite', ', '.join(t['variantes'])[:50])

    # R24 — une règle transversale absente du manuscrit ne se propage pas
    for rt in d.get('regles_transversales', []):
        if rt.get('statut_ancre') == 'absent des deux' and rt.get('verdict') != 'À ÉCRIRE AU MANUSCRIT':
            ech(rt.get('id'), 'R24 règle transversale sans ancre ni verdict d’attente', rt.get('verdict'))
        for n_ in rt.get('noeuds', []):
            if n_ not in idx:
                ech(rt.get('id'), 'R24 nœud inexistant', n_)
        if rt.get('statut_ancre') == 'implicite au manuscrit' and not rt.get('construction'):
            ech(rt.get('id'), 'R24 implicite sans construction écrite', '')

    # R25 — chaque complément normatif porte sa strate et se rattache à un nœud
    cn = d.get('complements_normatifs', {})
    strates_ok = set(cn.get('nomenclature_strates', {}))
    for m in cn.get('mecanismes', []):
        for n_ in m.get('noeuds_rattaches', []):
            if n_ not in props:
                ech(m.get('id'), 'R25 rattachement vers une proposition inexistante', n_)
        if not m.get('noeuds_rattaches'):
            ech(m.get('id'), 'R25 mécanisme sans nœud doctrinal', '')
        for e in m.get('effets', []):
            if e.get('strate_atteignable') not in strates_ok:
                ech(e.get('id'), 'R25 strate hors nomenclature', e.get('strate_atteignable'))
            if not e.get('siege_constitutionnel'):
                ech(e.get('id'), 'R25 effet sans siège constitutionnel', '')

    # R18 — une variante lexicale ne sert pas de terme principal ailleurs
    principaux = set(termes)
    for t in lex:
        for v in t.get('variantes', []):
            if v in principaux:
                alerte(t.get('terme'), 'R18 variante employée comme terme principal', v)

    # R11 — les identifiants sont uniques
    vus = {}
    for a in d['axes']:
        for lv in a['leviers']:
            for p in lv['propositions']:
                for x in p['parametres'] + p['effets']:
                    vus.setdefault(x['id'], 0)
                    vus[x['id']] += 1
    for k, n in vus.items():
        if n > 1:
            ech(k, 'R11 identifiant dupliqué', f'{n} occurrences')

    # R12 — tout renvoi pointe vers une proposition existante
    for pid, p in props.items():
        for r in p.get('renvois', []):
            if r.get('vers') not in cibles:
                ech(pid, 'R12 renvoi vers une cible inexistante', r.get('vers'))

    # R26 — un renvoi de sous-item porte la forme {vers, motif} et une cible
    # existante. R12 ne couvre que les renvois de proposition.
    for pid, p in props.items():
        for s in p.get('sous_items', []):
            for r in s.get('renvois', []):
                if not isinstance(r, dict) or set(r) != {'vers', 'motif'}:
                    ech(s['id'], 'R26 renvoi de sous-item non normalisé', str(r)[:60])
                elif r['vers'] not in cibles:
                    ech(s['id'], 'R26 renvoi de sous-item vers une cible inexistante',
                        r['vers'])

    # R13 — toute dépendance pointe vers une entrée existante
    for eid, x in idx.items():
        for dep in x.get('depend', []) or []:
            if dep not in idx:
                ech(eid, 'R13 dépendance vers une entrée inexistante', dep)

    # R14 — une entrée modifiée propage : ses dépendants portent une chaîne
    for eid, x in idx.items():
        if 'verdict' not in x:
            continue
        dependants = [k for k, y in idx.items() if eid in (y.get('depend') or [])]
        for dep in dependants:
            if 'verdict' in idx[dep] and not idx[dep].get('chaine'):
                alerte(dep, 'R14 dépendant sans chaîne', f'dépend de {eid}')

    # ------------------------------------------------------------------ sortie
    print(f'{len(idx)} entrées, {sum(1 for x in idx.values() if "verdict" in x)} peuplées')
    print(f'{len(ECHECS)} échec(s), {len(ALERTES)} alerte(s)\n')
    for eid, regle, detail in ECHECS:
        print(f'  ECHEC   {eid:<14} {regle:<48} {detail}')
    for eid, regle, detail in ALERTES:
        print(f'  ALERTE  {eid:<14} {regle:<48} {detail}')
    return 1 if ECHECS else 0


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'REF_doctrine_20260819_v10.json'
    sys.exit(controler(path))
