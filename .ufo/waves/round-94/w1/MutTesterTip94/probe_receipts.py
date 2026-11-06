#!/usr/bin/env python3
"""probe_receipts (MutTesterTip94, round 94 w1).

Bounded behavioural detector for NEW mutants of the fixed MALFORMED rule in
verifiers/fixtures/round-93/check-receipt-revs.sh, at a candidate revision
(freeze commit + ExecReceiptHeaders.patch). Mechanics mirror the frozen
counter's spirit: clone REV from REPO, apply each mutant as a literal
substitution of the instrument bytes in the probe's own clone working tree
(never committed), run the unmodified-then-mutated instrument on committed
fixture worlds, and compare observable behaviour (exit code AND full stdout)
against the honest (unmutated) readings recorded first in the same probe run.
A mutant is KILLED iff any world's (rc, stdout) differs from the honest
reading. A mutant whose bytes do not pass the heredoc python compile gate is
could-not-evaluate, never a kill. No checker source text is read to decide a
verdict; decisions use only process exit codes and output.

Usage: python3 -B probe_receipts.py <rev> <repo>
"""
from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TIMEOUT_S = 600
SCRIPT = "verifiers/fixtures/round-93/check-receipt-revs.sh"

WORLDS = [
    ("good", "verifiers/fixtures/round-94/receipt-headers/good"),
    ("hex41", "verifiers/fixtures/round-94/receipt-headers/hex41"),
    ("indented", "verifiers/fixtures/round-94/receipt-headers/indented"),
    ("r92-landing", ".ufo/waves/round-92/receipts/landing"),
    ("r93-landing", ".ufo/waves/round-93/receipts/landing"),
    ("r93-receipts", ".ufo/waves/round-93/receipts"),
]

A_SHAPE = "shaped_header = re.compile(r'(?:REV=|measured rev |rev )([0-9a-fA-F]+)')"
A_LSTRIP = "stripped = body.lstrip()"
A_EXIT = "sys.exit(1 if (unresolved or malformed) else 0 if resolved else 2)"
A_SHAPENULL = ("                        shape = shaped_header.match(stripped) or shaped_g1.match(stripped)\n"
               "                        if shape is None:")
A_PRINT = '                        print(f\'MALFORMED {path}:{number} {"; ".join(reasons)}\')'

MUTANTS = [
    ("r1-39hex-accepted", A_SHAPE, 1,
     "shaped_header = re.compile(r'(?:REV=|measured rev |rev )([0-9a-fA-F]{40,})')"),
    ("r2-tab-indent-ignored", A_LSTRIP, 1, "stripped = body.lstrip(' ')"),
    ("r3-malformed-exit-0", A_EXIT, 1,
     "sys.exit(1 if unresolved else 0 if resolved else 2)"),
    ("r4-scratch-swallows-malformed", A_SHAPENULL, 1,
     "                        shape = shaped_header.match(stripped) or shaped_g1.match(stripped)\n"
     "                        if shape is None or scratch_line.search(line):"),
    ("r5-malformed-not-printed", A_PRINT, 1,
     '                        suppressed = ("MALFORMED %s:%d" % (path, number))  # report suppressed'),
]


class NotEvaluated(Exception):
    pass


def heredoc_python(text: str) -> str:
    try:
        return text.split("<<'PY'\n", 1)[1].rsplit("\nPY\n", 1)[0]
    except IndexError:
        raise NotEvaluated("cannot locate the python heredoc in %s" % SCRIPT)


def run_worlds(clone: Path, env: dict) -> dict[str, tuple[int, str]]:
    results = {}
    for name, world in WORLDS:
        try:
            proc = subprocess.run(["bash", SCRIPT, world, str(clone)], cwd=clone, env=env,
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=TIMEOUT_S)
        except subprocess.TimeoutExpired:
            raise NotEvaluated("timeout after %ds on world %s" % (TIMEOUT_S, name))
        results[name] = (proc.returncode, proc.stdout.decode("utf-8", "replace"))
    return results


def first_diff(honest: tuple[int, str], got: tuple[int, str]) -> str:
    if honest[0] != got[0]:
        return "rc %d -> %d" % (honest[0], got[0])
    for a, b in zip(honest[1].splitlines(), got[1].splitlines()):
        if a != b:
            return "line %r -> %r" % (a, b)
    if len(honest[1].splitlines()) != len(got[1].splitlines()):
        return "line count %d -> %d" % (len(honest[1].splitlines()), len(got[1].splitlines()))
    return "no visible difference"


def main(argv: list[str]) -> int:
    rev, repo = argv[0], argv[1]
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r94" / "probe-receipts"
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
        print("probe-receipts rev %s repo %s script %s" % (rev, repo, SCRIPT))
        path = clone / SCRIPT
        if not path.is_file():
            raise NotEvaluated("script %s absent at %s" % (SCRIPT, rev))
        original = path.read_text(encoding="utf-8")
        compile(heredoc_python(original), "heredoc", "exec")
        sha_before = hashlib.sha256(original.encode("utf-8")).hexdigest()
        print("script sha256 before %s" % sha_before)

        honest = run_worlds(clone, env)
        for name, (rc, out) in honest.items():
            tail = [ln for ln in out.splitlines() if ln.strip()]
            print("honest world %s rc %d: %s" % (name, rc, tail[-2] if len(tail) > 1 else (tail[-1] if tail else "<no output>")))

        verdicts = {}
        for name, anchor, count, repl in MUTANTS:
            found = original.count(anchor)
            if found != count:
                verdicts[name] = "CNE"
                print("mutant %s CNE: anchor matches %d time(s), expected %d" % (name, found, count))
                continue
            mutated = original.replace(anchor, repl)
            try:
                compile(heredoc_python(mutated), "heredoc", "exec")
            except SyntaxError as exc:
                verdicts[name] = "CNE"
                print("mutant %s CNE: does not compile: %s" % (name, exc.msg))
                continue
            path.write_text(mutated, encoding="utf-8")
            try:
                got = run_worlds(clone, env)
            finally:
                path.write_text(original, encoding="utf-8")
            diffs = [w for w in honest if honest[w] != got[w]]
            killed = bool(diffs)
            verdicts[name] = "killed" if killed else "survived"
            detail = "; ".join("%s (%s)" % (w, first_diff(honest[w], got[w])) for w in diffs) or "all worlds identical"
            print("mutant %s %s: %s" % (name, "KILLED" if killed else "SURVIVED", detail))

        sha_after = hashlib.sha256(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
        print("script sha256 after %s restored %s" % (sha_after, sha_after == sha_before))
        for name, v in verdicts.items():
            print("verdict %s %s" % (name, v))
        return 0
    except NotEvaluated as exc:
        print("probe-receipts-NOT-EVALUATED: %s" % exc)
        return 2
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
