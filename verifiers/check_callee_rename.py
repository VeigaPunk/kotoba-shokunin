#!/usr/bin/env python3
r"""check_callee_rename.py -- frozen counter for the round-52 C1 (freshness) claim.

Round 52, claim C1: the omp loader-registration extractor in
`verifiers/verify_surfaces.py` survives a pure callee rename.  Six omp rebuilds
since round 18 renamed the registration callees while the call shape stayed
`<callee>(<v>, <group>, "<FILE>.md")`
(`.ufo/waves/round-51/build/OmpRenameHistory.md`); each rename turned the
freshness gate red until a round re-pinned a callee allowlist by hand.

This counter is frozen at the round-52 plan commit.  Its fixture revision, its
fixture list, its rename rule, its planted line and its expected strings are
pinned here and never read from the revision measured.

For each of the 4 pinned omp fixtures (read from FIXTURE_REV, never from the
revision measured), the gate script taken from `--rev` (or `--root`) is run
three times through its CLI with `--check surfaces.literal_present --check
surfaces.no_uncovered_class`:

  C  control:  the fixture as committed           -> exit 0, both checks PASS
  A  renamed:  every call-site callee that is one of the 19 historical
               registration callees (BASE_CALLEES) is replaced by a fresh
               two-character name (one fresh name per distinct callee, drawn
               from a seeded shuffle, absent from the fixture as an identifier
               and absent from BASE_CALLEES); alias decoys such as
               `q(u, "evil", "EVIL.md")` keep their callee
                                                  -> exit 0, both checks PASS
               (so the decoy must stay unextracted and every declared pair
               must still extract)
  B  renamed + planted: A plus one appended call by the first renamed real
               callee registering an undeclared pair
               `<fresh0>(u, "rnplant", "RNPLANT.md")`
                                                  -> exit 1, FAIL
               surfaces.no_uncovered_class naming `omp:rnplant/RNPLANT.md`
               (so a rule that only keeps declared pairs cannot pass)

A fixture is ROBUST iff C, A and B all hold.  Output:
`callee-rename robust <R> of 4 fixtures`; exit 0 iff R == 4, 1 otherwise,
2 = could not evaluate (git/show failure, missing gate script).

Usage:
  python3 -B verifiers/check_callee_rename.py --rev <rev> [--seed N] [--json]
  python3 -B verifiers/check_callee_rename.py --root <dir> [--seed N] [--json]
  python3 -B verifiers/check_callee_rename.py --self-test [--seed N]

`--seed` changes the fresh names (default 52) so a reader can check that no
implementation hardcodes them.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import random
import re
import string
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
FIXTURE_REV = "c8579a4c5b48789e56fb9060ddd48f33569e1215"
SELF_TEST_REV = "422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4"
FIXTURE_DIR = "verifiers/fixtures/surfaces"
GATE = "verifiers/verify_surfaces.py"
# (omp fixture, baseline, inventory) -- the pairings the gate's own self-test
# uses at FIXTURE_REV (verify_surfaces.py self_test (a), (b2), (b2c), (b2d)).
CASES = (
    ("strings-omp-clean.txt", "baseline-clean.json", "inventory-clean.md"),
    ("strings-omp-newcallees.txt", "baseline-clean.json", "inventory-clean.md"),
    ("strings-omp-18.12.5.txt", "baseline-18.12.5.json", "inventory-clean.md"),
    ("strings-omp-18.12.6.txt", "baseline-18.12.5.json", "inventory-clean.md"),
)
OC_FIXTURE = "strings-opencode-clean.txt"
# Every registration callee any omp generation used (OMP_CALL_RE at FIXTURE_REV).
BASE_CALLEES = ("Id", "Cl", "jDe", "jDf", "Tl", "dr", "GW", "Co", "Dl", "Hj",
                "I5", "Gl", "Mo", "lq", "Xl", "Fo", "Kl", "Ho", "bq")
GENERIC_CALL_RE = re.compile(
    r"(?<![A-Za-z0-9_$])([A-Za-z_$][A-Za-z0-9_$]*)(?=\(\s*[^\s,()]+\s*,\s*"
    r'(?:"[a-z0-9_-]+"|[A-Za-z_$][A-Za-z0-9_$]*)\s*,\s*'
    r'"[A-Za-z0-9_./-]+\.md"(?=\s*[,)]))'
)
PLANT_PAIR = ("rnplant", "RNPLANT.md")
PLANT_ID = "omp:rnplant/RNPLANT.md"
CHECKS = ("surfaces.literal_present", "surfaces.no_uncovered_class")


def git_show(rev: str, path: str) -> bytes:
    r = subprocess.run(["git", "-C", str(LANE), "show", "%s:%s" % (rev, path)],
                       capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("git show %s:%s failed: %s"
                           % (rev, path, r.stderr.decode(errors="replace").strip()))
    return r.stdout


def fresh_names(text: str, count: int, seed: int) -> list[str]:
    pool = [a + b for a in string.ascii_uppercase
            for b in string.ascii_lowercase + string.digits]
    random.Random(seed).shuffle(pool)
    out = []
    for name in pool:
        if name in BASE_CALLEES:
            continue
        if re.search(r"(?<![A-Za-z0-9_$])%s(?![A-Za-z0-9_$])" % re.escape(name), text):
            continue
        out.append(name)
        if len(out) == count:
            return out
    raise RuntimeError("fresh-name pool exhausted")


def rename(text: str, seed: int) -> tuple[str, dict[str, str]]:
    sites = [m for m in GENERIC_CALL_RE.finditer(text) if m.group(1) in BASE_CALLEES]
    callees = []
    for m in sites:
        if m.group(1) not in callees:
            callees.append(m.group(1))
    mapping = dict(zip(callees, fresh_names(text, len(callees), seed)))
    out, last = [], 0
    for m in sites:
        out.append(text[last:m.start(1)])
        out.append(mapping[m.group(1)])
        last = m.end(1)
    out.append(text[last:])
    return "".join(out), mapping


def run_gate(gate: Path, fx: Path, omp: Path, base: str, inv: str) -> tuple[int, str]:
    argv = [sys.executable, "-B", str(gate), "--repo", str(fx),
            "--omp-strings", str(omp), "--opencode-strings", str(fx / OC_FIXTURE),
            "--baseline", str(fx / base), "--inventory", str(fx / inv)]
    for c in CHECKS:
        argv += ["--check", c]
    r = subprocess.run(argv, capture_output=True, text=True, timeout=300)
    return r.returncode, r.stdout + r.stderr


def both_pass(code: int, out: str) -> bool:
    return code == 0 and all(("PASS %s:" % c) in out for c in CHECKS)


def self_test(seed: int) -> int:
    assertions = 0
    failures = 0

    def check(name: str, ok: bool, evidence: str) -> None:
        nonlocal assertions, failures
        assertions += 1
        if not ok:
            failures += 1
        print("%s self-test %s: %s" % (
            "PASS" if ok else "FAIL", name, evidence))

    def run_case(root: Path) -> tuple[int, dict, str]:
        out = io.StringIO()
        err = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(["--root", str(root), "--seed", str(seed), "--json"])
        text = out.getvalue()
        payload, separator, summary = text.rpartition("\ncallee-rename robust ")
        if not separator:
            raise RuntimeError("self-test run omitted the counter summary")
        return code, json.loads(payload), "callee-rename robust " + summary.strip()

    try:
        source = git_show(SELF_TEST_REV, GATE).decode("utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "robust"
            gate = root / GATE
            gate.parent.mkdir(parents=True)
            gate.write_text(source, encoding="utf-8")
            code, report, summary = run_case(root)
            row = next(r for r in report["rows"] if r["fixture"] == CASES[0][0])
            detail = "\n".join(row["detail"]["planted"])
            robust_ok = (
                code == 0 and summary == "callee-rename robust 4 of 4 fixtures"
                and report["robust"] == len(CASES) and row["robust"] is True
                and "FAIL surfaces.no_uncovered_class:" in detail
                and PLANT_ID in detail)
            check("robust case", robust_ok,
                  "%s exit=%d finding=%s" % (row["fixture"], code, PLANT_ID))

            anchor = '\nif __name__ == "__main__":\n'
            if source.count(anchor) != 1:
                raise RuntimeError("self-test gate mutation anchor changed")
            mutant = source.replace(
                anchor,
                '\ndef check_no_uncovered_class(entries, extracted, dumps=None):\n'
                '    return True, "self-test injected suppression"\n' + anchor,
                1)
            mutant_root = Path(tmp) / "non-robust"
            mutant_gate = mutant_root / GATE
            mutant_gate.parent.mkdir(parents=True)
            mutant_gate.write_text(mutant, encoding="utf-8")
            code, report, summary = run_case(mutant_root)
            row = next(r for r in report["rows"] if r["fixture"] == CASES[0][0])
            detail = "\n".join(row["detail"]["planted"])
            nonrobust_ok = (
                code == 1 and summary == "callee-rename robust 0 of 4 fixtures"
                and report["robust"] == 0 and row["robust"] is False
                and row["control"] == [0, True]
                and row["renamed_run"] == [0, True]
                and row["planted_run"] == [0, False]
                and "PASS surfaces.no_uncovered_class: self-test injected suppression"
                in detail and PLANT_ID not in detail)
            check("non-robust case", nonrobust_ok,
                  "%s exit=%d finding=self-test injected suppression" % (
                      row["fixture"], code))
    except (RuntimeError, subprocess.TimeoutExpired, OSError, ValueError,
            KeyError, StopIteration) as e:
        print("self-test could-not-evaluate: %s" % e, file=sys.stderr)
        return 2

    print("self-test: %d failure(s) over %d assertions" % (
        failures, assertions))
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--rev", help="lane revision whose gate script is measured")
    src.add_argument("--root", help="directory holding verifiers/verify_surfaces.py")
    src.add_argument("--self-test", action="store_true")
    ap.add_argument("--seed", type=int, default=52)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        if args.json:
            ap.error("--self-test cannot be combined with --json")
        return self_test(args.seed)
    rows = []
    try:
        with tempfile.TemporaryDirectory() as tmp:
            t = Path(tmp)
            fx = t / "fixtures"
            fx.mkdir()
            names = {c[0] for c in CASES} | {c[1] for c in CASES} | {c[2] for c in CASES}
            names.add(OC_FIXTURE)
            for n in sorted(names):
                (fx / n).write_bytes(git_show(FIXTURE_REV, "%s/%s" % (FIXTURE_DIR, n)))
            gate = t / "verify_surfaces.py"
            if args.rev:
                gate.write_bytes(git_show(args.rev, GATE))
            else:
                p = Path(args.root) / GATE
                if not p.is_file():
                    raise RuntimeError("missing %s" % p)
                gate.write_bytes(p.read_bytes())
            for omp, base, inv in CASES:
                text = (fx / omp).read_text(encoding="utf-8")
                renamed, mapping = rename(text, args.seed)
                fresh0 = next(iter(mapping.values()))
                planted = renamed.rstrip("\n") + '\nvar rnplant = %s(u, "%s", "%s");\n' % (
                    fresh0, PLANT_PAIR[0], PLANT_PAIR[1])
                pa, pb = t / ("A-" + omp), t / ("B-" + omp)
                pa.write_text(renamed, encoding="utf-8")
                pb.write_text(planted, encoding="utf-8")
                cc, co = run_gate(gate, fx, fx / omp, base, inv)
                ac, ao = run_gate(gate, fx, pa, base, inv)
                bc, bo = run_gate(gate, fx, pb, base, inv)
                ok_c = both_pass(cc, co)
                ok_a = both_pass(ac, ao)
                ok_b = (bc == 1 and "FAIL surfaces.no_uncovered_class:" in bo
                        and PLANT_ID in bo)
                rows.append({"fixture": omp, "renamed": mapping,
                             "control": [cc, ok_c], "renamed_run": [ac, ok_a],
                             "planted_run": [bc, ok_b],
                             "robust": ok_c and ok_a and ok_b,
                             "detail": {"control": co.strip().splitlines()[-3:],
                                        "renamed": ao.strip().splitlines()[-3:],
                                        "planted": bo.strip().splitlines()[-3:]}})
    except (RuntimeError, subprocess.TimeoutExpired, OSError) as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    robust = sum(1 for r in rows if r["robust"])
    if args.json:
        print(json.dumps({"robust": robust, "of": len(CASES), "seed": args.seed,
                          "rows": rows}, indent=1))
    else:
        for r in rows:
            print("%-28s control=%s renamed=%s planted=%s robust=%s map=%s" % (
                r["fixture"], r["control"], r["renamed_run"], r["planted_run"],
                r["robust"], r["renamed"]))
    print("callee-rename robust %d of %d fixtures" % (robust, len(CASES)))
    return 0 if robust == len(CASES) else 1


if __name__ == "__main__":
    sys.exit(main())
