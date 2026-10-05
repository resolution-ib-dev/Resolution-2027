#!/usr/bin/env python3
"""Installe et rafraîchit le dépôt de droit — sans geste manuel du destinataire.

Ce module existe parce que la version 1.0 décrivait le clonage et le
rafraîchissement comme deux gestes à faire soi-même, dans un mode d'emploi.
Un geste décrit n'est pas un geste fait : le destinataire qui saute la section
rédige sur un extrait qu'il n'a pas, ou sur un extrait périmé qu'il croit frais.
La chaîne s'occupe du droit, ou elle ne s'en occupe pas.

Trois refus tenus par le code, et ce sont eux qui font la pièce :

 1. **Le millésime ne se déduit jamais de l'horloge.** Il se lit dans le
    manifeste de l'extrait, et nulle part ailleurs. Un extrait arrêté en amont
    et estampillé du jour est le pire cas possible : il se lit frais, il est
    faux, et rien ne le dit. Aucun chemin de ce module n'écrit la date du jour
    comme millésime — `_jamais_l_horloge` le garde.
 2. **Un repli est documenté ou n'est pas un repli.** Quand la source
    officielle ne répond pas, le module dit *quelle* source n'a pas répondu,
    *sur quoi* il se replie, et *ce que vaut* ce repli. Il ne se rabat pas en
    silence sur ce qu'il a sous la main.
 3. **Un échec est bruyant.** Code de sortie non nul, bulletin écrit sur
    disque, et marqueur `EXTRAIT_PERIME` déposé dans le clone pour que l'étape
    de rédaction bute dessus même si personne n'a lu la sortie console.

Usage :
    python3 installer_droit.py                      installe ou rafraîchit, puis juge
    python3 installer_droit.py --racine CHEMIN      où poser le clone (défaut : ..)
    python3 installer_droit.py --peremption 45      seuil en jours
    python3 installer_droit.py --etat               ne touche à rien, juge seulement
    python3 installer_droit.py --sans-reseau        n'appelle pas le réseau

Codes de sortie :
    0  extrait en place et frais
    3  le clone n'a pas pu être obtenu — rien à lire, la chaîne ne peut pas partir
    4  le millésime de l'extrait est illisible — on ne devine pas, on s'arrête
    5  l'extrait est périmé et le rafraîchissement n'a pas abouti
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys

DEPOT = "https://github.com/resolution-ib-dev/Resolution-2027"
DOSSIER = "droit"
PEREMPTION = 45

# Les endroits où le millésime de l'extrait peut se lire, dans l'ordre. La
# liste est close : un fichier qui n'y est pas ne sert pas de source de date.
#
# Mesuré au dépôt le 20261003, et la version 1.1 se trompait sur les trois
# points à la fois : le manifeste est à `data/_manifeste.json` et non à la
# racine, sa clé est `millesime_legi` et non `millesime`, et sa date s'écrit
# `20261001` et non en ISO. Le module refusait donc un dépôt parfaitement sain,
# en code 4. Il échouait du bon côté — il n'a jamais inventé de date — mais il
# bloquait tout le monde.
MANIFESTES = ("data/_manifeste.json", "_manifeste.json", "manifeste.json",
              "manifest.json", "extrait/manifeste.json")
# `search` et non `match` : la clé réelle est `millesime_legi`, et un motif
# ancré en fin de clé ne la voyait pas.
CLE_DATE = re.compile(r"(millesime|millésime|date_base|jusqu_au|date)", re.I)
ISO = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
COMPACT = re.compile(r"\b(\d{4})(\d{2})(\d{2})\b")


def _date_quelque_part(valeur):
    """Rend une date ISO depuis `AAAA-MM-JJ` ou `AAAAMMJJ`, ou None.

    Les deux formes vivent au dépôt : le manifeste écrit le millésime LEGI en
    compact, le plancher historique en ISO. On lit les deux et on normalise.
    """
    m = ISO.search(valeur)
    if m:
        return m.group(0)
    m = COMPACT.search(valeur)
    if m:
        a, mo, j = m.groups()
        try:
            return dt.date(int(a), int(mo), int(j)).isoformat()
        except ValueError:
            return None
    return None


class Bruyant(Exception):
    """Un arrêt qui porte son code de sortie et sa phrase. Jamais avalé."""

    def __init__(self, code, phrase, remede=""):
        super().__init__(phrase)
        self.code = code
        self.phrase = phrase
        self.remede = remede


def _jamais_l_horloge(date, provenance):
    """Garde-fou du refus n° 1.

    Un millésime égal à aujourd'hui et qui ne vient pas d'un manifeste est
    presque toujours une date d'exécution qu'un appel a laissé passer pour une
    date de base. On refuse plutôt que de l'imprimer.
    """
    if provenance == "horloge":
        raise Bruyant(4, "le millésime proposé vient de l'horloge et non de "
                         "l'extrait — refusé")
    return date


def _git(args, cwd=None, delai=180):
    r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True,
                       text=True, timeout=delai)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


# --------------------------------------------------------------- le clone

def obtenir(racine, sans_reseau):
    """Rend (chemin du clone, ce qui a été fait, ce qui a échoué)."""
    chemin = os.path.join(racine, DOSSIER)
    present = os.path.isdir(os.path.join(chemin, ".git"))

    if not present:
        if sans_reseau:
            raise Bruyant(3, "aucun clone du dépôt de droit et le réseau est "
                             "coupé par option",
                          "relancez sans --sans-reseau")
        code, sortie = _git(["clone", "--depth", "1", DEPOT, chemin])
        if code != 0:
            raise Bruyant(
                3,
                "le clonage du dépôt de droit a échoué",
                "le dépôt est public, en lecture seule, sans clé ni compte. "
                "Un échec ici est un réseau coupé ou un mandataire qui refuse "
                "la sortie. Message de git, tel quel :\n"
                + sortie.strip()[-800:])
        return chemin, "clone", None

    # Clone déjà là : on tente le rafraîchissement, et son échec n'est pas
    # fatal — c'est le premier des deux replis, et il est documenté.
    if sans_reseau:
        return chemin, "inchange", "réseau coupé par option"
    code, sortie = _git(["fetch", "--depth", "1", "origin"], cwd=chemin)
    if code != 0:
        return chemin, "inchange", ("le dépôt n'a pas répondu — "
                                    + sortie.strip().split("\n")[-1][:200])
    code, sortie = _git(["reset", "--hard", "origin/HEAD"], cwd=chemin)
    if code != 0:
        code, sortie = _git(["reset", "--hard", "origin/main"], cwd=chemin)
    if code != 0:
        return chemin, "inchange", ("la mise à niveau locale a échoué — "
                                    + sortie.strip().split("\n")[-1][:200])
    return chemin, "rafraichi", None


# ------------------------------------------------------- le millésime lu

def _date_dans(obj):
    """Cherche une date ISO sous une clé qui en annonce une. Profondeur 3."""
    def descendre(o, prof):
        if prof > 3:
            return None
        if isinstance(o, dict):
            for k, v in o.items():
                if isinstance(v, (str, int)) and CLE_DATE.search(str(k)):
                    d = _date_quelque_part(str(v))
                    if d:
                        return d
            for v in o.values():
                t = descendre(v, prof + 1)
                if t:
                    return t
        return None
    return descendre(obj, 0)


def millesime(chemin):
    """Rend (date ISO, d'où elle vient). Lève plutôt que de deviner."""
    for nom in MANIFESTES:
        p = os.path.join(chemin, nom)
        if not os.path.isfile(p):
            continue
        try:
            with open(p, encoding="utf-8") as fh:
                d = _date_dans(json.load(fh))
        except (ValueError, OSError):
            continue
        if d:
            return d, nom

    # Repli documenté n° 2 : le lecteur lui-même. `droit.py etat` imprime le
    # millésime de la base ; on le lit dans sa sortie, on ne le reconstruit pas.
    lecteur = os.path.join(chemin, "droit.py")
    if os.path.isfile(lecteur):
        try:
            r = subprocess.run([sys.executable, os.path.abspath(lecteur), "etat"],
                               cwd=chemin, capture_output=True, text=True,
                               timeout=120)
            d = _date_quelque_part((r.stdout or "") + (r.stderr or ""))
            if d:
                return d, "droit.py etat"
        except (OSError, subprocess.SubprocessError):
            pass

    raise Bruyant(
        4,
        "le millésime de l'extrait est illisible",
        "ni manifeste ni `droit.py etat` n'ont rendu de date. On ne la "
        "remplace pas par celle du jour : un extrait daté d'aujourd'hui et "
        "arrêté en amont se lit frais et il est faux. Vérifiez que le clone "
        "est complet, puis relancez.")


# ------------------------------------------------------ le rafraîchissement

def rafraichir(chemin, sans_reseau):
    """Rejoue l'extraction depuis la source officielle. Rend (fait, pourquoi pas)."""
    extracteur = os.path.join(chemin, "extraire_legi.py")
    if sans_reseau:
        return False, "réseau coupé par option"
    if not os.path.isfile(extracteur):
        return False, ("l'extracteur n'est pas dans le clone — le "
                       "rafraîchissement passe alors par l'action programmée "
                       "du dépôt, qui tourne le 1er de chaque mois")
    try:
        r = subprocess.run([sys.executable, extracteur], cwd=chemin,
                           capture_output=True, text=True, timeout=3600)
    except subprocess.TimeoutExpired:
        return False, "l'extraction a dépassé une heure et a été interrompue"
    except OSError as e:
        return False, "l'extraction n'a pas pu être lancée — %s" % e
    if r.returncode != 0:
        derniere = (r.stderr or r.stdout or "").strip().split("\n")[-1][:300]
        return False, ("la source officielle n'a pas répondu ou l'extraction a "
                       "échoué — " + derniere)
    return True, ""


# ------------------------------------------------------------- le bulletin

def bulletin(chemin, etat):
    """Écrit le bulletin sur disque. C'est ce qui rend l'échec non silencieux
    même quand personne ne lit la console."""
    try:
        with open(os.path.join(chemin, "BULLETIN_DROIT.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(etat, fh, ensure_ascii=False, indent=1)
    except OSError:
        pass
    marqueur = os.path.join(chemin, "EXTRAIT_PERIME")
    if etat.get("verdict") == "perime":
        try:
            with open(marqueur, "w", encoding="utf-8") as fh:
                fh.write(
                    "EXTRAIT PÉRIMÉ — ne pas rédiger sur ce clone.\n"
                    "millésime de la base : %s (lu dans : %s)\n"
                    "âge : %s jours, seuil : %s\n"
                    "rafraîchissement tenté : %s\n"
                    "Effacez ce fichier seulement après un rafraîchissement "
                    "abouti.\n" % (etat["millesime"], etat["millesime_lu_dans"],
                                   etat["age_jours"], etat["peremption"],
                                   etat.get("rafraichissement", "—")))
        except OSError:
            pass
    elif os.path.isfile(marqueur):
        try:
            os.remove(marqueur)
        except OSError:
            pass


def dire(etat):
    print("dépôt de droit   : %s" % etat["clone"])
    print("état du clone    : %s%s" % (etat["clone_etat"],
                                       "" if not etat.get("clone_repli")
                                       else "  — repli : " + etat["clone_repli"]))
    print("commit           : %s" % etat.get("commit", "—"))
    print("millésime base   : %s   (lu dans : %s)"
          % (etat["millesime"], etat["millesime_lu_dans"]))
    print("âge              : %s jours   (seuil : %s)"
          % (etat["age_jours"], etat["peremption"]))
    if etat.get("rafraichissement"):
        print("rafraîchissement : %s" % etat["rafraichissement"])
    print("VERDICT          : %s" % etat["verdict"].upper())


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--racine", default="..")
    ap.add_argument("--peremption", type=int, default=PEREMPTION)
    ap.add_argument("--etat", action="store_true",
                    help="ne clone ni ne rafraîchit — juge l'existant")
    ap.add_argument("--sans-reseau", action="store_true")
    a = ap.parse_args(argv)

    try:
        if a.etat:
            chemin = os.path.join(a.racine, DOSSIER)
            if not os.path.isdir(chemin):
                raise Bruyant(3, "aucun clone du dépôt de droit à " + chemin,
                              "lancez le module sans --etat")
            fait, repli = "inchange", "option --etat"
        else:
            chemin, fait, repli = obtenir(a.racine, a.sans_reseau)

        date, source = millesime(chemin)
        _jamais_l_horloge(date, source)
        age = (dt.date.today() - dt.date.fromisoformat(date)).days
        code, sha = _git(["rev-parse", "--short", "HEAD"], cwd=chemin)

        etat = {"clone": os.path.abspath(chemin), "clone_etat": fait,
                "clone_repli": repli, "commit": sha.strip() if code == 0 else "—",
                "millesime": date, "millesime_lu_dans": source,
                "age_jours": age, "peremption": a.peremption,
                "juge_le": dt.date.today().isoformat(),
                "verdict": "frais" if age <= a.peremption else "perime"}

        if etat["verdict"] == "perime" and not a.etat:
            ok, pourquoi = rafraichir(chemin, a.sans_reseau)
            if ok:
                date, source = millesime(chemin)
                _jamais_l_horloge(date, source)
                age = (dt.date.today() - dt.date.fromisoformat(date)).days
                etat.update(millesime=date, millesime_lu_dans=source,
                            age_jours=age, rafraichissement="abouti",
                            verdict="frais" if age <= a.peremption else "perime")
            else:
                etat["rafraichissement"] = "ÉCHEC — " + pourquoi

        bulletin(chemin, etat)
        dire(etat)

        if etat["verdict"] == "perime":
            print("\nL'extrait n'est pas fiable et ne sert pas à rédiger.",
                  file=sys.stderr)
            print("Un marqueur EXTRAIT_PERIME a été déposé dans le clone.",
                  file=sys.stderr)
            print("Repli : l'action programmée du dépôt rejoue l'extraction le "
                  "1er de chaque mois. Relancez ce module après son passage, ou "
                  "reclonez. Rien n'autorise à rédiger entre-temps.",
                  file=sys.stderr)
            return 5
        return 0

    except Bruyant as e:
        print("ARRÊT — %s" % e.phrase, file=sys.stderr)
        if e.remede:
            print(e.remede, file=sys.stderr)
        return e.code


if __name__ == "__main__":
    sys.exit(main())
