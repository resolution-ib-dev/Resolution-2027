# -*- coding: utf-8 -*-
"""Relevé des notes de fin du manuscrit.

Le manuscrit est strate 1. Ses notes explicitent les raisonnements que le corps
du texte laisse implicites : hypothèses de calcul, sources, contre-arguments,
définitions. Elles ne se recopient nulle part — elles se relèvent.

Ce relevé est un dérivé. Il se régénère à chaque version du manuscrit et ne se
corrige jamais à la main.

Usage : python3 extraire_notes.py Manuscrit.html Notes_manuscrit.json
"""
import json, re, sys, html as H

# Une note porte un chiffre si elle contient un nombre autre qu'un millésime ou
# un numéro de rapport. Heuristique volontairement large : mieux vaut signaler
# une note inoffensive que taire une note chiffrée.
CHIFFRE = re.compile(
    r'\d[\d  \u202f]*(?:,\d+)?\s*(?:%|Md€|milliard|million|€|euros?|points?|fois)')


def relever(chemin):
    s = open(chemin, encoding='utf-8').read()

    # section appelante de chaque note, dans l'ordre du texte
    appel = {}
    for d in re.finditer(r'<div class="section" id="([^"]+)"[^>]*>(.*?)</div>',
                         s, re.S):
        for a in re.findall(r'appel-(e\d+)', d.group(2)):
            appel.setdefault(a, d.group(1))

    notes = []
    for m in re.finditer(r'id="note-(e\d+)"[^>]*>(.*?)(?=<[^>]*id="note-e|\Z)',
                         s, re.S):
        txt = re.sub(r'\s+', ' ',
                     H.unescape(re.sub(r'<[^>]+>', ' ', m.group(2))))
        txt = txt.strip().rstrip('↩ ').strip()
        notes.append({
            'id': m.group(1),
            'section': appel.get(m.group(1), ''),
            'texte': txt,
            'porte_un_chiffre': bool(CHIFFRE.search(txt)),
            'longueur': len(txt),
        })
    return notes


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    notes = relever(argv[1])
    orphelines = [n['id'] for n in notes if not n['section']]
    chiffrees = [n['id'] for n in notes if n['porte_un_chiffre']]
    json.dump({'_revision': {'source': argv[1].split('/')[-1],
                             'objet': 'relevé des notes de fin, dérivé de la strate 1'},
               'notes': notes},
              open(argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"{argv[2]} écrit — {len(notes)} notes, {len(chiffrees)} portant un chiffre")
    if orphelines:
        print(f"  {len(orphelines)} note(s) sans section appelante : "
              + ', '.join(orphelines))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
