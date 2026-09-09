# -*- coding: utf-8 -*-
"""Le partage calibrage / épreuve du banc de la rédaction modificative.

**Écrit le 20260903, en application d'A-330**, et écrit *avant* d'avoir regardé
un seul couple. Celui qui choisit son lot de calibrage choisit ses cas faciles,
et cela ne se voit pas après coup : la règle de sélection est donc du code, elle
se rejoue, et le fil qui écrira `disposition-cible` ne la choisit pas.

**La population.** Les couples du **texte déposé de la loi de finances**, relevés
sur `referentiels/redaction_plf.json` — la part versée au coffre. Le banc est
ainsi atteignable depuis le coffre seul, ce qui est la condition qu'A-342 pose à
tout dérivé. La loi de financement n'entre pas à ce banc : son socle n'est pas
versé, faute de jauge, et un banc qu'on ne peut pas rejouer n'est pas un banc.

**L'unité est le couple (alinéa, adresse ouverte)** — une disposition
modificative écrite par l'administration, et l'adresse qu'elle vise. C'est ce
que la colonne « disposition » du trois colonnes porte déjà à l'octet.

---

## La règle de sélection, et elle précède le tirage

1. **Éligibilité.** Un couple est éligible au calibrage s'il porte **une
   opération et une seule** de la liste fermée ci-dessous, et **une adresse et
   une seule** à son alinéa. Un alinéa qui vise deux articles, ou qui cumule
   deux opérations, est un cas d'épreuve : le calibrage sert à apprendre une
   forme, pas à démêler un cas composite.

2. **Les strates, et leur ordre est celui de notre usage** (A-329, A-329
   corrigeant A-324) : `abrogation_article`, `abrogation_subdivision`,
   `remplacement_membre_de_phrase`. Une quatrième strate s'ajoute : **la plus
   peuplée des opérations restantes**, mesurée sur la population et non choisie.
   Un rang mesuré n'est pas une préférence.

3. **Un couple par strate, quatre au total.** Le tirage est déterministe et
   vérifiable : dans chaque strate, les couples sont ordonnés par (numéro
   d'article du texte déposé, numéro d'alinéa, adresse) et **le premier est
   retenu**. Pas de graine pseudo-aléatoire — une graine est un choix caché,
   quand le premier de l'ordre du texte se recompte par quiconque.

4. **Le lot d'épreuve est le complément exact**, et il est scellé : toute la
   population moins les quatre couples de calibrage. Il sort du calibrage comme
   un cas contaminé sort d'un taux.

5. **Une strate vide ne se remplace pas.** Si l'une des trois premières
   opérations ne rend aucun couple éligible, la strate sort vide et le lot
   compte trois cas. Substituer une opération voisine ferait passer un choix
   pour un relevé.

---

## Les opérations, en liste fermée

Elles se lisent sur la **cible** de l'alinéa — ce qui précède la formule
modificative, hors guillemets. La liste dérive de `FORMULES_MODIFICATIVES` de
`socle_plf_texte.py` et n'en invente aucune : une formule absente laisse le
couple en `operation_indeterminee`, qui n'est pas une strate.

Usage : python3 partage_calibrage.py <redaction_plf.json> <lots_epreuve.json>
        --releve  pour n'afficher que la répartition, sans écrire
"""
import json
import re
import sys

# Les têtes de cible qui désignent un article entier. Tout le reste — un
# ordinal, un alinéa, une phrase, un membre — désigne une subdivision.
CIBLE_ARTICLE = re.compile(
    r'^(?:l[’\']articles?|les\s+articles?)\b', re.I)

# Ce qui, en tête de cible, nomme une subdivision de l'article.
CIBLE_SUBDIVISION = re.compile(
    r'^(?:le|la|les|l[’\'])\s*'
    r'(?:\d+\s*°|[IVXLC]+\b|[a-z]\s+(?:du|de)\b|premier|second[e]?|'
    r'derni[èe]re?|avant-dernier|alin[ée]a|phrase|mots?|membre|tableau|'
    r'colonne|ligne|paragraphe|chapitre|section|titre|livre|partie)',
    re.I)

# Les marqueurs d'énumération légistique en tête d'alinéa, à retirer avant de
# lire la cible. Repris de `socle_plf_texte.py`, jamais réécrits d'intuition.
PREFIXE_ENUM = re.compile(
    r'^\s*(?:[IVXLC]+|[A-Z]|[a-z]|\d+)\s*(?:°|\)|\.)\s*(?:[–—-]\s*)?')

# Les opérations, en liste fermée. L'ordre compte : la première qui mord gagne,
# et les formules les plus spécifiques passent d'abord.
OPERATIONS = (
    ('abrogation', (
        'est abrogé', 'est abrogée', 'sont abrogés', 'sont abrogées')),
    ('suppression', (
        'est supprimé', 'est supprimée', 'sont supprimés',
        'sont supprimées')),
    ('remplacement', (
        'est remplacé', 'est remplacée', 'sont remplacés',
        'sont remplacées')),
    ('redaction_nouvelle', (
        'est ainsi rédigé', 'est ainsi rédigée', 'sont ainsi rédigés',
        'sont ainsi rédigées')),
    ('completement', (
        'est complété', 'est complétée', 'sont complétés',
        'sont complétées')),
    ('insertion', (
        'il est inséré', 'il est ajouté', 'sont insérés', 'sont insérées',
        'est inséré', 'est insérée', 'est ajouté', 'est ajoutée')),
    ('creation', ('est créé', 'est créée', 'sont créés')),
    ('retablissement', ('est ainsi rétabli', 'est ainsi rétablie')),
    ('chapeau', (
        'est ainsi modifié', 'est ainsi modifiée', 'sont ainsi modifiés',
        'sont ainsi modifiées')),
)

# L'ordre des strates, arrêté par A-329 pour les trois premières. La quatrième
# se mesure.
STRATES_ARRETEES = ('abrogation_article', 'abrogation_subdivision',
                    'remplacement_membre_de_phrase')

CLE_LOT = 'plf_2026_texte_depose'


def hors_guillemets(txt):
    """Le texte hors des guillemets français : ce qu'on cite n'est pas ce
    qu'on modifie. Un guillemet ouvrant non refermé masque jusqu'à la fin."""
    out, dedans = [], False
    for c in txt:
        if c == '«':
            dedans = True
        elif c == '»':
            dedans = False
        elif not dedans:
            out.append(c)
    return ''.join(out)


def operation(txt):
    """L'opération de l'alinéa, ou None. La première formule qui mord."""
    nu = hors_guillemets(txt)
    trouvees = []
    for nom, formules in OPERATIONS:
        for f in formules:
            if f in nu:
                trouvees.append((nu.find(f), nom))
                break
    if not trouvees:
        return None, 0
    trouvees.sort()
    # Le nombre d'opérations distinctes dit si le couple est composite.
    return trouvees[0][1], len({n for _, n in trouvees})


def cible(txt):
    """La portée de l'opération : `article` ou `subdivision`."""
    nu = hors_guillemets(txt).strip()
    while True:
        red = PREFIXE_ENUM.sub('', nu, count=1)
        if red == nu:
            break
        nu = red.strip()
    if CIBLE_ARTICLE.match(nu):
        return 'article'
    if CIBLE_SUBDIVISION.match(nu):
        return 'subdivision'
    return 'indetermine'


def strate(op, portee):
    if op == 'abrogation':
        return ('abrogation_article' if portee == 'article'
                else 'abrogation_subdivision' if portee == 'subdivision'
                else None)
    if op == 'suppression':
        return 'abrogation_subdivision' if portee == 'subdivision' else None
    if op == 'remplacement':
        return 'remplacement_membre_de_phrase'
    if op in ('redaction_nouvelle', 'completement', 'insertion', 'creation',
              'retablissement'):
        return op
    return None


def _cle_couple(art, al, adresse):
    return f'{art}#{al}#{adresse}'


def population(red):
    """Les couples (alinéa, adresse ouverte), avec leur strate."""
    couples = []
    for a in red['articles']:
        textes = {al['numero']: al['texte'] for al in a['alineas']}
        par_alinea = {}
        for ref in a['references']:
            if ref['statut'] != 'modifie':
                continue
            par_alinea.setdefault(ref['alinea'], []).append(ref)
        for num, refs in sorted(par_alinea.items()):
            txt = textes.get(num)
            if txt is None:
                continue
            op, distinctes = operation(txt)
            portee = cible(txt)
            st = strate(op, portee) if op else None
            adresses = sorted(
                {(r['texte'] or 'aucun texte nommé', r['brut']) for r in refs})
            eligible = (op is not None and distinctes == 1
                        and len(adresses) == 1 and st is not None)
            couples.append({
                'cle': _cle_couple(a['numero'], num,
                                   adresses[0][1] if len(adresses) == 1
                                   else f'{len(adresses)} adresses'),
                'article_texte_depose': a['numero'],
                'alinea': num,
                'page': a['page'],
                'adresses': len(adresses),
                'operation': op or 'operation_indeterminee',
                'operations_distinctes': distinctes,
                'portee': portee,
                'strate': st,
                'eligible_calibrage': eligible,
                '_tri': (_num_tri(a['numero']), num,
                         adresses[0][1] if adresses else ''),
            })
    return couples


def _num_tri(numero):
    """« liminaire » précède 1. Un numéro d'article n'est pas un entier."""
    return (0, 0) if numero == 'liminaire' else (1, int(numero))


def partager(couples):
    par_strate = {}
    for c in couples:
        if c['strate']:
            par_strate.setdefault(c['strate'], []).append(c)
    eligibles = {s: sorted([c for c in v if c['eligible_calibrage']],
                           key=lambda c: c['_tri'])
                 for s, v in par_strate.items()}
    restantes = [s for s in eligibles if s not in STRATES_ARRETEES]
    # La quatrième strate se mesure : la plus peuplée des restantes, l'ordre
    # alphabétique tranchant une égalité pour que le tirage reste rejouable.
    restantes.sort(key=lambda s: (-len(eligibles[s]), s))
    quatrieme = [s for s in restantes if eligibles[s]][:1]
    strates = list(STRATES_ARRETEES) + quatrieme
    calibrage, vides = [], []
    for s in strates:
        lot = eligibles.get(s) or []
        if not lot:
            vides.append(s)
            continue
        calibrage.append(dict(lot[0], strate=s))
    cles = {c['cle'] for c in calibrage}
    epreuve = [c for c in couples if c['cle'] not in cles]
    return strates, calibrage, epreuve, vides, par_strate, eligibles


def main(src_red, src_lots, ecrire=True):
    red = json.load(open(src_red, encoding='utf-8'))
    couples = population(red)
    strates, calibrage, epreuve, vides, par_strate, eligibles = \
        partager(couples)

    print(f'population — {len(couples)} couple(s) (alinéa, adresse) sur '
          f'{red["_revision"]["extraction"]["piece_declaree"]}')
    print(f'  éligibles au calibrage : '
          f'{sum(1 for c in couples if c["eligible_calibrage"])}')
    for s in sorted(par_strate, key=lambda s: (-len(par_strate[s]), s)):
        marque = ' ← strate' if s in strates else ''
        print(f'    {s:<32} {len(par_strate[s]):>4} couple(s), '
              f'{len(eligibles.get(s) or []):>3} éligible(s){marque}')
    sans = sum(1 for c in couples if not c['strate'])
    print(f'    {"hors strate":<32} {sans:>4} couple(s)')
    print(f'\nlot de calibrage — {len(calibrage)} couple(s), '
          f'lot d\'épreuve scellé — {len(epreuve)} couple(s)')
    for c in calibrage:
        print(f'    {c["strate"]:<32} art. {c["article_texte_depose"]} '
              f'al. {c["alinea"]} — {c["cle"]}')
    for s in vides:
        print(f'    {s:<32} STRATE VIDE, non remplacée')

    if not ecrire:
        return 0

    lots = json.load(open(src_lots, encoding='utf-8'))
    entree = {
        'cle': CLE_LOT,
        'vehicule': 'plf',
        'intitule': 'Couples (alinéa, adresse ouverte) du texte déposé de la '
                    'loi de finances — banc de la rédaction modificative',
        'source': 'referentiels/redaction_plf.json, part versée du socle du '
                  'PLF 2026 n° 1906, empreinte de pièce '
                  + red['_revision']['piece']['sha256'],
        'entree_par': 'coffre',
        'unite': 'couple (alinéa, adresse ouverte)',
        'extrait_par': 'appareil/partage_calibrage.py',
        'population': {
            'couples': len(couples),
            'eligibles_calibrage': sum(1 for c in couples
                                       if c['eligible_calibrage']),
            'par_strate': {s: len(v) for s, v in sorted(par_strate.items())},
            'hors_strate': sum(1 for c in couples if not c['strate']),
        },
        'regle_de_selection': {
            '_ecrite_avant_le_tirage': True,
            'autorite': 'A-330',
            'eligibilite': 'Une opération et une seule, une adresse et une '
                           'seule à l\'alinéa. Un alinéa composite est un cas '
                           "d'épreuve, jamais de calibrage.",
            'strates_arretees': list(STRATES_ARRETEES),
            'quatrieme_strate': 'la plus peuplée des opérations restantes, '
                                'mesurée sur la population, égalité tranchée '
                                'par ordre alphabétique',
            'tirage': 'le premier couple de chaque strate dans l\'ordre '
                      '(numéro d\'article du texte déposé, numéro d\'alinéa, '
                      'adresse). Aucune graine pseudo-aléatoire.',
            'strate_vide': 'sort vide et ne se remplace pas',
            'operations': {nom: list(f) for nom, f in OPERATIONS},
        },
        'strates_retenues': strates,
        'strates_vides': vides,
        'lot_calibrage': [{k: v for k, v in c.items() if k != '_tri'}
                          for c in calibrage],
        'lot_epreuve': {
            '_scelle': True,
            'couples': len(epreuve),
            '_regle': "Le complément exact de la population moins le lot de "
                      "calibrage. Il ne s'énumère pas ici : le fil qui écrit "
                      "la skill ne doit pas en prendre connaissance. Il se "
                      "recalcule par `partage_calibrage.py` sur la part "
                      "versée du socle, à l'identique.",
            'par_strate': {
                s: len([c for c in epreuve if c['strate'] == s])
                for s in sorted(par_strate)},
        },
        'etapes': {
            'disposition': {
                'population_notee': len(epreuve),
                'dimension': 'correspondance',
                'mesures': [],
                'note': "Rien n'est joué : la skill n'existe pas. La notation "
                        "se fait en correspondance — même article visé, même "
                        "opération, même portée — jamais en égalité de "
                        "rédaction. Le lot de calibrage sort du compte.",
            },
        },
    }
    lots['lots'] = [l for l in lots['lots'] if l['cle'] != CLE_LOT]
    lots['lots'].append(entree)
    with open(src_lots, 'w', encoding='utf-8', newline='') as f:
        json.dump(lots, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print(f'\n{src_lots} — lot « {CLE_LOT} » inscrit')
    return 0


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    sys.exit(main(args[0], args[1], '--releve' not in sys.argv))
