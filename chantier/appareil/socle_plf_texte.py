# -*- coding: utf-8 -*-
"""Socle du texte déposé — extraction déterministe, article par article.

**Un extracteur, deux profils de pièce.** Les repères d'un projet de loi sont
ceux d'une pièce et non d'une famille : le PLF 2026 n° 1906 et le PLFSS 2026
n° 1907 ne bornent pas leur section d'articles de la même façon, ne numérotent
pas leurs pages de la même façon, ne composent pas leurs têtes d'article de la
même façon et ne marquent pas leurs alinéas de la même façon. Le profil déclare
ces repères ; le code de découpage, la grammaire d'adresse, la liste fermée des
codes et les dix contrôles sont uniques. Voir `PROFILS`.


Ce que ce module rend, et rien d'autre (A-229) : une entrée par article du
projet de loi, portant son **numéro**, sa **partie**, son **titre**, sa
**rédaction exacte**, sa **page dans la pièce**, et **l'exposé des motifs qui
s'y rapporte**.

**L'exposé des motifs est indexé avec l'article et jamais confondu avec lui.**
Il est de l'indice, pas de la norme : il ne décrit pas les mesures, il les
raconte. Deux champs distincts, jamais fusionnés, et aucune adresse d'article
ouvert n'est jamais relevée depuis l'exposé des motifs.

**Déterminisme.** Même pièce, même script, même JSON, même SHA-256. Le module
appelle `pdftotext` lui-même avec des options figées, relève l'empreinte de la
pièce et la version de l'outil, et les porte au JSON : si la version de
`poppler` change, cela se voit au lieu de se deviner.

**Rien ne se recopie à la main.** Le texte est découpé de la sortie de
`pdftotext` et jamais retapé. Le seul verbatim que ce module porte en clair est
la liste des **repères** — quatre lignes de structure attendues dans la pièce,
et les formules modificatives du style SGG. Un repère qui ne se retrouve pas
**arrête la génération** (A-236) ; il ne se contourne pas.

Usage : python3 socle_plf_texte.py <pdf> <sortie.json> [profil]
        profil : `plf` par défaut, ou `plfss`.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

import vecteurs

# ---------------------------------------------------------------------------
# Les options de `pdftotext`, figées. `-layout` parce que la mise en page porte
# l'information sur les tableaux — états, plafonds d'emplois, tableau
# d'équilibre. `-eol unix` et `-enc UTF-8` pour que l'octet ne dépende pas de la
# plateforme.
PDFTOTEXT = ('pdftotext', '-layout', '-enc', 'UTF-8', '-eol', 'unix')

# ---------------------------------------------------------------------------
# LES PROFILS DE PIÈCE
#
# Les repères de structure sont ceux d'une **pièce**, pas d'une famille. Le PLF
# borne sa section d'articles par un titre de section, numérote ses pages
# « 12 Projet de loi de finances », compose ses têtes d'article « ARTICLE 12 : »
# et marque ses alinéas « (3) ». Le PLFSS n° 1907 ne fait aucune de ces quatre
# choses de la même façon. Ce ne sont pas deux extracteurs : c'est un extracteur
# et deux profils, parce qu'une seconde grammaire d'adresse ferait un second
# point de vérité et la jointure avec `REF_norme` ne tomberait plus.
#
# Ce qu'un profil déclare, et rien d'autre : les repères. Le découpage, la
# séparation modifie/cite, la coupe à la formule modificative, le masquage des
# guillemets, le chapeau sans verbe, la liste fermée des codes et les dix
# contrôles sont communs et ne se dupliquent pas.
#
# **Un repère qui ne se retrouve pas arrête la génération** (A-236). Il ne se
# contourne pas, il ne se devine pas, et aucun profil ne s'applique par défaut à
# une pièce qui ne porte pas ses repères.

# --- PLF ---------------------------------------------------------------------
REPERE_DEBUT = 'Articles du projet de loi avec exposé des motifs'
REPERE_FIN = 'États législatifs annexés'

# L'en-tête de page, sur ses deux formes — page paire et page impaire. C'est
# aussi ce qui donne le numéro de page imprimé, qu'on confronte au numéro
# physique plutôt que de supposer qu'ils coïncident.
ENTETE = re.compile(r'^\s*(?:(\d+)\s+Projet de loi de finances'
                    r'|Projet de loi de finances\s+(\d+))\s*$')

# La tête d'article. Le deux-points en fin de ligne est ce qui la distingue des
# lignes du sommaire, qui portent le titre et le numéro de page sur la même
# ligne.
TETE_ARTICLE = re.compile(r'^ARTICLE\s+(liminaire|\d+)\s*:\s*$')

TETE_MOTIFS = 'Exposé des motifs'

# La tête d'alinéa telle que la pièce la compose : le numéro entre parenthèses,
# en colonne de gauche, suivi d'au moins deux espaces.
TETE_ALINEA = re.compile(r'^\s*\((\d+)\)\s{2,}(\S.*)$')

# La tête d'une division de structure, attendue **seule sur sa ligne**. Le
# relevé des divisions balaie désormais l'intérieur d'un article — il le doit,
# puisque sur le PLFSS une division s'ouvre en milieu de page —, et une
# expression qui se contenterait d'un début de ligne prendrait « titre de
# l'assurance vieillesse… » pour un titre de division. Le plein-ligne est ce qui
# rend le balayage sûr.
# La queue d'intitulé, corrigée le 20260902 sur relevé de la pièce (A-294).
#
# Le PLF 1906 compose la tête **et son intitulé sur la même ligne**, séparés par
# le deux-points de la pièce : « PREMIÈRE PARTIE : CONDITIONS GÉNÉRALES DE
# L'ÉQUILIBRE FINANCIER ». Le PLFSS 1907 pose la tête seule et son intitulé au
# bloc suivant. Les deux formes se relèvent donc, et le deux-points est celui de
# la pièce — jamais une ponctuation de notre cru.
#
# Le balayage de la zone d'extraction du PLF pour toute ligne portant « PARTIE »
# ou « TITRE » rend **six lignes, et six seulement** ; celui du PLFSS en rend
# sept. La queue est optionnelle et exige le deux-points : elle ne peut donc pas
# attraper une phrase, et le plein-ligne reste ce qui borne le motif.
#
# Ce que le relevé a écarté : « TITRE Ier » en bas de casse n'est pas la cause.
# Le PLF écrit « TITRE PREMIER » et « TITRE II », en capitales, que le motif
# acceptait déjà. Le « IER » en capitales est au PLFSS, où le profil marchait.
# Ce que le relevé a ajouté : page 210, « TITRE II: » sans espace avant le
# deux-points. D'où `\s*:` et non `\s+:`.
QUEUE_INTITULE = r'(?:\s*:\s*(\S.*))?$'
DIVISION_PARTIE = re.compile(
    r'^(?:PREMIÈRE|DEUXIÈME|TROISIÈME|QUATRIÈME|SECONDE)\s+PARTIE'
    + QUEUE_INTITULE)
DIVISION_TITRE = re.compile(r'^TITRE\s+(?:[IVXLC]+(?:ER)?|PREMIER)'
                            + QUEUE_INTITULE)


def tete_division(prof, s):
    """(tête, intitulé, rang) d'une ligne ou d'un bloc de division, ou None.

    `rang` vaut `'partie'` ou `'titre'`. L'intitulé est celui que la pièce
    accole à la tête sur la même ligne, et vaut `None` quand la pièce le pose
    au bloc suivant — auquel cas le mécanisme d'attente de `construire` le
    reprend. La tête rendue est **tronquée à ce qu'elle est** : « PREMIÈRE
    PARTIE », pas « PREMIÈRE PARTIE : CONDITIONS… ».
    """
    for cle, rang in (('division_partie', 'partie'),
                      ('division_titre', 'titre')):
        m = prof[cle].match(s)
        if m:
            intitule = m.group(1)
            tete = s[:m.start(1)].rstrip() if intitule is not None else s
            return tete.rstrip(' :').rstrip(), intitule, rang
    return None

# --- PLFSS -------------------------------------------------------------------
# Repères relevés sur la pièce le 20260901, PLFSS 2026 n° 1907, 162 pages,
# SHA-256 0660a073…, et non repris d'une lecture de page web.
#
# Ce que la pièce fait autrement que le PLF, point par point :
#
#   — **elle ne porte aucun sommaire**, donc aucun titre de section qui borne
#     les articles. La borne de début est la dernière ligne du décret de
#     présentation, « Décrète : », qui ne paraît qu'une fois ; la borne de fin
#     est « ANNEXE », p. 151, qui ouvre le rapport annexé ;
#   — **son en-tête de page est le seul numéro**, entre deux tirets demi-cadratin
#     — « – 42 – », parfois « –7– » sans espace ;
#   — **sa tête d'article ne porte pas de deux-points** et s'écrit en bas de
#     casse : « Article liminaire », « Article 1er », « Article 2 ». Faute de
#     sommaire, rien ne peut la confondre avec une ligne de sommaire ;
#   — **elle ne numérote pas ses alinéas en clair.** C'est une version
#     *pastillée* : chaque alinéa s'ouvre par une pastille composée dans une
#     police symbole, que `pdftotext` rend en zone à usage privé. Voir
#     `PASTILLE` plus bas ;
#   — **une tête d'article n'ouvre pas nécessairement une page** : six pages en
#     portent deux, une en porte trois. L'hypothèse qui tient sur le PLF ne tient
#     pas ici, et le découpage a été reprise plutôt que forcée.
REPERE_DEBUT_PLFSS = 'Décrète :'
REPERE_FIN_PLFSS = 'ANNEXE'
ENTETE_PLFSS = re.compile(r'^\s*[–—-]\s*(\d+)\s*[–—-]\s*$')
TETE_ARTICLE_PLFSS = re.compile(r'^Article\s+(liminaire|\d+(?:er)?)\s*$')

# ---------------------------------------------------------------------------
# LA PASTILLE, ET SON ALPHABET FERMÉ
#
# La pièce pastillée numérote ses alinéas par un glyphe de police symbole, que
# `pdftotext` rend en U+F000–U+F0FF. Le codet vaut U+F000 + le code ASCII du
# caractère que la police dessine ; l'alphabet est positionnel et fermé :
#
#     seule                L M N O P Q R S T          →   1 … 9
#     en tête              1 … 9                      →   1 … 9   (dizaines,
#                                                          centaines…)
#     au milieu            A B C D E F G H I J        →   0 … 9
#     en queue             a b c d e f g h i j        →   0 … 9
#
# Relevé sur la pièce : « 1a » vaut 10, « 2j » vaut 29, « 1Aa » vaut 100.
#
# **Ce n'est pas une interprétation, c'est une lecture qui se prouve** : les
# 1 060 pastilles de la section des articles se décodent en 55 suites
# strictement continues de 1 à N, une par article, sans trou ni doublon. Un
# jeton que l'alphabet ne couvre pas arrête la génération (A-236) ; une suite
# rompue la fait arrêter aussi, plutôt que de livrer une numérotation inventée.
# Le glyphe s'écrit en échappement et jamais en clair : un module qui
# porterait des caractères de zone privée en verbatim serait illisible, et un
# copier-coller les perdrait en silence.
PASTILLE = re.compile(r'^([\uF000-\uF0FF]+)(?:(\s.*)|$)')
_PAST_SEULE = {chr(ord('L') + i): i + 1 for i in range(9)}
_PAST_TETE = {str(i): i for i in range(1, 10)}
_PAST_MILIEU = {chr(ord('A') + i): i for i in range(10)}
_PAST_QUEUE = {chr(ord('a') + i): i for i in range(10)}


def pastille_valeur(jeton):
    """Le numéro d'alinéa qu'une pastille porte, ou `None` si l'alphabet ne le
    couvre pas. Le jeton est déjà ramené de la zone privée à l'ASCII."""
    if len(jeton) == 1:
        return _PAST_SEULE.get(jeton)
    if jeton[0] not in _PAST_TETE or jeton[-1] not in _PAST_QUEUE:
        return None
    v = _PAST_TETE[jeton[0]]
    for c in jeton[1:-1]:
        if c not in _PAST_MILIEU:
            return None
        v = v * 10 + _PAST_MILIEU[c]
    return v * 10 + _PAST_QUEUE[jeton[-1]]


def pastille_de(ligne):
    """(numéro, reste de la ligne) si la ligne s'ouvre par une pastille."""
    m = PASTILLE.match(ligne)
    if not m:
        return None, None
    jeton = ''.join(chr(ord(c) - 0xF000) for c in m.group(1))
    v = pastille_valeur(jeton)
    if v is None:
        raise SystemExit(
            f'pastille hors alphabet : « {jeton} ». La génération s’arrête '
            'plutôt que de numéroter au hasard.')
    return v, (m.group(2) or '').strip()


# ---------------------------------------------------------------------------
PROFILS = {
    'plf': dict(
        nom='plf',
        piece='PLF 2026 n° 1906',
        role='socle du texte déposé — PLF 2026 n° 1906',
        repere_debut=REPERE_DEBUT,
        repere_fin=REPERE_FIN,
        entete=ENTETE,
        tete_article=TETE_ARTICLE,
        tete_motifs=TETE_MOTIFS,
        alinea='marque',
        tete_alinea=TETE_ALINEA,
        alinea_unique_sans_marque=False,
        # « ARTICLE 12 : » puis son intitulé sur les lignes qui suivent.
        titre_article=True,
        division_partie=DIVISION_PARTIE,
        division_titre=DIVISION_TITRE,
        # Six, relevées sur la pièce le 20260902 et non héritées : première et
        # seconde partie, deux titres par partie. Le balayage de la zone
        # d'extraction pour toute ligne portant « PARTIE » ou « TITRE » en rend
        # six, et six seulement. L'épinglage à 0 était un défaut de repère
        # présumé, jamais une propriété de la pièce (A-294) ; il est levé.
        #
        # Ce que la pièce fait et que le PLFSS ne fait pas : la tête et son
        # intitulé tiennent sur la même ligne, séparés par le deux-points de la
        # pièce. Voir `QUEUE_INTITULE`.
        #
        # **L'article liminaire ne porte aucune division, et c'est juste** : il
        # est page 31, la première partie ouvre page 34. Il précède la première
        # partie, comme au PLFSS. Les 81 autres articles portent leur partie et
        # leur titre.
        #
        # Historique de l'épinglage, laissé pour mémoire :
        #
        # Ce qui est établi : DIVISION_PARTIE et DIVISION_TITRE, écrits sur la
        # composition du PLFSS, n'ont rien mordu sur le PLF 1906. Ce qui ne
        # l'est pas, et que ce commentaire affirmait à tort : que la pièce ne
        # porte aucune tête de division. Un projet de loi de finances porte une
        # première et une seconde partie, et des titres — l'auteur l'a relevé.
        # L'épinglage à 0 fige donc un **défaut de repère présumé**, pas une
        # propriété de la pièce.
        #
        # Deux causes candidates, non tranchées faute de la pièce au dépôt :
        # DIVISION_TITRE exige des chiffres romains en capitales et rejette
        # « TITRE Ier », dont le « er » est en bas de casse ; et les deux
        # expressions exigent la ligne pleine, qu'une tête composée avec son
        # intitulé sur la même ligne ne donne pas. Le départage est mécanique
        # et tient en une passe : balayer la région d'extraction pour toute
        # ligne contenant « PARTIE » ou « TITRE ». Il demande le PDF.
        #
        # Tant que ce n'est pas tranché, ce profil ne remonte ni partie ni titre
        # aux articles. Toute apparition future arrête la génération (A-236), ce
        # qui est le but de l'épinglage.
        divisions_attendues=6,
        sommaire=True,
    ),
    'plfss': dict(
        nom='plfss',
        piece='PLFSS 2026 n° 1907',
        role='socle du texte déposé — PLFSS 2026 n° 1907',
        repere_debut=REPERE_DEBUT_PLFSS,
        repere_fin=REPERE_FIN_PLFSS,
        entete=ENTETE_PLFSS,
        tete_article=TETE_ARTICLE_PLFSS,
        tete_motifs=TETE_MOTIFS,
        alinea='pastille',
        tete_alinea=None,
        # La pièce ne titre pas ses articles, et n'a pas de sommaire où les
        # lister. « Article 17 » est suivi directement de la disposition.
        titre_article=False,
        # Dix articles de la pièce ne portent aucune pastille : ce sont ceux
        # qui n'ont qu'un alinéa — la pièce ne pastille qu'à partir de deux.
        # Relevé et recompté sur le socle, pas supposé : articles 3, 13, 17,
        # 23, 25, 48, 51, 52, 53 et 54. Le compte boucle : 1 060 pastilles
        # relevées aux rédactions, plus dix alinéas uniques, font les 1 070
        # alinéas du socle.
        alinea_unique_sans_marque=True,
        division_partie=DIVISION_PARTIE,
        division_titre=DIVISION_TITRE,
        divisions_attendues=7,
        sommaire=False,
    ),
}


def profil_de(nom):
    if nom not in PROFILS:
        raise SystemExit(f'profil de pièce inconnu : « {nom} ». '
                         f'Connus : {", ".join(sorted(PROFILS))}.')
    return PROFILS[nom]


# ---------------------------------------------------------------------------
# Les formules modificatives du style SGG. Liste fermée : une formule absente
# d'ici fait sortir la référence en `cite` plutôt que de passer pour une
# modification. On préfère manquer une ouverture que d'en inventer une — un
# article ouvert qui ne l'est pas envoie l'amendement au mauvais endroit
# (A-245).
FORMULES_MODIFICATIVES = (
    'est ainsi modifié', 'est ainsi modifiée',
    'sont ainsi modifiés', 'sont ainsi modifiées',
    'est abrogé', 'est abrogée', 'sont abrogés', 'sont abrogées',
    'est ainsi rédigé', 'est ainsi rédigée',
    'sont ainsi rédigés', 'sont ainsi rédigées',
    'est complété', 'est complétée', 'sont complétés', 'sont complétées',
    'est remplacé', 'est remplacée', 'sont remplacés', 'sont remplacées',
    'est supprimé', 'est supprimée', 'sont supprimés', 'sont supprimées',
    'est ainsi rétabli', 'est ainsi rétablie',
    'il est inséré', 'il est ajouté', 'sont insérés', 'sont insérées',
    'est inséré', 'est insérée', 'est ajouté', 'est ajoutée',
    'est créé', 'est créée', 'sont créés',
)

# Le chapeau qui ouvre un bloc modificatif : « Le code général des impôts est
# ainsi modifié : ». Il nomme le texte que les sous-items héritent, puisqu'ils
# ne le répètent pas — « 1° L’article 39 AH est abrogé ; ».
CHAPEAU = re.compile(
    r'(?:est|sont)\s+(?:ainsi\s+modifi[ée]e?s?'
    r'|modifi[ée]e?s?\s+ainsi\s+qu[’\']il\s+suit)\s*[:;]\s*$')

# Les marqueurs d'énumération légistique, qui se cumulent : « I. – A. – ».
# On les retire un par un plutôt que d'écrire une expression qui les devine.
PREFIXE_ENUM = re.compile(
    r'^\s*(?:[IVXLC]+|[A-Z]|[a-z]|\d+)\s*(?:°|\)|\.)\s*(?:[–—-]\s*)?')

# ---------------------------------------------------------------------------
# Les codes, en liste fermée.
#
# **Le code ne se devine pas.** A-250 a coûté 55 entrées fausses parce qu'une
# règle affirmait « code général des impôts » sur une numérotation nue. Ici le
# code est celui que la pièce nomme, et on ne le retient que s'il figure à
# cette liste — relevée en balayant la pièce, et bornée. Un nom absent d'ici
# sort en `indéterminé` et se compte, il ne se rapproche pas du plus proche.
#
# Les noms sont écrits avec l'apostrophe droite ; la comparaison normalise
# l'apostrophe typographique de la pièce.
CODES = (
    'code général des impôts',
    'code général des collectivités territoriales',
    'code des impositions sur les biens et services',
    "code des douanes de l'Union",
    'code des douanes',
    "code de l'environnement",
    "code de l'énergie",
    "code de l'urbanisme",
    "code de l'entrée et du séjour des étrangers et du droit d'asile",
    'code de la santé publique',
    'code de la sécurité sociale',
    'code de la construction et de la habitation',
    "code de la construction et de l'habitation",
    'code de la commande publique',
    'code de la consommation',
    'code de la recherche',
    'code de la route',
    'code de la voirie routière',
    'code de commerce',
    'code de procédure pénale',
    'code des assurances',
    'code des transports',
    'code des relations entre le public et administration',
    "code des relations entre le public et l'administration",
    'code du travail',
    'code rural et de la pêche maritime',
    "code du cinéma et de l'image animée",
    'livre des procédures fiscales',
    # Relevés sur le PLFSS 2026 n° 1907 le 20260901, par balayage de tous les
    # noms de texte que la pièce introduit — « du / de la / de l' » suivi de
    # « code » ou « livre des ». Chacun est un nom que la pièce écrit ; aucun
    # n'est ajouté par anticipation, et la liste reste fermée (A-250).
    "code de l'action sociale et des familles",
    'code des pensions civiles et militaires de retraite',
    'code des pensions civiles et militaires',
    'code général de la fonction publique',
    'code général de la propriété des personnes publiques',
    "code de l'organisation judiciaire",
    'code monétaire et financier',
    "code de l'éducation",
    'code du tourisme',
    "code des procédures civiles d'exécution",
    'code de la sécurité intérieure',
    # Relevés au second balayage, celui des chapeaux — « Le code X est ainsi
    # modifié : ». Le premier balayage ne prenait que les noms introduits par
    # « du / de la / de l' » et manquait ceux qu'un chapeau annonce.
    'code de la défense',
    'code civil',
)
CODE_INDETERMINE = 'indéterminé'

# Un texte non codifié : la loi ou l'ordonnance elle-même est le vecteur. On
# retient le numéro et la date, qui l'identifient sans ambiguïté.
TEXTE_NON_CODIFIE = re.compile(
    r'\b(loi organique|loi|ordonnance|décret)\s+n[°o]\s*(\d+[\-‑]\d+)'
    r'\s+du\s+(\d{1,2}(?:er)?\s+\w+\s+\d{4})', re.I)

# Un texte qu'une loi de finances française ne modifie pas : traité, règlement
# ou directive de l'Union. Une référence qui y renvoie est une citation, quoi
# que porte la phrase.
TEXTE_ETRANGER = re.compile(r'^(?:règlement|traité|directive)\b', re.I)

# Ce qui, après une référence, annonce un texte : si le mot qui suit est de
# cette famille et que le nom n'est pas reconnu, la référence sort en
# `indéterminé`. **Elle n'hérite pas du chapeau** — hériter d'un code qui n'est
# pas le bon fabrique une adresse fausse, et c'est la faute d'A-250.
INTRODUCTEUR = re.compile(
    r'^(?:code|livre\s+des|loi|ordonnance|décret|règlement|traité|directive'
    r'|charte)\b', re.I)

# Le renvoi au texte déjà nommé : il hérite, et c'est régulier.
RENVOI = re.compile(r'^(?:m[êe]me|présent|dit|ledit|dudit)\b', re.I)

# Le chapeau annonce un texte, article défini compris : « Le code … », « La loi
# … ». Sert à distinguer un chapeau dont le nom de texte n'est pas reconnu — qui
# doit couper l'héritage — d'un chapeau qui ne nomme aucun texte, et pour lequel
# l'héritage reste régulier.
ARTICLE_DEFINI_PUIS_TEXTE = re.compile(
    r"^(?:l[ea]s?\s+|l'\s*)?"
    r'(?:code|livre\s+des|loi|ordonnance|décret)\b', re.I)

# Le siège — livre, titre, chapitre, section — quand le chapeau le nomme.
SIEGE = re.compile(r'^((?:le\s+|la\s+)?(?:livre|titre|chapitre|section|'
                   r'sous-section|paragraphe)\b.*?)\s+du\s+(code\b.*)$', re.I)

# La référence à un article, dans le texte de la disposition.
#
# On ne balaie pas de la prose : on reconnaît une **suite de numéros
# d'articles**, liés par la virgule, « et », « ou » ou « à ». La grammaire du
# numéro est celle de `ref_norme` — lettre de partie bornée à L, R, D, ordinal
# latin de la liste fermée de `vecteurs.ORDINAUX`, suffixe de lettre. Ce qui
# n'entre pas dans cette grammaire n'est pas relevé, plutôt que d'être deviné.
# Les ordinaux sont rangés du plus long au plus court : une alternance qui
# essaie « ter » avant « terdecies » coupe « 199 terdecies-0 A bis » en
# « 199 ter », et une adresse tronquée est une fausse adresse.
_ORDINAUX = '|'.join(sorted(vecteurs.ORDINAUX, key=len, reverse=True))

# Le suffixe se répète : « 235 ter ZD », « 220 Z octies », « 1518 A quinquies
# A », « 278 sexies-0 A ». Un bloc de capitales n'est retenu que s'il n'est pas
# suivi d'une minuscule collée — « Au » ne se lit pas comme le suffixe « A ».
#
# **Cette grammaire est plus large que celle de `ref_norme`**, qui borne le
# suffixe à une lettre de A à H parce que l'annexe des dépenses fiscales n'en
# porte pas d'autre. Sur la pièce, elle produit dix suffixes que `ref_norme`
# tronquerait — 235 ter ZD, 223 WT, L. 47 AB, 1518 A quinquies A. L'écart est
# compté et déclaré plutôt que d'être absorbé.
# Le bloc de capitales se lit **sensible à la casse** — `(?-i:…)` — bien que le
# reste de l'expression ignore la casse : sans cela « 224 du code » se lirait
# « article 224 du », le « du » passant pour un suffixe.
_SUFFIXE = (r'(?:\s+(?:' + _ORDINAUX + r')'
            r'|\s+(?-i:[A-Z]{1,3})(?![a-zà-ÿ])'
            r'|-\d+)')
_NUM = r'(?:[LRD]\.?\s*)?\d+(?:-\d+)*' + _SUFFIXE + r'*'
REFERENCE = re.compile(
    r'\barticles?\s+(' + _NUM
    + r'(?:\s*(?:,|\bet\b|\bou\b|\bà\b)\s*' + _NUM + r')*)',
    re.I)

# La fourchette : « les articles L. 3515-6-2 à L. 3515-6-13 ». La pièce ne
# nomme pas les articles intermédiaires, et on ne les invente pas : l'adresse
# se garde en fourchette, et se déclare comme telle.
FOURCHETTE = re.compile(r'\s+à\s+', re.I)

# Un alinéa de texte inséré s'ouvre par un guillemet français : ce qu'il cite
# n'est jamais ce qu'il modifie.
CITATION = re.compile(r'^\s*[«"]')

# Ce qui, dans une phrase, ouvre une citation plutôt qu'une cible. « A l'article
# L. 322-56, dans sa rédaction issue du 1° du I de l'article 18 de la loi
# n° 2025-127 » modifie le premier et cite le second. Liste fermée.
MARQUEURS_CITATION = (
    'dans sa rédaction', 'dans leur rédaction', 'mentionné', 'mentionnée',
    'mentionnés', 'mentionnées', 'prévu', 'prévue', 'prévus', 'prévues',
    'défini', 'définie', 'définis', 'définies', 'au sens de', 'visé', 'visée',
    'visés', 'visées', 'issu', 'issue', 'résultant', 'en application',
    'conformément', 'régi', 'régie', 'régis', 'relevant',
)

# Le chapeau qui pose la cible sans porter de verbe : « A l'article 81 : ». Les
# sous-items qui suivent modifient cet article ; sans cette forme, 77 chapeaux
# de la pièce passeraient pour de simples citations.
CHAPEAU_CIBLE = re.compile(r':\s*$')


# Le rang d'une division, qui dit ce qu'elle chasse. Une division de rang 1
# — « II – AUTRES MESURES » — remplace la précédente de rang 1 et vide les
# rangs inférieurs ; elle ne s'y ajoute pas.
RANG_1 = re.compile(r'^[IVXLC]+\s*[.\u2013\u2014-]')
RANG_2 = re.compile(r'^[A-Z]\s*[.\u2013\u2014-]')


def _rang_division(d):
    if RANG_1.match(d):
        return 1
    if RANG_2.match(d):
        return 2
    return 3


def _sha256(chemin):
    h = hashlib.sha256()
    with open(chemin, 'rb') as f:
        for bloc in iter(lambda: f.read(1 << 20), b''):
            h.update(bloc)
    return h.hexdigest()


def _version_outil():
    """La version de `pdftotext`, portée au JSON. Elle fait partie du procédé."""
    try:
        p = subprocess.run(['pdftotext', '-v'], capture_output=True, text=True)
        ligne = (p.stderr or p.stdout).strip().split('\n')[0]
        return ligne.strip()
    except OSError:
        return 'inconnue'


def texte_de(pdf):
    """La pièce, en texte, par un appel figé. Aucune lecture page à page."""
    p = subprocess.run(list(PDFTOTEXT) + [pdf, '-'],
                       capture_output=True)
    if p.returncode != 0:
        raise SystemExit('pdftotext a échoué : '
                         + p.stderr.decode('utf-8', 'replace')[:400])
    return p.stdout.decode('utf-8')


def pages_de(texte, prof=None):
    """Les pages, avec leur en-tête retiré et leur numéro imprimé relevé.

    Rend une liste de dicts : `physique`, `imprimee`, `lignes`.
    """
    prof = prof or PROFILS['plf']
    entete = prof['entete']
    # `pdftotext` clôt sa sortie par un saut de page, ce qui produit un dernier
    # morceau vide. Le compter ferait dire au socle 163 pages là où la pièce en
    # porte 162, et un chiffre faux dans un référentiel ne se rattrape pas plus
    # bas. On l'écarte s'il est vide, jamais s'il porte du texte.
    morceaux = texte.split('\f')
    if morceaux and not morceaux[-1].strip():
        morceaux.pop()
    out = []
    for i, brut in enumerate(morceaux):
        lignes = [l.rstrip() for l in brut.split('\n')]
        imprimee = None
        for j, l in enumerate(lignes):
            if not l.strip():
                continue
            m = entete.match(l)
            if m:
                imprimee = int(next(g for g in m.groups() if g))
                lignes = lignes[j + 1:]
            else:
                lignes = lignes[j:]
            break
        out.append(dict(physique=i + 1, imprimee=imprimee, lignes=lignes))
    return out


def _borne(pages, repere):
    """La page où un repère se retrouve littéralement, seul sur sa ligne."""
    trouves = [p['physique'] for p in pages
               if any(l.strip() == repere for l in p['lignes'])]
    if not trouves:
        raise SystemExit(f'repère introuvable dans la pièce : « {repere} ». '
                         "La génération s'arrête plutôt que de deviner.")
    return trouves[0]


def joindre(morceaux):
    """Recolle des lignes en une phrase, sans fabriquer d'espace parasite.

    Une ligne qui finit par un trait d'union porte un composé coupé par la mise
    en page — « Nouvelle- » puis « Calédonie ». On recolle sans espace ; le
    sommaire de la pièce, qui compose le même titre sur une seule ligne, sert
    de contrôle (S3).
    """
    out = ''
    for m in morceaux:
        m = m.strip()
        if not m:
            continue
        if not out:
            out = m
        elif out.endswith('-'):
            out += m
        else:
            out += ' ' + m
    return re.sub(r'\s+', ' ', out).strip()


def _bloc_titre(lignes, k):
    """Le titre d'un article : les lignes pleines qui suivent sa tête."""
    titre = []
    j = k + 1
    while j < len(lignes) and lignes[j].strip():
        titre.append(lignes[j].strip())
        j += 1
    return joindre(titre), j


def _blocs(lignes):
    """Des lignes regroupées en blocs séparés par une ligne vide, verbatim."""
    blocs, courant = [], []
    for l in lignes:
        if l.strip():
            courant.append(l.strip())
        elif courant:
            blocs.append(' '.join(courant))
            courant = []
    if courant:
        blocs.append(' '.join(courant))
    return blocs


def decouper(pages, p_debut, p_fin, prof=None):
    """Les articles, leurs pages, leur rédaction et leur exposé des motifs.

    **Un article court de sa tête à la tête suivante, position par position.**

    La première version coupait à la page : un article s'arrêtait à la page qui
    précède celle de la tête suivante. Cela tenait sur le PLF, où toute tête
    d'article ouvre une page — et cela ne tient pas sur le PLFSS 2026, où six
    pages portent deux têtes et une en porte trois. Cinq articles en sortaient
    avec une rédaction vide.

    Le découpage a donc été **repris et non forcé** : les lignes de la section
    forment une nappe, les têtes s'y repèrent par leur position, et un article
    court d'une tête à la suivante. Sur une pièce où chaque tête ouvre une page,
    les deux découpages rendent le même résultat.

    **Une division de structure se retire de l'article qui la précède.** Elle ne
    vit pas nécessairement en haut d'une page : sur le PLFSS, « DEUXIÈME PARTIE »
    s'ouvre en milieu de page 42, après l'exposé des motifs de l'article 17 et
    avant la tête de l'article 18. La région de division court donc du premier
    repère de division rencontré dans l'étendue d'un article jusqu'à la tête
    suivante, et elle est attribuée à l'article qui suit, jamais à celui qui
    précède. Le repère est attendu **seul sur sa ligne**, faute de quoi une
    phrase qui s'ouvre par « titre de… » passerait pour une division.
    """
    prof = prof or PROFILS['plf']
    tete_re = prof['tete_article']
    tete_motifs = prof['tete_motifs']
    est_division = (lambda s: tete_division(prof, s) is not None)

    # 1. La nappe des lignes de la section, chacune avec sa page.
    nappe = []
    for p in pages[p_debut - 1:p_fin]:
        for l in p['lignes']:
            nappe.append((p['physique'], l))

    # 2. Les têtes, par position dans la nappe.
    tetes = []
    for k, (page, l) in enumerate(nappe):
        m = tete_re.match(l.strip())
        if m:
            tetes.append(dict(numero=m.group(1), page=page, pos=k))
    if not tetes:
        raise SystemExit(
            'aucune tête d’article trouvée avec le profil '
            f'« {prof["nom"]} ». La génération s’arrête plutôt que de deviner '
            'une autre forme de tête.')

    # 3. Les régions de division, retirées des étendues qu'elles closent.
    #    `pending[i]` porte les blocs de division qui précèdent la tête i.
    pending = {0: []}
    fins = {}
    for i, t in enumerate(tetes):
        deb = t['pos'] + 1
        fin = tetes[i + 1]['pos'] if i + 1 < len(tetes) else len(nappe)
        coupe = None
        for k in range(deb, fin):
            if est_division(nappe[k][1].strip()):
                coupe = k
                break
        fins[i] = coupe if coupe is not None else fin
        if coupe is not None:
            pending[i + 1] = _blocs([l for _, l in nappe[coupe:fin]])
        else:
            pending.setdefault(i + 1, [])
    # Ce qui précède la première tête est de la structure aussi.
    pending[0] = _blocs([l for _, l in nappe[:tetes[0]['pos']]])

    divisions = []
    for i, t in enumerate(tetes):
        for b in pending.get(i, []):
            divisions.append(dict(intitule=b, page=t['page']))

    # 4. Le découpage.
    articles = []
    for i, t in enumerate(tetes):
        lignes = list(nappe[t['pos']:fins[i]])
        brut = [l for _, l in lignes]
        if prof['titre_article']:
            titre, j = _bloc_titre(brut, 0)
        else:
            # La pièce ne titre pas ses articles : « Article 17 » est suivi
            # directement de la disposition, parfois sans même une ligne vide.
            # Prendre un titre ici mangerait le premier alinéa — c'est ce qui
            # arrivait aux articles 13, 17, 23, 25, 48, 51, 52 et 53.
            titre, j = '', 1
        idx = [k for k in range(j, len(brut))
               if brut[k].strip() == tete_motifs]
        if len(idx) != 1:
            raise SystemExit(
                f"article {t['numero']} : {len(idx)} occurrence(s) de "
                f'« {tete_motifs} », une et une seule est attendue.')
        k = idx[0]
        articles.append(dict(
            numero=t['numero'],
            titre=titre,
            page_debut=t['page'],
            page_fin=lignes[-1][0] if lignes else t['page'],
            divisions=list(pending.get(i, [])),
            redaction=lignes[j:k],
            motifs=lignes[k + 1:],
        ))
    return articles, divisions


def _nettoyer(lignes):
    """Un bloc de lignes, débarrassé de ses lignes vides de tête et de queue."""
    out = list(lignes)
    while out and not out[0][1].strip():
        out.pop(0)
    while out and not out[-1][1].strip():
        out.pop()
    return out


def alineas_de(lignes, prof=None):
    """Les alinéas numérotés, et ce qui n'en est pas.

    Deux marques, une seule mécanique. Le profil dit laquelle la pièce emploie.

    **`marque`** — le PLF numérote ses alinéas en clair, `(3)`. Un alinéa court
    de sa tête à la tête suivante ou à la première ligne vide ; ce qui ne se
    rattache à aucun — les tableaux — sort en `hors_alinea`, avec sa page,
    parce que la mise en page y porte l'information.

    **`pastille`** — le PLFSS les numérote par une pastille de police symbole.
    La pastille est une borne franche : l'alinéa court d'une pastille à la
    suivante, **et une ligne vide ne le ferme pas**. Mesuré sur la pièce : 42
    des 1 060 alinéas portent du texte après une ligne vide — une coupure de
    page, ou un tableau —, et fermer sur la ligne vide les aurait tronqués,
    donc aurait perdu les adresses que leur queue porte.

    Un alinéa dont la pastille est **seule sur sa ligne** ouvre un tableau : la
    pièce en porte huit dans la section des articles. Il se marque, et ses
    lignes restent brutes.

    Une rédaction sans aucune pastille est **un alinéa unique**, quand le profil
    le déclare : la pièce ne pastille qu'à partir de deux alinéas.
    """
    prof = prof or PROFILS['plf']
    if prof['alinea'] == 'marque':
        return _alineas_marque(lignes, prof['tete_alinea'])
    return _alineas_pastille(lignes, prof)


def _prose(morceaux):
    """Le remplissage que `-layout` insère entre les mots est de la mise en
    page, pas du texte."""
    return re.sub(r'\s+', ' ', ' '.join(morceaux)).strip()


def _alineas_marque(lignes, tete):
    out, hors = [], []
    courant = None
    for page, l in lignes:
        m = tete.match(l)
        if m:
            if courant:
                out.append(courant)
            courant = dict(numero=int(m.group(1)), page=page,
                           lignes=[m.group(2).rstrip()], tableau=False)
        elif courant is not None:
            if l.strip():
                courant['lignes'].append(l.strip())
            else:
                out.append(courant)
                courant = None
        elif l.strip():
            hors.append(dict(page=page, ligne=l))
    if courant:
        out.append(courant)
    for a in out:
        a['texte'] = _prose(a.pop('lignes'))
    return out, hors


def _alineas_pastille(lignes, prof):
    out, hors = [], []
    courant = None
    for page, l in lignes:
        numero, reste = pastille_de(l)
        if numero is not None:
            if courant:
                out.append(courant)
            courant = dict(numero=numero, page=page,
                           lignes=[reste] if reste else [],
                           tableau=not reste)
        elif courant is not None:
            if l.strip():
                courant['lignes'].append(l.strip())
        elif l.strip():
            hors.append(dict(page=page, ligne=l))
    if courant:
        out.append(courant)
    if not out and prof['alinea_unique_sans_marque']:
        # Aucune pastille : la pièce ne pastille qu'à partir de deux alinéas,
        # donc la rédaction entière est l'alinéa 1. Sa page est celle de sa
        # première ligne pleine.
        pleines = [(p, l) for p, l in lignes if l.strip()]
        if pleines:
            out = [dict(numero=1, page=pleines[0][0],
                        texte=_prose([l for _, l in pleines]),
                        tableau=False)]
            hors = []
            return out, hors
    for a in out:
        a['texte'] = _prose(a.pop('lignes'))
    return out, hors


def _apostrophes(s):
    return (s or '').replace('’', "'").replace('‑', '-')


# Les codes rangés du plus long au plus court : « code des douanes de l'Union »
# avant « code des douanes », faute de quoi le second mangerait le premier.
_CODES_TRIES = tuple(sorted({_apostrophes(c).lower() for c in CODES},
                            key=len, reverse=True))


def _texte_nomme(fragment):
    """Le texte que la phrase nomme — un code de la liste, ou un texte daté.

    Rend `None` quand la phrase ne nomme rien : l'appelant hérite alors du
    chapeau, ou déclare `indéterminé`. **Jamais de code par défaut.**
    """
    f = _apostrophes(fragment or '')
    bas = f.lower()
    m = TEXTE_NON_CODIFIE.search(f)
    pos_code = None
    for c in _CODES_TRIES:
        i = bas.find(c)
        if i >= 0 and (pos_code is None or i < pos_code[0]):
            pos_code = (i, c)
    if m and (pos_code is None or m.start() < pos_code[0]):
        return (f'{m.group(1).lower()} n° {m.group(2)} '
                f'du {re.sub(chr(32) + "+", " ", m.group(3))}')
    if pos_code:
        return pos_code[1]
    return None


def _sans_prefixe(txt):
    """Le texte d'un alinéa, débarrassé de ses marqueurs d'énumération."""
    out = txt
    for _ in range(4):
        n = PREFIXE_ENUM.sub('', out, count=1)
        if n == out:
            break
        out = n
    return out


def _premiere(txt, formules):
    pos = [txt.find(f) for f in formules if f in txt]
    return min(pos) if pos else None


def _coupe(txt):
    """Où s'arrête la cible d'un alinéa, et si l'alinéa en porte une.

    Ce qui précède la formule modificative est **la cible** ; ce qui la suit est
    ce par quoi on remplace. « la référence à l'article L. 314-2 est remplacée
    par la référence à l'article L. 314-3 » modifie l'article qui porte la
    référence, jamais les deux références citées.

    Un marqueur de citation coupe plus tôt encore : « A l'article L. 322-56,
    dans sa rédaction issue du 1° du I de l'article 18 de la loi n° 2025-127 »
    ne rouvre pas l'article 18 de cette loi.

    Un alinéa sans formule mais terminé par deux-points est un **chapeau de
    cible** : ses sous-items modifient l'article qu'il nomme.
    """
    f = _premiere(txt, FORMULES_MODIFICATIVES)
    c = _premiere(txt, MARQUEURS_CITATION)
    if f is None and CHAPEAU_CIBLE.search(txt):
        f = len(txt)
    if f is None:
        return None, None
    bornes = [x for x in (f, c) if x is not None]
    return min(bornes), ('formule' if f <= (c if c is not None else f)
                         else 'chapeau de cible')


def _hors_guillemets(txt):
    """Le texte hors des guillemets français, les citations masquées.

    Un alinéa de texte inséré s'ouvre par un guillemet et ne le referme pas
    toujours : ce qu'il cite n'est jamais ce qu'il modifie.
    """
    out, dedans = [], False
    for c in txt:
        if c == '«':
            dedans = True
        elif c == '»':
            dedans = False
            out.append(' ')
            continue
        out.append(' ' if dedans else c)
    return ''.join(out)


def references_de(alineas):
    """Les adresses que la disposition vise, et leur statut.

    Deux statuts, et un seul alimente la colonne `variante` de `REF_norme` :

      `modifie`  la disposition rouvre l'article — c'est un `article_ouvert`
      `cite`     l'article n'est que nommé : il n'est pas rouvert

    **Le code ne s'affirme jamais.** Il est celui que la phrase nomme, ou celui
    du chapeau qui la commande, ou `indéterminé`. Jamais un code par défaut :
    c'est la faute d'A-250, et elle a coûté 55 entrées fausses.
    """
    contexte = dict(texte=None, siege=None, alinea=None)
    refs = []
    for a in alineas:
        txt = a['texte']
        citation = bool(CITATION.match(txt))
        nu = _sans_prefixe(txt)
        # Un chapeau nomme le texte que ses sous-items héritent.
        if not citation and CHAPEAU.search(nu):
            cible = CHAPEAU.sub('', nu).strip()
            s = SIEGE.match(cible)
            nom = _texte_nomme(s.group(2) if s else cible)
            if nom:
                contexte = dict(texte=nom,
                                siege=s.group(1).strip() if s else None,
                                alinea=a['numero'])
            elif ARTICLE_DEFINI_PUIS_TEXTE.match(_apostrophes(cible)):
                # **Le chapeau annonce un texte, et la liste fermée ne le
                # reconnaît pas.** Laisser le contexte en place ferait hériter
                # aux sous-items le code du chapeau précédent : c'est
                # exactement la faute d'A-250, et la pièce la déclenche.
                #
                # Le PLFSS 2026 écrit p. 117 « Le code la sécurité sociale est
                # ainsi modifié : », sans le « de ». Sans cette branche, les
                # treize articles du code de la sécurité sociale que ce bloc
                # modifie sortaient sous « code rural et de la pêche
                # maritime », nom du chapeau d'avant — treize adresses
                # plausibles et fausses.
                #
                # Le contexte passe donc à `indéterminé`, qui se compte et se
                # voit à `S7`. Aucun code par défaut, jamais.
                contexte = dict(texte=CODE_INDETERMINE, siege=None,
                                alinea=a['numero'])
        # La cible est ce qui précède la formule ; le reste est du remplacement.
        clair = _hors_guillemets(txt)
        coupe, _origine = _coupe(clair)
        for mm in REFERENCE.finditer(clair):
            brut = re.sub(r'\s+', ' ', mm.group(1)).strip(' ,.;:')
            if not brut:
                continue
            suite = clair[mm.end():mm.end() + 220]
            nomme = None
            etranger = False
            # « de l'ordonnance », « de l'arrêté » : l'apostrophe n'est pas
            # suivie d'une espace en français, et la première rédaction
            # exigeait `de\s+l’\s+`. La branche était donc morte, et le coût
            # se mesure : « A l'article 20-4 de l'ordonnance n° 96-1122 »
            # sortait sous le code du chapeau précédent — une adresse
            # plausible et fausse, la faute d'A-250 par un autre chemin.
            ms = re.match(r'^\s*(?:du\s+|de\s+la\s+|de\s+l[’\']\s*)'
                          r'(.{3,200})', suite)
            if ms:
                apres = ms.group(1).strip()
                if RENVOI.match(apres):
                    pass                       # « du même code » : il hérite
                else:
                    nomme = _texte_nomme(apres)
                    if nomme is None and INTRODUCTEUR.match(apres):
                        # La phrase nomme un texte, et ce n'est pas un de ceux
                        # que la liste fermée admet. On le dit.
                        nomme = CODE_INDETERMINE
                        etranger = bool(TEXTE_ETRANGER.match(apres))
            porte = ((not citation) and (not etranger)
                     and coupe is not None and mm.start() < coupe)
            refs.append(dict(
                alinea=a['numero'], page=a['page'],
                brut=brut,
                texte=nomme or contexte['texte'],
                texte_origine=('nomme' if nomme
                               else ('chapeau' if contexte['texte'] else None)),
                siege=None if nomme else contexte['siege'],
                statut='modifie' if porte else 'cite',
                fourchette=bool(FOURCHETTE.search(brut)),
            ))
            # « du même code » renvoie au dernier texte que la disposition a
            # modifié. On ne rafraîchit donc le contexte que sur une cible,
            # jamais sur une citation : un code cité en passant ne commande
            # pas les alinéas suivants.
            if porte and nomme and nomme != CODE_INDETERMINE:
                contexte = dict(texte=nomme, siege=None, alinea=a['numero'])
    return refs


def construire(pdf, prof=None):
    prof = prof or PROFILS['plf']
    texte = texte_de(pdf)
    pages = pages_de(texte, prof)
    p_debut = _borne(pages, prof['repere_debut']) + 1
    p_fin = _borne(pages, prof['repere_fin']) - 1
    articles, divisions = decouper(pages, p_debut, p_fin, prof)

    # Le compte des divisions est épinglé quand le profil a déjà tourné sur sa
    # pièce : une division de plus ou de moins veut dire qu'un repère a bougé,
    # et cela arrête plutôt que de livrer une ventilation muette (A-236).
    tetes_div = [d['intitule'] for d in divisions
                 if tete_division(prof, d['intitule']) is not None]
    attendu = prof['divisions_attendues']
    if attendu is not None and len(tetes_div) != attendu:
        raise SystemExit(
            f'{len(tetes_div)} tête(s) de division relevée(s) sur la pièce, '
            f'{attendu} attendue(s) par le profil « {prof["nom"]} ». La '
            'génération s’arrête : un repère de structure a bougé.')

    # La partie et le titre courants, dérivés des divisions rencontrées dans
    # l'ordre de lecture. Rien n'est écrit à la main : les intitulés sont
    # découpés de la pièce. Une tête de division — « DEUXIÈME PARTIE »,
    # « TITRE IER » — est suivie de son intitulé, qui est le bloc suivant tant
    # qu'il n'est pas lui-même une tête. Les deux se portent séparément : coller
    # l'un à l'autre avec une ponctuation de notre cru ferait sortir du verbatim
    # un champ qui doit en rester.
    partie = partie_int = titre_courant = titre_int = None
    pile = []          # (rang, intitulé) — une division chasse ses pairs
    entrees = []
    for a in articles:
        attente = None          # 'partie' ou 'titre' : le prochain bloc est son
        for d in a['divisions']:            # intitulé
            td = tete_division(prof, d)
            if td is not None and td[2] == 'partie':
                partie, partie_int = td[0], td[1]
                titre_courant = titre_int = None
                pile = []
                attente = None if td[1] is not None else 'partie'
            elif td is not None:
                titre_courant, titre_int = td[0], td[1]
                pile = []
                attente = None if td[1] is not None else 'titre'
            elif attente == 'partie':
                partie_int, attente = d, None
            elif attente == 'titre':
                titre_int, attente = d, None
            else:
                rang = _rang_division(d)
                pile = [(r, x) for (r, x) in pile if r < rang]
                pile.append((rang, d))
        red = _nettoyer(a['redaction'])
        mot = _nettoyer(a['motifs'])
        al, hors = alineas_de(red, prof)
        refs = references_de(al)
        entrees.append(dict(
            numero=a['numero'],
            titre=a['titre'],
            partie=partie,
            partie_intitule=partie_int,
            titre_division=titre_courant,
            titre_division_intitule=titre_int,
            divisions=[x for _, x in pile],
            page=a['page_debut'],
            page_fin=a['page_fin'],
            redaction=dict(
                lignes=[l for _, l in red],
                alineas=al,
                hors_alinea=hors,
                nb_alineas=len(al),
                porte_tableau=bool(hors) or any(x['tableau'] for x in al),
            ),
            expose_des_motifs=dict(
                lignes=[l for _, l in mot],
                page=mot[0][0] if mot else None,
                statut='indice, jamais norme (A-229)',
            ),
            references=refs,
        ))
    return dict(
        _revision=dict(
            role=prof['role'],
            regle=("Une entrée par article : numéro, partie, titre, rédaction "
                   "exacte, page dans la pièce, exposé des motifs rattaché. "
                   "L'exposé des motifs est indexé avec l'article et jamais "
                   "confondu avec lui : il est de l'indice, pas de la norme "
                   "(A-229)."),
            piece=dict(
                nom=os.path.basename(pdf),
                sha256=_sha256(pdf),
                octets=os.path.getsize(pdf),
                pages=len(pages),
                au_coffre=False,
                motif_hors_coffre=('document public, retéléchargeable à '
                                   "l'identique (A-235)"),
            ),
            extraction=dict(
                profil=prof['nom'],
                piece_declaree=prof['piece'],
                outil=' '.join(PDFTOTEXT),
                version=_version_outil(),
                repere_debut=prof['repere_debut'],
                repere_fin=prof['repere_fin'],
                page_premiere=p_debut,
                page_derniere=p_fin,
                marque_alinea=prof['alinea'],
                sommaire=prof['sommaire'],
                divisions_relevees=len(tetes_div),
            ),
            divisions=divisions,
        ),
        articles=entrees,
    )


def ecrire(obj, dst):
    os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
    with open(dst, 'w', encoding='utf-8', newline='') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=False)
        f.write('\n')
    return _sha256(dst)


def main(pdf, dst, nom_profil='plf'):
    prof = profil_de(nom_profil)
    obj = construire(pdf, prof)
    emp = ecrire(obj, dst)
    a = obj['articles']
    refs = [r for e in a for r in e['references']]
    mod = [r for r in refs if r['statut'] == 'modifie']
    print(f'profil « {prof["nom"]} » — {prof["piece"]}')
    print(f'{len(a)} article(s) — pages '
          f"{obj['_revision']['extraction']['page_premiere']} à "
          f"{obj['_revision']['extraction']['page_derniere']}")
    print(f"  {sum(e['redaction']['nb_alineas'] for e in a)} alinéa(s), "
          f"{sum(1 for e in a if e['redaction']['porte_tableau'])} article(s) "
          f'portant du hors-alinéa (tableau)')
    print(f'  {len(refs)} référence(s) relevée(s) à la disposition, '
          f'dont {len(mod)} modificative(s)')
    print(f'  {sum(1 for r in mod if not r["texte"])} référence(s) '
          'modificative(s) sans texte déterminé')
    print(f'  empreinte du socle — {emp}')
    return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
