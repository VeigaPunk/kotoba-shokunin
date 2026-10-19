#!/usr/bin/env python3
"""R1 counter-instrument: N/N agreement with ZERO substrate derivation.

Review probe ONLY — not a lane instrument; must never land in verifiers/.

Purpose: show that C1's counting command (`agreement N/28`) cannot distinguish
"source-blind independent re-derivation" from "expectations copied off the
harness's own --json stdout". This script complies with the letter of the
declared blindness rule: it never opens verifiers/verify_harness_claims.py,
verifiers/baseline.json, or any corpus doc. It only *runs* the harness and
reads its stdout, which the claim's own comparison design requires anyway.

Usage: counter_blind.py [extra harness args...]   e.g. --oc-log <fixture>
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

def _repo_root(start: pathlib.Path) -> pathlib.Path:
    for p in [start, *start.parents]:
        if (p / "verifiers/verify_harness_claims.py").is_file():
            return p
    raise SystemExit(f"repo root not found above {start}")

REPO = _repo_root(pathlib.Path(__file__).resolve().parent)
HARNESS = REPO / "verifiers/verify_harness_claims.py"


def run(*extra: str) -> tuple[int, dict]:
    proc = subprocess.run(
        [sys.executable, str(HARNESS), "--json", *extra],
        capture_output=True, text=True, cwd=REPO,
    )
    return proc.returncode, json.loads(proc.stdout)


def agrees(mode: str, got, want) -> bool:
    if mode in ("equal", "zero"):
        return got == want
    if mode in ("positive", "at_least"):
        return isinstance(got, int) and isinstance(want, int) and got >= want
    return False


def main(argv: list[str]) -> int:
    # phase 1 — LEAK: harvest id/mode/expected from the harness's own stdout
    code0, leak = run()
    copied = {r["check"]: (r["mode"], r["expected"]) for r in leak["results"]}
    assert len(copied) == 28, f"expected 28 rows, harvested {len(copied)}"

    # phase 2 — OBSERVE: harness in --no-baseline mode reads no pin at all
    code1, obs = run("--no-baseline", *argv)
    observed = {r["check"]: r["observed"] for r in obs["results"]}

    rows = [(cid, agrees(copied[cid][0], observed[cid], copied[cid][1])) for cid in copied]
    bad = [cid for cid, ok in rows if not ok]
    exact = sum(1 for cid in copied if copied[cid][1] == observed[cid])
    print("counter-instrument (expectations copied from the harness's --json; no derivation)")
    print(f"  rows harvested from leak: {len(copied)}  harness exit(leak)={code0} exit(observe)={code1}")
    print(f"  mode-semantics agreement: {len(rows) - len(bad)}/{len(rows)}   exact-value matches: {exact}/{len(copied)}")
    print(f"  disagreements: {bad if bad else 'none'}")
    print("  forbidden artifacts opened: none (no baseline.json, no harness source, no corpus doc)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))