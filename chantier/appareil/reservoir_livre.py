#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Réservoir d'arguments tiré du livre, indexé par mesure et par bloc.

Rend `livrables/reservoir_arguments_livre.md`. Pour chaque mesure de
l'arborescence financière : l'argument de fond, pris au livre ; et la
citation opposable, quand une note de fin la porte.

RÈGLES, et elles sont toutes mécaniques
---------------------------------------
1. Aucun mot du livre n'est retapé. Un passage se désigne par un folio de
   début, un folio de fin et deux ancres : le texte entre les deux, ancres
   comprises, est découpé dans le texte coulant de `texte_livre.py couler()`.
   Une ancre absente ou ambiguë arrête la génération.
2. Les appels de note sont relevés une fois, sur tout le corps, dans l'ordre
   de numérotation : l'appel n se cherche après l'appel n-1. Dans un passage,
   l'appel, collé au mot dans la composition, se rend « [n] ».
3. Une note citée est celle dont l'appel tombe dans un passage retenu, plus
   celles qu'une mesure rattache expressément (champ `notes`). Le texte de la
   note est rendu entier, coulé, coupes recollées par leur verdict. Une
   adresse web coupée en fin de ligne se recolle sans espace, et son trait
   d'union se garde.
4. Une note qui se déclare calcul propre (« Calcul(s) Résolution ») est
   marquée telle : elle est opposable comme décompte déclaré, non comme
   source tierce.
5. Le choix des passages est le seul jugement du fichier. Il vit dans la
   table `RESERVOIR` ci-dessous, et nulle part ailleurs.

Usage : python3 appareil/reservoir_livre.py [sortie]
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent
sys.path.insert(0, str(ICI))
from texte_livre import couler  # noqa: E402

LIVRE = RACINE / "livre" / "texte_livre.json"
ARBO = RACINE / "livrables" / "arborescence_mesures_20260928.md"
SORTIE = RACINE / "livrables" / "reservoir_arguments_livre.md"

CORPS = (7, 143)        # prologue, parties I à III, postface
NOTES = (145, 159)
DERNIERE_NOTE = 141

# --- la table : mesure -> passages (folio début, folio fin, ancre début, ancre fin)
RESERVOIR: dict[str, dict] = {
    "M-001": {"passages": [
        (66, 66, "Trois critères permettent", "cela n’exige pas notre impôt."),
        (68, 68, "En échange de nos impôts, l’État doit", "assurer."),
        (69, 69, "Nous proposons en conséquence", "ne constitue pas une mission publique."),
        (41, 41, "Seulement", "régalienne par excellence46."),
    ]},
    "M-002": {"passages": [
        (84, 85, "Payer pour l’Agence nationale", "peut devenir une dépense publique pérenne."),
        (43, 43, "On recense 434 agences", "Stop ou encore ?"),
        (44, 44, "Derrière une mission facultative", "se rendre incontournable53."),
        (83, 83, "Imaginez : le Conseil national du bruit", "peut être interrompu sans drame."),
    ]},
    "M-003": {"passages": [
        (85, 85, "Ce que l’État doit faire, il doit l’effectuer", "par une chaîne de délégations."),
        (85, 85, "Les fonctions régaliennes, progressivement", "au sein des ministères."),
    ]},
    "M-004": {"passages": [
        (85, 86, "Les établissements publics", "instituts de recherche."),
    ]},
    "M-007": {"passages": [
        (78, 79, "Un appareil public concentré", "mieux rémunérer les agents indispensables."),
        (43, 44, "La France compte 5,8 millions", "sans jamais passer par France Travail52."),
        (135, 135, "La France compte aujourd’hui 62 %", "période de prospérité inédite de l’histoire de France."),
    ]},
    "M-008": {"passages": [
        (79, 79, "Les agents dont les postes seront supprimés", "du sens dans leur carrière."),
    ]},
    "M-009": {"passages": [
        (80, 80, "Les armées recrutent déjà", "plus flexible que le concours de fonctionnaire."),
        (80, 81, "Honorons la fonction publique", "d’un État pleinement efficace."),
    ]},
    "M-010": {"passages": [
        (73, 74, "Faisons de la commune", "n’est impératif aux citoyens."),
        (71, 72, "L’excès d’État se démultiplie", "de la cohésion sociale91 »."),
        (72, 72, "Le vote des Français parle", "élections régionales et départementales92."),
        (46, 46, "Perdus dans le millefeuille", "élections régionales et départementales57."),
    ]},
    "M-011": {"passages": [
        (74, 74, "Les communes pourront s’associer", "sans perdre en autonomie."),
        (73, 73, "Les associations forcées", "que les communes les plus grandes93."),
    ]},
    "M-012": {"passages": [
        (74, 74, "La taxe foncière entièrement versée", "inciteront à une gestion efficace."),
    ]},
    "M-013": {"passages": [
        (74, 75, "Si une commune mal gérée", "la continuité des missions indispensables."),
    ]},
    "M-014": {"passages": [
        (75, 75, "Les préfectures resteront", "être assurées par l’État."),
    ], "notes": [88]},
    "M-015": {"passages": [
        (75, 75, "Aujourd’hui, le soutien au handicap", "des Ardennes aux Cévennes en passant par le Berry."),
    ]},
    "M-016": {"passages": [
        (86, 86, "Supprimons toutes les subventions.", "dès lors qu’ils disposeront plus librement de leur temps et de leur argent."),
        (40, 40, "Les subventions aux associations transforment", "devient un bon investissement."),
        (35, 35, "L’État distribue à grand bruit", "Une subvention ne crée pas de richesse."),
    ], "notes": [72]},
    "M-018": {"passages": [
        (86, 86, "A fortiori pour l’aide au développement", "aucun service en échange de l’impôt."),
    ]},
    "M-017": {"passages": [
        (39, 40, "Les aides aux entreprises alimentent", "coûte 66 millions d’euros par an36."),
        (40, 40, "La signature d’un adjoint au maire", "un privilège que distribue le pouvoir."),
        (86, 87, "La meilleure aide à l’innovation", "Son rôle n’est pas d’expérimenter."),
    ]},
    "M-031": {"passages": [
        (97, 98, "La suppression des taxes et impôts de production", "laissant le champ libre à l’investissement privé."),
        (28, 29, "Une entreprise ne supporte pas l’impôt", "finit par peser sur les citoyens ordinaires."),
        (97, 97, "À la place des charges sur les entreprises", "gardons un impôt simple sur les sociétés."),
    ]},
    "M-063": {"passages": [
        (96, 96, "La simplification volontaire est à notre portée", "prévaut sur la traduction ou le commentaire."),
        (95, 95, "Nos 521 pages de Code de la route", "peut se résumer en si peu de mots."),
        (48, 48, "Le volume du droit a doublé", "de 25 à 49 millions de mots60."),
    ]},
    "M-064": {"passages": [
        (93, 94, "Dans un État de droit, la loi doit rester", "Cette discipline s’impose au législateur responsable."),
        (51, 51, "Par faiblesse ou par calcul", "sans bien peser les conséquences68."),
    ]},
    "M-065": {"passages": [
        (94, 94, "De même, les régimes d’autorisation", "condamner ceux qui doivent l’être."),
        (48, 48, "L’excès de règles engendre l’injustice.", "les codes sont parfois contradictoires61."),
    ]},
    "M-066": {"passages": [
        (46, 46, "L’exemplarité devrait être", "détournement d’argent privé."),
        (40, 40, "Certaines de ces faveurs se paient", "loin des régimes exemplaires39."),
    ]},
    "M-022": {"passages": [
        (50, 50, "Nous subissons enfin des « quasi-taxes »", "sur sa facture énergétique64."),
    ]},
    "M-067": {"passages": [
        (87, 87, "Laissons aux salariés des vrais euros", "sous conditions administratives."),
        (35, 35, "Les titres-restaurant ou chèques-vacances", "d’en disposer librement28."),
        (92, 92, "Des obligations sédimentées", "ne répondent plus à leurs priorités."),
    ]},
    "M-068": {"passages": [
        (38, 39, "Chaque réglementation est un impôt.", "l’accès aux centres-villes."),
    ]},
    "M-026": {"passages": [
        (50, 50, "Les niches fiscales sont des subventions masquées.", "approuvés par les citoyens ?"),
        (86, 86, "Abolissons les faveurs fiscales.", "supprimons les deux."),
        (97, 97, "À la place des charges sur les entreprises", "gardons un impôt simple sur les sociétés."),
        (140, 140, "Par exemple, pour les 486 niches fiscales", "plus de deux mois."),
    ]},
    "M-025": {"passages": [
        (89, 89, "Rendons ces économies aux travailleurs", "sans augmenter ni peser sur les marges des entreprises."),
        (26, 26, "Pour une heure de travail", "Nous travaillons d’abord pour l’État."),
        (27, 27, "Le travail est plus lourdement taxé", "le prix de son mérite17."),
    ]},
    "M-047": {"passages": [
        (105, 106, "Finançons les retraites d’abord", "autres droits de propriété113."),
        (108, 109, "Cette restitution à chaque Français", "niches fiscales pour tous121."),
        (12, 12, "Côté patrimoine, 600 milliards", "20 000 euros de capital en trois ans."),
    ]},
    "M-048": {"passages": [
        (108, 108, "Ces actifs publics seront réunis", "apparaîtra sur votre compte épargne."),
        (142, 142, "Les actifs publics seront réunis au sein de fonds de défaisance", "maximiser la valeur réalisée pour les Français."),
    ]},
    "M-049": {"passages": [
        (107, 107, "L’État gère mal notre argent", "son rendement aurait dû alléger nos impôts."),
        (108, 108, "Notre souveraineté sera renforcée", "indépendante du secteur contrôlé."),
    ]},
    "M-050": {"passages": [
        (108, 108, "Restituons à tous les Français en trois ans", "sur leur compte épargne119."),
        (57, 57, "Le logement social n’est « social » que de nom", "pas assez pour accueillir tous les candidats."),
        (57, 58, "Alors qu’un locataire du parc social", "25 % de leur revenu contre 15 %74."),
        (58, 58, "En résumé, tous paient", "attribué exclusivement à quelques-uns."),
    ]},
    "M-051": {"passages": [
        (109, 109, "Aucun « or de la République »", "aux Français sur leurs comptes épargne."),
        (106, 106, "L’État immobilise 97 millions", "la crise de l’immobilier."),
        (107, 107, "Ce qui coûte au contribuable", "un appel aux dons pour sa rénovation."),
    ]},
    "M-028": {"passages": [
        (96, 97, "Supprimons toutes les taxes en trop", "de 5 %106."),
        (49, 49, "Il n’existe pas même de recensement", "la fraude devient rentable."),
        (97, 97, "Plus important, cette simplification", "plus traquer les abus est facile."),
    ]},
    "M-029": {"passages": [
        (97, 97, "À la place des taxes et taux réduits", "Taxons de la même façon un coiffeur et un hôtelier."),
        (49, 49, "Regardons ce que nous payons", "Ils sont certainement peu redistributifs."),
    ]},
    "M-030": {"passages": [
        (49, 50, "Nous payons ensuite des taxes spécifiques", "taxé jusqu’à 60 %."),
    ], "notes": [107]},
    "M-032": {"passages": [
        (97, 98, "À la place des charges sur les entreprises", "laissant le champ libre à l’investissement privé."),
    ]},
    "M-033": {"passages": [
        (97, 97, "Remplaçons les impôts cachés", "au taux fixé localement108."),
        (29, 29, "Les travailleurs sont particulièrement vulnérables", "laisser parents et amis derrière soi19."),
    ]},
    "M-034": {"passages": [], "notes": [108]},
    "M-035": {"passages": [
        (97, 97, "Remplaçons les impôts cachés", "au taux fixé localement108."),
    ]},
    "M-036": {"passages": [
        (114, 114, "Ce système garantit au travailleur", "par l’administration fiscale124."),
        (114, 114, "Le système fiscal conservera", "qu’un salaire stable et sécurisé ?"),
    ]},
    "M-039": {"passages": [
        (112, 113, "Quand l’État introduit une distinction", "notre capacité à y pourvoir."),
        (55, 56, "Les Français les plus précaires", "serait qualifié ailleurs d’abus de faiblesse."),
        (112, 112, "Un minimum social ne doit pas remplacer le travail.", "perdre brutalement ces oboles."),
    ]},
    "M-040": {"passages": [
        (115, 115, "Notre solidarité envers ceux", "Mettons fin aux inégalités créées par l’État."),
        (59, 60, "Un couple au SMIC bénéficie", "la participation équitable de chaque parent79."),
    ]},
    "M-041": {"passages": [
        (55, 55, "Notre système social prétend aider", "les femmes battues ou menacées."),
        (118, 118, "À ce titre, nous sommes solidaires", "jusqu’au handicap."),
    ], "notes": [124]},
    "M-019": {"passages": [
        (89, 90, "Il importe de souligner que cette restitution", "plutôt qu’au format formulaire."),
        (112, 112, "Fournir des réductions ponctuelles", "perdre brutalement ces oboles."),
        (35, 35, "Subventionner les loyers augmente les loyers", "subissent des prix immobiliers plus chers."),
        (36, 36, "La dépense publique est un jeu à somme négative.", "dans d’autres bureaux29."),
    ]},
    "M-023": {"passages": [
        (57, 57, "Si les dépenses publiques étaient la recette", "personnes étrangères sans titre permanent72."),
    ]},
    "M-042": {"passages": [
        (104, 104, "Épargner ses cotisations chômage", "leurs cotisations au-delà."),
    ]},
    "M-043": {"passages": [
        (104, 104, "La cotisation, fruit de l’effort", "ses souhaits, ses projets."),
        (104, 105, "Chaque Français constituera ainsi un capital", "tous les actionnaires et investisseurs."),
        (142, 142, "Les comptes épargne personnels seront créés", "sera proposée par votre banque."),
    ]},
    "M-044": {"passages": [
        (105, 105, "Au moment choisi par chaque travailleur", "restitué aux Français."),
        (58, 59, "Votre retraite dépend aujourd’hui", "illusoires se succèdent en vain."),
    ], "notes": [124]},
    "M-045": {"passages": [
        (103, 103, "Imaginez : vous pouvez choisir votre âge", "ou de gagner plus en partant plus tard."),
        (59, 59, "À 65 ans, il nous reste", "Tout le monde y perd."),
    ]},
    "M-046": {"passages": [
        (143, 143, "S’agissant du régime de retraite", "au moins équivalente au régime actuel."),
        (103, 104, "Introduire la capitalisation pour les retraites futures", "ni creuser le déficit public."),
    ], "notes": [124]},
    "M-053": {"passages": [
        (118, 118, "Malgré l’absence d’efficacité scientifique", "délais, pénuries et inflation."),
        (119, 119, "L’impôt doit se concentrer sur les cas graves", "le poids des dépenses de confort."),
        (118, 118, "L’illusion de la gratuité", "sans nous poser les bonnes questions126."),
    ]},
    "M-054": {"passages": [
        (119, 119, "Pour les soins critiques, un bouclier sanitaire", "plafond annuel de 5 % du revenu128."),
        (117, 117, "Nous payons plus cher qu’ailleurs", "est inférieure à la moyenne125."),
    ]},
    "M-055": {"passages": [
        (120, 120, "Choisissons librement quelle couverture", "jusqu’à 300 euros par an par foyer130."),
        (120, 120, "La concurrence libre entre mutuelles", "les prestations plus onéreuses."),
    ]},
    "M-056": {"passages": [
        (120, 120, "Les cotisations non dépensées", "en complément de la retraite et du patrimoine."),
    ]},
    "M-057": {"passages": [
        (119, 120, "Le Parlement doit définir", "entre catégories professionnelles et sociales."),
        (119, 119, "La Sécurité sociale a rompu", "qu’il ne paie pas ?"),
    ]},
    "M-024": {"passages": [
        (119, 119, "Les conditions fixées en contrepartie", "étrangers sans titre de séjour127."),
    ]},
    "M-052": {"passages": [
        (121, 122, "Des hôpitaux publics, par exemple", "selon les standards les plus efficaces."),
        (121, 121, "Libérons l’offre de soins", "n’a rien résolu132."),
    ]},
    "M-058": {"passages": [
        (123, 124, "Chaque élève bénéficie du même financement", "pour les enseignants, les bâtiments, le périscolaire."),
        (124, 124, "Le salaire net moyen des enseignants", "augmenté de 13 % grâce à la restitution134."),
        (61, 61, "Nous dépensons plus pour les élèves", "23 % mieux doté en euros que la moyenne nationale81."),
        (129, 129, "Ce compte éducation ne coûte rien", "donne les mêmes chances à tous."),
    ]},
    "M-059": {"passages": [
        (60, 61, "La carte scolaire prive", "jusque dans notre vie de famille."),
        (60, 60, "Seuls 7,4 % des élèves", "4e plus mauvais score parmi 78 pays recensés80."),
    ]},
    "M-060": {"passages": [
        (124, 125, "Selon l’OCDE, l’autonomie des écoles", "comme le formule la Cour des comptes137."),
        (125, 125, "Il en sera de même pour les écoles", "financées par le compte éducation."),
    ]},
    "M-061": {"passages": [
        (127, 127, "Le compte éducation versé et abondé", "doit exercer son discernement pour construire son avenir."),
        (127, 127, "Chaque Français pourra utiliser son compte", "peu de débouchés138."),
    ]},
    "M-062": {"passages": [
        (128, 128, "Des universités autonomes", "tous niveaux confondus139."),
        (61, 62, "La gratuité de l’université bénéficie", "obtiennent leur licence en trois ans85."),
        (62, 62, "La gratuité des uns est l’impôt de tous.", "et travailler un choix rémunérateur."),
    ]},
    "M-069": {"passages": [
        (139, 140, "La première étape est juridique", "sous l’égide de la représentation."),
    ]},
    "M-070": {"passages": [
        (141, 141, "Au sein de l’État, la suspension", "sera immédiate."),
    ]},
    "M-071": {"passages": [
        (141, 142, "Au bout de six mois", "sera déjà réalisée et restituée."),
        (142, 142, "Après les phases de transition", "égal à la hausse de salaire net déjà perçue."),
    ]},
    "M-037": {"passages": [
        (109, 109, "Transformer ce capital", "pourront être démocratiquement décidées."),
    ]},
    "M-038": {"passages": [
        (99, 99, "La baisse nette des impôts réduira", "à environ 36 % de la richesse produite."),
        (34, 34, "Toute dépense publique est un impôt", "l’impôt de demain27."),
    ]},
}

# --- annexe du livre, folios 170-171 : (folio, lignes du libellé, ligne des valeurs)
ANNEXE = {
    "B-01": [(170, [10], 10)],
    "B-02": [(170, [32, 34], 33), (170, [35, 37], 36), (170, [39], 39)],
    "B-03": [(170, [19, 21], 20), (170, [27], 27), (170, [39], 39), (171, [15], 15)],
    "B-04": [(171, [27], 27), (171, [29], 29)],
    "B-05": [(171, [5], 5), (171, [7, 8, 9], 8), (171, [11, 13], 12), (171, [15], 15)],
    "B-06": [(171, [21], 21), (171, [23, 25], 24)],
    "B-08": [(171, [31], 31), (171, [33], 33), (171, [35], 35)],
    "B-10": [(171, [39, 41], 40)],
    "B-11": [(171, [37], 37)],
    "B-17": [(170, [8], 8)],
}

# --- écarts du livre relevés au passage, rendus tels quels
ECARTS = [
    (86, "« Les établissements publics qui gèrent un patrimoine public et des "
         "revenus propres resterons autonomes » : accord du verbe."),
    (170, "Le titre du tableau porte « 236 millions d’euros (Md€) » : le total "
          "de la ligne suivante et le corps du livre portent 236 milliards."),
    (156, "La note 119 porte « environ 200 millions d’euros de produits de "
          "cession » pour un actif net de 340 milliards : l’ordre de grandeur "
          "est le milliard."),
    (158, "La note 137 porte une sur-contribution « estimée à 17 millions "
          "d’euros » qui représente « au moins 14 % de la dépense publique "
          "d’enseignement scolaire » : l’ordre de grandeur est le milliard."),
]

RESERVES = {
    "M-026": "Décision de l’auteure portée à l’arborescence : ne pas parler des "
             "pensions dans l’exposé. La note 121, sur l’abattement de 10 % "
             "sur les pensions, est rangée sous M-047 et M-037, non ici.",
    "M-053": "Décision de l’auteure portée à l’arborescence : ne pas présenter "
             "par les soins de confort, mais par des critères positifs — "
             "service médical rendu, criticité. Les passages ci-dessous sont "
             "le constat du livre, non la formule d’exposé.",
}


# --------------------------------------------------------------------------
def charger_livre():
    doc = json.loads(LIVRE.read_text(encoding="utf-8"))
    return doc, {p["folio"]: p for p in doc["pages"]}


def corps(doc, pages):
    """Texte coulant du corps, et table position -> folio."""
    morceaux, bornes, pos = [], [], 0
    for f in range(CORPS[0], CORPS[1] + 1):
        p = pages.get(f)
        if p is None or not p["lignes"]:
            continue
        t = couler(p, doc["coupes"])
        if morceaux:
            morceaux.append(" ")
            pos += 1
        bornes.append((pos, pos + len(t), f))
        morceaux.append(t)
        pos += len(t)
    return "".join(morceaux), bornes


def folio_de(bornes, i):
    for a, b, f in bornes:
        if a <= i < b:
            return f
    raise ValueError(i)


def plage(bornes, f0, f1):
    a = min(x for x, _, f in bornes if f0 <= f <= f1)
    b = max(y for _, y, f in bornes if f0 <= f <= f1)
    return a, b


COLLE = r"(?<=[A-Za-zÀ-ÿœŒ’»\)\]\.%])"
SUIT = r"(?=[\s.,;:!?»)\]]|$)"


def relever_appels(texte):
    """Position de chaque appel de note, dans l'ordre de numérotation."""
    appels, prec = {}, 0
    for n in range(1, DERNIERE_NOTE + 1):
        colle = re.compile(COLLE + rf"(?<!\d){n}(?!\d)" + SUIT)
        m = colle.search(texte, prec)
        suivant = None
        if n < DERNIERE_NOTE:
            suivant = re.compile(COLLE + rf"(?<!\d){n + 1}(?!\d)" + SUIT).search(texte, prec)
        if m is None or (suivant is not None and m.start() > suivant.start()):
            # appel détaché par une espace (cas composé « isolé 9. »)
            borne = suivant.start() if suivant else len(texte)
            espace = re.compile(rf"(?<=[A-Za-zÀ-ÿ]) {n}(?=[.,;:])")
            m2 = espace.search(texte, prec, borne)
            if m2 is not None:
                appels[n] = (m2.start() + 1, m2.end())
            else:
                # appel collé à un nombre (cas composé « CAC 40116. »)
                chiffre = re.compile(rf"(?<=\d){n}(?=[.,;:])")
                m3 = chiffre.search(texte, prec, borne)
                if m3 is None:
                    raise SystemExit(f"appel de note {n} introuvable")
                appels[n] = (m3.start(), m3.end())
        else:
            appels[n] = (m.start(), m.end())
        prec = appels[n][1]
    return appels


def adresse_coupee(ligne: str) -> bool:
    """Une ligne qui finit sur une adresse web, ou qui n'en porte qu'un morceau."""
    mots = ligne.split()
    if not mots:
        return False
    fin = mots[-1]
    return "://" in fin or fin.startswith("www.") or (len(mots) == 1 and "/" in fin)


def relever_notes(doc, pages):
    """Texte entier de chaque note, coupes recollées, dans l'ordre."""
    lignes = []
    for f in range(NOTES[0], NOTES[1] + 1):
        p = pages.get(f)
        if p is None:
            continue
        coupes = {c["ligne"]: c for c in doc["coupes"] if c["rang"] == p["rang"]}
        for i, l in enumerate(p["lignes"]):
            if f == NOTES[0] and i == 0 and l.strip() == "Notes":
                continue
            c = coupes.get(i)
            if c is not None:
                # dans une adresse web, le trait d'union appartient à l'adresse
                garde = c["verdict"] == "trait d’union du mot" or "/" in l.split()[-1]
                lignes.append((f, l if garde else l[:-1], ""))
            elif adresse_coupee(l):
                lignes.append((f, l, ""))
            else:
                lignes.append((f, l, " "))
    notes, n, cour = {}, 1, None
    for f, l, joint in lignes:
        if n <= DERNIERE_NOTE and re.match(rf"{n} ", l):
            if cour:
                notes[cour[0]] = (cour[1], "".join(cour[2]).strip())
            cour = (n, f, [l[len(str(n)) + 1:], joint])
            n += 1
        elif cour is not None:
            cour[2].extend([l, joint])
    notes[cour[0]] = (cour[1], "".join(cour[2]).strip())
    if len(notes) != DERNIERE_NOTE:
        raise SystemExit(f"{len(notes)} notes relevées sur {DERNIERE_NOTE}")
    return notes


def decouper(texte, bornes, f0, f1, debut, fin):
    a, b = plage(bornes, f0, f1)
    zone = texte[a:b]
    i = [m.start() for m in re.finditer(re.escape(debut), zone)]
    if len(i) != 1:
        raise SystemExit(f"ancre de début {debut!r} : {len(i)} occurrences p. {f0}-{f1}")
    j = [m.end() for m in re.finditer(re.escape(fin), zone) if m.start() >= i[0]]
    if not j:
        raise SystemExit(f"ancre de fin {fin!r} absente après {debut!r}")
    return a + i[0], a + j[0]


def rendre_passage(texte, appels, s, e):
    dedans = sorted((n, p) for n, p in appels.items() if s <= p[0] < e)
    out, k = [], s
    for n, (x, y) in dedans:
        out.append(texte[k:x])
        out.append(f"[{n}]")
        k = y
    out.append(texte[k:e])
    return "".join(out), [n for n, _ in dedans]


def arborescence():
    """Ordre de lecture : mouvement, bloc, mesures, tel que l'arborescence le porte."""
    ordre, mouv, bloc = [], None, None
    for l in ARBO.read_text(encoding="utf-8").splitlines():
        if l.startswith("## Mouvement") or l.startswith("## Transversal"):
            mouv = l[3:].replace("PÉRIMÈTRE À CONFIRMER", " — périmètre à confirmer")
        elif l.startswith("## "):
            mouv = None
        m = re.match(r"### (B-\d\d) — (.+)", l)
        if m and mouv:
            bloc = [m.group(1), m.group(2), mouv, []]
            ordre.append(bloc)
        m = re.match(r"\*\*(M-\d{3}(?: · M-\d{3})?) — (.+)\*\*$", l)
        if m and bloc:
            bloc[3].append((m.group(1), m.group(2)))
    return ordre


def valeurs_annexe(pages, f, libelle, ligne):
    l = pages[f]["lignes"]
    lib = " ".join(re.sub(r"\s{2,}[\d ]+$", "", l[i]).strip() for i in libelle)
    nums = [x for x in re.split(r"\s{2,}", l[ligne].strip()) if re.fullmatch(r"[\d ]+", x)]
    if len(nums) != 2:
        raise SystemExit(f"annexe f. {f} l. {ligne} : valeurs illisibles")
    return lib, nums[0], nums[1]


def generer():
    doc, pages = charger_livre()
    texte, bornes = corps(doc, pages)
    appels = relever_appels(texte)
    notes = relever_notes(doc, pages)
    empreinte = hashlib.sha256(LIVRE.read_bytes()).hexdigest()
    ordre = arborescence()

    vues = {m for b in ordre for m, _ in b[3]}
    cles = set()
    for m in vues:
        cles.update(m.split(" · "))
    manque = cles - set(RESERVOIR) - {"M-067 · M-068"}
    hors = set(RESERVOIR) - cles
    if hors:
        raise SystemExit(f"mesures hors arborescence : {sorted(hors)}")

    sortie, index, cmpt = [], [], {"passages": 0, "notes": set(), "sans_note": []}
    for code, titre, mouv, mesures in ordre:
        sortie.append(f"## {code} — {titre}\n\n*{mouv}*\n")
        if code in ANNEXE:
            sortie.append("**Chiffre du livre, tableau du détail des économies (annexe, p. 170-171)**\n")
            for f, lib, v in ANNEXE[code]:
                l, md, foyer = valeurs_annexe(pages, f, lib, v)
                sortie.append(f"- {l} — {md} Md€ par an, {foyer} € par an par foyer (p. {f})")
            sortie.append("")
        notes_bloc, folios_bloc = set(), set()
        for mcode, mtitre in mesures:
            for cle in mcode.split(" · "):
                spec = RESERVOIR.get(cle)
                t = mtitre.split(" · ")[mcode.split(" · ").index(cle)] if " · " in mcode else mtitre
                sortie.append(f"### {cle} — {t}\n")
                if spec is None:
                    sortie.append("*Le livre ne porte pas cette mesure.*\n")
                    continue
                if cle in RESERVES:
                    sortie.append(f"> *Réserve d’emploi.* {RESERVES[cle]}\n")
                cites = []
                if spec["passages"]:
                    sortie.append("**Argument de fond**\n")
                for f0, f1, deb, fin in spec["passages"]:
                    s, e = decouper(texte, bornes, f0, f1, deb, fin)
                    rendu, ns = rendre_passage(texte, appels, s, e)
                    fa, fb = folio_de(bornes, s), folio_de(bornes, e - 1)
                    ref = f"p. {fa}" if fa == fb else f"p. {fa}-{fb}"
                    sortie.append(f"> {rendu}\n>\n> — {ref}\n")
                    folios_bloc.update(range(fa, fb + 1))
                    cites += [n for n in ns if n not in cites]
                    cmpt["passages"] += 1
                for n in spec.get("notes", []):
                    if n not in cites:
                        cites.append(n)
                if cites:
                    sortie.append("**Citations opposables — notes de fin**\n")
                    for n in cites:
                        f, corps_note = notes[n]
                        propre = re.search(r"Calculs? Résolution", corps_note)
                        marque = " *(calcul propre déclaré)*" if propre else ""
                        sortie.append(f"- **Note {n}** (p. {f}){marque} — {corps_note}")
                    sortie.append("")
                else:
                    sortie.append("*Aucune note de fin ne porte cette mesure.*\n")
                    cmpt["sans_note"].append(cle)
                notes_bloc.update(cites)
                cmpt["notes"].update(cites)
        index.append((code, titre, [m for m, _ in mesures], sorted(folios_bloc), sorted(notes_bloc)))
        sortie.append("---\n")

    tete = [
        "# Réservoir d’arguments du livre — par mesure et par bloc\n",
        "*Pièce de la valise : rôle « réservoir d’arguments sourcés ». Dérivé, se régénère par "
        "`python3 appareil/reservoir_livre.py`.*\n",
        f"Source : `livre/texte_livre.json`, épreuve `{doc['_source']['epreuve']}`, "
        f"sha256 du JSON `{empreinte[:16]}…`. Ordre et intitulés : "
        f"`{ARBO.name}`.\n",
        "## Règles de lecture\n",
        "- **Tout texte cité est découpé mécaniquement dans le livre**, coupes de fin de ligne "
        "recollées selon le verdict porté au JSON. Aucun mot n’est retapé.",
        "- **Argument de fond** : un ou plusieurs passages du livre, folio en pied. Le choix des "
        "passages est un jugement ; leur texte ne l’est pas.",
        "- **Appel de note** : collé au mot dans la composition, il est rendu « [n] ».",
        "- **Citation opposable** : le texte entier de la note de fin appelée dans un passage retenu, "
        "ou expressément rattachée à la mesure. Une note qui se déclare « Calcul(s) Résolution » "
        "est marquée *calcul propre déclaré* : opposable comme décompte, non comme source tierce.",
        "- Une mesure dont aucun passage n’appelle de note le dit.",
        "- Rien n’est sourcé au-delà de ce que le livre porte.\n",
        f"**Relevé** : {sum(len(b[3]) for b in ordre)} entrées d’arborescence, "
        f"{len(cles)} mesures, {len(index)} blocs ; {cmpt['passages']} passages ; "
        f"{len(cmpt['notes'])} notes de fin citées sur {DERNIERE_NOTE} ; "
        f"{len(cmpt['sans_note'])} mesures sans note : "
        + (", ".join(cmpt["sans_note"]) or "aucune") + ".\n",
    ]
    if manque:
        tete.append(f"Mesures de l’arborescence sans passage : {', '.join(sorted(manque))}.\n")
    tete.append("## Index par bloc\n")
    tete.append("| bloc | mesures | folios | notes |")
    tete.append("|---|---|---|---|")
    for code, titre, ms, fs, ns in index:
        tete.append(f"| {code} — {titre} | {', '.join(ms)} | {', '.join(map(str, fs)) or '—'} "
                    f"| {', '.join(map(str, ns)) or '—'} |")
    tete.append("")
    pied = ["## Écarts du livre relevés au passage\n",
            "*Relevés, non corrigés : le livre fait foi, ces lignes signalent.*\n"]
    pied += [f"- p. {f} — {t}" for f, t in ECARTS]
    pied.append("")
    return "\n".join(tete + sortie + pied)


def main(argv):
    cible = Path(argv[1]) if len(argv) > 1 else SORTIE
    cible.write_text(generer(), encoding="utf-8")
    print(cible)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
