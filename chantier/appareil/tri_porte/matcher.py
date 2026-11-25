import csv, json, re, sys
sys.path.insert(0,'/home/user/Resolution-2027'); sys.path.insert(0,'.')
import droit
from extraire_visas import CODES, NOMS, ART_RE, code_de, CODEPAT
R='/home/user/Resolution-2027/chantier/referentiels/'
S=list(csv.DictReader(open(R+'sort_prelevements_20261015.tsv'),delimiter='\t'))
F=list(csv.DictReader(open(R+'prelevements_forces_20260930.tsv'),delimiter='\t'))
V=json.load(open('visas.json'))
A42=json.load(open('art42.json'))
n=droit.norm_num

def sieges(i):
    s,f=S[i-1],F[i-1]
    out=set()
    if f['siege_code'] and f['siege_article']:
        try: out.add((CODES[f['siege_code'].lower()], n(f['siege_article'])))
        except KeyError: out.add((f['siege_code'], n(f['siege_article'])))
    for txt in (f['siege_declare'], s['siege_article']):
        for part in re.split(r'\s;\s', txt or ''):
            c=None
            m=CODEPAT.search(part)
            if m: c=code_de(part[m.start():m.start()+110], None)
            pre=part[:m.start()] if m else part
            if c is None and f['siege_code']:
                c=CODES.get(f['siege_code'].lower(), f['siege_code'])
            for t in ART_RE.findall(pre):
                if re.fullmatch(r'\d{1,2}',t.strip()) and not re.search(r'\b(?:Art\.?|articles?)\s*'+re.escape(t.strip()), pre): continue
                out.add((c, n(t)))
    return sorted(out, key=str)

VIS={}
for v in V:
    VIS.setdefault((v['code'], n(v['article'])), []).append(v)
VIS_NC={}
for v in V:
    VIS_NC.setdefault(n(v['article']), []).append(v)

L24=[2, 8, 13, 38, 51, 52, 57, 58, 59, 60, 61, 62, 63, 64, 65, 68, 70, 73, 74, 76, 77, 78, 79, 96, 97, 98, 99, 100, 101, 103, 104, 105, 107, 108, 109, 110, 117, 118, 130, 3,4,5,6,7,10,11,12,17,22,23,24,36,37,39,41,42,43,55,56,66,67,71,75,80,81,82,83,84,85,86,87,88,89,90,91,102,106,132,133,134,135,136]
def lignes42(i):
    res=[]
    ss=sieges(i)
    for k,blocs in A42.items():
        b=' '.join(x['brut'] for x in blocs)
        bb=re.sub(r'\s+',' ',b)
        for c,a in ss:
            # numéro d'article présent dans la colonne A du bloc
            arts=[n(t) for t in ART_RE.findall(bb)]
            if a in arts:
                res.append(int(k)); break
    return sorted(set(res))

if __name__=='__main__':
    out=[]
    for i in range(1,len(S)+1):
        ss=sieges(i)
        hits=[]
        for c,a in ss:
            for v in VIS.get((c,a),[]):
                hits.append(f"{v['liasse']} n°{v['n']} : {v['article']} ({v['code']})")
            if not VIS.get((c,a)):
                distinct = bool(re.search(r'[a-z]', a.lstrip('lrdo'))) or a.count('-')>=1
                for v in VIS_NC.get(a,[]):
                    if v['code'] is None or distinct: hits.append(f"{v['liasse']} n°{v['n']} : {v['article']} (code lu : {v['code']})")
        l42=lignes42(i)
        out.append(dict(i=i, libelle=S[i-1]['libelle'], sieges=ss, visas=sorted(set(hits)), l42=l42, l42_24=[x for x in l42 if x in L24]))
    json.dump(out, open('match.json','w'), ensure_ascii=False, indent=0)
    print(sum(1 for o in out if o['visas']), sum(1 for o in out if o['l42_24']))
