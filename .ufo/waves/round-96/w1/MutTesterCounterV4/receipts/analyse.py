#!/usr/bin/env python3
"""Compare every mutant counter's reading against the pristine reading of the same world."""
from __future__ import annotations

import json
import re
from pathlib import Path

S = Path(__file__).resolve().parent
COMMITTED = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-96/receipts")
WORLD_RECEIPT = {
    "base": "redbefore-c1-base.txt",
    "f1-text-sniff": "forgery-f1-text-sniff.txt",
    "f2-crash-signal": "forgery-f2-crash-signal.txt",
    "f3-summary-no-line": "forgery-f3-summary-no-line.txt",
    "f4-honest-trip": "forgery-f4-honest-trip.txt",
    "f5-label-only": "forgery-f5-label-only.txt",
    "r95c1__base": "poscontrol-r95c1-base.txt",
}


def reading(text: str) -> tuple[str, str]:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    summary = next((ln for ln in reversed(lines) if " targets killed " in ln), "<no summary>")
    verdict = next((ln for ln in reversed(lines) if "-PREDICATE-" in ln or "-NOT-EVALUATED" in ln), "<no verdict>")
    return summary, verdict


def committed_reading(name: str) -> tuple[str, str]:
    return reading((COMMITTED / WORLD_RECEIPT[name]).read_text(encoding="utf-8"))


def main() -> int:
    results = json.loads((S / "matrix.json").read_text(encoding="utf-8"))
    rows = {}
    for r in results:
        counter, claim, world = r["tag"].split("__")
        rows[(counter, claim, world)] = r
    worlds = ["base", "f1-text-sniff", "f2-crash-signal", "f3-summary-no-line",
              "f4-honest-trip", "f5-label-only"]
    counters = sorted({c for c, _, _ in rows}, key=lambda c: (c != "pristine", c))
    out = []
    deviations = {}
    for world in worlds:
        prist = rows[("pristine", "c1", world)]
        psum, pver = reading(Path(prist["out"]).read_text(encoding="utf-8"))
        csum, cver = committed_reading(world)
        same_committed = (psum == csum and pver == cver)
        out.append("### world %s\n" % world)
        out.append("pristine: %s | %s (rc %d) — committed receipt match: %s\n"
                   % (pver, psum, prist["rc"], "YES" if same_committed else "NO"))
        if not same_committed:
            out.append("  committed: %s | %s\n" % (cver, csum))
        for c in counters:
            if c == "pristine":
                continue
            r = rows[(c, "c1", world)]
            sum_, ver = reading(Path(r["out"]).read_text(encoding="utf-8"))
            if (sum_, ver) == (psum, pver):
                kind = "INERT"
            elif ver != pver:
                kind = "VERDICT-FLIP %s -> %s" % (pver, ver)
            else:
                kind = "TALLY-DEVIATION"
            deviations.setdefault(c, []).append((world, kind, ver, sum_, r["rc"]))
            out.append("  %-34s %-22s rc %d | %s | %s\n" % (c, kind, r["rc"], ver, sum_))
        out.append("\n")
    # r95c1
    prist = rows[("pristine", "r95c1", "base")]
    psum, pver = reading(Path(prist["out"]).read_text(encoding="utf-8"))
    csum, cver = committed_reading("r95c1__base")
    out.append("### world r95c1-base (positive control)\n")
    out.append("pristine: %s | %s (rc %d) — committed receipt match: %s\n"
               % (pver, psum, prist["rc"], "YES" if (psum, pver) == (csum, cver) else "NO"))
    for c in counters:
        if c == "pristine":
            continue
        r = rows[(c, "r95c1", "base")]
        sum_, ver = reading(Path(r["out"]).read_text(encoding="utf-8"))
        kind = "INERT" if (sum_, ver) == (psum, pver) else (
            "VERDICT-FLIP %s -> %s" % (pver, ver) if ver != pver else "TALLY-DEVIATION")
        deviations.setdefault(c, []).append(("r95c1-base", kind, ver, sum_, r["rc"]))
        out.append("  %-34s %-22s rc %d | %s | %s\n" % (c, kind, r["rc"], ver, sum_))
    out.append("\n## summary\n")
    for c in counters:
        if c == "pristine":
            continue
        exposed = [(w, k) for w, k, *_ in deviations.get(c, []) if k != "INERT"]
        out.append("%-34s exposed by %d context(s): %s\n"
                   % (c, len(exposed), ", ".join("%s[%s]" % (w, k.split()[0]) for w, k in exposed) or "NONE"))
    (S / "analysis.md").write_text("".join(out), encoding="utf-8")
    print("".join(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
