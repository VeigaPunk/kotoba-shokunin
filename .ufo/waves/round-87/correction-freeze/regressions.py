"""Supplementary post-first-output regression freeze, not original47."""
import subprocess,tempfile,pathlib,json,sys
cases=[('runs_leading_zeroes',['--runs','0'*5000+'3'],0,'1/2',None),('runs_large_invalid',['--runs','9'*5000],2,None,None),('decimal_leading_zeroes',['--threshold','0'*5000+'.5'],0,'1/2',None),('fraction_leading_zeroes',['--threshold','0'*5000+'1/'+'0'*5000+'2'],0,'1/2',None)]
out=[]
with tempfile.TemporaryDirectory() as d:
 p=pathlib.Path(d)/'input.json';p.write_text('[{"query":"a","should_trigger":true}]')
 for name,args,code,threshold,count in cases:
  r=subprocess.run([sys.executable,'-I',sys.argv[1],str(p),*args],capture_output=True,text=True,timeout=10)
  try:a=json.loads(r.stdout)
  except Exception:a=None
  expected={'status':'invalid','diagnostics':[{'code':'INVALID_INPUT','set':'settings','indexes':[]}],'boundary':None} if code==2 else {'status':'ok','diagnostics':[],'boundary':{'runs':3,'threshold':threshold,'equality_reachable':False,'equality_count':count}}
  out.append({'id':name,'exit':r.returncode,'actual':a,'pass':r.returncode==code and a==expected and not r.stderr})
print(json.dumps(out,indent=2));sys.exit(not all(r['pass'] for r in out))
