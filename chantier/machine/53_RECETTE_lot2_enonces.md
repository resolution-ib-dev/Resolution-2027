# 53 — RECETTE, lot 2 : trois énoncés

**Le lot 1 (`50`) ne fait qu'une chose à la fois** : un véhicule, un article
additionnel, aucun gage. Ces trois mesures prennent le reste — les deux
véhicules, les trois formes de gage, un article que le véhicule ouvre déjà, et
un droit que le texte en vigueur abroge tout seul.

**Jouez-les une par une, dans l'ordre.** N'ouvrez
`54_RECETTE_lot2_sorties_attendues.md` qu'après avoir produit les trois.

---

## Mesure A

> Y a une taxe sur les vidéogrammes, les DVD et la location. Ça rapporte trois
> fois rien, ça part au CNC, et ça coûte sûrement autant à collecter. Je veux la
> virer.

## Mesure B

> Les assureurs se prennent une taxe quand leurs provisions sont jugées trop
> élevées. En gros on les punit d'avoir été prudents. Je veux la supprimer. Il me
> semble que le texte de finances touche déjà à cet article.

## Mesure C

> Les fabricants de matériel médical paient une contribution sur leur pub. Je
> veux la supprimer.

---

**Ce que vous rendez** : pour chaque mesure, l'amendement en markdown — ou la
raison motivée de ne pas en produire —, et le verdict de

```
python3 66_CONTROLE_recette.py --sortie votre_piece.md
```

**Une des trois ne doit produire aucun amendement.** Trouver laquelle, et dire
pourquoi, fait partie de la recette. Une chaîne qui rend trois amendements a
échoué, même si les trois sont bien écrits.
