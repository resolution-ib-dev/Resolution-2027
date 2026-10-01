# Mandat du fil code — garde, navigation, vocabulaire, quatre pages (20260924, go de l'auteure)

Arrêté par l'auteure le 20260924, contrainte par contrainte, sur audit mesuré du site en ligne. Cible : session `claude.ai/code` sur `resolution-ib-dev/Site-ETNP`, même fil. Pièces à joindre par l'auteure : couverture (PNG), quatrième de couverture (PNG), photo des trois auteurs, et les sept classeurs `_0910` **dans une seule archive `classeurs.zip`** (le fil code n'accepte que cinq pièces). Le prompt ci-dessous est autonome : la session ne voit pas le projet Résolution.

---

Dépôt `Site-ETNP`. On repart de `main` ; les variantes précédentes (`c56390c` et antérieures) sont abandonnées. Branche de travail. **Rien ne se génère ni ne se branche avant validation de la planche par l'auteure. Rien sur `main`.**

## 0. Mesure

Rends en quelques lignes : HEAD de `main` ; la liste des pages servies ; chemins de l'accueil et de `fiche.css` ; les règles CSS actuelles de la barre (onglets, boutons, liens) avec leurs valeurs réelles. Présence des pièces jointes : couverture, quatrième, photo des auteurs, et l'archive `classeurs.zip` que tu décompresses — elle doit porter sept classeurs (`Synthèse Calculs`, `Synthèse Graphiques`, `Synthèse ETP et agences`, `T_3305_APUL`, `Taxes affectées`, `Dépenses fiscales`, `Dépenses 2026 du BG et des BA`). Si l'accueil ou `fiche.css` manque : rends la mesure, arrête-toi. Si une image ou un classeur manque : le lot se joue sans lui, emplacement réservé, et tu le signales — rien n'est inventé.

## 1. Vocabulaire et renvois — sur tout le site

- **« Manifeste » ne nomme plus que la page.** L'adhésion se dit **« J'adhère »**, partout : bouton, titre de `adherer.html` (« J'adhère — Résolution »), objet du courriel. « Lire le manifeste d'abord » disparaît. Finalité des données, sur `adherer.html` et `contact.html` : « vous envoyer les nouvelles du mouvement ». Le reste du texte de ces deux pages ne change pas.
- **Un nom par page, identique sur l'onglet, le titre et tout renvoi**, sans déterminant : Manifeste · Propositions · Données · Vidéos · Auteurs, et Le livre. « Sommaire » devient « Propositions ». Sur `fiches.html`, « Ce que le plan change pour vous » passe en sous-titre sous « Propositions ».
- **Titre du manifeste** : les deux lignes de tête s'inversent, aucun corps ne change. Titre : **« Manifeste de Résolution »**. Ligne dessous, petite, existante : **« État partout, justice nulle part — en librairie le 9 octobre »**.
- **Fin du manifeste** : deux sorties, « J'adhère » et « Propositions → », puis « Télécharger en PDF ».

## 2. Quatre pages neuves

Forme : `fiche.css`, Archivo aux titres et petites capitales, Source Serif 4 au texte. Barre de retour en haut comme les autres pages intérieures. Aucun texte ajouté ni reformulé : ce qui suit est verbatim.

**`livre.html` — Le livre.** Couverture en image. État partout, justice nulle part. Ingrid Barrat, Arthur Marle, Moïse Mitterrand. Éditions Chronique. 9,90 €. ISBN 978-2-36-602648-1. En librairie le 9 octobre 2026. Bouton « Précommander le livre », même lien Amazon que la garde, même style. Quatrième de couverture en image.

**`auteurs.html` — Auteurs.** Photo des trois auteurs. Trois blocs, dans cet ordre : Ingrid Barrat, Arthur Marle, Moïse Mitterrand. Chaque bloc porte deux phrases : la ligne d'éditeur de la quatrième de couverture, **transcrite verbatim depuis l'image jointe** — tu la rends en clair dans ta réponse pour contrôle ; puis, telle quelle :
— Barrat : « Elle a mis le projet en musique. »
— Marle : « Son intuition est à l'origine du projet. »
— Mitterrand : « Il préside Résolution et porte le projet. »
Rien d'autre.

**`donnees.html` — Données.** Une ligne d'introduction : « Les classeurs qui fondent le plan, tels que nous les avons travaillés. » Puis les sept fichiers, chacun avec son lien de téléchargement et son descriptif :
- **Synthèse Calculs** — le chiffrage du plan : économies, niches, refonte de la fiscalité, CSG-CRDS, capitalisation.
- **Synthèse ETP et agences** — effectifs publics par versant ; opérateurs et ODAC-ODAL un par un, avec le sort proposé pour chacun.
- **Synthèse Graphiques** — les douze séries qui nourrissent les graphiques, sources en tête d'onglet.
- **Dépenses des collectivités par fonction** — tableau Insee 3.305 des administrations publiques locales, périmètre non indispensable identifié par Résolution.
- **Taxes affectées** — l'annexe du PLF 2026 retraitée : taxe par taxe, bénéficiaire, suppression proposée et économie.
- **Dépenses fiscales** — l'annexe du PLF 2026 retraitée : les 470 niches chiffrées une à une, typologie d'économie, échéances, bénéficiaires.
- **Dépenses de l'État 2026** — les crédits du PLF par mission et programme, retraités : hypothèses de restitution et économies par catégorie de dépense.
Les fichiers sont servis tels que joints, sous `donnees/`, noms conservés.

**`mentions-legales.html` — Mentions légales.**
Éditeur du site : association Résolution, association déclarée n° 991 580 622, siège 113 avenue de Verdun, 92130 Issy-les-Moulineaux. Contact : contact@france-resolution.fr.
Directeur de la publication : Moïse Mitterrand, président.
Hébergeur : Vercel Inc., 440 N Barranca Ave #4133, Covina CA 91723, États-Unis.

## 3. La garde

Hero inchangé — titre, promesse, « C'est possible, par ici → » vers `manifeste.html`, palette, corps.

- **En haut à droite, un seul bloc, le livre**, dans cet ordre : *Le livre* (→ `livre.html`), *Précommander le livre* (or plein, lien Amazon inchangé), *En librairie le 9 octobre* (petit). Il se lit comme une unité. *J'adhère* et *Je m'exprime* quittent le haut.
- **La bande**, en pied de hero, cinq onglets, sans déterminant, dans cet ordre : **Manifeste · Propositions · Données · Vidéos · Auteurs**. Elle ne porte plus la date. **Les onglets deviennent plus visibles qu'aujourd'hui** — corps ou graisse d'un cran, depuis les variables existantes — en miroir des actions qui s'atténuent.
- **Pied de page**, nouveau : *Je m'exprime* (→ `contact.html`) · *J'adhère* (→ `adherer.html`) · *Mentions légales* (→ `mentions-legales.html`). Je m'exprime en premier ; J'adhère moins visible ; Mentions légales le moins visible.

## 4. Toutes les pages intérieures

Deux lignes identiques partout : la barre de retour (marque à gauche, les cinq onglets), et le pied de page du point 3. Plus aucune action qui n'existe que sur la garde.

**Les fiches perdent trois renvois** : « Sommaire » (l'onglet Propositions le fait), les fiches sœurs listées dans le corps (précédent/suivant suffit), le second « Résolution » du pied (la marque est déjà là). Une fiche garde : barre commune, précédent/suivant, PDF, pied commun.

## 5. Quatre registres, aucun composant neuf

| registre | éléments | repris de |
|---|---|---|
| action | Précommander | l'or plein actuel, seul aplat de la page |
| accroche | « par ici → » | bouton filaire or |
| navigation | cinq onglets, « Le livre » du bloc haut | capitales espacées crème actuelles, montées d'un cran |
| service | Je m'exprime · J'adhère · Mentions légales · la date | petit, souligné or (l'actuel Je m'exprime) ; date en crème atténué |

L'ordre des poids ne s'inverse jamais. Toute valeur vient de `fiche.css` ; aucune inventée ni approchée. Mobile : le bloc livre passe sous la marque, la bande sur deux lignes si besoin, le pied en dernier.

## 6. Rendu, et arrêt

Planche avant/après de la garde à 1440, 1024, 768 et 390 ; capture de chacune des quatre pages neuves ; capture du manifeste (tête et fin) ; capture d'une fiche avec sa barre et son pied. La transcription des trois lignes de la quatrième, en clair. Tu soumets et tu t'arrêtes. **Rien n'est branché, rien n'est sur `main`, rien n'est déployé avant validation.**
