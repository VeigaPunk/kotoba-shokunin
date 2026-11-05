import json, os, subprocess
T=os.environ["TMPDIR"]; W=f"{T}/worlds"
base={"corpus.index.tracked_files":"DRIFT","corpus.index.unindexed":"DRIFT","corpus.pointers.report_total":"DRIFT","corpus.pointers.report_dead":"DRIFT","corpus.pointers.commit_total":"DRIFT","corpus.pointers.commit_unresolvable":"DRIFT"}
for w in ["addred_same","addred_new","addred_count","silenced_inplace"]:
    p=subprocess.run(["python3","-B","verifiers/verify_corpus_integrity.py","--json"],cwd=f"{W}/{w}",capture_output=True,text=True)
    d=json.loads(p.stdout); v={r["check"]:r for r in d["results"]}
    red={n for n,r in v.items() if r["verdict"]!="PASS"}
    print(f"\n{w}: rc={p.returncode} names={len(v)} red={sorted(red)} new_vs_base={sorted(red-set(base))} healed={sorted(set(base)-red)}")
    for n in ["corpus.pointers.commit_unresolvable","corpus.pointers.commit_nonhash","corpus.pointers.commit_total","corpus.pointers.report_total"]:
        print(f"   {n}: observed={v[n]['observed']} verdict={v[n]['verdict']}")
