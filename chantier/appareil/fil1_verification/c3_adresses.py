# -*- coding: utf-8 -*-
"""Contrôle C — exactitude des références, rejoué au millésime LEGI 20261007.

Les 2 844 occurrences de la liasse entière ont été contrôlées le 20261008 sur le
millésime **20261001**. Le dépôt de droit est au **20261007** depuis le commit
`2e0758c` : le contrôle se rejoue, à l'identique, sur le nouveau millésime. Le
périmètre ici est la colonne de première partie — 31 rangs, 30 fichiers.

La grammaire de numéro est celle du 20261008, reprise sans la toucher : la
comparer aux deux passes exige qu'elle ne bouge pas.

**Le rattachement se tranche par l'existence au dépôt de droit**, jamais par la
seule proximité : un jeu de codes candidats est formé — code nommé à la
proposition, puis codes nommés dans la fenêtre, puis codes dominants de la pièce
—, et le candidat retenu est celui où l'adresse existe ; une version vivante
l'emporte sur une version abrogée.

**Le contrôle rend, à côté de son compte d'absences, le compte des références
laissées hors contrôle et la raison de chacune** (reprise 1 du 20261007).
"""
import os
import re
import sys

sys.path.insert(0, '/home/claude/droit')
import droit                                                    # noqa: E402

from liasse import RANGS, lire, normaliser, segments            # noqa: E402

JOUR = '2026-10-07'

CODES = {
    "code général des impôts": "code général des impôts",
    "code des impositions sur les biens et services": "code des impositions sur les biens et services",
    "code de la sécurité sociale": "code de la sécurité sociale",
    "code général des collectivités territoriales": "code général des collectivités territoriales",
    "code du travail": "code du travail",
    "code de la construction et de l'habitation": "code de la construction et de l'habitation",
    "code de l'environnement": "code de l'environnement",
    "livre des procédures fiscales": "livre des procédures fiscales",
    "code civil": "code civil",
    "code monétaire et financier": "code monétaire et financier",
    "code de commerce": "code de commerce",
    "code de l'entrée et du séjour des étrangers et du droit d'asile":
        "code de l'entrée et du séjour des étrangers et du droit d'asile",
    "code rural et de la pêche maritime": "code rural et de la pêche maritime",
    "code des douanes": "code des douanes",
    "code de l'action sociale et des familles": "code de l'action sociale et des familles",
    "code de la santé publique": "code de la santé publique",
    "code du patrimoine": "code du patrimoine",
    "code de l'éducation": "code de l'éducation",
    "code général de la propriété des personnes publiques":
        "code général de la propriété des personnes publiques",
    "code de l'énergie": "code de l'énergie",
    "code des transports": "code des transports",
    "code du sport": "code du sport",
    "code de la voirie routière": "code de la voirie routière",
    "code de la recherche": "code de la recherche",
    "code de la défense": "code de la défense",
    "code de procédure pénale": "code de procédure pénale",
}
NOMS = sorted(CODES, key=len, reverse=True)


def _motif(nom):
    """Le nom d'un code, apostrophe droite ou typographique indifféremment.

    Les pièces écrivent l'apostrophe typographique ; la table des codes du
    dépôt de droit l'écrit droite. Les comparer telles quelles faisait manquer
    tout code dont le nom en porte une — l'énergie, l'environnement, l'action
    sociale, l'éducation, la construction et l'habitation —, et leurs adresses
    sortaient rattachées au code dominant de la pièce.
    """
    return re.escape(nom).replace("'", "[’']")


# Les textes non codifiés que le dépôt porte et que la liasse cite.
LOIS = re.compile(r"(?:loi|ordonnance)\s+n°\s*\d{2,4}-\d+\s+du\s+\d{1,2}(?:er)?\s+"
                  r"(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|"
                  r"octobre|novembre|décembre)\s+\d{4}", re.I)

ROMS = sorted({"quaterdecies", "quatervicies", "septdecies", "octodecies", "novodecies",
               "quindecies", "sexdecies", "duodecies", "terdecies", "undecies", "quinquies",
               "septvicies", "octovicies", "novovicies", "quinvicies", "unvicies", "duovicies",
               "tervicies", "sexvicies", "quater", "septies", "octies", "nonies", "decies",
               "vicies", "tricies", "sexies", "bis", "ter"}, key=len, reverse=True)
ROM = "(?:" + "|".join(ROMS) + r")(?:-0)?"
NUM = (r"(?:L\.?\s?|R\.?\s?|D\.?\s?|LO\s?)?\d+(?:-\d+)*(?:\s-0)?"
       r"(?:\s" + ROM + r"\b){0,2}(?:\s[A-Z]{1,2}\b)?(?:\s" + ROM + r"\b){0,2}(?:\s[A-Z]{1,2}\b)?")
LIST = NUM + r"(?:\s*(?:,\s*|\s+et\s+|\s+ou\s+|\s+à\s+)" + NUM + r")*"
ART_RE = re.compile(r"\b(?:[Aa]rticles?|[Aa]rt\.)\s+(" + LIST + r")")
CODE_RE = re.compile("|".join(_motif(k) for k in NOMS), re.I)

# Les quatre motifs de mise hors contrôle du 20261008, repris à l'identique.
TEXTE_EN_DISCUSSION = re.compile(
    r"(?:du |au )?texte déposé|projet de loi de finances pour 2027|"
    r"ARTICLE ADDITIONNEL|APRÈS L[’']ARTICLE|^ARTICLE \d", re.M)


def _canon(nom):
    """Le libellé exact de la table des codes, depuis une écriture quelconque."""
    plat = nom.lower().replace('’', "'")
    return CANON.get(plat, nom)


CANON = {k.lower(): k for k in CODES}


def _codes_candidats(texte, pos, dominants):
    """Le code nommé à la proposition, puis à ±400 caractères, puis les dominants."""
    cands = []
    for fen in (texte[max(0, pos - 160):pos + 200],
                texte[max(0, pos - 400):pos + 400]):
        for m in CODE_RE.finditer(fen):
            c = _canon(m.group(0))
            if c not in cands:
                cands.append(c)
        for m in LOIS.finditer(fen):
            c = m.group(0).lower()
            if c not in cands:
                cands.append(c)
    for c in dominants:
        if c not in cands:
            cands.append(c)
    return cands


def _verdict(code, num):
    """Le verdict d'une adresse au millésime du dépôt.

    `droit.article` ne rend qu'une version **applicable au jour dit** : un retour
    est donc toujours un article vivant, y compris `ABROGE_DIFF`, que LEGI pose
    sur une version applicable dont l'abrogation est déjà votée. Filtrer sur
    `VIGUEUR` l'aurait fait passer pour absent — la faute est inscrite au module
    `droit.py` lui-même.
    """
    try:
        a = droit.article(code, num, jour=JOUR)
        etat = a.get('etat', '?')
        return ('EXISTE_FIN_PROGRAMMEE' if etat.endswith('_DIFF') and etat.startswith('ABROGE')
                else 'EXISTE'), True
    except (KeyError, FileNotFoundError):
        return 'CODE_NON_PORTE', False
    except LookupError as e:
        m = str(e)
        if "absent de l'extrait" in m:
            return 'ABSENT', False
        if 'entre en vigueur le' in m:
            return 'VIGUEUR_DIFF', False
        return 'ABROGE', False


def controler(rang):
    texte = normaliser(lire(rang))
    seg = segments(texte, rang)
    dominants = [_canon(m.group(0)) for m in CODE_RE.finditer(texte)]
    dominants = sorted(set(dominants), key=dominants.count, reverse=True)[:3]

    occurrences, horsctl = [], []
    dernier_nomme = [dominants[0] if dominants else None]
    for nom_seg in ('cartouche', 'dispositif', 'expose', 'interne'):
        t = seg[nom_seg]
        if not t:
            continue
        for m in ART_RE.finditer(t):
            seq = m.group(1).rstrip(' ,.;')
            ligne_debut = t.rfind('\n', 0, m.start()) + 1
            ligne = t[ligne_debut:t.find('\n', m.end()) if t.find('\n', m.end()) > 0 else len(t)]
            # hors contrôle 1 — le texte en discussion n'est pas au droit en vigueur
            if TEXTE_EN_DISCUSSION.search(ligne) or re.search(
                    r"\bdu texte déposé\b|\bde la présente (?:clause|pièce|loi)\b", ligne):
                horsctl.append((rang, nom_seg, seq, 'texte en discussion ou accroche'))
                continue
            # hors contrôle 2 — numéro abrégé désignant un article de la pièce
            if re.fullmatch(r"\d{1,2}(?:er)?", seq) and not CODE_RE.search(ligne):
                horsctl.append((rang, nom_seg, seq, 'numéro abrégé, article de la pièce'))
                continue
            parts = []
            for p in re.split(r'\s*,\s*|\s+et\s+|\s+ou\s+', seq):
                p = p.strip().rstrip(' ,.;')
                if not p:
                    continue
                if ' à ' in p:
                    a, b = p.split(' à ', 1)
                    parts += [(a.strip(), 'borne-début'), (b.strip(), 'borne-fin')]
                else:
                    parts.append((p, 'simple'))
            # Le code désigné par la proposition elle-même : « article X du
            # code Y ». Il se prend **après** la citation et dans les quelques
            # dizaines de caractères qui la suivent, jamais au premier nom de
            # code de la ligne : une ligne de tableau en porte plusieurs, et
            # prendre le premier rattache un article du CGCT au code du travail.
            apres = t[m.end():m.end() + 90]
            mm = re.match(r"\s*(?:du|de la|des|au)\s+(?:même\s+(code|livre)\b|("
                          + "|".join(_motif(k) for k in NOMS) + r"))", apres, re.I)
            designe = None
            # « fort » : le code est désigné par la proposition elle-même, sous
            # la forme « article X du code Y » ou « du même code ». Un nom de
            # code trouvé plus loin dans la fenêtre est un simple candidat : une
            # énumération « code général des impôts, articles A, B, C » met le
            # nom **avant** la liste, et le prendre pour une désignation ferait
            # sortir chaque élément de la liste en désignation fausse.
            fort = False
            if mm and mm.group(2):
                designe = _canon(mm.group(2))
                dernier_nomme[0] = designe
                fort = True
            elif mm and mm.group(1):
                designe = dernier_nomme[0]
                fort = designe is not None
            else:
                mc = CODE_RE.search(apres)
                ml = LOIS.search(apres[:70]) or LOIS.search(ligne)
                if mc and mc.start() < 60:
                    designe = _canon(mc.group(0))
                    dernier_nomme[0] = designe
                elif ml:
                    designe = ml.group(0).lower().replace('  ', ' ')
            if designe is None and len(dominants) == 1:
                # La pièce ne nomme qu'un seul code : il est le code visé, et
                # une adresse qui n'y résout pas est une adresse morte, non une
                # citation non rattachable. Sans cette règle, une adresse fausse
                # sortait en « hors contrôle » et le compte d'absences restait
                # à zéro — c'est la deuxième faute du jeu.
                designe = dominants[0]
            cands = ([designe] if designe else []) + [
                c for c in _codes_candidats(t, m.start(), dominants) if c != designe]
            if not cands:
                for p, _k in parts:
                    horsctl.append((rang, nom_seg, p, 'code non rattachable'))
                continue
            for num, kind in parts:
                retenu = verdict = None
                for c in cands:
                    v, vivant = _verdict(c, num)
                    if vivant:
                        retenu, verdict = c, v
                        break
                if (retenu is not None and designe and fort and retenu != designe
                        and not _verdict(designe, num)[1]):
                    # Le code que la proposition désigne ne porte pas l'adresse,
                    # et un autre la porte. Le contrôle ne corrige pas la
                    # désignation : il la déclare. Sans ce verdict, une pièce
                    # pourrait viser le mauvais code sans qu'aucun compte bouge.
                    verdict = 'CODE_DESIGNE_FAUX'
                if retenu is None:
                    # Aucun candidat ne porte l'adresse vivante. Le fil ne devine
                    # pas : il ne retient un verdict négatif que si le code est
                    # **désigné par la proposition même**. Sinon il déclare hors
                    # contrôle, et le déclare.
                    if designe:
                        retenu = designe
                        verdict = _verdict(retenu, num)[0]
                        if verdict == 'CODE_NON_PORTE':
                            # Le texte désigné n'est pas à l'extrait du dépôt :
                            # l'adresse n'est pas fausse, elle n'est pas
                            # contrôlable. Elle se déclare, elle ne se compte
                            # pas en absence.
                            horsctl.append((rang, nom_seg, num,
                                            'texte hors extrait du dépôt de droit'))
                            continue
                    else:
                        horsctl.append((rang, nom_seg, num, 'code non rattachable'))
                        continue
                occurrences.append({'rang': rang, 'segment': nom_seg, 'code': retenu,
                                    'num': num, 'kind': kind, 'verdict': verdict,
                                    'seq': seq, 'ligne': ligne.strip()[:200]})
    return occurrences, horsctl


def jouer():
    occ, hors = [], []
    for rang in sorted(RANGS):
        o, h = controler(rang)
        occ += o
        hors += h
    return occ, hors


if __name__ == '__main__':
    import collections
    o, h = jouer()
    print('millésime', droit.manifeste().get('millesime', JOUR), '· jour', JOUR)
    print('occurrences contrôlées', len(o), '· distinctes',
          len({(x['code'], x['num']) for x in o}),
          '· hors contrôle', len(h))
    for k, v in collections.Counter(x['verdict'] for x in o).most_common():
        print(f'  {k:<26} {v}')
    for k, v in collections.Counter(x[3] for x in h).most_common():
        print(f'  hors: {k:<34} {v}')
