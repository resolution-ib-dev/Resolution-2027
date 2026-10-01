# Ce qui est sorti du projet — 20261001

*Registre des sorties. Un document sorti du projet n'est pas perdu : il vit à
l'archive et se redemande. Ce fichier est la seule table qui dit où.*

## Où vit l'archive

**`coffre_resolution_20261001.tar.gz`**, remis à l'auteure dans le fil du
20261001. 173 documents, copie d'octets depuis le transcript de session, sans
repasser par le modèle. **L'empreinte de l'archive ne s'écrit pas ici** : ce
document est dedans, et l'y citer ferait une boucle. Elle est rendue à l'auteure
dans le fil, et le contrôle qui compte est la relecture du manifeste.

Elle porte `MANIFESTE_ARCHIVE.txt` : sha256, taille et chemin de chacun des 173
documents. Relecture de l'archive après écriture : **173 conformes, 0 divergent,
0 absent.**

Elle porte l'état **final** du 20261001 : `methode/journal.md` et
`methode/arbitrages.md` rebâtis, `methode/index.json` à 363 artefacts,
`methode/empreintes.json` à 246 empreintes, le socle corrigé, et ce registre
lui-même. Elle ne porte pas `chantier/appareil/` ni les cinq référentiels JSON,
qui sont de voie `depot` et reviennent par `git clone`.

**Le dépôt ne porte toujours pas le coffre.** La poussée a été refusée par le
mandataire git — `resolution-ib-dev/Resolution-2027` n'est pas aux sources
autorisées de la session. Le commit d'archive existe en atelier
(`6559a6b`, branche `coffre-20261001`) et sera perdu avec lui. **Tant que le
dépôt n'est pas déclaré aux sources du projet, l'archive remise à l'auteure est
le seul exemplaire durable.**

## Les 15 documents sortis

Tous présents à l'archive, empreinte vérifiée avant sortie.

| document | octets | sha256 |
|---|---:|---|
| `methode/arbitrages_archive.md` | 243 539 | `a757463a5c37f717a9f7361ba7574e960125c64840d975827080057d358da255` |
| `livre/texte_livre.json` | 311 829 | `2d3854998e6b01d3ec45f320ec8eec3ad9f6d84d11eb579150adad349d5a0a9c` |
| `referentiels/prelevements_forces_20260930.tsv` | 207 773 | `13faa2a746c04fd1978928bfd80a2a310fe20c8274388bf95812f52ede86ae64` |
| `referentiels/cgi_expert_suppressions.tsv` | 136 606 | `133e009537b870725ab89a7e01ec6133d080a804813fbd5178f0b52d053ee292` |
| `referentiels/cgi_expert_articles.tsv` | 100 381 | `8448b4cf4292c84127fe1bdce77a1b64ef2e34c43a1bca74933a76a99f4ebafe` |
| `referentiels/cgi_expert_insertions.tsv` | 61 603 | `bb2722e16798146fc8030d66e0d8e395b41c142111c298f8bb8d3b9166fe09b8` |
| `referentiels/cgi_expert_articles_bouges.tsv` | 34 681 | `c4d0ad8d1ec43d734fbd789f1399149452f2ea96cf6424f268dc54c7734e575d` |
| `referentiels/cgi_expert_parametres.tsv` | 7 497 | `157742ece38f0c239a273790297d6b668488c7e0624102a9af52f7475668e0ec` |
| `livrables/releve_epreuve_EP2.tsv` | 95 095 | `bdf2c372740fe9dc488fecee21fe86356436c6b586748880e7ef61da3313e176` |
| `livrables/releve_epreuve_EP3.tsv` | 59 150 | `25b0e1cc1b31ea4fa603e3e3884655873e14c47415e2aac4f8fe544b09f5948c` |
| `reference/Constitution_reference_20260806_v1.html` | 134 250 | `2e07731c5a566cc9372275516b465721b6f0c0fe8435c17594a94ec58ba4cbc3` |
| `reference/Constitution_3col_20260916_v46.html` | 104 362 | `80de491474511d123e3e87811f65315834b457ee8f735ba0722e5a6f6f73caed` |
| `reference/LOLF_3col_20260507_v7.html` | 69 342 | `cb319222fb0312eaf6039d5ba48c6a7d0e26213cc5c1146b33890c64b073ee1f` |
| `reference/LOLF_reference_20260507.html` | 39 449 | `6ade55251222717e7935c2d7cfa75ed788766a5fbecbd3f413848d12fbe87e7b` |
| `reference/DDHC_20260806_v1.html` | 11 827 | `cb4508e7306f0d5e6efe3dd9e4a565b0cdc0b7e33b2fc3e7727821ddefc694c9` |

**Total sorti : 1 617 384 o.**

C'est la liste de l'étape 3 du délestage inscrite au socle — gros référentiels,
TSV du CGI expert, épreuves, HTML de référence en trois colonnes, `texte_livre`.
Elle n'avait pas pu être jouée faute de présence établie ; l'archive l'établit.

## Ce qui n'est pas sorti, et pourquoi

- **Les fragments.** L'étape 2 du socle disait de sortir les fragments
  assemblés. Elle casse l'idempotence de `appareil/fragments.py` : un fragment
  que l'assemblage ne voit plus disparaît du cumulatif. Onze sections
  d'arbitrages ont déjà été perdues ainsi. L'étape est retirée.
- **`methode/arbitrages.md`, `methode/a_trancher.md`, `methode/index.json`,
  `methode/empreintes.json`.** Lus en ouverture de fil.
- **Le socle, les prompts de fil, la carte des chantiers.** Lus en ouverture.

## Ce qui reste dû

- **`methode/journal.md`** : perdu avant cette archive. Empreinte connue
  (`faad6e948ae0fffe007c3a1f15b7da53954ebb623059b7c47a4684a787a5de1e`,
  295 275 o, 4 875 lignes), contenu introuvable au coffre, au dépôt et aux
  transcripts atteignables.
- **`input/Note_Retraite_20250619.docx`** : le coffre le rend en texte et non en
  octets. L'archive porte le rendu texte sous `.docx.txt` ; le binaire reste dû.
- **La poussée de l'archive au dépôt**, dès que le dépôt sera aux sources.
