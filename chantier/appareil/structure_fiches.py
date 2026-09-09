# -*- coding: utf-8 -*-
"""La structure de la série : qui porte quel gain, quelle perte, dans quel ordre.

C'est le document arbitré par l'auteur. `carte_attribution.py` le rend lisible,
`generer_fiches.py` l'exécute. **Une seule source** : la structure décide, les
deux autres suivent.

Chaque entrée : identifiant, titre d'affichage, axe en une ligne, gains
d'attache dans l'ordre de lecture, pertes. Un gain se dit en entier chez son
attache ; partout ailleurs il revient en rappel.
"""

# (id, titre d'affichage, axe, [gains d'attache], [pertes d'attache])
STRUCTURE = [
 ('C-01', 'Contribuable', 'Ce que l’État vous prend, et de combien ça baisse.',
  ['D11-e1', 'D2-5-1-e2', 'D2-4-1-e2', 'D6-2-2-e2', 'D2-2-1-e2', 'D5-2-1-e2',
   'D9-2-2-e1', 'D2-5-1-e1', 'D1-3-1', 'D6-2-2-e5'], []),
 ('C-02', 'Citoyen', 'Un État qui fait moins, et qui le fait bien.',
  ['D6-2-2-e6', 'D6-ei2', 'D2-3-1-e1', 'D5-3-3-e1', 'D5-2-1-e1', 'D1-1-1',
   'D1-2-1', 'D7-4-1-e1', 'D9-3-1-e5', 'D9-3-1-e4', 'D6-2-2-e3',
   'D11-4-1-e1'], ['D3-2-1-e4']),
 ('C-03', 'Foyer', 'Votre patrimoine : ce qu’on vous rend, ce que vous gardez.',
  ['D7-2-1-e1', 'D10-4-1-e5', 'D4-4-1-e1', 'D9-3-1-e3'], ['D2-4-1-s8']),
 ('C-04', 'Travailleur', 'Ce que votre travail vous rapporte enfin.',
  ['D3-2-2-e1', 'D3-2-1-e1', 'D9-3-1-e1', 'D8-2-2-e1', 'D8-2-1-e2',
   'D8-2-2-e2', 'D8-2-2-e4', 'D10-4-1-e1'], []),
 ('C-16', 'Jeune adulte', 'Démarrer dans la vie sans être plombé.',
  ['D9-2-1', 'D10-4-1-e4', 'D10-4-1-e2', 'D10-4-1-e6', 'D10-4-2-e1',
   'D10-4-2-e2', 'D10-4-2-e3', 'D9-4-1-e2'], ['D10-4-1-e3']),
 ('C-10', 'Personne sans emploi',
  'Six mois de solidarité, puis un compte à vous et un marché qui embauche.',
  ['D8-3-1-e1', 'D8-3-1-e2', 'D3-ei2'],
  ['D8-3-1', 'D2-4-1-s2', 'D2-4-1-s6']),
 ('C-06', 'Entreprise', 'Produire sans être taxé avant d’avoir gagné.',
  ['D4-3-3-e2', 'D4-3-1-e1', 'D4-2-3', 'D4-2-1-e1', 'D3-ei1', 'D9-3-1-e6',
   'D4-ei1', 'D4-ei2', 'D8-ei1'], ['D4-3-3', 'D3-2-1-e2']),
 ('C-05', 'Agent public indispensable', 'Mieux payé, mieux équipé, mieux jugé.',
  ['D6-3-2-e2', 'D6-3-1-e2', 'D6-3-2-e1', 'D6-3-1-e1'], ['D6-3-1']),
 ('C-30', 'Agent public dont le poste est supprimé',
  'Partir avec de quoi rebondir.',
  ['D6-2-2', 'D6-2-2-e7', 'D6-2-2-e4'], ['D2-2-1']),
 ('C-19', 'Enseignant',
  'Vous choisissez où vous enseignez, et ce que vous valez se négocie.',
  ['D10-3-1-e3', 'D10-3-1-e1', 'D10-3-1-e2'], ['D6-3-1']),
 ('C-17', 'Famille', 'Ce que vos enfants coûtent, et ce qu’on vous rend.',
  ['D9-4-1-e1', 'D10-2-1-e1', 'D10-3-1-e4', 'D10-3-1-e6', 'D9-4-2-e2'],
  ['D9-4-1']),
 ('C-09', 'Retraité',
  'Votre part des 20 000 € vous revient en rente, à vie.',
  ['D7-2-2-e1', 'D8-2-1-e1', 'D8-4-2-e4'], ['D9-3-1-e7', 'D7-2-2']),
 ('C-11', 'Locataire', 'Se loger, dans un marché qui se détend.',
  ['D7-3-1-e1'], ['D2-4-1-s1', 'D7-3-1']),
 ('C-13', 'Patient', 'Ce que les soins vous coûtent, plafonné.',
  ['D8-4-1-e1', 'D8-4-2-e1', 'D8-4-2-e3', 'D8-4-2-e2'], ['D8-4-1']),
 ('C-23', 'Consommateur', 'Des prix qui baissent, et le choix qui s’élargit.',
  ['D4-3-3-e1', 'D4-3-2-e1'], ['D4-3-2']),
 # Ce que le bénéficiaire d'un chèque gagne d'abord, c'est du salaire, non une
 # aide de remplacement : arbitrage de l'auteur du 20260828. La hausse du
 # salaire passe donc en tête, et l'aide libre vient après.
 ('C-32', 'Bénéficiaire d’un chèque ciblé',
  'Votre salaire net monte, et votre aide devient de l’argent libre.',
  ['D2-4-1-e1', 'D9-2-1-e1', 'D5-3-4'], ['D2-4-1-s9']),
 ('C-33', 'Entreprise ou association subventionnée',
  'La liberté d’agir sans formulaire, et des clients plus riches.',
  [], ['D2-4-1-s3']),
 ('C-14', 'Personne handicapée',
  'Une part supplémentaire d’aide, et un reste à charge plafonné.',
  ['D9-2-3-e1'], []),
]
