# Passation — le site : le fond au coffre, la forme au dépôt

Écrit le 20260904 par le fil du site. À lire par tout fil qui touche au site.

---

## Le partage, arrêté par l'auteur le 20260904

**Le fond ici, la forme au dépôt du site.** Un chiffre, un gain, une perte,
l'ordre des fiches, l'axe d'une fiche : cela se corrige au référentiel du
coffre. Une couleur, une police, une grille, une page nouvelle, un
enchaînement : cela se corrige au dépôt.

La couture est un seul fichier : **`referentiels/donnees_site.json`**, la
surface publiée, résolue et sans mise en forme. `appareil/exporter_site.py` la
produit ici depuis les positions et le `REF_doctrine` ;
`appareil/generer_site.py` ne lit plus qu'elle. **Un seul chemin de code rend
les pages, ici comme au dépôt** : les deux ne peuvent pas diverger.

Prouvé au moment de la refonte : le `site/` régénéré par la nouvelle chaîne est
**identique à l'octet** à celui de l'ancienne, sur les 27 fichiers.

Ce que l'export ne porte pas : le `REF_doctrine`, le manuscrit, les notes, les
ancrages doctrinaux, ni les avertissements de travail du proto du manifeste —
seul son article part. Il porte les identifiants d'ancrage, dont le rendu a
besoin pour les rappels ; ils ne paraissent dans aucune page.

**Une entorse connue, à reprendre** : `appareil/manifeste.py` porte à la fois le
rendu du manifeste et ses corrections de contenu (le compte d'agences, les
montants). Les corrections sont du fond et vivent donc, pour l'instant, au
dépôt avec la forme.

---

## Ce qui est fait

**Le site est en ligne** — `site-etnp.vercel.app`, poussé au dépôt
`resolution-ib-dev/Site-ETNP`, servi par Vercel depuis `site/`.

**La typographie est celle du livre** : `--titre` et `--chif` valent Archivo,
`--texte` vaut Source Serif 4 — Archivo aux titres, aux petites capitales et
aux chiffres, Source Serif au texte courant. La variable `--mono` est renommée
`--chif` partout, puisqu'elle ne porte plus de mono.

**Corrigé le 20260904, sur relevé de l'auteur** :

- l'accueil ne porte plus que la garde ; le sommaire des dix-huit a son adresse,
  `fiches.html` ;
- les liens des fiches résolvaient dans `fiches/` et tombaient sur la page
  d'erreur — ils voient maintenant la racine ;
- la page d'erreur porte des chemins absolus : elle répond de n'importe où,
  habillée ;
- fiche consommateur : l'axe devient « Plus de concurrence, plus de choix, plus
  de pouvoir d'achat », et la vedette 81 % « Les produits faits en France que
  vous consommez deviennent plus abordables » — la promesse de baisse
  d'étiquette était trompeuse.

**Reste signalé, non tranché** : sur la même fiche, la ligne *Le choix* dit
encore « et à meilleur prix ».

---

## Le dépôt autonome, et comment le site se maintient

Le paquet livré à l'auteur porte : `appareil/` (les quatre modules de rendu),
`referentiels/donnees_site.json`, `site/` rendu, `vercel.json`, un `Makefile`
réduit, un `README.md`, et **`.github/workflows/site.yml`**.

**L'automate** : toute poussée touchant `appareil/` ou `referentiels/`
régénère `site/`, le commet et pousse ; Vercel redéploie. `site/`, `vercel.json`
et le README sont ignorés au déclenchement, pour qu'il ne se rappelle pas
lui-même.

**Régime de croisière** : la forme se travaille depuis une session attachée au
dépôt — l'interface `claude.ai/code`, où `Site-ETNP` et `Resolution-2027` sont
sélectionnables. Le fond se travaille ici, et un export rejoué se pousse quand
la doctrine bouge.

---

## Le mur, pour mémoire

**Un seul hébergeur est joignable depuis l'atelier : GitHub** — Vercel, Netlify,
Cloudflare, GitLab, Bitbucket, Gandi, Codeberg refusés par le proxy.

**Et depuis Cowork, aucune écriture Git n'est possible**, sur aucun dépôt : le
proxy refuse la poussée hors de l'ensemble autorisé de la session, et cet
ensemble se fixe au démarrage, par un sélecteur de dépôt **qui n'existe pas
dans Cowork**. Aucun jeton n'y change rien — trois ont été essayés, tous
valides, tous refusés. La lecture, elle, passe partout.

*Règle qui en sort* : **ne jamais conclure de la lecture à l'écriture**, et
vérifier où l'on peut écrire avant de promettre une publication.

---

## L'état du courriel et du domaine, relevé au DNS

Domaine enregistré, DNS chez Gandi, courriel routé vers Microsoft 365 sur le
tenant de l'organisation de l'auteur, SPF correct, DKIM signé.
`contact@france-resolution.fr` existe. **Aucun DMARC** : à poser en TXT sur
`_dmarc`, `v=DMARC1; p=none; rua=mailto:contact@france-resolution.fr; fo=1`.

L'adresse de contact vit à un seul endroit, `CONTACT` dans `generer_site.py`.

**Reste à faire par l'auteur** : brancher le domaine dans Vercel (*Settings →
Domains*), puis coller chez Gandi les deux enregistrements que Vercel affiche —
les MX ne bougent pas. Et révoquer les trois jetons GitHub collés en
conversation, sans emploi.
