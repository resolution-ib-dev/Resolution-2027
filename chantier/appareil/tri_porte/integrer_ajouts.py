"""integrer_ajouts.py — intégration du 20261109 : les P1 n° 36, 37 et 38 du tri cessent d'être des amendements
nouveaux et rejoignent les amendements existants qui portent le même objet au même endroit.

  n° 36, I et II (impositions d'État)        → n° 22 (après l'art. 19), I, 4° à 7°, et II, 3°
  n° 36, III (Caisse des dépôts à l'IS)      → n° 23 (après l'art. 32), III
  n° 37 (impositions locales)                → n° 29 (après l'art. 27), III bis
  n° 38 (taxes affectées hors CGI)           → n° 25 (après l'art. 42), I, 8° et 10° à 17°

Le n° 35 (suppression de l'art. 15) et le PLFSS n° 9 restent seuls. Écrit sur la liasse, qui fait
foi pour les n° 22, 23, 25 et 29 ; refuse de jouer deux fois. Se joue depuis ce dossier."""
import re, sys

D = '/home/user/Resolution-2027/chantier/livrables/depot_2027/'
P1 = D + 'LIASSE_PLF_P1.md'
t = open(P1, encoding='utf-8').read()
if '## Amendement n° 36 [' not in t:
    sys.exit('déjà intégré')


def bloc(n):
    i = t.index(f'## Amendement n° {n} [')
    j = t.find('\n---\n\n## Amendement n° ', i)
    return i, (len(t) if j < 0 else j)


NB = '\u00a0'


def typo(s):
    """typographie de la liasse : celle de verser_amendements.typo"""
    s = s.replace("'", '’')
    s = re.sub(r' ([:;!?»%])', NB + r'\1', s)
    s = re.sub(r'« ', '«' + NB, s)
    s = re.sub(r'(\d) (\d{3})\b', r'\1' + NB + r'\2', s)
    return s


def remplace(n, paires):
    global t
    i, j = bloc(n)
    s = t[i:j]
    for a, b in paires:
        a, b = typo(a), typo(b)
        assert s.count(a) == 1, (n, a[:70], s.count(a))
        s = s.replace(a, b)
    t = t[:i] + s + t[j:]


# ------------------------------------------------------------------ n° 22
remplace(22, [
    ('## Amendement n° 22 [Taxes d’État : vingt et une disparaissent dans l’impôt, sans hausse du total]',
     '## Amendement n° 22 [Taxes d’État : quarante-huit disparaissent dans l’impôt, sans hausse du total]'),
    ('3° L’article L. 313-6 du code de l’entrée et du séjour des étrangers et du droit d’asile.\n',
     '3° L’article L. 313-6 du code de l’entrée et du séjour des étrangers et du droit d’asile.\n\n'
     '4° Les articles 235 ter ZG, 302 bis N, 302 bis O, 302 bis P, 302 bis R, 302 bis S, 302 bis T, 302 bis U, 302 bis V, '
     '302 bis W, 302 bis WA, 302 bis WB, 302 bis WC, 302 bis WD, 302 bis WE, 302 bis WF, 302 bis WG, 302 bis X, 302 bis XA, '
     '1605 nonies, 1609 novovicies, 1609 tricies, 1609 untricies, 1609 duotricies, 1609 tertricies, 1613 ter, 1613 quater, '
     '1635 bis AE, 1635 bis AF, 1635 bis AG et 1635 bis AH du code général des impôts.\n\n'
     '5° Le 5° ter de l’article 1001 du même code.\n\n'
     '6° Les I et II de l’article 138 de la loi n° 2019-486 du 22 mai 2019 relative à la croissance et la transformation des entreprises.\n\n'
     '7° Les articles L. 421-93 à L. 421-148, L. 421-151, L. 421-156 à L. 421-167 et L. 455-44 à L. 455-56 du code des '
     'impositions sur les biens et services.\n'),
    ('2° Les articles L. 453-1 à L. 453-12, L. 453-45 à L. 453-83 et L. 454-29 à L. 454-38 du code des impositions sur les biens et services.\n',
     '2° Les articles L. 453-1 à L. 453-12, L. 453-45 à L. 453-83 et L. 454-29 à L. 454-38 du code des impositions sur les biens et services.\n\n'
     '3° Les articles 231 ter, 231 quater, 302 bis ZA, 990 D, 990 E, 990 F, 990 FA et 990 G du code général des impôts.\n'),
    ('Par dérogation, l’abrogation des articles 235 ter C, 235 ter X et 235 ter ZC du code général des impôts s’applique aux exercices ouverts à compter du 1er juillet 2027.',
     'Par dérogation, l’abrogation des articles 235 ter C, 235 ter X et 235 ter ZC du code général des impôts s’applique aux exercices ouverts à compter du 1er juillet 2027. '
     'Les taxes mentionnées au 7° du I sont dues au titre de l’année 2027 à raison de la seule durée d’affectation des véhicules ou de détention des autorisations antérieure au 1er juillet 2027.'),
    ('Cet amendement supprime vingt et une impositions de l’État, au 1er juillet 2027.',
     'Cet amendement supprime quarante-huit impositions de l’État, au 1er juillet 2027 et au 1er janvier 2028.'),
    ('sur la demande de naturalisation ou sur l’attestation d’accueil¹. Chacun',
     'sur la demande de naturalisation ou sur l’attestation d’accueil¹. S’y ajoutent des dizaines de prélèvements à assiette étroite : '
     'redevances sanitaires d’abattage, de découpage et de contrôle à l’importation, droits sur les demandes d’autorisation de médicaments, '
     'taxes sur les boissons, prélèvements sur les jeux, dont ceux de la Française des jeux sur ses loteries, taxes sur l’affectation '
     'des véhicules, taxes sur les bureaux d’Île-de-France et de Provence, taxe sur la valeur vénale des immeubles. Chacun'),
    ('Ce jour-là tombent les droits de timbre, la taxe sur les transactions financières, la taxe sur les rachats d’actions et la contribution de sécurité immobilière.',
     'Ce jour-là tombent les droits de timbre, la taxe sur les transactions financières, la taxe sur les rachats d’actions, la contribution de sécurité immobilière, '
     'les redevances et taxes perçues par opération et les prélèvements sur les jeux ; les taxes sur les véhicules et les fréquences ne sont dues pour 2027 qu’au premier semestre.'),
    ('L’État cesse d’instruire, de contrôler et de recouvrer vingt et une impositions', 'L’État cesse d’instruire, de contrôler et de recouvrer quarante-huit impositions'),
    ('Vingt et une impositions se fondent dans un impôt unique', 'Quarante-huit impositions se fondent dans un impôt unique'),
    ('² Code général des impôts, code des impositions sur les biens et services et code de l’entrée et du séjour des étrangers et du droit d’asile.',
     '² Code général des impôts, code des impositions sur les biens et services, code de l’entrée et du séjour des étrangers et du droit d’asile et loi n° 2019-486 du 22 mai 2019.'),
])

# ------------------------------------------------------------------ n° 23
remplace(23, [
    ('III. – Les I et II s’appliquent aux exercices ouverts à compter du 1er juillet 2027.',
     'III. – A. – Le 1 de l’article 206 du code général des impôts est complété par un alinéa ainsi rédigé :\n\n'
     '« La Caisse des dépôts et consignations est passible de l’impôt sur les sociétés à raison du résultat net de son activité pour compte propre. »\n\n'
     'B. – À l’article L. 518-16 du code monétaire et financier, les mots : « d’une contribution représentative de l’impôt sur les sociétés » '
     'sont remplacés par les mots : « de l’impôt sur les sociétés ».\n\n'
     'IV. – Les I à III s’appliquent aux exercices ouverts à compter du 1er juillet 2027.'),
    ('IV. – Lorsque le rapport entre le montant total', 'V. – Lorsque le rapport entre le montant total'),
    ('V. – Le produit résultant du I concourt', 'VI. – Le produit résultant des I et III concourt'),
    ('sans taux réduit, sans quote-part dérogatoire et sans taux nul.',
     'sans taux réduit, sans quote-part dérogatoire et sans taux nul. La Caisse des dépôts et consignations, qui verse une contribution '
     'tenant lieu de l’impôt, y est assujettie dans les conditions du droit commun.'),
])

# ------------------------------------------------------------------ n° 25
remplace(25, [
    ('## Amendement n° 25 [Taxes affectées : cinquante-sept supprimées, fondues en une ressource unique à produit égal]',
     '## Amendement n° 25 [Taxes affectées : soixante-neuf supprimées, fondues en une ressource unique à produit égal]'),
    ('8° Les articles L. 2135-15-1, L. 5424-15,', '8° Les articles L. 2135-15-1, L. 3253-18, L. 5424-15,'),
    ('9° Les articles L. 2333-64 à L. 2333-75 et L. 2531-2 à L. 2531-11 du code général des collectivités territoriales.\n',
     '9° Les articles L. 2333-64 à L. 2333-75 et L. 2531-2 à L. 2531-11 du code général des collectivités territoriales.\n\n'
     '10° Les articles L. 351-12 à L. 351-15 du code général de la fonction publique.\n\n'
     '11° Les articles L. 4031-4 et L. 5141-8 du code de la santé publique.\n\n'
     '12° L’article L. 253-8-2 du code rural et de la pêche maritime.\n\n'
     '13° Le 1° de l’article L. 4316-1 et les articles L. 4316-10 à L. 4316-12 du code des transports.\n\n'
     '14° Les deuxième et dernier alinéas de l’article L. 423-6 du code de l’environnement.\n\n'
     '15° L’article L. 341-6 du code forestier.\n\n'
     '16° L’article L. 132-16 du code minier.\n\n'
     '17° L’article 72 de la loi de finances rectificative pour 2003 (n° 2003-1312 du 30 décembre 2003) et l’article 130 de la loi de finances pour 2007 (n° 2006-1666 du 21 décembre 2006).\n'),
    ('et, pour les contributions assises sur les rémunérations, aux rémunérations versées à compter de cette date.',
     'et, pour les contributions assises sur les rémunérations, aux rémunérations versées à compter de cette date. Par dérogation, '
     'sont dues une dernière fois au titre de l’année 2027 la contribution prévue à l’article L. 351-12 du code général de la fonction publique, '
     'la taxe annuelle prévue au II de l’article L. 5141-8 du code de la santé publique et la taxe prévue à l’article L. 253-8-2 du code rural et de la pêche maritime.'),
    ('Cet amendement supprime cinquante-sept impositions affectées', 'Cet amendement supprime soixante-neuf impositions affectées'),
    ('dialogue social, intempéries du bâtiment, versement mobilité.',
     'dialogue social, intempéries du bâtiment, versement mobilité, garantie des salaires, unions de professionnels de santé, médicaments '
     'vétérinaires, produits phytopharmaceutiques, prise d’eau des voies navigables, permis de chasser, défrichement, mines d’hydrocarbures.'),
    ('ressources locales, redevances de l’eau, bureaux d’Île-de-France.',
     'ressources locales, redevances de l’eau, bureaux d’Île-de-France, insertion des personnes handicapées dans la fonction publique.'),
    ('Cinquante-sept impositions se fondent dans une ressource unique', 'Soixante-neuf impositions se fondent dans une ressource unique'),
])

# ------------------------------------------------------------------ n° 29
remplace(29, [
    ('1520, 1529, 1530, 1530 bis et 1635 quater A du même code sont abrogés.\n',
     '1520, 1529, 1530, 1530 bis et 1635 quater A du même code sont abrogés.\n\n'
     'III bis. – Sont également abrogés :\n\n'
     '1° Les articles 1599 quater C, 1599 quater D, 1601, 1601-0 A, 1604, 1607 bis, 1607 ter, 1609 B, 1609 C, 1609 D, 1609 G, 1609 H, '
     '1609 I, 1635 quater B à 1635 quater N et 1635 quater P à 1635 quater T du code général des impôts.\n\n'
     '2° Les articles L. 2333-49 à L. 2333-55-2, L. 2333-56, L. 2333-81 à L. 2333-83, L. 2333-97, L. 3333-4 à L. 3333-7 et L. 5211-21-1 '
     'du code général des collectivités territoriales.\n\n'
     '3° Les articles L. 331-1 à L. 331-17 du code de l’urbanisme.\n\n'
     '4° Les articles L. 454-39 à L. 454-77 du code des impositions sur les biens et services.\n\n'
     '5° L’article L. 1331-7 du code de la santé publique.\n\n'
     '6° L’article 3 de la loi n° 72-657 du 13 juillet 1972 instituant des mesures en faveur de certaines catégories de commerçants et artisans âgés.\n'),
    ('V. – Les I à III s’appliquent aux impositions établies au titre des années 2028 et suivantes.',
     'V. – Les I à III bis s’appliquent aux impositions établies au titre des années 2028 et suivantes. Par dérogation, l’abrogation par le III bis '
     'des articles L. 2333-49 à L. 2333-53, L. 2333-81 à L. 2333-83 et L. 3333-4 à L. 3333-7 du code général des collectivités territoriales '
     's’applique aux recettes et aux accès réalisés à compter du 1er juillet 2027, celle des articles L. 2333-54 à L. 2333-55-2, L. 2333-56 et '
     'L. 5211-21-1 du même code au produit des jeux réalisé à compter de la même date et celle de l’article L. 1331-7 du code de la santé publique '
     'aux raccordements intervenus à compter de la même date ; celle des articles 1635 quater B à 1635 quater N et 1635 quater P à 1635 quater T '
     'du code général des impôts et des articles L. 331-1 à L. 331-17 du code de l’urbanisme s’applique aux autorisations dont le fait générateur '
     'intervient à compter du 1er janvier 2028.'),
    ('Les impositions établies au titre des années antérieures demeurent dues et sont recouvrées', 'Les impositions établies au titre des années antérieures, ou dont le fait générateur est antérieur aux dates mentionnées à la deuxième phrase, demeurent dues et sont recouvrées'),
    ('Les délibérations prises au titre des impositions supprimées cessent de produire effet au 1er janvier 2028.',
     'Les délibérations prises au titre des impositions supprimées cessent de produire effet au 1er janvier 2028 ou, pour celles qui tombent '
     'au 1er juillet 2027, à cette date. Les dispositions législatives qui affectent tout ou partie du produit des impositions supprimées par '
     'le III bis cessent de s’appliquer aux mêmes dates ; les dispositions réglementaires prises pour l’application des articles abrogés cessent '
     'de produire effet aux mêmes dates.'),
    ('VIII. – La perte de recettes pour l’État est compensée,',
     'VIII. – La perte de recettes résultant du III bis pour les collectivités territoriales est compensée, à due concurrence, par la majoration '
     'de la dotation globale de fonctionnement. La perte de recettes pour l’État est compensée,'),
])
i, j = bloc(29)
s = t[i:j]
k = s.rindex('Certaines des d')
ajout = ('L’amendement supprime avec elle dix-huit impositions locales qui subsistaient à côté : règles annexes de la taxe d’aménagement, '
         'taxes spéciales d’équipement, taxes pour frais de chambres de métiers et d’agriculture, taxe additionnelle spéciale annuelle '
         'd’Île-de-France, taxes sur les surfaces de stationnement et sur les surfaces commerciales, taxe locale sur la publicité extérieure, '
         'taxe de balayage, taxes sur les remontées mécaniques et les sites nordiques, prélèvements communaux sur les jeux des casinos, '
         'participation pour le financement de l’assainissement collectif. Elles tombent au 1er janvier 2028 et, pour celles qui se '
         'perçoivent sur une opération, au 1er juillet 2027 ; les collectivités sont compensées par la dotation globale de fonctionnement. ')
t = t[:i] + s[:k] + typo(ajout) + s[k:] + t[j:]

# ------------------------------------------------------------------ n° 36 à 38 retirés
for n in (38, 37, 36):
    i, j = bloc(n)
    if j < len(t):
        t = t[:i] + t[j + len('\n---\n\n'):]
    else:
        t = t[:i].rstrip('\n') + '\n'          # la liasse finit sur son filet « --- »
for n in (36, 37, 38):
    t = re.sub(rf'\n\| {n} \| [^\n]*', '', t, count=1)

# sommaire : intitulés et compte
for n, o in ((22, 'Taxes d’État : quarante-huit disparaissent dans l’impôt, sans hausse du total'),
             (25, 'Taxes affectées : soixante-neuf supprimées, fondues en une ressource unique à produit égal')):
    t, k = re.subn(rf'(\n\| {n} \| [^|]*\| )[^\n]*( \|)', lambda m: m.group(1) + typo(o) + m.group(2), t, count=1)
    assert k == 1, n
a = 'Trente-huit amendements de première partie, répartis en six lots. La numérotation va de 1 à 38.'
assert t.count(a) == 1
t = t.replace(a, 'Trente-cinq amendements de première partie, répartis en six lots. La numérotation va de 1 à 35.')
open(P1, 'w', encoding='utf-8').write(t)
print('intégré :', len(re.findall(r'\n## Amendement n° \d+ \[', t)), 'amendements en première partie')
