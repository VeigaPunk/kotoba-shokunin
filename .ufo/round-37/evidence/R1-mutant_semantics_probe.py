#!/usr/bin/env python3
"""R1 probe: which mutant semantics can the C1 move-text actually produce?

C1 move text: "re-derive the expected values ... directly from the live
substrates ..., then compare against live observed values".
C1 after-text: "exit 1 naming the mutant on a pinned mutant tree".

This probe shows the two are not the same operation. A live-deriving model is a
function f(state); the harness's observation is g(state). On any substrate
mutant both read the same state, so agreement is preserved and nothing flips:
the mutant can only be named by a model whose expectation was FROZEN before the
mutation. Reviewer probe (source-aware) — not a candidate blind instrument.

Usage: mutant_semantics_probe.py            # uses repo-local fixtures
"""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
HARNESS = REPO / "verifiers/verify_harness_claims.py"
MUTANT_LOG = HERE / "fixtures/oc-log-mutant.log"
CHECK = "oc.log.init_count_max"


def derive_init_count_max(log: pathlib.Path) -> int:
    """Independent derivation: max of `message=init count=N` over the log text."""
    text = log.read_text(errors="replace")
    counts = [int(n) for n in re.findall(r"message=init count=(\d+)", text)]
    return max(counts) if counts else 0


def harness_observed(*extra: str) -> int:
    proc = subprocess.run(
        [sys.executable, str(HARNESS), "--json", *extra],
        capture_output=True, text=True, cwd=REPO,
    )
    rows = json.loads(proc.stdout)["results"]
    return next(r["observed"] for r in rows if r["check"] == CHECK)


def main() -> int:
    landed = REPO.parent / ".."  # placeholder, replaced below by the real log
    real_log = pathlib.Path.home() / ".local/share/opencode/log/opencode.log"

    print(f"check under probe: {CHECK}")
    d_landed = derive_init_count_max(real_log)
    o_landed = harness_observed()
    print(f"  A landed      : derive={d_landed}  harness_observed={o_landed}  "
          f"agree={'yes' if d_landed == o_landed else 'no'}")

    d_mut = derive_init_count_max(MUTANT_LOG)
    o_mut = harness_observed("--oc-log", str(MUTANT_LOG))
    print(f"  B substrate-mutant: derive={d_mut}  harness_observed={o_mut}  "
          f"agree={'yes' if d_mut == o_mut else 'no'}   <- live re-derivation FOLLOWS the mutant")

    frozen, observed = d_landed, o_mut
    flips = frozen != observed
    print(f"  C frozen-vs-mutant: frozen_expect={frozen}  observed={observed}  "
          f"flip={'yes' if flips else 'no'}" + (f" names={CHECK}" if flips else ""))

    print("verdict: arm A/B = C1's move-text semantics (agreement, no flip, mutant unnamed);")
    print("         arm C    = the only semantics that can satisfy C1's after-text (frozen pins).")
    return 0


if __name__ == "__main__":
    sys.exit(main())