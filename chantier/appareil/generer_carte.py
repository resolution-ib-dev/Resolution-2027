# -*- coding: utf-8 -*-
"""Carte du projet — le classement du corpus par contenu, et l'affectation.

Un seul fichier à ouvrir pour savoir ce que le chantier porte, dans quelle
famille, à quelle adresse réelle, et ce qui manque. Il se régénère : rien ne s'y
écrit à la main.

Trois surfamilles, neuf familles. Les règles vivent dans
`methode/classement_corpus.md` ; **l'affectation vit ici**, et nulle part
ailleurs. `appareil/generer_index.py` importe la table ci-dessous pour porter le
champ `famille` de chaque artefact : un seul point de vérité pour le classement.

La colonne « adresse » n'est pas curée. Elle se déduit de l'index : le chemin au
coffre d'un artefact, un badge « replié » quand il est dans une archive, un badge
« pièce jointe » quand c'est un document du projet que Claude ne peut pas
déplacer. Ce qui n'existe pas encore porte un badge « à écrire ».

Usage : python3 generer_carte.py ../methode/index.json ../livrables/carte_du_projet.html
"""
import html
import json
import os
import sys

# --------------------------------------------------------------- l'affectation
# Une ligne de carte : (titre lisible, chemins au dépôt, adresse forcée, propos)
#
# `chemins` rattache la ligne à un ou plusieurs artefacts de l'index — c'est par
# là que le champ `famille` se propage. Une ligne sans chemin décrit quelque
# chose qui n'est pas encore un artefact : son adresse est alors forcée.
#
# `adresse` vaut None dans le cas courant — elle se déduit de l'index. Les deux
# seules valeurs forcées sont ('au', libellé) pour ce qui reste à écrire.

FAMILLES = [
 {'surfamille': 'Input',
  'intro': 'Ce sur quoi tout s’appuie. Lecture seule.',
  'familles': [

   {'titre': 'Doctrine', 'compte': None,
    'intro': 'Le manuscrit et ses annexes. Ils font vérité, et ne se révisent '
             'jamais depuis l’aval.',
    'colonnes': ('document', 'adresse', 'ce qu’il porte'),
    'apres': 'Des annexes formelles compléteront, versées par l’auteur.',
    'lignes': [
     ('Manuscrit', ['manuscrit/manuscrit.html'], None,
      'strate 1, corps et notes de fin. 141 notes, dont 37 chiffrées.'),
     ('Synthèse Calculs Résolution',
      ['sources/Synthèse_Calculs_Résolution_0819.xlsx'], None,
      'chiffrage. Onglets Manuscrit, Détail Économies, Perdants.'),
     ('Synthèse ETP et agences',
      ['sources/Synthèse_ETP_et_agences_Résolution_0819.xls'], None,
      'décompte des agences, opérateurs et effectifs.'),
     ('PLF 2026 — taxes affectées',
      ['sources/PLF_2026_VM_tome_I__Annexe_2__Taxes_affectees_IB_1113.xls'],
      None, 'tome I, annexe 2.'),
     ('PLF 2026 — dépenses fiscales',
      ['sources/PLF_2026_VM_tome_II__Annexe_3__Depenses_fiscales__IB__1126.xls'],
      None, 'tome II, annexe 3. Les 486 niches.'),
     ('PLF 2026 — dépenses du budget général',
      ['sources/PLF26__Depenses_2026_du_BG_et_des_BA_selon_nomenclatures_'
       'destination_et_nature_IB_1127.xls'], None,
      'par destination et par nature.'),
     ('Comptes des communes', ['sources/T_3207_Communes_IB_1113.xlsx'], None,
      'Insee, tableau 3207.'),
     ('Comptes des APUL', ['sources/T_3305_APUL_IB_1118.xlsx'], None,
      'Insee, tableau 3305.'),
     ('Dépense pour l’éducation',
      ['sources/deppee2025donneesfiche09ladepensepourleducation25_12_19IB.xlsx'],
      None, 'Depp, fiche 9.'),
    ]},

   {'titre': 'Extensions', 'compte': None,
    'intro': 'Textes gelés et validés qui complètent la doctrine. Strate '
             'maître : une mise à jour ciblée se fait ici, puis on rejoue les '
             'outputs concernés. Les trois pièces forment aujourd’hui un '
             'ensemble, la réforme budgétaire.',
    'colonnes': ('document', 'adresse', 'ce qu’il porte'),
    'apres': 'Dans le trois colonnes, la première colonne est le texte actuel : '
             'verbatim entre guillemets pour 26 blocs sur 37, résumé ou constat '
             'de vacance pour les onze autres. <b>Le point de vérité du texte en '
             'vigueur reste la Constitution en vigueur</b>, en références '
             'externes. Le texte projeté est en troisième colonne, la '
             'justification en deuxième et en note de la troisième.',
    'lignes': [
     ('Constitution — trois colonnes',
      ['sources/Constitution_3col_20260730_v44.html'], None,
      'texte actuel, réforme visée, rédaction révisée. 37 blocs. Fait paire '
      'avec la présentation, même millésime.'),
     ('Note de réforme budgétaire',
      ['sources/note_reforme_budgetaire_20260730_v12.html'], None,
      'externalisée, donc gelée. Promue de l’output vers l’input.'),
     ('Précédents restes à payer',
      ['sources/Precedents_restes_a_payer_20260721.md'], None,
      'précédents historiques, source dure de la réforme budgétaire.'),
    ]},

   {'titre': 'Références externes', 'compte': None,
    'intro': 'Sources de confiance où la doctrine puise sans s’y aligner. '
             'Elles se citent au dehors.',
    'colonnes': ('document', 'adresse', 'ce qu’il porte'),
    'apres': None,
    'lignes': [
     ('Constitution en vigueur',
      ['sources/Constitution_reference_20260806_v1.html'], None, 'texte nu.'),
     ('Déclaration de 1789', ['sources/DDHC_20260806_v1.html'], None,
      'texte nu. Articles 13, 14, 15.'),
     ('LOLF en vigueur', ['sources/LOLF_reference_20260507.html'], None,
      'texte nu.'),
     ('DGFiP statistiques 2025', ['sources/dgfip_stat_32_2025.pdf'], None,
      'recettes fiscales.'),
     ('Liste des impôts et taxes — Ifrap',
      ['sources/etude_fondation_ifrap_liste_des_impots_et_taxes.pdf'], None,
      'source des 438 taxes.'),
     ('Justice fiscale : comment nous avons trahi 1789',
      ['sources/Note_n__1_Justice_fiscalecomment_nous_avons_trahi_1789.pdf'],
      None, 'doctrine tierce.'),
     ('L’impasse de la taxe Zucman — Fondapol',
      ['sources/fondapollimpassedelataxezucman_fr_20260608_formatweb_w.pdf'],
      None, 'doctrine tierce.'),
     ('Plan stratégique réseaux',
      ['sources/France_Resolution_Strategie_Reseaux_2.pdf'], None,
      'vocabulaire et cinq postures de diffusion.'),
     ('Exposé sommaire — principes de rédaction, Génération Libre',
      ['sources/Expose_des_motifs_redaction_GL.docx'], None,
      'forme des amendements du contre-budget GL 2026. Docx à la racine du '
      'coffre, non déplaçable. Le chantier entre par sa digestion, '
      '<code>reference/gabarit_expose_sommaire.md</code>.'),
    ]},

   {'titre': 'Références internes', 'compte': None,
    'intro': 'Brouillons et proto-doctrine. On y puise, on ne s’y engage pas, '
             'et <b>ils ne se citent jamais au dehors</b> : ce sont nos propres '
             'textes.',
    'colonnes': ('document', 'adresse', 'ce qu’il porte'),
    'apres': 'Les quatre derniers sont des documents finis, écrits avant '
             'l’existence du référentiel et des contrôles. Leur texte tient, '
             'leurs chiffres n’ont jamais été confrontés au corpus, et certains '
             'le contredisent probablement.',
    'lignes': [
     ('Réserve d’arguments', ['sources/Reserve_arguments_20260806_v1.html'],
      None, 'matière argumentative.'),
     ('Input gagnants-perdants',
      ['sources/Input_gagnants_perdants_20260820_v1_brouillon.html'], None,
      'brouillon.'),
     ('Input HLM', ['sources/Input_HLM_20260806_v1_proto.html'], None,
      'proto sur le logement social.'),
     ('Note retraite', ['sources/20250619_Note_Retraite_IB.docx'], None,
      'note non validée. Ne rejoint pas la doctrine.'),
     ('Données', ['sources/Donnees_20260806_v1_proto.html'], None,
      '109 candidats chiffrés non sourcés, une soixantaine avec un calcul non '
      'documenté. Alimenterait REF_chiffres. Porte aussi une section '
      '« Perdants » rédigée, et une comparaison de régulateurs hors sujet.'),
     ('Q&A', ['sources/QA_20260806_v1_proto.html'], None,
      '152 questions, antérieures aux contrôles.'),
     ('Une page', ['sources/1pager_20260806_v1_proto.html'], None,
      'synthèse d’une page, antérieure aux contrôles.'),
     ('Note entreprises', ['sources/Note_entreprises_20260806_v1_proto.html'],
      None, 'antérieure aux contrôles.'),
    ]},
  ]},

 {'surfamille': 'Travail',
  'intro': 'Ce avec quoi on lit la doctrine, et ce qui la transforme.',
  'familles': [

   {'titre': 'Grilles', 'compte': '1 visible',
    'intro': 'Les lectures de la doctrine. Elles portent des jugements — '
             'verdict, degré, rattachement — et se corrigent dès qu’elles '
             's’écartent du manuscrit.',
    'colonnes': ('grille', 'adresse', 'ce qu’elle porte'),
    'apres': 'Le référentiel des faits naît sourcé par ce que le corpus '
             'énonçait déjà, et déclare le reste. Sur 257 entrées, 59 viennent '
             'du manuscrit, 89 du référentiel de doctrine, et 109 sont les '
             'candidats du proto Données, tous à sourcer. <b>Un chiffre sans '
             'source traçable reste déclaré sans source.</b>',
    'lignes': [
     ('Recensement des innovations',
      ['sources/Recensement_innovations_20260731_v1.md'], None,
      'travail de fond sur les strates normatives.'),
     ('REF_doctrine', ['referentiels/REF_doctrine.json'], None,
      'la doctrine en nœuds. Lu par cinq skills et tous les générateurs.'),
     ('REF_chiffres', ['referentiels/REF_chiffres.json'], None,
      'le référentiel des faits. Un point de vérité par chiffre, et la '
      'déclaration de ce qui n’est pas sourcé.'),
     ('Justifications, apports et sources',
      ['appareil/justifications.py', 'appareil/apports.py',
       'appareil/sources_chiffres.py'], None,
      'les champs rédigés à la main — les quatre du côté des positions, le '
      'sourçage du côté des chiffres. Du code par le format, de la rédaction '
      'par le contenu.'),
    ]},

   {'titre': 'Bac à sable', 'compte': None,
    'intro': 'Mes travaux, non relus. Ce qui n’est pas validé n’est pas de '
             'l’input.',
    'colonnes': ('document', 'adresse', 'état'),
    'apres': None,
    'lignes': [
     ('LOLF — trois colonnes', ['sources/LOLF_3col_20260507_v7.html'], None,
      'texte verbatim Légifrance, catégorie et motif, proposition. 29 blocs, '
      'dont 21 en verbatim. Transcription aboutie, jamais validée. Monterait '
      'en extensions une fois relue.'),
     ('Extrait gagnants-perdants',
      ['livrables/extrait_gagnants_perdants.html'], None,
      'généré, contrôles à zéro. Quatre catégories rédigées sur cinquante-six.'),
    ]},

   {'titre': 'Méthode', 'compte': None,
    'intro': 'Les règles qu’on s’est données. Ce qui est écrit ici ne se '
             'redemande pas.',
    'colonnes': ('document', 'adresse'),
    'apres': '<b>Structure d’une PPL</b> est la digestion du guide de '
             'légistique du SGG — fiche 3.1.1 du 5 décembre 2024, décisions du '
             'Conseil constitutionnel de 2009 et 2023, Conseil d’État Bailly '
             '1975 — augmentée de nos propres règles. Une référence externe '
             'entre au corpus par sa digestion, jamais par son fichier.',
    'lignes': [
     ('Classement du corpus', ['methode/classement_corpus.md'], None, None),
     ('Registre des arbitrages', ['methode/arbitrages.md'], None, None),
     ('Registre des arbitrages — archive',
      ['methode/arbitrages_archive.md'], None, None),
     ('Journal du corpus', ['methode/journal.md'], None, None),
     ('Index de résolution', ['methode/index.json'], None, None),
     ('Empreintes du coffre', ['methode/empreintes.json'], None, None),
     ('Localisation', ['methode/localisation.md'], None, None),
     # Renommé le 20260902 ; la ligne de carte pointait encore l'ancien
     # chemin, et la carte levait à chaque rejeu — invisible tant qu'aucun
     # fil ne la rejouait. Corrigé le 20260904.
     ('Rapport gagnants-perdants du 20260820',
      ['sources/rapport_gagnants_perdants_20260820.md'], None, None),
     ('Contrat de projection', ['methode/contrat_projection.md'], None, None),
     ('Règles de forme canonique', ['methode/regles_forme_canonique.md'],
      None, None),
     ('Règles rédactionnelles', ['methode/regles_redactionnelles.md'],
      None, None),
     ('Procédure de contrôle', ['methode/procedure_controle.md'], None, None),
     ('Croisements du corpus', ['methode/croisements_corpus.md'], None, None),
     ('Dérivation de l’axe D2', ['methode/derivation_D2.md'], None, None),
     ('Prompt du fil courant', ['methode/prompt_fil_courant.md'], None, None),
     ('Carte des trois chantiers', ['methode/carte_des_chantiers.md'],
      None, None),
     ('Procédure du contre-PLF', ['methode/procedure_contre_plf.md'],
      None, None),
     ('Test de rattachement', ['methode/test_rattachement.md'], None, None),
     ('Procédure des vecteurs', ['methode/procedure_vecteurs.md'],
      None, None),
     ('Structure d’une PPL', ['sources/structure_ppl.md'], None, None),
     ('Gabarit de l’exposé sommaire',
      ['reference/gabarit_expose_sommaire.md'], None, None),
     ('Prompt de la session d’organisation',
      ['sources/prompt_session_organisation_20260827.md'], None, None),
     ('Plan de la présentation', ['sources/Plan_presentation_20260730_v6.md'],
      None, None),
     ('Instructions permanentes', ['CLAUDE.md'], None, None),
     ('Démarrage', ['DEMARRAGE.md'], None, None),
    ]},

   {'titre': 'Outillage', 'compte': 'archives+pieces',
    'intro': 'Générateurs et contrôles. Tu n’as jamais à les ouvrir.',
    'colonnes': ('pièce', 'adresse'),
    'apres': None,
    'lignes': [
     ('Archive technique', [], ('archive',), None),
    ]},
  ]},

 {'surfamille': 'Output',
  'intro': 'Le grand objet du travail. Trois codes formels, trois métiers.',
  'familles': [

   {'titre': 'Juridique', 'compte': None,
    'intro': 'Code légistique. Projections du texte à trois colonnes.',
    'colonnes': ('document', 'adresse', 'état'),
    'apres': 'Rien en organique, rien en ordinaire. C’est un trou, pas un '
             'oubli de rangement.',
    'lignes': [
     ('PPLC — dispositions modificatives',
      ['sources/PPLC_consolidee_modificative_20260730_v6.md'], None,
      'consolidée. À rejouer si la révision bouge.'),
     ('PPLC — substitution intégrale',
      ['sources/PPLC_consolidee_substitution_20260730_v6.md'], None,
      'consolidée. Même exposé des motifs que la modificative.'),
    ]},

   {'titre': 'Rédactionnel', 'compte': None,
    'intro': 'Code des règles de forme. Un texte qui se lit sans sa mise en '
             'forme est rédactionnel.',
    'colonnes': ('document', 'adresse', 'état'),
    'apres': None,
    'lignes': [
     ('Récapitulatif de transposabilité',
      ['sources/Recap_transposabilite_20260731_v6.md'], None,
      'externalisé, donc gelé à son millésime. Une version neuve serait un '
      'artefact neuf.'),
     ('Présentation de la révision',
      ['sources/Presentation_20260731_v44.md'], None,
      'fait paire avec le texte à trois colonnes.'),
    ]},

   {'titre': 'Rédactionnel', 'compte': None,
    'intro': 'Texte suivi. Il se lit sans sa mise en forme.',
    'colonnes': ('document', 'adresse', 'état'),
    'apres': None,
    'lignes': [
     ('Le manifeste', ['site/manifeste.html'], None,
      'le proto 1-pager remis à jour, corrections déclarées à '
      '`appareil/manifeste.py` (A-206, A-211). Charte du livre, affichable et '
      'téléchargeable en PDF.'),
    ]},

   {'titre': 'Graphique', 'compte': None,
    'intro': 'Code de la charte. Une pièce dont la mise en forme porte le sens.',
    'colonnes': ('document', 'adresse', 'état'),
    'apres': None,
    'lignes': [
     ('Galerie des fiches gagnants-perdants',
      ['livrables/galerie_fiches.html'], None,
      'dix-huit fiches, un persona par fiche. Premier jet arrêté par '
      'l’auteur le 20260828, esthétique provisoire. Régénéré par '
      '`generer_fiches.py`, jamais corrigé à la main.'),
     ('Le site', ['site/index.html'], None,
      'un index et dix-huit fiches à leur adresse (A-195). Vingt et un '
      'fichiers, régénérés par `generer_site.py`, poussés au dépôt de '
      'publication par `make publier`, déployés par Vercel. Jamais corrigé '
      'en ligne.'),
    ]},
  ]},
]

# Artefacts qui appartiennent à une famille sans y avoir de ligne propre : la
# carte ne montre que ce que l'auteur peut ouvrir, et un référentiel replié ou
# une vue de travail interne n'a pas à encombrer sa lecture. Le classement, lui,
# doit être total : tout artefact déclaré porte une famille.
IMPLICITES = {
    'methode/prompt_disposition_cible.md': 'méthode',
    'methode/prompt_eval_disposition_cible.md': 'méthode',
    'methode/prompt_fil_strategie_machine.md': 'méthode',
    # --- déclarés le 20260903
    'methode/sas.md': 'méthode',
    'methode/banc_chouchous.md': 'méthode',
    'methode/banc_gl.md': 'méthode',
    'methode/prompt_fil_joueur_banc_gl.md': 'méthode',
    'reference/digestions_attendues.md': 'méthode',
    'reference/imposition_du_capital_fondapol.md': 'références externes',
    'reference/justice_fiscale_1789_fondapol.md': 'références externes',
    'reference/nomenclature_prelevements_ifrap.md': 'références externes',
    'reference/sourcage_ir_dgfip.md': 'références externes',
    'referentiels/articles_ouverts_plf.tsv': 'grilles',
    'referentiels/articles_ouverts_plfss.tsv': 'grilles',
    'livrables/eval_gl/reponses_vecteur_mesure_plf.json': 'bac à sable',
    'livrables/eval_gl/reponses_vecteur_mesure_plfss.json': 'bac à sable',
    'sources/accroche_politique_revision_20260901.md': 'références internes',
    'sources/prelevements_ifrap.tsv': 'références externes',
    # --- la relecture comparée des épreuves, 20260907
    # Le relevé d'écarts est une grille : une ligne par écart, que l'auteur
    # parcourt pour arbitrer. Ce n'est pas un rédactionnel — il ne se lit pas,
    # il se dépouille.
    'livrables/releve_epreuve_EP2.tsv': 'grilles',
    'livrables/releve_epreuve_EP2.md': 'grilles',
    # --- la digestion du texte déposé, 20260903
    # Les deux socles et leurs coupes sont des grilles : de la matière rangée
    # qu'un outil consomme, jamais un livrable qu'on lit.
    'referentiels/socle_plf_texte.json': 'grilles',
    'referentiels/socle_plfss_texte.json': 'grilles',
    'referentiels/redaction_plf.json': 'grilles',
    'referentiels/redaction_plfss.json': 'grilles',
    'referentiels/articles_ouverts_plf.json': 'grilles',
    'referentiels/articles_ouverts_plfss.json': 'grilles',
    'livrables/articles_ouverts_plf.txt': 'bac à sable',
    'livrables/articles_ouverts_plfss.txt': 'bac à sable',
    # --- absorbés du sas de la lecture en creux, 20260902
    'appareil/socle_plf_texte.py': 'outillage',
    'appareil/plages_articles.py': 'outillage',
    'appareil/lecture_en_creux.py': 'outillage',
    'appareil/portes_domaine_lfss.py': 'grilles',
    'referentiels/plages_articles.json': 'grilles',
    'referentiels/lecture_en_creux_plf.json': 'grilles',
    'referentiels/lecture_en_creux_plfss.json': 'grilles',
    'livrables/plages_articles.txt': 'bac à sable',
    'livrables/lecture_en_creux_plf.txt': 'bac à sable',
    'livrables/lecture_en_creux_plfss.txt': 'bac à sable',
    'livrables/portes_domaine_lfss.md': 'bac à sable',
    'methode/passation_lecture_en_creux.md': 'méthode',
    'methode/passation_site.md': 'méthode',
    'methode/regle_enonces_eval.md': 'méthode',
    'appareil/controle_lexique.py': 'outillage',
    'appareil/controle_generateurs.py': 'outillage',
    'livrables/eval_disposition/enonces.json': 'bac à sable',
    'livrables/eval_disposition/releve.json': 'bac à sable',
    'livrables/eval_disposition/notation.json': 'bac à sable',
    'methode/inventaire_coffre.tsv': 'méthode',
    # --- machine à amendements, 20260902
    'methode/contrat_chaine_amendement.md': 'méthode',
    'referentiels/lots_epreuve.json': 'grilles',
    'livrables/etat_machine.html': 'graphique',
    # Digestions et relevés écrits par nous et vérifiables contre une source
    # externe : ce sont des références, et elles sont internes au corpus.
    'reference/gabarit_expose_sommaire.md': 'méthode',
    'reference/depot_droit.md': 'méthode',
    'reference/domaine_lfss_LO111-3.md': 'références externes',
    'reference/passation_droit_renvois.md': 'méthode',
    # Rapport de clôture gelé, renommé le 20260902.
    'sources/rapport_gagnants_perdants_20260820.md': 'références internes',
    'referentiels/positions.json': 'grilles',
    'referentiels/socle_budgetaire.json': 'grilles',
    'referentiels/reconciliation_operateurs.json': 'grilles',
    'referentiels/economies.json': 'grilles',
    'livrables/reconciliation_operateurs.txt': 'bac à sable',
    'livrables/economies_tracees.txt': 'bac à sable',
    'methode/grille_lecture_budgetaire.md': 'méthode',
    'referentiels/notes_manuscrit.json': 'grilles',
    'livrables/interface_positions.html': 'bac à sable',
    'livrables/inventaire_gagnants_perdants.html': 'bac à sable',
    'livrables/ref_doctrine_arbre.html': 'bac à sable',
    'livrables/notes_manuscrit_releve.txt': 'bac à sable',
    'livrables/releve_protos.txt': 'bac à sable',
    'livrables/appariement_operateurs.txt': 'bac à sable',
    'livrables/synthese_budgetaire.xlsx': 'bac à sable',
    'livrables/donnees.json': 'bac à sable',
    'livrables/carte_attribution.html': 'bac à sable',
    'appareil/manifeste.py': 'grilles',
    'appareil/portes_domaine.py': 'grilles',
    'appareil/ventilation_vehicule.py': 'grilles',
    'appareil/axe_transparence.py': 'outillage',
    'appareil/porter_bloc.py': 'outillage',
    'livrables/portes_domaine.md': 'bac à sable',
    'livrables/axe_transparence.md': 'bac à sable',
    'livrables/ventilation_vehicule.md': 'bac à sable',
    'appareil/leviers_collocs.py': 'grilles',
    'appareil/chantier_vecteurs.py': 'outillage',
    'livrables/leviers_collocs.md': 'bac à sable',
    'livrables/chantier_vecteurs.md': 'bac à sable',
    'appareil/vecteurs.py': 'grilles',
    'appareil/ref_norme.py': 'outillage',
    'appareil/controle_norme.py': 'outillage',
    'referentiels/REF_norme.json': 'grilles',
    'livrables/etat_vecteurs.html': 'graphique',
    'livrables/etat_vecteurs.csv': 'grilles',
}

# La carte se lit en haut du projet, hors famille : elle est la vue, non une
# pièce de ce qu'elle range.
# Deux artefacts sont **délibérément** hors famille : la carte, qui est la vue
# et non une pièce de ce qu'elle range, et la feuille de route, qui dit ce qu'on
# produit et ne se range pas dans ce qu'on produit. `controle_index.py` les lit
# ici, faute de quoi il les sortirait en anomalie à chaque exécution.
HORS_FAMILLE = {'livrables/carte_du_projet.html',
                'methode/feuille_de_route.md'}

# Tout artefact de ce rang qui n'est ni une grille rédigée ni hors famille
# relève de l'outillage. Écrit en règle plutôt qu'en liste : une pièce
# d'appareil nouvelle se classe alors sans qu'on y pense.
FAMILLE_PAR_RANG = {'appareil': 'outillage'}

# ------------------------------------------------------------ reste à produire
# (produit, spécification, genre de spécification, état)
RESTE = [
    ('Fiches mesures', 'fiche-mesure', 'spec',
     '54 annoncées, aucune régénérée depuis les contrôles.'),
    ('Q&A', 'qa-riposte', 'spec',
     '152 questions antérieures aux contrôles, redescendues en matière.'),
    ('Propositions organique et ordinaire', 'redaction-legistique', 'spec',
     'aucun véhicule au-delà de la révision constitutionnelle.'),
    ('Site, vitrine du manuscrit', 'à spécifier', 'au',
     'sur le modèle de la page de garde. L’extrait en deviendrait une page.'),
    ('Infographies de diffusion', 'à spécifier', 'au',
     'aucune n’existe dans le projet.'),
    ('Charte graphique', 'à spécifier', 'au',
     'appelle la couverture du livre.'),
    ('Analyse du projet de loi de finances', 'à spécifier', 'au',
     'les trois classeurs d’entrée sont au projet.'),
]

CSS = """
:root{--enc:#1a1a1a;--pap:#fdfcfa;--fil:#ddd7cd;--vert:#1f5c3a;--rouge:#8a2f22;
--ocre:#6b5b3e;--gris:#6d6a64}
*{box-sizing:border-box}
body{margin:0;padding:2.4rem 1.4rem 5rem;background:var(--pap);color:var(--enc);
font:16px/1.6 Georgia,"Iowan Old Style",serif;max-width:58rem;margin-inline:auto}
h1{font-size:1.9rem;line-height:1.2;margin:0 0 .4rem;font-weight:600}
.chapeau{color:var(--gris);font-size:.95rem;margin:0 0 2rem}
h2{font-size:1.45rem;margin:3rem 0 .3rem;padding-bottom:.35rem;
border-bottom:3px solid var(--enc);font-weight:600;letter-spacing:.02em}
h3{font-size:1.02rem;margin:1.8rem 0 .2rem;font-weight:600;color:var(--ocre);
text-transform:uppercase;letter-spacing:.07em;font-family:system-ui,sans-serif}
h3 .n{float:right;font-family:"JetBrains Mono",Consolas,monospace;
font-size:.72rem;color:var(--gris);font-weight:400;text-transform:none;
letter-spacing:0}
.intro{font-size:.92rem;color:var(--gris);margin:.4rem 0 .8rem}
table{width:100%;border-collapse:collapse;font-size:.89rem;margin:.5rem 0 1.2rem}
th{text-align:left;font-family:system-ui,sans-serif;font-size:.7rem;
text-transform:uppercase;letter-spacing:.06em;color:var(--ocre);
border-bottom:1.5px solid var(--enc);padding:.3rem .5rem .25rem}
td{border-bottom:1px solid var(--fil);padding:.42rem .5rem;vertical-align:top}
td.t{font-weight:600;width:17rem}
td.m{font-family:"JetBrains Mono",Consolas,monospace;font-size:.74rem;
color:var(--gris);width:15rem;word-break:break-all}
.b{display:inline-block;font-family:system-ui,sans-serif;font-size:.66rem;
padding:.06rem .38rem;border:1px solid;border-radius:2px;white-space:nowrap}
.b-pj{border-color:var(--ocre);background:#f7f3e8;color:#5a4c30}
.b-ge{border-color:var(--gris);background:#f2f2f0;color:#55534e}
.b-au{border-color:var(--rouge);background:#fbeae7;color:#7a2519;font-weight:600}
.manque{background:#fbeae7;border-left:3px solid var(--rouge);
padding:.6rem 1rem;margin:.8rem 0}
.manque p{margin:.25rem 0;font-size:.9rem}
.manque .q{font-weight:600}
.regime{background:#f6f2ea;border-left:3px solid var(--enc);
padding:.8rem 1.1rem;margin:1.2rem 0;font-size:.92rem}
.regime p{margin:.35rem 0}
.avert{background:#f6f2ea;border:1px solid var(--fil);padding:.7rem 1rem;
margin:1.4rem 0;font-size:.86rem;color:var(--gris)}
footer{margin-top:3.5rem;padding-top:.9rem;border-top:1px solid var(--fil);
color:var(--gris);font-size:.8rem}
"""


def e(x):
    return html.escape(str(x), quote=False) if x is not None else ''


# ------------------------------------------------------------------ classement
def affectation():
    """chemin de dépôt → famille. Le seul point de vérité du classement."""
    par_chemin = {}
    for bloc in FAMILLES:
        for fam in bloc['familles']:
            for _titre, chemins, _adr, _propos in fam['lignes']:
                for c in chemins:
                    par_chemin[c] = fam['titre'].lower()
    par_chemin.update(IMPLICITES)
    return par_chemin


def famille_de(artefact, table):
    """La famille d'un artefact : sa ligne de carte, sa règle de rang, ou rien."""
    c = artefact['chemin']
    if c in HORS_FAMILLE:
        return None
    if c in table:
        return table[c]
    return FAMILLE_PAR_RANG.get(artefact['rang'])


# --------------------------------------------------------------------- adresse
def adresse(chemins, forcee, index):
    """La colonne « adresse » : où la chose vit réellement, au coffre."""
    if forcee is not None:
        if forcee[0] == 'au':
            return f'<span class="b b-au">{e(forcee[1])}</span>'
        if forcee[0] == 'archive':
            plis = sorted({x['chemin_coffre'] for x in index['archives']})
            return e(', '.join(plis))
    par_chemin = {a['chemin']: a for a in index['artefacts']}
    a = par_chemin[chemins[0]]
    plis = {x['chemin_coffre'] for x in index['archives']}
    if a['chemin_coffre'] in plis:
        return f'<span class="b b-ge">replié</span> {e(a["chemin_coffre"])}'
    if a['rang'] == 'source' and not a['coffre']:
        return '<span class="b b-pj">pièce jointe</span>'
    return e(a['chemin_coffre'])


def compte(fam, familles_index):
    if fam['compte'] is None:
        return str(len(fam['lignes']))
    if fam['compte'] == 'archives+pieces':
        n = len(familles_index.get(fam['titre'].lower(), []))
        return f'1 archive, {n} pièces'
    return fam['compte']


# --------------------------------------------------------------- la génération
def generer(src_index, dst):
    index = json.load(open(src_index, encoding='utf-8'))
    table = affectation()
    par_famille = {}
    for a in index['artefacts']:
        f = famille_de(a, table)
        if f:
            par_famille.setdefault(f, []).append(a['chemin'])

    o = ['<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         '<title>Carte du projet Résolution</title>',
         '<style>' + CSS + '</style></head><body>',
         '',
         '<h1>Carte du projet</h1>',
         '<p class="chapeau">Tout ce que le chantier porte, rangé par contenu. '
         'Trois surfamilles — ce qui entre, ce avec quoi on travaille, ce qui '
         'sort. Un seul fichier à ouvrir.</p>',
         '',
         '<div class="regime">',
         '<p><b>Ce classement est la vue.</b> Les adresses techniques des '
         'fichiers ne suivent pas : déplacer un document du projet suppose de '
         'le recopier entièrement, et recopier le manuscrit ou un texte '
         'normatif risquerait d’en altérer le verbatim. La colonne '
         '<i>adresse</i> dit où chaque chose vit réellement.</p>',
         '<p><b>Une matière de fond et le document qu’on en tire sont deux '
         'artefacts.</b> Ils ne se rangent jamais ensemble. Le texte à trois '
         'colonnes est de l’input, les propositions de loi qui en sortent sont '
         'de l’output.</p>',
         '<p><b>Un output gelé et validé monte en input.</b> C’est la '
         'promotion : il devient la strate sur laquelle s’appuient les '
         'suivantes.</p>',
         '</div>']

    for bloc in FAMILLES:
        o.append('')
        o.append(f'<h2>{e(bloc["surfamille"])}</h2>')
        o.append(f'<p class="intro">{bloc["intro"]}</p>')
        for fam in bloc['familles']:
            o.append('')
            o.append(f'<h3>{e(fam["titre"])}'
                     f'<span class="n">{compte(fam, par_famille)}</span></h3>')
            o.append(f'<p class="intro">{fam["intro"]}</p>')
            entetes = ''.join(f'<th>{e(c)}</th>' for c in fam['colonnes'])
            o.append(f'<table><tr>{entetes}</tr>')
            for titre, chemins, forcee, propos in fam['lignes']:
                cellules = [f'<td class="t">{e(titre)}</td>',
                            f'<td class="m">{adresse(chemins, forcee, index)}</td>']
                if len(fam['colonnes']) > 2:
                    cellules.append(f'<td>{e(propos)}</td>')
                o.append('<tr>' + ''.join(cellules) + '</tr>')
            o.append('</table>')
            if fam['apres']:
                o.append(f'<p class="intro">{fam["apres"]}</p>')

    # ------------------------------------------------------------- ce qui manque
    manq = index.get('manquants', [])
    o.append('')
    o.append('<h2>Ce qui manque</h2>')
    for m in manq:
        o.append('')
        o.append(f'<div class="manque"><p class="q">{e(m["intitule"])}</p>'
                 f'<p>{e(m["motif"])}</p></div>')

    # -------------------------------------------------------- reste à produire
    o.append('')
    o.append('<h2>Ce qui reste à produire</h2>')
    o.append('<table><tr><th>produit</th><th>spécifié par</th><th>état</th></tr>')
    for produit, spec, genre, etat in RESTE:
        cellule = (e(spec) if genre == 'spec'
                   else f'<span class="b b-au">{e(spec)}</span>')
        o.append(f'<tr><td class="t">{e(produit)}</td>'
                 f'<td class="m">{cellule}</td><td>{e(etat)}</td></tr>')
    o.append('</table>')

    o.append('')
    o.append('<footer>Classement par contenu validé bloc à bloc le 20260821. '
             'Voir <code>methode/classement_corpus.md</code> pour les règles, '
             '<code>methode/arbitrages.md</code> pour les décisions.</footer>')
    o.append('</body></html>')

    open(dst, 'w', encoding='utf-8').write('\n'.join(o) + '\n')

    total = sum(len(v) for v in par_famille.values())
    sans = [a['chemin'] for a in index['artefacts']
            if not famille_de(a, table) and a['chemin'] not in HORS_FAMILLE]
    print(f'{dst} écrit — {len(par_famille)} familles, {total} artefacts '
          f'classés, {len(manq)} renvoi(s) mort(s)')
    if sans:
        print(f'    {len(sans)} artefact(s) sans famille :')
        for c in sans:
            print(f'        {c}')
    return 0


if __name__ == '__main__':
    sys.exit(generer(sys.argv[1], sys.argv[2]))
