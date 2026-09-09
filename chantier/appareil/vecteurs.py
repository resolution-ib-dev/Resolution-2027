# -*- coding: utf-8 -*-
"""Les vecteurs relevés à la main — le siège juridique de chaque mesure.

Même dispositif que `sources_chiffres.py` : ce qui est **écrit à la main** vit
ici et survit à chaque régénération ; le référentiel produit ne s'édite jamais.

## Ce qu'est un vecteur, et ce qu'il n'est pas

Le vecteur est **l'endroit du droit qu'on modifie**. Ce n'est pas le véhicule —
le texte dans lequel on dépose —, et les deux ne se confondent jamais (A-227).

**Un vecteur est un identifiant, jamais du verbatim.** « Article L. 131-3 du
code de l'environnement » est une adresse ; le texte de cet article est autre
chose, et il n'entre au corpus que par pièce jointe (A-234). C'est ce qui rend
la recherche web légitime ici : elle repère, elle ne copie pas.

## Un organisme a souvent deux vecteurs, et l'économie porte sur le second

C'est le fait que le lot pilote a sorti, et il commande la structure. Les
agences de l'eau sont créées par une section du code de l'environnement et
financées par une autre — les redevances. Supprimer l'organisme et supprimer sa
ressource ne se font pas au même endroit, et une mesure d'économie vise
**presque toujours le financement**.

Chaque entrée déclare donc le **rôle** de son vecteur :

    creation      le texte qui institue l'organisme ou le dispositif
    financement   le texte qui lui affecte une ressource
    competence    le texte qui lui donne sa mission
    montant       le siège du chiffre voté, qui n'est pas codifié
    derogation    l'article qui porte la dépense fiscale

## Quatre provenances, et une seule est mécanique

    3 `annexe`      dérivé d'une annexe budgétaire importée au socle. Se
                    revérifie à chaque régénération, sans réseau.
    2 `legifrance`  relevé par recherche sur Légifrance, avec l'identifiant du
                    texte et la date du relevé. Se recontrôle sur pièce.
    1 `corpus`      porté par une pièce du corpus — récapitulatif de
                    transposabilité, trois colonnes.
    0 `a_trouver`   pas de vecteur. Ce n'est pas un défaut tant que c'est dit.

**Aucun vecteur ne s'invente et aucun trou ne se comble** — c'est la règle des
chiffres, appliquée au droit. Un vecteur vraisemblable est plus dangereux qu'un
vecteur absent : il a l'apparence d'une adresse et il envoie l'amendement au
mauvais endroit.
"""

# Les ordinaux latins que la numérotation française des codes emploie. La liste
# est fermée : un ordinal absent d'ici fait sortir la référence en N2 plutôt que
# de passer inaperçu.
ORDINAUX = (
    'bis', 'ter', 'quater', 'quinquies', 'sexies', 'septies', 'octies',
    'nonies', 'decies', 'undecies', 'duodecies', 'terdecies', 'quaterdecies',
    'quindecies', 'sexdecies', 'septdecies', 'octodecies', 'novodecies',
    'vicies', 'unvicies', 'duovicies', 'tervicies', 'quatervicies',
    'quinvicies', 'sexvicies', 'septvicies', 'octovicies', 'novovicies',
    'tricies', 'untricies', 'duotricies',
)

# ---------------------------------------------------------------------------
# La déduction du code, et pourquoi elle est nécessaire.
#
# **L'annexe des dépenses fiscales ne nomme jamais le code.** Elle donne
# « 1465 A », « L. 312-48 », « L. 2333-55-3 » et rien d'autre. La première
# version de `ref_norme.py` affirmait « code général des impôts » pour les 465
# — **c'était un faux sur 55 d'entre elles**, relevé par l'auteur : les accises
# sur les énergies et les taxes sur les véhicules vivent au code des impositions
# sur les biens et services, et le prélèvement sur le produit brut des jeux au
# code général des collectivités territoriales.
#
# Un vecteur vraisemblable est plus dangereux qu'un vecteur absent. La déduction
# est donc **écrite, bornée, et déclarée sur chaque vecteur** par le champ
# `regle_code`. Une forme de numéro qu'aucune règle ne couvre sort le code en
# `indetermine` et le contrôle N9 la compte.
#
#   motif        expression régulière sur le numéro d'article nu
#   code         le code, nommé en toutes lettres
#   identifiant  l'identifiant Légifrance du code, quand il a été relevé
#   siege        le niveau intermédiaire — livre, chapitre, section — quand la
#                numérotation le détermine sans ambiguïté
#   releve_le    la date à laquelle la règle a été vérifiée sur pièce
DEDUCTION_CODE = [
    dict(motif=r'^L\.?\s*312-',
         code='code des impositions sur les biens et services',
         identifiant='LEGITEXT000044595989',
         siege='chapitre II — Énergies (art. L. 312-1 à L. 312-107)',
         releve_le='20260831',
         requete='code des impositions sur les biens et services L312-48 '
                 'accise produits énergétiques'),
    dict(motif=r'^L\.?\s*421-',
         code='code des impositions sur les biens et services',
         identifiant='LEGITEXT000044595989',
         siege='chapitre Ier — Véhicules (art. L. 421-1 et suivants)',
         releve_le='20260831',
         requete='article L421-78 taxe émissions CO2 véhicules code des '
                 'impositions sur les biens et services'),
    dict(motif=r'^L\.?\s*2333-',
         code='code général des collectivités territoriales',
         identifiant=None,
         siege='livre III — Finances communales',
         releve_le=None,
         requete=None),
    dict(motif=r'^(?:Loi|Ordonnance|D[ée]cret|LOI)\s*n[°o]',
         code='texte non codifié — la loi elle-même est le vecteur',
         identifiant=None,
         siege=None,
         releve_le='20260831',
         requete="une dépense fiscale créée par une loi de finances et non "
                 "codifiée se modifie à l'article de cette loi"),
    dict(motif=r'^\*?\d',
         code='code général des impôts',
         identifiant='LEGITEXT000006069577',
         siege=None,
         releve_le='20260831',
         requete='numérotation nue sans lettre de partie — CGI par défaut'),
]

CODE_INDETERMINE = 'indéterminé'

PROVENANCES = {
    'annexe': (3, "dérivé d'une annexe budgétaire importée au socle"),
    'legifrance': (2, 'relevé sur Légifrance, identifiant et date portés'),
    'corpus': (1, 'porté par une pièce du corpus'),
    'a_trouver': (0, 'pas de vecteur relevé'),
}

ROLES = ('creation', 'financement', 'competence', 'montant', 'derogation')

# ---------------------------------------------------------------------------
# Le vecteur des mesures de crédits.
#
# **Une mesure de crédits est une mesure de plein exercice, et elle est de rang
# législatif** (A-243). Elle se dépose en amendement de chiffres sur l'état B
# annexé à l'article de crédits du budget général. Dire qu'elle serait « infra
# législative » parce qu'elle porte des plafonds est faux : l'état B est voté,
# il fait partie de la loi de finances, et les crédits qu'il ouvre sont
# limitatifs.
#
# Son vecteur n'est pas codifié — il n'y a pas d'article de code à modifier —
# mais il est parfaitement déterminé. C'est un `trouve`, pas un `sans objet`.
VECTEUR_CREDITS = dict(
    role='montant', provenance='corpus', strate='L',
    texte="loi de finances de l'année",
    articles="état B annexé à l'article de crédits du budget général — "
             "mission, puis programme",
    identifiant=None,
    note="Amendement de chiffres : une ligne de crédits, une baisse. Aucune "
         "disposition modificative, aucun article de code. **La mesure est de "
         "rang législatif** et les crédits ouverts sont limitatifs. Le montant "
         "se reprend au projet de loi de finances en discussion, pas au nôtre "
         "(A-244).")

# ---------------------------------------------------------------------------
# Relevés à la main sur Légifrance. Une entrée par cible.
#
#   cle          le libellé exact tel qu'il figure au socle — c'est la clé de
#                jointure, et elle ne se normalise pas (A-93, A-94)
#   population   operateur · odac_odal · taxe_affectee · proposition
#   vecteurs     un ou plusieurs, chacun avec son rôle
#   releve_le    la date du relevé. Un vecteur vieillit : un texte se modifie,
#                se recodifie, s'abroge.
#   requete      ce qui a été cherché, pour que le relevé se rejoue à
#                l'identique
ECRITS = {
    'ADEME - Agence de l\'environnement et de la maîtrise de l\'énergie': dict(
        population='operateur', releve_le='20260831',
        requete="ADEME texte fondateur code de l'environnement L131-3",
        vecteurs=[
            dict(role='creation', provenance='legifrance', strate='L',
                 texte="code de l'environnement",
                 articles='L. 131-3 à L. 131-7',
                 identifiant='LEGISCTA000006176637',
                 note="Section 1 du chapitre Ier — « Agence de "
                      "l'environnement et de la maîtrise de l'énergie »."),
            dict(role='creation', provenance='legifrance', strate='L',
                 texte='loi n° 90-1130 du 19 décembre 1990',
                 articles='texte entier',
                 identifiant='JORFTEXT000000525387',
                 note="Loi portant création de l'Agence. Codifiée depuis ; "
                      "**à instruire avant d'abroger la loi plutôt que les "
                      "articles du code**."),
        ]),

    'France Compétences': dict(
        population='operateur', releve_le='20260831',
        requete="France Compétences contribution unique code du travail "
                "L6131-1",
        vecteurs=[
            dict(role='creation', provenance='legifrance', strate='L',
                 texte='code du travail',
                 articles='L. 6123-5 à L. 6123-14',
                 identifiant='LEGISCTA000037386799',
                 note='Section 3 — « France compétences ».'),
            dict(role='financement', provenance='legifrance', strate='L',
                 texte='code du travail',
                 articles='L. 6131-1 à L. 6131-5',
                 identifiant='LEGISCTA000037375106',
                 note="Chapitre unique — financement de la formation "
                      "professionnelle. **C'est ici que porte l'économie de "
                      "10,6 Md€**, pas à la création."),
        ]),

    'AFITF - Agence de financement des infrastructures de transport de France': dict(
        population='operateur', releve_le='20260831',
        requete='AFITF texte de création décret 2004 code des transports',
        vecteurs=[
            dict(role='creation', provenance='legifrance', strate='L',
                 texte='code des transports',
                 articles='L. 1512-19 à L. 1512-20',
                 identifiant='LEGISCTA000037287576',
                 note='Sous-section 2 — « L\'Agence de financement des '
                      'infrastructures de transport de France ».'),
            dict(role='creation', provenance='legifrance', strate='reglementaire',
                 texte='décret n° 2004-1317 du 26 novembre 2004',
                 articles='texte entier',
                 identifiant='JORFTEXT000000805719',
                 note="**Partie réglementaire, hors de portée d'un "
                      "amendement.** La partie législative du code des "
                      "transports est le seul vecteur utilisable."),
        ]),

    'AFPA - Agence nationale pour la formation professionnelle des adultes': dict(
        population='operateur', releve_le='20260831',
        requete='AFPA établissement public code du travail L5315-1',
        vecteurs=[
            dict(role='creation', provenance='legifrance', strate='L',
                 texte='code du travail',
                 articles='L. 5315-1 à L. 5315-10',
                 identifiant='LEGISCTA000031073614',
                 note="Chapitre V — « Établissement public chargé de la "
                      "formation professionnelle des adultes »."),
        ]),

    'ANAH - Agence nationale de l\'habitat': dict(
        population='operateur', releve_le='20260831',
        requete='ANAH code de la construction et de l\'habitation L321-1',
        vecteurs=[
            dict(role='creation', provenance='legifrance', strate='L',
                 texte="code de la construction et de l'habitation",
                 articles='L. 321-1 à L. 321-12',
                 identifiant='LEGISCTA000006159134',
                 note='Chapitre Ier — « Agence nationale de l\'habitat — '
                      'statut et concours financier ». **Le titre du chapitre '
                      'porte les deux rôles**, création et financement.'),
        ]),

    'Agences de l\'eau': dict(
        population='operateur', releve_le='20260831',
        requete="agences de l'eau code de l'environnement L213-8 redevances",
        vecteurs=[
            dict(role='creation', provenance='legifrance', strate='L',
                 texte="code de l'environnement",
                 articles='L. 213-8 à L. 213-11-17',
                 identifiant='LEGISCTA000006176454',
                 note='Section 3 — « Comités de bassin et agences de l\'eau ».'),
            dict(role='financement', provenance='legifrance', strate='L',
                 texte="code de l'environnement",
                 articles='L. 213-10 à L. 213-10-12',
                 identifiant='LEGISCTA000006188366',
                 note="Sous-section 3 — « Redevances des agences de l'eau ». "
                      "**C'est le vecteur de l'économie de 2,1 Md€** : la "
                      "ressource, non l'organisme."),
        ]),

    'France Travail': dict(
        population='operateur', releve_le='20260831',
        requete='France Travail code du travail L5312-1 établissement public',
        vecteurs=[
            dict(role='creation', provenance='legifrance', strate='L',
                 texte='code du travail',
                 articles='L. 5312-1 à L. 5312-13-1',
                 identifiant='LEGIARTI000048600658',
                 note="Article L. 5312-1 — statut et missions de l'opérateur "
                      "France Travail. La partie réglementaire est aux "
                      "R. 5312-1 et suivants, hors de portée."),
        ]),

    'CNC - Centre national du cinéma et de l\'image animée': dict(
        population='operateur', releve_le='20260831',
        requete="Centre national du cinéma code du cinéma L111-1 "
                "impositions affectées",
        vecteurs=[
            dict(role='creation', provenance='legifrance', strate='L',
                 texte="code du cinéma et de l'image animée",
                 articles='L. 111-1 à L. 116-5',
                 identifiant='LEGISCTA000020907716',
                 note='Titre Ier — « Centre national du cinéma et de l\'image '
                      'animée ».'),
            dict(role='financement', provenance='legifrance', strate='L',
                 texte="code du cinéma et de l'image animée",
                 articles='L. 115-1 à L. 115-27',
                 identifiant='LEGISCTA000020907745',
                 note="Chapitre V — « Impositions affectées au Centre national "
                      "du cinéma et de l'image animée et perçues par lui ». "
                      "**Le titre du chapitre nomme lui-même l'affectation** : "
                      "c'est le vecteur des neuf taxes du CNC."),
        ]),

    'ALS Action logement services': dict(
        population='odac_odal', releve_le='20260831',
        requete='Action Logement Services PEEC code construction habitation '
                'L313-19',
        vecteurs=[
            dict(role='creation', provenance='legifrance', strate='L',
                 texte="code de la construction et de l'habitation",
                 articles='L. 313-19 à L. 313-19-6',
                 identifiant='LEGISCTA000033281169',
                 note='Sous-section 3 — « Action Logement Services ».'),
            dict(role='financement', provenance='legifrance', strate='L',
                 texte="code de la construction et de l'habitation",
                 articles='L. 313-1 à L. 313-6',
                 identifiant='LEGISCTA000006176366',
                 note="Section 1 — participation des employeurs à l'effort de "
                      "construction. **C'est l'assiette de la ressource**, "
                      "donc le vecteur de l'économie de 1,9 Md€."),
        ]),

    'Etablissements publics fonciers 40': dict(
        population='odac_odal', releve_le='20260831',
        requete="établissements publics fonciers taxe spéciale d'équipement "
                'CGI 1607 bis',
        vecteurs=[
            dict(role='financement', provenance='legifrance', strate='L',
                 texte='code général des impôts',
                 articles='1607 bis à 1607 ter',
                 identifiant='LEGISCTA000030300156',
                 note="Section VII bis — « Taxe spéciale d'équipement perçue "
                      "au profit des établissements publics fonciers et de "
                      "l'office foncier de Corse ». **Un seul vecteur pour les "
                      "34 affectataires** : c'est ce qui rend cette ligne "
                      "bon marché."),
        ]),

    'Chambres consulaires 273': dict(
        population='odac_odal', releve_le='20260831',
        requete='taxe pour frais de chambres de commerce CGI 1600 chambres '
                "d'agriculture 1604",
        vecteurs=[
            dict(role='financement', provenance='legifrance', strate='L',
                 texte='code général des impôts',
                 articles='1600 à 1600 A',
                 identifiant='LEGISCTA000006162690',
                 note="Section I — « Taxe pour frais de chambres de commerce "
                      "et d'industrie »."),
            dict(role='financement', provenance='legifrance', strate='L',
                 texte='code général des impôts',
                 articles='1604',
                 identifiant='LEGISCTA000006162693',
                 note="Section IV — « Taxe pour frais de chambres "
                      "d'agriculture ». **Deux vecteurs pour une seule ligne "
                      "d'économie** : les consulaires ne sont pas une "
                      "population homogène."),
        ]),
}
