# -*- coding: utf-8 -*-
"""`REF_norme` — une entrée par mesure, son véhicule et son vecteur.

A-231 fait du normage juridique une couche du corpus, au même rang que
`REF_chiffres`. A-227 impose deux colonnes distinctes — le rattachement se
plaide, le vecteur se trouve — et un contrôle qui refuse de les confondre.

Ce module construit la couche. **Il ne trouve aucun vecteur par lui-même** : il
en dérive mécaniquement ceux que les annexes portent, il reprend ceux que
`vecteurs.py` déclare à la main, et il laisse tout le reste en `a_trouver` avec
son compte.

## D'où vient chaque entrée

    depense_fiscale   l'annexe des dépenses fiscales nomme, pour chacune,
                      l'article du code qui la crée et la norme de référence à
                      laquelle elle déroge. **Le vecteur se dérive, il ne se
                      cherche pas.**
    taxe_affectee     l'annexe nomme le bénéficiaire et le code de taxe. Sa
                      référence juridique renvoie à une loi de finances, non à
                      un article de code : elle dit quand, pas où. Vecteur à
                      trouver.
    operateur         la liste officielle nomme l'organisme et son programme.
                      Aucune pièce ne nomme son texte fondateur. Vecteur à
                      trouver.
    odac_odal         même chose, sur une population sept fois plus large.
    programme         le vecteur est l'état B, et il est connu d'avance —
                      c'est le même pour tous.
    proposition       la norme cible s'écrit avant que le vecteur se cherche.

## Ce que le module refuse de faire

**Il ne déduit jamais un vecteur d'une ressemblance de libellé.** A-94 l'a
démontré une fois pour toutes : le meilleur voisin de « Communes » est « Ordre
de la Libération - Conseil National des communes », avec un score de 1,00, et
c'est faux. La jointure des entrées écrites à la main se fait sur le libellé
**exact** du socle, et un libellé qui ne joint pas sort en échec plutôt que de
s'apparier au plus proche.

Usage : python3 ref_norme.py ../referentiels/socle_budgetaire.json \\
            ../referentiels/REF_doctrine.json ../referentiels/REF_norme.json
"""
import collections
import json
import os
import re
import sys

import vecteurs

REVISION = {
    'version': 'REF_norme v1',
    'date': '20260831',
    'regle': "Le rattachement se plaide, le vecteur se trouve. Deux colonnes, "
             "jamais une. Aucun vecteur ne s'invente : un trou se déclare.",
}

ETATS = ('trouve', 'a_trouver', 'inexistant', 'sans_objet')


# ---------------------------------------------------------------------------
# La décomposition de l'adresse, du macro au micro.
#
# « 158-5-a » n'est pas une adresse : c'est plusieurs niveaux collés. Une
# procédure robuste les sépare, parce que la disposition modificative ne vise
# pas le même objet selon qu'on abroge l'article, le 5, ou le a.
#
#   code         le code ou le texte — déduit par `vecteurs.DEDUCTION_CODE`
#   siege        livre, titre, chapitre, section, quand la numérotation ou le
#                relevé le déterminent
#   article      le numéro nu, ordinal latin compris
#   subdivision  I, 5, a, al. 3 — tout ce qui vient après le numéro
#
# **Aucune épissure de chaîne.** La première version recollait un fragment
# orphelin sur un radical tronqué et fabriquait « L. al.3 » à partir de
# « L. 312-35, al.3 ». Un fragment qui ne commence pas par un numéro est
# désormais une **subdivision de l'article précédent**, et il s'écrit comme
# telle — l'article ne se réécrit jamais.

NUMERO = re.compile(
    r'^(\*?(?:[LRD]\.?\s*)?\d+(?:-\d+)*'
    r'(?:\s+(?:' + '|'.join(vecteurs.ORDINAUX) + r'))?'
    r'(?:-\d+)?'
    r'(?:\s+[A-H](?![a-z]))?)'
    r'(.*)$', re.I)

# Un texte non codifié : une loi, une ordonnance, un décret nommés en clair.
TEXTE_NOMME = re.compile(r'^(Loi|Ordonnance|D[ée]cret|LOI)\s*n[°o]', re.I)

# Ce qui précède inutilement une référence dans les cellules de l'annexe.
PREFIXES = re.compile(r'^(?:articles?|art\.)\s+', re.I)


# « 2° » est une subdivision, pas un article : un nombre nu immédiatement suivi
# du signe ordinal ne commence jamais une adresse.
SUBDIVISION_NUE = re.compile(r'^\d+\s*°')


def _est_numero(f):
    if SUBDIVISION_NUE.match(f):
        return False
    return bool(re.match(r'^\*?(?:[LRD]\.?\s*)?\d', f))


def decouper_articles(brut):
    """Rend une liste de couples (article, subdivision).

    « 199 undecies B, C » → deux articles. « 158-5-a » → un article et sa
    subdivision. « L. 312-35, al.3 » → un article et sa subdivision, jamais
    « L. al.3 ».
    """
    if not brut:
        return []
    brut = brut.strip()
    if TEXTE_NOMME.match(brut):
        # Un texte nommé ne se découpe pas : il se garde entier, son article
        # éventuel restant collé — c'est le vecteur, et il est déterminable.
        return [(brut, None)]
    out = []
    for frag in re.split(r'\s*(?:,|;| et )\s*', brut):
        frag = PREFIXES.sub('', frag.strip())
        if not frag:
            continue
        if _est_numero(frag):
            m = NUMERO.match(frag)
            if m:
                out.append((m.group(1).strip(),
                            m.group(2).strip(' -,–—.') or None))
            else:
                out.append((frag, None))
        elif out:
            # Subdivision de l'article précédent. On répète l'article, on ne le
            # reconstruit pas.
            out.append((out[-1][0], frag))
        else:
            out.append((frag, None))
    return out


def deduire_code(article):
    """Le code, sa règle et son siège — ou l'aveu qu'on ne sait pas."""
    nu = (article or '').strip()
    for r in vecteurs.DEDUCTION_CODE:
        if re.match(r['motif'], nu, re.I):
            return dict(code=r['code'], code_identifiant=r['identifiant'],
                        siege=r['siege'], regle_code=r['motif'],
                        code_releve_le=r['releve_le'])
    return dict(code=vecteurs.CODE_INDETERMINE, code_identifiant=None,
                siege=None, regle_code=None, code_releve_le=None)


def _vide(v):
    return v is None or (isinstance(v, str) and not v.strip())


def _entree(population, cle, libelle, montant_eur, regime, vecteurs_, **extra):
    """Une entrée du référentiel. `vecteurs_` peut être vide : cela se compte."""
    etat = 'trouve' if vecteurs_ else 'a_trouver'
    conf = max((vecteurs.PROVENANCES[v['provenance']][0] for v in vecteurs_),
               default=0)
    e = dict(population=population, cle=cle, libelle=libelle,
             montant_eur=montant_eur, regime=regime,
             vecteurs=vecteurs_, etat_vecteur=etat, confiance_vecteur=conf)
    e.update(extra)
    return e


def des_depenses_fiscales(socle):
    """Le lot mécanisable : l'annexe porte l'article, on le dérive."""
    out = []
    for x in socle['depenses_fiscales']:
        s, i = x['socle'], x['interpretation']
        regime = i.get('regime') or None
        brut = (s.get('article') or '').replace('#', '').strip()
        arts = decouper_articles(brut)
        v = []
        for art, sub in arts:
            d = deduire_code(art)
            v.append(dict(
                role='derogation', provenance='annexe', strate='L',
                texte=d['code'], identifiant=d['code_identifiant'],
                siege=d['siege'], article=art, subdivision=sub,
                articles=(art + (' — ' + sub if sub else '')),
                regle_code=d['regle_code'],
                code_releve_le=d['code_releve_le'],
                variante='a_determiner',
                note=f"Norme de référence à l'annexe : "
                     f"« {s.get('norme_de_reference') or '—'} ». "
                     "**Le code n'est pas nommé par l'annexe** : il est déduit "
                     "de la numérotation par une règle écrite et datée "
                     "(`vecteurs.DEDUCTION_CODE`). Une forme non couverte sort "
                     "en `indéterminé`, jamais en CGI par défaut."))
        out.append(_entree(
            'depense_fiscale', s['numero'], s['libelle'],
            (s.get('realisation_2024_m_eur') or 0) * 1e6, regime, v,
            categorie=s.get('categorie'),
            nb_articles=len(arts),
            nb_vecteurs=len(v),
            programme=s.get('programme_code')))
    return out


def des_taxes(socle):
    out = []
    for x in socle['taxes_affectees']:
        s, i = x['socle'], x['interpretation']
        out.append(_entree(
            'taxe_affectee', f"TA-{s.get('code_taxe')}-{s.get('siren') or 'x'}",
            f"{s.get('beneficiaire')} — taxe {s.get('code_taxe')}",
            s.get('affectation_nette_eur') or 0,
            i.get('regime') or None, [],
            beneficiaire=s.get('beneficiaire'),
            reference_annexe=s.get('reference_juridique'),
            indice="La référence de l'annexe est une loi de finances : elle "
                   "date la taxe, elle ne la localise pas."))
    return out


def _joindre_ecrits(population, cle):
    d = vecteurs.ECRITS.get(cle)
    if d and d['population'] == population:
        return d['vecteurs'], d
    return [], None


def des_organismes(socle):
    out, joints = [], set()
    for x in socle['operateurs']:
        s, i = x['socle'], x['interpretation']
        cle = s['operateur']
        v, d = _joindre_ecrits('operateur', cle)
        if d:
            joints.add(cle)
        out.append(_entree(
            'operateur', cle, cle, None, i.get('regime') or None, v,
            programme=s.get('programme'),
            releve_le=(d or {}).get('releve_le'),
            requete=(d or {}).get('requete')))
    for x in socle['odac_odal']:
        s, i = x['socle'], x['interpretation']
        cle = s.get('organisme') or ''
        v, d = _joindre_ecrits('odac_odal', cle)
        if d:
            joints.add(cle)
        out.append(_entree(
            'odac_odal', cle, cle, None, i.get('regime') or None, v,
            entites=s.get('nombre_entites'),
            releve_le=(d or {}).get('releve_le'),
            requete=(d or {}).get('requete')))
    return out, joints


def des_programmes(socle):
    """Le vecteur est le même pour tous : l'état B. Il est connu, pas absent."""
    out = []
    progs = socle['nomenclature']['programmes']
    missions = socle['nomenclature']['missions']
    for num, p in sorted(progs.items()):
        v = [dict(vecteurs.VECTEUR_CREDITS,
                  articles=vecteurs.VECTEUR_CREDITS['articles']
                  + f" — mission « {missions.get(p.get('mission'), p.get('mission'))} », "
                    f"programme {num}")]
        out.append(_entree(
            'programme', num, p.get('libelle'), None, None, v,
            mission=missions.get(p.get('mission'), p.get('mission'))))
    return out


def des_propositions(ref):
    out = []
    for ax in ref['axes']:
        for lv in ax.get('leviers', []):
            for pr in lv.get('propositions', []):
                v = []
                de = (pr.get('droit_existant') or '').strip()
                if de:
                    v.append(dict(
                        role='competence', provenance='corpus',
                        strate=pr.get('strate'), texte=de, articles=None,
                        identifiant=None,
                        note="Champ `droit_existant` du REF_doctrine. **C'est "
                             "un indice de siège, pas un vecteur** : il nomme "
                             "le texte, rarement l'article."))
                out.append(_entree(
                    'proposition', pr['id'], pr['intitule'], None,
                    pr.get('statut'), v,
                    axe=ax['id'], levier=lv['id'], strate=pr.get('strate'),
                    norme_cible_ecrite=bool(de),
                    bloquee_par_statut=(pr.get('statut') == 'esquissee')))
    return out


def construire(socle, ref):
    entrees = []
    entrees += des_depenses_fiscales(socle)
    entrees += des_taxes(socle)
    orgs, joints = des_organismes(socle)
    entrees += orgs
    entrees += des_programmes(socle)
    entrees += des_propositions(ref)

    # Un libellé écrit à la main qui ne joint aucune ligne du socle est une
    # faute de recopie, et elle se voit ici plutôt qu'à la rédaction.
    orphelins = sorted(set(vecteurs.ECRITS) - joints)

    comptes = collections.Counter(e['population'] for e in entrees)
    etats = collections.Counter(e['etat_vecteur'] for e in entrees)
    par_pop_etat = collections.defaultdict(collections.Counter)
    for e in entrees:
        par_pop_etat[e['population']][e['etat_vecteur']] += 1
    return {
        '_revision': REVISION,
        'entrees': entrees,
        'orphelins_ecrits': orphelins,
        'comptes': {
            'entrees': len(entrees),
            'par_population': dict(comptes),
            'par_etat': dict(etats),
            'par_population_et_etat': {k: dict(v)
                                       for k, v in par_pop_etat.items()},
            'vecteurs_declares': sum(len(e['vecteurs']) for e in entrees),
        },
    }


def main(src_socle, src_ref, dst):
    socle = json.load(open(src_socle, encoding='utf-8'))
    ref = json.load(open(src_ref, encoding='utf-8'))
    r = construire(socle, ref)
    os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
    json.dump(r, open(dst, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    c = r['comptes']
    print(f"{dst} écrit — {c['entrees']} entrées, "
          f"{c['vecteurs_declares']} vecteur(s) déclaré(s)")
    for pop, e in sorted(c['par_population_et_etat'].items()):
        tot = sum(e.values())
        tr = e.get('trouve', 0)
        print(f"    {pop:16} {tot:5} — trouvé {tr:5} ({100 * tr // tot:3} %)")
    if r['orphelins_ecrits']:
        print('    ÉCHEC — libellé(s) écrit(s) à la main sans ligne au socle : '
              + ', '.join(r['orphelins_ecrits']))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
