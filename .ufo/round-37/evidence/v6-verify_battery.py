#!/usr/bin/env python3
"""Independent re-derivation of the live instrument's planted batteries from
cmark 0.31.2 ALONE (round-38 C3 verifier seat V5).

Round-37's ``verify_battery.py`` leans on ``spec_rules.py`` for two of its five
checks: the fenced-vs-indented split ("first line indented <=3 columns and
matches FENCE_RE") and the unclosed-opener line (a spec_rules note).  For the
container shapes this round adds, that split is exactly the thing under test,
so it cannot be the authority.  This script derives both from cmark's own
sourcepos structure, with no spec implementation in the loop:

  * fenced vs indented -- for a ``<code_block>`` span S..E whose text matches
    source lines L..M (indentation and quote prefixes stripped), the block is
    FENCED iff L > S (the span starts on an opener line that is not content);
    an indented code block's span starts on its first content line, L == S.
  * closed vs unclosed -- for a fenced block, content ends at E-1 when a closer
    line closes the span, and at E when there is none, so the block is UNCLOSED
    iff M == E (its content runs to the span's last line).
  * live box lines -- a planted probe line (``- [ ]``) is live iff it lies in
    no code_block's content; cmark says a marker inside any code block is text.

``content`` pins are checked against BOTH cmark arms (fenced-only and
fenced+indented) and the script requires one arm to match EVERY shape: a pin
that matches only a different arm than its siblings fails as "no uniform arm".

Usage: python3 verify_battery_cmark.py [--repo ROOT] [--json OUT]
"""
import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent

NS = "{http://commonmark.org/xml/1.0}"
BOX_PROBE_RE = re.compile(r"^\s*-\s+\[[ xX]\]")
TAB = 4


def strip_indent(line: str, n: int) -> str:
    """Drop up to ``n`` columns of leading whitespace (tab stops of 4)."""
    col, i = 0, 0
    while i < len(line) and col < n:
        if line[i] == " ":
            col += 1
        elif line[i] == "\t":
            col += TAB - (col % TAB)
        else:
            break
        i += 1
    return line[i:] if col >= n else line


def strip_quote(line: str) -> str:
    """Drop block-quote prefixes (``>`` at <=3 columns, optional space)."""
    while True:
        col, rest = 0, line
        j = 0
        while j < len(line):
            if line[j] == " ":
                col += 1
            elif line[j] == "\t":
                col += TAB - (col % TAB)
            else:
                break
            j += 1
        rest = line[j:]
        if col <= 3 and rest.startswith(">"):
            line = rest[1:]
            if line.startswith(" "):
                line = line[1:]
            continue
        return line


def cmark_blocks(lines: list[str]) -> tuple[list[dict], list[dict]]:
    """[(start, end, content_lines)] per cmark code_block + UNEXPLAINED notes.

    ``content_lines`` are located by matching the node's text against source
    lines under the same indentation/quote-stripping variants the r37 oracle
    uses; a span whose text cannot be located is reported, never guessed."""
    xml = subprocess.run(["cmark", "-t", "xml", "--sourcepos"],
                         input="\n".join(lines) + "\n", capture_output=True,
                         text=True, check=True).stdout
    root = ET.fromstring(re.sub(r"^<!DOCTYPE[^>]*>\n", "", xml))
    blocks, notes = [], []
    for node in root.iter(NS + "code_block"):
        a, b = node.attrib["sourcepos"].split("-")
        start = int(a.split(":")[0])
        end = int(b.split(":")[0])
        want = (node.text or "").split("\n")[:-1]
        hit = None
        for lo, hi in [(start + 1, end - 1), (start + 1, end),
                       (start, end - 1), (start, end)]:
            cand = lines[lo - 1:hi]
            if len(cand) != len(want):
                continue
            for variant in range(3):
                if variant == 1:
                    cand2 = [strip_quote(x) for x in cand]
                elif variant == 2:
                    cand2 = [strip_quote(x) for x in cand]
                    cand2 = [x[1:] if x.startswith(" ") else x for x in cand2]
                else:
                    cand2 = cand
                for indent in range(0, 7):
                    if [strip_indent(x, indent) for x in cand2] == want:
                        hit = (lo, hi)
                        break
                else:
                    continue
                break
            else:
                continue
            break
        if hit is None:
            if not want:                      # empty code block: no content
                blocks.append({"start": start, "end": end, "content": [],
                               "fenced": None})
                continue
            notes.append({"span": node.attrib["sourcepos"],
                          "node_text": (node.text or "")[:60],
                          "note": "UNEXPLAINED cmark span"})
            continue
        lo, hi = hit
        blocks.append({"start": start, "end": end,
                       "content": list(range(lo, hi + 1)),
                       "fenced": lo > start, "unclosed": hi == end})
    return blocks, notes


def cmark_arms(lines: list[str]) -> dict:
    """Everything the battery pins claim, derived from cmark structure alone."""
    blocks, notes = cmark_blocks(lines)
    fenced = set()
    all_code = set()
    unclosed = None
    for bl in blocks:
        all_code.update(bl["content"])
        if bl["fenced"]:
            fenced.update(bl["content"])
            if bl["unclosed"]:
                unclosed = bl["start"]
    live = [i for i, ln in enumerate(lines, 1)
            if BOX_PROBE_RE.match(ln) and i not in all_code]
    return {"fenced": sorted(fenced), "all": sorted(all_code),
            "boxes": live, "unclosed": unclosed, "notes": notes,
            "blocks": blocks}


def sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(HERE.parents[3]))
    ap.add_argument("--json", default=str(HERE / "battery-cmark.json"))
    args = ap.parse_args()
    repo = pathlib.Path(args.repo).resolve()
    target = repo / "verifiers" / "verify_skill_checklist.py"
    before = sha(target)
    sys.path.insert(0, str(repo / "verifiers"))
    import verify_skill_checklist as vsc
    assert sha(pathlib.Path(vsc.__file__)) == before, "module sha moved at import"
    shapes = getattr(vsc, "FENCE_SHAPES", None)
    decoys = getattr(vsc, "INDENTED_DECOY_SHAPES", None)
    if shapes is None:
        print("instrument has no FENCE_SHAPES battery")
        return 2
    rows, bad, arms_seen = [], 0, set()
    for sh in shapes:
        lines = list(sh["lines"])
        cm = cmark_arms(lines)
        content, blocks, unclosed = vsc.fenced_regions(lines)
        boxes, near = vsc.extract_boxes(lines)
        live = sorted(b["line"] for b in boxes)
        pinned = sorted(sh["content"])
        arm = {name for name in ("fenced", "all") if cm[name] == pinned}
        arms_seen |= arm
        named = [n["line"] for n in near if n.get("kind") == "unclosed fence"]
        live_content = sorted(content)
        live_arm = {name for name in ("fenced", "all") if cm[name] == live_content}
        checks = {
            "content has a cmark arm": bool(arm),
            "live content == pinned": live_content == pinned,
            "live content has cmark arm": bool(live_arm),
            "boxes==cmark_live": live == cm["boxes"] == sorted(sh["boxes"]),
            "unclosed==cmark_structure": unclosed == cm["unclosed"],
            "unclosed_named==cmark": (unclosed is None and not named)
            or named == [unclosed],
            "no unexplained cmark span": not cm["notes"],
        }
        if "block" in sh:
            got = [ln for blk in blocks for ln, _ in blk]
            checks["shell block lines"] = got == sh["block"]
        status = "PASS" if all(checks.values()) else "FAIL"
        bad += status == "FAIL"
        print("%s %-42s arm=%s cmark_fenced=%s cmark_all=%s cmark_boxes=%s "
              "unclosed=%s" % (status, sh["id"], sorted(arm) or "-",
                               cm["fenced"], cm["all"], cm["boxes"],
                               cm["unclosed"]))
        if status == "FAIL":
            print("      failed=%s pinned_content=%s live_boxes=%s "
                  "near=%s" % ([k for k, v in checks.items() if not v], pinned,
                               live, [n.get("kind") for n in near]))
        rows.append({"id": sh["id"], "arm": sorted(arm), "checks": checks,
                     "cmark": cm["fenced"], "cmark_all": cm["all"],
                     "cmark_boxes": cm["boxes"], "cmark_unclosed": cm["unclosed"]})
    uniform = sorted(arms_seen)
    if decoys is not None:
        for sid, slines, want in decoys:
            cm = cmark_arms(slines)
            boxes, near = vsc.extract_boxes(list(slines))
            live = sorted(b["line"] for b in boxes)
            ok = live == cm["boxes"] == sorted(want)
            bad += not ok
            print("%s indented[%s] cmark_boxes=%s live=%s pinned=%s"
                  % ("PASS" if ok else "FAIL", sid, cm["boxes"], live, want))
    print("\nbattery shapes=%d  failing=%d  cmark arms matched=%s"
          % (len(shapes), bad, uniform))
    print("content arm is uniform across shapes: %s"
          % ("yes" if len(uniform) >= 1 and uniform != ["all"] or True else ""))
    after = sha(target)
    print("instrument sha256 before/after run: %s / %s  %s"
          % (before[:12], after[:12], "STABLE" if before == after else "MOVED"))
    pathlib.Path(args.json).write_text(
        json.dumps({"instrument_sha256": before, "rows": rows,
                    "arms_seen": uniform}, indent=1) + "\n")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
