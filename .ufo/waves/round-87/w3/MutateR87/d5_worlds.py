"""Fixture worlds for the D5(iii) form question: exact-set vs 'no red outside the set'."""
import contextlib, importlib.util, io, json, subprocess, sys, tempfile
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r87/MutateR87")
VARIANTS = {"pristine": S/"repo760/verifiers/check_r86_routed_repairs.py",
            "d5iii_subset": S/"mutants/c2_d5iii.py"}

GATE = '''#!/usr/bin/env python3
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
MODE = (ROOT / "GATE").read_text().strip()
CHECKS = ("corpus.index.tracked_files", "corpus.index.unindexed",
          "corpus.index.stale_patterns", "corpus.index.missing_paths",
          "corpus.pointers.report_total", "corpus.pointers.report_dead",
          "corpus.pointers.commit_total", "corpus.pointers.commit_unresolvable",
          "corpus.pointers.commit_nonhash")
DEAD = "corpus/lessons/round-86-verifier-spotcheck.md:33: .ufo/reports/round-84/kama.md"
UNRES = "corpus/lessons/round-81.md:8: 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1"
RED = {
  "honest": {"corpus.pointers.report_dead": DEAD,
             "corpus.pointers.commit_unresolvable": UNRES},
  "healed": {"corpus.pointers.commit_unresolvable": UNRES},
  "no_dead_heal_only": {"corpus.pointers.commit_unresolvable": UNRES},
  "only_dead": {"corpus.pointers.report_dead": DEAD},
  "empty": {},
  "extra": {"corpus.pointers.report_dead": DEAD,
            "corpus.pointers.commit_unresolvable": UNRES,
            "corpus.index.unindexed": "drift"},
  "healed_detail": {"corpus.pointers.commit_unresolvable": UNRES},
}[MODE]
DETAILS = {"healed_detail": {"report_dead_detail": [DEAD],
                             "commit_unresolvable_detail": [UNRES]}}.get(MODE) or {
    "report_dead_detail": [RED["corpus.pointers.report_dead"]]
        if "corpus.pointers.report_dead" in RED else [],
    "commit_unresolvable_detail": [RED["corpus.pointers.commit_unresolvable"]]
        if "corpus.pointers.commit_unresolvable" in RED else []}
RESULTS = [{"check": n, "verdict": "DRIFT" if n in RED else "PASS"} for n in CHECKS]
print(json.dumps({"observed": {"corpus": DETAILS}, "results": RESULTS}, indent=1))
'''

PLAN = """# kotoba round 87\n\n## Kill rule\n\nA counter, its ledger or its pins changed after the first candidate score kills that claim.\n"""
LESSON = """# kotoba round 87\n\n## Gate\n\n| candidate | decision | reason |\n|---|---|---|\n| ReviewerRoots row 3 | reject | the quote is a doc string line, not a code reader, so it cannot ground the plugin root |\n\n## Carried reds\n\nThe gate carries two DRIFTs, at `corpus/lessons/round-86-verifier-spotcheck.md:33` and `corpus/lessons/round-81.md:8`; both are left red and disclosed (Q64).\n"""
SPOT = "# spotcheck\n\n## 6. Routed defects\n\n- carried base red: `.ufo/reports/round-84/kama.md`\n"
L81 = "# lesson 81\n\n## 2. Evidence\n\n| test-world commit | 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1 |\n"

def load(path):
    spec = importlib.util.spec_from_file_location("v_" + path.stem, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def git(repo, *a, ok=True):
    p = subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True)
    if ok and p.returncode:
        raise SystemExit("git %s rc=%d out=%r err=%r" % (" ".join(a[:2]), p.returncode, p.stdout[-300:], p.stderr[-300:]))
    return p.stdout

def commit(repo, msg, files):
    for rel, body in files.items():
        p = Path(repo)/rel; p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body)
    git(repo, "add", "-A")
    git(repo, "-c", "user.name=probe", "-c", "user.email=probe@example.invalid",
        "commit", "-q", "-m", msg)
    return git(repo, "rev-parse", "HEAD").strip()

with tempfile.TemporaryDirectory(prefix="d5form-", dir=str(S)) as td:
    repo = Path(td)/"lane"; repo.mkdir()
    git(repo, "init", "-q", "-b", "master")
    if git(repo, "rev-parse", "--show-toplevel").strip() != str(repo):
        raise SystemExit("fixture toplevel is not the fixture")
    scaffold = commit(repo, "scaffold", {
        "verifiers/check_omp_catalogue_repro.py": "#!/usr/bin/env python3\nprint('i')\n",
        "verifiers/check_gate_registry.py": "#!/usr/bin/env python3\nprint('i')\n",
        "verifiers/verify_corpus_integrity.py": GATE,
        "GATE": "init\n", "plans/round-87.md": PLAN,
        "corpus/lessons/round-87.md": LESSON,
        "corpus/lessons/round-86-verifier-spotcheck.md": SPOT,
        "corpus/lessons/round-81.md": L81,
    })
    base = commit(repo, "receipts", {
        ".ufo/waves/round-86/receipts/tip-catalogue.txt":
            "$ python3 -B verifiers/check_omp_catalogue_repro.py --rev %s\n"
            "omp catalogue lines reproduced 215 of 215\nexit=0\n" % scaffold,
        ".ufo/waves/round-86/receipts/tip-registry.txt":
            "$ python3 -B verifiers/check_gate_registry.py --rev %s\n"
            "gate registry rows conformant 67 of 67\nexit=0\n" % scaffold,
    })
    work = Path(td)/"work"; work.mkdir()
    mods = {k: load(v) for k, v in VARIANTS.items()}
    rows = []
    for mode in ("honest", "healed", "only_dead", "empty", "extra", "healed_detail"):
        rev = commit(repo, "mode " + mode, {"GATE": mode + "\n"})
        for name, m in mods.items():
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                rc = m.main(["--rev", rev, "--repo", str(repo), "--work", str(work)],
                            landing_rev=base, validator_path=m.OMP_VALIDATOR, base_rev=base)
            text = out.getvalue()
            score = next((l for l in text.splitlines()
                          if l.startswith("r86 routed defects closed")), "?")
            d5 = next((l for l in text.splitlines() if " d5 " in l), "?")
            rows.append((mode, name, rc, score, d5[:150], err.getvalue().strip()[:80]))
    for r in rows:
        print("%-9s %-13s rc=%d | %-34s | %s %s" % r)
