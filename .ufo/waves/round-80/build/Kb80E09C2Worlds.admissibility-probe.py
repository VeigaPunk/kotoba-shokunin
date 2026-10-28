#!/usr/bin/env python3
"""Exhaustive admissibility probe over the six REAL committed snapshots.

For every surface this enumerates EVERY 5..25-word window of the snapshot's
text view that carries both the key token `allowed-tools` and the surface's
frozen page token, and reports the counter's own Q70 verdict for each.  It
also tests the located quotes the corpus's own SOURCES.md rows carry.
"""
import importlib.util, subprocess, re

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
REV = "398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93"
COUNTER = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/check_allowed_tools.py"

spec = importlib.util.spec_from_file_location("cat", COUNTER)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

SNAPS = {"spec": "S226-spec.md", "claude": "S227-claude.md",
         "factory": "S228-factory.md", "msaf": "S229-msaf.html",
         "pi": "S230-pi.md", "vibe": "S231-vibe.md"}


def blob(p):
    return subprocess.run(["git", "-C", LANE, "show", f"{REV}:{p}"],
                          capture_output=True).stdout


def all_windows(lines, tok, ground, lo=5, hi=25):
    """Every window of `lines` (contiguous, whitespace-collapsed) carrying
    both tokens, with the line index where the window starts."""
    joined = " ".join(lines)
    # line index of each character position
    starts = []
    off = 0
    for i, l in enumerate(lines):
        starts.append(off)
        off += len(l) + 1
    words = []
    wpos = []
    idx = 0
    for i, l in enumerate(lines):
        for w in l.split():
            words.append(w)
            wpos.append(i)
    out = []
    n = len(words)
    for i in range(n):
        for j in range(i + lo - 1, min(n, i + hi)):
            cand = " ".join(words[i:j + 1])
            if not re.search(r"(?<![A-Za-z0-9_])allowed-tools(?![A-Za-z0-9_])",
                             cand):
                continue
            if not re.search(r"(?<![A-Za-z0-9_])" + re.escape(ground)
                             + r"(?![A-Za-z0-9_])", cand, re.I):
                continue
            out.append((wpos[i], cand))
    return out


views = {}
for k, name in SNAPS.items():
    raw = blob(".ufo/waves/round-79/snapshots/" + name).decode("utf-8", "replace")
    views[k] = m.text_view(name, raw)

print("=== per-surface: every admissible window, and the Q70 verdict ===")
for k, sp in m.SURFACES.items():
    name = SNAPS[k]
    lines = views[k]
    fh = next((i for i, l in enumerate(lines) if l.startswith("#")), None)
    print(f"\n--- {k}  ({name})  first '#'-line in view = {fh} "
          f"({(lines[fh][:60] if fh is not None else None)!r})")
    wins = all_windows(lines, "allowed-tools", sp["page_token"])
    if not wins:
        print("    NO 5..25-word window carries both tokens")
        continue
    ok_lines = []
    bad = {}
    for line_idx, cand in wins:
        ok, why = m.quote_location(lines, cand)
        if ok:
            ok_lines.append((line_idx, cand))
        else:
            bad.setdefault(why, []).append((line_idx, cand))
    print(f"    {len(wins)} candidate windows; "
          f"{len(ok_lines)} pass Q70, {len(wins) - len(ok_lines)} fail")
    for why, lst in bad.items():
        idxs = sorted({i for i, _ in lst})
        print(f"    FAIL {why!r}: {len(lst)} windows, start lines {idxs[:10]}")
    for line_idx, cand in ok_lines[:4]:
        shared = [o for o, ol in views.items()
                  if o != k and any(cand in l for l in ol)]
        print(f"    OK  line {line_idx}: {cand[:110]!r}  shared={shared}")

print("\n=== the corpus SOURCES.md located quotes, tested ===")
src = blob("corpus/SOURCES.md").decode("utf-8", "replace")
for line in src.splitlines():
    mq = re.search(r"located quote \"(.*?)\"", line)
    if not mq:
        continue
    sid = line.split("|")[1].strip()
    if sid not in ("S226", "S227", "S228", "S229", "S230", "S231"):
        continue
    q = mq.group(1)
    key = {"S226": "spec", "S227": "claude", "S228": "factory",
           "S229": "msaf", "S230": "pi", "S231": "vibe"}[sid]
    lines = views[key]
    # the counter matches the quote as written, then once with backticks gone
    cands = []
    for c in (q, q.replace("`", "")):
        c = m.ws(c)
        if c and c not in cands:
            cands.append(c)
    hit = None
    for c in cands:
        ok, why = m.quote_location(lines, c)
        if ok:
            hit = (c, why)
            break
        hit = hit or (None, why)
    wcount = len(m.ws(q).split())
    print(f"  {sid} ({key}): {wcount} words; "
          f"Q70 -> {'OK' if hit[0] else 'FAIL'} {hit[1]!r}")
    print(f"      quote: {q[:120]!r}")

print("\n=== the r79 draft counter's OWN generator world on the real bytes ===")
print("(script_only_world reads the measured rev's registry + snapshots;")
print(" the round-80 draft above still writes SCRIPT_LABEL='unstated' for")
print(" every row, so its generator world cannot exceed 1 of 6.)")
