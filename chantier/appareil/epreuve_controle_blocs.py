#!/usr/bin/env python3
"""Épreuve de la série D de `controle_blocs.py` — un jeu de fautes, un jeu de justes.

Un contrôle qui n'a jamais rien attrapé ne prouve rien : il peut être vert parce
que le corpus est sain, ou parce qu'il ne regarde nulle part. L'épreuve tranche
en jouant le contrôle sur un corpus délibérément faux.

**Le jeu de fautes** mute une copie du corpus, une faute à la fois, et exige que
le code attendu — `D1`, `D2` ou `D3` — se lève. Une faute non attrapée est un
trou du contrôle, pas une bonne nouvelle.

**Le jeu de justes** mute la copie d'une manière qui ne doit rien lever : une
rédaction différente, une grandeur déplacée mais vraie, un agrégat juste. Une
faute levée là est un faux positif, et un faux positif use le contrôle plus
sûrement qu'un trou — on finit par ne plus le lire.

Le compte de référence du corpus sain est relevé au premier passage et sert de
départage : l'épreuve mesure ce que la mutation ajoute, jamais un absolu.

Usage : python3 appareil/epreuve_controle_blocs.py
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

APPAREIL = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(APPAREIL)
CONTROLE = os.path.join(APPAREIL, "controle_blocs.py")


# --- les mutations ----------------------------------------------------------
# Chacune reçoit le `blocs.json` de la copie et le rend muté. Le libellé dit ce
# que la faute imite, en clair, parce que c'est lui qu'on lit quand elle échappe.

def _bloc(data, bid):
    for b in data["blocs"]:
        if b["id"] == bid:
            return b
    raise KeyError(bid)


def faute_montant_recopie_de_travers(data):
    """Le cas nominal : un montant du bilan ne vaut plus celui de l'énoncé."""
    b = _bloc(data, "B-01")
    b["bilan"]["supprime"] = b["bilan"]["supprime"].replace("8,632 Md€", "9,632 Md€")
    return data


def faute_montant_attribue_au_mauvais_enonce(data):
    """Le montant existe, mais sous un autre énoncé que celui qui est nommé."""
    b = _bloc(data, "B-11")
    b["bilan"]["supprime"] = "580 000 Md€ par an (paramètre de M-042)."
    return data


def faute_grandeur_sans_source(data):
    """Une grandeur apparaît au bilan sans énoncé et sans origine déclarée."""
    b = _bloc(data, "B-14")
    b["bilan"]["supprime"] = ("Déclaré non chiffré. Le paquet ne porte aucun montant "
                              "propre à la cession. Le produit attendu est de 7,3 Md€.")
    return data


def faute_agregat_qui_ne_tombe_pas(data):
    """La somme annoncée ne vaut pas ses composantes."""
    b = _bloc(data, "B-05")
    b["bilan"]["supprime"] = b["bilan"]["supprime"].replace("soit 27,5 Md€", "soit 28,5 Md€")
    return data


FAUTES = [
    ("montant recopié de travers", "D1", faute_montant_recopie_de_travers),
    ("montant attribué au mauvais énoncé", "D1", faute_montant_attribue_au_mauvais_enonce),
    ("grandeur sans énoncé ni origine", "D2", faute_grandeur_sans_source),
    ("agrégat qui ne tombe pas", "D3", faute_agregat_qui_ne_tombe_pas),
]


def juste_rediger_autrement(data):
    """Même montant, même énoncé, phrase refaite : rien ne doit se lever."""
    b = _bloc(data, "B-11")
    b["bilan"]["supprime"] = ("Une économie de 30 Md€ par an (paramètre de M-042). "
                              "La durée d'indemnisation collective est ramenée à six mois.")
    return data


def juste_origine_declaree(data):
    """Grandeur sans énoncé, mais origine déclarée dans la phrase."""
    b = _bloc(data, "B-14")
    b["bilan"]["supprime"] = ("Déclaré non chiffré. Un produit de 7,3 Md€ est avancé "
                              "en ordre de grandeur, par calcul propre du paquet.")
    return data


def juste_agregat_exact(data):
    """Un agrégat neuf, mais juste."""
    b = _bloc(data, "B-06")
    b["bilan"]["supprime"] = b["bilan"]["supprime"].replace(
        "0,6 Md€ de chèque énergie (paramètres de M-019)",
        "0,6 Md€ de chèque énergie, soit 16,7 Md€ (paramètres de M-019)")
    return data


JUSTES = [
    ("même montant, autre rédaction", juste_rediger_autrement),
    ("grandeur d'origine déclarée", juste_origine_declaree),
    ("agrégat juste", juste_agregat_exact),
]


# --- le banc ----------------------------------------------------------------

def jouer(racine):
    r = subprocess.run([sys.executable, CONTROLE], capture_output=True, text=True,
                       env=dict(os.environ, RESOLUTION_RACINE=racine))
    sortie = r.stdout
    comptes = {}
    for code in ("B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3"):
        m = re.search(r"^%s : (\d+)$" % code, sortie, re.M)
        comptes[code] = int(m.group(1)) if m else -1
    return comptes, sortie


def copie(base):
    d = tempfile.mkdtemp(prefix="epreuve_blocs_")
    for sous in ("livrables/blocs", "livrables/paquet_machine"):
        shutil.copytree(os.path.join(base, sous), os.path.join(d, sous))
    return d


def muter(racine, mutation):
    p = os.path.join(racine, "livrables", "blocs", "blocs.json")
    data = json.load(open(p, encoding="utf-8"))
    json.dump(mutation(data), open(p, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


def main():
    temoin = copie(RACINE)
    reference, _ = jouer(temoin)
    shutil.rmtree(temoin)
    print("référence du corpus sain : " +
          ", ".join("%s=%d" % (k, v) for k, v in reference.items() if v))
    echecs = 0

    print("\njeu de fautes — chaque faute doit lever son code")
    for libelle, code, mutation in FAUTES:
        d = copie(RACINE)
        muter(d, mutation)
        comptes, _ = jouer(d)
        shutil.rmtree(d)
        leve = comptes[code] > reference[code]
        print("    %-40s %s attendu : %s" % (libelle, code, "levé" if leve else "NON LEVÉ"))
        echecs += 0 if leve else 1

    print("\njeu de justes — rien ne doit se lever")
    for libelle, mutation in JUSTES:
        d = copie(RACINE)
        muter(d, mutation)
        comptes, sortie = jouer(d)
        shutil.rmtree(d)
        ajouts = {k: comptes[k] - reference[k] for k in comptes
                  if comptes[k] > reference[k]}
        print("    %-40s %s" % (libelle, "rien levé" if not ajouts
                                else "FAUX POSITIF : %s" % ajouts))
        echecs += 0 if not ajouts else 1

    print("\nÉPREUVE : %s" % ("passée" if not echecs else "%d échec(s)" % echecs))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())

