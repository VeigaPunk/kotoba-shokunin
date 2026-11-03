#!/usr/bin/env python3
"""Owned neutral runner. No upstream imports or evaluation calls."""
import json,pathlib,subprocess,sys,tempfile,hashlib
cases=json.loads(pathlib.Path(__file__).with_name('CASES.json').read_text())
exe=pathlib.Path(sys.argv[1]).resolve(); results=[]
for case in cases:
 with tempfile.TemporaryDirectory() as d:
  root=pathlib.Path(d);train=root/'train.json';valid=root/'valid.json'
  data=case['train']; recipe=case.get('recipe','')
  if recipe.startswith('query'):data=[{'query':'x'*int(recipe[5:]),'should_trigger':True}]
  if recipe.startswith('rows'):data=[{'query':str(i),'should_trigger':False} for i in range(int(recipe[4:]))]
  blob=case.get('raw',json.dumps(data,ensure_ascii=False)).encode()
  if recipe=='bytes1048577':blob=b' '*1048577
  if recipe=='invalid_utf8':blob=b'\xff'
  if recipe!='missing':train.write_bytes(blob)
  argv=[sys.executable,'-I',str(exe),str(train)]
  if 'validation' in case:valid.write_text(json.dumps(case['validation']));argv+=['--validation',str(valid)]
  argv+=case['args']; before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in root.iterdir()}
  a=subprocess.run(argv,capture_output=True,timeout=10);b=subprocess.run(argv,capture_output=True,timeout=10)
  try:actual=json.loads(a.stdout)
  except Exception:actual=None
  after={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in root.iterdir()}
  ok=a.returncode==case['exit'] and actual==case['expected'] and not a.stderr and (a.returncode,a.stdout,a.stderr)==(b.returncode,b.stdout,b.stderr) and before==after
  results.append({'id':case['id'],'pass':ok,'exit':a.returncode,'actual':actual,'stderr':a.stderr.decode(errors='replace')})
print(json.dumps({'passed':sum(r['pass'] for r in results),'total':len(results),'results':results},indent=2))
sys.exit(0 if all(r['pass'] for r in results) else 1)
