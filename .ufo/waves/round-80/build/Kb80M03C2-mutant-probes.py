#!/usr/bin/env python3
"""Kb80M03C2 mutant probes (scratch tool)."""
import sys

sys.path.insert(0, "/fast/scratch/hyaku/kotoba-r80/Kb80M03C2")
import driver  # noqa: E402

S, REC = driver.S, driver.REC
MUT = S / "mutants"

worlds = {}
for line in (REC / "worlds.sha256").read_text().splitlines():
    sha, name = line.split()
    worlds[name] = sha

results = []


def probe(tag, counter, world, want_exit, want_sub=None, forbid=None):
    rc, out = driver.run_counter(tag, counter, worlds[world] if world in worlds else world)
    ok = rc == want_exit
    if want_sub is not None:
        ok = ok and want_sub in out
    if forbid is not None:
        ok = ok and forbid not in out
    results.append((tag, rc, ok))
    if forbid is not None:
        print(f"{tag}: exit={rc} forbid-present={forbid in out}")
    return out


M1 = MUT / "M1_exit_pred.py"
probe("R3-M1drift-W1", MUT / "M1drift_unfilled.py", "W1", 2, "counter drifted")
probe("R4-M1-W1", M1, "W1", 0)
probe("R5-M1-WH", M1, "WH", 0)
probe("R5b-M1-W5", M1, "W5", 0)
probe("R7-M3-W3", MUT / "M3_host_prefix.py", "W3", 0)
probe("R9-M4-W4", MUT / "M4_banner_quote.py", "W4", 0)
probe("R11-M5-W5", MUT / "M5_usedby.py", "W5", 0)
probe("R13-M6-W6", MUT / "M6_opened_date.py", "W6", 0)
out14 = probe("R14-M2-WH", MUT / "M2_genline.py", "WH", 0,
              forbid="generator world:")

print("--- verdicts (tag, exit, ok) ---")
bad = 0
for tag, rc, ok in results:
    print(("PASS " if ok else "FAIL ") + f"{tag}: exit={rc}")
    bad += 0 if ok else 1
print(f"mutant probes: {bad} unexpected result(s) over {len(results)}")
print("R14 stdout head:")
print("\n".join(out14.splitlines()[:8]))
sys.exit(1 if bad else 0)
