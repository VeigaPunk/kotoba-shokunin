#!/usr/bin/env python3
"""build-forgeries (round 96, pre-data controls for claim C1; plans/round-96.md).

Usage: python3 -B verifiers/fixtures/round-96/build-forgeries.py REV OUTDIR
Builds five control worlds of verifiers/verify_dispatch_prompts.py at REV. Each inserts code at the
end of self_test() (before the `for f in failures:` report loop) that tries to reach the C1 target
without behavioural arms that observe the mutated behaviour and report it as a failure:
  f1-text-sniff        reads its own source and fails when a mutant's replacement text is present
                       (the round-94/95 forgery shape, ported; tokens stored reversed so the honest
                       source never contains them)
  f2-crash-signal      drives the t04 behaviour (round 7 at latest dispatched 7 must PASS) but signals
                       the deviation by an uncaught RuntimeError (v3 rule 1: a RUN-ERROR is no kill)
  f3-summary-no-line   drives the same t04 behaviour but signals by printing a failure summary and
                       exiting 1 with no `self-test FAIL: ` line (the MutTesterCounter95 M2 shape)
  f4-honest-trip       records one failing assertion on every run, honest included (the
                       MutTesterCounter95 M6 shape: every mutant "killed", honest not CLEAN)
  f5-label-only        eleven assertions named after the targets that assert nothing (always true)
For each world it writes OUTDIR/<name>.patch (git diff against REV) and commits the world in a
scratch repository OUTDIR/<name>.repo (identity `forgery <forgery@example.invalid>`, never the lane),
printing `<name> <commit> <repo>` so the frozen counter runs as `selftest-kills.py c1 <commit> <repo>`.
Expected (counter v4): all five UNMET; f2 and f3 read `run errors 1`; f4 reads honest
REPORTED-FAILURE.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

INSTRUMENT = "verifiers/verify_dispatch_prompts.py"
ANCHOR = "    for f in failures:\n        print(\"self-test FAIL: %s\" % f)\n"
# the mutants' replacement texts (counter v4 CLAIMS["c1"]), stored reversed
TOKENS = (
    "return bool(PLACEHOLDER_RE.search(token))\n",
    'VARIABLE_RE = re.compile(r"\\$\\{[^}]*\\}")',
    'VARIABLE_RE = re.compile(r"\\$[A-Za-z_][A-Za-z0-9_]*")',
    "if round_n < value:",
    "elif not files:",
    "m = ROLE_ROUND_RE.search(text)",
    "elif round_n not in dirs:",
    "in paths[:1] if",
    "in stems[:1] if",
    'return "baseline", 10 ** 9, "non-integer',
    'verdicts[cid] = {"status": "PASS",',
)
EQ_WORLD = (
    "    _eqroot = Path(tempfile.mkdtemp(prefix=\"forgery-eq-\"))\n"
    "    _eq = _write_case(_eqroot, \"eq\", SELF_TEST_PROMPT.format(round=7), \"7\", None)\n"
    "    _eqf = _verdict_of(evaluate_dispatch_08(_eq / \"prompts\", _eq / \"state\", _eq / \"fleet\"),\n"
    "                       \"kote-round-7.md\")\n"
    "    shutil.rmtree(_eqroot, ignore_errors=True)\n"
)
WORLDS = {
    "f1-text-sniff": (
        "    _src = Path(__file__).read_text(encoding=\"utf-8\")\n"
        "    for _tok in (" + ", ".join("%r[::-1]" % t[::-1] for t in TOKENS) + ",):\n"
        "        rec(\"forgery f1: source free of %r\" % _tok, _tok not in _src, _tok)\n"),
    "f2-crash-signal": EQ_WORLD + (
        "    if not (_eqf and _eqf[\"verdict\"] == \"PASS\"):\n"
        "        raise RuntimeError(\"forgery f2: equality world is %r\" % (_eqf,))\n"),
    "f3-summary-no-line": EQ_WORLD + (
        "    if not (_eqf and _eqf[\"verdict\"] == \"PASS\"):\n"
        "        print(\"%d failure(s) over %d assertions\" % (len(failures) + 1, total + 1))\n"
        "        sys.exit(1)\n"),
    "f4-honest-trip": (
        "    rec(\"forgery f4: one failing assertion on every run\", False, None)\n"),
    "f5-label-only": "".join(
        "    rec(\"t%02d arm (label only)\", True, None)\n" % i for i in range(1, 12)),
}


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE).stdout.decode()


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: build-forgeries.py REV OUTDIR", file=sys.stderr)
        return 2
    lane = Path(__file__).resolve().parents[3]
    rev = git("-C", str(lane), "rev-parse", "--verify", argv[0] + "^{commit}").strip()
    out = Path(argv[1]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    for name, insert in WORLDS.items():
        repo = out / (name + ".repo")
        git("clone", "-q", "--shared", str(lane), str(repo))
        if git("-C", str(repo), "rev-parse", "--show-toplevel").strip() != str(repo):
            raise SystemExit("fixture toplevel mismatch for %s" % name)
        git("-C", str(repo), "checkout", "-q", "-b", "forgery", rev)
        path = repo / INSTRUMENT
        text = path.read_text(encoding="utf-8")
        if text.count(ANCHOR) != 1:
            raise SystemExit("anchor miss in %s" % name)
        text = text.replace(ANCHOR, insert + ANCHOR)
        compile(text, str(path), "exec", dont_inherit=True)
        path.write_text(text, encoding="utf-8")
        (out / (name + ".patch")).write_text(git("-C", str(repo), "diff", "--binary"), encoding="utf-8")
        git("-C", str(repo), "-c", "user.name=forgery", "-c", "user.email=forgery@example.invalid",
            "commit", "-q", "-am", "forgery world " + name)
        print(name, git("-C", str(repo), "rev-parse", "HEAD").strip(), repo)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
