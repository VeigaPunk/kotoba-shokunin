import importlib.util, sys, pathlib
spec = importlib.util.spec_from_file_location("vci", "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_corpus_integrity.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
text = pathlib.Path("corpus/lessons/round-76-verifier-spotcheck.md").read_text()
# pointer_exists that denies everything: any counted pointer shows up as dead
found = m.citation_findings("corpus/lessons/round-76-verifier-spotcheck.md", text,
                            lambda base, tok: False, lambda h: True)
print("report_total", found["report_total"])
print("report_dead", found["report_dead"])
print("detail", found["report_dead_detail"])
text80 = pathlib.Path("corpus/lessons/round-80.md").read_text()
f80 = m.citation_findings("corpus/lessons/round-80.md", text80, lambda base, tok: False, lambda h: True)
print("r80lesson report_total", f80["report_total"], "report_dead", f80["report_dead"])
text77 = pathlib.Path("corpus/lessons/round-77-verifier-spotcheck.md").read_text()
f77 = m.citation_findings("corpus/lessons/round-77-verifier-spotcheck.md", text77, lambda base, tok: False, lambda h: True)
print("r77lesson report_total", f77["report_total"], "dead detail", f77["report_dead_detail"])
