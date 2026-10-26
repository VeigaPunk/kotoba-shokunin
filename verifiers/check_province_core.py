#!/usr/bin/env python3
"""check_province_core.py — C3 counter for kotoba round 69.

Contract
--------
`python3 -B verifiers/check_province_core.py --rev <full-sha>` prints
    measured-rev: <full-sha>
    province core rows 2 of 2
and exits 0 when both areas are held in `PROVINCE.md` § Core, nonzero otherwise.  At the pinned
base `a5f7459f99bb27bf697e9438362e75ac5833eca8` it must print `province core rows 0 of 2`
and exit 1.

The surface: the two areas rounds 67 and 68 admitted into `corpus/knowledge/` but left on the
frontier side of `PROVINCE.md` (the round-68 closure: "`PROVINCE.md` § Core is untouched this
round (carried to 69)").  An area is held in § Core when ONE bullet of the `## Core` section
(the lines between `## Core` and the next `## ` heading):

  1. names the area's knowledge entry by its repo path (`corpus/knowledge/<file>`),
  2. names the area's counter by its repo path (`verifiers/<file>`),
  3. carries the round that admitted it (`round 67` / `round 68`),
and, at the same revision, the entry and the counter both exist and the entry has a
coverage-map row in `corpus/README.md`.

No-harm conjunct (global): the `## Frontier` and `## Adjacent` sections are byte-identical to
the base, so the Core rows are added without rewriting the sibling arbitration or the frontier
list.  Any global failure makes the count 0.

Trust boundary (QUALITY Q33): the counter is a structural check over committed bytes; it proves
the province names held ground, not that the ground is correct — the entries' own counters
(`check_instruction_authority.py`, `check_client_trust_gates.py`) carry that.

Exit codes: 0 both held · 1 not both held · 2 usage/environment error.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

BASE = "a5f7459f99bb27bf697e9438362e75ac5833eca8"
# Round 74 erratum (append-only ledger; plans/round-74-addendum-1.md E1.2, M138 in
# corpus/lessons/round-74.md): the no-harm conjunct below pins `## Adjacent` byte-identical to BASE,
# which was right when the round-69 claim was measured and is false after a LEGITIMATE re-pin of the
# sibling census.  A rewrite counts only when the whole section's sha256 is in this ledger with its
# reason; any other rewrite still reads `§ Adjacent differs from the base`.
ADJACENT_ERRATA: dict[str, str] = {
    "c41f7b54a97ea298d849f97140f1b28ae6a28d5f9a04de29c83ff5b666be674e": "round 74 re-pin of the sibling census (plans/round-74-addendum-1.md E1.2)",
}
PROVINCE = "PROVINCE.md"
README = "corpus/README.md"
AREAS = (
    ("round 67", "corpus/knowledge/instruction-authority-ladder-round67.md",
     "verifiers/check_instruction_authority.py"),
    ("round 68", "corpus/knowledge/client-trust-gates-round68.md",
     "verifiers/check_client_trust_gates.py"),
)
TOTAL = len(AREAS)


class EnvError(Exception):
    pass


def _show(repo: Path, rev: str, path: str) -> str | None:
    proc = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{path}"], capture_output=True, text=True)
    return proc.stdout if proc.returncode == 0 else None


def section(text: str, heading: str) -> str:
    m = re.search(rf"(?ms)^## {re.escape(heading)}[ \t]*\n.*?(?=^## |\Z)", text)
    return m.group(0) if m else ""


def bullets(core: str) -> list[str]:
    out: list[str] = []
    for line in core.splitlines():
        if re.match(r"^- ", line):
            out.append(line)
        elif out and line.startswith("  ") and line.strip():
            out[-1] += " " + line.strip()
    return out


def indexed(readme: str, entry: str) -> bool:
    token = f"`knowledge/{Path(entry).name}`"
    for line in readme.splitlines():
        cells = [c.strip() for c in line.strip()[1:].split("|")] if line.strip().startswith("|") else []
        if len(cells) >= 2 and cells[1] == token:
            return True
    return False


def check(read, base_province: str) -> tuple[int, list[str]]:
    """read(path) -> text or None at the measured revision."""
    province = read(PROVINCE)
    readme = read(README)
    if province is None or readme is None:
        raise EnvError(f"cannot read {PROVINCE} or {README} at the measured revision")
    findings: list[str] = []
    for name in ("Frontier", "Adjacent"):
        if section(province, name) != section(base_province, name):
            digest = hashlib.sha256(section(province, name).encode()).hexdigest()
            if name == "Adjacent" and digest in ADJACENT_ERRATA:
                continue
            findings.append(f"§ {name} differs from the base")
    core = bullets(section(province, "Core"))
    held = 0
    for rnd, entry, counter in AREAS:
        rows = [b for b in core if entry in b and counter in b and rnd in b]
        if not rows:
            findings.append(f"{entry}: no § Core bullet names the entry, {counter} and `{rnd}`")
            continue
        if read(entry) is None or read(counter) is None:
            findings.append(f"{entry}: the entry or {counter} is absent at the measured revision")
            continue
        if not indexed(readme, entry):
            findings.append(f"{entry}: no coverage-map row in {README}")
            continue
        held += 1
    if any(f.startswith("§ ") for f in findings):
        return 0, findings
    return held, findings


def selftest() -> int:
    entry67, entry68 = AREAS[0][1], AREAS[1][1]
    base = ("# P\n\n## Core\n\n- old row\n\n## Frontier\n\n- f\n\n## Adjacent\n\n| a | b |\n")
    good = base.replace("- old row\n", "- old row\n"
                        f"- Instruction authority ladder (round 67): `{entry67}`, `{AREAS[0][2]}`.\n"
                        f"- Client trust gates (round 68): `{entry68}`,\n  `{AREAS[1][2]}`.\n")
    readme = (f"| A | `knowledge/{Path(entry67).name}` | x |\n| B | `knowledge/{Path(entry68).name}` | x |\n")
    files = {PROVINCE: good, README: readme, entry67: "e", entry68: "e", AREAS[0][2]: "c", AREAS[1][2]: "c"}

    def run(over: dict) -> int:
        f = {**files, **over}
        return check(lambda p: f.get(p), base)[0]

    failures = 0
    if run({}) != TOTAL:
        print(f"FAIL honest world: {check(lambda p: files.get(p), base)}", file=sys.stderr)
        failures += 1
    else:
        print(f"PASS honest world: {TOTAL} of {TOTAL}")
    broken = {
        "base province": {PROVINCE: base},
        "row in Frontier, not Core": {PROVINCE: base.replace("- f\n", good.split("- old row\n")[1].split("\n## ")[0])},
        "row lacks the counter": {PROVINCE: good.replace(f"`{AREAS[0][2]}`", "")},
        "row lacks the round": {PROVINCE: good.replace("(round 67)", "")},
        "entry absent": {entry68: None},
        "counter absent": {AREAS[0][2]: None},
        "entry not indexed": {README: readme.replace(Path(entry67).name, "absent.md")},
        "Frontier rewritten": {PROVINCE: good.replace("- f\n", "- g\n")},
        "Adjacent rewritten": {PROVINCE: good.replace("| a | b |", "| a | c |")},
    }
    ledgered = good.replace("| a | b |", "| a | c |")
    ADJACENT_ERRATA[hashlib.sha256(section(ledgered, "Adjacent").encode()).hexdigest()] = "self-test"
    try:
        if run({PROVINCE: ledgered}) != TOTAL:
            print("FAIL ledgered Adjacent rewrite was rejected", file=sys.stderr)
            failures += 1
        else:
            print("PASS ledgered Adjacent rewrite is accepted")
        if run({PROVINCE: good.replace("| a | b |", "| a | d |")}) == TOTAL:
            print("FAIL an unledgered Adjacent rewrite survived the ledger", file=sys.stderr)
            failures += 1
        else:
            print("PASS an unledgered Adjacent rewrite is still rejected")
    finally:
        ADJACENT_ERRATA.clear()
    for name, over in broken.items():
        if run(over) == TOTAL:
            print(f"FAIL broken world survived: {name}", file=sys.stderr)
            failures += 1
        else:
            print(f"PASS broken world rejected: {name}")
    print(f"self-test: {failures} failure(s) over {len(broken) + 3} assertions")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="C3 counter for kotoba round 69")
    ap.add_argument("--rev", default=None)
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return selftest()
    repo = Path(args.repo)
    try:
        if not args.rev:
            raise EnvError("--rev <revision> is required")
        proc = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "--quiet", f"{args.rev}^{{commit}}"],
                              capture_output=True, text=True)
        if proc.returncode != 0:
            raise EnvError(f"unknown revision {args.rev}")
        sha = proc.stdout.strip()
        base_province = _show(repo, BASE, PROVINCE)
        if base_province is None:
            raise EnvError(f"cannot read {PROVINCE} at the base {BASE}")
        n, findings = check(lambda p: _show(repo, sha, p), base_province)
    except EnvError as exc:
        print(f"environment error: {exc}", file=sys.stderr)
        return 2
    print(f"measured-rev: {sha}")
    print(f"province core rows {n} of {TOTAL}")
    for f in findings:
        print(f"  - {f}")
    return 0 if n == TOTAL else 1


if __name__ == "__main__":
    sys.exit(main())
