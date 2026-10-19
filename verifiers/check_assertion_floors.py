#!/usr/bin/env python3
'''check_assertion_floors.py -- anti-shrink guard for the instruments' self-tests.

The claim under test: a self-test that silently loses assertions must never
still read green. Each instrument's --self-test prints an assertion count;
this guard reruns every self-test and FAILs when the observed count is below
the recorded floor (harness 10, corpus_integrity 88, corpus_independent 52,
surfaces 82, checklist 1504, pins 51 @ round 29). Exit: 0 all floors hold;
1 an instrument ran below its floor (named, observed-vs-floor); 2 an
instrument could not run or its output was unparseable. Read-only.

DOCUMENTED TRUST BOUNDARY (scout T4): the guard trusts each instrument's own
self-test output -- it detects silent block deletion and count drift, not a
self-test that deliberately prints a fake count. The instruments are the
trusted base of the verification stack; a malicious self-test is out of scope.
'''
import argparse
import re
import subprocess
import sys
from pathlib import Path

INSTRUMENTS = {
    "harness": ("verifiers/verify_harness_claims.py", 10,
                r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1),
    "corpus_integrity": ("verifiers/verify_corpus_integrity.py", 88,
                         r"self-test:\s*(\d+) failure\(s\) over (\d+) assertions", 2, 1),
    "corpus_independent": ("verifiers/verify_corpus_independent.py", 52,
                           r"self-test:\s*(\d+) assertions,\s*(\d+) failures", 1, 2),
    "surfaces": ("verifiers/verify_surfaces.py", 82,
                 r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
    "checklist": ("verifiers/verify_skill_checklist.py", 1504,
                  r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
    "pins": ("verifiers/check_substrate_pins.py", 51,
             r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1),
}


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--script", action="append", default=[], metavar="NAME=PATH")
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    paths = {name: repo / spec[0] for name, spec in INSTRUMENTS.items()}
    for override in args.script:
        if "=" not in override:
            parser.error("--script must be NAME=PATH")
        name, value = override.split("=", 1)
        if name not in paths:
            parser.error("unknown instrument: " + name)
        path = Path(value)
        paths[name] = path if path.is_absolute() else (repo / path).resolve()

    failed = False
    for name, (_, floor, pattern, assertion_group, failure_group) in INSTRUMENTS.items():
        proc = subprocess.run([sys.executable, str(paths[name]), "--self-test"],
                              cwd=repo, capture_output=True, text=True)
        match = re.search(pattern, proc.stdout)
        assertions = int(match.group(assertion_group)) if match else 0
        failures = int(match.group(failure_group)) if match else None
        ok = match is not None and assertions >= floor and failures == 0 and proc.returncode == 0
        print(("PASS" if ok else "FAIL") + " %s observed=%d floor=%d%s" % (
            name, assertions, floor,
            "" if failures == 0 else " summary=missing" if match is None
            else " self_test_failures=%d" % failures))
        failed |= not ok
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
