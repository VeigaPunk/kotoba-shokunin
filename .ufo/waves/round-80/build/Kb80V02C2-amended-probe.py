#!/usr/bin/env python3
"""Kb80V02C2 mechanism probe: r79-draft counter + 4 amendments, driven on a fixture.

Amendments (marked AMEND-1..4 below) are the reviewer's minimal fix set for the
round-80 predicate on real bytes; see .ufo/waves/round-80/w1/Kb80V02C2.md.
Usage: python3 -B Kb80V02C2-amended-probe.py <fixture-repo> <rev>
"""
import importlib.util, pathlib, re, sys

SRC = pathlib.Path(__file__).resolve().parent / "check_allowed_tools.py"
FIXTURE, REV = sys.argv[1], sys.argv[2]
src = SRC.read_text()

# AMEND-1: entry path
s = src.replace('ENTRY = "corpus/knowledge/allowed-tools-surfaces-round79.md"',
                'ENTRY = "corpus/knowledge/allowed-tools-surfaces-round80.md"')
assert s != src, "AMEND-1 anchor missing"
# AMEND-2: anchor fetch-record grammar as committed (date-only stamp, backticked hex)
old = 'r"fetched (\\d{4}-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ), HTTP 200, (\\d+) B, "\n    r"sha256 ([0-9a-f]{64})")'
new = 'r"fetched (\\d{4}-\\d\\d-\\d\\d(?:T\\d\\d:\\d\\d:\\d\\dZ)?), HTTP 200, (\\d+) B, "\n    r"sha256 `?([0-9a-f]{64})`?")'
assert old in src, "AMEND-2 anchor missing"
s = s.replace(old, new)
# AMEND-3: Q70 first-heading rule fires only when the page opens with its heading
old = "if first_head is not None and idx <= first_head + 1:"
assert old in src, "AMEND-3 anchor missing"
s = s.replace(old, "if first_head is not None and first_head <= 1 and idx <= first_head + 1:")
# AMEND-4: snapshot_name lifts names only from the row's (snapshot `X`) annotation
old = """            for tok in BACKTICK_RE.findall(line):
                base = tok.strip().split(":", 1)[0].strip().rsplit("/", 1)[-1]
                if base in man and base not in named:
                    named.append(base)"""
new = """            for m2 in re.finditer(r"\\(snapshot `([^`]+)`\\)", line):
                base = m2.group(1).strip().split(":", 1)[0].strip().rsplit("/", 1)[-1]
                if base in man and base not in named:
                    named.append(base)"""
assert old in src, "AMEND-4 anchor missing"
s = s.replace(old, new)

out = pathlib.Path(__file__).resolve().parent / "Kb80V02C2-amended-bytes.py"
out.write_text(s)

spec = importlib.util.spec_from_file_location("c2amended", out)
mod = importlib.util.module_from_spec(spec)
sys.modules["c2amended"] = mod
spec.loader.exec_module(mod)
repo = mod.Repo(pathlib.Path(FIXTURE).resolve(), REV)
n, findings, backed, opened = mod.check(repo)
print(f"AMENDED-PROBE N={n} backed={','.join(backed) or '-'} opened={opened}")
for f in findings:
    print(f"  note: {f}")
m, why = mod.script_only_world(repo)
print(f"script-only world M={m}")
print(f"held at base: {mod.held_at_base(repo)}")
ok = n == 6 and m < 5
print(f"reachability: {'N==6 reachable' if ok else 'NOT reachable'}")
sys.exit(0 if ok else 1)
