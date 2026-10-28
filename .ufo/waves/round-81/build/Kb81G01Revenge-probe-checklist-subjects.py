"""Kb81G01Revenge — is the round-16 fleet token in the checklist's evaluated subject set?"""
import importlib.util, pathlib
spec = importlib.util.spec_from_file_location(
    "vsc", "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_skill_checklist.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
lines = pathlib.Path("SCORECARD.md").read_text().splitlines()
subjects, _ = m.citation_subjects(lines)
tok = "../.ufo/reports/round-16/kotoba.md"
hits = [s for s in subjects if s["token"] == tok]
print("citation_subjects(SCORECARD.md) count:", len(subjects))
print("round-16 token evaluated:", bool(hits), hits[:2])
print("token resolves against the LANE (real fleet parent):",
      m.citation_resolve(tok, pathlib.Path(".").resolve()))
