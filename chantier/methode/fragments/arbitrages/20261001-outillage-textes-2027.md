*Tambouille tranchée par le fil d'outillage des textes 2027. Trois décisions
d'appareil, chacune imposée par une divergence mesurée.*

## Une pièce nommée ne se devine pas : elle se reconnaît sur table close

La reconnaissance du nom de pièce par expression régulière a été reprise trois
fois et a échoué trois fois : elle tronquait les noms longs — « code des
impositions sur les biens » pour « … sur les biens et services », « code des
pensions civiles » pour « … civiles et militaires de retraite » — et elle en
fabriquait — « code propriétés non bâties », « code général des taxe spéciale ».
Mesure au moment de la bascule : **222 adresses relevées contre 424** au relevé
qui fait foi, et huit textes entiers à zéro.

**Décision.** `appareil/pieces_nommees.py` porte une **table close** des codes,
reconnue au plus long libellé, apostrophe droite ou courbe indifférente. Les
lois, ordonnances et décrets gardent leur forme régulière : leur numéro et leur
date les identifient sans ambiguïté. Un libellé « code … » qu'aucune entrée ne
couvre se **déclare** par `non_reconnues()` et se verse à la table — il ne se
devine jamais au vol.

## Le guillemet français ne s'imbrique pas

C'était la faute lourde, et la table close ne l'a pas corrigée parce qu'elle
n'en était pas la cause. Le blanchiment des passages cités comptait la
profondeur d'imbrication. Or la légistique rouvre un `«` à chaque alinéa inséré
sans fermer le précédent : l'article 19 du PLF 2027 porte **78 ouvrants pour 75
fermants**. Le compte de profondeur ne retombait jamais à zéro et blanchissait
tout le reste de l'article — **11 669 octets de dispositif ramenés à 492**, et
ses trente sièges avec.

**Décision.** Un `«` se referme au `»` suivant, quels que soient les `«`
intermédiaires. Un `«` jamais refermé ne blanchit que jusqu'à la fin de sa
ligne. Effet mesuré, à table close inchangée : **221 → 449 adresses** côté PLF,
**78 → 191** côté PLFSS.

*La règle 6 de la grammaire de relevé est donc à lire ainsi : le blanchiment
traverse les lignes, il préserve les offsets, et **il ne compte pas la
profondeur**.*

## Le folio contre le sommaire, remesuré

L'écart entre le sommaire imprimé du PLF 2027 et le folio réel est **nul à
l'article 1 et atteint +21 à l'article 89**, croissant tout du long. La règle 1
de la grammaire tient, et le relevé des portes, fait au folio, est bon.

## Ce qui est déclaré et non corrigé

L'attribution de la pièce prend celle que la même phrase nomme après l'adresse,
à défaut la dernière déclarée avant elle. Quelques adresses du code de la
sécurité sociale sortent sous « code de la santé publique » quand une phrase
nomme les deux. **Le défaut est celui du millésime 2026**, dont le référentiel
porte les mêmes lignes et un bloc `indéterminé`. Il se corrige par une table de
familles d'adresses — `L. 16x` au code de la sécurité sociale — et ce n'est pas
de ce fil.

Le relevé rend **449 adresses côté PLF contre 424** au relevé qui fait foi.
L'écart tient aux énumérations — « les articles L. 1, L. 2 et L. 3 », dont seul
le premier était capté — et aux **31 adresses que le relevé qui fait foi déclare
lui-même « à vérifier »** comme renvois et non sièges. La confrontation par
texte tombe à moins de dix lignes près sur les huit têtes.
