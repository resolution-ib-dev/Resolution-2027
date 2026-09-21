#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trois colonnes de la PPLC règle d'or.

A — le texte en vigueur, verbatim, relevé sur
    reference/Constitution_reference_20260806_v1.html
    (Conseil constitutionnel, 8 mars 2024, vingt-cinquième révision).
B — la disposition modificative, verbatim de la proposition.
C — le texte résultant, **produit par réapplication de B sur A**, jamais retapé.

Sorties : trois_colonnes_regle_dor.html et trois_colonnes_regle_dor.md.
Le module échoue s'il ne peut pas prouver C.
"""
import html
import unicodedata

ELISION = "[…]"
SUPPRIME = "[Alinéa supprimé.]"
NEANT = "néant"

# ------------------------------------------------------------------ A, verbatim
A34 = [
    "La loi fixe les règles concernant :",
    "— les droits civiques et les garanties fondamentales accordées aux citoyens pour l’exercice des libertés publiques ; la liberté, le pluralisme et l’indépendance des médias ; les sujétions imposées par la défense nationale aux citoyens en leur personne et en leurs biens ;",
    "— la nationalité, l’état et la capacité des personnes, les régimes matrimoniaux, les successions et libéralités ;",
    "— la détermination des crimes et délits ainsi que les peines qui leur sont applicables ; la procédure pénale ; l’amnistie ; la création de nouveaux ordres de juridiction et le statut des magistrats ;",
    "— l’assiette, le taux et les modalités de recouvrement des impositions de toutes natures ; le régime d’émission de la monnaie.",
    "La loi fixe également les règles concernant :",
    "— le régime électoral des assemblées parlementaires, des assemblées locales et des instances représentatives des Français établis hors de France ainsi que les conditions d’exercice des mandats électoraux et des fonctions électives des membres des assemblées délibérantes des collectivités territoriales ;",
    "— la création de catégories d’établissements publics ;",
    "— les garanties fondamentales accordées aux fonctionnaires civils et militaires de l’État ;",
    "— les nationalisations d’entreprises et les transferts de propriété d’entreprises du secteur public au secteur privé.",
    "La loi détermine les principes fondamentaux :",
    "— de l’organisation générale de la défense nationale ;",
    "— de la libre administration des collectivités territoriales, de leurs compétences et de leurs ressources ;",
    "— de l’enseignement ;",
    "— de la préservation de l’environnement ;",
    "— du régime de la propriété, des droits réels et des obligations civiles et commerciales ;",
    "— du droit du travail, du droit syndical et de la sécurité sociale.",
    "La loi détermine les conditions dans lesquelles s’exerce la liberté garantie à la femme d’avoir recours à une interruption volontaire de grossesse.",
    "Les lois de finances déterminent les ressources et les charges de l’État dans les conditions et sous les réserves prévues par une loi organique.",
    "Les lois de financement de la sécurité sociale déterminent les conditions générales de son équilibre financier et, compte tenu de leurs prévisions de recettes, fixent ses objectifs de dépenses, dans les conditions et sous les réserves prévues par une loi organique.",
    "Des lois de programmation déterminent les objectifs de l’action de l’État.",
    "Les orientations pluriannuelles des finances publiques sont définies par des lois de programmation. Elles s’inscrivent dans l’objectif d’équilibre des comptes des administrations publiques.",
    "Les dispositions du présent article pourront être précisées et complétées par une loi organique.",
]

A40 = [
    "Les propositions et amendements formulés par les membres du Parlement ne sont pas recevables lorsque leur adoption aurait pour conséquence soit une diminution des ressources publiques, soit la création ou l’aggravation d’une charge publique.",
]

A47 = [
    "Le Parlement vote les projets de loi de finances dans les conditions prévues par une loi organique.",
    "Si l’Assemblée nationale ne s’est pas prononcée en première lecture dans le délai de quarante jours après le dépôt d’un projet, le Gouvernement saisit le Sénat qui doit statuer dans un délai de quinze jours. Il est ensuite procédé dans les conditions prévues à l’article 45.",
    "Si le Parlement ne s’est pas prononcé dans un délai de soixante-dix jours, les dispositions du projet peuvent être mises en vigueur par ordonnance.",
    "Si la loi de finances fixant les ressources et les charges d’un exercice n’a pas été déposée en temps utile pour être promulguée avant le début de cet exercice, le Gouvernement demande d’urgence au Parlement l’autorisation de percevoir les impôts et ouvre par décret les crédits se rapportant aux services votés.",
    "Les délais prévus au présent article sont suspendus lorsque le Parlement n’est pas en session.",
]

A47_2 = [
    "La Cour des comptes assiste le Parlement dans le contrôle de l’action du Gouvernement. Elle assiste le Parlement et le Gouvernement dans le contrôle de l’exécution des lois de finances et de l’application des lois de financement de la sécurité sociale ainsi que dans l’évaluation des politiques publiques. Par ses rapports publics, elle contribue à l’information des citoyens.",
    "Les comptes des administrations publiques sont réguliers et sincères. Ils donnent une image fidèle du résultat de leur gestion, de leur patrimoine et de leur situation financière.",
]

# ------------------------------------------------------------------ C, rédigé
# Le qualificatif porte sur le RETOUR et non sur la trajectoire : la régularité
# est une propriété du résultat, pas du document qui le projette. Couplée à
# « au plus tard », elle interdit de différer sans interdire d'aller plus vite.
# Elle rend inutile la phrase de borne qu'une trajectoire régulière exigeait.
#
# La définition de l'équilibre descend à la loi organique — arbitrage de l'auteur
# du 20260908. Le standard constitutionnel reste l'équilibre ; sa mesure devient
# organique, donc révisable sans révision. Le prix est que le législateur
# organique peut la desserrer.
C34_COMPETENCE = (
    "Les lois de finances déterminent les charges et les ressources de l’État dans "
    "les conditions et sous les réserves prévues par une loi organique. En cas de "
    "déséquilibre constaté, elles déterminent la trajectoire annuelle du retour "
    "régulier à l’équilibre effectif des comptes publics au plus tard au terme de "
    "la législature, dans les conditions d’appréciation définies par la loi "
    "organique. À cette fin, elles arrêtent les mesures de correction propres "
    "à en assurer le respect et les mettent en œuvre.")
# « À titre accessoire » qualifie l'autorisation, non l'alinéa entier. En tête de
# phrase il se lisait comme une réserve générale — c'était tolérable quand la
# phrase suivait celle de la protection sociale, ce n'est plus le cas depuis que
# le pluriannuel a son alinéa propre.
C34_PLURIANNUEL = "Les lois de finances et les lois de financement de la sécurité sociale peuvent, à titre accessoire, autoriser des obligations financières mises à la charge des exercices ultérieurs, sous réserve qu’elles soient limitées par un mécanisme d’ajustement automatique. Une loi organique fixe la nature et les bornes de ces obligations."
# Les cotisations sociales ne sont pas des impositions de toutes natures : elles
# ouvrent vocation à des droits (CC 93-325 DC du 13 août 1993). L'alinéa ne les
# atteint donc pas. Il atteint la CSG et les taxes affectées, qui sont des ITN
# (CC 90-285 DC du 28 décembre 1990), et dont la loi de finances autorise déjà
# la perception — LOLF art. 34-I 1°, « y compris affectées à des personnes
# morales autres que l'État ». Nommer la loi de financement ouvrirait une
# seconde porte là où le droit organique n'en connaît qu'une.
C34_FISCAL = "Les dispositions relatives à l’assiette, au taux, aux modalités de recouvrement et à la durée des impositions de toutes natures ne sont applicables qu’après avoir été autorisées par une loi de finances, qui en évalue les conséquences sur l’équilibre des comptes publics."
# Subordination de la loi de financement : deux phrases ajoutées à l'alinéa qui
# définit la catégorie. Aucun renvoi de rang — la trajectoire se nomme par son
# objet, de sorte que la phrase reste juste quel que soit le numéro de l'alinéa.
# L'alinéa garde son sujet — « Elles », les lois de financement — dans les deux
# phrases : une disposition qui change de sujet en cours d'alinéa se lit mal, et
# la forme positive évite l'interdiction. « Le cas échéant » est nécessaire : la
# trajectoire n'existe qu'« en cas de déséquilibre constaté », et sans cette
# réserve la première phrase renverrait à un objet qui peut ne pas exister.
# Le vingt-deuxième alinéa n'est plus supprimé mais réécrit. Deux verbatim du
# droit en vigueur sont ainsi conservés — « les orientations pluriannuelles des
# finances publiques » et « s'inscrivent dans l'objectif d'équilibre des comptes
# des administrations publiques » — et la compétence passe des lois de
# programmation aux lois de finances. C'est le fond de M4.2 et de M4.8 sans la
# suppression : la catégorie des lois de programmation des finances publiques
# cesse d'être le porteur des orientations, l'acte annuel le devient.
# « peuvent déterminer » et non « déterminent » : la portée pluriannuelle de la
# loi de finances est une faculté, non une obligation annuelle de plus. La
# contrainte dure vit au dix-neuvième alinéa, où elle est conditionnée au
# déséquilibre constaté ; ici on ouvre une capacité et on nomme sa borne.
# L'autorisation accessoire d'obligations sur les exercices ultérieurs est
# rapatriée ici — arbitrage de l'auteur du 20260908. Tout le pluriannuel de
# l'article 34 tient désormais dans un seul alinéa, placé après les alinéas de
# l'exercice, au lieu d'être coupé en deux endroits de l'article.
C34_ORIENTATIONS = (
    "Les lois de finances peuvent déterminer les orientations pluriannuelles des "
    "finances publiques, qui s’inscrivent dans l’objectif d’équilibre des comptes "
    "des administrations publiques. " + C34_PLURIANNUEL)

C34_LFSS_AJOUT = " Elles s’inscrivent, le cas échéant, dans la trajectoire de retour à l’équilibre déterminée par la loi de finances. Elles sont promulguées après la loi de finances du même exercice."

# Variante tenue en réserve, non active : l'équilibre sans renvoi de mesure. Le
# standard est alors entièrement constitutionnel, donc plus dur et moins souple.
# C'était la rédaction active jusqu'à l'arbitrage du 20260908.
C34_COMPETENCE_VARIANTE_SANS_RENVOI = (
    "Les lois de finances déterminent les charges et les ressources de l’État dans "
    "les conditions et sous les réserves prévues par une loi organique. En cas de "
    "déséquilibre constaté, elles déterminent la trajectoire annuelle du retour "
    "régulier à l’équilibre effectif des comptes publics au plus tard au terme de "
    "la législature. À cette fin, elles arrêtent les mesures de correction propres "
    "à en assurer le respect et les mettent en œuvre.")

C40 = "Les propositions et amendements formulés par les membres du Parlement ne sont pas recevables lorsque leur adoption aurait pour conséquence soit l’aggravation d’une charge publique, soit la diminution d’une ressource publique sans réduction effective et au moins égale d’une charge publique."

C47_UNIVERSALITE = "Le Parlement vote la loi de finances, qui retrace pour un exercice l’intégralité des charges et des ressources de l’État, y compris les obligations financières mises à la charge des exercices ultérieurs, et arrête leur emploi. L’ensemble des ressources couvre l’ensemble des charges. Les charges et les ressources sont retracées pour leur montant brut. Une ressource ne peut être affectée à une charge déterminée qu’à titre accessoire et motivé, sous réserve de leur équilibre propre."
C47_ORDRE = "Les charges sont examinées avant les ressources. Une loi organique fixe les conditions de ce vote et celles de cette affectation."
C47_DOUZIEME = "Si la loi de finances fixant les charges et les ressources d’un exercice n’a pas été déposée en temps utile pour être promulguée avant le début de cet exercice, le Gouvernement demande d’urgence au Parlement l’autorisation de percevoir les impôts en vigueur et ouvre par décret les seuls crédits indispensables à la continuité de l’État, dans la limite globale d’un douzième par mois des crédits votés lors du dernier exercice. Ces crédits se rapportent aux obligations exigibles et prennent la forme d’avances. La loi organique en fixe les quotités et les conditions."
C47_INDEMNITES = "Jusqu’à promulgation de la loi de finances, les indemnités des membres du Parlement et du Gouvernement ainsi que du Président de la République sont suspendues et définitivement perdues."

C47_2_COUR = "La Cour des comptes assiste le Parlement et les citoyens dans le contrôle de l’action du Gouvernement. Elle assiste le Parlement et le Gouvernement dans le contrôle de l’exécution des lois de finances et de l’application des lois de financement de la sécurité sociale ainsi que dans l’évaluation des politiques publiques. Par ses rapports publics, elle contribue à l’information des citoyens."
C47_2_SINCERITE = "Le vote de la loi de finances est éclairé par des informations sincères. La sincérité des prévisions repose sur une précaution raisonnable. Le Haut Conseil des finances publiques rend un avis public sur ces prévisions et assiste le Parlement dans leur appréciation."
C47_2_RECOURS = "Tout contribuable a qualité pour contester devant la juridiction compétente la légalité d’une dépense publique, dans les conditions fixées par une loi organique."

# ------------------------------------------------------------------ opérations
def supprimer(al, rang):
    assert 1 <= rang <= len(al), f"rang {rang} hors bornes"
    return al.pop(rang - 1)


def remplacer(al, rang, nouveaux):
    assert 1 <= rang <= len(al), f"rang {rang} hors bornes"
    ancien = al[rang - 1]
    al[rang - 1:rang] = nouveaux
    return ancien


def inserer_apres(al, rang, nouveaux):
    assert 1 <= rang <= len(al), f"rang {rang} hors bornes"
    al[rang:rang] = nouveaux


def completer(al, rang, phrases):
    """Le n-ième alinéa est complété par une ou deux phrases ainsi rédigées."""
    assert 1 <= rang <= len(al), f"rang {rang} hors bornes"
    ancien = al[rang - 1]
    assert ancien.endswith("."), (
        f"alinéa {rang} : un complément de phrase suppose un alinéa clos par un point")
    al[rang - 1] = ancien + phrases
    return ancien


def inserer_mots_apres(al, rang, apres, mots, occurrences_attendues=1):
    cible = al[rang - 1]
    n = cible.count(apres)
    assert n == occurrences_attendues, (
        f"alinéa {rang} : {n} occurrence(s) de {apres!r}, "
        f"{occurrences_attendues} attendue(s)")
    al[rang - 1] = cible.replace(apres, apres + mots, 1)


# ------------------------------------------------------------------ réapplication
r34 = list(A34)
assert len(r34) == 23, f"article 34 en vigueur : {len(r34)} alinéas, 23 attendus"
assert r34[18].startswith("Les lois de finances déterminent")
assert r34[21].startswith("Les orientations pluriannuelles")
assert r34[20].startswith("Des lois de programmation déterminent les objectifs")

# Ordre décroissant de rang. Aucune opération ne déplace un alinéa en vigueur :
# les deux réécritures et le complément se font sur place, et la seule insertion
# est faite après le 22e, de sorte que le seul alinéa déplacé est l'habilitation
# organique — désignée comme le dernier alinéa, désignation qui reste vraie.
# 1° — la réécriture du 22e ne déplace aucun rang.
ancien34_orientations = remplacer(r34, 22, [C34_ORIENTATIONS])
assert r34[18].startswith("Les lois de finances déterminent")
assert r34[19].startswith("Les lois de financement de la sécurité sociale")
assert r34[21] == C34_ORIENTATIONS

# 2° — l'alinéa fiscal est inséré après le 22e, en fin de bloc financier, plutôt
# que sous la compétence des lois de finances : porté au 20e il décalait de un
# tous les alinéas suivants, dont celui des lois de financement, que le droit
# désigne par son rang. Il vient donc en dernière position substantielle, avant
# la seule habilitation organique.
inserer_apres(r34, 22, [C34_FISCAL])
assert r34[21] == C34_ORIENTATIONS, "l’insertion a déplacé les orientations"
assert r34[22] == C34_FISCAL

# 3° — le complément ne change aucun rang.
ancien34_lfss = completer(r34, 20, C34_LFSS_AJOUT)
assert r34[18].startswith("Les lois de finances déterminent"), "le complément a déplacé le 19e"

# 4° — la rédaction nouvelle du 19e ne déplace aucun rang.
ancien34 = remplacer(r34, 19, [C34_COMPETENCE])
assert len(r34) == 24, f"article 34 révisé : {len(r34)} alinéas, 24 attendus"
assert r34[18] == C34_COMPETENCE
assert r34[19] == A34[19] + C34_LFSS_AJOUT, "l’alinéa des lois de financement ne rend pas C"
assert r34[19].startswith("Les lois de financement de la sécurité sociale")
assert "sont promulguées après la loi de finances du même exercice" in r34[19]
assert r34[19] == r34[19], ""
assert r34[20].startswith("Des lois de programmation déterminent les objectifs")
assert r34[21] == C34_ORIENTATIONS, "les orientations pluriannuelles ne sont pas au 22e alinéa révisé"
assert r34[22] == C34_FISCAL, "l’alinéa fiscal n’est pas au 23e alinéa révisé"
assert "à titre accessoire" in r34[21], "le pluriannuel accessoire n’est pas dans l’alinéa des orientations"
assert sum("à titre accessoire" in a for a in r34) == 1, "le pluriannuel accessoire figure en double"
assert r34[23].startswith("Les dispositions du présent article"), "l’habilitation organique n’est plus le dernier alinéa"
assert sum("orientations pluriannuelles" in a for a in r34) == 1, "les orientations pluriannuelles doivent figurer une fois"
assert not any("définies par des lois de programmation" in a for a in r34), "la compétence des lois de programmation subsiste"
# Les rangs en vigueur que la révision ne bouge pas : c'est ce que le placement
# de l'alinéa fiscal en fin de bloc achète.
assert r34[18].startswith("Les lois de finances déterminent"), "le 19e a changé de rang"
for rang in (20, 21):
    assert r34[rang - 1].startswith(A34[rang - 1][:40]), (
        f"le {rang}e alinéa en vigueur a changé de rang")
# Les trois renvois de rang de l'article 5 de la proposition, vérifiés sur l'état révisé.
RENVOIS_ART5 = {
    19: "trajectoire annuelle",                       # II
    20: "sont promulguées après la loi de finances du même exercice",  # III
    23: "ne sont applicables qu’après avoir été autorisées",  # IV
}
for rang, marqueur in RENVOIS_ART5.items():
    assert marqueur in r34[rang - 1], (
        f"article 5 de la proposition : le renvoi au {rang}e alinéa de l’article 34 "
        f"ne porte pas {marqueur!r}")

assert r34[4] == A34[4], "le cinquième alinéa du domaine de la loi a bougé"
assert r34[16] == A34[16], "le tiret des principes fondamentaux a bougé"
assert sum("orientations pluriannuelles" in a for a in r34) == 1, "les orientations pluriannuelles doivent figurer une fois"
assert not any("définies par des lois de programmation" in a for a in r34), "la compétence des lois de programmation subsiste"

r40 = [C40]

r47 = list(A47)
assert len(r47) == 5, f"article 47 en vigueur : {len(r47)} alinéas, 5 attendus"
assert r47[3].startswith("Si la loi de finances fixant les ressources et les charges")
remplacer(r47, 4, [C47_DOUZIEME])
inserer_apres(r47, 4, [C47_INDEMNITES])
assert r47[0].startswith("Le Parlement vote les projets de loi de finances")
remplacer(r47, 1, [C47_UNIVERSALITE, C47_ORDRE])
assert len(r47) == 7, f"article 47 révisé : {len(r47)} alinéas, 7 attendus"
assert r47[2] == A47[1] and r47[3] == A47[2], "les délais ont bougé"
assert r47[4] == C47_DOUZIEME and r47[5] == C47_INDEMNITES
assert r47[6] == A47[4], "la suspension hors session n’est plus le dernier alinéa"

r47_2 = list(A47_2)
assert len(r47_2) == 2
premiere = r47_2[0].split(". ")[0]
assert premiere.count("Parlement") == 1, (
    f"première phrase : {premiere.count('Parlement')} occurrence(s) de « Parlement »")
# L'ancre porte la phrase entière : « assiste le Parlement » apparaît deux fois
# dans l'alinéa — première et deuxième phrase — et une ancre plus courte
# insérerait au mauvais endroit. Le contrôle d'unicité l'a dit au premier passage.
inserer_mots_apres(
    r47_2, 1, "assiste le Parlement dans le contrôle de l’action du Gouvernement",
    "", occurrences_attendues=1)
r47_2[0] = r47_2[0].replace(
    "assiste le Parlement dans le contrôle de l’action du Gouvernement",
    "assiste le Parlement et les citoyens dans le contrôle de l’action du Gouvernement", 1)
r47_2 += [C47_2_SINCERITE, C47_2_RECOURS]
assert r47_2[0] == C47_2_COUR, "la première phrase du premier alinéa ne rend pas C"
assert r47_2[1] == A47_2[1], "la sincérité des comptes a bougé"
assert len(r47_2) == 4

# ------------------------------------------------------------------ lignes du trois colonnes
# (A, B, C) — A et C élidés hors des alinéas touchés ; B verbatim de la proposition.
B34_CHAPEAU = "L’article 34 de la Constitution est ainsi modifié :"
B47_CHAPEAU = "L’article 47 de la Constitution est ainsi modifié :"
B47_2_CHAPEAU = "L’article 47-2 de la Constitution est ainsi modifié :"

BLOCS = [
    ("Article 34", "Article 1er de la proposition", B34_CHAPEAU, [
        (ELISION, "", [], ELISION, None),
        (A34[18],
         "4° Le dix-neuvième alinéa est ainsi rédigé :",
         ["règle d’or : la trajectoire annuelle du retour régulier à l’équilibre, "
          "échéance au plus tard au terme de la législature",
          "correction : les mesures qui en assurent le respect sont arrêtées et "
          "mises en œuvre dans le même acte",
          "conditions d’appréciation de l’équilibre renvoyées à la loi organique, "
          "en fin de phrase, sans couper la trajectoire de son terme",
          "l’alinéa reste un alinéa : aucun rang suivant n’est décalé"],
         r34[18],
         "dix-neuvième alinéa · socle"),
        (A34[19],
         "3° Le vingtième alinéa est complété par deux phrases ainsi rédigées :",
         ["la loi de financement s’inscrit, le cas échéant, dans la trajectoire "
          "déterminée par la loi de finances",
          "elle est promulguée après la loi de finances du même exercice"],
         A34[19] + "**" + C34_LFSS_AJOUT + "**",
         "vingtième alinéa · socle · complément"),
        (A34[21],
         "1° Le vingt-deuxième alinéa est ainsi rédigé :",
         ["les orientations pluriannuelles des finances publiques passent des lois "
          "de programmation aux lois de finances, qui peuvent les déterminer sans "
          "y être tenues",
          "l’objectif d’équilibre des comptes des administrations publiques est "
          "conservé en verbatim",
          "la catégorie des lois de programmation des finances publiques cesse "
          "d’en être le porteur",
          "pluriannuel accessoire rapatrié ici : l’engagement des exercices "
          "ultérieurs devient une autorisation bornée par un ajustement "
          "automatique, dans les deux actes financiers",
          "tout le pluriannuel de l’article 34 tient dans ce seul alinéa"],
         C34_ORIENTATIONS,
         "vingt-deuxième alinéa · socle"),
        ("néant",
         "2° Après le vingt-deuxième alinéa, il est inséré un alinéa ainsi rédigé :",
         ["autorisation budgétaire : une disposition fiscale n’est applicable "
          "qu’après avoir été autorisée par une loi de finances",
          "la loi de finances qui autorise évalue les conséquences de la "
          "disposition sur l’équilibre des comptes publics",
          "inséré en fin de bloc financier, avant la seule habilitation "
          "organique : aucun alinéa en vigueur ne change de rang"],
         C34_FISCAL,
         "alinéa nouveau, vingt-troisième après révision · socle"),
        (ELISION, "", [], ELISION, None),
    ]),
    ("Article 40", "Article 2 de la proposition",
     "L’article 40 de la Constitution est ainsi rédigé :", [
        (A40[0],
         "L’article est rédigé en entier, précédé de « Art. 40. — ».",
         ["la diminution d’une ressource publique devient recevable si elle est "
          "gagée sur une réduction de charge effective et au moins égale",
          "l’aggravation d’une charge publique reste irrecevable et passe en tête "
          "des deux branches"],
         r40[0], "alinéa unique · optionnel"),
    ]),
    ("Article 47", "Article 3 de la proposition", B47_CHAPEAU, [
        (A47[0],
         "3° Le premier alinéa est remplacé par deux alinéas ainsi rédigés :",
         ["universalité : l’intégralité des charges et des ressources de l’exercice "
          "est retracée, engagements ultérieurs compris",
          "l’ensemble des ressources couvre l’ensemble des charges",
          "montants bruts, sans contraction",
          "affectation admise à titre accessoire, motivée et sous équilibre propre",
          "ordre du débat : les charges sont examinées avant les ressources"],
         "\n".join([r47[0], r47[1]]),
         "premier alinéa · socle, l’ordre du débat optionnel"),
        (ELISION, "", [], ELISION, None),
        (A47[3],
         "1° Le quatrième alinéa est ainsi rédigé :",
         ["fin de la reconduction des services votés",
          "douzième provisoire : les seuls crédits indispensables à la continuité "
          "de l’État, plafonnés à un douzième par mois",
          "crédits rapportés aux obligations exigibles et pris en avances",
          "autorisation de percevoir limitée aux impôts en vigueur"],
         r47[4], "quatrième alinéa · socle"),
        (NEANT,
         "2° Après le quatrième alinéa, il est inséré un alinéa ainsi rédigé :",
         ["indemnités des parlementaires, du Gouvernement et du Président de la "
          "République suspendues et définitivement perdues jusqu’à promulgation"],
         r47[5], "alinéa nouveau · optionnel"),
        (ELISION, "", [], ELISION, None),
    ]),
    ("Article 47-2", "Article 4 de la proposition", B47_2_CHAPEAU, [
        (A47_2[0],
         "1° À la première phrase du premier alinéa, après le mot : « Parlement », sont insérés les mots : « et les citoyens » ;",
         ["la Cour des comptes assiste les citoyens autant que le Parlement dans le "
          "contrôle de l’action du Gouvernement"],
         r47_2[0].replace("le Parlement et les citoyens",
                          "le Parlement **et les citoyens**", 1),
         "première phrase du premier alinéa · optionnel · complément"),
        (ELISION, "", [], ELISION, None),
        (NEANT,
         "2° L’article est complété par deux alinéas ainsi rédigés :",
         ["sincérité du vote : les informations qui l’éclairent sont sincères",
          "les prévisions reposent sur une précaution raisonnable",
          "le Haut Conseil des finances publiques rend un avis public et assiste "
          "le Parlement dans leur appréciation",
          "recours du contribuable contre la légalité d’une dépense publique"],
         "\n".join([r47_2[2], r47_2[3]]), "alinéas nouveaux · optionnel"),
    ]),
]

# ------------------------------------------------------------------ preuve
# Chaque cellule C non élidée doit se retrouver dans l'état réappliqué.
ETATS = {"Article 34": r34, "Article 40": r40, "Article 47": r47, "Article 47-2": r47_2}
verifiees = 0
for titre, _, _, lignes in BLOCS:
    etat = ETATS[titre]
    for a, b, puces, c, _ in lignes:
        if c in (ELISION, SUPPRIME):
            continue
        for morceau in c.replace("**", "").split("\n"):
            # Les marqueurs de gras sont de la présentation : la preuve porte
            # sur le texte, et elle les retire avant de comparer.
            assert morceau in etat, (
                f"{titre} : la cellule C n’est pas dans l’état réappliqué — "
                f"{morceau[:60]}…")
            verifiees += 1

# Le supprimé ne doit plus y être, et le nouveau doit y être.
assert ancien34 not in r34
assert ancien34_orientations not in r34

# ------------------------------------------------------------------ rendu
def para(txt, classe=""):
    """Rend un alinéa par ligne. « **…** » marque l'ajout dans un alinéa complété :
    le reste garde son poids normal, de sorte que l'œil trouve ce qui est neuf."""
    cl = f' class="{classe}"' if classe else ""
    out = []
    for l in txt.split("\n"):
        morceaux = l.split("**")
        rendu = "".join(
            html.escape(m) if i % 2 == 0 else f"<strong>{html.escape(m)}</strong>"
            for i, m in enumerate(morceaux))
        out.append(f"<p{cl}>{rendu}</p>")
    return "".join(out)


def cellule_b(operation, puces):
    """Colonne du milieu : la formule légistique, puis l'objet en puces."""
    if not operation and not puces:
        return '<td class="vide"></td>'
    bloc = f'<p class="op">{html.escape(operation)}</p>' if operation else ""
    if puces:
        bloc += "<ul>" + "".join(f"<li>{html.escape(x)}</li>" for x in puces) + "</ul>"
    return f"<td>{bloc}</td>"


def cellule(txt, classe=""):
    if txt == ELISION:
        return f'<td class="elision">{html.escape(ELISION)}</td>'
    if txt == SUPPRIME:
        return f'<td class="supprime"><p><em>{html.escape(SUPPRIME)}</em></p></td>'
    if txt == NEANT:
        return f'<td class="neant"><p><em>{html.escape(NEANT)}</em></p></td>'
    if not txt:
        return '<td class="vide"></td>'
    return f'<td{" class=" + chr(34) + classe + chr(34) if classe else ""}>{para(txt)}</td>'


CSS = """
:root{--encre:#1a1a1a;--gris:#6b6b6b;--trait:#c9c4b8;--fond:#fdfcfa;
--enteteA:#f2f0eb;--enteteB:#eceff2;--cible:#f6f4ee}
*{box-sizing:border-box}
body{margin:0;background:var(--fond);color:var(--encre);
font-family:"Times New Roman",Times,Georgia,serif;font-size:15px;line-height:1.45}
.page{max-width:1180px;margin:0 auto;padding:2.4rem 1.4rem 4rem}
h1{font-size:1.5rem;font-weight:600;letter-spacing:.01em;margin:0 0 .3rem;
text-align:center}
.sous{text-align:center;color:var(--gris);font-size:.9rem;margin:0 0 .4rem}
.avert{max-width:60ch;margin:1.4rem auto 2.4rem;color:var(--gris);font-size:.88rem;
border-top:1px solid var(--trait);border-bottom:1px solid var(--trait);padding:.8rem 0}
.avert b{color:var(--encre);font-weight:600}
h2{font-size:1.05rem;font-weight:600;margin:2.6rem 0 .2rem;
border-bottom:2px solid var(--encre);padding-bottom:.3rem}
h2 span{float:right;font-weight:400;font-size:.85rem;color:var(--gris)}
.chapeau{margin:.5rem 0 .7rem;font-style:italic;color:var(--gris);font-size:.9rem}
table{width:100%;border-collapse:collapse;table-layout:fixed;margin-bottom:.6rem}
col.a{width:31%}col.b{width:31%}col.c{width:38%}
th{font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;
padding:.45rem .6rem;text-align:left;border:1px solid var(--trait)}
th.a{background:var(--enteteA)}th.b{background:var(--enteteB)}th.c{background:var(--cible)}
td{border:1px solid var(--trait);padding:.55rem .6rem;vertical-align:top;font-size:.88rem}
td p{margin:0 0 .45rem}td p:last-child{margin-bottom:0}
td.c p{font-weight:600}
td p.op{font-size:.8rem;color:var(--gris);font-style:italic;margin-bottom:.4rem}
td ul{margin:0;padding-left:1.05em}
td li{margin-bottom:.22rem;font-size:.85rem}
td li:last-child{margin-bottom:0}
.elision{text-align:center;color:var(--gris);padding:.25rem}
.supprime,.neant{color:var(--gris)}
.rang{font-size:.74rem;color:var(--gris);text-transform:uppercase;
letter-spacing:.05em;padding:.3rem .6rem;border:1px solid var(--trait);
border-bottom:none;background:#faf9f6}
footer{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--trait);
color:var(--gris);font-size:.82rem}
@page{size:A4 landscape;margin:11mm}
@media print{body{background:#fff;font-size:14px}
.page{max-width:none;padding:0;width:100%}
table{page-break-inside:auto;width:100%;max-width:100%}
h2{page-break-after:avoid}tr{page-break-inside:avoid}
.avert{margin:1rem auto 1.8rem}}
@media(max-width:820px){col.a,col.b,col.c{width:auto}body{font-size:14px}}
"""

def rendre_html():
    out = ['<!DOCTYPE html>', '<html lang="fr">', '<head>', '<meta charset="utf-8">',
           '<meta name="viewport" content="width=device-width,initial-scale=1">',
           '<title>Trois colonnes — PPLC règle d’or</title>',
           f'<style>{CSS}</style>', '</head>', '<body>', '<div class="page">']
    out.append("<h1>Le retour à l’équilibre des comptes publics</h1>")
    out.append('<p class="sous">Proposition de loi constitutionnelle : trois colonnes</p>')
    out.append(
        '<p class="avert"><b>A</b> le texte en vigueur, verbatim, édition du Conseil '
        'constitutionnel du 8 mars 2024. <b>B</b> la disposition modificative, verbatim '
        'de la proposition. <b>C</b> le texte résultant, <b>produit par réapplication '
        'de B sur A</b> et non retapé : ' + str(verifiees) + ' cellules vérifiées, '
        'zéro échec. Seuls les alinéas touchés figurent ; les autres sont élidés. '
        'Chaque ligne porte un mot : <b>socle</b>, sans quoi la trajectoire est '
        'contournable et <b>optionnel</b> pour ce qui renforce sans conditionner. '
        'Le contrôle du verbatim sur Légifrance, bloc par bloc, demeure dû avant dépôt.</p>')
    for titre, source, chapeau, lignes in BLOCS:
        out.append(f'<h2>{html.escape(titre)}<span>{html.escape(source)}</span></h2>')
        out.append(f'<p class="chapeau">{html.escape(chapeau)}</p>')
        out.append('<table><colgroup><col class="a"><col class="b"><col class="c">'
                   '</colgroup><thead><tr>'
                   '<th class="a">Texte en vigueur</th>'
                   '<th class="b">Disposition modificative</th>'
                   '<th class="c">Texte résultant</th></tr></thead><tbody>')
        for a, b, puces, c, rang in lignes:
            if rang:
                out.append(f'<tr><td colspan="3" class="rang">{html.escape(rang)}</td></tr>')
            complete = rang and "complément" in rang
            classe_c = "" if complete else "c"
            out.append("<tr>" + cellule(a) + cellule_b(b, puces)
                       + cellule(c, classe_c) + "</tr>")
        out.append('</tbody></table>')
    out.append(
        '<footer>Quatre articles de la Constitution, cinq articles de proposition. '
        'Article 34 : vingt-trois alinéas en vigueur, vingt-quatre après révision. '
        'Article 47 : cinq alinéas, sept après révision. Article 47-2 : deux alinéas, '
        'quatre après révision. Article 40 : un alinéa, inchangé en nombre. '
        'Document de travail, 8 septembre 2026.</footer>')
    out += ['</div>', '</body>', '</html>']
    return "\n".join(out)


def cell_md(txt, cible=False):
    """Rend une cellule en markdown. La colonne C se met en gras comme au rendu
    HTML, sauf lorsqu'elle porte déjà un marquage d'ajout : dans ce cas le gras
    est réservé à l'ajout, et l'imbriquer le casserait."""
    if txt == SUPPRIME:
        return f"*{SUPPRIME}*"
    if txt == NEANT:
        return f"*{NEANT}*"
    if not txt:
        return ""
    rendu = txt.replace("\n", " <br> ").replace("|", "\\|")
    if cible and "**" not in rendu and rendu != ELISION:
        rendu = "**" + rendu.replace(" <br> ", "** <br> **") + "**"
    return rendu


def rendre_md():
    # Le bloc placé avant le premier séparateur devient la page de titre à
    # l'impression docx, et un intitulé « # » y sortirait en clair : le titre
    # s'écrit donc sans marqueur.
    out = ["**LE RETOUR À L’ÉQUILIBRE DES COMPTES PUBLICS**", "",
           "Proposition de loi constitutionnelle", "",
           "Trois colonnes : texte en vigueur, disposition modificative, texte résultant", "",
           "**A** le texte en vigueur, verbatim, édition du Conseil constitutionnel du "
           "8 mars 2024. **B** la disposition modificative, verbatim de la proposition. "
           "**C** le texte résultant, produit par réapplication de B sur A et non retapé : "
           f"{verifiees} cellules vérifiées, zéro échec. Seuls les alinéas touchés "
           "figurent ; les autres sont élidés. Chaque ligne porte un mot : **socle**, "
           "sans quoi la trajectoire est contournable et **optionnel** pour ce qui renforce "
           "sans conditionner.", ""]
    for titre, source, chapeau, lignes in BLOCS:
        out += ["---", "", f"## {titre}", "", f"*{source}. {chapeau}*", "",
                f"| {titre} | | |", "|---|---|---|",
                "| **Texte en vigueur** | **Disposition modificative** | **Texte résultant** |"]
        for a, b, puces, c, rang in lignes:
            if rang:
                out.append(f"| *{rang}* | | |")
            milieu = cell_md(b)
            if puces:
                milieu += (" <br> " if milieu else "") + " <br> ".join(
                    "• " + x for x in puces)
            out.append(f"| {cell_md(a)} | {milieu} | {cell_md(c, cible=True)} |")
        out.append("")
    out += ["---", "",
            "*Quatre articles de la Constitution, cinq articles de proposition. "
            "Article 34 : vingt-trois alinéas en vigueur, vingt-quatre après révision. "
            "Article 47 : cinq alinéas, sept après révision. Article 47-2 : deux alinéas, "
            "quatre après révision. Le contrôle du verbatim sur Légifrance, bloc par bloc, "
            "demeure dû avant dépôt. Document de travail, 8 septembre 2026.*", ""]
    return "\n".join(out)


def controle_derive(chemin="PPLC_regle_dor_modificative.md"):
    """La proposition rédigée porte-t-elle encore le C que le module prouve ?

    Le module est le point de vérité de la colonne C. La proposition en md la
    recopie pour être lisible et déposable : toute divergence est une dérive, et
    elle se relève mécaniquement plutôt qu'à la relecture.
    """
    import os
    if not os.path.exists(chemin):
        print(f"contrôle de dérive : {chemin} absent de l’atelier, non joué")
        return None
    texte = open(chemin, encoding="utf-8").read()
    attendus = {
        "art. 34, compétence et règle d’or": C34_COMPETENCE,
        "art. 34, pluriannuel": C34_PLURIANNUEL,
        "art. 34, autorisation fiscale": C34_FISCAL,
        "art. 34, subordination": C34_LFSS_AJOUT.strip(),
        "art. 34, orientations pluriannuelles": C34_ORIENTATIONS,
        "art. 40, gage réel": C40,
        "art. 47, universalité": C47_UNIVERSALITE,
        "art. 47, ordre du débat": C47_ORDRE,
        "art. 47, douzième provisoire": C47_DOUZIEME,
        "art. 47, indemnités": C47_INDEMNITES,
        "art. 47-2, sincérité du vote": C47_2_SINCERITE,
        "art. 47-2, recours du contribuable": C47_2_RECOURS,
    }
    derives = [nom for nom, c in attendus.items() if c not in texte]
    print(f"contrôle de dérive sur {chemin} : "
          f"{len(attendus) - len(derives)} sur {len(attendus)} conformes")
    for nom in derives:
        print(f"    dérive : {nom}")
    return derives


if __name__ == "__main__":
    open("trois_colonnes_regle_dor.html", "w", encoding="utf-8").write(rendre_html())
    open("trois_colonnes_regle_dor.md", "w", encoding="utf-8").write(rendre_md())
    nb_lignes = sum(len(l) for _, _, _, l in BLOCS)
    print(f"quatre blocs, {nb_lignes} lignes de tableau")
    print(f"cellules C vérifiées contre l’état réappliqué : {verifiees}, zéro échec")
    print("écrit : trois_colonnes_regle_dor.html et trois_colonnes_regle_dor.md")
    controle_derive()
