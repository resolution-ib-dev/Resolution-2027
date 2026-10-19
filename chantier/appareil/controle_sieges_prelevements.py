#!/usr/bin/env python3
"""Contrôle des sièges inscrits au tri des prélèvements, et du rapprochement
sur la liste IFRAP.

Inscrit le 20261016. Il rejoue chaque siège inscrit sans croire le
classeur : il rouvre la pièce qui fait foi et compare. Un siège qui ne
repasse pas ce contrôle n'est pas un siège.

Quatre règles, par statut inscrit à la colonne `statut_siege` :

  S1 — « relevé à l'annexe des ressources affectées PLF 2027 ».
       L'annexe se rouvre, le libellé se réapparie, et les références
       inscrites doivent être exactement celles de la colonne
       `reference_juridique`. Un libellé de ressource porte souvent
       PLUSIEURS lignes à l'annexe, donc plusieurs références : elles
       s'inscrivent jointes par « ; » et le contrôle compare les deux
       ensembles, non les deux chaînes. Comparer les chaînes a fait quatre
       faux au premier jeu, le 20261016. Un appariement par variante de
       libellé passe, et se DÉCLARE : il ne se tait pas.
  S2 — « relevé au dépôt de droit, vérifié article par article ».
       L'identifiant LEGIARTI porté au `fondement` se rouvre par le dépôt.
       L'article doit exister et s'appliquer au jour du contrôle.
  S3 — « relevé par renvoi exprès, vérifié ».
       L'identifiant porté au `fondement` se rouvre, et son texte doit
       nommer le texte cité au `siege_article`. Le renvoi fait preuve de
       l'adresse, le verbatim du siège reste hors dépôt.
  S4 — « siège abrogé, relevé au dépôt de droit ».
       Les articles cités doivent être portés par le dépôt et n'avoir
       AUCUNE version applicable au jour du contrôle. Une abrogation qui
       ne se relève pas est une affirmation.
  S5 — « siège abrogé dans l'article en vigueur, relevé au dépôt de droit ».
       Le cas où l'article qui PORTAIT le prélèvement s'applique toujours
       et marque « (Abrogé) » la subdivision qui l'instituait — ainsi de
       l'article L. 332-6-1 du code de l'urbanisme, dont le 2° b) portait
       la participation pour non-réalisation d'aires de stationnement.
       L'article doit s'appliquer ET son texte porter cette mention.

Les statuts antérieurs au fil du 20261016 — « confirmé », « relevé par le
fil », « nommé non porté au dépôt », « non établi » — ne sont pas du
ressort des règles S1 à S5 : elles les comptent et les laissent. La règle
S6, ci-dessous, les atteint néanmoins par la colonne `nature_ligne`.

**La règle S6, l'exigence de siège, inscrite le 20261019.** Un siège ne
s'exige QUE des rangs de `nature_ligne = imposition`, et il s'en exige de
tous : un rang d'imposition sans `siege_article` est un ÉCHEC, et le
classeur ne se verse pas. Les deux autres valeurs de `nature_ligne` en
sont hors : un `agrégat` est une ligne de nomenclature budgétaire qui se
résout en ses composantes et ne porte pas de siège par construction, et
une `ressource propre de l'Union` n'a pas de siège en droit national.

Deux statuts déclarent l'absence de siège par construction et valent
dispense, parce que l'absence y est le relevé lui-même et non son
manque :

  - « création du PLF — aucun article en vigueur au millésime du
    relevé » : le siège naîtra à la promulgation ;
  - « siège réglementaire — hors du champ du relevé législatif » : le
    siège existe et porte un R. Il S'INSCRIT quand il est relevé ; tant
    qu'il ne l'est pas, le rang passe en SIGNAL et non en échec, pour
    qu'un fil ultérieur le relève.

Tout autre statut sans siège — « non établi » au premier chef — échoue.
Un rang mesuré vide reste donc visible et bloquant : c'est ce qui
distingue une qualification non tranchée d'une qualification rendue.

**Le rapprochement IFRAP, règle R.** Les 420 libellés distincts de
`referentiels/prelevements_ifrap.tsv` doivent tous être couverts par la colonne
`libelle_ifrap` de `referentiels/prelevements_forces_20260930.tsv`, et toute
valeur déclarée doit exister dans la liste. **Cette colonne porte des cellules à
plusieurs valeurs, jointes par « ; »** — un rang du tri peut absorber plusieurs
lignes de la liste : versement mobilité et ses deux additionnels, redevances de
l'eau, taxes spéciales d'équipement. Une jointure qui n'éclate pas la cellule
rend 65 lignes orphelines et 24 déclarations introuvables, toutes fausses ; c'est
arrivé le 20261016. Les rangs qui ne viennent pas de la liste portent leur
provenance en colonne `origine` — « état A » ou « annexe » — et sont comptés à
part, non en défaut.

Un échec est bloquant. Un relevé par variante est un signal.

Pièces qui font foi :
  referentiels/annexe_ressources_affectees_2027.tsv — V&M 2027, tome I, annexe 2
  le dépôt de droit, millésime LEGI porté par `droit.fraicheur`

Usage : python3 appareil/controle_sieges_prelevements.py [classeur.tsv]
"""
import csv, re, sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / 'appareil'))
# `chasse_siege` résout le dépôt de droit dans ses deux dispositions — sous
# `depot/` en atelier, un cran au-dessus quand le chantier est sous `chantier/`.
# On prend son `droit` plutôt que de refaire la résolution ici.
from chasse_siege import par_annexe, norm, corpus, droit, VOIES_DROIT

DEFAUT = RACINE / 'referentiels/sort_prelevements_20261015.tsv'

S_ANNEXE = 'relevé à l’annexe des ressources affectées PLF 2027'
S_DEPOT = 'relevé au dépôt de droit, vérifié article par article'
S_RENVOI = 'relevé par renvoi exprès, vérifié'
S_ABROGE = 'siège abrogé, relevé au dépôt de droit'
S_ABROGE_IN = 'siège abrogé dans l’article en vigueur, relevé au dépôt de droit'

# Règle S6 — l'exigence de siège (20261019).
NATURE_AVEC_SIEGE = 'imposition'
S_PLF_A_NAITRE = 'création du PLF — aucun article en vigueur au millésime du relevé'
S_REGLEMENTAIRE = 'siège réglementaire — hors du champ du relevé législatif'
DISPENSES_SIEGE = (S_PLF_A_NAITRE, S_REGLEMENTAIRE)

RE_LEGI = re.compile(r'LEGIARTI\d{12}')
RE_NUM = re.compile(r'art(?:icles?)?\.?\s*((?:[LRD]\.?\s*)?[\d]+(?:[\- ]\d+)*(?:\s+(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies|terdecies|quaterdecies|quindecies|sexdecies|septdecies|octodecies|novodecies|vicies|unvicies|duovicies|tervicies|quatervicies|quinvicies|sexvicies|septvicies|octovicies|novovicies|tricies|untricies|duotricies|tertricies|[A-Z]{1,3})\b)*)', re.I)


def par_id(ident):
    for a in corpus():
        if a['id'] == ident:
            return a
    return None


def existe_mais_inapplicable(ident):
    """Vrai si le dépôt porte cet identifiant sans version applicable ce jour."""
    import gzip, json
    data = Path(droit.__file__).resolve().parent / 'data'  # noqa: suit la voie résolue
    for f in data.glob('*.jsonl.gz'):
        for ligne in gzip.open(f, 'rt', encoding='utf-8'):
            a = json.loads(ligne)
            if a['id'] == ident:
                return not droit.applicable(a)
    return None


def lire(chemin):
    with open(chemin, encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def controler(chemin):
    lignes = lire(chemin)
    echecs, signaux, comptes = [], [], {}
    for i, r in enumerate(lignes, 2):
        st = r['statut_siege'].strip()
        comptes[st] = comptes.get(st, 0) + 1

        # S6 — un siège s'exige de tout rang d'imposition, et de lui seul.
        nature = (r.get('nature_ligne') or '').strip()
        if nature == NATURE_AVEC_SIEGE and not r['siege_article'].strip():
            if st == S_REGLEMENTAIRE:
                signaux.append((i, r['libelle'],
                                'S6 : siège réglementaire déclaré, non relevé — à relever'))
            elif st != S_PLF_A_NAITRE:
                echecs.append((i, r['libelle'],
                               f'S6 : imposition sans siège (statut « {st} »)'))

        if st not in (S_ANNEXE, S_DEPOT, S_RENVOI, S_ABROGE, S_ABROGE_IN):
            continue
        lib, siege, fond = r['libelle'], r['siege_article'].strip(), r['fondement']
        ident = RE_LEGI.search(fond)

        if st == S_ANNEXE:
            trouve = par_annexe(lib)
            if not trouve:
                echecs.append((i, lib, 'S1 : le libellé ne se réapparie plus à l’annexe'))
                continue
            refs, mode = trouve
            attendu = {norm(x) for x in refs}
            inscrit = {norm(x) for x in siege.split(' ; ') if norm(x)}
            if inscrit != attendu:
                manque = sorted(attendu - inscrit)
                surplus = sorted(inscrit - attendu)
                detail = (f'manque {len(manque)}' if manque else '') + \
                         (f' en trop {len(surplus)}' if surplus else '')
                echecs.append((i, lib, f'S1 : les références inscrites ne sont pas celles de l’annexe ({detail.strip()})'))
            elif mode == 'variante':
                signaux.append((i, lib, 'S1 : apparié par variante de libellé'))
            continue

        if not ident:
            echecs.append((i, lib, f'{st[:12]} : aucun LEGIARTI au fondement'))
            continue
        ident = ident.group()

        if st in (S_DEPOT, S_RENVOI):
            a = par_id(ident)
            if a is None:
                echecs.append((i, lib, f'S2/S3 : {ident} sans version applicable au dépôt'))
                continue
            if st == S_RENVOI:
                m = re.search(r'(loi|ordonnance|décret)\s+n°\s*\d{2,4}-\d+', siege, re.I)
                if not m:
                    echecs.append((i, lib, 'S3 : le siège ne nomme aucun texte non codifié'))
                elif norm(m.group()) not in norm(a['texte']):
                    echecs.append((i, lib, f'S3 : {ident} ne nomme pas {m.group()}'))
            continue

        if st == S_ABROGE_IN:
            a = par_id(ident)
            if a is None:
                echecs.append((i, lib, f'S5 : {ident} ne s’applique pas — ce n’est pas le cas S5'))
            elif '(Abrogé)' not in a['texte'] and '(Abrogé' not in a['texte']:
                echecs.append((i, lib, f'S5 : {ident} ne porte aucune mention « (Abrogé) »'))
            continue

        if st == S_ABROGE:
            inapplicable = existe_mais_inapplicable(ident)
            if inapplicable is None:
                echecs.append((i, lib, f'S4 : {ident} absent du dépôt'))
            elif inapplicable is False:
                echecs.append((i, lib, f'S4 : {ident} s’applique encore — l’abrogation ne se relève pas'))
    return lignes, comptes, echecs, signaux


def controler_ifrap():
    """Règle R — le rapprochement du tri sur la liste IFRAP."""
    base = RACINE / 'referentiels'
    liste = base / 'prelevements_ifrap.tsv'
    forces = base / 'prelevements_forces_20260930.tsv'
    if not liste.exists() or not forces.exists():
        return None
    cles = {norm(r['libelle']) for r in lire(liste)}
    rangs = lire(forces)
    declare, sans = set(), 0
    for r in rangs:
        v = (r.get('libelle_ifrap') or '').strip()
        if not v:
            sans += 1
            continue
        for part in v.split(' ; '):
            if part.strip():
                declare.add(norm(part))
    return {
        'cles': len(cles), 'rangs': len(rangs),
        'couvertes': len(cles & declare),
        'non_couvertes': sorted(cles - declare),
        'orphelines': sorted(declare - cles),
        'sans_libelle': sans,
    }


def main(argv):
    chemin = Path(argv[1]) if len(argv) > 1 else DEFAUT
    mil, age, perime = droit.fraicheur()
    lignes, comptes, echecs, signaux = controler(chemin)

    print(f'{chemin.name} — {len(lignes)} lignes · millésime LEGI {mil} ({age} j)')
    for st, n in sorted(comptes.items(), key=lambda x: -x[1]):
        marque = '  <' if st in (S_ANNEXE, S_DEPOT, S_RENVOI, S_ABROGE, S_ABROGE_IN) else ''
        print(f'  {n:>4}  {st}{marque}')
    couverts = sum(comptes.get(s, 0) for s in (S_ANNEXE, S_DEPOT, S_RENVOI, S_ABROGE, S_ABROGE_IN))
    print(f'\n  {couverts} sièges sous contrôle.')
    impositions = sum(1 for r in lignes if (r.get('nature_ligne') or '').strip() == NATURE_AVEC_SIEGE)
    avec = sum(1 for r in lignes
               if (r.get('nature_ligne') or '').strip() == NATURE_AVEC_SIEGE and r['siege_article'].strip())
    print(f'  S6 : {avec}/{impositions} rangs d’imposition portent un siège.')

    for i, lib, motif in signaux:
        print(f'  SIGNAL l.{i} — {lib[:60]}\n          {motif}')
    r = controler_ifrap()
    if r is None:
        print('\n  Rapprochement IFRAP : liste ou tri absent — non contrôlé.')
    else:
        print(f"\n  Rapprochement IFRAP : {r['couvertes']}/{r['cles']} libellés couverts, "
              f"{r['sans_libelle']} rangs d'une autre origine sur {r['rangs']}.")
        for k in r['non_couvertes']:
            echecs.append((0, k[:60], 'R : ligne de la liste IFRAP sans rang'))
        for k in r['orphelines']:
            echecs.append((0, k[:60], 'R : libellé déclaré au tri, absent de la liste IFRAP'))

    if echecs:
        print()
        for i, lib, motif in echecs:
            print(f'  ÉCHEC l.{i} — {lib[:60]}\n         {motif}')
        print(f'\n  {len(echecs)} échec(s). Le classeur ne se verse pas.')
        return 1
    print(f'  0 échec, {len(signaux)} signal/signaux.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
