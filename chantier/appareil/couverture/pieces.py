# -*- coding: utf-8 -*-
"""Ce que nos pièces font à chaque article du code général des impôts.

Deux canaux, et le second est celui que le regroupement du 20261009 a rendu
indispensable :

1. **l'article nommé** — « l'article 219 du même code est abrogé » ;
2. **la division désignée** — « le 2 bis du II de la 1re sous-section… ». Depuis
   le 20261009 la clause abroge 171 blocs par leur division, soit 220 articles
   qu'aucune occurrence de numéro ne porte plus. Les relever par le seul texte
   ferait 220 articles déclarés absents de nos pièces, et le compte serait faux.

La table des rangs est prise au registre des colonnes, § I, II et III.
"""
import os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAQUET = os.path.join(RACINE, 'livrables', 'depot_2027')
sys.path.insert(0, os.path.join(RACINE, 'appareil', 'fil1_verification'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import liasse                                                  # noqa
import c3_adresses as adr                                      # noqa
import sources                                                 # noqa

CGI = 'code général des impôts'

# fichier du paquet -> [(rang, découpe)] ; registre des colonnes, §§ I, II, III.
RANGS = {}
for _r, (_f, _lib, _lot) in liasse.RANGS.items():
    RANGS.setdefault(_f, []).append(_r)
AUTRES = {
    'P2/etatB_01_structures_facultatives.md': ['P2-01'],
    'P2/coll_P2_02_credits_etat_B.md': ['P2-02'],
    'P2/etatB_02_subventions_associations.md': ['P2-03'],
    'P2/etatB_03_aides_ciblees.md': ['P2-04'],
    'P2/etatB_04_titre2_plafond_emplois.md': ['P2-05'],
    'P2/2_1_dissolution_structures_facultatives.md': ['P2-06'],
    'P2/2_1_etablissements_ressources_propres.md': ['P2-07'],
    'P2/2_1_missions_rendues_aux_ministeres.md': ['P2-08'],
    'P2/2_2_indemnite_depart_agents.md': ['P2-09'],
    'sans_colonne/n7b_m070_depenses_nouvelles.md': ['P2-10'],
    'sans_colonne/n7b_m037b_gel_indexations_plf.md': ['P2-11'],
    'P2/n6_logement_social_flux.md': ['P2-12'],
    'P2/n6_defaisance_participations.md': ['P2-13'],
    'P2/n6_typologies_de_depenses.md': ['P2-14'],
    'P2/2_6_extinction_aide_logement.md': ['P2-15'],
    'P2/2_6_socle_hebergement_urgence.md': ['P2-16'],
    'P2/2_6_cheque_energie.md': ['P2-17'],
    'P2/coll_P2_01_abrogation_concours_discretionnaires.md': ['P2-18'],
    'P2/coll_P2_03_suppression_articles_85_86_87.md': ['P2-19'],
    'SS/n7b_ss03_liste_niches_sociales.md': ['SS-01'],
    'SS/3_3_restitution_salariale_principale.md': ['SS-02'],
    'SS/3_3_restitution_salariale_coordination.md': ['SS-03'],
    'SS/nuit1c_suppression_taxe_salaires.md': ['SS-04'],
    'SS/arrets_04_m024_prolongation_droits_soins.md': ['SS-05'],
    'SS/n5_cadre_bouclier_sanitaire.md': ['SS-06'],
    'SS/n7b_m037a_gel_indexations_lfss.md': ['SS-07'],
    'SS/n5_amorce_extinction_repartition.md': ['SS-08'],
    'SS/n5_extinction_aides_fondues.md': ['SS-09'],
    'SS/2_3_subventions_associations_social.md': ['SS-10'],
    'sans_colonne/nuit1c_ppl_cession_participations.md': ['PPL (sans colonne)'],
}
for _f, _rr in AUTRES.items():
    RANGS.setdefault(_f, []).extend(_rr)

# Les liasses assemblées, le sommaire et le lisez-moi sont des dérivés : ils
# recopient les pièces et les compter ferait deux fois chaque article.
DERIVE = re.compile(r'^(LIASSE|SOMMAIRE|LISEZ-MOI)')

SUBDIV = re.compile(r'(alinéa|phrase|mots?|membre|\b[IVX]+\b|\b\d+°|\b[a-z]\)|\ble \d+ )', re.I)


def _operation(fenetre_avant, fenetre_apres):
    """Ce que la pièce fait à l'article nommé."""
    f = fenetre_apres
    if re.search(r'\best abrogée?\b', f[:120]):
        return 'abrogation entière' if not SUBDIV.search(fenetre_avant[-90:]) \
            else 'abrogation partielle'
    if re.search(r'\bsont abrogés?\b|\bsont abrogées\b', f[:160]):
        return 'abrogation entière' if not SUBDIV.search(fenetre_avant[-90:]) \
            else 'abrogation partielle'
    if 'est ainsi rédigé' in f[:160]:
        return 'réécriture'
    if 'est ainsi modifié' in f[:160] or 'sont ainsi modifiés' in f[:160]:
        return 'modification'
    if re.search(r'due concurrence|compensée|gage', fenetre_avant[-200:] + f[:200], re.I):
        return 'gage'
    return 'citation'


def fichiers():
    out = []
    for dp, _d, fs in os.walk(PAQUET):
        for n in sorted(fs):
            if n.endswith('.md') and '.PERIME.' not in n and not DERIVE.match(n):
                out.append(os.path.relpath(os.path.join(dp, n), PAQUET))
    return sorted(out)


def _dispositif(rel, texte):
    """Le ou les dispositifs d'un fichier ; la clause se découpe par division."""
    if rel == 'clause_generale_niches_20261005.md':
        bouts = []
        for rang in ('P1-31', 'P1-04'):
            seg = liasse.segments(texte, rang)
            bouts.append((rang, seg['dispositif']))
        return bouts
    blocs = liasse.dispositifs(texte)
    d = ''.join(texte[a:b] for a, b in blocs) or texte
    return [(' · '.join(RANGS.get(rel, ['— hors colonne'])), d)]


def nommes():
    """article du CGI -> liste de (rang, opération, pièce)."""
    out, cites = {}, {}
    for rel in fichiers():
        texte = liasse.normaliser(open(os.path.join(PAQUET, rel), encoding='utf-8').read())
        porte_cgi = CGI in texte
        for rang, disp in _dispositif(rel, texte):
            if not disp:
                continue
            dominants = [adr._canon(m.group(0)) for m in adr.CODE_RE.finditer(disp)]
            seul_cgi = set(dominants) == {CGI}
            dernier = [None]
            for m in adr.ART_RE.finditer(disp):
                seq = m.group(1).rstrip(' ,.;')
                apres = disp[m.end():m.end() + 120]
                avant = disp[max(0, m.start() - 220):m.start()]
                mm = re.match(r'\s*(?:du|de la|des|au)\s+(?:même\s+code\b|('
                              + '|'.join(adr._motif(k) for k in adr.NOMS) + r'))', apres, re.I)
                if mm and mm.group(1):
                    code = adr._canon(mm.group(1)); dernier[0] = code
                elif mm:
                    code = dernier[0]
                else:
                    mc = adr.CODE_RE.search(apres[:60])
                    code = adr._canon(mc.group(0)) if mc else (dernier[0] or
                                                               (CGI if seul_cgi else None))
                if code != CGI:
                    continue
                op = _operation(avant, apres)
                for p in re.split(r'\s*,\s*|\s+et\s+|\s+ou\s+', seq):
                    p = p.strip().rstrip(' ,.;')
                    if not p:
                        continue
                    for num in ([x.strip() for x in p.split(' à ', 1)] if ' à ' in p else [p]):
                        out.setdefault(num, []).append((rang, op, rel))
        if porte_cgi:
            cites[rel] = True
    return out, cites


def par_division():
    """article -> (rang, opération, désignation) pour les blocs abrogés en entier."""
    chemin = os.path.join(PAQUET, 'clause_generale_niches_20261005.md')
    texte = liasse.normaliser(open(chemin, encoding='utf-8').read())
    seg = liasse.segments(texte, 'P1-31')['dispositif']
    des = sources.designations()
    out = {}
    # Une division ne compte que si elle est **désignée comme feuille** d'une
    # abrogation : sa désignation close par « du même code » ou par le nom du
    # code. Sans cette ancre de fin, la désignation d'une division mère est
    # sous-chaîne de celle de ses filles, et le relevé passait de 220 articles
    # à 2 253 — toute la hiérarchie au-dessus de chaque bloc.
    for d, arts in sorted(des.items(), key=lambda kv: -len(kv[0])):
        if (d + ' du même code') in seg or (d + ' du code général des impôts') in seg:
            for a in arts:
                out.setdefault(a, ('P1-31', 'abrogation entière par division', d))
    return out
