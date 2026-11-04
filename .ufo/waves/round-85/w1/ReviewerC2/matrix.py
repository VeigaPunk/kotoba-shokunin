#!/usr/bin/env python3
"""ReviewerC2 control matrix: score every control world against two verifier
revisions of verifiers/check_substrate_pins.py.

V0 = git show HEAD:verifiers/check_substrate_pins.py (frozen: default omp path
     is ~/.local/bin/omp.real, which does not exist on this host)
V1 = working-tree verifiers/check_substrate_pins.py (ExecC2Pin's constant fix)

Every world is a JSON baseline written under this scratch dir. `--baseline` is
the only flag passed, exactly as the seat item specifies.
"""
import json
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
HERE = Path(__file__).resolve().parent
V0 = HERE / "v0" / "check_substrate_pins.py"
V1 = LANE / "verifiers" / "check_substrate_pins.py"
WORLDS = HERE / "worlds"
WORLDS.mkdir(exist_ok=True)

OC_SHA = "ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7"
TRUE_SHA = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"
TRUE_MTIME = "2026-11-01T17:11:07.281808804-03:00"
OLD_OMP_SHA = "85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4"
OLD_OMP_MTIME = "2026-10-21T20:37:24.615549837-03:00"


def blk(**pins):
    ma = {"omp_binary_sha256": TRUE_SHA, "omp_binary_mtime": TRUE_MTIME,
          "opencode_binary_sha256": OC_SHA}
    for k, v in pins.items():
        if v is ...:
            ma.pop(k, None)
        else:
            ma[k] = v
    return {"measured_against": ma}


W = [
    ("W0 truthful baseline (host values re-derived by ReviewerC2)", blk()),
    ("W1 committed baseline as at HEAD (18.12.6 pins)", {
        "measured_against": {"omp_binary_sha256": OLD_OMP_SHA,
                             "omp_binary_mtime": OLD_OMP_MTIME,
                             "opencode_binary_sha256": OC_SHA}}),
    ("W2 opencode sha under omp_binary_sha256", blk(omp_binary_sha256=OC_SHA)),
    ("W3 both omp pins deleted", blk(omp_binary_sha256=..., omp_binary_mtime=...)),
    ("W4 only omp_binary_mtime deleted", blk(omp_binary_mtime=...)),
    ("W5 unregistered substrate pin (cursor)", blk(cursor_binary_sha256="0" * 64)),
    ("W6 pin value not a string (epoch int)", blk(omp_binary_mtime=1793563867)),
    ("W7 mtime with 10 fractional digits",
     blk(omp_binary_mtime="2026-11-01T17:11:07.2818088040-03:00")),
    ("W8 mtime naive (no UTC offset)", blk(omp_binary_mtime="2026-11-01T17:11:07.281808804")),
    ("W9 mtime coarse: seconds only, correct second",
     blk(omp_binary_mtime="2026-11-01T17:11:07-03:00")),
    ("W10 mtime coarse: seconds only, WRONG second (+1s)",
     blk(omp_binary_mtime="2026-11-01T17:11:08-03:00")),
    ("W11 mtime ms precision (3 digits)",
     blk(omp_binary_mtime="2026-11-01T17:11:07.281-03:00")),
    ("W12 mtime space-separated (GNU stat %y form)",
     blk(omp_binary_mtime="2026-11-01 17:11:07.281808804 -0300")),
    ("W13 mtime ns-exact, off by 1 ns",
     blk(omp_binary_mtime="2026-11-01T17:11:07.281808805-03:00")),
    ("W14 measured_against null (vacuity)", {"measured_against": None}),
    ("W15 measured_against empty object", {"measured_against": {}}),
    ("W16 omp pin zeroed (a different ELF's sha)",
     blk(omp_binary_sha256="0" * 64)),
]

VERIFIERS = [("V0 HEAD omp.real", V0), ("V1 tree omp", V1)]
rows = []
for vname, vpath in VERIFIERS:
    for i, (wname, payload) in enumerate(W):
        p = WORLDS / ("%s-%02d.json" % (vname.split()[0], i))
        p.write_text(json.dumps(payload, indent=2) + "\n")
        r = subprocess.run([sys.executable, "-B", str(vpath), "--baseline", str(p)],
                           capture_output=True, text=True, cwd=str(LANE))
        out = [ln for ln in r.stdout.splitlines() if ln.strip()]
        err = [ln for ln in r.stderr.splitlines() if ln.strip()]
        rows.append({"verifier": vname, "world": wname, "exit": r.returncode,
                     "summary": out[-1] if out else "",
                     "first_fail": next((ln for ln in out if ln.startswith("FAIL ")), ""),
                     "lines": out + ["E " + e for e in err]})

json.dump(rows, open(HERE / "matrix.json", "w"), indent=2)

print("| world | V0 exit | V0 line | V1 exit | V1 line |")
print("|---|---|---|---|---|")
for i, (wname, _) in enumerate(W):
    a = rows[i]
    b = rows[len(W) + i]
    print("| %s | %d | `%s` | %d | `%s` |"
          % (wname, a["exit"], a["summary"], b["exit"], b["summary"]))
for r in rows:
    print("\n=== %s :: %s -> exit %d" % (r["verifier"], r["world"], r["exit"]))
    for ln in r["lines"]:
        print("   ", ln)
