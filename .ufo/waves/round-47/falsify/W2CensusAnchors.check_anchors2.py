#!/usr/bin/env python3
"""P-A refined: (1) every backticked span in a § B′ EVIDENCE CELL and in the
round-47 class ledger, with the count the ledger states; (2) the cited dump
line numbers actually contain the cited anchors.

Usage: check_anchors2.py <census.md> <strings.dump>
Exit 0 = all pass.
"""
import re
import sys

CENSUS = sys.argv[1]
DUMP = sys.argv[2]
text = open(CENSUS, encoding="utf-8").read()
dump = open(DUMP, errors="replace").read()
dump_lines = dump.split("\n")
lines = text.split("\n")

fails = []
notes = []


def bt(s):
    return [m.group(1) for m in re.finditer(r"(?<!`)`([^`\n]+)`(?!`)", s)]


# ---- locate sections ----
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

print(f"§ B′ = lines {bp[0]}..{bp[1]};  ledger = lines {lp[0]}..{lp[1]}")

# ================= PART 1: § B′ evidence cells =================
print("\n===== PART 1: § B′ class-table evidence cells =====")
brows = []
for i in range(bp[0], bp[1]):
    l = lines[i - 1]
    if l.startswith("| `opencode:"):
        cells = [c.strip() for c in l.strip().strip("|").split(" | ")]
        brows.append((i, cells))
for i, cells in brows:
    evid = cells[4]
    spans = bt(evid)
    for sp in spans:
        c = dump.count(sp)
        # the census cites a dump line for some; extract "dump NNNN"
        m = re.search(r"dump (\d+)(?:-(\d+))?", evid)
        status = "OK " if c > 0 else "FAIL"
        if c == 0:
            fails.append(f"B′ evidence census.md:{i} span {sp!r} count=0")
        print(f" {status} census.md:{i} id={cells[0]} span={sp!r} count={c}")
    # dump line citation check
    m = re.search(r"dump (\d+)(?:-(\d+))?", evid)
    if m:
        lo = int(m.group(1))
        hi = int(m.group(2)) if m.group(2) else lo
        seg = "\n".join(dump_lines[lo - 1:hi])
        for sp in spans:
            if sp.startswith("dump") or sp.startswith("/") or sp.startswith("~"):
                continue
            if sp in seg:
                print(f"      OK  dump:{lo}{'-'+str(hi) if m.group(2) else ''} contains {sp!r}")
            else:
                # try shorter prefix for code anchors
                print(f"      ??  dump:{lo}{'-'+str(hi) if m.group(2) else ''} does NOT contain {sp!r}")
                fails.append(
                    f"B′ census.md:{i}: cited dump line {lo} does not contain {sp!r}")

# ================= PART 2: ledger =================
print("\n===== PART 2: round-47 class ledger =====")
lrows = []
for i in range(lp[0], lp[1]):
    l = lines[i - 1]
    if l.startswith("| `opencode:"):
        cells = [c.strip() for c in l.strip().strip("|").split(" | ")]
        lrows.append((i, cells))
print(f"ledger rows: {len(lrows)}")
for i, cells in lrows:
    anchor = cells[3]
    # pair: `span` followed by optional count N
    found = False
    for m in re.finditer(r"`([^`\n]+)`(?:\s+(\d+))?", anchor):
        sp, stated = m.group(1), m.group(2)
        c = dump.count(sp)
        found = True
        if stated is not None:
            ok = c == int(stated)
            print(f" {'OK ' if ok else 'FAIL'} census.md:{i} {cells[0]} span={sp!r} count={c} stated={stated}")
            if not ok:
                fails.append(f"ledger census.md:{i} {cells[0]} span {sp!r} count={c} stated {stated}")
        else:
            ok = c > 0
            print(f" {'OK ' if ok else 'FAIL'} census.md:{i} {cells[0]} span={sp!r} count={c} (presence only)")
            if not ok:
                fails.append(f"ledger census.md:{i} {cells[0]} span {sp!r} count=0")
    # bare "text N" counts with no backticks
    bare = re.findall(r"(?<!`)\b([A-Za-z][A-Za-z0-9_ .\-]{2,60}?)\s+(\d+)\b(?!\s*\|)", anchor)
    for txt, stated in bare:
        if any(txt.strip() in sp for sp, _ in [(m.group(1), None) for m in re.finditer(r"`([^`\n]+)`", anchor)]):
            continue
        c = dump.count(txt.strip())
        ok = c == int(stated)
        print(f" {'OK ' if ok else 'FAIL'} census.md:{i} {cells[0]} BARE-text={txt.strip()!r} count={c} stated={stated}")
        if not ok:
            fails.append(f"ledger census.md:{i} {cells[0]} bare text {txt.strip()!r} count={c} stated {stated}")

# ================= PART 3: declared prose counts in § B′ =================
print("\n===== PART 3: § B′ prose declared counts =====")
prose_counts = [
    ("ConfigInstructionPlugin", 0), ("ReadTool.Plugin", 0),
    ("SessionInstructions", 0), ("session.instructions.entry.put", 0),
    ('j5(r.config,"AGENTS.md")', 0), ("InstructionDiscovery", 0),
    ("<system-reminder>", 18), ("2.0.26", 0),
]
for sp, stated in prose_counts:
    c = dump.count(sp)
    ok = c == stated
    print(f" {'OK ' if ok else 'FAIL'} span={sp!r} count={c} stated={stated}")
    if not ok:
        fails.append(f"prose span {sp!r} count={c} stated {stated}")

# ================= PART 4: dump line citations =================
print("\n===== PART 4: cited dump line numbers =====")
cites = [
    (443993, ["y=[\"AGENTS.md\",", 'X.join(r.config,"AGENTS.md")',
              'X.join(r.home,".claude","CLAUDE.md")',
              "for(let O of T.instructions)",
              'q.startsWith("https://")']),
    (443995, ['fn("Instruction.resolve")', "while(G.startsWith(N)&&G!==N)"]),
    (444228, ['fn("ReadTool.execute")']),
    (445481, ["InstructionContext.observe", 'targets:["AGENTS.md"]']),
    (445487, ['Key.make("core/instructions")', "system-context-builtins"]),
]
for ln, spans in cites:
    if ln > len(dump_lines):
        print(f" FAIL dump:{ln} OUT OF RANGE (dump has {len(dump_lines)} lines)")
        fails.append(f"dump line {ln} out of range")
        continue
    seg = "\n".join(dump_lines[ln - 1:ln])
    for sp in spans:
        present = sp in seg
        # also search within a window of the cited line
        win = "\n".join(dump_lines[max(0, ln - 3):ln + 2])
        near = sp in win
        print(f" {'OK ' if present else ('~near' if near else 'FAIL')} dump:{ln} span={sp!r} present={present} near={near}")
        if not present:
            fails.append(f"dump:{ln} lacks {sp!r} (near={near})")

# ================= PART 5: where ARE the anchors? =================
print("\n===== PART 5: true line numbers of key anchors =====")
for sp in ['y=["AGENTS.md",', 'n=[X.join(r.config,"AGENTS.md")',
           'X.join(r.home,".claude","CLAUDE.md")', 'for(let O of T.instructions)',
           'q.startsWith("https://")', 'fn("Instruction.resolve")',
           'fn("ReadTool.execute")', "InstructionContext.observe",
           'Key.make("core/instructions")', "system-context-builtins",
           'jX(L.config,"AGENTS.md")', 'targets:["AGENTS.md"]',
           "disableClaudeCodePrompt", "CONTEXT.md", "Instructions from: ",
           'var n="1.19.3"']:
    hits = [i for i, l in enumerate(dump_lines, 1) if sp in l]
    print(f" {sp!r}: lines {hits[:8]} (total {len(hits)})")

print("\n===== SUMMARY =====")
print(f"failures: {len(fails)}")
for f in fails:
    print("  FAIL:", f)
sys.exit(1 if fails else 0)
