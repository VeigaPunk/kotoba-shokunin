#!/usr/bin/env python3
"""record_measured.py -- write expected.json from the counter logs.

Reads `logs/<world>.log` (written by score_worlds.sh) for every `world-*` and
`diag-*` bundle, extracts the verdict line and the per-lane FAIL reasons, and
writes `expected.json`, which build_worlds.py folds into each world's README.
Mode is `measured` when the log came from the round-74 counter; a log from
`--emulate` is labelled `emulated`.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REASONS = {"measured": "measured (check_sibling_reread.py)", "emulated": "emulated"}


def main():
    out = {}
    for log in sorted((HERE / "logs").glob("*.log")):
        name = log.stem
        text = log.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"sibling rows re-pinned and re-read (\d+) of (\d+)", text)
        if not m:
            print("no verdict line in", log, file=sys.stderr)
            continue
        mode = "measured" if re.search(r"^repo .* base ", text, re.M) else "emulated"
        lanes = {}
        for line in text.splitlines():
            lm = re.match(r"^lane ([a-z0-9-]+): (ok|FAIL ?(.*))$", line)
            if not lm:
                continue
            lane, verdict, reason = lm.group(1), lm.group(2), lm.group(3) or ""
            lanes[lane] = [] if verdict == "ok" else [reason]
        out[name] = {"score": int(m.group(1)), "of": int(m.group(2)),
                     "mode": REASONS[mode], "lanes": lanes}
    (HERE / "expected.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n",
                                        encoding="utf-8")
    for name in sorted(out):
        print("%-30s %2d of %d  %s" % (name, out[name]["score"], out[name]["of"],
                                       out[name]["mode"]))


if __name__ == "__main__":
    main()
