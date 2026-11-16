#!/usr/bin/env python3
"""La chaîne de calcul d'un amendement de crédits, de bout en bout.

Réécrite le 20261116. **Elle ne porte plus aucun paramètre** : taux, rythme,
date, fraction d'exercice, part conservée, indemnité et résiduel se lisent,
ligne par ligne, à `referentiels/parametres_credits_20261116.tsv` (colonnes
`regle_*`, `retenu`, `amendement_mission`, `etatB_2027_*`), que construit
`controle_liasse_classeurs.py construire` depuis les classeurs du site et le
registre. Changer une règle, c'est changer la table.

L'ancienne chaîne (20261016) partait d'une « table A » tenue pour déjà nette
du socle et du rythme. C'était faux : ses montants étaient bruts (relevé du
20261116, `methode/etats/ECARTS_liasse_classeurs_20261116.md` § 1).

Les étapes, pour chaque ligne retenue de la table :

  1. ASSIETTE   brut du PAP 2026, `brut_ae` et `brut_cp`.
  2. AE         = brut_ae × taux × rythme × fraction d'exercice
                  × (1 − part conservée) × net d'indemnité.
                  Le taux vient du classeur du site ; le rythme, la date et
                  la fraction du § 4 du registre ; la part conservée (France
                  Travail) du § 3 ; le net d'indemnité (titre 2) du § 10.
  3. CP         = min (brut_cp ; brut_ae) × le même produit × (1 − résiduel),
                  le résiduel étant celui du § 3 du registre.
  4. PLAFOND    par programme : AE ≤ AE ouvertes à l'état B 2027 ;
                  CP ≤ CP ouverts et CP ≤ AE ; titre 2 ≤ titre 2 ouvert.

Usage : python3 appareil/chaine_credits.py [--mission] [--lignes]
"""
import csv, sys
from collections import OrderedDict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TABLE = RACINE / 'referentiels/parametres_credits_20261116.tsv'


def lire_table(chemin=TABLE):
    return list(csv.DictReader(open(chemin, encoding='utf-8'), delimiter='\t'))


def coefficient(d):
    """Part du brut retirée en 2027, d'après les seules colonnes de la table."""
    return (float(d['regle_taux']) * float(d['regle_rythme']) * float(d['regle_fraction'])
            * (1 - float(d['regle_part_conservee'])) * float(d['regle_net_indemnite']))


def montant(d):
    """AE et CP d'une ligne, avant plafond du programme."""
    k = coefficient(d)
    ae, cp = float(d['brut_ae']), float(d['brut_cp'])
    return ae * k, min(cp, ae) * k * (1 - float(d['regle_residuel']))


def programmes(table=None, retenu='oui'):
    """Par programme de l'état B 2027, dans l'ordre de la table :
    {libellé 2027 : dict(mission, amendement, ae, cp, t2, ouvert_ae, ouvert_cp,
                         ouvert_t2, ae_brute, cp_brut, ecrete, lignes)}."""
    out = OrderedDict()
    for d in (table or lire_table()):
        if d['retenu'] != retenu or d['regle_taux'] == '':
            continue
        ae, cp = montant(d)
        p = out.setdefault(d['etatB_2027_programme'] or d['libelle_programme'], dict(
            mission=d['etatB_2027_mission'] or d['mission'], amendement=d['amendement_mission'],
            numero=d['programme'], ae=0.0, cp=0.0, t2=0.0,
            ouvert_ae=int(d['etatB_2027_ae'] or 0), ouvert_cp=int(d['etatB_2027_cp'] or 0),
            ouvert_t2=int(d['etatB_2027_titre2'] or 0), lignes=[]))
        p['ae'] += ae
        p['cp'] += cp
        if d['titre'] == '2':
            p['t2'] += ae
        p['lignes'].append(d)
    for p in out.values():
        p['ae_brute'], p['cp_brut'] = p['ae'], p['cp']
        p['ae'] = min(p['ae'], p['ouvert_ae'])
        p['cp'] = min(p['cp'], p['ouvert_cp'], p['ae'])
        p['t2'] = min(p['t2'], p['ouvert_t2'], p['cp'])
        p['ecrete'] = p['ae'] < p['ae_brute'] - 0.5 or p['cp'] < p['cp_brut'] - 0.5
        p['ae'], p['cp'], p['t2'] = round(p['ae']), round(p['cp']), round(p['t2'])
    return out


def missions(table=None):
    """{n° d'amendement : (mission 2027, [(programme, dict)])}, programmes par AE décroissantes."""
    out = {}
    for lib, p in programmes(table).items():
        if p['ae'] < 1:
            continue
        out.setdefault(int(p['amendement']), (p['mission'], []))[1].append((lib, p))
    for n in out:
        out[n][1].sort(key=lambda x: -x[1]['ae'])
    return OrderedDict(sorted(out.items()))


def main(argv):
    f = lambda x: f'{x:>16,.0f}'.replace(',', ' ')
    if '--lignes' in argv:
        print(f"{'AE':>16} {'CP':>16}  prog cat ligne   coef.  date       cas")
        for d in lire_table():
            if d['retenu'] == 'oui':
                ae, cp = montant(d)
                print(f"{f(ae)} {f(cp)}  {d['programme']:>4} {d['categorie']:>3} {d['ligne_registre']:<7} "
                      f"{coefficient(d):.4f} {d['regle_date']:<10} {d['regle_cas']}")
        return 0
    ms = missions()
    tae = tcp = 0
    for n, (mis, progs) in ms.items():
        ae = sum(p['ae'] for _, p in progs)
        cp = sum(p['cp'] for _, p in progs)
        tae += ae
        tcp += cp
        print(f"n° {n:>2} {f(ae)} {f(cp)}  {mis}")
        if '--mission' not in argv:
            for lib, p in progs:
                print(f"      {f(p['ae'])} {f(p['cp'])}  {'écrêté ' if p['ecrete'] else '       '}{lib[:70]}")
    print(f"TOTAL {f(tae)} {f(tcp)}  {len(ms)} amendements")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
