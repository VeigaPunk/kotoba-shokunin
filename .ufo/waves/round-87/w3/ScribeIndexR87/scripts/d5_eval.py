import json, sys
doc = json.load(open(sys.argv[1]))
res = doc.get("results") or []
corpus = (doc.get("observed") or {}).get("corpus") or {}
red = sorted(r.get("check") for r in res if r.get("verdict") != "PASS")
want = ["corpus.pointers.commit_unresolvable", "corpus.pointers.report_dead"]
passed = sum(1 for r in res if r.get("verdict") == "PASS")
print("tally", f"{passed}/{len(res)}", "| red", red)
print("report_dead_detail", corpus.get("report_dead_detail"))
print("commit_unresolvable_detail", corpus.get("commit_unresolvable_detail"))
dead_site = any(l.startswith("corpus/lessons/round-86-verifier-spotcheck.md:33") for l in corpus.get("report_dead_detail") or [])
unres_site = any(l.startswith("corpus/lessons/round-81.md:8") for l in corpus.get("commit_unresolvable_detail") or [])
print("D5(iii) independent eval:", "PASS" if red == want and dead_site and unres_site and passed == 7 else "FAIL",
      "| exact-set", red == want, "| dead-site", dead_site, "| unres-site", unres_site, "| tally==7/9", passed == 7 and len(res) == 9)
