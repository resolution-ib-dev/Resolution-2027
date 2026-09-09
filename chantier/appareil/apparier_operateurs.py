# -*- coding: utf-8 -*-
"""Appariement des opérateurs entre les fichiers, faute d'identifiant unique.

Les dépenses fiscales ont un numéro, les taxes affectées un SIREN, les
programmes un code. **Les opérateurs n'ont rien.** Ils s'écrivent
« ADEME - Agence de l'environnement et de la maîtrise de l'énergie » ici,
« Ademe » là, « Agences de l'eau » ailleurs, et les agrégats du classeur les
filtrent sur leur intitulé exact. Un libellé qui change casse un total sans
bruit.

**La liste officielle est l'onglet « Opérateurs » du classeur ETP et agences.**
Tout le reste s'y rattache : c'est elle qui dit qui existe, combien d'entités
une ligne regroupe, et quel régime lui est appliqué.

## Comment l'appariement se fait, et ce qu'il refuse de faire

Trois passes mécaniques, de la plus sûre à la moins sûre.

  1. **le nom normalisé** — accents, casse, ponctuation et articles retirés ;
  2. **le sigle** — ce qui précède le premier tiret, quand c'est un sigle ;
  3. **la forme longue** — ce qui suit le tiret.

Ce qu'aucune passe n'attrape sort en **candidats**, avec leur meilleur voisin et
son score, et **rien n'est apparié sur un score**. Le rapprochement se tranche à
la lecture et s'écrit dans `ECRITS`, exactement comme A-35 le pose pour les
chiffres : deux libellés proches ne désignent pas forcément la même chose, et
c'est justement quand ils sont proches qu'on se trompe.

`ECARTES` porte le miroir : deux libellés que la mécanique rapprocherait et qui
ne désignent pas le même organisme.

Usage : python3 apparier_operateurs.py ../referentiels/socle_budgetaire.json \\
            ../livrables/appariement_operateurs.txt
"""
import json
import re
import sys
import unicodedata

# ------------------------------------------------------- les cas écrits à la main
# clé : le libellé tel qu'il apparaît dans le fichier d'origine
# valeur : le libellé officiel de l'onglet « Opérateurs », ou None quand
#          l'organisme n'y figure pas et que c'est constaté, non supposé.
ECRITS = {
    # Les affectataires que la tête de l'onglet des taxes isole nommément.
    'France Compétences': 'France Compétences',
    "Agences de l'eau": None,
    'Action Logement Services': None,
    'AFITF - Agence de financement des infrastructures de transport de France':
        'AFITF - Agence de financement des infrastructures de transport de '
        'France',
}

# Deux libellés que la mécanique rapprocherait à tort. Chacun dit pourquoi.
ECARTES = {
    ("Agences de l'eau", "Agence de l'eau"):
        "les agences de l'eau sont six établissements de bassin ; l'onglet des "
        "opérateurs ne porte pas d'entité unique de ce nom",
}

ARTICLES = {'de', 'du', 'des', 'la', 'le', 'les', "l", "d", 'et', 'pour',
            'aux', 'au', 'en', 'sur', 'a'}


def sans_accent(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t)
                   if unicodedata.category(c) != 'Mn')


def normaliser(t):
    """Le nom réduit à ses mots pleins, sans accent, casse ni ponctuation."""
    if not t:
        return ''
    t = sans_accent(t).lower()
    t = re.sub(r"[’']", ' ', t)
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    mots = [m for m in t.split() if m and m not in ARTICLES]
    return ' '.join(mots)


def sigle_et_long(t):
    """« ADEME - Agence de… » rend ('ademe', 'agence de…')."""
    if not t:
        return '', ''
    m = re.match(r'^\s*([^\-–]{1,14}?)\s*[\-–]\s*(.+)$', t)
    if not m:
        return '', normaliser(t)
    gauche, droite = m.group(1).strip(), m.group(2).strip()
    # Un sigle est court et majoritairement en capitales. « Agence nationale »
    # n'en est pas un.
    lettres = [c for c in gauche if c.isalpha()]
    if lettres and sum(c.isupper() for c in lettres) / len(lettres) >= 0.6:
        return normaliser(gauche), normaliser(droite)
    return '', normaliser(t)


def sigle_tete(t):
    """« ANSC Agence du numérique… » rend ('ansc', 'agence du numérique…').

    Les ODAC écrivent leur sigle collé au nom, sans tiret. Le premier mot est un
    sigle s'il fait au moins deux lettres et qu'il est majoritairement en
    capitales — « Agence » n'en est pas un, « ANSC » et « BPI_PARTICIP » en sont.
    """
    if not t:
        return '', ''
    mots = t.strip().split()
    if len(mots) < 2:
        return '', normaliser(t)
    premier = mots[0]
    lettres = [c for c in premier if c.isalpha()]
    if len(lettres) >= 2 and sum(c.isupper() for c in lettres) / len(lettres) >= 0.8:
        return normaliser(premier), normaliser(' '.join(mots[1:]))
    return '', normaliser(t)


def score(a, b):
    """Part des mots du plus court qui se retrouvent dans l'autre."""
    ma, mb = set(a.split()), set(b.split())
    if not ma or not mb:
        return 0.0
    return len(ma & mb) / min(len(ma), len(mb))


def index_officiel(operateurs):
    """Trois tables de résolution vers le libellé officiel."""
    par_nom, par_sigle, par_long = {}, {}, {}
    for o in operateurs:
        nom = o['socle']['operateur']
        par_nom.setdefault(normaliser(nom), nom)
        sig, lon = sigle_et_long(nom)
        if sig:
            par_sigle.setdefault(sig, nom)
        if lon:
            par_long.setdefault(lon, nom)
    return par_nom, par_sigle, par_long


def apparier(libelle, tables, officiels):
    """Le libellé officiel et la voie qui l'a trouvé, ou un candidat."""
    if libelle in ECRITS:
        return ECRITS[libelle], 'écrit à la main', 1.0
    par_nom, par_sigle, par_long = tables
    n = normaliser(libelle)
    if n in par_nom:
        return par_nom[n], 'nom', 1.0
    sig, lon = sigle_et_long(libelle)
    if sig and sig in par_sigle:
        return par_sigle[sig], 'sigle', 1.0
    if lon and lon in par_long:
        return par_long[lon], 'forme longue', 1.0
    if lon and lon in par_nom:
        return par_nom[lon], 'forme longue', 1.0
    # Les ODAC collent leur sigle au nom, sans tiret. Le sigle seul ne suffit
    # pas — il se confirme par la forme longue, et les deux ensemble font une
    # passe sûre.
    sig2, lon2 = sigle_tete(libelle)
    if lon2 and lon2 in par_nom:
        return par_nom[lon2], 'forme longue sans tiret', 1.0
    if lon2 and lon2 in par_long:
        return par_long[lon2], 'forme longue sans tiret', 1.0
    if sig2 and sig2 in par_sigle:
        officiel = par_sigle[sig2]
        confirme = score(lon2, sigle_et_long(officiel)[1] or
                         normaliser(officiel))
        if confirme >= 0.6:
            return officiel, 'sigle confirmé', confirme
    # Aucune passe sûre : on propose le meilleur voisin, on n'apparie pas.
    meilleur, meilleur_score = None, 0.0
    for nom in officiels:
        s = max(score(n, normaliser(nom)),
                score(lon, normaliser(nom)) if lon else 0.0,
                score(lon2, normaliser(nom)) if lon2 else 0.0)
        if s > meilleur_score:
            meilleur, meilleur_score = nom, s
    return None, meilleur, meilleur_score


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    s = json.load(open(argv[1], encoding='utf-8'))
    operateurs = s.get('operateurs') or []
    officiels = [o['socle']['operateur'] for o in operateurs]
    tables = index_officiel(operateurs)

    lignes = [f"Appariement des opérateurs — {len(officiels)} libellé(s) "
              f"officiel(s) à l'onglet « Opérateurs »",
              "",
              "La liste officielle fait foi. Rien n'est apparié sur un score :",
              "ce que la mécanique n'attrape pas sort en candidat, et se tranche",
              "à la lecture dans le bloc ECRITS.",
              ""]
    resume = []

    for titre, cle, entrees in (
            ("taxes affectées", 'beneficiaire', s.get('taxes_affectees') or []),
            ("ODAC-ODAL", 'organisme', s.get('odac_odal') or [])):
        libelles = {}
        for e in entrees:
            nom = e['socle'].get(cle)
            if nom:
                libelles.setdefault(nom, 0)
                libelles[nom] += 1
        apparies, candidats, absents, hors = [], [], [], []
        for nom in sorted(libelles):
            officiel, voie, sc = apparier(nom, tables, officiels)
            if officiel:
                apparies.append((nom, officiel, voie, libelles[nom]))
            elif voie == 'écrit à la main' or nom in ECRITS:
                absents.append((nom, libelles[nom]))
            elif sc >= 0.6:
                candidats.append((nom, voie, sc, libelles[nom]))
            else:
                hors.append((nom, voie, sc, libelles[nom]))
        resume.append((titre, len(libelles), len(apparies), len(absents),
                       len(candidats), len(hors)))
        lignes.append(f"\n{'=' * 78}\n{titre} — {len(libelles)} libellé(s) "
                      f"distinct(s) : {len(apparies)} apparié(s), "
                      f"{len(absents)} absent(s) de la liste officielle, "
                      f"{len(candidats)} candidat(s) à trancher, "
                      f"{len(hors)} sans voisin plausible\n{'=' * 78}")
        if apparies:
            lignes.append("\n-- APPARIÉS")
            for nom, officiel, voie, n in apparies:
                marque = '' if nom == officiel else f"  →  {officiel}"
                lignes.append(f"  [{voie:14s}] {nom[:70]}{marque}"
                              f"   ({n} ligne(s))")
        if absents:
            lignes.append("\n-- ABSENTS DE LA LISTE OFFICIELLE — constaté, "
                          "non supposé")
            for nom, n in absents:
                lignes.append(f"  {nom[:80]}   ({n} ligne(s))")
        if hors:
            lignes.append("\n-- SANS VOISIN PLAUSIBLE — vraisemblablement hors "
                          "liste officielle : collectivités, organismes de "
                          "sécurité sociale, personnes privées")
            for nom, _voisin, sc, n in sorted(hors):
                lignes.append(f"  {nom[:80]}   ({n} ligne(s))")
        if candidats:
            lignes.append("\n-- CANDIDATS — aucune passe sûre, à trancher "
                          "dans ECRITS")
            for nom, voisin, sc, n in sorted(candidats, key=lambda x: -x[2]):
                lignes.append(f"  {nom[:74]}   ({n} ligne(s))")
                lignes.append(f"      voisin le plus proche : "
                              f"{(voisin or '—')[:66]}   score {sc:.2f}")

    # -- le croisement qui mesure l'appariement contre une vérité déclarée.
    # La colonne « Opérateur déjà traité » de l'onglet ODAC-ODAL dit lesquels
    # sont comptés au titre des opérateurs du PLF. C'est la réponse du classeur ;
    # notre appariement doit la retrouver, non la remplacer.
    odac = s.get('odac_odal') or []
    declares = [o for o in odac if o['interpretation']['deja_traite_en_operateur']]
    retrouves, manques = [], []
    for o in declares:
        nom = o['socle']['organisme']
        officiel, _voie, _sc = apparier(nom, tables, officiels)
        (retrouves if officiel else manques).append(nom)
    taux = len(retrouves) / len(declares) if declares else 0.0
    lignes.append(f"\n{'=' * 78}\nCROISEMENT — les ODAC que le classeur déclare "
                  f"déjà traités en opérateur\n{'=' * 78}")
    lignes.append(f"\n  {len(declares)} déclaré(s) · {len(retrouves)} retrouvé(s) "
                  f"par l'appariement · {len(manques)} manqué(s)   "
                  f"— taux de rappel {taux:.0%}")
    lignes.append("\n  Ce taux mesure l'appariement, pas le classeur : les "
                  "manqués sont des libellés")
    lignes.append("  que la mécanique ne rattache pas, et qui se tranchent dans "
                  "ECRITS.")
    if manques:
        lignes.append("\n-- MANQUÉS")
        for nom in sorted(manques):
            lignes.append(f"  {nom[:88]}")

    entete = ["", "Résumé"]
    for titre, tot, app, abs_, cand, hs in resume:
        entete.append(f"  {titre:16s} {tot:4d} libellé(s) · {app:3d} apparié(s) "
                      f"· {abs_:2d} absent(s) · {cand:3d} candidat(s) "
                      f"· {hs:3d} sans voisin plausible")

    with open(argv[2], 'w', encoding='utf-8') as f:
        f.write('\n'.join(lignes[:1] + entete + lignes[1:]) + '\n')
    print('\n'.join(lignes[:1] + entete))
    print(f"\n{argv[2]} écrit")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
