#!/usr/bin/env python3
"""MutTesterV2: C2 mutants of verifiers/check_r86_routed_repairs_v2.py (scratch only).

Each mutant is a copy of the frozen-candidate v2 file with one change, placed in a
scratch verifiers/ dir next to a copy of the byte-frozen r87 counter it imports.
A signature is observed per copy: self-test output, controls C-a..C-d (check_d5 on
the four committed worlds, built with the copy's own fixture helpers), driver exits
(main with D1-D4 stubbed True, D5 real) on the silenced / tip worlds, and the real
CLI at the frozen tip. A mutant is KILLED iff its signature differs from the
unmutated baseline's signature; the differing items name the catching arm/control.
"""
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
SRC_V2 = LANE / "verifiers" / "check_r86_routed_repairs_v2.py"
SRC_R87 = LANE / "verifiers" / "check_r86_routed_repairs.py"
TIP = "4df1e8005016c75390a5e06b209462df58c95918"
SCR = Path(os.environ["TMPDIR"])

MUTANTS = {
    "n1_drop_identity": [(
        "def identity_holds(names_rev: list[str], names_base: list[str]) -> bool:\n"
        "    \"\"\"(i): the same set of names at both revisions, nine names at the base.\"\"\"\n"
        "    return set(names_rev) == set(names_base) and len(set(names_base)) == NAME_COUNT",
        "def identity_holds(names_rev: list[str], names_base: list[str]) -> bool:\n"
        "    \"\"\"(i): the same set of names at both revisions, nine names at the base.\"\"\"\n"
        "    return True  # n1: arm (i) dropped")],
    "n2_drop_monotone": [(
        "    return set(drift_rev) <= set(drift_base)",
        "    return True  # n2: arm (ii) dropped")],
    "n3_subset_to_superset": [(
        "    return set(drift_rev) <= set(drift_base)",
        "    return set(drift_base) <= set(drift_rev)  # n3")],
    "n4_exit0_on_d5_fail": [(
        "    return 0 if score == TARGET else 1",
        "    d5_ok = [ok for cid, ok, _d in rows if cid == \"d5\"][0]\n"
        "    return 0 if (score == TARGET or not d5_ok) else 1  # n4")],
    "n5_hardcode_d5_pass": [(
        "    return ident and mono, detail",
        "    return True, detail  # n5: D5 hardcoded PASS")],
    "n6_integrity_from_worktree": [(
        "    script = tree / INTEGRITY",
        "    script = Path(\"/home/vgpnk/Projects/shokunin/kotoba-shokunin\") / INTEGRITY  # n6"),
        ("[sys.executable, \"-B\", INTEGRITY, \"--json\"]",
         "[sys.executable, \"-B\", str(script), \"--json\"]")],
}

CONTROL_PROBE = r'''
import contextlib, importlib.util, io, json, sys, tempfile
from pathlib import Path
mod_path, work_dir = sys.argv[1], Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("v2under", mod_path)
v2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v2)
root = Path(tempfile.mkdtemp(prefix="ctl-", dir=str(work_dir)))
repo = root / "lane"; repo.mkdir()
v2._git_fixture(repo, "init", "-q")
base = v2._fixture_world(repo, "base world", "base")
tip = v2._fixture_world(repo, "tip world", "base")
healed = v2._fixture_world(repo, "healed world", "healed")
added = v2._fixture_world(repo, "added red world", "added", {
    "corpus/lessons/new-line.md": "commit `0123456789abcdef0123456789abcdef01234567`\n"})
silenced = v2._fixture_world(repo, "silenced world", "silenced")
out = {}
work = root / "work"; work.mkdir()
for label, rev, want in (("C-a_added_red", added, False), ("C-b_silenced", silenced, False),
                         ("C-c_healed", healed, True), ("C-d_tip", tip, True)):
    try:
        ok, detail = v2.check_d5(repo, rev, work, "", Path("/nonexistent"), base)
        out[label] = {"d5_ok": bool(ok), "want": want}
    except Exception as exc:  # could-not-evaluate or crash counts as a distinct signature
        out[label] = {"exception": type(exc).__name__, "msg": str(exc)[:160]}
# driver: main with D1-D4 stubbed True and the real D5, on silenced and tip worlds
for label, rev in (("drv_silenced", silenced), ("drv_tip", tip)):
    v2.BASE_REV = base
    v2.ITEMS = (("d1", lambda *a: (True, "")), ("d2", lambda *a: (True, "")),
                ("d3", lambda *a: (True, "")), ("d4", lambda *a: (True, "")),
                ("d5", v2.check_d5))
    import contextlib
    buf = io.StringIO()
    errbuf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(errbuf):
        try:
            code = v2.main(["--rev", rev, "--repo", str(repo), "--work", str(work)])
        except Exception as exc:
            code = "exc:" + type(exc).__name__
    out[label] = {"exit": code, "tail": buf.getvalue().strip().splitlines()[-1:], "err": errbuf.getvalue().strip()[-200:]}
print(json.dumps(out, sort_keys=True))
'''


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def run(cmd, env, cwd=None, timeout=900):
    p = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=cwd, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def build(name, replacements, root: Path) -> Path:
    vdir = root / name / "verifiers"
    vdir.mkdir(parents=True, exist_ok=True)
    shutil.copy(SRC_R87, vdir / SRC_R87.name)
    text = SRC_V2.read_text(encoding="utf-8")
    for old, new in replacements or []:
        n = text.count(old)
        if n != 1:
            raise SystemExit("replacement not unique (%d) for %s: %r" % (n, name, old[:60]))
        text = text.replace(old, new)
    target = vdir / SRC_V2.name
    target.write_text(text, encoding="utf-8")
    return target


def signature(name, target: Path, env, probe_dir: Path) -> dict:
    sig = {}
    code, out, err = run([sys.executable, "-B", str(target), "--self-test"], env)
    lines = out.strip().splitlines()
    sig["selftest_exit"] = code
    sig["selftest_summary"] = lines[0] if lines else ""
    sig["selftest_fails"] = sorted(l for l in lines[1:] if l.startswith("FAIL "))
    code, out, err = run([sys.executable, "-B", str(probe_dir / "ctl.py"), str(target),
                          str(probe_dir)], env)
    sig["controls"] = out.strip() if code == 0 else "probe-exit %d: %s" % (code, err[-200:])
    code, out, err = run([sys.executable, "-B", str(target), "--rev", TIP,
                          "--repo", str(LANE)], env, timeout=1500)
    sig["cli_tip_exit"] = code
    sig["cli_tip_last"] = out.strip().splitlines()[-1:] if out.strip() else [err.strip()[-160:]]
    return sig


def main() -> int:
    only = sys.argv[1:]
    root = SCR / "c2"
    root.mkdir(parents=True, exist_ok=True)
    probe = root / "probe"
    probe.mkdir(exist_ok=True)
    (probe / "ctl.py").write_text(CONTROL_PROBE, encoding="utf-8")
    env = dict(os.environ, TMPDIR=str(SCR))
    rows = []
    variants = [("baseline_unmutated", None)] + list(MUTANTS.items())
    base_sig = None
    for name, reps in variants:
        if only and name not in only and name != "baseline_unmutated":
            continue
        target = build(name, reps, root)
        sig = signature(name, target, env, probe)
        digest = sha(target)
        if name == "baseline_unmutated":
            base_sig = sig
            verdict, arms = "BASELINE", ""
        else:
            diff = [k for k in sig if sig[k] != base_sig[k]]
            verdict = "KILLED" if diff else "SURVIVED"
            arms = ",".join(diff)
        rows.append({"mutant": name, "sha256": digest, "verdict": verdict, "differs": arms,
                     "sig": sig})
        print(json.dumps({"mutant": name, "verdict": verdict, "differs": arms,
                          "selftest": sig["selftest_summary"], "fails": sig["selftest_fails"],
                          "controls": sig["controls"], "cli_tip_exit": sig["cli_tip_exit"],
                          "cli_tip_last": sig["cli_tip_last"]}, sort_keys=True), flush=True)
    (SCR / "c2-rows.json").write_text(json.dumps(rows, indent=1, sort_keys=True), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
