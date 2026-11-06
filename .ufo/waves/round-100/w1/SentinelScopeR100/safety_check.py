#!/usr/bin/env python3
"""SentinelScopeR100 safety scanner (round 100).

Usage: python3 -B safety_check.py REPO BASE CAND
Scans only the lines ADDED by BASE..CAND in verifiers/*.py (and reports the added
lines of every changed file). Prints PASS/FAIL per rule. Exit 0 iff all PASS.
"""
from __future__ import annotations

import re
import subprocess
import sys

NET = re.compile(r"\b(socket|urllib|http\.client|httplib|requests|ftplib|smtplib|"
                 r"telnetlib|xmlrpc|aiohttp|urlopen|urlretrieve)\b")
CRED = re.compile(r"(?i)(api[_-]?key|secret|passwd|password|bearer\s+[A-Za-z0-9._-]{12,}|"
                  r"ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|"
                  r"BEGIN [A-Z ]*PRIVATE KEY)")
TMP = re.compile(r"(?<![\w/])/tmp(?:/|\b)")
CHMOD0 = re.compile(r"chmod\(\s*0|S_IRUSR|mode=0o?0\b|0o000")

fails: list[str] = []


def run(*args: str) -> str:
    p = subprocess.run(args, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("%s -> rc %d: %s" % (" ".join(args), p.returncode, p.stderr.strip()))
    return p.stdout


def report(ok: bool, name: str, detail: str) -> None:
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)
    if not ok:
        fails.append(name)


def main() -> int:
    repo, base, cand = sys.argv[1], sys.argv[2], sys.argv[3]
    diff = run("git", "-C", repo, "diff", "--unified=0", base, cand, "--",
               "verifiers/", "corpus/")
    added: list[tuple[str, int, str]] = []
    path = None
    for ln in diff.splitlines():
        if ln.startswith("+++ b/"):
            path = ln[6:]
        elif ln.startswith("+") and not ln.startswith("+++"):
            added.append((path or "?", 0, ln[1:]))
    py_added = [(p, t) for p, _, t in added if p.endswith(".py")]
    print("added lines: total=%d python=%d" % (len(added), len(py_added)))

    tmp_hits = [(p, t.strip()) for p, t in py_added if TMP.search(t)]
    report(not tmp_hits, "no-hardcoded-tmp", "hits=%s" % tmp_hits[:5])

    net_hits = [(p, t.strip()) for p, t in py_added if NET.search(t)]
    report(not net_hits, "no-network", "hits=%s" % net_hits[:5])

    cred_hits = [(p, t.strip()) for p, _, t in added if CRED.search(t)]
    report(not cred_hits, "no-credential-shapes", "hits=%s" % cred_hits[:5])

    chmod_hits = [(p, t.strip()) for p, t in py_added if CHMOD0.search(t)]
    print("INFO chmod-000-shaped added lines: %s" % chmod_hits[:8])

    tmpdir_hits = [(p, t.strip()) for p, t in py_added
                   if "TMPDIR" in t or "tempfile" in t or "mkdtemp" in t]
    print("INFO TMPDIR/tempfile added lines: %d (sample %s)"
          % (len(tmpdir_hits), tmpdir_hits[:5]))

    print("SAFETY %s" % ("PASS" if not fails else "FAIL " + ",".join(fails)))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
