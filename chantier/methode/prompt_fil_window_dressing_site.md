# Prompt — fil window dressing du site (20260923)

*Cible : session `claude.ai/code`, dépôt `resolution-ib-dev/Site-ETNP` sélectionné.
Cette session ne voit pas le projet Résolution : tout ce qui suit est verbatim.*

---

Fil window dressing du site. Dépôt `resolution-ib-dev/Site-ETNP` seul.

**Règles de conduite, applicables à ce fil.**
Tout mandat de correction commence par une mesure : tu localises l'objet avant de
le toucher. Si la mesure sort vide — l'objet annoncé n'est pas là —, tu rends le
nombre mesuré et tu t'arrêtes ; tu ne cherches pas ailleurs, tu n'élargis pas ton
périmètre, tu ne joues aucun contrôle. Tu ne produis que les pièces nommées
ci-dessous : aucune page nouvelle, aucun fichier nouveau, même s'il paraît utile.
Forme du site : `fiche.css`, Archivo (titres, petites capitales, chiffres) et
Source Serif 4 (texte courant) ; le site fait foi, les pièces neuves suivent le
site. Ta réponse finale est courte et activable, sans récit de méthode.

**Trois choses, et rien d'autre.**

1. **Retirer `resolution_une_page.html`.** La page est servie mais liée de nulle
   part. Tu la retires du dépôt et tu vérifies qu'aucun lien entrant ne subsiste
   (recherche sur l'ensemble du dépôt). *Arbitrage de l'auteur du 20260923 :
   retrait, pas raccrochage.*

2. **Supprimer « et à meilleur prix »** sur la fiche consommateur, ligne
   *Le choix*. Suppression de ces quatre mots seuls ; la phrase se relit et se
   reponctue si la suppression la laisse bancale, sans autre réécriture.
   *Signalé le 20260904, tranché le 20260923.*

3. **Relever l'arborescence du site telle qu'elle est**, et la rendre en clair
   dans ta réponse — pas de fichier. Quatre choses :
   - les pages effectivement servies (chemin, titre) ;
   - les entrées de la barre de navigation, dans l'ordre, et la page que chacune
     ouvre ;
   - pour chaque page servie, si elle est liée depuis la barre, depuis une autre
     page, ou depuis nulle part ;
   - l'état du manifeste en ligne : `manifeste.html` et `manifeste.pdf`
     portent-ils bien le texte révisé du 20260923 (606 mots), et le PDF est-il
     accessible depuis la page ?
   Ce relevé arme le fil suivant, qui tranchera l'arborescence cible. Tu ne
   proposes aucun plan, tu ne réorganises rien.

**Ce que tu ne fais pas.** Aucune page nouvelle — « Le livre », « Les auteurs »,
« Mentions légales » ne s'écrivent pas dans ce fil, leur place n'est pas tranchée.
Aucun graphique, aucune carte, aucune notice. Aucune réécriture de contenu au-delà
des quatre mots du point 2.

**Sortie.** Tu commites et tu pousses sur `main` les points 1 et 2 — ce sont deux
retraits, ils vont en ligne. Le point 3 se rend en clair dans la conversation.
