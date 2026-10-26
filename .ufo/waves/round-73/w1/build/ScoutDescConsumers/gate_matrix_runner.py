import subprocess,sys,os,json,time,concurrent.futures as cf
P=open('/tmp/k73-scd-P.txt').read().strip()+'/kotoba-shokunin'
BASE='072048fa8e8a52c707d25f7079772fa317244eb7'
tag=sys.argv[1]; rev=sys.argv[2]   # tag, branch/rev
outdir='/tmp/k73-scd-out/'+tag; os.makedirs(outdir,exist_ok=True)
subprocess.run(['git','-C',P,'checkout','-q',rev],check=True)
R=subprocess.check_output(['git','-C',P,'rev-parse','HEAD']).decode().strip()
rv=lambda s:s.replace('<R>',R).replace('<B>',BASE)
G={
'verify_skill_checklist':['verify_skill_checklist.py'],
'sibling_census':['check_sibling_census.py','corpus/knowledge/sibling-overlap-census-round49.md','--province','PROVINCE.md','--skill','SKILL.md'],
'description_thresholds':['check_description_thresholds.py','--rev','<R>'],
'province_core':['check_province_core.py','--rev','<R>'],
'gate_registry':['check_gate_registry.py','--rev','<R>'],
'overlap_levers':['check_overlap_levers.py','--rev','<R>'],
'author_rules':['check_author_rules.py','--rev','<R>'],
'correction_sweep':['check_correction_sweep.py','--root','.'],
'skill_precedence':['check_skill_precedence.py','--rev','<R>'],
'instruction_authority':['check_instruction_authority.py','--rev','<R>'],
'alwayson_boxes':['check_alwayson_boxes.py','--rev','<R>'],
'could_not_evaluate':['check_could_not_evaluate.py','--rev','<R>'],
'routed_repairs':['check_routed_repairs.py','--rev','<R>'],
'routed_repairs_v2':['check_routed_repairs_v2.py','--rev','<R>'],
'r63':['check_r63_routed_repairs.py','--rev','<R>'],'r64':['check_r64_routed_repairs.py','--rev','<R>'],
'r66':['check_r66_routed_repairs.py','--rev','<R>'],'r67':['check_r67_routed_repairs.py','--rev','<R>'],
'r68':['check_r68_routed_repairs.py','--rev','<R>'],'r69':['check_r69_routed_repairs.py','--rev','<R>'],
'r69v2':['check_r69_routed_repairs_v2.py','--rev','<R>'],
'callee_rename':['check_callee_rename.py','--rev','<R>'],
'client_trust':['check_client_trust_gates.py','--rev','<R>'],
'mcp_instr':['check_mcp_instructions.py','--rev','<R>'],
'command_files':['check_command_files.py','--rev','<R>'],
'hook_files':['check_hook_files.py','--rev','<R>'],
'plugin_manifests':['check_plugin_manifests.py','--rev','<R>'],
'scoped_rules':['check_scoped_rules.py','--rev','<R>'],
'scoped_v31':['check_scoped_rules_v31.py','--rev','<R>'],
'scoped_v32':['check_scoped_rules_v32.py','--rev','<R>'],
'explicit_inv':['check_explicit_invocation.py','--rev','<R>'],
'skill_evals':['check_skill_evals.py','--rev','<R>'],
'skill_evals_v2':['check_skill_evals_v2.py','--rev','<R>'],
'opencode_repin':['check_opencode_repin.py','--rev','<R>'],
'substrate_repin_v2':['check_substrate_repin_v2.py','--rev','<R>'],
'sweep_mutants':['check_sweep_mutants.py','--rev','<R>'],
'sources_append_only':['check_sources_append_only.py','--base','422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4','--rev','<R>'],
'gate_finding_delta':['check_gate_finding_delta.py','--base','<B>','--head','<R>'],
'box_proof_case_deletion':['box_proof_case_deletion.py','--rev','<R>'],
'corpus_integrity':['verify_corpus_integrity.py'],
'corpus_independent':['verify_corpus_independent.py'],
'surfaces':['verify_surfaces.py'],
'dispatch_prompts':['verify_dispatch_prompts.py'],
'harness_claims':['verify_harness_claims.py'],
'substrate_pins':['check_substrate_pins.py'],
'compare_harness_independent':['compare_harness_independent.py'],
}
only=sys.argv[3:] 
def run(k):
    a=['python3','-B','verifiers/'+G[k][0]]+[rv(x) for x in G[k][1:]]
    t=time.time()
    try:
        p=subprocess.run(a,cwd=P,capture_output=True,text=True,timeout=120)
        rc,out=p.returncode,(p.stdout+p.stderr)
    except subprocess.TimeoutExpired as e:
        rc,out='TIMEOUT',''
    open(f'{outdir}/{k}.txt','w').write(out)
    return k,rc,round(time.time()-t,1)
ks=only or list(G)
with cf.ThreadPoolExecutor(4) as ex:
    res=list(ex.map(run,ks))
json.dump({k:[rc,t] for k,rc,t in res},open(outdir+'/_rc.json','w'))
print(tag,R,{k:rc for k,rc,t in res})
