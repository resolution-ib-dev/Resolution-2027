# Chaîne de génération du projet Résolution.
#
# Un dérivé ne se corrige jamais à la main : il se régénère. Ce fichier dit
# comment. `make` seul refait tout ce qui a changé et rien d'autre.
#
#   make            régénère ce qui doit l'être
#   make controle   joue les contrôles, sans rien produire
#   make propre     efface les dérivés, garde les référentiels
#   make etat       rappelle où en est la rédaction des apports

PY      := python3
APP     := appareil
REF     := referentiels
LIV     := livrables
MAN     := manuscrit

REF_JSON    := $(REF)/REF_doctrine.json
POSITIONS   := $(REF)/positions.json
NOTES       := $(REF)/notes_manuscrit.json
CHIFFRES    := $(REF)/REF_chiffres.json
PROTO_DON   := sources/Donnees_20260806_v1_proto.html
EPREUVE     := sources/ETAT_PARTOUT_JUSTICE_NULLE_PART_EP3.pdf
LIVRE       := livre/texte_livre.json
DONNEES     := $(LIV)/donnees.json
EXTRAIT     := $(LIV)/extrait_gagnants_perdants.html
INTERFACE   := $(LIV)/interface_positions.html
INVENTAIRE  := $(LIV)/inventaire_gagnants_perdants.html
ARBRE       := $(LIV)/ref_doctrine_arbre.html
RELEVE      := $(LIV)/notes_manuscrit_releve.txt
RELEVE_PROTOS := $(LIV)/releve_protos.txt
SITE        := site/index.html
SITE_DIR    := site
GALERIE     := $(LIV)/galerie_fiches.html
ATTRIBUTION := $(LIV)/carte_attribution.html
APPARIEMENT := $(LIV)/appariement_operateurs.txt
SYNTHESE_BUD := $(LIV)/synthese_budgetaire.xlsx
RECON_OP    := $(REF)/reconciliation_operateurs.json
RECON_TXT   := $(LIV)/reconciliation_operateurs.txt
ECO_JSON    := $(REF)/economies.json
ECO_TXT     := $(LIV)/economies_tracees.txt
PORTES      := $(LIV)/portes_domaine.md
AXE_TRANSP  := $(LIV)/axe_transparence.md
VENTILATION := $(LIV)/ventilation_vehicule.md
COLLOCS     := $(LIV)/leviers_collocs.md
VECTEURS    := $(LIV)/chantier_vecteurs.md
NORME       := $(REF)/REF_norme.json
ETAT_VECT   := $(LIV)/etat_vecteurs.html
ETAT_CSV    := $(LIV)/etat_vecteurs.csv
LOLF_REF    := sources/LOLF_reference_20260507.html
CARTE       := $(LIV)/carte_du_projet.html
LOTS        := $(REF)/lots_epreuve.json
ETAT_MACH   := $(LIV)/etat_machine.html
INDEX       := methode/index.json
EMPREINTES  := methode/empreintes.json

.PHONY: tout controle propre etat
# Les cibles qui dérivent du socle budgétaire ne sont pas ici : le socle vient
# des cinq classeurs, qui sont des pièces jointes, et `make` ne doit pas casser
# quand elles ne sont pas à l'atelier. Elles s'ajoutent plus bas, sous leur
# garde, par `BUD_DERIVES` — même procédé que `SOCLES_TEXTE` pour le texte
# déposé. Sans cette garde, `make tout` s'arrêtait sur le premier consommateur
# du socle et ne refaisait rien de ce qui vient après.
BUD_DERIVES :=
tout: $(EXTRAIT) $(INTERFACE) $(INVENTAIRE) $(ARBRE) $(RELEVE) $(CARTE) \
      $(CHIFFRES) $(RELEVE_PROTOS) $(SITE) $(GALERIE) $(ATTRIBUTION) \
      $(PORTES) $(AXE_TRANSP) $(ETAT_MACH)

# --- strate 1 vers référentiel ---------------------------------------------
# Le relevé des notes ne se refait que si son extracteur est présent. Sans lui,
# le relevé versé fait foi et la chaîne continue.
ifneq ($(wildcard $(APP)/extraire_notes.py),)
$(NOTES): $(MAN)/manuscrit.html $(APP)/extraire_notes.py
	cd $(APP) && $(PY) extraire_notes.py ../$(MAN)/manuscrit.html ../$@
endif

# Le référentiel des positions se régénère dès que sa matière bouge : sa
# structure, les justifications des pertes, les apports des gains.
$(POSITIONS): $(APP)/construire_positions.py $(APP)/justifications.py \
              $(APP)/apports.py
	cd $(APP) && $(PY) construire_positions.py ../$@

# --- référentiel des faits -------------------------------------------------
# Il se relève de trois lieux : les notes du manuscrit, le REF_doctrine, et le
# proto Données pour ses candidats non sourcés. Le sourçage écrit à la main vit
# dans `sources_chiffres.py` et survit à chaque régénération.
#
# Le proto est une source restaurable : sans lui, le référentiel versé fait foi
# et la chaîne continue plutôt que de rompre.
ifneq ($(wildcard $(PROTO_DON)),)
$(CHIFFRES): $(NOTES) $(REF_JSON) $(PROTO_DON) \
             $(APP)/generer_ref_chiffres.py $(APP)/sources_chiffres.py
	cd $(APP) && $(PY) generer_ref_chiffres.py ../$(NOTES) ../$(REF_JSON) \
	  ../$(PROTO_DON) ../$@
endif

# --- strate 1 du verbatim citable -------------------------------------------
# Le texte du livre imprimé, extrait de l'épreuve validée par l'auteur le
# 20260911. L'épreuve est une pièce jointe de 2,6 Mo : elle ne va pas au
# coffre, le texte qu'on en tire y va. Sans elle la règle s'efface, comme
# toute règle qui dépend d'une pièce jointe, et le texte versé fait foi.
ifneq ($(wildcard $(EPREUVE)),)
$(LIVRE): $(EPREUVE) $(APP)/texte_livre.py
	$(PY) $(APP)/texte_livre.py $(EPREUVE) $@
endif

# --- projection unique ------------------------------------------------------
# La jointure se fait une fois. Les deux livrables lisent le même fichier et ne
# peuvent pas diverger.
$(DONNEES): $(REF_JSON) $(POSITIONS) $(NOTES) $(APP)/exporter_donnees.py \
            $(APP)/generer_extrait.py $(APP)/generer_inventaire.py
	cd $(APP) && $(PY) exporter_donnees.py ../$(REF_JSON) ../$(POSITIONS) \
	  ../$(NOTES) ../$@

# --- livrables --------------------------------------------------------------
$(EXTRAIT): $(REF_JSON) $(POSITIONS) $(NOTES) $(APP)/generer_extrait.py
	cd $(APP) && $(PY) generer_extrait.py ../$(REF_JSON) ../$(POSITIONS) \
	  ../$(NOTES) ../$@

$(INTERFACE): $(DONNEES) $(APP)/generer_interface.py
	cd $(APP) && $(PY) generer_interface.py ../$(DONNEES) ../$@

# Le site : un index et dix-huit fiches, en pages statiques (A-193). Il ne se
# tire pas de l'interface de travail mais de la galerie, dont il importe le
# rendu de fiche. Vercel déploie $(SITE_DIR) et n'écrit rien.
PROTO_1PAGER := sources/1pager_20260806_v1_proto.html
# Le générateur écrit vingt et une pages d'un coup, et l'index en déclare deux :
# l'entrée, qui vaut pour le dossier, et le manifeste, qui est un livrable
# diffusable à part. **La cible nomme les deux.** Elle n'en nommait qu'une, et
# `make site/manifeste.html` sortait « no rule » dans un dépôt vierge — V2, le
# défaut exact qu'A-385 a relevé six fois et manqué ici : une sortie qu'aucune
# cible ne nomme ne se rejoue jamais par `make`.
SITE_MANIF  := site/manifeste.html

$(SITE) $(SITE_MANIF): $(POSITIONS) $(REF_JSON) $(APP)/generer_site.py \
         $(APP)/generer_fiches.py $(APP)/structure_fiches.py \
         $(APP)/manifeste.py $(PROTO_1PAGER)
	cd $(APP) && $(PY) generer_site.py ../$(POSITIONS) ../$(REF_JSON) \
	  ../$(SITE_DIR) ../$(PROTO_1PAGER)

# La galerie et sa carte d'attribution lisent la même structure arbitrée.
$(GALERIE): $(POSITIONS) $(REF_JSON) $(APP)/generer_fiches.py $(APP)/structure_fiches.py
	cd $(APP) && $(PY) generer_fiches.py ../$(POSITIONS) ../$(REF_JSON) ../$(LIV)

$(ATTRIBUTION): $(POSITIONS) $(REF_JSON) $(APP)/carte_attribution.py $(APP)/structure_fiches.py
	cd $(APP) && $(PY) carte_attribution.py ../$(POSITIONS) ../$(REF_JSON) ../$(LIV)

$(INVENTAIRE): $(REF_JSON) $(POSITIONS) $(NOTES) $(APP)/generer_inventaire.py
	cd $(APP) && $(PY) generer_inventaire.py ../$(REF_JSON) ../$(POSITIONS) \
	  ../$(NOTES) ../$@

# --- vues internes ----------------------------------------------------------
# Non diffusables : la nomenclature interne y est visible. Elles servent à lire
# le référentiel et à repérer à l'œil, jamais à citer.
$(ARBRE): $(REF_JSON) $(APP)/generer_arbre.py $(APP)/controle_arithmetique.py
	cd $(APP) && $(PY) generer_arbre.py ../$(REF_JSON) ../$@

$(RELEVE): $(NOTES) $(APP)/generer_releve_notes.py
	cd $(APP) && $(PY) generer_releve_notes.py ../$(NOTES) ../$@

# Le relevé des protos : les chiffres des livrables archivés, confrontés au
# référentiel des faits. Il ne se refait que si les protos sont au dépôt ; sans
# eux, le relevé versé fait foi et la chaîne continue.
PROTOS := $(wildcard sources/*proto*.html) \
          $(wildcard sources/Input_gagnants_perdants*.html) \
          $(wildcard sources/Reserve_arguments*.html) \
          $(wildcard sources/note_reforme_budgetaire*.html)
ifneq ($(PROTOS),)
$(RELEVE_PROTOS): $(CHIFFRES) $(PROTOS) $(APP)/relever_protos.py \
                  $(APP)/sources_chiffres.py
	cd $(APP) && $(PY) relever_protos.py ../$(CHIFFRES) ../$@ \
	  $(addprefix ../,$(PROTOS))
endif

# L'index lui-même est un dérivé : sa table curée vit dans son générateur, et
# rien ne le rejouait — la règle manquait depuis toujours. Un artefact porté au
# dérivé et absent de la table disparaissait donc au premier rejeu, ce qu'A-364
# et A-381 ont constaté deux fois. La cible est explicite : l'index est aussi
# une entrée de presque tout le reste, et le refaire au milieu d'une chaîne
# ferait tourner la chaîne sur deux états.
.PHONY: reindex
reindex:
	cd $(APP) && $(PY) generer_index.py ../$(INDEX) ..

# La carte du projet : l'inventaire lisible de tout ce que le chantier porte.
# Le seul fichier que l'auteur ait à ouvrir pour savoir où on en est.
$(CARTE): $(INDEX) $(APP)/generer_carte.py
	cd $(APP) && $(PY) generer_carte.py ../$(INDEX) ../$@

# L'état de la machine à amendements : deux grilles, aucun chiffre saisi à la
# main. Tout ce qui se compte sort du banc d'épreuve ; ce qu'aucun lot ne porte
# reste vide. Il ne dépend d'aucune pièce jointe et se refait toujours.
$(ETAT_MACH): $(LOTS) $(APP)/etat_machine.py
	cd $(APP) && $(PY) etat_machine.py ../$(LOTS) ../$@

# --- contre-PLF : portes, rattachement, véhicules ---------------------------
# La grille des portes se relève en verbatim sur le texte de référence de la
# LOLF. Le module ne porte que des repères ; un repère qui ne se retrouve pas
# arrête la génération plutôt que de composer une phrase de loi.
#
# La pièce de référence est restaurable : sans elle, la grille versée fait foi
# et la chaîne continue plutôt que de rompre.
ifneq ($(wildcard $(LOLF_REF)),)
$(PORTES): $(LOLF_REF) $(APP)/portes_domaine.py
	cd $(APP) && $(PY) portes_domaine.py ../$(LOLF_REF) ../$@
endif

$(AXE_TRANSP): $(REF_JSON) $(APP)/axe_transparence.py
	cd $(APP) && $(PY) axe_transparence.py ../$(REF_JSON) ../$@

# La ventilation par véhicule se tire des lignes tracées. Sans le traçage —
# donc sans le classeur de calculs converti sous sources/plf/ — elle ne se
# refait pas, et la version versée fait foi.
ifneq ($(wildcard $(ECO_JSON)),)
$(VENTILATION): $(ECO_JSON) $(APP)/ventilation_vehicule.py
	cd $(APP) && $(PY) ventilation_vehicule.py ../$(ECO_JSON) ../$@
endif

# Les leviers d'État sur la dépense des collocs (A-239). Une dépense locale ne
# se vote pas en loi de finances, mais la ressource qui la finance et le
# cofinancement qui l'appelle y sont. Les montants se prennent au socle.
ifneq ($(wildcard $(ECO_JSON)),)
$(COLLOCS): $(SOCLE_BUD) $(ECO_JSON) $(APP)/leviers_collocs.py
	cd $(APP) && $(PY) leviers_collocs.py ../$(SOCLE_BUD) ../$(ECO_JSON) ../$@
endif

# Le dimensionnement du chantier des vecteurs (A-241) : compté sur le socle et
# le référentiel de doctrine, jamais estimé.
# REF_norme : une entrée par mesure, son véhicule et son vecteur (A-231, A-245).
# Les vecteurs relevés à la main vivent dans `vecteurs.py` et survivent à chaque
# régénération ; ceux que les annexes portent se dérivent et se rejouent.
$(NORME): $(SOCLE_BUD) $(REF_JSON) $(APP)/ref_norme.py $(APP)/vecteurs.py
	cd $(APP) && $(PY) ref_norme.py ../$(SOCLE_BUD) ../$(REF_JSON) ../$@

# L'état des vecteurs, en une page que l'auteur ouvre. Aucun texte de loi :
# uniquement des adresses et le lien Légifrance qui y mène.
$(ETAT_VECT) $(ETAT_CSV): $(NORME) $(SOCLE_BUD) \
              $(APP)/generer_etat_vecteurs.py \
              $(APP)/controle_norme.py $(APP)/vecteurs.py
	cd $(APP) && $(PY) generer_etat_vecteurs.py ../$(NORME) ../$(SOCLE_BUD) \
	  ../$(ETAT_VECT) ../$(ETAT_CSV)

$(VECTEURS): $(SOCLE_BUD) $(REF_JSON) $(NORME) $(APP)/chantier_vecteurs.py
	cd $(APP) && $(PY) chantier_vecteurs.py ../$(SOCLE_BUD) ../$(REF_JSON) \
	  ../$@ ../$(NORME)

# --- socle budgétaire ------------------------------------------------------
# Les classeurs sectoriels sont des pièces jointes du projet : ils ne viennent
# pas au dépôt et se lisent là où ils sont. Le socle ne se refait donc que si
# on les a convertis dans l'atelier, sous sources/plf/ :
#
#   soffice --headless --convert-to xlsx --outdir sources/plf <fichier>.xls
#
# Il n'est pas versé au coffre : il se régénère à l'identique depuis les pièces
# jointes, comme le référentiel des faits (A-71).
SOCLE_BUD := $(REF)/socle_budgetaire.json
PLF_TAXES := $(wildcard sources/plf/*axes*ffectees*.xlsx)
PLF_OPS   := $(wildcard sources/plf/*ETP*.xlsx)
PLF_DF    := $(wildcard sources/plf/*epenses*iscales*.xlsx)
PLF_BG    := $(wildcard sources/plf/*Depenses_BG*.xlsx)
PLF_CALC  := $(wildcard sources/plf/Synthese_Calculs*.xlsx)
ifneq ($(PLF_TAXES)$(PLF_OPS)$(PLF_DF)$(PLF_BG)$(PLF_CALC),)
$(SOCLE_BUD): $(APP)/socle_budgetaire.py $(PLF_TAXES) $(PLF_OPS) $(PLF_DF) \
              $(PLF_BG) $(PLF_CALC)
	cd $(APP) && $(PY) socle_budgetaire.py ../$@ \
	  $(if $(PLF_TAXES),--taxes ../$(PLF_TAXES)) \
	  $(if $(PLF_OPS),--operateurs ../$(PLF_OPS)) \
	  $(if $(PLF_DF),--depenses-fiscales ../$(PLF_DF)) \
	  $(if $(PLF_BG),--depenses-bg ../$(PLF_BG)) \
	  $(if $(PLF_CALC),--calculs ../$(PLF_CALC))
endif

# L'appariement des opérateurs et le classeur de synthèse se tirent du socle.
# Sans socle au dépôt, ils ne se refont pas : les classeurs sectoriels sont des
# pièces jointes, et leur conversion n'est pas garantie. La garde porte sur le
# socle **ou** sur ses classeurs : un socle restauré suffit à rejouer ce qui en
# descend, même sans les pièces.
# Les règles restent écrites en toutes circonstances — elles se demandent une
# par une, et le balayage des générateurs veut pouvoir les jouer pour dire
# quel intrant leur manque. Ce qui est gardé, c'est leur entrée dans `tout` :
# une chaîne complète ne s'arrête pas parce qu'une pièce jointe n'est pas là.
BUD_DISPO := $(wildcard $(SOCLE_BUD))$(PLF_TAXES)$(PLF_OPS)$(PLF_DF)$(PLF_BG)$(PLF_CALC)
ifneq ($(BUD_DISPO),)
BUD_DERIVES += $(APPARIEMENT) $(RECON_TXT) $(ECO_TXT) $(SYNTHESE_BUD) \
               $(VENTILATION) $(COLLOCS) $(NORME) $(ETAT_VECT) $(ETAT_CSV) \
               $(VECTEURS)
endif
tout: $(BUD_DERIVES)

$(APPARIEMENT): $(SOCLE_BUD) $(APP)/apparier_operateurs.py
	cd $(APP) && $(PY) apparier_operateurs.py ../$(SOCLE_BUD) ../$@

$(ECO_TXT) $(ECO_JSON): $(SOCLE_BUD) $(APP)/tracer_economies.py
	cd $(APP) && $(PY) tracer_economies.py ../$(SOCLE_BUD) \
	  ../$(ECO_JSON) ../$@

$(RECON_TXT) $(RECON_OP): $(SOCLE_BUD) $(APP)/reconcilier_operateurs.py \
              $(APP)/apparier_operateurs.py $(APP)/tracer_economies.py
	cd $(APP) && $(PY) reconcilier_operateurs.py ../$(SOCLE_BUD) \
	  ../$(RECON_OP) ../$@

$(SYNTHESE_BUD): $(SOCLE_BUD) $(CHIFFRES) $(RECON_TXT) $(ECO_TXT) \
                 $(APP)/generer_classeur_synthese.py \
                 $(APP)/hypotheses_doctrine.py $(APP)/sources_chiffres.py
	cd $(APP) && $(PY) generer_classeur_synthese.py ../$(SOCLE_BUD) \
	  ../$(CHIFFRES) ../$@ ../$(RECON_OP) ../$(ECO_JSON)

# --- socle du texte déposé : PLF et PLFSS -----------------------------------
# **Un extracteur, deux profils de pièce** (A-273). Le troisième argument de
# `socle_plf_texte.py` est le profil. Sans lui, le profil `plf` s'applique, ses
# repères ne se retrouvent pas sur la pièce du PLFSS et la génération s'arrête :
# c'est le comportement voulu, non une panne.
#
# **Les pièces ne sont pas au dépôt d'une session à l'autre.** Ni le PLF ni le
# PLFSS ne vont au coffre — documents publics, retéléchargeables à l'identique
# (A-235) — et le verbatim n'entre que par pièce jointe (A-234). Elles se
# déposent sous `sources/plf/` et `sources/plfss/`, et ces règles sont donc
# conditionnelles à leur présence, comme les classeurs sectoriels.
#
# Ni les deux socles ni les deux JSON d'ouverts ne se versent au coffre : ils se
# régénèrent à l'octet depuis la pièce et depuis un script qui, lui, y va
# (A-71 lu avec A-235). Les deux TSV s'y versent, parce que ce sont les seules
# formes de cette matière qui se lisent sans outil (A-16).
SOCLE_PLF         := $(REF)/socle_plf_texte.json
OUVERTS_PLF       := $(REF)/articles_ouverts_plf.json
OUVERTS_PLF_TSV   := $(REF)/articles_ouverts_plf.tsv
RELEVE_PLF        := $(LIV)/articles_ouverts_plf.txt
SOCLE_PLFSS       := $(REF)/socle_plfss_texte.json
OUVERTS_PLFSS     := $(REF)/articles_ouverts_plfss.json
OUVERTS_PLFSS_TSV := $(REF)/articles_ouverts_plfss.tsv
RELEVE_PLFSS      := $(LIV)/articles_ouverts_plfss.txt
REDACTION_PLF     := $(REF)/redaction_plf.json
REDACTION_PLFSS   := $(REF)/redaction_plfss.json
# LOTS est déjà défini plus haut, à la même valeur : la seconde affectation a
# été retirée le 20260907. Un nom pour une chose, même quand les deux valeurs
# coïncident — sinon rien ne dit laquelle vaut quand l'une des deux change.
PLF_PDF           := $(wildcard sources/plf/PLF2026_1906.pdf)
PLFSS_PDF         := $(wildcard sources/plfss/PLFSS2026_1907.pdf)
SOCLES_TEXTE      :=

ifneq ($(PLF_PDF),)
SOCLES_TEXTE += $(OUVERTS_PLF_TSV)
$(SOCLE_PLF): $(APP)/socle_plf_texte.py $(APP)/vecteurs.py $(PLF_PDF)
	cd $(APP) && $(PY) socle_plf_texte.py ../$(PLF_PDF) ../$(SOCLE_PLF) plf

# Trois sorties d'un seul geste, et elles se déclarent toutes les trois : une
# sortie qu'aucune cible ne nomme ne se rejoue jamais par `make`, et le balayage
# des générateurs la comptait à juste titre sans règle.
$(OUVERTS_PLF_TSV) $(OUVERTS_PLF) $(RELEVE_PLF): \
                    $(APP)/articles_ouverts_plf.py $(APP)/ref_norme.py \
                    $(SOCLE_PLF)
	cd $(APP) && $(PY) articles_ouverts_plf.py ../$(SOCLE_PLF) \
	  ../$(OUVERTS_PLF) ../$(RELEVE_PLF) ../$(OUVERTS_PLF_TSV)

SOCLES_TEXTE += $(REDACTION_PLF)
$(REDACTION_PLF): $(APP)/redaction_deposee.py $(SOCLE_PLF)
	cd $(APP) && $(PY) redaction_deposee.py ../$(SOCLE_PLF) ../$@
endif

ifneq ($(PLFSS_PDF),)
SOCLES_TEXTE += $(OUVERTS_PLFSS_TSV)
$(SOCLE_PLFSS): $(APP)/socle_plf_texte.py $(APP)/vecteurs.py $(PLFSS_PDF)
	cd $(APP) && $(PY) socle_plf_texte.py ../$(PLFSS_PDF) \
	  ../$(SOCLE_PLFSS) plfss

$(OUVERTS_PLFSS_TSV) $(OUVERTS_PLFSS) $(RELEVE_PLFSS): \
                      $(APP)/articles_ouverts_plf.py $(APP)/ref_norme.py \
                      $(SOCLE_PLFSS)
	cd $(APP) && $(PY) articles_ouverts_plf.py ../$(SOCLE_PLFSS) \
	  ../$(OUVERTS_PLFSS) ../$(RELEVE_PLFSS) ../$(OUVERTS_PLFSS_TSV)

SOCLES_TEXTE += $(REDACTION_PLFSS)
$(REDACTION_PLFSS): $(APP)/redaction_deposee.py $(SOCLE_PLFSS)
	cd $(APP) && $(PY) redaction_deposee.py ../$(SOCLE_PLFSS) ../$@
endif

# --- le partage calibrage / épreuve -----------------------------------------
# La règle de sélection du banc de la rédaction (A-330). Elle joue sur la part
# **versée** du socle et non sur le socle : le banc doit être atteignable depuis
# le coffre seul, sinon ce n'est pas un banc. `lots_epreuve.json` est écrit à la
# main pour tout le reste, et cette cible n'en réécrit que son lot — elle
# s'appelle donc explicitement, jamais par `tout` : une régénération
# silencieuse du banc au milieu d'un `make` serait une faute.
.PHONY: partage
partage: $(APP)/partage_calibrage.py $(REDACTION_PLF) $(LOTS)
	cd $(APP) && $(PY) partage_calibrage.py ../$(REDACTION_PLF) ../$(LOTS)

.PHONY: partage-releve
partage-releve: $(APP)/partage_calibrage.py $(REDACTION_PLF)
	cd $(APP) && $(PY) partage_calibrage.py ../$(REDACTION_PLF) \
	  ../$(LOTS) --releve

# --- les portes ouvertes ----------------------------------------------------
# Quelle mesure du corpus tombe sur un article que le texte déposé ouvre déjà
# (A-293). Les deux tables sont au coffre : la règle n'attend pas les pièces, et
# elle joue dès que `REF_norme` existe. Dérivé, non versé — il se régénère.
# `PORTES` désignait déjà `livrables/portes_domaine.md`, plus haut. La
# réaffectation faisait qu'un même nom valait deux artefacts selon l'endroit du
# fichier où on le lisait, et qu'une des deux règles pouvait perdre sa cible au
# premier déplacement de ligne. Renommé le 20260907.
PORTES_OUV := $(REF)/portes_ouvertes.tsv

$(PORTES_OUV): $(APP)/portes_ouvertes.py $(NORME) \
           $(OUVERTS_PLF_TSV) $(OUVERTS_PLFSS_TSV)
	cd $(APP) && $(PY) portes_ouvertes.py ../$(NORME) ../$@ \
	  ../$(OUVERTS_PLF_TSV) ../$(OUVERTS_PLFSS_TSV)

# Les prérequis s'ajoutent à `tout` ici, et non à sa déclaration : les deux
# règles n'existent que si leur pièce est jointe.
tout: $(SOCLES_TEXTE)
# `portes_ouvertes.py` est aux manquants depuis le 20260903 : il est appelé et
# il n'existe pas. Tant qu'il n'est pas réécrit, l'inscrire dans `tout` fait
# tomber la chaîne entière sur un module absent — et cela cachait tout ce qui
# vient après. La garde le dit sans l'effacer ; le manquant reste déclaré.
ifneq ($(wildcard $(APP)/portes_ouvertes.py),)
tout: $(PORTES_OUV)
endif


# ---------------------------------------------------------------------------
# LA LECTURE EN CREUX, LES FOURCHETTES, ET LE DOMAINE DE LA LOI SÉCU
#
# Trois produits du 20260902. Les deux premiers se calculent sur le socle du
# texte déposé ; le troisième découpe le texte en vigueur à l'octet.
#
# **Le dépôt de droit n'est pas au corpus** — cinq pièces qui vivent à leur
# dépôt (`reference/depot_droit.md`). Il se clone par le fil, hors de l'atelier
# de préférence : cloné dedans, ses quinze fichiers font sortir `I2`, faute
# d'être ni au `.gitignore` ni aux `IGNORES` de `controle_index.py`. Les règles
# qui en dépendent sont donc conditionnelles à sa présence, comme les PDF et
# les classeurs.
DROIT             ?= ../droit
PLAGES            := $(REF)/plages_articles.json
PLAGES_TXT        := $(LIV)/plages_articles.txt
CREUX_PLF         := $(REF)/lecture_en_creux_plf.json
CREUX_PLF_TXT     := $(LIV)/lecture_en_creux_plf.txt
CREUX_PLFSS       := $(REF)/lecture_en_creux_plfss.json
CREUX_PLFSS_TXT   := $(LIV)/lecture_en_creux_plfss.txt
PORTES_LFSS       := $(LIV)/portes_domaine_lfss.md
# `DROIT` est le chemin du dépôt **tel que vu depuis `appareil/`**, puisque
# les recettes s'y placent. Le test de présence accepte les deux formes, le
# chemin absolu comme le relatif.
DROIT_PRESENT     := $(wildcard $(APP)/$(DROIT)/droit.py $(DROIT)/droit.py)

# La lecture en creux se calcule sur le socle seul. Sa cinquième colonne — le
# texte en vigueur en regard de la disposition — demande le dépôt ; sans lui
# elle se déclare non jouée, et la cible tourne quand même.
$(CREUX_PLF) $(CREUX_PLF_TXT): $(APP)/lecture_en_creux.py $(SOCLE_PLF)
	cd $(APP) && $(PY) lecture_en_creux.py ../$(SOCLE_PLF) \
	  ../$(CREUX_PLF) ../$(CREUX_PLF_TXT) $(DROIT)

$(CREUX_PLFSS) $(CREUX_PLFSS_TXT): $(APP)/lecture_en_creux.py $(SOCLE_PLFSS)
	cd $(APP) && $(PY) lecture_en_creux.py ../$(SOCLE_PLFSS) \
	  ../$(CREUX_PLFSS) ../$(CREUX_PLFSS_TXT) $(DROIT)

ifneq ($(DROIT_PRESENT),)
# Les fourchettes ne se déplient que sur le code, à sa source. Sans le dépôt,
# la plage reste comptée sur sa borne basse et le manque est déjà déclaré à la
# table des articles ouverts, colonne `fourchette`.
$(PLAGES) $(PLAGES_TXT): $(APP)/plages_articles.py $(OUVERTS_PLF_TSV) \
                         $(OUVERTS_PLFSS_TSV)
	cd $(APP) && $(PY) plages_articles.py $(DROIT) ../$(PLAGES) \
	  ../$(PLAGES_TXT) ../$(OUVERTS_PLF_TSV) ../$(OUVERTS_PLFSS_TSV)

$(PORTES_LFSS): $(APP)/portes_domaine_lfss.py
	cd $(APP) && $(PY) portes_domaine_lfss.py $(DROIT) ../$(PORTES_LFSS)

tout: $(PLAGES_TXT) $(PORTES_LFSS)
endif

ifneq ($(PLF_PDF),)
tout: $(CREUX_PLF_TXT)
endif
ifneq ($(PLFSS_PDF),)
tout: $(CREUX_PLFSS_TXT)
endif


# --- contrôles --------------------------------------------------------------
# Ils ne produisent rien. Ils disent si ce qui est produit tient.
controle:
	@$(PY) $(APP)/controle_lexique.py livrables site || true
	@cd $(APP) && $(PY) controle_structurel.py ../$(REF_JSON)
	@cd $(APP) && $(PY) controle_arithmetique.py ../$(REF_JSON)
	@cd $(APP) && $(PY) controle_notes.py ../$(NOTES) ../$(REF_JSON) ../$(POSITIONS) || true
	@if [ -f $(CHIFFRES) ]; then cd $(APP) && $(PY) controle_chiffres.py \
	  ../$(CHIFFRES); \
	 else echo "REF_chiffres absent du dépôt — non contrôlé"; fi
	@if [ -f $(MAN)/manuscrit.html ]; then cd $(APP) && \
	  $(PY) controle_hypotheses.py ../$(MAN)/manuscrit.html \
	  ../$(NOTES) ../$(REF_JSON); \
	 else echo "manuscrit absent du dépôt — hypothèses non contrôlées"; fi
	@if [ -f $(MAN)/manuscrit.html ]; then cd $(APP) && \
	  $(PY) controle_apports.py ../$(POSITIONS) ../$(REF_JSON) \
	  ../$(MAN)/manuscrit.html; \
	 else echo "manuscrit absent du dépôt — apports non contrôlés"; fi
	@if [ -f $(LIVRE) ]; then $(PY) $(APP)/texte_livre.py $(EPREUVE) \
	  /dev/null >/dev/null 2>&1 && echo "texte du livre : six contrôles joués" \
	  || echo "texte du livre : épreuve non jointe — non rejoué"; \
	 else echo "texte du livre absent du dépôt — non contrôlé"; fi
	@if [ -f $(SOCLE_BUD) ]; then cd $(APP) && $(PY) controle_socle.py \
	  ../$(SOCLE_BUD); \
	 else echo "socle budgétaire absent du dépôt — non contrôlé"; fi
	@if [ -f $(NORME) ]; then cd $(APP) && $(PY) controle_norme.py \
	  ../$(NORME) ../$(SOCLE_BUD) || true; \
	 else echo "REF_norme absent du dépôt — non contrôlé"; fi
	@if [ -f $(SOCLE_PLF) ] && [ -n "$(PLF_PDF)" ]; then cd $(APP) && \
	  $(PY) controle_socle_plf.py ../$(SOCLE_PLF) ../$(PLF_PDF) \
	  ../$(OUVERTS_PLF); \
	 else echo "socle du texte du PLF : pièce non jointe — non contrôlé"; fi
	@if [ -f $(SOCLE_PLFSS) ] && [ -n "$(PLFSS_PDF)" ]; then cd $(APP) && \
	  $(PY) controle_socle_plf.py ../$(SOCLE_PLFSS) ../$(PLFSS_PDF) \
	  ../$(OUVERTS_PLFSS); \
	 else echo "socle du texte du PLFSS : pièce non jointe — non contrôlé"; fi
	@if [ -f $(APP)/scinde/cles_eval.json ]; then cd $(APP) && \
	  $(PY) controle_cles_gl.py ../methode/banc_gl.md \
	  ../methode/prompt_fil_joueur_banc_gl.md; \
	 else echo "clé du banc des liasses absente — non contrôlée"; fi
	@$(PY) $(APP)/controle_index.py $(INDEX) .
	@$(MAKE) --no-print-directory G

# Le balayage des générateurs joue chaque producteur du corpus et compte ceux
# qui ne tournent plus. Il **écrit au dépôt** — il régénère pour de vrai —, donc
# il ne se glisse pas dans `controle`, qui ne produit rien par définition. Il se
# demande, et il est demandé à la clôture d'un fil.
.PHONY: generateurs
generateurs:
	@$(PY) $(APP)/controle_generateurs.py $(INDEX) .

# Le contrôle `G` de généralisation : une skill ne nomme ni déposant, ni projet,
# ni corpus interne, et elle dit ce qu'elle rend quand la base documentaire
# manque. Il porte sur des fichiers de skill, dont le point de vérité est la
# skill enregistrée au compte : au dépôt, il n'y en a que le temps d'un fil qui
# en écrit une. Sans fichier, il le dit et la chaîne continue.
#
# Il bloque sur ce qui identifie — déposant, projet, manuscrit, coffre,
# référentiel, nomenclature — et signale le reste. Une règle qu'on tient à l'œil
# se perd, et elle s'est perdue quatorze fois.
# **Le point de vérité d'une skill est la skill enregistrée au compte, pas une
# copie de travail** (A-269). Ne balayer que le dépôt rendait donc `G` aveugle
# par construction : sans fichier posé à la main, il ne contrôlait rien et le
# disait comme un succès. Il va désormais chercher les skills là où elles vivent,
# les deux racines possibles selon la façade, en plus du dépôt.
SKILLS_RACINES ?= $(HOME)/.claude/skills /root/.claude/skills
SKILLS := $(wildcard livrables/skills/*/SKILL.md) $(wildcard livrables/skills/*.md) \
          $(foreach r,$(SKILLS_RACINES),$(wildcard $(r)/*/SKILL.md)) \
          $(foreach r,$(SKILLS_RACINES),$(wildcard $(r)/synced/*/*/SKILL.md))

.PHONY: G
G:
	@$(PY) $(APP)/controle_generalisation.py $(SKILLS)

# Le contrôle du coffre seul, joué en ouverture de session : il dit si
# l'arborescence, l'index et les noms canoniques concordent.
.PHONY: index
index:
	@$(PY) $(APP)/controle_index.py $(INDEX) .

# Publication du site sur son dépôt distant, d'où Vercel déploie.
#
# Le dépôt de publication ne reçoit **que les pages rendues** : ni doctrine, ni
# référentiel, ni appareil, ni méthode. C'est une publication, pas un atelier —
# même relation que le projet ouvert du contre-PLF au corpus (A-134). Rien n'en
# revient.
#
# Il n'y a rien à configurer sur Vercel : un dépôt de fichiers statiques à la
# racine se déploie tel quel, sans commande de construction. Un chiffre qui
# change se corrige au référentiel, `make publier` régénère et pousse, Vercel
# redéploie. Personne ne touche au HTML.
# PUBLICATION       le clone local du dépôt distant
# PUBLICATION_SOUS  le sous-dossier de ce dépôt que le site occupe. Il est
#                   remplacé en entier à chaque publication ; le reste du dépôt
#                   n'est jamais touché. Vide pour publier à la racine.
PUBLICATION      ?= publication
PUBLICATION_SOUS ?= site
CIBLE_PUB = $(PUBLICATION)$(if $(PUBLICATION_SOUS),/$(PUBLICATION_SOUS))

.PHONY: publier
publier: $(SITE)
	@test -d $(PUBLICATION)/.git || { \
	  echo "Aucun dépôt de publication dans $(PUBLICATION)/ — le cloner d'abord."; \
	  exit 1; }
	@test -n "$(PUBLICATION_SOUS)" || { \
	  echo "PUBLICATION_SOUS vide : refus d'effacer la racine d'un dépôt existant."; \
	  exit 1; }
	@rm -rf $(CIBLE_PUB)
	@mkdir -p $(CIBLE_PUB)
	@cp -R $(SITE_DIR)/. $(CIBLE_PUB)/
	@rm -f $(CIBLE_PUB)/vercel.json.modele
	@cp $(SITE_DIR)/vercel.json.modele $(PUBLICATION)/vercel.json
	@cd $(PUBLICATION) && git add -A -- $(PUBLICATION_SOUS) vercel.json && \
	  if git diff --cached --quiet; then echo "rien à publier"; else \
	    git commit -q -m "Site régénéré depuis le référentiel" && \
	    git push -q origin HEAD && \
	    echo "poussé — Vercel déploie"; fi

# Le versement : relever les empreintes, puis dire ce qui est dû au dépôt.
#
# **La cible ne plie plus rien.** Elle appelait `coffre.py plier`, qui repliait
# la couche technique dans une archive unique du coffre. Cette archive a été
# versée au dépôt et supprimée du coffre le 20260909, prouvée 80 sur 80 à
# l'octet (A-395) : il n'y a plus d'archive à replier, et un pliage qui ne se
# verse plus fabriquerait une pièce que personne ne porte.
#
# Ce qui reste, et qui est l'essentiel : les empreintes de tout ce que le corpus
# porte de durable, sur les deux voies. Elles sont la seule référence à quoi
# comparer ce qui reviendra — le coffre rend ses documents en texte, et une
# restauration qui repasse par le modèle normalise sans le dire.
#
# Ce qui s'y ajoute : la dette au dépôt. **L'écriture au dépôt est fermée depuis
# Cowork** (A-393), donc une pièce d'appareil corrigée ici ne peut pas être
# poussée par le fil qui la corrige. Elle se déclare, et elle se perd si
# personne ne la porte. La comparaison se fait contre le clone, qui est ce que
# la session suivante recevra ; sans clone, la cible le dit et continue.
#
# **Le clone est passé au relevé des empreintes, et ce n'est pas une commodité**
# (20260910). Une empreinte de voie `depot` se relève **au clone**, qui est ce
# que la session suivante recevra, et jamais au dépôt courant : un fil Cowork
# qui corrige une pièce de l'appareil ne peut pas la pousser, et relever son
# empreinte ici écrirait au coffre la référence d'un fichier qui ne vit que dans
# un conteneur éphémère. Sans clone, ces empreintes ne se touchent pas.
.PHONY: coffre
coffre: $(INDEX)
ifneq ($(DROIT_PRESENT),)
	@cd $(APP) && $(PY) empreintes.py ../$(INDEX) .. $(DROIT)
	@cd $(APP) && $(PY) coffre.py dette ../$(INDEX) .. $(DROIT)
else
	@$(PY) $(APP)/empreintes.py $(INDEX) .
	@echo "Dette au dépôt non mesurée : aucun clone en $(DROIT)."
	@echo "    git clone https://github.com/resolution-ib-dev/Resolution-2027 droit"
endif

# Contrôle de la restauration, joué en ouverture juste après le dépliage, avant
# toute lecture et toute génération. Une divergence est un faux au dépôt.
.PHONY: restauration
restauration:
	@cd $(APP) && $(PY) controle_restauration.py ../$(INDEX) ../$(EMPREINTES) .. $(DROIT)

etat:
	@cd $(APP) && $(PY) exporter_donnees.py ../$(REF_JSON) ../$(POSITIONS) \
	  ../$(NOTES) /dev/null | tail -1

propre:
	rm -f $(DONNEES) $(EXTRAIT) $(INTERFACE) $(INVENTAIRE) $(ARBRE) $(RELEVE) \
	      $(CARTE) $(RELEVE_PROTOS) $(GALERIE) $(ATTRIBUTION) \
	      $(PORTES) $(AXE_TRANSP) $(VENTILATION) $(COLLOCS) $(VECTEURS) \
	      $(ETAT_VECT) $(ETAT_CSV) $(RELEVE_PLF) $(RELEVE_PLFSS)
	rm -rf $(SITE_DIR)

# Le référentiel des faits ne s'efface pas avec les dérivés : il porte le
# sourçage écrit à la main, et `make propre` ne détruit pas ce travail.
