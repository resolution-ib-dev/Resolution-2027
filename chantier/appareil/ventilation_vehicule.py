# -*- coding: utf-8 -*-
"""Ventilation des lignes d'économie tracées par véhicule législatif.

A-223 fait entrer le projet de loi de financement de la sécurité sociale au
périmètre, à parité d'appareil avec le projet de loi de finances, le PLF restant
prioritaire. **La ventilation ne commande plus le calendrier — l'auteur a
tranché l'ordre — mais elle dit combien de matière attendra la phase PLFSS.**

## Ce que le module fait, et ce qu'il ne fait pas

Il rapproche deux choses qui existent déjà : les lignes de
`referentiels/economies.json`, et la grille des portes relevée sur la loi
organique. Pour chaque ligne il déclare **le véhicule qui peut la porter**, et
**la porte par laquelle elle entre**.

**Il n'arbitre rien.** Un véhicule qui ne se déduit pas de la nature de la
dépense sort en `a_trancher`, avec la question écrite en toutes lettres. Le fil
l'inscrit et s'arrête.

Le rattachement est **écrit à la main, ligne par ligne**, jamais déduit d'un
score de ressemblance — c'est A-35, et A-94 en a montré le prix : le meilleur
voisin de « Communes » est « Ordre de la Libération - Conseil National des
communes », score 1,00, et c'est faux.

## Les quatre véhicules

    plf          projet de loi de finances. La dépense est une charge de
                 l'État, ou la ressource est une imposition affectée.
    plfss        projet de loi de financement de la sécurité sociale. La
                 dépense est une prestation ou une exonération de cotisation.
    a_trancher   la ligne agrège des flux des deux côtés. Le partage se fait
                 sur pièce, il ne se suppose pas.
    hors         aucun des deux véhicules ne vote la dépense. Une dépense de
                 colloc ne se vote pas en loi de finances.

**Le quatrième dit où la dépense se vote, jamais où le contre-PLF peut agir.**
C'est la correction d'A-239, et elle est importante : la ressource qui finance
une dépense locale, le cofinancement qui l'appelle et les dégrèvements qui la
soutiennent sont, eux, en loi de finances. Les leviers sont relevés et chiffrés
à `livrables/leviers_collocs.md` ; ce module ne les redouble pas et renvoie
vers eux.

Usage : python3 ventilation_vehicule.py ../referentiels/economies.json \\
            ../livrables/ventilation_vehicule.md
"""
import json
import os
import sys

VEHICULES = {
    'plf': 'projet de loi de finances',
    'plfss': 'projet de loi de financement de la sécurité sociale',
    'a_trancher': 'à trancher — la ligne agrège les deux côtés',
    'hors': 'hors véhicule financier de l\'État',
}

# ------------------------------------------------------------ la ventilation
# Une entrée par ligne de détail et par rubrique sans détail. Les totaux et les
# rubriques qui portent du détail ne sont pas ventilés : leur véhicule est celui
# de leurs lignes, et le déclarer deux fois inviterait à additionner deux fois.
#
#   vehicule   plf · plfss · a_trancher · hors
#   portes     les codes de la grille relevée sur la loi organique
#   motif      pourquoi ce véhicule, en une phrase
#   question   écrite seulement pour a_trancher — la question posée à l'auteur
VENTILATION = {
    # --- Opérateurs -------------------------------------------------------
    'ECO-5': dict(vehicule='a_trancher', portes=['P-06', 'P-09', 'P-12'],
                  motif="France Compétences est financé par onze taxes "
                        "affectées et par le programme 103 : les deux entrent "
                        "en loi de finances. Mais l'organisme finance "
                        "l'apprentissage, dont une part passe par des "
                        "exonérations de cotisations.",
                  question="La part apprentissage de la ligne relève-t-elle du "
                           "PLF seul, ou faut-il un volet PLFSS sur les "
                           "exonérations de cotisations d'apprentissage ?"),
    'ECO-6': dict(vehicule='plf', portes=['P-12', 'P-14'],
                  motif="France Travail ne perçoit aucune taxe affectée au "
                        "PLF 2026 : l'économie est entièrement budgétaire, sur "
                        "le programme 102, plus son plafond d'emplois."),
    'ECO-7': dict(vehicule='plf', portes=['P-06', 'P-09', 'P-12'],
                  motif="Le CNC vit de taxes affectées, les subventions "
                        "culturelles de crédits. Les deux canaux sont en loi "
                        "de finances."),
    'ECO-8': dict(vehicule='plf', portes=['P-06', 'P-09'],
                  motif="Les agences de l'eau sont financées par redevances "
                        "affectées ; leur reprise passe par le 5° bis."),
    'ECO-9': dict(vehicule='plf', portes=['P-06', 'P-09'],
                  motif="L'AFITF est un opérateur financé par taxes "
                        "affectées."),
    'ECO-10': dict(vehicule='plf', portes=['P-06', 'M-01', 'M-03'],
                   motif="Action Logement Services est un organisme "
                         "ODAC-ODAL affectataire : l'affectation ne peut être "
                         "défaite qu'en loi de finances."),
    'ECO-11': dict(vehicule='plf', portes=['P-06', 'M-03'],
                   motif="Les chambres consulaires vivent de taxes affectées ; "
                         "la condition de lien de l'article 2-II est la prise "
                         "la plus directe."),
    'ECO-12': dict(vehicule='plf', portes=['P-12', 'P-14'],
                   motif="L'ADEME est financée par crédits : programme et "
                         "plafond d'emplois."),
    'ECO-13': dict(vehicule='plf', portes=['P-06', 'M-03'],
                   motif="Les établissements publics fonciers vivent d'une "
                         "taxe spéciale d'équipement affectée."),
    'ECO-14': dict(vehicule='plf', portes=['P-06', 'P-12'],
                   motif="L'ANAH porte une taxe affectée et des crédits."),
    'ECO-15': dict(vehicule='plf', portes=['P-12'],
                   motif="MaPrimeRénov' est un dispositif budgétaire distribué "
                         "par l'ANAH — crédits des programmes 174 et 135."),
    'ECO-16': dict(vehicule='a_trancher', portes=[],
                   motif="Résidu que le classeur ne détaille pas. **Seule "
                         "ligne du chiffrage sans assiette nommée** : son "
                         "véhicule ne se déduit de rien.",
                   question="Que contient le résidu « autres » de la rubrique "
                            "des opérateurs, 2,8 Md€ ? Sans détail, ni le "
                            "véhicule ni le vecteur ne se trouvent."),

    # --- Chèques aux ménages ---------------------------------------------
    'ECO-18': dict(vehicule='plf', portes=['P-12'],
                   motif="L'aide personnalisée au logement est une prestation "
                         "de l'État, portée par les crédits du programme 109. "
                         "Elle est versée par les caisses mais elle n'est pas "
                         "une prestation de sécurité sociale."),
    'ECO-19': dict(vehicule='plf', portes=['P-12'],
                   motif="L'aide médicale de l'État est une dépense "
                         "budgétaire, programme 183, et non une prestation "
                         "d'assurance maladie."),
    'ECO-20': dict(vehicule='plf', portes=['P-12'],
                   motif="Le chèque énergie est une dépense budgétaire."),
    'ECO-21': dict(vehicule='a_trancher', portes=['P-04', 'P-17'],
                   motif="« Exonérations emploi à domicile » recouvre deux "
                         "dispositifs de nature différente : un crédit "
                         "d'impôt sur le revenu, qui est en loi de finances, "
                         "et une exonération de cotisations patronales, qui "
                         "est en loi de financement de la sécurité sociale.",
                   question="Les 1,1 Md€ portent-ils le crédit d'impôt, "
                            "l'exonération de cotisations, ou les deux ? La "
                            "réponse partage la ligne entre les deux "
                            "véhicules."),
    'ECO-22': dict(vehicule='a_trancher', portes=[],
                   motif="Résidu non détaillé de la rubrique.",
                   question="Que contient le résidu « autres » des chèques aux "
                            "ménages, 1,0 Md€ ?"),

    # --- Aides aux entreprises -------------------------------------------
    'ECO-24': dict(vehicule='plf', portes=['P-12', 'P-14'],
                   motif="L'audiovisuel public est financé par crédits depuis "
                         "la suppression de la contribution à l'audiovisuel "
                         "public ; son plafond d'emplois est en seconde "
                         "partie."),
    'ECO-25': dict(vehicule='a_trancher', portes=['P-12', 'P-04'],
                   motif="Les aides à l'emploi et à l'apprentissage mêlent des "
                         "crédits d'intervention — primes à l'embauche, aides "
                         "à l'apprentissage — et des exonérations de "
                         "cotisations sociales compensées ou non.",
                   question="Quelle part des 6,9 Md€ est en crédits et quelle "
                            "part en exonérations de cotisations ? C'est la "
                            "ligne la plus lourde à partager entre les deux "
                            "véhicules."),
    'ECO-26': dict(vehicule='plf', portes=['P-12'],
                   motif="France 2030 et les aides à l'investissement sont des "
                         "crédits, portés pour partie par des comptes "
                         "spéciaux."),
    'ECO-27': dict(vehicule='a_trancher', portes=[],
                   motif="Résidu non détaillé de la rubrique.",
                   question="Que contient le résidu « autres » des aides aux "
                            "entreprises, 1,3 Md€ ?"),

    # --- Subventions aux associations ------------------------------------
    'ECO-29': dict(vehicule='plf', portes=['P-12'],
                   motif="L'hébergement d'urgence est porté par les crédits du "
                         "programme 177."),
    'ECO-30': dict(vehicule='plf', portes=['P-12'],
                   motif="L'aide publique au développement est portée par les "
                         "crédits de la mission éponyme."),
    'ECO-31': dict(vehicule='plf', portes=['P-12'],
                   motif="Immigration et asile : crédits de la mission."),
    'ECO-32': dict(vehicule='a_trancher', portes=['P-12'],
                   motif="L'aide à l'emploi et à l'insertion par "
                         "l'associatif mêle crédits d'intervention et "
                         "dispositifs d'insertion dont une part est "
                         "cofinancée par la sphère sociale.",
                   question="Les 2,3 Md€ sont-ils entièrement des crédits "
                            "d'État, ou une part relève-t-elle de "
                            "l'insertion cofinancée ?"),
    'ECO-33': dict(vehicule='plf', portes=['P-12'],
                   motif="Volet associatif de France 2030 — crédits."),
    'ECO-34': dict(vehicule='plf', portes=['P-12'],
                   motif="Subventions culturelles — crédits."),
    'ECO-35': dict(vehicule='plf', portes=['P-12'],
                   motif="Politique de la ville — crédits du programme 147."),
    'ECO-36': dict(vehicule='a_trancher', portes=[],
                   motif="Résidu non détaillé de la rubrique.",
                   question="Que contient le résidu « autres » des subventions "
                            "aux associations, 1,4 Md€ ?"),

    # --- Rubriques sans détail, périmètre État ---------------------------
    'ECO-37': dict(vehicule='plf', portes=['P-12'],
                   motif="Charges courantes et achats de l'État — crédits de "
                         "fonctionnement, tous programmes."),
    'ECO-38': dict(vehicule='plf', portes=['P-10', 'P-12'],
                   motif="Départs de fonctionnaires de l'État — crédits de "
                         "titre 2 et plafond d'autorisation des emplois "
                         "rémunérés par l'État, en première partie."),

    # --- Périmètre collectivités locales ---------------------------------
    'ECO-40': dict(vehicule='hors', portes=['P-07'],
                   motif="Une dépense culturelle communale ne se vote pas en "
                         "loi de finances. L'État n'y agit que par le "
                         "prélèvement sur recettes, qui réduit la ressource "
                         "sans commander l'emploi."),
    'ECO-41': dict(vehicule='hors', portes=['P-07'],
                   motif="Aides locales aux entreprises — compétence des "
                         "collectivités, hors domaine de la loi de finances."),
    'ECO-42': dict(vehicule='hors', portes=['P-07'],
                   motif="Charges courantes et achats des collectivités — "
                         "hors domaine."),
    'ECO-43': dict(vehicule='hors', portes=['P-07'],
                   motif="Départs de fonctionnaires locaux — la fonction "
                         "publique territoriale ne relève ni du plafond "
                         "d'emplois de l'État ni des crédits votés en loi de "
                         "finances."),
}


def _md(v):
    """Un montant en milliards, à la française : espace fine, virgule décimale."""
    if v in (None, ''):
        return '—'
    return f'{float(v):,.1f}'.replace(',', ' ').replace('.', ',')


def rendre(eco):
    lignes = {l['id']: l for l in eco['lignes']}
    L = []
    a = L.append
    a('# La ventilation des 41 lignes d\'économie par véhicule')
    a('')
    a('*Produit par `appareil/ventilation_vehicule.py` sur '
      '`referentiels/economies.json`. Le rattachement à un véhicule est écrit '
      'à la main, ligne par ligne (A-35). Une ligne dont le véhicule ne se '
      'déduit pas de la nature de la dépense sort en `à trancher`, avec sa '
      'question — le fil ne l\'arbitre pas.*')
    a('')
    a('**Ce que cette ventilation sert.** L\'ordre du chantier est tranché : le '
      'PLF d\'abord, le PLFSS ensuite (A-223). Elle ne commande donc pas le '
      'calendrier. Elle dit **combien de matière attendra la phase PLFSS**, et '
      'combien n\'entrera dans aucun des deux textes.')
    a('')
    a('---')
    a('')

    # ------------------------------------------------------------ le compte
    a('## Le compte')
    a('')
    ventilees = [(i, v) for i, v in VENTILATION.items() if i in lignes]
    par_veh = {}
    for i, v in ventilees:
        par_veh.setdefault(v['vehicule'], []).append(i)
    a('| véhicule | lignes | montant supprimé |')
    a('|---|---|---|')
    total = 0.0
    for cle, nom in VEHICULES.items():
        lot = par_veh.get(cle, [])
        somme = sum(lignes[i]['total_supprime_md_eur'] or 0.0 for i in lot)
        total += somme
        a(f'| {nom} | {len(lot)} | **{_md(somme)} Md€** |')
    a(f'| | **{len(ventilees)}** | **{_md(total)} Md€** |')
    a('')
    a('*Les totaux et les rubriques qui portent du détail ne sont pas '
      'ventilés : leur véhicule est celui de leurs lignes, et les compter deux '
      'fois doublerait le chiffrage.*')
    a('')
    a('### Le contrôle de recomposition, et l\'écart qu\'il sort')
    a('')
    a('| périmètre | tête de l\'arbre | somme ventilée | écart |')
    a('|---|---|---|---|')
    ecarts = {}
    for per, nom in (('etat', 'État'),
                     ('collectivites_locales', 'collectivités locales')):
        tete = next((l['total_supprime_md_eur'] for l in eco['lignes']
                     if l['niveau'] == 'total' and l['perimetre'] == per), 0.0)
        somme = sum(lignes[i]['total_supprime_md_eur'] or 0.0
                    for i, _ in ventilees if lignes[i]['perimetre'] == per)
        ecarts[per] = round(somme - (tete or 0.0), 3)
        a(f'| {nom} | {_md(tete)} | {_md(somme)} | '
          f'{"0,0" if abs(ecarts[per]) < 0.0005 else _md(ecarts[per])} |')
    a('')
    if abs(ecarts.get('etat', 0)) >= 0.0005:
        a(f'**L\'écart de {_md(ecarts["etat"])} Md€ au périmètre État est dans '
          'l\'arbre du classeur lui-même**, entre la tête et la somme de ses '
          'six rubriques — il ne vient pas de la ventilation, qui reprend les '
          'lignes telles quelles. Chaque rubrique est affichée au dixième de '
          'milliard : six arrondis d\'affichage bornent l\'écart à trois '
          'dixièmes, et celui-ci en fait deux. **Il n\'est pas absorbé** '
          '(A-105) : il reste écrit ici, et la ventilation somme les lignes, '
          'jamais la tête.')
        a('')
    a('---')
    a('')

    # ------------------------------------------------------ le fait principal
    a('## Le fait principal, et il n\'était pas attendu')
    a('')
    plfss = par_veh.get('plfss', [])
    a(f'**Aucune des 41 lignes tracées ne relève du PLFSS à titre principal** — '
      f'{len(plfss)} ligne(s) en véhicule `plfss`. Ce que la phase PLFSS aura à '
      'porter **n\'est pas dans ce référentiel** : les 41 lignes sont le bras '
      '« dépenses d\'État et dépenses locales » du chiffrage. Le chômage, les '
      'retraites et la santé — qui sont la matière PLFSS du plan — vivent '
      'ailleurs au chiffrage et ne sont pas tracés ici.')
    a('')
    a('*Conséquence pour le chantier, et elle est nette* : **la phase PLFSS ne '
      'se prépare pas depuis `economies.json`.** Il lui faut sa propre couche '
      'tracée, sur les mêmes règles. À inscrire au fil suivant ; le fil ne le '
      'tranche pas.')
    a('')
    a_trancher = par_veh.get('a_trancher', [])
    somme_at = sum(lignes[i]['total_supprime_md_eur'] or 0.0 for i in a_trancher)
    a(f'**Ce qui appelle un partage entre les deux textes vaut '
      f'{_md(somme_at)} Md€ sur {len(a_trancher)} ligne(s)**, dont quatre sont '
      'des résidus « autres » que le classeur ne détaille pas. **La seule '
      'ligne lourde et vraiment mixte est celle des aides à l\'emploi et à '
      'l\'apprentissage**, 6,9 Md€ : crédits d\'un côté, exonérations de '
      'cotisations de l\'autre.')
    a('')
    hors = par_veh.get('hors', [])
    somme_hors = sum(lignes[i]['total_supprime_md_eur'] or 0.0 for i in hors)
    a(f'**Et {_md(somme_hors)} Md€ de dépense ne se votent pas en loi de '
      'finances** — le périmètre des collocs entier. **Cela ne veut pas dire '
      'qu\'ils sont hors de portée.** La dépense locale ne se vote pas ici, '
      'mais la ressource qui la finance et le cofinancement qui l\'appelle y '
      'sont : six leviers d\'État sur huit ont une porte au domaine. Ils sont '
      'relevés, chiffrés et rattachés ligne par ligne à '
      '`livrables/leviers_collocs.md` (A-239). **La colonne `hors` de ce '
      'tableau dit où la dépense se vote, pas où le contre-PLF peut '
      'agir.**')
    a('')
    a('---')
    a('')

    # ------------------------------------------------------------ le détail
    for cle, nom in VEHICULES.items():
        lot = par_veh.get(cle, [])
        if not lot:
            a(f'## {nom.capitalize()}')
            a('')
            a('Aucune ligne.')
            a('')
            a('---')
            a('')
            continue
        a(f'## {nom.capitalize()} — {len(lot)} ligne(s)')
        a('')
        a('| ligne | intitulé | rubrique | Md€ | portes |')
        a('|---|---|---|---|---|')
        for i in sorted(lot, key=lambda x: int(x.split('-')[1])):
            l, v = lignes[i], VENTILATION[i]
            rub = l['rubrique'] or ('— (rubrique sans détail)'
                                    if l['niveau'] == 'rubrique' else '—')
            portes = ', '.join(f'`{p}`' for p in v['portes']) or '—'
            a(f'| `{i}` | {l["intitule"]} | {rub} | '
              f'{_md(l["total_supprime_md_eur"])} | {portes} |')
        a('')
        for i in sorted(lot, key=lambda x: int(x.split('-')[1])):
            l, v = lignes[i], VENTILATION[i]
            a(f'**`{i}` — {l["intitule"]}** · {v["motif"]}')
            if v.get('question'):
                a('')
                a(f'> *À trancher par l\'auteur* — {v["question"]}')
            a('')
        a('---')
        a('')

    # --------------------------------------------------- ce qui reste ouvert
    a('## Ce que le fil inscrit et ne tranche pas')
    a('')
    n = 0
    for i, v in sorted(ventilees, key=lambda x: int(x[0].split('-')[1])):
        if v.get('question'):
            n += 1
            a(f'{n}. **`{i}` — {lignes[i]["intitule"]}, '
              f'{_md(lignes[i]["total_supprime_md_eur"])} Md€.** '
              f'{v["question"]}')
    a('')
    a(f'{n} question(s). Quatre d\'entre elles sont le même trou : les résidus '
      '« autres » des quatre rubriques de détail, que le classeur ne détaille '
      'pas. Elles ne se répondent pas au raisonnement — il faut ouvrir le '
      'classeur, ou l\'auteur les dit.')
    a('')
    return '\n'.join(L) + '\n'


def main(src, dst):
    eco = json.load(open(src, encoding='utf-8'))
    ids = {l['id'] for l in eco['lignes']}
    orphelins = [i for i in VENTILATION if i not in ids]
    if orphelins:
        print('ARRÊT — ventilation portant sur des lignes absentes du '
              'référentiel : ' + ', '.join(orphelins))
        return 1
    # Toute ligne de détail, et toute rubrique sans détail, doit être ventilée.
    # Une rubrique se reconnaît par le couple (périmètre, intitulé) et non par
    # son seul intitulé : « Aides aux entreprises » et « Charges courantes et
    # achats » existent des deux côtés, et l'intitulé nu ferait sortir du
    # compte les rubriques locales qui portent le même nom.
    avec_detail = {(l['perimetre'], l['rubrique'])
                   for l in eco['lignes'] if l['rubrique']}
    attendus = [l['id'] for l in eco['lignes']
                if l['niveau'] == 'detail'
                or (l['niveau'] == 'rubrique'
                    and (l['perimetre'], l['intitule']) not in avec_detail)]
    manquants = [i for i in attendus if i not in VENTILATION]
    if manquants:
        print('ARRÊT — ligne(s) non ventilée(s) : ' + ', '.join(manquants))
        return 1
    texte = rendre(eco)
    os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
    open(dst, 'w', encoding='utf-8').write(texte)
    print(f'{dst} — {len(eco["lignes"])} ligne(s) au référentiel, '
          f'{len(VENTILATION)} ventilée(s), {os.path.getsize(dst)} octets')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
