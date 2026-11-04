#!/usr/bin/env python3
"""ReviewerC2 control suite for verifiers/check_substrate_pins.py.

Builds control baselines in this scratch dir and scores each twice:
  A: --baseline <file> only (the item's literal command; default omp path is
     the still-missing ~/.local/bin/omp.real)
  B: --baseline <file> --omp-binary /home/vgpnk/.local/bin/omp (simulates the
     constant re-pin so the pin-document logic itself is exercised)

Read-only against the lane: only reads verifiers/ and stats the host binary.
"""
import json
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
VERIFIER = LANE / "verifiers" / "check_substrate_pins.py"
OMP = "/home/vgpnk/.local/bin/omp"
OC_SHA = "ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7"
TRUE_SHA = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"
TRUE_MTIME = "2026-11-01T17:11:07.281808804-03:00"
OUT = Path(__file__).resolve().parent / "controls"
OUT.mkdir(exist_ok=True)


def base(**pins):
    ma = {"omp_binary_sha256": TRUE_SHA, "omp_binary_mtime": TRUE_MTIME,
          "opencode_binary_sha256": OC_SHA}
    for k, v in pins.items():
        if v is ...:
            ma.pop(k, None)
        else:
            ma[k] = v
    return {"measured_against": ma}


def score(path, omp_binary=None):
    argv = [sys.executable, "-B", str(VERIFIER), "--baseline", str(path)]
    if omp_binary:
        argv += ["--omp-binary", omp_binary]
    p = subprocess.run(argv, capture_output=True, text=True, cwd=str(LANE))
    return p.returncode, p.stdout, p.stderr


CASES = [
    # name, payload-builder, omp-binary override
    ("01-correct-host-truth", lambda: base(), None),
    ("02-correct-host-truth", lambda: base(), OMP),
    ("03-wrong-sha-opencode-under-omp", lambda: base(omp_binary_sha256=OC_SHA), OMP),
    ("04-wrong-sha-opencode-under-omp", lambda: base(omp_binary_sha256=OC_SHA), None),
    ("05-omp-pins-deleted", lambda: base(omp_binary_sha256=..., omp_binary_mtime=...), OMP),
    ("06-omp-pins-deleted", lambda: base(omp_binary_sha256=..., omp_binary_mtime=...), None),
    ("07-wrong-path-nonexistent", lambda: base(), "/nonexistent/omp"),
    ("08-unregistered-substrate-pin", lambda: base(cursor_binary_sha256="0" * 64), OMP),
    ("09-different-elf-as-omp", lambda: base(omp_binary_sha256="0" * 64),
     "/home/vgpnk/.opencode/bin/opencode"),
    ("10-mtime-epoch-seconds-int", lambda: base(omp_binary_mtime=1793563867), OMP),
    ("11-mtime-10-fractional-digits",
     lambda: base(omp_binary_mtime="2026-11-01T17:11:07.2818088040-03:00"), OMP),
    ("12-mtime-naive-no-offset", lambda: base(omp_binary_mtime="2026-11-01T17:11:07.281808804"), OMP),
    ("13-mtime-space-separated", lambda: base(omp_binary_mtime="2026-11-01 17:11:07.281808804 -0300"), OMP),
    ("14-mtime-9-digit-utc-same-instant",
     lambda: base(omp_binary_mtime="2026-11-01T20:11:07.281808804+00:00"), OMP),
    ("15-mtime-microsecond-6-digit",
     lambda: base(omp_binary_mtime="2026-11-01T17:11:07.281808-03:00"), OMP),
    ("16-mtime-millisecond-3-digit",
     lambda: base(omp_binary_mtime="2026-11-01T17:11:07.281-03:00"), OMP),
    ("17-mtime-second-only-0-digit",
     lambda: base(omp_binary_mtime="2026-11-01T17:11:07-03:00"), OMP),
    ("18-mtime-second-only-wrong-second",
     lambda: base(omp_binary_mtime="2026-11-01T17:11:08-03:00"), OMP),
    ("19-mtime-9-digit-off-by-1ns",
     lambda: base(omp_binary_mtime="2026-11-01T17:11:07.281808805-03:00"), OMP),
    ("20-measured-against-null", lambda: {"measured_against": None}, OMP),
    ("21-baseline-not-object", lambda: [1, 2, 3], OMP),
    ("22-sha-uppercase-same-bytes", lambda: base(omp_binary_sha256=TRUE_SHA.upper()), OMP),
]

rows = []
for name, build, omp_bin in CASES:
    p = OUT / (name + ".json")
    p.write_text(json.dumps(build(), indent=2) + "\n")
    code, out, err = score(p, omp_bin)
    lines = [ln for ln in out.splitlines() if ln.strip()]
    tail = lines[-1] if lines else ""
    rows.append({"case": name, "omp_binary": omp_bin or "(default omp.real)",
                 "exit": code, "stdout": out, "stderr": err, "summary": tail})

json.dump(rows, open(OUT / "results.json", "w"), indent=2)
for r in rows:
    print("%-38s exit=%d  %s" % (r["case"], r["exit"], r["summary"]))
