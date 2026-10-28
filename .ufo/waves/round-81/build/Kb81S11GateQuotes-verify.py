#!/usr/bin/env python3
"""Kb81S11GateQuotes — located-quote verification for round 81 w1.

Reads committed/lane bytes only (plus the r79 fetch records) and reports, for
every candidate quote, the occurrence count and location under three views:

  raw  — the snapshot bytes as stored (UTF-8 byte offset, 1-based line);
  view — the round-80 counter's declared Markdown text view, reproduced
         exactly (every backtick byte deleted, unordered-list marker removed by
         (?m)^[ \t]{0,3}[*+\-][ \t]+, per-line whitespace collapsed, empty
         lines dropped, fenced blocks kept);
  link — the same view after stripping ``[text](url)`` to ``text`` first (a
         view change that must be DECLARED before data; recorded so the
         dependency is visible, never used to claim the counter's view).

Also verifies the S250 binding bytes (hash -> mistralai/mistral-vibe), the
negative sweep over badlogic/pi-mono's advertised refs, and the S230 audit-row
quote in its pinned snapshot.

No writes outside the caller's stdout / the JSON path given on the command
line.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
S249 = LANE / ".ufo/waves/round-81/snapshots/S249.md"
S249_FETCH = LANE / ".ufo/waves/round-81/snapshots/S249.fetch.json"
S249_MANIFEST = LANE / ".ufo/waves/round-81/snapshots/S249.manifest"
S230_SNAP = LANE / ".ufo/waves/round-79/snapshots/S230-pi.md"
S231_FETCH = LANE / ".ufo/waves/round-79/snapshots/S231.fetch.json"
S230_FETCH = LANE / ".ufo/waves/round-79/snapshots/S230.fetch.json"
VIBE_LS = LANE / ".ufo/waves/round-81/snapshots/mistral-vibe-lsremote.txt"
PI_LS = LANE / ".ufo/waves/round-81/snapshots/pi-mono-lsremote.txt"
E03_MANIFEST = LANE / ".ufo/waves/round-81/build/Kb81E03ExtManifest.json"
R80_SAVED = LANE / ".ufo/waves/round-80/build/Kb80S05-agent-sdk-skills.md"
SOURCES = LANE / "corpus/SOURCES.md"

EXPECTED_SHA = "ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2"
LIST_MARKER_RE = re.compile(r"(?m)^[ \t]{0,3}[*+\-][ \t]+")
LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def ws(s: str) -> str:
    return " ".join(s.split())


def _fence_flags(raw_lines: list[str]) -> list[bool]:
    """True where a raw line is a fence marker or sits inside a fence (r80)."""
    flags: list[bool] = []
    in_fence = False
    for line in raw_lines:
        if line.strip().startswith("```"):
            flags.append(True)
            in_fence = not in_fence
            continue
        flags.append(in_fence)
    return flags


def view_lines(raw: str, strip_links: bool = False) -> tuple[list[str], set[int]]:
    lines: list[str] = []
    heads: set[int] = set()
    if strip_links:
        raw = LINK_RE.sub(r"\1", raw)
    fences = _fence_flags(raw.splitlines())
    raw = raw.replace("`", "")
    raw = LIST_MARKER_RE.sub("", raw)
    for i, line in enumerate(raw.splitlines()):
        s = ws(line)
        if not s:
            continue
        lines.append(s)
        if s.startswith("#") and not (i < len(fences) and fences[i]):
            heads.add(len(lines) - 1)
    return lines, heads


def locate(lines: list[str], quote: str) -> tuple[int, int] | tuple[None, None]:
    """Return (view line index, char index in the joined view) or (None, None)."""
    joined = " ".join(lines)
    pos = joined.find(quote)
    if pos < 0:
        return None, None
    off = 0
    for i, line in enumerate(lines):
        if off <= pos < off + len(line) + 1:
            return i, pos
        off += len(line) + 1
    return len(lines) - 1, pos


def raw_locate(raw: bytes, quote: str) -> tuple[int, int] | tuple[None, None]:
    b = quote.encode()
    pos = raw.find(b)
    if pos < 0:
        return None, None
    line = raw[:pos].count(b"\n") + 1
    return line, pos


def repeated(raw: bytes, quote: str) -> int:
    b = quote.encode()
    n = 0
    start = 0
    while True:
        i = raw.find(b, start)
        if i < 0:
            return n
        n += 1
        start = i + 1


def check_quote(raw: bytes, name: str, quote: str, strip_links: bool = False) -> dict:
    lines, heads = view_lines(raw.decode("utf-8"), strip_links)
    idx, pos = locate(lines, quote)
    first_head = min(heads) if heads else None
    q70 = None
    if idx is not None:
        q70 = not (idx == first_head or (first_head is not None and idx <= first_head + 1))
    return {
        "name": name,
        "words": len(quote.split()),
        "has_key_token": ("allowed-tools" in quote or "allowedTools" in quote),
        "raw_occurrences": repeated(raw, quote),
        "raw_line": raw_locate(raw, quote)[0],
        "raw_byte": raw_locate(raw, quote)[1],
        "view_occurrences_real": " ".join(lines).count(quote),
        "view_line_index0": idx,
        "view_char": pos,
        "first_heading_view_index": first_head,
        "q70_after_first_heading": q70,
        "view": "view+links" if strip_links else "view",
        "quote": quote,
    }


def main() -> int:
    raw = S249.read_bytes()
    out: dict = {
        "seat": "Kb81S11GateQuotes",
        "round": 81,
        "wave": "w1",
        "s249": {},
        "s250": {},
        "s230_audit": {},
    }
    out["s249"]["snapshot"] = str(S249)
    out["s249"]["bytes"] = len(raw)
    out["s249"]["sha256"] = hashlib.sha256(raw).hexdigest()
    out["s249"]["sha256_matches_expected"] = out["s249"]["sha256"] == EXPECTED_SHA
    out["s249"]["lines"] = raw.count(b"\n") + 1
    if S249_MANIFEST.exists():
        man = S249_MANIFEST.read_text().split()
        out["s249"]["manifest"] = S249_MANIFEST.read_text().strip()
        out["s249"]["manifest_matches"] = (len(man) >= 2 and man[0] == out["s249"]["sha256"])
    if S249_FETCH.exists():
        f = json.loads(S249_FETCH.read_text())
        out["s249"]["fetch_record"] = {k: f.get(k) for k in
                                       ("url", "http", "bytes", "sha256", "fetched_utc")}
        out["s249"]["fetch_record_matches"] = (
            f.get("sha256") == out["s249"]["sha256"] and f.get("bytes") == len(raw))
    if R80_SAVED.exists():
        rb = R80_SAVED.read_bytes()
        out["s249"]["r80_saved"] = {
            "path": str(R80_SAVED), "bytes": len(rb),
            "sha256": hashlib.sha256(rb).hexdigest(),
            "identical": rb == raw,
        }

    quotes = {
        "A_line348": ("In SDK sessions, you can pre-approve tools for a project or "
                      "personal skill with the skill's allowed-tools frontmatter or "
                      "with the allowedTools option"),
        "B_line389": "The list pre-approves the named tools rather than restricting the others.",
        "C_line350": ("The example below pre-approves Read, Grep, and Glob with "
                      "allowedTools (allowed_tools in Python)"),
        "D_fragment": ("the allowedTools option (allowed_tools in Python) in your "
                       "query configuration"),
    }
    out["s249"]["quotes"] = []
    for name, q in quotes.items():
        rec = check_quote(raw, name, q, strip_links=False)
        rec_link = check_quote(raw, name, q, strip_links=True)
        rec["under_link_stripped_view"] = {k: rec_link[k] for k in
                                           ("view_occurrences_real", "view_line_index0",
                                            "view_char", "q70_after_first_heading")}
        out["s249"]["quotes"].append(rec)

    # ---------------- S250 binding ----------------
    s231 = json.loads(S231_FETCH.read_text())
    s230 = json.loads(S230_FETCH.read_text())
    s250_quote = ("'main' resolved to commit 7bb48f213ac677f943d5c791199ed3dddf302f00 "
                  "by git ls-remote at 2026-10-27T21:43:03Z")
    s250_bytes = S231_FETCH.read_bytes()
    out["s250"] = {
        "row_claims": "7bb48f213ac677f943d5c791199ed3dddf302f00 resolves in mistralai/mistral-vibe, not badlogic/pi-mono",
        "hash": "7bb48f213ac677f943d5c791199ed3dddf302f00",
        "repo": "mistralai/mistral-vibe",
        "evidence_live_at": {
            "S231.fetch.json.url": s231.get("url"),
            "S231.fetch.json.note": s231.get("note"),
            "S231.fetch.json.sha256": s231.get("sha256"),
            "S231.fetch.json.bytes": s231.get("bytes"),
            "S230.fetch.json.note": s230.get("note"),
        },
        "quote_candidate": s250_quote,
        "quote_words": len(s250_quote.split()),
        "quote_raw_occurrences_in_S231.fetch.json": repeated(s250_bytes, s250_quote),
        "quote_raw_occurrences_in_S230.fetch.json": repeated(S230_FETCH.read_bytes(), s250_quote),
        "vibe_lsremote": VIBE_LS.read_text().strip().splitlines() if VIBE_LS.exists() else None,
        "pi_lsremote": PI_LS.read_text().strip().splitlines() if PI_LS.exists() else None,
        "e03_manifest": json.loads(E03_MANIFEST.read_text()) if E03_MANIFEST.exists() else None,
        "hash_present_in_S230_snapshot": repeated(S230_SNAP.read_bytes(),
                                                  "7bb48f213ac677f943d5c791199ed3dddf302f00"),
        "hash_in_pi_snapshot": repeated(S230_SNAP.read_bytes(),
                                        "7bb48f213ac677f943d5c791199ed3dddf302f00"),
    }

    # ---------------- S230 audit row ----------------
    s230_raw = S230_SNAP.read_bytes()
    q230 = "Experimental pre-approved tool list"
    out["s230_audit"] = {
        "row_quote": q230,
        "snapshot": str(S230_SNAP),
        "bytes": len(s230_raw),
        "sha256": hashlib.sha256(s230_raw).hexdigest(),
        "raw_line": raw_locate(s230_raw, q230)[0],
        "raw_byte": raw_locate(s230_raw, q230)[1],
        "raw_occurrences": repeated(s230_raw, q230),
    }
    # SOURCES rows as landed (S249/S250 may be absent at read time)
    src = SOURCES.read_text()
    out["sources_rows"] = {
        "S248_line": next((i + 1 for i, l in enumerate(src.splitlines())
                           if l.startswith("| S248 ")), None),
        "S249_line": next((i + 1 for i, l in enumerate(src.splitlines())
                           if l.startswith("| S249 ")), None),
        "S250_line": next((i + 1 for i, l in enumerate(src.splitlines())
                           if l.startswith("| S250 ")), None),
    }
    print(json.dumps(out, indent=1))
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
