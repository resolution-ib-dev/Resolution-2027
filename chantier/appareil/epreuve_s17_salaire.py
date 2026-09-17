# -*- coding: utf-8 -*-
"""Épreuve de S17 — la restitution salariale, 30 % en année 1 et 70 % au solde.

**Un contrôle neuf porte son jeu de fautes et son jeu de justes.** Un contrôle
qui n'a jamais rien attrapé ne prouve pas qu'il regarde ; un contrôle qui hurle
sur tout ne prouve pas qu'il discrimine.

Le jeu de fautes blesse le socle d'une façon à la fois et vérifie que la
blessure lève son code. Le jeu de justes le modifie de façons légitimes et
vérifie qu'aucune ne lève rien — c'est lui qui a le plus appris au second
cercle du socle, et c'est lui qui dit ici ce qui a le droit de bouger : le
niveau des montants, leur libellé, l'ajout d'une ligne non salariale. Ce qui
n'a pas le droit de bouger est le **rapport**, et il se vérifie exact.

À fondre dans `appareil/epreuve_controle_socle.py` au dépôt — ne pas l'écraser :
ce module ne porte que S17, l'autre porte les sept bouclages du second cercle.

Usage : python3 epreuve_s17_salaire.py ../referentiels/socle_budgetaire.json
"""
import copy
import json
import sys

LIGNES_SALAIRE = (38, 43)


def _part(socle):
    """Rejoue S17 et rend la liste des rapports, nom par nom."""
    out = []
    eco = {l['ligne']: l['classeur'] for l in socle.get('economies', [])}
    for ligne in LIGNES_SALAIRE:
        c = eco.get(ligne)
        if c:
            out.append((f'ECO-{ligne}', c.get('restitue_annee_1_md_eur'),
                        c.get('total_supprime_md_eur')))
    par_ref = {p['ligne']: p
               for p in (socle.get('bg_synthese') or {}).get('postes', [])}
    a, e = par_ref.get('C20'), par_ref.get('C21')
    if a and e:
        out.append(('C20/C21', a['valeur_m_eur'],
                    a['valeur_m_eur'] + e['valeur_m_eur']))
    return out


def _leve(socle):
    """Vrai si S17 sort au moins un écart."""
    for nom, a1, tot in _part(socle):
        if not a1 or not tot or abs(a1 / tot - 0.30) > 1e-9:
            return True
    return False


def _eco(socle, ligne):
    return next(l for l in socle['economies'] if l['ligne'] == ligne)['classeur']


def _poste(socle, ref):
    return next(p for p in socle['bg_synthese']['postes'] if p['ligne'] == ref)


FAUTES = (
    ("part portée à 29 % sur les départs d'État",
     lambda s: _eco(s, 38).__setitem__('restitue_annee_1_md_eur', 0.87)),
    ("part portée à 31 % sur les départs locaux",
     lambda s: _eco(s, 43).__setitem__('restitue_annee_1_md_eur', 6.2)),
    ("total remis à la valeur d'avant le 20260917 sur les départs d'État",
     lambda s: _eco(s, 38).__setitem__('total_supprime_md_eur', 0.9)),
    ("solde effacé sur les départs locaux",
     lambda s: _eco(s, 43).__setitem__('total_supprime_md_eur', 6)),
    ("année 1 effacée sur les départs d'État",
     lambda s: _eco(s, 38).__setitem__('restitue_annee_1_md_eur', None)),
    ("total nul sur les départs locaux",
     lambda s: _eco(s, 43).__setitem__('total_supprime_md_eur', 0)),
    ("solde salarial de France Travail amputé de moitié",
     lambda s: _poste(s, 'C21').__setitem__('valeur_m_eur', 1227.24)),
    ("année 1 salariale de France Travail doublée",
     lambda s: _poste(s, 'C20').__setitem__('valeur_m_eur', 2103.84)),
)

JUSTES = (
    ("les trois lignes doublées, rapport tenu",
     lambda s: [_eco(s, 38).update(restitue_annee_1_md_eur=1.8,
                                   total_supprime_md_eur=6.0),
                _eco(s, 43).update(restitue_annee_1_md_eur=12.0,
                                   total_supprime_md_eur=40.0),
                _poste(s, 'C20').update(valeur_m_eur=2103.84),
                _poste(s, 'C21').update(valeur_m_eur=4908.96)]),
    ("libellé d'une ligne salariale réécrit",
     lambda s: _eco(s, 38).__setitem__('intitule', 'Départs des agents d’État')),
    ("hypothèse réécrite en toutes lettres",
     lambda s: _eco(s, 38).__setitem__('hypothese', 'Hors régalien, 90 % de '
                                       'départs, 30 % restitués en année 1')),
    ("une ligne non salariale change de montant",
     lambda s: _eco(s, 40).__setitem__('total_supprime_md_eur', 12.0)),
    ("un poste non salarial change de montant",
     lambda s: _poste(s, 'G20').__setitem__('valeur_m_eur', 400.0)),
    ("arrondi au dixième sur une ligne non salariale",
     lambda s: _eco(s, 41).__setitem__('restitue_annee_1_md_eur', 9.75)),
)


def main(chemin):
    socle = json.load(open(chemin, encoding='utf-8'))
    if _leve(socle):
        print('Le socle reçu lève déjà S17 : l\'épreuve ne prouverait rien.')
        return 2
    print(f"S17 — jeu de fautes, {len(FAUTES)} blessures")
    ko = 0
    for nom, blesser in FAUTES:
        s = copy.deepcopy(socle)
        blesser(s)
        leve = _leve(s)
        print(f"    {'OK ' if leve else 'MUET'} {nom}")
        ko += 0 if leve else 1
    print(f"\nS17 — jeu de justes, {len(JUSTES)} modifications légitimes")
    for nom, modifier in JUSTES:
        s = copy.deepcopy(socle)
        modifier(s)
        leve = _leve(s)
        print(f"    {'CRIE' if leve else 'OK '} {nom}")
        ko += 1 if leve else 0
    print(f"\n{ko} défaut(s) d'épreuve")
    return 1 if ko else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1
                  else '../referentiels/socle_budgetaire.json'))
