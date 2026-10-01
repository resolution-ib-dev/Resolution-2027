## 20260930 — versement-reprise

**Les deux pièces du 20260928-30 sont reversées en-têtes corrigés, et les deux
opérations d'appareil du mandat sont mesurées bloquées.**

**Ce qui est versé.** `livrables/arborescence_mesures_20260928.md` et
`methode/plan_sept_phases_20260930.md`, en remplacement des versions du matin.
L'arborescence porte désormais son compte juste : **66 mesures sur 65 lignes**,
M-067 et M-068 — deux directions sans dispositif — partageant une ligne ; et
**49 décisions de relecture, dont 45 sur une mesure et 4 sur la portée d'un bloc
ou d'un mouvement**. Les deux écarts que le fil d'inscription avait portés à
l'auteure sont clos : ils étaient d'en-tête, non de fond. Le plan déclare
explicitement la suppression du lot `H`.

La carte reprend ces comptes. L'index ne bouge pas : ses deux entrées portent le
rôle, le chemin, la voie et la famille, aucun chiffre d'en-tête.

---

### Le générateur de l'index a décroché — 253 contre 310

`appareil/generer_index.py`, joué au clone du dépôt, rend **253 artefacts dont
195 au coffre**. Le coffre porte **310 artefacts, 252 au coffre**. L'écart est de
cinquante-sept : les **dix-huit** entrées du 20260930, et **trente-neuf**
déclarations antérieures que la table curée du générateur n'a jamais reçues.

**Conséquence, et c'est elle qui compte.** Un `make index` joué en l'état ne
perdrait pas les dix-huit entrées de ce fil : il en perdrait cinquante-sept. La
table curée se rattrape **avant** tout rejeu de l'index, et le rattrapage porte
sur les trente-neuf autant que sur les dix-huit. Rien n'a été poussé.

**La poussée est refusée, et la mesure nomme son motif.** Le mandataire git rend
un `403` : le dépôt `resolution-ib-dev/Resolution-2027` n'est pas dans l'ensemble
des dépôts autorisés de la session, donc aucune identité n'est injectée. Le clone
en lecture passe. C'est la fermeture d'A-393 constatée mécaniquement, et elle se
lève en déclarant le dépôt aux sources de la session — non depuis ce fil.

### Les empreintes ne sont pas prises

`make coffre` relève l'empreinte de chaque artefact du coffre **au dépôt
courant**, c'est-à-dire aux fichiers que le fil porte. Ce fil ne porte que les
deux pièces reversées : relever sur cet état écrirait deux empreintes et
laisserait les seize autres artefacts du 20260930 sans référence, sans que rien
ne le dise. Le relevé est cumulatif, donc rien ne serait détruit — mais une
empreinte partielle passée pour un relevé complet est exactement ce que le
module interdit. Les dix-huit empreintes restent dues, et elles se prennent dans
la même session que le rattrapage du générateur, sur un coffre déplié.

**Ce que ce fil n'a pas fait, et volontairement.** Aucun contrôle joué, aucune
pièce neuve, aucun paquet de dépôt écrit : le mandat n'en nomme pas.
