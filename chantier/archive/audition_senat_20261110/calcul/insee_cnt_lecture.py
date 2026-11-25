import sys, pandas as pd
x=pd.ExcelFile(sys.argv[1], engine='xlrd')
for s in sys.argv[2:]:
    df=x.parse(s, header=None)
    print('=====',s)
    for _,r in df.iterrows():
        vals=[str(v)[:60] if isinstance(v,str) else ('' if pd.isna(v) else round(float(v),2)) for v in r.tolist()]
        if any(v!='' for v in vals): print(' | '.join(map(str,vals)))
