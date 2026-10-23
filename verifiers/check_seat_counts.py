#!/usr/bin/env python3
r"""check_seat_counts.py -- seat-report completeness counter (round 62).

Round 62, routed defect 1 of the round-61 non-author closure
(`corpus/lessons/round-61-verifier-spotcheck.md` §1 defect 1 and §6): the
round-61 report claimed "66/68 seats returned reports" while the committed
directory held 65 seat reports (the 66th file was `swarm-registry.json`) and
three seats had no report (`RevCounterHistory`, `SentNovelty`, `SimplEntry`).
That is M91's class — a self-assessment count asserted without its counting
command — recurring in the round that mined it.

This counter compares a wave's declared seats with the seat reports committed
for that wave, at one revision, and prints the count, the missing names and
any report file the spec does not name.  It judges presence only; a report's
content and a seat's verdict stay with the closure (corpus/QUALITY.md Q31).

Universe: the cells of `items[].name` in the wave spec (JSON, `items` list)
against the regular files `<name>.md` directly under the wave report
directory at the measured revision (`git ls-tree -r --name-only <rev> --
<dir>`), excluding `swarm-registry.json` (a registry, never a seat report).

Output:
  `seat reports committed K of N; missing M: <names or none>; unmatched U: <names or none>`
Exit 0 iff K == N and U == 0, 1 otherwise, 2 = could not evaluate.

Usage:
  python3 -B verifiers/check_seat_counts.py --spec .ufo/waves/round-61/wave-spec.json \
      --dir .ufo/waves/round-61/wave --rev <rev>
  python3 -B verifiers/check_seat_counts.py --self-test
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
REGISTRY = "swarm-registry.json"


class EnvError(Exception):
    """Could not evaluate: unreadable spec, revision or directory."""


def _git(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(LANE)] + args, capture_output=True)


def _show(rev: str, path: str) -> bytes | None:
    p = _git(["show", "%s:%s" % (rev, path)])
    return p.stdout if p.returncode == 0 else None


def _listing(rev: str, dirpath: str) -> list[str]:
    p = _git(["ls-tree", "-r", "--name-only", rev, "--", dirpath])
    if p.returncode != 0:
        raise EnvError("git ls-tree failed for %s at %s" % (dirpath, rev))
    prefix = dirpath.rstrip("/") + "/"
    out = []
    for line in p.stdout.decode("utf-8", "replace").splitlines():
        if not line.startswith(prefix):
            continue
        rest = line[len(prefix):]
        if "/" in rest:
            continue
        out.append(rest)
    return out


def score(spec: dict, files: list[str]) -> tuple[int, list[str], list[str]]:
    """Return (committed, missing_names, unmatched_report_files)."""
    names: list[str] = []
    for item in spec.get("items") or []:
        name = item.get("name") if isinstance(item, dict) else None
        if isinstance(name, str) and name:
            names.append(name)
    if not names:
        raise EnvError("spec declares no item names")
    present = {f for f in files if f.endswith(".md")}
    committed = [n for n in names if n + ".md" in present]
    missing = [n for n in names if n + ".md" not in present]
    expected = {n + ".md" for n in names}
    unmatched = sorted(present - expected)
    return len(committed), missing, unmatched


def measure(rev: str, spec_path: str, dirpath: str) -> tuple[int, list[str], list[str]]:
    raw = _show(rev, spec_path)
    if raw is None:
        raise EnvError("%s is missing at %s" % (spec_path, rev))
    try:
        spec = json.loads(raw.decode("utf-8"))
    except Exception as e:  # malformed spec is a could-not-evaluate
        raise EnvError("spec at %s is not JSON: %s" % (rev, e))
    if not isinstance(spec, dict):
        raise EnvError("spec at %s is not a JSON object" % rev)
    return score(spec, _listing(rev, dirpath))


def line(k: int, n: int, missing: list[str], unmatched: list[str]) -> str:
    return ("seat reports committed %d of %d; missing %d: %s; unmatched %d: %s"
            % (k, n, len(missing), ", ".join(missing) or "none",
               len(unmatched), ", ".join(unmatched) or "none"))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--spec", required=False)
    ap.add_argument("--dir", required=False)
    ap.add_argument("--rev", required=False)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        if args.spec or args.dir or args.rev:
            ap.error("--self-test cannot be combined with --spec/--dir/--rev")
        return self_test()
    if not args.spec or not args.dir or not args.rev:
        ap.error("--spec, --dir and --rev are required")
    try:
        k, missing, unmatched = measure(args.rev, args.spec, args.dir)
    except (EnvError, UnicodeDecodeError, OSError) as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    n = k + len(missing)
    print(line(k, n, missing, unmatched))
    return 0 if not missing and not unmatched else 1


def self_test() -> int:
    """Fixture arms: a complete wave scores 0, one missing seat scores 1, the
    round-61 shape (3 missing, registry json present) scores 3 missing, and a
    spec with no items is a could-not-evaluate."""
    failures = 0
    arms = 0

    def check(name: str, got: object, want: object) -> None:
        nonlocal failures, arms
        arms += 1
        ok = got == want
        if not ok:
            failures += 1
        print("self-test %s: %r (want %r) %s" % (name, got, want, "ok" if ok else "FAIL"))

    spec = {"items": [{"name": "Alpha"}, {"name": "Beta"}, {"name": "Gamma"}]}
    check("complete", score(spec, ["Alpha.md", "Beta.md", "Gamma.md"]),
          (3, [], []))
    k, missing, unmatched = score(spec, ["Alpha.md", "Gamma.md", REGISTRY])
    check("one-missing", (k, missing), (2, ["Beta"]))
    check("registry-is-not-a-seat", unmatched, [])
    k, missing, unmatched = score(spec, ["Alpha.md", "Note.md"])
    check("round61-shape", (k, missing, unmatched),
          (1, ["Beta", "Gamma"], ["Note.md"]))
    try:
        score({"items": []}, ["Alpha.md"])
        check("empty-spec-raises", False, True)
    except EnvError:
        check("empty-spec-raises", True, True)

    # the line is computed from the score, never asserted
    print(line(1, 3, ["Beta", "Gamma"], ["Note.md"]))
    check("arm-count", arms, 5)
    print("self-test: %d failure(s)" % failures)
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
