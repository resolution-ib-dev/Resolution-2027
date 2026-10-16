# Élargissement du dépôt de droit — pièce de préparation

Écrite le 20261016 par le fil Cowork « sièges des prélèvements ».
**Rien n'est joué ici** : un fil Cowork ne pousse pas. Cette pièce dit quoi
ajouter, où, et ce que l'ajout ferme.

---

## Correction du dimensionnement annoncé

Le plan du fil annonçait « douze lignes hors dépôt, cinq textes à ajouter ».
**Mesuré, c'est faux.** Sur les 17 lignes encore non établies, **trois seulement**
attendent un texte que le dépôt ne porte pas. Les autres relèvent de deux causes
différentes, qui n'appellent pas un élargissement.

| cause | lignes | ce qu'il faut |
|---|---:|---|
| le code n'est pas porté par le dépôt | 3 | l'élargissement ci-dessous |
| le code est porté, l'article manque à l'extrait | 4 | complément de l'extrait, matière des droits de timbre |
| le code est porté et la recherche a échoué | 8 | ouvrir la division, pas élargir |
| hors LEGI par nature | 2 | une détermination, pas une recherche |

**La part qui revient à l'élargissement est donc de trois lignes sur dix-sept.**
Le reste est du travail de relevé, et l'annoncer autrement aurait reporté sur
l'auteur le coût d'une erreur de mesure.

---

## 1. Les trois textes à ajouter à `depot/codes.json`

L'entrée est un objet à quatre champs — `cle`, `legitext`, `court`, `temoin`.
Le témoin est l'article que `extraire_legi.py` exige de retrouver : sans lui,
le script échoue plutôt que d'écrire un fichier vide.

| code | `legitext` | `court` | témoin proposé | ligne du tri qu'il ferme |
|---|---|---|---|---|
| code de la sécurité intérieure | `LEGITEXT000025503132` | `securite_interieure` | `L321-1` | Sommes constatées par les clubs de jeux au titre des « orphelins » |
| code de la route | `LEGITEXT000006074228` | `route` | `L221-1` | Redevance pour examen du code de la route |
| code des postes et des communications électroniques | `LEGITEXT000006070987` | `cpce` | `L33-1` | Taxes sur les stations et liaisons radioélectriques privées |

**Les trois identifiants sont relevés sur les adresses de Légifrance, non
mémorisés.** Les témoins, eux, sont *proposés* : ils n'ont pas été rouverts,
puisque le dépôt ne porte pas encore ces textes. Le fil qui joue l'ajout les
confirme à la première extraction, et les corrige si l'un ne mord pas — **un
témoin qui ne mord pas ne prouve rien sur le code, il prouve que le témoin ne
mord pas.**

Après ajout, `extraire_legi.py` tourne dans l'action programmée du dépôt, non
dans l'atelier. `droit.py etat` doit alors porter 77 textes au lieu de 74.

## 2. Le complément de l'extrait du code général des impôts

**Mesuré le 20261016** : `depot/data/cgi.jsonl.gz` porte 2 584 articles
distincts, 2 408 applicables, sur deux livres. Vingt-neuf plages de huit numéros
ou plus y manquent. La plage **901 à 952** est la matière des droits de timbre,
et c'est elle qui bloque quatre lignes du tri — timbre unique, timbre de
dimension, actes judiciaires et extrajudiciaires, taxe sur les émoluments.

Ce n'est pas un ajout de code : le code général des impôts est déjà porté. C'est
une **mesure de couverture à instruire sur `extraire_legi.py`** — pourquoi des
plages entières d'un code porté n'entrent pas. Tant qu'elle n'est pas faite,
**« absent de l'extrait » ne s'écrit jamais « abrogé »**.

## 3. Ce que l'élargissement ne ferme pas

Huit lignes vivent dans un code **déjà porté** et n'ont pas rendu leur siège :
financement du CIF-CDD, contribution IRSN, taxe des laboratoires de biologie
médicale, majoration de la taxe sur les assurances de protection juridique,
participation pour non-réalisation d'aires de stationnement, taxe additionnelle
au droit de bail, redevance proportionnelle des concessions hydroélectriques à
délais glissants, contributions de la SNCF pour frais de surveillance.

Pour celles-là, l'élargissement ne sert à rien. Ce qu'il faut est le geste du
septième garde-fou : **ouvrir la division du code qui porte la matière**, et non
chercher le mot. Trois d'entre elles sont peut-être éteintes plutôt
qu'introuvables — le CIF-CDD, la taxe additionnelle au droit de bail et la
contribution IRSN ont toutes trois été remplacées par un autre dispositif ; cela
se relève, comme la garantie des matières d'or, et cela s'inscrit.

Deux lignes enfin sortent de LEGI par nature et ne se ferment que par une
détermination de l'auteure : la cotisation interprofessionnelle étendue
« Équarrissage », qui est un accord étendu par arrêté, et la participation des
concessionnaires de la liaison fixe Trans-Manche, qui procède du traité
franco-britannique.
