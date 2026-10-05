*Reprise de lisibilité demandée par l'auteure sur la liste du PLFSS 2027. Jugée sur
le rendu regardé, pas sur le markdown : le PDF a été converti en image et lu.
Quatre défauts constatés, quatre règles portées au gabarit et au script — nulle part
ailleurs.*

**1. La clé de lecture était l'endroit le plus illisible de la page.** La légende
des poids courait en paragraphe justifié, pastilles de 3,2 px collées les unes aux
autres au milieu du texte. **Elle devient un tableau de quatre lignes**, au même
traitement que le tableau « annoncé / écrit ».

**2. Le fait et le commentaire avaient le même poids.** Tout sortait en 10 pt noir,
y compris les remarques en italique, qui font souvent la moitié d'une ligne
d'article. **L'italique passe en 9,2 pt gris `#3a3a3a`.** C'est le gain le plus
fort : le lecteur pressé lit les faits en noir et saute le reste, l'autre lit tout.
*Les titres de section et le sous-titre sont exemptés, sans quoi ils rétrécissaient
avec.*

**3. Les pastilles n'étaient pas décodables, et `●` seul était invisible.**
Disques portés de 3,2 à 4,2 px, espacés de 1,8 px, gris foncés de `#b4b4b4` à
`#8c8c8c` pour le poids simple, cercle vide bordé `#555`. Colonne élargie de 4,6 à
6 mm.

**4. Le texte entre accents graves sortait en chasse fixe.** `au texte` et
`annexe A` tombaient en police à chasse fixe au milieu d'un Times, par simple défaut
de la feuille de style. `code, tt, kbd, samp { font-family: inherit; font-style:
italic }`.

**Plus deux réglages de confort** : articles séparés de 2,8 mm au lieu de 1,4, et
`hyphenate-limit-chars: 6 3 3` pour interdire les coupes à deux lettres. Et deux
intertitres dans le chapeau — `## Les grandeurs`, `## Comment lire cette liste` —
sans quoi six paragraphes de même gris se lisent comme un mur.

**Coût : une page.** De 5 à 6 pages. L'air est le prix de la lisibilité, et il est
payé une fois pour tous les millésimes.

**Un faux défaut, inscrit pour ne pas être « corrigé » plus tard.** Au rendu en
image, `Md€` paraît collé au mot suivant. L'espace est bien présente : vérifiée en
extrayant le texte du PDF. Le contrôle d'une espace se fait sur le texte extrait,
jamais à l'œil sur une capture.

**Rien n'a été porté dans un troisième endroit.** Le gabarit `reference/gabarit_liste_articles.md`
et `livrables/rendre_liste_pdf.py` ont bougé ensemble, comme le gabarit l'exige. Le
script étant partagé, **les quatre règles valent aussi pour la liste du PLF 2027 à
son prochain rendu** — sans qu'il faille y toucher.
