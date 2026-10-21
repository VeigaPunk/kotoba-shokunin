#!/usr/bin/env python3
"""W2CensusAnchors — ledger anchor DISCRIMINATING-POWER analysis.

For every anchor the round-47 class ledger states, ask: if the class's own
subsystem were deleted from the dump, would the stated count change?

Method: the dump is a list of `strings -n 4` lines.  For each anchor we
(a) count its hits, (b) attribute each hit to a dump line, and (c) report
whether the anchor is (i) a literal, (ii) prose that cannot occur, and
(iii) shared across several subsystems.

The second column is what the ledger's own documented count command
(census.md:305-307) returns.

Usage: w2_ledger_power.py <census.md> <strings.dump>
"""
import re
import sys

CENSUS, DUMP = sys.argv[1], sys.argv[2]
lines = open(CENSUS, encoding="utf-8").read().split("\n")
dump = open(DUMP, errors="replace").read()
dump_lines = dump.split("\n")

lp = None
for i, l in enumerate(lines, 1):
    if l.startswith("**Class ledger (round 47"):
        lp = i
        break

rows = []
for i in range(lp, lp + 20):
    l = lines[i - 1]
    if not l.startswith("| `opencode:"):
        continue
    cells = [c.strip() for c in l.strip().strip("|").split(" | ")]
    rows.append((i, cells[0], cells[3]))

# The subsystem that owns each anchor, as a dump-line predicate.  The four
# opencode instruction subsystems live on these dump lines:
#   443993  @opencode/Instruction service (priority list y, config list n,
#            Instruction.systemPaths, Instruction.system  <- remote fetch)
#   443995  Instruction.find / Instruction.resolve (read hook)
#   444228  ReadTool.execute  (caller of the read hook)
#   445481-445487  instruction-context (2nd subsystem) + system-context-builtins
#   606940  generated client SDK (instructions:{entry:{list:...}})
SUB = {
    "443993": "Instruction service (priority list y / config list n / systemPaths / system)",
    "443995": "Instruction.find + Instruction.resolve (read hook)",
    "444228": "ReadTool.execute (read-hook caller)",
    "445481-445487": "instruction-context (2nd subsystem) + system-context-builtins",
    "606940": "generated client SDK",
}

print(f"{'row':>4} {'id':42s} {'anchor':46s} {'stated':>6} {'actual':>6}  "
      f"literal  subsystems-hit")
print("-" * 150)
for i, cid, anchor in rows:
    found = list(re.finditer(r"`([^`\n]+)`(?:\s+(\d+))?", anchor))
    if not found:
        m = re.search(r"([A-Za-z][A-Za-z0-9_.\- ]{2,40}?)\s+(\d+)\s*$", anchor)
        sp, st = (m.group(1).strip(), int(m.group(2))) if m else (anchor, None)
        literal = "NO(prose)"
    else:
        sp, st = found[0].group(1), (int(found[0].group(2)) if found[0].group(2) else None)
        literal = "yes" if sp in dump else "NO(vacuous)"
    actual = dump.count(sp)
    hit_lines = [n for n, l in enumerate(dump_lines, 1) if sp in l]
    subs = sorted({SUB.get(str(n), f"line {n}") for n in hit_lines})
    if not subs:
        subs = ["(none)"]
    print(f"{i:>4} {cid:42s} {sp!r:46s} {str(st):>6} {actual:>6}  "
          f"{literal:8s} {subs}")

print()
print("=== anchors that CANNOT decide their verdict (shared or non-literal) ===")
for i, cid, anchor in rows:
    found = list(re.finditer(r"`([^`\n]+)`(?:\s+(\d+))?", anchor))
    if found:
        sp = found[0].group(1)
        st = int(found[0].group(2)) if found[0].group(2) else None
    else:
        m = re.search(r"([A-Za-z][A-Za-z0-9_.\- ]{2,40}?)\s+(\d+)\s*$", anchor)
        sp, st = (m.group(1).strip(), int(m.group(2))) if m else (anchor, None)
    hit_lines = [n for n, l in enumerate(dump_lines, 1) if sp in l]
    subs = {SUB.get(str(n), f"line {n}") for n in hit_lines}
    if sp not in dump:
        print(f"  census.md:{i} {cid}: anchor {sp!r} occurs 0 times "
              f"(stated {st}) -> the count command returns {dump.count(sp)}, "
              f"NOT the stated {st}; anchor is not a literal in the dump")
    elif len(subs) > 1:
        print(f"  census.md:{i} {cid}: anchor {sp!r} (stated {st}) is shared by "
              f"{len(subs)} subsystems: {sorted(subs)}")
    elif st is not None and dump.count(sp) != st:
        print(f"  census.md:{i} {cid}: anchor {sp!r} stated {st} actual {dump.count(sp)}")
