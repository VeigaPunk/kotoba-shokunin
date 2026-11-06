import importlib.util, sys
from pathlib import Path
repo = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("vsc", repo/"verifiers/verify_skill_checklist.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
subjects=[]; log_lines=[]
for name in m.GOVERNANCE_FILES:
    lines=(repo/name).read_text(encoding="utf-8").splitlines()
    if name=="LOG.md": log_lines=lines
    found,skipped=m.citation_subjects(lines, source=name, exclude_quoted=True, exclude_schematic=True)
    subjects.extend(found)
problems,excused=m.errata_problems(m.GOVERNANCE_ERRATA, m.GOVERNANCE_ERRATA_HORIZON, log_lines, subjects, repo)
subjects=[s for s in subjects if s["source"]!="LOG.md" or (s["line"],s["token"]) not in excused]
cproblems,cexcused=m.correction_problems(m.GOVERNANCE_CORRECTIONS, m.GOVERNANCE_CORRECTIONS_HORIZON, log_lines, subjects, repo)
subjects=[s for s in subjects if (s["source"],s["line"],s["token"]) not in cexcused]
dead=[s for s in subjects if not m.citation_resolve(s["token"], repo)]
print("ERRATA_PROBLEMS", len(problems)); [print("  E", p) for p in problems]
print("CORRECTION_PROBLEMS", len(cproblems)); [print("  C", p) for p in cproblems]
print("DEAD_SUBJECTS", len(dead))
for s in dead: print("  D", s["source"], s["line"], repr(s["token"]))
