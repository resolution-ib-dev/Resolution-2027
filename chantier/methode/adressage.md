# Adressage — une seule grammaire pour les deux surfaces

Inscrit le 20261013. Remplace les règles d'adresse éparses de
`methode/carte_des_domiciles_20261012.md`, du bloc « Ouverture de session » de
`CLAUDE.md` et de `methode/gestion_depot_projet.md`, qui disaient la même chose
en trois endroits et en trois grammaires.

---

## 1. Une adresse de corpus s'écrit sans préfixe

Toute pièce du corpus s'adresse par son chemin nu : `methode/arbitrages.md`,
`livrables/depot_2027/P1/2_4_tarifs_reduits_accise.md`,
`referentiels/notes_manuscrit.json`.

Au dépôt, ces pièces vivent sous `chantier/`. **Ce préfixe n'est pas une
adresse : c'est un détail de rangement du dépôt, et il ne s'écrit jamais dans
une règle, un mandat, une skill ni un exposé.** Le geste d'ouverture l'efface.

## 2. Le geste d'ouverture, trois lignes, toujours les mêmes

```
git clone --depth 1 https://github.com/resolution-ib-dev/Resolution-2027 droit
cp -r droit/chantier/. .
python3 droit/droit.py etat
```

Après ce geste, et seulement après lui :

- toute adresse de corpus est valide telle quelle dans l'atelier ;
- le droit s'adresse **hors corpus**, sous `droit/` — `droit/droit.py`,
  `droit/codes.json`, `droit/data/` — parce qu'il vit à la racine du dépôt et
  non sous `chantier/` ;
- `droit.py etat` dit le millésime et imprime `À REJOUER` au-delà de 45 jours.

Un fil qui n'a pas joué ces trois lignes n'a pas de corpus. Il ne déclare
aucune pièce absente.

## 3. Qui prévaut

| matière | surface qui fait foi |
|---|---|
| pièces de liasse, arbitrages, états, registres, méthode, appareil | **coffre** |
| livre et ses notes, référentiels de droit, base LEGI, guides | **dépôt** |
| une pièce présente des deux côtés | **coffre**, toujours |

Le clone sert à **disposer** des pièces, jamais à les arbitrer. Une divergence
entre les deux surfaces se tranche au coffre et se verse ensuite au dépôt ; elle
ne se tranche jamais en faveur du clone au motif qu'il est sous la main.

## 4. Avant de déclarer une absence

Une absence se déclare avec le périmètre mesuré, et le périmètre complet est
toujours : **coffre + clone + base de droit**. « Absent du coffre » n'est pas
« absent du projet ». Un texte de loi se cherche à `droit/droit.py` avant d'être
dit introuvable, et l'inventaire des textes portés se lit à
`droit/codes.json`, non à la mémoire d'un fil.

## 5. **UN FIL CLAUDE.AI/CODE N'ACCÈDE PAS AU COFFRE**

**C'est la règle qui a coûté le plus cher, et elle n'admet aucune exception.**
Un fil claude.ai/code ne voit ni les documents du projet Claude, ni ses pièces
jointes. Il ne voit que le dépôt, qu'il clone et dans lequel il pousse.

**Conséquence tenue** : un mandat donné à un fil claude.ai/code ne cite jamais
une adresse de coffre comme une source à lire. Toute pièce de coffre dont ce
fil a besoin lui est **jointe en fichier, ou rassemblée dans un zip** par le
fil Cowork qui le lance. Un mandat qui dit « reprends depuis le projet » est un
mandat mort.

**Conséquence de fond** : le dépôt est le seul pont entre le coffre et code.
Tout ce qui doit être accessible à code vit donc au dépôt, et la dette de
versement n'est pas un détail d'intendance — c'est ce qui coupe le pont.

## 6. Versement

Un fil Cowork lit le dépôt et ne pousse pas. Tout ce qu'il corrige au dépôt
— appareil, `codes.json`, référentiels — reste dans son conteneur et doit être
repris par un fil claude.ai/code, qui est la seule surface qui pousse.

Un fil qui laisse une correction au dépôt la nomme en fin de fil, par son chemin
de dépôt complet, préfixe compris. C'est le seul endroit où le préfixe s'écrit.
