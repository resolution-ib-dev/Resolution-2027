# -*- coding: utf-8 -*-
"""Jeu de fautes des quatre contrôles du fil 1.

Un contrôle qui ne mord pas sur une faute injectée n'est pas un contrôle : c'est
un script qui affiche zéro. Six fautes injectées le 20260... sont passées sans
une anomalie, et les trois qui passaient étaient les trois seules questions qui
comptaient. Le jeu se verse avec les contrôles, et il échoue si l'un d'eux ne
mord pas.

Chaque contrôle reçoit les **quatre fautes minimales**, déclinées sur sa pièce :

1. une valeur juste remplacée par une valeur fausse, au même repère ;
2. un repère valide remplacé par un repère qui ne résout pas ;
3. un repère retiré, la valeur restant ;
4. **le verdict lui-même retourné** — un écart déclaré conforme.

La quatrième est celle qui compte : elle teste que le contrôle lit la pièce, et
non le verdict que la pièce s'est donné.

La faute s'injecte sur une **copie** du paquet, jamais sur le paquet. Le module
ne corrige rien et n'écrit rien sous `livrables/`.

Usage : python3 fautes_fil1.py
"""
import importlib
import os
import shutil
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PAQUET = os.path.join(RACINE, 'livrables', 'depot_2027')

# contrôle -> (pièce, texte juste, texte fauté, ce que la faute doit faire sortir)
FAUTES = [
    # ---- Contrôle A — conformité au corpus ------------------------------
    ('A', 'f1-valeur-fausse', 'P1-08',
     'P1/nuitp1_04_pret_taux_zero.md',
     "à compter du 1er janvier 2027",
     "à compter du 31 décembre 2027",
     'R9', 'une date juste remplacée par une date au 31 décembre'),
    ('A', 'f2-repere-faux', 'P1-08',
     'P1/nuitp1_04_pret_taux_zero.md',
     "L’article 244 quater V est abrogé.",
     "L’article 244 quater V est abrogé ; il cesse de produire effet.",
     'R3', 'un point-virgule introduit au texte normatif'),
    ('A', 'f3-repere-retire', 'P1-08',
     'P1/nuitp1_04_pret_taux_zero.md',
     "L’article 244 quater V est abrogé.",
     "Le dernier alinéa de l’article 244 quater V est abrogé.",
     'R8', 'abroger employé pour ce qui est à l’intérieur d’un article'),
    ('A', 'f4-verdict-retourne', 'P1-10',
     'P1/nuitp1_05_investissement_industriel.md',
     "\nARTICLE 9\n",
     "\nARTICLE 9\n\n*Contrôle 2 passé : aucun écart rédactionnel, phrase unique, "
     "aucune date au 31 décembre.*\n\nI bis. – Le présent article s’appliquera aux "
     "opérations engagées à compter du 31 décembre 2027.\n",
     'R9', 'un écart réel introduit sous une déclaration de conformité'),

    # ---- Contrôle B — reprise du CGI expert -----------------------------
    ('B', 'f1-valeur-fausse', 'P1-09',
     'P1/4_2_refonte_taxes_D_plus_values.md',
     "INS 127 (117 quater, alinéa 6)",
     "INS 127 (117 septies, alinéa 6)",
     'B6', 'un siège juste de la section remplacé par un siège voisin, au même repère'),
    ('B', 'f2-repere-faux', 'P1-09',
     'P1/4_2_refonte_taxes_D_plus_values.md',
     "INS 207 (157, alinéa 9)",
     "INS 99207 (157, alinéa 9)",
     'B3', 'une ligne de table remplacée par une ligne qui ne résout pas'),
    ('B', 'f3-repere-retire', 'P1-09',
     'P1/4_2_refonte_taxes_D_plus_values.md',
     "### Ce que la pièce reprend de l’expert — lignes citées",
     "### Reprises diverses",
     'B1', 'la section retirée, le dispositif restant'),
    ('B', 'f4-verdict-retourne', 'P1-09',
     'P1/4_2_refonte_taxes_D_plus_values.md',
     "EXPOSÉ SOMMAIRE",
     "I quater. – L’article 150 VB est abrogé.\n\nEXPOSÉ SOMMAIRE\n\nLa présente "
     "rédaction ne porte aucun écart à la rédaction de l’expert : la reprise est "
     "intégrale et le corpus n’a pas eu à primer.\n",
     'B4', 'un écart réel couvert par une déclaration générale de conformité'),

    # ---- Contrôle C — exactitude des références -------------------------
    ('C', 'f1-valeur-fausse', 'P1-14',
     'P1/nuitp1_09_impot_agricole.md',
     "AMENDEMENT",
     "AMENDEMENT\n\nI bis. – L’article 199 ZZ du code général des impôts est abrogé.\n",
     'ABSENT', 'une adresse juste remplacée par une adresse fausse, au même repère'),
    ('C', 'f2-repere-faux', 'P1-08',
     'P1/nuitp1_04_pret_taux_zero.md',
     "L’article 244 quater V est abrogé.",
     "L’article 244 quater ZZ est abrogé.",
     'ABSENT', 'une adresse valide remplacée par une adresse qui ne résout pas'),
    ('C', 'f3-repere-retire', 'P1-08',
     'P1/nuitp1_04_pret_taux_zero.md',
     "L’article 244 quater V est abrogé.",
     "L’article 244 quater V du code du sport est abrogé.",
     'CODE_DESIGNE_FAUX', 'le code désigné remplacé par un code qui ne porte pas l’adresse'),
    ('C', 'f4-verdict-retourne', 'P1-13',
     'P1/nuitp1_08_avantages_culturels.md',
     "\nARTICLE 12\n",
     "\nARTICLE 12\n\n*Adresses contrôlées au droit en vigueur : toutes EXISTE, "
     "aucune absente, aucune abrogée.*\n\nI bis. – L’article 238 ZZ du code général "
     "des impôts est abrogé.\n",
     'ABSENT', 'une adresse morte introduite sous une déclaration de conformité'),

    # ---- Contrôle D — recevabilité --------------------------------------
    ('D', 'f1-valeur-fausse', 'P1-36',
     'P1/nuitp1_12_affectation_article_42.md',
     "du texte déposé",
     "du texte déposé, pris avec l’article 207 du texte déposé",
     'D3', 'une citation juste du texte en discussion doublée d’une citation fausse'),
    ('D', 'f2-repere-faux', 'P1-08',
     'P1/nuitp1_04_pret_taux_zero.md',
     "\nARTICLE 7\n",
     "\nARTICLE 207\n",
     'D4', 'une accroche valide remplacée par un article qui n’est pas au socle'),
    ('D', 'f3-repere-retire', 'P1-10',
     'P1/nuitp1_05_investissement_industriel.md',
     "\nARTICLE 9\n",
     "\nARTICLE\n",
     'D4', 'l’accroche retirée, le dispositif restant'),
    ('D', 'f4-verdict-retourne', 'P1-27',
     'P1/nuitp1_10_impot_selon_adresse.md',
     "\nARTICLE 26\n",
     "*Accroche contrôlée au socle du texte déposé n° 3210 : recevable, "
     "première partie.*\n\nARTICLE 207\n",
     'D3', 'une accroche hors socle sous une déclaration de recevabilité'),
]

# La faute 1 du contrôle C et celle du contrôle D se posent par substitution de
# numéro : la faute 2 du même contrôle les porte déjà. Elles sont écrites pour
# que le jeu nomme les quatre, et elles sont marquées sans objet.
GABARIT = '''
import os, sys, json
sys.path.insert(0, {ici!r})
import liasse, importlib
importlib.reload(liasse)
import c1_conformite, c2_cgi_expert, c3_adresses, c4_recevabilite
for m in (c1_conformite, c2_cgi_expert, c3_adresses, c4_recevabilite):
    importlib.reload(m)
quoi = {quoi!r}
if quoi == 'A':
    sortie = [(x['ligne'], x['rang']) for x in c1_conformite.jouer()]
elif quoi == 'B':
    occ, _ = c3_adresses.jouer()
    sortie = [(x['test'], x['rang']) for x in c2_cgi_expert.jouer(occ)]
elif quoi == 'C':
    occ, _ = c3_adresses.jouer()
    sortie = [(x['verdict'], x['rang']) for x in occ]
else:
    e, _n = c4_recevabilite.jouer()
    sortie = [(x['test'], x['rang']) for x in e]
print(json.dumps(sortie, ensure_ascii=False))
'''


def _jouer(quoi, paquet):
    env = dict(os.environ, RESOLUTION_PAQUET=paquet, PYTHONPATH=ICI)
    code = GABARIT.format(ici=ICI, quoi=quoi)
    r = subprocess.run([sys.executable, '-c', code], capture_output=True,
                       text=True, env=env, cwd=ICI)
    if r.returncode:
        raise RuntimeError(r.stderr[-2000:])
    import json
    return json.loads(r.stdout.strip().splitlines()[-1])


def main():
    temoin = {q: _jouer(q, PAQUET) for q in 'ABCD'}
    lignes, echecs = [], 0
    for quoi, nom, rang, piece, juste, faute, attendu, propos in FAUTES:
        with tempfile.TemporaryDirectory() as tmp:
            copie = os.path.join(tmp, 'depot_2027')
            shutil.copytree(PAQUET, copie)
            chemin = os.path.join(copie, piece)
            src = open(chemin, encoding='utf-8').read()
            if juste not in src:
                lignes.append((quoi, nom, 'NON POSÉE', f'« {juste[:40]}… » absent de {piece}'))
                echecs += 1
                continue
            open(chemin, 'w', encoding='utf-8').write(src.replace(juste, faute, 1))
            apres = _jouer(quoi, copie)
            # Le compte se prend **au rang visé**, non à la liasse : une faute
            # qui déplace un écart d'un rang à un autre laisse le total intact.
            avant_n = sum(1 for k, r in temoin[quoi] if k == attendu and r == rang)
            apres_n = sum(1 for k, r in apres if k == attendu and r == rang)
            mord = apres_n > avant_n
            lignes.append((quoi, nom, 'MORD' if mord else 'NE MORD PAS',
                           f'{propos} — {rang} {attendu} : {avant_n} → {apres_n}'))
            echecs += 0 if mord else 1
    largeur = max(len(x[3]) for x in lignes)
    print(f'{"contrôle":<9}{"faute":<22}{"verdict":<13}détail')
    for quoi, nom, v, d in lignes:
        print(f'{quoi:<9}{nom:<22}{v:<13}{d[:largeur]}')
    print()
    print(f'{sum(1 for x in lignes if x[2] == "MORD")} fautes mordues · '
          f'{sum(1 for x in lignes if x[2] == "SANS OBJET")} sans objet · '
          f'{echecs} échec(s)')
    return 1 if echecs else 0


if __name__ == '__main__':
    sys.exit(main())
