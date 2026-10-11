# -*- coding: utf-8 -*-
"""Index de résolution des renvois — le seul point où un nom de fichier s'écrit.

Le chantier a été tenu pendant des mois sur des noms horodatés, `Nom_AAAAMMJJ_vN`.
Cette convention a produit trois maux : des consommateurs qui pointent une version
périmée, des doublons qui survivent à côté de leur remplaçante, et des inventaires
qui rouillent dès qu'un fichier bouge.

La règle est désormais inverse. **Un nom canonique par artefact, aucun horodatage.**
L'historique est porté par git, jamais par le nom. Deux fichiers qui ne diffèrent
que par un `_vN` : l'un des deux est un déchet, et il se supprime.

Cet index est la table de résolution. Chaque artefact y porte :

  role          la clé stable par laquelle on le désigne, y compris dans les skills
  chemin        son unique emplacement dans le dépôt
  rang          strate1 · referentiel · appareil · derive · methode · source
  coffre        vrai si l'artefact survit aux sessions sur une surface
                permanente — le coffre, ou le dépôt depuis le 20260909. Le champ
                dit la durabilité ; `voie` dit sur laquelle des deux.
  produit_par   le générateur qui le refait, ou null s'il s'écrit à la main
  consomme_par  ce qui le lit — générateurs, contrôles, skills
  alias         les noms horodatés qu'il remplace, pour que tout renvoi ancien résolve
  famille       sa famille du classement par contenu, reportée de la carte
  restaurable   faux si nul script ne peut le remettre au dépôt
  voie          la surface qui le rend — coffre · depot · piece_jointe · hors_coffre
  chemin_coffre où il se lit **sur sa voie** : son chemin au coffre, un chemin
                préfixé, ou son chemin dans le dépôt de droit sous `chantier/`

**La voie de restauration est un champ, et elle n'est plus déductible du rang.**
Jusqu'au 20260909, tout ce qui portait le rang `appareil` ou `referentiel` était
replié dans une archive unique du coffre, `technique/coffre.txt`. Cette archive a
été versée au dépôt et supprimée du coffre le 20260909 (A-395), après preuve à
l'octet 80 sur 80. Le chemin n'existe plus, et quatre-vingts artefacts le
déclaraient encore : `coffre.py deplier` n'avait plus d'archive à lire et
`restaurer.py` cherchait au transcript des documents que le coffre ne porte plus.

Ils se restaurent désormais par **copie d'octets depuis le clone du dépôt** —
`voie: depot` — et leur `chemin_coffre` donne leur chemin dans ce dépôt. Le bloc
`depot` de l'index porte la commande de clone, la sous-racine et la liste des
chemins ; il remplace l'ancien bloc `archives`.

L'index est lui-même un dérivé : il ne se corrige pas à la main, il se régénère.
La table curée vit ici, dans l'appareil, au même titre que `GROUPES` et `EVENTAIL`.

Deux choses ne s'écrivent pas ici. **L'affectation aux familles vit dans
`generer_carte.py`** : l'index l'importe et la reporte, il ne la redouble pas.
**Les sources ne se relèvent plus de l'arborescence** : le balayage faisait
dépendre la table de résolution de ce qu'un conteneur contenait ce jour-là, et
une pièce jointe non restaurée y disparaissait sans bruit.

**Le dossier se lit depuis le 20261009.** Les tables ne suffisaient plus : tout
fichier versé sans ligne à la table sortait en I2, 182 au versement du jour. Le
générateur parcourt donc la racine au périmètre de `controle_index.fichiers` et
déclare à son chemin, voie `depot`, tout fichier que les tables ne portent pas
(champ `releve`). Le balayage ajoute, il ne retire rien : une pièce déclarée
absente du conteneur reste à l'index. Un fichier relevé n'a pas de famille tant
que `generer_carte.py` ne lui en donne pas, et I5 le dit.

Usage : python3 generer_index.py ../methode/index.json ..
"""
import json
import os
import sys

import controle_index
import generer_carte

REVISION = {'version': 'index v1', 'date': '20260821',
            'regle': "Un nom canonique par artefact, aucun horodatage. "
                     "L'historique vit dans git, pas dans le nom."}

# role, chemin, rang, coffre, produit_par, consomme_par, alias horodatés
ARTEFACTS = [
    # ---------------------------------------------------------------- strate 1
    #
    # Deux artefacts portent la strate 1 depuis le 20260911, et ils ne
    # répondent pas à la même question.
    #
    # Le **manuscrit** est la strate 1 de la *doctrine* : c'est sur lui que le
    # référentiel de doctrine, les notes et les chiffres sont ancrés, et il ne
    # bouge pas. Il reste aussi le troisième terme de tout relevé d'épreuve —
    # celui qui dit de quel côté un écart déplace le texte.
    #
    # Le **livre imprimé** est la strate 1 du *verbatim citable* : depuis que
    # l'auteur a validé la troisième épreuve, ce qui se cite du livre se cite
    # de lui, et jamais du manuscrit. Entre les deux, 858 écarts relevés le
    # 20260908 : citer le manuscrit, c'est désormais mal citer le livre.
    #
    # Ce n'est pas deux points de vérité pour un même fait : c'est un point de
    # vérité par question. `consomme_par` porte le départage, et c'est là qu'il
    # se lit.
    ('manuscrit', 'manuscrit/manuscrit.html', 'strate1', True, None,
     ['extraire_notes.py', 'relevé d’épreuve — troisième terme',
      'toute skill qui cite un verbatim de la doctrine'],
     ['Manuscrit_20260820_v4.html']),
    ('livre', 'livre/texte_livre.json', 'strate1', True,
     'appareil/texte_livre.py',
     ['toute skill qui cite un verbatim du livre', 'audit-conformite',
      'controle_chiffres.py'],
     []),

    # ------------------------------------------------------------ référentiels
    ('ref_doctrine', 'referentiels/REF_doctrine.json', 'referentiel', True, None,
     ['construire_positions.py', 'exporter_donnees.py', 'generer_extrait.py',
      'generer_inventaire.py', 'generer_arbre.py', 'controle_structurel.py',
      'controle_arithmetique.py', 'controle_notes.py',
      'fiche-mesure', 'compatibilite-doctrine', 'contestabilite', 'qa-riposte',
      'audit-conformite'],
     ['REF_doctrine_20260820_v20.json', 'REF_doctrine_20260820_v19.json']),
    # Sorti du coffre le 20260904, sur arbitrage de l'auteur (A-357). Il se
    # régénère à l'identique à l'octet depuis le seul `REF_doctrine`, avec
    # `justifications.py` et `apports.py`, tous trois au coffre : la preuve est
    # faite avant le retrait, jamais affirmée.
    ('positions', 'referentiels/positions.json', 'referentiel', False,
     'appareil/construire_positions.py',
     ['exporter_donnees.py', 'generer_extrait.py', 'generer_inventaire.py',
      'controle_notes.py', 'fiche-mesure', 'compatibilite-doctrine',
      'contestabilite', 'qa-riposte', 'audit-conformite'],
     ['Positions_20260820_v16.json']),
    # Non versé au coffre, et c'est voulu : il se régénère à l'identique depuis
    # quatre artefacts qui y sont tous — les notes, le REF_doctrine, le proto
    # Données, et `sources_chiffres.py` qui porte la seule part écrite à la
    # main. Le verser ajouterait 280 ko au coffre sans rien y sauver.
    ('ref_chiffres', 'referentiels/REF_chiffres.json', 'referentiel', False,
     'appareil/generer_ref_chiffres.py',
     ['controle_chiffres.py', 'audit-conformite', 'fiche-mesure',
      'qa-riposte', 'contestabilite', 'compatibilite-doctrine',
      'tout livrable chiffré'],
     []),
    ('notes_manuscrit', 'referentiels/notes_manuscrit.json', 'referentiel', True,
     'appareil/extraire_notes.py',
     ['exporter_donnees.py', 'generer_extrait.py', 'generer_inventaire.py',
      'controle_notes.py', 'generer_releve_notes.py', 'fiche-mesure',
      'compatibilite-doctrine', 'qa-riposte', 'audit-conformite'],
     ['Notes_manuscrit_20260820_v1.json']),

    # ---------------------------------------------------------------- appareil
    ('construire_positions', 'appareil/construire_positions.py', 'appareil', True,
     None, ['make'], ['construire_positions_20260820_v16.py']),
    ('justifications', 'appareil/justifications.py', 'appareil', True,
     None, ['construire_positions.py'], ['justifications_20260820_v6.py']),
    ('apports', 'appareil/apports.py', 'appareil', True,
     None, ['construire_positions.py'], ['apports_20260820_v1.py']),
    ('exporter_donnees', 'appareil/exporter_donnees.py', 'appareil', True,
     None, ['make'], ['exporter_donnees_20260820_v1.py']),
    ('generer_extrait', 'appareil/generer_extrait.py', 'appareil', True,
     None, ['make'], ['generer_extrait_20260820_v9.py',
                      'generer_extrait_20260820_v8.py']),
    ('generer_interface', 'appareil/generer_interface.py', 'appareil', True,
     None, ['make'], ['generer_interface_20260820_v8.py']),
    ('generer_inventaire', 'appareil/generer_inventaire.py', 'appareil', True,
     None, ['make'], ['generer_inventaire_20260820_v6.py',
                      'generer_inventaire_20260820_v5.py']),
    ('manifeste_corrections', 'appareil/manifeste.py', 'appareil', True,
     None, ['generer_site.py'], []),
    ('generer_site', 'appareil/generer_site.py', 'appareil', True,
     None, ['make'], []),
    ('generer_arbre', 'appareil/generer_arbre.py', 'appareil', True,
     None, ['make'], ['generer_arbre_20260820_v2.py']),
    ('generer_releve_notes', 'appareil/generer_releve_notes.py', 'appareil', True,
     None, ['make'], []),
    ('generer_ref_chiffres', 'appareil/generer_ref_chiffres.py', 'appareil',
     True, None, ['make'], []),
    ('relever_protos', 'appareil/relever_protos.py', 'appareil', True,
     None, ['make'], []),
    ('socle_budgetaire', 'appareil/socle_budgetaire.py', 'appareil', True,
     None, ['make'], []),
    ('controle_socle', 'appareil/controle_socle.py', 'appareil', True,
     None, ['make controle'], []),
    ('apparier_operateurs', 'appareil/apparier_operateurs.py', 'appareil', True,
     None, ['make'], []),
    ('reconcilier_operateurs', 'appareil/reconcilier_operateurs.py', 'appareil',
     True, None, ['make'], []),
    ('tracer_economies', 'appareil/tracer_economies.py', 'appareil', True,
     None, ['make', 'make controle'], []),
    # Jeu de fautes et jeu de justes de S17 (restitution salariale, 30 % en
    # année 1 et 70 % au solde). Autonome pour l'instant : le fichier où il
    # doit se fondre, `appareil/epreuve_controle_socle.py`, porte les sept
    # bouclages du second cercle et n'est pas au dépôt.
    ('epreuve_s17_salaire', 'appareil/epreuve_s17_salaire.py', 'appareil',
     True, None, ['controle_socle.py'], []),
    ('nomenclature_lolf', 'appareil/nomenclature_lolf.py', 'appareil', True,
     None, ['socle_budgetaire.py', 'make controle'], []),
    ('generer_classeur_synthese', 'appareil/generer_classeur_synthese.py',
     'appareil', True, None, ['make'], []),
    ('hypotheses_doctrine', 'appareil/hypotheses_doctrine.py', 'appareil', True,
     None, ['controle_hypotheses.py', 'fiche-mesure', 'audit-conformite',
            'contestabilite', 'compatibilite-doctrine'], []),
    ('controle_hypotheses', 'appareil/controle_hypotheses.py', 'appareil', True,
     None, ['make controle'], []),
    ('sources_chiffres', 'appareil/sources_chiffres.py', 'appareil', True,
     None, ['generer_ref_chiffres.py', 'controle_chiffres.py'], []),
    ('controle_chiffres', 'appareil/controle_chiffres.py', 'appareil', True,
     None, ['make controle'], []),
    ('controle_apports', 'appareil/controle_apports.py', 'appareil', True,
     None, ['make controle'], []),
    ('generer_fiches', 'appareil/generer_fiches.py', 'appareil', True,
     None, ['make', 'galerie des fiches'], ['proto_fiches.py']),
    ('carte_attribution_py', 'appareil/carte_attribution.py', 'appareil', True,
     None, ['structuration des fiches'], []),
    ('structure_fiches', 'appareil/structure_fiches.py', 'appareil', True,
     None, ['generer_fiches.py', 'carte_attribution.py'], []),
    # Les quatre modules du premier fil de production du contre-PLF. Les deux
    # premiers portent de la matière écrite à la main — les repères des portes,
    # la ventilation ligne à ligne — et se rangent en grilles ; les deux autres
    # ne font que placer et relever.
    ('portes_domaine', 'appareil/portes_domaine.py', 'appareil', True, None,
     ['make', 'pack public'], []),
    ('ventilation_vehicule', 'appareil/ventilation_vehicule.py', 'appareil',
     True, None, ['make'], []),
    ('leviers_collocs', 'appareil/leviers_collocs.py', 'appareil', True, None,
     ['make'], []),
    ('chantier_vecteurs', 'appareil/chantier_vecteurs.py', 'appareil', True,
     None, ['make', 'REF_norme'], []),
    ('vecteurs', 'appareil/vecteurs.py', 'appareil', True, None,
     ['ref_norme.py', 'controle_norme.py'], []),
    ('ref_norme_gen', 'appareil/ref_norme.py', 'appareil', True, None,
     ['make'], []),
    ('controle_norme', 'appareil/controle_norme.py', 'appareil', True, None,
     ['make controle'], []),
    ('generer_etat_vecteurs', 'appareil/generer_etat_vecteurs.py', 'appareil',
     True, None, ['make'], []),
    # L'éval de `vecteur-mesure` sur les liasses GL. Les trois se rejouent
    # ensemble, les PDF rentrant par pièce jointe : ce qui se verse est
    # l'appareil, jamais les exposés extraits ni les clés (A-71, A-266).
    ('scinder_liasses', 'appareil/scinder_liasses.py', 'appareil', True, None,
     ['éval des liasses GL'], []),
    ('cles_eval_gl', 'appareil/cles_eval_gl.py', 'appareil', True, None,
     ['noter_eval_gl.py'], []),
    ('noter_eval_gl', 'appareil/noter_eval_gl.py', 'appareil', True, None,
     ['éval des liasses GL'], []),
    ('controle_cles_gl', 'appareil/controle_cles_gl.py', 'appareil', True, None,
     ['make controle', 'banc des liasses déposées'], []),
    # L'éval en sens inverse : le dispositif est donné, l'exposé est scellé.
    # Même corpus, même appareil, direction opposée — et non contaminée, aucun
    # fil n'ayant lu les exposés comme sorties attendues.
    ('cles_eval_expose', 'appareil/cles_eval_expose.py', 'appareil', True, None,
     ['noter_eval_expose.py'], []),
    ('noter_eval_expose', 'appareil/noter_eval_expose.py', 'appareil', True,
     None, ["éval inverse d'expose-sommaire"], []),
    ('axe_transparence', 'appareil/axe_transparence.py', 'appareil', True, None,
     ['make'], []),
    ('porter_bloc', 'appareil/porter_bloc.py', 'appareil', True,
     None, ['emploi manuel'], []),
    ('generer_index', 'appareil/generer_index.py', 'appareil', True,
     None, ['make'], []),
    ('generer_carte', 'appareil/generer_carte.py', 'appareil', True,
     None, ['make'], []),
    ('coffre', 'appareil/coffre.py', 'appareil', True,
     None, ['make coffre', 'ouverture de session'], []),
    ('extraire_notes', 'appareil/extraire_notes.py', 'appareil', True,
     None, ['make'], ['extraire_notes_20260820_v1.py']),
    ('canoniser_ref', 'appareil/canoniser_ref.py', 'appareil', True,
     None, ['emploi manuel'], ['canoniser_ref.py']),
    ('controle_structurel', 'appareil/controle_structurel.py', 'appareil', True,
     None, ['make controle'], ['controle_structurel.py']),
    ('controle_arithmetique', 'appareil/controle_arithmetique.py', 'appareil', True,
     None, ['make controle', 'generer_arbre.py'], ['controle_arithmetique.py']),
    ('controle_notes', 'appareil/controle_notes.py', 'appareil', True,
     None, ['make controle'], ['controle_notes_20260820_v2.py',
                               'controle_notes_20260820_v1.py']),
    ('controle_sortie', 'appareil/controle_sortie.py', 'appareil', True,
     None, ['fiche-mesure', 'qa-riposte', 'contestabilite',
            'compatibilite-doctrine', 'audit-conformite'],
     ['controle_sortie.py']),
    # Successeur de `controle_projet`, dont l'objet a changé : ce n'est plus un
    # montage qu'on vérifie mais la concordance arborescence / index / nommage.
    # L'ancêtre est gelé en archive, il ne se résout donc pas par alias.
    ('controle_generateurs', 'appareil/controle_generateurs.py', 'appareil',
     True, None, ['make generateurs', 'clôture de fil'], []),
    ('controle_index', 'appareil/controle_index.py', 'appareil', True,
     None, ['make controle', 'make index'], []),

    # Le coffre rend ses documents en texte, jamais en octets : une restauration
    # repasse par le modèle et normalise sans le dire. L'empreinte relevée au
    # versement est la seule référence à quoi comparer ce qui revient.
    ('empreintes_gen', 'appareil/empreintes.py', 'appareil', True,
     None, ['make coffre'], []),
    ('restaurer', 'appareil/restaurer.py', 'appareil', True,
     None, ['ouverture de session'], []),
    ('controle_restauration', 'appareil/controle_restauration.py', 'appareil',
     True, None, ['make restauration', 'ouverture de session'], []),
    # Le contrôle `G` : une skill ne nomme ni déposant, ni projet, ni corpus
    # interne, et elle dit ce qu'elle rend socle absent.
    ('controle_generalisation', 'appareil/controle_generalisation.py',
     'appareil', True, None, ['make controle', 'make G'], []),
    # --- absorbés du sas de la lecture en creux, 20260902
    ('socle_plf_texte', 'appareil/socle_plf_texte.py', 'appareil', True, None,
     ['make', 'socle du texte déposé'], []),
    ('plages_articles_gen', 'appareil/plages_articles.py', 'appareil', True,
     None, ['make', 'préparation des amendements'], []),
    ('lecture_en_creux_gen', 'appareil/lecture_en_creux.py', 'appareil', True,
     None, ['make', 'lecture en creux'], []),
    ('portes_domaine_lfss_gen', 'appareil/portes_domaine_lfss.py', 'appareil',
     True, None, ['make', 'test de rattachement', 'pack public'], []),
    ('etat_machine', 'appareil/etat_machine.py', 'appareil', True, None,
     ['make'], []),
    # --- la digestion du texte déposé, 20260903
    # Réécrit ce jour : il était invoqué par le Makefile, déclaré manquant, et
    # absent du dépôt comme du coffre. Les deux tables versées donnaient sa
    # sortie attendue à l'octet, et le réemploi s'est prouvé dessus.
    ('articles_ouverts_plf_gen', 'appareil/articles_ouverts_plf.py',
     'appareil', True, None, ['make', 'REF_norme', 'vecteur-mesure'], []),
    # La coupe du socle : ce qui se verse au coffre quand le socle entier ne
    # tient pas à la jauge (A-342, clause de repli).
    ('redaction_deposee_gen', 'appareil/redaction_deposee.py', 'appareil',
     True, None, ['make', 'versement du socle'], []),
    # Le partage calibrage / épreuve du banc de la rédaction (A-330). La règle
    # de sélection vit ici, et non dans le fil qui écrit la skill.
    ('partage_calibrage', 'appareil/partage_calibrage.py', 'appareil', True,
     None, ['make', "banc d'épreuve", 'disposition-cible'], []),
    # Le contrôle de réapplication et ses trois cas travaillés (20260904).
    # Versés comme documents et non dans l'archive, le fil qui les a écrits
    # n'ayant pas replié le coffre : l'archive est partie au dépôt sans eux le
    # 20260909, et **ils l'ont rejointe le même jour** (fusion `31896bb5`).
    # Voie `depot` depuis, comme tout le reste de l'appareil.
    ('reappliquer', 'appareil/reappliquer.py', 'appareil', True, None,
     ['disposition-cible', "banc d'épreuve"], []),
    ('cas_disposition', 'appareil/cas_disposition.py', 'appareil', True, None,
     ['reappliquer.py', 'disposition-cible'], []),
    # L'éval de la rédaction cible, jouée le 20260904. Cinq modules : le tirage,
    # l'unité de notation, la préparation du banc aveugle, le contrôle des
    # entrées, la notation.
    ('echantillon_epreuve', 'appareil/echantillon_epreuve.py', 'appareil', True,
     None, ["éval de la rédaction cible"], []),
    # L'appareil de la relecture comparée des épreuves. Écrit le 20260907, il
    # n'avait pas été versé — le fil n'avait pas déplié l'archive, et le
    # journal l'a déclaré comme un manque. Le 20260908 il a été retrouvé au
    # transcript par rejeu de son écriture et de ses quatorze retouches, sans
    # aucun échec d'appariement, et prouvé : rejoué sur les mêmes entrées, il
    # rend `releve_bat.tsv`, `releve_bat.md` et le contrôle des chiffres à
    # l'octet près. Il se verse à l'archive.
    ('relever_ecarts_epreuve', 'appareil/relever_ecarts_epreuve.py',
     'appareil', True, None,
     ['rendre_releve_epreuve.py', 'relecture comparée des épreuves'], []),
    ('rendre_releve_epreuve', 'appareil/rendre_releve_epreuve.py',
     'appareil', True, None,
     ['relecture comparée des épreuves', 'bon à tirer'], []),
    # Le texte du livre imprimé, extrait mécaniquement de l'épreuve validée.
    # Il ne compare rien et ne relève aucun écart : il rend le verbatim, page
    # par page, ligne par ligne, et il porte le SHA de l'épreuve dont il sort.
    # Six contrôles internes, `T1` à `T6`, dont le dernier prouve qu'aucune
    # ligne du livre n'est perdue à l'extraction.
    ('texte_livre', 'appareil/texte_livre.py', 'appareil', True, None,
     ['make', 'strate 1 du verbatim citable'], []),
    ('blocs_disposition', 'appareil/blocs_disposition.py', 'appareil', True,
     None, ['preparer_eval_disposition.py', "éval de la rédaction cible"], []),
    ('preparer_eval_disposition', 'appareil/preparer_eval_disposition.py',
     'appareil', True, None, ["éval de la rédaction cible"], []),
    ('controle_enonces', 'appareil/controle_enonces.py', 'appareil', True, None,
     ["éval de la rédaction cible"], []),
    ('noter_eval_disposition', 'appareil/noter_eval_disposition.py', 'appareil',
     True, None, ["éval de la rédaction cible", "banc d'épreuve"], []),
    # Le lexique d'A-53, enfin joué — treize jours après avoir été déclaré porté.
    ('controle_lexique', 'appareil/controle_lexique.py', 'appareil', True, None,
     ['make controle', 'tout livrable diffusable'], []),

    # ---------------------------------------------------------------- dérivés
    # Deux dérivés sont versés au coffre bien qu'ils se régénèrent : ce sont
    # ceux que l'auteur ouvre, et il doit pouvoir les ouvrir entre deux sessions.
    # Les trois pièces de l'éval de la rédaction cible qui ne se régénèrent pas :
    # les énoncés sont écrits par des fils, le relevé porte ce que la skill a
    # rendu, la notation porte la mesure. Le terrain, l'échantillon et les
    # colonnes A et C se refont — ils ne se versent pas.
    ('eval_disposition_enonces', 'livrables/eval_disposition/enonces.json',
     'derive', True, None, ["rejeu de l'éval de la rédaction cible"], []),
    ('eval_disposition_releve', 'livrables/eval_disposition/releve.json',
     'derive', True, 'appareil/noter_eval_disposition.py',
     ["rejeu de l'éval de la rédaction cible", 'correction de E4'], []),
    ('eval_disposition_notation', 'livrables/eval_disposition/notation.json',
     'derive', True, 'appareil/noter_eval_disposition.py',
     ["banc d'épreuve", 'correction de E4'], []),
    ('carte_attribution', 'livrables/carte_attribution.html', 'derive', False,
     'appareil/carte_attribution.py', ['arbitrage de l’auteur'], []),
    # Retiré du coffre le 20260908. Rejeu prouvé à l'octet contre l'empreinte
    # versée : `make livrables/galerie_fiches.html` rend `30e64637…`, 35 539 o.
    # A-342 — un dérivé dont la source est au coffre ne s'y verse pas.
    ('galerie_fiches', 'livrables/galerie_fiches.html', 'derive', False,
     'appareil/generer_fiches.py', ['diffusion', 'site'],
     ['proto_fiche.html', 'proto_fiche_A.html', 'proto_fiche_B.html',
      'proto_fiche_C.html']),
    # Retiré du coffre le 20260908. Rejeu prouvé, avec une réserve nommée : la
    # page horodate son propre pied, donc elle ne se compare qu'à date égale.
    # Rejouée le 20260908 elle rend `7a9994e3…`, 90 277 o ; la même privée de
    # son horodatage rend exactement l'empreinte versée `557c74fe…`. A-342.
    ('extrait', 'livrables/extrait_gagnants_perdants.html', 'derive', False,
     'appareil/generer_extrait.py', ['diffusion'],
     ['Extrait_gagnants_perdants_20260820_v11.html',
      'Extrait_gagnants_perdants_20260820_v10.html']),
    ('interface', 'livrables/interface_positions.html', 'derive', False,
     'appareil/generer_interface.py', ['travail interne'],
     ['Interface_positions_20260820_v10.html',
      'Interface_positions_20260820_v9.html']),
    ('inventaire', 'livrables/inventaire_gagnants_perdants.html', 'derive', False,
     'appareil/generer_inventaire.py', ['travail interne'],
     ['Inventaire_gagnants_perdants_20260820_v10.html',
      'Inventaire_gagnants_perdants_20260820_v9.html']),
    ('arbre_ref', 'livrables/ref_doctrine_arbre.html', 'derive', False,
     'appareil/generer_arbre.py', ['lecture interne du référentiel'],
     ['REF_doctrine_arbre_20260820_v7.html']),
    ('releve_notes', 'livrables/notes_manuscrit_releve.txt', 'derive', False,
     'appareil/generer_releve_notes.py', ['lecture interne des notes'],
     ['Notes_manuscrit_releve_20260820_v1.txt']),
    ('socle_bud', 'referentiels/socle_budgetaire.json', 'referentiel', False,
     'appareil/socle_budgetaire.py',
     ['controle_socle.py', 'tout chiffrage budgétaire'], []),
    ('grille_budgetaire', 'methode/grille_lecture_budgetaire.md', 'methode',
     True, None, ['ouverture de session', 'socle_budgetaire.py'], []),
    ('reconciliation_operateurs', 'referentiels/reconciliation_operateurs.json',
     'referentiel', False, 'appareil/reconcilier_operateurs.py',
     ['generer_classeur_synthese.py', 'tout chiffrage opérateur'], []),
    ('reconciliation_lisible', 'livrables/reconciliation_operateurs.txt',
     'derive', False, 'appareil/reconcilier_operateurs.py',
     ["lecture de l'auteur"], []),
    ('economies', 'referentiels/economies.json', 'referentiel', False,
     'appareil/tracer_economies.py',
     ['controle_socle.py', 'reconcilier_operateurs.py',
      'generer_classeur_synthese.py'], []),
    ('economies_tracees', 'livrables/economies_tracees.txt', 'derive', False,
     'appareil/tracer_economies.py', ["lecture de l'auteur"], []),
    ('appariement_operateurs', 'livrables/appariement_operateurs.txt',
     'derive', False, 'appareil/apparier_operateurs.py',
     ['lecture interne', 'rattachement des opérateurs'], []),
    ('synthese_budgetaire', 'livrables/synthese_budgetaire.xlsx', 'derive',
     False, 'appareil/generer_classeur_synthese.py',
     ["lecture de l'auteur"], []),
    ('portes_domaine_md', 'livrables/portes_domaine.md', 'derive', False,
     'appareil/portes_domaine.py',
     ['test de rattachement', 'pack public', 'qualification des articles'], []),
    ('axe_transparence_md', 'livrables/axe_transparence.md', 'derive', False,
     'appareil/axe_transparence.py', ["arbitrage de l'auteur"], []),
    ('ventilation_vehicule_md', 'livrables/ventilation_vehicule.md', 'derive',
     False, 'appareil/ventilation_vehicule.py',
     ["arbitrage de l'auteur", 'phase PLFSS'], []),
    ('leviers_collocs_md', 'livrables/leviers_collocs.md', 'derive', False,
     'appareil/leviers_collocs.py',
     ["arbitrage de l'auteur", 'contre-PLF'], []),
    ('chantier_vecteurs_md', 'livrables/chantier_vecteurs.md', 'derive', False,
     'appareil/chantier_vecteurs.py',
     ["arbitrage de l'auteur", 'REF_norme'], []),
    # Le banc d'épreuve : un lot de référence par véhicule, sur lequel on rejoue
    # le taux de chaque étape. Écrit à la main, donc versé — aucun script ne le
    # dérive, et un taux ne s'y inscrit qu'après avoir été joué.
    ('plages_articles', 'referentiels/plages_articles.json', 'referentiel',
     False, 'appareil/plages_articles.py',
     ['portes_ouvertes.py', 'vecteur-mesure'], []),
    ('lecture_en_creux_plf', 'referentiels/lecture_en_creux_plf.json',
     'referentiel', False, 'appareil/lecture_en_creux.py',
     ['lecture en creux', 'contestabilite'], []),
    ('lecture_en_creux_plfss', 'referentiels/lecture_en_creux_plfss.json',
     'referentiel', False, 'appareil/lecture_en_creux.py',
     ['lecture en creux', 'contestabilite'], []),
    ('lots_epreuve', 'referentiels/lots_epreuve.json', 'referentiel', True,
     None, ['etat_machine.py', 'noter_eval_gl.py', 'noter_eval_expose.py',
            'toute éval de la chaîne'], []),
    ('ref_norme', 'referentiels/REF_norme.json', 'referentiel', False,
     'appareil/ref_norme.py',
     ['controle_norme.py', 'chantier_vecteurs.py', 'redaction-legistique',
      'tout amendement rédigé'], []),
    # Reste au coffre le 20260908, quand les quatre autres dérivés graphiques
    # en sortent, et c'est A-342 qui le retient : il descend de `REF_norme`,
    # donc du socle budgétaire, donc des cinq classeurs, qui sont des pièces
    # jointes et non des documents du coffre. Un dérivé dont la source n'est
    # pas au coffre ne se régénère pas depuis le coffre seul : il se verse.
    ('etat_vecteurs', 'livrables/etat_vecteurs.html', 'derive', True,
     'appareil/generer_etat_vecteurs.py', ["lecture de l'auteur"], []),
    ('plages_articles_releve', 'livrables/plages_articles.txt', 'derive', False,
     'appareil/plages_articles.py', ["lecture de l'auteur"], []),
    ('lecture_en_creux_plf_releve', 'livrables/lecture_en_creux_plf.txt',
     'derive', False, 'appareil/lecture_en_creux.py',
     ["lecture de l'auteur"], []),
    ('lecture_en_creux_plfss_releve', 'livrables/lecture_en_creux_plfss.txt',
     'derive', False, 'appareil/lecture_en_creux.py',
     ["lecture de l'auteur"], []),
    ('portes_domaine_lfss_md', 'livrables/portes_domaine_lfss.md', 'derive',
     False, 'appareil/portes_domaine_lfss.py',
     ['test de rattachement', 'pack public',
      'qualification des articles'], []),
    # Les deux socles du texte déposé, et la part de chacun qui se verse.
    #
    # A-342 a renversé la règle : un dérivé dont la source n'est pas au coffre
    # se verse, et le socle se régénère depuis une pièce jointe. Mesuré, le
    # socle entier de la loi de finances pèse 494 461 jetons pour une marge de
    # 310 550 : la clause de repli s'applique, et c'est sa part irréproductible
    # qui se verse — `referentiels/redaction_plf.json`. Le socle complet reste
    # un dérivé de l'atelier, régénérable depuis la pièce jointe.
    #
    # La loi de financement a sa part versée depuis le 20260903 : le retrait
    # des deux rapports tiers a rendu 172 190 jetons, et les 104 000 requis
    # rentraient. La dette d'A-346 est close le jour où elle a été écrite
    # (A-350).
    ('socle_plf_json', 'referentiels/socle_plf_texte.json', 'referentiel',
     False, 'appareil/socle_plf_texte.py',
     ['articles_ouverts_plf.py', 'redaction_deposee.py',
      'lecture_en_creux.py'], []),
    ('socle_plfss_json', 'referentiels/socle_plfss_texte.json',
     'referentiel', False, 'appareil/socle_plf_texte.py',
     ['articles_ouverts_plf.py', 'redaction_deposee.py',
      'lecture_en_creux.py'], []),
    # Les deux parts versées ont quitté le coffre pour le dépôt le 20260909,
    # fusion `31896bb5`. Elles y étaient comme documents parce qu'une pièce plus
    # grosse que l'archive ne s'y repliait pas (A-349) ; l'archive n'existe plus,
    # et le dépôt ne pèse rien à la jauge. Voie `depot`, sous `chantier/`.
    ('redaction_plf', 'referentiels/redaction_plf.json', 'referentiel', True,
     'appareil/redaction_deposee.py',
     ['partage_calibrage.py', 'disposition-cible', 'redaction-legistique'],
     []),
    ('redaction_plfss', 'referentiels/redaction_plfss.json', 'referentiel',
     True, 'appareil/redaction_deposee.py',
     ['partage_calibrage.py', 'disposition-cible', 'redaction-legistique'],
     []),
    # Les socles de texte 2027 — PLF n° 3210 et PLFSS n° 3211, 17e législature.
    # Domicile au dépôt, voie `depot` : la pièce est publique et se retélécharge,
    # le socle ne reste ni à l'atelier ni au coffre. Empreintes des pièces et des
    # socles : `referentiels/socles_2027.sha256`.
    ('socle_texte_plf2027', 'referentiels/socle_texte_plf2027.json',
     'referentiel', True, 'appareil/socle_texte_2027.py', [], []),
    ('socle_texte_plfss2027', 'referentiels/socle_texte_plfss2027.json',
     'referentiel', True, 'appareil/socle_texte_2027.py', [], []),
    ('redaction_plf2027', 'referentiels/redaction_plf2027.json',
     'referentiel', True, 'appareil/redaction_2027.py', [], []),
    ('redaction_plfss2027', 'referentiels/redaction_plfss2027.json',
     'referentiel', True, 'appareil/redaction_2027.py', [], []),
    ('articles_ouverts_plf_json', 'referentiels/articles_ouverts_plf.json',
     'referentiel', False, 'appareil/articles_ouverts_plf.py',
     ['REF_norme', 'vecteur-mesure'], []),
    ('articles_ouverts_plfss_json', 'referentiels/articles_ouverts_plfss.json',
     'referentiel', False, 'appareil/articles_ouverts_plf.py',
     ['REF_norme', 'vecteur-mesure'], []),
    ('articles_ouverts_plf_releve', 'livrables/articles_ouverts_plf.txt',
     'derive', False, 'appareil/articles_ouverts_plf.py',
     ["lecture de l'auteur"], []),
    ('articles_ouverts_plfss_releve', 'livrables/articles_ouverts_plfss.txt',
     'derive', False, 'appareil/articles_ouverts_plf.py',
     ["lecture de l'auteur"], []),
    # Les deux tables plates du texte déposé. Le socle qui les produit ne se
    # verse pas — il se régénère depuis la pièce jointe —, les tables si :
    # elles portent l'empreinte de leur pièce source, donc le rejeu se vérifie.
    ('articles_ouverts_plf', 'referentiels/articles_ouverts_plf.tsv', 'derive',
     True, 'appareil/articles_ouverts_plf.py',
     ['REF_norme', 'vecteur-mesure', 'disposition-cible'], []),
    ('articles_ouverts_plfss', 'referentiels/articles_ouverts_plfss.tsv',
     'derive', True, 'appareil/articles_ouverts_plf.py',
     ['REF_norme', 'vecteur-mesure', 'disposition-cible'], []),
    # Les sorties d'éval versées : elles ne se régénèrent pas, un fil les a
    # écrites en aveugle et le rejeu ne redonnerait pas les mêmes réponses.
    ('reponses_eval_plf', 'livrables/eval_gl/reponses_vecteur_mesure_plf.json',
     'derive', True, None, ['noter_eval_gl.py', 'banc d\'épreuve'], []),
    ('reponses_eval_plfss',
     'livrables/eval_gl/reponses_vecteur_mesure_plfss.json', 'derive', True,
     None, ['noter_eval_gl.py', 'banc d\'épreuve'], []),
    # Retiré du coffre le 20260908. Rejeu prouvé à l'octet contre l'empreinte
    # versée : `make livrables/etat_machine.html` rend `e595ed53…`, 12 208 o.
    # Il ne dépend que de `lots_epreuve.json`, qui est au coffre. A-342.
    ('etat_machine', 'livrables/etat_machine.html', 'derive', False,
     'appareil/etat_machine.py', ["lecture de l'auteur"], []),
    ('etat_vecteurs_csv', 'livrables/etat_vecteurs.csv', 'derive', False,
     'appareil/generer_etat_vecteurs.py',
     ["lecture de l'auteur", 'export', 'pack public'], []),
    ('releve_protos', 'livrables/releve_protos.txt', 'derive', False,
     'appareil/relever_protos.py',
     ['lecture interne des protos', 'contrôle avant réemploi'], []),
    # Le relevé d'écarts du bon à tirer, versé le 20260907 et resté hors index
    # jusqu'au 20260908 : deux documents au coffre que nulle grille ne
    # déclarait, donc que nul rejeu n'aurait refaits. C'est le cas qu'A-364
    # nomme. Ils restent au coffre : ils descendent des épreuves, qui sont des
    # binaires de 3 Mo et n'y sont pas — A-342.
    ('releve_epreuve_tsv', 'livrables/releve_epreuve_EP2.tsv', 'derive', True,
     'appareil/rendre_releve_epreuve.py',
     ['arbitrage de l’auteur', 'bon à tirer'], []),
    ('releve_epreuve_md', 'livrables/releve_epreuve_EP2.md', 'derive', True,
     'appareil/rendre_releve_epreuve.py',
     ['arbitrage de l’auteur', 'bon à tirer'], []),
    # Le relevé de mandat du 20260910 — la troisième épreuve contre la seconde
    # relue. Le fil qui l'a produit les avait bien portés à cette table ; son
    # édition est morte avec son conteneur, faute d'avoir pu être poussée
    # (A-394). Seul l'index du coffre les portait encore, et le prochain
    # `make reindex` les aurait dé-déclarés en silence. Ils sont reportés ici.
    ('releve_mandat_tsv', 'livrables/releve_epreuve_EP3.tsv', 'derive', True,
     'appareil/rendre_releve_mandat.py',
     ['arbitrage de l’auteur', 'bon à tirer'], []),
    ('releve_mandat_md', 'livrables/releve_epreuve_EP3.md', 'derive', True,
     'appareil/rendre_releve_mandat.py',
     ['arbitrage de l’auteur', 'bon à tirer'], []),
    # Retiré du coffre le 20260908. Rejeu prouvé à l'octet contre l'empreinte
    # versée : `make livrables/carte_du_projet.html` rend `bd2280f2…`, 23 863 o.
    # Il ne dépend que de l'index, qui est au coffre. A-342.
    ('carte', 'livrables/carte_du_projet.html', 'derive', False,
     'appareil/generer_carte.py', ["lecture de l'auteur"], []),
    ('donnees', 'livrables/donnees.json', 'derive', False,
     'appareil/exporter_donnees.py', ['generer_interface.py'], []),
    ('manifeste', 'site/manifeste.html', 'derive', False,
     'appareil/generer_site.py', ['diffusion', 'téléchargement'],
     ['1pager', 'sources/1pager_20260806_v1_proto.html']),
    ('site', 'site/index.html', 'derive', False,
     'appareil/generer_site.py', ['diffusion', 'Vercel'],
     ['livrables/site_prototype.html', 'site_prototype.html']),

    # ---------------------------------------------------------------- méthode
    ('feuille_de_route', 'methode/feuille_de_route.md', 'methode', True, None,
     ['ouverture de session', 'instructions permanentes'], []),
    ('localisation', 'methode/localisation.md', 'methode', True, None,
     ['ouverture de session'], []),
    ('index', 'methode/index.json', 'methode', True,
     'appareil/generer_index.py',
     ['controle_index.py', 'toute skill qui résout un renvoi'], []),
    ('empreintes', 'methode/empreintes.json', 'methode', True,
     'appareil/empreintes.py',
     ['controle_restauration.py', 'ouverture de session'], []),
    ('journal', 'methode/journal.md', 'methode', True, None,
     ['ouverture de session'], []),
    ('arbitrages', 'methode/arbitrages.md', 'methode', True, None,
     ['ouverture de session'], []),
    # Scindé le 20260904 : le registre entier ne repassait plus au coffre.
    ('arbitrages_archive', 'methode/arbitrages_archive.md', 'methode', True,
     None, ['résolution d\'un renvoi A-nnn antérieur au 20260901'], []),
    ('contrat_projection', 'methode/contrat_projection.md', 'methode', True, None,
     ['fiche-mesure', 'audit-conformite', 'qa-riposte', 'compatibilite-doctrine',
      'contestabilite'],
     ['Contrat_projection_REF_20260820_v2.md',
      'Contrat_projection_REF_20260820_v1.md']),
    ('regles_forme_canonique', 'methode/regles_forme_canonique.md', 'methode',
     True, None,
     ['fiche-mesure', 'audit-conformite', 'qa-riposte', 'compatibilite-doctrine',
      'contestabilite'],
     ['Regles_forme_canonique_20260820_v2.md',
      'Regles_forme_canonique_20260820_v1.md']),
    ('regles_redactionnelles', 'methode/regles_redactionnelles.md', 'methode',
     True, None, ['redaction-legistique'],
     ['Regles_redactionnelles_synthese_20260807.md']),
    ('procedure_controle', 'methode/procedure_controle.md', 'methode', True, None,
     ['make controle'], ['Procedure_controle_20260820_v2.md']),
    ('croisements_corpus', 'methode/croisements_corpus.md', 'methode', True, None,
     ['travail interne'], ['Croisements_corpus_20260819_v1.md']),
    ('derivation_D2', 'methode/derivation_D2.md', 'methode', True, None,
     ['travail interne'], ['Derivation_D2_20260820_v1.md']),
    ('prompt_fil_courant', 'methode/prompt_fil_courant.md', 'methode', True, None,
     ['ouverture de session'], ['Prompt_fil_apports_20260820_v1.md']),
    ('prompt_disposition_cible', 'methode/prompt_disposition_cible.md',
     'methode', True, None,
     ['ouverture du fil disposition-cible'], []),
    ('prompt_fil_strategie_machine',
     'methode/prompt_fil_strategie_machine.md', 'methode', True, None,
     ['ouverture du fil de stratégie de la machine'], []),
    ('prompt_eval_disposition_cible',
     'methode/prompt_eval_disposition_cible.md', 'methode', True, None,
     ["ouverture du fil d'éval de disposition-cible"], []),
    ('classement_corpus', 'methode/classement_corpus.md', 'methode', True, None,
     ['ouverture de session'], []),
    ('carte_des_chantiers', 'methode/carte_des_chantiers.md', 'methode', True,
     None, ['ouverture de session', 'site', 'gagnants-perdants', 'contre-PLF'],
     []),
    ('procedure_contre_plf', 'methode/procedure_contre_plf.md', 'methode', True,
     None, ['ouverture de session', 'contre-PLF', 'pack public'], []),
    ('test_rattachement', 'methode/test_rattachement.md', 'methode', True, None,
     ['contre-PLF', 'pack public', 'qualification des articles'], []),
    ('procedure_vecteurs', 'methode/procedure_vecteurs.md', 'methode', True,
     None, ['contre-PLF', 'REF_norme', 'redaction-legistique'], []),
    # Le contrat entre étapes de la chaîne de l'amendement. Véhicule-agnostique
    # par construction : c'est lui qui rend la machine généralisable, et il
    # s'écrit avant la troisième skill, faute de quoi elle fixerait un contrat
    # implicite.
    ('contrat_chaine_amendement', 'methode/contrat_chaine_amendement.md',
     'methode', True, None,
     ['vecteur-mesure', 'disposition-cible', 'expose-sommaire',
      'controle_generalisation.py', 'toute étape de la chaîne'], []),

    # ------------------------------------------------- références de la chaîne
    # Digestions et relevés écrits par nous : vérifiables contre une source
    # externe, donc des références, et rangés là où le coffre les porte. Ce ne
    # sont pas des pièces jointes de l'auteur, et ils ne prennent pas le chemin
    # de dépôt des sources.
    ('gabarit_expose_sommaire', 'reference/gabarit_expose_sommaire.md',
     'methode', True, None,
     ['expose-sommaire', 'contre-PLF', 'pack public'],
     ['sources/gabarit_expose_sommaire.md', 'gabarit_expose_sommaire.md']),
    ('depot_droit', 'reference/depot_droit.md', 'methode', True, None,
     ['disposition-cible', 'vecteur-mesure', 'redaction-legistique',
      'contre-PLF'], []),
    ('domaine_lfss', 'reference/domaine_lfss_LO111-3.md', 'methode', True, None,
     ['test de rattachement', 'expose-sommaire', 'contre-PLF'], []),
    # Les deux digestions de référence externe, versées les 20261006 et 20261007.
    # `guide_legistique` absorbe `structure_ppl`, `regles_redaction_guide` et
    # `domaine_lois_financieres`, et en porte les alias ; `regles_credits` ne
    # fusionne avec rien — elle porte du verbatim relevé au dépôt de droit.
    ('guide_legistique', 'reference/guide_legistique.md', 'methode', True, None,
     ['redaction-legistique', 'disposition-cible', 'expose-sommaire',
      'test de rattachement', 'contre-PLF'],
     ['sources/guide_legistique.md', 'reference/structure_ppl.md',
      'reference/regles_redaction_guide.md',
      'reference/domaine_lois_financieres.md']),
    ('regles_credits', 'reference/regles_credits.md', 'methode', True, None,
     ['contre-PLF', 'amendement de crédits', 'état B'],
     ['sources/regles_credits.md']),
    # La table « type de passe → appui dû ». Une ligne de lancement de fil qui la
    # nomme suffit : le fil y trouve tout ce qu'il devait ouvrir.
    ('appui_des_passes', 'methode/appui_des_passes.md', 'methode', True, None,
     ['ouverture de session', 'redaction-legistique', 'contre-PLF'], []),
    ('procedure_fin_de_chantier_2027',
     'methode/procedure_fin_de_chantier_depot_2027.md', 'methode', True, None,
     ['ouverture de session', 'contre-PLF'], []),
    ('passation_droit_renvois', 'reference/passation_droit_renvois.md',
     'methode', True, None, ['ouverture de session'], []),
    ('passation_lecture_en_creux', 'methode/passation_lecture_en_creux.md',
     'methode', True, None, ['ouverture de session'], []),
    # Versée le 20260904 par le fil du site, qui n'avait pas la main sur
    # `methode/` : elle était au coffre et invisible à l'index.
    ('passation_site', 'methode/passation_site.md', 'methode', True, None,
     ['ouverture de session', 'tout fil qui touche au site'], []),
    ('regle_enonces_eval', 'methode/regle_enonces_eval.md', 'methode', True,
     None, ["éval de la rédaction cible", 'tout rejeu du banc'], []),
    # --- déclarés le 20260903, après ouverture : ils étaient au coffre et
    # invisibles à l'index, ce que `I6` compte désormais.
    ('sas', 'methode/sas.md', 'methode', True, None,
     ['ouverture de session', 'fil de réconciliation'], []),
    ('banc_chouchous', 'methode/banc_chouchous.md', 'methode', True, None,
     ['banc bout en bout', 'fil de test'], []),
    # --- déclarés le 20260907 par le fil de maintenance : versés la veille au
    # coffre par le fil du second banc, portés à l'index dérivé et non à cette
    # table, donc voués à disparaître au prochain rejeu. C'est A-381 qui se
    # répète, sur les deux pièces que ce fil-là n'avait pas portées.
    ('banc_gl', 'methode/banc_gl.md', 'methode', True, None,
     ['banc des liasses déposées', 'noter_eval_gl.py', 'fil de test'], []),
    ('prompt_fil_joueur_banc_gl', 'methode/prompt_fil_joueur_banc_gl.md',
     'methode', True, None,
     ['ouverture du fil joueur du banc des liasses déposées'], []),
    ('digestions_attendues', 'reference/digestions_attendues.md', 'methode',
     True, None, ['fil de digestion', 'ouverture de session'], []),
    ('imposition_du_capital_fondapol',
     'reference/imposition_du_capital_fondapol.md', 'methode', True, None,
     ['citation sourcée', 'contestabilite', 'qa-riposte'], []),
    ('justice_fiscale_1789_fondapol',
     'reference/justice_fiscale_1789_fondapol.md', 'methode', True, None,
     ['citation sourcée', 'contestabilite', 'qa-riposte'], []),
    ('nomenclature_prelevements_ifrap',
     'reference/nomenclature_prelevements_ifrap.md', 'methode', True, None,
     ['contre-PLF', 'réconciliation des prélèvements'], []),
    ('sourcage_ir_dgfip', 'reference/sourcage_ir_dgfip.md', 'methode', True,
     None, ['citation sourcée'], []),
    # L'inventaire de ce que le coffre porte, relevé à `project_info` en
    # ouverture. Il n'est pas versé — il se refait à chaque session, et le
    # verser figerait une photo. `controle_index.py` s'en sert pour `I6`.
    ('inventaire_coffre', 'methode/inventaire_coffre.tsv', 'methode', False,
     None, ['controle_index.py', 'ouverture de session'], []),

    # ---------------------------------------------------- dette du 20260914
    # Sept pièces dues au coffre : un nouveau millésime de la Constitution à
    # trois colonnes et six dérivés de la passe de révision constitutionnelle.
    # Les versions antérieures de ces cinq dernières gardent leur propre entrée
    # dans `COFFRE_SOURCES` — datées, non remplacées, non aliasées : c'est
    # l'arbitrage du 20260914 sur le nommage de cette famille.
    ('source:constitution_3col_20260914_v45',
     'reference/Constitution_3col_20260914_v45.html', 'source', True, None,
     ["lecture de l'auteur", 'redaction-legistique', 'audit-conformite'], []),
    ('pplc_modificative',
     'livrables/PPLC_consolidee_modificative_20260914_v7.md', 'derive', True,
     None, ['dépôt parlementaire', 'audit-conformite'], []),
    ('pplc_substitution',
     'livrables/PPLC_consolidee_substitution_20260914_v7.md', 'derive', True,
     None, ['redaction-legistique', 'audit-conformite'], []),
    ('presentation_revision', 'livrables/Presentation_20260916_v46.md',
     'derive', True, None, ['diffusion', "lecture de l'auteur"], []),
    ('etat_revision', 'methode/etat_revision_constitutionnelle.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('recap_transposabilite',
     'livrables/Recap_transposabilite_20260914_v7.md', 'derive', True, None,
     ['analyse-transposabilite', 'compatibilite-doctrine'], []),
    ('recensement_innovations',
     'livrables/Recensement_innovations_20260914_v2.md', 'derive', True, None,
     ['analyse-transposabilite', 'contestabilite'], []),
    # Nés de l'impression du 20260914. `refresh_toc_pdf.py` répond à un défaut
    # mesuré : le convertisseur pose bien les styles de titre mais laisse le
    # niveau de plan à zéro, et LibreOffice construit le sommaire sur les
    # niveaux de plan — d'où une table des matières vide dans tout PDF produit
    # hors de Word.
    ('refresh_toc_pdf', 'appareil/refresh_toc_pdf.py', 'appareil', True,
     None, ['impression-docx'], []),
    ('sans_cesure', 'appareil/sans_cesure.py', 'appareil', True,
     None, ['impression-docx'], []),

    # ---------------------------------------------------- dette du 20260916
    # Le contrôle qui a rouvert l'écart d'A-25 et d'A-47, et le millésime de
    # la Constitution à trois colonnes qui les corrige. La v45 garde son
    # entrée : datée, non remplacée, non aliasée.
    ('controle_colonne_c', 'appareil/controle_colonne_c.py', 'appareil', True,
     None, ['make controle'], []),
    ('source:constitution_3col_20260916_v46',
     'reference/Constitution_3col_20260916_v46.html', 'source', True, None,
     ["lecture de l'auteur", 'redaction-legistique', 'audit-conformite'], []),

    # ---------------------------------------------------- dette du 20260917
    # Le découpage doctrinal en blocs (lot C) et son contrôle mécanique, la
    # règle du fragment daté qui permet à deux fils de verser au même fichier
    # cumulatif sans collision, et le pliage d'un paquet de dépôt. Ces cinq
    # pièces n'étaient déclarées par aucun paquet reçu ; les rôles et
    # `consomme_par` ci-dessous sont posés depuis ce que chaque module dit de
    # lui-même en tête de fichier, faute d'une déclaration reçue — à corriger
    # si elle diverge de l'intention.
    ('controle_blocs', 'appareil/controle_blocs.py', 'appareil', True, None,
     ['make controle', 'lot C', 'lot D'], []),
    ('epreuve_controle_blocs', 'appareil/epreuve_controle_blocs.py',
     'appareil', True, None, ['controle_blocs.py'], []),
    ('fragments', 'appareil/fragments.py', 'appareil', True, None,
     ['tout fil qui dépose au journal ou aux arbitrages'], []),
    ('rendre_blocs', 'appareil/rendre_blocs.py', 'appareil', True, None,
     ['make', 'lot C', 'lot D'], []),
    ('plier_lot', 'appareil/plier_lot.py', 'appareil', True, None,
     ["pliage et dépliage d'un lot"], []),

    # Confrontation d'un résumé de texte financier à la pièce qui fait foi, et
    # son épreuve de fautes.
    ('confronter_lecture', 'appareil/confronter_lecture.py', 'appareil', True,
     None, ["confrontation d'un livrable à sa pièce"], []),
    ('faux_lecture', 'appareil/faux_lecture.py', 'appareil', True,
     None, ['confronter_lecture.py'], []),

    # ------------------------------------ extension de la machine, 20260916
    # Le plan et sa pièce opératoire, puis les trois prompts de lot. La méthode
    # de découpage est écrite **avant** le premier bloc : déduite des blocs,
    # elle ne pourrait plus les juger.
    #
    # `plier_paquet.py` et `controle_projection.py` ont d'abord été tenus hors
    # dépôt : la note de transmission du 20260917 les disait perdus, à
    # réécrire, sans rouvrir le paquet joint qui les portait déjà en code
    # entier. Écart signalé, tranché par l'auteur (20260917) — le paquet du
    # 20260916 fait foi, les deux fichiers sont poussés, empreintes vérifiées
    # à l'octet contre celles que ce paquet annonçait.
    ('plan_bataille', 'methode/plan_bataille.md', 'methode', True, None,
     ['ouverture de session', 'ordre des lots'], []),
    ('methode_decoupage_bloc', 'methode/methode_decoupage_bloc.md', 'methode',
     True, None, ['lot C — découpage doctrinal en blocs', 'plan_bataille'],
     []),
    ('prompt_lot_A_resume_attendu', 'methode/prompt_lot_A_resume_attendu.md',
     'methode', True, None, ['ouverture du fil du lot A'], []),
    ('prompt_lot_C_decoupage_blocs',
     'methode/prompt_lot_C_decoupage_blocs.md', 'methode', True, None,
     ['ouverture du fil du lot C'], []),
    ('prompt_lot_ecart', 'methode/prompt_lot_ecart.md', 'methode', True, None,
     ["ouverture du fil de la mesure de l'écart"], []),
    ('paquet_machine', 'livrables/paquet_machine.md', 'derive', True,
     'appareil/plier_paquet.py',
     ['lot C — découpage doctrinal en blocs',
      "lot Écart — passe équipée", 'controle_projection.py'], []),
    ('plier_paquet', 'appareil/plier_paquet.py', 'appareil', True, None,
     ['make', "pliage d'un paquet diffusable"], []),
    ('controle_projection', 'appareil/controle_projection.py', 'appareil',
     True, None, ['make controle', 'tout paquet diffusable'], []),

    # ---------------------------------------------------- dette du 20260921
    # Était au coffre comme document (D3), écrite par un fil Cowork qui ne
    # pouvait pas pousser. Portée au dépôt le 20260921, elle en sort.
    ('trois_colonnes_regle_dor', 'appareil/trois_colonnes_regle_dor.py',
     'appareil', True, None, ["règle d'or — trois colonnes"], []),

    # ---------------------------------------------- rattrapage du 20260930
    # Soixante-deux artefacts que l'index du coffre déclarait et que cette table
    # n'avait jamais reçus : les pièces du 20260929-30 et les déclarations
    # antérieures depuis le 20260916. Report à l'identique de l'index du coffre,
    # sans arbitrage : rôle, chemin, rang, consommateurs, alias.
    ('blocs_lot_C', 'livrables/blocs_lot_C.md', 'derive', True,
     'appareil/plier_lot.py',
     ['lot D — tri par véhicule et morceaux', 'controle_blocs.py'], []),
    ('blocs_lot_C_lecture', 'livrables/blocs_lot_C_lecture.md', 'derive', True,
     None, ["lecture de l'auteur"], []),
    ('cr_lot_C', 'methode/cr_lot_C_20260917.md', 'methode', True, None,
     ["ouverture du fil d'organisation et de méthode"], []),
    ('prompt_fil_organisation_methode',
     'methode/prompt_fil_organisation_methode.md', 'methode', True, None,
     ["ouverture du fil d'organisation et de méthode"], []),
    ('prompt_lot_D_tri_vehicule', 'methode/prompt_lot_D_tri_vehicule.md',
     'methode', True, None, ['ouverture du fil du lot D'], []),
    ('a_trancher', 'methode/a_trancher.md', 'methode', True,
     'appareil/fragments.py',
     ['ouverture de tout fil de méthode', 'ordre des lots'], []),
    ('cr_lecture_textes_2026', 'methode/cr_lecture_textes_2026.md', 'methode',
     True, None, ['a_trancher.md'], []),
    ('cr_confrontation', 'methode/cr_confrontation_20260916.md', 'methode',
     True, None, ['a_trancher.md', 'confrontation'], []),
    ('prompt_fil_bilan_methode', 'methode/prompt_fil_bilan_methode.md',
     'methode', True, None, ['ouverture du fil de bilan de méthode'], []),
    ('prompt_fil_socle_second_cercle',
     'methode/prompt_fil_socle_second_cercle.md', 'methode', True, None,
     ['ouverture du fil du second cercle du socle'], []),
    ('prompt_fil_strategie_chantier',
     'methode/prompt_fil_strategie_chantier.md', 'methode', True, None,
     ['ouverture du fil de stratégie du chantier'], []),
    ('prompt_fil_verif_listes_2026', 'methode/prompt_fil_verif_listes_2026.md',
     'methode', True, None,
     ['ouverture du fil de vérification des listes 2026'], []),
    ('sas_lot_A_resume_attendu', 'methode/sas_lot_A_resume_attendu.md',
     'methode', True, None, ['fil de réconciliation'], []),
    ('sas_pplc_regle_dor', 'methode/sas_pplc_regle_dor.md', 'methode', True,
     None, ['fil de réconciliation'], []),
    ('paquet_depot_20260914', 'methode/paquet_depot_20260914.md', 'methode',
     True, None, ['session claude.ai/code'], []),
    ('paquet_depot_20260916', 'methode/paquet_depot_20260916.md', 'methode',
     True, None, ['session claude.ai/code'], []),
    ('paquet_depot_machine_20260916',
     'methode/paquet_depot_machine_20260916.md', 'methode', True, None,
     ['session claude.ai/code'], []),
    ('paquet_depot_confrontation_20260916',
     'methode/paquet_depot_confrontation_20260916.md', 'methode', True, None,
     ['session claude.ai/code'], []),
    ('paquet_depot_application_20260917',
     'methode/paquet_depot_application_20260917.md', 'methode', True, None,
     ['session claude.ai/code'], []),
    ('fragment_arbitrages_20260917_application',
     'methode/fragments/arbitrages/20260917-fil-application.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20260917_application',
     'methode/fragments/journal/20260917-fil-application.md', 'methode', True,
     None, ['appareil/fragments.py'], []),
    ('comblement_termes_manquants', 'livrables/comblement_termes_manquants.md',
     'derive', True, None,
     ['second cercle du socle', 'bilans des blocs du lot C'], []),
    ('PLF2026_liste', 'livrables/PLF2026_liste.md', 'derive', True, None,
     ["lecture de l'auteur", 'confrontation'], []),
    ('PLFSS2026_liste', 'livrables/PLFSS2026_liste.md', 'derive', True, None,
     ["lecture de l'auteur", 'confrontation'], []),
    ('PLF_PLFSS_differences', 'livrables/PLF_PLFSS_differences.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('PLF_PLFSS_formats', 'livrables/PLF_PLFSS_formats.md', 'derive', True,
     None, ["lecture de l'auteur"], []),
    ('PLF2026_annexe_technique', 'livrables/PLF2026_annexe_technique.md',
     'derive', True, None, ["lecture de l'auteur"], []),
    ('index_mesures_plf_md', 'livrables/index_mesures_plf.md', 'derive', True,
     None, ["lecture de l'auteur"], []),
    ('index_mesures_plf', 'referentiels/index_mesures_plf.tsv', 'derive', True,
     None, ['vecteur-mesure', 'confrontation'], []),
    ('resume_attendu_texte_financier',
     'livrables/resume_attendu_texte_financier_2026.md', 'derive', True, None,
     ["lecture de l'auteur", 'confrontation'], []),
    ('reperes_resume_2026', 'referentiels/reperes_resume_2026.tsv', 'derive',
     True, None, ['confrontation'], []),
    ('confrontation_resume_2026', 'livrables/confrontation_resume_2026.tsv',
     'derive', True, None, ['confrontation', "arbitrage de l'auteur"], []),
    ('bordereau_confrontation_resume_2026',
     'livrables/bordereau_confrontation_resume_2026.md', 'derive', True, None,
     ['confrontation', "arbitrage de l'auteur"], []),
    ('presentation_revision_v47', 'livrables/Presentation_20260916_v47.md',
     'derive', True, None, ['diffusion', "lecture de l'auteur"], []),
    ('recensement_innovations_v3',
     'livrables/Recensement_innovations_20260916_v3.md', 'derive', True, None,
     ['analyse-transposabilite', 'contestabilite'], []),
    ('recap_transposabilite_v8',
     'livrables/Recap_transposabilite_20260916_v8.md', 'derive', True, None,
     ['analyse-transposabilite', 'compatibilite-doctrine'], []),
    ('pplc_regle_dor_modificative', 'livrables/PPLC_regle_dor_modificative.md',
     'derive', True, None, ['dépôt parlementaire', 'audit-conformite'], []),
    ('presentation_regle_dor', 'livrables/Presentation_regle_dor.md', 'derive',
     True, None, ['diffusion', "lecture de l'auteur"], []),
    ('fragment_arbitrages_20260917_socle',
     'methode/fragments/arbitrages/20260917-socle.md', 'methode', True, None,
     ['appareil/fragments.py'], []),
    ('fragment_journal_20260917_socle',
     'methode/fragments/journal/20260917-socle.md', 'methode', True, None,
     ['appareil/fragments.py'], []),
    ('paquet_depot_socle_20260917', 'methode/paquet_depot_socle_20260917.md',
     'methode', True, None, ['session claude.ai/code'], []),
    ('prompt_fil_noeud_mise_en_oeuvre',
     'methode/prompt_fil_noeud_mise_en_oeuvre.md', 'methode', True, None,
     ['ouverture du fil du nœud de mise en œuvre'], []),
    ('cr_socle_second_cercle', 'methode/cr_socle_second_cercle_20260917.md',
     'methode', True, None,
     ['ouverture du fil de bilan de méthode', 'a_trancher.md'], []),
    ('cgi_expert_articles', 'referentiels/cgi_expert_articles.tsv',
     'referentiel', True, None,
     ['disposition-cible', 'redaction-legistique',
      'lot F — blocs de rattachement', 'lot G — dossiers de mesure'], []),
    ('cgi_expert_insertions', 'referentiels/cgi_expert_insertions.tsv',
     'referentiel', True, None,
     ['disposition-cible', 'redaction-legistique',
      'lot G — dossiers de mesure'], []),
    ('cgi_expert_suppressions', 'referentiels/cgi_expert_suppressions.tsv',
     'referentiel', True, None,
     ['disposition-cible', 'redaction-legistique',
      'lot G — dossiers de mesure'], []),
    ('cgi_expert_articles_bouges',
     'referentiels/cgi_expert_articles_bouges.tsv', 'referentiel', True, None,
     ['disposition-cible', 'vecteur-mesure',
      "tout emploi d'un article du CGI réécrit"], []),
    ('cgi_expert_parametres', 'referentiels/cgi_expert_parametres.tsv',
     'referentiel', True, None,
     ['compatibilite-doctrine', 'disposition-cible',
      'confrontation au REF_chiffres'], []),
    ('cgi_expert_couverture', 'livrables/cgi_expert_couverture_20260929.md',
     'derive', True, None,
     ['lot F — blocs de rattachement', "arbitrage de l'auteur"], []),
    ('cgi_expert_comblements', 'livrables/cgi_expert_comblements_20260929.md',
     'derive', True, None,
     ['analyse-transposabilite', 'compatibilite-doctrine',
      'lot G — dossiers de mesure'], []),
    ('cgi_expert_commentaires',
     'livrables/cgi_expert_commentaires_20260929.md', 'derive', True, None,
     ["arbitrage de l'auteur", "constitution d'un lot d'amendements"], []),
    ('cgi_expert_regles_de_lecture',
     'reference/cgi_expert_regles_de_lecture.md', 'methode', True, None,
     ['disposition-cible', 'redaction-legistique', 'vecteur-mesure',
      'tout fil qui emploie le CGI réécrit'], []),
    ('predigestion_cgi', 'livrables/predigestion_cgi_20260929.md', 'derive',
     True, None, ['cgi_expert_regles_de_lecture', "lecture de l'auteur"], []),
    ('fragment_a_trancher_20260929_cgi_expert',
     'methode/fragments/a_trancher/20260929-cgi-expert.md', 'methode', True,
     None, ['appareil/fragments.py'], []),
    ('mecanique_gages_restitutions',
     'livrables/mecanique_gages_restitutions_20260929.md', 'derive', True,
     None,
     ['disposition-cible', 'expose-sommaire',
      'phase 0 du plan de rédaction'], []),
    ('prelevements_forces', 'referentiels/prelevements_forces_20260930.tsv',
     'referentiel', True, None,
     ['fil du sort des prélèvements', 'vecteur-mesure', 'bloc B-09'], []),
    ('recensement_prelevements',
     'livrables/recensement_prelevements_20260930.md', 'derive', True, None,
     ['fil du sort des prélèvements', "lecture de l'auteur"], []),
    ('prompt_fil_sort_prelevements', 'methode/prompt_fil_sort_prelevements.md',
     'methode', True, None, ['ouverture du fil du sort des prélèvements'], []),
    ('arborescence_mesures', 'livrables/arborescence_mesures_20260928.md',
     'derive', True, None,
     ['plan_sept_phases', 'lot F — blocs de rattachement',
      'lot G — dossiers de mesure',
      'disposition-cible'], ['arborescence_mesures_20260928.html']),
    ('plan_sept_phases', 'methode/plan_sept_phases_20260930.md', 'methode',
     True, None,
     ['ouverture de session', 'ordre des lots', 'carte_des_chantiers'], []),
    ('fragment_journal_20260930_inscription_registre',
     'methode/fragments/journal/20260930-inscription-registre.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20260930_versement_reprise',
     'methode/fragments/journal/20260930-versement-reprise.md', 'methode',
     True, None, ['appareil/fragments.py'], []),

    # ------------------------------------------- rattrapage du 20261001 (fil courroies)
    # Quarante-six documents du coffre absents de la table curée. Déclarés par
    # leur adresse, au sens de l'arbitrage du 20260917 sur le classement par
    # dossier : un fait vérifiable sur où le document vit, non un jugement de
    # contenu. Consommateur générique, à préciser quand le document s'ouvre.
    ('fragment_journal_20260930_table_de_passage',
     'methode/fragments/journal/20260930-table-de-passage.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20260930_correction_forfaits_cotisation',
     'methode/fragments/journal/20260930-correction-forfaits-cotisation.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20260930_perimetre_fiscal',
     'methode/fragments/journal/20260930-perimetre-fiscal.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20260930_sort_prelevements',
     'methode/fragments/journal/20260930-sort-prelevements.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20260930_arbitrages_phase1',
     'methode/fragments/journal/20260930-arbitrages-phase1.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20261001_courroies',
     'methode/fragments/journal/20261001-courroies.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_journal_20261001_lecture_2027',
     'methode/fragments/journal/20261001-lecture-2027.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20261006_digestion_guide_legistique',
     'methode/fragments/arbitrages/20261006-digestion-guide-legistique.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20261006_digestion_complements_guide',
     'methode/fragments/arbitrages/20261006-digestion-complements-guide.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20261006_digestion_sections_budgetaires',
     'methode/fragments/arbitrages/20261006-digestion-sections-budgetaires.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20261007_fusion_digestions_appui',
     'methode/fragments/arbitrages/20261007-fusion-digestions-appui.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20261007_corrections_methode_fil_code',
     'methode/fragments/arbitrages/20261007-corrections-methode-fil-code.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20261007_geste2_restauration',
     'methode/fragments/arbitrages/20261007-geste2-restauration.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_cle_de_passage',
     'methode/fragments/arbitrages/20260930-cle-de-passage.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_correction_cle_de_passage',
     'methode/fragments/arbitrages/20260930-correction-cle-de-passage.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_csa_forfaits_de_cotisation',
     'methode/fragments/arbitrages/20260930-csa-forfaits-de-cotisation.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_defauts_reconciliation',
     'methode/fragments/arbitrages/20260930-defauts-reconciliation.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_perimetre_fiscal',
     'methode/fragments/arbitrages/20260930-perimetre-fiscal.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_sort_prelevements',
     'methode/fragments/arbitrages/20260930-sort-prelevements.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_arbitrages_phase1',
     'methode/fragments/arbitrages/20260930-arbitrages-phase1.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20260930_sort_prelevements_decisions',
     'methode/fragments/arbitrages/20260930-sort-prelevements-decisions.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20261001_epargne_salariale_et_affectataires',
     'methode/fragments/arbitrages/20261001-epargne-salariale-et-affectataires.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_arbitrages_20261001_courroies',
     'methode/fragments/arbitrages/20261001-courroies.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_a_trancher_20260930_sort_prelevements',
     'methode/fragments/a_trancher/20260930-sort-prelevements.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('fragment_a_trancher_20261001_courroies',
     'methode/fragments/a_trancher/20261001-courroies.md', 'methode',
     True, None, ['appareil/fragments.py'], []),
    ('socle_prompt_fil', 'methode/socle_prompt_fil.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_courroies', 'methode/prompt_fil_courroies.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_lecture_textes_2027',
     'methode/prompt_fil_lecture_textes_2027.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_carto', 'methode/prompt_fil_carto.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_design_graphique', 'methode/prompt_fil_design_graphique.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_site_pages_bande', 'methode/prompt_fil_site_pages_bande.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('prompt_fil_window_dressing_site', 'methode/prompt_fil_window_dressing_site.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('audit_derives_20260924', 'methode/audit_derives_20260924.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('cr_site_arret_mesure_20260923', 'methode/cr_site_arret_mesure_20260923.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('charte_visuelle', 'reference/charte_visuelle.md', 'methode',
     True, None, ['ouverture de session'], []),
    ('index_livre_EP3', 'livre/index_livre_EP3.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('sort_prelevements_md', 'livrables/sort_prelevements_20260930.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('reconciliation_sources_fiscales_20260930',
     'livrables/reconciliation_sources_fiscales_20260930.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('couverture_table_de_passage_20260930',
     'livrables/couverture_table_de_passage_20260930.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('graphiques_index', 'livrables/graphiques/index.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('etat_carto_20260924', 'livrables/etat_carto_20260924.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('manifeste_20260924', 'livrables/manifeste_20260924.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('manifeste_20260923', 'livrables/manifeste_20260923.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('releve_passe_825_534_20260923', 'livrables/releve_passe_825_534_20260923.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('rapprochement_proto_20260921', 'livrables/rapprochement_proto_20260921.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('etat_site_20260921', 'livrables/etat_site_20260921.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('digestion_archives_20260921', 'livrables/digestion_archives_20260921.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('reconfirmation_chiffres_20260921', 'livrables/reconfirmation_chiffres_20260921.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('zip_doctrine_lisezmoi', 'livrables/zip_doctrine_lisezmoi.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('zip_doctrine_regles_de_lecture', 'livrables/zip_doctrine_regles_de_lecture.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('extrait_classeurs_anterieurs_20260917',
     'livrables/extrait_classeurs_anterieurs_20260917.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('ecart_classeurs_20260917', 'livrables/ecart_classeurs_20260917.md', 'derive',
     True, None, ["lecture de l'auteur"], []),
    ('sort_prelevements_tsv', 'referentiels/sort_prelevements_20260930.tsv', 'referentiel',
     True, None, ["lecture de l'auteur"], []),
    ('table_passage_schema_prelevements',
     'referentiels/table_passage_schema_prelevements_20260930.tsv', 'referentiel',
     True, None, ["lecture de l'auteur"], []),
    # ------------------------------------------------ paquet du 20261008 (C-4)
    # Versés au dépôt par le paquet `paquet_depot_2027_20261008.zip`, contrôlés
    # à l'octet sur `empreintes_paquet_20261008.json` : pièces et assemblages du
    # dépôt 2027, lots antérieurs et périmés, états et passations des fils, la
    # machine à amendements 1.2 à 1.4, les scripts de contrôle d'adresses et de
    # scission. Déclarés tels quels, aucun renommé. La note de l'auteure
    # `input/Note_Retraite_20250619.docx` n'y est pas : elle est déclarée comme
    # source, sous son nom d'origine (COFFRE_SOURCES).
    ('manifeste_paquet_20261008', 'MANIFESTE.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('controle_adresses_extraction_gen', 'appareil/controle_adresses_extraction.py', 'appareil', True, None,
     ['fil code'], []),
    ('controle_adresses_verdicts_gen', 'appareil/controle_adresses_verdicts.py', 'appareil', True, None,
     ['fil code'], []),
    ('scinder_liasse_trois_colonnes_gen', 'appareil/scinder_liasse_trois_colonnes.py', 'appareil', True, None,
     ['fil code'], []),
    ('versement_gen', 'appareil/versement.py', 'appareil', True, None,
     ['fil code'], []),
    ('clause_generale_niches_20261004', 'livrables/clause_generale_niches_20261004.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:liasse_20261008', 'livrables/depot_2027/LIASSE_20261008.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:liasse_p1_20261008', 'livrables/depot_2027/LIASSE_P1_20261008.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:liasse_p2_20261008', 'livrables/depot_2027/LIASSE_P2_20261008.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:liasse_plfss_20261008', 'livrables/depot_2027/LIASSE_PLFSS_20261008.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:lisez_moi_20261008', 'livrables/depot_2027/LISEZ-MOI_20261008.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:2_4_armateurs_tonnage', 'livrables/depot_2027/P1/2_4_armateurs_tonnage.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:2_4_credit_impot_famille', 'livrables/depot_2027/P1/2_4_credit_impot_famille.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:2_4_credit_impot_recherche', 'livrables/depot_2027/P1/2_4_credit_impot_recherche.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:2_4_deductions_exceptionnelles', 'livrables/depot_2027/P1/2_4_deductions_exceptionnelles.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:2_4_exonerations_par_zone', 'livrables/depot_2027/P1/2_4_exonerations_par_zone.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:2_4_sortie_agricole_trois_ans', 'livrables/depot_2027/P1/2_4_sortie_agricole_trois_ans.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:2_4_tarifs_reduits_accise', 'livrables/depot_2027/P1/2_4_tarifs_reduits_accise.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:4_2_refonte_taxes_a_taxes_etat', 'livrables/depot_2027/P1/4_2_refonte_taxes_A_taxes_etat.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:4_2_refonte_taxes_b_taxes_affectees', 'livrables/depot_2027/P1/4_2_refonte_taxes_B_taxes_affectees.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:4_2_refonte_taxes_c_dmto_franchise', 'livrables/depot_2027/P1/4_2_refonte_taxes_C_dmto_franchise.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:4_2_refonte_taxes_d_plus_values', 'livrables/depot_2027/P1/4_2_refonte_taxes_D_plus_values.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:4_3_aide_fondamentale_et_taux_unique', 'livrables/depot_2027/P1/4_3_aide_fondamentale_et_taux_unique.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:4_4_taxe_fonciere_unique', 'livrables/depot_2027/P1/4_4_taxe_fonciere_unique.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:4_5_solde_refonte_is_tf', 'livrables/depot_2027/P1/4_5_solde_refonte_is_tf.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:4_6_tva_taux_reduits', 'livrables/depot_2027/P1/4_6_tva_taux_reduits.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:4_7_abrogations_cgi', 'livrables/depot_2027/P1/4_7_abrogations_cgi.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:coll_p1_01_dotations_face_aux_reductions_de_champ', 'livrables/depot_2027/P1/coll_P1_01_dotations_face_aux_reductions_de_champ.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:coll_p1_02_fusion_dotation_forfaitaire_taxe_fonciere', 'livrables/depot_2027/P1/coll_P1_02_fusion_dotation_forfaitaire_taxe_fonciere.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:coll_p1_03_tva_sur_justification', 'livrables/depot_2027/P1/coll_P1_03_tva_sur_justification.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:n5_compte_epargne_personnel', 'livrables/depot_2027/P1/n5_compte_epargne_personnel.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:nuitp1_01_rendre_le_don', 'livrables/depot_2027/P1/nuitp1_01_rendre_le_don.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:nuitp1_04_pret_taux_zero', 'livrables/depot_2027/P1/nuitp1_04_pret_taux_zero.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:nuitp1_05_investissement_industriel', 'livrables/depot_2027/P1/nuitp1_05_investissement_industriel.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:nuitp1_06_cession_reprise_entreprise', 'livrables/depot_2027/P1/nuitp1_06_cession_reprise_entreprise.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:nuitp1_07_credit_impot_competitivite', 'livrables/depot_2027/P1/nuitp1_07_credit_impot_competitivite.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:nuitp1_08_avantages_culturels', 'livrables/depot_2027/P1/nuitp1_08_avantages_culturels.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:nuitp1_09_impot_agricole', 'livrables/depot_2027/P1/nuitp1_09_impot_agricole.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:nuitp1_10_impot_selon_adresse', 'livrables/depot_2027/P1/nuitp1_10_impot_selon_adresse.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:nuitp1_11_abroger_mises_a_jour', 'livrables/depot_2027/P1/nuitp1_11_abroger_mises_a_jour.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p1:nuitp1_12_affectation_article_42', 'livrables/depot_2027/P1/nuitp1_12_affectation_article_42.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:2_1_dissolution_structures_facultatives', 'livrables/depot_2027/P2/2_1_dissolution_structures_facultatives.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:2_1_etablissements_ressources_propres', 'livrables/depot_2027/P2/2_1_etablissements_ressources_propres.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:2_1_missions_rendues_aux_ministeres', 'livrables/depot_2027/P2/2_1_missions_rendues_aux_ministeres.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:2_2_indemnite_depart_agents', 'livrables/depot_2027/P2/2_2_indemnite_depart_agents.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:2_6_cheque_energie', 'livrables/depot_2027/P2/2_6_cheque_energie.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:2_6_extinction_aide_logement', 'livrables/depot_2027/P2/2_6_extinction_aide_logement.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:2_6_socle_hebergement_urgence', 'livrables/depot_2027/P2/2_6_socle_hebergement_urgence.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:coll_p2_01_abrogation_concours_discretionnaires', 'livrables/depot_2027/P2/coll_P2_01_abrogation_concours_discretionnaires.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:coll_p2_02_credits_etat_b', 'livrables/depot_2027/P2/coll_P2_02_credits_etat_B.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:coll_p2_03_suppression_articles_85_86_87', 'livrables/depot_2027/P2/coll_P2_03_suppression_articles_85_86_87.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:coll_p2_04_facultes_et_obligations_de_baisse', 'livrables/depot_2027/P2/coll_P2_04_facultes_et_obligations_de_baisse.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:etatb_01_structures_facultatives', 'livrables/depot_2027/P2/etatB_01_structures_facultatives.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:etatb_02_subventions_associations', 'livrables/depot_2027/P2/etatB_02_subventions_associations.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:etatb_03_aides_ciblees', 'livrables/depot_2027/P2/etatB_03_aides_ciblees.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:etatb_04_titre2_plafond_emplois', 'livrables/depot_2027/P2/etatB_04_titre2_plafond_emplois.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:n6_defaisance_participations', 'livrables/depot_2027/P2/n6_defaisance_participations.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:n6_logement_social_flux', 'livrables/depot_2027/P2/n6_logement_social_flux.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:p2:n6_typologies_de_depenses', 'livrables/depot_2027/P2/n6_typologies_de_depenses.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:ppl_cession_participations_20261008', 'livrables/depot_2027/PPL_CESSION_PARTICIPATIONS_20261008.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:sommaire_20261008', 'livrables/depot_2027/SOMMAIRE_20261008.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:ss:2_3_subventions_associations_social', 'livrables/depot_2027/SS/2_3_subventions_associations_social.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:ss:3_3_restitution_salariale_coordination', 'livrables/depot_2027/SS/3_3_restitution_salariale_coordination.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:ss:3_3_restitution_salariale_principale', 'livrables/depot_2027/SS/3_3_restitution_salariale_principale.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:ss:arrets_04_m024_prolongation_droits_soins', 'livrables/depot_2027/SS/arrets_04_m024_prolongation_droits_soins.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:ss:n5_amorce_extinction_repartition', 'livrables/depot_2027/SS/n5_amorce_extinction_repartition.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:ss:n5_cadre_bouclier_sanitaire', 'livrables/depot_2027/SS/n5_cadre_bouclier_sanitaire.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:ss:n5_extinction_aides_fondues', 'livrables/depot_2027/SS/n5_extinction_aides_fondues.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:ss:n7b_m037a_gel_indexations_lfss', 'livrables/depot_2027/SS/n7b_m037a_gel_indexations_lfss.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:ss:n7b_ss03_liste_niches_sociales', 'livrables/depot_2027/SS/n7b_ss03_liste_niches_sociales.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:ss:nuit1c_suppression_taxe_salaires', 'livrables/depot_2027/SS/nuit1c_suppression_taxe_salaires.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:clause_generale_niches_20261005', 'livrables/depot_2027/clause_generale_niches_20261005.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:sans_colonne:n7b_m022_certificats_energie', 'livrables/depot_2027/sans_colonne/n7b_m022_certificats_energie.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:sans_colonne:n7b_m037b_gel_indexations_plf', 'livrables/depot_2027/sans_colonne/n7b_m037b_gel_indexations_plf.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:sans_colonne:n7b_m070_depenses_nouvelles', 'livrables/depot_2027/sans_colonne/n7b_m070_depenses_nouvelles.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('depot_2027:sans_colonne:nuit1c_ppl_cession_participations', 'livrables/depot_2027/sans_colonne/nuit1c_ppl_cession_participations.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_2_6_aides_ciblees_20261002.perime', 'livrables/liasse_2_6_aides_ciblees_20261002.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_2_6_aides_ciblees_20261002', 'livrables/liasse_2_6_aides_ciblees_20261002.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_aides_entreprises_plf2027_p1.perime', 'livrables/liasse_aides_entreprises_plf2027_p1.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_aides_entreprises_plf2027_p1', 'livrables/liasse_aides_entreprises_plf2027_p1.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_arrets_immediats:01_m037_indexations', 'livrables/liasse_arrets_immediats/01_M037_indexations.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_arrets_immediats:02_m070_depenses_nouvelles', 'livrables/liasse_arrets_immediats/02_M070_depenses_nouvelles.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_arrets_immediats:03_m022_certificats_energie', 'livrables/liasse_arrets_immediats/03_M022_certificats_energie.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_arrets_immediats:04_m024_soins_jambe_lfss.perime', 'livrables/liasse_arrets_immediats/04_M024_soins_jambe_lfss.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_arrets_immediats:04_m024_soins_jambe_lfss', 'livrables/liasse_arrets_immediats/04_M024_soins_jambe_lfss.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_m025_restitution_salariale', 'livrables/liasse_m025_restitution_salariale.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:00_lisezmoi', 'livrables/liasse_nuit_plf2027_p1/00_LISEZMOI.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:01_j1_article_4.perime', 'livrables/liasse_nuit_plf2027_p1/01_J1_article_4.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:01_j1_article_4', 'livrables/liasse_nuit_plf2027_p1/01_J1_article_4.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:02_j2_article_additionnel', 'livrables/liasse_nuit_plf2027_p1/02_J2_article_additionnel.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:03_j3_article_2', 'livrables/liasse_nuit_plf2027_p1/03_J3_article_2.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:04_j4_7_article_7.perime', 'livrables/liasse_nuit_plf2027_p1/04_J4-7_article_7.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:04_j4_7_article_7', 'livrables/liasse_nuit_plf2027_p1/04_J4-7_article_7.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:05_j4_9_article_9.perime', 'livrables/liasse_nuit_plf2027_p1/05_J4-9_article_9.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:05_j4_9_article_9', 'livrables/liasse_nuit_plf2027_p1/05_J4-9_article_9.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:06_j4_10_article_10.perime', 'livrables/liasse_nuit_plf2027_p1/06_J4-10_article_10.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:06_j4_10_article_10', 'livrables/liasse_nuit_plf2027_p1/06_J4-10_article_10.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:07_j4_11_article_11.perime', 'livrables/liasse_nuit_plf2027_p1/07_J4-11_article_11.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:07_j4_11_article_11', 'livrables/liasse_nuit_plf2027_p1/07_J4-11_article_11.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:08_j4_12_article_12.perime', 'livrables/liasse_nuit_plf2027_p1/08_J4-12_article_12.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:08_j4_12_article_12', 'livrables/liasse_nuit_plf2027_p1/08_J4-12_article_12.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:09_j4_13_article_13.perime', 'livrables/liasse_nuit_plf2027_p1/09_J4-13_article_13.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:09_j4_13_article_13', 'livrables/liasse_nuit_plf2027_p1/09_J4-13_article_13.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:10_j4_26_article_26.perime', 'livrables/liasse_nuit_plf2027_p1/10_J4-26_article_26.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:10_j4_26_article_26', 'livrables/liasse_nuit_plf2027_p1/10_J4-26_article_26.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:11_j4_28_article_28.perime', 'livrables/liasse_nuit_plf2027_p1/11_J4-28_article_28.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:11_j4_28_article_28', 'livrables/liasse_nuit_plf2027_p1/11_J4-28_article_28.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:12_j5_article_42.perime', 'livrables/liasse_nuit_plf2027_p1/12_J5_article_42.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:12_j5_article_42', 'livrables/liasse_nuit_plf2027_p1/12_J5_article_42.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:01_j1_article_4', 'livrables/liasse_nuit_plf2027_p1/exposes/01_J1_article_4.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:02_j2_article_additionnel', 'livrables/liasse_nuit_plf2027_p1/exposes/02_J2_article_additionnel.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:03_j3_article_2', 'livrables/liasse_nuit_plf2027_p1/exposes/03_J3_article_2.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:04_j4_7_article_7', 'livrables/liasse_nuit_plf2027_p1/exposes/04_J4-7_article_7.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:05_j4_9_article_9', 'livrables/liasse_nuit_plf2027_p1/exposes/05_J4-9_article_9.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:06_j4_10_article_10', 'livrables/liasse_nuit_plf2027_p1/exposes/06_J4-10_article_10.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:07_j4_11_article_11', 'livrables/liasse_nuit_plf2027_p1/exposes/07_J4-11_article_11.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:08_j4_12_article_12', 'livrables/liasse_nuit_plf2027_p1/exposes/08_J4-12_article_12.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:09_j4_13_article_13', 'livrables/liasse_nuit_plf2027_p1/exposes/09_J4-13_article_13.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:10_j4_26_article_26', 'livrables/liasse_nuit_plf2027_p1/exposes/10_J4-26_article_26.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:11_j4_28_article_28', 'livrables/liasse_nuit_plf2027_p1/exposes/11_J4-28_article_28.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('liasse_nuit_plf2027_p1:exposes:12_j5_article_42', 'livrables/liasse_nuit_plf2027_p1/exposes/12_J5_article_42.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('lot_2_1_structures_facultatives_20261002.perime', 'livrables/lot_2_1_structures_facultatives_20261002.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('lot_2_1_structures_facultatives_20261002', 'livrables/lot_2_1_structures_facultatives_20261002.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('lot_2_2_effectifs:13_j6_article_63', 'livrables/lot_2_2_effectifs/13_J6_article_63.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('lot_2_2_effectifs:14_j6_article_additionnel.perime', 'livrables/lot_2_2_effectifs/14_J6_article_additionnel.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('lot_2_2_effectifs:14_j6_article_additionnel', 'livrables/lot_2_2_effectifs/14_J6_article_additionnel.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('lot_2_2_effectifs:exposes:13_j6_article_63', 'livrables/lot_2_2_effectifs/exposes/13_J6_article_63.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('lot_2_2_effectifs:exposes:14_j6_article_additionnel', 'livrables/lot_2_2_effectifs/exposes/14_J6_article_additionnel.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('lot_2_3_subventions_associations.perime', 'livrables/lot_2_3_subventions_associations.PERIME.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('lot_2_3_subventions_associations', 'livrables/lot_2_3_subventions_associations.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('lot_4_3_aide_fondamentale_et_taux_unique', 'livrables/lot_4_3_aide_fondamentale_et_taux_unique.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('piece_4_4_taxe_fonciere_unique', 'livrables/piece_4_4_taxe_fonciere_unique.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('registre_colonnes_depot_2027', 'livrables/registre_colonnes_depot_2027.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('registre_exceptions_dates', 'livrables/registre_exceptions_dates.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('registre_sources_gage', 'livrables/registre_sources_gage.md', 'derive', True, None,
     ["lecture de l'auteur"], []),
    ('commun', 'methode/COMMUN.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('analyse_constitutionnelle_collectivites_20261005', 'methode/analyse_constitutionnelle_collectivites_20261005.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('consignes_auteure_20261005', 'methode/consignes_auteure_20261005.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('controle_avant_transmission', 'methode/controle_avant_transmission.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('cr_consolidation_20261007', 'methode/cr_consolidation_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('cr_fil_de_tete_20261007', 'methode/cr_fil_de_tete_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:app_anomalies_pieces', 'methode/etats/APP_anomalies_pieces.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:app_anomalies_registres', 'methode/etats/APP_anomalies_registres.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:app_arrets_immediats', 'methode/etats/APP_arrets_immediats.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:app_classeur_20261007', 'methode/etats/APP_classeur_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:app_collectivites', 'methode/etats/APP_collectivites.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:app_compte_epargne', 'methode/etats/APP_compte_epargne.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:app_divisions_en_clair_20261007', 'methode/etats/APP_divisions_en_clair_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:app_etatb', 'methode/etats/APP_etatB.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:app_fiscal', 'methode/etats/APP_fiscal.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:app_social', 'methode/etats/APP_social.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:app_taxe_fonciere_20261007', 'methode/etats/APP_taxe_fonciere_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:calendrier_20261007', 'methode/etats/CALENDRIER_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:cloture_gage_20261007', 'methode/etats/CLOTURE_gage_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:croisements_20261007', 'methode/etats/CROISEMENTS_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:gage_taxes_affectees_20261007', 'methode/etats/GAGE_taxes_affectees_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:inscription_arbitrages_20261007', 'methode/etats/INSCRIPTION_arbitrages_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:l1', 'methode/etats/L1.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:l10_l11', 'methode/etats/L10_L11.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:l12', 'methode/etats/L12.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:l13', 'methode/etats/L13.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:l14_l16_l18', 'methode/etats/L14_L16_L18.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:l15_l17_l19', 'methode/etats/L15_L17_L19.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:l2', 'methode/etats/L2.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:l3_l5', 'methode/etats/L3_L5.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:l6_l8', 'methode/etats/L6_L8.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:mesure_taxes_affectees_20261007', 'methode/etats/MESURE_taxes_affectees_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:n1', 'methode/etats/N1.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:n2', 'methode/etats/N2.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:n3', 'methode/etats/N3.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:n4', 'methode/etats/N4.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:n5', 'methode/etats/N5.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:n6', 'methode/etats/N6.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:n7a', 'methode/etats/N7a.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:n7b', 'methode/etats/N7b.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_10_impression_trois_liasses_20261008', 'methode/etats/NUIT_10_impression_trois_liasses_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_1a_accroches_20261008', 'methode/etats/NUIT_1A_accroches_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_1b_versement_20261008', 'methode/etats/NUIT_1B_versement_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_1c_pieces_dues_20261008', 'methode/etats/NUIT_1C_pieces_dues_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_2_colonnes_20261008', 'methode/etats/NUIT_2_colonnes_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_2bis_versement_20261008', 'methode/etats/NUIT_2bis_versement_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_3a_exposes_20261008', 'methode/etats/NUIT_3A_exposes_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_3b_controles_1_2_20261008', 'methode/etats/NUIT_3B_controles_1_2_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_3ter_corrections_20261008', 'methode/etats/NUIT_3ter_corrections_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_4_rattachement_contestabilite_20261008', 'methode/etats/NUIT_4_rattachement_contestabilite_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_5_6_liasse_20261008', 'methode/etats/NUIT_5_6_liasse_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_7_exposes_appliques_20261008', 'methode/etats/NUIT_7_exposes_appliques_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_8_impression_20261008', 'methode/etats/NUIT_8_impression_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:nuit_9_tri_trois_liasses_20261008', 'methode/etats/NUIT_9_tri_trois_liasses_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:plafond_30_20261008', 'methode/etats/PLAFOND_30_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:reconciliation_impositions_maintenues', 'methode/etats/RECONCILIATION_impositions_maintenues.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:reprise_bilan_20261008', 'methode/etats/REPRISE_bilan_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:reprise_depenses_20261007', 'methode/etats/REPRISE_depenses_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:retablissement_taxes_affectees_20261007', 'methode/etats/RETABLISSEMENT_taxes_affectees_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:s1', 'methode/etats/S1.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:s2', 'methode/etats/S2.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:s3', 'methode/etats/S3.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:t1', 'methode/etats/T1.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:t2', 'methode/etats/T2.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:t3', 'methode/etats/T3.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:u1', 'methode/etats/U1.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:u3', 'methode/etats/U3.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:u4', 'methode/etats/U4.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:u5', 'methode/etats/U5.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:u6', 'methode/etats/U6.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:u7', 'methode/etats/U7.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:v1', 'methode/etats/V1.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:v2', 'methode/etats/V2.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:application_corrections_20261007', 'methode/etats/application_corrections_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:controle_extraction_p1_fiscale_20261007', 'methode/etats/controle_extraction_p1_fiscale_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:cr_relecture_p1_fiscale_20261007', 'methode/etats/cr_relecture_p1_fiscale_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:file_attente', 'methode/etats/file_attente.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('etats:mesure_paquet_20261007', 'methode/etats/mesure_paquet_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('fragments:arbitrages:20261005_reponses_audit_declinaison', 'methode/fragments/arbitrages/20261005-reponses-audit-declinaison.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('fragments:arbitrages:20261005_revue_lot1_clause', 'methode/fragments/arbitrages/20261005-revue-lot1-clause.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('fragments:arbitrages:20261006_digestion_regles_credits', 'methode/fragments/arbitrages/20261006-digestion-regles-credits.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('fragments:journal:20261007_integration_reprise', 'methode/fragments/journal/20261007-integration-reprise.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('gestion_depot_projet', 'methode/gestion_depot_projet.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('mode_de_production', 'methode/mode_de_production.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('objectifs_depot_2027', 'methode/objectifs_depot_2027.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('ordre_des_fils', 'methode/ordre_des_fils.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('passation_20261005', 'methode/passation_20261005.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('passation_20261007', 'methode/passation_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('passation_20261008', 'methode/passation_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('passation_relecture_export_20261008', 'methode/passation_relecture_export_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('pingpong_depot_2027_20261005', 'methode/pingpong_depot_2027_20261005.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('plan_liasse_2027_20261005', 'methode/plan_liasse_2027_20261005.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('premier_versement_propose', 'methode/premier_versement_propose.tsv', 'methode', True, None,
     ['lecture de fil'], []),
    ('procedure_nuit_20261008', 'methode/procedure_nuit_20261008.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('registre_exposes_depot_2027', 'methode/registre_exposes_depot_2027.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('reprise_20261007', 'methode/reprise_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('revue_dispositifs_20261005', 'methode/revue_dispositifs_20261005.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('suivi_depenses_20261007', 'methode/suivi_depenses_20261007.md', 'methode', True, None,
     ['lecture de fil'], []),
    ('paquet:machine_v1_2_a3:lisez_moi', 'paquet/machine_v1_2_a3/LISEZ-MOI.md', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:appareil:controle_sortie', 'paquet/machine_v1_2_a3/appareil/controle_sortie.py', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:appareil:installer_droit', 'paquet/machine_v1_2_a3/appareil/installer_droit.py', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:appareil:portes_ouvertes', 'paquet/machine_v1_2_a3/appareil/portes_ouvertes.py', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:motifs_locaux_atelier', 'paquet/machine_v1_2_a3/motifs_locaux_atelier.txt', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:procedures:contrat_chaine_amendement', 'paquet/machine_v1_2_a3/procedures/contrat_chaine_amendement.md', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:procedures:domaine_lfss_lo111_3', 'paquet/machine_v1_2_a3/procedures/domaine_lfss_LO111-3.md', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:procedures:gabarit_expose_sommaire', 'paquet/machine_v1_2_a3/procedures/gabarit_expose_sommaire.md', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:procedures:gabarit_liste_articles', 'paquet/machine_v1_2_a3/procedures/gabarit_liste_articles.md', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:procedures:passation_droit_renvois', 'paquet/machine_v1_2_a3/procedures/passation_droit_renvois.md', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:procedures:procedure_vecteurs', 'paquet/machine_v1_2_a3/procedures/procedure_vecteurs.md', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:procedures:structure_ppl', 'paquet/machine_v1_2_a3/procedures/structure_ppl.md', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_2_a3:procedures:test_rattachement', 'paquet/machine_v1_2_a3/procedures/test_rattachement.md', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_3:motifs_locaux_atelier', 'paquet/machine_v1_3/motifs_locaux_atelier.txt', 'derive', True, None,
     ['machine à amendements'], []),
    ('paquet:machine_v1_4:manifeste', 'paquet/machine_v1_4/MANIFESTE.md', 'derive', True, None,
     ['machine à amendements'], []),
    # ------------------------------------------------------------------ racine
    ('instructions', 'CLAUDE.md', 'methode', True, None,
     ['ouverture de session'], ['CLAUDE.md']),
    ('chaine', 'Makefile', 'appareil', True, None, ['make'], ['Makefile']),
    ('exclusions_git', '.gitignore', 'appareil', True, None, ['git'], []),
    ('demarrage', 'DEMARRAGE.md', 'methode', True, None,
     ['installation locale'], []),
]

# Artefacts cités par les skills, ou spécifiés, et qui n'existent nulle part.
# Les nommer explicitement vaut mieux que de laisser un renvoi mourir en
# silence. L'ordre est celui de lecture de la carte, du plus lourd au plus léger.
#
# `intitule` est le titre lisible : la carte le rend tel quel, et le `motif` est
# son paragraphe. Un seul texte, servi aux deux endroits.
#
# `guide_legistique` a quitté cette liste : il n'est pas perdu, il est digéré
# dans `sources/guide_legistique.md`, qui en porte l'alias. Même sort pour
# `guide_public_budgetaire`, sorti des manquants le 20261007 : son original est
# versé au dépôt sous `sources/guide-public-du-budgetaire-2023.pdf` et il est
# digéré dans `sources/regles_credits.md`.
MANQUANTS = [
    # Déclaré voie `depot` par l'index du coffre, absent du dépôt : le fil du
    # second cercle l'a écrit le 20260917 sans le pousser.
    ('epreuve_controle_socle', 'appareil/epreuve_controle_socle.py', 'appareil',
     "Épreuve du contrôle du socle — écrite au second cercle, jamais poussée",
     "Le fil du second cercle du socle a écrit ce module le 20260917 : quatorze "
     "fautes qui lèvent toutes leur code, sept justes qui ne lèvent rien, "
     "joués par `make controle`. Il n'est pas au dépôt, et l'index du coffre "
     "le déclarait pourtant rendu par lui. `epreuve_s17_salaire.py` doit s'y "
     "fondre. À réécrire, ou à retrouver.",
     ['make controle', 'epreuve_s17_salaire.py']),
    # `articles_ouverts_plf.py` a quitté cette liste le 20260903 : il est
    # réécrit, versé, et sa sortie prouvée identique à l'octet aux deux tables
    # que le coffre portait.
    #
    # Relevé du même fil, et il n'était pas déclaré : le `Makefile` invoque un
    # second module absent. Ce n'est pas le même manque — celui-là est un
    # contrôle, pas un générateur, et son absence ne bloque aucune sortie.
    ('controle_socle_plf_gen', 'appareil/controle_socle_plf.py', 'appareil',
     "Contrôle du socle du texte déposé — invoqué par `make controle`, "
     "jamais versé",
     "La cible `controle` du Makefile appelle `controle_socle_plf.py` sur "
     "chacun des deux socles, avec sa pièce et sa table d'articles ouverts. Le "
     "module n'est ni au dépôt, ni au coffre, ni dans l'archive du sas de la "
     "lecture en creux. La règle du Makefile est gardée par un test de "
     "présence du socle, donc `make controle` ne casse pas : il ne contrôle "
     "simplement rien sur les deux socles, et cela ne se voyait pas. Les dix "
     "contrôles internes de `socle_plf_texte.py` tournent, eux, à chaque "
     "génération. À réécrire, ou à retrouver.",
     ['Makefile', 'make controle']),
    # Troisième absent du même relevé, et le plus coûteux des trois : c'est la
    # jointure qui dit quelle mesure du corpus tombe sur un article que le
    # texte déposé ouvre déjà (A-293), et le dépliage des cinq fourchettes
    # attend d'elle sa consommation (A-333). Tant qu'il manque, les douze
    # adresses intérieures des plages restent comptées fermées.
    ('portes_ouvertes_gen', 'appareil/portes_ouvertes.py', 'appareil',
     "Jointure des portes ouvertes — invoquée par `make`, jamais versée",
     "Le Makefile appelle `portes_ouvertes.py` sur `REF_norme` et les deux "
     "tables plates du texte déposé pour produire "
     "`referentiels/portes_ouvertes.tsv`. Le module n'est ni au dépôt, ni au "
     "coffre, ni dans l'archive du sas de la lecture en creux. La règle est "
     "gardée par la présence de `REF_norme`, donc rien ne casse : la jointure "
     "ne se fait simplement pas. À réécrire, ou à retrouver — et sa réécriture "
     "est l'occasion de consommer le dépliage des fourchettes, qui vit à côté "
     "sans être lu.",
     ['Makefile', 'REF_norme', 'plages_articles.json', 'vecteur-mesure']),
    # Quatre pièces sorties du projet par l'auteur, entre le 20260903 et le
    # 20260906. Elles ne se recomposent pas — un binaire ne se refait pas par le
    # modèle — et aucune n'a de digestion au corpus. Elles se déclarent ici
    # plutôt que de disparaître de la table de résolution : un renvoi qui ne
    # résout pas ne meurt pas en silence.
    ('guide_nl_cba', 'sources/NL_cba-guidance.pdf', 'source',
     "Guide néerlandais coût-bénéfice — sorti du projet, non digéré",
     "Méthode d'évaluation étrangère. Même régime et même constat que le guide "
     "public du budgétaire. À rejoindre s'il sert.",
     ['citation sourcée']),
    ('comparaison_internationale', 'sources/Comparaison_internationale.pdf',
     'source',
     "Annexe des régimes de retraite comparés — sortie du projet le 20260906",
     "Écarts avec les pays comparables. Retirée par l'auteur, qui la refera "
     "plus tard : c'est une sortie décidée, non une perte. Aucune digestion.",
     ['citation sourcée']),
    ('resolution_d1a', 'sources/ResolutionD1a.png', 'source',
     "Page de garde ResolutionD1a — sortie du projet",
     "Image de garde, pièce jointe. Sortie constatée le 20260906. La charte "
     "graphique attend par ailleurs la couverture du livre, qui n'a jamais été "
     "au projet.",
     ['charte graphique']),
    ('strategie_reseaux', 'sources/France_Resolution_Strategie_Reseaux_2.pdf',
     'source',
     "Stratégie réseaux — sortie du projet, digestion partielle",
     "Pièce jointe. A-366 constatait le 20260906 qu'elle était encore au "
     "projet ; la confrontation des pièces jointes du 20260907 ne l'y trouve "
     "plus. Sa part digérée tient : le lexique (A-53), la date de parution du "
     "livre et son identification au manuscrit (A-55), trois angles morts "
     "(A-54). Ce qui sort avec elle et n'est digéré nulle part : "
     "l'architecture des comptes, le plan de lancement, les cinq postures, les "
     "scripts. C'est la sortie qu'A-366 disait coûteuse faute de digestion "
     "courte, et elle a eu lieu.",
     ['citation sourcée', 'plan de lancement']),
    # Les quatre modules du relevé de mandat, écrits le 20260910 depuis Cowork,
    # déclarés au dépôt par l'index du coffre, et **jamais poussés**. Le clone
    # du 20260911 ne les porte pas — `HEAD` à `9bf6744`, diff vide sur ces
    # quatre chemins — et le conteneur qui les portait est mort avec la
    # session. C'est A-394 réalisée : le fil qui corrige ne peut pas pousser,
    # et ce qu'il n'a pas poussé n'existe plus. Leur sortie, elle, est au
    # coffre : `livrables/releve_epreuve_EP3.tsv` et son `.md` restent lisibles
    # et font spécification exécutable si on les réécrit — c'est l'asymétrie
    # d'A-343, et elle joue ici en faveur de la réécriture.
    ('flux_epreuve_gen', 'appareil/flux_epreuve.py', 'appareil',
     "Flux de page d'une épreuve — écrit le 20260910, jamais poussé, perdu",
     "Extraction du flux de composition d'une épreuve, à deux échelles : les "
     "caractères couverts par un surlignage, et les lignes de composition qui "
     "les portent. Consommé par `relever_mandat_epreuve.py` et "
     "`valeurs_epreuve_relachees.py`. Déclaré voie `depot` par l'index du "
     "coffre, absent du clone. À réécrire depuis le relevé EP3, qui est sa "
     "sortie versée.",
     ['relever_mandat_epreuve.py', 'valeurs_epreuve_relachees.py']),
    ('relever_mandat_epreuve_gen', 'appareil/relever_mandat_epreuve.py',
     'appareil',
     "Relevé de mandat d'une épreuve — écrit le 20260910, jamais poussé, perdu",
     "Apparie les surlignages annotés d'une épreuve relue aux écarts de "
     "l'épreuve nouvelle, et rend les quatre mandats `porté`, `porté de "
     "travers`, `non porté`, `non demandé`, chacun avec sa preuve — `texte`, "
     "`suppression`, `alinéa`, `place`. Absent du clone. À réécrire depuis le "
     "relevé EP3.",
     ['rendre_releve_mandat.py', 'relecture d’épreuve contre épreuve']),
    ('valeurs_epreuve_relachees_gen', 'appareil/valeurs_epreuve_relachees.py',
     'appareil',
     "Contrôle relâché des grandeurs — écrit le 20260910, jamais poussé, perdu",
     "Relève les grandeurs du corpus dans une épreuve sur un texte dont les "
     "césures sont recollées, puis une seconde fois sans les virgules : c'est "
     "ce qui empêche un contrôle de disparaître au lieu d'échouer. Absent du "
     "clone. À réécrire — sa règle est écrite au relevé EP3.",
     ['contrôle des chiffres d’une épreuve', 'bon à tirer']),
    ('rendre_releve_mandat_gen', 'appareil/rendre_releve_mandat.py', 'appareil',
     "Rendu du relevé de mandat — écrit le 20260910, jamais poussé, perdu",
     "Rend `livrables/releve_epreuve_EP3.tsv` et son `.md`. Absent du clone, "
     "quand ses deux sorties sont au coffre : elles font spécification "
     "exécutable pour sa réécriture, à l'octet, comme la sortie versée "
     "d'`articles_ouverts_plf.py` l'avait fait en A-343.",
     ['relecture d’épreuve contre épreuve', 'bon à tirer']),
    ('releve_affecte', 'referentiels/releve_affecte.json', 'referentiel',
     'Releve_affecte — attendu par trois skills',
     "Couche de preuve à identifiants M-nnnn, citée par compatibilite-doctrine, "
     "contestabilite et qa-riposte. Introuvable. À reconstruire ou à retirer "
     "des trois skills.",
     ['compatibilite-doctrine', 'contestabilite', 'qa-riposte']),
    ('couverture_livre', 'sources/couverture_livre', 'source',
     'Couverture du livre — attendue par la charte',
     "Nécessaire à la charte graphique définitive. Absente du projet.",
     ['charte graphique']),
    ('qa_reference', 'livrables/qa_reference.md', 'derive',
     'Q&A de référence — attendue par qa-riposte',
     "La skill demande une Q&A à statut « référence » comme modèle de ton. Le "
     "corpus ne porte qu’un proto, dont la citation externe est interdite.",
     ['qa-riposte']),
]

# Archives de `sources/` qui n'existent nulle part ailleurs et que le coffre doit
# donc porter. Le reste de `sources/` vit déjà au projet comme fichier ou
# document : le coffre ne le redouble pas.
# `sources/` est plat au dépôt : c'est la copie de travail, et le contrôle y
# tolère les noms datés. Au coffre, en revanche, ces documents sont rangés — le
# coffre est la vue de l'auteur. La table dit où chacun se lit.
#
#   archive/    nos sorties gelées, produites avant les gabarits et les contrôles
#   reference/  textes normatifs en vigueur et leurs mises en forme
#   input/      documents de l'auteur ou de tiers versés comme documents
#
# Ce qui n'y figure pas est une pièce jointe du projet, que Claude ne peut pas
# déplacer, ou une copie de travail d'une pièce jointe, que le coffre ne redouble
# pas.
COFFRE_SOURCES = {
    # --- nos sorties gelées
    'sources/Input_gagnants_perdants_20260820_v1_brouillon.html':
        'archive/Input_gagnants_perdants_20260820_v1_brouillon.html',
    'sources/Reserve_arguments_20260806_v1.html':
        'archive/Reserve_arguments_20260806_v1.html',
    'sources/1pager_20260806_v1_proto.html':
        'archive/1pager_20260806_v1_proto.html',
    'sources/Input_HLM_20260806_v1_proto.html':
        'archive/Input_HLM_20260806_v1_proto.html',
    'sources/Note_entreprises_20260806_v1_proto.html':
        'archive/Note_entreprises_20260806_v1_proto.html',
    'sources/Donnees_20260806_v1_proto.html':
        'archive/Donnees_20260806_v1_proto.html',
    'sources/QA_20260806_v1_proto.html':
        'archive/QA_20260806_v1_proto.html',
    'sources/Recap_transposabilite_20260731_v6.md':
        'archive/Recap_transposabilite_20260731_v6.md',
    'sources/Recensement_innovations_20260731_v1.md':
        'archive/Recensement_innovations_20260731_v1.md',
    'sources/Presentation_20260731_v44.md':
        'archive/Presentation_20260731_v44.md',
    'sources/note_reforme_budgetaire_20260730_v12.html':
        'archive/note_reforme_budgetaire_20260730_v12.html',
    'sources/Plan_presentation_20260730_v6.md':
        'archive/Plan_presentation_20260730_v6.md',
    'sources/PPLC_consolidee_modificative_20260730_v6.md':
        'archive/PPLC_consolidee_modificative_20260730_v6.md',
    'sources/PPLC_consolidee_substitution_20260730_v6.md':
        'archive/PPLC_consolidee_substitution_20260730_v6.md',
    'sources/Precedents_restes_a_payer_20260721.md':
        'archive/Precedents_restes_a_payer_20260721.md',
    # --- textes normatifs de référence
    'sources/Constitution_reference_20260806_v1.html':
        'reference/Constitution_reference_20260806_v1.html',
    'sources/Constitution_3col_20260730_v44.html':
        'reference/Constitution_3col_20260730_v44.html',
    'sources/DDHC_20260806_v1.html':
        'reference/DDHC_20260806_v1.html',
    'sources/LOLF_reference_20260507.html':
        'reference/LOLF_reference_20260507.html',
    'sources/LOLF_3col_20260507_v7.html':
        'reference/LOLF_3col_20260507_v7.html',
    'sources/guide_legistique.md':
        'reference/guide_legistique.md',
    'sources/regles_credits.md':
        'reference/regles_credits.md',
    # Rapport de clôture du fil gagnants-perdants du 20260820. Il portait le nom
    # `ETAT_DU_CHANTIER`, qui laissait croire à un point de situation courant :
    # il ne parle ni de la machine à amendements, ni du projet de loi de
    # finances, et son inventaire de montage est celui d'un dispositif remplacé.
    # Renommé le 20260902, contenu inchangé à l'octet — un document externalisé
    # ne se réécrit pas.
    'sources/rapport_gagnants_perdants_20260820.md':
        'archive/rapport_gagnants_perdants_20260820.md',
    # Note de l'auteur, versée en `input/`.
    'sources/accroche_politique_revision_20260901.md':
        'input/accroche_politique_revision_20260901.md',
    # La table primitive d'une source externe, compagnon de sa digestion. Elle
    # se refait par relecture d'un nouveau millésime et ne se corrige pas à la
    # main ; aucun montant ne s'en cite directement.
    'sources/prelevements_ifrap.tsv':
        'referentiels/prelevements_ifrap.tsv',
    # --- documents de l'auteur ou de tiers, versés comme documents
    # `NL_cba-guidance.pdf` a quitté le coffre entre le 20260903 et le 20260904 :
    # `restaurable: false` et sans digestion, rien ne le remet, il est aux
    # manquants. `guide-public-du-budgetaire-2023.pdf` en est sorti le 20261007 :
    # son original est versé sous `sources/` et il est digéré par `regles_credits`.
    'sources/20250619_Note_Retraite_IB.docx':
        'input/Note_Retraite_20250619.docx',
    # Versé par l'auteur le 20260827 à la racine du coffre, sous un nom qui
    # n'est pas canonique. C'est un docx : le coffre le porte comme document et
    # non comme octets, et il ne se déplace donc pas — le recomposer par le
    # modèle fabriquerait un faux binaire. Il se déclare là où il est, et le
    # chantier n'entre pas par lui mais par sa digestion,
    # `sources/gabarit_expose_sommaire.md`.
    # Le prompt d'ouverture de la session d'organisation, versé par l'auteur.
    'sources/prompt_session_organisation_20260827.md':
        'methode/prompt_session_organisation.md',
}

# Les pièces jointes du projet. Elles ne sont pas versées au coffre — elles y
# sont déjà, comme fichiers ou documents, et Claude ne peut ni les déplacer, ni
# les renommer, ni les supprimer. Elles ne sont pas non plus restaurables au
# dépôt par script : un classeur ou un PDF ne se réécrit pas depuis le coffre
# sans passer par le modèle, ce qui le déformerait.
#
# Elles sont donc déclarées ici, et `controle_index.py` traite leur absence du
# conteneur comme une constatation, non comme une anomalie.
SOURCES_JOINTES = [
    # Deux pièces sont sorties du projet le 20260903, sur décision de l'auteur,
    # pour libérer la jauge — 172 190 jetons rendus. Elles ne sont donc plus des
    # pièces jointes, et elles ne sont pas non plus digérées : leur digestion
    # est due et inscrite à `reference/digestions_attendues.md` (A-350). Elles
    # rentreront par pièce jointe du fil qui les digérera, comme les classeurs.
    #
    #   sources/RAPPORTLemodelesocialfrancaisGenerationLibreFevrier2025.pdf
    #     — en réalité un rapport AIRE, « Le modèle social français contre les
    #       couples », février 2025. Le nom du fichier a induit son classement
    #       en erreur, et le registre des digestions le dit.
    #   sources/201701LIBERunepropositionrealiste_generationlibre.pdf
    #     — Génération Libre, LIBER volume II, janvier 2017, base 2016. Ses
    #       chiffres sont à réactualiser avant tout emploi.
    # Retiré du coffre le 20260901 sur autorisation de l'auteur, qui en a copie
    # (A-264). Son grain est porté à `sources/gabarit_expose_sommaire.md` avant
    # la suppression ; il rentre désormais par pièce jointe du fil qui en a
    # besoin, comme les classeurs.
    # L'épreuve validée par l'auteur le 20260911, dont `livre/texte_livre.json`
    # est extrait : 180 pages, composée le 10/09/2026, 2 759 475 octets,
    # `sha256 1ea863869f75fe4eb4711c99c3bacca6811d92426ead40f571913332f199948b`.
    # Le texte va au coffre, le binaire non — c'est le régime des épreuves
    # depuis le 20260908. Elle rentre par pièce jointe du fil qui rejoue
    # l'extraction, comme les classeurs, et sa jonction au projet revient à
    # l'auteur.
    'sources/ETAT_PARTOUT_JUSTICE_NULLE_PART_EP3.pdf',
    'sources/Expose_des_motifs_redaction_GL.docx',
    'sources/France_Resolution_Strategie_Reseaux_2.pdf',
    'sources/Note_n__1_Justice_fiscalecomment_nous_avons_trahi_1789.pdf',
    'sources/PLF26__Depenses_2026_du_BG_et_des_BA_selon_nomenclatures_'
    'destination_et_nature_IB_1127.xls',
    'sources/PLF_2026_VM_tome_II__Annexe_3__Depenses_fiscales__IB__1126.xls',
    'sources/PLF_2026_VM_tome_I__Annexe_2__Taxes_affectees_IB_1113.xls',
    'sources/Synthèse_Calculs_Résolution_0819.xlsx',
    'sources/Synthèse_ETP_et_agences_Résolution_0819.xls',
    'sources/T_3207_Communes_IB_1113.xlsx',
    'sources/T_3305_APUL_IB_1118.xlsx',
    'sources/deppee2025donneesfiche09ladepensepourleducation25_12_19IB.xlsx',
    'sources/dgfip_stat_32_2025.pdf',
    'sources/etude_fondation_ifrap_liste_des_impots_et_taxes.pdf',
    'sources/fondapollimpassedelataxezucman_fr_20260608_formatweb_w.pdf',
]

# Alias supplémentaires portés par une source. Un renvoi qui visait un document
# absent se résout ainsi sur celui qui l'a digéré : le guide de légistique du
# SGG n'entre pas au corpus par son fichier, il entre par `guide_legistique`,
# et le Guide du budgétaire par `regles_credits`.
ALIAS_SOURCES = {
    'sources/guide_legistique.md': ['guide_legistique', 'structure_ppl',
                                    'guide_redaction',
                                    'guide_domaine_financier',
                                    'guide_legistique_2026.pdf'],
    'sources/regles_credits.md': ['guide_budgetaire',
                                  'guide-public-du-budgetaire-2023.pdf'],
    'sources/rapport_gagnants_perdants_20260820.md': [
        'ETAT_DU_CHANTIER_20260820_v22.md',
        'methode/ETAT_DU_CHANTIER.md',
        'etat_du_chantier'],
}

# Ce qu'aucun script ne peut remettre au dépôt. Deux cas, une conséquence.
#
# Les pièces jointes du projet : Claude n'a pas la main sur elles.
# Les documents binaires du coffre — un PDF, un docx : le coffre les porte comme
# documents, non comme octets. Les réécrire au dépôt supposerait de les
# recomposer par le modèle, ce qui fabriquerait un faux binaire.
#
# `controle_index.py` traite leur absence du conteneur comme une constatation.
NON_RESTAURABLES = set(SOURCES_JOINTES) | {
    'sources/20250619_Note_Retraite_IB.docx',
}

# Le coffre n'accepte pas de fichier à la racine sous un nom nu : il le range
# d'office dans un espace réservé. Les artefacts de racine y prennent donc un
# préfixe, sauf les deux qui y existaient déjà avant la bascule.
COFFRE_RACINE = {
    'DEMARRAGE.md': 'racine/DEMARRAGE.md',
    '.gitignore': 'racine/gitignore',
}

# Rangs dont les fichiers ne vivent pas au coffre mais **au dépôt**, sous une
# sous-racine qui leur est propre. Le coffre est aussi la vue de l'auteur, et une
# liste de Python et de JSON y masque ses vrais produits : ils y étaient donc
# repliés dans une archive unique. Depuis le 20260909 (A-395) ils sont au dépôt,
# ce qui rend le même service — l'auteur ne les voit pas — et deux de plus : la
# restauration est une copie d'octets par `git clone`, et ils ne pèsent plus
# rien à la jauge du coffre.
#
# **Deux corpus dans un dépôt, deux racines distinctes** : le dépôt de droit à la
# racine, l'appareil du chantier sous `chantier/`, chacun avec son `.gitignore`.
# Ne pas les mêler — le `.gitignore` du chantier ignore `droit/`, et posé à la
# racine il masquerait le dépôt de droit tout entier.
DEPOT_RANGS = {'appareil', 'referentiel'}
DEPOT = {
    'nom': 'resolution-ib-dev/Resolution-2027',
    'url': 'https://github.com/resolution-ib-dev/Resolution-2027',
    'branche': 'main',
    'sous_racine': 'chantier',
    'clone': ('git clone https://github.com/resolution-ib-dev/Resolution-2027 '
              'droit && cp -r droit/chantier/. .'),
    'ecriture': "fermée depuis Cowork (A-393) : une pièce due au dépôt se "
                "déclare au registre et se pousse d'une session claude.ai/code. "
                "`appareil/coffre.py dette` dit ce qui est dû.",
}

# L'exception : une pièce de rang `appareil` ou `referentiel` versée au coffre
# **comme document**, à son propre chemin, et non portée au dépôt.
#
# **La table est vide depuis le 20260909, et elle reste.** Elle a porté quatre
# entrées : les deux référentiels de rédaction du texte déposé — 848 687 et
# 351 968 octets — et les deux modules de la réapplication. Les premiers y
# étaient depuis A-349, parce qu'une pièce plus grosse que l'archive ne s'y
# repliait pas sans rendre sa réécriture impossible ; les seconds parce que le
# fil qui les a écrits n'a pas replié le coffre. **Les deux motifs sont morts
# avec l'archive** (A-395), et les quatre ont été poussées au dépôt le 20260909,
# commit de fusion `31896bb5`, prouvées identiques à l'octet contre le clone et
# contre leur empreinte avant d'être supprimées du coffre — prouver, puis
# supprimer (A-357).
#
# **Elle reste parce que le cas peut revenir** : une pièce de l'appareil qu'un
# fil Cowork écrit ne peut pas être poussée par lui, l'écriture au dépôt étant
# fermée (A-393). Elle vit alors au coffre comme document, déclarée ici, et
# `coffre.py dette` la réclame en `D3` jusqu'à ce qu'un fil claude.ai/code la
# porte. Une entrée s'y ajoute sur mesure, jamais par intuition, et elle se
# retire **après** la preuve, jamais avant.
COFFRE_DOCUMENT = {
    # Rattrapage du 20260930 : six grilles écrites par des fils Cowork, au
    # coffre à leur propre chemin et absentes du dépôt.
    'referentiels/cgi_expert_articles.tsv':
        'referentiels/cgi_expert_articles.tsv',
    'referentiels/cgi_expert_insertions.tsv':
        'referentiels/cgi_expert_insertions.tsv',
    'referentiels/cgi_expert_suppressions.tsv':
        'referentiels/cgi_expert_suppressions.tsv',
    'referentiels/cgi_expert_articles_bouges.tsv':
        'referentiels/cgi_expert_articles_bouges.tsv',
    'referentiels/cgi_expert_parametres.tsv':
        'referentiels/cgi_expert_parametres.tsv',
    'referentiels/prelevements_forces_20260930.tsv':
        'referentiels/prelevements_forces_20260930.tsv',
    # Rattrapage du 20261001 : deux grilles du fil du sort des prélèvements,
    # au coffre à leur propre chemin et absentes du dépôt.
    'referentiels/sort_prelevements_20260930.tsv':
        'referentiels/sort_prelevements_20260930.tsv',
    'referentiels/table_passage_schema_prelevements_20260930.tsv':
        'referentiels/table_passage_schema_prelevements_20260930.tsv',
}

CLES = ('role', 'chemin', 'rang', 'coffre', 'produit_par', 'consomme_par', 'alias')

# Le rang d'un fichier relevé du dossier sans être déclaré aux tables : celui
# que portent déjà les artefacts déclarés du même dossier de tête.
RANG_PAR_DOSSIER = {'appareil': 'appareil', 'referentiels': 'referentiel',
                    'sources': 'source', 'livrables': 'derive',
                    'paquet': 'derive', 'site': 'derive'}


def voie_de(artefact, defaut):
    """La surface qui rend l'artefact, et le chemin qu'elle en porte.

    `defaut` est le chemin au coffre quand la voie est le coffre et que rien de
    particulier ne le déplace — le chemin de dépôt, ou son préfixé de racine, ou
    celui d'une source rangée autrement.

    Quatre voies, et aucune cinquième :

      depot         le clone du dépôt le rend, par copie d'octets
      coffre        le coffre le rend, en texte au transcript ou comme fichier
      piece_jointe  nul script ne le rend — l'auteur le rejoint
      hors_coffre   rien ne le rend de l'extérieur : `make` le refait
    """
    a = artefact
    if not a['coffre']:
        return 'hors_coffre', defaut
    if not a.get('restaurable', True):
        return 'piece_jointe', defaut
    if a['rang'] in DEPOT_RANGS and a['chemin'] not in COFFRE_DOCUMENT:
        return 'depot', f"{DEPOT['sous_racine']}/{a['chemin']}"
    return 'coffre', COFFRE_DOCUMENT.get(a['chemin'], defaut)


def generer(dst, racine):
    artefacts = [dict(zip(CLES, a)) for a in ARTEFACTS]
    # Par quelle voie l'artefact revient, et où il se lit sur cette voie.
    for a in artefacts:
        a['restaurable'] = True
        a['voie'], a['chemin_coffre'] = voie_de(
            a, COFFRE_RACINE.get(a['chemin'], a['chemin']))

    # --- sources : déclarées, jamais relevées de l'arborescence.
    # Le relevé par balayage faisait dépendre l'index de ce qu'un conteneur
    # contenait ce jour-là : une pièce jointe non restaurée disparaissait de la
    # table de résolution. La table est donc curée, comme tout le reste.
    sources = set(COFFRE_SOURCES) | set(SOURCES_JOINTES)
    for chemin in sorted(sources):
        nom = chemin.split('/')[-1]
        a = {'role': 'source:' + os.path.splitext(nom)[0].lower(),
             'chemin': chemin, 'rang': 'source',
             'coffre': chemin in COFFRE_SOURCES, 'produit_par': None,
             'consomme_par': ['citation sourcée'],
             'alias': [nom] + ALIAS_SOURCES.get(chemin, []),
             'restaurable': chemin not in NON_RESTAURABLES}
        a['voie'], a['chemin_coffre'] = voie_de(
            a, COFFRE_SOURCES.get(chemin, chemin))
        artefacts.append(a)

    # --- le dossier : tout fichier présent sous la racine que les tables ne
    # déclarent pas y entre à son chemin. Le périmètre est celui que relève
    # `controle_index.py`, lu à la même fonction : ce que le contrôle compte en
    # I2, le générateur le déclare. Les tables ci-dessus restent la couche qui
    # porte rôle, rang, producteur, consommateurs et alias ; le balayage ne fait
    # qu'ajouter, si bien qu'une pièce déclarée et absente du conteneur ne
    # disparaît pas de l'index. Un fichier relevé ainsi est au dépôt, puisqu'il
    # y est lu : sa voie est `depot`.
    declares = {a['chemin'] for a in artefacts}
    for chemin in controle_index.fichiers(racine):
        if chemin in declares:
            continue
        tete = chemin.split('/', 1)[0]
        a = {'role': 'fichier:' + os.path.splitext(chemin)[0],
             'chemin': chemin, 'rang': RANG_PAR_DOSSIER.get(tete, 'methode'),
             'coffre': True, 'produit_par': None, 'consomme_par': [],
             'alias': [], 'restaurable': True, 'voie': 'depot',
             'chemin_coffre': f"{DEPOT['sous_racine']}/{chemin}",
             'releve': True}
        artefacts.append(a)

    # --- famille : le classement par contenu, importé de la carte.
    # L'affectation vit dans `generer_carte.py` et nulle part ailleurs ; l'index
    # n'en porte que le report, pour que toute skill puisse le lire.
    table = generer_carte.affectation()
    for a in artefacts:
        a['famille'] = generer_carte.famille_de(a, table)

    manquants = [{'role': r, 'chemin_attendu': c, 'rang': g, 'intitule': i,
                  'motif': m, 'attendu_par': p}
                 for r, c, g, i, m, p in MANQUANTS]

    # Le bloc `depot` remplace l'ancien bloc `archives`. Il ne décrit pas un
    # pli mais une **voie de restauration** : la commande qui la parcourt, la
    # sous-racine qu'elle occupe, et les chemins qu'elle rend. Un fil qui ouvre
    # demain y lit tout ce dont il a besoin, sans avoir à connaître A-395.
    depot = dict(DEPOT)
    depot['rangs'] = sorted(DEPOT_RANGS)
    depot['contient'] = sorted(a['chemin'] for a in artefacts
                               if a['voie'] == 'depot')
    depot['au_coffre_comme_document'] = sorted(
        a['chemin'] for a in artefacts
        if a['rang'] in DEPOT_RANGS and a['coffre'] and a['voie'] == 'coffre')

    index = {'_revision': REVISION, 'artefacts': artefacts,
             'depot': depot, 'manquants': manquants,
             'comptes': {'artefacts': len(artefacts),
                         'au_coffre': sum(1 for a in artefacts if a['coffre']),
                         'au_depot': sum(1 for a in artefacts
                                         if a['voie'] == 'depot'),
                         'derives': sum(1 for a in artefacts if a['rang'] == 'derive'),
                         'sources': sum(1 for a in artefacts if a['rang'] == 'source'),
                         'non_restaurables': sum(1 for a in artefacts
                                                 if not a['restaurable']),
                         'sans_famille': sum(1 for a in artefacts
                                             if not a['famille']),
                         'manquants': len(manquants)}}
    with open(dst, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
        f.write('\n')
    c = index['comptes']
    print(f'{dst} écrit — {c["artefacts"]} artefacts dont {c["au_coffre"]} au '
          f'coffre, {c["au_depot"]} rendus par le dépôt, {c["derives"]} dérivés, '
          f'{c["sources"]} sources, {c["manquants"]} manquant(s) déclaré(s)')
    if depot['au_coffre_comme_document']:
        print(f'    {len(depot["au_coffre_comme_document"])} pièce(s) de '
              f'l\'appareil encore au coffre comme document, dues au dépôt :')
        for ch in depot['au_coffre_comme_document']:
            print(f'        {ch}')
    return 0


if __name__ == '__main__':
    sys.exit(generer(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '.'))
