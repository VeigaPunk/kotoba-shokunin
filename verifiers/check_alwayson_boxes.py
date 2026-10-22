#!/usr/bin/env python3
r"""check_alwayson_boxes.py -- frozen counter for the round-53 C2 (operability) claim.

Round 53, claim C2: the `SKILL.md` § Always-on constraint-file checklist
(AGENTS.md-class) has 8 boxes and none is executed or delegated
(`verifiers/checklist-baseline.json` at BASE_REV: all 8 `unexecuted:`).  The
claim is that two of them run as a machine check that discriminates the cases
pinned below:

  alwayson.04  "No dated or transient text; dates and live-state go to status
               files."
  alwayson.07  "One canonical rule-file name per repo (AGENTS.md **or**
               CLAUDE.md, or an explicit redirect)."

The redirect forms for alwayson.07 are the two that Claude Code's current
memory documentation names (https://code.claude.com/docs/en/memory.md,
opened 2026-10-22, § Share one file with other coding tools): a `CLAUDE.md`
that imports `AGENTS.md` with an `@AGENTS.md` line, and a `CLAUDE.md` symlink to
`AGENTS.md`.  The same page states that with both files present and no import,
Claude Code reads `CLAUDE.md` only (§ AGENTS.md table), so two independent rule
files are read by different clients.  A prose mention of AGENTS.md is not an
import.

This counter is frozen at the round-53 plan commit.  The box set, the cases,
their expected statuses and the instrument contract are pinned here and never
read from the revision measured.

Instrument contract.  A box counts only if the revision's
`verifiers/checklist-baseline.json` gives it the disposition
`delegated:<repo-relative path>`, that file exists in the revision, and for
every pinned case of that box

  python3 -B <path> --check <box> --target <case dir> --json

exits 0 with a `checks` entry `{"id": "<box>", "status": "PASS"}` when the case
expects PASS, and exits 1 with that entry's status `FAIL` when the case expects
FAIL.  Any other exit code, a missing entry, unparseable JSON or a timeout
(20 s) makes the box not count.

Output: `always-on boxes executed and discriminating <N> of <T>` where T is the
number of boxes in the revision's map whose section is the always-on
checklist; then one line per pinned box.  Exit 0 iff N == 2 (both pinned
boxes), 1 otherwise, 2 = could not evaluate (git failure, unreadable map).
"""
from __future__ import annotations

import argparse
import io
import json
import os
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
SECTION = "Always-on constraint-file checklist (AGENTS.md-class)"
TIMEOUT = 20

RULES_A = "# Rules\n\n- Never push to the main branch.\n- Keep each commit to one change.\n"
RULES_B = "# Rules\n\n- Run the full test suite before every commit.\n"

# (case name, files {relative path: text or ("symlink", target)}, expected status)
CASES: dict[str, list[tuple[str, dict, str]]] = {
    "alwayson.04": [
        ("plain-rules", {"AGENTS.md": RULES_A}, "PASS"),
        ("version-number", {"AGENTS.md": RULES_A + "- Use Python 3.12 or later.\n"}, "PASS"),
        ("iso-date", {"AGENTS.md": RULES_A + "- Until 2026-11-01, route builds to the staging runner.\n"},
         "FAIL"),
        ("iso-timestamp", {"AGENTS.md": RULES_A + "- Deploy freeze started 2026-10-22T19:37Z.\n"}, "FAIL"),
        ("month-day", {"AGENTS.md": RULES_A + "- Until November 1, do not deploy on Fridays.\n"}, "FAIL"),
        ("dated-claude-md", {"CLAUDE.md": RULES_B + "- As of 2026-10-22 the staging runner is down.\n"},
         "FAIL"),
    ],
    "alwayson.07": [
        ("agents-only", {"AGENTS.md": RULES_A}, "PASS"),
        ("claude-only", {"CLAUDE.md": RULES_B}, "PASS"),
        ("import-redirect", {"AGENTS.md": RULES_A,
                             "CLAUDE.md": "@AGENTS.md\n\n## Claude Code\n\n- Use plan mode for billing changes.\n"},
         "PASS"),
        ("symlink-redirect", {"AGENTS.md": RULES_A, "CLAUDE.md": ("symlink", "AGENTS.md")}, "PASS"),
        ("two-rule-files", {"AGENTS.md": RULES_A, "CLAUDE.md": RULES_B}, "FAIL"),
        ("prose-mention", {"AGENTS.md": RULES_A,
                           "CLAUDE.md": "# Rules\n\nSee AGENTS.md for the shared rules.\n\n- Run the tests.\n"},
         "FAIL"),
    ],
}


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True).stdout


def self_test() -> int:
    expectations = {
        "counted": (
            0,
            "always-on boxes executed and discriminating 2 of 2",
            (
                "  alwayson.04: counted (6 of 6 cases as pinned)",
                "  alwayson.07: counted (6 of 6 cases as pinned)",
            ),
        ),
        "missing-delegate": (
            1,
            "always-on boxes executed and discriminating 1 of 2",
            (
                "  alwayson.04: counted (6 of 6 cases as pinned)",
                "  alwayson.07: not counted (delegate verifiers/missing.py absent at the revision)",
            ),
        ),
    }
    try:
        with tempfile.TemporaryDirectory(prefix="alwayson-self-test-") as td:
            root = Path(td)
            for name, (want_rc, count_line, findings) in expectations.items():
                repo = root / name
                verifiers = repo / "verifiers"
                verifiers.mkdir(parents=True)
                delegate = "verifiers/verify_alwayson.py"
                boxes = [
                    {
                        "box_id": "alwayson.04",
                        "section": SECTION,
                        "disposition": f"delegated:{delegate}",
                    },
                    {
                        "box_id": "alwayson.07",
                        "section": SECTION,
                        "disposition": (
                            "delegated:verifiers/missing.py"
                            if name == "missing-delegate" else f"delegated:{delegate}"
                        ),
                    },
                ]
                (verifiers / "checklist-baseline.json").write_text(
                    json.dumps({"boxes": boxes}), encoding="utf-8"
                )
                (verifiers / "verify_alwayson.py").write_bytes(
                    (LANE / "verifiers" / "verify_alwayson.py").read_bytes()
                )
                git(repo, "init", "--quiet")
                git(repo, "add", "verifiers")
                git(
                    repo, "-c", "user.name=Kotoba self-test",
                    "-c", "user.email=kotoba-self-test@invalid",
                    "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null",
                    "commit", "--quiet", "-m", "always-on counter self-test",
                )
                rev = git(repo, "rev-parse", "HEAD").decode("ascii").strip()
                result = subprocess.run(
                    [sys.executable, "-B", str(Path(__file__).resolve()),
                     "--rev", rev, "--repo", str(repo)],
                    capture_output=True, text=True,
                    timeout=TIMEOUT * sum(len(v) for v in CASES.values()) + 60,
                )
                if (result.returncode != want_rc or count_line not in result.stdout
                        or any(finding not in result.stdout for finding in findings)):
                    print(f"self-test failed: {name}", file=sys.stderr)
                    print(result.stdout, file=sys.stderr, end="")
                    print(result.stderr, file=sys.stderr, end="")
                    return 1
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired,
            UnicodeError, tarfile.TarError) as e:
        print(f"self-test could not run: {e}", file=sys.stderr)
        return 1
    print("self-test PASS: counted box exit 0; missing delegate exit 1")
    return 0


def plant(root: Path, files: dict) -> None:
    root.mkdir(parents=True)
    for rel, body in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(body, tuple):
            os.symlink(body[1], p)
        else:
            p.write_text(body, encoding="utf-8")


def run_case(script: Path, box: str, target: Path, expect: str) -> tuple[bool, str]:
    try:
        r = subprocess.run([sys.executable, "-B", str(script), "--check", box, "--target", str(target),
                            "--json"], capture_output=True, text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    try:
        data = json.loads(r.stdout)
        status = next(c.get("status") for c in data.get("checks", []) if c.get("id") == box)
    except (json.JSONDecodeError, StopIteration, AttributeError, TypeError):
        return False, f"exit {r.returncode}, no `{box}` entry"
    want_rc = 0 if expect == "PASS" else 1
    return (r.returncode == want_rc and status == expect), f"exit {r.returncode}, {status}"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--rev", help="lane revision to measure")
    ap.add_argument("--repo", default=str(LANE), help="lane repository")
    ap.add_argument("--self-test", action="store_true", help="exercise isolated fixtures")
    args = ap.parse_args(argv)
    if args.self_test:
        if args.rev:
            ap.error("--self-test cannot be combined with --rev")
        return self_test()
    if not args.rev:
        ap.error("--rev is required")
    repo = Path(args.repo)
    try:
        boxes = json.loads(git(repo, "show", f"{args.rev}:verifiers/checklist-baseline.json"))["boxes"]
        with tempfile.TemporaryDirectory(prefix="alwayson-") as td:
            tree = Path(td) / "tree"
            tree.mkdir()
            data = git(repo, "archive", "--format=tar", args.rev, "--", "verifiers")
            with tarfile.open(fileobj=io.BytesIO(data)) as tf:
                tf.extractall(tree, filter="data")
            section = [b for b in boxes if b.get("section") == SECTION]
            disp = {b["box_id"]: b.get("disposition", "") for b in section}
            lines, n = [], 0
            for box, cases in CASES.items():
                d = disp.get(box, "<absent>")
                if not d.startswith("delegated:"):
                    lines.append(f"  {box}: not counted (disposition {d.split(':')[0]})")
                    continue
                script = tree / d.split(":", 1)[1]
                if not script.is_file():
                    lines.append(f"  {box}: not counted (delegate {d.split(':', 1)[1]} absent at the revision)")
                    continue
                bad = []
                for name, files, expect in cases:
                    target = Path(td) / "cases" / box / name
                    plant(target, files)
                    ok, seen = run_case(script, box, target, expect)
                    if not ok:
                        bad.append(f"{name} expect {expect}, saw {seen}")
                if bad:
                    lines.append(f"  {box}: not counted ({len(bad)} of {len(cases)} cases wrong: "
                                 + "; ".join(bad) + ")")
                else:
                    n += 1
                    lines.append(f"  {box}: counted ({len(cases)} of {len(cases)} cases as pinned)")
    except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError, OSError, tarfile.TarError) as e:
        print(f"cannot evaluate: {e}", file=sys.stderr)
        return 2
    print(f"always-on boxes executed and discriminating {n} of {len(section)}")
    print("\n".join(lines))
    return 0 if n == len(CASES) else 1


if __name__ == "__main__":
    sys.exit(main())
