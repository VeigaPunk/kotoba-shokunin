#!/usr/bin/env python3
"""Summarise the matrix logs into the exposure table.

Usage: python3 -B summarize.py
"""
import json
import re
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r98/MutTesterCounterV6")
BASE = S / "logs" / "matrix" / "BASE.txt"


def parse(path: Path) -> dict:
    out = {"measure": {}}
    if not path.is_file():
        return out
    for ln in path.read_text().splitlines():
        m = re.match(r"^(forgery|bound|honest|table|probe) (\S+)(?: seed (\S+))? rc (\d+) (\S+) \| (.*)$", ln)
        if m:
            kind, name, seed, rc, pred, tally = m.groups()
            out["measure"][(kind, name)] = {"rc": int(rc), "pred": pred, "tally": tally}
            continue
        m = re.match(r"^C2 (\S+): forgeries refused (\d+) of 5; honest held (\d+) of 2$", ln)
        if m:
            out["c2"] = (int(m.group(2)), int(m.group(3)))
    return out


def short(tally: str) -> str:
    """killed K of N; honest H; comment C; code X  (+ positive)."""
    m = re.search(r"targets killed (\d+) of (\d+)(?: \(run errors (\d+)\))?; positive killed (\d+) of 1; "
                  r"honest (\S+); comment decoys held (\d+) of (\d+); code decoys held (\d+) of (\d+)", tally)
    if not m:
        return tally[:60]
    return "k%s/%s e%s p%s H:%s c%s/%s x%s/%s" % m.groups()


def main() -> int:
    base = parse(BASE)
    files = sorted((S / "logs" / "matrix").glob("*.txt"))
    order = ["W1-rule8-off", "W2-rule9-env-inherited", "W3-nondumpable-removed", "W4-rule10-removed",
             "W5-seed-in-child-env", "W6-hardlink-pristine", "V4-home-xdg-not-reset", "V5-no-shuffle",
             "V6-honest-any", "V7-unicode-uncaught", "V8-mirror-original", "V9-decoy-runerror-held"]
    byname = {f.stem: f for f in files}
    print("BASE C2:", base.get("c2"), "| tables:",
          {k[1]: v["pred"] for k, v in base["measure"].items() if k[0] == "table"})
    print()
    hdr = "%-26s %-11s %-7s %-7s %-7s %-7s %-7s %-6s %-6s" % (
        "mutant", "C2", "g3", "g7", "g8", "g10", "g11", "h1", "h2")
    print(hdr)
    rows = []
    for name in order:
        p = byname.get(name)
        if p is None:
            print("%-26s MISSING" % name)
            continue
        d = parse(p)
        cells = []
        for w in ("g3-recompile-compare", "g7-stateful-fake", "g8-clone-marker",
                  "g10-head-compare", "g11-schedule-reader"):
            m = d["measure"].get(("forgery", w))
            cells.append("MET" if m and m["pred"].endswith("-MET") else ("UNMET" if m else "?"))
        h1 = d["measure"].get(("honest", "h1-r96-landing"))
        h2 = d["measure"].get(("honest", "h2-r95c1"))
        c2 = d.get("c2")
        print("%-26s %-11s %-7s %-7s %-7s %-7s %-7s %-6s %-6s" % (
            name, ("%d/5 %d/2" % c2) if c2 else "?", *cells,
            "MET" if h1 and h1["pred"].endswith("-MET") else "UNMET",
            "MET" if h2 and h2["pred"].endswith("-MET") else "UNMET"))
        rows.append((name, d))
    print()
    print("TALLIES (vs BASE) — only lines that differ from BASE")
    for name, d in rows:
        diffs = []
        for k, v in d["measure"].items():
            b = base["measure"].get(k)
            if b is None:
                diffs.append("%s %s: NEW %s" % (k[0], k[1], short(v["tally"])))
            elif (b["pred"], short(b["tally"])) != (v["pred"], short(v["tally"])):
                diffs.append("%s %s: %s -> %s [%s -> %s]" % (
                    k[0], k[1], short(b["tally"]), short(v["tally"]), b["pred"], v["pred"]))
        print("- %s" % name)
        for x in diffs:
            print("    %s" % x)
        if not diffs:
            print("    (identical to BASE on every committed control)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
