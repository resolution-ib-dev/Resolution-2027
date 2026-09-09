# -*- coding: utf-8 -*-
"""Dépliage des fourchettes d'articles du texte déposé.

Cinq lignes de la table des articles ouverts du PLF visent une **plage** et non
un article : « L. 314-13 à L. 314-18 ». La table les compte sur leur **borne
basse** seulement, et le champ `fourchette` les marque à 1. Conséquence : une
mesure qui vise un article intérieur à la plage — L. 314-15, par exemple —
passe pour fermée à tort, et l'amendement part au mauvais endroit.

**Les articles qui existent dans l'intervalle ne se devinent pas.** Ils se
relèvent sur le code, à sa source : le dépôt de droit, qui rend le verbatim
avec identifiant `LEGIARTI` et date de version, relevé sur la base LEGI. Un
code absent du dépôt, un article absent du code, un dépôt périmé : la plage se
déclare **non dépliée** et le manque se dit. C'est un résultat acceptable ;
inventer un numéro d'article n'en est pas un (A-94).

## L'ordre des numéros d'article, et pourquoi il se pose

Un numéro d'article n'est pas un nombre : « L. 421-79-1 » suit « L. 421-79 » et
précède « L. 421-79-2 », et la plage `L. 421-77 à L. 421-79-1` s'arrête donc à
un article suffixé. On ne peut ni comparer des chaînes — « L421-9 » passerait
après « L421-79 » — ni comparer un entier unique.

La clé est le **découpage du numéro en suites de chiffres et de lettres**, dans
l'ordre de lecture : `L421-79-1` donne `(L, 421, 79, 1)`. Un tuple plus court
est un préfixe et vaut donc moins : `(L, 421, 79) < (L, 421, 79, 1)`, ce qui est
l'ordre du code. Une lettre en queue — « L. 314-13 A » — se range après les
chiffres du même rang. L'appartenance est alors l'encadrement au sens de cet
ordre, borne basse et borne haute comprises.

**Ce que le module ne fait pas** : il ne remonte pas les plages au socle et ne
réécrit pas la table des articles ouverts. Il rend le relevé, à charge du fil
qui joint de le consommer.

Usage : python3 plages_articles.py <depot_droit> <sortie.json> <sortie.txt>
                                   <ouverts.tsv> [ouverts.tsv ...]
"""
import json
import os
import re
import sys

# Le numéro d'article, découpé en suites homogènes. Les points et les espaces
# ne portent rien : « L. 314-13 » et « L314-13 » sont le même article.
MORCEAU = re.compile(r'\d+|[A-Za-z]+')


def cle(num):
    """La clé d'ordre d'un numéro d'article.

    Chaque morceau sort en triplet, pour que les trois familles se comparent
    sans jamais confronter un entier à une chaîne : un chiffre donne
    `(0, n, '')`, une lettre `(1, 0, 'X')`. Un chiffre passe donc avant une
    lettre de même rang — « L. 421-79-1 » avant « L. 421-79 A » —, et c'est une
    convention déclarée, non une propriété du code.
    """
    out = []
    for m in MORCEAU.findall(num.replace('.', '').replace(' ', '').upper()):
        out.append((0, int(m), '') if m.isdigit() else (1, 0, m))
    return tuple(out)


def bornes(libelle):
    """(basse, haute) d'un libellé de fourchette, ou None si ce n'en est pas."""
    morceaux = re.split(r'\s+à\s+', libelle)
    if len(morceaux) != 2:
        return None
    return morceaux[0].strip(), morceaux[1].strip()


def lire_table(chemin):
    """Les lignes d'une table d'articles ouverts, en-têtes de commentaire ôtés."""
    lignes = []
    with open(chemin, encoding='utf-8') as f:
        for l in f:
            if l.startswith('#') or not l.strip():
                continue
            champs = l.rstrip('\n').split('\t')
            if len(champs) < 4:
                continue
            lignes.append(dict(texte=champs[0], article=champs[1],
                               subdivision=champs[2], fourchette=champs[3]))
    return lignes


def code_du_depot(depot, nom_texte):
    """La clé courte du dépôt de droit pour un nom de texte, ou None."""
    cfg = json.load(open(os.path.join(depot, 'codes.json'),
                        encoding='utf-8'))['codes']
    for c in cfg:
        if c['cle'] == nom_texte:
            return c['court']
    return None


def deplier(depot, nom_texte, libelle, droit):
    """Les articles que le code porte réellement dans l'intervalle.

    Rend un dict portant la plage, ses bornes, les articles relevés avec leur
    identifiant et leur date de version, et le motif quand elle ne se déplie
    pas. **Aucun numéro n'est fabriqué** : tout ce qui sort a été lu au dépôt.
    """
    b = bornes(libelle)
    resultat = dict(texte=nom_texte, plage=libelle,
                    borne_basse=b[0] if b else None,
                    borne_haute=b[1] if b else None,
                    articles=[], deplie=False, motif=None)
    if b is None:
        resultat['motif'] = 'libellé non reconnu comme une fourchette'
        return resultat
    court = code_du_depot(depot, nom_texte)
    if court is None:
        resultat['motif'] = (f'« {nom_texte} » n’est pas au dépôt de droit : '
                             'plage non dépliée, manque déclaré')
        return resultat
    basse, haute = cle(b[0]), cle(b[1])
    if not basse or not haute or basse[0] != haute[0]:
        resultat['motif'] = ('les deux bornes ne partagent pas leur tête : '
                             'l’intervalle n’est pas défini')
        return resultat
    index = droit.charger(court)
    vus = {}
    for arts in index.values():
        for a in arts:
            if not droit.applicable(a):
                continue
            k = cle(a['num'])
            if basse <= k <= haute:
                vus[k] = a
    resultat['articles'] = [
        dict(article=vus[k]['num'], id=vus[k]['id'],
             version=vus[k]['date_debut'], etat=vus[k]['etat'],
             section=vus[k].get('section', ''))
        for k in sorted(vus)]
    # Une plage dont on ne retrouve pas ses propres bornes n'est pas dépliée :
    # ou le dépôt ne porte pas le bon millésime, ou la borne a été abrogée. Le
    # dire vaut mieux que rendre un intervalle amputé sans le signaler.
    presents = {cle(x['article']) for x in resultat['articles']}
    manquantes = [n for n, k in ((b[0], basse), (b[1], haute))
                  if k not in presents]
    if manquantes:
        resultat['motif'] = ('borne(s) introuvable(s) au dépôt : '
                             + ', '.join(manquantes)
                             + ' — plage non dépliée, manque déclaré')
        return resultat
    resultat['deplie'] = True
    return resultat


def main(depot, dst_json, dst_txt, *tables):
    if not tables:
        raise SystemExit(__doc__)
    sys.path.insert(0, depot)
    import droit                                    # noqa: E402
    millesime, age, perime = droit.fraicheur()
    if perime:
        raise SystemExit(
            f'le dépôt de droit est au millésime {millesime}, vieux de '
            f'{age} jours. Un extrait de plus de 45 jours se déclare périmé : '
            'la génération s’arrête plutôt que de déplier sur du droit ancien.')

    plages, source = [], []
    for t in tables:
        source.append(os.path.basename(t))
        for l in lire_table(t):
            if l['fourchette'] != '1':
                continue
            plages.append(deplier(depot, l['texte'], l['article'], droit))

    deplies = [p for p in plages if p['deplie']]
    articles = sum(len(p['articles']) for p in deplies)
    interieurs = articles - 2 * len(deplies)

    obj = dict(
        _revision=dict(
            role='dépliage des fourchettes d’articles du texte déposé',
            regle=('Une entrée par plage. Les articles sont relevés sur le '
                   'code à sa source, avec identifiant LEGIARTI et date de '
                   'version. Une plage qui ne se déplie pas se déclare non '
                   'dépliée et son manque se dit : aucun numéro n’est '
                   'fabriqué (A-94).'),
            tables=source,
            depot_droit=dict(millesime=millesime, age_jours=age),
            comptes=dict(plages=len(plages), deplies=len(deplies),
                         articles=articles, interieurs=interieurs),
        ),
        plages=plages,
    )
    os.makedirs(os.path.dirname(dst_json) or '.', exist_ok=True)
    with open(dst_json, 'w', encoding='utf-8', newline='') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')

    lignes = ['# FOURCHETTES D’ARTICLES DÉPLIÉES — texte déposé',
              f'# tables lues : {", ".join(source)}',
              f'# dépôt de droit : base LEGI, millésime {millesime} '
              f'({age} j)',
              f'# {len(plages)} plage(s), {len(deplies)} dépliée(s), '
              f'{articles} article(s) relevé(s), dont {interieurs} '
              f'intérieur(s) que la table comptait fermé(s)', '']
    for p in plages:
        lignes.append(f'{p["texte"]} — {p["plage"]}')
        if not p['deplie']:
            lignes.append(f'    NON DÉPLIÉE — {p["motif"]}')
        for a in p['articles']:
            lignes.append(f'    {a["article"]:<16} {a["id"]}  '
                          f'version {a["version"]}  {a["etat"]}')
        if p['articles']:
            lignes.append(f'    section : {p["articles"][0]["section"]}')
        lignes.append('')
    os.makedirs(os.path.dirname(dst_txt) or '.', exist_ok=True)
    with open(dst_txt, 'w', encoding='utf-8', newline='') as f:
        f.write('\n'.join(lignes))

    print(f'{len(plages)} plage(s) — {len(deplies)} dépliée(s), '
          f'{len(plages) - len(deplies)} manque(s) déclaré(s)')
    print(f'{articles} article(s) relevé(s) au code, dont {interieurs} '
          f'intérieur(s) : autant d’adresses que la table comptait fermées')
    for p in plages:
        etat = (f'{len(p["articles"])} article(s)' if p['deplie']
                else f'NON DÉPLIÉE — {p["motif"]}')
        print(f'    {p["plage"]:<28} {etat}')
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
