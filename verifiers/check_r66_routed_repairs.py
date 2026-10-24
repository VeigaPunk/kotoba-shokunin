#!/usr/bin/env python3
"""Round-66 C2 counter for the round-65 closure-routed defects.

Frozen predicate: `python3 -B verifiers/check_r66_routed_repairs.py --rev <rev>`
prints `r66 routed defects closed 2 of 2` and exits 0 at the landing revision;
the pinned round-65 base prints `0 of 2` and exits 1. The counter refuses to
certify unless that base scores exactly 0 of 2.

D1 is the two generated round-65 swarm registries committed as nonempty JSON
blobs. D2 is the corpus-integrity repair: all four closure-owned spot-check
lessons indexed; the observed corpus counts re-recorded in the baseline; and
commit citations resolved lane-first with a fleet-root fallback while
code-span meta-findings remain excluded. Every check reads committed blobs at
--rev, never the worktree.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
BASE_REV_LITERAL = "11385e04e368c1e94ab1a5a89d7439033eb1f855"
BASE_REV = BASE_REV_LITERAL
REGISTRIES = (
    ".ufo/waves/round-65/w1/swarm-registry.json",
    ".ufo/waves/round-65/w2/swarm-registry.json",
)
SPOTCHECKS = tuple(
    "lessons/round-%d-verifier-spotcheck.md" % n for n in (62, 63, 64, 65)
)
README = "corpus/README.md"
BASELINE = "verifiers/corpus-baseline.json"
INTEGRITY = "verifiers/verify_corpus_integrity.py"
HOP_MARKER = 'COMMIT_HOP_MARKER = "resolves against the lane repository first, then the fleet root"'
EXPECTED_COUNTS = {
    "corpus.index.tracked_files": 118,
    "corpus.index.unindexed": 0,
    "corpus.pointers.report_total": 79,
    "corpus.pointers.report_dead": 0,
    "corpus.pointers.commit_total": 37,
    "corpus.pointers.commit_unresolvable": 0,
    "corpus.pointers.commit_nonhash": 0,
}
EXPECTED_NOTE = "round66_rerecord"


def git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                          text=True, check=False, timeout=20)


def show(root: Path, rev: str, path: str) -> str | None:
    result = git(root, "show", "%s:%s" % (rev, path))
    return result.stdout if result.returncode == 0 else None


def tracked_nonempty_json(root: Path, rev: str, path: str) -> bool:
    blob = show(root, rev, path)
    if blob is None or not blob.strip():
        return False
    try:
        value = json.loads(blob)
    except (json.JSONDecodeError, TypeError):
        return False
    return isinstance(value, dict) and bool(value)


def check_d1(root: Path, rev: str) -> bool:
    return all(tracked_nonempty_json(root, rev, path) for path in REGISTRIES)


def check_d2(root: Path, rev: str) -> bool:
    readme = show(root, rev, README)
    baseline_text = show(root, rev, BASELINE)
    integrity = show(root, rev, INTEGRITY)
    if readme is None or baseline_text is None or integrity is None:
        return False
    if not all(path in readme for path in SPOTCHECKS):
        return False
    try:
        baseline = json.loads(baseline_text)
    except (json.JSONDecodeError, TypeError):
        return False
    checks = baseline.get("checks", {})
    if any(checks.get(key, {}).get("expect") != value
           for key, value in EXPECTED_COUNTS.items()):
        return False
    if EXPECTED_NOTE not in baseline.get("notes", {}):
        return False
    return (HOP_MARKER in integrity
            and "def commit_resolves(" in integrity
            and "inside_code_span" in integrity
            and "commit_resolves(hex_id" in integrity)


def score(root: Path, rev: str) -> tuple[int, dict[str, bool]]:
    checks = {"D1-r65-registries-committed": check_d1(root, rev),
              "D2-corpus-integrity-reconciled": check_d2(root, rev)}
    return sum(checks.values()), checks


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev")
    ap.add_argument("--root", type=Path, default=LANE)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        if args.rev:
            ap.error("--self-test cannot be combined with --rev")
        return self_test()
    if not args.rev:
        ap.error("--rev is required")
    root = args.root.resolve()
    base_check = git(root, "cat-file", "-e", BASE_REV + "^{commit}")
    requested_check = git(root, "cat-file", "-e", args.rev + "^{commit}")
    if base_check.returncode or requested_check.returncode:
        print("could-not-evaluate: BASE_REV or --rev is not a commit", file=sys.stderr)
        return 2
    base_n, base_checks = score(root, BASE_REV)
    if base_n != 0:
        print("could-not-evaluate: pinned base scores %d of 2, expected 0 of 2" % base_n,
              file=sys.stderr)
        return 2
    after_n, after_checks = score(root, args.rev)
    print("control at %s: %d of 2" % (BASE_REV[:8], base_n))
    for name, passed in after_checks.items():
        print("%s: %s" % (name, "PASS" if passed else "FAIL"))
    print("r66 routed defects closed %d of 2" % after_n)
    return 0 if after_n == 2 else 1


def _run(root: Path, *args: str) -> str:
    result = git(root, *args)
    if result.returncode:
        raise RuntimeError("git %s: %s" % (" ".join(args), result.stderr.strip()))
    return result.stdout.strip()


def _commit(root: Path, message: str) -> str:
    _run(root, "add", "-A")
    _run(root, "-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid",
         "commit", "-q", "-m", message)
    return _run(root, "rev-parse", "HEAD")


def _write(root: Path, path: str, text: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def self_test() -> int:
    assertions = 0
    failures = 0

    def check(label: str, got, want) -> None:
        nonlocal assertions, failures
        assertions += 1
        if got != want:
            failures += 1
            print("FAIL %s: got %r want %r" % (label, got, want))

    global BASE_REV
    saved_base = BASE_REV
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            init = git(root, "-c", "init.defaultBranch=main", "init", "-q")
            if init.returncode:
                raise RuntimeError("fixture git init failed: " + init.stderr.strip())
            _run(root, "config", "user.name", "fixture")
            _run(root, "config", "user.email", "fixture@example.invalid")
            old_baseline = json.dumps({"checks": {
                "corpus.index.tracked_files": {"expect": 116},
                "corpus.index.unindexed": {"expect": 4},
                "corpus.pointers.report_total": {"expect": 79},
                "corpus.pointers.report_dead": {"expect": 0},
                "corpus.pointers.commit_total": {"expect": 37},
                "corpus.pointers.commit_unresolvable": {"expect": 1},
                "corpus.pointers.commit_nonhash": {"expect": 0}}, "notes": {}})
            _write(root, README, "| old coverage | no spot-check paths |\n")
            _write(root, BASELINE, old_baseline)
            _write(root, INTEGRITY, "def commit_resolves_lane_only(): pass\n")
            base = _commit(root, "fixture base")
            BASE_REV = base
            base_n, base_checks = score(root, base)
            check("control/base-is-zero-of-two", base_n, 0)
            check("control/D1-absent", base_checks["D1-r65-registries-committed"], False)
            check("control/D2-absent", base_checks["D2-corpus-integrity-reconciled"], False)

            _write(root, REGISTRIES[0], '{"wave":"w1"}\n')
            _write(root, REGISTRIES[1], '{"wave":"w2"}\n')
            _write(root, README, "\n".join("| %s | indexed |" % p for p in SPOTCHECKS) + "\n")
            new_baseline = json.dumps({"checks": {
                key: {"expect": value} for key, value in EXPECTED_COUNTS.items()},
                "notes": {EXPECTED_NOTE: "reconciled counters"}})
            _write(root, BASELINE, new_baseline)
            _write(root, INTEGRITY,
                   HOP_MARKER + "\ndef commit_resolves(hex_id): pass\n"
                   "def inside_code_span(line): pass\n"
                   "lambda hex_id: commit_resolves(hex_id)\n")
            tip = _commit(root, "fixture repaired")
            honest_n, honest_checks = score(root, tip)
            check("honest/D1", honest_checks["D1-r65-registries-committed"], True)
            check("honest/D2", honest_checks["D2-corpus-integrity-reconciled"], True)
            check("honest/2-of-2", honest_n, 2)

            registry_mut = REGISTRIES[1]
            _run(root, "rm", "--", registry_mut)
            missing_registry = _commit(root, "mutant missing registry")
            check("kill/D1-missing-registry", check_d1(root, missing_registry), False)

            _write(root, REGISTRIES[1], '{"wave":"w2"}\n')
            _write(root, README, "| %s | indexed |\n" % SPOTCHECKS[0])
            missing_row = _commit(root, "mutant missing index rows")
            check("kill/D2-missing-index-row", check_d2(root, missing_row), False)

            _write(root, README, "\n".join("| %s | indexed |" % p for p in SPOTCHECKS) + "\n")
            bad_counts = json.loads(new_baseline)
            bad_counts["checks"]["corpus.index.tracked_files"]["expect"] += 1
            _write(root, BASELINE, json.dumps(bad_counts))
            bad_baseline = _commit(root, "mutant fitted baseline")
            check("kill/D2-baseline-drift", check_d2(root, bad_baseline), False)

            _write(root, BASELINE, new_baseline)
            _write(root, INTEGRITY, "def commit_resolves(hex_id): pass\n")
            no_hop = _commit(root, "mutant lane-only resolution")
            check("kill/D2-no-fleet-hop", check_d2(root, no_hop), False)

            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                exit_code = main(["--rev", tip, "--root", str(root)])
            check("public-main/honest-exit", exit_code, 0)
            check("public-main/honest-line",
                  "r66 routed defects closed 2 of 2" in output.getvalue(), True)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                exit_code = main(["--rev", base, "--root", str(root)])
            check("public-main/control-exit", exit_code, 1)
            check("public-main/control-line",
                  "r66 routed defects closed 0 of 2" in output.getvalue(), True)
    finally:
        BASE_REV = saved_base
    print("self-test: %d failure(s) over %d assertions" % (failures, assertions))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
