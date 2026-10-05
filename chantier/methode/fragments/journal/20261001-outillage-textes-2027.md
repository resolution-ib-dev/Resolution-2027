**Mandat.** Outiller la machine sur les textes 2027 comme elle l'avait été sur
2026 — produire, au schéma du millésime 2026, ce que la chaîne consomme.

**Ce qui est fait.**

`appareil/socle_texte_2027.py` — le socle des deux véhicules depuis le PDF
déposé. Une entrée par article : numéro, partie, intitulé, rédaction exacte,
folio imprimé, exposé des motifs rattaché. **PLF 2027 : 90 articles**, liminaire
plus 1 à 89, 57 en première partie et 32 en seconde, folios 33 à 268.
**PLFSS 2027 : 49 articles**, liminaire plus 1 à 48, sur trois parties, folios 1
à 112. Aucun article sans intitulé, sans dispositif ni sans exposé.

`appareil/portes_ouvertes.py` — le module que l'index déclarait manquant. Il
rend `referentiels/articles_ouverts_<véhicule>2027.tsv` au schéma de 2026, celui
qui alimente la colonne `variante` de `REF_norme`. **PLF : 449 adresses,
56 textes. PLFSS : 191 adresses, 23 textes** — et c'est le premier relevé de
portes jamais fait côté loi de financement, 2026 compris n'en ayant qu'un pour
chaque véhicule.

`appareil/pieces_nommees.py` — la table close des pièces, neuve.

**Contrôles joués, tous mécaniques.** Déterminisme du socle et du relevé : deux
exécutions, même empreinte. Couverture : aucun numéro d'article manquant sur les
deux véhicules. Jeu de fautes sur le socle — article retiré, dispositif vidé,
folio cassé : les trois levés. Jeu de justes sur le blanchiment — un siège cité
entre guillemets n'en ressort pas ; un siège modificatif y survit.

**Ce qui reste ouvert.** Les blocs L1 à L4 ne sont pas joués. Le module
`controle_socle_plf.py` n'est pas écrit. L'attribution de pièce porte le défaut
du millésime 2026 et il est déclaré au fragment d'arbitrages du jour. Les deux
socles pèsent 1,27 Mo et 344 ko : ils restent à l'atelier, le coffre ne reçoit
que les modules et les deux référentiels.

**Dépôt.** Les trois modules sont de voie `depot` et un fil Cowork ne pousse
pas : ils attendent une session `claude.ai/code`, avec le paquet de courroies du
jour qui n'a pas abouti.
