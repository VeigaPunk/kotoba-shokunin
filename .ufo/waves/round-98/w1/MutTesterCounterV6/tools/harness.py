#!/usr/bin/env python3
"""MutTesterCounterV6 harness: the committed C2 runner's own measure step, on the slim substrate.

Usage: python3 -B harness.py <counter.py> <label> [--c2] [--tables] [--probe <name>]
Prints one line per measurement and a final JSON summary on the last line.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r98/MutTesterCounterV6")
SLIM = S / "slim"
WORLDS = S / "worlds"
SEED = "deadbeefdeadbeef"
FORGERIES = [("g3-recompile-compare", None), ("g7-stateful-fake", None), ("g8-clone-marker", None),
             ("g10-head-compare", None), ("g11-schedule-reader", SEED)]
BOUND = "g2b-guard-aware-sniff"


def revs(path: Path) -> dict:
    out = {}
    for ln in path.read_text().splitlines():
        p = ln.split()
        if len(p) >= 2:
            out[p[0]] = p[1]
    return out


WREV = revs(S / "logs" / "world-revs.txt")
SREV = revs(S / "logs" / "slim-revs.txt")


def measure(counter: Path, label: str, table: str, wrev: str, repo: Path, seed: str | None,
            extra: list[str]) -> dict:
    env = {k: v for k, v in os.environ.items() if k != "KOTOBA_R97_SEED"}
    env["HYAKU_SCRATCH"] = str(S / "hs" / label.replace("/", "_"))
    if seed:
        env["KOTOBA_R97_SEED"] = seed
    p = subprocess.run([sys.executable, "-B", str(counter), table, wrev, str(repo), *extra],
                       env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=3600)
    out = p.stdout.decode("utf-8", "replace").splitlines()
    tally = next((ln for ln in reversed(out) if " targets killed " in ln), "<no tally>")
    pred = next((ln for ln in reversed(out) if "-PREDICATE-" in ln or "-NOT-EVALUATED" in ln), "<no predicate>")
    rules = next((ln for ln in reversed(out) if ln.startswith("rules ")), "")
    raw = S / "logs" / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    (raw / (counter.stem + "__" + label.replace(" ", "_") + ".txt")).write_text("\n".join(out) + "\n")
    print("%s%s rc %d %s | %s" % (label, " seed " + seed if seed else "", p.returncode, pred, tally))
    if rules:
        print("   %s" % rules)
    return {"label": label, "rc": p.returncode, "pred": pred, "tally": tally, "rules": rules,
            "met": p.returncode == 0 and pred.endswith("-PREDICATE-MET"), "out": out}


def main(argv: list[str]) -> int:
    counter = Path(argv[0]).resolve()
    label = argv[1]
    rest = argv[2:]
    do_c2 = "--c2" in rest or not rest
    do_tables = "--tables" in rest or not rest
    probe = None
    if "--probe" in rest:
        probe = rest[rest.index("--probe") + 1]
    extra: list[str] = []
    if "--rules" in rest:
        extra = ["--rules", rest[rest.index("--rules") + 1]]
    res: dict = {"counter": str(counter), "label": label, "sha256": subprocess.run(
        ["sha256sum", str(counter)], stdout=subprocess.PIPE).stdout.decode().split()[0]}
    if do_c2:
        refused = held = 0
        for world, seed in FORGERIES:
            m = measure(counter, "forgery " + world, "r96c1", WREV[world], WORLDS, seed, extra)
            res[world] = m
            refused += not m["met"]
        m = measure(counter, "bound " + BOUND, "r96c1", WREV[BOUND], WORLDS, None, extra)
        res[BOUND] = m
        m = measure(counter, "honest h1-r96-landing", "r96c1", WREV["h1"], WORLDS, None, extra)
        res["h1"] = m
        held += m["met"]
        m = measure(counter, "honest h2-r95c1", "r95c1", SREV[label], SLIM, None, extra)
        res["h2"] = m
        held += m["met"]
        print("C2 %s: forgeries refused %d of 5; honest held %d of 2" % (label, refused, held))
        res["c2_refused"] = refused
        res["c2_held"] = held
        res["c2_met"] = refused == 5 and held == 2
    if do_tables:
        for table in ("c1", "r97c1", "r96c1", "r95c1"):
            m = measure(counter, "table " + table, table, SREV[label], SLIM, None, extra)
            res["table_" + table] = m
    if probe:
        m = measure(counter, "probe " + probe, probe, SREV[label], SLIM, None, extra)
        res["probe"] = m
    print("JSON " + json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items() if kk != "out"})
                                for k, v in res.items()}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
