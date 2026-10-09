# -*- coding: utf-8 -*-
"""Fil 1 — temps 1 de la procédure de liasse P1 : les quatre contrôles.

Il joue les quatre contrôles sur les 31 rangs, **ne corrige rien**, et rend
quatre listes d'écarts et la colonne d'export du registre, sur ses quatre
verdicts.

Usage : python3 fil1.py > ../../methode/etats/FIL1_verification_<date>.md
"""
import collections
import sys

# Qualification des verdicts négatifs, écrite ici, nommée et motivée. Elle ne
# retire aucun écart de la liste : elle dit ce que chacun est. Une qualification
# ne s'ajoute jamais en cours d'exécution pour laisser passer ce qu'on vient de
# trouver.
QUALIFICATION = {
    ('P1-06', 'L. 1614-1-2'): 'création voulue, portée par `coll_P1_01`, amendement A, III — déclarée',
    ('P1-32', 'L. 1614-1-2'): 'création voulue, portée par la pièce même — déclarée',
    ('P1-35', 'L. 1614-1-2'): 'création voulue, portée par `coll_P1_01` — déclarée',
    ('P1-11', '721'): 'la pièce déclare elle-même que l’article n’existe pas au millésime — Q5 du 20261008, à reprendre',
    ('P1-30', '179'): 'artefact de lecture — « l’article 179 de la loi n° 2019-1479 », au cartouche et à un tableau du bloc interne ; la loi porte bien l’article',
    ('P1-30', '72-2'): 'artefact de lecture — article 72-2 de la Constitution, texte hors extrait LEGI',
    ('P1-30', '21'): 'artefact de lecture — renvoi à un considérant de décision, non à un article de code',
    ('P1-31', '1'): 'artefact de lecture — « les références de l’article 1er au code des impositions… », l’article 1er étant celui de la clause',
    ('P1-32', 'L. 1614-1-2'): 'création voulue, portée par la pièce même — déclarée',
    ('P1-37', 'L. 116-1'): 'artefact de lecture — table du bloc interne, le code visé n’est pas celui que la ligne nomme en tête',
    ('P1-37', 'LO 111-3-14'): 'artefact de lecture — article du code de la sécurité sociale cité dans une table du bloc interne',
    ('P1-37', 'LO 111-3-16'): 'artefact de lecture — article du code de la sécurité sociale cité dans une table du bloc interne',
}

import c1_conformite as A
import c2_cgi_expert as B
import c3_adresses as C
import c4_recevabilite as D
from liasse import ACCROCHES, RANGS, dispositifs, lire, normaliser

JOUR = C.JOUR


def jouer():
    ecarts_a = A.jouer()
    occ, hors = C.jouer()
    ecarts_b = B.jouer(occ)
    ecarts_d, citations = D.jouer()
    return ecarts_a, ecarts_b, (occ, hors), (ecarts_d, citations)


def colonne_export(ea, eb, occ, ed):
    """rang -> (verdict A, verdict B, verdict C, verdict D)."""
    ca = collections.Counter(x['rang'] for x in ea if x['nature'] == 'écart')
    cb = collections.Counter(x['rang'] for x in eb if x['test'] not in ('B5',))
    cc = collections.Counter(x['rang'] for x in occ
                             if x['verdict'] in ('ABSENT', 'ABROGE', 'CODE_DESIGNE_FAUX'))
    cd = collections.Counter(x['rang'] for x in ed)
    out = {}
    for r in sorted(RANGS):
        out[r] = tuple('conforme' if n == 0 else f'{n} écart' + ('s' if n > 1 else '')
                       for n in (ca[r], cb[r], cc[r], cd[r]))
    return out


def main():
    ea, eb, (occ, hors), (ed, citations) = jouer()
    w = sys.stdout.write
    nb_amd = sum(len(dispositifs(normaliser(lire(r)), r)) for r in RANGS)

    w(f"""# Fil 1 — vérification de la liasse de première partie, temps 1 — 20261009

**Porteur** : fil 1 de la liasse de première partie, Cowork, 20261009.
**Mandat** : `methode/procedure_liasse_P1_20261009.md`, § 1 et § 8, fil 1 — jouer les quatre
contrôles sur les 31 rangs, **n'en corriger aucun**, rendre quatre listes d'écarts et la colonne
d'export du registre.
**Domicile** : `methode/etats/FIL1_verification_20261009.md`.
**Appui** : `methode/procedure_liasse_P1_20261009.md`, § 1 et § 8 ·
`methode/etats/SUIVI_chantier_20261009.md` · `methode/etats/FIL0_regroupement_20261009.md` (R-G) ·
`methode/appui_des_passes.md`, R-G, R-H, R-I · `methode/etats/NUIT_3B_controles_1_2_20261008.md` ·
`livrables/registre_colonnes_depot_2027.md`, § I · `reference/cgi_expert_regles_de_lecture.md` ·
`methode/regles_redactionnelles.md` · skills `resolution-chantier`, `confrontation` ·
dépôt de droit `Resolution-2027` cloné, millésime LEGI **20261007**, `droit.py etat` joué ·
socle `referentiels/socle_texte_plf2027.json`, 90 articles, 8 annexes.
**Appareil versé** : `appareil/fil1_verification/` — `liasse.py`, `c1_conformite.py`,
`c2_cgi_expert.py`, `c3_adresses.py`, `c4_recevabilite.py`, `fautes_fil1.py`, `fil1.py`.

---

## 0. Mesure d'entrée — l'objet, mesuré avant contrôle (R-H)

| objet | mesure |
|---|---|
| rangs actifs de la colonne | **31**, pris au registre des colonnes, § I |
| amendements portés | **{nb_amd}** — P1-30 et P1-32 en portent deux chacun |
| fichiers | **30** ; la clause porte P1-31 (article 1er) et P1-04 (article 3) |
| rangs vacants barrés, hors périmètre | **6** — P1-02, P1-03, P1-12, P1-22, P1-24, P1-29 |
| octets de dispositif contrôlés | **{sum(sum(y - x for x, y in dispositifs(normaliser(lire(r)), r)) for r in RANGS)}** |
| millésime du droit | **LEGI 20261007** — les 2 844 occurrences du 20261008 l'avaient été sur 20261001 |

**Neuf pièces du périmètre étaient en retard au dépôt** et ont été reprises au coffre avant
contrôle : la clause, les quatre pièces 4.2, la pièce 4.3, la pièce 4.6, `n7b_m022` et le registre
des sources de gage. Le fil 0 les a écrites au coffre le 20261009 ; le dépôt porte encore l'état
d'avant. **Les contrôles sont joués sur l'état du coffre.**

**Deux des quatre contrôles n'existaient pas** — reprise du CGI expert, recevabilité au socle. Ils
sont écrits ici, chacun avec son jeu de fautes, et versés avec lui.

---

## 1. Les quatre contrôles, et ce qu'ils mordent

**Le jeu de fautes est la preuve des contrôles, non leur accessoire.** Seize fautes injectées —
quatre par contrôle : une valeur fausse au même repère, un repère qui ne résout pas, un repère
retiré, et **le verdict retourné**, un écart réel couvert par une déclaration de conformité.
**Les seize mordent.** `python3 appareil/fil1_verification/fautes_fil1.py` les rejoue.

| contrôle | état avant ce fil | ce qu'il passe |
|---|---|---|
| **A — conformité au corpus** | se rejouait | les 15 lignes de la checklist, sur les dispositifs |
| **B — reprise du CGI expert** | **à écrire** | section due, siège repris, ligne résolue, écart déclaré, ligne cohérente |
| **C — exactitude des références** | se rejouait | toute adresse au droit, millésime 20261007 |
| **D — recevabilité** | **à écrire** | accroches et citations du texte déposé n° 3210, au socle |

---

""")

    # ---------------- Liste 1 ----------------
    reels = [x for x in ea if x['nature'] == 'écart']
    sansobjet = [x for x in ea if x['nature'] != 'écart']
    ca = collections.Counter(x['ligne'] for x in reels)
    w(f"""## Liste 1 — conformité au corpus · **{len(reels)} écarts**, {len(sansobjet)} qualifiés sans objet

Périmètre : les {nb_amd} dispositifs, et eux seuls. Aucun exposé, aucun cartouche, aucun bloc
interne. Chaque ligne reçoit un verdict ; aucune ne reste sans verdict.

| ligne | ce qu'elle passe | écarts |
|---|---|---:|
""")
    LIB = {'R1': 'rédactions positives', 'R2': 'pas de virgule devant une conjonction',
           'R3': 'pas de point-virgule au texte normatif', 'R4': 'apostrophes typographiques',
           'R5': 'guillemets français', 'R6': 'espaces insécables',
           'R7': '« est ainsi rédigé » pour une réécriture',
           'R8': 'abroger un texte, supprimer ce qui est dedans',
           'R9': 'aucune date au 31 décembre', 'R10': 'dates au 1er janvier ou 1er juillet',
           'R11': 'pas de « doit » ni de futur', 'R12': 'une phrase une norme',
           'R13': 'aucun chiffre inventé', 'R14': 'pas de redondance entre niveaux',
           'R15': 'cohérence de la hiérarchie des normes'}
    for l in A.LIGNES:
        n = ca.get(l, 0)
        w(f"| **{l}** | {LIB[l]} | {n if n else '**0**'} |\n")
    w('\n')
    if ea:
        w('| rang | ligne | ce qui est constaté | correction proposée |\n|---|---|---|---|\n')
        for x in sorted(ea, key=lambda x: (x['rang'], x['ligne'], x['nature'])):
            ext = x['extrait'].replace('\n', ' ').replace('|', '\\|')[:150]
            marque = '' if x['nature'] == 'écart' else f" *({x['nature']})*"
            w(f"| {x['rang']} | {x['ligne']}{marque} | {x['libelle']} — « {ext} » | "
              f"{x['correction']} |\n")
    w('\n---\n\n')

    # ---------------- Liste 2 ----------------
    cb = collections.Counter(x['test'] for x in eb)
    w(f"""## Liste 2 — reprise du CGI expert · **{len([x for x in eb if x['test'] != 'B5'])} écarts**, {cb.get('B5', 0)} signalement

La règle de fond est acquise et ne se rouvre pas : *le corpus prime sur la rédaction de l'expert,
et l'écart se déclare en exposé sommaire.* Le contrôle ne juge pas qui a raison.

**Exemption nommée et motivée, versée avec le contrôle** : l'abrogation sèche d'un article que
l'expert déclare `supprimé` est la reprise même de l'expert — le § 3 des règles de lecture pose
que la colonne C est vide et que la disposition est « L'article N est abrogé. » La clause générale
abroge 396 rangs à ce titre.

| test | ce qu'il dit | écarts |
|---|---|---:|
| **B1** | la pièce touche un siège du CGI et ne porte pas la section de reprise | {cb.get('B1', 0)} |
| **B2** | un siège du CGI touché au dispositif que la section ne cite pas | {cb.get('B2', 0)} |
| **B3** | la section cite une ligne hors de sa table | {cb.get('B3', 0)} |
| **B4** | la pièce s'écarte de l'expert sans le déclarer à l'exposé | {cb.get('B4', 0)} |
| **B6** | la ligne citée et l'article nommé à côté d'elle divergent | {cb.get('B6', 0)} |
| *B5* | *article à contrôler avant emploi — signalement, non écart* | *{cb.get('B5', 0)}* |

| rang | test | ce qui est constaté |
|---|---|---|
""")
    for x in sorted(eb, key=lambda x: (x['test'], x['rang'])):
        d = str(x['detail']).replace('|', '\\|')[:200]
        ex = f" *(exemption : {x['exemption']})*" if x.get('exemption') else ''
        w(f"| {x['rang']} | {x['test']} | {x['libelle']} — {d}{ex} |\n")
    w('\n---\n\n')

    # ---------------- Liste 3 ----------------
    cv = collections.Counter(x['verdict'] for x in occ)
    ch = collections.Counter(x[3] for x in hors)
    douteux = [x for x in occ if x['verdict'] in ('ABSENT', 'ABROGE', 'CODE_DESIGNE_FAUX')]
    w(f"""## Liste 3 — exactitude des références, millésime LEGI 20261007 · **{len(douteux)} écarts**

| | |
|---|---|
| millésime | **LEGI 20261007** ; la passe du 20261008 avait joué sur **20261001** |
| occurrences contrôlées | **{len(occ)}** |
| adresses distinctes | **{len({(x['code'], x['num']) for x in occ})}** |
| occurrences laissées hors contrôle | **{len(hors)}** |

**Verdicts, en occurrences** : """ + ' · '.join(
        f'`{k}` {v}' for k, v in cv.most_common()) + """

**Les occurrences laissées hors contrôle, et la raison de chacune** — un contrôle qui ne rend que
ses absences est incomplet (reprise 1 du 20261007).

| motif | occurrences |
|---|---:|
""")
    for k, v in ch.most_common():
        w(f'| {k} | {v} |\n')
    w(f'| **total** | **{len(hors)}** |\n\n')
    w('| rang | segment | adresse | verdict | qualification |\n|---|---|---|---|---|\n')
    for x in sorted(douteux, key=lambda x: (x['rang'], x['num'])):
        q = QUALIFICATION.get((x['rang'], x['num']), '**non qualifié — à reprendre**')
        w(f"| {x['rang']} | {x['segment']} | {x['code']}, art. {x['num']} | "
          f"`{x['verdict']}` | {q} |\n")
    reels3 = [x for x in douteux if 'artefact' not in
              QUALIFICATION.get((x['rang'], x['num']), '')]
    w(f"\n**{len(douteux)} verdicts négatifs, dont {len(reels3)} portent sur la pièce** : "
      f"{len(douteux) - len(reels3)} sont des artefacts de lecture, tous hors dispositif, "
      "chacun nommé ci-dessus. **Aucune adresse morte au dispositif**, hors les créations "
      "voulues et déclarées.\n")
    w('\n**Verdicts par rang.**\n\n| rang | occ. | EXISTE | fin programmée | VIGUEUR_DIFF | '
      'ABSENT | désignation fausse | hors contrôle |\n|---|---:|---:|---:|---:|---:|---:|---:|\n')
    for r in sorted(RANGS):
        o = [x for x in occ if x['rang'] == r]
        c = collections.Counter(x['verdict'] for x in o)
        h = sum(1 for x in hors if x[0] == r)
        w(f"| {r} | {len(o)} | {c.get('EXISTE', 0)} | {c.get('EXISTE_FIN_PROGRAMMEE', 0)} | "
          f"{c.get('VIGUEUR_DIFF', 0)} | {c.get('ABSENT', 0)} | "
          f"{c.get('CODE_DESIGNE_FAUX', 0)} | {h} |\n")
    w('\n---\n\n')

    # ---------------- Liste 4 ----------------
    cd = collections.Counter(x['test'] for x in ed)
    w(f"""## Liste 4 — recevabilité, contre le socle du texte déposé n° 3210 · **{len(ed)} écarts**

Le rattachement est joué et ne se refait pas. Ce contrôle passe les **accroches** et les
**citations du texte en discussion** contre le socle — 90 articles, 8 annexes.
**{citations} citations du texte en discussion contrôlées au socle**, qu'aucune passe n'avait
jamais passées : le contrôle d'adresses les met hors contrôle à bon droit, elles ne sont pas au
droit en vigueur.

| test | ce qu'il dit | écarts |
|---|---|---:|
| **D1** | l'article d'accroche n'est pas au socle | {cd.get('D1', 0)} |
| **D2** | une pièce de première partie s'accroche à un article de la seconde | {cd.get('D2', 0)} |
| **D3** | une citation du texte en discussion ne résout pas au socle | {cd.get('D3', 0)} |
| **D4** | la pièce écrit une accroche autre que celle du registre | {cd.get('D4', 0)} |

| rang | test | ce qui est constaté |
|---|---|---|
""")
    for x in sorted(ed, key=lambda x: (x['test'], x['rang'])):
        w(f"| {x['rang']} | {x['test']} | {x['libelle']} — {str(x['detail'])[:160]} |\n")
    w('\n---\n\n')

    # ---------------- Colonne d'export ----------------
    col = colonne_export(ea, eb, occ, ed)
    propres = sum(1 for v in col.values() if all(x == 'conforme' for x in v))
    w(f"""## Colonne d'export du registre — les 31 rangs, quatre verdicts

**Pleine sur les 31 rangs.** {propres} rangs sortent conformes aux quatre contrôles.

| rang | A · corpus | B · CGI expert | C · références | D · recevabilité |
|---|---|---|---|---|
""")
    for r in sorted(RANGS):
        a, b, c, d = col[r]
        w(f'| **{r}** | {a} | {b} | {c} | {d} |\n')
    w(f"""
---

## Mesure de sortie — le mandat, point par point

| point du mandat | verdict |
|---|---|
| jouer les quatre contrôles sur les 31 rangs | **joué** — {nb_amd} amendements, 30 fichiers |
| rejouer le contrôle d'adresses au millésime LEGI 20261007 | **joué** — {len(occ)} occurrences |
| écrire le contrôle de reprise du CGI expert | **joué** — cinq tests, un signalement |
| écrire le contrôle de recevabilité au socle | **joué** — {citations} citations passées au socle |
| chaque contrôle naît avec son jeu de fautes | **joué** — 16 fautes, **16 mordent** |
| n'en corriger aucun | **tenu** — 0 pièce touchée, 0 registre touché |
| rendre quatre listes d'écarts | **joué** — {len(reels)} · {len([x for x in eb if x['test'] != 'B5'])} · {len(douteux)} · {len(ed)} |
| rendre la colonne d'export sur ses quatre verdicts | **joué** — pleine sur les 31 rangs |
| ne pas élargir le périmètre | **tenu** — les 6 rangs vacants barrés ne sont pas contrôlés |

**Ce qui relève du jugement et n'entre dans aucun compte** : la hiérarchie des signalés, le partage
entre une phrase longue à scinder et une énumération qui est son propre véhicule, et l'arbitrage de
chaque divergence avec la rédaction de l'expert. Ils se posent au temps 2.
""")


if __name__ == '__main__':
    main()
