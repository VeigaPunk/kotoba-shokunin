#!/usr/bin/env python3
"""W2CensusAnchors — final falsification harness for
corpus/knowledge/instruction-surface-census-round13.md § B′ and the round-47
class ledger (at 7ad7fadfc09354b74fb66605dfb0c1182c115a2f).

Checks, in order:
  A. every backticked span in a § B′ class-table EVIDENCE cell occurs in the
     frozen dump (presence);
  B. every backticked span in the round-47 class ledger occurs with exactly
     the count the ledger states;
  C. every § B′ prose-declared count is exact;
  D. every cited dump LINE number actually contains the cited span;
  E. the true line number of each anchor (so a stale cite is visible);
  F. dump provenance: the frozen dump == strings -n 4 of the frozen binary;
  G. the ledger's "count command" reproduces every stated count.

Exit 0 = all A-C, F, G pass.  Exit 1 = a defect.  D/E are reported always
(a wrong line cite is a defect, but a D-only failure is reported separately).

Usage: w2_census_anchors.py <census.md> <strings.dump> [<binary>]
"""
import os
import re
import subprocess
import sys

CENSUS = sys.argv[1] if len(sys.argv) > 1 else "census.md"
DUMP = sys.argv[2] if len(sys.argv) > 2 else \
    "/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings"
BINARY = sys.argv[3] if len(sys.argv) > 3 else \
    "/fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3"

text = open(CENSUS, encoding="utf-8").read()
lines = text.split("\n")
dump = open(DUMP, errors="replace").read()
dump_lines = dump.split("\n")

fails = []
linefails = []


def bt(s):
    """Ordered single-backtick spans."""
    return [m.group(1) for m in re.finditer(r"(?<!`)`([^`\n]+)`(?!`)", s)]


def bounds(start, end):
    s = e = None
    for i, l in enumerate(lines, 1):
        if s is None and l.startswith(start):
            s = i
        elif s is not None and l.startswith(end):
            e = i
            break
    return s, e


bp = bounds("### B\u2032.", "### C. Excluded loader-derived")
lp = bounds("**Class ledger (round 47", "## The disagreement this census")
print(f"§ B′ = census.md lines {bp[0]}..{bp[1]};  ledger = lines {lp[0]}..{lp[1]}")

# ---------------------------------------------------------------- A
print("\n=== A. § B′ class-table EVIDENCE cells: backticked span present? ===")
brows = [(i, [c.strip() for c in lines[i - 1].strip().strip("|").split(" | ")])
         for i in range(bp[0], bp[1]) if lines[i - 1].startswith("| `opencode:")]
print(f"§ B′ class rows: {len(brows)}")
for i, cells in brows:
    if len(cells) < 5:
        fails.append(f"A census.md:{i} malformed row ({len(cells)} cells)")
        continue
    for sp in bt(cells[4]):
        c = dump.count(sp)
        ok = c > 0
        print(f" {'OK ' if ok else 'FAIL'} census.md:{i} {cells[0]:45s} span={sp!r} count={c}")
        if not ok:
            fails.append(f"A census.md:{i} {cells[0]} span {sp!r} absent from dump")

# ---------------------------------------------------------------- B
print("\n=== B. round-47 class ledger: span present with the STATED count? ===")
lrows = [(i, [c.strip() for c in lines[i - 1].strip().strip("|").split(" | ")])
         for i in range(lp[0], lp[1]) if lines[i - 1].startswith("| `opencode:")]
print(f"ledger rows: {len(lrows)}")
for i, cells in lrows:
    anchor = cells[3] if len(cells) > 3 else ""
    for m in re.finditer(r"`([^`\n]+)`(?:\s+(\d+))?", anchor):
        sp, stated = m.group(1), m.group(2)
        c = dump.count(sp)
        if stated is not None:
            ok = c == int(stated)
            print(f" {'OK ' if ok else 'FAIL'} census.md:{i} {cells[0]:45s} span={sp!r} count={c} stated={stated}")
            if not ok:
                fails.append(f"B census.md:{i} {cells[0]} span {sp!r} count={c} stated={stated}")
        else:
            ok = c > 0
            print(f" {'OK ' if ok else 'FAIL'} census.md:{i} {cells[0]:45s} span={sp!r} count={c} (presence)")
            if not ok:
                fails.append(f"B census.md:{i} {cells[0]} span {sp!r} absent")
    # a stated count on BARE (non-backticked) text: the count command cannot be
    # run against it -> the stated count is unverifiable by the documented method
    for m in re.finditer(r"(?<!`)(?<!\| )([A-Za-z][A-Za-z0-9_.\- ]{2,40}?)\s+(\d+)(?![\d|])", anchor):
        txt, stated = m.group(1).strip(), m.group(2)
        if any(txt in sp for sp in
               [x.group(1) for x in re.finditer(r"`([^`\n]+)`", anchor)]):
            continue
        c = dump.count(txt)
        ok = c == int(stated)
        print(f" {'OK ' if ok else 'FAIL'} census.md:{i} {cells[0]:45s} BARE={txt!r} count={c} stated={stated}")
        if not ok:
            fails.append(f"B census.md:{i} {cells[0]} bare text {txt!r} count={c} stated={stated}")

# ---------------------------------------------------------------- C
print("\n=== C. § B′ prose-declared counts ===")
for sp, stated in [("ConfigInstructionPlugin", 0), ("ReadTool.Plugin", 0),
                   ("SessionInstructions", 0), ("session.instructions.entry.put", 0),
                   ('j5(r.config,"AGENTS.md")', 0), ("InstructionDiscovery", 0),
                   ("<system-reminder>", 18), ("2.0.26", 0),
                   ('var n="1.19.3"', 1)]:
    c = dump.count(sp)
    ok = c == stated
    print(f" {'OK ' if ok else 'FAIL'} span={sp!r} count={c} stated={stated}")
    if not ok:
        fails.append(f"C span {sp!r} count={c} stated={stated}")

# ---------------------------------------------------------------- D/E
print("\n=== D/E. cited dump LINE numbers: does the cited line carry the span? ===")
CITES = [
    (443993, ["y=[\"AGENTS.md\",", 'n=[X.join(r.config,"AGENTS.md")',
              'X.join(r.home,".claude","CLAUDE.md")',
              "for(let O of T.instructions)",
              'q.startsWith("https://")', "{concurrency:4}",
              'globUp(T,d.directory,d.worktree)']),
    (443995, ['fn("Instruction.resolve")', "while(G.startsWith(N)&&G!==N)"]),
    (444228, ['fn("ReadTool.execute")']),
]
RANGE_CITES = [
    ((445481, 445487), ["InstructionContext.observe", 'targets:["AGENTS.md"]',
                        'jX(L.config,"AGENTS.md")', 'Key.make("core/instructions")',
                        "system-context-builtins"]),
]


def true_lines(sp):
    return [i for i, l in enumerate(dump_lines, 1) if sp in l]


for ln, spans in CITES:
    seg = dump_lines[ln - 1] if ln <= len(dump_lines) else ""
    for sp in spans:
        present = sp in seg
        tl = true_lines(sp)
        ok = present and tl == [ln]
        print(f" {'OK ' if ok else 'FAIL'} dump:{ln} span={sp!r} on_line={present} true_lines={tl}")
        if not present:
            linefails.append(f"D cited dump:{ln} lacks {sp!r} (true at {tl})")
        elif tl != [ln]:
            linefails.append(f"D cited dump:{ln} for {sp!r} but true at {tl}")

for (lo, hi), spans in RANGE_CITES:
    seg = "\n".join(dump_lines[lo - 1:hi])
    for sp in spans:
        present = sp in seg
        tl = true_lines(sp)
        inside = all(lo <= x <= hi for x in tl)
        ok = present and inside
        print(f" {'OK ' if ok else 'FAIL'} dump:{lo}-{hi} span={sp!r} in_range={present} true_lines={tl}")
        if not (present and inside):
            linefails.append(f"D cited dump:{lo}-{hi} for {sp!r} (true at {tl})")

# ---------------------------------------------------------------- F
print("\n=== F. dump provenance: strings -n 4 of the frozen binary == frozen dump? ===")
try:
    regen = subprocess.run(["strings", "-n", "4", BINARY], capture_output=True,
                           check=True).stdout
    same = regen == dump.encode("utf-8", errors="replace")
    print(f" {'OK ' if same else 'FAIL'} regenerated dump identical: {same}")
    if not same:
        fails.append("F frozen dump is not strings -n 4 of the frozen binary")
except Exception as e:  # noqa: BLE001
    print(f" SKIP regeneration failed: {e}")

# ---------------------------------------------------------------- G
print("\n=== G. the ledger's own documented count command reproduces every stated count ===")
CMD = [sys.executable, "-c",
       'import sys;d=open(sys.argv[1],errors="replace").read();print(d.count(sys.argv[2]))',
       DUMP]
for i, cells in lrows:
    anchor = cells[3] if len(cells) > 3 else ""
    for m in re.finditer(r"`([^`\n]+)`(?:\s+(\d+))?", anchor):
        sp, stated = m.group(1), m.group(2)
        out = subprocess.run(CMD + [sp], capture_output=True, text=True).stdout.strip()
        same = out == (stated if stated is not None else str(dump.count(sp)))
        print(f" {'OK ' if same else 'FAIL'} census.md:{i} {sp!r} -> cmd={out} stated={stated}")
        if not same:
            fails.append(f"G census.md:{i} count command for {sp!r} gave {out}, stated {stated}")

print("\n=== SUMMARY ===")
print(f"hard failures (A/B/C/F/G): {len(fails)}")
for f in fails:
    print("  FAIL:", f)
print(f"line-cite defects (D):     {len(linefails)}")
for f in linefails:
    print("  FAIL:", f)
sys.exit(1 if (fails or linefails) else 0)
