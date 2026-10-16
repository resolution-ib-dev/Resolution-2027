#!/usr/bin/env python3
"""diff_cible.py — diff structuré texte en vigueur / texte cible, et contrôle de bouclage.

Usage :
  Diff structuré (matrice de l'étape 3) :
    python diff_cible.py diff EN_VIGUEUR.txt CIBLE.txt [--label "Article 47"]

  Contrôle de bouclage (étape 3, obligatoire) :
    python diff_cible.py verify RECONSTRUIT.txt CIBLE.txt [--label "Article 47"]

Format d'entrée : texte brut, un alinéa par ligne non vide (lignes vides ignorées).
Un fichier par article. Pour un texte multi-articles, appeler le script article par article.

Sortie : markdown sur stdout. verify sort avec code 1 en cas de divergence.
"""
import argparse
import difflib
import re
import sys
import unicodedata


def read_alineas(path):
    with open(path, encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]


def norm(s):
    """Normalisation pour comparaison : espaces, apostrophes, espaces insécables."""
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\u2019", "'").replace("\u00a0", " ").replace("\u202f", " ")
    return re.sub(r"\s+", " ", s).strip()


def words(s):
    return norm(s).split(" ")


def word_diff(a, b):
    """Diff mot à mot lisible entre deux alinéas."""
    sm = difflib.SequenceMatcher(a=words(a), b=words(b), autojunk=False)
    parts = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        wa, wb = " ".join(words(a)[i1:i2]), " ".join(words(b)[j1:j2])
        if op == "equal":
            continue
        if op == "delete":
            parts.append(f'suppression des mots : « {wa} »')
        elif op == "insert":
            parts.append(f'insertion des mots : « {wb} »')
        else:
            parts.append(f'les mots : « {wa} » → « {wb} »')
    return parts


def ordinal(n):
    if n == 1:
        return "premier"
    specials = {2: "deuxième", 3: "troisième", 4: "quatrième", 5: "cinquième",
                6: "sixième", 7: "septième", 8: "huitième", 9: "neuvième",
                10: "dixième", 11: "onzième", 12: "douzième"}
    return specials.get(n, f"{n}e")


def similarity(a, b):
    return difflib.SequenceMatcher(a=norm(a), b=norm(b), autojunk=False).ratio()


def do_diff(vigueur, cible, label):
    print(f"## Diff structuré — {label}\n")
    if not vigueur and cible:
        print("**CRÉATION** : l'article n'existe pas dans le texte en vigueur.")
        return
    if vigueur and not cible:
        print("**ABROGATION** : l'article disparaît du texte cible.")
        return

    sm = difflib.SequenceMatcher(a=[norm(x) for x in vigueur],
                                 b=[norm(x) for x in cible], autojunk=False)
    deltas = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                print(f"- al. {ordinal(i1 + k + 1)} : inchangé")
            continue
        deltas += 1
        if op == "delete":
            for i in range(i1, i2):
                print(f"- **SUPPRESSION** du {ordinal(i + 1)} alinéa : « {vigueur[i][:80]}… »"
                      if len(vigueur[i]) > 80 else
                      f"- **SUPPRESSION** du {ordinal(i + 1)} alinéa : « {vigueur[i]} »")
        elif op == "insert":
            pos = f"après le {ordinal(i1)} alinéa" if i1 > 0 else "avant le premier alinéa"
            for j in range(j1, j2):
                print(f"- **INSERTION** {pos} : « {cible[j]} »")
        else:  # replace
            # apparier au mieux les alinéas remplacés
            for off in range(max(i2 - i1, j2 - j1)):
                ia, jb = i1 + off, j1 + off
                if ia < i2 and jb < j2:
                    sim = similarity(vigueur[ia], cible[jb])
                    if sim >= 0.6:
                        print(f"- **MODIFICATION** du {ordinal(ia + 1)} alinéa "
                              f"(similarité {sim:.0%}) :")
                        for p in word_diff(vigueur[ia], cible[jb]):
                            print(f"    - {p}")
                    else:
                        print(f"- **REMPLACEMENT** du {ordinal(ia + 1)} alinéa "
                              f"(similarité {sim:.0%} — remplacement d'alinéa entier "
                              f"recommandé) :")
                        print(f"    - nouveau texte : « {cible[jb]} »")
                elif ia < i2:
                    print(f"- **SUPPRESSION** du {ordinal(ia + 1)} alinéa")
                else:
                    print(f"- **INSERTION** après le {ordinal(i2)} alinéa : « {cible[jb]} »")
    print(f"\nAlinéas en vigueur : {len(vigueur)} — alinéas cibles : {len(cible)} — "
          f"blocs modifiés : {deltas}")
    if deltas == 0:
        print("\nAucun delta : article identique.")


def do_verify(reconstruit, cible, label):
    print(f"## Contrôle de bouclage — {label}\n")
    ok = True
    if len(reconstruit) != len(cible):
        ok = False
        print(f"**ÉCHEC** : {len(reconstruit)} alinéas reconstruits, "
              f"{len(cible)} attendus.\n")
    for idx, (r, c) in enumerate(zip(reconstruit, cible), 1):
        if norm(r) != norm(c):
            ok = False
            print(f"- **DIVERGENCE** au {ordinal(idx)} alinéa :")
            for p in word_diff(r, c):
                print(f"    - {p}")
    if ok:
        print("**CONFORME** : le texte reconstruit est identique au texte cible "
              "(à la normalisation typographique près).")
        return 0
    print("\nCorriger les dispositions modificatives, jamais le texte cible.")
    return 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["diff", "verify"])
    ap.add_argument("fichier_a", help="diff : texte en vigueur | verify : texte reconstruit")
    ap.add_argument("fichier_b", help="texte cible")
    ap.add_argument("--label", default="article")
    args = ap.parse_args()

    a, b = read_alineas(args.fichier_a), read_alineas(args.fichier_b)
    if args.mode == "diff":
        do_diff(a, b, args.label)
        return 0
    return do_verify(a, b, args.label)


if __name__ == "__main__":
    sys.exit(main())
