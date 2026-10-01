# Dépôt de droit — le texte en vigueur comme source déclarée

Le chantier a besoin du **verbatim** des articles qu'il modifie. Légifrance
refuse la lecture directe depuis l'atelier — neuf tentatives, un succès et huit
`403`, sur les pages d'article comme de section et de texte consolidé. Recopier
à la main ne s'industrialise pas.

Ce dépôt résout le problème par la voie que le corpus prévoit déjà : **le droit
devient une source déclarée de la session**, au même titre que le manuscrit ou
les classeurs. Une action programmée extrait les codes utiles de la base LEGI de
la DILA, les range ici, et chaque fil les lit hors ligne.

Aucune clé, aucun compte, aucun quota. La base LEGI est publiée en open data.

---

## Installation — trois gestes, une fois

1. **Poser ces fichiers dans un dépôt GitHub.** Soit un dépôt dédié, soit
   `resolution-ib-dev/Resolution-2027`, ce qui évite une déclaration de plus.
2. **Déclarer ce dépôt aux sources de la session Claude.** Sans cela le proxy
   git de l'atelier rend `403 access denied by the git proxy` et rien ne se
   clone — c'est établi par A-196 et cela ne se contourne pas, pas même avec un
   jeton.
3. **Onglet Actions → « Rafraîchir le droit en vigueur » → Run workflow.**
   Compter une à deux heures pour le premier passage : l'archive complète est
   volumineuse et se balaie en flux.

Ensuite l'action se rejoue seule le 1er de chaque mois, et à chaque
modification de `codes.json`.

## Emploi depuis un fil

```bash
git clone https://github.com/<compte>/<depot> droit
python3 droit/droit.py etat
python3 droit/droit.py article "code général des impôts" 279
python3 droit/droit.py article cgi "278 sexies-0 A"
python3 droit/droit.py article cgi 279 --au 2025-06-01
python3 droit/droit.py section cgi "Taux réduit"
python3 droit/droit.py verifier mes_vecteurs.json
```

Depuis un script :

```python
import droit
a = droit.article("code de la sécurité sociale", "L. 136-8")
print(droit.rendre(a))          # gabarit de l'étape 1 de redaction-legistique
```

`mes_vecteurs.json` est de la forme `{"code général des impôts": ["279", "235 bis"]}`
et rend, par adresse, `trouvé` · `abrogé` · `absent`.

`--au AAAA-MM-JJ` lit l'article tel qu'il s'appliquait à cette date passée,
plutôt que la version en vigueur aujourd'hui — c'est ce qu'un trois colonnes
demande pour sa colonne « texte en vigueur » sur un article déjà modifié par
le texte en discussion. Sans `--au`, le jour courant.

## Ce que le lecteur refuse, et c'est le point

Trois refus tenus par le code et non par la discipline :

- **aucun article ne sort sans son identifiant et sa date de version** ;
- **un article abrogé lève**, avec ses états, plutôt que de rendre son texte ;
- **un article absent lève** — jamais d'appariement au plus proche (A-94), jamais
  de texte approchant.

S'y ajoute la fraîcheur : le millésime de l'extrait est porté dans chaque sortie,
et au-delà de 45 jours la mention `À REJOUER` s'imprime d'elle-même. C'est la
règle du vecteur périmé de `vecteur-mesure`, appliquée au texte.

## Les textes portés

Ils vivent dans `codes.json`, et nulle part ailleurs. L'extrait ne porte plus
seulement des codes : il porte aussi les textes non codifiés — lois, lois de
finances, ordonnances — que la base LEGI publie à côté des codes.

Une entrée s'y résout par l'une de deux voies :

- **par identifiant**, quand l'entrée porte un champ `legitext` — c'est le cas
  des vingt premiers codes, dont l'identifiant Légifrance a été relevé une
  fois pour toutes ;
- **par intitulé exact**, sinon — `extraire_legi.py` cherche `cle` dans les
  métadonnées de chaque texte consolidé de l'archive **elle-même** : rien ne
  se cherche sur le web, aucun identifiant ne se saisit à la main. Un
  intitulé introuvable, ou qui résout vers plusieurs textes, fait échouer
  l'extraction en le nommant plutôt que de s'approcher du voisin le plus
  proche (A-94) ou de laisser le corpus choisir à sa place.

**Ajouter un texte** : une entrée dans `codes.json` — `legitext` pour un code
dont l'identifiant est déjà connu, ou seulement `cle` (l'intitulé exact),
`court` et `temoin` pour tout le reste — un commit, et l'action repart seule.

**Le volume de l'extrait est borné à 60 Mo.** Un texte ajouté qui ferait
dépasser cette limite n'est pas versé : il est déclaré dans
`data/_manifeste.json`, sous `non_verses`, avec son motif — jamais versé au
hasard, toujours dans l'ordre où les entrées apparaissent dans `codes.json`.
Les vingt premiers codes ne sont jamais concernés par cette limite.

## Ce qui n'est pas vérifié, et qui échouera bruyamment

Je n'ai pas pu ouvrir l'archive LEGI depuis l'atelier. **La disposition interne
du dump est donc présumée, pas constatée.** Le script en tient compte :

- il ne code en dur ni l'adresse de l'archive ni aucun chemin — il interroge
  l'API de data.gouv.fr et balaie l'archive ;
- il repère les articles par nom de balise et non par chemin fixe ;
- **si un code rend zéro article, il n'invente rien : il écrit
  `data/_diagnostic.json` avec un échantillon de chemins réels et il échoue.**

Si le premier passage échoue, le diagnostic est joint aux artefacts de l'action
et la correction tient en un commit. C'est le mode de défaillance voulu : mieux
vaut un job rouge qu'un extrait silencieusement vide.

## Épreuve à blanc

`python3 essai.py` monte un extrait factice et exerce 15 contrôles : lecture
du XML LEGI, article, structure et métadonnées de texte ; résolution par
intitulé — un texte non codifié, un code (l'identifiant du dossier `texte/`
retenu, jamais celui du fichier lu), un texte introuvable qui échoue en se
nommant ; lecture par libellé exact et par nom court ; normalisation de la ponctuation
d'un numéro sans jamais couper un suffixe ; présence de l'identifiant, de la
date et du millésime en sortie ; les trois refus ; la recherche par titre de
section ; la détection d'un extrait périmé. Elle passe, et elle ne prouve rien
sur le dump réel.

## Ce que ce dépôt ne fait pas

Ni jurisprudence, ni doctrine, ni textes réglementaires au-delà de ce que les
codes portent. Ni API PISTE : elle demanderait un compte et deux secrets pour
un service que LEGI rend sans clé. Et il ne porte **pas** le texte déposé du PLF
ou du PLFSS — c'est une autre source, qui entre par pièce jointe, et c'est la
brique qui reste ouverte.
