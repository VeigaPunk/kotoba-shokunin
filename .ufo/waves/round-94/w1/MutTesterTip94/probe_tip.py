#!/usr/bin/env python3
"""probe_tip (MutTesterTip94, round 94 w1).

The frozen counter's bounded behavioural detector, applied to NEW (non-frozen)
mutants of the C2 key-coverage block of verifiers/check_tip_battery.py.
Mechanics mirror verifiers/fixtures/round-94/selftest-kills.py exactly: clone
REV from REPO (--shared), run `python3 -B <instrument> --self-test` honest and
once per mutant; each mutant is a literal substitution of the instrument bytes
at REV made in the probe's own clone working tree (never committed); the anchor
must match exactly the declared number of times and the mutated bytes must
compile, else could-not-evaluate; a mutant is KILLED iff its self-test exits
non-zero within 600 s (a timeout is could-not-evaluate). Per target mutant a
DECOY (unmodified instrument with the replacement appended as `# r94-decoy`
comments) must exit 0. The frozen counter and its tables are not modified.

Usage: python3 -B probe_tip.py <rev> <repo>
"""
from __future__ import annotations

import hashlib
import os
import py_compile
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TIMEOUT_S = 600
INSTRUMENT = "verifiers/check_tip_battery.py"

A2 = "        for path in scripts:\n            if path not in INSTRUMENT_PINS:"
A3 = (A2 + '\n                failures.append(("instrument-pin", '
      '"%s has no INSTRUMENT_PINS key (battery instrument unpinned)" % path))')

MUTANTS = [
    ("n1-skip-middle-key", A2, 1,
     "        for path in scripts[:3] + scripts[4:]:\n            if path not in INSTRUMENT_PINS:"),
    ("n2-threshold-gate", A2, 1,
     "        for path in (scripts if len(INSTRUMENT_PINS) >= 7 else []):\n            if path not in INSTRUMENT_PINS:"),
    ("n3-fail-other-guard", A3, 1,
     A3.replace('failures.append(("instrument-pin", "%s has no INSTRUMENT_PINS key',
                'failures.append(("instrument-size", "%s has no INSTRUMENT_PINS key')),
    ("n4-pins-keys-not-battery", A2, 1,
     "        for path in INSTRUMENT_PINS:\n            if path not in INSTRUMENT_PINS:"),
    ("n5-normalised-compare", A2, 1,
     "        for path in scripts:\n            if os.path.normpath(path) not in INSTRUMENT_PINS:"),
]


class NotEvaluated(Exception):
    pass


def run_selftest(clone: Path, env: dict) -> tuple[int, str]:
    try:
        proc = subprocess.run([sys.executable, "-B", INSTRUMENT, "--self-test"], cwd=clone, env=env,
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=TIMEOUT_S)
    except subprocess.TimeoutExpired:
        raise NotEvaluated("self-test timeout after %ds" % TIMEOUT_S)
    return proc.returncode, proc.stdout.decode("utf-8", "replace")


def last_line(text: str) -> str:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    return lines[-1] if lines else "<no output>"


def main(argv: list[str]) -> int:
    rev, repo = argv[0], argv[1]
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r94" / "probe-tip"
    root.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="probe.", dir=root))
    try:
        env = dict(os.environ, TMPDIR=str(work / "tmp"), PYTHONDONTWRITEBYTECODE="1")
        (work / "tmp").mkdir()
        clone = work / "world" / "kotoba-shokunin"
        clone.parent.mkdir()
        for cmd in (["git", "clone", "-q", "--shared", repo, str(clone)],
                    ["git", "-C", str(clone), "checkout", "-q", rev]):
            if subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
                raise NotEvaluated("clone or checkout failed")
        print("probe-tip rev %s repo %s instrument %s" % (rev, repo, INSTRUMENT))
        path = clone / INSTRUMENT
        if not path.is_file():
            raise NotEvaluated("instrument %s absent at %s" % (INSTRUMENT, rev))
        original = path.read_text(encoding="utf-8")
        rev_blob = subprocess.run(["git", "-C", clone, "rev-parse", "%s:%s" % (rev, INSTRUMENT)],
                                  stdout=subprocess.PIPE, check=True).stdout.decode().strip()
        sha_before = hashlib.sha256(original.encode("utf-8")).hexdigest()
        print("instrument sha256 before %s (blob %s)" % (sha_before, rev_blob[:12]))

        rc_h, out_h = run_selftest(clone, env)
        honest_ok = rc_h == 0 and "0 failure(s)" in out_h
        print("honest rc %d ok %s: %s" % (rc_h, honest_ok, last_line(out_h)))

        def mutate(name: str, anchor: str, count: int, repl: str) -> str:
            found = original.count(anchor)
            if found != count:
                return "CNE anchor miss: %s matches %d time(s), expected %d" % (name, found, count)
            path.write_text(original.replace(anchor, repl), encoding="utf-8")
            try:
                py_compile.compile(str(path), cfile=str(work / "tmp" / "c.pyc"), doraise=True)
            except py_compile.PyCompileError as exc:
                path.write_text(original, encoding="utf-8")
                return "CNE mutant %s does not compile: %s" % (name, exc.msg.splitlines()[-1])
            try:
                rc, out = run_selftest(clone, env)
            finally:
                path.write_text(original, encoding="utf-8")
            killed = rc != 0
            print("mutant %s rc %d %s: %s" % (name, rc, "KILLED" if killed else "SURVIVED", last_line(out)))
            return "killed" if killed else "survived"

        verdicts = {}
        for name, a, c, w in MUTANTS:
            try:
                verdicts[name] = mutate(name, a, c, w)
            except NotEvaluated as exc:
                verdicts[name] = "CNE"
                print("mutant %s CNE: %s" % (name, exc))

        for name, _a, _c, w in MUTANTS:
            decoy = original.rstrip("\n") + "\n" + "".join("# r94-decoy " + ln + "\n" for ln in w.splitlines())
            path.write_text(decoy, encoding="utf-8")
            try:
                rc_d, out_d = run_selftest(clone, env)
            except NotEvaluated as exc:
                print("decoy %s CNE: %s" % (name, exc))
                continue
            finally:
                path.write_text(original, encoding="utf-8")
            print("decoy %s rc %d %s: %s" % (name, rc_d, "HELD" if rc_d == 0 else "KILLED (sniffing)", last_line(out_d)))

        sha_after = hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
        restored = sha_after == sha_before
        print("instrument sha256 after %s restored %s" % (sha_after, restored))
        for name, v in verdicts.items():
            print("verdict %s %s" % (name, v))
        return 0
    except NotEvaluated as exc:
        print("probe-tip-NOT-EVALUATED: %s" % exc)
        return 2
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
