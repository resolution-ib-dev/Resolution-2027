# -*- coding: utf-8 -*-
"""Restauration du coffre vers le dépôt, par copie d'octets.

Le coffre rend ses documents **en texte** : seule une archive assez volumineuse
revient comme fichier. Pendant trois sessions, on en a conclu qu'un document
lisible du coffre ne pouvait revenir au dépôt qu'en repassant par le modèle — et
le 20260824, cette croyance a produit un manuscrit tronqué à 607 octets et un
index aux retours ligne échappés.

Elle était fausse. **Le texte rendu par le coffre est écrit verbatim au
transcript de session**, en JSON, sur le disque de l'atelier. Il s'en extrait par
script. La restauration est donc une copie d'octets, exactement comme le
dépliage d'une archive, et rien ne passe par le modèle.

Deux sources d'octets, dans cet ordre :

1. **le fichier rendu** — un document assez volumineux revient comme fichier
   local, et l'appel le nomme. `cp`, rien d'autre.
2. **le transcript** — pour tout le reste. Le contenu y est le même octet que
   celui que le coffre a rendu.

Le transcript porte aussi ce que les fils auxiliaires ont lu, y compris ceux qui
sont morts avant d'écrire : leur lecture n'est pas perdue.

Quand un document apparaît plusieurs fois au transcript, **la lecture la plus
récente vaut** : le coffre est unique, donc deux versions ne sont pas un conflit
mais une chronologie — la session a versé entre les deux. Les versions écartées se
disent, avec leur horodatage, pour que rien ne disparaisse en silence.

Usage : python3 restaurer.py ../methode/index.json .. [chemin_coffre ...]
        sans argument de chemin, tout ce que le transcript porte.
"""
import glob
import hashlib
import json
import os
import sys

# Le transcript ne vit pas forcément sous le compte qui exécute `make` : selon
# la façade, la session écrit sous `~/.claude` ou sous `/root/.claude`. On
# balaie les deux plutôt que d'en supposer une.
RACINES_TRANSCRITS = (os.path.expanduser('~/.claude/projects'),
                      '/root/.claude/projects',
                      '/home/claude/.claude/projects')


def transcripts():
    """Les transcripts de la session et de ses fils auxiliaires."""
    vus = set()
    for racine in RACINES_TRANSCRITS:
        for dossier, _sous, fichiers in os.walk(racine):
            for nom in fichiers:
                if not nom.endswith('.jsonl'):
                    continue
                reel = os.path.realpath(os.path.join(dossier, nom))
                if reel not in vus:
                    vus.add(reel)
                    yield reel


def _lectures(chemin_transcript, trouve):
    """Ajoute à `trouve` tout (chemin coffre, horodatage, contenu) d'un transcript."""
    horodatage = ['']

    def scan(o):
        if isinstance(o, dict):
            for v in o.values():
                scan(v)
        elif isinstance(o, list):
            for v in o:
                scan(v)
        elif isinstance(o, str) and '"content"' in o and '"path"' in o:
            try:
                d = json.loads(o)
            except ValueError:
                return
            if (isinstance(d, dict) and d.get('method') == 'project_read'
                    and isinstance(d.get('content'), str)):
                trouve.setdefault(d['path'], []).append(
                    (horodatage[0], d['content']))
    with open(chemin_transcript, encoding='utf-8') as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue
            try:
                rec = json.loads(ligne)
            except ValueError:
                continue
            if isinstance(rec, dict) and isinstance(rec.get('timestamp'), str):
                horodatage[0] = rec['timestamp']
            scan(rec)


def moisson():
    """chemin au coffre → contenu, relevé de tous les transcripts."""
    trouve = {}
    for t in transcripts():
        try:
            _lectures(t, trouve)
        except OSError:
            continue
    retenu, ecartees = {}, {}
    for chemin, versions in trouve.items():
        # Par horodatage croissant : la dernière lecture est l'état courant du
        # coffre. Une version antérieure est ce qu'il portait avant que la
        # session ne verse.
        versions.sort(key=lambda hv: hv[0])
        distinctes = []
        for horo, contenu in versions:
            h = hashlib.sha256(contenu.encode()).hexdigest()
            if not distinctes or distinctes[-1][0] != h:
                distinctes.append((h, horo, contenu))
        retenu[chemin] = distinctes[-1][2]
        if len(distinctes) > 1:
            ecartees[chemin] = [(h[:16], horo, len(c))
                                for h, horo, c in distinctes[:-1]]
    return retenu, ecartees


def restaurer(chemin_index, racine, demandes=()):
    index = json.load(open(chemin_index, encoding='utf-8'))
    # chemin au coffre → chemin de dépôt. Un même chemin de coffre ne sert
    # qu'un artefact, hors archives, qui se déplient par `coffre.py`.
    cible = {a['chemin_coffre']: a['chemin'] for a in index['artefacts']
             if a['coffre'] and a['restaurable']
             and a['chemin_coffre'] not in
             {x['chemin_coffre'] for x in index['archives']}}

    dispo, ecartees = moisson()

    # Le balayage ne sait pas d'avance à quel projet appartient un transcript :
    # il ne retient que les chemins que l'index déclare, ce qui écarte l'essentiel
    # d'une confusion entre projets. Reste à le dire quand plusieurs projets sont
    # visibles depuis l'atelier.
    projets = {t.split('/projects/')[-1].split('/')[0]
               for t in transcripts() if '/projects/' in t}
    if len(projets) > 1:
        print(f'ATTENTION — {len(projets)} projets visibles depuis l\'atelier : '
              f'{", ".join(sorted(projets))}. Vérifier qu\'aucun chemin ne se '
              f'recoupe entre eux.')
    voulus = set(demandes) if demandes else set(cible)

    ecrits, absents, presents = [], [], []
    for coffre_ch in sorted(voulus):
        depot = cible.get(coffre_ch)
        if depot is None:
            print(f'    hors index — {coffre_ch}')
            continue
        contenu = dispo.get(coffre_ch)
        if contenu is None:
            absents.append(coffre_ch)
            continue
        dst = os.path.join(racine, depot)
        # La restauration remplit des trous, elle n'écrase rien. Un fichier
        # présent au dépôt a pu être délibérément modifié par la session, et le
        # transcript porte l'état d'avant : réécrire dessus détruirait le
        # travail en cours sans le dire.
        if os.path.exists(dst):
            presents.append(depot)
            continue
        os.makedirs(os.path.dirname(dst) or '.', exist_ok=True)
        with open(dst, 'w', encoding='utf-8', newline='') as f:
            f.write(contenu)
        octets = os.path.getsize(dst)
        ecrits.append((depot, octets))

    for chemin, vieilles in sorted(ecartees.items()):
        print(f'    version(s) écartée(s) — {chemin} : '
              + ', '.join(f'{h} du {horo[:19]} ({n} car.)'
                          for h, horo, n in vieilles))

    print(f'{len(ecrits)} document(s) restauré(s) par copie d\'octets, '
          f'{len(presents)} déjà au dépôt et laissé(s) tel(s) quel(s), '
          f'{len(absents)} absent(s) du transcript, '
          f'{len(ecartees)} document(s) lu(s) en plusieurs états')
    for depot, octets in ecrits:
        print(f'    {depot} — {octets} o')
    for c in absents:
        print(f'    non lu dans cette session — {c}')
    return 0


if __name__ == '__main__':
    sys.exit(restaurer(sys.argv[1],
                       sys.argv[2] if len(sys.argv) > 2 else '.',
                       sys.argv[3:]))
