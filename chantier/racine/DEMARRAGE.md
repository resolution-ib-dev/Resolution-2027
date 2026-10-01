# Démarrage

Trois choses à faire, une seule fois. Tout est déjà en place dans ce dossier.

## 1. Installer Claude Code

Ouvrir le Terminal.

Sur Mac, appuyer sur `Cmd + Espace`, taper « terminal », entrée.
Sur Windows, ouvrir « Terminal » depuis le menu Démarrer.

Coller cette ligne, entrée :

    curl -fsSL https://claude.ai/install.sh | bash

Sur Windows, coller celle-ci à la place :

    irm https://claude.ai/install.ps1 | iex

Fermer le Terminal, le rouvrir. Taper `claude --version` : un numéro doit
s'afficher. Si rien ne s'affiche, taper `claude doctor`, qui dit ce qui manque.

## 2. Se placer dans ce dossier

Toujours dans le Terminal, taper `cd ` — avec l'espace — puis faire glisser ce
dossier depuis le Finder ou l'Explorateur dans la fenêtre du Terminal. Le chemin
s'écrit tout seul. Entrée.

## 3. Lancer

    claude

À la première ouverture, une page s'ouvre dans le navigateur pour se connecter
avec le compte Claude.

Puis coller cette première instruction :

    Lis CLAUDE.md, methode/ETAT_DU_CHANTIER.md et methode/prompt_fil_courant.md.
    Joue make controle. Dis-moi où on en est, en français, sans jargon.

---

## Ce qui change

Les fichiers ne se téléchargent plus et ne se réattachent plus. Ils sont ici, et
Claude les modifie sur place.

Une commande refait tous les documents à partir des données :

    make

Pour voir un document, double-cliquer sur le fichier dans `livrables/` : il
s'ouvre dans le navigateur.

Pour revenir en arrière sur une modification, le demander à Claude : l'historique
est conservé automatiquement.

## Ce qu'il y a dans les dossiers

| dossier | ce qu'il contient |
|---|---|
| `manuscrit/` | le manuscrit — la référence, jamais modifiée |
| `referentiels/` | les données : doctrine, positions, notes |
| `appareil/` | les programmes qui fabriquent les documents |
| `livrables/` | les documents produits, à ouvrir dans le navigateur |
| `methode/` | l'état du chantier, les règles, le fil en cours |
| `sources/` | classeurs, textes, documents de référence |

## Une pièce à récupérer

La couverture du livre n'est pas ici. Elle est nécessaire pour la charte
graphique définitive. La déposer dans `sources/` quand elle sera disponible.

`generer_arbre.py`, donné pour perdu, est revenu : il est dans l'archive
technique et l'arbre se régénère.
