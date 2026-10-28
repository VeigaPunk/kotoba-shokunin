#!/usr/bin/env python3
"""C2 source-stability recheck for S226..S231 — round 80 w1, seat Kb80N01Sentinel.

WHY THIS EXISTS
  The r79 entry skeleton's `recheck:` line and any future recheck cell must ask
  "is the quoted text still on the page?", not "are the live bytes identical?".
  Byte equality is the wrong question for two measured reasons:
    * S229 (learn.microsoft.com) rewrites its static-asset build stamp and its
      Akamai bot-manager id on every site deploy — infra token rotation with
      content unchanged (measured 2026-10-27, 22 bytes / 4 sites).
    * The negative-sweep pages amp/codex/vscode rotate a CSP nonce / Vercel
      deployment id / A-B experiment id per request or per edge.
  A digest-equality recheck on those pages is red most of the time while nothing
  the rows quote has changed.

WHAT IT ASSERTS
  Per page: STABLE      = live bytes equal the committed snapshot pin.
            VARIED(class)= live bytes differ, but after normalising ONLY that
                           page's declared volatile token class the bytes are
                           equal -> known infrastructure class, content unchanged.
            VARIED(content) = live bytes differ and do not normalise back.
                              This is the only FAILING state.

  Normalisation is deliberately per-page and narrow. A page with no declared
  class gets none: any byte change on S226/S227/S228/S230/S231 is a content
  verdict, not a class. Widening a class to make a page pass would be
  laundering, which is the defect this tool exists to avoid.

USAGE
  recheck-c2-stability.py                     # fetch live and compare
  recheck-c2-stability.py --selftest          # prove the failing state is reachable
  recheck-c2-stability.py --snapdir DIR       # compare against another snapshot set

EXIT
  0  every page STABLE or VARIED(known class)
  3  at least one VARIED(content)  -- a real change; re-open the row
  2  environment error (missing pin, curl failure, no snapshot)
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# id -> (url, snapshot basename, volatile-class name or None)
PAGES = {
    "S226": ("https://agentskills.io/specification.md", "S226-spec.md", None),
    "S227": ("https://code.claude.com/docs/en/skills.md", "S227-claude.md", None),
    "S228": ("https://docs.factory.ai/cli/configuration/skills.md", "S228-factory.md", None),
    "S229": ("https://learn.microsoft.com/en-us/agent-framework/agents/skills",
             "S229-msaf.html", "msft-asset-stamp+akam"),
    "S230": ("https://raw.githubusercontent.com/badlogic/pi-mono/main/"
             "packages/coding-agent/docs/skills.md", "S230-pi.md", None),
    "S231": ("https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md",
             "S231-vibe.md", None),
}

# Declared volatile classes. Exactly the tokens measured in round 80; nothing more.
CLASSES = {
    "msft-asset-stamp+akam": (
        (rb"0\.4\.0\d+\.\d+-[0-9a-f]{8}", b"<BUILDSTAMP>"),
        (rb"akam/13/[0-9a-f]+", b"akam/13/<AKAM>"),
        (rb"pixel_[0-9a-f]+", b"pixel_<AKAM>"),
    ),
}


def normalize(raw: bytes, cls: str | None) -> bytes:
    if cls is None:
        return raw
    for pat, repl in CLASSES[cls]:
        raw = re.sub(pat, repl, raw)
    return raw


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def fetch(url: str, dest: Path) -> tuple[int, int, str]:
    proc = subprocess.run(
        ["curl", "-sSL", "-A", "Mozilla/5.0", "--max-time", "90",
         "-o", str(dest), "-w", "%{http_code}", url],
        capture_output=True, text=True)
    if proc.returncode != 0:
        return proc.returncode, -1, (proc.stderr or "").strip()
    return 0, int((proc.stdout or "0").strip() or 0), ""


def compare(snapdir: Path, workdir: Path, quiet: bool = False):
    rows, fails, missing = [], [], []
    for sid, (url, snapname, cls) in PAGES.items():
        snap = snapdir / snapname
        man = snapdir / f"{sid}.manifest"
        if not snap.is_file():
            raise SystemExit(f"environment error: snapshot {snap} is absent")
        if not man.is_file():
            raise SystemExit(f"environment error: pin {man} is absent")
        pin = man.read_text().split()[0]
        sb = snap.read_bytes()
        if sha(sb) != pin:
            raise SystemExit(f"environment error: {snap} does not match its pin {pin}")
        live = workdir / f"{sid}.live"
        rc, code, err = fetch(url, live)
        if rc != 0:
            raise SystemExit(f"environment error: curl failed for {sid} "
                             f"(rc={rc}): {err}")
        if code != 200:
            raise SystemExit(f"environment error: {sid} HTTP {code}")
        lb = live.read_bytes()
        if lb == sb:
            rows.append((sid, "STABLE", len(lb), sha(lb)[:8], "-"))
            continue
        if normalize(lb, cls) == normalize(sb, cls):
            rows.append((sid, "VARIED", len(lb), sha(lb)[:8], cls))
        else:
            rows.append((sid, "VARIED", len(lb), sha(lb)[:8], "CONTENT DIFFERS"))
            fails.append(sid)
    if not quiet:
        print(f"{'id':5} {'verdict':8} {'bytes':>8} {'live sha':10} class")
        for r in rows:
            print(f"{r[0]:5} {r[1]:8} {r[2]:>8} {r[3]:10} {r[4]}")
        g = sum(1 for r in rows if r[1] == "STABLE")
        known = sum(1 for r in rows
                    if r[1] == "VARIED" and r[4] != "CONTENT DIFFERS")
        print(f"\nC2 stability: {g} stable, {known} varied (known class), "
              f"{len(fails)} content change(s)")
    return fails


def selftest() -> int:
    """Prove VARIED(content) is reachable: flip one content byte in a copy."""
    snapdir = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/"
                   ".ufo/waves/round-79/snapshots")
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        for sid, (_u, snapname, _c) in PAGES.items():
            (tdp / snapname).write_bytes((snapdir / snapname).read_bytes())
            (tdp / f"{sid}.manifest").write_text(
                (snapdir / f"{sid}.manifest").read_text())
        # mutate the CONTENT region of S229 (well past the head's token sites),
        # and rebuild its pin so the failure is attribution, not a pin mismatch
        target = tdp / "S229-msaf.html"
        b = bytearray(target.read_bytes())
        b[90000] ^= 0x01
        target.write_bytes(bytes(b))
        (tdp / "S229.manifest").write_text(
            f"{sha(bytes(b))}  S229-msaf.html\n")
        print("selftest: one content byte flipped at offset 90000 of S229")
        print("selftest: expecting S229 VISIBLE as CONTENT DIFFERS")
        work = tdp / "work"
        work.mkdir()
        fails = compare(tdp, work, quiet=False)
        ok = fails == ["S229"]
        print(f"selftest {'PASS' if ok else 'FAIL'}: the content-change state is "
              f"{'reachable, so a real run would exit 3' if ok else 'NOT reachable — the tool cannot fail'}; "
              f"this selftest itself exits {0 if ok else 1}")
        return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapdir", type=Path,
                    default=Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/"
                                 ".ufo/waves/round-79/snapshots"))
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    with tempfile.TemporaryDirectory() as td:
        fails = compare(a.snapdir, Path(td))
    return 3 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
