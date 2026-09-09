# -*- coding: utf-8 -*-
"""Champs rédigés du côté gain, symétriques de `justification` et `relais`.

Un gain porte une vedette et une phrase.

`apport`        — ce que la personne y gagne, en langue ordinaire, à la deuxième
                  personne du pluriel. Court et frappant. Il répond à « qu'est-ce
                  que ça me fait ».
`contrepartie`  — qui le paie, en toutes lettres. Elle répond à « aux dépens de
                  qui ».
`vedette`       — deux ou trois signes qui tiennent la tête de ligne : un
                  chiffre quand le gain en porte un, **deux mots quand il n'en
                  porte pas**. « Le temps » vaut « 70 % » sur la ligne d'un agent
                  public dont le poste est supprimé, et se lit sur le même plan.

`MODALITES`     — une ligne qui n'est pas un gain mais la **modalité** d'un
                  autre : la restitution par paliers de 2 % par mois dit comment
                  arrivent les 600 €, elle n'ajoute rien à ce qu'on reçoit. Elle
                  reste au référentiel, elle ne sort pas en fiche. Restituer
                  n'est pas réciter.

Clé : "ancrage|position|categorie", comme les justifications.

**La vedette et l'apport font une seule unité, et ne se citent pas séparément.**
La phrase ne répète pas ce que la vedette porte — « 600 € » puis « rendus tous
les mois, sur votre compte », et non « 600 euros par mois vous sont rendus tous
les mois ». Tout livrable qui projette un apport projette sa vedette avec lui.

**La contrepartie, et la faute qu'elle a portée.** Presque toute la restitution
est payée par l'ensemble des économies, non par une mesure isolée. Écrire
« payé par la fin de l'abattement de 10 % sur les pensions » en regard d'un gain
de treize pour cent de salaire net attribue à une niche ce que finance tout le
plan : c'est un contresens, et il est attaquable. `CONTREPARTIE_GENERALE` porte
donc la formule commune, et le format la dit **une fois en pied** au lieu de la
répéter à chaque ligne.

Deux exceptions, et elles seules : le **chômage** et le **patrimoine**, dont la
restitution a sa propre source, nommée au corpus.

Une ligne sans apport se projette par l'énoncé du REF, qui est une phrase du
manuscrit, et sa vedette se relève de cet énoncé. C'est le régime transitoire,
non la cible.
"""

# Reconnue telle quelle par le générateur de fiches, qui la hisse en pied.
CONTREPARTIE_GENERALE = ("Payé par l'ensemble des économies publiques, "
                         "pas par une mesure en particulier.")

# Le chômage et le patrimoine ont leur source propre, nommée au corpus.
C_CHOMAGE = ("Payé par l'indemnisation de longue durée, qui passe de treize à "
             "six mois.")
# C_RETRAITE est retiré le 20260828 : les pensions supérieures à 1 600 euros
# gagent l'impôt sur le revenu, non la restitution des cotisations. La ligne de
# retraite ne porte donc aucune contrepartie propre.

G = CONTREPARTIE_GENERALE

# Une modalité n'est pas un gain : elle dit comment un gain arrive. Elle reste
# au référentiel et au compte, elle ne prend pas une ligne de fiche.
MODALITES = {
    "D11-4-2|gagnant|C-04": "D3-2-2-e1",
    # La hausse des salaires nets est, pour l'agent public qui part, un
    # atout du privé et non un gain séparé : elle se dit dans « Le privé ».
    "D3-2-1-e1|gagnant|C-30": "D6-2-2-e4",
    # « En franchise » ne se comprend pas seul : le propos va avec les
    # 0,77 € du taux unique, qui le porte désormais dans sa phrase.
    "D9-3-1-e2|gagnant|C-04": "D9-3-1-e1",
    "D11-4-2|gagnant|C-16": "D3-2-2-e1",
    "D9-3-1-e2|gagnant|C-16": "D9-3-1-e1",
    # Le chômage n'est pas un gain : c'est une part du compte épargne, qui le
    # nomme avec la retraite, une fois et directement.
    "D8-3-1-e2|gagnant|C-04": "D8-2-2-e1",
    # L'aide fondamentale se dit une fois : le reste est sa modalité.
    "D9-2-1-e1|gagnant|C-16": "D9-2-1",
    # Chez le bénéficiaire d'un chèque, c'est « 550 € en argent libre » qui
    # porte l'aide fondamentale : l'énoncé général en est la modalité.
    "D9-2-1|gagnant|C-32": "D9-2-1-e1",
}

# Ordre de lecture propre à chaque catégorie. Ce qui compte pour un jeune
# adulte n'est pas ce qui compte pour un retraité, et l'ordre des promesses du
# manuscrit est celui de la chaîne doctrinale, non celui d'une vie. Les
# ancrages listés ici passent devant, dans cet ordre ; le reste suit les
# promesses.
# Attache d'un gain projeté sur plusieurs catégories : **là où il est le plus
# pertinent**. Il s'y dit en entier ; partout ailleurs il revient en rappel, sa
# vedette seule. Un gain sans attache n'est porté que par une catégorie.
ATTACHE = {
 "D3-2-2-e1": "C-04",    # les 600 € rendus, c'est le travailleur
 "D3-2-1-e1": "C-04",    # la hausse du salaire net, c'est le travailleur
 "D9-3-1-e1": "C-04",    # le taux unique, c'est celui qui gagne un revenu
 "D8-2-1-e2": "C-04",    # la retraite en capital, avec son compte épargne
 "D8-2-2-e2": "C-04",
 "D8-2-2-e4": "C-04",
 "D7-2-1-e1": "C-16",    # démarrer avec un capital plutôt qu'avec zéro
 "D7-3-1-e1": "C-11",    # la détente locative, c'est le locataire
 "D9-2-1-e1": "C-10",    # l'aide fondamentale, d'abord celui qui n'a rien
 "D9-4-1-e1": "C-17",    # les 275 € par enfant sont versés au parent
 "D10-3-1-e4": "C-17",   # le choix de l'école appartient au parent
 "D10-2-1-e1": "C-15",   # le compte éducation finance la scolarité
}

ORDRE = {
 "C-04": ["D3-2-2-e1", "D3-2-1-e1", "D8-2-2-e1", "D9-3-1-e1", "D10-4-1-e1",
          "D10-4-1-e5"],
 "C-16": ["D3-2-1-e1", "D9-2-1", "D10-4-1-e4", "D7-3-1-e1", "D7-2-1-e1",
          "D8-2-1-e2"],
 "C-10": ["D3-2-1-e1", "D8-3-1-e1", "D2-4-1-e1", "D9-2-1-e1", "D3-ei2",
          "D8-3-1-e2"],
 "C-06": ["D4-3-3-e2", "D4-3-1-e1", "D4-2-3", "D4-2-1-e1", "D2-5-1-e1",
          "D3-ei1"],
 "C-05": ["D6-3-2-e2", "D6-3-1-e2", "D6-3-2-e1", "D6-3-1-e1"],
 "C-30": ["D6-2-2", "D6-2-2-e7", "D6-2-2-e4"],
 "C-09": ["D7-2-1-e1", "D7-2-2-e1", "D8-4-1-e1", "D8-2-1-e1", "D8-4-2-e4"],
 "C-15": ["D9-4-1-e1", "D10-3-1-e4", "D9-4-2-e2", "D10-2-1-e1"],
 "C-17": ["D9-4-1-e1", "D10-2-1-e1", "D10-3-1-e4", "D10-3-1-e6"],
 "C-40": ["D9-2-1-e1", "D7-3-1-e1"],
}

APPORTS = {

# ============================================================ C-04 travailleur

"D3-2-2-e1|gagnant|C-04": (
 "Rendus tous les mois : 300 euros sur votre salaire net, 300 euros sur un "
 "compte épargne à votre nom.", G, "600 €"),

"D3-2-1-e1|gagnant|C-04": (
 "Votre salaire net en un an, au salaire médian. 180 euros de plus par mois "
 "au SMIC.", G, "+13 %"),

"D9-3-1-e1|gagnant|C-04": (
 "Ce qui vous reste par euro gagné, quel que soit votre revenu. L'aide "
 "fondamentale n'est pas imposée : vous ne payez que sur ce qui la "
 "dépasse.", G, "0,77 €"),

"D8-3-1-e2|gagnant|C-04": (
 "Vos cotisations chômage alimentent le même compte.", C_CHOMAGE),

# Modalité du versement des 600 €, non un gain de plus. Voir MODALITES.
"D11-4-2|gagnant|C-04": (
 "La restitution arrive par paliers de 2 % par mois. Vous n'attendez pas la "
 "fin de la réforme.", G),

# La grappe de la retraite : la tête porte la vedette, les trois autres se
# rangent sous elle.
"D8-2-2-e1|gagnant|C-04": (
 "Sur votre compte épargne personnel : la retraite d'abord, le chômage "
 "ensuite. Vous partez quand il vous convient.", G, "300 €"),

"D8-2-1-e2|gagnant|C-04": (
 "Vous en suivez la croissance, mois après mois.", G),

"D8-2-2-e2|gagnant|C-04": (
 "Votre pension ne dépend plus d'aucune caisse ni d'aucun régime.", ""),

"D8-2-2-e4|gagnant|C-04": (
 "Vous ne dépendez plus d'une promesse politique ni du déficit public.",
 G),

"D9-3-1-e2|gagnant|C-04": (
 "L'aide fondamentale est inconditionnelle : vous ne payez l'impôt que sur "
 "ce qui la dépasse.", G, "En franchise"),

"D10-4-1-e1|gagnant|C-04": (
 "Une carrière longue vous paie un départ plus tôt, ou une pension plus "
 "élevée.", G, "Votre carrière"),

"D10-4-1-e5|gagnant|C-04": (
 "Vos choix se paient dessus, et personne ne porte la charge d'un autre.",
 G, "Compte éducation"),

# ====================================== C-30 agent public au poste supprimé
# Tranché par l'auteur le 20260828 (A-210) : la durée se dit « jusqu'à sept ans ».
# Un contrat à durée déterminée ne conserve pas le bénéfice au-delà de son terme,
# donc sept ans est un plafond et non une durée acquise. Les relais du côté perte
# le disent désormais aussi.
# La durée se dit « jusqu'à sept ans » et non « pendant sept ans » : D6-2-2-p2
# est un plafond, ses conditions l'écrivent, et l'alerte structurelle R10 le
# signale déjà. Les trois `relais` du côté perte portent « sept ans », écrits
# avant cette lecture ; l'écart est consigné au registre.

"D6-2-2|gagnant|C-30": (
 "De votre traitement, sans condition, jusqu'à sept ans. Cumulable avec un "
 "emploi privé.", G, "70 %"),

"D3-2-1-e1|gagnant|C-30": (
 "La hausse des salaires nets dans le privé, où vous pouvez travailler dès "
 "votre départ, indemnité comprise.", G, "+13 %"),

"D6-2-2-e7|gagnant|C-30": (
 "Il vous revient. Le métier d'après, vous le choisissez.",
 G, "Votre temps"),

"D6-2-2-e4|gagnant|C-30": (
 "Une entreprise, une association, un projet à vous — et des salaires nets "
 "qui montent de 13 %.", G, "Le privé"),

# ============================================ C-05 agent public maintenu
# Le pendant de C-30 : celui qui reste. Il perd le statut, il gagne le métier.

"D6-3-2-e2|gagnant|C-05": (
 "Votre rémunération nette, une fois l'État recentré sur ses missions.",
 G, "+13 %"),

"D6-3-2-e1|gagnant|C-05": (
 "Moins nombreux, mieux payés, mieux équipés : vous avez de quoi faire.",
 G, "Les moyens"),

"D6-3-1-e2|gagnant|C-05": (
 "Vous la conduisez vous-même : mobilité, promotion, primes au mérite.",
 G, "Votre carrière"),

"D6-3-1-e1|gagnant|C-05": (
 "Votre métier se juge sur ce que vous produisez.", G, "L'estime"),


# ============================================================ C-16 jeune adulte

"D3-2-2-e1|gagnant|C-16": (
 "Ce que le plan vous rend chaque mois, salaire et compte épargne réunis.",
 G, "600 €"),

"D3-2-1-e1|gagnant|C-16": (
 "Votre salaire net dès l'embauche. 180 euros de plus par mois au SMIC.",
 G, "+13 %"),

"D9-2-1|gagnant|C-16": (
 "Votre aide fondamentale, tous les mois, sans dossier ni guichet.",
 G, "550 €"),

"D9-2-1-e1|gagnant|C-16": (
 "Personne ne juge ce que vous faites de votre vie pour vous la verser.", G),

"D7-2-1-e1|gagnant|C-16": (
 "Vous démarrez avec un capital, plus avec zéro.", G, "20 000 €"),

"D9-3-1-e1|gagnant|C-16": (
 "Ce qui vous reste par euro gagné, dès le premier.", G, "0,77 €"),

"D9-3-1-e2|gagnant|C-16": (
 "Sous l'aide fondamentale, l'administration vous verse la différence.", G),

"D11-4-2|gagnant|C-16": (
 "Votre restitution arrive par paliers de 2 % par mois.", G),

"D8-2-1-e2|gagnant|C-16": (
 "Un capital à votre nom, qui grandit dès vos premières cotisations.",
 G, "Votre retraite"),

"D8-2-2-e2|gagnant|C-16": (
 "Elle ne dépend d'aucune caisse ni d'aucun régime, et vous la suivez à tout "
 "moment.", G),

"D8-2-2-e4|gagnant|C-16": (
 "À trente ans de la retraite, c'est la seule garantie qui tienne.", G),

"D7-3-1-e1|gagnant|C-16": (
 "D'offre locative en plus : votre premier logement cesse d'être une "
 "loterie.", G, "+25 %"),

"D9-4-1-e2|gagnant|C-16": (
 "Vous pouvez en fonder une : c'est devenu un projet finançable, plus un "
 "pari.", G, "Une famille"),

"D10-4-1-e2|gagnant|C-16": (
 "Chaque année travaillée compte pour vous, dès la première.", G),

"D10-4-1-e4|gagnant|C-16": (
 "Poursuivre des études devient une décision qui vous appartient.",
 G, "Vos études"),

"D10-4-1-e6|gagnant|C-16": (
 "Si vous travaillez à vingt ans, vous ne payez plus les études des autres.",
 G),

"D10-2-1-e1|gagnant|C-16": (
 "Le même montant pour vous former, où que vous viviez.",
 G, "Compte éducation"),

"D10-4-2-e1|gagnant|C-16": (
 "Les établissements vous proposeront des tarifs réduits sur vos résultats.",
 G),

"D10-4-2-e2|gagnant|C-16": (
 "Une formation devra vous démontrer ce qu'elle vous ouvre.", G),

"D10-4-2-e3|gagnant|C-16": (
 "Vous former par le travail redevient une voie qui en vaut une autre.", G),

# ============================================================== C-06 entreprise

"D4-3-3-e2|gagnant|C-06": (
 "Les impôts de production disparaissent : vous ne payez plus rien avant "
 "d'avoir gagné.", G, "0 € avant profit"),

"D2-5-1-e1|gagnant|C-06": (
 "Votre charge globale ne monte pas : ce qui sort d'un côté rentre de "
 "l'autre.", G, "Votre charge"),

"D3-ei1|gagnant|C-06": (
 "Ils ont 13 % de pouvoir d'achat en plus, et le travail moins taxé rend vos "
 "embauches rentables.", G, "Vos clients"),

"D4-2-1-e1|gagnant|C-06": (
 "Un principe court remplace les milliers de pages que vous subissez, et le coût "
 "qui allait avec.", G, "La paperasse"),

"D4-2-3|gagnant|C-06": (
 "Vous entreprenez d'abord : l'autorisation préalable disparaît, l'abus se "
 "sanctionne.", G, "Le formulaire"),

"D4-3-1-e1|gagnant|C-06": (
 "Un impôt unique sur les bénéfices remplace l'empilement, et nul ne le "
 "contourne à votre place.", G, "Un seul impôt"),

"D9-3-1-e1|gagnant|C-06": (
 "Ce qui vous reste par euro de revenu, quel qu'en soit le montant.",
 G, "0,77 €"),

"D9-3-1-e6|gagnant|C-06": (
 "Votre revenu d'indépendant est imposé au même taux que celui d'un salarié.",
 G, "Le taux unique"),

# ==================================================== C-10 personne sans emploi

"D2-4-1-e1|gagnant|C-10": (
 "De plus par mois au salaire type, une fois les aides remplacées par le "
 "salaire.", G, "+220 €"),

"D3-2-1-e1|gagnant|C-10": (
 "Le salaire net que vous retrouverez : 180 euros de plus par mois au SMIC.",
 G, "+13 %"),

"D9-2-1-e1|gagnant|C-10": (
 "Votre aide fondamentale, tous les mois, sans dossier ni contrôle.",
 G, "550 €"),

"D9-3-1-e1|gagnant|C-10": (
 "Ce qui vous reste par euro gagné, dès votre reprise.", G, "0,77 €"),

"D8-3-1-e1|gagnant|C-10": (
 "Ce que vous n'avez pas consommé de votre compte vous reste.",
 G, "La reprise"),

"D8-3-1-e2|gagnant|C-10": (
 "Vos cotisations chômage l'alimentent tous les mois, à votre nom.",
 C_CHOMAGE, "Compte épargne"),

"D3-ei2|gagnant|C-10": (
 "Les entreprises qui vous recrutent paient le travail moins cher, et "
 "embauchent davantage.", G, "L'embauche"),

# ================================================================ C-09 retraité

"D7-2-1-e1|gagnant|C-09": (
 "De patrimoine public transféré à votre foyer, en trois ans.", G, "20 000 €"),

"D7-2-2-e1|gagnant|C-09": (
 "Par an au moins, votre complément viager du patrimoine restitué.",
 G, "500 €"),

"D8-4-1-e1|gagnant|C-09": (
 "De votre revenu au maximum : votre reste à charge de santé est plafonné.",
 G, "5 %"),

"D8-2-1-e1|gagnant|C-09": (
 "Le système se remet d'aplomb sans y toucher.", G, "Votre pension"),

"D8-2-2-e4|gagnant|C-09": (
 "Elle ne dépend plus d'une promesse politique ni du déficit public.", G),

"D8-4-2-e4|gagnant|C-09": (
 "Votre capital santé finance aussi la perte d'autonomie, le moment venu.",
 G, "L'autonomie"),

# ================================================================== C-15 enfant

"D9-4-1-e1|gagnant|C-15": (
 "Par mois, versés à vos parents de votre naissance à vos dix-huit ans.",
 G, "275 €"),

"D9-4-2-e2|gagnant|C-15": (
 "La part de chacun d'eux est versée, quelle que soit leur situation.",
 G, "Vos parents"),

"D10-2-1-e1|gagnant|C-15": (
 "Le même montant pour votre scolarité, où que vous viviez.",
 G, "Compte éducation"),

"D10-3-1-e4|gagnant|C-15": (
 "Vos parents choisissent votre école, qui doit leur en donner les raisons.",
 G, "Le choix"),

# ================================================================== C-17 parent

"D9-4-1-e1|gagnant|C-17": (
 "Par mois et par enfant, versés à votre foyer sans dossier.", G, "275 €"),

"D10-2-1-e1|gagnant|C-17": (
 "Par an sur le compte éducation de votre enfant, où que vous viviez.",
 G, "6 600 €"),

"D10-3-1-e4|gagnant|C-17": (
 "Vous choisissez l'école de votre enfant, et elle doit vous en donner les "
 "raisons.", G, "La liberté scolaire"),

"D10-3-1-e6|gagnant|C-17": (
 "Agrément simple, sanction réelle : elle répond devant vous.", G),

# =========================================================== C-23 consommateur

"D4-3-2-e1|gagnant|C-23": (
 "Les taxes spécifiques et les taux réduits disparaissent de vos prix.",
 G, "Les taxes"),

"D4-2-3|gagnant|C-23": (
 "Plus d\'offre, plus de concurrence : vous choisissez, et à meilleur prix.",
 G, "Le choix"),

"D4-3-3-e1|gagnant|C-23": (
 "De ce que vous consommez est produit en France, et ces produits baissent.",
 G, "81 %"),

# =============================================================== C-11 locataire

"D7-3-1-e1|gagnant|C-11": (
 "D'offre locative privée en plus, et l'APL qui cesse de pousser les prix : "
 "les loyers baissent.", G, "+25 %"),

"D4-4-1-e1|gagnant|C-11": (
 "Les frais de notaire s'effondrent : acheter cesse d'être hors d'atteinte.",
 G, "L\'achat"),

"D3-2-1-e1|gagnant|C-11": (
 "De salaire net en plus, pendant que le loyer, lui, cesse de monter.",
 G, "+13 %"),


# ========================================================= C-40 locataire HLM

"D9-2-1-e1|gagnant|C-40": (
 "Elle vous est versée à vous, au lieu de passer par votre bailleur.",
 G, "550 €"),

"D7-3-1-e1|gagnant|C-40": (
 "D'offre locative privée en plus : vous avez le choix de votre logement.",
 G, "+25 %"),


# ============================================================= C-01 contribuable

"D11-e1|gagnant|C-01": (
 "De la richesse produite, contre 43 % aujourd\'hui : c\'est ce que vous "
 "verserez.", G, "36 %"),

"D2-5-1-e2|gagnant|C-01": (
 "De niches supprimées, dont 52 milliards vous reviennent en baisse de "
 "charges et de taxes.", G, "143 Md€"),

"D2-4-1-e2|gagnant|C-01": (
 "Par an de subventions et d\'aides que vous ne financez plus.",
 G, "68,9 Md€"),

"D6-2-2-e2|gagnant|C-01": (
 "Par an de masse salariale publique en moins sur votre feuille d\'impôt.",
 G, "29,6 Md€"),

"D2-2-1-e2|gagnant|C-01": (
 "Par an d\'agences et d\'administrations dont vous payiez le fonctionnement.",
 G, "12,4 Md€"),

"D5-2-1-e2|gagnant|C-01": (
 "Par an d\'échelons locaux dont vous payiez le fonctionnement.",
 G, "9,6 Md€"),

"D9-2-2-e1|gagnant|C-01": (
 "Par an d\'aide médicale d\'État : le droit commun s\'applique.", G, "1,1 Md€"),

"D2-5-1-e1|gagnant|C-01": (
 "Aucun prélèvement nouveau ne vous est demandé : tout se paie sur la "
 "dépense.", G, "Aucune hausse"),

"D1-3-1|gagnant|C-01": (
 "Celui qui abuse de votre argent répond plus lourdement, non moins.",
 G, "La sanction"),

"D6-2-2-e5|gagnant|C-01": (
 "Vous payez pour ce qui produit, et vous savez quoi.", G, "Le consentement"),

# ================================================================== C-02 citoyen

"D6-2-2-e6|gagnant|C-02": (
 "Concentré sur sept missions, il les remplit — et vous le voyez.",
 G, "L\'État utile"),

"D6-ei2|gagnant|C-02": (
 "Policiers, gendarmes et magistrats renforcés, et présents là où vous vivez.",
 G, "Le terrain"),

"D2-3-1-e1|gagnant|C-02": (
 "Police, justice, défense : un responsable identifié, qui répond devant "
 "vous.", G, "Le régalien"),

"D5-3-3-e1|gagnant|C-02": (
 "Un seul interlocuteur de l\'État sur votre territoire.", G, "Un guichet"),

"D5-2-1-e1|gagnant|C-02": (
 "Un échelon local lisible, et votre vote qui décide vraiment.",
 G, "Votre voix"),

"D1-1-1|gagnant|C-02": (
 "Chaque euro public est auditable en permanence, et vous pouvez le "
 "vérifier.", G, "L\'audit"),

"D1-2-1|gagnant|C-02": (
 "Vous votez périodiquement les missions que l\'État exerce en votre nom.",
 G, "Votre accord"),

"D7-4-1-e1|gagnant|C-02": (
 "Ceux qui contrôlent pour vous ne dépendent plus de ceux qu\'ils contrôlent.",
 G, "Le contrôle"),

"D9-3-1-e5|gagnant|C-02": (
 "Vous savez ce que vous devez, sans expert ni angoisse de fin d\'année.",
 G, "La clarté"),

"D9-3-1-e4|gagnant|C-02": (
 "Vous payez selon ce que vous gagnez : la progressivité tient.", G),

"D6-2-2-e3|gagnant|C-02": (
 "Les forces que l\'État libère reviennent à la société, donc à vous.", G),

"D11-4-1-e1|gagnant|C-02": (
 "Trois mois de préparation, trois mois d\'exécution : vous voyez venir.",
 G, "Le calendrier"),

# ==================================================================== C-03 foyer

"D7-2-1-e1|gagnant|C-03": (
 "De patrimoine public rendu à votre foyer, en trois ans.", G, "20 000 €"),

"D7-2-2-e2|gagnant|C-03": (
 "Par an, ce que votre capital rapporte au rythme de l’économie, non d’un vote, sans s\'épuiser.",
 G, "600 €"),

"D4-4-1-e1|gagnant|C-03": (
 "Les impôts cachés sur vos mutations et vos successions disparaissent.",
 G, "La transmission"),

"D10-4-1-e5|gagnant|C-03": (
 "Vos choix se paient sur vos comptes, et personne ne porte la charge d\'un "
 "autre.", G, "La restitution"),

"D9-3-1-e3|gagnant|C-03": (
 "Un seuil unique, sans niche ni quotient : la même loi pour vous que pour "
 "tous.", G, "Le seuil"),

# =============================================================== C-06 entreprise

"D4-ei1|gagnant|C-06": (
 "Une réglementation stable et lisible ramène les investisseurs chez vous.",
 G, "L\'attractivité"),

"D4-ei2|gagnant|C-06": (
 "Un cadre clair vaut mieux, pour vous attirer, que toutes les campagnes de "
 "communication.", G, "Le cadre"),

"D8-ei1|gagnant|C-06": (
 "Le travail et l\'épargne libérés vous donnent des clients et des "
 "investisseurs.", G, "Les moteurs"),

# =============================================================== C-19 enseignant

"D10-3-1-e1|gagnant|C-19": (
 "Il est maintenu, puis augmenté par la restitution.", G, "Votre salaire"),

"D10-3-1-e3|gagnant|C-19": (
 "Vous choisissez où et comment enseigner, et votre rémunération se négocie.",
 G, "La liberté"),

"D10-3-1-e2|gagnant|C-19": (
 "Instituteurs et jeunes enseignants, vous êtes les premiers revalorisés.",
 G, "Les débuts"),

# ================================================================= C-17 famille

"D9-4-2-e2|gagnant|C-17": (
 "La part de chacun des deux parents est versée, quelle que soit leur "
 "situation.", G, "Vos parents"),

# ================================================================= C-13 patient

"D8-4-1-e1|gagnant|C-13": (
 "Votre reste à charge est plafonné à 5 % de votre revenu annuel : au-delà, "
 "vous ne payez plus rien.", G, "Le bouclier sanitaire"),

"D8-4-2-e1|gagnant|C-13": (
 "Par an de frais de gestion en moins : vous ne payez plus l\'intermédiaire "
 "obligatoire.", G, "300 €"),

"D8-4-2-e3|gagnant|C-13": (
 "Les complémentaires se font concurrence, et vous choisissez la vôtre.",
 G, "Votre complémentaire"),

"D8-4-2-e2|gagnant|C-13": (
 "Vous êtes soigné au moins aussi bien qu\'aujourd\'hui, et souvent mieux.",
 G, "Le soin"),

# ================================================ C-32 allocataire d\'aide ciblée

"D9-2-1-e1|gagnant|C-32": (
 "Par mois en argent libre : vous en disposez en totalité, pour ce que vous "
 "voulez.", G, "550 €"),

"D2-4-1-e1|gagnant|C-32": (
 "De plus par mois au salaire type : le revenu remplace le guichet.",
 G, "+220 €"),

"D5-3-4|gagnant|C-32": (
 "L\'État reprend les solidarités : un seul payeur pour vous, plus de "
 "guichet à chercher.", G, "Un payeur"),

# ============================== C-33 entreprise ou association subventionnée

"D4-2-3|gagnant|C-33": (
 "Vous agissez d\'abord : aucun dossier à monter, aucune aide à mériter.",
 G, "Sans formulaire"),

"D3-ei1|gagnant|C-33": (
 "Ils ont 13 % de pouvoir d\'achat en plus : ils achètent ce que la "
 "subvention vous faisait produire à leur place.", G, "Des clients plus riches"),

"D4-3-3-e2|gagnant|C-33": (
 "Vous ne payez plus rien avant d\'avoir gagné : votre modèle tient sur ses "
 "recettes.", G, "0 € avant profit"),

"D4-3-1-e1|gagnant|C-33": (
 "Un impôt unique sur les bénéfices : votre concurrent aidé perd son "
 "avantage.", G, "Un seul impôt"),

# ======================================================= C-14 personne handicapée

"D8-4-1-e1|gagnant|C-14": (
 "Votre reste à charge est plafonné à 5 % de votre revenu annuel : la dépense "
 "lourde ne vous atteint pas.", G, "Le bouclier sanitaire"),

"D9-2-3-e1|gagnant|C-14": (
 "Par mois, versés automatiquement : vous ne refaites plus de dossier.",
 G, "1 100 €"),

}
