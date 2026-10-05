# Relevé de siège des prélèvements — trou d'adresse au 1er octobre 2026

Ce relevé mesure, pour chaque prélèvement portant un sort actif dans le référentiel de sort, si la table de passage lui attribue un siège juridique (colonne `siege_code_normalise`). Il relève les manques ; il ne les comble pas. Aucune adresse n'est ici proposée, déduite ni inventée.

**Avertissement sur la pièce jointe** — la table de passage versée au projet (`referentiels/table_passage_schema_prelevements_20260930.tsv`) porte un état antérieur à l'attribution des sorts : un correctif de deux lignes sur « dont forfaits de cotisation » lui est dû et n'a pas été appliqué ; le présent relevé a été établi sur cet état, sans le corriger.

## Pièces jointes et clé de jointure

- Référentiel de sort : `referentiels/sort_prelevements_20260930.tsv`
- Table de passage (porteuse du siège) : `referentiels/table_passage_schema_prelevements_20260930.tsv`
- Clé employée : le **libellé exact du prélèvement** (colonne `libelle` des deux pièces), seule colonne commune identifiante. La jointure prend sur la totalité des lignes : aucun libellé du référentiel de sort n'est absent de la table de passage.

## Mesure d'entrée

| Mesure | Nombre |
|---|---|
| Lignes du référentiel de sort | 420 |
| Lignes de la table de passage | 420 |
| Prélèvements portant un sort actif (hors « non touché » et « hors mandat ») | 326 |
| Parmi eux, sans siège (`siege_code_normalise` vide ou absent) | 101 |

Les 94 lignes écartées sont les 83 cotisations sociales « hors mandat » et les 11 lignes « non touché » (contributions sur les revenus de remplacement, prélèvements sociaux sur les revenus du capital, CASA).

## Poids du trou

| Grandeur | Montant |
|---|---|
| Rendement 2026 des prélèvements à sort actif (lignes chiffrées) | 857,9 Md€ |
| Rendement 2026 des lignes sans siège | 59,1 Md€ |
| Part du trou | 6,9 % |

Le rendement 2026 n'est pas renseigné sur 35 des 101 lignes sans siège : le montant du trou est un plancher.

## Sous-totaux par famille d'assiette

| Assiette | Lignes sans siège | Rendement |
|---|---|---|
| 6. La consommation | 37 | 21,4 Md€ |
| 3. Les taxes sur la masse salariale | 8 | 18,9 Md€ |
| 7. La propriété et les droits d'usage | 38 | 9,7 Md€ |
| 5. L'activité des entreprises | 14 | 5,1 Md€ |
| 4. Le revenu des personnes | 2 | 2,4 Md€ |
| 8. Hors champ | 2 | 1,7 Md€ |
| **Ensemble** | **101** | **59,1 Md€** |

## Détail — lignes sans siège portant un rendement, par rendement décroissant

| Libellé exact | Rendement 2026 | Sort | Assiette | Impôt absorbant |
|---|---|---|---|---|
| Taxe sur les salaires | 17,9 Md€ | supprimé | 3. Les taxes sur la masse salariale | — |
| Accise sur les énergies, perçue sur les gazoles et les essences, en métropole [part régionale] | 6,3 Md€ | maintenu à part | 6. La consommation | — |
| Accise sur les énergies, perçue sur les gazoles et les essences, en métropole [fractions transférées en compensation du transfert du RMI/RSA et dans le cadre de l'acte II de la décentralisation] | 5,8 Md€ | maintenu à part | 6. La consommation | — |
| Autres taxes | 5,0 Md€ | supprimé | 7. La propriété et les droits d'usage | — |
| Contribution exceptionnelle sur les bénéfices des entreprises | 4,0 Md€ | fondu | 5. L'activité des entreprises | impôt sur les sociétés |
| Redevances pour pollution de l'eau, redevances pour modernisation des réseaux de collecte, redevance sur la consommation d'eau potable, … redevance pour obstacle sur les cours d'eau | 2,5 Md€ | supprimé | 6. La consommation | — |
| Autres impôts directs perçus par voie d'émission de rôles | 2,4 Md€ | fondu | 4. Le revenu des personnes | impôt sur le revenu |
| Contribution tarifaire d'acheminement (CTA) | 2,2 Md€ | supprimé | 6. La consommation | — |
| Droit d'octroi de mer et droit d'octroi de mer régional | 1,7 Md€ | maintenu à part | 6. La consommation | — |
| Recettes issues de la mise aux enchères des « quotas carbone » | 1,5 Md€ | hors champ | 8. Hors champ | — |
| Taxe d'aménagement | 1,5 Md€ | fondu | 7. La propriété et les droits d'usage | taxe foncière |
| Droit sur les bières et les boissons non alcoolisées | 1,2 Md€ | maintenu à part | 6. La consommation | — |
| Taxe sur le patrimoine financier | 1,0 Md€ | supprimé | 7. La propriété et les droits d'usage | — |
| Prélèvement sur les contrats d'assurance de biens | 672,3 M€ | maintenu à part | 6. La consommation | — |
| Timbre unique | 567,0 M€ | supprimé | 7. La propriété et les droits d'usage | — |
| Contribution annuelle au fonds de développement pour l'insertion professionnelle des handicapés (FIPH) | 507,0 M€ | supprimé | 3. Les taxes sur la masse salariale | — |
| Taxe « petit colis » | 500,0 M€ | supprimé | 6. La consommation | — |
| Fraction des droits de timbre sur les passeports sécurisés | 392,7 M€ | supprimé | 7. La propriété et les droits d'usage | — |
| Contribution de la Caisse des dépôts et consignations représentative de l'impôt sur les sociétés | 374,0 M€ | fondu | 5. L'activité des entreprises | impôt sur les sociétés |
| TA-CVAE — Taxe additionnelle à la cotisation sur la valeur ajoutée des entreprises pour frais de chambres de commerce et d'industrie de région | 326,3 M€ | supprimé | 5. L'activité des entreprises | — |
| TA-CFE - fraction CCI-R de la Taxe additionnelle à la cotisation foncière des entreprises pour frais de chambres de commerce et d'industrie de région | 280,7 M€ | fondu | 7. La propriété et les droits d'usage | taxe foncière |
| Taxe sur les surfaces commerciales | 240,6 M€ | fondu | 7. La propriété et les droits d'usage | taxe foncière |
| PEFPC : Participation au financement de la formation des professions non salariées (à l'exception des artisans et des exploitants agricoles) correspondant à 0,25 % du plafond de la sécurité sociale | 204,0 M€ | supprimé | 3. Les taxes sur la masse salariale | — |
| Taxe sur les rachats d'actions | 200,0 M€ | fondu | 5. L'activité des entreprises | impôt sur les sociétés |
| Redevances perçues à l'occasion des procédures et formalités en matière de propriété industrielle ainsi que de registre du commerce et des sociétés, établies par divers textes | 186,9 M€ | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Taxe spéciale sur certains véhicules routiers | 176,5 M€ | supprimé | 5. L'activité des entreprises | — |
| Redevance pour création de bureaux ou de locaux de recherche en région Ile-de-France | 161,1 M€ | supprimé | 7. La propriété et les droits d'usage | — |
| Redevance hydraulique | 150,8 M€ | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Fraction des produits annuels de la vente de biens confisqués | 150,6 M€ | hors champ | 8. Hors champ | — |
| Cotisation BTP intempéries | 128,3 M€ | supprimé | 3. Les taxes sur la masse salariale | — |
| Taxe de balayage | 111,6 M€ | fondu | 7. La propriété et les droits d'usage | taxe foncière |
| Taxe sur les biens des industries de la fonderie (TBIF), de la soudure (TBIS), aérauliques et thermique (TBIAT), de la construction métallique (TBICC) et des industries mécaniques (TBIC) | 109,8 M€ | supprimé | 6. La consommation | — |
| Contribution des assurés | 109,5 M€ | maintenu à part | 6. La consommation | — |
| PEFPC : Participation au financement de la formation des professions non salariées (artisans) correspondant à 0,29 % du plafond de la sécurité sociale, dont micro entrepreneurs | 95,0 M€ | supprimé | 3. Les taxes sur la masse salariale | — |
| Contribution générale sur les boissons alcoolique, tarif sur les boissons édulcorées | 70,0 M€ | supprimé | 6. La consommation | — |
| Taxe sur le transport aérien de passagers, majoration Corse (TAP) et taxe sur le transport maritime de passagers dans certains territoires côtiers (TMPTC) | 53,6 M€ | supprimé | 6. La consommation | — |
| Taxe pour le développement de la formation professionnelle dans les métiers de la réparation de l'automobile, du cycle et du motocycle | 28,8 M€ | supprimé | 3. Les taxes sur la masse salariale | — |
| Fraction du prélèvement sur les jeux de loterie correspondant aux jeux dédiés au patrimoine | 26,5 M€ | maintenu à part | 6. La consommation | — |
| Taxe sur les déchets mis en décharge (TDMD) et taxe sur les déchets incinérés (TDI), majoration locale | 26,0 M€ | supprimé | 6. La consommation | — |
| Fraction des droits de timbre sur les cartes nationales d'identité | 25,2 M€ | supprimé | 7. La propriété et les droits d'usage | — |
| Taxes sur les stations et liaisons radioélectriques privées | 23,6 M€ | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Taxe additionnelle régionale de 15% à la taxe de séjour IDF | 20,3 M€ | maintenu à part | 6. La consommation | — |
| Taxe sur les biens des industries de l'horlogerie, de la bijouterie-joaillerie, de l'orfèvrerie et des arts de la table (TBIHBJOAT) | 20,0 M€ | supprimé | 6. La consommation | — |
| Taxe sur les biens des industries du cuir, de la chaussure et de la maroquinerie (TBICCM) | 18,1 M€ | supprimé | 6. La consommation | — |
| Taxe annuelle sur la vente des produits phytopharmaceutiques | 17,7 M€ | supprimé | 6. La consommation | — |
| Taxe sur la publicité diffusée au moyen de documents imprimés (ex-taxe sur certaines dépenses de publicité) | 14,9 M€ | supprimé | 6. La consommation | — |
| Taxe sur les biens des industries de l'ameublement (TBIA) et taxe sur les biens des industries du bois (TBIB) | 14,2 M€ | supprimé | 6. La consommation | — |
| Taxe sur les biens des industries du béton (TBIB), des matériaux de construction en terre cuite (TBIMCT) et des roches ornementales et de construction (TBIROC) | 13,2 M€ | supprimé | 6. La consommation | — |
| PEFPC : Participation au financement de la formation des professions non salariées (Artistes auteurs) correspondant au minimum à 0,1 % du plafond de la SS | 13,1 M€ | supprimé | 3. Les taxes sur la masse salariale | — |
| Cotisation versée par les organismes HLM | 11,3 M€ | supprimé | 5. L'activité des entreprises | — |
| Redevance due par les titulaires de titres d'exploitation de mines d'hydrocarbures liquides ou gazeux | 11,0 M€ | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Taxe sur les biens des industries de l'habillement (TBIH) | 9,8 M€ | supprimé | 6. La consommation | — |
| Taxe relative à la mise sur le marché des produits phytopharmaceutiques et de leurs adjuvants, des matières fertilisantes et de leurs adjuvants et des supports de culture | 9,5 M€ | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Contribution forfaitaire annuelle à la charge des professionnels de santé | 8,3 M€ | supprimé | 5. L'activité des entreprises | — |
| Taxe sur le biens des industries de la plasturgie et des composites (TBIPC) | 7,4 M€ | supprimé | 6. La consommation | — |
| Autres droits et recettes accessoires | 4,5 M€ | supprimé | 7. La propriété et les droits d'usage | — |
| Taxe sur les installations nucléaires de base relevant du secteur énergétique et assimilées, tarif de stockage (TINB-E, TC) | 3,3 M€ | supprimé | 5. L'activité des entreprises | — |
| Taxe pour le développement de l'industrie de la conservation des produits agricoles (CTCPA) | 2,9 M€ | supprimé | 6. La consommation | — |
| Taxe sur les biens des industrie du papier (TBIP) | 2,8 M€ | supprimé | 6. La consommation | — |
| Indemnité de défrichement | 2,0 M€ | fondu | 7. La propriété et les droits d'usage | taxe foncière |
| Taxe sur les biens des industries des corps gras (TICG) | 0,8 M€ | supprimé | 6. La consommation | — |
| Taxe due par les concessionnaires de mines d'or … exploitées en Guyane (taxe additionnelle aurifère) | 0,8 M€ | supprimé | 5. L'activité des entreprises | — |
| Redevance perçue à l'occasion de l'introduction des familles étrangères en France | 0,8 M€ | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Droit d'examen du permis de chasse | 0,7 M€ | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Taxe annuelle sur les engins maritimes à usage personnel (TAEMUP) – Fraction perçue sur les engins ne battant pas pavillon français | 0,2 M€ | supprimé | 6. La consommation | — |
| Actes et écrits assujettis au timbre de dimension | 0,0 M€ | supprimé | 7. La propriété et les droits d'usage | — |

## Détail — lignes sans siège dont le rendement 2026 n'est pas renseigné

| Libellé exact | Sort | Assiette | Impôt absorbant |
|---|---|---|---|
| Soulte rhum et tafias | maintenu à part | 6. La consommation | — |
| Taxe sur les boissons « premix » | maintenu à part | 6. La consommation | — |
| Sommes constatées par les clubs de jeux au titre des « orphelins » | maintenu à part | 6. La consommation | — |
| Majoration de la taxe sur les assurances de protection juridique au profit du Conseil national des barreaux | maintenu à part | 6. La consommation | — |
| Taxe sur les primes d'assurances | maintenu à part | 6. La consommation | — |
| Taxe sur le transport aérien de marchandises | supprimé | 6. La consommation | — |
| Taxes sur l'immatriculation des véhicules, taxe sur la masse en ordre de marche des véhicules de tourisme | supprimé | 6. La consommation | — |
| Taxes sur l'immatriculation des véhicules, taxe sur les émissions de dioxyde de carbone des véhicules de tourisme | supprimé | 6. La consommation | — |
| Taxe sur les papiers graphiques | supprimé | 6. La consommation | — |
| Droits d'importation | maintenu à part | 6. La consommation | — |
| Financement des congés individuels de formation des salariés sous contrats à durée déterminée CIF-CDD | supprimé | 3. Les taxes sur la masse salariale | — |
| Taxe spéciale due en cas de non-respect de l'engagement de conserver pendant 5 ans les parts de FCPR ou FCPI | fondu | 4. Le revenu des personnes | impôt sur le revenu |
| Versement pour sous-densité | fondu | 7. La propriété et les droits d'usage | taxe foncière |
| Droits sur les actes judiciaires et extrajudiciaires | supprimé | 7. La propriété et les droits d'usage | — |
| Taxe sur les émoluments | supprimé | 7. La propriété et les droits d'usage | — |
| Taxe applicable aux demandes de validation d'une attestation d'accueil | supprimé | 7. La propriété et les droits d'usage | — |
| Taxe annuelle due par les laboratoires de biologie médicale | supprimé | 5. L'activité des entreprises | — |
| Contribution annuelle au profit de l'Institut de radioprotection et de sûreté nucléaire | supprimé | 5. L'activité des entreprises | — |
| Cotisation interprofessionnelle étendue Équarrissage | supprimé | 5. L'activité des entreprises | — |
| Taxe sur les entreprises ayant bénéficié de quotas d'émission de gaz à effet de serre | supprimé | 5. L'activité des entreprises | — |
| Taxe sur les installations nucléaires de base concourant à la gestion des substances radioactives | supprimé | 5. L'activité des entreprises | — |
| Participation pour non-réalisation d'aires de stationnement | fondu | 7. La propriété et les droits d'usage | taxe foncière |
| Taxe pour frais de chambre de métiers d'Alsace | fondu | 7. La propriété et les droits d'usage | taxe foncière |
| Taxe pour frais de chambre de métiers de Moselle | fondu | 7. La propriété et les droits d'usage | taxe foncière |
| Taxe additionnelle au droit de bail | fondu | 7. La propriété et les droits d'usage | impôt sur le revenu |
| Garantie des matières d'or et d'argent | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Redevance sanitaire liée à la certification des végétaux à l'exportation | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Redevances versées pour la délivrance des certificats d'obtention végétale | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Redevance proportionnelle sur le résultat normatif des concessions hydroélectriques soumises aux « délais glissants » | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Redevance pour examen du code de la route | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Taxe sur les demandes de visa ou de renouvellement de visa de publicité et sur les dépôts de publicité pharmaceutiques | sortie du périmètre des PO | 7. La propriété et les droits d'usage | — |
| Redevance pour les contrôles vétérinaires et phytosanitaires des végétaux à l'importation | supprimé | 7. La propriété et les droits d'usage | — |
| Redevance relative aux contrôles renforcés à l'importation des denrées alimentaires d'origine non animale | supprimé | 7. La propriété et les droits d'usage | — |
| Participation des concessionnaires de la liaison fixe Trans-Manche au fonctionnement de la commission intergouvernementale et du comité de sécurité | supprimé | 7. La propriété et les droits d'usage | — |
| Contributions versées par la SNCF au titre des frais de surveillance et de contrôle des chemins de fer | supprimé | 7. La propriété et les droits d'usage | — |

## À trancher

- Périmètre du sort « actif » : la définition retenue ici est littérale — tout sort autre que « non touché » et « hors mandat ». Elle inclut donc les 2 lignes « hors champ » (assiette 8, produits non fiscaux) et les lignes « sortie du périmètre des PO », dont on peut soutenir qu'elles n'appellent aucune adresse. Les en retirer ramènerait le trou de 101 à 82 lignes et de 59,1 à 56,9 Md€.
- Le correctif de deux lignes dû à la table de passage sur « dont forfaits de cotisation » n'est pas appliqué : à sa reprise, le relevé devra être rejoué.
