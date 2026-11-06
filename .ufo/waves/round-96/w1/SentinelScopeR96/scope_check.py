#!/usr/bin/env python3
"""SentinelScopeR96 scope check: candidate vs freeze 679775a.

Checks (each prints PASS/FAIL + observed line):
  A. `git diff --name-status BASE..CAND` lists only owned paths.
  B. SKILL.md blob identical to base.
  C. no spotcheck file, dispatch-prompts fixture, round-9x fixture, round-96
     fixture, floors registry, plan, or other verifier touched.
  D. verify_dispatch_prompts.py: bytes before the self-test section and from
     box_proof() to EOF identical to base.
  E. corpus/SOURCES.md: additions only, exactly two new registry rows S271/S272.
  F. corpus/README.md: additions only, one new row naming the round-96 lesson.
  G. corpus/lessons/round-96.md: a new file at the candidate.
"""
from __future__ import annotations

import re
import subprocess
import sys

BASE = "679775abb9277a7b8d17f060b0f5b4ced2b127b6"
OWNED = {
    "verifiers/verify_dispatch_prompts.py",
    "corpus/SOURCES.md",
    "corpus/lessons/round-96.md",
    "corpus/README.md",
}
DP = "verifiers/verify_dispatch_prompts.py"
PREFIX_MARK = "    return results\n"
SUFFIX_MARK = "def box_proof(map_path: Path, fixtures: Path) -> int:"


def git(repo: str, *args: str) -> str:
    p = subprocess.run(["git", "-C", repo, *args], stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)
    if p.returncode != 0:
        raise SystemExit("git %s failed: %s" % (" ".join(args),
                                                p.stdout.decode()))
    return p.stdout.decode()


def blob(repo: str, rev: str, path: str) -> str:
    return git(repo, "cat-file", "-p", "%s:%s" % (rev, path))


def main(argv: list[str]) -> int:
    repo, cand = argv[0], argv[1]
    fails = 0

    def rec(name: str, ok: bool, got: object) -> None:
        nonlocal fails
        fails += 0 if ok else 1
        print("%s %s: %r" % ("PASS" if ok else "FAIL", name, got))

    # A + C: changed paths
    raw = git(repo, "diff", "--name-status", BASE, cand)
    rows = [ln.split("\t") for ln in raw.splitlines() if ln.strip()]
    changed = {r[-1] for r in rows}
    rec("A changed paths are exactly the owned set", changed == OWNED,
        sorted(changed))
    extra = sorted(changed - OWNED)
    rec("C no unowned path changed", not extra, extra)
    forbidden = [p for p in changed if (
        p == "SKILL.md"
        or re.search(r"verifier-spotcheck\.md$", p)
        or p.startswith("verifiers/fixtures/dispatch-prompts/")
        or p.startswith("verifiers/fixtures/round-9")
        or p == "verifiers/floors-registry.json"
        or p.startswith("plans/")
        or (p.startswith("verifiers/") and p.endswith((".py", ".sh"))
            and p != DP))]
    rec("C no forbidden path (spotcheck/fixtures/plan/floors/other verifier)",
        not forbidden, forbidden)

    # B: SKILL.md
    rec("B SKILL.md byte-identical", blob(repo, "HEAD", "SKILL.md") == blob(repo, BASE, "SKILL.md") if False else
        git(repo, "rev-parse", "%s:SKILL.md" % cand) == git(repo, "rev-parse", "%s:SKILL.md" % BASE),
        (git(repo, "rev-parse", "%s:SKILL.md" % cand).strip(),
         git(repo, "rev-parse", "%s:SKILL.md" % BASE).strip()))
    rec("B SKILL.md is 600 lines",
        len(blob(repo, cand, "SKILL.md").splitlines()) == 600,
        len(blob(repo, cand, "SKILL.md").splitlines()))

    # D: production code of the instrument
    b = blob(repo, BASE, DP)
    c = blob(repo, cand, DP)
    bi, ci = b.index(PREFIX_MARK) + len(PREFIX_MARK), c.index(PREFIX_MARK) + len(PREFIX_MARK)
    bs, cs = b.index(SUFFIX_MARK), c.index(SUFFIX_MARK)
    rec("D instrument prefix through run_checks() byte-identical",
        b[:bi] == c[:ci], (len(b[:bi]), len(c[:ci])))
    rec("D instrument suffix box_proof()/main() byte-identical",
        b[bs:] == c[cs:], (len(b[bs:]), len(c[cs:])))
    rec("D instrument middle (self-test section) is the only changed region",
        b[bi:bs] != c[ci:cs], (len(b[bi:bs]), len(c[ci:cs])))

    # E: SOURCES.md append-only, two rows S271/S272
    d = git(repo, "diff", "-U0", BASE, cand, "--", "corpus/SOURCES.md")
    minus = [ln for ln in d.splitlines() if ln.startswith("-") and not ln.startswith("---")]
    plus = [ln for ln in d.splitlines() if ln.startswith("+") and not ln.startswith("+++")]
    rec("E SOURCES.md additions only (no removed line)", not minus, minus[:3])
    new_ids = re.findall(r"\|\s*(S\d{3})\s*\|", "\n".join(plus))
    rec("E SOURCES.md adds exactly S271 and S272", sorted(set(new_ids)) == ["S271", "S272"],
        new_ids)

    # F: README one row
    d = git(repo, "diff", "-U0", BASE, cand, "--", "corpus/README.md")
    minus = [ln for ln in d.splitlines() if ln.startswith("-") and not ln.startswith("---")]
    plus = [ln for ln in d.splitlines() if ln.startswith("+") and not ln.startswith("+++")]
    rec("F corpus/README.md additions only", not minus, minus[:3])
    rec("F corpus/README.md adds one row naming round-96",
        len(plus) == 1 and "round-96" in plus[0], plus)

    # G: new lesson file
    rec("G corpus/lessons/round-96.md exists at candidate",
        git(repo, "cat-file", "-e", "%s:corpus/lessons/round-96.md" % cand).strip() == "",
        "present")

    print("scope fails: %d" % fails)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
