#!/usr/bin/env python3
"""MutTesterBattery harness: mutate the candidate check_mutation_battery.py, one mutant at a time.

Scratch-only driver. Every mutant starts from the committed candidate bytes (git checkout of the
single file in the scratch clone), gets one exact-count string edit, is run through --self-test
and (where cheap) through the public predicate, then is restored.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r91/MutTesterBattery")
D = S / "repo"
WAVE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-91/w1/MutTesterBattery")
F = "verifiers/check_mutation_battery.py"
MAN = "verifiers/fixtures/mutation-battery/manifest.tsv"
ENV = dict(os.environ, TMPDIR=str(S), PYTHONDONTWRITEBYTECODE="1")
ENV.pop("GIT_DIR", None)
ENV.pop("GIT_INDEX_FILE", None)

MUTANTS = [
    ("m1", "disable G1 commit check (rev-parse --verify result ignored)",
     'if rc != 0 or out.decode().strip() != rev:\n        raise CouldNotEvaluate("G1: %s is not a commit',
     'if False:\n        raise CouldNotEvaluate("G1: %s is not a commit'),
    ("m2", "disable G1 clean-tree guard on the scratch clone",
     'if rc != 0 or out.strip():\n        raise CouldNotEvaluate("G1: scratch clone is not clean',
     'if False:\n        raise CouldNotEvaluate("G1: scratch clone is not clean'),
    ("m3", "remove restore read-back: restore written with bare write_target",
     '        place(dest / row.target, data[row.target], rec_sha[row.target], "restore " + row.target)',
     '        write_target(dest / row.target, data[row.target])'),
    ("m4", "remove third PROBES entry (battery self-test probe)",
     '    BAT: (("bat-self-test", ["--self-test"], 0),),\n', ''),
    ("m5", "break equivalent comment-insert generator (emits a bare '(' line)",
     '            out.append(COMMENT_MARK)', '            out.append("(")'),
    ("m7", "invert new arm: G1 commit-check arm expects rc != 2",
     't.check("G1 commit check: a full-hex --rev that is not a commit exits 2", rc == 2, out)',
     't.check("G1 commit check: a full-hex --rev that is not a commit exits 2", rc != 2, out)'),
]


def sh(cmd, cwd, timeout=900):
    p = subprocess.run(cmd, cwd=str(cwd), env=ENV, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout + p.stderr


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], env=ENV, capture_output=True, text=True)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def restore():
    r = git(D, "checkout", "--", F)
    assert r.returncode == 0, r.stderr
    st = git(D, "status", "--porcelain").stdout
    assert st.strip() == "", "scratch not clean after restore: %r" % st
    head_sha = hashlib.sha256(git(D, "show", "HEAD:" + F).stdout.encode()).hexdigest()
    assert sha(D / F) == head_sha, "candidate bytes not restored"


def first_fail(out):
    for ln in out.splitlines():
        if ln.startswith("FAIL "):
            return ln[:200]
    tb = [ln for ln in out.splitlines() if ln.strip()]
    return ("traceback: " + tb[-1][:200]) if tb and "Traceback" in out else ""


def tally(out):
    m = re.findall(r"^(\d+) failure\(s\) over (\d+) assertions", out, re.M)
    return m[-1] if m else None


def predicate(repo, rev, work):
    rc, out = sh([sys.executable, "-B", F, "--rev", rev, "--work", str(work)], repo, timeout=1200)
    line = [ln for ln in out.splitlines() if ln.startswith("mutation battery killed")]
    return rc, out, (line[-1] if line else "")


def main():
    WAVE.mkdir(parents=True, exist_ok=True)
    rev = git(D, "rev-parse", "HEAD").stdout.strip()
    assert git(D, "rev-parse", "--show-toplevel").stdout.strip() == str(D.resolve()) or True
    top = git(D, "rev-parse", "--show-toplevel").stdout.strip()
    assert Path(top).resolve() == D.resolve(), top
    results = []
    base_src = (D / F).read_text(encoding="utf-8")
    restore()
    # clean candidate self-test as the control row
    rc0, out0 = sh([sys.executable, "-B", F, "--self-test"], D)
    (WAVE / "selftest-clean.txt").write_text(out0)
    results.append({"id": "clean", "mutation": "none (candidate control)", "selftest_rc": rc0,
                    "tally": tally(out0), "first_failing_arm": first_fail(out0),
                    "predicate_rc": None, "predicate_line": None, "verdict": "control"})
    for mid, desc, old, new in MUTANTS:
        restore()
        src = (D / F).read_text(encoding="utf-8")
        n = src.count(old)
        assert n == 1, "%s anchor count %d" % (mid, n)
        (D / F).write_text(src.replace(old, new), encoding="utf-8")
        assert git(D, "diff", "--stat").stdout.strip(), mid
        compile_ok = sh([sys.executable, "-c",
                         "import ast,sys;ast.parse(open(sys.argv[1]).read())", F], D)[0] == 0
        rc, out = sh([sys.executable, "-B", F, "--self-test"], D)
        (WAVE / ("selftest-%s.txt" % mid)).write_text(out)
        prc, pout, pline = predicate(D, rev, S / ("work-%s" % mid))
        (WAVE / ("predicate-%s.txt" % mid)).write_text(pout)
        results.append({"id": mid, "mutation": desc, "compiles": compile_ok,
                        "selftest_rc": rc, "tally": tally(out), "first_failing_arm": first_fail(out),
                        "predicate_rc": prc, "predicate_line": pline})
        restore()
    # m6: drop manifest row mb-m15 on a separate scratch clone (committed, so G1 reads it)
    D6 = S / "repo-m6"
    if D6.exists():
        import shutil
        shutil.rmtree(D6)
    sh(["git", "clone", "-q", "--shared", str(D), str(D6)], S)
    sh(["git", "-C", str(D6), "checkout", "-q", rev], S)
    man = D6 / MAN
    lines = man.read_text(encoding="utf-8").splitlines(keepends=True)
    kept = [ln for ln in lines if not ln.startswith("mb-m15-")]
    assert len(kept) == len(lines) - 1
    man.write_text("".join(kept), encoding="utf-8")
    git(D6, "add", "-A")
    git(D6, "-c", "user.name=scratch", "-c", "user.email=scratch@invalid", "commit", "-q", "-m", "m6")
    rev6 = git(D6, "rev-parse", "HEAD").stdout.strip()
    prc, pout, pline = predicate(D6, rev6, S / "work-m6")
    (WAVE / "predicate-m6.txt").write_text(pout)
    rc6, out6 = sh([sys.executable, "-B", F, "--self-test"], D6)
    results.append({"id": "m6", "mutation": "drop manifest row mb-m15-clean-tree-guard-off (rev %s)" % rev6[:12],
                    "compiles": True, "selftest_rc": rc6, "tally": tally(out6),
                    "first_failing_arm": first_fail(out6), "predicate_rc": prc,
                    "predicate_line": pline})
    (WAVE / "m6-selftest.txt").write_text(out6)
    # the row count, read from the m6 rev bytes
    rows_m6 = sum(1 for ln in git(D6, "show", "HEAD:" + MAN).stdout.splitlines()
                  if re.search(r"\tkill\t", ln))
    results[-1]["kill_rows_at_rev"] = rows_m6
    (WAVE / "summary.raw.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=1))


if __name__ == "__main__":
    main()
