#!/usr/bin/env python3
r"""check_opencode_repin.py -- frozen counter for the round-53 C1 (freshness) claim.

Round 53, claim C1: the host's opencode moved from npm `opencode-ai` 1.19.3
(sha256 179ca421...) to 1.19.4 (sha256 538fcb1b...) at 2026-10-22T17:50:30Z.
Since then `verifiers/verify_surfaces.py --json` reads `pass 6`
(`surfaces.opencode_extract` FAIL: rules OC-4 and OC-6 match nothing) and
`verifiers/check_substrate_pins.py` reads `DRIFT 1/3`.  The claim is that the
opencode extraction is re-derived from the 1.19.4 bytes and re-pinned, without
retiring, re-kinding or re-verdicting any declared opencode class.

This counter is frozen at the round-53 plan commit.  BASE_REV, the check
count, the self-test floor and the output line are pinned here and never read
from the revision measured.

For the revision given by `--rev`, the counter extracts that revision's tree
(`git archive <rev> -- verifiers corpus`) into a temporary directory and, from that tree:

  S  runs `verifiers/verify_surfaces.py --json --repo <tree>` against the
     installed binaries (the script's own default paths): P = the number of
     PASS checks, and the status of `surfaces.opencode_extract`;
  P  runs `verifiers/check_substrate_pins.py --json --repo <tree>`: the
     number of pins that hold out of the pins checked;
  K  compares the opencode classes declared in the tree's
     `verifiers/surfaces-baseline.json` with those declared at BASE_REV:
     a BASE_REV class counts as kept iff the same `class_id` is declared at
     the revision with the same `literal`, `context_kind` and `verdict`;
  T  runs `verifiers/verify_surfaces.py --self-test` from the tree: failures
     F and assertions A.

Output (one line, then the observed substrate):
  `opencode re-pin: surfaces pass <P> of 7 (opencode_extract <status>); pins
   OK <k>/<n>; opencode classes kept <K> of <N0>; self-test <F> failure(s)
   over <A> assertions`
Exit 0 iff P == 7, opencode_extract is PASS, k == n == 3, K == N0,
F == 0 and A >= SELFTEST_FLOOR; 1 otherwise; 2 = could not evaluate.

The counter reads the installed opencode and omp binaries, so its result names
the substrate it measured (path, sha256, bytes) on the second line.  A rebuilt
host binary is a different measurement, not the same one.
Usage:
  python3 -B verifiers/check_opencode_repin.py --rev <rev> [--repo <repo>]
  python3 -B verifiers/check_opencode_repin.py --self-test

The self-test builds isolated local git worlds and does not read host binaries.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

BASE_REV = "e78dff667237fba2e3cf9eccb802eff5bc9ea302"
CHECKS_TOTAL = 7
PINS_TOTAL = 3
SELFTEST_FLOOR = 129  # verifiers/floors-registry.json `surfaces` at BASE_REV
LANE = Path(__file__).resolve().parent.parent


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True).stdout


def extract(repo: Path, rev: str, dest: Path) -> None:
    data = git(repo, "archive", "--format=tar", rev, "--", "verifiers", "corpus")
    with tarfile.open(fileobj=io.BytesIO(data)) as tf:
        tf.extractall(dest, filter="data")


def opencode_classes(raw: bytes) -> dict[str, tuple]:
    data = json.loads(raw)
    out = {}
    for row in data.get("classes", []):
        if row.get("harness") == "opencode":
            out[row["class_id"]] = (row.get("literal"), row.get("context_kind"),
                                    row.get("verdict"))
    return out


def self_test() -> int:
    """Exercise one clean and one retired-class world without host binaries."""
    global BASE_REV
    assertions = 0
    failures = 0

    def check(name: str, ok: bool, detail: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if not ok:
            failures += 1
            print(f"FAIL {name}: {detail}")

    try:
        with tempfile.TemporaryDirectory(prefix="oc-repin-self-test-") as td:
            repo = Path(td) / "repo"
            repo.mkdir()

            def fixture_git(*args: str) -> str:
                return subprocess.run(
                    ["git", "-C", str(repo), *args], check=True, capture_output=True,
                    text=True).stdout.strip()

            fixture_git("init", "-q")
            fixture_git("config", "user.name", "opencode repin self-test")
            fixture_git("config", "user.email", "opencode-repinselftest@example.invalid")
            verifiers = repo / "verifiers"
            verifiers.mkdir()
            corpus = repo / "corpus"
            corpus.mkdir()
            (corpus / "fixture.md").write_text("fixture\n", encoding="utf-8")
            base_classes = {
                "classes": [{
                    "class_id": "opencode:fixture/AGENTS.md",
                    "harness": "opencode",
                    "literal": "AGENTS.md",
                    "context_kind": "doc",
                    "verdict": "governed",
                }]
            }
            (verifiers / "surfaces-baseline.json").write_text(
                json.dumps(base_classes), encoding="utf-8")
            (verifiers / "verify_surfaces.py").write_text(
                "import json, sys\n"
                "from pathlib import Path\n"
                "args = sys.argv[1:]\n"
                "if '--self-test' in args:\n"
                "    print('0 failure(s) over 129 assertions')\n"
                "    raise SystemExit(0)\n"
                "root = Path(args[args.index('--repo') + 1])\n"
                "rows = json.loads((root / 'verifiers' / "
                "'surfaces-baseline.json').read_text())['classes']\n"
                "has_opencode = any(r.get('harness') == 'opencode' for r in rows)\n"
                "checks = [{'id': f'surfaces.fixture_{i}', 'status': 'PASS'} "
                "for i in range(6)]\n"
                "checks.append({'id': 'surfaces.opencode_extract', "
                "'status': 'PASS' if has_opencode else 'FAIL'})\n"
                "print(json.dumps({'checks': checks, 'substrate': {'opencode': "
                "{'path': 'fixture/opencode', 'sha256': 'fixture', 'bytes': 1}}}))\n",
                encoding="utf-8")
            (verifiers / "check_substrate_pins.py").write_text(
                "import json\n"
                "print(json.dumps({'checks': [{'verdict': 'PASS'} for _ in range(3)]}))\n",
                encoding="utf-8")
            fixture_git("add", "verifiers", "corpus")
            fixture_git("-c", "core.hooksPath=/dev/null", "commit", "-q", "-m", "base")
            fixture_base = fixture_git("rev-parse", "HEAD")
            previous_base = BASE_REV
            BASE_REV = fixture_base
            try:
                def run_world(rev: str) -> tuple[int, str]:
                    stdout = io.StringIO()
                    stderr = io.StringIO()
                    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                        code = main(["--rev", rev, "--repo", str(repo)])
                    return code, stdout.getvalue() + stderr.getvalue()

                clean_rev = fixture_git("rev-parse", "HEAD")
                code, output = run_world(clean_rev)
                clean_line = ("opencode re-pin: surfaces pass 7 of 7 "
                              "(opencode_extract PASS); pins OK 3/3; "
                              "opencode classes kept 1 of 1; self-test "
                              "0 failure(s) over 129 assertions")
                check("retained class is clean",
                      code == 0 and clean_line in output, (code, output.strip()))

                (verifiers / "surfaces-baseline.json").write_text(
                    json.dumps({"classes": []}), encoding="utf-8")
                fixture_git("add", "verifiers/surfaces-baseline.json")
                fixture_git("-c", "core.hooksPath=/dev/null", "commit", "-q",
                            "-m", "retire opencode class")
                retired_rev = fixture_git("rev-parse", "HEAD")
                code, output = run_world(retired_rev)
                failed_line = ("opencode re-pin: surfaces pass 6 of 7 "
                               "(opencode_extract FAIL); pins OK 3/3; "
                               "opencode classes kept 0 of 1; self-test "
                               "0 failure(s) over 129 assertions")
                check("retired class is failed with stable finding",
                      code == 1 and failed_line in output, (code, output.strip()))
            finally:
                BASE_REV = previous_base
    except (OSError, subprocess.CalledProcessError, ValueError) as exc:
        check("isolated fixture execution", False, str(exc))

    print(f"{failures} failure(s) over {assertions} assertions")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--rev", help="lane revision to measure")
    ap.add_argument("--repo", default=str(LANE), help="lane repository")
    ap.add_argument("--self-test", action="store_true",
                    help="exercise the repin verdict on isolated fixtures")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.rev is None:
        ap.error("--rev is required unless --self-test is selected")
    repo = Path(args.repo)
    try:
        base = opencode_classes(git(repo, "show", f"{BASE_REV}:verifiers/surfaces-baseline.json"))
        with tempfile.TemporaryDirectory(prefix="oc-repin-") as td:
            tree = Path(td)
            extract(repo, args.rev, tree)
            gate = tree / "verifiers" / "verify_surfaces.py"
            pins = tree / "verifiers" / "check_substrate_pins.py"
            if not gate.is_file() or not pins.is_file():
                print("cannot evaluate: gate or pin script missing at the revision", file=sys.stderr)
                return 2
            s = subprocess.run([sys.executable, "-B", str(gate), "--json", "--repo", str(tree)],
                               capture_output=True, text=True)
            sj = json.loads(s.stdout)
            checks = sj.get("checks", sj.get("results", []))
            p = sum(1 for c in checks if c.get("status") == "PASS")
            oc = next((c.get("status") for c in checks if c.get("id") == "surfaces.opencode_extract"),
                      "ABSENT")
            q = subprocess.run([sys.executable, "-B", str(pins), "--json", "--repo", str(tree)],
                               capture_output=True, text=True)
            qj = json.loads(q.stdout)
            prow = qj.get("checks", qj.get("results", qj.get("pins", [])))
            n = len(prow)
            k = sum(1 for r in prow if r.get("verdict") == "PASS")
            rev_cls = opencode_classes((tree / "verifiers" / "surfaces-baseline.json").read_bytes())
            kept = sum(1 for cid, v in base.items() if rev_cls.get(cid) == v)
            t = subprocess.run([sys.executable, "-B", str(gate), "--self-test", "--repo", str(tree)],
                               capture_output=True, text=True)
            tail = (t.stdout + t.stderr).strip().splitlines()
            f = a = -1
            for line in reversed(tail):
                parts = line.split()
                if "failure(s)" in parts and "assertions" in line:
                    f = int(parts[0])
                    a = int(parts[parts.index("over") + 1])
                    break
            sub = sj.get("substrate", {}).get("opencode", {})
    except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError, ValueError, OSError,
            tarfile.TarError) as e:
        print(f"cannot evaluate: {e}", file=sys.stderr)
        return 2
    print(f"opencode re-pin: surfaces pass {p} of {CHECKS_TOTAL} (opencode_extract {oc}); "
          f"pins OK {k}/{n}; opencode classes kept {kept} of {len(base)}; "
          f"self-test {f} failure(s) over {a} assertions")
    print(f"substrate opencode: {sub.get('path')} sha256 {sub.get('sha256')} bytes {sub.get('bytes')}")
    ok = (p == CHECKS_TOTAL and oc == "PASS" and k == n == PINS_TOTAL and kept == len(base)
          and f == 0 and a >= SELFTEST_FLOOR)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
