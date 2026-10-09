import subprocess, sys, re
AV='/home/claude/work/coffre/livrables/depot_2027/clause_generale_niches_20261005.md'
AP='/home/claude/work/sortie/livrables/depot_2027/clause_generale_niches_20261005.md'
T=open(AP,encoding='utf-8').read()
def f1(s): # désignation fausse
    a='Le 10° de la section IX du chapitre IV'; assert a in s; return s.replace(a,'Le 11° de la section IX du chapitre IV',1)
def f2(s): # article retiré d'un rang
    a=' et l’article 1384 D du même code.'; assert s.count(a)==1; return s.replace(a,' du même code.')
def f3(s): # rang dupliqué
    a='\n> 2° Les a, b et b bis'; assert s.count(a)==1; return s.replace(a,'\n> 1° Les a, b et b bis')
def f4(s): # verdict retourné : un rang F déclaré B et réciproquement, couverture intacte
    s=re.sub(r'(\| F — .*?\| )157°, ',r'\g<1>156°, ',s)
    s=s.replace('| 2° à 11°, 13° à 18°, 21° à 36°, 44°, 48° et 49°, 112° et 113°, 115°, 117°, 130° et 131°, 138°, 141° à 149°, 153° à 156°,','| 2° à 11°, 13° à 18°, 21° à 36°, 44°, 48° et 49°, 112° et 113°, 115°, 117°, 130° et 131°, 138°, 141° à 149°, 153° à 155°, 157°,')
    s=s.replace('celles que le III abroge à ses 157°, 199°','celles que le III abroge à ses 156°, 199°')
    s=s.replace('141° à 149°, 153° à 156°, 158°','141° à 149°, 153° à 155°, 157°, 158°')
    return s
ok=True
for nom,f in (('désignation fausse',f1),('article retiré',f2),('rang dupliqué',f3),('lettre retournée',f4)):
    p='/tmp/claude-0/faute.md'; open(p,'w',encoding='utf-8').write(f(T))
    r=subprocess.run([sys.executable,'controle_regroupement.py',AV,p],capture_output=True,text=True)
    mord = r.returncode!=0
    print(('MORD ' if mord else 'NE MORD PAS ')+nom+' — '+r.stdout.split('\n')[0]); ok&=mord
sys.exit(0 if ok else 1)
